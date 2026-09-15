**COMPLETE — independent scoped acceptance of corrected04 and08. No supported finite candidate for09/10.**

14 September 2026; B17-11, gpt-6-astra/xhigh, same B15-11 worktree. This supplement preserves the [first-stage review](b17_11_report.md), [accepted02 supplement](b17_11_supplement02.md), and their certificates. It reviews the corrected [04 report](../../B15-04/docs/b17_04_report.md) and [08 report](../../B15-08/docs/b17_08_report.md), including linked proof and arithmetic artifacts. There was one new fixed independent control, no research search, no new points or representation census, and no wait for12.

The corrected04 eleven-basis identification is **ACCEPTED**. Its actual-padding restriction rank is certified in **[9,10]**; nine is a floor. Slot08's actual five-row product-map rank formula, clipping thresholds, and all-degree exclusion for the specified flag ideal are **ACCEPTED**, with the premises and scope below. Neither report supplies a numerical boundary loss or a viable finite gap test.

| Claim | Decision | Exact scope |
|---|---|---|
|04: Claude's eleven rational determinant candidates equal an invertible rational change of the accepted E basis | **ACCEPTED** | All eleven identities hold globally with the declared429-coordinate indexing, border signs and factorials. |
|04: independent z*per3 has restriction rank at least9 on E | **ACCEPTED** | A specified nonzero9-by-9 minor on actual invertible substitutions; this is the restriction of an eleven-space, not the full padding multiplicity. |
|04: one nonzero global shared kernel vector gives rank at most10 | **ACCEPTED** | The polynomial Hessian identity proves kappa globally, including closure. |
|04: the twelve-point matrix has rank9 and a two-dimensional sample kernel | **ACCEPTED** | Exact finite sample statement. |
|04: the second sample vector vanishes globally; exact restriction rank9 | **UNVERIFIED** | Requires the missing global Psi identity or another valid upper-rank proof. |
|Inference that a sample plateau proves exact global rank9 or a two-dimensional global kernel | **REJECTED** | Finite evaluations give the opposite bound direction. The corrected producer explicitly avoids this inference. |
|04: multiplication by the leading coefficient preserves restriction rank for the transported E space in every d>=27 | **ACCEPTED** | Only this specified eleven-space and shifted weights; no complete all-row ideal claim. |
|08: actual padding multiplicity equals the five-variable product-map rank for length(lambda)<=5 | **ACCEPTED** | Uses the accepted01 density and03 kernel-transfer theorems; proof below. |
|08: T is a product-target multiplicity and U=min(a,T) is a padding ceiling | **ACCEPTED** | No equality between target dimension and actual image rank is supplied. |
|Inference m_pad=U from the product target, or a positive gap from a separating equation | **REJECTED** | Neither rank surjectivity nor a comparison of kernel dimensions follows. |
|08: forbidden-weight clipping and one-base capacity thresholds | **ACCEPTED** | The scoped02 bound is now independently accepted; its rank input remains uncomputed. |
|08: Jflag has no types of length<=8 in any degree | **ACCEPTED** | Jflag=(E24), with generator type(65,17,2^7). This does not apply to the full determinant ideal, unrestricted J24 or saturation. |
|Inference that Jflag's absence excludes all five-row determinant equations or all-degree obstructions | **REJECTED** | It concerns only one generated ideal; accepted01/03 already supply a five-row separator in some unspecified degree. |
|A numerical five-row loss, a positive gap, or a supported09/10 candidate | **UNVERIFIED / NONE SUPPLIED** |08 nominates zero; no09/10 B17 candidate artifacts were present in the inspected docs/results/delivery paths. |

The rejected inferences are adversarial readings, not claims attributed to the corrected reports. Claim-level decisions are also saved in [decisions.json](../results/b17_11/supplement04_08/decisions.json).

**Conventions, inputs and inherited premises.**

