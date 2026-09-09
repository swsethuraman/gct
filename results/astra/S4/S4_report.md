# Batch 12 S4 Padded injectivity and a certified partial bound

Frozen for independent review. Research conducted 8 September 2026 local time; artifact timestamps use UTC. This is a completed bounded research session with an unresolved target, not a launch plan.

## Outcome

At the prescribed cell

\[
\lambda=(65,17,2^7),\quad \delta=24,\quad r=9,\quad \dim M_\lambda=274,
\]

this session proves the new characteristic-zero lower bound

\[
\boxed{12\leq\operatorname{rank}T_{\rm pad}\leq274.}
\]

Two explicit 12-minors on true padded points are nonzero. All 816 completed native evaluations, including every entry needed for these minors, agree with a separately implemented evaluator using independent point polarization and a reverse contraction order. Both evaluators also agree with literal small contraction sums. The same 12 source polynomials, rational normalization, and integer points are used at both house primes.

**Padded rank 274 remains OPEN.** The hypothesis that the permanent-specific stage is injective on the reducible image has not been established. No true padded kernel at the target was found or proved. The requested small residual was not achieved: the newly certified complementary source quotient has dimension **262**, not one. The result meets the bounded-fallback branch, not the full-rank or small-residual prize.

Additional results are:

* **PROVED:** the precisely normalized source-to-reducible-to-permanent factorization, its multiplicity-block assembly, and its kernel/intersection identity.
* **PROVED:** fixing the linear factor to the first variable is an exact kernel test on highest-weight sources. This supplies a cheap exact identity check without expanding the full reducible pullback.
* **CERTIFIED over Q:** the banked s64 quartic control `(8,8,8), delta=6, r=3` has source dimension 2, determinant rank 2, and reducible/padded rank 1, with kernel coordinates `(1,0)` in a new explicit integer source basis.
* **PROVED over Q:** an archived s64 kernel at `(8,4,4,4,4), delta=6` lifts to an explicit 19,834-term integer highest-weight polynomial vanishing identically on reducibles, hence on true padding. Its identity is checked exactly, not inferred from two modular zeros.
* **CERTIFIED:** the r=6 padded and reducible parameter images have dimensions 55 and 61, using nonzero minors and structural upper bounds. This distinguishes the point families.
* **Recomputed controls:** fresh n=3 determinant and **unpadded per3** ranks 5 and 6 at both primes.
* **Enumerated:** all 48 cubic indices, multiplicity indices, and row offsets. The inherited cubic multiplicities sum to 521; those multiplicities were not independently recomputed and no target cubic block rank was computed.

The determinant side is separate: S4 adds no new target determinant lower bound. Retaining S1's certified transported lower bound two and the inherited LMR theorem gives `2 <= rank(T_det) <= 273`. In particular, determinant rank 273 and the sign of D remain OPEN.

## Preregistration and execution boundary

The working hypothesis was: the permanent-specific restriction is injective on `S(M_lambda)`. Acceptance required an exact kernel-intersection proof or a valid 274-minor; determinant rank 273 was never assumed. The recorded bounded computation used the 34 saved ladder fillings and at most 36 fresh padded points, with a 25-minute soft evaluation limit checked after a completed point column. No source sampler was restarted.

The run completed 12 columns. It recorded 1,607.7 seconds of wall time and stopped at the next column boundary. One independent-evaluator call, `p2147483629_r32_c11`, recorded **1,204.7 seconds**, while the other calls of that type were fractions of a second. The cause of this isolated wall-clock outlier was not established. No CPU-time record was retained that would justify subtracting it from the gate. The budget was therefore respected and the same run was not restarted. This timing is unsuitable for extrapolating target completion cost. The arrays' mathematical dimensions do not change with this timing anomaly.

All 36 integer points were generated and checked. Only columns 0 through 11 were evaluated. Within those columns, all 34 candidate rows were evaluated at both primes: `34*12*2=816` entries on each evaluator path. Only a 12-dimensional source subspace is independently certified by the displayed minor. There is no claim that these finite point matrices have the full padded rank, or that all 34 saved rows have been independently certified here.

The exact failure is an evidence deficit: no full evaluable 274-vector source, no assembled target split matrix, and no target cubic kernel matrices were delivered by the available inputs or constructed here. It is not a theorem that the map fails to be injective or that a compact method is impossible.

## Inputs and provenance

All four canonical documents were read in full, including the actual WordprocessingML text of `Batch12_Reconciled_Final_Proposal.docx`: that proposal, `batch11_final_stocktake.md`, `stocktake_batch11.md`, and `GCT_Comprehensive_Session_Source.md`. The complete standalone S4 brief, shared requirements, frozen rank protocol, and launch packet were read. The finalized proposal and S4 brief control assignments over the older repository plan.

