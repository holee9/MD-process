---
title: "audit #1028 (citation/C3): GUIDE-SQA-001 §참고문헌 — AAMI TIR36:2007 표제 오귀속('Supplier Quality Agreement 가이드') + 철회(2020-04-10) 미표기"
labels: "audit:citation,prio:P1,risk:medium"
state: closed
gh-issue: 1706
---

## 결함 (C3×09_공급자_관리 전수 스윕, 2026-08-10 등록 — GH#1706)

`09_공급자_관리/GUIDE-SQA-001_품질합의서_작성지침.md` L558: "AAMI TIR36:2007 (Supplier Quality Agreement 가이드)".

## Tier1 (2026-09-09 직접 재확인)

- 공식 표제는 **AAMI TIR36:2007 *Validation of software for regulated processes***(ANSI webstore·AAMI 계열 복수 공식 채널 일치). "Supplier Quality Agreement 가이드"라는 표제·주제의 문서가 아님.
- 적용범위: 기기 설계·시험·부품수락·제조·라벨링·포장·유통·불만처리 등 **품질시스템 자동화 SW 및 21 CFR Part 11 전자기록 시스템의 밸리데이션**. 의료기기의 구성품·부속품 SW 또는 SW 자체가 의료기기인 경우는 **적용 제외**.
- **추가 확인(신규)**: 본 TIR은 **2020-04-10 철회(withdrawn)** — 등록 당시 미기재 사항으로, 표제 오귀속에 더해 currency 결함 동반.

## 수정 (2026-09-09, 드레인 스프린트)

- `GUIDE-SQA-001` L558 → 정식 표제 병기 + "SQA 작성 가이드가 아님" 명시 + "2020-04-10 철회" 부기 + 사용 범위를 "공급자 제공 자동화 SW/전자기록 시스템 밸리데이션 합의 항목 참고자료"로 한정 (v0.2.2).
- **동일 오류클래스 전 저장소 일괄점검**(표준·TIR 표제 오귀속, #1011/#1012/#1022/#1028 계보): grep(`TIR36`) 전수 — 타 출현은 감사 원장·로그뿐, 실문서 잔존 0건.

실운영 문서 미참고. web_verification: yes(ANSI webstore 표제·적용범위·철회일, AAMI 계열 채널 교차확인).
