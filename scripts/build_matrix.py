#!/usr/bin/env python3
"""
모든 .md 문서의 frontmatter를 읽어 매트릭스 문서 자동 생성.
출력: 00_프로젝트관리/문서_매트릭스.md (전체 표 + 카테고리별·유형별 섹션)
"""

import os, re, json, pathlib, datetime, sys, collections

REPO = pathlib.Path('.').resolve()
OUT  = REPO / '00_프로젝트관리' / '문서_매트릭스.md'

CATEGORY_DIRS = [
    '00_프로젝트관리','01_법규_규제','02_품질경영시스템_QMS','03_설계_개발관리',
    '04_제조공정_관리','05_검사_시험_밸리데이션','06_문서_기록관리',
    '07_위험관리_ISO14971','08_시판후_감시_PMS','09_공급자_관리','10_교육_훈련',
    '11_일일_리서치로그','12_교차검증_보고서',
]

EXCLUDE_NAMES = {'README.md', '_TEMPLATE.md', '문서_매트릭스.md'}

def parse_frontmatter(text):
    if not text.startswith('---\n'):
        return None, text
    end = text.find('\n---', 4)
    if end < 0:
        return None, text
    fm_text = text[4:end]
    body = text[end+4:].lstrip('\n')
    fm = {}
    cur_key = None
    for line in fm_text.split('\n'):
        if not line.strip():
            cur_key = None
            continue
        m = re.match(r'^([a-zA-Z_-]+):\s*(.*)$', line)
        if m:
            k = m.group(1)
            v = m.group(2).strip()
            # parse list inline [a, b, c]
            if v.startswith('[') and v.endswith(']'):
                v = [x.strip() for x in v[1:-1].split(',') if x.strip()]
            fm[k] = v
            cur_key = k
        elif line.startswith('  - ') and cur_key:
            v = line[4:].strip()
            if not isinstance(fm.get(cur_key), list):
                fm[cur_key] = []
            fm[cur_key].append(v)
    return fm, body

def collect():
    docs = []
    for cat in CATEGORY_DIRS:
        d = REPO / cat
        if not d.exists(): continue
        for p in sorted(d.rglob('*.md')):
            if p.name in EXCLUDE_NAMES: continue
            try:
                text = p.read_text(encoding='utf-8')
            except UnicodeDecodeError:
                continue
            fm, _ = parse_frontmatter(text)
            if fm is None: 
                continue
            fm['_path']     = str(p.relative_to(REPO))
            fm['_filename'] = p.name
            fm['_category'] = cat
            docs.append(fm)
    return docs

def fmt_list(v, sep=', '):
    if not v: return ''
    if isinstance(v, list): return sep.join(str(x) for x in v)
    return str(v)

def md_link(text, path):
    # encode path for markdown link (spaces, parens)
    p = path.replace(' ', '%20').replace('(', '%28').replace(')', '%29')
    return f'[{text}]({p})'

