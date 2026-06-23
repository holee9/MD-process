---
title: "[AUDIT][P0] FDA_QMSR_820.35_vs_ISO13485_4.2.5 §820.35 하위항목 (a)(b)(c)(d) 구조 사실오류 — eCFR 본문과 불일치, 비실재 §820.35(d) Part 11 조항 신설"
labels: "audit:factuality,prio:P0,risk:high"
---

## 대상 문서
- `01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md` v0.2 §3.1~§3.4, §4 항목별 비교 요약 표

## 주장 (문서 기재값)
| 하위항목 | 문서 기재 주제 |
|---|---|
| §820.35(a) | MDR 기록 (불만+서비스 활동, 21 CFR 803 보고 결정 근거·미보고 사유) |
| §820.35(b) | UDI 기록 (21 CFR 830) |
| §820.35(c) | 기밀성 |
| §820.35(d) | 전자서명 (21 CFR Part 11) |

본 매핑을 근거로 §4 "항목별 비교 요약" 표 및 §5 SOP 갱신 권고 전체가 구성되어 있음.

## 정답 (Tier 1 — eCFR 현행본, Source: 89 FR 7523, Feb. 2, 2024; 2026-02-02 시행)

§820.35 Control of records — ISO 13485 §4.2.5에 추가로 다음 정보를 기록에 포함하도록 요구:

| 실제 하위항목 | 실제 주제 | 핵심 요구 |
|---|---|---|
| §820.35(a) | **Records of complaints** (불만 기록) | 21 CFR Part 803 보고 대상·조사 필요·자율 조사 불만에 대해 기기명·접수일·UDI/UPC·고발자 정보·불만 상세·시정조치·답변 등 7항목 기록 |
| §820.35(b) | **Records of servicing activities** (서비스 활동 기록) | 기기명·UDI/UPC·서비스일·수행자·서비스 내용·시험/검사 데이터 등 6항목 기록 |
| §820.35(c) | **Unique Device Identification** | 각 기기 또는 배치에 대해 UDI 기록 |
| §820.35(d) | **Confidentiality** | 제조자가 기밀로 표시한 기록의 FDA 공개 판단 보조 |

§820.35에는 **"전자서명/Part 11" 하위항목이 존재하지 않음**. 21 CFR Part 11(전자기록·전자서명)은 §820.35의 일부가 아니라 독립 규정이며, QMSR 본문은 Part 11을 §820.35에 편입하지 않았다.

## 문서 vs 정답 매핑 (오류 4건)

| 항목 | 문서 기재 | Tier 1 정답 | 판정 |
|---|---|---|---|
| §820.35(a) | MDR 기록 | Records of complaints (불만 기록) | **사실오류** — 조항 범위·주제 혼동 |
| §820.35(b) | UDI 기록 | Records of servicing activities (서비스 활동 기록) | **사실오류** — 조항 주제 자체 잘못 |
| §820.35(c) | 기밀성 | Unique Device Identification (UDI) | **사실오류** — 조항 주제 자체 잘못 |
| §820.35(d) | 전자서명 (Part 11) | Confidentiality (기밀성) | **사실오류** — 비실재 Part 11 조항 신설 |

추가: §820.35의 어디에도 "MDR 보고 결정 근거를 반드시 기록하라"는 명시 조항은 없음 — §820.35(a)는 "review, evaluation, and investigation"과 7개 기록항목(기기명/접수일/UDI/고발자/불만상세/시정조치/답변)을 요구한다.

## 영향
- 본 문서 근거로 갱신되는 SOP-DOC-001(§820.35 추가 요건), SOP-TRC-001(UDI), SOP-IA-001(내부감사) 방향이 **조항 매핑 단계부터 오설계** → §820.35(b) "서비스 활동 기록" 6항목(시판 후 X-ray 출장정비 기록) 의무가 완전 누락, §820.35(c) UDI 기록 의무가 §820.35(b)로 오기재되어 GUDID·UDI-DI 절차 근거조항이 잘못 인용.
- §820.35(d)에 "Part 11 적용 의무"가 있다는 주장은 QMSR 본문 미존재 조항을 사실로 단정 → §3.4 표에 "선량 교정 성적서·SW 빌드·QC 성적서·CAPA·내부감사 보고서"를 자동 Part 11 대상으로 분류한 것은 근거 없음.
- FDA Form 483·Warning Letter 대응 시 잘못된 조항 인용 → 심사 신뢰성 훼손.

## Tier 1 출처
- 21 CFR 820.35 (eCFR 현행) — https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820/subpart-B/section-820.35
- Source: 89 FR 7523, Feb. 2, 2024 (QMSR Final Rule); 시행 2026-02-02
- 21 CFR 803 (MDR — 별도 Part) — https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-803
- 21 CFR 830 (UDI — 별도 Part) — https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-830
- 21 CFR Part 11 (§820.35와 무관 독립 Part) — https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11

## 권고
1. §3.1~§3.4 하위항목 (a)(b)(c)(d) 주제 전면 재맵핑:
   - (a) MDR 기록 → **불만 기록(7항목)** 으로 재정의 (MDR 보고 결정은 21 CFR 803의 요구로 별도 표기)
   - (b) UDI 기록 → **서비스 활동 기록(6항목)** 으로 재정의 (X-ray 정비기록 의무화)
   - (c) 기밀성 → **UDI 기록** 으로 재정의 (GUDID·DI/PI는 §820.35(c) 근거)
   - (d) Part 11 → **기밀성** 으로 재정의 (Part 11은 §820.35 외부 독립 규정)
2. §4 비교표·§5 SOP 갱신 권고도 재맵핑에 맞춰 갱신.
3. Part 11 적용 여부는 §820.35와 분리하여 별도 절로 이관 — 모든 전자기록을 Part 11 자동 대상으로 분류하지 말고 predicate rule 기준 적용성 분석.
4. v0.3 개정 이력에 "§820.35 하위항목 구조 정정(eCFR 1차 재확인)" 명시.
