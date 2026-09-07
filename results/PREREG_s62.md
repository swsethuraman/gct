# PRE-REGISTRATION — session 62 (batch 10, C1): the last-born scalar, and what the Gram route costs

Committed **before** any multiplicity, rank or Gram entry of this session is
computed. Branch `s62-gram`, off `main` at
`226b4ef1` (the public tip at session start; ancestry gate
`git merge-base --is-ancestor 226b4ef1 HEAD` passed on the fresh clone).
Container only, no pushes; delivery by single-ref bundle `s62_gram.bundle` +
`.md5`.

**Missing inputs, recorded.** The brief names `docs/batch10_worker_preamble.md`
and `docs/batch10_plan.md` as required reading. Neither file exists at
`226b4ef1`, in any branch of the public repository, or in any of the three
clones on the integrator's laptop (`work/`, `gct-rewrite/`,
`work-preRewrite/`, listed at session start). This session therefore works
from the brief's own statement of C1 (§0, §1, §4, §5 as quoted in the brief)
and says so wherever the plan would otherwise be cited.

What *was* computed before this commit, and is not a measurement of any claim
below: the weight-space dimensions `N_S` of the `n = 3` LMR ladder
(`1 155 302` at `(19,7,2^5)_{12}`, `1 118 518` at `δ = 11`, `1 017 919` at
`10`, `809 508` at `9`, `489 112` at `8`), and the ambient multiplicities
`a = 0, 2, 4, 5, 6, 6, 6` at `δ = 8..14` on that ladder by two house routines
(`a_weyl`, `pleth.ambient_multiplicity`), reproducing the brief's
`0,2,4,5,6,6`. These are sizes of the problem, quoted so the regimes below can
be stated; they decide nothing.

## 0. Provenance — what is already banked, and what this session does

The structural observation the brief builds on is **banked in the repository
since session 56**: `analysis/wk9_s56_hecke.py` (docstring and code) states and
verifies that `π ↦ ε_π` is not `S_N`-equivariant, that with the increasing
coset representative `K(π,π') = σ(h,π_0) K(π_0, hπ_0)` so one computed row gives
the whole signed Gram matrix, and that `β = K∘K` is `S_N`-invariant, depends
only on the double coset `rel(π,π')`, and is the Gram matrix of
`Θ⁺(π) = ε_π ⊗ ε_π`. Session 56 also proved `ker β = ker Θ⁺` and computed the
isotypic ranks `m_λ = rank(β|_{λ-isotypic})/f_λ` at every constituent of
`δ = 2, 3, 4`. **This session does not rediscover any of that.** It

1. measures what a Gram entry costs, as a curve, not an estimate;
2. lifts the orbital Gram to the `a_λ × a_λ` block on the highest-weight
   vectors, in the ladder splitting, and computes the room-one Schur
   complement `s`;
3. runs the positive control the programme has never had: a cell with a
   theorem-guaranteed rank drop.

## 1. The objects and the one identity everything rests on

Notation as in `docs/s57_report.md` §1 and `docs/s56_report.md` §1–2. For a
weight `λ ⊢ nδ` with `r = ℓ(λ)` (the programme's `n = 4`; the positive control
has `n = 3`; one control has `n = 2`), `H = H_{n,δ}` is the Foulkes module of
block decompositions of `[N]`, `N = nδ`, into `δ` blocks of size `n`;
`K(π,π') = ⟨ε_π, ε_π'⟩` the signed kernel; `β = K∘K`.

**Weight space.** Colour `[N]` by `λ` (the first `λ_1` labels colour 1, …).
`H^{S_λ}` has the basis of `S_λ`-orbit sums `m_O = Σ_{π∈O} π`, one per
multiset `O` of `δ` colour-content vectors summing to `λ`, i.e. one per
monomial of the weight-`λ` space of `Sym^δ(Sym^n C^r)`; `n_λ := dim H^{S_λ} =
N_S(λ,δ)`.

