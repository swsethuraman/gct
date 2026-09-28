# R28-01 — review of the frozen B28-01a machinery

**HAND — decision: B28-01b may launch: YES after listed repairs.** The current
frozen launch is not cleared. R1 ACCEPT; R2 REPAIR; R3 REPAIR; R4 ACCEPT;
R5 REPAIR; R6 ACCEPT. The repairs are enumerated below and require a new frozen
binding and successful branch controls before launch. The board's separate
requirement for the user's B28-01b go remains in force.

**READ — scope.** Producer `a1c3c3a69b789c91909ed5476354ad762f3e71c2`, parent
`c0122f57e745097ddb84d3f6ee6a26e1de8d8314`; governing protocol
`96a8074d:results/b27_06/PREREGISTRATION.md`. Source locators below refer to
that producer commit for `b28_01_*` and to `96a8074d` for the earlier engine.
They do not refer to mutable producer worktree files.

**HAND — achievement boundary.** This is an engineering and certificate review,
with READ, HAND and COMPUTED evidence. Cell A was not built, and there is no
new source condition, coefficient equation, padding separation, positive
multiplicity gap, geometric noncontainment, equation-existence result or
asymptotic bound. No achievement level moves. **READ:** "No five-row determinant
equation is known to be nonzero on padding." Programme decision: "no construction
ready."

## Preflight and evidence convention

**READ — preflight.** This was a fresh review session without exposure to the
producer's production session. Branch `b28-01r` had HEAD
`ee354b57a9f60baacef7f451db28e5cce86d29bd`, the specified setup commit. The
worktree was clean and all three output patterns were absent. No pre-existing
untracked file was changed. The project root is not a Git repository. Git's
sandbox ownership check was handled with a per-command `safe.directory` value,
without changing Git configuration. WSL access required the host execution
permission path; the authorized read/replay operations then succeeded.

**COMPUTED — raw launch-file SHA-256.** These name the exact on-disk bytes read
at preflight, including their line endings:

| File | SHA-256 |
|---|---|
| `B28_COMMON.md` | `06799a9e404fc45a0944f7fcae88d8dd5511f7721f704ebe69872dd3061c87b9` |
| `R28-01.md` | `57904854afc6be2e9c7385e6131eb4cc0a67b988e7d3dc3f8d069a9249b134ef` |
| `BATCH28_BOARD.md` | `01a20dd52fc1163bf99945d4c0c9c984af2e4cb6ecf90d2df131a1c8358b9bdf` |

**READ / COMPUTED — bindings.** `results/b28_01r/BINDINGS.json` binds every
producer payload, all engine originals and host copies, governing texts and
record files. `AUDIT_INPUTS.json` binds the additional exact-audit inputs.
Every SHA-256 in this delivery names raw blob/file bytes, with no decoding,
newline conversion or Git filtering. No third-party source was downloaded or
committed. Runtime libraries remain declared shared dependencies, not an
independently verified implementation of finite-field arithmetic.

## R1 — bindings: ACCEPT

**COMPUTED.** The producer parent is exactly the specified parent. Its 187
changed paths are additions confined to `analysis/b28_01_*`,
`docs/b28_01a_report.md` and `results/b28_01/`. The manifest is 32,991 bytes,
SHA-256 `420eb69ab49165338cfe9afab87f02ecb4ffc9d270b2fcc50ce2acb8172b934e`.
All 186 payload sizes and SHA-256 values match the committed blobs; together
with the manifest they exhaust the changed paths.

**COMPUTED.** All 19 engine sources in `~/b28_01/engine` are byte-identical to
their originals at both `96a8074d` and
`7c36a52ddf338eb390a9bcd491cb9c50cf9e2a19`. `schur.so` is the additional,
host-built binary, not a twentieth committed source. Its recorded hash matches.
The frozen host copies and committed sources match `frozen_v2_hashes.txt`:

| File | Raw SHA-256 |
|---|---|
| Driver | `de202bb09855301e911123e1e39dd4e85b493d1fc8b6d1bcae7d9986bd71094c` |
| Verifier | `7978a73aaf30ee0dee4fa37a6bdf088a52daf85b00390af62d532b2027e7def5` |
| Verifier C solve | `5166db3b1ff07d23d3a4c51d9430de1a9808dff9d1e5d4d92b802a98904995f7` |

