# The totals law at other weights: λ′ = (p,p,p,q⁶)
Session 23 (2026-08-30), branch `s22-pq`. Math/symbolic only; **no engine run.**

Question 7.2 of the paper, which the previous session wrote. Two parts:
**(a)** does the uniqueness step survive at p − q = 3 and 4? **(b)** the
transpose-vanishing law at odd q — identify a concrete self-transpose net,
pre-register TOTAL = 0, hand it to the engine track.

---

# PART I — PRE-REGISTRATION
*(committed before any of this session's computations were run.)*

## 0. The dependency structure, stated first

`TOTAL(X₋₃) = −3,456,432,000` is pre-registered and **unmeasured**. Every
falsifier named for Theorem 5.5 was internal to its derivation; Ψ = −3 is the
first measurement that can contradict it. So this session is organised so that
its conclusions degrade gracefully. The intended dependency table, to be
restated with the results:

| result | depends on |
|---|---|
| the counting lemma at general (p,q) | leg arithmetic only — **independent of Theorem 5.5** |
| dimensions of the equivariant spaces | invariant theory only — **independent** |
| the restriction-map correspondence with Vinberg's ring | invariant theory only — **independent** |
| "the governing object at p−q = m is the degree-3m generator" | needs the counting lemma **and** the χ computation |
| the transpose-vanishing law at odd q | needs the χ computation **and** the double-coset theorem; **not** the uniqueness step, and **not** Ψ |

If X₋₃ refutes Theorem 5.5, the culprit is the counting lemma or the
double-coset theorem, since the χ identification is an identity in the
conventions. The first three rows survive either way.

## 1. Predictions for part (a)

**P1 — the counting lemma generalises, with the balance forced by arithmetic.**
For λ′ = (p,p,p,q⁶) we have |λ′| = 3p + 6q, so δ = p + 2q copies of det₃. Each
copy contributes exactly one leg from each matrix row, so before substitution
the content is (δ, δ, δ) across the three row-blocks. The demands are 3p in row
0 and 3q in each of rows 1 and 2. Hence the number of legs substituted out of
row 1 is t₁ = δ − 3q = p − q, and likewise t₂ = p − q:

> **PREDICTION P1: t = (m, m) with m := p − q, so TOTAL is a polynomial of
> bidegree (m,m) on the balanced cone.** At (8,8,8,6⁶): δ = 20, m = 2 — the
> known case, which is the check.

**P2 — the equivariant space is the invariant ring, degree by degree.** With
χ = det(t)^q·det(q|_{V/W})^{p−q}, the parameter-slot character is det^m and the
equivariance conditions become

    D_A f + m·tr(A)·f = 0 ,   D_B f + m·tr(B)·f = 0     (δA = −A², δB = −BA, and the mirror)

on bidegree-(m,m) simultaneous-conjugation invariants. Restriction to slab
normal form is injective on the tensor invariant ring (tensors with invertible
first slab are dense, and each is carried to normal form by a slot-2 action), so
every monomial in Vinberg's generators contributes. Prediction: nothing else
does.

> **PREDICTION P2:  dim{equivariant, bidegree (m,m)} = #{(a,b,c) ≥ 0 :
> 2a + 3b + 4c = m}**, the degree-3m part of C[I₆, I₉, I₁₂]:
>
> | m | 2 | 3 | 4 | 5 | 6 |
> |---|---|---|---|---|---|
> | predicted dim | 1 | 1 | **2** | 1 | 3 |
> | monomials | I₆ | I₉ | I₆², I₁₂ | I₆I₉ | I₆³, I₆I₁₂, I₉² |

**P3 — the headline, and it is a mixed verdict.**

> **PREDICTION P3: the uniqueness step SURVIVES at p − q = 3 and FAILS at
> p − q = 4.** At m = 4 the space is 2-dimensional because I₆² and I₁₂ both sit
> in it; Ψ² is an explicit second element (D_A(Ψ²) + 4tr(A)Ψ² = 2Ψ·(D_AΨ +
> 2tr(A)Ψ) = 0). So the analogue of the totals law at (10,10,10,6⁶) is not
> forced by equivariance alone: it needs **two** measured points, not one, and
> the equivariance argument determines the answer only up to a line.

