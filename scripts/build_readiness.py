#!/usr/bin/env python3
"""
규제 준비도 자동 갭 분석.
- 13_규제평가_체크리스트/<표준>.md 의 YAML 항목 수집
- 각 항목의 applicable_keywords × 전체 문서 frontmatter.applicable 매핑
- 표준별 점수 + 항목별 충족/미충족 상세
출력:
  - 13_규제평가_체크리스트/_readiness_report.md  (사람 가독)
  - 13_규제평가_체크리스트/_readiness.json       (대시보드용)
"""
import os, re, json, pathlib, datetime, collections

REPO = pathlib.Path('.').resolve()
CHK_DIR = REPO / '13_규제평가_체크리스트'
OUT_MD  = CHK_DIR / '_readiness_report.md'
OUT_JSON = CHK_DIR / '_readiness.json'

CATEGORY_DIRS = [
    '00_프로젝트관리','01_법규_규제','02_품질경영시스템_QMS','03_설계_개발관리',
    '04_제조공정_관리','05_검사_시험_밸리데이션','06_문서_기록관리',
    '07_위험관리_ISO14971','08_시판후_감시_PMS','09_공급자_관리','10_교육_훈련',
]

SEVERITY_WEIGHT = {'must':1.0,'should':0.5,'may':0.2}

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

def collect_all_docs():
    """전체 문서: doc-id, type, applicable 수집"""
    docs = []
    for cat in CATEGORY_DIRS:
        d = REPO/cat
        if not d.exists(): continue
        for p in sorted(d.rglob('*.md')):
            if p.name in ('README.md','_TEMPLATE.md','문서_매트릭스.md'): continue
            try: text = p.read_text(encoding='utf-8')
            except: continue
            fm = parse_fm(text) or {}
            docs.append({
                'doc_id': fm.get('doc-id') or p.stem,
                'type': fm.get('type','-'),
                'category': cat,
                'applicable': fm.get('applicable') or [],
                'path': str(p.relative_to(REPO)),
            })
    return docs

def parse_checklist_items(checklist_md_text):
    """YAML 코드블록 안의 - id: 형식 항목 수집 (yaml 라이브러리 사용)"""
    import yaml
    items = []
    # 모든 ```yaml ... ``` 블록 추출
    for m in re.finditer(r'```yaml\n(.*?)\n```', checklist_md_text, re.S):
        try:
            data = yaml.safe_load(m.group(1))
            if isinstance(data, list):
                for it in data:
                    if isinstance(it, dict) and 'id' in it:
                        items.append(it)
        except Exception as e:
            print(f"  YAML 파싱 오류: {e}")
    return items

def collect_checklists():
    """모든 체크리스트 파일 스캔"""
    standards = {}
    for p in sorted(CHK_DIR.glob('*.md')):
        if p.name in ('README.md',) or p.name.startswith('_') or p.name.startswith('주간'): continue
        text = p.read_text(encoding='utf-8')
        fm = parse_fm(text) or {}
        items = parse_checklist_items(text)
        std_name = fm.get('title') or p.stem
        standards[std_name] = {
            'doc_id': fm.get('doc-id') or p.stem,
            'file': p.name,
            'items': items,
        }
    return standards