**COMPUTED.** All five files in `HOST_RETAINED.json`, not merely one, exist
under the stated host root and match their sizes and hashes. The audit also
checks the frozen launcher, repricer, rate file and two compiled helpers.
The Cell A output directory was absent. See `BINDINGS.json` for full paths and
hashes and `binding_receipt.json` for the bounded audit invocation.

## R2 — fidelity to protocol items 1–7: REPAIR

**READ / HAND — checklist.** The following distinguishes implemented normal
paths from the required changes; the detailed repair identifiers are below.

| Requirement | Assessment |
|---|---|
| Determinant family only | **READ:** the driver only creates determinant pencils and evaluation rows. Its unchanged s79 module imports definitions for other families, but their measurement routines and large allocations are not invoked. |
| `nullspace(G)`, not `nullspace(G.T)` | **READ:** driver line 143 has the correct orientation. Line 298 likewise uses `nullspace(VK)` for coefficient combinations. |
| Build, save cover, reprice before Schur | **READ:** driver lines 221–273 build E, assert the frozen dimension and Weyl value, record CSR shape/dtypes/bytes/hash, save S/U/rows, and evaluate the gate before `hybrid_det`. Timing/peak data go to the receipt. |
| 75% memory gate | **READ:** the comparison is present and uses the preregistered envelope. **HAND:** the verifier allocation estimate is incomplete (repair P4). |
| One pinned source projection per prime | **READ:** Schur attempt is fixed to zero, base seed 20260908, `pseed=20260908+p%1000`, `m=U+64`, `nproj=8`. **HAND:** the additional `rank_tall` search and failed-source continuation require P1. |
| 250 MB X block, minimum 32 columns | **READ:** `S71_MEM_X=250000000`; `max(32,floor(250000000/(4*nS)))`; the envelope includes `5*max(250000000,128*n)`. **HAND:** at Cell A, `128*n=104104192 < 250000000`, so the minimum cannot itself overrun the nominal block budget. |
| Exact arithmetic bounds | **HAND / COMPUTED:** the bounds below suffice for the frozen targets and calibration cells. No numerical rank tolerance is used. |
| Pencils | **READ:** exactly `a+8`, bound 40, seed 11, serialized once outside the prime loop; the same integer pencils are used at both primes. Evaluation batches contain at most eight points. |
| Primes, order, sequential execution | **READ:** the launcher pins 2147483647 followed by 2147483629; the driver loop is sequential and forces one BLAS thread. **HAND:** disagreement is not acted on (P1). |
| No extra points/primes or Cell B | **READ:** none is dispatched by the frozen launcher. **HAND:** source-failure stopping and the extra rank projection retries are the exceptions in P1. |
| Independent replay | **READ:** a separate verifier runs at the first prime. **HAND:** its source mathematics is sound, but certificate branch checks need P2, and its cost must be used correctly at the gate (P3). |

**HAND / COMPUTED — arithmetic.** For the producer's float64 limb dot products,
`(2^21-1)*(2^16-1)^2 < 2^53`; each nonnegative integer partial sum is exactly
representable. The inner-dimension assertion is present both at contraction and
in the helper. Cell A has 813,314 columns, below 2^21. The uint32 residues and
uint64 C products obey `(p-1)^2+(p-1) < 2^62`; the C solve and projection reduce
after each term. Signed CSR kernel checks have absolute limb sum at most
`813314*65535^2 < 2^63`. These are integer inequalities, not error tolerances.

**HAND / COMPUTED.** The verifier's integer contraction uses chunks of 2^15,
so `2^15*65535*(2147483647-1) < 2^62`. Its `PF_S*X` operation checks the actual
absolute row-sum bound before that product. The earlier sparse projection
product is also safe at Cell A: `z <= 4*k*n = 32*n`, hence its absolute
accumulation is bounded by `8*(32*n)*65535 < 2^63`. At cal2, its recorded z is
smaller. Evaluation accumulates at most the orbit size (one at Cell A and four
at cal2); each modular monomial multiplication is below 2^62. The verifier's
base-L keys obey `70^8 < 2^63` and `126^9 < 2^63`; the producer uses the
injective, below-wall combinadic path. `ARITHMETIC_AUDIT.json` records the exact
integer values and the verifier import inventory. A diagnostic `log2` is not
used to decide rank or arithmetic safety.

