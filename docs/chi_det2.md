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

# PART II — RESULT (computed after the pre-registration was committed, 2545f1e)

## Verdict: **the gap closes. The totals law is a theorem.**

> **THEOREM (totals law).** For every balanced direction N = e₁⊗A + e₂⊗B,
>
>     TOTAL(N)  =  Ψ(N) · 1,152,144,000 ,     Ψ = 2u₁ − 4u₂ − D = −I₆^prim(I,A,B).
>
> Proof: steps (i), (ii) as before; step (iii) below; step (iv) as before, with
> the uniqueness input re-verified independently here.

The predictions P1–P5 all landed, and none of the falsifiers F1–F5 fired. The
two named pieces of step (iii) behave as follows.

## 1. The character is a square, and the transpose coset cannot contribute

Write u_{N′} = q·u_N·s with s = t⁻¹ ∈ H, so that q = u_{N′}·t·u_N⁻¹ and
Γ_{N′} = t·Γ_N. Then, purely from λ′ = (8,8,8,6⁶) and 8 = 6 + 2,

    χ(q) = det(q|_{V/W})⁸ · det(q|_W)⁶ = det(q)⁶ · det(q|_{V/W})² .

Both u's are unipotent, so det(q) = det(t); and det(t) = ±1 on H, since
X ↦ aXb has determinant (det a·det b)³ = 1 and the transpose has determinant
(−1)³ = −1 on M₃. Hence **det(q)⁶ = 1 on both cosets** and

> **χ(q) = det(q|_{V/W})²  —  a perfect square, with the transpose coset
> contributing nothing.**

This is the same parity that closed the k = 2 ray (det₉ is −1 on the transpose
coset, and the exponent there was even too). Verified 58/58 in the sweep, on
both cosets, including non-unimodular elements. **P1 confirmed, F1 not fired.**

## 2. The slot dictionary: which 3-space is V/W?

Reconstructed from scratch (`analysis/wk4_s22_dict.py`), with the session-17
orientation: u_N is the unipotent in which **row 0 receives**,
(u_N X)_{0j} = X_{0j} + Σ_l A_{lj}X_{1l} + Σ_l B_{lj}X_{2l}, and
W = {row 0 = 0} = span{x₃…x₈}. Then Γ_N = u_N⁻¹(W) = ker(first three rows of
u_N), so

    Γ_N^⊥ = rowspan(first three rows of u_N),

and the *j*-th row of u_N, read as a 3×3 matrix, is exactly the net element
with rows (e_jᵀ, (Ae_j)ᵀ, (Be_j)ᵀ). Two consequences, and they are the whole
dictionary:

* the tensor slabs are (I, A, B) — session 18's closed form, re-derived here as
  a triviality of the construction rather than a computation;
* **the canonical parameter v is the u_N-transported basis of W^⊥.** The three
  tensor slots are: slot 1 = the row index of the net matrix, slot 3 = its
  column index, slot 2 = the parameter v. H acts on slots 1 and 3 only
  (X ↦ aXb acts on rows and columns); it does **not** act on slot 2.

Because (V/Γ_N)* = Γ_N^⊥ and the transported bases are the v-bases,

    det(q|_{V/W}) = det(G)⁻¹ ,

where G is the change of parameter induced by t — i.e. **the slot-2 basis
change**. Explicitly, with α = a^{-T}, β = b^{-T},

    S′_k = Σ_{k′} α_{kk′} βᵀ S_{k′},   P = Gᵀ = βᵀ(α₀₀I + α₀₁A + α₀₂B),
    A′ = S′₁P⁻¹,   B′ = S′₂P⁻¹.

Verified 58/58. **P2 confirmed, F2 not fired.** Combining with §1:

> **χ = det(G)⁻² : the character is det² in the net's parameter slot — the
> third tensor slot, the one H does not act on.** This is the χ ↔ det²
> identification, and it is an identity, not a numerical agreement.

The sign of the exponent is pinned independently by homogeneity, exactly as
session 17 pinned the convention: for the one-parameter subgroup realising
N ↦ sN one gets det G = s^{−4/3}·… , concretely χ = d¹² = s⁴ with s = d³,
which is V(sN) = s⁴V(N). **F3 not fired.**

## 3. What the group does to (A, B), and what it therefore does to TOTAL

Two one-parameter subgroups, computed symbolically in all 18 indeterminates
(`analysis/wk4_s22_oneparam.py`):

