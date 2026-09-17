# Arc-target dimension follow-up: a characteristic-zero upper bound on `rank C` via the grading-preserving Levi

Claude session, 17 September 2026. Fresh directory
`work/claude_source_vectors_20260917/arc_target_dimension_followup/` (sibling of the sealed parent
packet `routeA_signfilter_20260917/`, preserved byte-for-byte: 31 parent outputs and 46 inherited
inputs re-hashed at session start and again at sealing, 0 mismatches, no unlisted files).

## Verdict

**Case C. The grading-preserving Levi bound is `rank C ≤ b_L = 74` — PROVED, exact, by two
independent formulations — and it is far too weak to decide anything: the known ceiling is
`rank C ≤ 4` (`E ⊆ ker C`). No upper bound below 4 is obtained. Transverse independence from the arc
is therefore NOT proved here, neither existentially nor by a witness. The excess comes from the
skew-degree-11 part (70 of the 74) and, structurally, from the smallness of `L` (dimension 11) inside
`H^0` (dimension 31): the unipotent part of the stabilizer imposes constraints on the forbidden
components that the Levi count cannot see. A rigorously smaller target `F'' ⊆ F^L`, defined by those
constraints plus transposition invariance, is proved to contain `C(M)` (§6) but its dimension is not
computed (priced in §6.4). Proposition 7.1 shows that `rank C|_S = 2` on the certified three-vector
subspace `S = span(q_3, q_7, n02)` would already yield the existence result and the lift of the
displayed modular candidate; that hypothesis remains OPEN.**

Proof dependencies of the verdict: B19-01 Prop. 3.1 and Thm. 6.2 (PROVED there; the relevant parts
re-derived in §3); the `L`-invariant condition (§3.2, PROVED here); Littlewood–Richardson and Kostka
arithmetic (`code/b_L_branching.py`, exact integers, two formulations, controls in §5.2). No numerical
evaluation of any source vector was made in this session.

**Standing reminder.** `a = m_det = 1` in this cell: no positive multiplicity gap is possible. The cell
tests the boundary-compatibility mechanism only.

## 0. Question and proof skeleton

Known (parent packet; PROVED/CERTIFIED over `Q`): `dim M = 5`, `dim E = 1`, `E ⊆ ker C`, `rank C ≥ 2`,
`rank T = 3` for `T = (C2, C4_{S1,S2}, C4_{S1,S4})`. If `rank C ≤ 2` were proved: `rank C = 2`,
`dim ker C = 3 > 2 = dim ker T`, so `ker C ⊄ ker T` — an existence statement prior to any witness.
The tool is B19-01 Thm. 6.2: `rank C ≤ b_L := dim F^L`. This report repairs the logic (Part 1),
computes `b_L` (Part 2), and draws the justified conclusion (Part 3).

## 1. Inputs pinned (read-only; hashes in `MANIFEST.json`)

Parent packet `routeA_signfilter_20260917/` (`REPORT.md`, `MANIFEST.json`, `certificates/*.json`,
`results/*.json`); B19-01 `work/batch15_workers/B15-01/docs/b19_01_report.md` §2, §3 (Prop. 3.1),
§6 (Prop. 6.1, Thm. 6.2, §6.3); B18-02 `work/batch15_workers/B15-02/docs/b18_02_report.md` §1
(adapted coordinates, `gamma`, forbidden weights), §4 (Lemma 4.1); the clarification packet
(`SOURCE_HANDOFF.md`, `STABILIZER.md`, `CORRIGENDUM.md`). Session state at start: no `python`/CAS
process running (`tasklist`), about 6.1 GiB free physical memory.

## 2. Definitions (fixed before computing)

### 2.1 Module, dual, character

`W = Mat_4 = A ⊗ B` (dim 16), `d = 5`, `λ = (4^5)`. `M` is the space of polynomial functions on
`W ⊗ C^5` of multidegree `(4^5)` that are `GL_5`-highest-weight vectors of weight `λ` and satisfy
`z(AYB) = (det A det B)^5 z(Y)`, `z(Y^T) = z(Y)`. The highest-weight space is `S_λ(W*) ⊗ (one line)`,
isomorphic to `S_λ(W*)` as a `GL(W)`-module (B18-02 Thm. 2.1). On `H^0 = {(A,B): det A det B = 1}`
every `z ∈ M` is an invariant function. Every count below is a count of **invariants** (trivial
character) of a reductive group; `dim V^G = dim (V^*)^G`, so counting in `S_λ(W)` (pieces as
`GL_3`-modules) and in `S_λ(W*)` (the polynomial side) give the same number. All determinant twists
are explicit: `Λ² std ≅ std^* ⊗ det`, and the `L`-character is `αβc³(det g)²`.

