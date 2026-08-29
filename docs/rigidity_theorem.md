# RETRACTION NOTICE (session 16, 2026-08-29) — read before the body below

**The rigidity theorem stated in this document is RETRACTED.** Two
successive receiving-space hypotheses were falsified by pre-registered
engine tests:

1. **The det²-covariant slot (session 13, m = 3).** Falsified by
   f1X4_00 = −308,145,600 (gate-confirmed by f1X4_35). The three measured
   pencils C, R, T4 pin any slot element uniquely to Ψ = 2v − D, which
   predicts +434,851,200 at X4. The slot argument assumed each individual
   matrix element V^h_σ inherits det²-GL₂-covariance; h is a highest-weight
   vector for the ambient GL₉ Borel and neither H nor the scheme/σ choice
   preserves that covariance. This document's own caveat ("a MATRIX
   ELEMENT, not a naive covariant") named the risk that was realized.

2. **The 10-dim space of bidegree-(2,2) simultaneous-conjugation invariants
   (session 16 recovery fit).** Falsified by its own parameter-free
   prediction: the fit through C, R, T4, Q, P, X4, Xm3, Y2, Y3 plus the
   stabilizer zero required f1Y4_00 = +69,854,400; the engine returned
   **0**. The full system has rank 9 with augmented rank 10 — inconsistent.
   The violated relation is spread across nearly every point
   (6C + 30R − 18T4 + 12P − 9X4 + 2Y1 − 6Xm3 + 3Y2 + 3Y3 + 9Y4, residual
   −628,689,600 = 151200·(−4158)), so this is not an outlier artifact:
   **V^h_σ is not a simultaneous-conjugation invariant of the pencil.**
   (Sanity check passed inside the same computation: the relation C = Q is
   satisfied exactly, as it must be for H-conjugate points.)

**What this does NOT touch.** Every engine measurement stands, and so does
the programme's core: c((2,2,2),2) = 1, the second-point certificate
TOTAL_R = 1,152,144,000 at an H-inequivalent point, and the k = 2
ray-closure. None of those used a covariance assumption — they are direct
evaluations plus the Φ₁₈ product/parity algebra.

**What survives from the rigidity work.**
- The session-15 displacement-cancellation lemma (proved combinatorially,
  independent of any covariance claim), and its corollary that every
  displacement-infeasible pencil has all ten (2,2) invariants zero.
- The integrality theorem: V_σ(N) = W(σ)·Ψ(N) is impossible at X4, since
  W(id) = 2⁵·3³·5²·7·719 carries the prime 719 alone.
- The empirical universality itself, now WITHOUT an explanation: the full
  W-table is identical at C, R, Q (three balanced two-transvection points,
  two H-classes) and at T4 — four points, every W-class — while X4, Xm3
  give genuinely different values and Y2, Y3, Y4 give exact zeros.

**What is now OPEN (previously claimed).**
- TOTAL_G = 1,152,144,000: this prediction rested on the refuted fits and
  is **withdrawn**. G has never been run; its value is unknown.
