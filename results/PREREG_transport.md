# PRE-REGISTRATION — attainment in the World-B transport formula (session 23)

Committed **before any computation is run in this session.**  Nothing below has
been machine-checked yet; the derivation in §2 was done by hand from the
material named in §1.  Branch `s23-transport`, cloned from public `main` at
tip `5cdc29c`.

Date: 2026-08-31.

---

## 1. The question (Question 7.1 / Theorem 3.1 of `paper/det3-conductor.tex`)

World B: `W = Sym^3 C^3`, `v` = Fermat cubic, `H = stab(v) = mu_3^3 : S_3`
(order 162), `Omega-bar` = the Aronhold quartic hypersurface, boundary divisor
cut by the degree-6 semiinvariant `T` of weight `det^6`, dense boundary orbit
the cusp `G.(x^2 y + z^3)`, stabiliser torus `tau(t) = diag(t, t^-2, 1)`,
normal weight of size 6.

Theorem 3.1 as it stands: on every weight with `m(lambda) > 0` and
`delta <= 10` (254 of them),

    c(lambda) = floor( (lambda_1 - 2 lambda_3) / 6 ) = floor( mu_max / |w_N| ).

`<=` is proved (block-order estimate + FFT spanning + "Young symmetrisation
only cancels").  **Attainment (`>=`) is what is missing.**

## 2. The reduction this session will test (derived by hand, unverified)

Write `f_s = x^2 y + s y^3 + z^3` for the transversal family, `p = lambda_1 -
lambda_2`, `q = lambda_2 - lambda_3`, `r = lambda_3`.

**(R1) The transversal family is a single torus orbit.**  The Waring lines of
`f_s` are `l1 = kappa rho^-1 (x + rho^3 y)`, `l2 = -kappa rho^-1 (x - rho^3 y)`,
`l3 = z` with `kappa = 6^{-1/3}` and `s = rho^6 / 3`, so the matrix of Waring
lines factors as `M(rho) = A . diag(rho^-1, rho^2, 1)` with

    A = [[kappa, kappa, 0], [-kappa, kappa, 0], [0, 0, 1]]   (constant),

i.e. `f_s = tau(rho) . (B . v)` with `B = A^{-1}` and `tau(rho) = diag(rho,
rho^-2, 1)`.  Consequently, for `F` in the `lambda`-isotypic component,
`F(f_s)` is the `tau`-graded expansion of a single vector, and

**(R2) the conductor is a top-weight non-vanishing condition:**

    c(lambda) = (1/6) * max { nu : pi_nu( B . S_lambda^H ) != 0 },

`pi_nu` = projection onto the `tau`-weight-`nu` subspace of `S_lambda`, `B`
taken up to scalars (scalars are irrelevant because `B` preserves the
`GL_2 x GL_1` branching blocks, which are multiplicity-free, so no two blocks
interfere).  The largest `tau`-weight of `S_lambda` is `lambda_1 - 2 lambda_3`
= `mu_max`, recovering the upper bound; attainment is the statement that the
component at `nu = 6 floor(mu_max/6)` is nonzero.

**(R3) The combinatorial form.**  `S_lambda^H` is spanned by the images of the
`S_3`-symmetrised monomials

    Theta(a,Q) = sum_{pi in S_3} pi . ( e^a f^Q ) . det^r,
    a = (a_1,a_2,a_3) |- p,  Q = (q_12,q_13,q_23) |- q,

subject to the `mu_3^3` condition `n_i = a_i + sum_j q_ij + r = 0 (mod 3)`.
Under `B` (which sends `e_1 -> e_1 + e_2`, `e_2 -> -e_1 + e_2`, `e_3 -> e_3`)
each of the three permutation-pairs indexed by `k` (= the slot sent to 3)
contributes a top `tau`-weight

    N_k = (lambda_1 - 2 lambda_3) - a_k - 2 q_{kbar},   q_{kbar} = the wedge
                                                        count on the pair not
                                                        containing k,

and the top coefficient of that pair is proportional to `1 + (-1)^{N_k}`.

## 3. Predictions, with falsifiers

**P1 (the reduction is right).**  Conductors recomputed from (R2)/(R3) agree
with the conductor read off the multiplicity tables (`m(lambda)` minus closure
multiplicity along the `T`-ray) on **every** weight of the banked `delta <= 10`
range, all 254 with `m > 0` and the `m = 0` ones too.
*Falsifier F1: a single disagreement on that range.*

**P2 (the parity lemma).**  The top coefficient of the `k`-pair vanishes
**exactly** when `N_k` is odd — equivalently `a_k != lambda_1 (mod 2)` — and
never for any other reason.  So the only cancellation in Young symmetrisation
at top order is the integrality parity, exactly as in World A.
*Falsifier F2: a shape where the top coefficient vanishes with `N_k` even, or
survives with `N_k` odd (cross-`k` coincidences excepted and to be reported
separately).*

**P3 (attainment, the theorem).**  For every `lambda` with `m(lambda) > 0`
there is an admissible shape and a `k` with `N_k = 6 floor(mu_max/6)`; hence
attainment holds and Theorem 3.1's equality is a theorem for all `lambda`, with
no degree bound.  Predicted mechanism: the mod-3 conditions `n_i = 0` are
**automatically compatible** with imposing `a_k + 2 q_{kbar} = eps`, where
`eps = mu_max mod 6`, so the only possible obstruction is nonnegativity
(`a_k <= p`, `q_{kbar} <= q`) — i.e. small `p` and `q`.
*Falsifier F3: a weight with `m(lambda) > 0` at which the top-weight component
of `B . S_lambda^H` at `nu = 6 floor(mu_max/6)` vanishes.*

**P3' (the ranked alternative, logged now).**  If P3 fails, the predicted shape
of the failure is: it fails only on a thin set characterised by the same
nonnegativity arithmetic (`p = lambda_1 - lambda_2` and `q = lambda_2 -
lambda_3` both small relative to `eps`), and the corrected theorem carries an
explicit side condition of that form rather than being false in general.

**P4 (the orphan locus is duality-stable — a full answer to the paper's
Remark 3.4 question).**  `m(lambda) = 0` is invariant under
`lambda -> lambda^* (x) det^k` **whenever `6 | k`**, for the elementary reason
that `det|_H` has order 6 (`det` is `omega^{a+b+c}` on `mu_3^3` and `sgn` on
`S_3`), so `det^k|_H` is trivial exactly for `6 | k`; and `dim (S_lambda^*)^H =
dim S_lambda^H` for finite `H`.  The two banked pairs are the minimal such
twists (`k = 12` for `(10,1,1)`, `lambda_1 = 10`; `k = 18` for `(13,1,1)`,
`lambda_1 = 13`).  Predicted: the orphan locus IS stable, the stabiliser is
exactly `6 | k`, and it is **not** the key to the attainment proof — it is a
separate (easy) structural fact.
*Falsifier F4: an orphan whose `6|k` dual twist has `m > 0`; or a `k` not
divisible by 6 that nonetheless preserves the locus on the swept range.*

**P5 (the failure set is exactly empty support).**  Over the extended sweep
(`delta <= 24` at least), the weights where the shadow maximum
`floor(mu_max/6) >= 1` is not attained are **exactly** those with
`m(lambda) = 0`.
*Falsifier F5: a weight with `m(lambda) = 0` where the shadow is nevertheless
attained (harmless but would break the "exactly"), or — the dangerous one —
a weight with `m > 0` where it is not (this is F3 again).*

## 4. Method, fixed in advance

- Exact arithmetic only (Python integers / `Fraction` / sympy `Rational`).
- Two independent routes to `m(lambda)`: (i) the character count over the 162
  elements of `H` (the banked `orbitB` route in `analysis/wk2_s4_sweep.py`),
  (ii) the rank of the span of the `Theta(a,Q)` in the straightened
  (Plücker-quotient) model.  They must agree on the whole sweep before any
  claim is made.
- Two independent routes to `c(lambda)`: (i) the banked multiplicity/ray
  computation (`closureB` along the `T`-ray vs `orbitB`), (ii) the top-weight
  criterion (R2).  P1 is the gate.
- The `delta <= 10` banked range is the regression; nothing new is claimed
  until it reproduces exactly.

## 5. What is NOT claimed here

Nothing about level-2 (the conic-tangent tower), nothing about World A,
nothing about `det_3`.  No paper edit is made before P1 passes.
