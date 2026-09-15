# B17-01: five-variable padding is not contained in the det4 pencil closure

**COMPLETE — proved geometric noncontainment, with an explicit actual-padding
point.** Over the complex numbers, if a cubic `C(x0,...,x4)` defines a smooth
cubic threefold and `l` is any nonzero linear form, then

\[
 lC\notin D_{4,5}:=
 \overline{\{\det(x_0B_0+\cdots+x_4B_4):B_i\in\operatorname{Mat}_4(\mathbb C)\}}.
\]

The proof uses specialization of **ruledness**, including components of a
reducible limit. It applies to the coefficient closure, including limits whose
matrix entries cannot be specialized to finite matrices. A freshly certified
smooth cubic in the actual restricted `per3` image supplies a concrete point.
This is a new deduction in this delivery, not a claim of literature priority.
It does not give an explicit determinant equation module, an equation degree,
or a positive coordinate-multiplicity gap.

## Objects and the density premise

Work in characteristic zero, over `C`, with raw monomial coefficient
functionals. The ambient quartic space is `Sym^4(V*)`, `V=C^5`; its coordinate
ring in degree `d` is `Sym^d(Sym^4 V)`. Coefficient weights are positive.
The corresponding sixteen-variable comparison is always `det4` versus
`p=z*per3` with independent `z` and nine independent matrix entries.

Put

\[
 \Phi(A_0,\ldots,A_4)=\operatorname{per}_3\left(\sum_{k=0}^4x_kA_k\right),
 \qquad R_{1,3,5}=\{lC:l\in V^*,\ C\in\operatorname{Sym}^3V^*\}.
\]

The nonzero projectivized product locus is the image of the projective
multiplication map `P(V*) x P(Sym^3 V*) -> P(Sym^4 V*)`, so its affine cone
`R_{1,3,5}` is closed. If `Phi` is dominant, the closure of the *actual* padded
restriction image is exactly `R_{1,3,5}`: the polynomial map `(l,A)->l*Phi(A)`
has the same image closure as multiplication on all `(l,C)`.

The corrected local [isotypic report](isotypic_rank.md) and
[Session 26 review](s26_review.md) report this dominance. The located exact
certificate is the seeded Jacobian generator
`analysis/wk6_s26_density.py::jacobian_rank`, rather than a saved minor.
Before using dominance, this task reconstructed its `seed=1, spread=7,
trial=0` point, all 1,575 Jacobian entries, and an explicit minor. No old
Downloads copy was used. No legacy raising-operator code was imported; the
old rule still visible in ancillary Session 26 helpers is irrelevant to
this coefficient-derivative calculation.

The differential rows are
`x_k * per(M with row i and column j deleted)`, ordered by `(k,i,j)`;
the 35 columns are cubic exponents in descending lexicographic order. An
independent full six-permutation expansion checks every entry by an exact
unit difference in the corresponding source entry. Such differences equal
derivatives because the permanent is affine in each individual entry.
Rows `0,...,33,36` give determinant

```text
-61071160773612186548546419365012063050944242060048644997120
```

Its residue modulo the prime 65521 is 17609. Exact fraction-free elimination
checks every division, and separate modular elimination checks the residue.
Thus the differential has rank 35 over `Q`, hence over `C`. The characteristic
zero Jacobian criterion proves dominance. This establishes

\[
 D_{\mathrm{pad},5}=R_{1,3,5}.
\]

Only the five-variable image has been replaced by all cubics, after proving
its density. This makes no assertion about generic cubic padding in ten
variables, or about `per4`.

## Proved lemma: reduced limits have ruled components

**Lemma.** If `0 != F in D_{4,5}` is square-free, every irreducible component
of the projective hypersurface `V(F) subset P^4` is ruled over `C`.
Here ruled means birational to `P^1 x T`; it does not mean merely uniruled.

**Proof.** There is a nonempty open set of five-tuples of matrices for which
the determinant hypersurface is integral, normal, and rational. Rationality
has a direct incidence description. For a general pencil `M(x)`, consider

\[
 Z_M=\{([x],[u])\in\mathbb P^4\times\mathbb P^3:M(x)u=0\}.
\]

