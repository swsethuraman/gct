# B26-02: independent audit of the expander-tableau notes

**Registered outcome 1: ACCEPT, at the exact scope stated in §3. REVIEWER ONLY / UNCOMMITTED.**
This is a cross-lineage audit: Claude (Opus 5.5) reviewing notes that Astra (gpt-6-astra, Codex
session `01a0c159…`) produced. Zero pilots and zero programs. Every mathematical check below is a
hand derivation or a READ of committed bytes. No external source was read.

The notes' algebraic conclusions hold as stated:

- **Padding survival, every member.** The subdivided family survives on an explicit, literal
  actual-padding point.
- **Rejection, every individual member.** Each member is nonzero on an explicit literal
  determinant pencil that also lies in the normalized chart.
- **The invisible-direction identity** is exact.

I found no discrepancy in any load-bearing calculation. The achievement level is unchanged: the
family reaches neither a coefficient equation nor separation on padding. The binding constraint
stands: "No five-row determinant equation is known to be nonzero on padding."

## 0. Preflight and bindings

| item | observed |
|---|---|
| start (UTC) | 2026-09-22T23:41:26Z |
| worktree / branch | `work/batch15_workers/B15-02`, `b15-02-a1-probes` |
| HEAD | `9e12d7892734f6ec199da3b947e64f09704959d7`. This is exactly the expected value, not a descendant. |
| `git status --porcelain` | 4 pre-existing untracked files under `results/logs/` (`b15_02_runtime_*` `.pid` and `_resources.json`). Left alone. |
| output paths | `docs/b26_02_review.md` and `results/b26_02/` were both absent before writing |
| AGENTS.md / CLAUDE.md | none, either in the worktree or at the project root |
| `B26_COMMON.md` raw SHA-256 | `a22c91034244d48aae2be5c9f5ecb4337cff609cda1aaf08e593e497656a51fd` (matches the launch-protocol table) |
| `B26-02.md` raw SHA-256 | `1ad6bd6a966c8a419d9cacfed26b1660cb3c3ff4d6d49f7c9f304733ec2d1fbe` (matches the launch-protocol table) |
| `BATCH26_LIVE_LEDGER.md` raw SHA-256 | `9d24c37c5953c66583f199af3e8fc226e4feb9f7c70d412f2d4424594b47d2c8` |

Input hashes are listed in `results/b26_02/INPUT_BINDINGS.md`. Each is the SHA-256 of `git show`
output, which is the committed LF blob. Every hash matches the brief's prefix. The three notes, the
delivery note and the manifest contain no CR bytes, so blob = raw.

**Earlier byte states.** Note 3 cites note 2's pre-pointer state as `6bfebc9b…`. I reproduced that
hash exactly by deleting the follow-up paragraph (lines 6–10) from committed note 2. This was
administrative hashing, not mathematics, so the cited state is the committed text minus that
pointer. Note 2 cites note 1's pre-pointer state as `67d3d1cc…`. Deleting the pointer paragraphs
does **not** reproduce it; I tried five variants. That state is therefore **UNREAD**. It is not
load-bearing: I audit the tableau against committed note 1 §5, and note 2 §1 restates the same
tableau (duplicated star columns, n−4 singletons, shape `((10n−26)k,14k,4k,4k,4k)`).

## 1. Claim-by-claim certificate

The first version of this table is in `results/b26_02/CHECKPOINT.md`, written at 23:47Z. N1, N2
and N3 are notes 1–3, reviewed in supersession order.

