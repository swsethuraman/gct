---
board_numbering: batch13
session_id: B13-07
model: gpt-6-astra
reasoning_effort: xhigh
base_commit: 00495110c62acfbbbc951e82cc218ed091563b3f
branch: b13-07
delivery_parts: 1
status: verified_prefix_and_precise_bounded_fallback
---

# B13-07 — independent S79 audit

**RECORDED.** Delivery has **one part, `part00`**, in addition to the whole
`b13_07_s79_audit.bundle`; both have MD5 and SHA256 checksums naming bare
filenames. This single execution used **GPT-6 Astra (`gpt-6-astra`, xhigh)**,
also confirmed by the automation configuration. Work stayed on the prepared
isolated branch at the frozen base. No history was rewritten. No publication,
push, global Git configuration change, or follow-up schedule was made.

**RECORDED — outcome.** The board's bounded fallback is delivered: an exact
inherited proof, all sixteen stable blocks replayed, a complete census and
record audit, and a precisely enumerated certificate-regeneration boundary.
This is not a fresh independent certification of every S79 rank. All **46
available degree-nine full-rank certificates, covering 23 weights at both
primes**, pass; the other **187 weights** remain adopted from S79's record.

## Claim ledger

| Claim | Audit result | Evidence and scope |
|---|---|---|
| Five-variable permanent dominance | **CERTIFIED; PROVED consequence** | Exact 35-by-45 Jacobian, two nonzero 35-minors, integer determinants, all 45 derivative columns checked by exact finite differences |
| Every shorter cubic weight is excluded | **PROVED** | Dominance plus the support/restriction argument below; no 365-weight rank recomputation |
| Degree-nine ambient census | **CERTIFIED** | 331 six-part candidates; 210 positive weights, sum 592, maximum 9; 365 shorter positive weights, sum 1213 |
| All 210 records say full rank at both primes | **RECORDED, consistency verified** | Explicit prime-key checks and hybrid projected-nullity, verification, and rank fields, rather than a `primes_agree` flag alone |
| Independent degree-nine rank replay | **CERTIFIED on 23 weights** | 46 source, raising, point and rank replays; precise remaining 187 in `coverage.json` |
| Full `I(D_6^{per_3})_9=0` | **ADOPTED on the remaining rank inputs** | The shorter-weight dependency is now proved explicitly; missing long-weight certificates limit this audit's independent replay, not the logical inheritance |
| Sixteen positive stable blocks with `a_inf<=4` | **CERTIFIED** | Both primes, all source monomials, every raising image, integer-pencil evaluations, ranks and altered-vector controls |
| Completeness of that stable range | **CERTIFIED** | All 57 partitions of 13 with length at most five enumerated; counts at `a_inf=0,1,2,3,4` are `10,4,5,2,5` |
| Stable exclusions at every ladder degree | **PROVED given those certificates** | The dehomogenisation injection of Proposition S, reviewed below |
| Full determinant rank in 682 quartic cells | **ADOPTED certification; all records checked** | Both prime entries agree with `a`; this run did not rebuild 682 source/evaluation matrices |
| Padded/reducible deficient ranks | **MEASURED** | 59 deficiencies; 24 at degrees at most nine and **35 at degrees 10–12** |
| 69 first-stable Q1 cells, 63 tails | **RECORDED, cross-checked** | Join to the frozen Q1 queue; all four recorded ranks equal `a=a_inf` |
| `epsilon_pad=0` over Q | **NOT ESTABLISHED; conditional retained** | Modular birth coefficients replay to zero; a concrete integer counterexample invalidates the general inference |
| LMR determinant rank 273, padded floor 269 | **ADOPTED exact determinant result; padded floor replayed** | Preserve `D=mult_pad-mult_det=1-i_pad(24)` and `-4<=D<=1` |

## Exact inherited dependency

**CERTIFIED.** The s37 point was recovered from its actual generator:
`random.Random(20260902*1000+5)`, five row-major 3-by-3 integer matrices in
`[-1000000,1000000]`. For a parameter `A_k[a,b]`, the derivative is `s_k`
times the complementary 2-by-2 permanent. Independently, each entry parameter
occurs at most linearly in the permanent, so exact substitution at `A+1`
minus substitution at `A` equals that derivative. All 45 full coefficient
vectors agree over Z. The Jacobian has 35 coefficient rows and 45 parameter
columns; the delivered JSON stores its transpose, with the convention beside
the numbers. The two minor residues are **1263013162** at 2147483647 and
**1627206724** at 2147483629. Bareiss elimination also supplies the actual
nonzero integer determinant. The zero-Jacobian control has rank zero.

**PROVED.** The image closure of this polynomial map is irreducible. In
characteristic zero its dimension is the generic differential rank, so one
full-rank point proves `D_5^{per_3}=Sym^3 C^5`. Restricting the output to
fewer coordinates gives dominance for every `k<=5`.

