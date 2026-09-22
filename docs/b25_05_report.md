# B25-05 — the N = 9 → 7 reduction is proved on the record; the equivariance idea does not apply

**Slot:** B25-05 (reading and repair, no research pilots). **Worktree:** `work/batch15_workers/B15-01`,
branch `b15-01-ci159`. **HEAD:** `5a97317e7e28753261cf6e8dcece180a0e71b718`. This matches the
baseline at start and at close. **Session:** 2026-09-21T03:39:50Z start; close time in `results/b25_05/MANIFEST.json`. **Git was
read-only.** Nothing was staged, committed, stashed or reset. **Zero pilots, zero mathematical programs,
no lease.** Files written: this report and `results/b25_05/MANIFEST.json`. Both are **UNCOMMITTED**.

Labels follow CLAUDE_COMMON. Everything below is **producer-level** until B25-10 reviews it.

---

## Outcomes, up front

**Part A: registered outcome (a).** The reduction that s73 §1 calls "the programme's (★)
reduction" is a **PROVED** lemma on the record. It is `docs/isotypic_rank.md` (session 26),
Lemmas 3–4 and Proposition 5, and `docs/reducible_ideal.md` Cor. D later calls it "the programme's
standing lemma". s73 **adopts it by reference** without citing it. The s26 proof leaves two
elementary steps implicit:
(i) the highest-weight spaces for `GL_9` and `GL_7` are the same space;
(ii) ideal membership for `D_7`, which is not a `GL_7`-orbit closure.
B17-03 Lemmas 1–2 give both steps in general form. They are stated for quartics, but the proofs do
not depend on the degree. §A.3 gives a complete proof at `n = 3`, `N = 9`, `r = 7` and checks every
hypothesis. The range `ℓ(λ) ≤ 7` is closed, and the lemma holds for all `ℓ(λ) ≤ r ≤ 9`. The label
is **PROVED** (READ + independent hand re-derivation).

**Consequence for C45 (proposed, producer-level):** C45 becomes **PROVED**. Its only external input
is LMR Thm 2.3.1 + §§3.1–3.2, which is PRIMARY at statement level with the proofs not audited.
The "modulo (★)" qualifier would be discharged. B25-01/B25-02 keep the current qualifier until
B25-10 accepts this.

**Part B: registered outcome (c).** The proposal applies to the measured C45 nullity, and that
nullity comes from evaluation at a fixed finite set of points. No group acts non-trivially on its
domain, so no decomposition `Σ (dim V_μ) ν_μ` can constrain it (§B.2). The two equivariant repairs
are valid but vacuous, which is outcome-(b) behaviour. The first, the `GL_7`-equivariant
restriction map, turns the constraint into the definition `dim ker = dim S_λ · i_det`. The second,
the stabiliser/Frobenius route, gives `i_det ≥ a − m_det = 6 − 10 < 0`. Neither gives a floor.
No certificate is recommended.

---

## A. The exact internal reduction

### A.1 What s73 actually says (committed blob, read)

`82633a60:docs/s73_report.md` §1 (blob `de79c8dc…`, sha256(blob) `f40783ba…`):

> `D_7 = closure{det_3(Σ s_i A_i)}` and `P_7 = closure{per_3(Σ s_i A_i)}` in `Sym^3 C^7`,
> `A_i ∈ C^{3×3}` — the `7`-pencil slices of the `GL_9` orbit closures of `det_3` and `per_3` in
> `Sym^3 C^9`; by the programme's (★) reduction the `λ`-isotypic part of `C[GL_9·f]` is that of
> `C[X_7]` for `ℓ(λ) ≤ 7`.

s73 gives no citation and no proof, and "(★)" is defined nowhere else for this statement. In
the archive, "(★)" otherwise means the **different** Bruhat/reducible-locus monomial criterion
(`stabiliser_reduction.md` §4.2; `reducible_ideal.md` Theorem 1): a HWV lies in `I(X_r)` iff every
monomial has, for each `i`, a factor `c_α` with `α_i = 0`. **That theorem is not used anywhere
below.** I recommend retiring the "(★)" name for the restriction statement at the point of use (§C).

Read literally, "the `λ`-isotypic part is that of `C[X_7]`" is loose. The two isotypic components
are `S_λ(C^9) ⊗ M` and `S_λ(C^7) ⊗ M'`. They are different representations of different groups.
What is identified is the **multiplicity spaces**, as highest-weight spaces, together with their
ideal subspaces. §A.2 states it that way.

