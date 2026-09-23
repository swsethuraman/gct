# B26-10A — independent cross-lineage review

**UNCOMMITTED / REVIEWER ONLY.** This session did not produce B26-04 or B26-02. The user authorized this slot directly. No other task, prior-session summary, or tool memory is evidence.

**Registered verdicts: Part 1 ACCEPT; Part 2 ACCEPT, at the scopes below.** Part 1 accepts the quartic transfer certificate and independently supplies the generality needed by Paper 2's other degree-four uses. The recommended consequence for the length-restriction flag is **remove it**, after separate delivery and adjudication; the paper is not edited. Part 2 accepts the classification argument with "singular locus" understood as the reduced geometric locus. The Jacobian scheme is not reduced at the conics' intersections, and no scheme-theoretic reducedness is accepted.

**Achievement levels:** a transfer lemma and a literal-family classification. This review constructs no source condition, coefficient equation, padding separator, positive multiplicity gap or asymptotic bound. LMR supplies an existing ideal-copy existence statement; accepting its transport does not establish any of the subsequent numerical or padding claims. **No five-row determinant equation is known to be nonzero on padding.**

## 0. Incremental preflight record

First tool-recorded UTC start after reading the two briefs: **2026-09-23 02:43:59 UTC**. Brief-reading preceded this timestamp; no substantive mathematics or writes preceded it. The 60-minute substantive ceiling and 30-minute checkpoint are measured conservatively from this time without deductions for interleaved administration.

Administrative observations (raw working-copy hashes, not mathematical premises):

| File | SHA-256 of raw working-copy bytes |
|---|---|
| `batch26_launch/B26_COMMON.md` | `a22c91034244d48aae2be5c9f5ecb4337cff609cda1aaf08e593e497656a51fd` |
| `batch26_launch/B26-10A.md` | `b0c8e755c61020a41ad4dfa3cde1c6ca751a15a6683ee0474f811c591f082474` |
| `BATCH26_LIVE_LEDGER.md` | `8260cd3772c5208960b941d6243962e0e42012317f173dc48c68f28ac231de14` |

The handover base is `Claude_Handover_B15_B18/post_b19_housekeeping_20260917/` under the project root.

- Assigned worktree: `work/batch15_workers/B15-01`; branch **b15-01-ci159**; HEAD **65736d9f9b27ae508697c87f306f494760e87007**, exactly as required. No descendant exception is needed.
- Default `git status --porcelain`: **10,383 entries, all untracked**; no tracked or staged changes. The more detailed `--untracked-files=all` expands the same inventory to 20,761 individual files. This is an enumeration difference, not a baseline discrepancy.
- Both assigned output paths were absent. No applicable `AGENTS.md` or `CLAUDE.md` was found on the directory ancestry or in the output directories.
- The sandbox account initially triggered Git ownership protection. Read-only commands then used a command-scoped `-c safe.directory=...` for this user-designated worktree. No persistent configuration, ownership, index or Git content was changed. Git warned that the global ignore file was unreadable; default status nevertheless matches the brief's 10,383 entries.
- All seven explicitly pinned input blobs resolve. Fresh SHA-256 checks match all supplied prefixes: B26-04 report `9d61f5e2...`, its manifest `ee7805c8...`, and Paper 2 `065f8799...`. The paper's hash names the committed **CRLF** blob; the six other pinned inputs are **LF** blobs.
- Preflight completed without a mismatch at **2026-09-23 02:44:34 UTC**. All existing files are left alone.

## 1. Incremental review record

**2026-09-23 02:46:01 UTC:** READ the committed B26-04 certificate and manifest, B25-05 Lemma R, B25-10 section 2, the relevant Paper 2 passages, B26-02 section 4 and B26-05's flag-scope observation. READ the original isotypic-rank proof and B17-03's quartic restriction lemmas. The quartic R1–R6 checks and the reduced three-conic singular-locus calculation are provisionally sound by hand derivation. The broader flag scope and primary LMR dependency remain under review. No final verdict is recorded in this checkpoint.

No 30-minute checkpoint has yet been reached. Zero pilots; zero mathematical programs; no compute lease, subagents or other sessions.

