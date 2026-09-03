# Closing the six-row region already in reach: the 49 cells, the degree-7 permanent theorem, and the first rung at `δ = 9`

Session 43, branch `s43-sixrow-close`, 2026-09-03.  Clone tip `0c229c1` (gate
passes: `docs/s41_review.md`, `analysis/wk9_s41_kernel.py`,
`results/s41_ledger.md`, `results/sixrow_census.md`, `results/s41_per6.md`,
`docs/brief_wording.md` all present; no session 43 in the repository at clone
time).  Pre-registration `results/PREREG_s43.md`, committed before any
measurement.  Work list `results/s43_todo.md`; ledger `results/s43_ledger.md`;
permanent ideal `results/s43_per6.md`; `δ = 9` census `results/s43_d9census.md`;
validation `results/s43_validation.md`; route cross-check
`results/s43_inject_crosscheck.md`; coverage `results/s43_coverage.md`; code
`analysis/wk9_s43_*.py`.  Labels **proved** / **measured** /
**adopted-from-literature** / **expectation**, as pre-registered.  Vocabulary
per `docs/brief_wording.md`.

## 0. Verdict

> **The reachable six-row region is closed, the permanent has no equation of
> its own in degree 7 — a theorem with no points in it — and the determinant's
> six-row ideal is still empty everywhere the programme can look.**
>
> **Phase A finished its list: all 49 cells.**  With session 36's and session
> 41's, **every one of the 123 obstruction-eligible six-row cells that fits at
> `n_χ ≤ 20,000` is now measured — 123 of 123, 402 ambient units, `mult_det = a`
> at every one.**  There is no cell left inside the frontier: at `δ = 7` and at
> `δ = 8` the reachable set is exhausted, and what remains unmeasured is
> unmeasured because it does not fit, not because time ran out.  Since `D > 0`
> requires `mult_det < a`, no obstruction was possible at any of them, and none
> appeared.
>
> **Phase B closed degree 7.**  The seven length-6 weights `μ ⊢ 21` session 41
> left above its cap were measured, so `I(D_6^{per_3})_7 = 0` at **all 27**
> weights with `a ≥ 1`, outright; by Prop. 8(1) of `docs/transfer_lemma.md`
> this gives `I(P_6)_7 = I(R_6)_7` and `mult_pad = mult_red` at **every** weight
> of degree 7, independent of any pad point.  The scan then carried to `δ = 8`,
> where 81 of the 91 weights are now measured empty.
>
> **Phase C opened `δ = 9`** — a census of 1,079 eligible cells (86,363 units,
> 52 reachable) and **40 of the 52**, `mult_det = a` at every one — and found
> **the fourth rung of the reducibility ladder**: `(17,12,4,1,1,1)` and
> `(16,13,4,1,1,1)`, both `D = −1`, both `mult_pad = mult_red`, both certified
> by (★) on every monomial.  `I(R_6)` now has an element in a new weight at each
> of `δ = 6, 7, 8, 9`, exactly as P4 predicted — and both `δ = 9` cells sit in
> the `(λ_1,λ_2,λ_3,1,1,1)` family that §3 identifies, which is where §3 said to
> look.
>
> The new information on the pad side is quantitative.  Session 41 knew three
> `D = −1` reducibility bites in the whole six-row record.  This session found
> **eight more at `δ = 8` alone, four of them `D = −2`** — the first cells in
> the programme where the reducibility ideal takes two units out of one weight.
> Every one is `mult_pad = mult_red`, certified by (★) monomial by monomial, so
> **still no permanent-specific equation anywhere**; and now that the reachable
> `δ = 8` set is complete, one can say it exactly: **all nine `δ = 8` bites lie
> in the single weight family `(λ_1, λ_2, λ_3, 1, 1, 1)`, and the 32 measured
> `δ = 8` cells outside that family have no pad-side units at all.**

Nothing here moves the obstruction question, and the reason is the one session
41 already gave: `D > 0` needs `mult_det < a`, and the determinant's six-row
ideal has not switched on at any weight this container can reach.  What did
move is the pad side's bookkeeping — degree 7 is now closed by a theorem
instead of a cell-by-cell transport argument — and the map of where the
*reducibility* ideal lives at `δ = 8`.

### The pre-registered predictions, scored

