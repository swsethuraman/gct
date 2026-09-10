---
board_numbering: batch13
session_id: B13-03
model: gpt-6-astra
reasoning_effort: xhigh
status: success - complete exact control and reusable algorithm
base: 00495110c62acfbbbc951e82cc218ed091563b3f
branch: b13-03
bundle_parts: 1
---

# B13-03: exact reducible membership

**CERTIFIED / RECORDED.** This delivery has **one part, part00**, accompanying
`b13_03_exact_reducible_membership.bundle`, with whole-file and per-part MD5 and
SHA-256 checksums. The primary assignment is complete: a reusable exact
restriction algorithm, a complete rational highest-weight control with both an
accepted nonzero element and a rejected non-element, and a separate replay.
No branch history was rewritten. All work was done in the prepared B13-03
checkout and banked on `b13-03`.

**CERTIFIED.** For ternary quartics in coefficient degree 6 and weight
`lambda=(8,8,8)`, the complete source dimension is 2, the reducible restriction
rank is 1, and the reducible ideal multiplicity is 1. The accepted polynomial
`F0` has 377 nonzero integer terms. The rejected polynomial `F1` has 411 terms;
it takes the exact value **729** at the supplied reducible point. In the mixed
basis `(F0+F1,F1)`, neither basis vector is an ideal element and the exact kernel
is `(1,-1)`. Thus the implementation handles cancellation between source vectors.

**ADOPTED, unchanged.** The programme's sign is
`D=mult_pad-mult_det`. At the degree-24 LMR cell, `rank T_det=273` exactly and
`rank T_pad>=269`; the unconditional identity is `D=1-i_pad(24)` and the
justified interval is `[-4,+1]`. This run makes no new LMR rank, membership,
degree-23/24 equality, or sign claim. Sampled reducible nullity 5 remains a
sampled deficiency. No nonzero cubic-permanent ideal constituent or positive
gap is claimed, so the positive-claim verification protocol was not activated.

## 1. Exact map and conventions

**PROVED.** Let `V=Q^r` and write a quartic as
`f(x)=sum_(|alpha|=4) c_alpha x^alpha`, a linear form as `sum y_i x_i`, and a
cubic as `sum_(|beta|=3) d_beta x^beta`. The multiplication morphism induces

```
mu*: Q[c_alpha] -> Q[y_1,...,y_r,d_beta]
c_alpha -> sum_(i:alpha_i>0) y_i d_(alpha-e_i).
```

There is **no alpha_i factor** in this ordinary-coefficient formula. In source
degree `delta`, its image has bidegree `(delta,delta)`. With
`q4=binom(r+3,4)` and `q3=binom(r+2,3)`, the full source and target dimensions are

```
binom(q4+delta-1,delta),
binom(r+delta-1,delta) * binom(q3+delta-1,delta).
```

**PROVED.** A polynomial belongs to the ideal of the image closure exactly when
its pullback is the zero polynomial: every parameter value is substituted, and
a polynomial over the infinite field Q vanishes identically iff all its
coefficients vanish. The image over C is already closed: it is the affine cone
over the image of the projective multiplication map, whose source is projective.
Here “reducible” means **having a linear factor**. Quartics that factor only as
two quadrics are not part of the definition. Working over Q computes the same
kernel after scalar extension to C.

