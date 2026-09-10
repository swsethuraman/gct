# Pre-registration — B13-08, the moderate degree-10 cubic remainder

board_numbering: batch13.  Session B13-08 (Fable).  Model that is actually
running this session: Claude Fable 5.1 (`claude-fable-5-1`).

Base: `main` = `00495110c62acfbbbc951e82cc218ed091563b3f` at clone time
(2026-09-09 14:48 UTC); branch `b13_08`.  The tree carries
`docs/batch13_board.md`, `docs/batch13_corrections.md`,
`docs/stocktake_batch12.md` and `docs/batch13_worker_preamble.md` (all four
checked present before anything else).  Committed before any measurement.

Labels used throughout: **PROVED** (a theorem in the tree, cited, or a full
rank mod one house prime), **CERTIFIED** (a `full_rank` certificate written and
replayable), **MEASURED** (computed here, both house primes unless stated),
**ADOPTED** (taken from the record without re-derivation), **RECORDED** (a
mod-`p` kernel or a cost, not a characteristic-zero statement),
**EXPECTATION** (a prior).  Anything not written here is exploratory when it
appears in the report.

## Preflight

| item | state at clone | action |
|---|---|---|
| host | 2 CPUs, 8 023 MB RAM, no swap, ~30 GB free disk (a shared cloud container; the twelve batch-13 sessions do not share this box's memory with each other but this session has only this one budget) | recorded |
| `python3` | 3.11.15 | — |
| `numpy`, `scipy` | 2.4.4, 1.17.1, present | — |
| `python-flint` | **missing** | `pip install python-flint` → 0.9.0 |
| `sympy` | **missing** | `pip install sympy` → 1.14.0 (with mpmath 1.3.0) |
| `gcc` | 13.3.0, present | `analysis/wk11_s71_schur.c` compiled by the engine itself to `S71_SCHUR_SO=/home/claude/b13_08/schur.so` |
| `Singular`, `msolve` | absent | not needed by this assignment |
| `S71_MEM_X` | unset (engine default 1.0e9) | set to `2.5e8` for every run, the value session 79's report §5.3 says to use |

## 1. The question

Is `I(D_6^{per_3})_{10}` — the degree-10 part of the ideal of
`D_6^{per_3} = closure{ per_3(Σ_{i≤6} s_i A_i) } ⊂ Sym^3 C^6` — zero in the
isotypic component of each of the **95 length-6 weights `μ ⊢ 30` with
`a(μ,10) ≥ 1` and `N_S < 10^7` that session 79 priced and did not reach**?

Per weight the statement is: `mult_per3(μ, 10) = a(μ, 10)`, i.e. no nonzero
highest-weight vector of weight `μ` in `Sym^10(Sym^3 C^6)` vanishes on the
permanent family.  A full rank mod one house prime proves it over `Q`
(`rank_p ≤ rank_Q`, Lemma 2 of `docs/sparse_det_route.md`): **PROVED** per
weight, and `full_rank` certificates where the expanded basis fits the size
rule (CERTIFIED).

What the completed list does **not** give: `I(D_6^{per_3})_{10} = 0` as a
theorem.  That needs the eleven weights with `N_S ≥ 10^7` (batch 14's), and,
for the shorter weights of degree 10, the inherited exclusion
`docs/washout_lemma.md` Theorem 2 + Theorem 3(1) (length ≤ 5), which B13-07
audits.  This session serves objective 2 (permanent-specific equations,
`mult_pad < mult_red`, through Prop. 8 of `docs/transfer_lemma.md`); it says
nothing about objective 1 (`D > 0`), whose binding constraint is `i_det`
(`docs/batch13_corrections.md` §1).

## 2. The objects — frozen

`results/b13_08/queue.json`, written by `analysis/wk13_b08_queue.py` from
session 79's frozen queue `results/s79_per6_queue.json['10']` (402 weights in
`N_S` order) minus the 296 weights banked in `results/s79_per6.jsonl` at
`δ = 10`: 106 remaining, of which **95 with `N_S < 10^7`** (`Σa = 367`) are
this session's list, in the **recorded cost order** (session 79's `N_S`
ascending; `rank` = position in the 402-queue, 297 … 391), and 11 with
`N_S ≥ 10^7` (`Σa = 12`, ranks 392 … 402, from `(6,6,6,6,4,2)` at
`1.00·10^7` to `(5,5,5,5,5,5)` at `2.73·10^7`) are **deferred to batch 14**
and not run.  The 95 run from `(9,9,4,3,3,2)` (`a = 2`, `N_S = 1 706 497`)
to `(8,6,5,5,3,3)` (`a = 2`, `N_S = 9 412 742`); 69 have `N_S < 5·10^6` and
26 lie in `[5·10^6, 10^7)`, session 79's counts reproduced.  The full table
is appended in §8.