### 2.2 Adapted coordinates, grading, forbidden components

B18-02 §1: `a = Y_00`; `r_k = Y_{0k}`; `c_k = Y_{k0}`; lower-right block `E = Σ + A(v)`, `Σ` symmetric,
`A(v)_{ij} = −ε_{ijk} v_k` (0-based). Weight pieces `W_{-1} = ⟨a, r⟩` (dim 4), `W_0 = ⟨v⟩` (dim 3),
`W_{+1} = ⟨c, Σ⟩` (dim 9); a monomial has weight `#c + #Σ − #a − #r`. By B19-01 Prop. 3.1,
`S_λ W = ⊕ c^λ_{μκτ} S_μ(W_{-1}) ⊗ S_κ(W_0) ⊗ S_τ(W_{+1})`, and on torus-invariant `z` every component
has `|μ| = 5`, `|κ| = #v`, `|τ| = 15 − #v`, weight `10 − #v`. **Forbidden** = negative weight
= `#v ∈ {11, 12}` (`κ ⊆ λ`, `ℓ(κ) ≤ 3` ⇒ `κ ⊆ (4,4,4)`, so `#v ≤ 12`). `C(z) = (z_{−2}, z_{−1})`.
`F := F_{−2} ⊕ F_{−1}` denotes the `#v = 12` and `#v = 11` graded pieces of `S_λ W` (all `μ, τ`).

### 2.3 The grading-preserving Levi (B19-01 Prop. 6.1, re-derived in §3.1)

    L = { (diag(α, g), diag(β, c·gᵀ)) : g ∈ GL_3, α, β, c ∈ C*, αβc³(det g)² = 1 } ⊆ H^0,

connected. Action on the pieces (`GL_3 × (C*)³`-modules, `std = C³`):

| piece | `GL_3`-module | scalar |
|---|---|---|
| `a` | triv | `αβ` |
| `r` | std | `αc` |
| `v` | `Λ² std` | `c` |
| `c` (first column) | std | `β` |
| `Σ` | `Sym² std` | `c` |

`L` preserves each `W_i`, hence each `(μ,κ,τ)`-component, hence `F`; `C` is `L`-equivariant;
`M ⊆ (S_λ W)^L` because `(det A det B)^5 = 1` on `L`. Therefore `C(M) ⊆ F^L` and
`rank C ≤ b_L := dim F^L` (B19-01 Thm. 6.2). `C(M) = F^L` is not assumed anywhere.

## 3. Logic repairs (Part 1)

### 3.1 The two symmetry groups; no transposition in `L` (PROVED)

`STABILIZER.md` concerns `Stab(K5)`, the stabilizer of one pencil; it is irrelevant to `L`, which is the
subgroup of `H = Stab(det_4)` preserving the `gamma`-grading. Derivation of `L`: `x ↦ AxB` preserves
`W_{-1}` (matrices supported on the first row) iff `A e_0 ∈ C e_0`... precisely, `A Y B` has zero
entries outside the first row for all such `Y` iff `A = diag(α, g)` (first column `(α,0,0,0)ᵀ`, first
row `(α, *)` forced to `(α,0,0,0)` by preserving `W_0 ⊕ W_{+1}` = zero first row) and `B` has first
row `(β, 0, 0, 0)`; preserving `W_{+1}` (zero first row, symmetric block) forces the lower block of
`B` to be `c gᵀ` and the first column of `B` to be `(β,0,0,0)ᵀ`; preserving `W_0` (skew block) then
holds automatically. Every such element lies in `H^0` iff `αβc³(det g)² = 1`. For the transposition
coset: `Y ↦ (AYB)ᵀ = BᵀYᵀAᵀ` maps `W_{-1}` (first row) into matrices whose *column* structure is
`Bᵀ`-mixed: for `Y = e_0 vᵀ ∈ W_{-1}`, the image is `(Bᵀ v)(A e_0)ᵀ`, which lies in `W_{-1}` for all
`v` only if `Bᵀ v ∈ C e_0` for all `v` — impossible. Hence **no element of `τH^0` preserves the
grading; `L ⊆ H^0` is connected and the B19-01 count is an `L`-invariant count.** The parent's §7
suggestion to add a "transposition component from `STABILIZER.md`" is withdrawn (CORRIGENDUM C1).
Transposition does act on `F^L` (it normalises `L`) and does give a valid *separate* refinement,
proved in §6.2; it is not part of `b_L`.

