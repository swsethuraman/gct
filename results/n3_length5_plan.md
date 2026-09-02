# Plan: testing the onset conjecture from below at `n = 3` (paper 1's `D_5`)

Session 40 (2026-09-02).  Conjecture 2 of `docs/onset_conjecture.md` says
`onset I(D_5^{det_3}) = cap(3) = 65`; paper 1's record is `I(D_5)_δ = 0` for
`δ ≤ 7`.  The conjecture is testable from below on paper 1's own object:
**any length-5 cell `(λ, δ)` with `mult_det < a` at `δ ≤ 64` kills it and pins
`δ_0`**; every empty cell is evidence of the weak kind (absence).  This file
is the census of what exists at `δ = 8..12`, the record of what this
session ran (all empty), and the ordered plan a compute session executes.

Code: `analysis/wk9_s40_n3census.py` (census; `results/n3_census.md`, pickle
`results/logs/s40_n3census.pkl`), `analysis/wk9_s40_n3cells.py` (gates and
runs; ledger `results/n3_ledger.md`, per-cell pickle
`results/logs/s40_n3cells.pkl`, logs `results/logs/s40_n3cells_*.log`).
Pipeline: session 36's stabiliser-isotypic reduction
(`analysis/wk9_s36_stabred.py`, corrected raising rule, every simple raising
operator, certified compressed kernel above `n_χ = 2500`), with `det_3`
pencils in five variables as the evaluation points (box `±40`, `a + 8`
points, seed 11), both house primes.  Only the det side exists at `n = 3`:
the object is `D_5 = D_5^{det_3}` alone (there is no pad side in paper 1),
and `I(D_5)` is concentrated at length exactly 5 (paper 1, Remark
`rem:crossover`), so only length-5 weights are listed.  Gate `a ≥ 1`
(`docs/s37_review.md` §2b).

## 1. The census (`results/n3_census.md`)

`N_S` by the s36 generating-function DP; `n_χ` by orbit enumeration where
`N_S ≤ 250000` and `N_S/|Stab| ≤ 16000`, else the lower bound `N_S/|Stab|`
marked `~`; memory `2.5e-8 · n_χ²` GB; **fits** = `n_χ ≤ 15500` (s36's
measured frontier on a 7 GB container with 6.5 GB usable: flint's
`nullspace` holds three `8 n_χ²` copies).

| `δ` | length-5 cells with `a ≥ 1` | ambient units | cells that fit | units that fit | `n_χ ≤ 2500` | `n_χ ≤ 5000` | largest `a` | rectangular (invariant) cell |
|---|---|---|---|---|---|---|---|---|
| 8 | 107 | 227 | 95 | 203 | 41 | 60 | 7 | — |
| 9 | 188 | 688 | 120 | 421 | 49 | 70 | 11 | — |
| 10 | 305 | 1926 | 126 | 535 | 55 | 74 | 21 | `(6,6,6,6,6)`, `a = 1`, `N_S = 1350088`, `n_χ ≈ 11251` |
| 11 | 468 | 5049 | 140 | 628 | 55 | 83 | 54 | — |
| 12 | 680 | 12543 | 154 | 729 | 55 | 90 | 101 | — |

Compared with `n = 4` (`results/s36_census.md`) the `n = 3` weight spaces
are not small: the balanced cells are `N_S ~ 10^5–10^6` at `δ = 10` already,
and the fraction of *units* that fits falls from 89% at `δ = 8` to 6% at
`δ = 12`.  The cheap corner is the peaked one (`λ_1` large, small parts
repeated — large `Stab_W(λ)`), which is exactly where a low-degree
equation is least likely to sit; the balanced corner is where it would sit
and is what costs.

Timings this session (two cores, one worker): `n_χ ≈ 300` in `< 1 s`,
`1246` in 27 s, `2838` in 30 s, `4851` in 54 s (both primes, kernel plus 9
evaluation points); s36's calibration above that: `4562` in 82 s, `10091` in
7 min, `13969` in 16 min, and a cell at `n_χ = 16005` was OOM-killed.
Above `n_χ ≈ 8000` the container is a one-worker machine.

## 2. Validation gates (run before any new cell; both passed, `s40_n3cells_validate.log`)

- **(a) reduced vs unreduced at `n = 3`.**  `(16,2,2,2,2)`, `(14,4,2,2,2)`,
  `(13,5,2,2,2)` at `δ = 8` through `wk8_s30_core.measure` (unreduced) and
  `measure_reduced`: same `a` (1, 2, 3), same `N_S` (427, 1444, 2197), same
  `mult_det` (`= a`), both primes.
