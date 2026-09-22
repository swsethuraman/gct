# A25-02 — Typed bridges and proofs

UNCOMMITTED / NOT RELEASED. New statements below are PROVED by independent hand derivation in this producer assessment; they have no downstream review yet. They are elementary certificate criteria, not a claim of mathematical novelty or a constructed separator. Inputs and inherited results use READ, not REPLAY. Exact source bindings are in SOURCE_BINDINGS.json.

## 1. Objects and conventions

Over C let V=C^5, W5=Sym^4(V*), A=C[W5]=Sym(Sym^4 V), X=(Mat_4)^5. The 70 ordinary coefficient functions are c_alpha(F)=[x^alpha]F. The map phi(B)=det(sum x_k B_k) has 80 entry parameters. Put D=D45=closure(im phi), P=P5=closure{(z per_3) composed with T : T:C^5 -> C^10 linear}. All closures are affine Zariski closures; dimensions of linear spaces here are vector-space dimensions. No projective dimension is added to an affine one.

For coefficient degree d, q=phi*_d:A_d -> C[X]_(4d), K=ker q=I(D)_d, E=im q. The equality follows directly: a polynomial vanishes on im phi iff its pullback is identically zero; its zero set is closed. This is B19-02 Lemma 3.1, PROVED, re-derived here. Affine X is irreducible, so D is irreducible and I(D) is prime. The parameter space for T is irreducible, so P is irreducible too.

Variable substitution means F(x) -> F(gx). Coefficient weights are positive: c_alpha(F(diag(t)x))=t^alpha c_alpha(F). This explicit rule fixes the convention without switching silently between dual representations. On pencils the corresponding substitution mixes the B_k: B'_j=sum_k g_kj B_k. Left/right matrix action is B_k -> U B_k V; transposition is simultaneous B_k -> B_k^T. Then phi(UBV)=(det U det V)phi(B), phi(B^T)=phi(B). Every q(h) satisfies z(UBV)=(det U det V)^d z(B) and z(B^T)=z(B). Any proposed finite source space M must contain the pullbacks under consideration and must have its basis and polynomial membership proved.

If using a representation cell, fix H inside A_d (e.g. a highest-weight space of type lambda partitioning 4d, length <=5) with an exact linearly independent basis h_1,...,h_a. State the raising-operator convention explicitly. In the present convention E_ij c_alpha=(alpha_i+1)c_(alpha+e_i-e_j) for alpha_j>0. The source multiplicity uses the symmetric rectangular Kronecker coefficient s(lambda,(d^4)), i.e. the transpose-fixed part. The ordinary coefficient g(lambda,(d^4),(d^4)) omits that constraint and is only a possibly weaker upper bound. Neither one is the rank of q merely by definition. No Kronecker number is computed or used numerically in this packet.

## 2. The finite separator certificate (Theorem A)

Fix H as above and a basis m_1,...,m_b of a finite M containing q(H). Let Q be the exact b-by-a matrix defined by the polynomial identities q(h_j)=sum_i Q_ij m_i. Fix an explicit actual-padding substitution T and p=(h_1(P_T),...,h_a(P_T)), where P_T=(z per_3) composed with T. Then the following are equivalent:

1. Some h in H belongs to I(D) and h(P_T) is nonzero.
2. There is v in C^a with Qv=0 and pv nonzero.
3. p is not in the row space of Q.
4. rank([Q;p])=rank Q+1.

**Proof (PROVED, independent hand).** An exact basis identifies v with h=sum v_j h_j. The polynomial coordinate identities defining Q give q(h)=0 iff Qv=0, and evaluation gives h(P_T)=pv. This proves 1 iff 2 using section 1. Every row of Q annihilates ker Q, so 2 implies 3. Conversely, (ker Q)^ann=row(Q): inclusion holds as just noted and both have dimension rank Q by rank-nullity. Thus if p is outside the row space, it cannot annihilate ker Q; this proves 3 implies 2. Appending one row increases rank by one exactly when it is outside the row space, proving 3 iff 4. This uses no assertion about orbit multiplicities. QED.

**Finite artifact interpretation.** For a positive certificate one need not compute all of Q or prove its rank: a specified h, a global polynomial identity q(h)=0, and exact h(P_T) nonzero suffice. The matrix theorem says exactly what an exhaustive finite-space check must establish. Over Q, rational bases, pullback identities, v and T make every check exact; existence over C for rational Q,p implies a rational v by solving linear equations. Allow explicitly represented algebraic numbers when needed; do not assert every arbitrary complex witness is already a rational certificate.

**Sampled version (PROVED, independent hand; specializes B19-02 Theorem 7.1).** Let R be the matrix of evaluations h_j(phi(B^(i))) at finitely many exact pencils, rows indexed by i. If a global proof gives rank q|H <= u and an exact or rationally cleared modular nonzero u-minor of R gives rank R >= u, then rank R=rank q|H=u and ker R=ker q|H. Consequently rank([R;p])>u is an exact separation criterion. A nonzero (u+1)-minor of [R;p] modulo a good prime, together with the global ceiling, certifies a characteristic-zero separator exists in H. Explicit h still requires exact reconstruction and identity certification (or the just-proved kernel equality plus an exact R-nullvector). A rank drop in R without the global ceiling proves nothing about membership.

