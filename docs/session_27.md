# Session 27 — the n=4 padded gate

Branch `s27-n4gate`.  2026-08-31.  Fresh clone of the public repo, container
only.  Nothing read from or written to `Projects\gct` (rule 9).  Nothing
appended to `PROJECT_NOTES.md` or `docs/boundary_deficit.html`.
`paper/det3-conductor.tex` untouched.  All files added are new.

Deliverables: `results/PREREG_s27.md` (commit `54a6b88`, before any
computation), `docs/n4_gate.md`, this record.

## 0. Clone state

`origin/main` at clone: **`1203fe4`** ("Integrator review of sessions 25 and
26").  Ancestry check as instructed: `git merge-base --is-ancestor 6aaab97 HEAD`
**passes**; the single commit above `6aaab97` is the integrator review.  No
rollback alarm.  (The ancestry form does not self-defeat: committing this
session's own work moves the tip without disturbing the check.)

## 1. What came back

* **All nineteen gate cells close**, and uniformly:
  `mult_det_4 = mult_per_3^pad = a` at every one.  `D = 0` nineteen times;
  no cell has `mult_det < a`, and none has `mult_pad < a` either.
* **They were never open.**  `D_4^{per_3^pad} ⊆ D_4^{det_4}`, because every
  restriction of `x_0 . per_3` to a 4-plane is a reducible quartic `ell . c`,
  every 4-ary cubic `c` is `3x3`-determinantal, and then
  `ell . c = det_4 diag(ell, M)`.  So `D <= 0` at **every** weight of length
  `<= 4` at **every** degree — including the 65 length-4 cells of the
  `delta = 6` gate.
* **The open region is `ell >= 5`**, where the containment argument provably
  breaks (5-ary cubics are not all `3x3`-determinantal: rank 29 of 35).  There
  are **71** such cells at `delta = 6`.  **Nine were measured — every one with a
  weight space under 2800 — and all nine give `D = 0` with `mult = a` on both
  sides**, three of them at `a = 3`.
* **Calibration passed**: my independent implementation reproduces session 26's
  five cells (including `mult_per`), `mult = a` at all 20 weights with `a > 0`
  and `delta <= 4` by three routes, and the raising-operator kernel dimension
  equals the plethysm coefficient on every length-`<= 4` weight with
  `delta <= 5`.  Kill criterion 2 did not fire.
* **New measurement**: `det_4` at `r = 5` has Jacobian rank **50** = `16·5 − 30`
  — the entry the brief left blank.
* **By-product**: the hypersurface of determinantal quartic surfaces has degree
  **`>= 6`**.  Quaternary quartics have no `SL_4`-invariant in degrees 1, 2, 3,
  5, and the sole degree-4 invariant does not vanish on `D_4^{det_4}`.

## 2. Prediction ledger

| | prediction | outcome |
|---|---|---|
| P1 | `D <= 0` at all nineteen, by containment, and at every `ell <= 4` weight at every degree | **CONFIRMED**, and the containment ingredient (rank 20 of 20 at `n=3, r=4`) independently re-measured |
| P2a | `mult_det = a` at all nineteen (`e > 5`) | **CONFIRMED** — 0 of 19 below `a`; and `e >= 6` independently pinned in §5 of `n4_gate.md` |
| P2b | `mult_pad < a` at **19 of 19** | **REFUTED** — 0 of 19.  A codimension-12 stratum carries the full ambient multiplicity in all nineteen isotypic components |
| P2c | `D < 0` strictly at all nineteen | **REFUTED** — `D = 0` at all nineteen |
| P3 | my implementation agrees with session 26 on all five cells | **CONFIRMED** |
| P4 | the gate table reproduces exactly | **CONFIRMED**, including `5 -> 0` at `delta = 4` and `35 -> 19` at `delta = 5` |

Two refutations, and they are the instructive pair.  In P1 I wrote that the
dimension heuristic "is not a valid argument, since isotypic multiplicities are
not determined by dimensions" — and then in P2b used exactly that heuristic to
predict that a codimension-12 ideal must bite somewhere among nineteen
components.  It bites nowhere.  The sign was right for a structural reason; the
strictness was wrong for the reason I had already named.

## 3. Verification

| quantity | route 1 | route 2 | route 3 |
|---|---|---|---|
| `a` (ambient) | dim ker of the raising operators | symmetric-function plethysm `h_delta[h_n]` | agree on every length-`<=4` weight, `delta <= 5`, `n = 3`; and on `(delta^4)`, `n = 4` |
| `mult` | rank mod `2^31−1` | rank mod `2147483629` | exact `Q` wherever the weight space is `<= 200` |
| calibration | session 26's five cells | 20 weights at `delta <= 4` give `mult = a` | the paper's `1, 6, 31` row requires exactly that |
| Jacobian ranks | chain-rule columns, two primes | closed forms `n^2 r − dim Stab` and `r + C(r+2,3) − 1` | every session-26 entry reproduced |

**On rigour.**  A rank attaining `a` is a certificate, not a sample:
`rank_p <= rank_Q <= a`, so `mult_p = a` forces `mult_Q = a`.  Every
multiplicity reported in this session attains `a`, so no probabilistic step
enters any conclusion.  Cells falling short would have been re-run with three
times the evaluation points before being believed; none did.

**A free consistency check worth recording.**  The padded closed form
`r + C(r+2,3) − 1` predicts 61 at `r = 6` and the measurement is 55.  That is
the formula's hypothesis expiring, not the formula failing: `per_3` stops being
dense in the `r`-ary cubics at `r = 6` (rank 50 of 56), and the corrected
prediction `6 + 50 − 1 = 55` is exact.  The place the formula breaks is the
place its hypothesis breaks.

## 4. Honest boundary

* The containment theorem is proved, but it rests on "every 4-ary cubic is
  `3x3` linear-determinantal".  That is classical for smooth cubic surfaces and
  the density is a Jacobian rank of 20 out of 20 at an integer point, which is
  rigorous by lower semicontinuity.  I did not verify the classical statement
  itself, only the density that the argument needs.
* `e >= 6` is a lower bound only.  I did not determine the degree of the
  determinantal hypersurface; `delta = 6` at `lam = (6,6,6,6)` has a weight
  space of about 12,000 and was not run.
* The `ell >= 5` region is sampled, not swept: 9 of the 71 cells at
  `delta = 6` were measured, chosen as the cheapest by weight-space dimension.
  Cheapest is a cost criterion, not a mathematical one, and an expensive cell is
  neither more nor less likely to be interesting.  The remaining 62 are pure
  compute — the run was cut by its own wall-clock limit, not by any difficulty.
  Nine of nine agreeing is suggestive but is not a sweep, and I have not proved
  anything about length 5.
* Nothing here bears on `n = 3`.  Session 26's Corollary 9 is untouched, and
  the five cells it rests on are reproduced rather than revised.

## 5. Files added

    results/PREREG_s27.md        pre-registration, committed first
    docs/n4_gate.md              the theorem, the gate, the nineteen, the next gate
    docs/session_27.md           this record
    analysis/wk7_s27_rank.py     my own highest-weight / evaluation rank algorithm
    analysis/wk7_s27_pleth.py    plethysm, the independent route for `a`
    analysis/wk7_s27_calib.py    the calibration battery (kill criterion 2)
    analysis/wk7_s27_gate.py     the n=4 gate table
    analysis/wk7_s27_nineteen.py the nineteen cells
    analysis/wk7_s27_jac.py      Jacobian ranks, independent
    analysis/wk7_s27_degF.py     the degree of the determinantal hypersurface
    analysis/wk7_s27_next.py     the ell >= 5 gate and its cheapest cells

Pure Python, exact integers and `Fraction`, no engine, no checkpoints.

## 6. What a successor should do first

1. **Take the `ell >= 5` gate, not `delta = 6`.**  65 of the 136 length-`>= 4`
   cells at `delta = 6` are already closed by §1 of `n4_gate.md`.  The brief
   for the next session should name the 71.
2. **Ask whether the containment survives at length 5 by another route.**  The
   nine measured cells all show `mult_det = mult_pad = a`, which is what
   containment would predict — so the evidence points at a theorem rather than
   at an accident.  The
   block construction fails, but that is a failure of one argument, not a proof
   of non-containment.  `dim D_5^pad = 39 < 50 = dim D_5^{det_4}`, so
   containment is dimensionally possible.  Deciding it would close or open the
   whole length-5 stratum at a stroke — far better value than measuring cells
   one at a time.
3. **Finish the 67.**  Pure compute; the cost is roughly quadratic in the
   weight-space dimension, and the largest are near 20,000.
4. **Pin `e`.**  One measurement at `lam = (6,6,6,6)`, `delta = 6`.  If the
   degree-6 invariant vanishes on `D_4^{det_4}` then `e = 6` and the length-4
   determinant multiplicities start dropping there — which would be worth
   knowing even though §1 has already closed those weights.
