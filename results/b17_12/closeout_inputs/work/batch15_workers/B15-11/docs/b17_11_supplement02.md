**B17-11 supplement02 — COMPLETE: ACCEPTED scoped independent review of B17-02.**

14 September 2026. The [newly completed Slot02 report](../../B15-02/docs/b17_02_report.md), its full proof, executable and saved coefficient certificate pass this review. The result is a valid representation-specific **necessary extension bound**, together with a proved negative result for original-entry diagonal arcs. It supplies no positive forbidden-weight rank, strict numerical improvement, equation module or multiplicity gap.

The accepted [first-stage report](b17_11_report.md) and its certificates remain unchanged. Its historical “02 unfinished” status is superseded only by this supplement. Its 54 manifest-listed artifacts were checked before and after this work. The previous manifest is preserved byte-for-byte as [FIRST_STAGE_MANIFEST.json](../delivery/b17_11/supplement02/FIRST_STAGE_MANIFEST.json); the [current manifest](../delivery/b17_11/MANIFEST.json) adds this separately pinned review. No unfinished04 or held09/10 work was awaited.

| Claim | Decision | Essential scope |
|---|---|---|
| Explicit skew/symmetric polynomial arc and shared Taylor identities | **ACCEPTED** | Identities in all16 independent coordinates, including singular S. |
| Q0 is in the det4 closure and outside its orbit | **ACCEPTED** | Reducible cubic tangent cone at a triple point; no boundary-component classification. |
| Coordinate label and orbit multiplicity source | **ACCEPTED** | S_lambda(W*) paired with (S_lambda W)^H, for the full stabilizer of the adapted f. |
| Forbidden-weight interval [0,2d] and bound min(a,s-rank C) | **ACCEPTED** | Necessary for extension to the polynomial coordinate ring; not sufficient. |
| Strict-improvement threshold b>=s-min(a,s)+1 | **ACCEPTED** | Rank floor and s must refer to the same invariant source. |
| All-degree failure of original-entry diagonal arcs | **ACCEPTED** | The corresponding determinant arc must itself be polynomial of degree L; forbidden interval is [0,dL]. |
| A useful positive rank b or numerical improvement | **UNVERIFIED / UNCOMPUTED** | No finite representation basis or rank certificate was supplied. |

**Arc and endpoint audit.** With the producer's variable ordering, the ordinary matrix entries are

    [[a,  r1,        r2,        r3       ],
     [c1, s11,       s12-v3,    s13+v2   ],
     [c2, s12+v3,    s22,       s23-v1   ],
     [c3, s13-v2,    s23+v1,    s33      ]].

This is an invertible change of all16 linear coordinates, not a symmetric specialization. Its determinant in the declared row-major/order convention is **-8**. In particular the three off-diagonal pairs are independent in characteristic zero. The adapted determinant f is genuinely in the original det4 orbit. The group gamma acts on its linear forms with weights -1 on a,r, zero on v, and +1 on c,S, with dimensions 4,3,9 and determinant t^5.

For the cross-product matrix A(v), the following identities hold polynomially:

    det(A+tS) = t*v^T*S*v + t^3*det(S),
    adj(A+tS) = v*v^T - t*A(Sv) + t^2*adj(S).

I checked the sign of the middle term and the symmetric off-diagonal factors. One independent derivation of the adjugate is the three-dimensional Cayley–Hamilton formula E^2-tr(E)E+e2(E)I; it gives the same nine entries as the producer's cofactors. The division-free block determinant formula then gives

    gamma(t)f = Q0+t*Q1+t^2*Q2,
    Q0 = a*v^T*S*v - (r*v)(v^T*c),
    Q1 = r*A(Sv)*c,
    Q2 = a*det(S) - r*adj(S)*c.