| | prediction (`results/PREREG_s43.md`) | outcome |
|---|---|---|
| P1 | the three banked s41 rows, the `m_det` anchors and the route gate all reproduce | **held** — every field identical, including the discriminating `D = −1` row |
| P2 | **0 of 49** Phase-A cells show `mult_det < a` | **held** — 0 of 49 |
| P3 | all seven remaining `δ = 7` permanent weights empty (`mult = a = 1`); chance of a bite put at ≈ 1 in 6 | **held** — all seven empty |
| P4 | `mult_det = a` and `D ≤ 0` at every `δ = 9` cell reached, with `D = −1` at **zero or one** of them | **half held** — `mult_det = a` and `D ≤ 0` throughout, but **two** `D = −1` cells, not zero or one.  The prediction under-counted the rung; §3's family finding, made after it, is why |

The one prediction that missed, missed in the informative direction: the
`δ = 9` reducibility rung is *wider* than expected, and it sits exactly where
the completed `δ = 8` sweep says it should.

---

## 1. What was to be done, and the list rebuilt from scratch

The brief's Phase A is the 49 cells that fit inside session 41's validated
frontier (`n_χ ≤ 20,000`) and were never measured.  The brief asked for that
list to be **re-derived from `results/sixrow_census.md`**, not taken from
`results/s41_coverage.md`, and for any disagreement to be reported as a
finding.

`analysis/wk9_s43_todo.py` parses the census's two obstruction-eligible tables
(`λ_1 ≥ δ`), takes the cells with an exact `n_χ ≤ 20,000`, and subtracts the
measured ones — the census's own `s36` column, cross-checked against
`results/s36_ledger.md` **and** `results/s36_aone.md` (the `a = 1` cells live
in the second file, which is why a naive check against the ledger alone reports
six spurious differences), plus every row of `results/s41_ledger.md`.  It also
re-derives the census header's own totals and re-checks its `reach 20000` flag
against the raw `n_χ` at all 849 cells.

**Finding: none.**  The re-derived counts agree with `results/s41_coverage.md`
at both degrees and with the census header — 258 cells / 954 units at `δ = 7`,
591 / 10,054 at `δ = 8`; 58 and 65 reachable; 52 and 22 measured; **6 and 43
unmeasured, 49 cells and 226 ambient units in all**, published as
`results/s43_todo.md` ascending in `n_χ`.  That is exactly the brief's number,
independently obtained.

## 2. Validation (P1) — all four parts pass

`results/s43_validation.md`.  Run before the first new cell.

- **Three banked session-41 rows re-measured from scratch**, both primes:
  `(12,10,3,1,1,1)` `δ=7`, `(16,10,3,1,1,1)` `δ=8`, and the discriminating
  `(13,10,6,1,1,1)` `δ=8` (`a = 9`, `mult_det = 9`, `mult_pad = mult_red = 8`,
  `D = −1`).  Every field of every row reproduced identically, down to `N_S`,
  `Stab`, `n_χ`, the row count, the peak (1.46 GB) and the runtime.  A route
  that had lost the true padded-permanent points, or the (★) criterion, returns
  `mult_pad = 9 = a` at the third cell and nowhere else in the list; it did not.
- **`m_det` anchors:** `Σ m_det = 3, 11, 43` at `n = 3`, `δ = 2, 3, 4`.
- **Phase B's driver** reproduced two banked `results/s41_per6.md` rows.
- **The injectivity route** (§4) reproduced the dense route's verdict at three
  banked `a = 1` weights before being used anywhere.

## 3. Phase A — the 49 cells

`results/s43_ledger.md`, ascending in `n_χ`, one process per cell, banked and
committed before the next cell starts.  Per cell: `a` by kernel dimension and by
plethysm (asserted equal); `rank(R) = n_χ − a` asserted; every kernel vector
verified against the uncompressed raising-operator rows; `mult_det` and
`mult_pad` at `a + 8` true points (det pencils `det_4(Σ s_i A_i)`; pad the true
padded-permanent restriction `l(s)·per_3(A(s))`, never `l·(random cubic)`); both
house primes; point-free `mult_red` by (★).  Any `mult < a` on either side got
the independent re-check — `3a + 24` fresh points, seed 907, both primes — and
the vanishing vectors exhibited and run through `analysis/wk9_s41_bite.py`,
**before** the row was banked.

