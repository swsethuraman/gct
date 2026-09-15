# B16-03 portable receiver

This folder contains the executable equation export, exact arithmetic
certificate, proof, report, input hashes, and measured resource receipts.
It requires Windows and Python with python-flint. No B15 evaluator or saved
B15 Hessian coefficient is loaded. The unchanged B15 Job Object wrapper is
included solely for caps and receipts; its receipt labels still say B15.

From this delivery directory, use the assigned existing environment:

```powershell
& 'C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-03/.venv/python.exe' -B analysis/b15_bound.py --slot 03 --name b16_03_portable_receiver --seconds 60 --memory-mb 512 analysis/b16_03_receiver.py verify
```

The receiver recomputes the new padding substitution, ordinary quartic,
both full Hessian polynomials, normalization, pole-clearing circuit, root
and torus controls, and determinant controls, then compares every arithmetic
certificate field. It also checks the finite comparison arithmetic when
the received comparison file is present. The finite ambient count and B15
bounds remain explicit inherited inputs, not a fresh census in this slot.

The certificate proves a nonzero degree-23 global determinant equation with
highest weight `(61,15,2^8)`. Its independent-padding value is
`-26743148924112014067635076791795712`. Under slot02's a23=189 and accepted
bounds, this finite cell has `D<=-20`. The proof explains why a separator can
coexist with a negative multiplicity gap.

`MANIFEST.json` binds the delivered files by raw-byte SHA256. A replay adds
its own new runtime receipt, and may refresh `receiver_verify.json`; those
post-delivery execution outputs are distinguished from the shipped manifest.
All source and arithmetic outputs remain under this slot's owned paths.
