# B27-01 — a map of actual padding, a smooth witness, and its degree window

**Outcome:** all three rungs answered. **READ + HAND + COMPUTED:** the certified-in region has dimension at least 45 in the 50 substitution parameters; the smooth certified-out region is open dense of dimension 50; the remaining singular boundary has dimension 49. The last region is excluded from the *literal* determinant image by the committed classification, but its membership in the determinant **closure** remains unresolved. This is the precise remaining obstruction, not a claim of noncontainment for every singular cubic.

**READ + COMPUTED:** `T*` below is the committed B17-01 witness, independently replayed here over the integers and modulo 65521. This slot does not claim to have discovered that witness. **HAND using accepted C1:** `F*=l*per_3(A*)` is outside `D_{4,5}`. The achieved positive level is **geometric noncontainment at an explicit actual-padding point**. No coefficient equation, equation nonzero on padding, positive multiplicity gap, or asymptotic bound is produced.

**READ, governing wording:** “No five-row determinant equation is known to be nonzero on padding.” A25-10's decision, “no construction ready,” stands.

## 0. Preflight, bytes, and conventions

**READ / administrative:** branch `b27-01`, worktree `work/batch27/b27-01`, and initial HEAD `6dea55ec926c1618cc60ad71209795528705bf61` agree exactly with PART 25's setup receipt. Initial tracked and untracked status was clean. The report, result directory, and analysis glob were absent. No applicable `AGENTS.md` was found. The sandbox's different Windows account required a **per-command** `safe.directory` option for this worktree; no Git configuration was changed. All output writes are in this slot's allowed paths.

**READ / administrative raw SHA-256:**

| Launch file | SHA-256 of raw file bytes |
|---|---|
| `B27_COMMON.md` | `891e3ca872bc795b6f943ac89f55112573803f006e0208940dd6cad1f750d6ee` |
| `B27-01.md` | `ce5a7910fbc913fffd52924f1c98707d3970392fe979259bfb9e2931baf18b8b` |
| `BATCH27_BOARD.md` | `b0bc2501aba62d49b91862d821232ac1b9904480057a8dcdb4cbc03fbd86efec` |

**READ:** mathematical inputs are committed blobs, obtained with `git show`, not working copies or tool memory. [INPUT_BINDINGS.json](../results/b27_01/INPUT_BINDINGS.json) records each full commit, path, Git blob ID, raw payload SHA-256, byte count, snapshot, and actual read extent. These SHA-256 hashes name the **blob payload**, without Git's object header. The launch hashes above name administrative filesystem bytes. Output hashes name raw output bytes; the manifest excludes itself. Full-source snapshots do not imply that unread sections were audited.

**HAND definitions:** work over `C`. Write `E=Hom(C^5,C^10)=C^50`, with rows of `T` ordered as `(l,A11,A12,A13,A21,A22,A23,A31,A32,A33)`. Put `C_T=per_3(A(x))` and `F_T=l C_T`. All coefficients are ordinary monomial coefficients. Let `D35` be the closed five-variable cubic determinant locus and `D45=D_{4,5}` the closed quartic determinant locus. Let `Sigma_Pi` be the closed locus of cubics containing a projective plane, including zero, and set

`K = D35 union Sigma_Pi`.

**HAND convention:** the zero cubic is in the singular-cubic locus. Dimensions below are dimensions of algebraic/constructible subsets of **the affine 50-dimensional parameter space E**, not dimensions of their coefficient images and not projective dimensions. The same stated bounds hold after restricting to rank-five substitution matrices: the displayed witnesses and dense portions of the lower-bound families have rank five.

## 1a. The map

**READ:** B23-03 Theorem 2.1 and §§2.4–2.6 at `3bcad666`, affirmed on reading by B23-10 §3.4 at `239dd6e8`, establish

`closure({literal 4x4 determinants that are products lC}) = {lC : C in K} subset D45`.

This is a classification of the closure of the **literal product-determinant intersection**. It does not identify `D45 intersect {lC}`. **READ:** the B27 acceptance of C1 additionally excludes every `lC` with nonzero `l` and smooth `C`, including coefficient limits with no finite matrix specialization. Historical source statements leaving that smooth case open are superseded at precisely that scope.

**HAND using those READ certificates:** the following conditions are mutually exclusive and exhaust E.

