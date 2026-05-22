---
name: City Brand Light — 디자인 가이드
description: 라이트그레이 + 차콜 + 5컬러 도메인. 도시·문화·페스티벌 브랜드 톤.
version: 1.0
last_updated: 2026-05-22
---

# City Brand Light — 디자인 가이드

도시·문화·페스티벌 브랜드 발표용. 차분한 라이트그레이 베이스 + 다채로운 5색 글로우.

---

## 폰트

- 디스플레이 = Pretendard Variable (weight 800)
- 본문 = Pretendard Variable
- 모노 = Space Mono

## 컬러

```
배경         #F2F2F4  (라이트그레이)
텍스트       #1A1A22  (차콜)
hairline     rgba(26, 26, 34, 0.1)
muted        rgba(26, 26, 34, 0.55)

5색 도메인 (= 라이트 글로우용)
도메인 1     #FFB800   Amber
도메인 2     #F23A4E   Coral
도메인 3     #5BC4F5   Sky
도메인 4     #C6FF6F   Lime
도메인 5     #C77BFF   Violet
```

- 5색 = 우측 영역 다크 패널의 radial gradient용
- 좌측 본문 영역 = 단색 텍스트만
- `#FFFFFF` X · `#000000` X

## 레이아웃

- 1920×1080
- **좌우 분할** = 1fr 1fr 그리드 (= split layout)
- 좌측 = padding 64px + 본문 (brand·title·subtitle·meta)
- 우측 = 다크 차콜 (`#1A1A22`) + 5색 radial gradient blur(50px) 글로우 + 오버레이 라벨

## 타이포

| 요소 | 크기 | weight |
|---|---|---|
| Display Title | 80~96px | 800 |
| eyebrow | 13px | mono uppercase letter-spacing 0.16em |
| Subtitle | 18px | 400 |
| 우측 large num | 72px | 900 |
| 우측 label | 14px | mono uppercase letter-spacing 0.18em |

## 5색 글로우 사용

좌상단 30%·우측 60%·좌하단 80% 등 = 비대칭으로 radial gradient 5개 겹쳐서 blur 50px:

```css
background:
  radial-gradient(circle at 30% 30%, #FFB800 0%, transparent 18%),
  radial-gradient(circle at 70% 60%, #F23A4E 0%, transparent 22%),
  radial-gradient(circle at 45% 80%, #5BC4F5 0%, transparent 18%),
  radial-gradient(circle at 80% 25%, #C6FF6F 0%, transparent 15%),
  radial-gradient(circle at 20% 65%, #C77BFF 0%, transparent 16%);
filter: blur(50px);
```

## 5장 패턴

1. **표지** — 좌 brand + 큰 타이틀 + meta / 우 다크 + 5색 글로우 + "THE FIVE LIGHTS" 라벨
2. **목차** — 좌 헤딩 + 리스트 / 우 다크 패널 + 도메인 컬러 chip 5개
3. **콘텐츠** — 좌 헤딩 + bullet / 우 도메인 1색 강조 영역
4. **데이터** — 5색을 도메인별 데이터 시각화에 매핑
5. **마무리** — 좌 "THE FIVE LIGHTS" 큰 영문 / 우 다크 + contact

## 금기

- 5색 외 다른 컬러
- 그라디언트가 = 우측 글로우 외에 다른 곳 사용 X
- 둥근 카드 (= radius 0)
- 이모지
- 영업 톤

## 출력 형식

5장 stacked HTML.