The plethysm values `a` are session 79's (ADOPTED from the queue); the engine
asserts each against its own Weyl alternation (`wk9_s42_census.a_weyl`) before
building, and against the hybrid's exact kernel dimension after.

## 3. The instrument — the current engine, unchanged

`analysis/wk12_s79_per6.py` exactly as in the tree, one weight per
subprocess, with `--a` from the queue, `--out` and `--certs`:

    build     wk9_s45_build.build_cell (n = 3, r = 6): weight-μ monomials, the χ_μ-isotypic
              reduction, the raising rows E_{i,i+1} in the convention of wk9_s60_cell.CONVENTIONS
    kernel    wk11_s71_hybrid.hybrid_kernel: initial-term cover + exact Schur residual on the
              uncovered columns, python-flint nullspace, every vector verified E·K = 0 on the
              full E, kernel dimension = a asserted, both house primes
    points    K = a + 8 pencils per_3(Σ s_i A_i), A_i random integer 3×3, entries in [−40, 40],
              seed 41 (session 41's family, the recorded seed); the re-check family, on a drop
              only, 3a + 24 pencils with seed 907; hybrid seed 20260908
    mult      rank_p(ev_per3 · K) with session 60's χ-coordinate evaluation rows
              (wk12_s79_cell6.ev_rows_from_coeffs), both primes 2147483647 and 2147483629
    exps      the build, the evaluation rows and the certificates all key coefficients by the
              exponent TUPLE (wk8_s30_core.exps, first exponent up from 0, through
              `co.get(alpha)` and `E.index`-free tuple lookups); no literal position is used
              anywhere in this session's code

Two conventions the engine already honours: a stored `kernel_chi` (when
`n_χ·a ≤ 400 000`) is in χ-coordinates mod `p` and says so in its key; the
`full_rank` certificates carry the points (`permanent_pencil`) and the basis
expanded over the monomial basis, no transform.  No transported certificate
is produced by this assignment (no `u`-scaling), so no `u`-values arise.

**Runs are bounded at launch.**  Each weight is launched as
`bash -c 'ulimit -v <kB>; exec timeout 7200 python3 analysis/wk12_s79_per6.py …'`
by `analysis/wk13_b08_sweep.py`, the process id written to
`results/logs/b13_08_w<rank>.pid` and the sweep's own id to
`results/logs/b13_08_sweep_lane<k>.pid`; a run that must end early is ended by
the recorded id only.  Logs under `results/logs/`, one per lane and one per
weight.  Two lanes may run concurrently (the host has two cores and the engine
pins one thread): lane 0 walks the list in cost order; lane 1 walks the same
list in cost order taking only weights whose predicted peak
(`pred_peak_gb` in the queue file, a rough model fitted on session 79's
records and used for scheduling only, never for a result) is `≤ 2.5 GB`, and
a weight starts only if the predicted peaks of the two running weights sum to
`≤ 6.3 GB`; per-process `ulimit -v` = 7.0 GB on lane 0 when it runs alone, and
the lanes' limits sum to `≤ 7.0 GB` when both run.  Each lane appends to its
own file (`results/b13_08/per6_d10_lane<k>.jsonl`, single writer); the merged
record `results/b13_08/per6_d10.jsonl` and `results/b13_08/status.json` are
written by the sweep's merge step.  A weight is claimed by a lock file before
it is launched, so no weight is run twice.

## 4. Controls — run before the list (the input-and-control checkpoint)

1. `analysis/wk12_s79_per6_control.py` unchanged: `per_form(3)` equals a hand
   permanent; the `per_3` coefficient dicts differ from the `det_3`
   restriction at all ten recorded points; the two `a = 2` degree-8 weights
   `(11,4,4,2,2,1)`, `(10,6,4,2,1,1)` reproduce `mult = a = 2`.  **Must pass.**
2. Reproduction of two banked degree-10 records at the frontier of session
   79's scan, with the recorded seeds: `(11,6,5,3,3,2)` (`a = 5`,
   `N_S = 1 698 457`, the last weight session 79 banked) and `(9,8,5,4,3,1)`
   (`a = 13`, `N_S = 1 448 828`, `|Stab| = 1`, the largest `n_χ` among the
   banked degree-10 weights).  `a`, `N_S`, `|Stab|`, `n_χ`, `nrows`, `nnz`,
   the cover size and order, `|U|`, `mult` at both primes **must equal the
   record**.  Their wall time and peak RSS calibrate this host against
   session 79's box.