**All 49 cells were measured** — 6 at `δ = 7` (16 units, `n_χ` to 18,801) and
43 at `δ = 8` (210 units, `n_χ` to 19,892), 11.7 CPU-hours in all, largest peak
4.70 GB at the last cell `(16,9,2,2,2,1)`, `n_χ = 19,892`.  With s36 and s41
that closes the reachable set: **123 of 123 eligible cells at `n_χ ≤ 20,000`,
402 ambient units**, and the six-row record is now **139 cells** across
`δ = 6, 7, 8` (plus 24 at `δ = 9` from Phase C).

**Det side: `mult_det = a` at every cell measured.**  No determinant rank fell
below `a` anywhere, at `a` up to 11.  So `D ≤ 0` throughout and no obstruction
was possible at any of them — P2 held exactly as pre-registered (0 of 49), and
for the reason pre-registered: every one of these cells is peaked.

**Pad side: seven new reducibility bites at `δ = 8`, three of them `D = −2`.**
Each has `mult_pad = mult_red`, so each is a *reducibility* equation and not a
permanent one; each vanishing highest-weight vector satisfies (★) on **every one
of its monomials** (an exact certificate that it lies in `I(X_6)`), vanishes at
20 independently built true padded-permanent points and 20 `l·(random cubic)`
points, and is nonzero at 20 generic quartics and 20 determinant pencils.

| δ | λ | a | mult_det | mult_pad | mult_red | D | (★) on |
|---|---|---|---|---|---|---|---|
| 8 | `(13,12,4,1,1,1)` | 3 | 3 | 2 | 2 | −1 | 6,804 / 6,804 monomials |
| 8 | `(13,8,8,1,1,1)` | 3 | 3 | 2 | 2 | −1 | all |
| 8 | `(14,8,7,1,1,1)` | 9 | 9 | 8 | 8 | −1 | all |
| 8 | `(13,9,7,1,1,1)` | 11 | 11 | 10 | 10 | −1 | all |
| 8 | `(11,9,9,1,1,1)` | 3 | 3 | **1** | 1 | **−2** | 85,746 + 73,278, all |
| 8 | `(11,10,8,1,1,1)` | 4 | 4 | **2** | 2 | **−2** | all |
| 8 | `(12,10,7,1,1,1)` | 9 | 9 | **7** | 7 | **−2** | all |
| 8 | `(12,9,8,1,1,1)` | 6 | 6 | **4** | 4 | **−2** | all |

**The family — and now a complete statement of it.**  Every pad-side unit ever
found at `ℓ = 6`, `δ = 7, 8` — s36's `(10,8,7,1,1,1)`, s41's
`(13,10,6,1,1,1)`, and all eight here — sits at a weight of the shape
`(λ_1, λ_2, λ_3, 1, 1, 1)`.  Because the reachable `δ = 8` set is now complete,
this is no longer a selection effect that a wider sweep might dissolve: **of the
65 reachable eligible cells at `δ = 8`, 33 are in that family and 32 are not;
all nine bites are in the family, and the 32 cells outside it have `mult_pad = a`
without exception.**

Inside the family (`λ_1 + λ_2 + λ_3 = 29`), sorted by the spread
`λ_1 − λ_3`, the units concentrate hard at the balanced end:

| λ | spread | a | mult_pad | units |
|---|---|---|---|---|
| `(11,9,9,1,1,1)` | 2 | 3 | 1 | **2** |
| `(11,10,8,1,1,1)` | 3 | 4 | 2 | **2** |
| `(11,11,7,1,1,1)` | 4 | 3 | 3 | 0 |
| `(12,9,8,1,1,1)` | 4 | 6 | 4 | **2** |
| `(12,10,7,1,1,1)` | 5 | 9 | 7 | **2** |
| `(13,8,8,1,1,1)` | 5 | 3 | 2 | 1 |
| `(12,11,6,1,1,1)` | 6 | 6 | 6 | 0 |
| `(13,9,7,1,1,1)` | 6 | 11 | 10 | 1 |
| `(12,12,5,1,1,1)` | 7 | 3 | 3 | 0 |
| `(13,10,6,1,1,1)` | 7 | 9 | 8 | 1 |
| `(14,8,7,1,1,1)` | 7 | 9 | 8 | 1 |
| `(13,12,4,1,1,1)` | 9 | 3 | 2 | 1 |
| the other 21, spread 8–15 | | | | 0 |

