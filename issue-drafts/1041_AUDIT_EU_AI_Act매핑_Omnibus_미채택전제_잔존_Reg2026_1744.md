---
title: "audit(currency): EU_AI_Act_MDR_중첩적용_매핑 — Omnibus '미채택·관보 미게재' 전제 잔존, 실제로는 Regulation (EU) 2026/1744 발효(2026-07-27). 시나리오 (B) baseline 지시가 사실과 반대"
labels: "audit:currency,audit:factuality,prio:P0,risk:high,regulatory,ai-act"
opened: 2026-09-10
state: closed
---

## 대상 (C4×01_법규_규제 전수 스윕 — 발효/시행일 클래스)

`01_법규_규제/04_유럽_MDR/EU_AI_Act_MDR_중첩적용_매핑.md` (v0.8, last-review 2026-06-27)

| # | 라인 | 현재 기재 |
|---|---|---|
| 1 | L61 | `2026-08-02→2028-08-02` \| High-risk 조항 본격 적용(**Omnibus 잠정 합의 시** MDR/IVDR 탑재형은 2028-08-02로 이동) |
| 2 | L64 | "**2026-08-02부터 High-risk 의무가 본격 적용**되나, … Art. 6(1) 경로는 **2027-08-02**까지 과도기" |
| 3 | L66 | "**정식 채택은 2026년 6월, 관보 게재는 7월로 예상**된다(2026-06-13 확인 — **미완료 확인**). 단, **정식 채택 전까지 기존 일정(2026-08-02 / 2027-08-02)을 구속력 있는 기준선(baseline)으로 간주**하고 대비할 것" |
| 4 | L205·L207 | "시나리오 분기: (A) 관보 게재 완료 → 연기 적용 / (B) 미완료 → 기존 일정(2026-08-02) 유지. **현재 baseline은 (B)** — 2026-06-20 시점 Omnibus 관보 게재 미확인" |
| 5 | L192·L248·L252 | "Enforcement 적용일까지 **D-36**(2026-08-02)" / KPI "2026-08-02 기준" / §12.5 "적대적 자기검토 (**D-36 관점**)" |

## 결함

**Omnibus는 이미 정식 채택·관보 게재·발효되었다.** 본 문서가 "미완료"를 전제하고 시나리오 (B)를 구속력 있는 baseline으로 지시하는 것은 현시점(2026-09-10) 사실과 **반대**이다.

### Tier1 근거 — EUR-Lex 원문 메타데이터 직접 열람

> **Regulation (EU) 2026/1744** of the European Parliament and of the Council **of 8 July 2026** amending Regulations (EU) 2024/1689, (EU) 2018/1139 and (EU) 2023/1230 as regards the simplification of the implementation of harmonised rules on artificial intelligence (**Digital Omnibus on AI**)
> `eli:date_document: 2026-07-08` · `eli:first_date_entry_in_force: 2026-07-27` · CELEX `32026R1744`
> — https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng

- 관보(OJ) 게재: **2026-07-24**
- 발효: **2026-07-27** (게재 후 3일째 — AI Act 일반 적용일 2026-08-02 직전 긴급 발효)
- 결과: **고위험 의무 적용일 연기 확정** — 독립형(Annex III) **2027-12-02**, MDR/IVDR 등 규제제품 탑재형(Annex I, **자사 X-ray AI 모듈 해당**) **2028-08-02**.

### 영향

1. **시나리오 (A)가 확정**되었음에도 문서는 (B)를 baseline으로 지시 → 규제 대비 우선순위·자원배분 판단이 사실과 어긋난 전제 위에 놓임.
2. "D-36(2026-08-02)" 기준 D-day 표·KPI(§12.1~§12.5)는 **기준일이 이미 경과**하여 운영 지표로서 무효.
3. L61 "Omnibus **잠정 합의 시**" 조건부 표기는 확정 사실을 미확정으로 기술 — C4(발효/시행일) 클래스 정면 결함.
4. L64 "Art. 6(1) 경로 **2027-08-02**까지 과도기"는 Omnibus 개정 전 조문 기준으로, 개정 후 일정과 대조 필요.

**정확 유지 항목(PASS, 정정 대상 아님)**: AI Act 발효 2024-08-01, Chapters I·II 적용 2025-02-02(Art.113(a)), GPAI 2025-08-02, 일반 적용일 2026-08-02(Art.113 chapeau) — Omnibus는 이들 일자를 변경하지 않음. 2026-05-07 trilogue 잠정 합의 기술도 정확.

