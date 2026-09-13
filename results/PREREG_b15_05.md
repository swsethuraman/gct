# B15-05 preregistration: tail 21

Date: 2026-09-13. Model: gpt-6-astra, xhigh reasoning, for readiness,
proof, implementation, numerical review and delivery. Banked B14-06 code
retains its Claude Opus 5 attribution. No additional agents.

The existing worktree B15-05 on b15-05-tail21 is retained. HEAD and the
batch15-base commit are f365568d80d5f66fea2dd9342ff1998e1d866915; tree
aff6ca0921ec964cc8b7fcbd64bd5e5e9de9fbbd; annotated tag object
80209c13e9ae33bad8933cb47413bf7710c96cb1. All three were compared exactly.
READINESS.md and LEASES.json were read. No heavy lease is currently held.
Existing runtime and smoke logs are setup provenance and will not be staged.
No applicable AGENTS.md was found on the worktree ancestor chain.

## Inputs

SHA-256 below hashes the exact native bytes, including native line endings.

| Input | SHA-256 |
|---|---|
| analysis/b14_06_bracket.py | d67a78c39694b1d4229970fd1bec46213913935030afcfae5165d2697d68b493 |
| analysis/b14_06_points.py | 17f7b435ffe6dc796ed709c6fa554a43e804957e0b4986cb6361d20a41901aaf |
| results/b14_04/stable_summary.json | 41b24f86a738735387a2faf3a74973e86da4f4a92096c16ca4de945c04ad32f8 |
| results/b14_08/witnesses.json | bf69c9bfec4f71426fd30fa4fce2347cc276182affe9945393dfb8974468e7ff |
| results/b15_prep/transport_overlay.json | b594dcdae7b4b448039d705d6f15f319e245a0d2cf3636f8b08b15cbfc42b4df |

Read common preamble, accepted state, B15-05 brief, house wording,
B14-06 review and construction, B14-05 transport, B14-08 witness q44,
S57 Proposition S, canonical scoped ledger and CI73 acceptance receipt.
The ledger has no general exclusion for this nine-row quartic family;
the overlay explicitly leaves its degree-25 and degree-26 cells open.
Additional dependency hashes will accompany the result.

## Question and conventions

Quartic n=4, determinant size 4, stable V'=C^8, ambient slice C^9.
The original determinant and independent z*per3 live in C^16 (padding has
ten essential variables). Weight tail (21,2^7), weighted degree 35, full
partition (4d-35,21,2^7), d>=15. Polynomial-coordinate representation
convention is C[Sym^4 V*]=Sym(Sym^4 V). We evaluate the two-epsilon
highest-weight brackets in C[Sym^2 V'* + Sym^3 V'* + Sym^4 V'*].
Their conjugate tail is (8,8,1^19). Source columns are ordered (a,b,c,z)
brackets, rows are explicit points. Preserve c2!c3!c4! and the Laplace
sign (-1)^sum(a). Scalar/gradient/Hessian data obey Euler identities.

Can integral traceless 4x4 pencils produce a modular determinant rank
floor at least 530? Inherit a_inf=533. Then i_det_inf<=533-r_det and
Proposition S gives i_det(d)<=i_det_inf, including before stabilization.
The accepted three degree-13 equations times q44=12c0*c4-3c1*c3+c2^2
have degree 15 and weight (25,21,2^7); multiplying by u^(d-15),
u=24*c0, preserves three independent padded ideal vectors. Thus
D<=530-r_det. At degree 26 use a=531, U_pad=min(a,h_pad,a-3)=528
in the absence of a smaller certified h_pad bound. Never insert 533
into a finite coordinate calculation. No higher-degree pad=red assumption.

## Algorithm and controls

Count the explicit bracket list before evaluation. Use B14-06 evaluator
and integral family_DET with fixed family seeds from SHA-256, replacing
the historical process-dependent hash(family). Preserve actual pencil
matrices. Generic points are consistent symmetric jet triples with a
rational homogeneous-form construction. Both house primes 2147483647
and 2147483629 are planned; modular denominators are units and every
source is rational, so a nonzero minor is a characteristic-zero floor.

Small controls: known nonzero tail (2^8) equals 8!*det(N2); direct
epsilon contraction in dimension 3; factorial/sign alteration detects
disagreement; DET versus normalized/depressed DETQ jets with a scalar
shift; Euler consistency including defective data; deterministic seed
repeat; empty/over-ambient rank rejection; exact raising derivative of
q44. All failed controls exit nonzero. The research rank may be zero.

With a lease, evaluate batches up to 600 determinant and 560 generic
points per prime, checking incremental ranks and exporting actual
nonzero minors. Use a generic rank-533 subset as a source basis when
available. Retain modular sampled kernels in that basis if rank<=529;
they are candidates only. Replay selected minors from explicit geometric
points separately from stored-matrix arithmetic. Stop the bounded pilot
at the fixed point cap or resource limit; do not repeatedly resample a
stable deficient rank. Disagreement between primes triggers diagnosis
and a nonzero exit, not an averaged claim.

## Resources and decisions

Exact local executable is B15-05/.venv/python.exe. All numerical runs use
analysis/b15_bound.py, one process and one BLAS thread. First run a new
30-second/512-MiB resource smoke with a unique b15_05 name, preserving
setup logs. Small algorithm controls are capped at 60 seconds/512 MiB.
No production without the integrator's heavy lease and a fresh lease
read. Request at most a 900-second, 1536-MiB pilot; budget changes require
measured justification and are recorded. Record construction, evaluation,
reduction, wall time, aggregate memory, exit codes and input hashes.

Success requires a replayed actual minor of size >=530, the inherited
ambient bound, and checked finite ideal transport. If rank<=529, report
the exact floor and next sufficient missing witness; it is not positive D.
On absent lease or resource stop, deliver proof, sizing, controls and
replayable construction without claiming the production floor.
Only per-slot files are changed; proposed exclusions remain separate.
First commit contains this preregistration only. Final delivery is an
unpushed one-ref delta bundle checked by the Batch15 helpers.
