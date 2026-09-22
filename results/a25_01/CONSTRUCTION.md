# Frozen construction — second transverse coefficient jets

UNCOMMITTED / NOT RELEASED. One construction; freeze recorded at the tool-return checkpoint 2026-09-21T00:46:10Z. Status at freeze: proposed no-go, to be proved by an explicit section. The initial draft mistakenly typed a future 00:51:00Z timestamp; it was corrected immediately against the clock before further assessment.

Work over C with the rational model Q. Put y_i=x_(i+1), 1<=i<=4, and write a quartic's first three x1-layers as

    a x1^4 + x1^3 sum_i p_i y_i
      + x1^2 (sum_i q_ii y_i^2 + sum_(i<j) q_ij y_i y_j).

These are 15 ordinary coefficients, not divided powers. Let R2=Q[a,p_1,...,p_4,q_11,q_12,...,q_44] with one q for each i<=j, embedded in A=Q[Sym^4((Q^5)*)]. Let U_d=(R2)_d for 1<=d<=8. Its explicitly generated basis consists of degree-d monomials in these 15 named coefficients; dim U_d=binom(d+14,14). No ambient highest-weight basis is used. The claim, if proved, extends to every d>=0.

The source map is the ordinary determinant coefficient map phi on X=(Mat4)^5, 80 entry variables. M_d is the finite subspace of Q[X]_(4d) consisting of all polynomials z with z(PBQ)=(det P det Q)^d z(B), and z(B^T)=z(B). Define E_d=im(phi*_d) subset M_d and K_d=ker(phi*_d) subset A_d. Each monomial generator H of U_d pulls back to a degree-4d polynomial with exactly these transformation laws, by determinant multiplicativity and transposition. No claim M_d=E_d is made. Ordinary/symmetric rectangular Kronecker numbers are not used.

Choose the 65-parameter family B1=P_a=diag(a,1,1,1), B_(i+1)=P_a C_i, with a and four arbitrary 4x4 matrices C_i. In the arc x1 P_a+t sum_i y_i P_a C_i, the t^0,t^1,t^2 allowed jets give precisely the above coefficient projection pi2 composed with phi. This is a relation-among-allowed-jets question at a scalar normalized pencil, not a forbidden-weight test of the old five-block arc.

Coefficient target: ker(phi* restricted to U_d), with a possible nonzero h in this space. The frozen test asks whether universal polynomial relations among these 15 jets can supply such an h. PROOFS.md will show that the target is zero. This excludes only polynomials in the 15 selected coefficients (and changes of variable applied to such a polynomial), not polynomials mixing several differently framed jet sets.
