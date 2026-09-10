---
title: "audit #1030 (근본원인/거버넌스): owner 'TBD' 무한 재발 — 자동 주입 기본값이 원인, 스크립트 수정 + CI 게이트 신설"
labels: "audit:governance,prio:P1,risk:medium,maintenance,qms"
---

## 증상 (반복 재발)

`owner: TBD` 문서가 정정 후에도 계속 재출현. 2026-07-08 스프린트에서 24건을 직책으로 정정했으나, 2026-09-10 재점검 시 **34건**으로 오히려 증가.

## 근본원인 (2026-09-10 확정)

`scripts/inject_frontmatter.py` L200:

```python
owner = existing.get('owner') or 'TBD'
```

frontmatter 자동 주입 시 owner가 없으면 **무조건 'TBD'를 기록**. 신규·편집 문서가 자동화 사이클을 거칠 때마다 미배정 문서가 새로 생성되는 구조 — 수동 정정은 원인이 아닌 증상만 제거하므로 영구 재발한다.

부차 원인: `scripts/validate_frontmatter.py`가 owner 값을 **전혀 검증하지 않아** CI가 재발을 잡지 못했다(필수 필드 목록에 owner 미포함).

## 조치 (2026-09-10)

1. **기본값 제거 → 카테고리별 직책 자동 배정**: `DEFAULT_OWNER_BY_CATEGORY` + `default_owner_for()` 신설. 직책 정의 SSOT는 `00_프로젝트관리/프로젝트_개요.md §3.1`. 실명 미사용 원칙 주석으로 명문화(인사이동 시 문서 무효화 방지).
2. **CI 게이트 신설**: `validate_frontmatter.py`에 `FORBIDDEN_OWNERS = {'TBD','tbd','미정','-',''}` 검증 추가 → 미배정 시 exit 1. `.github/workflows/validate-frontmatter.yml`이 push마다 차단한다.
3. **존량 정리**: `owner: TBD` 34건 직책 배정 + 신규 게이트가 추가 검출한 **owner 필드 자체 누락 6건**(F-RM-001/002/003, F-SUP-001, GUIDE-SQA-001, F-TRN-001) 배정. 최종 `validate_frontmatter` 전체 통과.

## 예외 (의도적 미변경)

`11_일일_리서치로그`·`12_교차검증_보고서`의 `owner: holee9-automation|holee9-builder|QMS-Bot` 약 19건은 **시점 기록의 산출 주체 표기**이므로 변경하지 않는다(사람 직책이 아니라 생성 프로세스 식별자이며, 해당 카테고리는 경량 frontmatter 규칙 적용 대상이라 본 게이트 범위 밖).

## 체크리스트

- [x] 근본원인 코드 위치 특정
- [x] inject_frontmatter.py 기본값 수정
- [x] validate_frontmatter.py CI 게이트 추가
- [x] 존량 40건(TBD 34 + 누락 6) 배정
- [x] 전체 검증 통과 확인
- [ ] 다음 자동화 사이클에서 재발 0건 확인 (사후 검증)

## 참고 링크

- 관련 문서: `scripts/inject_frontmatter.py`, `scripts/validate_frontmatter.py`, `00_프로젝트관리/프로젝트_개요.md` §3.1
- 선행 이슈: #999 (반복오류클래스 근본원인 대응)

실운영 문서 미참고. 본 건은 저장소 내부 코드·거버넌스 결함으로 외부 규제 출처 검증 불요.
