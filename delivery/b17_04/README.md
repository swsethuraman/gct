B17-04: COMPLETE bounded continuation,14 September2026.

All eleven external determinant candidates match the accepted Hessian
basis exactly. A nonzero integer9-by-9 actual-padding minor proves a
fresh restriction rank floor9. The certified interval is9..10; the
second global kernel direction and exact rank9 remain unproved.

Read `docs/b17_04_report.md` for the full change-of-basis matrix, exact
ordering/scaling, proof, point construction, limits and one next sufficient
identity test. Machine-readable certificates are:

- `results/b17_04/basis_match.json`: C=M*E, M inverse, nonzero determinant,
  eleven exact zero residuals and complete candidate bracket ordering.
- `results/b17_04/Euler_relations.json`:884 universal relations, rank590
  in1019 coordinates; executable generation is in the corrected receiver.
- `results/b17_04/padding_points.json` and `restriction.json`: twelve
  fixed invertible sources, exact values, selected minor and full nonzero
  integer determinants, plus the sample kernel.
- `results/b17_04/kernel_target.json`: explicit unproved second identity.
- `results/b17_04/verification.json`: successful single-retry completion
  and37 input hash checks before and after execution.

The corrected receiver `analysis/b17_04_verify_next.py` ran successfully
under the inspected wrapper, unchanged from the saved repaired source:

```powershell
.\.venv\python.exe -B analysis/b15_bound.py --seconds 60 --memory-mb 512 --name b17_04_retry_20260914_01 --slot 04 analysis/b17_04_verify_next.py
```

Its preflight comment saying it had not yet run is retained to preserve
the exact executed input bytes; the new receipts record successful
execution. Wrapper wall time0.6656898999935947s, peak Job Object memory
27,930,624 bytes, exit0, hard60s/512MiB, one process/BLAS thread.

This command is a historical receipt, not authorization for another run.
The one corrected invocation authorized by the user is consumed. No
successful historical production was rerun. No heavy lease was used.

The first failed source `analysis/b17_04_verify.py`, failure transcript
and logs remain unchanged. Its initial delivery envelope/report/status
are archived in `results/b17_04/initial_delivery/`. Current and historical
artifacts, inputs and both resource receipts are bound by MANIFEST.json.
