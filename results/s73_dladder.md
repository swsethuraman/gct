# The `n = 3` `D`-ladder on `λ_δ = (3δ − 17, 7, 2^5)`, `r = 7` — session 73

`D = i_det − i_per = mult_per − mult_det`; `i_X = a − mult_X`.  `i_X = 0` rows are **proved** (nullity 0 at one prime proves `mult_X = a` over `Q`); positive nullities are **measured** at both primes and carried to `Q` by an exhibited integer kernel vector (see the certificates).  `a` by two independent plethysm engines.  Seed family `primary` = the pre-registered seeds; `second` = the verification-protocol family (`K = a + 20`).

| δ | λ | seeds | a | n_χ | i_det | mult_det | i_per | mult_per | D | outcome | dim(U_D ∩ U_P) | U_D ⊆ U_P / U_P ⊆ U_D | kernel origin (transport) | primes agree | wall s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 | `(10, 7, 2, 2, 2, 2, 2)` | primary | 2 | 11425 | 0 | 2 | 0 | 2 | 0 | D = 0: orientation test | 0 | True / True | — | True | 2001.5 |
| 10 | `(13, 7, 2, 2, 2, 2, 2)` | primary | 4 | 14598 | 0 | 4 | 0 | 4 | 0 | D = 0: orientation test | 0 | True / True | — | True | 3541.6 |
| 11 | `(16, 7, 2, 2, 2, 2, 2)` | primary | 5 | 16318 | 0 | 5 | 0 | 5 | 0 | D = 0: orientation test | 0 | True / True | — | True | 4785.2 |
| 12 | `(19, 7, 2, 2, 2, 2, 2)` | primary | 6 | 17047 | 1 | 5 | 0 | 6 | +1 | D = +1 > 0: multiplicity obstruction (i_per < i_det) | 0 | False / True | born at this rung (U_D(δ−1) = 0) | True | 5874.2 |
| 12 | `(19, 7, 2, 2, 2, 2, 2)` | second | 6 | 17047 | 1 | 5 | 0 | 6 | +1 | D = +1 > 0: multiplicity obstruction (i_per < i_det) | 0 | False / True | born at this rung (U_D(δ−1) = 0) | True | 2149.4 |
| 13 | `(22, 7, 2, 2, 2, 2, 2)` | primary | 6 | 17306 | 1 | 5 | 0 | 6 | +1 | D = +1 > 0: multiplicity obstruction (i_per < i_det) | 0 | False / True | = J(U_D(δ−1)) (transported, nothing born) | True | 1800.8 |
| 14 | `(25, 7, 2, 2, 2, 2, 2)` | primary | 6 | 17379 | 1 | 5 | 0 | 6 | +1 | D = +1 > 0: multiplicity obstruction (i_per < i_det) | 0 | False / True | = J(U_D(δ−1)) (transported, nothing born) | True | 1646.2 |
| 15 | `(28, 7, 2, 2, 2, 2, 2)` | primary | 6 | 17399 | 1 | 5 | 0 | 6 | +1 | D = +1 > 0: multiplicity obstruction (i_per < i_det) | 0 | False / True | = J(U_D(δ−1)) (transported, nothing born) | True | 1623.4 |
| 16 | `(31, 7, 2, 2, 2, 2, 2)` | primary | 6 | 17403 | 1 | 5 | 0 | 6 | +1 | D = +1 > 0: multiplicity obstruction (i_per < i_det) | 0 | False / True | = J(U_D(δ−1)) (transported, nothing born) | True | 1582.9 |

## Transport records (`J = ·c_{(3,0,…,0)}`)

| δ → δ+1 | a → a | J(M_δ) HWV at δ+1 | rank J(M_δ) | J(M_δ) ⊆ M_{δ+1} | birth dim | u-free rank of M_{δ+1} | E·J(v) = 0 over Z (det) | J(U_D) ⊆ U_D' / equal (P1) | lines equal over Z |
|---|---|---|---|---|---|---|---|---|---|
| 9 → 10 | 2 → 4 | True | 2 | True | 2 | 2 | — | — / — | — |
| 10 → 11 | 4 → 5 | True | 4 | True | 1 | 1 | — | — / — | — |
| 11 → 12 | 5 → 6 | True | 5 | True | 1 | 1 | — | — / — | — |
| 12 → 13 | 6 → 6 | True | 6 | — | — | — | [True] | True / True | True |
| 13 → 14 | 6 → 6 | — | — | — | — | — | [True] | True / True | True |
| 14 → 15 | 6 → 6 | — | — | — | — | — | [True] | True / True | True |
| 15 → 16 | 6 → 6 | — | — | — | — | — | [True] | True / True | True |
