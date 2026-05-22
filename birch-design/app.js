// ===========================================
// Birch Sound · PPT Design System
// 6 main cards (3-col grid) + 25 reference buttons
// ===========================================

const STYLES = [
  {
    id: '01',
    featured: true,
    name: '심플 모노 + 붉은 액센트',
    subName: 'Simple Mono Red',
    desc: '회사 표준 보고서 톤. 붉은 액센트, hairline divider, 카드 기반.',
    cover: 'previews/cover_01.html',
    meta: {
      '배경': '#FAFAFA',
      '텍스트': '#0A0A0E',
      '액센트': '붉은 액센트 (단색)',
      '폰트': 'Pretendard · JetBrains Mono',
      '레이아웃': 'hairline · card',
      '용도': '주간보고 · 사업계획 · 데이터 리포트'
    }
  },
  {
    id: '02',
    name: '다크 보고서',
    subName: 'Dark Mono Report',
    desc: '다크 배경 보고서 톤. 모노스페이스 메타 + 노란 액센트.',
    cover: 'previews/cover_02.html',
    meta: {
      '배경': '#0A0A0E',
      '텍스트': '#F5F5F7',
      '액센트': '#FFB800 — Amber',
      '폰트': 'Pretendard · JetBrains Mono',
      '레이아웃': 'hairline · 모노 메타',
      '용도': '전략 보고 · 투자자 자료'
    }
  },
  {
    id: '03',
    name: '컬러 블록 비즈니스',
    subName: 'Color Block Business',
    desc: '컬러 블록 + 화살표 + 큰 영문 타이포. 피치덱 양식.',
    cover: 'previews/cover_03.html',
    meta: {
      '배경': '#F5F4F0',
      '액센트': '#FF6B1F — Orange Block',
      '텍스트': '#15151D',
      '폰트': 'Inter · Pretendard · JetBrains Mono',
      '레이아웃': '컬러 블록 · 화살표 · 통계 카드',
      '용도': '피치덱 · B2B 제안'
    }
  },
  {
    id: '04',
    name: '시티 브랜드 라이트',
    subName: 'City Brand Light',
    desc: '라이트그레이 + 차콜 + 5컬러 도메인. 도시·문화 톤.',
    cover: 'previews/cover_04.html',
    meta: {
      '배경': '#F2F2F4',
      '텍스트': '#1A1A22',
      '액센트': '5색 도메인',
      '폰트': 'Pretendard · Space Mono',
      '레이아웃': '미니멀 좌우 분할 · 컬러 글로우',
      '용도': '브랜드 발표 · 페스티벌 라인업'
    }
  },
  {
    id: '05',
    name: '다크 디지털 아트',
    subName: 'Dark Digital Art',
    desc: '다크 + 네온 그라디언트. Display 타이포 + 글래스 칩.',
    cover: 'previews/cover_05.html',
    meta: {
      '배경': '#0A0A12',
      '액센트': 'Neon (Purple · Mint · Pink)',
      '텍스트': '#FFFFFF',
      '폰트': 'Bricolage Grotesque · Pretendard',
      '레이아웃': '풀스크린 비주얼 · 글래스 카드',
      '용도': '아트 프로젝트 · 페스티벌 발표'
    }
  },
  {
    id: '06',
    name: '에디토리얼 매거진',
    subName: 'Editorial Magazine',
    desc: '화이트 + 부드러운 컬러 카드 + Display Serif. 잡지 톤.',
    cover: 'previews/cover_06.html',
    meta: {
      '배경': '#F5F4F0',
      '텍스트': '#1A1A22',
      '액센트': '민트 #C8E0D5 · 모브 #3E2F2F',
      '폰트': 'Fraunces · Pretendard',
      '레이아웃': '둥근 카드 (cover 한정) · 큰 숫자 마커',
      '용도': '광고 협업 제안 · 아티스트 프로파일'
    }
  }
];

