# Dream session: use padding's hidden splitting before chasing more rank

13 September 2026. Separate exploratory session; **no Batch16 launch**. All new files are in this directory. No worker/canonical evidence, Git state, trust, ownership, sandbox settings, or other sessions were changed. No subagent, heavy lease, push, or publication was used. Slot01 replay and closeout remain launch gates. No applicable `AGENTS.md` was found in the checked workspace/target ancestors or the relevant source ancestors; a workspace search also found none.

## Outcome

**The most useful dream became a negative result.** A product-map argument, a cubic highest-weight chart injection, and a tiny exact character count give

\[
\boxed{m_{z\operatorname{per}_3}(35,(105,19,2^8))\le288.}
\]

Together with the supplied/reviewed `m_det=418` and padding floor 243, this gives

\[
243\le m_{pad}\le288,\qquad -175\le D\le-130,
\qquad141\le i_{pad}\le186.
\]

Thus **419 is impossible if the proof below passes the integrator's independent review**. The bound applies even to the larger family consisting of a linear factor times an arbitrary cubic with at most nine essential variables. It does not use a sampled kernel as an ideal, or assume that stabilizer invariants extend to the closure. The mathematical deduction and arithmetic are complete here; this is a new, same-task result awaiting external review, not a canonical promotion.

The same argument gives padding coordinate upper bounds **158, 218, 288** for the degree-23/25/27 cells. Their finite ambient dimensions are still unknown. I also obtained an exact full-support value **`c^23 S7 = 8,918,784`** on padding. That is one nonzero restriction of an inherited determinant equation; it is not a positive multiplicity gap.

My proposed change to Batch16 is consequently narrow: independently review this upper bound first, then do the finite census using the new ceilings. Do not allocate a padding-rank-419 search. The remaining independence ideas below target a viable finite cell, or the unresolved interval 243–288 for structural understanding.

## What the retained evidence actually says

The problem is in sixteen ambient variables, with **ten independent source variables** `(z,X11,...,X33)` for padding. The weight spaces under discussion are highest-weight multiplicity spaces. Their ranks are neither total orbit dimensions nor tangent dimensions.

At degree 35, the ambient multiplicity is 429. The 1019 bracket constructions span it by a generic rank-429 certificate. The determinant coordinate rank is exactly 418, supported by nonzero minors and eleven independent global equations. The retained full-family padding computation has rank 243 on 462 valid points from 480 integer substitutions, at both primes 2147483647 and 2147483629. Those points vary all ten linear forms, including the leading direction. The same integer ensemble was reused across primes. There is no evident omitted generic degree of freedom in that generator. The later four-point, fixed-leading-matrix diagnostic is a different restriction.

Before this session, 243 was solely a floor. This session has not proved it exact. Its new upper bound comes from a ring map and exact representation counts, not from additional sampled zeros.

The current finite determinant ideal floors are one at degree 23, two at degree 25, and five at degree 27, in tails `(15,2^8)`, `(17,2^8)`, `(19,2^8)`. These are sufficient lifts, not minimum-degree or complete-filtration assertions. Historical pending-review/Git statements inside individual reports are superseded only to the extent stated in the supplied current board/delegation; this session did not re-audit delivery acceptance.

## Why determinant curvature is constrained, and why padding is constrained too

The determinant is alternating in its rows. Adding a multiple of one row to another preserves it because the extra term has two proportional rows and vanishes. Column additions obey the same rule. These operations supply large families of exact identities among values and derivatives. For the permanent, the analogous extra terms generally survive. All-plus coefficients do not, by themselves, establish greater complexity or a multiplicity advantage.

At a generic singular matrix, the determinant's gradient is its cofactor matrix, with the appropriate transpose, and the adjugate has rank one. Put a rank-three 4-by-4 matrix in the form `diag(0,I3)`, and write a perturbation as

\[
Y=\begin{pmatrix}a&r\\c&E\end{pmatrix}.
\]

