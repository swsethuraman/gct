# B14-03 replay

Actual authoring model: gpt-6-astra, xhigh. Board numbering: batch14.
Frozen base: `9898e56941a7665f231873481dae956f08509995`.
Frozen tree: `cb688cd3fe454d638f3202e759e2eaa0c629739f`.
Named branch: `b14-03-astra`. The delivery has one bundle part, part00.

The delivery manifest records the final head/tree and prerequisite base. Verify
the bare-filename checksum sidecars before importing the bundle. In a separate
receiver repository which already has the frozen base, these commands import
the session without changing integration:

```powershell
git bundle verify C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-03/b14_03_astra.bundle
git fetch C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-03/b14_03_astra.bundle b14-03-astra:b14-03-astra
git switch b14-03-astra
```

If using the part, it is byte-identical to the whole bundle (one part). Copy
`b14_03_astra.bundle.part00` to `b14_03_astra.bundle` and verify the whole digest.
Do not import the branch into a repository where that branch is checked out.

From the resulting checkout root on Windows:

```powershell
$py = 'C:/Users/swami/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe'
& $py analysis/b14_03_replay.py
if ($LASTEXITCODE -ne 0) { throw 'B14-03 replay failed' }
```

This sequential driver checks exact process exit codes, writes PID/resource
files and logs, and applies 120 s to generation, 600 s to each verification,
768 MiB of hard Windows Job Object process memory, and one numerical-library
thread. It stops if the host has less than twice the memory cap available.
Every child is bounded; no existing process is addressed by name. CPython
3.12.14 and NumPy 2.3.5 were used. No dependency was installed. The checker
uses NumPy only for bounded modular elimination and stdlib for exact rational
arithmetic; flint/scipy are not required for this kind.

Expected results:

1. Deterministic producer selects bracket attempt 0 and writes the certificate.
2. Controls: **97/97**, with two accepted inputs, 95 rejected mutations, and
   71 separate required-key deletions; duplicate-key rejection and the full
   coefficient identity G=288 mu*(F1) also hold.
3. Standalone checker: PASS; source dimension 2, target dimension 1,
   restriction rank 1, i_red=1.
4. Repository dispatcher: PASS on integer, rational and gzip controls.
5. Dispatcher negative cases: one FAIL (altered integer entry), three
   UNPARSEABLE (missing points, duplicate key, nonexistent file), process
   exit **1**. This expected nonzero exit is checked by the replay driver.

`results/b14_03/replay_results.json` records the exit checks.
`results/b14_03/control_mutations.json` records every exact mutation.
`results/b14_03/control_results.json` records every verdict and reached checks.
Negative fixtures are intentionally invalid and are not proved certificates.
Run the named positive files, not every JSON artifact as if it were a certificate.

For direct review of the standalone files copied to the delivery directory:

```powershell
& $py C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-03/complete_interpolation.py C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-03/control.json
```

The standalone checker is also portable to Python/NumPy on other operating
systems; the bounded replay launcher specifically uses Windows Job Objects.
On this shared host, use the bounded driver for the full replay. No external
data, network connection, other session, or mutable main branch is required.

Delivery gates (from checkout root, captured base is mandatory):

```powershell
& $py tools/delivery/check_delivery.py --branch b14-03-astra --base 9898e56941a7665f231873481dae956f08509995
& $py tools/delivery/check_delivery.py --branch b14-03-astra --base 9898e56941a7665f231873481dae956f08509995 --bundle C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-03/b14_03_astra.bundle
```

No larger-cell CI verdict is implemented. LMR remains a24=274,
determinant rank 273, padded rank >=269, D in [-4,+1].
