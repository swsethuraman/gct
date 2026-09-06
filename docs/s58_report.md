# Session 58 — symmetric rectangular Kronecker coefficients at scale

Branch `s58-sk` off `main` at `0960bd5` (= `work/main` on the laptop and
`origin/main` at session start; ancestor test trivial).  Pre-registration
`results/PREREG_s58.md`, committed before any computation.  Code
`analysis/wk9_s58_sk.py` (+ `analysis/wk9_s58_chars.c`, a C pass for the
character blocks; the Python pass is the reference and both run on every
sample).  Calibration `results/s58_calibration.md`; every computed value in
`results/s58_calibration.jsonl`, `results/s58_longweight_all.jsonl.gz`,
`results/s58_costcurve.json`, `results/s58_engine_curve.json`,
`results/s58_target.json`, `results/s58_sumrule_{20,24,28}.json`; logs
`results/logs/s58_*`.  Nothing pushed; delivered as `s58_sk.bundle`.

## Verdict

> **`sk((65,17,2⁷), 24⁴) = 48 825`**, with `g((65,17,2⁷), 24⁴, 24⁴) = 92 000`
> and Adams part `A = 5 650` (so the antisymmetric coefficient is `43 175`).
> Computed in **0.4 s** (10.6 s including a one-off table shared by every cell
> at `δ = 24`), by four internal routes that agree, from an algorithm calibrated
> with **zero disagreements** against every banked value the brief lists, the
> 2585-cell length-5 screen, the s39 C engine on the goal cell's own family
> through `N = 64`, and brute force at every partition of `N = 20, 24, 28`.
>
> Under the Foulkes formulation, `Θ⁺ : C²⁷⁴ → C⁴⁸ ⁸²⁵`.  **The LMR cell is a
> well-posed finite linear-algebra problem for the first time**: the
> multiplicity `mult_det` is the rank of a `274 × 48 825` map, and `48 825` sits
> inside the size range the programme has already handled at other cells
> (`n_χ` up to 65 778 in s52).
>
> The algorithm is the brief's §3 "length" analogue made precise: `N` drops out
> of the cost altogether.  `sk(λ, 4×δ)` is an alternating sum over the vertical
> strips of the **tail** `λ̄ = (λ₂, λ₃, …)` of class sums over `S_m`, `m ≤ |λ̄|`,
> in which the rectangle enters only through the box condition `β₁ ≤ δ`.  At
> the goal cell the class sums are over `S₂₃ … S₃₁` (53 829 terms in all, against
> `p(96) = 118 114 304` for the partition sum), and the coefficient is **already
> constant in `δ`**: `48 825` at every `δ = 23 … 32`, provably for all
> `δ ≥ 31`, and by the Kronecker support bound for all `δ ≥ 24` — the LMR cell
> sits exactly at the stability threshold `λ₁ = |λ̄| + 2λ₂` (`65 = 31 + 34`).

**Direct, not extrapolated — the integrator's question (§0).**  `48 825` is
computed *at* `δ = 24`.  The reduction is an identity of symmetric functions,
valid at every `(λ, δ, n)`; the box condition `β₁ ≤ δ` is part of the exact
computation at that `δ`, and **no stability hypothesis enters anywhere**.  The
constancy in `δ` reported below was *observed* from separate direct
computations at each `δ`, and the direct partition sum of the s39 C engine
reproduces the reduction's *pre-stable* values (`2714 … 41463` at `N = 48 … 64`,
where the box condition actively cuts) as well as **nineteen cells of the
boundary family `(3k+2m, k, 2^m)` at `δ = k+m`** on which the LMR cell sits at
exact equality `2δ = |ρ| + ρ₁` (§3b).  The external audit's Manivel-route value
(`B_ρ = 92 000`, `T_ρ = 5 650`, `sk = 48 825`, communicated by the integrator)
is therefore confirmed by a route that does not use stability at all.

