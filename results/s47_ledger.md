# Session 47 ledger — Phase A, the exactness test

Branch `s47-exactness`, clone tip `9aa6a9c`.  Pre-registration
`results/PREREG_s47.md` (commit `3984bbd`, before any measurement).  Work list
`results/s47_todo.md` (commit before the first cell).  Engine
`analysis/wk9_s42_redengine.py` through the sparse route, wrapped by
`analysis/wk9_s47_sweep.py`, which adds the two guards the s42 engine does not
have because it does not know `h_pad`:

- `mult_red > h_pad` ⇒ **BUG** (Corollary B2 forbids it), stop and find it;
- `mult_red < h_pad` at a firing cell ⇒ **REFUTED**, stop the sweep and certify.

`h_pad` is recomputed inside the wrapper from `analysis/wk9_s42_hpad.py` at
every cell, never read from the census, so no verdict rests on a cached number.

## Validation, before the sweep

| `λ` | `δ` | `a` | `h_pad` | `n_χ` | `n_red` | nullity (both primes) | `mult_red` | record | agrees |
|---|---|---|---|---|---|---|---|---|---|
| `(10,8,7,1,1,1)` | 7 | 3 | 2 | 5740 | 5515 | 1 | **2** | 2 | yes |

`results/s47_validation.jsonl`.  The cell is session 36's bite, `h_pad`-exact on
the record; the wrapper reproduces it at both house primes.  Note `n_χ = 5740`
against the census `nchi_lb = 12615`: the census field is `N_S/stab` and
**over**estimates `n_χ`, which is why `results/s47_todo.md` orders by `N_S`.

## Phase A — the pre-registered sweep, and where it stopped

The pre-registered sweep halted at its **first** cell.  `(15,12,6,1,1,1)_9`:
`a = 21`, `h_pad = 19`, `nullity_p(E_red) = 3` at both house primes, so
`mult_red = 18 < 19 = h_pad`.  That is stopping rule 2 of
`results/PREREG_s47.md`, and the remaining 15 cells of wave 1
(`results/logs/wave1.cells`) were not measured under it.  Log
`results/logs/s47_refutation_cell.log`.

## The certificate

`a` and `h_pad` are the whole content of the verdict besides the nullity, so
both were recomputed by routes that share no code
(`analysis/wk9_s47_hpadcheck.py`, log `results/logs/s47_hpadcheck.log`):

| quantity | route 1 (symmetric-function plethysm) | route 2 (Weyl alternation) | route 3 (fresh multiset DP) |
|---|---|---|---|
| `a(λ, 9)` | 21 | 21 | — |
| `h_pad(λ, 9)` | 19 | 19 | 19 (39 Pieri strips) |

Route 3 is written for this session: it counts multisets of `δ` degree-3
monomials in 6 variables by a DP, alternates over the Weyl group to get the
cubic plethysm coefficients, and sums over the Pieri strips — it reuses neither
`wk8_s30_pleth.amb` nor the s42 tail DP.

The nullity direction needs more than mod-`p`: `nullity_p ≥ nullity_Q`, so
`mult_red ≥ a − nullity_p = 18` is what a mod-`p` run proves, and the refutation
needs `mult_red ≤ 18`, i.e. `nullity_Q ≥ 3` — three independent **rational**
kernel vectors.  `analysis/wk9_s42_lift.py` supplies them; see the row below.



## Phase A' — the post-refutation sweep (a different question)

Once the conjecture is known false the binary test is spent, and the measurement
worth making is the **failure rate**, so the sweep was restarted under
`--continue` (refuted cells banked, sweep carries on; a `BUG` verdict still
halts) over cells stratified by the parity of the gap `a − h_pad`, which was the
discriminant this session's rank-deficit reading proposed.  That reading is now
also refuted — see `docs/exactness.md` §0.  This table is the whole of the
session's firing-cell measurement, the pre-registered first cell included.

<!-- PHASE A TABLE -->