The quadratic term of the determinant is `a tr(E) - r c`. It pairs `a` with one trace direction, and the three entries of `r` with the three entries of `c`. Its Hessian therefore has rank eight. The bound extends over the singular-matrix hypersurface. Pulling back by an arbitrary linear pencil preserves the rank bound. At a simple root of the line polynomial `p`, a ten-variable Hessian has corank at least two, so its determinant vanishes to order at least two: `p^2 | det H`. Polynomial remainder identities and density, rather than the choice of a convenient matrix normal form alone, make the resulting equations valid on the orbit closure. This is the geometry underlying the retained eleven-space; compare [LMR, §§2.1–2.3](https://arxiv.org/html/1004.4802v1#S2).

There are important qualifications. A singular point of a restricted determinant polynomial can arise from a smooth rank-three matrix when all pencil directions are tangent to the determinant hypersurface. Then `a=0` and the Hessian can have rank six; one cannot infer rank at most four from singularity of the restricted polynomial. At an underlying rank-two matrix the Hessian has rank four. Also, the entries of an adjugate are functions of a matrix realization. Their relations are not automatically equations in quartic coefficients invariant under `GL16`.

Here is the requested exact intuition check:

\[
X=\begin{pmatrix}1&1&1\\1&2&3\\1&1&-3\end{pmatrix},\qquad
\operatorname{per}(X)=0,
\]
\[
\left(\frac{\partial\operatorname{per}}{\partial X_{ij}}\right)
=\begin{pmatrix}-3&0&3\\-2&-2&2\\5&4&3\end{pmatrix},\qquad\det=48.
\]

Adding row two to row one preserves the determinant `-4` but changes the permanent from 0 to 6. The **9-by-9 Hessian**, a different matrix from the displayed 3-by-3 first-partial array, has rank nine. At `(z,X)=(1,X)`, the 10-by-10 Hessian of `z per3` also has rank nine. These are natural-coordinate controls, not a new det4 separation theorem or a multiplicity computation.

Padding has an especially strong constraint that is easy to miss. For any homogeneous cubic `C` in nine variables, with `g=grad C` and `H_C=Hess C`,

\[
H_{zC}=\begin{pmatrix}0&g^T\\g&zH_C\end{pmatrix},\qquad
H_Cx=2g,
\]
\[
\boxed{\det H_{zC}=-\frac32 z^8 C\det H_C.}\tag{1}
\]

**Derivation here.** The bordered determinant equals `-z^8 g^T adj(H_C) g`. Euler's identity gives
`g^T adj(H_C) g = det(H_C) x^T H_C x /4 = (3/2) C det(H_C)`.
This is a polynomial identity, including singular `H_C`; inversion is unnecessary. It transports under arbitrary invertible changes of the ten essential variables by Hessian congruence. It applies to any ten-dimensional restriction of the sixteen-variable padded orbit, by substitution and density.

At `C=0,z!=0`, the vector `(-2z,x)` lies in the Hessian kernel. At `z=0`, the Hessian has rank at most two. Thus the two components of the padded hypersurface have very different curvature. In particular `zC` divides its full essential Hessian determinant, but generally its square does not. The intersection `z=C=0` is a singular locus of codimension two. Padding is not a generic quartic with unusually free derivatives.

There is an equivalent structural description. On the ten essential variables let `K` be projection onto the `z` coordinate. Then `K^2=K`, `rank K=1`, and the directional linear-vector-field operator satisfies

\[
D_KP=P,\qquad D_{I-4K}P=0.
\]

Conversely, a quartic satisfying `D_KF=F` for a rank-one projector has exactly one factor from that eigendirection and a cubic in its nine-dimensional complement. This incidence description survives change of basis; eliminating `K` describes the closure of this split family. The distinction between a cubic in nine essential variables and an arbitrary cubic in all ten variables is exactly what makes the new bound stronger than the old reducible-normalization ceiling 737.

## Resolved hypothesis 1: a separated-cubic upper bound kills the stable target

**Claim and certificate.** The proof below establishes the ceiling 288. The ring-map direction is essential throughout.

### A. A larger variety with a small source representation

Use the repository's positive-partition convention for coordinate representations, and write `V` for its sixteen-dimensional degree-one coordinate representation. Let

`Y = Sub_9(Sym^3 V*)`, the variety of cubics using at most nine variables, and

`Z = closure{ l C : l in V*, C in Y }`.

The independent padded-permanent orbit closure `X_pad` lies in `Z`. Indeed every linear substitution in `z per3` gives a linear factor times a cubic using at most nine linear forms. Consider multiplication `mu(l,C)=l C`. Pullback injects the coordinate ring of its image closure into the source ring. In coefficient degree `d`, the image has bidegree `(d,d)`, so

\[
\mathbb C[Z]_d\hookrightarrow \operatorname{Sym}^d V\otimes\mathbb C[Y]_d.
\tag{2}
\]

Restriction from `Z` to `X_pad` is surjective. Over characteristic zero these are maps of semisimple finite-degree `GL(V)` representations, hence

\[
m_{pad}(d,\lambda)\le m_Z(d,\lambda)
\le \sum_{\substack{|\mu|=3d,\ \ell(\mu)\le9\\\lambda/\mu\text{ horizontal }d\text{-strip}}}
a^{(3)}_d(\mu).\tag{3}
\]

Here `a^(3)_d(mu)` is the ambient cubic plethysm multiplicity in nine variables. Subspace inheritance removes the types of length greater than nine and retains the cubic types of length at most nine. Equivalently one can use only the corresponding upper bound, which is enough for (3). The product-map framework and inheritance are established ingredients; see [Kadish–Landsberg, Theorem 1.7 and Proposition 1.12](https://arxiv.org/pdf/1204.4693v1). The particular subspace-restricted target and numerical consequence here are derived in this session. No normalization-isomorphism claim is required.

### B. There are only eighteen channels

For

\[
\lambda=(4d-t-16,t,2^8)
\]

at each of `(d,t)=(23,15),(25,17),(27,19),(35,19)`, Pieri interlacing and `ell(mu)<=9` force

\[
\mu_b=(3d-14-b,b,2^7),\qquad b=2,\ldots,t.\tag{4}
\]

Reason: `mu_10=0`; interlacing forces `mu_3,...,mu_9=2`, and `2<=mu_2<=t`. Its size fixes `mu_1`. All these choices satisfy the remaining interlacing inequalities at the listed degrees. The independent checker also enumerates the horizontal strips directly and matches this list, rather than assuming it. At the stable cell the eighteen shapes are `(91-b,b,2^7)`.

### C. A finite cubic space injects into a small depressed-cubic space

For a cubic in nine variables choose coordinates `(s,y1,...,y8)`. On the open chart of nonzero `s^3` coefficient `c`, divide by `c` and remove the `s^2` term by the linear shear in `s`. The result is

\[
s^3+q_2(y)s+q_3(y).
\]

A highest-weight polynomial of coefficient degree `d` is invariant under the first-row unipotent shears. Its coefficient homogeneity recovers its value before division by `c`. Therefore its restriction to this chart is injective: zero on every normalized depressed cubic would imply zero on the dense `c!=0` chart, hence zero identically. The residual `GL8` highest weight is the tail of `mu_b`, namely `(b,2^7)`. Its image is a polynomial in the coefficients of `q2,q3` of that tail weight. Consequently

\[
a^{(3)}_d(3d-|\beta|,\beta)
\le [S_\beta\mathbb C^8]\,
\operatorname{Sym}(\operatorname{Sym}^2\mathbb C^8\oplus
\operatorname{Sym}^3\mathbb C^8)=:h(\beta).\tag{5}
\]

This is an **injection/upper bound at finite degree**, not a claim that every chart polynomial lifts at that degree. Its proof needs no stable-range equality. Normalization and depression do not add degrees of freedom; they provide a dense-chart test for highest-weight polynomials with known covariance.

### D. Exact count and numerical consequence

The power-sum generating series used for (5) is

\[
\sum_{w\ge0}F_w u^w
=\exp\!\left(\sum_{j=2,3}\sum_{r\ge1}\sum_{\rho\vdash j}
\frac{p_{r\rho}}{r z_\rho}u^{jr}\right),\qquad
h(\beta)=\sum_{\rho\vdash|\beta|}[p_\rho]F_{|\beta|}\,\chi^\beta(\rho).
\tag{6}
\]

The exact values for `beta=(b,2^7)` are:

| b | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| h | 1 | 1 | 2 | 3 | 5 | 6 | 9 | 11 | 14 |

| b | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| h | 16 | 19 | 21 | 24 | 26 | 29 | 31 | 34 | 36 |

Their partial sums through 15, 17, 19 are **158, 218, 288**. Combining (3)–(6) proves the stated upper bounds. In particular `429-288=141` is a legitimate global padded ideal floor, established by an image-dimension bound. No list of 141 explicit equations was reconstructed. The single known floor 243 does not make the upper bound an equality.

**Failure condition / review target.** Reject the conclusion if the product bidegree, subspace inheritance, horizontal strips, chart injection, or exact character sums fail. None of these premises is replaced by a numerical rank plateau. The full argument is in characteristic zero; no modular zero-to-identity inference is involved.

**Novelty and obstacle.** This is new relative to the read Batch16 board: it inserts the nine-variable cubic subspace condition *before* counting the source. The ingredients are standard; no priority or literature novelty is asserted. Arithmetic has two character implementations, but the same agent wrote the argument and checks. Integrator review should focus on (2) and (5), not commission another large padding sample.

## Hypothesis 2: the plateau 243 is the image of a structured multiplication map

**Prediction, not result.** The upper bound leaves only 45 possible new coordinate directions, not 176. Perhaps the multiplication map from the cubic channels has rank 243 already on the larger split-cubic family. Alternatively some of the loss from 288 to 243 is specific to `per3`. Distinguishing these cases identifies the right source of equations.

Factor the restriction map as

`A_(d,lambda) -> (Sym^d V tensor cubic-subspace coordinates)_lambda -> (Sym^d V tensor permanent-orbit-closure coordinates)_lambda`.

The source ceiling 288 is not the image dimension of the first arrow. Tensor channel multiplicities cannot be added as independent images. For the stable cell, an exact matrix for the first arrow of rank 243 would give `m_pad<=243`; the retained padding minor then gives equality. If that first image has rank greater than 243, the second arrow becomes the place to look for permanent-specific losses.

**Small discriminating test.** Evaluate a few full-support forms `l*C` with `C` an independently chosen cubic in nine variables against the retained 243-dimensional padding span in a fixed 429 ambient basis. A row outside it proves only that the enlarged split-cubic family is larger in this cell; it does **not** raise the padding lower bound. Then test only the discovered residual combinations on the actual permanent source. Distinguish all three spaces in the output.

Equation (1) and the rank-one projector incidence provide exact relations to organize the first map. For example, with `D=det H`, `p=t^4+s2 t^2+s3 t+s4`, and `S=D mod p^2`, divisibility `p|D` on split cubics gives

\[
S_3-s_2S_5-s_3S_6-(s_4-s_2^2)S_7=0.\tag{7}
\]

It is one global padding relation in the stable five-dimensional squared-remainder subspace. Its ambient nonzeroness follows from the retained independence of those five expressions. It also vanishes on determinants. This illustrates how a shared equation can be recovered without interpreting four sampled zeros as an identity. It does not account for all 141 forced relations.

**Exact endpoint and failure condition.** The endpoint is a source-restriction matrix with exact rank, backed by polynomial identities for the kernel and a nonzero minor for its image. To prove 243 exact, either first-map rank 243 or eleven-independent-relations style reasoning strengthened to `i_pad>=186` suffices. Any rank-244 minor on actual padding falsifies exact 243. A rank-244 minor on split cubics only falsifies the stronger enlarged-family hypothesis.

**Preflight / obstacle.** Start with at most four split-cubic and four padding points, one prime, a retained basis, and one residual block. Hard cap 60 seconds/512 MiB. Stop before symbolic construction unless a selected channel's source/support sizes are measured. The channel dimensions above are small multiplicities; they do not bound full Schur-module or monomial carrier sizes. This is for understanding the plateau, not a priority route to a stable positive gap now that 288<418.

## Hypothesis 3: coefficient signatures and orbit jets can certify independence in a viable cell

**Prediction.** Sparse parameter coefficients will expose independent padded restrictions with a smaller certificate than a generic point matrix. The correct target is a viable finite cell after the census, or an increment such as 243 to 244. A stable target 419 is now ruled out.

Let `B1,...,Ba` be actual ambient highest-weight polynomials in one finite cell. Pull them back along

\[
\Phi(L)=L_0(x)\sum_{\sigma\in S_3}\prod_iL_{i,\sigma(i)}(x),
\qquad L\in\operatorname{Mat}_{10\times10}.
\]

At degree 35 use the safe common lift `F_i(L)=c(L)^35 B_i(normalize/depress Phi(L))`. These are polynomial functions of the 100 matrix entries, of source degree 140. On `c!=0`, multiplying every evaluation vector by the same nonzero scalar preserves rank. Invertible `L` are dense, so polynomial nonzero coefficient witnesses apply to the genuine orbit. At a degree-`d` finite cell the corresponding source degree is `4d`.

**Triangular/minor certificate.** Choose `k` linear combinations `G_i` of the pulled-back basis and `k` parameter monomials `u^alpha_j` on an explicitly specified substitution chart. Supply the coefficient matrix

`M_(j,i) = [u^alpha_j] G_i(Phi(L(u)))`.

If it is triangular with nonzero diagonal, or has a nonzero determinant over Q or at a good prime with denominator checks, then the restrictions have rank at least `k`. For an increment over the old 243 rows, compute their annihilator `K` in the fixed 429 basis. A coefficient-functional matrix on `K` of rank `s` gives total rank at least `243+s`. This is just the rank of the augmented matrix after elimination. It is not a tangent-dimension argument.

**How to search for a checkable triangular matrix.** Start near an explicit invertible `L0` and activate a small set of matrix-entry parameters. Use a valuation to favor selected matching contributions of the permanent and selected antisymmetrization terms of the brackets. A unique lowest-valuation perfect matching in the coefficient determinant, with a nonzero product, certifies noncancellation. A support graph satisfying Hall's condition alone does not: different matchings can cancel. Leading coefficients must be computed after the bracket's signed sums and Euler/straightening relations, not read off from permanent monomials alone.

There are two traps. A degeneration of the permanent to one matching gives a product of four linear forms and can kill every relevant ten-row function. Keep enough matchings and parameter directions, and certify the actual initial forms. Also a coefficient degree-35 function on one affine matrix line has degree at most 140. That line supplies at most 141 independent coefficient functionals. If its base evaluation is already in the old span, it supplies at most 140 *new* ones. Even without the new upper bound, one line could not have supplied the missing 176 directions for 419.

**Jet variant.** Hasse derivatives in `L` at an invertible `L0` are coefficient functionals of `F_i(L0+U)`. Exact derivatives of the fixed functions give a valid lower-bound matrix. All multivariate orders through 140 determine these polynomials completely; a plateau at order one or two gives no upper bound. Do not claim closure of a Lie-derivative computation within the 429 highest-weight slice: Lie operators generally leave that slice. Differentiate the actual source pullbacks or retain a proved complete representation action.

**Endpoint / failure condition.** At a finite cell with determinant ideal floor `q`, obtain `k=a-q+1`. A certified rank-244 minor falsifies exact 243 in the stable cell but cannot make that cell positive. A vanishing initial coefficient rejects that proposed signature; zero on a finite set of arcs does not reject the functions globally. A complete polynomial restriction kernel, in contrast, supplies a true upper bound.

**Preflight / novelty.** Begin with eight kernel combinations and coefficients of order at most two in two to four parameters. Retain exact support counts; stop at 50,000 live monomials or 50 seconds before the hard cap. These are pilot limits, not a prediction that expansion fits. Never allocate all `binomial(240,100)` Taylor coefficients. Valuation and triangularity are established methods; the proposed new work is a compact signed matching certificate in this explicit bracket family. No such target-space minor was constructed in this session.

## Hypothesis 4: stabilizer channels become lower bounds only after polynomial lifting

**Prediction.** Some low-dimensional cubic-permanent channels will admit explicit polynomial lifts through the multiplication map. This could make a smaller finite padding minor practical and, in a scalable family, turn symmetry information into actual coordinate-ring lower bounds.

For the essential nine-variable permanent, orbit regular functions are controlled by its stabilizer. Their multiplicities bound closure multiplicities from above because restriction to the dense orbit injects the closure coordinate ring. An invariant vector, even several independent invariant vectors, does not reverse this inequality. This extension issue is central in [Bürgisser–Landsberg–Manivel–Weyman, §§4 and 7](https://arxiv.org/html/0907.2850v2).

A legitimate finite bridge is explicit: select independent source-channel functions `psi_j` and construct ambient highest-weight polynomials `B_j` in the required `(d,lambda)` satisfying `mu^*(B_j)=psi_j`. A coefficient/minor certificate for the `psi_j` then proves a lower bound for the image. Solving for these preimages, including multiplication-map kernels, is the substantive task. Merely summing invariant or branching dimensions is insufficient.

A different, asymptotic bridge can use a polynomial `b` whose nonvanishing defines an orbit chart and a proved localization `R_orbit=R_closure[b^-1]`: common powers `b^k` clear denominators of finitely many independent orbit functions. If `b` is a highest-weight function, this changes degree and weight by `k(deg b,wt b)` and preserves independence. It does **not** prove the original degree-35 statement. Boundary-localization mechanisms are studied in [Bürgisser–Ikenmeyer, *Fundamental invariants of orbit closures*](https://arxiv.org/html/1511.02927v2); their hypotheses must be checked for the specific orbit used. Do not assume the padded orbit is polystable or that normality follows.

**Exact target / failure.** First produce two polynomial lifts with independent images in one of the cubic channels of dimensions at most 36, and record their induced quartic weight and degree. Reject a proposed finite bridge if its functions require denominators that cannot be cleared in the allowed degree, if their lifts are dependent, or if the claimed localization/descent is unavailable. Normalization functions may fail to descend even when they have no apparent generic pole.

**Preflight / obstacle.** Count the two candidate supports and the linear lift matrix before solving; one 60-second/512-MiB pilot. Stabilizer character counts are not a resource estimate for constructing covariants. This route has a plausible asymptotic role, but it cannot rescue the excluded stable cell by shifting weights silently.

## Hypothesis 5: an earlier finite rung can improve the inequality

**Prediction, still untested.** A determinant equation may appear before most ambient and padding directions do, leaving a more favorable finite cell. The new padding upper bounds make this sharply falsifiable.

Let `a_d` mean the actual finite ambient count at the displayed weight. From the currently certified determinant ideal floor `q`, the required padding floor is `a_d-q+1`. The table supplies necessary conditions for success **using that floor**, not claims of exact determinant ideal dimensions.

| Cell | q | New padding ceiling U | Padding floor required | Necessary condition using q | Inherited stable ambient ceiling |
|---|---:|---:|---:|---:|---:|
| degree 23 `(61,15,2^8)` | 1 | 158 | `a23` | `a23<=158` | 189 |
| degree 25 `(67,17,2^8)` | 2 | 218 | `a25-1` | `a25<=219` | 294 |
| degree 27 `(73,19,2^8)` | 5 | 288 | `a27-4` | `a27<=292` | 429 |
| degree 35 `(105,19,2^8)` | 11, exact | 288 | 419 | impossible | 429, exact here |

Degree 26 `(71,17,2^8)` also has ceiling 218 by the same interlacing argument; its complete determinant finite filtration must be supplied separately. None of 158/218/288 is an ambient count or a padding lower bound.

There is a stronger exclusion test when a determinant ideal **upper** bound is known. Injective multiplication by the leading quartic coefficient embeds a finite ideal in its stable tail. For tail 19 the reviewed stable ideal dimension is eleven. Thus at degree 27, `a27>=299` implies `m_det>=a27-11>=288>=m_pad`, excluding a gap regardless of whether the known floor five grows. For tails 15 and 17, the retained same-row transport by the nonzero weight-two slice multiplier gives stable ideal upper bound eleven under its stated transport premise. If that premise is independently admitted, `a23>=169` and `a25>=229` similarly exclude those cells. Counts in the intermediate ranges require the actual determinant filtration, not another optimistic floor.

**Fresh positive control for degree 23.** Let the ten source coordinates be ordered as above. Take columns

`a=(1,1,0,0,0,1,0,0,0,1)`,
`b=(2,1,2,1,3,1,2,2,1,4)`,
then the eight standard source vectors `e2,...,e9` with zero-based indices. The resulting ten-by-ten substitution `L=[a,b,e2,...,e9]` has determinant `-1`. Along `(t,x)=(t,e1)`,

`z=t+2`, `X=t I3 + [[1,2,1],[3,1,2],[2,1,4]]`,

`P(t)=(t+2)(t^3+6t^2+19t+43)`.

Its leading coefficient is one, and the full cubic-in-`t` coefficient is `8x1+x5+x9`. Depressing by `t -> t-(8x1+x5+x9)/4` gives `p(t)=t^4+7t^2+21t` on the line. The exact remainder of the full ten-variable Hessian determinant modulo `p^2`, in ascending order, is

`(0,0,-92461824,286868736,293190912,58028544,15128064,8918784)`.

Hence the inherited polynomial `c^23 S7` evaluates to 8,918,784. Hessian congruence contributes `det(L)^2=1`, and the depression shear also has determinant one. This is a full-support evaluation with an explicit extension to GL16. It supplies a nonzero restriction, not all `a23` required directions. Its use of leading `I3` is stated; no global padding rank is inferred from this single choice.

**Target / failure / resource gate.** Count `a23,a25,a27` exactly before constructing larger padding matrices. If the table's inequalities fail, the currently certified `q` cannot prove a gap. Apply a genuine determinant ideal upper bound for a complete exclusion. Prefer degree 23 initially because of its smaller ceiling and the explicit nonzero control, then rank by measured residual requirement. Use a character/filtration size preflight; no degree-92 or degree-108 dense carrier is priced here. Reuse the known eleven-space for exact pole-cancellation conditions. A numerical pole cancellation is not a polynomiality certificate.

## Hypothesis 6: shared higher jets across roots give a new coefficient module

**Prediction.** The determinant's higher derivatives are constrained by a common matrix realization in a way not exhausted by pointwise Hessian ranks. The useful result would be a new finite module with enough independent padding restrictions, rather than a larger list of determinant equations alone.

The complete Taylor expansion at the rank-three normal form uses the **same** `a,r,c,E` in all four orders:

\[
F_1=a,\quad F_2=a\operatorname{tr}E-rc,
\]
\[
F_3=a e_2(E)-r((\operatorname{tr}E)I-E)c,\quad
F_4=a\det E-r\operatorname{adj}(E)c.
\]

At different roots of one pencil, the changes of frame also come from one pencil. Treating the rootwise jets as independent variables loses this compatibility. Conversely, imposing unrelated low-rank decompositions on several derivative tensors is not a derived determinant constraint. Polarization must retain the shared blocks and the product rule for padding.

A root-aware test should use the decomposition `p=l*C` on padding. On its squarefree chart, Chinese remainders split `Q[t]/p` into the linear-factor component and the cubic-factor component. Formula (1) gives order at least eight at the distinguished linear root and, generically, order one at each cubic root. For determinants the relevant ten-variable Hessian determinant has order at least two at every root. This explains why root-sensitive functionals can distinguish known remainders while some symmetric sums vanish. Root labels live on a cover: symmetrize or use exact trace/norm/remainder operations to descend to quartic coefficient polynomials. A count of roots is not a count of multiplicity directions.

**Exact target.** Eliminate the shared realization and basepoint variables to obtain a nonzero polynomial `E` in quartic coefficients, prove universal vanishing after substitution of arbitrary determinant-pencil entries, identify its finite degree/highest weight, and compute its class modulo the specified LMR multiplication image. Then require enough independent padding restrictions to satisfy `q+r>a`. A new equation that padding also satisfies does not improve the gap.

**Failure condition / preflight.** A three-direction Taylor check has 34 nonconstant coefficients and is a useful tiny instrument control, but can have a zero elimination ideal and cannot establish a ten-variable equation. Size the shared-block elimination before running it; stop on an unpriced dense carrier. No such elimination was performed here. The existing corank proof of `p^2` divisibility uses only ordinary second derivatives; it is not itself a higher-derivative compatibility theorem. Membership in an ideal generated by degree-24 equations, membership in its radical, and membership after discriminant saturation are three different questions.

For asymptotic inspiration, [Yabe, Definition 1.4 and Theorem 1.5](https://arxiv.org/html/1504.00151v1#S1) bounds ordinary affine determinantal complexity using the minimum number of products of degree-`k` forms needed for a degree-`2k` Taylor part. This suggests shared higher-jet tests, but its optimization formulation does not automatically produce complex orbit-closure equations. Here `z per3` is itself a sum of six products of two quadratics, so its fourth-degree bi-polynomial rank is at most six; the direct `k=2` Yabe inequality is uninformative at this tiny padded quartic. An asymptotic jet construction must be separately connected to polynomial coefficient modules and independent restrictions. No fixed `(4,3)` computation settles an asymptotic complexity conjecture.

## Ranked next three experiments

1. **Independent receiver for the 288 upper bound.** Review the product/subspace map and the cubic chart injection; rerun the retained exact counts and border-strip checker, preferably regenerating the power-sum coefficients by another construction. Success: an accepted `m_pad<=288` certificate, replacing the stable 419 target with an exclusion. Failure: exhibit the precise failed map/count premise. Current measured numerical time is about two seconds combined and far below 512 MiB; a reviewer has no reason to start a large geometric job.

2. **Finite census plus the eleven-space filtration.** Price and compute the three actual ambient counts; apply the thresholds above and any admitted determinant ideal upper bounds. Success: a rigorous exclusion, or a named finite cell with a attainable rank target. Only the latter proceeds to a padding independence matrix. Start with one sparse count/filtration preflight under 60 seconds/512 MiB; stop if the carrier is not bounded. This remains useful even if all three cells are negative.

3. **A small coefficient/minor block on actual padding, conditional on experiment 2.** In the best surviving finite cell, take a fixed ambient basis, preserve existing evaluation rows, and extract coefficients of at most eight residual functions in two to four source parameters. Success: a nonzero triangular/minor certificate that increases the padding floor toward `a-q+1`. Failure: no gain in the prescribed block; do not repeat blind sampling. If no finite cell survives, use one bounded split-cubic versus permanent residual comparison to investigate 243, then stop unless it reveals a structural relation. A full rank computation is unpriced until the pilot's supports, runtime, and memory are measured.

These are proposed work items, not dispatched Batch16 tasks or lease requests.

## Computations actually performed and reproducibility

All numerical runs were sequential, through the inspected retained `b15_bound.py`, with one Python process, one configured numerical thread, a 60-second wall cap and 512-MiB Windows Job Object cap. The wrapper's timer thread only enforces the deadline. All scripts used standard-library exact integers/rationals; no BLAS work or child process was launched. All three runs exited zero.

| Run | Wall seconds | Peak working-set bytes | Peak Job Object bytes | Scope |
|---|---:|---:|---:|---|
| `dream_tiny_01` | 0.104545 | 21,716,992 | 13,602,816 | Natural-coordinate controls; complete Hessian identity on one line |
| `dream_cubic_01` | 1.502142 | 55,848,960 | 46,977,024 | 18 exact cubic chart counts and source upper sums |
| `dream_independent_01` | 0.451828 | 34,004,992 | 24,494,080 | Independent character formulation, channel enumeration, full-support S7 lift |

The count preflight had at most 344,721 recurrence pairs and a conservative 110,516,224-byte storage estimate at 2048 bytes per partition; this was an estimate, with the actual cap enforced separately. It did not allocate a full representation carrier. All target characters were checked using a second implementation based on connected skew Young diagrams with no 2-by-2 square, independent of the retained beta-number implementation. Power-sum coefficients were retained from the first implementation; direct product checks through weight nine and full character orthogonality through `S5` were performed. This is **not** an external independent review of the geometry, nor a second complete power-sum implementation.

The source count reuses the inspected `wk8_s30_pleth.py` partition/character helpers and the recurrence method of retained B14-04 `recount.py`; attribution is preserved in the code. No retained module's producer or save function was called. The separate character checker imports only this directory's tiny matrix/polynomial helpers. Input hashes are retained in `tiny_evidence.json` and `cubic_bound.json`; they were checked unchanged during their runs. The final manifest records delivery hashes and the final input audit.

From this directory, use the following retained wrapper with fresh receipt names:

```powershell
& 'C:\Users\swami\Projects\gct-gpt\work\batch15_workers\B15-05\.venv\python.exe' -B 'C:\Users\swami\Projects\gct-gpt\Batch15_Launch\native_20260913\equation_review\evidence\analysis\b15_bound.py' --slot dream --name dream_tiny_replay --seconds 60 --memory-mb 512 tiny_controls.py
& 'C:\Users\swami\Projects\gct-gpt\work\batch15_workers\B15-05\.venv\python.exe' -B 'C:\Users\swami\Projects\gct-gpt\Batch15_Launch\native_20260913\equation_review\evidence\analysis\b15_bound.py' --slot dream --name dream_cubic_replay --seconds 60 --memory-mb 512 cubic_bound.py
& 'C:\Users\swami\Projects\gct-gpt\work\batch15_workers\B15-05\.venv\python.exe' -B 'C:\Users\swami\Projects\gct-gpt\Batch15_Launch\native_20260913\equation_review\evidence\analysis\b15_bound.py' --slot dream --name dream_independent_replay --seconds 60 --memory-mb 512 verify_cubic_and_lift.py
```

Run sequentially. `tiny_controls.py` compares against its saved output when present; the other scripts regenerate their outputs in this directory, with fresh timing fields. The wrapper's legacy `B15-dream` metadata is a label, not a Batch15 worker dispatch or a lease.

No full finite ambient census, new target-space padding minor, stabilizer lift, symbolic kernel reconstruction, or higher-jet elimination was performed. Those remain proposals with explicit gates above.

## Handoff to the integrator

Keep the Slot01 replay/closeout launch gate and existing resource rules. After independent review, add the **split-cubic source ceiling 288** and stable exclusion to the board; retain 243 as a lower bound unless an exact image calculation closes it. Add finite padding ceilings **158/218/288**, and let the finite census decide whether any of the degree-23/25/27 cells remain useful. The exact degree-23 value **8,918,784** supplies the small padding control for that work.

The next sufficient positive certificate is a full fixed-cell inequality `q+r>a`, with an actual nonzero minor or triangular coefficient witness on padding. The next sufficient negative certificate for the stable cell is acceptance of (2)–(6), already supplied here. No change to the board or canonical evidence has been made by this session.