Two units appear exactly at the four smallest spreads (2, 3, 4, 5), one unit at
five cells of spread 5–9, none beyond.  But `(11,11,7)` at spread 4 and
`(12,11,6)` at spread 6 are empty while `(12,9,8)` at spread 4 and
`(13,9,7)` at spread 6 bite, and `(13,12,4)` bites at spread 9 — so no single
statistic (spread, balance, `a`, or `λ_2 − λ_3`) separates the two sets.  This
is a **pattern, not a law**, and it is recorded here as one.  It is the sharpest
thing the six-row record has said so far about *where* `I(R_6)` lives, and it is
the natural input to a Kempf-collapsing calculation of `mult_λ C[R_6]_8`, which
would predict these numbers rather than measure them.

## 4. Phase B — `I(D_6^{per_3})_7 = 0`, and what it makes a theorem

`results/s43_per6.md`.  Session 41's Phase 0b measured 20 of the 27 length-6
weights `μ ⊢ 21` with `a(μ,7) ≥ 1`, stopping at `n_χ ≤ 6000`.  All 27 were
re-enumerated here by plethysm and each has `a = 1` (verified, as the brief
asked); the seven unmeasured are exactly the brief's list, at `n_χ` = 6,167,
6,895, 6,982, 8,402, 9,789, 12,564 and **39,921**.

Six were measured by the dense route: `mult = 1 = a` at every one, both primes.

The seventh, `(6,5,4,3,2,1)`, has trivial stabiliser and `n_χ = N_S = 39,921` —
about twice the dense frontier; the in-place rref would need roughly 19 GB
against an 8 GB container.  It was settled by a route pre-registered for exactly
this cell (§2 P3 of the prereg) and validated before use:

> **The injectivity certificate.**  `ker[M ; Ev]` — the reduced
> raising-operator rows stacked with the `a + 8` evaluation rows in the same
> χ-coordinates — is precisely the space of weight-`μ` highest-weight vectors
> vanishing at the points, of dimension `a − mult`.  So `[M;Ev]` is injective
> **iff** `mult = a`.  Full column rank over `F_p` forces it over `Q`, so the
> verdict is one-sided in the same direction as every other "empty" verdict in
> the programme.  Session 42's sparse Wiedemann tool
> (`analysis/wk9_s42_wied.c`) reports `NONSINGULAR` only when the
> Berlekamp–Massey minimal polynomial of the Wiedemann sequence has degree
> exactly `n_χ` with `f(0) ≠ 0` — which proves `M = D₂FᵀD₁FD₂` nonsingular and
> hence `F` injective, with no randomness in that implication.  Memory is
> `O(nnz)`, not `O(n_χ²)`.

At `(6,5,4,3,2,1)`: `[M;Ev]` is `134,212 × 39,921` with 801,854 nonzeros,
`NONSINGULAR` at **both** primes, 482 s, peak **0.15 GB**.  `mult = 1 = a`.

> **Therefore `I(D_6^{per_3})_7 = 0` outright** *(measured, one-sided in the
> exact direction)*, and by Prop. 8(1) of `docs/transfer_lemma.md`
> **`I(P_6)_7 = I(R_6)_7`, so `mult_pad(λ,7) = mult_red(λ,7)` for every `λ` —
> a theorem, with no points in it** *(proved, given the measurement)*.

This removes the one "not forced" cell of `results/s41_coverage.md`
(`(15,4,4,2,2,1)` at `δ = 7`, whose only unmeasured transport weight was
`(9,4,3,2,2,1)`, measured empty here): **every** degree-7 six-row cell in the
record now has `mult_pad = mult_red` by theorem rather than by measurement, and
the transport bookkeeping is no longer needed at that degree.

