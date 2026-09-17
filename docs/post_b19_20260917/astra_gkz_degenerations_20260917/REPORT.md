# Five-block determinant degenerations: a finite organization and an exact redundancy theorem

17 September 2026. **Outcome C: this restricted family adds no forbidden-weight conditions beyond the existing arc.** Final resource results and input hashes are recorded below and in MANIFEST.json.

## 1. Plain-language verdict

GKZ's initial-form viewpoint organizes all simultaneous scalings of the five fixed blocks (a, r, c, symmetric S, skew v) into the face fan of a rectangle. There are four vertex limits, four edge limits, and the original form: nine initial-form classes. This is a classification of initial forms for this restricted torus, not of actual paths up to every equivalence, and not of all determinant degenerations.

One explicit new-to-this-report arc has reducible endpoint a v^T S v. The old arc's endpoint a v^T S v - (rv)(v^T c) is irreducible. Thus these endpoints are not equivalent under any invertible linear coordinate change. Nevertheless, the new endpoint is a further face degeneration of the old endpoint, and its necessary source condition is a consequence of the old condition.

The conclusion is stronger than a failed search: **on the full certified source M, every test constructed here factors through C**. If N collects any or all of these tests, then

    ker(C,T,N) = ker(C,T),       rank(C,T,N) = rank(C,T).

This holds without computing the unknown combined rank of (C,T), without constructing the fifth source vector, and without reading the unfinished direct-arc-relation session. The corresponding statement holds in every degree and polynomial source label, under the explicit hypotheses below. Even the stronger test that forbids holes in the exact one-parameter exponent support, rather than just poles and excessive degree, adds nothing.

The conclusion concerns universal coefficient-support tests along the specified family. It does not cover equations among allowed jets, descent between different parameter points of a limit fiber, special-locus cancellations followed by stronger normalization, anisotropic weights inside a block, or different matrix-coordinate bases. None of those are ruled out.

**Funding decision:** stop enumerating weights or coherent triangulations for this five-block family. No further computational certificate is needed to settle its comparison with C or T.

## 2. Provenance and scope controls

All paths here are relative to C:/Users/swami/Projects/gct-gpt unless explicitly absolute. INPUT_PINS.json contains raw-byte SHA-256 hashes, sizes, and absolute paths for the sources actually used. It records comparisons against supplied manifests where available. MANIFEST.json seals the final outputs. PREREG.md preserves the incremental skeleton and the decision made before the pilot.

No AGENTS.md was found in the project roots, their applicable ancestors, or the searched project trees. RUNBOOK.md and the original project's delivery_contract.md, brief_wording.md, and astra_delivery_recipe.md were read. Their historical commit/bundle instructions do not authorize actions here: this user's fresh-directory, no-Git, no-shared-ledger contract governs. No Git command, worker, carrier search, historical edit, or shared-memory write was performed.

Authoritative input sequence:

- work/claude_transverse_structure_20260916_followup/clarification_20260917/{SOURCE_HANDOFF.md,STABILIZER.md,CORRIGENDUM.md,MANIFEST.json}: source model, action and normalization, old arc, and the distinction between sampled zeros and a global kernel certificate. The stabilizer repair is respected; none of its commutant measurements is needed for our theorem.
- work/claude_source_vectors_20260917/routeA_signfilter_20260917/REPORT.md, MANIFEST.json and relevant certificates: four independent source vectors q3,q7,n02,e; transverse rank 3, certified by minor 225843 modulo 524287. This supersedes the older handoff's rank-2-or-3 status.
- work/claude_source_vectors_20260917/arc_target_dimension_followup/REPORT.md and MANIFEST.json: b_L=74, not a useful improvement on rank C<=4. We do not adopt its proposed future experiments as instructions.
- work/batch15_workers/B15-02/docs/b17_02_report.md sections 2-4; its exact identity script analysis/b17_02_verify.py; the accepted review work/batch15_workers/B15-11/docs/b17_11_supplement02.md; B18-02 report sections 1,2,4 and analysis/b18_02_carrier.py's scaling convention; B19-01 report sections 2-6.
- Original project C:/Users/swami/Projects/gct/work/docs/onset_conjecture.md, especially Theorem 1 and its degree-300 quinary det4 cap, and PROVED.md's definitions/index; B18-01 sections 1-4 and 5.1-5.2; B18-05 summary; singular-locus audit section 4.