const REFERENCES = [
  {
    group: 'Design Systems',
    downloadable: true,
    groupDesc: '톤 가이드 .md 다운로드 → Claude · ChatGPT에 업로드해서 그 톤 흉내내기',
    visitLabel: '',
    items: [
      { name: 'Apple HIG', desc: '벤토 그리드 · iOS·macOS 디자인 원칙.', guide: 'guides/ref_01_apple_hig.md', source: 'developer.apple.com', url: 'https://developer.apple.com/design/human-interface-guidelines', palette: ['#000000', '#FFFFFF', '#007AFF'], style: '미니멀 · 벤토' },
      { name: 'Material 3', desc: 'Material You · 동적 컬러 시스템.', guide: 'guides/ref_02_material_3.md', source: 'm3.material.io', url: 'https://m3.material.io', palette: ['#6750A4', '#B69DF8', '#EADDFF'], style: '동적 컬러 · 라운드' },
      { name: 'IBM Carbon', desc: '엔터프라이즈 + 데이터 시각화 + AAA.', guide: 'guides/ref_03_ibm_carbon.md', source: 'carbondesignsystem.com', url: 'https://carbondesignsystem.com', palette: ['#0F62FE', '#161616', '#F4F4F4'], style: '엔터프라이즈 · 직각' },
      { name: 'shadcn/ui', desc: 'copy-paste 컴포넌트. React UI 표준.', guide: 'guides/ref_04_shadcn_ui.md', source: 'ui.shadcn.com', url: 'https://ui.shadcn.com', palette: ['#0A0A0A', '#FAFAFA', '#71717A'], style: '흑백 · 모던' },
      { name: 'Radix UI', desc: '헤드리스 접근성 프리미티브.', guide: 'guides/ref_05_radix_ui.md', source: 'radix-ui.com', url: 'https://www.radix-ui.com', palette: ['#1A1523', '#FFFFFF', '#3E63DD'], style: '헤드리스 · 인디고' },
      { name: 'Vercel Geist', desc: 'Geist 폰트 + 미니멀 흑백.', guide: 'guides/ref_06_vercel_geist.md', source: 'vercel.com/design', url: 'https://vercel.com/design', palette: ['#000000', '#FFFFFF', '#0070F3'], style: '미니멀 · 모노' },
      { name: 'Linear Method', desc: '미니멀 다크 · 키보드 퍼스트.', guide: 'guides/ref_07_linear_method.md', source: 'linear.app/method', url: 'https://linear.app/method', palette: ['#08090A', '#5E6AD2', '#9B9B9B'], style: '다크 · 퍼플' },
      { name: 'Stripe Design', desc: '그라디언트 메시 + 마이크로 인터랙션.', guide: 'guides/ref_08_stripe_design.md', source: 'stripe.com', url: 'https://stripe.com', palette: ['#635BFF', '#00D4FF', '#FF6BC8'], style: '그라디언트 · 프리미엄' },
      { name: 'Atlassian Design', desc: 'Confluence · Jira 워크 프로덕트 톤.', guide: 'guides/ref_09_atlassian_design.md', source: 'atlassian.design', url: 'https://atlassian.design', palette: ['#0052CC', '#172B4D', '#F4F5F7'], style: '워크 · 블루' },
      { name: 'Notion', desc: '문서 톤 미니멀 + 캘리그래픽.', guide: 'guides/ref_10_notion.md', source: 'notion.so', url: 'https://www.notion.so', palette: ['#37352F', '#F1F1EF', '#E03E3E'], style: '문서 · 따뜻한 톤' }
    ]
  },
  {
    group: 'Slide Tools',
    downloadable: false,
    groupDesc: '슬라이드 만들기 도구 — 사이트 방문해서 직접 사용',
    visitLabel: '↗ 사이트',
    items: [
      { name: 'Pitch', desc: '협업형 모던 슬라이드 도구.', guide: 'guides/ref_11_pitch.md', source: 'pitch.com', url: 'https://pitch.com', palette: ['#1A1A1A', '#FFFFFF', '#FF5C28'], style: '모던 · 협업' },
      { name: 'Gamma', desc: 'AI 슬라이드 · 웹페이지 자동 생성.', guide: 'guides/ref_12_gamma.md', source: 'gamma.app', url: 'https://gamma.app', palette: ['#1A1A1A', '#FF6B35', '#FFD9C2'], style: 'AI · 자동' },
      { name: 'Beautiful.ai', desc: 'AI 자동 레이아웃 슬라이드.', guide: 'guides/ref_13_beautiful_ai.md', source: 'beautiful.ai', url: 'https://www.beautiful.ai', palette: ['#0066FF', '#FFFFFF', '#000000'], style: 'AI · 블루' },
      { name: 'Slidesgo', desc: '무료 PPT 템플릿.', guide: 'guides/ref_14_slidesgo.md', source: 'slidesgo.com', url: 'https://slidesgo.com', palette: ['#FF6F00', '#FFFFFF', '#1A1A22'], style: '템플릿 · 다양' },
      { name: 'Canva Presentations', desc: '다양한 PPT 템플릿 + 협업.', guide: 'guides/ref_15_canva.md', source: 'canva.com', url: 'https://www.canva.com/presentations', palette: ['#00C4CC', '#7D2AE8', '#FFFFFF'], style: '시안·퍼플' },
      { name: 'Pages.xyz', desc: '랜딩 페이지 디자인 영감.', guide: 'guides/ref_16_pages_xyz.md', source: 'pages.xyz', url: 'https://pages.xyz', palette: ['#000000', '#FFFFFF', '#A0A0A0'], style: '모노 · 큐레이션' },
      { name: 'Slidebean', desc: 'IR · 피치덱 전문.', guide: 'guides/ref_17_slidebean.md', source: 'slidebean.com', url: 'https://slidebean.com', palette: ['#001F3F', '#FF851B', '#FFFFFF'], style: 'IR · 피치덱' }
    ]
  },
  {
    group: 'Inspiration',
    downloadable: false,
    groupDesc: '디자인 영감 큐레이션 — 사이트 방문해서 시안 보기',
    visitLabel: '↗ 영감',
    items: [
      { name: 'Awwwards', desc: '웹 디자인 시상식 · 트렌드.', guide: 'guides/ref_18_awwwards.md', source: 'awwwards.com', url: 'https://www.awwwards.com', palette: ['#000000', '#FFFFFF', '#FFCC00'], style: '트렌드 · 옐로우' },
      { name: 'Dribbble', desc: 'UI · 일러스트 디자인 샷.', guide: 'guides/ref_19_dribbble.md', source: 'dribbble.com', url: 'https://dribbble.com', palette: ['#EA4C89', '#0D0C22', '#FFFFFF'], style: '핑크 · 컬러풀' },
      { name: 'Behance', desc: '브랜딩 · 에디토리얼 · 풀 프로젝트.', guide: 'guides/ref_20_behance.md', source: 'behance.net', url: 'https://www.behance.net', palette: ['#1769FF', '#000000', '#FFFFFF'], style: '풀 프로젝트 · 블루' },
      { name: 'Mobbin', desc: '모바일 앱 UI 패턴 라이브러리.', guide: 'guides/ref_21_mobbin.md', source: 'mobbin.com', url: 'https://mobbin.com', palette: ['#F1F1F2', '#000000', '#0066FF'], style: '모바일 · 패턴' },
      { name: 'Land-book', desc: '랜딩 페이지 큐레이션.', guide: 'guides/ref_22_land_book.md', source: 'land-book.com', url: 'https://land-book.com', palette: ['#1A1A22', '#FFFFFF', '#FF4D4D'], style: '랜딩 · 큐레이션' },
      { name: 'SiteInspire', desc: '엄선된 웹 디자인 갤러리.', guide: 'guides/ref_23_siteinspire.md', source: 'siteinspire.com', url: 'https://www.siteinspire.com', palette: ['#FFFFFF', '#1A1A22', '#888888'], style: '모노 · 엄선' },
      { name: 'Godly', desc: '극상위 웹 디자인 큐레이션.', guide: 'guides/ref_24_godly.md', source: 'godly.website', url: 'https://godly.website', palette: ['#000000', '#FFFFFF', '#FF6B6B'], style: '극상위 · 모노' },
      { name: 'Pinterest · Presentation', desc: 'PPT · 키비주얼 보드 검색.', guide: 'guides/ref_25_pinterest_presentation.md', source: 'pinterest.com', url: 'https://www.pinterest.com/search/pins/?q=presentation%20design', palette: ['#E60023', '#FFFFFF', '#000000'], style: '보드 · 레드' }
    ]
  }
];

