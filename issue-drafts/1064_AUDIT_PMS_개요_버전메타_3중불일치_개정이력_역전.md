---
title: "audit #1064 (currency/문서관리): PMS_개요.md 버전 표기 3중 불일치(frontmatter v0.3.3 / 본문 헤더 v0.3.2 / purpose v0.3.1) + 개정이력 시간순 역전 + last-review 미갱신"
labels: "audit:currency,prio:P2,risk:low,qms,document-control"
state: open
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
