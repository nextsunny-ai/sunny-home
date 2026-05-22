---
name: Radix UI
description: 헤드리스 접근성 프리미티브.
url: https://www.radix-ui.com
category: Design Systems
---

# Radix UI — 디자인 가이드

## 핵심 원칙
- **헤드리스 (unstyled)** 프리미티브 — 디자인은 직접
- 행동·접근성만 제공 (= 포커스 트랩 · ARIA · 키보드)
- WAI-ARIA 자동 준수
- Linear · Vercel · Supabase 프로덕션 사용

## 제공 행동
- Dialog → 자동 `aria-modal` · ESC · 포커스 트랩
- Menu → 로빙 포커스 · 타입어헤드
- Dropdown · Popover · Tooltip · Tabs · Accordion · Toast 등

## 디자인은 = 직접
- 외형은 = Tailwind · CSS-in-JS · Vanilla CSS 자유
- shadcn/ui = Radix + Tailwind로 디자인 입힌 사례

## 사용 시점
- 자체 디자인 시스템 위에 행동 추가
- 접근성 직접 구현 X
- 컴포넌트 위에 자체 톤

## 참고
https://www.radix-ui.com