**PROVED.** If a highest-weight polynomial has weight `mu` of length `k`,
each coordinate monomial in it has sum of nonnegative exponent vectors
equal to `mu`. All factors therefore use only the first `k` variables.
Its value on a six-variable cubic equals its value on that cubic's
restriction to those variables. The restrictions of `D_6^{per_3}` are
dense in `D_k^{per_3}=Sym^3 C^k`. An ideal vector at such a weight must thus
be the zero polynomial. This proves the missing declared dependency at
**every degree**, not just degree nine. The 365 shorter constituents require
no new evaluation. Their counts by length are `1,11,48,117,188`.

**ADOPTED/PROVED distinction.** Combining this argument with the full-rank
inputs for all 210 six-row constituents proves the full degree-nine ideal
statement. This run independently replays 23 of those constituents and
audits the recorded evidence for all 210. It therefore retains the full
statement as adopted, with its inherited mathematical dependency verified.
The transfer to padded/reducible equality at degree nine uses Proposition 8
of `docs/transfer_lemma.md`; equality alone is not a prerequisite for `D>0`.

## Source arithmetic and stable exclusions

**PROVED — lifting justification.** The relevant polynomial representations
have total tensor degree 27 for the cubic census and 13 for the stable
spaces. Both house primes exceed these degrees. Over the localization of Z
at either prime, symmetrizers for all tensor permutations and Young
symmetrizers have invertible factorial/hook denominators. Schur-Weyl
decomposition therefore identifies the characteristic-zero highest-weight
lattice and its reduction with the same multiplicity spaces. Equivalently,
the Schur algebra in polynomial degree less than the characteristic is
semisimple. Simple-root infinitesimal invariance equals root-group
invariance here: the exponential expansion terminates before the prime,
so all its factorial denominators are units. Thus a full set of modular
highest-weight vectors with independent evaluations certifies injectivity
on the rational highest-weight space. This explains the lifting step; merely
counting supplied vectors would not be an upper bound on an arbitrary
modular kernel.

**CERTIFIED.** Cubic replay uses `tools/verify/hwv.py` and its independent
point-expansion modules, not S79's hybrid builder. It validates the declared
plain coefficient convention, each term's exact degree and weight, every
simple raising image without omitting targets, and the reconstructed
permanent pencils. Full evaluation rank also proves independence of the
supplied vectors. A deliberately wrong weight is rejected for each file.

**CERTIFIED.** Stable replay calls the integrator's independent enumeration,
Weyl-count and principal-minor functions, with this session's rank routine
and additional independence and altered-vector checks. This is independent
of S79 production, not a claim to have invented a third complete evaluator.
The generator ordering is detected and every source monomial is checked.
Every pencil is traceless. Principal-minor values use `e_d`; S79 stores
`(-1)^d e_d`. Since total weight is 13, **every evaluation differs by exactly
one global minus sign**, checked entry by entry. Nothing is silently skipped.
All 16 records, including the 11 inherited calibration blocks, pass at both
primes. The largest source has 12,479 monomials.

**PROVED.** The load-bearing part of Proposition S is sound: localize at the
leading quartic coefficient `c`, normalize `c=1`, and remove the cubic-in-
`s_1` term by the unique shift `s_1 -> s_1-g_1/4`. This gives the global
unipotent slice `Z=Sym^2 V' + Sym^3 V' + Sym^4 V'`. Restriction injects each
homogeneous highest-weight space into its fixed tail-weight space in
`C[Z]`. For determinant pencils, normalizing the first invertible matrix
and subtracting the trace gives exactly the traceless-pencil image closure.
An equation on a ladder would consequently yield a nonzero stable equation.
The verified zero stable ideals exclude every valid degree of these sixteen
ladders. This argument does not need the separate dimension formula appended
to Proposition S, which was not independently audited here.

## The rational birth question remains conditional

**MEASURED.** From the delivered padded points I recomputed every
`u=24[s_1^4]f`, checked all 282 values at each prime, verified that none is
zero, and applied `u^(24-rung)` to the native rows. This gives rank 269;
the first 273 transported rows have modular rank 268; all five kernel
vectors have birth coordinate zero. Native values were read as native,
not mistaken for transported rows. This replay does not reevaluate all
274 bracket polynomials from scratch.

**PROVED — the inference is insufficient.** Put
`q=2147483647*2147483629=4611685975477714963`. In a two-dimensional source
with old subspace `span(e_0)`, take evaluation matrix `[q,1]`. At both primes
its kernel is `span(e_0)`, so every modular kernel vector has zero birth
coordinate. Over Q its primitive kernel vector is `(1,-q)`, whose birth
coordinate is nonzero. Thus the precise finite-prime inference fails even
for an integer matrix, a primitive kernel vector, and an independent ambient
source. This is a counterexample to the argument, **not** a counterexample
about the actual padded variety.