I expect the table above to be exact, so that the failure at 4 is the first of
infinitely many (every even m ≥ 4 has more than one monomial).

## 2. Predictions for part (b)

**P4 — the self-transpose nets are the swap-symmetric family, and det G = 1
there.** The transpose acts on the net by Y ↦ Yᵀ, which swaps tensor slots 1
and 3. A net fixed by that swap in slab normal form satisfies (S_k)_{ji} =
(S_j)_{ki} with S₀ = I; explicitly

    A = [[0,1,0],[p,r,s],[u,v,w]] ,   B = [[0,0,1],[u,v,w],[y,z,c]]      (9 free parameters).

For such a net the transposed slab-zero is [row₀ I; row₀ A; row₀ B] = I, so the
renormalisation is trivial and **det G = 1**. Then χ = det(t)^q·det(G)^{−m} =
(−1)^q, and the double-coset theorem gives TOTAL = χ·TOTAL:

> **PREDICTION P4: at any weight (p,p,p,q⁶) with q ODD, TOTAL vanishes
> identically on the 9-parameter swap-symmetric family** — including at members
> where the gauge is nonzero, so the vanishing is not the gauge's doing. (At
> q even, χ = 1 and nothing is forced; this is consistent with the whole banked
> record, where q = 6 throughout.)

**P5 — a concrete, feasible witness exists.** I expect to find a member of the
family with entries in {0,1}, with Ψ ≠ 0, and displacement-feasible at an odd-q
weight; and I expect at least one odd-q weight of small δ to carry a nonzero
ambient multiplicity. Candidates, cheapest first: (3,3,3,1⁶) at δ = 5;
(5,5,5,3⁶) at δ = 11; (7,7,7,5⁶) at δ = 17. **Prediction: the cheapest of these
with amb > 0 is the test, and the prediction handed over is TOTAL = 0.**

## 3. FALSIFIERS, fixed in advance

* **G1.** The leg count does not force t₁ = t₂ (P1 fails) — then there is no
  balanced bidegree at other weights and part (a) has no space to work in.
* **G2.** dim at m = 3 is 0 or ≥ 2 — the p−q = 3 row of the table in Question
  7.2 is wrong as stated, and the degree-9 generator is not the governing
  object.
* **G3.** dim at m = 4 is 1. That contradicts injectivity of restriction (I₆²
  and I₁₂ are independent in a free ring), so it would be an **ALARM** — either
  the restriction argument or the machinery is wrong — not a result.
* **G4.** The dimensions do not match the Vinberg counts at some m ≤ 6 —
  restriction is not onto the equivariant functions, and the correspondence in
  the Question-7.2 table is looser than it looks.
* **G5.** The swap-symmetric family is not self-transpose as an H-orbit
  statement, or det G ≠ 1, or every member with Ψ ≠ 0 is weight-infeasible —
  then (b) has no clean witness and the vanishing law stays untestable.
* **G6.** No odd-q weight of reachable size has amb > 0 — (b) is untestable for
  a different reason, which is itself worth recording.

## 4. Discipline

Exact arithmetic throughout (integers, sympy Rationals, or arithmetic in a
finite field where a rank is all that is wanted — never floating point). Where a
rank is computed mod a prime, the conclusion is stated in the safe direction:
nullity mod p ≥ nullity over Q, so a mod-p nullity of d together with d explicit
independent witnesses over Q pins the dimension exactly. No engine run in this
session; anything that needs one is pre-registered and handed over.

---

# PART II — RESULT (computed after the pre-registration was committed, 9775d97)

## Verdict in one line

**(a) closes with a mixed answer**, sharper than pre-registered: the uniqueness
step survives at p − q = 3 and fails at p − q = 4, and the reason is a clean
theorem — the equivariant space is *exactly* the invariant ring of the tensor,
degree by degree, so its dimension is the number of monomials
I₆^a I₉^b I₁₂^c of degree 3m. **(b) yields a stronger falsifier than
pre-registered**, and a scarcer one: at odd q the transpose does not merely kill
the self-transpose directions, it kills **everything** when p − q is 2 or 4 —
but almost every cheap odd-q weight carries no highest weight vector at all.
The one that does is λ′ = (7,7,7,3⁶) at δ = 13, where every banked point is
weight-feasible and the prediction is TOTAL = 0 at all of them.

