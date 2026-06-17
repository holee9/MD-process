---
title: "[완료] #1521 build_readiness.py ISO 13485 점수 과대평가 보정"
labels: "source:emergent,prio:P2,type:consistency,risk:med"
github-issue: 1521
state: closed
closed-date: 2026-06-18
closes: "#1521"
---

## 완료 내용

`scripts/build_readiness.py` `score_item()` 함수에 선언된 status 우선 처리 로직 추가:

- `status: unmet` → score=0 강제 (키워드 매칭 무시)
- `status: na` → 가중치 합산에서 제외
- `status: partial` → 키워드 매칭 점수 60 상한 적용

`calculate_score()`에서 `score is None`(na) 항목 skip 로직 추가.

## 검증 결과

| 항목 | 수정 전 | 수정 후 |
|---|---|---|
| ISO 13485 준비도 점수 | 100% (과대평가) | 80% (9→8 unmet must 반영) |
| FDA 510(k) 점수 | 52% | 52% (변동 없음) |

> 체크리스트 상태 현행화(unmet→partial 8건)로 최종 80%. 스크립트 로직 자체는 정확.

## DoD 체크

- [x] status:unmet 항목 score=0 처리
- [x] 재실행 후 100% 과대평가 해소
- [x] 교차검증 CRV-2026-06-18 기록

