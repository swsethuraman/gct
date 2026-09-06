# Session 57 — the rank-loss selector: ladders, stable ranges, and where the kernel can be born

Branch `s57-selector` off `main` at `0960bd5`.  Pre-registration
`results/PREREG_s57.md`, committed at `905c1a2` **before any computation of the
session** (the brief is committed beside it as `docs/s57_prompt.md`).
Deliverables: this report; `results/s57_selector.md` (the table, the nominee
lists, the scores); `results/s57_cells/` (the banked per-cell data as
`csv.gz`, the census counts, the ladder and criterion analyses as JSON);
`analysis/wk9_s57_*.py`; logs `results/logs/s57_*`.  Every run bounded by
`timeout` and `ulimit -v`, pid recorded; two runs were ended early by their
recorded ids and are logged as such in `results/logs/s57_run_families.out`.
Exact integer arithmetic throughout; every `a` by two routes or two moduli.
Labels **proved** / **measured** / **adopted-from-literature** / **expectation**.
No rank was measured this session and no `D` is reported.  Delivered as a
bundle; nothing pushed.

---

## 0. Verdict

> **Cell selection is the wrong unit; the unit is the ladder.**  Write every
> weight as `λ = (4δ − |λ̄|, λ̄)` with the *tail* `λ̄ = (λ_2, …, λ_ℓ)`.
> Multiplication by the `s_1^4`-coefficient `c` (the highest-weight vector of
> `C[W]_1`) carries highest-weight vectors of weight `λ` in degree `δ` injectively
> to weight `λ + (4)` in degree `δ + 1`, on the ambient ring, on the ideal and
> on the coordinate ring of every irreducible `GL_ℓ`-stable cone (Lemma L,
> **proved**).  So `a`, `mult_det` and `i_det` are non-decreasing up each
> ladder `{(4δ − |λ̄|, λ̄) : δ}`, and `i_det` can grow at a step only by the
> increment of `a` there.  Moreover the whole ladder is constant from
> `δ = |λ̄|` on (Proposition S, **proved**): there `a` equals an explicit
> stable value `a_∞(λ̄)` — the multiplicity of `S_λ̄` in
> `Sym(Sym^2 ⊕ Sym^3 ⊕ Sym^4)(C^{ℓ−1})` — and `i_det` equals the multiplicity of
> `S_λ̄` in the ideal of the affine variety `M_ℓ` of *characteristic polynomials
> of traceless `(ℓ−1)`-dimensional pencils of `4×4` matrices*.  A rank drop is
> therefore either a genuinely projective phenomenon confined to the finite
> non-stable segment `δ < |λ̄|` of one ladder, or an equation of `M_ℓ`, which
> every cell of the ladder's stable range sees identically.

> **What the record now says, permanently.**  Of the 326 measured cells
> (210 six-row, 116 length-5; every one `mult_det = a`), <<N_IMPLIED>> were
> implied by a lower cell of the same ladder with the same `a` before they were
> measured.  Of the 100 six-row ladders the record touches, **34 are
> permanently dead** — the measured `a` already equals `a_∞`, so
> `i_det = 0` at every cell above the measurement, at every degree, and the
> corresponding isotypic component of `I(M_6)` is zero (**proved** given the
> measurements); the other 66 have room above (`a_∞ − a` from 1 to
> <<MAX_ROOM>>).  The peaked ladders `(4δ − 2(ℓ−1), 2^{ℓ−1})` are dead at
> every `ℓ ≤ 16` and every `δ ≥ ℓ` with **no measurement at all** (Theorem P,
> **proved**: `a_∞ = 1`, the unique highest-weight vector is the bordered
> discriminant `c·det G_2 − (3/8) g_1^T adj(G_2) g_1`, and it is nonzero at a
> generic pencil).  That covers <<N_PEAKED_MEASURED>> of the record's cells,
> including the thirteen `δ = 10` cells of s52.

> **The criteria (Task 2/3).**  *Closeness* `sk/a` (K2) is refuted as a
> prior: it ranks the known-dead cells first (median percentile <<K2_MED>> in
> their slices; <<K2_Q>>% in the first quartile).  *Balance* (K1) has no
> positive support anywhere: the one cell of the region with `i_det ≥ 1`, the
> LMR cell `(65,17,2^7)_24`, is among the <<LMR_SKEW>> most skewed of the
> 1,033,030 eligible weights of its slice, and K1's own first nominees at
> `δ ≤ 7`, `ℓ ≤ 6` are dead or untested; it survives the record only because
> the record is skewed by cost.  *LMR proximity* (K3) has exactly one positive
> and nominates dead cells almost as often as K2.  *Frontier degree* (K4) is
> the one criterion Proposition S justifies: the first stable cell of a ladder
> tests its whole isotypic component of `I(M_ℓ)` at once, and the ladders of
> tail weight 11 and 12 at `ℓ = 6` reach their stable range exactly at
> `δ = 11, 12`.

> **The LMR ladder.**  `a((4δ − 31, 17, 2^7), δ)` runs
> <<LMR_PROFILE>> for `δ = 12, …, 24`, and `a_∞((17,2^7)) = 274` — the ladder
> is already stable at the LMR cell.  <<LMR_FORCING>>

> **What to measure (for session 56).**  <<NOMINEE_SUMMARY>>

---

## 1. Two pieces of theory (proved)

Notation as in `docs/pieri_transport.md`: `V = C^ℓ` with basis `e_1, …, e_ℓ`
and dual coordinates `s_1, …, s_ℓ`; `W = Sym^4 V^*` the quartics; `G = GL(V)`
acting by substitution and on functions by `(g·h)(f) = h(g^{-1} f)`; `B ⊃ U`
the upper-triangular Borel and its unipotent radical (so `e_1` spans the
highest weight line of `V`); `T` the diagonal torus.  For a `GL_ℓ`-stable
irreducible closed cone `X ⊆ W` and a partition `λ ⊢ 4δ` with `ℓ(λ) ≤ ℓ`,

    a(λ,δ) = dim (C[W]_δ)^{hw}_λ,   i_X(λ,δ) = dim (I(X)_δ)^{hw}_λ,   mult_X(λ,δ) = a − i_X = dim (C[X]_δ)^{hw}_λ,

