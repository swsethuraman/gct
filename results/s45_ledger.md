# Session 45 ledger — the six-row determinant side by sparse certificate

`n = 4`, `ℓ(λ) = 6`, `a ≥ 1`, ascending in `n_χ`, most balanced cell available
at each size — the order published in `results/PREREG_s45.md` §4 before any of
it was measured.  Column `elig` = obstruction-eligible (`λ_1 ≥ δ`, Corollary B
of `docs/reducible_ideal.md`); the one `onset-only` row is the balanced corner
cell `(6,6,6,6,2,2)_7`, which cannot itself carry an obstruction but *can* carry
the determinant ideal, and is the cell the session was built to reach.

**Pipeline.**  The memory-lean build of `analysis/wk9_s45_build.py` (validated
against `wk9_s36_stabred` / `wk9_s42_orbits` at 16 cells, `results/s45_validation.md`
§2): weight-`λ` monomials enumerated as an `int32` array under an exact
feasibility DP, the `χ_λ`-isotypic reduction in two `|Stab|`-passes, the simple
raising operators assembled chunkwise into CSR against a directly enumerated
target basis, the `K = a + 8` evaluation rows contracted to `χ`-coordinates by
numpy.  **Points.**  det: `det_4(Σ s_i A_i)`, random integer `4×4` `A_i`, seed 11,
bound 40 — the house points of `wk8_s30_core`.  **Nullity.**  the session-42
Wiedemann certificates (`analysis/wk9_s42_wied.c` through
`analysis/wk9_s42_sparse.py`, unchanged) with the evaluation rows **pinned**
through every compression level (`analysis/wk9_s45_cell.py`), both house primes
`2147483647`, `2147483629` run concurrently.  `a` is always the plethysm value
(`wk8_s30_pleth`), asserted equal to the full-`E` nullity where marked.

**The certificate.**  `mult_det = a − dim ker[E; ev]` and `rank_p ≤ rank_Q`, so

    a − nullity_p([E; ev])  ≤  mult_det  ≤  a,

and `nullity_p = 0` at a **single** prime *proves* `mult_det = a` over `Q` — no
randomness enters that implication.  Every row below has `nullity_p = 0` at both
primes unless stated otherwise.  `level` is the compression `(sample, group)` that
carried the verdict — `(s, g)` means `s·n_χ` rows of `E` sampled and grouped in
`g`s, with the `K` evaluation rows pinned on afterwards; a nonsingularity
certificate at any level proves the full matrix injective.

`balance := λ_1 − λ_6`.  `HWM` is the cell's own peak resident set, one process
group per cell.

| δ | λ | elig | bal | a | full-`E` | `N_S` | \|Stab\| | `n_χ` | rows | `nnz` | `nnz/n_χ` | nullity | `mult_det` | level | build s | wall s | HWM GB |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8 | `(12, 12, 3, 3, 1, 1)` | yes | 11 | 6 | 6 | 237040 | 8 | 23700 | 171279 | 630087 | 26.6 | 0 | **6** = a | (3,2) | 4.4 | 1605.9 | 0.89 |
| 7 | `(9, 9, 4, 4, 1, 1)` | yes | 8 | 4 | 4 | 314143 | 8 | 32631 | 243459 | 933623 | 28.6 | 0 | **4** = a | (3,2) | 5.4 | 2331.7 | 0.37 |
| 7 | `(9, 9, 6, 2, 1, 1)` | yes | 8 | 4 | 4 | 177331 | 4 | 36090 | 177881 | 693243 | 19.2 | 0 | **4** = a | (3,2) | 2.2 | 1402.5 | 0.34 |
| 7 | `(8, 8, 5, 5, 1, 1)` | yes | 7 | 3 | — | 603787 | 8 | 62613 | 494685 | 1957617 | 31.3 | 0 | **3** = a | (3,2) | 12.6 | 721.9 | 0.4 |
| 7 | `(8, 8, 7, 3, 1, 1)` | yes | 7 | 3 | — | 387460 | 4 | 79865 | 404493 | 1619899 | 20.3 | 0 | **3** = a | (3,2) | 5.8 | 1271.8 | 0.36 |
| 7 | `(7, 7, 6, 6, 1, 1)` | yes | 6 | 1 | — | 832523 | 8 | 87045 | 720637 | 2882165 | 33.1 | 0 | **1** = a | (3,2) | 20.4 | 1554.1 | 0.45 |
| 8 | `(9, 9, 9, 3, 1, 1)` | yes | 8 | 3 | — | 1404263 | 12 | 97399 | 1333285 | 6167051 | 63.3 | 0 | **3** = a | (12,2) | 45.5 | 8527.0 | 1.08 |
| 7 | `(6, 6, 6, 6, 2, 2)` | onset-only | 4 | 1 | — | 4408003 | 48 | 99480 | 3628307 | 14273855 | 143.5 | 0 | **1** = a | (12,2) | 663.4 | 12745.0 | 1.03 |
| 7 | `(8, 8, 6, 2, 2, 2)` | yes | 6 | 3 | — | 1184921 | 12 | 114875 | 1418175 | 4120214 | 35.9 | 0 | **3** = a | (12,2) | 39.7 | 13479.5 | 0.49 |

**9 cells, 9 of them with `mult_det = a` proved by a single-prime
nonsingularity certificate.**  Ambient units (`Σ a`): 28.
Frontier reached: `n_χ = 114875` at
`N_S = 4408003`; best balance measured: 4.