The pre-registered predictions: P1 (`sk ≥ 274`) **confirmed**, `48 825`; P2
(`10³ ≤ sk ≤ 10⁶`) **confirmed**; P3 (flat cost in `N` at fixed tail)
**confirmed**, 0.37–0.41 s at every `N` from 48 to 96; P5 (constant from
`δ = 24` to `32`) **confirmed**, and constancy begins one step earlier, at
`δ = 23`.  Deliverable 3 (session 57's `pending` column) was **dropped by the
integrator mid-session** — sessions 56 and 57 have not been run — and replaced
by a rule for which cells the method makes newly affordable: §6.

## 0. The integrator's question, answered in its own terms

*Is `48 825` a direct computation at `δ = 24`, or an extrapolation from the
stable range?*  **Direct.**  The theorem of §1 is an identity in the ring of
symmetric functions — Jacobi–Trudi along the first row of `s_λ`, then
Frobenius reciprocity for the rectangle — so it computes `sk(λ, 24⁴)` at
`δ = 24` itself, with the cost driven by the tail; the rectangle enters the
exact formula only through the box `β₁ ≤ 24`, which the code enforces at that
`δ` and at no other.  Nothing in the derivation, the code path, or the
calibration uses Manivel's or any other stabilisation; the statements
"constant for `δ = 23 … 32`" (measured, each `δ` computed on its own) and
"constant for `δ ≥ 31`" (the box condition is vacuous once `δ ≥ |λ̄|`, a
one-line corollary) are *consequences* read off the direct values, not inputs.
Two facts make this checkable rather than asserted: (i) below the boundary the
reduction returns values that are *not* the limit (`2714, 15383, 26654,
35340, 41463` at `δ = 12 … 16` on the LMR family), and the s39 C engine — a
direct `p(N)` character sum — returns the same five numbers; (ii) the whole
boundary family `(3k+2m, k, 2^m)`, `δ = k+m`, on which `2δ = |ρ| + ρ₁` holds
with equality exactly as at the LMR cell, is reproduced by direct sums at
nineteen members through `N = 64` (§3b).  So the boundary concern does not
touch this route, and the value independently validates the external audit's
use of Manivel's stability at equality.

## 1. The reduction

Notation: `μ = (δⁿ)`, `N = nδ`, `λ ⊢ N`, tail `λ̄ = (λ₂, λ₃, …)`, `m = |λ̄|`;
`g(α,β,γ) = ⟨χ^α, χ^β χ^γ⟩`; `A(α,β) = ⟨χ^α, ψ²χ^β⟩` with `ψ²χ(σ) = χ(σ²)`.
The house quantity (`scripts/ambient_screen.m_det`, `wk9_s38_screen.py`,
`wk9_s39_chars.c`) is

    sk(λ, n×δ) = ⟨χ^λ, Sym² χ^μ⟩ = ( g(λ,μ,μ) + A(λ,μ) ) / 2 ,

the multiplicity of `S_λ(C^{n²})^*` in degree `δ` of the coordinate ring of the
`GL_{n²}`-orbit of `det_n`.

**Lemma 1.**  For `k + m = N` and `τ ⊢ m`,

    ⟨ h_k s_τ , s_μ ∗ s_μ ⟩ = Σ_{α ⊢ k, α ⊂ μ} g(τ, α^∨, α^∨),
    ⟨ h_k s_τ , ψ²χ^μ ⟩     = Σ_{α ⊢ k, α ⊂ μ} A(τ, α^∨),

`α^∨ ⊢ m` the complement of `α` in the rectangle.  *Proof.*  Frobenius
reciprocity, `Res χ^μ = Σ c^μ_{αβ} χ^α ⊠ χ^β` with `c^μ_{αβ} = [β = α^∨]` for a
rectangle, `⟨1, χ^α χ^{α'}⟩ = δ_{αα'}`, and — for the Adams part —
`(σ₁σ₂)² = σ₁²σ₂²` together with `⟨1, ψ²χ^α⟩ = 1` (the Frobenius–Schur
indicator of every irreducible character of a symmetric group).  ∎

**Lemma 2 (Jacobi–Trudi along the first row).**
`s_λ = Σ_{j≥0} (−1)^j h_{λ₁+j} s_{λ̄/(1^j)}`, and `s_{λ̄/(1^j)} = Σ_τ s_τ` over
the `τ ⊂ λ̄` with `λ̄/τ` a vertical strip of `j` boxes.

**Theorem.**  With `B_m(δ,n) = {β ⊢ m : ℓ(β) ≤ n, β₁ ≤ δ}`,

    g(λ,μ,μ) = Σ_j (−1)^j Σ_{τ ∈ V_j(λ̄)} Σ_{β ∈ B_{|τ|}} g(τ,β,β),
    A(λ,μ)   = Σ_j (−1)^j Σ_{τ ∈ V_j(λ̄)} Σ_{β ∈ B_{|τ|}} A(τ,β),

and `sk = (g + A)/2`.  The inner quantities are class sums over `S_{|τ|}`.

**Corollary (stability in the tail).**  For fixed `λ̄` and `n`,
`sk((N−m, λ̄), n×(N/n))` is constant for `δ ≥ m` (the box condition is then
vacuous).  Sharper: a term with `β₁ > δ` can only contribute if
`g(τ,β,β) ≠ 0` (note `|A(τ,β)| ≤ g(τ,β,β)`, both being sums and differences
of the `Sym²` and `Λ²` multiplicities), and the Kronecker depth bound
`|τ| − τ₁ ≤ 2(|τ| − β₁)` (Clausen–Meier, Dvir 1993: a constituent of
`χ^β χ^β` has depth at most twice the depth of `β`; re-checked here on every
pair `(τ, β)` of partitions of `N ≤ 9`) then forces `β₁ ≤ (|τ| + τ₁)/2`; so the coefficient
is constant for `δ ≥ (m + λ₂)/2`, i.e. for `λ₁ ≥ m + 2λ₂`.  At the goal cell
`65 = 31 + 2·17` exactly.  (Stabilisation of rectangular Kronecker
coefficients as the rectangle grows is Manivel's, arXiv:0907.3351,
J. Algebraic Combin. 33 (2011); here it falls out of the reduction together
with the computation.)

**What the "length" analogue is.**  For the plethysm `a`, the variable count
drops from 16 to `ℓ(λ) = 9`.  For `sk` there is no such drop: the object is
`S_λ(C⁴ ⊗ C⁴)^{SL₄×SL₄⋊Z₂}`, and the rectangle needs four rows on each side, so
16 variables is already minimal.  The right analogue is the theorem: the
symmetric-group size `N = 96` is replaced by the tail size `31`, and the
variable count never enters.

**The brief's four approaches, assessed.**  (1) *Restricting the `ρ`-sum to
`χ^λ(ρ) ≠ 0`*: the support of `χ^{(65,17,2⁷)}` is not sparse (every `ρ` that
can be peeled from a shape with a 65-box first row and a 31-box tail
contributes, and `(1^{96})` is among them), and each surviving term still
costs a Murnaghan–Nakayama evaluation in `S₉₆`; the s38 batched route already
does this restriction on the rectangle side (its `W`-support is `p(N)` minus a
few per cent).  No.  (2) *Jacobi–Trudi on the rectangle*:
`s_{(δ⁴)} = Σ_{w∈S₄} sgn(w) h_{δ+ρ−wρ}` gives `g = Σ_w sgn(w) ⟨s_λ ∗ s_μ, h_α⟩`
and `⟨s_λ ∗ s_μ, h_α⟩ = Σ c^λ_{ν¹…ν⁴} c^μ_{ν¹…ν⁴}` over quadruples of
partitions of the four parts of `α` — a sum over `~10⁸` quadruples with 9-row
multi-LR coefficients.  Correct, but not better.  (3) *A dynamic program over
the tail*: this is the reduction — the Jacobi–Trudi expansion along
**`λ`'s** first row, not the rectangle's, is what makes the rectangle's
restriction trivial (`c^μ_{αβ} = [β = α^∨]`) and puts the whole cost on the
tail.  (4) *Published algorithms*: nothing specific to 4-row rectangles is
known to me beyond Manivel's stability (cited above) and the two-row /
hook formulas (Rosas; Blasiak), which do not apply at a 4-row rectangle; the
reduction recovers the stability and adds the finite computation below the
stable range.

Hand checks recorded in the pre-registration (`λ = (N)`, `(N−1,1)`, `(2,2)`)
all pass; the algorithm reproduces the `n = 3` anchors of the s39 self-test
(`(sum, support)` of `m_det` over `λ ⊢ 3δ, ℓ ≤ 9`: `(3,3), (11,10), (43,34)`)
and the s28 `n = 3` zeros.

## 2. The implementation

`analysis/wk9_s58_sk.py`, one file, four routes:

1. **the reduction** (default): the terms `(j, τ)` from the vertical strips of
   the tail (enumerated per run of equal rows, polynomially); for each tail
   size `m`, the **box weights** `w_g(ρ) = Σ_{β∈B_m} χ^β(ρ)²`,
   `w_A(ρ) = Σ_β χ^β(ρ²)` — the house `W(ρ)` idea moved from `S_N` down to
   `S_m`, computed once per `(m, δ)` and shared by every cell — and one
   `τ`-side character pass paired with them.  Characters by a single
   depth-first pass over the trie of partitions of `m` with parts ascending,
   carrying the vector of signed Murnaghan–Nakayama path counts on bead masks,
   pruned to the sub-partitions of the tail (τ side) or to the box (β side),
   so a whole block of rows comes out of one pass;
2. **the Pieri organisation**: `⟨s_γ,F⟩ = ⟨h_{γ₁}s_{γ̄},F⟩ − Σ_{γ'≠γ}⟨s_{γ'},F⟩`
   over the other terms of `h_{γ₁} s_{γ̄}`, recursing on the tail — the same
   inner sums combined differently;
3. **per-β**: every `g(τ,β,β)` and `A(τ,β)` separately, as `fmpz_mat` products;
4. **brute force**: the definition, the sum over all `ρ ⊢ N`, with its own
   memoised strip-removal Murnaghan–Nakayama.

The C pass (`wk9_s58_chars.c`, `__int128`, output as two 64-bit words) and
the Python pass are compared on every calibration sample and at the goal
cell; the C pass is used only where every bead mask fits in 63 bits.  Every
division by `m!` is asserted exact; the parity `g ≡ A (mod 2)` and
`0 ≤ (g ± A)/2` are asserted at every cell.  Exact integers throughout; no
prime is used anywhere.

## 3. Calibration — zero disagreements

`results/s58_calibration.md` is the generated table; the sets:

| set | cells | disagreements |
|---|---|---|
| the brief's table (`8,8,8,13,78,30,5`) | 7 | 0 |
| s39 C-engine timing-log cells (`N` up to 48, incl. `4988, 14123, 2254`) | 9 | 0 |
| `n = 3` anchors `(3,3),(11,10),(43,34)` and the three s28 zeros | 6 | 0 |
| **the length-5 screen, every cell, δ = 5–10** | **2585** | **0** |
| the other three routes on 53 sampled cells | 53 | 0 |
| brute force (the definition) on random cells of every length 1–16, `N = 20, 24, 28`; house `m_det` where affordable | 138 | 0 |
| `λ` with more than 16 rows vanish without the shortcut | 4 | 0 |
| sum rules `Σ_λ f^λ sk = f^μ(f^μ+1)/2`, `Σ_λ f^λ g = (f^μ)²` over **every** `λ ⊢ N` | `N = 20, 24, 28` (627, 1575, 3718 partitions) | 0 |
| brute force at **every** `λ ⊢ N` | `N = 20, 24` | 0 |
| s39 C engine on the goal cell's family `(N−31,17,2⁷)`, `N = 48 … 64` | 5 | 0 |
| **the boundary family `(3k+2m, k, 2^m)`, `δ = k+m`, `N = 12 … 64` (§3a)** | **19** | **0** |
| **the long-weight screen (s39), lengths 6–10, δ = 8–12, `N` up to 48** | see §3b | see §3b |

The s39 engine values on the goal family are worth writing down, since they
are the only independent computation on that family: `2714, 15383, 26654,
35340, 41463` at `N = 48, 52, 56, 60, 64`, all reproduced.

### 3a. The boundary family — where the LMR cell sits at equality

The integrator's note (mid-session) points out that the LMR cell lies at exact
equality on the improved stability boundary, `2δ = 48 = |ρ| + ρ₁ = 31 + 17`,
while every calibration cell above sits in the interior, and asks for the
family

    λ = (3k + 2m, k, 2^m),   δ = k + m,   ρ = (k, 2^m):   2δ = |ρ| + ρ₁ exactly,

of which LMR is `k = 17, m = 7`.  Its nine values (direct `p(4δ)` character
sums, no stability anywhere) are reproduced, and ten larger members through
`N = 64` are reproduced by this session's own brute force, the house Python
`m_det`, and the s39 C engine — every one of them a direct sum
(`results/s58_boundary.json`, `analysis/wk9_s58_boundary.py`; "`g / sk`" in
the comparison columns):

| `k` | `m` | `δ` | `N` | `λ` | `g` | `A` | `sk` | `ak` | integrator (direct `p(4δ)` sum) | brute force (own MN) | house `m_det` | s39 C engine (direct) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 1 | 3 | 12 | `(8,2,2)` | 2 | 2 | **2** | 0 | 2 / 2 ✓ | 2 / 2 ✓ | 2 ✓ | — |
| 3 | 1 | 4 | 16 | `(11,3,2)` | 2 | 2 | **2** | 0 | 2 / 2 ✓ | 2 / 2 ✓ | 2 ✓ | — |
| 2 | 2 | 4 | 16 | `(10,2,2,2)` | 5 | 5 | **5** | 0 | 5 / 5 ✓ | 5 / 5 ✓ | 5 ✓ | — |
| 3 | 2 | 5 | 20 | `(13,3,2,2)` | 6 | 6 | **6** | 0 | 6 / 6 ✓ | 6 / 6 ✓ | 6 ✓ | — |
| 4 | 2 | 6 | 24 | `(16,4,2,2)` | 20 | 16 | **18** | 2 | 20 / 18 ✓ | 20 / 18 ✓ | 18 ✓ | — |
| 4 | 3 | 7 | 28 | `(18,4,2,2,2)` | 61 | 33 | **47** | 14 | 61 / 47 ✓ | 61 / 47 ✓ | 47 ✓ | — |
| 5 | 3 | 8 | 32 | `(21,5,2,2,2)` | 110 | 44 | **77** | 33 | 110 / 77 ✓ | 110 / 77 ✓ | 77 ✓ | — |
| 5 | 4 | 9 | 36 | `(23,5,2,2,2,2)` | 311 | 83 | **197** | 114 | 311 / 197 ✓ | 311 / 197 ✓ | 197 ✓ | — |
| 6 | 4 | 10 | 40 | `(26,6,2,2,2,2)` | 657 | 163 | **410** | 247 | 657 / 410 ✓ | 657 / 410 ✓ | 410 ✓ | — |
| 7 | 4 | 11 | 44 | `(29,7,2,2,2,2)` | 1073 | 207 | **640** | 433 | — | — | — | 640 ✓ |
| 8 | 4 | 12 | 48 | `(32,8,2,2,2,2)` | 1759 | 333 | **1046** | 713 | — | — | — | 1046 ✓ |
| 7 | 5 | 12 | 48 | `(31,7,2,2,2,2,2)` | 2436 | 348 | **1392** | 1044 | — | — | — | 1392 ✓ |
| 9 | 5 | 14 | 56 | `(37,9,2,2,2,2,2)` | 6069 | 703 | **3386** | 2683 | — | — | — | 3386 ✓ |
| 8 | 6 | 14 | 56 | `(36,8,2,2,2,2,2,2)` | 6609 | 687 | **3648** | 2961 | — | — | — | 3648 ✓ |
| 10 | 6 | 16 | 64 | `(42,10,2,2,2,2,2,2)` | 14853 | 1249 | **8051** | 6802 | — | — | — | 8051 ✓ |
| 11 | 5 | 16 | 64 | `(43,11,2,2,2,2,2)` | 11826 | 1210 | **6518** | 5308 | — | — | — | 6518 ✓ |
| 12 | 4 | 16 | 64 | `(44,12,2,2,2,2)` | 6046 | 890 | **3468** | 2578 | — | — | — | 3468 ✓ |
| 9 | 7 | 16 | 64 | `(41,9,2,2,2,2,2,2,2)` | 11550 | 1012 | **6281** | 5269 | — | — | — | 6281 ✓ |
| 13 | 3 | 16 | 64 | `(45,13,2,2,2)` | 1815 | 473 | **1144** | 671 | — | — | — | 1144 ✓ |

**Nineteen boundary cells, zero disagreements.**  The reduction computes each
directly at its own `δ`; the agreement with four direct routes on the very
boundary where the LMR cell sits is the test the note asked for, and it
passes.  The `β₁`-breakdown of the goal cell (§5) adds the mechanism: at
`δ = 24` the terms the boundary is about — those with `β₁ = 24` — are all
zero, and the value is already attained at `δ = 23`.

### 3b. The long-weight screen

LONGWEIGHT_PLACEHOLDER

## 4. The cost curve

**(i) Fixed tail `(17, 2⁷)`, `λ = (N−31, 17, 2⁷)`, `δ = N/4`** — the goal
cell's own family.  "Warm" is the reduction with the box weights cached (they
are keyed by `(|τ|, δ)`, so any cell at the same `δ` whose tail sizes overlap
shares them); "cold" rebuilds them.  Inner class-sum terms: 53 829 at every `N`.

