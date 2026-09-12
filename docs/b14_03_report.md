---
board_numbering: batch14
session_id: B14-03
model: gpt-6-astra
reasoning_effort: xhigh
status: core success - complete exact interpolation control
base: 9898e56941a7665f231873481dae956f08509995
base_tree: cb688cd3fe454d638f3202e759e2eaa0c629739f
branch: b14-03-astra
bundle_parts: 1
---

# B14-03: complete interpolation verifier

**CERTIFIED / RECORDED.** This delivery has **one part, part00**, accompanying
`b14_03_astra.bundle`, with whole-file and per-part MD5/SHA256 checksums. The
core assignment is complete: a proved complete-interpolation contract, an
independent checker integrated into the normal verifier, an accepted complete
h=1 control, and all named rejection tests. The final named branch head/tree,
bundle prerequisites and delivery-check outcomes are recorded in the adjacent
delivery `manifest.json` and verification logs, avoiding a self-referential
commit hash in this report.

**CERTIFIED.** For ternary quartics, coefficient degree 6, weight (8,8,8), the
complete source dimension is **2**, the mixed target dimension is **1**, the
reducible restriction rank is **1**, and **i_red=1**. The checker reconstructs
the target from eight determinant columns, proves its membership, independently
justifies the dimension and checks a nonzero full target minor. All source
arithmetic and the left-kernel relation hold exactly over Q. This agrees with
B13-03's existing mathematical result; the complete-interpolation certificate
and independent bracket-based verification route are new.

**ADOPTED / OPEN, unchanged.** At LMR the frozen evidence remains a24=274,
determinant rank 273, padded rank at least 269 and D in [-4,+1]. Five sampled
padded kernel vectors are not five certified equations. No new degree-13/14
source or target, padded ideal multiplicity, determinant multiplicity, or
positive obstruction is claimed.

## 1. What is proved and certified

**PROVED.** `docs/b14_03_complete_interpolation.md` gives Lemma CI with the
source-completeness and inclusion hypotheses, mixed-bracket membership and
coefficient normalization, the exact pullback, and rational/CRT safeguards.
If dim N=h, h genuine members have a full nonzero evaluation minor, and S(M)
lies in N, evaluation on those points is injective on N. Exact source
evaluation then computes ker S itself. A proved upper bound dim N<=h plus the
minor suffices to establish equality. For source rows and point columns,
relations are columns of K with **A^T K=0**.

**PROVED / CERTIFIED.** The target is the weight-(8,8,8) highest-weight space
in Sym^6 V tensor Sym^6(Sym^3 V). Pieri interlacing has exactly one predecessor,
(8,8,2). Complete cubic raising equations have rank 37 at both primes on 38
weight monomials, giving the dimension upper bound 1. The explicit mixed
bracket minor supplies the lower bound 1. Membership is proved by the
equivariant map z_j^alpha -> alpha! d_alpha for each cubic letter, with
linear letters sent to l_i, no orbit averaging; every coefficient-level
raising residual is also checked exactly.

| exact object | value | status |
|---|---:|---|
| source weight space / raising matrix | 561 / 1056-by-561 | CERTIFIED |
| source raising ranks, both primes and Q | 559 | CERTIFIED |
| complete source highest-weight dimension | 2 | CERTIFIED |
| cubic predecessor weight space / raising matrix | 38 / 54-by-38 | CERTIFIED |
| cubic raising ranks, both primes and Q | 37 | CERTIFIED |
| target dimension | 1 | CERTIFIED |
| reconstructed target polynomial support | 1720 terms | CERTIFIED |
| full target minor | 209952 | CERTIFIED |
| exact source rank / ideal multiplicity | 1 / 1 | CERTIFIED |

**CERTIFIED.** Let F0,F1 be the explicit ordinary-coefficient sources shipped
with the certificate. The basis is (F0+F1,F1), so both rows are nonzero and a
relation needs cancellation. At the supplied cubic and l=(1,0,0),(1,2,0):

    A = [[729,3969],[729,3969]], K = [[1],[-1]],
    T = [[209952,1143072]].

An additional symbolic comparison with the old universal-pullback instrument
checks **G=288 mu*(F1)** on all 1,720 coefficients and mu*(F0)=0. That oracle is
not used by the independent checker's acceptance path.

**CERTIFIED.** The independently derived integer row bounds are 7,494,539,904
and 7,541,849,088. The house-prime product is 4,611,685,975,477,714,963, exceeding
twice each bound. Signed CRT, independently reduced residues, direct integer
evaluations, rational rank and exact kernel identities agree. The rational
control uses rows ((F0+F1)/2,F1/3), denominators (2,3), unchanged cleared A_Z,
and K=(2,-3)^T. Both denominators are invertible at both primes.

## 2. Validation with failures that reach the relevant checks

**CERTIFIED.** The final control suite passes **97/97 cases**: two valid inputs
and **95 rejected mutations**, including **71 separate required-key deletions**.
The suite also rejects duplicate JSON keys and confirms the full symbolic
identity above. Every failure records the reason and checks already reached.

| deliberately wrong input | required failing gate |
|---|---|
| changed point l | reconstructed target entries |
| incorrect source row denominator | source scaling |
| bad cubic-letter valence | target membership |
| valid zero bracket, with all valences preserved and zero entries supplied | nonzero full target minor |
| one house prime only, with matching product and residue data | insufficient CRT modulus |
| one changed integer entry, including a congruent wrong lift | exact source evaluation |
| wrong residue | independent modular source evaluation |
| invented target/source dimension | full dimension reconstruction |
| right-kernel vector (49,-9) supplied as a source relation | exact A^T K identity |
| prime dividing a source denominator | common rational/integral model |
| absent/empty points, source, target, or required nested field | explicit parsing/input guard |
| unsupported larger profile | UNPARSEABLE / NOT VERIFIED |

