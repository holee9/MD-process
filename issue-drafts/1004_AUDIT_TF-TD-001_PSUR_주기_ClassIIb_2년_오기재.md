---
title: "audit(factuality): TF-TD-001 §13 체크리스트 — PSUR 갱신주기 'Class IIa 이상: 최소 2년 주기' 오기재 (정답: Class IIb/III 연 1회, IIa만 2년 — 자사 Class IIb 직접 해당)"
labels: "audit:factuality,prio:P1,risk:high"
state: closed
---

## 대상 (C2×06_문서_기록관리 스윕)

`06_문서_기록관리/TF-TD-001_의료기기파일_기술문서_관리.md` L487 (§13 기술문서 유지 체크리스트):

```
| 8.2 | PSUR 작성 (해당 시) | Class IIa 이상: 최소 2년 주기 | | |
```

## 결함

EU MDR 2017/745 **Art.86(1)** 원문(Tier1, 조문 전문 직접 열람):

- "Manufacturers of **class IIb and class III** devices shall update the PSUR **at least annually**."
- "Manufacturers of **class IIa** devices shall update the PSUR when necessary and **at least every two years**."

즉 "최소 2년 주기"는 Class IIa에만 해당하며, Class IIb·III는 **연 1회 이상**이다. 저장소 표기 "Class IIa 이상: 최소 2년 주기"는 IIb/III의 주기를 2배 완화한 사실오류. 자사 제품군(X-ray System, Class IIb 비이식형)이 직접 해당하므로 이 표기대로 운영 시 **PSUR 연간 갱신 의무 위반** 가능 — risk:high.

## 계보

원장 C2 클래스 정의 예시("MDR Art.87(2) IIb '매 2년' vs 정답 '연 1회'")와 동일 오류클래스. 08_PMS 카테고리는 C1×08 스윕(2026-07-19)에서 Art.86(1) PASS 확인된 바 있어, 06 카테고리 자매문서에 잔존한 **자매재발** 사례.

## 체크리스트
- [ ] TF-TD-001 L487: "Class IIb/III: 연 1회 이상, Class IIa: 최소 2년 주기(필요 시 수시)"로 정정
- [ ] 전 저장소 "2년 주기" grep으로 동일 오류 확산 확인
- [ ] 검증: EUR-Lex Art.86(1) 재대조

## 근거 (Tier1)
- EU MDR 2017/745 Art.86(1) 조문 전문 (medical-device-regulation.eu 전문 게재본 + WebSearch 독립 교차확인)

## 해소 (2026-07-29, 드레인 스프린트)
- TF-TD-001 §13 L487 'Class IIa 이상: 최소 2년 주기' → 'Class IIb/III: 연 1회 이상, Class IIa: 최소 2년마다(필요 시 수시) — EU MDR Art.86(1)' 정정(v0.7).
- 전 저장소 grep: 잔여 'Class IIa 이상' 2건(EU_MDR_2017_745.md L137, PMS_개요.md L126)은 PSUR **작성 의무 대상** 서술로 정답 — 정정 불요. PSUR 주기 수치 전 문서 정합 재확인.
- Tier1: EU MDR Art.86(1) 조문(기확보 재사용). 실운영 문서 미참고.
