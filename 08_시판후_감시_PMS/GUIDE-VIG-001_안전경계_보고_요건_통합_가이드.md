---
doc-id: GUIDE-VIG-001
title: "의료기기 안전경계(Vigilance) 보고 요건 통합 가이드"
type: Guide
version: v0.2
status: draft
category: 08_시판후_감시_PMS
purpose: MFDS·FDA·EU MDR 안전경계 보고 기한·기준·양식을 단일 문서로 통합하여 보고 누락 방지
applicable:
  - EU MDR 2017/745 Art.87-92
  - FDA 21 CFR 803 (MDR)
  - FDA 21 CFR 806 (Corrections and Removals)
  - MFDS 의료기기법 제31조 (부작용 등의 보고)
  - MFDS 의료기기 부작용 등 안전성 정보 관리에 관한 규정
  - ISO 13485:2016 §8.2.3
forms: [F-VIG-001, F-PMS-001, F-PMS-002]
related-docs: [SOP-PMS-001, SOP-FSCA-001, SOP-PSUR-001, PMS_개요]
related-issues: []
owner: RA/QA Lead
last-review: 2026-06-03
review-due: 2027-06-03
---

# 의료기기 안전경계(Vigilance) 보고 요건 통합 가이드

## 1. 목적 및 적용 범위

### 1.1 목적

본 가이드는 의료용 X-ray 시스템·디텍터·SW를 대상으로, MFDS·FDA·EU MDR 3개 규제 기관의 안전경계(Vigilance) 보고 요건을 단일 문서에서 비교·참조할 수 있도록 통합한다. 보고 의무자가 사고 발생 시 해당 시장별 보고 기한·양식·절차를 즉시 확인하여 지연·누락을 방지하는 것이 목적이다.

### 1.2 적용 범위

- **제품**: 의료용 X-ray 발생장치, 디지털 디텍터, 영상처리/선량관리 SW
- **시장**: 대한민국(MFDS), 미국(FDA), 유럽연합(EU MDR)
- **대상 사건**: 사망, 중상해, 공중보건 위협, 기기 오작동(malfunction), 현장안전시정조치(FSCA)

## 2. 용어 정의

| 용어 | 정의 | 비고 |
|------|------|------|
| Serious Incident | 사망 또는 건강 상태의 심각한 악화를 직·간접적으로 야기했거나 야기할 수 있었던 사건 | EU MDR Art.2(65) |
| MDR (Medical Device Report) | FDA에 제출하는 의무 부작용 보고 | 21 CFR 803 (FDA MDR ≠ EU MDR) |
| 부작용 보고 | MFDS에 제출하는 의료기기 부작용 등 안전성 정보 보고 | 의료기기법 제31조 |
| FSCA | Field Safety Corrective Action — 시판 후 안전 문제에 대한 시정 조치 | EU MDR Art.2(68) |
| FSN | Field Safety Notice — FSCA에 수반되는 사용자 통보 | EU MDR Art.89(8) |
| Trend Report | 통계적으로 유의미한 부작용 빈도 증가 경향 보고 | EU MDR Art.88 |

## 3. 규제 기관별 보고 요건 비교

### 3.1 보고 기한 매트릭스

| 사건 유형 | MFDS | FDA | EU MDR |
|-----------|------|-----|--------|
| **사망** | 15일 이내 | 30 calendar days | 10 calendar days |
| **중상해** | 15일 이내 | 30 calendar days | 15 calendar days |
| **중상해 — 즉각 위험** | 15일 이내 | 5 work days (FDA 요청 시) | 2 calendar days (Initial) |
| **공중보건 위협** | 15일 이내 | — | 2 calendar days (Initial) |
| **오작동 (사망·중상해 가능)** | 15일 이내 | 30 calendar days | 15 calendar days |
| **Trend (경향 보고)** | — | — | 15 calendar days (Art.88) |
| **FSCA/리콜** | 즉시 보고 | 10 work days (21 CFR 806) | 별도 FSCA 보고 (SOP-FSCA-001) |

### 3.2 보고 의무자

| 규제 | 보고 의무자 | 비고 |
|------|------------|------|
| MFDS | 제조업자, 수입업자, 수리업자 | 의료기기법 제31조 |
| FDA | Manufacturer, Importer, User Facility | 21 CFR 803.10-803.50 |
| EU MDR | Manufacturer (EC REP 경유 가능) | Art.87(1), Art.11(3)(d) |

### 3.3 보고 채널

| 규제 | 시스템 | URL/접수처 |
|------|--------|-----------|
| MFDS | 의료기기 부작용 보고 시스템 | https://emed.mfds.go.kr |
| FDA | MedWatch / eMDR (electronic MDR) | https://www.fda.gov/safety/medwatch |
| EU MDR | EUDAMED Module 5 (개발 중) → 현재 CA 직접 보고 | 각 Member State CA |

