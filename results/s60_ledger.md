# Session 60 — ledger: the balanced length-5 complement, both sides

One row per measured cell (`n = 4`, `r = 5`).  `a` = ambient multiplicity (Weyl alternation = s54 plethysm);
`h_pad` = normalisation bound (`mult_red <= h_pad`, proved).  `mult_det` at `a+8` det_4 pencils; `mult_red(★)`
point-free by Theorem (★) on the red columns of `E`; `mult_red(pts)` at `a+8` reducible `ℓ·c` points (—: not run,
(★) alone above `n_chi = 20000` on the sparse route).  Tags: *proved* = nullity 0 at both primes (or, on the
reducible side, nullity certified `<= a − h_pad` at both primes, meeting the theorem's `>=`); *exact* = explicit
kernel at both primes (dense route); *measured* = nullity exhibited at both primes; *bounded* = extraction budget
reached, the value is an upper bound on `mult`.  `D = mult_red − mult_det`; a refutation of `R_5 ⊆ D_5` is `D > 0`.
Route: dense = exact flint kernel (`n_chi <= 4000`), sparse = session-45 Wiedemann certificates.

| δ | λ | a | h_pad | N_S | Stab | n_chi | route | mult_det | mult_red(★) | mult_red(pts) | D | primes | s | certs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | `(12, 5, 5, 1, 1)` | 2 | 5 | 2795 | 4 | 524 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 0.6 | 4 |
| 6 | `(9, 9, 4, 1, 1)` | 2 | 4 | 3852 | 4 | 736 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 1.4 | 2 |
| 6 | `(13, 5, 2, 2, 2)` | 2 | 12 | 3672 | 6 | 825 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 3.3 | 2 |
| 6 | `(12, 6, 4, 1, 1)` | 2 | 12 | 2553 | 2 | 927 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 1.1 | 4 |
| 6 | `(12, 6, 2, 2, 2)` | 4 | 16 | 5194 | 6 | 1162 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 7.6 | 2 |
| 6 | `(11, 7, 4, 1, 1)` | 4 | 14 | 3209 | 2 | 1187 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 2.3 | 2 |
| 6 | `(8, 7, 7, 1, 1)` | 2 | 2 | 6718 | 4 | 1300 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 5.7 | 2 |
| 6 | `(10, 8, 4, 1, 1)` | 2 | 10 | 3686 | 2 | 1362 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 3.0 | 2 |
| 6 | `(11, 6, 5, 1, 1)` | 2 | 8 | 3818 | 2 | 1423 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 3.3 | 2 |
| 6 | `(11, 7, 2, 2, 2)` | 2 | 14 | 6563 | 6 | 1435 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 13.1 | 2 |
| 6 | `(11, 8, 2, 2, 1)` | 3 | 13 | 2919 | 2 | 1619 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 7.1 | 4 |
| 6 | `(10, 8, 2, 2, 2)` | 3 | 11 | 7576 | 6 | 1661 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 20.5 | 2 |
| 6 | `(13, 4, 4, 2, 1)` | 2 | 12 | 3199 | 2 | 1667 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 8.6 | 2 |
| 6 | `(10, 7, 5, 1, 1)` | 4 | 10 | 4672 | 2 | 1757 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 6.0 | 2 |
| 6 | `(10, 9, 2, 2, 1)` | 2 | 7 | 3176 | 2 | 1759 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 9.1 | 2 |
| 6 | `(9, 8, 5, 1, 1)` | 2 | 6 | 5159 | 2 | 1947 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 7.1 | 2 |
| 6 | `(11, 4, 4, 4, 1)` | 2 | 7 | 11574 | 6 | 2113 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 4.7 | 2 |
| 6 | `(9, 7, 6, 1, 1)` | 2 | 5 | 5967 | 2 | 2262 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 10.3 | 2 |
| 6 | `(12, 4, 4, 2, 2)` | 3 | 10 | 8803 | 4 | 2561 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 6.1 | 2 |
| 6 | `(13, 4, 3, 2, 2)` | 1 | 8 | 4940 | 2 | 2727 | dense | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 5.9 | 2 |
| 6 | `(12, 5, 3, 3, 1)` | 1 | 7 | 5837 | 2 | 2761 | dense | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 6.2 | 2 |
| 6 | `(13, 5, 3, 2, 1)` | 3 | 16 | 2800 | 1 | 2800 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 5.8 | 4 |
| 6 | `(9, 9, 3, 2, 1)` | 1 | 6 | 5994 | 2 | 2959 | dense | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 7.4 | 2 |
| 6 | `(12, 4, 4, 3, 1)` | 1 | 9 | 6675 | 2 | 3452 | dense | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 10.7 | 2 |
| 6 | `(11, 5, 5, 2, 1)` | 2 | 12 | 7461 | 2 | 3637 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 12.6 | 2 |
| 6 | `(11, 6, 3, 3, 1)` | 1 | 9 | 8035 | 2 | 3813 | dense | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 13.4 | 2 |
| 6 | `(12, 6, 3, 2, 1)` | 4 | 22 | 3942 | 1 | 3942 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 14.4 | 2 |
| 6 | `(12, 5, 3, 2, 2)` | 1 | 14 | 7685 | 2 | 4209 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 5.3 | 0 |
| 6 | `(8, 4, 4, 4, 4)` | 2 | 1 | 94675 | 24 | 4562 | sparse | 2 (proved) | 1 (proved) | 1 (proved) | -1 | agree | 21.2 | 0 |
| 6 | `(10, 7, 3, 3, 1)` | 2 | 10 | 9882 | 2 | 4702 | sparse | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 7.4 | 0 |
| 6 | `(12, 5, 4, 2, 1)` | 5 | 24 | 4942 | 1 | 4942 | sparse | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 8.0 | 0 |
| 6 | `(11, 7, 3, 2, 1)` | 5 | 24 | 4978 | 1 | 4978 | sparse | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 8.2 | 0 |
| 6 | `(9, 8, 3, 3, 1)` | 1 | 6 | 10939 | 2 | 5209 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 9.1 | 0 |
| 6 | `(10, 4, 4, 4, 2)` | 3 | 6 | 30870 | 6 | 5588 | sparse | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 27.3 | 0 |
| 6 | `(10, 8, 3, 2, 1)` | 4 | 18 | 5731 | 1 | 5731 | sparse | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 10.9 | 0 |
| 6 | `(11, 6, 3, 2, 2)` | 3 | 19 | 10607 | 2 | 5785 | sparse | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 13.7 | 0 |
| 6 | `(8, 8, 4, 2, 2)` | 3 | 8 | 22475 | 4 | 6247 | sparse | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 20.4 | 0 |
| 6 | `(8, 8, 5, 2, 1)` | 2 | 8 | 12445 | 2 | 6294 | sparse | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 14.8 | 0 |
| 6 | `(9, 6, 6, 2, 1)` | 2 | 8 | 12788 | 2 | 6501 | sparse | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 21.8 | 0 |
| 6 | `(11, 6, 4, 2, 1)` | 7 | 32 | 6789 | 1 | 6789 | sparse | 7 (proved) | 7 (proved) | 7 (proved) | 0 | agree | 16.8 | 0 |
| 6 | `(10, 7, 3, 2, 2)` | 2 | 17 | 13065 | 2 | 7102 | sparse | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 17.0 | 0 |
| 6 | `(11, 5, 4, 2, 2)` | 3 | 18 | 13363 | 2 | 7271 | sparse | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 22.7 | 0 |
| 6 | `(10, 5, 5, 3, 1)` | 2 | 9 | 14912 | 2 | 7306 | sparse | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 19.1 | 0 |
| 6 | `(9, 8, 3, 2, 2)` | 2 | 11 | 14477 | 2 | 7860 | sparse | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 21.0 | 0 |
| 6 | `(10, 7, 4, 2, 1)` | 7 | 31 | 8337 | 1 | 8337 | sparse | 7 (proved) | 7 (proved) | 7 (proved) | 0 | agree | 26.3 | 0 |
| 6 | `(8, 8, 4, 3, 1)` | 1 | 7 | 16933 | 2 | 8553 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 27.1 | 0 |
| 6 | `(8, 6, 6, 2, 2)` | 3 | 6 | 31356 | 4 | 8687 | sparse | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 42.7 | 0 |
| 6 | `(10, 5, 4, 4, 1)` | 3 | 12 | 17075 | 2 | 8773 | sparse | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 28.2 | 0 |
| 6 | `(9, 8, 4, 2, 1)` | 5 | 19 | 9224 | 1 | 9224 | sparse | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 31.0 | 0 |
| 6 | `(11, 4, 4, 3, 2)` | 1 | 7 | 18161 | 2 | 9341 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 38.1 | 0 |
| 6 | `(10, 6, 4, 2, 2)` | 6 | 24 | 17932 | 2 | 9743 | sparse | 6 (proved) | 6 (proved) | 6 (proved) | 0 | agree | 36.7 | 0 |
| 6 | `(10, 6, 5, 2, 1)` | 5 | 20 | 9964 | 1 | 9964 | sparse | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 35.8 | 0 |
| 6 | `(11, 5, 4, 3, 1)` | 4 | 18 | 10113 | 1 | 10113 | sparse | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 34.9 | 0 |
| 6 | `(9, 4, 4, 4, 3)` | 1 | 2 | 60305 | 6 | 10719 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 108.3 | 0 |
| 6 | `(9, 6, 4, 4, 1)` | 4 | 13 | 21982 | 2 | 11280 | sparse | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 49.5 | 0 |
| 6 | `(9, 7, 4, 2, 2)` | 2 | 18 | 21215 | 2 | 11473 | sparse | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 46.8 | 0 |
| 6 | `(9, 7, 5, 2, 1)` | 5 | 19 | 11766 | 1 | 11766 | sparse | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 52.1 | 0 |
| 6 | `(9, 5, 5, 4, 1)` | 1 | 5 | 24258 | 2 | 11908 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 52.3 | 0 |
| 6 | `(8, 6, 6, 3, 1)` | 1 | 4 | 23592 | 2 | 11955 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 79.0 | 0 |
| 6 | `(9, 7, 3, 3, 2)` | 1 | 5 | 25246 | 2 | 12092 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 50.9 | 0 |
| 6 | `(6, 6, 4, 4, 4)` | 1 | 1 | 133366 | 12 | 12096 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 152.2 | 0 |
| 6 | `(7, 7, 6, 3, 1)` | 1 | 3 | 25213 | 2 | 12473 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 60.1 | 0 |
| 6 | `(8, 7, 4, 4, 1)` | 2 | 8 | 24857 | 2 | 12743 | sparse | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 87.8 | 0 |
| 6 | `(6, 6, 6, 4, 2)` | 1 | 1 | 76288 | 6 | 13194 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 189.8 | 0 |
| 6 | `(10, 6, 4, 3, 1)` | 4 | 21 | 13533 | 1 | 13533 | sparse | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 64.5 | 0 |
| 6 | `(9, 6, 5, 2, 2)` | 3 | 14 | 25456 | 2 | 13733 | sparse | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 70.3 | 0 |
| 6 | `(8, 7, 6, 2, 1)` | 2 | 8 | 14436 | 1 | 14436 | sparse | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 73.2 | 0 |
| 6 | `(8, 7, 5, 2, 2)` | 1 | 9 | 28802 | 2 | 15510 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 86.5 | 0 |
| 6 | `(7, 7, 5, 4, 1)` | 1 | 3 | 31917 | 2 | 15798 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 96.2 | 0 |
| 6 | `(9, 7, 4, 3, 1)` | 5 | 19 | 16005 | 1 | 16005 | sparse | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 98.2 | 0 |
| 6 | `(7, 7, 4, 3, 3)` | 1 | 1 | 69495 | 4 | 16785 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 163.2 | 0 |
| 6 | `(8, 5, 5, 3, 3)` | 1 | 1 | 71858 | 4 | 17270 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 180.0 | 0 |
| 6 | `(7, 6, 6, 4, 1)` | 1 | 2 | 34726 | 2 | 17578 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 121.1 | 0 |
| 6 | `(9, 5, 5, 3, 2)` | 1 | 5 | 38401 | 2 | 18877 | sparse | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 131.6 | 0 |
| 6 | `(9, 6, 5, 3, 1)` | 3 | 12 | 19188 | 1 | 19188 | sparse | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 135.2 | 0 |
| 6 | `(8, 7, 5, 3, 1)` | 4 | 10 | 21694 | 1 | 21694 | sparse | 4 (proved) | 4 (proved) | — | 0 | agree | 112.5 | 0 |
| 6 | `(9, 5, 4, 4, 2)` | 2 | 9 | 44031 | 2 | 22532 | sparse | 2 (proved) | 2 (proved) | — | 0 | agree | 195.8 | 0 |
| 6 | `(7, 7, 5, 3, 2)` | 1 | 3 | 50668 | 2 | 25101 | sparse | 1 (proved) | 1 (proved) | — | 0 | agree | 153.8 | 0 |
| 6 | `(10, 5, 4, 3, 2)` | 2 | 12 | 26921 | 1 | 26921 | sparse | 2 (proved) | 2 (proved) | — | 0 | agree | 153.9 | 0 |
| 6 | `(8, 6, 4, 4, 2)` | 4 | 9 | 54343 | 2 | 27828 | sparse | 4 (proved) | 4 (proved) | — | 0 | agree | 346.6 | 0 |
| 6 | `(7, 6, 6, 3, 2)` | 1 | 2 | 55158 | 2 | 27893 | sparse | 1 (proved) | 1 (proved) | — | 0 | agree | 352.2 | 0 |
| 6 | `(8, 6, 5, 4, 1)` | 2 | 6 | 29854 | 1 | 29854 | sparse | 2 (proved) | 2 (proved) | — | 0 | agree | 224.6 | 0 |
| 6 | `(9, 6, 4, 3, 2)` | 3 | 13 | 34756 | 1 | 34756 | sparse | 3 (proved) | 3 (proved) | — | 0 | agree | 282.3 | 0 |
| 6 | `(8, 7, 4, 3, 2)` | 2 | 9 | 39362 | 1 | 39362 | sparse | 2 (proved) | 2 (proved) | — | 0 | agree | 386.7 | 0 |
| 6 | `(8, 5, 4, 4, 3)` | 1 | 3 | 82457 | 2 | 42042 | sparse | 1 (proved) | 1 (proved) | — | 0 | agree | 768.9 | 0 |
| 6 | `(8, 6, 5, 3, 2)` | 1 | 6 | 47357 | 1 | 47357 | sparse | 1 (proved) | 1 (proved) | — | 0 | agree | 535.3 | 0 |
| 6 | `(7, 6, 4, 4, 3)` | 1 | 2 | 96185 | 2 | 49013 | sparse | 1 (proved) | 1 (proved) | — | 0 | agree | 1092.4 | 0 |
| 6 | `(7, 6, 5, 4, 2)` | 1 | 3 | 70027 | 1 | 70027 | sparse | 1 (proved) | 1 (proved) | — | 0 | agree | 1252.6 | 0 |
| 7 | `(18, 4, 2, 2, 2)` | 3 | 9 | 2565 | 6 | 606 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 1.5 | 4 |
| 7 | `(16, 5, 5, 1, 1)` | 3 | 7 | 3575 | 4 | 663 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 1.3 | 2 |
| 7 | `(17, 5, 2, 2, 2)` | 3 | 15 | 4306 | 6 | 978 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 1.1 | 2 |
| 7 | `(15, 8, 3, 1, 1)` | 4 | 15 | 3127 | 2 | 1137 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 2.2 | 2 |
| 7 | `(16, 6, 4, 1, 1)` | 3 | 17 | 3264 | 2 | 1177 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 2.0 | 2 |
| 7 | `(14, 9, 3, 1, 1)` | 5 | 15 | 3782 | 2 | 1386 | dense | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 3.4 | 2 |
| 7 | `(14, 6, 6, 1, 1)` | 1 | 9 | 7964 | 4 | 1471 | dense | 1 (proved) | 1 (proved) | 1 (proved) | 0 | agree | 1.6 | 2 |
| 7 | `(16, 6, 2, 2, 2)` | 7 | 23 | 6602 | 6 | 1486 | dense | 7 (proved) | 7 (proved) | 7 (proved) | 0 | agree | 2.8 | 2 |
| 7 | `(11, 11, 4, 1, 1)` | 4 | 7 | 7865 | 4 | 1502 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 3.0 | 2 |
| 7 | `(13, 10, 3, 1, 1)` | 4 | 12 | 4289 | 2 | 1578 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 2.1 | 2 |
| 7 | `(12, 11, 3, 1, 1)` | 3 | 7 | 4562 | 2 | 1683 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 2.1 | 2 |
| 8 | `(22, 4, 2, 2, 2)` | 3 | 9 | 2625 | 6 | 625 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 1.5 | 4 |
| 8 | `(20, 5, 5, 1, 1)` | 3 | 7 | 3946 | 4 | 726 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 1.6 | 2 |
| 8 | `(18, 10, 2, 1, 1)` | 2 | 9 | 2558 | 2 | 899 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 1.0 | 4 |
| 8 | `(20, 7, 3, 1, 1)` | 4 | 14 | 2688 | 2 | 962 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 1.1 | 4 |
| 8 | `(21, 5, 2, 2, 2)` | 4 | 16 | 4538 | 6 | 1040 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 1.3 | 2 |
| 8 | `(17, 11, 2, 1, 1)` | 3 | 9 | 2980 | 2 | 1060 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 1.5 | 4 |
| 8 | `(16, 12, 2, 1, 1)` | 2 | 7 | 3331 | 2 | 1182 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 2.2 | 2 |
| 8 | `(15, 13, 2, 1, 1)` | 2 | 5 | 3553 | 2 | 1271 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 2.5 | 2 |
| 8 | `(20, 6, 4, 1, 1)` | 3 | 18 | 3611 | 2 | 1293 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 2.6 | 2 |
| 8 | `(19, 8, 3, 1, 1)` | 5 | 19 | 3673 | 2 | 1327 | dense | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 3.0 | 2 |
| 8 | `(20, 6, 2, 2, 2)` | 8 | 26 | 7256 | 6 | 1647 | dense | 8 (proved) | 8 (proved) | 8 (proved) | 0 | agree | 3.8 | 2 |
| 9 | `(26, 4, 2, 2, 2)` | 3 | 9 | 2635 | 6 | 629 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 1.6 | 4 |
| 9 | `(24, 5, 5, 1, 1)` | 3 | 7 | 4080 | 4 | 747 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 1.6 | 2 |
| 9 | `(24, 7, 3, 1, 1)` | 4 | 14 | 2804 | 2 | 999 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 1.2 | 4 |
| 9 | `(22, 10, 2, 1, 1)` | 2 | 11 | 2885 | 2 | 1010 | dense | 2 (proved) | 2 (proved) | 2 (proved) | 0 | agree | 1.3 | 4 |
| 9 | `(25, 5, 2, 2, 2)` | 4 | 16 | 4598 | 6 | 1059 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 1.3 | 2 |
| 9 | `(21, 11, 2, 1, 1)` | 4 | 12 | 3510 | 2 | 1243 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 2.4 | 2 |
| 9 | `(24, 6, 4, 1, 1)` | 3 | 18 | 3742 | 2 | 1334 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 2.9 | 2 |
| 9 | `(23, 8, 3, 1, 1)` | 5 | 20 | 3948 | 2 | 1419 | dense | 5 (proved) | 5 (proved) | 5 (proved) | 0 | agree | 3.4 | 2 |
| 9 | `(20, 12, 2, 1, 1)` | 3 | 12 | 4120 | 2 | 1459 | dense | 3 (proved) | 3 (proved) | 3 (proved) | 0 | agree | 3.6 | 2 |
| 9 | `(19, 13, 2, 1, 1)` | 4 | 11 | 4653 | 2 | 1661 | dense | 4 (proved) | 4 (proved) | 4 (proved) | 0 | agree | 2.2 | 2 |
