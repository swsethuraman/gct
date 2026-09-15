# B16-08: exact bounded elimination of shared determinant jets

13 September 2026. New work by gpt-6-astra/xhigh. The reused worktree head is
`0256ed2561964fe4085ad847518e3fcf85837024`, individually frozen by Batch16.
No common merged base is asserted.

## Statement and scope

Let K be a field of characteristic zero, J=diag(0,1,1,1), and let
B1,B2,B3 be arbitrary 4-by-4 matrices of independent variables. Write

    det(J+x1 B1+x2 B2+x3 B3) = sum_(1<=|alpha|<=4) f_alpha(B) x^alpha.

There are 34 coefficients f_alpha. Let S=K[y_alpha : 1<=|alpha|<=4] and
phi:S -> K[B1,B2,B3] send y_alpha to f_alpha. Define the graph ideal

    G = (y_alpha-f_alpha(B)) in K[y,B].

The exact result is

    (G intersect S) intersect S_(ordinary coefficient degree <=2) = {0}.

This computes one bounded part of the elimination ideal. It is not a
claim that the entire elimination ideal is zero. It is also not a
Jacobian-rank argument: the certificate proves injectivity on the entire
specified 630-dimensional polynomial space using nonzero minors.

## Universal shared-block identity

For any commutative characteristic-zero algebra, write the same matrix
of linear forms in every order as X=[[a,r],[c,E]], with E of size three.
In the polynomial ring of its sixteen unrestricted entries,

    det(J+tX) = t F1 + t^2 F2 + t^3 F3 + t^4 F4,
    F1 = a,
    F2 = a tr(E) - r c,
    F3 = a e2(E) - r ((tr E) I-E)c,
    F4 = a det(E) - r adj(E)c,
    e2(E) = sum_(i<j)(Eii Ejj-Eij Eji).

The proof is the block determinant identity

    det([[a,r],[c,D]]) = a det(D)-r adj(D)c,

which follows by cofactor expansion and is polynomial even when D is
singular. Insert D=I+tE and replace a,r,c by ta,tr,tc. Cofactor expansion
also gives

    det(I+tE)=1+t tr(E)+t^2 e2(E)+t^3 det(E),
    adj(I+tE)=I+t((tr E)I-E)+t^2 adj(E).

Collecting powers of t proves all four formulas. These identities hold
over Z using the displayed integral formula for e2; no matrix-inverse
assumption remains. Thus arbitrary substitutions for all sixteen entries,
including noncommuting matrix directions and dependent linear forms,
preserve the identity. The executable certificate independently expands
the 24 determinant permutations and the block expressions in the sixteen
unrestricted entry variables. Their residual is identically zero; the
four homogeneous supports have 1,6,18,24 signed monomials. All 49 monomials
are saved in `results/b16_08/certificate.json`.

For an arbitrary rank-three base matrix M0 and arbitrary directions Ai,
choose invertible constant L,R with LM0R=J. Set Bi=LAiR and
mu=det(L)det(R). Then

    det(J+sum xi Bi) = mu det(M0+sum xi Ai).

This precisely transports the formulas to every rank-three determinant
basepoint, with the stated common scalar. No claim that J-normalization
works at rank-two basepoints is made. No root/basepoint elimination has
been performed. The identities here retain realization variables and
are not new polynomial equations in quartic coefficients.

## Why the bounded elimination certificate proves an exact result

Give every entry of Bi multidegree ei in N^3, and give y_alpha
multidegree alpha. The substitution phi preserves this grading.
The 630 monomials 1, y_alpha, y_alpha y_beta (alpha<=beta) split into
165 multidegree blocks, each with at most 10 columns. Images from
different blocks cannot cancel: their parameter monomials have distinct
multidegrees. The grading is a polynomial-ring fact, not a sampling
assumption.

For each block w with m columns, the certificate saves m selected rows
from ten explicitly saved integer triples (B1,B2,B3), together with the
entire square evaluation matrix reduced modulo p=2147483647 and its
nonzero determinant. Every evaluated polynomial is obtained by actual
shared-block substitution. For each block, a nonzero determinant modulo
p proves the determinant of the corresponding integer evaluation matrix
is nonzero. Therefore its columns are independent over Q and over every
characteristic-zero field. This proves injectivity on each block, and
grading then proves injectivity on S_(degree<=2).

The ten points are reused across the blocks; this does not invalidate
the proof because independence is established separately after the
grading decomposition. A single ten-row evaluation matrix on all 630
columns would not prove their independence. Summing these block ranks
is justified only by the direct grading decomposition established above.

