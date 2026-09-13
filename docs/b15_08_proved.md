# B15-08 proof fragment: a third alternating column

Author/model: GPT-6 Astra, xhigh as dispatched. The two-column bordered determinant is an input from B14-06, attributed there to Claude Opus 5. This fragment gives the extension and a direct derivation of its coefficient extraction. It does not update any shared theorem record.

## Claim B15-08-A: explicit highest-weight polynomials

Status: EXACT (algebraic proof and finite exact controls). Let V have dimension h>=2, with ordered basis e_0,...,e_(h-1), and let Z=Sym^2 V^* + Sym^3 V^* + Sym^4 V^*. Let k>=0 and tau=(k+3,3,2^(h-2)). Its conjugate is (h,h,2,1^k).

An explicit source is a list of symmetric letters (d_j,S_j), d_j in {2,3,4}, S_j a subset of {A,B,C}, with |S_j|<=d_j. The sums of column occupancies are h,h,2, and sum d_j=2h+2+k. Its value B is the contraction of the letters with two copies of e_0 wedge ... wedge e_(h-1), one copy of e_0 wedge e_1, and k copies of e_0. Wedges are unnormalized alternating sums. Each column reads letter IDs in the supplied list order. Every unused slot of a letter receives e_0. This gives a polynomial with integer coefficients in the symmetric tensor entries T_d.

Under substitution T'_d(v_1,...,v_d)=T_d(gv_1,...,gv_d), an upper triangular g fixes the three wedge lines and the singleton line. The resulting scalar is det(g)^2 (g_00*g_11) g_00^k. Thus the weight is tau and the polynomial is fixed by the upper unitriangular group. This is the positive highest-weight convention for coordinate functions on Z with the contragredient point action. Every source belongs to the tau highest-weight space, even if it is zero. If two slots of one symmetric letter occupy the same alternating column, exchanging them shows that its contraction is zero in characteristic zero. Repeated identical vectors in a column vanish for the same reason.

Dependencies: elementary exterior algebra and symmetric tensors. The implemented enumeration contains explicit source polynomials; no general spanning theorem or formal source count is used as an ambient dimension. Swapping the two equal-height columns gives the same source up to column-order parity; canonicalizing that swap removes only redundant signed rows.

Verifier: `analysis/b15_08_run.py controls` checks small exact contractions, a repeated-vector zero, an invalid letter, upper unitriangular invariance and torus weight. `small_ranks` checks nine ambient counts against generic ranks at both primes, including zero-dimensional controls.

## Claim B15-08-B: the finite-difference bordered evaluator

Status: EXACT (identity over the integers). Expand the short column as the two permutations of (0,1), with their signs. Fix one assignment. Each letter now becomes a scalar, a vector on A or B only, or a symmetric matrix on A and B. A letter also incident to C uses the indicated fixed coordinate in its tensor: in particular, an ABC letter uses T_d(i,j,c,0,...,0). This requires third-order tensor data for d=3,4. A two-jet alone does not supply that data.

Let q be the number of paired A/B letters, and r=h-q the number of vectors in each tall column. Reorder each tall column into its single-column vectors followed by the common ordered list of paired letters. Let sigma be the product of the two reordering signs. Write U for the h by r matrix of A-vectors, and W^T for the r by h matrix of B-vectors, in those orders. For labelled pair matrices M_1,...,M_q, set

    D(x)=det [[sum_j x_j M_j, U],
              [W^T,             0]].

The contribution is its scalar-letter product times sigma*(-1)^r times the coefficient of x_1...x_q in D. To see this, expand on the last r rows and columns: the vector minors give the two complementary alternating tensors, while the remaining determinant expands over the two ordered complements. Its labelled coefficient assigns every paired letter exactly once. The block sign is (-1)^r. This also follows by adjoining the r vector columns and r vector rows to the two epsilon sums; the matching of the border indices contributes the same sign.

D has total degree q in x, since every nonzero determinant term uses r top-right entries, r bottom-left entries and q top-left entries. Therefore

    [x_1...x_q]D = sum_(S subset {1,...,q}) (-1)^(q-|S|) D(1_S).

