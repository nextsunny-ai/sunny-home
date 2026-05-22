---
name: Brand Intro — 디자인 가이드
description: 회사 소개·공식 프로필 톤. 크림 + 포스터·글래스 카드 + Fraunces serif.
version: 1.0
last_updated: 2026-05-22
---

# Brand Intro — 디자인 가이드

회사 공식 프로필 · 외부 소개 자료. 따뜻한 크림 톤 + Fraunces Display Serif + 포스터형 키비주얼.

## 폰트
- 디스플레이 = Fraunces (variable, weight 500, italic 변형 OK)
- 본문 = Pretendard Variable
- 모노 = JetBrains Mono

## 컬러
```
배경         #F5F2EB  (크림 오프화이트)
텍스트       #1A1A22  (차콜)
다크 카드    #1A1A22  (포스터 카드용)
hairline    rgba(26, 26, 34, 0.08)
muted        rgba(26, 26, 34, 0.55)
```

## 레이아웃
- 1920×1080 + 패딩 64px 80px
- 표지 = 좌 타이틀 + 우 다크 포스터 카드 (= 사진+텍스트 오버랩 위치)
- 본문 = 흰색 카드 + 다크 카드 페어
- 라운드 = 직각 (= 라운드 없음, 단정)

## 타이포
- Hero Title = Fraunces 500 · 96px · italic em 강조
- Section Title = Fraunces 500 · 56px
- Card Title = Fraunces 500 · 30~48px
- Body = Pretendard 400 · 15px · line-height 1.65

## 5장 패턴
1. 표지 — 좌 Hero Title + 서브 / 우 다크 포스터 카드 ("Key Visual")
2. Vision · Mission — 라이트 카드 + 다크 카드 페어
3. Core Business — 3 트랙 (라이브 + 전시 + 크리에이티브) 카드
4. Team — 4명 포트레이트 그리드 (= 빗금 placeholder)
5. 마무리 — 다크 포스터 ("Let's build the next stage") + 라이트 contact 카드

## 금기
- 그라디언트 X (= 단색만)
- 둥근 카드 X (= 직각)
- 이모지 X
- 영업 톤 X
- AI 슬롭 패턴

## 출력 형식
5장 stacked HTML.
