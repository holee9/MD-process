#!/usr/bin/env python3
"""
기존 .md 파일에 frontmatter 메타데이터를 일괄 주입.
- 이미 frontmatter가 있으면 부족한 필드만 보충 (idempotent)
- 적용 제외: README.md, _TEMPLATE.md, _log.json, issue-drafts/*
- 카테고리·doc-id·type·version 등은 파일명·내용 기반 휴리스틱 추정
사용:
  cd <repo>
  python3 scripts/inject_frontmatter.py
"""

import os, re, json, sys, datetime, pathlib, subprocess

REPO = pathlib.Path('.').resolve()
LOG_PATH = REPO / 'issue-drafts' / '_log.json'

# 카테고리 폴더 목록
CATEGORY_DIRS = [
    '00_프로젝트관리','01_법규_규제','02_품질경영시스템_QMS','03_설계_개발관리',
    '04_제조공정_관리','05_검사_시험_밸리데이션','06_문서_기록관리',
    '07_위험관리_ISO14971','08_시판후_감시_PMS','09_공급자_관리','10_교육_훈련',
    '11_일일_리서치로그','12_교차검증_보고서',
]

EXCLUDE_NAMES = {'README.md', '_TEMPLATE.md'}
EXCLUDE_DIRS  = {'issue-drafts', '.github', '.git', 'scripts'}

# 이슈 번호 역색인: doc-id-ish key → issue number
def load_issue_map():
    if not LOG_PATH.exists():
        return {}
    with open(LOG_PATH, encoding='utf-8') as f:
        return json.load(f)

def detect_type(name, content):
    n = name.upper()
    if n.startswith('SOP-') or n.startswith('SOP_') or 'SOP-' in n: return 'SOP'
    if n.startswith('F-') or n.startswith('F_') or '_양식' in name or '양식_' in name: return 'Form'
    if 'CHK-' in n or '체크리스트' in name: return 'Checklist'
    if 'JD-' in n or '직무기술서' in name: return 'JD'
    if '매트릭스' in name or '매핑' in name: return 'Matrix'
    if '계획서' in name: return 'Plan'
    if '_개요.md' in name.lower() or name.endswith('_개요.md'): return 'Overview'
    if '색인' in name or 'INDEX' in n: return 'Index'
    if '_명세' in name: return 'Spec'
    if '교차검증' in name or '_정합성' in name or '갭분석' in name: return 'Report'
    if '리서치' in name or 'LOG-' in n: return 'Log'
    if '규칙' in name or '가이드' in name: return 'Guide'
    if '요약' in name: return 'Guide'
    return 'Guide'

def detect_doc_id(name, type_):
    # SOP-CC-001 패턴 추출
    m = re.search(r'(SOP|F|CHK|JD|GUIDE)-[A-Z0-9]+(?:-\d+)?', name.upper())
    if m: return m.group(0)
    # F-CC-001_005 같은 범위 → F-CC-001
    m = re.search(r'F-[A-Z]+-\d+', name.upper())
    if m: return m.group(0)
    # 파일 stem 단순화
    stem = pathlib.Path(name).stem
    return stem[:60]  # fallback

def detect_version(content):
    m = re.search(r'v\s?(\d+\.\d+)', content)
    if m: return f'v{m.group(1)}'
    return 'v0.1'

def detect_applicable(content):
    found = set()
    patterns = [
        (r'ISO\s*13485[:\s]*(2016)?', 'ISO13485:2016'),
        (r'ISO\s*14971[:\s]*(2019)?', 'ISO14971:2019'),
        (r'IEC\s*62304', 'IEC62304'),
        (r'IEC\s*62366[-\s]*1', 'IEC62366-1'),
        (r'IEC\s*60601[-\s]*1\b', 'IEC60601-1'),
        (r'IEC\s*60601[-\s]*2[-\s]*54', 'IEC60601-2-54'),
        (r'IEC\s*81001[-\s]*5[-\s]*1', 'IEC81001-5-1'),
        (r'21\s*CFR\s*Part\s*820', '21 CFR Part 820'),
        (r'QMSR', 'FDA QMSR'),
        (r'EU\s*MDR|2017/745', 'EU MDR 2017/745'),
        (r'EU\s*AI\s*Act', 'EU AI Act'),
        (r'MFDS', 'MFDS'),
        (r'GSPR', 'EU MDR GSPR'),
        (r'PRRC', 'EU MDR PRRC'),
        (r'UDI', 'UDI'),
        (r'SBOM', 'FDA SBOM'),
        (r'디지털의료제품법', '디지털의료제품법'),
        (r'방사선안전관리규칙|제\s*1122\s*호', '진단용방사선안전관리규칙(제1122호)'),
    ]
    for pat, label in patterns:
        if re.search(pat, content, re.IGNORECASE):
            found.add(label)
    return sorted(found)

def detect_forms(content):
    return sorted(set(re.findall(r'F-[A-Z]+-\d{3}', content)))

def detect_purpose(content, title):
    # 첫 번째 ## 섹션 (개요/목적/배경) 다음 1~2줄
    m = re.search(r'^##\s*(?:목적|개요|배경|purpose|Purpose)\s*\n+(.+?)(?=\n##|\n\n##|\Z)', content, re.M | re.S)
    if m:
        text = m.group(1).strip().split('\n')[0]
        text = re.sub(r'\s+', ' ', text)[:120]
        return text
    return f"{title} 관련 문서"

