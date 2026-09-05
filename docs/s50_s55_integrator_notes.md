# Integrator verification notes — sessions 50, 51, 52, 54, 55

Each claim below was re-derived independently before the merge, by code sharing
nothing with the session that produced it.

## s50 — LMR

**Reproduced.**  The degree derivation `D = (e−d+1)+(k+3) = (d−1)(k+2)`, giving
`2n(n−1)`: confirmed at `n = 3,4,5,6` as `12, 24, 40, 60`.  The whole weight
family reproduces — `(19,7,2⁵)/12`, `(65,17,2⁷)/24`, `(151,31,2⁹)/40`,
`(289,49,2¹¹)/60` — with `|λ| = nD` and `ℓ(λ) = 2n+1` at every row.  The `n = 3`
row matches the paper's stated example, which was the pre-registered falsifier.

**Improved.**  The report establishes `rank Hess = 9` on `{per_3 = 0}` at six
sampled points and flags that both its implementations share a Hessian
*algorithm*.  That residual closes with no Hessian code at all.  Writing
`P = x_0·q`, the Schur complement plus Euler (`H_q A = 2∇q`, `AᵀH_qA = 6q`)
gives

    det H_P = −(3/2) · x_0^8 · per_3 · det(H_{per_3}),

so the rank is `≤ 9` on `{per_3 = 0}` **identically**, and `= 9` wherever
`det H_{per_3} ≠ 0`.  An independent `F_p` implementation confirms: generic rank
10, rank 9 at five points of the sheet, `dim(dual) = 7`.  P5 is an identity, not
six measurements.

**Corrected at merge.**  §2's inference from ambient dimensions to an
unreachable multiplicity is invalid: `ℓ(λ) = 9`, so plethysm stability makes this
a nine-variable computation and `a((65,17,2⁷),24) = 274`, in two minutes, under
two moduli, with the same code reproducing the paper's `n = 3` value of 6.
Independently obtained by an external reviewer via a Weyl alternant.

## s51 — `Λ⁵`

**Reproduced, and sharpened.**  The degeneracy-direction gate is the session's
decisive output, and it holds at a second degree with independent code.  At
`r = 10`, `d = 5`:

| quartic | Macaulay drop at `d = 5` |
|---|---|
| generic | **0** |
| `det_4` pencil | **0** |
| reducible `ℓ·c` | 36 |
| full ten-variable `x_0·per_3` | **86** |

At `d = 5` the determinant is *indistinguishable from generic* while the padded
permanent is already deeply degenerate — a stronger statement than the session's
`980` against `2141` at `d = 7`.  The direction failure is structural, not
marginal, and the gate correctly halted §4b before the expensive half ran.

## s52 — the `a = 1` census

**The argument is right and it retires my own recommendation.**  `i_det = 0` at
all 210 cells means `U_D = {0}`, so the orientation failure mode the `a = 1`
prior guards against is not instantiable and `D ≤ 0` is forced.  I endorsed that
prior; s52 refuted it correctly.

**And it killed the external reviewers' headline experiment.**  `(30,2^5)` at
`δ = 10` — named by two independent reviewers as the single best next test —
was measured here: `mult_det = mult_pad = mult_red = 1 = a`, `i_det = 0`,
`D = 0`.  Twelve more `δ = 10` `a = 1` cells with it.

**Closed from a third side.**  The successor proposal — find `sk(λ,4×δ) = 0`
with `m_pad > 0` — is correct logic but is what `results/occurrence_screen.md`
has run with the **symmetric** coefficient since s38: 2585 cells at `ℓ = 5`,
zero fires.  I computed `sk` at the three proposed `ℓ = 6` cells, calibrating
first against s38's peaked family (reproducing `sk = 8` at every degree):
`sk = 13, 78, 30` against `a = 1`.  All positive, and s38's data shows the gap
widening with degree, not closing.

## s54 — `R_5 ⊆ D_5`

Accepted as stated: leaning negative, not settled.  The two structural gains are
the ones that matter downstream — the order-1 exceptional image **fills** `D_5`
(dimension 50 of 50), so first determinant polars cannot isolate the boundary and
the higher-order Rees analysis is mandatory; and reducible quartics are singular
points of `D_5`, Zariski tangent saturating at 64.

Its citation correction is real and has been applied to `docs/washout_lemma.md`
and `docs/transfer_lemma.md`: s32 proves non-containment in the **image**, not
the **closure**.

## s55 — the equation census

**Reproduced.**  The floor argument, by two conditions: containment forces
`k ≥ min(6, r−2)`, non-vacuity forces `k ≤ r−3` since `ℓ(λ(k,4)) = k+3`.

| `r` | admissible `k` | lowest degree |
|---|---|---|
| 4–8 | **none** | the LMR module gives no equation at all |
| 9 | 6 | 24 |
| 10+ | 6 | 24 |

So at `r = 5, 6` — the entire measured region — LMR contributes nothing, and the
standing "24 versus `δ ≤ 9`" comparison was between different cells.

**Its Proposition D correction is right and has been applied.**
`docs/excess_singularity.md` extended the proposition to Hessian-rank conditions;
those run the *opposite* way (`det_4` rank 8, pad rank 9), which is exactly why
s50 works.  Narrowed to functionals monotone in `dim(S/J_F)_d`.

**Cross-session corroboration worth recording:** s55 predicted, before s50 ran,
that s50's control-4 remainder must be nonzero.  s50 found it nonzero.

## The organising fact these five establish jointly

There are two families of statistic at `n = 4` and they run in opposite
directions:

| family | `det_4` | `x_0·per_3` | separates |
|---|---|---|---|
| excess-singularity (Milnor corank, Macaulay drop, `Λ⁵` Fitting) | *less* degenerate | *more* degenerate | **wrong way** |
| dual-degeneracy (Hessian rank, LMR divisibility, conormal `δ_7`) | *more* degenerate | *less* degenerate | **right way** |

Three independent instances of the first row (Proposition D, s51 §4b, and the
`d = 5` re-derivation above); three of the second (s50, s55, and the external
conormal review, which arrived at the same taxonomy independently).  Every future
proposal should be classified into a row **before** any work is done on it.
