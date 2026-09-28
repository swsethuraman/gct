# B28-01c — R28-01's repairs P1–P5 applied (Claude Code producer)

**HAND: outcome 1, Repaired.** All five repairs, P1 to P5, are implemented.
- All 4 old controls and all 6 new ones behave as required. The launcher's own paths were also tested: 2 supervisor resource stops, 1 end-to-end run and the preflight.
- The regression is unchanged: every matrix, kernel, rank, minor and cover output is byte-identical to B28-01a.
- Repriced with P3 and P4, Cell A still fits the approved 24 h / 24 GB in all six scenarios:
  - at most 3.785 h;
  - at most 17.20 GB of estimated need, under the 18 GB gate (75% of 24 GB).
- Cell A was **not** built or started.

**No achievement level moves.** READ: "No five-row determinant equation is known to be nonzero on padding." Programme decision: "no construction ready." B28-01b still needs R28-01b's YES **and** the user's go.

Labels: **READ** means committed text I read, **HAND** means my own reasoning, **COMPUTED** means an exact run in this slot. Every SHA-256 below names raw file or blob bytes.

## 1. Preflight

**COMPUTED: raw SHA-256 of the launch files.**

| file | sha256 |
|---|---|
| `B28_COMMON.md` | `06799a9e404fc45a0944f7fcae88d8dd5511f7721f704ebe69872dd3061c87b9` (matches the board) |
| `B28-01c.md` | `d4c7909fa3fe13981562e34fe1f4160d01bc0ad55702feb536ae227305368b93` (matches the board) |
| `BATCH28_BOARD.md` | `69d0f6328e0ebcd9dc6e744e502686f69257fad5bb9a5fb56a8427e9601c3e1d` |
| `B28-01a.md` | `3975e63fbf3873e01ea4f64a6bb43a1d009cdaa5d39ea0d37b09f624419307b5` (matches the board) |

The board hash differs from the `01a20dd5…` that R28-01 recorded. **HAND:** the difference is expected, because the board was edited afterwards to add the B28-01c and R28-01b rows.

**COMPUTED: branch and review checks.**
- Branch `b28-01`, HEAD `a1c3c3a69b789c91909ed5476354ad762f3e71c2`, and the worktree was clean.
- `b28-01r` is at `8a86fec17b72b565baaef7f9e29709d1ced35168` locally and on origin.
- `docs/b28_01r_review.md` exists at that commit. Its `results/b28_01r/MANIFEST.json` has SHA-256 `5ffcc018b5e5a29effb2e31dc3e4ac171b13a5e9d7ad63816a3dd250544eb8a6`, as the brief requires.

**COMPUTED: host checks.**
- `~/b28_01/frozen` matches `results/b28_01/frozen_v2_hashes.txt` on all 6 lines. I did not modify it.
- The six committed calibration receipts are byte-identical to their host copies under `~/b28_01/out`.
- None of the output paths existed beforehand.

**READ.** I read R28-01's review in full, together with the frozen driver, verifier, launcher, repricer and wrapper at `a1c3c3a6`. I also read the parts of the preregistration that cover disk, the gates and exits.

## 2. The repairs (HAND, as implemented)

New frozen code lives in `analysis/b28_01c_*`, with the host copy in `~/b28_01/frozen_c`. I did not touch the committed `analysis/b28_01_*` or `results/b28_01/`.
- **Unchanged regenerating mathematics.** In the verifier, everything from `exponent_vectors` to `fl_rank` is byte-identical to `b28_01_verify.py` (COMPUTED by diff).
- **Unchanged arithmetic.** The driver's arithmetic is B28-01a's.
- **Unchanged C solve.** `b28_01c_vfy.c` is byte-identical to `b28_01_vfy.c` (`5166db3b…`), and `b28_01c_vfy.so` is a copy of the frozen `a5e8399d…`, so nothing was recompiled.

