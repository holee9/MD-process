---
doc-id: EU_AI_Act_MDR_중첩적용_매핑
title: "EU AI Act ↔ EU MDR 중첩 적용 매핑 (AI/ML SaMD 대비)"
type: Matrix
version: v0.9.1
status: draft
category: 01_법규_규제
purpose: "EU AI Act(2024/1689)와 EU MDR(2017/745) 간 중첩 요건 식별, 단일 QMS/기술문서 통합 충족 전략 및 X-ray AI 영상 분석 시스템 적용 지침"
applicable: [EU AI Act(Regulation 2024/1689), Regulation (EU) 2026/1744(Digital Omnibus on AI, 발효 2026-07-27), EU MDR 2017/745, ISO13485:2016, ISO14971:2019, IEC62304:2006/A1:2015, IEC62366-1:2015/A1:2020, IEC81001-5-1:2021, FDA QMSR 21 CFR 820, 디지털의료제품법]
forms: [F-AIAMD-GAP-001]
related-docs: [EU_MDR_2017_745, GSPR_정합표준_매핑표, GSPR_체크리스트_v0.2_템플릿, SOP-AIGOV-001, SOP-AIDATA-001, SOP-CC-001, SOP-RM-001, SOP-PSUR-001, 디지털의료제품법_SaMD_AI_요구]
related-issues: [4, 7, 20, 21, 48, 58, 1527]
owner: RA/QA Lead
last-review: 2026-09-25
review-due: 2027-06-27
---

# EU AI Act ↔ EU MDR 중첩 적용 매핑 (AI/ML SaMD 대비)

## 1. 목적

본 문서는 AI/ML 기반 의료 SW(SaMD), 특히 X-ray 영상 판독 보조 기능을 염두에 두고 EU AI Act (Regulation (EU) 2024/1689)와 EU MDR (Regulation (EU) 2017/745) 간 중첩 요건을 식별하고, 단일 QMS/기술문서에서 동시에 충족하기 위한 매핑을 정리한다.

## 2. 위험 분류 — 중첩 조건

### 2.1 High-risk AI 분류 판단 절차

```
1. 제품이 EU 조화법령(**Annex I**, Section A point 11 = Reg. (EU) 2017/745 MDR) 대상인가?
   ├─ Yes: MDR/IVDR 등재 확인
   │   └─ 제3자 적합성평가(NB) 필요한 Class?
   │       ├─ Class IIa/IIb/III → High-risk AI system (Art. 6(1))
   │       └─ Class I (non-sterile·non-measuring·비재사용 수술기구, self-cert) → Art.6(1) 비해당 (단, Annex III 별도 확인)
   │          ※ Class Is/Im/Ir(멸균·측정·재사용 수술기구)은 NB 관여 → **Art.6(1) 해당** (MDCG 2025-6/AIB 2025-1 Q2·Table 1)
   └─ No: Annex III 별도 해당 여부 확인

2. High-risk 확정 시
   ├─ AI Act Chapter III 전체 요건 적용
   ├─ 적합성평가 경로: MDR 경로에 AI Act 요건 통합
   └─ EU DB 등록 의무 (Art. 49)
```

**판정 기준**: 대부분의 Class IIa 이상 AI SaMD는 NB 관여가 필요하므로 High-risk 분류 가능성이 높다.

### 2.2 X-ray AI 시스템 분류 예시

| 구성요소 | MDR Class | MDR 분류규칙 (Annex VIII) | NB 필요 | AI Act 분류 | 근거 |
|----------|-----------|---------------------------|---------|-------------|------|
| AI 영상 판독 보조 SW (CADe/CADx) | IIa~IIb | Rule 11 (진단 결정 정보 제공; 영향 중대도에 따라 IIa/IIb/III) | Yes | **High-risk** | Art. 6(1) + **Annex I Section A point 11** (MDR) |
| X-ray 콘솔 SW (비AI) — 발생기 제어·노출 파라미터 설정 포함 | **IIb** | Rule 10 (진단용 전리방사선 기기를 제어·감시하거나 성능에 직접 영향) + Ch.II 3.3 (구동 SW = 기기 동일등급) | Yes | **비해당** | AI 기능 없음 |
| (참고) 영상 표시·저장 전용 SW (발생기 제어 없음, 분리 모듈) | 해석범위: Rule 11 판단 대상 (I~IIb) | Rule 11 | 등급에 따름 | **비해당** | AI 기능 없음 — 기능 분할 근거를 기술문서에 명시 |
| AI 자동 노출 제어 (AEC) | **IIb** | Rule 10 (X-ray 발생기 성능에 직접 영향) + Ch.II 3.3 | Yes | **High-risk** | 안전 구성요소 — Art.6(1) + Annex I Section A point 11 |
| AI 데이터 분석 (통계 리포트) | IIa (잠정) | Rule 11 (진단·치료 결정 목적이 아니면 Class I 가능 — 의도된 용도로 판정) | 등급에 따름 | 판단 필요 | Rule-based vs. ML 여부 |

