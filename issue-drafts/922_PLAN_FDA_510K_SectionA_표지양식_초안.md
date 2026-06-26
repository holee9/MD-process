---
title: "[PLAN P0] FDA 510(k) Section A/B 제출 표지 양식 초안 작성 (A1~A4, B2, B3)"
labels: "planning,review,compliance,prio:P0"
---

## 배경

2026-06-26 주간 갭분석(WGAP-2026-06-26) 결과 FDA 510(k) RTA 표준 점수 0% — 15 must 항목 전부 "증빙 없음(related_docs:[])". 이 중 6건은 제출 표지/필수 양식으로 부재 시 RTA(Refuse to Accept) 즉시 사유. 양식 초안 1차본만으로도 점수 +40%p 회복 가능하며, 직전 2주 연속 Top 1로 유지 중이라 우선순위 상향.

## 대상 항목

| ID | 조항 | 결과물 | severity |
|---|---|---|---|
| FDA-510K-A1 | A.1 | Cover Letter draft (.docx) — applicant info, contact, submitter type | must |
| FDA-510K-A2 | A.2 | FDA Form 3514 (CDRH Premarket Review Submission Cover Sheet) 채워넣기 | must |
| FDA-510K-A3 | A.3 | FDA Form 3654 (Indications for Use Statement) | must |
| FDA-510K-A4 | A.4 | FDA Form 3601 (User Fee Cover Sheet) + Section A 영수증 첨부 자리 | must |
| FDA-510K-B2 | B.2 | Intended Use / Indications for Use 문서 (질환·인구·환경 기술) | must |
| FDA-510K-B3 | B.3 | Substantial Equivalence 비교표 — Predicate K-number 식별 + 비교 매트릭스 | must |

## 체크리스트

- [ ] `13_규제평가_체크리스트/FDA_510k_RTA.md` 의 A1~A4, B2, B3 항목 `related_docs:` 에 신규 doc-id 등록
- [ ] `01_법규_규제/FDA_510k/` 신규 폴더 + 6건 초안 생성 (doc-id: FDA-510K-COVER-001 ~ FDA-510K-SE-001)
- [ ] Predicate device 1~2건 K-number 식별 (Digital X-ray DR / Flat Panel Detector 카테고리)
- [ ] `build_readiness.py` 재실행 → FDA 점수 ≥40% 확인
- [ ] 교차검증 보고서(12_교차검증_보고서) 1차 항목 추가

## 참고 링크

- 갭분석: `13_규제평가_체크리스트/주간_갭분석_2026-06-26.md`
- 1차 출처: FDA "Refuse to Accept Policy for 510(k)s" Guidance (최신 개정)
- 관련 문서: `13_규제평가_체크리스트/FDA_510k_RTA.md`
