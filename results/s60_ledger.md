# Session 60 — ledger: the balanced length-5 complement, both sides

One row per measured cell (`n = 4`, `r = 5`).  `a` = ambient multiplicity (Weyl alternation = s54 plethysm);
`h_pad` = normalisation bound (`mult_red <= h_pad`, proved).  `mult_det` at `a+8` det_4 pencils; `mult_red(★)`
point-free by Theorem (★) on the red columns of `E`; `mult_red(pts)` at `a+8` reducible `ℓ·c` points (—: not run,
(★) alone above `n_chi = 20000` on the sparse route).  Tags: *proved* = nullity 0 at both primes (or, on the
reducible side, nullity certified `<= a − h_pad` at both primes, meeting the theorem's `>=`); *exact* = explicit
kernel at both primes (dense route); *measured* = nullity exhibited at both primes; *bounded* = extraction budget
reached, the value is an upper bound on `mult`.  `D = mult_red − mult_det`; a refutation of `R_5 ⊆ D_5` is `D > 0`.
Route: dense = exact flint kernel (`n_chi <= 4000`), sparse = session-45 Wiedemann certificates.
`N_S` is the full weight-space dimension; `n_chi = dim V_chi` is the chi_lambda-isotypic reduction of
`docs/stabiliser_reduction.md` (the column count of the matrix every certificate runs on), `n_chi ~ N_S/|Stab|`;
the two are never the same quantity unless `Stab` is trivial.  Every `n_chi` on a measured row is exact.

Ladder columns (integrator note, s60): `ρ = (λ_2..λ_5)`, `t = |ρ| = 4δ − λ_1`; along the ladder `λ_δ = (4δ−t, ρ)`
the quantities `a, mult_det, mult_red, i_det, i_red` are non-decreasing in δ, constant from the first δ with `a_δ = a_∞ = a_t`
(`δ_close`, from `results/s60_tail_census.md`) and in particular for `δ ≥ t` (multiplication by `u = c_(4,0,0,0,0)`).
`reach` says what the row closes: below `δ_close`, this δ and every lower δ of the ladder; at or above it, the whole ladder in
every degree (with `mult_det = a` the tail is dead for `D > 0` permanently).  Rows with route `ladder` are implied by the
named source cell (no computation).

| δ | λ | ρ | t | reach | a | h_pad | N_S | Stab | n_chi | route | mult_det | mult_red(★) | mult_red(pts) | D | primes | s | certs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | `(12, 5, 5, 1, 1)` | `(5, 5, 1, 1)` | 12 | δ<δ_close=7: δ<= 6 of ladder | 2 | 5 | 2795 | 4 | 524 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 0.6 | 4 |
| 6 | `(9, 9, 4, 1, 1)` | `(9, 4, 1, 1)` | 15 | δ<δ_close=10: δ<= 6 of ladder | 2 | 4 | 3852 | 4 | 736 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 1.4 | 2 |
| 6 | `(13, 5, 2, 2, 2)` | `(5, 2, 2, 2)` | 11 | δ<δ_close=8: δ<= 6 of ladder | 2 | 12 | 3672 | 6 | 825 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 3.3 | 2 |
| 6 | `(12, 6, 4, 1, 1)` | `(6, 4, 1, 1)` | 12 | δ<δ_close=7: δ<= 6 of ladder | 2 | 12 | 2553 | 2 | 927 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 1.1 | 4 |
| 6 | `(12, 6, 2, 2, 2)` | `(6, 2, 2, 2)` | 12 | δ<δ_close=9: δ<= 6 of ladder | 4 | 16 | 5194 | 6 | 1162 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 7.6 | 2 |
| 6 | `(11, 7, 4, 1, 1)` | `(7, 4, 1, 1)` | 13 | δ<δ_close=8: δ<= 6 of ladder | 4 | 14 | 3209 | 2 | 1187 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 2.3 | 2 |
| 6 | `(8, 7, 7, 1, 1)` | `(7, 7, 1, 1)` | 16 | δ<δ_close=10: δ<= 6 of ladder | 2 | 2 | 6718 | 4 | 1300 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 5.7 | 2 |
| 6 | `(10, 8, 4, 1, 1)` | `(8, 4, 1, 1)` | 14 | δ<δ_close=9: δ<= 6 of ladder | 2 | 10 | 3686 | 2 | 1362 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 3.0 | 2 |
| 6 | `(11, 6, 5, 1, 1)` | `(6, 5, 1, 1)` | 13 | δ<δ_close=8: δ<= 6 of ladder | 2 | 8 | 3818 | 2 | 1423 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 3.3 | 2 |
| 6 | `(11, 7, 2, 2, 2)` | `(7, 2, 2, 2)` | 13 | δ<δ_close=10: δ<= 6 of ladder | 2 | 14 | 6563 | 6 | 1435 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 13.1 | 2 |
| 6 | `(11, 8, 2, 2, 1)` | `(8, 2, 2, 1)` | 13 | δ<δ_close=9: δ<= 6 of ladder | 3 | 13 | 2919 | 2 | 1619 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 7.1 | 4 |
| 6 | `(10, 8, 2, 2, 2)` | `(8, 2, 2, 2)` | 14 | δ<δ_close=11: δ<= 6 of ladder | 3 | 11 | 7576 | 6 | 1661 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 20.5 | 2 |
| 6 | `(13, 4, 4, 2, 1)` | `(4, 4, 2, 1)` | 11 | δ<δ_close=7: δ<= 6 of ladder | 2 | 12 | 3199 | 2 | 1667 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 8.6 | 2 |
| 6 | `(10, 7, 5, 1, 1)` | `(7, 5, 1, 1)` | 14 | δ<δ_close=9: δ<= 6 of ladder | 4 | 10 | 4672 | 2 | 1757 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 6.0 | 2 |
| 6 | `(10, 9, 2, 2, 1)` | `(9, 2, 2, 1)` | 14 | δ<δ_close=10: δ<= 6 of ladder | 2 | 7 | 3176 | 2 | 1759 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 9.1 | 2 |
| 6 | `(9, 8, 5, 1, 1)` | `(8, 5, 1, 1)` | 15 | δ<δ_close=10: δ<= 6 of ladder | 2 | 6 | 5159 | 2 | 1947 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 7.1 | 2 |
| 6 | `(11, 4, 4, 4, 1)` | `(4, 4, 4, 1)` | 13 | δ<δ_close=8: δ<= 6 of ladder | 2 | 7 | 11574 | 6 | 2113 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 4.7 | 2 |
| 6 | `(9, 7, 6, 1, 1)` | `(7, 6, 1, 1)` | 15 | δ<δ_close=9: δ<= 6 of ladder | 2 | 5 | 5967 | 2 | 2262 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 10.3 | 2 |
| 6 | `(12, 4, 4, 2, 2)` | `(4, 4, 2, 2)` | 12 | δ<δ_close=8: δ<= 6 of ladder | 3 | 10 | 8803 | 4 | 2561 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 6.1 | 2 |
| 6 | `(13, 4, 3, 2, 2)` | `(4, 3, 2, 2)` | 11 | δ<δ_close=7: δ<= 6 of ladder | 1 | 8 | 4940 | 2 | 2727 | dense | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 5.9 | 2 |
| 6 | `(12, 5, 3, 3, 1)` | `(5, 3, 3, 1)` | 12 | δ<δ_close=7: δ<= 6 of ladder | 1 | 7 | 5837 | 2 | 2761 | dense | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 6.2 | 2 |
| 6 | `(13, 5, 3, 2, 1)` | `(5, 3, 2, 1)` | 11 | δ<δ_close=7: δ<= 6 of ladder | 3 | 16 | 2800 | 1 | 2800 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 5.8 | 4 |
| 6 | `(9, 9, 3, 2, 1)` | `(9, 3, 2, 1)` | 15 | δ<δ_close=11: δ<= 6 of ladder | 1 | 6 | 5994 | 2 | 2959 | dense | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 7.4 | 2 |
| 6 | `(12, 4, 4, 3, 1)` | `(4, 4, 3, 1)` | 12 | δ<δ_close=7: δ<= 6 of ladder | 1 | 9 | 6675 | 2 | 3452 | dense | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 10.7 | 2 |
| 6 | `(11, 5, 5, 2, 1)` | `(5, 5, 2, 1)` | 13 | δ<δ_close=8: δ<= 6 of ladder | 2 | 12 | 7461 | 2 | 3637 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 12.6 | 2 |
| 6 | `(11, 6, 3, 3, 1)` | `(6, 3, 3, 1)` | 13 | δ<δ_close=8: δ<= 6 of ladder | 1 | 9 | 8035 | 2 | 3813 | dense | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 13.4 | 2 |
| 6 | `(12, 6, 3, 2, 1)` | `(6, 3, 2, 1)` | 12 | δ<δ_close=8: δ<= 6 of ladder | 4 | 22 | 3942 | 1 | 3942 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 14.4 | 2 |
| 6 | `(12, 5, 3, 2, 2)` | `(5, 3, 2, 2)` | 12 | δ<δ_close=8: δ<= 6 of ladder | 1 | 14 | 7685 | 2 | 4209 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 5.3 | 0 |
| 6 | `(8, 4, 4, 4, 4)` | `(4, 4, 4, 4)` | 16 | δ<δ_close=10: δ<= 6 of ladder | 2 | 1 | 94675 | 24 | 4562 | sparse | 2 (proved) | 1 (proved) | 1 (proved) | -1 | agree | 21.2 | 0 |
| 6 | `(10, 7, 3, 3, 1)` | `(7, 3, 3, 1)` | 14 | δ<δ_close=9: δ<= 6 of ladder | 2 | 10 | 9882 | 2 | 4702 | sparse | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 7.4 | 0 |
| 6 | `(12, 5, 4, 2, 1)` | `(5, 4, 2, 1)` | 12 | δ<δ_close=8: δ<= 6 of ladder | 5 | 24 | 4942 | 1 | 4942 | sparse | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 8.0 | 0 |
| 6 | `(11, 7, 3, 2, 1)` | `(7, 3, 2, 1)` | 13 | δ<δ_close=9: δ<= 6 of ladder | 5 | 24 | 4978 | 1 | 4978 | sparse | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 8.2 | 0 |
| 6 | `(9, 8, 3, 3, 1)` | `(8, 3, 3, 1)` | 15 | δ<δ_close=10: δ<= 6 of ladder | 1 | 6 | 10939 | 2 | 5209 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 9.1 | 0 |
| 6 | `(10, 4, 4, 4, 2)` | `(4, 4, 4, 2)` | 14 | δ<δ_close=9: δ<= 6 of ladder | 3 | 6 | 30870 | 6 | 5588 | sparse | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 27.3 | 0 |
| 6 | `(10, 8, 3, 2, 1)` | `(8, 3, 2, 1)` | 14 | δ<δ_close=10: δ<= 6 of ladder | 4 | 18 | 5731 | 1 | 5731 | sparse | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 10.9 | 0 |
| 6 | `(11, 6, 3, 2, 2)` | `(6, 3, 2, 2)` | 13 | δ<δ_close=9: δ<= 6 of ladder | 3 | 19 | 10607 | 2 | 5785 | sparse | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 13.7 | 0 |
| 6 | `(8, 8, 4, 2, 2)` | `(8, 4, 2, 2)` | 16 | δ<δ_close=12: δ<= 6 of ladder | 3 | 8 | 22475 | 4 | 6247 | sparse | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 20.4 | 0 |
| 6 | `(8, 8, 5, 2, 1)` | `(8, 5, 2, 1)` | 16 | δ<δ_close=11: δ<= 6 of ladder | 2 | 8 | 12445 | 2 | 6294 | sparse | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 14.8 | 0 |
| 6 | `(9, 6, 6, 2, 1)` | `(6, 6, 2, 1)` | 15 | δ<δ_close=10: δ<= 6 of ladder | 2 | 8 | 12788 | 2 | 6501 | sparse | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 21.8 | 0 |
| 6 | `(11, 6, 4, 2, 1)` | `(6, 4, 2, 1)` | 13 | δ<δ_close=9: δ<= 6 of ladder | 7 | 32 | 6789 | 1 | 6789 | sparse | 7 (proved) | 7 (proved) | 7 (proved) | 0 | agree | 16.8 | 0 |
| 6 | `(10, 7, 3, 2, 2)` | `(7, 3, 2, 2)` | 14 | δ<δ_close=10: δ<= 6 of ladder | 2 | 17 | 13065 | 2 | 7102 | sparse | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 17.0 | 0 |
| 6 | `(11, 5, 4, 2, 2)` | `(5, 4, 2, 2)` | 13 | δ<δ_close=9: δ<= 6 of ladder | 3 | 18 | 13363 | 2 | 7271 | sparse | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 22.7 | 0 |
| 6 | `(10, 5, 5, 3, 1)` | `(5, 5, 3, 1)` | 14 | δ<δ_close=9: δ<= 6 of ladder | 2 | 9 | 14912 | 2 | 7306 | sparse | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 19.1 | 0 |
| 6 | `(9, 8, 3, 2, 2)` | `(8, 3, 2, 2)` | 15 | δ<δ_close=11: δ<= 6 of ladder | 2 | 11 | 14477 | 2 | 7860 | sparse | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 21.0 | 0 |
| 6 | `(10, 7, 4, 2, 1)` | `(7, 4, 2, 1)` | 14 | δ<δ_close=10: δ<= 6 of ladder | 7 | 31 | 8337 | 1 | 8337 | sparse | 7 (proved) | 7 (proved) | 7 (proved) | 0 | agree | 26.3 | 0 |
| 6 | `(8, 8, 4, 3, 1)` | `(8, 4, 3, 1)` | 16 | δ<δ_close=11: δ<= 6 of ladder | 1 | 7 | 16933 | 2 | 8553 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 27.1 | 0 |
| 6 | `(8, 6, 6, 2, 2)` | `(6, 6, 2, 2)` | 16 | δ<δ_close=11: δ<= 6 of ladder | 3 | 6 | 31356 | 4 | 8687 | sparse | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 42.7 | 0 |
| 6 | `(10, 5, 4, 4, 1)` | `(5, 4, 4, 1)` | 14 | δ<δ_close=9: δ<= 6 of ladder | 3 | 12 | 17075 | 2 | 8773 | sparse | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 28.2 | 0 |
| 6 | `(9, 8, 4, 2, 1)` | `(8, 4, 2, 1)` | 15 | δ<δ_close=11: δ<= 6 of ladder | 5 | 19 | 9224 | 1 | 9224 | sparse | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 31.0 | 0 |
| 6 | `(11, 4, 4, 3, 2)` | `(4, 4, 3, 2)` | 13 | δ<δ_close=8: δ<= 6 of ladder | 1 | 7 | 18161 | 2 | 9341 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 38.1 | 0 |
| 6 | `(10, 6, 4, 2, 2)` | `(6, 4, 2, 2)` | 14 | δ<δ_close=10: δ<= 6 of ladder | 6 | 24 | 17932 | 2 | 9743 | sparse | 6 (proved) | 6 (proved) | 6 (proved) | 0 | agree | 36.7 | 0 |
| 6 | `(10, 6, 5, 2, 1)` | `(6, 5, 2, 1)` | 14 | δ<δ_close=9: δ<= 6 of ladder | 5 | 20 | 9964 | 1 | 9964 | sparse | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 35.8 | 0 |
| 6 | `(11, 5, 4, 3, 1)` | `(5, 4, 3, 1)` | 13 | δ<δ_close=8: δ<= 6 of ladder | 4 | 18 | 10113 | 1 | 10113 | sparse | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 34.9 | 0 |
| 6 | `(9, 4, 4, 4, 3)` | `(4, 4, 4, 3)` | 15 | δ<δ_close=9: δ<= 6 of ladder | 1 | 2 | 60305 | 6 | 10719 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 108.3 | 0 |
| 6 | `(9, 6, 4, 4, 1)` | `(6, 4, 4, 1)` | 15 | δ<δ_close=10: δ<= 6 of ladder | 4 | 13 | 21982 | 2 | 11280 | sparse | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 49.5 | 0 |
| 6 | `(9, 7, 4, 2, 2)` | `(7, 4, 2, 2)` | 15 | δ<δ_close=11: δ<= 6 of ladder | 2 | 18 | 21215 | 2 | 11473 | sparse | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 46.8 | 0 |
| 6 | `(9, 7, 5, 2, 1)` | `(7, 5, 2, 1)` | 15 | δ<δ_close=10: δ<= 6 of ladder | 5 | 19 | 11766 | 1 | 11766 | sparse | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 52.1 | 0 |
| 6 | `(9, 5, 5, 4, 1)` | `(5, 5, 4, 1)` | 15 | δ<δ_close=9: δ<= 6 of ladder | 1 | 5 | 24258 | 2 | 11908 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 52.3 | 0 |
| 6 | `(8, 6, 6, 3, 1)` | `(6, 6, 3, 1)` | 16 | δ<δ_close=10: δ<= 6 of ladder | 1 | 4 | 23592 | 2 | 11955 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 79.0 | 0 |
| 6 | `(9, 7, 3, 3, 2)` | `(7, 3, 3, 2)` | 15 | δ<δ_close=9: δ<= 6 of ladder | 1 | 5 | 25246 | 2 | 12092 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 50.9 | 0 |
| 6 | `(6, 6, 4, 4, 4)` | `(6, 4, 4, 4)` | 18 | δ<δ_close=12: δ<= 6 of ladder | 1 | 1 | 133366 | 12 | 12096 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 152.2 | 0 |
| 6 | `(7, 7, 6, 3, 1)` | `(7, 6, 3, 1)` | 17 | δ<δ_close=11: δ<= 6 of ladder | 1 | 3 | 25213 | 2 | 12473 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 60.1 | 0 |
| 6 | `(8, 7, 4, 4, 1)` | `(7, 4, 4, 1)` | 16 | δ<δ_close=11: δ<= 6 of ladder | 2 | 8 | 24857 | 2 | 12743 | sparse | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 87.8 | 0 |
| 6 | `(6, 6, 6, 4, 2)` | `(6, 6, 4, 2)` | 18 | δ<δ_close=12: δ<= 6 of ladder | 1 | 1 | 76288 | 6 | 13194 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 189.8 | 0 |
| 6 | `(10, 6, 4, 3, 1)` | `(6, 4, 3, 1)` | 14 | δ<δ_close=9: δ<= 6 of ladder | 4 | 21 | 13533 | 1 | 13533 | sparse | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 64.5 | 0 |
| 6 | `(9, 6, 5, 2, 2)` | `(6, 5, 2, 2)` | 15 | δ<δ_close=10: δ<= 6 of ladder | 3 | 14 | 25456 | 2 | 13733 | sparse | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 70.3 | 0 |
| 6 | `(8, 7, 6, 2, 1)` | `(7, 6, 2, 1)` | 16 | δ<δ_close=11: δ<= 6 of ladder | 2 | 8 | 14436 | 1 | 14436 | sparse | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 73.2 | 0 |
| 6 | `(8, 7, 5, 2, 2)` | `(7, 5, 2, 2)` | 16 | δ<δ_close=11: δ<= 6 of ladder | 1 | 9 | 28802 | 2 | 15510 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 86.5 | 0 |
| 6 | `(7, 7, 5, 4, 1)` | `(7, 5, 4, 1)` | 17 | δ<δ_close=11: δ<= 6 of ladder | 1 | 3 | 31917 | 2 | 15798 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 96.2 | 0 |
| 6 | `(9, 7, 4, 3, 1)` | `(7, 4, 3, 1)` | 15 | δ<δ_close=10: δ<= 6 of ladder | 5 | 19 | 16005 | 1 | 16005 | sparse | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 98.2 | 0 |
| 6 | `(7, 7, 4, 3, 3)` | `(7, 4, 3, 3)` | 17 | δ<δ_close=10: δ<= 6 of ladder | 1 | 1 | 69495 | 4 | 16785 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 163.2 | 0 |
| 6 | `(8, 5, 5, 3, 3)` | `(5, 5, 3, 3)` | 16 | δ<δ_close=9: δ<= 6 of ladder | 1 | 1 | 71858 | 4 | 17270 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 180.0 | 0 |
| 6 | `(7, 6, 6, 4, 1)` | `(6, 6, 4, 1)` | 17 | δ<δ_close=11: δ<= 6 of ladder | 1 | 2 | 34726 | 2 | 17578 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 121.1 | 0 |
| 6 | `(9, 5, 5, 3, 2)` | `(5, 5, 3, 2)` | 15 | δ<δ_close=9: δ<= 6 of ladder | 1 | 5 | 38401 | 2 | 18877 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 131.6 | 0 |
| 6 | `(9, 6, 5, 3, 1)` | `(6, 5, 3, 1)` | 15 | δ<δ_close=10: δ<= 6 of ladder | 3 | 12 | 19188 | 1 | 19188 | sparse | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 135.2 | 0 |
| 6 | `(8, 7, 5, 3, 1)` | `(7, 5, 3, 1)` | 16 | δ<δ_close=11: δ<= 6 of ladder | 4 | 10 | 21694 | 1 | 21694 | sparse | 4 (proved) | 4 (proved) | — | 0 | agree | 112.5 | 0 |
| 6 | `(9, 5, 4, 4, 2)` | `(5, 4, 4, 2)` | 15 | δ<δ_close=10: δ<= 6 of ladder | 2 | 9 | 44031 | 2 | 22532 | sparse | 2 (proved) | 2 (proved) | — | 0 | agree | 195.8 | 0 |
| 6 | `(7, 7, 5, 3, 2)` | `(7, 5, 3, 2)` | 17 | δ<δ_close=11: δ<= 6 of ladder | 1 | 3 | 50668 | 2 | 25101 | sparse | 1 (proved) | 1 (proved) | — | 0 | agree | 153.8 | 0 |
| 6 | `(10, 5, 4, 3, 2)` | `(5, 4, 3, 2)` | 14 | δ<δ_close=9: δ<= 6 of ladder | 2 | 12 | 26921 | 1 | 26921 | sparse | 2 (proved) | 2 (proved) | — | 0 | agree | 153.9 | 0 |
| 6 | `(8, 6, 4, 4, 2)` | `(6, 4, 4, 2)` | 16 | δ<δ_close=11: δ<= 6 of ladder | 4 | 9 | 54343 | 2 | 27828 | sparse | 4 (proved) | 4 (proved) | — | 0 | agree | 346.6 | 0 |
| 6 | `(7, 6, 6, 3, 2)` | `(6, 6, 3, 2)` | 17 | δ<δ_close=11: δ<= 6 of ladder | 1 | 2 | 55158 | 2 | 27893 | sparse | 1 (proved) | 1 (proved) | — | 0 | agree | 352.2 | 0 |
| 6 | `(8, 6, 5, 4, 1)` | `(6, 5, 4, 1)` | 16 | δ<δ_close=10: δ<= 6 of ladder | 2 | 6 | 29854 | 1 | 29854 | sparse | 2 (proved) | 2 (proved) | — | 0 | agree | 224.6 | 0 |
| 6 | `(9, 6, 4, 3, 2)` | `(6, 4, 3, 2)` | 15 | δ<δ_close=10: δ<= 6 of ladder | 3 | 13 | 34756 | 1 | 34756 | sparse | 3 (proved) | 3 (proved) | — | 0 | agree | 282.3 | 0 |
| 6 | `(8, 7, 4, 3, 2)` | `(7, 4, 3, 2)` | 16 | δ<δ_close=11: δ<= 6 of ladder | 2 | 9 | 39362 | 1 | 39362 | sparse | 2 (proved) | 2 (proved) | — | 0 | agree | 386.7 | 0 |
| 6 | `(8, 5, 4, 4, 3)` | `(5, 4, 4, 3)` | 16 | δ<δ_close=10: δ<= 6 of ladder | 1 | 3 | 82457 | 2 | 42042 | sparse | 1 (proved) | 1 (proved) | — | 0 | agree | 768.9 | 0 |
| 6 | `(8, 6, 5, 3, 2)` | `(6, 5, 3, 2)` | 16 | δ<δ_close=10: δ<= 6 of ladder | 1 | 6 | 47357 | 1 | 47357 | sparse | 1 (proved) | 1 (proved) | — | 0 | agree | 535.3 | 0 |
| 6 | `(7, 6, 4, 4, 3)` | `(6, 4, 4, 3)` | 17 | δ<δ_close=11: δ<= 6 of ladder | 1 | 2 | 96185 | 2 | 49013 | sparse | 1 (proved) | 1 (proved) | — | 0 | agree | 1092.4 | 0 |
| 6 | `(7, 6, 5, 4, 2)` | `(6, 5, 4, 2)` | 17 | δ<δ_close=11: δ<= 6 of ladder | 1 | 3 | 70027 | 1 | 70027 | sparse | 1 (proved) | 1 (proved) | — | 0 | agree | 1252.6 | 0 |
| 7 | `(18, 4, 2, 2, 2)` | `(4, 2, 2, 2)` | 10 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 3 | 9 | 2565 | 6 | 606 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 1.5 | 4 |
| 7 | `(16, 5, 5, 1, 1)` | `(5, 5, 1, 1)` | 12 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 3 | 7 | 3575 | 4 | 663 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 1.3 | 2 |
| 7 | `(17, 5, 2, 2, 2)` | `(5, 2, 2, 2)` | 11 | δ<δ_close=8: δ<= 7 of ladder | 3 | 15 | 4306 | 6 | 978 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 1.1 | 2 |
| 7 | `(15, 8, 3, 1, 1)` | `(8, 3, 1, 1)` | 13 | δ<δ_close=8: δ<= 7 of ladder | 4 | 15 | 3127 | 2 | 1137 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 2.2 | 2 |
| 7 | `(16, 6, 4, 1, 1)` | `(6, 4, 1, 1)` | 12 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 3 | 17 | 3264 | 2 | 1177 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 2.0 | 2 |
| 7 | `(14, 9, 3, 1, 1)` | `(9, 3, 1, 1)` | 14 | δ<δ_close=9: δ<= 7 of ladder | 5 | 15 | 3782 | 2 | 1386 | dense | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 3.4 | 2 |
| 7 | `(14, 6, 6, 1, 1)` | `(6, 6, 1, 1)` | 14 | δ<δ_close=8: δ<= 7 of ladder | 1 | 9 | 7964 | 4 | 1471 | dense | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 1.6 | 2 |
| 7 | `(16, 6, 2, 2, 2)` | `(6, 2, 2, 2)` | 12 | δ<δ_close=9: δ<= 7 of ladder | 7 | 23 | 6602 | 6 | 1486 | dense | 7 (proved) | 7 (proved) | 7 (proved) | 0 | agree | 2.8 | 2 |
| 7 | `(11, 11, 4, 1, 1)` | `(11, 4, 1, 1)` | 17 | δ<δ_close=12: δ<= 7 of ladder | 4 | 7 | 7865 | 4 | 1502 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 3.0 | 2 |
| 7 | `(13, 10, 3, 1, 1)` | `(10, 3, 1, 1)` | 15 | δ<δ_close=10: δ<= 7 of ladder | 4 | 12 | 4289 | 2 | 1578 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 2.1 | 2 |
| 7 | `(15, 7, 4, 1, 1)` | `(7, 4, 1, 1)` | 13 | δ<δ_close=8: δ<= 7 of ladder | 8 | 25 | 4510 | 2 | 1658 | dense | 8 (proved) | 8 (proved) | 8 (proved) | 0 | agree | 2.8 | 2 |
| 7 | `(12, 11, 3, 1, 1)` | `(11, 3, 1, 1)` | 16 | δ<δ_close=11: δ<= 7 of ladder | 3 | 7 | 4562 | 2 | 1683 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 2.1 | 2 |
| 7 | `(16, 7, 2, 2, 1)` | `(7, 2, 2, 1)` | 12 | δ<δ_close=8: δ<= 7 of ladder | 5 | 22 | 3154 | 2 | 1759 | dense | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 2.5 | 2 |
| 7 | `(17, 4, 4, 2, 1)` | `(4, 4, 2, 1)` | 11 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 3 | 14 | 3753 | 2 | 1958 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 2.9 | 2 |
| 7 | `(15, 6, 5, 1, 1)` | `(6, 5, 1, 1)` | 13 | δ<δ_close=8: δ<= 7 of ladder | 4 | 15 | 5368 | 2 | 1988 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 3.4 | 2 |
| 7 | `(15, 7, 2, 2, 2)` | `(7, 2, 2, 2)` | 13 | δ<δ_close=10: δ<= 7 of ladder | 6 | 27 | 9196 | 6 | 2023 | dense | 6 (proved) | 6 (proved) | 6 (proved) | 0 | agree | 4.9 | 2 |
| 7 | `(14, 8, 4, 1, 1)` | `(8, 4, 1, 1)` | 14 | δ<δ_close=9: δ<= 7 of ladder | 7 | 28 | 5777 | 2 | 2133 | dense | 7 (proved) | 7 (proved) | 7 (proved) | 0 | agree | 4.4 | 2 |
| 7 | `(15, 8, 2, 2, 1)` | `(8, 2, 2, 1)` | 13 | δ<δ_close=9: δ<= 7 of ladder | 7 | 26 | 4098 | 2 | 2277 | dense | 7 (proved) | 7 (proved) | 7 (proved) | 0 | agree | 4.7 | 2 |
| 7 | `(13, 9, 4, 1, 1)` | `(9, 4, 1, 1)` | 15 | δ<δ_close=10: δ<= 7 of ladder | 10 | 25 | 6863 | 2 | 2561 | dense | 10 (proved) | 10 (proved) | 10 (proved) | 0 | agree | 7.2 | 2 |
| 7 | `(14, 8, 2, 2, 2)` | `(8, 2, 2, 2)` | 14 | δ<δ_close=11: δ<= 7 of ladder | 9 | 29 | 11875 | 6 | 2600 | dense | 9 (proved) | 9 (proved) | 9 (proved) | 0 | agree | 9.4 | 2 |
| 7 | `(12, 7, 7, 1, 1)` | `(7, 7, 1, 1)` | 16 | δ<δ_close=10: δ<= 7 of ladder | 7 | 10 | 14024 | 4 | 2712 | dense | 7 (proved) | 7 (proved) | 7 (proved) | 0 | agree | 10.1 | 2 |
| 7 | `(14, 9, 2, 2, 1)` | `(9, 2, 2, 1)` | 14 | δ<δ_close=10: δ<= 7 of ladder | 7 | 24 | 4966 | 2 | 2750 | dense | 7 (proved) | 7 (proved) | 7 (proved) | 0 | agree | 7.1 | 2 |
| 7 | `(14, 7, 5, 1, 1)` | `(7, 5, 1, 1)` | 14 | δ<δ_close=9: δ<= 7 of ladder | 10 | 25 | 7336 | 2 | 2751 | dense | 10 (proved) | 10 (proved) | 10 (proved) | 0 | agree | 8.4 | 2 |
| 7 | `(12, 10, 4, 1, 1)` | `(10, 4, 1, 1)` | 16 | δ<δ_close=11: δ<= 7 of ladder | 5 | 18 | 7613 | 2 | 2840 | dense | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 7.6 | 2 |
| 7 | `(10, 10, 6, 1, 1)` | `(10, 6, 1, 1)` | 18 | δ<δ_close=12: δ<= 7 of ladder | 1 | 6 | 15469 | 4 | 2924 | dense | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 7.3 | 2 |
| 7 | `(15, 4, 4, 4, 1)` | `(4, 4, 4, 1)` | 13 | δ<δ_close=8: δ<= 7 of ladder | 4 | 13 | 16239 | 6 | 2966 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 11.5 | 2 |
| 7 | `(13, 9, 2, 2, 2)` | `(9, 2, 2, 2)` | 15 | δ<δ_close=12: δ<= 7 of ladder | 6 | 26 | 14164 | 6 | 3063 | dense | 6 (proved) | 6 (proved) | 6 (proved) | 0 | agree | 12.2 | 2 |
| 7 | `(13, 10, 2, 2, 1)` | `(10, 2, 2, 1)` | 15 | δ<δ_close=11: δ<= 7 of ladder | 6 | 19 | 5640 | 2 | 3118 | dense | 6 (proved) | 6 (proved) | 6 (proved) | 0 | agree | 9.7 | 2 |
| 7 | `(17, 4, 3, 2, 2)` | `(4, 3, 2, 2)` | 11 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 2 | 10 | 5768 | 2 | 3197 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 8.7 | 2 |
| 7 | `(16, 4, 4, 2, 2)` | `(4, 4, 2, 2)` | 12 | δ<δ_close=8: δ<= 7 of ladder | 5 | 15 | 11158 | 4 | 3250 | dense | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 11.5 | 2 |
| 7 | `(17, 5, 3, 2, 1)` | `(5, 3, 2, 1)` | 11 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 4 | 19 | 3291 | 1 | 3291 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 9.2 | 2 |
| 7 | `(12, 11, 2, 2, 1)` | `(11, 2, 2, 1)` | 16 | δ<δ_close=12: δ<= 7 of ladder | 3 | 11 | 6003 | 2 | 3315 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 9.7 | 2 |
| 7 | `(12, 10, 2, 2, 2)` | `(10, 2, 2, 2)` | 16 | δ<δ_close=13: δ<= 7 of ladder | 7 | 17 | 15771 | 6 | 3414 | dense | 7 (proved) | 7 (proved) | 7 (proved) | 0 | agree | 15.6 | 2 |
| 7 | `(13, 8, 5, 1, 1)` | `(8, 5, 1, 1)` | 15 | δ<δ_close=10: δ<= 7 of ladder | 10 | 27 | 9228 | 2 | 3485 | dense | 10 (proved) | 10 (proved) | 10 (proved) | 0 | agree | 13.8 | 2 |
| 7 | `(16, 5, 3, 3, 1)` | `(5, 3, 3, 1)` | 12 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 2 | 10 | 7419 | 2 | 3504 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 11.1 | 2 |
| 7 | `(9, 9, 8, 1, 1)` | `(9, 8, 1, 1)` | 19 | δ<δ_close=12: δ<= 7 of ladder | 2 | 1 | 20299 | 4 | 3969 | dense | 2 (proved) | 1 (proved) | 1 (proved) | -1 | agree | 16.2 | 2 |
| 7 | `(13, 7, 6, 1, 1)` | `(7, 6, 1, 1)` | 15 | δ<δ_close=9: δ<= 7 of ladder | 8 | 19 | 10686 | 2 | 4052 | sparse | 8 (proved) | 8 (proved) | 8 (proved) | 0 | agree | 5.9 | 0 |
| 7 | `(12, 9, 5, 1, 1)` | `(9, 5, 1, 1)` | 16 | δ<δ_close=11: δ<= 7 of ladder | 10 | 23 | 10724 | 2 | 4072 | sparse | 10 (proved) | 10 (proved) | 10 (proved) | 0 | agree | 6.7 | 0 |
| 7 | `(16, 4, 4, 3, 1)` | `(4, 4, 3, 1)` | 12 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 2 | 13 | 8475 | 2 | 4384 | sparse | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 7.1 | 0 |
| 7 | `(11, 10, 5, 1, 1)` | `(10, 5, 1, 1)` | 17 | δ<δ_close=12: δ<= 7 of ladder | 6 | 14 | 11555 | 2 | 4398 | sparse | 6 (proved) | 6 (proved) | 6 (proved) | 0 | agree | 6.9 | 0 |
| 7 | `(12, 8, 6, 1, 1)` | `(8, 6, 1, 1)` | 16 | δ<δ_close=10: δ<= 7 of ladder | 7 | 21 | 13143 | 2 | 5001 | sparse | 7 (proved) | 7 (proved) | 7 (proved) | 0 | agree | 9.3 | 0 |
| 7 | `(16, 6, 3, 2, 1)` | `(6, 3, 2, 1)` | 12 | δ<δ_close=8: δ<= 7 of ladder | 7 | 32 | 5022 | 1 | 5022 | sparse | 7 (proved) | 7 (proved) | 7 (proved) | 0 | agree | 8.3 | 0 |
| 7 | `(15, 5, 5, 2, 1)` | `(5, 5, 2, 1)` | 13 | δ<δ_close=8: δ<= 7 of ladder | 5 | 22 | 10472 | 2 | 5106 | sparse | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 9.1 | 0 |
| 7 | `(15, 6, 3, 3, 1)` | `(6, 3, 3, 1)` | 13 | δ<δ_close=8: δ<= 7 of ladder | 3 | 18 | 11269 | 2 | 5343 | sparse | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 11.1 | 0 |
| 7 | `(16, 5, 3, 2, 2)` | `(5, 3, 2, 2)` | 12 | δ<δ_close=8: δ<= 7 of ladder | 3 | 21 | 9750 | 2 | 5356 | sparse | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 10.0 | 0 |
| 7 | `(11, 9, 6, 1, 1)` | `(9, 6, 1, 1)` | 17 | δ<δ_close=11: δ<= 7 of ladder | 9 | 16 | 14837 | 2 | 5687 | sparse | 9 (proved) | 9 (proved) | 9 (proved) | 0 | agree | 12.8 | 0 |
| 7 | `(11, 11, 3, 2, 1)` | `(11, 3, 2, 1)` | 17 | δ<δ_close=13: δ<= 7 of ladder | 4 | 12 | 12310 | 2 | 6101 | sparse | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 13.9 | 0 |
| 7 | `(16, 5, 4, 2, 1)` | `(5, 4, 2, 1)` | 12 | δ<δ_close=8: δ<= 7 of ladder | 8 | 34 | 6290 | 1 | 6290 | sparse | 8 (proved) | 8 (proved) | 8 (proved) | 0 | agree | 13.5 | 0 |
| 7 | `(11, 8, 7, 1, 1)` | `(8, 7, 1, 1)` | 17 | δ<δ_close=11: δ<= 7 of ladder | 6 | 12 | 16757 | 2 | 6452 | sparse | 6 (proved) | 6 (proved) | 6 (proved) | 0 | agree | 15.5 | 0 |
| 7 | `(15, 7, 3, 2, 1)` | `(7, 3, 2, 1)` | 13 | δ<δ_close=9: δ<= 7 of ladder | 11 | 44 | 6983 | 1 | 6983 | sparse | 11 (proved) | 11 (proved) | 11 (proved) | 0 | agree | 19.0 | 0 |
| 7 | `(10, 9, 7, 1, 1)` | `(9, 7, 1, 1)` | 18 | δ<δ_close=12: δ<= 7 of ladder | 4 | 7 | 18305 | 2 | 7068 | sparse | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 17.7 | 0 |
| 7 | `(14, 7, 3, 3, 1)` | `(7, 3, 3, 1)` | 14 | δ<δ_close=9: δ<= 7 of ladder | 7 | 26 | 15542 | 2 | 7398 | sparse | 7 (proved) | 7 (proved) | 7 (proved) | 0 | agree | 20.6 | 0 |
| 7 | `(15, 6, 3, 2, 2)` | `(6, 3, 2, 2)` | 13 | δ<δ_close=9: δ<= 7 of ladder | 8 | 36 | 14862 | 2 | 8123 | sparse | 8 (proved) | 8 (proved) | 8 (proved) | 0 | agree | 24.4 | 0 |
| 7 | `(14, 5, 5, 2, 2)` | `(5, 5, 2, 2)` | 14 | δ<δ_close=9: δ<= 7 of ladder | 2 | 20 | 31165 | 4 | 8151 | sparse | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 29.6 | 0 |
| 7 | `(14, 4, 4, 4, 2)` | `(4, 4, 4, 2)` | 14 | δ<δ_close=9: δ<= 7 of ladder | 6 | 15 | 48844 | 6 | 8812 | sparse | 6 (proved) | 6 (proved) | 6 (proved) | 0 | agree | 67.7 | 0 |
| 7 | `(14, 8, 3, 2, 1)` | `(8, 3, 2, 1)` | 14 | δ<δ_close=10: δ<= 7 of ladder | 14 | 50 | 8987 | 1 | 8987 | sparse | 14 (proved) | 14 (proved) | 14 (proved) | 0 | agree | 35.5 | 0 |
| 7 | `(13, 8, 3, 3, 1)` | `(8, 3, 3, 1)` | 15 | δ<δ_close=10: δ<= 7 of ladder | 7 | 27 | 19678 | 2 | 9385 | sparse | 7 (proved) | 7 (proved) | 7 (proved) | 0 | agree | 34.3 | 0 |
| 7 | `(15, 6, 4, 2, 1)` | `(6, 4, 2, 1)` | 13 | δ<δ_close=9: δ<= 7 of ladder | 15 | 58 | 9524 | 1 | 9524 | sparse | 15 (proved) | 15 (proved) | 15 (proved) | 0 | agree | 40.1 | 0 |
| 7 | `(12, 4, 4, 4, 4)` | `(4, 4, 4, 4)` | 16 | δ<δ_close=10: δ<= 7 of ladder | 4 | 4 | 205616 | 24 | 9738 | sparse | 4 (proved) | 3 (proved) | 3 (proved) | -1 | agree | 173.7 | 0 |
| 7 | `(15, 5, 4, 2, 2)` | `(5, 4, 2, 2)` | 13 | δ<δ_close=9: δ<= 7 of ladder | 7 | 34 | 18734 | 2 | 10216 | sparse | 7 (proved) | 7 (proved) | 7 (proved) | 0 | agree | 37.4 | 0 |
| 7 | `(15, 5, 3, 3, 2)` | `(5, 3, 3, 2)` | 13 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 1 | 9 | 22234 | 2 | 10592 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 34.0 | 0 |
| 7 | `(13, 9, 3, 2, 1)` | `(9, 3, 2, 1)` | 15 | δ<δ_close=11: δ<= 7 of ladder | 13 | 44 | 10712 | 1 | 10712 | sparse | 13 (proved) | 13 (proved) | 13 (proved) | 0 | agree | 51.3 | 0 |
| 7 | `(12, 9, 3, 3, 1)` | `(9, 3, 3, 1)` | 16 | δ<δ_close=11: δ<= 7 of ladder | 7 | 23 | 22969 | 2 | 10972 | sparse | 7 (proved) | 7 (proved) | 7 (proved) | 0 | agree | 49.2 | 0 |
| 7 | `(14, 7, 3, 2, 2)` | `(7, 3, 2, 2)` | 14 | δ<δ_close=10: δ<= 7 of ladder | 9 | 44 | 20552 | 2 | 11179 | sparse | 9 (proved) | 9 (proved) | 9 (proved) | 0 | agree | 60.3 | 0 |
| 7 | `(12, 5, 5, 5, 1)` | `(5, 5, 5, 1)` | 16 | δ<δ_close=9: δ<= 7 of ladder | 1 | 3 | 70510 | 6 | 11243 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 120.1 | 0 |
| 7 | `(14, 5, 5, 3, 1)` | `(5, 5, 3, 1)` | 14 | δ<δ_close=9: δ<= 7 of ladder | 6 | 22 | 23524 | 2 | 11536 | sparse | 6 (proved) | 6 (proved) | 6 (proved) | 0 | agree | 51.5 | 0 |
| 7 | `(13, 6, 6, 2, 1)` | `(6, 6, 2, 1)` | 15 | δ<δ_close=10: δ<= 7 of ladder | 10 | 30 | 23037 | 2 | 11697 | sparse | 10 (proved) | 10 (proved) | 10 (proved) | 0 | agree | 62.5 | 0 |
| 7 | `(8, 8, 8, 2, 2)` | `(8, 8, 2, 2)` | 20 | δ<δ_close=14: δ<= 7 of ladder | 3 | 2 | 127004 | 12 | 11778 | sparse | 3 (proved) | 2 (proved) | 2 (proved) | -1 | agree | 160.1 | 0 |
| 7 | `(11, 10, 3, 3, 1)` | `(10, 3, 3, 1)` | 17 | δ<δ_close=12: δ<= 7 of ladder | 4 | 13 | 24802 | 2 | 11856 | sparse | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 52.2 | 0 |
| 7 | `(12, 10, 3, 2, 1)` | `(10, 3, 2, 1)` | 16 | δ<δ_close=12: δ<= 7 of ladder | 10 | 31 | 11906 | 1 | 11906 | sparse | 10 (proved) | 10 (proved) | 10 (proved) | 0 | agree | 59.1 | 0 |
| 7 | `(14, 7, 4, 2, 1)` | `(7, 4, 2, 1)` | 14 | δ<δ_close=10: δ<= 7 of ladder | 21 | 76 | 13100 | 1 | 13100 | sparse | 21 (proved) | 21 (proved) | — | 0 | agree | 48.7 | 0 |
| 7 | `(15, 4, 4, 3, 2)` | `(4, 4, 3, 2)` | 13 | δ<δ_close=8: δ<= 7 of ladder | 3 | 14 | 25465 | 2 | 13100 | sparse | 3 (proved) | 3 (proved) | — | 0 | agree | 46.0 | 0 |
| 7 | `(14, 5, 4, 4, 1)` | `(5, 4, 4, 1)` | 14 | δ<δ_close=9: δ<= 7 of ladder | 7 | 27 | 26952 | 2 | 13838 | sparse | 7 (proved) | 7 (proved) | — | 0 | agree | 42.1 | 0 |
| 7 | `(13, 8, 3, 2, 2)` | `(8, 3, 2, 2)` | 15 | δ<δ_close=11: δ<= 7 of ladder | 12 | 47 | 26078 | 2 | 14147 | sparse | 12 (proved) | 12 (proved) | — | 0 | agree | 71.7 | 0 |
| 7 | `(15, 5, 4, 3, 1)` | `(5, 4, 3, 1)` | 13 | δ<δ_close=8: δ<= 7 of ladder | 8 | 32 | 14189 | 1 | 14189 | sparse | 8 (proved) | 8 (proved) | — | 0 | agree | 40.6 | 0 |
| 7 | `(12, 7, 3, 3, 3)` | `(7, 3, 3, 3)` | 16 | δ<δ_close=8: δ<= 7 of ladder | 1 | 3 | 100940 | 6 | 15132 | sparse | 1 (proved) | 1 (proved) | — | 0 | agree | 120.5 | 0 |
| 7 | `(14, 6, 4, 2, 2)` | `(6, 4, 2, 2)` | 14 | δ<δ_close=10: δ<= 7 of ladder | 17 | 58 | 28258 | 2 | 15358 | sparse | 17 (proved) | 17 (proved) | — | 0 | agree | 66.4 | 0 |
| 7 | `(10, 10, 4, 2, 2)` | `(10, 4, 2, 2)` | 18 | δ<δ_close=14: δ<= 7 of ladder | 9 | 17 | 56427 | 4 | 15454 | sparse | 9 (proved) | 9 (proved) | — | 0 | agree | 102.1 | 0 |
| 7 | `(10, 10, 5, 2, 1)` | `(10, 5, 2, 1)` | 18 | δ<δ_close=13: δ<= 7 of ladder | 8 | 19 | 30931 | 2 | 15577 | sparse | 8 (proved) | 8 (proved) | — | 0 | agree | 65.7 | 0 |
| 7 | `(14, 6, 5, 2, 1)` | `(6, 5, 2, 1)` | 14 | δ<δ_close=9: δ<= 7 of ladder | 14 | 50 | 15677 | 1 | 15677 | sparse | 14 (proved) | 14 (proved) | — | 0 | agree | 100.5 | 0 |
| 7 | `(14, 6, 3, 3, 2)` | `(6, 3, 3, 2)` | 14 | δ<δ_close=8: δ<= 7 of ladder | 2 | 17 | 33610 | 2 | 16041 | sparse | 2 (proved) | 2 (proved) | — | 0 | agree | 73.2 | 0 |
| 7 | `(12, 9, 3, 2, 2)` | `(9, 3, 2, 2)` | 16 | δ<δ_close=12: δ<= 7 of ladder | 9 | 38 | 30477 | 2 | 16499 | sparse | 9 (proved) | 9 (proved) | — | 0 | agree | 135.8 | 0 |
| 7 | `(11, 10, 3, 2, 2)` | `(10, 3, 2, 2)` | 17 | δ<δ_close=13: δ<= 7 of ladder | 6 | 21 | 32934 | 2 | 17813 | sparse | 6 (proved) | 6 (proved) | — | 0 | agree | 73.0 | 0 |
| 7 | `(13, 4, 4, 4, 3)` | `(4, 4, 4, 3)` | 15 | δ<δ_close=9: δ<= 7 of ladder | 3 | 8 | 110498 | 6 | 19579 | sparse | 3 (proved) | 3 (proved) | — | 0 | agree | 217.0 | 0 |
| 7 | `(10, 9, 3, 3, 3)` | `(9, 3, 3, 3)` | 18 | δ<δ_close=10: δ<= 7 of ladder | 1 | 2 | 133855 | 6 | 20177 | sparse | 1 (proved) | 1 (proved) | — | 0 | agree | 379.3 | 0 |
| 8 | `(22, 4, 2, 2, 2)` | `(4, 2, 2, 2)` | 10 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 3 | 9 | 2625 | 6 | 625 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 1.5 | 4 |
| 8 | `(20, 5, 5, 1, 1)` | `(5, 5, 1, 1)` | 12 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 3 | 7 | 3946 | 4 | 726 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 1.6 | 2 |
| 8 | `(18, 10, 2, 1, 1)` | `(10, 2, 1, 1)` | 14 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 2 | 9 | 2558 | 2 | 899 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 1.0 | 4 |
| 8 | `(20, 7, 3, 1, 1)` | `(7, 3, 1, 1)` | 12 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 4 | 14 | 2688 | 2 | 962 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 1.1 | 4 |
| 8 | `(21, 5, 2, 2, 2)` | `(5, 2, 2, 2)` | 11 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 4 | 16 | 4538 | 6 | 1040 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 1.3 | 2 |
| 8 | `(17, 11, 2, 1, 1)` | `(11, 2, 1, 1)` | 15 | δ<δ_close=9: δ<= 8 of ladder | 3 | 9 | 2980 | 2 | 1060 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 1.5 | 4 |
| 8 | `(16, 12, 2, 1, 1)` | `(12, 2, 1, 1)` | 16 | δ<δ_close=10: δ<= 8 of ladder | 2 | 7 | 3331 | 2 | 1182 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 2.2 | 2 |
| 8 | `(15, 13, 2, 1, 1)` | `(13, 2, 1, 1)` | 17 | δ<δ_close=11: δ<= 8 of ladder | 2 | 5 | 3553 | 2 | 1271 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 2.5 | 2 |
| 8 | `(20, 6, 4, 1, 1)` | `(6, 4, 1, 1)` | 12 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 3 | 18 | 3611 | 2 | 1293 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 2.6 | 2 |
| 8 | `(19, 8, 3, 1, 1)` | `(8, 3, 1, 1)` | 13 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 5 | 19 | 3673 | 2 | 1327 | dense | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 3.0 | 2 |
| 8 | `(20, 6, 2, 2, 2)` | `(6, 2, 2, 2)` | 12 | δ<δ_close=9: δ<= 8 of ladder | 8 | 26 | 7256 | 6 | 1647 | dense | 8 (proved) | 8 (proved) | 8 (proved) | 0 | agree | 3.8 | 2 |
| 8 | `(18, 9, 3, 1, 1)` | `(9, 3, 1, 1)` | 14 | δ<δ_close=9: δ<= 8 of ladder | 7 | 22 | 4730 | 2 | 1724 | dense | 7 (proved) | 7 (proved) | 7 (proved) | 0 | agree | 2.7 | 2 |
| 8 | `(18, 6, 6, 1, 1)` | `(6, 6, 1, 1)` | 14 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 2 | 13 | 9883 | 4 | 1816 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 2.8 | 2 |
| 8 | `(19, 7, 4, 1, 1)` | `(7, 4, 1, 1)` | 13 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 9 | 30 | 5265 | 2 | 1922 | dense | 9 (proved) | 9 (proved) | 9 (proved) | 0 | agree | 3.7 | 2 |
| 8 | `(20, 7, 2, 2, 1)` | `(7, 2, 2, 1)` | 12 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 6 | 25 | 3505 | 2 | 1961 | dense | 6 (proved) | 6 (proved) | 6 (proved) | 0 | agree | 3.3 | 2 |
| 8 | `(21, 4, 4, 2, 1)` | `(4, 4, 2, 1)` | 11 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 3 | 14 | 3950 | 2 | 2064 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 3.4 | 2 |
| 8 | `(17, 10, 3, 1, 1)` | `(10, 3, 1, 1)` | 15 | δ<δ_close=10: δ<= 8 of ladder | 8 | 24 | 5767 | 2 | 2114 | dense | 8 (proved) | 8 (proved) | 8 (proved) | 0 | agree | 4.4 | 2 |
| 8 | `(19, 6, 5, 1, 1)` | `(6, 5, 1, 1)` | 13 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 5 | 18 | 6250 | 2 | 2298 | dense | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 4.7 | 2 |
| 8 | `(19, 7, 2, 2, 2)` | `(7, 2, 2, 2)` | 13 | δ<δ_close=10: δ<= 8 of ladder | 9 | 34 | 10666 | 6 | 2365 | dense | 9 (proved) | 9 (proved) | 9 (proved) | 0 | agree | 7.9 | 2 |
| 8 | `(16, 11, 3, 1, 1)` | `(11, 3, 1, 1)` | 16 | δ<δ_close=11: δ<= 8 of ladder | 9 | 22 | 6675 | 2 | 2459 | dense | 9 (proved) | 9 (proved) | 9 (proved) | 0 | agree | 6.2 | 2 |
| 8 | `(18, 8, 4, 1, 1)` | `(8, 4, 1, 1)` | 14 | δ<δ_close=9: δ<= 8 of ladder | 11 | 40 | 7191 | 2 | 2640 | dense | 11 (proved) | 11 (proved) | 11 (proved) | 0 | agree | 7.6 | 2 |
| 8 | `(19, 8, 2, 2, 1)` | `(8, 2, 2, 1)` | 13 | δ<δ_close=9: δ<= 8 of ladder | 9 | 33 | 4803 | 2 | 2676 | dense | 9 (proved) | 9 (proved) | 9 (proved) | 0 | agree | 6.7 | 2 |
| 8 | `(13, 13, 4, 1, 1)` | `(13, 4, 1, 1)` | 19 | δ<δ_close=14: δ<= 8 of ladder | 6 | 10 | 14133 | 4 | 2701 | dense | 6 (proved) | 6 (proved) | 6 (proved) | 0 | agree | 9.4 | 2 |
| 8 | `(15, 12, 3, 1, 1)` | `(12, 3, 1, 1)` | 17 | δ<δ_close=12: δ<= 8 of ladder | 6 | 16 | 7359 | 2 | 2718 | dense | 6 (proved) | 6 (proved) | 6 (proved) | 0 | agree | 6.9 | 2 |
| 8 | `(14, 13, 3, 1, 1)` | `(13, 3, 1, 1)` | 18 | δ<δ_close=13: δ<= 8 of ladder | 4 | 10 | 7723 | 2 | 2857 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 6.8 | 2 |
| 8 | `(13, 13, 2, 2, 2)` | `(13, 2, 2, 2)` | 19 | δ<δ_close=16: δ<= 8 of ladder | 1 | 8 | 29372 | 12 | 3009 | dense | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 9.3 | 2 |
| 8 | `(18, 8, 2, 2, 2)` | `(8, 2, 2, 2)` | 14 | δ<δ_close=11: δ<= 8 of ladder | 14 | 43 | 14694 | 6 | 3238 | dense | 14 (proved) | 14 (proved) | 14 (proved) | 0 | agree | 17.0 | 2 |
| 8 | `(21, 4, 3, 2, 2)` | `(4, 3, 2, 2)` | 11 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 2 | 10 | 6044 | 2 | 3360 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 9.4 | 2 |
| 8 | `(18, 7, 5, 1, 1)` | `(7, 5, 1, 1)` | 14 | δ<δ_close=9: δ<= 8 of ladder | 14 | 35 | 9110 | 2 | 3394 | dense | 14 (proved) | 14 (proved) | 14 (proved) | 0 | agree | 14.1 | 2 |
| 8 | `(19, 4, 4, 4, 1)` | `(4, 4, 4, 1)` | 13 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 5 | 15 | 18630 | 6 | 3411 | dense | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 16.2 | 2 |
| 8 | `(17, 9, 4, 1, 1)` | `(9, 4, 1, 1)` | 15 | δ<δ_close=10: δ<= 8 of ladder | 17 | 46 | 9203 | 2 | 3419 | dense | 17 (proved) | 17 (proved) | 17 (proved) | 0 | agree | 15.8 | 2 |
| 8 | `(18, 9, 2, 2, 1)` | `(9, 2, 2, 1)` | 14 | δ<δ_close=10: δ<= 8 of ladder | 11 | 37 | 6198 | 2 | 3440 | dense | 11 (proved) | 11 (proved) | 11 (proved) | 0 | agree | 12.5 | 2 |
| 8 | `(21, 5, 3, 2, 1)` | `(5, 3, 2, 1)` | 11 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 4 | 19 | 3475 | 1 | 3475 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 10.6 | 2 |
| 8 | `(20, 4, 4, 2, 2)` | `(4, 4, 2, 2)` | 12 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 6 | 16 | 12141 | 4 | 3553 | dense | 6 (proved) | 6 (proved) | 6 (proved) | 0 | agree | 14.6 | 2 |
| 8 | `(20, 5, 3, 3, 1)` | `(5, 3, 3, 1)` | 12 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 2 | 10 | 8111 | 2 | 3821 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 13.4 | 2 |
| 8 | `(16, 7, 7, 1, 1)` | `(7, 7, 1, 1)` | 16 | δ<δ_close=10: δ<= 8 of ladder | 13 | 21 | 20517 | 4 | 3946 | dense | 13 (proved) | 13 (proved) | 13 (proved) | 0 | agree | 25.2 | 2 |
| 8 | `(17, 9, 2, 2, 2)` | `(9, 2, 2, 2)` | 15 | δ<δ_close=12: δ<= 8 of ladder | 13 | 46 | 18911 | 6 | 4107 | sparse | 13 (proved) | 13 (proved) | 13 (proved) | 0 | agree | 22.1 | 0 |
| 8 | `(16, 10, 4, 1, 1)` | `(10, 4, 1, 1)` | 16 | δ<δ_close=11: δ<= 8 of ladder | 16 | 46 | 11130 | 2 | 4145 | sparse | 16 (proved) | 16 (proved) | 16 (proved) | 0 | agree | 8.0 | 0 |
| 8 | `(17, 10, 2, 2, 1)` | `(10, 2, 2, 1)` | 15 | δ<δ_close=11: δ<= 8 of ladder | 12 | 38 | 7572 | 2 | 4192 | sparse | 12 (proved) | 12 (proved) | 12 (proved) | 0 | agree | 7.4 | 0 |
| 8 | `(17, 8, 5, 1, 1)` | `(8, 5, 1, 1)` | 15 | δ<δ_close=10: δ<= 8 of ladder | 18 | 48 | 12360 | 2 | 4644 | sparse | 18 (proved) | 18 (proved) | 18 (proved) | 0 | agree | 10.2 | 0 |
| 8 | `(15, 11, 4, 1, 1)` | `(11, 4, 1, 1)` | 17 | δ<δ_close=12: δ<= 8 of ladder | 18 | 40 | 12706 | 2 | 4767 | sparse | 18 (proved) | 18 (proved) | 18 (proved) | 0 | agree | 11.3 | 0 |
| 8 | `(20, 4, 4, 3, 1)` | `(4, 4, 3, 1)` | 12 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 2 | 13 | 9241 | 2 | 4787 | sparse | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 8.2 | 0 |
| 8 | `(16, 11, 2, 2, 1)` | `(11, 2, 2, 1)` | 16 | δ<δ_close=12: δ<= 8 of ladder | 11 | 34 | 8776 | 2 | 4848 | sparse | 11 (proved) | 11 (proved) | 11 (proved) | 0 | agree | 11.8 | 0 |
| 8 | `(16, 10, 2, 2, 2)` | `(10, 2, 2, 2)` | 16 | δ<δ_close=13: δ<= 8 of ladder | 17 | 45 | 22999 | 6 | 4983 | sparse | 17 (proved) | 17 (proved) | 17 (proved) | 0 | agree | 36.1 | 0 |
| 8 | `(14, 12, 4, 1, 1)` | `(12, 4, 1, 1)` | 18 | δ<δ_close=13: δ<= 8 of ladder | 9 | 26 | 13771 | 2 | 5163 | sparse | 9 (proved) | 9 (proved) | 9 (proved) | 0 | agree | 10.1 | 0 |
| 8 | `(15, 12, 2, 2, 1)` | `(12, 2, 2, 1)` | 17 | δ<δ_close=13: δ<= 8 of ladder | 9 | 26 | 9683 | 2 | 5343 | sparse | 9 (proved) | 9 (proved) | 9 (proved) | 0 | agree | 11.2 | 0 |
| 8 | `(17, 7, 6, 1, 1)` | `(7, 6, 1, 1)` | 15 | δ<δ_close=9: δ<= 8 of ladder | 13 | 33 | 14304 | 2 | 5395 | sparse | 13 (proved) | 13 (proved) | 13 (proved) | 0 | agree | 12.2 | 0 |
| 8 | `(20, 6, 3, 2, 1)` | `(6, 3, 2, 1)` | 12 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 8 | 35 | 5531 | 1 | 5531 | sparse | 8 (proved) | 8 (proved) | 8 (proved) | 0 | agree | 10.2 | 0 |
| 8 | `(14, 13, 2, 2, 1)` | `(13, 2, 2, 1)` | 18 | δ<δ_close=14: δ<= 8 of ladder | 5 | 14 | 10167 | 2 | 5606 | sparse | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 11.3 | 0 |
| 8 | `(15, 11, 2, 2, 2)` | `(11, 2, 2, 2)` | 17 | δ<δ_close=14: δ<= 8 of ladder | 11 | 37 | 26335 | 6 | 5653 | sparse | 11 (proved) | 11 (proved) | 11 (proved) | 0 | agree | 42.4 | 0 |
| 8 | `(20, 5, 3, 2, 2)` | `(5, 3, 2, 2)` | 12 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 4 | 23 | 10638 | 2 | 5863 | sparse | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 10.7 | 0 |
| 8 | `(19, 5, 5, 2, 1)` | `(5, 5, 2, 1)` | 13 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 7 | 26 | 12095 | 2 | 5895 | sparse | 7 (proved) | 7 (proved) | 7 (proved) | 0 | agree | 13.0 | 0 |
| 8 | `(16, 9, 5, 1, 1)` | `(9, 5, 1, 1)` | 16 | δ<δ_close=11: δ<= 8 of ladder | 24 | 54 | 15684 | 2 | 5937 | sparse | 24 (proved) | 24 (proved) | 24 (proved) | 0 | agree | 19.5 | 0 |
| 8 | `(12, 12, 6, 1, 1)` | `(12, 6, 1, 1)` | 20 | δ<δ_close=14: δ<= 8 of ladder | 4 | 11 | 31933 | 4 | 6089 | sparse | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 15.2 | 0 |
| 8 | `(14, 12, 2, 2, 2)` | `(12, 2, 2, 2)` | 18 | δ<δ_close=15: δ<= 8 of ladder | 11 | 25 | 28617 | 6 | 6151 | sparse | 11 (proved) | 11 (proved) | 11 (proved) | 0 | agree | 50.3 | 0 |
| 8 | `(19, 6, 3, 3, 1)` | `(6, 3, 3, 1)` | 13 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 4 | 21 | 13005 | 2 | 6154 | sparse | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 12.4 | 0 |
| 8 | `(14, 8, 8, 1, 1)` | `(8, 8, 1, 1)` | 18 | δ<δ_close=11: δ<= 8 of ladder | 5 | 15 | 35388 | 4 | 6791 | sparse | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 18.9 | 0 |
| 8 | `(20, 5, 4, 2, 1)` | `(5, 4, 2, 1)` | 12 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 9 | 36 | 6894 | 1 | 6894 | sparse | 9 (proved) | 9 (proved) | 9 (proved) | 0 | agree | 16.2 | 0 |
| 8 | `(15, 10, 5, 1, 1)` | `(10, 5, 1, 1)` | 17 | δ<δ_close=12: δ<= 8 of ladder | 24 | 53 | 18702 | 2 | 7113 | sparse | 24 (proved) | 24 (proved) | 24 (proved) | 0 | agree | 28.5 | 0 |
| 8 | `(16, 8, 6, 1, 1)` | `(8, 6, 1, 1)` | 16 | δ<δ_close=10: δ<= 8 of ladder | 18 | 48 | 19226 | 2 | 7294 | sparse | 18 (proved) | 18 (proved) | 18 (proved) | 0 | agree | 26.4 | 0 |
| 8 | `(14, 11, 5, 1, 1)` | `(11, 5, 1, 1)` | 18 | δ<δ_close=13: δ<= 8 of ladder | 22 | 43 | 20993 | 2 | 8013 | sparse | 22 (proved) | 22 (proved) | 22 (proved) | 0 | agree | 35.0 | 0 |
| 8 | `(19, 7, 3, 2, 1)` | `(7, 3, 2, 1)` | 13 | δ<δ_close=9: δ<= 8 of ladder | 14 | 54 | 8117 | 1 | 8117 | sparse | 14 (proved) | 14 (proved) | 14 (proved) | 0 | agree | 28.1 | 0 |
| 8 | `(13, 12, 5, 1, 1)` | `(12, 5, 1, 1)` | 19 | δ<δ_close=14: δ<= 8 of ladder | 11 | 22 | 22246 | 2 | 8503 | sparse | 11 (proved) | 11 (proved) | 11 (proved) | 0 | agree | 31.1 | 0 |
| 8 | `(18, 7, 3, 3, 1)` | `(7, 3, 3, 1)` | 14 | δ<δ_close=9: δ<= 8 of ladder | 10 | 36 | 19159 | 2 | 9105 | sparse | 10 (proved) | 10 (proved) | 10 (proved) | 0 | agree | 33.3 | 0 |
| 8 | `(15, 9, 6, 1, 1)` | `(9, 6, 1, 1)` | 17 | δ<δ_close=11: δ<= 8 of ladder | 27 | 54 | 24048 | 2 | 9207 | sparse | 27 (proved) | 27 (proved) | 27 (proved) | 0 | agree | 50.9 | 0 |
| 8 | `(19, 6, 3, 2, 2)` | `(6, 3, 2, 2)` | 13 | δ<δ_close=9: δ<= 8 of ladder | 11 | 44 | 17114 | 2 | 9382 | sparse | 11 (proved) | 11 (proved) | 11 (proved) | 0 | agree | 40.4 | 0 |
| 8 | `(11, 11, 8, 1, 1)` | `(11, 8, 1, 1)` | 21 | δ<δ_close=14: δ<= 8 of ladder | 8 | 8 | 49204 | 4 | 9684 | sparse | 8 (proved) | 7 (proved) | 7 (proved) | -1 | agree | 87.9 | 0 |
| 8 | `(12, 9, 9, 1, 1)` | `(9, 9, 1, 1)` | 20 | δ<δ_close=13: δ<= 8 of ladder | 7 | 6 | 49820 | 4 | 9800 | sparse | 7 (proved) | 5 (proved) | 5 (proved) | -2 | agree | 131.1 | 0 |
| 8 | `(18, 5, 5, 2, 2)` | `(5, 5, 2, 2)` | 14 | δ<δ_close=9: δ<= 8 of ladder | 4 | 29 | 38185 | 4 | 10016 | sparse | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 43.9 | 0 |
| 8 | `(15, 8, 7, 1, 1)` | `(8, 7, 1, 1)` | 17 | δ<δ_close=11: δ<= 8 of ladder | 18 | 36 | 27182 | 2 | 10450 | sparse | 18 (proved) | 18 (proved) | 18 (proved) | 0 | agree | 55.4 | 0 |
| 8 | `(18, 4, 4, 4, 2)` | `(4, 4, 4, 2)` | 14 | δ<δ_close=9: δ<= 8 of ladder | 9 | 21 | 59569 | 6 | 10766 | sparse | 9 (proved) | 9 (proved) | 9 (proved) | 0 | agree | 107.5 | 0 |
| 8 | `(14, 10, 6, 1, 1)` | `(10, 6, 1, 1)` | 18 | δ<δ_close=12: δ<= 8 of ladder | 23 | 50 | 28181 | 2 | 10814 | sparse | 23 (proved) | 23 (proved) | 23 (proved) | 0 | agree | 66.9 | 0 |
| 8 | `(13, 13, 3, 2, 1)` | `(13, 3, 2, 1)` | 19 | δ<δ_close=15: δ<= 8 of ladder | 6 | 16 | 22168 | 2 | 11011 | sparse | 6 (proved) | 6 (proved) | 6 (proved) | 0 | agree | 51.1 | 0 |
| 8 | `(19, 6, 4, 2, 1)` | `(6, 4, 2, 1)` | 13 | δ<δ_close=9: δ<= 8 of ladder | 19 | 70 | 11015 | 1 | 11015 | sparse | 19 (proved) | 19 (proved) | 19 (proved) | 0 | agree | 58.6 | 0 |
| 8 | `(18, 8, 3, 2, 1)` | `(8, 3, 2, 1)` | 14 | δ<δ_close=10: δ<= 8 of ladder | 21 | 72 | 11144 | 1 | 11144 | sparse | 21 (proved) | 21 (proved) | 21 (proved) | 0 | agree | 63.0 | 0 |
| 8 | `(19, 5, 4, 2, 2)` | `(5, 4, 2, 2)` | 13 | δ<δ_close=9: δ<= 8 of ladder | 10 | 41 | 21496 | 2 | 11758 | sparse | 10 (proved) | 10 (proved) | 10 (proved) | 0 | agree | 54.4 | 0 |
| 8 | `(13, 11, 6, 1, 1)` | `(11, 6, 1, 1)` | 19 | δ<δ_close=13: δ<= 8 of ladder | 22 | 36 | 30933 | 2 | 11927 | sparse | 22 (proved) | 22 (proved) | 22 (proved) | 0 | agree | 79.7 | 0 |
| 8 | `(19, 5, 3, 3, 2)` | `(5, 3, 3, 2)` | 13 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 1 | 10 | 25456 | 2 | 12103 | sparse | 1 (proved) | 1 (proved) | — | 0 | agree | 34.1 | 0 |
| 8 | `(17, 8, 3, 3, 1)` | `(8, 3, 3, 1)` | 15 | δ<δ_close=10: δ<= 8 of ladder | 14 | 48 | 26219 | 2 | 12493 | sparse | 14 (proved) | 14 (proved) | — | 0 | agree | 41.0 | 0 |
| 8 | `(14, 9, 7, 1, 1)` | `(9, 7, 1, 1)` | 18 | δ<δ_close=12: δ<= 8 of ladder | 25 | 41 | 33416 | 2 | 12925 | sparse | 25 (proved) | 25 (proved) | — | 0 | agree | 55.7 | 0 |
| 8 | `(18, 7, 3, 2, 2)` | `(7, 3, 2, 2)` | 14 | δ<δ_close=10: δ<= 8 of ladder | 15 | 63 | 25284 | 2 | 13789 | sparse | 15 (proved) | 15 (proved) | — | 0 | agree | 62.1 | 0 |
| 8 | `(16, 4, 4, 4, 4)` | `(4, 4, 4, 4)` | 16 | δ<δ_close=10: δ<= 8 of ladder | 7 | 10 | 299333 | 24 | 14148 | sparse | 7 (proved) | 6 (proved) | — | -1 | agree | 333.3 | 0 |
| 8 | `(18, 5, 5, 3, 1)` | `(5, 5, 3, 1)` | 14 | δ<δ_close=9: δ<= 8 of ladder | 9 | 30 | 28877 | 2 | 14156 | sparse | 9 (proved) | 9 (proved) | — | 0 | agree | 46.3 | 0 |
| 8 | `(17, 9, 3, 2, 1)` | `(9, 3, 2, 1)` | 15 | δ<δ_close=11: δ<= 8 of ladder | 26 | 81 | 14325 | 1 | 14325 | sparse | 26 (proved) | 26 (proved) | — | 0 | agree | 63.8 | 0 |
| 8 | `(13, 10, 7, 1, 1)` | `(10, 7, 1, 1)` | 19 | δ<δ_close=13: δ<= 8 of ladder | 22 | 36 | 38291 | 2 | 14862 | sparse | 22 (proved) | 22 (proved) | — | 0 | agree | 70.9 | 0 |
| 8 | `(19, 4, 4, 3, 2)` | `(4, 4, 3, 2)` | 13 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 4 | 16 | 29093 | 2 | 14980 | sparse | 4 (proved) | 4 (proved) | — | 0 | agree | 57.0 | 0 |
| 8 | `(17, 6, 6, 2, 1)` | `(6, 6, 2, 1)` | 15 | δ<δ_close=10: δ<= 8 of ladder | 18 | 53 | 30685 | 2 | 15576 | sparse | 18 (proved) | 18 (proved) | — | 0 | agree | 71.8 | 0 |
| 8 | `(12, 11, 7, 1, 1)` | `(11, 7, 1, 1)` | 20 | δ<δ_close=14: δ<= 8 of ladder | 15 | 21 | 40951 | 2 | 15926 | sparse | 15 (proved) | 15 (proved) | — | 0 | agree | 73.0 | 0 |
| 8 | `(16, 9, 3, 3, 1)` | `(9, 3, 3, 1)` | 16 | δ<δ_close=11: δ<= 8 of ladder | 19 | 54 | 33501 | 2 | 16000 | sparse | 19 (proved) | 19 (proved) | — | 0 | agree | 104.4 | 0 |
| 8 | `(19, 5, 4, 3, 1)` | `(5, 4, 3, 1)` | 13 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 10 | 37 | 16315 | 1 | 16315 | sparse | 10 (proved) | 10 (proved) | — | 0 | agree | 114.2 | 0 |
| 8 | `(16, 5, 5, 5, 1)` | `(5, 5, 5, 1)` | 16 | δ<δ_close=9: δ<= 8 of ladder | 2 | 7 | 102820 | 6 | 16402 | sparse | 2 (proved) | 2 (proved) | — | 0 | agree | 155.9 | 0 |
| 8 | `(13, 9, 8, 1, 1)` | `(9, 8, 1, 1)` | 19 | δ<δ_close=12: δ<= 8 of ladder | 15 | 21 | 42539 | 2 | 16556 | sparse | 15 (proved) | 13 (proved) | — | -2 | agree | 211.6 | 0 |
| 8 | `(18, 5, 4, 4, 1)` | `(5, 4, 4, 1)` | 14 | δ<δ_close=9: δ<= 8 of ladder | 11 | 37 | 33034 | 2 | 16973 | sparse | 11 (proved) | 11 (proved) | — | 0 | agree | 69.2 | 0 |
| 8 | `(12, 10, 8, 1, 1)` | `(10, 8, 1, 1)` | 20 | δ<δ_close=13: δ<= 8 of ladder | 9 | 17 | 47488 | 2 | 18503 | sparse | 9 (proved) | 9 (proved) | — | 0 | agree | 173.5 | 0 |
| 8 | `(18, 6, 3, 3, 2)` | `(6, 3, 3, 2)` | 14 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 4 | 24 | 41144 | 2 | 19608 | sparse | 4 (proved) | 4 (proved) | — | 0 | agree | 181.2 | 0 |
| 9 | `(26, 4, 2, 2, 2)` | `(4, 2, 2, 2)` | 10 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 3 | 9 | 2635 | 6 | 629 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 1.6 | 4 |
| 9 | `(24, 5, 5, 1, 1)` | `(5, 5, 1, 1)` | 12 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 3 | 7 | 4080 | 4 | 747 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 1.6 | 2 |
| 9 | `(24, 7, 3, 1, 1)` | `(7, 3, 1, 1)` | 12 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 4 | 14 | 2804 | 2 | 999 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 1.2 | 4 |
| 9 | `(22, 10, 2, 1, 1)` | `(10, 2, 1, 1)` | 14 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 2 | 11 | 2885 | 2 | 1010 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 1.3 | 4 |
| 9 | `(25, 5, 2, 2, 2)` | `(5, 2, 2, 2)` | 11 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 4 | 16 | 4598 | 6 | 1059 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 1.3 | 2 |
| 9 | `(21, 11, 2, 1, 1)` | `(11, 2, 1, 1)` | 15 | δ>=δ_close=9: whole ladder (a_δ = a_∞) | 4 | 12 | 3510 | 2 | 1243 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 2.4 | 2 |
| 9 | `(24, 6, 4, 1, 1)` | `(6, 4, 1, 1)` | 12 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 3 | 18 | 3742 | 2 | 1334 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 2.9 | 2 |
| 9 | `(23, 8, 3, 1, 1)` | `(8, 3, 1, 1)` | 13 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 5 | 20 | 3948 | 2 | 1419 | dense | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 3.4 | 2 |
| 9 | `(20, 12, 2, 1, 1)` | `(12, 2, 1, 1)` | 16 | δ<δ_close=10: δ<= 9 of ladder | 3 | 12 | 4120 | 2 | 1459 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 3.6 | 2 |
| 9 | `(19, 13, 2, 1, 1)` | `(13, 2, 1, 1)` | 17 | δ<δ_close=11: δ<= 9 of ladder | 4 | 11 | 4653 | 2 | 1661 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 2.2 | 2 |
| 9 | `(24, 6, 2, 2, 2)` | `(6, 2, 2, 2)` | 12 | δ>=δ_close=9: whole ladder (a_δ = a_∞) | 9 | 27 | 7489 | 6 | 1710 | dense | 9 (proved) | 9 (proved) | 9 (proved) | 0 | agree | 4.2 | 2 |
| 9 | `(18, 14, 2, 1, 1)` | `(14, 2, 1, 1)` | 18 | δ<δ_close=12: δ<= 9 of ladder | 2 | 9 | 5081 | 2 | 1811 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 2.2 | 2 |
| 9 | `(22, 9, 3, 1, 1)` | `(9, 3, 1, 1)` | 14 | δ>=δ_close=9: whole ladder (a_δ = a_∞) | 8 | 26 | 5280 | 2 | 1915 | dense | 8 (proved) | 8 (proved) | 8 (proved) | 0 | agree | 3.3 | 2 |
| 9 | `(17, 15, 2, 1, 1)` | `(15, 2, 1, 1)` | 19 | δ<δ_close=13: δ<= 9 of ladder | 3 | 6 | 5349 | 2 | 1917 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 3.0 | 2 |
| 9 | `(22, 6, 6, 1, 1)` | `(6, 6, 1, 1)` | 14 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 2 | 14 | 10867 | 4 | 1987 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 3.3 | 2 |
| 9 | `(23, 7, 4, 1, 1)` | `(7, 4, 1, 1)` | 13 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 9 | 31 | 5616 | 2 | 2039 | dense | 9 (proved) | 9 (proved) | 9 (proved) | 0 | agree | 4.3 | 2 |
| 9 | `(24, 7, 2, 2, 1)` | `(7, 2, 2, 1)` | 12 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 6 | 26 | 3651 | 2 | 2047 | dense | 6 (proved) | 6 (proved) | 6 (proved) | 0 | agree | 3.5 | 2 |
| 9 | `(25, 4, 4, 2, 1)` | `(4, 4, 2, 1)` | 11 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 3 | 14 | 4000 | 2 | 2093 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 3.4 | 2 |
| 9 | `(23, 6, 5, 1, 1)` | `(6, 5, 1, 1)` | 13 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 5 | 18 | 6637 | 2 | 2427 | dense | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 5.4 | 2 |
| 9 | `(21, 10, 3, 1, 1)` | `(10, 3, 1, 1)` | 15 | δ<δ_close=10: δ<= 9 of ladder | 10 | 31 | 6731 | 2 | 2456 | dense | 10 (proved) | 10 (proved) | 10 (proved) | 0 | agree | 6.0 | 2 |
| 9 | `(23, 7, 2, 2, 2)` | `(7, 2, 2, 2)` | 13 | δ<δ_close=10: δ<= 9 of ladder | 10 | 37 | 11324 | 6 | 2528 | dense | 10 (proved) | 10 (proved) | 10 (proved) | 0 | agree | 9.3 | 2 |
| 9 | `(23, 8, 2, 2, 1)` | `(8, 2, 2, 1)` | 13 | δ>=δ_close=9: whole ladder (a_δ = a_∞) | 10 | 36 | 5155 | 2 | 2879 | dense | 10 (proved) | 10 (proved) | 10 (proved) | 0 | agree | 8.2 | 2 |
| 9 | `(22, 8, 4, 1, 1)` | `(8, 4, 1, 1)` | 14 | δ>=δ_close=9: whole ladder (a_δ = a_∞) | 12 | 45 | 7962 | 2 | 2908 | dense | 12 (proved) | 12 (proved) | 12 (proved) | 0 | agree | 9.8 | 2 |
| 9 | `(20, 11, 3, 1, 1)` | `(11, 3, 1, 1)` | 16 | δ<δ_close=11: δ<= 9 of ladder | 13 | 34 | 8198 | 2 | 3009 | dense | 13 (proved) | 13 (proved) | 13 (proved) | 0 | agree | 10.2 | 2 |
| 9 | `(25, 4, 3, 2, 2)` | `(4, 3, 2, 2)` | 11 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 2 | 10 | 6108 | 2 | 3401 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 9.7 | 2 |
| 9 | `(25, 5, 3, 2, 1)` | `(5, 3, 2, 1)` | 11 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 4 | 19 | 3524 | 1 | 3524 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 10.6 | 2 |
| 9 | `(19, 12, 3, 1, 1)` | `(12, 3, 1, 1)` | 17 | δ<δ_close=12: δ<= 9 of ladder | 12 | 32 | 9587 | 2 | 3531 | dense | 12 (proved) | 12 (proved) | 12 (proved) | 0 | agree | 15.6 | 2 |
| 9 | `(23, 4, 4, 4, 1)` | `(4, 4, 4, 1)` | 13 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 5 | 15 | 19525 | 6 | 3587 | dense | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 17.7 | 2 |
| 9 | `(22, 8, 2, 2, 2)` | `(8, 2, 2, 2)` | 14 | δ<δ_close=11: δ<= 9 of ladder | 17 | 50 | 16184 | 6 | 3588 | dense | 17 (proved) | 17 (proved) | 17 (proved) | 0 | agree | 22.0 | 2 |
| 9 | `(24, 4, 4, 2, 2)` | `(4, 4, 2, 2)` | 12 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 6 | 16 | 12436 | 4 | 3651 | dense | 6 (proved) | 6 (proved) | 6 (proved) | 0 | agree | 15.0 | 2 |
| 9 | `(22, 7, 5, 1, 1)` | `(7, 5, 1, 1)` | 14 | δ>=δ_close=9: whole ladder (a_δ = a_∞) | 15 | 38 | 10036 | 2 | 3718 | dense | 15 (proved) | 15 (proved) | 15 (proved) | 0 | agree | 17.2 | 2 |
| 9 | `(22, 9, 2, 2, 1)` | `(9, 2, 2, 1)` | 14 | δ<δ_close=10: δ<= 9 of ladder | 13 | 44 | 6907 | 2 | 3842 | dense | 13 (proved) | 13 (proved) | 13 (proved) | 0 | agree | 16.0 | 2 |
| 9 | `(24, 5, 3, 3, 1)` | `(5, 3, 3, 1)` | 12 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 2 | 10 | 8336 | 2 | 3920 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 14.2 | 2 |
| 9 | `(21, 9, 4, 1, 1)` | `(9, 4, 1, 1)` | 15 | δ<δ_close=10: δ<= 9 of ladder | 21 | 58 | 10662 | 2 | 3940 | dense | 21 (proved) | 21 (proved) | 21 (proved) | 0 | agree | 21.3 | 2 |
| 9 | `(18, 13, 3, 1, 1)` | `(13, 3, 1, 1)` | 18 | δ<δ_close=13: δ<= 9 of ladder | 12 | 29 | 10766 | 2 | 3978 | dense | 12 (proved) | 12 (proved) | 12 (proved) | 0 | agree | 18.4 | 2 |
| 9 | `(17, 14, 3, 1, 1)` | `(14, 3, 1, 1)` | 19 | δ<δ_close=14: δ<= 9 of ladder | 9 | 22 | 11627 | 2 | 4304 | sparse | 9 (proved) | 9 (proved) | 9 (proved) | 0 | agree | 7.0 | 0 |
| 9 | `(15, 15, 4, 1, 1)` | `(15, 4, 1, 1)` | 21 | δ<δ_close=16: δ<= 9 of ladder | 9 | 12 | 23136 | 4 | 4415 | sparse | 9 (proved) | 8 (proved) | 8 (proved) | -1 | agree | 17.2 | 0 |
| 9 | `(16, 15, 3, 1, 1)` | `(15, 3, 1, 1)` | 20 | δ<δ_close=15: δ<= 9 of ladder | 5 | 11 | 12085 | 2 | 4478 | sparse | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 6.9 | 0 |
| 9 | `(20, 7, 7, 1, 1)` | `(7, 7, 1, 1)` | 16 | δ<δ_close=10: δ<= 9 of ladder | 17 | 29 | 24865 | 4 | 4753 | sparse | 17 (proved) | 17 (proved) | 17 (proved) | 0 | agree | 12.0 | 0 |
| 9 | `(21, 9, 2, 2, 2)` | `(9, 2, 2, 2)` | 15 | δ<δ_close=12: δ<= 9 of ladder | 18 | 60 | 21793 | 6 | 4764 | sparse | 18 (proved) | 18 (proved) | 18 (proved) | 0 | agree | 32.3 | 0 |
| 9 | `(21, 10, 2, 2, 1)` | `(10, 2, 2, 1)` | 15 | δ<δ_close=11: δ<= 9 of ladder | 16 | 51 | 8822 | 2 | 4894 | sparse | 16 (proved) | 16 (proved) | 16 (proved) | 0 | agree | 11.3 | 0 |
| 9 | `(24, 4, 4, 3, 1)` | `(4, 4, 3, 1)` | 12 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 2 | 13 | 9479 | 2 | 4916 | sparse | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 7.4 | 0 |
| 9 | `(15, 15, 2, 2, 2)` | `(15, 2, 2, 2)` | 21 | δ<δ_close=18: δ<= 9 of ladder | 2 | 12 | 48120 | 12 | 4964 | sparse | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 19.2 | 0 |
| 9 | `(20, 10, 4, 1, 1)` | `(10, 4, 1, 1)` | 16 | δ<δ_close=11: δ<= 9 of ladder | 23 | 68 | 13587 | 2 | 5040 | sparse | 23 (proved) | 23 (proved) | 23 (proved) | 0 | agree | 13.7 | 0 |
| 9 | `(21, 8, 5, 1, 1)` | `(8, 5, 1, 1)` | 15 | δ<δ_close=10: δ<= 9 of ladder | 22 | 59 | 14247 | 2 | 5323 | sparse | 22 (proved) | 22 (proved) | 22 (proved) | 0 | agree | 35.0 | 0 |
| 9 | `(24, 6, 3, 2, 1)` | `(6, 3, 2, 1)` | 12 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 8 | 35 | 5716 | 1 | 5716 | sparse | 8 (proved) | 8 (proved) | 8 (proved) | 0 | agree | 10.6 | 0 |
| 9 | `(20, 11, 2, 2, 1)` | `(11, 2, 2, 1)` | 16 | δ<δ_close=12: δ<= 9 of ladder | 17 | 53 | 10761 | 2 | 5954 | sparse | 17 (proved) | 17 (proved) | 17 (proved) | 0 | agree | 17.3 | 0 |
| 9 | `(24, 5, 3, 2, 2)` | `(5, 3, 2, 2)` | 12 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 4 | 23 | 10918 | 2 | 6029 | sparse | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 11.2 | 0 |
| 9 | `(20, 10, 2, 2, 2)` | `(10, 2, 2, 2)` | 16 | δ<δ_close=13: δ<= 9 of ladder | 25 | 66 | 27936 | 6 | 6079 | sparse | 25 (proved) | 25 (proved) | 25 (proved) | 0 | agree | 61.5 | 0 |
| 9 | `(19, 11, 4, 1, 1)` | `(11, 4, 1, 1)` | 17 | δ<δ_close=12: δ<= 9 of ladder | 31 | 71 | 16483 | 2 | 6162 | sparse | 31 (proved) | 31 (proved) | 31 (proved) | 0 | agree | 23.7 | 0 |
| 9 | `(21, 7, 6, 1, 1)` | `(7, 6, 1, 1)` | 15 | δ>=δ_close=9: whole ladder (a_δ = a_∞) | 16 | 40 | 16447 | 2 | 6167 | sparse | 16 (proved) | 16 (proved) | 16 (proved) | 0 | agree | 29.3 | 0 |
| 9 | `(23, 5, 5, 2, 1)` | `(5, 5, 2, 1)` | 13 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 7 | 26 | 12749 | 2 | 6208 | sparse | 7 (proved) | 7 (proved) | 7 (proved) | 0 | agree | 17.2 | 0 |
| 9 | `(23, 6, 3, 3, 1)` | `(6, 3, 3, 1)` | 13 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 4 | 21 | 13715 | 2 | 6477 | sparse | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 27.1 | 0 |
| 9 | `(19, 12, 2, 2, 1)` | `(12, 2, 2, 1)` | 17 | δ<δ_close=13: δ<= 9 of ladder | 18 | 51 | 12599 | 2 | 6960 | sparse | 18 (proved) | 18 (proved) | 18 (proved) | 0 | agree | 29.0 | 0 |
| 9 | `(24, 5, 4, 2, 1)` | `(5, 4, 2, 1)` | 12 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 9 | 36 | 7095 | 1 | 7095 | sparse | 9 (proved) | 9 (proved) | 9 (proved) | 0 | agree | 17.3 | 0 |
| 9 | `(18, 12, 4, 1, 1)` | `(12, 4, 1, 1)` | 18 | δ<δ_close=13: δ<= 9 of ladder | 26 | 66 | 19147 | 2 | 7168 | sparse | 26 (proved) | 26 (proved) | 26 (proved) | 0 | agree | 29.6 | 0 |
| 9 | `(20, 9, 5, 1, 1)` | `(9, 5, 1, 1)` | 16 | δ<δ_close=11: δ<= 9 of ladder | 34 | 78 | 19068 | 2 | 7183 | sparse | 34 (proved) | 34 (proved) | 34 (proved) | 0 | agree | 79.1 | 0 |
| 9 | `(19, 11, 2, 2, 2)` | `(11, 2, 2, 2)` | 17 | δ<δ_close=14: δ<= 9 of ladder | 22 | 67 | 34024 | 6 | 7332 | sparse | 22 (proved) | 22 (proved) | 22 (proved) | 0 | agree | 86.6 | 0 |
| 9 | `(18, 13, 2, 2, 1)` | `(13, 2, 2, 1)` | 18 | δ<δ_close=14: δ<= 9 of ladder | 16 | 44 | 14160 | 2 | 7811 | sparse | 16 (proved) | 16 (proved) | 16 (proved) | 0 | agree | 29.8 | 0 |
| 9 | `(17, 13, 4, 1, 1)` | `(13, 4, 1, 1)` | 19 | δ<δ_close=14: δ<= 9 of ladder | 27 | 55 | 21268 | 2 | 8001 | sparse | 27 (proved) | 27 (proved) | 27 (proved) | 0 | agree | 38.0 | 0 |
| 9 | `(17, 14, 2, 2, 1)` | `(14, 2, 2, 1)` | 19 | δ<δ_close=15: δ<= 9 of ladder | 12 | 33 | 15302 | 2 | 8434 | sparse | 12 (proved) | 12 (proved) | 12 (proved) | 0 | agree | 32.1 | 0 |
| 9 | `(16, 14, 4, 1, 1)` | `(14, 4, 1, 1)` | 20 | δ<δ_close=15: δ<= 9 of ladder | 14 | 36 | 22666 | 2 | 8523 | sparse | 14 (proved) | 14 (proved) | 14 (proved) | 0 | agree | 33.9 | 0 |
| 9 | `(18, 12, 2, 2, 2)` | `(12, 2, 2, 2)` | 18 | δ<δ_close=15: δ<= 9 of ladder | 26 | 62 | 39670 | 6 | 8538 | sparse | 26 (proved) | 26 (proved) | 26 (proved) | 0 | agree | 128.4 | 0 |
| 9 | `(23, 7, 3, 2, 1)` | `(7, 3, 2, 1)` | 13 | δ>=δ_close=9: whole ladder (a_δ = a_∞) | 15 | 57 | 8630 | 1 | 8630 | sparse | 15 (proved) | 15 (proved) | 15 (proved) | 0 | agree | 31.5 | 0 |
| 9 | `(16, 15, 2, 2, 1)` | `(15, 2, 2, 1)` | 20 | δ<δ_close=16: δ<= 9 of ladder | 6 | 17 | 15908 | 2 | 8764 | sparse | 6 (proved) | 6 (proved) | 6 (proved) | 0 | agree | 28.8 | 0 |
| 9 | `(20, 8, 6, 1, 1)` | `(8, 6, 1, 1)` | 16 | δ<δ_close=10: δ<= 9 of ladder | 25 | 68 | 23316 | 2 | 8802 | sparse | 25 (proved) | 25 (proved) | 25 (proved) | 0 | agree | 161.5 | 0 |
| 9 | `(19, 10, 5, 1, 1)` | `(10, 5, 1, 1)` | 17 | δ<δ_close=12: δ<= 9 of ladder | 41 | 91 | 24190 | 2 | 9163 | sparse | 41 (proved) | 41 (proved) | 41 (proved) | 0 | agree | 233.8 | 0 |
| 9 | `(18, 8, 8, 1, 1)` | `(8, 8, 1, 1)` | 18 | δ<δ_close=11: δ<= 9 of ladder | 12 | 32 | 49071 | 4 | 9398 | sparse | 12 (proved) | 12 (proved) | 12 (proved) | 0 | agree | 44.8 | 0 |
| 9 | `(17, 13, 2, 2, 2)` | `(13, 2, 2, 2)` | 19 | δ<δ_close=16: δ<= 9 of ladder | 16 | 49 | 44152 | 6 | 9442 | sparse | 16 (proved) | 16 (proved) | 16 (proved) | 0 | agree | 134.4 | 0 |
| 9 | `(23, 6, 3, 2, 2)` | `(6, 3, 2, 2)` | 13 | δ>=δ_close=9: whole ladder (a_δ = a_∞) | 12 | 46 | 18022 | 2 | 9903 | sparse | 12 (proved) | 12 (proved) | 12 (proved) | 0 | agree | 40.4 | 0 |
| 9 | `(22, 7, 3, 3, 1)` | `(7, 3, 3, 1)` | 14 | δ>=δ_close=9: whole ladder (a_δ = a_∞) | 11 | 39 | 20951 | 2 | 9939 | sparse | 11 (proved) | 11 (proved) | 11 (proved) | 0 | agree | 41.2 | 0 |
| 9 | `(16, 14, 2, 2, 2)` | `(14, 2, 2, 2)` | 20 | δ<δ_close=17: δ<= 9 of ladder | 16 | 32 | 47139 | 6 | 10089 | sparse | 16 (proved) | 16 (proved) | 16 (proved) | 0 | agree | 154.3 | 0 |
| 9 | `(22, 5, 5, 2, 2)` | `(5, 5, 2, 2)` | 14 | δ>=δ_close=9: whole ladder (a_δ = a_∞) | 5 | 31 | 41357 | 4 | 10869 | sparse | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 41.7 | 0 |
| 9 | `(18, 11, 5, 1, 1)` | `(11, 5, 1, 1)` | 18 | δ<δ_close=13: δ<= 9 of ladder | 48 | 94 | 29148 | 2 | 11096 | sparse | 48 (proved) | 48 (proved) | 48 (proved) | 0 | agree | 309.0 | 0 |
| 9 | `(14, 14, 6, 1, 1)` | `(14, 6, 1, 1)` | 22 | δ<δ_close=16: δ<= 9 of ladder | 9 | 22 | 58246 | 4 | 11173 | sparse | 9 (proved) | 9 (proved) | 9 (proved) | 0 | agree | 62.2 | 0 |
| 9 | `(22, 4, 4, 4, 2)` | `(4, 4, 4, 2)` | 14 | δ>=δ_close=9: whole ladder (a_δ = a_∞) | 10 | 22 | 64127 | 6 | 11620 | sparse | 10 (proved) | 10 (proved) | 10 (proved) | 0 | agree | 124.1 | 0 |
| 9 | `(23, 6, 4, 2, 1)` | `(6, 4, 2, 1)` | 13 | δ>=δ_close=9: whole ladder (a_δ = a_∞) | 20 | 72 | 11637 | 1 | 11637 | sparse | 20 (proved) | 20 (proved) | 20 (proved) | 0 | agree | 66.2 | 0 |
| 9 | `(19, 9, 6, 1, 1)` | `(9, 6, 1, 1)` | 17 | δ<δ_close=11: δ<= 9 of ladder | 44 | 91 | 31048 | 2 | 11834 | sparse | 44 (proved) | 44 (proved) | 44 (proved) | 0 | agree | 409.1 | 0 |
| 9 | `(22, 8, 3, 2, 1)` | `(8, 3, 2, 1)` | 14 | δ<δ_close=10: δ<= 9 of ladder | 24 | 82 | 12296 | 1 | 12296 | sparse | 24 (proved) | 24 (proved) | — | 0 | agree | 43.6 | 0 |
| 9 | `(23, 5, 4, 2, 2)` | `(5, 4, 2, 2)` | 13 | δ>=δ_close=9: whole ladder (a_δ = a_∞) | 11 | 42 | 22539 | 2 | 12358 | sparse | 11 (proved) | 11 (proved) | — | 0 | agree | 41.8 | 0 |
| 9 | `(23, 5, 3, 3, 2)` | `(5, 3, 3, 2)` | 13 | δ>=δ_close=7: whole ladder (a_δ = a_∞) | 1 | 10 | 26643 | 2 | 12643 | sparse | 1 (proved) | 1 (proved) | — | 0 | agree | 26.7 | 0 |
| 9 | `(17, 12, 5, 1, 1)` | `(12, 5, 1, 1)` | 19 | δ<δ_close=14: δ<= 9 of ladder | 43 | 83 | 33483 | 2 | 12785 | sparse | 43 (proved) | 43 (proved) | — | 0 | agree | 69.5 | 0 |
| 9 | `(19, 8, 7, 1, 1)` | `(8, 7, 1, 1)` | 17 | δ<δ_close=11: δ<= 9 of ladder | 29 | 60 | 35068 | 2 | 13419 | sparse | 29 (proved) | 29 (proved) | — | 0 | agree | 275.0 | 0 |
| 9 | `(16, 13, 5, 1, 1)` | `(13, 5, 1, 1)` | 20 | δ<δ_close=15: δ<= 9 of ladder | 36 | 64 | 36700 | 2 | 14046 | sparse | 36 (proved) | 36 (proved) | — | 0 | agree | 112.3 | 0 |
| 9 | `(21, 8, 3, 3, 1)` | `(8, 3, 3, 1)` | 15 | δ<δ_close=10: δ<= 9 of ladder | 17 | 58 | 30002 | 2 | 14272 | sparse | 17 (proved) | 17 (proved) | — | 0 | agree | 56.6 | 0 |
| 9 | `(15, 14, 5, 1, 1)` | `(14, 5, 1, 1)` | 21 | δ<δ_close=16: δ<= 9 of ladder | 19 | 34 | 38413 | 2 | 14717 | sparse | 19 (proved) | 19 (proved) | — | 0 | agree | 95.9 | 0 |
| 9 | `(22, 7, 3, 2, 2)` | `(7, 3, 2, 2)` | 14 | δ<δ_close=10: δ<= 9 of ladder | 18 | 71 | 27600 | 2 | 15088 | sparse | 18 (proved) | 18 (proved) | — | 0 | agree | 61.8 | 0 |
| 9 | `(22, 5, 5, 3, 1)` | `(5, 5, 3, 1)` | 14 | δ>=δ_close=9: whole ladder (a_δ = a_∞) | 10 | 31 | 31332 | 2 | 15350 | sparse | 10 (proved) | 10 (proved) | — | 0 | agree | 55.9 | 0 |
| 9 | `(23, 4, 4, 3, 2)` | `(4, 4, 3, 2)` | 13 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 4 | 16 | 30386 | 2 | 15664 | sparse | 4 (proved) | 4 (proved) | — | 0 | agree | 61.6 | 0 |
| 9 | `(20, 4, 4, 4, 4)` | `(4, 4, 4, 4)` | 16 | δ<δ_close=10: δ<= 9 of ladder | 9 | 13 | 353074 | 24 | 16732 | sparse | 9 (proved) | 8 (proved) | — | -1 | agree | 535.1 | 0 |
| 9 | `(23, 5, 4, 3, 1)` | `(5, 4, 3, 1)` | 13 | δ>=δ_close=8: whole ladder (a_δ = a_∞) | 10 | 37 | 17133 | 1 | 17133 | sparse | 10 (proved) | 10 (proved) | — | 0 | agree | 60.5 | 0 |
| 9 | `(15, 15, 3, 2, 1)` | `(15, 3, 2, 1)` | 21 | δ<δ_close=17: δ<= 9 of ladder | 9 | 21 | 36314 | 2 | 18062 | sparse | 9 (proved) | 9 (proved) | — | 0 | agree | 89.2 | 0 |
| 9 | `(20, 5, 5, 5, 1)` | `(5, 5, 5, 1)` | 16 | δ>=δ_close=9: whole ladder (a_δ = a_∞) | 3 | 9 | 122467 | 6 | 19514 | sparse | 3 (proved) | 3 (proved) | — | 0 | agree | 235.0 | 0 |
| 9 | `(13, 13, 8, 1, 1)` | `(13, 8, 1, 1)` | 23 | δ<δ_close=16: δ<= 9 of ladder | 19 | 17 | 101838 | 4 | 20099 | sparse | 19 (proved) | 15 (proved) | — | -4 | agree | 459.2 | 0 |

## Closing cells — one determinant-side rank per tail, the tail settled in every degree

`(λ_close, δ_close)` is the first rung of the tail's ladder with `a = a_∞ = a_t` (proved stable value).  `mult_det = a` there
gives `i_det = 0` at every rung of the ladder (downward by monotonicity, upward by stability), hence `D ≤ 0` at every
degree: the tail is **closed**.  `i_red(∞) = a − mult_red` at the closing cell is the stable reducible-ideal dimension;
`i_red = 0` there forces `i_red = 0` on the whole ladder (so `D = i_det = 0` everywhere on it).

| tail ρ | t | δ_close | λ_close | a_∞ | h_pad | N_S | Stab | n_chi | route | mult_det | mult_red(★) | mult_red(pts) | i_red(∞) | census rungs settled (δ) | status | s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `(2, 2, 2, 2)` | 8 | 5 | `(12, 2, 2, 2, 2)` | 1 | 2 | 553 | 24 | 56 | dense | 1 (proved) | 1 (proved) | 1 (proved) | 0 | [6, 7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 0.1 |
| `(7, 2, 1, 1)` | 11 | 5 | `(9, 7, 2, 1, 1)` | 1 | 2 | 621 | 2 | 218 | dense | 1 (proved) | 1 (proved) | 1 (proved) | 0 | [6, 7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 0.1 |
| `(5, 3, 1, 1)` | 10 | 5 | `(10, 5, 3, 1, 1)` | 1 | 4 | 774 | 2 | 276 | dense | 1 (proved) | 1 (proved) | 1 (proved) | 0 | [6, 7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 0.1 |
| `(3, 2, 2, 2)` | 9 | 6 | `(15, 3, 2, 2, 2)` | 1 | 4 | 1280 | 6 | 304 | dense | 1 (proved) | 1 (proved) | 1 (proved) | 0 | [6, 7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 0.4 |
| `(8, 2, 1, 1)` | 12 | 6 | `(12, 8, 2, 1, 1)` | 1 | 4 | 1121 | 2 | 391 | dense | 1 (proved) | 1 (proved) | 1 (proved) | 0 | [6, 7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 0.2 |
| `(4, 2, 2, 1)` | 9 | 5 | `(11, 4, 2, 2, 1)` | 1 | 5 | 705 | 2 | 399 | dense | 1 (proved) | 1 (proved) | 1 (proved) | 0 | [6, 7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 0.3 |
| `(6, 3, 1, 1)` | 11 | 6 | `(13, 6, 3, 1, 1)` | 1 | 7 | 1463 | 2 | 524 | dense | 1 (proved) | 1 (proved) | 1 (proved) | 0 | [6, 7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 0.4 |
| `(9, 2, 1, 1)` | 13 | 7 | `(15, 9, 2, 1, 1)` | 2 | 6 | 1761 | 2 | 622 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | [6, 7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 0.5 |
| `(5, 4, 1, 1)` | 11 | 6 | `(13, 5, 4, 1, 1)` | 2 | 9 | 1824 | 2 | 658 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | [6, 7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 0.5 |
| `(5, 2, 2, 1)` | 10 | 6 | `(14, 5, 2, 2, 1)` | 2 | 10 | 1337 | 2 | 752 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | [6, 7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 1.0 |
| `(7, 3, 1, 1)` | 12 | 7 | `(16, 7, 3, 1, 1)` | 4 | 13 | 2414 | 2 | 870 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | [6, 7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 1.0 |
| `(6, 2, 2, 1)` | 11 | 7 | `(17, 6, 2, 2, 1)` | 4 | 17 | 2257 | 2 | 1267 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | [6, 7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 0.9 |
| `(12, 2, 1, 1)` | 16 | 10 | `(24, 12, 2, 1, 1)` | 4 | 15 | 4651 | 2 | 1642 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | [8, 9, 10] | tail closed (D <= 0 in every degree) | 2.2 |
| `(4, 3, 2, 1)` | 10 | 6 | `(14, 4, 3, 2, 1)` | 1 | 8 | 1785 | 1 | 1785 | dense | 1 (proved) | 1 (proved) | 1 (proved) | 0 | [6, 7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 1.9 |
| `(13, 2, 1, 1)` | 17 | 11 | `(27, 13, 2, 1, 1)` | 6 | 19 | 5977 | 2 | 2122 | dense | 6 (proved) | 6 (proved) | 6 (proved) | 0 | [8, 9, 10] | tail closed (D <= 0 in every degree) | 3.9 |
| `(7, 2, 2, 2)` | 13 | 10 | `(27, 7, 2, 2, 2)` | 11 | 38 | 11557 | 6 | 2591 | dense | 11 (proved) | 11 (proved) | 11 (proved) | 0 | [6, 7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 10.4 |
| `(10, 3, 1, 1)` | 15 | 10 | `(25, 10, 3, 1, 1)` | 11 | 35 | 7282 | 2 | 2647 | dense | 11 (proved) | 11 (proved) | 11 (proved) | 0 | [7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 7.3 |
| `(14, 2, 1, 1)` | 18 | 12 | `(30, 14, 2, 1, 1)` | 6 | 23 | 7522 | 2 | 2666 | dense | 6 (proved) | 6 (proved) | 6 (proved) | 0 | [9, 10] | tail closed (D <= 0 in every degree) | 6.7 |
| `(15, 2, 1, 1)` | 19 | 13 | `(33, 15, 2, 1, 1)` | 9 | 27 | 9284 | 2 | 3304 | dense | 9 (proved) | 9 (proved) | 9 (proved) | 0 | [9, 10] | tail closed (D <= 0 in every degree) | 11.4 |
| `(11, 3, 1, 1)` | 16 | 11 | `(28, 11, 3, 1, 1)` | 16 | 45 | 9717 | 2 | 3543 | dense | 16 (proved) | 16 (proved) | 16 (proved) | 0 | [7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 15.5 |
| `(8, 2, 2, 2)` | 14 | 11 | `(30, 8, 2, 2, 2)` | 19 | 54 | 17076 | 6 | 3815 | dense | 19 (proved) | 19 (proved) | 19 (proved) | 0 | [6, 7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 27.6 |
| `(16, 2, 1, 1)` | 20 | 14 | `(36, 16, 2, 1, 1)` | 9 | 32 | 11298 | 2 | 4016 | sparse | 9 (proved) | 9 (proved) | 9 (proved) | 0 | [10] | tail closed (D <= 0 in every degree) | 6.1 |
| `(9, 2, 2, 1)` | 14 | 10 | `(26, 9, 2, 2, 1)` | 14 | 47 | 7259 | 2 | 4045 | sparse | 14 (proved) | 14 (proved) | 14 (proved) | 0 | [6, 7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 8.0 |
| `(9, 4, 1, 1)` | 15 | 10 | `(25, 9, 4, 1, 1)` | 22 | 63 | 11437 | 2 | 4209 | sparse | 22 (proved) | 22 (proved) | 22 (proved) | 0 | [6, 7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 9.1 |
| `(12, 3, 1, 1)` | 17 | 12 | `(31, 12, 3, 1, 1)` | 19 | 55 | 12646 | 2 | 4619 | sparse | 19 (proved) | 19 (proved) | 19 (proved) | 0 | [8, 9, 10] | tail closed (D <= 0 in every degree) | 10.9 |
| `(17, 2, 1, 1)` | 21 | 15 | `(39, 17, 2, 1, 1)` | 12 | 37 | 13557 | 2 | 4835 | sparse | 12 (proved) | 12 (proved) | 12 (proved) | 0 | [10] | tail closed (D <= 0 in every degree) | 10.1 |
| `(7, 7, 1, 1)` | 16 | 10 | `(24, 7, 7, 1, 1)` | 19 | 32 | 27232 | 4 | 5180 | sparse | 19 (proved) | 19 (proved) | 19 (proved) | 0 | [6, 7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 14.7 |
| `(9, 2, 2, 2)` | 15 | 12 | `(33, 9, 2, 2, 2)` | 23 | 71 | 24179 | 6 | 5343 | sparse | 23 (proved) | 23 (proved) | 23 (proved) | 0 | [7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 44.4 |
| `(10, 2, 2, 1)` | 15 | 11 | `(29, 10, 2, 2, 1)` | 19 | 61 | 9884 | 2 | 5500 | sparse | 19 (proved) | 19 (proved) | 19 (proved) | 0 | [7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 15.0 |
| `(8, 5, 1, 1)` | 15 | 10 | `(25, 8, 5, 1, 1)` | 23 | 62 | 15189 | 2 | 5651 | sparse | 23 (proved) | 23 (proved) | 23 (proved) | 0 | [6, 7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 28.2 |
| `(10, 4, 1, 1)` | 16 | 11 | `(28, 10, 4, 1, 1)` | 28 | 85 | 15838 | 2 | 5834 | sparse | 28 (proved) | 28 (proved) | 28 (proved) | 0 | [7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 19.6 |
| `(13, 3, 1, 1)` | 18 | 13 | `(34, 13, 3, 1, 1)` | 25 | 68 | 16102 | 2 | 5894 | sparse | 25 (proved) | 25 (proved) | 25 (proved) | 0 | [8, 9, 10] | tail closed (D <= 0 in every degree) | 19.8 |
| `(11, 2, 2, 1)` | 16 | 12 | `(32, 11, 2, 2, 1)` | 24 | 76 | 13077 | 2 | 7265 | sparse | 24 (proved) | 24 (proved) | 24 (proved) | 0 | [7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 29.7 |
| `(10, 2, 2, 2)` | 16 | 13 | `(36, 10, 2, 2, 2)` | 35 | 91 | 33225 | 6 | 7324 | sparse | 35 (proved) | 35 (proved) | 35 (proved) | 0 | [7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 104.2 |
| `(14, 3, 1, 1)` | 19 | 14 | `(37, 14, 3, 1, 1)` | 30 | 81 | 20138 | 2 | 7382 | sparse | 30 (proved) | 30 (proved) | 30 (proved) | 0 | [9, 10] | tail closed (D <= 0 in every degree) | 34.0 |
| `(11, 4, 1, 1)` | 17 | 12 | `(31, 11, 4, 1, 1)` | 43 | 110 | 21240 | 2 | 7866 | sparse | 43 (proved) | 43 (proved) | 43 (proved) | 0 | [7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 79.1 |
| `(9, 5, 1, 1)` | 16 | 11 | `(28, 9, 5, 1, 1)` | 39 | 92 | 21946 | 2 | 8205 | sparse | 39 (proved) | 39 (proved) | 39 (proved) | 0 | [7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 182.3 |
| `(15, 3, 1, 1)` | 20 | 15 | `(40, 15, 3, 1, 1)` | 37 | 95 | 24796 | 2 | 9104 | sparse | 37 (proved) | 37 (proved) | 37 (proved) | 0 | [9, 10] | tail closed (D <= 0 in every degree) | 58.6 |
| `(12, 2, 2, 1)` | 17 | 13 | `(35, 12, 2, 2, 1)` | 31 | 93 | 16919 | 2 | 9390 | sparse | 31 (proved) | 31 (proved) | 31 (proved) | 0 | [8, 9, 10] | tail closed (D <= 0 in every degree) | 63.3 |
| `(8, 6, 1, 1)` | 16 | 10 | `(24, 8, 6, 1, 1)` | 28 | 76 | 25572 | 2 | 9610 | sparse | 28 (proved) | 28 (proved) | 28 (proved) | 0 | [7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 208.5 |
| `(11, 2, 2, 2)` | 17 | 14 | `(39, 11, 2, 2, 2)` | 40 | 113 | 44317 | 6 | 9694 | sparse | 40 (proved) | 40 (proved) | 40 (proved) | 0 | [8, 9, 10] | tail closed (D <= 0 in every degree) | 199.5 |
| `(12, 4, 1, 1)` | 18 | 13 | `(34, 12, 4, 1, 1)` | 51 | 137 | 27816 | 2 | 10308 | sparse | 51 (proved) | 51 (proved) | 51 (proved) | 0 | [8, 9, 10] | tail closed (D <= 0 in every degree) | 424.9 |
| `(16, 3, 1, 1)` | 21 | 16 | `(43, 16, 3, 1, 1)` | 43 | 111 | 30128 | 2 | 11074 | sparse | 43 (proved) | 43 (proved) | 43 (proved) | 0 | [10] | tail closed (D <= 0 in every degree) | 187.3 |
| `(10, 5, 1, 1)` | 17 | 12 | `(31, 10, 5, 1, 1)` | 56 | 130 | 30586 | 2 | 11472 | sparse | 56 (proved) | 56 (proved) | 56 (proved) | 0 | [7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 501.5 |
| `(13, 2, 2, 1)` | 18 | 14 | `(38, 13, 2, 2, 1)` | 38 | 111 | 21453 | 2 | 11893 | sparse | 38 (proved) | 38 (proved) | 38 (proved) | 0 | [8, 9, 10] | tail closed (D <= 0 in every degree) | 202.9 |
| `(8, 8, 1, 1)` | 18 | 11 | `(26, 8, 8, 1, 1)` | 19 | 51 | 63647 | 4 | 12100 | sparse | 19 (proved) | 19 (proved) | — | 0 | [8, 9, 10] | tail closed (D <= 0 in every degree) | 47.2 |
| `(12, 2, 2, 2)` | 18 | 15 | `(42, 12, 2, 2, 2)` | 56 | 139 | 57864 | 6 | 12641 | sparse | 56 (proved) | 56 (proved) | — | 0 | [8, 9, 10] | tail closed (D <= 0 in every degree) | 245.9 |
| `(8, 3, 2, 1)` | 14 | 10 | `(26, 8, 3, 2, 1)` | 25 | 85 | 12810 | 1 | 12810 | sparse | 25 (proved) | 25 (proved) | — | 0 | [6, 7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 94.0 |
| `(17, 3, 1, 1)` | 22 | 17 | `(46, 17, 3, 1, 1)` | 51 | 128 | 36172 | 2 | 13312 | sparse | 51 (proved) | 51 (proved) | — | 0 | [10] | tail closed (D <= 0 in every degree) | 165.9 |
| `(9, 6, 1, 1)` | 17 | 11 | `(27, 9, 6, 1, 1)` | 56 | 122 | 37691 | 2 | 14251 | sparse | 56 (proved) | 56 (proved) | — | 0 | [7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 359.0 |
| `(14, 2, 2, 1)` | 19 | 15 | `(41, 14, 2, 2, 1)` | 46 | 132 | 26750 | 2 | 14818 | sparse | 46 (proved) | 46 (proved) | — | 0 | [9, 10] | tail closed (D <= 0 in every degree) | 193.1 |
| `(8, 3, 3, 1)` | 15 | 10 | `(25, 8, 3, 3, 1)` | 18 | 61 | 31812 | 2 | 15112 | sparse | 18 (proved) | 18 (proved) | — | 0 | [6, 7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 145.3 |
| `(7, 3, 2, 2)` | 14 | 10 | `(26, 7, 3, 2, 2)` | 19 | 73 | 28512 | 2 | 15612 | sparse | 19 (proved) | 19 (proved) | — | 0 | [6, 7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 81.7 |
| `(8, 7, 1, 1)` | 17 | 11 | `(27, 8, 7, 1, 1)` | 37 | 78 | 42368 | 2 | 16079 | sparse | 37 (proved) | 37 (proved) | — | 0 | [7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 617.5 |
| `(4, 4, 4, 4)` | 16 | 10 | `(24, 4, 4, 4, 4)` | 10 | 14 | 375953 | 24 | 17896 | sparse | 10 (proved) | 9 (proved) | — | 1 | [6, 7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 482.6 |
| `(5, 4, 4, 1)` | 14 | 9 | `(22, 5, 4, 4, 1)` | 12 | 39 | 35768 | 2 | 18396 | sparse | 12 (proved) | 12 (proved) | — | 0 | [6, 7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 222.2 |
| `(7, 3, 3, 3)` | 16 | 8 | `(16, 7, 3, 3, 3)` | 3 | 8 | 146934 | 6 | 21991 | sparse | 3 (proved) | 3 (proved) | — | 0 | [7, 8, 9, 10] | tail closed (D <= 0 in every degree) | 506.7 |
