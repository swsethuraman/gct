---
board_numbering: batch13
session_id: B13-02
model: gpt-6-astra
reasoning_effort: xhigh
base: 00495110c62acfbbbc951e82cc218ed091563b3f
branch: b13-02
outcome: bounded-fallback
bundle_parts: 1
---

# B13-02 — structural restriction of the LMR source

**RECORDED — Delivery has one part, `part00`, in addition to the whole bundle.**
The bundle is `b13_02_structural_restriction.bundle`, against the frozen base
above; the part is `b13_02_structural_restriction.bundle.part00`. Whole-file and
per-part MD5 and SHA256 accompany it. User-facing copies are in
`C:\Users\swami\Projects\gct-gpt\Batch13_Results\B13-02`. No history was rewritten.

**RECORDED — The bounded fallback is delivered; the primary upper bound is not.**
This run constructed exact restriction circuits for all 274 integral source
rows, independently verified the 48 cubic multiplicities summing to 521,
constructed complete small structural matrices, and computed 1,127 exact integer
entries of a 274-by-5 LMR coefficient matrix. There are 243 uncomputed entries,
explicitly null. No rational LMR ideal element was established.

**ADOPTED — The mathematical conclusion at LMR remains**

    rank T_det = 273 exactly,
    269 <= mult_pad <= rank S = mult_red <= 274 <= 521,
    D = mult_pad - mult_det = 1 - i_pad(24) in [-4,+1].

**RECORDED — Neither D <= 0 nor reducible rank 269 was proved here.** Three
completed coefficient columns happen to vanish; a coordinate projection with
rank zero is consistent with full-map rank at least 269. It is not a full-map
upper bound. The inherited five-dimensional sampled kernels remain candidates.

## Exact map and normalization

**PROVED —** For ordinary quartic coefficients, multiplication has pullback

    c_alpha -> sum_(i:alpha_i>0) y_i d_(alpha-e_i).

For house symbols `m4_alpha = alpha! c_alpha`, the same map is
`m4_alpha -> sum_i alpha_i y_i m3_(alpha-e_i)`. After fixing the linear factor
to `x1`, its value in ordinary cubic coefficients is **alpha! d_(alpha-e1)**
when alpha1>0, and zero otherwise. Multiplying by just alpha1 while treating
the cubic coordinates as ordinary coefficients would be a normalization error.

**PROVED —** On the highest-weight source, this fixed-factor map `R1` and the
full restriction `S` have the same kernel. One inclusion is specialization.
For the converse, the highest-weight equations make each source vector invariant
under the shears that carry a linear factor with nonzero first coefficient to
a scalar multiple of x1. The cubic factor remains arbitrary under that invertible
change of variables. Vanishing for x1 times every cubic therefore implies
vanishing on a dense open subset of the full parameter space, hence an exact
polynomial identity. This is S4's lemma, audited here against full pullbacks.
Consequently `rank R1 = rank S` on this source. A partial coordinate projection
of R1 need not have that rank.

**CERTIFIED —** All 274 native and literal fillings satisfy the column-distinct
and four-legs-per-letter conditions. Their column heights give the stated
weights, their literal extensions are the native fillings plus isolated
four-singleton letters, and every stored transport scalar equals `24^(24-d)`.
The exponent index of u was resolved from the explicit exponent enumeration.

**PROVED / CERTIFIED —** The artifact `source_restriction_circuit.json.gz`
specifies the full source in a lossless contraction realization: two tall
alternating columns, the short alternating columns, fixed singleton indices,
the 495 explicit quartic-symbol substitutions, and every native transport.
At x1*c, row j is its native restricted circuit multiplied by
`(24 d_(3,0^8))^(24-d_j)`. The coefficient algorithm applies exactly that scalar.
No pointwise u normalization or point transport is used in these new matrices.
No numeric conversion to 521 independent Pieri coordinates is claimed.

**PROVED —** The coefficient extractor tracks used tall-column indices, the
open short-edge assignments, and remaining cubic monomial multiplicities.
Its transitions are precisely the legal local tensor assignments. A tall-column
index cannot recur; an edge has complementary endpoint indices; each selected
letter contributes alpha!; the signs are the two exterior inversion signs and
the original short-column orientations. Summing over completed states enumerates
each contributing literal contraction once. Tuple keys are exact, with no
probabilistic hashing. Missing states caused by a cap return no coefficient.

