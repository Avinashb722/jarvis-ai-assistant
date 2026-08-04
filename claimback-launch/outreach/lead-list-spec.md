# Lead-List Build Spec — First 300 Leads

## Metro selection (start with ONE)

Pick by: hot/humid climate (AC failure volume), fragmented market (no single dominant shop), high housing density. Ranked recommendations:

| Rank | Metro | Why |
|---|---|---|
| 1 | **Phoenix, AZ** | Brutal compressor attrition, huge residential AC install base, thousands of independent shops |
| 2 | Dallas–Fort Worth, TX | Volume + growth; slightly more consolidated |
| 3 | Tampa/Orlando, FL | High humidity failures + strong plumbing (water heater) crossover |

Start with #1 only. One metro = tighter references ("we work with 3 shops in Phoenix"), one filing timezone, faster referral loops. Expand at 25 customers.

## Apollo filters (decision-makers)

```
Industry:        HVAC, Plumbing, Mechanical Contractors
Employee count:  5–100
Titles:          Owner, Founder, President, General Manager,
                 "Office Manager", "Operations Manager", "Service Manager"
Location:        Phoenix–Mesa–Scottsdale MSA
Exclusions:      keywords "new construction", "commercial only",
                 "facilities", "mechanical engineering"
Email status:    Verified only
```
Export cap: 300 contacts (~150–200 companies; grab owner + office manager per company — office manager answers, owner decides).

## Outscraper / Google Maps pass (volume signal)

```
Query:      "hvac repair" OR "air conditioning repair" OR "plumber" — Phoenix AZ
Filters:    reviews >= 100, rating >= 4.0, exclude national franchises
            (One Hour, Horizon, Parker & Sons, ARS, Roto-Rooter)
Output:     name, phone, website, review count
```
Reviews ≥100 ≈ high job volume ≈ high claimable-part volume. Cross-join with Apollo on domain/company name; Maps-only companies (no Apollo emails) go to the **phone-first track** — trades answer phones.

## Enrichment & scoring (in the CRM)

| Signal | How to check | Score |
|---|---|---|
| Review count 100–500 | Maps data | +2 |
| Mentions Carrier/Trane/Lennox/Rheem "dealer" on website | site scan | +3 (confirmed warrantable-brand volume) |
| Uses ServiceTitan/Housecall Pro | careers page, BuiltWith, job posts | +2 (clean export = easy audit) |
| Hiring techs or dispatcher | Indeed/site | +1 (growing = volume) |
| "Family owned since 19xx" | site | +1 (owner-operated, fast decisions) |

Tier A (6+): personalized first line, phone touch on day 2.
Tier B (3–5): standard sequence.
Tier C (<3): hold for later batches.

## Hygiene rules
- 1 sequence per company at a time (owner OR office mgr first, not both — office manager first for 20+ tech shops, owner first for smaller)
- Suppress: current pilots' metro competitors until you have 2 case studies (small-world risk)
- Refresh bounces weekly; keep bounce rate <3% or pause and re-verify
