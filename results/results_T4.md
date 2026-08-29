# Session 14: the rigidity determination (T4 + cross-scheme runs)

Date 2026-08-28. Engine dp2g evalopts (checkpointed), exact int64; every
value below landed AFTER its outcome map was committed (pre-registration
commits 8e9f51e and 7af9d09).

## Engine record (all final states 1)

| run      | point | scheme | sigma | VALUE        | role |
|----------|-------|--------|-------|--------------|------|
| f1T4_00  | T4    | 1      | 00    | +108,712,800 | ratio_id = 1 |
| f1T4_35  | T4    | 1      | 35    | +108,712,800 | GATE = 00 (pre-rho AND post-omega partner): PASSED |
| f1T4_05  | T4    | 1      | 05    | −476,884,800 | ratio_(02) = 1: uniformity |
| f2C_00   | C     | 2      | 00    |  +78,850,800 | kappa_2 = 1043/1438 |
| f3C_00   | C     | 3      | 00    |  +17,388,000 | kappa_3 = 115/719 |
| f2T4_00  | T4    | 2      | 00    |  +78,850,800 | LS1 prediction HIT exactly |
| f3T4_00  | T4    | 3      | 00    |  +17,388,000 | LS1 prediction HIT exactly |

T4 = {x3+=x0, x4+=x1, x7+=x1, x8+=x2}, pencil (diag(1,1,0), diag(0,1,1)) —
a third pencil class (contains invertible elements; not H-conjugate to C's
cyclic or R's diagonal-units class). Point symmetry pi = (0 2)(3 8)(4 7)(5 6)
sign +1, rho = (0 2); extended orbits (with the scheme automorphisms):
8 orbits, sizes (2,8,8,2,4,4,4,4). SAT screen: live at point and all run
sigmas. Input integrity: f1T4 verified distinct from f1R at file level and
canonically identical to an independent regeneration.

## VERDICT

1. **Scheme-1 line measured: Psi ∝ 2v − D** (v = u1 − 2u2, D the pencil
   discriminant; normalization Psi(C-pencil) = 1). Selected by the
   pre-registered O3 map at rho = 1; uniform across both tested W-classes.
2. **Strong rigidity (rank 1) across the ambient multiplicity space:**
   schemes 2 and 3 evaluate through the SAME line — cross-point ratios
   V^h(T4)/V^h(C) = 1 = Psi(T4)/Psi(C), both exact. Every functional
   V^h_sigma(N) = W^h(sigma) · Psi(N) on balanced pencils.
3. **Integrality theorem: the three ambient HWVs are pairwise-independent
   functionals** (kappa_2·W((0 2)) = −248695423200/719 ∉ Z, and 719 ∤
   115·476884800 — sigma-table proportionality is impossible). The amb = 3
   basis is honest; the compression to one covariant is a property of the
   balanced-pencil restriction, not of a degenerate basis.
4. Everything banked is explained by Psi = 2v − D: Psi(C) = Psi(R) =
   Psi(T4) = 1 (universality of totals and tables across three pencil
   classes), Psi ≡ 0 on rank-1 pencils (P's exact zeros — doubly derived),
   and TOTAL_G = Psi(G)·TC = 1,152,144,000 (standing implied prediction,
   still deliberately un-run).
5. Standing falsifiers (cheap, any time): coefficient-2 pencil must scale
   all values by 4; any new balanced point N must give
   TOTAL(N) = (2v−D)(N) · 1,152,144,000.

Prediction ledger: gate 00=35 HIT; T4-05 = −476,884,800 HIT; f2T4_00 =
+78,850,800 HIT; f3T4_00 = +17,388,000 HIT — every pre-registered
prediction of the session landed exactly; the one open map entry (rho)
selected O3 = 1 from within the pre-written inversion formula.

The theorem left to prove (math, no engine): the composite
Sym⁴W → (3-dim ambient)* has rank 1 on the balanced cone with image
span{2v − D} — all measured structure is now an exact target.

---

# SESSION 16 ADDENDUM: the theorem meets its off-locus probe and FAILS

Date 2026-08-29. All values engine-exact, all predictions pre-registered at
commit 832cf3d before any run.

## Completing runs — 4/4 HIT (the theorem's measured classes close)

| run     | VALUE        | predicted    | verdict |
|---------|--------------|--------------|---------|
| f1T4_01 |  −21,772,800 |  −21,772,800 | HIT |
| f1T4_03 | +301,870,800 | +301,870,800 | HIT |
| f2R_00  |  +78,850,800 |  +78,850,800 | HIT |
| f3R_00  |  +17,388,000 |  +17,388,000 | HIT |

With these, scheme 1 is measured at three independent pencils in every
W-class, and schemes 2/3 at the id class: V = W(σ)·Ψ holds **as an
interpolation identity through C, R, T4**.

## X4 — the off-locus test: PREDICTION MISSED (theorem falsified off the unit locus)

    f1X4_00 = −308,145,600     (predicted +434,851,200 = 4·W(id))
    f1X4_35 = −308,145,600     GATE PASSED (point symmetry + scheme
                                automorphism partner: identical)

Input integrity verified independently before drawing conclusions: the
f1X4 input file canonically matches a fresh regeneration, and its monomial
list matches a separate sympy derivation of det₃∘(I+N).

Ratio V₀₀(X4)/W(id) = −2038/719, not 4 — and not any value achievable by
an element of span{u₁,u₂,D} that also takes the measured values at C, R,
T4 (those three pin the slot element uniquely to Ψ, and Ψ(X4) = 4).
**Therefore the receiving space is strictly larger than the session-13
3-dimensional slot.**

## Diagnosis

The slot argument assumed every individual V^h_σ is a det²-GL₂-covariant
of the pencil. But h is a highest-weight vector for the AMBIENT GL₉ Borel;
neither H nor the choice of scheme/σ preserves that covariance. (The
formulation doc flagged exactly this — "a MATRIX ELEMENT, not a naive
covariant" — and the risk was realized.) The branching arithmetic of
session 13 is not thereby refuted; its APPLICATION to individual matrix
elements is.

## Integrality theorem (proved, no runs): factorization fails at X4

W(id) = 2⁵·3³·5²·7·**719**, and 719 divides no other entry's cofactor.
If V_σ(X4) = W(σ)·Ψ_true(X4) with Ψ_true(X4) = −2038/719, then
V_(0 2)(X4) = 971,891,222,400/719 ∉ ℤ. The engine returns integers, so
**V_σ(N) = W(σ)·Ψ(N) cannot hold at X4**: σ-structure and N-dependence
entangle there. (Pre-registered before f1X4_05 landed.)

## Recovery: the true functional, and what survives

Refit over the full 10-dim space of bidegree-(2,2) pencil invariants
(analysis/wk3_s16_fit.py). Constraints: six engine points (C, R, T4, Q, P,
X4) → rank 5; plus one FREE structural constraint — A = B = I is a
stabilizer direction (I+N ∈ H ⟹ substituted form is det₃ itself ⟹ 0 by the
counting lemma) → rank 6, four free parameters. Displacement-infeasible
pencils add nothing: every one of the 5,958 has all ten invariants zero
(a corollary of the session-15 lemma worth recording).

SURVIVING PREDICTION: **G is parameter-free at +108,712,800**, so
TOTAL_G = 1,152,144,000 stands — now forced by the enlarged space rather
than by Ψ. The maximum attainable rank on the feasible {0,1} cone is 9
(one invariant direction is invisible there), so four more measurements
determine the functional completely on that cone: Xm3_00 (running) plus
three designed cheap points, each Ψ_old = 0 (so each is also an
independent refutation test):

    Y2 = {x₃+=x₀, x₆+=x₀, x₇+=x₁, x₈+=x₂}      8 monomials
    Y3 = {x₃+=x₀, x₄+=x₁, x₅+=x₂, x₆+=x₀}      8 monomials
    Y4 = {x₃+=x₀, x₄+=x₁, x₈+=x₂}             10 monomials

Inputs banked (f1Y2/f1Y3/f1Y4_00..35). f1Xm3_05 deprioritized in favour of
these.

## Session-16 round 2: the refit closes to one free parameter

Engine (all σ = 00, scheme 1):

    f1X4_35  = −308,145,600   GATE PASSED (= f1X4_00; X4 value is real)
    f1Xm3_00 = +893,138,400   (old-theory prediction −326,138,400: MISSED —
                               second independent refutation)
    f1Y2_00  = 0  (final states 0)
    f1Y3_00  = 0  (final states 0)

Refit constraints now: C, R, T4, Q, P, X4, Xm3, Y2, Y3 (engine) + the free
stabilizer zero at (I, I) → **rank 9 of 10, consistent, ONE free parameter**,
and rank 9 is the maximum attainable on the feasible {0,1} cone (one
invariant direction is invisible there). Hence the σ=00 functional is now
DETERMINED on the whole feasible cone; the residual parameter τ₀ moves only
the invisible direction and changes no prediction there.

Striking arithmetic: every measured value is 151,200 × an integer, with
W(id) = 151200·719, V(X4) = 151200·(−2038), V(Xm3) = 151200·5907 — the
prime 719 organizes the whole table.

### PRE-REGISTERED (logged before the value landed)

  **f1Y4_00 = +69,854,400  = 151200 · 462**  — parameter-free consequence of
  the refit, and the validation test of the recovery. A hit confirms the
  enlarged-space fit and hands us the true functional on the feasible cone;
  a miss means even the bidegree-(2,2) conjugation-invariance assumption
  fails, and the receiving space is larger still.

  **G remains parameter-free at +108,712,800** in the refit, so
  TOTAL_G = 1,152,144,000 continues to stand — it has now survived the
  collapse of the theory that first predicted it.
