---
doc-id: SOP-SBOM-001
title: SBOM 생성·관리 절차
type: SOP
version: v0.4
status: draft
category: 03_설계_개발관리
purpose: 의료용 X-ray 시스템 SW 구성요소의 SBOM 생성·유지·취약점 관리 절차를 정의
applicable: [ISO 13485:2016 §4.2.4, FDA QMSR §820.180/ISO13485 §4.2.5, FDA Section 524B, FDA Cybersecurity Guidance 2026-02, EU MDR 2017/745 Annex II, EU CRA 2024/2847, IEC 81001-5-1:2021 §7.SR, MFDS 사이버보안 가이드라인, 디지털의료제품법 §16, NTIA SBOM Minimum Elements, CISA CSAF 2.0]
forms: [F-SBOM-001, F-SBOM-002]
related-docs: [SOP-CC-001, SOP-DT-001, SOP-CVD-001, IEC_81001-5-1_FDA_Cybersecurity_SW보안, SOP-VAL-001, IEC_62304_SW_수명주기, SOP-PSUR-001, SOP-FSCA-001, SOP-AIGOV-001]
related-issues: [13, 17]
owner: SW Lead / Security Officer
last-review: 2026-06-28
review-due: 2027-06-08
---

# SBOM 생성·관리 절차 — v0.3

## 1. 목적

의료용 X-ray 시스템(Generator 제어 FW, Detector FW, Workstation SW, AI 추론 엔진 포함)에 탑재·사용되는 모든 소프트웨어 구성요소를 식별·추적하여 FDA Section 524B, MDCG 2019-16, MFDS 사이버보안 가이드라인, 디지털의료제품법 제16조에 부합하는 SBOM을 생성·유지·관리한다.

## 2. 적용 범위

- Generator 제어 펌웨어 (FreeRTOS 기반)
- Detector 제어 펌웨어 및 FPGA 설계 도구
- Workstation OS 및 3rd-party 미들웨어 (Yocto Linux, Qt, DICOM Toolkit 등)
- 영상처리/재구성 SW, AI 추론 모델 런타임 (ONNX Runtime, TensorRT 등)
- 오픈소스 및 상용 라이선스 소프트웨어 전체
- 빌드 도구·CI/CD 파이프라인 구성요소 (빌드 의존성 포함)

## 3. 용어 정의

| 용어 | 정의 |
|------|------|
| SBOM | Software Bill of Materials — SW 구성요소 목록 |
| VEX | Vulnerability Exploitability eXchange — 취약점 영향 판정 문서 |
| VDR | Vulnerability Disclosure Report — 취약점 공개 보고서 |
| NTIA Baseline | 미 상무성 NTIA 최소 필수 요소 7종 |
| CPE/PURL | Common Platform Enumeration / Package URL — 구성요소 고유 식별자 |
| SPDX | ISO/IEC 5962:2021 — SBOM 표준 포맷 |
| CycloneDX | OWASP SBOM 표준 포맷 (v1.5+) |

## 4. 책임과 권한

| 역할 | 책임 | 판정 권한 |
|------|------|-----------|
| SW Lead | SBOM 산출물 범위 정의, 빌드 파이프라인 통합 총괄 | SBOM 릴리스 승인 |
| SW Engineer | 빌드 파이프라인에서 SBOM 자동 생성, 수작업 보완, 품질 검증 | SBOM 초안 작성 |
| Security Officer | SBOM→취약점 매핑, VEX 결정, VDR 배포, 보안 리스크 평가 | VEX/VDR 승인 |
| QA Manager | SBOM·VEX·VDR 기록 DDF 편입, 감사 대응 | 기록 적합성 확인 |
| RA Lead | FDA/MDR/MFDS 제출물에 SBOM·VEX 포함 확인 | 규제 제출 적합 확인 |
| PM | SBOM 산출물 범위 최종 승인 | 범위 승인 |

## 5. 절차

### 5.1 SBOM 생성 범위 정의

| 단계 | 수행자 | 활동 | 산출물 | 판정 기준 |
|------|--------|------|--------|-----------|
| 5.1.1 | SW Lead | 제품 SW 아키텍처에서 SBOM 대상 구성요소 식별 | 구성요소 목록 | 전 SW 모듈 포함 |
| 5.1.2 | SW Lead | X-ray 시스템 특수 구성요소 식별 (아래 참조) | 확장 목록 | 펌웨어 블롭 포함 |
| 5.1.3 | PM | 범위 승인 | 승인 기록 | 서명 완료 |