### A.2 Source/target diagram

```
 LMR, arXiv:1004.4802v1 §3.2                           record, s73 §1–§2(c)
 ─────────────────────────────                         ─────────────────────────────
 S^12(S^3 C^9) = C[W_9]_12,  W_9 = Sym^3 (C^9)^*        C[W_7]_12,  W_7 = Sym^3 (C^7)^*
 GL_9-module S_λ(C^9) ⊗ C^{a_9}                          GL_7-module S_λ(C^7) ⊗ C^{a_7}
 X^det = closure(GL_9·det_3) ⊂ W_9                       D_7 = closure Φ_det((M_3)^7) ⊂ W_7
   (affine cone over LMR's closure(GL(W)·[det_3]))        Φ_f(A_1..A_7) = f(Σ_{i≤7} s_i A_i)

 H^9 := HWV_{(λ,0,0)}(C[W_9]_12)   ≅ (ρ^*)   H^7 := HWV_λ(C[W_7]_12)          [R1–R2]
     ∪                                            ∪
 K_{X^det} := H^9 ∩ I(X^det)       ≅ (ρ^*)   K_{D_7} := H^7 ∩ I(D_7) = U_D      [R3–R5]

 ρ : W_9 → W_7 restriction of cubic forms to L = ⟨e_1..e_7⟩;
 ρ^* : C[W_7] ↪ C[W_9], c_α ↦ c_{(α,0,0)}  (the evaluation/restriction map, h = h̄∘ρ).
 λ = (19,7,2^5) ⊢ 36, δ = 12, n = 3, ℓ(λ) = 7 ≤ r = 7 ≤ N = 9.  Same diagram with f = per_3,
 X^per = closure(GL_9·per_3), P_7 = closure Φ_per((M_3)^7).
```

Conventions are those of `isotypic_rank.md` §1, and B17-03 re-derives them. `(g·F)(v) = F(g^{-1}v)`.
`c_α(F)` is the coefficient of `y^α`, and `wt(c_α) = α ≥ 0`. For `i ≠ j`,
`E_ij c_α = (α_i+1) c_{α+e_i−e_j}` if `α_j > 0` and `0` if `α_j = 0`, extended as a derivation. The
HWVs are the weight vectors killed by the upper-triangular simple `E_{i,i+1}`.

### A.3 Lemma R (length restriction) at `n = 3`, with every hypothesis checked

> **Lemma R.** Let `1 ≤ r ≤ N`. Let `f ∈ Sym^3 (C^N)^*`, `X = closure(GL_N·f)`, and
> `X_r = closure Φ_f(Hom(C^r, C^N))`, where `Φ_f(T) = f∘T`. For every `δ ≥ 0` and every `λ ⊢ 3δ`
> with `ℓ(λ) ≤ r`, `ρ^*` restricts to linear isomorphisms `H^r_{δ,λ} ≅ H^N_{δ,λ}` and
> `K_{X_r} ≅ K_X`. Hence `a_r = a_N`, `i_X = i_{X_r}` and `mult_X = mult_{X_r}`.
> Instance used: `N = 9 = n²`, `V_9 = M_3(C)`, `r = 7`, `f ∈ {det_3, per_3}`, and `X_7 = D_7`,
> resp. `P_7`, exactly as s73 §1 defines them.

*Proof.*

- **(R1) Weight support.** A monomial `Π_k c_{α^(k)}` has weight `Σ_k α^(k)`, and every entry is
  ≥ 0. So a monomial of weight `(λ_1..λ_r, 0..0)` uses only `c_α` with `supp α ⊆ [r]`. The weight
  space of `C[W_N]_δ` at `(λ,0^{N−r})` is therefore `ρ^*` of the weight-`λ` space of `C[W_r]_δ`.
  The map `ρ^*` is injective because it includes a polynomial subring. This uses only that
  exponents are non-negative, so it holds for cubics.
- **(R2) Raising operators.** For `i < r`, the formula for `E_{i,i+1}` involves only indices
  `≤ r`, so it agrees on the two rings: `E_{i,i+1}∘ρ^* = ρ^*∘E^{(r)}_{i,i+1}`. For `r ≤ i < N`,
  every `c_α` in the image has `α_{i+1} = 0`, so `E_{i,i+1} c_α = 0`. `E_{i,i+1}` is a
  derivation, so it kills the whole image. Hence `H^N_{δ,(λ,0)} = ρ^* H^r_{δ,λ}`.
