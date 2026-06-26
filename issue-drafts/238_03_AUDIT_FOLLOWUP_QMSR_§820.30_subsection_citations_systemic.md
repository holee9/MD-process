---
title: "[AUDIT-FOLLOWUP P1] QMSR §820.30(f)/(g)/(i)/(j) subsection-letter 인용 사내 전반 잔존 — Reserved 사실과 불일치, ISO 13485:2016 §7.3 하위절로 일괄 전환 필요"
labels: "source:emergent,type:audit-followup,audit:citation,prio:P1,risk:high,규제,QMSR,설계관리"
state: open
parent-audit: [921]
---

## 배경
audit #921(2026-06-26) 종결 과정에서 SOP-AIGOV-001 frontmatter "FDA QMSR §820.30/ISO13485 §7.3"를 "§820.10(c) → ISO 13485:2016 §7.3 (incorporation by reference; §820.30은 Reserved)"로 정정하였으나, **동일한 §820.30 subsection-letter 인용 패턴이 사내 설계관리 SOP·Form·매트릭스 전반에 분산 잔존**함을 grep 점검에서 확인. eCFR 21 CFR Part 820(QMSR, 2026-02-02 시행) §820.30은 본문 전체가 Reserved이고, 설계관리 요구는 §820.10(c)가 ISO 13485:2016 §7.3을 incorporation by reference로 끌어오는 단일 경로로 일원화되었다.

## 잔존 인용 (grep 결과, 2026-06-27)

| 위치 | 현재 표기 | 정정 방향 (1차 출처: eCFR 21 CFR 820.10(c), §820.30 Reserved) |
|---|---|---|
| `03_설계_개발관리/F-DVV-001_설계검증_계획_결과서.md` line 11 frontmatter applicable | "FDA QMSR §820.30(f)" | "FDA QMSR §820.10(c) → ISO 13485:2016 §7.3.6 (설계 검증)" |
| `03_설계_개발관리/F-DVV-002_설계유효성확인_보고서.md` line 11 | "FDA QMSR §820.30(g)" | "FDA QMSR §820.10(c) → ISO 13485:2016 §7.3.7 (설계 유효성확인)" |
| `03_설계_개발관리/F-DVV-003_VV_역추적성_매트릭스.md` line 11 | "FDA QMSR §820.30(j) DHF" | "FDA QMSR §820.10(c) → ISO 13485:2016 §7.3.10 (설계개발 파일)" |
| `03_설계_개발관리/SOP-DHF-001_설계개발파일_관리.md` line 8 purpose | "FDA QMSR §820.30(j)" | "FDA QMSR §820.10(c) → ISO 13485:2016 §7.3.10" |
| `03_설계_개발관리/SOP-DHF-001` line 11 applicable | "FDA QMSR §820.30(j) (Design History File)" | "FDA QMSR §820.10(c) → ISO 13485:2016 §7.3.10 (DHF 개념 incorporation)" |
| `03_설계_개발관리/SOP-DHF-001` line 57 본문 | "FDA QMSR §820.30(j) DHF 요건" | 동일 방향 |
| `03_설계_개발관리/SOP-DHF-001` line 94 용어 | "DHF — FDA QMSR §820.30(j) 용어" | "DHF — 21 CFR 820 (구 QSR) §820.30(j) 용어, QMSR 시행으로 §820.10(c)를 통해 ISO 13485 §7.3.10로 이관" |
| `03_설계_개발관리/SOP-DHF-001` line 494 매핑표 | "FDA QMSR §820.30(j)" | "FDA QMSR §820.10(c) → ISO 13485 §7.3.10" |
| `03_설계_개발관리/SOP-DVV-001_설계개발_검증_및_유효성확인_절차.md` line 11 | "FDA QMSR §820.30(f)(g)(i) (2026-02-02 발효)" | "FDA QMSR §820.10(c) (2026-02-02 발효) → ISO 13485:2016 §7.3.6/§7.3.7/§7.3.9" |
| `03_설계_개발관리/SOP-DVV-001` line 31 본문 | "FDA QMSR §820.30(f)(g)" | 동일 방향 |
| `issue-drafts/203_03_SOP-DHF-001_설계개발파일_7.3.10.md` line 17 | "FDA QMSR §820.30(j)" | 동일 방향 (issue 본문) |
| `issue-drafts/214_03_SOP-DVV-001_*.md` line 10 | "FDA QMSR §820.30(f)(g)" | 동일 방향 |
| `issue-drafts/227_03_F-DHF-001_*.md` line 10, 18, 33 | "FDA QMSR §820.30(j)" 등 | 동일 방향 |

