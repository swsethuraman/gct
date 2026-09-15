# B17-07: conormal feasibility audit

**COMPLETE — scoped theorem and negative audit; no new multiplicity obstruction.**

13 September 2026, America/New_York. Existing B15-07 worktree; gpt-6-astra / xhigh. The invariant below is defined on every nonzero homogeneous polynomial, including reducible and nonreduced padding. It has the required downward specialization direction for degenerations from an irreducible hypersurface. A separate counterexample shows that the *whole limiting conormal cycle* depends on the degeneration, even when its general fibers belong to one orbit and its final polynomial is fixed. Thus it cannot silently replace the intrinsic invariant.

There is no proved transfer from these conormal numbers to a positive coordinate-multiplicity gap. This report stops at that boundary. No numerical conjecture, 3/4 constant, coefficient-degree estimate O(m^3), or improved determinant-size growth is adopted.

## 1. Definition and conventions

Work over C. Let V=C^N, N>=3, and let 0!=f in Sym^n(V*). Write f=c product_i f_i^{e_i}, with distinct irreducible homogeneous factors. Put X_i=Z(f_i) in P(V), and define the **reduced conormal cycle**

\[
 C_{\mathrm{red}}(f)=\sum_i[\mathcal N_{X_i}],\qquad
 \mathcal N_X=\overline{\{(x,H):x\in X_{\mathrm{sm}},\ T_xX\subset H\}}
 \subset\mathbb P(V)\times\mathbb P(V^*).
\]

Every component has dimension N-2. If h and eta are the hyperplane classes of the first and second factors, respectively, our **one invariant** is the polynomial

\[
 \mathcal P_f(u)=\sum_{j=0}^{N-2}\delta_j(f)u^j,
 \qquad \delta_j(f)=\int_{C_{\mathrm{red}}(f)}h^{N-2-j}\eta^j. \tag{1}
\]

There are no binomial coefficients in this normalization. Coefficients are nonnegative integers. In particular delta_0(f)=degree(f_red). They are unchanged by nonzero scalar multiplication or by GL(V), acting contragrediently on the second projective factor. Exponents e_i are deliberately discarded. This is an invariant of embedded reduced support, not a measure of its nilpotent thickening.

For a squarefree equation, the conormal is the closure of the gradient graph on its smooth zero set. One must remove the singular locus before closing. For a nonreduced equation, first take its reduced support. For instance f=x^2 has no smooth scheme points; its raw-gradient construction misses the nonempty conormal of the line x=0. Likewise, grad(z^k P) vanishes identically along z=0 for k>=2, although that reduced hyperplane has a conormal component.

