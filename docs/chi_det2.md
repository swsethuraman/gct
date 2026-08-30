# χ ↔ det²: closing (or breaking) step (iii) of the totals law
Session 22 (2026-08-30). Math/symbolic only; **no engine run, and none required.**

Target: step (iii) of the proof route recorded at the end of
`docs/i6_identification.md` and as Question 7.2 of `paper/det3-conductor.tex`.
Steps (i) [TOTAL is bidegree (2,2)], (ii) [TOTAL is constant on Q·u·H up to χ,
and the coset is the H-orbit of the net as a subspace] and (iv) [if χ = det²
then uniqueness forces TOTAL = c·Ψ] are proved. Step (iii) — the transpose
coset and the slot dictionary — is not.

---

# PART I — PRE-REGISTRATION
*(written and committed before any of this session's computations were run;
the derivation below was carried out by hand first, and is logged here as a
prediction with named falsifiers, not as a result.)*

## What is being asked, stated precisely

Let V = M₃ = C⁹ with coordinates x_{ij} (i = row, j = column), f = det₃,
H = Stab(f) ⊂ GL(V), and W ⊂ V the 6-dimensional coordinate subspace of
session 17, with Q = Stab(W) the parabolic (Levi GL₃×GL₆) stabilising the
highest-weight line of h₁, λ′ = (8,8,8,6⁶). For a balanced direction
N = e₁⊗A + e₂⊗B write u_N for the corresponding unipotent, Γ_N = u_N⁻¹(W),
and Γ_N^⊥ = {[v; Av; Bv] : v ∈ C³} for the net (tensor slabs (I, A, B)).

Step (ii) gives: if u_{N′} = q·u_N·s with q ∈ Q, s ∈ H, then
TOTAL(N′) = χ(q)·TOTAL(N), with χ(q) = det(q|_{V/W})⁸·det(q|_W)⁶.

**Two things must be checked.**

* **(1) The slot dictionary.** The tensor of the net has three slots: the slab
  index (row of Y), the parameter v, and the column index of Y. H acts on V by
  X ↦ aXb and by the transpose; the net moves accordingly, and must then be
  renormalised back to graph form (I, A′, B′). The question is which slot each
  group does, whether the renormalisation is exactly a slot-2 (parameter)
  change, and whether χ equals the factor by which Ψ transforms.
* **(2) The transpose coset.** H = H⁰ ⊔ H⁰τ with τ : X ↦ Xᵀ. τ acts on the net
  by Y ↦ Yᵀ, i.e. it **swaps slots 1 and 3**. Two things can go wrong: τ could
  contribute an extra character to χ, and I₆ (hence Ψ) could pick up a sign
  under an odd permutation of the tensor slots, since the degree-6 invariant
  space is one-dimensional and S₃ therefore acts on it by a character.

## PREDICTIONS (logged before computing)

**P1 — the structural form of χ.** Because 8 = 6 + 2,

    χ(q) = det(q|_{V/W})⁸ · det(q|_W)⁶ = det(q)⁶ · det(q|_{V/W})² .

With u_{N′} = q u_N s and s = t⁻¹ ∈ H, one has q = u_{N′} t u_N⁻¹, so
det(q) = det(t) because both u's are unipotent. For t ∈ H⁰ (X ↦ aXb with
det a · det b = 1) det(t) = (det a det b)³ = 1; for the transpose coset
det(t) = −1 (three off-diagonal 2-cycles). Either way **det(t)⁶ = 1**, so

> **PREDICTION P1:  χ(q) = det(q|_{V/W})² — a perfect square, always, with no
> contribution from the transpose coset.**

This is the same parity argument that closed the k = 2 ray (det₉ is −1 on the
transpose coset but the exponent there was even too). It is the reason to
expect a *square* character at all, and it ties the exponent 2 to the gap
8 − 6 = 2 in λ′, not to anything about tensors.

**P2 — the dictionary.** V/W is 3-dimensional and (V/Γ_N)* = Γ_N^⊥ = the net,
with the u_N-transported basis equal to the canonical parametrisation by v.
So det(q|_{V/W}) is the determinant of the induced map on the net's **parameter
space — tensor slot 2**. Predicted transformation, for t given by (a, b) with
α = a^{-T}, β = b^{-T}:

    S′_k = Σ_{k′} α_{kk′} βᵀ S_{k′},    P := S′₀ = βᵀ(α₀₀I + α₀₁A + α₀₂B),
    A′ = S′₁P⁻¹,  B′ = S′₂P⁻¹,   det(q|_{V/W}) = det(P)⁻¹ .

