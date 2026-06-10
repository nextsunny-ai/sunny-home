---
name: Investor IR — 디자인 가이드
description: 라이트 배경 + 숫자·차트 중심 + 푸른 액센트. 투자자·시리즈 자료.
version: 1.0
last_updated: 2026-05-22
---

# Investor IR — 디자인 가이드

투자자 · IR · 시리즈 자료. 라이트 배경 (= 숫자 가독성) + 푸른 액센트 + 차트·표 중심.

## 폰트
- 본문 = Pretendard Variable
- 디스플레이 = Pretendard Variable (weight 700)
- 모노 = JetBrains Mono

## 컬러
```
배경         #FFFFFF
텍스트       #0A0A0E
다크 카드    #0A0A0E  (ARR · The Ask 강조용)
액센트       #1A4FD9  (Investor Blue — 단색)
delta+       #5BC4F5  (Sky — 긍정 변화)
hairline    rgba(10, 10, 14, 0.08)
muted        rgba(10, 10, 14, 0.55)
```

## 레이아웃
- 1920×1080 + 패딩 56px 80px
- 표지 = 큰 타이틀 + 우측 ARR 다크 카드 (= 즉시 임팩트)
- 본문 = 흰색 + hairline + 숫자 강조
- The Ask = 다크 카드 (= 클로징 임팩트)

## 타이포
- Hero Title = Pretendard 700 · 84px · letter-spacing -0.03em
- Section Heading = Pretendard 700 · 44px
- Stat Value = Pretendard 700 · 56~64px (= 숫자 큼)
- Body = Pretendard 400 · 15~18px
- Mono small = 10~13px · letter-spacing 0.16em uppercase

## 5장 패턴
1. 표지 — Hero Title + 서브 + 우측 ARR 다크 카드 (= 즉시 핵심 숫자)
2. 목차 — 4 sections (Market · Metrics · Revenue · Ask)
3. Metrics — 4 stat 카드 + 막대 차트 (= 강조 막대 = 푸른)
4. Revenue Architecture — 6 매출 스트림 표 (= NO · STREAM · CHANNEL · YoY · SHARE)
5. The Ask — 다크 카드 ("$ 12M Series A") + Use of Funds 라이트 카드

## 표·차트 룰
- 표 = 직각 hairline + header 박스 음영
- 차트 = 막대 1개만 강조 컬러 (= 현재 분기)
- forecast 막대 = opacity 0.3
- 숫자 = 단위 명확 ($M · % · pt · mo)

## 금기
- 그라디언트 X (= 단색만)
- 다크 배경 메인 X (= 라이트가 메인, 다크는 강조 카드만)
- 이모지 X
- 영업 톤 X
- "혁신적·놀라운·차세대" 형용사 X (= 숫자로 말함)

## 출력 형식
5장 stacked HTML.
