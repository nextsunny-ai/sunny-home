---
name: Tech Spec — 디자인 가이드
description: 기술 개발 기획서. 라이트 + 푸른 액센트 + 모노 디스플레이 + 아키텍처 다이어그램 + 코드 박스.
version: 1.0
last_updated: 2026-05-22
---

# Tech Spec — 디자인 가이드

기술 개발 기획서 · AR/VR · 앱 개발. 라이트 베이스 + 푸른 액센트 + 모노 디스플레이 + 다이어그램·코드 중심.

## 폰트
- 디스플레이 = JetBrains Mono (weight 600 · letter-spacing -0.05em)
- 본문 = Pretendard Variable
- 모노 = JetBrains Mono

## 컬러
```
배경         #FAFBFC  (= 매우 라이트 cool)
텍스트       #0A0A0E
다크 카드    #0A0A0E  (code · ship 카드용)
액센트       #1A6BFF  (Tech Blue — 단색)
code-key     #5BC4F5  (코드 키워드)
code-str     #C6FF6F  (문자열)
code-fn      #FFB800  (함수)
code-comment #6F7681  (주석)
hairline    rgba(10, 10, 14, 0.08)
```

## 레이아웃
- 1920×1080 + 패딩 56px 80px
- 표지 = 좌 모노 타이틀 + 우 다크 코드 카드
- 아키텍처 = 3 layer (Client → API → Data) + 화살표
- 스택 = 좌 카테고리·이름·버전 표 + 우 다크 코드 카드
- 마무리 = 다크 ship 카드 + 라이트 links 카드

## 타이포
- Hero Title = JetBrains Mono 600 · 88px · letter-spacing -0.05em
- Section Title = JetBrains Mono 600 · 44px
- Body = Pretendard 400 · 14~15px
- Code = JetBrains Mono 500 · 12~13px · line-height 1.7

## 시그니처 패턴
- **코드 카드** = 다크 #0A0A0E + 좌측 푸른 보더 3px + JetBrains Mono
- **아키텍처 박스** = 흰색 + hairline + 모노 텍스트 + 강조 1박스 (= 푸른)
- **화살표** = "↓ HTTPS · WebSocket" 식 mono 텍스트
- **eyebrow** = `> ` prefix (= 터미널 톤)
- **타이틀** = `build()`, `.deploy()`, `ship().success()` 식 함수 호출 톤

## 5장 패턴
1. 표지 — `build() .deploy()` + 한국어 부제 + 다크 코드 카드 (project.config)
2. 목차 — `// contents[]` + 4 sections
3. 아키텍처 — 3 layer 다이어그램 (Client · API · Data) + 화살표
4. Tech Stack — 좌 표 + 우 코드 카드 (= 실제 코드 스니펫)
5. 마무리 — `ship().success()` + 다크 ship 카드 + 라이트 links 카드 (repo · docs · demo)

## 다이어그램 룰
- 박스 = 직각 + hairline + 모노 텍스트
- 강조 박스 = 푸른 배경 + 흰 텍스트
- 화살표 = 모노 텍스트 (`↓` 또는 `→`) + 라벨 (`HTTPS · WebSocket`)
- 레이어 라벨 = 모노 uppercase

## 금기
- 그라디언트 X
- 둥근 박스 X (= radius 0)
- 이모지 X
- 영업 톤 X
- "차세대·혁신적·놀라운" X

## 출력 형식
5장 stacked HTML.
