# B28-01d — launch supervisor repairs P5a and P5b (Claude Code producer)

**HAND — outcome 1, Repaired.** P5a and P5b are implemented as R28-01b's review specifies:
- both of R28-01b's fixtures now behave as required;
- all of B28-01c's supervisor controls still pass;
- the driver, verifier, model, rates and C code are byte-identical to B28-01c.

Only the supervisor and the launcher were refrozen. Cell A was not built. No achievement level moves.
READ: "No five-row determinant equation is known to be nonzero on padding." Programme decision:
"no construction ready." B28-01b needs R28-01c's YES **and** the user's go.

Labels: READ = committed text, HAND = own reasoning, COMPUTED = exact run in this slot. Every SHA-256 names raw bytes.

## 1. Preflight (COMPUTED)

**Launch files.** Raw SHA-256 of the files read at launch:

| file | sha256 |
|---|---|
| `B28_COMMON.md` | `06799a9e404fc45a0944f7fcae88d8dd5511f7721f704ebe69872dd3061c87b9` (matches the board) |
| `B28-01d.md` | `e26a0914ef65e63af7f14078151cc33bfc06453fde53740ca551d219b7c7b240` (matches the board) |
| `BATCH28_BOARD.md` | `34b0852845c0e4caca809e4f2bdfb10e1b36ffa492f61380dfd3678de7809e81` |

**Branch and review.**
- Branch `b28-01`, HEAD `5a3174cd3a1ec96b05b92a8bcb73fbee58c0544b`, clean worktree.
- `origin/b28-01r` = `93db0679fc06d4c51733b47a640c307128a5631a`.
- `docs/b28_01rb_review.md` is present there.
- `results/b28_01rb/MANIFEST.json` SHA-256 = `5068e6cdabfb0d578bb5c1c5f3d02ba36f15542e5c3bcfba63cae5bd1266d4b4`.

**Host state.**
- `~/b28_01/frozen_c` matches all 11 lines of `results/b28_01c/frozen_c_hashes.txt`.
- The output paths were absent.
- No leftover fixture process was running.

**READ.** R28-01b in full; its P5 section governs, together with its supervisor-control script.

## 2. The repairs (HAND), `analysis/b28_01d_supervise.py`

**P5a — whole-group termination.**
- The supervisor makes itself a child subreaper (`prctl(PR_SET_CHILD_SUBREAPER)`). Every orphaned job process is therefore re-parented to it and stays visible.
- The group id is kept separately from the `/usr/bin/time` leader (`pgid = proc.pid` under `start_new_session`).
- On a stop, the sequence is:
  1. SIGTERM the group;
  2. wait up to 30 s for the leader, the group and every descendant to be gone;
  3. then loop: SIGKILL the group and every live descendant, reap, recheck;
  4. return only when the leader has been waited for, `killpg(pgid, 0)` finds no member, and no live child remains.
- The receipt is written after the loop by the supervisor itself. The supervisor is outside the killed group, so receipt writing survives.
- The same sweep runs after every normal step exit. Leftover background processes are killed and listed in the receipt as `survivors_sigkilled`.
- Each step record now carries `pgid` and `group_alive_after_step`. The receipt carries `job_processes_remaining_at_end`.

**P5b — checks at completion boundaries.**
- Immediately after each step exits, the supervisor rechecks two things, before any next step and before a success return:
  1. the artifact size (checked first);
  2. the monotonic deadline.
- An excess returns **125**, or **124** for the deadline, with the resource-stop receipt.
- A final boundary check also precedes `finish(0)`.
- Checks at each poll are unchanged.

**Order after a step.** The checks run in this order:
1. a supervisor-initiated stop;
2. an OOM SIGKILL (137);
3. the boundary check (P5b);
4. the step's own exit code.

**Launcher (`analysis/b28_01d_cellA.sh`).** It is `b28_01c_cellA.sh` with only four changes (`diff`):
1. the header;
2. `F=$HOME/b28_01/frozen_d`;
3. the supervisor's name and hash in the embedded list;
4. the supervisor invocation.

Everything else is unchanged:
- the preflight: bindings, library versions, no recompile, no prior output, `MemAvailable` ≥ 24,000,000,000, and free disk ≥ 64,000,000,000;
- the 50,000,000,000-byte artifact stop;
- the single 24,000,000,000-byte scope with no swap;
- the 86,400 s monotonic cap.

`~/b28_01/frozen_d` holds byte-identical copies of the unchanged files, plus the new supervisor, launcher and controls.

## 3. Controls (COMPUTED)

The harness `b28_01d_controls.py` ran in **one** scope: `MemoryMax=8000000000`, `MemorySwapMax=0`, outer `timeout 1800`. `scope_limits_receipt.txt` records the effective limits. The run took 47.1 s and met all expectations. Per-step records are in `out_d/controls_receipt.json`.