3. **The instrument can fail (the negative control).**  On the two
   reproduction weights, the same kernel `K` is evaluated at `a + 8` points
   of two other families through the same evaluation rows:
   (i) *products of three linear forms* — pencils with every `A_i` diagonal,
   so `per_3(Σ s_i A_i) = (Σ s_i x_i)(Σ s_i y_i)(Σ s_i z_i)`.  Every `S_μ` with
   `ℓ(μ) = 6` has multiplicity zero in `(Sym^10 C^6)^{⊗3}` (three Pieri
   steps give at most three rows), so the coordinate ring of the Chow variety
   of triple products contains no length-6 weight and the evaluation rank
   **must be 0** at both primes.  (ii) `det_3` pencils — the same random
   matrices, the determinant instead of the permanent: recorded, `≤ a`, as a
   second family the rows distinguish.  If (i) does not give rank 0 the
   instrument is defective and nothing below is run.
4. The lean contingency driver of §6 (used only after a memory failure) is
   run on the same two reproduction weights and must return identical `mult`,
   `n_χ`, cover and `|U|`, and, where the record carries `kernel_chi`, the
   identical kernel matrix.

## 5. Stopping rules

- Per weight: `timeout 7200 s`; `ulimit -v` as above.  A weight that ends
  without a `RESULT` line is recorded as *not reached* with the reason
  (timeout / memory / no result, and the exit code) and the lane moves on;
  a memory failure gets **one** re-run on the lean driver (§6) after the list
  has been walked once; a second failure is final for this session and is
  priced in the report.
- The sweep stops taking new weights at **19:30 America/New_York** so the
  report and bundle are delivered by 20:30; anything running then is allowed
  to finish within its own timeout, and the not-reached suffix is stated by
  rank and priced by `N_S·δ`.
- Halt-and-protocol: a **drop** (`mult < a` at either prime) halts both lanes
  by their recorded ids after the weight's own re-check; §7 applies.
- Information-rate rule: none needed — every weight is a separate exact
  statement and the list is finite.

## 6. The lean contingency driver (pre-registered, not the primary instrument)