Indeed a monomial missing any x_j is removed by that finite difference. A surviving monomial has all q variables and total degree q, so all exponents are one. Grouping c identical pair matrices replaces the subset choices by integer binomial weights. Equivalently the result is the ordinary grouped coefficient multiplied by the product of c! over groups. The implementation's finite differences already include these factors; no division by them is allowed. The proof works modulo any prime as a polynomial identity as well as over the integers.

Finally sum the two signed short-column assignments. Matrix order is h+r<=2h. The count used in sizing is 2*product_d(c_d+1)*2^s, where c_d counts ordinary AB letters and s<=2 counts ABC letters. Scalar zero or repeated vectors can reduce actual work. No large weight-space carrier is constructed.

Verifier: `value` in `analysis/b15_08_bracket.py` versus `brute` in the same file. The latter directly enumerates all h!^2*2 assignments and does not use determinants or finite differences. The controls bank 193 exact integer equalities, including 120 nonzero values. Reversing the short-column order negates live values. Removing a short-column sign and removing repeated-matrix factorials each changes at least one live control. The separate h=3 quadratic liveness control equals 3!*det(T_2) and is nonzero. No research determinant rank is required to be positive by a control.

## Claim B15-08-C: normalization, rational lifting and point scope

Status: EXACT (polynomial construction and controls). A symmetric tensor entry T_d(i_1,...,i_d) contributes ordinary monomial coefficient (d!/product alpha_i!)*T_d, with alpha the coordinate multiplicities. Thus the k-th derivative at e_0 equals d!/(d-k)! times the partially contracted tensor, including repeated derivative indices. All partial tensors come from the same polynomial. Scalar, gradient, Hessian and third derivatives cannot be sampled independently.

Generic points use explicitly stored integer symmetric tensor entries. Determinant points use integer traceless 4 by 4 matrices A_j and F(s_0,x)=det(s_0 I+sum x_j A_j). Padded points begin with the true independent polynomial z*per3 and an invertible integer 10 by 10 matrix L. For the h=8 instrument, retain the first nine columns of L and evaluate the resulting nine-variable restriction. This is an explicitly valid restriction of the ten-variable family; it is not a claim that nine variables parametrize all padded points. The controls also construct and evaluate the full ten-variable polynomial with h=9 and verify rank(L)=10 at both primes. Reducible controls use an independently chosen linear form and cubic.

For any of these quartics on the chart c=[s_0^4]F!=0, write F/c=s_0^4+g_1 s_0^3+g_2 s_0^2+g_3 s_0+g_4. Substitute s_0 -> s_0-g_1/4. The resulting coefficients are

    G2 = g2 - 3*g1^2/8,
    G3 = g3 - g1*g2/2 + g1^3/8,
    G4 = g4 - g1*g3/4 + g1^2*g2/16 - 3*g1^4/256.

The new module constructs the entire sparse polynomial, then extracts its symmetric tensors. It evaluates both the original native polynomial and the depressed identity at explicit test arguments. It also freshly regenerates B14-06's two-jets on the identical DET and PAD parameters and compares every scalar, gradient and Hessian entry. Inputs with c=0 are rejected and recorded; they do not become artificial points. Normalization and tensor conversion only introduce rational denominators generated by c, 2, 3 and tensor multinomial factors through degree four. The two primes exceed all fixed small denominators and c is checked nonzero. Stored modular values therefore have a specified rational lift from the native integer parameters. No modular nullspace is declared a rational source.

Verifier: `analysis/b15_08_run.py point_controls`, the derivative controls, and fresh polynomial replay. Dependencies: B14-06 two-jet code is a comparison implementation with retained attribution; new full polynomial evaluation is independent of its jet multiplication.

## Claim B15-08-D: how counted dimensions bound the output

Status: EXACT for the character formula; rank floors require their replay receipts. Let F_W be weighted degree W in Sym(Sym^2 V + Sym^3 V + Sym^4 V). Its Frobenius characteristic is the coefficient of z^W in

    product_(d=2,3,4) sum_(m>=0) h_m[h_d] z^(dm).

