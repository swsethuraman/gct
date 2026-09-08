# Batch 12 S1 — partial straightening and evaluation of ladder births

**Frozen research result, 8 September 2026.** This is an S1 research report and executable fallback, not a launch plan. Canonical documents and the shared checkout were not edited. The full 274-vector target basis and both target ranks remain **OPEN**.

## Result and preregistration

**PROVED:** restriction to the hyperplane where the leading coefficient vanishes realizes the ladder birth quotient exactly. It replaces elimination against the transported old source by direct evaluation of birth classes. For the specified n=4 ladder, the retained row dimension is at most 54, and is one at each of the last two rungs. The proof does not assume a full source basis or a compact Pieri operator.

**PROVED:** signed column normalization, pure-leading-coefficient factor removal, an unshared-column vanishing test, and a terminating Plücker straightening subsystem for the fifteen short columns. Each rule preserves the represented polynomial, or expresses it as an explicitly signed linear combination of valid circuits.

**KILL as a target basis strategy:** unrestricted expansion using this Plücker subsystem. Every one of the 113 saved target fillings exceeded the deliberately small 64-term working cap under the specified reducer. This demonstrates a failure of this implementation budget, not a carrier-scale lower bound or a mathematical impossibility. There is no triangular independence theorem after the umbral contraction and identical-letter symmetrization.

**Working hypothesis stated before the experiments:** exact filling relations and ladder birth selection materially reduce the rare-direction sampling tail. Acceptance required preservation proofs, termination, valid independence evidence, both controls, and measured improvement. The strong claim of eliminating the rare-direction tail is **NOT ESTABLISHED**. The narrower reduction in evaluation and elimination work is established structurally and benchmarked on controlled data. Candidate discovery remains unresolved.

The deliverables include both control matrices, retained minors, exact point data, executable evaluators, a compact relations example, a bounded matched-candidate benchmark, and an integrator relay. Detailed numerical results and timings are in `run_results.md`; JSON artifacts are authoritative for matrix entries and zero-based indices.

The fresh degree-13 replay certifies eight birth classes. Together with the two seed vectors and the proved ladder injection, these give **ten independent, evaluation-ready target source vectors**, supplied in `partial_source_10.json`. The seed determinant minor transports to a target determinant lower bound **two**, recorded explicitly. Neither statement completes the 274-dimensional source or the target determinant/padded decision.

## Input inventory and preflight

All four user-designated canonical sources were read: `Batch12_Reconciled_Final_Proposal.docx` (including S1 and section 4), `batch11_final_stocktake.md`, `stocktake_batch11.md`, and the complete `GCT_Comprehensive_Session_Source.md`. The entire S1 brief, shared requirements, frozen rank protocol, and launch packet were read. The DOCX text was extracted directly from its WordprocessingML; the extracted text is included. The finalized proposal and S1 brief govern this work, superseding the checkout's older assignment board.

The local checkout is `C:\Users\swami\Projects\gct\work`. HEAD and cached `origin/main` both resolved to **c984e2c6d59ba0bbc6ac2fdd113edf920a8aebd9**. A new `git ls-remote` attempt failed to connect to GitHub from the shell. The user's earlier live-remote verification is retained as source-reported readiness evidence; this run does not claim a fresh successful remote check. The obsolete absent-input statement at `226b4ef1` is historical.

| Required computational input | Found and inspected | Actual content / scope |
|---|---|---|
| `analysis/wk11_s69_circuit.py`, C evaluators and relevant drivers | Yes, exact names | Filling format, factorial normalization, DP and determinant-polarization paths, ladder transport |
| `docs/compact_circuit.md`, `docs/s69_report.md` | Yes | Definitions/proofs and original measurements; overclaims corrected below |
| `results/s69_n4_seed.json` | Yes | Two fillings, generic and determinant matrices, integer pencil data, both primes |
| `results/s69_ladder_n4.json` | Yes | 34 saved fillings: two native degree-12 and 32 native degree-13; no completed higher-rung source |
| `results/s69_lmr_state.json` | Yes | 113 saved target fillings and a 113 by 300 generic matrix at P1; 1,497 recorded samples |
| `results/s63_aladder.json` | Yes | Correct cumulative multiplicities, stable value 274; not independently recomputed plethysm here |
| `results/s69_n3_d12.json` | Yes | Six fillings and the integer determinant-ideal combination |
| `results/artefacts/s69_n3_d12_basis.json.gz` | Yes | Archived exact six by 17,047 chi-coordinate arrays |
| `results/artefacts/s69_banked_n3_d12.json` | Yes | Banked primitive integer ideal vector |
| `results/s69_ladder_n3.json` | Yes | Saved transported old five-dimensional span for a matched birth benchmark |

