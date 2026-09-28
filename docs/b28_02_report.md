# B28-02: image multiplicities and first-order determinant boundary points

**HAND (literature assessment): registered verdicts are 2a = (B), 2b = (B).** There are relevant theorems, including explicit first-order boundary components for `det_4`. In the sources searched, no result computes or improves the upper bound for the **degree-four-generated image** at the requested five-variable degrees, and no result decides the residual class-(iii) padding question. These are scoped search conclusions, not claims that such results cannot exist.

**READ (standing):** “No five-row determinant equation is known to be nonzero on padding.” Programme decision: **“no construction ready.”** No record change follows from this slot.

## Provenance and preflight

**READ (administrative):** this fresh task was expressly authorized by the user's launch. Branch `b28-02`, initial HEAD `9daf22c5f311c9153a736a5a27416d5beff37ef6`, and the worktree match PART 27's receipt. Initial Git status was empty; both output paths were absent. No applicable `AGENTS.md` was found. The sandbox required a per-command `safe.directory` for this worktree; no persistent Git configuration was changed. Full preflight: [PREFLIGHT.json](../results/b28_02/PREFLIGHT.json).

| READ: administrative file | Raw SHA-256 |
|---|---|
| `B28_COMMON.md` | `06799a9e404fc45a0944f7fcae88d8dd5511f7721f704ebe69872dd3061c87b9` |
| `B28-02.md` | `ac957649f624f59e69e98f4ea6635f6849ea6c3ac2758dfffc81e4e65a201158` |
| `BATCH28_BOARD.md` | `c635ac1a73e5e0c855c9bc1b75809c447e3b7184d707af75d49bad6c14ba96af` |

**READ (provenance):** all committed mathematical citations below refer to `96a8074d240033161302233672aed5980d84eccb`, abbreviated **C**. [INPUT_BINDINGS.json](../results/b28_02/INPUT_BINDINGS.json) gives SHA-256 of each raw `git show C:path` payload, its Git blob ID, byte count, and read extent. These are not hashes of working copies or Git object headers.

**PRIMARY (provenance):** each source ID below resolves to a version, precise reading locator, download URL, byte count and full SHA-256 in [SOURCES.json](../results/b28_02/SOURCES.json). Those hashes identify the exact downloaded **PDF bytes**. Full downloads do not imply full-paper reading. Third-party PDFs, extracted text and page images are outside the worktree and are not committed. Statements below are paraphrased precisely; mathematical notation is retained. Abstract-only pointers are **UNREAD** for their mathematical claims. [SEARCH_LOG.md](../results/b28_02/SEARCH_LOG.md) records queries, reference-following, access failures and coverage limits.

## 2a: the image, its ambient spaces, and applicable literature

**READ — C:`docs/s56_report.md` §§1-2,4-5; C:`results/b27_05/REPORT.md`.** Let `R = C[M_4(C)^5]^(SL_4 x SL_4)` and `A = C[R_4]`. Use coefficient grading on `A`: `A_k` has matrix-entry degree `4k`. The requested degrees are therefore `k=8,9,10`, or matrix degrees `32,36,40`. The target is `A_k`, not all of `R_(4k)`.

**READ — same committed sources.** The existing exact description is

```text
Theta_k^+ : Ind_(S_4 wreath S_k)^(S_(4k)) 1 --> Sym^2([k^4]),
pi |--> epsilon_pi tensor epsilon_pi,
mult_det(lambda,k) = rank Hom_(S_(4k))([lambda], Theta_k^+).
```

**READ:** its exact Gram kernel is the entrywise square of the Plucker Gram kernel. The source multiplicity is `a(lambda,k)` and the symmetric rectangular Kronecker target multiplicity is `sk(lambda,k^4) = m_det`. Thus the recorded comparison is `mult_det <= min(a,sk)`. Its enumerating implementation is priced out from `k=5`; that is an implementation limit, not an impossibility theorem for other algorithms.

**READ — C:`docs/s38_review.md` §§1-2.** The recorded exhaustive length-five screen has `a <= sk` through `k=10`. A full-ring count, even strengthened by transpose symmetry, supplies no drop below the source in this window. No screen or rank computation was repeated here.

### Spanning and presentation results

