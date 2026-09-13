# B15-09 proof fragment: complete determinant pullbacks

Model: gpt-6-astra. Statuses below distinguish exact proofs from inherited
input records. This fragment proposes no change to the shared theorem index.

## Claim 09.1: a polynomial parameter map with dense image

**Status: EXACT (proof).** Work over Q and extend to C for Zariski closures.
Let D_{n,N} be the closure of the image of

    (B_0,...,B_k) -> det(x_0 B_0 + sum_(i=1)^k y_i B_i),  k=N-1.

This definition includes all restrictions of the n-by-n determinant. For
N>=n^2 it agrees with the GL_N orbit closure of the determinant with unused
variables: full-rank linear maps onto Mat_n are dense and are restrictions
of invertible changes of the N variables. For N<n^2 the image definition is
used; it is not the orbit of a fixed N-variable form.

Use independent c, t_1,...,t_k and A_i in sl_n, and set

    Phi(c,t,A) = c det((x_0 + sum_i t_i y_i/n) I_n + sum_i y_i A_i).

This is a polynomial map over Q; its only fixed denominators divide powers
of n. It lands in the original image, since left multiplication of the whole
pencil by diag(c,1,...,1) supplies the factor c. On the dense open subset of
the original parameter domain where det B_0 != 0, put

    c=det B_0, C_i=B_0^(-1)B_i,
    t_i=tr C_i, A_i=C_i-(t_i/n)I_n.

Then the two displayed forms agree. The original domain is irreducible,
and det B_0 is a nonzero polynomial; its open subset is dense. For a
continuous polynomial map, the image of a dense subset is dense in the
closure of the full image. Hence Phi has dense image in D_{n,N}. A source
polynomial with zero pullback under Phi vanishes on all of D_{n,N}, including
the boundary c=0. No assertion about generic conjugacy fibers is needed.

For a homogeneous highest-weight source H of degree delta, fixed by
x_0 -> x_0+linear(y), and with positive weight (lambda_1,tau), write

    psi(A) = H(det(x_0 I_n + A(y))).

Unipotent invariance and scalar homogeneity give H(Phi)=c^delta psi(A).
Consequently psi=0 is equivalent to global determinant-side vanishing.
Scaling A_i scales the variable y_i, so psi is homogeneous of degree tau_i
in the n^2-1 independent entries of block A_i. It therefore lies in the
explicit complete containing space

    T_tau = tensor_i Sym^(tau_i)(Q^(n^2-1)),
    dim T_tau = product_i binomial(tau_i+n^2-2,n^2-2).

For n=4 these are 15-entry traceless blocks. This statement holds at a finite
degree; equality with an entire stable highest-weight space is not assumed.
The complete containing space can be much larger than the actual image.

**Verifier and dependencies:** algebra above; the symbolic 2x2 and explicit
whole-polynomial 4x4 controls in `analysis/b15_09_global.py`. S57 suggested
the chart; the density argument here is supplied independently.

## Claim 09.2: complete interpolation gives a global upper bound

**Status: EXACT (linear algebra).** Let S have an explicit independent rational
basis of size s, let P:S->T be the polynomial pullback, and prove membership
in a complete finite polynomial space T of dimension H. At explicit rational
points let E:T->Q^b have exact rank t and EP have rank r. Then

    dim im P <= min(s,r+H-t),
    dim ker P >= max(0,s-r-H+t).

Indeed dim im P = dim E(im P)+dim(im P intersect ker E), and dim ker E=H-t.
For t=H, evaluation is injective and the computed source kernel equals the
global polynomial kernel. For a full highest-weight basis s=a this is

    U_det = min(a,r+H-t),  i_det_lb=max(0,a-r-H+t).

For a mere coefficient weight space, it is a weight-space bound only, until
the highest-weight interpretation is separately proved. A kernel vector of
the sampled matrix is not itself a global equation when t<H. Exact integer
coefficient expansion is an alternative: every possible monomial coefficient
is checked, so there is no interpolation completeness premise to infer.

**Verifier:** `exact_kernel`, `image_upper_bound`, full monomial support check,
and the independent tensor-grid evaluation in `analysis/b15_09_global.py`.
CI73 provides the inherited proof pattern, not any reused values or dimension.

## Claim 09.3: the complete small pullback has kernel det M