## 2. Part 1: object and independent quartic proof

### 2.1 The objects agree — ACCEPT

**READ:** Paper 2 at `79b68dcf7597e3b0efa63984327ad9f34e5bf74d:paper/det4-onset.tex`, lines 112–117 and 251–262; B25-05 section A.3; B26-04 sections 3–4. Paper line numbers count the committed CRLF blob without altering its bytes.

**Hand derivation:** Identify `V₁₆=M₄(C)`. A linear map `T:C⁹→V₁₆` is exactly a tuple of nine matrices `Aᵢ=T(eᵢ)`, and
`Φ_det₄(T)(s)=det₄(Σᵢ sᵢAᵢ)`. All tuples occur, including dependent ones. Taking Zariski closures gives precisely Paper 2's `D₉=X₉`. This is an affine coefficient-space closure; it is not assumed to be a single orbit closure.

### 2.2 R1–R6 at degree four — ACCEPT, each step

**READ inputs:** B25-05 section A.3 (R1–R6); `82633a60:docs/isotypic_rank.md`, sections 1–3; `0cce6172:docs/b17_03_report.md`, coefficient convention and Lemmas 1–2. The following is an independent **hand derivation**, not an appeal to B25-10's cubic ruling.

Work over C. Put `W_N=Sym⁴(V_N*)`, with action on forms `(g·F)(v)=F(g⁻¹v)`. Coefficient polynomials carry the dual action `(g·h)(F)=h(g⁻¹·F)`. Write `c_α(F)=[y^α]F`, where `|α|=4`. Let `ρ:W₁₆→W₉` restrict to the first nine coordinates. Its pullback sends `c_α` to `c_(α,0⁷)`. The cell is `δ=24, λ=(65,17,2⁷)`.

For a diagonal torus element `t`, `t·c_α=t^α c_α`. For `g=I+tE_ij`, the coefficient action extracts coefficients from `F(gy)=F(y+t y_j e_i)`. Thus

`E_ij c_α = (α_i+1)c_(α+e_i−e_j)` if `α_j>0`, and zero if `α_j=0`.

This is the action on ordinary quartic coefficients, extended to products as a derivation. No factorial-rescaled tensor coefficients are substituted. The positive sign comes from the dual action on functions.

1. **R1, weight support.** A coefficient monomial of degree 24 has weight equal to the sum of 24 nonnegative multi-indices of size four. If its total weight has zero coordinates 10–16, every factor has zero coordinates there. Thus the weight-`(λ,0⁷)` space is exactly the pullback of the nine-variable weight-`λ` space. Pullback is injective because it includes a polynomial subring.
2. **R2, highest-weight spaces.** For `i<9`, `E_(i,i+1)` commutes with pullback. For `9≤i<16`, each included coefficient has `α_(i+1)=0`, so the operator kills it and every product. The simultaneous raising kernels therefore identify in both directions: `H¹⁶_(24,(λ,0⁷))=ρ*H⁹_(24,λ)`. Equality at the boundary `ℓ(λ)=9` causes no loss.
3. **R3, evaluation identity.** Restriction substitutes `y₁₀=⋯=y₁₆=0`. Consequently `c_α(ρF)=c_(α,0⁷)(F)`. For every polynomial `h̄` and every quartic `F`, `(ρ*h̄)(F)=h̄(ρF)`. This is an identity on the entire ambient space, not a statement about sampled pencils.
4. **R4, closure of the orbit image.** For `g∈GL₁₆`, `ρ(g·det₄)(s)=det₄(Σᵢsᵢg⁻¹eᵢ)`. Such tuples range over all independent nine-tuples, because every independent tuple extends to a basis of `V₁₆`. They form a nonempty dense open subset of `V₁₆⁹`. The map `Φ` is polynomial, with coefficients quartic in the entries of `T`. For any coefficient polynomial `q`, vanishing of `q∘Φ` on this open set is equivalent to vanishing on all tuples. Hence `closure(ρ(GL₁₆·det₄))=X₉`. Also `closure(ρ(closure(GL₁₆·det₄)))=X₉`, by testing `q∘ρ` on the dense orbit. Neither assertion assumes that a closed set has closed image.
5. **R5, ideal kernels.** Let `X=closure(GL₁₆·det₄)` and `h=ρ*h̄` in the identified highest-weight space. Then `h∈I(X)` iff `h` vanishes on the orbit, iff `h̄` vanishes on its restriction (R3), iff `h̄∈I(X₉)` (R4). Thus `ρ*(K_X₉)=K_X`. No dense-orbit hypothesis on `X₉` is used.
6. **R6, cones and multiplicities.** Precomposition of `T` by `GL₉` preserves the pencil family. For every `c≠0` choose `t∈C` with `t⁴=c`; then `Φ(tT)=cΦ(T)`, and `T=0` gives zero. Thus `X₉` is a `GL₉`-stable closed cone. On `X`, the scalar `tI∈GL₁₆` acts on the determinant by `t⁻⁴`, again covering every nonzero scalar; zero lies in the closure. Homogeneous ideals and characteristic-zero complete reducibility give `I∩M_λ=S_λ⊗U`. Its highest-weight line identifies `U` with `K`, so `i=dim K` and `m=a−i`. R2 and R5 yield `a₁₆=a₉`, `i_X=i_X₉` and `m_X=m_X₉`.

