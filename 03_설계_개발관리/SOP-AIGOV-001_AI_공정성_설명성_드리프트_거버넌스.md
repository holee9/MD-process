# SOP-AIGOV-001 — AI 공정성·설명성·드리프트 거버넌스 (v0.1 초안)

문서번호: SOP-AIGOV-001
버전: v0.1 (초안)
작성일: 2026-04-25
관련: 03_설계_개발관리/AI_구성요소_단위_성능평가.md, 02_QMS/디지털의료제품법_요구사항_매트릭스.md(DR-32/33/35), 07_위험관리_ISO14971/

## 1. 목적
의료용 X-ray 시스템에 탑재되는 AI 구성요소(진단보조, 선량제어, 영상복원, 생성형)의
공정성(Fairness)·설명성(Explainability)·데이터 드리프트(Drift)를 전 수명주기 동안
정량 모니터링·통제하기 위한 거버넌스를 정의한다.

## 2. 규제·표준 근거
- 디지털의료제품법 시행규칙(개정 예정 2026) 제40조 — 구성요소 성능평가
- MFDS "AI 의료기기 허가·심사 가이드라인" 2025 개정판
- FDA "AI/ML-Based Software as a Medical Device Action Plan" + PCCP Guidance(2024-12)
- EU AI Act(Reg. 2024/1689) Art. 9 (Risk Mgmt), Art. 10 (Data Governance), Art. 13 (Transparency), Art. 14 (Human Oversight), Art. 17 (QMS)
- IMDRF AIMD WG/N67 "Machine Learning-enabled Medical Devices: Key Terms and Definitions"
- ISO/IEC 23894:2023 (AI Risk Management)
- ISO/IEC TS 12791:2024 (Treatment of unwanted bias in classification/regression ML)
- ISO/IEC TS 4213:2022 (Assessment of ML classification performance)

## 3. 적용 범위
| 분류 | 예시 | 본 SOP 적용 |
|------|------|------------|
| 진단보조 AI | 결절 검출, 골밀도 추정 | ●(Full) |
| 선량제어 AI | AEC, 자동 KV/mAs | ●(Full) |
| 영상복원 AI | DLR, MAR, Denoise | ●(Full) |
| 생성형 AI | 합성 이미지, Synthesis View | ●(Full + 추가 검토) |
| 비-임상 AI | UI 추천, 워크플로 최적화 | ◐(Drift만 적용) |

## 4. 책임·권한
| 역할 | 책임 |
|------|------|
| AI Governance Officer | 본 SOP 운영 총괄, 분기별 리뷰 주재 |
| Data Steward | 데이터셋 수집·라벨링·메타데이터·바이어스 평가 |
| ML Engineer | 모델 학습·검증·재학습 트리거 실행 |
| Clinical Lead | 임상 영향평가, 의료진 사용성 검토 |
| QA/RA | DHF·시판후 보고, 규제 보고 |
| Risk Manager | ISO 14971 위험분석 통합 |

## 5. 핵심 원칙
1. **Pre-specified**: 모든 AI 컴포넌트는 PCCP(Predetermined Change Control Plan)와 등가의 사전 변경계획을 보유한다.
2. **Continuously monitored**: 시판 후 성능·드리프트·공정성을 자동 수집·집계한다.
3. **Human oversight**: 임상 의사결정 경로에는 항상 의료진 개입 지점을 명시한다(EU AI Act Art. 14).
4. **Explainable**: 의료진이 활용 가능한 수준의 설명(saliency, feature attribution, confidence interval 등)을 제공한다.
5. **Auditable**: 학습·재학습·예측 결정에 대한 데이터 lineage를 보존한다(MDR §10.4 / ISO 13485 §4.2.5).

## 6. 공정성(Fairness)
### 6.1 평가 차원
- 인구학적: 연령(소아/성인/고령), 성별, 인종/민족(가능한 경우), 체격(BMI/체중)
- 임상학적: 병변 유형, 영상 프로토콜, 장비 모델, 시설(병원 규모/지역)
- 데이터 출처: 국가, 데이터 vendor

### 6.2 지표
- Demographic Parity Difference, Equalized Odds, Equal Opportunity
- Subgroup AUROC/Sensitivity/Specificity 95% CI
- 임계값: 주요 부분군 간 성능 격차 ≤ 5%p (절대) / 상대편향 ≤ 10%

