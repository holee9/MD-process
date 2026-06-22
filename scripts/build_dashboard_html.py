#!/usr/bin/env python3
"""
회의·보고용 HTML 대시보드 자동 생성 (단일 진실원).
출력: docs/index.html
입력:
  - 각 카테고리 .md 의 frontmatter (version, status 등)
  - issue-drafts/*.md (state 필드)
  - 00_프로젝트관리/_dashboard_config.yml (사업 정보: 목표일·Tier)
  - git log (최근 활동·일별 속도)
사용:
  python3 scripts/build_dashboard_html.py
"""

import os, re, json, pathlib, subprocess, datetime, collections, html

REPO = pathlib.Path('.').resolve()
OUT  = REPO / 'docs' / 'index.html'
CONFIG_PATH = REPO / '00_프로젝트관리' / '_dashboard_config.yml'

CATEGORY_DIRS = [
    '00_프로젝트관리','01_법규_규제','02_품질경영시스템_QMS','03_설계_개발관리',
    '04_제조공정_관리','05_검사_시험_밸리데이션','06_문서_기록관리',
    '07_위험관리_ISO14971','08_시판후_감시_PMS','09_공급자_관리','10_교육_훈련',
    '11_일일_리서치로그','12_교차검증_보고서',
]
CATEGORY_LABELS = {
    '01_법규_규제':'01 법규','02_품질경영시스템_QMS':'02 QMS',
    '03_설계_개발관리':'03 설계','04_제조공정_관리':'04 제조',
    '05_검사_시험_밸리데이션':'05 검사','06_문서_기록관리':'06 문서',
    '07_위험관리_ISO14971':'07 위험','08_시판후_감시_PMS':'08 PMS',
    '09_공급자_관리':'09 공급','10_교육_훈련':'10 교육',
}

EXCLUDE_NAMES = {'README.md','_TEMPLATE.md','문서_매트릭스.md','_dashboard_config.yml'}

# ---------- YAML 파서 (PyYAML) ----------
def parse_yaml(text):
    import yaml
    return yaml.safe_load(text)

# ---------- Frontmatter 파서 ----------
def parse_fm(text):
    if not text.startswith('---\n'): return None
    end = text.find('\n---', 4)
    if end < 0: return None
    fm = {}; cur = None
    for line in text[4:end].split('\n'):
        if not line.strip(): cur = None; continue
        m = re.match(r'^([a-zA-Z_-]+):\s*(.*)$', line)
        if m:
            k=m.group(1); v=m.group(2).strip()
            if v.startswith('[') and v.endswith(']'):
                v=[x.strip() for x in v[1:-1].split(',') if x.strip()]
            fm[k]=v; cur=k
        elif line.startswith('  - ') and cur:
            if not isinstance(fm.get(cur),list): fm[cur]=[]
            fm[cur].append(line[4:].strip())
    return fm

def version_to_tuple(v):
    if not v: return (0,0)
    m = re.match(r'v?(\d+)\.(\d+)', str(v))
    return (int(m.group(1)), int(m.group(2))) if m else (0,0)

# ---------- Data Collection ----------
def collect_docs():
    docs = []
    for cat in CATEGORY_DIRS:
        d = REPO/cat
        if not d.exists(): continue
        for p in sorted(d.rglob('*.md')):
            if p.name in EXCLUDE_NAMES: continue
            try: text = p.read_text(encoding='utf-8')
            except: continue
            fm = parse_fm(text) or {}
            fm['_category']=cat; fm['_path']=str(p.relative_to(REPO)); fm['_name']=p.name
            docs.append(fm)
    return docs

def collect_issues():
    drafts_dir = REPO/'issue-drafts'
    total=0; closed=0; open_n=0
    for p in drafts_dir.glob('*.md'):
        if p.name in ('README.md','_TEMPLATE.md'): continue
        total += 1
        fm = parse_fm(p.read_text(encoding='utf-8')) or {}
        if str(fm.get('state','')).lower() == 'closed': closed += 1
        else: open_n += 1
    log = {}
    log_path = drafts_dir/'_log.json'
    if log_path.exists():
        try: log = json.loads(log_path.read_text(encoding='utf-8'))
        except: pass
    return {'total': total, 'closed': closed, 'open': open_n, 'mapped': len(log)}

def git_commits(n=20):
    try:
        out = subprocess.check_output(
            ['git','log',f'-{n}','--pretty=%h|%ad|%s','--date=short'],
            stderr=subprocess.DEVNULL).decode(errors='ignore').strip()
        return [line.split('|',2) for line in out.split('\n') if line]
    except: return []

def daily_v02_velocity(days=5):
    """최근 N일간 일별 'docs(' 또는 v0.2 보강 커밋 수"""
    try:
        out = subprocess.check_output(
            ['git','log',f'--since={days+1} days ago','--pretty=%ad|%s','--date=short'],
            stderr=subprocess.DEVNULL).decode(errors='ignore').strip()
        by_day = collections.Counter()
        for line in out.split('\n'):
            if '|' not in line: continue
            d, msg = line.split('|',1)
            # docs(...) 커밋 중 v0.2 또는 보강 키워드만 카운트
            if re.search(r'docs\([0-9]', msg) and re.search(r'v0\.\d|보강|신규', msg):
                by_day[d] += 1
        today = datetime.date.today()
        result = []
        for i in range(days-1,-1,-1):
            day = (today - datetime.timedelta(days=i)).isoformat()
            result.append((day, by_day.get(day, 0)))
        return result
    except:
        return []

