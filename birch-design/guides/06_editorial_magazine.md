---
name: Editorial Magazine — 디자인 가이드
description: 화이트 + 부드러운 컬러 카드 + Display Serif. 잡지 톤. 광고 협업·아티스트.
version: 1.0
last_updated: 2026-05-22
---

# Editorial Magazine — 디자인 가이드

광고 협업·아티스트 프로파일·잡지 톤. 따뜻한 화이트 + Display Serif + 부드러운 컬러 카드.

---

## 폰트

- 디스플레이 = Fraunces (variable, weight 400~500, italic 변형 가능)
- 본문 = Pretendard Variable

## 컬러

```
배경        #F5F4F0  (따뜻한 베이지 화이트)
텍스트      #1A1A22
hairline    rgba(26, 26, 34, 0.12)
muted       rgba(26, 26, 34, 0.5)

카드 컬러 (= 부드러운 톤)
Mint         #C8E0D5
Mauve        #3E2F2F
Cream        #F0E6D2
Charcoal     #1A1A22
```

- 카드 배경 = 부드러운 컬러 1개씩
- 본문 텍스트 = 차콜 #1A1A22

## 레이아웃 (★ 이 톤만 둥근 카드 OK ★)

- 1920×1080 + 패딩 48px 56px
- **둥근 카드 = radius 20~24px** (= 이 톤의 시그니처. 다른 가이드 룰 X → 여기서만 예외)
- 비대칭 그리드 = `grid-template-columns: 1.4fr 1fr` + `grid-template-rows: auto 1fr`

## 타이포

| 요소 | 크기 | weight |
|---|---|---|
| Title Display | 64~80px | Fraunces 500 |
| em (italic) | 같음 | Fraunces 400 italic, color = muted |
| Section name | 32~36px | Fraunces 500 |
| Body | 13~14px | Pretendard 400 |
| Number marker | 200px | Fraunces 400 (= 섹션 번호 큰 마커) |
| Pill label | 11px | Pretendard 500 uppercase letter-spacing 0.18em |

## 카드 패턴

- **Title Card** (= 큰 카드) = white 배경 + Fraunces 큰 타이틀 + 우하단 원형 화살표 버튼 (`#1A1A22` 배경)
- **Section Mark** (= 다크 카드) = `#1A1A22` 배경 + 흰색 텍스트 + 큰 숫자 (200px Fraunces)
- **Stat 카드** (= 컬러 카드) = mint·mauve·cream 등 1개 + label + value

## 5장 패턴

1. **표지** — top pill ("WELCOME") + Title Card + Section Mark + Stat 2개
2. **목차** — 큰 Fraunces 헤딩 + 둥근 카드 리스트
3. **콘텐츠** — 매거진 그리드 = 큰 사진 placeholder + 텍스트 + 부드러운 카드
4. **데이터** — 차트 = 부드러운 컬러 면적 그래프 또는 = 컬러 카드 4개에 stat
5. **마무리** — 큰 Fraunces "Thank you." + contact

## 금기

- 그라디언트 (= 단색 컬러 카드만)
- 이모지 (= ⌃ ↗ 같은 ASCII 화살표만 OK)
- 5개 이상 컬러 (= mint·mauve·cream·charcoal 4개까지)
- 영업 톤
- AI 슬롭 (= 보라→핑크 그라디언트, 컬러 보더)

## 출력 형식

5장 stacked HTML. 둥근 카드 + Fraunces serif 일관.
