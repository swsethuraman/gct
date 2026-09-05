# Session 52 ledger — the `a = 1` cells measured this session

`n = 4`, `ℓ(λ) = 6`, `a = 1`, ascending in the pre-registered `n_χ` order.

**Routes.**  Below `n_χ ≈ 20,000`, the dense route of session 41
(`analysis/wk9_s41_cell.py`): exact kernel on the `χ_λ`-isotypic reduction,
both house primes, `a` re-derived as the kernel dimension and asserted equal to
the plethysm value, `rank(R) = n_χ − a` asserted, every kernel vector verified
against the uncompressed raising-operator rows, `mult_red` point-free by (★).
Above it, session 45's sparse certificate (`analysis/wk9_s45_cell.py`,
`analysis/wk9_s42_wied.c`): `mult = a − dim ker[E; ev]` with the `K = a + 8`
evaluation rows pinned through every compression level, both house primes
`2147483647` and `2147483629` run concurrently.  Since `rank_p ≤ rank_Q`,
`nullity_p = 0` at a **single** prime *proves* `mult = a` over `ℚ`; at `a = 1`
that is exactly the brief's cheap direction, `i = 0` certified by one
non-singularity certificate.  A non-zero nullity is a measurement, not a
verdict, until its kernel vector is exhibited and verified.

**An engineering note.**  The sparse route is not merely unnecessary on small
cells, it is worse.  At `(30,2,2,2,2,2)`, `δ = 10`, `n_χ = 200` it reached
4.6 GB and was ended by the kernel after 317 s (its build was 1 s at 0.07 GB,
so the cost is in the evaluation/compression stage), while the dense exact
route finished the same cell in **3.3 s at 0.09 GB**.

**`n_χ` measured against the estimate.**  The work-list order is by
`⌈N_S/|Stab|⌉`; the measured `n_χ` below runs up to 20% above it
(`(14,5,3,2,2,2)_7`: estimate 24,971, measured 30,037), which is session 46's
correction seen again.

**`mult_red` marked `1*`** is not measured but forced: `mult_pad ≤ mult_red ≤ a`
and `a = 1`, so a measured `mult_pad = 1` gives `mult_red = 1` for free.  The
unstarred values are the point-free (★) computation of the dense route.

**Points.**  det: `det_4(Σ s_i A_i)`, random integer `4×4` `A_i`.  pad: the
**true** padded permanent `x_0·per_3(x_1..x_9)` restricted, never
`ℓ·(random cubic)`.


| `δ` | λ | `h_pad` | `N_S` | \|Stab\| | `n_χ` | rows | `mult_det` | `i_det` | `mult_pad` | `i_pad` | `mult_red` | `D` | route | certificate | secs | HWM GB |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 | `(24, 4, 3, 2, 2, 1)` | 8 | 31187 | 2 | 16929 | 79265 | **1** | 0 | 1 | 0 | 1* | +0 | sparse | proved (nullity 0 at 2147483647) | 235.2 | 2.64 |
| 10 | `(30, 2, 2, 2, 2, 2)` | 2 | 8269 | 120 | 200 | 5826 | **1** | 0 | 1 | 0 | 1 | +0 | exact | exact kernel, both primes, mult_red by (*) | 2.1 | 0.09 |
| 10 | `(29, 3, 2, 2, 2, 2)` | 4 | 19779 | 24 | 1389 | 28134 | **1** | 0 | 1 | 0 | 1 | +0 | exact | exact kernel, both primes, mult_red by (*) | 52.5 | 0.97 |
| 10 | `(27, 5, 5, 1, 1, 1)` | 4 | 20979 | 12 | 673 | 4151 | **1** | 0 | 1 | 0 | 1 | +0 | exact | exact kernel, both primes, mult_red by (*) | 4.4 | 0.13 |
| 10 | `(29, 4, 2, 2, 2, 1)` | 6 | 12800 | 6 | 2785 | 28422 | **1** | 0 | 1 | 0 | 1 | +0 | inplace | exact kernel, both primes, mult_red by (*) | 14.7 | 0.2 |
| 10 | `(26, 8, 3, 1, 1, 1)` | 3 | 20702 | 6 | 1247 | 4197 | **1** | 0 | 1 | 0 | 1 | +0 | exact | exact kernel, both primes, mult_red by (*) | 8.2 | 0.2 |
| 10 | `(27, 7, 2, 2, 1, 1)` | 6 | 18599 | 4 | 3745 | 19211 | **1** | 0 | 1 | 0 | 1 | +0 | inplace | exact kernel, both primes, mult_red by (*) | 26.1 | 0.29 |
| 10 | `(25, 9, 3, 1, 1, 1)` | 4 | 28708 | 6 | 1782 | 5949 | **1** | 0 | 1 | 0 | 1 | +0 | exact | exact kernel, both primes, mult_red by (*) | 16.4 | 0.33 |
| 10 | `(26, 7, 4, 1, 1, 1)` | 6 | 29793 | 6 | 1862 | 5977 | **1** | 0 | 1 | 0 | 1 | +0 | exact | exact kernel, both primes, mult_red by (*) | 17.4 | 0.34 |
| 10 | `(26, 6, 5, 1, 1, 1)` | 6 | 35442 | 6 | 2263 | 7105 | **1** | 0 | 1 | 0 | 1 | +0 | exact | exact kernel, both primes, mult_red by (*) | 27.9 | 0.46 |
| 10 | `(26, 8, 2, 2, 1, 1)` | 9 | 27196 | 4 | 5486 | 28071 | **1** | 0 | 1 | 0 | 1 | +0 | inplace | exact kernel, both primes, mult_red by (*) | 69.9 | 0.49 |
| 10 | `(28, 5, 3, 2, 1, 1)` | 7 | 17722 | 2 | 6740 | 20618 | **1** | 0 | 1 | 0 | 1 | +0 | inplace | exact kernel, both primes, mult_red by (*) | 160.1 | 0.65 |
| 10 | `(27, 5, 3, 3, 1, 1)` | 7 | 44095 | 4 | 8350 | 47300 | **1** | 0 | 1 | 0 | 1 | +0 | inplace | exact kernel, both primes, mult_red by (*) | 249.8 | 0.96 |
| 7 | `(14, 5, 3, 2, 2, 2)` | 14 | 149822 | 6 | 30037 | 313184 | **1** | 0 | 1 | 0 | 1* | +0 | sparse | proved (nullity 0 at 2147483647) | 1609.1 | 0.34 |
| 10 | `(28, 4, 3, 2, 2, 1)` | 8 | 31299 | 2 | 17000 | 79596 | **1** | 0 | 1 | 0 | 1 | +0 | inplace | exact kernel, both primes, mult_red by (*) | 1458.1 | 3.47 |
| 7 | `(14, 5, 3, 3, 2, 1)` | 10 | 112552 | 2 | 54477 | 293964 | **1** | 0 | 1 | 0 | 1* | +0 | sparse | proved (nullity 0 at 2147483647) | 1591.4 | 0.32 |
| 7 | `(14, 4, 4, 3, 2, 1)` | 10 | 129228 | 2 | 65778 | 343979 | **1** | 0 | 1 | 0 | 1* | +0 | sparse | proved (nullity 0 at 2147483647) | 1349.2 | 0.33 |

**17 cells measured, `i_det = 0` at 17 of them, `D > 0` at 0.**