**Highest-weight vectors on the `S_N` side.** In the tensor model
`Sym^δ(Sym^n V) = (V^{⊗N} ⊗ H)^{S_N}`, a weight-`λ` vector is determined by its
`H^{S_λ}`-component `v`, and the raising operator `E_{ij}` acts by
recolouring: `E_{ij} v = Σ_{p ∈ C'_i} g_p · v`, the sum over the positions `p`
of colour `i` in the new colouring `λ + e_i − e_j`, `g_p ∈ S_N` the permutation
carrying the standard `λ`-colouring to the one in which `p` has colour `j`
and everything else is standard. `M_λ := ⋂_i ker E_{i,i+1} ⊂ H^{S_λ}` is the
highest-weight space; by Schur–Weyl it is `{φ(w) : φ ∈ Hom_{S_N}([λ], H)}`,
`w` the `S_λ`-invariant line of `[λ]` (`K_{λλ} = 1`), so `dim M_λ = a(λ,δ)`.

**The block Gram matrix.** `β` is `S_N`-invariant, so on the `λ`-isotypic
component `[λ] ⊗ Hom([λ],H)` it is `(form on [λ]) ⊗ G_λ`; restricted to `M_λ`
it is `⟨w,w⟩ · G_λ`. Hence, with `V` the `n_λ × a` matrix of highest-weight
coordinates in the orbit-sum basis and `B_λ(O,O') := β(m_O, m_O') = |O'|
Σ_{π∈O} β(π, π'_0)` (`π'_0 ∈ O'` any representative),

    G_λ = Vᵀ B_λ V     (a × a, exact rational),     mult_det(λ,δ) = rank_Q G_λ,

which is the `a_λ × a_λ` block the brief names. `B_λ` is exactly session 56's
`|O'|·b^μ(O,O')` at `μ = λ`. The identity `rank G_λ = rank Θ⁺|_{M_λ}` holds
over `Q` (and `R`) because the target inner product is positive definite; it
is **false over `F_p`**, and no rank of `G_λ` modulo a prime is used as a
multiplicity anywhere in this session. Ranks of `G_λ` are taken over `Q`
(`fmpz_mat`/`fmpq_mat`); ranks modulo the house primes appear only as the
usual lower-bound cross-checks on the original evaluation map, labelled as
such.

**Ladder splitting and the scalar.** At a room-one cell (`a_δ − a_{δ−1} = 1`),
Lemma L (s57, proved) gives `M_δ = u·M_{δ−1} ⊕ ⟨v_ρ⟩`, `u = e_1^n` the
coefficient functional of `s_1^n`. In a basis adapted to the splitting

    G = [[A, b],[bᵀ, c]],   det G = det A · s,   s = c − bᵀ A⁻¹ b,

`A` is the Gram matrix of the transported vectors `u·h_i`; it is nonsingular
exactly when the predecessor is determinant-full-rank (multiplication by `ū`
is injective on `C[D_r]`, a domain, Lemma L). Then `rank G ∈ {a−1, a}` and
**a determinant kernel is born at the cell iff `s = 0`.** `s` is independent of
the choice of `v_ρ` modulo `u·M_{δ−1}` and of the basis of `M_{δ−1}`
(`s ↦ s`, `det A ↦ (det P)² det A`); its vanishing is intrinsic.

**Two inner products, both legitimate, kept apart.** Any positive-definite
form on the target gives the same rank and the same zero of `s`. Two are used
and every claim names which:

- **Foulkes Gram** — the `S_N`-invariant form `β = K∘K` on `H`, i.e. (as shown
  in the report) the Fischer inner product of the pulled-back polynomials
  `Φ_h(A_1..A_r) = h(det_n(Σ s_i A_i))` up to the constant `∏ λ_i!`. This is
  the orbital Gram of the brief; its entries are the cost object of Task 1/5.
- **Evaluation Gram** — `G = E Eᵀ` with `E` the `a × K` exact integer matrix of
  the highest-weight basis evaluated at `K ≥ a` integer `det_n` pencils; the
  form `⟨f,g⟩ = Σ_k f(P_k) g(P_k)` on `C[D_r]_δ`, positive definite on the span
  of the restrictions for generic points. `rank_Q(EEᵀ) = rank_Q E = mult_det`
  exactly. It is the programme's evaluation route re-expressed as a Gram
  matrix; it validates the **ladder splitting and the scalar criterion**, not
  the orbital entries.

## 2. Regimes

