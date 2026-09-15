**B17-03 — quartic restriction and exclusion through four rows**

13 September 2026. **COMPLETE: source-grounded deduction, submitted for independent review.** Work was confined to the existing B15-03 worktree and the assigned B17 paths. No mathematical computation or lease was needed. This report is a fresh proof audit, not a claim that a previously accepted numerical certificate already establishes the result.

**Main theorem.** Over \(\mathbb C\), let \(V=\mathbb C^{16}\), let
\(X_{\rm det}=\overline{GL(V)\cdot\det_4}\), and let
\(X_{\rm pad}=\overline{GL(V)\cdot p}\), where
\[
p=z\,\operatorname{per}_3(x_{11},\ldots,x_{33})
\]
uses ten independent linear coordinates and ignores the other six. For every integer \(d\geq0\) and every partition \(\lambda\vdash4d\) with \(\ell(\lambda)\leq4\), in the positive coefficient convention defined below,
\[
K_{\rm det}(d,\lambda)\subseteq K_{\rm pad}(d,\lambda),\qquad
i_{\rm det}(d,\lambda)\leq i_{\rm pad}(d,\lambda),\qquad
m_{\rm pad}(d,\lambda)\leq m_{\rm det}(d,\lambda).
\tag{1}
\]
Here the two \(K\)'s are subspaces of the **same ambient highest-weight space**. Thus
\(D=m_{\rm pad}-m_{\rm det}=i_{\rm det}-i_{\rm pad}\leq0\)
in each such finite cell. The assertion holds in every degree; it does not use stabilization or the onset of known equations.

The geometric input proved below is
\[
\overline{\{\ell C:\ell\in L^*,\ C\in\operatorname{Sym}^3L^*\}}
\ \subseteq\ D_r,
\qquad \dim L=r\leq4,
\tag{2}
\]
where \(D_r\) is the closure of the \(r\)-variable \(4\times4\) linear determinant family. The closure and the polynomial extension to **every** cubic core are essential.

**Coefficient convention and finite-cell dimensions.** For general ambient dimension \(N\), write
\[
W_N=\operatorname{Sym}^4V_N^*,\quad
A_N=\mathbb C[W_N]=\operatorname{Sym}(\operatorname{Sym}^4V_N),\quad
c_\alpha(F)=[x^\alpha]F.
\]
The action on forms is \((g\cdot F)(v)=F(g^{-1}v)\), and that on coefficient polynomials is \((g\cdot h)(F)=h(g^{-1}\cdot F)\). Consequently
\[
\operatorname{wt}(c_\alpha)=\alpha,\qquad
E_{ij}c_\alpha=
\begin{cases}
(\alpha_i+1)c_{\alpha+e_i-e_j},&\alpha_j>0,\\
0,&\alpha_j=0,
\end{cases}\qquad i\ne j.
\tag{3}
\]
Indeed, for \(g=I+tE_{ij}\), evaluating \(g\cdot c_\alpha\) extracts the coefficient of \(x^\alpha\) from \(F(gv)\). The substitution is \(x_i\mapsto x_i+t x_j\), and the first-order contribution comes from exponent \(\alpha+e_i-e_j\), with coefficient \(\alpha_i+1\). This also fixes the sign and the choice of upper-triangular raising operators. The action on products is the derivation action.

Under the differential pairing, \(c_\alpha=e^\alpha/\alpha!\). The house symbols are \(m_\alpha=\alpha!c_\alpha\), and those instead obey \(E_{ij}m_\alpha=\alpha_jm_{\alpha+e_i-e_j}\). No factorial symbols are substituted for ordinary coefficients in this proof. This agrees with the session-29 correction in [isotypic_rank.md](isotypic_rank.md), the direct derivation in [visible_ideals.md](visible_ideals.md), and the quartic convention in [b14_05_transport.md](b14_05_transport.md). Equal kernel dimensions under a diagonal rescaling would not identify the same kernel vectors.

