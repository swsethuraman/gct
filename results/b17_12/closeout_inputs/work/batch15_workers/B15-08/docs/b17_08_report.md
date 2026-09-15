**B17-08 — COMPLETE: no supported finite representation family nominated.**

Theory-only selection in the assigned B15-08 worktree, 14 September 2026; requested model gpt-6-astra, reasoning xhigh. Nominations: **zero**. Scientific computations, Python invocations and numerical evaluations: **zero**. Slots09/10 remain held. This closes the authorized bounded contribution; it does not claim exclusion of all five-row multiplicity obstructions.

The [first-stage independent review](../../B15-11/docs/b17_11_report.md) accepts the scoped01/03/05/06/07 claims. Their original reports were read, and the five report hashes match the versions pinned by that review. Slot02's [original report](../../B15-02/docs/b17_02_report.md) and manifest are supplied, but **02 remains provisional in this delivery**: no independent02 supplement was consumed or awaited. Its formula is analyzed conditionally and authorizes no computation.

The exact missing determinant input is an explicitly labelled five-row cell with finite a,s,U and a certified forbidden-weight rank large enough to make B<U. Geometry identifies five rows, but supplies no degree or partition. The accepted flag module supplies no five-row equations through polynomial multiplication. The accepted permanent coefficient method supplies an exact instrument, but no rank promise. None of these gaps can be filled by treating a source dimension as an image rank.

**Conventions and inherited scope.**

Work over C. Let V=C^16, forms lie in Sym^4(V*), and A=Sym(Sym^4 V). In coefficient degree d, partitions lambda of 4d label S_lambda V. Coefficients are ordinary monomial coefficients, with positive weights; in particular
`E_ij(c_alpha)=(alpha_i+1)c_(alpha+e_i-e_j)` when alpha_j>0. For the same highest-weight space H=H_(d,lambda), set

\[
 a=\dim H,\quad K_f=H\cap I(X_f),\quad i_f=\dim K_f,\quad m_f=a-i_f,
 \qquad D=m_{\rm pad}-m_{\det}=i_{\det}-i_{\rm pad}.
\]

The polynomial is independent z*per3 with nine independent entry coordinates and one independent z, embedded in sixteen variables. A sufficient certificate is a global m_det<=B and an actual padding restriction rank r>B. A source ceiling U only gives a necessary gate U>B.

