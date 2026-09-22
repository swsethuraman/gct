# The decisive five-center comparison

UNCOMMITTED / NOT RELEASED. PROVED hand reductions, producer-only. The final containment statement is OPEN. Optional C_PER and C_DUBE premises are separately identified; neither is needed for the elementary reductions.

## 1. Literal completion and closure are different questions

Put q_i=product_{j!=i}x_j. A literal completion of retained data of F has the exact form

    F + sum_{i=1}^5 b_i q_i.

No other quartic coefficient is free. The correct global identity of closed sets is

    pi_5^{-1}(Y_5)=closure(D+K_5)=closure(im phi+K_5).

To prove it, split W=J_5 direct-sum K_5 linearly. Then D+K_5 corresponds to pi_5(D) times K_5; taking closure gives Y_5 times K_5. Density of im phi in D gives the second equality. Thus actual-padding separation asks whether some actual F_T is outside this **closed saturation**, not merely whether its five-parameter family lacks a literal determinant.

**PROVED: every element of K_5 is itself an actual determinant.** If b5!=0, take

    Q(x)=b5 det(diag(x1,x2,x3,x4)+x5 u 1^T),  u_i=bi/b5 (i<=4).

Multilinearity in columns makes all terms with two rank-one columns zero. The remaining terms give exactly sum bi q_i. The scalar b5 can be absorbed into the first matrix row, so this is a 4-by-4 linear determinant. If b5=0 but another coefficient is nonzero, permute variables; zero is also a determinant. This proves actual membership, not just a limit assertion.

Consequently the projective center P(K_5) lies in P(D). Projection cannot be treated as a base-point-free proper morphism from P(D). This fact alone does not prove that pi_5(D) is nonclosed, but it invalidates an automatic properness argument. B23-03's determinant-part classification also cannot rule out either determinant boundary points or new projection-boundary points. Its classification is not used as a theorem here.

## 2. Solve seventeen coordinates before the remaining comparison

Write t=x1, u=x2, z=(x3,x4,x5). On the open set where a=c_(4e1)!=0 and the binary quartic has distinct roots, pass to the ordered-root cover:

    F(t,u,0)=a product_{i=1}^4 L_i,  L_i=t+lambda_i u,
    P_i=product_{j!=i} L_j,  lambda_i distinct.

Let ell_s(t,u) be the binary cubic multiplying z_s in F, for s=1,2,3. All five binary coefficients and all twelve coefficients of the ell_s are retained already at two centers. Instead of their five binary coordinates use a and the four ordered lambda_i. The base field is

    k=Q(a,lambda1,...,lambda4, ell_(s,j) : 1<=s<=3, 0<=j<=3),

with seventeen independent transcendental parameters. Define

    d_(s,i)=ell_s(-lambda_i,1)/(a P_i(-lambda_i,1)).

**PROVED.** In the normalized pencil

    M=t I4+u diag(lambda)+sum_s z_s C_s,

the diagonal entries of C_s must be d_(s,i). Indeed the z_s coefficient of a det M is a sum_i (C_s)_ii P_i. Evaluating at (-lambda_i,1) isolates its i-th term, and the four P_i are a basis of binary cubics. This identity is independent of all off-diagonal entries.

Set (C_1)_12=(C_1)_13=(C_1)_14=1 as in STRUCTURAL_MAP.md. The remaining off-diagonal variables are nine in C_1 and twelve each in C_2,C_3, totaling **33**. Let eta denote those variables. For alpha in E_5 except the preceding seventeen monomials define

    f_alpha(eta)=[x^alpha] a det M.

This is a completely specified map f:A_k^33 -> A_k^48, of degree at most four in eta. Its image closure Z is the generic fiber, over the seventeen base parameters and ordered roots, of the determinant projection. This follows by localizing the kernel of the dense fifty-parameter normal form; localization of the kernel commutes with this polynomial map. This is a statement about the generic base, not arbitrary specialization of a closed image.

The same bookkeeping gives 25 remaining outputs for m=3 and 37 for m=4. It explains the change from a possible dominance problem (33 to 25) to forced relations (33 to 37 or 48). No rank equality is assumed for any of these maps.

## 3. The padding fiber is four explicitly specified affine planes

For each i=1,...,4, let

    l_i=L_i+sum_s d_(s,i) z_s,
    C_i^0=a P_i+sum_s z_s (ell_s-d_(s,i) a P_i)/L_i.

Each quotient is exactly a binary quadratic: its numerator vanishes at the root of L_i and is a homogeneous binary cubic. No rational function of t,u remains. The form C_i^0 is cubic.

Let U be the 22-dimensional cubic space of transverse degree at least two:

    U = span{t z_s z_r, u z_s z_r : s<=r}
        direct-sum span{z^beta:|beta|=3}.

There are twelve quadratic-transverse and ten cubic-transverse monomials. Define the affine-linear map

    g_i: U -> A_k^48,
    g_i(H)=the remaining retained coefficients of l_i(C_i^0+H).

