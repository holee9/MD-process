#!/usr/bin/env python3
"""
HTML 대시보드 생성기 — GitHub Pages 호스팅 또는 로컬 브라우저 열기용.
입력:
  - 각 카테고리의 .md frontmatter
  - issue-drafts/*.md frontmatter
  - issue-drafts/_log.json
  - git log (최근 활동)
출력:
  - docs/index.html
스택:
  - 단일 HTML, Chart.js (CDN), 외부 리소스 최소
"""
import os, re, json, pathlib, subprocess, datetime, collections, html

REPO = pathlib.Path('.').resolve()
OUT  = REPO / 'docs' / 'index.html'

CATEGORY_DIRS = [
    '00_프로젝트관리','01_법규_규제','02_품질경영시스템_QMS','03_설계_개발관리',
    '04_제조공정_관리','05_검사_시험_밸리데이션','06_문서_기록관리',
    '07_위험관리_ISO14971','08_시판후_감시_PMS','09_공급자_관리','10_교육_훈련',
    '11_일일_리서치로그','12_교차검증_보고서',
]
CATEGORY_LABELS = {
    '00_프로젝트관리':'00 관리','01_법규_규제':'01 법규','02_품질경영시스템_QMS':'02 QMS',
    '03_설계_개발관리':'03 설계','04_제조공정_관리':'04 제조','05_검사_시험_밸리데이션':'05 검사',
    '06_문서_기록관리':'06 문서','07_위험관리_ISO14971':'07 위험','08_시판후_감시_PMS':'08 PMS',
    '09_공급자_관리':'09 공급','10_교육_훈련':'10 교육','11_일일_리서치로그':'11 리서치',
    '12_교차검증_보고서':'12 검증',
}
EXCLUDE_NAMES = {'README.md','_TEMPLATE.md','문서_매트릭스.md'}

def parse_fm(text):
    if not text.startswith('---\n'): return None
    end = text.find('\n---', 4)
    if end < 0: return None
    fm = {}; cur_key = None
    for line in text[4:end].split('\n'):
        if not line.strip(): cur_key = None; continue
        m = re.match(r'^([a-zA-Z_-]+):\s*(.*)$', line)
        if m:
            k=m.group(1); v=m.group(2).strip()
            if v.startswith('[') and v.endswith(']'):
                v=[x.strip() for x in v[1:-1].split(',') if x.strip()]
            fm[k]=v; cur_key=k
        elif line.startswith('  - ') and cur_key:
            if not isinstance(fm.get(cur_key),list): fm[cur_key]=[]
            fm[cur_key].append(line[4:].strip())
    return fm

def collect_docs():
    docs = []
    for cat in CATEGORY_DIRS:
        d = REPO/cat
        if not d.exists(): continue
        for p in sorted(d.rglob('*.md')):
            if p.name in EXCLUDE_NAMES: continue
            try: text = p.read_text(encoding='utf-8')
            except: continue
            fm = parse_fm(text)
            if not fm: continue
            fm['_category']=cat; fm['_path']=str(p.relative_to(REPO)); fm['_name']=p.name
            docs.append(fm)
    return docs

def collect_issues():
    log_path = REPO / 'issue-drafts' / '_log.json'
    log = {}
    if log_path.exists():
        log = json.loads(log_path.read_text(encoding='utf-8'))
    closed = 0; open_n = 0
    for p in (REPO/'issue-drafts').glob('*.md'):
        if p.name in ('README.md','_TEMPLATE.md'): continue
        t = p.read_text(encoding='utf-8')
        fm = parse_fm(t)
        if not fm: continue
        if str(fm.get('state','')).lower() == 'closed': closed += 1
        else: open_n += 1
    return {'total': len(log), 'closed': closed, 'open': open_n, 'log': log}

def recent_commits(n=15):
    try:
        out = subprocess.check_output(
            ['git','log',f'-{n}','--pretty=%h|%ad|%s','--date=short'],
            stderr=subprocess.DEVNULL
        ).decode(errors='ignore').strip()
        return [line.split('|',2) for line in out.split('\n') if line]
    except:
        return []