**Status: EXACT (fresh coefficient expansion and complete interpolation).**
For four independent traceless 2x2 matrices set

    A_i = [[a_i,b_i],[c_i,-a_i]],
    q(y)=det(sum_i y_i A_i)=y^T M y/2,
    M_ij=-tr(A_i A_j)=-2a_i a_j-b_i c_j-c_i b_j.

The equality follows either from 2x2 determinant expansion or A^2+det(A)I=0.
All M entries are integral polynomials in twelve independent parameters.
The symmetric entries have coefficient weights e_i+e_j. All monomials of
weight (2,2,2,2) are enumerated before allocation. There are 17: one with
four loops, six with a two-cycle and two loops, three with two two-cycles,
four with a three-cycle and a loop, and three with a four-cycle. Distinct
monomials in the ten independent symmetric entries are independent over Q.

Each pullback has degree two in each triple (a_i,b_i,c_i). The full containing
space has dimension 6^4=1296. The coefficient matrix has 17 source rows and
1296 ordered parameter-monomial columns, 710 nonzero entries, and maximal
absolute coefficient 16. Its exact rational rank is 16. The delivered
16-by-16 minor has integer determinant

    70368744177664 = 2^46 != 0.

The determinant det M has the above 17 monomials with coefficients 1,-1,1,2,-2
for the five cycle types. Its substitution cancels identically in the sparse
integer polynomial ring. The resulting primitive coefficient vector is
exactly the one-dimensional kernel computed by rational RREF.

Independently, order the local quadratic monomials as

    a^2, b^2, c^2, ab, ac, bc

and the local nodes as e_a,e_b,e_c,e_a+e_b,e_a+e_c,e_b+e_c. Their evaluation
matrix has diagonal blocks I_3 and I_3 and an upper-right zero block, hence
determinant 1. Its fourth tensor power is the complete 1296-point evaluation
matrix and has determinant 1^(4*6^3)=1. This factorization proves full
completeness without allocating the square matrix. Every one of the 17*1296
source evaluations is regenerated from products of actual integer 2x2
matrices, rather than from the symbolic coefficient rows. Exact RREF again
gives rank 16 and the same kernel. Every value agrees with the independently
expanded polynomial. The source-row/point-column convention is A^T K=0.

The compact certificate lists every source monomial, every kernel coefficient,
the six explicit nodes, Cartesian order, both minor index sets, and matrix
digests. The script reconstructs all points and matrices; saved matrices are
not necessary for replay. There are no modular reconstructions or uniqueness
flags: all calculations are in Z or Q.

The point-free explanation is that the trace pairing is nondegenerate on
the three-dimensional vector space sl_2, so a four-vector Gram matrix has
rank at most three. Its three-direction minor at diag(1,-1), E12, E21 has
determinant 2. This nonzero minor is a separate liveness control.

**Verifier:** `results/b15_09/final01/certificate.json`, regenerated by
`analysis/b15_09_global.py`; no inherited numerical premise.

## Claim 09.4: i_det=1 in a full finite multiplicity control

**Status: EXACT (proof plus fresh small controls).** Here n=2, delta=5,
ambient variable count N=5, lambda=(2,2,2,2,2). Let a general quadric be

    f(x_0,y)=c x_0^2+x_0 g(y)+y^T G y=x^T S x,
    S=[[c,g^T/2],[g/2,G]],  F(f)=det(2S).

The diagonal entries of 2S are twice ordinary square coefficients and the
off-diagonal entries are ordinary mixed coefficients. Thus they equal the
degree-two factorial symbols m_alpha=alpha!c_alpha, or 2! times normalized
polar tensor entries. In the stable control M=2Q as well; det M=2^4 det Q.
A two-column epsilon contraction with four valence-two letters is 4! det M;
with five letters it is 5! F. These nonzero rational rescalings are explicit.
B14-06 uses normalized polar entries, whereas these integral controls use
factorial symbols. There is no silent change of basis to a banked source.

The polynomial F has degree five, is fixed by the upper unipotent group,
and transforms under congruence with weight det^2. In the positive coefficient
convention its weight is (2^5). It is nonzero: at f=sum_(i=0)^4 x_i^2, F=32.
The multiplicity of det^2 in degree five is exactly one. To see uniqueness,
any two det^2-relative invariants have invariant ratio on nonsingular symmetric
matrices, and this is one GL_5 orbit over C. The ratio is constant there,
hence the polynomials are proportional on the dense ambient open subset.
A highest-weight module of weight (2^5) is the one-dimensional det^2 module,
so this argument is also uniqueness in the highest-weight multiplicity space.
Thus a=1; the 17-dimensional weight space of Claim 09.3 is not a.

