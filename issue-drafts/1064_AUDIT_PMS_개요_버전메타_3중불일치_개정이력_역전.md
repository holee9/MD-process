---
title: "audit #1064 (currency/문서관리): PMS_개요.md 버전 표기 3중 불일치(frontmatter v0.3.3 / 본문 헤더 v0.3.2 / purpose v0.3.1) + 개정이력 시간순 역전 + last-review 미갱신"
labels: "audit:currency,prio:P2,risk:low,qms,document-control"
state: closed
created: 2026-09-21
created-by: md-process-auditor
related-issues: [1026]
sweep: "C4 x 08_시판후_감시_PMS"
---

## 결함

`08_시판후_감시_PMS/PMS_개요.md`:

| 위치 | 기재 | 문제 |
|---|---|---|
| frontmatter L4 `title` / L6 `version` | `v0.3.3` | 최신 |
| frontmatter L8 `purpose` | "… — **v0.3.1** 관련 문서" | 2단계 구판 |
| frontmatter L13 `last-review` | `2026-07-20` | v0.3.3 개정일(2026-09-09) 미반영 |
| 본문 L17 제목 | "… — **v0.3.2**" | 구판 |
| 본문 L19 | "**버전**: v0.3.2 \| **최종 갱신**: 2026-07-20" | 구판 |
| 본문 L23~L24 개정이력 | v0.3.3(2026-09-09) 행이 **v0.3.2(2026-07-20) 행보다 위에** 배치 | 시간순 역전 |

## 판정

- **사실오류(C4) 미판정**: 규제 일자·발효일 주장이 아니며 문서관리 메타에 해당(원장 C4 비대상 범위).
- **확정 결함은 currency/문서관리 측면**: 동일 문서 내 버전 식별자가 3종(v0.3.1 / v0.3.2 / v0.3.3) 병존하여 **유효판 식별 불가**. ISO 13485 §4.2.4(문서관리 — 현행 개정상태 식별) 및 사내 `00_프로젝트관리/문서_메타데이터_규칙.md` 위배.
- 발생 경위: audit #1026 정정(2026-09-09) 시 frontmatter만 v0.3.3으로 갱신하고 본문 헤더·purpose·last-review·이력 정렬을 미갱신 — **#1050·#1058과 동형의 '정정 미확산' 패턴 4차**.

## 권고

1. 본문 L17·L19를 v0.3.3 / 최종 갱신 2026-09-09로 정정, frontmatter `purpose`에서 버전 문자열 제거(또는 v0.3.3).
2. `last-review`를 2026-09-09로 갱신, `review-due` 재산정.
3. 개정이력 표를 시간 오름차순으로 재정렬.
4. **재발 방지**: 정정 커밋 시 frontmatter·본문 헤더·개정이력 3자 동기화를 체크 항목으로 편입(CI grep 검사 후보 — `version:` 값과 본문 `**버전**:` 값 일치 검증).

실운영 문서 미참고. web_verification: n/a (문서 내부 정합 점검).

---

## 종결 (2026-09-22, audit-drain 스프린트)

- `PMS_개요.md` 정정: 본문 H1 헤더·`**버전**` 라인 v0.3.2 → **v0.3.3**, 최종 갱신 2026-07-20 → **2026-09-09**, frontmatter `purpose` v0.3.1 → v0.3.3, `last-review` **2026-09-09**·`review-due` **2027-09-09** 재산정, 개정이력 v0.3.3 행을 v0.3.2 행 **아래로 이동**(시간 오름차순 복원).
- **동일 오류클래스 전 저장소 일괄 교정(proactive)**: frontmatter `version:` ↔ 본문 H1 `— vX` ↔ 본문 `**버전**: vX` 3자 불일치를 전 문서 스캔(issue-drafts·자동생성 원장 제외, 39건 적발) → **자기버전 식별자 불일치 25건(19문서 + purpose 자기버전 6문서) 정정**. 잔여 14건은 11·12 로그류 `purpose`가 **대상 문서의 버전을 참조**하는 정상 표기로 확인(오탐), GSPR 체크리스트는 파일명·제목에 버전이 포함된 템플릿으로 현행 유지.
  - 정정 문서: SOP-DHF-001, SOP-AIDATA-001, IEC_81001-5-1, SOP-DT-001, 설계개발_프로세스, IEC_62304_SW_수명주기, CHK-DR-001, SOP-AIGOV-001, ALARA_지원기능_설계명세, SOP-SBOM-001, AI_구성요소_단위_성능평가, SOP-IA-001, SOP-MR-001, SOP-CAPA-001, PRO-CRP-001, SOP-DOC-001, 문서_기록관리_개요, SOP-SUP-001, SOP-PMS-001, SOP-CC-001, SOP-MFG-001, IEC60601-2-54_형식시험_체크리스트, SOP-UDI-001, 공급자_관리_개요, 프로젝트_개요.
- ISO 13485 §4.2.4(현행 개정상태 식별) 위배 상태 해소. 재발 방지(CI grep 검사) 항목은 governance 계열 audit #1030과 함께 후속 처리 대상으로 이월.

실운영 문서 미참고.