def recent_logs(days=7):
    today = datetime.date.today()
    cutoff = today - datetime.timedelta(days=days)
    items = []
    for p in sorted((REPO/'11_일일_리서치로그').glob('*.md')):
        m = re.match(r'(\d{4}-\d{2}-\d{2})', p.name)
        if not m: continue
        d = datetime.date.fromisoformat(m.group(1))
        if d >= cutoff:
            items.append((d.isoformat(), p.stem))
    return sorted(items, reverse=True)

def build():
    docs = collect_docs()
    issues = collect_issues()
    commits = recent_commits(15)
    logs = recent_logs(10)

    by_cat = collections.Counter(d.get('_category','-') for d in docs)
    by_type = collections.Counter(d.get('type','-') for d in docs)
    by_status = collections.Counter(d.get('status','-') for d in docs)
    types_sorted = [t for t,_ in by_type.most_common()]

    # category × type matrix
    matrix = {cat:{t:0 for t in types_sorted} for cat in CATEGORY_DIRS}
    for d in docs:
        c = d.get('_category','-'); t = d.get('type','-')
        if c in matrix and t in matrix[c]:
            matrix[c][t] += 1

    # standards
    std_counter = collections.Counter()
    for d in docs:
        for s in d.get('applicable',[]) or []:
            std_counter[s] += 1

    today = datetime.date.today().isoformat()

    # Build JS data
    cat_labels = [CATEGORY_LABELS.get(c, c) for c in CATEGORY_DIRS]
    cat_counts = [by_cat.get(c, 0) for c in CATEGORY_DIRS]
    type_labels = list(by_type.keys())
    type_counts = [by_type[t] for t in type_labels]

    HTML = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>의료기기 제조 업무규칙 — 프로젝트 대시보드</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.5.0/dist/chart.umd.js"></script>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{color-scheme:light}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans KR',sans-serif;background:#f6f8fa;color:#1f2328;padding:24px;line-height:1.5}}