| δ | N | `sk` | `g` | `A` | cold | warm | #β | s39 C engine: build + cell | engine memo |
|---|---|---|---|---|---|---|---|---|---|
| 12 | 48 | 2 714 | 5 241 | 187 | 3.9 s | 0.39 s | 691 | 2.8 s + 0.54 s | 1.3 M |
| 13 | 52 | 15 383 | 29 326 | 1 440 | 4.8 s | 0.40 s | 890 | 6.1 s + 1.16 s | 2.6 M |
| 14 | 56 | 26 654 | 50 660 | 2 648 | 5.6 s | 0.39 s | 1 079 | 12.2 s + 2.53 s | 4.7 M |
| 15 | 60 | 35 340 | 67 035 | 3 645 | 6.4 s | 0.40 s | 1 251 | 26.0 s + 4.68 s | 8.3 M |
| 16 | 64 | 41 463 | 78 520 | 4 406 | 7.0 s | 0.37 s | 1 402 | 50.9 s + 9.13 s | 14.2 M |
| 17 | 68 | 45 366 | 85 782 | 4 950 | 8.0 s | 0.40 s | 1 533 | beyond `NMAX = 64` | — |
| 18 | 72 | 47 488 | 89 672 | 5 304 | 8.6 s | 0.40 s | 1 645 | | |
| 19 | 76 | 48 435 | 91 362 | 5 508 | 8.8 s | 0.40 s | 1 740 | | |
| 20 | 80 | 48 744 | 91 883 | 5 605 | 9.4 s | 0.39 s | 1 819 | | |
| 21 | 84 | 48 815 | 91 989 | 5 641 | 9.8 s | 0.41 s | 1 884 | | |
| 22 | 88 | 48 824 | 91 999 | 5 649 | 10.0 s | 0.37 s | 1 936 | | |
| 23 | 92 | 48 825 | 92 000 | 5 650 | 10.3 s | 0.39 s | 1 977 | | |
| **24** | **96** | **48 825** | **92 000** | **5 650** | 10.6 s | 0.40 s | 2 008 | | |