The graph ideal has quotient K[B], so its elimination ideal is exactly
ker(phi). This proves the stated elimination result without Groebner
expansion of all parameter products.

The producer expands the 49 universal entry monomials after replacing
each entry with its common three-direction linear form. The receiver
instead computes the 24 determinant permutations as polynomials in x
at each saved point. It reconstructs all 34 integer coefficients at all
ten points, all 165 square matrices and every determinant. A changed
cubic coefficient is rejected, as is a square matrix with a duplicated
row. This is a second coefficient-computation route in the same new
implementation, not an independent reviewer or independent source base.

## Support and resource pricing

The total expanded parameter support before any products is

    k + 6 k^2 + 18 k^3 + 24 k^4.

For k=3 this is 2487, split as 3,54,486,1944 by order. The largest
individual coefficient has 288 terms. These counts follow because the
49 entry monomials are squarefree in distinct matrix entries; assigning
one of k directions to each entry gives distinct parameter monomials.
The complete direct quadratic expansion has a conservative raw bound
2487^2=6185169 product terms. We did not construct it. A naive ungraded
630-by-630 evaluation matrix has 396900 entries. The saved square block
matrices total only 3072 entries; ten shared points suffice.

The preflight was saved and read before elimination. Each run had the
inspected B15 wrapper's enforced 60-second/512-MiB Windows Job Object cap,
one process and one BLAS thread. The wrapper's timer thread is solely a
deadline guard. No multiprocessing or subprocess computation was used.
Its legacy B15 labels are preserved and explicitly mapped to B16-08 in
the delivery receipt; the wrapper itself was not changed.

The initial selection of the first m rows stopped on a zero 1-by-1
minor, because one linear coefficient at the first point is zero. This
was not interpreted as a relation. Pivot-row selection among the same
ten already priced points fixed the instrument. The failed receipt is
retained alongside the successful producer and receiver receipts.

## Boundaries and next sufficient witness

This experiment concerns an affine three-direction root chart. A
homogeneous quartic in sixteen variables has C(19,4)=3876 coefficients;
its polynomial space of coefficient degree at most two has
C(3878,2)=7517503 monomials. A dehomogenized root chart using fifteen
directions has 3875 nonconstant coefficients. These counts must not be
replaced by the 34 in the instrument. A sixteen-direction affine Taylor
chart would have 4844 nonconstant coefficients and is yet another object.

No new global equation E in the 3876 quartic coefficients is proposed.
No highest weight, finite determinant ideal floor q, padding coordinate
floor r, ideal membership modulo LMR, or positive multiplicity gap is
claimed. In particular, a sixteen-variable equation can restrict to the
zero polynomial on every chosen three-direction slice, so the present
negative result does not exclude such an equation. The independent ten
variables in z*per3 remain the padding model; no inside-variable padding
substitution was made and no padding computation was run.

Any further candidate must first have a nonzero polynomial in Taylor
coefficients with an exact substitution-zero witness eliminating the
common a,r,c,E. In this chart its ordinary coefficient degree must be at
least three. There are already 7770 monomials of degree at most three
in the 34 coefficients; that extension was priced by count only and not
run. Turning a candidate into a global sixteen-variable equation then
requires root/basepoint and normalization removal, polynomiality after
denominator clearing, and an exact identity after arbitrary substitution
of all entries of all sixteen matrices in det(sum Ai xi). Ambient
nonzeroness, the finite weight and full specified LMR-image comparison
must be certified separately. For a multiplicity obstruction, a global
determinant ideal floor q and actual independent-padding coordinate
floor r must satisfy q+r>a in one finite cell.

## Attribution and inherited premises

The shared-block formulas and proposed three-direction control come
from `Hessian11_1631/REPORT.md`, original gpt-6-astra/xhigh work, reached
through the B15 intake. Its Hessian eleven-space and the older Slot05
four-space are inherited background, not replayed or enlarged here.
The original Astra review and its `hessian_relations.py`, and original
Slot05 proof and orchestration source, were read for conventions and
proof boundaries. The underlying B14 bracket work retains Claude Opus 5
attribution; none of its code or evaluator is imported into this work.

Fresh results are the unrestricted sixteen-entry symbolic verification,
the multigraded bounded elimination proof and certificate, support
prices, and executable receiver. The frozen stable numbers
ambient429, m_det418, 243<=m_pad<=288 are inherited instructions and are
not inputs to the fresh elimination proof. No B15 result, shared board,
manifest, theorem or exclusion file was modified. Exact file read hashes
are in the delivery input manifest.