**P1: control flow in the driver.**
1. **Nullity check before the lift.** If the projected nullity is not `a`, the driver writes the failed-source certificate and receipt and exits 4. This happens before `Kc(n,nul)` is allocated and before the next prime.
2. **Stop on a failed check.** If the all-row `E K` check fails, the loop breaks and the driver exits 4 before the next prime. The same applies if the rank of `K[U,:]` is below `a`, or if any deficiency candidate fails a check.
3. **Deterministic rank.** `rank_tall` (randomized, with retries) is gone. Its replacement is the flint rank of `Kc[U,:]`.
4. **Prime comparison.** After both source gates pass, the driver compares `mult_det` and the outcome category across the primes and writes `{tag}_primes.json`. If they disagree, it writes `INCONCLUSIVE CONTROL FAILURE` and exits 6, with no verifier and no further prime.

**P2: certificate checks in the verifier, plus the driver side.**
- **Registered recipe.** The verifier rebuilds the projection recipe from `p` and `|U|`: base seed 20260908, attempt 0, `pseed = base + 7919·attempt + p mod 1000`, `m = |U|+64`, 8 projections. Every recorded field must equal it. `G` is formed from the rebuilt recipe, never from the certificate's.
- **`FULL_RANK` verdict.** It needs a complete `a`×`a` minor: `a` distinct in-range row indices, with a determinant that is nonzero and equal to the claim.
- **`MODULAR_DEFICIENCY` verdict, with lower bound `r`.** It needs the following, and each candidate is reported separately:
  - the candidate and combination files, with count `a−r`, shapes and hashes as certified;
  - every candidate nonzero;
  - the candidates independent, meaning their rank on the `U` coordinates is `a−r`;
  - `E v = 0` on every row;
  - every candidate zero at every saved point, where the points' evaluation rows are regenerated;
  - each candidate equal to `K c` for its saved combination.
- **Verdict labels.** The verifier's verdicts are `FULL_RANK` (exit 0), `MODULAR_DEFICIENCY` (exit 8) or `REJECT` (exit 5). The word "drop" appears nowhere.
- **Driver side.** The driver saves the combinations and checks the same four properties: nonzero, independent, the `E` equations, and zero at every saved point (rows regenerated in batches of eight). Any failure exits 4.

**P3: verifier time at the gate.** The shared `b28_01c_model.py` gives the gate and the repricer identical formulas.
- The rate file (`gate_rates_c.json`, `665e9da1…`) keeps both coefficient sets and `verifier_ratio_up = 2.7389`. That is the maximum of the six verifier/producer ratios (cH: 2.738894…), rounded up.
- The gate charges `max(direct verifier model, 2.7389 × producer six-phase model)`.
- **COMPUTED cross-check.** At `z=32n`, `U=4,013`, the direct verifier model gives **1,695.4 s**, which is exactly R28-01's independent figure. The new gate budgets **2,184.3 s**, where the old one budgeted 1,440.4 s.

**P4: verifier memory at the gate.** The gate now requires `max(producer envelope, verifier estimate) ≤ 0.75 × cap`.
- **Inputs.** The verifier estimate uses the actual row count, `z`, `N_S`, `|S|`, `U`, the rows outside the cover, and the nonzeros inside and outside the cover rows. All of these are measured at the gate.
- **Form.** The estimate is a phase-by-phase live set: a base, then the maximum over build, three Schur stages, lift and evaluation. The formulas are in `b28_01c_model.py`.
- **What it covers.** The three Schur stages are the projection build (with the `P·F_o` CSR, its CSC copy and the S/U slices), the dense residual, and the flint conversion of `G`.
- **COMPUTED coverage** (`results/b28_01c/GATE_MODEL_CHECK.json`). The peaks are the largest per-phase VmHWM in B28-01a's receipts and in this slot's:

| cell | verifier estimate | measured verifier peak | producer envelope | measured producer peak |
|---|---|---|---|---|
| control `(22,6,5,2,1)_9` | 1,031,435,588 | 128,798,720 | 1,785,435,512 | 110,866,432 |
| cal1 `(24,6,5,3,2)_10` | 1,302,513,072 | 919,474,176 | 2,173,950,624 | 1,176,100,864 |
| cal2 `(13,9,9,3,1,1)_9` | 9,127,518,584 | **5,651,423,232** | 4,831,800,620 | 4,026,748,928 |

