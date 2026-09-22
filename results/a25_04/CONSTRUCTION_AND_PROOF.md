# A25-04: bordered Jacobian minors and the trace pairing

**PROVED, producer-only. UNCOMMITTED / NOT RELEASED.** Characteristic zero, with all formulas over Q and then C. Method: self-contained hand derivation after reading the provisional A25-01/02 packets. No mathematical program was run. This is a scoped specialization of the two-jet idea, not a claim of an independently accepted new general exclusion.

## 1. Exact coefficient matrix and selected minors

Let V=C^5, S=C[x1,...,x5], W=Sym^4(V*), and A=C[c_alpha: |alpha|=4]. The 70 c_alpha are ordinary monomial coefficients, without factorial normalization. Set X=(Mat_4)^5 and

    phi(B1,...,B5)=det(x1 B1+...+x5 B5),
    D=closure(im phi),
    P=closure{(z per_3) composed with T : T:C^5 -> C^10 linear}.

Closures are affine Zariski closures. No identification of P with all products is needed.

Fix **N=5, j=1, k=3**. Use K_j(k)=wedge^j V tensor S_(k-3j), with differential

    d_j(e_(i1) wedge ... wedge e_(ij) tensor u)
      = sum_(t=1..j) (-1)^(t-1) e_(i1)...omit e_(it)...e_(ij) tensor u partial_(it)F.

The matrix **M(F)=d_1^(3): V tensor S_0 -> S_3** has 35 rows and 5 columns. Columns are e1,...,e5. Rows are ordinary degree-three monomials in descending lexicographic order x1>...>x5. Thus

    M_(beta,l)=(beta_l+1)c_(beta+e_l).

Every entry is linear in quartic coefficients. This specifies the orientation; some historical displays transpose this matrix, which does not affect rank but would affect index notation.

Write yi=x_(i+1), 1<=i<=4, and retain

    F = a x1^4 + x1^3 sum_i p_i yi
        + x1^2 (sum_i q_ii yi^2 + sum_(i<j) q_ij yi yj)
        + terms of transverse degree at least three.

Let beta0=3e1 and betai=2e1+e_(i+1). These are the first five rows. The corresponding five-by-five block is

    L = [ 4a    p^T ]
        [ 3p     Q  ],

where Q_ii=2q_ii and Q_ij=q_ij for i!=j. Multiplying its first row by 3 gives Hess_F(e1), so the block has an intrinsic interpretation as one framed second jet.

Select the **ten size-two minors** indexed by 1<=i<=j<=4:

    m_ij(F)=det M[rows (beta0,betai), columns (1,j+1)]
           =4a Q_ij-3p_i p_j.

Their order is (11,12,13,14,22,23,24,33,34,44). Row and column orders inside each determinant are as displayed; there is no additional sign. Define m_ji=m_ij. For i>j this also equals the analogous actual minor because Q is symmetric. Hence

    m_ii=8a q_ii-3p_i^2,
    m_ij=4a q_ij-3p_i p_j  (i<j).

The fixed candidate is the exact degree-eight coefficient polynomial

    h0(F)=det(m_ij(F))_(i,j=1..4)
         =sum_(pi in S4) sign(pi) product_(i=1..4) m_(i,pi(i))(F).

The selected structural mechanism also permits replacing this determinant by a polynomial R in the **same ten** minors, h_R=R(m_11,...,m_44). It does not permit new rows, arbitrary coefficient multipliers, or a second frame. We prove that no nonzero R supplies a determinant identity. This is a no-go for the entire specified minor algebra, beyond rejecting h0 alone.

## 2. Why the determinant suggested this mechanism

For a determinant pencil the Hessian/adjugate formula expresses the bordered minors through a trace pairing on traceless matrices. A rank constraint on that pairing would force relations among smaller minors without using a rank threshold of the full Jacobian matrix. The question is whether the determinant presentation actually imposes such a constraint. It does not for these four transverse directions.

Here is the complete translation, including its global polynomial meaning. On the open set a=det B1!=0 put

    C_i=B1^(-1) B_(i+1),   r_i=tr(C_i),
    D_i=C_i-(r_i/4)I4.