- **(R3) Restriction identity.** If `h = ρ^* h̄`, then `h(F) = h̄(ρF)` for all `F ∈ W_N`.
- **(R4) The image of the orbit.** For `g ∈ GL_N`,
  `ρ(g·f)(s) = f(g^{-1} Σ_{i≤r} s_i e_i) = f(Σ s_i A_i)` with `A_i := g^{-1}e_i ∈ V_N`. As `g` runs
  over `GL_N`, `(A_1..A_r)` runs over exactly the linearly independent `r`-tuples, because
  `r ≤ N` lets any such tuple be completed to a basis. This is where `r = 7 ≤ 9` is used. These
  tuples form a nonempty Zariski-open subset of the irreducible affine space `V_N^r ≅ C^{63}`,
  so they are dense. `Φ_f` is polynomial, so for any polynomial `q` on `W_r`:
  `q` vanishes on `ρ(GL_N·f)` ⇔ `q∘Φ_f` vanishes on a dense open set ⇔ `q∘Φ_f ≡ 0` ⇔ `q` vanishes
  on `X_r`. Dependent tuples are included in `X_r`, which is s73's definition. No claim is made
  that the image of a closed set is closed.
- **(R5) Kernel identification.** Take `h = ρ^*h̄ ∈ H^N`. Then `h ∈ I(X)` ⇔ `h` vanishes on
  `GL_N·f` ⇔ (R3) `h̄` vanishes on `ρ(GL_N·f)` ⇔ (R4) `h̄ ∈ I(X_r)`. So `ρ^*(K_{X_r}) = K_X`. This
  step uses only vanishing, so it needs neither a dense `GL_r`-orbit on `X_r` nor Lemma 2 of
  `isotypic_rank.md`. That is the gap in the s26 write-up, which appeals to Lemma 2 (stated for
  orbit closures) for `D_r`, and `D_r` is not an orbit closure.
- **(R6) Multiplicities.** `X_r` is a `GL_r`-stable closed cone. Substituting `s ↦ g s` replaces
  `(A_i)` by linear recombinations, and `t^3 Φ_f(A) = Φ_f(tA)`. In characteristic 0,
  `I(X) ∩ M_λ = S_λ ⊗ U` with `U ≅ K_X` through the highest-weight line, and the same holds for
  `X_r`. So `i = dim K` and `mult = a − i` on both sides. `f` is arbitrary, and the determinant and
  permanent cases are the same argument. ∎

**Hypotheses at the C45 cell.** `n = 3` (unpadded, `f` = `det_3` or `per_3` on `M_3`). `N = 9`.
`r = 7`. `ℓ(19,7,2^5) = 7 ≤ 7`. `δ = 12`. `|λ| = 36 = 3·12`. Characteristic 0 is used only in R6.
The field is `C`. The modular computations enter only through the ceiling, §A.4. The endpoint
`ℓ(λ) = r` plays no special role, because R1 needs only `λ_j = 0` for `j > r`.

**Quartic-specific material is not used.** B17-03 Lemma 1 (restriction and multiplicity inheritance)
and Lemma 2 (arbitrary substitutions) are stated for `W_N = Sym^4`. Their proofs use only
non-negative exponents, the zero case of the raising formula, `r ≤ N`, and polynomiality of `T ↦ f∘T`.
I checked each of these step by step at degree 3, above, instead of transferring the statements.
B17-03 Lemmas 3–4 (Beauville density, padded restriction) and its main theorem **are**
quartic-specific, and nothing here uses them.

### A.4 The C45 chain, determinant and permanent separately

**Determinant: floor `i_det ≥ 1`.**
1. LMR §3.2, read by me (§E): *"A copy of the module with highest weight … in
   `S^{2n(n−1)}(S^n C^{n²})` is in the ideal of `closure(GL(W)·[det_n])`"*. The `n = 3` instance
   reads: *"the module with highest weight `12ω_1 + 5ω_2 + 2ω_7` occurs with multiplicity six in
   `S^{12}(S^3 C^9)`, but only one copy of it is in the ideal"*. The source is Thm 2.3.1, with §3.1
   giving `[det_n] ∈ Dual_{2n−2,n,n²}` (the dual is the Segre, of dimension `2n−2 = 4`).
   **PRIMARY, statement level. Proofs not audited.**
