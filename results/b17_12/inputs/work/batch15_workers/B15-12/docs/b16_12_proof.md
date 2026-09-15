# B16-12: adversarial proof review

This is an independent mathematical review by slot 12, starting from the frozen B16 brief and the B15 intake. It makes no new character-count production, geometric rank census, Git-binding, or positive-gap claim. Arithmetic inputs retain the Dream source author's attribution; the B14 bracket conventions retain Claude Opus 5 attribution. New arguments, explicit formulas, and tiny receiver controls below are slot 12's work.

## 1. The ring-map direction is correct

Work over C. Use the repository's positive partition convention consistently: the coordinate functions of degree one transform as V, dim V=16, and forms belong to Sym^4(V*). Put Y=Sub_9(Sym^3(V*)) and Z=closure{l C : l in V*, C in Y}. An arbitrary linear substitution in the ten independent variables of z per3 produces l times a cubic in at most nine linear forms. Therefore X_pad is contained in Z. This does not put X_pad in Sub_9(Sym^4(V*)); the product can use ten variables.

The polynomial map mu: V* x Y -> Sym^4(V*) has dense image in Z by definition. A regular function on Z whose pullback is zero vanishes on a dense set, hence is zero. Consequently C[Z] injects into C[V* x Y]. A quartic coefficient pulls back to a bilinear polynomial in l and the cubic coefficients. A homogeneous degree-d coordinate function thus pulls back in bidegree (d,d), not in total source degree d:

    C[Z]_d -> Sym^d(V) tensor C[Y]_d   (injective).
    C[Z]_d -> C[X_pad]_d              (surjective).

Characteristic-zero complete reducibility turns these arrows into multiplicity inequalities in the indicated directions. No normality of Z, finite parameterization, isomorphism with a normalization, or extension of orbit functions is needed. Degenerate factors and dependent forms cause no problem: Z is the image closure.

