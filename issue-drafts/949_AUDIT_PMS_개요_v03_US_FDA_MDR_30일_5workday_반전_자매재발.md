---
title: "audit(08): PMS_개요 v0.3 §6 — US(FDA) 표 '30 calendar days (사망·중상은 5 work days)' 반전 사실오류 (정답: §803.50 사망/중상/오작동 30일 · §803.53 remedial action 필요 시 5 work day) — audit #916 자매재발"
labels: "audit:factuality,prio:P0,risk:high"
state: closed
---

## 대상
- 문서: `08_시판후_감시_PMS/PMS_개요.md` v0.3 (2026-07-02 갱신, audit #927/#928/#929 close 반영판)
- 위치: §6 "보고 기한 (주요국 비교)" 표, "US (FDA)" 행 "중대 부작용" 열
- 사매재발: audit **#916** (2026-06-24 close, `01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md` §3.1 동일 반전 패턴). audit #916 fix가 대상 문서에 국한되어 08_시판후_감시_PMS 폴더의 시판후 감시 개요 문서에 미전파.

## 독립 감사 요약

PMS_개요 v0.3 §6 표의 US(FDA) 행이 **"30 calendar days (사망·중상은 5 work days)"** 로 기재됨. Tier 1(eCFR 21 CFR Part 803) 재확인 결과:

- **21 CFR 803.50** = 제조자·수입자의 개별 이상사례(individual adverse event) 보고 = **30 calendar days**. 사망·중상·리포터블 오작동 **모두** 30일이 원칙.
- **21 CFR 803.53** = **5 work day 보고**는 **"MDR reportable event necessitates remedial action to prevent an unreasonable risk of substantial harm to the public health"** (즉, 공중보건 실질피해 방지 시정조치가 필요한 경우) 또는 **FDA의 서면요구** 시 적용.

즉, PMS_개요는 "사망·중상 = 5 work day"로 기술하여 **§803.50과 §803.53의 발동 조건을 반전**시켰음. 이는 audit #916에서 정확히 확정한 패턴과 동일.

## 1차 출처 정답 (Tier 1)

- **eCFR — 21 CFR 803.50** (30-day individual adverse event report, manufacturer): https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-803/subpart-E/section-803.50
- **eCFR — 21 CFR 803.53** (5 work day report, remedial action필요 시): https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-803/subpart-E/section-803.53
- **eCFR — 21 CFR 803.3** (정의: "remedial action" = any action other than routine maintenance or servicing of a device where such action is necessary to prevent recurrence of a reportable event): https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-803/subpart-A/section-803.3
- 사내 선행 감사 **#916** (동일 패턴 확정).

## 결함 (P0, 사실오류)

### D1 — §6 표 US(FDA) 행 (라인 근접치: 92~96 부근)
- **기재값 요지 (해당 셀):**
  > `| **US (FDA)** | 30 calendar days (사망·중상은 5 work days) | 말펑션 30일 | 연간(해당 시) |`
- **정답 (Tier 1):**
  > `| **US (FDA)** | § 803.50(a): 개별 이상사례(사망·중상·리포터블 오작동) — **30 calendar days** | § 803.53: **5 work day** — MDR reportable event가 공중보건 실질피해 방지 시정조치를 요구하거나 FDA 서면요구 시 | 연간 요약(해당 시), 오작동 요약보고 자율옵션(21 CFR 803.20(c) 참조) |`
- **영향:** 사이의 문서 이용자(RA/QA·PMS 담당자)가 사망·중상 발생 시 5 work day로 잘못 이해할 수 있음. **반대 상황**(5일이 급한 것으로 오인 → 30일 여유 있는 사건을 5일로 오인 대응) 및 실제 5-day 발동 조건(remedial action)이 30일 사건과 혼동될 수 있음. 감사·심사 지적 시 신뢰성 결정타.

### 참고 (Cross-Ref) — 같은 문서 §7·§6.1 정합 확인
- §6.1 X-ray 사고 유형별 판정 셀 "EU: 단일 환자 사망·심각 건강 악화 = Art.87(3) **10일**" — audit #929 정정과 정합(PASS).
- KR 셀 "7일(사망·중대위해), 15일(중대 부작용)" — 정합(PASS).

## 재발 방지 (Plan #935 확장 필수)

audit #916 close 시점부터 자매재발 방지 grep 룰 등록되었어야 함. 다음 패턴을 plan #935/#945 확장 매칭에 즉시 편입:
- `사망.*중상.*5.?work.?day` (반전 패턴)
- `5.?work.?day.*(사망|중상)` (역순)
- `21 CFR 803\.5[03]` 근접 문맥 검증
- 스캔 범위: 08_시판후_감시_PMS/**, 01_법규_규제/03_미국_FDA/**, 09_공급자_관리/**, 관련 SOP·GUIDE.

## 판정
- **P0 사실오류 (factuality) × 1문서 (자매재발 #916 확장)**
- 근거: eCFR §803.50 / §803.53 / §803.3 Tier 1 + 사내 선행 감사 #916
- 문서 수정은 빌더 몫.
