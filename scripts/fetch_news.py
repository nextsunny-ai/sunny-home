#!/usr/bin/env python3
"""써니홈 뉴스 자동 수집 — 7개 카테고리 Google News RSS

핵심 설계 (2026-05-17 재작성, 테오):
- 누적 보존  : 기존 sunny_home_data.json 을 읽어 새 뉴스와 병합한다.
- 절대 안 사라짐: RSS 수집이 실패/0건이면 그 카테고리는 옛 데이터를 그대로 둔다.
- 읽을 시간 확보: 카테고리별 최근 KEEP_DAYS 일 · 최대 KEEP_MAX 개를 유지한다.
- 섹션 항상 보장: 모든 카테고리 키가 항상 존재한다 (items 가 비어도 키는 남는다).
- 영어는 분리   : 영어 학습은 data/english.json + 클라이언트 로테이션이 담당한다.
"""
import json
import os
import re
import ssl
import urllib.request
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

KST = timezone(timedelta(hours=9))
ROOT = os.path.join(os.path.dirname(__file__), "..")
OUTPUT = os.path.join(ROOT, "sunny_home_data.json")

KEEP_DAYS = 14   # 이 기간 안의 뉴스는 보존 (안 읽어도 안 사라짐)
KEEP_MAX = 30    # 카테고리당 최대 보관 수
MIN_KEEP = 5     # 14일이 넘어도 카테고리당 최소 이만큼은 남긴다 (빈 칸 방지)
PER_QUERY = 4    # 쿼리당 RSS 최대 수집 수

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; SunnyHome/2.0)"}

CATEGORIES = [
    {"id": "ai",          "name": "AI 트렌드", "queries": ["AI 에이전트", "클로드 Claude Anthropic", "AI 이미지 생성", "ChatGPT GPT"]},
    {"id": "content_ip",  "name": "콘텐츠·IP", "queries": ["K웹툰 IP", "한국 콘텐츠 IP", "OTT 콘텐츠"]},
    {"id": "performance", "name": "공연",      "queries": ["뮤지컬 공연 2026", "공연 페스티벌 서울"]},
    {"id": "exhibition",  "name": "전시",      "queries": ["미디어아트 전시", "현대미술 전시 서울"]},
    {"id": "grants",      "name": "지원사업",  "queries": ["KOCCA 지원사업", "문체부 콘텐츠 지원", "영상 콘텐츠 공모"]},
    {"id": "design",      "name": "디자인",    "queries": ["UI UX 디자인 트렌드 2026", "브랜딩 디자인"]},
    {"id": "festival",    "name": "페스티벌",  "queries": ["음악 페스티벌 2026 한국", "아트 페스티벌 서울"]},
]


def now_kst():
    return datetime.now(KST)


def iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%S+09:00")


def item_key(item):
    """병합용 식별자. URL 우선, 없으면 제목 앞부분."""
    url = (item.get("url") or "").strip()
    if url:
        return url
    return "t:" + (item.get("title") or "").strip()[:50]


def parse_seen(item):
    """first_seen → datetime. 없으면 published, 그것도 없으면 아주 오래전."""
    for field in ("first_seen", "published"):
        val = (item.get(field) or "").strip()
        if not val:
            continue
        for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%d"):
            try:
                dt = datetime.strptime(val, fmt)
                return dt if dt.tzinfo else dt.replace(tzinfo=KST)
            except ValueError:
                continue
    return datetime(2000, 1, 1, tzinfo=KST)