| element of H | induced action on (A,B) | χ |
|---|---|---|
| β unipotent, α = I | (A,B) ↦ (βᵀAβ^{-T}, βᵀBβ^{-T}) — **conjugation** | **1** |
| α: slab₀ ↦ slab₀+t·slab₁, β = I | (A,B) ↦ (A(I+tA)⁻¹, B(I+tA)⁻¹) | **det(I+tA)⁻²** |
| α: slab₀ ↦ slab₀+t·slab₂, β = I | (A,B) ↦ (A(I+tB)⁻¹, B(I+tB)⁻¹) | **det(I+tB)⁻²** |

Both are realised inside H (α, β ∈ SL₃, so det a·det b = 1), so the
double-coset theorem applies to them. Hence, for TOTAL:

    TOTAL(gAg⁻¹, gBg⁻¹) = TOTAL(A,B),
    D_A TOTAL + 2 tr(A)·TOTAL = 0,     D_B TOTAL + 2 tr(B)·TOTAL = 0,

with the derivations δA = −A², δB = −BA (and the mirror δA = −AB, δB = −B²).

**A correction to the session-18/19 record, and it changes nothing.** Those
documents write the slab renormalisation as *left* multiplication,
((I+tA)⁻¹A, (I+tA)⁻¹B); the dictionary gives *right* multiplication,
(A(I+tA)⁻¹, B(I+tA)⁻¹). The two differ by conjugation by (I+tA) — verified
symbolically — so on conjugation-invariant functions they impose the same
condition, and the recorded characterisation of Ψ stands verbatim. The
derivations above are the ones actually derived from the dictionary.

## 4. Ψ obeys the same law — including on the transpose coset

Ψ = −I₆^prim(I,A,B) is a semi-invariant with character det² in each slot. Under
t ∈ H, slots 1 and 3 receive α and βᵀ with (det α·det β)² = (det a·det b)⁻² = 1,
and the renormalisation is a slot-2 action by G⁻¹. So

    **Ψ(A′,B′) = det(G)⁻²·Ψ(A,B) = χ·Ψ(A,B)** — verified 58/58, exactly.

The transpose acts on the net by Y ↦ Yᵀ, i.e. it **swaps slots 1 and 3**. Since
the degree-6 invariant space is one-dimensional, S₃ acts on it by a character,
and the sign character was the live danger (F4): it would have made Ψ
anti-invariant where TOTAL is invariant and refuted the law outright. It is
**trivial**, confirmed two independent ways:

1. all transpose-coset cases in the sweep satisfy the Ψ law with a **+** sign
   (16 in the first pass, 29 in the consolidated sweep, no exceptions);
2. directly: on the 9-parameter family of tensors fixed by the slot-1↔3 swap
   (row 0 of A = e₁ᵀ, row 0 of B = e₂ᵀ, row 2 of A = row 1 of B), Ψ takes the
   values 2532, 480, 3712, −1259, 4096, 1992 at random members — it does not
   vanish identically, which it would have to if the character were the sign.

**P4 confirmed, F4 not fired.** Note that the transpose is harmless *twice
over*, and for independent reasons: it cannot enter χ (det(t)⁶ = 1) and it
cannot enter Ψ (trivial swap character).

## 5. The uniqueness input, re-verified from scratch (F5)

Not taken from the session-19 record (`analysis/wk4_s22_unique.py`):

* **dim of the bidegree-(2,2) simultaneous-conjugation invariants = 9**, by an
  SL₃ character computation independent of any trace-word basis: the
  multiplicity of the trivial representation in Sym²(gl₃) ⊗ Sym²(gl₃) is 9
  (with dim Sym²(gl₃) = 45 and dim of the tensor square = 2025 as sanity
  checks). The ten trace words have rank 9 as functions — the one relation is
  the polarised Cayley–Hamilton identity, as recorded.
* Imposing the two equivariances **derived in this session** leaves a
  2-dimensional coefficient space, hence **exactly 1 dimension in function
  space**, and both nullspace vectors are constant multiples of Ψ (ratios 1/2
  and 2 over the whole sample). **F5 not fired.**

## 6. The proof

1. TOTAL is a bidegree-(2,2) polynomial on the 18-dimensional balanced cone
   (counting lemma, session 15).
2. For t ∈ H, q := u_{N′}·t·u_N⁻¹ preserves W and TOTAL(N′) = χ(q)·TOTAL(N)
   (session 17).
3. χ(q) = det(q)⁶·det(q|_{V/W})² = det(q|_{V/W})², since det(q) = det(t) = ±1
   and 6 is even. **[§1]**