**X-ray 시스템 SBOM 특수 대상:**
- Generator 제어 FW (실시간 kVp/mAs 제어 라이브러리)
- Detector FPGA 비트스트림 및 제어 FW
- DICOM Conformance 라이브러리 (dcm4che, DCMTK 등)
- 영상 재구성 라이브러리 (FBP, 반복재구성 등)
- AI 추론 엔진 (ONNX Runtime, TensorRT) 및 모델 가중치 해시
- 선량 계산 모듈 (DAP, CTDI 등)
- ALARA 기능 관련 라이브러리

### 5.2 자동 생성 (빌드 파이프라인 통합)

| 단계 | 수행자 | 활동 | 판정 기준 |
|------|--------|------|-----------|
| 5.2.1 | SW Engineer | CI/CD 빌드 시 SBOM 자동 생성 도구 호출 (Syft, CycloneDX CLI 등) | 도구 정상 실행 |
| 5.2.2 | SW Engineer | SBOM 파일을 아티팩트 저장소에 저장 — 파일명: `<product>_<version>_<YYYYMMDD>.cdx.json` | 파일명 규칙 준수 |
| 5.2.3 | SW Engineer | 서명(SHA-256 Hash + GPG/Sigstore)으로 무결성 확보 | 서명 검증 Pass |

### 5.3 수작업 보완

| 단계 | 수행자 | 활동 | 판정 기준 |
|------|--------|------|-----------|
| 5.3.1 | SW Engineer | 빌드에서 포착 불가 구성요소 수동 추가 (FW 블롭, Binary-only 라이브러리) | `evidence.analysis = "manual"` 플래그 |
| 5.3.2 | SW Engineer | Detector FPGA 비트스트림 정보 수동 기입 | 버전·해시 기재 |
| 5.3.3 | SW Lead | 수작업 항목 검토·승인 | 검토 서명 |

### 5.4 검증

| 단계 | 수행자 | 활동 | 판정 기준 |
|------|--------|------|-----------|
| 5.4.1 | SW Engineer | NTIA Baseline 체크리스트 통과 (F-SBOM-001) | 7종 필수 요소 100% |
| 5.4.2 | SW Engineer | 자동 린터로 누락 필드·버전 불일치 검출 | 린터 오류 0건 |
| 5.4.3 | QA | 빌드 ID와 SBOM 1:1 대응 샘플링 검증 | 불일치 0건 |

### 5.5 취약점 매핑 및 VEX

| 단계 | 수행자 | 활동 | 판정 기준 |
|------|--------|------|-----------|
| 5.5.1 | Security Officer | SBOM 구성요소 PURL/CPE를 NVD/OSV/CISA KEV와 매핑 | 매핑 완료 |
| 5.5.2 | Security Officer | CVSS v3.1 + Medical Rubric(IMDRF/CYBER/N60) 반영 위험도 재평가 | 평가 완료 |
| 5.5.3 | Security Officer | VEX 결정: not_affected / affected / fixed / under_investigation | F-SBOM-002 기록 |
| 5.5.4 | Security Officer | Critical/High 취약점은 SOP-CC-001 변경관리 진입 | 변경요청 제출 |

**X-ray 시스템 취약점 우선순위:**
- 원격 코드 실행(RCE) 가능한 DICOM 스택 취약점 → 최우선 패치
- Generator 제어 FW 취약점 → 환자 안전 직결, 즉시 대응
- Detector FW 취약점 → 영상 데이터 무결성 영향 평가
- AI 추론 라이브러리 취약점 → 모델 조작 가능성 평가

### 5.6 유지·갱신

| 이벤트 | 수행자 | 활동 | 기한 |
|--------|--------|------|------|
| SW 릴리스 (Major/Minor/Patch) | SW Engineer | SBOM 재생성 | 릴리스와 동시 |
| 취약점 발견/패치 | Security Officer | SBOM·VEX 동시 갱신 | 발견 후 14일 이내 |
| 분기 정기 리뷰 | SW Lead | SBOM 정확성 전수 검증 | 분기 말 |
| 규제 제출 | RA Lead | 최신 SBOM·VEX·VDR 포함 확인 | 제출 전 |

### 5.7 제출 및 배포

| 규제 기관 | 제출물 | 근거 |
|-----------|--------|------|
| FDA | Premarket Submission에 SBOM·VEX·VDR 포함 | Section 524B (2025-10-01 이후 필수) |
| EU MDR / NB | Technical Documentation Cybersecurity Annex에 SBOM 첨부 | MDCG 2019-16, IMDRF N73 |
| MFDS | 사이버보안 허가·심사 서류에 RA-07(SBOM), RA-08(취약점) 포함 | 사이버보안 가이드라인 |
| 고객/운영자 | VDR 또는 Customer Security Advisory 형태로 배포 | Section 524B Postmarket |

### 5.8 QMSR 실사 대응 — SBOM 기록 요구사항 (v0.3 신설)

