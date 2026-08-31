# PRE-REGISTRATION 2 — the corrected transport law (session 23)

Committed **after** the refutation of the original Theorem 3.1 equality
(commit `c1629a8`) and **before** any of the confirming computations named in
§3 have been run.  Branch `s23-transport`.

## 1. What is now established

- The reduction (R1)/(R2)/(R3) of `results/PREREG_transport.md` is verified:
  the top-`tau`-weight criterion reproduces the multiplicity-table conductor on
  all 380 weights with `delta <= 10` (322 with `m > 0`), no mismatch, and no
  achievable `nu` outside `6Z`.  **P1 passed, P2 passed** (see §2).
- **P3 is REFUTED.**  `(17,17,2)` has `m = 1`, `mu_max = 13`,
  `floor(mu_max/6) = 2`, and `c = 1` by both independent routes.
- Sweep to `delta <= 20`: the five failures with `m > 0` all have
  `p = lambda_1 - lambda_2 = 0` and `mu_max = 1 (mod 6)`.

## 2. The mechanism, as now understood (derivation, not yet fully swept)

Write `p = l1-l2`, `q = l2-l3`, `r = l3`, `mu = l1 - 2 l3`, `eps = mu mod 6`.
For an admissible shape and a slot `k`, put `s = a_k + 2 q_kbar`.  Three facts:

- **(F-a)** `s = mu (mod 3)` always, forced by the `mu_3^3` conditions
  `n_i = 0 (mod 3)`; hence every achievable `nu = mu - s` or `mu - s - 3` is
  divisible by 3.
- **(F-b)** the `S_3` symmetrisation keeps exactly the drops `T = lambda_1 -
  a_k (mod 2)`; hence every achievable `nu` is even.  Together with (F-a),
  every achievable `nu` is divisible by 6 — which is the single-valuedness of
  `F(f_s)` in `s`, recovered combinatorially.
- **(F-c)** consequently `nu = mu - s` if that is even, else `mu - s - 3`, and
  reaching `nu* = 6 floor(mu/6)` requires `s in {eps, eps-3}`.

When `p = 0` every `a_k = 0`, so `s = 2 q_kbar` is **even**; if in addition
`eps = 1` then `s` would have to be `1` (`eps - 3 < 0`), which is odd.  The top
is unreachable and the conductor drops by exactly one step of the ray.

## 3. The corrected law — PREDICTED, not yet verified

**C1 (the corrected theorem).**  For every `lambda` with `m(lambda) > 0`,

    c(lambda) = floor( (l1 - 2 l3) / 6 )  -  [ l1 = l2  and  l1 - 2 l3 = 1 mod 6 ]

with `[.]` the indicator.  Equivalently: the transport formula holds verbatim
unless `lambda_1 = lambda_2` and `mu_max = 1 (mod 6)`, in which case it
overshoots by exactly 1.
*Falsifier G1: any weight with `m > 0` where this disagrees with the
multiplicity-table conductor.*

**C2 (the failure set is exactly that).**  Over `delta <= 30`, the set of
`lambda` with `m(lambda) > 0` at which the ORIGINAL formula fails is exactly
`{ l1 = l2, l1 - 2 l3 = 1 mod 6 }`; no second family appears, and in
particular nothing with `p >= 1` ever fails.
*Falsifier G2: a failure with `p >= 1` and `m > 0`.*

**C3 (all of the family fails).**  Every `lambda` with `l1 = l2`,
`l1 - 2 l3 = 1 (mod 6)` and `mu_max >= 6` fails attainment, whether `m` is 0 or
positive; the `m = 0` members are exactly the `p = 0` orphans of the paper's
Remark 3.4.
*Falsifier G3: a member of the family that attains.*

**C4 (the drop is exactly one).**  On the failing family with `m > 0`, the
minimum admissible `s` is `4` (i.e. `q_kbar = 2`), so
`nu_max = mu - 7 = 6(floor(mu/6) - 1)` — the conductor is one below the shadow,
never two or more.  Requires `q >= 2`; `q >= 2` is predicted to hold
automatically on the family whenever `mu >= 6`.
*Falsifier G4: a family member with `m > 0` whose conductor is more than one
below the shadow.*

**C5 (orphan locus, restated).**  The orphan locus `{m = 0}` is stable under
`lambda -> lambda^* (x) det^k` exactly for `6 | k`; that duality swaps `p` and
`q`, which is why the paper's two `q = 0` orphans `(10,1,1)`, `(13,1,1)` pair
with the two `p = 0` orphans `(11,11,2)`, `(17,17,5)`.  The `p = 0` orphans are
NOT a separate phenomenon: they are the `m = 0` members of the C3 family.  The
`q = 0` orphans fail for a different reason (cross-slot cancellation between
the `k`-classes), and that reason is predicted to occur only when `m = 0`.
*Falsifier G5: a weight with `m > 0`, `p >= 1`, at which the three `k`-classes
cancel at `nu*`.  (This is G2 again, by a different route.)*

## 4. Method, fixed in advance

- The corrected law is checked against the **multiplicity-table** conductor
  (`orbitB` vs `closureB` along the `T`-ray) — the route that does not use any
  of this session's machinery — on: every member of the failing family up to
  `delta <= 24`, every weight with `delta <= 14`, and a stratified sample
  beyond.
- Exact arithmetic only.
- No paper edit until C1 and C2 both pass.