**HAND — P1, smallest control-flow repair.** In driver lines 143–165 and
280–311:

1. If the projected nullity is not a, write the failed-source certificate and
   receipt and exit 4 before allocating `Kc(n,nul)`. On any failed all-row or
   independence check, similarly stop before the next prime. Currently the
   driver sets `status=4` and continues the prime loop; it also lifts a surplus
   nullspace before discovering that the source gate failed.
2. Replace `H.rank_tall(Kc,p)` with a deterministic small rank check of
   `Kc[U,:]` (or the equivalent `yU`). The existing helper contains four
   randomized projection attempts and a fallback. This is distinct from the
   single Schur projection, but it remains an unnecessary retry path in the
   advertised no-search machinery. Because the U coordinates are exactly the
   residual basis, this replacement loses no certificate strength.
3. After the two successful source gates, explicitly compare determinant ranks
   and outcome categories. On disagreement, report an inconclusive control
   failure. Currently unequal ranks can return zero and the launcher verifies
   only the first prime, without acknowledging the discrepancy.

## R3 — verifier independence and certificate logic: REPAIR

**READ.** `b28_01_verify.py` imports no driver or engine module. Its shared
third-party libraries are NumPy, SciPy sparse and python-flint; standard-library
utilities and its own `b28_01_vfy.c` are separate. It independently enumerates
the monomial carrier, forms twisted orbit coordinates, assembles the raising
rows, selects a five-order cover, forms `P*F_o` and its residual, expands the
4-by-4 determinant by Leibniz, evaluates, and contracts with K. The producer
uses a different monomial enumerator/indexing scheme and per-row C residual
accumulation. This is substantive implementation independence, with the
declared shared low-level trust boundary.

**READ / HAND.** G1 verifies a nonzero upper-triangular cover and an S/U
partition. G2 recomputes `rank(G)=|U|-a`, never using a stored rank as evidence.
Thus `rank(E) >= |S|+rank(G)=n-a`. The verifier checks every row of EK and
`rank(K[U,:])=a`, giving the reverse inequality. This proves the modular
source-rank equality conditionally on the regenerated E being the specified
integer raising matrix; its construction agrees with the conventions in
`docs/stabiliser_reduction.md` §§1–2 and `docs/sparse_det_route.md` §1.

**HAND — lifting argument.** The committed plethysm premise supplies
`dim ker_Q(E)=a`. With `rank_Fp(E)=rank_Q(E)=n-a`, choose an `(n-a)` square minor
which is a unit in the local ring `Z_(p)`. Row/column elimination over that
ring expresses a free a-dimensional kernel whose reduction is all of
`ker_Fp(E)`. The verified basis K is a change of basis of this reduction and
therefore lifts over `Z_(p)`. Evaluations of the serialized integer determinant
pencils are integral. A nonzero a-minor of VK implies injectivity of this
evaluation map, hence `mult_det=a` over Q. More generally its rank r supplies
only `mult_det >= r`. A finite-sample modular nullspace supplies no
characteristic-zero upper bound or global vanishing identity. This is the
preregistration's lifting and decision rule, not a new result for Cell A.

**READ — normal full-rank path.** The producer saves VK, a pivot-row list and
the corresponding nonzero determinant. The verifier recomputes VK and its rank
and checks that determinant when the minor field exists. E, G and VK hashes
are cross-checks in addition to regenerated arithmetic. The cover is also
regenerated; S/U hashes and cover statistics are checked. Stored ranks are
compared with recomputed values, not trusted.

**HAND — P2, certificate-branch repair.** The current verifier can omit its
minor check entirely (`if 'minor_rows'...`, lines 508–513), and it takes the
projection recipe from the certificate (lines 459–461) without enforcing the
frozen base seed, attempt, effective seed, extra rows and projection count.
Require the registered recipe and a complete, nonzero a-minor for a full-rank
verdict. Reconstruct the pinned recipe from p and U and compare its recorded
fields. Generic `ACCEPT` must identify whether it accepted full rank or only
a modular lower-bound certificate.

