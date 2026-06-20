---
doc-id: EU_AI_Act_MDR_중첩적용_매핑
title: "EU AI Act ↔ EU MDR 중첩 적용 매핑 (AI/ML SaMD 대비)"
type: Matrix
version: v0.5
status: draft
category: 01_법규_규제
purpose: "EU AI Act(2024/1689)와 EU MDR(2017/745) 간 중첩 요건 식별, 단일 QMS/기술문서 통합 충족 전략 및 X-ray AI 영상 분석 시스템 적용 지침"
applicable: [EU AI Act(Regulation 2024/1689), EU MDR 2017/745, ISO13485:2016, ISO14971:2019, IEC62304:2006/A1:2015, IEC62366-1:2015/A1:2020, IEC81001-5-1:2021, FDA QMSR 21 CFR 820, 디지털의료제품법]
forms: [F-AIAMD-GAP-001]
related-docs: [EU_MDR_2017_745, GSPR_정합표준_매핑표, GSPR_체크리스트_v0.2_템플릿, SOP-AIGOV-001, SOP-AIDATA-001, SOP-CC-001, SOP-RM-001, SOP-PSUR-001, 디지털의료제품법_SaMD_AI_요구]
related-issues: [4, 7, 20, 21, 48, 58, 1527]
owner: RA/QA Lead
last-review: 2026-06-20
review-due: 2027-06-11
---

# EU AI Act ↔ EU MDR 중첩 적용 매핑 (AI/ML SaMD 대비)

## 1. 목적

본 문서는 AI/ML 기반 의료 SW(SaMD), 특히 X-ray 영상 판독 보조 기능을 염두에 두고 EU AI Act (Regulation (EU) 2024/1689)와 EU MDR (Regulation (EU) 2017/745) 간 중첩 요건을 식별하고, 단일 QMS/기술문서에서 동시에 충족하기 위한 매핑을 정리한다.

## 2. 위험 분류 — 중첩 조건

### 2.1 High-risk AI 분류 판단 절차

```
1. 제품이 EU 조화법령(Annex II) 대상인가?
   ├─ Yes: MDR/IVDR 등재 확인
   │   └─ 제3자 적합성평가(NB) 필요한 Class?
   │       ├─ Class IIa/IIb/III → High-risk AI system (Art. 6(1))
   │       └─ Class I (self-cert) → 원칙상 비해당 (단, Annex III 확인)
   └─ No: Annex III 별도 해당 여부 확인

2. High-risk 확정 시
   ├─ AI Act Chapter III 전체 요건 적용
   ├─ 적합성평가 경로: MDR 경로에 AI Act 요건 통합
   └─ EU DB 등록 의무 (Art. 49)
```

**판정 기준**: 대부분의 Class IIa 이상 AI SaMD는 NB 관여가 필요하므로 High-risk 분류 가능성이 높다.

### 2.2 X-ray AI 시스템 분류 예시

| 구성요소 | MDR Class | NB 필요 | AI Act 분류 | 근거 |
|----------|-----------|---------|-------------|------|
| AI 영상 판독 보조 SW (CADe/CADx) | IIa~IIb | Yes | **High-risk** | Art. 6(1) + Annex II §11 |
| X-ray 콘솔 SW (비AI) | IIa | Yes | **비해당** | AI 기능 없음 |
| AI 자동 노출 제어 | IIa | Yes | **High-risk** | 안전 구성요소 |
| AI 데이터 분석 (통계 리포트) | IIa | Yes | 판단 필요 | Rule-based vs. ML 여부 |

## 3. 적용 일정 (단계별)

| 시점 | AI Act 적용 내용 | MDR 상태 | 비고 |
|------|-----------------|----------|------|
| 2024-08-01 | AI Act 발효 | MDR 전면 적용 중 | |
| 2025-02-02 | 금지 AI 관행 적용 | — | 의료기기 해당 거의 없음 |
| 2025-08-02 | 범용 AI 모델(GPAI) 규칙 적용 | — | 의료기기 탑재 GPAI 해당 시 |
| **2026-08-02** | **High-risk 조항 본격 적용** | MDR 전면 적용 | **핵심 마일스톤** |
| 2027-08-02 | Art. 6(1) 경로 과도기 종료 | MDR 유지 | Class IIb/III + IVD C/D |