No aliases were needed for these computational inputs. Full paths, byte lengths, SHA256 fingerprints and the final source snapshot are recorded in the manifests.

**Calibration limitations:** the repository self-test was attempted and stopped at import with `ModuleNotFoundError: flint`; no self-test cases ran. The supplied `.so` evaluators are Linux binaries and were not loaded. A C/C++ compiler was not found. A working C# compiler through PowerShell `Add-Type` permitted a small Windows evaluator and an algorithmically distinct determinant-polarization checker. The current verifier retains `split_rank` and `hybrid_kernel` as **RECORDED**, explicitly without re-deriving those ranks. The points module appends `permanent_pencil` after the original four families, preserving their seed offsets. The full s67/s71 reconciliation and calibration corpus were not replayed. Nor were the twelve B24 multiplicities or weighted Pieri economics independently reproduced. This is a qualified independent-theory/control run, not a blanket preflight PASS.

The requested Documents output directory was denied by the filesystem permissions. Results are delivered in the permitted isolated directory `C:\Users\swami\Projects\gct-gpt\Batch12_Results\S1`. No permission workaround or canonical edit was attempted.

## Coordinates, field, and evaluable vectors

Work first over **Q**, in the polynomial ring

\[
R=\mathbb Q[c_\alpha: \alpha\in\mathbb N^r,\ |\alpha|=n].
\]

The ordinary coefficient coordinate is `c_alpha(f) = [s^alpha]f`. The symmetric letter symbol is

\[
m_\alpha=\alpha!c_\alpha=n!\,\widetilde f(e_{i_1},\ldots,e_{i_n}).
\]

The filling has exactly n occurrences of each of delta letters. Its columns are two ordered h-tuples C1,C2, a list of ordered pairs `two`, and singleton entries `one`. Its polynomial is the integer sum

\[
F_T(f)=\sum_{\sigma_C\in S_{|C|}}\left(\prod_C\mathrm{sgn}(\sigma_C)\right)
 \prod_l \alpha_l(\sigma)!\,c_{\alpha_l(\sigma)}(f).
\]

Each column contributes the tensor `e1 wedge ... wedge eh`. Upper triangular unipotents fix it, and its torus weight is the column indicator. Thus the contraction is a highest-weight vector of weight lambda, including when it is zero. This also follows in house coordinates from

\[
E_{ij}c_\alpha=(\alpha_i+1)c_{\alpha+e_i-e_j},\quad i<j,
\]

with the term zero if alpha_j=0. The all-fillings spanning assertion follows by applying the equivariant inner/outer symmetrizers to the highest-weight tensors in tensor space. It does not assert independence of different fillings. No target tensor-space expansion is needed to define or evaluate a vector.

Exponent coordinates are in the recursive order used by `exps(n,r)`: the first exponent increases from 0 to n, then recurse on the remaining entries. Explicit exponent arrays and coefficients occur in the control design. Rows are fillings; columns are points. A linear combination is stored as rational coefficients attached to these ordered rows.

The target is fixed throughout:

\[
n=4,\ r=h=9,\ \delta=24,\ \lambda=(65,17,2^7),\ \lambda'=(9,9,2^{15},1^{48}),\ a=274.
\]

One ladder step adds **four** singleton columns, not one. The phrase “one 1-column per degree” in the old circuit specification is a typo; its implementation appends n singletons and is consistent with total degree.

## Exact birth-quotient theorem

Set `u = c_(n,0,...,0)`, with weight `(n,0,...,0)` and coefficient degree one. Fix the tail rho and let M_d be the weight `(nd-|rho|,rho)` highest-weight space in R_d. Let

\[
\rho_d:M_d\longrightarrow R/(u),\qquad F\longmapsto F\big|_{u=0}.
\]

**Theorem.** Over Q,

\[
\ker\rho_d=uM_{d-1};\qquad M_d/uM_{d-1}\ \cong\ \rho_d(M_d).
\]