The warm time is flat to within 10 % from `N = 48` to `N = 96` (P3); the cold
time grows only with the number of `β` in the box, and is paid once per `δ`.
The s39 engine — the fastest house route, C with a memo — doubles per step of
four in `N` (build ×2.0, cell ×1.9, memo ×1.7 per step) and stops at
`NMAX = 64` with 64-bit beads.

**(ii) Growing tail at `δ = 10`** (`N = 40`, `λ = (40−m, tail)`):

| `m` | `λ` | `sk` | cold | warm | terms | inner ops |
|---|---|---|---|---|---|---|
| 4 | (36,2,2) | 2 | 0.00 s | 0.00 s | 3 | 10 |
| 8 | (32,2,2,2,2) | 8 | 0.00 s | 0.00 s | 5 | 60 |
| 12 | (28,4,4,2,2) | 175 | 0.01 s | 0.00 s | 9 | 397 |
| 16 | (24,8,4,2,2) | 3 850 | 0.06 s | 0.01 s | 12 | 1 679 |
| 20 | (20,8,4,2,2,2,2) | 43 521 | 0.23 s | 0.04 s | 20 | 6 412 |
| 24 | (16,10,6,4,2,2) | 1 272 250 | 0.53 s | 0.11 s | 24 | 22 151 |
| 28 | (12,12,8,4,2,2) | 591 245 | 1.09 s | 0.29 s | 24 | 54 071 |