The accepted [03 proof](../../B15-03/docs/b17_03_report.md) identifies ambient highest-weight spaces and both restriction kernels with their r-variable counterparts when length(lambda)<=r. Its all-degree inclusion for r<=4 uses smooth cubic-surface determinant representations, density, and the polynomial block construction diag(l,M). The classical premise is [Beauville, Corollary6.4](https://math.univ-cotedazur.fr/u/beauvill/pubs/det.pdf); it is extended to arbitrary cubic forms by closure, not by claiming exact representations of every singular cubic. Thus D<=0 at lengths<=4. Ten-variable padding support gives m_pad=0 at lengths>10.

The accepted [01 proof](../../B15-01/docs/b17_01_report.md) establishes dominance of five-variable per3 restrictions onto all five-variable cubics, and coefficient-closure noncontainment of lC in the det4 pencil closure for smooth cubic threefold C and nonzero l. Its boundary proof uses ruledness specialization componentwise, including divergent-pencil limits. These non-elementary geometric premises and its exact density/smoothness/frame certificates are **inherited from the accepted review**, not replayed here.

Together01/03 imply existence of a homogeneous determinant equation surviving on padding in some exactly five-row cell. Indeed the five-variable separating ideal has a homogeneous isotypic component whose padding restriction is nonzero; equivariance and complete reducibility give a highest-weight vector with that property. The four-row kernel inclusion excludes shorter labels. This proves neither a finite degree bound nor a dimension inequality between the two kernels. Different one-dimensional kernels in a two-dimensional H already show why kernel noncontainment alone is insufficient.

The current SCREEN_REPORT supersedes the stale six-cell status in COMMON_CONTEXT. All six nearby Batch16 cells are excluded. The specified degree-seven short-body screen closes its symmetry certificate, with no conclusion about further boundary loss. Neither screen is expanded here.

**Fresh finite reduction: the actual five-row padding multiplicity is a product-map rank.**

Let L=C^5 and define the coefficient pullback
\[
 \Phi_d:\operatorname{Sym}^d(\operatorname{Sym}^4 L)
 \longrightarrow \operatorname{Sym}^d L\otimes
                     \operatorname{Sym}^d(\operatorname{Sym}^3 L).
\]
For l=sum b_i x_i and C=sum a_beta x^beta it is the substitution
\[
 c_\alpha\longmapsto\sum_{i:\alpha_i>0}b_i a_{\alpha-e_i}.       \tag{1}
\]
Let Phi_(d,lambda) denote its map on highest-weight multiplicity spaces. For every length(lambda)<=5,
\[
 \boxed{m_{\rm pad}(d,\lambda)=\operatorname{rank}\Phi_{d,\lambda}.} \tag{2}
\]

*Proof.* Pullback under (l,C)->lC has kernel exactly the ideal of its image closure. The projective multiplication map has projective source, hence closed image, so its affine cone is the product locus R_(1,3,5). Accepted01 says the closure of actual five-variable padded restrictions equals that locus. Accepted03 identifies the same H and the same ideal kernel with the GL16 comparison. Taking the quotient of H by this kernel gives (2). No surjectivity onto the source of Phi is used. QED.

This is a source-grounded deduction from the reviewed results. The general coefficient-map construction agrees with [Kadish–Landsberg, Theorem1.7](https://arxiv.org/pdf/1204.4693v1), but (1) also proves its needed kernel description directly. The theorem's source ring and its image remain different objects.

For one finite five-row lambda, define
\[
 a=[s_\lambda]h_d[h_4],\qquad
 T=\sum_{\substack{\mu\vdash3d\\\lambda/\mu\text{ horizontal }d\text{-strip}}}
                    [s_\mu]h_d[h_3],
 \qquad U=\min(a,T).                                      \tag{3}
\]
All characters can be specialized to five variables. Pieri interlacing forces mu to have at most five rows, so the original cubic support ceiling of nine imposes no additional deletion in this formula. This is consistent with the accepted [B16-01 original product-source proof](../../B15-01/docs/b16_01_proof.md), not a replacement of the ten-variable problem by generic ten-variable cubic padding.

Equation(2) yields m_pad<=U, but not m_pad=U or m_pad=a. It also supplies an actual lower-bound route: r independent columns of (1) on explicitly supplied highest-weight polynomials give m_pad>=r. Such independent functions admit a nonzero evaluation determinant on r separate product-parameter copies. Dominance preserves its nonvanishing after substituting each C=per3(B(x)). The open set of full-rank five-frames and nonzero entry forms is dense in those parameter spaces, so the evaluations can be realized by restrictions of invertible GL16 substitutions with every entry retained. A concrete rational realization would still need its own certificate; dominance supplies no coefficient values or price.

Pieri gives an elementary preliminary exclusion lambda_1<d => T=0. Beyond such proved conditions, no all-row or eventual-degree surjectivity of Phi is assumed. Raising the first row does not by itself establish that its kernel disappears: multiplication of any nonzero highest-weight ideal polynomial by powers of the leading coefficient preserves ideal membership and is injective in the ambient polynomial ring.

**Provisional02: the exact loss needed after ambient clipping.**

To reconcile dual conventions, set W=V*. Slot02 treats forms as Sym^4 W and coefficient modules as S_lambda(W*)=S_lambda V. Its multiplicity source is M_lambda=(S_lambda W)^H_det, and s=dim M_lambda includes the full stabilizer, including transposition. Equivalently, s is the symmetric rectangular Kronecker coefficient with rectangle (d,d,d,d). This is the orbit bound, not the closure multiplicity; see [BLMW, §4.1 and Proposition5.2.1](https://arxiv.org/pdf/0907.2850v2).

The adapted coordinate blocks of02 have gamma weights -1,0,+1 and dimensions4,3,9. Its shared skew/symmetric identity gives
\[
 \gamma(t)f=Q_0+tQ_1+t^2Q_2,\qquad
 C_{d,\lambda}:M_\lambda\longrightarrow
                  \bigoplus_{k<0\ {\rm or}\ k>2d}(S_\lambda W)_k.
\]
Here C is the forbidden-weight projection, not a count of its carrier. Provisionally, if rank(C)>=b, then
\[
 m_{\det}\le B(b):=\min(a,s-b).                          \tag{4}
\]
The reason is polynomial extension: for every extending multiplicity vector z and every matrix-coefficient functional ell, ell(gamma(t)z) is the restriction of a coefficient-degree-d polynomial to Q0+tQ1+t^2Q2. It has exponents only0 through2d, hence all forbidden projections of z vanish. This proves necessity, without assuming that ker C is precisely the extension space. It also explains why the projection must be evaluated on actual full-H invariant vectors, rather than on arbitrary ambient tensors.

**Clipping lemma.** Let a,s be nonnegative integers, 0<=b<=s, and let U be an integer with 1<=U<=a. Then
\[
 B(b)<U\quad\Longleftrightarrow\quad
 b\ge b_{\rm gate}:=\max(0,s-U+1).                       \tag{5}
\]
The strict improvement threshold relative to B0=min(a,s) is
\[
 b\ge s-B_0+1.                                          \tag{6}
\]

*Proof.* Since a>=U, min(a,s-b)<U holds exactly when s-b<U. Integrality and b>=0 give (5). Similarly min(a,s-b)<B0 is equivalent to s-b<B0, giving (6). If U=0, no nonnegative B can pass the gate. QED.

Consequently, in the ambient-limited case s>=a, the first s-a lost dimensions buy no reduction at all. Strict improvement costs s-a+1; crossing a smaller padding ceiling costs the larger s-U+1. If s<U, b=0 already passes the symmetry gate, but no such new specific cell is furnished by these reports. A nonzero b can improve the symmetry bound yet still leave B>=U.

A rank upper bound on the forbidden carrier, or its nonempty Levi support, supplies no positive b. Negative and high-weight projections must be stacked on the **same invariant columns**; their separate ranks cannot be added without proving independence. Likewise an independent equation floor q can be combined safely as B<=min(a-q,s-b). Adding q and b as losses would require a further intersection argument.

For the one-base Slot06 construction, let
\[
 K_d=\binom{d+5}{5}-\binom{d+2}{5}.
\]
Its capacity also requires B+1<=K_d. Thus a necessary simultaneous headroom/capacity condition for that instrument is
\[
 b\ge\max(0,s-\min(U,K_d)+1),\qquad U\ge1.             \tag{7}
\]
This is only a capacity condition, not a lower bound on padding rank. No finite values of a,s,U,b or basis for C in a new five-row cell are supplied, so (5) and (7) cannot currently be certified numerically. Slot02's small arc-identity pilot prices its identity verification only; it does not price a Schur-basis expansion or a forbidden-weight minor.

**Why05 cannot fill the five-row determinant deficit.**

Accepted05 completes E24*A2 in degree26, lambda=(69,19,2^8): image dimension5, quotient of the complete determinant ideal dimension5. The already excluded cell has a=428, m_det=418 and U=288. These are inherited results and not a nomination.

There is a stronger structural reason this particular input cannot reach our priority rows. Let mu=(65,17,2^7), of length9, and Jflag=(E24) in A. For **every** d and every lambda with length(lambda)<=8,
\[
 \operatorname{Hom}_{GL_{16}}(S_\lambda V,(J_{\rm flag})_d)=0. \tag{8}
\]
For d<24 it is zero by degree. For d>=24, Jflag_d is an equivariant quotient of S_mu V tensor A_(d-24). Every polynomial constituent S_nu V of the multiplier has nonnegative partition nu. A nonzero Littlewood–Richardson coefficient c^lambda_(mu,nu) requires the diagram mu to be contained in lambda, hence lambda has at least nine rows. The quotient cannot acquire a type absent in its source. This proves (8) in all degrees.

Thus the certified flag-ideal contribution is **q_flag=0 in every five-row cell**. This says nothing about the full determinant ideal there. The primary generator is [LMR, Theorem2.3.1 and its following paragraph](https://arxiv.org/pdf/1004.4802v1). Polynomial multiplication, the full unrestricted J24, and saturation are separate constructions; (8) concerns only Jflag. Parameter contractions in05 do not evade it, since their outputs remain actual products. No coefficient differentiation or rational division that might change ideal membership is introduced.

Accepted07 gives no coefficient-module bridge and no det4 five-row finite label. Its det5 conormal target is a different geometric test, so it does not supply B or r here.

**Actual-padding construction and a cost contract; no finite job proposed.**

For a future supplied cell and r=B+1 highest-weight polynomials F_j, the reviewed [06 method](../../B15-06/docs/b17_06_report.md) uses one specified invertible base of ten independent forms b,L_ij. It retains all nine entries and sets
\[
 q_\sigma=b\prod_iL_{i,\sigma(i)},\qquad
 H_j(y)=F_j\left(\sum_{\sigma\in S_3}y_\sigma q_\sigma\right).
\]
Reduce modulo the single matching relation product_(even sigma)y_sigma minus product_(odd sigma)y_sigma. Canonical coefficients are signed sums over the complete exponent fibers. A nonzero r-square minor of this normal-form coefficient matrix proves m_pad>=r. The optional four-scalar unit arc preserves the rank of that fixed family; it promises neither r independent columns nor success of its first r Hasse rows. A failed base does not bound the entire padding orbit.

The following quantities are a **symbolic price specification**, not an instantiated or measured computation proposal. No d,lambda is nominated, no finite calculation is proposed to09, and there is no asserted runtime estimate for an absent input.

| Stage if a future single cell is supplied | Support/operation quantities that its preflight must instantiate |
|---|---|
|09 finite ambient/source characters (3)|For h_d[h_k], raw power-sum terms T_k(d)=sum_(rho partitions d) p(k)^(length rho), with p(3)=3 and p(4)=5. Merged support is at most p(kd). Source channels obey mu_i in [lambda_(i+1),lambda_i], sum mu_i=3d, so at most product_(i=1..5)(lambda_i-lambda_(i+1)+1), lambda_6=0. Count finite corrections or establish stability before using a tail count.|
|Full stabilizer s|The symmetric-square character sum has p(4d) conjugacy terms: sum_eta chi_lambda(eta)(chi_R(eta)^2+chi_R(eta squared))/(2 z_eta), R=(d^4). Character recursion work and integer/rational bit bounds still need pricing.|
|Provisional02 minor|Supply certified full-H invariant columns already expressed in the adapted basis, their total stored support N, forbidden row count F, bit sizes, and a specified b-square minor with b>=b_gate. Projection extraction is linear in N once the expansion exists; elimination on F by s costs O(F s min(F,s)) field operations and O(Fs) dense scalar slots. A selected minor uses O(b^3) operations and b^2 slots after its entries are obtained. Basis construction/conversion is additional, presently unpriced work.|
|06 padding minor|r K_d output scalar slots. If highest-weight circuits are supplied, a naive multiplication of homogeneous intermediate degrees e,f costs at most K_e K_f pair accumulations modulo the matching relation; sum this over actual circuit gates. For five-variable restrictions, each of the six q_sigma expands from at most5^4 ordered terms, hence at most6*5^4 before collecting. Price each circuit's live supports, coefficient bits and selected minor extraction; the final r-square determinant costs O(r^3) field operations.|
|Optional Hasse conversion|At most K_d support slots, but a full binomial transform has K_d^2 entries. It is not included for free in the coefficient-support bound.|

Here p(k) denotes the partition number, z_eta the usual conjugacy centralizer order, and eta squared the cycle type of the square of a permutation of type eta. These are operation counts over an exact field, not wall seconds or bytes. A modular nonzero minor is sufficient only with an integral/rational lattice certificate, denominator control and certified representation membership. Zero modulo one prime supplies no rational upper rank. No support expansion, character enumeration, highest-weight construction, basis search or minor evaluation was executed.

An eventual preflight must convert its actual terms and bit sizes to time and aggregate memory. The only small-run envelope contemplated by the assignment is existing .venv Python with -B through inspected analysis/b15_bound.py, <=60 seconds and <=512MiB, one process and one BLAS thread; a cap hit means uncomputed. The integrator must review any larger lease. **No larger lease is requested now**: there is no finite object to price, and neither09 nor10 is released.

**One next sufficient test and exact missing input, addressed to the integrator.**

The next determinant gate test is **one exact nonzero forbidden-projection minor in one explicitly supplied five-row cell**, after independent acceptance of02 and finite certification of a,s,T:
\[
 U=\min(a,T)\ge1,\qquad
 b\ge\max(0,s-U+1),\qquad
 B=\min(a,s-b)<U.                                       \tag{9}
\]
Supply its invariant basis with transposition, row/column labels, and concrete support/bit-cost price. This is the smallest missing representation-specific determinant lemma for the assessed arc. The existence of a five-row separator alone does not imply (9). If (9) is met and reviewed, the separate final gap certificate is exactly B+1 actual-padding columns as above; a nonzero minor gives D>=1. For a beyond-occurrence label also require actual determinant occurrence in that same cell: B>=1 is not such evidence.

The current result is a completed **no-candidate selection**, not a claim that (9) is impossible. No all-degree five-row exclusion, positive multiplicity gap, or improved LMR size growth is established. The LMR equation degree and its quadratic determinant-size benchmark remain distinct.

**Provenance, delivery and verification limits.**

The required board, screen, common context, stocktake and INTAKE were read. INTAKE was followed to original B16-01/02 product-source and finite-character proofs, B16-04/06 filtration/flag proofs, B16-08 shared-block proof and B16-10 arc proof, with original delivery bindings checked. The B16-12 milestone review and original accepted Dream_Upper288 report/review were read for the inherited geometry and scope. Historical matrix minors, characters and complete ideal ranks were not recomputed.

Fresh in08 are (2), the clipping/capacity deductions (5)–(7), the polynomial-ideal row exclusion (8), and this finite selection audit and cost specification. They use elementary representation/ring arguments and the explicitly accepted premises. They have not themselves received an independent08 review. The claimed source ceilings and operator convention retain the original attribution; no novelty-to-literature claim is made.

[Input hashes](../results/b17_08/input_hashes.json) pin37 local files with byte snapshots. [Metadata verification](../results/b17_08/verification.json) checks those snapshots, five reviewed B17 report bindings and six original B16 proof bindings. This is a metadata check, not mathematical replay. [Primary source notes](../results/b17_08/primary_sources.json) identify the versions and theorem locations freshly read through the web reader; remote publisher PDF bytes are not claimed archived or hashed.

Final integrity checking detected one upstream change: B15-11/delivery/b17_11/MANIFEST.json differs from its pinned snapshot. The pinned11 report and its input-hash ledger, all five reviewed worker reports, and the remaining inputs stayed unchanged at that check. This delivery uses the saved envelope and review evidence; it neither repins nor adopts the changed envelope or any new02 review. The drift is recorded in verification.json and does not change the scoped acceptance used here.

The [metadata script](../analysis/b17_08_metadata.ps1) is executable with PowerShell in Verify mode and performs no scientific arithmetic. The [manifest](../delivery/b17_08/MANIFEST.json) binds this report, snapshots, resources and limitations; it excludes its own hash. No mathematical verifier is needed for a numerical result because there is no new numerical result. Python and the unchanged wrapper were located/inspected and pinned, but not run.

The initial metadata lookup used B16-10/MANIFEST.json, which does not exist; read-only discovery resolved its actual name SHA256_MANIFEST.json, and pinning then completed. Read-only Git status returned the pre-existing B16 outputs and warned that the user's global ignore file was inaccessible. These exact operations/reasons are saved in [operations.json](../results/b17_08/operations.json). No automatic approval rejection, escalation or bypass occurred. No agents, tasks, worktrees, commits, pushes, publication, ownership/trust changes, sandbox changes, common coordination edits or closed-batch edits were made. No dependency was idle-polled.
