# Session 43 ledger — closing the six-row region already in reach (`n = 4`, `ℓ(λ) = 6`, `a ≥ 1`, `δ = 7, 8, 9`)

Pipeline exactly as `results/s41_ledger.md`: the stabiliser reduction `analysis/wk9_s36_stabred.py` unchanged up
to the kernel; kernel by the in-place rref route of `analysis/wk9_s41_kernel.py`, every kernel vector verified
against the uncompressed raising-operator rows; `a` by kernel dimension AND by plethysm (asserted equal);
`rank(R) = n_χ − a` asserted; ranks by python-flint `nmod_mat` over `2147483647` and `2147483629`; `a + 8`
evaluation points per side; independent re-check (`3a + 24` fresh points, seed 907, both primes) on any
`mult < a`.  **Points.**  det: `det_4(Σ s_i A_i)`, random integer `4×4` `A_i`.  pad: the **true padded-permanent
restriction** `x_0 · per_3(x_1..x_9)` with each `x_t` a random linear form in `s_1..s_6` (`per_padded(3,4)`
through `restrict()`) — never `l · (random cubic)`.  `mult_red` is the point-free reducibility multiplicity by
(★) (`docs/reducible_ideal.md`, Corollary A).  `m_det` is the symmetric rectangular Kronecker bound.  Convention
`D = mult_pad − mult_det`; only `D > 0` is an obstruction.  `HWM` is the cell's own peak resident set (GB), one
process per cell.  Cells are taken in ascending `n_χ` from `results/s43_todo.md`.

| delta | lam | a | m_det | N_S | Stab | n_chi | rows | route | mult_det | mult_pad | mult_red | D | secs | HWM |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8 | `(14, 11, 4, 1, 1, 1)` | 4 | 953 | 62680 | 6 | 4403 | 13895 | inplace | 4 | 4 | 4 | +0 | 51 | 0.35 |
| 8 | `(16, 8, 5, 1, 1, 1)` | 7 | 1564 | 63163 | 6 | 4457 | 13442 | inplace | 7 | 7 | 7 | +0 | 51 | 0.36 |
| 8 | `(13, 12, 4, 1, 1, 1)` | 3 | 543 | 66550 | 6 | 4701 | 14986 | inplace | 3 | 2 | 2 | -1 | 59 | 0.39 |
