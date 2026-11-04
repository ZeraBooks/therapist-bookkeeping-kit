# Therapist bookkeeping kit

Bookkeeping for a therapy practice records insurance payments and self-pay
sessions separately, grosses card payments back up before processor fees,
books late-cancellation fees as revenue, pays contract clinicians their agreed
share of what they collect, and keeps owner pay out of expenses. This kit has
the chart of accounts, a checklist and a worked month.

## Files

| File | What it is |
|---|---|
| `chart-of-accounts.csv` | A starting chart of accounts for a solo or group practice: insurance, self-pay and cancellation fees as separate income, contract clinician payments, supervision and practice costs. Columns: Number, Name, Type, Detail, Notes. |
| `month-end-checklist.md` | Eight steps for closing a practice's month. No clinical records needed. |
| `insurance-remittances.csv` | A fictional month of insurance EFTs, each matched to its remittance total. |
| `clinician-collections.csv` | The same month's collections by clinician, split into insurance, self-pay sessions and late-cancel fees, with each contract clinician's split rate. |
| `october-2026-month.csv` | The fictional practice's October 2026 on cash basis: every line, its account, and whether it counts in profit. |
| `check_practice_month.py` | Ties EFTs to remittances and to collections, works out each contract clinician's pay, and prints profit before owner pay. Python 3, standard library only. |

## How to use it

1. Import `chart-of-accounts.csv` into your accounting software, or compare it
   with the accounts you have. A solo practice can delete the clinician lines.
2. Each month, fill in copies of `insurance-remittances.csv` from your
   remittance advice and `clinician-collections.csv` from the practice
   software's payments report.
3. Run the check:

   ```
   python3 check_practice_month.py insurance-remittances.csv clinician-collections.csv october-2026-month.csv
   ```

4. Work through `month-end-checklist.md` before you lock the month.

## The worked month

Harborlight Counseling is a fictional practice: the owner and two contract
clinicians paid 60% of what they collect. October 2026, cash basis:

| | Amount |
|---|---|
| Insurance EFTs, 4 payers | 9,860.00 |
| Self-pay card payments for sessions | 5,940.00 |
| Late-cancellation fees | 300.00 |
| **Revenue** | **16,100.00** |
| Card processor fees, 2.9% of 6,240.00 | 180.96 |
| Contract clinicians, 60% of the 7,400.00 they collected | 4,440.00 |
| Practice management and telehealth software | 149.00 |
| Office rent | 1,600.00 |
| Liability insurance | 62.00 |
| Continuing education course | 295.00 |
| **Expenses** | **6,726.96** |
| **Profit before owner pay** | **9,373.04** |

The clinicians' 4,440.00 is worked out from their collections that month,
which is why the books need payments by clinician, not just a total. What the
owner takes home comes out of the 9,373.04 as a draw or salary, depending on
how the practice is set up.

All figures are fictional.

## FAQ

### Is a superbill a receivable for the practice?

No. An out-of-network client pays you in full and sends the superbill to their
insurer. Any reimbursement goes to the client, so nothing more is owed to the
practice.

### Are contract clinicians paid on sessions or collections?

In a split arrangement, usually on what they collected. A session that was
billed but not paid yet isn't in the split until the money arrives. Whether a
clinician is a contractor or an employee depends on how the work is actually
arranged, and your accountant should decide it.

### Can a solo therapist keep the books in a spreadsheet?

It works while the practice is small and you reconcile to the bank every
month. A second payer panel or a clinician on a split is usually when it gets
hard to keep straight.

## Learn more

Full guide: [Bookkeeping for therapists](https://www.zerabooks.com/bookkeeping-for-therapists). Related: [ZeraBooks bookkeeping services](https://www.zerabooks.com/bookkeeping-services).

## License

The content and data in this repository are licensed under
[CC BY 4.0](LICENSE). Free to use and adapt with credit to ZeraBooks.
The code (`*.py`) is licensed under [MIT](LICENSE-CODE).

Maintained by [ZeraBooks](https://www.zerabooks.com).
