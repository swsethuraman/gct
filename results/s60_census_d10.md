# Session 60 -- census of the balanced length-5 complement

`n = 4`, `r = 5`.  Complement of the cells session 54 measured (its dense route reached `nb <= 2500`).
`a` = plethysm (s54's census value, re-derived by the Weyl alternation and asserted equal);
`h_pad` = normalisation bound (`mult_red <= h_pad`, proved); `h_pad = 0` forces `mult_red = 0`, so
such a cell cannot refute `R_5 ⊆ D_5` and only its determinant side is a measurement ('dead').
`n_chi` is exact unless marked `~` (estimate `ceil(N_S/|Stab|)`).

| delta | cells `a>0` | measured by s54 | unmeasured | informative (`h_pad>=1`) | dead (`h_pad=0`) | sum `a` unmeasured | smallest `n_chi` unmeasured | largest `n_chi` |
|---|---|---|---|---|---|---|---|---|
| 10 | 1075 | 0 | 1075 | 1056 | 19 | 294154 | 66 at `(32, 2, 2, 2, 2)` | 301693666 at `(10, 9, 8, 7, 6)` |

## Per-degree cost bands (unmeasured cells, by `n_chi`)

| delta | `n_chi <= 3000` | `3000 < n_chi <= 20000` | `20000 < n_chi <= 100000` | `n_chi > 100000` |
|---|---|---|---|---|
| 10 | 36 | 81 | 116 | 842 |

## The twenty cheapest unmeasured informative cells overall (order key `n_chi^2 (a+30)`)

| delta | lam | a | h_pad | N_S | Stab | n_chi | key |
|---|---|---|---|---|---|---|---|
| 10 | `(32, 2, 2, 2, 2)` | 1 | 2 | 619 | 24 | 66 | 1.35e+05 |
| 10 | `(31, 3, 2, 2, 2)` | 1 | 4 | 1350 | 6 | 327 | 3.31e+06 |
| 10 | `(30, 5, 3, 1, 1)` | 1 | 5 | 1188 | 2 | 412 | 5.26e+06 |
| 10 | `(29, 7, 2, 1, 1)` | 1 | 5 | 1232 | 2 | 421 | 5.49e+06 |
| 10 | `(31, 4, 2, 2, 1)` | 1 | 6 | 901 | 2 | 516 | 8.25e+06 |
| 10 | `(28, 8, 2, 1, 1)` | 1 | 7 | 1741 | 2 | 596 | 1.1e+07 |
| 10 | `(30, 4, 2, 2, 2)` | 3 | 9 | 2636 | 6 | 630 | 1.31e+07 |
| 10 | `(29, 6, 3, 1, 1)` | 1 | 8 | 1893 | 2 | 664 | 1.37e+07 |
| 10 | `(28, 5, 5, 1, 1)` | 3 | 7 | 4117 | 4 | 752 | 1.87e+07 |
| 10 | `(27, 9, 2, 1, 1)` | 2 | 9 | 2353 | 2 | 819 | 2.15e+07 |
| 10 | `(29, 5, 4, 1, 1)` | 2 | 10 | 2330 | 2 | 823 | 2.17e+07 |
| 10 | `(30, 5, 2, 2, 1)` | 2 | 11 | 1537 | 2 | 872 | 2.43e+07 |
| 10 | `(28, 7, 3, 1, 1)` | 4 | 14 | 2840 | 2 | 1009 | 3.46e+07 |
| 10 | `(26, 10, 2, 1, 1)` | 2 | 12 | 3065 | 2 | 1069 | 3.66e+07 |
| 10 | `(29, 5, 2, 2, 2)` | 4 | 16 | 4608 | 6 | 1063 | 3.84e+07 |
| 10 | `(28, 6, 4, 1, 1)` | 3 | 18 | 3779 | 2 | 1344 | 5.96e+07 |
| 10 | `(25, 11, 2, 1, 1)` | 4 | 14 | 3837 | 2 | 1354 | 6.23e+07 |
| 10 | `(29, 6, 2, 2, 1)` | 4 | 18 | 2457 | 2 | 1387 | 6.54e+07 |
| 10 | `(27, 8, 3, 1, 1)` | 5 | 20 | 4064 | 2 | 1456 | 7.42e+07 |
| 10 | `(24, 12, 2, 1, 1)` | 4 | 15 | 4651 | 2 | 1642 | 9.17e+07 |
