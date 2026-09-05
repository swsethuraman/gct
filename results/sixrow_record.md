# The six-row record — every cell, reconciled across sessions 36, 41, 43, 45 and 46

Integrator, 2026-09-04, at repository tip `543e394`.  The 188-cell base was
rebuilt from the five ledgers themselves (`results/s36_ledger.md`,
`results/s36_aone.md`, `results/s41_ledger.md`, `results/s43_ledger.md`,
`results/s45_ledger.md`) by `analysis/wk9_int_record.py`; session 46's five
cells and session 47's refutation were folded in by hand from
`results/s46_ledger.md` and `docs/exactness.md`.  This file supersedes the
per-session totals in `results/s41_coverage.md`, `results/s43_coverage.md` and
`docs/sparse_det_route.md` §7, each of which was current when written and none
of which knows about the sessions that ran concurrently with it.

## The count

**193 distinct six-row cells (`n = 4`, `ℓ(λ) = 6`, `a ≥ 1`) have a measured
`mult_det`, carrying 593 ambient units, and `mult_det = a` at every one.**

The cell sets are disjoint: 34 from s36's `a ≥ 2` sweep, 19 more from s36's
`a = 1` extension, 37 from s41, 89 from s43, 9 from s45, 5 from s46 —
`34 + 19 + 37 + 89 + 9 + 5 = 193`, with **no cell measured twice and no
disagreement anywhere**.  (The sessions ran on disjoint ranges: s43 worked at
`n_χ ≤ 20,000`, s45 at `n_χ ≥ 23,700`, s46 in the balanced band at `δ = 7`.)

| `δ` | cells | units | eligible (`λ_1 ≥ δ`) | onset-only (`λ_1 < δ`) |
|---|---|---|---|---|
| 6 | 16 | 19 | 15 | 1 |
| 7 | 70 | 156 | 69 | 1 |
| 8 | 67 | 282 | 67 | 0 |
| 9 | 40 | 136 | 40 | 0 |
| **all** | **193** | **593** | **191** | **2** |

Cross-check: session 43 exhausted the reachable set at `δ = 7, 8` with 123
eligible cells at `n_χ ≤ 20,000`; session 45 added 8 eligible cells above that
frontier at those degrees; session 46 added 5 more at `δ = 7` in the balanced
band.  `123 + 8 + 5 = 136 = 69 + 67`. ✓

## By balance (`λ_1 − λ_6`)

| balance | 0 | 4 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cells | 1 | 2 | 4 | 7 | 8 | 9 | 14 | 15 | 17 | 19 | 17 | 13 | 11 | 11 | 13 | 9 | 7 | 5 | 6 | 3 | 2 |

Session 46 added the balance-4 cell `(8,4,4,4,4,4)_7` and four balance-7 cells.

**A correction to `results/s45_ledger.md`.**  Its closing line reads "best
balance measured: 4".  That is right for `δ ≥ 7`, but the most balanced six-row
cell ever measured is `(4,4,4,4,4,4)` at `δ = 6` — **balance 0** — banked by
session 36's `a = 1` extension (`results/s36_aone.md`, `n_χ = 2804`,
`mult_det = 1`, `mult_pad = 0`).  The rectangular weight has been reachable
since s36 at `δ = 6`; what s45 opened is balance 4–7 at `δ = 7, 8`, where `n_χ`
is two orders of magnitude larger, and what s46 delivered there is the
most balanced *obstruction-eligible* `δ = 7` cell there is.

**A correction to the census, from s46.**  `n_χ` is not `N_S/|Stab|`.  At
`(8,4,4,4,4,4)_7` the true `n_χ` is **92,031**; the census tabulated 83,836,
which is that quotient and is neither an upper nor a lower bound — it is off by
21% in both directions on different cells.  Count `n_χ` by the generator walk
(`results/s46_reach.md` §1), and predict `n_rows` from the same character count
rather than from a fit (§5 there): the fitted `n_rows ≈ 0.88·N_S` was out by a
factor of 2.3 at `(9,8,5,2,2,2)_7`, which is why that cell was not reached.

## The determinant side

`mult_det = a` at all 193 cells, across `δ = 6, 7, 8, 9`.  **The determinant's
six-row ideal has never been observed to be nonzero.**  No cell has
`mult_pad > mult_det`, so `D ≤ 0` everywhere and no obstruction exists at any
measured cell.