The shared checkout was observed at `afb8c3319d3d1f3afc3d2578c8cb322f2b8a3b92`, with no tracked changes reported. Local HEAD, main, and cached origin/main agreed. Git verified that the user-supplied readiness commit `c984e2c6d59ba0bbc6ac2fdd113edf920a8aebd9` is an ancestor. Computation uses files archived from **c984e2c6d59ba0bbc6ac2fdd113edf920a8aebd9**, rather than a moving checkout. The fresh live-remote query failed to connect to GitHub. The earlier successful remote verification supplied by the user remains reported evidence, not a fresh PASS.

| Input | What was actually available and used |
|---|---|
| s69 source/evaluator | Filling definitions, symbol normalization, original exterior C code, and circuit documentation were inspected; the Linux shared objects were not loaded |
| n4 seed and ladder | Two degree-12 and 32 degree-13 saved fillings, 34 total; used without adding sampled fillings |
| target checkpoint | 113 target fillings with an archived generic matrix; read as incomplete source evidence, not promoted or combined by adding ranks |
| s63 ladder | Correct births `2,37,54,52,43,31,22,14,9,5,3,1,1`; a24=274 remains inherited multiplicity evidence |
| s70 | `s_split.md`, original report, coefficient pullback implementation and rank ledger; its old source-wall conclusion is obsolete and its adopted det=273 claim is rejected |
| s64 | Original report, integrator factorization note, padded point code, parameter-separation code, 48-cell ledger, and stored kernel artifacts |
| 48 cubic blocks | `results/logs/hpad_lmr.log`; index census independently reproduced, a3 values retained as source-reported |
| Completed Batch 12 reports | Actual workspace S1 and S3 reports read for source/conversion evidence; S2 outcome and preflight inspected for context. No session was awaited or declared complete without a report |
| S1 | Supplies birth quotient and circuit controls; no full target basis. Its transported determinant lower bound two is retained separately |
| S3 | Supplies compact operator and certified 31-to-2 dimension control, but explicitly leaves recursive-basis evaluation unresolved; it is not a usable target source |
| S2 | Reports a special rank-three geometry example and leaves global r=5 completeness/bounds open; S4 does not re-audit or promote the geometry |
| Verifier semantics | `permanent_pencil` is retained in the family list; `split_rank` and `hybrid_kernel` explicitly remain RECORDED without re-derivation |
| Broader preflight | Full self-test/corpus, s67/s71 reconciliation, second-engine B24, and weighted target DAG were not rerun. No blanket preflight PASS |

The S4 runtime uses bundled Python/NumPy and PowerShell's C# compiler. No target ambient carrier was built. The only expanded source control is the tractable 561-coordinate quartic r=3 control. Original canonical files, the shared checkout, schedules, and other tasks were not edited. No external relay was sent.

The requested Documents results directory was absent, and creating it returned access denied. The complete permitted deliverable is under `C:\Users\swami\Projects\gct-gpt\Batch12_Results\S4`. Input and output hashes, the denial, base commit, and replay commands are retained. This is a delivery-location limitation, not a mathematical input gap.

## Field and coefficient conventions

Work over Q, extending to C for orbit-image closures and semisimple representation decompositions. Let `V=Q^9`, `A_delta=Sym^delta(Sym^4 V)`, and `M_lambda=HWV_lambda(A_delta)`. Ordinary coefficient functions are

\[
c_\alpha(f)=[x^\alpha]f,\qquad d_\beta(c)=[x^\beta]c.
\]

Exponent lists use recursive order with the first exponent increasing, matching the frozen circuit packer. All supplied vectors and matrices state their row/column order; indices in JSON are zero-based.

For a degree-n form the house letter symbol is

\[
m^{(n)}_\alpha=\alpha!c_\alpha=n!\,\widetilde f(e_{i_1},\ldots,e_{i_n}).
\]

The polarization is normalized by `f(v)=tilde f(v,...,v)`. Column wedges are unnormalized alternating sums. A valid filling has n occurrences of every letter, distinct letters in each column, and the specified column heights. Its polynomial is the signed sum of products of these letter symbols. Each column wedge is fixed by upper-unipotent raising operators and has the corresponding indicator weight. Equivariant contraction and inner/outer symmetrization therefore give a highest-weight polynomial of the claimed weight, possibly zero. Distinct fillings alone imply no independence.

At the target the conjugate shape is `(9,9,2^15,1^48)`. All saved native fillings have `n=4,h=9` and degree 12 or 13. Put `u=c_(4,0,...,0)`. Our target row i is

\[
F_i^{24}=u^{24-d_i}F_i^{d_i}.
\]

Appending four singleton occurrences of a new letter multiplies the literal filling polynomial by `24u`. Consequently the scalar relating the literal extended filling to this normalized target row is exactly

\[
24^{-(24-d_i)}.
\]

The normalized polynomials themselves have integer coefficients. `source_coordinate_transforms.json` provides every literal extension, scalar, and permutation from column-ordered tensor slots to consecutive four-slot letters. These are exact common source-coordinate transforms. They are not an uncomputed change of basis to a 274-vector source or to a cubic Pieri basis.