**Proof.** Multiplication by u is injective because R is a domain, and every raising derivation kills u. It therefore maps M_(d-1) into M_d. Conversely, if F in M_d restricts to zero, polynomial division by the coordinate u gives F=uG for a unique polynomial G of degree d-1. Weight homogeneity gives G the predecessor weight. For each raising operator E, `0=E(F)=u E(G)`, hence E(G)=0 in the domain R. Thus G belongs to M_(d-1). This proves both inclusions and the induced isomorphism. If the predecessor weight is nondominant, its highest-weight space is zero. QED.

This is restriction of actual source vectors. It does **not** identify births with a highest-weight kernel supported on u-free monomials. The old support-restricted strategy remains killed: other coefficients can be necessary to make a vector highest weight even when its residue is nonzero. Nor does the theorem give a determinant or padded rank property to a birth direction.

**Selection corollary.** Suppose the old source basis has been certified and `b_d = dim M_d - dim M_(d-1)` is known. Choose valid fillings T1,...,T_b and points Q1,...,Q_b on u=0. A nonzero b by b evaluation determinant proves their classes independent modulo uM_(d-1). Appending these fillings to u times the old basis gives a basis of M_d. A rank-q minor proves q independent birth classes even when q<b. No old-basis evaluation is needed for this test.

**Characteristic-zero justification.** The F_T have integer coefficients. A nonzero minor at either house prime lifts by taking the displayed residues as integer coefficient points, with the u-coordinate exactly zero. Its integer determinant is not zero; therefore the Q-classes are independent. This does not require a theorem that every modular kernel lifts, or a blanket claim about semisimplicity in large characteristic. Both primes exceed n and all displayed rational lift denominators are powers of n!. A second prime checks robustness; it does not replace circuit semantics. Zero matrices or kernels at finitely many points remain sampling information unless a separate identity proves the zero.

### Actual finite matrices and dimensions

For a candidate T and explicit coefficient points Q_j on u=0, compute `R_d(T,j)=F_T(Q_j)` using the above contraction formula and the existing tensor packer. A streaming row-echelon selection retains at most b_d rows; with eight reserve points each matrix under elimination has at most `(b_d+1) by (b_d+8)` entries, including the candidate. Record unnormalized source rows and minor indices separately from the echelon work buffer. The maximum is **55 by 62**, and the final two rungs need **2 by 9** work matrices. The linear algebra is explicitly bounded; the number of candidate circuits needed to attain b_d is not yet bounded economically.

| d | old dimension | b_d | a_d | b_d+8 points | Saved native births available |
|---:|---:|---:|---:|---:|---:|
|12|0|2|2|10|2|
|13|2|37|39|45|32|
|14|39|54|93|62|0|
|15|93|52|145|60|0|
|16|145|43|188|51|0|
|17|188|31|219|39|0|
|18|219|22|241|30|0|
|19|241|14|255|22|0|
|20|255|9|264|17|0|
|21|264|5|269|13|0|
|22|269|3|272|11|0|
|23|272|1|273|9|0|
|24|273|1|274|9|0|

These are corrected source-reported multiplicities, not a new plethysm calculation. Births sum to 274. The checkpoint has five still-unfilled degree-13 slots and all later slots, **240 slots in total** if its 34-vector source is accepted after full replay. Fresh checks here cover only the specified subset; do not confuse that conditional remainder with a newly certified 34-vector basis. The separate 113-vector target checkpoint is not combined with it, and the two ranks must not be added.

For a symbolic deterministic existence bound, lexicographically enumerate column-strict balanced fillings and coefficient points in `{0,...,d}^494` on u=0. Tensor-product interpolation separates polynomials of degree at most d; at most `(d+1)^494` points suffice at n=4,r=9. This is a correct finite termination argument, but is **KILL for implementation**. We do not enumerate this grid or present its astronomical size as a solution. The practical theorem bounds the small rank problems, while the candidate-hitting bound remains OPEN.

## Partial straightening: identities, termination, and limitations

Use formal letter variables x_(l,i) and apply the linear umbral map sending the degree-n monomial for letter l to m_alpha. The product of flag minors and singleton factors is multihomogeneous of degree n in every letter. Polynomial identities with this content remain identities after the umbral map. Multiplication is used before applying the map; it is not claimed that the umbral map is an algebra homomorphism.

