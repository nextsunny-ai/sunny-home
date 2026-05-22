---
name: Color Block Business — 디자인 가이드
description: 컬러 블록 + 화살표 + 큰 영문 타이포. 피치덱·B2B 제안서 양식.
version: 1.0
last_updated: 2026-05-22
---

# Color Block Business — 디자인 가이드

피치덱·B2B 제안서 톤. 컬러 블록 + 화살표 모티프 + 큰 영문 디스플레이.

---

## 폰트

- 디스플레이 영문 = Inter (weight 800~900)
- 본문 = Pretendard Variable
- 모노 = JetBrains Mono

## 컬러

```
배경         #F5F4F0  (따뜻한 베이지 톤 화이트)
텍스트       #15151D
액센트       #FF6B1F  (Orange Block — 큰 면적 가능)
액센트 텍스트 #FFFFFF  (액센트 블록 위)
hairline     rgba(21, 21, 29, 0.15)
muted        rgba(21, 21, 29, 0.55)
```

- Orange Block (`#FF6B1F`) = **큰 면적 사용 OK** (= 통계 카드 배경, 좌측 사이드 블록 등)
- 다른 톤들과 달리 = 컬러 블록 패턴이 핵심
- 단, 그라디언트 X = 단색 블록만

## 레이아웃

- 1920×1080 + 패딩 56px 80px
- top-bar = 좌측 mark + brand · 우측 날짜
- mark = `4px × 18px` 오렌지 세로 막대
- middle = 그리드 1.3fr / 1fr (좌 타이틀 + 우 stat 카드)
- bottom-bar = 4 컬럼 메타

## 타이포

| 요소 | 크기 | weight |
|---|---|---|
| Display Title (영문) | 96~120px | 800 uppercase |
| Title accent (↗) | 같음 | 800, color = #FF6B1F |
| Subtitle | 18px | 400 |
| Stat value | 88px | 800 |
| Stat label | 11px | mono uppercase |

## 컬러 블록 패턴

- **사이드 블록** = 좌측 30% 너비 + Orange #FF6B1F + 흰색 텍스트
- **stat 카드** = 오렌지 배경 + 흰색 텍스트 + 우상단 화살표 (↗) 원형 보더
- **clip-path** 사용 = 카드 좌하단 모서리 깎기 (`polygon(0 0, 100% 0, 100% 100%, 24px 100%, 0 calc(100% - 24px))`) = 비대칭 모서리. 단, 둥근 X = 직각 깎기.

## 5장 패턴

1. **표지** — mark + brand → 큰 영문 타이틀 + ↗ accent → 우측 stat 카드 (Key Projects·245+)
2. **목차** — 좌측 큰 영문 "01·02·03·04" → 우측 항목명
3. **콘텐츠** — 좌측 사이드 블록 (오렌지) + 우측 본문 grid
4. **데이터** — 큰 stat 카드 3~4개 + 막대 차트 (강조 = 오렌지)
5. **마무리** — "LET'S BUILD" 등 큰 영문 → 사이드 블록 → contact

## 금기

- 그라디언트 (= 단색 오렌지만)
- 이모지
- 둥근 카드 (= 직각 또는 비대칭 모서리만)
- 화려한 일러스트
- 영업 톤 문구
- 오렌지 외 액센트 컬러

## 출력 형식

5장 stacked HTML.