the last equality because `C[W]_δ → C[X]_δ` is a surjection of finite-dimensional
polynomial `G`-modules and taking highest-weight vectors of a fixed weight is
exact on those.  Let `c ∈ C[W]_1 = W^* = Sym^4 V` be `e_1^4`, the functional
`f ↦ [s_1^4] f`: a highest-weight vector of weight `(4, 0, …, 0)`.

### Lemma L (first-row transport)

*Let `X ⊆ W` be an irreducible `G`-stable closed cone with `X ⊄ {c = 0}`
(`X = W`, `D_ℓ`, `P_ℓ`, `R_ℓ` all qualify: `det(s_1 I_4) = s_1^4 ∈ D_ℓ`, and
`c(g·f) = f(g^{-1}e_1) ≠ 0` for generic `g` whenever `f ≠ 0`).  Write
`λ⁺ = (λ_1 + 4, λ_2, …, λ_ℓ)`.  Multiplication by `c` induces injections*

    (C[W]_δ)^{hw}_λ ↪ (C[W]_{δ+1})^{hw}_{λ⁺},    (I(X)_δ)^{hw}_λ ↪ (I(X)_{δ+1})^{hw}_{λ⁺},    (C[X]_δ)^{hw}_λ ↪ (C[X]_{δ+1})^{hw}_{λ⁺},

*hence*

    a(λ⁺,δ+1) ≥ a(λ,δ),    mult_X(λ⁺,δ+1) ≥ mult_X(λ,δ),    i_X(λ,δ) ≤ i_X(λ⁺,δ+1) ≤ i_X(λ,δ) + [a(λ⁺,δ+1) − a(λ,δ)].

*In particular `a(λ⁺,δ+1) = a(λ,δ)` forces `i_X(λ⁺,δ+1) = i_X(λ,δ)` and
`mult_X(λ⁺,δ+1) = mult_X(λ,δ)`.*

*Proof.*  `c` is `U`-invariant of `T`-weight `(4)`, so for a highest-weight
vector `h` of weight `λ` the product `ch` is `U`-invariant of weight `λ⁺`,
i.e. a highest-weight vector of weight `λ⁺` in degree `δ + 1`.  `h ↦ ch` is
injective on `C[W]` (a domain), maps `I(X)` into `I(X)` (an ideal), and is
injective on `C[X] = C[W]/I(X)` because `C[X]` is a domain (`X` irreducible)
and the image `c̄` of `c` is nonzero (`X ⊄ {c = 0}`).  Restricting the three
injections to highest-weight vectors gives the three displayed ones.  The
first two inequalities are their dimension statements; for the third,
`i_X(λ⁺,δ+1) = a(λ⁺,δ+1) − mult_X(λ⁺,δ+1) ≤ a(λ⁺,δ+1) − mult_X(λ,δ) =
a(λ⁺,δ+1) − a(λ,δ) + i_X(λ,δ)`, and `i_X(λ⁺,δ+1) ≥ i_X(λ,δ)` is the second
injection.  ∎

The **ladder** of a tail `λ̄ = (λ_2, …, λ_ℓ)` (a partition with `ℓ − 1`
positive parts) is `{(4δ − |λ̄|, λ̄) : 4δ − |λ̄| ≥ λ̄_1, δ ≥ ℓ}`; every cell
lies on exactly one ladder, and Lemma L says `a`, `mult_X`, `i_X` are
non-decreasing up it, with `i_X` growing at a step by at most the increment of
`a`.  Three mechanical consequences the session uses:

- **dead by transport** — a cell above a measured `i_det = 0` cell of the same
  ladder with the same `a` has `i_det = 0` (proved, given the measurement);
- **live room** — above a dead cell, `i_det ≤ a(cell) − a(dead cell)`;
- **downward forcing** — `i_det(λ,δ) ≥ i_det(λ⁺,δ+1) − [a(λ⁺,δ+1) − a(λ,δ)]`,
  so a known kernel forces kernels below it wherever `a` is constant.

The lemma is elementary and is the `c`-version of the `Δ`-ray monotonicity
already in the record (`docs/obstruction_power.md` §2, Ikenmeyer–Kandasamy
Lemma 5.2); what is new is only its use on the *slice* `D_ℓ`, where the
programme measures, and the pairing of the three injections.

### Proposition S (the stable range, and what it computes)

*Let `V' = span(e_2, …, e_ℓ)`, `Z = Sym^2 V'^* ⊕ Sym^3 V'^* ⊕ Sym^4 V'^*`
(so `C[Z] = Sym(Sym^2 V' ⊕ Sym^3 V' ⊕ Sym^4 V')` as a `GL(V')`-module), and for a
tail `λ̄` put*

    a_∞(λ̄) := mult of S_λ̄(V') in C[Z] = Σ_{2n_2 + 3n_3 + 4n_4 = |λ̄|} mult( S_λ̄, Sym^{n_2}(Sym^2 V') ⊗ Sym^{n_3}(Sym^3 V') ⊗ Sym^{n_4}(Sym^4 V') ).

