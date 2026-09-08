# Batch 12 S2 — global r=5 completeness: partial theorems, a rank-stratum counterexample, and exact remaining ideals

**Frozen for independent review, 8 September 2026.** This session produced new proofs and exact verification. The global assertion **R5 is not contained in D5 remains OPEN**. No canonical source or shared-checkout file was changed.

## 1. Result and preregistration

The working hypothesis was that the named exceptional supports suffice after scheme-level completion and exact treatment of all rank strata and higher contact. Acceptance required complete coverage and a universal fixed-factor image bound below 35. **That hypothesis has not been established.** The stronger assertion of global image dimension at most 31 is also unproved.

The productive results are:

1. **PROVED:** on the common-kernel/common-cokernel stratum, if the restricted 3 by 3 determinant is an irreducible cubic, the reduced second-order matrix has only ranks **0 and 9**. Its parameter kernel has dimension three. This replaces sampling by a theorem on a precisely stated open locus.
2. **PROVED:** every order-two fixed-factor leading form on that locus is s5 times an honest 3 by 3 linear determinant. Consequently its affine image dimension is **at most 29**, uniformly over this locus. This does not cover arbitrary higher contact.
3. **CERTIFIED counterexample to an unqualified rank dichotomy:** a concise five-dimensional pencil on a special common-kernel/common-cokernel incidence has reduced matrix rank **3**. An explicit arc realizes a nonzero fixed-factor order-two leading form there. Thus ranks 1 through 8 cannot be discarded globally. This does not exhibit a new normal-cone component or prove containment.
4. **PROVED:** for the affine coefficient ideal, the exceptional fibre over the zero pencil is already the projectivized determinant image closure. Treating this fibre as an independently bounded low-rank residue is circular. Projectivizing the source removes the vertex and gives a proper graph.
5. **PROVED finite fallback:** two explicit projective-source chart elimination ideals, on the target chart where the s5^4 coefficient is nonzero, suffice to decide noncontainment. They cover all schemes and all contact orders without assuming the old support enumeration. Their complete rational inputs were generated and checked. **The eliminations were not run.**

The rank-3 example falsifies a stronger rank premise, not the entire named-support hypothesis. It lies on further compression incidences already within the broad support universe. The remaining task is to bound all exceptional images there, not to infer a geometric reversal from its existence.

## 2. Inputs, repository state, and execution boundary

All four canonical documents were read: the final reconciled proposal, both Batch 11 stock-takes, and the comprehensive session source. The full standalone S2 brief, its shared requirements and frozen rank protocol, and the launch packet were read. Assignments follow the final proposal and S2 brief, including their correction that completeness alone cannot promote sampled image bounds.

The relevant original S3 text is section S3 of the consolidated Sol report, rather than a separate S3 file. The original s66 and s72 reports, s72 Markdown and JSONL ledgers, coefficient-map implementation, P/SP builders, rank-drop driver, P/C21 reduction and top-component driver, order-four driver, and the original interior certification discussion were inspected. The source families are defined in section 3 below from these inputs.

The durable checkout's HEAD and cached origin/main were both **b8d82416735f75b4c91f359b7e7708ce6a2a5455**, a descendant of the supplied readiness commit c984e2c6d59ba0bbc6ac2fdd113edf920a8aebd9. The working tree was clean. A direct live-remote query failed because the shell could not connect to GitHub; this run does not claim a fresh remote verification. The user's earlier live check is retained as source-reported readiness evidence. The obsolete absence warning at 226b4ef1 is historical.

There are 195 frozen input entries with byte lengths, SHA256 hashes, and source paths in the [input manifest](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/input_manifest.json). Git-tracked snapshots were read with `git show` at the fixed commit, avoiding a moving working-tree read. The [preflight record](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/preflight.json) contains the exact remote failure and status output.

