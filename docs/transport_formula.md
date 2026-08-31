# The World-B transport formula: attainment, and where it fails
Session 23 (2026-08-31), branch `s23-transport`. Mathematics and exact
arithmetic only; no engine run and none required.

Pre-registrations: `results/PREREG_transport.md` (commit `41d1389`, before any
computation) and `results/PREREG_transport2.md` (commit `2a82158`, after the
refutation and before the confirming sweep).

---

## 0. Summary

Theorem 3.1 of `paper/det3-conductor.tex` asserted that for the ternary-cubic
world, on every weight with `m(λ) > 0`,

    c(λ) = ⌊ (λ₁ − 2λ₃) / 6 ⌋ = ⌊ μ_max(λ) / |w_N| ⌋,

verified on the 254 weights with `m(λ) > 0` and `δ ≤ 10`. The `≤` half was
proved; attainment was conjectural.

**The equality is false.** The first counterexample is `λ = (17,17,2)` at
`δ = 12`, where `m(λ) = 1`, the shadow maximum is `⌊13/6⌋ = 2`, and the
conductor is `1`. It is a genuine deficit-positive weight (closure
multiplicity 0 against `m = 1`), and the value `c = 1` is confirmed by two
independent routes.

**What replaces it is a complete theorem, with no degree bound.**

> **Theorem (corrected transport formula).** For every `λ` with `m(λ) > 0`,
>
>     c(λ) = ⌊ (λ₁ − 2λ₃)/6 ⌋ − [ λ₁ = λ₂  and  λ₁ − 2λ₃ ≡ 1 (mod 6) ],
>
> the bracket being 1 when both conditions hold and 0 otherwise.

The correction term is a **parity obstruction**, and it is the exact analogue
of the phase/integrality parity that already governs World A. The failure
locus is one explicit congruence family, and on it the conductor falls short of
the shadow by exactly one step of the `T`-ray — never more.

Two further results, both answering questions posed in the paper:

- **The orphan locus is finite: exactly four weights.** `(10,1,1)`, `(13,1,1)`,
  `(11,11,2)`, `(17,17,5)` are the only `λ` with `m(λ) = 0` and shadow `≥ 1`,
  and there are no others at any degree. They form two dual pairs, and the
  orphan locus is stable under `λ ↦ λ* ⊗ det^k` **exactly** for `6 | k` —
  because `det|_H` has order exactly 6. That duality exchanges
  `p = λ₁−λ₂` with `q = λ₂−λ₃`, which is why the two `q = 0` orphans pair with
  the two `p = 0` orphans.
- **Remark 3.4's characterisation of the failure is also wrong.** It said
  attainment fails exactly on weights of empty support. In fact the two `p = 0`
  orphans are just the `m = 0` members of the parity family above, and there
  are weights with `m(λ) > 0`, shadow `≥ 1` and deficit `0` that are not
  orphans at all: `(23,23,8)`, `(29,29,11)`, `(35,35,14)`.

The engine of all of this is a reduction that removes the pole calculus
entirely: **the transversal family is a single torus orbit of a single fixed
point of the open orbit**, so the conductor is the top nonvanishing weight of
one linear-algebra object.

---

## 1. The reduction

### 1.1 The transversal family is a torus orbit

Take the family `f_s = x²y + s y³ + z³` through the cusp `p₀ = x²y + z³`, whose
stabiliser contains the torus `τ(ρ) = diag(ρ, ρ⁻², 1)` and whose normal
direction `y³` has `τ`-weight of size 6. Its Waring lines are

    l̂₁ = κ ρ⁻¹ (x + ρ³ y),  l̂₂ = −κ ρ⁻¹ (x − ρ³ y),  l̂₃ = z,
    κ = 6^(−1/3),   s = ρ⁶/3,