**The `δ = 8` continuation.**  With degree 7 closed, the same scan was carried
up to `δ = 8`, where session 41 had measured 28 of the 91 length-6 weights; this
session added 53 more (9 dense, 44 by the certificate), so **81 of 91 are
measured, all empty**, and `I(D_6^{per_3})_8 = 0` is within a session's reach.
The
injectivity certificate turns out to prove `mult = a` at **every** `a`, not only
at `a = 1` — the identity `dim ker[M;Ev] = a − mult` does not care about `a` —
and it was validated on that reading against four banked `a = 2, 3` weights
before use.  In all, **13 of 13 agreements with the dense route**
(`results/s43_inject_crosscheck.md`), at 12–15× the speed and a tenth of the
memory.  Every `inject` verdict is marked as such in the `route` column of
`results/s43_per6.md`; none is merged into a dense row.

## 5. Phase C — the first rung at `δ = 9`

`results/s43_d9census.md`: every `λ ⊢ 36` with `ℓ(λ) = 6` and `a ≥ 1` —
**1,079 obstruction-eligible cells (`λ_1 ≥ 9`), 86,363 ambient units**, plus 37
onset-only cells whose smallest `n_χ` bound is 3,208,647 (as at `δ = 7, 8`, the
balanced corner is nowhere near reach).  **52 eligible cells are reachable at
`n_χ ≤ 20,000`** (204 units).  The arithmetic route is silent at all 52
(`a ≤ m_det`, tightest margin 12 at `(26,2,2,2,2,2)`), so as at `δ = 7, 8` any
determinant equation here would be a pure multiplicity drop.

One honest difference from `results/sixrow_census.md`: the census-wide **Kostant
cross-check on `a` is not available at `δ = 9` on this container** — its dense
weight table is a 2.58 GB `int32` array, which does not fit beside a running
cell.  `a` is therefore by plethysm in the census, and again **by kernel
dimension inside every cell process that is measured** (the two routes the
ledger has always used per cell); `N_S` is by the generating-function DP alone.
That is one cross-check fewer than at `δ = 7, 8`, and it is recorded in the
boundary below rather than papered over.

**40 of the 52 reachable cells were measured** (136 units, `n_χ` to 11,435, `a`
to 12, peak 1.66 GB) — the first `δ = 9` six-row cells in the programme.
`mult_det = a` at every one: the determinant's six-row ideal is empty at
`δ = 9` too, on everything reached.

**P4 confirmed: the fourth rung of the reducibility ladder.**  Two cells have
`mult_pad < a`, and both are `mult_pad = mult_red`, so both are reducibility
equations and not permanent ones:

| δ | λ | a | mult_det | mult_pad | mult_red | D | (★) on |
|---|---|---|---|---|---|---|---|
| 9 | `(17,12,4,1,1,1)` | 8 | 8 | 7 | 7 | −1 | all |
| 9 | `(16,13,4,1,1,1)` | 7 | 7 | 6 | 6 | −1 | 11,214 / 11,214 monomials |

Each vanishing highest-weight vector was re-checked at `3a + 24` fresh points on
seed 907 at both primes, exhibited, and run through the symbolic battery: zero
at 20 true padded-permanent points and 20 `l·(random cubic)` points, nonzero at
20 generic quartics and 20 determinant pencils.  So `I(R_6)` has an element in a
new weight at **each** of `δ = 6, 7, 8, 9` — the ladder session 41 described now
has a fourth rung — and both `δ = 9` rungs lie in the `(λ_1,λ_2,λ_3,1,1,1)`
family of §3 (`λ_1 + λ_2 + λ_3 = 33` here).  The family finding predicted where
they would be before they were measured, which is the first time anything in the
six-row record has been predictive.

## 6. Engineering

- **The frontier is unchanged for the dense route** (`n_χ ≤ 20,000`, peak
  `≈ 1.2e-8·n_χ²` measured), and the ledger's `HWM` column again records each
  cell's own peak.  Above `n_χ ≈ 8,000` the container remains a strict one-cell
  machine; the shared guard of `analysis/wk9_s43_guard.py` enforces that with an
  exclusive lock plus a wait on `MemAvailable`, so Phase A and Phase B could run
  concurrently on the two cores without ever holding two large matrices.  The
  guard waits; it never skips.
- **Every long run was launched under `timeout` and `ulimit -v`** with its
  process id written to `results/logs/`, per `docs/brief_wording.md` §1.  One
  duplicate launch of the `(6,5,4,3,2,1)` run (a stray shell argument produced
  two copies) was ended by its recorded id, noted in
  `results/logs/s43_inject_stray.pid`.  Nothing was ended by name matching.
