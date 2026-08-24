# Week-3 grind results: f1C piece (scheme 1, point C)

Date: 2026-08-24. Exact integer arithmetic throughout (int64 DP, no floats).

## Headline result

    TOTAL_f1C = 2 x 576,072,000 = 1,152,144,000

Sum over the 18 orbit representatives of the 36 subproblems (sigma6, sigma7)
in S3 x S3, doubled by the proven orbit symmetry.

## Subproblem values (all with final states = 1)

| n  | (i6,i7) | rel = s6^-1 s7 | VALUE |
|----|---------|----------------|-------|
| 00 | (0,0)   | id             | +108,712,800 |
| 01 | (0,1)   | (1 2)          | -21,772,800 |
| 02 | (0,2)   | (0 1)          | -21,772,800 |
| 03 | (0,3)   | 3-cycle        | +301,870,800 |
| 04 | (0,4)   | 3-cycle        | +301,870,800 |
| 05 | (0,5)   | (0 2)          | -476,884,800 |
| 07 | (1,1)   | id [dup of 00] | +108,712,800 |
| 12 | (2,0)   | (0 1)          | -21,772,800 |
| 13 | (2,1)   | 3-cycle        | +301,870,800 |
| 14 | (2,2)   | id             | +108,712,800 |
| 15 | (2,3)   | (1 2)          | -21,772,800 |
| 16 | (2,4)   | (0 2)          | -476,884,800 |
| 17 | (2,5)   | 3-cycle        | +301,870,800 |
| 18 | (3,0)   | 3-cycle        | +301,870,800 |
| 19 | (3,1)   | (0 2)          | -476,884,800 |
| 20 | (3,2)   | (1 2)          | -21,772,800 |
| 21 | (3,3)   | id             | +108,712,800 |
| 22 | (3,4)   | 3-cycle        | +301,870,800 |
| 23 | (3,5)   | (0 1)          | -21,772,800 |

(Permutation indexing: itertools order over perms of (0,1,2); n = 6*i6 + i7.
07 is the redundant partner of 00, computed for validation only.)

## Validations

1. **Orbit-pair check (proven symmetry, empirical confirmation):**
   pi = (1 2)(3 6)(4 8)(5 7) preserves point C (sign +1) and induces
   (s6,s7) -> (rho s6, rho s7), rho = (1 2), preserving signed contributions.
   VALUE(00) = VALUE(07) = 108,712,800 exactly, via fully independent runs.
2. **Final-state uniqueness:** all 19 runs end with exactly 1 DP state.
3. **Empirical structure (unproven, 19/19 consistent, 8 confirmed as blind
   predictions):** VALUE depends only on rel = s6^-1 s7 with
   W(id) = +108,712,800; W((0 1)) = W((1 2)) = -21,772,800;
   W((0 2)) = -476,884,800; W(3-cycle) = +301,870,800.
   Assembly check: 2 x [3 W(id) + 6 W(odd-small) + 3 W((0 2)) + 6 W(3cyc)]
   = 2 x 576,072,000 = 1,152,144,000.
4. **Sign structure:** every VALUE sign equals sgn(s6) sgn(s7).

## Reference level profile (subproblem 00, for regression)

    level 7: states 54685987  emitted 100774838  sum|w| 141001840
    level 8: states 128027708 emitted 422952740  sum|w| 603408404

## Companion values already computed in this workspace (earlier phases)

    PHI18(det3)  = 36 x (-24,385,536,000) = -877,879,296,000
      (two independent routes agree: direct root-subtree DP and evalfile
       calibration run)
    PHI18(perm3) = 36 x 1,403,781,120     = +50,536,120,320

## Engine notes (for reproducibility)

dp.c: exact streamed level DP; per-epsilon 9-bit used-variable masks packed
in u64; open-addressing table (2^26 slots) with sorted spill runs;
delta-varint compressed runs (~5.5x, ~3.2 B/rec); levels processed in
bounded shards (auto-doubling P when a 6 GB scratch budget trips);
atomic checkpoints (level, shard, phase, input byte/record/prev-key,
run count, output position) written at every spill -> kill -9 / OOM /
container-suspension safe, resume granularity ~5 min. Validated:
level-by-level equality with the unsharded engine on real subproblems,
byte-identical results under forced 8-way sharding with mid-shard
kill/resume. Runtime ~45 min per subproblem on 2 cores / 7 GB / 30 GB.

## Provenance note (2026-08-24 evening)

The cloud container rolled back ~11h after the grind completed, deleting the
raw r_XX.out files. The values above were captured in-session before the
rollback (each subproblem's VALUE line was read and logged as it completed,
including the full 19-row table printed by assemble.py at completion) and
delivered to Swami in-conversation. The engine in this repo is the exact
reconstruction of the code that produced them, re-validated against the
canonical regression suite. Re-running the grind from inputs/evalin/f1C_*.txt
reproduces every row (~15 worker-hours).
