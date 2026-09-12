# Complete interpolation: theorem and certificate contract

**PROVED / CERTIFIED.** This document specifies the mathematical contract and
its implemented exact profile `ternary_quartic_888_d6`. The kind is
`complete_interpolation` in `gct-cert/1`. Both
`tools/verify/complete_interpolation.py` and the normal
`tools/verify/verify.py` command check it. Larger profiles are **NOT VERIFIED**
(nonzero exit, UNPARSEABLE with an unsupported-profile reason). A free-text
dimension assertion or a stored value matrix cannot enable acceptance.

## 1. Lemma CI with all hypotheses

**PROVED.** Let M have a verified Q-basis F_1,...,F_a, let S:M -> Q[Y] be a
specified linear polynomial map, and let N be a finite-dimensional subspace of
Q[Y] with S(M) subset N. Suppose:

1. dim_Q N=h is established independently of sampled source rank;
2. G_1,...,G_h are verified members of N;
3. at specified rational parameter points P_1,...,P_m, T_ij=G_i(P_j) has a
   verified nonzero h-by-h minor;
4. A_ij=(S F_i)(P_j) is established over Q with exact source arithmetic.

Then evaluation ev_P:N -> Q^m is injective. The minor makes the h members
independent, hence a basis; an element with zero evaluations has zero basis
coordinates by that same minor. Thus ker(ev_P S)=ker S and
dim ker S=a-rank_Q A. It suffices initially to prove dim N<=h: the h-member
nonzero minor supplies the reverse inequality. This is the implemented
dimension sandwich, without circularity.

**PROVED.** In the source-row convention A is a-by-m. Relations are columns of
an a-by-k matrix K with **A^T K=0**. Exact rank K=k and rank A=a-k make its
columns a basis of ker S. A K=0 instead concerns relations between point
columns. If sources only span a subspace, CI computes its restriction kernel;
identifying an ideal multiplicity requires completeness in the intended M.
All identities persist under extension from Q to C.

**PROVED / OPEN boundary.** Without the target dimension, membership, minor or
inclusion, evaluation proves only rank S>=rank A: observed nullity is a ceiling
on dim ker S. Missing an input never weakens the verdict to PASS.

## 2. Spaces, pullback, and the integral model

**PROVED.** For f=sum c_alpha x^alpha (quartic), l=sum l_i x_i, and
c=sum d_beta x^beta (cubic), all ordinary coefficients, multiplication gives

    mu*: c_alpha -> sum_(i:alpha_i>0) l_i d_(alpha-e_i).

There is **no alpha_i multiplier**. This GL-equivariant substitution takes
coefficient degree delta to bidegree (delta,delta). On highest-weight vectors
of weight lambda it lands in

    N = HW_lambda(Sym^delta V tensor Sym^delta(Sym^3 V)).

The positive coefficient-weight convention is
E_ij c_alpha=(alpha_i+1)c_(alpha+e_i-e_j), zero if alpha_j=0, and
E_ij l_j=l_i, extended by Leibniz. Equivariance also follows by applying these
derivations on both sides of the displayed substitution. Thus S=mu* restricted
to M has the required inclusion. Membership in the ideal of the closure of
the linear-times-cubic image is equivalent to zero universal pullback. No
normalization theorem or finiteness of the parameter map is assumed.

**PROVED.** Mixed bracket specifications use labelled auxiliary vectors z_j.
For each ordered column of height q take its determinant in initial coordinates
1,...,q. Expand the product. A linear letter occurs once and is mapped to l_i;
a cubic letter occurs three times and is mapped by

    z_j^alpha -> alpha! d_alpha,  alpha! = product_i alpha_i!.

All linear letters use the same l, and all cubic letters the same c. There is
no averaging over letters and no division by 3!, 6!, or an orbit size. The
linear umbral map is equivariant, because

    alpha_j (alpha+e_i-e_j)! = (alpha_i+1) alpha!.

It intertwines the auxiliary derivation with the ordinary coefficient
derivation. Initial determinants are highest-weight vectors; their product
has the column-shape weight and prescribed bidegree. Its image is a member,
possibly zero. The implemented profile uses eight height-three columns and
also reconstructs the full polynomial, checks every term's weight/bidegree,
and checks every simple raising residual exactly. A zero member must still
fail the nonzero-minor gate.

**PROVED.** For rational source rows, d_i is the coefficient-denominator lcm,
Z_i=d_i F_i, and A_Z=diag(d_i)A_Q. Let C be the maximum of 1 and the absolute
ordinary quartic coordinates reconstructed at the supplied points. Then

    H_i = (sum_m |coefficient_m(Z_i)|) C^delta

bounds every row-i integer entry. The verifier reconstructs this bound. CRT
primes must be distinct, prime, and invertible on every d_i. Product
M>2 max H_i gives a unique lift in the bounded interval. The checker compares
residues with separately reduced evaluations, reconstructs signed integers,
compares all entries with direct integer evaluation, and checks rational rank
and kernel. A wrong entry differing by an entire modulus is rejected too.
Direct evaluation makes CRT redundant on this small control; CRT sufficiency
nevertheless remains a required protocol condition.

**PROVED.** rank(A_Z mod p)<=rank_Q A_Z=rank_Q A_Q. Denominator invertibility
is checked before that comparison in the common model. An invertible rational
source change B is applied before clearing denominators. K refers to the
changed rational basis, not the row-cleared basis. Kernel identities here are
only over Q, so no modular interpretation of K is claimed.

