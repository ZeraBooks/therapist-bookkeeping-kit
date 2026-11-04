"""Check a therapy practice's month in this repo's layout.

1. Each insurance EFT matches its remittance total, and the EFTs add up to
   the insurance collected by all clinicians.
2. Each contract clinician's pay is their split rate times what they
   collected (insurance + self-pay + late-cancel fees), and the total agrees
   with the contract clinician line in the month.
3. Profit is every "In profit" line in the month file added up.

Usage:
  python3 check_practice_month.py insurance-remittances.csv clinician-collections.csv october-2026-month.csv
Python 3, standard library only.
"""
import csv
import sys
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def d(cell):
    return Decimal(cell.strip()) if cell and cell.strip() else Decimal("0")


def rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main(remit_path, coll_path, month_path):
    ok = True
    eft_total = Decimal("0")
    by_payer = {}
    for r in rows(remit_path):
        remit, eft = d(r["Remittance total"]), d(r["EFT deposited"])
        if remit != eft:
            ok = False
            print(f"{r['EFT date']} {r['Payer']}: remittance says {remit:,.2f}, bank got {eft:,.2f}")
        eft_total += eft
        by_payer[r["Payer"]] = by_payer.get(r["Payer"], Decimal("0")) + eft
    print(f"Insurance EFTs: {eft_total:,.2f}")
    for payer, amt in sorted(by_payer.items()):
        print(f"  {payer}: {amt:,.2f} ({amt / eft_total * 100:.1f}% of insurance)")

    ins = selfpay = late = pay = Decimal("0")
    for r in rows(coll_path):
        i, s, lc = d(r["Insurance collected"]), d(r["Self-pay sessions collected"]), d(r["Late-cancel fees collected"])
        ins, selfpay, late = ins + i, selfpay + s, late + lc
        collected = i + s + lc
        if r["Paid as"].strip().lower() == "contract":
            share = (collected * d(r["Split rate"])).quantize(CENT, ROUND_HALF_UP)
            pay += share
            print(f"{r['Clinician']}: collected {collected:,.2f}, paid {share:,.2f}")
        else:
            print(f"{r['Clinician']}: collected {collected:,.2f}")
    if ins != eft_total:
        ok = False
        print(f"Insurance collected by clinician is {ins:,.2f}, EFTs are {eft_total:,.2f}")

    income = expenses = Decimal("0")
    lines = {}
    for r in rows(month_path):
        amt = d(r["Amount"])
        lines[r["Account"]] = lines.get(r["Account"], Decimal("0")) + amt
        if r["In profit"].strip().lower() == "yes":
            if amt >= 0:
                income += amt
            else:
                expenses -= amt
    checks = [
        ("Insurance revenue", ins),
        ("Self-pay revenue", selfpay),
        ("Cancellation fees", late),
        ("Contract clinician payments", -pay),
    ]
    for acct, expected in checks:
        if lines.get(acct, Decimal("0")) != expected:
            ok = False
            print(f"{acct} in the month is {lines.get(acct, Decimal('0')):,.2f}, collections say {expected:,.2f}")
    print(f"Revenue {income:,.2f}, expenses {expenses:,.2f}, profit before owner pay {income - expenses:,.2f}")
    print("All checks pass." if ok else "Some checks failed; see above.")
    return ok


if __name__ == "__main__":
    a = sys.argv[1:] + [None] * 3
    sys.exit(0 if main(a[0] or "insurance-remittances.csv", a[1] or "clinician-collections.csv",
                       a[2] or "october-2026-month.csv") else 1)
