# Exact rank-29 differential and global no-go

UNCOMMITTED / NOT RELEASED. **PROVED, producer-only, independent hand derivation.** There is no numerical or symbolic-program rank computation. All numbers and blocks below follow from the displayed determinant expansion. Bases and frame scope are in FRAMES.md.

## Theorem

Let phi:(Mat4)^5 -> W send B to det(sum_i x_i B_i). For the explicit pair in FRAMES.md, pi_(2,g) composed with phi is dominant onto its actual 29-dimensional joint-data space J. Equivalently

    ker(phi*:Q[W] -> Q[(Mat4)^5]) intersect R_(2,g) = {0}.

This holds in every polynomial degree. By the proved frame transport it holds for every fixed pair of distinct-center frames over C (and rationally for rational frames). In the redundant 30-coordinate presentation, the entire kernel is the universal duplicate-coordinate ideal, with no determinant-specific additional relation.

## 1. An explicit affine 29-parameter family

Write E_ij for the 4-by-4 matrix unit. Put lambda=(1,2,3,4) and

    U1=E12+E13,    U2=E14+E23,    U3=E24+E34.

The base pencil is

    B1=I4, B2=diag(1,2,3,4), B_(a+2)=Ua  (a=1,2,3).

Use six ordered edge pairs grouped as follows. An edge ij means i<j.

| a | e_(a,1) | e_(a,2) | complementary lambda products w_(a,1), w_(a,2) |
|---|---|---|---|
| 1 | 12 | 13 | 12, 8 |
| 2 | 14 | 23 | 6, 4 |
| 3 | 24 | 34 | 3, 2 |

For edge e=ij let E_rev(e)=E_ji. Define an affine map iota:A^29 -> (Mat4)^5 by

    B1=(I4+s E11),
    B2=diag(1+tau1,2+tau2,3+tau3,4+tau4),
    B_(a+2)=Ua + diag(d_(a,1),...,d_(a,4))
                   + sum_(c=1..a) sum_(h=1..2) r_(ca,h) E_rev(e_(c,h)).

The independent domain coordinates, in order, are s; tau1..tau4; d_(a,i) ordered by a then i; and r_(ab,1),r_(ab,2) in the same lexicographic a<=b order used for Q. There are 1+4+12+12=29 coordinates. Only the second matrix index of r_(ca,h) specifies the pencil matrix in which the entry is varied. No source gauge quotient or parameter-count inference is used.

Let f=pi_(2,g) phi iota, with the duplicate coordinate removed. At the origin all pencil matrices are upper triangular, with diagonal linear forms L_i=x1+lambda_i x2. Consequently

    phi(iota(0))=L1 L2 L3 L4.

## 2. The binary block has rank five

Let P_i=product_(j!=i) L_j. Differentiating a diagonal entry at the base gives

    partial_s F=x1 P1,
    partial_(tau_i) F=x2 P_i.

These derivatives have no z terms. In the b_k order, the s column begins with 1 and every tau column begins with 0. Below that first row, the tau columns form the coefficient matrix of the cubic P_i in the order x1^3,x1^2 x2,x1 x2^2,x2^3:

    M = [[ 1, 1, 1, 1],
         [ 9, 8, 7, 6],
         [26,19,14,11],
         [24,12, 8, 6]].

The P_i are independent: evaluation at (x1,x2)=(-lambda_j,1) kills all P_i except P_j, whose value is product_(k!=j)(lambda_k-lambda_j), nonzero. Thus M is invertible without relying on a parameter count.

For an exact scalar check, replacing the first three columns by consecutive differences and keeping the fourth gives first row (0,0,0,1). The complementary 3-by-3 matrix is [[1,1,1],[7,5,3],[12,4,2]], of determinant -12; the cofactor sign is minus. Hence det M=12. The binary 5-by-5 block has determinant 12.

## 3. The twelve first-transverse coordinates

At the base, varying d_(a,i) preserves triangularity, giving exactly

    partial_(d_(a,i)) F = z_a P_i.