- **(b) a bite-detecting anchor.**  The `n = 4` cell `(4,4,4,4,4)`, `δ = 5`
  through the same reduced code with `det_4` and true padded-permanent
  points: `a = 1`, `mult_det = 1`, `mult_pad = 0` — s36's `I_5` bite
  reproduced.  The pipeline sees a rank drop when there is one.

## 3. What this session ran — every cell empty *(measured; `results/n3_ledger.md`)*

| tranche | cells | units | result |
|---|---|---|---|
| `δ = 8`, all cells with `n_χ ≤ 5000` | 60 of 107 | 120 of 227 | `mult_det = a` at every cell, both primes |
| `δ = 9`, all cells with `n_χ ≤ 2500` | 49 of 188 | 92 of 688 | `mult_det = a` at every cell, both primes |
| `δ = 10`, the rectangular cell `(6,6,6,6,6)` — the unique degree-10 `SL_5`-invariant of cubic threefolds (`N_S = 1350088`, `n_χ = 12321` exact, compressed route, 24 min) | 1 | 1 | **`mult_det = 1 = a`, both primes**: the invariant does not vanish on `D_5` |
| `δ = 8`, further cells `5000 < n_χ ≤ 9100` (in flight at bundling time; whatever the ledger lists) | see ledger | | `mult_det = a` at every completed cell |

So `I(D_5)_8` is empty on at least 60 of 107 cells, including every cell
with balance `≥ 6` below `n_χ = 5000` and the balanced `(8,4,4,4,4)` (`n_χ =
2838`); `I(D_5)_9` is empty on the 49 peaked cells; and **no
`SL_5`-invariant of cubic threefolds of degree below 15 vanishes on the
determinantal ones** (degree 5: s28; degree 10: this session; `5 | δ` is
forced for an invariant).  The sceptical branch never fired; the STOP rule
never triggered.  Nothing here moves the lower end of paper 1's bracket
(which needs *every* cell of a degree), and nothing contradicts the
conjecture.

Why the invariant cell mattered more than its size: a bite there would
have been an `SL_5`-*invariant* of cubic threefolds vanishing on every
determinantal cubic — the cheapest conceivable equation of `D_5`, in the
smallest possible weight class — and it is the only invariant cell in the
whole range (`5 | δ` is forced; `δ = 5` was measured empty by s28, `δ = 15`
is out of reach).  Its emptiness says no invariant vanishes on `D_5` before
degree 15; the `n = 4` analogue, `(8^5)` at `δ = 10` (`|Stab| = 120`), is
the corresponding single test there and is recommended.

## 4. The plan for a compute session (ordered; pre-register first)

Pre-registration to copy: P1 = the two gates of §2 pass; P2 = "every cell
run returns `mult_det = a`" with the regime stated (the conjecture's prior
is low-to-moderate, `PREREG_s40.md` P1.4, so P2 is a genuine prediction,
not a formality); the STOP protocol below verbatim.  Bank every cell with a
commit; insurance bundle every few hours; one worker above `n_χ ≈ 8000`;
kill by explicit PID only.

1. **Finish `δ = 8`** — the 47 cells above `n_χ = 5000`, of which 36 fit
   (`5070 ≤ n_χ ≤ 15700`; ascending, ~3–4 h total).  Completing the fitting
   part leaves 11 cells (`n_χ ≈ 16000–41600`, all balanced, 19 units) as
   the honest residue.  Priority cells: the most balanced —
   `(6,6,4,4,4)` (7523), `(6,6,6,4,2)` (7923), `(7,7,4,3,3)` (9863),
   `(7,6,6,4,1)` (10149), `(8,5,5,3,3)` (10190), `(7,7,5,3,2)` (14639),
   `(9,5,4,3,3)` (14898) — and the largest-`a` ones `(10,6,4,2,2)` (`a = 7`,
   5682), `(9,7,4,3,1)` (`a = 5`, 9067).  Interleave 3 : 1 ascending :
   balanced, as s36 did.
2. **`δ = 9` beyond `n_χ = 2500`** — 71 fitting cells (~5–6 h).  Priority:
   `(9,9,3,3,3)` (`a = 1`, 3569), `(6,6,6,6,3)` (`a = 1`, `≈ 10588`),
   `(7,7,7,3,3)` (10680), `(8,8,7,2,2)` (`a = 2`, 11316); largest `a`:
   `(13,6,4,2,2)` (10, 6806), `(12,8,4,2,1)` (10, 6910), `(12,7,4,2,2)`
   (10, 8791), `(11,8,4,2,2)` (11, 10393).
