---
title: "audit(C1): 외부_Pen-test_계획서 — FD&C §524B(b)(1)(B)에 'reasonable assurance' 귀속 사실오류(정답 §524B(b)(2)), audit #954 자매재발(역방향)"
labels: "audit:factuality,prio:P0,risk:medium"
state: closed
---

## 대상
- `05_검사_시험_밸리데이션/외부_Pen-test_계획서_v0.1.md` L52(§2 표 "FD&C Act §524B(b)(1)(B) | — | \"reasonable assurance that the device and related systems are cybersecure\"")
- 클래스: C1 (조항번호 정확성)

## 결함
FD&C Act §524B(b) 구조: **(b)(1)** = 시판후 취약점 모니터링·식별·대응 계획 제출(CVD 포함), **(b)(2)** = "design, develop, and maintain processes and procedures to provide a **reasonable assurance** that the device and related systems are cybersecure" + 패치·업데이트 제공((A) 정기/(B) 긴급), **(b)(3)** = SBOM. 'reasonable assurance' 문구의 정답 인용은 **§524B(b)(2)**. "(b)(1)(B)"는 해당 문구의 소재지가 아님.
audit #954(SOP-CVD-001: CVD 계획을 (b)(2)로 오귀속)와 동일 조문 쌍의 **역방향 자매재발** — (b)(1)↔(b)(2) 혼동 패턴이 카테고리를 넘어 반복.

## Tier1
FDA 공식(Cybersecurity in Medical Devices FAQ, fda.gov; §524B 조문 구조) — audit #954 시 fda.gov/media/178134 원문과 동일 구조 재확인.

## 판정
P0, 1개소. 해석범위 아님. 감사관 본문 미수정. 실운영 문서 미참고. web_verification: yes.


## 처리 결과 (2026-07-16)
- `05_검사_시험_밸리데이션/외부_Pen-test_계획서_v0.1.md` L52 정정: "§524B(b)(1)(B)" → "§524B(b)(2)".
- Tier1 재확인: FD&C Act §524B(b)(2) 원문 chapeau = "design, develop, and maintain processes and procedures to provide a reasonable assurance that the device and related systems are cybersecure..."(WebSearch: FDA 관련 요약·1차조문 구조 교차확인, audit #954 근거 fda.gov/media/178134 슬라이드 13/14 구분과 일치).
- 동일 클래스 일괄 점검: 전 저장소 `524B(b)(1)`/`524B(b)(2)` 인용 전수 grep — `12_교차검증_보고서/2026-04-26_사용적합성_Pentest_정합성.md` L37에 동일 오류(§524B(b)(1)(B)→reasonable assurance) 잔존 발견, 함께 정정("§524B(b)(2) [audit #974 정정 — 원문 (b)(1)(B) 오기재]"). SOP-CVD-001의 §524B(b)(1) 인용(CVD 계획 근거)은 이미 audit #954로 정정 완료·정확(PASS).
- 실운영 문서 미참고.