The cal2 verifier peak is the one R28-01 found uncovered. The new estimate covers it with a 1.6× margin.
- **HAND consequence.** Under an 8 GB job cap, this conservative gate would stop cal2, since it needs 9.13 GB against 6 GB. So the cal2 regression passed `--mem-cap 24000000000`, the Cell A job cap, so that the full path ran. The OS scope of 8,000,000,000 bytes remained the backstop.

**P5: aggregate cap and launch preflight.**
- **Supervisor.** `b28_01c_supervise.py` sets one `time.monotonic()` deadline for the whole job. Steps run sequentially, each in its own process group. `{REMAINING}` hands the driver the monotonic budget that is left.
- **Stops.** A deadline or an artifact stop kills the whole group (SIGTERM, then SIGKILL after 30 s), and no later step runs. A resource-stop receipt is written. A SIGKILL inside the scope is recorded as a memory stop.
- **Launcher.** `b28_01c_cellA.sh` runs the supervisor inside **one** scope over producer plus replay:
  - `MemoryMax=24000000000`;
  - `MemorySwapMax=0`;
  - a backstop `RuntimeMaxSec=87000`, which is COMPUTED to be enforced on user scopes by a dev test.
- **Clock.** The launcher no longer uses `date +%s`.
- **Preflight checks** before anything is built:
  - hashes of the frozen code, rates, `.so` files and engine;
  - the Python, NumPy, SciPy and python-flint versions;
  - **no recompile:** `schur.so` must not be older than its C source, because the engine's `lib()` would otherwise rebuild it. The driver re-checks this, and the `.so` hash, in-process. The verifier refuses rather than compile.
  - no `out/cellA`, no `job_cellA`, no `out/cellA*/` directory, and no `12_8_6_4_2_d8_*` file anywhere under `~/b28_01`;
  - `MemAvailable` ≥ 24,000,000,000;
  - free disk ≥ 64,000,000,000 (the reservation);
  - the 50,000,000,000-byte artifact stop is enforced by the supervisor.
- **After the run**, the launcher re-hashes both `.so` files.

## 3. Controls and regression (COMPUTED)

**Harness.** One harness, `b28_01c_controls.py`, runs every step inside a user scope with `MemoryMax=8000000000`, `MemorySwapMax=0` and `timeout 3600`, one process at a time. `scope_limits_receipt.txt` records the effective limits. The per-step records are in `out_c/controls_receipt.json`.

| step | expected | got |
|---|---|---|
| control cell driver, both primes | exit 0, primes AGREE | yes |
| control verify at 2147483647 / 2147483629 | FULL_RANK | yes / yes |
| B28-01a corrupted kernel `K[0,0]+1` | REJECT | yes |
| B28-01a corrupted pencil entry | REJECT | yes |
| **R28-01 missing minor** | REJECT (was ACCEPT) | **REJECT**, `M1_claimed_minor_nonzero` false |
| **R28-01 false recipe annotations** | REJECT (was ACCEPT) | **REJECT**, `projection_recipe_registered` false |
| **deficiency fixture**, first 22 < a=24 points at 2147483647 | driver exit 0, MODULAR_DEFICIENCY, all driver checks true | yes, lower bound 22, 2 candidates |
| verifier, valid candidates | MODULAR_DEFICIENCY | yes; both candidates valid |
| verifier, candidate 1 replaced by `K[:,0]` (combination `e_0`, hashes re-signed) | REJECT with candidate 0 valid and candidate 1 invalid | yes: candidate 1 passes nonzero, `E` equations and `K c`, and **fails zero at the saved points** |
| **source-gate fixture** (`m=40 < |U|−a`) | exit 4 at the first prime | exit 4. Nullity 30. Phases were build, cover and one schur: no lift, no `K` file, no second-prime certificate |
| **prime-disagreement fixture** (22 points at 2147483629 only) | exit 6, INCONCLUSIVE | yes (24 FULL_RANK against 22 MODULAR_DEFICIENCY) |
| supervisor, 3 s cap on `sleep 60` | 124, wall stop | yes, killed at 3.0 s |
| supervisor, 10 MB artifact stop | 125, artifact stop | yes |
| supervisor, driver then verifier on the control cell | both 0 | yes, FULL_RANK |
| launcher `--preflight-only` | 0 | yes |
| cal1 gate-only sizing (inputs for the memory check; no Schur) | 0 | yes |
| **cal2 regression** (s79 line 121), 2147483647, driver and verifier | FULL_RANK | yes |

