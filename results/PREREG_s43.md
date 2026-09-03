# Pre-registration — session 43 (closing the six-row region already in reach)

Written **before any measurement of this session**, on branch `s43-sixrow-close`,
clone tip `0c229c1` (clone gate passes: `docs/s41_review.md`,
`analysis/wk9_s41_kernel.py`, `results/s41_ledger.md`, `results/sixrow_census.md`,
`results/s41_per6.md`, `docs/brief_wording.md` all present).  Date 2026-09-03.
Vocabulary per `docs/brief_wording.md`.  Labels used in the report:
**proved** / **measured** / **adopted-from-literature** / **expectation**.

There is no session 43 in the repository at clone time (`docs/s43_prompt.md` is
the brief; no `results/s43_*`), so nothing is renumbered.

## 0. What this session does

Three phases, all inside the frontier session 41 established and validated
(`n_χ ≤ 20,000`, in-place rref route, peak `≈ 1.4e-8·n_χ² + 0.4` GB predicted /
`4.68` GB measured at `n_χ = 19,985`).

- **Phase A.**  The eligible six-row cells that fit at `n_χ ≤ 20,000` and were
  not measured by sessions 36 or 41.  The list is **re-derived from
  `results/sixrow_census.md`**, not taken from `results/s41_coverage.md`; any
  disagreement with the inherited counts is reported as a finding.
- **Phase B.**  The seven length-6 weights `μ ⊢ 21` with `a(μ,7) ≥ 1` that
  Phase 0b of session 41 left above its `n_χ = 6000` cap.  If all are empty,
  `I(D_6^{per_3})_7 = 0` outright and Prop. 8(1) of `docs/transfer_lemma.md`
  makes `mult_pad = mult_red` in **every** weight of degree 7 a theorem with no
  points in it.  Then, as budget allows, the same scan at `δ = 8` above
  `n_χ = 6000`, ascending in `n_χ`.
- **Phase C.**  The cheapest `ℓ = 6`, `λ ⊢ 36`, `λ_1 ≥ 9`, `a ≥ 1` cells — the
  first rung at `δ = 9`.

**Order of execution.**  Phases A and B run concurrently under one shared
memory guard (the container has 2 cores and ~7 GB; the guard waits, never
skips, and above `n_χ ≈ 8000` only one cell of either phase is resident).  This
is a scheduling decision, pre-registered here, and changes no measurement: each
cell is an independent process with its own peak recorded.  Within each phase
the order is strictly ascending `n_χ`, as the brief requires.  Phase C starts
only after Phase B's seven weights are settled.

## 1. Pipeline (unchanged, inherited, validated)

`analysis/wk9_s36_stabred.py` up to the kernel; kernel by the in-place rref
route of `analysis/wk9_s41_kernel.py`; every kernel vector multiplied against
the **uncompressed** sparse raising-operator rows and asserted to vanish mod
`p`.  `a` by kernel dimension **and** by plethysm, asserted equal;
`rank(R) = n_χ − a` asserted.  Ranks by `python-flint` `nmod_mat` over
`p₁ = 2147483647` and `p₂ = 2147483629`; both primes must agree.  `a + 8`
evaluation points per side.  Points: det `det_4(Σ s_i A_i)`; pad the **true
padded-permanent restriction** `l(s)·per_3(A(s))` through `per_padded(3,4)` and
`restrict()` — never `l·(random cubic)`.  `mult_red` point-free by (★)
(`docs/reducible_ideal.md`, Corollary A).  `m_det` the symmetric rectangular
Kronecker bound.  Convention `D = mult_pad − mult_det`; only `D > 0` is an
obstruction.  `python-flint` only.  One process per cell, so the banked `HWM`
is that cell's own peak.

**Independent re-check.**  Any cell with `mult < a` on either side gets
`3a + 24` fresh points, a fresh seed (907), both primes, **before** it is
banked; the vanishing vector is exhibited and run through the symbolic battery
of `analysis/wk9_s41_bite.py`.

**Bounding long runs.**  Every long run is launched under `timeout <seconds>`
and `ulimit -v`, with its process id written to `results/logs/<run>.pid`.  A run
that must be ended early is ended by that recorded id; never by name-pattern
matching.

