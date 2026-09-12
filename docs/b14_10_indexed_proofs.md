# B14-10: recovered proof rules and their exact scope

board_numbering: batch14. Author/model: gpt-6-astra. Sources are frozen at
9898e56941a7665f231873481dae956f08509995. This file supplies the proof and
application contract for the appendices to PROVED and inherited_exclusions.

## First-row transport and stable-dimension closure — PROVED

These are Lemma L and the filtration part of Proposition S in
docs/s57_report.md, now indexed by name. Work in characteristic zero with
W=Sym^4(V*) and a GL(V)-stable irreducible closed cone X not contained in
{c=0}, where c(f)=[s_1^4]f. Let lambda+=(lambda_1+4,lambda_2,...).
Multiplication by c is injective in C[W], in its ideal I(X), and in C[X]:
the first is a domain, the second is its subspace, and the third is a domain
in which c is nonzero. The product of c and a HWV is again a HWV. Consequently

    a+ >= a, mult_X+ >= mult_X,
    i_X <= i_X+ <= i_X + a+ - a.

In particular equal adjacent ambient multiplicities preserve both ideal and
coordinate-ring multiplicities. This has no conclusion when the hypotheses
or the equal ambient dimensions are unverified.

For a tail rho, dehomogenize at c=1, then remove the s_1^3 coefficient by
s_1 -> s_1-g_1/4. This is a global slice for the first-row root subgroups;
the remaining tensors have tail degrees 2,3,4. Thus the weight-rho HWVs are
filtered subspaces of the fixed space

    Sym(Sym^2 V' + Sym^3 V' + Sym^4 V')_rho^hw.

Their dimensions are at most a_inf(rho), and the filtration is exhausted
by coefficient degree delta>=|rho|: a monomial of tail weight |rho| has
at most |rho| positive-tail-degree factors before homogenization. The same
argument applies to the ideal of X on the slice. This is the stable-range
statement; **no dimension formula for the trace-pencil quotient is used**.

If at a valid rung delta0 an exact witness gives mult_X=a=a_inf and the
stable ambient dimension is justified, every later rung has the same a and
i_X=0. Every earlier valid rung also has i_X=0 by injectivity on the ideal.
This is `stable_dimension_full_rank_closure`. It is an implication with two
indispensable inputs (stable dimension and exact full-rank witness), not an
automatic closure for every stable record or a sampled deficient kernel.

## Peaked quartic ladders — PROVED

Recover Theorem P of docs/s57_report.md with its length restriction explicit:
2<=ell<=16, delta>=ell, and lambda=(4delta-2(ell-1),2^(ell-1)). Then

    a(lambda,delta)=mult_det(lambda,delta)=1, i_det=0, D<=0.

Write k=ell-1 and f=c*s_1^4+s_1^3*g_1+s_1^2*g_2+..., with G_2 the symmetric
coefficient matrix of the quadric g_2 (off-diagonal entries are half the
plain coefficients). On c=1 the centered quadratic tensor is
Q=G_2-(3/8)g_1*g_1^T. Its determinant has tail weight (2^k). Homogenizing
and using the rank-one determinant formula gives the polynomial HWV

    H=c*det(G_2)-(3/8)g_1^T adj(G_2) g_1,
    c^(delta-ell) H in coefficient degree delta.

The slice is equivariant, its first-row translations have been removed,
and det(Q) is a GL(V') semi-invariant, so this is a HWV. The stable
multiplicity for tail (2^k) is one: the contraction description uses two
alternating k-tensors; a symmetric tensor cannot put two indices in the
same alternating tensor. Tensors of degree 3 or 4 therefore contribute
zero, leaving only the determinant of the quadratic tensor. Equivalently
the degree-k component of Sym(Sym^2 V') contains det^2 once. This is the
same invariant-theory argument as the banked proof. The stable bound and
the displayed nonzero HWV give a=1 for every delta>=ell.

At f=det(s_1 I_4+A(s')), with A traceless, c=1 and g_1=0. The centered
quadratic tensor is -tr(A(s')^2)/2. The trace pairing on sl_4 is nondegenerate
and has rank 15. An explicit integral basis is E_ij+E_ji and E_ij-E_ji
for each i<j, followed by E_11-E_22, E_22-E_33, E_33-E_44. Its Gram matrix
is a diagonal block of six (2,-2) pairs followed by the type-A3 matrix
with diagonal 2 and adjacent entries -1. Every leading principal minor is
nonzero. Hence restricting to its first k members gives H(f)!=0 for
each 1<=k<=15. Integer determinants and both prime residues are stored in
results/b14_10/trace_form_validation.json. This proves mult_det=1; since
mult_pad<=a=1, D<=0. It does not assert that the padded ideal is empty.

All normalizations have denominators powers of two, invertible at both
house primes. The actual polynomial and trace pairing are rational/integral
objects before reduction. The boundary ell=17 is outside this proof.
The displayed expression in the old report `dim M_ell=15ell-30` is not
adopted here: it requires a generic stabilizer calculation and already
fails for one traceless matrix (ell=2), whose conjugation quotient has
three characteristic coefficients. This defect does not affect the slice,
transport, stable filtration, or the trace-pairing proof above.

## Four compact exact certificate replacements — CERTIFIED

At n=3, delta=ell=8 the following four cells have a=1 by the proved
`top_cells_catalecticant` theorem:

    (7,5,5,2,2,1,1,1), (7,6,3,3,2,1,1,1),
    (8,5,3,2,2,2,1,1), (9,4,2,2,2,2,2,1).

For each strict partition nu of 8 in the certificate, take its shifted
diagram S(nu)={(i,j):i<=j<i+nu_i}. The matrix entry in row (i,j), column k
is alpha!*[s^alpha]per_3(sum s_t A_t), alpha=e_i+e_j+e_k. Its determinant
is the integral HWV; its weight is (1^8)+sum_(i,j in S)(e_i+e_j).
`analysis/b14_10/recover.py` independently expands all 8! determinant
summands, checks every weight and all seven raising derivatives exactly
with the plain-coefficient rule, rebuilds the permanent coefficients from
the six permanent permutations, and checks the nonzero determinant by
Bareiss and by the separate Leibniz formula. It agrees with the recorded
integer value and both residues in results/b13_05_topcells.json.

Thus each has mult_per3=a=1 and i_per3=0 over Q. These replace the
mathematical role of eight missing B13-09 prime files with four replayable
integral witnesses. They neither restore those original bytes nor add a
new frontier closure: all four belong to the existing degree-eight theorem.
Every certificate includes the pencil, diagram, integral matrix, values_are,
orientation, scaling, exact determinant, both residues and a reproducible
hash of the expanded HWV. No modular-to-rational lift is assumed.

## Machine use

`tools/integrate/exclusion_predicates.py` returns typed conclusions for a
declared mathematical context. The cubic-per3 census join requests only
`cubic_per3_ideal`. Containment results, stability identities, and the n=3
padded-per2 comparison cannot silently become cubic-per3 empty-ideal claims.
Unrecognized predicates and malformed cell keys fail explicitly. Structural
proof rules remain implications; only the listed unconditional exclusions
are automatically applied. The module's boundary tests include deliberately
wrong contexts, shapes, degrees, lengths and missing premises.
