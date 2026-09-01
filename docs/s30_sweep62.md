# Session brief — s30: the 62

**Branch `s30-sweep62`.**  Measurement lineage (25 → 27).  Pure compute with
one engineering prerequisite done right.  Goal: finish the genuinely open cells
at `n = 4`, `delta = 6`, `ell(lam) >= 5`.

## 0. Standing orders

- Rule 9; new files only; do not touch `paper/`, `PROJECT_NOTES.md`,
  `docs/boundary_deficit.html`.  Ancestry: `1203fe4` must be an ancestor of the
  tip; commits above are expected.  Pre-register first; push likely refused —
  bundle.
- **Your cells are exactly the `delta = 6`, `a >= 2`, `ell >= 5` cells not in
  session 27's nine** (their table is in `docs/n4_gate.md` if merged; the nine
  are `(14,5,2,2,1) (13,5,4,1,1) (12,7,3,1,1) (13,6,2,2,1) (11,8,3,1,1)
  (14,4,2,2,2) (12,7,2,2,1) (12,6,4,1,1) (12,5,5,1,1)`, all `mult = a` both
  sides).  **Do not touch length-4 or rectangular cells** — s29 owns those.

## 1. Why these 62 matter

They are the only weights anywhere in reach where a multiplicity obstruction is
arithmetically possible (`a >= 2`), not closed by the length-4 containment
(`ell >= 5` — the containment provably fails there: the block construction
needs every 5-ary cubic to be `3x3`-determinantal, and it is not, rank 29 of
35), and not yet measured.  Nine of 71 came back `D = 0` with `mult = a` on
both sides — a pattern with **no theorem behind it**.  The 62 decide whether
that pattern is a law waiting to be found or an artifact of measuring the
cheapest nine.

## 2. The engineering, first and properly

The wall is exact rank at `N_S` up to ~20,000 (cost roughly `O(N^3)`).
Session 28 hand-rolled a blocked elimination, its self-test failed, and it
rightly deleted it.  **Do not hand-roll.  Use an existing exact library** —
`python-flint` (`nmod_mat.rank()`, two different word-size primes) or Sage's
`Matrix_mod`.  Requirements:

- a self-test that runs FIRST: reproduce session 27's nine cells and session
  26's five, exactly;
- the structural check `rank(R) = N_S − a` at every cell (catches basis bugs);
- ranks over two independent primes; a rank attaining `a` is a certificate;
  a rank BELOW `a` must be reproduced at 3x evaluation points and both primes
  before being believed;
- **bank each cell as it completes** (append to `results/sweep62_ledger.md`,
  commit every few cells) — containers reset, and a lost half-sweep is the
  history of this programme.

Sort by ascending `N_S`; report partial coverage honestly if the clock runs
out — coverage fraction, not vibes.

## 3. What to record per cell

`lam, a, N_S, mult_det, mult_pad, D`, and for any cell with `mult < a` on both
sides: the kernel subspaces `U_det, U_pad` as explicit bases, and whether
`U_det = U_pad` / one contains the other / neither (two primes).  Equal
multiplicities with DIFFERENT subspaces is the single most valuable outcome
available — it would show the closures differing in a way multiplicities cannot
see.

## 4. Pre-registration

1. Predicted count of the 62 with `D = 0` and `mult = a` both sides.
2. Predicted count with `mult < a` (either side), and which side first.
3. A falsifier for "the nine were representative".

Integrator's prior: the pattern holds broadly (most cells `mult = a` both
sides) but not universally — the first `mult < a` appears on the pad side.
Genuinely uncertain; that is why the sweep exists.

## 5. Kill criteria

- **Any `D > 0`: STOP EVERYTHING.**  Verify by both routes, both primes, 3x
  points, and the independent `a` (raising-kernel vs plethysm).  If it
  survives, it is the programme's first multiplicity obstruction — report
  immediately with the full certificate, and do not resume sweeping.
- Any disagreement with the nine: stop; tool bug until proven otherwise.
- If flint/Sage cannot be installed in the container: fall back to the
  session-27 subsampled two-prime route and say so; do not hand-roll a new
  elimination.

## 6. Deliverables

    results/PREREG_s30.md        first
    results/sweep62_ledger.md    the running ledger, committed as it grows
    docs/sweep62.md              the verdict on the pattern
    docs/session_30.md           record, ledger, honest boundary
    analysis/wk8_s30_*.py        the tooling (with its self-test)