| regime | `n` | cells | Gram used | purpose |
|---|---|---|---|---|
| R1 | 4 | every constituent of `Sym^δ(Sym^4)`, `δ = 2,3,4` (3+9+28 = 40) | Foulkes, full `H` enumerated (`|H| ≤ 2 627 625`) | Task 2/3: reproduce s56; room-one cells by `s`, others by `rank_Q G_λ`; certificates |
| R2 | 4 | the same 40 | — | Task 1: support sizes `n_λ`, HWV support, last-born (u-free) support; cost curve of `B_λ` and of one Gram entry |
| R3 | 3 | every weight of `H_{3,δ}`, `δ = 2..5` (`|H| ≤ 1 401 400`) | Foulkes, full `H` | independent cross-check of the block formula against s56's weight route (inverse Kostka on the whole of `H`), at an `n` where a kernel of `Θ⁺` is possible |
| R4 | 2 | `(2^5)_5`, `(2^6)_6` | Foulkes, full `H` (945, 10 395) | a **proved** rank drop (`det` of the symmetric matrix vanishes on rank-≤4 quadrics): the Foulkes Gram must return `mult = 0 < a = 1` |
| R5 | 3 | the `n = 3` LMR ladder `(3δ−17, 7, 2^5)`, `δ = 9..12` | evaluation engine (`mult_det = a − nullity [E; ev_det]`, `r = 7`, `det_3` pencils), then evaluation Gram in the ladder splitting | Task 4, the must-pass: ground truth `rank ≤ 5` at `δ = 12`, then `s = 0` there |
| R6 | 3 | `(19,7,2^5)_{12}` | Foulkes | attempted only through the block-intersection counting of Task 5; declared out of reach if the counting does not fit, with the cost curve as the reason |

Nothing at `δ ≥ 5` for `n = 4` is attempted; `δ = 23, 24` are not attempted
under any circumstances (stopping rule 3 of the brief).

## 3. Predictions, falsifiers, labels

