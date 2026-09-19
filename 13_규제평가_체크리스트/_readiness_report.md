# 규제 준비도 자동 갭 분석

> **생성일:** 2026-09-20 · **출처:** `13_규제평가_체크리스트/*.md` × 전체 문서 frontmatter
> 본 파일은 자동 생성. 수동 편집 금지.

## 종합 점수

| 표준 | 점수 | 항목 | must 미충족 |
|---|---:|---:|---:|
| FDA 510(k) RTA Checklist 평가표 | 83% `████████░░` | 15 | 10 |
| ISO 13485:2016 자체평가 체크리스트 | 81% `████████░░` | 94 | 38 |

## 표준별 항목 상세

### FDA 510(k) RTA Checklist 평가표 — 83%

| ID | 조항 | 요구사항 | severity | 상태 | 매칭 문서 |
|---|---|---|---|---|---|
| FDA-510K-A1 | A.1 | Cover Letter — applicant name, address, contact, submitter type | must | 충족 | T-FDA510K-A1_Cover_L |
| FDA-510K-A2 | A.2 | FDA Form 3514 — Cover Sheet | must | 충족 | T-FDA510K-A2_Form351 |
| FDA-510K-A3 | A.3 | FDA Form 3881 — Indications for Use Statement | must | 충족 | T-FDA510K-A3_Form388 |
| FDA-510K-A4 | A.4 | User Fee Cover Sheet (Form 3601) + payment receipt | must | 충족 | T-FDA510K-A4_Form360 |
| FDA-510K-A5 | A.5 | Standards Data Report (Form 3654 또는 별도 문서) | must | 충족 | T-FDA510K-A5_Form365, X-ray_장비_안전성능_표준_매핑 |
| FDA-510K-B1 | B.1 | Device Description — physical, technological characteristics, components, access | must | 충족 | T-FDA510K-B1_Device_ |
| FDA-510K-B2 | B.2 | Intended Use / Indications for Use — disease, population, environment | must | 충족 | T-FDA510K-B2_Intende |
| FDA-510K-B3 | B.3 | Substantial Equivalence — predicate device(s) identified with K-number, comparis | must | 충족 | T-FDA510K-B3_SE_비교표_ |
| FDA-510K-C1 | C.1 | Non-clinical Bench Performance Testing — protocol, results, acceptance criteria | must | 충족 | F-DVV-001, IEC60601-2-54_형식시험_체, QC-IQ-001 |
| FDA-510K-C2 | C.2 | Biocompatibility — ISO 10993 series testing (or rationale for omission) | must | 충족 | T-FDA510K-C2_Biocomp |
| FDA-510K-C3 | C.3 | Electrical safety — IEC 60601-1, EMC IEC 60601-1-2 | must | 충족 | IEC60601-2-54_형식시험_체, X-ray_장비_안전성능_표준_매핑 |
| FDA-510K-C4 | C.4 | Software (Major LoC) — IEC 62304 + FDA SW guidance + cybersecurity | must | 충족 | IEC_62304_SW_수명주기, IEC_81001-5-1_FDA_Cy, SOP-SBOM-001 …외 1건 |
| FDA-510K-D1 | D.1 | Sterilization validation (해당 시) | should | 미충족(증빙 없음) | 없음 |
| FDA-510K-E1 | E.1 | Labeling — proposed labels, IFU draft, contraindications | must | 충족 | T-FDA510K-E1_Labelin |
| FDA-510K-E2 | E.2 | UDI compliance — GS1/HIBCC issuing agency identified | must | 충족 | T-FDA510K-E2_UDI_템플릿 |

### ISO 13485:2016 자체평가 체크리스트 — 81%