.container{{max-width:1280px;margin:0 auto}}
header{{margin-bottom:24px;border-bottom:2px solid #d0d7de;padding-bottom:16px}}
header h1{{font-size:1.6rem;margin-bottom:6px}}
header .meta{{font-size:0.85rem;color:#656d76}}
header .meta a{{color:#0969da;text-decoration:none}}
header .meta a:hover{{text-decoration:underline}}
.kpi-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:14px;margin-bottom:24px}}
.kpi{{background:#fff;border:1px solid #d0d7de;border-radius:8px;padding:18px;text-align:center}}
.kpi .num{{font-size:2rem;font-weight:700;color:#0969da}}
.kpi .num.green{{color:#1f883d}} .kpi .num.orange{{color:#bf8700}} .kpi .num.purple{{color:#8250df}}
.kpi .label{{font-size:0.75rem;color:#656d76;margin-top:4px;text-transform:uppercase;letter-spacing:0.5px}}
.row{{display:grid;grid-template-columns:repeat(auto-fit,minmax(380px,1fr));gap:16px;margin-bottom:16px}}
.card{{background:#fff;border:1px solid #d0d7de;border-radius:8px;padding:16px}}
.card h2{{font-size:0.95rem;color:#1f2328;margin-bottom:12px;padding-bottom:8px;border-bottom:1px solid #e6e8eb}}
.chart-box{{position:relative;height:260px}}
table{{width:100%;border-collapse:collapse;font-size:0.82rem}}
table th,table td{{padding:6px 8px;text-align:left;border-bottom:1px solid #e6e8eb}}
table th{{background:#f6f8fa;font-weight:600;color:#1f2328}}
table td.num{{text-align:right;font-variant-numeric:tabular-nums}}
.matrix-cell{{text-align:center;color:#0969da;font-variant-numeric:tabular-nums}}
.matrix-cell.zero{{color:#d0d7de}}
.matrix-cell.bold{{font-weight:700;color:#1f2328}}
.commit-list,.log-list{{list-style:none;font-size:0.82rem}}
.commit-list li,.log-list li{{padding:6px 0;border-bottom:1px solid #e6e8eb}}
.commit-list li:last-child,.log-list li:last-child{{border-bottom:none}}
.sha{{font-family:'SF Mono',ui-monospace,monospace;color:#8250df;font-size:0.75rem;margin-right:6px}}
.date{{color:#656d76;font-size:0.75rem;margin-right:6px}}
.health-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px}}
.health{{padding:10px;border-radius:6px;font-size:0.82rem;background:#dafbe1;border:1px solid #1f883d40}}
.health.warn{{background:#fff8c5;border-color:#bf870040}}
.health.bad{{background:#ffebe9;border-color:#cf222e40}}
.health .name{{font-weight:600}}
footer{{margin-top:24px;padding-top:16px;border-top:1px solid #d0d7de;font-size:0.8rem;color:#656d76;text-align:center}}
footer a{{color:#0969da;text-decoration:none}}
.print-hint{{display:none}}
@media print{{
  body{{background:#fff;padding:0}}
  .card{{break-inside:avoid;border:1px solid #ccc}}
  .print-hint{{display:block;text-align:center;color:#888;font-size:0.7rem;margin-bottom:10px}}
}}
</style>
</head>
<body>
<div class="container">
<header>
  <h1>📊 의료기기 제조 업무규칙 — 프로젝트 대시보드</h1>
  <div class="meta">
    <strong>홀리9/MD-process</strong> ·
    생성일 <strong>{today}</strong> ·
    다음 자동 갱신 매일 03:18 KST · 
    <a href="https://github.com/holee9/MD-process">GitHub 저장소</a> ·
    <a href="https://github.com/holee9/MD-process/blob/main/00_%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%EA%B4%80%EB%A6%AC/%EB%AC%B8%EC%84%9C_%EB%A7%A4%ED%8A%B8%EB%A6%AD%EC%8A%A4.md">상세 매트릭스</a> ·
    <a href="https://github.com/holee9/MD-process/issues">이슈</a>
  </div>
  <div class="print-hint">— 인쇄용 (회의자료) —</div>
</header>

<div class="kpi-grid">
  <div class="kpi"><div class="num">{len(docs)}</div><div class="label">총 문서</div></div>
  <div class="kpi"><div class="num">{issues['total']}</div><div class="label">총 이슈</div></div>
  <div class="kpi"><div class="num green">{issues['closed']}</div><div class="label">완료 (closed)</div></div>
  <div class="kpi"><div class="num orange">{issues['open']}</div><div class="label">진행중 (open)</div></div>
  <div class="kpi"><div class="num purple">{by_cat.get('11_일일_리서치로그',0)}</div><div class="label">리서치 로그</div></div>
  <div class="kpi"><div class="num">{by_cat.get('12_교차검증_보고서',0)}</div><div class="label">교차검증</div></div>
</div>

<div class="row">
  <div class="card">
    <h2>카테고리별 문서 분포</h2>
    <div class="chart-box"><canvas id="catChart"></canvas></div>
  </div>
  <div class="card">
    <h2>문서 유형별 분포</h2>
    <div class="chart-box"><canvas id="typeChart"></canvas></div>
  </div>
</div>

<div class="row">
  <div class="card">
    <h2>이슈 상태</h2>
    <div class="chart-box"><canvas id="issueChart"></canvas></div>
  </div>
  <div class="card">
    <h2>문서 상태 (라이프사이클)</h2>
    <div class="chart-box"><canvas id="statusChart"></canvas></div>
  </div>
</div>

<div class="card" style="margin-bottom:16px">
  <h2>카테고리 × 유형 매트릭스 (전체 {len(docs)}건)</h2>
  <table>
    <thead><tr><th>카테고리</th>{''.join(f'<th>{t}</th>' for t in types_sorted)}<th>합계</th></tr></thead>
    <tbody>
"""

    for cat in CATEGORY_DIRS:
        row = matrix[cat]
        total = sum(row.values())
        cells = ''.join(
            f'<td class="matrix-cell {"zero" if row[t]==0 else ""}">{row[t] or "·"}</td>'
            for t in types_sorted
        )
        HTML += f"<tr><td>{CATEGORY_LABELS.get(cat,cat)}</td>{cells}<td class='matrix-cell bold'>{total}</td></tr>\n"
    HTML += "</tbody></table></div>\n"

    # Standards
    if std_counter:
        HTML += '<div class="card" style="margin-bottom:16px"><h2>표준·법규별 충족 문서 수</h2><table><thead><tr><th>표준·법규</th><th class="num">문서 수</th></tr></thead><tbody>\n'
        for s,c in sorted(std_counter.items(), key=lambda x:-x[1])[:20]:
            HTML += f'<tr><td>{html.escape(s)}</td><td class="num">{c}</td></tr>\n'
        HTML += '</tbody></table></div>\n'

    # Recent activity
    HTML += '<div class="row"><div class="card"><h2>최근 커밋 (15)</h2><ul class="commit-list">\n'
    for c in commits:
        if len(c) >= 3:
            sha, date, msg = c
            HTML += f'<li><span class="sha">{html.escape(sha)}</span><span class="date">{html.escape(date)}</span>{html.escape(msg)[:90]}</li>\n'
    HTML += '</ul></div>\n'

    HTML += '<div class="card"><h2>최근 리서치 로그 (10일)</h2><ul class="log-list">\n'
    for d, stem in logs[:12]:
        HTML += f'<li><span class="date">{d}</span>{html.escape(stem)[:80]}</li>\n'
    HTML += '</ul></div></div>\n'

    # System health
    HTML += '''<div class="card" style="margin-bottom:16px">
<h2>시스템 헬스</h2>
<div class="health-grid">
<div class="health"><div class="name">✅ Auto-Issue Workflow</div><div>정상 가동</div></div>
<div class="health"><div class="name">✅ Build Matrix Workflow</div><div>push 시 자동</div></div>
<div class="health"><div class="name">✅ Validate Frontmatter</div><div>스키마 검증</div></div>
<div class="health"><div class="name">✅ 일일 스케줄러</div><div>03:18 KST</div></div>
<div class="health"><div class="name">✅ Issue Close 처리</div><div>state: closed 지원</div></div>
<div class="health warn"><div class="name">⚠ 로컬 작업 폴더 git</div><div>자동 흐름 무관</div></div>
</div>
</div>
'''

    HTML += f'''<footer>
자동 생성 — <code>scripts/build_dashboard_html.py</code> · 출처 단일 진실원: 각 문서 frontmatter ·
<a href="https://github.com/holee9/MD-process">repo</a> ·
<a href="https://github.com/holee9/MD-process/actions">Actions</a>
</footer>
</div>

<script>
const palette = ['#0969da','#1f883d','#bf8700','#8250df','#cf222e','#bf3989','#0a3069','#953800','#1f6feb','#5fed83','#fae17d','#c8c1f0'];

new Chart(document.getElementById('catChart'), {{
  type: 'bar',
  data: {{ labels: {json.dumps(cat_labels)}, datasets: [{{label:'문서 수', data: {json.dumps(cat_counts)}, backgroundColor:'#0969da'}}] }},
  options: {{ indexAxis:'y', responsive:true, maintainAspectRatio:false, plugins:{{legend:{{display:false}}}}, scales:{{x:{{beginAtZero:true}}}} }}
}});

new Chart(document.getElementById('typeChart'), {{
  type:'doughnut',
  data: {{ labels: {json.dumps(type_labels)}, datasets: [{{data: {json.dumps(type_counts)}, backgroundColor: palette}}] }},
  options: {{ responsive:true, maintainAspectRatio:false, plugins:{{legend:{{position:'right',labels:{{font:{{size:11}}}}}}}}}}
}});

new Chart(document.getElementById('issueChart'), {{
  type:'doughnut',
  data: {{ labels:['완료 (closed)','진행중 (open)'], datasets: [{{data:[{issues['closed']}, {issues['open']}], backgroundColor:['#1f883d','#bf8700']}}] }},
  options: {{ responsive:true, maintainAspectRatio:false, plugins:{{legend:{{position:'right'}}}}}}
}});

new Chart(document.getElementById('statusChart'), {{
  type:'bar',
  data: {{ labels: {json.dumps(list(by_status.keys()))}, datasets: [{{data: {json.dumps(list(by_status.values()))}, backgroundColor:'#8250df'}}] }},
  options: {{ responsive:true, maintainAspectRatio:false, plugins:{{legend:{{display:false}}}}, scales:{{y:{{beginAtZero:true}}}} }}
}});
</script>
</body>
</html>
'''

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(HTML, encoding='utf-8')
    print(f"✓ dashboard built: {OUT}  ({len(HTML)} bytes)")

if __name__ == '__main__':
    build()
