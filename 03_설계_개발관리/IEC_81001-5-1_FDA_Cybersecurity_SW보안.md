# 의료기기 SW 사이버보안 — IEC 81001-5-1 및 FDA Premarket Cybersecurity 통합 (v0.1)

## 1. 목적
의료기기 SW(X-ray system SW / detector firmware / 영상처리 SaMD)의 사이버보안 수명주기 활동을
단일 체계로 통합 관리한다. IEC 62304 SDLC, ISO 14971 위험관리, IEC 81001-5-1 제품 보안, FDA Premarket
Cybersecurity Guidance(2023-09) 요구사항을 한 개의 Security Management Plan으로 연결한다.

## 2. 적용 표준·규제

| 표준·규제 | 범위 | 상태(2026-04) |
|----------|------|---------------|
| IEC 81001-5-1:2021 | 제조사용 제품 보안 capability(SDL) | SoTA 적용 — OJEU 미등재 |
| IEC 62443-4-1 (참조) | 일반 제품 보안 개발 프로세스 참조 | 산업계 참조 |
| FDA Guidance "Cybersecurity in Medical Devices: QSR and Premarket Submissions" (2023-09-27) | 510(k)·De Novo·PMA 필수 | 시행 중 |
| FDA 섹션 524B (FDARA) | 사이버기기(Cyber Device) 정의·제출 의무 | 2023-03-29 시행 |
| MDR Annex I §17.2, §17.4 | SW 반복성, 보안, 오용 방지 | Harmonized |
| MDCG 2019-16 rev.1 (2020) | MDR 사이버보안 지침 | 참조 |
| MFDS 「사이버보안 허가·심사 가이드라인」(2022 개정) | 국내 제출용 | 시행 중 |
| 디지털의료제품법(2025-01-24) | SaMD·AI 중복 적용 여부 확인 필요 | 확인 진행 |

## 3. Security Management Plan (단일 산출물 구조)

1. 범위 및 Cybersecurity Device 해당성
2. 역할·책임 (PRRC/품질책임자/Security Officer/개발 리드)
3. Threat Modeling — STRIDE + DFD (기기 + 네트워크 + 업데이트 경로)
4. 보안 요구사항(Functional/Non-functional) ← 요구사항 추적 매트릭스 연결
5. 보안 아키텍처 — 신뢰경계·노출표면
6. SBOM (CycloneDX 또는 SPDX JSON, 모든 상용·오픈소스 포함)
7. Vulnerability Management Plan (취약점 접수·평가·패치 SLA)
8. Security Testing Plan (정적·동적·fuzzing·침투시험·알려진 취약점 검사)
9. Cryptographic / Key Management
10. 사용자용 보안 문서 (MDS2 또는 동등)
11. PMS 보안 감시 및 조정 통제(Coordinated Vulnerability Disclosure)

## 4. IEC 81001-5-1 활동 ↔ IEC 62304 SDLC 매핑

| 81001-5-1 활동(§) | 62304 SDLC 대응 |
|-------------------|-----------------|
| 5.2 Security Risk Management | 62304 §4.3 SW 안전성 클래스 결정과 병행; ISO 14971 보안위험 서브프로세스 |
| 5.3 Security Management | 62304 §5 개발계획 |
| 6.1 Security Requirements | 62304 §5.2 요구사항 분석 |
| 6.2 Secure by Design | 62304 §5.3 아키텍처·상세설계 |
| 6.3 Implementation (secure coding) | 62304 §5.5 구현 |
| 7.x Security V&V | 62304 §5.6/5.7 단위·통합시험 |
| 8.x Release / 유지보수 보안 | 62304 §6 유지·§7 문제해결 |
| 9.x Decommissioning | 62304 §8.x 연계 |

## 5. FDA 제출물 매핑 (2023 Guidance)

| FDA 요구 제출물 | 본 체계에서의 출처 |
|------------------|---------------------|
| Security Risk Management Report | Security Management Plan §3~§4 + ISO 14971 보안위험 |
| Threat Model | Plan §3 |
| Architecture Views (global, multi-patient, updateability) | Plan §5 |
| SBOM | Plan §6, 빌드파이프라인 자동 생성 |
| Vulnerability Assessment (SBOM 기반 CVE 매핑) | Plan §7 |
| Security Testing Documentation | Plan §8 + 형식시험 보고서 |
| Interoperability Considerations | 사용자용 보안 문서 |
| Labeling (사이버보안 부속 문서) | Plan §10 |
| Software-level POA (안전한 개발·유지보수 계획) | Plan §3~§11 통합 |

## 6. 취약점 대응 절차(Coordinated Vulnerability Disclosure)

1. 접수 — security@<company> 창구, ISAC 참여
2. 분류 — CVSS v3.1 기본 + CVSS v4 의료기기 Rubric(선택)
3. 위험평가 — ISO 14971 업데이트, 임상·선량 영향 판단
4. 패치 개발 — 62304 §6.2, PCCP 해당 여부 판정
5. 배포 — 보안 공지(SBOM 갱신본 포함) / FDA Voluntary Malfunction Summary Reporting 정합
6. PMS 통합 — PSUR에 보안 섹션 포함, MDR vigilance 임계치 이하 건도 추이 관찰

## 7. X-ray 제품 특성 반영(요약)
- 원격 서비스 포트(VPN) — 접근통제·로그·세션 제한 필수
- DICOM 서비스 — TLS, 역할기반 접근, AE Title 관리
- Workstation OS — Windows LTSC 등 장수명 OS 선택 및 패치 윈도우
- Detector Firmware — 서명된 펌웨어, 롤백 방지
- 이동형 장비 — 물리적 접근 위협 모델링 추가

## 8. 오픈 이슈
1. MFDS 사이버보안 가이드 2024 이후 개정 여부 재확인
2. 디지털의료제품법 시행규칙 SaMD 사이버보안 중복조항 최종 확인
3. EUDAMED 사이버 사건 입력 스키마 확정 여부
4. SBOM 자동 생성 툴체인(제조 파이프라인 내) 선정 후 SOP 부속서 확정

## 9. 연계 문서
- 03_설계_개발관리/IEC_62304_SW_수명주기.md
- 07_위험관리_ISO14971/ISO14971_프로세스_상세.md
- 05_검사_시험_밸리데이션/X-ray_장비_안전성능_표준_매핑.md
- 01_법규_규제/04_유럽_MDR/EU_AI_Act_MDR_중첩적용_매핑.md (AI Art. 15 사이버보안 중첩)
- 06_문서_기록관리/SOP-UDI-001_UDI_통합관리_초안.md (DI 변경 시 보안 릴리스 연계)