### 3.2 The invariant condition (PROVED)

`L` is the kernel of the primitive character `φ = αβc³(det g)²` of `GL_3 × (C*)³` (exponents
`(1,1,3,2)` have gcd 1, so `L` is connected and the characters of `GL_3 × (C*)³` trivial on `L` are
exactly the powers of `φ`). `L ⊇ SL_3`, and `S_ν(std)^{SL_3} ≠ 0` iff `ν = (m,m,m)` (then it is the line
`det^m`). So an irreducible `S_ν(std) ⊗ α^p β^q c^s` has `L`-invariants (one line) iff `ν = (m,m,m)` and
`α^p β^q c^s det^m = φ^k`, i.e. `(p,q,s,m) = k(1,1,3,2)`. On a component of `F` with adapted
multidegree `(#a, #r, #v, #c, #Σ)`: `p = #a + #r`, `q = #a + #c`, `s = #r + #v + #Σ`, and total degree
`20`; `p = q = k`, `s = 3k`, `20 = k + 3k` give `k = 5`: **`#a + #r = 5`, `#a + #c = 5`,
`#r + #v + #Σ = 15`, `GL_3`-type `det^{10}`** (consistent with B18-02 Lemma 4.1, which now follows
from `L`-invariance alone). In particular `|μ| = 5` is automatic for `L`-invariants, so `F^L` is the
same whether `F` is taken as "negative weight" or as "`#v ∈ {11,12}`".

### 3.3 Witness language (PROVED distinctions)

Three statements are kept apart throughout: (1) *existence* of `n ∈ ker C` (characteristic zero) with
`T(n) ≠ 0`; (2) an *explicit rational* such `n`; (3) that the *displayed modular candidate*
`n̄ = n02 − 265391 q_3 − 275398 q_7 ∈ F_P ⊗ M` is the reduction of such an `n`. The residues are not a
rational witness. Status after this session: (1) OPEN, (2) OPEN, (3) PROVED only conditionally on
`rank C|_S = 2` (Prop. 7.1). See CORRIGENDUM C3.

## 4. Plan, resources, stopping rules (pre-registered)

Pilot 1: `code/b_L_branching.py` under the Job Object wrapper (60 s / 512 MiB, one process, one
BLAS thread): exact `b_L` by (I) the B19-01 recipe and (II) an independent Kostka weight count, with
the controls of §5.2. Pilots 2–3 reserved for a refined target only if priced within the cap. Limits:
≤ 3 wrapped pilots, ≤ 180 s total, no contraction search, no source-vector evaluation.

## 5. Results (Part 2)

### 5.1 The exact count: `b_L = 74` (PROVED)

`results/b_L_branching.json`, tables in `results/b_L_tables.md`. Constituents with `c^λ_{μκτ} > 0`,
`|μ| = 5`, `#v ∈ {11, 12}` (`κ = (4,4,3)` or `(4,4,4)` — the only partitions of 11, 12 inside `(4,4,4)`):

| `#v` | `μ` | `κ` | `τ` | `c^λ_{μκτ}` | `dim S_μ(C⁴)·dim S_κ(C³)·dim S_τ(C⁹)` | `L`-invariants |
|---|---|---|---|---|---|---|
| 11 | (4,1) | (4,4,3) | (4) | 1 | 84·3·495 | 6 |
| 11 | (4,1) | (4,4,3) | (3,1) | 1 | 84·3·990 | 19 |
| 11 | (3,2) | (4,4,3) | (3,1) | 1 | 60·3·990 | 13 |
| 11 | (3,2) | (4,4,3) | (2,2) | 1 | 60·3·540 | 7 |
| 11 | (3,2) | (4,4,3) | (2,1,1) | 1 | 60·3·630 | 11 |
| 11 | (3,1,1) | (4,4,3) | (3,1) | 1 | 36·3·990 | 10 |
| 11 | (2,2,1) | (4,4,3) | (2,2) | 1 | 20·3·540 | 4 |
| 12 | (4,1) | (4,4,4) | (3) | 1 | 84·1·165 | 2 |
| 12 | (3,2) | (4,4,4) | (2,1) | 1 | 60·1·240 | 2 |