## Small structural controls

**CERTIFIED —** On S4's ordinary-coefficient source at `(8,8,8), d=6`:

| Check | Exact outcome |
|---|---:|
| All simple raising equations on both integer vectors | 1,056 equations, zero residual |
| Nonzero 2-by-2 source minor | -3,981,312 |
| Full pullback matrix, retaining the union of nonzero coordinate columns | 2 by 1,720 |
| Fixed-factor matrix, same convention | 2 by 21 |
| Nonzero terms in the two full images | 0 and 1,720 |
| Nonzero terms in the two fixed images | 0 and 21 |
| Exact split rank and source kernel coordinates | 1 and (1,0) |
| Explicit nonzero fixed coefficient | 36 |

**CERTIFIED —** The source multiplicity two was also checked by fresh Weyl
alternation and by independent power-sum character arithmetic. Thus this is an
exact rank-one map from a complete two-dimensional source, not a sampled drop.
The full integer matrix is delivered in `control_r3_full_split.json.gz`.

**CERTIFIED —** A height-two degree-two bracket control has exact split rank
one. Its literal expansion agrees coefficient-by-coefficient with the new
extractor, including the zero coefficients of the relevant cubic weight.
A height-three degree-three control has 15 nonzero source terms and nine
nonzero fixed-factor terms; all nine coefficients agree with literal expansion.

**RECORDED —** The chosen height-four control cancels identically even before
restriction. Its zero result is retained as a cancellation example and is not
counted as a positive validation. No claim rests on a vacuous coefficient check.

## The 521-dimensional intermediate was recomputed

**CERTIFIED —** All 48 horizontal-24-strip predecessors were re-enumerated.
For each, the cubic multiplicity was recomputed by Weyl alternation, with shifted
weights sorted using symmetry before a fresh multiset generating-function DP.
Every integer addition was checked for overflow before execution. The algorithm
was calibrated against the separate power-sum/Murnaghan–Nakayama implementation
on three small cells. Every one of the 48 values agrees with S4's ledger; their
sum is **521**. This run upgrades that dimension from an inherited number to
an independently recomputed exact count.

**CERTIFIED —** The ordinary cubic weight space used by the fixed-factor
realization has **6,711,509,400 monomials** at weight `(41,17,2^7)`, degree 24.
The number 521 is a highest-weight/Pieri dimension, not the size of this
coefficient expansion. This distinction is the remaining construction problem.

## Bounded LMR coefficient pilot

**RECORDED —** Five coefficient monomials were fixed by seed 130200, using
legal literal summands of source rows 0,1,2,39,273 before examining their values.
Their explicit cubic triples are in `source_audit.json`. Every monomial has
degree 24 and weight `(41,17,2^7)`; no term or exponent lookup was silently dropped.

**CERTIFIED —** The exact completed entries are:

| Column | Completed out of 274 | Nonzero entries | Status |
|---:|---:|---:|---|
| 0 | 274 | 0 | complete coordinate column |
| 1 | 274 | 0 | complete coordinate column |
| 2 | 31 | 18 | interrupted; row 29 and 242 other rows uncomputed |
| 3 | 274 | 0 | complete coordinate column |
| 4 | 274 | 18 | complete coordinate column |

**CERTIFIED —** Rows 39 and 273, columns 2 and 4, give the exact minor

    [ 545694627621824058359808,                            0 ]
    [                        0, -1510785419245967974072320 ]

with determinant
`-824427486771909835571692119328382052689573314560`.
Its reductions at the two house primes are 921432311 and 1836696183.
The two nonzero entries were replayed after reversing the letter labels,
exchanging tall columns, and reversing one short-column orientation; each
replay gave exactly the expected negative. These are additional order/sign
checks, not an independent source construction or a proof of full-map rank.

**RECORDED —** This exact partial rank floor two is weaker than the adopted
padded floor 269. It demonstrates working structural entries, including a
nonzero degree-24 birth restriction. It says nothing about whether that birth
image is independent of all earlier images. In particular it does not settle
the degree-23/24 padded-nullity question assigned elsewhere.

**MEASURED / RECORDED —** The full two-prime s74 reducible candidate coordinates
and their source supports are preserved in `inherited_candidates.json` and
`verification.json`. Three directions are supported through rung 13 (rows at
most 38); two more through rung 14 (rows at most 92). These are modular candidates
in the literal transported source convention. No naive rational lift is treated
as an ideal element, and finite column zeros do not establish membership.