**CERTIFIED.** The final fresh-process replay checks all five process outcomes:
producer, controls, standalone verifier and dispatcher return 0; the dispatcher
negative run returns the expected **1**. Integer, rational and gzip positive
certificates PASS. The negative CLI run reports one FAIL (altered entry), three
UNPARSEABLE (missing points, duplicate key, nonexistent file), and zero PASS.
See `results/b14_03/replay_results.json`, `control_results.json`,
`control_mutations.json`, `verification.json` and the dispatcher reports.

**RECORDED.** No analysis code is imported by the checker. Its full bracket
polynomial expansion is distinct from the producer's pointwise contraction.
Source and cubic raising matrices are rebuilt using an independent exponent
enumeration and tuple-based remapping. Modular operations reduce before int64
conversion, with an explicit product/subtraction bound; all rational operations
use Python integers/Fraction. The normal verifier now lazily imports legacy
flint/scipy backends. Full legacy-corpus re-derivation was **NOT REACHED** because
those dependencies are absent; no legacy arithmetic was changed.

## 3. Resources, reproducibility, and provenance

**RECORDED.** Preregistration was committed as `3398a4da` before any new
mathematical measurement. Historical source dimension 2, target dimension 1,
rank 1 and value 729 were labelled already observed. Actual model
**gpt-6-astra**, effort **xhigh**, was confirmed from local turn_context for task
`01a093aa-7331-79e3-bddc-8b76e48a9616`. No subagents or other sessions were used.
HEAD and peeled batch14-base matched the requested frozen commit; both tree
readings matched the requested tree. Portable blob IDs and working-byte SHA256
are in `results/b14_03/input_manifest.json`; launch identities are in
`results/b14_03/launch_inputs.json`.

**RECORDED.** Host resources: 20 logical CPUs, 33,752,997,888 bytes physical RAM;
12,970,004,480 bytes available at preflight, shared rather than reserved.
CPython 3.12.14 and NumPy 2.3.5 were available; flint, sympy and psutil were
absent. Nothing was installed. WMI was unavailable, so native Windows memory
queries supplied resource facts. Exact stdlib arithmetic follows the launch
brief's permitted alternative to python-flint.

**MEASURED.** Final replay costs below are child-process measurements, not
forecasts for larger cells. Total driver elapsed time was about 22 seconds.

| final replay unit | seconds | peak working set MiB |
|---|---:|---:|
| producer | 0.47 | 22.54 |
| all control mutations and symbolic oracle | 5.44 | 43.62 |
| standalone verifier | 5.21 | 43.41 |
| dispatcher, three positive files | 5.02 | 44.26 |
| dispatcher, four negative files | 5.11 | 44.30 |

**RECORDED.** Every mathematical unit had one process, one numerical-library
thread, a hard Windows Job Object process-memory cap of 768 MiB and a 120 s
producer or 600 s verification deadline. PID and resource files accompany the
logs. No resource stop occurred. The banked wrapper was reused and then adapted
to B14 metadata; earliest launch banners retain its inherited B13 label, while
their normalized resource JSON and every final replay banner say B14-03.
The mathematical artifacts and actual model attribution were never relabelled.

**PROVED cost bound / MEASURED search.** Literal full bracket expansion has
6^8=1,679,616 assignments. Sparse l=x1 point contraction has at most
2^6*6^2=2304; the first preregistered cycle-plus-two-triples bracket was nonzero,
so no random-layout fallback was needed. Live symbolic terms are capped at
250,000, weight monomials at 3,000 and raising entries at five million.
The old universal-pullback cross-check accumulated 106,969 branches, with
maximum 216 terms in a monomial expansion and 1,723 accumulated polynomial
terms before final zero pruning.

## 4. Boundaries, assignment defects, and next work

**NOT REACHED / OPEN.** The verifier implements the exact h=1 profile, not a
general degree-13/14 bracket engine. At those degrees the unresolved inputs
are complete genuine target members, accepted dimension evidence, exact source
matrices and compatible scaling/transport data. This run waited for none of
them. A larger adapter must preserve the current gates and prove its convention
compatibility. Its literal full expansion is not priced by the five-second
ternary control; no defensible larger-cell runtime is inferred. The core control
and specification are complete, so the substantive fallback is not needed.

**RECORDED defects/clarifications.** The packet's checkout and HEAD-only bundle
examples conflict with the launch brief; the latter correctly governs the
already prepared named branch and immutable base. The packet's flint/Linux
commands need the explicitly authorized Windows/exact-stdlib adaptation.
The legacy verifier's eager flint/scipy imports would prevent even this
independent CI checker from running; lazy kind-specific imports fix that
integration issue. A proof of only dim N<=h is sufficient when the full
h-member minor supplies the reverse bound; labelling this sandwich explicitly
avoids treating a modular upper-bound computation as an unsupported equality.

**RECORDED.** Only intentional B14-03 files, the new kind's dispatcher hook,
an appended format specification and two justified PROVED index entries are
included. No machine exclusion family is asserted, so the inherited-exclusion
ledger is unchanged. Protected files, other worktrees, integration branches
and repository configuration were not edited. No push, merge, publication,
external message or recurring automation was created.

**RECORDED next step.** Review the CI proof and the fail-closed profile contract,
then implement a larger profile only against completed compatible target/source
inputs. `results/b14_03/REPLAY.md` provides exact commands. The delivered
manifest and before/after delivery-check logs record bundle integrity and the
named ref `refs/heads/b14-03-astra`.
