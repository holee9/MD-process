---
doc-id: IEC_81001-5-1_FDA_Cybersecurity_SW보안
title: 의료기기 SW 사이버보안 — IEC 81001-5-1 및 FDA Premarket Cybersecurity 통합
type: Guide
version: v0.3
status: draft
category: 03_설계_개발관리
purpose: IEC 81001-5-1 및 FDA Cybersecurity Guidance 기반 의료기기 SW 사이버보안 수명주기 활동의 단계별 절차·책임·양식 제공
applicable:
  - IEC 81001-5-1:2021
  - IEC 62443-4-1 (참조)
  - FDA Final Guidance "Cybersecurity in Medical Devices: Quality Management System Considerations and Content of Premarket Submissions" (February 2026, Docket FDA-2021-D-1158; supersedes 2025-06-27 및 2023-09-27 final) [audit #938]
  - FD&C Act §524B (Consolidated Appropriations Act, 2023, P.L. 117-328 §3305 신설; 2023-03-29 시행)
  - EU MDR 2017/745 Annex I §17.2, §17.4
  - MDCG 2019-16 Rev.1
  - IEC 62304:2006/A1:2015
  - ISO 14971:2019
  - MFDS 사이버보안 허가심사 가이드라인
  - 디지털의료제품법 (법률 제20722호)
forms:
  - F-SEC-001
related-docs:
  - IEC_62304_SW_수명주기
  - SOP-SBOM-001
  - SOP-CC-001
  - SOP-CAPA-001
  - ISO14971_프로세스_상세
  - 외부_Pen-test_계획서
  - X-ray_장비_안전성능_표준_매핑
  - EU_AI_Act_MDR_중첩적용_매핑
  - SOP-UDI-001
related-issues: [11]
owner: Security Officer / SW Lead
last-review: 2026-06-24
review-due: 2027-05-24
---

# 의료기기 SW 사이버보안 — IEC 81001-5-1 및 FDA Premarket Cybersecurity 통합 — v0.3

## 1. 목적

의료기기 SW(X-ray system SW, Detector firmware, 영상처리 SaMD)의 사이버보안 수명주기 활동을 단일 체계로 통합 관리한다. IEC 62304 SDLC, ISO 14971 위험관리, IEC 81001-5-1 제품 보안, FDA Premarket Cybersecurity Guidance(2023-09) 요구사항을 한 개의 Security Management Plan으로 연결한다.

## 2. 적용 범위

본 문서는 Cyber Device(FDA §524B 정의) 해당 여부와 무관하게, 네트워크 연결 가능한 모든 의료기기 SW에 적용한다.

| 구성요소 | 네트워크 연결 | Cyber Device 해당 | 적용 수준 |
|----------|-------------|-------------------|----------|
| X-ray 제어 SW | 이더넷(DICOM, HL7) | ○ | Full |
| Detector 펌웨어 | 내부 버스 + 서비스 포트 | ○ | Full |
| 영상처리 SaMD | 병원 네트워크, 클라우드 | ○ | Full |
| 이동형 X-ray 제어 | Wi-Fi/LTE(선택) | ○ | Full |
| 로컬 전용 유틸리티 | 없음 | △ | Lite (위협모델링만) |

## 3. 용어 정의

| 용어 | 정의 |
|------|------|
| TARA | Threat Analysis and Risk Assessment |
| STRIDE | Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege |
| SBOM | Software Bill of Materials |
| CVD | Coordinated Vulnerability Disclosure |
| CVSS | Common Vulnerability Scoring System |
| MDS2 | Manufacturer Disclosure Statement for Medical Device Security |

## 4. 역할·책임

| 역할 | 책임 |
|------|------|
| Security Officer | Security Management Plan 총괄, 보안 리뷰 승인, CVD 대응 총괄 |
| SW Lead | 보안 요구사항 구현 관리, 보안 코딩 표준 적용 |
| 위험관리자 | 보안위험의 ISO 14971 프로세스 통합, TARA 수행 |
| RA/QA | 규제 제출 보안 문서 패키지 검토, SBOM 포맷 확인 |
| DevOps/CM | SBOM 자동 생성, CVE 스캔 파이프라인 운영 |
| PRRC (EU) | 기술문서 보안 섹션 적합성 최종 확인 |

## 5. Security Management Plan 구조 및 수행 절차

### 5.1 Cyber Device 해당성 판단 (단계 1)

| 수행자 | 활동 | 판정 기준 | 산출물 |
|--------|------|-----------|--------|
| RA + Security Officer | FDA §524B 정의에 따른 해당성 평가 | SW가 포함되고 + 인터넷/네트워크 연결 가능 또는 기술적으로 사이버공격 가능 | Cyber Device 해당성 결정문서 |

### 5.2 위협 모델링 — TARA (단계 2)

| 단계 | 수행자 | 활동 | 산출물 |
|------|--------|------|--------|
| 2-1 | Security Officer | DFD(Data Flow Diagram) 작성 — 기기 내부, 병원 네트워크, 원격 서비스, 업데이트 경로 | DFD |
| 2-2 | SW 팀 + 위험관리자 | STRIDE 분석 — 각 데이터 흐름/저장소/프로세스에 위협 식별 | STRIDE 위협 목록 |
| 2-3 | 위험관리자 | 위협별 심각도·발생확률 평가 → 위험등급 결정 (ISO 14971 연계) | 보안 위험 평가표 |
| 2-4 | Security Officer | 공격 벡터 우선순위 결정, 위험통제 전략 수립 | 위협 모델 보고서 |

**X-ray 시스템 주요 위협 시나리오**:

| 위협 | 공격 벡터 | 영향 | 위험등급 |
|------|-----------|------|---------|
| 노출 파라미터 변조 | DICOM Modality Worklist 위변조 | 환자 과노출 (S4) | 높음 |
| Detector FW 변조 | 서비스 포트 무인증 접근 | 영상 왜곡, 오진 유발 | 높음 |
| 환자 영상 유출 | 미암호화 DICOM 전송 | 개인정보 침해 | 중간 |
| 원격 서비스 침투 | VPN 취약점 | 기기 제어권 탈취 | 높음 |
| 랜섬웨어 감염 | OS 패치 미적용 | 서비스 중단 (DoS) | 높음 |
| USB 매체 감염 | 물리 접근 | 멀웨어 설치 | 중간 |

### 5.3 보안 요구사항 정의 (단계 3)

| 수행자 | 활동 | 산출물 |
|--------|------|--------|
| Security Officer + SW Lead | TARA 결과 기반 보안 요구사항 도출 (기능적/비기능적) | 보안 요구사항 명세 (SRS 보안 섹션) |
| SW Lead | 요구사항 추적 매트릭스에 보안 요구 반영 | 추적 매트릭스 갱신 |

**X-ray 필수 보안 요구사항 (최소)**:
- 사용자 인증: 역할기반 접근통제 (RBAC), 비활동 자동 잠금
- 통신 암호화: DICOM TLS 1.2+, VPN IPsec/IKEv2
- 데이터 무결성: 영상 데이터 해시 검증, 감사 로그 변조 방지
- FW 보호: 서명된 펌웨어만 설치, 롤백 방지(Anti-rollback)
- 로그: 접근·변경·오류 이벤트 감사 로그 (최소 90일 보존)
- SBOM 관리: 빌드 시 자동 생성, CVE 자동 스캔

### 5.4 보안 아키텍처·설계 (단계 4)

| 수행자 | 활동 | 산출물 |
|--------|------|--------|
| SW 아키텍트 + Security Officer | 신뢰경계(Trust Boundary) 정의, 노출표면(Attack Surface) 최소화 설계 | 보안 아키텍처 문서 |
| SW 아키텍트 | 암호화·키 관리 설계 (Cryptographic Architecture) | 암호화 설계서 |
| DevOps | SBOM 초안 생성 (CycloneDX 또는 SPDX JSON) | SBOM |

### 5.5 보안 구현 (단계 5)

| 수행자 | 활동 | 판정 기준 |
|--------|------|-----------|
| 개발자 | 보안 코딩 표준 적용 (CERT C/C++, OWASP 등) | 정적분석 보안 결함 0건(Critical/High) |
| 개발자 | 보안 요구사항 구현 | 코드 리뷰 보안 체크 통과 |
| DevOps | SBOM 자동 갱신, 의존성 CVE 스캔 | Known CVE Critical 0건 |

### 5.6 보안 V&V (단계 6)

| 시험 유형 | 수행자 | 방법 | 합격 기준 |
|----------|--------|------|-----------|
| 정적 분석 | DevOps | SAST 도구 (Coverity, SonarQube 등) | Critical/High 0건 |
| 동적 분석 | SW QA | DAST/Fuzzing (DICOM, 웹 인터페이스) | 크래시 0건 |
| 알려진 취약점 검사 | DevOps | SBOM 기반 CVE 매핑 | CVSS ≥7.0 해결 완료 |
| 침투 시험 | 외부 업체 | 외부_Pen-test_계획서 참조 | Critical 발견사항 0건 |
| 보안 기능 시험 | SW QA | 인증·접근통제·암호화·로그 기능 시험 | 모든 보안 요구 Pass |

### 5.7 릴리스 및 유지보수 보안 (단계 7)

| 활동 | 수행자 | 주기 | 산출물 |
|------|--------|------|--------|
| SBOM 최종본 확정 | DevOps | 릴리스 시 | SBOM (릴리스 버전) |
| MDS2 작성/갱신 | Security Officer | 릴리스 시 | MDS2 문서 |
| CVE 모니터링 | DevOps | 상시 (주 1회 이상) | CVE 모니터링 보고 |
| 패치 개발·배포 | SW 팀 | 필요 시 | 패치 릴리스 |
| PMS 보안 감시 | QA + Security Officer | 분기 | PSUR 보안 섹션 |

## 6. IEC 81001-5-1 ↔ IEC 62304 SDLC 매핑

| 81001-5-1 활동(§) | 62304 SDLC 대응 | 본 문서 단계 |
|-------------------|-----------------|-------------|
| 5.2 Security Risk Management | §4.3 SW 안전성 클래스 결정 + ISO 14971 | 5.2 |
| 5.3 Security Management | §5 개발계획 | 5.1 |
| 6.1 Security Requirements | §5.2 요구사항 분석 | 5.3 |
| 6.2 Secure by Design | §5.3/5.4 아키텍처·상세설계 | 5.4 |
| 6.3 Secure Coding | §5.5 구현 | 5.5 |
| 7.x Security V&V | §5.6/5.7 시험 | 5.6 |
| 8.x Release/유지보수 | §6 유지보수, §7 문제해결 | 5.7 |
| 9.x Decommissioning | §8 연계 | (별도 절차) |

## 7. FDA 제출물 매핑

| FDA 요구 제출물 | 본 체계 출처 | 단계 |
|----------------|-------------|------|
| Security Risk Management Report | §5.2 TARA + ISO 14971 보안위험 | 2 |
| Threat Model | §5.2 DFD + STRIDE | 2 |
| Architecture Views | §5.4 보안 아키텍처 | 4 |
| SBOM (CycloneDX/SPDX) | §5.4~5.7 빌드 파이프라인 자동 생성 | 4~7 |
| Vulnerability Assessment | §5.6 SBOM 기반 CVE 매핑 | 6 |
| Security Testing Documentation | §5.6 시험 기록 | 6 |
| Interoperability Considerations | MDS2 | 7 |
| Labeling (사이버보안 부속) | MDS2 + IFU 보안 섹션 | 7 |
| Software-level POA | Plan §5.1~5.7 통합 | 전체 |

## 8. 취약점 대응 절차 (CVD)

| 단계 | 수행자 | 활동 | SLA |
|------|--------|------|-----|
| 접수 | Security Officer | security@ 창구 접수, ISAC 참여 확인 | 접수 확인 48시간 이내 |
| 분류 | Security Officer + 위험관리자 | CVSS v3.1/v4 평가, 임상·선량 영향 판단 | 분류 완료 5영업일 |
| 위험평가 | 위험관리자 | ISO 14971 업데이트, 긴급 통보 필요 여부 판단 | — |
| 패치 개발 | SW 팀 | IEC 62304 §6.2 변경 절차, PCCP 해당 여부 판정 | Critical: 30일 / High: 60일 / Medium: 90일 |
| 배포 | QA + 서비스 | 보안 공지, SBOM 갱신본 발행, 필드 업데이트 | 패치 완료 후 15일 이내 |
| PMS 통합 | QA | PSUR 보안 섹션 반영, MDR vigilance 임계치 평가 | 분기 보고 |

## 9. 보안 활동 체크리스트 (F-SEC-001)

```
┌──────────────────────────────────────────────────────────────┐
│              사이버보안 활동 체크리스트 (F-SEC-001)             │
├──────────────────────────────────────────────────────────────┤
│ 프로젝트명:                    버전:                         │
│ 대상 SW:                       Security Officer:             │
├──────────────────────────────────────────────────────────────┤
│ ■ 설계 단계                                                  │
│ □ Cyber Device 해당성 판단 완료                               │
│ □ DFD 작성 완료                                              │
│ □ STRIDE 위협 분석 완료                                       │
│ □ 보안 위험 평가 (ISO 14971 연계) 완료                        │
│ □ 보안 요구사항 SRS 반영 완료                                 │
│ □ 보안 아키텍처 문서화 완료                                    │
│ □ 암호화·키 관리 설계 완료                                    │
│ □ SBOM 초안 생성 완료                                        │
├──────────────────────────────────────────────────────────────┤
│ ■ 구현·시험 단계                                              │
│ □ 보안 코딩 표준 적용 확인                                    │
│ □ 정적 분석(SAST) 수행 — Critical/High: 0건                  │
│ □ 동적 분석/Fuzzing 수행 — 크래시: 0건                        │
│ □ SBOM CVE 스캔 — CVSS≥7.0: 0건 미해결                      │
│ □ 침투 시험 완료 — Critical: 0건                              │
│ □ 보안 기능 시험 Pass                                        │
├──────────────────────────────────────────────────────────────┤
│ ■ 릴리스 단계                                                │
│ □ SBOM 최종본 확정                                           │
│ □ MDS2 작성/갱신                                             │
│ □ CVD 절차 수립 확인                                          │
│ □ 사용자 보안 문서(IFU 보안 섹션) 검토                        │
│ □ 규제 제출 보안 패키지 완결성 확인                            │
├──────────────────────────────────────────────────────────────┤
│ Security Officer 서명:          일자:                         │
│ QA 확인:                        일자:                         │
└──────────────────────────────────────────────────────────────┘
```

## 10. X-ray 제품 보안 설계 지침

| 영역 | 위협 | 보안 통제 |
|------|------|----------|
| 원격 서비스 포트(VPN) | 무인증 원격 접속 | IPsec VPN, MFA, 세션 타임아웃, 접근 로그 |
| DICOM 서비스 | 미암호화 영상 전송 | DICOM TLS, AE Title 기반 접근통제, 감사 로그 |
| Workstation OS | 패치 미적용, 멀웨어 | Windows LTSC 선택, 호스트 FW, AV, 분기 패치 |
| Detector 펌웨어 | 변조된 FW 설치 | 코드 서명, Secure Boot, Anti-rollback |
| 이동형 장비 | 물리적 접근(USB) | USB 포트 비활성화 정책, 물리 잠금장치 |
| AI 모델 | 적대적 입력(Adversarial) | 입력 검증, 이상 탐지, 모델 무결성 해시 |

## 11. 오픈 이슈

1. MFDS 사이버보안 가이드 2024 이후 개정 여부 재확인
2. 디지털의료제품법 시행규칙 SaMD 사이버보안 중복조항 최종 확인
3. EUDAMED 사이버 사건 입력 스키마 확정 여부
4. SBOM 자동 생성 툴체인(제조 파이프라인 내) 선정 후 SOP 부속서 확정

## 12. 변경 이력

| 버전 | 일자 | 변경 내용 | 작성자 |
|------|------|----------|--------|
| v0.1 | 2026-04-21 | 초안 — 표준·규제 매핑, 기본 구조 | RA/QA |
| v0.2 | 2026-05-24 | 단계별 수행절차·책임·SLA 추가, X-ray 위협 시나리오 구체화, F-SEC-001 보안활동 체크리스트 포함, CVD 절차 상세화, FDA 제출물 매핑 보강, 상호참조 확충 | Security Officer/QA |


## 개정 이력

| 버전 | 일자 | 변경 내용 | 작성자 |
|---|---|---|---|
| v0.3 | 2026-06-24 | audit #913 frontmatter 법령 명칭 정정 (FDARA → CAA 2023 §3305) | QMS-Bot |
