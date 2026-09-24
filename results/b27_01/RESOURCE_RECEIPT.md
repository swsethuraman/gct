# B27-01 resource receipt

This receipt distinguishes mathematical computation from administrative file/Git reads, byte hashing, source snapshots, and delivery checks. The scripts and raw results are retained even for the negative run.

## Clock and scope

- First actual clock read: **2026-09-23 03:47:57 UTC**. Intake had already begun. The preflight records **03:47:00 UTC** as the conservative rounded accounting start, not as an independently observed timestamp.
- Early checkpoint: **04:00:59 UTC**, CHECKPOINT.md. The 45-minute checkpoint was not reached.
- Mathematical stop after proof and scope review: **04:06:27 UTC**. All three rungs were answered or their exact obstruction identified. Conservative elapsed accounting interval: **19m27s**, with no interruptions or deductions claimed. Subsequent work is administrative sealing and the authorized commit/push.
- Limits: 10 mathematical runs maximum, sequential, each at most 60 seconds and 512 MB. **Used: 3 runs**, about **10.875957 seconds total**; largest measured Job Object memory **21,884,928 bytes**.
- Each research process assigned itself to a Windows Job Object before the calculation, with process and aggregate memory limits of **512,000,000 bytes** (stricter than 512 MiB). A watchdog enforced a 60-second wall deadline. One computation process; no child numerical processes, no numerical threads, no parallel mathematical runs.

## Installed tools and exact commands

The initial `python -c "import sympy; print(sympy.__version__)"` probe could not run because python was absent from PATH. The already installed bundled interpreter was located by the workspace-dependencies tool:

`C:\Users\swami\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`

Its `-c "import sympy; print(sympy.__version__)"` metadata probe returned ModuleNotFoundError. No install followed. Installed Python's standard-library integers, modular inverses, and fraction-free exact elimination were sufficient. These two import/availability probes performed no mathematics on the research objects and are not counted as research runs. The interpreter raw SHA-256 is recorded in RUN_01_RECEIPT.json:

`b7a12c3af0b4db44191eec14ea095eba731b7328917f570806183093d19ddca2`.

Each command below was run in `C:\Users\swami\Projects\gct-gpt\work\batch27\b27-01`, with that full interpreter path and `-B`:

| Run | Command suffix | Start UTC | Wall seconds | Peak job bytes | Mathematical outcome |
|---|---|---|---:|---:|---|
| 1 | `-B analysis/b27_01_verify.py` | 03:52:47 | 3.0810560999670997 | 16,683,008 | COMPUTED PASS: fixed committed smooth witness; integer and modular 210-square determinant, frame determinant. |
| 2 | `-B analysis/b27_01_boundary.py` | 03:55:57 | 0.04282530001364648 | 13,225,984 | COMPUTED NEGATIVE: first fixed boundary input gave rank 203 modulo 65521, not 209; no unique-node or rational-rank conclusion. |
| 3 | `-B analysis/b27_01_tangent.py` | 03:58:28 | 7.752075599972159 | 21,884,928 | COMPUTED PASS: separately specified tangent section; unique ordinary node, integer/modular 209-square certificate, rank-35 parameter differential. |

The corresponding RUN_01_RECEIPT.json, RUN_02_RECEIPT.json, and RUN_03_RECEIPT.json store complete argv, input hashes (including imported research scripts), output hashes, wall time, caps, and measured memory. Their own raw bytes are bound by MANIFEST.json. Hashes name complete raw file bytes, not text normalized by the shell.

## Run bindings

**Run 1**:

- Script SHA-256: `d3aa0f47ad6973ce830a81d67ec771f34b952a47253ea807fe8b60c29d7c48f2`.
- Mathematical input: exact `01c49022:results/b17_01/certificate.json` blob; SHA-256 `03585015180e0724bb7d8f1a6264a64e9a6fc877d191dc13cab0187c49f58e9c`.
- `T_STAR.json`: `671e786894d2a37f13a494968ad6de40e92c2c2b4d1d030204aad5f72ee49bd2`.
- `SMOOTHNESS_CERTIFICATE.json`: `67392878c0051bc77538d2266f8368164f3175f226a92ddf0c541c27cf776c42`.

**Run 2**:

- Script SHA-256: `2d999431ede68da95c9dca282f9cbb18617f2f7e550c1f26f5fd365a65b74845`; imported b27_01_verify.py has the run-1 hash above.
- HAND-specified `NODAL_INPUT.json`: `8ffb9a3041db4fcacc8c15bd45c9eda64f10df4fa20dcff8aba9c7b165ebc920`.
- `BOUNDARY_CERTIFICATE.json`: `9afaa64aafb113b8afa50c9d7a1026b703d4032b3302baac39ac2cf9321273b1`.

**Run 3**:

- Script SHA-256: `fc5ae58fe0e1681973a023deca7503d547337432e813a5b2d3fba05f55ac80de`; it imports the run-1 exact arithmetic and run-2 deterministic row-elimination routines at their unchanged hashes.
- The fixed q and four tangent vectors are specified by exact formulas in the script, so its hash also binds the HAND-constructed mathematical input. The resulting five matrices are saved in the output for reviewers.
- `TANGENT_CERTIFICATE.json`: `6e39942cceaba93e63cb4ba52374016c3381edde15547fcde9577444587da1b8`.

## Interpretation, audit, and exclusions

All numerical results are **COMPUTED**, not PROVED. Nonzero integer determinants and checked modular residues are finite certificates; the smoothness, one-node, and dimension implications are separate HAND arguments. Run 2 is a retained negative. No prime, random seed, or point was iterated inside any run. The historical random generator in the B17 source was read but never executed: run 1 consumes its already committed fixed certificate. Runs 2 and 3 are complete exact checks of specified constructions, not random searches, sampled nullspaces, or equation searches.

Administrative `b27_01_admin.py audit` re-read and verified **18 committed source blobs**, all corresponding snapshots, and all three runs' script/input/output bindings. It also checked each reported run against its caps. Those are byte and receipt checks, not additional mathematical replays. `manifest` checks filtered versus `--no-filters` Git object hashes for every payload and the manifest itself. `verify-commit` is provided to check all committed payload bytes and the exact setup parent after the single delivery commit.

No subagents, other sessions, messages to other tasks, installs, equation search, paper edits, ledger/seal edits, publication, or automatic continuation. No other branch was changed. The only Git write operations authorized for delivery are explicit-path staging, one commit on b27-01, and its push to origin; ls-remote verifies the pushed tip. No merge, rebase, amend, reset, clean, checkout, force operation, attribute edit, or ignore edit is used.