**HAND: fixture switches.** The fixtures use two driver switches, `--fixture-proj-m` and `--fixture-npts P:N` (with `N < a`), and one verifier switch, `--fixture-npts N`.
- Each is recorded in the certificate or verdict.
- The launcher never passes them.
- A fixture projection cannot pass the verifier's registered-recipe check.
- A fixture point count cannot yield `FULL_RANK`.

**COMPUTED: regression** (`REGRESSION.json`).
- **Control cell.** Both `K`, both `VK`, the pencils and all three cover arrays are byte-identical to `results/b28_01/control`.
- **cal2.** `K` (`d0720b65…`), `cover_S` and `cover_rows` match `results/b28_01/HOST_RETAINED.json`. `VK`, the pencils and `cover_U` match the committed files.
- **JSON values.** No hash, rank, nullity, minor, cover or dimension value changed.
- **Fields that differ.** All of them are schema fields:
  - **cell.json:** none.
  - **cert:** `schema` changed from `b28-01-cert/1` to `b28-01c-cert/1`. Added: `outcome`, `evaluation.npts`, `hybrid.rank_K_method`. The value of `rank_K` is unchanged; only its method changed.
  - **verify:** `schema` changed from `b28-01-verify/1` to `b28-01c-verify/1`, and `verdict` changed from `ACCEPT` to `FULL_RANK`. Added: `checks.projection_recipe_registered`, `checks.point_count_registered`, `checks.outcome_label_matches`, `inputs.npts`, `values.projection_recipe.{attempt,base_seed,extra,m,nproj,pseed}`.
  - **New files:** `{tag}_primes.json` for two-prime runs, and the receipt schema `b28-01c-receipt/1`, which carries the new gate fields.

**COMPUTED: timing sanity check at cal2.** These are receipt times, not certificate data.
- **Producer after the gate:** measured 106.7 s against 195.0 s predicted.
- **Verifier:** measured 376.2 s against 627.1 s predicted.

## 4. Cell A repriced (COMPUTED, `cellA_price_c.json`)

**Inputs.**
- The rates are B28-01a's calibration receipts, with the same mapping as `b28_01_reprice.py`. The coefficients reproduce `results/b28_01/host_rates.json`.
- For the scenarios, the unknown row data are bounded conservatively: rows `= ⌈0.30 z⌉` (calibration rows/z ≤ 0.277), `z_R1 = z_Fo = z`, and rows outside the cover = rows.
- At the gate, the driver uses the actual values instead.

**Totals.** Time is producer plus the gated verifier. Memory is the maximum of the producer envelope and the verifier estimate. Both columns are in decimal units.

| z/n | U | producer s | verifier direct / ratio s | total h | need GB | fits 24 h | gate 75% |
|---|---|---|---|---|---|---|---|
| 10 | 923 | 384.8 | 228.1 / 571.2 | 0.266 | 5.751 | yes | yes |
| 10 | 4,013 | 783.1 | 631.6 / 1,116.6 | 0.528 | 5.751 | yes | yes |
| 10 | 10,683 | 3,664.2 | 2,011.1 / 5,062.1 | 2.424 | 13.437 | yes | yes |
| 32 | 923 | 565.3 | 474.3 / 821.4 | 0.385 | 17.202 | yes | yes |
| 32 | 4,013 | 1,560.6 | 1,695.4 / 2,184.3 | 1.040 | 17.202 | yes | yes |
| 32 | 10,683 | 5,730.3 | 4,839.6 / 7,894.6 | 3.785 | 17.202 | yes | yes |

