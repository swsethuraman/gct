---
board_numbering: batch14
session_id: B14-05
model: gpt-6-astra
requested_reasoning_effort: xhigh
attribution: actual executing model; requested effort is not independently introspected
base_commit: 9898e56941a7665f231873481dae956f08509995
base_tree: cb688cd3fe454d638f3202e759e2eaa0c629739f
branch: b14-05-astra
---

# B14-05 preregistration

Registered 2026-09-12 UTC, before new mathematical measurements. The prepared
branch HEAD and peeled batch14-base commit/tree matched the frozen identities.
An unquoted PowerShell rev-parse HEAD^{tree} attempt misparsed; the authoritative
checks were git log -1 --format=%H and --format=%T batch14-base, plus HEAD.
No applicable AGENTS.md was found in the checkout or its parent chain.

## Questions and instruments

1. Prove transport (T), the first-row birth bound (B), and complete interpolation
(CI) with hypotheses and a common rational model. Index only valid conclusions.
2. Define mixed linear/cubic highest-weight brackets and spanning at degrees 13
and 14. Audit source pullback, scaling, and the conditional dimension inputs.
3. Decide whether raw horizontal-strip letter adjunction factors through the
source polynomial. Check dependence on representatives before calling it a
Pieri operator. If it fails, exhibit an exact counterexample and state a corrected
operator (where justified); do not claim the false identity.
4. Validate genuinely multidimensional source and destination spaces, aiming at
a small binary quartic case and the banked n=3 six-dimensional bracket basis and
s62/s73 integer vector. First-row adjunction and non-Cartan adjunction must be
reported separately. A Cartan-only check does not validate the non-Cartan rule.

Use stdlib integer and Fraction polynomial arithmetic, explicit permutations,
raising/lowering operators and small exact elimination. Read banked code before
reuse. Load banked coefficient data without rerunning historical drivers that
write into other sessions' paths. No 239-component census or large rank sweep.

## Already observed evidence, not blind predictions

The frozen board records a24=274, det rank=273, pad rank>=269, D in [-4,+1].
The sampled five-dimensional padded kernel is not five certified equations.
Historical dimension counts 73 and 159 and n=3 basis ranks 6 are recorded inputs,
not new predictions. No new mathematical pilot has run. Inspection suggests raw
adjunction may depend on which singleton columns are extended; this is an
unmeasured hypothesis. Expected fallback: T, B, CI and mixed conventions plus
an exact adjunction obstruction if representative-independence fails.

## Conventions

A=Q[c_alpha], c_alpha(f)=[s^alpha]f. House raising action:
E_ij c_alpha=(alpha_i+1)c_(alpha+e_i-e_j), alpha_j>0.
A valence n letter has m_alpha=alpha! c_alpha=n! times polar tensor entry.
Use separate factorials for each mixed letter type, separately symmetrize equal
types, and never permute linear and cubic letters together. Ordinary coefficients
and polar tensors must not be identified without scaling. u=c_(n,0,...,0),
msym_u=n!u. Resolve coefficient indices by explicit exponent tuples.
Stored matrices: vectors are rows, points are columns; relation columns K satisfy
A^T K=0. Every matrix includes values_are. Q arithmetic is authoritative; modular
comparisons use both 2147483647 and 2147483629 only after denominator checks.
Transported evaluation certificates include the points, u, and nonzero checks.
Input blob IDs and working-byte SHA256 are in results/b14_05/input_manifest.json.

## Controls and decision table

- T: explicit q62, q44 raising and nonzero checks; reject zero multiplier.
- CI: a complete small rational polynomial target, independent source arithmetic,
  exact left kernel, nonzero target minor; reject deficient/absent/mislabelled
  target, missing membership/dimension/input, wrong entry/point/scaling,
  denominator divisible by a checking prime, and incorrect kernel orientation.
- Mixed membership: exact small expansions, weight and raising checks. Deliberate
  tensor scaling error must fail comparison. Spanning of all fillings is a theorem,
  not evidence that an arbitrary bounded semistandard search is complete.
- Adjunction: compare raw extensions of equal source polynomials; reject a map
  if their images differ. Check a corrected binary operator independently by
  lowering/raising equations and coefficient identities. Validate linear mixing
  with non-diagonal invertible basis changes and reject a deliberately unmixed
  or misnormalized image. Record exactly which dimensions were proved.
- n=3: reuse the six integral coordinate columns to check rank, the recorded
  integer line, and first-row multiplication; do not promote sampled determinant
  vanishing to a new ideal-membership proof.

PASS requires every input and assertion reached. Each control is itself fed a
wrong input and must reject. Disagreement stops dependent claims and is retained.
Success is T/CI indexed, mixed conventions for both degrees, and a valid adjunction
statement with dimension>=2 checks. Substantive fallback is the same lemmas and
conventions, with a proved counterexample or precisely named unresolved operator.

## Bounded shared-host execution

Toolchain inspected: Python 3.12.14, Windows 11 build 26200, 20 logical CPUs;
numpy present, flint/sympy/scipy absent. No installation planned. Exact stdlib
elimination is suitable for the small matrices and explicitly permitted by the
launch's stdlib-host clarification. Do not materialize large weight spaces.
Adapt the banked Windows Job Object wrapper under session-specific names: one
worker, numerical library threads=1, per-process cap 512 MiB (at most 768 MiB
only by a committed addendum), each calculation <=300 s; n=3 coordinate audit
<=600 s. Record PID, physical memory, elapsed time, peak private memory and status.
Combinatorial expansions: max 1,000,000 literal permutation terms for new tiny
controls; banked n=3 812,851,200-term fresh expansions are excluded. At most 128
small filling trials, stop once a certified counterexample and a multidimensional
operator control are obtained. No external service, other-session dependency,
push, integration merge, or recurring work.

## Delivery

Proofs in docs/b14_05_transport.md, outcome in docs/b14_05_report.md; scripts and
certificates under analysis/b14_05* and results/b14_05*. Append new PROVED entries.
Commit intentional changes with actual-model Co-Authored-By trailer. Use the
repository checker before/after a named-branch bundle against the frozen base.
Deliver report, replay, bundle, part00 onward (all <=5 MB), bare-filename MD5 and
SHA256, manifest, verification logs in Batch14_Results/B14-05 outside the worktree.
Protected files and configuration stay untouched. No new positive D is expected.

## Addendum 2026-09-12 03:42 UTC, before n=3 arithmetic

The small control certified failure of raw adjunction at (12,4)_4 -> (14,6)_5,
with both dimensions two. The corrected binary average passed all coefficient
identities and basis mixing. This is now observed, not a new prediction.
For the banked n=3 check use s69 degree-12 and independently selected degree-13
integral chi matrices; use s73 representative arrays to multiply by 6u and solve
the exact 6x6 change of basis, verifying every coordinate, plus the s62 integer
line and s73 degree-13 integer line. Load NPZ using installed numpy only as an
array reader. No old build or fresh 812-million-term expansion will run. Banked
filling-to-coordinate expansions remain adopted; the new replay proves identities
of those supplied integer coordinate vectors. Extra input hashes are appended
to the manifest. The 600-second / 512-MiB n=3 bound remains. Record failure if
coordinate order compatibility cannot be justified; never assume identical indices.
