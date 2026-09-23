# One local merge sees B^2, but is not a determinant equation

UNCOMMITTED / PRODUCER ONLY. Registered outcome 3: REJECTION.
All statements and calculations below are **hand derivation**, unless explicitly
labelled READ. No mathematical program, numerical evaluation or external theorem
is a premise. This is a finite exact certificate, not a claim of literature novelty.

## 1. Object, normalization and admissibility

READ: B26-02 at cdf6839cd81031d42e43dc640b08e2746a7ef22c, sections 1.1 and 3,
confirms the tensor normalization and the old K5,5 construction at the scope used
here. We independently define and justify the changed contraction.

Work over C, with n=4 and five variables. There are 50 distinct labels
a_ij,b_ij for 0<=i,j<=4. The following is a list of **single representatives** of
column pairs; put every listed column into the tableau twice, in the same order:

* (a_i0,a_i1,a_i2,a_i3,a_i4), for i=0,...,4;
* (b_0j,b_1j,b_2j,b_3j,b_4j), for j=0,...,4;
* (a_ij,b_ij), for all (i,j) except (0,0),(0,2);
* (a_00,b_00,a_02,b_02).

Sort columns by height, retaining the displayed within-column orders. This is
one local operation on the old base: merge the two selected height-two column
pairs into a height-four column pair. There is no change of seed or second
candidate. There are 20 height-five, 2 height-four and 46 height-two columns.
Each label occurs four times; no column repeats a label. Thus d=50, content
50 x 4, shape lambda=(68,68,22,22,20), size 200 and tail 132. It is a legal
five-row filling. Semistandardness is neither required nor asserted.

For a quartic q use the symmetric tensor with

    q(x)=sum_(i,j,k,l=1)^5 q_ijkl x_i x_j x_k x_l.

In particular, a coefficient c of x1^2 x2^2 gives q_1122=c/6. Put one copy of
this tensor at each label and contract its four legs with the alternating
tensors of its four column occurrences. An alternating tensor of height h is
the determinant on coordinates 1,...,h, with epsilon_(1,...,h)=1. No extra
factorials divide the columns or the label symmetrization. This defines f(q),
a homogeneous coefficient polynomial of degree 50, without reference to BDI.

More explicitly, for q=sum_r w_r L_r^4, with L_r(x)=v_r dot x, multilinearity gives

    f(q)=sum_(phi: labels -> summands) (product_a w_phi(a))
                product_(paired-column representatives c) Delta_c(v_phi)^2. (1)

This follows directly from (L_r^4)_ijkl=v_ri v_rj v_rk v_rl, so it is independent
of which pure-power presentation is used. The formula fixes the normalization
also for unequal weights; no choice of fourth roots of w_r is necessary.

For a lower-unitriangular change on evaluation vectors each top h-coordinate
minor is unchanged. A diagonal change scales a height-h column by t1...th,
so the exponent of t_i is lambda_i. Hence f, once shown nonzero, is a
highest-weight function in the convention used in B26-02 (the action on forms
has the corresponding opposite triangular convention). This is a direct proof,
not an invocation of the unreviewed BDI statements.

## 2. Exact visibility certificate

Put V=span(x3,x4,x5), B=x3^2+x4^2+x5^2, and

    L_c=x1+c x2+c^2 x3+c^3 x4+c^4 x5,   c=0,...,4;
    q0=sum_(c=0)^4 L_c^4.

The following positive pure-power identity is obtained by expanding each pair:

    B^2=(1/3)(x3^4+x4^4+x5^4)
        +(1/6) sum_(3<=i<j<=5) ((xi+xj)^4+(xi-xj)^4).           (2)

Call the nine summands' vectors h_r and their weights eta_r (three weights
1/3 and six weights 1/6). For a subset S of the 50 labels define the **exact
rational number**

    C(S)=sum_(psi:S->{1,...,9}, chi:S^c->{0,...,4})
            (product_(a in S) eta_psi(a)) product_c Delta_c(v)^2,

where v_a=h_psi(a) on S and v_a is the coefficient vector of L_chi(a) otherwise;
the product is over the 34 representatives in section 1. Define

    C_r=sum_(S: |S|=r) C(S).

These finite sums specify exact coefficients, not sampled estimates. All
summands are nonnegative. Formula (1) gives f(q0+s B^2)=sum_r C_r s^r.
If S contains any label outside E={a00,b00,a02,b02}, a height-two determinant
has a zero vector in its top two coordinates. That term is zero. If |S|>=3
inside E, the height-four column has at least three vectors in the two-dimensional
space span(e3,e4) after projection to its first four coordinates, and is zero.
Consequently the **exact dependence** is

    f(q0+s B^2)=C_0+C_1 s+C_2 s^2.                            (3)

We now certify each coefficient positive by one explicitly specified summand.
Start with the color assignment

    a_ij -> L_((i+j) mod 5),   b_ij -> L_((i+j+1) mod 5).

Each of the ten height-five representatives uses all five colors, giving
absolute determinant 288, the Vandermonde product. The merged height-four
representative has colors (0,1,2,3), with determinant 12. Of the remaining
height-two representatives, precisely five wrap from color 4 to 0; they give
squared determinant 16, and the others give 1. Thus

    C_0 >= 288^20 * 12^2 * 16^5 > 0.                         (4)

