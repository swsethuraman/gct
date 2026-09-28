# R28-01c — supervisor repairs P5a/P5b

**HAND — decision: P5a ACCEPT; P5b ACCEPT.** The two blocking fixtures now
behave as required, and the frozen launch preflight passes.

**B28-01b may launch: YES.**

**READ / HAND — authorization boundary.** This is the review clearance.
The board still requires the user's separate go for B28-01b. The user's
"Yes authorized" in this task authorized R28-01c only. This review did not
dispatch the measurement command or construct Cell A.

## Scope and preflight

**READ.** The scope is `R28-01c.md`: only B28-01d's repair of P5a/P5b in
`93db0679fc06d4c51733b47a640c307128a5631a:docs/b28_01rb_review.md`.
The earlier accepted bindings, P1–P4, controls, regression and launch
preflight remain accepted. Unchanged hashes are checked here to establish
that boundary; their arithmetic is not re-reviewed or rerun.

**COMPUTED.** At the refreshed preflight, `b28-01r` was clean at the required
HEAD `93db0679fc06d4c51733b47a640c307128a5631a`, matching origin. The document,
results directory and `analysis/b28_01rc_*` prefix were absent. The producer
tip matched `ls-remote`. No pre-existing untracked file was modified.
Git reads used the owner execution context or a per-command safe-directory
setting; no Git configuration was changed.

**COMPUTED — raw launch-file bindings.** Hashes name the exact on-disk bytes,
including original line endings:

| File | SHA-256 |
|---|---|
| `B28_COMMON.md` | `06799a9e404fc45a0944f7fcae88d8dd5511f7721f704ebe69872dd3061c87b9` |
| `R28-01c.md` | `947405cefedc81b425263c356d318c506a1d5b2b3e4ee72e4ac1f1c85b2ddbdc` |
| `BATCH28_BOARD.md` | `34b0852845c0e4caca809e4f2bdfb10e1b36ffa492f61380dfd3678de7809e81` |

## Bindings: ACCEPT

**COMPUTED.** Producer tip
`0f7af8b11e55da20cd135c73d04554a0360dd97f` has sole parent
`5a3174cd3a1ec96b05b92a8bcb73fbee58c0544b`. All 64 changed paths are additions
within `analysis/b28_01d_*`, `results/b28_01d/`, or `docs/b28_01d_report.md`.
All 63 payload lengths and SHA-256 values match the raw committed blobs;
together with the manifest they exhaust the changed paths. The producer
manifest SHA-256 is
`2129631d0b9189c4bd21a6ebafb8b148ff49dfb94829d9ad6adda9eaf66d3d90`.
`BINDINGS.json` records every path, byte count and hash.

**COMPUTED.** All nine new frozen entries match `~/b28_01/frozen_d`.
The six unchanged entries are byte-identical to `frozen_c`, its committed
hash list, and their committed source/rate blobs where applicable. All 11
old `frozen_c` entries also still match. The prior review manifest remains
`5068e6cdabfb0d578bb5c1c5f3d02ba36f15542e5c3bcfba63cae5bd1266d4b4`.

| Frozen input | Raw SHA-256 | Assessment |
|---|---|---|
| Driver | `f6fe04e239d28fa4ff89e8a103b4dd2b9b9f93ae146cbd3f64e0ec86ce49e23e` | **COMPUTED:** unchanged |
| Model | `73dbb5ac318cda4328659f95f6e26f6081241ee4ee029033498961f35dca4400` | **COMPUTED:** unchanged |
| Verifier | `fcac55b4eca11330048ed3f6a1401d6dfdbbe8a1a185ae36991e618f6a5e2532` | **COMPUTED:** unchanged |
| Verifier C source | `5166db3b1ff07d23d3a4c51d9430de1a9808dff9d1e5d4d92b802a98904995f7` | **COMPUTED:** unchanged |
| Verifier binary | `a5e8399d1e78e285a5864098dbe43d68f618c331a03705bbcb9df4e4dfd60fe6` | **COMPUTED:** unchanged |
| Rates | `665e9da1dd997b4318976c0a617d52f09f924f53e0fe2c451a7b0afce4787d1b` | **COMPUTED:** unchanged |
| New supervisor | `af3b5aa285713e20633189288589953b715d3027cb75432b959f0a485a2f7258` | **COMPUTED:** host equals committed bytes |
| New launcher | `461a92de9be6189f2ee1f64af4eddceb292d2dcbf3ba38df337dcc2e985970e6` | **COMPUTED:** host equals committed bytes |

## P5a — whole-job cleanup: ACCEPT

**READ / HAND.** The bound `supervise.diff` compares the old and new committed
supervisors. In `0f7af8b1:analysis/b28_01d_supervise.py`, `main` saves
`pgid = proc.pid` independently of the leader's exit. `become_subreaper`
enables adoption of orphaned descendants. `reap` collects exited children
without stealing the Popen leader's exit status. `stop_group` sends SIGTERM
and waits through the existing 30-second grace period, then calls `sweep`.
`sweep` repeatedly kills surviving group members and adopted children, reaps
and rechecks; return requires the leader to have exited, the group to be
absent and no live adopted child to remain. A normal step exit also invokes
this cleanup. The supervisor stays outside the killed step group so that
it can write the resource-stop receipt.

