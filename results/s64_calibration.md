# Session 64 — padded-side calibration table

`n = 4`.  48 cells; **48/48 PASS**; 12 discriminating (`mult_pad = mult_red < mult_det`).  Both house primes `2147483647, 2147483629`; `mult_pad` at ≥2 independent seeds on the dense route (exact per-prime certificate on the sparse route).  `mult_pad = mult_red` is forced at `r ≤ 5` by `P_r = R_r` (`results/s64_paramrank.md`); the check is non-vacuous only where `mult_red < a`.  Engine: `reduced` = `wk10_s64_cell` (isotypic + shared dense kernel) / sparse `wk10_s64_sparse`; `indep` = `wk10_s64_indep` (full basis, no reduction, no Wiedemann — a second implementation).

| r | δ | λ | a | h_pad | n_χ | route | mult_det | mult_red | mult_pad | D | engine | banked det/red | PASS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 6 | `(8, 8, 8)` **d** | 2 | — | — | dense | 2 | 1 | 1 | -1 | indep | (indep only) | ✅ |
| 5 | 6 | `(8, 4, 4, 4, 4)` **d** | 2 | 1 | 4562 | dense | 2 | 1 | 1 | -1 | reduced | 2/1 ✓ | ✅ |
| 5 | 7 | `(8, 8, 8, 2, 2)` **d** | 3 | 2 | 11778 | sparse | 3 | 2 | 2 | -1 | reduced | 3/2 ✓ | ✅ |
| 5 | 7 | `(9, 9, 8, 1, 1)` **d** | 2 | 1 | 3969 | dense | 2 | 1 | 1 | -1 | reduced | 2/1 ✓ | ✅ |
| 5 | 7 | `(12, 4, 4, 4, 4)` **d** | 4 | 4 | 9738 | sparse | 4 | 3 | 3 | -1 | reduced | 4/3 ✓ | ✅ |
| 5 | 8 | `(11, 11, 8, 1, 1)` **d** | 8 | 8 | 9684 | sparse | 8 | 7 | 7 | -1 | reduced | 8/7 ✓ | ✅ |
| 5 | 8 | `(12, 9, 9, 1, 1)` **d** | 7 | 6 | 9800 | sparse | 7 | 5 | 5 | -2 | reduced | 7/5 ✓ | ✅ |
| 5 | 8 | `(13, 9, 8, 1, 1)` **d** | 15 | 21 | 16556 | sparse | 15 | 13 | 13 | -2 | reduced | 15/13 ✓ | ✅ |
| 5 | 8 | `(16, 4, 4, 4, 4)` **d** | 7 | 10 | 14148 | sparse | 7 | 6 | 6 | -1 | reduced | 7/6 ✓ | ✅ |
| 5 | 9 | `(13, 13, 8, 1, 1)` **d** | 19 | 17 | 20099 | sparse | 19 | 15 | 15 | -4 | reduced | 19/15 ✓ | ✅ |
| 5 | 9 | `(15, 15, 4, 1, 1)` **d** | 9 | 12 | 4415 | dense | 9 | 8 | 8 | -1 | reduced | 9/8 ✓ | ✅ |
| 5 | 9 | `(20, 4, 4, 4, 4)` **d** | 9 | 13 | 16732 | sparse | 9 | 8 | 8 | -1 | reduced | 9/8 ✓ | ✅ |
| 2 | 2 | `(4, 4)` | 1 | — | — | dense | 1 | 1 | 1 | 0 | indep | (indep only) | ✅ |
| 3 | 3 | `(4, 4, 4)` | 1 | — | — | dense | 1 | 1 | 1 | 0 | indep | (indep only) | ✅ |
| 3 | 4 | `(8, 6, 2)` | 2 | — | — | dense | 2 | 2 | 2 | 0 | indep | (indep only) | ✅ |
| 3 | 5 | `(10, 6, 4)` | 4 | — | — | dense | 4 | 4 | 4 | 0 | indep | (indep only) | ✅ |
| 3 | 5 | `(12, 6, 2)` | 4 | — | — | dense | 4 | 4 | 4 | 0 | indep | (indep only) | ✅ |
| 4 | 4 | `(6, 6, 2, 2)` | 1 | — | — | dense | 1 | 1 | 1 | 0 | indep | (indep only) | ✅ |
| 4 | 5 | `(8, 6, 4, 2)` | 3 | — | — | dense | 3 | 3 | 3 | 0 | indep | (indep only) | ✅ |
| 4 | 6 | `(8, 8, 4, 4)` | 4 | — | — | dense | 4 | 4 | 4 | 0 | indep | (indep only) | ✅ |
| 5 | 6 | `(8, 7, 7, 1, 1)` | 2 | 2 | 1300 | dense | 2 | 2 | 2 | 0 | reduced | 2/2 ✓ | ✅ |
| 5 | 6 | `(9, 7, 6, 1, 1)` | 2 | 5 | 2262 | dense | 2 | 2 | 2 | 0 | reduced | 2/2 ✓ | ✅ |
| 5 | 6 | `(9, 8, 5, 1, 1)` | 2 | 6 | 1947 | dense | 2 | 2 | 2 | 0 | reduced | 2/2 ✓ | ✅ |
| 5 | 6 | `(9, 9, 4, 1, 1)` | 2 | 4 | 736 | dense | 2 | 2 | 2 | 0 | reduced | 2/2 ✓ | ✅ |
| 5 | 6 | `(10, 8, 2, 2, 2)` | 3 | 11 | 1661 | dense | 3 | 3 | 3 | 0 | reduced | 3/3 ✓ | ✅ |
| 5 | 6 | `(11, 7, 4, 1, 1)` | 4 | 14 | 1187 | dense | 4 | 4 | 4 | 0 | reduced | 4/4 ✓ | ✅ |
| 5 | 6 | `(12, 5, 5, 1, 1)` | 2 | 5 | 524 | dense | 2 | 2 | 2 | 0 | reduced | 2/2 ✓ | ✅ |
| 5 | 6 | `(12, 6, 2, 2, 2)` | 4 | 16 | 1162 | dense | 4 | 4 | 4 | 0 | reduced | 4/4 ✓ | ✅ |
| 5 | 6 | `(12, 6, 4, 1, 1)` | 2 | 12 | 927 | dense | 2 | 2 | 2 | 0 | reduced+indep | 2/2 ✓ | ✅ |
| 5 | 6 | `(13, 5, 2, 2, 2)` | 2 | 12 | 825 | dense | 2 | 2 | 2 | 0 | reduced | 2/2 ✓ | ✅ |
| 5 | 7 | `(14, 9, 3, 1, 1)` | 5 | 15 | 1386 | dense | 5 | 5 | 5 | 0 | reduced | 5/5 ✓ | ✅ |
| 5 | 7 | `(15, 8, 3, 1, 1)` | 4 | 15 | 1137 | dense | 4 | 4 | 4 | 0 | reduced | 4/4 ✓ | ✅ |
| 5 | 7 | `(16, 5, 5, 1, 1)` | 3 | 7 | 663 | dense | 3 | 3 | 3 | 0 | reduced | 3/3 ✓ | ✅ |
| 5 | 7 | `(16, 6, 4, 1, 1)` | 3 | 17 | 1177 | dense | 3 | 3 | 3 | 0 | reduced | 3/3 ✓ | ✅ |
| 5 | 7 | `(17, 5, 2, 2, 2)` | 3 | 15 | 978 | dense | 3 | 3 | 3 | 0 | reduced | 3/3 ✓ | ✅ |
| 5 | 7 | `(18, 4, 2, 2, 2)` | 3 | 9 | 606 | dense | 3 | 3 | 3 | 0 | reduced+indep | 3/3 ✓ | ✅ |
| 5 | 8 | `(17, 11, 2, 1, 1)` | 3 | 9 | 1060 | dense | 3 | 3 | 3 | 0 | reduced | 3/3 ✓ | ✅ |
| 5 | 8 | `(18, 10, 2, 1, 1)` | 2 | 9 | 899 | dense | 2 | 2 | 2 | 0 | reduced+indep | 2/2 ✓ | ✅ |
| 5 | 8 | `(20, 5, 5, 1, 1)` | 3 | 7 | 726 | dense | 3 | 3 | 3 | 0 | reduced | 3/3 ✓ | ✅ |
| 5 | 8 | `(20, 7, 3, 1, 1)` | 4 | 14 | 962 | dense | 4 | 4 | 4 | 0 | reduced+indep | 4/4 ✓ | ✅ |
| 5 | 8 | `(21, 5, 2, 2, 2)` | 4 | 16 | 1040 | dense | 4 | 4 | 4 | 0 | reduced | 4/4 ✓ | ✅ |
| 5 | 8 | `(22, 4, 2, 2, 2)` | 3 | 9 | 625 | dense | 3 | 3 | 3 | 0 | reduced+indep | 3/3 ✓ | ✅ |
| 5 | 9 | `(21, 11, 2, 1, 1)` | 4 | 12 | 1243 | dense | 4 | 4 | 4 | 0 | reduced | 4/4 ✓ | ✅ |
| 5 | 9 | `(22, 10, 2, 1, 1)` | 2 | 11 | 1010 | dense | 2 | 2 | 2 | 0 | reduced | 2/2 ✓ | ✅ |
| 5 | 9 | `(24, 5, 5, 1, 1)` | 3 | 7 | 747 | dense | 3 | 3 | 3 | 0 | reduced | 3/3 ✓ | ✅ |
| 5 | 9 | `(24, 7, 3, 1, 1)` | 4 | 14 | 999 | dense | 4 | 4 | 4 | 0 | reduced | 4/4 ✓ | ✅ |
| 5 | 9 | `(25, 5, 2, 2, 2)` | 4 | 16 | 1059 | dense | 4 | 4 | 4 | 0 | reduced | 4/4 ✓ | ✅ |
| 5 | 9 | `(26, 4, 2, 2, 2)` | 3 | 9 | 629 | dense | 3 | 3 | 3 | 0 | reduced+indep | 3/3 ✓ | ✅ |

**d** marks a discriminating cell (`mult_pad = mult_red < mult_det`), where a correct padded engine must return a value strictly below the determinant's — the only cells that distinguish the padded side from a silent copy of the determinant.
