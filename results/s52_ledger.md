# Session 52 ledger — the `a = 1` cells measured this session

`n = 4`, `ℓ(λ) = 6`, `a = 1`, ascending in the pre-registered `n_χ` order.

**Route.**  Session 45's sparse certificate (`analysis/wk9_s45_cell.py`,
`analysis/wk9_s42_wied.c`): `mult = a − dim ker[E; ev]` with the `K = a + 8`
evaluation rows pinned through every compression level, both house primes
`2147483647` and `2147483629` run concurrently.  Since `rank_p ≤ rank_Q`,
`nullity_p = 0` at a **single** prime *proves* `mult = a` over `ℚ`; at `a = 1`
that is exactly the brief's cheap direction, `i = 0` certified by one
non-singularity certificate.  A non-zero nullity is a measurement, not a
verdict, until its kernel vector is exhibited and verified.

**Points.**  det: `det_4(Σ s_i A_i)`, random integer `4×4` `A_i`.  pad: the
**true** padded permanent `x_0·per_3(x_1..x_9)` restricted, never
`ℓ·(random cubic)`.


| `δ` | λ | `h_pad` | `N_S` | \|Stab\| | `n_χ` | rows | `nnz` | `mult_det` | `i_det` | `mult_pad` | `i_pad` | `D` | status | secs | HWM GB |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 | `(24, 4, 3, 2, 2, 1)` | 8 | 31187 | 2 | 16929 | 79265 | 206599 | **1** | 0 | 1 | 0 | +0 | proved (nullity 0 at 2147483647) | 235.2 | 2.64 |

**1 cells measured, `i_det = 0` at 1 of them, `D > 0` at 0.**

