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
| 8 | `(19, 5, 2, 2, 2, 2)` | 3 | 195 | 72959 | 24 | 4706 | 99547 | inplace | 3 | 3 | 3 | +0 | 75 | 0.43 |
| 8 | `(20, 5, 2, 2, 2, 1)` | 2 | 169 | 22622 | 6 | 4804 | 49394 | inplace | 2 | 2 | 2 | +0 | 63 | 0.40 |
| 8 | `(18, 8, 2, 2, 1, 1)` | 1 | 326 | 23830 | 4 | 4829 | 24733 | inplace | 1 | 1 | 1 | +0 | 62 | 0.40 |
| 8 | `(13, 13, 2, 2, 1, 1)` | 2 | 113 | 48210 | 8 | 5072 | 33595 | inplace | 2 | 2 | 2 | +0 | 71 | 0.44 |
| 8 | `(16, 7, 6, 1, 1, 1)` | 4 | 1173 | 73559 | 6 | 5263 | 15640 | inplace | 4 | 4 | 4 | +0 | 78 | 0.46 |
| 8 | `(15, 9, 5, 1, 1, 1)` | 9 | 1941 | 79731 | 6 | 5766 | 17300 | inplace | 9 | 9 | 9 | +0 | 100 | 0.54 |
| 8 | `(17, 9, 2, 2, 1, 1)` | 3 | 419 | 30829 | 4 | 6308 | 32109 | inplace | 3 | 3 | 3 | +0 | 118 | 0.59 |
| 8 | `(20, 5, 3, 2, 1, 1)` | 1 | 375 | 17213 | 2 | 6575 | 20081 | inplace | 1 | 1 | 1 | +0 | 135 | 0.62 |
| 8 | `(13, 8, 8, 1, 1, 1)` | 3 | 918 | 178586 | 12 | 6838 | 39973 | inplace | 3 | 2 | 2 | -1 | 173 | 0.72 |
| 8 | `(14, 10, 5, 1, 1, 1)` | 9 | 1900 | 93987 | 6 | 6886 | 20718 | inplace | 9 | 9 | 9 | +0 | 161 | 0.69 |
| 8 | `(15, 8, 6, 1, 1, 1)` | 6 | 1908 | 98550 | 6 | 7239 | 21333 | inplace | 6 | 6 | 6 | +0 | 171 | 0.76 |
| 8 | `(18, 6, 2, 2, 2, 2)` | 7 | 397 | 119467 | 24 | 7562 | 160897 | inplace | 7 | 7 | 7 | +0 | 221 | 0.88 |
| 8 | `(13, 11, 5, 1, 1, 1)` | 7 | 1427 | 103583 | 6 | 7671 | 23253 | inplace | 7 | 7 | 7 | +0 | 210 | 0.84 |
| 8 | `(16, 10, 2, 2, 1, 1)` | 2 | 413 | 37571 | 4 | 7689 | 39274 | inplace | 2 | 2 | 2 | +0 | 197 | 0.83 |
| 8 | `(19, 6, 2, 2, 2, 1)` | 4 | 319 | 36762 | 6 | 7707 | 79316 | inplace | 4 | 4 | 4 | +0 | 215 | 0.85 |
| 8 | `(11, 11, 7, 1, 1, 1)` | 3 | 787 | 195853 | 12 | 7745 | 35808 | inplace | 3 | 3 | 3 | +0 | 208 | 0.89 |
| 8 | `(19, 5, 3, 3, 1, 1)` | 1 | 575 | 41763 | 4 | 7963 | 44894 | inplace | 1 | 1 | 1 | +0 | 214 | 0.88 |
| 8 | `(15, 11, 2, 2, 1, 1)` | 4 | 397 | 43155 | 4 | 8887 | 45358 | inplace | 4 | 4 | 4 | +0 | 299 | 1.03 |
| 8 | `(14, 12, 2, 2, 1, 1)` | 1 | 248 | 46912 | 4 | 9644 | 49589 | inplace | 1 | 1 | 1 | +0 | 356 | 1.19 |
| 8 | `(11, 9, 9, 1, 1, 1)` | 3 | 548 | 240291 | 12 | 9675 | 55677 | inplace | 3 | 1 | 1 | -2 | 378 | 1.29 |
| 8 | `(14, 8, 7, 1, 1, 1)` | 9 | 1778 | 138895 | 6 | 10542 | 30446 | inplace | 9 | 8 | 8 | -1 | 462 | 1.43 |
| 8 | `(19, 6, 3, 2, 1, 1)` | 2 | 718 | 27876 | 2 | 10762 | 32624 | inplace | 2 | 2 | 2 | +0 | 462 | 1.45 |
