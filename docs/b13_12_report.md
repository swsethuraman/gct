---
board_numbering: batch13
session_id: B13-12
model: gpt-6-astra
reasoning_effort: xhigh
base: 00495110c62acfbbbc951e82cc218ed091563b3f
branch: b13-12
bundle_parts: 1
---

# B13-12: a global five-variable closure formulation and a universal rank-one support

**PROVED / CERTIFIED.** Delivery has **one part, part00**, a byte-identical copy
of the whole bundle. This session repairs the global formulation, completes two
nontrivial exact controls, and supplies the remaining rational elimination job.
The principal new result is that a **nonzero projective rank-one base support
already has the entire determinant image closure as its graph image**. Thus
removing the affine zero pencil does not make the remaining exceptional-image
bounds independently easier. Global `R5` versus `D5` containment remains open.

**RECORDED.** The actual session model was **GPT-6 Astra, `gpt-6-astra`**, with
`xhigh` reasoning; the automation configuration confirms this designation. No
finer serving-build identifier is exposed. Work used only the prepared isolated
checkout on `b13-12`. Its initial HEAD was the specified frozen base. `main` is
absent in this checkout; no fresh clone, remote operation, shared-source edit,
global Git configuration change, delegation, or follow-up schedule was needed.
History was not rewritten.

## 1. Outcome and claim ledger

| Claim | Status and evidence |
|---|---|
| s78's 69 monic coefficient polynomials are correct | **CERTIFIED**: exact equality of every polynomial with an independent construction; all exponents accounted for |
| `W subset D5` is equivalent to dominance of s78's restricted actual map `G` | **NOT ESTABLISHED**: s78's argument uses an unjustified closure-to-actual-image step; dominance remains sufficient |
| Eliminate the full monic graph, then impose `W` | **PROVED**: exact global reduction, 133 variables and 69 graph equations |
| Full projective graph over the specific rank-one support `Y ~= P3` maps onto `P(D5)` | **PROVED**, section 4; generic 64-parameter polynomial arc identity **CERTIFIED** over Z |
| Simultaneously triangularizable monic-family image is closed; its fixed-factor chart dimension is 12 | **PROVED** by a finite-map argument; 70 coefficient identities **CERTIFIED** |
| S2 rank cases `9,0,3,9`, tangent quotient zero, and explicit rank-three arc | **CERTIFIED replay** over Q and both house primes, using the inherited verifier with isolated outputs |
| Full image ideal, radical/primary decomposition, global dimension bound, or `R5 not subset D5` | **NOT COMPUTED / OPEN** |

**RECORDED.** All planned computations finished under their launch bounds. The
board's formulation-plus-control success criterion is met; the global
elimination is supplied as an exact, uncompleted handoff, not a claimed theorem.

## 2. Setup and the exact correction to s78

**Definition.** Work over C geometrically, with all equations over Q. Write

```
M(s,v) = s1 A1 + s2 A2 + s3 A3 + s4 A4 + v A5,
Phi : A^80 -> Sym^4 C^5,  A |-> det M,
D5 = closure(image Phi),       W = v Sym^3 C^5.
```

Coefficients are ordinary monomial coefficients, without factorials. There are
70 quartic coefficients. `W` is a 35-dimensional affine linear subspace;
`P(W)` has dimension 34. This is a coefficient-image problem, not a
highest-weight-vector or multiplicity-matrix computation. Its ambient GL5
representation is `Sym^4 C^5` in the repository's form convention; coordinate
functions use the dual convention. `R5` is the union of the GL5-translates of
`W`. Since `D5` is GL5-stable, `W subset D5 iff R5 subset D5`.

**PROVED.** On the target chart whose `v^4` coefficient is nonzero, actual
representations have `A5` invertible. Left multiplication by `A5^-1` gives

```
det(v I4 + sum s_i B_i) = v^4 + v^3 P1(B;s) + v^2 P2(B;s)
                        + v P3(B;s) + P4(B;s),
B_i = A5^-1 A_i.
```

Here `Pj` is homogeneous of degree j in both s and B. The nonanchor coefficient
counts are `4,10,20,35`. The 34 good coordinates come from `P1,P2,P3`; the 35
bad coordinates come from `P4`. The anchor is identically one.