The initial native-entry idea was rejected as duplicated: **B17-02 section 4 already proves its weight tests vanish on all stabilizer sources**, by decomposing a balanced integer matrix into permutation matrices. This report does not claim that theorem as new. The five-block extension and exact support comparison below are the selected result.

Background, not premises of the redundancy proof: dim D45=50, dim P5=39, and P5=closure{linear times arbitrary cubic} only in five variables. The old onset note records degree-300 Jacobian-cap equations with named adopted literature dependencies. Thus "no five-row determinant equations are known" would be wrong. Those equations do not supply a positive multiplicity gap here. We neither reverify the onset literature nor rely on it.

## 3. Objects and action conventions

Work over C (the polynomial identities have rational coefficients). Let W=Mat_4, and use the following sixteen independent linear coordinates:

    X = [ a   r1       r2       r3      ]
        [ c1  s11      s12-v3   s13+v2  ]
        [ c2  s12+v3   s22      s23-v1  ]
        [ c3  s13-v2   s23+v1   s33     ]
      = [[a,r],[c,S+K(v)]],

    K(v) = [[0,-v3,v2],[v3,0,-v1],[-v2,v1,0]].

The change from native entries to these coordinates is invertible (each off-diagonal symmetric/skew pair has determinant of magnitude 2). Let f=det X and X_det=closure(GL_16.f).

For k pencil variables put Y=(Y_1,...,Y_k) in W^k and

    phi(Y)(x) = det(sum_i x_i Y_i).

Applying any linear coordinate map D:W->W to the pencil means Y_i->D(Y_i), for every i. We write actions as actual substitution, z(DY), never as an implicit contragredient action. This fixes the signs of all weights.

For d>=1 let M be any finite source subspace of degree-4d polynomials on W^k such that

    z(PYQ) = (det P det Q)^d z(Y),       z(Y^T)=z(Y)

for all P,Q in GL_4. A specified highest-weight source M_lambda is such a subspace. The interval theorem needs only the two diagonal-torus symmetries; the strengthened support theorem also needs transposition. The argument therefore applies to the full M of the user's diagnostic, not just its four known vectors.

Let E be its genuine coefficient subspace: z=H o phi where H is a homogeneous degree-d polynomial in ordinary quartic coefficients, in the relevant label. It is essential that polynomial descent is assumed only for E, not for arbitrary z in M.

In the diagnostic k=d=5, lambda=(4,4,4,4,4), dim M=5, E=span(e), e=H5 o phi, and a=m_det=1. We use the updated facts rank T=3 and 2<=rank C<=4. None of our proofs needs a numerical value of rank(C,T).

## 4. The polynomial and its projected toric configuration

The division-free block determinant identity and the 3-by-3 cofactor identities give

    det X = a det(S+K) - r adj(S+K)c
          = G12 + G02 + G01 + G10 + G00,

where the subscripts record (degree in a, degree in v):

| label | nonzero polynomial | (p,q) |
|---|---|---|
| G12 | a v^T S v | (1,2) |
| G02 | -(rv)(v^T c) | (0,2) |
| G01 | r K(Sv)c | (0,1) |
| G10 | a det S | (1,0) |
| G00 | -r adj(S)c | (0,0) |

For completeness, the cofactor identities underlying this are

    det(K(v)+tS)=t v^T S v+t^3 det S,
    adj(K(v)+tS)=vv^T-t K(Sv)+t^2 adj S.

They follow by expanding the three-by-three cofactors; the existing B17-02 proof and the independent exact pilot both check signs. All formulas are global polynomial identities, with no assumption that S or a coefficient is invertible.

Let A_full be the set of exponent vectors of the nonzero monomials of f in the sixteen adapted variables. Its projection to (p,q) is exactly

    A = {(0,0),(1,0),(0,1),(0,2),(1,2)},
    P = conv(A) = [0,1] x [0,2].

A describes torus characters of five linearly independent polynomial groups. It is not the native determinant/permanent support, nor are the Gpq independent matrix variables. Their linear independence follows from their different (p,q) degrees.

