#!/usr/bin/env python3
"""써니홈 뉴스 자동 수집 — 8개 카테고리 Google News RSS + og:image 크롤링"""
import json, os, re, urllib.request, ssl
from datetime import datetime, timezone, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed

KST = timezone(timedelta(hours=9))
OUTPUT = os.path.join(os.path.dirname(__file__), "..", "sunny_home_data.json")

# SSL 검증 완화 (일부 뉴스 사이트 인증서 문제 대비)
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

CATEGORIES = [
    {"id": "ai", "name": "AI 트렌드", "queries": ["AI 에이전트", "AI 이미지 생성", "GPT 클로드"]},
    {"id": "content_ip", "name": "콘텐츠·IP", "queries": ["K웹툰 IP", "한국 콘텐츠 IP", "OTT 콘텐츠"]},
    {"id": "performance", "name": "공연", "queries": ["뮤지컬 공연 2026", "공연 페스티벌 서울"]},
    {"id": "exhibition", "name": "전시", "queries": ["미디어아트 전시", "현대미술 전시 서울"]},
    {"id": "grants", "name": "지원사업", "queries": ["KOCCA 지원사업", "문체부 콘텐츠 지원", "영상 콘텐츠 공모"]},
    {"id": "design", "name": "디자인", "queries": ["UI UX 디자인 트렌드 2026", "브랜딩 디자인"]},
    {"id": "festival", "name": "페스티벌", "queries": ["음악 페스티벌 2026 한국", "아트 페스티벌 서울"]},
    {"id": "english", "name": "비즈니스 영어", "queries": ["business english phrases", "English negotiation tips"]},
]


def fetch_og_image(url, timeout=8):
    """기사 URL에서 og:image 추출."""
    if not url or "google.com/rss" in url:
        return ""
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            # 처음 50KB만 읽기 (og:image는 <head> 안에 있으므로)
            html = r.read(50_000).decode("utf-8", errors="replace")
        # og:image
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', html, re.I)
        if m:
            img = m.group(1).strip()
            # 상대 URL 처리
            if img.startswith("//"):
                img = "https:" + img
            return img
    except Exception:
        pass
    return ""


def resolve_google_news_url(gnews_url, timeout=5):
    """Google News 리다이렉트 URL → 실제 기사 URL."""
    if "news.google.com" not in gnews_url:
        return gnews_url
    try:
        req = urllib.request.Request(gnews_url, headers=HEADERS, method="HEAD")
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            return r.url
    except Exception:
        # HEAD 실패 시 GET으로 리다이렉트 따라가기
        try:
            req = urllib.request.Request(gnews_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
                return r.url
        except Exception:
            pass
    return gnews_url


def fetch_google_news_rss(query, max_items=5):
    """Google News RSS 검색."""
    items = []
    url = f"https://news.google.com/rss/search?q={urllib.request.quote(query)}&hl=ko&gl=KR&ceid=KR:ko"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15, context=CTX) as r:
            text = r.read().decode("utf-8", errors="replace")
        for m in re.finditer(r"<item>(.*?)</item>", text, re.DOTALL):
            block = m.group(1)
            title_m = re.search(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", block)
            link_m = re.search(r"<link>(.*?)</link>", block)
            source_m = re.search(r"<source[^>]*>(.*?)</source>", block)
            date_m = re.search(r"<pubDate>(.*?)</pubDate>", block)
            if title_m:
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
        print(f"  [{query}] RSS failed: {e}")
    return items


def enrich_with_images(items):
    """병렬로 og:image 크롤링."""
    def _process(item):
        real_url = resolve_google_news_url(item["url"])
        if real_url != item["url"]:
            item["url"] = real_url
        item["image"] = fetch_og_image(real_url)
        return item

    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(_process, it): it for it in items}
        for f in as_completed(futures):
            try:
                f.result()
            except Exception:
                pass
    return items


def main():
    now = datetime.now(KST)
    categories = []

    for cat in CATEGORIES:
        all_items = []
        for q in cat["queries"]:
            items = fetch_google_news_rss(q, max_items=3)
            all_items.extend(items)
            print(f"  [{cat['id']}] '{q}' -> {len(items)}")

        # 중복 제거
        seen = set()
        unique = []
        for item in all_items:
            key = item["title"][:40]
            if key not in seen:
                seen.add(key)
                unique.append(item)
        unique = unique[:5]

        # og:image 크롤링
        print(f"  [{cat['id']}] fetching images for {len(unique)} items...")
        enrich_with_images(unique)
        img_count = sum(1 for it in unique if it["image"])
        print(f"  [{cat['id']}] -> {img_count}/{len(unique)} images found")

        categories.append({"id": cat["id"], "name": cat["name"], "items": unique})

    payload = {
        "updated": now.strftime("%Y-%m-%dT%H:%M:%S+09:00"),
        "categories": categories,
        "sources_definition": {},
    }

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    total = sum(len(c["items"]) for c in categories)
    total_img = sum(1 for c in categories for it in c["items"] if it["image"])
    print(f"\nDone: {total} news, {total_img} with images -> {OUTPUT}")


if __name__ == "__main__":
    main()
