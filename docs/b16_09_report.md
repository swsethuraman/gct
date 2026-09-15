# B16-09 delivery: two-dimensional geometric completion

Completed: at quartic degree19 and weight(57,4,3,2^6), the two B15-08 sources have determinant rank2. Their exact rational minor is166461230261179373415548625/256. With the fresh ambient character sum2 and inherited stable identification, a=m_det=2, i_det=0, and D<=0. The same conclusion holds at delta>=19, weight(4*delta-19,4,3,2^6). No earlier finite stabilization or exact padding rank is claimed.

The proof and complete arithmetic are in `docs/b16_09_proof.md` and `results/b16_09/certificate.json`. The original B15-08 source and report are attributed and preserved byte for byte. Six source/report files also match the integrator's intake snapshot. `delivery/b16_09/input_manifest.json` records SHA256 for all24 actual input files, including these comparisons, the frozen brief, board, intake, source modules, local wrapper, and Python executable provenance.

Fresh work consists of two integral traceless determinant pencils, independent integer polynomial expansion, full16-variable invertible frame completions, integer source evaluation by both finite differences and a rational trace identity, two-prime polynomial reconstruction, and the exact289-term ambient character sum. The source highest-weight proof, character algorithm, and S57 stable identification are inherited; the report makes no source-count/image-rank substitution. No padding computation was needed: only m_pad<=a is used, leaving independent ten-variable z*per3 intact.

All numerical work used the assigned `.venv/python.exe`, inspected `analysis/b15_bound.py`, one process and one BLAS thread. Every new run was capped at60 seconds/512 MiB with an enforced Windows Job Object. The wrapper's historical metadata labels read batch15/B15-09; the uniquely prefixed receipts below identify these B16-09 runs.

| Run | Exit | Wall seconds | Aggregate peak MiB |
|---|---|---|---|
| price | 0 | 0.0761 | 18.39 |
| one-point pilot | 0 | 0.0900 | 18.53 |
| exact certificate | 0 | 0.1694 | 21.34 |
| input packaging | 0 | 0.0908 | 13.68 |
| fresh bounded receiver | 0 | 0.3001 | 23.26 |

Pricing preceded evaluation: <=47,520 coefficient-product visits and88 order-eight bracket determinants per point, with only486 tensor entries. The two actual integer constructions used23,109 and24,036 coefficient-product visits. The pilot measured0.0137s construction and0.00583s evaluation. The final calculation used two points and at most528 bracket determinants across integer and both modular paths. Neither a dense carrier nor a heavy job ran. No heavy lease was acquired; none is held and no release is pending. All five listed run PIDs were absent at completion. The launch-runtime PID46992 was also absent.

Process inspection preceded computation. CIM command-line inspection was denied by Windows; ordinary Get-Process succeeded, and no slot09 calculation was pending. No process was killed or duplicated. Read-only Git confirmed the frozen head5e555cbe23725a247b572dde9b0ac9338f5dc797 and tree25ca726a9ff15b3e11fb2ef8254b2524e15fb4c2. No Git mutation, shared-file change, push, or publication was performed. The output is a hashed filesystem delivery; no commit or unified merged base is asserted.

Run this receiver from the assigned B15-09 worktree:

```powershell
& ./.venv/python.exe -B analysis/b15_bound.py --slot 09 --name b16_09_receiver_again --seconds 60 --memory-mb 512 analysis/b16_09_receiver.py replay
```

The receiver imports the bundled source snapshots, verifies input hashes, regenerates the determinant coefficients, frames, exact values, modular minors and ambient sum, compares the saved certificate, and rejects two deliberate mutations. It does not rerun B15 production or write to B15 paths. Python-flint is required from the recorded worktree environment. Resource receipts are under `results/logs/b16_09_*_resources.json`; receiver output is `results/b16_09/replay.json`.

No next determinant witness is needed: the assigned rank2 completion is complete. Exact D would require the padding image rank. The known upper bound alone gives D<=0, which is the delivered geometric exclusion.