Labels: **proved** / **measured** / **adopted** (from the record) /
**expectation** (this session's prior, falsifiable).

- **P1 (proved, checked)** `dim M_λ = a(λ,δ)` at every R1/R3/R4 cell, `a` by
  `tools/verify/pleth.py` (Weyl alternation). *Falsifier:* any cell where the
  recolouring kernel has a different dimension — that stops the
  implementation.
- **P2 (adopted from s56, to reproduce)** `rank_Q G_λ = a` at all 40 R1
  cells, `i_det = 0`; at the room-one cells `s ≠ 0`. *Falsifier:* any
  `rank_Q G_λ < a`, or `s = 0`, at a banked full-rank cell → stopping rule 1
  (find the defect before proceeding). Note the weakness, stated now: at
  `δ ≤ 4`, `β` is injective on all of `H` (s56), so *any* independent
  `a`-tuple has a nonsingular Gram; P2 tests the plumbing and the
  normalisation, not the identification of `M_λ`. P3–P5 carry that weight.
- **P3 (isotypic membership, `δ = 2, 3`)** every vector of `M_λ` satisfies
  `P_λ v = v` for the Hecke isotypic projector of s56 (rebuilt on `|H| × |H|`).
  *Falsifier:* `P_λ v ≠ v` → the recolouring operators or the orbit-sum
  normalisation are wrong.
- **P4 (independent route, R3)** at every weight of `n = 3`, `δ ≤ 5`, the
  block rank `rank_Q G_λ` equals the isotypic rank obtained by s56's route
  (b): `m_λ = Σ_μ (K^{-1})_{λμ} r_μ` from the weight-space ranks `r_μ` of
  `B_μ` on all of `H_{3,δ}`. *Falsifier:* a single disagreement.
- **P5 (proved)** `n = 2`: `rank_Q G_{(2^5)} = 0` at `δ = 5` and
  `rank_Q G_{(2^6)} = 0` at `δ = 6` (`a = 1` at each: the determinant of the
  symmetric matrix of the quadric). *Falsifier:* rank 1 → the Foulkes Gram
  cannot see a kernel that exists, stop.
- **P6 (bookkeeping, to verify)** pair-orbitals of `S_{4δ}` on `H_{4,δ}`:
  3, 9, 43 at `δ = 2, 3, 4`; constituents of `Sym^δ(Sym^4)`: 3, 9, 28; max
  multiplicity 1, 1, 2, the multiplicity-2 constituents at `δ = 4` being
  `(12,4), (10,6), (10,4,2), (8,6,2), (8,4,4)`; `Σ_λ a_λ² = #orbitals` at
  each `δ` (the dimension of the centralizer algebra). *Falsifier:* any
  number differs.
- **P7 (must-pass, adopted from theory)** R5 ground truth: `mult_det((19,7,
  2^5), 12) ≤ 5 < a = 6`. The engine's mod-`p` nullity of `[E; ev_det]` is
  `≥ 1` at both primes (that alone proves only `mult_det ≥ 5`); the drop is
  proved over `Q` by exhibiting an **integer** highest-weight vector
  (rational reconstruction of the mod-`p` kernel, `E·v = 0` checked over `Z`)
  whose evaluation at fresh integer `det_3` pencils is exactly `0` over `Z`
  at every point tried, and which is nonzero at a generic cubic. *If the
  ground truth is out of reach* (build or kernel does not fit the container),
  that is the session's headline and the Gram programme is declared
  unvalidated.
- **P8 (the scalar)** with the evaluation Gram in the ladder splitting at
  `(19,7,2^5)_{12}`: `A` (5×5) nonsingular over `Q` and `s = 0` exactly.
  *Falsifier:* `s ≠ 0` while P7 holds → the splitting or the transport is
  wrong; `A` singular → the predecessor `(16,7,2^5)_{11}` is not full rank
  (see P9).
- **P9 (expectation)** the predecessor cells are full rank:
  `mult_det = a` at `δ = 9, 10, 11` (`2, 4, 5`), so at the room-one cell
  `δ = 11` (`4 → 5`) `s ≠ 0` and at `δ = 10` (room two) the block rank is
  `4`. *Refutation would be a finding*: a degree-11 equation of `D_7^{det_3}`,
  below the LMR degree, is not predicted by anything in the record.
- **P10 (expectation)** the Foulkes Gram at the `n = 3` LMR cell is **out of
  reach**: `|H_{3,12}| ≈ 3.7·10^{23}`, so enumeration is impossible, and the
  block-intersection counting of Task 5 runs over labelled `12 × 12`
  contingency tables with margins 3 — the session will size that count and
  expects it to exceed anything computable. R6 is then reported as out of
  reach with the numbers, and P8 stands on the evaluation Gram alone.
- **P11 (expectation, the cost curve)** the cost of `B_λ` is `Θ(|H| · n_λ)`
  by the enumeration route (the s56 pass), and the alternative — one Gram
  entry from block-intersection data — needs the full distribution of
  `rel(π, π'_0)` over `π ∈ O`, a count over 3-way tables (π-block × π'-block
  × colour) whose number explodes with `δ`; the session expects the Gram
  route, as a route to `δ = 23, 24`, to die on this curve at `δ = 4`
  (brief's stopping rule 2), and expects the curve to say so unambiguously.
- **P12 (expectation)** Smith normal forms of the small blocks `G_λ` and
  `B_λ` look generic (elementary divisors dominated by one large last
  invariant, no repeated small primes beyond the `24^δ`-type content).
  Diagnostics only; no congruence claim will be made whatever they show.

## 4. Kill / stopping rules

1. Any mismatch with a banked rank (P2, P4) stops the implementation until
   the defect is found; the theorem is not in question.
2. If Gram-entry construction (P11) does not fit at `δ = 4` for `n = 4`, the
   Gram route stops there; the Schur-complement results and the cost curve
   are kept and reported.
3. `δ = 23` and `δ = 24` are not attempted. `δ = 5` for `n = 4` is not
   attempted (s56 measured the wall).
4. Every rank of `G` is over `Q`; every mod-`p` statement is about the original
   map and is labelled as a characteristic-zero lower bound.
5. Anything over 5 MB is not committed; logs go to `results/logs/`; every cell
   is banked with a commit as it completes.

## 5. Deliverables

`results/PREREG_s62.md` (this file); `docs/s62_report.md`; `results/s62_cost.md`
and `results/s62_cost.json`; certificates for every reproduced calibration in
the declared format (`tools/verify/FORMAT.md`, kind `matrix` for `G_λ`, `B_λ`
and the `n = 3` evaluation matrices — the `hwv`/`full_rank` kinds fix
`n = 4` and are not used for `n = 3`); the `n = 3` positive control as its
own artefact `results/s62_n3_control.md` (+ `.json`) with both routes side by
side and an independent checker `analysis/wk10_s62_n3check.py`; code under
`analysis/wk10_s62_*.py`; bundle `s62_gram.bundle` + `.md5`.
