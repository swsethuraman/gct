# B28-01a — Cell A: build and calibrate

**Registered outcome 1: Ready.** The driver and the verifier are frozen. All controls pass. Both preregistered calibration cells reproduce the record exactly, and the independent verifier accepts both. Repriced on this laptop, Cell A `(12,8,6,4,2)` at k=8 (a=109, n_χ=N_S=813,314) fits the approved 24 h / 24 GB caps in every required scenario. Cell A's matrix was **not** built. B28-01b needs an R28-01 ACCEPT and the user's go.

No achievement level moves. **READ:** "No five-row determinant equation is known to be nonzero on padding." Programme decision: "no construction ready."

## Preflight

**READ.** Raw SHA-256 of the briefs, matching the board:
- `B28_COMMON.md`: `06799a9e…c87b9`
- `B28-01a.md`: `3975e63f…307b5`
- `BATCH28_BOARD.md`: `c635ac1a…96af` (this matches PART 27's receipt)

**READ.** Git state:
- Branch `b28-01`. HEAD = `c0122f57e745097ddb84d3f6ee6a26e1de8d8314`, which is PART 27's setup commit (parent `96a8074d`). `ls-remote` agreed.
- The worktree was clean. `docs/b28_01a_report.md`, `results/b28_01/` and `analysis/b28_01_*` were absent.

**READ.** Governing inputs. `96a8074d:results/b27_06/MANIFEST.json` hashes to `b713ca8b…cfce`, the folder named in the brief. `PREREGISTRATION.md` and `REPORT.md` were read in full.

**READ.** Engine sources. All 19 are byte-identical at `7c36a52d` (B27-06's "C") and `96a8074d`. They were copied into WSL with `git show`, and every host copy's SHA-256 equals the committed blob's (`results/b28_01/engine_hashes.txt`).

## 1a — Environment

**READ** (host facts). Full record: `results/b28_01/ENVIRONMENT.json`.

- **System.** Ubuntu 24.04.5 LTS on WSL2, kernel 6.18.33.2. Intel Core Ultra 7 255HX, 20 cores.
- **Memory.** `free -g`: 27 GiB total, 8 GiB swap.
- **Toolchain.** gcc 13.3.0, Python 3.12.3.
- **Installed in this slot:**
  - via apt: build-essential 12.10ubuntu1, python3-venv, python3-pip;
  - via pip, in the venv `~/b28venv`: NumPy 2.5.3, SciPy 1.18.1, python-flint 0.9.0.
  - Nothing was installed on Windows.
- **BLAS.** scipy-openblas 0.3.34 (NumPy) / 0.3.31.dev (SciPy). One thread, forced.
- **sudo.** It needs a password, so apt ran through WSL's documented root entry (`wsl -d Ubuntu-24.04 -u root`). Reviewers should note this.
- **Schur helper.** `analysis/wk11_s71_schur.c` (`17cfdf42…`), compiled `gcc -O3 -march=native -shared -fPIC` (native = sierraforest) → `schur.so` `d6024a63…`.

## 1b — Determinant-only driver

**HAND.** `analysis/b28_01_driver.py` (frozen v2 `de202bb0…`) adapts `wk12_s79_cell6.py`.
- **Imports.** It imports the committed engine unchanged:
  - `wk9_s45_build.build_cell`;
  - `wk11_s71_hybrid` (cover, `_split_rows`, `trisolve`, `spmm_mod`, `schur_project`, `nullspace_mod_p`, `check_kernel_mat`, `rank_tall`, `matmul_mod`);
  - `wk12_s79_cell6.det_pencils/det_coeffs/ev_rows_from_coeffs`.
- **Determinant family only.** The pad, per4 and reducible families and their allocations are gone.
- **One projection attempt per prime.** Base seed 20260908; pseed = seed + p mod 1000; m = |U|+64; nproj 8.
- **Recorded Schur outputs.** G's SHA-256 and its recipe are recorded. Kernel vectors are taken by `nullspace(G)`, and deficiency candidates would be taken by `nullspace(VK)`, never the transpose.
- **Memory limits.**
  - X blocks are sized by `S71_MEM_X`=250 MB, with the 32-column minimum.
  - Evaluation runs in batches of eight points.
  - matmul_mod's inner-dimension assertion (< 2^21) is kept and asserted again. Cell A's 813,314 < 2,097,152.
- **Pencils.** a+8 integer pencils (seed 11, bound 40) are serialized and shared by both primes.
- **Primes.** 2,147,483,647 then 2,147,483,629, sequentially.
- **Build-and-cover gate.**
  - The driver saves rows, z, dtypes, CSR bytes, the cover (S/U/rows `.npy`) and phase peaks.
  - It then reprices with the phase model and host rates: remaining = n_primes·(H+V+R+D) + verifier_factor·(B+S+H+V+R+D).
  - It exits 3 before any Schur allocation if that exceeds the unused budget, or if the envelope exceeds 75% of the cap.
- **Exit states.** A failed source gate exits 4 with no retry. Full rank saves K (uint32), VK, the pivot rows of a nonzero a-minor and the minor's value.
- **Output files** hold no times. Times and per-phase VmHWM go only to `*_receipt.json`.

## 1c — Independent verifier

**HAND.** `analysis/b28_01_verify.py` (frozen v2 `7978a73a…`) with its own C solve `analysis/b28_01_vfy.c` (`5166db3b…`, `-O2`, `.so` `a5e8399d…`). It imports nothing from the producer or the engine. The declared shared low-level libraries are numpy, scipy.sparse and python-flint (`nmod_mat` rank/det/rref).

From λ, k, a and p it regenerates:
- the monomials, by memoised feasibility and base-L positional keys (the engine uses a DP prune and combinadic codes);
- the χ-isotypic columns: the Young subgroup, χ = the product of block signs over odd parts, and the twisted signs;
- E, as derivation rows restricted to H-canonical, non-obstructed targets, with a cancellation assertion;
- the five-order cover;
- the projected residual, built as the sparse product P·F_o followed by PF_U − PF_S·X. This is a different algorithm from the producer's per-row C accumulation, and it carries an asserted int64 bound;
- Leibniz determinant coefficients, the evaluation rows, and V·K through 16-bit-limb int64 products with chunks of 2^15.

It checks, trusting no stored rank:
- **G1:** the cover pivots are nonzero and T is upper triangular;
- **G2:** rank G = |U|−a;
- **K1:** EK=0 on every row, and rank K[U]=a;
- **M1:** the claimed minor is nonzero;
- plus hash cross-checks (E, cover, G, VK) and the pencils against their generator.

## 1d — Controls

The replay cell is **READ** `96a8074d:results/s71_sweep.jsonl` line 5: `(22,6,5,2,1)` at k=9, a=24, a session-71 hybrid row with mult_det=24 at both primes.

**COMPUTED, both primes.** Every recorded value is reproduced:
- n_χ 21,093; rows 51,337; nnz 185,066;
- cover 21,023 "reversed", with stats {natural 20,412, reversed 21,023, fill_asc 17,779, fill_desc 17,434, random 14,571};
- |U| 70, m 134, projected nullity 24, mult_det 24.

The verifier ACCEPTs at both primes.

**Corrupted controls (COMPUTED), both REJECTed:**
- **Kernel** (K[0,0]+1): fails K1 `EK=0`, and also the K hash, VK and minor checks.
- **Point** (one pencil entry +1): fails the generator, VK and minor checks.

Before freezing, the pair also agreed bit-for-bit on four development fixtures, including repeated odd parts (non-trivial χ): `(12,2,2,2,2)_5`, `(9,9,3,3)_6`, `(9,5,5,3,1,1)_6` and the control cell.

## 1e — Calibration (p = 2,147,483,647, determinant only)

| cell | recorded (READ) | reproduced (COMPUTED) |
|---|---|---|
| `(24,6,5,3,2)_10` (s71_sweep:145) | N_S=n_χ 188,872; rows 510,662; nnz 1,951,800; cover 188,498 reversed; \|U\| 374; m 438; a 47; mult_det 47 | identical, including the cover stats; projected nullity 47; mult_det 47; verifier ACCEPT |
| `(13,9,9,3,1,1)_9` (s79_cells:121) | N_S 3,503,556; \|Stab\| 4; n_χ 732,815; rows 3,899,488; nnz 18,374,635; cover 731,538 reversed; \|U\| 1,277; m 1,341; ublock 85×16; a 70; mult_det 70 | identical; projected nullity 70; mult_det 70; verifier ACCEPT |

**COMPUTED — phase seconds and peak VmHWM in GB (driver | verifier):**

| phase | cal1 | cal2 |
|---|---|---|
| build | 1.34 / 0.14 \| 0.53 / 0.15 | 31.7 / 0.97 \| 12.8 / 1.73 |
| cover | 0.22 / 0.16 \| 0.22 / 0.16 | 2.25 / 0.92 \| 2.08 / 0.98 |
| Schur (split, trisolve, project, nullspace) | 2.98 / 1.18 \| 7.60 / 0.92 | 78.4 / 2.03 \| 340.8 / 5.65 |
| lift + check | 1.01 / 0.65 \| 0.56 / 0.50 | 9.36 / 3.99 \| 6.19 / 3.16 |
| evaluation | 1.87 / 0.58 \| 2.04 / 0.31 | 33.1 / 3.04 \| 25.3 / 1.38 |
| process total | 7.5 s \| 11.0 s | 155.4 s \| 387.6 s |

**Calibration cap.** All control and calibration runs, including the superseded v1 set, used about 10.0 minutes of the 2-hour cap. The largest peak was 5.65 GB, under the 8 GiB scope cap.

**Two caveats:**
- The scope cap `MemoryMax=8G` is 8 GiB, slightly above 8×10⁹ bytes. Every measured peak is below 8×10⁹.
- GNU `time -v` reports lower maximum RSS (2.97 / 1.39 GB for cal2) than the per-phase VmHWM. The pricing uses the larger figure.

**Deviation.** The first frozen set, v1, measured durations with `time.time()`, and one verifier phase came out negative, which suggests a WSL wall-clock step. Durations now use `time.perf_counter()`. That is the only change from v1 to v2; the v1 hashes are in `RESOURCE_RECEIPT.json`. Controls and calibration were re-run under v2. All 25 non-receipt control and cal1 outputs are **byte-identical** between v1 and v2, which is a determinism check. The v1 outputs are kept in `results/b28_01/superseded_v1/`.

## 1f — Cell A repriced for this host

**COMPUTED** (`analysis/b28_01_reprice.py` → `results/b28_01/host_rates.json`, `cellA_price.json`, `gate_rates.json` `6bbc5aed…`).

**Rate fitting.** Each coefficient of the preregistered phase model is fitted per cell, and the maximum over the two cells is kept.
- cH covers Schur plus lift/check, minus nullspace.
- cD = max(5e-10, nullspace/U³).
- Evaluation is charged to **both** cV and cR, a deliberate double count.
- The verifier has its own coefficients.

**Host producer rates versus baseline:**
- cB 4.8e-6 (baseline 2.1e-6)
- cS 1.2e-7 (5e-7)
- cH 5.4e-9 (8e-8)
- cV 6.4e-8 (2.7e-8)
- cR 8.3e-9 (1e-9)
- cD 9.9e-10 (5e-10)

**Totals.** Producer = B+S+2(H+V+R+D). Verifier = one independent rebuild and replay.

| z | f | U | producer | verifier | total | envelope |
|---|---|---|---|---|---|---|
| 10n | 0.10% | 923 | 0.11 h | 0.06 h | **0.17 h** | 4.4 GB |
| 10n | 0.48% | 4,013 | 0.22 h | 0.18 h | **0.39 h** | 5.6 GB |
| 10n | 1.30% | 10,683 | 1.02 h | 0.56 h | **1.58 h** | 13.4 GB |
| 32n | 0.10% | 923 | 0.16 h | 0.13 h | **0.29 h** | 6.2 GB |
| 32n | 0.48% | 4,013 | 0.43 h | 0.47 h | **0.90 h** | 7.4 GB |
| 32n | 1.30% | 10,683 | 1.59 h | 1.34 h | **2.94 h** | 15.2 GB |

**HAND — verdict: fits the 24 h / 24 GB caps.** Every envelope is also below the 75% gate (18 GB).
- **Envelope check.** At cal2 the envelope (4.83 GB) bounded the measured producer peak (3.99 GB).
- **Verifier memory.** Scaling the verifier's cal2 Schur peak by z, and adding about 44U² bytes for its dense G and flint conversion, gives roughly 13 GB in the worst row.
- **Weakest extrapolation.** The weakest term is D, the flint nullspace or rank at U≈10⁴, fitted at U≤1,277. A fourfold error in the whole worst row still gives under 12 h.
- **What calibration measured.** Measured z/n was 10.3 for the five-row distinct-part cell and 25.1 for the six-row cell. Cell A's z and U are unmeasured and are decided at the gate.

**Frozen command for B28-01b (not run).** `bash ~/b28_01/frozen/b28_01_cellA.sh`, the frozen copy of `analysis/b28_01_cellA.sh`. In order, it:
1. preflights the frozen code, engine and rates hashes, and checks that the output folder is absent;
2. runs `b28_01_run.sh cellA_driver 24000000000 86400 … b28_01_driver.py --lam 12 8 6 4 2 --delta 8 --a 109 --nchi 813314 --primes 2147483647 2147483629 --wall-budget 86400 --mem-cap 24000000000 --rates gate_rates.json`;
3. runs the verifier at 2,147,483,647 within the remaining wall time.

## Delivery notes

- **HAND — large files not committed.** Five files over 5 MB stay on the host at `~/b28_01/out`, bound by SHA-256 in `HOST_RETAINED.json`: the cal1 and cal2 kernels (35.5 MB, 205 MB), the cal2 cover arrays, and the v1 cal1 kernel. The verifier regenerates each of them.
- **Resource receipt.** `RESOURCE_RECEIPT.json` lists every wrapped run with its command, rc, wall time, max RSS and stdout/stderr hashes, plus output hashes. Development fixture runs, each under 1 s, are in `dev_fixtures/`.
- **What is and is not claimed.** The calibration verdicts restate recorded full-rank results; they are **COMPUTED** controls, not new mathematics. No subagent, no other session, no publication.

**Achievement level:** engineering and calibration only (COMPUTED + HAND). No source condition, coefficient equation, padding separation, positive multiplicity gap or geometric noncontainment is claimed.