**Delivery.**  Git bundle `sixrowclose.bundle`, single ref `s43-sixrow-close`;
no push; a checkpoint bundle every few hours.  Commit messages carry
`Co-Authored-By` only — no session-link trailer, and no script of this session
writes one.  Single-writer files (`paper/det3-conductor.tex`,
`paper/det4-onset.tex`, `PROJECT_NOTES.md`, `docs/boundary_deficit.html`) are
not touched.  Nothing over 5 MB; logs under `results/logs/`; no repository-wide
config rewritten.

## 2. Predictions and falsifiers

### P1 — validation (stopping rule: failure stops the session)

Three banked session-41 rows are re-measured from scratch by this session's
driver and must reproduce **exactly**, both primes:

| δ | λ | a | mult_det | mult_pad | mult_red | D |
|---|---|---|---|---|---|---|
| 8 | `(13,10,6,1,1,1)` | 9 | 9 | 8 | 8 | −1 |
| 8 | `(16,10,3,1,1,1)` | 2 | 2 | 2 | 2 | +0 |
| 7 | `(12,10,3,1,1,1)` | 1 | 1 | 1 | 1 | +0 |

The first is the discriminating one: a route that cannot see the pad-side drop
returns `mult_pad = 9 = a` and `D = 0`.  A pipeline that has lost the true
padded-permanent points, or the (★) reducibility criterion, fails here and
nowhere else in this list.  In addition the `m_det` anchors `Σ = 3, 11, 43` at
`n = 3` are re-run (`wk9_s38_screen` self-test), and Phase B's driver is
validated by reproducing two banked `results/s41_per6.md` rows.

**Falsifier:** any disagreement in `a`, `mult_det`, `mult_pad`, `mult_red` at
either prime → stop, report, measure nothing further.

### P2 — Phase A: will any of the 49 show `mult_det < a`?

**Prediction: no.  0 of 49.**  Stated before measurement, with the reasoning
and the regime.

*Reasoning.*  (i) The determinant's six-row ideal is empty at all 90 cells
measured so far (`δ = 6, 7, 8`), at `a` up to 10 and `n_χ` up to 19,985; the
49 cells here are drawn from the same reachable set and are not distinguished
from it by any statistic the census exposes.  (ii) The arithmetic route is
silent at every one of the 849 census cells (`a ≤ m_det`, tightest margin 12),
so any drop here would be a pure multiplicity drop invisible to the occurrence
screen — the length-5 phenomenon of s38, which at length 5 first appeared only
at `δ = 8`, and there in the *balanced* corner.  (iii) **Regime.**  All 49 are
peaked: at `δ = 7` the six cells have balance 9–15, at `δ = 8` the 43 have
balance 10–19.  The balanced corner where s30/s36's dimension heuristic would
place a first det-side bite (balance `≤ 8` at `δ = 7`, `≤ 9` at `δ = 8`) is
**entirely outside** this list — it sits above `n_χ = 20,000`.  So this
session's Phase A tests the *peaked* regime once more and cannot test the
balanced one.  A negative result therefore extends coverage, not the bracket's
credibility, and the report will say so.

*What would falsify it:* one cell with `mult_det < a`, surviving the
independent re-check.  That is the six-row onset and the number the programme
wants; the protocol below takes over immediately.

### P3 — Phase B: is `I(D_6^{per_3})_7 = 0`?

**Prediction: yes — all seven weights empty (`mult = a = 1` at each).**

*Reasoning.*  `I(D_6^{per_3})_δ = 0` for `δ ≤ 5` for free (Pieri), is measured
zero at `δ = 6` (all four `a > 0` weights, s37), at 20 of the 27 weights of
`δ = 7` and at 28 weights of `δ = 8` (s41).  Nothing yet distinguishes the
seven remaining weights from the twenty measured except `n_χ`, which is an
artefact of the stabiliser, not of the geometry: the seven are the
*less*-symmetric weights (stabiliser 1, 2 or 4), and there is no reason for the
first equation of a `GL_6`-stable ideal to prefer a small stabiliser.  Against
that: `dim D_6^{per_3} = 50 < 56 = dim Sym^3 C^6`, so the ideal is certainly
nonzero in *some* degree, and 21 of the 56 coefficient functions is a small
system — degree 7 is not an unreasonable place for it to start.  I put the
chance that one of the seven bites at roughly 1 in 6.

*Verification of `a` (pre-registered, done before measurement):* all 27 weights
of `δ = 7` were enumerated by plethysm and each has `a = 1`; the seven
unmeasured are exactly the brief's list, with `n_χ` = 6167, 6895, 6982, 8402,
9789, 12564, **39921**.

