# S2 to the integrator / s77 — exact finite completion specification

**Prepared, not sent.** Read the [S2 report](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/S2_report.md) for proofs, scope and corrections. New verified work includes an integral-cubic 0/9 theorem, an order-two image bound 29, and a rank-three counterexample with an actual arc. Global r=5 noncontainment remains OPEN.

## A. The shortest unconditional specification: two graph jobs

Use the exact 70 ordinary determinant coefficient functions in the [chart generator](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/build_chart_jobs.py). Source variable x_(16k+4i+j) is the (i,j) entry of A_(k+1). Coefficients are indexed by the exponent array in the [manifest](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/chart_manifest.json). Index 0 is s5^4, so F0=det A5. The target chart F0-ratio=1 has 34 free W coordinates.

For h=0 and h=64, dehomogenize x_h=1. In Q[x_other79,y1,...,y69], compute

H_h = (f_alpha-y_alpha f0 : alpha=1,...,69) : f0^infinity.

Equivalently eliminate u from (1-u f0, all 69 ratio equations). Only **after that** add y_alpha=0 for the 35 indices alpha5=0. Eliminate all 79 source variables. The result in Q[y_good34] is I_h.

Generated jobs:

* [chart_0_Q.sing](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/cas/chart_0_Q.sing)
* [chart_64_Q.sing](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/cas/chart_64_Q.sing)

The exact monomial formula is

F_alpha = sum_(sigma in S4) sign(sigma)
          sum_(k1,...,k4 with counts alpha) product_(i=1)^4 x_(ki,i,sigma(i)).

The files contain all 15,000 signed terms. Each first ring has 149 variables and lex order u > x_other in numeric order > y1,...,y69. The contracted target ring is lex on the 34 good y coordinates. A different certified elimination order is acceptable; record it.

**Success:** obtain a nonzero exact polynomial in each I_h. Unit ideal is acceptable for an empty chart. This proves W is not contained in D5 and supplies the sufficient affine bound <=34. The full 80-source-chart cover reduces to these two via finite row/column permutations and permutations of s1,...,s4; no classification hypothesis or contact cutoff is needed. The proof is in report section 8.

**Reversal:** a certified exact I_h=(0), for either h, proves that chart image is dense in the full W chart and hence W is contained in D5. A solver timeout, a failed search for an equation, or modular zero is not this certificate.

**Economics:** these are exhaustive reference jobs, not claimed cheap runs. No full Gröbner basis was computed here and the Singular files were not executable-tested in this host. Begin with algebraic reductions and a resource-bounded pilot; preserve the exact residual ideal if the pilot fails. Suggested first pilot: one job, 10 minutes and an explicit memory limit chosen for the implementation host. Do not launch an unbounded 149-variable lex run merely because its inputs now exist.

**Certificate requirements:** preserve rational bases and exact generator provenance for the full graph saturation. For a positive equation, show membership after the graph is formed and W imposed, not in a prematurely restricted/saturated source. Retain transformation matrices or explicit identities for the relevant standard-basis and elimination steps; independently reduce their differences to zero. Record denominator exclusions. A modular nonzero equation does not lift automatically to a rational image equation. CRT/rational reconstruction requires exact substitution/membership verification. For a zero ideal or dimension claim, verify the complete elimination basis and its Hilbert/dimension calculation, including the change to the 34-variable ring.

## B. Localization rule that preserves exceptional structure

Once H_h is known, its exceptional chart is H_h+(f0). To restrict to a closed support with ideal K in source coordinates, form

H_h + (f0) + K,

then impose W and any open-chart conditions by saturation. **Do not first substitute a base-family pencil into J and then blow up the resulting zero ideal.** Formation of the blowup need not commute with this non-flat restriction.

For a parameterized support x=B(theta), pull back the already formed H_h+(f0) by adding x-B(theta), keeping all parameters and invertibility conditions. Finite source and flag charts must cover the support, including boundaries excluded by any chosen minor. A calculation at a fixed rational or modular B0 certifies only that fibre unless a uniform specialization or stratification proof is supplied.

Image dimension is a property of the reduced image. Embedded primes do not independently enlarge its underlying set, but replacing J by its radical **before** constructing the Rees algebra can change that image. Preserve the full scheme until the graph and the W restriction have been formed. At that stage a verified minimal-prime decomposition of the restricted graph, or direct elimination, is sufficient for a set-theoretic noncontainment proof.

## C. Finite residual list for a smaller localized attack

The following is an explicit list of unresolved algebra problems, not a claim that their sampled specializations cover the global graph. Job A remains the unconditional completion criterion.

### C1. P cap C21: all consistent affine-linear ranks

