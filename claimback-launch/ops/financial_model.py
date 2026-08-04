#!/usr/bin/env python3
"""ClaimBack financial model — month-by-month to $1M ARR.

Run: python3 financial_model.py            (base case)
     python3 financial_model.py --bear     (conservative)
     python3 financial_model.py --bull     (aggressive)
Outputs a month table + hiring triggers + CSV (financial_model_<case>.csv).
"""
import csv
import sys

CASES = {
    # new_customers_per_month ramp, ARPU/mo, monthly churn, CAC
    "bear": dict(ramp=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
                 arpu=450, churn=0.035, cac=1100),
    "base": dict(ramp=[2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35],
                 arpu=625, churn=0.025, cac=900),
    "bull": dict(ramp=[3, 5, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68],
                 arpu=750, churn=0.02, cac=750),
}

# Cost assumptions (monthly)
FOUNDER_DRAW = 6000
SDR_COST = 5500          # hired when trigger fires
VA_COST = 2200           # per claims VA (Philippines/LatAm, full time)
CUSTOMERS_PER_VA = 12    # manual era; rises to 25 after automation (month 7+)
TOOLING_BASE = 800       # Apollo, Instantly, HubSpot, hosting, misc
OUTBOUND_SPEND = 1500    # data, phones, sends
GM_TARGET = 0.75


def run(case_name):
    p = CASES[case_name]
    rows, customers, cum_cash = [], 0.0, 0.0
    sdr_hired = va_count = 0
    ops_lead_hired = False
    triggers = []

    for m in range(1, len(p["ramp"]) + 1):
        new = p["ramp"][m - 1]
        churned = customers * p["churn"]
        customers = customers + new - churned
        mrr = customers * p["arpu"]
        arr = mrr * 12

        # Hiring triggers
        if not sdr_hired and mrr > 8000:
            sdr_hired = 1
            triggers.append(f"Month {m}: MRR ${mrr:,.0f} > $8K -> hire SDR (${SDR_COST}/mo)")
        per_va = CUSTOMERS_PER_VA if m < 7 else 25  # automation lands month 7
        needed_vas = max(1, int(customers // per_va) + (1 if customers % per_va else 0)) if customers >= 6 else 0
        if needed_vas > va_count:
            triggers.append(f"Month {m}: {customers:.0f} customers -> claims VA #{needed_vas} (${VA_COST}/mo each)")
            va_count = needed_vas
        if not ops_lead_hired and va_count >= 3:
            ops_lead_hired = True
            triggers.append(f"Month {m}: 3 VAs -> promote/hire Ops Lead (+$4,500/mo)")

        costs = (FOUNDER_DRAW + TOOLING_BASE + OUTBOUND_SPEND
                 + sdr_hired * SDR_COST + va_count * VA_COST
                 + (4500 if ops_lead_hired else 0)
                 + new * p["cac"] * 0.4)   # 40% of CAC is cash (rest is labor already counted)
        cogs = mrr * (1 - GM_TARGET)
        net = mrr - cogs - costs
        cum_cash += net
        rows.append(dict(month=m, new=new, churned=round(churned, 1),
                         customers=round(customers, 1), mrr=round(mrr),
                         arr=round(arr), costs=round(costs + cogs),
                         net=round(net), cum_cash=round(cum_cash)))
        if arr >= 1_000_000:
            break

    return rows, triggers


def main():
    case = "base"
    if "--bear" in sys.argv: case = "bear"
    if "--bull" in sys.argv: case = "bull"
    rows, triggers = run(case)

    print(f"\nClaimBack Financial Model — {case.upper()} case")
    print(f"(ARPU ${CASES[case]['arpu']}/mo, churn {CASES[case]['churn']*100:.1f}%/mo, CAC ${CASES[case]['cac']})\n")
    hdr = f"{'Mo':>3} {'New':>4} {'Churn':>6} {'Cust':>6} {'MRR':>9} {'ARR':>11} {'Costs':>9} {'Net':>9} {'CumCash':>10}"
    print(hdr); print("-" * len(hdr))
    for r in rows:
        print(f"{r['month']:>3} {r['new']:>4} {r['churned']:>6} {r['customers']:>6} "
              f"${r['mrr']:>8,} ${r['arr']:>10,} ${r['costs']:>8,} ${r['net']:>8,} ${r['cum_cash']:>9,}")

    m1 = next((r for r in rows if r["arr"] >= 1_000_000), None)
    print()
    if m1:
        print(f">>> $1M ARR reached in month {m1['month']} "
              f"({m1['customers']:.0f} customers, cumulative cash ${m1['cum_cash']:,})")
    else:
        last = rows[-1]
        print(f">>> $1M ARR NOT reached by month {last['month']} (ARR ${last['arr']:,}) — extend ramp or raise ARPU")
    trough = min(rows, key=lambda r: r["cum_cash"])
    print(f">>> Cash trough: ${trough['cum_cash']:,} in month {trough['month']} (min capital needed + buffer)")
    print("\nHiring triggers:")
    for t in triggers:
        print("  -", t)

    out = f"financial_model_{case}.csv"
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader(); w.writerows(rows)
    print(f"\nCSV written: {out}")


if __name__ == "__main__":
    main()
