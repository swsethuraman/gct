---
board_numbering: batch14
session_id: B14-08
actual_model: gpt-6-astra
reasoning_effort: xhigh
model_evidence: executing automation.toml; model=gpt-6-astra, reasoning_effort=xhigh
branch: b14-08-astra
base_commit: 9898e56941a7665f231873481dae956f08509995
base_tree: cb688cd3fe454d638f3202e759e2eaa0c629739f
preregistration_commit: c58063e5
run_date_utc: 2026-09-12
---

# B14-08: transport census audit

**RECORDED — Delivery has one part, `part00`, alongside the whole named-branch
bundle. The core audit is complete:** all 239 records and 717 source/target tests
were rebuilt, and every positive pair has an explicit, exactly checked
highest-weight polynomial witness. All frozen flags agree. **No new
multiplicity-gap exclusion is certified.** The witnesses establish that
transport is possible; they do not supply the missing padded ideal relations.
The frozen LMR evidence remains **a=274, determinant rank 273, padded rank at
least 269, and D in [-4,+1]**. Actual bundle head/tree, checksums, prerequisite,
and final delivery-gate results are in the accompanying delivery manifest and
verification logs; this report does not try to contain its own commit hash.

## Exact result

**CERTIFIED — Finite comparison relative to the frozen B13-06 tensor-domain
list.** The new producer imports neither the historical reachability script nor
the house `a_weyl` counter. It reconstructs canonical `(degree, partition)` keys,
checks the full degree/length histogram and named controls, and computes every
source difference. The original decomposition and its channel multiplicities
are **ADOPTED** inputs, not a fresh tensor decomposition.

| Degree | Records | Length 9 / 10 | Reached from rung 13 | Rung 14 | LMR | Reached from any source |
|---|---:|---:|---:|---:|---:|---:|
| 25 | 31 | 15 / 16 | 5 | 5 | 1 | 5 |
| 26 | 208 | 89 / 119 | 26 | 26 | 3 | 26 |

**CERTIFIED.** Of 717 tests, 600 fail dominance, 51 have exact ambient
multiplicity zero, and 66 are positive. Those 66 pairs use **61 distinct
primitive integral HWV witnesses**, comprising 1,149 nonzero monomial terms.
The verifier checks all their weights, degrees, nonzeroness, and every simple
raising operator, including the boundary into an unused variable. It also
independently recounts 694 weight-monomial terms in the character certificates.
The maximum constructed raising matrix is 425 rows by 221 columns.

**CERTIFIED — Negative domain.** All 135 ten-row records are unreached from
these three nine-row sources; the 16 degree-25 records were processed first.
Each has ninth part 2 and positive tenth part. Subtracting any specified source
therefore gives difference entries 9 and 10 equal to 0 and a positive integer,
which is not dominant. Some stored certificates record an earlier inversion;
the verifier additionally checks this common ninth/tenth-row argument.
This says nothing about arbitrary source weights or non-Cartan projections.
Among nine-row records, 73 are also unreached. In total, 208 records are
unreached by these source Cartan products; they are not excluded from D>0.

The four LMR-specific positives are `(69,17,2^7)_25`, `(73,17,2^7)_26`,
`(71,19,2^7)_26`, and `(69,21,2^7)_26`. Their multiplier weights are respectively
`(4)`, `(8)`, `(6,2)`, and `(4,4)`. The latter factors are scalar-normalized
versions of `8c0*c2-3c1^2` and `12c0*c4-3c1*c3+c2^2`.

## What the certificates prove

**PROVED — Character instrument.** Work in
`A_Z=Z[c_alpha: |alpha|=4]`, in coefficient degree d, with
`c_alpha(F)=[s^alpha]F`. Ordinary monomials are a weight basis. The new integer
coin recurrence counts these monomials; a separate multiset recursion checks
the recorded counts. If C is the weight character, the coefficient of a
dominant weight mu in `C * product_(i<j)(1-x_j/x_i)` is its Schur multiplicity:
multiplying the Schur character formula by this product leaves the alternating
orbit of `lambda+rho`, and exactly its identity term can contribute at the
dominant `mu+rho`. The certificate stores every nonzero aggregated alternant
term and its integer monomial count. Thus a recorded zero is an exact finite
character calculation, not a sampled vanishing.