| Class | Defining condition on T | Certificate and status | Parameter dimension |
|---|---|---|---|
| (i) certified in | `l=0`, or `C_T in K` | **READ:** zero determinant; block lift for `D35`; B23-03 compression-family closure for `Sigma_Pi`. Hence `F_T in D45`, literally when a finite pencil is supplied, otherwise in closure. | **HAND:** `45 <= dim(i) <= 49`; a 45-dimensional nonzero literal subfamily is given below. |
| (ii) certified out | `l != 0` and `C_T` smooth in `P^4` | **READ:** accepted smooth-cubic C1. **COMPUTED:** the replayed witness makes this nonempty. | **HAND:** open dense, dimension **50**. |
| (iii) unresolved boundary | `l != 0`, `C_T` singular, and `C_T notin K` | **READ + HAND:** no literal determinant representation can exist, by B23-03's direct-point classification. Membership in the coefficient closure is not decided by that classification or by C1. | **HAND + COMPUTED:** dimension **49**, with the tangent-section certificate below. |

**HAND scope:** “unknown” in class (iii) means that the committed containment and exclusion results used here do not decide its closure membership. It does not assert that every such point has the same answer, or that all possible future certificates fail. This map gives an explicit algebraic residual set and its size. Its exact unresolved question is whether any of its points lies in `D45 \ {literal determinants}`. No equality of intersection and closure-of-intersection is assumed.

### Concrete conditions that put T in class (i)

**READ, A26-01 at `7464a2bd`, PROOF §§1–3:** if `A` is symmetric, with rows `(a,d,e;d,b,f;e,f,c)`, then for `u^2=2`,

```text
M_u = [ a   d          e
       -d   b      (u-1)f
       -e -(u+1)f      c ],       det diag(l,M_u) = l per_3(A).
```

**HAND:** the symmetric parameter subspace has dimension `5+6*5=35`. The certificate holds for all its degenerations and all variable changes. The stronger map above also recognizes nonsymmetric presentations of the same cubic or quartic. Symmetry of the displayed matrix is sufficient, not necessary, for membership.

**HAND, a 45-dimensional literal subfamily:** impose only `A33=0`. For arbitrary eight linear forms,

```text
per [ a b c ]       det [ -a  b c ]
    [ d e f ]   =       [  d -e f ]   = afh+bfg+cdh+ceg.
    [ g h 0 ]           [  g  h 0 ]
```

Multiplication by `l` gives a block-diagonal 4x4 determinant. There are `8*5+5=45` independent parameters, and nonzero products form a nonempty open subset. Permuting rows and columns gives the corresponding certificate for any zero entry. The simpler `l=0` subspace also has dimension 45. These are parameter counts, not image-dimension claims.

**READ + HAND:** if `C_T` is reducible, then it has a linear factor `w`, so it contains a hyperplane and hence a plane. It is in `Sigma_Pi`, and `F_T` is in class (i). In particular the B26 expander padding point `p4=zw(zw+uv+t^2)` is **in D45 in closure**. B26-02's classification “neither” means neither smooth nor a literal symmetric permanent; it was not a nonmembership theorem for D45. An independent explicit Laurent-pencil limit for this very point appears in [MAP_AND_BOUNDARY_PROOF.md](../results/b27_01/MAP_AND_BOUNDARY_PROOF.md).

**READ + HAND:** the nonsingular-quadratic squares `Q^2` and `(A+B/2)^2` used in B26-02/A26-03 are determinant control points. They have no linear factor and are not nonzero actual-padding points; their inverse images under `T -> l per_3(A)` are empty. Their agreement with particular tableau evaluations does not put a padding point into D by equality of forms. The independent closure certificate just given is what places `p4` in class (i).

### The 49-dimensional unresolved part

**COMPUTED:** [TANGENT_CERTIFICATE.json](../results/b27_01/TANGENT_CERTIFICATE.json) supplies a rational `A^dagger` such that `C^dagger=per_3(A^dagger)` has exactly one projective singular point, `[1:0:0:0:0]`, with nondegenerate affine Hessian. Its degree-six Jacobian-ideal matrix has exact rank 209 of 210, and the full 45-parameter permanent coefficient differential has exact rank 35 of 35. The 209-square minor has residue **54422 modulo 65521**; the parameter minor has residue **5949**. Both determinants were also evaluated as integers with every Bareiss division checked. The Hessian determinant is **-863583313736999047506762240**.

