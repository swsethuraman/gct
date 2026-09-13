# B15-01 preregistration

Date: 2026-09-13. Model for planning, implementation, analysis and reporting:
gpt-6-astra (Codex); xhigh requested by dispatch. No other live model or agent.
Banked B14-07 code and source arithmetic retain Claude Opus 5 attribution.

Existing checkout: B15-01; branch b15-01-ci159. Before work, HEAD and the
resolved annotated batch15-base commit both equal
f365568d80d5f66fea2dd9342ff1998e1d866915; the resolved tree is
aff6ca0921ec964cc8b7fcbd64bd5e5e9de9fbbd and the tag object is
80209c13e9ae33bad8933cb47413bf7710c96cb1. No checkout was created or changed.
READINESS.md reports native runtime PASS. LEASES.json grants slot 01 one
initial heavy lease; at most one numerical job will run here at a time.
Pre-existing setup logs are preserved and excluded from this registration.

## Question and conventions

Over Q, n=4, degree14, nine evaluation variables, weight (25,17,2,2,2,2,2,2,2):
does evaluation separate the full normalization space
N14 = HW_lambda(Sym^14 V tensor Sym^14(Sym^3 V)), of proposed dimension159?
Can this prove that the five rational sampled source relations are global
equations of the reducible closure R = closure{ell*c}?

The source comprises 93 native S74 fillings, transported by
u^(14-native_degree), u=24*c_(4,0^8). Preserve all indices, including the first
39, and every factorial coefficient alpha!*c_alpha. Source rows, point
columns; relation columns satisfy A^T K=0. No rational rescaling is introduced.
P14 supplies 192 primary plus 20 holdout integral reducible points. New points,
if needed, require fresh exact source values. Ambient multiplicity a, ideal
multiplicity i, coordinate multiplicity m, and normalization dimension h are
distinct. True padding is an independent z times per3 in ten essential
variables; this work uses P contained in R and does not assume m_pad=m_red
in degree14.

Apply ACCEPTED_STATE.md over historical claims. Degree13 already proves three
relations. At degree24, inherited a=274, m_det=273 and m_pad>=269 imply
i_pad<=5 and D=1-i_pad in [-4,-2]. In that cell U_pad=min(274,h_pad,274-3,
other valid bounds) <=271, already below r_det=273. No positive search is
authorized. Five independent equations transported by u^10 would give D=-4;
four give D<=-3. The scoped ledger is read without modification.

## Frozen input identities

SHA256 of actual working bytes (including their existing line endings):

| Path | SHA256 |
|---|---|
| analysis/b14_07_source14.py | 1192e298b69bcc16246f01c6dcd50c7b69094341dcc9262823cf5e59242ab3b9 |
| analysis/b14_07_kernel.py | e4c3e382e4270f3b796b1151190f99cddf5f6cbb99c12e659dd0fdbf3a175a9a |
| results/b14_07/K14.json | eef4e41c7bc5bccc7a70b5b95ee59b7ccee018d412474729d6ed6daa518ceee3 |
| results/b14_07/A14_exact.json.gz | 68a555cd11c566a8ed8dfe0fe87dff1bb1427a96165d8f493684b3bcea7a241d |
| results/b14_04/hpad14.json | 0d2eb2f3bca7cbb85a911a3c8f2ff70312d724462710af76c1ce9e83d09c4b65 |
| results/b15_prep/degree14_target_seed88.json | 537211d435562d0766beb3d8aec63e8172b47a0e95da7af0e007274f8c956c79 |
| results/ci73/certificate.json | 8f4d168ecfb922213b5baee66ac6250dd99dcf2ace669eebc2426c782e9b231d |
| docs/ci73_proof.md | 644acd3aaf603e1200e77c5be9b0ccb73b8b312d4f63cff7ed6205fc25475b81 |

Additional dependencies will be hashed before use: S74 source and generic
points, P14, degree13 mixed definitions and equations, accepted CI73 evaluator,
C# backend, exact dimension routines, accepted-state and scoped ledger.

## Algorithm and controls

1. Recompute h14 by exact Newton power-sum recurrence, independent outer-rim
Murnaghan--Nakayama characters and complete Pieri interlacing. Check small
character orthogonality and the complete channel list. Recompute a14 if
resources permit; do not infer it from a sampled source rank.
2. Recheck the exact stored A14 left-kernel identities, rank5 of K and rank88
of A, and its first39 comparison with the accepted degree13 kernel. Label this
stored arithmetic separately from geometric replay. Re-derive H14 and the
seven-prime signed margin. Check source definitions and seed membership.
3. Pass small literal-Leibniz versus C# mixed and quartic controls over integers
and both house primes. Require a known nonzero liveness example. Reverse a
column, alter a coefficient/factorial, alter a point and alter a kernel entry;
the relevant checks must detect the defects. Allow research members to vanish.
4. Extend the source-pullback seed first by the 72 degree13 mixed members
multiplied by ell_0*m_(3,0^8)(c), a nonzero highest-weight factor of bidegree
(1,1), weight (4). This factor is u(ell*c)/4. Then construct degree14 mixed
brackets by explicitly exchanging singleton occurrences of the added cubic
or linear letter with compatible existing column occurrences, preserving
valences and column distinctness. Count and plan before numerical allocation.
Retain full definitions for every accepted row, deterministic candidate order,
point IDs, residues and minor indices. These are explicit genuine members,
not a claimed spanning list. No sampled zero-pruning establishes completeness.
5. Use the CI73 independently implemented evaluator/backend with slot-specific
output/cache paths. Evaluate existing P14 primary points modulo the house
prime, measure construction/planning, evaluation and reduction separately,
and checkpoint after each added direction. If rank159 is attained, obtain a
full minor, fresh source values with exact signed reconstruction, rational
identities, source completeness, and independent replay. The stock verifier
is currently degree13-specific; any degree14 extension must be explicit and
validated, not described as existing acceptance.

## Resource envelope and decision rules

Use exactly the worker .venv/python.exe and analysis/b15_bound.py. One process
and BLAS thread; sequential C# child contraction inside the same aggregate
Windows Job Object; 1536 MiB cap. Run small controls first, then a 900-second
pilot, checkpointing before its deadline. Check LEASES.json and available RAM
before heavy work. Record PID, UTC start, exit code, wall time and aggregate
peak commitment. No child cleanup outside a verified slot-specific directory.

Stop on failed controls, inconsistent definitions/normalization, resource cap,
or insufficient remaining pilot time. Report actual added rank and seconds per
direction. A measured productive method may justify one <=5400-second
production attempt under the same lease and memory cap; record the decision
before extending. If the proposed moves stall, report that bounded family,
not an exhaustive search, and give the next sufficient witness.

Rank159 plus all CI premises establishes five equations; rank158 permits the
partial-interpolation lower bound4. General partial rank r gives
i_red>=max(0,5-(159-r)), subject to exact source and membership premises;
combine with the existing lower bound3. Lower ranks are infrastructure only.
Statuses: EXACT, REPLAYED_RANK_FLOOR, RECORDED, CANDIDATE, RESOURCE_STOP.
All proposed theorem/exclusion records remain per-slot. Every new tracked
artifact is below5,000,000 bytes; final commits precede delivery checks and the
one-ref delta bundle. No push or publication.
