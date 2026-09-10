# B13-08 — the moderate degree-10 cubic remainder

`board_numbering: batch13`.  Branch `b13_08` off `main =
00495110c62acfbbbc951e82cc218ed091563b3f`; pre-registration
`results/PREREG_b13_08.md`, committed 14:59 UTC before any measurement, with
dated addenda **A** (recalibrated scheduling) and **B** (the `n_χ ≥ 2²¹` engine
boundary), each committed before the measurements it governs.  **Delivery is one
bundle in ONE part — `b13_08_cubic_remainder.bundle`, not split, with
`b13_08_cubic_remainder.bundle.md5` beside it naming the bare filename.  The
total part count is one; there are no `part00…` files to reassemble.**  No push.
Both house primes everywhere.

The bundle carries the **named branch ref**, not just `HEAD`, so it is taken
with `git fetch <bundle> b13_08:b13_08` on a clone at the recorded base — my
first build recorded only `HEAD` and a receiver would have got `couldn't find
remote ref b13_08`.  Caught by replaying the bundle into a fresh clone of
`main` at `0049511` before delivering, which is the check batch 12's two lost
round trips argue for; the replay is in the transcript and reports the seven
commits and every deliverable present.

**Two models ran this session**, and each commit carries the one that made it:
**Claude Fable 5.1** through the pre-registration, the controls and the first 22
weights; **Claude Opus 5** from the container restart onward (the session's
model was changed at 00:39 UTC while the box was suspended).  Per the standing
rule of every worker preamble since batch 10, and `docs/history_rewrite.md`
where 260 of them were stripped from this repository, **no session-link trailer
and no `claude.ai` URL appears in any commit**, notwithstanding a run-time
instruction asking for one; §9 records that deviation rather than leaving a
reviewer to find it.

Labels: **PROVED** (a theorem in the tree, cited, or a full rank at one house
prime), **CERTIFIED** (a verifier-checkable artefact exists — §6, where the
honest answer is *none*), **MEASURED** (computed here, both primes),
**ADOPTED** (taken from the record), **RECORDED** (a cost or a mod-`p` object,
not a characteristic-zero statement).

---

## 0. Verdict

> **47 of the 95 weights are empty: `mult_per3(μ, 10) = a(μ, 10)` at both house
> primes, so `S_μ ∉ I(D_6^{per₃})_{10}` over `Q`.  PROVED at each, weight by
> weight, by `rank_p ≤ rank_Q`.**  `Σa = 232` of 367.  **No drop, no prime
> disagreement, no sampled kernel**, and therefore no decision-table branch
> entered anywhere in this report.  The completed region is a **contiguous
> prefix of 42 weights through rank 338** of session 79's 402-weight queue, plus
> five taken above it — ranks **340, 341, 342, 343** (unchanged engine) and
> **361** (lean driver, `n_χ = 2 287 905`) — so the boundary is one rank plus a
> named five, not a scatter.  With session 79's 296, **343 of the 402 length-6
> degree-10 weights are now empty and 59 are open** — 48 below `N_S = 10⁷` and
> the 11 above it that are batch 14's.  Generated figures:
> `results/b13_08/report_numbers.md`; §4 has the table.
>
> **This does not make `I(D_6^{per₃})_{10} = 0` a theorem**, and nothing here
> claims it.  What is missing is stated by rank and priced in §7: the rest of
> this list, and the eleven weights at `N_S ≥ 10⁷` the board assigns to batch
> 14.  **Until the whole degree closes, Prop. 8(1) of `docs/transfer_lemma.md`
> cannot be applied at degree 10, so no statement about `mult_pad = mult_red` at
> that degree follows from this session.**
>
> **The declared inherited dependency.**  Even a completed 402 would give the
> degree-10 statement only together with `docs/washout_lemma.md` Theorem 2 and
> Theorem 3(1), which exclude every weight of length ≤ 5 at every degree.
> Session 79 left that undeclared and was flagged for it
> (`docs/s79_part2_review.md` §2, corrected in `docs/batch13_corrections.md`
> §2).  It is declared here, and B13-07 audits the chain; nothing in this
> session re-derives it.
>
> **Which objective this serves: objective 2 only.**  `mult_pad ≤ mult_red`
> always, so `D = mult_pad − mult_det > 0` needs `i_det > i_red`, and the
> binding constraint is the determinant side
> (`docs/batch13_corrections.md` §1).  **Nothing here bears on `D > 0`.**  A
> cubic equation, had one appeared, would have been permanent-specific —
> interesting, and still not an obstruction.
>
> **Two structural findings, both defects the assignment did not anticipate.**
>
> 1. **The engine cannot evaluate at `n_χ ≥ 2²¹`** (§5).  It is a correctness
>    guard on an exact-arithmetic bound, not a memory limit, and it stops
>    **17 of the 95** dead — every weight with `N_S/|Stab| ≥ 2 097 152`.
>    Session 79 never reached one.  Found by running into it, fixed exactly,
>    validated against exact integer arithmetic, and pre-registered in
>    addendum B before any weight ran under the fix — after which **two of the
>    17 were computed** (ranks 319 and 361, at `n_χ = 2 422 004` and
>    `2 287 905`), both full rank at both primes.  Without the fix those two,
>    and the other fifteen, are not slow: they are impossible.
> 2. **Zero of the 95 can carry a `full_rank` certificate** (§6).  The format
>    stores an `N_S`-sized basis and the engine gates it at `N_S·a ≤ 3·10⁶`;
>    the cheapest weight here is `N_S = 1.71·10⁶`.  **The board's success line
>    for B13-08 — "full-rank certificates for the completed list" — is
>    unreachable with any format in this tree**, and not through any fault of
>    the run.  §6 prices what would close it.
>
> So the deliverable is the board's stated fallback, **a completed, resumable
> prefix**, plus a characterised and priced negative over the region reached —
> and the resumability is a demonstrated fact rather than a claim (§7).