| Input or check | Actual status |
|---|---|
| Original S3 | Present in the frozen consolidated Sol report; finite-exhaustion assertion audited, not adopted as a proved coverage theorem |
| s66/s72 reports and s72 normal-cone ledger | Present, read; numerical and universal claims separated below |
| P/C21 top-component driver | Present; inspected, not replayed |
| s69 state, ladder, seed and s63 ladder | Present and frozen; no restart, target sampling, or plethysm recomputation |
| Current certifier | Snapshot inspected; format still distinguishes recipe-style RECORDED from re-derived PASS |
| Repository self-test | Attempted in the isolated snapshot; stopped at import because `flint` is unavailable; no cases ran |
| CAS/runtime | Bundled Python works; `sympy`, `flint`, Singular and msolve were unavailable in the inspected runtime/PATH |
| New S2 computations | Standard-library Python, rational arithmetic and both house primes; no repository evaluator dependency |
| Completed Batch 12 reports | Requested Documents results directory was absent; the existing workspace S1 report was read for context and supplies no r=5 proof |

The requested Documents output location is outside this run's writable roots. Deliverables are saved in the permitted isolated directory **C:\Users\swami\Projects\gct-gpt\Batch12_Results\S2**. No permission workaround was used. No new automation, worker, external message, commit, push, or canonical promotion was made.

The current verifier commit repairs a session-73 reconstruction defect. Its presence is not evidence that this run replayed the full corpus. The broader s67/s71 reconciliation, B24 second-engine check and weighted economics were not rerun; they are not prerequisites for the independent algebra below. There is no blanket preflight PASS.

## 3. Exact mathematical setup and inherited names

Work over k=C for geometry, with all displayed equations defined over Q. Let

R=Q[x_(k,i,j): 1<=k<=5, 1<=i,j<=4],  M(s)=sum_(k=1)^5 s_k A_k,

F_alpha=[s^alpha] det M(s),  |alpha|=4,  J=(F_alpha : |alpha|=4).

There are 80 source coordinates and 70 ordinary coefficient functions. **No divided-power or polarization factorial is included.** The affine map is Phi:A^80 -> A^70. Let D5 be its Zariski image closure over C, and let B=Spec(R/J) be its full base scheme, not its reduction. Set

W=s5 Sym^3 C^5,  dim_aff W=35,  dim P(W)=34.

The projection pi retains precisely the 35 quartic coefficients with alpha_5=0. Hence membership in W is pi F=0. The full reducible cone R5 consists of arbitrary linear-factor times cubic forms and has source-recorded dimension 39; it is not the fixed-factor slice W. Since D5 is GL5-stable and GL5 acts transitively on nonzero linear factors,

W subset D5  if and only if  R5 subset D5.

The nontrivial direction follows by transporting W to each other linear-factor slice. D5 and W are cones. Any proper closed intersection D5 cap W has affine dimension at most 34.

The following are the **source-defined** families, with their GL4 by GL4 orbit closures understood. These labels are unrelated to the padded-permanent notation P_r elsewhere in the programme.

| Label | Normal-form definition | Source-recorded affine parameter-locus dimension |
|---|---|---:|
| ker | All A_k have a common nonzero kernel vector | 63 |
| coker | All images lie in a common three-plane | 63 |
| C21 | A_k(U2) subset W1 for fixed subspaces of dimensions 2 and 1 | 57 |
| C32 | A_k(U3) subset W2 for dimensions 3 and 2 | 57 |
| P | M_phi(u(s)), where phi:Lambda^2 k^4 -> k^4 and M_phi(y)t=phi(t wedge y) | 43 |
| SP | [phi N(x(s)) | c(s)], phi:k^3 -> k^4, N(x)y=x cross y, c(s) a four-vector of linear forms | 49 |
| P^T, SP^T | Transposes of the preceding families | 43, 49 |

The code orders the six wedge slots as (0,1),(0,2),(0,3),(1,2),(1,3),(2,3). It sets M_phi(y)_(a,b)=sum_c phi_(a,b,c)y_c with phi antisymmetric in b,c. SP uses the usual skew cross-product matrix. These definitions, not notation guessed from the labels, are used here. The adopted bounded-rank classification is discussed in the original reports; it is not independently recertified by this session. The fallback in section 8 does not require it.