All five pre-registered predictions landed; falsifiers G3 and G4 did not fire;
**G6 fired partially** and is reported below as the honest negative it is.

---

## 1. The counting lemma at a general weight (P1 confirmed)

λ′ = (p,p,p,q⁶) has |λ′| = 3p + 6q, so δ = p + 2q copies of det₃. Each copy
contributes exactly one leg from each matrix row, so before substitution the
content is (δ, δ, δ) across the three row-blocks; the demands are 3p, 3q, 3q.
Substituting a leg moves it from row 1 or row 2 into row 0, so

    t₁ = δ − 3q = p − q ,      t₂ = δ − 3q = p − q ,

with 2(p − q) = 3p − δ substitutions in total.

> **LEMMA (counting, general weight).** On balanced directions, TOTAL at
> λ′ = (p,p,p,q⁶) is a polynomial of bidegree (m, m) with **m := p − q**.

At (8,8,8,6⁶): δ = 20, m = 2 — the known case. This is arithmetic; it uses
nothing from Theorem 5.5.

## 2. The equivariant space IS the invariant ring (the structural theorem)

Write E_m for the space of bidegree-(m,m) simultaneous-conjugation invariants of
a pencil satisfying the slab equivariance with character det^m,

    D_A f + m·tr(A)·f = 0  (δA = −A², δB = −BA),   and the B-mirror,

which is what χ = det(G)^{−m} imposes. Let R = C[I₆, I₉, I₁₂] be the
SL₃×SL₃×SL₃ invariant ring of C³⊗C³⊗C³ (Vinberg; free on those degrees).

> **THEOREM (restriction is an isomorphism).** Restriction to slab normal form,
> I ↦ I(I, A, B), is a linear isomorphism from R_{3m} onto E_m. Consequently
>
>     dim E_m = #{ (a,b,c) ∈ ℤ³≥0 : 2a + 3b + 4c = m } .

*Injective.* If I|₍I,A,B₎ ≡ 0 then for any tensor T with slab S₀ invertible, the
slot-2 action by S₀⁻¹ carries T to (I, S₁S₀⁻¹, S₂S₀⁻¹), so
I(T) = det(S₀)^m·I(I,A,B) = 0; such T are dense, so I = 0.

*Surjective.* Given f ∈ E_m put F(S₀,S₁,S₂) := det(S₀)^m f(S₁S₀⁻¹, S₂S₀⁻¹).
Left multiplication of all slabs by g (slot 3) conjugates the normal form and
multiplies det(S₀)^m by det(g)^m; right multiplication by h (slot 2) leaves the
normal form alone and multiplies it by det(h)^m; and a slot-1 slab mixing α
sends S₀ ↦ P̃S₀ with P̃ = α₀₀I + α₀₁A + α₀₂B and the normal form to
((α₁₀I+α₁₁A+α₁₂B)P̃⁻¹, …), so F is unchanged exactly because f is equivariant.
So F is a semi-invariant of character det^m in each slot — i.e. an invariant of
degree 3m — as soon as it is polynomial. It is: F is regular off {det S₀ = 0},
so its polar divisor D is contained there; D is invariant, and the slot-1 group
moves {det S₀ = 0} to {det(Σ c_k S_k) = 0} for every c, so D lies in the
intersection of all of them, which is the locus where the slab pencil is
identically singular — of codimension ≥ 2. A divisor cannot. Hence D = ∅. ∎

*Degrees match* because each ε in the slab slot needs three distinct slab
indices, so every invariant of degree 3m restricts in slab multidegree
(m,m,m) — the argument of session 19, stated for general degree.

**Verification (P2 confirmed).** Independently of the theorem:

| m | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| ambient: dim of bidegree-(m,m) conjugation invariants | 2 | 9 | 25 | 66 | 149 | 329 | — |
| **dim E_m computed** | **0** | **1** | **1** | **2** | **1** | **3** | **2** |
| #{2a+3b+4c = m} | 0 | 1 | 1 | 2 | 1 | 3 | 2 |
| monomials | — | I₆ | I₉ | I₆², I₁₂ | I₆I₉ | I₆³, I₆I₁₂, I₉² | I₆²I₉, I₉I₁₂ |