**HAND: risks.**
- **Memory margin.** At `z=32n`, the bounded verifier estimate of 17.20 GB is close to the 18 GB gate. The actual gate values will be lower, because `z_R1 + z_Fo = z` and the real row count applies. If the real inputs push the estimate above 18 GB, the gate stops Cell A with a sizing receipt (exit 3). That is a registered exit, not a failure.
- **Extrapolation.** R28-01's warning stands: these figures are scenarios fitted at U ≤ 1,277. The genuine aggregate cap (P5) is the enforcement.

## 5. Frozen launch for B28-01b

```
bash ~/b28_01/frozen_c/b28_01c_cellA.sh                  # the measurement
bash ~/b28_01/frozen_c/b28_01c_cellA.sh --preflight-only  # checks only
```

**Frozen hash list.** `results/b28_01c/frozen_c_hashes.txt` holds 11 files. The launcher is `3e823c4d6366a9f9bb4f5f7b7e7e6cd6e35b13008b38d079ba5283b0cd104453`, and its own bytes are bound here. Its embedded preflight list covers seven files:
- driver `f6fe04e2…`
- model `73dbb5ac…`
- verifier `fcac55b4…`
- `vfy.c` `5166db3b…`
- `vfy.so` `a5e8399d…`
- supervisor `772979a1…`
- rates `665e9da1…`

The same list also binds the repricer `c145e643…`, the fixture tool `489eb69e…` and the controls harness `580183da…`. `CODE_BINDING.json` confirms that the committed `analysis/` copies are the frozen bytes.

**Exit codes:**
- 0: FULL_RANK
- 8: MODULAR_DEFICIENCY (a lower bound only)
- 3: gate stop
- 4: source gate or check failed
- 6: prime disagreement
- 5: replay rejected
- 124 / 125 / 137: wall / artifact / memory resource stop

**Outputs.** The target output goes to `~/b28_01/out/cellA`, and the job receipt to `~/b28_01/job_cellA/job_receipt.json`.

## 6. Resources and deviations

**Resources** (COMPUTED, `RESOURCE_RECEIPT.json`).
- The harness took 557 s of the 3,600 s allowance. The largest step RSS was 3.08 GB (the cal2 driver), under the 8,000,000,000-byte scope.
- Development runs, all under 60 s, are logged in the same receipt.
- Nothing was installed.

**Deviations (HAND).**
1. **Harness attempt 1 stopped** at its 16th step, 20 s in. The launcher's `cellA*` prior-output glob matched B28-01a's legitimate pricing file `out/cellA_price.json`.
   - The first 15 steps had met their expectations.
   - I narrowed the check to directories and added a search for any `12_8_6_4_2_d8_*` file, then refroze the launcher (`9646ee37…` became `3e823c4d…`).
   - I reran the whole harness from a fresh output directory.
   - The attempt-1 records are in `results/b28_01c/attempt1/`.
   - As a result, the controls ran in **two sequential scopes** of the same 8 GB class, not one. Their combined time is 557 s.
2. **The cal2 regression's gate used the 24 GB Cell A cap** as its parameter (see P4), not 8 GB.

**Host-retained files.** Files over 5 MB are not committed. They are bound in `results/b28_01c/HOST_RETAINED.json`: cal2 `K`, `cover_S` and `cover_rows`, and the supervisor test blob. **Do not delete** `~/b28_01/frozen_c`, `~/b28_01/out_c` or `~/b28_01/out` before B28-01b and R28-01b.

## 7. Outcome

| rung | outcome |
|---|---|
| P1 | implemented; source-gate and disagreement fixtures exit 4 and 6 as required |
| P2 | implemented; both R28-01 malformed certificates are now REJECTED; the corrupted deficiency candidate is rejected and the valid one accepted |
| P3 | implemented; rate file refreshed and bound (`665e9da1…`) |
| P4 | implemented; the estimate covers the cal2 verifier peak |
| P5 | implemented; wall and artifact stops tested; preflight passes |
| regression | unchanged (schema fields listed above) |
| **registered outcome** | **1. Repaired** |

**Achievement level:** none moves (READ, HAND, COMPUTED engineering only). "No five-row determinant equation is known to be nonzero on padding."