## Remaining calculation and its price

**RECORDED —** The smallest interrupted implemented object is **column 2,
source row 29**. Its 120-second per-coefficient/250,000-state instrument was
interrupted by the absolute wall deadline, not by a demonstrated mathematical
zero or a proved state-space barrier. The other completed contractions in that
column took 0.005–0.196 recorded seconds apiece, median 0.066; this range does
not price the interrupted coefficient. The existing 31 coefficients are retained.
The replay file gives a bounded resume command which skips completed entries.

**RECORDED —** Closing the primary question still requires an exact dependence
of the full restriction images, with a nonzero rational source combination, or
an equivalent complete structural matrix of rank at most 273. The smallest
inherited candidate uses the first degree-13 support; its unknown rational
coordinates and its entire symbolic restriction remain to be certified.
This session supplies a full-source instrument and partial matrices, not that
candidate identity. Nothing waits on another Batch 13 session.

**MEASURED / ESTIMATED —** The four completed columns cost 12.82, 13.22, 10.05,
and 0.73 seconds at launch level. Applying even this very selective range to all
6.711 billion coefficient columns would cost roughly 156–2,811 serial years;
this is a crude price for this particular exhaustive method, not a complexity
lower bound or a prediction for a compact Pieri conversion. Even eight bytes
per entry in a dense 274-row expansion would require 14.71 TB; actual exact
coefficients can exceed 64 bits. The unimplemented compact 521-coordinate
conversion has no measured cost here. Enumeration of the full carrier was not
launched.

## Execution, verification scope, and deviations

**RECORDED —** The actual scheduled model was **gpt-6-astra**, with `xhigh`
reasoning in the automation configuration. No model switch or subagent was
used. The clean prepared checkout was on b13-02 at the requested frozen base.
There is no local `main` reference; the immutable base replaces that preamble
query. No shared-checkout changes, external publication, push, fresh clone,
follow-up schedule, or global Git configuration change was made.

**RECORDED —** Required documents and the exact s74/S4 inputs were read.
The corrections control over the older stocktake and s74 review: sampled
padded/reducible equality and `i_pad(23)=i_pad(24)` were not adopted as theorems.
The tier-three board dependency was not reconstructed from unrelated sessions.
An input packaging defect was found: S4's retained replay refers to an omitted
`inputs/s1_checks.py` and `src/run.ps1`; its retained mathematical controls were
read directly. B13-02 itself has no separately specified fallback rubric beyond
the preamble's bounded-report discipline; this run preregistered its precise
fallback before computation.

**RECORDED —** Windows Python 3.12.14 and NumPy were available; python-flint,
SymPy, SciPy, psutil, Singular, and msolve were not. An isolated pip installation
was attempted and failed with network-permission error WinError 10013. No local
wheel was found. Exact integer polynomial arithmetic and explicit tiny
determinants were used; the required flint general-rank engine was not replaced
silently. Consequently there was no new replay of the large s74 sampled ranks.

**RECORDED —** One numerical worker and one BLAS thread were used throughout.
Initial available RAM was 7.56 GB. Every numerical child entered a Windows Job
Object with a 768 MiB process-memory cap before arithmetic, and every PID and
launch bound was recorded. Two wall-clock gaps nevertheless exceeded the
requested elapsed bounds: the dimension run recorded 11,001.92 seconds against
600, and column 2 recorded 10,891.94 against 600. Their causes are unverified.
No time was subtracted from those totals. The first timeout design failed;
after repair the second child's absolute deadline saved a partial column, but
the parent's exit-code handling still allowed the already queued short columns
3 and 4 to run. That exit-code defect is now fixed. The elapsed pilot budget was
exceeded, and this report does **not** claim execution-budget compliance.
Details and original logs are retained in `timing_deviation.md`.

**RECORDED —** Final verification checked 1,127 computed entries versus 243
explicit missing entries, exact monomial weights, the nonzero integer minor,
its two prime reductions, sign/order replays, source indexing, and candidate
supports. It did not construct or use the permanent stage Q; therefore the
conditional 144/144 S4 Q cross-check was not triggered or claimed. No new
positive D cell or nonzero cubic permanent ideal was reported, so the additional
positive-result protocol was not invoked. The primary and stretch outcomes
remain open with the unconditional bounds stated at the beginning.
