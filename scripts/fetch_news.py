#!/usr/bin/env python3
"""써니홈 뉴스 자동 수집 — 8개 카테고리 RSS/Google News 크롤링 → sunny_home_data.json"""
import json, os, re, urllib.request
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))
OUTPUT = os.path.join(os.path.dirname(__file__), "..", "sunny_home_data.json")

CATEGORIES = [
    {
        "id": "ai",
        "name": "AI 트렌드",
        "queries": ["AI 에이전트", "AI 이미지 생성", "GPT 클로드"],
        "emoji": "🤖",
    },
    {
        "id": "content_ip",
        "name": "콘텐츠·IP",
        "queries": ["K웹툰 IP", "한국 콘텐츠 IP", "OTT 콘텐츠"],
        "emoji": "🎬",
    },
    {
        "id": "performance",
        "name": "공연",
        "queries": ["뮤지컬 공연 2026", "공연 페스티벌 서울"],
        "emoji": "🎭",
    },
    {
        "id": "exhibition",
        "name": "전시",
        "queries": ["미디어아트 전시", "현대미술 전시 서울"],
        "emoji": "🖼️",
    },
    {
        "id": "grants",
        "name": "지원사업",
        "queries": ["KOCCA 지원사업", "문체부 콘텐츠 지원", "영상 콘텐츠 공모"],
        "emoji": "📋",
    },
    {
        "id": "design",
        "name": "디자인",
        "queries": ["UI UX 디자인 트렌드 2026", "브랜딩 디자인"],
        "emoji": "✨",
    },
    {
        "id": "festival",
        "name": "페스티벌",
        "queries": ["음악 페스티벌 2026 한국", "아트 페스티벌 서울"],
        "emoji": "🎵",
    },
    {
        "id": "english",
        "name": "비즈니스 영어",
        "queries": ["business english phrases", "English negotiation tips"],
        "emoji": "🌐",
    },
]


def fetch_google_news_rss(query, max_items=5):
    """Google News RSS로 검색 결과 가져오기."""
    items = []
    url = f"https://news.google.com/rss/search?q={urllib.request.quote(query)}&hl=ko&gl=KR&ceid=KR:ko"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "SunnyHome-NewsBot/1.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            text = r.read().decode("utf-8", errors="replace")
        for m in re.finditer(r"<item>(.*?)</item>", text, re.DOTALL):
            block = m.group(1)
            title_m = re.search(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", block)
            link_m = re.search(r"<link>(.*?)</link>", block)
            source_m = re.search(r"<source[^>]*>(.*?)</source>", block)
            date_m = re.search(r"<pubDate>(.*?)</pubDate>", block)
            if title_m:
                # 날짜 파싱
                pub = ""
                if date_m:
                    try:
                        from email.utils import parsedate_to_datetime
                        dt = parsedate_to_datetime(date_m.group(1))
                        pub = dt.strftime("%Y-%m-%d")
                    except Exception:
                        pub = date_m.group(1)[:10]
                items.append({
                    "title": title_m.group(1).strip(),
                    "url": link_m.group(1).strip() if link_m else "",
                    "source": source_m.group(1).strip() if source_m else "",
                    "summary": "",
                    "published": pub,
                    "image": "",
                })
            if len(items) >= max_items:
                break
    except Exception as e:
        print(f"  [{query}] fetch failed: {e}")
    return items


def main():
    now = datetime.now(KST)
    categories = []

    for cat in CATEGORIES:
        all_items = []
        for q in cat["queries"]:
            items = fetch_google_news_rss(q, max_items=3)
            all_items.extend(items)
            print(f"  [{cat['id']}] '{q}' → {len(items)}건")

        # 중복 제거 (제목 앞 40자 기준)
        seen = set()
        unique = []
        for item in all_items:
            key = item["title"][:40]
            if key not in seen:
                seen.add(key)
                unique.append(item)

        categories.append({
            "id": cat["id"],
            "name": cat["name"],
            "items": unique[:5],
        })
        print(f"  → {cat['id']}: {len(unique)}건 (max 5)")

    payload = {
        "updated": now.strftime("%Y-%m-%dT%H:%M:%S+09:00"),
        "categories": categories,
        "sources_definition": {},
    }

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"\nSaved {sum(len(c['items']) for c in categories)} news items → {OUTPUT}")
    print(f"Updated: {payload['updated']}")


if __name__ == "__main__":
    main()