1. **Column antisymmetry and repeated-letter zero.** Swapping entries in one column negates F_T. A repeated letter in that column gives zero by swapping its identical tensor legs. This justifies sorting entries with signs and rejecting a repeated label.
2. **Identical-letter relabeling and whole-column permutation.** Bijectively renaming all letters preserves the product of identical f tensors. Permuting whole columns of equal height preserves the polynomial. The implemented normalizer only normalizes fixed labels; a complete unlabeled graph canonicalizer is not claimed.
3. **Pure-u removal.** If a letter occurs only in n singleton columns, its symbol is n!u. Delete it and relabel the remaining letters to obtain `F_T=n!u F_deleted`. In the birth quotient this is an exact zero, so such candidates can be rejected without evaluation. In the full source it must be transported and retained as appropriate, not declared zero.
4. **A proved unshared-column zero test.** If the tall columns share k letters and `h-k>n`, then F_T=0. For each fixed binary assignment on short columns, a tall-only letter contributes one of the n vectors `v_t(i)=m_(e_i+(n-1-t)e1+t e2)`, `0<=t<n`. More than n such columns are linearly dependent, so the tall determinant is zero term by term. This proves k<4 at n=3,h=7 and k<5 at n=4,h=9. It does **not** prove the stronger empirical statement k<=4 at n=3, and does not authorize deleting any additional overlap sector.
5. **Short-column Plücker rule.** For `a<c<d<b`,

   \[
   [a\ b][c\ d]=[a\ d][c\ b]-[a\ c][d\ b].
   \]

   Multiplying by the remaining column factors and applying the umbral map preserves F_T. Each term keeps every letter's occurrence count and the same column heights. `relations.json` contains all three complete valid fillings for a nontrivial small example, coefficients, and both-prime evaluations.

**Termination of rule 5.** With labels fixed during rewriting, define

\[
E(T)=\sum_{(a,b)\text{ short column},\ a<b}(b-a)^2.
\]

Put `x=c-a`, `y=d-c`, `z=b-d`, all positive. The energy contribution on the left is `(x+y+z)^2+y^2`. The positive term has `(x+y)^2+(y+z)^2`, a decrease of 2xz. The negative term has x^2+z^2, a strictly smaller value too. Sorting or permuting whole short columns does not change E. Therefore every branch strictly decreases a nonnegative integer; its depth is at most the initial E, bounded here by `15*(delta-1)^2`. A deterministic choice of the first nested pair in sorted order supplies an executable terminating rewrite. Stop conditions in the implementation preserve an unresolved expression rather than falsely reporting a complete normal form.

At termination the short columns are comparable componentwise, so their two rows are weakly increasing after ordering columns. Repeated use of the identity proves spanning by these partial normal forms. It proves neither their independence nor completion of relations involving the tall columns. Branch count can still grow exponentially in the depth bound. Umbral contraction can identify or kill different standard forms. This is why a dimension count, a list of distinct normalized fillings, or a classical standard-monomial theorem before contraction does not prove the desired source basis.

## Evaluation and source-coordinate handoff

The portable exterior evaluator stores the coefficient in `Lambda^p(Q^h) tensor Lambda^q(Q^h)` and the binary states of open short-column edges. Processing each letter wedges its tall indices, applies the closing-edge signs, and multiplies by its factorial-weighted symbol. Final row-order signs are explicit in the packer. The C# arithmetic maintains canonical residues below p; products are below `(p-1)^2<2^62`, and pairwise sums below 2p. There is no floating-point rank arithmetic.

The independent evaluator uses determinant polarization:

\[
F_T=\mathrm{sgn}(\pi)\sum_{s\in\{0,1\}^{n_2}}(-1)^{|s|}N(s)
\sum_{S\subseteq[h]}(-1)^{h-|S|}\det\left(\sum_{k\in S}M_k(s)\right).
\]

A shared letter supplies a matrix M_k of its two tall slots; paired tall-only letters supply a rank-one outer product. The inner finite difference extracts the squarefree coefficient of degree h in `det(sum x_k M_k)`. It has no exterior-state recurrence. These paths share the audited tensor-normalization packer, so they are not claimed to be independent in every component. Tiny literal Leibniz sums check the shared packing conventions. Fresh determinant/permanent pencils are constructed separately from the s69 point generator and checked by direct numerical substitution into the expanded form. Fresh minors are also recomputed by exact integer Bareiss elimination, distinct from modular elimination.

### Ladder normalization that must accompany a relay

For native degree d filling T, let T^up be the literal degree-D filling formed by adding D-d fresh letters, each occupying n singleton columns. Then

\[
F_{T^{up}}=(n!)^{D-d}u^{D-d}F_T.
\]

