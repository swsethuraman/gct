# Pre-registration — B13-09, higher-length cubic exploration

board_numbering: batch13
Session B13-09 (Fable).  Model that ran this session: Claude Fable 5.1
(`claude-fable-5-1`).  Base `git rev-parse main` = `00495110c62acfbbbc951e82cc218ed091563b3f`;
branch `b13-09-higher-length`.  Written 2026-09-09 15:40 UTC, before any queue
weight is measured (the calibration and control runs of §2.3 precede it and are
banked in `results/b13_09/calibration_r6.jsonl`, `results/b13_09/controls.jsonl`).

Labels used below and in the report: **PROVED** (a theorem in the tree, or a
full rank at one prime), **CERTIFIED** (an exact statement over `Q` carried by a
replayable certificate), **MEASURED** (computed here mod both primes; a sampled
rank is a floor on the rank and a ceiling on `i`), **ADOPTED** (the record),
**RECORDED** (a cost, a boundary, a mod-`p` kernel), **EXPECTATION**.

## 1. The question

The cubic-side ideal at lengths seven and eight through degree nine:

    is  I(D_r^{per_3})_delta = 0  in  C[Sym^3 C^r]_delta  for  (r, delta) in {(7,7), (7,8), (7,9), (8,8), (8,9)} ?