The logarithmic-derivative recurrence in B14-04 computes its rational power-sum coefficients. The multiplicity is sum_rho [p_rho]F_W * chi_tau(rho), with no additional z_rho factor. This is an exact upper and lower ambient dimension in characteristic zero. The Murnaghan-Nakayama character routine is a banked input; small character orthogonality and known Schur coefficients are rechecked. The full selected coefficient lists can be regenerated during replay.

For a matrix of explicit bracket rows and valid rational points, a nonzero minor modulo a good prime proves the corresponding rational rank floor. All source rows lie in the counted highest-weight space by Claim A. Thus generic rank equal to the exact ambient dimension certifies completeness for that cell without assuming that every enumerated signature is independent or that a general spanning theorem applies. A deficient sampled rank supplies only a coordinate-rank lower bound and an ideal-dimension upper bound. It gives no global vanishing statement.

For the quartic stable interpretation, Proposition S of `docs/s57_report.md` is an inherited premise, not reproved here: with n=4, ell=h+1, delta>=W and lambda=(4*delta-W,tau), the ambient and geometric stable spaces identify with the corresponding Z picture. Only this conservative delta range is used. The typed exclusion predicates and accepted-state transport overlay are applied per cell. No equality between padded and reducible multiplicities is assumed above degree eight. For any gap deduction with no sharper padded bound, U_pad=a is valid. A determinant rank floor a then implies D<=0. A deficient determinant sample does not prove D>0.

## Claim B15-08-E: a two-point exact full-height ambient witness

Status: EXACT (algebraic derivation; evaluator replay is separately recorded). For every h>=2 define two sources of weight (4,3,2^(h-2)):

    B = [(2,AB) repeated h-1 times, (2,C), (3,ABC)],
    H = [(2,AB) repeated h-2 times, (3,ABC), (4,ABC)].

They have weighted degree 2h+3 and column occupancies h,h,2. Take the symmetric quadratic tensor to be the identity, so f2=sum_i x_i^2. Use the following full polynomials to define two points of Z:

| Point | f2 | f3 | f4 |
|---|---|---|---|
| P | sum_i x_i^2 | x_1^3 | 0 |
| Q | sum_i x_i^2 | x_0^3 | 4*x_0*x_1^3 |

All tensor entries are integers: at P, T3(1,1,1)=1; at Q, T3(0,0,0)=1 and the symmetric entry T4(0,1,1,1)=1. Unlisted entries are zero, except for the diagonal quadratic entries. The coefficient 4 in f4 is essential.

For B the C-only quadratic contributes u2=e_0. Only the short assignment (0,1) survives. At P its special pair matrix is E_11, giving

    B(P) = (h-1)! [y^(h-1) z] det(y I+z E_11) = (h-1)!.

At Q the corresponding T3 slice in direction 1 is zero, so B(Q)=0. Also H(P)=0 because T4 is zero. At Q, the two special pair matrices for the positive short assignment are E_00 and E_11. The negative assignment has the zero direction-1 slice of T3. Consequently

    H(Q) = (h-2)! [y^(h-2) z w] det(y I+z E_00+w E_11) = (h-2)!.

There are no tall-column reorderings or border vectors in these two sources, and the listed source order is also the short-column order. The evaluation matrix with rows (B,H) and columns (P,Q) is therefore diag((h-1)!,(h-2)!). At h=8 it is diag(5040,720), with integer determinant 3,628,800. The exact character count a_inf((4,3,2^6))=2 supplies the upper bound. This proves ambient completeness for that full-height cell without a sampled saturation assertion or an assumed bracket spanning theorem. The points are generic-family controls (points of unrestricted Z); they are not asserted to be determinant or padded points, so this witness alone gives no geometric multiplicity comparison.

The formula is independent of any numerical lease. Running the full-height evaluator against it is a separate operational check, whose status must be taken from the session report and receipt. This separation prevents an unexecuted test from being described as a replay.
