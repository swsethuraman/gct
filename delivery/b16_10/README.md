# B16-10 bounded filesystem delivery

Read docs/b16_10_report.md and docs/b16_10_proof.md. The exact coefficient
receiver uses only the copied Python modules and copied input snapshots.
The finite census is an explicitly inherited input, with slot02 proof and
receiver receipt preserved. No Git binding or publication is claimed.

From the reused B15-10 worktree, use a fresh log/receipt name:

```powershell
& .venv/python.exe -B delivery/b16_10/analysis/b15_bound.py --slot 10 --name b16_10_portable_fresh --seconds 60 --memory-mb 512 delivery/b16_10/analysis/b16_10_receive.py verify --inputs-dir delivery/b16_10/results --certificate delivery/b16_10/results/jet_certificate.json --receipt results/b16_10/portable_fresh.json
```

The Windows wrapper enforces the Job Object and time caps. One process,
one configured numerical thread; standard library only. Portable here means
that no live B15/other-worker mathematical module is imported. A Windows
Python runtime and the inspected wrapper are still required for the caps.
SHA256_MANIFEST.json lists exact delivery bytes; input_hashes.json records
actual original paths, their hashes and the copied snapshot names.
