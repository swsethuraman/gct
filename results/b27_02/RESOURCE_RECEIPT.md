# B27-02 resource receipt

Administrative observations are **READ**; exact replay records are **COMPUTED**.
The hand argument is separate in PROOF.md. No subagents, sessions, task messages,
installs, random searches, sampled nullspaces, or external sources were used.

## Clock and checkpoint

- First explicit UTC observation: 2026-09-23T03:48:28Z, after reading the briefs
  and initial preflight. The exact earlier session-start time was not measured.
- For conservative budget accounting, assign five additional minutes before
  that observation: origin 03:43:28Z. This is an allowance, not an observed time.
- Candidate and early checkpoint recorded around 03:53Z. The 45-minute deadline
  and 90-minute ceiling were not approached.
- Mathematical verification completed at 03:54:44Z. Subsequent work is proof
  transcription, administrative validation, manifest generation and delivery.
- Final explicit clock before manifest/delivery: 03:58:15Z. Both the checkpoint
  and substantive work finished well within the conservative accounting budget.
- Availability checks: `python -c "import sympy"` could not run because python
  was absent on PATH. The installed bundled Python was then tested and reported
  ModuleNotFoundError for sympy. Installed standard-library integers/Fraction
  provide the exact arithmetic used here. These import probes did no mathematics.

## Two runs, sequential (allowance: at most ten)

The executable is
`C:/Users/swami/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`.
Working directory is this slot's worktree. Exact argv arrays and raw byte
bindings are preserved in each run's JSON resource receipt.

| run | command following the Python executable | start UTC | wall seconds | peak job bytes | exit |
|---|---|---|---:|---:|---:|
| 1 | analysis/b27_02_run.py run01 grouped | 03:54:37Z | 0.10314669995568693 | 11993088 | 0 |
| 2 | analysis/b27_02_run.py run02 full | 03:54:43Z | 0.8712580000283197 | 11784192 | 0 |

Both runs enforce aggregate Job Object and process memory limits of 536870912
bytes (512 MiB), with a 55-second watchdog, below the brief's 60-second ceiling.
There is one worker. Python is 3.12.14. No mathematical code uses floating point;
floating-point receipt fields measure elapsed time only. The runner's resource
implementation adapts the committed b15_bound.py already read and byte-bound.

Input hashes below name exact raw file bytes; both runs used these same inputs:

| input | SHA-256 |
|---|---|
| analysis/b27_02_run.py | 83343936a8455ece6ec7377547587fff95226dd4fd741d8258408c54c19a22fd |
| analysis/b27_02_verify.py | fed48cb06feddec89cde679351456407d16d6d64a438177c6d9c40750cca67a3 |
| results/b27_02/candidate.json | b75f8e9c5330d8a5ba2b749d00f42bf8d505d708b0339deae2cb05db9b95555e |
| results/b27_02/INPUT_BINDINGS.json | fd2a4437947c25f085c254067fb3f8321525b5eb6e680bb8d25ced2bc361972a |

| output | raw SHA-256 |
|---|---|
| run01_output.json | a4ae4176f63460cc84e938847e9e59b8c62e86f03812486047b64af225f31d5b |
| run02_output.json | 92d8fbe91d0abe8847e13492ff4642f8bf733863c77d055c135b84517c2b6b1b |

The run output values are COMPUTED finite certificates, not a proof inferred
from numerical tests. They replay the independent hand argument in PROOF.md.
The two runs use the same verification script with two enumeration modes, so
they are not an independent review. Their exact code and all payloads are
bound by MANIFEST.json. No third mathematical run was needed.

Administrative operations outside the mathematical allowance: reading files
and committed blobs, environment/import probes, Git inspection, hashing, file
creation, manifest checks, staging by explicit path, one commit, push and
ls-remote. No existing untracked file was present or modified; no ledger,
seal, paper, attribute file or ignore file was edited.
