# The `a = 1` injectivity route against the dense route — nine weights

Session 43.  The route is described in `analysis/wk9_s43_inject.py` and
pre-registered in `results/PREREG_s43.md` §2 (P3).  For `a = 1`,
`mult = 1 ⟺ [M ; Ev]` is injective, where `M` are the reduced raising-operator
rows and `Ev` the `a + 8` evaluation rows in the same χ-coordinates; full column
rank over `F_p` forces it over `Q`, so the verdict is one-sided in the same
direction as every other "empty" verdict in the programme.  The certificate is
session 42's sparse Wiedemann tool (`analysis/wk9_s42_wied.c`): `NONSINGULAR`
is reported only when the Berlekamp–Massey minimal polynomial of the Wiedemann
sequence has degree exactly `n_χ` with `f(0) ≠ 0`, which proves `M = D₂FᵀD₁FD₂`
nonsingular and hence `F` injective, with no randomness in that implication.
Memory is `O(nnz)`, not `O(n_χ²)`.

| δ | μ | n_χ | rows of `[M;Ev]` | nnz | injectivity `mult` | dense `mult` | inject secs / HWM | dense secs / HWM |
|---|---|---|---|---|---|---|---|---|
| 7 | `(8, 4, 4, 2, 2, 1)` | 5029 | 35327 | 150395 | 1 | 1 (s41) | 12 / 0.10 | 56 / 0.41 |
| 7 | `(7, 6, 4, 2, 1, 1)` | 4383 | 14179 | 82028 | 1 | 1 (s41) | 6 / 0.10 | 37 / — |
| 7 | `(6, 5, 5, 3, 1, 1)` | 4187 | 23562 | 116119 | 1 | 1 (s41) | 8 / 0.10 | 35 / — |
| 7 | `(9, 4, 3, 2, 2, 1)` | 6167 | — | — | 1 | 1 (s43) | 12 / 0.10 | 110 / 0.56 |
| 7 | `(7, 5, 4, 3, 1, 1)` | 6895 | 22003 | 131282 | 1 | 1 (s43) | 14 / 0.10 | 146 / 0.67 |
| 7 | `(6, 6, 4, 2, 2, 1)` | 6982 | 44647 | 202517 | 1 | 1 (s43) | 20 / 0.11 | 153 / 0.70 |
| 7 | `(8, 5, 3, 2, 2, 1)` | 8402 | 39968 | 185548 | 1 | 1 (s43) | 22 / 0.10 | 236 / 0.96 |
| 7 | `(7, 6, 3, 2, 2, 1)` | 9789 | — | — | 1 | 1 (s43) | 30 / 0.11 | 383 / 1.22 |
| 7 | `(7, 5, 4, 2, 2, 1)` | 12564 | — | — | 1 | 1 (s43) | 49 / 0.11 | 717 / 1.96 |

**9 of 9 agree**, both primes at every weight.  The route is 12–15× faster and
runs at a tenth of the memory, and its cost grows like `n_χ · nnz` rather than
`n_χ²` in space — which is why `(6,5,4,3,2,1)` at `n_χ = 39,921`, twice the
dense frontier, is reachable at all (482 s, 0.15 GB).

On this record the route is used for the `a = 1` weights of the `δ = 8`
Phase-B scan as well.  Every row it produces is marked `inject` in the `route`
column of `results/s43_per6.md`; no `inject` row is merged into a dense one.

## The `a ≥ 2` extension

`ker[M ; Ev]` is the space of weight-`μ` highest-weight vectors vanishing at the
`K` points, of dimension `a − mult`, so `[M;Ev]` injective ⟺ `mult = a` — **at
every `a`, not only `a = 1`**.  A `NONSINGULAR` certificate therefore proves the
empty verdict at any `a`; a verified `KERNEL` vector proves only `mult < a`, and
the exact value would then be taken by the dense route.  Four banked `δ = 8`
weights of `results/s41_per6.md` with `a ≥ 2` were re-measured by the route:

| δ | μ | a | injectivity `mult` | dense `mult` (s41) | secs | HWM |
|---|---|---|---|---|---|---|
| 8 | `(12, 4, 2, 2, 2, 2)` | 2 | 2 | 2 | 5 | 0.15 |
| 8 | `(11, 6, 2, 2, 2, 1)` | 2 | 2 | 2 | 9 | 0.15 |
| 8 | `(10, 6, 2, 2, 2, 2)` | 3 | 3 | 3 | 14 | 0.16 |
| 8 | `(10, 5, 5, 2, 1, 1)` | 2 | 2 | 2 | 10 | 0.16 |

**13 of 13 agreements in all** (nine at `a = 1`, four at `a = 2, 3`), both primes
at every weight.  On this record the route is used for the whole `δ = 8`
Phase-B scan.