An optional precise toric model is the projective closure of

    (s,t) |-> [1:s:t:t^2:s*t^2] in P^4,

with coordinates labelled by A. Its homogeneous coordinate algebra is the image of Z_pq -> z*s^p*t^q in C[z,s,t]. The linear injection Z_pq -> Gpq identifies this torus orbit of a coefficient point with the two-parameter projective family of determinant forms below. This is the promised map from the combinatorial configuration to the determinant problem.

## 5. Allowed weights, actual orbit points, and the finite organization

Choose any five integers w=(A0,R0,C0,S0,V0). Define D_w(t) by scaling a,r,c,S,v by t to these powers. It is an algebraic GL_16-valued map for t in C*, diagonal in the fixed adapted basis. This is a change of polynomial variables/matrix-coordinate space, not an assertion about arbitrary coefficient scalings.

Put

    beta = R0+C0+2S0,
    u = A0-R0-C0+S0,
    h = V0-S0.

The weight of Gpq is beta+u*p+h*q. Let m_w and M_w be the minimum and maximum of these five weights. Then

    F_w(t) = t^(-m_w) det(D_w(t)X)
           = sum_(p,q in A) t^(beta+u*p+h*q-m_w) Gpq

is a polynomial in t of degree L_w=M_w-m_w, with nonzero constant term. For t!=0 it is an actual orbit point: multiply D_w(t)X on the left by diag(t^(-m_w),1,1,1). This is an invertible linear map on W with determinant polynomial exactly F_w(t). No fourth-root choice or unproved coefficient action is required.

The polynomial map A^1->Sym^4(W*) has punctured image in the determinant orbit, so its endpoint is in X_det. Substituting arbitrary linear forms for all sixteen coordinates gives a polynomial family in D4k=closure(phi(W^k)). This holds on all pencils, not just a chart; the universal limit is nonzero but a special pencil can specialize it to zero.

Three independent weight directions with u=h=0 are block-scalar left/right multiplications: choose diagonal blocks (l,kI_3) on the left and (m,nI_3) on the right. The weights are (l+m,l+n,k+m,k+n,k+n). They account exactly for the kernel of w->(u,h) and multiply f by a scalar t^beta. Normalization removes this scalar, including its degree-d character on source functions.

Conversely every integer (u,h) is realized by w=(u,0,0,0,h). Thus the projective family has exactly the two effective parameters s,t above.

**Equivalence chosen:** weights are initial-form-equivalent when they give the same minimizing face of P. These equivalence classes are the relatively open cones of the normal fan of P. They classify universal initial polynomials, not entire arcs: positive reparametrizations preserve classes, but different slopes within a cone can have different intermediate exponents. We do not quotient by all GL_16 symmetries or assert pairwise GL-inequivalence of the nine forms.

| sign of u | sign of h | limit |
|---|---|---|
| + | + | G00 |
| - | + | G10 |
| + | - | G02 |
| - | - | G12 |
| 0 | + | G00+G10 |
| 0 | - | G02+G12 (old endpoint) |
| + | 0 | G00+G01+G02 |
| - | 0 | G10+G12 |
| 0 | 0 | f |

This is the complete finite initial-form classification of the chosen family: four vertices, four edges, one full face. The zero cone gives the constant normalized family. There remain infinitely many actual one-parameter weight paths.

### Normal fan, secondary fan, and initial ideals are different

Our nine classes belong to the **normal fan of P**. A secondary fan instead starts with independent heights eta_pq on the five points and records coherent subdivisions of their convex hull. The heights permitted here are eta_pq=beta+u*p+h*q, affine functions on A. The lifted points all lie in a single affine plane, so their lower envelope gives the trivial subdivision. Thus these heights lie in secondary-fan lineality; they do not yield nontrivial triangulations of A.

Likewise, on A_full, native variable scaling induces a linear height. It does not create a nontrivial coherent subdivision of that configuration either. This does not prevent taking an initial form of the polynomial f: retaining a minimizing face of f and subdividing its configuration are different operations.

