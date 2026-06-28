---
title: "[P0/RA] FDA 510(k) dossier Form 표지 양식 4건 작성 (Form 3514 / 3601 / 3654 / Cover Letter) — 2026-Q3 우선"
labels: "P0,RA,510k,dossier"
state: open
---

## 배경
- 분기 종합 감사 2026-Q2 결과 FDA 510(k) RTA 점수 **0% (15항목 중 must 14건 미충족)**.
- 0%의 직접 원인: dossier-단계 Form 표지 일체 미작성 (RTA Checklist Section A 전부 미충족).
- 510(k) 벤치마크 K243734 / K250211 / K243171 3건 모두 해당 Form 첨부.

## 작업 범위 (Done 정의)
- [ ] FDA Form 3514 — 510(k) Cover Sheet 양식 (회사명/주소/연락처 자리표시자 포함)
- [ ] FDA Form 3601 — User Fee Cover Sheet 양식 + 수수료 결제 영수증 자리표시자
- [ ] FDA Form 3654 — Standards Data Report 양식 또는 자사 별도 문서 양식
- [ ] FDA Form 3881 — Indications for Use Statement 양식 (현행 OMB 만료일 2026-07-31 주의)
- [ ] 510(k) Cover Letter 영문 표준 양식 (applicant name/address/contact/submitter type)
- [ ] `13_규제평가_체크리스트/FDA_510k_RTA.md` 항목 A1~A5의 `related_docs:` 필드에 신규 doc-id 등록

## 목표 영향
- 다음 분기(2026-Q3) `build_readiness.py` 재실행 시 FDA RTA Section A 5건 모두 충족 → **점수 0% → 33%** 예상.

## 1차 출처
- FDA "Refuse to Accept Policy for 510(k)s" Guidance
- BMK-2026Q2-K243734 §2 Submission 표지 항
- Form 3881 OMB No. 0910-0120 (2026-07-31 expiration)

## 우선순위 / 기한
- 우선순위: **P0**
- 기한: 2026-09-30 (Q3 종료)
- Owner: RA Lead (US)