What this earns, stated as the reviews require: *no six-row determinant equation
occurs at any measured cell of degree ≤ 9.*  It is not a statement about the
degrees themselves — the balanced corner at `δ = 8, 9` and every `λ_1 < δ` cell
above `n_χ ≈ 3·10^5` remain unmeasured.

## The pad side — all fourteen bites, with proof status

`mult_pad = mult_red` at every cell where both are known: **no permanent-specific
equation anywhere in the record.**  Session 47 strengthened this from a
measurement to a theorem at `δ = 8`: `I(D_6^{per_3})_8 = 0`, so by Prop. 8(1) of
`docs/transfer_lemma.md`, `mult_pad = mult_red` at **every** weight of degree 8 —
the degree where every pad-side bite in the record lives.

`h_pad` is session 42's free normalisation bound.

| `δ` | `λ` | `a` | `mult_pad` | `D` | `h_pad` | bound | proof of `mult_red` |
|---|---|---|---|---|---|---|---|
| 6 | `(4,4,4,4,4,4)` | 1 | 0 | −1 | **0** | fires, exact | `h_pad = 0` proves it |
| 7 | `(8,4,4,4,4,4)` | 2 | 0 | **−2** | **0** | fires, exact | `h_pad = 0` proves it |
| 7 | `(10,8,7,1,1,1)` | 3 | 2 | −1 | **2** | fires, exact | integer lift (s42) |
| 8 | `(11,9,9,1,1,1)` | 3 | 1 | **−2** | **1** | fires, exact | integer lift, 2 vectors (s42) |
| 8 | `(11,10,8,1,1,1)` | 4 | 2 | **−2** | **2** | fires, exact | integer lift, 2 vectors (integrator) |
| 8 | `(12,9,8,1,1,1)` | 6 | 4 | **−2** | **4** | fires, exact | integer lift, 2 vectors (s47) |
| 8 | `(12,10,7,1,1,1)` | 9 | 7 | **−2** | **7** | fires, exact | integer lift, 2 vectors (s47) |
| 8 | `(13,8,8,1,1,1)` | 3 | 2 | −1 | 3 | silent | integer lift (s42) |
| 8 | `(13,9,7,1,1,1)` | 11 | 10 | −1 | 11 | silent | integer lift (s47) |
| 8 | `(13,10,6,1,1,1)` | 9 | 8 | −1 | 9 | silent | integer lift (integrator) |
| 8 | `(13,12,4,1,1,1)` | 3 | 2 | −1 | 3 | silent | integer lift (s42) |
| 8 | `(14,8,7,1,1,1)` | 9 | 8 | −1 | 11 | silent | integer lift (s47) |
| 9 | `(16,13,4,1,1,1)` | 7 | 6 | −1 | 9 | silent | integer lift (s47) |
| 9 | `(17,12,4,1,1,1)` | 8 | 7 | −1 | 12 | silent | integer lift (s47) |

The **bound** column records, per cell, whether the free normalisation bound
`h_pad` *fires* (`h_pad < a`) and whether it is *exact there* (`h_pad =
mult_red`).  These are per-cell facts.  They are **not** the claim "the bound is
exact whenever it fires," which s47 refuted (see below) — a `mult_red < h_pad`
cell such as `(15,10,8,1,1,1)_9` shows the bound firing without being exact.

**No bite in the six-row record rests on a mod-`p` vector.**  Session 47 closed
all six outstanding lifts, including two independent integer vectors at each of
the two remaining `D = −2` cells.  The word "generator" is now earned at every
row above.

Every bite lies at a weight of shape `(λ_1, λ_2, λ_3, 1, 1, 1)` except
`(4,4,4,4,4,4)_6` and `(8,4,4,4,4,4)_7`, the two near-rectangular invariants —
session 43's family finding, which held at `δ = 9` where it was used as a
prediction.

## The exactness conjecture is refuted

