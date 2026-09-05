# PRE-REGISTRATION — session 56, the Foulkes engine

Committed **before** any computation of this session. Branch `s56-foulkes`,
off `main` at `0960bd548eae4a9767276f9a1f20d686538c3374` (the tip of
`work/main` and of the GitHub mirror at session start; the sync baseline for
rule 10 — the ancestor test is trivially satisfied because the branch is cut
from that commit).

Nothing below has been measured at the time of this commit. The dimensions
quoted in §2 (`|H|`, `f`, `a`, `sk`) are bookkeeping computed with the house
routines (`tools/verify/pleth.py`, `scripts/ambient_screen.py`) and closed
formulas; they are the *known* source and target dimensions, not measurements.
The only quantity this session measures is a rank.

## 0. The object and the claim

Polarise the degree-`δ` coordinate ring into `N = 4δ` separately labelled
matrices. Schur–Weyl duality turns the `GL(V)`-equivariant restriction map

    Φ*_V : Sym^δ(Sym^4 V) → C[Hom(V, M_4)]_{4δ},   F ↦ F(det_4(Σ s_i A_i)),

whose image is `C[D_r]_δ` for `r = dim V`, into an `S_N`-module map

    Θ_δ : H_{4,δ} = Ind_{S_4 ≀ S_δ}^{S_N} 1  →  [δ^4] ⊗ [δ^4],

and the multiplicity of `S_λ(V)` in `C[D_r]_δ` (`r = ℓ(λ)`) is the rank of
`Hom_{S_N}([λ], Θ_δ)`. Both facts are standard (polynomial functors of degree
`N` ≅ `S_N`-modules; the image of a natural transformation is a subfunctor). The
claim to implement and verify is therefore

    mult_det(λ, δ) = rank Hom_{S_N}([λ], Θ_δ),

with source dimension `a(λ, δ)` (plethysm coefficient) and target dimension the
rectangular Kronecker coefficient.

**Concretely.** A basis vector of `H_{4,δ}` is an unordered block decomposition
`π = {B_1, …, B_δ}` of `[N]` into 4-sets. Each block contributes the coefficient
of `∏_{i∈B} s_i` in `det(Σ s_i A_i)`, which is the full polarisation of the
determinant — the mixed discriminant `D(A_i : i ∈ B) = ⟨ε ⊗ ε, ⊗_{i∈B} A_i⟩`
with `ε` the `4×4×4×4` alternating tensor. Hence, as a multilinear function of
`(A_1, …, A_N)` with `A_i ∈ E ⊗ F`,

    Θ_δ(π) = ε_π ⊗ ε_π,      ε_π := ⊗_{j} ε^{(B_j)} ∈ (E*)^{⊗N},

the *same* block-alternating tensor on the row side and on the column side: the
diagonal Plücker map. `R_δ := span{ε_π} ⊂ (Q^4)^{⊗N}` is the space of
multilinear `SL_4`-invariants of `N` vectors (products of maximal minors), which
is the rectangular Specht module `[δ^4]` of dimension `f_{δ^4}` = the number of
standard tableaux of the `4 × δ` rectangle — this is the multilinear first and
second fundamental theorem (the Plücker relations are the kernel of
`H → R_δ`, `π ↦ ε_π`; after straightening, `R_δ ≅ [δ^4]`).

## 1. Task 1 — the involution, decided

`Θ_δ(π) = ε_π ⊗ ε_π` is manifestly symmetric under the swap of the two tensor
factors, which is the simultaneous transpose `(A_1, …, A_N) ↦ (A_1^T, …, A_N^T)`
(`det A^T = det A`). So the image lies in `Sym^2 R_δ ≅ Sym^2 [δ^4]` with no
projection, and the `[λ]`-multiplicity of the target is the **symmetric**
rectangular Kronecker coefficient `sk(λ, δ^4) = ⟨χ^λ, Sym^2 χ^{(δ^4)}⟩`, the
house `m_det`.

