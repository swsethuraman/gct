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
