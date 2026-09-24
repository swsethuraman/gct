# B28-01b — Cell A measurement: report

**Exit: launcher 0, verifier `FULL_RANK`.**
Per the brief's table, this is recorded as **COMPUTED: no determinant equation in this cell.**

- **Cell A:** `λ = (12,8,6,4,2)`, `k = 8`, `a = 109`, `n_χ = 813,314`.
- **Primes:** both agree (2,147,483,647 and 2,147,483,629).
- **Independent replay** at 2,147,483,647: `FULL_RANK`, with all 16 checks true.

Producer: Claude Code (B28-01a/c/d lineage), fresh session, 2026-09-24. Branch `b28-01`,
parent `0f7af8b11e55da20cd135c73d04554a0360dd97f`.

## 1. Preflight

**COMPUTED — raw SHA-256 of the launch files, on-disk bytes:**

| file | sha256 |
|---|---|
| `B28_COMMON.md` | `06799a9e404fc45a0944f7fcae88d8dd5511f7721f704ebe69872dd3061c87b9` |
| `B28-01b.md` | `66cd584e5e9726bb427da14d2dc768a6f342f59c6896287f0f23e9e4918b482f` |
| `BATCH28_BOARD.md` | `886cd9db2c0962e601db3940282bac84971ed7e03368407a8763f6d2e24ba3b3` |

The board's own table lists `B28-01b.md` at the same hash.

**COMPUTED — repository state:**
- Branch `b28-01` HEAD was `0f7af8b1…`, equal to `ls-remote origin b28-01`.
- The worktree was clean, with no untracked files.
- `docs/b28_01b_report.md` and `results/b28_01b/` were absent.

**COMPUTED — review commits:** `8a86fec1` (R28-01), `93db0679` (R28-01b) and `ff62d929e53e…`
(R28-01c) are all on `b28-01r`, which equals origin.

**READ — clearance:** `ff62d929:docs/b28_01rc_review.md` says "B28-01b may launch: YES."
`ff62d929:results/b28_01rc/MANIFEST.json` hashes to
`66eb68fc311b475a9bdf6b92431646ec10cf3ed43061d89f6f3f78ad6ee45f99`, as the brief states.

**COMPUTED — frozen files:** all nine files in `~/b28_01/frozen_d` match
`0f7af8b1:results/b28_01d/frozen_d_hashes.txt`. They include the supervisor `af3b5aa2…` and the
launcher `461a92de…`. They were re-checked after the run and are unchanged.

**COMPUTED — launcher preflight:** `bash ~/b28_01/frozen_d/b28_01d_cellA.sh --preflight-only`
exited 0 (`results/b28_01b/preflight_stdout.txt`):
`PREFLIGHT OK: bindings, no-recompile, no prior output, MemAvailable=28532994048, free disk=1022409691136`.

**READ — host conditions:** the user confirmed that the laptop was plugged in, sleep was off, and
the browser and heavy apps were closed. Section 4 records that **the host went into idle sleep
anyway** during the verifier step.

## 2. The run: executed exactly once

The command was `bash ~/b28_01/frozen_d/b28_01d_cellA.sh`, invoked through
`results/b28_01b/launch_wrapper.sh`. The wrapper only tees stdout and records the exit code.
- **Launched:** 2026-09-24T19:54:41Z. **Ended:** 20:28:25Z.
- Nothing was edited, recompiled, retried, reseeded or extended.
- No other prime, point or cell was used, and Cell B was not run.

The launcher's final lines, verbatim (`launch_stdout.txt`):

```
JOB exit=0 resource_stop=None
FULL_RANK at 2147483647 (both primes agree; independent replay FULL_RANK)
```

**COMPUTED — driver certificates:**
- Per-prime results: `out_cellA/12_8_6_4_2_d8_p{2147483647,2147483629}_cert.json`.
- Both primes have outcome `FULL_RANK`, with:
  - `mult_det = 109`;
  - `projected_nullity = rank_K = 109`;
  - `verified_on_all_rows = true`;
  - a nonzero 109-minor of `VK` (117 × 109).
- Minors mod p: `763718730` at 2,147,483,647 and `124471553` at 2,147,483,629.
- `12_8_6_4_2_d8_primes.json`: verdict `AGREE`.

**COMPUTED — independent verifier:**
- File: `out_cellA/12_8_6_4_2_d8_p2147483647_verify.json`.
- Verdict: `FULL_RANK`.
- Every check below is true:
  - `n_chi_matches_frozen`, `E_matches_producer`, `cover_matches_producer`;
  - `projection_recipe_registered`, `G1_cover_pivots`, `G_matches_producer`, `G2_residual_rank`;
  - `K_file_matches_cert`, `K1_EK_zero_all_rows`, `K1b_rank_K`;
  - `pencils_match_generator`, `point_count_registered`, `VK_matches_producer`;
  - `mult_det_matches_claim`, `M1_claimed_minor_nonzero`, `outcome_label_matches`.