**RECORDED — exact task still needed.** Supply a rational functional on the
restriction image that annihilates `uM_23` and does not annihilate the birth,
or otherwise prove `I(P) intersect M_24` lies in `uM_23`. One sufficient
certificate would be an integer padded point with `u=0` and nonzero value
of the degree-24 native birth; no such point was evaluated or found in this
run. Another route is a rational row-space certificate for actual integer
evaluation matrices with a justified old-row rank upper bound. The existing
269-minor is a lower bound and cannot supply that upper bound. A cost for
the latter symbolic calculation is unresolved; its finite source has 274
rows, of which 273 are old. The compact evaluator needs a native Windows
build and its flint dependency for the first route.

**PROVED conditional on the missing containment.** Irreducibility of `P`
and `u` nonzero on `P` give `ug in I(P)` iff `g in I(P)`. Together with the
birth-quotient proposition this would imply `i_pad(24)=i_pad(23)`. Until
then retain `epsilon_pad in {0,1}` and use the unconditional formula
`D=1-i_pad(24)`. No exact value of `i_red` or `D=-4` is claimed.

## Delivery defects, corrections and costed handoff

**RECORDED.** The original S79 transport bundle is not present in this
isolated checkout; the final merged artefacts are. All **1,200** files marked
shipped in its **2,066-file** manifest exist and match size and MD5. Another
**29** files marked unshipped are present but differ from the final manifest;
all are supplemental calibration objects. There are **837** absent listed
files. I recorded actual SHA256 and canonical JSON SHA256 for the 29
supplemental objects. The final original bytes are unavailable, so gzip
timestamp variation is not asserted as the explanation and these files are
not silently treated as hash-verified final certificates.

**RECORDED correction.** S79's final boundary paragraph says 31 sampled
drop comparisons at degree at least ten. That counts Q2 alone. Q1 contributes
four more, so the total is **35**: 15 at degree ten, 12 at eleven, 8 at twelve.
The four Q1 cells are listed explicitly in `coverage.json`. The total 59
deficiencies and all 682 determinant-full records agree with the board.
The determinant result alone implies `D<=0` in those cells; no positive
reducible ideal dimension is needed. Several older prose conclusions about
permanent invisibility remain stronger than sampled equality warrants;
the corrected board controls this report.

**RECORDED fallback.** The 187 unreplayed cubic weights split into **119**
with **238** omitted expanded certificates and **68** for which no expanded
certificate was written under the original size rule. `coverage.json`
lists every weight, multiplicity, original cost, missing state, and exact
driver arguments with isolated output paths. They cost **5,623.5 seconds**
in S79's recorded runs (about 94 minutes); this is a historical price, not
a Windows promise. The largest has `N_S=3,299,214` and
`N_S*delta=29,692,926`. Rebuilding needs flint/SciPy and a Windows-compatible
engine, or the original compatible environment. Large weights may require
compact replay certificates rather than expanded files exceeding 5 MB.
No other Batch 13 session is needed to specify or resume this work.

**RECORDED environment.** Python was not on PATH; the bundled runtime has
NumPy, but initial checks found no flint, SymPy, SciPy, psutil, Singular,
msolve or C compiler. A local-target dependency installation was attempted
and blocked by host socket policy (`WinError 10013`). WMI memory access was
also denied; native `GlobalMemoryStatusEx` worked. Exact stdlib arithmetic
and the existing independent NumPy checker were used instead of flint,
explicitly deviating from that tool preference without using floating-point
ranks. Two early runs failed on an omitted function argument and on the
supplemental manifest mismatch; both were diagnosed and retained in the logs.

**RECORDED resource control.** Every numerical launch used one worker, one
BLAS/OpenMP thread, a native Windows Job Object limit of 1.5 GiB, a recorded
PID and a supervisor wall limit. Actual job limits and memory at launch
are in `results/logs/b13_07_*_run.json`. Seventy bounded jobs consumed about
66 seconds of summed child wall time; the largest measured job commit peak
was **1,181,536,256 bytes**, during supplemental JSON canonicalization.
This is a Windows committed-memory measure, not RSS. No numerical job hit
its limit. Summed numerical time is distinct from elapsed session time.

**RECORDED replay.** On the frozen base plus this bundle, use the bundled
Python path (or an installed Python with NumPy):

```powershell
& $auditPython analysis/b13_07_run.py b13_07_replay_dominance 300 analysis/b13_07_audit.py dominance
& $auditPython analysis/b13_07_run.py b13_07_replay_census 1800 analysis/b13_07_audit.py census
& $auditPython analysis/b13_07_run.py b13_07_replay_stable 900 analysis/b13_07_audit.py stable results/s79_stable/stable_5_3_2_2_1.json
& $auditPython analysis/b13_07_run.py b13_07_replay_epsilon 600 analysis/b13_07_audit.py epsilon
```

**RECORDED.** Each original launch's exact arguments are in its run JSON.
`b13_07_batch.py` is the sequential original banking driver: it creates a
commit per completed weight/block, so use individual launch recipes when
only replaying. The delivery manifest records the final branch tip and
whole/part checksums; the tracked manifest binds reports, scripts, audit
outputs and their frozen input dependencies. No source file exceeds 5 MB.
