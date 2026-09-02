<!-- finalized from the completed screen at session end -->
# One-bit ledger — session 39

Phase 1 of `results/PREREG_s39.md`.  A **one-bit** cell (`a = 1, m_det = 0`)
has `mult_det ≤ m_det = 0` for free; it is an occurrence-obstruction candidate
iff its unique highest-weight vector is nonzero at a true padded-permanent
point.  A **forced** cell (`a > m_det ≥ 1`) has `mult_det ≤ m_det`; it is a
candidate iff the pad-side rank at true-pad points is `≥ m_det + 1`.

## Result

**The Phase 0 screen produced no one-bit cell and no forced cell** in the whole
eligible region — exhaustively: all **79,255** weights with `6 ≤ ℓ ≤ 10`,
`λ_1 ≥ δ`, `δ = 8..12`, of which **69,967** have `a ≥ 1`, and every one of those
satisfies `a ≤ m_det` (`results/longweight_screen.md`).  Phase 1 therefore has
**no obstruction test to run**: no cell has its determinant side zero for free
(`m_det = 0`), and none loses units for free (`a > m_det`).  This is the
session's result on the occurrence route — banked with the screen table, as the
brief prescribes for an empty screen.  Confirmed end-to-end by
`analysis/wk9_s39_onebit.py runall results/longweight_screen.csv`:
*"one-bit cells: 0 ; forced cells: 0 ; no obstruction candidate."*

## The harness (in tree, its core path P1-validated)

`analysis/wk9_s39_onebit.py` implements both tests against the s36-audited
certificate path:

- **one-bit test** — build the unique HWV by the validated stabiliser
  reduction (`wk9_s36_stabred.measure_reduced`; P1 reproduced three s36 ledger
  cells and the `l^3 m` witness exactly, `results/s39_validation.md`),
  reconstruct it over `Z` by CRT + rational reconstruction, assert every simple
  raising operator kills it over `Z`, then (i) evaluate at 20 `det_4` pencils —
  must vanish, auditing `m_det = 0`; a nonzero value is a KILL — and (ii) test
  20 true padded-permanent points `l(s)·per_3(A(s))` built by the independent
  `wk9_s36_bite.family('truepad')` construction — nonzero at any one is a
  candidate;
- **forced test** — pad-side rank at `3(a+8)` true-pad points, both primes;
  `≥ m_det + 1` is a candidate.

`STOP-EVERYTHING` on any candidate (`results/PREREG_s39.md` §4).  With the
screen silent, the harness ran no cell; it is delivered validated and unused.

| kind | λ | δ | ℓ | N_S | n_χ | verdict | notes |
|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | no one-bit or forced cell in the screened region |

_(finalized from `results/longweight_screen.md`)_
