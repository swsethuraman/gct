# R28-01b — re-review of repairs P1–P5

**HAND — decision: P1 ACCEPT; P2 ACCEPT; P3 ACCEPT; P4 ACCEPT; P5 REPAIR.**
The remaining defects are confined to supervisor resource-stop enforcement.
The arithmetic/control regressions pass. **B28-01b may launch: NO.**

**HAND — scope.** This reviews only repair commit
`5a3174cd3a1ec96b05b92a8bcb73fbee58c0544b`, against P1–P5 in
`8a86fec17b72b565baaef7f9e29709d1ced35168:docs/b28_01r_review.md` and the
stated launch preflight. Code locators below refer to that repair commit.
R28-01's accepted R1, R4 and R6 stand; regression bindings are checked as
required, without reopening their accepted conclusions. The governing protocol
is `96a8074d:results/b27_06/PREREGISTRATION.md`.

## Preflight and bindings

**READ / COMPUTED.** The reviewer worktree was clean on `b28-01r`, at the
required continuation HEAD `8a86fec17b72b565baaef7f9e29709d1ced35168`.
The review document, results directory and script prefix were absent. No
pre-existing untracked file was modified. Both the producer tip and reviewer
HEAD matched `ls-remote`. Git's sandbox ownership restriction was handled by
owner-context read commands and a per-command `safe.directory` setting; no
Git configuration was changed.

**COMPUTED — launch-file bindings.** These SHA-256 values name raw on-disk
bytes, including their original line endings:

| File | SHA-256 |
|---|---|
| `B28_COMMON.md` | `06799a9e404fc45a0944f7fcae88d8dd5511f7721f704ebe69872dd3061c87b9` |
| `R28-01b.md` | `5952741b70b9370802c3bc897c1e6bc7af874046f4ff2d35717398220b6e1165` |
| `R28-01.md` | `57904854afc6be2e9c7385e6131eb4cc0a67b988e7d3dc3f8d069a9249b134ef` |
| `BATCH28_BOARD.md` | `69d0f6328e0ebcd9dc6e744e502686f69257fad5bb9a5fb56a8427e9601c3e1d` |

**COMPUTED — producer bindings: ACCEPT.** The repair's sole parent is
`a1c3c3a69b789c91909ed5476354ad762f3e71c2`. All 212 changed paths are additions
within `analysis/b28_01c_*`, `results/b28_01c/`, or `docs/b28_01c_report.md`.
The manifest has 37,926 bytes and SHA-256
`93bb78e2f4bee90ec668c6c957689571052761860b5556d41bd67641f278254a`.
All 211 payload hashes and lengths match raw committed blobs; the manifest
and its payloads exhaust the changed paths. `BINDINGS.json` enumerates them.

**COMPUTED.** All 11 `frozen_c_hashes.txt` entries match their WSL host copies;
the nonbinary files also match their committed code/rate blobs. All six old
frozen entries and the engine inventory still match their old hashes. All four
new host-retained files match their committed bindings. The verifier C source
and binary are unchanged. No prior Cell A output or job exists. The five saved
diffs bind old and new source bytes; `vfy.diff` is empty.

**COMPUTED — actual launch preflight: ACCEPT.** The hash-checked launcher ran
only with `--preflight-only` and passed input/library bindings, the binary-mtime
guard, prior-output checks, free memory and the 64 GB free-disk requirement.
Observed free-resource quantities and elapsed time are in
`preflight_receipt.json`, not in a deterministic certificate. The full target
launch was not invoked.

## P1 — stop paths and deterministic rank: ACCEPT

**READ / HAND.** In `analysis/b28_01c_driver.py:hybrid_det`, a projected nullity
different from `a` now returns before the `Kc(n,nul)` allocation. A failed
all-row kernel check stops lifting; a failed deterministic rank check likewise
returns a failed-source result. `main` writes the certificate and receipt,
then exits 4 before the next prime. The replacement `H.rank_mod_p(Kc[U,:],p)`
uses Flint directly, without `rank_tall`'s projection retries. The two-prime
comparison checks both outcome category and evaluation rank, and disagreement
returns 6 with an inconclusive control-failure record.

