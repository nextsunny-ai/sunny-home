---
name: Global Design Systems — 통합 가이드
description: Apple HIG · Material 3 · IBM Carbon · shadcn/ui · Radix · Vercel Geist · Linear · Stripe · Atlassian · Notion 톤 통합. AI에 업로드하면 "Stripe 톤으로" "Linear 톤으로" 식으로 호출 가능.
version: 1.0
last_updated: 2026-05-22
---

# Global Design Systems — 통합 가이드

10개 글로벌 디자인 시스템의 핵심 원칙 통합. 이 파일을 Claude / ChatGPT Project Knowledge에 업로드한 뒤 AI에 "**Stripe 톤으로**" "**Linear 톤으로**" 등으로 호출하면 해당 톤을 흉내낸다.

---

## 1. Apple HIG

URL = https://developer.apple.com/design/human-interface-guidelines

핵심:
- **벤토 그리드** = 큰 카드 1 + 작은 카드 N의 불균등 배치
- **SF Pro** 폰트 (= 비슷한 톤 = Geist · Inter)
- 큰 여백 · 단색 카드 + 카드별 컬러 1개씩
- 모서리 라운드 (Apple 한정 = 16~24px) — 다른 톤에선 둥근 카드 X

용도: 제품 · IP 쇼케이스 / 포트폴리오

## 2. Google Material 3

URL = https://m3.material.io

핵심:
- **Material You** = 동적 컬러 시스템
- elevation 시스템 (0·1·3·6·8·12)
- 부드러운 라운드 (12·16·28)
- 모션 = standard easing `cubic-bezier(0.2, 0, 0, 1)`

용도: Android · 안드로이드 호환 제품 발표

## 3. IBM Carbon

URL = https://carbondesignsystem.com

핵심:
- **엔터프라이즈 톤** = 회색 다층 + 파란 액센트 (`#0F62FE`)
- 직각 카드 (라운드 X)
- 데이터 시각화 강함 (= 차트·테이블)
- 접근성 WCAG AAA

용도: B2B 엔터프라이즈 · 데이터 자료

## 4. shadcn/ui

URL = https://ui.shadcn.com

핵심:
- **copy-paste 컴포넌트** = `npx shadcn@latest add`
- Radix UI 위 + Tailwind CSS
- CSS 변수 기반 테마 (런타임 비용 0)
- Default · New York 두 스타일

용도: React 앱 + 모던 SaaS

## 5. Radix UI

URL = https://www.radix-ui.com

핵심:
- **헤드리스 프리미티브** = 무스타일 + 접근성
- WAI-ARIA 자동 준수
- Linear · Vercel · Supabase 사용

용도: 컴포넌트 위에 자체 스타일 입히기

## 6. Vercel Geist

URL = https://vercel.com/design

핵심:
- **Geist Sans / Geist Mono** 폰트
- 미니멀 흑백 + 단일 액센트 (블루 또는 퍼플 그라디언트)
- CSS 변수 기반 토큰
- Spacing · color · typography 모두 토큰

용도: Tech · SaaS · 기술 자료

## 7. Linear Method

URL = https://linear.app/method

핵심:
- **극도 미니멀** · 불필요한 UI 제거
- 키보드 퍼스트 (모든 액션 단축키)
- 60fps 부드러운 모션
- 다크 모드 디폴트 · 뉴트럴 그레이 + 퍼플 액센트
- 사이드바 + 메인 + 디테일 3열 레이아웃

용도: 프로덕트 데모 · 개발자 도구

## 8. Stripe

URL = https://stripe.com

핵심:
- **그라디언트 메시 배경** (= 시그니처)
- 마이크로 인터랙션 정교
- 인디고·퍼플 그라디언트 + 화이트 + 뉴트럴
- 카드 = 12~16px 라운드 + 서브틀 섀도우
- 코드 블록 + 인터랙티브 예제 (= 문서 디자인의 골드 스탠다드)

용도: IR · 결제 · B2B 프리미엄 톤

## 9. Atlassian Design

URL = https://atlassian.design

핵심:
- Confluence · Jira · 워크 프로덕트 톤
- 블루 액센트 (`#0052CC`)
- 정직한 비즈니스 톤 (= 화려함 X)
- 데이터 + 협업 중심

용도: 사내 협업 · 프로젝트 관리 자료

## 10. Notion

URL = https://www.notion.so

핵심:
- 문서 톤 미니멀
- 캘리그래픽 라인 (= 손글씨 일러스트)
- 흰색 + 검정 + 1~2 액센트 (Pink · Blue · Yellow 등)
- 라운드 = 6~8px

용도: 문서 · 매뉴얼 · 가이드

---

## 사용법 (AI 호출 패턴)

Project Knowledge에 이 파일 업로드 후, AI에:

```
이 가이드의 N번 (예: Stripe / Linear / Vercel Geist) 톤으로
PPT 5장 (표지·목차·콘텐츠·데이터·마무리)을 HTML로 만들어 줘.

주제: {여기에 본인 주제}
```

---

*출처 정리: 리안 sources `에이전트시스템/skills/sunny-rian/sources/` 풀버전 참조.*