> **PREDICTION P2:  χ = det(P)⁻².** In particular b acts by conjugation
> (A ↦ βᵀAβ^{-T}) with χ = 1, and a acts by slab mixing with the
> (I + tA)⁻¹-renormalisation of session 18, with χ = det(P)⁻².

**P3 — Ψ transforms by exactly the same factor.** Ψ = −I₆^prim(I,A,B) is a
semi-invariant of character det² in *each* slot. Slots 1 and 3 receive α and βᵀ,
contributing (det α det β)² = (det a det b)⁻² = 1; the renormalisation is a
slot-2 action by P⁻¹, contributing det(P)⁻². So

> **PREDICTION P3:  Ψ(A′,B′) = det(P)⁻²·Ψ(A,B) = χ·Ψ(A,B), identically.**

**P4 — the transpose is harmless on the Ψ side too.** τ swaps slots 1 and 3.
S₃ acts on the 1-dimensional degree-6 invariant space by a character.
Predicted: **the trivial one**, so that Ψ(A′,B′)·det(P)² = +Ψ(A,B) for the
transposed net as well. Reason to expect it: if the character were the sign
character, I₆ would vanish identically on every tensor symmetric under
swapping slots 1 and 3, and the family of such tensors in graph form (row 0 of
A = e₁ᵀ, row 0 of B = e₂ᵀ, row 2 of A = row 1 of B) is 9-dimensional and not
visibly degenerate — I expect Ψ ≢ 0 on it.

**P5 — the verdict.** If P1–P4 hold, then TOTAL and Ψ satisfy the *same*
equivariance identity, TOTAL is bidegree (2,2) by step (i), and Proposition
"Uniqueness" (equivariance alone pins the bidegree-(2,2) space to ⟨Ψ⟩) forces

    **TOTAL(N) = Ψ(N) · 1,152,144,000**,   the constant fixed at C.

> **PREDICTION P5: step (iii) closes and the totals law becomes a theorem.**

## FALSIFIERS, fixed in advance

Each of these is a publishable negative and will be reported as the headline if
it occurs, not buried:

* **F1.** χ ≠ det(q|_{V/W})² for some explicit q — kills P1, i.e. the parity
  argument is wrong or the Levi character convention of session 17 is wrong.
* **F2.** det(q|_{V/W}) ≠ det(P)⁻¹ — the slot dictionary is wrong; the
  renormalisation is not a pure slot-2 action. Then TOTAL carries a character
  in a slot where Ψ does not, and the route dies at (iii).
* **F3.** The exponent comes out +2 rather than −2 (i.e. χ = det(P)^{+2}).
  Then χ = Ψ-factor⁻¹, TOTAL/Ψ is not coset-constant, and the 120/120
  agreement of session 18 must be re-examined — an alarm, since that data
  would then have to be explained away.
* **F4.** I₆ ∘ (slot 1 ↔ slot 3) = −I₆. Then Ψ(A′,B′)·det(P)² = −Ψ(A,B) on the
  transpose coset while TOTAL is unchanged there, so **TOTAL ∝ Ψ is refuted**
  and any point whose net is H-equivalent to its own transpose with a
  nontrivial connecting element is an explicit counterexample. This is the
  single most dangerous check in the session and it is why the transpose coset
  was named as a gap.
* **F5.** The uniqueness input is weaker than recorded (the equivariant
  bidegree-(2,2) space in function space is bigger than 1-dimensional). Then
  even with P1–P4 the conclusion does not follow. This will be re-verified
  independently in this session rather than taken from the session-19 record.

## Standing engine handoff (pre-registered; DO NOT RUN HERE)

The theorem, if it closes, predicts a value that has never been measured and
that no fit could have produced. The discriminating point is
X₋₃ = {x₃+=x₂, x₄+=x₁, x₇+=x₁, x₈+=x₀}, with Ψ = −3:

    **TOTAL_{X₋₃} = −3 × 1,152,144,000 = −3,456,432,000**,
    with the whole σ-table sign-flipped relative to a Ψ > 0 point.

Inputs are already banked (`inputs/evalin/f1Xm3_*`); one measured value there
is V₀₀ = +893,138,400. Cost: the eight orbit representatives, ≈ one overnight
on two workers. This is handed to the engine track as a pre-registered test of
the *theorem*, not of a fit: a miss refutes one of steps (i)–(iv) and localises
which. It is not run in this session.

---
