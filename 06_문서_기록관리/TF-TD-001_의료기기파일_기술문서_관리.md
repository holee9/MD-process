---
doc-id: TF-TD-001
title: 의료기기파일 및 기술문서 관리 절차
type: Procedure
category: 06_문서_기록관리
purpose: 의료기기 기술문서(MDF)의 구성·작성·갱신·보관 절차
version: v0.5
status: draft
last-review: 2026-07-02
owner: RA/QA
applicable:
  - ISO 13485:2016
  - EU MDR 2017/745
  - FDA QMSR (21 CFR 820)
  - MFDS GMP
  - IEC 62304
  - IEC 60601-2-54
  - IEC 81001-5-1
  - FDA 510(k) Program Guidance (2014-07-28)
  - FDA SSXI 510(k) Guidance (2016-09-01)
---

# TF-TD-001 의료기기파일 및 기술문서 관리 절차

## 개정 이력

| 버전 | 일자 | 변경 내용 | 작성/승인 |
|------|------|-----------|-----------|
| v0.1 | 2026-05-03 | 초안 — MDF 정의, DHF/DMR/DHR 개요, Annex II 기본 매핑 | holee9-automation |
| v0.2 | 2026-05-30 | STED 매핑, MFDS 별표 상세, FDA QMSR 전환 반영, eDMS 요건, F-TD-002 상세화 | holee9-automation |
| v0.3 | 2026-06-25 | §9.3 §820.35(a)(b)(c)(d) 하위항목 주제 eCFR 1차 재확인 정정 — (a)Records of complaints/(b)Records of servicing activities/(c)UDI/(d)Confidentiality; §9.2·§12.4 동반 정정; Part 11은 §820.35 외부 독립 Part로 표현 [audit #915] | holee9-builder |
| v0.4 | 2026-06-29 | §18 N:M Substantial Equivalence 비교 매트릭스 양식 신설(predicate 최대 5 × model variant cross-product: scintillator×substrate×portability), §18.4 Reference Device 항 분리, §18.5 적합성 표준 일괄 매핑, §18.6 SE 결론문 양식; §17에 F-TD-005 추가; §16 교차참조에 12_벤치마크 3건 추가 [plan #934] | holee9-builder |
| v0.5 | 2026-07-02 | audit 정정: §18.5 FDA Cyber Guidance 2023-09-27 → **2026-02 Final** (Docket FDA-2021-D-1158, 2회 supersede) [audit #938]; §18.6 §807.100(b)(2)(ii)(B) → **(C)** 정정, (B)는 "as safe and as effective" 근거 별기록 [audit #936]; §18.7·§출처 Best Practices Predicate Draft 상태·Docket FDA-2023-D-3134 명시 [audit #937] | holee9-builder |

---

## 1. 목적

의료기기 기술문서(Medical Device File, MDF)의 구성, 작성, 갱신, 보관에 관한 절차를 정의하여 다시장(한국 MFDS / 유럽 EU MDR / 미국 FDA) 인허가 적합성을 확보한다. 본 절차는 자사 의료용 X-ray 시스템, 디지털 디텍터, 관련 SW 제품군에 적용한다.

## 2. 적용 범위

| 구분 | 적용 대상 |
|------|-----------|
| 제품 | 일반촬영/투시 X-ray 시스템, 디지털 디텍터(FPD), 영상처리 SW, AI 보조 기능 SW |
| 문서 유형 | DHF, DMR, DHR, MDF, STED, MFDS 기술문서, FDA Premarket Submission |
| 수명주기 | 설계 입력 ~ 단종 후 보존 기간 종료 시점까지 |
| 관련 부서 | RA, QA, 설계(HW/SW/기구), 제조, 서비스, IT |

## 3. 용어 정의

| 용어 | 정의 |
|------|------|
| MDF (Medical Device File) | ISO 13485 4.2.3 — 제품별 규제 요구사항 및 QMS 절차를 매핑한 최상위 기술문서 파일 |
| DHF (Design History File) | 설계 입력, 출력, 검증, 확인 이력을 포함하는 설계 이력 파일 |
| DMR (Device Master Record) | 완제품 사양, BOM, 도면, SOP 참조 등 제조 기준 문서 집합 |
| DHR (Device History Record) | 개별 제조 단위의 생산 이력 기록 (시리얼번호별) |
| STED | IMDRF/GHTF Summary Technical Documentation — 국제 인허가 기술문서 공통 형식 |
| RMF (Risk Management File) | ISO 14971 위험관리 프로세스 산출물 파일 |
| UEF (Usability Engineering File) | IEC 62366-1 사용적합성 엔지니어링 산출물 파일 |
| eDMS | 전자문서관리시스템 (Electronic Document Management System) |

## 4. 역할 및 책임

| 역할 | 책임 |
|------|------|
| RA 팀장 | MDF 구성 총괄, 시장별 기술문서 완전성 검증, 인허가 제출 승인 |
| QA 팀장 | 문서통제 절차 적합성 감사, DHR/DMR 정합성 확인 |
| 설계팀 리더 | DHF 산출물 작성·갱신, 설계 변경 시 기술문서 갱신 트리거 보고 |
| 제조팀 리더 | DMR/DHR 유지, 공정 변경 시 연계 문서 갱신 |
| PRRC (규제준수책임자) | EU MDR Art. 15 — 기술문서 적합성 최종 확인 |
| IT | eDMS 운영·유지, 접근권한 관리, 백업·감사추적 |

## 5. MDF 구성 체계

### 5.1 MDF 상위 구조

```
MDF (Medical Device File) — TF-TD-001
├── DHF (Design History File)
│   ├── 설계 입력 (사용자 요구, 규제 요건, GSPR 매핑)
│   ├── 설계 출력 (사양서, 도면, SW 설계문서, BOM)
│   ├── 설계 검증 (시험 보고서, EMC, 전기안전, 방사선)
│   ├── 설계 확인 (임상평가, 사용적합성 평가)
│   ├── 설계 변경 이력 (SOP-CC-001 연계)
│   ├── RMF (Risk Management File)
│   ├── UEF (Usability Engineering File)
│   └── 사이버보안 파일 (위협 모델, SBOM, Pen-test)
├── DMR (Device Master Record)
│   ├── 완제품 사양서
│   ├── BOM / 도면 / 라벨링
│   ├── 제조공정 절차 (SOP-MFG 시리즈)
│   ├── 검사·시험 기준서 (IQC/IPQC/FQC)
│   └── 교정 절차 (WI-CAL 시리즈)
├── DHR (Device History Record)
│   ├── 시리얼번호별 제조 기록
│   ├── 입고 검사 기록
│   ├── 공정 검사 기록
│   ├── 최종 검사·출하 시험 기록
│   └── 교정 성적서
├── 규제 제출물
│   ├── EU MDR Annex II 기술문서
│   ├── FDA 510(k) / De Novo
│   ├── MFDS 기술문서 (별표 양식)
│   └── STED (다시장 공통)
└── PMS 기록
    ├── PMS 계획·보고서
    ├── 불만·부작용 기록
    └── PSUR / PMCF
```

### 5.2 DHF / DMR / DHR 관계 다이어그램

```
┌─────────────────────────────────────────────────────────────────────┐
│                DHF / DMR / DHR 관계도                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────┐    설계 이전     ┌─────────────┐    제조 실행      │
│  │    DHF       │ ──────────────→ │    DMR       │ ──────────────→  │
│  │ (설계 이력)  │  Design Transfer│ (제조 기준)  │  Production      │
│  └──────┬──────┘                  └──────┬──────┘                   │
│         │                                │                          │
│    포함 관계                         참조 관계                       │
│         │                                │                          │
│  ┌──────▼──────┐                  ┌──────▼──────┐                   │
│  │    RMF       │                  │    DHR       │                  │
│  │ (위험관리)   │                  │ (제조 이력)  │                  │
│  ├─────────────┤                  ├─────────────┤                   │
│  │    UEF       │                  │ S/N별 기록   │                  │
│  │ (사용적합성) │                  │ - 조립 기록  │                  │
│  ├─────────────┤                  │ - 검사 기록  │                  │
│  │ 사이버보안   │                  │ - 교정 성적  │                  │
│  │ (SBOM 등)   │                  │ - 출하 판정  │                  │
│  └─────────────┘                  └─────────────┘                   │
│                                                                     │
│  ※ DHF는 "왜 이렇게 설계했는가"의 이력                              │
│  ※ DMR은 "이 제품을 어떻게 만드는가"의 기준                         │
│  ※ DHR은 "이 개별 기기를 실제 어떻게 만들었는가"의 증거              │
│                                                                     │
│  [설계 변경 발생 시]                                                 │
│  SOP-CC-001 → DHF 갱신 → DMR 개정 → 이후 DHR에 신규 기준 적용      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 5.3 DHF / DMR / DHR 문서 체크리스트

| 파일 | 점검 항목 | 확인 기준 | 점검 빈도 |
|------|-----------|-----------|-----------|
| DHF | 설계 입력-출력 추적성 매트릭스 존재 | 모든 입력이 출력에 매핑됨 | 설계 변경 시 |
| DHF | 설계 검증 보고서 완결 | 모든 사양 항목 시험 완료 | 설계 변경 시 |
| DHF | 설계 확인 기록 (임상평가, UEF) | 의도된 사용 확인 증거 | 연 1회 |
| DHF | RMF 최신성 | 잔여위험 수용 판정 유효 | 설계 변경 시 + 연 1회 |
| DHF | 사이버보안 파일 (SBOM, Pen-test) | IEC 81001-5-1 산출물 완결 | SW 변경 시 |
| DMR | BOM 현행판 일치 | 생산 BOM = 설계 BOM | 분기 1회 |
| DMR | 제조공정 SOP 유효판 | EDMS 유효 상태 확인 | 분기 1회 |
| DMR | 검사 기준서 최신 반영 | 규격 변경 반영 여부 | 표준 개정 시 |
| DMR | 라벨링/IFU 승인본 | 규제 시장별 최신 승인본 | 변경 시 |
| DHR | 시리얼번호별 기록 완결 | 모든 공정 스텝 서명 완료 | 출하 전 |
| DHR | 입고 검사 성적 | ASL 공급자 성적서 첨부 | 입고 시 |
| DHR | 최종 검사 합격 판정 | FQC 기준 대비 합격 | 출하 전 |
| DHR | 교정 성적서 유효성 | 교정 유효기간 내 시험 | 출하 전 |

## 6. STED (Summary Technical Documentation) 매핑

### 6.1 IMDRF/GHTF STED 섹션 ↔ 자사 문서 매핑

STED는 IMDRF(구 GHTF) N4가 정의한 국제 기술문서 공통 형식으로, 한국(MFDS), 호주(TGA), 캐나다(Health Canada), 일본(PMDA) 등 다수 규제기관이 채택한다.

| STED 섹션 | 섹션 제목 | 내용 요약 | 자사 문서 매핑 | EU MDR Annex II 대응 |
|-----------|-----------|-----------|---------------|---------------------|
| 1 | 기기 설명 (Device Description) | 의도된 사용, 작동 원리, 구성품, 액세서리, 변형 | DMR 사양서, UDI 레코드 (SOP-UDI-001) | §1 |
| 2 | 기기 설계 (Design & Manufacturing) | 설계 명세, 도면, BOM, 제조공정 개요 | DHF 설계 출력, DMR, SOP-MFG-001 | §3 |
| 3 | 위험 분석 (Risk Analysis) | ISO 14971 기반 위험관리 산출물 | RMF (위험분석, FMEA, FTA) | §5 |
| 4 | 제품 검증·확인 (Verification & Validation) | 전기안전, EMC, 성능, SW V&V, 생체적합성 | 05_검사 시험 문서, SW V&V 보고서 | §6 |
| 5 | 소프트웨어 (Software Documentation) | IEC 62304 산출물, SW 아키텍처, 사이버보안 | DHF SW 섹션, SBOM, IEC 81001-5-1 | §6 |
| 6 | 임상 증거 (Clinical Evidence) | 임상평가 보고서, 문헌 검토, 동등성 평가 | 임상평가보고서 (CER) | §5, §6 |
| 7 | 라벨링 (Labeling) | 라벨, IFU, 포장 표시 | DMR 라벨링 섹션, ISO 15223-1 | §1 |
| 8 | 안전성·성능 요약 (SSCP) | EU MDR Art. 32 기반 공개 요약 | SSCP 문서 | Art. 32 |
| 9 | PMS 및 PMCF 계획 | 시판후 감시 계획 | PMS 계획서, PMCF 프로토콜 | Annex III |

### 6.2 STED 활용 시나리오

| 시장 | 기술문서 형식 | STED 기반 여부 | 비고 |
|------|-------------|---------------|------|
| 한국 (MFDS) | MFDS 별표 양식 (기술문서 심사자료) | STED 구조 채택 | 한글 작성, MFDS 고유 양식 항목 추가 |
| EU (MDR) | Annex II + Annex III | STED 호환 | Annex II §1~§6 = STED 1~7 대응 |
| 미국 (FDA) | 510(k) / De Novo / PMA | 부분 호환 | Predicate 비교, SE 논증 별도 |
| 일본 (PMDA) | STED 형식 직접 채택 | 완전 채택 | 일본어 번역 요구 |
| 캐나다 (Health Canada) | STED 형식 채택 | 완전 채택 | 영어/불어 |

## 7. MFDS 기술문서 심사 별표 양식 상세

### 7.1 의료기기법 시행규칙 별표 기반 기술문서 구성

의료기기법 시행규칙 별표에 따른 기술문서 심사자료 제출 양식을 아래와 같이 상세화한다.

| 별표 양식 항목 | 제출 내용 | 자사 적용 (X-ray 시스템) | 해당 STED 섹션 |
|---------------|-----------|------------------------|---------------|
| 1. 기기 개요 | 명칭, 모델, 분류, 의도된 사용목적, 작동원리 | 시스템 사양서, 모델 목록, 방사선 발생장치 사양 | STED §1 |
| 2. 원재료 | 원재료 목록, 생체적합성 해당 시 시험성적 | BOM (디텍터 섬광체, 하우징 재질 등) | STED §2 |
| 3. 제조공정 | 공정 흐름도, 주요 공정 설명, 밸리데이션 | SOP-MFG-001, 공정밸리데이션 보고서 | STED §2 |
| 4. 사용목적 | 적응증, 대상 환자군, 사용 환경, 사용자 자격 | IFU, 기기 개요서 (진단용 X-ray 촬영) | STED §1 |
| 5. 시험검사 기록 | 안전성·유효성 시험성적서 | IEC 60601-1, IEC 60601-2-54, EMC, 방사선 시험 | STED §4 |
| 6. 임상시험 자료 | 임상시험 결과 또는 문헌적 동등성 입증 | CER (문헌 기반 동등성 평가) | STED §6 |
| 7. 표시 기재사항 | 라벨, 포장, IFU | 한글 라벨·IFU, 방사선 경고 표시 | STED §7 |
| 8. 위험분석 | ISO 14971 기반 위험관리 | RMF, FMEA, FTA, 방사선 위험 평가 | STED §3 |
| 9. SW 밸리데이션 | IEC 62304 산출물 (Class B/C) | SW 개발계획, 아키텍처, V&V 보고서 | STED §5 |
| 10. 전기·기계 안전성 | IEC 60601-1 적합성 | 전기안전 시험성적서, 기계적 안전성 평가 | STED §4 |
| 11. 생물학적 안전성 | ISO 10993 해당 시 | 환자 접촉부 재질 평가 (해당 시) | STED §4 |
| 12. 방사선 안전성 | 선량 평가, 차폐 시험 | 방사선 출력 시험, HVL, DAP, 누설선량 | STED §4 |
| 13. 전자파 적합성 | IEC 60601-1-2 EMC | EMC 시험성적서 (방출·내성) | STED §4 |
| 14. 사이버보안 | IEC 81001-5-1, MFDS 가이던스 | SBOM, 위협모델링, Pen-test, 취약점 관리 | STED §5 |

### 7.2 MFDS 기술문서 제출 시 유의사항

| 항목 | 요구사항 | 자사 대응 |
|------|----------|-----------|
| 언어 | 한글 작성 원칙 (원문 첨부 가능) | 핵심 문서 한글 번역본 준비, 시험성적서 원문 첨부 |
| 전자 제출 | 의료기기전자민원시스템(eMEDIAS) 활용 | RA가 eMEDIAS 제출 담당 |
| 기술문서 갱신 | 허가·인증 사항 변경 시 변경 기술문서 제출 | SOP-CC-001 연계, 변경 영향 평가 후 제출 |
| 방사선 관련 | 진단용 방사선 발생장치 안전관리규칙 준수 | 별도 안전성 시험 성적서 (kVp, mAs, HVL 등) |
| SW 등급 분류 | MFDS SW 분류 가이던스 적용 | IEC 62304 Safety Class ↔ MFDS 등급 매핑 문서화 |

## 8. EU MDR Annex II 기술문서 상세 매핑

### 8.1 Annex II 전체 섹션 매핑

| Annex II 섹션 | 내용 | 자사 문서 매핑 | 담당 |
|---------------|------|---------------|------|
| §1 제품 설명·사양 | UDI, 모델, 구성, 액세서리, 이전 세대 | DMR 사양서 + SOP-UDI-001 | RA/설계 |
| §2 제조자 정보 | 설계·제조 사이트, 핵심 공급자 | 품질매뉴얼, ASL | QA |
| §3 설계·제조 정보 | 설계이력, 공정 밸리데이션 | DHF + SOP-MFG-001/002 | 설계/제조 |
| §4 GSPR 적합성 | Annex I 23개 GSPR 체크리스트 | GSPR_체크리스트_v0.2 | RA |
| §5 편익-위험 분석·위험관리 | ISO 14971 RMF, B/R 분석 | RMF, B/R 분석서 | RA/설계 |
| §6.1 제품 검증·확인 (전임상) | 전기안전, EMC, 성능, 방사선 시험 | 05_검사 시험 문서 | QA/설계 |
| §6.2 임상평가 | CER, PMCF | 임상평가보고서, PMCF 프로토콜 | RA |
| §6.2(c) 사용적합성 | UEF (IEC 62366-1) | UEF 산출물 | 설계/HFE |
| Annex III PMS 계획 | PMS/PMCF 계획 | PMS 계획서, PSUR | RA/QA |

## 9. FDA QMSR 2026 전환 반영 — MDF 관리 변경점

### 9.1 QMSR 전환 개요

2026-02-02부터 21 CFR Part 820이 QMSR로 전환되어 ISO 13485:2016이 참조편입(Incorporation by Reference)되었다. 이에 따라 MDF 관리에 아래 변경점을 반영한다.

### 9.2 MDF 관리 변경 매트릭스

| 변경 항목 | 이전 (QSR) | 현행 (QMSR) | 자사 대응 |
|-----------|------------|-------------|-----------|
| 문서통제 근거 | 21 CFR 820.40 | ISO 13485 4.2.4 참조편입 | SOP-DOC-001에 ISO 13485 4.2.4 조항 매핑 |
| 기록통제 근거 | 21 CFR 820.184 | ISO 13485 4.2.5 + §820.35 추가요건 | §820.35(a)~(d) 추가 요건 별도 섹션 |
| DMR 정의 | 21 CFR 820.181 | ISO 13485 4.2.3 MDF 개념으로 전환 | MDF 내 DMR 섹션 유지, ISO 용어 병기 |
| DHR 정의 | 21 CFR 820.184 | ISO 13485 7.5.1 생산기록과 통합 | DHR 양식에 ISO 조항 참조 추가 |
| 설계이력파일 | 21 CFR 820.30(j) | ISO 13485 7.3.10 설계개발파일 | DHF 구조 유지, 조항 번호 갱신 |
| 내부감사 기록 | §820.180(c) 비공개 | 비공개 예외 폐지 — FDA 열람 가능 | 감사보고서 품질 상향, 객관적 증거 기재 |
| 경영검토 기록 | §820.180(c) 비공개 | 비공개 예외 폐지 — FDA 열람 가능 | 경영검토 의사록 작성 기준 강화 |
| 전자기록 | 21 CFR Part 11 | 21 CFR Part 11 유지 (§820.35 외부 독립 Part) | eDMS Part 11 적합성 재검증 — predicate rule 기반 적용성 평가 |

### 9.3 §820.35 추가 요건 대응 (v0.3 정정 — eCFR 1차 재확인 [audit #915])

| §820.35 항 | 정식 명칭 (eCFR) | 요구사항 | MDF 반영 방법 |
|------------|------------------|----------|-------------|
| (a) | Records of complaints (불만 기록) | 21 CFR Part 820 Subpart M에 따른 7항목(기기명·접수일·UDI/UPC·제기자·내용·조사/시정·회신) 기록 | PMS 기록 섹션에 SOP-PMS-001 결정 트리·F-QMSR-REC-001 7항목 매핑 |
| (b) | Records of servicing activities (서비스 활동 기록) | 6항목(기기명·UDI/UPC·일자·수행자·내용·시험/검사 데이터) 기록 | 서비스 SOP·X-ray 출장정비 기록 양식 6항목 도입 |
| (c) | Unique Device Identification (UDI 기록) | 21 CFR Part 830에 따른 UDI 발급·DI/PI 변경이력·GUDID 제출 기록 | SOP-UDI-001 연계, UDI 마스터 포함 |
| (d) | Confidentiality (기밀성) | FDA 송수신 기록 공개 판단 보조 — 영업비밀/FOIA 처리 | 기밀 등급 라벨 체계 적용, "Confidential — Contains Trade Secrets" 헤더 |

> v0.2에서 (a)=MDR 기록·(b)=UDI·(c)=기밀성·(d)=전자서명(Part 11)으로 기재했던 매핑은 eCFR 본문과 불일치하는 사실오류였음. **21 CFR Part 11은 §820.35의 하위항목이 아닌 독립 Part**이며, Part 11 적용성은 §9.4(외부 절)에서 별도 다룸 — 정정 [audit #915].

## 10. 전자문서관리시스템(eDMS) 요건

### 10.1 21 CFR Part 11 요건

| Part 11 조항 | 요구사항 | eDMS 구현 요건 |
|-------------|----------|---------------|
| §11.10(a) | 시스템 밸리데이션 | eDMS IQ/OQ/PQ 수행, 밸리데이션 보고서 유지 |
| §11.10(b) | 정확하고 완전한 사본 생성 | PDF/A 형식 출력·백업, 원본 동일성 검증 |
| §11.10(c) | 기록 보호 (보존 기간) | 암호화 보관, 보존 기간 자동 관리 |
| §11.10(d) | 시스템 접근 제한 | 역할 기반 접근제어 (RBAC), 계정 관리 SOP |
| §11.10(e) | 감사 추적 (Audit Trail) | 변경 이력 자동 기록 (Who, What, When, Why) |
| §11.10(g) | 권한 확인 | 전자서명 전 사용자 인증 (ID + 암호) |
| §11.10(k)(1) | 문서 유효성 기간 관리 | 유효판/폐지판 자동 상태 관리 |
| §11.50 | 전자서명 표시 | 서명자 이름, 일시, 서명 의미 표시 |
| §11.70 | 전자서명-기록 연결 | 서명과 기록의 변경 불가 결합 |
| §11.100 | 전자서명 통제 | 개인별 고유 서명, 재사용 금지 |
| §11.200 | 전자서명 구성요소 | 비생체 서명: ID + 암호 조합 |
| §11.300 | 식별코드·암호 통제 | 암호 복잡도, 주기적 변경, 실패 잠금 |

### 10.2 EU MDR Annex II 전자기록 요건

| 요건 | 내용 | eDMS 구현 |
|------|------|----------|
| 기술문서 가용성 | NB 및 관할당국 요청 시 즉시 열람 가능 | 클라우드/온프레미스 24시간 접근 보장 |
| 기술문서 언어 | EU 공용 언어 (통상 영어) | 영문본 eDMS 등록, 원본 동일성 관리 |
| 변경 추적성 | 기술문서 변경 이력 완전 추적 | Audit Trail + 버전 관리 |
| 보존 기간 | 최종 제품 시판 후 최소 10년 (임플란트 15년) | 자동 보존 기간 계산 및 알림 |
| 전자서명 유효성 | eIDAS 규정 준거 또는 동등 수준 | 적격 전자서명 또는 검증된 전자서명 적용 |

### 10.3 eDMS 운영 요건 요약

| 구분 | 요건 | 점검 주기 |
|------|------|-----------|
| 접근 통제 | RBAC (작성/검토/승인/읽기전용), 부서별 권한 분리 | 반기 1회 |
| 감사 추적 | 모든 CRUD 작업 자동 기록, 변경 사유 필수 입력 | 상시 (시스템) |
| 백업·복구 | 일일 증분 백업, 주간 전체 백업, RPO 24h / RTO 4h | 월 1회 복구 시험 |
| 밸리데이션 | 초기 IQ/OQ/PQ + 주요 업그레이드 시 재밸리데이션 | 업그레이드 시 |
| 전자서명 | 2-Factor (ID + Password), 서명 의미 표시 | 연 1회 |
| 보존 관리 | 제품별 보존 기간 자동 계산, 만료 알림 | 분기 1회 |
| 교육 | eDMS 사용자 교육, Part 11 인식 교육 | 연 1회 |

## 11. 기술문서 갱신 트리거 의사결정 플로우차트

### 11.1 갱신 트리거 이벤트

| 트리거 유형 | 세부 이벤트 | 영향 범위 | 긴급도 |
|------------|-----------|-----------|--------|
| 설계 변경 | HW/SW/기구 설계 변경 (SOP-CC-001) | DHF, DMR, 규제 제출물 | 변경 등급에 따름 |
| 공정 변경 | 제조공정·설비·환경 변경 | DMR, DHR 양식 | 변경 등급에 따름 |
| 규제 변경 | 법규·표준 개정, 가이던스 변경 | MDF 전체 | 유예기간 내 |
| 부작용/CAPA | 부작용 보고, 시정조치 완료 | RMF, 임상평가, PMS | 즉시~30일 |
| 정기 검토 | 연간 기술문서 정기 검토 | MDF 전체 | 계획 |
| 공급자 변경 | 핵심 부품·원재료 공급자 변경 | DMR, DHF(해당 시) | 변경 등급에 따름 |
| 임상 데이터 | 신규 임상 데이터, PMCF 결과 | CER, RMF | 분기/연간 |
| 사이버보안 | 취약점 발견, SBOM 변경, 패치 | 사이버보안 파일, SW 문서 | 즉시~90일 |

### 11.2 갱신 의사결정 플로우차트

```
┌──────────────────────────────────────────────────────────────────┐
│             기술문서 갱신 의사결정 플로우차트                       │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  [이벤트 발생]                                                   │
│       │                                                          │
│       ▼                                                          │
│  ┌─────────────────────────┐                                     │
│  │ 1. 트리거 유형 식별      │                                     │
│  │ (설계/공정/규제/부작용    │                                     │
│  │  /정기/공급자/임상/보안)  │                                     │
│  └────────┬────────────────┘                                     │
│           ▼                                                      │
│  ┌─────────────────────────┐    아니오    ┌──────────────────┐   │
│  │ 2. 안전성·유효성 영향?   │ ──────────→ │ Minor 변경 처리   │   │
│  │ (환자 선량, 영상품질,    │              │ - 문서 개정만     │   │
│  │  SW 안전 클래스 등)      │              │ - 규제 통지 불요  │   │
│  └────────┬────────────────┘              └──────────────────┘   │
│           │ 예                                                   │
│           ▼                                                      │
│  ┌─────────────────────────┐                                     │
│  │ 3. 변경영향평가 (CIA)    │                                     │
│  │ - SOP-CC-001 적용       │                                     │
│  │ - 위험관리 재평가       │                                     │
│  │ - 규제 영향 분석        │                                     │
│  └────────┬────────────────┘                                     │
│           ▼                                                      │
│  ┌─────────────────────────┐                                     │
│  │ 4. 갱신 대상 문서 식별   │                                     │
│  │ - DHF □  DMR □  DHR □   │                                     │
│  │ - RMF □  UEF □          │                                     │
│  │ - CER □  SBOM □         │                                     │
│  │ - 규제 제출물 □         │                                     │
│  └────────┬────────────────┘                                     │
│           ▼                                                      │
│  ┌─────────────────────────┐    예     ┌──────────────────────┐  │
│  │ 5. 규제 통지/변경 필요?  │ ───────→ │ 6a. 시장별 통지      │  │
│  │ - MFDS 변경허가/신고    │           │ - MFDS: 변경허가     │  │
│  │ - EU: NB 통지           │           │ - EU: NB 심사        │  │
│  │ - FDA: Special 510(k)   │           │ - FDA: 510(k) 재제출 │  │
│  └────────┬────────────────┘           └──────────┬───────────┘  │
│           │ 아니오                                 │              │
│           ▼                                       ▼              │
│  ┌─────────────────────────┐  ┌──────────────────────────────┐  │
│  │ 6b. 내부 갱신 수행      │  │ 7. 제출물 작성·제출          │  │
│  │ - 문서 개정             │  │ - 변경 기술문서 패키지       │  │
│  │ - 이력 기록             │  │ - 규제 기관 제출             │  │
│  │ - 교육 실시             │  │ - 승인 대기                  │  │
│  └────────┬────────────────┘  └──────────┬───────────────────┘  │
│           │                              │                       │
│           ▼                              ▼                       │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ 8. F-TD-002 MDF 완전성 검증 체크리스트 수행              │    │
│  │ - 갱신 문서 완결성 확인                                  │    │
│  │ - 교차 참조 정합성 확인                                  │    │
│  │ - RA/QA 승인                                            │    │
│  └──────────────────────────────────────────────────────────┘    │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

## 12. F-TD-002 MDF 완전성 검증 체크리스트

### 12.1 목적

MDF (Medical Device File) 구성 문서의 완전성을 EU MDR Annex II 전 섹션, MFDS 별표 양식, FDA QMSR 요건에 대해 체계적으로 점검한다.

### 12.2 체크리스트 사용 시점

- 인허가 제출 전 최종 점검
- 기술문서 정기 검토 (연 1회)
- 주요 설계 변경 완료 후
- NB 심사, MFDS 심사, FDA 검사 대비

### 12.3 EU MDR Annex II 섹션별 점검항목

#### A. 제품 설명 및 사양 (Annex II §1)

| No. | 점검 항목 | 확인 기준 | Y/N/NA | 비고 |
|-----|-----------|-----------|--------|------|
| 1.1 | 제품명·모델명·변형 목록 | UDI-DI와 일치 확인 | | |
| 1.2 | 의도된 목적(Intended Purpose) | IFU, 라벨, CER과 일관성 | | |
| 1.3 | 의도된 사용자·환자군 | UEF Use Specification 일치 | | |
| 1.4 | 작동 원리 설명 | X-ray 발생·검출·영상처리 기술 | | |
| 1.5 | 액세서리·조합기기 목록 | 호환성 시험 증거 | | |
| 1.6 | 이전 세대·유사 기기 설명 | 동등성 평가 근거 (CER) | | |
| 1.7 | UDI-DI / Basic UDI-DI | EUDAMED 등록 확인 | | |

#### B. 제조자 정보 (Annex II §2)

| No. | 점검 항목 | 확인 기준 | Y/N/NA | 비고 |
|-----|-----------|-----------|--------|------|
| 2.1 | 제조사 명칭·주소·SRN | EUDAMED 등록 확인 | | |
| 2.2 | 수권대리인 정보 (해당 시) | EU 수권대리인 계약서 | | |
| 2.3 | 설계·제조 사이트 목록 | ISO 13485 인증 범위 일치 | | |
| 2.4 | 핵심 공급자 목록 (해당 시) | ASL 최신 상태 | | |

#### C. 설계·제조 정보 (Annex II §3)

| No. | 점검 항목 | 확인 기준 | Y/N/NA | 비고 |
|-----|-----------|-----------|--------|------|
| 3.1 | 설계 단계별 산출물 | DHF 완결 (입력→출력→검증→확인→이전) | | |
| 3.2 | 제조공정 개요 | SOP-MFG-001 유효판 참조 | | |
| 3.3 | 공정 밸리데이션 현황 | IQ/OQ/PQ 완료, 유효기간 내 | | |
| 3.4 | 핵심 공급자 관리 증거 | 공급자 감사·재평가 기록 | | |
| 3.5 | 조립·검사 작업지침서 | WI 시리즈 유효판 | | |

#### D. GSPR 적합성 (Annex II §4)

| No. | 점검 항목 | 확인 기준 | Y/N/NA | 비고 |
|-----|-----------|-----------|--------|------|
| 4.1 | GSPR 체크리스트 작성 완료 | 23개 요구사항 전수 대응 | | |
| 4.2 | 적용 표준 최신판 확인 | OJEU 등재 표준 현행판 | | |
| 4.3 | 비적용(NA) 항목 사유 기재 | 정당한 근거 문서화 | | |
| 4.4 | 객관적 증거 위치 명기 | 시험보고서·문서번호 기재 | | |

#### E. 편익-위험 분석·위험관리 (Annex II §5)

| No. | 점검 항목 | 확인 기준 | Y/N/NA | 비고 |
|-----|-----------|-----------|--------|------|
| 5.1 | 위험관리계획(RMP) 승인 | ISO 14971 요건 충족 | | |
| 5.2 | 위험분석 (FMEA/FTA) 완료 | 식별된 위험 전수 평가 | | |
| 5.3 | 위험통제 조치 검증 | 통제 조치 유효성 확인 | | |
| 5.4 | 잔여위험 수용성 판정 | 수용 기준 대비 합격 | | |
| 5.5 | 편익-위험 분석 보고서 | 전체 잔여위험 대비 편익 우위 | | |
| 5.6 | 방사선 위험 특별 평가 | ALARA 원칙 적용 증거 | | |

#### F. 제품 검증·확인 (Annex II §6)

| No. | 점검 항목 | 확인 기준 | Y/N/NA | 비고 |
|-----|-----------|-----------|--------|------|
| 6.1 | 전기안전 시험 (IEC 60601-1) | 공인시험성적서 유효 | | |
| 6.2 | 방사선 성능 (IEC 60601-2-54) | 형식시험 체크리스트 완료 | | |
| 6.3 | EMC 시험 (IEC 60601-1-2) | 공인시험성적서 유효 | | |
| 6.4 | SW 밸리데이션 (IEC 62304) | SW V&V 보고서, 아키텍처 | | |
| 6.5 | 사이버보안 (IEC 81001-5-1) | SBOM, 위협모델, Pen-test | | |
| 6.6 | 사용적합성 (IEC 62366-1) | UEF: Summative 평가 완료 | | |
| 6.7 | 임상평가보고서 (CER) | Art. 61 요건 충족 | | |
| 6.8 | 생체적합성 (해당 시) | ISO 10993 평가 | | |

#### G. 라벨링 (Annex II §1 관련)

| No. | 점검 항목 | 확인 기준 | Y/N/NA | 비고 |
|-----|-----------|-----------|--------|------|
| 7.1 | 라벨 ISO 15223-1 기호 적용 | 필수 기호 전수 확인 | | |
| 7.2 | IFU 내용 완전성 | ISO 20417 요건 대비 | | |
| 7.3 | UDI 바코드 라벨 | GS1/HIBCC 형식, 스캔 검증 | | |
| 7.4 | 방사선 경고 표시 | IEC 60601-2-54 요구 기호 | | |
| 7.5 | 다시장 언어 요건 | EU: 현지 언어, 한국: 한글 | | |

#### H. PMS 및 PMCF (Annex III)

| No. | 점검 항목 | 확인 기준 | Y/N/NA | 비고 |
|-----|-----------|-----------|--------|------|
| 8.1 | PMS 계획서 승인 | Annex III 요건 포함 | | |
| 8.2 | PSUR 작성 (해당 시) | Class IIa 이상: 최소 2년 주기 | | |
| 8.3 | PMCF 계획 (해당 시) | Art. 61(11) 요건 | | |
| 8.4 | 불만·부작용 처리 기록 | SOP-PMS-001 연계 | | |

### 12.4 FDA QMSR 추가 점검항목

| No. | 점검 항목 | 확인 기준 | Y/N/NA | 비고 |
|-----|-----------|-----------|--------|------|
| F.1 | MDF 구성 (ISO 13485 4.2.3) | 제품별 규제 요건 매핑 완료 | | |
| F.2 | §820.35(a) Records of complaints | 불만 7항목(기기명·접수일·UDI·제기자·내용·조사/시정·회신) 기록 완결 | | |
| F.3 | §820.35(b) Records of servicing activities | 서비스 6항목(기기명·UDI·일자·수행자·내용·시험데이터) 기록 완결 | | |
| F.3-1 | §820.35(c) UDI 기록 | GUDID 제출·DI/PI 변경이력 완결 | | |
| F.3-2 | §820.35(d) Confidentiality | FDA 송수신 기록 기밀 분류 체계 운영 | | |
| F.4 | 21 CFR Part 11 적합 (§820.35 외부) | predicate rule 적용성 평가·eDMS 밸리데이션 현행 유효 | | |
| F.5 | 내부감사 기록 열람 대비 | 객관적 증거 기재 수준 | | |
| F.6 | 510(k) Summary/SE 보고서 | 최신 Predicate 비교 유효 | | |

### 12.5 MFDS 추가 점검항목

| No. | 점검 항목 | 확인 기준 | Y/N/NA | 비고 |
|-----|-----------|-----------|--------|------|
| M.1 | 별표 양식 전 항목 작성 | §7.1 양식 항목 대비 완결 | | |
| M.2 | 한글 기술문서 준비 | 핵심 문서 한글 번역 완료 | | |
| M.3 | 방사선 안전관리규칙 준수 | 안전성 시험 성적서 유효 | | |
| M.4 | SW 등급 분류 문서 | MFDS 가이던스 대비 분류 | | |
| M.5 | eMEDIAS 제출 패키지 | 전자 제출 형식 적합 | | |

## 13. 기술문서 정기 검토

### 13.1 정기 검토 일정

| 검토 주기 | 대상 | 책임자 | 산출물 |
|-----------|------|--------|--------|
| 분기 1회 | 규제·표준 개정 모니터링 | RA | 규제 변경 영향 평가서 |
| 반기 1회 | DMR/DHR 정합성 점검 | QA | 점검 보고서 |
| 연 1회 | MDF 전체 정기 검토 (F-TD-002 수행) | RA + QA | MDF 검토 보고서 |
| 수시 | 설계 변경·부작용 발생 시 | 해당 부서 + RA | 갱신 기록 |

### 13.2 정기 검토 점검 항목

| 점검 사항 | 확인 방법 | 판정 기준 |
|-----------|-----------|-----------|
| 적용 표준 최신성 | 외부문서 관리대장 대비 현행판 확인 | 최신판 적용 또는 전환 계획 수립 |
| 임상 데이터 유효성 | CER 최신 문헌 검색 수행 여부 | 연 1회 이상 문헌 업데이트 |
| PMS 데이터 반영 | 불만·부작용·시장 데이터 기술문서 반영 | 미반영 항목 없음 |
| 위험관리 최신성 | RMF 잔여위험 재평가 | 신규 위험 식별·평가 완료 |
| UDI 정보 정확성 | GUDID/EUDAMED/국내 UDI DB 일치 | 불일치 항목 없음 |
| 라벨링 현행성 | 승인 라벨 vs 생산 라벨 일치 | 불일치 시 즉시 시정 |

## 14. 보존 기간

| 기록 유형 | 최소 보존 기간 | 근거 |
|-----------|--------------|------|
| MDF / DHF | 제품 수명 + 최소 2년 (EU: 시판 후 최소 10년) | ISO 13485 4.2.5, EU MDR Art. 10(8) |
| DMR | 제품 수명 + 최소 2년 | ISO 13485 4.2.3 |
| DHR | 제품 수명 + 최소 2년 | ISO 13485 7.5.1, §820.35 |
| RMF | 제품 수명 + 최소 2년 | ISO 14971 |
| UEF | 제품 수명 + 최소 2년 | IEC 62366-1 |
| 규제 제출물 사본 | 인허가 유효 기간 + 5년 | 각 규제기관 요구 |
| PMS 기록 | 5년 이상 | FDA 21 CFR 803, EU MDR |
| 사이버보안 파일 | SW 수명 + 최소 2년 | IEC 81001-5-1 |
| eDMS 감사추적 로그 | 해당 기록 보존 기간과 동일 | 21 CFR Part 11 §11.10(e) |

## 15. 기밀 등급 관리

| 등급 | 정의 | 접근 범위 | 표시 방법 |
|------|------|-----------|-----------|
| Confidential | 규제 제출물, 인허가 서신, 영업비밀 | RA 팀장 + 경영진 | 문서 상단 "CONFIDENTIAL" 표시 |
| Restricted | DHF, RMF, 시험보고서, 감사 기록 | 관련 부서 + QA/RA | 문서 상단 "RESTRICTED" 표시 |
| Internal | DMR, SOP, 작업지침서 | 전사 임직원 | 문서 상단 "INTERNAL" 표시 |
| Public | 라벨, IFU, SSCP | 제한 없음 | 별도 표시 없음 |

## 16. 교차참조

| 참조 문서 | 연계 내용 |
|-----------|-----------|
| 06_문서/문서_기록관리_개요 | 문서 계층, 문서통제 기본 절차, 보존 기간 |
| 02_QMS/SOP-CC-001 | 설계·공정·문서 변경 시 변경통제 절차 |
| 06_문서/SOP-UDI-001 | UDI 부여·등록·변경 관리 |
| 01_법규/GSPR_체크리스트_v0.2 | Annex II §4 GSPR 매핑 |
| 01_법규/FDA_QMSR_2026 | QMSR 전환 상세 |
| 01_법규/FDA_QMSR_820.35_vs_ISO13485_4.2.5 | §820.35 추가 요건 대비표 |
| 03_설계/IEC_62304_SW_수명주기 | SW 기술문서 산출물 |
| 03_설계/IEC_81001-5-1_FDA_Cybersecurity_SW보안 | 사이버보안 문서 요건 |
| 05_검사/IEC60601-2-54_형식시험_체크리스트 | 방사선 성능 시험 체크리스트 |
| 07_위험관리/ISO14971_프로세스_상세 | RMF 구성·관리 |
| 08_PMS/SOP-PMS-001 | PMS 기록 → MDF 연계 |
| 12_교차검증/벤치마크_2026-Q2_K243734 | Special 510(k) Reference Device 3건 패턴·DQE/MTF/Sensitivity 정량 |
| 12_교차검증/벤치마크_2026-Q2_K250211 | Multi-predicate 4건·다중 UI 변형 패턴 |
| 12_교차검증/벤치마크_2026-Q2_K243171 | 단일 510(k) 8개 모델(CsI×GOS×Glass×Non-Glass×Wireless/Wired) |
| 13_규제평가/FDA_510k_RTA | Section C1 Non-clinical Bench Performance·SE 비교 매트릭스 RTA 충족 |

## 17. 관련 양식 목록

| 양식 번호 | 양식명 | 용도 |
|-----------|--------|------|
| F-TD-001 | MDF 목차·구성 체크시트 | MDF 초기 구성 시 필수 문서 체크 |
| F-TD-002 | MDF 완전성 검증 체크리스트 | 인허가 제출 전·정기 검토 시 (본 문서 §12) |
| F-TD-003 | 기술문서 갱신 이력 로그 | 갱신 트리거·변경 내용·승인 기록 |
| F-TD-004 | eDMS 접근권한 신청·변경서 | eDMS 사용자 권한 관리 |
| F-TD-005 | SE 비교 매트릭스(Substantial Equivalence Matrix) | 510(k) Predicate×Model variant N:M 비교표·SE 결론문(본 문서 §18) |
| F-DOC-001 | 문서관리대장 | 문서_기록관리_개요 §10 참조 |
| F-DOC-002 | 외부문서 관리대장 | 문서_기록관리_개요 §11 참조 |


## 18. N:M Substantial Equivalence 비교 매트릭스 양식 [v0.4 신설, plan #934]

### 18.1 목적·적용 범위

본 §은 FDA 510(k) Premarket Notification(21 CFR 807 Subpart E)·Special 510(k)·De Novo 제출 시 Substantial Equivalence(SE) 입증을 위한 **N:M(N predicate × M model variant) 비교 매트릭스 양식**을 정의한다. 적용 제품군은 자사 디지털 X-ray Flat Panel Detector(FPD) 및 X-ray System(Product Code MQB, 21 CFR 892.1680)으로 한다. 본 §은 양식·작성 안내만 제공하며, 실제 비교값은 제품별 510(k) dossier 작성 시 F-TD-005에 채운다.

### 18.2 Predicate vs Reference Device 구분

FDA 510(k) Program Guidance(2014-07-28)·SSXI Guidance(2016-09-01) 기준 용어를 다음과 같이 구분한다.

| 구분 | FDA 정의(요지) | 자사 매트릭스 적용 |
|------|---------------|------------------|
| **Predicate device** | 동일한 의도된 사용(intended use)을 가진 합법적 시판 기기. SE 입증의 직접 근거. (FDA 510(k) Program Guidance 2014, §6) | §18.3 Predicate columns(최대 5건 동시 비교) |
| **Reference device** | Predicate가 아니며, **과학적 방법론·표준 기준값·시험 방법** 등을 보조 지원하는 합법적 시판 기기. SE 단독 근거로 사용 불가. (FDA 510(k) Program Guidance 2014, §7) | §18.4 Reference columns(별도 표) |

> 주: Multi-predicate(>1)는 동일 의도된 사용 전제 하에 기술적 특성의 일부씩을 각각의 predicate에 매칭하는 패턴이며, FDA에서 명시적으로 허용한다(FDA Guidance §6). 자사는 최대 5건 동시 비교 셀을 양식 한도로 한다.

### 18.3 §SE-1 Predicate 비교 매트릭스 (N predicate × M model variant)

비교축은 **Model variant Row × Predicate Column**으로 구성하며, **Model variant**는 다음 3차원의 cross-product로 정의한다.

| 차원 | 값 |
|------|-----|
| Scintillator | CsI / GOS |
| Substrate | Glass / Non-Glass PET |
| Portability | Wireless / Wired / Non-portable |

> Cross-product 최대 조합 수 = 2 × 2 × 3 = **12 model variants**. 단일 510(k)에서 실제로 등록할 변형 수는 RA 전략에 따라 부분 집합을 선택한다(자사 표 한도 12 row).

**비교 매트릭스 표(공란 양식, 채움은 F-TD-005)**

| Model Variant ID | Scintillator | Substrate | Portability | Subject Device 값 | Predicate-1 (K#####) | Predicate-2 (K#####) | Predicate-3 (K#####) | Predicate-4 (K#####) | Predicate-5 (K#####) | SE 판정 |
|---|---|---|---|---|---|---|---|---|---|---|
| MV-01 | CsI | Glass | Wireless | | | | | | | |
| MV-02 | CsI | Glass | Wired | | | | | | | |
| MV-03 | CsI | Glass | Non-portable | | | | | | | |
| MV-04 | CsI | Non-Glass PET | Wireless | | | | | | | |
| MV-05 | CsI | Non-Glass PET | Wired | | | | | | | |
| MV-06 | CsI | Non-Glass PET | Non-portable | | | | | | | |
| MV-07 | GOS | Glass | Wireless | | | | | | | |
| MV-08 | GOS | Glass | Wired | | | | | | | |
| MV-09 | GOS | Glass | Non-portable | | | | | | | |
| MV-10 | GOS | Non-Glass PET | Wireless | | | | | | | |
| MV-11 | GOS | Non-Glass PET | Wired | | | | | | | |
| MV-12 | GOS | Non-Glass PET | Non-portable | | | | | | | |

비교 대상 기술적 특성(rows 내 Subject/Predicate 셀에 채울 항목)은 다음과 같다(SSXI Guidance 2016-09-01 §VII 항목 + K243171/K250211/K243734 벤치마크 공통 항목).

| 분류 | 비교 항목 |
|------|----------|
| 의도된 사용 | Indications for Use, Contraindications, Patient population, Use environment |
| 디텍터 코어 | Scintillator type/thickness(μm), Substrate, Pixel pitch(μm), Pixel matrix, Active area(cm), A/D bit depth |
| 영상 성능 | DQE(0.5/1/2 lp/mm), MTF(0.5/1/2 lp/mm), Sensitivity(LSB/μGy), Resolution(lp/mm), Dynamic range, Lag |
| 인터페이스 | Wired interface(Gigabit Ethernet 등), Wireless interface(Wi-Fi 802.11ac/ax 등), Tethering |
| 전원 | Battery type/capacity, AC adapter, Charger |
| 환경 | Operating temp/humidity, IP rating, Drop/load-bearing |
| SW | SW Level of Concern(Basic/Moderate/Major), OTS components, Cybersecurity controls |
| Biocompat | Patient-contact materials, ISO 10993 결과 |
| Accessories | Battery, Cable, Adapter, Dongle, Charger, Software apps |

### 18.4 §SE-2 Reference Device 표 (Predicate와 분리)

Reference device는 **SE 단독 근거가 아니며, 과학적 방법론·표준 기준값을 보조**한다(FDA 510(k) Program Guidance 2014, §7). 자사 양식에서는 Predicate 표와 **물리적으로 분리된 별도 표**로 작성한다.

| Reference ID | K-Number | 신청인/Trade Name | 인용 목적(예: scintillator 두께 표준값·DQE 측정 방법론) | 적용 모델 변형 | SE 단독 근거 사용 여부 |
|---|---|---|---|---|---|
| REF-01 | | | | | **불가**(고정) |
| REF-02 | | | | | **불가**(고정) |
| REF-03 | | | | | **불가**(고정) |

> SSXI 디텍터의 reference device 적용 예: K243734(Allengers, Special 510k)는 K201528/K210988/K220510(InnoCare) 3건을 reference로 인용. K201528 등은 동일 신청인의 predicate가 아니며 scintillator 두께·DQE 표준값 보조용. (BMK-2026Q2-K243734 §1·§3)

### 18.5 §SE-3 적합성 표준 일괄 매핑 양식

K243734/K250211/K243171 3건 벤치마크 공통 표준 패턴이며, SE 매트릭스와 함께 510(k) §VII Performance Data에 일괄 매핑한다.

| 분류 | 표준·가이던스 | 적용 부위 | 자사 산출물 |
|------|--------------|----------|------------|
| 전기안전 | AAMI/ANSI ES60601-1 (FDA Recognized Consensus Standard — 판본은 X-ray 표준매핑 v0.4 참조) | 시스템·디텍터 전기안전 | 전기안전 시험성적서 |
| 일반 안전·성능 | IEC 60601-1 (판본은 X-ray 표준매핑 v0.4 참조) | 시스템·디텍터 일반 안전 | IEC 60601-1 형식시험 보고서 |
| EMC | IEC 60601-1-2 (판본은 X-ray 표준매핑 v0.4 참조) | 방출·내성 | EMC 시험성적서 |
| 사용적합성 | IEC 60601-1-6 + IEC 62366-1:2015+AMD1:2020 | HF/사용적합성 | UEF (IEC_62366-1_계획서) |
| HFE 보조 | ANSI/AAMI HE75 (판본은 X-ray 표준매핑 v0.4 참조) | 일반 HFE 가이드 | UEF 부속 |
| 방사선 성능 | IEC 60601-2-54 Ed.2 (2022-09-26) | X-ray 영상기기 안전·성능 | IEC60601-2-54_형식시험_체크리스트 |
| 영상 성능(DQE) | IEC 62220-1-1 (DQE 측정 방법, 판본은 X-ray 표준매핑 v0.4 참조) | DQE 측정 방법 | DQE 시험 보고서(F-IQ-001 예정, plan #932) |
| 영상 성능(MTF) | IEC 62220-1-3 (MTF 측정 방법, 판본은 X-ray 표준매핑 v0.4 참조) | MTF 측정 방법 | MTF 시험 보고서(F-IQ-001 예정, plan #932) |
| SW 수명주기 | IEC 62304:2006+AMD1:2015 (Ed.1.1) [audit #908/#925 정정 패턴 적용 — 'A2:2020' 미존재 표준 인용 금지] | SW 수명주기 프로세스 | IEC_62304_SW_수명주기 |
| SW 사이버보안 | IEC 81001-5-1:2021 + FDA Final Guidance "Cybersecurity in Medical Devices: Quality Management System Considerations and Content of Premarket Submissions" (**February 2026**, Docket FDA-2021-D-1158; supersedes 2025-06-27 및 2023-09-27 final) | SW 사이버보안 | IEC_81001-5-1_FDA_Cybersecurity_SW보안, SBOM |
| FDA SW | FDA "Content of Premarket Submissions for Device Software Functions" (2023-06-14) | SW 문서 수준 | SW Level of Concern 평가서 |
| FDA SSXI | FDA "Solid State X-ray Imaging Devices 510(k) Guidance" (2016-09-01) | SSXI 510(k) 일반 | 본 §18 + X-ray 표준매핑 |
| 위험관리 | ISO 14971:2019 | 위험관리 프로세스 | RMF, ISO14971_프로세스_상세 |
| 생체적합성 | ISO 10993-1:2018 + 시리즈 | 환자 접촉부 | ISO 10993 시험기록(F 양식 예정, plan #933) |
| 라벨링 | ISO 15223-1:2021, ISO 20417:2021 | 라벨·IFU 기호 | DMR 라벨링 |

### 18.6 §SE-4 Substantial Equivalence 결론문 표준 양식

FDA 510(k) Program Guidance(2014-07-28) §6·§9에 따른 SE 결론은 다음 4요건의 충족 결과를 명시한다.

| SE 요건(2014 Guidance Decision Flow) | 충족 진술 양식 |
|---|---|
| Decision 1 — Predicate 식별 | "The subject device {Trade Name} is being compared to legally marketed predicate device(s) K_____ (Predicate-1)[, K_____ (Predicate-2), …]." |
| Decision 2 — Same intended use | "The subject device has the **same intended use** as the predicate(s) — diagnostic X-ray imaging for {populations}, in {environment}, used by {user qualifications}." |
| Decision 3 — Same technological characteristics? | (Same case) "The subject device has **the same technological characteristics** as the predicate(s)." / (Different case) "The subject device has **different technological characteristics** in the following items: {list}; however, **these differences do not raise different questions of safety and effectiveness** based on §SE-1 comparison and §SE-3 standards-based performance testing." |
| Decision 4/5 — Performance data 입증 | "Performance data demonstrate that the subject device is **as safe and effective** as the predicate(s) — see §SE-3 standards mapping and accompanying test reports (전기안전·EMC·DQE/MTF·SW V&V·cybersecurity·biocompat)." |
| 최종 결론문 | "Therefore, the subject device is **substantially equivalent** to the identified predicate device(s) within the meaning of 21 CFR 807.100(b). The technological differences identified **raise no new/different questions of safety and effectiveness**." |

> 표준 결론문 중 "raise no new/different questions of safety and effectiveness"는 FDA **21 CFR 807.100(b)(2)(ii)(C)** 및 2014 Guidance §6의 표현을 직접 인용한 양식이며, 실제 dossier 작성 시 가감 없이 사용한다. (참고: "as safe and as effective" 표현의 근거는 21 CFR 807.100(b)(2)(ii)(B).) [audit #936]

### 18.7 §SE-5 매트릭스 작성·점검 절차

| 단계 | 수행 | 책임 | 산출물 |
|------|------|------|--------|
| 1. Predicate 후보 검색 | FDA 510(k) Database(accessdata, openFDA) 검색, Product Code(예: MQB)·Regulation(21 CFR 892.1680)·intended use 일치 K-number 후보 5건 이상 추출 | RA Lead | Predicate 후보 long-list |
| 2. Best practice 적용 | FDA **Draft Guidance** "Best Practices for Selecting a Predicate Device" (September 2023, Docket FDA-2023-D-3134, *Not for implementation. Contains non-binding recommendations.*) **권고 사항 참고 평가** (자사 RA 정책으로 Draft 권고 채택): ① 동일 product code ② 최근 SE 결정 ③ 시판 중 ④ recall/safety issue 부재 | RA Lead | Predicate short-list 5건 이하 |
| 3. Reference device 결정 | Scientific methodology·표준 기준값 보조 필요 시 §18.4 별도 표 작성. SE 단독 근거 사용 금지 | RA Lead | Reference list |
| 4. §SE-1 채움 | F-TD-005에 Subject·Predicate 컬럼 정량/정성값 기재. Source 셀에 K-number, Summary 페이지 인용 | RA Lead + 설계 Lead | F-TD-005 작성본 |
| 5. §SE-3 표준 매핑 | §18.5 표 채움. 각 표준에 대응하는 시험성적서·V&V 문서 ID 기재 | QA + 설계 Lead | §SE-3 채움본 |
| 6. §SE-4 결론문 작성 | §18.6 양식에 따라 SE 결론문 작성. Decision 1~5 진술 누락 없음 확인 | RA Lead | SE Conclusion Statement |
| 7. 동반 문서 정합성 점검 | TF-TD-001 §12 F-TD-002 체크리스트 항목 §C/F/F.6 동시 충족 확인. ALARA_지원기능_설계명세·X-ray 표준매핑·IEC_62304_SW_수명주기 cross-ref 유효성 확인 | QA | F-TD-002 통과 기록 |
| 8. PRRC/RA 최종 승인 | EU 동시 신청 시 PRRC 확인 후 510(k) §III/§VI/§VII 패키지 봉인 | PRRC + RA 팀장 | 승인 기록 |

### 18.8 비적용·예외

| 사례 | 처리 |
|------|------|
| De Novo classification 경로 | §18.3 Predicate 컬럼 공란. §SE-4 결론 대신 "De Novo classification request — no predicate, classification rationale separately" 진술 |
| 단일 model variant 단일 predicate(1:1) | §18.3 표는 1 row × 1 predicate column으로 축소. 양식 자체는 동일 |
| Special 510(k)(설계 변경 자기 predicate) | Predicate를 동일 신청인 K-number로 명시. §SE-3 표준은 변경 영향 부위만 갱신 |
| Multi-predicate 5건 초과 | RA Lead 사전 승인 필요. 표 한도 5건 유지하되 별첨 부속표로 분리 |

### 18.9 양식 부적합 시 조치

| 부적합 사례 | 조치 |
|------------|------|
| Subject vs Predicate 정량값 차이 사유 미기재 | §18.5 해당 표준 시험 결과로 보강. 보강 불가 시 De Novo 경로 재평가 |
| Reference device를 SE 단독 근거로 사용한 흔적 | §18.4 표시 위반 — 즉시 정정. RA 팀장 보고 |
| §SE-4 결론문 "different questions" 진술 누락 | dossier 봉인 차단. §18.6 양식 강제 적용 |
| Cross-ref 문서 폐지·갱신 미반영 | SOP-CC-001 변경통제 트리거. F-TD-002 §C/F 재실행 |


## 출처

- ISO 13485:2016 §4.2.3, 4.2.4, 4.2.5, 7.3.10
- EU MDR 2017/745 Annex II, Annex III, Art. 10(8), Art. 15, Art. 32
- FDA QMSR (21 CFR Part 820, 2026-02-02 시행) + §820.35 추가 요건
- 21 CFR Part 11 (전자기록·전자서명)
- IMDRF/GHTF SG1/N071:2012 (STED)
- MFDS 의료기기법 시행규칙 별표 (기술문서 심사자료)
- IEC 62304:2006+A1:2015, IEC 60601-2-54:2022, IEC 81001-5-1:2021
- IEC 62366-1:2015+Amd1:2020, ISO 14971:2019
- 확인일: 2026-05-30 (v0.3 기준)
- FDA "The 510(k) Program: Evaluating Substantial Equivalence in Premarket Notifications [510(k)]" Guidance (2014-07-28) — Decision Flow, Predicate vs Reference 구분, "different questions of safety and effectiveness" 표현
- FDA **Draft Guidance** "Best Practices for Selecting a Predicate Device to Support a Premarket Notification [510(k)] Submission" (**September 2023, Docket FDA-2023-D-3134, Not for implementation. Contains non-binding recommendations**) — 2026-06 시점 미확정 [audit #937]
- FDA "Solid State X-ray Imaging Devices 510(k) Submissions" Guidance (2016-09-01)
- 21 CFR 807.100(b) Determination of Substantial Equivalence
- IEC 62220-1-1:2015 (DQE), IEC 62220-1-3:2008 (MTF), AAMI/ANSI ES60601-1, ANSI/AAMI HE75:2009/R2018
- BMK-2026Q2-K243734 / BMK-2026Q2-K250211 / BMK-2026Q2-K243171 (자사 분기 종합 벤치마크)
- 확인일(v0.4 추가): 2026-06-29
- 확인일(v0.5 audit 정정): 2026-07-02 — eCFR §807.100 (last amended 2026-06-11), FDA Cybersecurity Final Guidance 페이지 (Feb 2026, Docket FDA-2021-D-1158), FDA Best Practices Draft Guidance 페이지 (Docket FDA-2023-D-3134)