Session 79's records show the engine's peak RSS is a transient of the kernel
check `E @ K` (about 32 bytes per row of `E` per kernel column) and of the
evaluation-row product, on top of the build.  Sixteen of the 95 weights are
predicted above 4 GB on this 8 GB host.  `analysis/wk13_b08_per6_lean.py` is
`wk12_s79_per6.measure_weight` with exactly two memory-only changes, both
computing the identical numbers: the kernel check `E·K ≡ 0` evaluated in
row blocks of `E` (the same predicate), and the evaluation rows formed eight
points at a time (the pattern of `wk12_s79_cell6._prime_job`) with the same
points in the same order, so `G = ev·K` is the same matrix.  Same seeds, same
cover, same hybrid.  Its records carry `engine: "lean (b13_08)"` and the diff
against the engine is in the report.  It is used only for a weight the
unchanged engine could not finish for memory, and only after §4.4 passes.

## 7. What counts as what

- **Negative (the expected outcome, EXPECTATION 0.85 that all 95 reached are
  full):** `mult = a` at both primes → `S_μ ∉ I(D_6^{per_3})_{10}` over `Q`,
  PROVED per weight.  A completed list is *full-rank certificates for the
  completed list*; a partial list is *a completed, resumable prefix* stated by
  rank with the unreached weights priced by `N_S·δ`.
- **Candidate deficiency (EXPECTATION 0.10 somewhere in the 95):** `mult < a`
  at a prime.  The engine re-checks in the same call at `3a + 24` fresh
  points (seed 907), exhibits the kernel vector(s) in χ-coordinates, verifies
  `E·v = 0`, and writes the `ideal` file.  Then, pre-registered here, the
  investigation: (a) a third point family, seed 20260909, bound 200, `4a + 32`
  points, on the recorded vector — sampled vanishing persists or it does not;
  (b) the exact source check: the vector expanded over the monomial basis is
  evaluated on fresh integer pencils by an independent route
  (`wk8_s30_core.restrict` + `eval_row` on the expanded terms, no χ-machinery)
  mod both primes; (c) agreement of the nullity at both primes and the
  same behaviour under (a) and (b).  The deliverable is then *a reproducible
  candidate deficiency with explicit vectors*: **MEASURED / RECORDED**, a
  ceiling on the rank and a floor on the mod-`p` nullity, **never** a
  rational identity — nothing here is a membership statement over `Q`, and
  `i ≥ 1` is not claimed.  The verification protocol of the preamble then
  takes over (second prime, two point families, characteristic zero where a
  kernel is claimed, an independent source, the §5 degeneracy pre-check) and
  no negative decision-table branch is entered on it.
- **Primes disagree:** an instrument fault until explained; the weight is
  re-run once alone; reported as such.
- **Not reached:** memory or time, priced by `N_S·δ` under session 79's
  hybrid cost model (build `2.1·10⁻⁶ s · N_S·δ`, rows `2.7·10⁻⁸ s` per point
  per `N_S·δ`) and by this host's measured peak.

## 8. The 95 weights, frozen (rank = position in session 79's 402-queue)