Work over C, V=C^16, forms in Sym^4(V*), coefficient algebra A=Sym(Sym^4 V), ordinary monomial coefficients and positive highest weights. In one degree/partition cell H, write a=dim H, i_f=dim(H intersect I(X_f)), and m_f=a-i_f. Then D=m_pad-m_det=i_det-i_pad. The padding polynomial is independent z*per3 in ten independent source variables, embedded in sixteen. A sufficient certificate requires a global determinant coordinate upper B and an actual padding lower r>B in that same cell.

Batch16/INTAKE was followed to the accepted04 filtration and original Hessian11_1631 evidence, plus the accepted product-source and flag-module proofs. The original eleven-space's independence, determinant-closure vanishing, degree27 polynomial lifts and highest-weight identification are inherited accepted premises. They were read and hash-bound, not presented as a new reconstruction of the whole Batch15/16 proof. Accepted01/03/05/06/07 and02 remain unchanged. In particular, the first-stage non-elementary geometry behind01/03 is inherited; this supplement does not offer another proof of ruledness specialization.

Key SHA256 pins:

| Input | SHA256 |
|---|---|
|Corrected04 report|`aee0a938b4099ce0b92b4d953787b80c3f4229cb180a1bcd6ae15f7d4e8945d5`|
|08 report|`246c96c506ebb4e43a979ef68500813e995886e7b323e3618068e931895578d2`|
|Accepted02 supplement|`449a9ac5960889f01932a268f7889a98de1b2a03698cb68122f349c49885172b`|
|04 basis_match.json|`6876d316b89a70c1a5e88ab01be2aff73ad676ec6316fbb9214d7a54cc1e9a2c`|
|04 restriction.json|`92f9579c33fb4b7ca89162b6d8b2f4a9a1be319e46a62a5c787ca54330aee19e`|

The separately pinned [52-input ledger](../results/b17_11/supplement04_08/input_hashes.json), byte snapshots and [146 delivery/input bindings](../results/b17_11/supplement04_08/delivery_bindings.json) include the original rational candidate data, accepted Hessian source vectors, corrected04 code, Euler relations, points, kernel target, and historical08 inputs. Hashes establish provenance; the proofs and independent arithmetic establish the claims.

**04: proof of the exact eleven-basis identification.**

On the monic depressed chart F=t^4+f2(x)t^2+f3(x)t+f4(x), let N_d=Hess(f_d)(e)/(d(d-1)), u_d=N_d e, s_d=e^T N_d e, with nine transverse variables and e=e1. Put p=F(t,e), B=2t^2 N2+6t N3+12N4, v=4t u2+3u3, h=12t^2+2s2 and H=[[h,v^T],[v,B]]. Use A0=det B, D_H=det H, J_d=-u_d^T adj(B)v, Q22=(0,u2)^T adj(H)(0,u2), and T2=tr(adj(H)diag(0,N2)). R_j denotes the t^j coefficient modulo p, and S_j the coefficient of D_H modulo p^2.

The basis order is

```
E=(R1(A0), s2 R3(A0), R2(J2), R3(J3), R3(Q22),
   S3, s2 S5, s3 S6, s4 S7, R1(T2), s2 R3(T2)).
```

These are original fourteen-list indices[0,1,2,3,4,5,6,7,8,10,11]. Candidate coefficient j multiplies `brackets[basis_bracket_indices[j]]`, with429 declared indices in a1019-bracket list. Replacing this by `brackets[j]` changes the polynomials.

Here is the global identity underlying the match. For M(y)=y2 N2+y3 N3+y4 N4 and ordered index lists I,J, define

\[
 \mathcal B(I,J)=(-1)^{|I|}\det\begin{pmatrix}M&U_J\\U_I^T&0\end{pmatrix}
 \quad (|I|=|J|).
\]

Because M e=sum_j y_j u_j, multilinearity followed by subtracting the corresponding first-nine-column combination from the last column gives, for |I|=k+1, |J|=k,