## 3. 적용 일정 (단계별)

| 시점 | AI Act 적용 내용 | MDR 상태 | 비고 |
|------|-----------------|----------|------|
| 2024-08-01 | AI Act 발효 | MDR 전면 적용 중 | |
| **2025-02-02** | 금지 AI 관행(Chap.II) 적용 + **AI 리터러시 의무(Art.4) 적용일(applicability) — 이미 적용 중** | — | **Art.113(a)** — "Chapters I and II shall apply from 2 February 2025"(Art.4는 Chapter I 소재); 의료기기 운영·사용 인력 대상 |
| 2025-08-02 | 범용 AI 모델(GPAI) 규칙 적용 | — | 의료기기 탑재 GPAI 해당 시 |
| **2026-07-27** | **Regulation (EU) 2026/1744 (Digital Omnibus on AI) 발효** — 고위험 의무 적용일 연기 **확정** | MDR 전면 적용 | 채택 2026-07-08 / OJ L 게재 2026-07-24 / 발효 2026-07-27 (CELEX 32026R1744) |
| **2026-08-02** | **거버넌스·감독·과징금(Art.99 등) 적용일** — Art.4 등 기적용 의무에 대한 enforcement 개시 | MDR 전면 적용 | **Art.113 본문(chapeau, 일반 적용일)** — "It shall apply from 2 August 2026". Art.4 의무는 2025-02-02부터 이미 적용 중이므로 본 시점은 enforcement 트리거 |
| **2027-12-02** | 독립형(Annex III) 고위험 의무 적용 | MDR 전면 적용 | 당초 2026-08-02 → 연기 |
| **2028-08-02** | **MDR/IVDR 등 규제제품 탑재형(Annex I) 고위험 의무 적용 — 자사 X-ray AI 모듈 해당** | MDR 전면 적용 | **핵심 마일스톤**. 당초 2027-08-02(Art.113(c)) → 연기 |

**주의**: Regulation (EU) 2026/1744 발효(2026-07-27)로 MDR Annex I 제품 탑재형 고위험 AI의 의무 적용일은 **2028-08-02**로 확정 이동하였다(당초 2027-08-02). 다만 Art.50 투명성 의무·GPAI 의무·Art.5 금지관행·Art.4 리터러시 의무는 **연기 대상이 아니며 기존 일정대로 적용 중**이다. NB 선정 시 AI Act 지정 범위(designated scope) 포함 여부를 반드시 확인한다.