**PRIMARY [DW2000](https://hderksen.sites.northeastern.edu/files/2020/12/A.I.a.6.pdf), Theorem 1, p.470; version and SHA-256 in SOURCES.** For an acyclic quiver `Q`, a dimension vector `beta`, and an algebraically closed field, `SI(Q,beta)` is the linear span of Schofield functions `c^V` with Euler pairing `<dim V,beta>=0`; the analogous assertion holds for `c_W`. These are determinants of the square maps defined on p.469.

**HAND (hypothesis check):** the five-arrow Kronecker quiver is acyclic, `beta=(4,4)`, and the field is `C`, so this applies to the full ring in degrees `32,36,40`. Its vertex-character grading is not the `GL_5` highest-weight decomposition under arrow mixing. It neither restricts the spanning functions to products of degree-four coefficients nor gives their image multiplicities. No complexity bound for that image problem is stated here.

**PRIMARY [SVB1999](https://arxiv.org/pdf/math/9907174v1), Theorem 2.3, pp.8-9; version and SHA-256 in SOURCES.** Over an algebraically closed field of characteristic zero, for a finite quiver and dimension vector, the semi-invariant functions are spanned by determinantal semi-invariants. A map `phi` between sums of vertex objects defines `P_(phi,alpha)(p)=det R_p(phi)` when source and target have equal evaluated dimension (§1).

**HAND (hypothesis check):** our quiver and field satisfy these assumptions, at all three requested degrees. The allowed determinant sizes vary. The theorem does not say that the size-four determinants alone generate the degree-`4k` image, or give a rank formula for their products. No image-complexity guarantee follows.

**PRIMARY [IQS2015](https://arxiv.org/pdf/1508.01554v1), Proposition 1 and Fact 4, pp.5-8; version and SHA-256 in SOURCES.** In characteristic zero, for the multilinear map `phi: P(d) tensor P_hat(d) -> R(n,dn)`, the kernel is

```text
K(d) tensor P_hat(d) + P(d) tensor K_hat(d),
```

where `K` and `K_hat` are the respective Plucker-relation spaces. The quotient is the tensor product of the two rectangular Specht modules of shape `(d^n)`.

**HAND (hypothesis check):** `n=4`, `d=k=8,9,10` fits this characteristic-zero multilinear theorem; its labels number `4k`, not five. **READ — s56 §4:** this supplies the target and its straightening after polarization, not the kernel of the diagonal determinant-generated subspace. The source's Proposition 9 concerns generation of the entire invariant ring by all invariants through a degree bound. Neither statement provides the missing image contraction or a complexity bound for it.

**UNREAD [DZ2001](https://link.springer.com/article/10.1007/BF01236060):** the original Domokos-Zubkov theorem was not retrieved; the publisher provides a subscription preview and abstract. It is not promoted to PRIMARY via another paper's attribution. The independently read DW2000 and SVB1999 statements above suffice for the spanning comparison.

### Characters, degree bounds and SAGBI bases

**PRIMARY [M2015](https://arxiv.org/pdf/1510.08420v1), Lemma 1.14 and its proof in §4; version and SHA-256 in SOURCES.** Over `C`, in the source's notation,

```text
R(n,m)_(kn) = direct_sum_(lambda |- kn)
             S_lambda(C^m) ^ {g((k^n),(k^n),lambda)}.
```

Consequently the graded dimension is the sum of these Kronecker coefficients times the corresponding Schur-module dimensions.

**HAND (hypothesis check):** `n=4,m=5` gives an exact full-ring character at `4k=32,36,40`; its weight-space dimensions likewise concern the full ring. **READ — s56 §§1-2:** `A_k` occupies a potentially smaller image, even inside the transpose-symmetric target. The character formula does not compute that image. No runtime bound for doing so is asserted by this lemma.

**PRIMARY [DM2017](https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/05/A.I.a.54.pdf), Theorems 1.2, 1.4, 1.8, pp.46-47; version and SHA-256 in SOURCES.** In characteristic zero, the generation bound is `beta(n,m)<=m*n^4`. Over an infinite field, `R(n,m)` is spanned by `f_T(X)=det(sum X_i tensor T_i)` with square `T_i` of variable size `d`. If `n>=2` and `X` is outside the null cone, every `d>=n-1` admits some `T` with `f_T(X)!=0`; hence the null cone is defined through degree `n(n-1)`.

**HAND (hypothesis check and integer substitution):** our field qualifies; these give full-ring generation through degree `1280` and null-cone defining degree `12`. They apply to the surrounding invariant problem, including matrix degrees `32,36,40`, but make no assertion about multiplicities in `C[R_4]`. Generation degree and null-cone tests do not identify the multiplication image.

**PRIMARY [HK2025](https://arxiv.org/pdf/2312.17224v3), Theorems 1.2-1.3, p.4; version and SHA-256 in SOURCES.** Over `C`, primitive semistandard linked tableaux for a generalized Kronecker quiver index a SAGBI basis of its semi-invariant algebra, with the paper's term order and link convention. Finiteness is established there for dimension vector `(2,2)`; the general theorem allows an infinite basis.

**HAND (hypothesis check):** Theorem 1.2 covers five arrows and `(4,4)` and hence the full ring in the requested degrees. The `(2,2)` finiteness theorem does not cover `(4,4)`. The statements read do not identify a SAGBI basis of the subalgebra generated only in degree four. Restricting a full-ring generating set to those elements is not a result established here. No applicable finite-count or complexity guarantee for `A_k` was found.

### Foulkes maps and determinant orbit closures

**PRIMARY [CIM2015](https://arxiv.org/pdf/1509.03944v1), Theorem 6(a), Remark 7, §§3.1-3.2,4.1; version and SHA-256 in SOURCES.** The paper proves injectivity of `Psi_(5,6): Sym^5(Sym^6 V) -> Sym^6(Sym^5 V)` in its stated stable-dimensional setting. Its `Psi_(a,b)` regroups and symmetrizes tensor factors; the degree-`a` Chow ideal is its kernel. The algorithm computes highest-weight restrictions using an evaluation matrix, with an independently full-rank target evaluation matrix making the test exact. The unpruned tableau tree has `(b!)^a` leaves.

**HAND (hypothesis check):** this is a Chow-map calculation, not the map `Theta_k^+` above. The theorem's `(a,b)=(5,6)` and assumption `dim V>=max(a,b)` are not the requested `GL_5`, quartic, `k=8-10` setting. Neither the theorem nor its complexity discussion licenses substitution of Chow rank for determinant-image rank. Its randomized basis-selection procedure was not run.

**PRIMARY [BI2015](https://arxiv.org/pdf/1511.02927v2), Proposition 3.9 and Corollary 3.29; version and SHA-256 in SOURCES.** For a nonzero polystable complex form `w` and its fundamental invariant `Phi_w`, the boundary of its general-linear orbit is the zero set of `Phi_w` in the closure, and the orbit's coordinate ring is obtained by localizing the closure's ring at `Phi_w`. The corollary states nonnormality of the determinant and permanent orbit closures for size greater than two.

**HAND (hypothesis check):** this includes the full `GL_16` orbit closure of `det_4`. It supplies neither the degree-`k` character of the five-variable substitution image nor a normalization theorem for `D_(4,5)`. In particular, an orbit or normalized-ring count cannot simply be asserted equal to the requested image count at `k=8-10`. No such image algorithm is provided by these statements.

### Algorithms whose polynomial complexity solves another problem

**PRIMARY [DM2020](https://msp.org/ant/2020/14-10/ant-v14-n10-p08-s.pdf), Theorem 1.17, Remark 1.9 and §5A; version and SHA-256 in SOURCES.** For two matrix tuples, left-right `SL_n x SL_n` orbit-closure intersection is decidable in polynomial time; if the closures are disjoint, a separating invariant can be produced in polynomial time. The complexity uses unit-cost field arithmetic over an infinite field of definition, with geometric closures taken over its algebraic closure. Section 5A also states polynomial bit complexity for rational inputs.

**HAND (hypothesis check):** the action on our tuples has precisely `n=4,m=5`. However, its input is a pair of tuples and its output is intersection/separation for their left-right orbits. It does not compute `GL_5` multiplicities of coefficient products in degrees `32,36,40`. Nor is it a membership test for a quartic in the `GL_16` determinant-form orbit closure. No algorithm was run.

**HAND (2a verdict): B.** Applicable full-ring theorems and related exact algorithms were found. The precise remaining gap is the rank/character of `im(Sym^k R_4 -> R_(4k))`, or a certified upper bound that controls this image beyond the recorded source/target comparisons. The literature read supplies no such evaluated bound or faster guaranteed method for the requested window. This verdict does not erase the existing exact READ-level s56 method.

## 2b: first-order boundary limits

**READ — C:`docs/b27_01_report.md` §1a.** The residual question is about actual padding `l*C`, where `C=per_3(A)` for a five-variable linear matrix pencil `A`, with `l!=0`, `C` singular, `C notin D_(3,5)`, and `C` containing no projective plane. Singular cubics already in `D_(3,5)` or containing a plane belong to the recorded certified-in region. Thus “a singular cubic factor” alone does not isolate the open class. No claim below changes the distinction between the closure of literal product determinants and the product locus intersected with the full determinant closure.

**PRIMARY [HL2016](https://arxiv.org/pdf/1512.02437v2), Theorem 1 and Lemma 5, pp.1-3; version and SHA-256 in SOURCES.** In nine variables over `C`, the projective `det_3` boundary has exactly two irreducible components: the orbit closure of the generic traceless determinant, and the orbit closure of

```text
P2 = x4*x1^2 + x5*x2^2 + x6*x3^2
     + x7*x1*x2 + x8*x2*x3 + x9*x1*x3.
```

The second is obtained from a skew-symmetric `3 x 3` pencil `A` and a symmetric pencil `S`: Jacobi's formula gives the first coefficient `tr(adj(A) S)` of `det(A+tS)`, while `det A=0`.

**HAND (scope):** completeness of this two-component classification is **for size three only**. It is not a classification of `det_4`, and does not decide a five-variable quartic with cubic factor outside `D_(3,5)`.

**PRIMARY [LMR](https://math.univ-lyon1.fr/~ressayre/PDFs/lmr.pdf), Proposition 3.5.1 and its preceding definition, pp.9-10; version and SHA-256 in SOURCES.** For odd matrix size `n`, write `M=A+S` into skew-symmetric and symmetric parts. The polarized polynomial `P_Lambda(M)=det_n(A,...,A,S)` gives a boundary component outside the literal endomorphism orbit. The displayed degeneration is `det(A+tS)=n*t*P_Lambda+O(t^2)`. The text explicitly says this polarized expression vanishes for even `n`.

**HAND (scope):** the odd-size hypothesis excludes `n=4`. This excludes using that particular theorem at even size; it does not exclude other first-order quartic limits. Theorem 1.0.3's separate dual-dimension bound assumes an irreducible polynomial, so it cannot be applied directly to a nonzero product `l*C`.

**PRIMARY [H2017](https://d-nb.info/1156010608/34), Corollary 8.3.2 and Proposition 8.4.1, printed pp.96,103-105; version and SHA-256 in SOURCES.** The traceless-determinant orbit closure is a boundary component for every size at least three. For size four the dissertation supplies two further components via first-order approximation paths. One displayed representative is `Q2=tr(adj(M0) M1)`, with

```text
M0 = [ x1  x2   0   0 ]       M1 = [ y1   y2   b1   b2 ]
     [  0   0  x1  x2 ]            [ b3   b4  -y1  -y2 ]
     [ x3   0  x4   0 ]            [ y3   a1   y4   a2 ]
     [  0  x3   0  x4 ]            [ a3  -y3   a4  -y4 ].
```

**PRIMARY H2017:** these are linear matrices in sixteen independent variables; `M0` lies in the singular space `L2`. Component dimensions rely on the source's Program 8.3, which was **not replayed**. Question 8.4.2 asks whether the three displayed component closures exhaust the boundary.

**HAND (scope):** this is an actual size-four construction, but the source does not identify a specialization with all the residual class-(iii) properties. No such specialization is asserted or attempted here.

**PRIMARY [ASS2022](https://arxiv.org/pdf/2201.00135v1), Assumption 3.1 and Theorem 3.13(i), pp.14-15,19; version and SHA-256 in SOURCES.** Given complex forms and an algebraic family `A(t)` of variable changes with normalized expansion `A(t)f=g+t^b f_b+...`, assume the span of the higher terms is transverse to the orbit tangent space at `g`. The theorem constructs a limiting stabilizer subalgebra `K0`, of the generic stabilizer's dimension, inside the stabilizer of the tangent-of-approach class for the induced action.

**HAND (scope):** this is a necessary structural result for a supplied family; the hypotheses include that family and transversality. Neither has been supplied for a class-(iii) point by this source. It is not an existence theorem for `M0,M1` realizing a prescribed singular-cubic padding form.

**HAND (2b verdict): B.** Explicit first-order determinant limits are known, including size four. No theorem read here decides whether any of the residual class-(iii) points is such a limit, or supplies another construction placing a verified member of that class in `D_(4,5)`. This leaves those points **unresolved**, not excluded. Completeness for `det_3`, odd-size skew constructions, and the explicit size-four components have been kept separate.

## 2c: registered outcomes and achievement

| Rung | Verdict and disposition | Achievement |
|---|---|---|
| 2a | **B**: related full-ring, Chow and orbit-ring results; exact image rank remains the gap | PRIMARY/READ literature audit, with HAND hypothesis checks |
| 2b | **B**: known size-three and size-four first-order constructions; no class-(iii) decision found | PRIMARY/READ literature audit, with HAND scope checks |
| 2c | Complete: both verdicts, source inventory, search methods and limitations recorded | No mathematical record change |

**READ (administrative):** zero mathematical runs, no installs, no new mechanism, no subagents, no messages to other tasks, no edits to papers, ledgers, seals, attributes or ignore rules. Scripts only perform PDF reading and byte/provenance checks; the receipt distinguishes those from mathematical computation. [CHECKPOINT.md](../results/b28_02/CHECKPOINT.md) and [RESOURCE_RECEIPT.json](../results/b28_02/RESOURCE_RECEIPT.json) document completion within the slot ceiling.

**HAND (achievement assessment):** no new source condition, coefficient equation, separation on padding, positive multiplicity gap, geometric noncontainment, equation-existence cell, or asymptotic bound is claimed. Historical certificates and source computations were read, not rerun. **READ (standing): “No five-row determinant equation is known to be nonzero on padding.”** **“no construction ready.”**