For C_1 replace only the vector at a00 by e3, from (2), with weight 1/3.
The a_0j star now consists of e3,L1,L2,L3,L4. Its determinant has absolute
value 420: the four-node Vandermonde is 12 and the x^2 coefficient of
(x-1)(x-2)(x-3)(x-4) is 35. The merged column is e3,L1,L2,L3; its determinant
has absolute value 12 (the x^2 coefficient of (x-1)(x-2)(x-3) has absolute
value 6, and its three-node Vandermonde is 2). Other factors are unchanged:

    C_1 >= (1/3) * 420^2 * 288^18 * 12^2 * 16^5 > 0.         (5)

For C_2 replace a00 by e3 and a02 by e4, each with weight 1/3. The a_0j star
contains e3,e4 and L1,L3,L4. Its remaining rows have exponents 0,1,4, and
the three-by-three determinant has absolute value

    (3-1)(4^4-1)-(4-1)(3^4-1)=2*255-3*80=270.

The merged column e3,L1,e4,L3 has absolute determinant 3-1=2. Therefore

    C_2 >= (1/9) * 270^2 * 288^18 * 2^2 * 16^5 > 0.          (6)

Equations (2)--(6) prove exact quadratic, nonconstant dependence on the formerly
invisible direction B^2 at the stated q0. They also prove f is nonzero, completing
the highest-weight certificate. q0 is only an ambient visibility point; no
actual-padding membership for q0 is claimed.

## 3. Exact determinant rejection

Set Q=x1^2+x2^2+x3^2+x4^2+x5^2. We prove an elementary positivity statement
for paired quartic contractions and apply it to the single candidate above.

Let G={-2,-1,0,1,2}, with positive weights

    rho(0)=1/2, rho(1)=rho(-1)=1/6, rho(2)=rho(-2)=1/12.

Their zeroth, first, second, third and fourth moments are respectively
1,0,1,0,3: the second moment is 1/3+2/3=1, and the fourth is 1/3+8/3=3.
For v in G^5 put w(v)=product_i rho(v_i). Expanding by these four moments gives
the exact finite identity

    Q^2=(1/3) sum_(v in G^5) w(v) (v dot x)^4.                (7)

For independently named vectors X_a, one per label, let

    P(X)=product_c Delta_c(X)^2.

This is a nonzero integer polynomial: every column has distinct labels, so
each determinant is a nonzero polynomial in independent coordinate variables,
and a product of such polynomials is nonzero. Alternatively (4) exhibits a
point with P>0. Each scalar coordinate of each X_a has degree at most four,
because label a occurs in exactly four column occurrences.

A nonzero polynomial of degree at most four in each scalar variable cannot
vanish on the Cartesian grid of five distinct values in every variable. Proof:
induct on the variable count, using that a univariate polynomial of degree at
most four with five roots is zero, coefficient by coefficient. Apply this to
P and G^250. Some grid assignment has P nonzero; on that integer assignment,
P is a positive integer, hence at least 1. All other grid assignments have P>=0.

Combining (1) and (7) gives the exact finite evaluation certificate

    f(Q^2)=3^(-50) sum_(v_a in G^5 for all 50 labels)
                          (product_a w(v_a)) P(v)
          >= 3^(-50) * 12^(-250) > 0.                      (8)

The sum is symbolic and has not been enumerated. Its strict rational lower
bound follows from the grid lemma and positivity, not a program or a random
evaluation. This proves the structural no-go: in form degree four, an entirely
paired-column contraction of this kind with no repeated label in a column is
positive on Q^2. No extension to unpaired columns, signed sums or n>4 is claimed.

Finally define z=x1+i*x2, w=x1-i*x2, u=x3+i*x4, v=x3-i*x4, t=x5 and

    K_Q = [ 0   z   u   t
           -z   0   t  -v
           -u  -t   0   w
           -t   v  -w   0 ].

The skew determinant identity gives

    det K_Q=(zw-u*(-v)+t*t)^2=(zw+uv+t^2)^2=Q^2.

READ: the same elementary identity is audited in B26-02, item 5; here its
linear forms are explicitly changed and the substitution checked by hand.
The x1 coefficient matrix is diag(J,J), J=[[0,1],[-1,0]], with determinant 1.
Left multiplication by its inverse gives a normalized pencil without changing
its determinant. Thus Q^2 is in the literal determinant image, even in the
normalized chart. Equation (8) proves f is not a determinant equation.

## 4. Stopping consequence

Outcome 3 is decided by an exact structural nonvanishing certificate at a
literal determinant. The one-defined-redesign stop rule applies. We do not
try another graph, form degree, seed, column pattern or linear combination.
The redesign's value at actual padding is **UNRESOLVED in this packet**; the
old padding certificate cannot be transferred through a column merge. An
actual-padding test cannot repair the failed determinant-identity requirement.

The old common pair (p4,D4) is not used as a pair of separation witnesses.
Equation (3) breaks the global blindness identity, but does not assert
f(p4)!=f(D4). The new rejection point is Q^2=(A+B)^2, whereas the old one was
(A+B/2)^2. Visibility is established; padding survival and separation are not.

No five-row determinant equation is known to be nonzero on padding.
