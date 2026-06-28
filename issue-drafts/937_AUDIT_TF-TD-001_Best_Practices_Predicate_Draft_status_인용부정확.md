---
title: "[AUDIT P1] TF-TD-001 v0.4 §18.7 / §출처 — FDA 'Best Practices for Selecting a Predicate Device' Guidance (2023-09) Draft 상태 미표시 인용부정확"
labels: "audit:citation,prio:P1,risk:medium"
---

## 대상 문서
- `06_문서_기록관리/TF-TD-001_의료기기파일_기술문서_관리.md` v0.4 (2026-06-29)
- 위치 1: §18.7 §SE-5 매트릭스 작성·점검 절차 — 단계 2 "Best practice 적용" 행
- 위치 2: 문서 말미 "## 출처" — "FDA 'Best Practices for Selecting a Predicate Device to Support a Premarket Notification [510(k)] Submission' Guidance (2023-09)"

## 주장 (기재값)
> 2. Best practice 적용 | FDA **"Best Practices for Selecting a Predicate Device"** (2023-09) **기준 평가**: ① 동일 product code ② 최근 SE 결정 ③ 시판 중 ④ recall/safety issue 부재 | RA Lead | Predicate short-list 5건 이하

§출처에서는 "(2023-09)"만 기재, **Draft / Final 구분 없음**.

## Tier 1 정답
FDA Guidance 페이지 (Docket FDA-2023-D-3134):

> **Best Practices for Selecting a Predicate Device to Support a Premarket Notification [510(k)] Submission**
> **Draft Guidance for Industry and Food and Drug Administration Staff**
> **September 2023**
>
> **Draft**
> **Not for implementation. Contains non-binding recommendations.**

- Issued: September 2023
- 상태: **Draft** (2026-06 시점 미확정·미시행)
- Docket Number: FDA-2023-D-3134
- Content current as of: 09/07/2023

## 판정
**인용부정확 (P1, audit:citation)** — 가이던스 자체와 발행 시점(2023-09)은 일치(사실오류 아님). 그러나:

1. **Draft 상태 미표시**: 발행 후 2년 9개월 지난 시점(2026-06) 까지 Final 미공포 상태이며, "Not for implementation. Contains non-binding recommendations." 의 명문 표시가 있음. 사내 절차서 §18.7 단계 2 에서 본 가이던스를 normative("기준 평가") 로 사용하는 양식에 Draft 표시 누락은 RA 실무자가 final guidance 로 오인할 위험.
2. **Docket 번호 미표시**: audit #920 권고 후 다른 사내 가이던스 인용 (예: PCCP) 은 Docket 번호 (FDA-2022-D-2628) 가 보강된 사례 있음 — TF-TD-001 v0.4 §18 양식 신설 시 동일 표준이 적용되지 않음.

**같은 패턴 사내 재발**: audit #920 (EU_AI_Act_MDR §5/§9 "FDA PCCP Draft Guidance 2023" → 정답 "Final Guidance 2024-12-03") 는 Draft→Final 미반영이 사실오류였던 반면, 본 건은 가이던스가 **여전히 Draft** 이므로 사실오류 아님. 다만 동일 "Draft 상태 표시" 결함 카테고리.

## Tier 1 출처
- FDA Guidance 페이지: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/best-practices-selecting-predicate-device-support-premarket-notification-510k-submission
- Federal Register Notice: https://www.federalregister.gov/d/2023-19283
- Docket: https://www.regulations.gov/docket/FDA-2023-D-3134

## 권고
1. §출처 항목 "FDA 'Best Practices for Selecting a Predicate Device...' Guidance (2023-09)" → "**FDA Draft Guidance** 'Best Practices for Selecting a Predicate Device to Support a Premarket Notification [510(k)] Submission' (**September 2023, Docket FDA-2023-D-3134, Not for implementation**)" 로 정정.
2. §18.7 단계 2 행 — "기준 평가" 표현을 "**Draft Guidance 권고 사항 참고 평가**" 로 완화하거나, "(자사 RA 정책으로 Draft 권고 사항 채택, 적용 근거: 사내 정책 SOP-CC-001 §x.x)" 형태로 자사 정책 귀속 보강 (audit #910 CVSS 정량기한 패턴 — IEC 일반원칙 + 자사정책 귀속 정정과 동일 패턴).
3. 가이던스 finalization 모니터링 — Docket FDA-2023-D-3134 finalization 시 즉시 §18.7 / §출처 갱신 (cadence: 분기 종합 시 점검).

## PASS 별기록
- 발행 시점 "2023-09" 자체는 Tier 1 일치.
