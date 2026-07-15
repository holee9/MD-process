---
title: "audit(factuality): SOP-DOC-001 §7(보존기간표) 위험관리파일(RMF) 근거 'ISO 14971 §3.5' 사실오류 — 정답 §4.5(Risk management file)"
labels: "audit:factuality,prio:P0,risk:high"
---

## 대상 (C1×06 전수 스윕)
`06_문서_기록관리/SOP-DOC-001_문서_기록관리_절차.md` L191

> | 위험관리파일(RMF) | 제품 수명 + 5년 | ISO 14971 §3.5 |

## 결함
ISO 14971:2019 조항 구조: §3 = "Terms and definitions"(용어 정의, 하위 §3.1~§3.n은 개별 용어 정의이며 요구사항 조항이 아님). 위험관리파일(Risk management file) 요구사항은 §4 "General requirements for risk management system"의 하위조항 **§4.5 "Risk management file"**에 규정됨(§4.1 General, §4.2 Management responsibilities, §4.3 Competence of personnel, §4.4 Risk management plan, §4.5 Risk management file). "§3.5"는 용어정의 조항 번호이며 RMF 보존·구성 요구사항과 무관 — 조항번호 오귀속.

## Tier1/근거
- 표준 원문(ISO 14971:2019) 직접 구매본 미보유 — web 교차확인(ISO 표준 발췌·해설 복수 소스: ISO/TR 24971:2020 발췌 PDF, 업계 표준해설 자료 등)으로 §4.5="Risk management file" 조항 제목·§4.1~4.5 하위조항 순서 일치 확인. 순수 Tier2(블로그) 단독 근거 아님 — ISO/TR 24971 공식 발췌 포함 복수 독립 소스 교차일치.
- 참고: 동일 오류 패턴(§4.x 계열↔§3.x/§7.x 혼동)은 기존 audit #907(§7 하위조항)·#942(§7.6→§7.5)·#944(§4.1→§4.4)에서도 반복 확인된 자매재발 클래스.

## 판정
P0. 감사관 본문 미수정. 실운영 문서 미참고.
