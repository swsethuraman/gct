# B15-05: tail-21 determinant pilot

Model: gpt-6-astra, xhigh reasoning, for this session. B14-06's inherited
bracket and point implementations retain their Claude Opus 5 attribution.
No additional agents were used. The worktree and branch are the assigned
existing B15-05 / b15-05-tail21. No worktree was created or replaced.

**REPLAYED_RANK_FLOOR: determinant rank at least 529 at both house
primes.** The generic control rank is 533. The fixed-cap pilot and fresh
geometric replay completed; the sufficient threshold 530 was not reached.
The resulting bound is i_det(d)<=4 and D(d)<=1 for all d>=15, with the
inherited premises below. This is neither a family exclusion nor a
positive D result. Four modular sampled kernel candidates per prime are
retained. The heavy lease was explicitly released after both jobs exited.

## Checked numerical findings

| Prime | Family | Points | Sample rank | Actual minor determinant |
|---|---|---|---|---|
| 2147483647 | GEN | 560 | 533 | 1828515817 |
| 2147483647 | DET | 600 | 529 | 1967323645 |
| 2147483629 | GEN | 560 | 533 | 1852112970 |
| 2147483629 | DET | 600 | 529 | 262406295 |

At both primes DET ranks at 520, 560 and 600 points were 520, 529 and
529. GEN reached 533 at 560 points. The run stopped at the preregistered
sample cap; no production extension or further resampling was requested.

The exported minors have sizes 533x533 (GEN) and 529x529 (DET). Fresh
replay regenerated **1,127,860 entries** from the explicit integral points
using a changed interpolation seed, matched every stored entry, and
reproduced the four displayed nonzero determinants. This certifies the
rank floors over Q via good modular reduction. It does not prove the
determinant rank is globally at most 529. Kernel candidates are checked
against all 600 sampled determinant points, in the 533-column ambient
basis defined by the generic pivots; none is asserted to vanish globally.

| Run | Exit | Wall seconds | Aggregate peak MiB |
|---|---|---|---|
| Fixed-cap pilot | 0 | 49.72475 | 119.1992 |
| Fresh geometric replay | 0 | 14.35940 | 53.6719 |

Combined numerical wall time was 64.08415 seconds. Replay used an
800-second cap after the pilot, within the original 900-second granted
window. No resource limit was reached. The final process checks found
neither recorded heavy PID present; the release and both start/exit
receipts are preserved in `results/b15_05/lease_release.json`.

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

A floor of 530 suffices. The attained floor 529 is not a positive result.
At degree 26 the inherited ambient multiplicity is 531, and the padded
coordinate upper bound supplied by three ideal vectors is 528. A stable
coordinate rank is never substituted into this finite calculation.
With the actual stable floor 529, the finite degree-26 statements are
m_det>=531-4=527 and m_pad<=531-3=528, hence D<=1.
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

The completed pilot used 600 determinant and 560 generic points per prime,
using 2147483647 and 2147483629. It exports actual nonzero square minors,
not just rank totals. The generic rank-533 columns define a basis for
sampled kernel candidates. Those finite-field candidates carry no global
ideal lower bound. Point counts and rank growth are saved every 40
points. The geometric replay reconstructs the selected sources and
points with a different interpolation seed, compares every minor entry,
then checks its determinant. It shares B14-06's evaluator; it is a fresh
geometric replay, not an independent mathematical implementation.

The preregistered maximum was 900 seconds and 1536 MiB per heavy job,
with one process and one BLAS thread. The grant placed pilot plus replay
within one 900-second window, which was respected. No production extension
was requested. The integrator owns the two-job host limit and the external
lease record. The driver refuses a heavy launch without slot 05 in that
record. The request, queue confirmation, grant, completion and release decisions
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
construction, finite weight/degree transport, q44's exact derivative,
the scoped exclusion predicates and all four geometric minors. No protected paper, shared theorem
index or canonical exclusion ledger was edited.

## Outstanding witness

The next sufficient missing witness is a rationally valid stable
determinant minor of size at least 530 at tail (21,2^7), with its explicit
points and source definitions. Alternatively, a fourth independent
global padded ideal vector already at degree 15 would give i_pad>=4
throughout the family by u-multiplication and combine with this floor
to exclude positive D. A fourth degree-13 reducible equation in the
accepted 39-dimensional source is impossible under the complete rank-36
result. The accepted receipt states i_red13=3; here its padded consequence
is only the lower bound i_pad13>=3. No padded upper bound is inferred from
the reducible interpolation. The alternative needs an independently
proved fourth padded direction at degree 15. The four sampled
determinant kernel candidates do not supply this padded witness.

Actual pencils, generic points, source definitions, complete sampled
matrices, minors and candidate kernels are retained in results/b15_05.
The proposed-exclusions file contains no proposals. Delivery helpers are run after
the final commit; their external manifest gives the exact head, tree,
bundle prerequisites and checksums. A packaging PASS checks delivery
integrity, not the inherited mathematical premises.