| # | `λ` | `δ` | `ℓ` | `a` | `h_pad` | gap `a−h_pad` | `n_red` | `nnz_red` | nullity | `mult_red` | `d` | units | verdict | secs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `(15,12,6,1,1,1)` | 9 | 6 | 21 | 19 | 2 | 20323 | 222487 | 3 | **18** | 1 | 3 | **REFUTED** | 686 |
| 2 | `(14,13,6,1,1,1)` | 9 | 6 | 12 | 10 | 2 | 21742 | 241739 | 2 | **10** | 0 | 2 | exact | 557 |
| 3 | `(16,10,7,1,1,1)` | 9 | 6 | 30 | 29 | 1 | 22720 | 248152 | 4 | **26** | 3 | 4 | **REFUTED** | 810 |
| 4 | `(15,11,7,1,1,1)` | 9 | 6 | 30 | 27 | 3 | 27226 | 304026 | 4 | **26** | 1 | 4 | **REFUTED** | 1156 |
| 5 | `(13,13,7,1,1,1)` | 9 | 6 | 9 | 6 | 3 | 15809 | 315180 | 3 | **6** | 0 | 3 | exact | 436 |
| 6 | `(15,9,9,1,1,1)` | 9 | 6 | 13 | 9 | 4 | 17211 | 387878 | 5 | **8** | 1 | 5 | **REFUTED** | 915 |
| 7 | `(13,12,8,1,1,1)` | 9 | 6 | 14 | 7 | 7 | 40421 | 475888 | 7 | **7** | 0 | 7 | exact | 5054 |
| 8 | `(13,9,6,1,1,1,1)` | 8 | 7 | 2 | 1 | 1 | 5159 | 56035 | 1 | **1** | 0 | 1 | exact | 126 |
| 9 | `(13,8,7,1,1,1,1)` | 8 | 7 | 2 | 1 | 1 | 6054 | 66615 | 1 | **1** | 0 | 1 | exact | 52 |
| 10 | `(8,8,5,5,1,1)` | 7 | 6 | 3 | 2 | 1 | 61622 | 1926397 | 1 | **2** | 0 | 1 | exact | 6675 |
| 11 | `(12,9,7,1,1,1,1)` | 8 | 7 | 2 | 1 | 1 | 7558 | 85403 | 1 | **1** | 0 | 1 | exact | 77 |
| 12 | `(11,11,11,1,1,1)` | 9 | 6 | 2 | 1 | 1 | 9538 | 612204 | 1 | **1** | 0 | 1 | exact | 356 |
| 13 | `(16,8,8,1,1,1,1)` | 9 | 7 | 4 | 1 | 3 | 6427 | 145556 | 3 | **1** | 0 | 3 | exact | 483 |
| 14 | `(15,12,5,1,1,1,1)` | 9 | 7 | 3 | 2 | 1 | 7624 | 84396 | 1 | **2** | 0 | 1 | exact | 89 |
| 15 | `(14,13,5,1,1,1,1)` | 9 | 7 | 2 | 1 | 1 | 8208 | 92343 | 1 | **1** | 0 | 1 | exact | 99 |
| 16 | `(16,10,6,1,1,1,1)` | 9 | 7 | 6 | 2 | 4 | 9598 | 106881 | 4 | **2** | 0 | 4 | exact | 221 |
| 17 | `(14,10,9,1,1,1)` | 9 | 6 | 15 | 8 | 7 | 41699 | 486358 | 7 | **8** | 0 | 7 | exact | 5840 |

**17 firing cells measured this session: the bound is exact at 13 and missed at 4.**

| gap `a − h_pad` | parity | cells | missed |
|---|---|---|---|
| 1 | odd | 8 | 1 |
| 2 | even | 2 | 1 |
| 3 | odd | 3 | 1 |
| 4 | even | 2 | 1 |
| 7 | odd | 2 | 0 |


Stratified by where the cell sits:

| stratum | cells | exact | missed |
|---|---|---|---|
| `ell = 6`, `delta = 7`, outside the family | 1 | 1 | 0 |
| `ell = 6`, `delta = 9`, in family | 9 | 5 | 4 |
| `ell = 7`, `delta = 8` | 3 | 3 | 0 |
| `ell = 7`, `delta = 9` | 4 | 4 | 0 |

Rank deficits `d = min(a, h_pad) − mult_red` seen: {0: 13, 1: 3, 3: 1}.
