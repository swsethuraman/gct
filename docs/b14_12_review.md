# Review of B14-12

**Slot:** B14-12, `(12,4,4,4,4,4)` at `δ = 8` — the last cell of session 79's Q1
queue. Claude (`claude-opus-5`), one cloud container, 2 cores, 7.84 GB.
**Base:** `9898e569` / tree `cb688cd3`, the dispatch base, matched exactly.
**Delivered head:** `28f7a195`. Bundle 59,313 bytes, md5 `4bd25b9c…`, one part and
it is the whole file. `git bundle list-heads` gives one ref,
`refs/heads/b14-12-q1-last-cell`. The four single-writer files are untouched, and
so is every shared ledger — the change set is 15 new files and nothing else.
**Verdict: ACCEPTED.** Merged, with the cell rebuilt here from scratch. Intake gate clean on the first run,
the only delivery in the batch for which that is true.

**What it establishes.** `mult_det = a = 4` at both house primes, hence over `ℚ`:
`i_det((12,4,4,4,4,4), 8) = 0`, so `D ≤ 0` there. With it, **all 123 cells of
session 79's frozen Q1 queue carry `i_det = 0`. There is no six-row determinant
equation anywhere in Q1** — the successor laboratory that queue was built to find
is not in it. That is the batch's cleanest closed statement, and the slot the
board deprioritised is where it came from.

## 1. What I checked with my own code

| claim | how I checked it | outcome |
|---|---|---|
| `a = 4` | three ways: my own exact Weyl alternation over my own weight counter (600 terms, 341 distinct), the house `a_weyl_mod` (modular DP + CRT), and the census `a_weyl` the driver called | all three give 4 |
| `N_S = 27,009,659` | my own generating-function DP over the 126 quartic letters | exact |
| **`n_χ = 244,454`** | **my own signed-Burnside orbit count** over the `g`-orbits of the letters — a different lineage from the builder's `_canon_acc`. The character is trivial here (every repeated part is even), so `n_χ` is the plain orbit count | exact; signed sum 29,334,480 = 120 × 244,454 |
| the pilot control `n_χ = 1,606,104` at `(10,6,6,6,2,2)₈` | same route | exact, and it also reproduces that cell's `N_S = 18,337,360` and `\|Stab\| = 12` |
| `ceil(N_S/\|Stab\|) = 225,081` and `1,528,114` | arithmetic | both exact; `N_S/n_χ = 110.5`, not 120 |
| **all 123 `nchi_est` in `results/s79_queue.json` are `ceil(N_S/\|Stab\|)`** | checked every entry | 123 of 123 |
| the frozen queue is as `PREREG_s79` §2.4 describes | 123 cells, cost-ordered, endpoints, degree histogram | 123; ordered; `(13,7,4,2,1,1)₇` at `4.46×10⁵` to `(12,4,4,4,4,4)₈` at `2.16×10⁸`; 2/25/27/62/6/1 at `δ` 7–12 — every figure as frozen |
| **121 of the 123 are in `s79_cells.jsonl`, every one with `i_det = 0`** | joined the frozen queue against the delivery | 121 present, `i_det = 0` on all 121, none missing the field |
| the two absent are exactly the pilot and this cell | same join | exactly those two |
| the pilot closes the 122nd | `results/b13_10/pilot.json`: `a = 10`, `mult_det = 10`, `i_det = 0`, both primes | confirmed; its `N_S`, `n_χ`, `\|Stab\|` and `nnz` all match what B14-12 compares against |
| `cost_model` predicts 4,129 s | `3.06×10⁻⁶·N_S·δ + 1.07×10⁻⁶·\|Stab\|·N_S` | 4,129.2 s, 1.46× the measured 2,838.1; at the pilot it gives 684.4 against 812.1, 16 % under — so the model is not biased one way |
| the `N_S·δ`-only scaling gives 1,196 s | pilot 812.1 s scaled by `N_S·δ` | 1,196.2 s, **2.4× low** — and that is the model the assignment used |
| lean rate 0.686 GB per `10⁸`, below B13-10's 0.99–2.48 | from the delivered peak; B13-10's own suite recomputed | 0.686; the suite's minimum above-baseline rate is 0.964 and its largest cell is `N_S·δ = 3.15×10⁷`, so this cell is 6.9× beyond its reach |
| `N_S·a = 1.08×10⁸`, 36× the certificate gate | arithmetic | 108,038,636, exactly 36.0× `3×10⁶`; the pilot is `1.83×10⁸` |
| `n_χ` is 8.6× under `2²¹` | arithmetic | 8.58× — `matmul_mod`'s guard is nowhere near |
| entry bound `\|Stab\|·δ·(n+1) = 4,800`, `L = \|exps(4,6)\| = 126` | arithmetic | 4,800 and `C(9,5) = 126`; the build's measured max entry is 16 |
| the build's own internal arithmetic | per-phase rows and nonzeros from `b14_12_build.log` | rows `602,685 + 4×3,969,507 = 16,480,713` and nnz `3,400,880 + 4×13,173,286 = 56,094,024`, both matching the totals; phase seconds sum to 2,838.2 |
| the five Q2 figures | recomputed over `s79_queue2.json` | 10,513 cells, **9,952 open**, median `N_S·δ` `2.44×10⁹`, **7,386** above `2×10⁸`, **2,643** at or below this cell, `cost_model` **161 CPU-hours** for those 2,643 — all five exact once computed over the open set, which is what the row says |
| the pre-registration scorecard is faithful | E1–E7 in `PREREG_b14_12.md` against §8 | all seven present with the stated probabilities and the stated reasoning, including the 0.65 on the one MISS |
| the tree defect | read `wk13_b10_lean.py` lines 358–361 and 501, and the delivered `build_attempt1.log` | confirmed: `scratch = scratch or tempfile.mkdtemp(...)` then `shutil.rmtree(scratch)`, and the log ends `FileNotFoundError: '/root/b14_12_scratch/b14_12_E.npz'` |