*Then for every `δ`: `a((4δ − |λ̄|, λ̄), δ) ≤ a_∞(λ̄)`, with equality for all
`δ ≥ |λ̄|`.  For an irreducible `G`-stable cone `X ⊄ {c = 0}` there is a closed
`GL(V')`-stable subvariety `Z_X ⊆ Z` such that `i_X((4δ − |λ̄|, λ̄), δ) ≤
dim (I(Z_X))^{hw}_λ̄ =: i_X^∞(λ̄)` with equality for `δ ≥ |λ̄|`; for `X = D_ℓ`,*

    Z_D = M_ℓ := closure { (e_2, e_3, e_4)(A(s')) : A ∈ Hom(V', sl_4) },

*the characteristic-polynomial coefficients of traceless pencils, of dimension
`15ℓ − 30`.*

*Proof.*  Let `W_c = {c = 1}`, an affine space with coordinates the
coefficient functionals `c_α`, `α ≠ (4,0,…,0)`; each `c_α` has weight `α` under
the subtorus `T' = {t_1 = 1}` and *tail weight* `|ᾱ| = 4 − α_1 ≥ 1`.  A
polynomial `h ∈ C[W]_δ` satisfies `h(f) = c(f)^δ · h(f/c(f))` on `{c ≠ 0}`, so
`h ↦ φ := h|_{W_c}` is injective, and `h` is recovered from `φ` as
`c^δ φ(f/c)`, a polynomial exactly when `deg φ ≤ δ`.  `h` is a highest-weight
vector of weight `(4δ − |λ̄|, λ̄)` iff `φ` is invariant under the root groups
`N = {E_{1j}}` (the substitutions `s_1 ↦ s_1 + t·s'`, which fix `c`), invariant
under `U(V')`, and of `T'`-weight `λ̄` (the `s_1`-weight is then forced by
`|λ| = 4δ`).  `N` acts freely on `W_c` with the global slice `Z ≅ {g_1 = 0}`
(shift `s_1 ↦ s_1 − g_1/4`), `π : W_c → Z` is `GL(V')`-equivariant, and
`C[W_c]^N = π^* C[Z]`.  Hence

    a((4δ − |λ̄|, λ̄), δ) = dim { ψ ∈ C[Z]^{hw}_λ̄ : deg(ψ ∘ π) ≤ δ },

which is non-decreasing in `δ` and bounded by `a_∞(λ̄) = dim C[Z]^{hw}_λ̄`.  A
monomial in the `c_α` of tail weight `λ̄` has at most `|λ̄|` factors, so
`deg(ψ ∘ π) ≤ |λ̄|` for every `ψ` of weight `λ̄`, which gives equality for
`δ ≥ |λ̄|`.  The decomposition of `a_∞` is the `T'`-grading of `C[Z]`.  For
`X`, put `X_c = X ∩ W_c` (irreducible, `N`- and `GL(V')`-stable) and
`Z_X = π(X_c)`, closed because `W_c ≅ Z × N` as varieties; `h` vanishes on `X`
iff `φ` vanishes on `X_c` iff `ψ` vanishes on `Z_X`, so the same argument gives
the statement for `i_X`.  For `X = D_ℓ`: a generic determinantal quartic with
`c(f) ≠ 0` is `det(A_1 s_1 + A(s'))` with `A_1` invertible, `f/c = det(s_1 I +
A_1^{-1}A(s'))`, whose `s_1^3`-coefficient is `tr(A_1^{-1}A(s'))`; the shift by
`−g_1/4` replaces the pencil by its traceless part, and the remaining
coefficients are `e_2, e_3, e_4` of that pencil.  The dimension is
`15(ℓ − 1)` (traceless pencils) minus `15` (conjugation).  ∎

Two remarks.  (i) Lemma L's monotonicity is the `δ`-filtration of the fixed
space `C[Z]^{hw}_λ̄` by the degree of `ψ ∘ π`; the *non-stable* segment of a
ladder is exactly where that filtration is still growing, and a kernel born
there is a highest-weight vector whose dehomogenisation has ordinary degree
`δ < |λ̄|`.  (ii) `sk`, `h_pad`, `mult_pad`, `mult_red` and their kernels
stabilise on ladders by the same argument (the orbit `GL_16·det_4` for `sk`,
the normalisation ring of `docs/reducible_engine.md` for `h_pad`); only `a_∞`
has been put into a computable form here.

`a_∞(λ̄)` is computed as `Σ_w sgn(w) K_∞(w(λ̄ + ρ') − ρ')` over the Weyl group of
`GL(V')`, with `K_∞(μ)` the number of multisets of monomials of degree 2, 3 or
4 in `ℓ − 1` variables with exponent sum `μ` (a box DP with no degree index,
mod two primes, CRT; `analysis/wk9_s57_stable.py`).  **Checked** against the
s39 table: at every `ℓ = 6` cell of `δ = 12` in the stable range (`|λ̄| ≤ 12`,
7 cells) `a = a_∞` exactly; at every cell with `12 < |λ̄| ≤ 16` (82 cells)
`a ≤ a_∞`; and `a_∞((17,2^7)) = 274 = a((65,17,2^7),24)`, the integrator's
value.

### Theorem P (the peaked ladders are dead, at every length)

*For every `ℓ ≥ 2` and every `δ ≥ ℓ`, the cell `((4δ − 2(ℓ−1), 2^{ℓ−1}), δ)`
has `a = 1`, its highest-weight vector is (a scalar multiple of)*

    h = c · det G_2 − (3/8) · g_1^T adj(G_2) g_1 ,

*where `g_1 = [s_1^3] f ∈ V'^*` and `G_2` is the symmetric matrix of the quadric
`[s_1^2] f ∈ Sym^2 V'^*`, extended to degree `δ` by `c^{δ−ℓ}`; and `h` does not
vanish on `D_ℓ` for `ℓ ≤ 16`.  Hence `i_det = 0` at every cell of every peaked
ladder.*

*Proof.*  `a_∞((2^{ℓ−1}))` is the dimension of the `SL(V')`-invariants of
`C[Z]` of `T'`-weight `2(ℓ−1)` (the weight `(2^{ℓ−1})` is `det^2`).  In the
bracket description of `SL(V')`-invariants of the tensors `(q, C, F) ∈ Sym^2 ⊕
Sym^3 ⊕ Sym^4`, an invariant of weight `det^2` is a contraction with exactly
two `ε`-tensors of `ℓ − 1` slots each; a symmetric tensor can place at most one
index in each `ε`, so `C` (three indices) and `F` (four) cannot occur, and the
invariant is a polynomial in `q` alone of degree `ℓ − 1`: the discriminant.  So
`a_∞ = 1`, hence `a ≤ 1` on the whole ladder (Proposition S).  The displayed
`h` is a nonzero highest-weight vector of the right weight and degree
(`det(G_2 − (3/8) g_1 g_1^T) = det G_2 − (3/8) g_1^T adj(G_2) g_1` by the
rank-one expansion; the `3/8` is the `s_1^2`-coefficient of
`(s_1 − g_1/4)^4 + (s_1 − g_1/4)^3 g_1 + (s_1 − g_1/4)^2 g_2`), so `a = 1` for
`δ ≥ ℓ`.  At a generic determinantal point `f/c = det(s_1 I + A(s'))`,
`g_1 = tr A(s')` and `g_2 = e_2(A(s'))`, and (normalising `c = 1`)
`h(f) = det( G_2 − (3/8) g_1 g_1^T ) = disc( e_2(A) − (3/8)(tr A)^2 ) =
disc( −½ tr(A_0(s')^2) )` with `A_0 = A − (tr A / 4) I`: the
discriminant of the pull-back of the trace form of `sl_4` (non-degenerate, rank
15) along `s' ↦ A_0(s')`, which is non-degenerate for a generic linear map
`V' → sl_4` when `dim V' ≤ 15`.  ∎

Theorem P accounts for every peaked cell the programme has measured — the
`(4δ−8, 2^4)` family at `ℓ = 5` and `(4δ−10, 2^5)` at `ℓ = 6`, `δ = 6..10`,
including the `(30,2^5)_{10}` that the integrator and an external reviewer
named as the single best next test before s52 measured it — and every peaked
cell of the region at `ℓ = 6..10`, `δ ≤ 24`, with no further measurement.
The same index-counting shows that *any* tail `(x, 2^{ℓ−2})` with `x ≥ 3` is
`det^2 ⊗ S_{(x−2)}`, a covariant with two `ε`'s and `x − 2` free indices; the
LMR tail `(17, 2^7)` is the case `x = 17`, `ℓ = 9`, and LMR's equation is such
a covariant of degree 15 built from an `8 × 8` bordered-Hessian minor.

---

## 2. Task 1 — the table

The table is `results/s57_selector.md` with the per-cell data in
`results/s57_cells/` (`table_d{δ}_l{ℓ}.csv.gz` for the full slices,
`families.csv.gz`, `below_l6.csv.gz`, `short_ladders.json`, `census_counts.json`;
every value banked with its route in the `bank_*.jsonl` files, which are not
committed).  Coverage, as pre-registered:

- **C1** the census: 12,707,460 eligible cells in the 75 `(δ, ℓ)` chunks
  (`ℓ = 6..10`, `δ = 10..24`), exact; at `δ = 10, 11, 12` the counts agree with
  the s39 candidate counts chunk by chunk (V6).
- **C2** every cell of `δ = 10, 11, 12` — 71,501 cells, 69,967 with `a ≥ 1` —
  with all columns: `a` and `sk` from the s39 engine table (`a` re-verified at
  all 1,874 cells of `(10, 6)` and a sample across the other chunks by the
  modular Weyl route, V1; `sk` at three cells by the house Python route, V2),
  `h_pad` by the C engine at `d = 3` over the Pieri strips, `N_S` exact by the
  two-prime tail DP wherever the DP cost was within the cap or the merged
  lower bound left the cell inside the sparse frontier (<<N_EXACT>> of the
  69,967 cells; the rest carry the lower bound and the status `lb`), `n_χ~`,
  balance, `|Stab|`, the pad-forced kernel `max(0, a − h_pad)`, the Lemma-A flag
  `h_pad = 0`, and — from Lemma L against the record — the transport status
  and room.
- **C3/C4** the families: F1 (the LMR ladder) at every `δ = 12..24` (`a` by
  two routes at `δ ≤ 16`, by the Weyl route with two moduli above; `sk` at
  `δ ≤ 16`; `h_pad` at `δ ≤ 16`, pending above — the Weyl `d = 3` route took
  over ten minutes per cell and was ended by its recorded id; `N_S` exact
  everywhere); F2 (peaked) and F3 (LMR shapes `k = 3, 4, 5, 7`) at
  `δ = 12..24` with the same pattern (`ℓ = 10` cells above `δ = 16` have `a`
  pending: the Weyl route there has 13,122 surviving terms and was capped); F4
  (the most balanced eligible cells) at `δ = 13` for `ℓ = 6, 7` only — the
  character engine spends tens of minutes per balanced seven-row shape at
  `N = 52`, the run was ended by its recorded id, and the rest is pending.
- **C5** was not run; instead every `ℓ = 6` cell *below* the region
  (`δ = 6..9`, eligible, `a ≥ 1`: 58 + 258 + 591 + 1,079 cells) got the same
  columns, so that the scoring of the record and the nominee lists use one
  set of definitions.
- Beyond the pre-registration: the stable value `a_∞` for every tail of
  weight `≤ 16` at `ℓ = 6..10` (481 tails) and for every tail of the six-row
  record (100), with the first stable region cell of each open ladder and its
  cost.

What the columns say at a glance (`δ = 10, 11`; the `δ = 12` row of the same
table is in the selector file):

| δ | ℓ | cells `a ≥ 1` | units | `h_pad = 0` (Lemma A) | pad-forced | dense / sparse / beyond |
|---|---|---|---|---|---|---|
| 10 | 6 | 1,793 | 653,974 | 27 | 1,073 (60%) | 51 / 97 / 1,645 |
| 10 | 7 | 2,330 | 613,128 | 57 | 1,545 (66%) | 7 / 59 / 2,264 |
| 10 | 8 | 2,460 | 273,801 | 208 | 1,655 (67%) | 2 / 9 / 2,449 |
| 10 | 9 | 2,074 | 59,507 | 342 | 1,326 (64%) | 7 / 7 / 2,060 |
| 10 | 10 | 1,318 | 5,184 | 460 | 766 (58%) | 18 / 29 / 1,271 |
| 11 | 6 | 2,817 | 4,528,493 | 16 | 1,956 (69%) | 48 / 104 / 2,665 |
| 11 | 7 | 3,955 | 6,155,291 | 47 | 2,989 (76%) | 6 / 50 / 3,899 |
| 11 | 8 | 4,593 | 3,983,257 | 209 | 3,536 (77%) | 2 / 7 / 4,584 |
| 11 | 9 | 4,486 | 1,344,177 | 493 | 3,417 (76%) | 7 / 15 / 4,464 |
| 11 | 10 | 3,701 | 233,847 | 813 | 2,724 (74%) | 58 / 83 / 3,560 |

Three things in the table that shape the prior.

**The pad-forced kernel is a function of balance.**  At `(10, 6)` the
normalisation bound fires (`h_pad < a`) at 145 of 145 cells with balance
`≤ 8`, at 921 of 1,158 with balance 9–16, at 7 of 459 with balance 17–24 and
at 0 of 31 beyond; the same gradient holds in every chunk.  At the balanced
end it is not a small effect: the 145 balance-`≤ 8` cells of `(10, 6)` have
median `a = 124` and median `h_pad = 5`, so the pad ideal is forced to hold a
median of 118 of the 124 highest-weight vectors, and the two most balanced
cells are `(10,6,6,6,6,6)` (`a = 5`, `h_pad = 1`) and `(10,10,5,5,5,5)`
(`a = 8`, `h_pad = 0`, dead by Lemma A).  This is the §5 pre-check for K1 in
tabular form: whatever the determinant does at balanced weights, the padded
permanent is more degenerate there, and `D > 0` would need `i_det` to exceed a
forced `i_pad` in the hundreds.  (The onset question is unaffected by this;
the obstruction question is not.)

**The dense frontier at `ℓ = 6` is nearly exhausted by theorem.**  Of the 51
cells of `(10, 6)` with `n_χ~ ≤ 20,000`, 34 are dead by transport from the
record, 14 are bounded with room 1–13, and 3 are unconstrained with `a ≤ 3`;
the same holds at `δ = 11, 12` (<<DENSE_11_12>>).  What is left inside the old
frontier is a short list of one- and few-function tests (§5).

**`sk` dominates `a` everywhere and the cheap cells are the tight ones**, as
s38/s39 found; the largest-`a` cell of `(10, 6)` is `(14,10,7,5,3,1)` with
`a = 2,269` against `sk = 3,174,116` and `h_pad = 984`.

**The LMR ladder, sized** (pre-registration F1; batch review §8.4 asked for
this).  `a`: 2, 39, 93, 145, 188, 219, 241, 255, 264, 269, 272, 273, 274 for
`δ = 12..24`, two routes at `δ ≤ 16`, Weyl with two moduli above, and
`a_∞((17,2^7)) = 274` (Proposition S), so the ladder is stable from `δ = 24`
on — one step above the threshold at which the known equation lives.  `sk`:
2,714, 15,383, 26,654, 35,340, 41,463 at `δ = 12..16` (`≥ 41,463` at 24 by
transport).  `h_pad`: 15, 73, 159, 251, 331 at `δ = 12..16`, so `h_pad(24) ≥ 331
> 274 = a(24)`: the normalisation bound does **not** fire at the LMR cell
(pre-registered P9 refuted by transport, no pad-forced kernel there).  `N_S`:
`8.09·10^{10}` at `δ = 13` rising to `1.564·10^{11}` at `δ = 23` and
`1.5644·10^{11}` at `δ = 24` (the plateau of Proposition S), i.e.
`n_χ~ = 31,039,465` at the LMR cell and `1.6·10^7` at `δ = 13` — a factor of
`10^3` beyond the dense frontier and `10^2` beyond the sparse one.  On the
slice `Z` the same isotypic computation has `K_∞ = 7,212,907,703` monomials,
`K_∞/|Stab'| ≈ 1.43·10^6`: a factor 20 cheaper than the cell, still a factor
10 beyond the sparse route.

---

## 3. Task 2 — the criteria, each against evidence

The brief asks, for each criterion: what would confirm it, what would refute
it, and whether existing data bears on it.  The scoring machinery is
`analysis/wk9_s57_falsify.py` (percentile of a cell in its `(δ, ℓ)` slice of
eligible cells with `a ≥ 1` under the criterion's ordering; 0 = first nominee);
the numbers are in §4 and `results/s57_selector.md` §6.  One remark applies to
all of them and is worth stating once.  A criterion is a statement about
*where* in a slice the kernel sits, and the record can refute it only in slices
where the ideal is known to be non-empty — there are none.  So "the dead cells
rank low under K" is a weak test, which any criterion anti-correlated with
cheapness passes; the stronger tests are (i) *does the criterion's first
nominee in some slice already lie in the record?* and (ii) *where does the one
known live cell fall?*  Both are reported.

### K1 — balance (ascending `λ_1 − λ_ℓ`)

*Would confirm:* a first kernel at a cell in the balanced end of its slice
while the skewed cells of the slice are dead.  *Would refute:* a first kernel at
a skewed cell with the balanced cells of the same slice dead; or the balanced
first nominees dead across many slices while a kernel appears elsewhere.

*Evidence.*  (a) The one cell of the region with `i_det ≥ 1`, the LMR cell
`(65,17,2^7)_{24}`, has balance 63 in a slice whose balances run 15–87: K1
percentile 0.9954, rank 1,028,287 of 1,033,030 — only 3,869 cells of its slice
are more skewed.  This is the wrong direction, by a wide margin, and it is not
an accident of one weight: LMR's equations for `Dual_{k,d,N}` are of weight
`det^2 ⊗ S_{(2k+3)}` in the tail, i.e. two `ε`'s and a covariant of positive
degree, and every such module is maximally skewed for its length.
(b) The record's dead cells sit in the skewed half of K1 (median percentile
0.84; 9% in the first quartile), which is consistent with K1 but says nothing,
because the record was selected by cost and cost rises with balance.
(c) K1's first nominees: at `(δ, ℓ) = (6, 6)` and `(7, 6)` the most balanced
eligible cells `(6,4,4,4,4,2)`, `(7,6,4,4,4,3)`, `(7,7,4,4,3,3)` are unmeasured
(the record's `(8,4,4,4,4,4)_7` ties them at balance 4 and is dead); at
`δ = 8, 9, 10` the first nominees `(8,6,6,4,4,4)`, `(9,6,6,6,5,4)`,
`(10,6,6,6,6,6)` are unmeasured with `n_χ~` far beyond the frontier.  At
`ℓ = 5` the most balanced cells of `δ = 6` (`(6,6,4,4,4)`, balance 2) and
`δ = 7` (`(7,7,5,5,4)`, balance 3) are also unmeasured; s36's balanced `ℓ = 5`
stratum reached balance 4 and found nothing.
(d) The structural reading.  Eligibility `λ_1 ≥ δ` already excludes the
weights on which the folklore rests (the `SL`-invariants and their neighbours,
which have `λ_1 = |λ|/ℓ < δ` for `ℓ ≥ 5`); the most balanced *eligible* cells
are the ladder bottoms with the largest tails, `|λ̄| = 3δ`, whose stable range
begins at `δ' = 3δ`.  They are the cells that see the smallest fraction of
their ladder's eventual highest-weight space (`a` at the bottom against
`a_∞`: e.g. tail `(4^5)`, `a = 2` at `δ = 7` against `a_∞ = 13`).  A kernel
there would be a highest-weight vector whose dehomogenisation has ordinary
degree `δ` far below its tail weight `3δ` — possible, but the opposite of every
equation family that is known (LMR: degree 24 against tail weight 31; the
bordered discriminants: degree `ℓ` against `2(ℓ−1)`; the Macaulay cap
equations: degree 661 against tail weights in the thousands).

*Verdict:* no positive support anywhere; the one positive points the other
way; the balanced corner remains untested for the same reason it always was
(`n_χ~ > 3·10^5` at `δ = 8, 9`).  What survives of the folklore is a
conditional, made precise by Proposition S in §5: an equation of *low ordinary
degree* `δ` must sit on a ladder of tail weight at least the weighted onset
`m_0(ℓ)` of `I(M_ℓ)`, hence at `λ_1 ≤ 4δ − m_0(ℓ)`; the record now proves
`m_0(6) ≥ 13`, so any six-row equation of degree `δ ≤ 12` would have
`λ_1 ≤ 4δ − 13` — balanced in exactly that sense, and only in that sense.

### K2 — closeness (ascending `sk/a`)

*Would confirm:* a first kernel at a cell with `sk/a` in the lowest part of its
slice.  *Would refute:* the low-`sk/a` cells dead while a kernel appears at a
high-`sk/a` cell.

*Evidence.*  Refuted on both counts.  (a) The dead cells are K2's first
nominees: median percentile 0.163, 65% in the first quartile, 34% in the first
decile, and K2's first nominee is dead in *every* six-row slice `δ = 6..10` and
every length-5 slice `δ = 6..9` (the peaked cells, `sk/a = 8` at `ℓ = 5`,
`13` at `ℓ = 6`).  (b) The one live cell has `sk/a` in the hundreds:
`sk/a = 394, 287, …` along the LMR ladder at `δ = 13, 14, …` and
`sk(24) ≥ sk(16)` by transport.  (c) Theorem P explains why the tightest cells
are dead: the peaked ladders are rigid (`a_∞ = 1`), and their single
highest-weight vector is the bordered discriminant.  Closeness of source and
target dimensions is a dimension statement, and the brief's own diagnosis of
dimension screening applies to its continuous version.

### K3 — LMR proximity (ascending tail distance to `(2k+5, 2^{k+1})`)

*Would confirm:* kernels at the LMR-shaped tails of other lengths, or on the
LMR ladder below `δ = 24`.  *Would refute:* the LMR-shaped cells dead at
`ℓ ≤ 8` where the LMR module is proved empty (s55), with nothing else nearby.

*Evidence.*  (a) Exactly one positive, by construction (distance 0 at
`ℓ = 9`).  (b) At `ℓ = 6, 7, 8` the distance-0 cells are `λ(k,4)` for
`k = 3, 4, 5`, whose LMR vector is *not* in the ideal (s55: `k ≥ 6` is needed);
their ladders have `a_∞ = 49, 94, 166` and are unmeasured, so nothing bears on
them either way.  (c) K3 nominates dead cells almost as often as K2 (41% of
the dead cells in its first quartile), because the record is made of
tails-of-twos.  (d) The LMR ladder itself: `a` runs 2, 39, 93, 145, 188, 219,
241, 255, 264, 269, 272, 273, 274 over `δ = 12..24`; the increment at the last
step is exactly one, so the LMR equation is (modulo the `c`-multiples of lower
vectors) the *last* highest-weight vector to appear on its ladder, and
downward forcing (Lemma L) reaches no cell below 24: `i_det(23) ≥ i_det(24) −
1`, which is vacuous.  Pre-registered P8 resolved in its stated default
direction; no equation of degree 23 follows.  What does follow:
`i_det(23) ≤ i_det(24) ≤ i_det(23) + 1`.  Either `(61,17,2^7)_{23}` is dead,
in which case the LMR module is the whole kernel at 24 and is spanned by the
single vector born there; or it is live, in which case an equation of degree
23 exists at `ℓ = 9`.  The cell `(61,17,2^7)_{23}` is therefore the sharpest
single test of "nothing below 24" that exists, and its cost is sized in §5.

*Verdict:* supported by one cell whose mechanism is proved absent below
`ℓ = 9`; as an ordering it fails the record like K2.  Its content is better
carried by the ladder: the cells `(4δ − 31, 17, 2^7)` for `δ` just below 24
are the natural place to look for a *lower-degree* equation at `ℓ = 9`, and
their cost is now sized (§5, T3).

### K4 — the frontier (`δ = 11, 12` at `ℓ = 6`)

*Would confirm:* a kernel at a cheap cell of `δ = 11, 12`.  *Would refute:*
those cells dead — but a dead verdict there is now *informative*, which is
the point.

*Evidence.*  Proposition S turns this from a convenience into a criterion: a
ladder is tested completely by any cell at which `a = a_∞`, and at `ℓ = 6` the
ladders of tail weight 13–16 with `a_∞ ≥ 1` reach their stable value at
`δ = 8–12` (observed, `results/s57_selector.md` §5), so their first stable
region cells, at `δ = 10–12`, decide the corresponding components of `I(M_6)`
for every degree at once.  The record has already done this for every tail of
weight `≤ 12` (all seven with `a_∞ ≥ 1` are permanently dead: **`m_0(6) ≥ 13`**,
proved given the record), so the frontier cells of weight 13–16 are the next
rung.  Their costs are small — seven at `ℓ = 6` inside the dense frontier
(`n_χ~` 5,485 to 18,859), and at `ℓ = 7` and `8`, which no session has ever
measured, the first stable cells of the shortest open ladders cost
`n_χ~` 3,026 to 13,129.  This is the one criterion with a mechanism behind it.

### K5 — new room (Lemma L)

The operational form of Lemma L: rank cells by the number of highest-weight
vectors not obtained from a dead cell below.  Its nominees coincide with the
*next-room cells* of the record's ladders (`results/s57_selector.md` §4.1):
66 ladders touched by the record have room above, and at 22 of them the next
cell adds exactly **one** vector, five of those inside the dense frontier at
`δ = 10`: `(26,6,2,2,2,2)` (`n_χ~` 5,485, `a = 9 = a_∞`), `(22,12,3,1,1,1)`
(9,800, `a = 4 = a_∞`), `(21,13,3,1,1,1)` (11,489), `(23,11,2,2,1,1)`
(15,924, `a = 6 = a_∞`), `(23,9,5,1,1,1)` (19,239, `a = 13 = a_∞`).  Each is a
one-function test; a dead verdict at a stable one closes its ladder for good.

---

## 4. Task 3 — the score against the negative record

<<SCORE_SECTION>>

---

## 5. The prior, and the nominees

<<NOMINEES_SECTION>>

---

## 6. Pre-registration scorecard

| # | prediction (prior) | outcome |
|---|---|---|
| P1 | s39 `a` reproduces by the Weyl route at all 1,874 cells of `(10, 6)` and a sample elsewhere (0.95) | **<<P1>>** |
| P2 | K2 refuted as a closeness prior: ≥ 90% of the dead six-row cells in K2's first quartile (0.85) | **substance confirmed, threshold missed**: 65% in the first quartile, 34% in the first decile, and K2's first nominee is dead in every measured slice; the 90% was too strong because the balanced `ℓ = 5` stratum of s36 and the `(λ_1,λ_2,λ_3,1,1,1)` cells sit mid-slice |
| P3 | the LMR cell in the last K1 decile of its slice (0.85) | **confirmed**, percentile 0.9954 |
| P4 | dead cells mostly in the skewed half of K1 (median > 0.5); K1's first nominee at `(7, 6)` dead (0.8) | **confirmed on the median** (0.84); the `(7, 6)` nominee is a three-way tie at balance 4 of which one member, `(8,4,4,4,4,4)`, is dead and two are unmeasured |
| P5 | ≥ 40% of the 210 six-row dead cells implied by a lower dead cell with equal `a` (0.6) | **refuted**: 59 of 210 (28%); 34 of the 116 length-5 cells |
| P6 | ≥ 40 cells of `δ = 10–12` dead by transport, including every peaked `ℓ = 6` cell (0.8) | **confirmed**: <<P6>> |
| P7 | LMR ladder `a` non-decreasing, `a(24) = 274` (0.95) | **confirmed**, both |
| P8 | `a(23) < 274` (0.5), the alternative forcing a degree-23 equation | **the stated default holds**: `a(23) = 273`; no equation below 24 follows; the increment at the last step is exactly one |
| P9 | `h_pad(LMR cell) < 274` (0.7) | **refuted by transport**: `h_pad(16) = 331` and `h_pad` is non-decreasing up the ladder, so `h_pad(24) ≥ 331 > 274`; no pad-forced kernel at the LMR cell |
| P10 | `sk/a ≥ 10` on every F1 cell with `sk` (0.9) | **confirmed**: 1,357, 394, 287, 244, 221 at `δ = 12..16` |
| P11 | peaked ladders `a = 1`, `sk` constant `8, 13, 18, 21, 21, 18`; `ℓ = 6` dead by transport, `ℓ ≥ 7` unconstrained (0.9) | **confirmed and superseded**: the values hold at every tabulated `δ`, and Theorem P makes all of them dead at every `ℓ ≤ 16` without measurement |
| P12 | `ℓ = 6`, `δ = 11, 12`: fewer than 40 dense cells not dead by transport, all with `a ≤ 3` (0.6) | **half right**: 15 at `δ = 11` and <<P12_12>> at `δ = 12`, but their `a` runs up to 24 (`(28,8,2^4)_{11}`, room 9) — the cheap cells are not all rigid |
| P13 | no criterion has positive support except K3's one cell (0.7) | **confirmed as stated**, but the outcome is not the brief's "acceptable" one: Lemma L and Proposition S supply a prior with a mechanism (§5), and the record already proves `m_0(6) ≥ 13` |

Two things were decided after the pre-registration and are flagged: Proposition
S and Theorem P (§1) were derived during the session, after the first ladder
counts were seen; nothing pre-registered depends on them, and every consequence
drawn from them is checked against independently computed values (V4).  The F5
family (the record's ladders continued to `δ = 16`) was dropped once the
next-room cells of all 66 open ladders turned out to lie at `δ ≤ 10`; F4 was
cut short by cost.

---

## 7. Honest boundary

- **Coverage.**  All columns at `δ = 10–12`; the families above that; `sk`
  pending at `δ ≥ 17` everywhere and at `δ = 13–16` outside the families
  (session 58); `a` pending outside the families at `δ ≥ 13`; F4 beyond
  `(13, 7)` pending.  The table is designed for fill-in by `(δ, λ)`.
- **`n_χ~` is an estimate** (s46's correction), and the lower-bound rows are
  bounds; reach classes on those rows carry a `?`.
- **Proposition S is a theorem about `a`, `i_X`, `mult_X`; the explicit
  computable form is for `a_∞` only.**  `sk_∞`, `h_pad_∞` exist but were not
  put into a closed form; the report uses their monotonicity only.
- **"Permanently dead" rests on the record's verdicts**, which the record
  labels proofs (exact kernels at both primes, or one-sided non-singularity
  certificates); this session did not re-run any of them.
- **Theorem P's genericity step** (`disc(−½ tr A_0(s')^2) ≠ 0` for a generic
  pencil) is proved for `dim V' ≤ 15`; at `ℓ = 6..10` this is the whole
  region.  `analysis/wk9_s57_thmP_check.py` evaluates the bordered
  discriminant exactly (sympy, rationals) at random integer pencils for
  `ℓ = 6..10` and confirms both `h(f) ≠ 0` and the identity
  `h(f) = c^ℓ · disc(e_2(B) − (3/8) tr(B)^2)`, `B = A_1^{-1}A(s')`
  (`results/logs/s57_thmP_check.log`); the first version of that check had the
  power of `c` wrong and was ended — by a name pattern, against the process
  rule, which self-matched the shell and is recorded as a lapse in
  `results/logs/s57_run_families.out`.
- **The Weyl route at `ℓ = 10`** was capped (13,122 surviving terms); `a` at
  those cells comes from the engine alone at `δ ≤ 16` and is pending above.
- **`h_pad` on the LMR ladder above `δ = 16`** is pending; the P9 verdict uses
  monotonicity, which is proved (Lemma L for the normalisation ring).
- **Nothing here is an obstruction.**  No rank was measured; the nominees are
  where to measure, with reasons; `D` is not reported anywhere.
- **The criteria scores are against a record selected by cost**, and the
  report says in §3 why that makes "dead cells rank low" a weak test.

---

## 8. Corrections and notes for the integrator

1. **`results/sixrow_record.md` is not exhaustive at `δ = 6`.**  The slice
   `(6, 6)` has 58 eligible cells with `a ≥ 1` (62 units); the record holds 15
   of them.  The phrase "the measured set is not exhaustive at any degree
   `≥ 7`" is correct as written but invites the reading that `δ = 6` is
   exhaustive; it is not, and the two most balanced eligible cells there,
   `(6,4,4,4,4,2)` and `(6,6,4,4,2,2)`, are unmeasured.
2. **The `a = 1` peaked measurements were never necessary.**  Theorem P
   decides the whole family at every length; the record's nine peaked cells
   (`ℓ = 5, 6`, `δ = 6..10`) are confirmations.  More generally 59 of the 210
   six-row cells were implied by a lower cell of the same ladder before they
   were measured (Lemma L), and 34 of the 100 six-row ladders the record
   touches are closed for every degree.  Future measurement plans should be
   written in ladders: one stable cell per ladder.
3. **The batch review's §8.4 question** ("size `N_S` before committing" at the
   LMR cell) is answered: `N_S = 156,438,903,314`, `n_χ~ = 31,039,465`; on the
   slice `K_∞/|Stab'| ≈ 1.43·10^6`.  Neither is within reach of the dense or
   sparse routes.