**COMPUTED.** The source-failure fixture returned 4 at the first prime with
projected nullity 30, no lift phase, no kernel file, and no second-prime
certificate. The disagreement fixture returned 6 for ranks 24 versus 22,
with `FULL_RANK` versus `MODULAR_DEFICIENCY`. These are control fixtures, not
measurements of an additional research cell.

## P2 — certificate branches: ACCEPT

**READ / HAND.** `analysis/b28_01c_verify.py:registered_recipe` reconstructs
base seed 20260908, attempt 0, the per-prime offset, `m=|U|+64`, and eight
projections. The recorded fields must equal that reconstruction; residual
construction uses the reconstruction. Full rank requires `a` distinct,
in-range minor rows and a recomputed nonzero determinant equal to the claim.
The regeneration functions and independent C solve retain the accepted
arithmetic.

**READ / HAND.** A deficiency requires candidate and combination files with
the prescribed counts, shapes and hashes. The verifier independently checks
every candidate's nonzeroness, all E equations, all saved-point evaluations,
and equality to its saved combination of K; rank on U checks independence.
The driver's new `deficiency_candidates` checks the corresponding properties
and a failed check stops before the next prime. New verdicts distinguish
`FULL_RANK` from `MODULAR_DEFICIENCY`, with lower bound `r` and unproved
candidates. Fixture switches are confined to the registered small-cell
controls and are absent from the frozen target command.

**COMPUTED.** The missing-minor and false-recipe controls both now return
`REJECT` (exit 5), failing their specific new checks. The valid deficient
fixture returns `MODULAR_DEFICIENCY` (exit 8), lower bound 22 with two valid
candidates. In the corrupted fixture the first candidate remains valid;
the replacement second candidate passes its E equations and K-combination
check but fails zero at the saved points, and the verifier rejects it.
The original corrupted-kernel and corrupted-pencil controls also reject.

## P3 — verifier time in the gate: ACCEPT

**READ / HAND.** `analysis/b28_01c_model.py:remaining_secs` is called by both
the driver gate and repricer. It charges the maximum of the direct verifier
model and the upward-rounded coefficient-ratio bound times the producer's
six-phase model. The producer's post-gate work is charged at both primes and
the verifier's independent rebuild is included. The refreshed rate file is
bound by SHA-256
`665e9da1dd997b4318976c0a617d52f09f924f53e0fe2c451a7b0afce4787d1b`.

**COMPUTED.** `GATE_AUDIT.json` recomputes all six price scenarios with exact
rational arithmetic on the serialized decimal coefficients. Both coefficient
sets equal the old committed host rates. Their maximum ratio is strictly
between 2.7388 and 2.7389, so 2.7389 is the required upward rounding.
All displayed prices and gate comparisons reproduce. The largest scenario
total rounds to 3.785 hours; this remains a scenario, not a completion guarantee.

## P4 — verifier memory in the gate: ACCEPT

**READ / HAND.** The shared model accounts for the carrier and sparse E,
build temporaries, cover-row matrices, projection construction, sparse PF and
its slices/copies, dense residual/solve temporaries, Flint conversion, kernel
checking and evaluation. It uses actual row count, nonzeros inside and outside
the cover, `N_S`, n, U and a. The driver gates the maximum of this estimate
and the producer envelope at 75% of the job cap before Schur allocation.
This is a conservative engineering estimate backed by calibration, not a
proved allocator-wide memory bound. The OS cap remains necessary.

