# The rigidity theorem: formulation (session 13)

Status: FORMULATION + the n=3 covariant-space count (this session). The
theorem's empirical content (universality of the W-table across live
H-classes, 11/11 + 36 + 2) is banked in results_R.md; this document fixes
the precise statement whose proof would force it, and computes the
dimension that decides which statement is available.

## Objects

Ambient: G = GL₉ on cubic forms in the entries of A ∈ C³ᵃ⊗C³ᵇ (x_{3i+j} =
A_{ij}); H = stab(det₃) = S(GL₃ᵃ×GL₃ᵇ)/C^× ⋊ ⟨τ⟩ acting by A ↦ uAv, τ =
transpose. λ′ = (8,8,8,6⁶), δ = 20; h₁, h₂, h₃ = the three scheme HWVs
(hwv1–3); amb(λ′,20) = 3 (MN census, 627 outer partitions / 94,167
power-sum classes — session 12), so span{h₁,h₂,h₃} ⊆ the FULL 3-dim
ambient λ′-HWV space, equality (their independence) unverified.

Balanced directions: W := Hom(row-0 variables, rows-1,2 variables)
≅ C²ₐ ⊗ (C³ᵇ ⊗ C³ᵇ*), written N = e₁⊗M⁽¹⁾ + e₂⊗M⁽²⁾ with M⁽ʳ⁾_{ja} =
coefficient of x_{0a} added into x_{ra+...}: target column j ← source
column a in target row r. (C: M⁽¹⁾ = E₂₁, M⁽²⁾ = E₁₂ — cyclic pencil.
R: E₀₀, E₁₁ — diagonal. P: E₀₀, E₀₀ — rank-1.)

