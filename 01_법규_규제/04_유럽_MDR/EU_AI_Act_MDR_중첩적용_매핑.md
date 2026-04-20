# EU AI Act ↔ EU MDR 중첩 적용 매핑 (AI/ML SaMD 대비)

## 1. 목적
본 문서는 AI/ML 기반 의료 SW(SaMD), 특히 X-ray 영상 판독 보조 기능을 염두에 두고 EU AI Act (Regulation (EU) 2024/1689)와 EU MDR (Regulation (EU) 2017/745) 간 중첩 요건을 식별하고, 단일 QMS/기술문서에서 동시에 충족하기 위한 매핑을 정리한다.

## 2. 위험 분류 — 중첩 조건
- AI Act Art. 6(1): 부속 II에 나열된 EU 조화법령(MDR 포함) 제품의 안전 구성요소 또는 그 자체 제품이고, 제3자 적합성평가(NB)가 필요한 경우 → **High-risk AI system**
- 대부분의 Class IIa 이상 AI SaMD는 NB 관여가 필요하므로 High-risk 분류 가능성이 높음
- Class I self-certification 기기는 원칙상 High-risk 비해당 (단, Annex III 별도 해당 여부 확인)

## 3. 요건 매핑
| AI Act 요건 | MDR / ISO 매핑 | 통합 접근 |
|-------------|----------------|-----------|
| Art. 9 Risk Management System | MDR Annex I §3, ISO 14971:2019/A11 | 단일 Risk File, AI 특유 위험(편향, 데이터 드리프트, 적대적 입력) 항목 보강 |
| Art. 10 Data & Data Governance | MDR Annex II §6.1, IEC 62304, GMLP | 학습/검증/테스트 데이터셋 관리 SOP (대표성, 라벨링 품질, 편향 점검) |
| Art. 11 Technical Documentation | MDR Annex II/III | 통합 TD에 AI Act Annex IV 항목 별도 섹션 |
| Art. 12 Record-keeping (Logging) | MDR Annex I §17.2 + IEC 62304 | 배포 모델별 추론 로그 설계, PII 분리·보존 기간 규정 |
| Art. 13 Transparency/IFU | MDR Annex I §23, IEC 82304-1 | IFU에 의도된 용도, 한계, 성능지표, 모니터링 지표 명시 |
| Art. 14 Human Oversight | MDR Annex I §14.2, IEC 62366-1 | 사용적합성 파일에 감독 시나리오 추가 |
| Art. 15 Accuracy/Robustness/Cybersecurity | MDR Annex I §17.2/§17.4, IEC 81001-5-1, FDA Pre-mkt Cyber Guidance | 사이버보안 계획 + 모델 성능 적합성 시험 결합 |
| Art. 16–17 QMS | MDR Art. 10(9), ISO 13485, QMSR §820.25 | 기존 QMS 확장, AI 관련 절차 추가 (데이터·모델 변경관리) |
| Art. 43 CA 경로 | MDR 적합성평가(Annex IX/X/XI) | MDR 경로에 AI Act 요건을 포함해 단일 평가 — NB 선택 시 지정 범위 확인 |
| Art. 61 Post-market monitoring | MDR Art. 83–86 (PMS/PSUR) | 통합 PMS Plan/Report — 모델 성능 모니터링·드리프트 지표 포함 |
| Art. 62 Serious incident reporting | MDR Art. 87 | Vigilance SOP 단일화, AI Act 관련 지표 추가 필드 |

## 4. PCCP / Change Management
- AI Act는 사전 계획된 변경(예: 재학습)을 "substantial modification" 예외로 허용(Art. 43(4))
- MDR은 중요 변경 시 NB 보고 필요 — PCCP(Pre-determined Change Control Plan) 방식으로 정합
- SOP-CHG-001(가칭)에 PCCP 섹션 추가 필요

## 5. 시점/적용
- AI Act 발효: 2024-08-01 / High-risk 조항 본격 적용: 2026-08-02
- 기존 MDR 인증 제품은 2027-08-02까지 과도기 (해석 지침 확인 필요)
- 본 프로젝트는 2026년 내 설계개발 중 → 초기 단계부터 AI Act 반영 권고

## 6. 한국·미국 연계 참고
- KR: 디지털의료제품법(2025-01-24 시행) SaMD·AI 규정 병합 검토(후속 과제)
- US: FDA GMLP 원칙, 2025 Draft Guidance on AI/ML enabled devices, PCCP 개념 일치 → 통합 변경관리 가능

## 7. Gap → 조치
| Gap | 조치 |
|-----|------|
| Risk File에 AI 특유 위험 템플릿 부재 | 14971 위험관리 계획·표에 AI 위험 카탈로그(편향/드리프트/적대적입력/설명가능성) 추가 |
| 데이터 거버넌스 SOP 부재 | SOP-DATA-001(가칭) 신규 — 수집/라벨링/편향감사/버전관리 |
| 모델 변경관리 SOP 부재 | SOP-CHG-001 개정 또는 SOP-ML-001 신규 + PCCP 섹션 |
| PMS에 모델 성능 지표 부재 | PMS Plan에 AUC/Sensitivity/Specificity/서비스드리프트 모니터링 포함 |
| 기술문서 구조가 MDR 전용 | TD 템플릿에 AI Act Annex IV 매핑 컬럼 도입 |

## 8. 출처
- Regulation (EU) 2024/1689 (AI Act)
- Regulation (EU) 2017/745 (MDR)
- MDCG 2019-11, MDCG 2019-16 Rev.1
- IEC 62304:2006/A2:2015, IEC 62366-1:2015/A1:2020, IEC 81001-5-1:2021
- FDA AI/ML-based SaMD Action Plan, PCCP Draft Guidance 2023

## 9. 개정 이력
| 버전 | 일자 | 내용 |
|------|------|------|
| 0.1 | 2026-04-20 | 초안 작성 (High-risk 기준·요건 매핑·Gap) |