| ID | 조항 | 요구사항 | severity | 상태 | 매칭 문서 |
|---|---|---|---|---|---|
| ISO-4.1.1 | 4.1 | - | must | 부분충족(선언) | JD-RA-001, GUIDE-PHASE2-FRAMEWO, 문서_메타데이터_규칙 …외 86건 |
| ISO-4.1.2 | 4.1 | - | must | 부분충족(선언) | F-ENV-001, F-QP-001, F-RA-001 …외 46건 |
| ISO-4.1.3 | 4.1 | - | must | 부분충족(선언) | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-4.2.1 | 4.2.1 | - | must | 부분충족(선언) | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-4.2.2 | 4.2.2 | - | must | 부분충족(선언) | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-4.2.3 | 4.2.3 | - | must | 부분충족(선언) | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-4.2.4 | 4.2.4 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-4.2.5 | 4.2.5 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-5.1 | 5.1 | - | must | 부분충족(선언) | F-QP-001, QM-001, SOP-QP-001 |
| ISO-5.2 | 5.2 | - | must | 부분충족(선언) | PRO-CRP-001, QM-001 |
| ISO-5.3 | 5.3 | - | must | 부분충족(선언) | QM-001, SOP-QP-001 |
| ISO-5.4.1 | 5.4.1 | - | must | 부분충족(선언) | F-QP-001, QM-001, SOP-QP-001 |
| ISO-5.4.2 | 5.4.2 | - | should | 부분충족(선언) | QM-001, SOP-CC-001 |
| ISO-5.5.1 | 5.5.1 | - | must | 충족 | F-RA-001, QM-001, SOP-RA-002 |
| ISO-5.5.2 | 5.5.2 | - | must | 충족 | F-RA-002 |
| ISO-5.5.3 | 5.5.3 | - | should | 충족 | F-RA-003, QM-001, SOP-RA-002 |
| ISO-5.6.1 | 5.6.1 | - | must | 충족 | QM-001, SOP-MR-001 |
| ISO-5.6.2 | 5.6.2 | - | must | 부분충족(선언) | SOP-MR-001 |
| ISO-5.6.3 | 5.6.3 | - | must | 부분충족(선언) | SOP-MR-001 |
| ISO-6.1 | 6.1 | - | must | 부분충족(선언) | QM-001, SOP-ENV-001 |
| ISO-6.2 | 6.2 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-6.3 | 6.3 | - | must | 부분충족(선언) | SOP-ENV-001, SOP-MFG-002 |
| ISO-6.4.1 | 6.4.1 | - | must | 부분충족(선언) | F-ENV-001, SOP-ENV-001, SOP-MFG-002 |
| ISO-6.4.2 | 6.4.2 | - | should | 미충족(증빙 없음) | 없음 |
| ISO-7.1 | 7.1 | - | must | 부분충족(선언) | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.2.1 | 7.2.1 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.2.2 | 7.2.2 | - | must | 부분충족(선언) | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.2.3 | 7.2.3 | - | must | 부분충족(선언) | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.3.1 | 7.3.1 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.3.2 | 7.3.2 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.3.3 | 7.3.3 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.3.4 | 7.3.4 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.3.5 | 7.3.5 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.3.6 | 7.3.6 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.3.7 | 7.3.7 | - | must | 충족 | 프로젝트_개요, 디지털의료제품법_SaMD_AI_요구, EU_AI_Act_MDR_중첩적용_매 …외 56건 |
| ISO-7.3.8 | 7.3.8 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.3.9 | 7.3.9 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.3.10 | 7.3.10 | - | must | 부분충족(선언) | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.4.1 | 7.4.1 | - | must | 부분충족(선언) | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.4.2 | 7.4.2 | - | must | 부분충족(선언) | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.4.3 | 7.4.3 | - | must | 부분충족(선언) | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.5.1.1 | 7.5.1 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 43건 |
| ISO-7.5.1.2 | 7.5.1 | - | must | 충족 | GUIDE-PHASE2-FRAMEWO, 색인_INDEX, 프로젝트_개요 …외 68건 |
| ISO-7.5.2 | 7.5.2 | - | should | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.5.3.1 | 7.5.3 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.5.3.2 | 7.5.4 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.5.4 | 7.5.6 | - | must | 부분충족(선언) | SOP-MFG-001, 공정_밸리데이션 |
| ISO-7.5.6 | 7.5.6 | - | may | N/A | 없음 |
| ISO-7.5.7 | 7.5.7 | - | may | N/A | 없음 |
| ISO-7.5.8 | 7.5.8 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.5.9 | 7.5.9 | - | must | 충족 | JD-RA-001, 색인_INDEX, 프로젝트_개요 …외 62건 |
| ISO-7.5.10 | 7.5.10 | - | should | 미충족(증빙 없음) | 없음 |
| ISO-7.5.11 | 7.5.11 | - | must | 충족 | SOP-PKG-001, SOP-PRES-001, SOP-TRC-001 |
| ISO-7.6 | 7.6 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-8.1 | 8.1 | - | must | 부분충족(선언) | F-ENV-001, F-QP-001, F-RA-001 …외 43건 |
| ISO-8.2.1 | 8.2.1 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-8.2.2 | 8.2.2 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-8.2.3 | 8.2.3 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-8.2.4 | 8.2.4 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-8.2.5 | 8.2.5 | - | must | 부분충족(선언) | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-8.2.6 | 8.2.6 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-8.3.1 | 8.3.1 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-8.3.2 | 8.3.2 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-8.3.3 | 8.3.3 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-8.3.4 | 8.3.4 | - | must | 부분충족(선언) | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-8.4 | 8.4 | - | must | 충족 | PRO-DA-001 |
| ISO-8.5.1 | 8.5.1 | - | must | 부분충족(선언) | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-8.5.2 | 8.5.2 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-8.5.3 | 8.5.3 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-4.1.4 | 4.1 | - | must | 충족 | GUIDE-PHASE2-FRAMEWO, 색인_INDEX, 프로젝트_개요 …외 68건 |
| ISO-4.2.3a | 4.2.3 | - | must | 부분충족(선언) | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-5.4.2a | 5.4.2 | - | should | 부분충족(선언) | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.1a | 7.1 | - | must | 부분충족(선언) | JD-RA-001, GUIDE-PHASE2-FRAMEWO, 문서_메타데이터_규칙 …외 80건 |
| ISO-7.3.2a | 7.3.2 | - | must | 부분충족(선언) | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.3.6a | 7.3.6 | - | must | 충족 | JD-RA-001, GUIDE-PHASE2-FRAMEWO, 문서_메타데이터_규칙 …외 70건 |
| ISO-7.3.7a | 7.3.7 | - | must | 충족 | 프로젝트_개요, 디지털의료제품법_SaMD_AI_요구, EU_AI_Act_MDR_중첩적용_매 …외 56건 |
| ISO-7.3.7b | 7.3.7 | - | must | 충족 | GUIDE-PHASE2-FRAMEWO, 색인_INDEX, 프로젝트_개요 …외 68건 |
| ISO-7.4.1a | 7.4.1 | - | must | 부분충족(선언) | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.4.1b | 7.4.1 | - | should | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.5.1a | 7.5.1 | - | must | 충족 | JD-RA-001, 색인_INDEX, 프로젝트_개요 …외 62건 |
| ISO-7.5.1b | 7.5.1 | - | must | 부분충족(선언) | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.5.4a | 7.5.6 | - | should | 부분충족(선언) | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-7.5.9a | 7.5.9 | - | must | 충족 | JD-RA-001, 색인_INDEX, 프로젝트_개요 …외 62건 |
| ISO-8.2.1a | 8.2.1 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-8.2.4a | 8.2.4 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-8.3.1a | 8.3.1 | - | should | 부분충족(선언) | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-RM-01 | 7.1 + ISO14971 | - | must | 부분충족(선언) | GUIDE-PHASE2-FRAMEWO, 색인_INDEX, 이슈관리_규칙 …외 63건 |
| ISO-RM-02 | 7.1 + ISO14971 §4 | - | must | 부분충족(선언) | GUIDE-PHASE2-FRAMEWO, 색인_INDEX, 이슈관리_규칙 …외 63건 |
| ISO-RM-03 | 7.1 + ISO14971 §6 | - | must | 부분충족(선언) | GUIDE-PHASE2-FRAMEWO, 색인_INDEX, 이슈관리_규칙 …외 63건 |
| ISO-FSCA-01 | 8.2.3 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-CAPA-01 | 8.5.2 | - | must | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-DOC-01 | 4.2.4 | - | should | 충족 | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
| ISO-INFRA-01 | 6.3 | - | should | 부분충족(선언) | JD-RA-001, GUIDE-PHASE2-FRAMEWO, 색인_INDEX …외 67건 |
| ISO-ENV-01 | 6.4.1 | - | must | 부분충족(선언) | F-ENV-001, F-QP-001, F-RA-001 …외 42건 |