For the embedded toric variety above, an affine height preserves its toric ideal: a binomial relation with equal exponent sums has equal total height on both terms. In particular its initial ideal for such a height is unchanged. By contrast, the hypersurface ideal (f) in the original variable ring has initial ideal (in_w f): the lowest component of a product is the product of lowest components in a polynomial domain. Neither assertion computes an initial ideal of I(X_det) or I(D45).

An arbitrary non-affine coefficient height has no orbit-membership justification from this construction. We do not claim that no such family could ever be realized by a different GL_16 map. We simply have not supplied that additional bridge. No Hilbert-Mumford classification is invoked.

## 6. One explicit candidate arc and its precise novelty

Use the matrix

    B(t) = [[a/t, r],[t*c, K(v)+t*S]],      t in C*.

This is D_w(t)X for w=(-1,0,1,1,0). It has weights -1 on a, 0 on r and v, and +1 on c and S; hence it is invertible as a map on all sixteen coordinates for every t!=0. Its determinant as a GL_16 linear map is t^8. Here beta=3,u=h=-1,m_w=0. Direct substitution gives

    F(t) = det B(t)
         = a v^T S v
           - t (rv)(v^T c)
           + t^2 [a det S + r K(Sv)c]
           - t^3 r adj(S)c.                                      (6.1)

There is no scalar normalization in (6.1). Although matrix entries have a pole, the determinant has none. Its nonzero limit G12=a v^T S v is in the affine determinant orbit closure. It is reducible, and therefore is not an orbit point of the irreducible generic determinant. One elementary reason that the determinant is irreducible is that rank-at-most-three matrices are the image of (4-by-3,3-by-4) matrix pairs under multiplication, an irreducible set, and the determinant has a simple zero at diag(1,1,1,0).

For any pencil Y, decompose each Y_i into (a_i,r_i,c_i,S_i,v_i), apply this same formula, and use a(x)=sum x_i a_i, etc. Equation (6.1) is valid identically. The construction requires no special locus. The endpoint may degenerate further for special pencils.

**Not a reparametrization or symmetry-conjugate of the old arc, in the universal setting.** Write q=v^T S v. It is irreducible in C[v,S]: as a linear polynomial in the S entries, its coefficients have no common nonconstant factor (they include v1^2,v2^2,v3^2), and over C(v) it has degree one. It remains irreducible after adjoining r,c. Since q has S-dependence, it divides neither rv nor v^T c. Consequently q and (rv)(v^T c) are coprime, and

    Q_old = a*q - (rv)(v^T c)

is a primitive degree-one polynomial in a and is irreducible. A factorization would have one factor of a-degree zero dividing both coefficients. In contrast, G12=a*q is reducible. Invertible coordinate changes and scalar factors preserve reducibility; a positive reparametrization preserves the endpoint. This proves the asserted inequivalence of endpoints, hence excludes those equivalences of arcs.

**But it is an already-controlled refinement.** Scaling a by s^(-1) in Q_old and multiplying by s gives aq-s(rv)(v^T c), with limit aq. Combinatorially the vertex (1,2) is a face of the old top edge. We make no claim of historical novelty for this endpoint. Its novelty relative to the old path is geometric only; its test is redundant, as now proved.

## 7. Necessary-condition proof

Decompose a polynomial z in the adapted pencil variables by total block degrees

    alpha=#a, rho=#r, kappa=#c, sigma=#S, nu=#v,

summed over all pencil indices. Denote its simultaneous (alpha,nu) component by P_alpha,nu z. These components live in the ambient polynomial space; they need not separately belong to M.

**Lemma 7.1 (global weight identity).** Every monomial of z in M satisfies

    alpha+rho=d,   alpha+kappa=d,
    sigma=2d+alpha-nu,   0<=alpha<=d,   nu>=0.              (7.1)

Proof. Apply independent row and column diagonal matrices P,Q to the native matrix entries. Equality of torus characters in the semi-invariance formula forces each monomial's row and column totals to be d. The adapted substitution mixes only the lower-right 3-by-3 block, so it preserves the first-row and first-column counts. Total degree is 4d. These observations give all of (7.1). This proof is the same mechanism as B18-02 Lemma 4.1 and does not assume any sampled identity.

It follows that

    z(D_w(t)Y) = sum_(alpha,nu)
        t^(d*beta+u*alpha+h*nu) P_alpha,nu z(Y).            (7.2)

