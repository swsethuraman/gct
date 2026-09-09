# s86 — the balanced six-row cells

`board_numbering: batch13`.  Read `docs/batch13_worker_preamble.md` first.

## Mission

Session 57 named them and session 79 confirmed them: the balanced six-row cells
are the only place a six-row determinant equation of degree ≤ 12 can still hide.
They were priced out of reach until s80.

## What is true going in

- 682 six-row cells at `δ ≤ 12`, tail weights 13–23: `i_det = 0`,
  `mult_pad = mult_red`, `i_per4 = 0` at every one (s79, verified 17/18 by the
  integrator).  These are the **cheap — that is, skewed —** cells.
- 63 tails closed for every degree by Proposition S, from 69 first stable cells.
- The balanced cells (s57's T4) have `n_χ ≥ 10⁶`, `N_S·δ ≥ 10⁸`, above the old
  build wall.
- The record is `mult_det = a` at 210 six-row cells at `δ = 6..10`, every one
  skewed; `I(M_6)` has no component of tail weight ≤ 12.

## Task

The T4 balanced six-row cells in `N_S·δ` order on s80's builder, four families
(`det₄`, reducible `ℓ·c` with the `(★)` point-free mask, the true padded
`x₀·per₃` on a generic 6-plane, unpadded `per₄`), both primes, `K = a + 8`
points, on `analysis/wk12_s79_cell6.py` unchanged.

**Sort first stable cells (`a = a_∞`) to the front.**  A full rank there closes
its tail at *every* degree by Prop. S — s79 closed 63 tails with 69 cells, and it
is the highest information per second in the queue.

Calibrate first on three of s79's banked cells spanning the `a` range, both
primes, and on `(13,9,9,3,1,1)₉` (`a = 70`, `red = pad = 45`, `D_R = −25`), the
largest reducible bite in the record at any length.

## Order of work

The preamble's rule stands: **no quartic sweep at a new length before the cubic
screen at that length has run.**  Length 6 is screened at `δ ≤ 9` (subject to
s81) so this queue is licensed there.  At `δ ≥ 10` the `mult_pad = mult_red`
readings are measurements, not theorems — label them so.

## Predictions and falsifiers

- **P1 (0.7):** `i_det = 0` at every balanced cell reached.
- **P2 (0.6):** `mult_pad = mult_red` at every one.
- **P3:** a cell with `i_det ≥ 1` — the successor laboratory — or with
  `mult_pad < mult_red`.  Either triggers the protocol before it is reported
  anywhere; and a `mult_pad < mult_red` at `δ ≤ 9` contradicts Prop. 8(1) and is
  an instrument defect, not a result.
- **F1:** a calibration cell disagreeing with s79 at either prime → stop.

## Deliverables

`results/PREREG_s86.md`; `results/s86_cells.jsonl`; the tails closed by Prop. S;
the unreached region priced by `N_S·δ`; `docs/s86_report.md`; bundle + `.md5`.
