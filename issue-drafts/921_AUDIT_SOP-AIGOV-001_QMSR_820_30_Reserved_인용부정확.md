---
title: "[AUDIT P1] SOP-AIGOV-001 v0.3 — applicable 'FDA QMSR §820.30/ISO13485 §7.3' 인용부정확 (§820.30은 QMSR에서 Reserved)"
labels: "audit:citation,prio:P1,risk:medium"
state: closed
closed-date: 2026-06-27
close-commits: ["TBD-this-execution"]
---

## 대상 문서
- `03_설계_개발관리/SOP-AIGOV-001_AI_공정성_설명성_드리프트_거버넌스.md` v0.3 (last-review: 2026-06-08)

## 감사 주장

frontmatter `applicable:` 목록이 설계관리 근거를 **"FDA QMSR §820.30/ISO13485 §7.3"** 로 기재.

대표 인용:
- frontmatter Line 10: `applicable: [ISO 13485:2016 §7.3, **FDA QMSR §820.30/ISO13485 §7.3**, ISO 14971:2019, ...]`

(§3.2 본문 표는 ISO 13485 §7.3.2~§7.3.9 하위절을 사용해 정확히 매핑하므로, **결함은 frontmatter `applicable:` 인용 부분에 한정**된다.)

## 독립 확인 결과 — 1차 출처 (Tier 1)

FDA QMSR(2026-02-02 시행, 21 CFR Part 820 개정) eCFR 원문:
- **§820.30 (Design controls) — Reserved** (조항 본문 제거, ISO 13485:2016 §7.3 by reference로 대체)
- **§820.10(c)** — Manufacturers shall comply with the requirements of ISO 13485:2016 Clause 7.3 and its subclauses (설계관리 요구를 §820.10(c) 가 incorporation by reference 로 끌어옴)

| 사항 | 문서 기재 | Tier 1 정답 |
|---|---|---|
| QMSR 설계관리 조항 인용 | "FDA QMSR §820.30/ISO13485 §7.3" | **§820.30은 Reserved (조항 본문 없음)** — QMSR 설계관리는 **§820.10(c) → ISO 13485:2016 §7.3** 경로로 인용 |

## 판정
**인용부정확 (citation) — P1**
- §820.30이 QMSR에서 Reserved 처리되어 본문이 존재하지 않으므로, "§820.30/ISO13485 §7.3" 표기는 1차 출처와 일치하지 않는다.
- 사실 자체(설계관리가 ISO 13485 §7.3로 통합됨)는 옳으나, **조항번호 매핑이 잘못된** 인용. QMSR 실사 시 인용 표기 부정확으로 지적될 가능성.
- 본 SOP는 사내 자매문서 `FDA_QMSR_820.35_vs_ISO13485_4.2.5.md` v0.3과 `FDA_QMSR_2026.md` v0.3가 QMSR §820 구조 정정(audit #915~#917)을 받은 직후 작성된 문서로, 동일 구조 정정이 본 SOP까지 전파되지 않은 패턴.

## 권고 수정
1. frontmatter `applicable:` —
   - 변경 전: `FDA QMSR §820.30/ISO13485 §7.3`
   - 변경 후: **`FDA QMSR §820.10(c) → ISO 13485:2016 §7.3`** (또는 `FDA QMSR §820.10(c) (incorporation by reference) — ISO 13485:2016 §7.3`)
2. §3.2 헤더 또는 도입문에 "QMSR는 §820.30을 Reserved 처리하고 ISO 13485:2016 §7.3를 incorporation by reference로 적용" 단서 1줄 추가.
3. 사내 자매문서 SOP-DHF-001, SOP-DT-001, SOP-DVV-001 등 설계관리 인용 일괄 점검(파급 확인).

## 출처 (Tier 1)
- eCFR — 21 CFR Part 820 (QMSR 현행): https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820
- FDA — Quality Management System Regulation (QMSR) 공식 페이지: https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr
- FDA — QMSR FAQ (Reserved subparts 설명): https://www.fda.gov/medical-devices/quality-management-system-regulation-qmsr/quality-management-system-regulation-frequently-asked-questions

## Tier 2 (보조)
- BSI Compliance Navigator "The New FDA 21 CFR Part 820 – QMSR" (Reserved 처리 설명, 범위 확인용)
