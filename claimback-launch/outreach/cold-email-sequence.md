# ClaimBack Cold Outbound — 6 touches / 12 days

**Vars:** `{{first_name}}` `{{company}}` `{{metro}}` `{{sender}}`
**Rules:** 30–50 sends/day/inbox after 14-day warm-up. Plain text, no images, no links in touch 1 (deliverability). Phone touches scripted below.

---

## Touch 1 — Day 1 — Email: found-money hook

**Subject A:** `{{company}}'s unfiled warranty claims`
**Subject B:** `who files your warranty claims?`

```
{{first_name}} — quick question: when your techs swap a compressor or
water heater that's still under manufacturer warranty, does someone at
{{company}} actually file the claim with Carrier or Rheem every time?

Industry data says most shops recover only 12–15% of what they're owed.
For a shop your size that's usually $20–60K/yr left on the table.

We find it and file it through your existing distributor accounts.
You keep 75%. No recovery, no fee.

Want a free audit of your last 90 days of invoices? You send an export,
we send back a dollar figure in 3 days.

— {{sender}}, ClaimBack
```

## Touch 2 — Day 3 — Phone (office manager)

> "Hi, this is {{sender}} from ClaimBack — I emailed {{owner_first}} about
> manufacturer warranty reimbursements. Real quick: when a tech replaces a
> part under warranty, does the claim actually get filed every time?
> ...Right — that's exactly why I'm calling. Ferguson gives you 30 days
> from the repair date, hard deadline, so every month that slips is money
> gone for good. We file them for you, you only pay from what we recover.
> Who'd be the right person to run a free audit past?"

**Voicemail (if no answer):**
> "Hi, {{sender}} from ClaimBack. Most HVAC shops only collect about 15%
> of the manufacturer warranty credits they're owed — the rest expires,
> usually 30 days after the repair. We file them for you, no fee unless
> money comes back. I'll send the details to {{email}}. Thanks."

## Touch 3 — Day 5 — Email: proof

**Subject:** `$38,000 in unfiled claims (real number)`

```
{{first_name}} — real example from the industry: a shop installed 5,200
warrantable parts in a year. 208 failed under warranty. They filed 31.

The other 177 — about $38,000 in manufacturer credits — just expired.

That's not an outlier, it's the norm. Shops that file systematically go
from ~15% recovery to 65–75%.

The audit is free and tells you YOUR number: {{audit_link}}

— {{sender}}
```

## Touch 4 — Day 8 — Phone + reference the range

> "{{first_name}}, {{sender}} again from ClaimBack. Shops your size that
> we audit typically show $15–40K a year in unfiled claims. Ten minutes
> to send us an invoice export, three days to your number, zero cost.
> Can I send the intake link to {{email}}?"

## Touch 5 — Day 10 — Email: direct ask

**Subject:** `10 minutes → your number`

```
{{first_name}} — last useful email, I promise.

The free audit takes you 10 minutes (one export from ServiceTitan /
Housecall / QuickBooks). We do the rest and hand you a dollar figure.

If it's small, great — you're already tight and you've lost nothing.
If it's $20K+, you'll want to know before this quarter's claims expire.

Intake link: {{audit_link}}. Or reply "send it" and I'll email it.

— {{sender}}
```

## Touch 6 — Day 12 — Email: breakup (true urgency)

**Subject:** `closing your file`

```
No response needed — I'll close the file at {{company}}.

One thing worth knowing either way: most distributor-filed claims
(Ferguson handles Carrier, Trane, Rheem, Goodman) have a hard 30-day
deadline from the repair date. No grace period. Whatever failed last
month is expiring right now.

If that ever becomes a priority: {{audit_link}}

Full schedules and full reimbursements to you either way.
— {{sender}}
```

---

## A/B plan
- Wk 1–2: Subject A vs B on touch 1 (open rate). Keep winner.
- Wk 3: test "75/25 split" vs "you keep 75%" phrasing (reply rate).
- Track: open ≥55%, reply ≥3%, audit-intake ≥1% of sends. Below that → rewrite touch 1 before scaling volume.
