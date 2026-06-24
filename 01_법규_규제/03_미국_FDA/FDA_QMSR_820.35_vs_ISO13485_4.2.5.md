---
doc-id: FDA_QMSR_820.35_vs_ISO13485_4.2.5
title: "FDA QMSR §820.35 ↔ ISO 13485 4.2.5 차이표"
type: Guide
version: v0.3
status: draft
category: 01_법규_규제
purpose: "FDA QMSR §820.35와 ISO 13485 §4.2.5 간 차이 분석 및 X-ray 시스템 기록관리 적용 지침"
applicable: [FDA QMSR 21 CFR 820, ISO13485:2016 §4.2.5, 21 CFR 803, 21 CFR 830, 21 CFR Part 11, UDI]
forms: [F-QMSR-REC-001]
related-docs:
  - FDA_QMSR_2026
  - ISO13485_2016_요약
  - SOP-DOC-001
  - SOP-TRC-001
  - SOP-FSCA-001
  - SOP-PSUR-001
  - SOP-PMS-001
related-issues: [44, 915, 916]
owner: RA/QA Lead
last-review: 2026-06-25
review-due: 2027-06-25
---

# FDA QMSR §820.35 ↔ ISO 13485 4.2.5 차이표

## 0. 개정 이력

| 버전 | 일자 | 변경요지 | 작성자 |
|---|---|---|---|
| v0.2 | 2026-05-25 | 초안 — §820.35 추가 요건 비교표·X-ray 적용 절차 | RA/QA Lead |
| v0.3 | 2026-06-25 | (1) §3 §820.35 하위항목 (a)(b)(c)(d) 주제 eCFR 1차 재확인 정정 — (a)불만 기록·(b)서비스 활동 기록·(c)UDI·(d)Confidentiality; 비실재 "§820.35(d) Part 11" 표현 삭제 [audit #915]. (2) §3.1 MDR 보고기한 21 CFR 803.50(30 calendar days) / 803.53(5 work days) 트리거 기준 재작성 — 사망/중상 기본 30일, 5영업일은 remedial action 필요 또는 FDA 서면요청 시 발동 [audit #916]. (3) F-QMSR-REC-001 보고유형 체크박스 정정. (4) Part 11 적용성을 §820.35와 분리하여 별도 절(§3.5)로 이관. | holee9-builder |

## 1. 적용 전제

- 21 CFR Part 820이 2026-02-02부터 QMSR로 전환되어 ISO 13485:2016이 참조편입(Incorporation by Reference) 됨
- ISO 13485 §4.2.5(기록의 관리)는 **기본 요건**이며, FDA는 §820.35에서 **추가 요건**을 부과
- 따라서 ISO 13485 §4.2.5만 충족해서는 미국 시장 적합성이 불충분

## 2. ISO 13485 §4.2.5 (기록의 관리) 핵심 요구사항

| 요구사항 | 상세 |
|----------|------|
| 기록 작성·유지 | 적합성 입증 및 QMS 효과적 운영 증거 |
| 절차 수립 대상 | 식별, 보관, 보호, 검색, 보유기간, 폐기 |
| 보호 범위 | 가독성, 변조방지, 손실방지 |
| 보유기간 | 제품 수명 + 적용 규제·계약 요구 기간 (최소 2년) |
| 기밀/개인정보 | 건강 관련 기록의 기밀성·무결성 보호 |

## 3. §820.35 추가 요건 상세 (eCFR 현행 — Source: 89 FR 7523, Feb. 2, 2024; 시행 2026-02-02)

§820.35 Control of records는 ISO 13485 §4.2.5에 더하여 다음 4개 하위항목으로 추가 기록 요건을 부과한다.

| 하위항목 | 정식 명칭 | 주제 요약 |
|---|---|---|
| §820.35(a) | Records of complaints | 불만 기록 (7항목) |
| §820.35(b) | Records of servicing activities | 서비스 활동 기록 (6항목) |
| §820.35(c) | Unique Device Identification | UDI 기록 |
| §820.35(d) | Confidentiality | FDA 공개 판단 보조 기밀성 |

> v0.2에서 (a)(b)(c)(d)의 주제를 각각 "MDR 기록 / UDI / 기밀성 / 전자서명(Part 11)"으로 기재하였으나, 이는 eCFR 본문과 불일치하는 사실오류였음 — v0.3에서 정정 [audit #915]. **21 CFR Part 11(전자기록·전자서명)은 §820.35의 일부가 아니라 독립 Part**이므로 §3.5에 분리 기술한다.

### 3.1 §820.35(a) — Records of complaints (불만 기록)

**요구사항** (eCFR 21 CFR 820.35(a)): 21 CFR Part 820 Subpart M (Complaint Files)에 따라 불만(complaint) 처리·평가·조사 활동에 대해 다음 7개 항목을 기록한다:
1. 기기명(name of the device)
2. 불만 접수일(date the complaint was received)
3. UDI 또는 UPC, 모델·카탈로그·일련번호 등 기기 식별정보
4. 불만 제기자 성명·주소·전화 등 식별정보
5. 불만 내용·상세
6. 조사 결과(개시일·종결일 포함) 및 시정조치
7. 불만 제기자에 대한 회신

**X-ray 시스템 적용 절차**:

| 단계 | 수행자 | 활동 | 기한 | 기록 |
|------|--------|------|------|------|
| 1 | 서비스팀 | 현장 불만/이상 접수 → CRM 등록 | 접수 즉시 | 불만 접수 기록 (7항목 필드 확보) |
| 2 | QA | 불만 분류 — MDR 보고 대상 여부 평가 → 결정 트리(§3.1.1) 적용 | 인지 후 신속(보고기한 역산) | 불만 처리 기록 + MDR 결정 기록 (F-QMSR-REC-001) |
| 3-A | RA | §803.50 또는 §803.53 트리거 충족 시 → FDA eMDR(MedWatch 3500A) 제출 | §3.1.1 기한표 | 제출 확인서 |
| 3-B | QA | 미보고 → 미보고 사유 문서화 | 판정 즉시 | 미보고 사유서 |
| 4 | QA | CAPA 필요성 평가 | 판정 후 5영업일 | CAPA 연계 기록 |

#### 3.1.1 MDR 보고기한·결정 트리 (21 CFR Part 803)

| 21 CFR | 보고 유형 | 트리거 | 기한 |
|---|---|---|---|
| **§803.50** | 30-day report | (i) 기기가 사망/중대상해(serious injury)에 기여했다고 합리적으로 의심, 또는 (ii) 기기 오작동이 재발 시 사망/중상을 유발할 가능성 | 인지 후 **30 calendar days** |
| **§803.53** | 5-day report | (1) MDR 보고대상 사건이 공중보건에 대한 부당한 실질적 위해 방지를 위해 **시정조치(remedial action)** 가 필요한 경우, 또는 (2) FDA가 서면으로 5-day report를 요청한 경우 | 인지 후 **5 work days** |
| §803.50(b) | Supplemental | 후속 정보 인지 | **30 calendar days** |

> v0.2 "사망/중상=5영업일·기타=30일" 기재는 사실오류로, 정답은 위 표대로다. 사망/중상은 기본 30일(§803.50)이며, 5 work days(§803.53)는 "사망/중상이라서"가 아니라 **시정조치 필요 또는 FDA 서면 요청**이 트리거다 — 정정 [audit #916]. §803.53 발동 시에도 §803.50의 30-day 보고는 병행한다(상호 배타 아님).

```
불만/이상 접수 → MDR 보고대상 평가
│
├─ Q1) Remedial action이 공중보건상 부당한 실질적 위해 방지에 필요한가?
│      또는 FDA가 5-day report를 서면 요청했는가?
│   ├─ Yes → 5 work days 보고 (§803.53)  + 30-day 트랙도 병행
│   └─ No → Q2)
│
├─ Q2) 기기가 사망/중대상해에 기여했다고 합리적으로 의심되는가?
│      또는 재발 시 사망/중상을 유발할 가능성이 있는 오작동인가?
│   ├─ Yes → 30 calendar days 보고 (§803.50)
│   └─ No → 미보고 (사유 기록)

특수 사례 (X-ray 시스템):
- 선량 과다 노출 사건 → 기본 §803.50(30cd) 평가
  · 동일 사유 추가 발생 우려가 있어 즉각적 device removal/notification 등
    remedial action 필요 → §803.53(5wd) 병행
- AEC 오작동 → §803.50(30cd) 평가
- 영상 미표시/왜곡 → §803.50(30cd) 평가
- SW 오류(선량 표시 부정확) → §803.50(30cd) 평가
  · 즉시 패치·중지 등 remedial action 필요 시 §803.53(5wd) 병행
```

### 3.2 §820.35(b) — Records of servicing activities (서비스 활동 기록)

**요구사항** (eCFR 21 CFR 820.35(b)): 시판 후 출장정비·수리·교정 등 서비스 활동에 대해 다음 6개 항목 기록:
1. 기기명(name of the device serviced)
2. UDI 또는 UPC, 모델·카탈로그·일련번호 등 식별정보
3. 서비스 일자
4. 서비스 수행자
5. 서비스 내용(service performed)
6. 시험·검사 데이터(test and inspection data)

**X-ray 시스템 서비스 기록 관리**:

| 서비스 유형 | 6항목 기록 포인트 | 비고 |
|---|---|---|
| 정기 PM(예방정비) | 출장일·기사·작업항목·측정값(kVp/mAs/DAP) | DI/PI(S/N) 식별 |
| 부품 교체 수리 | 교체 부품 S/N·작업기사·교체 후 시험 | 교체 시 PI 변경 발생 여부 판정 |
| SW 패치 적용 | 빌드 번호·적용일·기사·사후 시험 결과 | UDI-PI(SW 버전) 갱신 트리거 |
| 선량 교정 | 측정 장비·측정값·기준값·합격여부 | 5_검사_시험 표준매핑 연계 |

> 서비스 기록(§820.35(b))은 v0.2에서 누락 또는 "UDI 기록"으로 오분류되었던 의무로, X-ray 사후관리의 핵심 적합성 증빙이다 — 정정 [audit #915].

### 3.3 §820.35(c) — Unique Device Identification (UDI 기록)

**요구사항** (eCFR 21 CFR 820.35(c)): 21 CFR Part 830에 따라 각 기기(or 배치)에 대한 UDI를 기록한다.
- UDI-DI 발급 기관(FDA 인정: GS1, HIBCC, ICCBBA)
- DI/PI 구성·변경 이력
- GUDID(Global UDI Database) 제출·갱신 기록

**X-ray 시스템 UDI 기록 관리**:

| UDI 대상 품목 | DI 예시 | PI 구성 | GUDID 갱신 트리거 |
|--------------|---------|---------|------------------|
| X-ray 본체(System) | (01)08806XXXXX | 제조일+S/N+SW버전 | 모델명 변경, 의도된 사용 변경 |
| Flat Panel Detector | (01)08806XXXXX | 제조일+S/N | 센서 사양 변경 |
| 콜리메이터 | (01)08806XXXXX | 제조일+S/N | 기구적 변경 |
| SW (SaMD/SiMD 해당 시) | (01)08806XXXXX | SW 버전 | 주요 버전 업그레이드 |

### 3.4 §820.35(d) — Confidentiality (기밀성)

**요구사항** (eCFR 21 CFR 820.35(d)): 제조자가 기밀로 표시한 기록의 FDA 공개 판단을 보조한다. FDA가 송부·수령한 기록에 대해 제조자는 기밀 표시를 적용할 수 있고, FDA는 18 USC 1905(영업비밀), 21 USC 331(j), 5 USC 552(FOIA) 등 관련 법령에 따라 공개 여부를 판단한다.
- 실무: FDA 제출 문서에 "Confidential — Contains Trade Secrets" 헤더 표기
- 사내: 기밀 분류 기록 목록 관리(F-QMSR-REC-001과 별도 등록부 권장)

### 3.5 (참고) 전자기록·전자서명 — 21 CFR Part 11 적용성

> Part 11은 **§820.35의 하위항목이 아니라 독립 Part**이며, QMSR 본문이 Part 11을 §820.35에 편입하지 않았다. 따라서 §3.5는 §820.35 외부 적합성 논의로 분리한다 [audit #915].

전자기록·전자서명을 predicate rule(§820·Part 803·Part 830 등) 이행 수단으로 사용할 경우 Part 11이 적용된다. 모든 전자기록을 자동으로 Part 11 대상으로 분류하지 말고, predicate rule 요구를 충족하기 위해 채택한 기록에 한해 적용성을 분석한다(FDA Part 11 Scope and Application guidance, 2003 기조 유지).

**Part 11 적용성 평가 대상 예시 (사례별 판정 필요)**:
- 선량 교정 성적서 (kVp, mAs, DAP 측정 기록) → predicate: §820.72·§820.75·§820.250
- SW 빌드·릴리즈 기록 → predicate: §820.30(j) DHF
- 영상품질 QC 성적서 → predicate: §820.80
- 출하 시험 기록 → predicate: §820.80(d)
- CAPA 기록 → predicate: §820.100
- 내부감사 보고서 → predicate: §820.22

각 기록별 (i) open/closed system 구분, (ii) audit trail 요구, (iii) 전자서명 채택 여부를 문서화한다.

## 4. 항목별 비교 요약 (v0.3 정정 반영)

| 항목 | ISO 13485 §4.2.5 | FDA QMSR §820.35 추가 |
|------|-----------------|-------------------------|
| 불만 기록 | 8.2.2(불만 처리)에 따른 일반 요건 | **§820.35(a)** 7항목 명시(기기명·접수일·UDI/UPC·제기자·내용·조사/시정·회신) |
| 서비스 기록 | 7.5.4(서비스 활동) 일반 요건 | **§820.35(b)** 6항목 명시(기기명·UDI/UPC·일자·수행자·내용·시험데이터) |
| UDI 기록 | 직접 요구 없음 | **§820.35(c)** + 21 CFR Part 830 DI/PI·GUDID 의무 |
| 기밀성 | 보호 일반(고객정보 포함) | **§820.35(d)** FDA 송수신 기록 공개 판단 보조 |
| 보유기간 | 제품수명 + 최소 2년 | (§820.180 폐지) 별도 보유기간 표는 §820.180 폐지로 FDA 열람 가능성 강화 — 보유기간 자체는 predicate rule 적용 |
| 전자기록 | 일반 적합성(4.2.4) | **§820.35 외부** — 21 CFR Part 11 별도 적합성 분석 |
| 내부감사·경영검토 | 비공개 가능(이전 §820.180(c)) | 비공개 예외 폐지 → FDA 열람 대상 |

## 5. SOP 반영 절차

### 5.1 반영 대상 SOP 및 갱신 내용 (v0.3 정정 반영)

| SOP | 갱신 내용 | 담당 | 판정 기준 |
|-----|----------|------|----------|
| SOP-DOC-001 | §3에 "미국 시장 적용 시 §820.35(a)(b)(c)(d) 추가요건" 절 신설, Part 11은 §820.35 외부로 별도 절 분리 | QA | 기록관리 절차에 불만/서비스/UDI/기밀성·Part 11 분리 기재 여부 |
| SOP-PMS-001 | MDR 결정 트리(§803.50 30cd / §803.53 5wd 트리거 기준) + 미보고 사유 양식 첨부 | QA/RA | 불만 → MDR 판정 → 기록 흐름 완비 여부 |
| SOP-TRC-001 / SOP-UDI-001 | UDI 기록관리 절 추가 — **§820.35(c)** + 21 CFR Part 830 | RA | GUDID 제출·갱신 기록 체계 구축 여부 |
| SOP-SVC-001 (신설/갱신) | **§820.35(b)** 6항목 서비스 기록 양식 도입 | Service/QA | X-ray 출장정비 기록 6항목 완결성 |
| SOP-IA-001 | 감사보고서 작성 기준에 "외부 열람 대비 객관적 증거 인용" 항목 추가 | QA | 보고서 품질 기준 갱신 여부 |

### 5.2 반영 절차

| 단계 | 수행자 | 활동 | 산출물 |
|------|--------|------|--------|
| 1 | RA/QA Lead | 갱신 대상 SOP 식별 및 변경요청서(CCR) 발행 | F-CC-001 |
| 2 | 각 SOP 소유자 | SOP 개정 초안 작성 | 개정 초안 |
| 3 | QA | §820.35 충족 여부 교차검토 | 검토 기록 |
| 4 | 승인권자 | 승인 | 승인된 SOP |
| 5 | QA | 배포·교육·유효일 관리 | 교육기록, 배포기록 |

## 6. 기록 관리 양식 (F-QMSR-REC-001)

### F-QMSR-REC-001: MDR 보고 결정 기록 양식 (v0.3 정정)

| 필드 | 내용 |
|------|------|
| **불만 접수 번호** | COMP-YYYY-NNNN |
| **접수일** | YYYY-MM-DD |
| **기기 명칭 / 모델** | (§820.35(a)#1·#3) |
| **UDI-DI / S/N** | (§820.35(a)#3) |
| **제기자 식별** | 성명/주소/전화 (§820.35(a)#4) |
| **사건 요약(불만 내용)** | (§820.35(a)#5, 200자 이내) |
| **환자 영향** | ☐사망 ☐중상 ☐경상 ☐없음 |
| **기기 오작동 여부** | ☐Yes ☐No |
| **재발 시 사망/중상 가능성** | ☐Yes ☐No ☐해당없음 |
| **Remedial action 필요?** | ☐Yes(공중보건 부당 실질위해 방지) ☐No |
| **FDA 5-day report 서면요청?** | ☐Yes ☐No |
| **MDR 보고 결정** | ☐보고 ☐미보고 |
| **보고 유형** | ☐**30 calendar days (§803.50)** ☐**5 work days (§803.53 트리거)** ☐해당없음 |
| **미보고 사유** | (미보고 시 필수 기재) |
| **조사 결과 / 시정조치** | 개시일·종결일·요지 (§820.35(a)#6) |
| **제기자 회신** | 회신일·요지 (§820.35(a)#7) |
| **판정자** | 성명 / 직위 |
| **판정일** | YYYY-MM-DD |
| **CAPA 연계** | ☐필요 → CAPA-YYYY-NNNN ☐불필요 |

## 7. 출처

- 21 CFR 820.35 (eCFR 현행, Source: 89 FR 7523, Feb. 2, 2024; 시행 2026-02-02) — https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820/subpart-B/section-820.35
- 21 CFR 803.50 (eCFR 현행) — https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-803/subpart-E/section-803.50
- 21 CFR 803.53 (eCFR 현행) — https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-803/subpart-E/section-803.53
- 21 CFR Part 830 (UDI) — https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-830
- 21 CFR Part 11 (전자기록·전자서명 — §820.35와 무관 독립 Part) — https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11
- FDA "Medical Device Reporting (MDR)" — https://www.fda.gov/medical-devices/medical-device-safety/medical-device-reporting-mdr-how-report-medical-device-problems
- FDA QMSR FAQ — https://www.fda.gov/medical-devices/quality-management-system-regulation-qmsr/quality-management-system-regulation-frequently-asked-questions
- Federal Register 2024-01709, 2025-21955
- 확인일: 2026-06-25

## 8. 적대적 자기검토 (Adversarial Self-Review)

| 검토 관점 | 결함 가능성 | 본 v0.3 처리 |
|---|---|---|
| §820.35 (a)(b)(c)(d) 하위항목 주제 | eCFR 원문과 불일치 시 SOP 매핑 오설계 | §3 표·§3.1~§3.4 본문 모두 eCFR 1차 재확인 후 동기화 [audit #915] |
| MDR 보고기한 5wd / 30cd | 트리거 혼동 시 §803.50 또는 §803.53 위반 | §3.1.1 표·결정 트리·F-QMSR-REC-001 모두 §803.50/§803.53 트리거 기준 통일 [audit #916] |
| Part 11 적용성 | 자동 일괄 적용 시 over-validation | §3.5 분리, predicate-rule 기반 사례별 평가로 전환 |
| §820.180 폐지 처리 | 보유기간 단순화 후 과도/과소 해석 | §4 표 비고로 "predicate rule 적용" 표기 |
| 사내 동반 모순 | 타 SOP/가이드 동일 오류 유지 시 정합성 훼손 | TF-TD-001·SOP-UDI-001·X-ray 표준매핑 같은 사이클에서 동반 교정 |

## 9. 기록·예외

- 본 가이드 자체는 Guide 분류로 §820.35(a)(b)에 따른 운영기록 대상 아님(절차서·SOP를 통해 운영기록 산출).
- 예외: 본 가이드 인용을 근거로 발생한 검토 메모는 일반 기록통제(§4.2.5)를 따른다.
- 보유기간: 최신 개정본 + 이전본 1개 회수 시점까지 유지(SOP-DOC-001 §4 기준).
