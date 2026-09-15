# B15-10 proof fragment: four portable integral highest-weight sources

**Claim B15-10.1 — EXACT.** In coefficient degree 8 and weight
lambda=(12,4,4,4,4,4), four explicitly constructed integral polynomials restrict
independently to the det4 orbit closure. One restricts nontrivially to the true
z*per3 orbit closure. Consequently r_det>=4 and r_pad>=1. With the inherited
upper bounds a<=4 and h_pad<=1, m_det=4, m_pad=1, i_det=0, i_pad=3 and D=-3.

Verifier: `analysis/b15_10_full.py verify`, with its two named companion modules
and `results/b15_10/full_certificate.json`. The certificate contains all integer
points, source formulas, normalization, and minors. The source membership proof
below is an exact tensor identity, not an inference from the evaluation ranks.

## Setting and action

Let V have dimension 16. The degree-8 coordinate ring of Sym^4(V*) is
Sym^8(Sym^4 V). Use ordinary coefficient functions c_alpha and the convention

    E_(i,i+1)c_alpha = (alpha_i+1)c_(alpha+e_i-e_(i+1))

when alpha_(i+1)>0, and zero otherwise. Indices start at 0. All sources use
only the first six basis indices. Write

    T_ijkl = alpha! c_alpha,  alpha = e_i+e_j+e_k+e_l.

Thus T is 24 times the ordinary symmetric tensor of the quartic, not the plain
coefficient array. In particular T_0000=24 c_400000. This is an integral change
of normalization. The derivation replaces each occurrence of i+1 in T by i;
the factorial identity converts alpha_i+1 to the number of those occurrences.

For a symmetric four-tensor S on the first six indices, define the polynomial

    H(S) = sum_(sigma,tau,upsilon in S6)
           sgn(sigma)sgn(tau)sgn(upsilon)
           product_(i=0..5) S_(i,sigma(i),tau(i),upsilon(i)).

This has integer coefficients. The full contraction of six identical copies
of S against four alternating six-index epsilon tensors equals 6! H(S).
Indeed, relabel the six identical copies by the permutation in the first
epsilon. The other three permutation signs acquire its sign three times, and
the first epsilon supplies the fourth, so their product is unchanged. Each
fixed-first-permutation summand therefore occurs 6! times. There is no
denominator in the displayed definition of H, and no modular lifting premise.

The full epsilon contraction transforms by det(g)^4 under a simultaneous
change of all four index sets by g in GL6. The same is true of H over Q.
Equivalently, its simple raising derivatives vanish identically. Its diagonal
weight is (4,4,4,4,4,4). These statements also follow directly by replacing
an epsilon index: the resulting epsilon has repeated rows and is zero.

## Four sources

Put c=c_400000, v_i=T_i000 and M_ij=T_ij00. Define symmetric tensors

    V_ijkl = M_ij M_kl + M_ik M_jl + M_il M_jk,

    W_ijkl = M_ij v_k v_l + M_ik v_j v_l + M_il v_j v_k
             + M_jk v_i v_l + M_jl v_i v_k + M_kl v_i v_j.

The letter V in this formula denotes a tensor, not the ambient vector space.
The four coefficient polynomials, in certificate column order, are

    F0 = c^2 H(T),
    F1 = c [z] H(T+z V),
    F2 = [z^2] H(T+z V),
    F3 = [z] H(T+z W).

Here [z^k] is formal coefficient extraction, computed exactly by a truncated
polynomial recurrence, with no interpolation assumption. H is degree 6 in its
argument, T is degree 1 in coefficients, V degree 2 and W degree 3. Thus the
four coefficient degrees are 2+6, 1+5+2, 4+2*2 and 5+3, all equal to 8.

All pinned index slots are 0. A simple raising derivation never changes a
pinned slot, so v, M, V and W obey exactly the tensor replacement rule on
their remaining free indices. Every formal coefficient of the epsilon
contractions is therefore annihilated by each E_(i,i+1). The factor c is also
annihilated by these operators. Roots with i>=5 act as zero because no source
index is 6 or larger. This proves highest-weight membership in GL16 globally.

