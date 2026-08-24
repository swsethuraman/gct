# Final assembly for the f1C grind (scheme 1, point C)

## Completed 2026-08-24: TOTAL_f1C = 2 x 576,072,000 = 1,152,144,000
See results/results_f1C.md for the full table. This file documents the
operational procedure (kept for reproducing or extending the grind).

## Workers
- `sh w1.sh` (g1) and `sh w2.sh` (g2): each loops its subproblem list,
  retrying until r_XX.out contains VALUE; dp2g resumes from ck2 checkpoints.
- `sh resume.sh` revives dead workers (normal after container idle).
- RAM budget 7GB / 2 cores: never run extra compute beside two workers.

## Subproblems
36 subproblems (sigma6, sigma7) in S3 x S3 reduce by the symmetry
pi = (1 2)(3 6)(4 8)(5 7) of point C (sign +1, rho = (1 2)) to 18 orbit
representatives contributing equally:
- g1 reps: 00 02 04 12 14 16 18 20 22
- g2 reps: 01 03 05 13 15 17 19 21 23, plus 07 (= partner of 00, validation)

## Completion + assembly
XX done when r_XX.out contains `VALUE V (final states 1)` (states must be 1).
    total_f1C = 2 * sum of the 18 representative VALUEs  (exclude r_07)
Validation gates (all passed): VALUE(00) == VALUE(07); final states 1
everywhere; level-profile regression for subproblem 00 (L8: states
128027708, emitted 422952740, sum|w| 603408404).
`python3 assemble.py` performs the assembly + gates.
