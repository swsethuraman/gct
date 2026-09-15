# B16-07: both low nine-row rungs are excluded

Slot 07, gpt-6-astra/xhigh. Existing worktree B15-07; frozen and freshly
observed HEAD `3eb29ed3b91e0e65ba5407e5031a71c4865fe4f3`.

An exact coefficient certificate proves that the determinant ideal is zero
in both assigned finite cells, conditional on the accepted complete stable
determinant four-space. Consequently neither cell can have a positive gap.

| Degree | Weight | Determinant ideal | Padded ideal floor | Gap bound |
|---|---|---:|---:|---:|
| 14 | (21,21,2^7) | 0 | 0 | D <= 0 |
| 15 | (25,21,2^7) | 0 | 3, inherited with freshly checked transport | D <= -3 |

Here `D=m_pad-m_det=i_det-i_pad`. The floor 3 is an **ideal** floor,
not a padded coordinate rank. No finite ambient multiplicity is needed or
asserted: in each cell `m_det=a`, and `D=-i_pad`.

The accepted stable ideal has basis `(s4 R3, s2^2 R3, s3 R2, s2 R1)`.
For a single explicit ambient quartic family, scale every nonleading
coefficient by `u`, normalize and depress, and compute these four functions
exactly. The coefficients of `u^28,u^26,u^25,u^24` form an invertible matrix.
A polynomial of coefficient degree at most 14 or 15 must have all four
coefficients zero. Thus its stable image is zero, and finite restriction
injectivity makes the original equation zero. The calculation is a necessary
polynomial-degree test; it is not an inference from sampled determinant zeros.

The complete proof, actual quartic, primitive matrix, determinant, and finite
restriction argument are in `docs/b16_07_proof.md`. All integer coefficients
of the Hessian determinant, quotient, remainder, depressed scalars, and four
functions are saved in `results/b16_07/pilot.json`.

Fresh work consists of the sparse integer producer, independent differentiation
of the genuine nine-variable quartic, monic polynomial division, the exact
nonzero minor, four altered-coefficient rejection controls, degree/weight
checks, q44 raising and nonzero checks, and all 23 actual input hashes.
The independent receiver imports no producer or historical evaluator.

Inherited premises are the reviewed global Hessian membership and complete
stable four-space, ultimately using stable ambient 533 and determinant rank
529; characteristic-zero highest-weight restriction; and CI73's three
independent degree-13 reducible equations. The finite injection argument is
also written out in the proof. The receiver does not replay the old expensive
rank or complete-interpolation calculations. Original B14 bracket and point
sources retain their Claude Opus 5 attribution; the snapshot Hessian review
and the new B16 coefficient certificate are Astra work.

| Fresh job | Exit | Wall seconds | Peak Job Object bytes | Peak working set bytes |
|---|---:|---:|---:|---:|
| Sparse producer, PID 10600 | 0 | 0.017685 | 13,176,832 | 21,897,216 |
| Independent receiver, PID 296 | 0 | 0.763830 | 56,524,800 | 70,533,120 |
| Delivery-script end-to-end replay, PID 40832 | 0 | 0.626825 | 56,168,448 | 70,365,184 |

All three ran under the inspected, unchanged `analysis/b15_bound.py`, using this
worktree's `.venv/python.exe -B`, a 60-second deadline, 512 MiB Job Object,
one process and one numerical thread. No heavy lease was requested or held.
All three PIDs were absent after completion; `results/b16_07/resource_release.json`
records their exit and the receipts. The inherited wrapper still prints
`board_numbering=batch15`; the unique `b16_07` receipt names bind these jobs
to this batch. Process command-line inspection was unavailable, but the
initial process inventory was read and no slot07 computation existed before
this run. No duplicate process was launched.

From the assigned worktree, a receiver run is:

```powershell
& ./.venv/python.exe -B analysis/b15_bound.py --slot 07 --name b16_07_receive_review --seconds 60 --memory-mb 512 analysis/b16_07_receive.py --out results/b16_07/receiver_review.json
```

Use a fresh receipt/output name per replay. `delivery/b16_07/receive.ps1`
chooses fresh names automatically. Input hashes use raw native bytes; the
launch intake and Slot05 review hashes match the frozen input manifest.

These results concern exactly degrees 14 and 15. The certificate uses high
powers of a scaling parameter to rule out low-degree lifts; it does not
recompute excluded higher-degree cells. Independent ten-variable `z*per3`
padding is preserved: every such form is reducible, and no variable is
identified with z. No equality of padded and reducible image ranks is used.

There is no missing witness for the two stated exclusions under the accepted
premises. To determine their exact gaps, the next sufficient witness is an
exact padded ideal multiplicity in the respective finite cell, giving
`D=-i_pad`. No positive-gap witness can exist in these cells under the stated
premises. The delivery is a filesystem certificate, not a new commit; shared
records and all B15 artifacts remain unchanged. Read-only Git confirmed the
frozen head; status emitted an inaccessible optional global-ignore warning.