Thus the twelve ell coordinates against the twelve d variables form diag(M,M,M). These columns do not affect binary coordinates or quadratic-transverse coordinates at first order. The s and tau columns do not affect ell or Q either. The determinant of this block is 12^3.

## 4. The twelve second-transverse coordinates

The part of a determinant with exactly two transverse factors is, by the permutation expansion,

    sum_(i<j) (Z_ii Z_jj - Z_ij Z_ji) product_(k notin {i,j}) L_k,

where Z=sum_a z_a C_a, and the other two matrix factors are diagonal. This is the complete degree-two-in-z part for a diagonal binary pencil: the contributing permutations are the identity with two transverse diagonal entries and the single transposition (ij). Longer cycles have at least three transverse factors.

At the base C_a=U_a all diagonal and lower entries are zero. For an edge in group a its upper entry is exactly z_a. Varying r_(ab,h), with a<=b, changes the reverse entry by z_b. Therefore

    partial_(r_(ab,h)) F
        = -z_a z_b product_(k notin e_(a,h)) L_k
          + terms of transverse degree at least three.

The last terms cannot contribute to any retained coordinate. This formula applies equally to a=b and a<b: ordinary coefficients of z_a^2 and z_a z_b both carry coefficient -1 here. There is no extraneous factor of two.

It follows that the Q_(ab,1),Q_(ab,2) rows against r_(ab,1),r_(ab,2) give exactly

    N_a = [[-1,        -1       ],
           [-w_(a,1), -w_(a,2)]].

Different (a,b) do not mix, because their z monomials are different. Hence this block is

    diag(N1,N1,N1,N2,N2,N3),

with det N1=-4, det N2=-2, det N3=-1. Its determinant is (-4)^3 (-2)^2 (-1)=256. Lower-entry variations have no binary or first-transverse contribution: a determinant term containing one such lower entry needs at least one upper transverse entry to close its permutation cycle.

## 5. The complete certificate

With exactly the row and column orders stated above, the Jacobian at zero is block diagonal:

    J_f(0)=diag(A,M,M,M,N1,N1,N1,N2,N2,N3),

where A is the binary 5-by-5 block, det A=12. Therefore

    det J_f(0)=12^4 * 256 = 5,308,416 != 0.

This is an exact rational/integer certificate in characteristic zero, not a modular rank floor and not a sampled absence of relations. The 29 displayed columns are actual independent source-entry variations. The full 29-by-80 projection differential consequently also has rank 29. The proof does not assume smoothness of the determinant image or that this special triangular pencil is generic.

## 6. Why this proves the global polynomial claim

Here is an elementary algebraic proof of the needed differential implication, so no inverse-function or geometric smoothness theorem is an unverified premise.

Suppose a nonzero H in C[J] satisfied H(f(t))=0 identically. Translate the target by f(0), and let H_m be the lowest nonzero homogeneous part of H(f(0)+Y). Since f(t)=f(0)+J_f(0)t+terms of degree at least two, the lowest possible part of H(f(t)) is H_m(J_f(0)t). It is nonzero because J_f(0) is invertible. This contradicts the supposed identity. Thus f has no polynomial relation, which is exactly Zariski density in J. The same argument works over Q and remains valid after scalar extension to C.

Any polynomial relation on ALL determinant pencils would in particular vanish on this affine family. The contradiction therefore proves the theorem on the global determinant image, and then on its closure. Conversely no special-slice equation has been asserted: the slice is used only to prove algebraic independence. Failure of a chosen slice would not have implied nondominance; here a positive full-rank certificate was obtained.

## 7. Consequence and limit

For every fixed distinct-center pair, all polynomial relations among the two 15-coordinate jet arrays are universal linear-overlap relations and their ideal consequences. After quotienting those, there are none. This excludes determinant coefficient equations in the entire joint subring, in all degrees. It does not claim the full determinant locus equals W, nor that every joint datum is attained, nor that adjoining a third frame or a higher layer is harmless. No such extension was investigated.
