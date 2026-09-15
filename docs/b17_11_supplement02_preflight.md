B17-11 supplement02: price recorded before the one new permitted control.

Use the existing interpreter and re-inspected, unchanged original wrapper:

```powershell
& .venv/python.exe -B analysis/b15_bound.py --seconds 60 --memory-mb 512 --name b17_11_supplement02 --slot 11 analysis/b17_11_supplement02_verify.py
```

The receiver imports no producer arithmetic. It expands a 4x4 polynomial
determinant by a subset recurrence after multiplying its first row by t,
then verifies the exact t factor. A Cayley-Hamilton formula checks the nine
adjugate entries independently of the producer's cofactor implementation.
Binomial translation at J checks all four saved Taylor coefficients. It also
checks the 16-coordinate linear change, a fixed 4x4 matching decomposition,
and the clipping inequality on tiny artificial integers. No representation
source, character census, rank search, new padding point or symbolic package.

Price: under 5 seconds and estimated 64 MiB commitment. The arc's direct
permutation support bound is 192 raw terms; degree-four binomial translation
adds at most 16 terms per monomial. Hard dictionary and pair-operation guards
are 10,000 and 1,000,000. Actual enforcement remains 60 seconds / 512 MiB,
one process and one configured BLAS thread, with only the wrapper's deadline
thread. Estimates are not measurements or a heavy lease. A failure/cap hit
is retained as uncomputed; no second control is authorized in this supplement.
