# B14-11 replay

Use the named branch from the bundle in a repository containing prerequisite
commit `9898e56941a7665f231873481dae956f08509995`. The bundle advertises
`refs/heads/b14-11-astra`; `HEAD` alone is not the import contract.

```powershell
git bundle verify C:/path/to/b14_11_astra.bundle
git fetch C:/path/to/b14_11_astra.bundle b14-11-astra:replay-b14-11
git worktree add C:/path/to/replay-b14-11 replay-b14-11
Set-Location C:/path/to/replay-b14-11
$b14Python = 'C:/Users/swami/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe'
```

Python 3.12 with numpy suffices. No flint, SciPy, compiler, network or install
is required. `b14_11_run.py` sets thread counts to one, fixes the hash seed,
enforces a 1.5-GiB process memory limit and the chosen timeout, and saves logs
and the actual PID under `results/logs/b14_11_*`. It refuses to continue if
the memory limit cannot be established. On Unix it uses RLIMIT_AS instead.

Quick validation, about 12 seconds on this host:

```powershell
& $b14Python analysis/b14_11_run.py --tag b14_11_replay_controls --seconds 120 controls
if ($LASTEXITCODE -ne 0) { throw 'controls failed' }
& $b14Python analysis/b14_11_run.py --tag b14_11_replay_sizecontrols --seconds 120 sizecontrols
if ($LASTEXITCODE -ne 0) { throw 'size controls failed' }
& $b14Python analysis/b14_11_run.py --tag b14_11_replay_verify --seconds 120 verify
if ($LASTEXITCODE -ne 0) { throw 'artifact validation failed' }
```

Full enumeration replay, about three minutes of supervised worker time here:

```powershell
foreach ($b14Delta in 5..8) {
    foreach ($b14Ell in 5..$b14Delta) {
        & $b14Python analysis/b14_11_run.py --tag "b14_11_replay_d${b14Delta}_l${b14Ell}" --seconds 300 census --delta $b14Delta --ell $b14Ell
        if ($LASTEXITCODE -ne 0) { throw 'census failed or timed out' }
    }
}
foreach ($b14Delta in 5..8) {
    & $b14Python analysis/b14_11_run.py --tag "b14_11_replay_hpad_${b14Delta}" --seconds 300 hpad --delta $b14Delta
    if ($LASTEXITCODE -ne 0) { throw 'pullback count failed' }
}
& $b14Python analysis/b14_11_run.py --tag b14_11_replay_inventory --seconds 120 inventory
if ($LASTEXITCODE -ne 0) { throw 'historical join failed' }
foreach ($b14Index in 0..9) {
    & $b14Python analysis/b14_11_run.py --tag "b14_11_replay_size_${b14Index}" --seconds 120 size --index $b14Index
    if ($LASTEXITCODE -ne 0) { throw 'size failed' }
}
& $b14Python analysis/b14_11_finish.py assemble
& $b14Python analysis/b14_11_run.py --tag b14_11_replay_final --seconds 120 verify
if ($LASTEXITCODE -ne 0) { throw 'final validation failed' }
```

Mathematical fields reproduce exactly; PID, time, memory and absolute command
paths are host-specific metadata. Census files include zero coefficients.
`hpad_d5.json` through `hpad_d8.json` use compact JSON to stay below 5 MB.
The ten Burnside artifacts include all class representatives, character signs
and fixed-monomial traces. `shortlist.json` includes the cost formulas and
their unmeasured stages. `cost_queue.json` holds all 1,715 candidates.

`analysis/b14_11_finish.py audit` repeats the documented lexical prose scan;
`inputs` checks and hashes the frozen Git blobs. Protected errata remain in
`docs/b14_11_protected_errata.md`. `b14_11_prose.py` is an idempotent record of
explicit prose fixes; mathematical replay does not need to edit historical prose.
The original seven inherited predicates are preserved. New relational and
explicit-key predicates use `b14_11_finish.session_exclusions`; the generic
legacy range-only join skips them until integration implements those types.

```powershell
& $b14Python tools/delivery/check_delivery.py --branch b14-11-astra --base 9898e56941a7665f231873481dae956f08509995
git bundle create C:/path/to/b14_11_astra.bundle 9898e56941a7665f231873481dae956f08509995..b14-11-astra b14-11-astra
git bundle list-heads C:/path/to/b14_11_astra.bundle
& $b14Python tools/delivery/check_delivery.py --branch b14-11-astra --base 9898e56941a7665f231873481dae956f08509995 --bundle C:/path/to/b14_11_astra.bundle
```

If working on an alternate replay branch, substitute its name consistently.
The delivered `part00` is the one-part binary copy of the whole bundle. Verify
all bare-filename entries in `checksums.md5` and `checksums.sha256` before use.
The final delivery manifest is external to the bundle to avoid a self-referential
head or checksum. Both pre-bundle and post-bundle gate logs are delivered.