Set V=C[W^k]_(4d). Define N_w:M->direct_sum V by projecting the Laurent polynomial t^(-d*m_w) z(D_w(t)Y) onto the coefficients whose t-exponents lie outside [0,d*L_w]. Its finite codomain is indexed by the forbidden integer weights occurring in V. This is an explicitly defined linear map on polynomials, not a collection of sampled values.

**Proposition 7.2. E is contained in ker N_w.** If z=H o phi then homogeneity gives

    t^(-d*m_w) z(D_w(t)Y) = H(F_w(t;Y)).

Every coefficient of F_w(t;Y) is a polynomial in t of degree at most L_w and has no negative exponent. A degree-d polynomial H therefore has t-degree at most dL_w and no pole. This holds identically in all Y, proving N_w z=0. Alternatively, the upper-degree assertion follows by reversing t and normalizing the reversed family. This is a global necessary source condition on functions descending to the entire closure. It is not itself an equation in quartic coefficients, and it is not sufficient for descent.

For the candidate (6.1), its source weight is 3d-alpha-nu. Thus

    N_candidate z = projection onto alpha+nu>3d.           (7.3)

No upper violation is possible because alpha,nu>=0. Formula (7.3) is the exact negative-power projection; it vanishes on E by Proposition 7.2.

## 8. Exact comparison with C, including support holes

The original arc has w_old=(-1,-1,1,1,0), beta=2,u=0,h=-1,m=0,L=2. Equations (7.1)-(7.2) give its familiar condition

    C z = projection onto nu>2d.

The upper forbidden range is empty. In the diagnostic this is precisely the full skew-degree-11 and skew-degree-12 projection, not its sampled S0 restriction.

**Theorem 8.1 (interval tests).** For every permitted w there is an explicit linear map L_w on the old forbidden polynomial space such that N_w=L_w C on M. Moreover the simultaneous kernel of all N_w is ker C.

Proof. If Cz=0, its (alpha,nu) support lies in

    [0,d] x [0,2d] = dP.

The functional u*alpha+h*nu consequently lies between d times the minimum and maximum of u*p+h*q on P. Adding d*beta and subtracting d*m_w puts all source weights in [0,dL_w]. Therefore N_w z=0. More explicitly, to obtain L_w, regroup the components of Cz by the weight d*beta+u*alpha+h*nu and retain precisely the forbidden ones. No component with nu<=2d can contribute, so this is the exact identity N_w=L_w C, not just an inclusion observed on samples. Conversely the family includes w_old, whose N_w is C. This proves equality of simultaneous kernels.

**Theorem 8.2 (exact exponent-support tests).** Replace the interval in N_w by the d-fold sumset of the exact exponents occurring in F_w, and call this stronger map N_w^support. The same simultaneous kernel equality holds.

Proof. The d-fold sum of A is exactly

    A_d = {(p,q) in Z^2: 0<=p<=d, 0<=q<=2d,
                          p<d or q is even}.             (8.1)

To see this, choose p factors with first coordinate 1; each contributes 0 or 2 to q. The d-p remaining factors contribute 0,1,or 2. If p=d, q must be even and every even q in range occurs. If p<d, the intervals [2j,2j+2(d-p)], j=0,...,p, cover every integer from 0 to 2d. This proves (8.1) in all degrees.

For z in ker C, (7.1) puts the support in dP. If alpha=d then rho=kappa=0. Transposition fixes a,S and sends v to -v; on this slice it forces every odd-nu component to vanish. Hence the actual support of z is contained in A_d. Projecting A_d by d*beta+u*p+h*q-d*m_w gives exactly the d-fold sumset of the exponents of F_w. Therefore N_w^support vanishes on ker C. The old arc has exponent set {0,1,2}, whose d-fold sumset is every integer in [0,2d]; so its support test is exactly C, proving equality. Again, explicit projections give factorization through C.

This also explains why detecting a lattice hole on the right edge of the rectangle buys nothing: the full stabilizer's transposition already forbids that hole. Connected-stabilizer-only sources would not justify this strengthened conclusion; transpose invariance is an essential hypothesis here.