**Proof.** R is evaluation after q, so ker q is contained in ker R and rank R <= rank q. The inequalities force equal ranks, hence equal kernels. Apply Theorem A to this common kernel. Modular nonzero minors give rational rank floors after denominators are cleared and the prime avoids those denominators. Zero modular minors do not supply the missing global ceiling. QED.

## 3. What a source test can and cannot do (Theorem B)

Let N:M -> U be a linear necessary source test, meaning E_H=q(H) is contained in ker N. Then Nq|H=0 identically and ker(Nq|H)=H. Thus applying that composite to coefficient candidates cannot distinguish K intersect H from other coefficient functions. Its useful consequence is instead the dimension bound

    rank(q|H) <= dim ker N = dim M - rank N.

Combined with a saturating determinant evaluation matrix, this can certify equations by section 2. The conclusion alone neither supplies a vector in K nor proves nonvanishing on P.

**Proof (PROVED, independent hand).** The composite vanishes by the stated inclusion. The dimension inequality follows because the image lies in ker N. These are statements in different vector spaces; the zero composite is not the coefficient kernel. QED.

**Five-block corollary (PROVED from inherited factorization).** Let C_arc be the old source test, T_src any further source test (not the padding substitution T), and N_w=L_w C_arc on the entire named M. Then ker[C_arc;T_src;N_w]=ker[C_arc;T_src] and their ranks agree by rank-nullity. Therefore the source-dimension ceiling in Theorem B is unchanged by adding any of these block-scalar tests, even when followed by the sampling certificate of Theorem A. This is the explicit bridge from Astra's source redundancy to a coefficient-construction feasibility test. The corollary is an implication about this certificate, not a no-go for all equations. The inherited factorization requires exactly S6's hypotheses in SCOPE_MATRIX.md.

## 4. Closure of padding-blind outputs (Proposition C)

Let g_1,...,g_s be coefficient polynomials vanishing on all P. Then the ideal (g_1,...,g_s) is contained in I(P). Any output h in that ideal which also belongs to I(D) cannot separate D from P. In particular, polynomial expressions without constant term in these g_i vanish on P. If P is GL5-stable, so does every translate and every polynomial combination of translates; consequently isotypic projections of such a GL5-stable subspace remain in I(P).

**Proof (PROVED, independent hand).** At every P-point each term a_i g_i is zero. For translates use g_i(gP)=0 and GL5-stability of P. A representation component is a subspace of the stable ideal; projection within a finite-dimensional homogeneous stable piece stays in that ideal. QED.

This combines output ideals only after they have landed in the same coefficient ring. It includes the appropriate rank-threshold ideals, positive-degree SL5 invariants, and (with S2's convention) pullbacks of equations of D35 along the specified cubic covariants. It does not claim those generators all lie in I(D); intersection with I(D) is explicit. For an r-minor extraction the hypothesis may hold only at one P-point; then the proposition excludes separation at that point only. A whole-P conclusion needs rank M(P)<r on all P (or a dense subset, followed by closure of polynomial vanishing).

No rational saturation claim follows. If h=a/b extends polynomially but b vanishes on P, vanishing of a on P alone says nothing about the extension's value. Such a construction needs its own regularity, determinant identity, and padding evaluation. Leaving this hypothesis is an out-of-scope class, not evidence of viability.

## 5. Tail transfer, witness tests, and non-arrows

The tail theorem's actual bridge is multiplication by c_(n e1)^(d-t), for a weight lambda with t=sum_(i>=2)lambda_i<d. Every degree-d coefficient monomial has at most t factors other than c_(n e1), so every weight vector factors f=c^(d-t)g, deg g=t. For determinant and actual-padding closures, both prime ideals avoid c: det(x_1 I_n)=x_1^n, and actual padding is x_1^n by sending z and three diagonal permanent entries to x_1 and other entries to zero. Primality proves f in I(D) iff g in I(D), and domain structure of C[P] proves f|P nonzero iff g|P nonzero. Thus a separating weight has t>=D*, including the case t>=d by definition of D*. This restates B24-04 Theorem 1 with independent hand verification; it is not a GL-equivariant map or a multiplicity equality. For t>=d there is no asserted factorization reducing the degree to t.

D2' checks a form-space locus at a pure power. An equation already proved to lie in I(D) passes its pure-power vanishing test tautologically. That is a necessary consistency check, not evidence of padding nonvanishing: x_1^4 is itself both a determinant and actual padding point.

Source forbidden-support maps versus invariant property loci: NOT COMPARABLE without a construction map. Tail size versus determinant-rank direction: NOT COMPARABLE as predicates on different objects. Small evaluation cost versus existence, spanning, independence, equation membership, or separation: NOT ESTABLISHED. Single-point separation versus a positive multiplicity gap or an asymptotic lower bound: NOT ESTABLISHED. No intersection of six subsets of one candidate universe is defined or claimed.