On c!=0, normalize by c and shift x_0 by -g/(2c). The resulting quadric is
x_0^2+y^T Q y with

    Q=G/c-gg^T/(4c^2), M=2Q,
    det S = c det(G-gg^T/(4c)),
    F=2 c^5 det M.

The last equation is an identity in the localization at c. In particular
c^5 clears all chart denominators of the determinant expression; clearing
entry denominators separately would give an unnecessarily high power.
Claim 09.3 makes det M vanish for every traceless determinant pencil.
Claim 09.1, homogeneity, and unipotent invariance imply F vanishes on the
full determinant closure. Therefore i_det>=1. Since a=1,

    i_det=1, m_det=0.

Alternatively, a 2x2 determinant is a nondegenerate quadratic form in its
four matrix entries, so every five-variable pencil has coefficient rank<=4.
Its fifth discriminant vanishes point-free. Full-rank four-dimensional
restrictions are dense, identifying the same orbit closure. This control
is intentionally outside the four-essential-variable determinant space;
it certifies the instrument, not a new quartic or padded obstruction.

**Verifier:** symbolic trace identity; complete interpolation; the explicit
finite pencil with det B_0=3, S rank 4 and traceless Gram rank 3; and the
nonzero ambient value in the final certificate. The finite pencil verifies
rational normalization with nonzero trace, including its denominators.

## Claim 09.5: exact cost and the scope of the quartic stop

**Status: EXACT counts; RESOURCE_STOP for the dense representation.** The
frozen proposal is n=4, delta=8, N=7, lambda=(13,11,3,2,1,1,1).
Its a=2 and h_pad=2 are RECORDED inherited values. Applying the current
typed ledger under `quartic_padded_gap` and checking matching entries in the
accepted transport/removal overlays yields no exclusion. This is scoped to
the frozen record; no other worker's output is used.

Without normalization, 112 matrix-entry parameters give the complete
multidegree containing space

    product_i binomial(lambda_i+15,15)
      = 131496322579119577497600.

On the justified highest-weight chart there are six 15-entry blocks, with
degrees (11,3,2,1,1,1). Their complete block dimensions are

    4457400, 680, 120, 15, 15, 15,

and their product is 1227567960000000. One dense eight-byte row already
requires 9820543680000000 bytes (about 9.82 PB). Even assuming one microsecond
per evaluation, visiting the complete grid takes 1227567960 seconds, about
38.9 years. This is an illustrative rate assumption, not benchmarked speed.
The local six-node factorization of the control does not reduce the number
of required source values for this dense method.

The preregistered 1536 MiB gate rejects this representation before allocation.
No inference is made that the actual image has that dimension, or that sparse
coefficient extraction and trace-identity methods cannot work. Construction,
source reduction and geometric evaluation of the quartic sources were not
attempted. The recorded source carrier size 519879 is not a newly verified
signed Burnside count and was not divided by a stabilizer.

With the inherited a and h_pad and the trivial L_pad=0, U_pad=2. For this
cell an exact determinant ideal floor 1 and a padded rank floor 2 would
suffice for positive D. A determinant rank floor 2 would exclude it. Neither
floor has been obtained here. A smaller globally certified containing space
or direct symbolic relations for two explicit independent rational sources
is needed before this instrument can decide the quartic cell. The true
padded locus is the orbit closure of z*per3 in ten independent variables;
length seven is a restriction for highest-weight evaluation, not a change
of the definition of padding.

## Proposed input correction, not a change to the shared record

S57's subtraction `15*(ell-1)-15` does not, by itself, prove the dimension
of the image of the characteristic-polynomial map. It requires separate
generic-fiber hypotheses and is false without a range qualification. For
ell=2 there is one traceless 4x4 matrix: the three coefficients e2,e3,e4
are freely prescribed by a traceless companion matrix, so the image has
dimension three, whereas that formula gives zero. For ell=3 the coefficient
ambient space has dimension 3+4+5=12, already below the formula's 15.
Our density proof and polynomial-space counts use neither dimension claim.
This correction does not contradict the chart construction itself.