Let \(H^N_{d,\lambda}\) be the weight-\(\lambda\) vectors in \((A_N)_d\) killed by all simple raising operators \(E_{i,i+1}\). For a homogeneous \(GL_N\)-stable ideal \(I(X)\), define
\[
a_N=\dim H^N_{d,\lambda},\quad
K_X=I(X)_d\cap H^N_{d,\lambda},\quad i_X=\dim K_X.
\]
Complete reducibility in characteristic zero gives
\(m_X=a_N-i_X\): an isotypic component is
\(S_\lambda V_N\otimes M\), its ideal submodule is
\(S_\lambda V_N\otimes U\), and the highest-weight line identifies the multiplicity spaces with \(M\) and \(U\). These are multiplicities, not dimensions of the entire isotypic components. In particular, the coordinate representation label is \(S_\lambda V_N\), with no transposed partition or determinant twist.

**Lemma 1: quartic length restriction and multiplicity inheritance.** Let \(1\leq r\leq N\), \(L=\langle e_1,\ldots,e_r\rangle\), and let \(\rho_r:W_N\to W_r\) restrict forms to \(L\). For a \(GL_N\)-stable closed cone \(X\), set \(X_r=\overline{\rho_r(X)}\). If \(\ell(\lambda)\leq r\), padding exponents with zeros induces identifications
\[
H^r_{d,\lambda}\simeq H^N_{d,\lambda},\qquad
K_{X_r}(d,\lambda)\simeq K_X(d,\lambda),\qquad
m_{X_r}(d,\lambda)=m_X(d,\lambda).
\tag{4}
\]
The first multiplicity in (4) is for \(GL_r\), and the second for \(GL_N\); their equality is supplied by the identified highest-weight spaces, not by a comparison of unrelated representations.

*Proof.* Every coefficient monomial \(\prod_{k=1}^d c_{\alpha^{(k)}}\) has weight \(\sum_k\alpha^{(k)}\). All entries of every \(\alpha^{(k)}\) are nonnegative. A monomial of weight \((\lambda_1,\ldots,\lambda_r,0,\ldots,0)\) therefore contains only coefficients supported on the first \(r\) variables. A weight vector is a linear combination of monomials of exactly its weight, so it has a unique expression \(h=\rho_r^*\bar h\), and
\[
h(F)=\bar h(\rho_rF)\quad\text{for every }F.
\tag{5}
\]
The raising operators with \(i<r\) agree in the two rings. Those with \(i\geq r\) vanish identically on these polynomials by the zero case of (3). This proves the first identification, including the reverse implication from a \(GL_r\) highest-weight vector to a \(GL_N\) highest-weight vector.

By (5), \(h\) vanishes on \(X\) if and only if \(\bar h\) vanishes on \(\rho_r(X)\), equivalently on its Zariski closure. That proves the kernel identification. The variety \(X_r\) is a \(GL_r\)-stable cone because block-diagonal changes of coordinates on \(V_N\) extend \(GL_r\). Taking highest-weight dimensions and using complete reducibility proves (4). The degree-zero assertion is immediate from constants. \(\square\)

**Lemma 2: arbitrary substitutions, not just independent frames.** For a fixed quartic \(f\in W_N\), put
\[
\Phi_{f,r}:\operatorname{Hom}(L,V_N)\longrightarrow W_r,
\qquad T\longmapsto f\circ T.
\]
This is a polynomial map in the matrix entries of \(T\). Then
\[
(\overline{GL_N\cdot f})_r
=\overline{\Phi_{f,r}(\operatorname{Hom}(L,V_N))}.
\tag{6}
\]

*Proof.* Full-rank \(T\)'s form a nonempty dense open subset of the affine space \(\operatorname{Hom}(L,V_N)\). Each extends to an invertible endomorphism of \(V_N\), so their images are exactly the restrictions of orbit points. If a coefficient polynomial \(q\) vanishes on those restrictions, the polynomial \(q\circ\Phi_{f,r}\) vanishes on that dense open subset and hence on **all** \(T\). These images therefore have the same vanishing ideal and the same closure. Likewise, \(q\circ\rho_r\) vanishes on the orbit exactly when it vanishes on the orbit closure. This proves (6), without assuming that the image of a closed set under restriction is closed. \(\square\)

For \(N=16\) and \(f=\det_4\), (6) identifies
\[
D_r=\overline{\{\det(\textstyle\sum_{i=1}^r x_iA_i):A_i\in M_4(\mathbb C)\}}.
\tag{7}
\]
In particular, dependent matrix tuples are legitimate points of this closure. For the independent padding, its ten independent source coordinates make the analogous family exactly
\[
P_r=\overline{\{\ell(x)\operatorname{per}_3(B(x)):
\ell\in L^*,\ B\in M_3(L^*)\}}.
\tag{8}
\]
All ten linear forms can be specified arbitrarily as the first ten coordinate functions of \(T\); the six unused coordinates can be set to zero. Lemma 2 justifies this even if \(T\) is not injective. No density assertion about permanent cubics is needed.

