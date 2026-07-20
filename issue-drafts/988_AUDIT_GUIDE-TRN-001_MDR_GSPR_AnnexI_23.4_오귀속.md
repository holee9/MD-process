---
title: "audit(factuality): GUIDE-TRN-001 frontmatter 'EU MDR GSPR Annex I §23.4' 를 인력 역량/교육 근거로 오귀속 — §23.4는 '사용설명서(IFU) 기재사항'(라벨링) 조항으로 인력 역량과 무관"
labels: "audit:factuality,prio:P1,risk:medium"
state: closed
---

## 대상 (C1×10_교육_훈련 전수 스윕)

- `10_교육_훈련/GUIDE-TRN-001_역량평가_교육니즈_매트릭스.md` frontmatter L12
  - `applicable: ... EU MDR 2017/745 Art.10(9), GSPR Annex I §23.4 ...`
  - 본문 목적(§1)은 "품질에 영향을 미치는 업무를 수행하는 인원"의 역량·교육·훈련 체계(ISO 13485 §6.2 기반)를 다루는 문서로, 문서 전체 주제가 **인력 역량평가·교육니즈 매트릭스**임.

## 결함

EUR-Lex Regulation (EU) 2017/745 Annex I 원문(Consolidated text 02017R0745-20230320) 직접 대조 결과, **Chapter III, Section 23 "Label and instructions for use"**이며 **23.4 "Particulars in instructions for use"**는 사용설명서(IFU)에 기재해야 할 항목(23.2 각 항목 중 (a)(c)(e)(f)(k)(l)(n)(r) 인용, 임상적 이익, SSCP 링크, 심각한 사고 보고 안내 등)을 규정하는 조항이다. **제조사 내부 인력의 역량·교육·훈련과는 무관**하다.

GUIDE-TRN-001은 인력 역량평가 가이드 문서의 frontmatter "applicable"(적용 규제) 목록에 §23.4를 포함시켜, 마치 본 조항이 인력 역량 요건의 근거인 것처럼 오귀속하고 있다. MDR상 인력 역량 관련 요구는 GSPR(Annex I)이 아니라 QMS 영역(Annex IX 등) 및 PRRC(Art.15)에서 다루어지며, 본 저장소의 다른 문서(SOP-TRN-001 등)는 ISO 13485 §6.2를 정확히 인용하고 있어 GUIDE-TRN-001의 §23.4 인용만 이질적이다.

이는 기존 audit #950(GSPR §19 EMC 오인용 — 비이식형 기기에 능동이식형 기기 조항 오적용)과 유사한 "GSPR 조항 topically 불일치" 오류 클래스이다.

## Tier1 근거

EUR-Lex (https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02017R0745-20230320) Annex I 목차 직접 열람 — "23. Label and instructions for use" 표제 및 하위 "23.4 Information in the instructions for use" 조항 내용(사용설명서 기재사항 목록) 직접 확인.

## 판정

**P1, audit:factuality/citation.** frontmatter 수준의 근거 오귀속으로 문서 본문 요구사항 자체에는 영향 없으나, 규제 근거 목록의 신뢰성 문제 및 향후 GSPR 체크리스트류 문서와의 교차참조 오류 유발 가능성. 감사관 본문 미수정(이슈 등록만). 실운영 문서 미참고.

## 권고

frontmatter applicable 목록에서 "GSPR Annex I §23.4"를 제거하거나, 인력 역량 관련 근거로는 "ISO 13485:2016 §6.2", "EU MDR Art.15(PRRC)" 등으로 대체.

## 참고 (추가 발견, 별도 등록 없이 향후 C4 사이클 후보로 기록)
- GUIDE-TRN-001 및 09/10 카테고리 다수 문서가 "진단용 방사선 발생장치의 안전관리에 관한 규칙(제1122호)"를 최신 버전으로 인용하나, law.go.kr 확인 결과 **현행 버전은 보건복지부령 제1185호(2026-07-09 시행)**로 제1122호(2025-07-18 시행)보다 최신 개정본이 존재함 — C4(발효/시행일) 전수 스윕 시 저장소 전체 "제1122호" 인용 재검토 필요.

## 참고
- Tier1: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02017R0745-20230320 (Annex I §23)
- 계보: audit #950 (동일 오류클래스 — GSPR 조항 topically 불일치)
