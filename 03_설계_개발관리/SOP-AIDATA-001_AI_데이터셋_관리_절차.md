# SOP-AIDATA-001: AI/ML 데이터셋 관리 절차 (v0.1)

## 1. 목적
AI/ML 기반 의료기기(X-ray 영상분석 등)의 학습·검증·시험 데이터셋에 대한 수집, 선별, 라벨링, 버전관리, 편향관리, 보존 절차를 정의한다.

## 2. 적용 범위
- 본 절차는 AI/ML 구성요소를 포함하는 모든 의료기기 소프트웨어에 적용
- 학습(Training), 검증(Validation), 시험(Test) 데이터셋 전체 수명주기

## 3. 근거
| 규격/가이드 | 관련 요구 |
|------------|-----------|
| ISO 13485:2016 §7.3 | 설계개발 입력·검증·확인 |
| IEC 62304:2006+A1 §5.2 | SW 요구사항 (데이터 의존성 포함) |
| ISO 14971:2019 §5 | 위험 분석 (데이터 편향 → 진단 오류 위험) |
| FDA GMLP (2021) | Good Machine Learning Practice 10원칙 |
| FDA PCCP Guidance (2023) | 사전결정 변경관리 계획 — 데이터 재학습 포함 |
| MFDS AI 의료기기 허가심사 가이드 (2024) | 데이터셋 명세 제출 요구 |
| EU AI Act Art. 10 (2024) | 학습 데이터 거버넌스 의무 |
| MDCG 2025-6 | AI-Powered Medical Devices 가이드 |
| Johner AI Guideline | 데이터 품질·분리·문서화 실무 |

## 4. 용어 정의
| 용어 | 정의 |
|------|------|
| 학습 데이터(Training Data) | 모델 파라미터 최적화에 사용되는 데이터 |
| 검증 데이터(Validation Data) | 하이퍼파라미터 튜닝·조기종료 판단에 사용 |
| 시험 데이터(Test Data) | 최종 성능 평가에만 사용, 학습·튜닝에 노출 금지 |
| 라벨링(Annotation) | 의료전문가에 의한 정답(Ground Truth) 부여 |
| 데이터 카드(Data Card) | 데이터셋 메타정보 기술서 |

## 5. 데이터셋 수명주기

### 5.1 수집 (Collection)
- 데이터 출처 식별: 임상기관, 공개 데이터셋, 시뮬레이션 등
- 윤리 승인: IRB/기관생명윤리위원회 승인 또는 면제 근거 확보
- 환자 동의: 개인정보보호법, HIPAA(해당 시), GDPR(해당 시) 충족
- 비식별화: DICOM 헤더 비식별화(de-identification) 수행, 방법 기록

### 5.2 선별 및 분리 (Curation & Split)
- 포함/배제 기준(Inclusion/Exclusion Criteria) 문서화
- 데이터 분리 비율 및 방법 명시 (예: 환자 단위 분리로 데이터 누출 방지)
- **시험 데이터는 학습·검증과 완전 격리** — 접근권한 분리, 버전 잠금
- 대표성 분석: 연령·성별·인종·질환 분포 기록, 목표 사용환경과의 정합성 검토

### 5.3 라벨링 (Annotation)
- 라벨링 가이드라인 문서 작성 (판독 기준, 등급 정의)
- 최소 2인 독립 라벨링 + 불일치 해소 프로토콜(제3자 전문의 판정)
- 라벨러 자격 요건: 해당 영역 전문의 또는 동등 경력
- 라벨링 품질 지표: 합의율(Inter-rater Agreement, Cohen's κ ≥ 0.7 목표)

### 5.4 버전관리 (Versioning)
- 데이터셋 버전 ID 부여: `DS-{유형}-{버전}-{날짜}` (예: DS-TRAIN-v1.2-20260401)
- 변경 이력: 추가·삭제·라벨 수정 사유 및 승인자 기록
- DVC(Data Version Control) 또는 동등 도구 사용 권장
- 변경 시 영향 분석: 모델 재학습·재검증 필요 여부 판단 (PCCP 연계)

### 5.5 편향 관리 (Bias Management)
- 수집 단계에서 알려진 편향 요인 문서화
- 분포 분석: 하위그룹별 성능 편차 확인 (Subgroup Analysis)
- 편향 완화 전략 기록: 오버샘플링, 데이터 증강, 가중치 조정 등
- 잔여 편향은 ISO 14971 위험평가에 반영 → 07_위험관리 파일 교차 참조

### 5.6 보존 및 폐기 (Retention & Disposal)
- 보존 기간: 제품 수명 + 최소 2년 (ISO 13485 §4.2.5 정합)
- 원시 데이터(Raw) + 전처리 데이터(Processed) + 라벨 모두 보존
- 폐기 시 비식별화 데이터도 안전 삭제 절차 적용, 기록 보존

## 6. 데이터 카드 (Data Card) 필수 항목
| 항목 | 내용 |
|------|------|
| 데이터셋 ID·버전 | DS-{유형}-{버전}-{날짜} |
| 출처 | 기관명, 공개 데이터셋명, 수집 기간 |
| 윤리 승인 번호 | IRB No. 또는 면제 근거 |
| 비식별화 방법 | DICOM de-id 프로파일, 도구명 |
| 포함/배제 기준 | 질환, 연령, 영상 모달리티 등 |
| 분포 통계 | 총 건수, 클래스 비율, 인구통계 분포 |
| 라벨링 방법 | 라벨러 수, 자격, 합의 프로토콜, κ 값 |
| 분리 방법 | Train/Val/Test 비율, 분리 단위(환자/영상) |
| 알려진 한계 | 편향 요인, 대표성 부족 영역 |

## 7. 역할 및 책임
| 역할 | 책임 |
|------|------|
| 데이터 관리자(Data Steward) | 수집·비식별화·버전관리·접근제어 |
| AI/ML 엔지니어 | 전처리·분리·편향분석·모델 학습 |
| 의료전문가(라벨러) | 라벨링·불일치 해소·임상 타당성 검토 |
| 품질보증(QA) | 데이터 카드 검토·감사, SOP 준수 확인 |
| 위험관리 담당 | 데이터 편향 → 위험 평가 연계 |

## 8. 프로젝트 내 연계
- 03_설계_개발관리/AI_구성요소_단위_성능평가.md — 시험 데이터셋 기반 성능 지표
- 03_설계_개발관리/SOP-AIGOV-001_AI_공정성_설명성_드리프트_거버넌스.md — 편향·드리프트 관리
- 07_위험관리_ISO14971/ISO14971_프로세스_상세.md — 데이터 편향 위험 항목
- 02_품질경영시스템_QMS/디지털의료기기_GMP_적합판정_신청_패키지.md — 서류 #16, #17

## 9. 참고 자료
- [Johner AI Guideline (GitHub)](https://github.com/johner-institut/ai-guideline)
- [FDA GMLP 10 Principles](https://www.fda.gov/medical-devices/software-medical-device-samd/good-machine-learning-practice-medical-device-development)
- [MDCG 2025-6 AI-Powered Medical Devices](https://www.kiwa.com/en/insights/stories/aib-2025-1-mdcg-2025-6--a-guiding-document-for-ai-powered-medical-devices/)