**Lemma 3: the classical premise implies density of four-variable cubic determinants.** Define
\[
\delta_r:M_3(L^*)\longrightarrow\operatorname{Sym}^3L^*,\qquad M\longmapsto\det M.
\]
Then \(\overline{\delta_r(M_3(L^*))}=\operatorname{Sym}^3L^*\) for \(r\leq4\).

*Proof for four variables.* The primary input is Beauville, *Determinantal Hypersurfaces*, Michigan Math. J. 48 (2000), 39–64, **Corollary 6.4**, printed pp.52–53: over an algebraically closed field, a smooth cubic surface admits a \(3\times3\) linear determinantal equation. Its preceding Proposition 6.2 supplies the curve-to-matrix construction; Corollary 6.5 separately explains the extra conditions over a field that is not algebraically closed. These precise hypotheses, rather than a parameter count, are what is used here. [Primary paper](https://math.univ-cotedazur.fr/u/beauvill/pubs/det.pdf). Buckley–Košir's author abstract gives a second primary corroboration of the smooth-surface assertion. [Author abstract, v2](https://arxiv.org/abs/math/0606098v2).

Smooth cubic forms constitute a nonempty Zariski open subset \(U\) of the affine cubic coefficient space. For completeness, the set of pairs \((C,[x])\) where all four partial derivatives vanish is closed in \(\operatorname{Sym}^3(\mathbb C^4)^*\times\mathbb P^3\). Its projection is closed because the projective factor is proper; by Euler's identity this is exactly the singular-form locus. The Fermat cubic \(x_1^3+x_2^3+x_3^3+x_4^3\) is smooth over \(\mathbb C\), so the complement is nonempty. Affine coefficient space is irreducible, hence \(U\) is dense.

For \(C\in U\), Beauville's projective equation gives \(\det M=aC\) with \(a\ne0\). Indeed a smooth cubic hypersurface in \(\mathbb P^3\) is integral (distinct hypersurface components would meet and create a singularity), and its degree-three defining equation is unique up to a scalar. Rescaling one row by \(a^{-1}\) gives \(\det M=C\). Thus the **affine** image of \(\delta_4\) contains \(U\), and its closure is the entire cubic space, including singular, reducible, nonreduced, and zero forms.

For fewer variables, let \(q\) vanish on \(\operatorname{im}\delta_r\). Compose \(q\) with the surjective restriction map from four-variable cubics to \(r\)-variable cubics. Restricting a linear matrix commutes with its determinant, so this composite vanishes on \(\operatorname{im}\delta_4\), hence everywhere. Surjectivity makes \(q=0\), proving the smaller-variable density. \(\square\)

This proves a closure statement for arbitrary cubics, not an exact determinantal representation for each singular cubic. No Jacobian rank or stabilizer-dimension calculation is a premise.

**Lemma 4: polynomial extension to arbitrary padded restrictions.** For every \(r\leq4\),
\[
P_r\subseteq R_r\subseteq D_r,\qquad
R_r=\overline{\{\ell C:\ell\in L^*,\ C\in\operatorname{Sym}^3L^*\}}.
\tag{9}
\]

*Proof.* Take any polynomial \(q\in I(D_r)\). In ordinary coefficients the multiplication map is polynomial:
\[
c_\alpha(\ell C)=\sum_{i:\alpha_i>0}b_i a_{\alpha-e_i},
\qquad \ell=\sum_i b_ix_i,\quad C=\sum_{|\beta|=3}a_\beta x^\beta.
\tag{10}
\]
There are no factorial factors in (10). Set \(Q(b,a)=q(\ell C)\), a polynomial in the independent \(b_i,a_\beta\). If \(C=\det M\), then
\[
\ell C=\det\begin{pmatrix}\ell&0\\0&M\end{pmatrix},
\tag{11}
\]
so \(Q(b,\delta_r(M))=0\) for every \(b,M\) by (7). Write \(Q=\sum_\gamma b^\gamma Q_\gamma(a)\). Since this polynomial in \(b\) vanishes for all \(b\), every \(Q_\gamma\) vanishes on \(\operatorname{im}\delta_r\). Lemma 3 gives \(Q_\gamma=0\) identically. Thus \(q(\ell C)=0\) for **every pair** \((\ell,C)\).

This proves \(I(D_r)\subseteq I(R_r)\), hence \(R_r\subseteq D_r\). Formula (8) gives \(P_r\subseteq R_r\). In particular it is valid to specialize \(a\) to the coefficients of \(\operatorname{per}_3(B(x))\), even on every exceptional or singular parameter locus. No assumption that a generic permanent restriction lies in the smooth-cubic open subset is used. \(\square\)

The same argument also verifies the requested ambient interpretation of the block construction. Any \(4\times4\) matrix of linear forms on \(V\) defines an endomorphism \(T:V\to M_4\simeq V\), and \(\det_4\circ T\in X_{\rm det}\): a global equation pulls back to a polynomial on \(\operatorname{End}(V)\) that vanishes on the dense \(GL(V)\). Consequently \(\ell C\in X_{\rm det}\) whenever the cubic \(C\) uses at most four linear coordinates, even if \(\ell\) is an additional independent coordinate. For arbitrary such \(C\), apply the same coefficient-polynomial density argument with the four-dimensional core subspace fixed. This does not treat an arbitrary five-variable cubic core.

**Proof of the main theorem.** For \(d>0\) put \(r=\ell(\lambda)\leq4\). Lemmas 1 and 2 identify the determinant and padding kernels in \(H^{16}_{d,\lambda}\) with their respective kernels in the same space \(H^r_{d,\lambda}\). By (9),
\[
I(D_r)_d\cap H^r_{d,\lambda}
\ \subseteq\ I(P_r)_d\cap H^r_{d,\lambda}.
\]
Transporting back gives the actual subspace inclusion in (1), not just a dimension bound. Subtracting their dimensions from the common ambient multiplicity proves the two numerical inequalities. Constants give equality at \(d=0\). This proves the result for each degree independently, hence for all degrees. \(\square\)

Equivalently, if \(h\) is any highest-weight determinant equation of this length, (5) makes it a polynomial in a restricted quartic. Lemma 2 extends its vanishing from independent determinant frames to arbitrary matrix tuples; Lemma 4 then makes it vanish at every \(\ell\operatorname{per}_3(B)\); and closure makes it vanish on \(X_{\rm pad}\). This explicitly supplies the arbitrary-padded-restriction implication. Merely showing that some generic padded point cannot be separated would not supply this chain.

**Scope of the remaining lengths.** The new theorem leaves length five as the first unresolved length. The elementary support ceiling for this independent padding is ten. A short proof also makes the combined range precise: let \(U\subset V^*\) have dimension ten and contain the coordinates of \(p\). If \(\ell(\lambda)>10\), an \(S_\lambda V\) has no weight supported on the first ten indices. In its semistandard tableau model its first column has more than ten boxes, which cannot be filled strictly increasingly with those ten indices. Therefore every polynomial in such an isotypic component restricts to zero on \(\operatorname{Sym}^4U\): only monomials with weights supported there could survive that restriction. The component is \(GL(V)\)-stable, so it vanishes on all translates of \(\operatorname{Sym}^4U\), in particular on \(GL(V)\cdot p\) and its closure. Thus \(m_{\rm pad}=0\) for length greater than ten. Combined with (1), a positive gap, if one exists, must have **\(5\leq\ell(\lambda)\leq10\)**. These are infinite degree families, not six finite problems. This proof does not assert a nine-row ceiling.

**Evidence audit and acceptance boundary.** The input chain starts at [Batch16/INTAKE.json](../../../../Batch16/INTAKE.json). Its accepted slot-01 entry was followed to the original B15-01 [proof](../../B15-01/docs/b16_01_proof.md), [report](../../B15-01/docs/b16_01_report.md), and delivery manifest. Section 3 of that proof distinguishes the product-map image from its source and retains the nine-variable cubic support with an independent linear factor. Its exact numerical source bounds are contextual here; no value such as 288 is used to prove (1). The original report/proof byte hashes are checked against that accepted delivery in the new metadata receipt. The specified slot-12 milestone review was also read for the distinction between a shared equation, a restricted image, and a full multiplicity comparison. The earlier B15-12 [scope proof](../../B15-12/docs/b15_12_proved.md) was consulted for the independent ten-variable definition.

The requested Batch17 board, screen report, common context, and Batch16 stocktake were read. The newer completed screen supersedes the common context's older description of six cells as unscreened. Those finite-cell exclusions and the degree-seven symmetry screen are inherited context, not premises of this proof; no boundary-loss exclusion is inferred from the latter.

The local [isotypic_rank.md](isotypic_rank.md), Lemmas 3–5 and the session-29 correction, supplies the historical starting argument and convention. This report derives the quartic version directly. Its classical cubic premise was freshly checked in Beauville; its old Jacobian ranks and claims about permanent density were not replayed or used. The historical [l5_containment.md](l5_containment.md) already outlines a length-four block argument. Its wording about exact representations of every four-variable cubic is stronger than the smooth theorem needed here; the closure proof above supplies the appropriate statement. Its conditional branch-based length-five discussion is not an accepted premise here. Thus “fresh” means a newly written, source-checked deduction for review, not a literature priority claim.

Fresh work consists of (3)–(11), the all-degree same-cell conclusion (1), and the support-ten proof. The non-elementary literature premise is Beauville's smooth-surface theorem; basic characteristic-zero representation theory is explicit. No independent reviewer has yet accepted this delivery, and no earlier numerical certificate is relabeled as a replay of it.

**Limitations and next sufficient test.** This does not assert \(m_{\rm det}=a\) for quartics, an exact padding multiplicity, containment of the full ten-variable \(X_{\rm pad}\) in \(X_{\rm det}\), a positive multiplicity gap, or improved LMR determinant-size growth. It concerns independent \(z\operatorname{per}_3\), not \(\operatorname{per}_4\). The unrestricted \(\ell C\) family is used only in the proved four-variable restriction; it does not replace the actual ten-variable padding source with a generic ten-variable cubic. Kernel inclusion here is justified by (9); shared equation presence elsewhere would not imply it.

One next sufficient **structural** test is the five-variable inclusion
\[
\overline{\{\ell(x)\operatorname{per}_3(B(x)):
\ell,B_{ij}\in(\mathbb C^5)^*\}}\ \subseteq\ D_5.
\tag{12}
\]
A proof covering the polynomial closure in (12), with no omitted degenerations, would extend (1) through length five by exactly Lemmas 1–2. A global determinant equation nonzero on an actual left-hand-side point would instead refute (12), but would establish separation only. To obtain a positive multiplicity obstruction after such a failure still requires one fixed finite cell, a global determinant coordinate upper bound \(B\), and an actual padding coordinate lower bound \(r>B\). A source ceiling \(U\) can screen for headroom but cannot supply that lower bound. No computation for (12) was undertaken or priced, and no larger lease is requested by this contribution; any such computation belongs in an integrator-reviewed proposal.

**Resources and delivery.** Mathematical computations: **zero**; Python invocations: **zero**; heavy leases: **none**. The existing `.venv/python.exe` and the fully inspected `analysis/b15_bound.py` are hashed in the manifest but were not executed. The permitted 60-second/512-MiB, one-process/one-BLAS-thread cap was therefore not consumed. No cap hit or uncomputed numerical answer is concealed. All verification in this delivery is proof review and metadata hashing; there is no numerical assertion needing an executable mathematical verifier.

[analysis/b17_03_metadata.ps1](../analysis/b17_03_metadata.ps1) pins local input bytes, checks that they remain unchanged, checks the two original B16-01 delivery bindings, and seals the artifact inventory. [Input hashes](../results/b17_03/input_hashes.json), [metadata verification](../results/b17_03/verification.json), and [delivery manifest](../delivery/b17_03/MANIFEST.json) record the exact scopes. The manifest does not hash itself.

The direct PDF archival action was blocked with: “An attempt was made to access a socket in a way forbidden by its access permissions.” The theorem had already been read through the web reader. There was no escalation, retry, or bypass attempt. The exact action and reason are saved in [blocked_actions.json](../results/b17_03/blocked_actions.json). The hashed [primary-source note](../delivery/b17_03/sources/primary_source_note.json) contains citation details and a short retrieved excerpt; it is explicitly not a hash of the unavailable PDF. This limits archival reproducibility, not the mathematical conclusion from the retrieved theorem.
