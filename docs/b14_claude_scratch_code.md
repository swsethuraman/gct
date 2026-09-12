# Batch-14 strategy session (Claude) — the scratch code, and what it reproduces

**Status: scratch.** This is the code written during the batch-14 strategy
session of 2026-09-11, cleaned up for the tree. Nothing here was run as a
pre-registered measurement, nothing was banked at the time, and each number
below comes from a single implementation unless the line says otherwise. It is
committed so the numbers quoted in the batch-14 memo can be re-run, and so the
next session starts from working code rather than a transcript.

Session conventions that **do** hold: every script carries a control that can
fail and runs it by default; every reported value is a printed number, not a
hand-transcribed one; nothing writes outside `results/`.

Written by Claude Opus 5 against baseline `7a47e2b`.

---

## Files

| File | What it is |
|---|---|
| `analysis/b14_claude_stable_count.py` | The stable slice of Proposition S: raw weight-space counts and stable multiplicities, at any tail length and any generator degrees. New code. |
| `analysis/b14_claude_hpad_general.c` | `analysis/wk13_b13_01_mcount.c` (B13-01) with the degree unfixed. Two mechanical changes, listed in its header. |
| `analysis/b14_claude_hpad.py` | `analysis/wk13_b13_01_hpad.py` (B13-01) with the degree unfixed, driving the counter above. |
| `analysis/b14_claude_aweyl.py` | A timed driver with banked controls for the house `wk9_s42_census.a_weyl`. No new mathematics. |
| `analysis/b14_claude_reach.py` | Which of B13-06's product targets are reached by a single Cartan product of the rung-13/14 relations (Lemma T of the memo). New code. |
| `results/b14_claude_reach.json` | Output of the last script: the per-target table. |

**Dependencies.** `numpy` for the stable counter; `gcc` for the C counter (built
into `/tmp` on first use); `analysis/wk9_s42_hpad.py` and
`analysis/wk9_s42_census.py` from the tree. No flint, no scipy, no CAS.

---

## Replay

Run from the repository root. Times are as measured in a 2-core container.

```
# 1. Stable slice: calibration against s79's five stable blocks, and a_inf = 4 at two of them
python3 analysis/b14_claude_stable_count.py --selftest                                  # <1 s, 7/7 PASS

# 2. The four stable multiplicities quoted in the memo
python3 analysis/b14_claude_stable_count.py --mult 17,2,2,2,2,2,2,2                     # 274,  ~95 s
python3 analysis/b14_claude_stable_count.py --mult 17,2,2,2,2,2,2,2 --degs 1,2,3        # 521,  ~95 s
python3 analysis/b14_claude_stable_count.py --mult 19,2,2,2,2,2,2,2                     # 392,  ~71 s
python3 analysis/b14_claude_stable_count.py --mult 21,2,2,2,2,2,2,2                     # 533,  ~77 s
python3 analysis/b14_claude_stable_count.py --raw  17,2,2,2,2,2,2,2                     # 7,212,907,703, <1 s

# 3. h_pad at rung 14, after the rung-13 control (which reproduces B13-01's 73)
python3 analysis/b14_claude_hpad.py --cell 25,17,2,2,2,2,2,2,2 --delta 14               # 73 then 159, ~30 s + ~42 s

# 4. Ambient multiplicities on the two neighbour ladders (controls first: 1 s + 101 s)
python3 analysis/b14_claude_aweyl.py --cell 63,19,2,2,2,2,2,2,2 --delta 24               # 390, ~217 s
python3 analysis/b14_claude_aweyl.py --cell 67,19,2,2,2,2,2,2,2 --delta 25 --no-control  # 391, ~224 s
python3 analysis/b14_claude_aweyl.py --cell 69,21,2,2,2,2,2,2,2 --delta 26 --no-control  # 531, ~260 s (reproduces B13-06)
python3 analysis/b14_claude_aweyl.py --cell 73,21,2,2,2,2,2,2,2 --delta 27 --no-control  # 532, ~271 s

# 5. The Cartan-reachability census over B13-06's targets
python3 analysis/b14_claude_reach.py                                                     # <1 s, 2/2 controls PASS
```

---

## What each number is for

| Number | Meaning | Status |
|---|---|---|
| 274, 521 at tail (17,2⁷) | The stable slice reproduces the banked `a` and `h_pad` of the LMR cell. | Agreement with two banked values; the strongest evidence here that the slice code is right. |
| 7.21×10⁹ | Raw stable weight space at the LMR tail, against `N_S` = 1.56×10¹¹. Divided by \|Stab\| = 5040 it is 1.43×10⁶, and s57 sizes the same slice at ≈1.4×10⁶. | Agrees with s57. |
| 392 at tail (19,2⁷) | Equals the banked `a` at (71,19,2⁷)₂₆, so that cell is the first stable cell of its ladder. | New. |
| 533 at tail (21,2⁷) | The banked `a` at (69,21,2⁷)₂₆ is 531, so that cell is **not** stable — two directions are still to be born. | New. |
| 390, 391 | `a` at (63,19,2⁷)₂₄ and (67,19,2⁷)₂₅. With 392 they give the ladder's birth counts, which bound `i_det` at the stable cell through s57's Lemma L. | New, single route. |
| 531, 532 | `a` at (69,21,2⁷)₂₆ — reproducing B13-06 — and at (73,21,2⁷)₂₇. | 531 is a reproduction; 532 is new. |
| 159 | `h_pad`((25,17,2⁷), 14): the target dimension of the rung-14 complete-interpolation certificate. | New, and **not independent**: it shares the counter and the strip enumeration with B13-01's 73. |
| 4 of 30, 23 of 205 | How few of B13-06's targets are settled by Lemma T alone. | New. |