def get_last_commit_date(filepath):
    try:
        out = subprocess.check_output(
            ['git','log','-1','--format=%ad','--date=short','--', filepath],
            stderr=subprocess.DEVNULL
        ).decode().strip()
        return out or datetime.date.today().isoformat()
    except Exception:
        return datetime.date.today().isoformat()

def parse_existing_frontmatter(content):
    """Return (existing_dict, body_after_frontmatter, has_frontmatter)."""
    if content.startswith('---\n'):
        end = content.find('\n---', 4)
        if end > 0:
            fm_text = content[4:end]
            body = content[end+4:].lstrip('\n')
            existing = {}
            for line in fm_text.split('\n'):
                m = re.match(r'^([a-zA-Z_-]+):\s*(.*)$', line)
                if m:
                    existing[m.group(1)] = m.group(2).strip()
            return existing, body, True
    return {}, content, False

def fmt_yaml_value(v):
    if isinstance(v, list):
        if not v: return '[]'
        if all(isinstance(x, (int, str)) and (isinstance(x, int) or len(x) < 30) for x in v):
            inner = ', '.join(str(x) for x in v)
            return f'[{inner}]'
        # multi-line
        return '\n' + '\n'.join(f'  - {x}' for x in v)
    if isinstance(v, str) and (':' in v or '"' in v or v.startswith('[') or v.startswith('-')):
        return '"' + v.replace('"', '\\"') + '"'
    return str(v)

def build_frontmatter(meta):
    order = ['doc-id','title','type','version','status','category',
             'purpose','applicable','forms','related-docs','related-issues',
             'owner','last-review','review-due']
    lines = ['---']
    for k in order:
        if k in meta and meta[k] not in (None, ''):
            v = meta[k]
            if isinstance(v, list) and not v:
                continue
            line = f'{k}: {fmt_yaml_value(v)}'
            lines.append(line)
    lines.append('---')
    return '\n'.join(lines) + '\n'

def find_related_issues(name, issue_map):
    """Look up the issue numbers where the draft filename references this doc-id or filename."""
    # Heuristic: find drafts that mention the file's stem in title/body, and reverse via issue_map
    stem = pathlib.Path(name).stem
    # quick pass: drafts named after doc-id pattern
    related = []
    for draft_name, issue_num in issue_map.items():
        if stem in draft_name or any(x in draft_name for x in stem.split('_') if len(x) > 3):
            try: related.append(int(issue_num))
            except: pass
    return sorted(set(related))

def process_file(path, issue_map, dry_run=False):
    content = path.read_text(encoding='utf-8')
    existing, body, had_fm = parse_existing_frontmatter(content)
    rel = path.relative_to(REPO)
    name = path.name

    title_existing = existing.get('title', '').strip().strip('"').strip("'")
    if not title_existing:
        # extract first H1 or filename
        m = re.search(r'^#\s+(.+)$', body, re.M)
        title_existing = m.group(1).strip() if m else pathlib.Path(name).stem

    type_ = existing.get('type') or detect_type(name, body)
    doc_id = existing.get('doc-id') or detect_doc_id(name, type_)
    version = existing.get('version') or detect_version(body)
    status = existing.get('status') or 'draft'
    category = existing.get('category') or rel.parts[0]
    purpose = existing.get('purpose') or detect_purpose(body, title_existing)
    applicable = detect_applicable(body) if 'applicable' not in existing else None
    forms = detect_forms(body) if 'forms' not in existing else None
    related = find_related_issues(name, issue_map) if 'related-issues' not in existing else None
    last_review = existing.get('last-review') or get_last_commit_date(str(rel))
    review_due = existing.get('review-due')
    if not review_due:
        try:
            d = datetime.date.fromisoformat(last_review)
            review_due = (d.replace(year=d.year+1)).isoformat()
        except:
            review_due = ''
    owner = existing.get('owner') or 'TBD'

    # Log files: lighter frontmatter
    if type_ == 'Log' or category in ('11_일일_리서치로그', '12_교차검증_보고서'):
        meta = {
            'doc-id': existing.get('doc-id') or f"LOG-{pathlib.Path(name).stem[:30]}",
            'title': title_existing,
            'type': 'Log' if category == '11_일일_리서치로그' else 'Report',
            'category': category,
            'purpose': purpose,
            'last-review': last_review,
        }
    else:
        meta = {
            'doc-id': doc_id,
            'title': title_existing,
            'type': type_,
            'version': version,
            'status': status,
            'category': category,
            'purpose': purpose,
            'applicable': applicable if applicable else existing.get('applicable_raw', []),
            'forms': forms if forms else [],
            'related-docs': [],
            'related-issues': related if related is not None else [],
            'owner': owner,
            'last-review': last_review,
            'review-due': review_due,
        }

    new_fm = build_frontmatter(meta)
    new_content = new_fm + '\n' + body

    if new_content == content:
        return False
    if dry_run:
        print(f"  [WOULD UPDATE] {rel}")
    else:
        path.write_text(new_content, encoding='utf-8')
        print(f"  ✓ {rel}")
    return True

def main():
    issue_map = load_issue_map()
    print(f"issue map entries: {len(issue_map)}")
    targets = []
    for cat in CATEGORY_DIRS:
        d = REPO / cat
        if not d.exists(): continue
        for p in d.rglob('*.md'):
            if p.name in EXCLUDE_NAMES: continue
            targets.append(p)
    # Root README skipped (kept manual)
    print(f"target files: {len(targets)}")
    updated = 0
    for p in targets:
        if process_file(p, issue_map):
            updated += 1
    print(f"\nupdated: {updated}/{len(targets)}")

if __name__ == '__main__':
    main()