- **Two container suspensions** (at ~04:53 and ~13:20–15:02) terminated every
  worker.  Both times the claim queue's pid-aware reconcile released the dead
  owner's claim and the sweep resumed from the ledger with no cell lost;
  `results/logs/s43_interruptions.txt` records both.
- **The sparse route is the engineering result worth carrying forward.**  It
  reaches `n_χ ≈ 40,000–70,000` at a fifth of a gigabyte, where the dense route
  stops at 20,000 and 4.7 GB — but it answers only the question "is `mult = a`?"
  It cannot produce `mult_red`, which needs the kernel vectors themselves, so it
  does not replace the dense route in the Phase-A ledger; it replaces it exactly
  where the answer wanted is an empty verdict.

## 7. Honest boundary

- **Proved:** the eligibility constraints (`docs/sixrow_frontier.md` §1); the
  in-place certificate chain and the mod-`p` highest-weight verification of
  every exhibited kernel; `v ∈ I(X_6)` by (★) on every monomial for each of the
  ten new bites; `mult_pad = mult_red ⇒ D_P ≤ D_R` via transfer; and — the
  session's one new theorem — `mult_pad = mult_red` at **every** weight of
  degree 7, from `I(D_6^{per_3})_7 = 0` and Prop. 8(1).
- **Measured, certified one-sidedly** (`rank_p ≤ rank_Q ≤ a`): every
  `mult_det = a` and `mult_pad = a` in the ledger, each an independence
  certificate at explicit integer points; every `mult = a` in
  `results/s43_per6.md`, whether by the dense route or by the injectivity
  certificate.  `a` by two routes at every cell.
