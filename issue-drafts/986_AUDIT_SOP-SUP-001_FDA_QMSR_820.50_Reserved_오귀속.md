---
title: "audit(factuality): SOP-SUP-001 FDA QMSR §820.50 (Purchasing controls) 오귀속 — 현행 QMSR에서 §820.50은 [Reserved], 구매통제는 §820.10(c)→ISO 13485 §7.4로 편입 (audit #951/#967/#972 동일 오류클래스 자매재발)"
labels: "audit:factuality,prio:P0,risk:high"
state: closed
---

## 대상 (C1×09_공급자_관리 전수 스윕)

- `09_공급자_관리/SOP-SUP-001_공급자_감사_재평가_절차.md`
  - frontmatter L13: `FDA QMSR §820.50 (Purchasing controls)`
  - L77: `| FDA QMSR | §820.50(a) | 공급자 선정기준, 평가·재평가 기록 (ISO 13485 §7.4 참조 편입) |`
  - L78: `| FDA QMSR | §820.50(b) | 구매문서 품질 요건 및 수립 절차 |`
  - L481-482 (규제 매핑표): `FDA QMSR §820.50(a)/(b)` → `ISO 13485 §7.4.1/§7.4.2 충족으로 대응`

## 결함

eCFR 21 CFR Part 820 현행 목차(Tier1, 89 FR 7523, 2026-02-02 시행 QMSR 기준, 조회일 2026-07-20 as of 7/16/2026) 직접 확인 결과, Part 820의 **현재 실재 조항은 §820.1·§820.3·§820.7·§820.10(Subpart A) 및 §820.35·§820.45(Subpart B)뿐**이다. §820.20-820.30, §820.40은 [Reserved]이며 **Subparts C-O(§820.50 포함 구 QSR 조항 전체) 역시 전부 [Reserved]**로 전환되었다 — 즉 §820.50(구 QSR "Purchasing controls")은 현재 존재하지 않는 조항이다.

문서는 이를 마치 현행 활성 조항인 것처럼 §820.50(a)/(b) 하위항목까지 구체적으로 인용하고 있으나, 실제로 구매통제 요건은 **§820.10(c) 경로를 통해 ISO 13485:2016 §7.4로 전면 편입**되었다(문서 자체의 "ISO 13485 §7.4 참조 편입" 서술은 방향은 맞으나, 근거 조항번호를 존재하지 않는 §820.50(a)/(b)로 특정한 것이 오류).

이는 앞선 스윕에서 반복 확인된 동일 오류 클래스다:
- audit #951(01카테고리): FDA_QMSR_2026 §820.30 Reserved 혼동
- audit #967(04카테고리): 구 QSR 조항 현행 인용 6문서 ~13개소
- audit #972(05카테고리): 검사개요 §820.70(i)/§820.180(c) 현행 미존재 조항 인용

09_공급자_관리 카테고리에서 동일 패턴이 잔존/미전파 확인됨.

## Tier1 근거

eCFR (https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820) Table of Contents 직접 열람 — "Part 820 Quality Management System Regulation, 820.1–820.45" 범위 명시, "§820.50" 개별 페이지 접근 시 404, Subpart 목록상 Subparts C-O 전체 [Reserved] 확인. Source: 89 FR 7523 (2026-02-02).

## 판정

**P0, audit:factuality/citation.** 실사·심사 대응 SOP 근거란에 현재 존재하지 않는 조항번호가 구체 하위항목((a)/(b))까지 명시되어 있어 규제기관 대응 시 신뢰성 문제 소지. 감사관 본문 미수정(이슈 등록만). 실운영 문서 미참고.

## 권고

frontmatter 및 L77/L78/L481-482의 "FDA QMSR §820.50(a)/(b)" 표기를 "FDA QMSR §820.10(c) → ISO 13485:2016 §7.4 참조편입"으로 정정.

## 참고
- Tier1: https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820
- 계보: audit #951, #967, #972 (동일 오류클래스)