**HAND, detailed proof in the linked file:** the one-node cubic is irreducible, is outside `D35`, and contains no plane. The discriminant is smooth at a cubic with exactly one ordinary node. The rank-35 coefficient differential makes its pullback locally a hypersurface of dimension 44 in the 45 matrix-entry parameters. The nonzero padding row adds five dimensions. Removing the closed set `K` leaves a nonempty open portion of that hypersurface. Thus class (iii) has dimension at least 49; its inclusion in the proper singular-cubic pullback gives the matching upper bound. This is a dimension certificate for an unresolved region, **not** geometric noncontainment of its quartics from D45.

**COMPUTED, retained negative:** the first fixed boundary example, with `A33=0`, gave degree-six modular rank **203**, not 209. It did not certify a unique singular point. Its input, output, script and receipt are retained. **HAND:** the zero-entry identity above explains why that example belongs to the certified-in family. No random search was used; the subsequent fixed tangent construction checks a different, explicitly specified candidate and its complete finite certificates.

## 1b. Smooth permanental cubics and T*

**READ:** this is the explicit B17-01 point at `01c49022c2a222254884c8c96611dd0e9f302892`. **COMPUTED:** the new verifier reconstructs its cubic by all six permanent summands and checks every stored coefficient. The rows below multiply `(x0,x1,x2,x3,x4)^T`:

```text
T* = [  1  0  0  0  0       l
       -5  5 -7  4 -2       A11
        2  0  7  0 -7       A12
        6  0  6 -3 -7       A13
        5  3 -1  4 -7       A21
        5 -1 -1  5  3       A22
       -6  5  2 -4  1       A23
       -3 -4  5  2 -7       A31
       -6 -6  5 -6  7       A32
        0  0 -7  7 -1 ]     A33
```

**COMPUTED:** let `J=(partial_0 C*,...,partial_4 C*)`. Form the 350-by-210 integer matrix with rows `x^beta partial_i C*`, `|beta|=4`, and columns all degree-six monomials, using descending lexicographic exponent order. Replay the **fixed 210 row indices** in the committed certificate; no row-set search is used in this replay. Its integer determinant is nonzero (569 decimal digits), and its residue is **61614 modulo 65521**, agreeing with B17. The complete integer and row-index certificate is in [SMOOTHNESS_CERTIFICATE.json](../results/b27_01/SMOOTHNESS_CERTIFICATE.json).

**HAND from that finite certificate:** the matrix spans `S_6` over Q and over `F_65521`, so every degree-six monomial lies in J in both fields. A nonzero common projective zero of the partials would make some `x_i^6` both zero and nonzero. Thus the cubic is geometrically smooth over Q (hence C), and also over the algebraic closure of `F_65521`. This is an exact Jacobian-ideal spanning certificate, not a sampled smoothness test and not a claim to have run a Gröbner basis.

**COMPUTED + HAND:** the first five rows of the 9-by-5 matrix of matrix-entry forms have determinant **2562**. Hence `T*` has rank five and is an actual injective substitution of the ten independent source coordinates. With `l=x0 != 0`, accepted C1 gives `F* notin D45`. Its quartic is reducible and singular; it is the **cubic factor**, not the quartic, that is smooth.

**HAND:** the nonvanishing of the same 210-square Jacobian-ideal minor is a nonempty Zariski-open condition on the 45 entries of A. Consequently a general five-variable permanental cubic is smooth. Multiplying by an arbitrary nonzero padding row gives the open dense 50-dimensional class (ii). Neither dominance onto all cubics nor equality of padding with the full product locus is needed for this conclusion.

## 1c. The degree window at this fixed point

**HAND definition:** `d(T*)=min{d : some homogeneous h in I(D45)_d has h(F*) != 0}`. This is a coefficient degree. It differs from the first degree containing any determinant equation, from the internal Macaulay grading, and from the degree four of F*.

