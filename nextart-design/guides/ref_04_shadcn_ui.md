---
name: shadcn/ui
description: copy-paste 컴포넌트. 2026 React UI 표준.
url: https://ui.shadcn.com
category: Design Systems
---

# shadcn/ui — 디자인 가이드

## 핵심 원칙
- **copy-paste 컴포넌트** (= npm install X, 직접 복사)
- Radix UI 프리미티브 위 + Tailwind CSS
- **CSS 변수 기반 테마** (런타임 비용 0)
- Default · New York 2 스타일

## 컬러 토큰 (HSL)
```
--background: 0 0% 100%
--foreground: 240 10% 3.9%
--primary: 240 5.9% 10%
--muted: 240 4.8% 95.9%
--accent: 240 4.8% 95.9%
--border: 240 5.9% 90%
--radius: 0.5rem
```

## 타이포
- 기본 = system font stack (= 대체 = Geist / Inter)
- 모노 = JetBrains Mono

## 컴포넌트 룰
- CVA (class-variance-authority) 사용
- variant 기반 타입 안전
- Default · Destructive · Outline · Secondary · Ghost · Link

## 사용 시점
- React 앱 + 모던 SaaS
- 빠른 프로토타입
- 컴포넌트 일관성 필요한 자료

## 참고
https://ui.shadcn.com
