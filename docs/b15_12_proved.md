# B15-12 proof record

Model: gpt-6-astra, xhigh. Field: C, with all displayed computational certificates over Z or Q. This per-slot record does not amend the canonical theorem index. Its claims concern the explicitly independent padded form, not a relabelling of inside-variable padding.

## P1. The nine-row restriction does not apply to the independent form

**Status: EXACT.** Let W=C^16 be the variable space, and let

    f = z * sum_{sigma in S3} x_1,sigma(1) x_2,sigma(2) x_3,sigma(3),
    q = x_11 * sum_{sigma in S3} x_1,sigma(1) x_2,sigma(2) x_3,sigma(3).

The ten displayed variables of f are independent; the other six ambient variables are unused. Write X_ind=closure(GL(W).f) and X_in=closure(GL(W).q). Coordinate representations use the positive partition labels in Sym^delta(Sym^4 W*); replacing W* by the repository's V gives its convention Sym^delta(Sym^4 V). This uniform dualisation changes no partition or multiplicity in the comparisons below.

The first-derivative span of f has dimension ten. Indeed, its z derivative is per_3 and contains no z. Its nine matrix-variable derivatives are z times complementary two-by-two permanents. A quadratic monomial in one such derivative determines its omitted row and column, so these nine supports are pairwise disjoint. They are nonempty. Together with the z derivative they are linearly independent. The point f uses at most ten variables, hence exactly ten.

The verifier constructs both polynomials independently, compares f with the banked `per_padded(3,4)` definition, and builds their derivative coefficient matrices in ordinary monomial coefficients. The matrix for f is 10 by 24, and the ten explicitly selected cubic columns in `results/b15_12/controls.json` give the identity matrix: its determinant is 1. It separately finds derivative ranks 9 for q and 16 for det_4. Replacing one selected diagonal entry by zero makes the minor zero. These are exact polynomial calculations, not ranks of random evaluation samples.

The rank of the first-derivative map is invariant under invertible changes of variables. The condition rank<=9 is closed, being given by minors. Thus X_in is contained in the nine-variable subspace variety Sub_9, whereas f is not. In particular f is not in X_in and the two points are not linearly equivalent. Conversely, the substitution z=x_11 is a singular linear substitution, approximated by invertible substitutions. It proves q in X_ind and hence X_in is a proper subvariety of X_ind. The induced map C[X_ind] onto C[X_in] can increase multiplicities on the independent side; it supplies no upper bound of nine rows for that side.