# ---------- Main ----------
STYLE = "<style>\n:root{--bg:#0f172a;--card:#1e293b;--border:#334155;--text:#e2e8f0;--muted:#94a3b8;--accent:#38bdf8;--green:#4ade80;--yellow:#fbbf24;--red:#f87171;--purple:#a78bfa}\n*{margin:0;padding:0;box-sizing:border-box}\nbody{background:var(--bg);color:var(--text);font-family:'Segoe UI','Noto Sans KR',system-ui,sans-serif;padding:20px;line-height:1.5}\nh1{font-size:1.4rem;margin-bottom:4px}\n.subtitle{color:var(--muted);font-size:.85rem;margin-bottom:20px}\n.subtitle a{color:var(--accent);text-decoration:none}\n.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin-bottom:20px}\n.kpi{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:16px;text-align:center}\n.kpi .value{font-size:1.8rem;font-weight:700;color:var(--accent)}\n.kpi .label{font-size:.75rem;color:var(--muted);margin-top:4px}\n.kpi.green .value{color:var(--green)}\n.kpi.yellow .value{color:var(--yellow)}\n.kpi.red .value{color:var(--red)}\n.card{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:18px;margin-bottom:16px}\n.card h2{font-size:1rem;margin-bottom:12px;color:var(--accent)}\ntable{width:100%;border-collapse:collapse;font-size:.82rem}\nth,td{padding:6px 8px;text-align:left;border-bottom:1px solid var(--border)}\nth{color:var(--muted);font-weight:600}\n.bar{display:inline-block;height:14px;border-radius:3px;background:var(--accent);transition:width .3s}\n.bar-bg{display:inline-block;width:100px;height:14px;border-radius:3px;background:var(--border)}\n.tag{display:inline-block;padding:2px 8px;border-radius:4px;font-size:.7rem;font-weight:600}\n.tag-green{background:#065f4620;color:var(--green)}\n.tag-yellow{background:#78350f20;color:var(--yellow)}\n.progress-overall{height:24px;background:var(--border);border-radius:12px;overflow:hidden;margin:8px 0}\n.progress-fill{height:100%;background:linear-gradient(90deg,var(--accent),var(--green));display:flex;align-items:center;justify-content:center;font-size:.75rem;font-weight:700;color:var(--bg);border-radius:12px}\n.two-col{display:grid;grid-template-columns:1fr 1fr;gap:16px}\n@media(max-width:700px){.two-col{grid-template-columns:1fr}}\n.commit-list{list-style:none;font-size:.8rem}\n.commit-list li{padding:4px 0;border-bottom:1px solid var(--border)}\n.commit-list .date{color:var(--muted);margin-right:6px}\n.schedule-info{display:flex;gap:16px;flex-wrap:wrap;font-size:.82rem}\n.schedule-info div{background:var(--bg);padding:8px 12px;border-radius:6px;border:1px solid var(--border)}\n.actions{display:flex;gap:8px;margin-bottom:16px;flex-wrap:wrap}\n.actions a,.actions button{background:var(--card);border:1px solid var(--border);color:var(--text);padding:6px 12px;border-radius:6px;text-decoration:none;font-size:.8rem;cursor:pointer}\n.actions a:hover,.actions button:hover{background:#2d3a52}\n@media print{\n  body{background:#fff;color:#000;padding:0}\n  .card,.kpi{background:#fff;color:#000;border:1px solid #ccc}\n  .subtitle,.muted,th{color:#666}\n  .actions,.schedule-info{display:none}\n  h2{color:#000 !important}\n}\n</style></head><body>"


def last_commit_dates(paths):
    """경로별 마지막 커밋일(YYYY-MM-DD). 단일 git log 패스."""
    res = {}
    try:
        out = subprocess.check_output(
            ['git','-c','core.quotepath=false','log','--pretty=format:%ad','--date=short','--name-only'],
            stderr=subprocess.DEVNULL).decode('utf-8', errors='ignore')
    except Exception:
        return res
    cur = None
    for line in out.split('\n'):
        line = line.strip()
        if not line:
            continue
        if re.match(r'^\d{4}-\d{2}-\d{2}$', line):
            cur = line
            continue
        if cur and line not in res:
            res[line] = cur
    return res


def parse_audit_log():
    """00_프로젝트관리/_audit_log.md 표 파싱 → 사이클별/누적 사실성 지표. 컬럼 위치 변동에 강건."""
    import re as _re
    p = REPO / '00_프로젝트관리' / '_audit_log.md'
    rows = []
    if not p.exists():
        return rows
    for line in p.read_text(encoding='utf-8').split('\n'):
        line = line.strip()
        if not line.startswith('| 20'):
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        if len(cells) < 6:
            continue
        def _n(x):
            m = _re.search(r'-?\d+\.?\d*', x)
            return float(m.group()) if m else 0.0
        # 안정 인덱스: 0날짜 1표본 2주장 3사실오류 4노후 5인용결함 (해석범위/통과율은 뒤에 위치 변동)
        claims = int(_n(cells[2])); errors = int(_n(cells[3])); cit = int(_n(cells[5]))
        passpct = round((claims - errors - cit) / claims * 100, 1) if claims else 0.0
        rows.append({'date': cells[0], 'docs': int(_n(cells[1])), 'claims': claims,
                     'errors': errors, 'outdated': int(_n(cells[4])), 'citation': cit, 'pass': passpct})
    return rows