| # | note § | statement | check | verdict |
|---|---|---|---|---|
| 1 | N1 §§2,5 | Content `d × n` with `d=10k`; `λ=((10n−26)k,14k,4k,4k,4k)`; a highest-weight function of shape `λ` when nonzero, with no semistandardness assumed | hand derivation | CONFIRMED |
| 2 | N1 §2, N2 §3, N3 §3 | Power-sum formula = symmetric-tensor contraction with `q=Σq_ijkl x_i x_j x_k x_l` (`q_1122=c/6`); `C_n(q)=(4!/n!)∂_{x1}^{n−4}q` | hand derivation | CONFIRMED |
| 3 | N2 §2 | `per_3(Y)=w·aᵀMb=wQ`; `z^{n−3}per_3(Y)=p_n`, a literal point of the actual padding parametrization | hand derivation; parametrization READ (B25-04 notation) | CONFIRMED |
| 4 | N2 §§3–6 | `f_{H,n}(p_n)=(12800/6561)^k α_n^{4k} β_n^{6k} Z_H`, with `Z_H ≥ 1` and no cancellation | hand derivation | CONFIRMED |
| 5 | N3 §2 | `det K=(af−be+cd)²`; `D_4=(A+B/2)²`; `D_n=z^{n−4}(A+B/2)²` in the literal pencil image and the normalized chart | hand derivation | CONFIRMED |
| 6 | N3 §3 | `f_{H,4}(q+h)=f_{H,4}(q)` for `h∈Sym⁴⟨x3,x4,x5⟩`; `h=B²/4`; general-`n` term `B²/[4·binom(n,4)]` | hand derivation | CONFIRMED |
| 7 | N3 §6 | Rejection of every individual member; nothing proved for linear combinations; the common pair cannot witness separation for any combination | hand derivation | CONFIRMED at the scope in §3 |
| C | typed | Classification of the cubic `wQ` | hand derivation | **neither** (§4) |

### 1.1 Derivations (hand)

**Item 1.** Let H have 2k vertices and 5k edges. Subdividing it gives 10k half-edge labels. The
columns are:

- two copies of each old-vertex star: 4k columns of height 5;
- two copies of each subdivision-vertex star: 10k columns of height 2;
- `10k(n−4)` singleton columns.

Each label lies in two stars, so it occurs 2+2+(n−4)=n times. No column repeats a label.

- `λ_1` is the column count, `4k+10k+10k(n−4)=(10n−26)k`.
- `λ_2` counts the columns of height at least 2, which is 14k. Likewise `λ_3=λ_4=λ_5=4k`.
- The sum is `10nk=nd`, and `λ_1≥λ_2` holds exactly when n≥4.

For the highest-weight property:

- A lower-unitriangular map on the evaluation vectors changes the top h coordinates by a
  unitriangular block. Each top-coordinate minor is therefore unchanged.
- The diagonal torus scales each column of height h by `t_1⋯t_h`. The exponent of `t_i` is then
  the number of columns of height at least i, which is `λ_i`.
- The argument never uses semistandardness.

For well-definedness, the multilinear contraction of the symmetric tensor is a polynomial in p.
On `p=Σℓ_j^n` it expands to the stated `Σ_φ Π det` formula. So I do not need BDI's
well-definedness statement.

**Item 2.** The tensor of `ℓ^4` is `ℓ^{⊗4}`, since `(Σℓ_i x_i)^4=Σℓ_iℓ_jℓ_kℓ_l x_i x_j x_k x_l`.
The coefficient `c` of `x1²x2²` is spread over `4!/(2!2!)=6` index tuples, so `q_1122=c/6`. This
convention is forced by the power-sum formula, so BDI's own normalization prose is not
load-bearing.

A singleton column is the top 1×1 minor, which is the first coordinate. Contracting m legs of
`ℓ^{⊗n}` with `e_1` leaves `ℓ_1^m ℓ^{⊗4}`, and `∂_{x1}^m ℓ^n=(n!/4!)ℓ_1^mℓ^4`. By linearity,
`f_{H,n}=f_{H,4}∘C_n`.

**Item 3.** `(J−I)(−I+J/2)=−J+J²/2+I−J/2=I`, using `J²=3J`. So `aᵀMb=aᵀc=zw+uv+t²=Q`, where
`u=x3+ix4`, `v=x3−ix4` and `t=x5`. `per Y=Σ_σ Y_{1σ1}Y_{2σ2}w=w·Σ_{i≠j}a_ib_j=w·aᵀMb`.

With padding coordinate z, `z^{n−3}wQ=z^{n−4}A(A+B)=p_n`. All ten inputs of `x_0^{n−3}per_3` are
linear forms in x1..x5 over Q(i). This is a literal point of the r=5 restriction image, `P_5` in
B25-04's notation. No product locus and no cubic-universality premise enters.

**Item 4.** Take `q=αA²+βAB`. Then:

- `q_1111=q_2222=α` and `q_1122=α/3`;
- `q_{aajj}=β/6` for `a∈{1,2}` and `j∈{3,4,5}`;
- every other entry is 0; in particular, entries with an odd number of V indices vanish.