**PROVED.** Every product l C over this generic base belongs to one of these four families. Its nonzero t-coefficient allows normalization of l to have t-coefficient one; its binary restriction must then be one of the four L_i. Evaluating each ell_s at that root forces the transverse coefficient of l to be d_(s,i). Dividing the residual ell_s fixes the binary-quadratic part of C, leaving exactly H in U. Conversely the displayed formulas reproduce the prescribed seventeen base coefficients for every H.

Generically l_i has all five coefficients nonzero, so PADDING_FIBERS.md shows g_i is injective. Thus its image A_i is an affine **22-plane** in A^48. The four choices are permuted by eigenvalue relabeling. Over an algebraic closure of k the generic product fiber is their union. No claim about a generic actual permanent fiber follows without C_PER; modulo C_PER their union is precisely the generic fiber of the actual-padding closure.

There is also a sharper completion-fiber consequence than the elementary 256 bound in PADDING_FIBERS.md. On the open set of retained data where the binary roots are distinct and all four derived l_i are nonzero at the selected centers, **there are at most four possible linear factors**, already determined by those seventeen coordinates. For each factor, the remaining equations in the cubic coefficients are linear. Hence every nonempty branch of the literal product-completion fiber is an affine space of dimension 4,1,0 for m=3,4,5 respectively, by the fixed-factor kernel formula. In particular the five-center projection has at most **four** literal product completions on this open set. This proves an exact generic fiber description, not just the dimension of its source. It still says nothing about determinant completions of other factorization types.

This reduction is a finite structural comparison of one mechanism:

    Does the closure of the specified 33-parameter degree-four map f
    contain the specified 22-plane A_1 (equivalently, by relabeling, all A_i)?

It is not a dimension argument: 22<33<48 is consistent with both answers. The new restriction is that padding occupies four explicit affine planes once the common seventeen coordinates are fixed, whereas determinant compatibility is carried by 33 off-diagonal parameters.

## 4. What exactly remains to be certified

Let y denote the 48 remaining coordinates. The ideal of Z is

    I_Z=(y_alpha-f_alpha(eta) : alpha) intersect k[y].

The ideal of A_1 is the kernel of y -> g_1(H). The single missing scientific lemma on this generic chart is

    I_Z subseteq I(A_1), or a rigorously certified failure of this inclusion.

The elimination **must precede** substitution of the padding plane. Testing only solvability of f(eta)=g_1(H), or computing the dimension of its affine solution set, can miss values attained only in the image closure. A proof of impossibility of factor-preserving completions, although established above, does not address those values or completions that change factorization.

A sparse h in I_Z with h(g_1(H)) nonzero would be an existential separation on this chart (modulo C_PER until actual padding is checked). It is not yet an explicit polynomial in the original 65 coefficient coordinates: ordered roots and denominators must be removed. A correct descent is available. Clear base denominators, form all 24 eigenvalue-permuted conjugates h_sigma, and take the coefficients other than the leading one of product_sigma(T+h_sigma). These are symmetric in the roots, hence rational in the binary coefficients and ell_s. After clearing denominators they are global coefficient polynomials vanishing on D by the dense-chart argument. If one conjugate is nonzero at a padding point, some such coefficient is nonzero there, since a monic polynomial with roots -h_sigma cannot equal T^24 unless every root is zero. Taking the product alone would be wrong: another conjugate can vanish. A final exact actual T evaluation still has to be supplied.

Conversely a proof of generic-plane containment, **together with C_PER**, implies global actual-padding projected containment: the generic part is dense in the irreducible product parametrization, and Y_5 is closed. For an unconditional certificate independent of C_PER, NEXT_CERTIFICATE.md gives a single finite comparison using the original actual-padding parametrization.

No I_Z generator, nonzero padding evaluation, or whole-plane containment proof has been obtained in this session. These are the exact unresolved parts; the reduced maps and the factor/kernel theorems are established, not conjectured.

## 5. Why extending the old triangular Jacobian is insufficient

For the old type of base pencil, all diagonals are binary L_i(t,u) and every strictly upper entry is a linear form in z=(x3,x4,x5). Restrict its first-order determinant variation to t=u=0. Diagonal cofactors and cofactors for short paths still contain a binary diagonal and vanish there. Only the path 1->2->3->4 survives, in the cofactor for the (4,1) entry. Therefore the space of pure-transverse quartic variations is contained in

    span{z1,z2,z3} * (u12(z) u23(z) u34(z)),

of dimension at most three. The three-center retained target requires six independent pure-transverse quartics with z1 exponent at least two. Hence **every** such binary-diagonal triangular base has projected differential rank at most 42-(6-3)=39 at m=3. The earlier particular pencil may have still smaller rank. This proves that simply enlarging the same triangular Jacobian certificate cannot settle even the three-center dominance question. It is an obstruction to that proof construction, not a theorem that Y_3 is nondominant. No pilot to rediscover this rank deficit was warranted.