def count_issue_backlog():
    """issue-drafts frontmatter 라벨로 3소스 백로그 집계."""
    import re as _re
    d = REPO / 'issue-drafts'
    r = {'audit_open': 0, 'audit_closed': 0, 'plan_open': 0, 'emergent_open': 0,
         'p0_open': 0, 'p1_open': 0, 'p2_open': 0, 'audit_p0_open': 0}
    if not d.exists():
        return r
    for p in d.glob('*.md'):
        if p.name in ('README.md', '_TEMPLATE.md'):
            continue
        try:
            head = p.read_text(encoding='utf-8')[:700]
        except Exception:
            continue
        closed = bool(_re.search(r'(?m)^state:\s*closed', head))
        is_audit = 'audit:' in head
        if is_audit:
            if closed:
                r['audit_closed'] += 1
            else:
                r['audit_open'] += 1
                if 'prio:P0' in head:
                    r['audit_p0_open'] += 1
        if not closed:
            if 'source:plan' in head:
                r['plan_open'] += 1
            if 'source:emergent' in head:
                r['emergent_open'] += 1
            if 'prio:P0' in head:
                r['p0_open'] += 1
            elif 'prio:P1' in head:
                r['p1_open'] += 1
            elif 'prio:P2' in head:
                r['p2_open'] += 1
    return r