The join is banked as `results/integrate/s79_q1_complete.json`, produced by
`analysis/integrate/b14_12_q1_join.py`; `--mutate` drops one cell's `i_det` and the
join refuses, so it is a check that can fail.

## 2. I rebuilt the cell

The rank is the one claim no amount of arithmetic on the delivered record can
settle, so I rebuilt the whole cell here — a second cloud container, and
**`fo='copy'` instead of the delivered `fo='inplace'`**. That deviation is the one
that could have silently corrupted a 27-million-monomial build, and B14-12's
Control F tested it only on the 3,672-monomial A1 cell.

Everything comes back identical:

| | this rebuild (`fo='copy'`) | delivered (`fo='inplace'`) |
|---|---|---|
| `N_S` / `\|Stab\|` / `n_χ` | 27,009,659 / 120 / 244,454 | identical |
| rows / nnz / nfixed | 16,480,713 / 56,094,024 / 0 | identical |
| per-operator rows, nonzeros, triples, obstructed | all five operators | identical |
| cover, `\|U\|`, excess, certified floor | 244,444 / 10 / 6 / 244,444 | identical |
| nullity, verified on full `E`, `rank_tall` | 4 / yes / 4 at both primes | identical |
| **`mult_det`, `i_det`** | **4, 0 at both primes** | identical |
| Control N | diagonal rank 0 all-zero, generic `det₄` rank 4 | identical |
| build wall | 4,396.5 s | 2,838.1 s — this host is 1.55× slower |
| build peak / whole cell | 1.489 GB / 2.54 GB | 1.483 / 2.225 — `copy` keeps a copy |

Record: `results/integrate/b14_12_integrator_reproduction.json`, log
`results/logs/b14_12_integrator_fo_copy.log`. So `i_det = 0` at
`(12,4,4,4,4,4)₈` is not one run's word, and the `fo='inplace'` deviation is now
checked at the cell that matters rather than only at a small one.

## 3. The inference structure, which is the part that could have gone wrong

This slot reads ranks in both directions in one report, and it gets the asymmetry
right everywhere:

- `mult_det = 4 = a` is a **full** modular rank. `rank_p ≤ rank_ℚ` and
  `rank_ℚ ≤ a = 4` together force `rank_ℚ = 4`, so one prime proves it and both
  agree. **PROVED** is the correct label. Same for `mult_per4`.
