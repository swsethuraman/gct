# Session 69 — the size curve: circuit against carrier

Every number below is measured in this session unless marked (lmr_cell §6) or (s63).

## 1. The `n = 3` ladder `λ_δ = (3δ − 17, 7, 2^5)`, `det_3`, `r = 7`

| δ | λ | a | N_S (carrier, raw) | n_χ (carrier, χ-reduced) | cells per filling | fillings needed (= a) | samples to reach a | Leibniz terms per filling | expansion s/filling | evaluation s/(filling, point) | χ-support of the six fillings | det rank / i_det |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 12 | (19, 7, 2, 2, 2, 2, 2) | 6 | 1,155,302 | 17,047 | 36 | 6 | 9 | 812,851,200 | 227 | 0.0072 | [2645, 887, 2877, 866, 2998, 3165] | 5 / 1 |
| 13 | (22, 7, 2, 2, 2, 2, 2) | 6 | 1,165,249 | 17,306 | 39 | 6 | 88 | 812,851,200 | 268 | 0.0073 | [826, 2710, 866, 2768, 3141, 3201] | 5 / 1 |
| 14 | (25, 7, 2, 2, 2, 2, 2) | 6 | 1,167,156 | 17,379 | 42 | 6 | 556 | 812,851,200 | 440 | 0.0148 | [866, 887, 2399, 2041, 2723, 3221] | 5 / 1 |

Reading. Along this ladder the circuit's size is **constant**: six fillings at every degree (`a = 6` throughout), the same `(7!)^2·2^5 = 812 851 200`-term expansion per filling (one-columns are fixed indices and add nothing to the enumeration), the same `2^5·2^7 = 4 096` determinants per evaluation. The carrier grows: `N_S` 1,155,302 → 1,167,156, `n_χ` 17,047 → 17,379 — slowly, because the `n = 3` ladder is already close to its stable range (`a` is constant from `δ = 12`). So the honest statement is not about growth rates at `n = 3` (both are nearly flat) but about the constant: `6 × 36`–`42` cells against `17 047`–`17 3xx` coordinates, and an ideal element written as six integers against 3 900 nonzero coordinates. The one-column part of the shape, which is what grows with `δ`, costs the circuit nothing.

## 2. The `n = 4` LMR ladder `λ_δ = (4δ − 31, 17, 2^7)`, `det_4`, `r = 9`

| δ | λ | a (s57/s63) | N_S (lmr_cell §6) | n_χ ≈ N_S/|Stab| (|Stab| = 2·7! = 10 080 at δ = 12, 7! = 5 040 above) | cells per filling | fillings needed | evaluation s/(filling, point), Grassmann DP |
|---|---|---|---|---|---|---|---|
| 12 | (17, 17, 2, 2, 2, 2, 2, 2, 2) | 2 | 51,446,325,457 | 5,103,802 | 48 | 2 (from 120 samples, 22 nonzero) | 0.13-0.4 (DP) |
| 14 | (25, 17, 2, 2, 2, 2, 2, 2, 2) | 93 | 106,429,467,326 | 21,116,957 | 56 | — | — |
| 18 | (41, 17, 2, 2, 2, 2, 2, 2, 2) | 241 | 151,601,110,197 | 30,079,585 | 72 | — | — |
| 21 | (53, 17, 2, 2, 2, 2, 2, 2, 2) | 269 | 156,124,593,451 | 30,977,101 | 84 | — | — |
| 22 | (57, 17, 2, 2, 2, 2, 2, 2, 2) | 272 | 156,346,649,229 | 31,021,160 | 88 | — | — |
| 23 | (61, 17, 2, 2, 2, 2, 2, 2, 2) | 273 | 156,419,279,221 | 31,035,571 | 92 | — | — |
| 24 | (65, 17, 2, 2, 2, 2, 2, 2, 2) | 274 | 156,438,903,314 | 31,039,464 | 96 | ladder rank 2/274 (checkpointed) | 0.13 (DP) |
| 25 | (69, 17, 2, 2, 2, 2, 2, 2, 2) | 274 | 156,443,174,266 | 31,040,312 | 100 | — | — |

Reading. Here the carrier is `~5×10^6` coordinates at the ladder bottom and `~3.1×10^7` at the LMR cell, neither of which any session has built; the circuit needs `a_δ` fillings of `4δ` cells (`2 × 48` at the bottom, `274 × 96` at the top) and evaluates any of them at any point in a fraction of a second. The number of fillings grows exactly like `a_δ`, which is the dimension of the object — the circuit's size is the object's size, not the carrier's. What grows with the carrier is only the cost of *converting* to it (§6 of the spec).
