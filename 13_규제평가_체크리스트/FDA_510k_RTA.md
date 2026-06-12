---
doc-id: CHK-FDA-510K-RTA
title: FDA 510(k) RTA Checklist 평가표
type: Checklist
version: v0.1
status: draft
category: 13_규제평가_체크리스트
purpose: FDA 510(k) RTA Checklist 기반 자체 평가 항목 데이터
applicable: [FDA QMSR, FDA 510(k)]
owner: RA Lead (US)
last-review: 2026-05-28
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
  related_docs: []

- id: FDA-510K-A2
  source: FDA RTA Checklist Section A
  clause: A.2
  requirement: FDA Form 3514 — Cover Sheet
  severity: must
  evidence_type: form
  applicable_keywords: [FDA 510]
  related_docs: []

- id: FDA-510K-A3
  source: FDA RTA Checklist Section A
  clause: A.3
  requirement: FDA Form 3654 — Indications for Use Statement
  severity: must
  evidence_type: form
  applicable_keywords: [FDA 510]
  related_docs: []

- id: FDA-510K-A4
  source: FDA RTA Checklist Section A
  clause: A.4
  requirement: User Fee Cover Sheet (Form 3601) + payment receipt
  severity: must
  evidence_type: form
  applicable_keywords: [FDA 510]
  related_docs: []

- id: FDA-510K-A5
  source: FDA RTA Checklist Section A
  clause: A.5
  requirement: Standards Data Report (Form 3654 또는 별도 문서)
  severity: must
  evidence_type: form
  applicable_keywords: [FDA 510, IEC60601-1, IEC60601-2-54]
  related_docs: []
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
  related_docs: []

- id: FDA-510K-B2
  source: FDA RTA Checklist Section B
  clause: B.2
  requirement: Intended Use / Indications for Use — disease, population, environment
  severity: must
  evidence_type: technical_documentation
  applicable_keywords: [FDA 510]
  related_docs: []

- id: FDA-510K-B3
  source: FDA RTA Checklist Section B
  clause: B.3
  requirement: Substantial Equivalence — predicate device(s) identified with K-number, comparison table
  severity: must
  evidence_type: SE_comparison_table
  applicable_keywords: [FDA 510]
  related_docs: []
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
  related_docs: []

- id: FDA-510K-C2
  source: FDA RTA Checklist Section C
  clause: C.2
  requirement: Biocompatibility — ISO 10993 series testing (or rationale for omission)
  severity: must
  evidence_type: test_report
  applicable_keywords: [ISO10993]
  related_docs: []

- id: FDA-510K-C3
  source: FDA RTA Checklist Section C
  clause: C.3
  requirement: Electrical safety — IEC 60601-1, EMC IEC 60601-1-2
  severity: must
  evidence_type: test_report
  applicable_keywords: [IEC60601-1, IEC60601-2-54]
  related_docs: []

- id: FDA-510K-C4
  source: FDA RTA Checklist Section C
  clause: C.4
  requirement: Software (Major LoC) — IEC 62304 + FDA SW guidance + cybersecurity
  severity: must
  evidence_type: SW_documentation
  applicable_keywords: [IEC62304, FDA SBOM, IEC81001-5-1]
  related_docs: []
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
  related_docs: []

- id: FDA-510K-E2
  source: FDA RTA Checklist Section E
  clause: E.2
  requirement: UDI compliance — GS1/HIBCC issuing agency identified
  severity: must
  evidence_type: udi_plan
  applicable_keywords: [UDI]
  related_docs: []
```

---

> v0.1 — 16개 핵심 항목으로 시작. 다음 보강에서 ~64개 추가하여 RTA 전체 ~80건 완성 예정.