and, from the long-weight screen, the hardest tails there — `(4⁹)` at
`δ = 12`, `m = 36`, `ℓ = 10` — take 1.3 s warm / 8.4 s cold.  The cost is
`Σ_τ p(|τ|) × (states)` with the states the sub-partitions of the tail: it is
the tail's size and, second, its number of rows that matter.

**(iii) The partition-sum routes**, measured:

| route | N = 20 | 24 | 28 | 32 | 36 | 40 | growth per +4 |
|---|---|---|---|---|---|---|---|
| house Python `m_det`, peaked cell `(N−8,2⁴)` | 0.04 s | 0.12 s | 0.29 s | 0.70 s | 1.6 s | 3.7 s | ×2.3 (memo ×2.1: 397 K entries at 40) |

and the s39 engine as in (i).

**The cost of the partition sum at `N = 96`, in numbers.**  `p(96) =
118 114 304` classes, each needing three characters of `S₉₆`.  Extrapolating
the measured growth (8 steps of four from `N = 64`): the s39 engine would need
about `51 s × 2.0⁸ ≈ 3.6 h` to build its rectangle weights, `9 s × 1.9⁸ ≈ 1.5 h`
for the cell, and a memo of `14 M × 1.7⁸ ≈ 10⁹` entries (tens of GB) beside
the `1.2 × 10⁸`-entry weight table — after an engine rewrite (`NMAX`, bead
width).  The house Python route extrapolates to `3.7 s × 2.3¹⁴ ≈ 5 × 10⁵ s`
for a *peaked* cell with a memo of `4 × 10⁵ × 2.1¹⁴ ≈ 10¹¹` entries, i.e.
terabytes.  Neither fits the 7 GB container; the memory, not the time, is the
wall.  The reduction does the same cell in `0.4 s` with `53 829` class-sum
terms over `S₂₃ … S₃₁` and a few MB.