3. **`δ = 10`** — 126 fitting cells (535 units); after the invariant, the
   balanced `(11,11,4,2,2)` (`a = 3`, 8301), `(11,11,3,3,2)` (8700),
   `(12,9,3,3,3)` (10148), and the large-`a` `(14,8,4,2,2)` (18, 12625),
   `(14,8,5,2,1)` (15, 12651), `(13,9,4,2,2)` (15, 14847).  The 55 cells
   below `n_χ = 2500` cost minutes in total and should be done first as a
   sweep.
4. **`δ = 11, 12`** — the cheap corner (55 cells each below 2500, minutes)
   as sweeps, then the most balanced fitting cells: `(11,11,9,1,1)` (`a = 2`,
   3780), `(13,13,3,2,2)` (6528), `(12,11,8,1,1)` (6672), `(10,10,10,2,1)`
   (9674) at `δ = 11`; `(15,15,2,2,2)` (1607), `(13,13,8,1,1)` (`a = 3`,
   4858), `(12,11,11,1,1)` (6457) at `δ = 12`; and the largest-`a` fitting
   cells (`a = 21` at `δ = 11`: `(17,8,4,2,2)`, 13797; `a = 22` at `δ = 12`:
   `(20,8,4,2,2)`, 14300).
5. **What never fits** on this container: 12 cells at `δ = 8`, 68 at `δ =
   9`, 179 at `δ = 10`, 328 at `δ = 11`, 526 at `δ = 12` — the balanced
   majority of the units from `δ = 10` on.  Two ways past the wall, in
   order of cost: (i) the compressed-kernel route already drops the
   assembly constant; a container with 32 GB reaches `n_χ ≈ 36000` and
   most of `δ = 9, 10`; (ii) the invariant-theoretic route of paper 1's
   Question 8.5 (semi-invariants of `(M_3)^5` in bidegree `(δ, δ)`) or
   abstract-HWV evaluation (Direction 7 of `docs/theory_directions.md`),
   neither of which pays the weight-space wall.

**STOP protocol on a bite** (`mult_det < a` at any cell): no further cells.
(i) Re-measure at `3(a + 8)` fresh points, seed 907, both primes (the runner
does this automatically and records both numbers).  (ii) Exhibit the
vanishing highest-weight vector(s) and reconstruct exactly over `Z`
(`analysis/wk9_s36_exact.py`, CRT over the two primes); verify every simple
raising operator kills it over `Z`.  (iii) Evaluate the exact vector at 20
independently built `det_3` pencils in five variables (a `3×3` matrix of
random integer linear forms, determinant expanded symbolically — the
construction of `wk9_s36_bite.py` with `det_3` in place of `per_3`), and at
20 random cubics: zero at every pencil, nonzero at generic cubics.  (iv)
Write `docs/DELTA0_PINNED.md` with every input named: then `δ_0 = δ` for
paper 1, Conjecture 2 is dead at `n = 3`, and `docs/paper1_delta0_patch.md`
is superseded by a two-line statement.  (v) The session ends there; the
integrator re-derives before anyone uses the number.

## 5. What the outcomes mean

- **A bite at `δ ≤ 64`** pins `δ_0` (the first five-row equation of `\cO`
  for `det_3`) exactly, closes Question 8.5's bracket, and kills the onset
  conjecture at `n = 3`; the same mechanism would then be expected to beat
  `300` at `n = 4`, and the `n = 4` hunt should look for its analogue at
  once.  It would *not* be an obstruction (det-side, permanent-independent).
- **Emptiness through `δ = 12` on every fitting cell** raises the weak
  evidence for the conjecture but moves paper 1's bracket only when a whole
  degree is closed; `δ = 8` needs 11 unreachable cells (19 units) for that,
  so the honest bracket after a full session is still `8 ≤ δ_0 ≤ 65` unless
  those 11 are reached elsewhere.
- **The invariant cell** decides a clean sub-question on its own: whether
  any `SL_5`-invariant of cubic threefolds of degree `< 15` vanishes on the
  determinantal ones.

## 6. Costs and honesty

- Every number above is from this container's timings and s36's frontier;
  a different container re-calibrates by running the two gates and one
  `n_χ ≈ 5000` cell.
- `a` is asserted against the plethysm and `rank(R) = n_χ − a` is asserted
  in-run at every cell; a compressed-certificate miss is retried once with
  a different projection seed and otherwise stops the cell.
- Ranks attaining `a` are one-sided certificates (`rank_p ≤ rank_Q ≤ a`),
  so "empty" cells are proved empty; a rank below `a` is believed only after
  the STOP protocol.
- The per-cell pickle stores kernels only for `n_χ ≤ 3000` and stays under
  5 MB; larger kernels are reproducible from the cell's parameters (seed,
  primes, projection seed 101).
