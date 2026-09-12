# Replay B14-05

The package carries one incremental named-branch Git bundle, plus one identical
part `part00` (total part count one). Both fit below 5 MB. Verify MD5SUMS.txt and
SHA256SUMS.txt in the delivery directory; every line names a bare filename.
The frozen base prerequisite must already be present in the receiving repository.
Do not switch the shared integration checkout. Use a separate clone/worktree.

```powershell
git bundle verify C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-05/b14_05_astra.bundle
git bundle list-heads C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-05/b14_05_astra.bundle
git fetch C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-05/b14_05_astra.bundle b14-05-astra:b14-05-replay
git worktree add C:/path/to/new/replay-worktree b14-05-replay
```

In that isolated replay worktree, verify the base:

```powershell
git log -1 --format=%H batch14-base
git log -1 --format=%T batch14-base
```

Expected commit: `9898e56941a7665f231873481dae956f08509995`.
Expected tree: `cb688cd3fe454d638f3202e759e2eaa0c629739f`.
If the base commit is present but the annotated tag is absent, obtain the frozen
tag from the trusted base repository before running the input auditor. The
external delivery manifest captures the bundle head, head tree and prerequisites.

Run sequentially on Windows with Python 3.12 and numpy (only for NPZ reading).
The delivered wrapper writes fresh logs and results in this replay worktree.
No flint, scipy or sympy is needed; there is no installation step.

```powershell
$taskPython = 'C:/Users/swami/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe'
& $taskPython analysis/b14_05_bound.py --name replay_inputs --seconds 300 --mib 512 -- analysis/b14_05_inputs.py
if ($LASTEXITCODE -ne 0) { throw 'Input audit failed' }
& $taskPython analysis/b14_05_bound.py --name replay_controls --seconds 300 --mib 512 -- analysis/b14_05_controls.py
if ($LASTEXITCODE -ne 0) { throw 'Small exact controls failed' }
& $taskPython analysis/b14_05_bound.py --name replay_n3 --seconds 600 --mib 512 -- analysis/b14_05_n3.py
if ($LASTEXITCODE -ne 0) { throw 'n=3 coordinate replay failed' }
```

Expected outputs:

- Input audit: PASS for conventions only, 116/212 points, six corruptions rejected.
- Small controls: qualified claims PASS, **raw adjunction REFUTED**, 24 corruptions
  rejected; witness difference -497664; corrected source/image ranks both two.
- n=3: ranks six/six, conversion determinant 5/12, line scalar -29859840, six
  corruptions rejected. The upper s73 integer vector equals u times the s62 one.

The three research JSON outputs are deterministic and can be compared with the
delivered versions. Resource JSON/logs contain actual timestamps/PIDs and will
differ on replay. The small scripts use exact arithmetic. The n=3 script adopts
the frozen polynomial-to-chi expansions and verifies the supplied integer
coordinates against an independent target basis; it does not repeat those large
expansions. The proof note gives the exact boundary of each assertion.

On a non-Windows host, apply an equivalent per-process 512-MiB and 300/600-second
bound, set the usual BLAS/OpenMP thread variables to one, then run the three
underlying scripts. The Windows wrapper deliberately refuses other platforms.

The new exact certificates are controls.json, n3_transport.json and
input_audit.json. Stored matrices explicitly declare values_are. No file is a
complete-interpolation certificate at degree 13 or 14, and no new LMR rank was
computed. Input blob identities are in input_manifest.json; working-byte SHA256
values additionally record the producer's line endings. The package manifest
also hashes the launch prompt and packet outside the worktree.

Producer delivery validation (after committing, before export, then with bundle):

```powershell
& $taskPython tools/delivery/check_delivery.py --branch b14-05-astra --base 9898e56941a7665f231873481dae956f08509995
git bundle create C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-05/b14_05_astra.bundle 9898e56941a7665f231873481dae956f08509995..b14-05-astra b14-05-astra
& $taskPython tools/delivery/check_delivery.py --branch b14-05-astra --base 9898e56941a7665f231873481dae956f08509995 --bundle C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-05/b14_05_astra.bundle
```

Do not create a HEAD-only bundle. The explicit refs/heads/b14-05-astra is required.
The packaging script is a producer convenience and refuses a dirty worktree or
an incorrect branch/base. It requires its own final source commit before export.