FDA QMSR(2026-02-02 시행)에 따라 SBOM 관련 기록은 ISO 13485:2016 §4.2.5 기록 관리 요구사항을 준수해야 한다.

| 단계 | 수행자 | 활동 | 판정 기준 |
|------|--------|------|-----------|
| 5.8.1 | QA Manager | SBOM·VEX·VDR을 MDF 내 사이버보안 파일(Cybersecurity File)로 편입 | QMSR §820.180 준수 |
| 5.8.2 | QA Manager | SBOM 변경 이력의 추적성 확보 — 빌드 ID↔SBOM↔VEX 삼중 연결 | 1:1:1 대응 확인 |
| 5.8.3 | RA Lead | FDA 실사 시 SBOM 즉시 제시 가능 상태 유지 (전자 서명 포함) | 2시간 내 제출 가능 |
| 5.8.4 | Security Officer | QMSR 감사 관점 자체 점검 — SBOM 갱신 이력, VEX 판정 근거, 패치 타임라인 문서화 | 분기 자체감사 완료 |

**QMSR 실사 체크포인트:**
- 사이버보안 파일(Cybersecurity File)이 MDF 내 독립 섹션으로 구성되어 있는가?
- SBOM이 최신 릴리스와 동기화되어 있는가? (§524B 시판후 유지 의무)
- VEX 판정 근거가 객관적 증거(취약점 분석 보고서)로 뒷받침되는가?
- 취약점 패치 시 SOP-CC-001 변경관리 기록과 SBOM 갱신 기록이 연동되는가?

### 5.9 CSAF 기반 취약점 공개 연동 (v0.3 신설)

CISA CSAF(Common Security Advisory Framework) 2.0 기반으로 취약점 정보를 자동 수신하고 SBOM과 연계한다.

| 단계 | 수행자 | 활동 | 판정 기준 |
|------|--------|------|-----------|
| 5.9.1 | Security Officer | CSAF provider feed 구독 설정 (NVD, CISA ICS-CERT, 벤더 CSAF) | 피드 활성화 확인 |
| 5.9.2 | Security Officer | CSAF 어드바이저리 수신 시 SBOM PURL 자동 매칭 | 매칭률 ≥ 95% |
| 5.9.3 | Security Officer | 매칭 결과를 VEX 판정 워크플로(§5.5)에 자동 투입 | 24시간 내 초기 분류 |
| 5.9.4 | Security Officer | SOP-CVD-001(조정된 취약점 공개 정책)과 연계하여 고객 통지 판단 | CVD 정책 준수 |

**EU CRA(Cyber Resilience Act) 2024/2847 대비:**
- 2027년 시행 예정인 EU CRA는 디지털 제품(의료기기 포함 가능)에 대해 SBOM 의무화 및 취약점 보고 의무를 강화
- CycloneDX 1.6+ / SPDX 3.0 호환 포맷으로 사전 전환 검토
- SBOM 자동 갱신 주기를 현행 릴리스 단위에서 CI 빌드 단위로 단축 계획

## 6. 포맷 및 필수 메타데이터

- **포맷**: SPDX 2.3 / 3.0 또는 CycloneDX 1.5 / 1.6 (NTIA 최소필수 요소 7종 충족, EU CRA 대비 SPDX 3.0 또는 CycloneDX 1.6 권장)
- **최소 필드**: Supplier, Component Name, Version, Unique Identifier(PURL/CPE), Dependency Relationship, Author, Timestamp
- **확장 필드(권장)**: License, Hash(SHA-256), Origin URL, Build Environment, Support Status, EOL Date

## 7. 양식

### F-SBOM-001 SBOM 검증 체크리스트

```
═══════════════════════════════════════════════════════════
         F-SBOM-001 SBOM 검증 체크리스트
═══════════════════════════════════════════════════════════
제품명: ________________    SW 버전: ________________
SBOM 파일명: ____________________  작성일: ____-__-__

A. NTIA Baseline 필수 요소 (7종)
┌──┬──────────────────────────────┬────┬───────────────┐
│# │ 항목                         │ Y/N│ 비고          │
├──┼──────────────────────────────┼────┼───────────────┤
│1 │Supplier Name                 │    │               │
│2 │Component Name                │    │               │
│3 │Version                       │    │               │
│4 │Unique Identifier (PURL/CPE)  │    │               │
│5 │Dependency Relationship       │    │               │
│6 │Author of SBOM Data           │    │               │
│7 │Timestamp                     │    │               │
└──┴──────────────────────────────┴────┴───────────────┘

B. 품질 검증
┌──┬──────────────────────────────┬────┬───────────────┐
│# │ 항목                         │ Y/N│ 비고          │
├──┼──────────────────────────────┼────┼───────────────┤
│8 │자동 린터 오류 0건             │    │               │
│9 │빌드 ID↔SBOM 1:1 대응 확인   │    │               │
│10│수작업 항목 manual 플래그      │    │               │
│11│서명(SHA-256+GPG) 검증 Pass   │    │               │
│12│이전 버전 대비 Delta 검토      │    │               │
└──┴──────────────────────────────┴────┴───────────────┘

C. X-ray 특수 구성요소 포함 확인
┌──┬──────────────────────────────┬────┬───────────────┐
│# │ 항목                         │ Y/N│ N/A           │
├──┼──────────────────────────────┼────┼───────────────┤
│13│Generator 제어 FW             │    │               │
│14│Detector FW/FPGA              │    │               │
│15│DICOM 라이브러리              │    │               │
│16│영상처리/재구성 라이브러리     │    │               │
│17│AI 추론 엔진 + 모델 해시      │    │               │
│18│선량 계산 모듈                │    │               │
└──┴──────────────────────────────┴────┴───────────────┘

판정: □ 합격  □ 부적합 (재작업 필요)
검증자: ___________ 일자: ____-__-__
승인자: ___________ 일자: ____-__-__
```