**PROVED / ADOPTED.** The parameter map itself is not finite: nonzero fibers
contain `(t ell,t^-1 c)`. Its image coordinate ring embeds in the diagonal
subring `bigoplus_delta Sym^delta V tensor Sym^delta(Sym^3 V)`. For `r>=3`, this
diagonal ring is the normalization of the linear-factor image ring, as in
[Kadish--Landsberg, Theorem 1.7 and Proposition 1.8](https://arxiv.org/pdf/1204.4693).
The normalization description is background, not an assumption of our kernel
test. In two variables a general quartic has four choices of linear factor up
to scale, so that parameter quotient is not birational and must not be called
its normalization. The binary control below deliberately exercises that case.

**PROVED.** On the highest-weight space `M_lambda`, the equivariant map is
`S=mu*|M_lambda`, and

```
i_red(lambda,delta)=dim ker S,
mult_red(lambda,delta)=dim M_lambda - dim ker S = rank S.
```

These are multiplicities, not dimensions of whole Schur modules. The Pieri
decomposition of the target multiplicity space is a direct sum of cubic
highest-weight spaces indexed by horizontal `delta`-strip predecessors of
`lambda`. Every cubic plethysm multiplicity is retained. The stored coefficient
rows do not pretend to be a normalized Pieri basis; they realize the same map
in an explicitly labeled ambient weight basis, hence have the same kernel/rank.
This is the first stage of the batch-10/S4 factorization. No permanent stage `Q`
is constructed or used. In particular no sum of separate block ranks is used
to infer a composite rank.

**PROVED / CERTIFIED.** House symbols satisfy `m_alpha=alpha! c_alpha`, with
`alpha!=product_i alpha_i!`. Therefore their substitution is
`m_alpha -> sum_i alpha_i y_i m_(alpha-e_i)`. The factorial identity was checked
at every ternary quartic coordinate, along with a squared mixed-coordinate
pullback whose coefficients are `1,1,1,2,2,2`. The raising rule on ordinary
coefficients is `(alpha_i+1)c_(alpha+e_i-e_(i+1))`; replacing this with
`alpha_(i+1)c_(...)` would change the actual source vectors.

## 2. Why the small exact restriction suffices

**PROVED, rederived from S4.** Define `R1 F=F(x1*c)` by retaining precisely the
source monomials all of whose factors have `alpha_1>0`, and subtracting `e1`
from each retained factor's exponent. The surviving monomial map is injective.
On a checked highest-weight source, `ker R1=ker mu*`.

Indeed, the simple raising operators generate all positive-root derivations.
Thus a highest-weight polynomial is invariant under the shears
`x1 -> x1+sum_(j>1) t_j xj`. For `ell=y1*x1+...+yr*xr` with `y1!=0`, choose
`t_j=-y_j/y1`; the shear carries `ell*c` to `y1*x1*c'`. If `R1 F=0`, it follows
that `F(ell*c)=0` on this dense open parameter set. Polynomiality then gives
`mu*F=0` identically. The converse is specialization. Every source vector and
every combination has the same checked highest weight, so this is a linear
kernel test on the entire source.

**PROVED.** The all-coordinate `(star)` test follows too: general membership
implies restriction zero on each `xi*c`; conversely their vanishing includes
`x1*c`. This rederives the repository criterion without requiring a numerical
Pieri conversion. The fixed-factor codomain may be chosen as cubic coefficient
monomials of degree `delta` and weight `lambda-delta*e1`. If `lambda_1<delta`
that space is zero. There is no claim that this fixed-factor map is a
GL_r-equivariant representation of the full factorization; only its kernel
equality on highest-weight inputs is used.

**CERTIFIED hypothesis guard.** The non-highest-weight polynomial
`c_(4,0,0)c_(0,4,0)c_(0,0,4)` passes the monomial support condition on every
coordinate-factor subspace but evaluates to 1 at
`(x1+x2+x3)(x1^3+x2^3+x3^3)`. The shortcut rejects it after an explicit nonzero
raising residual. The universal pullback correctly rejects ideal membership.
The guard is essential: coordinate-factor vanishing alone proves nothing for
an arbitrary polynomial.

## 3. Complete control and certificates

**CERTIFIED.** The producer independently enumerated all source weight
monomials in the opposite exponent order to the old core, built every simple
raising equation, and used exact primitive-integer elimination with rational
back substitution. The archived vectors were remapped by exponent tuples,
verified over Z, proved independent, and proved to span the newly built space.

| Quantity at `(8,8,8)`, degree 6 | Exact value | Status |
|---|---:|---|
| Full quartic degree-6 source dimension | 38,760 | CERTIFIED |
| Source weight-monomial count | 561 | CERTIFIED |
| Raising matrix | 1,056 by 561 | CERTIFIED |
| Raising rank over Q and at both house primes | 559 | CERTIFIED |
| Highest-weight source dimension | 2 | CERTIFIED |
| Full bidegree target dimension | 140,140 | CERTIFIED |
| Target weight-monomial count | 2,077 | CERTIFIED |
| Stored full pullback after deleting zero rows | 1,720 by 2 | CERTIFIED |
| Fixed-factor weight-monomial count | 38 | CERTIFIED |
| Stored fixed-factor matrix after deleting zero rows | 21 by 2 | CERTIFIED |
| Both exact restriction ranks | 1 | CERTIFIED |
| Both exact kernels, archived source coordinates | span `(1,0)` | CERTIFIED |

**CERTIFIED.** The unique Pieri predecessor is `(8,8,2)`. A separate complete
cubic highest-weight calculation gives a `54 by 38` raising matrix of rank 37,
so its multiplicity is 1 and `h_red=1` exactly. This computes a cubic source
multiplicity only, not a cubic-permanent restriction or ideal.

**CERTIFIED.** `primary_source.json` contains the explicit nonzero polynomials
as ordinary coefficient monomials with integer coefficients. The first source
has maximum coefficient magnitude 288; the second 13,824. The fixed pullback
of `F1` contains, for example,
`36*d_(1,2,0)^2*d_(0,2,1)^2*d_(0,0,3)^2`. Thus rejection is independently
visible in one nonzero coefficient, not just an evaluation rank.

**CERTIFIED.** An additional exact rejection witness uses `ell=x1` and the
cubic coefficient vector
`[0,-1,-2,-1,-1,1,-1,3,3,0]`, in the explicit descending cubic exponent order
stored with the point. It gives `(F0,F1)=(0,729)`. `primary.json` contains every
nonzero pullback coefficient and row label, the mixed-basis cancellation maps,
all nine archived point evaluations replayed at both house primes, complete
source certificates, and the normalization multiplicity control. Zero rows
are omitted by an explicitly stated sparse convention; no source term is
silently discarded.

**CERTIFIED.** `b13_03_verify.py` imports no producer routines. It uses brute
force source enumeration, occurrence-by-occurrence derivatives, literal
labeled-factor pullback expansion, and a separate dense modular elimination.
It reproduces rank 559 at both house primes, checks the two integer source
vectors and their independence, and compares every pullback coefficient. NumPy
int64 arithmetic is exact here: each multiply/subtract is reduced modulo p,
and `(p-1)^2+(p-1)<2^63`. It also rechecks the mixed cancellation and value 729.
The load-bearing membership proof is the rational identity, not modular zeros.

**CERTIFIED additional controls.** The complete degree-2 cells `(4,4)` in two
variables and `(4,4,0)` in three variables both have source dimension 1 and
restriction rank 1. The highest-weight powers `c_(4,0,0)^delta` at degrees 1
and 2 are rejected. Six malformed-coordinate/degree/weight/coefficient inputs
are rejected. Exact rational coefficient arithmetic is exercised by the row
`(1/2,1/3)`, whose kernel is `(2,-3)`.

**CERTIFIED extension, bounded scope.** The archived polynomial at
`(8,4,4,4,4)`, degree 6 in five variables, has 19,834 distinct integer terms.
All four simple raising derivatives vanish over Z, and every coordinate-factor
support restriction is zero. It is nonzero by an explicit coefficient and by
replayed determinant-point values. This certifies one rational reducible ideal
element. Neither its entire highest-weight space nor its full symbolic
pullback was computed. The independent verifier repeats the raising and support
checks using the original exponent ordering.

## 4. Algorithm, interface, and cost boundary

**RECORDED / PROVED.** `analysis/b13_03_exact.py` accepts either a supplied
rational source or `--cell n:r:degree:lambda1,...,lambdar`. The latter enumerates
the full weight basis, builds the simple raising map, and constructs its exact
kernel. The supplied-source interface verifies weight, raising equations and
independence, but explicitly does **not** assert completeness of an externally
supplied source. Both return the ideal kernel in source coordinates. `--full`
additionally constructs and checks the universal pullback. The polynomial-level
`full_pullback` function also accepts non-highest-weight inputs; the fixed-factor
shortcut always checks the highest-weight hypothesis first.

**PROVED cost model.** If the input basis has `a` vectors, `K` total nonzero
coefficient monomials and degree `delta`, support filtering and fixed-factor
mapping take `O(K*delta)` coordinate inspections. Verifying the raising
equations takes at most `O(K*delta*(r-1))` contributions, plus dictionary/sorting
costs. Literal full expansion has at most `r^delta` choices per monomial; the
implementation combines duplicates after each multiplication. Exact linear
algebra then acts on a matrix with `a` columns and the displayed coefficient
rows. Ordinary dense elimination needs `O(m*a*min(m,a))` rational arithmetic
operations; coefficient bit growth and sparse fill affect actual cost. These
are arithmetic bounds, not forecasts for an unexpanded circuit source.

**MEASURED.** The complete primary control took 0.496 seconds, including exact
source reconstruction; the full pullback portion took 0.047 seconds. It made
106,969 branch accumulations, with at most 216 live terms in a single source
monomial expansion and 1,720 in an accumulated image. The five-variable check
took 0.459 seconds. A fresh complete-space CLI run took 0.381 seconds and
24.4 MiB peak working set; the separate verifier took 2.812 seconds and
50.0 MiB peak working set. Timings are local observations, not asymptotic claims.

**RECORDED boundary.** The launch cap is one worker, one BLAS thread, 768 MiB
of Windows Job Object process memory, and 600 seconds per unit. The builder
guards 1,500 source weight monomials, 2,500 raising rows and 5,000,000 matrix
entries. Symbolic images guard 250,000 live terms. All runs completed well
inside these limits. Inputs larger than the builder cap may still use a
certified supplied source under the separate term and process caps.

**RECORDED, not reached.** No degree-13 or degree-24 LMR source was expanded.
At `(r,delta)=(9,24)`, there are 495 quartic and 165 cubic coefficients. The
uncompressed degree source has approximately `1.31e41` monomials, the full
bidegree target `1.39e37`, and even the unweighted fixed-cubic target `1.32e30`.
These exact binomial dimensions price why a dense ambient implementation is
excluded; they do not estimate the much smaller weight or circuit support.
The next concrete integration job is to export a certified source into these
ordinary coefficient coordinates, or implement coefficient queries on its
retained fixed-factor slice. Its expansion size `K` must be measured before
allocating it. No runtime estimate for that missing conversion is asserted.

## 5. Provenance, execution audit, and limitations

**RECORDED.** The actual model was `gpt-6-astra`, reasoning effort `xhigh`,
verified from this session's local `turn_context` metadata. The controlling
board, preamble, corrections, batch-12 stocktake and wording rules were read.
The broad B13-03 input names resolved to `docs/reducible_ideal.md`,
`docs/s64_integrator_note1.md`, S4's report, calibration implementation and two
control artifacts, plus `analysis/wk8_s30_core.py` for coefficient convention.
`docs/transfer_lemma.md` was read for the factorization/containment distinction.
The board gives no exact small-control filenames; resolving them from S4 was
the only assignment ambiguity. No withdrawn session prompt controlled this run.

**RECORDED toolchain deviation.** Bundled CPython 3.12.14 and NumPy 2.3.5 were
available. python-flint, SymPy, SciPy, psutil, Singular and msolve were absent
from the detected runtime/PATH. A local binary-wheel installation attempt was
blocked by WinError 10013. No dependency or global configuration was changed.
The run retained the exact question, using Python integers/Fraction for the
producer and independently bounded int64 modular arithmetic for verification.
No missing dependency was treated as a mathematical result. Native memory
preflight observed 6.94 GiB available initially; every numerical launch rechecked
availability. PID files are retained with the user delivery; `.pid` is ignored
by the repository, and resource JSON files also record the same IDs.

**RECORDED correction.** The first primary run reconstructed the exact source
and both maps, then stopped at a proposed rejection-point assertion: the
hand-selected cubic also lay in `F1`'s zero set. That was a poor witness choice,
not a map discrepancy. A bounded deterministic eight-point search found the
recorded witness at index 0. Both the original failed log and successful retry
are retained. No measured outcome or negative mathematical claim was banked
from the failed witness.

**RECORDED.** The prepared branch started at the user-specified frozen base.
There was no local `main` ref, so preregistration recorded verified HEAD and the
failed `git rev-parse main` rather than inventing a main revision. No shared
checkout writes, other-session dependencies, subagents, fresh clone, external
publication, push, or follow-up schedule were used. Source identities and
small-control ranks were certified; the optional whole padded factorization,
target-scale source conversion and LMR sign remain outside this deliverable.

**RECORDED replay.** See `results/b13_03/REPLAY.md` and
`results/b13_03/manifest.json`. The user-facing delivery includes the report,
code, exact sources, coefficient maps, resource logs, original control inputs,
the verified bundle and its single part, and delivery checksums. All committed
files are below 5 MB. The package needs only the frozen base to apply the
bundle; the copied control inputs also support direct local replay.
