# Session 46 ledger — the balanced corner of the six-row determinant side

`n = 4`, `ℓ(λ) = 6`, `a ≥ 1`, `δ = 7`.  The order is the pre-registered one
(`results/PREREG_s46.md` §4 and §6, published before any measurement): the named
target `(8,4,4,4,4,4)_7` first, then the rest of the balanced band **ascending in
predicted cost, most balanced first at each size**, from
`results/s46_reach.md` / `results/s46_order.json`.  Column `elig` =
obstruction-eligible (`λ_1 ≥ δ`, Corollary B of `docs/reducible_ideal.md`);
`bal := λ_1 − λ_6`.

**Pipeline.**  Session 45's route with one change, validated entrywise before
use (`results/s46_buildvalidation.md`): the `χ_λ`-isotypic reduction is built
from the **generators** of `Stab_W(λ)` — the adjacent transpositions inside its
blocks — by min-label propagation and a character walk, instead of `2|Stab|`
passes over the `(N_S × δ)` monomial array.  Everything else is imported
unchanged: the monomial enumeration, the raising rule, the `H`-orbit row dedup,
the evaluation rows, and the whole solve path
(`wk9_s45_cell.measure_cell`; `analysis/wk9_s46_cell.py` substitutes the build
function and nothing else).

**Points.**  det: `det_4(Σ s_i A_i)`, random integer `4×4` `A_i`, seed 11,
bound 40, `K = a + 8` points — the house choice of `wk8_s30_core.measure`.
**Nullity.**  The session-42 Wiedemann certificates
(`analysis/wk9_s42_wied.c`) with the evaluation rows pinned through every
compression level, both house primes `2147483647` and `2147483629` run
concurrently on the two cores.  `a` is the plethysm value (`wk8_s30_pleth`).
`h_pad` is session 42's normalisation bound (`docs/reducible_engine.md` §B),
free.

**The certificate.**  `mult_det = a − dim ker[E; ev]` and `rank_p ≤ rank_Q`, so

    a − nullity_p([E; ev])  ≤  mult_det  ≤  a,

and `nullity_p = 0` at a **single** prime *proves* `mult_det = a` over `Q` — no
randomness enters that implication.  Every row below has `nullity_p = 0` at
**both** primes.  `level` is the compression that carried the verdict.
`D = mult_pad − mult_det`, bounded using `mult_pad ≤ mult_red ≤ min(a, h_pad)`.

| δ | λ | elig | bal | `a` | `h_pad` | `N_S` | \|Stab\| | `n_χ` | rows | `nnz` | `nnz_c` | level | nullity | `mult_det` | `D` | build s | seq s | wall s | HWM GB |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7 | `(8, 4, 4, 4, 4, 4)` | yes | 4 | 2 | 0 | 10060304 | 120 | 92031 | 6212840 | 20680806 | 4596782 | `(12,2)` | 0 | **2** = a | **−2** (exact, `h_pad = 0`) | 331.0 | 5023.2 | 5585.5 | 1.69 |
| 7 | `(9, 9, 3, 3, 2, 2)` | yes | 7 | 1 | 2 | 823745 | 8 | 105536 | 993656 | 3345005 | 4294688 | `(12,2)` | 0 | **1** = a | ≤ 0 | 11.2 | 5195.9 | 9026.9 | 0.26 |
| 7 | `(8, 8, 6, 4, 1, 1)` | yes | 7 | 1 | 4 | 542288 | 4 | 112088 | 555718 | 2268981 | 2382523 | `(3,2)` | 0 | **1** = a | ≤ 0 | 6.0 | 2505.0 | 2772.2 | 0.22 |
| 7 | `(8, 7, 7, 4, 1, 1)` | yes | 7 | 3 | 3 | 582738 | 4 | 120653 | 685541 | 2783437 | 2796623 | `(3,2)` | 0 | **3** = a | ≤ 0 | 6.1 | 3124.2 | 3410.6 | 0.23 |
| 7 | `(8, 8, 7, 2, 2, 1)` | yes | 7 | 1 | 4 | 520021 | 4 | 137693 | 914710 | 3317491 | 2737093 | `(3,2)` | 0 | **1** = a | ≤ 0 | 6.0 | 3768.5 | 4225.3 | 0.23 |

**5 cells, ambient units Σa = 8, `mult_det = a` proved at 5 of them.**

## Notes on individual rows

- **`(8,4,4,4,4,4)_7` is the cell session 45 named and could not build.**
  `N_S = 10,060,304`, `|Stab| = 120`, balance 4, `λ_1 = 8 ≥ δ` — the most
  balanced *obstruction-eligible* `δ = 7` cell there is.  Its isotypic reduction
  took **45 s** (4 generator passes and a 5-round label propagation, against
  240 group passes), the whole build 331 s at 1.69 GB, and the solve one
  sequence of 5,023 s at level `(12,2)` with `n_rows/n_χ = 67.5`.
  `n_χ = 92,031` exactly — the census's tabulated `~83,836` is the bound
  `N_S/|Stab|`, and it is not a bound (§ `results/s46_reach.md` §1).
  `h_pad = 0` here, so `mult_red = 0`, `mult_pad = 0` and **`D = −2` exactly,
  proved** — the largest-magnitude exact `D` at balance 4 anywhere in the record.
- **`(9,9,3,3,2,2)_7` escalated, and that is the second live demonstration of
  the safety property.**  At `n_rows/n_χ = 9.4` the driver started at the cheap
  `(3,2)` level, which came out rank-deficient; the kernel candidate was checked
  against the **full** `[E; ev]`, failed, and the run escalated to `(12,2)`,
  which certified nonsingularity.  No wrong verdict was emitted; the cell cost
  2.5 h instead of the predicted 0.9 h.  The rule session 45 left behind was
  "start at `(12,2)` when `n_rows/n_χ ≳ 10`"; this cell failed at **9.4**, so the
  rule this session leaves behind is **`≳ 9`** — equivalently, escalate before
  the `(3,2)` level would sample under about a third of the rows (it worked at
  38 %, 36 % and 32 % is where it broke).
- The four Phase-3 cells are all **balance 7**.  That is what the cost order
  gives: the cheapest unmeasured cells in the band are balance-7 cells, and the
  next balance-6 cell (`(7,7,7,4,2,1)_7`, `n_χ = 236,122`) is predicted at 9.2 h,
  behind two more balance-7 cells in cost order.

## What was reproduced, not newly measured

Phase 1 (`results/s46_validation.md`) also ran five banked rows end to end
through this build — `(8,8,5,5,1,1)_7`, `(9,9,6,2,1,1)_7`, `(12,12,3,3,1,1)_8`,
`(12,9,3,2,1,1)_7` (at all three compression levels) and the pad-side drop
`(13,10,6,1,1,1)_8` (at the cheap level and uncompressed).  Those are *not*
counted as new cells anywhere in this session's totals.

## Not reached

`results/s46_notreached.jsonl` (empty: no cell was attempted and failed).  The
sweep stopped where the pre-registered cost budget ran out, at
`(9,8,5,2,2,2)_7` (balance 7, `n_χ = 182,806`, predicted 4.8 h) — recorded in
`results/logs/s46_sweep.log` as a budget stop, not a failure.
