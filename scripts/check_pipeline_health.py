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
DEFAULT_MAX_DIRTY_FILES = 0    # 사이클 종료 시 워킹트리는 비어 있어야 정상


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


def lock_state():
    """(잔존 락 수, 잔재 수) 반환. (audit #1034)

    락이 남아 있으면 이후 모든 git 쓰기 명령이 즉사하므로, 정지의 선행 신호다.
    잔재(.lock.bak/.old/.stale 등)는 과거 세션이 손으로 치운 흔적으로,
    누적된다는 것 자체가 같은 문제가 반복되고 있다는 증거다.
    """
    gd = REPO / '.git'
    try:
        locks = list(gd.glob('*.lock')) + list(gd.glob('refs/heads/*.lock'))
        debris = [p for p in gd.glob('*.lock.*')]
        return len(locks), len(debris)
    except Exception:
        return None, None


def working_tree_state():
    """(변경파일수, 미push커밋수) 반환. 조회 실패 시 (None, None).

    (audit #1033) 2026-09-18 사례: 야간 사이클이 작업은 마쳤으나 커밋 단계에서 멈춰
    12개 파일이 워킹트리에 방치됐고, 커밋일 기준 점검만으로는 이를 잡지 못했다.
    '산출은 됐는데 반영이 안 된' 상태를 별도 신호로 감시한다.
    """
    dirty = unpushed = None
    try:
        out = subprocess.run(['git', 'status', '--porcelain'],
                             cwd=REPO, capture_output=True, text=True, check=True).stdout
        dirty = len([l for l in out.splitlines() if l.strip()])
    except Exception:
        pass
    try:
        out = subprocess.run(['git', 'log', '@{u}..HEAD', '--oneline'],
                             cwd=REPO, capture_output=True, text=True, check=True).stdout
        unpushed = len([l for l in out.splitlines() if l.strip()])
    except Exception:
        pass
    return dirty, unpushed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--max-commit-days', type=int, default=DEFAULT_MAX_COMMIT_DAYS)
    ap.add_argument('--max-report-days', type=int, default=DEFAULT_MAX_REPORT_DAYS)
    ap.add_argument('--max-dirty-files', type=int, default=DEFAULT_MAX_DIRTY_FILES,
                    help='워킹트리 미커밋 파일 허용 상한 (기본 0 = 커밋 누락 즉시 경보)')
    ap.add_argument('--skip-local', action='store_true',
                    help='로컬 워킹트리/미push 점검 생략 (GitHub Actions 등 클론 환경용)')
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

    if not args.skip_local:
        locks, debris = lock_state()
        if locks is not None:
            lines.append(f'git 락 잔존: {locks}건 / 정리 잔재: {debris}건')
            if locks > 0:
                problems.append(
                    f'git 락 {locks}건 잔존 — 이 상태에서는 모든 git 쓰기 명령이 실패한다. '
                    f'`bash scripts/git_safe.sh --clean` 으로 정리할 것')
            if debris > 10:
                problems.append(
                    f'락 정리 잔재 {debris}건 누적 — 같은 문제가 반복되고 있다는 신호. '
                    f'사이클이 scripts/run_cycle.sh(마운트 밖 실행)를 타는지 확인할 것')

        dirty, unpushed = working_tree_state()
        if dirty is not None:
            lines.append(f'워킹트리 미커밋: {dirty}건 (임계 {args.max_dirty_files}건)')
            if dirty > args.max_dirty_files:
                problems.append(
                    f'커밋 누락 의심: 워킹트리에 미커밋 변경 {dirty}건 — '
                    f'사이클이 작업 후 커밋 단계에서 중단됐을 수 있음 '
                    f'(전형 원인: .git/*.lock 잔존)')
        if unpushed is not None:
            lines.append(f'미push 커밋: {unpushed}건')
            if unpushed > 0:
                problems.append(
                    f'push 누락: 로컬 커밋 {unpushed}건이 origin에 미반영 — '
                    f'산출물이 GitHub에 도달하지 못하는 상태')

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