Expanding in the orthonormal basis E0, E1, E2 gives exactly the stated M0, M1 and M2, with
`a0=4α/(3√2)`, `b0=2α/(3√2)` and `c0=β/(3√2)`.

At a subdivision vertex the metric is `K_rs=⟨E_r, εE_sεᵀ⟩`. For symmetric X, `εXεᵀ` swaps the
diagonal entries and negates the off-diagonal ones, so `K=diag(1,−1,−1)`. The two copies of a
column share one ordering, so the ordering signs cancel.

At an old vertex, `Σ_{i,j}ε_iε_jΠ_hN(i_h,j_h)=5!·det N`, where `N=Σy_rM_r`. This equals
`120c0³y0³(a0²y0²−b0²(y1²+y2²))`. `R` is symmetric in its five slots, so:

- `R0=120a0²c0³=160α²β³/(81√2)`;
- `R1=−120b0²c0³/binom(5,2)=−12b0²c0³`, hence `R1/R0=−(b0/a0)²/10=−1/40`;
- every other assignment gives 0.

The nonzero-colour edges therefore form a 2-regular subgraph F. Each cycle of F has one colour,
1 or 2. Its weight is `(−1/40)^{|V(F)|}(−1)^{|E(F)|}=40^{−|E(F)|}` because `|V(F)|=|E(F)|`.
Odd cycles are included. It follows that:

- `f_{H,4}(q)=R0^{2k}Z_H` and `R0²=(12800/6561)α⁴β⁶`;
- the empty configuration contributes 1 to `Z_H` and every term is positive, so `Z_H≥1` and
  nothing cancels.

For general n, write `m=n−4`. Then `∂_{x1}=∂_z+∂_w` and `p_n=z^{m+2}w²+z^{m+1}wB`. Every term of
`p_n` has weight m under `z→tz, w→w/t`. After s derivatives in w, a term has weight `2s∈{0,2,4}`.
The weight-0 part is `(24/n!)[(m+2)!/2·A²+(m+1)!·AB]`. This gives `α_n=12/[n(n−1)]` and
`β_n=24/[n(n−1)(n−2)]`.

The torus map is block-diagonal with determinant 1 on ⟨x1,x2⟩ and the identity on V. So every
height-5 and height-2 minor is invariant, and `f_{H,4}(q_n∘g_t)` is a polynomial in t that does
not depend on t. Setting t=0 gives the claim. At n=5, `(3/5,2/5)` checks directly against
`q_5=(3/5)A²+(2/5)AB+(1/5)z²(2A+B)`.

**Item 5.** `Pf=K12K34−K13K24+K14K23=zw−(u/2)(−v)+(t/2)t=A+B/2`. The lower triangle equals minus
the upper, entry by entry. So `D_4=A²+AB+B²/4`, `D_4−p_4=B²/4` and `D_n−p_n=z^mB²/4`.

The x1-coefficient matrix of K is `diag(J,J)` with `J=[[0,1],[−1,0]]`; only z and w involve x1.
With the `zI_m` block it becomes `diag(J,J,I_m)`, whose determinant is 1. Left-multiplying by its
inverse produces `x1I+Σ_{j≥2}x_jA_j` without changing the determinant. This is the chart used in
B25-04 §6 (READ).

**Item 6.** Every label sends exactly two legs into height-2 columns, and those use indices in
{1,2}. An `h∈Sym⁴(V)` has zero tensor entries whenever an index lies in {1,2}. Expand the
contraction of `q+h` multilinearly over labels: every term that uses h at some label vanishes.
The identity is therefore exact, not first-order.

`C_n(z^mB²/4)=(4!/n!)·m!·B²/4=B²/[4·binom(n,4)]`, which lies in `Sym⁴(V)`. `B=x3²+x4²+x5²` in both
notes (`uv+t²=x3²+x4²+x5²`). Hence `f_{H,n}(D_n)=f_{H,n}(p_n)>0`.

**Ancillary checks.** These are not items 1–7, but they sit on the same lines as the audited
claims.

- N1 §4, capacity no-go. The direct family has `λ_1=(5n−16)k<(n−3)d=(5n−15)k`, and the
  pigeonhole argument is sound. For the subdivided family, `λ_1−(n−3)d=4k`. CONFIRMED.