4. det(q|_{V/W}) = det(G)⁻¹ with G the induced change of the net's parameter —
   the third tensor slot. So χ = det(G)⁻². **[§2]**
5. Specialising t: TOTAL is a simultaneous-conjugation invariant and satisfies
   D_A TOTAL + 2 tr(A)TOTAL = D_B TOTAL + 2 tr(B)TOTAL = 0. **[§3]**
6. That space is one-dimensional and is spanned by Ψ. **[§5]**
7. So TOTAL = c·Ψ; TOTAL(C) = 1,152,144,000 and Ψ(C) = 1 give
   c = 1,152,144,000. ∎

## 7. Three consequences

**(a) Session 17's honest negative is resolved.** C and R are in *different*
double cosets and have equal totals; session 17 concluded "the group is smaller
than the phenomenon" and left the coincidence standing. It is now explained:
the group is indeed too small to connect C to R, but the space of functions it
constrains is **one-dimensional**, so the law extends across cosets even though
the group does not. Equality of the two certificate totals is forced.

**(b) Session 18's χ = Ψ on 120/120 same-coset pairs was not a coincidence and
not merely a character argument** — it is the identity χ = det(G)⁻² together
with Ψ's slot-2 character, which is what §2 and §4 prove.

**(c) The character is det² for an arithmetic reason, and the reason
generalises.** For a deficit weight λ′ = (p,p,p,q⁶) the same computation gives

    χ = det(t)^q · det(q|_{V/W})^{p−q} ,

so the character in the net's parameter slot is **det^{p−q}**, and the transpose
coset is harmless **iff q is even**. For our weight p − q = 8 − 6 = 2, which is
why the relevant classical object is the degree-6 Aronhold invariant (character
det² per slot on 3×3×3 tensors). Two predictions follow for other weights, and
they are cheap to state and expensive to test:

* if p − q = 3 the governing object would be the **degree-9** Vinberg generator;
  if p − q = 4, the degree-12 one. The totals law is not special to Ψ — it is
  the p = q + 2 case of a family.
* if q is odd, χ picks up −1 on the transpose coset while any det^{even}
  semi-invariant does not, forcing TOTAL to **vanish** on every direction whose
  net is H-equivalent to its own transpose. That is a testable vanishing law at
  the first odd-q deficit weight.

## 8. What this does NOT settle

* **Per-σ values.** Untouched. Session 16's refutation stands: the σ-table is
  scheme bookkeeping, stable under neither Q nor H, and at X4 it reorganises
  rather than rescaling. The theorem is about totals and says nothing here.
* **The hypotheses are inherited.** The proof consumes step (i) (the counting
  lemma) and step (ii) (the double-coset theorem) as given; both were proved in
  earlier sessions and were not re-derived here beyond rebuilding the
  conventions they rest on. A failure of the standing engine prediction below
  would most likely indict one of those, not §§1–5.
* **Other weights.** Everything above is for λ′ = (8,8,8,6⁶). §7(c) says what
  the generalisation should look like; nothing here proves it.

## 9. The standing engine prediction is now a theorem's prediction

The handoff logged in Part I is unchanged in content and changed in status. At
X₋₃ = {x₃+=x₂, x₄+=x₁, x₇+=x₁, x₈+=x₀}, where Ψ = −3:

    **TOTAL_{X₋₃} = −3,456,432,000**, with the whole σ-table sign-flipped.

This is now the prediction of a proved law rather than of a fit, and the first
test of the law at a negative value of Ψ. Inputs are banked
(`inputs/evalin/f1Xm3_*`; the one measured value there is V₀₀ = +893,138,400);
cost is the eight orbit representatives, about one overnight on two workers.
**Not run in this session** — it is handed to the engine track. A miss would
refute step (i) or step (ii), since §§1–5 are now identities.

## Files

    analysis/wk4_s22_dict.py      conventions rebuilt from scratch; u_N, W, the
                                  net, the slot dictionary, chi from the 9x9
                                  definition, Psi
    analysis/wk4_s22_chi.py       chi vs det(G)^-2 vs the Psi ratio, both cosets
    analysis/wk4_s22_oneparam.py  the one-parameter slab subgroups, symbolically
    analysis/wk4_s22_unique.py    the character count (dim = 9) and the
                                  equivariant subspace (dim = 1)
    analysis/wk4_s22_sweep.py     the consolidated 58-case sweep, seven checks