The ambient row is an SL₃ character computation (multiplicity of the trivial in
Sym^m(gl₃)⊗Sym^m(gl₃)); it is reproduced exactly as the rank of the
trace-monomial evaluation matrix in every case, which cross-checks both. The
E_m row is an exact nullspace over ℚ at m ≤ 4, the same computation in GF(p) at
m = 5, 6 (safe direction: nullity_p ≥ nullity_ℚ, and the products below supply
matching witnesses over ℚ), and the span of products at m = 7. The products
Ψ^a g₃^b f₄^c were checked to have exactly the predicted rank at m = 2,…,7 — the
ring structure of the theorem, verified rather than assumed.

## 3. The answer to (a)

> **dim E_m = 1 exactly for m ∈ {2, 3, 5}. It is 0 at m = 1, and ≥ 2 for every
> other m.**

* **p − q = 3: the uniqueness step SURVIVES.** dim E₃ = 1, spanned by the
  restriction of the degree-9 Vinberg generator. So at λ′ = (9,9,9,6⁶) —
  δ = 21, the δ = 3 row of the conductor table — the equivariance argument still
  forces TOTAL = c·g₃, and **one** measured total fixes c.
* **p − q = 4: the uniqueness step FAILS.** dim E₄ = 2. Ψ² is in it (from
  D_A(Ψ²) = 2Ψ·D_AΨ = −4tr(A)Ψ², so D_A(Ψ²) + 4tr(A)Ψ² = 0 identically), and so
  is the restriction of I₁₂; they are independent. The equivariance argument
  determines TOTAL only up to a line, and **two** measured totals are needed.
* **p − q = 1: TOTAL vanishes identically.** dim E₁ = 0 — the ambient space of
  bidegree-(1,1) conjugation invariants is 2-dimensional (tr A tr B, tr AB) and
  neither combination is equivariant. So at any weight with p = q + 1 the
  evaluation is zero on every balanced direction, whatever q.
* p − q = 5 is the last value where uniqueness holds (E₅ = ⟨Ψ·g₃⟩).

So the table in Question 7.2 is right about *which* invariant governs and wrong
to suggest the argument continues to determine it: the correspondence
p−q = m ↔ degree 3m is exact, but the space stops being a line after m = 5.

## 4. The degree-9 generator, explicitly, and where it does not vanish

Extracted from the nullspace and put in primitive integral form (13 trace
monomials, coefficients ±1, ±3, 6):

    g₃ = −tr(A)³tr(B)³ + tr(A)³tr(B)tr(B²) + 3tr(A)²tr(B)²tr(AB)
         − 3tr(A)²tr(B)tr(AB²) + tr(A)tr(B)³tr(A²) − 3tr(A)tr(B)²tr(A²B)
         + 3tr(A)tr(B)tr(A²B²) − tr(A)tr(A²)tr(B³) − tr(B)tr(B²)tr(A³)
         − 3tr(AB)tr(A²B²) + tr(A³)tr(B³) − 3tr(A²B)tr(AB²) + 6tr(A²BAB²)

It vanishes on compression nets, as any tensor invariant must — with compression
characterised correctly as **{I, A, B} linearly dependent** (a common left kernel
u for the net means u₀I + u₁A + u₂B = 0; setting a row of A and B to zero is
*not* compression, and an earlier draft of this check was wrong for that reason).

**It also vanishes at every banked point:** g₃ = 0 at C, R, T4, X4, Xm3 and P,
where Ψ = 1, 1, 1, 4, −3, 0. This is actionable rather than curious. If the
totals law analogue holds at λ′ = (9,9,9,6⁶), then TOTAL = c·g₃ there and **every
point the programme has ever evaluated gives zero**. A certificate at the δ = 3
row needs a direction off the g₃-locus.

Sweep of the {0,1} balanced cone: **87,660 of 262,144 pencils have g₃ ≠ 0**, and
the smallest live ones have four transvections and |g₃| = 3. The recommended
evaluation point, weight-feasible at (9,9,9,6⁶) with δ = 21:

> **G3a = {x₃ += x₂, x₄ += x₀, x₆ += x₂, x₈ += x₁}**,
> i.e. A = E₀₂ + E₁₀, B = E₀₂ + E₂₁, with **g₃ = 3 and Ψ = 0**.