- **Measured, one-sided the other way:** the ten bites (eight at `δ = 8`, two
  at `δ = 9`) — `mult_pad ≤ a − k` by
  (★) on the exhibited vectors, `mult_pad ≥ a − k` by rank-attaining
  certificates at `3a + 24` fresh points on a second seed and both primes.
  These are **mod-`p` vectors**; as at `(13,10,6,1,1,1)` in session 41, an exact
  integer lift (session 42's `analysis/wk9_s42_lift.py`) is what would turn
  `mult_red ≤ a − k` from measured into proved, and it was **not** run here for
  want of time.  The integrator should expect to run it before the word
  "generator" is used of any of them.
- **Not measured:** every eligible cell with `n_χ > 20,000` — 200 of 258 at
  `δ = 7` and 526 of 591 at `δ = 8`, and *all* of the balanced corner
  (`balance ≤ 8` at `δ = 7`, `≤ 9` at `δ = 8`), which is where s30/s36's
  dimension heuristic would put a first det-side bite; every `λ_1 < δ`
  onset-only cell at all three degrees; the 10 remaining length-6 weights of
  `I(D_6^{per_3})_8`; and 12 of the 52 reachable `δ = 9` cells.  Inside the
  frontier, by contrast, **nothing is left**: 123 of 123.  Coverage fractions in
  `results/s43_coverage.md` are of what *exists*, never of what fits.
- **Regime, and the limit of the reading.**  Everything measured this session is
  peaked — at `δ = 7` the new cells have balance 12–15, at `δ = 8` balance
  10–19, at `δ = 9` balance 15–24.  The det-side verdict therefore says what
  session 41's said, on more cells and no new kind of cell: *no six-row
  determinant equation occurs at any measured cell of degree ≤ 9.*  It is not
  evidence about the balanced corner, and the report does not offer it as such.
  The `δ = 9` rung extends the degree range of that statement by one; it does
  not extend the bracket's credibility, because the cells that would test it are
  not in reach.
- **One cross-check fewer at `δ = 9`:** the census-wide Kostant alternation on
  `a` (§5).  `a` is still two-route at every *measured* cell.
- **One error found and corrected, in full:** the `δ = 8` Phase-B driver passed
  the literal `1` where the weight's `a` belongs, so 21 `a ≥ 2` rows were banked
  with a spurious `units = a − 1`.  It was caught by a status check on the
  commit log, the 21 rows were removed rather than edited, the call site was
  fixed, and all 21 weights were re-measured from scratch at the pre-registered
  `a + 8` points (all `mult = a`).  `results/s43_bookkeeping_correction.md` sets
  out what the original certificates did and did not prove — the verdict
  `mult = a` was right at all 21, only the recorded number was wrong — and why
  the thirteen-weight cross-check missed it (it called the routine directly, not
  through the driver).  No Phase-A, `δ = 7`, or `a = 1` row was affected.
- **Post-hoc, labelled.**  Two things were decided after the prereg and are
  flagged as such: (i) the `a ≥ 2` extension of the injectivity route — the
  prereg scoped it to `a = 1`; the identity `dim ker[M;Ev] = a − mult` makes it
  valid at any `a`, and it was validated against four banked `a = 2, 3` weights
  before any new use, with every such row marked `inject`; (ii) running the
  `δ = 8` Phase-B scan by that route rather than the dense one, for the same
  reason.  Neither touches a Phase-A row.  The pre-registered order, points,
  primes, seeds and frontier were not changed.

## 8. What next

1. **Lift the ten new bites.**  Session 42's integer lift at each turns
   `mult_red ≤ a − k` from measured into proved, exactly as the integrator did
   for `(13,10,6,1,1,1)`.  Cheap, and it is what the `D = −2` cells need before
   anyone calls them two independent equations.
2. **Close `I(D_6^{per_3})_8`.**  81 of 91 weights are already empty; the ten
   left are a couple of hours by the injectivity route, and they would make
   `mult_pad = mult_red` a theorem at degree 8 too — which is where every
   pad-side bite in the record actually lives.  This is the cheapest theorem
   available to the next session.
3. **Use the sparse route on the det side above the frontier.**  It answers "is
   `mult_det = a`?" at `n_χ` several times the dense frontier for a fifth of a
   gigabyte.  That does not by itself reach the balanced corner (the smallest
   balanced onset-only cell is `n_χ ≈ 91,834`), but it puts a large band of
   eligible cells at `20,000 < n_χ < 70,000` — including much lower balance than
   anything measured so far — inside reach for the first time.  **This is the
   cheapest way to test the balanced regime that the programme has had**, and it
   is the natural Phase A of the next session.
4. **A six-row cap theorem** remains the theory successor, unchanged from
   session 41's item 2, and needs no container.

## 9. The frontier as left

- **The reachable six-row region is exhausted.**  Every obstruction-eligible
  cell with `ℓ(λ) = 6`, `a ≥ 1`, `λ_1 ≥ δ` and an exact `n_χ ≤ 20,000` is
  measured: **123 of 123 at `δ = 7, 8`** (402 ambient units), plus 40 of the 52
  at `δ = 9`.  The frontier is now a memory bound, not a queue.
- **The determinant's six-row ideal has still not switched on** at any weight
  the programme can reach, at `δ = 6, 7, 8, 9`; the balanced corner where it
  plausibly first does is unreached and will stay so on this container by the
  dense route.
- **`I(D_6^{per_3})_7 = 0` outright**, so `mult_pad = mult_red` in every weight
  of degree 7 is a theorem; at `δ = 8`, 81 of 91 weights are measured empty and
  the same theorem is one short session away.
- **`I(R_6)` has an element in a new weight at each of `δ = 6, 7, 8, 9`**, and
  at `δ = 8` — where the reachable set is complete — every one of them lies in
  the family `(λ_1, λ_2, λ_3, 1, 1, 1)`, with two units at the four most
  balanced and none at all outside the family.
- **The permanent has still left no trace:** `mult_pad = mult_red` at every cell
  ever measured, now by theorem at degree 7 and by measurement elsewhere.
- **New capability:** the sparse injectivity certificate answers "is
  `mult = a`?" at `n_χ ≈ 40,000–77,000` in a fifth of a gigabyte, three to four
  times past the dense frontier.  It cannot produce `mult_red`, so it does not
  replace the ledger's route; it is the tool for the det-side question above the
  frontier, and that is the cheapest route to the balanced regime the programme
  has ever had.

*Session 43 is delivered by git bundle `sixrowclose.bundle`, single ref
`s43-sixrow-close`, 187 commits on `0c229c1`.  The branch history was rewritten
once, at the end, to keep the exhibited vanishing vectors out of the delivered
pack in uncompressed form (`results/s43_bookkeeping_correction.md`, second
note); the head hash is reported with the bundle.*
