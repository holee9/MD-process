---
title: "audit(factuality): ISO14971_프로세스_상세.md §3.7 표 — ISO 14971:2019 Clause 10 하위조항(10.1~10.4) 전체 시프트 오류"
labels: "audit:factuality,prio:P1,risk:medium"
---

## 대상 (C1×07_위험관리_ISO14971 전수 스윕)

`07_위험관리_ISO14971/ISO14971_프로세스_상세.md` L213-216 (§3.7 생산·시판후 활동 표)

> | 10.1 정보 수집 | PMS, PMCF, 불만, Vigilance, 문헌, 규제 경보 | 상시 | PMS |
> | 10.2 정보 검토 | 이전 추정과 비교, 새 위해요인 여부 | 분기 | QA/RA |
> | 10.3 조치 | 위험 재평가, 통제 변경, 기술문서 개정 | 사안별 | R&D/QA |
> | 10.4 CAPA 환류 | 근본원인 → 위험분석 갱신 → RMF 개정 | 사안별 | QA |

## 결함

ISO 14971:2019 Clause 10 "Production and post-production activities"의 공식 하위조항 구조는 다음 4개다(web 교차확인 — 영문 요약 복수 소스 + 슬로베니아어 국가채택판 병기 대조로 순서·주제 일치 확인):

- **10.1 General**
- **10.2 Information collection**
- **10.3 Review of information**
- **10.4 Actions**

문서는 "10.1=정보수집"(실제 10.2), "10.2=정보검토"(실제 10.3), "10.3=조치"(실제 10.4)로 **한 단계씩 밀려** 배정했고, 실제로는 존재하지 않는 별도 "10.4=CAPA 환류" 항목을 추가로 신설했다(10.4 Actions 안에 포함되어야 할 내용). 즉 10.1 "General"(총칙) 서브조항이 누락된 채 정보수집부터 10.1로 잘못 시작한 오프바이원(off-by-one) 오류.

## Tier1/근거

web_verification: yes — ISO 14971:2019 Clause 10 구조 관련 복수 독립 소스(영문 요약 자료 + 슬로베니아 국가표준 채택판 조항 제목 병기: "10.1 Splošno/General, 10.2 Zbiranje informacij/Information collection, 10.3 Pregled informacij/Review of information, 10.4 Ukrepi/Actions") 교차 일치 확인. 표준 원문 완전본 구매 미보유(우아한 저하) — 단 4단계 구조·순서·주제는 다수 독립 출처(공식 채택판 포함) 일치로 사실오류로 판정.

## 판정

P1. 감사관 본문 미수정. 실운영 문서 미참고.