**COMPUTED.** Independent integer evaluation reproduces all six memory
scenarios and all three committed calibration/control estimates. The cal2
verifier estimate is 9,127,518,584 bytes, covering the largest committed
verifier phase peak of 5,651,423,232 bytes. The maximum Cell A scenario estimate
is 17,202,216,616 bytes, below the 18,000,000,000-byte gate. Cal2's fresh replay
used the target's 24 GB *model parameter* to pass this conservative gate,
while its actual OS scope remained capped at 8,000,000,000 bytes.

## P5 — launch supervisor: REPAIR

**READ / HAND.** The launcher uses one decimal 24,000,000,000-byte scope with
zero swap over producer and verifier. The supervisor maintains one monotonic
deadline and passes the remaining budget to the driver. The launch preflight
binds all invoked code/rates/engine helpers and checks library versions,
available memory/disk, and absence of target output. The driver also guards
the Schur binary hash and mtime; the verifier refuses to compile a missing
binary. These implement the requested launch checks and no-recompile rule.

**READ.** The producer disclosed two sequential 8 GB control scopes after
correcting its initial prior-output glob. This review uses one aggregate
8,000,000,000-byte scope for its own control/calibration replay. That producer
receipt deviation does not change the frozen arithmetic or waive any target
resource requirement.

**READ / HAND — P5a, whole-group termination is incomplete.** In
`analysis/b28_01c_supervise.py:46–54`, `kill_group` sends SIGTERM to the process
group, waits only for its `/usr/bin/time` leader, and returns immediately when
that leader exits. A remaining child is not then sent SIGKILL. Therefore the
supervisor can write a wall-stop receipt and exit while numerical work is
still alive. The launcher's 87,000-second scope backstop does not establish
termination at the registered 86,400-second deadline.

**COMPUTED.** The two-second deadline fixture launches a small child that
ignores SIGTERM. The frozen supervisor returns 124 and records a wall stop,
but the child remains running. The reviewer explicitly kills that test child
after observing it. `SUPERVISOR_CONTROLS.json` records the deterministic
outcome; `supervisor_controls_receipt.json` records commands, timings, PID,
hashes, scope limits and cleanup. This fixture does not run any matrix work.

**HAND — smallest P5a repair.** Retain the process-group identity independently
of the leader's exit. After SIGTERM, enforce termination of surviving group
members with SIGKILL even if `proc.wait()` already returned; do not finish
until the job's remaining processes have terminated. A scope-based kill can
also enforce the same property, provided receipt writing survives. Add this
TERM-resistant-child control and assert that no child remains after the stop.

**READ / HAND — P5b, artifact stop is skipped at step completion.** In
`analysis/b28_01c_supervise.py:92–102`, size is checked only when `proc.wait`
times out. An exited step breaks directly out of the loop. `finish` at
lines 71–80 records final size but does not enforce the limit, and the next
step checks only remaining time. A size crossing between the last poll and
process exit can consequently pass to another step or return success.

**COMPUTED.** A fast writer creates exactly 2,048 bytes under a 1,024-byte
artifact-stop setting. The frozen supervisor returns 0 with no resource stop,
while its own receipt records 2,048 final bytes. The small limit exercises
the same integer comparison/control flow as the launcher's 50 GB setting;
no large file was needed.

**HAND — smallest P5b repair.** Recheck artifact size immediately after each
step exits, before dispatching any following step and before a success return.
Return 125 with the resource-stop receipt on an excess. Also recheck the
monotonic deadline at these completion boundaries, so a successful process
exit cannot bypass that check. Add the fast-writer fixture. Preserve the
existing 64 GB free-disk preflight and 50 GB artifact setting. No producer or
verifier arithmetic change is requested. Refreeze the changed supervisor,
launcher binding and hash list before the next review.

## Controls, regression and resources

**COMPUTED — registered controls: ACCEPT.** All controls in the producer
harness met their expectations, including both malformed certificates,
deficiency/corruption, source failure and prime disagreement. The existing
slow-writer, ordinary wall-stop and full-rank two-step supervisor controls
also pass; the two added boundary controls explain why those successful
examples do not settle P5. Only cal2 was replayed; the cal1 sizing call was
skipped and its already committed gate inputs were used for the memory audit.