4. **`docs/s55_report.md` §0** says "no construction below 24 … and none below
   9"; the ladder gives a sharper, cell-level statement at `ℓ = 9`: any
   equation of degree 23 at weight `(61,17,2^7)` would have to be one of the
   273 highest-weight vectors already present at that degree, and
   `i_det(23) ≤ i_det(24) ≤ i_det(23) + 1`.
5. **`docs/s57_prompt.md` §4** describes the balanced cells as "never measured
   at any length"; s36's stratum A measured `ℓ = 5` cells of balance 4–6 at
   `δ = 6` (e.g. `(8,4,4,4,4)_6`, `a = 2`, `mult_det = 2`) and the six-row
   record holds `(8,4,4,4,4,4)_7`.  Balance 2–3 is indeed unmeasured
   everywhere.
6. **The brief's count "266 negative measurements"** undercounts the length-5
   record: the ledgers of s36 hold 70 length-5 cells with a measured
   `mult_det` (60 of them not in s54's 56), so the reconciled negative record is
   326 cells (210 + 116), all `mult_det = a`.
7. **`PROJECT_NOTES.md`, the two papers and `docs/boundary_deficit.html` were
   not edited.**  Lemma L is the `c`-analogue of the `Δ`-ray monotonicity in
   `docs/obstruction_power.md` §2; if the integrator adopts the ladder
   language, that section is the natural place to cross-reference it.