There is no remaining t pole. The receiver multiplies the first matrix row by t before its determinant expansion, proves that the resulting polynomial is divisible by t, then divides by that monomial. It never assumes S or A+tS invertible. For t!=0 this is an orbit point; because X is closed, its polynomial continuation at zero lies in X. The cubic skew precursor is established in [Hüttenhain–Lairez, Lemma5](https://arxiv.org/pdf/1512.02437); its component-classification conclusion is not imported here.

At the nonzero coordinate point J with S=I and all other coordinates zero, the four ordinary Taylor coefficients are, respectively,

    t^2*a,
    t^2*(a*tr(S)-r*c),
    a*(v^T*v) + t*r*A(v)*c
      + t^2*(a*e2(S)-r*((tr S)I-S)*c),
    Q0+t*Q1+t^2*Q2.

Each uses the same a,r,c,v,S. At t=1 these equal the original shared-block formulas with E=A+S: tr(A)=0 and e2(A+S)=v^T v+e2(S). At t=0 the first two vanish and the third is the nonzero reducible cubic a(v1^2+v2^2+v3^2). Hence Q0 has multiplicity exactly three at J.

For the generic determinant at a matrix of rank r, invertible constant row/column changes give multiplicity 4-r and initial form a nonzero scalar times the determinant of the missing (4-r)-square block. Every triple point of an invertible coordinate transform of det4 therefore has an irreducible det3 initial form. Irreducibility survives adjoining unused tangent coordinates and invertible linear changes. Q0's reducible cubic contradicts this. Thus Q0 is outside the orbit, while the polynomial arc proves Q0 belongs to its closure. This argument does not assert nonmembership in every singular linear-substitution image or that the endpoint generates a boundary component.

**Coordinate convention and orbit source.** Here W is the space of linear forms, f belongs to Sym^4 W and G=GL(W). Its coefficient functions belong to Sym(Sym^4 W*). Consequently the coordinate module is S_lambda(W*), while its matrix-coefficient source is

    M_lambda = (S_lambda W)^H,
    H = Stab_G(f),
    h_(ell,z)(g f) = ell(g z).

The function is well-defined because z is H-fixed. Under left translation of functions, ell transforms in (S_lambda W)*, as required. This is compatible with the first-stage positive coefficient convention by putting V_ref=W* and identifying the groups contragrediently; no transposed partition or determinant twist is introduced.

In particular gamma weights in the **source** S_lambda W are the exponents of t in ell(gamma(t)z). The representation action on raw coordinate function c_alpha has the opposite weight, -sum(alpha_i*w_i), because functions act by pullback through gamma inverse. Confusing those two actions would incorrectly reverse the forbidden interval. Evaluation of a coefficient on gamma(t)f has exponent +sum(alpha_i*w_i), consistent with the source formula.

The orbit decomposition uses the full determinant stabilizer, including transposition. Restricting S_lambda(C4 tensor C4) to the two SL4 factors leaves rectangular types (d,d,d,d) on both sides when |lambda|=4d; transposition selects the symmetric subspace of the corresponding Kronecker carrier. This gives s=dim M_lambda, the symmetric rectangular coefficient. The dual placement and full-stabilizer identification are explicitly supported by [Bürgisser–Landsberg–Manivel–Weyman, §4.1 and §5.2, especially Proposition5.2.1](https://arxiv.org/pdf/0907.2850v2).

For numerical use, the invariant basis must be transported by the same coordinate change as f. If T sends standard matrix-entry variables to the adapted forms above, then H=T H_standard T^(-1), and its Schur-module invariants are transported by S_lambda(T). The adapted transpose sends r to c^T, c to r^T, v to -v and fixes a,S. A basis fixed only by the connected group is a larger source; a rank measured there cannot be subtracted from the smaller full-H dimension s. For example, an abstract two-dimensional connected source may have one full-H line and a forbidden projection only on the other line: subtracting that rank from the full-H dimension would wrongly remove the full-H line. This is a logical control, not an asserted determinant representation example.

**Extension theorem and exact clipping threshold.** Fix one finite d>=0 and lambda partitioning 4d, with length at most16. Write U_lambda=S_lambda W and let E_lambda be the subspace of M_lambda whose entire matrix-coefficient copy belongs to C[X]_d. Restriction to the dense orbit is injective. Complete reducibility therefore identifies dim E_lambda=m_det(d,lambda).

The central scalar qI acts by q^(4d) on U_lambda and sends f to q^4 f. Thus the coordinate copy has coefficient degree d. Since C[X] is a graded quotient of ambient polynomial functions, every ell has a homogeneous degree-d ambient representative P_ell when z lies in E_lambda. Pulling it back to the explicit arc gives

    sum_k t^k*ell(pr_k z) = P_ell(Q0+t*Q1+t^2*Q2).

The right side is polynomial with exponents in the **inclusive** interval [0,2d]. Equality on C* implies equality of Laurent coefficients. It holds for every ell, so pr_k z=0 for all k<0 and k>2d. Therefore

    E_lambda is contained in ker C,
    C : M_lambda -> direct sum of (U_lambda)_k for k outside [0,2d],
    m_det <= min(a, dim ker C) = min(a, s-rank C).

This is a global upper bound: every function on the closure has a polynomial representative, and the arc is a morphism A1->X. No normality of X, local rational identity, or unproved denominator extension is used. The reverse inclusion ker C contained in E_lambda is not proved. One arc need not detect all extension failures.

The Schur module embeds in W^(tensor4d), so all its gamma weights lie in [-4d,4d]. Under the Levi decomposition W=W_- direct-sum W_0 direct-sum W_+, a constituent S_alpha W_- tensor S_beta W_0 tensor S_delta W_+ has weight |delta|-|alpha| and the usual iterated LR multiplicity. This correctly labels the proposed projection carrier; no such decomposition was numerically enumerated. For d=0 the constant has weight0. For d=1, the actual invariant vector f has nonzero components at both weights0 and2, and also at1: neither endpoint may be excluded. This control also checks the sign convention directly on an extending function.

For an exact rank floor b<=rank C, put B=min(a,s-b) and B0=min(a,s). Since a>=B0,

    B<B0  iff  s-b<B0  iff  b>=s-B0+1.

All quantities are integer dimensions. This proves the producer's threshold, including the cases a=0, s=0 or s>a. For example artificial values a=3,s=5,b=1 leave B=B0=3, whereas b=3 gives B=2. These are arithmetic controls, not computed representation cells. A certified nonzero forbidden vector alone is insufficient when ambient clipping hides the drop. Likewise s must be exact, or replaced consistently by a proved dimension/upper bound for the very source on which the rank floor was obtained.

**All-degree negative control for entry-diagonal arcs.** Consider a one-parameter subgroup diagonal on the **original independent matrix entries**, x_ij -> t^(w_ij)x_ij, with integer weights. Assume its determinant image is polynomial of degree L. Each of the24 determinant monomials is a distinct coordinate monomial, so cancellation cannot hide a permutation exponent outside [0,L]. Thus every sum_i w_(i,sigma(i)) belongs to that interval, even if some individual w_ij are negative.

Embed a polynomial Schur module of size4d into W^(tensor4d). The determinant-preserving row and column diagonal SL4 tori act diagonally on the tensor-word basis. Every word with nonzero coefficient in an invariant vector must have equal row counts and equal column counts. Total length4d makes each count d. Its occurrence matrix N is a nonnegative integer4x4 matrix with all margins d.

For d>0 its support graph has a perfect matching: for any subset R of rows, its d|R| incident edges end in columns with capacity at most d apiece, giving at least |R| neighboring columns. Hall's criterion applies. Remove one matching and repeat on the margins d-1. Therefore N is a sum of d permutation matrices. Its gamma weight is a sum of d permutation exponents and belongs to [0,dL]. This holds for every supported tensor word, hence every H-invariant vector and every polynomial lambda of size4d. For d=0 it is immediate. The forbidden projection outside [0,dL] is identically zero in every degree.

Both hypotheses are essential: torus invariance supplies the equal margins, and polynomiality supplies the permutation interval. The independent control uses one fixed degree-three occurrence matrix and an entry-weight matrix with some negative entries, all permutation weights in [0,8], and total word weight8. Removing three matchings recovers that weight. A word with all12 occurrences in the negative-weight (1,1) entry has negative weight and fails the margin condition. This illustrates the hypotheses; the all-degree conclusion rests on the proof above, not finite testing.

The adapted gamma mixes each original off-diagonal entry pair through symmetric/skew coordinates. It is not an original-entry diagonal subgroup, so the negative lemma does not prove its forbidden map zero. Conversely escaping that lemma does not prove its map has positive rank in any useful cell.

**Independent arithmetic, controls and provenance.** Exactly one new control ran through the re-inspected, unchanged original wrapper, using the existing `.venv/python.exe -B`, 60 seconds / 512 MiB, one process and one configured BLAS thread. It exited0 in **0.0226015 seconds**, with **13,914,112 bytes** peak aggregate Job Object commitment. It checked all18 separately pinned inputs. Thirteen delivery/provenance bindings matched, including all11 Slot02 artifacts, the original B16-08 proof and its inherited Hessian report binding.

The new [receiver](../analysis/b17_11_supplement02_verify.py) imports no producer code. It uses exponent-vector polynomials and a subset determinant recurrence instead of the producer's permutation expansion; a Cayley–Hamilton adjugate instead of cofactors; and binomial translation instead of re-expanding the translated matrix. Every saved arc coefficient and all four Taylor coefficient records match. Supports are15/18/23 and90, and all nine adjugate entries agree. The largest dictionary has90 monomials; there were656 monomial-pair products. Wrong Q1 sign and omission of a symmetric factor2 were rejected. The clipping equivalence passed196 tiny artificial integer cases. No H-invariant basis, representation rank, census, or padding evaluation was computed.

The evidence chain follows the current Slot02 delivery through Batch16/INTAKE slot08, the original [B16-08 proof](../../B15-08/docs/b16_08_proof.md), its artifact/input manifests, the slot12 intake receipt, and the original Hessian11_1631 shared formulas. The historical 34-coordinate/630-column negative computation was not replayed; it is not a premise of the new extension bound. Literature on orbit functions and the cubic skew precursor was freshly checked; [source notes](../results/b17_11/supplement02/primary_sources.json) identify versions and locations. Remote PDF bytes are not claimed hash-archived. Local evidence snapshots and hashes are in the supplementary manifest.

The [preflight](b17_11_supplement02_preflight.md), [verification](../results/b17_11/supplement02/verification.json), [resource receipt](../results/logs/b17_11_supplement02_resources.json), [binding checks](../results/b17_11/supplement02/delivery_bindings.json) and [decisions](../results/b17_11/supplement02/decisions.json) record the exact scope. There was no cap hit, second new computation, heavy lease, approval rejection, agent, new worktree, commit, push, publication, configuration/trust/ownership change or write to another worktree. The earlier accepted report and certificates remain byte-identical.

**One next sufficient test for the integrator.** Supply one finite (d,lambda), certified a,s and correctly supported padding ceiling U, plus an exact full-H invariant basis in the adapted coordinates. Price a sparse forbidden-projection minor before execution and certify rank b satisfying b>=s-min(a,s)+1 and B=min(a,s-b)<U. Such a certificate would give a strict global determinant upper bound, not a positive gap. A later actual independent z*per3 coordinate floor r>B is still required in the same cell; actual determinant occurrence must also be proved for any beyond-occurrence label. This supplement authorizes use of the theorem with those inputs, not a representation computation or a claim of numerical improvement. No such basis/rank input is available here, and this bounded review is complete.