- Any cone-wide law for V^h_σ. The functional is a bidegree-(2,2)
  polynomial in the 18 direction coordinates (this much is forced by the
  counting lemma's t = (2,2)), living in a space of dimension up to 2025 —
  not determinable by ~2h-per-point sampling. A different route is needed.

**Leads for the next attempt** (patterns in the measured zeros, unexplained):
  - A ∝ I or B ∝ I (a row-wise stabilizer direction) ⟹ 0 (Y1, Y2, Y3).
  - Rank-1 pencils ⟹ 0 (P) — previously derived from the slot, now needing
    an independent proof.
  - Y4 = (diag(1,1,0), diag(0,0,1)): complementary projections, AB = 0,
    A + B = I ⟹ 0. A third, unexplained vanishing mechanism.
  - Arithmetic: every measured value is 151,200 × an integer, cofactors
    719 (C/R/T4/Q), −2038 (X4), 5907 (Xm3).

---

# The rigidity theorem (session 15 — math only, no engine runs)

Companion to docs/rigidity_formulation.md (the framework and the session-14
determination record) and results/results_T4.md (the engine data). All
machine checks referenced here were run and passed this session
(analysis/wk3_s15_psilocus.py and inline verifications).

## Statement

Let W = C²ₐ⊗gl₃ᵇ be the balanced direction cone, N = e₁⊗A + e₂⊗B, and for
an ambient λ′-HWV h and subproblem σ let V^h_σ(N) be the factored scheme
evaluation at (I+N)·det₃. Set

    Ψ := 2u₁ − 4u₂ − D = 2v − D,  where
    u₁ = tr(A²)tr(B²) − tr(AB)²,  u₂ = tr(A²B²) − tr((AB)²),
    D  = (trA·trB − trAB)² − ((trA)²−trA²)((trB)²−trB²),  v = u₁ − 2u₂.

THEOREM (rank one on the balanced cone).  For every h in the 3-dimensional
ambient λ′-HWV space and every σ,

    V^h_σ(N) = W^h(σ) · Ψ(N)      for all N ∈ W,

with scalar tables W^h. In particular the evaluation composite
Sym⁴W → (ambient multiplicity space)* has rank 1, image span{Ψ}.

## Proof of the pinned cases (complete)

Two ingredients, both machine-verified:

1. (Session 13, branching computation with brute-force validation and a
   transpose-side double check.) Every V^h_σ lies in the 3-dimensional
   covariant slot span{u₁, u₂, D} — the (ρ=(2,2), triv-GL₃ᵇ) isotypic
   block, the unique nonzero block of the P_H-equivariant receiving space.
2. (Session 14 engine data.) The evaluation matrix of (u₁,u₂,D) at the
   three pencils C = (E₂₁,E₁₂), R = (E₀₀,E₁₁), T4 = (diag(1,1,0),
   diag(0,1,1)) is [[−1,−1,1],[1,0,1],[3,0,5]] with determinant 2 ≠ 0 —
   the three measured pencils are INDEPENDENT points of the slot's dual.

Hence any slot element is uniquely determined by its values at C, R, T4,
and the unique interpolant through equal values (1,1,1) is
(c_{u₁}, c_{u₂}, c_D) = (2, −4, −1), i.e. Ψ = 2v − D exactly.

Consequently, for every (h, σ) whose values at the THREE pencils are
measured and equal to W^h(σ)·(1,1,1), the identity V^h_σ = W^h(σ)·Ψ holds
on ALL of W. This is the case for:

  (h₁, σ ∈ id-class):    C, R, T4 all measured (+108,712,800·1 each) ✔
  (h₁, σ ∈ (0 2)-class): C, R, T4 all measured (−476,884,800·1 each) ✔

## Status map for the remaining cases (confinements + completing runs)

The same two ingredients confine every other case to an explicit subspace:

  (h₁, small class), (h₁, 3-cycle class): measured at C and R (equal) →
      confined to the plane {2c₁ + c₂ = 0} ∋ Ψ.  One T4 value each
      completes the interpolation. PRE-REGISTERED completing runs:
          f1T4_01 = −21,772,800      f1T4_03 = +301,870,800
  (h₂, id), (h₃, id): measured at C and T4 (equal) → confined to the
      plane {4c₁ + c₂ + 4c₃ = 0} ∋ Ψ.  One R value each completes.
      PRE-REGISTERED: f2R_00 = +78,850,800     f3R_00 = +17,388,000
  (h₂/h₃, other σ): slot-confined only (no engine data); pinned by any
      three-point sweep if ever needed.

Four ~30–100-min engine runs therefore convert the theorem from
"proved on the measured classes" to "proved for scheme 1 in full and for
schemes 2/3 at the id class". (The remaining scheme-2/3 σ-classes are
corollaries once their tables W^{h₂,₃} are defined by any single point,
IF one accepts the σ-uniformity that scheme 1 exhibited; as pure
mathematics they stay open until measured or derived.)

## Why the suggested a-priori route cannot work as stated (machine-proved)

Vanishing on proportional pencils (B = tA, general symbolic A) and on both
rank-1-locus pencil families (A = ab₁ᵀ, B = ab₂ᵀ and the right-handed
mirror) annihilates ALL THREE slot generators u₁, u₂, D identically
(symbolic zero, fully general). These conditions define the slot (its
det²_{GL₂}-covariance) — they cannot cut m = 3 to 1. Any a-priori proof
must use finer structure of Φ₄ (e.g. the τ-coset of H, or the copy-level
combinatorics); the interpolation proof above sidesteps this entirely.