so that `f_s = l̂₁³ + l̂₂³ + l̂₃³`. The matrix `M(ρ)` whose rows are the `l̂ᵢ`
therefore factors

    M(ρ) = A · diag(ρ⁻¹, ρ², 1),        A = [[κ, κ, 0], [−κ, κ, 0], [0, 0, 1]]

with `A` **constant**: all the `ρ`-dependence sits in the torus. Equivalently,
writing `B` for the corresponding element of `GL(V)`,

> **Lemma A.** `f_s = τ(ρ) · (B·v)` with `s = ρ⁶/3`, where `B·v = x²y + y³/3 + z³`
> is a fixed point of the open orbit.

(Verified symbolically, `analysis/wk2_s23_lemmas.py::L1`, four independent
identities.) This is the whole mechanism: the degeneration is not a curve one
has to expand along, it is a one-parameter subgroup acting on one point.

### 1.2 The conductor as a top-weight condition

`Ω̄` is a hypersurface, hence Cohen–Macaulay; its singular locus is the cone
over `σ₂(v₃(P²))`, of codimension 3, and the cusp orbit — dense in the
boundary — consists of smooth points. So `Ω̄` is normal, `C[Ω̄]` is exactly the
subring of `C[G·v]` with no pole along `∂`, and `c(λ)` is the maximal pole
order in the `λ`-isotypic component (this is Definition 2.1's own reading).

Write the `λ`-isotypic component of `C[G·v] = C[G]^H` as matrix coefficients
`F(g) = ⟨φ, π_λ(g) w⟩` with `w` in the multiplicity space `S_λ^H`. By Lemma A,

    F(f_s) = Σ_ν ρ^ν ⟨φ, π_ν(B w)⟩ ,

`π_ν` the projection onto the `τ`-weight-`ν` subspace. Since `ρ ↦ ζ₆ρ` changes
`M(ρ)` only by an element of `H`, the left-hand side is a function of `s = ρ⁶/3`
alone; every surviving `ν` is therefore divisible by 6, and `ord_s = ν/6`.
Because `ord_∂` is `G`-invariant and `T^{-p}F` is nonvanishing on a dense open
subset of the boundary, evaluating on the curve at a generic `G`-translate
computes it exactly. Hence

> **Lemma B (the criterion).**
>
>     c(λ) = (1/6) · max { ν : π_ν( B · S_λ^H ) ≠ 0 }.

Here `S_λ` is taken with `τ`-weights `(1, −2, 0)` on `e₁, e₂, e₃`, so that the
largest weight available is `λ₁ − 2λ₃` and Lemma B immediately re-proves the
paper's upper bound `c ≤ ⌊μ_max/6⌋`. The orientation is forced: the opposite
one would bound the pole by `(2λ₁ − λ₃)/6`, contradicting the block-order
estimate, and it disagrees with the multiplicity tables on 74 of 74 weights
already at `δ ≤ 6` (`L4`). Scalars in `B` are irrelevant, because `B` preserves
the `GL₂ × GL₁` branching blocks of `S_λ` and that branching is
multiplicity-free, so distinct blocks cannot interfere.

**Regression (falsifier F1, not fired).** Lemma B reproduces the conductor read
off the multiplicity tables — `m(λ)` versus the closure multiplicity along the
`T`-ray, a computation sharing no code with the criterion — on **all 380
weights with `δ ≤ 10`** (322 of them with `m > 0`), and on **all 2361 weights
with `m > 0` and `δ ≤ 20`**. No `ν` outside `6Z` ever appears.

### 1.3 The combinatorial model

Realise `S_λ = ( C[e₁,e₂,e₃,f₁₂,f₁₃,f₂₃] / (Π) )_{(p,q)} ⊗ det^r` with
`Π = e₁f₂₃ − e₂f₁₃ + e₃f₁₂`, `p = λ₁−λ₂`, `q = λ₂−λ₃`, `r = λ₃`. The ideal is
principal, so `{Π}` is a Gröbner basis and the normal forms are the monomials
not divisible by `e₁f₂₃`. Because `μ₃³ ⊂ H` acts diagonally,

> **Lemma C.** `S_λ^H` is spanned by the `S₃`-symmetrisations
> `Θ(a,Q) = Σ_{π∈S₃} π·(e^a f^Q)·det^r` over **admissible shapes**: `|a| = p`,
> `|Q| = q`, and `nᵢ = aᵢ + Σ_j q_{ij} + r ≡ 0 (mod 3)` for `i = 1,2,3`.

This is the same class bookkeeping the paper's block-order estimate uses; here
it is on the vector side rather than the bracket side.

### 1.4 The class decomposition, and why everything is divisible by 6

`B` acts by `e₁ ↦ e₁+e₂`, `e₂ ↦ −e₁+e₂`, `e₃ ↦ e₃`, hence `f₁₂ ↦ 2f₁₂`,
`f₁₃ ↦ f₁₃+f₂₃`, `f₂₃ ↦ −f₁₃+f₂₃`, `det ↦ 2 det`. Every "down" choice in the
expansion lowers the `τ`-weight by exactly 3.

Group the six permutations into three pairs by `k = π⁻¹(3)`, the slot sent to
the untouched line. Writing `q_k̄` for the wedge count on the pair **not**
containing `k`, the top weight of the `k`-pair is

    N_k = μ − a_k − 2 q_k̄ ,      μ := λ₁ − 2λ₃ = p + q − r,

and the two permutations of the pair produce the *same* monomials at every
drop. Their combined generating polynomial is

> **Lemma D.**  `P_k(X,Y) = F(X,Y) + (−1)^{λ₁ − a_k} F(−X,−Y)`,
> `F(X,Y) = (1+X)^{a_i}(X−1)^{a_j}(1+Y)^{q_{ik}}(Y−1)^{q_{jk}}`,
>
> the coefficient of `X^u Y^w` being the coefficient at drop `T = u+w`, i.e. at
> weight `N_k − 3T`.

So **only the drops `T ≡ λ₁ − a_k (mod 2)` survive**: the symmetrisation is a
pure parity filter, nothing else. In particular at `T = 0` the top survives iff
`N_k` is even, which is the exact analogue of World A's phase condition.

> **Lemma E.** `N_k ≡ 0 (mod 3)` for every admissible shape and every `k`.

*Proof.* `n_k ≡ 0` gives `a_k + (q − q_k̄) + r ≡ 0`, so `a_k − q_k̄ ≡ −q−r`,
independent of `k`; hence `N_k ≡ μ + q + r ≡ p + 2q ≡ p − q ≡ 0 (mod 3)`, the
last step because `3 | |λ|`. ∎

Since `N_k ≡ λ₁ − a_k (mod 2)`, Lemma D makes every achievable `ν = N_k − 3T`
even, and Lemma E makes it divisible by 3. **Every achievable `ν` is divisible
by 6** — the single-valuedness of `F(f_s)` in `s`, recovered combinatorially.
(Checked directly on 147056 (shape, `ν`) pairs: `L3`.)

Consequently the achievable weight of a class is `N_k` if `N_k` is even and
`N_k − 3` if it is odd, and reaching `ν* = 6⌊μ/6⌋` requires

    s := a_k + 2 q_k̄  ∈  {ε, ε−3},        ε := μ mod 6.

---

## 2. The obstruction

> **Theorem 1 (parity obstruction).** If `λ₁ = λ₂` and `μ ≡ 1 (mod 6)` then
> `c(λ) ≤ ⌊μ/6⌋ − 1`.

*Proof.* `λ₁ = λ₂` means `p = 0`, so every `a_k = 0` and `s = 2q_k̄` is **even**.
Here `ε = 1`, so `ε − 3 < 0` and the only admissible target is `s = 1`, which is
odd. No class can reach `ν* = μ − 1`. By Lemma E the next available weight is
`μ − 4`, which is odd, hence unreachable too (Lemma D); the next is `μ − 7`. ∎

That is the entire mechanism, and it is invisible to the block-order estimate,
which sees only `μ_max`. It is also invisible to any sweep with `δ ≤ 11`: the
smallest weight in the family with `m(λ) > 0` is `(17,17,2)` at `δ = 12`, one
degree past the range on which Theorem 3.1 was tested.

**The two `p = 0` orphans belong to this family.** `(11,11,2)` (`μ = 7`) and
`(17,17,5)` (`μ = 7`) satisfy `p = 0`, `μ ≡ 1 (mod 6)`; they are the members
with `m(λ) = 0`. They were not a separate phenomenon.

---

## 3. Attainment

> **Theorem 2 (attainment).** If `m(λ) > 0` and we are **not** in the family of
> Theorem 1, the shadow maximum is attained: `c(λ) = ⌊μ/6⌋`. If we are in the
> family and `m(λ) > 0`, then `c(λ) = ⌊μ/6⌋ − 1` exactly.

The proof has two halves, and it is finite because of a periodicity.

### 3.1 Periodicity in `r`

`det|_H` has order exactly **6**: on `μ₃³` it is `ω^{a+b+c}` (order 3) and on
`S₃` it is the sign (order 2). Since `S_{λ+(1,1,1)} = S_λ ⊗ det`,
`m(λ) = dim Hom_H(det^{−r}, S_{(p+q,q,0)})` depends only on `(p, q, r mod 6)`.
The admissible shapes depend on `r` only mod 3, `ε` only on `r` mod 6, and the
coefficient signs of Lemma D only on `r` mod 2. Hence:

> **Lemma F.** `m(λ)` and the defect `⌊μ/6⌋ − c(λ)` are functions of
> `(p, q, r mod 6)` alone.

(Verified: `L5`, and again over `p, q ≤ 12`, all classes, no violation.) This
makes a sweep over `(p, q, j)` with `j = r mod 6` an **exhaustive** statement
about all weights with those `p, q`.

### 3.2 The construction

Given the target `ν*` (with `D = μ − ν*` equal to `ε`, or to `7` on the family),
build a shape whose slot 3 realises `s = a₃ + 2q₁₂ ∈ {D, D−3}` while the other
two slots are pushed strictly out of range, `a₁ + 2q₂₃` and `a₂ + 2q₁₃ ≥ s+3`
(`≥ s+6` when a drop `T = 1` is used), so that the class `k = 3` contributes to
`π_{ν*}` alone. Then:

- at `T = 0` the coefficient is `± 2^{q₁₂ + r + 1}` on the monomial
  `e₁^{p−a₃} e₃^{a₃} f₁₂^{q₁₂} f₁₃^{q−q₁₂}`, which contains no `f₂₃` and is
  therefore already a normal form — never zero;
- at `T = 1` the reduction of the `f₂₃`-monomial merges with the `e₂`-monomial,
  leaving coefficients `(a₁−a₂) + (q₁₃−q₂₃)` and `−(q₁₃−q₂₃)`; the contribution
  is nonzero iff `(a₁−a₂, q₁₃−q₂₃) ≠ (0,0)`.

The admissibility of the completion reduces to a single congruence,
`a₁ + q₁₃ ≡ −q₁₂ − r (mod 3)`, which is consistent with `s ≡ ε (mod 3)`
automatically (Lemma E), so it can always be met when the ranges are wide.

Concretely: `q₁₂ ≤ 2` always suffices to realise `s`; taking
`q₁₃, q₂₃ ≥ 4` unequal (`≥ 5` on the family) gives the separation, and the
congruence is fixed by moving `q₁₃` within `{⌊Q/2⌋ ± 6}`. So the construction
succeeds whenever `q` is at least about 12 (15 on the family), and separately
whenever `p` is large enough to do the same job on the singles side.

`construct()` in `analysis/wk2_s23_transport.py` implements exactly these rules
— no search over shapes. Over all `(p, q, j)` with `p, q ≤ 150` (45593 classes,
i.e. **every** `λ` with `λ₁ − λ₃ ≤ 300`, by Lemma F) it returns a shape that is
verified admissible and verified to give a nonzero normal form at `ν*` in
**45513** cases. The remaining **80** classes all lie in the finite region
`q ≤ 12`, `p ≤ 18`, and are settled by full brute force over *all* admissible
shapes: 0 failures. Among those 80, the classes with `m(λ) = 0` and shadow `≥ 1`
are exactly `(p,q,j) = (9,0,1), (12,0,1), (0,9,2), (0,12,5)`, i.e. the four
orphans.

**Why the family case lands at exactly one step down.** With `p = 0` the only
even `s ≡ μ ≡ 1 (mod 3)` values are `4, 10, 16, …`; `s = 4` gives
`N₃ = μ − 4` odd, hence `ν = μ − 7 = 6(⌊μ/6⌋ − 1)`. It needs `q₁₂ = 2` and
`q₁₃ ≠ q₂₃` both `≥ 5`, so `q ≥ 13`; with `3 | q` that is `q ≥ 15`, and the two
family members below it (`q = 9, 12`) are precisely the two `p = 0` orphans.
The `T = 1` degeneracy `q₁₃ = q₂₃` is what kills them.

### 3.3 What the sweep says

Over the same exhaustive range:

| statement | result |
|---|---|
| weights with `m > 0` where the original formula fails | exactly `{p = 0, μ ≡ 1 (mod 6)}`, 46 classes in range |
| any failure with `p ≥ 1` | none (falsifier G2 not fired) |
| family members that nevertheless attain | none (G3 not fired) |
| defect ever exceeding 1 | never (G4 not fired) |
| `m = 0` with shadow `≥ 1` | exactly 4 classes |

Independent confirmation against the multiplicity tables: all `m > 0` weights
with `δ ≤ 20`; all 16 family members up to `δ = 28`; a 600-weight random sample
at `δ = 21…28`. Zero disagreements (G1 not fired).

---

## 4. Orphans, and Remark 3.4

`det|_H` has order exactly 6, so for finite `H`,
`m(λ* ⊗ det^k) = m(λ)` **iff** `6 | k`. (Checked for `k = 1…24`: invariance
holds at `k = 6, 12, 18, 24` and fails at every other `k`.) That duality sends
`(p, q, r) ↦ (q, p, k − p − q − r)`: it **exchanges `p` and `q`**. Hence the two
`q = 0` orphans and the two `p = 0` orphans are one another's minimal `6|k`
twists:

    (10,1,1)* ⊗ det¹² = (11,11,2)      Weyl dims 55, 55
    (13,1,1)* ⊗ det¹⁸ = (17,17,5)      Weyl dims 91, 91

This answers the paper's question: **the orphan locus is stable under
`λ ↦ λ* ⊗ det^k`, with stabiliser exactly `6Z`.** But — contrary to the guess
recorded in Remark 3.4 — it is *not* the key to the attainment proof. It is an
elementary character fact, and the orphans it relates fail for two *different*
reasons: the `p = 0` pair by the parity obstruction of Theorem 1, the `q = 0`
pair by cancellation between the three slot-classes (their shapes have
`a_k` repeated, so two classes produce the same monomial with opposite signs).

Two corrections to Remark 3.4 as written:

1. **"Attainment fails exactly on weights of empty support" is false.** It fails
   on the whole parity family, most of which has `m(λ) > 0`.
2. **Empty support is not the same as a non-attained shadow with zero deficit.**
   `(23,23,8)`, `(29,29,11)`, `(35,35,14)` all have `m(λ) > 0`, shadow 1 and
   deficit 0 — they are exactly the family members whose shadow is 1, so the
   corrected formula sends them to `c = 0`.

Finally, the orphan locus is **finite**. Beyond the finite region it cannot
occur: `162·m(λ) = Σ_h χ_λ(h)`, the three scalar elements of `H` contribute
`3·dim S_λ` (using `3 | |λ|`), the elements with three distinct eigenvalues
contribute `O(1)` each by the bialternant (numerator bounded by 6, denominator
bounded away from 0 since all eigenvalues are 18th roots of unity), and the
elements with a repeated eigenvalue contribute `O(λ₁)`. Since
`dim S_λ = (p+1)(q+1)(p+q+2)/2` is cubic, `m(λ) > 0` outside a bounded region.
The exhaustive sweep to `p, q ≤ 150` locates that region and finds exactly the
four known orphans, at Weyl dimensions 55, 55, 91, 91.

---

## 5. The honest boundary

**Proved outright, no computation:**
Lemma A (symbolic identity), Lemmas C, D, E, F, and **Theorem 1** — the parity
obstruction, hence that Theorem 3.1's equality is *false*. The counterexample
`(17,17,2)` is independently confirmed by the multiplicity tables and needs no
part of this machinery to state or check.

**Proved modulo an explicit finite verification:**
**Theorem 2**. The construction of §3.2 is by rules, not search, and its
correctness at `T = 0` and `T = 1` is the elementary coefficient computation
above. What is *verified rather than argued in closed form* is that the
construction's range conditions hold outside the 80 exceptional `(p,q,j)`
classes, and the behaviour on those 80. Both are finite by Lemma F, and both
were checked exhaustively. A referee-proof version would replace "the
construction succeeds whenever `q ≥ 12`" by the corresponding chain of
inequalities written out; the content is the same, the bookkeeping is not yet
on paper.

**Not proved:**

- **Lemma B's orientation.** The dictionary between the paper's indexing of
  isotypic types and the `τ`-graded model `S_λ` was pinned by consistency with
  the (independently proved) block-order bound and by the 2361-weight
  regression, not by tracking the dualisation `V ↔ V*` through the
  Peter–Weyl identification. This is bookkeeping, but it is bookkeeping that has
  not been done, and it is the one place where a sign convention could in
  principle hide.
- **Normality of `Ω̄`** is used (hypersurface + singular locus of codimension 3)
  to identify `C[Ω̄]` with the pole-free subring. The codimension statement is
  standard for `σ₃(v₃(P²))` but is quoted, not verified here.
- **Finiteness of the orphan locus** has the character estimate of §4 as a
  proof sketch; the explicit constant that turns it into a bound was not
  computed. The sweep to `p, q ≤ 150` is the actual evidence.
- **The level-2 tower** (§7(1) of the paper) is untouched.

**What would break it:** a weight with `m(λ) > 0`, `p ≥ 1`, at which the
multiplicity tables give a conductor below `⌊μ/6⌋`; or a family member with
`m(λ) > 0` whose table conductor is not `⌊μ/6⌋ − 1`. Both were searched for
exhaustively in the ranges above and not found.

---

## 6. Consequences for the paper

- **Theorem 3.1** must be restated with the correction term. It then holds for
  *all* weights with `m(λ) > 0`, with no degree bound — a strictly stronger
  statement than the one it replaces, and one whose hypothesis is still the
  cheap, `Ω̄`-free character count.
- **Remark 3.4** must be rewritten: the orphan-pairing question is answered
  (`6 | k`, and it swaps `p` and `q`), and the "attainment fails exactly on
  empty support" sentence is false.
- **Question 7.1** is answered for World B. What remains open is the
  *general* conjecture, §7(4): the corrected law says that the naive
  `⌊μ_max/|w_N|⌋` is right only up to an arithmetic correction coming from the
  order of the stabiliser character on the degenerating slot — so the right
  general statement is presumably `⌊μ_max/|w_N|⌋` minus a parity defect
  determined by the finite stabiliser, not the bare floor. World A has defect
  identically 0; World B has a defect supported on one congruence family. That
  is a sharper conjecture than the one in §7(4), and a more likely true one.
