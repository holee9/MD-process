---
doc-id: CHK-FDA-510K-RTA
title: FDA 510(k) RTA Checklist 평가표
type: Checklist
version: v0.4
status: draft
category: 13_규제평가_체크리스트
purpose: FDA 510(k) RTA Checklist 기반 자체 평가 항목 데이터
applicable: [FDA QMSR, FDA 510(k)]
owner: RA Lead (US)
last-review: 2026-09-10
review-due: 2027-05-28
---

# FDA 510(k) Refuse to Accept (RTA) Checklist 평가표

> 출처: FDA "Refuse to Accept Policy for 510(k)s" Guidance (최신 개정 반영)
> 본 파일은 `scripts/build_readiness.py` 가 자동 스캔. YAML 항목 형식 준수.

## 1. Submission Coverage (제출 표지)

```yaml
- id: FDA-510K-A1
  source: FDA RTA Checklist Section A (2024)
  clause: A.1
  requirement: Cover Letter — applicant name, address, contact, submitter type
  severity: must
  evidence_type: cover_letter
  applicable_keywords: [FDA 510, FDA QMSR]
  related_docs: [T-FDA510K-A1_Cover_Letter_템플릿]

- id: FDA-510K-A2
  source: FDA RTA Checklist Section A
  clause: A.2
  requirement: FDA Form 3514 — Cover Sheet
  severity: must
  evidence_type: form
  applicable_keywords: [FDA 510]
  related_docs: [T-FDA510K-A2_Form3514_템플릿]

- id: FDA-510K-A3
  source: FDA RTA Checklist Section A
  clause: A.3
  requirement: FDA Form 3881 — Indications for Use Statement
  severity: must
  evidence_type: form
  applicable_keywords: [FDA 510]
  related_docs: [T-FDA510K-A3_Form3881_IFU_템플릿]

- id: FDA-510K-A4
  source: FDA RTA Checklist Section A
  clause: A.4
  requirement: User Fee Cover Sheet (Form 3601) + payment receipt
  severity: must
  evidence_type: form
  applicable_keywords: [FDA 510]
  related_docs: [T-FDA510K-A4_Form3601_UserFee_템플릿]

- id: FDA-510K-A5
  source: FDA RTA Checklist Section A
  clause: A.5
  requirement: Standards Data Report (Form 3654 또는 별도 문서)
  severity: must
  evidence_type: form
  applicable_keywords: [FDA 510, IEC60601-1, IEC60601-2-54]
  related_docs: [T-FDA510K-A5_Form3654_Standards_템플릿, X-ray_장비_안전성능_표준_매핑]
```

## 2. Device Description & Indications

```yaml
- id: FDA-510K-B1
  source: FDA RTA Checklist Section B
  clause: B.1
  requirement: Device Description — physical, technological characteristics, components, accessories
  severity: must
  evidence_type: technical_documentation
  applicable_keywords: [FDA 510, FDA QMSR]
  related_docs: [T-FDA510K-B1_Device_Description_템플릿]

- id: FDA-510K-B2
  source: FDA RTA Checklist Section B
  clause: B.2
  requirement: Intended Use / Indications for Use — disease, population, environment
  severity: must
  evidence_type: technical_documentation
  applicable_keywords: [FDA 510]
  related_docs: [T-FDA510K-B2_Intended_Use_템플릿]

- id: FDA-510K-B3
  source: FDA RTA Checklist Section B
  clause: B.3
  requirement: Substantial Equivalence — predicate device(s) identified with K-number, comparison table
  severity: must
  evidence_type: SE_comparison_table
  applicable_keywords: [FDA 510]
  related_docs: [T-FDA510K-B3_SE_비교표_템플릿]
```

## 3. Performance Data

```yaml
- id: FDA-510K-C1
  source: FDA RTA Checklist Section C
  clause: C.1
  requirement: Non-clinical Bench Performance Testing — protocol, results, acceptance criteria
  severity: must
  evidence_type: test_report
  applicable_keywords: [FDA 510, IEC60601-1, IEC60601-2-54]
  related_docs: [IEC60601-2-54_형식시험_체크리스트, QC-IQ-001, F-DVV-001]

- id: FDA-510K-C2
  source: FDA RTA Checklist Section C
  clause: C.2
  requirement: Biocompatibility — ISO 10993 series testing (or rationale for omission)
  severity: must
  evidence_type: test_report
  applicable_keywords: [ISO10993]
  related_docs: [T-FDA510K-C2_Biocompatibility_템플릿]

- id: FDA-510K-C3
  source: FDA RTA Checklist Section C
  clause: C.3
  requirement: Electrical safety — IEC 60601-1, EMC IEC 60601-1-2
  severity: must
  evidence_type: test_report
  applicable_keywords: [IEC60601-1, IEC60601-2-54]
  related_docs: [X-ray_장비_안전성능_표준_매핑, IEC60601-2-54_형식시험_체크리스트]

- id: FDA-510K-C4
  source: FDA RTA Checklist Section C
  clause: C.4
  requirement: Software (Major LoC) — IEC 62304 + FDA SW guidance + cybersecurity
  severity: must
  evidence_type: SW_documentation
  applicable_keywords: [IEC62304, FDA SBOM, IEC81001-5-1]
  related_docs: [IEC_62304_SW_수명주기, SOP-VAL-001, IEC_81001-5-1_FDA_Cybersecurity_SW보안, SOP-SBOM-001]
```

## 4. Sterility / Shelf Life (해당 시)

```yaml
- id: FDA-510K-D1
  source: FDA RTA Checklist Section D
  clause: D.1
  requirement: Sterilization validation (해당 시)
  severity: should
  evidence_type: validation_report
  applicable_keywords: [ISO11135, ISO11137]
  related_docs: []
```

## 5. Labeling

```yaml
- id: FDA-510K-E1
  source: FDA RTA Checklist Section E
  clause: E.1
  requirement: Labeling — proposed labels, IFU draft, contraindications
  severity: must
  evidence_type: labeling_draft
  applicable_keywords: [FDA 510, UDI]
  related_docs: [T-FDA510K-E1_Labeling_템플릿]

- id: FDA-510K-E2
  source: FDA RTA Checklist Section E
  clause: E.2
  requirement: UDI compliance — GS1/HIBCC issuing agency identified
  severity: must
  evidence_type: udi_plan
  applicable_keywords: [UDI]
  related_docs: [T-FDA510K-E2_UDI_템플릿]
```

---

> v0.1 — 16개 핵심 항목으로 시작. 다음 보강에서 ~64개 추가하여 RTA 전체 ~80건 완성 예정.
>
> v0.2 (2026-09-09) — must 항목 중 3건(A1 Cover Letter, B1 Device Description, B3 SE 비교표) 골격 템플릿 신규 생성 및 related_docs 연결. 제품별 실 데이터는 미기재(작성 예정).
>
> v0.3 (2026-09-10) — must 항목 3건 추가(B2 Intended Use/IFU, E1 Labeling, E2 UDI) 골격 템플릿 신규 생성 및 related_docs 연결. 누적 6/14 must 항목 골격 확보.
>
> v0.4 (2026-09-10) — **audit #1028 정정**: A.3 양식번호 오귀속(Form 3654 → **Form 3881**, Tier1 FDA 원문 확인). Section A 표지 양식 4건(3514/3881/3601/3654) 및 C.2 생체적합성 템플릿 신규 생성(이슈 #931 P0 대응). C.1/C.3/C.4는 신규 생성 없이 기존 실문서(형식시험 체크리스트·표준매핑·62304/81001-5-1/SBOM/SOP-VAL-001)에 연결. must 14/14 증빙 경로 확보.