**READ / HAND — P2 continued.** The deficient branch of the driver (lines
297–305) saves `K*nullspace(VK)` vectors, but does not verify their saved-point
evaluations. It merely records the Boolean `okc`, even if false. The verifier
never opens or validates the candidates file. Require the candidate count and
shape, hash, nonzeroness and independence, every E equation, and zero at every
one of the fixed saved points; reject a missing, corrupted or failed candidate.
Save the combinations if that is the cheaper way to check membership in K,
while independently checking the resulting vectors. Emit only
`MODULAR_DEFICIENCY`, lower bound r and unproved candidates; never a drop.
No extra point, seed or prime is needed for this repair.

**COMPUTED — adversarial checks.** `CERTIFICATE_CONTROLS.json` and
`certificate_controls/` record a full-rank control certificate with its minor
removed, and another with false base-seed/attempt annotations but unchanged
effective projection. Both are accepted by the frozen verifier. The regenerated
rank of this control remains correct; these checks demonstrate missing protocol
validation, not a false full-rank mathematical result. They should reject after
P2. A deterministic deficient-branch fixture must additionally exercise a
corrupted candidate before the repaired machinery is frozen.

## R4 — controls and calibration: ACCEPT

**READ / COMPUTED.** `RECORD_COMPARISON.json` compares the producer results with
raw committed rows, binding both whole record files and exact line bytes:

| Cell | Committed locator at `96a8074d` | n_chi; rows; nnz | Cover; U; projected rows | a; determinant rank |
|---|---|---|---|---|
| `(22,6,5,2,1)_9` | `results/s71_sweep.jsonl:5` | 21,093; 51,337; 185,066 | 21,023; 70; 134 | 24; 24 at both primes |
| `(24,6,5,3,2)_10` | `results/s71_sweep.jsonl:145` | 188,872; 510,662; 1,951,800 | 188,498; 374; 438 | 47; 47 |
| `(13,9,9,3,1,1)_9` | `results/s79_cells.jsonl:121` | 732,815; 3,899,488; 18,374,635 | 731,538; 1,277; 1,341 | 70; 70 |

**COMPUTED.** N_S, stabiliser order and all five cover statistics also match.
Cal2 has N_S=3,503,556 and stabiliser order four. Its 85-column, 16-block path
matches the historical record. Cal1's historical one-block setting is not
preserved: the mandated 250 MB budget yields two blocks. This is an intended
resource adaptation, with unchanged source dimensions, cover and rank.

**HAND / COMPUTED.** The `K[0,0]+1` control is meaningful: it fails the all-row
EK check as well as downstream hash/evaluation checks. The single pencil-entry
change fails the fixed generator check and changes VK/minor checks. Their
failures are arithmetic/provenance failures, not merely rejection of a filename.
They do not exercise missing-minor, bad-recipe, deficient-candidate,
prime-disagreement or failed-source stop paths; those gaps motivate P1/P2.

**COMPUTED — fresh replay.** Both small-control primes, both registered
corruptions and exactly one calibration cell, cal2 at 2147483647, were replayed
from hash-checked frozen bytes. The producer and independent verifier accept
cal2 and agree on E, G and VK hashes. Every deterministic mathematical output
matches the committed result or the committed hash of its host-retained file
byte-for-byte: 26 of 26 files. `REPLAY_COMPARISON.json` enumerates each comparison. No timing
receipt is falsely claimed byte-identical. Cal1 was checked against committed
records and artifacts, not rerun in this review.

**READ / COMPUTED — resources.** One aggregate systemd scope set
`MemoryMax=8000000000` and `MemorySwapMax=0`, with an outer 3600-second hard
timeout and sequential subprocesses. The effective settings are recorded in
`scope_limits_receipt.txt`; all commands, input/code hashes, stdout/stderr
hashes and measurements are in the resource receipts. The supplementary
certificate controls use the same small cell under a separate 512,000,000-byte,
60-second scope and count toward the same one-hour review allowance. No install,
Cell A/Cell B build, producer-file change, subagent or other session was used.

