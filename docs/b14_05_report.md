---
board_numbering: batch14
session_id: B14-05
actual_model: gpt-6-astra
requested_reasoning_effort: xhigh
branch: b14-05-astra
base_commit: 9898e56941a7665f231873481dae956f08509995
base_tree: cb688cd3fe454d638f3202e759e2eaa0c629739f
---

# B14-05: the lemmas hold; raw adjunction needs correction

**RECORDED — Delivery contains one bundle part, `part00`, plus the whole named-branch
bundle.** Lemmas T and CI are proved and indexed, and mixed-target membership and
spanning conventions are fixed at degrees 13 and 14. The proposed raw adjunction
identity is false: equal source polynomials can acquire different images. This
session supplies an exact counterexample, proves a corrected binary averaging
operator, and validates first-row transport across the banked six-dimensional
n=3 spaces. This is the substantive fallback with an exact mathematical
obstruction, rather than a proof of the false general identity.

**ADOPTED / OPEN — LMR is unchanged:** a24=274, determinant rank 273, padded
rank at least 269, and D in [-4,+1]. No new value of i_red or i_pad is claimed.
Five sampled padded kernel vectors remain five sampled vectors, not five
certified equations.

## Results that can now be used

**PROVED — Transport T and birth bound B.** A nonzero ambient HWV multiplies
every ideal HW space injectively into its Cartan sum weight. No quotient
nonvanishing assumption is needed for that ideal injection. The coordinate-ring
injection and upper bound by the ambient dimension increment require a regular
residue; an irreducible variety and a nonzero residue suffice. All genuine LMR
padded equations consequently survive q62 and q44 transport. First-row u
transport gives the birth bound and equality across flat ambient steps.

**PROVED — Complete interpolation CI.** A justified target dimension, genuine
members with a full target minor, proved source pullback inclusion, a complete
source basis and exact rational source arithmetic make the sampled source
kernel the true restriction kernel. Source vectors are rows, points are columns,
and relation columns K satisfy A^T K=0. Modular target minors are rank floors
over Q only after checking the common rational model and denominators. The
abstract two-dimensional control has rank two and kernel y2-2y1; it is not a
certificate for either LMR rung.

**PROVED — Mixed targets.** At d=13 and 14 use d distinct formal linear letters
of valence one and d cubic letters of valence three, separately symmetrized
within types, with m_alpha=alpha!c_alpha. Initial-column bracket sums give genuine
members, and the full family spans the desired HW space. The column shapes
are (9,9,2^15,1^4) and (9,9,2^15,1^8). The ordinary quartic pullback is exactly
the sum of all 4^d mixed slot splits; there is no additional averaging factor.
The proof is independent of non-Cartan adjunction.

**RECORDED / ADOPTED — Dimension inputs.** The target dimension formula is
stated; numerical dimensions 73 and 159 are inherited, with two counting routes
recorded in the frozen board. This session does not duplicate slot 04's recount.
The source contract audit verifies 39 rows through degree 13 and 93 through
degree 14. Those counts alone do not reprove basis completeness.

**PROVED + CERTIFIED — Raw adjunction counterexample.** For binary quartics,
the source (12,4)_4 and destination (14,6)_5 both have HW dimension two. Two
fillings differing only by singleton order both give
576(8c0c2-3c1^2)^2. Extending columns 5 and 6 and adding singleton columns 13
and 14 gives values 0 and 497664 at f=s1^4+s1*s2^3. The proof note gives a
one-surviving-assignment derivation; the certificate also retains the complete
polynomial difference. Hence raw extension fails to respect a source relation.
Checking highest weight or a single basis direction would miss this defect.

**PROVED + CERTIFIED — Corrected binary operator.** Averaging over all eligible
singleton columns equals (n-k)!k! times the explicitly normalized Pieri
operator written with E21. At n=4,k=2 this is checked on a full two-dimensional
source basis; its two images are independent. All polynomial coefficients
agree under a non-diagonal source basis change. A missing normalization factor
and unchanged target coordinates are rejected.

**PROVED + CERTIFIED coordinate replay — n=3 first-row transport.** Literal
adjunction is J=6u. Across the independently selected six-row s69 bases, the
exact conversion matrix has determinant 5/12, and all 103836 destination
coordinates agree. Both supplied coordinate matrices have exact rank six, also
six at both house primes. The combination
(66,-972,12,-37,4,320) of source rows equals -29859840 times the s62 integer
vector; u times that vector equals the s73 degree-13 integer vector exactly.
The banked filling expansions and ambient upper counts are adopted. This replay
does not rebuild their large raising matrices or freshly prove ideal membership.