def build_maintenance(config):
    proj = config.get('project', {})
    maint = config.get('maintenance', {}) or {}
    target_cats = config.get('target_categories', [])
    docs = collect_docs()
    issues = collect_issues()
    commits = git_commits(20)
    today = datetime.date.today()
    today_str = today.isoformat()
    repo = proj.get('repo', 'holee9/MD-process')

    core_docs = [d for d in docs if d.get('_category') in target_cats]
    n_core = len(core_docs); n_total = len(docs)

    def valid_fm(d):
        t = str(d.get('type', '')).strip()
        return bool(t) and t != '?'
    fm_valid = sum(1 for d in docs if valid_fm(d))
    fm_rate = round(fm_valid / max(1, n_total) * 100)
    fm_invalid = n_total - fm_valid

    log_ok = (issues['total'] > 0 and issues['mapped'] >= issues['total'])

    regs = maint.get('regulations', []) or []
    reg_threshold = int(maint.get('reg_check_days', 90))
    reg_rows = []; reg_overdue = 0
    for r in regs:
        lc = str(r.get('last_checked', '') or '')
        try:
            ago = (today - datetime.date.fromisoformat(lc)).days
        except Exception:
            ago = None
        overdue = (ago is None) or (ago > reg_threshold)
        if overdue:
            reg_overdue += 1
        reg_rows.append({'id': r.get('id', '?'), 'last': lc or '-', 'ago': ago, 'overdue': overdue})

    review_months = int(maint.get('review_cycle_months', 12))
    review_days = review_months * 30
    last_dates = last_commit_dates([d['_path'] for d in core_docs])
    review_due = []
    for d in core_docs:
        ds = last_dates.get(d['_path'])
        if not ds:
            continue
        try:
            ago = (today - datetime.date.fromisoformat(ds)).days
        except Exception:
            continue
        if ago > review_days:
            review_due.append({'name': str(d.get('doc-id') or d['_name'])[:40],
                               'cat': CATEGORY_LABELS.get(d.get('_category'), d.get('_category')),
                               'last': ds, 'ago': ago})
    review_due.sort(key=lambda x: -x['ago'])

    cad = maint.get('cadence', {}) or {}
    def next_weekly(t):
        days = (7 - t.weekday()) % 7 or 7
        return t + datetime.timedelta(days=days)
    def next_monthly(t):
        y, mo = (t.year, t.month + 1) if t.month < 12 else (t.year + 1, 1)
        return datetime.date(y, mo, 1)
    def next_quarterly(t):
        for mo in (1, 4, 7, 10):
            cand = datetime.date(t.year, mo, 1)
            if cand > t:
                return cand
        return datetime.date(t.year + 1, 1, 1)
    cad_rows = [
        ('일일', '매일 03:18', cad.get('daily_last', '') or today_str, '매 실행'),
        ('주간', '월요일', cad.get('weekly_last', '') or '-', next_weekly(today).isoformat()),
        ('월간', '매월 1일', cad.get('monthly_last', '') or '-', next_monthly(today).isoformat()),
        ('분기', '1·4·7·10월 1일', cad.get('quarterly_last', '') or '-', next_quarterly(today).isoformat()),
    ]

    def kc(cond_red):
        return 'red' if cond_red else 'green'

    H = []
    H.append('<!DOCTYPE html>')
    H.append('<script type="application/json" id="cowork-artifact-meta">')
    H.append('{"name":"MD-process Dashboard","schemaVersion":1,"description":"자율구축+독립감사 — 사실 기반 신뢰도·3소스 백로그·문서통제"}')
    H.append('</script>')
    H.append('<html lang="ko"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">')
    H.append('<title>MD-process 대시보드 (유지보수)</title>')
    H.append('<script src="https://cdn.jsdelivr.net/npm/chart.js@4.5.0/dist/chart.umd.js" integrity="sha384-iU8HYtnGQ8Cy4zl7gbNMOhsDTTKX02BTXptVP/vqAWIaTfM7isw76iyZCsjL2eVi" crossorigin="anonymous"></script>')
    H.append(STYLE)

    H.append('<h1>의료기기 제조 업무규칙 — 자율구축·독립감사 대시보드</h1>')
    H.append(f'<p class="subtitle">마지막 갱신: <strong>{today_str}</strong> · 단계: <strong>유지보수(통제문서 상시 운영)</strong> · <a href="https://github.com/{repo}">GitHub</a> · <a href="https://github.com/{repo}/issues">이슈</a> · <span class="tag tag-green">1차 구축 v0.2+ 완료</span></p>')

    H.append('<div class="actions">')
    H.append('<button onclick="window.print()">\U0001f5a8 인쇄 / PDF 저장</button>')
    H.append(f'<a href="https://github.com/{repo}/raw/main/docs/index.html" download="md-process-dashboard.html">\U0001f4be HTML 다운로드</a>')
    H.append('</div>')

    # ── 사실성·신뢰도 (독립 감사) — 신규 핵심 패널 ──
    _al = parse_audit_log()
    _bk = count_issue_backlog()
    _latest = _al[-1]['pass'] if _al else None
    _tc = sum(r['claims'] for r in _al); _te = sum(r['errors'] for r in _al); _tcit = sum(r['citation'] for r in _al)
    _overall = round((_tc - _te - _tcit) / _tc * 100, 1) if _tc else 0
    def _pk(v):
        return 'green' if v >= 90 else ('yellow' if v >= 70 else 'red')
    H.append('<div class="card" style="border-color:#7c3aed">')
    H.append('<h2 style="color:#a78bfa">\U0001f52c 사실성·신뢰도 (독립 감사 · 1차 출처 재검증)</h2>')
    H.append('<div class="grid">')
    _lp = f'{_latest}%' if _latest is not None else '—'
    H.append(f'<div class="kpi {_pk(_latest if _latest is not None else 0)}"><div class="value">{_lp}</div><div class="label">최신 표본 사실 통과율</div></div>')
    H.append(f'<div class="kpi {kc(_bk["audit_p0_open"]>0)}"><div class="value">{_bk["audit_p0_open"]}</div><div class="label">열린 사실오류(audit P0)</div></div>')
    H.append(f'<div class="kpi"><div class="value">{_te}</div><div class="label">누적 발견 사실오류</div></div>')
    H.append(f'<div class="kpi"><div class="value">{_tc}</div><div class="label">누적 검증 주장</div></div>')
    H.append(f'<div class="kpi green"><div class="value">{_bk["audit_closed"]}</div><div class="label">감사결함 수정완료</div></div>')
    H.append(f'<div class="kpi"><div class="value">{_overall}%</div><div class="label">누적 통과율</div></div>')
    H.append('</div>')
    if len(_al) >= 2:
        H.append('<canvas id="auditTrend" height="90"></canvas>')
    H.append('<p style="font-size:.76rem;color:var(--muted);margin-top:6px">독립 감사관이 빌더 산출물을 <b>1차 출처(법령·규제기관·표준 원문)</b>로 재검증. 통과율 = (검증주장 − 사실오류 − 인용결함)/검증주장. 시험소·컨설팅 자료는 보조(범위)로만 사용.</p>')
    H.append('</div>')
    H.append('<div class="card"><h2>3소스 이슈 백로그 (열림)</h2><table>')
    H.append('<tr><th>소스</th><th>열린 수</th><th>의미</th></tr>')
    H.append(f'<tr><td><b>① audit</b> (감사 결함)</td><td>{_bk["audit_open"]}</td><td>독립 감사가 찾은 미수정 결함 — <b>최우선</b></td></tr>')
    H.append(f'<tr><td>② plan (전략 갭)</td><td>{_bk["plan_open"]}</td><td>ISO 13485 조항완전성 백로그</td></tr>')
    H.append(f'<tr><td>③ emergent (발생)</td><td>{_bk["emergent_open"]}</td><td>실행 중 자가발견</td></tr>')
    H.append('</table>')
    H.append(f'<p style="font-size:.76rem;color:var(--muted);margin-top:6px">우선순위 <b>audit P0 &gt; emergent P0 &gt; plan P1···</b> · 열린 P0 {_bk["p0_open"]} / P1 {_bk["p1_open"]} / P2 {_bk["p2_open"]}</p>')
    H.append('</div>')
    if len(_al) >= 2:
        import json as _json
        _labels = _json.dumps([f"#{i+1}" for i in range(len(_al))])
        _data = _json.dumps([r['pass'] for r in _al])
        H.append("<script>new Chart(document.getElementById('auditTrend'),{type:'line',"
                 f"data:{{labels:{_labels},datasets:[{{label:'사실 통과율%',data:{_data},"
                 "borderColor:'#a78bfa',backgroundColor:'rgba(167,139,250,.15)',fill:true,tension:.3}]},"
                 "options:{responsive:true,plugins:{legend:{labels:{color:'#94a3b8'}}},"
                 "scales:{y:{min:0,max:100,ticks:{color:'#94a3b8'},grid:{color:'#1e293b'}},x:{ticks:{color:'#94a3b8'}}}}});</script>")
    H.append('<div class="grid">')
    H.append(f'<div class="kpi {kc(reg_overdue>0)}"><div class="value">{reg_overdue}/{len(regs)}</div><div class="label">규제 점검만기 경과</div></div>')
    H.append(f'<div class="kpi {kc(fm_rate<100)}"><div class="value">{fm_rate}%</div><div class="label">frontmatter 유효율</div></div>')
    H.append(f'<div class="kpi {kc(not log_ok)}"><div class="value">{"✓" if log_ok else "✗"}</div><div class="label">_log 정합 ({issues["mapped"]}/{issues["total"]})</div></div>')
    H.append(f'<div class="kpi {kc(len(review_due)>0)}"><div class="value">{len(review_due)}</div><div class="label">리뷰 만기 문서</div></div>')
    H.append(f'<div class="kpi {kc(issues["open"]>0)}"><div class="value">{issues["open"]}</div><div class="label">미해결 이슈</div></div>')
    H.append(f'<div class="kpi"><div class="value">{n_core}</div><div class="label">통제 문서 (01~10)</div></div>')
    H.append('</div>')

    H.append('<div class="card"><h2>유지보수 케이던스 현황</h2><table>')
    H.append('<tr><th>주기</th><th>실행 시점</th><th>마지막 실행</th><th>다음 예정</th></tr>')
    for name, when, last, nxt in cad_rows:
        H.append(f'<tr><td>{name}</td><td>{when}</td><td>{last}</td><td>{nxt}</td></tr>')
    H.append('</table></div>')

    H.append('<div class="two-col">')
    H.append('<div class="card"><h2>규제 추적 현황</h2><table>')
    H.append('<tr><th>규제</th><th>최종 확인</th><th>경과</th><th>상태</th></tr>')
    if reg_rows:
        for r in reg_rows:
            ago = '-' if r['ago'] is None else f"{r['ago']}일"
            tag = '<span class="tag tag-yellow">점검 필요</span>' if r['overdue'] else '<span class="tag tag-green">최신</span>'
            H.append(f'<tr><td>{html.escape(str(r["id"]))}</td><td>{html.escape(str(r["last"]))}</td><td>{ago}</td><td>{tag}</td></tr>')
    else:
        H.append('<tr><td colspan="4">규제 목록 미설정 (_dashboard_config.yml maintenance.regulations)</td></tr>')
    H.append('</table></div>')

    H.append('<div class="card"><h2>이슈 상태</h2><canvas id="issueChart" height="160"></canvas>')
    H.append(f'<p style="font-size:.78rem;color:var(--muted);margin-top:8px">총 {issues["total"]}건 중 {issues["closed"]}건 완료 · 미해결 {issues["open"]}건</p>')
    H.append('</div></div>')

    H.append(f'<div class="card"><h2>문서 정기검토 만기 ({len(review_due)}건, 주기 {review_months}개월)</h2><table>')
    H.append('<tr><th>문서</th><th>카테고리</th><th>최종 갱신</th><th>경과</th></tr>')
    if review_due:
        for d in review_due[:15]:
            H.append(f'<tr><td>{html.escape(str(d["name"]))}</td><td>{html.escape(str(d["cat"]))}</td><td>{d["last"]}</td><td>{d["ago"]}일</td></tr>')
        if len(review_due) > 15:
            H.append(f'<tr><td colspan="4">…외 {len(review_due)-15}건</td></tr>')
    else:
        H.append('<tr><td colspan="4">만기 도래 문서 없음 — 전 문서 검토주기 내</td></tr>')
    H.append('</table></div>')

    H.append('<div class="card"><h2>문서통제 정합성</h2><table>')
    H.append(f'<tr><td>frontmatter 유효 문서</td><td>{fm_valid}/{n_total} ({fm_rate}%)</td></tr>')
    H.append(f'<tr><td>frontmatter 결함</td><td>{fm_invalid}건</td></tr>')
    H.append(f'<tr><td>이슈 드래프트 ↔ _log 매핑</td><td>{issues["mapped"]}/{issues["total"]} {"일치" if log_ok else "불일치(매핑 보정 필요)"}</td></tr>')
    H.append('</table></div>')

    H.append('<div class="card"><h2>최근 커밋 (10)</h2><ul class="commit-list">')
    for c in commits[:10]:
        if len(c) < 3:
            continue
        sha, date, msg = c
        H.append(f'<li><span class="date">{date[5:]}</span>{html.escape(msg)[:90]}</li>')
    H.append('</ul></div>')

    H.append('<div class="card"><h2>시스템 정보</h2><div class="schedule-info">')
    H.append('<div>⏰ 매일 03:18 KST (일일 감시·정합성)</div>')
    H.append('<div>\U0001f4c5 주간: 월요일 · 월간: 1일 · 분기: 1·4·7·10월</div>')
    H.append(f'<div>\U0001f4ca 리서치 로그: {sum(1 for d in docs if d.get("_category")=="11_일일_리서치로그")}건</div>')
    H.append(f'<div>✅ 교차검증: {sum(1 for d in docs if d.get("_category")=="12_교차검증_보고서")}건</div>')
    H.append('<div>\U0001f310 GitHub Pages 배포</div>')
    H.append('</div></div>')

    H.append(f"""<script>
new Chart(document.getElementById('issueChart'), {{
  type:'doughnut',
  data:{{labels:['완료 (closed)','미해결 (open)'], datasets:[{{data:[{issues["closed"]}, {issues["open"]}], backgroundColor:['#4ade80','#fbbf24']}}]}},
  options:{{responsive:true, plugins:{{legend:{{labels:{{color:'#94a3b8'}}}}}}}}
}});
</script></body></html>""")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text('\n'.join(H), encoding='utf-8')
    print(f'maintenance dashboard built: {OUT}  ({sum(len(l) for l in H)} bytes)')


