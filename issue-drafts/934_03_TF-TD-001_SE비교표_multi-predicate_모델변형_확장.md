---
title: "[P0/설계] TF-TD-001 SE 비교표 multi-predicate / 모델변형 매트릭스 양식 확장 — 2026-Q3"
labels: "P0,설계,RA,510k,SE"
state: open
---

## 배경
- 분기 종합 감사 2026-Q2 벤치마크 3건 모두 **multi-predicate(2~4건) + 동일 510(k) 내 다중 모델 변형(4~8개)** 구조.
  - K243734: predicate 1건 + reference 3건, 모델 4개
  - K250211: predicate 4건 (multi), 모델 4개
  - K243171: predicate 3건 (multi), 모델 **8개** (CsI×GOS×Glass×Non-Glass×portable×wired)
- 자사 TF-TD-001 §SE 비교표는 1:1 (1 predicate × 1 model) 구조만 가정.

## 작업 범위 (Done 정의)
- [ ] TF-TD-001 §SE 비교표를 N:M (N predicate × M model variant) 매트릭스로 확장
- [ ] Predicate column: 최대 5건 동시 비교 셀
- [ ] Model row: scintillator (CsI/GOS) × substrate (Glass/Non-Glass PET) × portability (wireless/wired/non-portable) 차원 cross-product
- [ ] Reference device 항 신설 (Predicate와 구분)
- [ ] Substantial Equivalence rationale: "no new questions of safety and effectiveness" 표준 결론문 양식
- [ ] 적합성 표준 일괄 매핑 (AAMI/ANSI ES60601-1 / IEC 60601-1/-1-2/-1-6 / IEC 62304 / IEC 62366-1 / HE75) 양식

## 1차 출처
- BMK-2026Q2-K243171 §3 단일 510k 8개 모델
- BMK-2026Q2-K250211 §3 multi-predicate 4건
- BMK-2026Q2-K243734 §3 reference device 3건

## 우선순위 / 기한
- 우선순위: **P0**
- 기한: 2026-09-30
- Owner: RA Lead + 설계 Lead