## The factorization and its exact normalization

Let `C_r` be the Zariski closure of the cubic parameter image `A(x) -> per3(A(x))`, where A is a 3 by 3 matrix of linear forms in r variables. Let `R_r` be the reducible image closure and `P_r` the image closure of `(ell,A) -> ell per3(A)`. Thus `P_r` is the true padded model.

The multiplication map `mu(ell,c)=ell c` induces

\[
\mu^*_\delta:A_\delta\longrightarrow
D_\delta:=\operatorname{Sym}^\delta V\otimes\operatorname{Sym}^\delta(\operatorname{Sym}^3V),
\qquad
\mu^*(c_\alpha)=\sum_{i:\alpha_i>0} y_i d_{\alpha-e_i}.
\]

This is an ordinary coefficient formula: there is **no alpha_i factor** in it. In house symbols the equivalent formula is

\[
m^{(4)}_\alpha(\ell c)=\sum_i\alpha_i y_i m^{(3)}_{\alpha-e_i}(c),
\]

or, with four separately labelled legs,

\[
m^{(4)}(v_1,v_2,v_3,v_4)
=\sum_{t=1}^4\ell(v_t)m^{(3)}(v_1,\ldots,\widehat v_t,\ldots,v_4).
\]

There is no factor 1/4 in this last house-symbol identity. The normalized polarization identity does have 1/4; multiplying by 4! and replacing cubic polarization by its 3! symbol cancels it. Substituting this four-term identity at every letter node is the actual source-to-reducible circuit map. It is a definition with no carrier expansion; it is not an instruction to materialize all `4^24` summands.

The ideal of the image of mu is precisely `ker mu*`. Hence, on highest-weight multiplicity spaces,

\[
S:=\mu^*|_{M_\lambda},\qquad
\operatorname{rank}S=\operatorname{mult}_\lambda\mathbb Q[R_r]_\delta.
\]