## 5. The goal cell (`results/s58_target.json`, `results/logs/s58_target.log`)

    λ = (65,17,2⁷), δ = 24, N = 96, ℓ(λ) = 9, |λ̄| = 31
    g((65,17,2⁷), 24⁴, 24⁴) = 92 000
    A((65,17,2⁷), 24⁴)      =  5 650
    sk = (g + A)/2          = 48 825        ak = (g − A)/2 = 43 175

Terms: `j = 0 … 8`, 16 tails `τ = (17−a, 2^{7−b}, 1^b)`, sizes 23–31;
box `B_m(24, 4)`; four routes, all `48 825`: reduction 11.7 s cold, Pieri 2.1 s
(cached), per-β `fmpz_mat` 17.7 s, pure-Python pass 35.4 s.  The stability
probe `(N−31, 17, 2⁷)`, `δ = 20 … 32`:

| δ | 20 | 21 | 22 | 23 | 24 | 25 … 32 |
|---|---|---|---|---|---|---|
| `sk` | 48 744 | 48 815 | 48 824 | **48 825** | **48 825** | 48 825 |
| `g` | 91 883 | 91 989 | 91 999 | 92 000 | 92 000 | 92 000 |
| `A` | 5 605 | 5 641 | 5 649 | 5 650 | 5 650 | 5 650 |