> **주의**: EUDAMED Module 5 (Vigilance) 미시행 상태(2026-06-03 현재). EU 안전경계 보고는 해당 시장국 CA(Competent Authority)에 직접 제출. Module 5 의무화 시점 미정.

## 4. X-ray 의료기기 특수 고려사항

### 4.1 방사선 관련 사건

| 사건 유형 | 예시 | 추가 보고 의무 |
|-----------|------|---------------|
| 과선량 노출 | SW 오류로 설정값 초과 노출 | MFDS: 방사선 사고 보고 (원안위 병행), FDA: MDR + Radiation Control, EU: Serious Incident |
| 선량 표시 오류 | DAP/DLP 계산 오류 | SW 오작동으로 분류 → 기기 오작동 보고 기준 적용 |
| 이미지 품질 저하 | 디텍터 결함으로 진단 불가 이미지 | 진단 지연 → 건강 악화 가능 → 보고 기준 충족 가능 |
| 사이버보안 사건 | 랜섬웨어로 시스템 중단 | FDA: 21 CFR 806 + Section 524B, EU: Serious Incident 해당 가능 |

### 4.2 SW 관련 사건 분류 기준

IEC 62304 Safety Classification 기반 SW 이상이 보고 대상인지 판단:

1. **Class C SW 이상** → 사망·중상해 가능 → 모든 규제 기관 보고 대상
2. **Class B SW 이상** → 경미한 상해 가능 → 오작동 보고 기준 평가
3. **Class A SW 이상** → 상해 가능성 낮음 → 보고 비대상 (단, trend 모니터링 대상)

## 5. 보고 프로세스 통합 흐름

```
사건 인지 (Day 0)
    │
    ├──[1] 사건 기록 (F-PMS-001)
    │
    ├──[2] 초기 평가 (24h 이내)
    │      ├── 보고 대상? → Yes/No
    │      ├── 심각도 분류: 사망/중상해/오작동/기타
    │      └── 해당 시장 식별: MFDS/FDA/EU
    │
    ├──[3] 규제 기관별 초기 보고
    │      ├── EU: 2일(즉각위험) / 10일(사망) / 15일(중상해·오작동)
    │      ├── MFDS: 15일
    │      └── FDA: 30일 (5 work days if requested)
    │
    ├──[4] 조사 및 근본원인 분석
    │      ├── CAPA 연계 (SOP-CAPA 참조)
    │      └── 추가 시험·분석 수행
    │
    ├──[5] 후속 보고 (Final Report)
    │      ├── EU: 최종보고 기한 없음 (CA 협의)
    │      ├── MFDS: 추가 정보 제출 (요청 시)
    │      └── FDA: Supplemental Report (30일 이내)
    │
    └──[6] FSCA 필요 시 → SOP-FSCA-001 개시
           ├── FSN 작성·배포
           ├── 시정조치 실행
           └── FSCA 종결 보고
```

## 6. 보고 기록 및 보존

| 항목 | 요건 |
|------|------|
| 보고 기록 보존 기간 | MFDS: 5년, FDA: 2년(제조)/3년(수입), EU: 10년(Class III)/15년(임플란트) |
| 기록 매체 | 전자 기록 허용 (21 CFR Part 11 / EU MDR Annex II §4 준수) |
| 추적 대장 | 모든 안전경계 사건에 대해 고유 번호 부여, 진행 상태 추적 |
| 경영진 보고 | 사망·중상해 사건은 경영진 즉시 보고 (Management Review 연계) |

## 7. 관련 양식

| 양식 ID | 명칭 | 용도 |
|---------|------|------|
| F-PMS-001 | 고객 불만 접수/처리 기록서 | 초기 사건 접수 |
| F-PMS-002 | 부작용 보고서 | MFDS 보고용 |
| F-VIG-001 | 안전경계 사건 추적 대장 | 사건별 보고 상태·기한 추적 |

## 8. 교육 요건

본 가이드 관련 교육 대상 및 주기:

| 대상 | 교육 내용 | 주기 |
|------|-----------|------|
| RA/QA 담당 | 전 규제 기관 보고 요건, 기한, 양식 | 신규 + 연 1회 |
| 서비스 엔지니어 | 사건 인지·초기 보고 절차 | 신규 + 연 1회 |
| 경영진 | 보고 의무 개요, 법적 책임 | 연 1회 |
| 영업/고객 지원 | 불만 접수 → RA 에스컬레이션 절차 | 신규 + 연 1회 |

## 9. 개정 이력

| 버전 | 일자 | 변경 내용 |
|------|------|-----------|
| v0.1 | 2026-06-03 | 초안 작성 — MFDS/FDA/EU MDR 보고 기한·기준 통합 |
| v0.2 | 2026-06-03 | X-ray 특수 고려사항, SW 사건 분류 기준, 보고 프로세스 흐름도 보강 |