In the source-defined primitive normal form M_phi(u(s)), impose rank u<=2 using its 3 by 3 minors and cover rank u=2 by its nonzero 2 by 2 minors. Include rank u<=1 separately or leave it to Job A. Apply left/right frames as in the original definition. For C21, an independent exact incidence presentation uses a 4 by 2 frame U, a nonzero four-vector z and rows v_k of length two, with

A_k U = z v_k  for k=1,...,5,

saturating on full-rank minors of U and a nonzero coordinate of z. Eliminate the frame parameters only with all open charts covered. Intersect this incidence with the P presentation to define the closed support and its rank-two open part without guessing its ideal from the label.

The frozen second-order reduction has source-recorded 30 reduced variables, split a_12,b_18, and nine quadrics

q(a,b)=C(b)a+Q(b),  C a 9 by 12 matrix, Q a nine-vector.

The matrices and splitting were produced at modular base points. The absence of a-a entries there is not a characteristic-zero identity across the support. Rebuild symbolically over Q on a justified chart, or reconstruct and verify all coefficients and tangent-coordinate transformations exactly. Track every denominator.

For **each j=0,...,9**, and **each j-minor Delta of C** that defines a nonempty chart, define the base consistency ideal

K_(j,Delta) = I_(j+1)([C|Q]) : Delta^infinity.

Then solve C a+Q=0 on this chart, or retain these equations together with K_(j,Delta). For j=0 take Delta=1 and set all entries of C and Q to zero. For j=9 the (j+1)-minor ideal is zero, and full row rank ensures consistency. This finite rank cover includes ranks not encountered by the sampler; remove j>=7 only after proving the requisite minors vanish identically. The sampled generic value six is not such a proof.

Decompose every resulting consistent piece, including lower-dimensional pieces missed by a generic affine slice, and intersect with the full graph. **Required inequality:** every fixed-factor image has affine dimension <=34, or equivalently projective image <=33. To retain the stronger recorded 19, prove the corresponding bound by exact target elimination. A slice dimension and a handful of reconstructed points are not a global component certificate.

### C2. ker cap coker: reducible nonzero restricted cubic

Use M0=diag(B,0) and retain all 45 coefficients of B(s). Write B'=B|_(s5=0), f=det B'. Sections 4-5 of S2 remove the need to sample ranks on the **absolutely irreducible** f locus at order two: only ranks 0 and 9 occur, and the image is <=29 there. They do not remove higher-contact work.

The missing nonzero reducible locus is explicit over C:

f=l q,   l=sum_(i=1)^4 l_i s_i,   q=sum_(|beta|=2) q_beta s^beta.

Equate all **20 cubic coefficients** of f-lq. Cover l!=0 by four coordinate charts and q!=0 by ten coordinate charts. This includes repeated factors and products of three linears. Retain frame/chart variables and do not assume the factorization is unique. Nonconstant common factors are precisely why the integral-domain proof fails here.

On a chart where a coefficient of f is nonzero, construct

L_b(c)=[c'^T adj(B')b'] in S4/(f S1).

Use exact quotient elimination or a localized pivot chart; then stratify by minors I_(j+1)(L_b), saturating on every nonzero j-minor for j=0,...,12 if no structural rank bound is imposed. Constant row multiples of B' are always a three-dimensional kernel when f!=0, proving rank<=9, so **j=0,...,9** suffices. Each nonempty rank stratum must be intersected with the full exceptional graph before making an all-contact image claim.

The [rank-three arc](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/intermediate_rank3_arc.json) is a deterministic must-pass test. Its restricted B'=[[x,w,0],[0,y,0],[0,0,z]], b'=(w,0,0), and the reduced matrix has rank 3. It is a concise five-dimensional base pencil with invertible B5 and an actual W-leading arc. A program reporting only strata 0 and 9 on the entire ker/coker support is incomplete.

**Required inequality:** bound the full fixed-factor exceptional image over every factorization/rank piece by <=34 affine. Merely showing its base dimension is smaller than the integral-cubic locus is insufficient.

### C3. ker cap coker: identically zero restricted cubic

Impose all 20 coefficients det B'=0. This is separate from C2's nonzero charts. The original 31-dimensional quotient target used that f!=0; here pi dPhi can be zero and the quotient must be rebuilt from the 35 unrestricted quartic coefficients. Retain det B(s)!=0 for the rank-three common-kernel/cokernel case, covered by nonzero cubic coefficient charts in five variables. If det B(s)=0 identically, transfer to the rank-at-most-two base problem C5.

**Required lemma:** all images of H_h+(f0)+these support equations+W have affine dimension <=34. Neither Theorem 4.1 nor its rank-nine matrix applies when f=0.

### C4. Nonlinear order four and the extra P/C32, SP/C21 branches