The hypotheses are exactly `d=4`, `N=16`, `r=9≤16`, `ℓ(λ)=9≤r` and `|λ|=65+17+14=96=4δ`. Fourth roots are taken in C; complete reducibility uses characteristic zero. This establishes the certificate directly at degree four.

### 2.3 Scope extension needed for the flag audit

**Hand derivation:** The same proof works for any quartic `f∈Sym⁴((C¹⁶)*)`, any `1≤r≤16`, any `δ≥0` and `λ⊢4δ` with `ℓ(λ)≤r`. In R1 replace 24 by `δ` and nine by `r`; R2 has boundary `i=r`; R3 is the same coefficient identity. In R4 full-rank `16×r` matrices are dense and extend to invertible `16×16` matrices. In R6 `f(tT)=t⁴f(T)`. Degree zero is immediate from constants. Thus pullback identifies the highest-weight spaces and ideal kernels for `closure(GL₁₆·f)` and `closure{f∘T}`, and equates their same-cell multiplicities.

For `f=x₀per₃`, embed its ten independent coordinates in `(C¹⁶)*`. An arbitrary `T` specifies the ten linear forms `ℓ,B₁₁,…,B₃₃` independently; the other six coordinate forms may be zero. The restricted closure is exactly `closure{ℓ·per₃(B)}=P_r`. R4 covers these possibly noninjective substitutions by density. The proof does not replace the permanent factor with an arbitrary cubic.

**Scope distinction:** B26-04's stated ruling is only the determinant cell `(4,16,9;24,λ)` and expressly declines a ruling on `P_r`. That conclusion alone does not justify every unflagged use. The general degree-four statement and the `P_r` identification just proved are this review's explicit extension of its proof, within the requested flag audit.

## 3. Weight, primary dependency and wording

### 3.1 Weight conversion and conventions — ACCEPT

**READ:** Paper 2 lines 1054–1059 and 1071–1075, B26-04 section 5. **Hand derivation:** at `k=6,d=4` the displayed `Ω(k,d)` has coefficients `3·2·8=48`, `4·8−12−5=15`, and 2 on `ω₉`. Its degree is `8·3=24`. Add the fundamental-weight partitions `(48)+(15,15)+(2⁹)` to obtain `(65,17,2⁷,0⁷)`, of size 96. A determinant twist adds a constant to all 16 parts; the prescribed size 96 forces that constant to be zero.

**READ + hand derivation:** Paper 2's explicit coefficient module is `Sym²⁴(Sym⁴ C⁹)`; its `u=c_(4,0,…,0)` shifts the first weight by four; line 798 uses raising-operator kernels. These agree with Lemma R's positive coefficient weights. Although the paper suppresses dual symbols in some descriptions of the space of forms, its point-of-use coefficient representation agrees. Scalars act on this degree-24 coefficient space by `t⁹⁶`, so an `SL₁₆` submodule is `GL₁₆`-stable with the unique partition above. No dual or transpose is needed.