**Source/hypothesis audit.** Kadish--Landsberg, [arXiv:1204.4693v1](https://arxiv.org/abs/1204.4693v1), 20 April 2012, Definition 1.1 and Theorem 1.2, printed p.2, use Sub_{M(m)+1}; their length condition is <=M(m)+1. Their Proposition 1.12, p.4, is the subspace inheritance statement. Taking M=9 allows ten rows. Theorem 1.3, p.2, separately yields lambda_1>=delta(n-m), which here is lambda_1>=delta and is unaffected by independent padding. These are distinct necessary conditions, not a proof of occurrence for every eligible partition.

Bürgisser--Ikenmeyer--Panova, [arXiv:1604.06431v3](https://arxiv.org/abs/1604.06431v3), 17 September 2018, define Z_{n,m} with X_11^{n-m}per_m in Section 1, printed p.2. Theorem 2.1, p.4, gives length<=m^2 for that convention. Its nine-variable hypothesis fails for f. Theorem 1.4, p.3, assumes n>=m^25, which fails at (4,3). The theorem is about occurrence, not equality of multiplicities.

Ikenmeyer--Panova, [arXiv:1512.03798v2](https://arxiv.org/abs/1512.03798v2), 11 August 2017, Appendix 7, Claim 7.1, printed p.17, is the appendix cited by BIP. It starts from an endomorphism-image determinantal realization at size n and obtains independent padding at a polynomially larger size N. Its proof interpolates the X_11 dependence at 1 and 2 and constructs a skew circuit. The size becomes N=4q(n)+8, with q(n) a skew-circuit size for det_n. It is not a same-size coordinate-ring map, orbit equivalence or multiplicity identity. The appendix establishes the required asymptotic complexity comparison; it cannot transfer a fixed-(n,delta,lambda) nine-row exclusion.

The applicable length ceiling for independent padding is therefore ten. In the degree-seven/eight pilot it changes nothing because the ambient plethysm already has length<=delta. In degrees at least ten it changes the permissible search coverage. This is a scope correction and proves no comparison with determinant multiplicity.

**Verifier:** `analysis/b15_12_orbit_bounds.py controls`, output `results/b15_12/controls.json`. **Dependencies:** first-derivative essential-variable criterion; closed rank conditions; primary source versions above. Banked input use is confined to checking the exact polynomial convention.

## P2. Some length-ten representation occurs at degree ten

**Status: EXACT (existence, no individual partition identified).** This strengthens the failed-hypothesis conclusion: a blanket length<=9 bound is false for X_ind.

For a general quartic F=sum_alpha c_alpha X^alpha in sixteen variables, let C(F) have rows indexed by variables and columns by degree-three monomials beta, with entry

    C(F)_{j,beta} = (beta_j+1) c_{beta+e_j}.

Extend the ten-variable exponents in the stored certificate by six zeros. Use rows z,x_11,...,x_33 and the ten recorded columns to define the degree-ten polynomial P(F) as the determinant of that submatrix. The explicit point f gives P(f)=1. Every point of Sub_9 has derivative rank at most nine, so P vanishes on Sub_9.

For completeness, the relevant subspace inheritance fact is that I(Sub_r)_delta consists of the complete Schur isotypic components of length>r. One way to see it is to decompose the polynomial functor Sym^delta(Sym^4 V) into S_lambda V tensor its multiplicity space. Specialization V to C^r preserves that multiplicity space and annihilates precisely the Schur factors of length>r. Taking all GL(V) translates of this specialization gives restriction to Sub_r. Thus no copy of a Schur factor of length<=r can vanish identically on Sub_r.

The GL_16 span of P consequently has only types of length>=10. Since X_ind is contained in Sub_10, every type of length>10 restricts to zero on X_ind. But P restricts nontrivially, as P(f)=1. Complete reducibility in characteristic zero now implies that at least one S_lambda, with |lambda|=40 and length(lambda)=10, occurs in C[X_ind]_10. Equivalently, some lambda of this size and length satisfies m_ind>=1. No individual lambda, ambient multiplicity, or determinant multiplicity is asserted here. The torus weight of the chosen minor is not asserted to be a highest weight.

**Verifier:** the same determinant-one certificate as P1; the Schur-type conclusion is the preceding exact argument. **Dependencies:** characteristic-zero complete reducibility and subspace inheritance. **Next witness for a named cell:** decompose the GL span or project this nonzero minor to an explicit highest-weight component. A determinant upper bound would still be necessary for a positive gap.

## P3. Valid determinant-orbit bounds at n=4

**Status: EXACT as a bound formula.** Let E=F=C^4 and W=E tensor F. The subgroup H0=image(SL(E) x SL(F)) preserves det_4. Matrix transpose also preserves it. The full stabilizer is H=H0 semidirect <transpose>. No large-n limit is required here.

For a partition lambda of N=4delta and length<=16, Schur--Weyl duality gives

    S_lambda(E tensor F)
      = direct_sum_{mu,nu partitions of N}
          S_mu E tensor S_nu F tensor Hom_{S_N}([lambda],[mu] tensor [nu]).

The only SL4-invariant Schur factor of degree 4delta is the determinant power of shape R=(delta,delta,delta,delta), and it is one-dimensional. Thus dim(S_lambda W)^H0=g(lambda,R,R). Transpose swaps the two R factors and acts as the ordinary flip on [R] tensor [R]. The invariant multiplicity for H is therefore sk(lambda,R)=dim Hom_{S_N}([lambda],Sym^2[R]). This identifies the plus sign in the character formula; it does not introduce a sign depending on delta or transpose lambda.

This stabilizer calculation and the restriction inequality are precisely [Bürgisser--Landsberg--Manivel--Weyman, arXiv:0907.2850v2](https://arxiv.org/abs/0907.2850v2), 7 January 2011, Section 5.2, equations (5.2.1), (5.2.5), and Proposition 5.2.1, especially (5.2.7), printed pp.7--9. The pages were checked visually to distinguish the orbit from its overlined closure. Their orbit formula is used only for the specified polynomial representation; no assertion about all rational weights of the orbit ring is needed.

Functions on the determinant closure restrict injectively to its dense orbit. The algebraic Peter--Weyl description of functions on GL(W)/H identifies polynomial-type orbit multiplicities with H-invariant dimensions. In the degree-delta polynomial coordinate ring this gives

    m_det(lambda,delta) <= sk(lambda,R) <= g(lambda,R,R),
    U_det = min(a, sk(lambda,R)).

The dual convention for polynomial functions simply dualises all Schur factors consistently and does not conjugate the partition. Both closure and ambient use the same convention. Nothing here makes the upper bound an equality for the closure.

For cycle type rho, put z_rho=product_j j^{m_j} m_j!. If rho^(2) is the cycle type after squaring a permutation, then each even part 2k becomes two parts k and odd parts remain. Exact character formulas are

    g = sum_rho chi_lambda(rho) chi_R(rho)^2 / z_rho,
    t = sum_rho chi_lambda(rho) chi_R(rho^(2)) / z_rho,
    sk = (g+t)/2,  exterior coefficient = (g-t)/2.

The second formula is the trace of the flip on the multiplicity space; the symmetric-square character identity follows by tracing the flip on A tensor A. All sums can be evaluated as integers divided by N!, using exact class sizes N!/z_rho. Conjugating R tensors [R] with sign, whose tensor square is trivial; hence conjugating both rectangular factors leaves both g and sk unchanged. Conjugating lambda alone is a different operation and is not made.

**Verifier:** `analysis/b15_12_orbit_bounds.py`; seven predeclared cells only. Small controls compare two character constructions for all 209 pairs (lambda,rho) through S_6, prove full weighted row orthogonality there, test hook dimensions and conjugate signs, and test nonnegative integral symmetric/exterior decompositions. Complete pilot status, measured costs and inherited rank-floor comparisons belong in the report. No numerical pilot result is implied by this formula record.