| control | expected | got |
|---|---|---|
| `sup_wall` (B28-01c): 3 s cap on `sleep 60` | 124, wall stop, nothing left | yes (3.0 s), 0 processes remaining |
| `sup_artifact` (B28-01c): slow writer, 10 MB stop | 125, artifact stop | yes |
| `sup_ctl` (B28-01c): driver then verifier on the control cell | 0, 0, FULL_RANK | yes |
| **`fx_term_resistant`** (R28-01b): child ignores SIGTERM, 2 s deadline | 124, **no process alive** | 124; the child was SIGKILLed after the 30 s grace and is gone; 0 job processes remaining |
| **`fx_fast_writer`** (R28-01b): 2,048 bytes against a 1,024-byte stop | **125 with receipt** | 125, `resource_stop.reason = artifact`, "at the exit of step writer" |
| `fx_fast_writer_two_step`: the same writer, then a marker step | 125, marker never runs | yes; 1 step recorded, no marker |
| `fx_stray_child`: step exits 0 leaving `sleep 120 &` | 0, stray killed, none alive | yes |
| `launcher_preflight`: `b28_01d_cellA.sh --preflight-only` | 0 | yes |

Under the frozen B28-01c supervisor, R28-01b recorded two failures on these fixtures: the TERM-resistant child survived, and the fast writer returned exit 0. **HAND:** the P5a sweep and the P5b boundary check are exactly what change those results.

A dev run of the same harness, from `~/b28_01/d_dev` in its own 8 GB scope, also met every expectation before the freeze. Both runs are logged in `RESOURCE_RECEIPT.json`. A `pgrep` after each run found no fixture process.

## 4. Hashes

**Unchanged** (COMPUTED, `results/b28_01d/UNCHANGED.json`; byte-identical in `frozen_c`, `frozen_d` and the committed `analysis/` sources):

| file | sha256 |
|---|---|
| `b28_01c_driver.py` | `f6fe04e239d28fa4ff89e8a103b4dd2b9b9f93ae146cbd3f64e0ec86ce49e23e` |
| `b28_01c_model.py` | `73dbb5ac318cda4328659f95f6e26f6081241ee4ee029033498961f35dca4400` |
| `b28_01c_verify.py` | `fcac55b4eca11330048ed3f6a1401d6dfdbbe8a1a185ae36991e618f6a5e2532` |
| `b28_01c_vfy.c` | `5166db3b1ff07d23d3a4c51d9430de1a9808dff9d1e5d4d92b802a98904995f7` |
| `b28_01c_vfy.so` | `a5e8399d1e78e285a5864098dbe43d68f618c331a03705bbcb9df4e4dfd60fe6` |
| `gate_rates_c.json` | `665e9da1dd997b4318976c0a617d52f09f924f53e0fe2c451a7b0afce4787d1b` |

The engine files and `schur.so` are unchanged too. The launcher still checks them against the same embedded list.

**Refrozen.** New hash list: `results/b28_01d/frozen_d_hashes.txt`, 9 files.

| file | old | new |
|---|---|---|
| supervisor | `b28_01c_supervise.py` `772979a1…` | `b28_01d_supervise.py` `af3b5aa285713e20633189288589953b715d3027cb75432b959f0a485a2f7258` |
| launcher | `b28_01c_cellA.sh` `3e823c4d…` | `b28_01d_cellA.sh` `461a92de9be6189f2ee1f64af4eddceb292d2dcbf3ba38df337dcc2e985970e6` |
| controls (new) | — | `b28_01d_controls.py` `22ab35a6bbdcb75cf9746e7bc5688f78e8d2afbbf9fa4d4573fb4dcc59f8a856` |

No committed `b28_01_*` or `b28_01c_*` file was modified.

## 5. Frozen launch for B28-01b

```
bash ~/b28_01/frozen_d/b28_01d_cellA.sh                  # the measurement
bash ~/b28_01/frozen_d/b28_01d_cellA.sh --preflight-only  # checks only
```

Exit codes are unchanged from B28-01c:

| exit | meaning |
|---|---|
| 0 | FULL_RANK |
| 8 | MODULAR_DEFICIENCY |
| 3 | gate stop |
| 4 | source/check failure |
| 6 | prime disagreement |
| 5 | replay rejected |
| 124 / 125 / 137 | resource stop: wall / artifact / memory |

## 6. Resources

- One aggregate scope, 47 s, for the registered harness; plus one dev scope, about 47 s.
- No installs, no matrix work beyond B28-01c's registered small-cell supervisor control, no Cell A.
- Host-retained: the 20 MB `sup_artifact` blob, bound in `HOST_RETAINED.json`.
- Keep `~/b28_01/frozen_d` for B28-01b and R28-01c.

## 7. Outcome

| rung | outcome |
|---|---|
| P5a | implemented; the TERM-resistant child leaves no process alive |
| P5b | implemented; the fast writer returns 125 with the receipt; no later step runs |
| old supervisor controls | pass |
| non-supervisor hashes | unchanged (listed) |
| **registered outcome** | **1. Repaired** |

**Achievement level:** none moves (engineering only). "No five-row determinant equation is known to be nonzero on padding."