- `mult_pad = mult_red = 1` is a **deficient** modular rank. It gives
  `mult_pad ≥ 1`, hence `i_pad ≤ 3` — a **ceiling**. The report says so in four
  places and never reads it downward, and the families JSON carries
  "a CEILING on i, never read downward" on each such side.
- so `D ∈ [-3, 0]` with both ends proved, measured value `-3`. Correct.
- and the nullity is not a free parameter: the kernel of the simple raising
  operators on the `λ`-weight space **is** the highest-weight space, of dimension
  exactly `a`. So `nullity = 4` at both primes, with `a = 4` computed three ways
  and never read from the build, is itself a check on a 27-million-monomial
  assembly that could have failed — a mis-assembled `E` would not land on exactly
  `a`. `nullity_p ≥ nullity_ℚ = a` always, so equality also says no extra kernel
  appears at either prime. The cover's 244,444 columns bound the nullity above by
  10 independently, at `O(nnz)`, and the four vectors were verified on the full
  `E` rather than on the projected system.
- Control N's forced zero rests on the repaired support lemma, not the withdrawn
  one: a diagonal pencil's `det₄` is a product of four linear forms, so the point
  has essential span `≤ 4 < 6 = ℓ(λ)`, and the **whole λ-isotypic component**
  vanishes there. That is the form B14-11 supplied a proof for at this batch's
  intake, and the kernel vectors here are highest-weight vectors, so it applies.
  The generic `det₄` column beside it reading 4 is what keeps the control from
  being one that cannot fail.

## 4. Defects in the delivery

**D1. `i_pad` and `i_red` are shipped as bare integers at top level.**
`results/b14_12/b14_12_families.json` carries `"i_pad": 3` and `"i_red": 3`
alongside the correct `sides.*.status` caution. A consumer joining on the bare
field reads a ceiling as a value — the exact shape of `nchi_lb_field_is_false`
from batch 13, and of the `nchi_est` defect this very slot reports one section
earlier. The report's prose is careful; the machine-readable record is not. The
fields want an `_ub` suffix or a `values_are` line, and the batch-15 schema should
require it.

**D2. Its own `s79_schema_rows.jsonl` would carry that ceiling into the record if
merged.** B14-12 correctly declines to append the two rows to
`results/s79_cells.jsonl` and calls it an integration decision. **Declined here
too, and for a sharper reason than the null fields:** those rows carry `i_pad: 3`
and `i_red: 3`, so merging them would put a ceiling into the field every
downstream join reads as a value. `s79_cells.jsonl` stays session 79's delivery,
pinned by other sessions' verification; the completion is recorded in
`results/integrate/s79_q1_complete.json` and in `PROVED.md` instead, where the
join is replayable and the ceiling is labelled.

**D3. No `.pid` files in the delivery.** The standing rule is that each run records
its own process id to `results/logs/<run>.pid`, and §7.3 says the scripts were
fixed to do exactly that. The `.log` files shipped and the `.pid` files did not;
the ids survive only inside the JSON records (`3977`, `4136`, `2694`). Every other
slot in this batch shipped them. Nothing is unverifiable as a result — it is the
convention, not the discipline, that slipped.

**D4. Two rate figures are quoted on different bases.** §4.3 puts this cell's lean
rate at 0.686 GB per `10⁸` (from the raw peak, 1.483 GB) against "its pilot rate
of 1.30" (from the pilot's *above-baseline* peak, 1.904 GB; the pilot's raw peak
gives 1.338). Consistently raw it is 0.686 against 1.338; consistently
above-baseline, 0.658 against 1.298. The ratio is ~0.51 either way, so "half" holds
and the conclusion is untouched — but a section whose whole subject is a number
quoted loosely should not mix measures.

**D5. "5.1 % low" and "8.6 % low" are measured against the estimate, not the
truth.** `(1,606,104 − 1,528,114)/1,528,114 = 5.10 %`; against the measured value
it is 4.85 %. Same for 8.61 % versus 7.92 %. The convention is fixed in the
pre-registration before measurement and used consistently, so this is a reading
note rather than an error — but "the quotient is 5.1 % low" naturally parses the
other way.

## 5. Defects in my own material, and the one I fixed

