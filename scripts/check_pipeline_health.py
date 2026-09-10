#!/usr/bin/env python3
"""
파이프라인 생존 감시 (audit #1031).

문제: process-project 스케줄(일 03:18 KST)이 멈추면 감사·주간리포트·매트릭스 재빌드가
      모두 함께 정지하지만 **아무 경보도 발생하지 않는다**. 2026-08-10 이후 약 1개월간
      아무도 정지를 인지하지 못한 사례가 실제로 발생했다.

동작: 저장소의 '생존 신호'(최근 커밋일, 최신 주간 갭분석 리포트일)를 임계일수와 대조해
      초과 시 exit 1 로 CI를 실패시킨다. 리포트 부재를 사람이 눈치채야만 알 수 있는
      구조를 기계 검출로 바꾸는 것이 목적이다.

사용: python3 scripts/check_pipeline_health.py [--max-commit-days N] [--max-report-days N]
"""
import argparse
import datetime
import pathlib
import re
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
CHK_DIR = REPO / '13_규제평가_체크리스트'

DEFAULT_MAX_COMMIT_DAYS = 10   # 일 03:18 스케줄 기준, 10일 무커밋이면 명백한 정지
DEFAULT_MAX_REPORT_DAYS = 14   # 주간 리포트 기준, 2회차 연속 결번이면 경보


def last_commit_date():
    try:
        out = subprocess.run(
            ['git', 'log', '-1', '--format=%cI'],
            cwd=REPO, capture_output=True, text=True, check=True).stdout.strip()
        return datetime.date.fromisoformat(out[:10])
    except Exception:
        return None


def last_weekly_report_date():
    dates = []
    for p in CHK_DIR.glob('주간_갭분석_*.md'):
        m = re.search(r'(\d{4}-\d{2}-\d{2})', p.name)
        if m:
            try:
                dates.append(datetime.date.fromisoformat(m.group(1)))
            except ValueError:
                pass
    return max(dates) if dates else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--max-commit-days', type=int, default=DEFAULT_MAX_COMMIT_DAYS)
    ap.add_argument('--max-report-days', type=int, default=DEFAULT_MAX_REPORT_DAYS)
    args = ap.parse_args()

    today = datetime.date.today()
    problems = []
    lines = []

    c = last_commit_date()
    if c is None:
        problems.append('최근 커밋일을 확인할 수 없음 (git 이력 조회 실패)')
    else:
        age = (today - c).days
        lines.append(f'최근 커밋일: {c} ({age}일 경과, 임계 {args.max_commit_days}일)')
        if age > args.max_commit_days:
            problems.append(
                f'커밋 정지 의심: 마지막 커밋 {c}, {age}일 경과 '
                f'(임계 {args.max_commit_days}일) — process-project 스케줄 실행 여부 확인 필요')

    r = last_weekly_report_date()
    if r is None:
        problems.append('주간 갭분석 리포트를 찾을 수 없음')
    else:
        age = (today - r).days
        lines.append(f'최신 주간 리포트: {r} ({age}일 경과, 임계 {args.max_report_days}일)')
        if age > args.max_report_days:
            problems.append(
                f'주간 리포트 결번: 최신 {r}, {age}일 경과 '
                f'(임계 {args.max_report_days}일) — 리뷰 주기 중단 확인 필요')

    for l in lines:
        print(f'  {l}')

    if problems:
        print('\n=== 파이프라인 생존 점검 실패 ===')
        for p in problems:
            print(f' - {p}')
        print('\n조치: README.md §자동화 시스템의 process-project 스케줄 실행 상태를 확인할 것.')
        sys.exit(1)

    print('\n✓ 파이프라인 생존 점검 통과')
    sys.exit(0)


if __name__ == '__main__':
    main()