`D_r^{per_3} = closure{ per_3(sum_{i<=r} s_i A_i) } ⊂ Sym^3 C^r`, `dim = 9r − 4`
(`docs/washout_lemma.md` Prop. 5; 59 of 84 at `r = 7`, 68 of 120 at `r = 8`).
By Prop. 8(1) of `docs/transfer_lemma.md`, `I(D_r^{per_3})_delta = 0` gives
`mult_pad = mult_red` at **every** `r`-row quartic weight of degree `delta`
(objective 2's negative, a theorem with no points in it); by Prop. 8(2), a
constituent `S_mu ⊆ I(D_r^{per_3})_delta` is the only route to
`mult_pad < mult_red` at an `r`-row weight `lambda ⊇ mu` with `lambda/mu` a
horizontal `delta`-strip.  **This session serves objective 2 and the pricing of
the region; it makes no claim about objective 1 (`D > 0`), whose binding
constraint is `i_det`, not anything computed here** (`docs/batch13_corrections.md` §1).

Weight by weight the object is `units(mu, delta) = a(mu, delta) − mult(mu, delta)`,
`a` the multiplicity of `S_mu` in `Sym^delta(Sym^3 C^r)`, `mult` the rank of the
evaluation of the weight-`mu` highest-weight space at points of the parametrisation.

## 2. The instrument

### 2.1 Evaluator (`analysis/b13_09_per_r.py`)

Session 79's cubic evaluator `analysis/wk12_s79_per6.py` (fixed at `R = 6`)
with `R = len(mu)`, on the **unchanged** engine: build `wk9_s45_build.build_cell`
(`n = 3`; monomials, `chi`-isotypic reduction, raising rows), kernel
`wk11_s71_hybrid.hybrid_kernel` (initial-term cover + exact Schur residual, every
kernel vector verified `E·v = 0` on the full `E`, the kernel dimension asserted
equal to `a` at each prime), evaluation rows `wk12_s79_cell6.ev_rows_from_coeffs`
(length-general).  Points: session 41's family, `per_3(sum_{i<=r} s_i A_i)` with
`A_i` integer `3×3` in `[−40, 40]`, seed 41, `K = a + 8` points, **both house
primes** `2147483647`, `2147483629`.  `mult = rank_p(ev · K)`.

- `mult = a` at one prime **proves** `mult = a` over `Q` (`rank_p ≤ rank_Q`):
  `S_mu ⊄ I(D_r^{per_3})_delta`.  The two primes are asserted to agree.
- `mult < a` is a **MEASUREMENT**: a rank read off a finite point set is a
  floor on the rank of the family, so it bounds `units` from *below* only by
  sampling; nothing here establishes `units ≥ 1` over `Q`.  The evaluator
  re-checks a drop in the same call at `3a + 24` fresh points (seed 907), exhibits
  the vector(s) in `chi`-coordinates with `values_are` beside them, verifies
  `E·v = 0`, and returns `halt`.
- `a` enters three ways and must agree: Weyl alternation (tail DP,
  `wk9_s42_census`; the census uses an `S_r`-symmetric cache, asserted equal to
  the s42 routine on all 492 weights of `(7,7)`, `(7,8)`, `(8,8)`), the
  symmetric-function plethysm (`wk8_s30_pleth.a_of`, asserted in the census for
  every weight except `(8, 9)`, where `amb(9,3,8)` runs separately and is merged
  when it finishes), and the mod-`p` nullity of the raising operator on `V_chi`
  inside the hybrid at both primes.
- Exponent letters are resolved by tuple lookup through `exps(3, r)` of
  `wk8_s30_core` (`co.get(alpha)`), never by a literal position.
- Stored vectors carry `values_are` beside the numbers.  Runs are bounded at
  launch (`timeout`, `ulimit -v`), pids in `results/logs/<run>.pid` and
  `results/logs/<run>_child.pid`.

### 2.2 Sweep (`analysis/b13_09_sweep.py`)

One weight per bounded subprocess, queue in **`N_S` order** within each
`(r, delta)`, each result appended to `results/b13_09/per_r{r}_d{delta}.jsonl`
and committed as it lands (bank per unit); `status_r{r}_d{delta}.json` holds
reached / not-reached with reasons; the sweep halts at the first `halt`.

### 2.3 Calibration and controls (MEASURED before this document, all PASS)

| what | expected | read |
|---|---|---|
| s47's control `(7,5,4,4,2,2)_8`, `R = 6` | `a = 1`, `N_S = 285313`, `n_chi = 76792`, `mult = 1` | identical, both primes, 9.6 s |
| s79's `(11,7,4,2,2,1)_9`, `R = 6` | `a = 9`, `N_S = 74566`, `n_chi = 39986`, `mult = 9` | identical, both primes |
| s79's `(13,7,2,2,2,1)_9`, `R = 6` | `a = 3`, `N_S = 19505`, `n_chi = 4137`, `mult = 3` | identical, both primes |
| **negative control**: the same code path on `per_3` of **diagonal** pencils (split cubics) at `(13,7,2,2,2,1)_9` | `mult = 0` (PROVED: `C[Chow_3(V)]_delta` is a quotient of `Sym^3(Sym^delta V)`, no constituent with `> 3` rows) | `mult = 0`, `units = 3` at both primes; the recheck at `3a + 24` points and the exhibit-and-verify path executed |

Before the queue runs, the negative control is repeated at one length-7 queue
weight (`(6,5,5,2,1,1,1)_7`) and one length-8 weight (`(6,6,5,3,1,1,1,1)_8`);
a read other than `mult = 0` there is an instrument defect and stops the session
(F1).  Also the s79 control that the `per_3` coefficient dictionaries differ
from the `det_3` restriction of the same pencils, at `R = 7`.

## 3. The objects — the census (`results/b13_09_census.json`, md5 `79f59f39e4669669561c78afe16fee1a`)

### 3.1 What is inherited, and from where (accounted, not run)

`I(D_r^{per_3})_delta` decomposes over weights `mu ⊢ 3·delta` of length `≤ r`.
The restriction lemma (`docs/washout_lemma.md` §1, standing, PROVED) applies
verbatim with `X = D_r^{per_3}`: a highest-weight vector of weight `mu`,
`ell(mu) = k < r`, is a polynomial in the `c_alpha` with `supp(alpha) ⊆ {1..k}`,
so it sees only `F|_{C^k}`, and as `F` runs over the dense subset
`per_3(sum_{i<=r} s_i A_i)` of `D_r^{per_3}` the restriction
`per_3(sum_{i<=k} s_i A_i)` runs over a dense subset of `D_k^{per_3}`.  Hence
`mult_mu C[D_r^{per_3}]_delta = mult_mu C[D_k^{per_3}]_delta`, `k = ell(mu)`:
**a shorter weight's `units` is its length-`k` value.**  Therefore

| length of `mu` | covered by | status |
|---|---|---|
| `≤ 5` | `docs/washout_lemma.md` Thm 2 (`D_k^{per_3} = Sym^3 C^k`, `k ≤ 5`, exact Jacobian rank 35 at both primes) + Thm 3(1) | PROVED, every degree |
| `6` | `I(D_6^{per_3})_delta = 0`: `delta ≤ 6` Pieri + s37 (`docs/transfer_lemma.md` §4); `delta = 7` s41 + s43 (27 weights, `results/s41_per6.md`, `results/s43_per6.md`); `delta = 8` s41 + s43 + s47 (91 weights, `results/s47_per6_d8.md`); `delta = 9` s79 (210 weights, `results/s79_per6_d9.md`) | PROVED (full ranks at both primes), `delta ≤ 9` |
| `7`, at `r = 8` | this session's length-7 results | PROVED where §3.2's `(7, delta)` group completes; otherwise open with the unreached weights named |
| exactly `r` | **this session's queue** | — |

The counts the census records for the shorter weights at each degree
(weights with `a ≥ 1`; `Σa`): `delta = 7`: `ell ≤ 5`: 129 (193), `ell = 6`: 27
(27); `delta = 8`: `ell ≤ 5`: 232 (490), `ell = 6`: 91 (139); `delta = 9`:
`ell ≤ 5`: 365 (1213), `ell = 6`: 210 (592).  The `ell = 6` counts equal the
record's (27, 91, 210) and the `ell ≤ 5` count at `delta = 9` equals the
integrator's 365 / 1213 (`docs/s79_part2_review.md` §2a) — the enumeration is
consistent with the record.  **None of these is re-run.**

### 3.2 The new components — exact length `r`, `a ≥ 1`

| `(r, delta)` | weights | `Σa` | max `a` | `N_S` range | `N_S·delta` total | model build (2.1·10⁻⁶ s/unit) | above the `1.5·10⁸` wall |
|---|---|---|---|---|---|---|---|
| (7, 7) | **5** | 5 | 1 | 48 122 – 67 131 | 2.0·10⁶ | 4 s | 0 |
| (7, 8) | **42** | 42 | 1 | 63 711 – 843 890 | 9.6·10⁷ | 3.4 min | 0 |
| (8, 8) | **6** | 6 | 1 | 804 050 – 1 259 739 | 5.1·10⁷ | 1.8 min | 0 |
| (7, 9) | **152** | 265 | 6 | 65 416 – 10 848 589 | 2.33·10⁹ | 82 min | 0 (largest `9.76·10⁷`) |
| (8, 9) | **62** | 63 | 2 | 1 063 374 – 19 615 170 | 3.39·10⁹ | 119 min | **3**: `(7,6,4,3,3,2,1,1)` 1.53·10⁸, `(9,4,4,2,2,2,2,2)` 1.69·10⁸, `(8,5,4,3,2,2,2,1)` 1.77·10⁸ |

267 weights in all, `Σa = 381`, total `N_S·delta = 5.9·10⁹` (model build 3.4 h,
plus evaluation rows at `2.7·10⁻⁸ s` per point per unit and the hybrid, which
was never the cost at `n_chi < 10⁶` in s79 and is unpriced above).  Every
weight of the census is in the JSON with `a`, `N_S`, `|Stab|`, the `n_chi` lower
bound, `N_S·delta` and the model time.

### 3.3 Queue order and streams (host: 2 vCPU, 7.8 GB, no swap)

- **Stream A** (sequential, commits per weight): `(7,7)` → `(7,8)` → `(8,8)` →
  `(7,9)` → the `(8,9)` weights stream B has not reached.
- **Stream B** (parallel while both are cheap): `(8,9)` in `N_S` order, capped
  at `N_S·delta ≤ 5·10⁷` so that two builds never share more than the box.
- Within a group, `N_S` ascending, so that what is reached is a **certified
  prefix** in cost order and what is not is the priced remainder.
- Bounds per weight: `timeout 5400` s, `ulimit -v 6 500 000` kB (address space),
  `S71_MEM_X = 2.5·10⁸` (s79's setting).  Cap `N_S·delta ≤ 1.8·10⁸`: the three
  `(8,9)` weights above s79's wall are queued **last** and attempted only if
  everything below them is done; a failure there is the boundary, reported with
  its `N_S·delta`.  No degree extension beyond 9 is requested or run.
- Wall clock: the queues run until **23:15 UTC** (19:15 EDT) at the latest;
  what is reached is reported with its cost, what is not with its `N_S·delta`.
  Substantive update at about 22:00 UTC (18:00 EDT).

## 4. Predictions (EXPECTATION) and what counts as a negative

- **P1 (0.6):** `I(D_7^{per_3})_delta = 0` for `delta = 7, 8` and
  `I(D_8^{per_3})_8 = 0` — all 53 weights of `(7,7)`, `(7,8)`, `(8,8)` at
  `mult = a`.  Then, with §3.1: **`mult_pad = mult_red` at every seven-row weight
  of degree `≤ 8` and every eight-row weight of degree 8** is a THEOREM
  (Prop. 8(1)); the permanent is invisible on the reducible side there.
- **P2 (0.5):** `I(D_7^{per_3})_9 = 0` on the whole `(7,9)` group; **P3 (0.4):**
  `I(D_8^{per_3})_9 = 0` on the whole `(8,9)` group if reached.  The prior is
  lower than at length 6 (s79's 0.6): `codim D_7^{per_3} = 25` and
  `codim D_8^{per_3} = 52` against 6 at `r = 6`, so the ideal is larger and may
  start lower, and every equation through degree 9 must sit at a weight of
  length exactly `r` (§3.1).
- **What counts as a negative:** `mult = a` at both primes at every weight of a
  group is `I(D_r^{per_3})_delta = 0` **PROVED** (a full rank at one prime
  suffices; both are required to agree), with the Prop. 8(1) corollary.  A
  partial group is a **certified prefix** (PROVED at each reached weight) plus a
  priced remainder — a negative characterised over a stated region.
- **What counts as a candidate:** `mult < a` at both primes at a weight, the
  recheck at `3a + 24` points confirming, the vector(s) exhibited with
  `E·v = 0` verified.  Reported as **MEASURED** (a mod-`p` kernel; a ceiling on
  the rank), never as `units ≥ 1` over `Q`; the sweep of that group halts; the
  verification protocol of `docs/batch13_worker_preamble.md` runs: second prime
  (already in), a **second independent point family** (seed 1041, bound 1000,
  `3a + 24` points), the degeneracy pre-check of `docs/brief_wording.md` §5 in
  its cubic-side form (the exhibited vector evaluated at random **generic**
  cubics `F ∈ Sym^3 C^r` mod `p` must be nonzero — a vector that vanishes on
  generic cubics is the zero function and no equation at all — and at split
  cubics, where it must vanish), and the Pieri list of `r`-row quartic weights
  `lambda ⊇ mu`, `lambda/mu` a horizontal `delta`-strip, which is where a
  `mult_pad < mult_red` cell could then be sought (not run here unless time
  remains; it is not this session's queue).  No rational membership statement is
  attempted (that is B13-03's method); no negative decision-table branch is
  entered on a sampled kernel.
- **Primes disagree** at a weight: recorded, re-run once with a fresh hybrid
  seed, no verdict until they agree.

## 5. Falsifiers and stopping rules

- **F1 (instrument):** a calibration cell disagrees with the record at either
  prime, or a negative control reads `mult ≠ 0`, or the three routes to `a`
  disagree, or a `chi`-obstructed row fails to cancel (an assertion in the
  build) → the queue does not start / stops; the defect is reported.
- **F2 (theory-contradicting drop):** a drop at a weight of length `≤ 6` cannot
  occur here (none is run); a drop at a `(7, delta)` weight with `delta ≤ 6` is
  impossible (Pieri) and none is queued.
- **Stopping rules:** the wall clock of §3.3; a weight that exceeds its
  `timeout` or its address-space bound is recorded as *not reached* with its
  `N_S·delta` and the queue continues (the boundary is the deliverable, not a
  reason to stop); a group halts at its first `halt`.  Anything run outside
  this document is reported as **exploratory**.

## 6. Deliverables

`results/b13_09_census.json`; `results/b13_09/per_r{r}_d{delta}.jsonl` and
`status_*.json`; certificates `results/certs/b13_09/` (`gct-cert/1`
`full_rank`, `n = 3`, `permanent_pencil`, gzipped, ≤ 4.5 MB each, only those
that fit the 5 MB rule committed, all listed with md5 in
`results/b13_09/cert_manifest.json`); logs under `results/logs/b13_09_*`;
`docs/b13_09_report.md`; bundle `b13_09_higher_length.bundle` + `.md5`
against the base above, parts from `part00`.

Author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI (session run
by Claude Fable 5.1).
board_numbering: batch13

---

## Addendum A (committed 2026-09-10 00:45 UTC, before any queue weight is measured)

**A.1 The wall clock, revised.**  §3.3 set the queues to run until 23:15 UTC
2026-09-09.  The session's container was idle from about 15:45 to 00:40 UTC and
**no queue weight was measured in that window** — the interval is lost, not
spent.  The revised bound: the queues run until **02:30 UTC 2026-09-10**, and
the report is written from whatever is banked at that point.  Everything else in
§3.3 stands unchanged (per-weight `timeout`, `ulimit -v`, the `N_S·delta` caps,
`N_S`-ascending order within each group, no degree extension).  The consequence
is priced honestly rather than hidden: the `(7,9)` and `(8,9)` groups will be
**certified prefixes with a priced remainder**, not completed ranges, and the
report says so.

**A.2 Queue order, narrowed to the revised clock.**  Unchanged in kind, but
stated as one list so what is reached is unambiguous:

1. `(7,7)` — 5 weights, `N_S·delta ≤ 4.7·10⁵`
2. `(8,8)` — 6 weights, `N_S·delta ≤ 1.01·10⁷`
3. `(7,8)` — 42 weights, `N_S·delta ≤ 6.75·10⁶`
4. `(7,9)` — 152 weights, `N_S` ascending
5. `(8,9)` — 62 weights, `N_S` ascending

1–3 are the 53 weights of prediction **P1** and are the session's first claim on
the clock: completing them makes `I(D_7^{per_3})_delta = 0` for `delta = 7, 8`
and `I(D_8^{per_3})_8 = 0`, hence (Prop. 8(1)) `mult_pad = mult_red` at every
seven-row weight of degree `≤ 8` and every eight-row weight of degree 8.
Streams 4 and 5 run concurrently after them (two vCPU, one build each, the
`(8,9)` stream capped at `N_S·delta ≤ 5·10⁷` so two builds cannot exhaust the
box), each banking a prefix in cost order.

**A.3 The model that ran this session, stated exactly.**  The board asks for the
model that actually ran the session, and two did.  **Claude Fable 5.1**
(`claude-fable-5-1`) ran everything up to and including this pre-registration:
the reading, the instrument (`analysis/b13_09_per_r.py`), the census
(`analysis/b13_09_census.py`, `b13_09_pleth89.py`, `b13_09_census_merge.py`), the
three calibration reproductions and the negative control of §2.3.  The session's
model was then changed, and **Claude Opus 5** (`claude-opus-5`) runs the measured
queue, the verification and the report.  Commits carry the model that made them:
the setup commits `Co-Authored-By: Claude Fable 5.1`, this addendum and
everything after it `Co-Authored-By: Claude Opus 5`.  The report repeats this in
its first paragraph.  No number in this session was produced by a model other
than the one its commit names.

**A.4 The (8,9) plethysm cross-check landed.**  `amb(9,3,8)` (789 constituents
of at most 8 rows, 29 s) is merged into the census and agrees with the Weyl
alternation at all 62 `(8,9)` weights, **in both directions**: no 8-row weight
with `a ≥ 1` in the plethysm is missing from the census and none is extra
(`analysis/b13_09_census_merge.py`).  So `a` now has two independent sources at
every weight of all five groups, and the hybrid's mod-`p` nullity is the third
at run time.

---

## Addendum B (committed 2026-09-10 00:58 UTC, before the measurements it governs)

**B.1 The wall clock, extended.**  The session owner extended the deadline by two
hours.  Addendum A.1's bound of 02:30 UTC is replaced by **04:30 UTC 2026-09-10**
for the queues, with the report written after.  Nothing else changes: the
per-weight `timeout` and `ulimit -v`, the `N_S·delta` caps, the `N_S`-ascending
order within each group, the halt-on-drop rule and the "no degree extension
beyond 9" bound all stand as pre-registered.  The extension is recorded here
rather than applied silently, because a stopping rule that moves after the
numbers are seen is not a stopping rule.

**B.2 What the extension is spent on, in order.**  It does not change the queue
order of A.2.  It buys, in this priority: (i) the remainder of `(7,8)` and
`(8,8)`, completing prediction **P1**; (ii) as much of `(7,9)` as the clock
allows, in `N_S` order, banked per weight; (iii) as much of `(8,9)` as the second
stream allows under its `5·10⁷` cap; (iv) if and only if (i)–(iii) leave time,
the three `(8,9)` weights above s79's `1.5·10⁸` wall, attempted last, one at a
time, with the failure recorded as the boundary and its `N_S·delta` — not as a
result.  No new group and no new degree is added.

**B.3 Controls, both lengths, before their queues (MEASURED, PASS).**  The
length-7 negative control at `(6,5,5,2,1,1,1)_7` and the length-8 one at
`(6,6,5,3,1,1,1,1)_8` both read `mult = 0` at both primes on the split-cubic
family, `n_chi = 1973` and `4257` respectively, with the recheck and
exhibit-and-verify path executed.  The `per_3`/`det_3` distinctness control at
`R = 7` differs at 10 of 10 points.  F1 did not fire.