For Y=sum_i yi C_i the determinant expansion gives

    det(x1 I4+Y)=x1^4+x1^3 tr Y
                +(x1^2/2)((tr Y)^2-tr(Y^2))+higher transverse terms.

This degree-two expression follows by summing the terms
Y_aa Y_bb-Y_ab Y_ba over a<b. It is not an adopted Newton-identity theorem. Multiplying by a gives

    p_i=a r_i,
    Q_ij=a(r_i r_j-tr(C_i C_j))

for every i,j, including i=j because Q_ii=2q_ii. Substitution yields

    m_ij(phi(B))=-4a^2 tr(D_i D_j).                         (1)

To remove all inverses define the polynomial matrices

    Z_i=adj(B1) B_(i+1),
    W_i=Z_i-(tr Z_i/4)I4.

The adjugate is the transpose of the signed cofactor matrix: adj(B1)_(uv)=(-1)^(u+v) det B1[omit row v, omit column u]. Thus W_i is defined globally and tr W_i=0. On a!=0 it equals a D_i, and p_i=tr Z_i. Consequently (1) is the globally polynomial identity

    m_ij(phi(B))=-4 tr(W_i W_j)
                =(tr Z_i)(tr Z_j)-4tr(Z_i Z_j).           (2)

Both sides are degree eight polynomials in the 80 pencil entries. They agree on the nonempty open set det B1!=0 of affine X. A polynomial over C that vanishes on that dense open set is zero, so (2) holds for **all** pencils, including singular B1. No division by a is used to define an output or evaluate the boundary. This proves source-to-coefficient translation; it does not by itself prove any coefficient relation.

In particular,

    h0(phi(B))=256 det(tr(W_i W_j))_(i,j=1..4).             (3)

The four W_i lie in sl4, a space of dimension 15. A forced dependence of four Gram vectors does not follow from this fact. The next section gives the stronger obstruction: every symmetric Gram matrix occurs already with B1=I4.

## 3. Polynomial section and no-go theorem

**Theorem.** The polynomial map mu composed with phi:X -> Sym_4, where mu(F)=(m_ij(F)), has a polynomial section over Q. Thus

    C[t_ij:1<=i<=j<=4] -> A -> C[X],
    t_ij |-> m_ij |-> m_ij(phi(B))

is injective. Equivalently, h_R(phi(B))=0 for all B **if and only if R=0**. Therefore I(D) intersect C[m_11,...,m_44]={0}. In particular this subalgebra has no nonzero determinant equation in any coefficient degree.

**Proof, entirely explicit.** Put

    (u1,u2,u3,u4)=(E12,E13,E14,E23),   v_i=u_i^T.

The elementary identity E_ab E_cd=delta_bc E_ad gives

    tr(u_i)=tr(v_i)=0,
    tr(u_i u_j)=tr(v_i v_j)=0,
    tr(u_i v_j)=tr(v_j u_i)=delta_ij.                      (4)

For an arbitrary symmetric matrix t of ten independent variables set

    B1=I4,
    B_(i+1)=u_i-(1/8)sum_(j=1..4) t_ij v_j.              (5)

These are polynomial matrices in t with rational constants. They have trace zero, so a=1, p_i=0, and W_i=B_(i+1). Expanding the trace pairing with (4) gives

    tr(W_i W_j)=-t_ji/8-t_ij/8=-t_ij/4.

Equation (2) now gives m_ij(phi(B(t)))=t_ij for all ten indices. This proves the section identity. Pullback along (5) sends the composite ring map back to the identity of C[t], proving injectivity. Since h vanishes on D iff h composed with phi is the zero polynomial, the ideal-intersection statement follows. This last equivalence uses only that polynomial zero sets are closed. QED.

No lemma of A25-01 is assumed. Formula (4) is the same useful elementary construction appearing there; it is re-derived here and applied directly to these minor coordinates. This is not an independent acceptance of A25-01's whole packet. A25-02's pullback criterion is likewise not needed: the section gives an explicit left inverse instead of building any pullback matrix.

For the homogeneous degree-d space of polynomials in ten minors, the pullback rank is exactly binom(d+9,9), by injectivity. Those functions have coefficient degree 2d and pencil degree 8d. This symbolic dimension formula is not a materialized matrix, cell nomination, enumeration, or computation. It shows that the trace factorization cannot improve a coefficient-image ceiling on this space.