So `48 825` is the **limit value** of the whole family `(4δ−31, 17, 2⁷)`, and
the LMR cell is the first cell at which the depth bound guarantees it.  The
breakdown of the goal value by `β₁` (`results/s58_target_by_beta1.json`, the
per-β route): the box condition removes nothing at `δ = 24` — **no inner
value `g(τ,β,β)` or `A(τ,β)` with `β₁ = 24` is non-zero**, the equality case
of the depth bound being empty here — and `β₁ = 23` contributes exactly `1`
to `g` and `1` to `A`, which is the whole difference between `δ = 22`
(`48 824`) and `δ ≥ 23`.  The bulk sits at `β₁ = 12 … 16` (`g`-parts
`16 896, 24 085, 21 334, 16 375, 11 485`), i.e. at balanced `β`; the
`β₁ ≤ 11` contributions are negative, an artefact of the alternating sum.

**What it means for the LMR block.**  `a = 274` (s50 integrator) is the source
dimension; `48 825` is the target.  `mult_det = rank Θ⁺ ≤ 274`, and s50/s55
give `i_det = a − mult_det ≥ 1` there (the LMR equation lives in this
isotypic).  The computation the programme now faces is exact rank of a
`274 × 48 825` integer (or two-prime) matrix, once s56's `Θ⁺` is materialised —
comparable in size to the largest cells already measured (`n_χ = 65 778`,
s52), and far below the cells the census estimates at `10⁵–10⁶`.  Whether the
274 ambient vectors restricted to the orbit stay independent is exactly the
question; nothing here prejudges it.

## 6. Which cells the method makes newly affordable — the rule (in place of deliverable 3)

Deliverable 3 was dropped by the integrator: sessions 56 and 57 have not been
run, and their table is not to be reconstructed here.  What whoever runs s57
can apply directly is the cost as a function of the tail (`results/s58_reach.json`,
`analysis/wk9_s58_reach.py`; "cold" includes the box weights for that `δ`,
which every cell at that `δ` then shares; measured with two other runs on the
two cores, so upper bounds):

| tail size `m` | rows | `λ` | `δ` | sub-partitions of the tail | cold | warm |
|---|---|---|---|---|---|---|
| ≤ 36 | ≤ 9 | every cell of the long-weight screen | 8–12 | ≤ 715 | ≤ 8 s | ≤ 1 s |
| 31 | 8 | `(65,17,2⁷)` (the goal cell) | 24 | 585 | 11 s | 0.23 s |
| 40 | 6 | `(40,20,8,4,4,2,2)` | 20 | 4 939 | 79 s | 4.9 s |
| 44 | 6 | `(36,24,8,4,4,2,2)` | 20 | 6 207 | 167 s | 11 s |
| 48 | 6 | `(32,24,12,4,4,2,2)` | 20 | 9 281 | 325 s | 33 s |
| 48 | 8 | `(32,12,8,8,8,4,4,2,2)` | 20 | 20 075 | 433 s | 94 s |
| 49 | 10 | `(151,31,2⁹)`, `n = 5`, `N = 200` | 40 | 1 661 | 645 s | — |
| 52, 56 | 6 | `(…,24,12,8,4,2,2)`, `(…,28,12,8,4,2,2)` | 22 | 18 345, 22 749 | > 20 min (ended by pid) | |

The cost is `Σ_τ (trie of partitions of |τ|) × (reachable sub-partitions of
the tail)`: the tail's size first, then its width and row count; **`N` and
`δ` do not enter** beyond the one-off box weights.  **The rule:** a cell
`(λ, δ)` with `|λ̄| = |λ| − λ₁ ≤ 40` costs seconds warm and at most a minute or
two cold, at *any* `N` (the whole `δ ≥ 11` region the s38/s39 screens declared
beyond budget, and every `a = 1` census cell, is in this class); `|λ̄| ≈ 48` is
minutes; beyond `|λ̄| ≈ 52` with wide tails it is tens of minutes to hours —
still far below any partition sum, whose cost is set by `p(N)` — and there the
second reduction step (Lemma 1 applied again to the tail's
first row, with LR coefficients of ≤ 4-row shapes in place of the rectangle
rule) is the next thing to build.  `wk9_s58_sk.py cell <λ> <δ>` prints `g`,
`A`, `sk` and the timing for any cell; `--pieri --brute --house` add the checks.