**CONDITIONAL future interface.** A profile using u^(d-native_degree) must
specify each native row, exponent, u's formula, points and exact u(P_j), and
check u(P_j)!=0 at every column before comparing transported/divided values.
Each matrix carries its transform in `values_are`. The present control has no
transport and no u. Unimplemented transport assertions are rejected.

## 3. Target dimension and source completeness

**PROVED / CERTIFIED.** For delta=6, r=3, lambda=(8,8,8), the ordinary
characteristic-zero Pieri rule gives

    dim N = sum_(lambda/nu horizontal 6-strip) mult_nu Sym^6(Sym^3 V).

All multiplicities are retained. Interlacing forces nu_1=nu_2=8, and |nu|=18
then forces nu_3=2. The checker re-enumerates these inequalities. For the
unique predecessor (8,8,2), it enumerates all degree-6 ordinary cubic monomials
of that weight and constructs all simple raising equations: 38 columns,
54 rows, ranks 37 at both house primes. Hence dim N<=1 over Q. The verified
nonzero target bracket minor supplies dim N>=1, so dim N=1. This also proves
the cubic raising rank is 37 over Q. No census implementation is imported.

**CERTIFIED.** The source enumeration similarly has 561 quartic weight
monomials and 1,056 raising rows, with ranks 559 at both primes. Both supplied
rational source polynomials have zero raising residuals and are independent
over Q. Therefore the complete source dimension is 2 and the rational raising
rank is 559. Each modular rank floor is combined with exact kernel members;
modular deficiency is never promoted on its own.

## 4. Strict wire contract

**RECORDED.** `results/b14_03/control.json` is the fully populated canonical
example. All its fields are required. Unknown object keys, duplicate JSON
keys, floating scalars and booleans as integers are rejected. Rational scalars
are integers or signed decimal numerator/positive-denominator strings.

| object | required content |
|---|---|
| top | format, kind, profile, nonempty title and produced_by, field=Q, cell, conventions, points, source, target, source_arithmetic, kernel, claim |
| cell | n=4, r=3, delta=6, lambda=[8,8,8] |
| conventions | exact example strings for coefficient, raising, bracket, orientation |
| points | 1..16 reducible parameter records; l and all ten cubic coefficients, including zeros |
| source | complete exponent list, two rational polynomials, invertible 2-by-2 change_of_basis, provenance_sha256, dimension_proof |
| source.dimension_proof | complete_raising method, weight_dimension, raising_rank, dimension; all recomputed |
| target.dimension_proof | pieri_complete_cubic_raising method, predecessors, weight_dimensions, raising_ranks, dimension; all recomputed |
| target.members | exactly one; letter_types and ordered columns, with every valence checked |
| target.evaluation | values_are and entries; all compared against reconstructed brackets |
| target.minor | rows, columns, determinant; full h-by-h minor, recomputed nonzero |
| source_arithmetic | values_are, exact row_denominators, entries, derived height_bounds, crt |
| crt | distinct house primes, modulus product, canonical residue matrix at each prime |
| kernel | values_are, a-by-k entries, rank; exact independence and A^T K=0 |
| claim | source_dimension, target_dimension, rank_Q, i_red; all recomputed |

`provenance_sha256` records a historical input byte identity; it is not a proof
of membership/authorship. The delivered source is checked mathematically
regardless of this informational hash. Portable frozen Git blob identities
and byte hashes are recorded separately in the input manifest.

**CERTIFIED example.** For sources (F0+F1,F1) and the supplied cubic at
l=(1,0,0), (1,2,0), the matrices are

    A = [[729,3969],[729,3969]], K = [[1],[-1]],
    T = [[209952,1143072]], det(T[:,{0}])=209952.

Both source rows are nonzero. Exact rank is 1 and i_red=1. An extra independent
coefficient check, outside CI's acceptance path, proves G=288 mu*(F1) on all
1,720 terms and mu*(F0)=0. For rational rows ((F0+F1)/2,F1/3), A_Z stays the
same, d=(2,3), A_Q=diag(1/2,1/3)A_Z and K=(2,-3)^T.

## 5. Validation and limits

**CERTIFIED.** `analysis/b14_03_controls.py` runs 97 cases: two valid
certificates and 95 rejected mutations, including all 71 required-key
deletions. It also rejects a duplicate JSON key. Named rejections cover wrong
points, source scaling, target membership, a valid zero bracket with preserved
valences, insufficient CRT and one changed integer entry. The actual right
kernel vector (49,-9) fails as a source relation. The dispatcher also rejects
an absent file and returns a nonzero process exit status.

**RECORDED.** The verifier imports no analysis code. Its full bracket
polynomial expansion differs from the producer's pointwise contraction. It
rebuilds source/cubic raising matrices in ascending exponent order, remapping
input coordinates by tuples. Primality uses trial division. Modular elimination
reduces before int64 conversion and checks the signed-int64 multiplication
bound. Characteristic-zero arithmetic uses Python integers/Fraction; NumPy is
the sole nonstandard CI dependency. Legacy dependencies/semantics are retained,
with flint/scipy imports now lazy.

**NOT REACHED / OPEN.** No degree-13/14 profile, those target bases, their source
arithmetic, or new LMR ideal dimension is supplied. Larger profiles need
checked dimension certificates and scalable bracket evaluators preserving all
gates. An unsupported profile cannot fall back to generic-matrix PASS. The
historical `certificate_ceiling` and s79 records are unchanged.
