#!/usr/bin/env python3
"""
주간 갭분석 리포트 결정론적 생성기 (audit #1035).

배경: 주간 리포트가 AI 사이클(로컬 PC 스케줄)에만 의존해, PC가 꺼지면
10-23·10-30 회차처럼 결번이 발생했다. 본 스크립트는 LLM 없이 저장소 데이터만으로
리포트를 생성하므로 GitHub Actions에서 무조건 실행된다.

입력: 13_규제평가_체크리스트/_readiness.json (현재) + git 이력상 7/14/28일 전 스냅샷
출력: 13_규제평가_체크리스트/주간_갭분석_<오늘>.md  (이미 있으면 덮어쓰지 않음)
"""
import datetime, json, pathlib, re, subprocess, sys, collections

REPO = pathlib.Path(__file__).resolve().parent.parent
CHK = REPO / '13_규제평가_체크리스트'
RJ = '13_규제평가_체크리스트/_readiness.json'

def git(*a):
    return subprocess.run(['git', *a], cwd=REPO, capture_output=True, text=True).stdout

def snapshot(days):
    """N일 전 시점의 _readiness.json (없으면 None)."""
    rev = git('rev-list', '-1', f'--before={days} days ago', 'HEAD').strip()
    if not rev: return None
    raw = git('show', f'{rev}:{RJ}')
    try: return json.loads(raw)
    except Exception: return None

def score(d, k):
    try: return d['standards'][k]['score']
    except Exception: return None

def unmet(d, k):
    try: return d['standards'][k]['unmet_must']
    except Exception: return None

def avg(d):
    if not d: return None
    s = [v['score'] for v in d['standards'].values()]
    return round(sum(s) / len(s)) if s else None

def fmt(v, suf='%'):
    return '—' if v is None else f'{v}{suf}'

def delta(a, b):
    if a is None or b is None: return '—'
    x = a - b
    return '0' if x == 0 else f'{x:+d}'

def main():
    today = datetime.date.today()
    out = CHK / f'주간_갭분석_{today.isoformat()}.md'
    if out.exists() and '--force' not in sys.argv:
        print(f'이미 존재: {out.name} — 생성 생략'); return 0

    cur = json.loads((REPO / RJ).read_text(encoding='utf-8'))
    w1, w2, w4 = snapshot(7), snapshot(14), snapshot(28)
    stds = list(cur['standards'].keys())

    # 1. 점수표
    rows = []
    for k in stds:
        rows.append(f"| {k[:40]} | {fmt(score(w1,k))} | **{fmt(score(cur,k))}** | {delta(score(cur,k), score(w1,k))} | {unmet(cur,k)} ({delta(unmet(cur,k), unmet(w1,k))}) |")
    rows.append(f"| **종합(단순평균)** | {fmt(avg(w1))} | **{fmt(avg(cur))}** | {delta(avg(cur), avg(w1))} | {cur.get('all_unmet_must')} |")

    # 정체 판정: 4주간 종합 변화 0
    stall = []
    if avg(w4) is not None and avg(cur) == avg(w4) and avg(w1) == avg(cur):
        stall.append(f'- ⚠ **종합 점수 4주 이상 변동 없음**({fmt(avg(cur))}). 감사(정정)만 진행되고 보강이 지표에 반영되지 않는 패턴 — 보강 담당 지정 필요.')
    if w1 and cur.get('all_unmet_must') == w1.get('all_unmet_must'):
        stall.append(f"- must 미충족 {cur.get('all_unmet_must')}건 — 7일간 순감소 0건.")

    # 2. 활동
    since = (today - datetime.timedelta(days=7)).isoformat()
    log = git('log', f'--since={since}', '--format=%an\t%s').splitlines()
    by_kind = collections.Counter()
    audits = set()
    for line in log:
        _, _, s = line.partition('\t')
        m = re.match(r'(\w+)', s); by_kind[m.group(1) if m else '기타'] += 1
        audits.update(re.findall(r'#(1\d{3})', s))
    days_active = len(set(git('log', f'--since={since}', '--format=%cd', '--date=short').split()))
    kinds = ', '.join(f'{k} {v}' for k, v in by_kind.most_common()) or '없음'

    # 3. 미충족 must 상위
    rep = (CHK / '_readiness_report.md').read_text(encoding='utf-8') if (CHK / '_readiness_report.md').exists() else ''
    gaps = []
    for l in rep.splitlines():
        c = [x.strip() for x in l.split('|')]
        if len(c) > 6 and c[4] == 'must' and not c[5].startswith('충족'):
            gaps.append(f'| {c[1]} | {c[3][:60]} | {c[5]} |')
    open_drafts = sum(1 for p in (REPO / 'issue-drafts').glob('[0-9]*.md')
                      if not re.search(r'^state:\s*closed', p.read_text(encoding='utf-8', errors='ignore'), re.M))

    body = f"""---
doc-id: WGAP-{today.isoformat()}
title: 주간 갭분석 — {today.isoformat()}
type: Report
category: 13_규제평가_체크리스트
purpose: 주간 규제 준비도 변동 추적·우선순위 재정렬 (자동 생성)
owner: RA 담당자
last-review: {today.isoformat()}
---

# 주간 갭분석 — {today.isoformat()}

> **자동 생성** — `scripts/build_weekly_report.py` (GitHub Actions `scheduled-maintenance.yml`). 저장소 데이터만으로 산출하며 해석·판단 문장은 포함하지 않는다. 비교 기준: 7일 전 `_readiness.json`.

## 1. 종합 점수 변동

| 표준 | 7일 전 | 현재 | 변동 | must 미충족 (변동) |
|---|---|---|---|---|
{chr(10).join(rows)}

{chr(10).join(stall) if stall else '- 정체 경고 없음.'}

## 2. 지난 7일 활동

| 지표 | 값 |
|---|---|
| 커밋 | {len(log)}건 ({kinds}) |
| 커밋 발생일 | {days_active}/7일 |
| 언급된 감사 이슈 | {', '.join('#'+a for a in sorted(audits)) or '없음'} |
| open 이슈 드래프트 | {open_drafts}건 |

{'- ⚠ **7일간 커밋 없음** — 사이클 정지 의심.' if not log else ''}

## 3. 미충족 must 항목 (상위 15)

| ID | 요구사항 | 상태 |
|---|---|---|
{chr(10).join(gaps[:15]) if gaps else '| — | 없음 | — |'}

## 첨부

- `_readiness_report.md` — 상세 평가 / `_readiness.json` — 구조화 메트릭
"""
    out.write_text(body, encoding='utf-8')
    print(f'✓ 생성: {out.name}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