// ── 카드 그리드 렌더링 ──
const stylesHost = document.getElementById('styles-host');
STYLES.forEach(s => {
  const btn = document.createElement('button');
  btn.className = 'style-card';
  btn.type = 'button';
  btn.dataset.id = s.id;
  btn.innerHTML = `
    <span class="style-card__chip ${s.featured ? 'featured' : ''}">${s.id} · ${s.subName}</span>
    <div class="style-card__preview is-loading" data-cover="${s.cover}"></div>
    <div class="style-card__body">
      <div class="style-card__mark ${s.featured ? 'featured' : ''}">${s.id}</div>
      <div class="style-card__text">
        <div class="style-card__name">${s.name}</div>
        <div class="style-card__desc">${s.desc}</div>
      </div>
    </div>
  `;
  btn.addEventListener('click', () => openModal(s));
  stylesHost.appendChild(btn);
});

// ── 미리보기 lazy load + scale ──
const previewObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    const el = entry.target;
    if (el.dataset.loaded === 'true') return;
    el.dataset.loaded = 'true';
    const iframe = document.createElement('iframe');
    iframe.src = el.dataset.cover;
    iframe.loading = 'lazy';
    iframe.tabIndex = -1;
    iframe.setAttribute('aria-hidden', 'true');
    iframe.addEventListener('load', () => el.classList.remove('is-loading'));
    el.appendChild(iframe);
    previewObserver.unobserve(el);
  });
}, { rootMargin: '200px' });
document.querySelectorAll('.style-card__preview').forEach(el => previewObserver.observe(el));