def build():
    config = parse_yaml(CONFIG_PATH.read_text(encoding='utf-8')) if CONFIG_PATH.exists() else {}
    if str((config.get('maintenance') or {}).get('phase','')).lower() == 'maintenance':
        return build_maintenance(config)
    proj = config.get('project', {})
    target_cats = config.get('target_categories', [])
    tiers = config.get('tiers', [])

    docs = collect_docs()
    issues = collect_issues()
    commits = git_commits(20)
    velocity = daily_v02_velocity(5)

    # 핵심/전체 카운트
    core_docs = [d for d in docs if d.get('_category') in target_cats]
    log_docs  = [d for d in docs if d.get('_category') in ('11_일일_리서치로그','12_교차검증_보고서')]
    n_core = len(core_docs)
    n_total = len(docs)

    # v0.2+ 보강 카운트
    boosted = [d for d in core_docs if version_to_tuple(d.get('version')) >= (0,2)]
    n_boosted = len(boosted)
    rate = round(n_boosted / n_core * 100) if n_core else 0

    # 카테고리별 보강 진행
    cat_rows = []
    remaining = []
    for cat in target_cats:
        cat_docs = [d for d in core_docs if d.get('_category') == cat]
        cat_b = [d for d in cat_docs if version_to_tuple(d.get('version')) >= (0,2)]
        total = len(cat_docs); done = len(cat_b)
        pct = round(done/total*100) if total else 0
        cat_rows.append({'cat':cat, 'label':CATEGORY_LABELS.get(cat,cat),
                         'total':total,'done':done,'pct':pct})
        for d in cat_docs:
            if version_to_tuple(d.get('version')) < (0,2):
                remaining.append({'cat':cat,'label':CATEGORY_LABELS.get(cat,cat),
                                  'doc_id':d.get('doc-id') or d['_name'][:30],
                                  'title':(d.get('title','') or '').strip().strip('"').strip("'")[:60]})

    # 일정 소화율
    today = datetime.date.today()
    start = datetime.date.fromisoformat(proj.get('start_date','2026-04-16'))
    goal = datetime.date.fromisoformat(proj.get('goal_date','2026-06-01'))
    elapsed = (today - start).days + 1
    total_days = (goal - start).days + 1
    schedule_pct = round(elapsed/total_days*100) if total_days else 0
    remain_days = max(0, (goal - today).days)
    daily_need = round(len(remaining)/remain_days, 1) if remain_days else len(remaining)

    today_str = today.isoformat()

    H = []
    H.append('<!DOCTYPE html>')
    H.append('<script type="application/json" id="cowork-artifact-meta">')
    H.append('{"name":"MD-process Dashboard","schemaVersion":1,"description":"v0.2+ 보강 진행률, 카테고리별 현황, 이슈 상태, 일별 속도 추이"}')
    H.append('</script>')
    H.append('<html lang="ko"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">')
    H.append(f'<title>MD-process 대시보드</title>')
    H.append('<script src="https://cdn.jsdelivr.net/npm/chart.js@4.5.0/dist/chart.umd.js" integrity="sha384-iU8HYtnGQ8Cy4zl7gbNMOhsDTTKX02BTXptVP/vqAWIaTfM7isw76iyZCsjL2eVi" crossorigin="anonymous"></script>')
    H.append("""<style>
:root{--bg:#0f172a;--card:#1e293b;--border:#334155;--text:#e2e8f0;--muted:#94a3b8;--accent:#38bdf8;--green:#4ade80;--yellow:#fbbf24;--red:#f87171;--purple:#a78bfa}
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI','Noto Sans KR',system-ui,sans-serif;padding:20px;line-height:1.5}
h1{font-size:1.4rem;margin-bottom:4px}
.subtitle{color:var(--muted);font-size:.85rem;margin-bottom:20px}
.subtitle a{color:var(--accent);text-decoration:none}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin-bottom:20px}
.kpi{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:16px;text-align:center}
.kpi .value{font-size:1.8rem;font-weight:700;color:var(--accent)}
.kpi .label{font-size:.75rem;color:var(--muted);margin-top:4px}
.kpi.green .value{color:var(--green)}
.kpi.yellow .value{color:var(--yellow)}
.kpi.red .value{color:var(--red)}
.card{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:18px;margin-bottom:16px}
.card h2{font-size:1rem;margin-bottom:12px;color:var(--accent)}
table{width:100%;border-collapse:collapse;font-size:.82rem}
th,td{padding:6px 8px;text-align:left;border-bottom:1px solid var(--border)}
th{color:var(--muted);font-weight:600}
.bar{display:inline-block;height:14px;border-radius:3px;background:var(--accent);transition:width .3s}
.bar-bg{display:inline-block;width:100px;height:14px;border-radius:3px;background:var(--border)}
.tag{display:inline-block;padding:2px 8px;border-radius:4px;font-size:.7rem;font-weight:600}
.tag-green{background:#065f4620;color:var(--green)}
.tag-yellow{background:#78350f20;color:var(--yellow)}
.progress-overall{height:24px;background:var(--border);border-radius:12px;overflow:hidden;margin:8px 0}
.progress-fill{height:100%;background:linear-gradient(90deg,var(--accent),var(--green));display:flex;align-items:center;justify-content:center;font-size:.75rem;font-weight:700;color:var(--bg);border-radius:12px}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:16px}
@media(max-width:700px){.two-col{grid-template-columns:1fr}}
.commit-list{list-style:none;font-size:.8rem}
.commit-list li{padding:4px 0;border-bottom:1px solid var(--border)}
.commit-list .date{color:var(--muted);margin-right:6px}
.schedule-info{display:flex;gap:16px;flex-wrap:wrap;font-size:.82rem}
.schedule-info div{background:var(--bg);padding:8px 12px;border-radius:6px;border:1px solid var(--border)}
.actions{display:flex;gap:8px;margin-bottom:16px;flex-wrap:wrap}
.actions a,.actions button{background:var(--card);border:1px solid var(--border);color:var(--text);padding:6px 12px;border-radius:6px;text-decoration:none;font-size:.8rem;cursor:pointer}
.actions a:hover,.actions button:hover{background:#2d3a52}
@media print{
  body{background:#fff;color:#000;padding:0}
  .card,.kpi{background:#fff;color:#000;border:1px solid #ccc}
  .subtitle,.muted,th{color:#666}
  .actions,.schedule-info{display:none}
  h2{color:#000 !important}
}
</style></head><body>""")

    # 헤더
    H.append(f'<h1>의료기기 제조 업무규칙 — 프로젝트 대시보드</h1>')
    H.append(f'<p class="subtitle">마지막 갱신: <strong>{today_str}</strong> · 자동 실행: 매일 03:18 KST · 연속 실행: {elapsed}일 · <a href="https://github.com/{proj.get("repo","holee9/MD-process")}">GitHub</a> · <a href="https://github.com/{proj.get("repo","holee9/MD-process")}/blob/main/00_%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%EA%B4%80%EB%A6%AC/%EB%AC%B8%EC%84%9C_%EB%A7%A4%ED%8A%B8%EB%A6%AD%EC%8A%A4.md">매트릭스</a> · <a href="https://github.com/{proj.get("repo","holee9/MD-process")}/issues">이슈</a></p>')

    # 액션 버튼
    H.append('<div class="actions">')
    H.append('<button onclick="window.print()">🖨 인쇄 / PDF 저장</button>')
    H.append(f'<a href="https://github.com/{proj.get("repo","holee9/MD-process")}/raw/main/docs/index.html" download="md-process-dashboard.html">💾 HTML 다운로드</a>')
    H.append(f'<a href="https://github.com/{proj.get("repo","holee9/MD-process")}/blob/main/docs/index.html">📋 소스 보기</a>')
    H.append('</div>')

    # KPI
    H.append('<div class="grid">')
    H.append(f'<div class="kpi"><div class="value">{n_core}</div><div class="label">핵심 문서 (01~10)</div></div>')
    H.append(f'<div class="kpi green"><div class="value">{n_boosted}</div><div class="label">v0.2+ 보강 완료</div></div>')
    H.append(f'<div class="kpi green"><div class="value">{rate}%</div><div class="label">심화 보강률</div></div>')
    H.append(f'<div class="kpi"><div class="value">{n_total}</div><div class="label">전체 파일 (로그 포함)</div></div>')
    H.append(f'<div class="kpi"><div class="value">{issues["total"]}</div><div class="label">이슈 드래프트</div></div>')
    H.append(f'<div class="kpi green"><div class="value">{issues["closed"]}</div><div class="label">이슈 완료(closed)</div></div>')
    H.append('</div>')

    # 전체 진행률 바
    H.append('<div class="card">')
    H.append('<h2>전체 진행률 (v0.2+ 보강 기준)</h2>')
    H.append(f'<div class="progress-overall"><div class="progress-fill" style="width:{rate}%">{rate}% ({n_boosted}/{n_core})</div></div>')
    avg_speed = round(sum(v for _,v in velocity[-5:])/max(1,len(velocity[-5:])),1) if velocity else 0
    H.append(f'<p style="font-size:.78rem;color:var(--muted);margin-top:6px">목표: {proj.get("goal_date","-")} {proj.get("goal_description","")} | 일정 소화율: {schedule_pct}% ({elapsed}/{total_days}일) | 잔여 보강: {len(remaining)}문서 | 필요 속도: {daily_need}건/일 | 최근 5일 평균: {avg_speed}건/일</p>')
    H.append('</div>')

    # 카테고리별 + 차트
    H.append('<div class="two-col">')
    H.append('<div class="card"><h2>카테고리별 현황</h2><table>')
    H.append('<tr><th>카테고리</th><th>문서</th><th>v0.2+</th><th>진행</th></tr>')
    for r in cat_rows:
        tag = '<span class="tag tag-green">완료</span>' if r['pct'] == 100 else ''
        H.append(f'<tr><td>{r["label"]}</td><td>{r["total"]}</td><td>{r["done"]}</td>'
                 f'<td><span class="bar-bg"><span class="bar" style="width:{r["pct"]}%"></span></span> {tag}</td></tr>')
    H.append('</table></div>')
    H.append('<div class="card"><h2>카테고리 성숙도 차트</h2><canvas id="catChart" height="220"></canvas></div>')
    H.append('</div>')

    # Tier
    H.append('<div class="card"><h2>Tier 진행 현황</h2><table>')
    H.append('<tr><th>Tier</th><th>카테고리</th><th>상태</th><th>완료/목표</th></tr>')
    for t in tiers:
        cats_str = ', '.join(CATEGORY_LABELS.get(c,c) for c in (t.get('categories') or []))
        if t.get('completed_at'):
            tag = '<span class="tag tag-green">완료</span>'
            date = t.get('completed_at')
        else:
            tag = '<span class="tag tag-yellow">진행중</span>'
            date = f'~{t.get("target_date","-")}'
        H.append(f'<tr><td>{t.get("id","-")}</td><td>{cats_str}</td><td>{tag}</td><td>{date}</td></tr>')
    H.append('</table></div>')

    # 잔여 보강 대상
    if remaining:
        by_cat = collections.defaultdict(list)
        for r in remaining:
            by_cat[r['label']].append(r)
        H.append(f'<div class="card"><h2>잔여 보강 대상 ({len(remaining)}건)</h2><table>')
        H.append('<tr><th>카테고리</th><th>잔여</th><th>문서</th></tr>')
        for label, items in sorted(by_cat.items()):
            docs_str = ', '.join(html.escape(it['doc_id']) for it in items[:5])
            if len(items) > 5: docs_str += f' …외 {len(items)-5}건'
            H.append(f'<tr><td>{html.escape(label)}</td><td>{len(items)}건</td><td>{docs_str}</td></tr>')
        H.append('</table></div>')

    # 최근 작업 + 이슈
    H.append('<div class="two-col">')
    H.append('<div class="card"><h2>최근 커밋 (10)</h2><ul class="commit-list">')
    for c in commits[:10]:
        if len(c) < 3: continue
        sha, date, msg = c
        H.append(f'<li><span class="date">{date[5:]}</span>{html.escape(msg)[:90]}</li>')
    H.append('</ul></div>')
    H.append('<div class="card"><h2>이슈 상태</h2><canvas id="issueChart" height="160"></canvas>')
    H.append(f'<p style="font-size:.78rem;color:var(--muted);margin-top:8px">총 {issues["total"]}건 중 {issues["closed"]}건 완료 ({round(issues["closed"]/max(1,issues["total"])*100)}%)</p>')
    H.append('</div></div>')

    # 보강 속도 추이
    if velocity:
        H.append('<div class="card"><h2>보강 속도 추이 (최근 5일)</h2><canvas id="velChart" height="140"></canvas></div>')

    # 시스템 정보
    H.append('<div class="card"><h2>스케줄 & 시스템 정보</h2><div class="schedule-info">')
    H.append(f'<div>⏰ 매일 03:18 KST 자동 실행</div>')
    H.append(f'<div>📅 시작: {proj.get("start_date","-")}</div>')
    H.append(f'<div>🎯 목표: {proj.get("goal_date","-")}</div>')
    H.append(f'<div>🔄 연속 {elapsed}일 실행</div>')
    H.append(f'<div>📊 리서치 로그: {sum(1 for d in docs if d.get("_category")=="11_일일_리서치로그")}건</div>')
    H.append(f'<div>✅ 교차검증: {sum(1 for d in docs if d.get("_category")=="12_교차검증_보고서")}건</div>')
    H.append(f'<div>🌐 GitHub Pages 배포</div>')
    H.append('</div></div>')

    # Scripts (Chart.js)
    cat_labels_js = json.dumps([r['label'] for r in cat_rows], ensure_ascii=False)
    cat_total_js = json.dumps([r['total'] for r in cat_rows])
    cat_done_js  = json.dumps([r['done']  for r in cat_rows])
    vel_labels_js = json.dumps([d[5:] for d,_ in velocity])
    vel_data_js   = json.dumps([v for _,v in velocity])

    H.append(f"""<script>
new Chart(document.getElementById('catChart'), {{
  type:'bar',
  data:{{labels:{cat_labels_js}, datasets:[
    {{label:'전체 문서',data:{cat_total_js},backgroundColor:'#334155'}},
    {{label:'v0.2+ 보강',data:{cat_done_js},backgroundColor:'#38bdf8'}}
  ]}},
  options:{{responsive:true, plugins:{{legend:{{labels:{{color:'#94a3b8',font:{{size:11}}}}}}}}, scales:{{x:{{ticks:{{color:'#94a3b8',font:{{size:10}}}}}}, y:{{ticks:{{color:'#94a3b8'}}, grid:{{color:'#1e293b'}}}}}}}}
}});
new Chart(document.getElementById('issueChart'), {{
  type:'doughnut',
  data:{{labels:['완료 (closed)','진행중 (open)'], datasets:[{{data:[{issues["closed"]}, {issues["open"]}], backgroundColor:['#4ade80','#fbbf24']}}]}},
  options:{{responsive:true, plugins:{{legend:{{labels:{{color:'#94a3b8'}}}}}}}}
}});""")
    if velocity:
        H.append(f"""new Chart(document.getElementById('velChart'), {{
  type:'line',
  data:{{labels:{vel_labels_js}, datasets:[{{label:'일별 v0.2+ 보강 건수',data:{vel_data_js},borderColor:'#38bdf8',backgroundColor:'#38bdf820',fill:true,tension:0.3}}]}},
  options:{{responsive:true, plugins:{{legend:{{labels:{{color:'#94a3b8'}}}}}}, scales:{{x:{{ticks:{{color:'#94a3b8'}}}}, y:{{beginAtZero:true,ticks:{{color:'#94a3b8'}}, grid:{{color:'#1e293b'}}}}}}}}
}});""")
    H.append('</script></body></html>')

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text('\n'.join(H), encoding='utf-8')
    print(f'✓ dashboard built: {OUT}  ({sum(len(l) for l in H)} bytes)')

if __name__ == '__main__':
    build()
