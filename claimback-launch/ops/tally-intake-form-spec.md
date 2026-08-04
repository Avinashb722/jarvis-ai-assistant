# Tally Form Build Spec — "Free Warranty Audit" Intake

**Build at:** tally.so → New form. Copy-paste each block below.
**Design settings:** Title "Free Warranty Audit — ClaimBack" · one question per page ON
(progress feels fast) · progress bar ON · brand color `#0d6e5f`.

**Form strategy:** qualify → capture contact EARLY (before the heavy ask) →
tease their number → then request the invoice export. If they bail at the
export step, you still have a qualified lead with a phone number.

---

## Page 1 — Hook (Statement block, no input)

**Heading:** Let's find out what you're owed.
**Text:** Most shops recover only 12–15% of the manufacturer warranty credits
they're entitled to. This free audit tells you your number in 3 business days.
Takes about 3 minutes. No cost, no obligation — ever.
**Button:** Start →

## Page 2 — Company basics

**Q1 · Short answer · required**
> What's your company name?

**Q2 · Dropdown · required**
> What kind of work do you do?
- HVAC (residential/light commercial service & replacement)
- Plumbing
- Both HVAC & plumbing
- Other

**Q3 · Multiple choice · required**
> How many field techs do you run?
- 1–4
- 5–14
- 15–39
- 40+

*(Scoring note, not in form: 1–4 = Tier C nurture; 5–39 = core ICP; 40+ = founder handles personally.)*

## Page 3 — Contact (BEFORE the heavy questions)

**Q4 · Short answer · required** → Your name
**Q5 · Email · required** → Best email for the audit report
**Q6 · Phone · required** → Best phone number
*Helper text:* We'll only call about your audit. No spam, ever.

## Page 4 — The pain (also your discovery data)

**Q7 · Multiple choice · required**
> When a tech replaces a part that's still under manufacturer warranty
> (compressor, coil, control board, water heater)… who files the claim?
- Our office manager files them all *(→ great, the audit confirms it)*
- We file the big ones, small ones slip
- The distributor handles it when we remember to ask
- Honestly? It depends / not sure
- We rarely file them

**Q8 · Multiple choice · required**
> Which brands do you install/service most? (pick up to 3 — checkbox, limit 3)
- Carrier / Bryant
- Trane / American Standard
- Lennox
- Rheem / Ruud
- Goodman / Daikin / Amana
- York
- Bradford White / AO Smith (water heaters)
- Other

**Q9 · Multiple choice · required**
> What do you run the office on?
- ServiceTitan
- Housecall Pro
- Jobber
- FieldEdge / other field software
- QuickBooks only
- Paper / spreadsheets

## Page 5 — Conditional tease (Logic: show after Q7)

**IF Q7 = "rarely file" / "depends" / "distributor handles":**
**Statement:** Based on shops your size with that answer, there's a good chance
you have **$15,000–$40,000/year** sitting unfiled. Let's get your exact number.

**IF Q7 = "office manager files them all":**
**Statement:** Nice — you're ahead of most. The audit will either confirm your
office is catching everything (free peace of mind) or find the stragglers.
Either way you win.

## Page 6 — The ask (invoice upload OR promise)

**Q10 · Multiple choice · required**
> Last step. We need ~90 days of job invoices to run the audit. What's easiest?
- Upload a CSV/Excel export right now
- Email it to me and I'll send an export from {{their software}}
- I'd rather hop on a 10-minute call first

**Q11 · File upload · shown only if "Upload right now"**
> Drop your export here (CSV, XLSX, or PDF — up to 10 files)
*Helper:* From ServiceTitan: Reports → Invoices → Export. From QuickBooks:
Sales → Invoices → Export to Excel. We sign an NDA on request; we never see
customer payment details.

**Q12 · Multiple choice · shown only if "10-minute call first"**
> When's good? *(or embed Cal.com inline block here instead)*
- Mornings (8–11am)
- Midday (11am–2pm)
- Afternoons (2–5pm)

## Thank-you page

**Heading:** You're in. Here's what happens next.
**Text:**
1. We review your invoices for unfiled manufacturer warranty claims.
2. Within **3 business days** you get a one-page report: every claim we found,
   its dollar value, and its filing deadline.
3. You decide if you want us to file them. If yes — we handle everything and
   you keep 75%. If no — the report is yours to keep, free.

⏱ One heads-up: distributor claims expire **30 days after the repair date**,
so the sooner we run this, the more of your money is still recoverable.

Questions right now? Call/text {{PHONE}} — a human answers.

---

## Integrations (Tally settings → Integrations)

1. **Notifications → email** you on every submission.
2. **Zapier** (from the Phase-4 plan):
   - Trigger: New Tally submission
   - HubSpot: create/update contact + deal, stage = "Audit Sent",
     map Q3 (techs) and Q7 (filing habits) to custom properties
   - Slack #leads: `🔥 {{Q1}} — {{Q3}} techs — files claims: "{{Q7}}" — {{Q6}}`
   - IF Q10 = "call first" → also create a task "Call {{Q4}} TODAY"
3. **Hidden fields** (Tally supports URL params): add `source`, `sequence`
   hidden fields; link from cold email as `...?source=cold-email&sequence=t3`
   so you know which touch converts.

## Response-time rule (write it on the wall)

**Speed-to-lead: call every submission within 5 minutes during business hours.**
A trades owner filling out a form is reachable RIGHT THEN and gone an hour later.
The 5-minute callback converts 3–5× better than same-day.

---

*When the form is live: send me the tally.so URL → I update the landing page
CTA + the {{audit_link}} vars in the email sequence and redeploy.*