On the rank-three locus of `M(x)`, the kernel gives a unique `[u]`, so the
first projection is birational to the determinant hypersurface. For general
`[u]`, these are four independent linear equations in five `x` coordinates,
giving a unique `[x]`. The second projection is therefore birational to
`P^3`. Generic irreducibility and normality also follow from a general linear
section of the determinant hypersurface: its matrix-rank-at-most-two locus
has codimension four in matrix space, so the general section has only
isolated possible singularities. These generic facts and the incidence
construction are recorded in [Leal–Lozano Huerta–Vite, introduction and
§1.1](https://arxiv.org/html/2504.14461v1#S1.SS1). We only need this open set,
not a rationality assertion for arbitrary specialized pencils.

To account for all boundary points, take the projective closure of the graph
of the determinant coefficient map
`P((Mat4)^5) -->> P(Sym^4 V*)`. Its projection onto the latter space is proper
and has image `P(D_{4,5})`. Pick a point over `[F]` and an integral curve
through it whose generic point lies over the preceding good open set.
Normalize that curve and localize at a point above `[F]`. This gives a DVR
`R`, essentially of finite type over `C`, with residue field `C` and fraction
field `K`. On the generic fiber the matrix representation and the incidence
birational maps are defined over `K`; no assumption about finite limiting
matrix entries is made.

The coefficient coordinate over this DVR can be represented by a primitive
quartic `F_R`, reducing to a nonzero scalar multiple of `F`. Let
`X=V(F_R) subset P^4_R`. It is projective and flat over `R`. Primitivity and
generic integrality imply that `X` is integral (equivalently, use Gauss's
lemma on affine charts). As a hypersurface in the regular scheme `P^4_R`,
it is Cohen–Macaulay and satisfies `S2`.

We check `R1`, the point at which a careless boundary argument could fail.
At codimension-one points over the generic base point, normality follows
from that of the generic determinant hypersurface. Vertical codimension-one
points are generic points of the components of `V(F)`. Since `F` is reduced
in characteristic zero, each such generic point is a smooth point of the
special hypersurface: precisely one factor vanishes there, to order one.
The corresponding spatial partial derivative of `F_R` is a unit locally,
so the total space is regular there. Thus `X` satisfies `R1` and `S2` and
is normal. The singular intersections of special components have higher
codimension in the total space and cause no gap in this argument.

Now apply the rational-generic-fiber form of Matsusaka's specialization
theorem: in this normal integral projective DVR family, every special
component is ruled. The precise componentwise statement and its proof are
[Kollár's lectures, written by Smith with Rosenberg, Theorem 5.3,
Remark 5.3.1 and Theorem 5.4, printed pp. 34–37](https://arxiv.org/pdf/alg-geom/9707013v1).
In that proof, the normalized graph of a generic rational parametrization
maps birationally to both `X` and `P^3_R`. A special component has a
birational strict transform. It either dominates the special `P^3`, or is
exceptional over the regular `P^3_R`; in the latter case Abhyankar's theorem
makes it ruled. All hypotheses were checked above. This proves the lemma. ∎

The original source is [Matsusaka, *Algebraic Deformations of Polarized
Varieties*, Appendix §1](https://doi.org/10.1017/S0027636000012733).
For the reducible special fiber here, the exact formulation used is the
componentwise theorem in the cited lectures, rather than an inferred
extension of the older smooth-variety formulation.

## Consequence and explicit actual-padding witness

A smooth complex cubic threefold `Y` is unirational but not rational:
[Clemens–Griffiths, Theorem 13.12 and Appendix B](https://publications.ias.edu/sites/default/files/intermediatejacobian.pdf).
It cannot be ruled. Indeed, if `Y` were birational to `P^1 x T`, projection
would make the surface `T` unirational. A complex unirational surface is
rational by Castelnuovo; see [Colliot-Thélène–Karpenko–Merkurjev,
Theorem 2.3](https://arxiv.org/pdf/math/0611777v1). Then `Y` would itself be
rational, a contradiction. This uses neither a stable-rationality assertion
nor an asymptotic complexity theorem.

For a smooth cubic `C` and nonzero `l`, the quartic `lC` is reduced and has
the nonruled component `V(C)`. The lemma proves `lC notin D_{4,5}`. No
transversality condition on the hyperplane `l=0` is needed.

For an explicit actual cubic, use the same five matrices as the density
certificate:

```text
A0 = [[-5, 2, 6], [ 5, 5,-6], [-3,-6, 0]]
A1 = [[ 5, 0, 0], [ 3,-1, 5], [-4,-6, 0]]
A2 = [[-7, 7, 6], [-1,-1, 2], [ 5, 5,-7]]
A3 = [[ 4, 0,-3], [ 4, 5,-4], [ 2,-6, 7]]
A4 = [[-2,-7,-7], [-7, 3, 1], [-7, 7,-1]]
C* = per3(x0*A0 + x1*A1 + x2*A2 + x3*A3 + x4*A4)
F* = x0*C*
```

All nine matrix-entry linear forms are nonzero and all six permanent
summands are included. This is not a zero-entry matrix family.
The certificate forms the 350 by 210 integer matrix whose rows are
`x^beta * partial_i(C*)`, `|beta|=4`, in the basis of degree-six monomials.
Its recorded 210-square minor has residue **61614 modulo 65521**. Thus all
degree-six monomials lie in the gradient ideal over `Q`, hence over `C`.
The partial derivatives have no common projective zero, proving smoothness.
No sampled smoothness test or numerical root finding enters this conclusion.

The `9 x 5` matrix with columns `vec(Ak)` has a `5 x 5` minor **2562** in
its first five rows. Hence these five source directions are independent.
Adding the `z` row `(1,0,0,0,0)` gives an injective map into the ten original
source coordinates; embedding in sixteen coordinates and completing this
frame yields an invertible ambient change of variables whose restriction
to the chosen five-plane is exactly `F*`. Consequently the point genuinely
tests restrictions of the original independent `z*per3` orbit.

The resulting concrete conclusion is

\[
 F_*\in\{\text{actual five-variable restrictions of }GL_{16}\cdot p\}
 \setminus D_{4,5},\qquad D_{\mathrm{pad},5}\nsubseteq D_{4,5}.
\]

## Representation meaning, missing quantitative step, and next test

Restriction of coefficient polynomials is compatible with the orbit
closures. A weight with trailing zeros only involves coefficients supported
in the first five variables, since all coefficient weights are nonnegative.
Thus the geometric result implies that some homogeneous determinant
equation of a Schur type of length at most five survives on actual padding.
This is an existence statement: no degree, partition, highest-weight vector,
or dimension of its restriction image has been extracted here. Conditional
on Slot03's independently reviewed four-row exclusion, such a surviving
type must have exactly five rows. The main lemma and concrete witness do
not depend on that review.

In one finite cell the required multiplicity difference remains
`D=m_pad-m_det=i_det-i_pad`. Noncontainment of kernels does not order their
dimensions. None of the integers 35, 210, or 2562 is a coordinate-ring
multiplicity. The source of `(l,C)->lC` still only gives a ceiling until its
actual image is computed. The six excluded Batch16 cells and the failed
degree-seven symmetry certificate remain excluded in their stated scopes.

**One next sufficient test.** For one proposed finite cell `(d,lambda)` with
at most five rows, give a global determinant coordinate upper bound `B` and
`B+1` highest-weight coefficient polynomials whose evaluations on actual
five-variable restrictions of `z*per3` have a nonzero square minor. This
would prove `m_pad >= B+1 > B >= m_det`. The missing quantitative lemma is
the construction of such a labeled finite cell and functions; the ruledness
proof supplies neither `B` nor a degree bound. In particular, merely finding
one equation nonzero at `F*` would yield an explicit separator, but would
not by itself pass this multiplicity test. No census, elimination job, or
larger lease is proposed without those inputs and a priced support bound.

## Provenance, resources, and limits

Read-only intake followed `Batch16/INTAKE.json` to the original B16-01 report,
proof, manifest and input ledger, and through those to
`Batch15_Launch/native_20260913/reviews_filesystem/Dream_Upper288/DREAM_REPORT.md`
and its `integrator_review.json`. Those accepted bounds and the other
stocktake numbers are context only; this proof does not require their
numerical reexecution. Twenty local inputs, including the corrected
density sources, interpreter and inspected wrapper, were hashed before the
sole run and checked inside it.

Fresh here: the saved density minor and complete two-route Jacobian check;
the explicit smoothness and frame certificates; the application of ruledness
specialization to the full five-pencil coefficient closure; and the actual
padding noncontainment deduction. Inherited literature: generic determinant
rationality, specialization of ruledness, cubic-threefold irrationality and
unirationality, and Castelnuovo's surface theorem. There has been no external
independent review of this B17 proof or a second computational run.

The only research execution used `.venv/python.exe -B` with the inspected
`analysis/b15_bound.py`, `--seconds 60 --memory-mb 512`, one process and one
configured BLAS thread. Its timer is an enforcement thread, not a numerical
worker. It passed in **0.2731305 seconds** with **13,733,888 bytes** peak Job
Object committed memory; exit 0. No heavy lease was issued or used. The
preflight price was 20 seconds and 96 MiB; those estimates were not treated
as enforcement bounds. The wrapper's inherited B15 session label is metadata
only. The recorded process exited; no background calculation remains.

The source and exact certificate are
[analysis/b17_01_verify.py](../analysis/b17_01_verify.py) and
[results/b17_01/certificate.json](../results/b17_01/certificate.json).
Reproduction, if separately authorized, is the same single bounded command:

```powershell
& '.\.venv\python.exe' -B analysis/b15_bound.py --seconds 60 --memory-mb 512 --name b17_01_pilot --slot 01 analysis/b17_01_verify.py
```

The reconstructed certificate data are compared exactly on replay; the saved
certificate is not silently replaced. The executable uses exact integer and modular
arithmetic and imports no historical research module.

Primary theorem statements were read through the browser. Attempts to archive
four original source files with `Invoke-WebRequest` failed because local
socket access was forbidden. Each exact action and reason is preserved in
[literature_sources.json](../results/b17_01/literature_sources.json). No
permission bypass, configuration change, or escalated retry was attempted.
The source URLs, versions and checked theorem locations are recorded in
the separately hashed source notes; original remote PDF/HTML bytes are **not**
claimed hash-pinned. Local input and output hashes and all resource receipts
are inventoried in [delivery/b17_01/MANIFEST.json](../delivery/b17_01/MANIFEST.json).

Writes are confined to the assigned `analysis/b17_01*`, `docs/b17_01*`,
`results/b17_01/`, `delivery/b17_01/`, and `results/logs/b17_01*` paths.
No agents, tasks, worktrees, commits, push, publication, ownership/trust
changes, closed-output edits, or common coordination edits were made.
This is a completed bounded contribution. No nonreduced-limit theorem,
explicit equation module, positive multiplicity gap, or improved LMR
determinant-size growth is claimed.