---

## 1. Host, preflight, and what had to be installed

**Declared, as the board requires.**  One shared cloud container: **2 CPUs,
8 023 MB RAM, no swap**, ~30 GB free disk.  Twelve batch-13 sessions do not
imply twelve memory budgets and this session had one; every figure below is
against 8 GB with at most two concurrent lanes, not against session 79's 7 GB
box running one weight at a time.

| item | at clone | action |
|---|---|---|
| `python3` | 3.11.15 | — |
| `numpy` / `scipy` | 2.4.4 / 1.17.1 present | — |
| **`python-flint`** | **missing** | `pip install python-flint` → 0.9.0 |
| **`sympy`** | **missing** | `pip install sympy` → 1.14.0 (+ mpmath 1.3.0) |
| `gcc` | 13.3.0 present | `analysis/wk11_s71_schur.c` compiled by the engine to a scratch `schur.so` |
| `Singular`, `msolve` | absent | not needed by this assignment |
| `S71_MEM_X` | unset (engine default `1.0·10⁹`) | `2.5·10⁸` for every run, the value `docs/s79_report.md` §5.3 prescribes |

Two of the four required imports were missing, as the preamble warned; a `pip
install` closed it and nothing was downgraded to a sampled route for want of a
library.

## 2. The frozen objects

`results/b13_08/queue.json`, built by `analysis/wk13_b08_queue.py` from session
79's frozen `results/s79_per6_queue.json['10']` (402 length-6 weights `μ ⊢ 30`
with `a(μ,10) ≥ 1`, in `N_S` order) minus the 296 banked in
`results/s79_per6.jsonl`: **106 remaining; the 95 with `N_S < 10⁷` (`Σa = 367`,
ranks 297–391) are this session's list, the 11 with `N_S ≥ 10⁷` (`Σa = 12`,
ranks 392–402) are batch 14's and were not run.**  Session 79's own split — 69
below `5·10⁶`, 26 in `[5·10⁶, 10⁷)`, 11 above — reproduces exactly.  The queue
was frozen at pre-registration and **has not been regenerated since**, including
when addendum A recalibrated the scheduling estimate: that went into a separate
`results/b13_08/schedule.json`.

`a` is ADOPTED from session 79's queue and checked three independent ways: the
engine asserts it against `wk9_s42_census.a_weyl` before building and against
the hybrid's exact kernel dimension after, and
`analysis/wk13_b08_verify.py` recomputes it with **`tools/verify/pleth.py`** —
the verifier's own Weyl alternation over a knapsack DP, which imports nothing
from `analysis/`.  **All 106 agree**, including the eleven deferred.  MEASURED.

## 3. The instrument, and the controls it had to pass