**COMPUTED — regression: ACCEPT.** Both small-cell primes and cal2 at the
first prime return full rank under independent verification. The replay
runner hashes every output before exiting. `REGRESSION.json` compares those
raw hashes to the bound repair manifest/retained-file hashes: all 95
deterministic files match. Against B28-01a, all 14 binary/pencil outputs match,
and all eight cell/certificate/verifier JSON records preserve their original
matrix, cover, kernel, rank and minor values. Driver and verifier E/G/VK
hashes agree. The C solve has no diff.

**COMPUTED — schema changes only.** The cell JSON is unchanged. Certificate
changes are `schema`, with added `evaluation.npts`, `hybrid.rank_K_method`
and `outcome`. Verifier changes are `schema` and `ACCEPT` to `FULL_RANK`, with
added outcome/point-count/recipe checks, `inputs.npts` and the six reconstructed
recipe values. No old JSON field is removed. New prime-comparison files and
resource/gate receipts are separate. The exact field-by-field comparison is
in `REGRESSION.json`.

**READ / COMPUTED — temporary-file limitation and audit recovery.** The
completed runner durably saved `replay_receipt.json`, `controls_receipt.json`
and its stdout receipt under this review's results. A subsequent audit found
the `/tmp` replay files unavailable and exited before writing results; its
unchanged script and `audit_attempt1_receipt.json` are retained. The reason
for the temporary-file disappearance is not established. No calibration was
rerun. The corrected audit compares the already saved raw output hashes with
committed hashes. Small JSON evidence under `results/b28_01rb/replay/` is
recovered from committed producer blobs only after matching their raw hashes
to the fresh replay hashes. It is not presented as a direct copy from the
temporary run. `TEMPORARY_OUTPUTS.json` binds the former temporary binaries
without claiming they are retained; the matching producer-bound originals
remain available. This limitation affects availability of this review's
duplicate binary files, not the completed hash comparison.

**READ / COMPUTED — limits.** `RESOURCE_RECEIPT.json` enumerates all seven
sequential WSL invocations, including the failed follow-up audit and final
bookkeeping. The control/calibration replay used one scope with decimal
`MemoryMax=8000000000`, `MemorySwapMax=0`, and an outer 3,500-second timeout;
its measured time and scope peak are in `replay_receipt.json`. Other runs
were limited to 60 seconds and at most 512 MB. Aggregate measured runtime is
below one hour. There were no installs, no changes to `~/b28_01`, no Cell A
or Cell B build, no other session, and no subagent. Nondeterministic runtime
measurements are confined to receipts.

## Registered outcome

| Repair/rung | Outcome | Achievement level |
|---|---|---|
| Bindings | **ACCEPT** | **READ / COMPUTED:** raw-byte provenance |
| P1 | **ACCEPT** | **READ / HAND / COMPUTED:** stop-path review |
| P2 | **ACCEPT** | **READ / HAND / COMPUTED:** certificate controls |
| P3 | **ACCEPT** | **READ / HAND / COMPUTED:** gate-time audit |
| P4 | **ACCEPT** | **READ / HAND / COMPUTED:** gate-memory audit |
| Controls/regression | **ACCEPT** | **COMPUTED:** unchanged recorded arithmetic |
| Launch preflight/no recompile | **ACCEPT** | **READ / HAND / COMPUTED:** engineering checks |
| P5 | **REPAIR** — P5a/P5b above | **READ / HAND / COMPUTED:** resource enforcement |

**B28-01b may launch: NO.**

**HAND.** No achievement level moves: this establishes no new source
condition, coefficient equation, separation on padding, positive multiplicity
gap, geometric noncontainment, equation-existence result or asymptotic bound.
**READ:** "No five-row determinant equation is known to be nonzero on padding."
Programme decision: "no construction ready."
