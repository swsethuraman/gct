# The six-row record — every cell, reconciled across sessions 36, 41, 43 and 45

Integrator, 2026-09-04, at repository tip `a1c8e7f`.  Rebuilt from the five
ledgers themselves (`results/s36_ledger.md`, `results/s36_aone.md`,
`results/s41_ledger.md`, `results/s43_ledger.md`, `results/s45_ledger.md`) by
`analysis/wk9_int_record.py`, not copied from any coverage document.  This file
supersedes the per-session totals in `results/s41_coverage.md`,
`results/s43_coverage.md` and `docs/sparse_det_route.md` §7, each of which was
current when written and none of which knows about the sessions that ran
concurrently with it.

## The count

**188 distinct six-row cells (`n = 4`, `ℓ(λ) = 6`, `a ≥ 1`) have a measured
`mult_det`, carrying 585 ambient units, and `mult_det = a` at every one.**

The cell sets are disjoint: 34 from s36's `a ≥ 2` sweep, 19 more from s36's
`a = 1` extension, 37 from s41, 89 from s43, 9 from s45 — `34 + 19 + 37 + 89 + 9
= 188`, with **no cell measured twice and no disagreement anywhere**.  (The
sessions ran on disjoint ranges: s43 worked at `n_χ ≤ 20,000`, s45 at
`n_χ ≥ 23,700`.)

| `δ` | cells | units | eligible (`λ_1 ≥ δ`) | onset-only (`λ_1 < δ`) |
|---|---|---|---|---|
| 6 | 16 | 19 | 15 | 1 |
| 7 | 65 | 148 | 64 | 1 |
| 8 | 67 | 282 | 67 | 0 |
| 9 | 40 | 136 | 40 | 0 |
| **all** | **188** | **585** | **186** | **2** |

Cross-check: session 43 exhausted the reachable set at `δ = 7, 8` with 123
eligible cells at `n_χ ≤ 20,000`; session 45 added 8 eligible cells above that
frontier at those degrees.  `123 + 8 = 131 = 64 + 67`. ✓

## By balance (`λ_1 − λ_6`)

| balance | 0 | 4 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cells | 1 | 1 | 4 | 3 | 8 | 9 | 14 | 15 | 17 | 19 | 17 | 13 | 11 | 11 | 13 | 9 | 7 | 5 | 6 | 3 | 2 |

**A correction to `results/s45_ledger.md`.**  Its closing line reads "best
balance measured: 4".  That is right for `δ ≥ 7`, but the most balanced six-row
cell ever measured is `(4,4,4,4,4,4)` at `δ = 6` — **balance 0** — banked by
session 36's `a = 1` extension (`results/s36_aone.md`, `n_χ = 2804`,
`mult_det = 1`, `mult_pad = 0`).  The rectangular weight has been reachable
since s36 at `δ = 6`; what s45 opened is balance 4–7 at `δ = 7, 8`, where
`n_χ` is two orders of magnitude larger.

## The determinant side

`mult_det = a` at all 188 cells, across `δ = 6, 7, 8, 9`.  **The determinant's
six-row ideal has never been observed to be nonzero.**  No cell has
`mult_pad > mult_det`, so `D ≤ 0` everywhere and no obstruction exists at any
measured cell.

What this earns, stated as the reviews require: *no six-row determinant equation
occurs at any measured cell of degree ≤ 9.*  It is not a statement about the
degrees themselves — the balanced corner at `δ = 8, 9` and every `λ_1 < δ` cell
above `n_χ ≈ 3·10^5` remain unmeasured.

## The pad side — all thirteen bites, with proof status

`mult_pad = mult_red` at every cell where both are known: **no permanent-specific
equation anywhere in the record.**  `h_pad` is session 42's free normalisation
bound.

| `δ` | `λ` | `a` | `mult_pad` | `D` | `h_pad` | bound | proof of `mult_red` |
|---|---|---|---|---|---|---|---|
| 6 | `(4,4,4,4,4,4)` | 1 | 0 | −1 | **0** | fires, exact | `h_pad = 0` proves it |
| 7 | `(10,8,7,1,1,1)` | 3 | 2 | −1 | **2** | fires, exact | integer lift (s42) |
| 8 | `(11,9,9,1,1,1)` | 3 | 1 | **−2** | **1** | fires, exact | integer lift, 2 vectors (s42) |
| 8 | `(11,10,8,1,1,1)` | 4 | 2 | **−2** | **2** | fires, exact | integer lift, 2 vectors (integrator) |
| 8 | `(12,9,8,1,1,1)` | 6 | 4 | **−2** | **4** | fires, exact | mod-`p` — **lift outstanding** |
| 8 | `(12,10,7,1,1,1)` | 9 | 7 | **−2** | **7** | fires, exact | mod-`p` — **lift outstanding** |
| 8 | `(13,8,8,1,1,1)` | 3 | 2 | −1 | 3 | silent | integer lift (s42) |
| 8 | `(13,9,7,1,1,1)` | 11 | 10 | −1 | 11 | silent | mod-`p` — lift outstanding |
| 8 | `(13,10,6,1,1,1)` | 9 | 8 | −1 | 9 | silent | integer lift (integrator) |
| 8 | `(13,12,4,1,1,1)` | 3 | 2 | −1 | 3 | silent | integer lift (s42) |
| 8 | `(14,8,7,1,1,1)` | 9 | 8 | −1 | 11 | silent | mod-`p` — lift outstanding |
| 9 | `(16,13,4,1,1,1)` | 7 | 6 | −1 | 9 | silent | mod-`p` — lift outstanding |
| 9 | `(17,12,4,1,1,1)` | 8 | 7 | −1 | 12 | silent | mod-`p` — lift outstanding |

Two readings, both computed here rather than taken from a session:

1. **The bound is exact whenever it fires** — 6 of 13 bites, exact at all 6, no
   counterexample anywhere in the record.  This is the evidence behind the
   exactness conjecture (`docs/s43_review.md` §2, session 47's brief).
2. **At `δ = 8` — where the reachable set is complete — it fires at exactly the
   four `D = −2` cells and nowhere else**, across all 33 in-family cells with
   `a ≥ 1`.  So at that degree the second unit is a normalisation phenomenon and
   the first is not.  At `δ = 6, 7` it also fires on `D = −1` cells, so
   "fires ⟺ two units" is a `δ = 8` statement, not a general one; "fires ⟹
   exact" is the general one.

Every bite lies at a weight of shape `(λ_1, λ_2, λ_3, 1, 1, 1)` except
`(4,4,4,4,4,4)_6`, the rectangular invariant — session 43's family finding,
which held at `δ = 9` where it was used as a prediction.

## Outstanding

Six bites rest on mod-`p` vectors and need `analysis/wk9_s42_lift.py` before the
word "generator" is used of them — in priority order, the two remaining `D = −2`
cells `(12,9,8,1,1,1)_8` and `(12,10,7,1,1,1)_8`, which need **two** independent
integer vectors each, then the four `D = −1` cells.  This is Phase C of session
47's brief.