**RECORDED — Proof index.** Seven entries were appended to PROVED.md:
`transport_lemma_T`, `birth_bound_B`, `complete_interpolation`,
`mixed_bracket_targets_13_14`, `raw_bracket_adjunction_false`,
`binary_averaged_adjunction`, and `first_row_bracket_adjunction`.
No unconditional new cell exclusion was established, so no machine exclusion
predicate was added. Existing index entries and protected files were preserved.

## Exact validation and resource evidence

**CERTIFIED — 36 deliberate corruptions rejected.** The released small controls
reject 24 wrong inputs, n=3 rejects six, and the point audit rejects six. Cases
include missing targets/source data, invalid target membership, a deficient
target, an altered integer entry, wrong point/scaling, transposed or false
kernel, a denominator divisible by either house prime, incorrect raising
cancellation, dependent rank witnesses, an unmixed basis and a zero-u point.
Checks raise errors when assertions fail; absent data cannot become PASS.

**CERTIFIED arithmetic audit, not an evaluation certificate.** All 116 stored
P13 points (96 primary plus 20 holdout) and 212 P14 points (192 plus 20) have
their u values recomputed from explicit exponent tuples; u and 24u are recorded
and nonzero at both primes. Their frozen files carry the complete point definitions.
The audit also verifies all required blob contracts and reads the full 336-row
B13-06 tensor-domain input. It does not repeat slot 08's 239-component census.

**MEASURED — Released runs on the shared Windows host.**

| Calculation | Wall seconds | Peak private process bytes | Enforced bounds |
|---|---:|---:|---|
| Exact binary/mixed/CI controls | 0.031 | 14,532,608 | 300 s / 512 MiB |
| n=3 integer coordinate replay | 1.266 | 77,086,720 | 600 s / 512 MiB |
| Frozen input and point audit | 0.953 | 35,889,152 | 300 s / 512 MiB |

**RECORDED.** Python 3.12.14 on Windows 11, 20 logical CPUs; physical memory
33,752,997,888 bytes, with about 12.8–13.6 GB available at these launches.
One worker ran at a time and numerical library thread limits were one. Algebra
uses stdlib integers/Fractions; installed numpy only loads the n=3 NPZ arrays.
flint, sympy and scipy are absent; no packages were installed. A session-specific
adaptation of the banked Windows Job Object wrapper enforces memory and wall
bounds and records PIDs. No calculation reached a resource limit. All pilot
and release logs are retained; released measurements above match their resource
JSON files. The initial preregistration commit is af1198b5, before mathematical
measurements; later scoped addenda were committed before their measurements.

## Limits, assignment defects, and next work

**PROVED defect in the brief.** The general identity F_(T')=Phi_nu(F_T) assumes
that a raw operation on fillings respects all source relations. It does not.
A fixed strip and a global scalar cannot repair the exhibited failure.
The corrected general definition uses a chosen normalized highest-weight Pieri
tensor followed by multiplication; constructing those coupled tensors for the
n=4 non-Cartan strips remains OPEN. First-row validation, even in dimension six,
does not validate these other strips. A future implementation must pass a
representative-independence test and a comparison of multiple basis directions.

**NOT REACHED / OPEN.** There is no degree-13 or degree-14 full mixed target
minor, exact LMR source matrix, complete-interpolation certificate, or higher-rank
non-Cartan operator implementation in this delivery. These are separate inputs
owned by the designated slots. No time was spent waiting for them. Literal
fresh n=3 expansion would have 812851200 terms per filling and was excluded at
preregistration; higher-rank expansion is still larger. The next bounded operator
pilot should use one selected non-Cartan strip with a 300-second / 512-MiB cap;
its runtime is unmeasured, not estimated from the first-row check.

**CONDITIONAL — What could decide LMR next.** An accepted CI certificate with
i_red(13)>=1 would imply D<=0 at LMR. One with i_red(14)=5 would imply D=-4
using the adopted padded rank floor. The new mixed conventions support that
route despite the adjunction counterexample.

**RECORDED — Attribution and delivery.** Actual executing model: gpt-6-astra;
xhigh was requested by the launch, and no independent effort-setting introspection
was exposed. No subagents ran. Base and tag identities match the header;
the final head/tree, exact bundle prerequisite refs, output hashes, size and
verification statuses are captured in the external delivery manifest, avoiding
a self-referential commit hash in this report. The repository delivery checker
must be CLEAN both before and after bundling; its actual output is delivered.
The package includes a named refs/heads/b14-05-astra bundle, part00, report,
proof note, replay instructions, exact JSON certificates and resource logs.
No push, integration merge, external message or recurring work was performed.

**RECORDED — Absolute delivery directory:**
`C:\Users\swami\Projects\gct-gpt\Batch14_Results\B14-05`.
The committed proof and replay files are `docs/b14_05_transport.md` and
`results/b14_05/REPLAY.md` on the isolated branch.
