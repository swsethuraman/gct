# A bookkeeping error in the `δ = 8` Phase-B rows, found and corrected

Session 43, 2026-09-03, found at 15:56 during a routine status check on the
committed log (`s43: per6 delta=8 (9,5,4,3,2,1): a=3 mult=1 units=2`) — a
`units > 0` row is exactly what Phase B's stopping rule exists to catch, so it
was looked at immediately.

## What happened

When the injectivity route was extended from `a = 1` to any `a` (§4 of
`docs/sixrow_close.md`), the driver's call site in `analysis/wk9_s43_per6.py`
was left passing the literal `1` where the weight's own `a` belongs:

```
res = inject_one(delta, m, 1, verbose=True)     # wrong
res = inject_one(delta, m, a, verbose=True)     # corrected
```

`inject_one` returns `a_exp` on a `NONSINGULAR` certificate, so every `a ≥ 2`
weight measured by that path was **banked with `mult = 1`** and therefore with
a spurious `units = a − 1 > 0`.  **21 rows** of `results/s43_per6.md` were
affected, all at `δ = 8`, `a` between 2 and 5.

## What the certificates actually proved

Nothing was mis-measured; only mis-recorded.  With `a_exp = 1` the driver built
`Ev` with `K = 1 + 8 = 9` evaluation rows instead of `a + 8`, and certified
`[M ; Ev]` injective.  Injectivity gives `dim ker[M;Ev] = a − mult_9 = 0`, so
`mult_9 = a`, where `mult_9` is the multiplicity measured at those 9 points; and
`mult ≥ mult_9` because adding evaluation rows cannot lower the rank.  With
`mult ≤ a` always, **`mult = a` at all 21 weights** — the empty verdict, which
is what the row should have said.  A smaller `K` makes injectivity *harder*, not
easier, so the certificates are if anything stronger than the pre-registered
ones; they are simply not the pre-registered ones.

## What was done

The 21 rows were **removed** from `results/s43_per6.md` rather than edited in
place, the call site was corrected, and every one of the 21 weights was
**re-measured from scratch** by the corrected driver at the pre-registered
`a + 8` points, both primes.  The re-measured rows are the ones in the file; no
row in `results/s43_per6.md` was produced by the faulty path.

No Phase-A row, no `δ = 7` row, and no `a = 1` row was affected: at `a = 1` the
literal `1` was correct, which is why the `δ = 7` closure and the
thirteen-weight cross-check of `results/s43_inject_crosscheck.md` are untouched.
The `δ = 7` theorem of §4 rests only on `a = 1` weights.

## Why it was not caught by the validation

`results/s43_inject_crosscheck.md` validated the `a ≥ 2` extension by calling
`inject_one` **directly** with the right `a` (13 of 13 agreements, and those
runs are correct).  The defect was in the *driver's* call, one level up, on a
path the cross-check did not exercise.  The lesson for the next session is the
narrow one: validate the driver, not only the routine it calls.