`b_L(11) = 70`, `b_L(12) = 4`, **`b_L = 74`**. Every LR coefficient was computed twice (alternant
extraction in five variables; combinatorial LR rule) and asserted equal. By adapted multidegree
(Formulation II, Kostka count with the `S_3` alternant; the `(10,10,10)`-weight-space dimension of
each graded piece is shown for scale):

| `#v` | `(#a, #r, #c, #Σ)` | weight-space dim | `L`-invariants |
|---|---|---|---|
| 11 | (1,4,4,0) | 396 | 7 |
| 11 | (2,3,3,1) | 1845 | 31 |
| 11 | (3,2,2,2) | 1812 | 28 |
| 11 | (4,1,1,3) | 318 | 4 |
| 12 | (2,3,3,0) | 33 | 1 |
| 12 | (3,2,2,1) | 66 | 2 |
| 12 | (4,1,1,2) | 18 | 1 |

Both formulations give `70 + 4 = 74`. The S0-slice part (`#Σ = 0`) alone has 8 invariants; the
parent's observed S0 rank 2 on twelve vectors is far below even that, and the full-row rank 2 on
`(q_3, q_7, n02)` is far below 74: the Levi target does not track `C(M)`.

`b_L = 74 ≥ 2` is consistent with the certified floor (no convention conflict); it is also weaker than
the trivial ceiling `4`, so the bound adds nothing to `rank C` (Case C).

### 5.2 Controls (all passed; `results/b_L_branching.json: checks`)

- **Graded decomposition identities** (complete, with dimensions): for `n = 11`:
  `Σ_{|κ|=n} c^λ_{μκτ} dim S_μ(C⁴) dim S_κ(C³) dim S_τ(C⁹)` over all 40 constituents `= 10,930,920`
  `= [u^{11}] s_λ(1^{13}, u, u, u)`; for `n = 12`: 15 constituents, `496,860`, equal. These validate the LR
  routine, the enumeration and `dim S_κ(C³) ∈ {3, 1}` exactly on the forbidden pieces.
- **Small full identity** `S_{(2,2)}(C¹ ⊕ C² ⊕ C³)`: `105 = dim S_{(2,2)}(C⁶)` (combinatorial LR).
- **Kostka routine**: `K_{(2,1),(1,1,1)} = 2`, `K_{λ,λ} = 1`, `K_{λ,(1^{20})} = 1,662,804 = 20!/∏hooks`.
- **Alternant/plethysm**: `S_{21}⊗S_{21} ∋ S_{222}` once; `S_2⊗S_2⊗S_2 ∋ S_{222}` once; `dim S_{21}(C³) = 8`;
  `c^{(4^5)}_{(4,4,4),(4,4)} = 1`, `c^{(4^5)}_{(4,4,4),(4,3,1)} = 0`, `c^{222}_{21,21} = 1` (both LR routines).
- Hand computation of `b_L(12) = 4` (per pattern `1 + 2 + 1`) done before the run agrees.

### 5.3 Resource ledger

| run | wrapped | exit | wall | peak job memory | note |
|---|---|---|---|---|---|
| `p1_b_L_branching` | yes | 124 | 60.0 s (cap) | see receipt | first version: all-triples identity with a slow coefficient scan; no output; receipt preserved (`results/logs/p1_*`) |
| unwrapped micro-test | no | 0 | 0.14 s | — | small-control functions only (`exec` of the module head); disclosed, counted |
| `p2_b_L_branching` | yes | 0 | 14.4 s | see receipt | the delivered computation |

Total numerical wall: `60.0 + 0.14 + 14.4 = 74.5 s` of 180 s; two of three wrapped pilots used; no
further pilot run (the refined target of §6 is not affordable in the remaining single pilot, §6.4).

## 6. A rigorously smaller target `F'' ⊆ F^L` (PROVED to contain `C(M)`; dimension NOT computed)

