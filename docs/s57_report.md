# Session 57 — the rank-loss selector: ladders, stable ranges, and where the kernel can be born

Branch `s57-selector` off `main` at `0960bd5`.  Pre-registration
`results/PREREG_s57.md`, committed at `905c1a2` **before any computation of the
session** (the brief is committed beside it as `docs/s57_prompt.md`).
Deliverables: this report; `results/s57_selector.md` (the table, the nominee
lists, the scores); `results/s57_cells/` (the banked per-cell data as
`csv.gz`, the census counts, the ladder and criterion analyses as JSON);
`analysis/wk9_s57_*.py`; logs `results/logs/s57_*`.  Every run bounded by
`timeout` and `ulimit -v`, pid recorded; the runs that were ended early were
ended by their recorded ids and are logged in
`results/logs/s57_run_families.out`, together with one lapse (§7).
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
> (210 six-row, 116 length-5; every one `mult_det = a`), 93 (59 six-row, 34 length-5) were
> implied by a lower cell of the same ladder with the same `a` before they were
> measured.  Of the 100 six-row ladders the record touches, **34 are
> permanently dead** — the measured `a` already equals `a_∞`, so
> `i_det = 0` at every cell above the measurement, at every degree, and the
> corresponding isotypic component of `I(M_6)` is zero (**proved** given the
> measurements); the other 66 have room above (`a_∞ − a` from 1 to
> 570 (median 13)).  The peaked ladders `(4δ − 2(ℓ−1), 2^{ℓ−1})` are dead at
> every `ℓ ≤ 16` and every `δ ≥ ℓ` with **no measurement at all** (Theorem P,
> **proved**: `a_∞ = 1`, the unique highest-weight vector is the bordered
> discriminant `c·det G_2 − (3/8) g_1^T adj(G_2) g_1`, and it is nonzero at a
> generic pencil).  That covers nine of the record's cells — the peaked
> `ℓ = 5` and `ℓ = 6` families at `δ = 6..10` — among them s52's
> `(30,2^5)_{10}`, the cell the integrator and an external reviewer had named
> as the single best next test.

> **The criteria (Task 2/3).**  *Closeness* `sk/a` (K2) is refuted as a
> prior: it ranks the known-dead cells first (median percentile 0.16 in
> their slices; 65% in the first quartile).  *Balance* (K1) has no
> positive support anywhere: the one cell of the region with `i_det ≥ 1`, the
> LMR cell `(65,17,2^7)_24`, is among the 0.4% most skewed of the
> 1,033,030 eligible weights of its slice, and K1's own first nominees at
> `δ ≤ 7`, `ℓ ≤ 6` are dead or untested; it survives the record only because
> the record is skewed by cost.  *LMR proximity* (K3) has exactly one positive
> and nominates dead cells almost as often as K2.  *Frontier degree* (K4) is
> the one criterion Proposition S justifies: the first stable cell of a ladder
> tests its whole isotypic component of `I(M_ℓ)` at once; the open ladders of
> tail weight 13–16 at `ℓ = 6` reach their stable values by `δ = 8–12`
> (observed), so the frontier cells decide whole components of `I(M_6)`, and
> the record has already closed every tail of weight `≤ 12`.

> **The LMR ladder.**  `a((4δ − 31, 17, 2^7), δ)` runs
> 2, 39, 93, 145, 188, 219, 241, 255, 264, 269, 272, 273, 274 for `δ = 12, …, 24`, and `a_∞((17,2^7)) = 274` — the ladder
> is already stable at the LMR cell.  The last increment is exactly one, so `a(23) = 273 < 274` and the downward forcing of Lemma L reaches no cell below 24: pre-registered P8 resolved in its stated default direction, and no equation of degree 23 follows.  What follows instead is `i_det(23) ≤ i_det(24) ≤ i_det(23) + 1` — the cell `(61,17,2^7)_{23}` is the sharpest single test of "nothing below 24", and it costs `n_χ~ ≈ 3.1·10^7` (`N_S = 1.564·10^{11}`), the same as the LMR cell itself, which is now sized at `N_S = 156,438,903,314`, `n_χ~ = 31,039,465`; the normalisation bound does not fire there (`h_pad ≥ 331 > 274`), so no pad kernel is forced at the LMR cell and the multiplicity comparison `D` there remains open.

