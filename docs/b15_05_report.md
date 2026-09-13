# B15-05: tail-21 determinant pilot

Model: gpt-6-astra, xhigh reasoning, for this session. B14-06's inherited
bracket and point implementations retain their Claude Opus 5 attribution.
No additional agents were used. The worktree and branch are the assigned
existing B15-05 / b15-05-tail21. No worktree was created or replaced.

Current evidence status: **RECORDED**, awaiting the requested heavy
lease. Proof, source construction, sizing and small controls are complete.
No new family exclusion or positive D is claimed at this checkpoint.

## Question and sufficient bound

The family is n=4, degree d>=15, partition (4d-35,21,2^7). It has nine
rows. The original ambient has 16 variables, the highest-weight
restriction has nine, and the stable slice V' has eight. The stable tail
is (21,2^7), weighted degree 35, conjugate (8,8,1^19). Coordinate
functions follow C[Sym^4 V*]=Sym(Sym^4 V).

The inherited stable ambient multiplicity is 533. For any certified
stable determinant rank floor r, the finite ideal injection and three
transported padded equations give

    i_det(d) <= 533-r,   i_pad(d) >= 3,   D(d) <= 530-r.

A floor of 530 suffices. A floor of at most 529 is not a positive result.
At degree 26 the inherited ambient multiplicity is 531, and the padded
coordinate upper bound supplied by three ideal vectors is 528. A stable
coordinate rank is never substituted into this finite calculation.
`docs/b15_05_proved.md` contains the conditional all-degree proof and
separates its inherited premises from fresh arithmetic checks.

The exact scoped ledger and accepted-state overlay were applied before
the numerical work. Tail 21 is open in the supplied degree-25 and
degree-26 overlay records. Neither the length exclusions nor the peaked
quartic family match it. Independent padding means z*per3 with ten
essential variables. No degree-above-eight pad=red identity is used.

## Fresh controls and sizing

The new resource smoke passed. The algorithm control ran in 1.102 seconds
with aggregate peak 71,434,240 bytes (68.125 MiB), one process and one
BLAS thread. Its 18 checks passed, including known determinant liveness
at tail (2^8), direct epsilon contraction, factorial and sign defects,
Euler consistency, shifted DETQ normalization, reproducible family seeds,
empty-matrix rejection, ambient-rank rejection and exact q44 raising.
The research rank is permitted to be zero. The small three-point
tail-21 determinant matrix had rank 3; it is an instrument control, not
the planned saturation result.

Finite transport and scoped-ledger checks passed separately in 1.362
seconds. The intentional altered-value control exited 1 with the expected
disagreement message in 0.272 seconds. Its nonzero exit is the successful
negative-control outcome. All runs used the tested Windows Job Object
wrapper; no existing setup logs were included as research evidence.

Exact enumeration gives 1,887 double-epsilon brackets before swap
deduplication and 1,337 after it, in 14 patterns. A 600-point uint32
evaluation matrix needs 3,208,800 bytes, and all 600 integral pencil
points need 614,400 bytes as int64 data. These counts concern the
explicit bracket spanning set, not a stabilizer quotient estimate for a
weight-space carrier. Three-point timings were 0.0226 seconds for point
construction, 0.0471 seconds for evaluation and 0.00282 seconds for rank
reduction. NumPy 2.4.6 and python-flint 0.9.0 are available and used.

## Implementation and resource decisions

`analysis/b15_05_tail21.py` adds a per-slot driver around the banked
source/evaluator. It uses SHA-256 family seeds in place of the historical
process-dependent hash(family). It preserves bracket order, factorials,
Laplace signs, source orientation, rational tensor normalization and
explicit integral points. Every point passes Euler and symmetry checks.
Generic control points have a complete integral homogeneous-form
construction, rather than independent inconsistent scalar/gradient data.

The pilot is fixed at 600 determinant and 560 generic points per prime,
using 2147483647 and 2147483629. It exports actual nonzero square minors,
not just rank totals. The generic rank-533 columns define a basis for
sampled kernel candidates. Those finite-field candidates carry no global
ideal lower bound. Point counts and rank growth are saved every 40
points. The geometric replay reconstructs the selected sources and
points with a different interpolation seed, compares every minor entry,
then checks its determinant. It shares B14-06's evaluator; it is a fresh
geometric replay, not an independent mathematical implementation.

The preregistered maximum is 900 seconds and 1536 MiB per heavy job,
with one process and one BLAS thread. No production extension has been
requested. The integrator owns the two-job host limit and the external
lease record. The driver refuses a heavy launch without slot 05 in that
record. The request, queue confirmation and later resource decisions
are recorded in `results/b15_05/resource_decisions.json`.

## Provenance and replay

The frozen base commit, tree and annotated tag were compared exactly:

- Commit: f365568d80d5f66fea2dd9342ff1998e1d866915.
- Tree: aff6ca0921ec964cc8b7fcbd64bd5e5e9de9fbbd.
- Tag object: 80209c13e9ae33bad8933cb47413bf7710c96cb1.
- Preregistration commit: 58ca7a69e320064de8272f9cee6c6230fcad2f05.

Exact native-byte input SHA-256 hashes are in `controls.json`; these
include native line endings. `results/b15_05/README.md` gives replay
commands with the required local Python executable. Return codes,
start times, wall times and aggregate peaks are in the uniquely named
`results/logs/b15_05_*_resources.json` research receipts. The pre-existing
runtime-native and b15_00 smoke receipts remain setup provenance.

Inherited rather than freshly evaluated here: the 533 stable ambient
dimension, degree-26 ambient 531, three degree-13 global equations and
their complete interpolation proof, and the S57 stable-slice theorem.
Freshly checked: all controls above, source enumeration, point
construction, finite weight/degree transport, q44's exact derivative and
the scoped exclusion predicates. No protected paper, shared theorem
index or canonical exclusion ledger was edited.

## Outstanding witness

The next sufficient missing witness is a rationally valid stable
determinant minor of size at least 530 at tail (21,2^7), with its explicit
points and source definitions. The bounded pilot and geometric replay
are prepared to check that witness after the integrator grants a lease.
