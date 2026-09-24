# Exact lift and scoped containment

**PROVED by hand, PRODUCER ONLY / UNCOMMITTED.** No symbolic program, certificate replay, sampled rank, or numerical evaluator was used. No claim of literature priority is made. All coefficients below are ordinary coefficients. Closures are affine Zariski closures over C.

## 1. Spaces, maps and quantified family

Let W=Sym^4((C^5)*), X=(Mat_4(C))^5, phi(B)=det(sum_i x_i B_i), and D=closure(im phi). Let P=closure{l per_3(A(x))}, with l and all nine entries of A arbitrary linear forms in x1,...,x5. This is the actual-padding parametrization, not an identification with all products lC.

Let E={alpha in N^5: |alpha|=4, max_i alpha_i>=2}, pi:W->C^E the coefficient projection, and Y=closure(pi(D)). The omitted subspace K5 is precisely span{product_(j!=i) x_j: 1<=i<=5}. Its five directions stay omitted for every input.

Write S_lit={l per_3(A_sym): l,a,b,c,d,e,f in (C^5)*}, where

    A_sym = [a d e; d b f; e f c].

Let S=closure(S_lit). The seven linear forms give 35 coefficient parameters; no injectivity, dimension equality, genericity, or distinctness is claimed. S_lit consists of actual padded-permanent substitutions: the ten rows of T are (l,a,d,e,d,b,f,e,f,c). The symmetry restriction is an explicit restriction on those rows. We make no assertion that every T has this form or the same image as such a T.

**Theorem A.** S_lit is contained in im phi. Consequently S is contained in D, closure(pi(S)) is contained in Y, and

    for every h in C[c_alpha:alpha in E],
    h|Y=0  implies  h(pi(F))=0 for every F in S.

This covers every degree and every fixed choice of five centers, and also the full 70-coordinate coefficient ring. It is a theorem for S, not for P.

## 2. Universal polynomial certificate

In the polynomial ring Z[u,l,a,b,c,d,e,f] set

    M_u = [ a       d             e
           -d       b          (u-1)f
           -e    -(u+1)f          c ].

The six signed permutation terms of det M_u, with signs included, are

    abc,
    -(u-1)def,
    +(u+1)def,
    +be^2,
    +cd^2,
    +(u-1)(u+1)af^2.

They sum to

    abc+be^2+cd^2+(u^2-1)af^2+2def.

Independently the six unsigned permutation terms of per A_sym sum to

    abc+af^2+be^2+cd^2+2def.

Hence the exact polynomial identity is

    det diag(l,M_u)-l per A_sym = (u^2-2) l a f^2.       (C)

This is the complete certificate, including its explicit ideal-membership multiplier l a f^2. It holds with independent abstract indeterminates before any linear-form substitution.

Take the fixed field K=Q[u]/(u^2-2), embedded in C by either square root of 2. Relation (C) becomes det diag(l,M_u)=l per A_sym. Substituting arbitrary linear forms for l,a,b,c,d,e,f is a ring homomorphism, so the equality holds for every parameter value, including zero forms and dependent forms. The entries of diag(l,M_u) are linear in x. Reading their x_i coefficients gives five 4-by-4 matrices B_i, proving the literal inclusion in Theorem A. No closure argument is needed for a literal family member.

The two conjugates u=+sqrt(2) and u=-sqrt(2) give two determinant presentations of exactly the same form. The algebraic constant has degree 2 and fixed minimal polynomial u^2-2; no approximation to it is used. The construction does not promise rational pencil entries for every rational input. Algebraic pencil entries are sufficient for the stated complex determinant image and are exact permitted data.

## 3. Complete map factorization, closure and descent

Let q denote the 35 coefficients of the seven linear forms. Let s(q)=pi(l per A_sym), and let R_u(q) be the 80 matrix coefficients of diag(l,M_u). R_u is a linear map over K. For the original global determinant map (with all 80 source entries, without a normal-form chart), (C) proves the polynomial-map identity

    s(q) = pi(phi(R_u(q)))                              (F)

over K[q]. In coordinate rings, s*=R_u* phi* pi*. Therefore

    ker(phi* pi*) subset ker(s*)                        (I)

for the entire coefficient ring, not merely a sampled or degree-truncated matrix. For rational h the output s*(h) has rational coefficients; its equality to zero after extension from Q to K implies equality to zero over Q, since the embedding Q[q]->K[q] is injective. No ordered eigenvalues, norm, root-permutation argument, or parameter-dependent denominator appears. In particular there is no point at which clearing a denominator could erase the conclusion.