**HAND.** This addresses the specific earlier defect: the leader's exit
alone no longer authorizes return. Adoption and reaping support the requested
whole-job cleanup; they do not change producer/verifier arithmetic. Cleanup
can include the preserved grace period: the deadline triggers termination,
and a resistant child is forcibly killed after that grace. The test does
not claim that cleanup itself takes zero time.

**COMPUTED.** The reviewer reran the same TERM-resistant child behavior as
R28-01b: ignore SIGTERM, write its PID, sleep 40 seconds, under a two-second
supervisor deadline. Exit is now 124 with a wall-stop receipt. The child is
listed among the supervisor's SIGKILLed survivors; the reviewer independently
finds neither its `/proc` entry nor its process group after return. The receipt
records zero remaining job processes. No fallback reviewer kill was needed.

**COMPUTED.** A normally exiting parent that leaves a background child also
returns 0 only after that child is killed and reaped. Independent PID and
group checks confirm absence. This checks the newly added normal-exit sweep.

## P5b — checks at completion: ACCEPT

**READ / HAND.** The new `boundary` helper checks artifact size and the
monotonic deadline. `main` invokes it after step cleanup and before either
the next step or returning the step's status; it invokes it again before
the final success return. A detected size excess returns 125 with an artifact
receipt, and an expired deadline returns 124 with a wall receipt. Existing
resource-stop paths already terminate dispatch. Polling checks remain in
place. These changes close the successful-fast-exit path identified by P5b.

**COMPUTED.** The reviewer's original fast writer creates exactly 2,048 bytes
against a 1,024-byte limit. It now returns 125, with an artifact receipt that
identifies the step-exit boundary. A second run adds a marker-writing step;
only the first step is recorded, exit remains 125, and no marker exists.
All groups are absent at return. These small sizes exercise the same code
as the launcher's fixed 50,000,000,000-byte artifact limit.

**COMPUTED — ordinary control.** The prior ordinary wall control, a
three-second cap on `/bin/sleep 60`, returns 124 with a wall receipt and
zero remaining job processes. The reviewer independently confirms the
process group is absent. No driver/verifier or other matrix control is
dispatched in this slot.

## Launch preflight: ACCEPT

**READ / HAND.** `cellA.diff` shows only the updated header, frozen directory,
supervisor name/hash and supervisor invocation. The 86,400-second monotonic
budget, one 24,000,000,000-byte scope, zero swap, 64,000,000,000-byte free-disk
check, 50,000,000,000-byte artifact limit, no-recompile checks, prior-output
checks and all unchanged input bindings are preserved.

**COMPUTED.** The hash-checked new launcher was invoked exactly once with
`--preflight-only`. It returned 0, passing the actual input/library bindings,
mtime guard, absence of prior target output, free memory and free disk checks.
Its command, observed resource values, stdout hash and elapsed time are in
`binding_receipt.json`. This does not reserve those resources for a later
launch; the measurement command repeats the preflight.

**READ — frozen command for the separately authorized measurement.**

```bash
bash ~/b28_01/frozen_d/b28_01d_cellA.sh
```

## Evidence and resources

**COMPUTED.** `CONTROLS.json` contains deterministic fixture outcomes.
Commands, PIDs, clocks, process receipts and runtime measurements are in
`controls_receipt.json` and `fixture_receipts/`. These small files were written
directly into the review results directory and are included in the manifest.
No `/tmp` recovery or substitution of producer outputs is used in this review.
Every hash names raw bytes, without decoding, newline conversion or Git
filtering. The saved diffs preserve the exact context whitespace.

**READ / COMPUTED — harness correction.** The first reviewer fixture
invocation stopped at Python parsing because `pass` was mistakenly used as
a dict keyword argument. No fixture or matrix work started. The unchanged
failed source is preserved as `analysis/b28_01rc_controls_attempt1.py`, bound
in `controls_attempt1_receipt.json`. After correcting the harness, one complete
fixture invocation passed all five checks. This was a reviewer harness issue,
not a producer-code change or a failed supervisor control.

**COMPUTED.** The passing fixtures ran sequentially in one scope with
`MemoryMax=512000000`, `MemorySwapMax=0`, and a 60-second outer timeout.
The binding/preflight and final bookkeeping invocations each used a
60-second timeout and a 500,000 KiB address-space limit, equal to 512 MB decimal.
`RESOURCE_RECEIPT.json` accounts for all four invocations, including the
parser failure; total measured runtime is below the slot's 15-minute cap.
No installs, matrix work, Cell A/Cell B build, host-frozen-file edits, other
session, subagent, or automatic continuation occurred.

## Registered outcome

| Rung | Outcome | Achievement level |
|---|---|---|
| Bindings | **ACCEPT** | **READ / COMPUTED:** raw-byte provenance |
| P5a | **ACCEPT** | **READ / HAND / COMPUTED:** process cleanup |
| P5b | **ACCEPT** | **READ / HAND / COMPUTED:** completion-boundary stops |
| Required fixtures and ordinary control | **ACCEPT** | **COMPUTED:** supervisor checks only |
| Launch preflight | **ACCEPT** | **READ / HAND / COMPUTED:** engineering checks |

**B28-01b may launch: YES.**

**HAND.** No achievement level moves. This review establishes no new source
condition, coefficient equation, separation on padding, positive multiplicity
gap, geometric noncontainment, equation-existence result or asymptotic bound.
**READ:** "No five-row determinant equation is known to be nonzero on padding."
Programme decision: "no construction ready."