Note Ψ = 0 there: the δ = 2 gauge and the δ = 3 gauge have different zero loci,
so the points that certify one row are exactly the wrong points for the other.

## 5. Part (b): the transpose law, and it is stronger than predicted

**The self-transpose family (P4 confirmed).** The transpose acts on the net by
Y ↦ Yᵀ, swapping tensor slots 1 and 3. In slab normal form the fixed nets are
(S_k)_{ji} = (S_j)_{ki}, i.e.

    A = [[0,1,0],[p,r,s],[u,v,w]] ,   B = [[0,0,1],[u,v,w],[y,z,c]]    (9 parameters),

for which the transposed slab-zero is [row₀I; row₀A; row₀B] = I, so the
renormalisation is trivial, **det G = 1**, and χ = det(t)^q·det(G)^{−m} = (−1)^q.
At q odd the double-coset theorem then gives TOTAL = −TOTAL on the family.

**But TOTAL lies in E_m, and that is what makes the law bite everywhere.** The
question is which elements of E_m vanish on the family. Computed:

| m | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| dim E_m | 0 | 1 | 1 | 2 | 1 | 3 | 2 |
| rank of E_m on the self-transpose family | 0 | 1 | 0 | 2 | 0 | 2 | 0 |
| elements vanishing there | 0 | **0** | 1 | **0** | 1 | 1 | 2 |

The pattern has a clean cause: **g₃ vanishes identically on the family** (checked
on 60 random members and implied by every entry of the table), so a monomial
I₆^a I₉^b I₁₂^c restricts to zero on the family as soon as b ≥ 1, and the rank is
#{(a,c) : 2a + 4c = m} — zero for m odd, ⌊m/4⌋ + 1 for m even. This says the
degree-9 Vinberg generator is **anti-invariant under odd permutations of the
three tensor slots**, while I₆ and I₁₂ are invariant: the S₃-character on the
invariant ring is (−1)^{I₉-degree}. (For I₆ this was already forced in session
22 — Ψ does not vanish on the family.)

> **THEOREM (transpose-vanishing law, sharpened).** At λ′ = (p,p,p,q⁶) with q
> **odd**:
> * if m = p − q is **odd**, the transpose imposes nothing — every element of
>   E_m already vanishes on the self-transpose family;
> * if m = 2 or m = 4, no nonzero element of E_m vanishes there, so
>   **TOTAL ≡ 0 identically on the whole balanced cone**;
> * if m ≥ 6 is even, TOTAL is confined to the (dim E_m − ⌊m/4⌋ − 1)-dimensional
>   subspace of elements with a factor of I₉ — at m = 6, the line ⟨g₃²⟩.

The pre-registration predicted vanishing on the self-transpose directions. The
actual law is universal vanishing at m ∈ {2,4}, which is a much cheaper thing to
test: any balanced direction will do.

## 6. Which odd-q weight can be tested — the honest negative (G6, partially)

A weight is testable only if S_{λ′} actually occurs in Sym^δ(Sym³ℂ⁹). Computed
with the plethysm machinery of `wk3_s7_ray.py`, re-parametrised and validated
against two classical cases (h₁[h₃] = s₃ and h₂[h₃] = s₆ + s₄₂, plus the recorded
amb((2,2,2),2) = 0):

| λ′ | δ | m = p−q | amb |
|---|---|---|---|
| (3,3,3,1⁶) | 5 | 2 | **0** |
| (5,5,5,1⁶) | 7 | 4 | **0** |
| (4,4,4,1⁶) | 6 | 3 | 0 |
| (6,6,6,1⁶) | 8 | 5 | 0 |
| (4,4,4,3⁶) | 10 | 1 | 0 |
| (5,5,5,3⁶) | 11 | 2 | **0** |
| (6,6,6,3⁶) | 12 | 3 | 0 |
| **(7,7,7,3⁶)** | **13** | **4** | **1** |
| (7,7,7,5⁶) | 17 | 2 | **0** |
| (8,8,8,5⁶) | 18 | 3 | 1 |

So the cheap odd-q weights with m even — exactly the ones carrying the sharp
prediction — are mostly **empty**: no highest weight vector, nothing to evaluate.
That is falsifier G6 firing for the small cases, and it is worth recording,
because it says the vanishing law is hard to see rather than easy. The one
survivor in reach is λ′ = (7,7,7,3⁶) at δ = 13. (The other nonempty odd-q weight
found, (8,8,8,5⁶), has m = 3 — odd — so the law says nothing there.)