`00_프로젝트관리/문서_매트릭스.md` 의 §820.30 표기는 본 SOP/Form frontmatter에서 자동 생성되므로 위 frontmatter 정정 후 빌드 스크립트로 자동 갱신됨.

## 판정 근거 (Tier 1)
- eCFR — 21 CFR Part 820 (QMSR 현행): https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820
  - §820.30: "[Reserved]"
  - §820.10(c) Design and Development: "Manufacturers of class II, class III, and those class I devices listed shall comply with the requirements in Design and Development, Clause 7.3 and its Subclauses in ISO 13485."
- FDA QMSR FAQ: https://www.fda.gov/medical-devices/quality-management-system-regulation-qmsr/quality-management-system-regulation-frequently-asked-questions

## 판정
**인용부정확 (citation) — P1 / 위험도 high (사내 전반 파급)**
- audit #921 동일 오류 패턴이 설계관리 단일 SOP가 아닌 **DHF·DVV 영역 전체 SOP/Form**에 분포. QMSR 실사·심사 시 동일 지적이 다발 발생 가능.
- (구) QSR §820.30(f)(g)(i)(j) 표기는 1996년 QSR 본문에는 존재하나, **QMSR(2026-02-02 시행) 이후로는 §820.30 자체가 Reserved**이므로 현행 시점에서 단독 인용은 부정확.

## 권고 수정 (DoD)
1. 위 grep 표의 각 frontmatter `applicable:`에서 "§820.30(letter)" 단독 표기를 **"§820.10(c) → ISO 13485:2016 §7.3.x"** 형태로 일괄 변환(letter→hsub-clause 매핑은 표 우측 컬럼).
2. 각 SOP/Form 본문에서 §820.30(letter)를 직접 호출하는 문장은 "QMSR §820.10(c)가 ISO 13485:2016 §7.3.x(설계검증/유효성확인/이관/파일)를 incorporation by reference로 적용" 형태로 표현 전환.
3. 용어 정의(SOP-DHF-001 line 94 등)는 "(구) QSR §820.30(j) — QMSR 시행 후 §820.10(c)→ISO 13485 §7.3.10로 이관" 형태의 역사적 단서 보존.
4. issue-drafts 내 #203/#214/#227 본문도 동일 형식으로 수정(미해결 plan 이슈이므로 향후 SOP 작성 시점에 일관성 확보).
5. 빌드 스크립트로 `00_프로젝트관리/문서_매트릭스.md` 재생성(수동 편집 금지) — frontmatter 정정으로 자동 동기화 확인.
6. 정정 후 `12_교차검증_보고서/`에 §820.30 인용 검색 결과 0건 보고(역사적 단서 표기 제외).

## 수락 기준 (DoD)
- [ ] grep "QMSR §820.30(" 결과 = 0 (역사적 단서 또는 수정 이력 라인 제외)
- [ ] 각 frontmatter applicable에 "§820.10(c)" 명시
- [ ] 문서_매트릭스 자동 재빌드 후 §820.30 단독 표기 0건
- [ ] 본 이슈 close 커밋에 변경 파일 전체 enumerate

## 출처 (Tier 1)
- eCFR — 21 CFR Part 820 (QMSR): https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820
- FDA — QMSR 공식 페이지: https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr
- FDA — QMSR FAQ (Reserved 설명·incorporation by reference 경로): https://www.fda.gov/medical-devices/quality-management-system-regulation-qmsr/quality-management-system-regulation-frequently-asked-questions

## 비고
본 이슈는 audit #921 종결 직후 발견된 **emergent** 결함이며, 수정 범위가 다수 문서(SOP 2건 + Form 3건 + issue-drafts 3건 + 매트릭스 자동 재빌드)에 걸쳐 일관 정정이 필요하므로 **차기 실행에서 단일 변경집합으로 일괄 처리**한다. (단일 실행 내 부분 정정은 자매문서 간 일시적 불일치를 유발하므로 회피.)
