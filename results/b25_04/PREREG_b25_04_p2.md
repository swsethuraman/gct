# PREREG — B25-04 pilot 2 (`b25_04_p2_nonvacuous`)

Written after pilot 1's output was read and before this script exists. UNCOMMITTED.

## Why a second pilot

Pilot 1 passed every assertion, but its K2 component check was **vacuous**: the factor
`f_{T̂_123}` (columns `(1,2,3),(1,2)`, shape `(12,2,1)`) was `0` at all five sampled points, so
`lhs = f123 · f45` was checked only as `0 = 0`. The isolated-vertex check was not vacuous. Pilot 1
is reported as is; this pilot replaces its K2 by a check whose factors are proved nonzero.
Pilot 1's output is pinned: `results/b25_04/p1_factor.json` sha256
`cc6031c8ed9fe6a354e53676fc03e21426feae661fbbfa70e5581e2f1ed40ce5` (asserted in code).

## Object

The same weighted BDI (5.2) evaluator as pilot 1, imported by executing only pilot 1's
function-definition prefix (up to and excluding the line `# T_g: shape (8,2)`), so the evaluator is
provably the one pilot 1 ran. `n = 5`, `r = 3`.

## Claims tested (fixed now)

- `g`: shape `(8,2)`, columns `(1,2),(1,2)` + singletons; `h`: shape `(6,4)`, columns
  `(1,2)×4` + singletons (row 1 `1 1 1 1 1 2`, row 2 `2 2 2 2`), the unique semistandard tableau
  of that shape and content `2 × 5`, spanning the 1-dimensional `HWV_{(6,4)}(Sym^2 Sym^5)`.
- **K2′.** `T = T_g on {1,2} ⊔ T_h on {3,4}` (`d = 4`, `λ = (14,6)`, asserted):
  `f_T(p) = g(p)·h(p)` at 5 seeded points, **and** `g(p) ≠ 0` and `h(p) ≠ 0` at at least 3 of them
  (non-vacuity is asserted, not hoped).
- **K2″.** `T ⊔ {5 in five singleton columns}` (`d = 5`, `λ = (19,6)`):
  `= g(p)·h(p)·c_{5e_1}(p)` at 5 seeded points, with all three factors nonzero at ≥ 3 of them.
- `G_T` is computed and its components are asserted to be `{1,2},{3,4}` (and `{5}` for K2″).

## Price, limits, stop rule

`3^5 = 243` placements × ≤ 25 dets × ~15 evaluations: **< 2 s, < 100 MiB**. Same wrapper and caps
(`--seconds 60 --memory-mb 512`), under a freshly acquired exclusive lease. A failed assertion
(including non-vacuity) is reported as the result; no pilot 3 is planned. Seed
`random.Random(2509210402)`. Output `results/b25_04/p2_nonvacuous.json`.
