---
name: Dark Mono Report — 디자인 가이드
description: 다크 배경 보고서 톤. 노란 액센트, 모노스페이스 메타. Pretendard + JetBrains Mono.
version: 1.0
last_updated: 2026-05-22
---

# Dark Mono Report — 디자인 가이드

전략·투자자·경영진 대상 보고서. 다크 배경으로 무게감 · 모노스페이스 메타로 정밀한 데이터 톤.

---

## 폰트

- 본문 = Pretendard Variable
- 디스플레이 = Pretendard Variable (weight 700)
- 모노 = JetBrains Mono

## 컬러

```
배경        #0A0A0E
텍스트      #F5F5F7
액센트      #FFB800  (Amber — 단색)
hairline    rgba(255, 255, 255, 0.12)
muted       rgba(255, 255, 255, 0.5)
secondary   rgba(255, 255, 255, 0.65)
```

- `#000000` 절대 X — `#0A0A0E`로
- 흰 텍스트도 `#FFFFFF` 보단 `#F5F5F7` 권장
- 액센트 = Amber (`#FFB800`) 단색만

## 레이아웃

- 1920×1080 + 패딩 56px 80px
- top-bar · middle · bottom-bar 3단 그리드 (Simple Mono과 동일 구조)
- hairline = 흰색 12% 투명도

## 타이포

| 요소 | 크기 | weight | letter-spacing |
|---|---|---|---|
| Display Title | 88~120px | 700 | -0.04em |
| Section Heading | 48~56px | 700 | -0.02em |
| Subtitle | 22px | 400 | 0 |
| Body | 15~18px | 400 | 0 |
| Mono | 11~14px | 500 | 0.16em uppercase |

## 액센트 사용

- Amber (#FFB800) = 슬라이드당 1~2곳
- dot (8×8) / eyebrow line / 차트 강조 막대 / 마무리 eyebrow
- 라벨·delta 표시 (= 모노 + amber)

## 5장 패턴

1. **표지** — BIRCH SOUND · STRATEGY brand → 큰 타이틀 → 서브 → 메타
2. **목차** — Amber eyebrow → 큰 헤딩 → 리스트
3. **콘텐츠** — 좌측 헤딩 / 우측 bullet (bullet-num = amber)
4. **데이터** — stat 카드 4개 (라벨·값·delta = amber) + 차트 (강조 막대 = amber)
5. **마무리** — Amber eyebrow → "감사합니다." → contact

## 금기

- 그라디언트 (= 단색만)
- 이모지
- 둥근 카드 (= radius 0 또는 4px만)
- 흰색 = 순백 #FFF X · 검정 = 순흑 #000 X
- 영업 톤
- AI 슬롭 (= 네온 그라디언트, 컬러 코너 보더)

## 출력 형식

5장 stacked HTML — 동일 구조.
