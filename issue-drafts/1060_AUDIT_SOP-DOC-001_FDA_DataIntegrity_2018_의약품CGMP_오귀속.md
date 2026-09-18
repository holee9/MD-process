---
title: "audit #1060 (factuality/오귀속): SOP-DOC-001 L164 'FDA Data Integrity Guidance 2018' — 실체는 의약품 CGMP(21 CFR 210/211) 대상 가이던스, 의료기기 QMS 기록 근거로 무조건 귀속"
labels: "audit:factuality,prio:P2,risk:low,regulatory,FDA"
state: open
created: 2026-09-19
created-by: md-process-auditor
related-issues: [1052, 1030, 1028, 1022, 1021, 1011]
sweep: "C4 x 06_문서_기록관리 (부수 적출 — 클래스 외)"
---

## 결함

`06_문서_기록관리/SOP-DOC-001_문서_기록관리_절차.md` L164 §6.2.1:

> 모든 품질기록은 **ALCOA+ 원칙**을 준수하여야 한다 (FDA Data Integrity Guidance 2018 참조).

해당 명칭의 2018년 FDA 가이던스 실체는 **"Data Integrity and Compliance With Drug CGMP: Questions and Answers"**(Final, Federal Register **2018-26957**, 2018-12-13 게재)로, 적용 대상이 **의약품 CGMP(21 CFR Parts 210·211·212)** 이다. 의료기기(21 CFR 820 / QMSR)를 규율하지 않는다.

## 판정

- **발행연도 2018 자체는 정확 → C4 PASS.**
- **적용범위 오귀속은 확정 결함**: 의료기기 QMS 기록관리 SOP가 약사 영역 가이던스를 무한정·무조건적 준수근거로 제시. ALCOA+ 자체는 범분야 데이터무결성 원칙으로 채택에 문제 없으나, **근거 문서의 적용범위를 밝히지 않은 인용**은 심사 시 근거 불성립 지적 소지.
- 무관·영역불일치 조항/문서 오귀속 클래스 **7차 자매재발**(#1011 · #1021 · #1022 · #1028 · #1030 · #1052에 이어).

## 권고

`(FDA "Data Integrity and Compliance With Drug CGMP: Q&A", 2018-12 — 의약품 CGMP 대상이나 데이터무결성 원칙을 자사 정책으로 준용)` 형태로 적용범위 병기, 또는 MHRA GxP Data Integrity Guidance(2018) 등 범분야 근거로 교체.
