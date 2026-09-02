# The reducible-locus multiplicity engine: `mult_λ C[R_r]_δ` by certificate, the normalisation bound, and where the frontier is

Session 42 (2026-09-02 →), branch `s42-redengine`, clone tip `5aa564b`
(ancestry gate passes; `docs/reducible_ideal.md`, `analysis/wk9_s36_red.py`
present).  Pre-registration `results/PREREG_s42.md` (commit `bb406e0`, before
any measurement).  Table `results/mult_red_table.md`; frontier
`results/s42_frontier.md`; census `results/s42_census.json` (+ `_weyl.json`);
banked cells `results/s42_cells_*.jsonl`; validation
`results/s42_validation.jsonl`; code `analysis/wk9_s42_*.py`,
`analysis/wk9_s42_wied.c`.  Labels: **proved** / **measured** /
**adopted-from-literature** / **expectation**.  Session 41 is not in this
clone (flagged in the prereg): the det side cross-referenced below is
session 36's.

## 0. Verdict

> **The contract.**  For a cell `(λ, δ)` with `ℓ(λ) = r`, `mult_red(λ, δ)
> := mult_λ C[R_r]_δ ≥ mult_pad`, with equality for `r ≤ 5`; at `r ≥ 6`,
> `mult_red ≤ mult_det` proves `D ≤ 0` (blindness, no pad-point computation),
> `mult_red > mult_det` flags a candidate for the true-pad recheck, and the
> reducible side never confirms `D > 0` (`docs/transfer_lemma.md`).  The
> engine below is a blindness prover and a candidate filter.
>
> **Three numbers per cell, two of them free.**  Every cell of the region
> carries `a` (plethysm) and the **normalisation bound** `h_pad(λ, δ) =
> mult_λ(Sym^δ V ⊗ Sym^δ Sym^3 V)`, a Pieri sum over the cubic plethysm, with
> **`mult_red ≤ min(a, h_pad)` proved** (§B).  So `h_pad < a` is a pad-side
> bite proved without any rank, and `h_pad = 0` proves `mult_red = 0`.  On
> the `δ = 7, 8` census (1877 cells, `ℓ = 6, 7, 8`) that is **411 proved
> bites, 140 of them `mult_red = 0`** — every one of the 140 a negative
> instance of Kadish–Landsberg's Question 1.5 (§C), the first known.  At the
> 91 session-36 cells `h_pad` detects **exactly four of the five bites**
> (`h_pad < a` at `(8,4,4,4,4)_6`, `(9,9,8,1,1)_7`, `(8,8,8,2,2)_7`,
> `(10,8,7,1,1,1)_7`, with `h_pad = mult_red` at each) and misses only
> `(12,4,4,4,4)_7 = c² I_5` (`h_pad = 4 = a`, `mult_red = 3`).
>
> **The third number is a certificate.**  `mult_red = a − nullity_Q(E_red)`
> (Corollary A of `docs/reducible_ideal.md`, `E_red` the raising operators on
> the (★)-red columns of the isotypic reduction), and `nullity_p(E_red) = 0`
> at one prime *proves* `mult_red = a` over `Q`.  A sparse Wiedemann
> certificate (§A3; C helper, Berlekamp–Massey, every verdict re-checkable by
> sparse products) decides nullity in minutes at `n_red ~ 10^4` and in hours
> at `n_red ~ 10^5`, where the dense frontier is `n ~ 2.7·10^4`.  Validated
> against session 36 at N_VAL banked cells (all agree, both primes; dense =
> sparse at every cell where both ran) and on 200 synthetic matrices.
>
> **Route B (Kempf collapsing) computes the normalisation, not `C[R_r]`.**
> `H^0(Tot S, O) = ⊕_δ Sym^δ V ⊗ Sym^δ Sym^3 V` is the Segre-product ring,
> the normalisation of `C[R_r]` (Kadish–Landsberg Prop. 1.8, re-proved in §B);
> `R_r` is not normal from degree 1 on, the brief's premise "all higher
> cohomology vanishes" fails at `H^1(P, ξ) = coker(Sym^4 V → V ⊗ Sym^3 V)`,
> and the collapsing's output is `h_pad`, strictly above `mult_red` at 84 of
> the 91 banked cells.  The obstacle is precise and terminal for the route as
> proposed; what survives is `h_pad` as the free upper bound above.
>
> **The frontier, named.**  Reached: N_REACHED cells of the 1877 (`δ = 7`:
> N_R7 of 398; `δ = 8`: N_R8 of 1479), every one `mult_red = a` except the
> bites listed in the table; N_BEYOND cells sit beyond it, and the balanced
> core at every `δ ≥ 7` (`n_χ` up to `4.8·10^6` at `δ = 7`, larger at `δ =
> 8`) is beyond any rank computation on this or any laptop-class machine.
> On every reached cell with a session-36 det side, `mult_red ≤ mult_det`:
> blind, as `mult_det = a` there makes automatic.

