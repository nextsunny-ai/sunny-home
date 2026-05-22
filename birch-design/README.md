# Birch Sound · 디자인 시스템

6가지 PPT 스타일 + 25 글로벌 레퍼런스. 디자인 가이드 `.md`를 Claude / ChatGPT Project Knowledge에 업로드하면 AI가 그 톤으로 슬라이드 콘텐츠를 만들어 준다.

## 사용 방법

1. 스타일 카드 클릭
2. 디자인 가이드 `.md` 다운로드
3. Claude / ChatGPT 새 프로젝트 → Project Knowledge에 업로드
4. 프롬프트 복사 → 대화창에 주제 박고 생성

## 6 스타일

| # | 이름 | 톤 | 용도 |
|---|---|---|---|
| 01 | Simple Mono Red | #FAFAFA + Red 액센트 | 보고서·내부 자료·데이터 |
| 02 | Dark Mono Report | #0A0A0E + Amber | 전략·경영진·투자자 |
| 03 | Color Block Business | 컬러 블록 + 화살표 | 피치덱·B2B 제안 |
| 04 | City Brand Light | 라이트그레이 + 5색 글로우 | 도시·문화·페스티벌 |
| 05 | Dark Digital Art | 다크 + 네온 그라디언트 | 디지털 아트·이머시브·뮤직 |
| 06 | Editorial Magazine | 따뜻한 화이트 + Fraunces | 매거진·광고 협업·아티스트 |

## 25 글로벌 레퍼런스

- **Design Systems · 10** — Apple HIG · Material 3 · IBM Carbon · shadcn/ui · Radix UI · Vercel Geist · Linear Method · Stripe · Atlassian · Notion
- **Slide Tools · 07** — Pitch · Gamma · Beautiful.ai · Slidesgo · Canva · Pages.xyz · Slidebean
- **Inspiration · 08** — Awwwards · Dribbble · Behance · Mobbin · Land-book · SiteInspire · Godly · Pinterest

## 폴더 구조

```
.
├── index.html          갤러리 메인
├── style.css           스타일
├── tokens.css          디자인 토큰
├── app.js              로직 (카드·모달·레퍼런스)
├── guides/             6 디자인 가이드 .md
├── prompts/            6 AI 프롬프트 .txt
└── previews/           스타일별 표지 + (cover_01은 5장 풀세트)
```

## 로컬 실행

```bash
python -m http.server 8092
# http://localhost:8092
```

## 라이선스

내부 사용 전용. 외부 공유 시 별도 합의.