**The tree defect is real and I have fixed it.** `wk13_b10_lean.raising_rows_lean`
took `scratch` from the caller when given, then ended a `blocks='disk'` run with
`shutil.rmtree(scratch, ignore_errors=True)` — removing the caller's directory and
everything else in it. B13-10 never met it because its own runs passed
`scratch=None` and took the `mkdtemp` branch the builder does own. B14-12 lost a
completed 47-minute build to it and reported it without patching, which was the
right call for a worker and leaves it for me.

Fixed: the function now removes the block files it wrote, and removes the
directory only when it created the directory. `tools/verify/scratch_not_removed.py`
tests all four properties — the caller's directory survives, the caller's own file
in it is untouched, the builder's `block_*.npz` are gone, and `scratch=None` still
cleans up its own temporary directory — and `--show-old` applies the old line to a
copy of the module and shows the test failing, so it is a check that can fail.
Any batch-15 session taking B13-10 §3's advice to use `blocks='disk'` with its own
scratch directory would have hit this; now it will not.

**The board mispriced this slot, in the direction that mattered.** Three of the
four numbers it handed the slot were wrong: ≈20 minutes against 47.3 measured
(2.4× low, and drawn from the `N_S·δ`-only model that `cost_model` says not to
quote), ≈2.8 GB against 1.483, and "budget for the kernel, not the builder" when
the builder took 95 % of the wall clock and the kernel ran in ten seconds. The
sizing that produced "`|Stab| = 120` compresses `n_χ` sevenfold" came from
`ceil(N_S/|Stab|)`, the quotient `nchi_2_21_guard` forbids — and every one of the
123 queue entries carries that quotient in a field named `nchi_est` with nothing
saying what the estimator is. The conclusion drawn from it happened to be right;
the number was not, and the error direction under-provisions. `stab_trade` in
`PROVED.md` now states the trade in both directions so the next board does not
have to rediscover it.

**`build_no_longer_binding` was cited to this slot as an input and was an
extrapolation.** It is now a measured point above `1.47×10⁸`, and it shows the
extrapolation's *shape* is wrong, not just its constant: the peak is not a function
of `N_S·δ` alone. So B13-10's `2.8×10⁸` ceiling should not be carried, and neither
should the `1.0×10⁹` the same arithmetic now produces — B14-12 says exactly that
and declines to adopt its own more favourable number, which is the right instinct.

## 6. What is now open

Q1 is closed. Q2 is where the six-row frontier goes next and it is an order of
magnitude larger: **9,952 cells still open**, median `N_S·δ` `2.44×10⁹`, 7,386 of
them above session 79's own `2×10⁸` build wall, and 2,643 at or below this cell's
size — those 2,643 priced by `cost_model` at ≈161 CPU-hours, which on a one-build
box is ≈161 wall-hours. Before spending that, one cell at `|Stab| = 1` or 2 near
`10⁸` would separate the two terms of the cost model and give the ceiling a shape
in `(N_S·δ, |Stab|)` rather than in `N_S·δ` alone. That is about an hour and it
should come first.

`i_pad ≥ 1` and `i_red ≥ 1` at this weight are NOT REACHED and are not reachable
by evaluation — the drop to 1 is a ceiling. They need Lemma CI, which is where
B14-01 through B14-03 already are. And this cell joins B13-10's pilot as a result
this tree can **prove and cannot certify**: `N_S·a = 1.08×10⁸` against
`certificate_ceiling`'s `3×10⁶`. Two concrete targets now exist for compact
certificates, which is worth more to that work than an argument about formats.

## 7. Batch-15 items added by this slot

1. Ceiling-valued fields must be named as ceilings or carry `values_are`
   (D1, D2) — and no estimator may ship in a field named `est` without naming
   itself (the `nchi_est` defect, which cost two documents a wrong inference).
2. A packet must not quote the `N_S·δ`-only cost model, and must name what binds
   on the cell at hand rather than what bound on the last one (D4 of §5).
3. The packet's bundle command must be the board's form,
   `git bundle create <file> <base>..<branch> <branch>` — B14-12 is the seventh
   session to report the `..HEAD` form, which `check_delivery.py` already rejects.
4. The dispatch message carrying the expected commit and tree did not arrive for
   this slot either — the eleventh report of it. Put the values in the tag
   annotation, as recorded at B14-07.