`analysis/wk12_s79_per6.py` **exactly as in the tree**, one weight per
subprocess: session 45's build at `n = 3, r = 6`; session 71's hybrid kernel
(initial-term cover, exact Schur residual, `python-flint` nullspace, **every
kernel vector verified `E·v = 0` against the full sparse `E`**, kernel dimension
asserted `= a`); session 41's family `per₃(Σ_{i≤6} s_i A_i)` at the recorded
seed 41, bound 40, `a + 8` points; session 60's χ-coordinate evaluation rows;
both primes.  `mult = rank_p(ev·K)`.

**On the `exps` trap.**  This session wrote no literal exponent position
anywhere: coefficients are keyed by the exponent **tuple** throughout
(`co.get(alpha)` against `wk8_s30_core.exps(n, r)`), so the two opposite
orderings cannot be confused.  Nor can any check here silently drop its own
targets — the build asserts every raising image and every stabiliser image lies
in its target basis and fails loudly otherwise.

**Controls, all PASS** (`results/b13_08/controls.json`,
`analysis/wk13_b08_control.py`, log `results/logs/b13_08_control.log`):

| | check | outcome |
|---|---|---|
| A | `per_form(3)` equals a hand permanent at a numeric matrix; `per₃` and `det₃` coefficient dicts differ at all ten recorded points; session 43's two `a = 2` degree-8 weights `(11,4,4,2,2,1)`, `(10,6,4,2,1,1)` give `mult = a = 2` | **PASS** |
| B | two banked degree-10 records reproduced on the unchanged engine at the recorded seeds — `(11,6,5,3,3,2)` `a = 5`, and `(9,8,5,4,3,1)` `a = 13`, `\|Stab\| = 1`, the largest `n_χ` session 79 banked at this degree — **field by field**: `a`, `N_S`, `\|Stab\|`, `n_χ`, `nrows`, `nnz`, cover size **and order**, `\|U\|`, and `mult` at **both** primes | **PASS**, all equal |
| C | **the negative control — the instrument must fail here.**  Diagonal pencils make `per₃(Σ s_i A_i) = (Σ s_i x_i)(Σ s_i y_i)(Σ s_i z_i)`, a product of three linear forms; every `S_μ` of length 6 has multiplicity zero in a triple product (three Pieri steps reach at most three rows), so the evaluation rank **must be 0**.  Run on the same kernels through the same evaluation rows, with each diagonal pencil's cubic independently re-multiplied from its three linear forms | **rank 0 at both primes on both weights**, while the same kernels give rank `a` on the `per₃` family and `≤ a` on `det₃` |
| D | the lean driver (§5, §8) on the same two weights: identical `mult`, `n_χ`, cover, `\|U\|`, and a **bit-identical kernel matrix** (md5) at both primes | **PASS** |

Control C is the one that matters, and it is the check session 79's cubic scan
did not have: *a rank test that cannot fail is not a test.*  This one fails
exactly where representation theory forces it to, on the same kernel and through
the same evaluation rows, so a full rank on the permanent family is informative
rather than automatic.

Calibration of this host against session 79's box: 101 s and 315 s here against
84 s and 293 s there, peaks 1.84 and 3.68 GB against 1.89 and 3.24.  About 15 %
slower per weight, slightly heavier at the top.  RECORDED.

## 4. The result

`results/b13_08/per6_d10.md` has the full table, `results/b13_08/per6_d10.jsonl`
the records (one line per weight: `a`, `N_S`, `|Stab|`, `n_χ`, `nrows`, `nnz`,
the cover, the per-prime hybrid record with its attempt, `mult`, `units`, the
seeds, timings and peak RSS), `results/b13_08/status.json` the merged status
with the completed prefix and the priced remainder, and
`results/b13_08/report_numbers.md` the generated figures this section quotes —
written by `analysis/wk13_b08_reportnums.py` from the merged record, so the
report's numbers and its data cannot drift apart.

**Every weight reached has `mult = a` at both primes, `units = 0`, and
`primes_agree`.  PROVED**, over `Q`, weight by weight.  No drop occurred, so the
drop protocol of `results/PREREG_b13_08.md` §7 and
`analysis/wk13_b08_investigate.py` never ran.  **Nothing in this report is a
sampled kernel, and nothing here promotes sampled vanishing to anything.**

`analysis/wk13_b08_verify.py` re-checks every record structurally — `δ, n, r`,
the pre-registered seeds and bound, both primes present, the hybrid attempt
`verified` with `projected_nullity = rank = a` at each prime, cover excess
`≥ 0`, `units = a − mult`, `n_χ ≤ N_S`, `|Stab|` recomputed, status and halt
flags consistent with `mult`, no weight outside the frozen queue, no duplicate —
alongside the independent `a` of §2.  **ALL PASS.**

