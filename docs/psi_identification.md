# What is Ψ? — a reduction, and the death of the plane-cubic hypothesis
Session 18 (2026-08-29), symbolic only; no engine was launched (the six X4
completing runs held the two worker slots throughout).

## The reduction (new, and it simplifies everything)

Session 17 showed the double coset of a direction is the H-orbit of the
3-dimensional annihilator net Γ_N^⊥ ⊂ M₃. Computing that annihilator in
closed form: for M ∈ Γ_N with free rows c₁, c₂,
    ⟨Y, M⟩ = c₁·(y₁ − A y₀) + c₂·(y₂ − B y₀),
which vanishes for all c iff y₁ = A y₀ and y₂ = B y₀. Hence

> **Γ_N^⊥ = { [ v ; Av ; Bv ] : v ∈ C³ }** — canonically parametrised by v,
> with no basis ambiguity.

Validated against session 17's nullspace construction at all 11 banked
points. Two consequences:

1. **The net's 3×3×3 tensor has slabs exactly (I, A, B)** (verified
   symbolically). So the object whose classical invariant theory we want is
   the tensor (I, A, B) — the pencil with the identity adjoined. That is a
   substantially cleaner target than a general 27-parameter tensor.
2. Its two contractions give two ternary cubics:
   the **v-cubic** c_N(v) = det[v; Av; Bv], and the
   **slab-cubic** det(x₀I + x₁A + x₂B) (the classical matrix-pencil
   determinant). Only the first was examined in session 17.

## The plane-cubic hypothesis is DEAD (two independent proofs)

**(a) Degree count.** The coefficients of c_N have bidegree exactly (1,1) in
(A,B) (verified symbolically on the general pencil). Ψ has bidegree (2,2).
So Ψ would have to be a **degree-2 invariant of ternary cubics** — but the
invariant ring of ternary cubics is C[S,T] with deg S = 4, deg T = 6, which
has nothing in degree 2. Ψ is therefore not a polynomial invariant of c_N.

**(b) Explicit counterexample, projective class.** Three points whose
v-cubics are all **triangles** — hence all projectively equivalent — with
three different Ψ:

| point | v-cubic | Ψ |
|-------|---------|---|
| C  | −v₀v₁v₂            | 1 |
| X4 | −v₀(v₁−v₂)(v₁+v₂)  | 4 |
| Z = (A=[[1,0,0],[1,0,0],[0,0,0]], B=[[1,0,1],[1,0,1],[1,1,0]]) | v₀(v₀−v₁)(v₀+v₁) | **0** |

So Ψ is not a function of the cubic's projective class either. The
"Ψ is a classical invariant of the associated plane cubic" route is closed.

**Corollary — a vanishing characterisation that also fails.** Ψ = 0 at all
five compression points (whose cubic is identically zero) and at D (cubic
−v₀v₁², non-reduced), suggesting "Ψ = 0 ⟺ c_N non-reduced". Tested on 400
feasible points: **361 agree, 39 counterexamples**, every one of the form
Ψ = 0 with a perfectly reduced squarefree cubic (Z above is one). Rejected.

## What survives, and the precise remaining target

The cubic loses information that the tensor keeps, and Ψ is empirically
consistent with the tensor orbit: session 18's other result — χ = Ψ on
120/120 same-coset pairs — says exactly that Ψ respects the H-orbit of the
tensor up to the character. So the live hypothesis is now sharp:

> **Ψ is the bidegree-(2,2) component of a classical SL₃×SL₃×SL₃ invariant
> of the tensor (I, A, B).**

Degree bookkeeping supports the degree-6 generator specifically: a degree-6
invariant restricted to slabs (I, A, B) contains a term using 2 I's, 2 A's
and 2 B's — bidegree (2,2), exactly Ψ's shape. This also explains, without
further assumption, why Ψ behaves multiplicatively like a character
(the χ = Ψ agreement): a tensor semi-invariant must.

CAVEAT, flagged rather than assumed: the claim that the invariant ring of
3×3×3 tensors under SL₃³ is polynomial on generators of degrees 6, 9, 12
(Vinberg θ-group, ℤ/3-grading of E₆) was **not verified in this session**.
It should be checked before being relied on, and the identification of the
degree-6 and degree-12 generators with the Aronhold S and T of a
determinantal cubic should be treated as unverified folklore — especially
since (a) and (b) above show the v-cubic's S and T cannot be the whole story.

NEXT STEP (engine-free): construct I₆ explicitly for 3×3×3 tensors, restrict
to (I, A, B), extract the bidegree-(2,2) part, and compare with
Ψ = 2u₁ − 4u₂ − D as a symbolic identity. If it matches, Ψ stops being a
fitted quartic and becomes a formula evaluable at any direction, forever,
with no engine — and the compression criterion, the χ law and the totals
prediction all become corollaries of classical invariant theory.
