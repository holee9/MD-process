---
title: "[05_검사_시험_밸리데이션] 외부 침투시험(Pen-test) 계획서 v0.1 초안"
labels: "documentation,compliance,review"
---

## 배경
2026-04-24 보고서가 적시한 FDA SBOM 의무화(2025-10) 대응 P0 블로커 4종 중 "Pen-test 섭외" 항목을 해소하기 위한 발주·수행·결과보고용 계획서. FDA Premarket Cybersecurity Guidance(2023-09-26) §V.D/§VI.D 및 MFDS 사이버보안 가이드(2025-01-10) 제6장의 외부 검증 산출물 의무 충족.

## 작업 내용
- 신규 작성: `05_검사_시험_밸리데이션/외부_Pen-test_계획서_v0.1.md`
- 근거: FD&C §524B, FDA Premarket Cyber 2023, MFDS 가이드 2025, AAMI TIR57:2016, IEC 81001-5-1:2021 §7.4, IEC TR 60601-4-5:2021, NIST SP 800-115, OWASP WSTG/MASTG/IoTSVS
- 핵심: 적용 자산(콘솔·검출기·DICOM·원격·클라우드·모바일), 7단계 방법론, Black/Grey/White Box 혼합, VEX(OpenVEX/CSAF 2.0) 산출물, SLA(SOP-CVD-001 §7과 정합)

## 체크리스트
- [x] 1단계 — 적용 자산·범위 정의
- [x] 2단계 — 단계별 방법론·도구 매핑
- [x] 3단계 — 발주 RFP 자격 요건(ISO/IEC 27001 + ICS/Medical IoT ≥3년 + CREST/OSCP)
- [x] 4단계 — 결과 분류·SLA(CVD와 정합)
- [x] 5단계 — 산출물 7종 정의(VEX 포함)
- [ ] 검증 — RFP 발행·평가기관 발주 (P0, ~05-30)
- [ ] 검증 — 09/공급자_관리에 보안 시험기관 자격 SLA 신설 (P1, ~05-31)
- [ ] 검증 — Kick-off 후 보고서 최종(T0+5m), 재시험(T0+6m)

## 참고 링크
- 본 문서: `05_검사_시험_밸리데이션/외부_Pen-test_계획서_v0.1.md`
- 일일 리서치: `11_일일_리서치로그/2026-04-26_사용적합성_Pentest계획.md`
- 교차검증: `12_교차검증_보고서/2026-04-26_사용적합성_Pentest_정합성.md`
- 연계: `02_QMS/SOP-CVD-001_조정된_취약점_공개_정책.md`, `03_설계_개발관리/SOP-SBOM-001_*`, `03_설계_개발관리/IEC_81001-5-1_*`, `12_교차검증_보고서/2026-04-24_FDA_SBOM_제출물_사전점검.md`