### 6.1 Pure equations from the whole stabilizer Lie algebra (PROVED)

Let `X ∈ gl(A) ⊕ gl(B)` act on functions by `(X·z)(Y) = d/dt|₀ z(exp(tX)·Y)`. For `z ∈ M`,
`X·z = 5 tr(X) z` (derivative of the character). Write the vector field of `X` as `v_X = Σ_j v_{X,j}`
with `v_{X,j}` homogeneous of `gamma`-weight `j ∈ [−2, 2]` (in adapted coordinates, e.g. left
multiplication by `E_{0k}` gives `c_k ∂_a + Σ_{kn} ∂_{r_n}` of weight `+2` and `v`-terms `∂_{r_n}` of
weight `+1`; the weight-0 parts of `Lie(L)` are the Levi operators). Decompose `z = Σ_w z_w`. Then for
every `w`: `Σ_j v_{X,j} z_{w−j} = 5 tr(X) z_w`. Let `j_0 = min{j : v_{X,j} ≠ 0}`. At `w = j_0 − 2` and
`w = j_0 − 1` the left side involves only `z_{−2}, z_{−1}`; whenever the right side is `0` or a forbidden
component (always when `w ≤ −1`, and when `tr X = 0`), the equation is a **linear constraint on
`C(z) = (z_{−2}, z_{−1})`**:

    v_{X,j_0} z_{−2} = 5 tr(X)·[w = −2]·z_{−2},        v_{X,j_0} z_{−1} + v_{X,j_0+1} z_{−2} = 5 tr(X)·(z_w, if w ∈ {−2,−1}).

Running over a basis of `gl_4 ⊕ gl_4` adapted to the weight filtration gives all such equations. For
`X ∈ Lie(L)` they are the `L`-invariance already imposed; for the 22 remaining basis directions (the
6 unipotent directions of `P_+`, the 6 of `P_−`, and the 10 block directions mixing `Σ` and `v`) they
are new. These are necessary conditions on `C(z)`, so `C(M) ⊆ F''_1 := {f ∈ F^L : all pure equations}`.

### 6.2 Transposition (PROVED)

`τ: Y ↦ Yᵀ` maps `(a, r, v, c, Σ) ↦ (a, c, −v, r, Σ)`, so it preserves the adapted multidegree pieces
with `#r = #c` — which by §3.2 contain `F^L` — and normalises `L`
(`τ(diag(α,g), diag(β, cgᵀ))τ^{−1} = (diag(β, cg), diag(α, gᵀ))`). Hence `τ` acts on `F^L_{−2}` and
`F^L_{−1}`. For `z ∈ M`, `z∘τ = z` and the `#v`-graded pieces with `#r = #c` are `τ`-stable, so
`z_{−2}∘τ = z_{−2}`, `z_{−1}∘τ = z_{−1}`: `C(M) ⊆ (F^L)^{τ}`. (Here `τ` coincides on `M` with the
`STABILIZER.md` element `τ' = (−I_5, I, I, τ)`, since `−I_5` acts trivially in degree 20.)

### 6.3 The refined target

`F'' := F''_1 ∩ (F^L)^{τ}`. **`C(M) ⊆ F''` and `rank C ≤ dim F'' ≤ b_L = 74`** (PROVED). `dim F''` is
NOT computed here. It is not a character computation: it is the kernel of explicit differential
operators on an explicit basis of the 74-dimensional space `F^L`.

### 6.4 Price of computing `dim F''` (ESTIMATE, not run)

1. An explicit spanning set of `F^L`: by the first fundamental theorem for `SL_3` and reductivity of
   `L`, `F^L` is spanned by complete `GL_3`-contractions (`δ`, `ε`) of adapted-coordinate slots
   (`a`, `r`, `v` as a covector with a `det` twist, `c`, `Σ`) arranged in four `5×5` determinants over the
   matrix index, with multidegrees from the second table of §5.1. Completeness is certified by a
   nonzero `74×74` modular minor of evaluations at 74 points (dimension count `b_L = 74`). New
   evaluator (adapted column tensors with typed slots; einsum over `≤ 20` indices of dimension 3),
   about 300 lines; runtime estimate `~35 s` for `~200` candidate patterns at `80` points.