\[
 \sum_j y_j\mathcal B(I,J\mathbin{\|}j)
 =\sum_{i=0}^{k}(-1)^{k-i}s_{I_i}\mathcal B(I\setminus I_i,J).
\]

The new last column has upper part zero and lower part -s_I. Its Laplace signs give exactly the displayed sign; sorting the appended j contributes the permutation sign, and repeated border columns vanish. Multiplying its y^h coefficient by h! gives the left factors h_j. The stored bracket is (-1)^k c2!c3!c4! times the y^c coefficient, times s^z. These signs and factorials are necessary.

The receiver independently regenerates all884 coefficient relations, matches their complete saved ledger, and obtains rational rank590 using ascending pivots. The accepted source vectors are inherited inputs; none of the producer's arithmetic functions are imported. For every candidate C_i, exact reduction of C_i-sum_j M_ij E_j is zero. The saved rational M and inverse multiply to the identity, and an independent determinant calculation gives

\[
 \det M=-1610167840460004934900135107421875\ne0.
\]

Thus **C=M E globally**, with exactly the orientation stated by04. These are identities in actual bracket polynomials; no completeness claim about all their relations is needed. In particular1019-590=429 alone would not prove injectivity of the formal quotient into functions. Global independence comes from the accepted E certificate. Degree27 polynomial lifts and chart density promote the identities to the stated finite coefficient polynomials.

The omitted expression s2^2 S7 has coordinates(12,-10,4,3,0,-1,1,1,1,0,0), also checked by a zero rational residual. It is not a twelfth basis vector. Controls reject the wrong429-index map, omitted border sign, changed mixed factorial normalization and a unit mutation in M.

**04: actual rank floor, global upper bound, and missing kernel.**

For each saved invertible10-by-10 integer L, let G=(z*per3)(L y), c=[t^4]G and a1_i=[t^3 x_i]G. Define Q00=1, Q0i=-3 a1_i, Qii=12c for i>0. Then det Q=(12c)^9 and G(Qy)/c is monic and depressed. Indeed its t^3 x_i coefficient is 12c a1_i-12c a1_i=0. The independent receiver recalculates det L, c, a1, LQ and all three exact jet matrices from the six permanent monomials, with source row0 reserved for independent z. All twelve L have nonzero entries and nonzero determinant, and all c are nonzero. Thus these are actual orbit substitutions; extending GL10 by an identity block gives GL16 substitutions. No per4 or generic ten-variable cubic is substituted.

For each point, the receiver reconstructs132 total E values modulo the fixed prime1000003, using different interpolation nodes(-10..10), unordered-pair Hessian differentiation and a column-replacement derivative for T2. Exact full-Hessian checks at t=-3,5 also agree with the block formula. It recomputes the saved integer9-by-9 determinant by rational Bareiss elimination. Rows0..8 and E columns[0,1,2,4,5,6,7,8,9] give

\[
 \Delta\bmod1000003=617601\ne0.
\]

The degree27 global lift has value c^27 E(N); the saved finite determinant equals Delta times product_(i=0)^8 c_i^27, checked exactly. All denominators used in the modular verification are invertible: c_i are nonzero modulo the prime, the tensor factors are2 and3, and the distinct interpolation nodes differ by at most20. Consequently the modular nonzero result is a valid characteristic-zero rank floor on genuine padding. The saved exact integer values were not all independently recomputed over Q; their modular evaluations and the exact determinant identity are the independent checks needed for this floor. Duplicate-row and changed-value controls fail as expected.

For the upper bound, Euler's identities for any homogeneous cubic C in nine variables give K x=2 grad C and x^T K x=6C, where K=Hess C. Hence the polynomial bordered-determinant identity is

\[
 \det\operatorname{Hess}(zC)
 =-z^8(\nabla C)^T\operatorname{adj}(K)\nabla C
 =-\tfrac32 z^8 C\det K.
\]

This uses K adj(K)=det(K)I and holds even when K is singular. It shows divisibility by zC. Hessians transform by congruence under every invertible linear substitution, so divisibility survives on the entire padding orbit. Monic division and polynomiality extend the resulting equation to its closure.