Let `H:A^64 -> A^69` be this **full** monic coefficient map and `Z=closure(im H)`.
The monic chart of `P(D5)` equals `Z`: intersecting a dense image with an open
target chart gives a dense subset of that chart, and all actual points there
have the displayed normalization. This argument asserts density, not actual
representability of every point of the closure.

**Correction.** s78's `S=V(P4)` and `G=H_good|S` describe actual monic
representations in `W`. They imply

```
closure(G(S)) subset Z intersect {y_bad=0}.
```

Equality is an additional statement. Irreducibility of `W` does not prove it.
In particular, `G` dominant implies containment, but failure of dominance does
not by itself prove noncontainment. The reviewed s78 reduction from 149 to 98
variables remains valid for the restricted actual-image problem; the claimed
global equivalence and dismissal of the boundary do not follow.

**CERTIFIED control, with a structural proof.** For `(a,b) -> (u=a,v=a*b)`, the
full image is dense in A2: the pullbacks of monomials `u^i v^j` have distinct
exponents `(i+j,j)` for every pair of nonnegative integers. Its closure meets
`u=0` in the whole v-axis, whereas the actual image with `u=0` is the origin.
The exact saturation control `(x(x-z)):x^infinity=(x-z)` similarly retains
`(x,z)=(0,0)` after `z=0`; imposing `z=0` first gives `(x^2):x^infinity=(1)`.
Certificates and finite auxiliary checks are in `small_exact_controls.json`.
These controls refute the inference, not the unproved equality for s78's
particular map.

## 3. A valid global reduction retaining all limits

**PROVED.** Put `A=Q[y1,...,y69]`, let `p_i(B)` be all nonanchor coefficients,
and define

```
L = (y_i - p_i(B) : 1 <= i <= 69) in Q[B_1,...,B_64,y_1,...,y_69],
K = L intersect A = ker(A -> Q[B], y_i |-> p_i(B)),
J_W = (K + (y_bad))/(y_bad) in Q[y_good].
```

Then `V(K)=Z` and `V(J_W)=Z intersect A^34`. Consequently

```
W subset D5     iff J_W = (0),
W not subset D5 iff J_W != (0).
```

Indeed a nonzero rational polynomial cannot vanish identically on A34 over C;
conversely, if every restricted element of K is zero, the whole chart lies in
`D5`, and its closure is `P(W)`. No radical computation is needed for this
zero-versus-nonzero decision. For these specific inputs `J_W` cannot be the unit
ideal: `B=0` gives the known point `v^4`. A unit output would contradict that
control. Containment over C is correctly tested over Q here, since these ideals
and polynomial identities are defined over Q and field extension is faithful.

**RECORDED exact job.** `results/b13_12/cas/full_monic_Q.sing` gives all
polynomials, the source-before-target elimination order and the final target
restriction. There are **133 variables, 69 generators, 7,957 displayed graph
terms**, and maximal ordinary degree four. The smaller 98-variable job is not
substituted for this one. A global dimension proof must show
`dim V(J_W) <= 33` in the monic chart; the resulting proper closed intersection
has affine dimension at most 34 in all of W.

**PROVED proper compactification.** Compactify normalized tuples to
`[z:N1:...:N4] in P64`. The rational coefficient map is

```
[z:N] |-> [z^4, z^3 P1(N), z^2 P2(N), z P3(N), P4(N)].
```

On the finite target chart its graph closure has source-chart ideal

```
H_h = (z^deg(p_i) y_i - p_i(N) : 1<=i<=69) : z^infinity,
       on N_h=1.
```

Saturate first. Only afterwards impose `y_bad=0`, or `z=0` to inspect infinity.
This graph is closed in `P64 x A69`, hence its target projection is proper,
and its image is Z. On `z=0` the displayed equations imply **all 69**
`p_i(N)=0`, not merely the 35 determinant equations: every member of the
four-matrix pencil is nilpotent. These are necessary support equations; they
are not a substitute for the saturated graph's scheme structure.

`infinity_b3_Q.sing` supplies a 134-variable saturation job on the chart
`N1(0,3)=1`; `nilpotent_support_Q.sing` supplies all 69 necessary equations.
The one chart alone is not asserted to cover the full graph. All 64 `N_h`
charts plus `z=1` do. The full contraction K avoids this chart bookkeeping.