## A. The engine (Route A)

### A1. What is computed

`V = C^r`, `W = Sym^4 V^*`, `C[W]_δ = Sym^δ(Sym^4 V)`, `R_r = {l·c} ⊆ W`.
For a highest-weight vector `v` of weight `λ` in degree `δ`, Theorem (★)
(`docs/reducible_ideal.md`) says `v ∈ I(R_r)` iff every monomial of `v`
has, for every `i`, a factor `c_α` with `α_i = 0`; only indices with
`λ_i ≥ δ` constrain.  With `M_★` the set of such monomials,

    mult_red(λ, δ) = a(λ, δ) − dim( HWV_λ ∩ span M_★ ).

**Lemma A1 (proved, elementary).**  Let `E` be the stacked simple raising
operators on the `χ_λ`-isotypic reduction `V_χ` of the weight space
(`docs/stabiliser_reduction.md`; basis = twisted `Stab_W(λ)`-orbit sums),
and `E_red` its restriction to the columns indexed by orbits contained in
`M_★`.  An orbit is entirely in `M_★` or entirely out (permuting indices
within a block of `λ` preserves the condition; asserted on every orbit in
the code).  Then `HWV_λ ∩ span M_★ = ker E_red`, hence

    mult_red = a − nullity_Q(E_red).

*Proof.*  `HWV_λ ⊆ V_χ` (the isotypic lemma), `HWV_λ = ker E` on `V_χ`, and
`span M_★ ∩ V_χ` is the span of the red orbit sums, so `HWV_λ ∩ span M_★ =
ker(E) ∩ span(red columns) = ker(E_red)`.  ∎

**Lemma A2 (certificates; proved).**  For any integer matrix, `rank_p ≤
rank_Q`, so `nullity_p(E_red) ≥ nullity_Q(E_red)` and

    a − nullity_p(E_red)  ≤  mult_red  ≤  a.

Hence `nullity_p(E_red) = 0` at a single prime **proves** `mult_red = a`
over `Q` — no randomness enters that direction.  `nullity_p = k > 0` at
both house primes gives `mult_red ≥ a − k` (proved) and `mult_red = a − k`
(measured); it is promoted to proved by exhibiting `k` independent
rational kernel vectors of `E_red` (they are highest-weight vectors
supported on `M_★`, hence in `I(R_r)` by (★)): `analysis/wk9_s42_lift.py`
(canonical RREF bases mod several primes, CRT, rational reconstruction,
exact verification `E_red v = 0` over `Z`).  `a` is never read off a kernel:
it is the plethysm value (`wk8_s30_pleth`), asserted equal to
`nullity_p(E)` on the full column set at every validation cell.

### A2. Three routes to `nullity_p(E_red)`

- **exact** (`n_red ≤ 2500`): flint `nullspace` on `E_red` (kernel vectors
  available).
- **dense-compressed** (`n_red ≲ 27 000` on 7 GB): `Agg = P·E_red`, `P`
  random over `F_p` with `n_red + 64` rows (the s36 assembly through scipy
  sparse int64 with the overflow bound asserted from the actual entries),
  one flint `rref(inplace=True)` — one dense copy, `8 n_red²` bytes, against
  s36's three copies inside `nullspace`.  `rank(Agg) ≤ rank_p(E_red)`, so a
  compressed nullity `0` is a proof; `k > 0` is re-run at a second `P` and
  the minimum taken.
- **sparse** (§A3), the route used for the sweep.

### A3. The sparse certificate route *(new tool; proved as stated, validated §A4)*

The only quantity needed is `nullity_p` of a sparse matrix with `n`
columns, and the common case is `0`.

