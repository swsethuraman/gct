# Corrigendum to `work/descent_followup_claude_20260916/REPORT.md`

Claude session, 17 September 2026. The sealed packet (REPORT.md SHA-256 `80e90c1b…`,
MANIFEST.json `2c47ca21…`, 33 outputs re-verified by hash at the start of this session) is
preserved byte-for-byte; nothing below edits it. The accepted decision stands:
**INCONCLUSIVE on five-row arc exactness at `d = 5`, `lambda = (4^5)`.**

Every correction cites the sealed report by section and the underlying certificate by file.

## A. "33 contractions vanish identically" is not supported; the counts

**Where:** REPORT.md §C.4 (table and paragraph "The affordable contraction family …"),
§D.2 ("33 identically-vanishing candidates"), §F item 2 ("33 of 35 cheap candidates
vanish identically").

**Defect.** A zero value at finitely many integer points modulo one prime is not a
global identity, and no argument bounding the span of the "affordable family" was given.

**Replacement.** *The listed candidates evaluated to zero at the recorded points modulo
`p = 524287`. No global vanishing, and no upper bound on the span of the affordable
contraction family, follows without additional proof.*

**Reconciled counts** (read from `pilots/p2_carrier_arc.json`, `p4_paired_basis.json`,
`p6_basis.json`, `p8_basis_v2.json`):

| pilot | family | generated / accepted by the cost filter | attempted (evaluated) | points per evaluation | zero-valued at all points | nonzero | added to the independent set |
|---|---|---|---|---|---|---|---|
| P2 | column-local cyclic shifts | 19 planned (all 19 shifts; 400 random partitions also planned, 0 accepted) | 19 | 7 | 19 | 0 | 0 |
| P4 | paired blocks, over-strict filter | 0 of 60 generated | 0 | — | 0 | 0 | 0 |
| P6 | same-pairing paired blocks | 30 generated; 16 reached before the 50 s internal deadline | 16 | 5 | 14 | 2 | 2 (rank 2) |
| P8 | priced random and pair-block partitions | 4000 tried, 65 accepted; 19 reached before deadline | 19 | 5 (the P6 points) | 19 | 0 | 0 (rank stays 2) |
| **total** | | | **54** | | **52** | **2** | **2** |

**Distinctness.** The 19 P2 candidates are distinct by construction (distinct shifts). The two
P6 vectors are distinct partition pairs (checked). Distinctness among the other 14 P6
candidates and the 19 P8 candidates was **not verified**: their partitions were generated
from a seeded random stream and only their values were stored. So the supported statement
is "54 attempted, at most 54 distinct, 52 zero-valued at the sampled points, 2 nonzero, 2
independent"; the sealed "33 of 35" counted only P6 and P8 and omitted P2.

## B. The 2 GiB intermediate is a property of particular plans

**Where:** REPORT.md §C.4 last paragraph, §D.2 ("the next family needs `4^14`-entry
intermediates (2 GiB) per contraction"), §F item 2.

**Replacement.** *The `4^14`-entry (2 GiB) intermediate was the cost of the specific
contraction plans produced by the greedy planner and by the hand-ordered runner for the
partitions tried. It is not a lower bound over all evaluators or all plans. The affordable
family was not proved exhausted, and it was not proved that the three missing dimensions
require any plan of that size.* The feasibility note accompanying this corrigendum prices
one alternative (sparse) evaluator for exactly this question.

## C. The recommendation is restricted to `k = 1`

**Where:** REPORT.md §D.3 (the question over `(4k)^5`, items (i)–(iv)).

**Replacement.** *The recommendation applies to `lambda = (4^5)`, `d = 5` only.* For
`(4k)^5` the first tuple carries degree `4k`, so `z(K + tS)` is an even polynomial of degree
`<= 4k`, not `<= 4`; the three-point extraction of `[t^2]` and the specific map
`112 z(K5+S) - 7 z(K5+2S) - 177 z(K5)` do not transfer unchanged, and the harmonic
decomposition constants must be recomputed for each `k`. The stopping criterion "a
nonzero `4 x 4` forbidden minor proves exactness" uses `s = 5` and `m_det = 1` of the
present cell and does not transfer either.

## D. `C2(n) = 0` on one exact kernel vector does not prove redundancy

**Where:** REPORT.md §D.3 "Falsification" ("`C2(n) = 0` on an exact kernel vector kills the
transverse map as a detector in this cell").

**Replacement.** *A nonzero `C2(n)` on one globally certified survivor `n in ker C` proves a
rank increment. A zero `C2(n)` on one such vector proves only that `C2` does not detect
that vector; redundancy of `C2` relative to `C` requires `C2` to vanish on the whole
certified kernel `ker C` (here of dimension `5 - rank C`), or a spanning argument.*

## E. The two six-row conditions; the nature of the replay

**Where:** REPORT.md §D.1 first bullet ("detected by two independent globally necessary
conditions … both replayed here"); §A.1 and §E11–E12.

**Replacement.** *The two-pencil descent test `q(K) - 1120 q(L)` and the fourth-order
transverse condition `J2 - 108 J1 + 14 z(K)` are each separately valid globally necessary
conditions, each nonzero on `Q^2`. No common-source rank certificate for the pair was
computed, so nothing here says whether they are linearly independent functionals on
`M_(4^6)` (each has rank one; the pair has rank one or two).* And: *pilot P9 is a new
script that drives the producer's own evaluator (`sixrow_witness.invariant_Q`, `H6`,
`quartic`) at new points; it is an execution replay and a consistency check of the
producer's code and of the symbolic constants, not an independent implementation of the
contraction.* The statement in §A.1 that `Q(K)` and `H6(F_K)` were "replayed" is to be read
in that sense.

## F. Resource disclosures, retained and separated

**Where:** REPORT.md §C.7 and §F item 3.

**Retained facts.** (1) Pilots P1, P3 and P5 ran under `timeout 60` with
`OMP_NUM_THREADS=1` and **not** under the Windows Job Object wrapper; their wall times
(27.5 s, 0.8 s, 0.5 s) are console-reported, and no memory receipt exists for them.
(2) The first P7 attempt (a `4^14` plan) failed with a 2 GiB allocation error; its wrapper
receipt was overwritten by the successful P7 run of the same name, so the surviving
`results/logs/p7_arc_S0_resources.json` describes the second run only. The figures
"exit code 1, 0.6 s, peak job memory 94,101,504 bytes" for the failed run are
**console-reported, not preserved in a receipt**. (3) No missing evidence is recreated
here. The receipt set in the sealed packet is therefore **incomplete** for three pilots and
one failed run, exactly as listed; the sealed §C.7 table should be read with that caveat.

## What is unchanged

These corrections leave the certified partial result of the sealed packet unchanged:

- `s = 5`, `g = 6`, `a = 1`, `m_det = 1` (P1, P3; controls passing);
- `2 <= rank C <= 4` (floor from a nonzero modular minor of actual forbidden coefficients
  at three symmetric-part-zero points on two certified vectors; ceiling from
  `E subset ker C`, `dim E = 1`);
- `C2 = 112 z(K5+S) - 7 z(K5+2S) - 177 z(K5)` is globally necessary and nonzero on the source
  (rank 1 on the certified two-dimensional subspace);
- the independence of `C2` from `C` on `M_(4^5)` remains **unresolved**;
- the `(8,4,4,4,4)` exclusion, the ten corrections to the coefficient-algebra note, and the
  six-row replay values are unaffected.

A rank-four old-arc minor would prove exactness in this cell; a globally certified
`z in ker C` with `C2(z) != 0` would prove an additional constraint; neither would produce a
positive multiplicity gap in this already excluded cell.

---
See `FEASIBILITY.md` in this directory for the bounded sparse-evaluator attempt referred to in item B (decision: feasibility unresolved; one pilot, 1.7 s).