const scaleObserver = new ResizeObserver(entries => {
  entries.forEach(entry => {
    const iframe = entry.target.querySelector('iframe');
    if (!iframe) return;
    iframe.style.transform = `scale(${entry.contentRect.width / 1920})`;
  });
});
document.querySelectorAll('.style-card__preview').forEach(el => scaleObserver.observe(el));

// ── 글로벌 레퍼런스 = 작은 버튼 ──
const refHost = document.getElementById('references-host');
REFERENCES.forEach(group => {
  const g = document.createElement('div');
  g.className = 'ref-group';
  if (group.downloadable) {
    g.innerHTML = `
      <div class="ref-group__head">
        <div class="ref-group__left">
          <h3 class="ref-group__title">${group.group}</h3>
          <span class="ref-group__count">${String(group.items.length).padStart(2, '0')} guides</span>
        </div>
        <p class="ref-group__desc">${group.groupDesc}</p>
      </div>
      <div class="ref-grid">
        ${group.items.map(item => `
          <article class="ref-card ref-card--featured">
            <button class="ref-card__download" data-guide="${item.guide}" data-name="${item.name}" aria-label="${item.name} 가이드 .md 다운로드"><span class="ref-card__download-icon">↓</span><span class="ref-card__download-text">.md 다운</span></button>
            <a class="ref-card__link" href="${item.url}" target="_blank" rel="noopener noreferrer">
              <div class="ref-card__shot" data-url="${item.url}" data-fallback-palette='${JSON.stringify(item.palette)}'></div>
              <div class="ref-card__body">
                <div class="ref-card__palette">
                  ${item.palette.map(c => `<span class="ref-color" style="background:${c}" title="${c}"></span>`).join('')}
                  <span class="ref-card__style">${item.style}</span>
                </div>
                <div class="ref-card__top">
                  <span class="ref-card__name">${item.name}</span>
                </div>
                <p class="ref-card__desc">${item.desc}</p>
                <div class="ref-card__bottom">
                  <span class="ref-card__url">${item.source}</span>
                  <span class="ref-card__visit-cta">사이트 방문 →</span>
                </div>
              </div>
            </a>
          </article>
        `).join('')}
      </div>
    `;
  } else {
    g.innerHTML = `
      <div class="ref-group__head">
        <div class="ref-group__left">
          <h3 class="ref-group__title">${group.group}</h3>
          <span class="ref-group__count">${String(group.items.length).padStart(2, '0')} sites</span>
        </div>
        <p class="ref-group__desc">${group.groupDesc}</p>
      </div>
      <div class="ref-pills">
        ${group.items.map(item => `
          <a class="ref-pill" href="${item.url}" target="_blank" rel="noopener noreferrer" title="${item.desc} — 사이트 방문">
            <span class="ref-pill__dot" style="background:${item.palette[0]}"></span>
            ${item.name}
            <span class="ref-pill__arrow">사이트 →</span>
          </a>
        `).join('')}
      </div>
    `;
  }
  refHost.appendChild(g);
});