## 판정

**P0 / risk:high** — 자사 X-ray AI 영상분석 모듈의 고위험 의무 적용 시점이 **2026-08-02 → 2028-08-02**로 이동한 확정 사실을 문서가 반영하지 못하고, 오히려 구(舊) 일정을 "구속력 있는 기준선"으로 지시하고 있음.

**정정 권고**
- §3 일정표·단서를 Regulation (EU) 2026/1744(2026-07-08 채택 / OJ 2026-07-24 / 발효 2026-07-27) 기준으로 재작성, "예상·미완료·잠정 합의 시" 조건부 표현 전량 제거.
- §12.2 시나리오 분기를 **(A) 확정**으로 종결, (B) 트랙 삭제.
- §12 D-day/KPI 기준일을 신규 마일스톤(Annex I 2028-08-02)으로 재설정.
- Omnibus가 신설한 Art.5 금지관행 추가분(AI 생성 비동의 성적 이미지·CSAM) 반영 여부 별도 검토.

## 참고

- Tier1: EUR-Lex CELEX 32026R1744 원문 메타데이터 직접 열람(date_document·first_date_entry_in_force).
- 독립 교차확인(Tier2, 범위 확인 목적만): White & Case, Hunton, Mayer Brown, lawandtechnology.eu — OJ 게재 2026-07-24 / 발효 2026-07-27 일관.
- 실운영 문서 미참고: 확인. web: ok.

## 종결 (2026-09-11, 드레인 스프린트 — 빌더 정정 완료)

- **Tier1 재확인(감사자 출처 직접 재검증)**: EUR-Lex `https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng` 직접 열람 — `meta-eli:date_document: 2026-07-08`, `meta-eli:first_date_entry_in_force: 2026-07-27`, CELEX `32026R1744`, 표제 "…of 8 July 2026 amending Regulations (EU) 2024/1689, (EU) 2018/1139 and (EU) 2023/1230 … (Digital Omnibus on AI)" 확인. OJ 게재 2026-07-24·발효 2026-07-27 및 연기 일정(Annex III 2027-12-02 / Annex I 2028-08-02) 독립 교차확인.
- **정정 반영(`EU_AI_Act_MDR_중첩적용_매핑.md` v0.8→v0.9)**: §3 일정표에 발효(2026-07-27)·Annex III(2027-12-02)·Annex I(2028-08-02) 행 신설, 종전 "2026-08-02→2028-08-02(잠정 합의 시)" 조건부 행 및 "2027-08-02 과도기 종료" 행 대체. §3 주의문 재작성. ⚠️ Omnibus 동향 단서를 ✅ 확정 단서로 전면 교체("예상·미완료·잠정 합의 시" 표현 전량 제거, 종전 baseline 지침 폐지 명시). §12 제목·현재위치 재작성(enforcement 기준일 경과 반영), §12.1 SLA D-day→즉시, §12.2 (A)/(B) 분기 종결·(B) 트랙 삭제·기준일 2028-08-02 재설정, §12.3 D-day 역산표→착수일 기준 주차표, §12.4 KPI 기준일 재설정, §12.5 자기검토 문항 교체. frontmatter `applicable`·§9 출처에 Reg. (EU) 2026/1744 추가, last-review 2026-09-11.
- **동일 오류 클래스 일괄 교정(proactive)**: 저장소 전수 grep("Omnibus")로 자매 결함 1건 확인·동반 정정 — `03_설계_개발관리/SOP-AIGOV-001_...md` §3.1이 "Digital Omnibus 패키지 **제안**"으로 미확정 기술하던 부분을 Reg. (EU) 2026/1744 확정으로 정정하고, embedded(Annex I) '당초 일정'을 2026-08-02→**2027-08-02(AI Act Art.113(c))** 로 정정. 일일리서치로그·교차검증보고서의 Omnibus 언급은 **일자 고정된 시점 기록물**이므로 소급 수정 대상에서 제외(기록 무결성 원칙).
- **미해결 잔여(사실오류 아님)**: Omnibus 신설 Art.5 금지관행 추가분의 자사 해당 여부 — 문서에 검토 항목으로 명기, 별도 후속.
- 실운영 문서 미참고. web_verification: ok(EUR-Lex Tier1 직접 열람).