**주의**: 2026-08-02부터 High-risk 의무가 본격 적용되나, MDR Annex I(GSPR) 제품의 경우 Art. 6(1) 경로는 2027-08-02까지 과도기가 인정될 수 있다. NB 선정 시 AI Act 지정 범위(designated scope) 포함 여부를 반드시 확인한다.

> **⚠️ 2026 Omnibus 개정 동향 (2026-06-11 갱신):** 2026-03-13 EU 이사회는 고위험 AI 적용 시점을 연기하는 데 합의하였다 — 독립형 고위험(Annex III)은 **2027-12-02**, MDR/IVDR 등 규제 제품에 탑재된 고위험(Annex I, 의료기기 포함)은 **2028-08-02**로 이동(기존 2027-08-02 대비). 유럽의회 소관 위원회는 2026-03-18 이를 지지 의결하였고, **2026-05-07 3자(이사회·의회·집행위) 협의에서 잠정 합의(provisional agreement)에 도달**하였다. 정식 채택은 2026년 6월, 관보 게재는 7월로 예상된다(2026-06-13 확인: 정식 채택 6월 예상, 관보 7월 게재 예상 — 미완료 확인). 단, **정식 채택 전까지 기존 일정(2026-08-02 / 2027-08-02)을 구속력 있는 기준선(baseline)으로 간주**하고 대비할 것. **AI 리터러시 의무(Art. 4)의 2026-08-02 시한은 Omnibus 결과와 무관하게 유지**된다.
>
> **고위험 분류 가이드라인 초안(2026-05-19):** 집행위는 Art. 6 고위험 AI 분류에 관한 *Draft Commission Guidelines*를 이해관계자 의견수렴용으로 공개하였다(의견수렴 **2026-06-23**까지, 정식 채택 일정 미정). 본 매핑의 분류 판단 절차(§2.1)는 가이드라인 확정 시 재검토 대상이다.

## 4. 요건 매핑 상세

### 4.1 위험관리

| AI Act 요건 | 조항 | MDR / ISO 대응 | 통합 접근 | X-ray 적용 |
|-------------|------|----------------|-----------|-----------|
| Risk Management System | Art. 9 | MDR Annex I §3, ISO 14971:2019/A11 | 단일 Risk File에 AI 특유 위험 항목 추가 | 편향(특정 체형·인종별 판독 정확도 차이), 데이터 드리프트(장비 교체·프로토콜 변경 시 영상 특성 변화), 적대적 입력(조작된 영상) |
| 위험 허용 기준 | Art. 9(2) | ISO 14971 §7 | ALARP + AI 특유 임계값 추가 | 위음성(missed finding) 위험 → Sensitivity 하한선 설정 |

### 4.2 데이터 거버넌스

| AI Act 요건 | 조항 | MDR / ISO 대응 | 통합 접근 | X-ray 적용 |
|-------------|------|----------------|-----------|-----------|
| Data & Data Governance | Art. 10 | MDR Annex II §6.1, IEC 62304, GMLP | 학습/검증/테스트 데이터셋 관리 SOP | X-ray 영상 데이터: 다기관(≥3), 다장비 브랜드, 체형·연령·성별 대표성 확보 |
| 데이터 품질 | Art. 10(2-5) | — | 라벨링 품질 관리, 편향 점검 | 판독 전문의 ≥2인 합의 라벨링, Cohen's κ ≥ 0.80 |

### 4.3 기술문서 & 투명성

| AI Act 요건 | 조항 | MDR / ISO 대응 | 통합 접근 |
|-------------|------|----------------|-----------|
| Technical Documentation | Art. 11 | MDR Annex II/III | 통합 TD에 AI Act Annex IV 항목 별도 섹션 추가 |
| Record-keeping (Logging) | Art. 12 | MDR Annex I §17.2, IEC 62304 | 추론 로그 설계: 입력 영상 ID, 출력 결과, 신뢰도 점수, 타임스탬프. PII 분리·보존 기간 규정 |
| Transparency/IFU | Art. 13 | MDR Annex I §23, IEC 82304-1 | IFU에 의도된 용도, 한계(false positive/negative 비율), 성능 지표, 모니터링 지표 명시 |
| Human Oversight | Art. 14 | MDR Annex I §14.2, IEC 62366-1 | 사용적합성 파일에 감독 시나리오 추가: 방사선사/의사가 AI 결과를 무시(override)할 수 있는 UI 설계 |