> **What to measure (for session 56).**  Think in ladders, and measure one stable cell per ladder.  **T1** — the eleven *room-one* cells: ladders the record touches whose next cell adds exactly one highest-weight vector; seven are inside the dense frontier (`n_χ~` 5,485–19,239), six of those at a cell where `a = a_∞`, so each is a one-function test that either exhibits the first six-row equation or closes its ladder for every degree.  **T2** — the first stable cells of the open short ladders (tail weight 13–16): thirteen inside the dense frontier, seven at `ℓ = 6`, five at `ℓ = 7` and one at `ℓ = 8` — the `ℓ ≥ 7` ones are the cheapest measurements the programme has never made (`n_χ~` from 3,026).  **T3** — the LMR ladder at `δ = 21–24`, where `a` is within five of its stable value, for an engine that reaches `n_χ ≈ 3·10^7` or works on the slice (`K_∞/|Stab'| ≈ 1.4·10^6`).  **T4** — the balanced corner, unchanged in cost (`n_χ~ ≥ 1.3·10^6`) and now known to be where the pad ideal is forced first; only for the onset question.

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
LMR tail `(17, 2^7)` is the case `x = 17`, `ℓ = 9`: LMR's equation is such a
covariant of degree 15 (their construction takes `(k+2) × (k+2)` minors of
the Hessian; that the two `ε`'s are that minor is a reading of the weight, not
a re-derivation of their construction).

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
- **C2** every cell of `δ = 10, 11, 12` — 71,501 cells, 64,357 with `a ≥ 1` —
  with all columns: `a` and `sk` from the s39 engine table (`a` re-verified at
  all 1,874 cells of `(10, 6)` and a sample across the other chunks by the
  modular Weyl route, V1; `sk` at three cells by the house Python route, V2),
  `h_pad` by the C engine at `d = 3` over the Pieri strips, `N_S` exact by the
  two-prime tail DP wherever the DP cost was within the cap or the merged
  lower bound left the cell inside the sparse frontier (15,695 of the
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
the same holds at `δ = 11, 12` (48 dense cells at `δ = 11` of which 15 are not dead by transport (13 bounded, 2 unconstrained, `a` up to 24, five with room 1); 47 at `δ = 12` of which 14 (13 bounded, 1 unconstrained, `a` up to 25, five with room 1)).  What is left inside the old
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
transport).  `h_pad`: 10, 73, 159, 251, 331 at `δ = 12..16`, so `h_pad(24) ≥ 331
> 274 = a(24)`: the normalisation bound does **not** fire at the LMR cell
(pre-registered P9 refuted by transport, no pad-forced kernel there).  `N_S`:
`8.09·10^{10}` at `δ = 13` rising to `1.564·10^{11}` at `δ = 23` and
`1.5644·10^{11}` at `δ = 24` (the plateau of Proposition S), i.e.
`n_χ~ = 31,039,465` at the LMR cell and `1.6·10^7` at `δ = 13` — a factor of
`10^3` beyond the dense frontier and `10^2` beyond the sparse one.  On the
slice `Z` the same isotypic computation has `K_∞ = 7,212,907,703` monomials,
`K_∞/|Stab'| ≈ 1.43·10^6`: a factor 20 cheaper than the cell, still a factor
10 beyond the sparse route.

**A regularity across the LMR family (F3), not pre-registered.**  On the
ladder of every LMR shape the stable value is reached *exactly* at the LMR
degree, and the last step is exactly one:

| k | ℓ | tail | a_∞ | a at δ = 3(k+2) − 1 | a at the LMR degree 3(k+2) | first stable δ observed | bound `|λ̄|` |
|---|---|---|---|---|---|---|---|
| 3 | 6 | `(11,2^4)` | 49 | 48 (δ = 14) | **49** (δ = 15) | 15 | 19 |
| 4 | 7 | `(13,2^5)` | 94 | 93 (δ = 17) | **94** (δ = 18) | 18 | 23 |
| 5 | 8 | `(15,2^6)` | 166 | 165 (δ = 20) | **166** (δ = 21) | 21 | 27 |
| 6 | 9 | `(17,2^7)` | 274 | 273 (δ = 23) | **274** (δ = 24) | 24 | 31 |

