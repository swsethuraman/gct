# The six-row frontier: the onset of `I(D_6^{det_4})`, and the obstruction there

Session 41, branch `s41-sixrow`, 2026-09-02.  Clone tip `5aa564b` (ancestry
gate passes; `docs/s40_review.md` and `analysis/wk9_s36_stabred.py` present).
Pre-registration `results/PREREG_s41.md` (commit `4051730`, before any
measurement).  Census `results/sixrow_census.md`; ledger `results/s41_ledger.md`;
Phase 0b `results/s41_per6.md`; validation `results/s41_validation.md`; code
`analysis/wk9_s41_*.py`.  Labels: **proved** / **measured** /
**adopted-from-literature** / **expectation**, as pre-registered.

## 0. Verdict

> **The six-row determinant ideal `I(D_6^{det_4})` is empty at every cell
> reached — `mult_det = a` throughout — so the obstruction cannot yet appear,
> and does not: `D ≤ 0` at every six-row cell, `D = 0` except at three
> reducibility bites (`D = −1`).**  This session raised the reachable frontier
> from `n_χ ≈ 15,500` to `n_χ ≈ 20,000` with a validated in-place kernel route
> and measured **37 new `ℓ = 6` cells** (86 ambient units) at `δ = 7, 8` — the
> first six-row cells ever measured above `δ = 7`, and the first ever above
> `n_χ = 15,500`.  With session 36's inherited cells the six-row record is now
> **90 cells / 195 ambient units** across `δ = 6, 7, 8`, `mult_det = a` at every
> one.  **The six-row onset of the determinant ideal is bracketed `≥ 9` in
> every component reached** — the six-row analogue of the five-row bracket
> `[8, 300]`; nothing in reach forces it lower, and the balanced cells where a
> low onset would most plausibly sit remain above the memory frontier.
>
> On the pad side, `mult_pad = mult_red` at **every** cell — **no
> permanent-specific equation** — including a new `D = −1` reducibility bite,
> `(13,10,6,1,1,1)` at `δ = 8`, the six-row analogue of s36's `(10,8,7,1,1,1)`
> one degree up, certified by (★) on all 28,248 monomials of its exhibited
> vector.  Phase 0b measured `I(D_6^{per_3})_δ = 0` for `δ = 7, 8` on the
> reachable weights, which by Prop. 8 of `docs/transfer_lemma.md` makes
> `mult_pad = mult_red` a **theorem** at 89 of the 90 cells.  The permanent has
> still left no trace.

The obstruction question is open in exactly one direction, and it is the one
the programme has always said matters: **the determinant's six-row ideal has
not switched on.**  Until it does, `D > 0` is arithmetically impossible
(`mult_pad ≤ a` and `mult_det = a` give `D ≤ 0`), so the hunt at `ℓ = 6` is,
first and last, the hunt for the six-row onset.

---

## 1. Why `ℓ = 6`, `δ ≥ 7`, and why the det side is the whole question

Three inherited facts (all proved elsewhere) fix the target.

*The permanent is invisible below `ℓ = 6` and `δ = 7`.*  Washout
(`docs/washout_lemma.md`, Thm 2–3): for `r ≤ 5`, `D_r^{per_3} = Sym^3 C^r`, so
the padded permanent is indistinguishable from `{l·c}` and every `D ≠ 0` cell
is a statement about reducibility versus the determinant, not the permanent.
At `r = 6`, `dim D_6^{per_3} = 50 < 56` (Thm 6), so `P_6 ⊊ R_6` and a
permanent-specific equation becomes *possible*; but by Prop. 8 of
`docs/transfer_lemma.md` it can appear at degree `δ` only where
`I(D_6^{per_3})_δ ≠ 0`, empty through `δ = 6` (Pieri + s37).  So `ℓ = 6`,
`δ ≥ 7` is the first permanent-sensitive corner.

*An obstruction needs the determinant ideal nonzero.*  `mult_pad ≤ a` always,
so `D = mult_pad − mult_det > 0` forces `mult_det < a`.  Session 36 found the
six-row determinant ideal empty at all its reachable cells of `δ = 6, 7`; the
onset degree was unknown entering this session.  **Pinning it is the first job;
the obstruction hunt rides on top of it.**