## R5 — frozen launch and pricing: REPAIR

**READ.** `b28_01_cellA.sh` pins the target and two primes, checks the driver,
verifier, C source/binary, wrapper, gate rate file, and the transitive engine
source dependencies and Schur binary. The four other source copies in the
19-file inventory are unused by this launch. The launch file's own bytes were
bound externally by R1; it does not self-authenticate. It refuses an existing
output directory, then runs the driver and first-prime verifier. Nonzero driver
exit codes prevent verifier launch. The wrapper's decimal 24,000,000,000-byte
MemoryMax and zero swap are appropriate for sequential numerical processes.

**HAND.** Full rank, a resource-gate stop, a returned verifier failure, and a
returned timeout are visible exits. The currently unhandled cases are immediate
source failure and two-prime disagreement (P1), invalid deficient candidates
(P2), and aggregate deadline enforcement (P5). A deficient modular measurement
is not authority for an identity calculation or Cell B.

**COMPUTED — prices.** `PRICE_AUDIT.json` independently recomputes the six
scenarios using exact rational arithmetic on the committed decimal phase
receipts and serialized rates. Coefficients are maxima over the two calibration
cells; cD has its registered floor; evaluation is deliberately charged to both
V and R. Producer B+S is paid once because its E/cover are reused across primes,
and the independent verifier pays its own rebuild. The displayed scenario
roundings and all integer memory envelopes agree:

| z/n | U=923 | U=4,013 | U=10,683 |
|---|---|---|---|
| 10, total hours | 0.170 | 0.393 | 1.576 |
| 32, total hours | 0.289 | 0.904 | 2.936 |
| 10, envelope GB | 4.375 | 5.595 | 13.437 |
| 32, envelope GB | 6.165 | 7.385 | 15.226 |

**HAND — P3, verifier time at the gate.** The published price uses separate
verifier coefficients. The actual gate replaces them with `verifier_factor =
1.8061` times the producer model, fitted only at the two calibration shapes
(`b28_01_reprice.py:83–85`; driver `258–260`). A ratio of sums at those shapes
does not bound the ratio at a new z/U. **COMPUTED:** at z=32n and U=4,013,
the gate budgets 1,440.398 seconds for the verifier, while its own phasewise
rates give 1,695.384 seconds: an underprice of 254.986 seconds. **HAND:** the
smallest format-preserving repair is
to use an upward-rounded maximum of the six verifier/producer coefficient
ratios; alternatively store both coefficient sets and evaluate the verifier
model directly at measured n/z/U. Refresh and bind the rate hash.

**HAND — P4, verifier memory at the gate.** At cal2 the envelope is
4,831,800,620 bytes but the committed verifier Schur peak is 5,645,422,592 bytes.
The report only checks that envelope against the producer peak. The launch
gate needs the maximum of the producer envelope and a conservative verifier
allocation estimate. Include the simultaneously live projection construction,
`P*F_o` sparse arrays, source/cover arrays, dense residual and Flint conversion,
using the actual row count and z as well as n/U. At minimum the estimate must
cover the calibration peak. Scaling only by z and mentioning an additional
44U^2 in prose does not implement this check in the gate. The 24 GB OS backstop
does not replace the promised 75% preallocation decision.

**HAND — extrapolation risk.** The 0.17–2.94 h figures are correctly derived
scenarios, not a completion guarantee. The largest fitted U is 1,277, whereas
the worst scenario uses 10,683: over eight times the dimension and hundreds of
times the cubic work. The producer's cD maximum is fitted at even smaller U;
the verifier's cubic allowance is a floor, with its measured rank cost mixed
into H. Cache, dense conversion and memory pressure can change the constants.
Multiplying the whole worst scenario by four stays below 24 h, but that is a
sensitivity calculation, not a demonstrated bound on extrapolation error.
P3/P4 and a genuine aggregate cap remain necessary.