| Committed fact | What it says at T* | What it does not say |
|---|---|---|
| **READ:** B19-02 §8.1; Paper 3 C08: `I(D45)_d=0` for `d<=5`, on the record's 03-A and LLV premises | **HAND:** `d(T*)>=6`. The historical evaluations are READ, not replayed here. | It gives no explicit h in degree 6. |
| **READ:** B18-01 §§3.3–3.6, F2 lineage: point separation in degree at most `deg P(D45)<=4^49`, **conditional on refined Bézout** | **HAND:** applies to this exact F*, not merely to some unspecified padding point. Thus **`6 <= d(T*) <= 4^49`**, with the upper-bound dependency retained. | No equation, partition, practical search bound, or multiplicity gap is supplied. Without that dependency, finite existence remains but no numerical upper bound is claimed here. |
| **READ:** cubic-factor restriction, B23-03 §2.5 / Paper 3 C34 | **HAND:** `g(C)=h(x0 C)` is a nonzero degree-d element of `I(K)`, hence `d(T*)>=onset I(K)>=onset I(D35)`. | A cubic equation does not automatically lift to a quartic equation. |
| **READ:** the corrected cubic-onset record, Paper 2 introduction and Paper 3 C12 | Cubic onset is at least 6 in the unconditional record, and at least **8 given the batch-13 measured total-deficit identity**. With that additional adopted premise the displayed separator window sharpens to **`[8,4^49]`**. | The old cap note's bare `[8,300]` headline is not an unconditional fixed-point separator bracket. No measured premise is silently promoted. |
| **READ:** cap theorem, n=3, and plane-cubic Proposition 2.5 | Some degree-65 **cubic-side** minor is nonzero at C*, while all such minors vanish on K. This is conditional on the cap's named adopted inputs for the D35 half. | **65 is not an upper bound on d(T*)**. A global quartic lift is absent. |
| **READ:** cap theorem, n=4 | Gives nonzero determinant equations of coefficient degree **300**, the size-300 minors of the quartic `M_7`. It bounds the onset of the determinant ideal, subject to its named Kleiman/Dimca/Gulliksen–Negard premises. | It does **not** bound the first equation nonzero at F* above by 300. The displayed cap equations all vanish at F*. |
| **READ:** A25-02 Application 3 and A25-10 audit | Quartic `rank M_7(F*)<=245` is **proved**. The determinant floor 299 retains **CERTIFIED-modular** status. Every 299-minor and its entire polynomial ideal vanish at F*. | 245 and 299 are ranks/minor sizes, not bounds on d(T*). A 299-minor is not automatically a determinant equation. |

**HAND:** for the 245 ceiling, `J_{lC} subset (l,C)`. At degree seven, `dim S_7=330`; modulo l, degree-seven forms in four variables have dimension 120 and the degree-three C can remove at most 35 dimensions. Thus `dim(S/(l,C))_7>=85`, giving rank at most `330-85=245`. This proof applies in particular to F* and requires no replay of the historical determinant floor. It also kills all size-300 minors.

**READ + HAND:** the cap conjecture supplies no unconditional lower bound 300 or strictly greater than 300 for this separator. The length-nine LMR transfer is in a different regime and supplies no equation nonzero at T*. The B26 paired-tableau theorem is a rejection certificate, not a numerical lower bound on arbitrary equations. C45 remains the unpadded degree-12 control under the current standing convention. None of these changes the fixed-point window above.

## Completion and limits

**READ / administrative:** three sequential mathematical runs, all below 60 seconds and 512 MB; about **10.876 seconds total**, maximum measured Job Object memory **21,884,928 bytes**. Scripts, fixed inputs, complete outputs and per-run hashes are retained. Only installed Python standard-library arithmetic was used; `python` was absent from PATH and the bundled interpreter had no SymPy, so no package was installed. The exact computations are labelled **COMPUTED**, not PROVED. The mathematical implications and dimension arguments are separately labelled HAND.

**HAND / registered outcomes:** 1a is a certified three-way map with an exact unresolved closure obstruction; 1b is a positive smoothness certificate and explicit geometric noncontainment; 1c is committed-record degree bookkeeping, with the relevant dependencies and inapplicable bounds separated. The 45-minute checkpoint was not reached; [CHECKPOINT.md](../results/b27_01/CHECKPOINT.md) records an early checkpoint. Mathematical work stopped when all three rungs were answered. No equation search, subagent, other session, task message, installation, paper edit, shared ledger/seal edit, publication, or automatic continuation occurred. Commit and push are to this slot's branch only, as authorized by B27_COMMON.