- N1 §6, colouring certificate. The Vandermonde product is 288. The new-vertex factors are 1 for
  c=0..3 and 16 for c=4, with each colour on k edges. So the summand is `288^{4k}16^k`. CONFIRMED.
- N3 §5, the K_{5,5} counts.
  - Cycles by length: 100, 600, 1800 and 1440.
  - Disjoint pairs: 450 pairs of 4-cycles and 600 pairs of a 4-cycle with a 6-cycle.
  - Hence `Z_0=1+200/40⁴+1200/40⁶+5400/40⁸+5280/40^{10}`, where `5400=2·1800+4·450` and
    `5280=2·1440+4·600`.
  - CONFIRMED.

## 2. Registered outcome

**Outcome 1, ACCEPT.** The algebraic conclusions hold at the scope of §3:

- padding survival for every member;
- rejection of every individual member;
- the invisible-direction identity.

No REPAIR is needed: no load-bearing calculation is wrong.

No DEFER applies. The one unread earlier byte state, note 1 at `67d3d1cc…`, is not load-bearing.
No external source is load-bearing: the notes' tensor convention is forced by the formula they
state, and I proved well-definedness and the highest-weight property by hand.

## 3. Exact scope

1. **Padding survival.** For every simple 5-regular seed graph H on 2k vertices, whether or not
   it is bipartite or an expander, and every n≥4, `f_{H,n}(p_n)>0`. Here
   `p_n=z^{n−3}·per_3(Y)` is the literal padding point of note 2 §2, over Q(i).
2. **Individual rejection.** For the same H and n, `f_{H,n}(D_n)=f_{H,n}(p_n)>0`, with `D_n` a
   literal n×n pencil in five variables. So `f_{H,n}∉I(D_5^{det_n})`. No individual member is a
   determinant equation.
3. **Linear combinations.** Take any g in the span of the `f_{H,n}` at fixed n and k, where the
   cell is fixed by k. Then `g(D_n)=g(p_n)`, by linearity of item 6. The same holds for any
   function that is blind to `Sym⁴(V)` after `C_n`. If such a g vanishes on `D_5^{det_n}`, then
   `g(p_n)=0`. **The old common padding/determinant pair (p_n, D_n) cannot witness separation for
   any combination that keeps this blindness.**

   The notes leave three questions open:
   - whether some nonzero combination lies in `I(D_5^{det_n})`;
   - if one does, whether it is nonzero at some other actual padding point;
   - anything about other column arrangements.
4. **Achievement level.** Of the four achievements, the family reaches neither a coefficient
   equation nor separation on padding. Padding nonvanishing is a necessary condition only. No
   multiplicity gap, noncontainment or lower bound is claimed.
5. **NOT REVIEWED (out of scope):** N1 §3 (the MSS 2-lift sequence and the Ramanujan property)
   and N1 §7 (the spectral gap, expansion and treewidth). None of items 1–7 uses them.

## 4. Classification of the witness cubic (typed; answered, not built on)

The cubic is `per_3(Y)=w·Q`, with `Q=x1²+⋯+x5²` of rank 5 and `w=x1−ix2`.

- **Not smooth.** It is reducible. As a hypersurface in P⁴ its singular locus is
  `{w=0,Q=0}`, a nonempty quadric-cone surface. So it is outside the smooth-cubic case. B17-01's
  general form is unreviewed; B26-01 is a delivered same-lineage review of it. **That result does
  not bear on this witness.**
