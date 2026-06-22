# 독립 감사 로그 (Independent Audit Log)

> 본 로그는 **독립 감사관(holee9-auditor)**이 빌더 산출물을 1차 출처로 재확인한 결과의 시계열 기록이다.
> 빌더의 자체 교차검증(12_교차검증_보고서) 결론은 신뢰하지 않으며, 회사 실운영 문서 미참고.

| 날짜 | 표본문서수 | 검증주장수 | 사실오류 | 노후 | 인용결함 | 통과율% | 비고 |
|---|---|---|---|---|---|---|---|
| 2026-06-22 | 2 | 9 | 4 | 0 | 1 | 44.4 | 첫 감사. audit 이슈 #900~904 등록. 표본: GUIDE-VIG-001 v0.2, SOP-PMS-001 v0.3 |
| 2026-06-22 | 4 | 9 | 1 | 0 | 1 | 77.8 | 표본: EU_MDR_2017_745 v0.3, FDA_QMSR_2026 v0.2, EU_AI_Act_MDR_중첩매핑 v0.5, ISO13485_2016_요약 v0.2. audit #905(P0 Art.4 시점 사실오류) #906(P1 ISO13485 reconfirmed 날짜 인용부정확) 등록. FDA QMSR 2026-02-02·EUDAMED 2026-05-28·AI Act 발효·고위험·Omnibus(2027-12-02/2028-08-02) 일정 일치 확인. web_verification:yes |
| 2026-06-22 | 1 | 4 | 4 | 0 | 0 | 0.0 | 표본: ISO14971_프로세스_상세 v0.2. ISO 14971:2019 §7 하위조항 번호 4건 사실오류 P0 (#907). web_verification:yes (ISO OBP + ANSI/AAMI 미리보기 + medicaldeviceacademy) |
| 2026-06-22 | 4 | 13 | 2 | 0 | 1 | 76.9 | 표본: SOP-FSCA-001 v0.3, IEC_62304_SW_수명주기 v0.3, SOP-RM-001, 진단용방사선규칙 제1122호 v0.2. audit #908(IEC 62304 A2:2020 미존재 표준 인용 P0) #909(피폭기록 보존 5년→정답 30년 P0) #910(IEC 81001-5-1 §8.3 CVSS 정량기한 인용부정확 P1) 등록. EU MDR Art.87(2/10/15일)·21 CFR 806(10영업일)·21 CFR 803(30일/5일)·정기검사 3년·제1122호 시행일 2025-07-18·IEC 62366-1 AMD1:2020 일치 확인. web_verification:yes |
| 2026-06-23 | 3 | 7 | 2 | 0 | 1 | 57.1 | 표본: SOP-PSUR-001 v0.2, IEC_81001-5-1_FDA_Cybersecurity_SW보안 v0.2, SOP-SBOM-001 v0.3. audit #912(SOP-PSUR-001 §5.1 Class IIb '매 2년' P0 사실오류 — Art.86(2) annually) #913(IEC_81001-5-1 frontmatter 'FDA §524B FDARA' P0 사실오류 — 정답 CAA 2023 §3305) #914(SOP-PSUR-001 §2 '단종 후 15년' P1 인용부정확 — Art.10(8) 비이식형 10년 vs 회사정책 출처 미표시). FDA Cyber Guidance 2026-02-03·§524B 시행일 2023-03-29·EU MDR Art.86(2) IIb 연 1회·Art.10(8) 비이식형 10년 일치 확인. web_verification:yes |