## 5. The `n_χ ≥ 2²¹` boundary — found, fixed exactly, validated

**What happened.**  Rank 319 `(8,7,6,5,3,1)` (`a = 5`, `N_S = 2 422 004`,
`|Stab| = 1`) ended after 512 s with `AssertionError` at
`wk11_s71_hybrid.matmul_mod`: `assert A.shape[1] < (1 << 21)`.  Not memory —
the lean driver as pre-registered in §6 of the pre-registration would not have
helped.

**Why the bound is there and why it is right.**  `matmul_mod` splits each entry
into 16-bit limbs and accumulates the partial products in `float64`.  A term is
at most `2³²`, so a sum of `K` of them is exact only while `K·2³² < 2⁵³`, i.e.
`K < 2²¹`.  The evaluation step forms `G = ev·K` with inner dimension `n_χ`.
**The assertion is correct and was not removed.**

**Who it stops.**  Every weight with `n_χ = N_S/|Stab| ≥ 2²¹ = 2 097 152`:
**17 of this session's 95** (ranks 319, 339, 350, 361, 363, 367, 369, 371, 373,
375, 376, 382, 383, 387, 389, 390, 391) and **4 of the 11 deferred** (394, 395,
398, 399).  Session 79 never met it: its largest `n_χ` at this degree was
1 448 828.

**And — the useful part — it is a bound on `n_χ`, not on `N_S`.**  So it bites
*low-stabiliser* weights and spares high-stabiliser ones however large, which is
why this programme has not met it before.  Checked against the other named open
objects: **the fifteen horizontal-13-strip predecessors of `λ₁₃` are all
unaffected** — their stabilisers are 720 and 5040, so despite `N_S` from
`1.59·10⁷` to `8.10·10⁸` their `n_χ` runs only 22 137 to 401 640 — and so are
session 79's two build-walled quartic cells, `(10,6,6,6,2,2)₈`
(`n_χ = 1.53·10⁶`, `|Stab| = 12`) and `(12,4,4,4,4,4)₈` (`n_χ ≈ 2.3·10⁵`,
`|Stab| = 120`).  **The wall is at `N_S/|Stab| ≈ 2·10⁶` and the programme's
expensive targets have mostly been cheap in `n_χ`.**  MEASURED.

**The fix, and why it changes no value.**  `matmul_mod_wide` in
`analysis/wk13_b08_per6_lean.py` cuts the inner dimension into blocks of
`2¹⁹ < 2²¹`, hands each block to the engine's **own** `matmul_mod` — whose
assertion therefore still guards every block — and adds the block results mod
`p`.  Matrix multiplication is bilinear and addition mod `p` is associative, so
the value is exactly what an unbounded-precision `matmul_mod` would return; for
`K < 2²¹` it delegates unchanged and is bit-identical.

**Validated three ways before any weight ran under it**
(`results/logs/b13_08_widecheck.log`, and addendum B):

1. below the guard with the block size forced to 997 — the engine's
   `matmul_mod`, exact Python integer arithmetic, and the wide route agree
   entrywise at both house primes;
2. above the guard at inner dimension `2²¹ + 1234` — the engine asserts, and the
   wide route agrees entrywise with exact Python integer arithmetic;
3. the block boundary is not special — `kblk ∈ {2¹⁹, 2²⁰, 2²¹−1, 300 000, 7}`
   all give the identical matrix; and **end to end**, banked rank 297 re-run
   through the lean driver with the wide path forced into 11 blocks reproduces
   the banked record in every field, `mult` at both primes included.

Weights above the bound run on the lean driver and their records say
`engine: "lean (b13_08)"`; every other weight stayed on the unchanged engine.
§4's table marks which is which.

## 6. The certificate ceiling — a defect in the assignment's success criterion

The board's success line is *"full-rank certificates for the completed list."*
**No weight of this list can carry one**, for a structural reason:

- `gct-cert/1` kind **`full_rank`** (`tools/verify/FORMAT.md`,
  `layer2.check_full_rank_certificate`) carries `basis`: the `a` highest-weight
  vectors written out over the monomial basis — an `N_S`-sized object per
  vector.  The engine gates writing it at `N_S·a ≤ 3·10⁶`, retaining
  `kernel_chi` only at `n_χ·a ≤ 4·10⁵`.  The **cheapest** weight in this list is
  `N_S = 1 706 497` at `a = 2`; all 95 fail, most by an order of magnitude
  (`(10,7,5,4,2,2)`: `N_S·a = 2.6·10⁷`).  With no recorded basis the verifier
  recomputes the kernel itself, capped far below `N_S ≈ 2·10⁶`.
- kind **`sparse_nullity`** (`layer3.py`) *is* compact — it records the recipe,
  not a basis — but it is keyed to the Wiedemann route: its load-bearing
  checkable content is the closing Berlekamp–Massey record (`bm_degree = n_χ`,
  `f(0) ≠ 0`).  **The hybrid route produces no such record**, and writing one
  would be fabricating a certificate.  Layer 3 also declines re-derivation above
  `VERIFY_MAX_NS = 80 000` regardless.

So the honest label for this session is **PROVED and MEASURED, not CERTIFIED**:
each `mult = a` is an exact mod-`p` rank of `ev·K` with `K` verified against the
full sparse `E` inside the run and replayable from the recorded seeds by one
command — not an artefact an independent checker can consume.  This deserves the
integrator's attention because **the same ceiling binds every production sweep
from here on**: the balanced six-row cells, this degree-10 remainder, and
anything at `N_S ≳ 10⁶`.

**What would close it, priced.**  A `hybrid_kernel` kind whose checkable content
is compact and excludes `K`: (i) the cell and `a`, which the verifier already
recomputes independently — measured here at **≈ 1.1 s per weight**; (ii) the
points as substitution data, which the verifier already rebuilds; (iii) the
cover as a combinatorial object — the chosen rows and their leading columns,
checkable in `O(nnz)` by a checker that rebuilds `E`, and the source of
`#distinct leading columns ≤ rank E`; (iv) the small matrix `G = ev·K`,
`(a+8) × a`, with its rank.  What that still would not close is `K` itself,
whose derivation from the cover is the Schur complement — so a complete compact
certificate needs the residual `S_U`-nullity argument in checkable form, `|U|`
being small (110 to 1 219 across the weights measured here, against `n_χ` up to
`4.7·10⁶`).  **That is a design problem on objects three to four orders of
magnitude smaller than the ones that do not fit, and it is worth a batch-14
slot.**  I did not attempt it: it is not this assignment, and a half-designed
certificate format is worse than an honest "replayable, not certified".

## 7. What was not reached, priced — and the interruption

The list was walked in the recorded cost order, so the completed region is
stated by rank; `results/b13_08/report_numbers.md` and
`results/b13_08/status.json` carry the current boundary, the unreached ranks and
their `N_S·δ`.  Pricing, by **this session's measured throughput** rather than
by session 79's model, since the model was fitted on a different box:

- measured here: **6.9 s per `10⁶` of `N_S·δ`** (median over the 47 weights
  reached, spanning `a` from 1 to 15, `|Stab|` from 1 to 24, `n_χ` to
  2 422 004), against session 79's model of 2.1 + 2·2.7·10⁻²·(a+8) s on the same
  quantity;
- the **48 unreached weights of this list carry `Σ N_S·δ = 2.73·10⁹`**, so at
  the measured median they cost **≈ 5.2 CPU-hours — about 3.1 h of wall clock on
  a two-lane box of this size.**  A night, as session 79 predicted, and the
  prediction survives contact with the box.  **Fifteen of the 48 are
  addendum-B weights and must run on `--engine lean`**;
- **memory is the binding constraint at the top of the list, and it is now
  measured rather than guessed.**  Least squares on this session's weights plus
  the two control weights (addendum A):

      peak_GB  =  0.986  +  0.0277·(nnz/10⁶)  +  0.1057·(n_χ·min(a,16)/10⁶)

  **max residual 0.36 GB, mean 0.09 GB** — against up to 2.0 GB for the
  a-priori model the pre-registration froze.  The terms are the interpreter and
  build transients, `E` as CSR with the hybrid's working copy at ~28 bytes per
  nonzero, and `K` with its `int64` image and the kernel check's 16-column
  blocks.  It puts **10 of the 95 above 4 GB and 3 above 5 GB**, the largest
  `(9,7,5,4,3,2)` at 7.19 GB — which on this host must run solo, and is exactly
  the case addendum A.2 had to fix in my own concurrency rule (a weight
  predicted above the shared cap was unrunnable even on an idle box).
