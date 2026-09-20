# Pre-registration — B24-04 pilot 2 (`b24_04_p2_saturate`)

Written and hashed after pilot 1's output was read and before pilot 2 was written or run. The
pilot prints this file's sha256 and pilot 1's output sha256 in its own output.

## Why

Pilot 1 (`results/b24_04/p1_patterns.json`) found that `s_a` (the multidegree) grades `F^L_{-1}`
with graded dimensions `7, 31, 28, 4`, and that every other pre-registered statistic has a rank
profile that tracks the **sample size** rather than the statistic. For one statistic, `s_inv`, and
to a lesser degree `s_cr`, `s_sp`, `s_nk`, `s_rep`, some low classes had more sampled patterns than
their measured rank, which pilot 1 could only label MEASURED. Pilot 2 decides those classes by
sampling each one directly and heavily.

This is the **only** live thread from pilot 1. No new statistic is introduced.

## The classes to be decided (fixed here; no class added after seeing results)

| block | dim | statistic and threshold `j` | pilot 1 saw (`n`, rank) |
|---|---|---|---|
| `11:2,3,3,1` | 31 | `s_inv <= 11` | 46, 27 |
| `11:2,3,3,1` | 31 | `s_inv <= 13` | 61, 29 |
| `11:2,3,3,1` | 31 | `s_cr <= 27`  | 29, 28 |
| `11:2,3,3,1` | 31 | `s_sp <= 11`  | 15, 15 |
| `11:3,2,2,2` | 28 | `s_inv <= 12` | 37, 25 |
| `11:3,2,2,2` | 28 | `s_nk <= 5`   | 18, 18 |
| `11:3,2,2,2` | 28 | `s_sp <= 11`  | 7, 7   |
| `11:1,4,4,0` | 7  | `s_rep <= 0`  | 8, 6   |
| `11:1,4,4,0` | 7  | `s_sp <= 11`  | 10, 6  |
| `11:4,1,1,3` | 4  | `s_cr <= 20`  | 4, 4   |
| `11:4,1,1,3` | 4  | `s_sp <= 10`  | 3, 3   |

## Method

Rejection sampling under a **third** seed `20260920`: a pattern is drawn, its statistic computed
from the pattern alone (cheap, no tensor work), and it is evaluated only if it falls in the class.
Accepted patterns are evaluated at the 70 certified points and the rank of the class is tracked.

Sampling for a class stops at the first of: (i) rank reaches the block dimension; (ii) 120
consecutive accepted patterns without a rise in rank; (iii) 400 accepted; (iv) the class's share of
the deadline.

## Verdicts (fixed here)

- **rank reaches the block dimension** -> the filtration is not proper at `j`; the statistic is
  **trivial** there. A modular rank is a floor for the rational rank (G27), so this direction is
  a **PROVED** negative.
- **rank stalls below the block dimension** under (ii) or (iii) -> **MEASURED candidate only**.
  A sampled rank below the ambient dimension is never a proof that the filtration is proper; it
  will be reported as a candidate with its sample size, and never as a grading.
- **stopped by the deadline** -> **UNDECIDED**, reported as such.

## Scope

Nothing here is claimed about Kronecker coefficients, about any other weight space, or about
plethysm in general. Producer-only (G18). One wrapped pilot, 60 s / 512 MiB, deadline-guarded at
55 s, JSON written after every class.

## Pinned inputs

```
analysis/b22_01_typed_v2.py    93d739eda3afd8c0dbddf452de1e73e76470864fd8ece27171f683574eb326fc  13226 B
results/b22_01/p2_basis.json   7162d852b4490d2f22702b9b974979e403dd0dfb8794cef92b6be894d9a66e79 293596 B
results/b24_04/p1_patterns.json  (sha256 recomputed and recorded by the pilot; pilot 1's output)
```
