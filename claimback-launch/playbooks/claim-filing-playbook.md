# Per-Brand Claim Filing Playbook (v0.1 — living doc)

> This document IS the company. Update it after every claim filed.
> Verified facts below from Aug 2026 research; fill gaps during pilot filings.

## Universal rules (all brands)

1. **File as the contractor's authorized agent.** Claims run through THEIR
   distributor/dealer portal accounts. Get a signed Letter of Authorization
   (template in ops/) + portal credentials via their office manager.
2. **The 30-day rule:** distributor-filed claims (e.g., Ferguson — handles
   Carrier, Trane, Rheem, Ruud, American Standard, Goodman) must be filed
   within **30 days of the repair date. Hard deadline, no grace period.**
   → Ops SLA: every intake batch triaged within 24h, newest failures first.
3. **#1 rejection reason = missing documented install date.** Every claim
   package must prove the part was in coverage: original install invoice or
   equipment registration record.
4. **Claim package checklist (every claim):**
   - [ ] Model + serial of unit
   - [ ] Failed part number, lot/date codes if present
   - [ ] Failure description (mode, not just "bad")
   - [ ] Install date proof (invoice/registration)
   - [ ] Repair invoice / work order
   - [ ] Proof of purchase from authorized distributor (invoice or PO#)
   - [ ] Failed part RETAINED — many brands require physical return
     (local branch or prepaid label). Tell the shop: "don't scrap it."
5. **Registration affects eligibility:** most brands require registration
   within 60–90 days of install for full 10-yr parts coverage; unregistered
   drops to ~5-yr base. Carrier = 90 days; Trane = 60 days.
   → Upsell: registration-compliance sweep as part of onboarding.
6. **Reimbursement mechanics:** typically issued as a CREDIT to the
   contractor's distributor account (not a check). Bill our 25% on
   **approval/credit issued**, not cash-out.

## Brand quick-reference

| Brand | Portal / route | Notes | Warranty line |
|---|---|---|---|
| Trane / Am. Standard | ComfortSite dealer portal, or distributor counter | Dealer buys part, refunded after approval. May request maintenance records. | 1-855-338-5765 |
| Carrier / Bryant | Distributor (e.g. Ferguson) or dealer portal | 90-day registration window for extended coverage | 1-800-227-7437 |
| Rheem / Ruud | Distributor or MyRheem | Unlicensed install can void coverage — verify license on file | 1-866-720-2076 |
| Goodman / Daikin | Distributor; labor warranty in-house | — | fill in |
| Bradford White (plumbing) | Wholesaler only — never retail | Strong fit for plumbing wedge | fill in |
| Lennox | LennoxPros | May request maintenance records | fill in |
| Ferguson (distributor) | Single digital form, multi-brand | Paper forms dead since Jul 31 2025. 30-day deadline. | ferguson.com warranty page |

## Per-claim ops workflow

```
Intake (invoice export) 
  → OCR/parse: flag lines w/ part # + "warranty|swap|replace|failed"
  → Cross-check install date vs coverage window
  → Build claim package (checklist above)
  → File via shop's portal/distributor  [log portal, date, claim #]
  → Track to approval (follow up at day 7, 14, 21)
  → Credit issued → invoice shop 25% → update case-study tally
```

## Log every claim

| Date filed | Shop | Brand | Part | $ value | Portal | Status | $ approved | Days to approval | Rejection reason |
|---|---|---|---|---|---|---|---|---|---|

**North-star ops metric: approval rate ≥70% and median days-to-approval.
If a brand runs <50% approval, write down why and fix the package template.**
