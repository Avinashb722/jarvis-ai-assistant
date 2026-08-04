#!/usr/bin/env python3
"""ClaimBack claim finder v0.1 — flags likely-claimable parts in an invoice CSV.

Usage:
    python3 claim_finder.py invoices.csv [--as-of YYYY-MM-DD]

Expected CSV columns (case-insensitive, extra columns ignored):
    date, invoice_id, description, part_number (optional), amount (optional)

Works with raw exports from ServiceTitan / Housecall Pro / QuickBooks —
map columns via --col-date/--col-desc if headers differ.

Output: claims_found.csv + console summary with deadline status.
This is a TRIAGE tool: every flagged row still needs human review against
install-date records before filing.
"""
import argparse
import csv
import re
import sys
from datetime import datetime, timedelta

# --- Signal dictionaries (tune per shop, grow with every audit) ---

# Part classes with typical manufacturer credit ranges (midpoint used for estimate)
PART_CLASSES = {
    "compressor":        (450, 1800, 900),
    "condenser coil":    (300, 900, 500),
    "evaporator coil":   (300, 900, 500),
    "coil":              (250, 800, 400),
    "heat exchanger":    (400, 1200, 700),
    "control board":     (150, 600, 300),
    "circuit board":     (150, 600, 300),
    "inducer motor":     (150, 450, 250),
    "blower motor":      (150, 500, 280),
    "ecm motor":         (200, 600, 350),
    "condenser fan motor": (100, 350, 200),
    "txv":               (100, 300, 180),
    "expansion valve":   (100, 300, 180),
    "contactor":         (30, 90, 50),
    "capacitor":         (20, 60, 35),
    "gas valve":         (120, 350, 200),
    "igniter":           (40, 120, 70),
    "water heater":      (250, 900, 450),
    "anode rod":         (25, 80, 45),
    "thermocouple":      (25, 75, 40),
}

BRANDS = ["carrier", "bryant", "trane", "american standard", "lennox", "rheem",
          "ruud", "goodman", "daikin", "york", "amana", "bradford white",
          "ao smith", "a.o. smith", "navien", "rinnai", "mitsubishi", "bosch"]

# Words suggesting a replacement under existing equipment (claim-eligible context)
REPLACE_HINTS = re.compile(
    r"\b(replac\w+|swap\w*|warrant\w+|failed|failure|defect\w+|bad|burnt|"
    r"shorted|leak\w+|install\w+ new)\b", re.I)

# Words suggesting NOT claimable (new install/quote/maintenance)
NEGATIVE_HINTS = re.compile(
    r"\b(estimate|quote|proposal|maintenance plan|tune[- ]?up|new system|"
    r"full system install|filter change|diagnostic only)\b", re.I)

FILING_WINDOW_DAYS = 30  # distributor hard deadline from repair date


def parse_date(s):
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%m/%d/%y", "%d-%b-%Y", "%m-%d-%Y"):
        try:
            return datetime.strptime(s.strip(), fmt)
        except (ValueError, AttributeError):
            continue
    return None


def scan_row(desc):
    """Return (part_class, est_credit, brand, score) or None."""
    d = desc.lower()
    if NEGATIVE_HINTS.search(d):
        return None
    hit = next(((k, v) for k, v in PART_CLASSES.items() if k in d), None)
    if not hit:
        return None
    part, (lo, hi, mid) = hit
    brand = next((b for b in BRANDS if b in d), "")
    score = 1
    if REPLACE_HINTS.search(d): score += 2
    if brand: score += 2
    if re.search(r"\b[A-Z0-9]{2,}[-][A-Z0-9]{2,}\b", desc): score += 1  # part-number-ish token
    return part, mid, brand.title(), score


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_file")
    ap.add_argument("--as-of", default=None, help="Audit date YYYY-MM-DD (default: max date in file)")
    ap.add_argument("--col-date", default="date")
    ap.add_argument("--col-desc", default="description")
    ap.add_argument("--out", default="claims_found.csv")
    args = ap.parse_args()

    with open(args.csv_file, newline="", encoding="utf-8-sig") as f:
        rdr = csv.DictReader(f)
        rows = [{k.lower().strip(): (v or "").strip() for k, v in r.items()} for r in rdr]
    if not rows:
        sys.exit("No rows found.")

    dates = [d for d in (parse_date(r.get(args.col_date, "")) for r in rows) if d]
    as_of = parse_date(args.as_of) if args.as_of else (max(dates) if dates else datetime.now())

    found, total, filable_total = [], 0.0, 0.0
    for r in rows:
        desc = r.get(args.col_desc, "")
        if not desc:
            continue
        hit = scan_row(desc)
        if not hit:
            continue
        part, est, brand, score = hit
        d = parse_date(r.get(args.col_date, ""))
        deadline = d + timedelta(days=FILING_WINDOW_DAYS) if d else None
        filable = bool(deadline and deadline >= as_of)
        total += est
        if filable:
            filable_total += est
        found.append({
            "repair_date": d.strftime("%Y-%m-%d") if d else "?",
            "invoice_id": r.get("invoice_id", r.get("invoice", "")),
            "part_class": part,
            "brand": brand or "unknown",
            "description": desc[:80],
            "est_credit": est,
            "confidence": ["low", "low", "medium", "medium", "HIGH", "HIGH", "HIGH"][min(score, 6)],
            "file_by": deadline.strftime("%Y-%m-%d") if deadline else "?",
            "status": "FILABLE" if filable else "EXPIRED",
        })

    found.sort(key=lambda x: (x["status"] != "FILABLE", x["file_by"]))
    with open(args.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=found[0].keys() if found else ["none"])
        w.writeheader(); w.writerows(found)

    n_fil = sum(1 for x in found if x["status"] == "FILABLE")
    print(f"\nClaimBack audit triage — {args.csv_file}  (as of {as_of.date()})")
    print(f"  Rows scanned:        {len(rows)}")
    print(f"  Likely claims found: {len(found)}   (est ${total:,.0f} total)")
    print(f"  Still FILABLE:       {n_fil}   (est ${filable_total:,.0f}) <- file these THIS WEEK")
    print(f"  Expired:             {len(found) - n_fil}   (${total - filable_total:,.0f} lost — show this in the audit)")
    print(f"  Detail written to:   {args.out}")
    if n_fil:
        print("\n  Most urgent (soonest deadline):")
        for x in [x for x in found if x["status"] == "FILABLE"][:5]:
            print(f"    {x['file_by']}  {x['part_class']:<20} {x['brand']:<15} ~${x['est_credit']}  [{x['confidence']}]")


if __name__ == "__main__":
    main()