**Decision: construct `Θ^+_δ : H_{4,δ} → Sym^2 [δ^4]` directly.** Reason: the
diagonal form makes the symmetric square the natural codomain — nothing is
projected away, and the antisymmetric part (`g − sk` dimensions per `λ`) is never
built. The alternative (build `Θ_δ` into `[δ^4] ⊗ [δ^4]` and project onto the
transpose-even eigenspace) constructs a strictly larger target only to discard
part of it. The `sk` identity itself is re-checked in this session at every `δ`
built (P6 below) against the house `m_det` column.

## 2. Method — exact, in the symmetric-group category, no highest-weight vectors, no pencils

**The realisation of the target.** `R_δ` is realised as the span of the sparse
integer tensors `ε_π` in the `4^N`-dimensional tensor basis of `(Q^4)^{⊗N}`
(`ε_π(x) = ∏_j ε(x|_{B_j})`, non-zero at exactly `24^δ` points, values `±1`).
The invariant inner product gives the exact integer Gram kernel

    K(π, π') := ⟨ε_π, ε_π'⟩ = Σ_{x ∈ [4]^N} ε_π(x) ε_π'(x),

which depends only on the relative position `d = rel(π, π')` (the `δ × δ` block
intersection matrix up to row and column permutation — a double coset
`W \ S_N / W`, `W = S_4 ≀ S_δ`). `K(π, π) = 24^δ`.

**The map, coordinate-free.** The pull-back of the target inner product along
`Θ^+` is the Hadamard square

    β(π, π') := ⟨Θ^+(π), Θ^+(π')⟩ = K(π, π')²,

an `S_N`-invariant positive-semidefinite form on `H` with `ker β = ker Θ^+`. So
`Im Θ^+ ≅ H / ker β` as `S_N`-modules and, for every `λ`,

    rank Hom_{S_N}([λ], Θ^+_δ) = rank(β restricted to the λ-isotypic part of H) / f_λ.

Straightening into standard bitableaux is one *coordinatisation* of `R_δ`; the
Gram kernel is another, and it is the one the computation uses. At `δ = 2` the
straightened matrix of `Θ^+` (35 × 105) is also written out explicitly, as the
literal form of the brief's construction, and the two agree or the session
reports the discrepancy.

**Isotypic ranks, two independent routes within the engine.**

(a) *Full Hecke route* (`δ ≤ 3`). `β` and the isotypic projectors
`P_λ = (f_λ/N!) Σ_C χ^λ(C) (Σ_{g∈C} g)` both lie in `End_{S_N}(H) = span{A_d}`
(the double-coset operators). Their coefficients are computed exactly: `K_d` by
the sum above; `P_λ`'s by the cycle-type histogram of one coset `g_d W` per
double coset and the character table of `S_N` (Murnaghan–Nakayama). Then
`m_λ = rank(β P_λ) / f_λ` and `a_λ = rank(P_λ) / f_λ` on the `|H| × |H|` matrices
(35 and 5775).

(b) *Weight-space route* (`δ ≤ 4`). For a dominant weight `μ` (a colouring of
`[N]` with `μ_c` positions of colour `c`), the `S_μ`-fixed vectors of `H` are the
weight-`μ` monomials `m_O = Σ_{π∈O} π` (`O` an `S_μ`-orbit = a multiset of `δ`
exponent vectors of degree 4 summing to `μ`); there are `nb_μ` of them. The Gram
matrix of their images,

    B^μ(O, O') = ⟨Θ^+ m_O, Θ^+ m_O'⟩ = |O'| · b^μ(O, O'),
    b^μ(O, O') := Σ_{π ∈ O} K(π, π'_0)²   (π'_0 any representative of O'),

has rank `r_μ := rank Θ^+|_{H^{S_μ}} = Σ_{ν ⊵ μ} K_{νμ} m_ν` (Kostka numbers),
while `nb_μ = Σ_ν K_{νμ} a_ν`. Hence

    m_λ = Σ_{μ ⊵ λ} (K^{-1})_{λμ} r_μ,      a_λ = Σ_{μ ⊵ λ} (K^{-1})_{λμ} nb_μ,
    nb_μ − r_μ = Σ_{ν ⊵ μ} K_{νμ} i_det(ν, δ) ≥ 0.

In particular `r_{(δ^4)} = nb_{(δ^4)}` if and only if `i_det = 0` at **every**
weight of degree `δ` (every `ν ⊢ 4δ` with `ℓ(ν) ≤ δ` dominates the rectangle),
i.e. iff `Θ^+_δ` is injective. `b^μ` is computed by one exact pass over all of
`H` per monomial `O'` (a C program: block masks, `δ²` popcounts, a hash lookup of
`K_d`, an integer accumulator per orbit), so its cost is `nb_μ · |H_{4,δ}|`.

**Arithmetic.** Integer kernels; ranks over `Q` (`fmpz_mat`, exact) where the
matrix fits, and modulo **both house primes** `2147483647` and `2147483629`
(`nmod_mat`) everywhere. A rank is reported only when the two primes agree; a
disagreement between primes is itself reported.

**Bookkeeping (known, not measured).**

| `δ` | `N` | `|H_{4,δ}|` | `f_{δ^4} = dim [δ^4]` | `dim Sym^2 [δ^4]` | constituents `a ≥ 1` |
|---|---|---|---|---|---|
| 2 | 8 | 35 | 14 | 105 | 3 |
| 3 | 12 | 5,775 | 462 | 106,953 | 9 |
| 4 | 16 | 2,627,625 | 24,024 | 288,588,300 | 28 |
| 5 | 20 | 2,546,168,625 | 1,662,804 | ≈ 1.38 × 10^12 | 23 of length 5, more of length ≤ 4 |
| 6 | 24 | ≈ 4.51 × 10^12 | 140,229,804 | ≈ 9.8 × 10^15 | (six-row record lives here) |
| 7 | 28 | ≈ 1.32 × 10^16 | ≈ 1.37 × 10^10 | ≈ 9.3 × 10^19 | |

`Σ_λ a_λ f_λ = |H|` at `δ = 2, 3, 4` (checked: 35, 5775, 2627625).

## 3. What will be measured

For every `(λ, δ)` with `δ ∈ {2, 3, 4}`, `λ ⊢ 4δ`, `ℓ(λ) ≤ δ` (all others have
`a = 0`): the integer `m_λ = rank Hom_{S_N}([λ], Θ^+_δ)`, by route (a) at
`δ ≤ 3` and route (b) at `δ ≤ 4`, both primes, and `Q` where feasible. Also
`r_μ`, `nb_μ` for every dominant `μ ⊢ 4δ`, `ℓ(μ) ≤ δ`.

At `δ = 5` the engine is not expected to reach any length-5 cell (§5); one
bounded cost probe is run (a single pass over `H_{4,5}` at the most dominant
weights) so that the cost curve has a measured point at `δ = 5`.

## 4. Predictions and falsifiers, fixed now

- **P1 (the calibration).** `m_λ = a_λ` at every cell built. The banked values:
  `ℓ(λ) ≤ 3`: `mult_det = a` is a theorem (`D_r^{det_4} = Sym^4 C^r` for
  `r ≤ 3`, `docs/sweep62.md` §4); `ℓ(λ) = 4`, `δ ≤ 9`: `mult_det = a` because
  `I(D_4^{det})` is principal of degree `e ≥ 10` (certified, s33,
  `docs/e4_hunt.md`); `(4,4,4,4)_4`: measured `a = 1`, `mult_det = 1`
  (`docs/det_onset.md` §3, `results/e4_ledger.md`). So at `δ ≤ 4` the prediction
  is `Θ^+_δ` **injective**: `rank β = |H|`.
- **P2.** `rank K = f_{δ^4}` at `δ = 2, 3` (the Gram matrix of a spanning set of
  `[δ^4]`); at `δ = 4` the per-weight form `rank k^μ = K_{(δ^4), μ}` (Kostka
  number) for every dominant `μ`, where `k^μ(O,O') = Σ_{π∈O} K(π, π'_0)`.
- **P3.** `Σ_μ (K^{-1})_{λμ} nb_μ = a_λ` for every `λ` (the weight-space count
  reproduces the plethysm coefficient) and `m_λ = 0` wherever `a_λ = 0`.
- **P4.** Routes (a) and (b) agree at `δ = 2, 3`; the explicit straightened
  `Θ^+_2` agrees with both.
- **P5.** `0 ≤ m_λ ≤ min(a_λ, sk_λ)` identically; `m_λ = a_λ ⟺ i_det = 0`
  (given the claim this is `i_det = a − m`; it is recorded as the consistency
  the brief asks for).
- **P6.** `sk(λ, δ^4)` recomputed here as `⟨χ^λ, Sym^2 χ^{(δ^4)}⟩` equals the
  house `m_det` at every `δ ≤ 5` cell it can be compared with (the 23 `δ = 5`
  rows of `results/occurrence_screen.csv`, and the `δ ≤ 4` values of
  `scripts/ambient_screen.m_det`).
- **P7 (cost).** The `δ = 4` weight-space computation completes within the
  session (`Σ_μ nb_μ` passes over 2.6 × 10^6 partitions); the `δ = 5` probe
  measures a per-pass cost of order minutes over 2.5 × 10^9 partitions, from
  which the cost of the cheapest length-5 cell (`(12,2,2,2,2)`, `nb = 553`)
  and of the rectangle (`nb = 19834`) is extrapolated and reported as the wall.

## 5. Stopping rule — absolute

One disagreement `m_λ ≠` banked `mult_det` at any cell, on both primes, and the
session **stops**: it reports the cell, both computations (this engine's rank
and the banked measurement with its source), and a diagnosis of which is wrong.
The map is not tuned to agree. A prime-to-prime disagreement or a failed
structural check (P2–P4) is a bug in this engine until proved otherwise and is
reported as such; it does not count as a calibration disagreement.

## 6. What is out of range, stated before the fact

The 210 six-row cells (`δ = 6..10`) and the length-5 cells at `δ ≥ 5` are
outside what this engine can reach exactly: `|H_{4,5}| = 2.5 × 10^9` and every
exact isotypic question about `Θ_5` touches every basis vector of `H_{4,5}`
(per weight monomial, in the weight-space route). The session will measure this
wall rather than guess it (P7). Any statement about six-row cells in the report
is therefore about *method*, not calibration.

## 7. The two house pre-checks

- **§7 functoriality.** No new invariant is proposed. The quantity computed is
  `mult_det` itself — the coordinate-ring multiplicity, row 1 of the §7 table,
  functorial under closed immersion by `C[D] ↠ C[P]`. Passes by reference.
- **§5 degeneracy direction.** No statistic is developed; a second computation
  of an existing multiplicity is. The pre-check concerns statistics evaluated at
  the three test points (det pencil, `ℓ·c`, ten-variable `ℓ·per_3`); the
  engine's output is a rank of a module map with no evaluation point, so the
  check has no instance here. Recorded as not applicable, with this reason.

## 8. Process

Every run: `timeout`, `ulimit -v`, pid in `results/logs/s56_<run>.pid`, log in
`results/logs/s56_<run>.log`. Code `analysis/wk9_s56_*.py`,
`analysis/wk9_s56_pass.c`. Certificates in `gct-cert/1` (`kind: matrix`, the
integer Gram matrices with claimed ranks over `Q` and mod both primes) through
`tools/verify/verify.py`. No committed file over 5 MB. Deliver by bundle; do
not push. Commit trailers: `Co-Authored-By` only.