- The verifier regenerated `E`. `E_sha256` = `7f37eee6…1938`, with `rows_E = 2,310,607`,
  `nnz_E = 10,062,442` and `N_S = n_χ = 813,314`.
- `rank_G = 3549`, which equals `nU − a = 3658 − 109`.

## 3. Measured sizes, time and memory

**COMPUTED — gate** (`out_cellA/12_8_6_4_2_d8_receipt.json` and `_cell.json`):
- **Measured `z` = 10,062,442.** This is `nnz E`, about `12.37 n`.
- **Measured `U` = 3,658.**
- The cover has size 809,656, using the "reversed" order.
- `f_measured` = 0.436%.
- The gate passed, with a memory envelope of 5,570,466,536 bytes and 1,900.9 s of predicted
  remaining time.

**COMPUTED — time and memory** (`job_cellA/job_receipt.json`, `*.time`,
`*_verify_receipt.json`):

| step | monotonic s | GNU `time` elapsed | peak RSS |
|---|---|---|---|
| producer, `cellA_driver` (build, cover, both primes, compare) | 334.984 | 5:34.98 | 3,345,821,696 B |
| replay, `cellA_verify` | 641.794 | 28:08.92 | 1,137,893,376 B |
| whole job | **976.779** | UTC 19:54:41 to 20:28:25 (2,024 s) | scope `memory.peak` **4,087,738,368 B** |

- Producer phases at the first prime:
  - build 3.8 s;
  - cover 1.1 s;
  - Schur 125.7 s;
  - lift and check 7.8 s;
  - evaluation 31.9 s.

  The second prime took about the same time.
- The verifier's Schur phase took 583.8 s.
- Scope memory events: `oom 0`, `oom_kill 0`, `max 0`.
- At the end, the artifacts totalled 722,344,199 bytes and no job process remained.
- Both compiled binaries were unchanged after the run (`job_cellA/post_run_binaries.sha256`).

## 4. Host deviation: idle sleep during the verifier step

**COMPUTED** (`results/b28_01b/host_power_events.txt`, from the Windows System log):
- The laptop entered sleep at **2026-09-24T20:09:49.6Z**, with "Sleep Reason: System Idle".
- It woke at **20:27:21.4Z**, about 1,052 s later.
- The wake source was the USB host controller.
- `powercfg` shows the AC "Sleep after" timeout set to 900 s. So sleep was **not** off, even
  though the host conditions had been confirmed.
- The machine was on AC power.

The suspension falls entirely inside `cellA_verify`. That explains the gap between the verifier's
GNU `time` elapsed (28:08.92) and its monotonic time (641.8 s). The supervisor's
`time.monotonic` budget did not count the suspended interval.

**HAND:**
- The certificates are exact finite-field computations whose checks are recorded bit for bit.
  Their content does not depend on timing.
- The verifier completed with every check true, and the process exited normally with no signal
  and no OOM.
- The suspension therefore affects only the wall-time receipt, not the verdict.
- This is recorded as a deviation from the preregistered host conditions. It is not an exit
  label. Whether it bears on acceptance is for the reviewer.

## 5. Delivery

- `results/b28_01b/` contains:
  - `out_cellA/`: the certificates, verifier output, primes file, gate receipt, cell record,
    `cover_U`, `VK` files and pencils;
  - `job_cellA/`: the supervisor receipt, logs and GNU `time` files;
  - the launch stdout, metadata and wrapper, and the preflight stdout;
  - `host_power_events.txt`, `RESOURCE_RECEIPT.json`, `HOST_RETAINED.json` and `MANIFEST.json`.
- Four files over 5 MB stay on the host under `~/b28_01/out/cellA` and are bound by hash in
  `HOST_RETAINED.json`:
  - both `K` kernels, 354,604,904 bytes each;
  - `cover_S` and `cover_rows`, 6,477,376 bytes each.
- The `K` hashes equal the `K.sha256` values in the certificates.

## 6. Outcome and achievement level

- **Exit:** launcher exit 0. Both primes are `FULL_RANK` and `AGREE`.
- **Verdict:** the independent verifier returned `FULL_RANK`.
- **Record:** COMPUTED: no determinant equation in this cell. In the brief's words: `mult_det = a
  = 109` over ℚ at Cell A.
- **Achievement level:** this closes the degree-8 Cell A negatively. **No equation exists
  there**, as a COMPUTED certificate that is not PROVED; reviewers re-run it.
- None of the four achievements moves:
  - source condition;
  - coefficient equation;
  - separation on padding;
  - positive multiplicity gap.
- The binding constraint stands: "No five-row determinant equation is known to be nonzero on
  padding."
- Programme decision: "no construction ready."