This argument only uses the coordinate ring of the image; it does not require assuming the parameter map itself is a finite normalization map. The generalized Foulkes-type pullback and normalization context also appear in [Kadish–Landsberg, Theorem 1.7 and Proposition 1.8](https://arxiv.org/pdf/1204.4693). Their general high-first-row injectivity criterion has threshold `min(24*3,96-3)=72` here; lambda1=65 does not satisfy it. It supplies no target injectivity shortcut and no permanent-specific conclusion.

Let

\[
\mathcal I=\{\mu:\ |\mu|=72,\ \lambda_i\ge\mu_i\ge\lambda_{i+1}\},
\qquad M^{(3)}_\mu=\operatorname{HWV}_\mu\operatorname{Sym}^{24}(\operatorname{Sym}^3V).
\]

Pieri gives

\[
\operatorname{HWV}_\lambda D_{24}
\simeq\bigoplus_{\mu\in\mathcal I}M^{(3)}_\mu.
\]

Each Pieri multiplicity is one. The extra index `alpha=0,...,a3(mu,24)-1` is a **cubic plethysm multiplicity** and must not be omitted. Choose a rational basis `g_(mu,alpha)` and one consistently normalized Pieri embedding `iota_mu` for each shape. For example, in a rational seminormal model, use columns as vectors and normalize the horizontal-strip invariant to coefficient one on each standard extension of the old tableau; make this same choice on the quotient module below. The precise gauge is `s_i e_t=q_i(t)^(-1)e_t+(1+q_i(t)^(-1))e_(s_i t)`, with `q_i=content(i+1)-content(i)`, content column-minus-row, and the second term omitted for a nonstandard tableau. Normalize the Schur-Weyl map by sending the column-superstandard basis vector to the product of unnormalized column wedges. Group projections are averages `|G|^(-1) sum_(g in G) g`. This specifies an exact abstract convention, not numerical bases that this session claims to have constructed. A different nonzero scaling of an embedding rescales its entire block and is harmless only if used consistently on both stages.

Define the actual source coordinates by the identity

\[
\mu^*F_j=\sum_{\mu\in\mathcal I}\sum_{\alpha=0}^{a_3(\mu,24)-1}
 S_{(\mu,\alpha),j}\,\iota_\mu(g_{\mu,\alpha}).
\]

This fixes all row and multiplicity meanings. To compute a column in ordinary coefficient coordinates, apply the displayed coefficient substitution and resolve it in these embeddings. To compute it in tensor coordinates, designate the first slot of each quartic letter as linear, shuffle the remaining three slots first and all linear slots last, and average over `(S3 wr S24) x S24`. If source and cubic tensors use their house scales `24^24` and `6^24`, respectively, the tensor split carries the scalar **4^24**. The shuffle and scalar are supplied in the transform artifact. Conversion from that invariant tensor realization to chosen numeric cubic bases is still an explicit missing implementation, not a number hidden in our certificate.

Let `Q_mu:M^(3)_mu -> N_mu` be the cubic restriction map induced by

\[
d_\beta\longmapsto[x^\beta]\operatorname{per}_3(A(x)),
\]

where `N_mu` is its image multiplicity space, with any specified rational basis. Write `K_mu=ker Q_mu`, `K=direct_sum_mu K_mu`, and `Q=direct_sum_mu Q_mu`. For an input basis of size a, `S_mu` is `a3(mu,24) by a`; if Q_mu has q_mu rows, its composite block is `q_mu by a`.

The complete factorization on multiplicities is

\[
\boxed{M_\lambda\xrightarrow{S}\bigoplus_{\mu\in\mathcal I}M^{(3)}_\mu
\xrightarrow{Q}\bigoplus_{\mu\in\mathcal I}N_\mu.}
\]

Its rank is `rank T_pad`. Indeed, first restrict the cubic coordinate ring to `Q[C_r]`, tensor with `Sym^24 V`, and then compose with mu*. The composition is exactly the pullback along `(ell,A) -> ell per3(A)`, so its kernel is the padded ideal in the source. In characteristic zero the isotypic decomposition and Pieri embeddings carry this equivariant restriction blockwise. There is no replacement of permanental cubics by arbitrary cubics in this argument.

The assembled matrix is the **vertical stack**

\[
\mathcal T=\begin{bmatrix}Q_{\mu_1}S_{\mu_1}\\\cdots\\Q_{\mu_{48}}S_{\mu_{48}}\end{bmatrix},
\]

on the same source columns. One must rank this stack or supply a justified source/image decomposition. Summing its individual block ranks is generally wrong: one source vector can have nonzero components in many blocks, all controlled by the same single scalar.

The exact obstruction identity is

\[
\boxed{\operatorname{rank}T_{\rm pad}
=\operatorname{rank}S-\dim(S(M_\lambda)\cap K).}
\]

Equivalently, `ker T_pad=S^{-1}(K)` and its dimension is `dim ker S + dim(S(M_lambda) cap K)`. Full padded rank requires both `ker S=0` and the intersection zero. Even if S has rank 274, its image is a 274-dimensional subspace of the inherited 521-dimensional intermediate space, and its position relative to K matters.

A further correction to the original integrator note is necessary:

\[
521-\operatorname{rank}T_{\rm pad}
=(521-\operatorname{rank}S)+\dim(S(M_\lambda)\cap K).
\]

The entire deficit from 521 is **not** the sum of cubic permanent kernels. Even an injective S already leaves codimension 247 in this intermediate space. No global target rank, blockwise injection, or separating-vector argument bypasses this distinction.

## Exact fixed-factor kernel test and calibration proofs

For a highest-weight polynomial F define `R_1F` by setting `c_alpha=0` when alpha1=0, and replacing every remaining `c_alpha` by the distinct cubic coordinate `d_(alpha-e1)`. This is evaluation on `x1 c`. The map on surviving coefficient monomials is injective, so `R_1F=0` is an exact coefficient-support test.

**Lemma.** On the highest-weight source, `ker R_1=ker S`.

**Proof.** The easy inclusion follows from specialization. Conversely, F is fixed by each shear `x1 -> x1+t xj` for j>1: the induced derivation on ordinary coefficients is `E_(1j)c_alpha=(alpha1+1)c_(alpha+e1-ej)`, and F is highest weight. If the first coefficient y1 of ell is nonzero, the simultaneous shears with `t_j=-y_j/y1` take ell to `y1 x1`. They carry an arbitrary cubic to another cubic. Thus F vanishes on every such ell c if it vanishes on all x1 c. This is a dense open parameter set, so the polynomial pullback vanishes identically. QED.

The same argument applies with cubic c restricted to the GL-stable permanental cubic image. It does not say arbitrary cubics and permanent cubics are interchangeable; it only normalizes the linear factor within either family. On true padding the remaining cubic evaluation can still have a kernel.

At `(8,8,8), degree=6, r=3`, an independent enumeration gives 561 ordinary coefficient monomials and a 1056 by 561 simple-raising matrix. A retained 559-minor is `1143488089 mod 2147483647`. Independent NumPy elimination verifies it, with reduction after each multiply/subtract. Two reconstructed primitive integer source vectors satisfy **every raising equation over Z** and have an independent two-minor. The modular minor gives nullity at most two over Q; the exact vectors give nullity at least two. This certifies the source dimension, without lifting a modular kernel by assumption.

The first source vector has no surviving monomial in the fixed-factor test; its split is identically zero. The second has a surviving coefficient 36. Consequently split rank is exactly one and its kernel is `(1,0)`. Fresh padded evaluations of the second vector are nonzero, giving padded rank exactly one. This proves a real kernel and prevents the evaluator from spuriously returning source-full rank.

| Control minor | P1=2147483647 | P2=2147483629 |
|---|---:|---:|
| quartic r3 determinant 2-minor | 993656878 | 2002274814 |
| quartic r3 reducible nonzero entry | 219024 | 219024 |
| quartic r3 true-padded nonzero entry | 1366661096 | 1366946072 |
| cubic n3 determinant 5-minor | 1039976059 | 898798153 |
| cubic n3 unpadded per3 6-minor | 1018711257 | 718047479 |

For the separate r5 archived kernel, rational reconstruction proposes coefficients with common denominator 3. After clearing denominators and taking primitive content, the maximum coefficient magnitude is 41,472. Reconstruction is only a proposal: all simple raising equations were then checked exactly over Z, and the fixed-factor surviving-term count is exactly zero. The lemma proves its reducible and padded identities over characteristic zero. Fresh determinant evaluations are nonzero at both primes. The archive-to-integer scalar and the archive's modular source coordinates `(1,0)` are retained; these are **not target common-source kernel coordinates**.

The n3 source is the six saved bracket fillings for `(19,7,2^5),delta=12`. Fresh seven-point matrices recover determinant rank five and unpadded permanent rank six at both primes. The banked ideal combination `[66,-972,12,-37,4,320]` vanishes on the fresh determinant points. Its global ideal identity and the determinant upper bound five are inherited banked evidence, not proved by these finite zeros. No comparison with padded per2 is made.

### Correct interpretation of s64's discriminating cases

The archived 48-row s64 ledger has **zero** rows where `mult_pad != mult_red` and **twelve** where `mult_pad != mult_det`. Thus the brief's request for banked s64 cases with differing padded and reducible multiplicities cannot literally be fulfilled from that ledger. We do not relabel the twelve cases. The genuine archived distinction between padded and reducible families is at the level of their parameter images.

For r=6, the padded parameters are ten six-entry linear forms, dimension 60. Five effective row/column/padding torus directions preserve the polynomial on a dense open parameter set, so the image dimension is at most 55. In detail, row scalings a_i, column scalings b_j, and padding scaling c satisfy `c product(a_i) product(b_j)=1`; the one-dimensional ineffective row/column scaling leaves a five-dimensional effective action. Generic nonzero matrix entries and nonzero padding make this action free. The reducible parameter space has dimension `6+56=62`, with the usual one-dimensional scaling fibre, giving upper bound 61.

An exact derivative matrix, computed by single-parameter differences (the polynomial is affine in each such parameter), has padded rank at least 55 at both primes. The reducible analytic derivative has rank at least 61. Retained minors, checked by exact integer Bareiss elimination, prove the corresponding characteristic-zero lower bounds. Together with the structural upper bounds:

\[
\dim P_6=55<61=\dim R_6.
\]

These dimensions distinguish the actual point producers. They do not assert a padded-versus-reducible multiplicity difference in any target block.

## Target padded certificate and independent evaluation

The point family is explicitly

\[
f_j(x)=L_{j,0}(x)\sum_{\pi\in S_3}\prod_{a=0}^2L_{j,1+3a+\pi(a)}(x).
\]

The 10 by 9 integer array of linear forms for every point is saved, as are all 495 ordinary quartic coefficients. Generation uses Python `random.Random(12040000+j)`, entries in `[-3,3]`, rejecting a draw with `u(f_j)=0`. Final arrays are authoritative, so reconstruction does not depend on remembering an RNG implementation. Both primes use these identical integer arrays.

Every generated point has a full-rank 9 by 10 frame and a rank-nine first-derivative coefficient matrix at both primes; retained minors certify these nondegeneracy checks. The leading coefficient u is nonzero. No generic cubic or determinant point enters the padded matrix.

The first evaluator uses the audited s69 coefficient-to-symbol packer and the frozen S1 C# exterior recurrence. The second was written in this session. It computes symbols directly as coefficients of `t1*t2*t3*t4` in the product of four linear forms, summing 24 leg assignments and six permanent terms. It does not use the quartic coefficient packer. It contracts in reverse letter order, stores compact combinations of used tall-column indices, uses dynamic bags of actual short-edge IDs, and pays short-column signs on opening rather than closing. Its C# implementation is separate from the first evaluator.

These paths share the mathematical tensor contraction, as they must; they do not share the point-to-tensor builder, traversal, state allocation, sign bookkeeping, or evaluator code. The direct polarization was compared exactly over Z with `alpha! c_alpha` for every coefficient of all 36 points. Eight small literal full contractions independently check both complete paths, including normalization and signs.

All native matrix entries are multiplied by `u(f_j)^(24-d_i)` to obtain the common degree-24 matrix. Rows are source polynomials, columns points. In both primes the retained minor uses rows and columns **0,...,11**:

| Target certificate | P1 | P2 |
|---|---:|---:|
| matrix dimensions actually completed | 34 by 12 | 34 by 12 |
| certified lower bound | 12 | 12 |
| retained normalized target 12-minor | 1086325324 | 2097075880 |

`padded_certificate.json` contains the native and transported matrices, exact indices and both determinants. Independent integer Bareiss elimination on the displayed residue matrices verifies the determinants modulo p. Since the original filling polynomials, transport factors, and integer points are explicitly defined over Z, a nonzero modular determinant is the reduction of a nonzero integer determinant. It therefore proves independence of the same 12 padded restrictions over Q. The optional literal-filling normalization has only powers of 24 in its denominator, units at both primes. A second prime is a robustness check, not the reason for characteristic-zero transfer.

This certificate also proves 12 independent source vectors and 12 independent reducible restrictions. It does not prove that source dimension is only 12 or that a modular nullspace of the 34 by 12 matrix lifts to the padded ideal.

## Residual quotient and the exact finishing matrix

Let V0 be the span of the first 12 normalized target vectors, and let `e0:M_lambda -> Q^12` evaluate at points 0,...,11. Write B for the **points by vectors** 12 by 12 matrix, the transpose of the retained matrix in the artifact. B is an exact rational/integer matrix defined by the circuits at the saved integer points. Its inverse below is its **rational inverse**, not the naive lift of a modular inverse.

Define

\[
\Pi(F)=\sum_{i=0}^{11}(B^{-1}e_0(F))_iF_i,
\quad R(F)=F-\Pi(F),\quad L=\ker e_0.
\]

Then

\[
M_\lambda=V_0\oplus L,\qquad \dim L=262.
\]

The certificate proves `T_pad|V0` injective. Moreover `T_pad(V0) cap T_pad(L)=0`: evaluating an equality of such images at the first twelve points forces the V0 term to be zero. Thus this is a justified independent-image decomposition, and

\[
\operatorname{rank}T_{\rm pad}=12+\operatorname{rank}(T_{\rm pad}|_L).
\]

This is the smallest complementary source space certified by this run. It need not equal the global padded kernel, and it is not the last-born line. On the factorization side the exact remaining question is

\[
\{F\in L:S(F)\in\bigoplus_\mu K_\mu\}=0.
\]

Here is the finite finishing matrix specification. Given valid additional source vectors `G_1,...,G_262` whose classes span `M_lambda/V0`, and new true-padded points `Z_1,...,Z_262`, form

\[
H_{ji}=G_i(Z_j)-\sum_{a=0}^{11}(B^{-1}e_0(G_i))_aF_a(Z_j).
\]

A nonzero 262-minor of H, equivalently a 274-minor of the untransformed block evaluation matrix, finishes padded rank 274 and certifies independence of all source columns. For lower bounds, any k independent residual columns and k-minor add k to the current 12. The block alternative is to compute the vertical stack `Q_mu S_mu R` on these same residual columns. One must not substitute an unrelated basis in one block or add overlapping block ranks.

**Missing entries are explicit:** the 262 additional spanning source directions are not constructed, B's full rational inverse is not materialized, the 48 S_mu blocks are not instantiated, and no Q_mu/K_mu matrices are computed. The displayed H is an executable interface once those vectors are supplied, not a claim that a filled 262 by 262 rational matrix has been delivered. Direct full minors avoid materializing B inverse and can certify new independence without a separate source-basis certificate. This is a precise obstruction and bounded handoff, not an assertion that a small numerical residue has been isolated.

In particular, the 273-dimensional old source span at degree 23 has not been certified padded-full. The last-born direction cannot be the sole padded question here. Even after an old padded rank-273 certificate exists, a new vector must escape the **old padded image span**, not merely evaluate nonzero.

## Claim ledger and handoff

| Claim | Status | Evidence or remaining obligation |
|---|---|---|
| Coefficient/house-symbol split and padded composite rank identity | PROVED | Explicit pullbacks, equivariance, and block assembly above |
| Fixed-factor kernel lemma | PROVED | Highest-weight shear invariance and dense-open parameter argument |
| All 48 cubic indices and offsets | VERIFIED index census | Interlacing enumeration agrees with archived log |
| Cubic multiplicity sum 521 | Source-reported BANK | Sum checked; terms not independently recomputed |
| Target block S_mu / Q_mu ranks | OPEN | No block rank computations; ledger reports this for every nonzero block |
| Target padded rank at least 12 | CERTIFIED over Q | Both nonzero minors, exact source/points, separate evaluators and integer checking |
| Target source/reducible rank at least 12 | PROVED consequence | Same nonzero padded minor |
| Quartic r3 source 2, det 2, red/pad 1 | CERTIFIED over Q | Raising minor, exact integer HWVs, exact split kernel and nonzero evaluations |
| Archived r5 reducible/padded kernel | PROVED identity over Q | Rational reconstruction followed by full exact raising and fixed-factor checks |
| r6 image dimensions 55/61 | CERTIFIED over Q | Jacobian minors plus torus/scaling upper bounds |
| n3 unpadded per3/det controls | Fresh lower-bound certificates | Exact determinant upper bound and global ideal line retained from bank |
| Full source, S injectivity, permanent intersection zero | OPEN | No full evaluable source or target block matrices |
| Full preflight and live remote | NOT VERIFIED / blocked remote check | No blanket calibration or remote PASS |

**BANK** the new lower bound, coefficient-normalization theorem, exact calibration identities, index ledger, and independent evaluator. **KILL** inference from generic reducibles to true padding, summing individual block ranks, and interpreting a sampled nullspace as a Q-kernel. **PARK** a one-dimensional finishing task until a real padded rank-273 old-span certificate exists. Do not fund target carrier expansion, a broad census, generic r5 arcs, standard q=2 transport, or exceptional-group numerology from this result.

The implementation handoff is `HANDOFF_s74_s75_s76.md`. It requests continuation from supplied checkpoints with this common coordinate convention, independent residual-minor certification, and a bounded control for any new Pieri conversion. It sends no task or message automatically. Available S1/S3 results reduce duplicated work but do not remove their stated conversion gaps.

The outputs are frozen for independent review; no canonical mathematical claim has been promoted by this automation. The inherited B24=2168 is a precursor dimension, not a completed source. The separate r5 theorem still needs global completeness and valid exceptional-image bounds.

## Separate determinant and padded bounds

Using the earlier S1 target determinant certificate and the LMR upper bound, with their provenance retained:

\[
2\le\operatorname{rank}T_{\rm det}\le273,
\qquad
12\le\operatorname{rank}T_{\rm pad}\le274.
\]

Only the padded lower bound is a new target rank result of S4. Consequently

\[
1\le i_{\rm det}\le272,\qquad 0\le i_{\rm pad}\le262,
\qquad -261\le D\le272.
\]

These broad bounds establish no sign of D. Determinant rank 273, padded rank 274, D=1, exact D<=0, and target kernel orientation all remain OPEN. If future exact ranks are both 273, compare kernel lines in common source coordinates. A known separator alone is not a multiplicity advantage.

## Appendix The 48 cubic block ledger

Rows are in the original log's increasing lexicographic order. The two inherited zero-dimensional blocks have zero maps conditional on those dimension inputs. Every other split/permanent rank is uncomputed. This is the horizontal-24-strip list with cubic degree 24; it is **not** S5's twelve horizontal-four-strip predecessor channels. The complete machine-readable ledger additionally records every cubic multiplicity index.

The count can also be checked without the log: for each b=2,...,17 the three possibilities are `(58-b,b,2^7)`, `(59-b,b,2^6,1)`, and `(60-b,b,2^6)`. These give 16+16+16=48 shapes, of lengths nine, nine, and eight respectively. The a3 values below remain inherited.

| block | mu | inherited a3 | row interval (zero-based, half-open) | S block / permanent rank |
|---:|---|---:|---|---|
| 1 | (41, 17, 2, 2, 2, 2, 2, 2, 2) | 31 | [0,31) | OPEN / OPEN |
| 2 | (42, 16, 2, 2, 2, 2, 2, 2, 2) | 29 | [31,60) | OPEN / OPEN |
| 3 | (42, 17, 2, 2, 2, 2, 2, 2, 1) | 14 | [60,74) | OPEN / OPEN |
| 4 | (43, 15, 2, 2, 2, 2, 2, 2, 2) | 26 | [74,100) | OPEN / OPEN |
| 5 | (43, 16, 2, 2, 2, 2, 2, 2, 1) | 14 | [100,114) | OPEN / OPEN |
| 6 | (43, 17, 2, 2, 2, 2, 2, 2) | 28 | [114,142) | OPEN / OPEN |
| 7 | (44, 14, 2, 2, 2, 2, 2, 2, 2) | 24 | [142,166) | OPEN / OPEN |
| 8 | (44, 15, 2, 2, 2, 2, 2, 2, 1) | 12 | [166,178) | OPEN / OPEN |
| 9 | (44, 16, 2, 2, 2, 2, 2, 2) | 26 | [178,204) | OPEN / OPEN |
| 10 | (45, 13, 2, 2, 2, 2, 2, 2, 2) | 21 | [204,225) | OPEN / OPEN |
| 11 | (45, 14, 2, 2, 2, 2, 2, 2, 1) | 11 | [225,236) | OPEN / OPEN |
| 12 | (45, 15, 2, 2, 2, 2, 2, 2) | 24 | [236,260) | OPEN / OPEN |
| 13 | (46, 12, 2, 2, 2, 2, 2, 2, 2) | 19 | [260,279) | OPEN / OPEN |
| 14 | (46, 13, 2, 2, 2, 2, 2, 2, 1) | 10 | [279,289) | OPEN / OPEN |
| 15 | (46, 14, 2, 2, 2, 2, 2, 2) | 22 | [289,311) | OPEN / OPEN |
| 16 | (47, 11, 2, 2, 2, 2, 2, 2, 2) | 16 | [311,327) | OPEN / OPEN |
| 17 | (47, 12, 2, 2, 2, 2, 2, 2, 1) | 9 | [327,336) | OPEN / OPEN |
| 18 | (47, 13, 2, 2, 2, 2, 2, 2) | 19 | [336,355) | OPEN / OPEN |
| 19 | (48, 10, 2, 2, 2, 2, 2, 2, 2) | 14 | [355,369) | OPEN / OPEN |
| 20 | (48, 11, 2, 2, 2, 2, 2, 2, 1) | 7 | [369,376) | OPEN / OPEN |
| 21 | (48, 12, 2, 2, 2, 2, 2, 2) | 18 | [376,394) | OPEN / OPEN |
| 22 | (49, 9, 2, 2, 2, 2, 2, 2, 2) | 11 | [394,405) | OPEN / OPEN |
| 23 | (49, 10, 2, 2, 2, 2, 2, 2, 1) | 7 | [405,412) | OPEN / OPEN |
| 24 | (49, 11, 2, 2, 2, 2, 2, 2) | 15 | [412,427) | OPEN / OPEN |
| 25 | (50, 8, 2, 2, 2, 2, 2, 2, 2) | 9 | [427,436) | OPEN / OPEN |
| 26 | (50, 9, 2, 2, 2, 2, 2, 2, 1) | 5 | [436,441) | OPEN / OPEN |
| 27 | (50, 10, 2, 2, 2, 2, 2, 2) | 13 | [441,454) | OPEN / OPEN |
| 28 | (51, 7, 2, 2, 2, 2, 2, 2, 2) | 6 | [454,460) | OPEN / OPEN |
| 29 | (51, 8, 2, 2, 2, 2, 2, 2, 1) | 4 | [460,464) | OPEN / OPEN |
| 30 | (51, 9, 2, 2, 2, 2, 2, 2) | 11 | [464,475) | OPEN / OPEN |
| 31 | (52, 6, 2, 2, 2, 2, 2, 2, 2) | 5 | [475,480) | OPEN / OPEN |
| 32 | (52, 7, 2, 2, 2, 2, 2, 2, 1) | 3 | [480,483) | OPEN / OPEN |
| 33 | (52, 8, 2, 2, 2, 2, 2, 2) | 9 | [483,492) | OPEN / OPEN |
| 34 | (53, 5, 2, 2, 2, 2, 2, 2, 2) | 3 | [492,495) | OPEN / OPEN |
| 35 | (53, 6, 2, 2, 2, 2, 2, 2, 1) | 2 | [495,497) | OPEN / OPEN |
| 36 | (53, 7, 2, 2, 2, 2, 2, 2) | 6 | [497,503) | OPEN / OPEN |
| 37 | (54, 4, 2, 2, 2, 2, 2, 2, 2) | 2 | [503,505) | OPEN / OPEN |
| 38 | (54, 5, 2, 2, 2, 2, 2, 2, 1) | 1 | [505,506) | OPEN / OPEN |
| 39 | (54, 6, 2, 2, 2, 2, 2, 2) | 5 | [506,511) | OPEN / OPEN |
| 40 | (55, 3, 2, 2, 2, 2, 2, 2, 2) | 1 | [511,512) | OPEN / OPEN |
| 41 | (55, 4, 2, 2, 2, 2, 2, 2, 1) | 1 | [512,513) | OPEN / OPEN |
| 42 | (55, 5, 2, 2, 2, 2, 2, 2) | 3 | [513,516) | OPEN / OPEN |
| 43 | (56, 2, 2, 2, 2, 2, 2, 2, 2) | 1 | [516,517) | OPEN / OPEN |
| 44 | (56, 3, 2, 2, 2, 2, 2, 2, 1) | 0 | [517,517) | 0 / 0 conditional on a3 |
| 45 | (56, 4, 2, 2, 2, 2, 2, 2) | 2 | [517,519) | OPEN / OPEN |
| 46 | (57, 2, 2, 2, 2, 2, 2, 2, 1) | 0 | [519,519) | 0 / 0 conditional on a3 |
| 47 | (57, 3, 2, 2, 2, 2, 2, 2) | 1 | [519,520) | OPEN / OPEN |
| 48 | (58, 2, 2, 2, 2, 2, 2, 2) | 1 | [520,521) | OPEN / OPEN |


## Delivered artifact links

* [Padded certificate](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S4/artifacts/padded_certificate.json)
* [Exact points](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S4/artifacts/points.json)
* [Source transforms](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S4/artifacts/source_coordinate_transforms.json)
* [48-block ledger](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S4/artifacts/48_block_ledger.json)
* [Independent checks](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S4/artifacts/independent_checks.json)
* [Implementation handoff](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S4/HANDOFF_s74_s75_s76.md)
* [Replay commands](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S4/REPLAY.md)
* [Artifact manifest](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S4/artifact_manifest.json)
