# B13-04 — sharpen the cubic-to-quartic transfer

board_numbering: batch13
session: B13-04 (the board's "sharpen the cubic-to-quartic transfer")
model: **two** — the session's first pass (everything through commit `2b89394`:
§§1–12) ran as **Claude Fable 5.1** (`claude-fable-5-1`); at a model-availability
limit the session was continued as **Claude Opus 5** (`claude-opus-5`), which
produced §12 and this header.  The serving model is not observable from inside
the session; each is recorded as configured at the time, and no result is
attributed to the model that did not produce it.  Commit trailers carry the
same split.
base: `0049511` (`git rev-parse main` at clone); branch `b13_04`
delivery: `b13_04_fable.bundle`, **one part** (`part00` is the whole file), with
`b13_04_fable.bundle.md5` carrying a whole-file digest and the `part00` digest
pre-registration: `results/PREREG_b13_04.md` (commit `35148d8`, before any
computation) with **addendum 1** (commit `b4c6a93`, committed before the
measurements it governs — §12); everything not covered by either is marked
exploratory below
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

**§12 (addendum 1, Claude Opus 5) settles the natural next question with a
second counterexample.**  The swap identity is a candidate *sufficient*
condition — it is cheap, exact, and in 432 of 433 cells across 23 `(r,δ)` pairs
it cuts the channel space down to exactly the descending image, certified.  It
is nevertheless **not sufficient**: at `r = 3`, `δ = 7`, `λ = (16,6,6)` there is
an explicit 78-term integer polynomial that satisfies the swap identity **as a
polynomial identity over `Z`**, satisfies the general two-factor consistency
condition **as a polynomial identity over `Z`**, shows no boundary pole at any
of fifteen specialisations, and is provably not `ρ(h)` for any quartic
highest-weight vector `h`.  So no condition read off the affine slice
`ℓ₁ ≠ 0` — swap, or full fibre-consistency — characterises descent.  The
enlarged model census (199 transfer cells, 646 Pieri-compatible pairs, 13
contributing alone) and a clean demonstration of the length quantifier at
`λ = (7,7,1,1)`, where the only contributing channel is a **shorter**
predecessor, are in §12 too.

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
quartics), `ρ(h) = c₁₂² − 3c₂₁c₀₃`, which is the branching vector `g^{↓(4,4)}`
(a nonzero multiple of `E₂₁²g`; the stored witness is `−ρ(h)`, gcd-normalised),
so the gap is 1: `mult_R = 1`, `mult_P = 0` (`I` vanishes on a
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

**Lemma B(4) on a house cell (exploratory, not pre-registered; CERTIFIED).**
S4's calibration control `(8,8,8)`, `δ = 6`, `r = 3` (`a = 2`, reducible and
padded multiplicity 1, `results/s64_calibration_unified.jsonl`) has
`N_S = 561`, so its two HWVs can be written out over `Q`.  The fixed-factor
restriction `ρ` has rank exactly 1 over `Q`, so `mult_R = 1` and `i_R = 1` are
**certified**; the kernel vector is the first basis HWV itself (S4's "explicit
kernel `(1,0)`"), 377 monomials, **none** of them `x₁`-pure — the support test
of Lemma B(4) passes by inspection — and, as an independent confirmation of the
lemma, `h(ℓ·c)` expanded symbolically in the 13 coefficients of `(ℓ, c)` is the
zero polynomial.  True padded points `ℓ·per₃(As)` give rank 1 as well
(`P₃ = R₃`, Theorem 2).  `analysis/wk13_b04_control888.py`,
`results/b13_04/control_888_d6.json`, 0.8 s.  This is the shape of the
certificate B13-03 can use: a reducible-ideal membership is a support
condition on a highest-weight vector, with no reducible pullback to expand.

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
- Lemma B(4)'s support test was exercised only at the `r = 3` control
  `(8,8,8)₆` (§4).  The measured reducible deficiencies of the record — s64's
  twelve `r = 5` cells (`N_S` from 20,299 at `(9,9,8,1,1)₇`) and s79's 59
  six-row cells (`N_S` from 125,231 at `(21,12,4,1,1,1)₁₀`) — are beyond dense
  exact arithmetic here.  Price to upgrade any one of them from MEASURED
  `i_red ≥ 1` to CERTIFIED: one exact kernel of the raising operators
  restricted to the non-`x₁`-pure columns, or one modular kernel vector
  reconstructed and verified over `Z` (`E·v = 0` and support off the pure
  monomials, both cheap to check once the vector is in hand).  This is
  B13-03's territory and is offered to it.
- No sufficient condition beyond Corollary D's dimension count was found that
  does not require computing the intersection.  **§12 explains why**: the swap
  identity, the natural candidate, is not sufficient (Theorem H), and neither is
  the full two-factor consistency condition.  The intrinsic question —
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
| `analysis/wk13_b04_control888.py`, `results/b13_04/control_888_d6.json`, `results/logs/b13_04_control888.log` | the `(8,8,8)₆` support-test control (exploratory) |
| `analysis/wk13_b04_descent.py` | addendum 1: the swap-identity subspace `T^λ`; `sweep <r> <delta>` runs it model-free |
| `analysis/wk13_b04_swapwitness.py` | the `(16,6,6)` witness and its two symbolic identities |
| `analysis/wk13_b04_fibre.py`, `analysis/wk13_b04_pole.py` | the general two-factor condition; the boundary/pole probe |
| `results/b13_04/descent_*.json`, `swap_witness_r3_d7.json`, `fibre_*.json`, `pole_*.json`, `model_{D,E}_*.json` | addendum-1 data, one file per run |
| `docs/b13_04_report.md` | this report |

Replay of the criterion at any cell of the models is `run_model(...)` with the
same seed; a different seed changes only the point families and must give the
same ranks (they are exact statements about the ideal, not about the points).

## 12. Addendum 1 (Claude Opus 5) — is the swap identity sufficient?

Pre-registered in `results/PREREG_b13_04.md` addendum 1 (commit `b4c6a93`),
committed before these measurements.  Q6 the sufficiency question, Q7 an `r = 4`
model for the length quantifier, Q8 a larger census, Q9 an independent `a`-check.

### 12.1 The question, and why the answer is worth a section

§5 gives the swap identity as a cheap **necessary** condition for a channel
vector to descend.  The board's primary success criterion is a *sufficient*
condition, so the natural move is to ask whether it is also sufficient:

    T^λ  :=  { F ∈ B_full : F(ℓ·q) = F( u_ℓ^{-1}(x₁·q) ) for all ℓ with ℓ₁ = 1,
                                                          all quadrics q },
    B_full := { F of weight λ⁻ : E_{i,i+1}F = 0 for i ≥ 2 }   ⊇ B^λ.

`ρ(H_λ) ⊆ T^λ ⊆ B_full` by Lemma F.  `T^λ` is an exact kernel over `Q` of
linear conditions, and — this is what makes the sweep possible — **the swap
conditions and `B_full` involve only `(r, δ, λ)`, not the cubic `f`**.  So the
descent question is a statement about the reducible locus alone and can be
swept with no model attached (`analysis/wk13_b04_descent.py`, `sweep` mode).

**One-sidedness, stated once (PROVED).**  Sampling can only *under*-constrain a
kernel, so the computed `T^λ` always contains the true one.  Hence a computed
`dim T^λ = mult_R` **certifies** `T^λ = ρ(H_λ)` at that cell — no saturation
caveat.  A computed `dim T^λ > mult_R` is only a ceiling and needs a symbolic
certificate.  Both directions are used below exactly this way.

### 12.2 The sweep: 433 cells, 23 `(r,δ)` pairs, one exception

| `r` | `δ` | cells | swap exact | `Σ mult_R` | `Σ dim B_full` |
|---|---|---|---|---|---|
| 2 | 2,3,4,5,6,7,8,10 | 3+5+6+9+11+13+15+19 = 81 | **81** | | |
| 3 | 2,3,4,5,6,7 | 3+9+18+34+49+69 = 182 | **181** | | |
| 4 | 2,3,4,5 | 3+9+28+72 = 112 | **112** | | |
| 5 | 3,4 | 9+28 = 37 | **37** | | |
| 6 | 3 | 9 | **9** | | |
| 9 | 2,3 | 3+9 = 12 | **12** | | |
| **total** | | **433** | **432** | 887 (sweeps) | 3461 (sweeps) |

Across the twenty sweep files alone the swap identity cuts a total channel
dimension of 3461 down to 887 — exactly `Σ mult_R` — so it is doing real work
and is nowhere vacuous.  Every one of the 432 "exact" verdicts is CERTIFIED by
the one-sidedness above.  (`r = 6, δ = 4` and `r = 5, δ = 5` were still running
at the deadline and are not counted; the partial log shows no exception.)

**The exception, and it is a real one.**

    r = 3,  δ = 7,  λ = (16,6,6),  λ⁻ = (9,6,6):
        a⁽⁴⁾ = 7,   mult_R = rank ρ = 7   (exact over Q),
        dim B_full = 15,   dim T^λ = 8    (two primes agree; 307 points,
                                           fresh seed, 300 stable).

### 12.3 Theorem H — the swap identity is not sufficient (PROVED)

**Theorem H.** There is an explicit integer polynomial `F` of weight `(9,6,6)`
in `C[Sym³C³]₇`, 78 monomials, killed by `E₂₃`, such that

1. `F(ℓ·q) − F(u_ℓ^{-1}(x₁·q))` is the **zero polynomial** in
   `Z[ℓ₂, ℓ₃, q_{200}, …, q_{002}]` — the swap identity holds identically, not
   at sampled points (expansion: 233 monomials on each side, cancelling);
2. `F(u_ℓ^{-1}(ℓ'·q)) − F(u_{ℓ'}^{-1}(ℓ·q))` is likewise the **zero
   polynomial**, now in ten variables (3152 monomials each side) — so `F` also
   satisfies the **general two-factor consistency condition**, of which the
   swap identity is only the `ℓ = x₁` slice;
3. `rank_Q( ρ(H_λ) ∪ {F} ) = 8 > 7 = mult_R`, so `F ∉ ρ(H_λ)`: there is **no**
   quartic highest-weight vector `h` of weight `(16,6,6)` with `h(x₁·c) = F(c)`.

Hence `ρ(H_λ) ⊊ T^λ`, and the swap identity — and even the full two-factor
condition — is necessary but **not** sufficient for descent.  ∎

*Certificates.* `analysis/wk13_b04_swapwitness.py` →
`results/b13_04/swap_witness_r3_d7.json` (the vector, both symbolic checks, the
exact rank); `analysis/wk13_b04_fibre.py` → `results/b13_04/fibre_r3_d7_16-6-6.json`
(the saturated fibre-condition kernel, `dim T_fib = dim T_swap = 8` at both
primes).  Items 1–3 are proofs; the saturated kernels are ceilings and are not
used in the theorem.

**Why this is the right kind of answer.**  Every condition in Theorem H is read
off the affine slice `ℓ₁ ≠ 0`, where the reconstruction `h(ℓ·c) = ℓ₁^δ ρ(h)(u_ℓ^{-1}c)`
of Lemma B(1) is defined.  What Theorem H says is that no such condition can
characterise descent: the obstruction lives at the boundary `ℓ₁ = 0`, where the
reconstruction is a priori only rational.  Writing `ℓ(s) = (s, a₂, …, a_r)`,
every coefficient of `u_{ℓ(s)}^{-1}c` is `N(s)/s^m` with `deg N ≤ 3`, `m ≤ 3`, so

    P(s) := s^{3δ} F(u_{ℓ(s)}^{-1}c)  is a polynomial,  and  h(ℓ(s)·c) = P(s)/s^{2δ},

and descent requires the boundary condition `(POLE)`: `ord_{s=0} P ≥ 2δ`.  A
specialisation can only *raise* the order, so `ord < 2δ` at one integer
`(a, c)` would be a proof of non-descent.  **It does not happen here**
(`analysis/wk13_b04_pole.py`, `results/b13_04/pole_sweep_r3_d7.json`): at
fifteen random specialisations the witness has `ord₀P = 15` or `18` against the
threshold `2δ = 14`, the same profile as the genuine `ρ(h)` (15 to 17).
**MEASURED**, therefore, and not proved: the witness appears to lift to a
regular function on `V* × Sym³V*` that is constant on the fibres of the
multiplication map, i.e. to lie in the seminormalisation of `R` and not in `R`
itself — which would say `R₃ = {ℓ·c} ⊆ Sym⁴C³` is **not seminormal** in this
graded piece.  Proving it needs the divisibility `s^{2δ} | P` with `(a, c)`
symbolic rather than specialised: 2 + 10 further indeterminates on top of the
ten already handled, a bounded but not free expansion, and the single most
valuable follow-up here.  If it holds, the descent criterion is *strictly*
finer than seminormality and no fibre-type condition will ever be enough.

*What Theorem H does not say.*  It does not weaken §5: the swap identity
remains an exact, two-evaluation **necessary** test, and it remains sufficient
wherever `dim T^λ = mult_R` is computed — which is 432 of 433 cells, including
every cell of every model in this report.  As a screen it is used the same way
either direction: a violation certifies non-descent; equality of dimensions
certifies the cell.

### 12.4 The enlarged transfer census (Q8)

`analysis/wk13_b04_model.py`, all cells exact over `Q` with certified cubic
ideals as in §4:

| model | `f`, `r` | `δ` | cells | pairs `(ν,λ)`, `i⁽³⁾ ≥ 1` | contribute alone | cells with gap | total gap | gap above Cor. D's floor |
|---|---|---|---|---|---|---|---|---|
| A | `x³`, 2 | 2 | 3 | 2 | 1 | 1 | 1 | 0 |
| B | `x³+y³`, 3 | 3 | 9 | 5 | 1 | 1 | 1 | 0 |
| B | | 4 | 18 | 28 | 0 | 1 | 1 | 0 |
| B | | 5 | 34 | 115 | 2 | 10 | 14 | 5 |
| B | | 6 | 49 | 318 | 1 | 29 | 53 | 17 |
| C | `xyz`, 3 | 4 | 18 | 6 | 0 | 0 | 0 | 0 |
| D | `x³`, 4 | 2 | 3 | 2 | 1 | 1 | 1 | 0 |
| D | | 3 | 9 | 15 | 2 | 6 | 6 | 0 |
| D | | 4 | 28 | 95 | 3 | 25 | 29 | 0 |
| E | `x³+y³`, 4 | 4 | 28 | 60 | 2 | 11 | 11 | 0 |
| **total** | | | **199** | **646** | **13** | **85** | **117** | **22** |

Every consistency check of §4 held in all 199 cells: `mult_R` by `ρ` equals
`mult_R` by reducible points; `mult_P` by padded points equals `mult_P` by
fixed-factor points; the criterion equals the direct gap; the criterion equals
`dim(ρ(H_λ) ∩ span of branching vectors)`.  **13 of 646** Pieri-compatible
constituent/cell pairs contribute on their own — 2 % — which is the quantitative
form of §4's headline, now on five cubics, two lengths and five degrees.  The
22 cells whose gap exceeds Corollary D's dimension floor (all at `δ ≥ 5`) are
the cells where the exact criterion is doing work no count can do.

### 12.5 The length quantifier, demonstrated (Q7)

Model D (`r = 4`, `f = x₁³`) at `δ = 4` is the first model in this report with
quartic weights of full length 4, so a predecessor may have `μ₄ = 0` (length 3)
or `μ₄ > 0` (length 4) in the same cell.  Both occur, and the shorter ones are
not idle:

- `λ = (7,7,1,1)`: `a⁽⁴⁾ = 1`, `mult_R = 1`, gap **1**.  Its length-4
  predecessors carry `Σ a⁽³⁾ = 0`; the **only** channel is the length-3
  predecessor `ν = (7,4,1)` (i.e. `(7,4,1,0)`), which has `i⁽³⁾ = 1` and
  **contributes** (`branch_in_W = True`).  The additional padded equation at a
  full-length weight comes entirely from a *shorter* predecessor.
- `λ = (4,4,4,4)`: same shape, over the length-3 predecessor `(4,4,4,0)`.
- Twenty-three further (cell, shorter-predecessor) pairs at `r = 4, δ = 4` have
  `i⁽³⁾ ≥ 1`; twenty-one of them do not contribute alone, so the shorter
  predecessors behave exactly like the full-length ones — live, and mostly
  non-descending.

This is the operational content of §7: a shorter `μ` pairs with `λ` and may be
ignored **only** when its length-`k` value of `i⁽³⁾` is already known — for
`k ≤ 5` by Theorem 2, and otherwise not at all.  At `λ₁₃` the five length-8
predecessors sit at `k = 8 > 5` and are as live as the ten length-9 ones, which
`(7,7,1,1)` shows is not a formality.

### 12.6 Q9, the independent `a`-check

Every `a⁽⁴⁾` and `a⁽³⁾` used anywhere in §12 — one per cell and per cubic shape,
in every model and every sweep — was checked, as an assertion inside the run,
against the Kostant alternation of `analysis/wk13_b04_pred13.kostant` (a
different formula on a different data structure from the highest-weight
kernel).  **No disagreement**, in any cell; a disagreement would have halted
the run.  The same routine is the one that reproduced the fifteen predecessors'
`a`-values in §6.

### 12.7 What §12 adds to the prices of §8

The swap identity's real value at the goal cell is unchanged by Theorem H, and
is worth stating as a price.  Suppose a session obtains a candidate cubic-ideal
highest-weight vector `g` at one of the fifteen predecessors of `λ₁₃` (B13-01's
route, or the screen of §8).  Deciding whether that constituent contributes at
`λ₁₃` — the question §4 shows is *not* answered by Pieri compatibility — then
costs **two evaluations of a degree-13 polynomial per test point** on the
branching vector `g^{↓λ₁₃}`, against the alternative of building the 39-row
quartic system at a weight space of `8.09·10⁸` monomials.  A single violation
certifies non-contribution outright.  What Theorem H removes is the hope of
*certifying contribution* the same cheap way: for that, the exact intersection
of §3 is still required.

`r = 6, δ = 4` and `r = 5, δ = 5` were mid-run at the deadline; each is minutes
of work and is the obvious first thing to finish.  A symbolic proof of the
`(POLE)` divisibility for the §12.3 witness is the one open item this session
would take next.

## 13. Ledger

| claim | label |
|---|---|
| Theorem A: `I(P)_δ/I(R)_δ ≅ W_δ ∩ (Sym^δV ⊗ J_δ)`; gap = dim of the intersection | PROVED (the identity of S4's factorization, identified with Prop. 8) |
| Lemma B: fixed-factor restriction; `h ∈ I(R) ⟺ ρ(h) = 0`, `h ∈ I(P) ⟺ ρ(h) ∈ J`; support form; `mult_R = 0` for `λ₁ < δ` | PROVED (kernel half is S4's lemma) |
| Proposition C: `ρ(H_λ) ⊆ ⊕_ν B^λ_ν`, `dim B^λ_ν = a⁽³⁾(ν,δ)`, branching vectors | PROVED |
| Corollary D: the two-sided bound; conditions S1, S2; forced gaps | PROVED |
| Theorem E: the converse of Prop. 8(2) fails at `((6,2), 2)` over `(4,2)` for `f = x³` | PROVED, machine-confirmed |
| Lemma F: the swap identity | PROVED |
| 82 model cells: all ranks, ideals, gaps, witnesses | CERTIFIED over `Q` (ideal membership by symbolic identity; ranks exact) |
| `(8,8,8)₆`, `r = 3`: `mult_R = 1`, `i_R = 1`, the reducible equation with 377 monomials none `x₁`-pure, `h(ℓ·c) ≡ 0` symbolically | CERTIFIED (exploratory) |
| in the 30 pre-registered cells the gap equals Cor. D's lower bound; at `δ = 5` five cells exceed it | CERTIFIED (exact facts about the models), exploratory at `δ = 5` |
| the swap identity detected all 152 non-descents | MEASURED (a property of the search, not a theorem) |
| fifteen predecessors of `λ₁₃`, `a`, `N_S`, `Σ a⁽³⁾ = 73`, `a⁽⁴⁾ = 39` | re-derived, agree with the audit log (CERTIFIED as exact counts; the audit log RECORDED) |
| `dim(weight (8,17,2⁷)) = 809,527,307`; `N_S(λ₁₃) = 80,921,422,068` in `Q₁₃` | CERTIFIED (tail DP) |
| `mult_R(λ₁₃,13) = 36` | ADOPTED from `docs/rung13_reducible.md`: `≥ 36` certified, `= 36` measured |
| Theorem 2 (`k ≤ 5`), the restriction lemma, Prop. 8 | ADOPTED (`docs/washout_lemma.md`, `docs/transfer_lemma.md`) |
| nothing about `I(D₉^{per₃})₁₃` itself | not computed; priced in §8 |
| **Addendum 1** | |
| one-sidedness: a computed `dim T = mult_R` certifies `T = ρ(H_λ)` | PROVED |
| 432 of 433 cells over 23 `(r,δ)` pairs: the swap identity cuts `B_full` to exactly `ρ(H_λ)` | CERTIFIED |
| Theorem H: the swap identity, and the full two-factor condition, are **not sufficient** — the `(16,6,6)`, `δ = 7` witness | PROVED (two symbolic identities over `Z` + an exact rank over `Q`) |
| the witness has no boundary pole at fifteen specialisations, so it appears to lie in the seminormalisation of `R` and not in `R` | MEASURED (specialisation is one-sided the wrong way); the symbolic divisibility is priced in §12.3 |
| 199 model transfer cells; 13 of 646 Pieri-compatible pairs contribute alone; 22 gaps above Cor. D's floor | CERTIFIED over `Q` |
| the length quantifier demonstrated at `λ = (7,7,1,1)`: the only contributing channel is a shorter predecessor | CERTIFIED |
| every `a⁽⁴⁾`, `a⁽³⁾` in §12 agrees with the Kostant alternation | CERTIFIED (in-run assertion) |

Author of record for this session: B13-04 (Claude Fable 5.1), for Swami
Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
board_numbering: batch13
