# Resource receipt

UNCOMMITTED / PRODUCER ONLY. A26-03, registered outcome 3 (REJECTION).

| Item | Actual record |
|---|---|
| Session origin | 2026-09-23T01:29:21Z, this task's saved session metadata |
| First explicit UTC clock read / preflight start | 2026-09-23T01:29:37Z |
| First incremental report written | 2026-09-23T01:33:08Z |
| Early checkpoint and mathematical stop | 2026-09-23T01:35:25Z |
| Mathematical-work upper bound | 6m04s from session origin, including interleaved administration; 5m48s from the first explicit clock read |
| 45-minute checkpoint | Not reached; the early registered rejection closed research. No later checkpoint time is claimed. |
| 90-minute ceiling | Respected, without interruption deductions |
| Final pre-seal branch/HEAD observation | 2026-09-23T01:38:04Z; batch15-launch at 7464a2bd02c9740db55d15ac43571cca74acea5f, unchanged |
| Interruptions | None; no deductions |
| Pilots | 0 |
| Mathematical programs, symbolic tests, exact-arithmetic evaluators, certificate replays, random searches | 0 |
| Compute leases acquired, altered or invented | 0 |
| Subagents, other sessions launched/read/messaged, dependency installs, publication, automatic continuation | 0 |
| Git mutations | 0; no staging, commit, push, fetch, checkout, reset, clean, config, attribute or ignore change |

Model and freshness: own session metadata says gpt-6-astra, xhigh, task
01a0cbe1-b51e-7b00-b1f7-525b906c89fc. It is not the earlier expander-notes
session 01a0c159... and not the coordinator task. No tool memory is evidence.

Administrative operations: Get-Content / file inventory / Get-FileHash;
read-only git -C commands; own session metadata fields for identity; UTC
clock reads; apply_patch to new authorized report/results files; and PowerShell
.NET raw-byte Git reads, SHA-256, JSON/manifest generation and verification.
ADMIN_SEAL.ps1 contains only these administrative operations. Reading the own
session metadata is not reading another task.

One attempted administrative hash command could not start because python was
not on PATH; no Python code executed and nothing was installed. PowerShell
.NET performed the hashes instead. One proof-file patch was rejected for a
malformed patch line before writing; the corrected patch succeeded. These are
administrative failures, not mathematical pilots, and no time is subtracted.
Git's warning about an unreadable global ignore file was left alone.

The symbolic sums in PROOF.md, the rational lower bounds, and the operation
prices in CHECKPOINT.md were derived by hand. No sum, determinant evaluator,
grid, rank calculation or identity-verification program was run.

Pre-existing untracked paths retained:
docs/a26_02_review.md; results/a26_02/; results/a25_10/literature/;
results/b15_integrator/. No tracked/staged difference was present at either
observed status. Output writes are only docs/a26_03_report.md and results/a26_03/.
The manifest and proposed list bind the exact final inventory.

Packet preparation stop: 2026-09-23T01:39:02Z (9m41s after session origin),
with byte-only final sealing and verification following. At that observation
the manuscript had been read back, all 20 input bindings had zero CR bytes
(their hashes therefore name LF committed blobs), and both tracked and staged
Git diffs were empty. The initial seal verified all five governing audit
payloads and all eight output payloads; the final seal repeats raw hashing
after these receipt/wording updates. No mathematical work resumed after the
01:35:25Z checkpoint.