def score_item(item, all_docs):
    """1개 항목의 충족 점수 산출"""
    # 체크리스트에 명시적으로 선언된 status 우선 적용 (#1521 버그 수정)
    declared = item.get('status', '')
    if declared == 'unmet':
        return {'score': 0, 'status': '미충족(확인됨)', 'matches': []}
    if declared == 'na':
        return {'score': None, 'status': 'N/A', 'matches': []}

    keywords = item.get('applicable_keywords') or []
    if not keywords:
        return {'score': 0, 'status':'키워드 미정', 'matches':[]}
    matches = []
    for d in all_docs:
        for k in keywords:
            if any(k.lower() in str(a).lower() for a in d['applicable']):
                matches.append(d)
                break
    if not matches:
        return {'score':0, 'status':'미충족', 'matches':[]}

    ev_type = item.get('evidence_type','')
    # Form/Checklist 필요 시 해당 type 문서가 있는지
    if ev_type in ('form',) and not any(m['type'] in ('Form',) for m in matches):
        return {'score':50, 'status':'부분(양식 없음)', 'matches':matches}
    if ev_type in ('SOP','sop') and not any(m['type']=='SOP' for m in matches):
        return {'score':70, 'status':'부분(SOP 미작성)', 'matches':matches}
    if len(matches) >= 2:
        raw_score = 100
    else:
        raw_score = 80
    # 선언된 partial 상태는 키워드 매칭 점수를 60으로 상한 (#1521)
    if declared == 'partial':
        return {'score': min(raw_score, 60), 'status': '부분충족(선언)', 'matches': matches}
    return {'score': raw_score, 'status': '충족', 'matches': matches}

def calculate_score(items, all_docs):
    if not items: return 0, []
    total_w = 0; weighted = 0; details = []
    for it in items:
        sev = it.get('severity','should')
        w = SEVERITY_WEIGHT.get(sev, 0.5)
        r = score_item(it, all_docs)
        if r['score'] is None:  # N/A 항목 — 가중치 합산 제외
            details.append({**it, **r})
            continue
        weighted += r['score'] * w
        total_w += w
        details.append({**it, **r})
    return (round(weighted/total_w) if total_w else 0), details

def main():
    all_docs = collect_all_docs()
    standards = collect_checklists()
    today = datetime.date.today().isoformat()

    report_md = [f"# 규제 준비도 자동 갭 분석\n\n> **생성일:** {today} · **출처:** `13_규제평가_체크리스트/*.md` × 전체 문서 frontmatter\n> 본 파일은 자동 생성. 수동 편집 금지.\n"]
    report_md.append("## 종합 점수\n")
    report_md.append("| 표준 | 점수 | 항목 | must 미충족 |")
    report_md.append("|---|---:|---:|---:|")

    json_out = {'generated_at': today, 'standards': {}, 'all_items': 0, 'all_unmet_must': 0}
    total_items = 0; total_unmet_must = 0

    for std_name, std in standards.items():
        items = std['items']
        score, details = calculate_score(items, all_docs)
        unmet_must = sum(1 for d in details if d.get('severity')=='must' and d['score']<100)
        total_items += len(items); total_unmet_must += unmet_must
        bar = '█'*(score//10) + '░'*(10-score//10)
        report_md.append(f"| {std_name[:50]} | {score}% `{bar}` | {len(items)} | {unmet_must} |")
        json_out['standards'][std_name] = {
            'score': score, 'items': len(items), 'unmet_must': unmet_must, 'file': std['file'],
        }

    json_out['all_items'] = total_items
    json_out['all_unmet_must'] = total_unmet_must

    # 항목별 상세
    report_md.append("\n## 표준별 항목 상세\n")
    for std_name, std in standards.items():
        score, details = calculate_score(std['items'], all_docs)
        report_md.append(f"### {std_name} — {score}%\n")
        report_md.append("| ID | 조항 | 요구사항 | severity | 상태 | 매칭 문서 |")
        report_md.append("|---|---|---|---|---|---|")
        for d in details:
            matches_str = ', '.join((m['doc_id'] or '-')[:20] for m in d.get('matches',[])[:3])
            if len(d.get('matches',[])) > 3:
                matches_str += f' …외 {len(d["matches"])-3}건'
            report_md.append(f"| {d.get('id','-')} | {d.get('clause','-')} | {(d.get('requirement','-') or '')[:80]} | {d.get('severity','-')} | {d.get('status','-')} | {matches_str or '없음'} |")
        report_md.append("")

    OUT_MD.write_text('\n'.join(report_md), encoding='utf-8')
    OUT_JSON.write_text(json.dumps(json_out, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"✓ readiness report: {OUT_MD}  ({len(standards)} 표준, {total_items} 항목, {total_unmet_must} must 미충족)")

if __name__ == '__main__':
    main()