*The permanent-sensitive region is sharp* (all proved): `a ≥ 1` (BIP silent at
`(3,4)`, `docs/s37_review.md` §2b — the gate is `a ≥ 1`, not `a ≥ 2`); `λ_1 ≥ δ`
for an obstruction (Corollary B of `docs/reducible_ideal.md`:
`λ_1 < δ ⇒ mult_pad = 0`); `6 ≤ ℓ(λ) ≤ 10` (permanent-visible — `ℓ ≥ 6` is where
the permanent *enters*, not a bar to an obstruction at `ℓ ≤ 5`, which is closed
by containment at `ℓ ≤ 4` and by measurement at `ℓ = 5`; corrected s49).  The
onset of the *determinant* ideal is
not restricted by `λ_1 ≥ δ`; the census lists the `λ_1 < δ` cells separately as
onset-eligible-only, and they are the balanced cells, all far above reach.

## 2. Two engineering additions, both validated before use

**The in-place kernel route (`analysis/wk9_s41_kernel.py`).**  Session 36's
frontier `n_χ ≈ 15,500` was set by flint's `nullspace()` holding three `8n_χ²`
copies of the compressed matrix.  Measured this session before anything else
(`VmHWM` after `clear_refs`, random `(n+64)×n` matrices of nullity 3):
`nullspace()` adds 2.04 / 1.96 further copies at `n = 4000 / 8000`;
`rref(inplace=True)` adds 0.76 / 0.62.  Reading the kernel off the rref (pivot
columns found by scanning `≤ a+1` entries per row; one vector per free column)
with the same certificate chain `rank(Agg) ≤ rank_p(M) ≤ rank_Q(M) = n_χ − a`
and the assert `n_χ − rank(Agg) = a` forcing equality, the peak drops from
`≈ 2.4e-8·n_χ²` to `≈ 1.4e-8·n_χ² + 0.4` GB.  **Every kernel vector is
additionally multiplied against the uncompressed sparse raising-operator rows
and asserted to vanish mod `p`** — an exact certificate that the exhibited
vectors are highest-weight mod `p`, independent of the compression.
*(measured)*  The pre-registered frontier `n_χ ≤ 20,000` was confirmed: the two
cells above 15,500 measured this session, `(12,8,3,3,1,1)` at `n_χ = 18,716`
and `(12,9,3,2,1,1)` at `n_χ = 19,985` — the largest reduced kernel ever taken
in the programme — peaked at 4.17 and **4.68 GB**, inside the 6.5 GB budget.

**Validation (`results/s41_validation.md`, P1 — all pass).**  (A) the `l^3 m`
witness through the reduced and unreduced pipelines: `a = 1`, kernel
`∝ (12, −3, 1)`, `mult = 0` (the wrong rule gives `(1, −4, 3)`, `mult = 1`);
`wk8_s30_calib.py` as-is prints `CALIBRATION PASSED`, 41 of 48 World A cells
discriminating.  (B) the in-place route against the exact route on the six s36
validation cells (`δ = 6`, `ℓ = 5`): same `a`, `mult_det`, `mult_pad`, and
**identical kernel span**, both primes.  (C) three banked `ℓ = 6` cells of
`results/s36_ledger.md` — the discriminating `(10,8,7,1,1,1)` (`a = 3`,
`mult_pad = 2 < a`, which must reproduce *as a bite*), plus `(13,8,4,1,1,1)`
and `(13,9,2,2,1,1)` — reproduced by s36's own route **and** by the in-place
route, identical spans, both primes.  (D) the `m_det` anchors `Σ = 3, 11, 43`
at `n = 3`.  The wrong lemma fails B, C and the witness; they passed in every
direction.

## 3. Phase 0 — the census and the arithmetic map

`results/sixrow_census.md`, published before any measurement.  Every `λ ⊢ 28`
(`δ = 7`) and `λ ⊢ 32` (`δ = 8`) with `ℓ(λ) = 6` and `a ≥ 1`.  `a` by **two
independent routes** — Frobenius plethysm `h_δ[h_4]` and a Kostant alternation
`Σ_{w∈S_6} sgn(w)·m(w(λ+ρ)−ρ)` over a dense weight-multiplicity table sharing
no formula with the first — **asserted equal at every one of the 849 cells**;
`N_S` by that table and by an independent generating-function DP, asserted
equal; `m_det` (the symmetric rectangular Kronecker bound) by `wk9_s38_screen`
after its `n = 3` self-test `Σ = 3, 11`.  *(measured, exact)*

