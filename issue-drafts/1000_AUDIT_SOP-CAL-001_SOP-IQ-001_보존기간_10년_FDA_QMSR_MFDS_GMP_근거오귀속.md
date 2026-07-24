---
title: "audit #1000 (citation): SOP-CAL-001 §5.7·SOP-IQ-001 §7 — 기록보존 '10년' 근거를 'FDA QMSR, MFDS GMP'로 기재하나 두 규정 모두 특정 연수 미규정(정답 근거는 EU MDR Art.10(8) 비이식형 10년으로 추정, 근거조항 오귀속/누락)"
labels: "audit:citation,prio:P1,risk:med"
state: open
---

## 대상 (C2×05_검사_시험_밸리데이션 스윕)

`05_검사_시험_밸리데이션/SOP-CAL-001_교정관리_절차.md` §5.7 기록 관리 표:

```
| 교정 기록서 (F-CAL-002) | 의료기기 수명 종료 후 10년 | FDA QMSR, MFDS GMP |
| OOT 영향평가서 (F-CAL-003) | 의료기기 수명 종료 후 10년 | SOP-NC-001 연계 |
```

`05_검사_시험_밸리데이션/SOP-IQ-001_설치검증_수용시험_절차.md` §7 기록 관리 표:

```
| F-IQ-001 설치검증 체크리스트 | 장비 수명 + 10년 | 전자/지류 | FDA QMSR, MFDS GMP |
| F-IQ-003 고객 인수 확인서 | 장비 수명 + 10년 | 전자/지류 | 계약 관리 |
| 부적합·재시험 기록 | 장비 수명 + 10년 | 전자 | SOP-NC-001 연계 |
```

(F-IQ-002는 "ISO 13485 §4.2.5"로 별도 기재 — 본 건 범위 밖, §4.2.5 자체는 연수 미규정 조항이라는 점은 기존 반복 확인 사항과 동일)

## 결함

eCFR 21 CFR 820.180(FDA QSR/QMSR 기록 일반요건, Tier1 원문 직접 확인)은 "records shall be retained for a period of time equivalent to the design and expected life of the device, but in no case less than 2 years from the date of release for commercial distribution" — 즉 **기기 설계수명 상당 기간, 최저 2년**만 규정하며 특정 "10년"이라는 고정 수치는 어디에도 없다. MFDS GMP(의료기기 제조 및 품질관리 기준) 역시 본 저장소 기존 감사이력(전 사이클 전체) 어디에서도 고정 "10년" 수치 확인 사례가 없다(웹서치로도 특정 연수 조항 미확인).

본 저장소의 다른 카테고리(04_제조공정_관리, 09_공급자_관리 등, audit #914/#963/#993/#995/#996 계보)에서는 동일한 "10년" 수치의 정확한 근거를 일관되게 **EU MDR Art.10(8)(비이식형 기기 10년)**로 명시해왔다. 그러나 05 카테고리의 두 문서는 수치는 우연히 정답과 같은 "10년"이면서도 근거란에는 EU MDR을 누락하고 대신 이를 규정하지 않는 "FDA QMSR, MFDS GMP"만 기재 — 근거조항 오귀속(citation misattribution) 결함이다. 값 자체(10년)는 EU MDR 기준으로는 우연히 정답과 일치하나, 표시된 근거로는 해당 수치를 도출할 수 없다.

## Tier1 근거

- eCFR 21 CFR 820.180 원문(본 사이클 WebSearch로 직접 확인): "period of time equivalent to the design and expected life of the device... not less than 2 years" — 고정 10년 수치 없음.
- EU MDR Art.10(8)(EUR-Lex) — 비이식형 10년/이식형 15년, 본 저장소 기확정 Tier1(#914/#963/#966에서 원문 대조 완료, 정확한 근거로 추정되나 05 카테고리 문서에는 누락).

## 판정

P1/risk:med. 수치 자체는 (우연히) EU MDR 비이식형 기준과 일치하여 실무상 즉각적 과소보존 위험은 낮으나, 근거로 명시된 규정이 실제로 해당 수치를 규정하지 않아 문서 신뢰성·추적성 결함이며, 향후 EU MDR 기준이 변경되거나 이식형 제품으로 확장될 경우 잘못된 근거를 따라가 오류가 전파될 위험이 있다.

## 미정정 (감사관 문서 미수정 원칙 — 이슈 등록만)

정정은 빌더/문서 소유자 조치 필요. 권고: "FDA QMSR, MFDS GMP" → "EU MDR Art.10(8)(비이식형); FDA QMSR/MFDS GMP는 최소 2년(제품수명) 원칙만 규정"으로 근거 명확화.

## 참고

- Tier1: eCFR 21 CFR 820.180(본 사이클 직접 확인), EUR-Lex Regulation (EU) 2017/745 Art.10(8)(기확보, #914/#963/#966 재사용).
- 계보(수치 자체 정답 10년 확립 이력): #914→#963→#993→#995→#996.
- 실운영 문서 미참고. web_verification: yes.
