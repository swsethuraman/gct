# B13-04 — sharpen the cubic-to-quartic transfer

board_numbering: batch13
session: B13-04 (the board's "sharpen the cubic-to-quartic transfer")
model: Claude Fable 5.1 — configured id `claude-fable-5-1`; the serving model is
not observable from inside the session and is recorded as configured
base: `0049511` (`git rev-parse main` at clone); branch `b13_04`
delivery: `b13_04_fable.bundle`, **one part** (`part00` is the whole file), with
`b13_04_fable.bundle.md5` carrying a whole-file digest and the `part00` digest
pre-registration: `results/PREREG_b13_04.md` (commit `35148d8`, before any
computation); everything not listed there is marked exploratory below
date: 2026-09-09

## 0. What this session delivers, in one paragraph

Proposition 8 of `docs/transfer_lemma.md` says a permanent-specific equation at
a quartic weight `λ` needs a cubic-ideal constituent `S_ν ⊆ I(D_r^{per₃})_δ`
with `λ/ν` a horizontal `δ`-strip.  This report states the **exact** form of
that statement (§3, PROVED): `mult_R(λ,δ) − mult_P(λ,δ)` is the dimension of the
intersection of the reducible image `ρ(H_λ)` with the cubic ideal, where
`ρ(h)(c) = h(x₁·c)` is the fixed-factor restriction — the intersection of the
multiplication pullback's image with the cubic ideal, read in one weight space
of the cubic coordinate ring.  The image sits inside the direct sum of the Pieri
predecessor channels, of dimension `Σ_ν a⁽³⁾(ν,δ)`, and the gap is pinned
between `max(0, Σ_ν i⁽³⁾ + mult_R − Σ_ν a⁽³⁾)` and `min(mult_R, Σ_ν i⁽³⁾)`.
**The converse of Prop. 8(2) is false** (§4, PROVED): a Pieri-compatible cubic
constituent need not contribute; the smallest instance is two lines in a
two-dimensional weight space that fail to coincide, `8c₃₀c₁₂ − 3c₂₁²` against
`3c₃₀c₁₂ − c₂₁²`.  Across 82 exactly computed model cells (CERTIFIED over `Q`),
only 4 of 156 Pieri-compatible constituent/cell pairs contribute on their own,
the criterion agrees with direct measurement everywhere, and one cell's
additional padded equation restricts to a combination of three cubic channels
none of which descends alone.  A cheap, exact certificate of non-descent (the
swap identity, §5, PROVED) detected every one of the 152 non-descents.  The
fifteen degree-13 predecessors of `λ₁₃` are re-derived and reconcile with the
audit log entry for entry (§6); the length quantifier is stated in quotable form
(§7); at `λ₁₃` the reducible image is a 36-to-39-dimensional subspace of a
73-dimensional channel space, so no dimension count forces a transfer there,
and the fifteen-cell predecessor screen — a targeted screen for one quartic
cell, not a census of `I(D₉^{per₃})₁₃` — is sufficient but far from necessary
for `mult_pad = mult_red` at `λ₁₃` (§8).  What was not reached, with prices, is
in §9; defects in the assignment are in §10.

## 1. Inputs, preflight, host

| | |
|---|---|
| clone | `0049511`; `docs/batch13_board.md`, `docs/batch13_corrections.md`, `docs/stocktake_batch12.md`, `docs/batch13_worker_preamble.md` present |
| read in full | the four above, `docs/brief_wording.md`, `docs/transfer_lemma.md`, `docs/washout_lemma.md`, `docs/rung13_reducible.md`, `docs/s4_batch12_review.md`, `results/astra/S4/S4_report.md` (factorization section), `results/logs/wk12_int_pred13_audit.log`, `analysis/wk8_s30_core.py`, `tools/verify/{pleth,chi_build}.py` |
| host | 2 CPU (Xeon 2.80 GHz), 7 GB RAM, no swap, ~30 GB disk; a separate cloud container, so this is the whole budget — one heavy run at a time, `ulimit -v ≤ 4 GB` |
| toolchain | numpy 2.4.4, scipy 1.17.1 pre-installed; **installed here**: python-flint 0.9.0, sympy 1.14.0, mpmath 1.3.0 |
| runs | every run bounded with `timeout` and `ulimit -v`, pid in `results/logs/b13_04_*.pid`; the one run ended early (the first audit attempt, Frobenius plethysm out of memory at 3 GB) was ended by its recorded pid |
| `exps` orderings | this session's code never resolves a letter by position; letters are dict keys (exponent tuples) throughout |

## 2. Setting and notation

`V = Cʳ` with coordinates `x₁..x_r`; `Q_δ = C[Sym⁴V*]_δ = Sym^δ(Sym⁴V)` the
quartic coordinate ring and `C_δ = C[Sym³V*]_δ` the cubic one, with coordinate
functionals `q_β` (`|β| = 4`) and `c_α` (`|α| = 3`) reading off monomial
coefficients.  `GL_r` acts as in `tools/verify/FORMAT.md`:
`E_ij c_α = (α_i + 1) c_{α + e_i − e_j}`; a highest-weight vector (HWV) is
killed by every `E_ij`, `i < j`, hence fixed by the unipotent group `U` they
generate.  `H_λ = HWV_λ(Q_δ)`, `a⁽⁴⁾(λ,δ) = dim H_λ`; for a `GL_r`-stable closed
cone `X`, `i_X(λ,δ) = dim HWV_λ(I(X)_δ)` and `mult_X(λ,δ) = a⁽⁴⁾ − i_X`.

`μ : V* × Sym³V* → Sym⁴V*`, `(ℓ,c) ↦ ℓ·c`; `μ*(q_β) = Σ_i ℓ_i c_{β−e_i}` (no
`β_i` factor; S4's coefficient formula).  `R = μ(V* × Sym³V*)` is the reducible
locus, `W_δ = μ*(Q_δ) ≅ C[R]_δ ⊆ B_δ := Sym^δV ⊗ C_δ`.  `D ⊆ Sym³V*` is any
`GL_r`-stable closed cone — `D_r^{per₃}` in the programme, `D_r^f` for the model
cubics `f` here — with `J_δ = I(D)_δ`, and `P = μ(V* × D)` the padded variety
(closed, and equal to the closure of the parametrised padded points because
`μ` is proper on projectivisations and `D`'s parametrisation is dense in `D`).
For `λ ⊢ 4δ` with `λ₁ ≥ δ`, `λ⁻ := (λ₁ − δ, λ₂, …, λ_r)`; a **predecessor** of
`(λ,δ)` is a `ν` with `λ/ν` a horizontal `δ`-strip (§7 for the quantifier).

## 3. The exact criterion

**Theorem A (exact transfer; PROVED).**  `μ*` induces a `GL_r`-equivariant
isomorphism

    I(P)_δ / I(R)_δ   ≅   W_δ ∩ ( Sym^δ V ⊗ J_δ ).

Hence for every `λ`:  `mult_R(λ,δ) − mult_P(λ,δ) = i_P − i_R = dim HWV_λ( W_δ ∩ (Sym^δV ⊗ J_δ) )`.

*Proof.*  `h ∈ I(R)` iff `μ*h = 0` (`μ` dominant onto `R`); `h ∈ I(P)` iff
`μ*h` vanishes on `V* × D` iff `μ*h ∈ I(V* × D) = C[V*] ⊗ J` (ideal of a
product with an affine space), in bidegree `(δ,δ)`.  So `μ*` maps `I(P)_δ` into
`W_δ ∩ (Sym^δV ⊗ J_δ)` with kernel `I(R)_δ`, and onto it: any `μ*h` in the
right-hand side has `h ∈ I(P)_δ` by the same equivalence.  Multiplicities of a
submodule intersection are the dimensions of the intersected HWV spaces.  ∎

This is the equality behind Prop. 8's injection, and it is also the
ideal-theoretic form of S4's factorization identity
`rank T_pad = rank S − dim(S(M_λ) ∩ K)` (`results/astra/S4/S4_report.md`,
PROVED there, verified in `docs/s4_batch12_review.md`); nothing in Theorem A is
claimed as new beyond the identification with Prop. 8.

**Lemma B (fixed factor; (i)–(ii) for `R` are S4's fixed-factor kernel lemma,
PROVED there; the extension to `P` and (iii)–(iv) PROVED here).**  For
`h ∈ H_λ` put `ρ(h)(c) := h(x₁·c)`, a polynomial in `C_δ` of weight `λ⁻`.  Then

1. for every `ℓ` with `ℓ₁ ≠ 0`, `h(ℓ·c) = ℓ₁^δ · ρ(h)(u_ℓ⁻¹c)`, where `u_ℓ ∈ U`
   is the shear with `u_ℓ x₁ = ℓ/ℓ₁` (so `u_ℓ⁻¹c = c(x₁ − Σ_{j≥2}(ℓ_j/ℓ₁)x_j, x₂, …, x_r)`);
2. `h ∈ I(R)_δ ⟺ ρ(h) = 0`, and `h ∈ I(P)_δ ⟺ ρ(h) ∈ J_δ`;
3. `ρ : H_λ → C_δ` has kernel `HWV_λ(I(R)_δ)`, so `rank ρ = mult_R(λ,δ)`, and
   **`mult_R(λ,δ) − mult_P(λ,δ) = dim( ρ(H_λ) ∩ J_δ )`**;
4. in monomial terms `ρ` deletes every monomial of `h` containing a letter
   `q_β` with `β₁ = 0` and relabels the surviving ("`x₁`-pure") monomials by
   `β ↦ β − e₁`, injectively.  Hence `HWV_λ(I(R)_δ)` is exactly the set of
   HWVs every monomial of which contains a letter not divisible by `x₁`; and
   `mult_R(λ,δ) = 0` whenever `λ₁ < δ`.

*Proof.*  `U` fixes `h`, `U` acts on forms by substitution (ring
automorphisms), and `U·x₁ = {x₁ + Σ_{j≥2} t_j x_j}`, so for `ℓ₁ ≠ 0`:
`h(ℓc) = h(ℓ₁(u x₁)c) = ℓ₁^δ h(u·(x₁·u⁻¹c)) = ℓ₁^δ (u⁻¹·h)(x₁·u⁻¹c) = ℓ₁^δ ρ(h)(u⁻¹c)`.
(1) gives (2): `{ℓ₁ ≠ 0}` is dense in `V*`, `u⁻¹` permutes `Sym³V*` and
preserves `D`.  (3) restates (2).  (4): `x₁·c` has `q_β = c_{β−e₁}` for
`β₁ ≥ 1` and `q_β = 0` otherwise; `β ↦ β − e₁` is injective on `{β₁ ≥ 1}`, so
distinct pure monomials map to distinct cubic monomials and no cancellation
occurs; if `λ₁ < δ` no monomial of weight `λ` is pure.  ∎

**Proposition C (channels; PROVED).**  Let `B^λ ⊆ C_δ` be the span, over the
predecessors `ν` of `(λ,δ)`, of the vectors of weight `λ⁻` in the `S_ν`-isotypic
part of `C_δ` that are killed by `E_ij` for `2 ≤ i < j ≤ r`.  Then
`B^λ = ⊕_ν B^λ_ν` with `dim B^λ_ν = a⁽³⁾(ν,δ)`: each copy `S_ν ⊆ C_δ` with HWV
`g` contributes one line, spanned by the **branching vector** `g^{↓λ}` — the
unique-up-to-scalar vector of weight `λ⁻` in `S_ν(g)` that is `GL_{r−1}`-highest
(indices `2..r`).  Moreover `ρ(H_λ) ⊆ B^λ`, and with `J^λ := J_δ ∩ B^λ = ⊕_ν
(J_δ ∩ B^λ_ν)`, `dim(J_δ ∩ B^λ_ν) = i⁽³⁾(ν,δ)`,

    mult_R(λ,δ) − mult_P(λ,δ)  =  dim( ρ(H_λ) ∩ J^λ ),      ρ(H_λ) ⊆ B^λ = ⊕_ν B^λ_ν,  dim B^λ = Σ_ν a⁽³⁾(ν,δ).

*Proof.*  `μ*h ∈ Sym^δV ⊗ C_δ` is a HWV of weight `λ`; by Pieri its component
in `Sym^δV ⊗ C_δ[ν]` is nonzero only for predecessors `ν`.  `ρ(h)` is the
coefficient of `ℓ₁^δ` in `μ*h`; `E_ij` with `i,j ≥ 2` kills `ℓ₁^δ` and does not
produce `ℓ₁^δ` from any other `ℓ^α`, so `ρ(h)` is `GL_{r−1}`-highest of weight
`(λ₂..λ_r)`, `x₁`-weight `λ₁ − δ`, and lies in the predecessor isotypic parts.
Branching `GL_r ↓ GL₁ × GL_{r−1}`: `S_ν` contains a `GL_{r−1}`-highest vector of
weight `κ = (λ₂..λ_r)` and `x₁`-weight `m` iff `κ` interlaces `ν` and
`m = |ν| − |κ|`, with multiplicity one — for a predecessor, `κ` interlaces `ν`
by the strip condition and `m = λ₁ − δ`.  The rest is Theorem A read through
Lemma B(3).  ∎

(Isotypic pieces of `C_δ` with `κ` interlacing `ν` but `ν₁ > λ₁` carry vectors
of the same type; `ρ(H_λ)` never meets them, so they are not channels.)

**Corollary D (bounds; PROVED).**  With both sums over the predecessors of `(λ,δ)`,

    max( 0,  Σ_ν i⁽³⁾(ν,δ) + mult_R(λ,δ) − Σ_ν a⁽³⁾(ν,δ) )   ≤   mult_R − mult_P   ≤   min( mult_R(λ,δ),  Σ_ν i⁽³⁾(ν,δ) ).

The upper bound is Prop. 8(2) made quantitative (each constituent contributes
at most its cubic nullity; no constituent, no gap).  The lower bound is the
dimension count of two subspaces of `B^λ`.  Two sufficient conditions follow at
once: **(S1)** if `mult_R = Σ_ν a⁽³⁾` then `ρ(H_λ) = B^λ` and the gap is
`Σ_ν i⁽³⁾` — every constituent transfers; **(S2)** if `Σ_ν i⁽³⁾ = Σ_ν a⁽³⁾`
(every predecessor channel lies in the cubic ideal) then `mult_P = 0`.  More
generally a gap is **forced** whenever `Σ_ν i⁽³⁾ + mult_R > Σ_ν a⁽³⁾`.

**Per-constituent form.**  A copy `S_ν ⊆ J_δ` with HWV `g` contributes on its
own at `λ` — the gap has a witness whose reducible restriction lies in that
copy's channel — iff `g^{↓λ} ∈ ρ(H_λ)`, i.e. iff some quartic HWV `h` of weight
`λ` satisfies `h(x₁·c) = g^{↓λ}(c)` identically.  This is sufficient for a gap
and, by Theorem A, the gap is the dimension of the intersection, which can be
positive with no constituent contributing on its own (§4, the `(8,4,4)` cell).

## 4. The converse of Prop. 8(2) is false

The proposed converse: *if `S_ν ⊆ I(D)_δ` and `λ/ν` is a horizontal
`δ`-strip, then `mult_P(λ,δ) < mult_R(λ,δ)`.*  (The board asks for a
counterexample to "a proposed converse" without stating one; this is the
natural one, and Prop. 8(2)'s wording "requires" invites it.)

**Theorem E (PROVED, by hand and by machine).**  `r = 2`, `f = x₁³`,
`D = {m³}` (the Veronese cone), `δ = 2`.  `I(D)_2 = S_{(4,2)}`, spanned by
`g = 3c₃₀c₁₂ − c₂₁²` (a `2×2` catalecticant minor, `E₁₂g = 0`, `g(m³) ≡ 0`).
`λ = (6,2)` is a horizontal 2-strip over `(4,2)` and `a⁽⁴⁾((6,2),2) = 1`, with
`h = 8q₄₀q₂₂ − 3q₃₁²` (`E₁₂h = 3·8 q₄₀q₃₁ − 8·3 q₄₀q₃₁ = 0`).  Then

    ρ(h) = 8c₃₀c₁₂ − 3c₂₁²  ∉  C·(3c₃₀c₁₂ − c₂₁²) = J_2 ∩ (weight (4,2)),

so `h ∉ I(P)` (Lemma B(2)), `mult_P((6,2),2) = mult_R((6,2),2) = 1`, and the
Pieri-compatible constituent contributes nothing.  Directly: `h(x₂·x₁³) = −3 ≠ 0`
at the padded point `x₂·x₁³` (`q₃₁ = 1`, every other coordinate 0).  For contrast, `λ = (4,4)` over the same `ν`:
`h = 12q₄₀q₀₄ − 3q₃₁q₁₃ + q₂₂²` (the classical degree-2 invariant of binary
quartics), `ρ(h) = 3c₂₁c₀₃ − c₁₂²`, which is the branching vector `g^{↓(4,4)}`
(`= ½ E₂₁²g`), so the gap is 1: `mult_R = 1`, `mult_P = 0` (`I` vanishes on a
quartic with a triple root).  Both cells are in `results/b13_04/model_A_d2.json`.

**The models (CERTIFIED over `Q`; `analysis/wk13_b04_model.py`).**  Everything
below is exact: HWVs are integer kernels of the raising operators; `mult_R` is
`rank ρ` over `Q` and, independently, the rank of evaluation at 60 integer
reducible points over `Q` (both primes as cross-checks); `mult_P` is the rank at
60 padded points `ℓ·f(As)` and, independently, at fixed-factor points
`x₁·f(As)`; the cubic ideal in the weight-`λ⁻` space is the kernel of evaluation
with **every** basis vector certified by symbolic substitution `c = f(A·s)`,
`A` symbolic (flint `fmpz_mpoly` identity over `Z`); the criterion is
`dim ρ(H_λ) + dim J_{λ⁻} − dim(ρ(H_λ) + J_{λ⁻})`; branching vectors are computed
by lowering operators and intersected with the `GL_{r−1}`-highest condition.

| model | `f`, `r` | `δ` | cells | cubic ideal `I(D_r^f)_δ` | pairs `(ν,λ)` with `i⁽³⁾ ≥ 1` | contribute alone | cells with gap (total gap) | gap = lower bound of Cor. D |
|---|---|---|---|---|---|---|---|---|
| A | `x³`, 2 | 2 | 3 | `S_{42}` | 2 | 1 | 1 (1) | 3/3 |
| B | `x³+y³`, 3 (`D = Sub₂`) | 3 | 9 | `S_{522} ⊕ S_{441}` | 5 | 1 | 1 (1) | 9/9 |
| B | | 4 | 18 | `S_{822} ⊕ S_{741} ⊕ S_{732} ⊕ S_{642} ⊕ S_{444}` | 28 | 0 | 1 (1) | 18/18 |
| B (exploratory) | | 5 | 34 | 11 copies in 10 shapes (`S_{942}` twice) | 115 | 2 | 10 (14) | 29/34 |
| C (exploratory) | `xyz`, 3 (Chow) | 4 | 18 | `S_{732}` | 6 | 0 | 0 (0) | 18/18 |

Consistency checks that held in all 82 cells: `mult_R` by `ρ` = `mult_R` by
reducible points; `mult_P` by padded points = by fixed-factor points;
criterion = `mult_R − mult_P`; criterion = `dim(ρ(H_λ) ∩ span of branching
vectors)`.  Every additional padded equation found is shipped as an explicit
integer combination of the HWV basis with `ρ(h)` certified in the ideal and
`h` nonzero at a reducible point (`witnesses` in the JSON).

Three things the models show:

- **Pieri compatibility is far from sufficient.**  4 of 156 compatible pairs
  contribute alone; in Model B at `δ = 4` all 28 fail.
- **The gap is not channel-by-channel.**  At `((8,4,4), δ=4)` in Model B the
  gap is 1 (`mult_R = 2`, `mult_P = 1`), no branching vector lies in
  `ρ(H_λ)`, and the witness (`q₄₀₀ · I₃`, `I₃` the degree-3 invariant of
  ternary quartics that is the `((4,4,4),3)` equation) restricts to
  `ρ(h) = (4·b_{741} + 15·b_{642} + 7·b_{444})/420`, a combination of the
  branching vectors of all three predecessor constituents (as stored,
  gcd-normalised, in the JSON).
- **The dimension count is often, not always, the whole story.**  In the 30
  pre-registered cells the gap equals the lower bound of Cor. D (every gap is
  forced by dimension).  At `δ = 5` (exploratory) five cells —
  `(14,4,2)`, `(13,4,3)`, `(12,6,2)`, `(11,6,3)`, `(10,7,3)` — have gap 1 with
  lower bound 0: the first additional equations not forced by a count.  So the
  exact criterion is needed; Cor. D is a screen on both sides, not a substitute.

## 5. A cheap exact certificate of non-descent: the swap identity

**Lemma F (PROVED).**  For every `F ∈ ρ(H_λ)`, every `ℓ` with `ℓ₁ ≠ 0` and every
quadric `q`:

    F(ℓ·q)  =  ℓ₁^δ · F( u_ℓ⁻¹(x₁·q) ),        u_ℓ⁻¹(x₁q) = (x₁ − Σ_{j≥2}(ℓ_j/ℓ₁)x_j) · q(x₁ − Σ_{j≥2}(ℓ_j/ℓ₁)x_j, x₂, …, x_r).

*Proof.*  Lemma B(1) applied to the reducible cubic `ℓ·q` and to `x₁·q`:
`F(ℓq) = h(x₁ℓq) = h(ℓ·x₁q) = ℓ₁^δ ρ(h)(u_ℓ⁻¹(x₁q))`.  ∎

A branching vector `g^{↓λ}` that violates the identity at one integer point
`(ℓ, q)` is certifiably outside `ρ(H_λ)`: that constituent does not contribute
on its own, by an exact integer computation at two points.  In the models the
identity was asserted for every `ρ(h)` (held, all cells) and a violating point
was searched for every non-descending branching vector: **152 of 152 found**,
first try in almost every case (`swap_certificates` in the JSON; e.g. at
Model A `(6,2)`: `ℓ = (1,5)`, `q = −5x² − 5xy + 5y²`, left side `−600`, right
side `−100`).  The identity is necessary, not sufficient (MEASURED: it never
failed to detect a non-descent here; no claim beyond the models).

## 6. The degree-13 predecessor audit

**RECORDED and independently re-derived (`analysis/wk13_b04_pred13.py`,
`results/b13_04/pred13.json`, `results/logs/b13_04_pred13_reconcile.log`).**
Own interlacing enumerator; `N_S` by `tools/verify/chi_build.weight_monomials_count`
(the tail DP); `a` by the Kostant alternation over `S_r` with `W`-sorted weight
caching (the Frobenius engine `analysis/wk8_s30_pleth` exceeds 3 GB at
`δ = 13`); 111 s.  The Kostant route was checked against the exact HWV kernels
of the models and against s37's banked `δ = 6` cells before use.

`λ₁₃ = (21,17,2⁷)`, `|λ| = 52`, `δ = 13`: **fifteen** predecessors, all of size
39 with at most nine parts — five of length 8 (`ν₉ = 0`), ten of length 9.
All fifteen shapes, all fifteen `a` and all fifteen `N_S` agree with
`results/logs/wk12_int_pred13_audit.log` entry for entry; `a⁽⁴⁾(λ₁₃,13) = 39`
reproduced.

| `ν` | parts | `a⁽³⁾` | `N_S` |
|---|---|---|---|
| `(21,6,2⁶)` | 8 | 5 | 15,938,771 |
| `(20,7,2⁶)` | 8 | 6 | 24,106,596 |
| `(19,8,2⁶)` | 8 | 8 | 34,104,118 |
| `(18,9,2⁶)` | 8 | 9 | 45,302,282 |
| `(17,10,2⁶)` | 8 | 9 | 56,619,400 |
| `(21,5,2⁶,1)` | 9 | 1 | 60,408,023 |
| `(20,6,2⁶,1)` | 9 | 2 | 100,317,022 |
| `(21,4,2⁷)` | 9 | 2 | 117,718,904 |
| `(19,7,2⁶,1)` | 9 | 3 | 153,401,944 |
| `(18,8,2⁶,1)` | 9 | 4 | 218,042,768 |
| `(20,5,2⁷)` | 9 | 3 | 219,816,302 |
| `(17,9,2⁶,1)` | 9 | 4 | 289,180,512 |
| `(19,6,2⁷)` | 9 | 5 | 369,720,484 |
| `(18,7,2⁷)` | 9 | 5 | 569,323,864 |
| `(17,8,2⁷)` | 9 | 7 | 809,527,307 |

`Σ_ν a⁽³⁾(ν,13) = 73`; `N_S` from `1.59·10⁷` at `(21,6,2⁶)` to `8.10·10⁸` at
`(17,8,2⁷)`, total `3.08·10⁹`.  The board's two prose corrections are
confirmed: the cheapest is `(21,6,2⁶)` with eight parts, and `(19,6,2⁷)` has
nine parts; `(19,6,2⁷,2)` and `(21,6,2⁷)` are not predecessors (sizes 41 and
41).  One further stale line: `docs/stocktake_batch12.md` §7 still quotes the
range as `1.6·10⁷` to `3.7·10⁸` (the truncated list); the board's `8.10·10⁸` is
right.

**Scope (stated as the board asks).**  A predecessor screen is targeted at one
quartic cell: the fifteen are the constituents of `I(D₉^{per₃})₁₃` that can
reach `λ₁₃` through Theorem A, and running them certifies `mult_pad = mult_red`
at `λ₁₃` (and at any other degree-13 quartic weight all of whose predecessors
are among them).  They do not exhaust `I(D₉^{per₃})₁₃`: the census of that ideal
runs over every `ν ⊢ 39` of length 6 to 9 with `a⁽³⁾(ν,13) ≥ 1` — there are
10,046 partitions of 39 with 6 to 9 parts (1,729 / 2,400 / 2,857 / 3,060 by
length; lengths `≤ 5` are excluded by Theorem 2), of which the fifteen are a
targeted subset.  "In full" was the wrong word and the board is right to
retire it.

## 7. The length quantifier, once, in a form a brief can quote

> Let `λ` be a quartic weight of length `r` and degree `δ`.  The cubic
> predecessors of `(λ,δ)` are the `μ` with
> `λ₁ ≥ μ₁ ≥ λ₂ ≥ μ₂ ≥ … ≥ λ_r ≥ μ_r ≥ 0` and `|μ| = |λ| − δ`.  Since `μ_r` may
> be 0, a predecessor has length `r` or `r − 1`, and both lengths pair with
> `λ`.  A predecessor of length `k` enters the transfer only through
> `i⁽³⁾(μ,δ) = a⁽³⁾(μ,δ) − mult_μ C[D_k^{per₃}]_δ`, its **length-`k`** value
> (restriction lemma, `docs/washout_lemma.md` §1), which may be computed in `k`
> variables.  It may be **ignored** — `i⁽³⁾(μ,δ) = 0` entered without
> computation — exactly when that length-`k` value is already known to be zero:
> for every `k ≤ 5` and every `δ`, by Theorem 2 of `docs/washout_lemma.md`
> (`D_k^{per₃} = Sym³Cᵏ`); and for `(k,δ)` pairs closed by an earlier full-rank
> scan, e.g. `k = 6`, `δ ≤ 9` (s79 with Theorem 2; B13-07 audits that chain).
> Otherwise it is as live as a full-length predecessor: at `λ₁₃` the five
> length-8 predecessors are not ignorable.  Whether ignored or not, its channel
> dimension `a⁽³⁾(μ,δ)` counts in `Σ_ν a⁽³⁾` of Corollary D.

Two consequences worth a line each.  For a six-row quartic cell only the
length-6 predecessors need cubic computation (the length-5 ones are ignorable),
which is why s79's length-6 cubic scan at `δ = 9`, with Theorem 2, closes
every six-row quartic weight at `δ = 9` (Prop. 8(1) closes them all at once).  And at
`λ₁₃`, `k = 8 > 5`: nothing is inherited; the five length-8 cells cost what the
table says, at `r = 8` (same `N_S`, one raising operator fewer).

## 8. The goal cell: what the criterion says at `λ₁₃`, and what it costs

Numbers (RECORDED/CERTIFIED as marked): `a⁽⁴⁾(λ₁₃,13) = 39` (re-derived);
`mult_R(λ₁₃,13) ≥ 36` CERTIFIED (nonzero 36-minor, `docs/rung13_reducible.md`),
`= 36` MEASURED; `dim B^{λ₁₃} = Σ_ν a⁽³⁾ = 73`; `λ₁₃⁻ = (8,17,2⁷)`, whose
weight space in `C₁₃` has dimension 809,527,307 `= N_S(17,8,2⁷)` (`W`-symmetry).
`Σ_ν i⁽³⁾(ν,13)` is unknown; every one of the fifteen has `a ≥ 1`.

What Corollary D says at `λ₁₃`:

    max(0, Σ_ν i⁽³⁾ − 37)  ≤  mult_red − mult_pad  ≤  min(36, Σ_ν i⁽³⁾)        (if mult_R = 36; with 39 read 34 for 37)

- **No dimension count forces a transfer**: the reducible image is a 36-
  dimensional subspace of a 73-dimensional channel space.  A forced gap would
  need at least 38 of the 73 channel dimensions inside the cubic ideal.
- **A transfer with `Σ_ν i⁽³⁾ ≤ 37` needs special position** — the reducible
  image must meet the ideal's part of the channel space without being made to.
  The models show that special position does occur (five cells at `δ = 5`), so
  this is not evidence against a permanent-specific equation at `λ₁₃`; it is
  the statement of what one would have to be.
- **The predecessor screen is sufficient, not necessary.**  `Σ_ν i⁽³⁾ = 0`
  (all fifteen at full cubic rank, one prime each) certifies `mult_pad =
  mult_red` at `λ₁₃`.  Conversely `mult_pad = mult_red` is compatible with up
  to 37 ideal dimensions in the channels.

This is the degree-13 form of S4's degree-24 count (`rank S ≤ 274` inside the
inherited 521-dimensional intermediate): 39 against 73 here, 274 against 521
there, the same shape.

**Prices.**

| route | what it certifies | cost | status |
|---|---|---|---|
| fifteen cubic cells (the predecessor screen) | `Σ_ν i⁽³⁾ = 0` ⟹ gap 0 at `λ₁₃`; or the ideal HWVs `g` if any cell is deficient (then membership must still be certified) | `N_S` `1.59·10⁷`–`8.10·10⁸`, `N_S·δ` `2.1·10⁸`–`1.05·10¹⁰`; **all fifteen** are above s79's build wall `N_S·δ ≈ 1.5·10⁸` (rows > 4 GB), by factors 1.4 to 70 | waits on B13-10's builder; batch 14 |
| the fixed-factor weight space `(8,17,2⁷)` | all fifteen channels in one rank computation (`ρ(H_λ)`, `J^λ` and their intersection at once) | one weight space of dimension `8.1·10⁸` — the dearest predecessor's size; no saving in peak memory, a saving in bookkeeping only | not run |
| B13-01's three reducible identities + the certified `rank T_pad ≥ 36` | `mult_R ≤ 36 = mult_P` ⟹ gap 0 at `λ₁₃`, with **no cubic computation** | whatever B13-01 costs; one identity gives gap `≤ 2`, two give `≤ 1` | in flight, other session |
| after the cubic cells: deciding the intersection | `dim(ρ(H_λ) ∩ J^λ)` exactly | 39 fixed-factor evaluations `h_i(x₁·c_j)` per cubic point (`≈ 0.2 s` per row per point on the s69 circuit, `docs/rung13_reducible.md`) plus the 73 branching vectors evaluated at the same points; a nonzero `73`-minor of the branching-vector evaluation makes evaluation injective on `B^λ` and every subspace statement exact | after the screen |

The quartic HWVs at `λ₁₃` cannot be expanded in monomials: the weight-`λ₁₃`
space of `Q₁₃` has `80,921,422,068` monomials (tail DP), which is why s74's
source is a circuit and why Lemma B(4)'s support test, exact and cheap on an
expanded basis, is not available at the goal cell.

## 9. What was not done, and what it would cost

- No cubic cell at the goal rung was run (pre-registered exclusion; above the
  host and above the wall).  The screen's price is in §8.
- No `per₃` example of the transfer mechanism exists to compute on: every
  measured `I(D_r^{per₃})_δ` in the tree is zero (`r ≤ 5` all `δ`; `r = 6`,
  `δ ≤ 9`).  The models use other cubics (`x³`, cubics in two variables,
  `xyz`); the theorems are general, the numerical behaviour is the models'.
  A first `per₃` instance costs the first deficient cubic cell — the degree-10
  length-6 remainder (B13-08) is the cheapest place it could appear.
- Lemma B(4)'s support test was not exercised on a house cell with a reducible
  deficiency (none of the models has `I(R)_δ ≠ 0` at these sizes; the smallest
  six-row cell with a measured reducible deficiency, `(21,12,4,1,1,1)₁₀`, has
  `N_S = 125,231`, beyond dense exact arithmetic here).  Price: one exact
  kernel of the raising operators restricted to the non-`x₁`-pure columns, or a
  modular kernel vector reconstructed and verified over `Z` (`E·v = 0` and
  support off the pure monomials), which would upgrade a MEASURED `i_red ≥ 1`
  to CERTIFIED at that cell.  This is B13-03's territory and is offered to it.
- No sufficient condition beyond Corollary D's dimension count was found that
  does not require computing the intersection.  The intrinsic question —
  which vectors of `B^λ` extend to quartic HWVs — is the question of which
  functions on the normalisation `P(V*) × P(Sym³V*)` descend to the
  non-normal `R`; the swap identity is the two-point part of the descent
  conditions along `{ℓ₁ℓ₂q}`, and a complete list (including the tangential
  conditions along `{ℓ²q}`) was not derived.
- Model B at `δ ≥ 6`, and any model at `r ≥ 4`, were not run: dense exact
  linear algebra on weight spaces of a few thousand monomials is minutes, and
  the ideal certification scales with it; `δ = 6` at `r = 3` is an hour-class
  job on this host, not attempted.

## 10. Defects in the assignment, for the integrator

1. The B13-04 entry asks for the criterion "through the intersection of the
   multiplication pullback's image with the cubic ideal" without citing S4,
   whose factorization identity is that intersection on multiplicity spaces
   (PROVED, batch 12).  A session could re-derive it unaware.  The entry
   should point at `results/astra/S4/S4_report.md` §"The factorization" and
   `docs/s4_batch12_review.md` §1 items 1–2.
2. "A counterexample to a proposed converse" — no converse is proposed anywhere
   in the tree.  This report states the one it refutes (§4); the brief should
   state it.
3. "Existing small exact controls" are named as inputs but none with a nonzero
   cubic ideal exists for `per₃`; the models here had to be built.  The brief
   should say that a model cubic is expected.
4. `docs/stocktake_batch12.md` §7 still carries the truncated `N_S` range
   (`3.7·10⁸`); the board corrected it to `8.10·10⁸`.
5. `analysis/wk8_s30_pleth.amb` (Frobenius plethysm) is not usable at
   `δ = 13, r = 9` on a 3 GB budget; the Kostant tail alternation in
   `analysis/wk9_s42_census.a_weyl` is, and is faster still with `W`-sorted
   caching (`analysis/wk13_b04_pred13.kostant`).  Worth a line in the preamble's
   tool list.
6. Not a defect but a suggestion: the "length quantifier" paragraph of §7 could
   replace the four scattered sentences in the board's B13-04 entry.

## 11. Files, replay

| path | what |
|---|---|
| `results/PREREG_b13_04.md` | pre-registration (commit `35148d8`) |
| `analysis/wk13_b04_model.py` | the exact instrument; `python3 analysis/wk13_b04_model.py A` / `B 3` / `B 4` / `B 5` / `C 4` (seconds each) |
| `results/b13_04/model_{A_d2,B_d3,B_d4,B_d5,C_d4}.json` | every cell: `a⁽⁴⁾`, `mult_R` (fixed-factor over `Q`, points over `Q`, both primes), `mult_P` (padded and fixed-factor points), `dim J_{λ⁻}` with certification flag, criterion, direct gap, per-predecessor `a⁽³⁾`, `i⁽³⁾`, branching vectors, `branch_in_W`, swap certificates, explicit witnesses.  All stored values are native (`values_are: none`); points are regenerated from `seed = 20260909`, `bound = 7` |
| `results/logs/b13_04_model*.log` | run logs |
| `analysis/wk13_b04_pred13.py`, `results/b13_04/pred13.json`, `results/logs/b13_04_pred13{,_reconcile}.log` | the audit and its reconciliation |
| `docs/b13_04_report.md` | this report |

Replay of the criterion at any cell of the models is `run_model(...)` with the
same seed; a different seed changes only the point families and must give the
same ranks (they are exact statements about the ideal, not about the points).

## 12. Ledger

| claim | label |
|---|---|
| Theorem A: `I(P)_δ/I(R)_δ ≅ W_δ ∩ (Sym^δV ⊗ J_δ)`; gap = dim of the intersection | PROVED (the identity of S4's factorization, identified with Prop. 8) |
| Lemma B: fixed-factor restriction; `h ∈ I(R) ⟺ ρ(h) = 0`, `h ∈ I(P) ⟺ ρ(h) ∈ J`; support form; `mult_R = 0` for `λ₁ < δ` | PROVED (kernel half is S4's lemma) |
| Proposition C: `ρ(H_λ) ⊆ ⊕_ν B^λ_ν`, `dim B^λ_ν = a⁽³⁾(ν,δ)`, branching vectors | PROVED |
| Corollary D: the two-sided bound; conditions S1, S2; forced gaps | PROVED |
| Theorem E: the converse of Prop. 8(2) fails at `((6,2), 2)` over `(4,2)` for `f = x³` | PROVED, machine-confirmed |
| Lemma F: the swap identity | PROVED |
| 82 model cells: all ranks, ideals, gaps, witnesses | CERTIFIED over `Q` (ideal membership by symbolic identity; ranks exact) |
| in the 30 pre-registered cells the gap equals Cor. D's lower bound; at `δ = 5` five cells exceed it | CERTIFIED (exact facts about the models), exploratory at `δ = 5` |
| the swap identity detected all 152 non-descents | MEASURED (a property of the search, not a theorem) |
| fifteen predecessors of `λ₁₃`, `a`, `N_S`, `Σ a⁽³⁾ = 73`, `a⁽⁴⁾ = 39` | re-derived, agree with the audit log (CERTIFIED as exact counts; the audit log RECORDED) |
| `dim(weight (8,17,2⁷)) = 809,527,307`; `N_S(λ₁₃) = 80,921,422,068` in `Q₁₃` | CERTIFIED (tail DP) |
| `mult_R(λ₁₃,13) = 36` | ADOPTED from `docs/rung13_reducible.md`: `≥ 36` certified, `= 36` measured |
| Theorem 2 (`k ≤ 5`), the restriction lemma, Prop. 8 | ADOPTED (`docs/washout_lemma.md`, `docs/transfer_lemma.md`) |
| nothing about `I(D₉^{per₃})₁₃` itself | not computed; priced in §8 |

Author of record for this session: B13-04 (Claude Fable 5.1), for Swami
Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
board_numbering: batch13