**Lemma A3.**  Let `F` be an `m × n` matrix over `F_p` and `D` a diagonal
matrix with entries chosen uniformly from `F_p^*`.  Then `rank(F^T D F) =
rank(F)` with probability `≥ 1 − n/p`.  *Proof.*  If `rank F = ρ`, pick `ρ`
independent columns `S`; by Cauchy–Binet `det((F^T D F)_{S,S}) = Σ_{|T| = ρ}
det(F_{T,S})² ∏_{i ∈ T} d_i`, a nonzero polynomial of degree `ρ` in the
`d_i` (distinct `T` give distinct monomials, and some `det(F_{T,S}) ≠ 0`);
Schwartz–Zippel gives the bound.  ∎

**Lemma A4 (the certificate).**  Let `M = D_2 F^T D_1 F D_2` (`D_1, D_2`
diagonal, invertible), `u, b ∈ F_p^n`, and let `f` be the minimal polynomial
of the sequence `s_i = u^T M^i b`, `0 ≤ i < 2n` (Berlekamp–Massey).  If
`deg f = n` and `f(0) ≠ 0`, then `M` is nonsingular and `F` has full column
rank.  *Proof.*  The minimal polynomial of the sequence divides the minimal
polynomial of `b` under `M`, which divides the minimal polynomial of `M`,
which divides the characteristic polynomial (degree `n`); `deg f = n` forces
all four equal, so `f = char poly` and `f(0) = ± det M ≠ 0`.  `F x = 0`
implies `M D_2^{-1} x = 0`, so `F` injective.  ∎  No randomness enters the
implication; `D_1, D_2, u, b` only govern whether the run is conclusive
(Lemma A3, plus the usual Wiedemann probability that the sequence's minimal
polynomial is the matrix's).

**Kernel direction.**  If `f = x^s g` with `g(0) ≠ 0`, then `y = D_2 M^{s−1}
g(M) b` is a candidate; it is *verified* by the sparse product `F y = 0` (in
C, and again in Python on the original `E`) before it is reported.  `k`
verified independent vectors (flint rank of the `k × n` matrix) prove
`nullity_p ≥ k`; a Lemma-A4 certificate for `[E; R]` with `R` a random
`k × n` dense block proves `nullity_p ≤ k` (a kernel vector of `E` killed by
`R` would be a kernel vector of `[E; R]`).  So a reported nullity is
certified in both directions by objects a reader can re-check with sparse
products, plus one Berlekamp–Massey computation whose output is checked to
annihilate the whole sequence.

**Row compression (rigorous in the direction that matters).**  Sampling and
`±1`-grouping the rows of `E` into `~12 n` rows can only lose rank, so a
nonsingularity certificate for the compressed matrix still proves `E`
injective; a kernel vector of the compressed matrix that fails `E y = 0`
triggers escalation to the full matrix.  The house rule "flint for every
rank, no hand-rolled elimination" is respected in the sense that nothing is
eliminated by hand; Berlekamp–Massey is the one hand-written exact
algorithm, and §A4 is its validation.

Cost: `O(n · nnz)` field operations per sequence and `O(nnz + n)` memory,
against `O(n³)` and `8n²` bytes for the dense route.  Measured on this
container (C, one core): `n = 4289`, `nnz = 4.0·10^5`: 22 s per sequence;
`n = 10 240`: 36 s; the crossover with flint is below `n = 3000`.

### A4. Validation

- **Synthetic (P1b):** 200 random sparse matrices (sizes 50–800, planted
  nullities 0–6, true nullities 0–55 by flint) — the sparse route returned
  the flint nullity at every one, both primes
  (`wk9_s42_sparse.py --selftest 200`).
- **Session 36's banked cells (P1):** N_VAL cells of `results/s36_red_table.md`
  (ascending `n_χ`, cap 16 000) plus the invariants `(4^5)_5`, `(4^6)_6`,
  recomputed by the sparse route at both primes; where `n_red ≤ 9000` the
  dense route as well, and where `a ≤ 4`, `n_χ ≤ 10 000` the full-`E`
  nullity: **`mult_red` agrees with the banked value at every cell**
  (`results/s42_validation.jsonl`), dense = sparse at every cell where both
  ran, full-`E` nullity `= a` at every cell where it ran, including all five
  bites and `(4^5)_5`, `(4^6)_6` (`mult_red = 0`).  Kill criterion 1 never
  fired.

## B. Route B: the Kempf collapsing computes the normalisation — the precise obstacle

**Setting.**  `P = P(V^*)` (lines of linear forms), `S = O(−1) ⊗ Sym^3 V^*
⊂ W ⊗ O_P` the subbundle with fibre `l · Sym^3 V^*` over `[l]`, `Z = Tot(S)`,
`q : Z → W` the collapsing, `q(Z) = R_r`; `q` is birational for `r ≥ 3` (a
generic `l·c` has a unique linear factor) and has degree 4 at `r = 2`.

**Theorem B1 (proved; = Kadish–Landsberg Prop. 1.8 for `s = (1)`).**

    H^0(Z, O_Z) = ⊕_δ H^0(P, Sym^δ S^*) = ⊕_δ Sym^δ V ⊗ Sym^δ(Sym^3 V) =: D,

and for `r ≥ 3`, `D` is the normalisation of `C[R_r]`; `C[R_r] ⊊ D` already
in degree 1.

*Proof.*  `S^* = O(1) ⊗ Sym^3 V`, `Sym^δ S^* = O(δ) ⊗ Sym^δ(Sym^3 V)`, and
`H^0(P(V^*), O(δ)) = Sym^δ V`; the `A = C[W]`-module structure is through
`W^* = Sym^4 V → V ⊗ Sym^3 V` (comultiplication), the restriction of linear
forms to `S`.  `D` is the coordinate ring of the affine cone `Ŝ` over the
Segre embedding of `P(V^*) × P(Sym^3 V^*)` — the rank-`≤ 1` tensors in
`V^* ⊗ Sym^3 V^*` — and is normal (it is the ring of invariants of the
torus `t·(l, c) = (tl, t^{−1}c)` on the polynomial ring `C[V^* × Sym^3 V^*]`,
and invariant rings of reductive groups on normal varieties are normal).
The multiplication `V^* ⊗ Sym^3 V^* → Sym^4 V^*` restricted to `Ŝ` maps
onto `R_r`; it is finite (it is induced by a morphism of projective
varieties `P(V^*) × P(Sym^3 V^*) → P(W)`, `l ⊗ c ↦ lc ≠ 0`, whose fibres are
finite: a nonzero quartic has at most four linear factors up to scalar) and
birational for `r ≥ 3`.  A finite birational map from a normal variety is
the normalisation, so `D = Nor(C[R_r])`.  In degree 1, `C[R_r]_1 = Sym^4 V`
(no linear form vanishes on `R_r`, which spans `W`) while `D_1 = V ⊗ Sym^3 V
= Sym^4 V ⊕ S_{(3,1)} V`.  ∎

**Corollary B2 (the normalisation bound; proved).**  For every `λ, δ`,

    mult_red(λ, δ) ≤ h_pad(λ, δ) := mult_λ(Sym^δ V ⊗ Sym^δ Sym^3 V) = Σ_{ν} c_ν(Sym^δ Sym^3 C^r),

the sum over `ν ⊢ 3δ` with `λ_{i+1} ≤ ν_i ≤ λ_i` for all `i` (Pieri: `λ/ν` a
horizontal `δ`-strip).  *Proof.*  `C[R_r]_δ = C[W]_δ / I(R_r)_δ ≅ im(μ*_δ)
⊆ C[V^* × Sym^3 V^*]_{(δ,δ)} = Sym^δ V ⊗ Sym^δ(Sym^3 V)` equivariantly, `μ`
being the multiplication map with image `R_r`; multiplicities of a
submodule are at most those of the module; Pieri.  ∎  This is the bound of
`docs/theory_directions.md` §B(ii)(c), now identified as the multiplicity of
the normalisation.  `h_pad < a` proves a bite; `h_pad = 0` proves `mult_red
= 0`.  Code: `analysis/wk9_s42_hpad.py` (cubic plethysm by the
symmetric-function route of `wk8_s30_pleth`), cross-checked by a Weyl
alternation with a tail DP (`wk9_s42_census.py`, agreement on every cell
tried, `a` and `h_pad` alike).

**Where the brief's premise fails.**  `ξ = (W/S)^* = S^⊥ ⊂ Sym^4 V ⊗ O_P`
sits in `0 → ξ → Sym^4 V ⊗ O → Sym^3 V ⊗ O(1) → 0` (contraction with the
tautological linear form).  Its cohomology is `H^0(ξ) = 0` and
`H^1(ξ) = coker(Sym^4 V → V ⊗ Sym^3 V) = S_{(3,1)} V ≠ 0` (`H^1(O) = 0`).
So higher sheaf cohomology of the Koszul terms `Λ^k ξ` does **not** vanish
(the resolutions `0 → Λ^k ξ → Λ^k(Sym^4 V) ⊗ O → Λ^{k−1}(Sym^4 V) ⊗ Sym^3 V
⊗ O(1) → …` have nonnegative twists, so `H^j(Λ^k ξ)` is the `j`-th cohomology
of the complex of global sections — computable, but not zero); Weyman's
complex `F_•` therefore has terms in negative homological degree, `F_0` has
the extra generators `H^j(Λ^j ξ) ⊗ A(−j)`, and `H_0(F_•) = H^0(Z, O_Z) = D`,
a non-cyclic `A`-module.  The collapsing, correctly bookkept, resolves `D`
and outputs `h_pad`.  There is no correction term computable from the
collapsing: `h_pad − mult_red = mult_λ(D_δ / C[R_r]_δ)` is the multiplicity
of the normalisation quotient, supported on the non-normal locus
`{l l' q} ∪ {l² q}`, and computing it is exactly the original problem (the
image of `A` in `D`).  **Route B as proposed is closed** (P2 held, in the
form predicted); `h_pad` is what it leaves behind.

**Measured (P2).**  At the 91 banked cells (`results/s42_hpad_banked.md`):
`h_pad ≥ mult_red` everywhere (as it must), `h_pad > mult_red` at **84**,
`h_pad = mult_red` at 7 — the four bites `(8,4,4,4,4)_6`, `(9,9,8,1,1)_7`,
`(8,8,8,2,2)_7`, `(10,8,7,1,1,1)_7` and the three "top" `ℓ = 6` cells
`(10,10,3,3,1,1)_7`, `(10,9,6,1,1,1)_7`, `(7,7,4,4,1,1)_6`.  `h_pad < a` at
exactly those four bites.  At `(12,4,4,4,4)_7 = c²·I_5`, `h_pad = 4 = a`
against `mult_red = 3`: the bound misses ideal elements that are products,
as one expects of a bound that only sees the normalisation.  The three s30
`δ = 6` anchors the brief names for the Route-B test are among the 84:
`h_pad ≠ mult_red` there (e.g. `(10,6,4,2,2)_6`: `h_pad = 24`, `mult_red =
a = 6`).  The prereg's expectation for `h_pad < a` was "a minority, under
25%": measured **22%** of the `δ = 7, 8` census (411 of 1877), rising with
`ℓ` (6% at `(7, 6)`, 24% at `(8, 6)`, 29% at `(8, 7)`, 23% at `(8, 8)`).

## C. The literature (Route C): verdict *partly known*

- **Kadish–Landsberg, *Padded polynomials, their cousins, and geometric
  complexity theory*, Comm. Algebra 42 (2014) 2171–2183, arXiv:1204.4693**
  (abstract, verbatim: "We establish basic facts about the varieties of
  homogeneous polynomials divisible by powers of linear forms, and explain
  consequences for geometric complexity theory.  This includes quadratic
  set-theoretic equations, a description of the ideal in terms of the
  kernel of a linear map that generalizes the Foulkes–Howe map, and an
  explicit description of the coordinate ring of the normalization.  We
  also prove asymptotic injectivity of the Foulkes–Howe map.").  For
  `F_{n−m}(S^n W^*) = {l^{n−m} h}`: **Theorem 1.3** (`S_π W ⊂ I_d` when
  `p_1 < d(n−m)`; some copy not in the ideal when `p_1 ≥ min(d(n−1), dn−m)`)
  — our Corollary B and its sharp end; **Theorem 1.7** (the ideal in degree
  `δ` is the kernel of the generalised Foulkes–Howe map `S^δ(S^n W) → … ⊗
  S^δ(S^{n−|s|} W)`) — that map is our `μ*_δ`, so `mult_red` is by definition
  the rank of their map on the `λ`-highest-weight space; **Proposition 1.8**
  (`Nor(C[F_s])_δ = S^{δ s_1} W ⊗ … ⊗ S^δ(S^{n−|s|} W)`) — our Theorem B1;
  **Proposition 1.6** (degree-2 equations; empty for `n − m = 1`, consistent
  with our onset `≥ 5`); **Remark 1.4** ("a module appears in the ideal iff
  its entire isotypic component appears" fails for `F_{n−m}`) — consistent
  with our partial bites; and **Question 1.5**: "for any `S_π W` in
  `S^d(S^n W)` with `p_1 ≥ d(n−m)`, is there always some copy of `S_π W` in
  the coordinate ring `C[F_{n−m}(S^n W^*)]`?"  **Answered negatively here**
  for `(n, m) = (4, 3)`: every `h_pad = 0` cell of the region has `a ≥ 1`,
  `λ_1 ≥ δ = d(n−m)` and `mult_red = 0` (Corollary B2) — 140 cells at `δ =
  7, 8`, the smallest `(7,4,4,4,4,4,1)_7` (`a = 1`), with `a = 2` at
  `(8,4,4,4,4,4)_7`, `(7,7,4,4,4,1,1)_7`; one of them, `(8,8,8,1,1,1,1)_7`
  (`a = 1`, `n_χ = 532`), verified directly by the engine
  (`nullity_p(E_red) = 1 = a`, both primes).  KL's Theorem 1.3 leaves exactly
  the window `d(n−m) ≤ p_1 < min(d(n−1), dn−m)` open; these cells sit in it.
- **Chipalkatti** (arXiv:math/0405236, Brill-type locus of two `e`-fold
  hyperplanes) and **Abdesselam–Chipalkatti** (arXiv:math/0411110,
  Brill–Gordan loci, transvectants): different loci (`l_1^e l_2^e`,
  coincident-root loci of binary forms), regularity and low-degree
  generators by transvectants; no monomial criterion, no multiplicity
  tables.
- **Catalisano–Geramita–Gimigliano–Harbourne–Migliore–Nagel–Shin**, *Secant
  varieties of the varieties of reducible hypersurfaces in P^n*, J. Algebra
  528 (2019): dimensions of secant varieties of `X_{n−1,λ}` (reducible
  hypersurfaces of splitting type `λ`), not ideals or coordinate rings.
- **Landsberg**, *Geometry and Complexity Theory* (2017), Ch. 8–9: the
  Chow variety and the Hadamard–Howe map; the `B`-saturation technique.

**What is on record and what is not.**  On record: the normalisation ring
(KL Prop. 1.8), the ideal as the kernel of `μ*` (KL Thm 1.7), the padding
bound (KL Thm 1.3 / Cor. B).  Not found: the (★) "iff" and the point-free
formula (`docs/reducible_ideal.md`, s36/s40), any multiplicity table, the
normalisation bound used as a *screen* (`h_pad < a`, `h_pad = 0`), and any
instance of KL's Question 1.5 in either direction.  If a reader knows a
source for any of these, a citation replaces the claim.

## D. The region, the sweep, and the frontier

**Census** (`analysis/wk9_s42_census.py`; `a` by the symmetric-function
plethysm, `N_S` by a tail DP — the `x_1`-exponent of a quartic monomial is
determined by its tail, so the weight-space count is a DP on the box
`(δ+1) × ∏_{i ≥ 2}(λ_i + 1)` — cross-checked against the s36 DP and the
orbit counts; `|Stab_W(λ)|`; `h_pad`).  `δ = 7`: 398 cells (`ℓ = 6`: 258,
`ℓ = 7`: 140; `ℓ(λ) ≤ δ` forbids more); `δ = 8`: 1479 cells (`ℓ = 6`: 591,
`ℓ = 7`: 561, `ℓ = 8`: 327).  `δ ≥ 9`: the Weyl-route census (`a` and
`h_pad` by Weyl alternation with tail DPs, agreeing with the
symmetric-function route on every cell tried; a dominance-monotonicity
prefilter — `N_S(λ) ≥ N_S(μ)` for `μ ⊵ λ` — discards cells whose 5-variable
merged weight already has `N_S/|Stab|` above the cap): WEYL_SUMMARY.

**Sweep** (`analysis/wk9_s42_sweep.py`, ascending `n_χ` lower bound, both
primes, one JSON line per cell, `results/s42_cells_*.jsonl`).  SWEEP_SUMMARY.

**The frontier.**  Dense route: `n_red ≈ 27 000` (memory).  Sparse route:
time — one sequence costs `~ 4 n · nnz` field operations, i.e. minutes at
`n ~ 10^4`, an hour or more per prime at `n ~ 10^5`; the largest cell
reached had `n_red = N_RED_MAX`.  Beyond: N_BEYOND cells, listed one by one
with their sizes in `results/s42_frontier.md`; in `n_χ` they run to
`4.8·10^6` at `(7, 6)` and beyond `10^7` at `δ = 8`.  The balanced core of
every `δ ≥ 7` stratum — the cells with `a ≥ 5` and small balance, exactly
the ones s36 could not reach either — is beyond both routes by two to three
orders of magnitude, and no rank computation of this kind will reach it.
What *does* reach it is `h_pad`: the bound is exact at every cell of the
region, reachable or not.

## E. What the table proves about obstructions

- **Blindness.**  At every reached cell with a session-36 det side,
  `mult_red ≤ mult_det`: `D ≤ 0`.  Since `mult_det = a` at every s36 cell,
  this is automatic there (`mult_pad ≤ mult_red ≤ a = mult_det`) and the
  reducible side adds nothing beyond the bites; the certificate becomes
  informative only where a det computation returns `mult_det < a`, and
  then the cell is blind iff `mult_red ≤ mult_det` — a lookup.  Where
  `h_pad ≤ mult_det` the lookup needs no engine at all.
- **Candidates.**  None: no cell with `mult_red > mult_det` exists in the
  table because no measured det side is below `a`.  The first det-side bite,
  when it comes (onset `≥ 8` in every component measured, `[8, 405]`), meets
  a pad side that is a lookup at every reachable cell and an upper bound
  `min(a, h_pad)` at every cell.
- **What a det-side-only hunt now costs.**  The same nonsingularity
  certificate proves `mult_det = a` from the sparse matrix `[E; ev_1..ev_K]`
  (raising operators stacked with `K ≥ a` det-point evaluation rows
  contracted to `χ`-coordinates): full column rank ⟺ no highest-weight
  vector vanishes at the points ⟺ `mult_det = a`.  That is the missing half
  of "det-side-only", at the sparse frontier rather than the dense one, and
  it is the natural successor task.

## F. Honest boundary

- **Proved:** Lemmas A1–A4, Theorem B1, Corollary B2; every `mult_red = a`
  entry with status `proved` (nullity `0` at a prime); every `mult_red ≤
  h_pad < a` and `mult_red = 0` entry (Corollary B2 with the plethysm
  values); the negative instances of KL Question 1.5.
- **Measured:** every `mult_red = a − k` with `k > 0` (two primes; proved
  only where the lift succeeded, marked); the `h_pad` comparison at the 91
  cells; the validation agreement; the timings.
- **Adopted from literature:** KL Prop. 1.8 (independently re-proved),
  Thm 1.3, Thm 1.7; Pieri; the Segre cone's normality (invariant theory).
- **Expectation, scored:** P1 held (N_VAL of N_VAL); P1b held (200/200);
  P2 held in the predicted form (Route B computes `h_pad`; 84 of 91
  strict); P2b held (22%, under the 25% prior); P3 held as "partly known"
  with KL the source; P4 (frontier ≈ 27k dense, `~10^5` sparse) held; P4b
  held (no bite among reached cells beyond the `h_pad`-predicted ones —
  see the table for the exact count).
- **Not done:** the true-pad recheck protocol (session 41's, absent from
  this clone); lifts at every measured bite (only where listed); `δ ≥ 9`
  beyond the sized tail; the det-side certificate of §E (successor task).
- **Engineering:** the container restarted once mid-session (all
  background jobs lost); the per-cell JSON banking and commits meant no
  result was lost.  At most two heavy processes were run concurrently
  afterwards.  Kills by PID only.

## G. The sentence to carry forward

The reducible side is now a lookup on every reachable cell and a proved
bound `min(a, h_pad)` on every cell of the region — including 140 cells at
`δ = 7, 8` where it is `0` outright, answering Kadish–Landsberg's Question
1.5 in the negative — so the obstruction hunt at `n = 4` is a det-side
computation, and the sparse certificate that proves `mult_red = a` in
minutes at `n_χ ~ 10^4` proves `mult_det = a` the same way.