def build():
    docs = collect()
    today = datetime.date.today().isoformat()
    out = []
    out.append(f"# 문서 매트릭스 (자동 생성)\n")
    out.append(f"> **생성일:** {today} · **문서 총수:** {len(docs)} · **출처:** 각 문서의 frontmatter\n")
    out.append(f"> 본 파일은 `scripts/build_matrix.py`에 의해 자동 생성됩니다. 수동 편집 금지.\n")

    # === 종합 통계 ===
    by_type = collections.Counter(d.get('type','?') for d in docs)
    by_cat  = collections.Counter(d.get('_category','?') for d in docs)
    by_status = collections.Counter(d.get('status','-') for d in docs)
    out.append("## 1. 종합 통계\n")
    out.append("### 1.1 카테고리별\n")
    out.append("| 카테고리 | 문서 수 |")
    out.append("|---|---:|")
    for cat in CATEGORY_DIRS:
        out.append(f"| {cat} | {by_cat.get(cat, 0)} |")
    out.append("")
    out.append("### 1.2 유형별\n")
    out.append("| Type | Count |")
    out.append("|---|---:|")
    for t, c in sorted(by_type.items(), key=lambda x:-x[1]):
        out.append(f"| {t} | {c} |")
    out.append("")
    out.append("### 1.3 상태별\n")
    out.append("| Status | Count |")
    out.append("|---|---:|")
    for s, c in sorted(by_status.items()):
        out.append(f"| {s or '-'} | {c} |")
    out.append("")

    # === 카테고리 × 유형 cross-tab ===
    types = sorted({d.get('type','?') for d in docs})
    out.append("### 1.4 카테고리 × 유형 매트릭스\n")
    header = "| 카테고리 \\ 유형 | " + " | ".join(types) + " | **합계** |"
    sep    = "|---|" + "|".join([':---:']*len(types)) + "|---:|"
    out.append(header); out.append(sep)
    for cat in CATEGORY_DIRS:
        row = [cat]
        total = 0
        for t in types:
            n = sum(1 for d in docs if d.get('_category')==cat and d.get('type')==t)
            row.append(str(n) if n else '·')
            total += n
        row.append(f"**{total}**")
        out.append("| " + " | ".join(row) + " |")
    out.append("")

    # === 표준별 충족 문서 ===
    std_docs = collections.defaultdict(list)
    for d in docs:
        for std in (d.get('applicable') or []):
            std_docs[std].append(d)
    if std_docs:
        out.append("## 2. 표준·법규별 충족 문서\n")
        out.append("| 표준·법규 | 문서 수 | 대표 문서 |")
        out.append("|---|---:|---|")
        for std in sorted(std_docs.keys()):
            ds = std_docs[std]
            sample = ', '.join((d.get('doc-id') or pathlib.Path(d['_filename']).stem)[:25] for d in ds[:3])
            out.append(f"| {std} | {len(ds)} | {sample}{'…' if len(ds)>3 else ''} |")
        out.append("")

    # === 전체 문서 매트릭스 (메인) ===
    out.append("## 3. 전체 문서 매트릭스\n")
    out.append("| Doc ID | 제목 | Type | 버전 | Status | 카테고리 | 적용 표준 | Forms | Issues | Owner | Review-due |")
    out.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for d in sorted(docs, key=lambda d:(d.get('_category',''), d.get('doc-id') or d['_filename'])):
        title = (d.get('title') or '').strip().strip('"').strip("'")
        title = title.replace('|','\\|')[:80]
        ttype = d.get('type','-')
        ver = d.get('version','-') if ttype not in ('Log','Report') else '-'
        status = d.get('status','-') if ttype not in ('Log','Report') else '-'
        cat = d.get('_category','-').split('_',1)[0]
        appl = fmt_list(d.get('applicable'), ', ')[:80]
        forms = fmt_list(d.get('forms'), ', ')[:40]
        issues = fmt_list(d.get('related-issues'), ', ')[:30]
        owner = d.get('owner','-')[:20]
        rdue = d.get('review-due','-')
        link = md_link(d.get('doc-id') or d['_filename'][:24], d['_path'])
        out.append(f"| {link} | {title} | {ttype} | {ver} | {status} | {cat} | {appl} | {forms} | {issues} | {owner} | {rdue} |")
    out.append("")

    # === 카테고리별 문서 (간이) ===
    out.append("## 4. 카테고리별 문서 목록\n")
    for cat in CATEGORY_DIRS:
        cat_docs = [d for d in docs if d.get('_category')==cat]
        if not cat_docs: continue
        out.append(f"### {cat} ({len(cat_docs)}건)\n")
        out.append("| Doc ID | 제목 | Type | Ver | 용도 |")
        out.append("|---|---|---|---|---|")
        for d in sorted(cat_docs, key=lambda d:d.get('doc-id') or d['_filename']):
            title = (d.get('title') or '').strip().strip('"').strip("'")[:60].replace('|','\\|')
            purpose = (d.get('purpose') or '').strip().strip('"').strip("'")[:80].replace('|','\\|')
            link = md_link(d.get('doc-id') or d['_filename'][:24], d['_path'])
            out.append(f"| {link} | {title} | {d.get('type','-')} | {d.get('version','-')} | {purpose} |")
        out.append("")

    return '\n'.join(out)

def main():
    content = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(content, encoding='utf-8')
    print(f"✓ matrix written: {OUT}  ({content.count(chr(10))} lines)")

if __name__ == '__main__':
    main()