**The claim removed.**  Earlier versions of this file read "the bound is exact
whenever it fires", and cited it as the evidence behind the exactness conjecture
(`docs/s43_review.md` §2, session 47's brief).  **That claim is false and is
withdrawn.**

Session 47's counterexample: at `λ = (15,12,6,1,1,1)`, `δ = 9`, `ℓ = 6`,
`a = 21` and `h_pad = 19` — so the bound fires — and `mult_red = 18`.  Not
attained.  It was the first cell that session measured.

| `λ` (all `δ = 9`, `ℓ = 6`) | `a` | `h_pad` | `mult_red` | deficit | units `a − mult_red` | status |
|---|---|---|---|---|---|---|
| `(15,12,6,1,1,1)` | 21 | 19 | **18** | 1 | 3 | proved over `Q`, 3 integer HWVs |
| `(16,10,7,1,1,1)` | 30 | 29 | **26** | 3 | 4 | proved over `Q`, 4 integer HWVs |
| `(15,11,7,1,1,1)` | 30 | 27 | **26** | 1 | 4 | proved over `Q`, 4 integer HWVs |
| `(15,9,9,1,1,1)` | 13 | 9 | **8** | 1 | 5 | proved over `Q`, 5 integer HWVs |
| `(15,10,8,1,1,1)` | 23 | 17 | **16** | 1 | 7 | measured only |

Nineteen firing cells were measured in all: **exact at 14, missed at 5.**
`mult_red ≤ h_pad` holds at every one, so Corollary B2 is not violated.

**Why the old evidence was worthless.**  At `h_pad = 0`, exactness is a theorem
of Corollary B2 — `mult_red ≤ 0` forces equality with no computation — and those
cells were being counted as confirmations.  Of the 411 firing cells at
`δ = 7, 8`, **140 are of that kind**; of the 62 at `δ = 9`, 22; of session 42's
eight banked firing cells, four.  The conjecture's real support was **seven
cells**, with `h_pad = 1, 1, 1, 2, 2, 4, 7`.  Every genuine test sat at
`h_pad ≤ 7`; every refutation is at `h_pad ≥ 9`.  **The conjecture was never
tested where it could fail.**

**What replaces it, as an ordering and not a threshold.**  Exactness is
surjectivity of `μ_λ` onto `C^{h_pad}`, so a small target is a weak demand: all
twelve cells measured with `h_pad ≤ 8` are exact, against five of seven missed at
`h_pad ≥ 9`.  Not a threshold — `h_pad = 10` and `16` are exact, `9` and `17` are
not — and severely confounded, since every cell measured with `a ≥ 9` lies in the
one `(λ_1,λ_2,λ_3,1,1,1)`, `δ = 9` stratum.  The confound is structural rather
than a matter of session time: a large `a` needs a balanced `λ`, a balanced `λ`
has a small stabiliser, and a small stabiliser is what makes the isotypic
reduction unreachable.  Of the 57 unmeasured firing cells with `a ≥ 13` outside
that stratum, **not one is reachable**.

**A regularity proposed and withdrawn in the same session.**  The parity rule on
`e := h_pad − a` held at nine of nine cells with a positive deficit and was
killed two cells later by `(16,10,7,1,1,1)_9` and `(15,11,7,1,1,1)_9`, both
odd — and the first of them also killed "deficit `= 1` always" by failing at 3.
It is recorded because it was proposed on the record and refuted by its own
session's measurements.

**What survives.**  `mult_red ≤ h_pad` is still proved (Corollary B2), so
`units := a − mult_red ≥ a − h_pad` at **every** cell of the region, reachable or
not, in milliseconds.  That free lower bound on the pad-side units — the thing
the programme wants at unreachable cells — is untouched.  Only the claim that it
is an equality is gone.  `results/s47_units.md` tabulates it at all 311 cells
with `0 < h_pad < a`.

## The deepest bites relative to what `h_pad` can see

Two of session 47's cells carry more reducibility equations than the
normalisation bound can account for: `(15,9,9,1,1,1)_9` carries five in degree 9
where the bound proves four, and `(16,10,7,1,1,1)_9` carries four where the
bound proves one.  The latter is the deepest in the record on that measure, and
both are deeper than anything sessions 43 or 45 found.  These are
**reducible-side** measurements; `mult_det` is not measured at either, so they do
not enter the 193-cell count or the `D` column above.

## Outstanding

Nothing on the pad side: all lifts are closed.  On the determinant side,
`(9,8,5,2,2,2)_7` remains unreached — session 46 attempted it twice within its
cost budget and produced no verdict — and the balanced corner at `δ = 8, 9`
above `n_χ ≈ 3·10^5` is untouched.
