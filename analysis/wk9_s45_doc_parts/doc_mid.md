
## 2. The build, which is now the binding constraint

For balanced `λ` the stabiliser is trivial or small, so `n_χ ≈ N_S` and the
build is the whole cost.  Session 42's build is vectorised but stores `|Stab|`
index arrays of length `N_S`, the Python `basis` list of `N_S` tuples and
(optionally) the `vecs` list of `N_S` dicts, and recovers the raising
operators' target set by an `np.unique` over an `N_S·δ` concatenation.  At
`N_S ~ 10^6` that is already gigabytes.  `analysis/wk9_s45_build.py` changes
*how*, never *what* — every step is checked against the s36/s42
implementations at 16 cells (`results/s45_validation.md` §2):

**(a) Monomials by an exact feasibility DP.**  The weight-`λ` monomials are
produced as an `(N_S × δ)` `int32` array, level by level, never as a Python
list.  The naive prune (`residual ≥ 0`, `residual ≤ n·(factors left)`) overshoots
badly — at `(7,7,6,6,1,1)_7` it holds 5,537,426 length-6 prefixes for a cell with
`N_S = 832,523`.  Instead a DP over the *small* state space (distinct residual
weight, minimum allowed index) decides feasibility exactly:
`G[k][t][i] = 1` iff `A[i] ≤ REM_k[t]` and `REM_k[t] − A[i]` is a sum of
`δ−k−1` exponent vectors with indices `≥ i`, computed by a backward suffix-OR
over `D_k × L` states with `D_k` in the thousands and `L = |exps(4,r)| = 84` at
`r = 6`.  **No dead prefix is ever stored**, so the live set never exceeds `N_S`
at any level.  Breadth-first expansion in index order reproduces the depth-first
lexicographic order of `wk8_s30_core.monomials` exactly (asserted).  Measured:
`N_S = 10,060,304` in 11.3 s at 1.10 GB, against 2.7 s for `monomials()` at
`N_S = 75,689` — a 25× speed-up at the small end and the difference between
possible and impossible at the large one.

**(b) The isotypic reduction in two group passes.**  `canon[j] = min_g index(g·m_j)`
and `acc[j] = Σ_g χ(g)[g·rep_j = j]` are computed in two passes over
`Stab_W(λ)`, each pass recomputing the image index rather than storing `|Stab|`
arrays of length `N_S` (which at `N_S = 10^7`, `|Stab| = 120` would be 9.6 TB).
The s42 assertions are kept and vectorised: `|acc| = |Stab|/|orbit|` on every
kept orbit, and — a theorem, now checked — the twisted sum vanishes on **every**
member of a dropped orbit, not only on its representative.

**(c) Raising operators against a directly enumerated target basis.**  For each
`E_{i,i+1}` the target set is the weight-`λ + e_i − e_j` monomial basis,
enumerated by (a) and ranked by the same multiset combinadic, so the operator is
assembled by `searchsorted` in chunks with periodic consolidation into CSR — no
`np.unique` over an `N_S·δ` concatenation, no dense object anywhere.  The
`H`-orbit dedup of target rows and the assertion that `χ`-obstructed `H`-fixed
rows cancel exactly are unchanged.

**(d) Evaluation rows by numpy.**  `wk9_s36_stabred.point_rows` is a Python loop
over `N_S × δ`, needing `basis` and `vecs`.  Here the monomial values are a
running modular product over the `δ` columns of `M` and the orbit sums are one
`add.reduceat` over the monomials pre-grouped by `χ`-column.  Identical output,
entrywise, on the same random stream (asserted, det and pad).

## 3. The measured cost curve

Two curves, because the two costs scale with different quantities: the **build**
with `N_S` (and `|Stab|`), the **solve** with `n_χ · nnz`.