### 6.3 대응
- 사전: 데이터 수집 시 부분군 ≥ 100명/군 확보, 미달 시 가중 샘플링
- 사후: ISO/IEC TS 12791 권고 기법(reweighing, threshold optimization, post-hoc calibration) 적용
- 격차 해소 불가 시: 라벨에 적용 제한 명시(Indications for Use 한정)

## 7. 설명성(Explainability)
### 7.1 출력 형태
- 분류/검출: 픽셀 단위 heatmap(Grad-CAM 등) + 확률·신뢰도
- 회귀(선량 추정 등): 입력 특징 기여도 + 95% 예측구간
- 생성형: 입력 대비 변형 영역 차이맵 + 합성 표시 워터마크(EU AI Act Art. 50 의무)

### 7.2 의료진 인터페이스 요건
- 모든 AI 결과 화면에 "AI 보조 결과 — 최종 판단은 의료진" 고정 문구
- 신뢰도 임계값 미달 시 "Low confidence" 경고
- 의료진 Override 로그 100% 기록(ISO 14971 Pos-Market 입력)

### 7.3 설명 품질 검증
- 정성: 임상 패널(≥3명) 평가, 합치도 κ ≥ 0.6
- 정량: Faithfulness(Insertion/Deletion AUC), Stability(Local Lipschitz)
- 임계값 미달 시 모델 또는 설명 기법 재검토

## 8. 데이터·모델 드리프트
### 8.1 드리프트 유형
| 유형 | 정의 | 모니터링 방법 |
|------|------|---------------|
| Covariate (Input) Drift | 입력 분포 변화 | PSI, KL Divergence |
| Concept Drift | 입출력 관계 변화 | Rolling AUROC, Bayesian online detector |
| Label Drift | 정답 분포 변화 | 분기별 라벨 검토 표본 |
| Prevalence Drift | 양성률 변화 | EWMA 모니터 |
| Hardware Drift | 장비 노후/캘리브레이션 변화 | Phantom QA 결과 연동 |

### 8.2 모니터링 빈도
- 자동: 일 단위 입력 통계, 주 단위 성능 메트릭
- 수동: 분기 1회 임상 라벨 표본 재평가(N≥200)

### 8.3 트리거·조치
| 임계 | 조치 |
|------|------|
| PSI > 0.1 | 데이터 검토(소프트 알람) |
| PSI > 0.25 또는 AUROC 하락 ≥ 5%p | 재학습 검토(SOP-CC-001 변경관리 진입) |
| 임상 위해 가능성(ISO 14971 RAR ↑) | 즉시 사용중지·FSN 검토 |

## 9. 변경관리(PCCP) 연계
- 사전 정의된 학습 데이터 추가, 임계값 튜닝, 정기 재학습은 PCCP 범위 내에서 SOP-CC-001 경량 경로로 처리
- 새로운 인구집단·장비 추가, 알고리즘 구조 변경, 적응증 확대는 정식 변경관리(중·대 변경) 진입
- PCCP 범위 변경은 FDA·MFDS·EU에 사전 통지 필요

## 10. 시판후 감시(PMS) 연동
- 본 SOP의 KPI는 08_시판후_감시_PMS/PMS_개요.md 의 PSUR/PMCF 입력으로 활용
- AI 관련 부작용은 별도 분류 코드(AIE-XX) 부여하여 통계 분리

## 11. 측정 지표(KPI)
- 부분군 성능 격차 5%p 이내 유지 비율 ≥ 95%
- 설명 품질 임계값 미달 모델 비율 = 0
- 드리프트 알람 후 조치 평균 일수 ≤ 14일
- AI 부작용(AIE-XX) 보고 누락 = 0

## 12. 기록 및 보관
- 학습/검증 데이터셋 카드, 모델 카드, 공정성 평가서, 설명성 평가서, 드리프트 모니터링 로그
- 보관 기간: ISO 13485 §4.2.5 + MDR Annex IX = 제품 EoS 후 15년

## 13. 개정 이력
| 버전 | 날짜 | 변경 내용 |
|------|------|-----------|
| v0.1 | 2026-04-25 | 초안 작성 |

## 14. 미확정·후속 과제
- ISO/IEC TS 12791 권고 기법별 임상영상 적용성 비교 — 별도 워킹페이퍼 필요
- EU AI Act Art. 50 합성 표시 워터마크 기술적 요건 — 표준 미확정 상태
- 디지털의료제품법 자율성능인증제 세부 항목과 본 SOP §6/§7 매핑 — 시행규칙 확정 후 보강
- PCCP 범위 외 변경에 대한 FDA 510(k)/De Novo·MFDS 변경허가 결정 트리 — SOP-CC-001 v0.2와 병합