2. **Translation of the LMR object into the record's object, with each conversion checked.**
   - **Space.** LMR's equations are polynomials on `S^n W^*`, i.e. elements of `S^δ(S^n W)`. That
     is `C[W_9]` with `W = V_9 = M_3`. This is a polynomial `GL_9`-module, so the copy is
     `S_λ(C^9)` and not its dual.
   - **Weight.** For `SL_9`, `12ω_1 + 5ω_2 + 2ω_7` fixes `λ` up to full columns of length 9, and
     `|λ| = 3·12 = 36` fixes `λ = (19,7,2^5,0,0)`.
   - **SL versus GL.** Scalars act on degree 12 by a scalar (`t^{±36}`), so an `SL_9`-submodule of
     `C[W_9]_12` is a `GL_9`-submodule.
   - **Projective versus affine.** Scalars in `GL_9` scale `det_3` by all of `C^*`. So
     `closure(GL_9·det_3)` is the affine cone over LMR's `closure(GL(W)·[det_3])`, and the two
     have the same homogeneous ideal.
   - **Borel.** Any nonzero copy of `S_λ(C^9)` in `I_12` contains a nonzero vector of weight `λ`
     killed by the record's upper-triangular `E_{i,i+1}`.

   Hence `K_{X^det}(12,λ) ≠ 0` at `N = 9`.
3. Lemma R gives `K_{D_7}(12,λ) ≠ 0`, so `i_det(12) ≥ 1` for `D_7 ⊂ Sym^3 C^7`. **PROVED**, modulo
   the LMR statement in step 1.

**Determinant: ceiling `i_det ≤ 1`.** This is s73's nullity `1` at the house primes, with
`nullity_Q ≤ nullity_p` (B24-10 §3.1, accepted). It is measured directly on `D_7` and **does not
use Lemma R.**

**Permanent: `i_per = 0`.** This is s73's nullity-`0` certificate on `P_7` (`nullity_Q ≤ nullity_p = 0`;
B24-10 §3.2). LMR says nothing about the permanent, and none of its statements is used for it.
C45 compares `D_7` and `P_7` inside `Sym^3 C^7`, so **the permanent side needs no transport.**

**`D = i_det − i_per = +1` at `(λ, δ) = ((19,7,2^5), 12)`, `n = 3`, unpadded.** The label is
**PROVED**. External input: LMR (PRIMARY, statement level).

**Two corollaries of Lemma R, both producer-level:**
- **The same `D = +1` holds for the `GL_9` orbit closures in `Sym^3 C^9`.** Apply Lemma R with
  `f = per_3` and with `f = det_3`, transporting upward.
- **LMR's unproved "only one copy" (B24-02b §3.3) now follows.** It comes from the record's
  ceiling transported up: `i_det^{(9)} = i_det^{(7)} ≤ 1`. The record should still not *cite*
  LMR for it. It is a consequence of the record's ceiling, not of LMR.

**What the "multiplicity six" agreement is.** B24-02b and B24-10 §3.2 note that LMR's six at
`N = 9` equals s73's `a = 6` at `N = 7`. Under Lemma R this is a **consistency check on the
identification R1–R2**, because `a_9 = a_7` is part of the lemma. As the brief says, it
corroborates only the ambient multiplicity. The ideal-copy transport is R5, which is a proof and
not a corroboration.

### A.5 Record lineage and read-status of the reduction

| source (pin, blob) | what it contains | status for this use |
|---|---|---|
| `isotypic_rank.md` @`82633a60` (blob `4b204683…`) Lemmas 2–4, **Prop. 5** | the reduction, stated for `ℓ(λ) = r`, for any `f` on `M_3`. The proof is "combining Lemmas 2–4" and leaves R2 and R5 implicit | READ. The proof is a correct sketch with two elementary gaps |
| `s26_review.md` @`82633a60` (blob `3d420b63…`) §§1–4 | integrator review of s26. It re-computes the Theorem 6 Jacobian ranks and applies "the reduction … verbatim" to padding. It does not audit Prop. 5's proof line by line | READ |
| `reducible_ideal.md` @`82633a60` Cor. D | "the programme's standing lemma restated for `X^{(k)}`", for the reducible locus. Shows the record treats the lemma as proved | READ; context only |
| `b17_03_report.md` @`0cce6172` (blob `856a9fe9…`) **Lemmas 1–2** | full general proofs of R1–R5, stated for quartics | READ. Each step re-checked at `n = 3` (§A.3). Its own acceptance status is not relied on |
| `s73_report.md` @`82633a60` §1 | **adopts** the reduction by name ("the programme's (★) reduction") without citation | READ. Citation gap |
| this report §A.3 | complete proof at `n = 3`, `N = 9`, `r = 7` | independent hand re-derivation |