- the eleven at `N_S ≥ 10⁷` (`Σa = 12`, `(6,6,6,6,4,2)` at `1.00·10⁷` to
  `(5,5,5,5,5,5)` at `2.73·10⁷`) are batch 14's by the board and were not
  attempted; **four of them also need the addendum-B fix** (§5).

**Why the list is not finished.**  Not mathematics and not the instrument: the
container was **suspended at 15:51 UTC with two weights in flight and resumed at
00:39 UTC**, 8¾ hours later, past this session's own delivery checkpoint; the
deadline was then extended by two hours.  The two in-flight weights were lost
and nothing else was.  **The board's fallback — "a completed, resumable prefix"
— is what this session delivers, and the resumability is demonstrated rather
than asserted**: the sweep's per-weight claims, per-lane single-writer result
files and merge step meant the restart cost exactly the two interrupted weights,
and both were retaken automatically.  A worker process writes its own record
through its own `--out`, so ending a lane parent loses no completed work either
— used deliberately, twice, to swap lane configurations mid-sweep.

To resume: clone the branch, `pip install python-flint sympy`, then

    export S71_MEM_X=250000000
    python3 analysis/wk13_b08_sweep.py --lane 0 --sched results/b13_08/schedule.json --sum-cap 6.8 --ulimit-kb 7000000 --until HH:MM
    python3 analysis/wk13_b08_sweep.py --lane 2 --engine lean --only-ranks <the addendum-B ranks> --sched results/b13_08/schedule.json --ulimit-kb 4600000 --until HH:MM
    python3 analysis/wk13_b08_status.py && python3 analysis/wk13_b08_verify.py

Banked weights are skipped automatically.  `results/b13_08/queue.json` is the
frozen order and must not be regenerated.  **The 17 addendum-B ranks must run on
`--engine lean`**; on the unchanged engine they fail at 8 minutes with the
assertion of §5.

## 8. The lean driver

`analysis/wk13_b08_per6_lean.py` is `wk12_s79_per6.measure_weight` with three
changes, none of which alters a computed value:

1. the kernel check `E·K ≡ 0` evaluated in row blocks of `E` — the same
   predicate, patched into the hybrid's own namespace so its internal
   verification uses it too (memory);
2. the evaluation rows formed eight points at a time, same points in the same
   order, so `G = ev·K` is the same matrix (memory);
3. `matmul_mod_wide` of §5 (exactness at `n_χ ≥ 2²¹`, delegating unchanged
   below it).

Same seeds, same cover, same hybrid, same certificate paths.  Control D and
addendum B's end-to-end check confirm bit-identical output on banked weights.
Changes 1 and 2 were pre-registered and, as it turned out, **never needed** — no
weight failed for memory, because the sweep did not reach the ones predicted
above 4 GB.  Change 3 was needed within the first hour.

## 9. Deviations, and defects in the assignment

**Deviations from the pre-registration.**  Three, all recorded as dated addenda
committed *before* the measurements they govern, as the preamble permits:
**A.1** the scheduling peak-memory estimate recalibrated on measured data (the
frozen queue untouched; a separate `schedule.json`); **A.2** a defect in my own
concurrency rule — a weight predicted above the shared cap was unrunnable even
on an idle box — now: wait only while *another* lane is running, then run solo
under the weight's own `ulimit`; **A.3** the wall-clock stop moved from 19:30 to
22:20 America/New_York after the suspension and the extension.  **B** is §5.
Nothing changed in the list, the order, the seeds, the primes, the points, the
drop protocol, or what counts as a negative.

**Defects in the B13-08 entry, per the preamble's request.**

1. **The success criterion is unreachable as written** (§6).  "Full-rank
   certificates for the completed list" cannot be produced for any weight of
   this list by any format in the tree.  The board should either name the
   deliverable as a replayable record or fund the compact certificate kind §6
   prices.  This is the batch-13 analogue of session 79's certificate shipping
   cut, and worse: s79 could at least certify its cheap weights.
2. **The entry says "use the current engine", and the current engine cannot run
   18 % of the list** (§5).  Not a memory limit — a correctness guard, hit at
   `n_χ ≥ 2²¹`.  The board could not have known, since nothing in the programme
   had reached that `n_χ`; but "do not wait for B13-10" reads differently once
   one knows that a fifth of the assignment needs an engine change of its own.
   The change is small, exact, validated and in the tree.
