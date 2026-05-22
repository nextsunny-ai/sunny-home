---
name: Dark Digital Art — 디자인 가이드
description: 다크 + 네온 그라디언트. Display 타이포 + 글래스 칩. 디지털 아트·이머시브·뮤직.
version: 1.0
last_updated: 2026-05-22
---

# Dark Digital Art — 디자인 가이드

디지털 아트·이머시브·뮤직 프로젝트용. 다크 베이스 + 네온 그라디언트 + Display 타이포.

---

## 폰트

- 디스플레이 = Bricolage Grotesque (weight 800, opsz 96)
- 본문 = Pretendard Variable

## 컬러

```
배경         #0A0A12  (다크 블루-블랙)
텍스트       #FFFFFF
secondary    rgba(255, 255, 255, 0.65)
muted        rgba(255, 255, 255, 0.5)
hairline     rgba(255, 255, 255, 0.12)

네온 글로우 (= 배경에만)
Purple       #C77BFF
Mint         #5FEAAF
Pink         #FF5FA9
Sky          #5BC4F5
```

- 네온 = 배경 radial gradient에만 사용
- 텍스트 그라디언트 = 디스플레이 글리프(italic accent)만 OK
- 본문 텍스트 = 흰색·반투명 흰색만

## 레이아웃

- 1920×1080 + 패딩 56px 80px
- 그리드 = top-bar · middle · bottom-bar
- 배경 = 네온 radial gradient + 도트 그리드 패턴 (`background-image: radial-gradient(circle, rgba(255,255,255,0.05) 1px, transparent 1px), 40px 40px`)

## 타이포

| 요소 | 크기 | weight | letter-spacing |
|---|---|---|---|
| Hero Display | 96~140px | 800 (Bricolage) | -0.045em |
| Glyph italic | 같음 | 800 italic | 같음 |
| Section Heading | 48~64px | 700 | -0.02em |
| Body | 17~20px | 400 | 0 |
| chip | 12px | 500 | 0.05em |

## 디스플레이 + Glyph

```html
<h1 class="title">P<span class="glyph">o</span>rt<span class="glyph">a</span><br/>~ digit<span class="glyph">A</span>l art</h1>
```

```css
.glyph {
  font-style: italic;
  background: linear-gradient(135deg, #C77BFF 0%, #5FEAAF 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
```

## 글래스 칩

```css
.chip {
  padding: 8px 14px;
  border: 1px solid rgba(255,255,255,0.25);
  border-radius: 999px; /* ★ 이 톤에서만 둥근 칩 OK */
  color: rgba(255,255,255,0.8);
  backdrop-filter: blur(8px);
  background: rgba(255,255,255,0.04);
}
```

## 5장 패턴

1. **표지** — brand + 큰 Display Title (= glyph 강조) + subtitle + 글래스 칩
2. **목차** — 큰 헤딩 + 리스트 (= 네온 도트 강조)
3. **콘텐츠** — 좌 헤딩 + 우 시각화/이미지 placeholder
4. **데이터** — 큰 숫자 (= glyph 그라디언트) + 차트
5. **마무리** — 풀스크린 Display + 글래스 칩 contact

## 금기

- 라이트 모드 적용 (= 다크 베이스만)
- 카드 컨테이너 둥근 (= 칩만 둥근 OK / 카드는 radius 0)
- 영업 톤
- AI 슬롭 (= 너무 많은 네온 색상, 5개 이상 그라디언트 hue)
- 본문 텍스트 그라디언트

## 출력 형식

5장 stacked HTML. 네온 글로우 + 도트 그리드 배경 일관.