P_H := the subgroup of H⁰ whose action preserves the construction
N ↦ (I+N)·det₃, i.e. u in the parabolic P₁ ⊂ GL₃ᵃ stabilizing the row-0
line, v ∈ GL₃ᵇ free; Levi L = (GL₁×GL₂)ₐ × GL₃ᵇ (mod the det u·det v = 1
identification). τ does NOT normalize the construction (it swaps the
row-flag to a column-flag), so the covariant analysis lives over P_H, not H
— the H-statement is recovered at the end because the three tested pencil
classes are already separated by H-conjugacy (rule 8's invariant).

## The functional and its degree

For an ambient λ′-HWV h and a subproblem σ = (σ₆,σ₇), the factored
evaluation defines V^h_σ(N) := V_σ evaluated at (I+N)·det₃. Content
arithmetic (the session-8 counting lemma): row-0 demand is 24 = 6·3 + 2·3,
each of the 20 copies supplies exactly one row-0 leg unsubstituted, and
each substituted leg converts exactly one lower-row leg into a row-0 leg;
hence every completing path uses EXACTLY 4 substituted legs and

    V^h_σ : W → C is homogeneous of degree 4:  V^h_σ ∈ (Sym⁴ W)*.

It is a MATRIX ELEMENT, not a standalone covariant: V^h_σ(N) =
⟨ ℓ_σ ∘ h , Φ₄(N) ⟩ where Φ₄: Sym⁴W → Sym²⁰(Sym³C⁹) is the (I+N)-expansion
component and ℓ_σ the subproblem contraction functional. The full
evaluation TOTAL(N) = Σ_σ (folded signs) V^h_σ(N) is the case of interest;
per-σ values are the refined data.

Grading bookkeeping (a-side torus): the degree-4 slice carries a-weight
α = (24, 20−t₁?, …) — precisely, with t = (t₁,t₂), t₁+t₂ = 4, the number
of substituted legs targeting rows 1, 2: a-content (24, 20−t₁, 20−t₂)
after reordering; b-content β = (20,20,20) shifted by the four
(source−target) column moves. Both sides stay within the ≤3-row window —
the exact (α, β) support list is computed below.

## The theorem target (two-tier)

**Tier 1 (universality as rigidity of the covariant slot).** Let

    m := dim Hom_L( Sym⁴W ⊗ (central-character match) , (Res_{P_H} S_λ′(C⁹))^{U_{P_H}} )

(the n=3 covariant-space dimension; U-invariants of an irreducible are the
L-irrep of the same highest weight, so the right side decomposes by the
a-side branching α ↦ e₀^{α₁} ⊗ S_{(α₂,α₃)}(C²) with the Kronecker-type
multiplicities m(α,β) of S_αᵃ⊗S_βᵇ in S_λ′(C³⊗C³)).

If the α₁ = 24 block of this Hom-space is 1-DIMENSIONAL, then every
functional V^h_σ (any scheme h, any σ) is a scalar multiple of ONE
covariant Ψ: V^h_σ(N) = W^h(σ)·Ψ(N) — the empirical universality
(W-table point-independence, P's rank-1 vanishing as a property of Ψ,
rel-only law as a property of W alone) becomes a THEOREM, with the scalars
W^h(σ) exactly the banked table for h = h₁.

If the block has dimension d > 1, universality is NOT formal: the theorem
becomes a RANK statement — the composite Sym⁴W → C^{3×36} of all
(scheme, σ) matrix elements has rank 1 on the balanced cone — and needs
the empirical rank probe (scheme-2/3 evaluations at C and R; h2C/h3C
banked, factorable by wk3_s12_genD) or the finer P_H-analysis to close.

**Tier 2 (attainment).** Ψ ≠ 0 on the live classes and Ψ = 0 on rank-1
directions. Already certified by engine data (C, R nonzero; P exactly 0);
a closed form for Ψ (candidate: an L-invariant of Λ²N — degree-4 in N,
quadratic in the 2×2 minors of the pencil) upgrades P's vanishing from
engine fact + conjecture to lemma.

## The count (computed this session — see analysis/wk3_s13_covcount.py)

Pipeline, all exact:
1. Pin W's L-module structure including the e₀-character twist by direct
   sympy transformation of (I+N)·det₃ under sampled (u,v) ∈ P_H.
2. Decompose Sym⁴W into L-irreps (character algebra; Cauchy over the C²ₐ
   factor: Sym⁴(X⊗Y) = ⊕_{ρ⊢4} S_ρ(X)⊗S_ρ(Y), Y = gl₃ᵇ ⊗ twist).
3. For each L-irrep, the matching (α, β) and the multiplicity m(α,β) of
   S_αᵃ⊗S_βᵇ in S_λ′(C³⊗C³) via Kostant alternation over S₃ (a-side) with
   weight-space b-decompositions K_{μ,β} = Σ_{ηⁱ⊢μᵢ} c^{λ′}_{η¹η²η³}
   c^β_{η¹η²η³} (iterated Littlewood–Richardson, lrcalc).
4. Validation gates: (i) small-case brute force (S_λ(C²⊗C²), λ ⊢ 4, full
   sympy expansion) must match the alternation machinery exactly;
   (ii) dimension bookkeeping Σ_α,β m(α,β)·dims = dim S_λ′(C⁹) is too big
   to check directly — instead check on the medium case λ ⊢ 6 on C³⊗C³;
   (iii) the known anchor amb(λ′,20) = 3 is NOT re-derivable from this
   pipeline (different object) — no circularity.

RESULT (n=3, all machine-verified 2026-08-27):

    m = 3,   concentrated in a SINGLE branching slot:
    mult( S_(24,18,18)(C³ᵃ) ⊗ S_(20,20,20)(C³ᵇ) , S_λ′(C³⊗C³) ) = 1
    (validated from the transpose side: mult((20,20,20),·) has exactly three
    betas — (20,20,20), (22,20,18), (24,18,18) — each multiplicity 1),
    times the multiplicity 3 of the (ρ=(2,2), trivial-GL₃ᵇ) constituent of
    Sym⁴W (its dimension audit: Σ constituents = C(21,4) = 5985 exact).
    The α = (24,19,17) and (24,20,16) blocks pair to ZERO.

Consequences (each machine-checked):

1. **Forced covariant shape.** Every V^h_σ is a det²_{GL₂} ⊗ triv_{GL₃}
   covariant of the pencil (A,B) = (M⁽¹⁾,M⁽²⁾) — an element of the 3-dim
   space span{u₁, u₂, D}:
       u₁ = tr(A²)tr(B²) − tr(AB)²
       u₂ = tr(A²B²) − tr((AB)²)
       D  = (trA·trB − tr(AB))² − ((trA)²−trA²)((trB)²−trB²)
   (independence det = 2; SL₂-mix invariance verified; note (trAtrB−trAB)²
   alone is NOT in the slot — it fails proportional-pencil vanishing — the
   discriminant completion D is the correct third generator; caught by the
   machine check, hand algebra had it wrong.)
2. **Rank-1 vanishing is a LEMMA.** det²-covariants vanish on proportional
   pencils identically ((A,cA) is a det-0 GL₂-transform of (A,0)); hence
   V^h_σ ≡ 0 at every rank-1 point — P's exact engine zeros are explained
   by pure representation theory; session-12's rank-1 conjecture is proved
   at the covariant level (engine data = attainment confirmation).
3. **Balanced legs forced.** The vanishing of the (24,19,17)/(24,20,16)
   blocks means only the t = (2,2) substituted-leg distribution (two per
   lower row) survives — the functionals automatically antisymmetrize
   through Λ²-pairs across the two rows.
4. **Universality NOT formally forced** (m = 3 > 1): it is a genuine rank
   statement. The C = R value equality confines every actual functional to
   the 2-dim consistent subspace span{v = u₁−2u₂, D} (values at the
   classes: (u₁,u₂,D): C (−1,−1,1), R (1,0,1), P (0,0,0), G (−1,−1,1),
   T4 (3,0,5); v: C,R,G = 1, T4 = 3).
5. **Free prediction (logged before any G engine run exists):** every
   consistent covariant takes the same value at G as at C ⟹ the G-point
   engine totals must reproduce the W-table exactly (TOTAL_G =
   1,152,144,000), despite G's 2.4× cost — universality at G is implied by
   m-structure + C = R alone, so a G run is a CONSISTENCY test, not a
   discriminator.
6. **The discriminating probe** (next engine session): the four-transvection
   point T4 = {x₃+=x₀, x₄+=x₁, x₇+=x₁, x₈+=x₂}, pencil
   (diag(1,1,0), diag(0,1,1)) — weight-FEASIBLE, 11 monomials (C-sized
   grind). (v,D)(T4) = (3,5) vs (1,1) at C: the engine total at T4, against
   the W-table normalization, measures the actual line C·(c_v·v + c_D·D)
   and decides rigidity: TOTAL_T4/TOTAL_C = (3c_v + 5c_D)/(c_v + c_D).
   Scheme-2/3 evaluations at C (banked h2C/h3C contracts, factorable)
   separately measure whether different (h, σ) select different lines —
   the full rank probe.

## n = 4, behind it

The framework transplants verbatim: W₄ = C³ₐ⊗(C⁴ᵇ⊗C⁴ᵇ*), P_H the row-0
line parabolic in GL₄ₐ × GL₄ᵇ, and the forced degree in N and the ray
weight λ′₄ come from det₄'s counting arithmetic. Two inputs are NOT yet in
the results bank and gate the numeric count: (a) e(det₄) (the fundamental
invariant degree — conjecturally 2n² = 32 by the n=3 pattern, open), and
(b) the first deficit weight of det₄ and its k=1 ray weight λ′₄ =
(first-deficit) + (e(det₄)·4/16)·1¹⁶. Given those, the same pipeline
computes the n=4 covariant dimension; the a-side becomes GL₁×GL₃ (row-0
line in C⁴ₐ) and the forced substituted-leg count follows from the same
row-0 demand−supply subtraction. The structural pieces that do NOT depend
on the unknowns (W₄'s L-structure, Sym^d(W₄) decompositions for small d)
are implemented in the same script under n=4 flags.
