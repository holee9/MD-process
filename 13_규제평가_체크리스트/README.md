# 13_규제평가_체크리스트

본 폴더는 1차 구축 자료의 **인허가 충분성**을 자체 평가하기 위한 공식 체크리스트와 갭 분석 결과를 보관합니다.

## 파일 구성

- `<표준>.md` — 각 표준의 항목별 평가 체크리스트
- `_readiness_report.md` — 자동 생성 갭 분석 리포트 (수동 편집 금지)
- `주간_갭분석_YYYY-MM-DD.md` — 위클리 스케줄 산출
- `모의감사_시나리오.md` — 가상 감사관 질문 모음

## 표준 목록

| 파일 | 표준 | 항목 수 (예상) |
|------|------|---:|
| FDA_510k_RTA.md | FDA 510(k) RTA Checklist | ~80 |
| FDA_QMSR.md | 21 CFR Part 820 (QMSR) | ~120 |
| EU_MDR_Annex_II.md | EU MDR 2017/745 Annex II 기술문서 | ~75 |
| ISO_13485.md | ISO 13485:2016 §4~8 | ~95 |
| ISO_14971.md | ISO 14971:2019 위험관리 | ~35 |
| IEC_62304.md | IEC 62304 SW 안전등급 | ~50 |
| IEC_60601-2-54.md | IEC 60601-2-54:2022 X-ray | ~53 |
| MFDS_제조허가.md | MFDS 의료기기 제조허가 | ~40 |

## 운영 규칙

- 각 체크리스트 항목은 YAML 코드블록으로 작성 (id/source/clause/requirement/severity/evidence_type/applicable_keywords 필수)
- 표준 개정 시 해당 파일의 `last-review`·`review-due` 갱신, 변경분은 변경통제(SOP-CC-001) 절차
- `scripts/build_readiness.py` 가 이 폴더를 스캔하여 자동 갭 분석

자세한 평가 프레임: [`../00_프로젝트관리/Phase2_평가프레임.md`](../00_프로젝트관리/Phase2_평가프레임.md)
