# Session 56 calibration — the Foulkes rank against every banked `mult_det`

One row per constituent `S_lambda(C^r)` of `Sym^delta(Sym^4 C^r)` at `delta = 2, 3, 4`
(`r = ell(lambda)`), for which an exact `mult_det` is banked. `m` is the Foulkes
engine's `rank Hom_{S_N}([lambda], Theta^+_delta)`, computed with no highest-weight
vector and no determinant pencil; `a` the ambient plethysm coefficient; `sk` the
symmetric rectangular Kronecker coefficient (the target multiplicity). Every `m`
is exact, confirmed at both house primes; at `delta = 2, 3` also by the independent
Hecke-projector route and over `Q`.

**40 of 40 cells agree with the banked value. No disagreement. `i_det = a - m = 0` at every cell.**

| delta | lambda | r | a | sk | m (Foulkes) | i_det | banked mult_det | agree |
|---|---|---|---|---|---|---|---|---|
| 2 | (8,) | 1 | 1 | 1 | 1 | 0 | 1 | yes |
| 2 | (6, 2) | 2 | 1 | 1 | 1 | 0 | 1 | yes |
| 2 | (4, 4) | 2 | 1 | 1 | 1 | 0 | 1 | yes |
| 3 | (12,) | 1 | 1 | 1 | 1 | 0 | 1 | yes |
| 3 | (10, 2) | 2 | 1 | 1 | 1 | 0 | 1 | yes |
| 3 | (9, 3) | 2 | 1 | 1 | 1 | 0 | 1 | yes |
| 3 | (8, 4) | 2 | 1 | 1 | 1 | 0 | 1 | yes |
| 3 | (8, 2, 2) | 3 | 1 | 2 | 1 | 0 | 1 | yes |
| 3 | (7, 4, 1) | 3 | 1 | 1 | 1 | 0 | 1 | yes |
| 3 | (6, 6) | 2 | 1 | 1 | 1 | 0 | 1 | yes |
| 3 | (6, 4, 2) | 3 | 1 | 2 | 1 | 0 | 1 | yes |
| 3 | (4, 4, 4) | 3 | 1 | 2 | 1 | 0 | 1 | yes |
| 4 | (16,) | 1 | 1 | 1 | 1 | 0 | 1 | yes |
| 4 | (14, 2) | 2 | 1 | 1 | 1 | 0 | 1 | yes |
| 4 | (13, 3) | 2 | 1 | 1 | 1 | 0 | 1 | yes |
| 4 | (12, 4) | 2 | 2 | 2 | 2 | 0 | 2 | yes |
| 4 | (12, 2, 2) | 3 | 1 | 2 | 1 | 0 | 1 | yes |
| 4 | (11, 4, 1) | 3 | 1 | 1 | 1 | 0 | 1 | yes |
| 4 | (11, 3, 2) | 3 | 1 | 2 | 1 | 0 | 1 | yes |
| 4 | (10, 6) | 2 | 2 | 2 | 2 | 0 | 2 | yes |
| 4 | (10, 5, 1) | 3 | 1 | 1 | 1 | 0 | 1 | yes |
| 4 | (10, 4, 2) | 3 | 2 | 4 | 2 | 0 | 2 | yes |
| 4 | (10, 2, 2, 2) | 4 | 1 | 5 | 1 | 0 | 1 | yes |
| 4 | (9, 6, 1) | 3 | 1 | 1 | 1 | 0 | 1 | yes |
| 4 | (9, 5, 2) | 3 | 1 | 2 | 1 | 0 | 1 | yes |
| 4 | (9, 4, 3) | 3 | 1 | 2 | 1 | 0 | 1 | yes |
| 4 | (9, 4, 2, 1) | 4 | 1 | 5 | 1 | 0 | 1 | yes |
| 4 | (8, 8) | 2 | 1 | 1 | 1 | 0 | 1 | yes |
| 4 | (8, 6, 2) | 3 | 2 | 4 | 2 | 0 | 2 | yes |
| 4 | (8, 5, 2, 1) | 4 | 1 | 5 | 1 | 0 | 1 | yes |
| 4 | (8, 4, 4) | 3 | 2 | 5 | 2 | 0 | 2 | yes |
| 4 | (8, 4, 2, 2) | 4 | 1 | 11 | 1 | 0 | 1 | yes |
| 4 | (7, 7, 1, 1) | 4 | 1 | 1 | 1 | 0 | 1 | yes |
| 4 | (7, 6, 3) | 3 | 1 | 2 | 1 | 0 | 1 | yes |
| 4 | (7, 5, 3, 1) | 4 | 1 | 5 | 1 | 0 | 1 | yes |
| 4 | (7, 4, 4, 1) | 4 | 1 | 5 | 1 | 0 | 1 | yes |
| 4 | (6, 6, 4) | 3 | 1 | 3 | 1 | 0 | 1 | yes |
| 4 | (6, 6, 2, 2) | 4 | 1 | 7 | 1 | 0 | 1 | yes |
| 4 | (6, 4, 4, 2) | 4 | 1 | 10 | 1 | 0 | 1 | yes |
| 4 | (4, 4, 4, 4) | 4 | 1 | 4 | 1 | 0 | 1 | yes |

## Banked sources

- theorem: D_r=Sym^4 C^r for r<=3 (docs/sweep62.md §4), so mult_det=a
- theorem: I(D_4^det) principal of degree e>=10 (s33, docs/e4_hunt.md), so I(D_4)_delta=0 at delta<=4, mult_det=a
- measured: a=1, mult_det=1 (docs/det_onset.md §3, results/e4_ledger.md)

## The two identities the brief asks to check

- `0 <= m <= min(a, sk)` at every cell: **holds** (checked in-run for all 40 cells).
- `m = a` exactly when `i_det = 0`: **holds** — `i_det = a - m = 0` at every cell, and `m = a` at every cell.
  Equivalently `Theta^+_delta` is injective at `delta = 2, 3, 4` (`rank beta = |H_{4,delta}|`:
  35, 5775, 2627625), which is the statement `i_det = 0` at every weight of degree `<= 4`.