The rank-at-most-two types in the record are: (2,0), a common two-dimensional kernel; (4,2), its transpose; (3,1), a three-dimensional domain subspace mapped into a fixed line; and the padded three-by-three skew type diag(N(x),0), with left/right changes of frame. Lower-rank and lower-span degenerations must be retained.

## 4. New theorem: the ker/coker rank dichotomy on the integral-cubic locus

Put a common-kernel/common-cokernel base pencil into the constant frame

M0(s) = diag(B(s),0),

where B is a 3 by 3 matrix of linear forms. Write S=k[s1,s2,s3,s4], B'=B|_(s5=0), and f=det B'. Assume **f is irreducible over k**, in particular nonzero. This is an explicit restriction on the base point. For geometry over C it means absolute irreducibility of a rational example.

For an arc M0+tN+t^2H+..., write N in blocks as [[A,b],[c^T,m]]. The first coefficient is g1=m det B, so g1=0 forces m=0. The second coefficient is

g2=h det B-c^T adj(B)b,  h=H_(4,4).

Therefore pi g2=0 is solvable in h exactly when

c'^T adj(B')b' = 0 in S_4/(f S_1).                                      (4.1)

This is the intrinsic version of the s66/s72 bilinear system. For fixed b', define

L_b : S_1^3 -> S_4/(f S_1),  c' |-> c'^T adj(B')b'.

It has a 31-dimensional target and a 12-dimensional displayed domain. Its rank agrees with the reduced 31 by 12 matrix in adapted tangent coordinates. To see the coordinate issue explicitly, the full off-diagonal blocks have 15 coefficients each; quotienting by the common tangent directions B(s)v and w^T B(s) removes three each. Restriction to s5=0, then quotienting by B'v or w^T B', has a nine-dimensional image and three-dimensional kernel on each reduced 12-space. The displayed c' space has the same nine-dimensional quotient. At an invertible fifth coefficient B5 it is also a literal gauge section, obtained by setting the s5 coefficient to zero after subtraction of w^T B. Invertibility of B5 is not needed for the rank argument.

**Theorem 4.1.** Under the irreducibility hypothesis:

* L_b=0 exactly when b'=B'v for a constant vector v in k^3.
* Otherwise ker L_b={w^T B':w in k^3}, so rank L_b=9.
* The kernel of the linear parameter map b' |-> L_b has dimension 3.
* Set-theoretically, the bilinear solution variety is the union of the two rulings b' in B'k^3 and c'^T in k^3 B'. Each has dimension 15 in the displayed 24 coordinates and their intersection has dimension 6.

**Proof.** The domain A=S/(f) is integral. Over its fraction field B' has rank exactly two: its determinant is zero, while some degree-two cofactor is nonzero and cannot be divisible by the irreducible degree-three f. Thus adj(B') has rank one over this fraction field.

If adj(B')b'=0 in A^3, its three degree-three polynomial entries are constant multiples of f, so adj(B')b'=f v for a constant vector v. Multiplying by B' gives f b'=f B'v in S^3, whence b'=B'v. The converse follows from adj(B')B'=f I. The same argument on the left shows that c'^T adj(B')=0 in A^3 exactly when c'^T=w^T B'.

If b' is outside B'k^3, the vector adj(B')b' is nonzero in the fraction field. Since adj(B') has rank one, c'^T adj(B')b'=0 there forces c'^T adj(B')=0 there, hence in A. The preceding paragraph identifies the kernel as precisely the three-dimensional constant-row space. Injectivity of v |-> B'v and w |-> w^T B' follows from det B' nonzero. This proves every rank and the two-ruling assertion. QED.

By the Nullstellensatz the **radical** of the bilinear coefficient ideal, at a fixed such B', is the intersection of the two ruling ideals. This is not a claim that its scheme ideal is reduced, nor a computation of the full Rees algebra. In particular it does not settle the scheme structure at the intersection of the rulings or higher contact.

An explicit absolutely irreducible control is

B' = [[x,y,0],[0,x,z],[w,0,x]],  f=x^3+yzw.

Viewed as a polynomial in y over k[x,z,w], it is primitive because gcd(zw,x^3)=1, and it is linear and irreducible over the fraction field. Gauss's lemma proves irreducibility over every field. The proof above is thus applicable over Q, C, and both house primes, without a guessed good-reduction hypothesis.

## 5. New universal order-two image bound on that locus

**Theorem 5.1.** Under the hypothesis of Theorem 4.1, every nonzero order-two leading form satisfying pi g2=0 belongs to s5 times the set of 3 by 3 linear determinants. Its total affine image, as all these base and arc parameters vary, has dimension at most 29.

**Proof.** By Theorem 4.1 either b'=B'v or c'^T=w^T B' for constant v or w. Transposition interchanges the cases. In the first case write b=Bv+s5 d with d a constant three-vector. Then

g2=(h-c^T v)det B-s5 c^T adj(B)d.

Restriction to s5=0 and f nonzero force h-c^T v=s5 a for a constant a. Hence

g2/s5 = a det B-c^T adj(B)d
       = det [[B,d],[c^T,a]].                                            (5.1)

The last column is constant. If it is zero the polynomial is zero; otherwise a constant invertible row operation takes it to a multiple of the fourth basis vector. Expansion along that column gives a scalar multiple of a 3 by 3 linear determinant, with the scalar absorbed in a row. The transpose case is identical.

For the dimension bound, 3 by 3 pencils in five variables have 45 parameters. The determinant-preserving pairs (P,Q) with det(P)det(Q)=1 form a 17-dimensional group. Their action on a generic five-tuple has a one-dimensional stabilizer, consisting of (aI,a^-1 I), hence 16-dimensional orbits in fibres. The stabilizer assertion holds on a nonempty open set: take one matrix I, a second diagonal with distinct entries, and a third cyclic permutation matrix; their common centralizer is scalar. Therefore the image closure of this irreducible 45-dimensional parameter space has dimension at most 45-16=29. Every special determinant image is in that same closure. This proves the uniform bound in (5.1). QED.

This is a new structural upper bound, **not a Jacobian estimate**. It covers all solutions of the second-order fixed-factor equations on the specified integral-cubic locus, including its rank-zero ruling. It does not claim that all higher-contact directions there are second-order directions. The order-one fixed-factor image on this locus has the same 3 by 3 determinant description and bound.

## 6. Explicit intermediate-rank point and actual arc

Let (x,y,z,w,v)=(s1,s2,s3,s4,s5), and set

B(s) = [[x+v,w,0],[0,y+v,v],[0,0,z+v]],  M0=diag(B,0).

Its five coefficient matrices are linearly independent: in the upper block they are E11,E22,E33,E12,I+E23. Thus this is a genuine five-dimensional pencil, with matrix rank three at a general s, common kernel and cokernel e4, and rank dPhi=5. Also B5=I+E23 is invertible, so the gauge used in section 4 is available. The restricted determinant is the **reducible** cubic xyz.

Take b'=(w,0,0)^T. The reduced map is

L_b(c') = [wyz c'_1] in S_4/(xyz S_1).

The x coefficient of c'_1 disappears, and its y,z,w coefficients have independent images wy^2z, wyz^2, w^2yz. The other two components of c' contribute zero. Thus **rank L_b=3 exactly**, with a nine-dimensional kernel. This rank is intrinsic to the reduced quotient; it is not an artefact of adding a scalar tangent direction.

It also occurs in a valid fixed-factor arc. Set

b=(w,0,0)^T,  c=(x,0,0)^T,
M(t) = [[B,t b],[t c^T,t^2 w]].

The block determinant identity gives, as an identity in Z[x,y,z,w,v,t],

det M(t)=t^2{w det B-c^T adj(B)b}
        =t^2 v w (y+v)(z+v).

The leading form is nonzero and belongs to W. This exhibits an actual order-two exceptional direction, rather than merely an unsolved quadratic constraint.

The point lies on additional compression incidences. Its output is itself a simple exact determinant; it is **not** a counterexample to an image bound below 35. It refutes only the global removal of intermediate rank strata and identifies the reducible-restricted-cubic support as necessary. The older statement “no intermediate rank was observed” is consistent with this example. The JSONL ledger's stronger “constant rank 9, no intermediate strata” is not.

Stored rational matrices, kernels, pivot rows/columns and minors are in the [rank certificates](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/ker_coker_certificates.json). The [arc artifact](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/intermediate_rank3_arc.json) gives all five base matrices and the leading polynomial. The matrices have ranks 9,0,3,9 over Q and at both house primes; the two rank-nine cases use different b inputs. The intermediate rank-three minor is nonzero integrally. These finite checks certify these matrices; universal assertions use the proofs above.

## 7. The affine vertex and the correct closure argument

Let m=(all 80 source coordinates). Since J is generated by homogeneous polynomials of the same degree four,

F_m(J)=direct_sum_(n>=0) J^n/mJ^n  is isomorphic to  k[F_alpha],

with the latter algebra regraded so that F_alpha has degree one.

**Proof.** J^n is generated in degree 4n, and its degree-4n part is the span of the products of n generators. All higher-degree terms lie in mJ^n. Thus the quotient in degree n is exactly that product span, and the multiplication is the same. Relations among products are precisely the homogeneous relations of the coefficient image algebra. QED.

Because J is contained in m, the fibre of gr_J R at m is this special-fibre algebra. Consequently

E_0 = Proj F_m(J) = P(D5).                                               (7.1)

This is a statement about a **fibre**; it does not assert that E_0 is a new irreducible component of the entire exceptional divisor. But its fixed-factor image is already P(D5 cap W). Bounding it by the desired number is exactly the original problem. A rank-at-most-one/zero-pencil leading-term shortcut cannot replace that obligation. Likewise, at a nonzero rank-two base point, an identity for e2 settles that leading coefficient when it is nonzero; if it cancels, it is not a bound on every later leading coefficient.

Remove the vertex by using the rational map

P^79 --[F_alpha]--> P^69,

and its graph closure Gamma=Bl_(sheaf J) P^79. The graph lies in P^79 times P^69, so its projection q to P^69 is proper. It has image P(D5): its image is closed and contains the actual image densely. The exceptional divisor of this projective-source blowup has the local description Proj gr_J R_i on source charts. These standard Rees and blowup-chart facts are also recorded in the [Stacks Project, blowing up](https://stacks.math.columbia.edu/tag/01OF) and [blowup algebras](https://stacks.math.columbia.edu/tag/052P); (7.1) and the specialized argument here were proved above.

Every arc through the affine vertex can alternatively be divided by its common smallest source-coordinate power of t; its determinant gains only a scalar power t^(4e), leaving the same projective leading form at a nonzero source limit. Thus this correction does not discard directions.

Set Gamma_W=q^-1(P(W)). Properness implies

q(Gamma_W)=P(D5) cap P(W).

One must form the full graph **before** imposing W. In general closure(image Phi) cap W differs from closure(image Phi cap W). For a small exact example, the source chart y=1 of [x:y] |-> [x^2:xy] has target-chart equation x^2-zx=0. Saturation by x gives x-z=0, after which z=0 leaves the boundary point x=0. Imposing z=0 before saturation gives (x^2):x^infinity=(1), wrongly losing that point.

## 8. Exhaustive two-chart fallback, with complete generated inputs

This is a finite exact algebra problem with a **proved coverage implication**, not a claim that the eliminations completed.

Index source variables by x_(16k+4i+j), with k,i,j zero-based. Order quartic exponents recursively, first exponent increasing; alpha0=(0,0,0,0,4), so F0=det A5. Take the nonempty target chart y0=1. Within P(W) this is A^34. It is enough to prove D5 misses a point of this chart.

For each projective source chart x_h=1, write R_h=Q[the other 79 x coordinates] and f_alpha=F_alpha|_(x_h=1). In R_h[y1,...,y69] form

H_h = (f_alpha-y_alpha f0 : alpha!=0) : f0^infinity.                     (8.1)

This is the exact graph chart: its coordinate ring is R_h[J/f0], a subalgebra of R_h[1/f0]. For an implementation without guessing syzygies,

H_h = (1-u f0, f_alpha-y_alpha f0 : alpha!=0) cap R_h[y].                (8.2)

Now, **after** this elimination, impose y_alpha=0 for alpha5=0, and contract to the remaining 34 good y variables:

I_h = (H_h + (y_alpha:alpha5=0)) cap Q[y_alpha:alpha5>0, alpha!=0].       (8.3)

The closed set V(I_h) is the closure of the image of this part of Gamma_W. Nilpotents in the original base ideal have already been accounted for through the full graph saturation. No reduced-base classification or contact cutoff is used.

**Theorem 8.1 (two representative jobs).** It suffices to compute I_0 and I_64. If both are nonzero ideals, then W is not contained in D5, hence R5 is not contained in D5; in particular dim_aff(D5 cap W)<=34. If either ideal is exactly zero, then W is contained in D5.

**Proof.** The 80 source charts cover P^79 and their graph preimages. A row and a column permutation carry any nonzero entry of A_k to its (1,1) entry; they change the determinant only by a nonzero scalar, so target ratios are unchanged. If k<=4, a permutation of s1,...,s4 carries the source chart to x0=1. If k=5, it is carried to x64=1. These finite permutations preserve W, the target chart y0=1, and image dimensions. Thus the 80 image closures are finite transforms of the two displayed image closures.

If I_0 and I_64 are nonzero, each closure has dimension at most 33 in A^34; their finite union cannot fill it. Any noncontainment on this chart proves W is not contained in D5. Proper closedness then gives the affine bound 34 on the whole W, including the chart complement. Conversely, if an I_h is zero, that chart image is dense in A^34. Its closure lies in the closed set P(D5) cap P(W), which therefore contains this entire chart and its closure P(W). QED.

An empty image has unit ideal and counts as nonzero. No claim that either current I_h is nonzero or zero is made. The stronger affine bound 31 would need the other target charts, or a further structural argument; the two-chart criterion is designed for the permitted strict-bound fallback.

The [chart manifest](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/chart_manifest.json) defines every coordinate. The generated rational files are [chart 0](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/cas/chart_0_Q.sing) and [chart 64](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/cas/chart_64_Q.sing), produced by the [generator](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/build_chart_jobs.py).

Each job has 149 variables: u, 79 source coordinates and 69 target ratios. The term order is lex with u first, source coordinates in numeric order, then target coordinates in numeric order. The first ideal has 70 generators; after eliminating u, add the 35 W equations, eliminate source coordinates, and map to the 34-variable rational target ring. All 15,000 determinant monomial terms were generated by the 24 permutation terms and 5^4 coefficient choices. Twelve fresh integer coefficient evaluations agreed with a direct numerical determinant, including the anchor det A5, with corresponding checks at both house primes.

**CAS status:** equations generated and checked; no Singular Gröbner basis, saturation, associated-prime list, or image ideal was computed here. Script execution itself has not been tested in Singular. The mathematical specification (8.1)-(8.3) is authoritative. This is a complete finite fallback, not a runtime estimate or a promise that unrestricted elimination is cheap.

## 9. Coverage and proof ledger

The rows below cover the inherited component table, including transposes. “Recorded” values are not new universal bounds. The exact two-chart fallback covers all rows simultaneously, with its image inequalities still open.

| Support or image-changing sublocus | Source-recorded affine image values | Newly established evidence | Exact outstanding obligation |
|---|---|---|---|
| Interior through B4 | maximum 31; ker/coker 29, C21/C32 31, SP 27, P 25, skew 22 | Exact divisibility reparameterization is valid | Universal branch bounds and lower-span coverage; original upper certification uses sampling |
| Smooth ker/coker | 29 | Smooth-base contact lemma is valid with scheme-smoothness hypothesis; integral restricted-cubic order-one bound 29 follows here | Bound all parameter subloci or use (8.3) |
| Smooth C21/C32 | 28 | Fresh rational calibration at their incidence gives the corrected zero transverse quotient | Universal fixed-factor images, including rank changes of the constrained map |
| Smooth P/P^T, SP/SP^T | 24,26 | Definitions and contact lemma audited | Universal image bounds; generic samples do not cover all subloci |
| P cap SP; P cap coker; P cap SP^T | 26/23;24;23 | No new universal image result | Full graph restrictions, not only the generic second-order primes |
| P cap C32; SP cap C21 | 27/24/23;25/28 | Exact full-jet and Rees specifications in the handoff | Extra quadratic branches, nonlinear order-four image, and arbitrary higher contact |
| P cap C21 | top 19, special 12; 26-dimensional quadratic locus | a-linear structure inspected in code, not lifted or replayed here | All consistent C(b) ranks 0 through 9, lower-dimensional components, rational identities and full graph bounds |
| SP cap C32; SP cap coker | 24;26/28 | No new universal image result | All incidence degenerations and higher contact |
| C21 cap C32; ker cap C21 | 27;29/28 | Tangent calibration is 16/64,57/57,intersection 50,span 64,quotient 0 at an exact fresh point | Universal exceptional-image bounds |
| ker cap coker, integral restricted cubic | 29; sampled matrix ranks 0/9 | **PROVED ranks 0/9 and order-two image <=29**, sections 4-5 | Full higher-contact scheme, especially the intersection of the two rulings |
| ker cap coker, nonzero reducible restricted cubic | No separately certified universal bound | **CERTIFIED rank 3 and actual order-two arc**, section 6 | Factorization locus, all intermediate ranks, full graph images |
| ker cap coker, restricted cubic identically zero | Not separately bounded by the generic 31 by 12 model | Identified as separate equations: pi dPhi changes rank | Use all 20 restricted determinant equations; rebuild the quotient and full graph |
| Rank-two (2,0),(4,2),(3,1) and their incidences | <=31; sample 18 on one incidence | First nonzero order-two determinant identities remain valid in their stated scope | Cancellations e2=0 and later leading forms; deterministic interior bound if invoked |
| Padded-skew, rank of x equal to 3,2,1 | 28/26;19;9 | Inherited e2=mq-beta gamma formula retained | All factorization components and exceptional degenerations, not numerical monotonicity |
| Rank at most one, nonzero pencil | <=31 in the record | Specific order-three replacement-row identity retained | Vanishing of that coefficient and later contact |
| Zero pencil in affine source | Hidden in broad deeper-rank wording | **PROVED E0=P(D5)** | Remove by projectivizing; do not claim a new bound on E0 |
| Unlisted associated structure or further intersections | No certificate supplied | **PROVED coverage by full projective graph charts** | I0,I64, or certified reductions preserving all their images |

The smooth-base contact lemma says that when the local scheme R/J is regular, one can choose independent generators f1,...,fc of J locally and write F=Hf with H at the point injective. Every leading coefficient then lies in im dPhi and every such nonzero vector is realizable. This proves contact-order invariance of the fibre, not the numerical dimension of its fixed-factor image over an entire family. Regularity of the scheme, not just smoothness of its reduction, is essential.

The original consolidated S3 section 3.5 asserts a four-residue exhaustion theorem, but no chart, support-ideal identity, or elimination certificate establishes that assertion there. Smoothness only restricts new components to the scheme-singular locus. It does not prove that the generic points sampled in each named incidence exhaust its image-changing subloci.

A simple illustration of the invalid specialization step is Z={(a,b):a b=0}, where b is an m-vector. Over a!=0 the only b is zero; over a=0 an entire m-dimensional fibre appears. The vertical component is not in the closure of the generic kernel ruling. Semicontinuity cannot supply an image bound for a component whose coverage has not been proved.

The original interior proof also deserves a precise label: its discussion explicitly calls pointwise Jacobian ranks lower bounds, then uses wide random points and a Schwartz-Zippel probability to rule out a missed higher minor. That is a **probabilistic upper-bound protocol**, not an exact polynomial-identity certificate over Q. Rational evaluation at finitely many points does not change this. No new contradictory interior point was found or sought. The value 31 is retained as source-recorded evidence, but not silently used as a deterministic theorem here.

## 10. Checks actually completed and characteristic-zero semantics

The [verification summary](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/verification_summary.json) and [verifier source](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/verify_s2.py) are reproducible with standard-library Python.

| Check | Result and interpretation |
|---|---|
| Two integral-cubic b inputs, one kernel input, one reducible input | Exact rational ranks 9,9,0,3; same at 2147483647 and 2147483629 |
| Rational rank certificates | Pivot rows/columns, nonzero Bareiss minors and a full exact kernel stored for each finite matrix |
| Cofactor identities | Polynomial adj(B)B=det(B)I checked on both explicit restricted matrices |
| Fresh C21/C32 tangent calibration, seed 660072 | dPhi rank 16, kernel 64; tangent ranks 57 and 57; intersection 50; sum 64; transverse quotient **zero**, over Q and both primes |
| Tangent semantic check | Every tangent generator annihilates dPhi coefficient-by-coefficient; dPhi independently agrees with entry replacement in the determinant |
| Block g2 formula, seed 20260908 | Eight fresh integer cases; coefficient extracted by nine-point interpolation of direct 4 by 4 numerical determinants agrees with h det B-c adj(B)b over Q and both primes |
| Rank-three arc, seed 20260909 | Symbolic leading-form identity; 24 independent numerical determinant checks; base coefficient span exactly five |
| Generic coefficient-map generator, seed 2077002 | 12 fresh source/input points across two charts, exact determinant agreement and house-prime agreement; full 70-coefficient combinatorial formula supplied |
| P/C21 top-component msolve run | NOT RUN; no claim of a replayed 19 or certified dimension 26 |
| Full nonlinear order-four or Rees elimination | NOT RUN; exact remaining problems supplied |
| Full repository self-test | Import failure, no cases ran; NOT PASS |

The rational RREF kernels are computed and checked over Q, so their finite-matrix upper bounds do not rely on lifting modular kernels. Nonzero rational minors are retained, and neither house prime divides their relevant denominators or annihilates the displayed rank. Universal upper bounds in sections 4-5 have structural proofs. The independent numerical interpolation path uses direct permutation determinants, distinct from the symbolic cofactor construction; it checks evaluator semantics on fresh inputs rather than merely rerunning a rank routine.

The tangent matrices use ordinary quartic coefficients in the 70-exponent order and columns (k,row,column) in ascending zero-based order. The two compression masks in this fresh calibration are simultaneous coordinate permutations of the original normal forms; the exact masks and point matrices are in the artifact. Every rank claim here is tied to its actual matrix or theorem. These are not HWV evaluation matrices, and no source multiplicity rank follows from them.

## 11. Finite handoff and final status

The [s77 handoff](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/HANDOFF_s77.md) specifies the two exhaustive chart ideals, localized residual ideals, the full nonlinear order-four equations, term orders and required certificates. It is addressed to the integrator and has **not** been sent to another worker. The [replay instructions](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/REPLAY.md) identify commands and distinguish completed checks from generated CAS work. The final artifact manifest hashes the deliverables and all frozen inputs.

**BANK after independent review:** the integral-cubic rank theorem and order-two bound, the rank-three counterexample and actual arc, the vertex correction, and the exhaustive two-chart reduction. **KILL:** an unqualified global 0/9 assertion, upper bounds from generic samples, truncating all contact to the normal degree, or applying an e2 identity after e2 has vanished. **OPEN:** global image bounds and the desired r=5 noncontainment. **CONDITIONAL:** nonzero exact image ideals in both representative charts would close noncontainment with the sufficient global bound 34.

The frozen LMR protocol is unchanged: lambda=(65,17,2^7), delta=24, a=274; B24=2168 is a reported precursor dimension; LMR gives determinant rank at most 273; determinant rank 273 and padded rank 274 remain OPEN. True padding is ell per3, distinct from ell c. This S2 session computes no new LMR determinant or padded rank and makes no new conclusion about D. Run once; outputs remain frozen for independent review before promotion.