Subspace inheritance in degree d says C[Y]_d retains the Schur components of Sym^d(Sym^3 V) of length at most nine, with the same multiplicity spaces. This also follows directly by restricting the polynomial functor to C^9 and taking all translates: precisely the Schur factors of length greater than nine vanish. The cited literature checks agree: Kadish–Landsberg, Theorem 1.7 gives the product map; Proposition 1.12 gives inheritance. Their general padded variety and this particular subspace-restricted cubic source must still be distinguished. [Primary version: arXiv:1204.4693v1](https://arxiv.org/pdf/1204.4693v1).

Pieri therefore gives

    m_pad(d,lambda) <= sum a_cubic(d,mu),

over |mu|=3d, length(mu)<=9, and lambda/mu a horizontal d-strip. This is a source ceiling. It is not a dimension of the multiplication image or of the permanent restriction image.

## 2. The horizontal strips and degree conventions

For lambda=(4d-t-16,t,2^8), pad mu with mu_10=0. Horizontal-strip interlacing means lambda_i>=mu_i>=lambda_(i+1). Hence mu_3 through mu_9 are all 2 and 2<=mu_2=b<=t. The cubic degree fixes mu_1=3d-14-b. Thus

    mu_b=(3d-14-b,b,2^7),  b=2,...,t.

There is no additional channel. The remaining first-row inequalities hold at (d,t)=(23,15),(25,17),(26,17),(27,19),(35,19); the receiver checks each listed strip and its size. The exhaustion is the preceding proof, not an assumption that these lists were complete. The weights have ten parts on the quartic side and nine on the cubic side. There are t-1 channels: 14,16,16,18,18 respectively.

## 3. Dense cubic chart: an actual injection, not an inverse lifting theorem

Write a nine-variable cubic as

    C(s,y)=c s^3 + L(y)s^2 + Q(y)s + R(y),  dim(y)=8.

On c!=0 the shear s -> s-L/(3c) and scalar normalization give

    C(s-L/(3c),y)/c = s^3 + q2(y)s + q3(y),
    q2=Q/c-L^2/(3c^2),
    q3=R/c-L Q/(3c^2)+2 L^3/(27c^3).

Fix the Borel for the positive coefficient convention so the highest-weight functions are invariant under the induced shears s -> s+h(y). Let P be one such polynomial of coefficient degree d and highest weight mu=(3d-|beta|,beta). The defining identity is

    P(C)=c^d P(s^3+q2 s+q3).

Indeed the shear fixes P, and scalar multiplication of the entire cubic changes P by its coefficient degree d. This uses all shears h, not a sampled subset. Restriction P -> P(s^3+q2 s+q3) is polynomial, because it is obtained by setting coefficient variables c=1,L=0 in a polynomial. If this restriction is zero, the identity makes P zero on every C with c!=0, an open dense subset of the full cubic affine space. Thus P=0. The possible poles in expressing q2,q3 in unnormalized coefficients do not obstruct this direction.

The residual GL8 acts only on y and commutes with setting c=1,L=0. Its torus weight and upper-unipotent invariance restrict to beta. Therefore the restriction is an injection of highest-weight multiplicity spaces into the beta highest-weight space of

    Sym(Sym^2 C^8 + Sym^3 C^8).

This supplies a finite-degree upper bound. Conversely, a chart polynomial need not clear denominators at the selected d; injectivity does not imply surjectivity. Ordinary chart monomials obey 2u+3v=|beta|, and those coming from a degree-d P also satisfy u+v<=d. Dropping this latter restriction only enlarges the upper bound. Here |beta|<=33 and d>=23, so it imposes no extra restriction by itself.

The tiny exact receiver proves shear invariance of 3cQ-L^2 and 27c^2R-9cLQ+2L^3 in a binary restriction. These are sign/normalization controls. The proof for arbitrary forms L,Q,R is the algebraic expansion above; the binary control alone does not prove the nine-variable injection. A cubic-sign mutation is rejected.

## 4. What the number 288 does and does not certify

The retained complete power-sum/character files give h(b,2^7), b=2,...,19:

    1,1,2,3,5,6,9,11,14,16,19,21,24,26,29,31,34,36.

The source producer forms exp(sum_(j=2,3; r>=1; rho a partition of j) p_(r rho) u^(jr)/(r z_rho)). Differentiating in u produces the implemented coefficient j/z_rho in the recurrence for n F_n; the missing-looking factor r is canceled by jr. The character scalar product with p_rho contributes chi_beta(rho), with no second z_rho factor. The source code and its independent connected-border-strip checker were read. Neither is executed here. The integrator's prior fresh character and recurrence replays remain the correctness/completeness evidence.

The receiver freshly sums every saved rational coefficient times saved character, verifies row shapes, term lengths, and partial sums, and hashes the files. This arithmetic audit does not independently regenerate their character values or certify their power-sum support completeness.

The sums through b=15,17,19 are 158,218,288. Sections 1–3 therefore support the accepted padding ceilings, and also 218 at d26 with t17. With inherited a=429, m_det=418 and genuine padding floor 243 in the d35 cell:

    243<=m_pad<=288;
    -175<=D=m_pad-418<=-130;
    141<=i_pad=429-m_pad<=186;
    i_det=11.

No exact padding rank 243 or 288, explicit 141-equation basis, or smaller finite ambient multiplicity is inferred. Using the upper bound as a floor would reverse the relevant map. A larger split-cubic evaluation outside the retained padding span would concern the enlargement Z, not raise the genuine padding floor.

## 5. Independent review of the Hessian signs and shared padding relation

For any cubic C(x) in nine variables, g=grad C and H=Hess C obey Hx=2g and x^T Hx=6C. Thus

    Hess(z C) = [[0,g^T],[g,zH]],
    det Hess(z C) = -z^8 g^T adj(H)g
                 = -(3/2) z^8 C det H.

The middle equality is a bordered determinant. The last follows from
4 g^T adj(H)g = x^T H adj(H) H x = det(H) x^T Hx.
This is a polynomial identity, including singular H; no division by det H is made. Independent z is essential. The exponent z^8 follows from the nine-by-nine lower block and its adjugate. The receiver checks the same identity exactly in a three-variable toy C=x^3+x y^2+y^3 and rejects the opposite sign.

For every invertible map of the ten essential variables, Hessian congruence multiplies its determinant by det(L)^2. Consequently F divides its ten-variable Hessian determinant on the full split-cubic family. Polynomial remainder identities extend to singular substitutions by density. This handles a ten-dimensional restriction of the sixteen-variable orbit as well; invertible maps of the essential variables are dense in the parameter matrix space. A fixed-leading-matrix sample does not establish this identity; the argument does.

On the monic depressed line p=t^4+s2 t^2+s3 t+s4, write D_H=det Hess F. Since p divides D_H, its remainder S modulo p^2 has the form p T with deg T<=3. Writing T=t0+t1 t+t2 t^2+t3 t^3 yields

    S7=t3, S6=t2, S5=t1+s2 t3,
    S3=s2 t1+s3 t2+s4 t3,
    S3-s2 S5-s3 S6-(s4-s2^2)S7=0.

This derives the requested shared padding identity globally. Its constant relation on the five weight-35 expressions has coefficients (1,-1,-1,-1,+1). After a common valid polynomial lift it still holds. The five displayed restrictions consequently have rank at most four, but the full padding cell can have much larger rank. Independent source vectors alone would not certify their restriction rank. An exact symbolic receiver control and a wrong-sign rejection accompany the proof.

For determinant pencils, rank Hess(det4)<=8 on det4=0 follows at rank-three matrices from the quadratic normal form a tr(E)-r c, and extends by closure. A ten-by-ten pullback has corank at least two at a simple root. Constant row/column changes at that root show its determinant has order at least two there, giving p^2 | D_H on the squarefree chart. Monic division is polynomial; density of squarefree pencils extends the identity to all pencils. This is valid ordinary-Hessian geometry, not a new higher-jet compatibility theorem.

The formula for genuine slice jets is H_tt=12t^2+2s2, H_tx=4t u2+3u3, H_xx=2t^2 N2+6t N3+12N4, where N_d e=u_d and e^T u_d=s_d. The bordered source convention includes (-1)^k c2!c3!c4!; an abbreviated old docstring omits the sign, but the inspected mathematical report and executable source include it. A coefficient or basis comparison must use that convention.

## 6. Finite lifts, independence, and closure gates for 03–08

For the ten-variable Hessian det of an unnormalized quartic G, coefficient degree is 10 and line degree is at most 20. Normalize by c, so Hessian determinant gains c^-10. For q=G(t,e)/c, each coefficient of q^2 dropping the t-degree by i has denominator dividing c^i. Induction in monic reduction gives the coefficient of t^j in t^k mod q^2 denominator at most c^(k-j) when k>=j. The bound is harmless when k<8 because the only nonzero term has j=k. Therefore the remainder coefficient has denominator at most c^(30-j). Translating t by -a1(e)/(4c) after division, and using the determinant-one full shear for Hessian congruence, preserves that bound: moving l to j introduces at most c^-(l-j).

Thus c^(30-j) S_j is polynomial of coefficient degree 30-j; this is a sufficient degree, not a valuation equality or a complete filtration. At j=7 the degree is 23. Weighted line scaling gives wt(S_j)=(22-j,2^8), so the finite full weight is (4(30-j)-(38-j),22-j,2^8). For j7 it is (61,15,2^8). This checks the signs/degrees in the inherited recipe, without claiming a fresh Hessian nonzero or highest-weight basis replay for slot03.

The eleven-space dimensions 8+5-2=11 use an actual nonzero ambient evaluation minor and exact source relations in the inherited Hessian11 report. Euler quotient rank alone would be only an upper bound on the image rank. Matching finite filtration upper bounds require all cancellation constraints and a proof that they exhaust the relevant finite subspace. A special one-parameter pole test can disprove a lift but cannot by itself certify that all poles cancel. Products of a nonzero ambient polynomial preserve independence inside the ambient polynomial ring; images after restriction require their own argument. Degree-23 nonmembership in the ideal generated in degree24 follows by grading, but multiplication may put its later products in that ideal. None of this establishes nonmembership in a radical, discriminant saturation, or every LMR construction.

For nine-row slots, distinguish an ideal floor from a coordinate floor. If i_pad>=3 at d15, i_det<=3 is sufficient for D<=0. The higher-degree exclusion requires the retained four-equation reducible premise, a nonzero degree-two q44 of weight (4,4), and the compatible determinant ideal upper bound four. Its accepted onset16 is inherited, not rederived from d28 finite sufficient lifts.

For higher-jet slot08, blocks a,r,c,E must be shared across orders. A local specialization or a tiny three-direction instrument is not a universal sixteen-variable quartic-coefficient identity. Require elimination/substitution proof for arbitrary determinant-pencil entries, polynomial clearing of normalization/basepoint conditions, ambient nonzeroness, weight/degree, and actual images modulo the specified comparison ideal.

## 7. A finite positive certificate must pass all premises

In one finite degree and highest weight, let a be the exact ambient multiplicity, q a proved floor for i_det, and r a proved floor for m_pad from actual independent z per3 substitutions. Then D>=q+r-a, so q+r>a is sufficient. An equation with one padding nonzero gives one separating equation, not automatically the full multiplicity inequality. A source ceiling cannot replace r. A stable ambient cannot replace finite a. If q+r<=a, this sufficient certificate fails; it does not exclude a positive gap.

A genuine exclusion instead follows, for example, from i_det<=u and m_pad<=v with a-u>=v. For the inherited stable cell this gives 429-11>=288. For the still-unknown finite cells, one must receive finite a and its evidence before making a numerical decision. The receiver's arithmetic gate includes synthetic mutation examples for missing finite a, mixed cells, non-global determinant evidence, and replacing a padding floor with a source ceiling. It explicitly does not machine-prove the geometric premises.

No B16 results from 03–08 are accepted by this initial proof review. Each delivered version must have its exact report/source/resource paths and hashes recorded in results/b16_12/received.json, followed by a scoped supplement. Independent work is complete without waiting for those deliveries.