**CERTIFIED — Positive instrument.** For every distinct positive difference,
the code independently enumerates actual coefficient monomials and solves the
simple raising equations over Q. The combined raising rank has nullity equal
to the independently counted multiplicity. Only one nonzero vector per
difference is needed and delivered. Clearing denominators and removing content
gives a primitive vector; the separate verifier differentiates every individual
factor occurrence over Z. These derivative identities, together with the weight
and a nonzero coefficient, certify an ambient HWV without trusting the
construction's reported rank. No determinant or padded evaluation is involved.

**RECORDED — Matrix and normalization contract.** A raising matrix has raised
monomials as rows and source monomials as columns; its HWVs form the **right
kernel**. An evaluation matrix would instead have source polynomials as rows,
points as columns, and relation vectors in its **left kernel**, `A^T K=0`.
No evaluation matrix is shipped or used here. Stored polynomial and matrix
metadata include `values_are`. Letter exponent tuples are explicit; no other
module's exponent ordering is assumed.

The exact convention is `E_ij c_alpha=(alpha_i+1)c_(alpha+e_i-e_j)` when
`alpha_j>0`. The common integral model is the ordinary coefficient ring above,
embedded in its Q extension. Rational construction denominators observed were
`1,2,3,4,5,8,9,10,40`; their prime support is only `{2,3,5}`. Each witness's
clearing LCM is checked coprime to **both** 2147483647 and 2147483629, and the
primitive witness reduces nontrivially at both. Integer zero derivatives reduce
to zero there. No modular rank is lifted to an upper bound over Q. The historical
`m_alpha=alpha! c_alpha` convention is not silently substituted; in particular
`msym_u=24u` differs from this report's `u=c_(4,0,...)`.

## Lemma T: conditional transport, zero new exclusions

**PROVED — Application of frozen Lemma T.** If w is a nonzero ambient HWV of
weight mu, multiplication by w is injective in the polynomial domain A and
preserves every ideal I(X). It sends an ideal HWV of weight lambda to weight
lambda+mu without projection. Consequently `i_X(lambda+mu)>=i_X(lambda)`.
It does not require w to be nonzero on X for this ideal injection. The stronger
coordinate-ring injection does require that additional hypothesis.

**CONDITIONAL.** Let p13, p14 and p24 be certified padded ideal floors at the
three stated sources, once certificates exist. Each record supplies
`L=max(0, all reached p-values)`. The maximum is essential: independent source
images may overlap, so their dimensions cannot simply be added. If a compatible
certified determinant ideal upper bound U is available, then `D<=U-L` and
`U<=L` excludes D>0. A determinant rank floor k with certified ambient dimension
a gives the valid upper bound `U=a-k`.

**OPEN.** The frozen inputs provide no positive certified padded source floor,
so the currently certified floor is zero for every record. Only the two pure
u-ladder targets inherit `i_det=1` from `lmr_ranks` and
`cartan_ladder_invariance`; their gap remains the original [-4,+1]. The other
237 rows have no sufficient determinant ideal upper certificate in the audited
inputs. Every table entry explicitly records the missing evidence and leaves
`exclusion_status=OPEN`. The tensor-domain multiplicity bounds the image of
the LMR-generated product subspace; it is **not** an upper bound on the whole
determinant ideal. The inherited 97 eleven-row exclusions are outside this
239-record task and were not recounted or claimed anew.

Five sampled padded kernel vectors do not provide five equations.
`evaluation_cannot_certify_i_ge_1` applies: a sampled nullity is an ideal
dimension ceiling. Complete interpolation could change that only with a proved
target dimension, genuine target members, a full target minor, and exact source
arithmetic in compatible conventions. None of those missing source/target
packages was substituted by this census.

## Lemma B: every row has an explicit bound

