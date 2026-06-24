---
title: "[AUDIT][P0] FDA_QMSR_820.35_vs_ISO13485_4.2.5 §3.1 MDR 보고기한 사실오류 — '사망/중상=5영업일·기타=30일'은 반대로, 21 CFR 803.50/803.53과 불일치"
labels: "audit:factuality,prio:P0,risk:high"
state: closed
closed-date: 2026-06-25
closed-by: holee9-builder
close-ref: audit-915-916-fixed-v0.3
---

## 대상 문서
- `01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md` v0.2 §3.1 X-ray 시스템 적용 절차 표(3-A 행) 및 그 아래 "MDR 보고 결정 트리"

## 주장 (문서 기재값)
1. 표(3-A 행): "보고 대상 → FDA MedWatch 제출 | **사망/중상: 5영업일, 기타: 30일**"
2. §3.1 본문: "보고 기한 관리 (30일/5영업일)" + "사망/중상: 5영업일, 기타: 30일" 표 매핑
3. MDR 결정 트리:
   - "환자 사망 또는 중상 발생? Yes → **5영업일** MDR 보고 (초기보고)"
   - "재발 시 사망/중상 유발 가능성? Yes → **30일** MDR 보고"
4. 특수 사례: "선량 과다 노출 → **5영업일** 보고 검토"

## 정답 (Tier 1 — 21 CFR Part 803)

| 21 CFR | 보고 유형 | 트리거 | 기한 |
|---|---|---|---|
| **§803.50** | 30-day report | 기기가 사망/중대상해(serious injury)에 기여했다고 합리적으로 의심되는 경우, 또는 기기 오작동이 재발 시 사망/중상을 유발할 가능성이 있는 경우 | 인지 후 **30 calendar days** |
| **§803.53** | 5-day report | (1) MDR 보고대상 사건이 공중보건에 대한 부당한 실질적 위해 방지를 위해 **시정조치(remedial action)** 가 필요한 경우, 또는 (2) FDA가 서면으로 5-day report를 요청한 경우 | 인지 후 **5 work days** |

→ **사망/중상은 기본 30일 보고**가 정답.
→ 5일 보고는 "사망/중상이라서"가 아니라 **"시정조치가 필요한 경우 또는 FDA 서면 요청 시"** 트리거된다.
→ 즉, 단순히 사망/중상이 발생했다는 사실만으로 5-day 보고가 발동되지 않으며, 5-day는 §803.50의 30-day 보고에 **추가**(parallel)되는 별도 트랙이다.

## 문서 vs 정답 매핑
| 사건 유형 | 문서 기재 기한 | Tier 1 정답 | 판정 |
|---|---|---|---|
| 사망/중상 (death/serious injury) | 5영업일 | **30 calendar days** (§803.50) | **사실오류 — 기한 반전** |
| 오작동(재발 시 사망/중상 유발) | 30일 | **30 calendar days** (§803.50) — 기한은 우연히 일치하나 트리거 근거가 다름 | 부분일치 (기한 OK) |
| 시정조치 필요(remedial action) | (트리거 누락) | **5 work days** (§803.53) | **사실오류 — 트리거 누락** |
| FDA 서면 요청 시 | (트리거 누락) | **5 work days** (§803.53(b)) | **사실오류 — 트리거 누락** |

## 영향
- 본 결정 트리가 SOP-PMS-001 §MDR 보고 절차로 그대로 이식될 경우(§5 권고: "SOP-PMS-001 MDR 결정 트리 + 미보고 사유 양식 첨부") → 실제 운영에서 **사망/중상 사건을 5일 내 보고하려 시도하면 인적 자원·자료 미비로 보고 누락 또는 부실 보고 위험**.
- 반대로 시정조치 필요 사건을 30일로 처리하면 **§803.53 5-day 의무 위반** → FDA Form 483·Warning Letter 사유.
- F-QMSR-REC-001 양식 "보고 유형: ☐5영업일(사망/중상) ☐30일(오작동)" 체크박스도 잘못된 기준 → 양식 채택 시 운영 전반 부정합.

## Tier 1 출처
- 21 CFR 803.50 (eCFR 현행) — https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-803/subpart-E/section-803.50
- 21 CFR 803.53 (eCFR 현행) — https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-803/subpart-E/section-803.53
- FDA "Medical Device Reporting (MDR)" — https://www.fda.gov/medical-devices/medical-device-safety/medical-device-reporting-mdr-how-report-medical-device-problems
- (보조 — 범위 가늠용) sgsystemsglobal MDR 해설 — Tier 2, 사실 판정 근거 아님

## 권고
1. §3.1 X-ray 시스템 적용 절차 표 3-A 행을 다음과 같이 정정:
   - "사망/중상 또는 기기 오작동(재발 시 사망/중상 유발 가능): **30 calendar days** (§803.50)"
   - "시정조치 필요 또는 FDA 서면 요청: **5 work days** (§803.53)"
2. MDR 결정 트리에서 첫 분기를 다음과 같이 재작성:
   - 1단계: 시정조치 필요? / FDA 서면 요청? → Yes면 **5 work days** (§803.53)
   - 2단계: 사망/중상 또는 재발 시 사망/중상 유발 오작동? → Yes면 **30 calendar days** (§803.50)
3. 특수 사례 4건(선량 과다 노출/AEC 오작동/영상 미표시/SW 오류) 각각의 기한을 §803.50 적용으로 통일하고, "remedial action 발동 여부" 별도 판정 분기 신설.
4. F-QMSR-REC-001 양식의 보고 유형 체크박스를 ☐30 calendar days (§803.50) ☐5 work days (§803.53 trigger) 로 정정.
5. v0.3 개정 이력에 "21 CFR 803.50/803.53 기한·트리거 정정(eCFR 1차 재확인)" 명시.

## 종결 (Closure) — 2026-06-25

- 대상 문서 `01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md` v0.2→**v0.3** 정정.
- §3 §820.35 하위항목 주제 eCFR 1차 재확인 동기화: (a)Records of complaints / (b)Records of servicing activities / (c)UDI / (d)Confidentiality.
- §3.1.1 MDR 보고기한·결정 트리 21 CFR 803.50(30 calendar days) / 803.53(5 work days) 트리거 기준 재작성.
- F-QMSR-REC-001 보고유형 체크박스 30cd(§803.50) / 5wd(§803.53 트리거)로 정정 + remedial action·FDA 서면요청 필드 신설.
- Part 11 적용성을 §820.35와 분리하여 §3.5에 이관.
- 동반 교정:
  - `06_문서_기록관리/TF-TD-001_의료기기파일_기술문서_관리.md` v0.2→v0.3 §9.2·§9.3·§12.4
  - `06_문서_기록관리/SOP-UDI-001_UDI_통합관리_초안.md` v0.2→v0.3 §1·§참조·§근거
  - `05_검사_시험_밸리데이션/X-ray_장비_안전성능_표준_매핑.md` v0.3→v0.4 표준매핑 라인
- Tier 1 재확인 출처: 21 CFR 820.35 (Source: 89 FR 7523, 2024-02-02; 시행 2026-02-02), 21 CFR 803.50, 21 CFR 803.53 — 모두 eCFR 현행본.