**ADOPTED foundations, specialized above.** The projective graph is the blowup
of the coefficient ideal, with affine charts given by the corresponding Rees
algebras. Closed source subsets have closed target images under the proper
graph projection. The general facts were checked in the primary
[Stacks Project blowup reference](https://stacks.math.columbia.edu/tag/01OF),
[blowup-algebra reference](https://stacks.math.columbia.edu/tag/052P), and
[proper-morphism reference](https://stacks.math.columbia.edu/tag/01W0).
The specializations and image equalities here have the explicit proofs above
and below; no bounded-rank classification is assumed.

## 4. New theorem: a nonzero rank-one singular support is already universal

**PROVED.** This holds in the **original** projective source, not only in the
normalized compactification. Let

```
Gamma = closure(graph(P79 --[det]--> P69)),
q : Gamma -> P69,
Y = {A5=0, A_i=a_i E14 (1<=i<=4)} ~= P3 in P79.
```

Then

```
q(Gamma restricted over Y) = P(D5).
```

All points of Y are nonzero rank-one pencils. They lie in the scheme-singular
base locus: every 3 by 3 cofactor is zero, so all differentials of the 70
determinant coefficients vanish there. The base scheme is a proper subscheme
of P79; its tangent space there is the full ambient tangent space, so it cannot
be regular at those points.

**Proof of universality.** Take an arbitrary constant tuple `C1,...,C4` in the
dense open set where `(C1(1,4),...,C4(1,4))` is nonzero, with matrix coordinates
in this paragraph one-based. Set

```
w=(-1,0,0,1),  g(t)=diag(t^-1,1,1,t),  z(t)=t^2,
N_i(t)=t^2 g(t) C_i g(t)^-1,
A_i(t)=N_i(t) (i<=4),   A5(t)=t^2 I4.
```

The entry exponents `2+w_row-w_column` form the matrix

```
2 1 1 0
3 2 2 1
3 2 2 1
4 3 3 2
```

so this is a polynomial source arc with a nonzero projective limit, and
`N_i(0)=C_i(1,4)E14`, `A5(0)=0`. Over Q[t,t^-1] conjugation gives the identity

```
det(v A5(t) + sum s_i A_i(t))
       = t^8 det(v I4 + sum s_i C_i).
```

Both sides are polynomials, so this is an identity over
`Z[t,s1,...,s4,v,C_entries]`. The right-hand monic determinant is nonzero
(its `v^4` coefficient is one). For every `t != 0` the projective target is
constant, and the source specializes to Y. Thus the graph over Y contains
every target `H(C)` from that dense open set of tuples.

The graph over Y is closed in `P79 x P69`. Its projection is closed, contains
a dense subset of `P(D5)`, and is contained in `P(D5)`. Equality follows.
The same argument gives the equality with Z in the normalized compactification
over its corresponding rank-one support. This proof includes closure-only
targets by proper closedness; it never asserts they have actual monic
representations. QED.

**CERTIFIED symbolic control.** Every monomial in every coefficient `Pj` was
checked to acquire exactly exponent `2j` under the entry substitution. An
independent permutation/diagonal-subset calculation checks that every full
determinant term acquires exponent eight. No coefficient or monomial is
silently omitted. Four integral C-tuples, recorded in full, additionally check
all coefficients at `t=1,2,3` and their square-zero rank-one limits. The generic
identity proves the result over Q and both house primes directly; there is no
modular reconstruction or sampled upper bound.

**Consequence.** Intersecting the target with `P(W)` yields exactly
`P(D5) intersect P(W)` again. At least one irreducible component of the graph
over Y dominates `P(D5)` (there are finitely many components). This is not a
claim that Y itself is a base component, or that this component is an entire
exceptional divisor. It is enough to show that a bound for **every** singular
support must cover a piece whose image is already the original problem.

These arcs are changes of basis with constant target; they have first nonzero
determinant order **eight**, despite nonzero rank-one source limits. The
exceptional image of a parameter-space blowup must therefore not be identified
with the target's closure-minus-actual-image boundary. The old wording of that
identification in `critic_rees_response.md` is not adopted.

## 5. A completed nontrivial family: simultaneous triangularization

**PROVED and CERTIFIED.** For upper triangular `B_i`, let `L_a(s)` be their
four diagonal linear forms. Then

```
det(v I4 + B(s)) = product_(a=1)^4 (v+L_a(s)).
```

The exact 70 coefficient comparisons reduce the general coefficient family to
625 terms. Setting one entire `L_a` to zero leaves 125 terms, all divisible by
v. This is an identity over Z, verified independently by expanding the four
linear factors.

The diagonal parameter space is A16. Its map to A69 is **finite onto its
image**: each of the 16 diagonal coefficients is a root of the monic
characteristic polynomial of the corresponding `B_i`. Its four coefficients
are among the image coordinates (with alternating signs for `det(TI-B_i)`).
Thus Q[diagonal entries] is integral, and finite, over the image subalgebra.
The image is closed and has dimension 16. It is also precisely the image of
all simultaneously triangularizable tuples, since conjugation does not change
the coefficients and every diagonal tuple is allowed.

The fixed-factor condition is `product L_a(s)=0`. Since C[s1,...,s4] is a
domain, this means that one whole `L_a` is zero. Its preimage is a union of four
12-dimensional linear spaces. The finite map preserves their dimension and
has closed image. Hence the fixed-factor **chart** image of this family has
dimension **12 exactly**.

This closes the family-image problem, including limits taken inside that
family. It does not bound the full graph over a triangular support: Y in
section 4 is itself strictly triangular, but transverse arcs over it carry the
whole determinant closure. The same distinction applies to s78's retained
28-dimensional common-kernel/common-cokernel monic-family image result.

## 6. Remaining supports and the precise next job

**PROVED scope of the residual.** The global contraction K includes every
source support without a classification assumption. For a support-based route,
retain the full S2 projective graph chart ideals

```
H_h = (f_alpha - y_alpha f0 : alpha != 0) : f0^infinity,
L_h = H_h + (f0) + (y_bad),
```

on each `x_h=1`, with all 69 ratios present before saturation. S2's two
representative chart construction is retained as an alternative exhaustive
criterion, rather than rerun. The affine zero-pencil fibre is still the whole
projectivized image, as proved by S2, and is excluded from the projective
source. Section 4 now identifies a separate nonzero support with the same
image issue.

| Residue | Exact defining data / obligation |
|---|---|
| Normalized infinity | `z=0`, all 69 `p_i(N)=0`, and the full saturated graph, not only its support |
| Nonzero rank-one support Y | Explicit equations `A5=0`, all entries except `(1,4)` zero; graph image is **already `P(D5)`**, proved here |
| Entire rank-at-most-one original pencil locus | All coefficients of all 2 by 2 minors: at most 36 times 15 = **540 equations**; includes Y, so its graph image is also universal |
| Rank-at-most-two original pencil locus | All coefficients of all 3 by 3 minors: at most 16 times 35 = **560 equations**; cannot discard later leading coefficients after the quadratic one cancels |
| Lower coefficient-span loci | Minors of the 16 by 5 coefficient array; independent of the bounded matrix rank of the pencil |
| Other named primitive/compression incidences and special rank strata | Retain S2's exact graph restrictions and unresolved support-complement obligation; the names are not an exhaustion certificate |

**Exact next elimination job.** Compute
`K=<y-p(B)> intersect Q[y]` from `full_monic_Q.sing`, then substitute the 35
bad variables to zero. That **first contraction** is uncompleted; no intermediate
Groebner basis is claimed. A smaller proof certificate could consist of one
explicit polynomial `F(y)` with:

1. `F(p(B))=0` as an exact rational polynomial identity;
2. `F(y_good,0)` nonzero, with a displayed nonzero coefficient or a rational
   fixed-factor witness where it does not vanish.

Such a certificate suffices without finishing a Groebner basis. Vanishing only
on `G(S)` does not suffice. Any returned equation must also pass the known
`B=0`/`v^4` control and exact triangular-family substitution. Equality `J_W=0`
needs a complete contraction or an independent valid dominance argument.

**RECORDED cost, not a runtime promise.** Input construction here takes less
than a second and under 17 MiB process commit memory. The global algebra is
133 variables / 69 generators / degrees `1^4,2^10,3^20,4^35` / 7,957 terms.
The infinity-chart saturation has 134 variables / 70 generators. s78's different
149-variable pilot is source-reported to have reached 600 seconds with about
4.4 GB, and its 64-variable singular-source dimension pilot reached a 6.2 GB
cap at 420 seconds. Those are historical measurements, not predictions for K.
This session did not launch either large job. A next CAS pilot should begin
with one bounded 600-second run and an explicit host-appropriate cap, preserving
the input and partial basis if the contraction does not finish. No such run or
schedule has been created here.

## 7. Verification, dependencies, and execution record

**CERTIFIED.** `analysis/b13_12_exact.py` independently reconstructs the monic
coefficients using determinant permutations and subsets of fixed diagonal rows.
It parses the inherited coefficient expressions with a restricted AST parser;
they are data, not executed code. Equality holds at all 69 nonanchor
polynomials. Two integer point families (seeds `1312001`, `1312002`, six cases
each) compare the whole polynomial with a separate fraction-free Bareiss
determinant path, over Z and both house primes `2147483647`, `2147483629`.
All points and ordinary coefficient arrays carry their `values_are` convention.
There is no transported-value or unrecorded u-scaling issue in this task.

**CERTIFIED replay.** The inherited S2 verifier was imported with only its
output directory redirected to `results/b13_12/s2_replay`. Its complete run
returned rational ranks `9,0,3,9`; tangent ranks `57,57`, sum 64, intersection
50, quotient zero; eight independent jet controls; and the explicit rank-three
arc with 24 determinant checks. The finite rational matrices have exact
kernels and nonzero minors and agree at both house primes. This is a replay
of that instrument, not a newly independent proof of every S2 theorem. Its
previously unstaged tangent artifact is regenerated in the delivery.

**RECORDED preflight.** Bundled Python 3.12 and numpy were available.
`python-flint`, sympy, scipy and psutil were absent; Singular and msolve were
not on PATH. Installation was attempted, but the host denied the package
network socket (`WinError 10013`) before download. A local runtime/workspace
search found no substitute installation. No missing import is interpreted as
a mathematical result. All completed calculations use exact standard-library
arithmetic; no finite exact computation was downgraded to sampling. The
Singular files are generated mathematical inputs, **not executed CAS scripts**.

**MEASURED launch controls.** Available physical memory was checked before
every run. Each child waited for assignment to a Windows Job Object before
computation, with a 1 GiB process-memory limit, one computational worker and
one BLAS/OpenMP thread. Logs, recorded PIDs and resource records are under
`results/logs/b13_12_*`.

| Unit | Wall cap | Measured elapsed seconds | Peak process commit bytes |
|---|---:|---:|---:|
| Coefficient audit and residual generation | 120 s | 0.187 | 16,244,736 |
| Generic boundary identity and small controls | 120 s | 0.141 | 14,819,328 |
| Complete S2 replay | 300 s | 1.156 | 15,986,688 |
| Triangular-family coefficient control | 120 s | 0.109 | 14,290,944 |

**RECORDED input interpretation.** The board names S2, reviewed s78 and the
batch-11 formulation as collections rather than exact filenames. Repository
search resolved them to the S2 report/verifier/graph generator and certificates,
`docs/s78_report.md`, `docs/s78_review.md`, `results/s78_reduced_polys.json`,
their generators, `docs/batch11_plan.md` section 6 and the Rees audit/response.
These are documented input-resolution choices; no unrelated historical context
was used to invent an assignment. The input manifest hashes every used file.

## 8. Boundaries, delivery, and what to review

**ADOPTED, unchanged.** At LMR, `D=mult_pad-mult_det`, exact determinant rank is
**273**, and the certified padded floor is **269** in the 274-dimensional
source. Thus `D=1-i_pad(24)` and the justified interval is `[-4,+1]`. The
measured value `-4` is not certified here; `i_pad(24)=i_pad(23)` is not promoted.
Sampled deficiency never establishes rational ideal membership. This geometry
session proposes no new multiplicity obstruction or separating statistic, so
it makes no claim to have run the three-family degeneracy protocol.

**RECORDED delivery.** The bundle is
`b13_12_five_variable_closure.bundle`, with identical
`b13_12_five_variable_closure.part00`. Whole and part MD5 and SHA256 digest
files use bare filenames. `results/b13_12/manifest.json` records the session,
provenance and artifact checksums; the user-facing delivery manifest records
the final branch head and bundle hashes. All changed files are below 5 MB.
User-facing copies live under
`C:\Users\swami\Projects\gct-gpt\Batch13_Results\B13-12`.

Review first the proper-image argument in section 4 and the ordering of
contraction and restriction in section 3. The next mathematical result needed
is a certified nonzero restriction of an element of K, or a valid proof that
the fixed-factor chart is contained. More generic higher-contact samples or a
classification of actual singular pencils alone do not discharge that job.