**PROVED — Application of frozen Lemma B.** Each row records the valid
predecessor `(nu1-4,nu2,...)` at degree d-1 and the inequality

`0 <= i_X(nu,d)-i_X(predecessor,d-1) <= a(nu,d)-a(predecessor,d-1)`.

For X=D,P,R, u is nonzero in their irreducible coordinate rings, so multiplication
injects ambient spaces, ideals, and coordinate rings. Subtracting the
coordinate-ring dimension inequality from the ambient increment proves the
upper bound. This is s57 Lemma L, restated as the memo's Lemma B.

**ADOPTED / RECORDED — Four numerical increments.** Both endpoints are present
in the frozen ambient-count records only at the following audited rows:

| Degree and target | Predecessor a | Target a | Ambient increment |
|---|---:|---:|---:|
| 25, `(69,17,2^7)` | 274 | 274 | 0 |
| 25, `(67,19,2^7)` | 390 | 391 | 1 |
| 26, `(73,17,2^7)` | 274 | 274 | 0 |
| 26, `(71,19,2^7)` | 391 | 392 | 1 |

B13-06's exact ambient counts are adopted; 390/391 are recorded single-method
recounts from the frozen prep file. These are not new ambient measurements.
In particular, the `(69,21,2^7)_26` target has a=531, but its immediate
predecessor's dimension is not supplied, so its increment is left OPEN.

**PROVED — Conservative numerical fallback for all 239 rows.** Put
`r=length(nu)`, `s=sum(nu[1:])`, and

`B(r,d,s)=[z^d t^s] product_(j=1..4)(1-z*t^j)^(-binom(r+j-2,j))`.

There are `binom(r+j-2,j)` quartic letters of tail degree j. Thus B counts all
degree-d monomials of scalar tail weight s with no u factor. The quotient
`M_nu / (u*M_predecessor)` injects into `(A/uA)_nu`: if an HWV is divisible by
u, its quotient is an HWV because every raising operator kills u and A is a
domain. Its dimension, the ambient birth increment, is therefore at most B.
Dropping the separate tail coordinates only enlarges this monomial space.

Each row carries this exact integer B, the symbolic exact ambient increment,
and the best available bound (the inherited increment when available, otherwise
B). The verifier recomputes B by a separate two-loop binomial sum over counts
of tail-degree-3/4 letters. **These coarse bounds do not claim exact ambient
dimensions or close a gap.** The 235 unsupplied exact increments remain OPEN;
the largest delivered coarse bound is 688909497685201096650. Funding 235 large
ambient recounts was not part of the transport audit.

## Validation and resource record

**CERTIFIED.** The final verifier requires all 239 keys, all three source
definitions, all 717 tests, all 61 positive witnesses and the frozen input blobs.
It checks the 600 explicit dominance inversions, exact character sums, 694
independent monomial counts, all positive polynomial identities and all 239
birth bounds. Missing data cannot yield a successful audit.

**CERTIFIED — Controls exercised.** There are 29 local controls, including
empty census, each of four missing named controls (with counts preserved to
reach the named-control assertion), duplicate/invalid keys, missing reference
source/target, wrong source degree, a false LMR flag with another source true,
a forced ten-row positive, altered witness coefficient, wrong coefficient
normalization, a denominator divisible by a house prime, and missing/wrong-source
positive witnesses. Synthetic exclusion cases reject missing certificates,
insufficient bounds and product-image bounds; the sufficient synthetic case
accepts the arithmetic implication. This is a test of decision logic, not a
verifier of other sessions' ideal certificates. Seven small exact character
controls include both nonzero and zero constituents of Sym^2(Sym^4 C^2).

**RECORDED — Historical code also tested.** Eight runs comprise a valid replay,
empty census, each missing named control, wrong-source flags and a forced
ten-row positive. The valid case returns 0; every deliberately invalid case
returns 1. The wrong-source case retains positive rung flags while setting the
LMR flags false. The historical file itself is untouched. The `historical_06`
and `historical_07` JSON outputs are deliberately invalid fixtures, not evidence;
their expected failure transcripts are in verification.json.

