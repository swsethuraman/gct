# Session 41 ledger — the six-row frontier (`n = 4`, `ℓ(λ) = 6`, `a ≥ 1`, `δ = 7, 8`)

Pipeline: the stabiliser reduction `analysis/wk9_s36_stabred.py` unchanged up to the kernel; kernel by the
in-place rref route of `analysis/wk9_s41_kernel.py` (validated in `results/s41_validation.md`: identical
kernel span to s36's exact and compressed routes on nine cells, both primes), every kernel vector verified
against the uncompressed raising-operator rows; `a` by kernel dimension AND by plethysm (asserted equal);
`rank(R) = n_χ − a` asserted; ranks by python-flint `nmod_mat` over `2147483647` and `2147483629`;
`a + 8` evaluation points per side; sceptical branch (`3a + 24` fresh points, seed 907, both primes) on any
`mult < a`.  **Points.**  det: `det_4(Σ s_i A_i)`, random integer `4×4` `A_i`.  pad: the **true
padded-permanent restriction** `x_0 · per_3(x_1..x_9)` with each `x_t` a random linear form in `s_1..s_6`
(`per_padded(3,4)` through `restrict()`) — never `l · (random cubic)`.  `mult_red` is the point-free
reducibility multiplicity by (★) (`docs/reducible_ideal.md`, Corollary A); at `r = 6`, `mult_pad ≤ mult_red`
with a strict gap iff a permanent-specific equation exists.  `m_det` is the symmetric rectangular Kronecker
bound (`mult_det ≤ m_det`).  Convention `D = mult_pad − mult_det`; only `D > 0` is an obstruction.
`HWM` is the cell's own peak resident set (GB), one process per cell.

| delta | lam | a | m_det | N_S | Stab | n_chi | rows | route | mult_det | mult_pad | mult_red | D | secs | HWM |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7 | `(12, 10, 3, 1, 1, 1)` | 1 | 227 | 19488 | 6 | 1282 | 4357 | inplace | 1 | 1 | 1 | +0 | 3 | 0.09 |
| 7 | `(14, 7, 4, 1, 1, 1)` | 1 | 501 | 21445 | 6 | 1414 | 4513 | inplace | 1 | 1 | 1 | +0 | 3 | 0.10 |
| 7 | `(14, 6, 5, 1, 1, 1)` | 1 | 433 | 25741 | 6 | 1735 | 5391 | inplace | 1 | 1 | 1 | +0 | 4 | 0.11 |
| 7 | `(10, 10, 5, 1, 1, 1)` | 1 | 259 | 51383 | 12 | 1841 | 8795 | inplace | 1 | 1 | 1 | +0 | 8 | 0.13 |
| 7 | `(11, 10, 4, 1, 1, 1)` | 1 | 326 | 34377 | 6 | 2396 | 7737 | inplace | 1 | 1 | 1 | +0 | 10 | 0.17 |
| 7 | `(11, 11, 2, 2, 1, 1)` | 1 | 81 | 26710 | 8 | 2806 | 18757 | inplace | 1 | 1 | 1 | +0 | 14 | 0.18 |
| 7 | `(9, 9, 7, 1, 1, 1)` | 1 | 223 | 79501 | 12 | 3086 | 14631 | inplace | 1 | 1 | 1 | +0 | 21 | 0.24 |
| 7 | `(15, 7, 2, 2, 1, 1)` | 1 | 222 | 14910 | 4 | 3027 | 15549 | inplace | 1 | 1 | 1 | +0 | 15 | 0.22 |
| 7 | `(14, 8, 2, 2, 1, 1)` | 1 | 248 | 19318 | 4 | 3927 | 20218 | inplace | 1 | 1 | 1 | +0 | 30 | 0.31 |
| 8 | `(22, 2, 2, 2, 2, 2)` | 1 | 13 | 8253 | 120 | 197 | 5797 | exact | 1 | 1 | 1 | +0 | 2 | 0.09 |
| 8 | `(19, 5, 5, 1, 1, 1)` | 1 | 198 | 19664 | 12 | 645 | 3957 | exact | 1 | 1 | 1 | +0 | 4 | 0.12 |
| 8 | `(18, 8, 3, 1, 1, 1)` | 1 | 430 | 18091 | 6 | 1123 | 3768 | inplace | 1 | 1 | 1 | +0 | 3 | 0.09 |
| 8 | `(21, 3, 2, 2, 2, 2)` | 1 | 30 | 19634 | 24 | 1366 | 27850 | inplace | 1 | 1 | 1 | +0 | 5 | 0.11 |
| 8 | `(17, 9, 3, 1, 1, 1)` | 1 | 516 | 23354 | 6 | 1495 | 4996 | inplace | 1 | 1 | 1 | +0 | 4 | 0.10 |
| 8 | `(18, 7, 4, 1, 1, 1)` | 1 | 632 | 26390 | 6 | 1700 | 5420 | inplace | 1 | 1 | 1 | +0 | 5 | 0.11 |
| 8 | `(16, 10, 3, 1, 1, 1)` | 2 | 536 | 28410 | 6 | 1850 | 6173 | inplace | 2 | 2 | 2 | +0 | 5 | 0.12 |
| 8 | `(18, 6, 5, 1, 1, 1)` | 1 | 531 | 31621 | 6 | 2081 | 6472 | inplace | 1 | 1 | 1 | +0 | 8 | 0.14 |
| 8 | `(15, 11, 3, 1, 1, 1)` | 1 | 476 | 32593 | 6 | 2158 | 7240 | inplace | 1 | 1 | 1 | +0 | 8 | 0.15 |