## 4. Three rejection tests and exact controls

### Universality

The familiar bordered-minor determinant formula here is

    h0(F)=(4a)^3 det L(F).                                (6)

Indeed for 4a!=0, the Schur complement gives
det L=(4a) det(Q-3pp^T/(4a)), while m=(4a)(Q-3pp^T/(4a)). Multiplying determinants proves (6) on a dense open set, hence polynomially everywhere. This identity holds for **every** matrix with these block sizes, independently of determinants of pencils. Thus h0-(4a)^3 det L is the zero coefficient polynomial and cannot be an obstruction. Equation (6) does not say h0=0.

The ten chosen m_ij themselves have no algebraic relation even on ambient quartics, because their determinant subfamily already maps onto Sym_4. Universal Pluecker/Laplace identities involving further minors give no exception to this conclusion inside C[m_ij].

### Wrong rank mechanism: exact determinant control

Take

    B1=I4,   B_(i+1)=u_i+(1/2)v_i,

with u,v as in (4). Then tr B_(i+1)=0 and tr(B_(i+1)B_(j+1))=delta_ij. Hence

    a=1, p=0, Q=-I4, m=-4I4,
    h0(phi(B))=256 !=0,   det L=4.

This is one exact rational determinant point, derived by hand. It refutes global determinant vanishing of h0. It also proves rank M=5 is attained on D. Since M has only five columns, max_D rank M=max_W rank M=5. The selected size 2 is genuinely smaller than that maximum; the full-matrix threshold size is 6 and gives only the zero ideal. No historical rank floor or depth-sensitivity theorem is needed at this grading.

### Padding blindness: explicit actual-padding control

Use the row order (z,y11,y12,y13,y21,y22,y23,y31,y32,y33) and columns (x1,...,x5). Define the exact 10-by-5 integer map T by

    T = [1 0 0 0  0
         1 0 0 0  1
         0 1 0 0  0
         0 0 1 0  0
         0 1 0 0  0
         1 0 0 0 -1
         0 0 0 1  0
         0 0 1 0  0
         0 0 0 1  0
         1 0 0 0  0].

Equivalently z=x1 and the permanent matrix is

    [x1+x5   x2     x3
       x2   x1-x5   x4
       x3     x4    x1].

The six permanent terms, with all signs positive, give exactly

    P_T=x1^4+x1^2(x2^2+x3^2+x4^2-x5^2)
                +x1*x5*(x4^2-x3^2)+2*x1*x2*x3*x4.

Thus a=1, p=0, Q=diag(2,2,2,-2), m=diag(8,8,8,-8), and

    h0(P_T)=-4096 !=0,   det L(P_T)=-64.

This is a **PROVED exact actual-padding nonvanishing** statement for h0. It is not separation: h0 already failed determinant membership. Rank M(P_T)=5, so max_P rank M=5 also. This establishes the actual scope of the rank comparison for the selected matrix without transplanting the M7 numbers.

At the shared pure-power point F=x1^4, all m_ij=0 and h0=0. Any determinant identity in the selected algebra must have R(0)=0; this necessary test is much weaker than the section theorem.

All three controls are hand calculations, not sampled evidence for a universal identity. The theorem in section 3 supplies the all-pencil/all-polynomial conclusion.

## 5. Exact scope and end of mechanism

Outcome (3): **scoped no-go for the determinant trace-pairing mechanism on these ten bordered 2-minors**. The exact proposed h0 is nonzero on ambient quartics and on actual padding, but is not a determinant equation. Every attempt to replace it by another R in the same minor algebra fails by section 3.

The result holds after any single fixed GL5 change of frame, because D is preserved by mixing the pencil matrices. It does not cover combinations from different frames, the other rows/minors of M, higher k or j, arbitrary coefficient-dependent multipliers, or every possible identity arising from the determinantal presentation. In particular it does not close row 3 in general. No rational cancellation/saturation route has been proposed or evaluated. No second mechanism is launched.

There is no unresolved scientific premise in this producer proof; independent review and committed-byte delivery remain pending. The exact missing certificate for a positive inside this class is impossible by the theorem, not merely uncomputed. Any wider positive would need a different specified family and authorization; none is selected here.