**MEASURED — Shared Windows host.** Python 3.12.14; numpy 2.3.5 available, used
only by the historical replay; 20 logical CPUs; total physical RAM
33,752,997,888 bytes. No dependency installed. Each run used one calculation
process and one numerical-library thread. The reused native Windows Job Object
wrapper, adapted only to B14-08 paths/labels, enforced 512 MiB and 180 seconds.
PIDs and resource files are under results/logs with the b14_08 prefix.

The core completed in 1.282 seconds, with peak process memory 27,181,056 bytes
and 12,327,043,072 bytes host RAM available at launch. Initial verification
completed in 0.859 seconds at 68,493,312 bytes. Final verification after the
additional missing-witness controls completed in 0.891 seconds at 69,124,096
bytes, with 13,461,008,384 bytes of host RAM available at launch. No calculation
exceeded a registered cap; no extension was used.
These timings are measured replay costs, not estimates for ambient rank builds.

## Limits, assignment defects, and next work

**NOT REACHED — Adjunction stretch.** The frozen board assigns proof and a
validation with both spaces of dimension at least two to slot 5; the frozen
memo explicitly says adjunction is missing and names needed height-3 and
unequal-height (10,9) evaluator support. No qualifying frozen certificate was
provided, so no U_D/U_P image-rank sweep was launched. Ten sampled zero values
would remain unresolved. We did not wait for or import later-session results.

**RECORDED — Precise next requirements.** To turn any reached row into an
exclusion, first accept a padded source ideal floor using the coupled target
membership/dimension/minor and exact-source certificates, then supply a
sufficient determinant ideal upper bound at that row. The CSV gives the exact
comparison needed for each one. For the stretch, validate adjunction and recover
the exact source directions before running one checkpointed column pilot at
1,200 seconds / 768 MiB. Total symbolic construction cost remains unmeasured;
B13-06's 156,438,903,314-monomial LMR space is a reason to avoid full expansion,
not a runtime estimate for the small multiplicity maps.

**RECORDED — Assignment wording needing care.** The scratch manifest's phrase
that “4 of 30, 23 of 205” are settled by Lemma T alone remains too strong in its
historical table, despite its later correction. They are reached. “Lemma T
exclusions” in the packet cannot promise actual exclusions without both kinds
of ideal bound. The packet also supplies too few ambient counts for exact
numeric Lemma B increments at every row; this session provides the explicit
symbolic inequalities and proved coarse numerical bounds instead. The ten-row
sentence must keep its specified source/census scope. No historical file was
silently corrected, and no absence of a known equation became an exclusion.

## Artifacts and replay

**RECORDED.** The named branch contains the scripts, frozen-input hash manifest,
committed preregistration, full JSON/CSV census, all factor witnesses, controls,
resource logs, and this report. Only two new finite results are appended to the
proved index. There is no new D-exclusion predicate to add to the shared ledger.
Protected files, other sessions and integration were untouched; no push or
merge was performed.

- [Complete table and certificates](C:/Users/swami/Projects/gct-gpt/work/batch14/B14-08/results/b14_08/census.json)
- [Spreadsheet-friendly census](C:/Users/swami/Projects/gct-gpt/work/batch14/B14-08/results/b14_08/census.csv)
- [61 integral witnesses](C:/Users/swami/Projects/gct-gpt/work/batch14/B14-08/results/b14_08/witnesses.json)
- [Exact verification and control transcripts](C:/Users/swami/Projects/gct-gpt/work/batch14/B14-08/results/b14_08/verification.json)
- [Replay instructions](C:/Users/swami/Projects/gct-gpt/work/batch14/B14-08/results/b14_08/replay.md)
- [Delivery directory](C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-08)

The delivery manifest supplies immutable base/head/tree identities, artifact
hashes, prerequisite refs and results of the repository's checks before and
after creation of the actual named-branch bundle. Whole/part checksum sidecars
name bare filenames. The input manifest records both canonical Git blob IDs
and local SHA256 values, accounting for line-ending differences on replay.