### 4.4 정확도·견고성·사이버보안

| AI Act 요건 | 조항 | MDR / ISO 대응 | 통합 접근 | X-ray 적용 |
|-------------|------|----------------|-----------|-----------|
| Accuracy | Art. 15(1) | MDR Annex I §1 | 임상 성능 시험 + AI 성능 지표 결합 | AUC, Sensitivity, Specificity, PPV, NPV (해부 구조별·병변별) |
| Robustness | Art. 15(3) | MDR Annex I §17.2 | Stress Testing: 입력 변형, 장비 변동, 환경 변화 | 다양한 kVp/mAs 조합, 노이즈 주입, 저선량 영상 테스트 |
| Cybersecurity | Art. 15(4) | MDR Annex I §17.4, IEC 81001-5-1 | 사이버보안 계획 통합 | DICOM 통신 보안, 모델 파일 무결성 검증 |

### 4.5 QMS & 적합성평가

| AI Act 요건 | 조항 | MDR / ISO 대응 | 통합 접근 |
|-------------|------|----------------|-----------|
| QMS | Art. 16-17 | MDR Art. 10(9), ISO 13485, QMSR §820.25 | 기존 QMS 확장: AI 데이터·모델 변경관리 절차 추가 (SOP-AIGOV-001, SOP-AIDATA-001) |
| 적합성평가 경로 | Art. 43 | MDR Annex IX/X/XI | MDR 경로에 AI Act 요건 포함하여 단일 평가. NB 선택 시 AI Act 지정 범위 확인 필수 |

### 4.6 시판 후 관리

| AI Act 요건 | 조항 | MDR / ISO 대응 | 통합 접근 | X-ray 적용 |
|-------------|------|----------------|-----------|-----------|
| Post-market monitoring | Art. 61 | MDR Art. 83-86 (PMS/PSUR) | 통합 PMS Plan/Report에 모델 성능 모니터링·드리프트 지표 포함 | AUC 월간 추적, 드리프트 임계 ±5% 시 경보 |
| Serious incident reporting | Art. 62 | MDR Art. 87 (Vigilance) | Vigilance SOP 단일화, AI 관련 추가 필드(모델 버전, 입력 데이터 특성) | AI 오판독으로 인한 진단 지연/오진 → FSCA 연계 |

## 5. PCCP / Change Management

| 규제 | 변경관리 접근 | 통합 방안 |
|------|-------------|-----------|
| AI Act Art. 43(4) | 사전 계획된 변경(재학습) → "substantial modification" 예외 허용 | SOP-CC-001에 PCCP 섹션: 사전 승인 범위, 성능 기준, 검증 방법 명시 |
| MDR | 중요 변경 시 NB 보고 | PCCP 범위 내 변경 → NB 사전 합의, 범위 외 → 변경 인증 |
| 디지털의료제품법 | 변경관리 계획(CMP) 제출 가능 | CMP와 PCCP 구조 통합 (단일 문서) |
| FDA | PCCP Draft Guidance (2023) | 동일 프레임워크 활용, 미국 제출용 별도 섹션 |

## 6. Gap → 조치 매트릭스

| # | Gap | 심각도 | 조치 | 담당 | 연계 문서 | 목표 완료 |
|---|-----|--------|------|------|-----------|-----------|
| 1 | Risk File에 AI 특유 위험 템플릿 부재 | 높음 | ISO 14971 위험관리 계획·표에 AI 위험 카탈로그(편향/드리프트/적대적입력/설명가능성) 추가 | RA/QA | SOP-RM-001, F-RM-002 | 2026 Q3 |
| 2 | 데이터 거버넌스 SOP 부재 | 높음 | SOP-AIDATA-001 수립: 수집/라벨링/편향감사/버전관리 | SW/Data | SOP-AIDATA-001 | v0.2 완료 |
| 3 | 모델 변경관리 절차 보강 필요 | 높음 | SOP-CC-001에 PCCP 섹션 추가, AI 변경 판정 기준 구체화 | RA/QA | SOP-CC-001 | v0.2 완료 |
| 4 | PMS에 모델 성능 지표 부재 | 중간 | PMS Plan에 AUC/Sensitivity/Specificity/드리프트 모니터링 포함 | RA | SOP-PSUR-001 | 2026 Q3 |
| 5 | 기술문서 구조가 MDR 전용 | 중간 | TD 템플릿에 AI Act Annex IV 매핑 컬럼 도입 | RA | TF-TD-001 | 2026 Q3 |
| 6 | NB AI Act 지정 범위 확인 미완 | 중간 | NB 선정 시 AI Act 범위 포함 여부 확인 계획 수립 | RA | — | 2026 Q4 |