### F-SBOM-002 VEX 판정 기록양식

```
═══════════════════════════════════════════════════════════
         F-SBOM-002 VEX 판정 기록
═══════════════════════════════════════════════════════════
제품명: ________________    SBOM 버전: ______________
평가일: ____-__-__          평가자: ________________

┌──┬──────────┬────────┬──────┬────────────┬──────┬──────┐
│# │구성요소   │CVE ID  │CVSS  │VEX 판정    │사유  │조치  │
│  │(PURL)    │        │Score │            │      │기한  │
├──┼──────────┼────────┼──────┼────────────┼──────┼──────┤
│1 │          │        │      │□N/A □Aff   │      │      │
│  │          │        │      │□Fix □Inv   │      │      │
├──┼──────────┼────────┼──────┼────────────┼──────┼──────┤
│2 │          │        │      │□N/A □Aff   │      │      │
│  │          │        │      │□Fix □Inv   │      │      │
└──┴──────────┴────────┴──────┴────────────┴──────┴──────┘
(N/A=not_affected, Aff=affected, Fix=fixed, Inv=under_investigation)

총 취약점: __건  Critical: __  High: __  Medium: __  Low: __
변경관리 진입 건수: __건 (SOP-CC-001)

승인: Security Officer ___________ 일자: ____-__-__
```

## 8. 기록·이력 관리

- SBOM, VEX, VDR 모두 DDF 및 MDF에 편입 (ISO 13485 §4.2.4 / §4.2.5)
- 보존 기간: 제품 수명 + 15년 (MDR Annex IX) 또는 제품 수명 + 2년 (QMSR §820.180) 중 긴 기간
- QMSR 실사 대비: 사이버보안 파일(Cybersecurity File)을 MDF 내 독립 섹션으로 유지, FDA 실사 시 2시간 내 제출 가능 상태
- 변경 시 SOP-CC-001 변경통제 연동 판정

## 9. 참조 문서

| 문서/표준 | 관계 |
|-----------|------|
| IEC 81001-5-1:2021 | 사이버보안 SBOM 요구 (§7.SR) |
| IEC 62304:2006+AMD1:2015 | SW 구성 관리 (§8) |
| SOP-CC-001 | 취약점 패치 시 변경관리 |
| SOP-DT-001 | 이관 시 SBOM 확정본 전달 |
| SOP-PSUR-001 | 시판후 취약점 보고 |
| SOP-VAL-001 | 패치 후 SW 재검증 |
| SOP-CVD-001 | 조정된 취약점 공개 — CSAF 연동 |
| SOP-AIGOV-001 | AI 모델 런타임 SBOM 연동 |
| SOP-FSCA-001 | 보안 취약점 긴급 조치 시 FSCA 연계 |

## 10. 변경 이력

| 버전 | 일자 | 변경 내용 | 작성자 |
|------|------|----------|--------|
| v0.1 | 2026-04-22 | 초안 작성 | 업무규칙 개발팀 |
| v0.2 | 2026-05-23 | 보강 — 단계별 절차 표(수행자/판정기준), F-SBOM-001/002 양식, X-ray 특수 구성요소·취약점 우선순위, 상호참조 확충 | QA/RA |
| v0.3 | 2026-06-08 | QMSR 실사 대응 — §5.8 사이버보안 파일 MDF 편입·실사 체크포인트 신설, §5.9 CSAF 기반 취약점 자동 연동 신설, EU CRA 2024/2847 사전 대비(SPDX 3.0/CycloneDX 1.6 전환 계획), QMSR §820.180 기록 관리 연동, SOP-CVD-001·SOP-FSCA-001 상호참조 추가 | QA/RA |