| # | rank | `mu` | `a` | `N_S` | `|Stab|` | `N_S*delta` | pred. peak GB |
|---|---|---|---|---|---|---|---|
| 1 | 297 | `(9,9,4,3,3,2)` | 2 | 1706497 | 4 | 1.71e+07 | 2.06 |
| 2 | 298 | `(9,7,6,4,3,1)` | 13 | 1713081 | 1 | 1.71e+07 | 3.46 |
| 3 | 299 | `(8,8,7,3,2,2)` | 3 | 1737405 | 4 | 1.74e+07 | 2.07 |
| 4 | 300 | `(10,7,5,4,2,2)` | 15 | 1758298 | 2 | 1.76e+07 | 3.38 |
| 5 | 301 | `(8,8,6,4,3,1)` | 5 | 1824112 | 2 | 1.82e+07 | 2.1 |
| 6 | 302 | `(10,6,5,4,4,1)` | 7 | 1845977 | 2 | 1.85e+07 | 2.11 |
| 7 | 303 | `(9,7,5,5,3,1)` | 8 | 1920626 | 2 | 1.92e+07 | 2.37 |
| 8 | 304 | `(10,6,6,4,2,2)` | 13 | 1929198 | 4 | 1.93e+07 | 2.61 |
| 9 | 305 | `(8,7,7,4,3,1)` | 4 | 1966669 | 2 | 1.97e+07 | 2.14 |
| 10 | 306 | `(9,8,5,4,2,2)` | 12 | 1972064 | 2 | 1.97e+07 | 3.19 |
| 11 | 307 | `(11,6,4,4,3,2)` | 9 | 1973175 | 2 | 1.97e+07 | 2.61 |
| 12 | 308 | `(8,8,5,5,3,1)` | 3 | 2045486 | 4 | 2.05e+07 | 2.16 |
| 13 | 309 | `(10,5,5,5,4,1)` | 2 | 2069786 | 6 | 2.07e+07 | 2.17 |
| 14 | 310 | `(9,6,6,5,3,1)` | 4 | 2108140 | 2 | 2.11e+07 | 2.18 |
| 15 | 311 | `(10,7,5,3,3,2)` | 8 | 2147468 | 2 | 2.15e+07 | 2.61 |
| 16 | 312 | `(10,6,5,5,2,2)` | 3 | 2162479 | 4 | 2.16e+07 | 2.2 |
| 17 | 313 | `(11,5,5,4,3,2)` | 5 | 2211400 | 2 | 2.21e+07 | 2.21 |
| 18 | 314 | `(9,7,5,4,4,1)` | 7 | 2233926 | 2 | 2.23e+07 | 2.49 |
| 19 | 315 | `(9,7,6,4,2,2)` | 12 | 2333773 | 2 | 2.33e+07 | 3.72 |
| 20 | 316 | `(10,6,6,3,3,2)` | 2 | 2357000 | 4 | 2.36e+07 | 2.26 |
| 21 | 317 | `(8,8,5,4,4,1)` | 4 | 2379720 | 4 | 2.38e+07 | 2.26 |
| 22 | 318 | `(9,8,5,3,3,2)` | 5 | 2410145 | 2 | 2.41e+07 | 2.27 |
| 23 | 319 | `(8,7,6,5,3,1)` | 5 | 2422004 | 1 | 2.42e+07 | 2.47 |
| 24 | 320 | `(9,6,6,4,4,1)` | 6 | 2452773 | 4 | 2.45e+07 | 2.29 |
| 25 | 321 | `(8,8,6,4,2,2)` | 8 | 2486029 | 4 | 2.49e+07 | 2.42 |
| 26 | 322 | `(10,7,4,4,3,2)` | 10 | 2497176 | 2 | 2.50e+07 | 3.47 |
| 27 | 323 | `(11,5,4,4,4,2)` | 4 | 2571001 | 6 | 2.57e+07 | 2.32 |
| 28 | 324 | `(7,7,7,5,3,1)` | 1 | 2612751 | 6 | 2.61e+07 | 2.33 |
| 29 | 325 | `(9,7,5,5,2,2)` | 4 | 2617854 | 4 | 2.62e+07 | 2.34 |
| 30 | 326 | `(8,6,6,6,3,1)` | 1 | 2659758 | 6 | 2.66e+07 | 2.35 |
| 31 | 327 | `(8,7,7,4,2,2)` | 2 | 2681277 | 4 | 2.68e+07 | 2.35 |
| 32 | 328 | `(11,5,5,3,3,3)` | 2 | 2703004 | 12 | 2.70e+07 | 2.36 |
| 33 | 329 | `(9,6,5,5,4,1)` | 3 | 2752707 | 2 | 2.75e+07 | 2.38 |
| 34 | 330 | `(8,8,5,5,2,2)` | 2 | 2789125 | 8 | 2.79e+07 | 2.39 |
| 35 | 331 | `(9,8,4,4,3,2)` | 7 | 2803928 | 2 | 2.80e+07 | 3.04 |
| 36 | 332 | `(8,7,6,4,4,1)` | 4 | 2819270 | 2 | 2.82e+07 | 2.4 |
| 37 | 333 | `(9,7,6,3,3,2)` | 6 | 2854539 | 2 | 2.85e+07 | 2.82 |
| 38 | 334 | `(7,7,6,6,3,1)` | 1 | 2869624 | 4 | 2.87e+07 | 2.41 |
| 39 | 335 | `(9,6,6,5,2,2)` | 6 | 2874863 | 4 | 2.87e+07 | 2.41 |
| 40 | 336 | `(8,8,6,3,3,2)` | 1 | 3041630 | 4 | 3.04e+07 | 2.46 |
| 41 | 337 | `(7,7,7,4,4,1)` | 1 | 3042013 | 12 | 3.04e+07 | 2.46 |
| 42 | 338 | `(10,7,4,3,3,3)` | 1 | 3054521 | 6 | 3.05e+07 | 2.47 |
| 43 | 339 | `(10,6,5,4,3,2)` | 11 | 3076302 | 1 | 3.08e+07 | 5.25 |
| 44 | 340 | `(9,5,5,5,5,1)` | 1 | 3090597 | 24 | 3.09e+07 | 2.48 |
| 45 | 341 | `(11,5,4,4,3,3)` | 1 | 3143967 | 4 | 3.14e+07 | 2.49 |
| 46 | 342 | `(8,7,5,5,4,1)` | 3 | 3165424 | 2 | 3.17e+07 | 2.5 |
| 47 | 343 | `(8,7,7,3,3,2)` | 2 | 3282047 | 4 | 3.28e+07 | 2.53 |
| 48 | 344 | `(8,7,6,5,2,2)` | 4 | 3305381 | 2 | 3.31e+07 | 2.57 |
| 49 | 345 | `(10,5,5,5,3,2)` | 3 | 3453247 | 6 | 3.45e+07 | 2.59 |
| 50 | 346 | `(8,6,6,5,4,1)` | 2 | 3477991 | 2 | 3.48e+07 | 2.59 |
| 51 | 347 | `(10,6,4,4,4,2)` | 7 | 3581036 | 6 | 3.58e+07 | 3.44 |
| 52 | 348 | `(8,6,6,6,2,2)` | 3 | 3631655 | 12 | 3.63e+07 | 2.64 |
| 53 | 349 | `(11,4,4,4,4,3)` | 1 | 3658331 | 24 | 3.66e+07 | 2.65 |
| 54 | 350 | `(9,7,5,4,3,2)` | 12 | 3730858 | 1 | 3.73e+07 | 6.75 |
| 55 | 351 | `(7,7,6,5,4,1)` | 1 | 3754247 | 2 | 3.75e+07 | 2.68 |
| 56 | 352 | `(10,6,5,3,3,3)` | 1 | 3766613 | 6 | 3.77e+07 | 2.68 |
| 57 | 353 | `(8,8,5,4,3,2)` | 5 | 3977057 | 2 | 3.98e+07 | 3.42 |
| 58 | 354 | `(10,5,5,4,4,2)` | 2 | 4021114 | 4 | 4.02e+07 | 2.76 |
| 59 | 355 | `(9,6,6,4,3,2)` | 6 | 4099812 | 2 | 4.10e+07 | 3.92 |
| 60 | 356 | `(7,6,6,6,4,1)` | 1 | 4126276 | 6 | 4.13e+07 | 2.79 |
| 61 | 357 | `(7,7,5,5,5,1)` | 1 | 4218911 | 12 | 4.22e+07 | 2.82 |
| 62 | 358 | `(9,7,4,4,4,2)` | 5 | 4345969 | 6 | 4.35e+07 | 3.4 |
| 63 | 359 | `(10,6,4,4,3,3)` | 1 | 4386577 | 4 | 4.39e+07 | 2.87 |
| 64 | 360 | `(9,7,5,3,3,3)` | 2 | 4573023 | 6 | 4.57e+07 | 2.92 |
| 65 | 361 | `(9,6,5,5,3,2)` | 4 | 4606382 | 2 | 4.61e+07 | 3.47 |
| 66 | 362 | `(8,8,4,4,4,2)` | 3 | 4633877 | 12 | 4.63e+07 | 2.94 |
| 67 | 363 | `(8,7,6,4,3,2)` | 7 | 4719476 | 1 | 4.72e+07 | 5.65 |
| 68 | 364 | `(8,8,5,3,3,3)` | 1 | 4876249 | 12 | 4.88e+07 | 3.01 |
| 69 | 365 | `(10,5,5,4,3,3)` | 3 | 4928715 | 4 | 4.93e+07 | 3.03 |
| 70 | 366 | `(7,7,7,4,3,2)` | 1 | 5096493 | 6 | 5.10e+07 | 3.08 |
| 71 | 367 | `(8,7,5,5,3,2)` | 4 | 5304916 | 2 | 5.30e+07 | 3.95 |
| 72 | 368 | `(9,7,4,4,3,3)` | 2 | 5329441 | 4 | 5.33e+07 | 3.15 |
| 73 | 369 | `(9,6,5,4,4,2)` | 6 | 5369144 | 2 | 5.37e+07 | 5.03 |
| 74 | 370 | `(10,5,4,4,4,3)` | 1 | 5744084 | 6 | 5.74e+07 | 3.27 |
| 75 | 371 | `(8,6,6,5,3,2)` | 2 | 5833614 | 2 | 5.83e+07 | 3.3 |
| 76 | 372 | `(9,5,5,5,4,2)` | 1 | 6036880 | 6 | 6.04e+07 | 3.36 |
| 77 | 373 | `(8,7,5,4,4,2)` | 4 | 6186200 | 2 | 6.19e+07 | 4.56 |
| 78 | 374 | `(7,7,7,3,3,3)` | 1 | 6256335 | 36 | 6.26e+07 | 3.43 |
| 79 | 375 | `(7,7,6,5,3,2)` | 2 | 6302047 | 2 | 6.30e+07 | 3.44 |
| 80 | 376 | `(9,6,5,4,3,3)` | 3 | 6590439 | 2 | 6.59e+07 | 4.19 |
| 81 | 377 | `(10,4,4,4,4,4)` | 1 | 6696948 | 120 | 6.70e+07 | 3.56 |
| 82 | 378 | `(8,6,6,4,4,2)` | 5 | 6804680 | 4 | 6.80e+07 | 4.69 |
| 83 | 379 | `(7,6,6,6,3,2)` | 1 | 6932301 | 6 | 6.93e+07 | 3.63 |
| 84 | 380 | `(7,7,6,4,4,2)` | 1 | 7352720 | 4 | 7.35e+07 | 3.76 |
| 85 | 381 | `(9,5,5,5,3,3)` | 3 | 7414387 | 12 | 7.41e+07 | 3.77 |
| 86 | 382 | `(8,7,5,4,3,3)` | 3 | 7598805 | 2 | 7.60e+07 | 4.79 |
| 87 | 383 | `(8,6,5,5,4,2)` | 2 | 7655836 | 2 | 7.66e+07 | 4.08 |
| 88 | 384 | `(9,6,4,4,4,3)` | 2 | 7688193 | 6 | 7.69e+07 | 3.88 |
| 89 | 385 | `(7,7,5,5,4,2)` | 1 | 8274441 | 4 | 8.27e+07 | 4.03 |
| 90 | 386 | `(8,5,5,5,5,2)` | 1 | 8616678 | 24 | 8.62e+07 | 4.14 |
| 91 | 387 | `(9,5,5,4,4,3)` | 1 | 8652131 | 4 | 8.65e+07 | 4.15 |
| 92 | 388 | `(8,7,4,4,4,3)` | 1 | 8868581 | 6 | 8.87e+07 | 4.21 |
| 93 | 389 | `(7,7,6,4,3,3)` | 1 | 9038623 | 4 | 9.04e+07 | 4.26 |
| 94 | 390 | `(7,6,6,5,4,2)` | 1 | 9106420 | 2 | 9.11e+07 | 4.34 |
| 95 | 391 | `(8,6,5,5,3,3)` | 2 | 9412742 | 4 | 9.41e+07 | 4.43 |