**Part A label: PROVED.** The reduction is not merely adopted, conditional or open. The missing
item was a **citation** at s73 §1, not a theorem. s73's use is ADOPTED-by-reference to a proved
lemma.

### A.6 A remark that is not load-bearing

At `N = 7 = k + 3`, LMR's subspace `F` is all of `W = C^7`. A general point of `D_7` is a general
`P^6`-section of the determinant hypersurface, which is irreducible by Bertini. Its dual lies in the
image of the Segre under restriction `P(W_9^*) ⇢ P(W_7^*)`, so it has dimension `≤ 4`. That would
put `D_7 ⊆ Dual_{4,3,7}` and give `i_det ≥ 1` from Thm 2.3.1 read at `N = 7`, with no transport at
all. I record it only as a possible second lineage. It relies on two classical facts I did not read
at source (UNREAD), and on reading Thm 2.3.1 at the pinch `N = k + 3`. **CONDITIONAL, not used.**

---

## B. The equivariance half-slot

### B.1 The proposal as recorded

Sources: `b24_12_ledger.md` @`f55ed57f` item 11, and B24-10 §8.2/§11.8. The suggestion is that
"the C45 nullity is constrained by equivariance to a sum `Σ_λ (dim V_λ)·ν_λ`", and it comes from
the user's thesis, Lemmas 18–19 (SO(n)-harmonics). The ledger's caution is that the thesis case is
multiplicity-free, while the programme's rings reduce to an `m_λ × m_λ` block and not to a scalar.
**The thesis itself is UNREAD by me.** I audit the shape as the record states it.

### B.2 The actual map, and why no group acts on it (outcome (c))

The C45 nullity is `nullity_F [E; ev_X]`, where `F = F_p` (or `Q` for the conclusion).
- **Domain.** `V_χ`, the `χ_λ`-isotypic reduction of the weight-`λ` monomial space of
  `C[W_7]_12`, under `Stab_W(λ) = S_5` on the five equal parts.
- **`E`.** The stacked simple raising operators, so `ker E = HWV_λ ≅ C^{a}`, `a = 6`.
- **`ev_X`.** Evaluation at `K = a + 8 = 14` fixed integer points of `X ∈ {D_7, P_7}`.
- **Codomain.** `F^{rows(E)} ⊕ F^{14}`.

Which group could act?
- **`GL_7`** does not preserve a single weight space, so it does not act on `V_χ`.
- **The torus `T_7`** acts on `V_χ` by the single character `λ`, i.e. by scalars.
- **The unipotent radical** acts trivially on `ker E`.
- **`S_5`** has already been quotiented out through `χ_λ`.

So on the domain that matters, `HWV_λ`, every available group acts through scalars. A decomposition
`Σ (dim V_μ) ν_μ` then has one term with `dim V = 1`, which is the tautology `nullity = ν`.

In the other direction, `ev_X` at a fixed finite point set is not equivariant for any non-scalar
subgroup of `GL_7`, because a generic set of 14 integer pencils is not stable under one. Over `F_p`
there is a further obstruction: modular representations are not semisimple, so the decomposition
step is unavailable for the measured nullity anyway. **So, as proposed, the idea is inapplicable to
the measured nullity: (c).**

### B.3 The equivariant repairs are valid but give no floor

- **(M2) Restriction map.** `R_λ : M_λ = S_λ(C^7) ⊗ C^6 → C[D_7]_12`.
  - *Setting:* group `GL_7`, field `C`, domain the λ-isotypic component, codomain the coordinate
    ring of the `GL_7`-stable cone `D_7`.
  - *Equivariance:* `D_7` is `GL_7`-stable (R6), so restriction commutes with `g·`.
  - *What it gives:* `ker R_λ = S_λ ⊗ U_D`, so `dim ker = dim S_λ(C^7) · i_det`. This is the shape
    `Σ (dim V) ν`, with one term and `ν = i_det`. By Schur, any equivariant endomorphism of `M_λ`
    has the form `id ⊗ B` with `B` a `6 × 6` block, not a scalar, which confirms the ledger's
    caution.
  - *Why no floor:* the constraint is the definition of `i_det`. A floor needs an independent lower
    bound on `dim ker`, and the equivariance does not supply one.
