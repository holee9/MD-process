---
title: "audit(C1/citation): 제조자 측정장비 교정관리(ISO 13485 §7.6) 근거를 MDR Annex I §15/§15.1·§14.2(g)(기기 설계요구)로 귀속 — Tier1 대응은 Annex IX §2.2(e)"
labels: "audit:citation,prio:P2,risk:low"
state: closed
---

## 대상 (2문서 2개소)
| 문서 | 위치 | 현재 기재 |
|---|---|---|
| `05_검사_시험_밸리데이션/검사_시험_밸리데이션_개요.md` | L33 §2 표 '측정장비 관리' 행 EU MDR 열 | `Annex I §15` |
| `05_검사_시험_밸리데이션/SOP-CAL-001_교정관리_절차.md` | L12 frontmatter applicable | `EU MDR 2017/745 Annex I §15.1, §14.2(g)` |

- 클래스: C1 (조항번호/주제 귀속). 표본 32차 (d''') MDR Annex I 잔여 §n 인용 전수 재대조 중 발견.

## 결함
EUR-Lex 공식 PDF (CELEX 02017R0745-20250110) pdftotext 원문 대조:
- Annex I §15 = "Devices with a diagnostic or measuring function" — §15.1: 진단·측정기능 **기기 자체**의 정확도·정밀도·안정성 설계·제조 요구 (제품 GSPR).
- Annex I §14.2(g) = "risks arising where maintenance or calibration are not possible" — **기기 설계**상 유지보수·교정 불가 위험 제거 요구.
- 반면 SOP-CAL-001 §2.1 적용대상은 제조자가 사용하는 시험·계측장비(선량계·누설전류시험기·팬텀·온습도계·캘리퍼스 등)로 ISO 13485 §7.6 영역.
- MDR에서 제조자 시험장비 교정 소급성을 직접 규정한 Tier1 조문: **Annex IX Chapter I §2.2(e)** — "the test equipment to be used; it shall be possible to trace back adequately the calibration of that test equipment."
→ 측정장비 관리의 EU MDR 근거로 Annex I §15/§14.2(g)는 주제 오귀속. 정답 계열 Annex IX §2.2(e) (QMS 문서 요건; NB 심사 §2.3).

## 해석범위 (사실오류 아님)
- SOP-CAL-001 §2.1 'SW 기반 측정 — 선량 표시 SW'가 **자사 제품의 측정기능**(DAP/선량 표시) 검증을 포함한다면 그 한정 범위에서 §15.1 병기는 가능. 단 단독 근거로는 부적합.
- 동 개요 L30/L31 수입검사·공정관리 → Annex IX §2.3(심사)은 §2.2(d)/(e)가 문서요건 본조이나 #975 처리 시 수용된 귀속으로 해석범위 유지.

## 정정 제안 (빌더 처리, 감사관 본문 미수정)
1. 개요 L33: `Annex I §15` → `Annex IX Ch.I §2.2(e) (시험장비 교정 소급성)`
2. SOP-CAL-001 L12: `Annex I §15.1, §14.2(g)` → `Annex IX Ch.I §2.2(e)` (+ 제품 측정기능 한정 시 `Annex I §15.1` 병기 주석)

## Tier1
EUR-Lex Regulation (EU) 2017/745 consolidated 02017R0745-20250110 공식 PDF (curl → pdftotext) Annex I §14.2(a)~(g)·§15·§15.1·Annex IX §2.2(a)~(e)·§2.3 원문 직접 대조. web:ok.

## 자매 선례
#975 (Annex I §10/§14 진단기기 오귀속, closed) — 동일 문서군·동일 클래스.

실운영 문서 미참고.

## 처리 결과 (빌더, 2026-11-18 — FACTUALITY 드레인 스프린트)
| 문서 | 정정 |
|---|---|
| SOP-CAL-001 v0.2.3 L12 | `Annex I §15.1, §14.2(g)` → `Annex IX Ch.I §2.2(e)` + §15.1은 제품 측정기능 검증 한정 병기, §14.2(g) 삭제 |
| 검사_시험_밸리데이션_개요 v0.2.1 L33 | `Annex I §15` → `Annex IX Ch.I §2.2(e) (시험장비 교정 소급성)` |

- Tier1 재확인: EUR-Lex CELEX 02017R0745-20250110 공식 PDF pdftotext — Annex IX §2.2(e) "the test equipment to be used; it shall be possible to trace back adequately the calibration of that test equipment." 원문 일치.
- 동일 클래스 일괄 점검: 저장소 `Annex I §15` 인용 잔여 2개소(X-ray_장비_안전성능_표준_매핑 L107 '진단기기', 영상품질_QC_프로토콜 frontmatter)는 **제품** 측정·진단기능 맥락 → 해석범위 PASS.

실운영 문서 미참고.