Let M(t)=M0+tM1+t^2M2+t^3M3+t^4M4, with **all** entries of M1,...,M4 arbitrary linear forms in five s variables. Define

g_(q,alpha)=[t^q s^alpha]det M(t)
 = [s^alpha] sum_(sigma in S4) sign(sigma)
   sum_(j1+...+j4=q, 0<=ji<=4) product_(i=1)^4 (M_ji)_(i,sigma(i)).

This is an explicit coefficient formula, with no inverse or normalization. Impose all 70 coefficients g0,g1,g2,g3 equal to zero and all 35 bad coefficients of g4 equal to zero. On the target chart g_(4,0)!=0, add

g_(4,alpha)-y_alpha g_(4,0)=0  for the 34 good nonanchor alpha,
1-z g_(4,0)=0.

Add the source chart x_h(M0)=1 and exact support equations when localizing. **Do not fix M1 in a sampled tangent ruling and do not fix particular M2,M3 solutions.** The nonlinear compatibility equations and their full solution sets are the task. There are 315 zero-coefficient equations before the 34 ratio equations and one inverse equation: 4 times 70 plus 35. The nonzero g4 condition makes every such solution a genuine order-four polynomial arc; no extension of its later coefficients is required to realize its leading form.

For support presentations: P/C32 uses P as above and A_k U3=W2 V_k with full-rank 4 by 3 and 4 by 2 frames; SP/C21 uses the source SP builder and the C21 frame equations. Rank drops in these frames belong to their covered boundary charts. The extra quadratic branches are defined by their actual Q2 ideals, not by naming one generic linear component from a modular decomposition.

**Required inequality:** eliminate all base/jet/frame variables and bound the 34-coordinate target image by dimension <=33 (or provide a nonzero image equation). This solves the specified nonlinear order-four image question. It still does not settle q>=5. To close every order, finish the corresponding restrictions of H_h or the full Job A. This session supplies these equations but does **not** claim the nonlinear locus has been solved.

### C5. Deeper rank at most two, rank one and lower-span strata

Define K2 by all coefficients of all 3 by 3 minors of M0(s). There are 16 minors and 35 cubic monomials per minor, hence at most **560 explicit equations**. Define K1 by coefficients of all 2 by 2 minors: 36 minors times 15 quadratic monomials, at most **540 equations**. These are bounded-matrix-rank conditions on the entire pencil, not just the rank of its coefficient array. The source projective charts exclude the zero pencil automatically.

For compression incidences, use frame equations A_k U2=0, their transpose, or A_k U3=z v_k for (3,1); combine them rather than assuming a generic point of one covers its intersections. The skew type uses diag(N(x),0) with invertible left/right frames; cover coefficient ranks of the 3 by 5 x-map by minors and account for ranks zero through three.

Form H_h+(f0)+K2+W, and K1 or frame equations when separating strata. The source-recorded e2 exact-determinant identities control nonzero order-two leading forms only. Their vanishing does not prove that all later forms remain exact determinants. At rank one the same qualification applies to the order-three replacement-row identity.

**Required inequality:** image dimension <=34 affine on every restricted graph piece. The vertex E0=P(D5) is removed by projectivizing; do not reintroduce it as an independently “bounded” rank-zero piece.

### C6. Residual complement / support completeness

If taking the named-support route, provide explicit support ideals K1,...,Kn, including open-chart conditions, in the projective source charts. Let L_h=H_h+(f0)+W. Prove that every component of L_h outside the claimed handled pieces has empty support, or list its actual prime and source contraction. This requires exact localizations/saturations or a verified primary decomposition; inspection of the reduced B alone does not suffice.

The full Job A is an alternative that avoids having to prove this named-support complement empty. It includes all incidences, all higher contact and all embedded structure relevant to the image. It also avoids depending on the source-recorded interior bound 31.

## D. What may be promoted now, and what may not

* The structural rank dichotomy and order-two bound 29 on the integral restricted-cubic locus have proofs and explicit controls; independently review them before banking.
* The rank-three example is an exact counterexample to the **global** 0/9 assertion. Preserve its limited scope: its leading form is an exact determinant and proves no containment reversal.
* The original P/C21 top-component value 19 remains source-recorded. The top driver reconstructs points from a finite-field affine slice; it does not certify the entire rational support or every lower-dimensional component.
* The interior value 31 is source-recorded with a probabilistic Jacobian protocol. If used in a deterministic global proof, supply a structural upper bound or an exact identity/elimination certificate.
* Neither agreement at both house primes nor an unobserved higher rank is a characteristic-zero universal bound.
* The finalized S2/s77 assignment controls over the older repository board. No new LMR rank or source-independence claim is part of this handoff.