- **Not the permanent of a symmetric 3×3 matrix of linear forms** (hand derivation). Write
  `Π=per[[α,β,γ],[β,δ,ε],[γ,ε,ζ]]=αδζ+αε²+δγ²+ζβ²+2βγε` on C⁶. The argument runs as follows.
  1. **The map must be injective.** Suppose `wQ=Π∘L` with `L:C⁵→C⁶` linear. `wQ` is not a
     cone: `∂_v(wQ)≡0` forces `w(v)=0` and then `B_Q(v,·)=0`, so `v=0`. Hence L is injective.
  2. **Π would contain a P³.** Then `{Π=0}` contains the P³ given by `{w=0}` inside `P(im L)`.
  3. **Consequence of containing a P³.** Suppose `Π⊃Λ≅P³`. Then `Π=ℓ1Q1+ℓ2Q2`, and
     `Sing Π∩Λ⊇V(Q1,Q2)∩Λ`, which has dimension at least 1.
  4. **The singular locus of Π.** Solving `∇Π=0`: if `αδζ≠0`, then `βγε=αδζ` and
     `(βγε)²=−(αδζ)²`, a contradiction. If `α=0`, then `β=γ=0` and `δζ+ε²=0`; the other two
     cases follow by symmetry. So `Sing Π` is three smooth conics, each spanning a coordinate
     plane `P_1=⟨δ,ζ,ε⟩`, `P_2=⟨α,ζ,γ⟩` or `P_3=⟨α,δ,β⟩`.
  5. **So Λ contains a plane.** By steps 3 and 4, Λ contains some conic and therefore its plane
     `P_i`.
  6. **Contradiction.** On `Λ=P_1+⟨v⟩` with `v=(α0,β0,γ0,0,0,0)≠0`,
     `Π|_Λ=sα0(δζ+ε²)+s²(β0²ζ+2β0γ0ε+γ0²δ)`. This is identically zero only if `v=0`. The cases
     `P_2` and `P_3` follow by the same symmetry.

  So `wQ` is not a symmetric permanent. `p_4=z·wQ` has only z and w as linear factors, up to
  scalars, and `zQ` fails the same way. So `p_4` is **not** in the literal family of A26-01's
  Theorem A, which is delivered at `7464a2bd` and **unreviewed**. I do not decide whether `p_4`
  lies in that family's closure. The question is moot, because note 3's rejection never uses
  `p_4∈D`.
- **Verdict: neither.** The cubic is reducible: a linear form times a smooth quadric. **Neither
  B26-01 nor A26-01 bears on this witness.** The rejection rests only on the explicit pencil
  `D_n≠p_n` together with the invisible-direction identity.

## 5. Source and method ledger

| source | label | use |
|---|---|---|
| Notes 1–3, delivery note, manifest @ `0d6f5a8c` | READ | objects under audit |
| Note 2's pre-pointer state `6bfebc9b…` | READ (reconstructed: committed note 2 minus lines 6–10) | the premise note 3 cites |
| Note 1's pre-pointer state `67d3d1cc…` | UNREAD | not load-bearing |
| B25-04 report @ `92a7d054` (§0 notation, §2.3, §6 chart) | READ | definitions of `P_r`, `D_r^{det_n}` and the normalized chart; quotation of BDI (5.2) |
| B25-04 scope erratum @ `9e12d789` | READ | context only |
| A26-01 report and PROOF @ `7464a2bd` | READ (delivered, **unreviewed**) | the scope of Theorem A for §4 only |
| A25-10 NEXT_ACTION @ `ab4f5271` | READ | "no construction ready" baseline, unchanged |
| B26-01 review / B17-01 general form | UNREAD (scope taken from `B26_COMMON.md`) | §4 classification only |
| BDI arXiv:2002.11594v2 §5, (5.2), L5.4, L6.5 | UNREAD (SECONDARY via B25-04's quotation) | not load-bearing |
| MSS, Gima et al. | UNREAD | out of scope (spectral claims) |
| every calculation in §1.1 and §4 | hand derivation | — |

## 6. Limitations

- These are hand checks only. No symbolic replay was run: the brief prohibits programs, and none
  was priced, because no step is in doubt.
- The global sign and orientation convention for the highest-weight property depends on whether
  the action is on vectors or on forms. This affects only the triangular convention, not
  nonvanishing.
- The spectral and expansion claims are NOT REVIEWED.
- In §4, the closure question for A26-01's family is left undecided.
- This is a single-reviewer, cross-lineage verdict. Acceptance by the record needs a delivery pass
  and the coordinator's reconciliation. This report is not an acceptance.

## 7. Resource receipt

Zero pilots, zero mathematical programs and zero compute lease. The administrative operations
were `git show`/`rev-parse`/`status`/`merge-base`/`ls-tree`, SHA-256 hashing (including the
pre-pointer reconstruction) and `date`. No Git mutations. The clock is in
`results/b26_02/RESOURCE_RECEIPT.md`.
