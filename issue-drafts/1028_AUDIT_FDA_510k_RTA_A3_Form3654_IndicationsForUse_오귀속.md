---
title: "audit #1028 (citation/C3): FDA_510k_RTA A.3 — 'FDA Form 3654 = Indications for Use Statement' 오귀속 (정답 Form 3881)"
labels: "audit:citation,prio:P2,risk:medium,compliance"
---

## 결함 (13_규제평가_체크리스트 스윕, 2026-09-10 등록)

`13_규제평가_체크리스트/FDA_510k_RTA.md` 항목 **FDA-510K-A3**:

```
requirement: FDA Form 3654 — Indications for Use Statement
```

동일 파일 **FDA-510K-A5**는 `Standards Data Report (Form 3654 또는 별도 문서)`로 기재 — 같은 파일 안에서 Form 3654가 서로 다른 두 용도로 중복 귀속되어 내부 모순.

## Tier1 (2026-09-10 직접 확인)

- **FORM FDA 3881 = "Indications for Use"** — FDA 승인 510(k) 문서(K180196) 내 실제 양식 페이지에서 표제 및 양식번호 라인 직접 확인: `FORM FDA 3881 (7/17) Page 1 of 1`.
- **FORM FDA 3654 = Standards Data Report(표준 적합성 요약 양식)** — FDA 510(k) Format Guidance(fda.gov/media/88379) 본문에서 "FDA Form 3654"를 standards form으로 명시.

→ A.3의 Form 번호는 오귀속. A.5(3654 = Standards Data Report)는 정답이므로 유지.

## 수정

- `FDA_510k_RTA.md` FDA-510K-A3: `FDA Form 3654` → **`FDA Form 3881`** (Indications for Use Statement).
- 동일 오류클래스 저장소 전수 grep(`3654`, `3881`) 후 잔존 오기재 확인·정정.

## 체크리스트

- [x] Tier1 원문 확인 (FDA.gov, accessdata.fda.gov)
- [x] A.3 정정
- [x] 동일클래스 전수 스윕
- [ ] 실 제출 시 최신 양식 개정판 재확인 (양식은 개정될 수 있음)

## 참고 링크

- 관련 문서: `13_규제평가_체크리스트/FDA_510k_RTA.md`
- Tier1: https://www.fda.gov/media/88379/download , https://www.accessdata.fda.gov/cdrh_docs/pdf18/K180196.pdf

실운영 문서 미참고. web_verification: yes (FDA.gov 직접 확인, 2026-09-10).