### 3.2 Precisely what is required from LMR — PRIMARY at statement level

**PRIMARY:** Landsberg–Manivel–Ressayre, [arXiv:1004.4802v1](https://arxiv.org/pdf/1004.4802v1), 27 April 2010. I read Theorem 2.3.1 and its setup on printed page 4, section 3.1 on page 5, and Theorem 3.1.1 with its following paragraph on page 6, using extracted text and rendered pages of the archived PDF. The **raw binary PDF** has **180,675 bytes**, SHA-256 **cfc28275a8c6b27f0ad6946d495ed4f889f7617df479be943d8d35718dbf2d79**.

The required external content is a **nonzero copy** of the `Ω(6,4)` module in coefficient degree 24, vanishing on the projective determinant orbit closure. Theorem 2.3.1 supplies the equation module; section 3.1 identifies the determinant's dual as the Segre of dimension six; Theorem 3.1.1 supplies the determinant component. Its stronger smoothness statement is unnecessary. Full proofs are not audited. I do not use Theorem 1.0.2's smaller printed coefficient/degree or section 3.2's general weight display, whose first coefficient disagrees with Theorem 2.3.1. The journal version is **UNREAD**.

**Hand derivation:** R6 makes `X=closure(GL₁₆·det₄)` the affine cone over its projective counterpart, so the homogeneous equations vanish on `X`. A nonzero module copy has a nonzero highest-weight line; the R1–R5 isomorphism carries it nontrivially into `I(D₉)`. Thus **`i_det(λ,24)≥1`**, with the specified external input. This yields neither an upper bound of one nor padding nonvanishing.

### 3.3 Complete flag inventory — remove the length-restriction flag

**READ:** all of Paper 2 section 2 (249–282), every occurrence of `eq:lengthred` in the pinned paper, and B26-05 section 5. The brief's wording about uses "in section 2" is addressed literally and through every downstream reference, including line 888, which B26-05's short list omits.

| Paper locator | Unflagged degree-four assertion/use | Covered by B26-04's expressly stated cell alone? | This review's ruling |
|---|---|---|---|
| 251–259, section 2 | General orbit-closure/restricted-closure multiplicity equality, for both named quartics | Only its determinant `r=9,δ=24,λ` instance | ACCEPT by section 2.3 for `1≤r≤16,ℓ(λ)≤r`, every degree |
| 260–261, section 2 | Restricted determinant closure is `D_r` | Explicitly `D₉` only | ACCEPT for all stated `r`, by tuples and density |
| 261–262, section 2 | Restricted padded-permanent closure is `P_r` | No; its ruling expressly excludes this clause | ACCEPT via the ten independent coordinate forms |
| 705–706, cap-theorem proof | Lifts determinant ideal modules from five variables to the orbit closure | No; `r=5`, potentially several weights | ACCEPT for the `n=4` transfer: decompose the finite-degree `GL₅`-stable span into highest-weight lines and apply section 2.3 |
| 860–861, negative-results notation | Both families' multiplicities equal their 16-variable orbit-closure versions | Only the named determinant cell; not the two-family assertion | ACCEPT for admissible lengths and degrees, both sides |
| 888–894, short-slab proof | Both families are seen at `k≤4` | No | ACCEPT for this transport; the subsequent washout/containment premises are not re-reviewed |
| 1060–1063, length-nine paragraph | The goal-cell determinant copy transfers; this occurrence is flagged | Yes | ACCEPT; **remove this transfer flag** after separate delivery/adjudication |

**READ:** lines 105–122 also summarize the reduction without a flag. **Hand derivation:** this summary is covered by section 2.3. There are no further `eq:lengthred` references. The dimension proposition at 264–282 is not another explicit use and is not being re-certified. This review does not certify other inputs to the cap theorem or any `n≠4` instance.

**Consequence:** **remove** the length-restriction flag because the explicit general degree-four proof covers all of these uses. Merely accepting B26-04's single-cell conclusion would not suffice. This recommendation clears only this transfer issue, not unrelated claims or paper readiness; no paper edit is authorized or made by this review.

### 3.4 B26-04 section 7's replacement — ACCEPT at its stated scope

**READ + hand derivation:** Its proposed replacement is accurate for `D₉`: the object, weight support, raising operators, density and complete reducibility all check out. Its "same proof" reference now has an explicit quartic check, including fourth roots. Its concluding attribution means that the ideal-copy floor depends only on LMR **beyond the proved internal transfer and standard representation theory**. LMR alone is not asserted to prove transfer or an exact multiplicity.

An optional sharper replacement (**proposal only; hand derivation with the PRIMARY dependency above**) is:

> The length-restriction lemma identifies the highest-weight spaces and their ideal subspaces for the sixteen-variable determinant orbit closure and its nine-variable pencil closure D₉. Hence the LMR ideal copy transfers nontrivially at (λ,δ)=((65,17,2⁷),24), proving i_det≥1. This uses LMR Theorem 2.3.1 with section 3.1 and Theorem 3.1.1; it supplies no upper bound or padding-separation assertion.

For section 2's general equation, cite the general degree-four statement in section 2.3 of this review, not only the single-cell verdict. Retain the name "the length-restriction lemma."

## 4. Part 2: classification of the cubic — ACCEPT

**READ:** `cdf6839cd81031d42e43dc640b08e2746a7ef22c:docs/b26_02_review.md`, section 4. Everything in the proof below is a **hand derivation** over C for homogeneous linear substitutions, including all changes of variables.

### 4.1 Full singular-locus calculation (step 4)

The symmetric permanent is

`Π=αδζ+αε²+δγ²+ζβ²+2βγε`.

The six gradient equations, with the last three divided by two, are

- `δζ+ε²=0`,
- `αζ+γ²=0`,
- `αδ+β²=0`,
- `ζβ+γε=0`,
- `δγ+βε=0`,
- `αε+βγ=0`.

Euler's identity implies that every nonzero solution lies on `Π=0`.

If `αδζ≠0`, the first three equations give
`(βγε)²=(−αδ)(−αζ)(−δζ)=−(αδζ)²`.
Multiplying `ζβ+γε=0` by `β` and using `β²=−αδ` gives `βγε=αδζ`. These contradict each other in characteristic zero with nonzero product. At least one diagonal coordinate must vanish.

If `α=0`, the second and third equations force `γ=β=0`, and all the remaining equations reduce to `δζ+ε²=0`. The two other cases follow by simultaneous row and column permutations of the symmetric matrix. Conversely, every point of each conic below satisfies all six equations:

| Component | Equations in P⁵ | Spanning coordinate plane |
|---|---|---|
| `C₁` | `α=β=γ=0, δζ+ε²=0` | `⟨δ,ζ,ε⟩` |
| `C₂` | `δ=β=ε=0, αζ+γ²=0` | `⟨α,ζ,γ⟩` |
| `C₃` | `ζ=γ=ε=0, αδ+β²=0` | `⟨α,δ,β⟩` |

The plane gradient of `δζ+ε²` is `(ζ,δ,2ε)`, nonzero at every projective point on `C₁`. Thus `C₁` is smooth and spans its plane; the others are identical by symmetry. These are three distinct irreducible components with no extra isolated points in the reduced locus. They meet pairwise at the three diagonal-coordinate points: they are not disjoint, and their union is not smooth.

**Necessary scheme precision:** this proves
`Sing(V(Π))_red=C₁∪C₂∪C₃`.
The Jacobian scheme is not the reduced union. On `ζ=1`, eliminate
`δ=−ε², α=−γ², β=−γε`.
The remaining ideal in `C[γ,ε]` is `(γ²ε,γε²)`, with radical `(γε)`. The class of `γε` is nonzero and has square zero. The classification uses only reduced supports and dimensions, so this distinction does not undermine it.

### 4.2 Steps 1–3 and 5–6, confirmed independently

1. **Injectivity (step 1).** Let `F=wQ`, `Q=x₁²+⋯+x₅²` of rank five and `w=x₁−ix₂`. If `∂_vF=0` for a constant vector `v`, then `w(v)Q+w∂_vQ=0`. The irreducible quadric `Q` is not divisible by `w`. Reduction modulo `w` forces `w(v)=0`, then `∂_vQ=0`. Nondegeneracy forces `v=0`. If `F=Π∘L`, every vector in `ker L` would satisfy this identity. Thus `L:C⁵→C⁶` is injective.
2. **A three-plane (step 2).** The four-dimensional vector hyperplane `ker w` maps injectively into `Π=0`. Its projectivization is `Λ≅P³⊂V(Π)⊂P⁵`.
3. **A singular curve (step 3).** If `Λ=V(ℓ₁,ℓ₂)` lies in this cubic, then `Π=ℓ₁Q₁+ℓ₂Q₂` for quadrics `Qᵢ`. Along `Λ`, `dΠ=Q₁dℓ₁+Q₂dℓ₂`, so `V(Q₁,Q₂)∩Λ⊂Sing(V(Π))∩Λ`. Two homogeneous quadrics in P³ have a nonempty common zero set of dimension at least one: their ideal has height at most two in four variables. This includes dependent or zero quadrics.
4. **Containing a conic's plane (step 5).** A positive-dimensional closed subset of the finite union `C₁∪C₂∪C₃` contains a whole conic, since a proper closed subset of an irreducible curve is finite. Thus `Λ` contains one `Cᵢ` and its spanning plane `Pᵢ`.
5. **Contradiction (step 6).** By symmetry take `Pᵢ=P₁`. Modulo that plane's vector span, choose an extra vector `v=(α₀,β₀,γ₀,0,0,0)≠0`. On the vector space above `Λ`,
   `Π|_Λ=sα₀(δζ+ε²)+s²(β₀²ζ+2β₀γ₀ε+γ₀²δ)`.
   Identical vanishing forces `α₀=0` from the coefficient of `sδζ`, then `β₀=γ₀=0` from the coefficients of `s²ζ` and `s²δ`. This contradicts `v≠0`.

Therefore `V(Π)` contains no P³, and **`wQ` is not a symmetric permanent**.

### 4.3 Exact classification scope

**Hand derivation:** `wQ` is singular and reducible, hence outside the smooth-cubic class. Its reduced singular locus is `V(w,Q)`: if `w≠0` and `wQ=0` at a projective point, then `Q=0` and `d(wQ)=w dQ≠0`. With `z=x₁+ix₂`, we have `Q=zw+x₃²+x₄²+x₅²`; the intersection `w=Q=0` is the nonempty quadric-cone surface asserted in B26-02.

The argument also excludes `zQ`. As `Q` is irreducible, the only linear factors of `p₄=zwQ` are `z,w` up to scalars. Removing a linear padding factor cannot leave a symmetric permanent. This confirms the **literal-family** classification without using A26-01's theorem or B17-01. It supplies no exclusion from the **closure** of the symmetric-padding family.

**Registered Part 2 outcome: ACCEPT.** The reduced singular-locus statement and all six classification steps are valid. No load-bearing repair or missing source remains. An explicit assertion that the Jacobian scheme is reduced would instead require the narrower wording in section 4.1.

## 5. Source/method ledger and limitations

Claims are labelled at their points of use. `results/b26_10a/INPUT_BINDINGS.json` records full resolved commits, SHA-256 of exact blob bytes, byte counts, line endings and read extents. Hashing a complete file is not a claim to have read every section.

| Source or method | Label for this review | Scope |
|---|---|---|
| B26-04 report and manifest at its pin | READ | Object, proof, conventions, dependency, proposed wording and provenance |
| B25-05 section A, especially A.3–A.5 | READ | Lemma R and proof-file lineage |
| B25-10 section 2 | READ | Prior cubic ruling and the quartic residue |
| Isotypic-rank sections 1–3; B17-03 convention and Lemmas 1–2 | READ | Original proofs and coefficient conventions |
| s73 section 1; s26 review sections 1–4; reducible-ideal Corollary D | READ | Historical use and terminology only; no measurements imported |
| Paper 2 locators above | READ | Exact objects, conventions, source dependency and complete flag inventory |
| B26-05 section 5 | READ | Observation independently checked against Paper 2 |
| B26-02 section 4 | READ | Classification under review |
| Archived LMR v1 at the locators in section 3.2 | PRIMARY, statements | External ideal-copy premise; full proofs not audited |
| Older packets' accounts of their LMR reading | SECONDARY | Leads only, superseded by direct reading |
| LMR journal version; Paper 1 Proposition 4.19 | UNREAD | Not needed for the independently derived transfer |
| Sections 2, 3.1, conversion after 3.2, and section 4 | hand derivation | No mathematical executable, pilot, search or replay |

Background used: characteristic-zero finite-dimensional representation theory, polynomial vanishing on dense subsets, polynomial-ring height/dimension, and elementary projective geometry. Complete reducibility identifies multiplicity spaces, not full representations of different general linear groups. No restricted pencil closure is assumed to have a dense orbit.

This is an independent cross-lineage review in a new session, not a blind review: the assigned reports were read before the re-derivations. This session produced neither reviewed packet and contacted no other session.

Out of scope: LMR's full proofs; rank 273, ambient dimension 274 and later kernel/padding assertions in Paper 2; finite-point certificates; other cap-theorem inputs; washout/containment proofs; the expander construction beyond its classification; reducedness of the Jacobian scheme; closure exclusion for symmetric padding; new research or numerical tests. No accepted wording clears those claims by implication. The two scoped verdicts have no remaining missing lemma and require no proposed computation.

Standing boundaries remain: C45's reviewed base rung is unpadded `n=3`, `(19,7,2⁵),δ=12,D=+1`, with higher rungs on their s73 lineage; Application 3's ceiling is proved and floor CERTIFIED-modular at one prime; A25-10's programme decision remains "no construction ready." No unrelated status changes here.

## 6. Resource and delivery record

**Zero pilots; zero mathematical programs; no compute lease.** All mathematical expansions, case splits, weight conversions and proofs were done by hand. Administrative executables performed only Git reads, inventory, UTC clock reads, hashes, PDF retrieval/extraction/rendering, and packet authoring/verification. Python was used for PDF text extraction and administrative receipts, never symbolic or numerical mathematics. No dependencies were installed.

The initial sandboxed public PDF download failed because sockets were restricted. The same download into the authorized output directory succeeded through the normal approval mechanism. Local PDF extraction initially met an output-encoding error; UTF-8 output resolved it. These were administrative retries, not mathematical experiments or substantive interruptions. The downloaded PDF is unedited. Temporary page renders were inspected and removed from this slot's own output directory. An authoring escape error in the first report draft was corrected before sealing; final text is checked for stray control characters.

Completion times, the early-final checkpoint in place of an unreached 30-minute checkpoint, and final inventory checks follow below and in `results/b26_10a/resource_receipt.json`. No waiting to consume the ceiling, automatic continuation, staging, commit, push, fetch, checkout, reset, branch/worktree creation, paper edit, historical-packet edit or ledger edit occurred.

The packet contains this report, input bindings, an administrative sealing script, a resource receipt, the exact source PDF, and the proposed delivery list. `MANIFEST.json` binds every payload's **raw SHA-256 and byte count**, excluding itself. `PROPOSED_DELIVERY_PATHS.txt` lists payloads plus manifest. **All remains UNCOMMITTED / REVIEWER ONLY pending a separately authorized delivery pass.**

### Final clock and verification

- **Substantive stop / early-final checkpoint:** 2026-09-23T02:54:01Z. Elapsed time from the recorded start: **10m02s**, including interleaved administration; no interruption deductions. The 30-minute checkpoint was not reached.
- **Packet administrative close:** 2026-09-23T02:55:39Z.
- Final read-only checks: branch and HEAD unchanged; zero tracked/staged changes; the pre-existing inventory remains 10,383 default-status entries / 20,761 individual files. These counts are inventory checks, not a fresh hash audit of every unrelated file.
- All twelve committed input bindings and the three preflight administrative hashes were rechecked; all six payloads are bound by the manifest, and the seven-path delivery list matches exactly. Every packet path is untracked.
- **Part 1 ACCEPT; Part 2 ACCEPT**, with the scope and source limitations above. Recommended flag action: **remove the length-restriction flag** after separate delivery/adjudication. No paper edit was made.