- **`δ = 7`:** 258 obstruction-eligible cells (`λ_1 ≥ δ`), 954 units; 58
  reachable at `n_χ ≤ 20,000` (129 units), 37 of them banked by s36.
- **`δ = 8`:** 591 eligible cells, 10,054 units; 65 reachable (273 units), none
  previously measured.
- **The arithmetic route is silent (P2a holds):** `a ≤ m_det` at **every one of
  the 849 cells**, tightest margin `m_det − a = 12` at `(18,2,2,2,2,2)` (`δ=7`).
  So no cell carries a determinant equation by arithmetic alone; wherever
  `I(D_6^{det})` first switches on, it is a **multiplicity drop**
  `mult_det < a ≤ m_det`, invisible to the occurrence screen — the length-5
  finding of s38, confirmed at length 6.
- The `λ_1 < δ` (onset-only) cells are the balanced weights `(6,6,6,6,2,2)`,
  `(7,7,7,7,2,2)`, …; the smallest sits at `n_χ ≈ 91,834` (`δ=7`) and
  `≈ 578,194` (`δ=8`), far beyond reach.  A low balanced onset, if one exists,
  lives here and is unreachable on this container.

## 4. Phase 1 — the sweep

`results/s41_ledger.md`.  Pre-registered order: arithmetic-forced cells first
(none), then `δ = 7` ascending `n_χ` interleaved 3:1 with largest-`a` and
most-balanced probes, then `δ = 8` by the same rule.  Per cell: `a` by kernel
dimension and plethysm (asserted equal); `rank(R) = n_χ − a` asserted; the
χ-obstructed fixed rows asserted to cancel; both sides at `a + 8` true points;
both primes; `mult_red` by (★); one process per cell (so the banked `HWM` is
the cell's own peak); banked and committed before the next cell.

**Result: `mult_det = a` at every measured cell.**  37 new cells (86 units):
15 at `δ = 7` and 22 at `δ = 8`.  Not one determinant rank fell below `a`, at
`a` up to 10.  Combined with s36 the six-row record is **90 cells / 195 ambient
units, `mult_det = a` throughout** — the determinant's six-row ideal is empty
at every reachable weight of `δ = 6, 7, 8`.

**The one new bite (`D = −1`, expected direction, certified).**
`(13,10,6,1,1,1)` at `δ = 8`: `a = 9`, `mult_det = 9 = a` (**det side empty**),
`mult_pad = 8`, so `D = −1`.  Sceptical branch: `3a + 24 = 51` fresh pad points,
seed 907, both primes — `mult_pad = 8` again.  The vanishing HWV was exhibited
(support 28,248 of 140,749 monomials, both primes; `results/s41_cells/`) and
run through the independent symbolic battery of `wk9_s41_bite.py`: it vanishes
at 20 true padded-permanent points **and** at 20 `l·(random cubic)` points, and
is nonzero at 20 generic quartics and 20 `det_4` pencils.  **Every one of its
28,248 monomials satisfies (★)**, so `v ∈ I(X_6)`: **a reducibility equation,
proved** — `mult_red = 8 = mult_pad`.  It is the six-row analogue of s36's
`(10,8,7,1,1,1)` (`δ = 7`), one degree up: the reducibility ideal `I(R_6)` has
gained a degree-8 length-6 generator, and the determinant and permanent are
both untouched by it.  Not an obstruction; `D = −1 ≤ 0`.

**Coverage** (fractions of what *exists*, `λ_1 ≥ δ`, `a ≥ 1`, `ℓ = 6`):

| δ | eligible cells | units | reachable (`n_χ ≤ 20000`) | measured (s36+s41) | units | new s41 | `mult_det < a` | `mult_pad < a` |
|---|---|---|---|---|---|---|---|---|
| 7 | 258 | 954 | 58 | 52 (20%) | 113 (12%) | 15 | 0 | 1 (`(10,8,7,1,1,1)`, s36) |
| 8 | 591 | 10054 | 65 | 22 (4%) | 63 (1%) | 22 | 0 | 1 (`(13,10,6,1,1,1)`, s41) |

Reached in balance up to 16 (`δ=7`) and 20 (`δ=8`), in `a` up to 5 (`δ=7`) and
10 (`δ=8`).  What was *not* reached: every eligible cell with `n_χ > 20,000` —
at `δ = 7` that is 200 of 258 cells (all `a ≥ 6` among them) and at `δ = 8`
526 of 591 (all `a ≥ 11`); and every balanced onset-only cell.  The
representativeness falsifier was exposed as far as the budget allows —
largest-`a` and most-balanced reachable cells interleaved 3:1 as pre-registered
— not further.  The balanced corner (`balance ≤ 8` at `δ = 7`, `≤ 9` at
`δ = 8`) is essentially unreached, and that is where s30/s36's dimension
heuristic would place a first det-side bite if one exists in this range.

## 5. The pad side: still no permanent

Two facts, kept separate as the transfer lemma requires.

**`mult_pad = mult_red` at every measured cell** *(measured)*: the point-based
`mult_pad` equals the point-free `mult_red` (criterion (★)) everywhere, so **no
permanent-specific equation appears in any component reached**, through `δ = 8`.
The only cells with `mult_pad < a` in the whole six-row record are three
reducibility bites — `(4,4,4,4,4,4)` at `δ = 6` (`I_6`), `(10,8,7,1,1,1)` at
`δ = 7`, and `(13,10,6,1,1,1)` at `δ = 8` — each `mult_pad = mult_red`.

**Phase 0b makes it a theorem where it can** *(measured + proved)*.
`I(D_6^{per_3}) ⊂ C[Sym^3 C^6]` is concentrated at length-6 weights, and by
Prop. 8 a gap `mult_pad < mult_red` at degree `δ` requires `I(D_6^{per_3})_δ ≠
0`.  `results/s41_per6.md` measured every length-6 weight `μ ⊢ 3δ` with
`a(μ,δ) ≥ 1` and `n_χ ≤ 6000`: **`I(D_6^{per_3})_7 = 0`** (20 reachable weights)
and **`I(D_6^{per_3})_8 = 0`** (28 reachable weights); with s37's `δ = 6` the
permanent ideal is empty at every reachable weight through `δ = 8`.  Where every
Pieri-transport weight `μ` of a swept cell is measured empty (or has `a(μ) = 0`
outright), `mult_pad = mult_red` is **forced independent of the pad points** — a
theorem given the measurement.  This holds at **89 of the 90** measured cells;
the one exception, `(15,4,4,2,2,1)` at `δ = 7`, has a single transport weight
`(9,4,3,2,2,1)` above the `n_χ = 6000` Phase-0b cap and is covered by the point
measurement alone.

The transfer lemma then carries every `D ≤ 0` here to the true permanent:
`D_P ≤ D_R ≤ 0`.  The permanent can only *erase* an obstruction, and there is
none to erase.

## 6. Honest boundary

- **Proved:** the eligibility constraints (§1); the in-place certificate chain
  and the mod-`p` HWV verification of every exhibited kernel (§2); `v ∈ I(X_6)`
  for the `(13,10,6,1,1,1)` bite by (★) on all 28,248 monomials (§4);
  `mult_pad = mult_red ⇒ D_P ≤ D_R` via transfer; the Phase-0b "forced" cells
  (§5, Prop. 8 given the measurement).
- **Measured, certified one-sidedly (both primes, `rank_p ≤ rank_Q ≤ a`):**
  every `mult_det = a` and `mult_pad = a` in the ledger — each an independence
  certificate at explicit integer points.  `a` by two routes (three at every
  measured cell, counting kernel dimension); `N_S` by two routes.  The one
  `D = −1` cell is exact one-sided the other way: `mult_pad ≤ a − 1` by (★) on
  the exhibited vector, `mult_pad ≥ a − 1` and `mult_det = a` by rank-attaining
  certificates.
- **Measured, one-sided in the other direction:** nothing on the det side.  No
  determinant rank came in below `a`; the sceptical branch fired once, on the
  pad side, and (★) closed it as a reducibility equation.
- **Not measured:** every eligible cell with `n_χ > 20,000`
  (`results/sixrow_census.md`) — 200 of 258 at `δ = 7`, 526 of 591 at `δ = 8`,
  all higher-`a` and all lower-balance cells among them; every `λ_1 < δ`
  balanced onset-only cell (smallest `n_χ ≈ 91,834`); the Phase-0b weights above
  `n_χ = 6000` (7 at `δ = 7`, 63 at `δ = 8`).  Coverage fractions above are of
  what *exists*, not of what fits.
- **Regime and its limits:** the "det side empty" reading is measured only on
  the *peaked* reachable cells (long first row, trailing `1,1,1` or `2,2,2,2`).
  Whether the six-row onset is `[9, …]` low or high is genuinely open; the
  extrapolation from length 5 (onset `[8, 300]`) is across a codimension jump
  (20 → 60) and a change in the determinantal singular locus (20 points → a
  degree-20 curve), so the bracket `≥ 9` is honest and the upper end is
  unpinned in reach.  The five-row cap `cap(4) = 300` (`docs/s40_review.md`)
  does **not** transfer to six rows; no six-row cap theorem exists yet.
- **Post-hoc, labelled:** none of the pre-registered order, points, primes, or
  frontier was changed after the fact.  The in-place route and its `n_χ ≤ 20,000`
  frontier were pre-registered in `results/PREREG_s41.md` §1 and validated in P1
  before any new cell.  The `(13,10,6,1,1,1)` sceptical branch and battery ran
  exactly as §4 of the prereg prescribes.
- **Engineering honesty:** the sweep was interrupted twice by the session
  suspending its background workers; each time the claim queue's PID-aware
  reconcile released the dead owners' claims and the sweep resumed from the
  ledger with no cell lost.  `(12,9,3,2,1,1)` at `n_χ = 19,985` was OOM-killed
  on its first attempt while a Phase-0b worker held ~2.5 GB concurrently
  (recorded in `/root/s41/failed.txt`, the concurrent worker killed by explicit
  PID after read-back — a `pgrep -f` self-match onto the shell wrapper was
  caught by the read-back rule, as it has been in prior sessions), then
  re-measured solo: `mult_det = mult_pad = 5 = a`, peak 4.68 GB.  Above
  `n_χ ≈ 8000` this container is a strict one-cell machine; the ledger's `HWM`
  column records the peak the memory model was validated against.

## 7. What next

1. **The balanced corner is the missing evidence.**  Every reachable cell is
   peaked; the cells where s30/s36's dimension heuristic would first show a
   det-side bite (`balance ≤ 8`) sit at `n_χ > 20,000`.  A larger machine, or a
   second reduction axis (the `λ_5 = 1` jet reduction of `docs/s37_review.md`
   §3, or a further quotient by a within-block symmetry at the balanced
   weights), is what moves this.
2. **A six-row cap theorem.**  The five-row `cap(n)` came from a node count
   (`docs/s40_review.md`); the six-row analogue — the first degree at which the
   Jacobian/nodal family of `D_6^{det_4}` enters the ideal — would bracket the
   onset from above without measurement, exactly as `cap(4) = 300` did at five
   rows.  The natural theory successor; needs no container.
3. **`δ = 9` in reach.**  The Phase-0b degrees and the peaked `δ = 9` cells are
   cheap and extend the bracket a degree at a time; `I(R_6)` gained a generator
   at each of `δ = 6, 7, 8`, and `δ = 9` is the next rung of that ladder.
4. **Do not chase the balanced onset-only cells on this container** — `n_χ ≥
   91,834`; they stand on whatever cap theorem item 2 produces.

*The frontier as left:* the six-row determinant ideal is empty through `δ = 8`
at every reachable weight (onset `≥ 9` in reach), the reduction now reaches
`n_χ ≈ 20,000`, the permanent is still invisible (`mult_pad = mult_red`
everywhere, and `I(D_6^{per_3}) = 0` through `δ = 8` in reach), and `D ≤ 0`
everywhere with three reducibility bites at `δ = 6, 7, 8`.  The obstruction
remains where session 36 left it — waiting on the determinant's six-row ideal
to wake, in a balanced corner this container cannot see.