## The displacement-cancellation feasibility lemma (new, with proof)

LEMMA. For any balanced substitution with supports supp(A), supp(B) ⊂
{0,1,2}² (targets×sources; coefficients irrelevant), the weight-support
(content) feasibility of the λ′-evaluation — BEFORE coefficient
cancellation — holds iff there exist a 2-multiset S₁ ⊆ supp(A) and a
2-multiset S₂ ⊆ supp(B) whose four displacement vectors e_target −
e_source sum to zero in Z³.

Proof. Row sums of the demanded content (24,18,18 by rows; 20 copies of
degree 3, one leg per row before conversion) force exactly t₁ = 2 row-1
conversions and t₂ = 2 row-2 conversions. Fixing the conversion multisets
S₁, S₂, the per-position column marginals form a 3×3 nonnegative integer
matrix with all row sums 20; its column sums are 20 + Σ displacements.
By König/Birkhoff–von Neumann (integral version), a nonnegative integer
matrix with equal row and column sums is a sum of permutation matrices —
i.e. realizable by a choice of 20 det₃-monomial copies — iff the column
sums also equal 20, which is exactly Σ displacements = 0. Conversion-to-
copy assignment is unobstructed since the marginal counts include the
converted copies. ∎

Corollaries: D, A, B, E, F infeasible structurally (e.g. D = {(0,0)}ᴬ,
{(2,1)}ᴮ: A-side displacements are 0, B-side cannot cancel 2(e₂−e₁));
the 15/81 sweep result is derivable by inspection; feasibility depends
only on supports. Validated against the exact content-DFS on all named
points (C, R, P, D, T4, G, single transvections).

## The Ψ-locus over the {0,1} cone (dichotomy FALSE) and the mod-4 lemma

Exhaustive enumeration (255,163 displacement-feasible {0,1} pencil pairs
of 262,144): Ψ takes 48 distinct values in [−40, 53]. The natural-stratum
dichotomy Ψ ∈ {0,1} is FALSE far beyond coefficient scaling.

LEMMA (mod 4). For integer matrices, Ψ ≡ 0 or 1 (mod 4), with the class
determined by the parity of s = trA·trB − tr(AB): Ψ ≡ 2s − s² (mod 4).
Proof: (trM)² ≡ tr(M²) (mod 2) gives p = (trA)²−trA² and q even, so
pq ≡ 0 (mod 4) and D ≡ s² (mod 4); u₁ ≡ trA²trB² + trAB ≡ s (mod 2), so
2u₁ ≡ 2s (mod 4); Ψ ≡ 2s − s² (mod 4), which is 0 for s even, 1 for s
odd. ∎  (Consistent with all 48 observed values.)

Also notable: Ψ = 0 occurs at non-proportional feasible pencils (e.g.
(diag(1,1,0), E₂₂)) — predicted cancellation-zeros of a new kind.

## THE DECISIVE PRE-REGISTERED RUNS (designed, NOT run this session)

Both points verified content-feasible (exact post-cancellation DFS) and
SAT-live (wedge level, point and subproblems 00, 05); input sets
f1X4_00..35 and f1Xm3_00..35 are banked. First off-the-Ψ=1-locus tests:

  X4 = {x₃+=x₀, x₇+=x₂, x₈+=x₁}   (3 transvections, 14 monomials, Ψ = 4):
      V_00 = +434,851,200      V_05 = −1,907,539,200
      TOTAL_X4 = 4 × 1,152,144,000 = 4,608,576,000
  Xm3 = {x₃+=x₂, x₄+=x₁, x₇+=x₁, x₈+=x₀}  (4 transvections, 17 monomials,
      Ψ = −3 — a SIGN-FLIPPED table, nothing like it yet observed):
      V_00 = −326,138,400      V_05 = +1,430,654,400
      TOTAL_Xm3 = −3 × 1,152,144,000 = −3,456,432,000

Any hit is dramatic confirmation of the quartic law; any miss falsifies
the theorem off the unit locus. Standing implied predictions unchanged:
TOTAL_G = 1,152,144,000; coefficient scaling (A,2B) ↦ ×4.