## 7. 양식: F-AIAMD-GAP-001 AI Act × MDR 갭 분석 워크시트

```
=== AI Act × MDR 갭 분석 워크시트 ===

제품명:                           MDR Class:
AI 기능 설명:                     AI Act 분류:
분석 일자:                        분석자:

| # | AI Act 조항 | MDR 대응 조항 | 현재 충족 수준 | 갭 설명 | 조치 계획 | 완료 목표 | 상태 |
|---|-------------|--------------|---------------|---------|-----------|-----------|------|
| 1 | Art. 9 Risk Mgmt | Annex I §3 | ☐ 충족 / ☐ 부분 / ☐ 미충족 | | | | |
| 2 | Art. 10 Data Gov. | Annex II §6.1 | ☐ 충족 / ☐ 부분 / ☐ 미충족 | | | | |
| 3 | Art. 11 Tech Doc | Annex II/III | ☐ 충족 / ☐ 부분 / ☐ 미충족 | | | | |
| 4 | Art. 12 Logging | Annex I §17.2 | ☐ 충족 / ☐ 부분 / ☐ 미충족 | | | | |
| 5 | Art. 13 Transparency | Annex I §23 | ☐ 충족 / ☐ 부분 / ☐ 미충족 | | | | |
| 6 | Art. 14 Human Oversight | Annex I §14.2 | ☐ 충족 / ☐ 부분 / ☐ 미충족 | | | | |
| 7 | Art. 15 Accuracy/Robust/Cyber | Annex I §17 | ☐ 충족 / ☐ 부분 / ☐ 미충족 | | | | |
| 8 | Art. 16-17 QMS | Art. 10(9) | ☐ 충족 / ☐ 부분 / ☐ 미충족 | | | | |
| 9 | Art. 43 CA | Annex IX/X/XI | ☐ 충족 / ☐ 부분 / ☐ 미충족 | | | | |
| 10 | Art. 61 PMS | Art. 83-86 | ☐ 충족 / ☐ 부분 / ☐ 미충족 | | | | |
| 11 | Art. 62 Incident | Art. 87 | ☐ 충족 / ☐ 부분 / ☐ 미충족 | | | | |

서명: _____________________ 일자: _______________
```

## 8. 한국·미국 연계 참고

| 규제 | 대응 개념 | 통합 가능성 |
|------|----------|-------------|
| 디지털의료제품법 (KR) | SaMD·AI 규정, 변경관리계획(CMP) | CMP = PCCP 구조 통합 |
| FDA GMLP 원칙 (US) | AI/ML SaMD 개발 원칙 | 데이터 거버넌스·투명성 요건 정합 |
| FDA PCCP (US) | 사전 계획 변경관리 | 단일 PCCP 문서로 EU/US/KR 대응 |
| FDA Pre-market Cyber Guidance (US) | 사이버보안 사전심사 | IEC 81001-5-1 기반 통합 |

## 9. 출처

- Regulation (EU) 2024/1689 (AI Act) — 전문, Art. 6, 9-17, 43, 61-62, Annex II/III/IV
- Regulation (EU) 2017/745 (MDR) — Art. 10, 15, 83-87, Annex I-III, IX-XI
- MDCG 2019-11 (소프트웨어 분류), MDCG 2019-16 Rev.1 (사이버보안), MDCG 2020-3 (significant changes)
- IEC 62304:2006/A1:2015, IEC 62366-1:2015/A1:2020, IEC 81001-5-1:2021
- ISO 14971:2019/A11:2021
- FDA AI/ML-based SaMD Action Plan, PCCP Draft Guidance 2023
- DQS Global — AI Act & AI-Enabled Medical Devices: Regulatory Status 2026
- MedDeviceGuide — EU AI Act for Medical Devices Compliance Guide 2026
- Gibson Dunn — EU AI Act Omnibus Agreement: Postponed High-Risk Deadlines (2026)
- Bird & Bird — The Commission's Draft High-Risk AI Guidelines under the EU AI Act: A First Read (2026)
- European Commission — Draft Commission Guidelines on classification of high-risk AI systems under Art. 6 (2026-05-19, 의견수렴 ~2026-06-23)