Thus a source normalized as `u^(D-d)F_T` is represented by the literal filling with coefficient `(n!)^(-(D-d))`. The saved s69 ladder's generic rows omit n! factors; this preserves row ranks but changes common source coordinates if omitted factors are forgotten when combining kernel coefficients. For a kernel vector x in normalized rows, literal-filling coefficients are `x_i/(n!)^(D-d_i)`. Do not mix row systems silently. Target ranks must use one declared system for generic, determinant, reducible and true padded points.

### Pieri-to-circuit conversion status

The reported precursor has B12=31 and B24=2168. Those are dimensions, not supplied intertwiners or evaluable basis vectors. S1 does not construct the missing compact Pieri recoupling map. The exact interface is: s75 supplies ordered predecessor vectors, normalized Pieri embeddings, their compact coordinates, and an evaluator for each embedded vector. If independent circuit vectors Q_i spanning the desired space and an invertible evaluation matrix A_(i,j)=Q_i(P_j) are already available, an abstract vector v with evaluable values y_j has circuit coefficients `x=y A^(-1)`. This is a valid **post-construction conversion**, not a basis-selection algorithm: using it to assume a missing full basis is circular and is killed for this task.

No raw tau restriction is used. The genuine invariant source is `W intersect Fix(tau)`; the projected/spherical formulation needs its own exact compact matrix and modular justification. That remains the s75/S3 interface, not a result of S1.

## Bounded deterministic selection rule

The relay replaces old-source elimination and structurally old candidates, not all randomness:

```text
for d in 12,...,24:
    target = corrected_birth[d]
    choose and record target+8 coefficient points, all with u=0
    replay saved native degree-d candidates first
    take candidates in a fixed order; preserve signs and original filling data
    reject repeated-column labels and proved unshared-rank zeros
    reject pure-u factors only in this birth test
    normalize fixed-label column order; memoize exact normalized duplicates
    optionally apply Plucker relations within 64 terms / 512 rewrites
    evaluate each candidate on the fixed u=0 points
    retain it only when a recorded nonzero minor increases birth rank
    stop this rung at target; retain original source rows, not just echelon rows
    if budget ends below target: record lower bound and missing count, then stop
```

For new candidates, a concrete bounded choice is a seed-recorded stream of valid balanced fillings, cycled across **all feasible** overlap k sectors satisfying the proved zero test, then sorted by `(pure-u count, certified DP slot width, normalized JSON key)`. Do not discard k=5 at n=4 merely because older samplers preferred 6–9. An implementation may enumerate local switches in lexicographic order, but such a switch graph has no proved spanning/hitting guarantee here. Use a stream budget of 256 candidates and at most `(b+8)*256` candidate evaluations per rung for the first handoff trial. If no new class appears, stop and report the exact residue rather than enlarge the census automatically.

Fresh points at a second prime and an algorithmically distinct evaluator certify accepted minors. Sampled zeros are not identities; retire candidates as zero only under the proved rules. The theorem guarantees existence of separating points over Q, but does not guarantee that one fixed finite set or one finite-field stream finds them. Primes and seeds remain explicit.

## Economics and remaining obligations

With N candidate circuits and per-evaluation cost t_d, the conservative birth screen costs at most `N*(b_d+8)*t_d`, plus about `O(N*b_d*(b_d+8))` field operations and `O(b_d*(b_d+8))` retained field elements. The s69 ladder uses approximately a_d+24 points and repeatedly evaluates/extends the old source. Under equal per-point costs, the final rung changes 298 points to nine, a **33.1-fold reduction in point count**, not a measured total speedup. At d=14 the count changes 117 to 62, only 1.89-fold. Candidates per independent birth can still dominate.

DP peak memory depends on the actual slot allocator and letter order, not merely on delta or the overlap. The dense implementation allocates two arrays of `(2^h)^2*2^W` 64-bit entries; at h=9 this is `4 MiB * 2^W` before overhead. Its operation count is bounded by summing, per letter, `binom(h,p)*binom(h,q)*2^W*h^2*2^(new edges)`. Record the actual packer W, which may exceed a cutwidth heuristic because slots are freed only after a letter. No claim is made that every target filling has W<=3.

