---
title: "[02] SOP-CC-001 Change Control v0.1 — 선량·보안 통합 판정 체계"
labels: "documentation,qms,compliance"
---

## 배경
X-ray 제품의 변경은 선량/영상 품질(임상) 영향과 사이버보안 영향이 병발한다.
2026-04-21 교차검증(G2)에서 단일 Change Control Board에서 두 축을 동시 판정하는 SOP 부재 확인.
MDR Art. 10(9), QMSR § 820.40·820.30(i), ISO 13485 7.3.9 요구와 정합되는 SOP 작성.

## 체크리스트
- [ ] 변경 분류(Major/Minor) 결정 기준표(선량, SW 안전성 클래스, 보안 영향)
- [ ] 평가 절차: DHF·RMF·Security Plan·SBOM 영향도 병렬 평가
- [ ] 규제 통지 의사결정(MDR PCCP, FDA Supplement, MFDS 변경허가)
- [ ] 기록 양식(변경 요청·승인·실행·검증 기록)
- [ ] UDI DI 재발급 판정 트리와 연결
- [ ] 62304 문제해결 §7, 81001-5-1 §8 유지보수 보안과 연결

## 참고 링크
- `03_설계_개발관리/IEC_62304_SW_수명주기.md`
- `03_설계_개발관리/IEC_81001-5-1_FDA_Cybersecurity_SW보안.md`
- `06_문서_기록관리/SOP-UDI-001_UDI_통합관리_초안.md`
- `12_교차검증_보고서/2026-04-21_Xray_안전성능_사이버보안_정합성.md`