D is closed by definition. S_lit subset im phi subset D implies S subset D. Applying pi and taking closure proves closure(pi(S)) subset closure(pi(D))=Y. This argument includes all family limits and all projection boundary points arising from this family. It neither asserts pi(D) is closed nor replaces Y by the literal projected image. It does not attempt to certify the larger saturation closure(D+K5) on all P.

If x is changed by any fixed invertible linear map, the seven forms remain arbitrary linear forms and the same matrix identity applies. Thus all fixed changes of variables of this family are covered. Since inclusion already holds before projection, the choice of independent centers cannot undo the obstruction. This transport does not claim K5 is preserved by an arbitrary variable change in a fixed coordinate presentation.

## 4. The exact proposed H

Over Q set A5=Q[c_alpha:alpha in E], with deg c_alpha=1 and wt c_alpha=alpha under F(x)->F(diag(t)x). Choose

    H=(A5)_{8,(24,2,2,2,2)}.

The exact basis is indexed by

    B={m in N^E: sum_alpha m_alpha=8,
                       sum_alpha m_alpha alpha=(24,2,2,2,2)},
    h_m=product_alpha c_alpha^(m_alpha), m in B.

Order E in descending lexicographic order and the exponent arrays m lexicographically. Distinct monomials are linearly independent; these constraints define the full stated weight component, so this is an exact finite basis without an enumerated dimension claim. There are no factorial normalizations. H is not asserted to be a highest-weight space, a GL5 module, or a span of any tableau family. The certificate (I) applies to all of H without forming its basis matrix.

The basis contains c_(4,0,0,0,0)^6 c_(0,2,2,0,0) c_(0,0,0,2,2), so it permits retained data outside the first-center jet. A25-04's theorem for the polynomial algebra in its ten first-center minors does not by itself imply a theorem for all of H. The actual kernel on H, or on all of A5, is not computed here. Theorem A instead closes every potential h in that kernel at the chosen padding family.

## 5. Visibility control and why it does not reopen separation

Set t=x1 and, for any s in C, choose the actual substitution

    l=t, a=t+x5, b=t-x5, c=t,
    d=x2+s t, e=x3, f=x4.

Call the resulting actual padded permanent F_s. The old signed matrix

    N=[a d e; -d b f; -e -f c]

has determinant abc+af^2+be^2+cd^2, so

    F_s-det diag(t,N)=2t(x2+s t)x3x4
                     =2x1x2x3x4+2s x1^2 x3x4.

The first term is in K5; the second is retained for s!=0. This does not recover a discarded direction: the discrepancy itself has gained a different, retained component. In particular the old signed matrix is no longer a completion at s!=0. Its failure alone is not a nonmembership certificate.

One explicit nonzero member of H detecting this particular discrepancy is

    h_star=c_(4,0,0,0,0)^4 c_(2,0,1,1,0)^2
               c_(2,2,0,0,0) c_(2,0,0,0,2).

Direct hand expansion of F_s gives the four relevant coefficients

    1+s^2, 2s, 1, -1,

respectively. Therefore h_star(F_s)=-4s^2(1+s^2)^4 and h_star(F_1)=-64, while h_star(det diag(t,N))=0. This is an actual-padding visibility control and an admissible nonzero coefficient polynomial, **not a determinant equation**. Indeed Theorem A expresses F_1 itself as det diag(t,M_sqrt(2)), so the same value -64 is an exact algebraic determinant counterexample to membership of h_star in I(Y).

For s=0 this also strengthens the old result: A25-04's integer T yields a quartic that itself has a determinant presentation over Q(sqrt(2)), without discarding its squarefree coefficient. It was already forbidden as a five-center separator witness; that ruling remains intact.

## 6. Scientific boundary

The certificate is complete for S, even in the full coefficient ring. It supplies no equation separating general actual padding from Y; no vanishing identity for h_star; no complete kernel description for H; and no inclusion I(Y) subset ker(q_P) for the general 50-parameter actual-padding map. A statement quantified over all P would require that separate complete certificate. No C_PER, C_DUBE, B17-01 smooth-cubic claim, source-rank certificate, or external classification enters this proof.

Registered outcome **(2)** is achieved at the level of **scoped geometric containment / no-go**. No positive multiplicity gap or asymptotic lower bound follows. The producer proof is ready for a separate independent hand audit; acceptance and delivery remain open.