The standard conormal/biduality conventions are checked against [Kohn, Theorem 1 and Section 4](https://arxiv.org/html/1607.05932v3). This report fixes (1) explicitly to avoid index reversals between polar-degree conventions.

## 2. Specialization theorem, including nonreduced final fibers

**Theorem.** Let F_t be a family of nonzero degree-n forms over a smooth complex curve with distinguished point 0. Assume its geometric generic hypersurface is integral. The final hypersurface may be reducible or nonreduced. Then, for a general t,

\[
 \delta_j(F_0)\leq\delta_j(F_t)\quad(0\leq j\leq N-2). \tag{2}
\]

In particular, if g is irreducible and [f] belongs to the projective GL(V)-orbit closure of [g], then P_f<=P_g coefficientwise. One strict reverse inequality certifies geometric noncontainment.

**Proof.** The hypersurface family is flat: it is a relative effective Cartier divisor of fixed degree with no zero fiber. Close the generic projective conormal in P(V) x P(V*) x T, and call the closure C. It is integral, dominates the smooth curve, and is flat. Its projective fibers therefore have constant multidegrees.

We use the characteristic-zero principle of Lagrangian specialization: the specialized conormal cycle is effective and is a sum of conormals to subvarieties of the final support. The statement used here is the cycle theorem, not a semicontinuity theorem for an intersection with a zero section. See [Codogni–Krämer, Section 2, Lemmas 2.2–2.3](https://link.springer.com/article/10.1007/s00208-021-02246-y).

Here is why this gives every component required by our definition, including at a nonreduced fiber. The first projection C -> Z(F) is proper and contains the generic hypersurface in its image. Its image is consequently the entire family. It surjects onto every irreducible component X_i of the final support. A finite collection of conormals over proper subvarieties of X_i cannot cover its generic point. Thus [C_0] contains [N_{X_i}] with some positive integer coefficient for every i. In particular

\[
 [C_0]=C_{\mathrm{red}}(F_0)+E
\]

with E effective. We do not assert that the coefficient on X_i equals e_i. The projection argument uses the support, not smoothness of the nonreduced scheme. Intersecting E with any product of h and eta of total degree N-2 gives a nonnegative number, since these classes are globally generated. Constancy of the multidegrees of C proves (2).

For the orbit-closure assertion, take an algebraic curve through [f] whose general point lies in the orbit, normalize it, and locally trivialize the coefficient line. A finite base extension is harmless. This reduces to the preceding family. The argument does not assume that every boundary point is a one-parameter-subgroup limit. QED.

The nonreduced convention and the possibility of additional limiting components are also discussed in [Borovik–Briand, Section 3, Remark 3.6](https://arxiv.org/html/2607.17966v1). That recent preprint is corroborating context, not an additional unproved premise. We use the published Lagrangian specialization theorem above for arbitrary curve degenerations.

## 3. Exact padding rule

Let P(y) be irreducible of degree m in M variables, and embed these variables, an independent z, and any unused variables in V*, with N>=M+1. For k>=1,

\[
 \boxed{\mathcal P_{z^kP}(u)=1+\mathcal P_P(u)} \tag{3}
\]

where the right-hand coefficients computed in P^{M-1} are extended by zeros.

**Proof.** The reduced support is the union of H={z=0} and the cone Y={P(y)=0}. Their conormals are separate components. The hyperplane contributes (1,0,...). The conormal of Y has dual projection equal to that of P in the linear dual subspace P^{M-1}. Cut its first projection by a general P^{M-1} complementary to the cone vertex. This cut is the graph of a linear map from the M core coordinates to the unused coordinates, so its conormal correspondence identifies with that of P. For j<=M-2, the intersection in (1) includes these N-M first-factor hyperplanes and gives delta_j(P). For j>M-2 it vanishes: the dual image has dimension at most M-2. QED.

In particular, for actual independent padding z^{n-m} per_m, M=m^2 and delta_0=m+1, independent of the padding exponent. The permanent is irreducible: its row and column multidegrees are all one. In any factorization, each row and each column would belong entirely to one factor. A variable whose row and column belonged to different factors could occur in neither factor, but every matrix entry occurs in the permanent. Hence every row and column belongs to the same factor, leaving the other factor constant.

Thus (3) uses the actual permanent core. It does not replace it by a generic cubic, identify z*per3 with per4, or identify independent z with a matrix entry. In the existing n=4 case it uses nine core variables and one independent padding variable, embedded in sixteen.

By the determinant/Segre duality, delta_j(det_n)=0 for j>2n-2. The determinant dual is P^{n-1} x P^{n-1}; see [LMR, Section 3.1](https://arxiv.org/pdf/1004.4802v1). This gives a valid geometric obstruction if a padding coefficient beyond that index is positive. It does not supply any new positive coefficient or stronger size bound here. LMR's Theorem 1.0.1 already proves the quadratic border bound m^2/2. Their irreducible-hypersurface discussion and nonreduced warning in Sections 2.1–2.4 must not be read as a statement that the whole limiting conormal is determined by f_red.

## 4. Counterexample: identical double line, different limiting cycles

Take P^2 with coordinates [x:y:z] and dual [a:b:c]. Let L={x=0}, A=[0:1:0], B=[0:0:1]. Consider the two flat families

\[
 F_t=x^2+t yz,\qquad G_t=x^2+t y^2+t^2z^2. \tag{4}
\]

All fibers for t!=0 are smooth conics, and hence belong to the same GL_3 orbit. Both special forms equal x^2. Let N_A={A} x {b=0} and N_B={B} x {c=0}. The flat limiting conormal cycles are

\[
 \lim_{t\to0}[\mathcal N_{F_t}]
   =2[\mathcal N_L]+[\mathcal N_A]+[\mathcal N_B],\qquad
 \lim_{t\to0}[\mathcal N_{G_t}]
   =2[\mathcal N_L]+2[\mathcal N_B]. \tag{5}
\]

**Proof.** The first conic has gradient [2x:tz:ty] and dual equation

\[
 t a^2+4bc=0.
\]

Substitution of its gradient gives exactly 4tF_t. The second has gradient [2x:2ty:2t^2z] and dual equation

\[
 t^2a^2+t b^2+c^2=0,
\]

whose gradient substitution gives 4t^2G_t. The quadratic matrices are invertible for t!=0. Hence these are the actual dual conics, not just equations vanishing on a smaller image.

In the first limit, x=0, bc=0 and incidence by+cz=0 force every possible conormal component to be N_L, N_A or N_B. In the second, x=0, c=0 and by=0 leave only N_L or N_B. All listed correspondences are curves. Proper pushforward to the first P^2 specializes to 2[L], so the coefficient of N_L is two in each case. Pushforward to the dual P^2 specializes to [b=0]+[c=0] for the first family, and 2[c=0] for the second. This gives all the remaining coefficients in (5). There is no other curve component in the permitted support. QED.

The ordinary reduced-support invariant of the final form is P_{x^2}=1, whereas the generic invariant is 2+2u. The cycles in (5) both have multidegrees (2,2), as required by flatness. They are different cycles over exactly the same final polynomial. Consequently:

- Equating the final intrinsic conormal with the flat limit is false.
- Retaining every limiting component or its multiplicity requires specifying the degeneration; it is not an invariant of the final form alone.
- The valid direction for (1) is downward, and the drop can be strict. Neither equality nor the reverse inequality is valid in general.

This is a counterexample to those proposed replacements, not a counterexample to every possible conormal obstruction.

## 5. Why geometric separation is not a multiplicity certificate

Let W=Sym^n(V*) and A_d=C[W]_d=Sym^d(Sym^n V). For lambda partitioning nd use V_lambda=S_lambda V, and write

\[
 A_d=\bigoplus_\lambda V_\lambda\otimes M_{\lambda,d},\quad
 K_f=\operatorname{Hom}_G(V_\lambda,I(\overline{Gf})_d)\subset M_{\lambda,d}.
\]

In this one finite cell, a=dim M, i_f=dim K_f, m_f=a-i_f, so

\[
 D=m_{\rm pad}-m_{\det}=i_{\det}-i_{\rm pad}. \tag{6}
\]

If a conormal inequality proves noncontainment, the definition of a closed algebraic set supplies some coefficient polynomial vanishing on the determinant closure and not on padding. Homogeneity and reductivity supply some degree and isotypic component with K_det not contained in K_pad. That is a statement about subspace position. It implies neither dim K_det>dim K_pad nor any bound on the degree or representation label. Even two different lines in a two-dimensional multiplicity space can have equal dimensions and give different kernels.

For a multiplicity certificate one still needs, in a named finite (d,lambda), a globally valid determinant coordinate upper B and actual padding coordinate lower r>B. Equivalently a determinant ideal floor q and padding floor r must satisfy q+r>a. A conormal degree delta_j is not i_det, m_det, a, or the number of independent coefficient equations. A polar-degree polynomial in point/dual variables is not already a module of equations in the coefficients of f. An elimination or extension construction, its coefficient degree, its GL(V) covariance, and independent restrictions on actual padding would all require proofs.

The project already exhibits the distinction. Following Batch16 INTAKE entries 03 and 04 to their original, hash-matching deliveries: c^23 S7 separates actual z*per3 from det4 in degree 23 and weight (61,15,2^8), while the accepted final counts are a=189, i_det=1, m_det=188 and m_pad<=158. Hence D<=-30 in that same cell. The larger stable example has m_det=418 and 243<=m_pad<=288. These are inherited results; their arithmetic was not replayed here. The source ceiling never substitutes for the actual lower bound.

No implication to all rows, all degrees, or asymptotic multiplicities is drawn. The six nearby excluded cells and the negative degree-seven symmetry certificate remain closed to rank hunting; that screen does not exclude boundary losses elsewhere.

## 6. One next sufficient test, with an exact determinant target

For a narrowly specified *geometric* continuation, fix (m,n)=(3,5), use G=GL_25, and use independent z^2 per3. The single test is

\[
 \boxed{\delta_7(\operatorname{per}_3)>280.} \tag{7}
\]

By (3), this equals delta_7(z^2 per3). The determinant comparison is the exact identity delta_7(det5)=280, proved next. Thus (7) would prove noncontainment in the det5 closure, beyond the integer consequence n>=5 of the existing m=3 quadratic bound. It would still not prove a coordinate-multiplicity gap. The left-hand side is **uncomputed**, and there is no assertion that it exceeds 280.

**Proof of the determinant target.** The dual of Z(det5) is the smooth Segre S=P^4 x P^4 in P^24. Write H=a+b on S, so degree S=binom(8,4)=70 and K_S=-5H. Let L=O_S(1), and let E be the rank-16 kernel of the first-jet evaluation

\[
 0\longrightarrow E\longrightarrow (\mathbb C^{25})^*\otimes O_S
 \longrightarrow J^1L\longrightarrow0.
\]

Linear forms on P^24 generate these first jets because S is smoothly embedded. The projective conormal of S is P(E), with the convention of lines in E. Its dual hyperplane class eta is c1(O_{P(E)}(1)). The jet sequence

\[
 0\longrightarrow\Omega_S^1\otimes L\longrightarrow J^1L\longrightarrow L\longrightarrow0
\]

gives c1(J^1L)=K_S+9H=4H. The projective-bundle relation gives pi_*(eta^16)=-c1(E)=4H. Biduality swaps the two conormal projections. Since their dimension is 23, our index convention yields

\[
 \delta_7(\det_5)=\int_{\mathcal N_S}H^7\eta^{16}
 =\int_S H^7(4H)=4\binom84=280.
\]

This is a hand intersection-theory calculation, not an expansion of det5 or a computed degree of the permanent dual. The associated-geometry degree 280 is not a degree of an equation in quintic coefficients.

For the integrator: this is a sufficient test specification, not a released computation or a positive candidate. Any computational continuation first needs a priced support/algorithm pilot and the ordinary resource gate. No larger lease is requested here. If the intended output is specifically a multiplicity obstruction, a rigorous coefficient-module bridge remains required before this geometric test can authorize a padding coordinate-rank job. A proof of delta_7(per3)<=280 would retire only (7), not every conormal coefficient or every degree.

## 7. Provenance, verification, resources and limits

Fresh deductions in this contribution are (1)–(3) with their stated scope, the explicit pair of cycles (5), the finite-cell transfer audit, and the exact determinant target 280 with test (7). The Lagrangian specialization theorem, biduality and determinant/Segre duality are literature inputs, not claimed new results. No novelty claim is made for the elementary deductions. Batch16 multiplicities, equations and replay acceptances remain inherited.

The required BOARD, SCREEN_REPORT, COMMON_CONTEXT and STOCKTAKE were read. Older text in COMMON_CONTEXT and the Astra report calls the six cells uncomputed; the later SCREEN_REPORT and authorized BOARD supersede that status. Batch16/INTAKE.json was followed through the accepted 03/04 delivery manifests and the 12 milestone review. Five relevant original artifacts match both the archived accepted copies and their declared SHA256 values; see results/b17_07/accepted_evidence_checks.json.

The accessible Gemini critique is Batch16/GEMINI_REVIEW.md. It names an original user attachment, dbea20d6-aaee-414c-893d-908d8a0162c4/pasted-text.txt, that was not supplied in the required local paths. Neither the supplied COMMON_CONTEXT nor the Astra DREAM_REPORT contains the stated 3/4 conormal conjecture. Therefore the original numerical conjecture cannot be quoted or reconstructed faithfully here. The assignment's explicit rejection of that premise is followed, and the independent invariant audit does not need it. No claim of direct inspection of the unavailable attachment is made.

Primary sources were checked online: [Codogni–Krämer, published 2021, journal volume 2022](https://link.springer.com/article/10.1007/s00208-021-02246-y), [Kohn v3, 2017](https://arxiv.org/html/1607.05932v3), [LMR v1, 2010](https://arxiv.org/pdf/1004.4802v1), and [Borovik–Briand v1, 2026](https://arxiv.org/html/2607.17966v1). Stored web receipts are serialized tool retrievals, not publisher-original files. A fetch of the Mignon–Ressayre publisher page failed; its unavailable text is not used as an additional premise. The exact failed request and the benign Git ignore-file warning are preserved in results/b17_07/operations.json.

The bounded executable analysis/b17_07_verify.py checks the two universal gradient/dual identities, incidence, a wrong-sign mutation, the small arithmetic behind 280, and pinned local input hashes. It has no symbolic package, elimination, matrix search, subprocess, or numerical worker thread. Its hardcoded algebra has at most 16 terms in an intermediate polynomial. The pre-run estimate is <=2 seconds and <=64 MiB; the enforced ceiling is 60 seconds / 512 MiB, one process and one BLAS thread through the inspected existing analysis/b15_bound.py. This single control is not a proof by sampling of the specialization theorem, the limiting-cycle multiplicities, or a permanent polar degree. Its measured receipt and scope are in results/b17_07/verification.json and results/logs/b17_07_verify_resources.json.

The one run passed all eight algebra controls and 22 input hashes, exiting 0 in **0.068739 seconds**. Peak Job Object committed memory was **12,861,440 bytes**; peak process working set was **20,811,776 bytes**. No cap was hit. The unchanged wrapper retains its historical `batch15` / `B15-07` metadata labels; the receipt name and this manifest identify the new B17-07 audit. The wrapper's deadline guard thread is not a numerical worker.

Reproduce the small control from this worktree with a fresh owned log name:

```powershell
& .venv/python.exe -B analysis/b15_bound.py --seconds 60 --memory-mb 512 --name b17_07_verify_replay --slot 07 analysis/b17_07_verify.py
```

The manifest binds resources, code, report, source receipts and all relied-on local inputs. This is a filesystem delivery, with no commit, push, publication, new task, agent, worktree, ownership/trust change, or sandbox change. The scoped audit is complete. The missing mathematical bridge, not an assumed numerical inequality, is the stopping point.
