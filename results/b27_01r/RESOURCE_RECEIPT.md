# R27-01 resource receipt

- **Session.** Claude Code in default permission mode.
- **Clock.**
  - First clock read: 2026-09-23T04:18:15Z, at the start of run 1. Intake and preflight began a
    few minutes earlier; I did not read the clock then.
  - Mathematical work ended at about 04:22Z.
  - All of this is well inside the 60-minute ceiling.
- **Tools.**
  - Interpreter: installed CPython 3.12,
    `C:\Users\swami\AppData\Local\Programs\Python\Python312\python.exe`, SHA-256
    `4d6f5f81a4bca11191c4c7c6b43632694d0a4ce74e068619d8fdc161d469859a`.
  - SymPy 1.14.0 was already installed.
  - Nothing was installed.
- **Allowance.** 10 runs, each at most 60 s and 512 MB, run sequentially. **I used 5.**
  - Runs 1–3 ran under the producer's own Job Object cap of 512,000,000 bytes.
  - Runs 4–5 ran under `analysis/b27_01r_cap.py`: a Job Object with the same byte limit, plus a
    60 s watchdog.

| run | start UTC | command (cwd) | input hash(es) | output hash(es) | wall s | peak bytes |
|---|---|---|---|---|---:|---:|
| 1 | 04:18:15 | `python -B analysis/b27_01_verify.py` (scratch copy of tip `01f78eb2`) | script `d3aa0f47…48f2`; B17 cert `03585015…8e9c` | `671e7868…9bd2`, `67392878…6c42` (= manifest) | 3.024 | 38,621,184 |
| 2 | 04:18:18 | `python -B analysis/b27_01_boundary.py` (same) | script `2d999431…4845`; `NODAL_INPUT.json` `8ffb9a30…c920` | `9afaa64a…73b1` (= manifest) | 0.043 | 34,103,296 |
| 3 | 04:18:19 | `python -B analysis/b27_01_tangent.py` (same) | script `fc5ae58f…80de` | `6e39942c…a1b8` (= manifest) | 7.302 | 44,048,384 |
| 4 | 04:20:39 | `python -B analysis/b27_01r_ranks.py` (worktree) | see `RUN_04_RECEIPT.json` | `RANKS.json` `c8b75729…12ab` | 5.461 | 110,243,840 |
| 5 | 04:21:04 | `python -B analysis/b27_01r_identities.py` (worktree) | see `RUN_05_RECEIPT.json` | `IDENTITIES.json` `8099d3ce…87fb` | 0.123 | 71,921,664 |

- **Runs 1–3.** These ran on a scratch copy built from `git show 01f78eb2:<path>`. Their
  producer-format receipts were rewritten in that scratch copy and are not shipped. The figures
  above come from their console output. Runs 1–3 also rewrite the producer's own receipts; those
  rewritten receipts are not compared, because they contain wall times.
- **Runs 4–5.** These read the producer files only through `git show 01f78eb2:<path>`.
- **Method.** Nothing was random or sampled, and there was no equation search. The ranks were
  computed by full elimination modulo 1000003 and 2147483647.