> **✅ 2026 Omnibus 개정 — 확정 (2026-09-11 갱신, audit #1041):** **Regulation (EU) 2026/1744** of the European Parliament and of the Council **of 8 July 2026** amending Regulations (EU) 2024/1689, (EU) 2018/1139 and (EU) 2023/1230 (**Digital Omnibus on AI**)이 **OJ 2026-07-24 게재, 2026-07-27 발효**되었다(CELEX 32026R1744, `eli:date_document 2026-07-08`, `eli:first_date_entry_in_force 2026-07-27`). 이로써 고위험 AI 의무 적용일은 독립형(Annex III) **2027-12-02**, MDR/IVDR 등 규제제품 탑재형(Annex I — **자사 X-ray AI 영상분석 모듈 해당**) **2028-08-02**로 **연기 확정**되었다. 종전 문서가 지시하던 "정식 채택 전까지 기존 일정(2026-08-02/2027-08-02)을 구속력 있는 기준선으로 간주" 지침은 **폐지**한다. **변동 없는 항목**: AI Act 발효 2024-08-01, Art.5 금지관행·Art.4 AI 리터러시 적용 2025-02-02(Art.113(a)), GPAI 2025-08-02, 일반 적용일(chapeau) 2026-08-02, Art.50 투명성 의무 — Omnibus는 이들 일자를 변경하지 않았다. **추가 검토 항목**: Omnibus가 신설한 Art.5 금지관행 추가분(AI 생성 비동의 성적 이미지·CSAM 관련)의 자사 해당 여부 별도 확인 필요.
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
| FDA | **PCCP Final Guidance — Marketing Submission Recommendations for a Predetermined Change Control Plan for AI-Enabled Device Software Functions** (Final; latest content August 2025; Docket FDA-2022-D-2628; original final issued December 2024) | 동일 프레임워크 활용, 미국 제출용 별도 섹션 — Final 기준 **AI-enabled device software functions 전반**으로 범위 확대(ML 한정 아님), modifications 설명·labeling 고려사항·diversity 고려·intended use 명확화 반영 |

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

- Regulation (EU) 2024/1689 (AI Act) — 전문, Art. 6, 9-17, 43, 61-62, Annex I(Section A point 11: MDR)/III/IV (※ Annex II는 Art.5(1)(h)(iii) 형사범죄 목록으로 본 문서 비해당)
- MDCG 2025-6 / AIB 2025-1 (2025-06) — Interplay between MDR/IVDR and AIA, Q2·Table 1 (Art.6(1) 적용 조건)
- Regulation (EU) 2017/745 Annex VIII Chapter III Rule 10·11·17 및 Chapter II 3.3 (legislation.gov.uk adopted text)
- Regulation (EU) 2017/745 (MDR) — Art. 10, 15, 83-87, Annex I-III, IX-XI
- MDCG 2019-11 (소프트웨어 분류), MDCG 2019-16 Rev.1 (사이버보안), MDCG 2020-3 (significant changes)
- IEC 62304:2006/A1:2015, IEC 62366-1:2015/A1:2020, IEC 81001-5-1:2021
- ISO 14971:2019/A11:2021
- FDA — AI/ML-based SaMD Action Plan (2021)
- FDA — **Marketing Submission Recommendations for a Predetermined Change Control Plan for AI-Enabled Device Software Functions, Final Guidance** (Final; latest content current as of 2025-08-18; Docket FDA-2022-D-2628; original final issued December 2024)
- DQS Global — AI Act & AI-Enabled Medical Devices: Regulatory Status 2026
- MedDeviceGuide — EU AI Act for Medical Devices Compliance Guide 2026
- Gibson Dunn — EU AI Act Omnibus Agreement: Postponed High-Risk Deadlines (2026)
- Bird & Bird — The Commission's Draft High-Risk AI Guidelines under the EU AI Act: A First Read (2026)
- European Commission — Draft Commission Guidelines on classification of high-risk AI systems under Art. 6 (2026-05-19, 의견수렴 ~2026-06-23)
- **EUR-Lex — Regulation (EU) 2026/1744 of 8 July 2026 (Digital Omnibus on AI), CELEX 32026R1744, OJ 2026-07-24, 발효 2026-07-27** — https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng (Tier1, 2026-09-11 직접 열람)


## 12. AI 리터러시(Art.4) 갭점검 매트릭스 — Enforcement(2026-08-02, 경과) 사후 점검 (2026-09-11 기준 — v0.9)

> **사실관계 정정 (audit #905·#919):** Art.4 AI 리터러시 의무의 **적용일(applicability)은 2025-02-02**(Art.113(a))로 이미 약 17개월 전부터 적용 중이다. **2026-08-02**(Art.113 본문 chapeau, 일반 적용일)는 **감독·집행(enforcement, Art.99 등)** 적용일이며, 본 매트릭스는 (2026-08-02 경과 후인 현재) 적용 중 상태의 잔존 갭을 제거하기 위한 자가점검이다. v0.5에서 "발효 2026-08-02 = D-43"으로 적용일과 enforcement를 혼동한 표현은 사실오류였고(v0.6에서 분리), v0.6에서 enforcement 일자를 "2026-08-03" 및 Art.113(b)/(c)로 기재한 것 역시 1차 출처와 불일치하여 v0.7에서 정정.

> **현재 위치:** 2026-09-11. Art.4 의무는 **2025-02-02부터 적용 중**(Art.113(a)), enforcement(Art.99 등) 적용일 **2026-08-02은 이미 경과**하였다. 따라서 본 매트릭스는 사전 대비가 아니라 **적용 중 상태의 사후 준수 점검(잔존 갭 즉시 해소)** 으로 성격이 전환된다 — 종전 'D-36' 기준 D-day 표기는 기준일 경과로 무효이며, 잔존 항목의 SLA는 **즉시(즉응)** 로 재설정한다. Omnibus(Reg. (EU) 2026/1744)는 고위험 의무를 연기하나 **Art.4 적용일·enforcement 일정에는 영향 없음**.

### 12.1 Art.4 갭 — 즉시 충족 대상 (이미 적용 중)

| 의무 | 출처 | 책임 | 산출물 | 완료 SLA | 상태 |
|---|---|---|---|---|---|
| AI 시스템 운영·사용 인력에 대한 충분한 AI 리터러시 보장 | Art.4 | QA·HR | 교육 커리큘럼·교육 기록 (F-TRN-001) | 즉시 (기준일 경과) | ☐ Pending |
| GPAI 사용 시 모델 제공자 의무 인식 교육 | Art.4 + Chap. V | RA | 내부 가이드(GUIDE-AI-002 신규 검토) | 즉시 (기준일 경과) | ☐ Pending |
| AI 위험·한계·인간감독 시나리오 교육 (의료영상 판독자 대상) | Art.4 + Art.14 | RA·임상 | 교육 자료 + 평가시험 | 즉시 (기준일 경과) | ☐ Pending |
| 외부 협력자(MR/PRRC, NB 보조인력)에게도 적용 | Art.4 | HR·QA | 외부 교육 합의서 | 즉시 (기준일 경과) | ☐ Pending |

### 12.2 High-risk 의무 — 적용 기준일 확정 (Art.4와는 별개 트랙)

> **시나리오 분기 종결(audit #1041):** 종전 (A)/(B) 분기는 **(A)로 확정**되었다 — Regulation (EU) 2026/1744 발효(2026-07-27)로 Annex I 탑재형(자사 X-ray AI 모듈) 고위험 의무 적용일은 **2028-08-02**. (B) 트랙(2026-08-02 baseline)은 **삭제**한다.
>
> **본 표의 기준일:** **2028-08-02**(Annex I). SLA는 해당 기준일 대비 역산하며, 아래 표의 'SLA' 열은 **내부 목표 마일스톤**으로 재설정한다(종전 D-36 표기 무효).

| 의무 | 내부 목표 마일스톤 (기준일 2028-08-02) | 현 충족 수준 |
|---|---|---|
| Art.9 Risk Management 통합 (Risk File에 AI 위험 카탈로그) | 2027-Q4 | 갭 #1 진행 중 (목표 2026 Q3) |
| Art.10 Data Governance SOP-AIDATA-001 | 2027-Q4 | 갭 #2 v0.2 완료 (충족) |
| Art.11 Technical Documentation Annex IV 매핑 | 2027-Q4 | 갭 #5 진행 중 |
| Art.12 추론 로그 설계 | 2027-Q4 | 일부 충족 — 보강 필요 |
| Art.13 IFU(투명성) | 2027-Q4 | TF-TD-001 v0.2 일부 충족 |
| Art.14 Human Oversight | 2027-Q4 | 사용적합성 파일 보강 필요 |
| Art.15 정확도·견고성·사이버보안 | 2027-Q4 | 일부 충족 |
| Art.16-17 QMS 확장 | 2027-Q4 | 충족 (SOP-AIGOV-001) |
| Art.43 적합성평가 NB 범위 확인 | 2027-Q4 | 갭 #6 미완 (목표 2026 Q4) |
| Art.49 EU DB 등록 | 시판 전 | 미해당 (시판 전 단계) |
| Art.61-62 PMS·중대사고 보고 통합 | 2027-Q4 | SOP-PSUR-001·Vigilance 통합 충족 |

**잔여 리스크 분석(기준일 2028-08-02):** 내부 목표 마일스톤(2027-Q4) 내 100% 충족이 지연될 경우의 완화책:
1. 정식 채택·관보 게재 즉시 시나리오 (A) 적용 자동 발동.
2. (B) 지속 시 시판 일정 재검토 + NB 사전 협의(고위험 적합성평가 경로 명확화).
3. AI 리터러시(Art.4) 의무는 **이미 적용 중**이므로 즉시 갭 제거(교육 이수)하고, 2026-08-02 enforcement 이전까지 증빙(F-TRN-001) 완비.

### 12.3 준수 액션 플랜 (2026-08-02 경과 후 — 즉응 기준, 착수일 2026-09-11)

> Art.4 및 enforcement 기준일이 모두 경과하였으므로 종전 D-day 역산 표기는 폐기하고 **착수일 기준 주차(週次)** 로 재설정한다.

| 시기 | 활동 | 책임 | 산출물 | 종속성 |
|---|---|---|---|---|
| 1주차 | AI 리터러시 커리큘럼 초안·교육자료 작성 | QA·HR | 교육 슬라이드, 평가시험 | — |
| 2주차 | 내부 교육 1차 실시(전 직원 대상) | HR | F-TRN-001 기록 | 커리큘럼 확정 |
| 2~3주차 | 외부 협력자 교육 합의서 발송 | HR·법무 | 외부 합의서 회신 | 내부 교육 사례 |
| 3주차 | GPAI 사용 인식 가이드 발행 | RA | GUIDE-AI-002 | — |
| (종결) | Omnibus 관보 게재 모니터링 + 시나리오 결정 — **완료·종결**(Reg. (EU) 2026/1744, OJ 2026-07-24 / 발효 2026-07-27, 시나리오 (A) 확정) | RA | 결정 메모 | EU 공식 발표 |
| 4주차~ | 고위험 의무(Annex I, 기준일 2028-08-02) 보강 — 갭 #1·#5·#6 | RA·QA·SW | 갭 종결 기록 | 내부 목표 2027-Q4 |
| 4주차 | 내부 점검·자체 감사 | QA Lead | 자체 감사 보고서 | 상기 조치 완료 |
| 5주차 | 잔여 조치·고객·NB 통보 | RA·CEO | 외부 통보 메모 | 자체 감사 통과 |

### 12.4 KPI

| 지표 | 목표 | 측정 |
|---|---|---|
| AI 리터러시 교육 이수율 (대상 인원) | 100% | 적용 중 — 상시 100% 유지 (기준일 2026-08-02 경과) |
| GPAI 사용 부서 인식 교육 완료 | 100% | 적용 중 — 상시 100% 유지 |
| Omnibus 시나리오 결정 메모 발행 | 1건 | **완료** — Reg. (EU) 2026/1744 확정 반영(2026-09-11) |
| 고위험 의무(Annex I, 기준일 2028-08-02) 충족률 | ≥ 80% | 2027-Q4 기준 |
| 외부 협력자 교육 합의서 회신율 | ≥ 90% | 적용 중 — 상시 유지 |

### 12.5 적대적 자기검토 (2026-09-11 관점)
- Q: "Art.4 AI 리터러시 의무의 적용 시점은?" → A: **2025-02-02부터 이미 적용**(Reg. 2024/1689 Art.113(a) — Chapters I, II from 2 February 2025). Enforcement(Art.99 등)는 **2026-08-02**부터(Art.113 본문 chapeau, 일반 적용일). Omnibus와 무관(§3 단서·§12 본문).
- Q: "자사 X-ray AI 모듈의 고위험 의무 적용 기준일은?" → A: **2028-08-02**(Annex I 탑재형). Reg. (EU) 2026/1744 발효(2026-07-27)로 확정 — 종전 (B) baseline(2026-08-02)은 폐지(§3 단서·§12.2).
- Q: "연기 대상이 아닌 의무는?" → A: Art.5 금지관행·Art.4 리터러시(2025-02-02), GPAI(2025-08-02), Art.50 투명성 및 일반 적용일(2026-08-02) — 모두 **이미 적용 중**.
- Q: "교육 대상은 자사 직원만인가, 외부 협력자도 포함하는가?" → A: §12.1 4번째 행(외부 협력자 포함).
- Q: "교육 효과성 측정은?" → A: 평가시험(§12.3 1주차) + 이수율 KPI(§12.4).


## 10. 개정 이력

| 버전 | 일자 | 내용 |
|------|------|------|
| v0.1 | 2026-04-20 | 초안 작성 (High-risk 기준·요건 매핑·Gap) |
| v0.2 | 2026-05-26 | 분류 판단 절차·적용 일정 구체화, X-ray 적용 예시 전면 보강, 양식 F-AIAMD-GAP-001 추가, 상호참조 확충, Gap 조치 매트릭스 상세화 |
| v0.3 | 2026-06-10 | 2026 Omnibus 고위험 시점 연기(이사회 03-13: Annex III→2027-12-02, Annex I→2028-08-02) 및 집행위 고위험 분류 가이드라인 초안(05-19, 의견수렴 ~06-23) 반영. AI 리터러시(Art.4) 2026-08-02 유지 명시. 출처 보강 |
| v0.4 | 2026-06-11 | 2026 Omnibus 입법 진행상황 갱신 — 2026-05-07 trilogue 잠정 합의 도달, 정식 채택 6월·관보 게재 7월 예상 반영. 기존 baseline(2026-08-02/2027-08-02) 대비 유지. 출처(Gibson Dunn·Inside Privacy) 보강 |
| v0.5 | 2026-06-20 | §12 D-43 AI 리터러시(Art.4) 발효 준비도 매트릭스 신규 (이슈 #1527). 시나리오 (A) Omnibus 채택 / (B) baseline 분기, 영업일 단위 액션 플랜, KPI 5종, 적대적 자기검토 4항목 |
| v0.6 | 2026-06-22 | **사실오류 정정** — Art.4 AI 리터러시 의무의 적용일을 **2025-02-02(이미 적용 중)**로, enforcement(Art.99 등)를 **2026-08-03**으로 명확히 분리. §3 일정 표·단서, §12 제목·헤더·자기검토 재구성 — audit #905 |
| v0.7 | 2026-06-27 | **1차 출처 정합화 (audit #919)** — (1) Art.4 적용 근거를 Art.113(b)→**Art.113(a)** 정정(Art.4는 Chapter I 소재). (2) Enforcement(Art.99 등) 일자를 **2026-08-03→2026-08-02** 정정(Art.113 본문 chapeau "It shall apply from 2 August 2026"; Art.113(c)는 Art.6(1) 고위험 의무로 2027-08-02 적용이므로 enforcement 근거가 될 수 없음). (3) §12 D-Day를 **D-36(2026-06-27 기준 → 2026-08-02)** 로 재계산, §12.1 SLA 일자·§12.3 영업일 표·§12.4 KPI·§12.5 자기검토 일괄 갱신. EUR-Lex Reg. 2024/1689 Art.113 원문 및 European Commission AI Literacy Q&A로 직접 재확인 |
| v0.8 | 2026-06-27 | **노후 인용 갱신 (audit #920)** — §5 PCCP 행 및 §9 출처를 "FDA PCCP **Draft** Guidance (2023)"→"**Final Guidance** — Marketing Submission Recommendations for a Predetermined Change Control Plan for AI-Enabled Device Software Functions (Final; 2025-08-18 현재 본; Docket FDA-2022-D-2628; original final issued December 2024)"으로 갱신. 범위를 ML→**AI-enabled device software functions 전반**으로 보정. FDA Guidance 페이지(2025-08-18 current)로 직접 재확인. 사내 SOP-AIGOV-001 v0.3 "FDA PCCP Guidance 2024" 표기와 정합 회복 |
| v0.9 | 2026-09-11 | **P0 사실성 정정 (audit #1041)** — Regulation (EU) 2026/1744(Digital Omnibus on AI, 채택 2026-07-08 / OJ 2026-07-24 / 발효 2026-07-27, CELEX 32026R1744) 확정 반영. §3 일정표에 발효일·Annex III 2027-12-02·Annex I 2028-08-02 행 신설, '잠정 합의 시·예상·미완료' 조건부 표현 전량 제거. §12.2 시나리오 (A)/(B) 분기를 (A) 확정으로 종결하고 (B) 트랙 삭제, 기준일을 2028-08-02로 재설정. §12 D-36 D-day·KPI 기준일(경과분) 무효화 및 재설정. 자매 문서 SOP-AIGOV-001 §3.1 '제안'→'확정' 동반 정정 |
| v0.9.1 | 2026-09-25 | **audit #1069/#1070 정정** — (1) AI Act 고위험 근거 'Annex II'(§2.1·§2.2·§9, 3개소)→**Annex I Section A point 11**(MDR) 정정(Annex II는 형사범죄 목록). §2.1 Class Is/Im/Ir Art.6(1) 해당 보완(MDCG 2025-6 Table 1). (2) §2.2 AEC·X-ray 콘솔 SW MDR 등급 IIa→**IIb**(Annex VIII Rule 10 + Ch.II 3.3), 'MDR 분류규칙' 열 신설, 표시·저장 전용 SW는 Rule 11 판단(해석범위)으로 분리. 근거: MDR Annex VIII 원문, MDCG 2025-6 Q2 |