Each V replaces one four-slot tensor by two tensors with four additional
pinned-zero slots. Each W has eight additional pinned-zero slots. The factors
c contribute four zero slots each. All four sources therefore have weight
(4,4,4,4,4,4)+(8,0,0,0,0,0)=(12,4,4,4,4,4), extended by zeros to length 16.
This proves the common degree and weight without expanding 373,248,000 terms.

## Points and exact nonvanishing

Every determinant point is the ordinary quartic

    f(x)=det(sum_(i=0..5) x_i A_i),

with all six integer 4-by-4 matrices A_i retained. Every such substitution is
in the det4 orbit closure on 16 variables: arbitrary linear substitutions
are limits of invertible substitutions. The first point is skew-symmetric,
with Pfaffian x0^2+x1^2+x2^2-x3^2-x4^2-x5^2. Its F0 value is 5,284,823,040.
This alone supplies the rank-one exclusion with inherited h_pad<=1.

The four-point, four-source evaluation matrix has exact determinant

    525876952903928530201627329192414396439263877926189997328382842540874792960.

The two check residues are 1261539314 modulo 2147483647 and 635991447 modulo
2147483629. Bareiss elimination and a separate 24-term Leibniz determinant
agree over Z. No conclusion depends on integer reconstruction from residues.

The padded point is an explicit six-by-ten integer frame substituted into
z*per3(a11,...,a33), with a separately specified z column and nine matrix-entry
columns. The source polynomial has ten essential variables before restriction;
there is no nine-variable padding assumption. Its source-value row is

    (0, 0, -493414004913340416, 0).

These values are regenerated from the six permanent permutations, the linear
padding form, the quartic tensor, and the four defining polynomials. Thus the
nonzero third entry proves a padded rank floor of 1. These are orbit-closure
points, and no claim that the six-variable restrictions lie in the open GL16
orbits is needed.

## Exact computation and evidence boundaries

Fixing the first permutation leaves three subsets of used indices. After k
letters, at most binomial(6,k)^3 states occur. Summing gives 15,184 states;
the largest layer has 8,000. The exact transition upper bound is 486,432.
Appending an unused index j contributes sign (-1)^(number of previously used
indices greater than j). Multiplying the three signs and the current tensor
entry gives the recurrence for H. Replacing each entry by T+zV or T+zW and
retaining degrees <=2 or <=1 gives the other sources. Intermediate state
coefficients are integers; there is no floating-point or modular reduction.

The source construction and rank floors are fresh. The bounds a<=4 and
h_pad<=1 are inherited from the exact accepted Q1 recount in
`results/b15_prep/Q1_combined_bound.json`; the receiver records this dependency
explicitly and does not purport to rederive it. Four independent ambient
sources also give a>=4 freshly. Since m_X=a-i_X and m_pad<=min(a,h_pad)=1,
the bounds and witnesses force the asserted multiplicities and D=-3.

The separate small banked B14-10 cubic witness was replayed first with its
original verifier and original attribution. Its dimension-one ambient bound
remains inherited. The old B14-12 four determinant directions, old per4 result,
and native 753,614,285-byte operator were not replayed. The new sources provide
the determinant and padded ranks independently and require no comparison of
the old and new multiplicity bases. No new frontier exclusion is claimed.

Checks include independent direct permutations at dimension 3, exact series
coefficients, separate nonzero liveness on a sum of six fourth powers, five
raising shears and three diagonal weight scalings on a generic pencil, and
zero/four-factor family controls. The shear checks are finite implementation
checks; the global highest-weight proof is the epsilon argument above.
Altered source, factorial normalization, point, matrix, minor, padded minor,
degree, and missing native point are rejected. The receiver regenerates values
in a new process from only the portable modules and explicit certificate.

Dependencies: the elementary epsilon transformation identity, ordinary
determinant/permanent definitions, the coordinate-ring highest-weight/rank
interpretation, and the two explicitly inherited Q1 upper bounds. Actual model
for this new proof and code: gpt-6-astra, requested reasoning xhigh.