(`pred. peak GB` is the scheduling model of §3, not a result.)

Deferred to batch 14, not run (`N_S ≥ 10^7`): ranks 392–402,
`(6,6,6,6,4,2)`, `(7,7,5,5,3,3)`, `(8,6,5,4,4,3)`, `(7,7,5,4,4,3)`,
`(8,5,5,5,4,3)`, `(8,6,4,4,4,4)`, `(7,6,6,4,4,3)`, `(7,6,5,5,4,3)`,
`(7,5,5,5,5,3)`, `(6,6,6,4,4,4)`, `(5,5,5,5,5,5)`; `a = 2` at
`(8,6,5,4,4,3)` and 1 at the others, `N_S` from `1.00·10^7` to `2.73·10^7`.

Author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
board_numbering: batch13

---

## Addendum A — 2026-09-10, recalibrated scheduling; committed before the measurements it governs

Two changes, both to **scheduling only**.  `results/b13_08/queue.json` stays
frozen: the list, its order, the seeds, the primes, the stopping rules and the
drop protocol of §§2–7 are unchanged, and no result depends on anything here.

**A.1  The peak-memory estimate is recalibrated on this session's own
measurements.**  The `pred_peak_gb` of §3 was an a-priori model fitted by eye on
session 79's records; on this box it is wrong by up to 2.0 GB, in both
directions.  Least squares on the 22 weights measured here plus the two control
weights, all on the unchanged engine at `S71_MEM_X = 2.5·10⁸`:

    peak_GB  =  0.986  +  0.0277·(nnz/10⁶)  +  0.1057·(n_χ·min(a,16)/10⁶)