So `λ(k,4)` is, for `k = 3..6`, the first stable cell of its ladder, and the
LMR degree `3(k+2)` is the degree at which the *last* highest-weight vector of
its tail is born — the vector of maximal ordinary degree in the
`λ̄`-isotypic part of `C[Z]`.  For `k ≥ 6` that vector (or the one new
direction it spans, modulo `c`-multiples of lower ones) is the LMR equation;
for `k = 3, 4, 5` the same last-born vector exists and does not vanish on
`D_ℓ` (s55).  This is measured at four values of `k`, not proved; it predicts
`a((69,19,2^8), 26) = 428` and `a((73,19,2^8), 27) = 429 = a_∞((19,2^8))` at
`k = 7`, `ℓ = 10`, where the ladder is tabulated only to `δ = 16` (`a = 167`)
because the Weyl route at ten rows was capped — a cheap check for a later
session (**expectation**).

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
degree, and every such module is extremely skewed for its length.
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
degree `δ` far below its tail weight `3δ` — possible, but the opposite of the
equation families whose types are known (LMR: degree 24 against tail weight
31; the bordered discriminants: degree `ℓ` against `2(ℓ−1)`; the isotypic
types of the degree-661 cap equations are not on record).

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

(e) The regularity of §2: at every `k = 3..6` the LMR cell is the first
stable cell of its ladder and the LMR degree is where the last highest-weight
vector of the tail is born.  Whatever the LMR construction is doing, it is
producing the *top-degree* vector of its isotypic type, which is a statement
about ladders, not about proximity in shape.

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
66 ladders touched by the record have room above, and at 11 of them the next
cell adds exactly **one** vector, seven of those inside the dense frontier:
`(26,6,2,2,2,2)_{10}` (`n_χ~` 5,485, `a = 9 = a_∞`), `(22,12,3,1,1,1)_{10}`
(9,800, `a = 4 = a_∞`), `(22,7,2,2,2,1)_9` (9,928, `a = 7 = a_∞`),
`(21,13,3,1,1,1)_{10}` (11,489), `(23,11,2,2,1,1)_{10}` (15,924,
`a = 6 = a_∞`), `(19,4,3,2,2,2)_8` (16,593, `a = 2 = a_∞`), `(23,9,5,1,1,1)_{10}`
(19,239, `a = 13 = a_∞`).  Each is a one-function test; a dead verdict at a
stable one closes its ladder for good.

---

## 4. Task 3 — the score against the negative record