**HAND — P5, total wall cap.** Driver/verifier phase timers use a monotonic
clock, but the launch still sets `T0=$(date +%s)` and computes LEFT using another
wall-clock reading (`b28_01_cellA.sh:47,55`). A backward clock step gives the
verifier extra budget; a forward step can stop it prematurely. This matters
especially because a clock step was already observed in v1. Enclose the complete
producer-plus-replay dispatch in one 86,400-second elapsed-time limit and memory
scope, use a monotonic remaining budget, and enforce termination of the whole
job on expiry while preserving a resource-stop receipt. Per-process timeouts
with a wall-clock subtraction do not enforce the registered aggregate cap.

**HAND — launch preflight details.** The future B28-01b preflight must still
check current free memory/disk, input bindings, and absence of a valid prior
target measurement; a comment saying "after the user's go" cannot perform
those checks. Preserve the 64 GB disk reservation and 50 GB artifact stop, or
document an explicit output-size bound for this fixed target. Also forbid an
unrecorded recompile after the hash check: the engine loader recompiles when
the `.so` mtime precedes the C source. The current host's mtimes and hashes were
checked and did not take that path during this review.

## R6 — host notes: ACCEPT

**READ / HAND.** The producer records apt via `wsl -u root` because sudo required
a password. The slot allowed WSL toolchain/library installation. This is a
provenance/privilege detail, not evidence of incorrect matrix arithmetic. The
record identifies OS, compiler, Python, libraries, BLAS, compile flags and
binary hashes. This review installed nothing and performed no privileged
package operation.

**COMPUTED.** The host v1 driver/verifier hashes match the committed resource
receipt. Replacing `time.time()` by `time.perf_counter()` in those exact v1
bytes gives the committed v2 bytes exactly. All 25 retained non-receipt control
and cal1 artifact pairs also match exactly (`TIMER_AUDIT.json`). The fix preserves
mathematical output; the old negative duration is superseded, not silently used
as a calibration rate. P5 addresses the separate timer defect still in the
launcher.

**READ / HAND.** `8G` in the producer's systemd scope was 8 GiB = 8,589,934,592
bytes, 589,934,592 bytes above the 8,000,000,000-byte wording. Its recorded peaks
were below the stricter decimal limit, so this enforcement mismatch does not
invalidate the observed calibration. The fresh replay used the decimal limit.
Resetting VmHWM phasewise also explains why GNU time's lifetime RSS figure should
not be substituted uncritically for the larger recorded phase peaks.

**COMPUTED / HAND.** All five host-retained files were checked; the cal2 kernel
and cover arrays were additionally regenerated and matched. Excluding large
payloads from Git does not itself invalidate the certificate when committed
hashes and reproducible generators bind them. Availability remains dependent
on retaining them or regenerating them. The review's temporary large outputs
have their own paths/hashes in `replay_receipts/host_retained_receipt.json`.

## Required repair gate and final outcome

**HAND.** P1–P5 are required before launch. Implement them on the producer's
authorized branch, add deterministic controls for the identified failure and
deficiency branches, freeze the changed code/rates/launcher, and have the
repaired bindings and controls reviewed without constructing Cell A. No rewrite
of the successfully reproduced carrier or determinant arithmetic is requested.
The reviewers' two extra malformed-certificate controls must change from ACCEPT
to REJECT. Existing control and calibration matrices, kernels, ranks and minors
must remain unchanged; verifier schemas may record the added checks.

| Rung | Outcome | Achievement level |
|---|---|---|
| R1 | **ACCEPT** | **READ / COMPUTED:** bindings only |
| R2 | **REPAIR** — P1, P3, P4 | **READ / HAND:** protocol fidelity review |
| R3 | **REPAIR** — P2 | **READ / HAND / COMPUTED:** certificate review and controls |
| R4 | **ACCEPT** | **READ / COMPUTED:** historical calibration reproduction |
| R5 | **REPAIR** — P1–P5 and the stated launch preflight | **READ / HAND / COMPUTED:** engineering/pricing review |
| R6 | **ACCEPT** | **READ / HAND / COMPUTED:** provenance and resource audit |

**B28-01b may launch: YES after listed repairs.**

**HAND.** No achievement level moves. **READ:** "No five-row determinant equation
is known to be nonzero on padding." Programme decision: "no construction ready."
