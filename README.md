# SUNNY HOME

대표 유희정의 개인 시작 페이지.
**도메인 안 치고 = 한 화면에서 모든 정보 확인.**

## 라이브
https://nextsunny-ai.github.io/sunny-home/

## 섹션
1. **Hero** = 시간 / 날짜 / 인사 / 날씨 + News Pick (12건)
2. **Today's Business English** = 매일 1구문
3. **Tools** = 4사 도구 + Visual Maker · Sunny Team · Drive · Calendar 등
4. **Recent Projects** = `nextsunny-ai/*` 최근 푸시된 12 레포
5. **Notice** = 11명 에이전트 보고 (HANA / TEO / RIAN / SERA / GENIE)
6. **News** = AI · 공연 · 전시 · 콘텐츠IP · 디자인 · 지원사업 · 페스티벌 (탭 전환)
7. **This Week** = 마감 카드 (지원사업 / 납품 / 계약, D-day + 긴급도 색상)
8. **Recent Outputs** = visual-maker 최근 결과물 6장
9. **Hana's Daily Pages** = 플립북 (좌우 화살표 / 터치 스와이프 / 키보드)
10. **Footer** = 빌드 시각 (자동 갱신 = 신선도 표시)

## 자동 갱신
- **GitHub Action `.github/workflows/daily.yml`** = 매일 04:00 KST (UTC 19:00)
- `scripts/refresh_projects.py` = nextsunny-ai 레포 12개 → `data/projects.json`
- `scripts/refresh_build.py` = 빌드 시각 → `data/build.json`

## 데이터 구조
```
data/
├── projects.json     # GitHub 레포 (자동 갱신)
├── deadlines.json    # This Week 마감 (수동 또는 에이전트 push)
├── curation.json     # 하나 일일 페이지 (자동 또는 수동)
├── outputs.json      # visual-maker 최근 6장 (visual-maker push)
└── build.json        # 빌드 시각
sunny_home_data.json  # 뉴스/날씨/영어 (기존 유지)
```

## 크롬 시작 페이지로 박기
1. `chrome://settings/onStartup` 접속
2. **"특정 페이지 또는 페이지 모음 열기"** 선택
3. **새 페이지 추가** → URL: `https://nextsunny-ai.github.io/sunny-home/`

## 디자인
- Pretendard Variable + JetBrains Mono
- 매거진 톤 / 다크 / 오렌지 그라디언트 (RIAN v5)
- 1024 / 768 / 480 반응형