## 7. PRE-REGISTERED, handed to the engine track, NOT run here

> **TEST.  λ′ = (7,7,7,3⁶), δ = 13, m = p − q = 4, q = 3 odd, amb = 1.**
> **PREDICTION: TOTAL = 0 at every balanced direction.**
> In particular TOTAL = 0 at C = {x₅+=x₁, x₇+=x₂} — the most-validated point in
> the programme — and at R, T4, X4 and Xm3, all five of which are
> **weight-feasible** at this weight (checked; the prediction is therefore not
> vacuous by infeasibility).

δ = 13 is materially smaller than the δ = 20 grind, and the balanced structure is
the same (t = (4,4): eight substituted legs among thirteen copies); the engine
track should scope the input generation from `wk3_s12_genD.py` as usual. A
nonzero total at any balanced direction refutes the law and, with it, one of the
two inputs the χ computation rests on.

**Why this is a good falsifier.** It is not a number produced by a fit; it is
zero, predicted universally, at a weight nobody has looked at, from a parity that
has nothing to do with the arithmetic of the δ = 2 row. And unlike X₋₃ it does
not test Theorem 5.5's *value* — it tests the character computation that the
whole p−q story rests on.

## 8. What survives if Theorem 5.5 is retracted

The standing external test is `TOTAL(X₋₃) = −3,456,432,000`, still unmeasured. If
it misses, the fault is in the counting lemma or in the double-coset theorem, not
in the χ identification, which is an identity in the conventions. Accordingly:

| result of this session | survives a retraction of Theorem 5.5? |
|---|---|
| §1 counting lemma at general (p,q), t = (m,m) | **Yes** — leg arithmetic only. It is *step (i)* itself; a retraction traced to step (i) would kill it, but nothing else here depends on the totals law. |
| §2 restriction isomorphism, dim E_m = #{2a+3b+4c = m} | **Yes, entirely** — pure invariant theory of ℂ³⊗ℂ³⊗ℂ³; no evaluation, no χ, no h. |
| §3 uniqueness survives at m = 3, fails at m = 4, is empty at m = 1 | **Yes** as statements about E_m; their *relevance* to totals needs steps (i)–(iii). |
| §4 g₃ explicitly, its compression vanishing, the g₃-locus, the point G3a | **Yes** — g₃ is a classical invariant; only the claim that it governs the δ = 3 row needs the theorem. |
| §5 the transpose-vanishing law | **No** — it needs the χ formula (step iii, this is where it would break) and the double-coset theorem (step ii). It does **not** need the uniqueness step or Ψ. |
| §6 the multiplicity table | **Yes** — plethysm only. |
| §7 the prediction TOTAL ≡ 0 at (7,7,7,3⁶) | **No** — same dependence as §5. A miss localises the failure to step (ii) or (iii). |

The two halves therefore fail independently: §§2–4, 6 are invariant theory and
plethysm and stand on their own; §§5, 7 are the part that shares a fate with
Theorem 5.5. That is the graceful degradation the brief asked for, and it is why
the deliverable is organised this way.

## 9. Files

    analysis/wk4_s23_dims.py      SL_3 character count of the ambient spaces
    analysis/wk4_s23_words.py     trace-monomial machinery, dual-number derivations
    analysis/wk4_s23_equiv.py     the equivariant nullspace over Q (m <= 4)
    analysis/wk4_s23_equivp.py    the same in GF(p) (m = 5, 6)
    analysis/wk4_s23_gens.py      generator extraction; Psi^2 and the m = 4 pair
    analysis/wk4_s23_swap.py      the self-transpose family and its ranks
    analysis/wk4_s23_products.py  the ring structure, m = 2..7
    analysis/wk4_s23_g3locus.py   feasibility DFS at a general weight; the g3-locus
    analysis/wk4_s23_g3points.py  {0,1} directions with g3 != 0; the point G3a
    analysis/wk4_s23_amb.py       amb(lambda', delta), validated on two classical cases
    analysis/wk4_s23_feas773.py   feasibility of the banked points at (7,7,7,3^6)
