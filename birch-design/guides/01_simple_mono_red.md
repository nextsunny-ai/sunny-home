---
name: Simple Mono Red — 디자인 가이드
description: 회사 표준 보고서 톤. 붉은 액센트, hairline divider, 카드 기반. Pretendard + JetBrains Mono.
version: 1.0
last_updated: 2026-05-22
---

# Simple Mono Red — 디자인 가이드

이 파일을 Claude 또는 ChatGPT의 **Project Knowledge**에 업로드한 뒤, 그 프로젝트에서 PPT 콘텐츠 생성을 요청하면 이 톤이 일관되게 적용된다.

---

## 폰트

- **본문** = Pretendard Variable
- **디스플레이** = Pretendard Variable (weight 700~800)
- **모노** = JetBrains Mono (메타 정보·라벨·페이지 번호)
- system-ui / Inter / Roboto 등 디폴트 사용 금지
- Google Fonts CDN 또는 `cdn.jsdelivr.net/gh/orioncactus/pretendard` 사용

## 컬러

```
배경        #FAFAFA
텍스트      #0A0A0E
액센트      #E63329  (Red — 단색)
hairline    rgba(10, 10, 14, 0.08)
muted       rgba(10, 10, 14, 0.5)
secondary   rgba(10, 10, 14, 0.65)
```

- **`#FFFFFF` / `#000000` 절대 X** — 약간 따뜻한 톤으로 (`#FAFAFA` / `#0A0A0E`)
- 액센트 = 단색만, 그라디언트 X
- 한 슬라이드에 hue 1개 + 톤 변주 3~4단계까지만

## 레이아웃

- 슬라이드 = **1920 × 1080**
- 가장자리 패딩 = 56px 80px
- 그리드 = `top-bar (auto) / middle (1fr) / bottom-bar (auto)`
- top-bar = 좌측 brand · 우측 section-tag · 하단 1px hairline
- bottom-bar = 3 컬럼 메타 (Author·Reviewers·Date) · 상단 1px hairline

## 타이포

| 요소 | 크기 | weight | letter-spacing | line-height |
|---|---|---|---|---|
| Display Title | 88~120px | 700 | -0.04em | 1.0~1.05 |
| Section Heading | 48~56px | 700 | -0.02em | 1.1 |
| Subtitle | 22px | 400 | 0 | 1.55 |
| Body | 15~18px | 400 | 0 | 1.6 |
| Mono small | 11~14px | 500 | 0.16em | — uppercase |

## 액센트 사용 규칙

- 매 슬라이드 = 액센트 컬러 = **1~2 곳만**
- 보통 사용처:
  - 8px square dot (= 둥글지 않은 사각)
  - eyebrow 텍스트 (= mono small uppercase)
  - 차트의 현재 분기 막대 1개
  - 마무리 슬라이드의 eyebrow line
- 큰 컬러 블록 X · 배경 X · 그라디언트 X

## 슬라이드 5장 패턴

1. **표지 (Cover)** — brand → 큰 타이틀 → 서브타이틀 → 메타 (Author·Reviewers·Date)
2. **목차 (Contents)** — eyebrow "Contents · N sections" → 큰 헤딩 → 리스트 (toc-num·toc-title·toc-page)
3. **콘텐츠 (Content)** — 좌측 헤딩 + lead 문장 / 우측 bullet 리스트 (bullet-num·strong·small)
4. **데이터 (Data)** — 큰 헤딩 → 4 stat 카드 (라벨·값·delta) → 막대 차트
5. **마무리 (Closing)** — eyebrow → 큰 타이틀 "감사합니다." → 서브 → contact

## 금기 (절대 X)

- 그라디언트 (배경·텍스트·카드 모두)
- 이모지 (= 헤더·라벨·UI 어디서나)
- 둥근 카드 (= border-radius 0 또는 최대 4px만)
- 5개 이상 컬러 (= 단일 hue 유지)
- 영업·홍보·광고 톤 문구 ("Powerful·Beautiful·Premium·혁신적·새로운 ___을 만나다")
- AI 슬롭 패턴 (= 보라→핑크 그라디언트 · 컬러 코너 보더 · 이모지 헤더 · 카드 5개 이상)
- 사람 얼굴 stock 사진 (= 차라리 빈 placeholder)

## 출력 형식

- HTML 5장 = `<section class="slide cover-slide">` ~ `<section class="slide closing-slide">` 순서로 vertically stacked
- CSS = `<style>` 안에 임베디드
- 외부 폰트 = `@import url(...)` 사용
- 본문 사용 가능한 한국어 토큰 = 자유 (= 콘텐츠 자체는 사용자 주제대로)

## 자가 검토

- [ ] 그라디언트·이모지·둥근 카드 없음
- [ ] 액센트 컬러 = 슬라이드당 1~2 곳 이내
- [ ] hairline + 카드 패턴 일관
- [ ] 영업 톤 문구 없음
- [ ] 5장 풀세트 (표지·목차·콘텐츠·데이터·마무리)
- [ ] 1920×1080 비율 유지