## 7. `g(λ, δ⁴, δ⁴)` (deliverable 4), and the LMR family at the other `n`

The same technique reaches it — the reduction computes `g` and `A`
separately and `sk` is their mean, so `g` is a by-product at every cell above
(`92 000` at the goal cell), as is the antisymmetric coefficient
`ak = (g−A)/2 = 43 175`, the multiplicity in `Λ²`.  Nothing changes in cost.

Since the rectangle's row count `n` is a parameter, the LMR weights of the
other `n` (s50: `λ(k,d)` with `ℓ = 2n+1`, `δ = 2n(n−1)`) come at the same
price (`results/s58_lmrfamily.json`, `analysis/wk9_s58_lmrfamily.py`):

| `n` | `λ` | `δ` | `N` | `p(N)` | `g` | `A` | `sk` | time |
|---|---|---|---|---|---|---|---|---|
| 3 | `(19,7,2⁵)` | 12 | 36 | 17 977 | 11 | 9 | **10** | 0.3 s (brute force agrees: 10) |
| 4 | `(65,17,2⁷)` | 24 | 96 | 1.18 × 10⁸ | 92 000 | 5 650 | **48 825** | 0.4 s |
| 5 | `(151,31,2⁹)` | 40 | 200 | 3.97 × 10¹² | 2 864 545 604 | 6 344 960 | **1 435 445 282** | 645 s |

At `n = 3` the ambient multiplicity is `a = 6` (LMR's own value, reproduced
by the s50 integrator) against `sk = 10`; at `n = 4`, `274` against `48 825`;
the `n = 5` cell, at `N = 200`, is far beyond any partition sum and was never
computable before.

## 8. Standing constraints, as applied

- Degeneracy-direction (§5) and functoriality (§7) pre-checks: **vacuous** —
  no statistic or invariant is proposed; `sk` is the house `m_det`, the
  multiplicity in the orbit's coordinate ring, and `C[D̄] ↪ C[GL·det₄]` is why
  it bounds `mult_det`.  Recorded in the pre-registration, not skipped.
- Certificates: no `gct-cert/1` kind (`hwv`, `matrix`, `full_rank`) can carry a
  character-sum value, so **this session produced no certificate and did not
  run `tools/verify`**; its verification is the calibration of §3 and the
  four-route agreement of §5.  A `kronecker` kind, if wanted, would record the
  terms `(j, τ)`, the box, and the inner sums, which are the checkable
  intermediates.
- Runs bounded by `timeout` and `ulimit -v`, pids in `results/logs/s58_*.pid`;
  one run was ended by its recorded pid (the first `N = 28` sum-rule run, whose
  vertical-strip enumeration was exponential in the number of rows; rewritten
  polynomially, re-run, result unchanged).
- No file over 5 MB (the long-weight values are gzipped).  `PROJECT_NOTES.md`,
  the papers and `docs/boundary_deficit.html` untouched.
- No prime anywhere: the arithmetic is exact integers.

## 9. Corrections and observations for the single writer

1. `results/occurrence_screen.md` says δ = 11, 12 "exceed the session's
   character-computation budget"; with the reduction the entire δ = 11, 12
   length-5 region is minutes of work (tails ≤ 4δ−δ = 36), should anyone want
   the exhaustive rows.
2. The s39 engine is limited to `N ≤ 64` (`NMAX`) and to `λ₁ + 9 < 64`; the
   `(56, 2⁴)` cell at `N = 64` is refused by the bead width.  Neither is a bug,
   but neither is stated in `results/longweight_screen.md`.
3. Observation, not a claim: on the goal family the coefficient increases
   monotonically in `δ` to its limit (`2714 → 48825`); a proof would need the
   summands with `β₁ > δ` to be non-negative, which the support argument does
   not give.

## 10. Scorecard

| id | prediction | prior | outcome |
|---|---|---|---|
| M1 | every calibration value reproduced | — | **all reproduced** (see §3) |
| P1 | `sk ≥ 274` | 0.85 | confirmed, 48 825 |
| P2 | `10³ ≤ sk ≤ 10⁶` | 0.7 | confirmed |
| P3 | flat cost in `N` at fixed tail | 0.95 | confirmed, 0.37–0.41 s at `N = 48 … 96` |
| P5 | constant on `δ = 24 … 32` | 0.7 | confirmed; constant from 23 |
| M4 | s57 pending column | conditional | dropped by the integrator (s56/s57 not run); replaced by the rule of §6 |
| — | the integrator's boundary family, 9 direct values | added mid-session | all reproduced, plus 10 more through `N = 64` |