max residual **0.36 GB**, mean 0.09 GB.  The three terms are the interpreter
plus build transients, `E` held as CSR with the hybrid's working copy (~28 bytes
per nonzero), and the kernel `K` with its `int64` image and the 16-column blocks
of the kernel check.  For an unrun weight `nnz` and `n_χ` are estimated from
`N_S` and `|Stab|` by ratios measured over session 79's 506 cubic-scan records
and this session's 22, taken at **p90** so the estimate errs high.
`analysis/wk13_b08_schedule.py` writes `results/b13_08/schedule.json`; the sweep
reads it with `--sched`.  It predicts 10 of the 95 above 4 GB and 3 above 5 GB,
where the frozen model said 16 above 4 GB.

**A.2  A weight whose own estimate exceeds the concurrency cap runs solo rather
than never.**  The §3 rule ("a weight starts only if the predicted peaks of the
two running weights sum to `≤ 6.3 GB`") makes any weight predicted above the cap
unrunnable even on an idle box — a defect in my own pre-registration, found when
the recalibration put one weight at 7.19 GB.  The rule now reads: **wait while
another lane is running and the two together exceed the cap; then run, bounded
by the weight's own `ulimit -v`.**  Concurrency is still capped; solvability no
longer depends on the cap.

**A.3  The wall-clock stop of §5 moves from 19:30 to 22:20 America/New_York.**
The container was suspended 15:51–00:39 UTC, 8¾ hours, which consumed the
delivery window the 19:30 stop existed to protect; the deadline was extended by
two hours and the stop moves with it.  Lane parameters for the remainder:
lane 0 `--sched --sum-cap 6.8 --ulimit-kb 7000000`, lane 1 `--sched --max-pred
2.7 --sum-cap 6.8 --ulimit-kb 3000000`.

Nothing above changes what counts as a negative, a candidate deficiency, or
not-reached.