The Schur identity D_H=h A0+4t J2+3J3 yields

\[
 R_3(D_H)=12R_1(A0)-10s2R_3(A0)+4R_2(J2)+3R_3(J3)
 =S3-s2S5-s3S6+(s2^2-s4)S7.
\]

Thus kappa=(12,-10,4,3,0,0,0,0,0,0,0) is a nonzero ambient element of E whose padding restriction is identically zero. Together with the nonzero minor, this proves

\[
 9\le\operatorname{rank}(E\longrightarrow\mathbb C[X_{\rm pad}])\le10,
 \qquad1\le\dim(E\cap I(X_{\rm pad}))\le2.
\]

The exact sample matrix has rank9. Its other kernel direction can be taken as w=(216,-212,64,0,0,-1,1,1,13,4,2), independent of kappa. Both annihilate all twelve rows. However w is currently only a necessary candidate for a second global kernel direction. The saved Psi identity identifies w.E with an ambient expression; it does not prove that expression vanishes on padding. Even an arbitrarily long finite list of zeros can belong to a nonzero polynomial. The derivation p divides D_H proves kappa only.

Multiplication by c^(d-27) preserves the restriction rank of the transported E space for every d>=27 because the padding coordinate ring is a domain and c is nonzero on it. Its weights become(4d-35,19,2^8). This does not identify the full ideal or full padding space in any new degree. At d27 the inherited complete multiplicities remain a=429, m_det=418 and243<=m_pad<=288, so D lies in[-175,-130]. The new rank floor inside E does not improve the full padding floor243. Actual determinant occurrence in this old cell is inherited from m_det=418; the cell is nevertheless excluded as a positive gap candidate.

**08: proof that the five-variable product map gives the actual rank.**

Let L=C^5 and let R be the cone of products lC with l linear and C cubic in L*. Its projectivization is the image of the projective multiplication map P(L*) times P(Sym^3 L*) to P(Sym^4 L*), so R is closed. Accepted01 proves that the closure of actual five-variable restrictions of independent z*per3 equals R: the per3 cubic map is dominant, and the independent z factor supplies arbitrary l. Restricting to full-rank five-frames retains a dense open set of the parameter space.

The pullback in coefficient degree d is

\[
 \Phi_d:\operatorname{Sym}^d(\operatorname{Sym}^4L)
 \longrightarrow\operatorname{Sym}^dL\otimes
                    \operatorname{Sym}^d(\operatorname{Sym}^3L),
 \qquad c_\alpha\mapsto\sum_{i:\alpha_i>0}b_i a_{\alpha-e_i}.
\]

An element is in ker Phi_d exactly when it vanishes at every lC, hence exactly when it belongs to I(R)_d. Accepted03 identifies the ambient highest-weight spaces and restriction kernels between five and sixteen variables whenever length(lambda)<=5. Restricting Phi_d to that highest-weight space therefore gives

\[
 m_{\rm pad}(d,\lambda)=\operatorname{rank}\Phi_{d,\lambda}.
\]

This is an actual rank identity, conditional on the accepted density and transfer premises, not an assertion of surjectivity. Pieri gives the target multiplicity

\[
 T=\sum_{\mu\vdash3d,\ \lambda/\mu\text{ horizontal }d\text{-strip}}
 [s_\mu]h_d[h_3],\qquad a=[s_\lambda]h_d[h_4],\qquad m_{\rm pad}\le U=\min(a,T).
\]

Interlacing puts mu inside lambda, so all contributing mu have at most five rows. The nine-variable cubic support ceiling imposes no additional deletion here. This explains why the reduction to generic five-variable cubic products is valid for these labels; it does not replace independent ten-variable z*per3 by generic ten-variable cubic padding. Also a horizontal d-strip has at most lambda_1 boxes, giving T=0 when lambda_1<d.