The historical **12–15 CPU-hours** is an estimate from a different host and an unfinished source run. It was not rerun as a baseline. The paired n=3 benchmark measures a finite stream on available controls and compares clearly specified evaluation policies; it cannot be extrapolated into an n=4 completion time or an expected waiting time for the final birth. The n=4 prefix experiment is a replay of saved vectors, not newly discovered target directions.

Outstanding obligations, in implementation order:

1. Replay all 32 saved degree-13 classes on u=0 with retained minors; this report's eight-vector prefix does not certify the rest. Import their normalized source coordinates without restarting s69.
2. Fill the five remaining degree-13 classes and each subsequent birth count in the table. Supply candidates and separating-point minors; the quotient theorem does not locate them.
3. Derive compact relations involving the tall columns or another noncircular hitting construction. A useful next theorem must bound candidate production as well as rank-matrix size.
4. Complete any needed native n=3 expansion/E-matrix replay and house calibration in a supported runtime before repository-wide promotion. Exact arithmetic on archived expansions is explicitly narrower than a fresh expansion.
5. Obtain the Pieri embeddings and evaluable compact map if using S3/s75; B24=2168 alone is insufficient.
6. Only after a usable source span is certified, run common-coordinate determinant/red/true-padded evaluations under the frozen stopping rules. No target sampler was launched here.

## Claim ledger and frozen rank interpretation

| Claim | Status | Evidence / exact limitation |
|---|---|---|
| Kernel of u=0 restriction is uM_(d-1) | PROVED | Polynomial divisibility and raising derivations, over Q |
| Local signed identities and short-column termination | PROVED | Tensor/umbral identities and strictly decreasing energy |
| Full target triangular straightening basis | OPEN / route KILL | Capped expansion grows on every saved target filling; no independence theorem |
| Fresh control ranks and birth-prefix minors | CERTIFIED lower bounds | Explicit points, matrices, both primes and independent checks in accompanying artifacts |
| n=3 exact integer combination agrees with the bank | CERTIFIED artifact identity | 17,047 archived coordinates, zero mismatches; original expansion and raising-matrix build not rerun |
| n=3 exact determinant rank 5 | BANK plus fresh lower bound | Upper bound/global ideal identity is inherited; fresh finite zeros alone do not prove it |
| n=4 degree-12 source and determinant rank 2 | BANK dimension plus fresh lower bound | Two valid circuit vectors and nonzero 2-minors; no large carrier |
| Archived target generic matrix rank 113 | MEASURED matrix arithmetic | Saved matrix re-eliminated; no fresh semantic replay of the 113 target vectors |
| Original strong sampling-tail hypothesis | OPEN | Small-matrix savings demonstrated; rare-direction hitting rate not resolved |
| B24=2168, target source dimension 274 | Source-reported BANK | No second multiplicity engine rerun |
| Determinant rank 273 / padded rank 274 at target | OPEN / OPEN | No qualifying target minors supplied |

At the target, `i_X=274-rank(T_X)` and `D=rank(T_pad)-rank(T_det)` only describe the full common source and genuine variety restriction. LMR gives determinant rank **at most 273**. Certified determinant lower bound 273 would finish that side without a 274th vector. A valid true-padded 274-minor would itself certify source independence and padded rank 274. Here neither event occurred, so D is unresolved. True padding means **ell times per3**, whereas the reducible comparison means ell times a general cubic. No claim about one is substituted for the other.

If future exact ranks are both 273, compare kernel lines in common coordinates. If exact padded rank is below exact determinant rank, retain the negative multiplicity result and orientation information. A finite deficient evaluation or stalled source sampler establishes neither a characteristic-zero kernel nor D<=0. The r=5 programme still requires global completeness **and** valid exceptional-image bounds; S1 supplies neither and does not alter that status. No target carrier expansion, broad census, generic arc sweep, exceptional-group numerology, q=2 replication, or arbitrary-shape timing extrapolation was pursued.

## External literature boundary and review

The primary paper by de Boeck, Paget and Wildon constructs plethystic polynomial representations with tableau-indexed bases; it does not supply this session's missing 274 circuit vectors. The present restriction and rewrite proofs are given above, rather than imported as an unverified general plethysm rule. See [Plethysms of symmetric functions and highest weight representations](https://arxiv.org/abs/1810.03448). The author's abstract was checked; a repository PDF fetch timed out. No claim of novelty is made for the elementary quotient or Plücker arguments.

The artifacts are frozen for independent integrator review. The relay is a local document only; no worker was dispatched and no message was sent to another task. Scientific promotion remains with the integrator.
