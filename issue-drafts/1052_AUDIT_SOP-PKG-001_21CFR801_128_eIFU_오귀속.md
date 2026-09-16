---
title: "audit(citation): SOP-PKG-001 §5.6 'FDA 21 CFR 801.128 Guidance' 전자 IFU 근거 오귀속 — 801.128은 전략비축물자(SNS) 라벨링 예외 조항"
labels: "audit:citation,prio:P2,risk:low,fda,labeling,eifu"
opened: 2026-09-17
state: open
---

## 대상 (C4×04_제조공정_관리 전수 스윕 중 부수 적출 — 귀속 클래스 C1)

`04_제조공정_관리/SOP-PKG-001_라벨링_포장관리_절차.md` L227 (§5.6 전자 라벨링)

> 1. SW 제품 또는 SW 업데이트는 전자 IFU 제공 가능 (EU MDR Annex I §23.1(f), Commission Implementing Regulation (EU) 2021/2226, **FDA 21 CFR 801.128 Guidance**)

## 결함

**21 CFR 801.128의 실제 표제**: "Exceptions or alternatives to labeling requirements for medical devices held by the Strategic National Stockpile."
= 전략국가비축물자(SNS)에 포함되거나 포함될 의료기기에 한하여, 라벨링 요구사항 준수가 제품의 안전성·유효성·가용성에 악영향을 줄 수 있는 경우 FDA Center Director가 예외·대체를 승인할 수 있도록 하는 조항이다. Part 801 Subpart D(Exemptions From Adequate Directions for Use) 소재.

**전자 IFU(eLabeling)와 무관하다.** 미국의 처방용 의료기기 전자 IFU 허용 근거는 21 CFR 801.109(c)(처방기기 adequate directions for use 면제 — 제조자가 IFU를 라벨 외 수단으로 제공) 계열이며, 801.128을 eIFU 근거로 인용한 사례는 Tier1 어디에도 없다. 또한 "Guidance"라는 접미도 부정확하다 — 801.128은 **가이던스가 아니라 시행규칙(CFR 조문)** 이다.

동일 오류 클래스(무관 조항·무관 표준을 근거로 오귀속): audit #1011 / #1021 / #1022 / #1028 / #1030 자매재발 6차.

## 증거 등급

**Tier1**: eCFR 현행본(Title 21 > Ch. I > Subch. H > Part 801 > Subpart D > §801.128) 및 govinfo CFR 연간판 표제부 확인 — 표제·소재 일치. (Tier2 LII는 보조 확인용, 사실 근거 아님.)

## 판정

**P2 / risk:low — 사실오류(citation/attribution) 확정.**

라벨링 절차서의 규제근거 표기이므로 심사 시 지적 가능성은 있으나, 본문 실체 요구사항(전자 IFU URL 라벨 인쇄, 접근성 검증, 종이 IFU 무상 제공 등)은 EU 2021/2226 기반으로 정확하게 기술되어 있어 절차 실행 오류로는 전개되지 않는다.

**정정 권고**: L227의 `FDA 21 CFR 801.128 Guidance` → `FDA 21 CFR 801.109(c)(처방기기 IFU 제공 요건)` 으로 대체하거나, 미국 eIFU 근거를 특정할 수 없다면 해당 괄호 인용에서 **삭제**하고 EU 근거만 유지할 것. 확정 전 FDA eLabeling 관련 현행 가이던스(있을 경우 문서번호 포함) Tier1 대조를 선행할 것.

## 부기 (사실오류 아님)

- 동 문서 §5.1 eIFU 웹사이트 유지 "제품 수명 종료 후 최소 15년"은 Commission Impl. Reg. (EU) 2021/2226 근거로 기존 C2×04 사이클에서 PASS 확정된 값이며 본 이슈와 무관하다.
- 2021/2226 자체의 발효일(2021-12-14 채택·OJ 게재 후 20일 경과) 및 구 Reg. (EU) No 207/2012 경과적용 종료(2024-05-26)는 문서에 미기재이나, **일자 주장 자체가 부재**하므로 C4 결함으로 판정하지 않는다(보완 권고 수준).