If r image polynomials are independent, their evaluation determinant on r independent parameter copies is a nonzero polynomial: successive choices of points increase the span of their value vectors until its dimension is r. Dominance preserves its nonvanishing after each cubic is replaced by an actual restricted per3. The nonzero determinant open set intersects the full-frame open set. Thus a certified product-map minor can transfer to actual padding. No such finite minor, rational point values or numerical rank is supplied by08. Its symbolic support counts are specifications for future pricing, not a measured representation job.

Accepted01/03 imply some exactly five-row determinant equation survives on padding in an unspecified degree. This only proves that one kernel is not contained in the other. Two distinct one-dimensional kernels inside a two-dimensional ambient space have equal quotient dimensions; therefore that existence statement alone proves no positive D. No degree or partition for09 can be extracted without another argument.

**08: historical02, clipping, and flag-ideal scope.**

Slot08 pinned02 before consuming an independent02 supplement. Its historical provisional wording is accurate for that delivery. This review retains those snapshots, and uses the now accepted [supplement02](b17_11_supplement02.md) for the current decision. The formula is available for scoped use, but still supplies **no numerical loss**. There is no retroactive change to08's input history.

Set W=V*. The source M_lambda=(S_lambda W)^H uses the full determinant stabilizer H, including transposition; s=dim M_lambda is the symmetric rectangular Kronecker orbit multiplicity. The coordinate module is S_lambda(W*)=S_lambda V. Slot02's adapted arc weights(-1,0,1), block dimensions(4,3,9), give f_t=Q0+t Q1+t^2 Q2. On actual extending vectors the forbidden projections outside the inclusive interval[0,2d] vanish. For an exact rank floor b on those same full-H invariant columns,

\[
 m_{\det}\le B(b)=\min(a,s-b),\qquad0\le b\le s.
\]

For integers1<=U<=a, min(a,s-b)<U holds exactly when s-b<U. Consequently

\[
 B(b)<U\iff b\ge\max(0,s-U+1).
\]

Likewise, for B0=min(a,s), strict improvement over B0 requires b>=s-B0+1. When B0=0 this is infeasible, as it should be. For s>=a the first s-a losses do not improve the clipped bound. If s<U, b=0 already passes the source gate, but no such new cell is furnished here. U=0 makes a positive-gap gate impossible.

The Slot06 one-base matching quotient has Hilbert dimension K_d=binom(d+5,5)-binom(d+2,5). Requiring both B<U and B+1<=K_d is equivalent to

\[
 b\ge\max(0,s-\min(U,K_d)+1),\quad U\ge1.
\]

This is only instrument capacity. Separate negative/high forbidden projections must be stacked on the same columns; their ranks cannot be added without independence. An independent equation floor q combines safely as min(a-q,s-b), not as subtraction of q+b without an overlap argument. The receiver checked3276 finite clipping cases. No auxiliary representation counts were made. The relevant adversarial examples are a=5,s=8,b=1 (no improvement), and b=4 (improvement to4, but no crossing of U=4). A nonempty forbidden carrier provides no rank floor.

For the flag exclusion, let mu=(65,17,2^7), of length9, and Jflag=(E24) inside A, with E24 a copy of S_mu V. For d<24 the ideal piece is zero. For every d>=24, multiplication is an equivariant surjection

\[
 S_\mu V\otimes A_{d-24}\twoheadrightarrow (J_{\rm flag})_d.
\]

Every constituent of A_(d-24) has a polynomial partition nu. Littlewood–Richardson nonvanishing c^lambda_(mu,nu)>0 requires mu to be contained in lambda, hence length(lambda)>=9. Complete reducibility prevents a quotient from acquiring an absent type. Therefore Hom_GL16(S_lambda V,(Jflag)_d)=0 for all d and all length(lambda)<=8. In particular q_flag=0 in every five-row cell. This is an all-degree proof for the specified ideal. It supplies no statement about unrestricted J24, saturation or the entire determinant ideal. The parameter contractions in05 remain genuine products and do not alter this conclusion.