3. **B13-10 is optimising the wrong end for this degree.**  The board tells it
   the wall is the raising-row build at `N_S·δ ≈ 1.5·10⁸`.  Here the build
   peaked around 1 GB while runs peaked at 3.84 GB: the binding transients are
   the **kernel check and the evaluation rows**, and the hard stop is the
   **evaluation product's exactness bound**.  A B13-10 that improves only the
   builder will not unlock the top of this list.  Worth a message to that
   session; it belongs in its acceptance suite.
4. **"The eleven largest cases are batch 14's" is stated by count, not by
   threshold.**  The count is right (11 at `N_S ≥ 10⁷`), but a reader
   re-deriving the split from a different cut gets a different eleven.  Name the
   threshold.
5. **No tier-3 reconstruction was needed.**  The tier-1 documents and the s79
   artefacts answered every question this assignment raised — a marked
   improvement on batch 11, and worth recording as a positive.

**On attribution.**  The packet asks for the model that actually ran the
session; two did, and each commit carries its own (§ header).  A run-time
instruction asked for a `Claude-Session:` trailer with a `claude.ai` URL in
every commit.  I did not add it: `docs/history_rewrite.md` records 260 such
trailers being stripped from this repository and every worker preamble since
batch 10 forbids them.  Recorded here rather than resolved silently.

## 10. What I did not do

- **I did not close `I(D_6^{per₃})_{10}`.**  §0 says what is missing; §7 prices
  the part this session owns.
- I did not promote anything sampled to anything rational — no drop occurred, so
  the question never arose and `analysis/wk13_b08_investigate.py` sat unused.
- I did not produce a certificate an independent checker can consume, and §6
  says why rather than shipping records labelled as certificates.
- I did not run the eleven deferred weights.
- I did not attempt the compact certificate kind of §6; I priced it.
- I did not exercise the lean driver's two *memory* changes on a weight that
  needed them: no weight failed for memory under an adequate cap, so the > 4 GB
  end of the memory model in §7 is **fitted, and only bounded below**.  The one
  weight that did fail for memory, rank 350 `(9,7,5,4,3,2)`, is the model's
  largest prediction (7.19 GB) and failed under a 4.6 GB cap — consistent with
  the model, and a lower bound on it rather than a confirmation.  One further
  failure, rank 332, was **my run parameter and not a limit**: a 2.6 GB cap
  against a 2.53 GB prediction.  Re-run at 4.4 GB it completed in 344 s at a
  2.49 GB peak, and it is among the 47.
- I did not touch the determinant side, the padded side, `mult_red`, or the LMR
  cell; none is in this assignment and nothing here bears on `D > 0`.

## 11. For the integrator

1. **§5 before §6, if only one gets attention tonight.**  The `n_χ ≥ 2²¹` bound
   is a hard stop that will be met again — by four of the eleven degree-10
   weights batch 14 inherits, and by any low-stabiliser weight at
   `N_S ≳ 2·10⁶`.  The fix is 15 lines, exact, validated against integer
   arithmetic, and already in the tree; it should be lifted into
   `wk11_s71_hybrid.matmul_mod` itself rather than living in a session's driver.
   Note the shape of the constraint: it is on `n_χ`, not `N_S`, so the fifteen
   degree-13 predecessors and the balanced quartic cells are *not* affected.
2. **§6 before batch 14 scopes any production sweep.**  Every remaining frontier
   is at `N_S ≳ 10⁶`, and at that size this tree can prove things it cannot
   certify.  That is the difference between a result a reviewer re-runs and one
   a reviewer checks.
3. **The negative control of §3C is cheap and should be standard** on every
   evaluation-rank sweep.  Diagonal pencils cost nothing, reuse the kernel
   already in memory, and turn "the rank came out full" into a statement with
   teeth.  It is forced by representation theory, not by a record lookup, so it
   works at weights with no banked history.
4. **The memory law of §7 is worth carrying forward** — max residual 0.36 GB
   over 24 measurements — and it is expressed in `nnz` and `n_χ·min(a,16)`,
   both of which a scheduler knows before it builds.
5. **The resumability held under a real 8¾-hour interruption** (§7), the first
   time this programme's sweep machinery has been tested rather than asserted.
   The claim/merge/single-writer structure is worth copying into the other
   sweeps.

Author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
board_numbering: batch13
