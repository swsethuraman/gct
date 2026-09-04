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

## Phase A — the sweep, and where it stopped

| # | `λ` | `δ` | `ℓ` | `a` | `h_pad` | `n_χ` | `n_red` | `nnz_red` | nullity | `mult_red` | verdict | secs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `(15,12,6,1,1,1)` | 9 | 6 | 21 | 19 | 21451 | 20323 | 222487 | 3 | **18** | **REFUTED** | 686 |

**The first cell measured refutes the conjecture.**  `mult_red = 18 < 19 =
h_pad`, at both house primes (`nullity_p(E_red) = 3` at `p = 2147483647` and
`p = 2147483629`).  `mult_red ≤ h_pad` holds, so Corollary B2 is not violated
and this is not stopping rule 1.  It is stopping rule 2, and the sweep halted
at once, as pre-registered.  Log `results/logs/s47_refutation_cell.log`.

The remaining 15 cells of wave 1 (`results/logs/wave1.cells`) were not measured.

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

