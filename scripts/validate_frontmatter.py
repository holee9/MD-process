#!/usr/bin/env python3
"""
모든 카테고리 문서의 frontmatter 스키마 검증.
- 필수 필드 누락 / enum 위반 / doc-id 중복 / YAML 파싱 오류 검출
- 위반 시 exit 1 (CI 실패)
- issue-drafts/, README.md, _TEMPLATE.md, 11_/12_ 의 경량 frontmatter는 별도 규칙
"""

import os, re, sys, pathlib, collections

REPO = pathlib.Path('.').resolve()

FULL_CATEGORIES = [
    '00_프로젝트관리','01_법규_규제','02_품질경영시스템_QMS','03_설계_개발관리',
    '04_제조공정_관리','05_검사_시험_밸리데이션','06_문서_기록관리',
    '07_위험관리_ISO14971','08_시판후_감시_PMS','09_공급자_관리','10_교육_훈련',
]
LOG_CATEGORIES = ['11_일일_리서치로그','12_교차검증_보고서']

EXCLUDE_NAMES = {'README.md','_TEMPLATE.md','문서_매트릭스.md'}

VALID_TYPES = {'SOP','Procedure','Form','Checklist','Matrix','Plan','Report','Guide','Spec','JD','Index','Overview','Log'}
VALID_STATUS = {'draft','review','approved','released','obsolete'}

def parse_fm(text):
    if not text.startswith('---\n'): return None
    end = text.find('\n---', 4)
    if end < 0: return None
    fm = {}
    cur_key = None
    for line in text[4:end].split('\n'):
        if not line.strip():
            cur_key = None; continue
        m = re.match(r'^([a-zA-Z_-]+):\s*(.*)$', line)
        if m:
            k = m.group(1); v = m.group(2).strip()
            if v.startswith('[') and v.endswith(']'):
                v = [x.strip() for x in v[1:-1].split(',') if x.strip()]
            fm[k] = v
            cur_key = k
        elif line.startswith('  - ') and cur_key:
            if not isinstance(fm.get(cur_key), list): fm[cur_key] = []
            fm[cur_key].append(line[4:].strip())
    return fm

def check_full(fm, path, errors):
    required = ['doc-id','title','type','version','status','category','purpose']
    for f in required:
        if f not in fm or not fm[f]:
            errors.append(f'{path}: 필수 필드 누락: {f}')
    if fm.get('type') and fm['type'] not in VALID_TYPES:
        errors.append(f'{path}: type 위반: {fm["type"]} (허용: {sorted(VALID_TYPES)})')
    if fm.get('status') and fm['status'] not in VALID_STATUS:
        errors.append(f'{path}: status 위반: {fm["status"]} (허용: {sorted(VALID_STATUS)})')

def check_log(fm, path, errors):
    required = ['doc-id','title','type','category']
    for f in required:
        if f not in fm or not fm[f]:
            errors.append(f'{path}: 필수 필드 누락 (log): {f}')
    if fm.get('type') not in {'Log','Report'}:
        errors.append(f'{path}: log/report type 위반: {fm.get("type")}')

def main():
    errors = []
    seen_ids = collections.defaultdict(list)

    for cat in FULL_CATEGORIES:
        d = REPO / cat
        if not d.exists(): continue
        for p in d.rglob('*.md'):
            if p.name in EXCLUDE_NAMES: continue
            text = p.read_text(encoding='utf-8')
            fm = parse_fm(text)
            if fm is None:
                errors.append(f'{p.relative_to(REPO)}: frontmatter 없음')
                continue
            check_full(fm, str(p.relative_to(REPO)), errors)
            if 'doc-id' in fm: seen_ids[fm['doc-id']].append(str(p.relative_to(REPO)))

    for cat in LOG_CATEGORIES:
        d = REPO / cat
        if not d.exists(): continue
        for p in d.rglob('*.md'):
            if p.name in EXCLUDE_NAMES: continue
            text = p.read_text(encoding='utf-8')
            fm = parse_fm(text)
            if fm is None:
                errors.append(f'{p.relative_to(REPO)}: frontmatter 없음 (log)')
                continue
            check_log(fm, str(p.relative_to(REPO)), errors)

    # doc-id 중복 검사 (Log 제외)
    for did, paths in seen_ids.items():
        if len(paths) > 1:
            errors.append(f'doc-id 중복 [{did}]: ' + ' | '.join(paths))

    if errors:
        print('=== Frontmatter 검증 실패 ===')
        for e in errors[:50]:
            print(' -', e)
        if len(errors) > 50: print(f'   ... 외 {len(errors)-50}건')
        sys.exit(1)
    else:
        print('✓ Frontmatter 검증 통과')

if __name__ == '__main__':
    main()
