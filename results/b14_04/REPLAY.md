# Replay B14-04

The delivery is a named-branch Git bundle, requiring frozen base commit
9898e56941a7665f231873481dae956f08509995. It is not a standalone repository.
Use an isolated receiving checkout; do not switch or merge a shared integration checkout.

On a repository that already contains the frozen base, verify and fetch:

```powershell
git bundle verify 'C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-04/b14_04_astra.bundle'
git bundle list-heads 'C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-04/b14_04_astra.bundle'
git fetch 'C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-04/b14_04_astra.bundle' 'b14-04-astra:refs/heads/review-b14-04-astra'
```

The bundle must list refs/heads/b14-04-astra. Select the receiving branch in
an isolated checkout before replay. The original prepared working directory is:
C:/Users/swami/Projects/gct-gpt/work/batch14/B14-04.
The final head and tree are in delivery_manifest.json, outside the bundle.

The only runtime dependency is Python's standard library. On this Windows host:

```powershell
Set-Location 'C:/Users/swami/Projects/gct-gpt/work/batch14/B14-04'
$pythonB1404 = 'C:/Users/swami/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe'
& $pythonB1404 analysis/b14_04/bounded.py --name replay_verify --seconds 600 analysis/b14_04/verify.py
```

This independently regenerates the exact stable expansions, cubic expansions,
all character values, and checks both primes and deliberately invalid inputs.
Expected: PASS; hpad 73/159; stable 274/392/533; 19 rejected mutations.
The final PASS status is written only after every required check passes.
Frozen input Git blobs are authoritative. CRLF/LF differences are allowed; the session appendix in PROVED.md is allowed only with its entire frozen prefix intact.
The report describes the proof and the exact normalization.

For a full producer replay, run these sequentially, checking each exit code:

```powershell
& $pythonB1404 analysis/b14_04/bounded.py --name replay_controls --seconds 120 analysis/b14_04/recount.py controls
if ($LASTEXITCODE -ne 0) { throw 'controls failed' }
& $pythonB1404 analysis/b14_04/bounded.py --name replay_hpad13 --seconds 180 analysis/b14_04/recount.py hpad13
if ($LASTEXITCODE -ne 0) { throw 'hpad13 failed' }
& $pythonB1404 analysis/b14_04/bounded.py --name replay_hpad14 --seconds 180 analysis/b14_04/recount.py hpad14
if ($LASTEXITCODE -ne 0) { throw 'hpad14 failed' }
& $pythonB1404 analysis/b14_04/bounded.py --name replay_stable --seconds 600 analysis/b14_04/recount.py stable
if ($LASTEXITCODE -ne 0) { throw 'stable failed' }
& $pythonB1404 analysis/b14_04/bounded.py --name replay_verify --seconds 600 analysis/b14_04/verify.py
if ($LASTEXITCODE -ne 0) { throw 'verification failed' }
```

The supervisor enforces a 1,024 MiB Windows process commit limit before work
and records PID, peak commitment and wall time. Numerical-library threads are
capped at one. It intentionally refuses non-Windows hosts; on another OS use
that host's wall and address-space limits to launch recount.py and verify.py.
Do not replace bounded launches with unrestricted shared-host runs.
Measured producer total was about 32 seconds and the first independent verifier
about 12 seconds on this host; final stronger-check timings are in logs.

Resource guard checks (expected nonzero process exits):

```powershell
& $pythonB1404 analysis/b14_04/bounded.py --name replay_memory_probe --seconds 10 --memory-mib 64 analysis/b14_04/resource_probe.py memory
& $pythonB1404 analysis/b14_04/bounded.py --name replay_wall_probe --seconds 0.4 --memory-mib 64 analysis/b14_04/resource_probe.py wall
```

The first log must show MemoryError; the second resources record must say
RESOURCE_STOPPED_WALL. These are deliberately invalid resource requests.

The five .json.gz files are ordinary gzip-compressed JSON, each below 5 MiB
both compressed and uncompressed. Compression metadata and both hashes for
compressed/uncompressed bytes are in artifacts/artifact_manifest.json.
Example decompression from the original worktree:

```powershell
& $pythonB1404 -c 'import gzip,pathlib; p=pathlib.Path("results/b14_04/stable33.json.gz"); p.with_suffix("").write_bytes(gzip.decompress(p.read_bytes()))'
```

Stable row: [cycle_partition, power_coefficient_numerator, denominator, character].
Compute sum(numerator/denominator * character), with exact fractions. There is
no extra z factor. Hpad rows are unscaled cubic Schur multiplicities. No evaluation
matrix or tensor normalization is encoded, and no ideal/rank conclusion follows.

Delivery checks (run from the isolated session checkout):

```powershell
& $pythonB1404 tools/delivery/check_delivery.py --branch b14-04-astra --base 9898e56941a7665f231873481dae956f08509995
& $pythonB1404 tools/delivery/check_delivery.py --branch b14-04-astra --base 9898e56941a7665f231873481dae956f08509995 --bundle 'C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-04/b14_04_astra.bundle'
```

The provided .md5 and .sha256 files name bare filenames. The delivery manifest
indexes all direct artifacts, checksums, base/head/tree, bundle named ref and
prerequisites. There are zero numbered parts for this unsplit bundle.