- **(M3) Stabiliser / Frobenius route.**
  - *Setting:* `C[closure(GL_9·det_3)] ↪ C[GL_9·det_3]`, which is `GL_9`-equivariant and
    injective because the orbit is dense. Alternatively, on the pencil side,
    `Φ^* : C[D_7] ↪ C[(M_3)^7]^{G'}`, where `G' = {(P,Q)}` acts by `A_i ↦ P A_i Q` with
    `det P det Q = 1`, plus transpose.
  - *What it gives:* `mult_det ≤ m_det(λ) = sk`, hence `i_det ≥ a − sk`. This is a genuine
    constraint and bypasses both LMR and Lemma R when it is positive.
  - *Why no floor:* the record gives `sk((19,7,2^5), 12) = 10` (`session_58.md`, "brute force
    agrees"; `sk` "is the house `m_det`"). I did not re-verify it (READ, MEASURED). It gives
    `i_det ≥ 6 − 10 = −4`, which is **vacuous**. This route gives a floor only when `a > m_det`,
    which is the occurrence-type situation, and this cell is not one. The conclusion would change
    only if the record's `sk = 10` were wrong and the true value were `≤ 5`. The known
    `mult_det = 5` forces `sk ≥ 5` in any case.

**Part B outcome: (c).** The map is not equivariant for any group that acts non-trivially on
`HWV_λ`, and evaluation at a fixed point set is not equivariant. The valid repairs (M2, M3) behave
like (b): the constraints are real but give no useful floor.

**Future certificate: none recommended.** Lemma R removes the motivation, since the only reason to
bypass (★) was that its label was unsettled. An LMR-free floor would need an exact identity
`h∘Φ_det ≡ 0` in `C[(M_3)^7]` for an explicit integer HWV `h`. That is a degree-36 polynomial in 63
variables. I have not priced it, and it is not a half-slot item.

---

## C. Proposed C45 wording at the point of use (for B25-01/02 **after** B25-10 review; not applied)

> **C45 (unpadded `n = 3` positive control).** At `δ = 12`, `λ = (19,7,2^5)`, in
> `Sym^{12}(Sym^3 C^7)` with `D_7`, `P_7` the 7-pencil families of `det_3`, `per_3`:
> `i_det = 1`, `i_per = 0`, `D = +1`. **PROVED.**
> Floor `i_det ≥ 1`: LMR arXiv:1004.4802v1 Thm 2.3.1, with §3.1 (`k = 2n−2`) and §3.2 (the `n = 3`
> instance, in `S^{12}(S^3 C^9)`); PRIMARY at statement level, proofs not audited. It is transferred
> to `D_7` by the length-restriction lemma (`isotypic_rank.md` Lemmas 3–4 / Prop. 5; complete proof
> at `n = 3`, `ℓ(λ) ≤ 7`, in B25-05 §A.3).
> Ceiling `i_det ≤ 1` and `i_per = 0`: s73 modular nullity certificates, using
> `nullity_Q ≤ nullity_p`.
> Do not cite LMR Thm 1.0.2. Do not take `i_det = 1` from LMR's example.

**Until B25-10 accepts this, the baseline "PROVED modulo (★)" stands.** Replace "(★)" with
"length-restriction lemma" wherever the N = 9 → 7 transfer is meant, so that it is not confused
with the reducible-locus (★).

---

## D. Limitations

- LMR is PRIMARY at **statement** level only. Thm 2.3.1's proof (§§2.2–2.3) and Thm 3.1.1's proof
  (§3.3) were not audited. C45's floor is exactly as strong as that reading.
- The ceiling and `i_per = 0` are s73 certificates, including the `χ`-reduction and evaluation
  families. I did not re-audit them; B24-10 §3.1–3.2 accepted them.
- Lemma R is new as a *complete written proof at n = 3* only. Its content is the record's s26
  Prop. 5, and I claim no priority.
- `sk = 10` in §B.3 is a record value that I did not re-verify. The Part B verdict (c) does not
  depend on it. Only the "vacuous" clause for M3 does.
- The thesis behind Part B is UNREAD. If its mechanism differs from the shape recorded in the
  ledger, §B audits the ledger's shape and not the thesis.
- The C45 scope stays as it was. Only the cell at `δ = 12`, only `n = 3`, unpadded. Nothing about
  padding, `n = 4`, or the `δ ≥ 12` ladder (Lemma L / Prop. S) is claimed here.

## E. Use-specific primary-source ledger

| source | exact version / bytes | used for | read-status |
|---|---|---|---|
| LMR, *Hypersurfaces with degenerate duals and the GCT Program* | arXiv:1004.4802**v1** PDF, re-downloaded 2026-09-21T03:42:19Z, sha256 `cfc28275a8c6b27f0ad6946d495ed4f889f7617df479be943d8d35718dbf2d79` (180 675 B), identical to the recorded hash. Text read from the ar5iv HTML, sha256 `fb5844ada6bec339638b584bcf385686935e96e03aa8f0ab9e2561bb0b316e05` (382 135 B), identical to B24-02b. My tag-strip is sha256 `4f01978272f392498edf02f9932cf2a8d20e662064f182cf99d05f17063803e9`, which differs from B24-02b's derived text because the extraction differs. Kept in the session scratchpad, not delivered | the §3.2 ideal-membership sentence and the `n = 3` instance; Thm 2.3.1 (the `ω_{k+3}` / `N ≥ k+3` construction, §2.3); §3.1 (dual of `det_n` = Segre, Thm 3.1.1 and the sentence after it); the §2.3 statement that the equations are polynomials on `S^n W^*` (for the space conversion) | **PRIMARY**, statements. Proofs not audited |
| Bertini; dual of a linear section | — | §A.6 remark only | UNREAD, not load-bearing |
| Sethuraman thesis (2009), Lemmas 18–19 | — | Part B shape, via the ledger | UNREAD (SECONDARY through `b24_12_ledger.md`) |

**Record inputs** (all READ from committed blobs; sha256 of blob content in the manifest):
`s73_report.md`, `isotypic_rank.md`, `s26_review.md`, `reducible_ideal.md`,
`stabiliser_reduction.md`, `lmr_cell.md`, `session_58.md` @`82633a60`; `b24_02b_report.md`,
`results/b24_02b/lmr_quotes.md` @`5a97317e`; `b24_10_review.md` and `results/b24_10/MANIFEST.json`
@`ab2f8a40`. The manifest's sha256 is `ba6aea51…`, which matches SOURCE_INDEX. Also
`b24_12_ledger.md` @`f55ed57f` and `b17_03_report.md` @`0cce6172`.

**Line-ending check.** The archive working copy of `s73_report.md` is CRLF, sha256
`add70bef…`. The committed blob content is sha256 `f40783ba…`, which matches B24-02b's binding.
The quotations are taken from the blob.

**Verification method.** READ plus independent hand re-derivation (Lemma R, the LMR-to-record
conversion, and Part B). No REPLAY, and no evaluator. **Tool memory:** I consumed the session
memory index, which includes a note on the B24-02 C45 citation and a note that PDF text extraction
is unavailable. I treated both as leads only and re-checked them against sources. After drafting I
created one memory file recording this outcome. It sits outside the repository and is not an input
to anything here.

## F. Resources

Pilots: **0**. Mathematical programs: **0**. Compute lease: **not requested**. Tools used: `git`
(read-only: `show`, `rev-parse`, `grep`, `ls-tree`, `cat-file`, `status`, `branch`), `curl` (two
GETs of public arXiv/ar5iv pages), `sha256sum`, `sed`, `tr`, `grep`, `wc`, `file`, `find`, `date`.
No interpreter was launched.

## G. Files and bindings (UNCOMMITTED)

| path | state |
|---|---|
| `docs/b25_05_report.md` | created. **UNCOMMITTED.** Its hash is in the manifest |
| `results/b25_05/MANIFEST.json` | created. **UNCOMMITTED.** Not self-hashed |

Baseline commit `5a97317e7e28753261cf6e8dcece180a0e71b718`. No delivery commit exists. A separately
authorised pass must commit these explicit paths and verify the blobs before B25-10 can accept them.
No paper, s73, old packet, or coordinator ledger was edited.