## 12. D-43 AI 리터러시(Art.4) 발효 준비도 매트릭스 (2026-06-20 기준 — v0.5 신규)

> **현재 위치:** 2026-06-20. AI 리터러시 의무(Art.4) 발효 2026-08-02 = **D-43 (영업일 기준 약 31일 잔여)**. Omnibus는 고위험 의무를 연기하나 **Art.4는 영향 없음**.

### 12.1 D-43 잔여 의무 — 즉시 충족 대상

| 의무 | 출처 | 책임 | 산출물 | 완료 SLA | 상태 |
|---|---|---|---|---|---|
| AI 시스템 운영·사용 인력에 대한 충분한 AI 리터러시 보장 | Art.4 | QA·HR | 교육 커리큘럼·교육 기록 (F-TRN-001) | D-30(2026-07-22) | ☐ Pending |
| GPAI 사용 시 모델 제공자 의무 인식 교육 | Art.4 + Chap. V | RA | 내부 가이드(GUIDE-AI-002 신규 검토) | D-20(2026-08-02) | ☐ Pending |
| AI 위험·한계·인간감독 시나리오 교육 (의료영상 판독자 대상) | Art.4 + Art.14 | RA·임상 | 교육 자료 + 평가시험 | D-15 | ☐ Pending |
| 외부 협력자(MR/PRRC, NB 보조인력)에게도 적용 | Art.4 | HR·QA | 외부 교육 합의서 | D-10 | ☐ Pending |

### 12.2 D-43 잔여 의무 — High-risk 의무 (Omnibus 미발효 시 시나리오)

> **시나리오 분기:** (A) Omnibus 정식 채택·관보 게재 완료 → 고위험 의무 연기 적용(Annex I 2028-08-02). (B) 미완료 → 기존 일정(2026-08-02) 유지.
>
> **현재 baseline은 (B)** — 2026-06-20 시점 Omnibus 관보 게재 미확인. 정식 채택 시점에 본 표 재평가.

| 의무 | (B) 시 SLA | 현 충족 수준 |
|---|---|---|
| Art.9 Risk Management 통합 (Risk File에 AI 위험 카탈로그) | D-43 | 갭 #1 진행 중 (목표 2026 Q3) |
| Art.10 Data Governance SOP-AIDATA-001 | D-43 | 갭 #2 v0.2 완료 (충족) |
| Art.11 Technical Documentation Annex IV 매핑 | D-43 | 갭 #5 진행 중 |
| Art.12 추론 로그 설계 | D-43 | 일부 충족 — 보강 필요 |
| Art.13 IFU(투명성) | D-43 | TF-TD-001 v0.2 일부 충족 |
| Art.14 Human Oversight | D-43 | 사용적합성 파일 보강 필요 |
| Art.15 정확도·견고성·사이버보안 | D-43 | 일부 충족 |
| Art.16-17 QMS 확장 | D-43 | 충족 (SOP-AIGOV-001) |
| Art.43 적합성평가 NB 범위 확인 | D-43 | 갭 #6 미완 (목표 2026 Q4) |
| Art.49 EU DB 등록 | 시판 전 | 미해당 (시판 전 단계) |
| Art.61-62 PMS·중대사고 보고 통합 | D-43 | SOP-PSUR-001·Vigilance 통합 충족 |

**Worst case 분석(시나리오 B):** D-43 내 100% 충족 불가능. 위험 완화책:
1. 정식 채택·관보 게재 즉시 시나리오 (A) 적용 자동 발동.
2. (B) 지속 시 시판 일정 재검토 + NB 사전 협의(고위험 적합성평가 경로 명확화).
3. AI 리터러시(Art.4)는 어떤 경우든 D-43 충족.