**Corollary 8.3 (the requested comparison).** Any stack N of the interval or exact-support tests satisfies

    rank(C,T,N)=rank(C,T),   ker(C,T,N)=ker(C,T).

All rows of N lie in the row space of C. The statement is over characteristic zero on the complete M. It is not a restricted four-column rank assertion, a sampled-kernel claim, or a new rank measurement.

For the entire infinite set of integer weights, take the product of their finite codomains, or equivalently their finite-dimensional row span in M*. The rank statement has the same meaning in either formulation; no infinite direct-sum support assumption is used.

The candidate's inequality follows especially simply: C=0 gives nu<=2d, while symmetry gives alpha<=d, hence alpha+nu<=3d. Nothing about the unknown fifth vector can change this.

## 9. What GKZ contributes, and the external-dependency audit

Primary reading: Ed Segal, [A short guide to GKZ, arXiv:2412.14748v1](https://arxiv.org/pdf/2412.14748v1), 19 December 2024, 21 pages. Downloaded to the temporary literature cache, not the delivery tree. SHA-256:

    8c8d9d058c878e77c953928c63d9d8fc9db184c46e6f94bf4d5a66f9eb31afc1

The version and date were checked on page 1. All sections were read. The following references are a dependency map, not an invocation of unverified machinery:

| survey location | content examined | role here |
|---|---|---|
| section 1.2, pp.3-5; (1.8), Theorem 1.9 | principal A-determinant, face contributions, extremal terms | warning against interpreting a toric boundary factor as determinant-specific |
| section 2.1, pp.6-7 | embedded toric variety and projective dual discriminant | distinguishes a chosen toric configuration from the determinant orbit closure |
| section 2.2, pp.8-10; Claim 2.13 and footnote 6 | initial limits and coherent triangulations; Chow/Hilbert distinction | motivates the finite organization, with the distinction proved in section 5 |
| section 2.3, pp.11-14; Theorem 2.22 | associated hypersurfaces and extremal Chow terms | read; not needed for the redundancy theorem |
| section 2.4, pp.14-17; (2.27) | logarithmic derivatives and principal-determinant factors | read; no discriminant expansion or resultant condition imposed |
| section 3.1, pp.18-19; (3.2) | Koszul complexes and determinants of complexes | read; not the project's Cayley differential identity |
| section 3.2, pp.20-21 | several different toric varieties and secondary data | reinforces the distinction from the normal fan used here |

Concrete contribution: a projected torus-character configuration, its face organization, and a support-semigroup check that prevents a false upgrade from new limits to new tests. The normal-fan and affine-height assertions were proved directly above; we do not need the GKZ triangulation/Chow theorem as a premise.

**No unverified load-bearing external theorem remains in the selected result.** The determinant identity, weight relation, finite classification, support sumset, and rank comparison are proved here. Elementary polynomial factorization is used explicitly in section 6. The historical native-entry negative result is attributed, not used to infer the five-block result. The survey's deeper theorem references (GKZ pp.260,302) were not independently verified and are not load-bearing. A claim about general coherent triangulations, toric flatness, principal-determinant multiplicities, or all orbit degenerations would require new primary-source verification and is deliberately not made.

The toric variety in section 4 is defined as an image closure; no normality claim is needed. In particular the missing point (1,1) is handled by transpose symmetry, not silently filled by an assumed normal toric semigroup.

## 10. Early rejection checks and achievement levels

- Native determinant and permanent have identical support; the native-entry route is already silent by B17-02. Here signs enter the symmetric/skew cancellation, which is explicitly proved from the determinant identity.
- Every t!=0 member is justified by an invertible map on matrix-coordinate space. Arbitrary independent scaling of the five polynomial groups or of individual determinant coefficients is not assumed to stay in the orbit.
- Constant left/right block scalings are removed explicitly; varying (u,h) need not be a left/right multiplication. The adapted basis mixes original entries.
- The candidate endpoint is not symmetry-equivalent to the old universal endpoint, but is an iterated face limit and adds no condition.
- The theorem concerns all source vectors and all pencils, not a smooth-root chart.
- Neither ordinary singularity nor a principal A-determinant face factor is used as a separator. A product ell*C already has d(ell*C)=C*dell+ell*dC and is singular along ell=C=0.
- No claim about arbitrary cubic padding in six or more variables is made.
- The singular-pencil audit's five-row vanishing and the product-structure identities of B18-05 are background warnings, not new tests produced here.

Achievement levels:

1. A globally necessary source condition: **proved**, with a global proof of redundancy.
2. A new determinant coefficient equation: **not produced**.
3. Such an equation nonzero on actual padding: **not produced**.
4. Positive multiplicity gap: **not produced**; the diagnostic has a=m_det=1.
5. Asymptotic lower bound: **not produced**.

## 11. Pilot, controls, resource receipts

The initial process inspection and SESSION_STATE.json found no running Python/CAS computation; no worker or separate computational session was started. One synchronous interpreter process is used. The existing wrapper work/batch15_workers/B15-02/analysis/b15_bound.py was inspected before launch: Windows Job Object process/job memory caps, 60-second watchdog, thread environment set to 1, original PID and JSON receipts. It does not enforce an OS active-process count; the pilot itself imports only standard-library arithmetic modules and starts no child processes or numerical threads.

Pre-registered estimate: <5 seconds, <64 MiB. Hard contract: at most 3 pilots, each <=60 seconds/512 MiB, total <=180 seconds. The pre-registered computation is a single exact sparse identity check, not a source search.

The pilot independently compares the 24-permutation determinant with the five cofactor groups, checks (6.1), verifies the weight formula on every expanded determinant monomial for a small fixed set of weights, and checks (8.1) in degrees 1 through 6. These finite checks supplement, and do not replace, the all-degree proofs.

Controls that can fail: change the sign of G01 and require rejection; test a*v1^3 and require its forbidden exponent -1; retain the missing support point (d,1) as a rejection control. No zero at finitely many points is promoted to a global identity.

Pilot status: **passed**, one wrapped run, exit 0. Wrapper wall time 0.0202754999 seconds; the complete shell invocation returned in 0.344 seconds. Peak Job Object memory was 13,111,296 bytes (12.50 MiB); peak working set was 20,664,320 bytes. The original reading is retained in results/logs/p1_fiveblock_exact_resources.json and summarized in MANIFEST.json. This used one of three permitted pilots and less than one second of the 180-second computational budget. No retry or other symbolic computation was run.

Exact code: pilot_exact.py. Certificate: results/pilot_exact.json. The expansion has 56 distinct adapted-coordinate monomials. All 13,608 fixed weight/monomial checks and 307 small-degree lattice controls passed. The wrong-sign control produced 18 nonzero residual terms, and the invalid monomial produced exponent -1 as required. The exact support counts for d=1,...,6 were 5,13,25,41,61,85; these are controls, not the proof of (8.1). Original PID, resource JSON and console output are preserved.

Reproduction from this directory (existing interpreter and wrapper are read-only):

    & '../batch15_workers/B15-02/.venv/python.exe' -B '../batch15_workers/B15-02/analysis/b15_bound.py' --seconds 60 --memory-mb 512 --name reviewer_unique_name --slot astra_gkz_20260917 pilot_exact.py

The exact absolute invocation is preserved in MANIFEST.json. A reviewer should use a fresh output directory and receipt name to preserve both the original result JSON and original receipts.

Literature download and PDF text extraction were document I/O, not symbolic pilots. The first network attempt was blocked by the sandbox; the operation-specific download approval was then used successfully. No sandbox or Git-trust setting changed. Literature PDF/text remain in C:/Users/swami/AppData/Local/Temp/astra_gkz_20260917_literature, not this delivery. A failed web screenshot request produced no artifact and no mathematical computation.

## 12. Smallest next step and realistic cost

The comparison certificate is already the factorization N=L C in Theorems 8.1-8.2. It needs no carrier evaluations or fan enumeration. Independent review is a short symbolic/weight-identity audit; the included exact pilot is priced under five seconds.

**Single action worth taking: close this five-block weight-search route and retain the theorem as an exclusion for future proposals.** Do not fund additional weights within it. Any future degeneration proposal must leave this block-scalar torus (or ask an explicitly different question about allowed-jet relations or limit-fiber descent), give its own actual-orbit map, and price that new comparison separately. This session does not nominate or price an unconstructed outside-family certificate.
