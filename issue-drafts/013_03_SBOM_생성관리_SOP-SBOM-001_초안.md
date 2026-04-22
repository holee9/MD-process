---
title: "[03] SOP-SBOM-001 v0.1 초안 — SBOM 생성·VEX·VDR 통합 관리 절차"
labels: "documentation,qms,design-control,compliance"
---

## 배경
FDA는 2025-10-01부터 premarket submission에 SBOM 미포함 시 반려한다. MFDS 디지털의료기기 전자적 침해행위 보안 지침 제16조도 SBOM 관리 활동을 권고하며, MDR(MDCG 2019-16)·IMDRF N73 역시 동일한 기조. 본 프로젝트는 빌드 파이프라인에 SBOM 자동 생성 도구가 연동돼 있지 않아 2026-Q3까지 파일럿 완료가 시급하다.

2026-04-22 교차검증 결과 G1(파일럿 미실행) / G6(Change Control 인터페이스 미정의) / G7(VEX 포맷 미선정) 도출.

## 체크리스트
- [ ] SOP-SBOM-001 v0.1 초안 리뷰 및 v0.2 갱신 (IMDRF N73 체크리스트 매핑 추가)
- [ ] 빌드 파이프라인 SBOM 자동 생성 도구 PoC (Syft / CycloneDX CLI / SPDX Tools 중 택1)
- [ ] 수작업 보완 항목(binary-only 펌웨어 블롭) 리스트 수집
- [ ] CVSS v3.1 + Medical Rubric(IMDRF/CYBER/N60) 적용 프로세스 문서화
- [ ] VEX 포맷 결정 (OpenVEX vs CycloneDX VEX) 및 v0.2 반영
- [ ] SOP-CC-001(이슈 012)과 인터페이스 섹션 추가: SBOM 컴포넌트 변경 → Change 분류 기준
- [ ] DHF/DMR 편입 기록 양식 설계
- [ ] 2025-10-01 FDA 시점 대비 리허설 제출 패키지 구성

## 참고 링크
- `03_설계_개발관리/SOP-SBOM-001_SBOM_생성관리_절차.md`
- `03_설계_개발관리/IEC_81001-5-1_FDA_Cybersecurity_SW보안.md`
- `12_교차검증_보고서/2026-04-22_SBOM_디지털의료제품법_정합성.md`
- 관련 이슈: 009(IEC 81001-5-1), 012(SOP-CC-001)
