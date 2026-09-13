# Resource decisions

2026-09-13, gpt-6-astra throughout. Initial numerical lease 02 was confirmed
before the pilot; one numerical job ran. Controls returned 0 in 2.032 seconds,
with aggregate peak Job Object memory 47,390,720 bytes. All liveness, changed
source, changed point, factorial, zero-outcome and dense residual checks passed.

Preregistration commit: d34d4e95 (full identifier in Git history).
Pilot returned 0 in 6.992 seconds. Carrier: 209,487 monomials, 1,576 signed
columns, 6,346 raising rows, 15,731 nonzeros. The cover already has 1,575
pivots, leaving one residual coordinate. The first determinant point is nonzero.

Decision: continue cells 2 through 9 under a single 900-second production cap
and the unchanged 1536 MiB aggregate memory cap. Their original monomial counts
remain below 320,000; the local residual guard refuses nU>2000 or triangular
blocks above 256 MiB. The measured pilot supports this bounded attempt; no
90-minute extension is needed. Preserve all per-cell checkpoints. Before launch,
LEASES.json again lists holders 01 and 02. Each process uses one BLAS thread.

Final source/point replay is a separate bounded job after production ends;
the lease remains held until that work completes and release is recorded.