### 12.3 D-43 액션 플랜 (영업일 단위)

| 영업일 D-day | 활동 | 책임 | 산출물 | 종속성 |
|---|---|---|---|---|
| D-43~D-35 | AI 리터러시 커리큘럼 초안·교육자료 작성 | QA·HR | 교육 슬라이드, 평가시험 | — |
| D-35~D-30 | 내부 교육 1차 실시(전 직원 대상) | HR | F-TRN-001 기록 | 커리큘럼 확정 |
| D-30~D-25 | 외부 협력자 교육 합의서 발송 | HR·법무 | 외부 합의서 회신 | 내부 교육 사례 |
| D-25~D-20 | GPAI 사용 인식 가이드 발행 | RA | GUIDE-AI-002 | — |
| D-20~D-15 | Omnibus 관보 게재 모니터링 + 시나리오 (A)/(B) 결정 | RA | 결정 메모 | EU 공식 발표 |
| D-15~D-10 | (시나리오 B 채택 시) 고위험 의무 보강 작업 가속 | RA·QA·SW | 갭 #1·#5·#6 종결 시도 | — |
| D-10~D-5 | 내부 점검·자체 감사 | QA Lead | 자체 감사 보고서 | 모든 준비 완료 |
| D-5~D-0 | 잔여 조치·고객·NB 통보 | RA·CEO | 외부 통보 메모 | 자체 감사 통과 |

### 12.4 KPI

| 지표 | 목표 | 측정 |
|---|---|---|
| AI 리터러시 교육 이수율 (대상 인원) | 100% | 2026-08-02 기준 |
| GPAI 사용 부서 인식 교육 완료 | 100% | D-15 기준 |
| Omnibus 시나리오 결정 메모 발행 | 1건 | D-15 기준 |
| 고위험 의무 D-43 충족률 (시나리오 B 시) | ≥ 80% | D-5 기준 |
| 외부 협력자 교육 합의서 회신율 | ≥ 90% | D-5 기준 |

### 12.5 적대적 자기검토 (D-43 관점)
- Q: "Art.4 AI 리터러시 의무가 Omnibus와 무관함을 누가 보장하는가?" → A: §3 Omnibus 동향 + 본 §12.1 명시.
- Q: "시나리오 (B) 발생 시 시판 영향 평가는?" → A: §12.2 worst case 완화책 §2.
- Q: "교육 대상은 자사 직원만인가, 외부 협력자도 포함하는가?" → A: §12.1 4번째 행(외부 협력자 포함).
- Q: "교육 효과성 측정은?" → A: 평가시험(§12.3 D-43~D-35) + 이수율 KPI(§12.4).


## 10. 개정 이력

| 버전 | 일자 | 내용 |
|------|------|------|
| v0.1 | 2026-04-20 | 초안 작성 (High-risk 기준·요건 매핑·Gap) |
| v0.2 | 2026-05-26 | 분류 판단 절차·적용 일정 구체화, X-ray 적용 예시 전면 보강, 양식 F-AIAMD-GAP-001 추가, 상호참조 확충, Gap 조치 매트릭스 상세화 |
| v0.3 | 2026-06-10 | 2026 Omnibus 고위험 시점 연기(이사회 03-13: Annex III→2027-12-02, Annex I→2028-08-02) 및 집행위 고위험 분류 가이드라인 초안(05-19, 의견수렴 ~06-23) 반영. AI 리터러시(Art.4) 2026-08-02 유지 명시. 출처 보강 |
| v0.4 | 2026-06-11 | 2026 Omnibus 입법 진행상황 갱신 — 2026-05-07 trilogue 잠정 합의 도달, 정식 채택 6월·관보 게재 7월 예상 반영. 기존 baseline(2026-08-02/2027-08-02) 대비 유지. 출처(Gibson Dunn·Inside Privacy) 보강 |
| v0.5 | 2026-06-20 | §12 D-43 AI 리터러시(Art.4) 발효 준비도 매트릭스 신규 (이슈 #1527). 시나리오 (A) Omnibus 채택 / (B) baseline 분기, 영업일 단위 액션 플랜, KPI 5종, 적대적 자기검토 4항목 |