2. The constraint matrix: directional derivatives of each basis vector along the weight components
   of the 32 basis vector fields (derivative column tensors, one row of the `5×5` determinant
   replaced), at 2–3 points, plus `τ` rows; estimate `~100 s`. The **sampled** kernel dimension `b''`
   satisfies `b'' ≥ dim F'' ≥ rank C` (sampling can only drop constraints), so it is a valid upper
   bound; over `F_P` it is again an upper bound (rank drops under reduction).
3. Validation: the coordinates of `C(q_3), C(q_7)` in the basis (from full-row evaluations at
   `≥ 4` general points, `≥ 26` further runner evaluations) must lie in the sampled kernel.
Total: about four to five wrapped pilots (`≈ 4` minutes) after an untested build — not affordable in
the one pilot remaining here, and not attempted. If `b'' = 2`, Case A follows at once (§7).

## 7. Conclusion (Part 3)

### 7.1 The justified conclusion: Case C

`b_L = 74 ≥ 4`: the Levi bound does not settle the comparison. Proved upper bound on `rank C`: `74`,
which is weaker than the known `rank C ≤ 4`. Proved lower bound: `2` (unchanged). Whether `T`
vanishes on all of `ker C` is OPEN. Nothing here is a multiplicity obstruction (`a = m_det = 1`).

### 7.2 What would suffice on the known three-vector subspace (PROVED, conditional)

Let `S = span(q_3, q_7, n02)` (certified 3-dimensional).

**Proposition 7.1.** Suppose `rank C|_S = 2`. Then: (i) `ker C ∩ S` is the line spanned by an exact
`n* = n02 − α* q_3 − β* q_7`, `α*, β* ∈ Q`; (ii) `(α*, β*) ≡ (265391, 275398) mod P`; (iii)
`C4_{S1,S2}(n*) ≠ 0` and `C4_{S1,S4}(n*) ≠ 0` over `Q`; hence `T` does not vanish on `ker C`, and the
displayed modular candidate is the reduction of an exact witness.

*Proof.* `C` is injective on `span(q_3, q_7)` (sealed E6), so under the hypothesis the kernel on `S`
is one-dimensional with nonzero `n02`-coefficient; normalise it to 1. Take the two recorded
forbidden-row functionals `φ_1, φ_2` at P7 point 0 (degrees 11, 12; integer-valued on `M`); the
determinant of `[φ_i(C q_j)]` is `104967 ≢ 0 mod P` (`results/injectivity_minors.json`; the full rows at
P6 point 0 give `171205 ≢ 0` as a second choice). Since `C(n*) = 0`, `φ_i(C n02) = α* φ_i(C q_3) + β* φ_i(C q_7)`
exactly, a `2×2` integer system with determinant `D ≢ 0 mod P`; its unique rational solution has
denominators dividing `D` and reduces mod `P` to the unique solution of the reduced system, which is
`(265391, 275398)` (the recorded relation, residuals 0). For an integer-valued functional `T` on `M`,
`D·T(n*) = D T(n02) − D_1 T(q_3) − D_2 T(q_7)` is an integer congruent to `D·T(n̄) mod P`, where
`T(n̄) := T(n02) − 265391 T(q_3) − 275398 T(q_7) mod P` equals `499917` and `487898` for the two
`C4` rows (parent certificates); both nonzero, so `T(n*) ≠ 0`. ∎

For `C2`, `C2(n̄) ≡ 0 mod P` proves nothing about `C2(n*)`. The hypothesis `rank C|_S = 2` is exactly
what the ten recorded sampled functionals suggest and what neither the Levi bound nor any
certificate proves; a proof needs `dim F'' = 2`, or a target of dimension 2 containing `C(S)`, or exact
multi-prime evaluation of the forbidden components on a spanning set of `F^L` (priced in the parent
as unaffordable).

### 7.3 Smallest next step

Compute `dim F''` (§6.4). If it is 2: `rank C = 2`, `dim ker C = 3`, `ker C ⊄ ker T`, Proposition 7.1
applies with no further evaluation, and the `C4` conditions are proved independent of the arc in this
cell (existentially, with a characterised but not explicitly rational witness). If it is 3: Case B
(`rank C ≤ 3`, the arc does not isolate `E`; the comparison with `T` needs Prop. 7.1's hypothesis).
If it is ≥ 4: the unipotent constraints are also insufficient and only exact arithmetic remains.