**Verification limits, primary attribution, and next sufficient test.**

Fresh here: proof audit of the884-relation argument and the global shared kernel; separate rational elimination and fixed-padding arithmetic; proofs of the08 product-rank, clipping and row-exclusion deductions; current no-candidate decision. Inherited: the accepted E construction/lifts and complete finite counts,01/03 geometry and transfer,02 arc/orbit-source proof,05/06 module and matching constructions. No full symbolic Psi pullback, full padding rank, invariant-basis construction or forbidden-projection rank was computed.

The primary mathematical attributions remain [LMR, §§2.2–2.4 and Theorem2.3.1](https://arxiv.org/pdf/1004.4802v1) for the Hessian/remainder framework and flag generator; [Kadish–Landsberg, Theorem1.7](https://arxiv.org/pdf/1204.4693v1) for product-map background; [BLMW, §4.1 and Proposition5.2.1](https://arxiv.org/pdf/0907.2850v2) for orbit multiplicity sources; and [Beauville, Corollary6.4](https://math.univ-cotedazur.fr/u/beauvill/pubs/det.pdf) for the inherited cubic-surface premise. These citations were already recorded and checked in the accepted/project evidence. There was no fresh literature search or newly downloaded primary source in this supplement. The present finite basis coordinates and minors are project certificates, with the original Claude Opus5 candidate/bracket attribution retained. No novelty or improved LMR size growth is claimed.

The [executable control](../analysis/b17_11_supplement04_08_verify.py) ran once under the inspected original wrapper: exit0,0.38938070001313463 seconds,23334912 peak Job bytes,3530 modular determinants,2596 peak sparse entries. It checked all52 inputs before and after. The [preflight](b17_11_supplement04_08_preflight.md), [verification](../results/b17_11/supplement04_08/verification.json), [resource receipt](../results/logs/b17_11_supplement04_08_resources.json) and snapshots are preserved. The caps were60 seconds/512MiB, one process and one BLAS thread; no cap hit, retry or approval rejection occurred.

**One next sufficient finite gate test, addressed to the integrator:** supply one explicit five-row cell(d,lambda), certified finite a,s,T, and a full-H invariant basis in the adapted02 coordinates, with a concrete support/bit-cost price. A certified forbidden-projection minor of size b>=max(0,s-U+1), U=min(a,T)>=1, proves B=min(a,s-b)<U. That passes the determinant/source gate only. A final positive gap still needs B+1 actual padding columns with a nonzero minor. A beyond-occurrence witness additionally needs actual determinant occurrence in the same cell; B>=1 is not occurrence evidence. No such finite input or candidate is presently supplied, so09/10 have no supported job to accept. Resolving04's Psi identity would settle its old restriction rank, but would not reopen that excluded cell.

The [main manifest](../delivery/b17_11/MANIFEST.json) preserves earlier run/artifact records and appends this supplement. Its [previous manifest archive](../delivery/b17_11/supplement04_08/PREVIOUS_MANIFEST.json) captures the accepted first-stage plus02 delivery before this update.81 prior artifact/manifest checks pass. No closed outputs, coordination files, sandbox/trust/ownership settings or sibling worktree files were changed. No agents, tasks, worktrees, commits, push or publication were created. This bounded review is complete;12 was not awaited.

Finalization after the user's continuation instruction inspected the saved report, receipt, hashes and resources and performed metadata sealing only: **zero additional scientific executions**. The [Slot12 closeout](../../B15-12/docs/b17_12_closeout.md) records04/08 as pending in its earlier snapshot and pins exactly the producer report hashes reviewed above. This final scoped acceptance supplies that missing review input for integration; it does not amend12's delivery or independently review its other claims. The closeout snapshot and finalization-only input hashes are separately recorded in [finalization_metadata.json](../results/b17_11/supplement04_08/finalization_metadata.json), outside the52-input scientific receipt.
