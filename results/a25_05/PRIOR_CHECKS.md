# Essential prior steps checked in this session

UNCOMMITTED / NOT RELEASED. Method: READ plus independent hand derivation of the following elementary steps. This is producer verification for A25-05, not downstream acceptance of A25-01..04. All their manifests and payloads were freshly byte-checked; no historical file was edited or replayed computationally.

## One center and the ten-minor algebra

For matrix units u=(E12,E13,E14,E23), v_i=u_i^T, direct multiplication gives tr(u_i u_j)=tr(v_i v_j)=0 and tr(u_i v_j)=delta_ij. Thus D_i=u_i+(1/2)sum G_ij v_j realizes any symmetric Gram matrix G. Expanding the determinant by permutations gives the degree-two term ((tr Y)^2-tr Y^2)/2. With tr C_i=r_i, the square coefficient is (r_i^2-tr C_i^2)/2 and a mixed coefficient is r_i r_j-tr(C_i C_j). Taking the scalar part r_i I/4 gives exactly the A25-01 section after multiplying by det B1=a. Localization at a is injective, so no boundary extension of the section is needed.

The same expansion gives the A25-04 bordered minors m_ij=-4 tr(W_i W_j) after clearing a, where W_i is the traceless part of adj(B1)B_(i+1). The polynomial identity extends from a!=0 by density. The four hyperbolic pairs realize an arbitrary symmetric m, so that single-center algebra supplies no relation. These facts explain the prior scope but are not used to infer any higher-center dominance.

## The two-center lower bound 29

Re-derive the needed differential directly. At B1=I, B2=diag(1,2,3,4), use upper entries in three groups:

    U1=E12+E13, U2=E14+E23, U3=E24+E34.

Let L_i=x1+i x2 and P_i=product_{j!=i}L_j. Varying a diagonal entry in B_(a+2) gives z_a P_i. The four P_i are independent because evaluation at (-i,1) isolates P_i. Varying B1(1,1) gives x1 P1; varying the four B2 diagonal entries gives x2 P_i. The first has leading x1^4 coefficient one and the others zero, giving a five-dimensional binary block. Together these supply five binary and twelve first-transverse coordinates.

For each a<=b, vary in B_(b+2) the two lower entries reverse to the two edges in group a. The retained quadratic-transverse terms are -z_a z_b product_{k not on edge}L_k. Against the coordinates x1^2 z_a z_b and x2^2 z_a z_b, their two columns form

    [-1 -1; -w1 -w2].

The complementary products are (12,8), (6,4), (3,2) for groups a=1,2,3. Their differences are nonzero. The six blocks occur with multiplicities 3,2,1. These columns have no binary or first-transverse terms: a single lower entry needs at least one upper entry to close a permutation cycle. Longer cycles have transverse degree at least three and are not retained at two centers. The diagonal-variation columns contribute only the earlier blocks. Thus the full 29-column differential is invertible without assuming generic rank from a parameter count. In the earlier stated orders its determinant is 12^4*(-4)^3*(-2)^2*(-1)=5,308,416; nonvanishing, rather than this scalar, is what is used here.

If a polynomial relation vanished on this affine source family, translate the target at its base point and take the lowest nonzero homogeneous part of the relation. Substitution of an invertible linear Jacobian preserves its nonzero lowest part, a contradiction. This proves two-center dominance and provides the dimension lower bound 29 for each higher-center projection by further projection. It does not provide a higher-center Jacobian. FIVE_CENTER_REDUCTION.md proves why the same binary-diagonal triangular family cannot simply be enlarged to a rank-42 certificate.

## Kernel/evaluation implication

For exact coefficient maps Q_D and Q_P on the same finite coefficient-polynomial space, a separator exists in that space exactly when ker Q_D is not contained in ker Q_P. Indeed v represents h, Q_D v=0 is the global identity, and Q_P v!=0 is a nonzero polynomial on the actual-padding parameters. Row-annihilator duality gives the equivalent strict inequality rank([Q_D;Q_P])>rank Q_D. A sampled rank floor without a global identity or rank ceiling cannot establish Q_D v=0. This independently supplies the elementary A25-02 bridge used in NEXT_CERTIFICATE.md.

## What remains conditional

No A25-01..04 theorem is a residual conditional premise of the new elementary proofs. The optional equality P=R is instead conditional here on the separately committed B13-07 permanent-dominance certificate C_PER, read but not recomputed. The optional finite universal degree cap is conditional on C_DUBE, a primary statement-level reading of an external degree-bound theorem. Neither condition decides padding containment; both are named wherever used.
