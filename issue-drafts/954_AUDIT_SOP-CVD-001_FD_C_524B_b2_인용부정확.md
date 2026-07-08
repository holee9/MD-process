---
title: "audit(C1): SOP-CVD-001 §524B(b)(2) 인용부정확 — CVD 계획 근거는 §524B(b)(1)"
labels: "audit:factuality,prio:P0,risk:high"
---

## 대상
- 문서: `02_품질경영시스템_QMS/SOP-CVD-001_조정된_취약점_공개_정책.md` (v0.3, last-review 2026-06-05)
- 위치 1: §2 근거 목록, 라인 31
- 위치 2: §배경 (v0.3 변경 이력), 라인 138
- 적용 법령: FD&C Act §524B (Consolidated Appropriations Act, 2023 §3305로 신설)
- 감사 클래스: C1 (조항번호 정확성) — 전수 클래스 스윕 (02_품질경영시스템_QMS)

## 독립 감사 요약

문서는 두 곳에서 "CVD(Coordinated Vulnerability Disclosure) 계획"의 법적 근거를 **§524B(b)(2)**로 인용하나, Tier 1(FDA 공식 자료) 확인 결과 CVD 계획·모니터링·식별·대응 의무는 **§524B(b)(1)**에 해당하고, §524B(b)(2)는 별개 요구사항("reasonable assurance of cybersecurity" 프로세스·업데이트/패치 제공)이다.

## 1차 출처 정답 (FD&C Act §524B(b), FDA 공식 슬라이드/문서)

| 조항 | 요구사항 |
|---|---|
| **§524B(b)(1)** | **Plan to monitor, identify, and address, as appropriate, in a reasonable time, postmarket cybersecurity vulnerabilities and exploits, including coordinated vulnerability disclosure and related procedures** |
| §524B(b)(2) | Design, develop, and maintain processes/procedures to provide reasonable assurance that the device and related systems are cybersecure, and make available postmarket updates and patches |
| §524B(b)(3) | Provide a Software Bill of Materials (SBOM) |

**Tier 1 출처:**
- FDA, "Section 524B of the FD&C Act" (Select Updates for the Premarket Cybersecurity Guidance 웨비나 자료) — https://www.fda.gov/media/178134/download — 슬라이드 13 "Plans and Procedures (524B(b)(1))", 슬라이드 14 "Reasonable Assurance of Cybersecurity (524B(b)(2))" 명시적 구분
- FDA Cybersecurity in Medical Devices FAQ — https://www.fda.gov/medical-devices/digital-health-center-excellence/cybersecurity-medical-devices-frequently-asked-questions-faqs

## 결함 (P0, 사실오류)

### D1 — §2 라인 31
- **기재값:** `FDA FD&C Act §524B(b)(2): "have a plan to monitor, identify, and address ... vulnerabilities and exploits"`
- **독립확인 정답:** 해당 인용문(모니터링·식별·대응 계획, CVD 포함)은 **§524B(b)(1)**의 요구사항. §524B(b)(2)는 "reasonable assurance of cybersecurity" 프로세스 유지 요구.
- **권고수정:** `§524B(b)(2)` → `§524B(b)(1)`

### D2 — §배경 라인 138
- **기재값:** `CVD 계획은 FD&C Act §524B(b)(2)에 따라 "cyber device"의 시판 전 제출 의무 문서이며...`
- **독립확인 정답:** CVD 계획의 법적 근거는 §524B(b)(1). 동일 오류 반복.
- **권고수정:** `§524B(b)(2)` → `§524B(b)(1)`

## 참고 — 자매문서 확산 여부

audit #913(closed)은 동일 §524B 관련이나 **법령 명칭 오류**(FDARA vs CAA 2023 §3305)를 다룬 별개 결함이며 본 건(subsection 번호 오류)과 중복 아님. #913 권고에서 "SOP-CVD-001 등에서 유사 패턴 검색·일괄 정정 필요"를 언급했으나 subsection 번호 자체는 미점검 상태였음.

grep 패턴 `§524B\(b\)\(2\)` 로 03_설계_개발관리, 09_공급자_관리 등 자매문서 확산 여부 추가 확인 권고(본 사이클 범위 밖).

## 판정
- **P0 사실오류 (factuality)** — 2건 (동일 문서 내 2개소)
- 근거: Tier 1 (FDA 공식 문서, 정부 웨비나 자료)
- 문서 수정은 빌더 몫(본 이슈 등록으로 감사관 임무 완료).