def fetch_google_news_rss(query, max_items=PER_QUERY):
    """Google News RSS 검색. 실패하면 빈 리스트 (예외를 위로 던지지 않는다)."""
    items = []
    url = (
        "https://news.google.com/rss/search?q="
        + urllib.request.quote(query)
        + "&hl=ko&gl=KR&ceid=KR:ko"
    )
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15, context=CTX) as resp:
            text = resp.read().decode("utf-8", errors="replace")
    except Exception as exc:  # noqa: BLE001 — 네트워크 실패는 조용히 빈 결과
        print(f"  [{query}] RSS failed: {exc}")
        return items

    for match in re.finditer(r"<item>(.*?)</item>", text, re.DOTALL):
        block = match.group(1)
        title_m = re.search(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", block)
        if not title_m:
            continue
        link_m = re.search(r"<link>(.*?)</link>", block)
        source_m = re.search(r"<source[^>]*>(.*?)</source>", block)
        date_m = re.search(r"<pubDate>(.*?)</pubDate>", block)
        published = ""
        if date_m:
            try:
                published = parsedate_to_datetime(date_m.group(1)).astimezone(KST).strftime("%Y-%m-%d")
            except Exception:  # noqa: BLE001
                published = date_m.group(1)[:10]
        items.append({
            "title": title_m.group(1).strip(),
            "url": link_m.group(1).strip() if link_m else "",
            "source": source_m.group(1).strip() if source_m else "",
            "summary": "",
            "published": published,
            "image": "",
        })
        if len(items) >= max_items:
            break
    return items


def load_existing():
    """기존 sunny_home_data.json. 없거나 깨졌으면 빈 구조."""
    try:
        with open(OUTPUT, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            return data
    except FileNotFoundError:
        pass
    except (json.JSONDecodeError, OSError) as exc:
        print(f"  [load] 기존 파일 무시: {exc}")
    return {}


def merge_category(old_items, fresh_items, stamp):
    """옛 뉴스 + 새 뉴스 병합. 옛 항목의 first_seen 은 보존, 새 항목엔 stamp 부여.

    반환: (merged_items, new_count)
    """
    by_key = {}
    order = []
    for it in old_items:
        key = item_key(it)
        if key not in by_key:
            by_key[key] = dict(it)
            order.append(key)

    new_count = 0
    for it in fresh_items:
        key = item_key(it)
        if key in by_key:
            continue  # 이미 본 뉴스 — first_seen 보존, 중복 추가 안 함
        rec = dict(it)
        rec["first_seen"] = stamp
        by_key[key] = rec
        order.append(key)
        new_count += 1

    merged = []
    for key in order:
        rec = by_key[key]
        rec.setdefault("first_seen", rec.get("published") or stamp)
        merged.append(rec)

    # 최신순 정렬 (first_seen 기준)
    merged.sort(key=parse_seen, reverse=True)

    # KEEP_DAYS 이내만 유지하되, 최소 MIN_KEEP 개는 무조건 남긴다 (빈 칸 방지)
    cutoff = now_kst() - timedelta(days=KEEP_DAYS)
    kept = [it for it in merged if parse_seen(it) >= cutoff]
    if len(kept) < MIN_KEEP:
        kept = merged[:MIN_KEEP]
    return kept[:KEEP_MAX], new_count


def main():
    existing = load_existing()
    old_by_id = {c.get("id"): c for c in existing.get("categories", []) if isinstance(c, dict)}
    stamp = iso(now_kst())

    categories = []
    total_new = 0
    total_kept = 0
    for cat in CATEGORIES:
        fresh = []
        for query in cat["queries"]:
            got = fetch_google_news_rss(query)
            fresh.extend(got)
            print(f"  [{cat['id']}] '{query}' -> {len(got)}")

        # 같은 회차 내 중복 제거
        seen, unique = set(), []
        for it in fresh:
            key = item_key(it)
            if key not in seen:
                seen.add(key)
                unique.append(it)

        old_items = old_by_id.get(cat["id"], {}).get("items", []) or []
        merged, new_count = merge_category(old_items, unique, stamp)

        if not unique and old_items:
            print(f"  -> {cat['id']}: RSS 0건 — 옛 데이터 {len(merged)}개 보존")
        else:
            print(f"  -> {cat['id']}: 신규 {new_count} / 총 {len(merged)}")

        categories.append({"id": cat["id"], "name": cat["name"], "items": merged})
        total_new += new_count
        total_kept += len(merged)

    payload = {
        "updated": stamp,
        "categories": categories,
        "sources_definition": existing.get("sources_definition", {}),
    }
    # 기존 weather 등 부가 데이터는 건드리지 않고 보존
    if "weather" in existing:
        payload["weather"] = existing["weather"]

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"\nDone: 신규 {total_new}건 / 보존 포함 총 {total_kept}건 -> {OUTPUT}")


if __name__ == "__main__":
    main()
