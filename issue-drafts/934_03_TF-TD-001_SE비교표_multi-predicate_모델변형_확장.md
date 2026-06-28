---
title: "[P0/설계] TF-TD-001 SE 비교표 multi-predicate / 모델변형 매트릭스 양식 확장 — 2026-Q3"
labels: "P0,설계,RA,510k,SE"
state: closed
closed-at: 2026-06-29
closed-by: holee9-builder
related-commits: [TF-TD-001 v0.4]
---

## 배경
- 분기 종합 감사 2026-Q2 벤치마크 3건 모두 **multi-predicate(2~4건) + 동일 510(k) 내 다중 모델 변형(4~8개)** 구조.
  - K243734: predicate 1건 + reference 3건, 모델 4개
  - K250211: predicate 4건 (multi), 모델 4개
  - K243171: predicate 3건 (multi), 모델 **8개** (CsI×GOS×Glass×Non-Glass×portable×wired)
- 자사 TF-TD-001 §SE 비교표는 1:1 (1 predicate × 1 model) 구조만 가정.

## 작업 범위 (Done 정의)
- [x] TF-TD-001 §18 SE 비교 매트릭스 신설 — N:M (최대 5 predicate × 12 model variant) 양식 도입 (TF-TD-001 v0.4 §18.3)
- [x] Predicate column: 5건 동시 비교 셀 양식 (§18.3 표 Predicate-1~Predicate-5)
- [x] Model row: 3차원 cross-product 12 row 양식 (MV-01~MV-12, §18.3)
- [x] Reference device 별도 표 §18.4 — Predicate와 물리적 분리, SE 단독 근거 사용 금지 명시 (FDA 510(k) Program Guidance 2014 §7 직접 인용)
- [x] §18.6 SE 결론문 양식 — 21 CFR 807.100(b) + 2014 Guidance §6 직접 인용 ("raise no new/different questions of safety and effectiveness")
- [x] §18.5 적합성 표준 매핑 양식 — AAMI/ANSI ES60601-1·IEC 60601-1/-1-2/-1-6/-2-54·IEC 62304·IEC 62366-1·HE75·IEC 62220-1-1/-1-3·ISO 14971·ISO 10993·FDA SSXI/SW/Cyber Guidance·ISO 15223-1/20417 망라

## 1차 출처
- BMK-2026Q2-K243171 §3 단일 510k 8개 모델
- BMK-2026Q2-K250211 §3 multi-predicate 4건
- BMK-2026Q2-K243734 §3 reference device 3건

## 우선순위 / 기한
- 우선순위: **P0**
- 기한: 2026-09-30
- Owner: RA Lead + 설계 Lead


## 종결 요약 (2026-06-29)
- 처리: TF-TD-001 v0.3 → **v0.4** (§18 SE 비교 매트릭스 신설 — 9 subsection: 18.1 목적/18.2 Predicate vs Reference/18.3 N:M 매트릭스/18.4 Reference 별도표/18.5 표준 매핑/18.6 SE 결론문/18.7 작성절차/18.8 비적용/18.9 부적합조치).
- 양식 등록: F-TD-005 (SE 비교 매트릭스) §17에 추가.
- 교차참조 추가: §16에 BMK-2026Q2-K243734/K250211/K243171, 13_규제평가/FDA_510k_RTA 4건.
- Tier 1: FDA 510(k) Program Guidance 2014-07-28, Best Practices for Predicate 2023-09, SSXI 2016-09-01, 21 CFR 807.100(b), 21 CFR 892.1680, 자사 분기 종합 벤치마크 3건.
- 적대적 자기검토: 표준 판본 미확정 항목은 'X-ray 표준매핑 v0.4 참조'로 회피하여 Tier 1 미확보 추정 기재 회피. IEC 62304는 'A2:2020 미존재' audit #908/#925 패턴 명시 인용.