// 사이트 미리보기 lazy load (thum.io 무료 스크린샷 서비스)
const shotObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    const el = entry.target;
    if (el.dataset.loaded === 'true') return;
    el.dataset.loaded = 'true';
    const url = el.dataset.url;
    const palette = JSON.parse(el.dataset.fallbackPalette || '[]');
    const img = new Image();
    img.alt = '';
    img.loading = 'lazy';
    img.onerror = () => {
      el.classList.add('ref-card__shot--fallback');
      el.style.background = `linear-gradient(135deg, ${palette[0] || '#000'} 0%, ${palette[1] || '#888'} 60%, ${palette[2] || '#fff'} 100%)`;
    };
    img.onload = () => el.classList.add('ref-card__shot--loaded');
    img.src = `https://image.thum.io/get/width/720/crop/225/noanimate/${encodeURIComponent(url)}`;
    el.appendChild(img);
    shotObserver.unobserve(el);
  });
}, { rootMargin: '300px' });
document.querySelectorAll('.ref-card__shot').forEach(el => shotObserver.observe(el));

// ── 모달 ──
const modal = document.getElementById('modal');
const modalClose = document.getElementById('modal-close');
const modalIndex = document.getElementById('modal-index');
const modalTitle = document.getElementById('modal-title');
const modalDesc = document.getElementById('modal-desc');
const modalMeta = document.getElementById('modal-meta');
const modalFrame = document.getElementById('modal-frame');
const btnDownload = document.getElementById('btn-download');
const btnCopyPrompt = document.getElementById('btn-copy-prompt');

let currentStyle = null;

function openModal(s) {
  currentStyle = s;
  modalIndex.textContent = `${s.id} / 06 · ${s.subName}`;
  modalTitle.textContent = s.name;
  modalDesc.textContent = s.desc;
  modalMeta.innerHTML = Object.entries(s.meta).map(([k, v]) => `<dt>${k}</dt><dd>${v}</dd>`).join('');
  modalFrame.src = s.cover;
  const slug = slugify(s.subName);
  btnDownload.href = `guides/${s.id}_${slug}.md`;
  btnDownload.download = `${s.id}_${slug}.md`;
  modal.dataset.open = 'true';
  modal.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  modal.dataset.open = 'false';
  modal.setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
  modalFrame.src = 'about:blank';
}

modalClose.addEventListener('click', closeModal);
modal.addEventListener('click', (e) => { if (e.target === modal) closeModal(); });
document.addEventListener('keydown', (e) => {
  if (modal.dataset.open !== 'true') return;
  if (e.key === 'Escape') closeModal();
});

btnCopyPrompt.addEventListener('click', async () => {
  if (!currentStyle) return;
  try {
    const slug = slugify(currentStyle.subName);
    const res = await fetch(`prompts/${currentStyle.id}_${slug}.txt`);
    if (!res.ok) throw new Error('not found');
    const text = await res.text();
    await navigator.clipboard.writeText(text);
    showToast('AI 프롬프트 복사 완료');
  } catch (err) {
    showToast('프롬프트 파일 준비 중');
  }
});

// ── 회사 카드 가이드 .md 다운로드 = Blob 방식 (Chrome 경고 X) ──
btnDownload.addEventListener('click', async (e) => {
  if (!currentStyle) return;
  e.preventDefault();
  const slug = slugify(currentStyle.subName);
  const path = `guides/${currentStyle.id}_${slug}.md`;
  const filename = `${currentStyle.id}_${slug}.md`;
  await downloadMd(path, filename, currentStyle.name);
});

// ── 글로벌 레퍼런스 다운로드 버튼 ──
document.addEventListener('click', async (e) => {
  const dlBtn = e.target.closest('.ref-card__download');
  if (!dlBtn) return;
  e.preventDefault();
  e.stopPropagation();
  const guide = dlBtn.dataset.guide;
  const filename = guide.split('/').pop();
  await downloadMd(guide, filename, dlBtn.dataset.name);
});

async function downloadMd(path, filename, displayName) {
  try {
    const res = await fetch(path);
    if (!res.ok) throw new Error('not found');
    const text = await res.text();
    const blob = new Blob([text], { type: 'text/markdown;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    setTimeout(() => URL.revokeObjectURL(url), 1000);
    showToast(`${displayName} 가이드 다운로드 완료`);
  } catch (err) {
    showToast('가이드 파일 준비 중');
  }
}

// ── helpers ──
function slugify(s) {
  return s.toLowerCase().replace(/[^\w\s-]/g, '').trim().replace(/\s+/g, '_');
}

const toast = document.getElementById('toast');
let toastTimer;
function showToast(msg) {
  toast.textContent = msg;
  toast.dataset.visible = 'true';
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => { toast.dataset.visible = 'false'; }, 2400);
}