---

## Caveats worth carrying forward

1. **`h_pad` = 73 and 159 share one lineage.** B13-01's Weyl alternation, B13-04's
   reconciliation and this script are the same method. The memo's Avenue 1 makes
   `dim N = h_pad` load-bearing, so it should be recounted by a *different*
   method — plethysm through character inner products, say — before anything is
   certified against it.
2. **The `(1,2,3)` reading of the stable counter is an identification, not a
   theorem.** It rests on one agreement, 521 at the LMR tail.
3. **The `a_weyl` values at 390, 391, 532 are single-route.** The house routine is
   well exercised, but these particular cells were computed once.
4. **Two cells were wanted and not finished** inside the session's time bound:
   `a`((77,21,2⁷), 28) — the closing cell of the (21,2⁷) ladder, where the stable
   count predicts 533 — and the ten-row degree-25 cells (68,17,2⁷,1) and
   (67,17,2⁸), both of which exceeded 560 s.
5. **The stable counter has no circuit.** It counts and it alternates; it does not
   evaluate. The stable bracket evaluator that Avenue 3 of the memo asks for is
   not here and is not started.

---

## Integrator's note, 2026-09-12

Banked at `4d19b8fd`. Nothing in the worker's text above is edited; this section
records what the integration machine reproduced before the commit.

**Static checks.** Seven files, largest 50 KB, all LF, no file over 5 MB. No session-link
URL and no session-link trailer anywhere. Exactly one script writes,
and it writes under `results/`. No filename collides with the tree. Every
dependency the manifest names is present: `wk9_s42_census.py`, `wk9_s42_hpad.py`,
`wk13_b13_01_mcount.c`, `wk13_b13_01_hpad.py`, `wk12_s79_stable.py`,
`results/b13_06/components.json`, `results/b13_01_hpad.json`,
`results/s63_aladder.json`.

**`b14_claude_hpad_general.c` carries the two changes it claims and no others.**
Diffed against `analysis/wk13_b13_01_mcount.c`: `DELTA` from `argv[1]`, and the
memo key repacked to 6 bits on coordinate 0. The repacking is sound — the driver
sorts each target descending, so only coordinate 0 can exceed 31, and the DP only
subtracts, so the bound is preserved down the whole recursion. The program exits
5 rather than aliasing if a target violates it. Key occupies 59 of 64 bits.

**Replayed here.**

| run | result | cost |
|---|---|---|
| `b14_claude_stable_count.py --selftest` | 7/7 PASS | <1 s |
| `b14_claude_reach.py` | both controls PASS; output **byte-identical** to the delivered `results/b14_claude_reach.json` | 0.1 s |
| `b14_claude_hpad.py --cell 25,17,2⁷ --delta 14` | control `h_pad(21,17,2⁷;13) = 73`, 15 strips, B13-01's `a3` exactly → PASS; then **`h_pad((25,17,2⁷),14) = 159`**, 27 strips | 38 s + 43 s |

Logs: `results/logs/b14_claude_hpad_verify.log`,
`results/logs/b14_claude_reach_verify.log`.

**The ladder values agree with an independent run.** `results/b14_prep/ladder_recount.log`
was produced on this machine before the scratch code arrived and gives 390, 391,
392, 531, 532 and 274 — the same values `b14_claude_aweyl.py` documents. Two runs,
one routine: this rules out transcription error, not method error. Caveat 3 stands.

**What the replay does and does not buy.** Re-running the author's code on another
machine is replay, not method diversity — which is why slot 4 exists, and why it
is told not to treat these scripts as its second method. **159 no longer rests on
one lineage:** Astra piloted the power-sum / Murnaghan–Nakayama route through the
banked `wk8_s30_pleth` before dispatch, and it returns 73 and 159 with every
channel matching the Weyl route partition by partition, importing nothing from
here. That is the recount, and it cost under a minute. Caveat 1 is discharged for
73 and 159; it still stands for 533 and the `a_∞` values.

The reach census is a finite enumeration reproducible bit-for-bit, which is worth
something — but on the strength of it I told slot 8 to check rather than rebuild,
and that instruction rested on controls that could not fail. Slot 8 is now told
to reconstruct all 717 target/source difference tests independently and compare
every flag. **And a reachability flag is not an exclusion**: it says
multiplication can carry a relation *if the source relation is certified*, so
every reached cell stays CONDITIONAL until slots 1, 2 and 7 deliver.

**Caveat 5 does not collide with slot 6.** The stable counter counts and
alternates; it does not evaluate. The stable bracket evaluator slot 6 asks for,
sharing no code with s69/s74, is not here and not started, so slot 6's
independence requirement is untouched.

**Caveat 4 is not funded.** `a((77,21,2⁷),28)` and the ten-row degree-25 cells
are named in slot 4's inputs as unfinished; no slot is reallocated to them.