**The seventh weight is out of reach for the dense route.**  `(6,5,4,3,2,1)`
has trivial stabiliser, `n_χ = N_S = 39,921`; the in-place rref would need
`≈ 19` GB against a 7 GB container.  Pre-registered alternative, to be
attempted only after the other six are banked and only if it validates first:

> **The `a = 1` injectivity route.**  For `a = 1`, `mult = 1` iff the single
> highest-weight vector does not vanish at the evaluation points, i.e. iff the
> stacked sparse system `[M ; Ev]` (raising-operator rows plus the `K` dense
> evaluation rows, all `n_χ` columns) is injective.  Full rank over `F_p`
> forces full rank over `Q`, so an injectivity certificate proves `mult = a`
> in the same one-sided direction as every other "empty" verdict in the
> programme.  It needs no kernel and no dense `n_χ × n_χ` matrix: session 42's
> sparse Wiedemann tool (`analysis/wk9_s42_sparse.py`, `wk9_s42_wied.c`)
> certifies exactly this.  **Validation gate:** the route must first reproduce
> the verdict of the dense route at three already-measured `a = 1` weights of
> this same family, both primes, before it is used at `(6,5,4,3,2,1)`; and its
> verdict there is reported as `mult = a` **by the injectivity route**, in its
> own column, never merged into the dense rows.  If the tool is inconclusive
> after its retry budget, the weight is reported unmeasured and Phase B's
> theorem is stated conditionally on it.

**Consequence if P3 holds at all seven:** `I(D_6^{per_3})_7 = 0` outright, so
by Prop. 8(1) `I(P_6)_7 = I(R_6)_7` and `mult_pad = mult_red` at **every**
weight of degree 7 — a theorem with no points in it.  It removes the one "not
forced" cell of `results/s41_coverage.md`, `(15,4,4,2,2,1)` at `δ = 7`, whose
only unmeasured transport weight is `(9,4,3,2,2,1)`.

**Falsifier:** any weight with `mult = 0`.  That is the first permanent
equation the programme has seen.  Stop, certify it (exhibit the vector, fresh
seed, both primes, the symbolic battery, and (★) on every monomial to
distinguish a permanent-specific equation from a reducibility one), report,
and end the session there — it is a bigger result than anything in Phase A.

### P4 — Phase C: `δ = 9`

**Prediction: `mult_det = a` at every `δ = 9` cell reached, and `D ≤ 0`
throughout, with `D = −1` at zero or one of them.**  `I(R_6)` has an element in
a new weight at each of `δ = 6, 7, 8`, so a further `D = −1` reducibility bite
at `δ = 9` is expected and is **not** an obstruction; it would be the fourth
rung of that ladder.  Note that Phase B's theorem covers degree 7 only: at
`δ = 9` the pad side is not forced, and `mult_pad = mult_red` there is a
measurement.

## 3. Stopping rules

1. **Validation failure (P1)** → stop; nothing further is measured; report.
2. **`D > 0` at any cell** → halt the sweep; the verification protocol of §4
   takes over; the session ends with `docs/OBSTRUCTION_CANDIDATE.md`.
3. **`mult = 0` at a Phase-B weight** → halt Phase B; certify; report; end.
4. **Memory** → the todo list bounds honesty: a cell whose process is ended by
   the wall-clock or memory bound is recorded as attempted-and-not-reached in
   `results/logs/s43_failed.txt` and named in the report's honest boundary; it
   is never quietly dropped from the denominator.
5. **Budget** → the session stops measuring when the wall clock runs out, banks
   what is banked, and reports the frontier as left.  Coverage fractions in the
   report are always of what *exists*, never of what fits.

## 4. The verification protocol (copied verbatim from the brief)

> `D > 0` — halt the sweep; the verification protocol takes over: `a` both
> routes; `mult_det` and `mult_pad` re-derived at 3× points and a second prime;
> the kernel vector exhibited and shown nonzero at 20 independently built true
> padded-permanent points and zero at 20 determinant pencils; `m_det`
> re-derived by a second, independently written implementation (calibrated on
> the anchors 3, 11, 43); everything into `docs/OBSTRUCTION_CANDIDATE.md`, and
> end the session there. The integrator re-derives before the word is used.

## 5. Deliverables

`results/PREREG_s43.md` (this file), `results/s43_todo.md`,
`results/s43_ledger.md`, `results/s43_per6.md`, `docs/sixrow_close.md`, code
`analysis/wk9_s43_*.py`.  The report ends with the frontier as left and the
bundle head hash.