The machinery and its caveat are in §3.  Percentiles of the 324 eligible dead cells in their `(δ, ℓ)` slices (0 = the criterion's first nominee; the two onset-only dead cells `(4^6)_6` and `(6,6,6,6,2,2)_7` lie outside every eligible slice):

| criterion | min | q1 | median | q3 | max | in first quartile | in first decile | ranked first in its slice |
|---|---|---|---|---|---|---|---|---|
| K1 balance | 0.000 | 0.567 | 0.840 | 0.962 | 0.999 | 9% | 3% | 0.3% |
| K2 closeness `sk/a` | 0.000 | 0.066 | 0.163 | 0.310 | 0.838 | 65% | 34% | 2.8% |
| K3 LMR shape | 0.000 | 0.140 | 0.323 | 0.533 | 0.996 | 41% | 19% | 0.9% |

Per slice, the first nominee of each criterion and whether it is already dead (`results/s57_selector.md` §6.1 has every slice):

| (δ, ℓ) | slice | dead | K1 first (balance) | dead? | K2 first (`sk/a`) | dead? | K3 first | dead? |
|---|---|---|---|---|---|---|---|---|
| (6, 5) | 105 | 44 | `(6,6,4,4,4)` (2) | no | `(16,2,2,2,2)` (8) | yes | `(10,8,2,2,2)` | no |
| (7, 5) | 238 | 48 | `(7,7,5,5,4)` (3) | no | `(20,2,2,2,2)` (8) | yes | `(13,9,2,2,2)` | yes |
| (8, 5) | 434 | 12 | `(8,6,6,6,6)` (2) | no | `(24,2,2,2,2)` (8) | yes | `(17,9,2,2,2)` | no |
| (9, 5) | 705 | 12 | `(9,7,7,7,6)` (3) | no | `(28,2,2,2,2)` (8) | yes | `(21,9,2,2,2)` | no |
| (6, 6) | 58 | 15 | `(6,4,4,4,4,2)` (4) | no | `(14,2,2,2,2,2)` (13) | yes | `(8,8,2,2,2,2)` | yes |
| (7, 6) | 258 | 72 | `(7,6,4,4,4,3)` (4) | no | `(18,2,2,2,2,2)` (13) | yes | `(10,10,2,2,2,2)` | yes |
| (8, 6) | 591 | 67 | `(8,6,6,4,4,4)` (4) | no | `(22,2,2,2,2,2)` (13) | yes | `(13,11,2,2,2,2)` | no |
| (9, 6) | 1079 | 41 | `(9,6,6,6,5,4)` (5) | no | `(26,2,2,2,2,2)` (13) | yes | `(17,11,2,2,2,2)` | no |
| (10, 6) | 1793 | 13 | `(10,6,6,6,6,6)` (4) | no | `(30,2,2,2,2,2)` (13) | yes | `(21,11,2,2,2,2)` | no |

Reading.  **K2 is refuted**: its first nominee is dead in every one of the nine measured slices, 65% of the dead cells sit in its first quartile, and the one live cell has `sk/a` in the hundreds.  **K3 fails the same test** at three of the nine slices and nominates dead cells at 41% in the first quartile; its single positive is the cell it was built from.  **K1 is consistent with the record** (median 0.84, 9% in the first quartile) but *only* because the record is skewed by cost; its first nominees are unmeasured in every slice except `(7, 6)`, where the tie at balance 4 contains the dead `(8,4,4,4,4,4)`; and the one live cell is in its last half-percent.  None of the three would have picked the LMR cell out of its slice of a million; K3 picks it by construction and nothing else.

The stronger reading of the record is the one Lemma L and Proposition S give: 93 of the 326 cells were implied before they were measured, 34 six-row ladders are closed for every degree, all seven six-row tails of weight `≤ 12` with a highest-weight vector are closed (`m_0(6) ≥ 13`), and the remaining 66 touched ladders have their next new vector at `δ ≤ 10`.  That is a statement about tails, not about balance or closeness, and it is what the nominees in §5 are built on.

---

## 5. The prior, and the nominees

**The prior, stated.**  A rank drop at `(λ, δ)` is a highest-weight vector of tail weight `λ̄` and ordinary degree `δ` vanishing on `D_ℓ`.  By Proposition S every such vector is, for `δ ≥ |λ̄|` (and in practice from the first `δ` at which `a = a_∞`), an equation of the affine variety `M_ℓ` of characteristic polynomials of traceless pencils, seen identically at every cell of its ladder; below that it is a "projective" vector confined to the non-stable segment.  The equations of `D_ℓ` whose types are known are of the first kind (LMR at tail weight 31 for `ℓ ≥ 9`; the bordered discriminants, which do not vanish; the types of the degree-661 cap equations are not on record), and the record proves that `I(M_6)` has no component of tail weight `≤ 12`.  So:

1. *Measure ladders, not cells*: one cell per ladder, the cheapest at which `a = a_∞`, decides the ladder for every degree; a second cell on the same ladder is redundant (Lemma L).  Fifty-nine of the record's 210 six-row cells were such repeats.
2. *Order ladders by tail weight*, lowest first, skipping the closed ones and the `a_∞ = 0` ones (which carry no vector at all — 346 of the 481 tails of weight `≤ 16`).  The first open tail weights are 13–16 at `ℓ = 6`, 13 at `ℓ = 7`, 15 at `ℓ = 8`, and above 16 at `ℓ = 9, 10` (the LMR tail is at 31).
3. *Within a tail weight, by cost*; the cheap cells are the skewed ones, and skewness is no longer a bias, since a stable cell of a skewed weight tests the same isotypic component of `I(M_ℓ)` as any other cell of its ladder.
4. *Prefer cells where the new room is one* (Lemma L): a single function to test, and a dead verdict closes the ladder if the cell is stable.
5. *Carry the pad side*: the nominated cells below all have `h_pad ≥ a` (no forced pad kernel), so a determinant kernel there is an obstruction candidate in the same measurement, unlike the balanced corner where the pad ideal is forced to hold almost everything.

**T1 — room-one cells** (ladders the record touches; the next cell adds exactly one highest-weight vector).  A dead verdict at a cell with `a = a_∞` closes the ladder.

| tail | a_∞ | top dead (δ, a) | cell | δ | a | stable? | h_pad | n_χ~ | reach |
|---|---|---|---|---|---|---|---|---|---|
| `(6,2,2,2,2)` | 9 | (9, 8) | `(26,6,2,2,2,2)` | 10 | 9 | yes | 28 | 5,485 | dense |
| `(12,3,1,1,1)` | 4 | (9, 3) | `(22,12,3,1,1,1)` | 10 | 4 | yes | 6 | 9,800 | dense |
| `(7,2,2,2,1)` | 7 | (8, 6) | `(22,7,2,2,2,1)` | 9 | 7 | yes | 29 | 9,928 | dense |
| `(13,3,1,1,1)` | 4 | (9, 2) | `(21,13,3,1,1,1)` | 10 | 3 | no | 6 | 11,489 | dense |
| `(11,2,2,1,1)` | 6 | (9, 5) | `(23,11,2,2,1,1)` | 10 | 6 | yes | 17 | 15,924 | dense |
| `(4,3,2,2,2)` | 2 | (7, 1) | `(19,4,3,2,2,2)` | 8 | 2 | yes | 10 | 16,593 | dense |
| `(9,5,1,1,1)` | 13 | (9, 12) | `(23,9,5,1,1,1)` | 10 | 13 | yes | 29 | 19,239 | dense |
| `(7,3,3,1,1)` | 6 | (8, 5) | `(21,7,3,3,1,1)` | 9 | 6 | yes | 25 | 28,465 | sparse |
| `(6,4,2,1,1)` | 5 | (7, 4) | `(18,6,4,2,1,1)` | 8 | 5 | yes | 30 | 28,466 | sparse |
| `(5,3,3,2,1)` | 2 | (7, 1) | `(18,5,3,3,2,1)` | 8 | 2 | yes | 13 | 68,255 | sparse |
| `(4,4,3,2,1)` | 2 | (7, 1) | `(18,4,4,3,2,1)` | 8 | 2 | yes | 14 | 78,267 | sparse |

**T2 — first stable cells of the open short ladders** (tail weight 13–16, `a_∞ ≥ 1`, not closed, not peaked), inside the dense frontier.  Each decides its tail's component of `I(M_ℓ)` for every degree.  The `ℓ = 7, 8` rows are the first cells at those lengths anyone would measure, and they are cheap.

| ℓ | tail | \|λ̄\| | a_∞ | cell | δ | a | sk | h_pad | n_χ~ | K_∞/\|Stab'\| |
|---|---|---|---|---|---|---|---|---|---|---|
| 7 | `(3,2,2,2,2,2)` | 13 | 1 | `(27,3,2,2,2,2,2)` | 10 | 1 | 50 | 4 | 3,026 | 362 |
| 6 | `(6,2,2,2,2)` | 14 | 9 | `(26,6,2,2,2,2)` | 10 | 9 | 410 | 28 | 5,485 | 625 |
| 7 | `(4,2,2,2,2,2)` | 14 | 3 | `(26,4,2,2,2,2,2)` | 10 | 3 | 179 | 9 | 6,695 | 761 |
| 6 | `(7,2,2,2,2)` | 15 | 12 | `(29,7,2,2,2,2)` | 11 | 12 | 640 | 42 | 8,871 | 934 |
| 7 | `(4,2,2,2,2,1)` | 13 | 1 | `(27,4,2,2,2,2,1)` | 10 | 1 | 179 | 6 | 9,545 | 1,137 |
| 6 | `(7,2,2,2,1)` | 14 | 7 | `(26,7,2,2,2,1)` | 10 | 7 | 533 | 30 | 10,228 | 1,156 |
| 8 | `(3,2,2,2,2,2,2)` | 15 | 1 | `(25,3,2,2,2,2,2,2)` | 10 | 1 | 63 | 4 | 11,205 | 1,199 |
| 7 | `(5,2,2,2,2,2)` | 15 | 4 | `(25,5,2,2,2,2,2)` | 10 | 4 | 385 | 16 | 13,129 | 1,403 |
| 6 | `(8,2,2,2,2)` | 16 | 21 | `(32,8,2,2,2,2)` | 12 | 21 | 1046 | 60 | 13,618 | 1,357 |
| 6 | `(8,2,2,2,1)` | 15 | 11 | `(25,8,2,2,2,1)` | 10 | 11 | 812 | 42 | 15,148 | 1,609 |
| 6 | `(4,3,2,2,2)` | 13 | 2 | `(27,4,3,2,2,2)` | 10 | 2 | 270 | 10 | 17,344 | 2,080 |
| 7 | `(5,2,2,2,2,1)` | 14 | 2 | `(26,5,2,2,2,2,1)` | 10 | 2 | 427 | 11 | 18,328 | 2,071 |
| 6 | `(4,4,2,2,2)` | 14 | 6 | `(26,4,4,2,2,2)` | 10 | 6 | 539 | 16 | 18,859 | 2,159 |

The full T2 list (101 open short ladders, of which 88 are beyond the dense frontier) is in `results/s57_selector.md` §5; the sparse-route band (`n_χ~ ≤ 120,000`) adds a further 53 cells.

**T3 — the LMR ladder.**  `a` is within five of its stable value from `δ = 21`; the cells `(4δ − 31, 17, 2^7)` for `δ = 21..24` have `n_χ~` from 30,977,102 to 31,039,465 (`N_S ≈ 1.56·10^{11}`), and the same isotypic computation on the slice `Z` has `K_∞/|Stab'| ≈ 1.43·10^6`.  Nothing the programme has reaches either number; the slice formulation is the cheaper by a factor twenty and is the one an engine for this ladder should be built on.  What the ladder would settle: at `δ = 23`, whether a degree-23 equation exists at `ℓ = 9` (the sharpest form of s55's "nothing below 24"); at `δ = 24`, `i_det` and `i_pad` at the one cell where a determinant kernel is known, hence whether the known separation is also a multiplicity obstruction — the question s50 §2 left open.

**T4 — the balanced corner** (`ℓ = 6`, `δ = 8..12`, the K1 first nominees): `(8,6,6,4,4,4)_8` (`a = 4`, `h_pad = 1`, `n_χ~ ≈ 9.9·10^6`), `(8,8,4,4,4,4)_8` (`a = 5`, `h_pad = 1`, `1.7·10^6`), `(10,6,6,6,6,6)_{10}` (`a = 5`, `h_pad = 1`, `≥ 1.3·10^6`), and at `δ = 9, 11, 12` cells with `h_pad = 0` that Lemma A excludes from the obstruction ranking.  Unchanged in cost since s41, no positive evidence, and the pad ideal is forced to hold nearly all of `a` there; nominated for the onset question only, and last.

**What would move the prior.**  A kernel at any T1 or T2 cell is the six-row (or seven-row) onset and its tail weight is the weighted onset `m_0(ℓ)`; that would say the first equations of `M_ℓ` are of low tail weight and skewed — the LMR pattern.  All of T1 and T2 dead would prove `m_0(6) ≥ 17` and push the search to tail weights 17–20 (still cheap at the stable end) while making the balanced, low-degree regime the only place a six-row equation of degree `≤ 12` could hide; that regime is priced above `10^6` and has been for six sessions.

---

## 6. Pre-registration scorecard

| # | prediction (prior) | outcome |
|---|---|---|
| P1 | s39 `a` reproduces by the Weyl route at all 1,874 cells of `(10, 6)` and a sample elsewhere (0.95) | **confirmed**: 1,874 of 1,874, and 26 of 26 in a sample across `(10, 7..10)` and `(11, 6..8)` restricted to tail boxes `≤ 2·10^6` (the sample run was ended by its recorded id when the eight- and nine-row cells of `δ = 11, 12` took over seven minutes each); `sk` reproduced by the house Python route at three cells (V2) |
| P2 | K2 refuted as a closeness prior: ≥ 90% of the dead six-row cells in K2's first quartile (0.85) | **substance confirmed, threshold missed**: 65% in the first quartile, 34% in the first decile, and K2's first nominee is dead in every measured slice; the 90% was too strong because many measured cells — s36's balanced `ℓ = 5` stratum, the `(λ_1,λ_2,λ_3,1,1,1)` family — have mid-slice `sk/a` |
| P3 | the LMR cell in the last K1 decile of its slice (0.85) | **confirmed**, percentile 0.9954 |
| P4 | dead cells mostly in the skewed half of K1 (median > 0.5); K1's first nominee at `(7, 6)` dead (0.8) | **confirmed on the median** (0.84); the `(7, 6)` nominee is a three-way tie at balance 4 of which one member, `(8,4,4,4,4,4)`, is dead and two are unmeasured |
| P5 | ≥ 40% of the 210 six-row dead cells implied by a lower dead cell with equal `a` (0.6) | **refuted**: 59 of 210 (28%); 34 of the 116 length-5 cells |
| P6 | ≥ 40 cells of `δ = 10–12` dead by transport, including every peaked `ℓ = 6` cell (0.8) | **confirmed**: 34 at each of `δ = 10, 11, 12` at `ℓ = 6` (114 region cells in all with the family cells), every `ℓ = 6` peaked cell among them |
| P7 | LMR ladder `a` non-decreasing, `a(24) = 274` (0.95) | **confirmed**, both |
| P8 | `a(23) < 274` (0.5), the alternative forcing a degree-23 equation | **the stated default holds**: `a(23) = 273`; no equation below 24 follows; the increment at the last step is exactly one |
| P9 | `h_pad(LMR cell) < 274` (0.7) | **refuted by transport**: `h_pad(16) = 331` and `h_pad` is non-decreasing up the ladder, so `h_pad(24) ≥ 331 > 274`; no pad-forced kernel at the LMR cell |
| P10 | `sk/a ≥ 10` on every F1 cell with `sk` (0.9) | **confirmed**: 1,357, 394, 287, 244, 221 at `δ = 12..16` |
| P11 | peaked ladders `a = 1`, `sk` constant `8, 13, 18, 21, 21, 18`; `ℓ = 6` dead by transport, `ℓ ≥ 7` unconstrained (0.9) | **confirmed and superseded**: the values hold at every tabulated `δ`, and Theorem P makes all of them dead at every `ℓ ≤ 16` without measurement |
| P12 | `ℓ = 6`, `δ = 11, 12`: fewer than 40 dense cells not dead by transport, all with `a ≤ 3` (0.6) | **half right**: 15 at `δ = 11` and 14 at `δ = 12`, but their `a` runs up to 24 (`(28,8,2^4)_{11}`, room 9) — the cheap cells are not all rigid |
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
  where to measure, with reasons; `D` is not reported anywhere.  No
  certificate was produced, so `tools/verify/` had nothing to check; its
  self-test was run on this tree and passes (`results/logs/s57_verify_selftest.log`).
- **The criteria scores are against a record selected by cost**, and the
  report says in §3 why that makes "dead cells rank low" a weak test.
- **Verification** (`analysis/wk9_s57_verify.py`, `results/s57_cells/verify.json`):
  V1 as in P1; V2 `sk` by the house route at three cells, all agree; V3 `a`
  non-decreasing up ladders at 43,090 consecutive pairs on 37,276 ladders and
  `h_pad` at 31,551 pairs, no violation (Lemma L on the data); V4 `a ≤ a_∞` at
  750 cells with a stable value and `a = a_∞` at all 64 of them with
  `δ ≥ |λ̄|`, no violation (Proposition S on the data); V5 the 48 family cells
  with both `a` routes agree; V6 the census counts equal the s39 candidate
  counts at `δ = 10–12`.

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
