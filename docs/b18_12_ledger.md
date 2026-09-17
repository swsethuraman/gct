# B18-12 — Evidence ledger and next decisions

**Slot:** 12 (evidence ledger; stays open across batch 18)
**Worktree:** `work/batch15_workers/B15-12`
**Opened:** 2026-09-15
**Starting commit (recorded before any write):**

```
git rev-parse HEAD          761e0e7e17a3d6091670e3774281a2bfcd97aa99
git rev-parse HEAD^{tree}   67f8d12616a6323644410fba40829e6584e7e6bd
```

No other git command has been or will be run by this slot.

## 0. Plain terms

This ledger exists so that a *finished session* is never read as a *finished
proof*. It keeps six things in separate boxes: what the reviewer (slot 10) has
actually accepted; what is merely plausible and who is leaning on it; the exact
numbers per cell; which slot is gated on which; what has been priced versus what
has been spent; and each slot's completion state.

**State at opening.** No batch-18 slot has written anything to disk. Across all
twelve worktrees there is no `docs/b18_*`, `analysis/b18_*` or `results/b18_*`
artifact (checked 2026-09-15, before this file was created). The only batch-18
research input is the external v1 report of slot 01, which is **unreviewed**.
Slot 10 has not ruled on anything. Therefore, as of this opening:

- **Reviewed facts of batch 18: none.** The reviewed base is B15–B17 only.
- **Positive gaps: none.** Unchanged since batch 15.
- **Nominated cells: none.** Slot 06 has not reported.
- **Chain status:** link 1 (06 selects) not started; links 2–5 (02 carries,
  03 certifies `b`, `B`; 04 produces `r`; 09 assembles) cannot start.

The honest one-line summary at opening is exactly the one the assignment
anticipated: *no cell is nominated and the chain has no second link.*

**State at last update (17:05).** Slot 10's review is partially on disk and has
accepted, claim by claim, the v1 report's closure, dimension and degree-bound
claims (`dim D45 = 50`, `dim R135 = 39`, a five-row separating equation exists in
degree at most `4^49`), and rejected the implication that `deg P(D45)` is the only
obstruction (§2a). Its rulings on the aggregate Claim 5.1, the ceilings, and the
release gates for 03/04/09 are not yet written. Slot 01's revision is partially on
disk with a new rank certificate. **The one-line summary is unchanged:** reviewed
facts now exist in batch 18, but every one of them is about existence or
dimension; none names a cell, an `s`, a `b`, an `r`, or a gap. The chain still has
no first link.

## 1. Inputs read, with provenance

| Input | Path (relative to `Claude_Handover_B15_B18/` unless stated) | Role |
|---|---|---|
| Preamble | `batch18_launch/B18_PREAMBLE.md` | conventions, rejected results, rules of inference |
| Revised board | `BATCH18_REVISED_BOARD.md` | slot roles, gates, success criteria |
| Launch note | `batch18_launch/LAUNCH.md` | which slots launched, standing limits |
| Slot prompts | `batch18_launch/B18-01,02,05,06,10,12.md` | per-slot deliverables and gates |
| Slot 01 v1 report | `batch18_launch/b18_01_report_v1.md` | **unreviewed** research input; SHA256 `d03d5c976405a603abc8831ac20be3673afa2a0117dc31cd2523a58de29fc60c` |
| B15–B17 summary | `SUMMARY_B15_B17.md` | accepted base |
| Prelaunch / start | `B18_PRELAUNCH.md`, `START_HERE.md` | lease state, worktree rules |
| B17 reviewer decisions | `work/batch15_workers/B15-11/docs/b17_11_supplement02.md`, `b17_11_supplement04_08.md` | what B17-02/04/08 actually established |
| B17-12 closeout | `work/batch15_workers/B15-12/docs/b17_12_closeout.md` | previous ledger, exact cell table |
| Slot 10 review (partial) | `work/batch15_workers/B15-10/docs/b18_10_review.md` | reviewer decisions, §§0–2 only at time of reading; hash in §7 |
| Slot 01 revision (partial) | `work/batch15_workers/B15-01/docs/b18_01_report.md`, `analysis/b18_01_rank_certificate.py`, `results/b18_01/` | §§0–2 only; certificate present, unreplayed here |
| Slot 02 report (partial) | `work/batch15_workers/B15-02/docs/b18_02_report.md` | §§0–1 only |
| B17 lease state | `Batch17/LEASES.json`, `Batch17/NOT_TRIGGERED.json` | no active lease; 09/10 NOT_TRIGGERED in B17 |

Everything below that is not marked **B17-ACCEPTED** or **REVIEWED (slot 10)** is
either a hypothesis or a record of an unreviewed claim.

## 2. Reviewed facts

### 2a. Batch-18 decisions by slot 10

Source: `B15-10/docs/b18_10_review.md`, **partial on disk** (206 lines, SHA256
`0a512384bb12124160285a8b5c449637413411e7a5a688155c3c461af353521f`, unchanged from
16:09 to 17:04 on 2026-09-15). Its §§1–2 (certificate replays; geometry and degree
bound) are written; its announced §§3–7 (Claim 5.1 and every regime-level sentence
drawn from it; ceilings and missing theorems; decision ledger; comparison with the
board intake; release-gate position for 03/04/09) are **not on disk**. The object
reviewed is the **v1** report, not the slot-01 revision. Decisions below are the
reviewer's own words as written; they are not final until the review's own §5
ledger closes.

| # | Claim (v1 numbering) | Slot 10 decision on disk | Reviewer basis |
|---|---|---|---|
| 1.1 | Zariski = Euclidean closure on constructible sets | ACCEPTED | standard |
| 1.2 | `D45` closed cone, both closures agree; `R135` Zariski closed | ACCEPTED | base-point-free multiplication map |
| 1.3 | `D_pad,5 = R135` in either topology | ACCEPTED | 1.1–1.2 + accepted B17-01-A |
| 1.4 | B17-03 restriction/kernel identification | ACCEPTED as adopted | read B17-03 Lemmas 1–2 and B17-11 03-A; no convention drift found |
| 2.1 | some degree has `I(D45)_d` not inside `I(R135)_d` | ACCEPTED | B17-11 01-C |
| 2.2 | such a degree has a five-row `lambda` with `K_det` not inside `K_pad` | ACCEPTED | highest-weight argument; `ell <= 4` excluded by 03-C |
| 2.3 | this gives **no** sign for `D` | ACCEPTED ("the most important correct sentence in the report") | two-lines-in-a-plane counterexample |
| 2.4 | if also `K_pad` inside `K_det` then `D >= 1` | ACCEPTED | trivial |
| A | point/variety separation in degree `<= deg Y` | ACCEPTED | edge case `k = m-1` checked |
| B | `deg Y <= D^{dim Y}` | ACCEPTED, pointer corrected to Fulton Ex. 8.4.6 / Thm 12.3 | refined Bézout is real and correctly stated |
| C | `dim D45 <= 50` | ACCEPTED | stabiliser Lie algebra nullity 1 at the point (80 eqns, 32 unknowns); kernel of Jacobian = 30; upper semicontinuity |
| 4.1 | `dim D45 = 50` | ACCEPTED, and lower half upgraded to PROVED over `Q` | exact rational rank 50 at the report's point and at an independent random point (seed 20260915), plus two primes; controls replayed |
| 4.2 | `dim R135 = 39` | ACCEPTED | exact rank 39 of a 40 x 70 Jacobian; UFD fibre argument checked |
| E | five-row separating equation exists with `d <= 4^49` | ACCEPTED (modulo the standard citation); interfaces of A, B, C, 1.4, 2.2 checked; global polynomiality and closure validity fine | — |
| §3.5 / plain-terms (1) | "`deg P(D45)` is the only quantity standing between this and a usable bound" | **REJECTED as an implication** | Lemma A is only a set-theoretic cut-out bound; four-variable control: Lemma B gives `4^34 ≈ 2.9e20` against LLV's actual component degrees 320, 2508, 136512, 38475, 320112, an overshoot of about fifteen orders of magnitude. The obstruction is the absence of any handle on `I(D45)`, as v1 §7.1 (a)–(c) itself lists. |
| 1.5 (reviewer's) | Weyl ratio bound used by Claim 5.1 | ACCEPTED (elementary) | six shapes checked |
| 5.1 and its regime-level readings | — | **NOT YET ON DISK** | review §3 announced, absent |
| 6.1, 6.2, 6.3, §7 missing theorems | — | **NOT YET ON DISK** | review §4 announced, absent |
| release gate for 03, 04, 09 | — | **NOT YET ON DISK** | review §7 announced, absent |

Reviewer's hypothesis flag, carried here: which of the five LLV components is the
linear 4x4 determinantal one was not verified; the calibration holds for any of
them.

**What this changes operationally: nothing.** Every accepted line is about
existence and dimension; none names a cell, an `s`, a `b`, an `r`, or a gap. The
board's "Intake of the first Slot 01 report" remains an *integrator* reading; where
slot 10 and the intake differ (the intake says `dim D45 = 50` "requires the
producer's modular rank certificate"; slot 10 replayed it exactly over `Q` and
accepted it), slot 10 governs.

### 2b. Accepted base inherited from B15–B17 (B17-ACCEPTED, per B17 intake and the B17-11 supplements)

Only the items the batch-18 chain actually consumes are listed. Each line says what
was accepted and, in italics, what it does **not** give.

| Ref | Accepted statement | Does not give |
|---|---|---|
| B17-01 | Actual five-variable restrictions of `z·per3` are dense in five-variable cubics; `l·C` with `C` a smooth cubic threefold lies outside the five-variable det4 pencil coefficient closure `D45`. An actual padding point `F*` is certified (density rank 35, smoothness rank 210, frame minor 2562). | *no degree, no partition, no numerical `B`, no gap* |
| B17-03 | For every degree and every `lambda` of length at most 4, `K_det` is contained in `K_pad`, hence `D <= 0`. `m_pad = 0` for length > 10. Restriction identifies ordinary-coefficient highest-weight spaces across `r <= 16`. | *nothing about lengths 5–10 beyond "that is where any gap must be"* |
| B17-02 (as fixed by supplement02) | Arc `det = Q0 + t Q1 + t^2 Q2` in sixteen independent coordinates is a genuine polynomial boundary arc. With full-stabilizer source `M_lambda`, `s = dim M_lambda` (symmetric rectangular Kronecker, transposition included), and forbidden-weight projection `C` of rank at least `b`: `m_det <= min(a, s - b)`. Original-entry diagonal arcs give zero forbidden projection in every degree. | *necessary-extension condition only; **no numerical `b >= 1` in any cell**; not an exact multiplicity formula* |
| B17-08 (as fixed by supplement04_08) | Five-row actual padding multiplicity equals the rank of the coefficient pullback along `(l, C) -> lC`. Product-target multiplicity `T` is a ceiling; `U = min(a, T)`. Crossing needs `b >= b_required = max(0, s - U + 1)` when `1 <= U <= a`. Polynomial multiples of the nine-row E24 generator have no types with at most 8 rows in any degree. | *no finite family nominated; no source or projection rank computed; the E24 exclusion is for that generation route only* |
| B17-04 | All eleven external candidates match the accepted global basis. Restriction rank on the eleven-equation space is at least 9 (exact actual-padding minor) and at most 10 (known global kernel `kappa`). | *exact 9 vs 10 open; second kernel vector `w` is sample-only; this is not full padding multiplicity; the cell is excluded regardless* |
| B17-05, 06, 07 | Accepted within stated scope (E24·A2 image 5 at d = 26; signed matching-binomial independence criterion and `K_d` capacity; conormal multidegree specialization with `delta7(det5) = 280`). | *none feeds the chain directly; `K_d` is capacity not multiplicity; `delta7(per3)` uncomputed* |
| B16 | In the four cells of §4, `m_pad <= 288` (source argument) against `m_det = 418`, and similarly in the smaller cells; explicit degree-23 separator; eleven tail-19 equations lift to degree 27. | *these cells are excluded; the separator is geometric separation, not a gap* |
| B15 | Global Hessian-divisibility identities certify determinant equations on the entire closure; `(21,2^7)` tail: `a = 533, m_det = 529, i = 4`; `(19,2^8)` tail: `a = 429, m_det = 418, i = 11`, padding floor 243. | *no positive gap* |

Two rejections in force (preamble): the `MN = F·I4` membership criterion, and the
use of four-variable determinantal-surface literature as a shortcut.

## 3. Hypotheses: plausible, unproved, and who relies on them

"Relied on by" names the slot whose plan would change if the hypothesis fell.
**None of these is a fact.** Where the v1 report labels something PROVED, that label
is the *producer's*, not the reviewer's.

| ID | Hypothesis | Source | Producer label | Relied on by | Ledger note |
|---|---|---|---|---|---|
| H1a | `dim D45 <= 50` (stabilizer computation, Lemma C) | v1 §3.3 | PROVED | Theorem E exponent (H2) | **Moved to §2a: ACCEPTED by slot 10** (on-disk, review incomplete). |
| H1b | `dim D45 >= 50` | v1 §4 | MEASURED | Claim 5.1 (H3) needs only `dim D45 >= 40` | v1's own certificate never existed on disk (confirmed by the slot-01 revision §0). Slot 10 replayed the rank independently, exactly over `Q`, at two points: **moved to §2a, ACCEPTED**. Separately, the slot-01 revision has delivered its own certificate (`analysis/b18_01_rank_certificate.py`, `results/b18_01/rank_certificate.json`: rational rank 50 of `J(B)`, rank-30 symmetry matrix `T(B)` with `T·J = 0`, two points, negative controls). Not replayed by this ledger; its upper half needs `T·J = 0` on a dense set, which is Lemma C's invariance argument, not the one-point check. |
| H1 | `dim D45 = 50` exactly | v1 Claim 4.1 | PROVED | v1 §5, §7 narrative | **Moved to §2a: ACCEPTED by slot 10.** |
| H2 | A five-row separating equation exists in degree `d <= 4^49` (Theorem E) | v1 §3.4 | PROVED modulo citation | nobody operationally; strategic only | **Moved to §2a: ACCEPTED by slot 10** modulo the standard citation, pointer corrected. The companion claim that `deg P(D45)` is the *only* obstruction is REJECTED. Not a search budget. |
| H3 | For all large `d`, the `dim S_lambda(C^5)`-weighted sum of `D(d, lambda)` over five-row cells is negative (Claim 5.1) | v1 §5 | PROVED (aggregate) | v1's recommendation to move the `D > 0` hunt to 6–10 rows; **slot 06 is at risk of leaning on it** | Aggregate only, `d_0` non-effective, depends on H1b. Board: does not exclude any individual five-row cell, does not predict that screens fail, does not justify abandoning five rows. |
| H4 | `m_det <= g((d^4),(d^4),lambda)`, ordinary rectangular Kronecker (Claim 6.1) | v1 §6.2 | PROVED | none new | Weaker than the accepted symmetric `s` (`s <= g`), so harmless as a bound, but **must not be substituted for `s` in `b_required`**. |
| H5 | Five-row `U(d, lambda)` in explicit Pieri x plethysm form (Claim 6.2) | v1 §6.2 | PROVED | v1's proposed screen | Same object as B17-08's `T`, clipped by `a`. Fine if it matches B17-08 exactly; slot 10 to confirm the identification. |
| H6 | The ruledness argument cannot be made effective; the degree must come from the determinant side | v1 §7.1 | ASSESSED | slot 07 planning | Argument, not theorem. |
| H7 | In some five-row (or 6–10-row) cell, the B17-02 arc has forbidden projection of rank `b >= b_required` | programme goal | — | **slots 03, 04, 09 entirely** | **No evidence exists.** B17: "no useful numerical `b` is known"; the degree-7 screen found no symmetry-only `B < U` witness among 31 eligible shapes. |
| H8 | Some cell has `U > s` (so `b_required = 0`) or `U > B` for a cheap `b` | v1 §9 test; slot 06 remit | — | slot 06 | Unknown. A count of such cells would be *headroom*, not a candidate (v1 §9 says so itself). |
| H9 | B17-04's candidate second kernel vector `w = (216, -212, 64, 0, 0, -1, 1, 1, 13, 4, 2)` is a global kernel vector (rank exactly 9) | B17-04 | sample-only | slot 05 | Sampled zero; ceiling only until a global Psi identity is proved. |
| H10 | Constrained Cayley identities retain rigidity (constrained rank at most 6) | Capelli/Cayley packet | producer-verified only | slot 08 | Expanded repair shows unconstrained rank is too weak (rank 28 is not a universal floor). |
| H11 | Leal–Lozano Huerta–Vite degree 320112 for the four-variable component bears on `deg P(D45)` | board intake | literature | none | Control only. Different variety (surfaces in `P^3`, a divisor). Slot 10 used the five LLV degrees as a calibration of Lemma B's looseness (§2a). |
| H12 | **Weight lemma** (slot 02): on every full-`H` invariant in `S_lambda W`, the `gamma`-weight of an adapted-coordinate monomial is `2d - (number of skew factors v)`; weights lie in `[-d, 2d]`; the forbidden range `k > 2d` is empty; `C` is exactly the projection onto skew-degree `>= 2d + 1` | slot 02 rev, §0 summary (§4 body not yet on disk) | PROVED (producer) | slot 03's forbidden projection; slot 02's pricing | Unreviewed. Ledger sanity check (not a review): torus invariance forces row-1 and column-1 index counts each equal to `d`, so `#r = #c`, `#S = 2d + #a - #v`, and weight `= #S - #a = 2d - #v`; consistent. Whether the adapted-coordinate mixing inside the `3x3` block preserves that count is for slot 10. |
| H13 | Explicit conversion of `M_lambda` into adapted coordinates is a **cost barrier in every cell of interest**; a basis of `M_lambda` and a rank floor `b` can instead be certified by exact modular evaluation without expanding any polynomial, and this is priced | slot 02 rev, §0 (§5 body not yet on disk) | priced (producer) | slot 03 entirely; link 2 of the chain | **A price is not measured feasibility.** No number is on disk yet. If the barrier holds and the modular route is the only one, slot 03's `b` will be a modular rank floor, which is a valid lower bound on `b` only when the evaluation points are actual and the matrix is exact. |
| H14 | `d = 2` control: all partitions of 8 with at most five rows, construction checked against the character formula for `s` and the weight lemma; every five-row cell at `d = 2` has `a = 0` | slot 02 rev, §0 (§6 body not yet on disk) | MEASURED (producer), method validation | nobody | `a = 0` for five-row cells at `d = 2` is immediate: `Sym^2(Sym^4 C^5) = S_(8) + S_(6,2) + S_(4,4)`, all with at most two rows (ledger check). So this control validates the method only and cannot be a candidate, exactly as the producer says. |

**Rejected, not hypotheses:** v1 §6.1's "`F` in `D45` iff `MN = F·I4`" (two-line
counterexample `M = l·I4`, `N = C·I4`); slot 01's revision must withdraw it.

## 4. Exact cells

Conventions (preamble): ordinary coefficients `c_alpha = [x^alpha] F`; `s` is the
**symmetric** rectangular Kronecker coefficient with rectangle `(d,d,d,d)`,
transposition included; `U = min(a, T)` with `T` the product-map target
multiplicity; `B = min(a, s - b)` only with a certified `b`;
`b_required = max(0, s - U + 1)`.

### 4a. Cells with exact data (all ten are EXCLUDED for a positive gap)

These are the ten explicitly excluded cells. `i_det` is a certified global ideal
floor (equations valid on the whole determinant closure), so `m_det <= a - i_det`
and `D <= U - (a - i_det)`; that bound is negative in every row. The "padding
ceiling" column is the reviewed source ceiling, already at or below `a`, so it is
the clipped `U`.

| d | lambda | a | i_det (floor) | m_det (exact where known) | U | s | b | b_required | D upper | status |
|---|---|---:|---:|---:|---:|---|---|---|---:|---|
| 23 | (61,15,2^8) | 189 | 1 | 188 | 158 | unknown | 0 known | unknown | -30 | EXCLUDED (B16) |
| 25 | (67,17,2^8) | 294 | 4 | 290 | 218 | unknown | 0 known | unknown | -72 | EXCLUDED (B16) |
| 26 | (71,17,2^8) | 294 | 4 | 290 | 218 | unknown | 0 known | unknown | -72 | EXCLUDED (B16) |
| 27 | (73,19,2^8) | 429 | 11 | 418 | 288 | unknown | 0 known | unknown | -130 | EXCLUDED (B16; padding floor 243, so D in [-175, -130]) |
| 23 | (59,17,2^8) | 292 | 2 | unknown (<= 290) | 218 | unknown | 0 known | unknown | -72 | EXCLUDED (B17 screen) |
| 24 | (63,17,2^8) | 293 | 3 | unknown (<= 290) | 218 | unknown | 0 known | unknown | -72 | EXCLUDED (B17 screen) |
| 23 | (57,19,2^8) | 419 | 4 | unknown (<= 415) | 288 | unknown | 0 known | unknown | -127 | EXCLUDED (B17 screen) |
| 24 | (61,19,2^8) | 424 | 7 | unknown (<= 417) | 288 | unknown | 0 known | unknown | -129 | EXCLUDED (B17 screen) |
| 25 | (65,19,2^8) | 427 | 9 | unknown (<= 418) | 288 | unknown | 0 known | unknown | -130 | EXCLUDED (B17 screen) |
| 26 | (69,19,2^8) | 428 | 10 | unknown (<= 418) | 288 | unknown | 0 known | unknown | -130 | EXCLUDED (B17 screen) |

The B17-screen first parts are `4d - t - 16` with `t = 17` or `19`, as recorded in
the summary's `lambda = (4d - t - 16, t, 2^8)`; they are written out here so nobody
has to re-derive them. **These rows are closed. Do not rank-hunt here.** Their
exclusion is by exact determinant floors against a reviewed padding ceiling; it is
not a symmetry-screen result and does not depend on `s` or `b`.

### 4b. Cells nominated in batch 18

| d | lambda | a | s | U | b | b_required | padding evidence | carrier cost | eval cost | nominated by | reviewed by 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| — | (none) | | | | | | | | | slot 06 has not reported | — |

**No cell is nominated.** No cell anywhere in the programme has a certified
`b >= 1`, and no cell has a recorded exact `s` in the inputs read here. The B17-08
degree-7 screen (114 shapes, 31 eligible) computed symmetry-only data and found no
`B < U` witness with `b = 0`; its per-cell numbers live in that slot's screen
report and were not re-extracted for this ledger. That screen excluded **only**
"`s <= U`-crossing without boundary loss, at degree 7, in those 31 shapes"; it did
not exclude boundary improvements or other degree-7 cells.

### 4c. Regime facts that constrain where a cell can be

- Length at most 4: `D <= 0` in every degree (B17-03, accepted). Closed.
- Length 5: geometric separation exists in some cell (B17-01 + B17-03, accepted);
  degree unknown; v1 claims `d <= 4^49` (H2, unreviewed). Gap sign unknown cell by
  cell; aggregate negativity claimed (H3, unreviewed, aggregate only).
- Lengths 6–10: no theorem either way. The five-variable density theorem does
  **not** apply; the correct padding ceiling is the honest `r`-variable image of
  `z·per3` (B17-08 / board).
- Length above 10: `m_pad = 0` (B17-03, accepted). Closed.

## 5. Prerequisites and gates

| Slot | Gated on | Gate met? | Notes |
|---|---|---|---|
| 01 (revise) | v1 report + board intake | yes, launched | Must deliver the H1b certificate to disk or downgrade Claim 4.1 to an inequality. |
| 02 (carrier, theory) | nothing for theory; slot 06 selection **and** slot 10 approval of definitions and cost for any candidate computation | theory: yes; computation: **no** | Heavy-eligible but no lease. |
| 03 (certify `b`, `B`) | certified carrier from 02 with exact `s`; explicit resource cap; slot 10 review | **no** | NOT_TRIGGERED. |
| 04 (produce `r`) | a reviewed cell with `B < U`; reviewed bound and circuit/evaluation costs | **no** | NOT_TRIGGERED. |
| 05 (rank 9 or 10) | B17-04 report + supplement04_08; one priced bounded attempt | yes, launched | Result cannot revive the cell. |
| 06 (select cells) | B15–B17 intake | yes, launched | Any new finite screen must list cells, range and cap in the report before running. |
| 07 (geometric equation) | slot 01 revision supplying a concrete construction that survives slot 10 | **no** | Second wave, conditional. v1 supplies no surviving construction (its incidence criterion is rejected; Hessian route argued not to transfer). |
| 08 (constrained Cayley) | capacity remaining after the chain, and reviewer justification | **no** | Optional, lowest priority. |
| 09 (assemble certificate) | an actual `r > B` from 03/04 or another reviewed route | **no** | NOT_TRIGGERED. |
| 10 (review) | v1 report, read before any opinion of it | yes, launched | Then stands as release gate for 03, 04, 09. |
| 11 (delivery) | — | complete | Commit work done per LAUNCH.md. |
| 12 (this ledger) | all of the above as they report | open | — |

**Rule for later launches (LAUNCH.md):** a gated slot's worktree needs its batch-18
`.gitattributes` / `.gitignore` rules committed before it writes anything. Only 01,
02, 05, 06, 10, 12 have them. 03, 04, 07, 08, 09 do not.

## 6. Costs and leases

Standing limits (LAUNCH.md, Batch17/LEASES.json): default pilot one process, one
BLAS thread, `timeout 60`, `ulimit -v 524288`. Heavy jobs: at most two, eligible
slots 01 and 02 only, **active leases: none**.

| Item | Slot | Status | Basis | Ledger note |
|---|---|---|---|---|
| Two bounded python runs (Jacobian rank mod p; controls) | 01 v1 | claimed SPENT, sub-second | v1 §4, §10 | **No receipt on disk.** Scripts cited at `out/b18_01_pilot.py` and `out/b18_01_control.py` do not exist in B15-01. Counts as unreceipted until the revision delivers them under `analysis/b18_01_*` and `results/b18_01/`. |
| Five-row `U > B` screen, `d <= 5` | 01 v1 §9 (proposed) | PRICED (estimate) | producer estimate: under the default pilot cap | Not run. Not authorized here. A screen hit is headroom, not a candidate. |
| Five-row `U > B` screen, `d <= 8` | 01 v1 §9 (proposed) | PRICED (estimate) | producer estimate: minutes, under 2 GiB, needs a small lease | Not run. **A price estimate is not measured feasibility.** |
| Matrix-factorisation elimination over 80 variables | 01 v1 §6.1 | UNPRICED and moot | criterion rejected | Do not price; the underlying criterion is wrong. |
| Carrier construction and adapted-coordinate conversion | 02 | to be PRICED by slot 02 | — | Price before running. |
| Symbolic support for the global Psi identity | 05 | to be PRICED by slot 05 | — | If above the pilot cap, the price is the deliverable. |
| Any new finite screen | 06 | must be listed and capped before execution | — | Cells, range, cap in the report first. |
| Polar-degree computation | 07 | deferred, unpriced | board | Not ruled out. |
| Low-rank polynomial solve / saturation | 08 | not permitted without a separately reviewed budget | board | — |

Nothing in batch 18 has been measured as feasible. Everything above is either an
estimate or an unreceipted claim.

## 7. Completion states

`NOT_TRIGGERED` is a completion state, not a failure.

| Slot | State (2026-09-15, at ledger opening) | On disk |
|---|---|---|
| 01 | IN PROGRESS, **partial on disk** (revision 2; status line reads IN PROGRESS; 65 lines, sections 0–2 only; unchanged 16:04–17:04) | `B15-01/docs/b18_01_report.md` SHA256 `a5183f29f11901f3420395069e77666040cf097e38d7079ed3241bc0c26013a2`; `analysis/b18_01_rank_certificate.py`; `results/b18_01/{rank_certificate.json, rank_certificate_matrices.json, intake/b18_01_report_v1.md, literature/arXiv_2303.09028v3.pdf}` |
| 02 | IN PROGRESS, **partial on disk** (94 lines, §§0–1 only; status line promised in its §9, absent) | `B15-02/docs/b18_02_report.md` SHA256 `80916c0d7e44fcac419ac128925b36e1723dbe9f47e6e3361e1dffc4c2cf886b` at 17:05; claims listed as H12–H14 |
| 03 | NOT_TRIGGERED (gate: certified carrier) | — |
| 04 | NOT_TRIGGERED (gate: reviewed cell with `B < U`) | — |
| 05 | IN PROGRESS (one bounded attempt) | nothing |
| 06 | IN PROGRESS | nothing |
| 07 | NOT_TRIGGERED (second wave, conditional on 01 + 10) | — |
| 08 | NOT_TRIGGERED (optional) | — |
| 09 | NOT_TRIGGERED (gate: `r > B`) | — |
| 10 | IN PROGRESS, **partial on disk** (§§0–2 written, §§3–7 absent; 206 lines; unchanged 16:09–17:04) | `B15-10/docs/b18_10_review.md` SHA256 `0a512384bb12124160285a8b5c449637413411e7a5a688155c3c461af353521f`; decisions transcribed in §2a |
| 11 | COMPLETE | commit inventory in `Claude_Handover_B15_B18/COMMIT_*` |
| 12 | OPEN (this file) | `B15-12/docs/b18_12_ledger.md` |

A slot that finishes its session moves to `REPORTED (unreviewed)`, and only after a
slot 10 decision to `ACCEPTED (scoped)`, `CONDITIONAL` or `REJECTED`. **A report on
disk is not an accepted result.**

## 8. Chain watch: candidate -> bound -> rank

The batch's value is the chain `06 selects -> 02 carries -> 03 certifies b and B ->
04 produces r -> 09 assembles iff r > B`. Each link is listed with what "quietly
weakening" would look like there, so the failure is named before it happens.

| Link | Current state | How it weakens quietly | Ledger check |
|---|---|---|---|
| 1. 06 selects | **absent** (no report) | nominating a cell with `s` marked `unknown` while filling `b_required` with a number; using ordinary `g` for `s`; using the five-variable ceiling in a 6–10-row cell; treating a `U > s` count as a candidate | every 4b row must have exact `a`, `s`, `U` with the source of each, or `unknown` |
| 2. 02 carries | theory only, partial report on disk (H12–H14): transposition imposed by explicit symmetrisation, `s` pinned to the symmetric coefficient, conversion declared a cost barrier with a modular alternative; **no cell, no `b`** | dropping transposition (changes `s`); mixing ordinary and divided-power coordinates; pricing the conversion after running it; quoting a modular rank floor for `b` without saying it is modular | `s` must be the symmetric coefficient, and the same `H` must be used for `s` and for the projection |
| 3. 03 certifies `b`, `B` | NOT_TRIGGERED | subtracting a connected-stabilizer rank from a full-`H` `s`; taking a modular deficient rank as `b`; a nonzero forbidden *vector* reported as a rank floor | `b` is a certified rank lower bound on the same full-`H` columns; `B = min(a, s - b)`; compare against `b_required`, not against `s` |
| 4. 04 produces `r` | NOT_TRIGGERED | sampling unrelated quartics as "padding"; reporting a stalled sampled rank as an upper bound; leaving the characteristic-zero status of a modular witness unstated | `r` is an exact minor on actual `z·per3` restrictions, with the product-map identification justified by accepted dominance in five variables only |
| 5. 09 assembles | NOT_TRIGGERED | assembling on `r > U` or `r > s` instead of `r > B`; assembling in a cell whose `B` was reviewed in a different convention from `r` | same cell, same conventions, `r > B` with `B` global |

**Chain verdict at opening:** the chain has no first link. Nothing downstream can be
assessed. This is the expected state on day one, not a defect, and it is recorded
so that it is not confused with "the chain is intact".

**Two distinctions kept visible.**

1. *Promising method* vs *positive gap*. Positive gaps: **none**. Promising methods
   on the table: the B17-02 boundary arc (accepted, no numerical `b`); the five-row
   product-map coefficient pullback for `r` (accepted instrument, no rank promise);
   v1's `U > B` screen (unrun, would give headroom only).
2. *Failed method* vs *excluded cell*. Excluded cells: exactly the ten in §4a, by
   exact floors against reviewed ceilings. Everything else reported as negative in
   B17 or in v1 is a **scoped** negative: the degree-7 screen (31 shapes, `b = 0`
   only), the E24 generation route (that route only), the diagonal-arc projection
   (that arc family only), v1's aggregate Claim 5.1 (aggregate only, unreviewed).
   None of these excludes a cell.

## 9. Recommendations for the optional slots

Each recommendation names the evidence, not a preference.

**Slot 05 (rank 9 or 10): continue, as launched, within its gate.**
Evidence: the question is exact and bounded (two integers, an accepted basis, an
accepted `>= 9` minor and `<= 10` kernel); either route closes it; the cost cap is
the default pilot, and if the symbolic support prices out, the price is the
deliverable. Evidence against: none. Guard: the result changes nothing about the
excluded cell and must not be written up as if it did. Stop condition: one attempt.

**Slot 07 (explicit geometric equation): hold (NOT_TRIGGERED); do not launch on v1.**
Evidence: the board's launch condition is "a concrete construction worth pursuing"
from slot 01. v1 offers two routes and both are dead on v1's own account or the
board's: the incidence criterion `MN = F·I4` is rejected by counterexample, and the
Hessian-divisibility mechanism is argued not to transfer to five variables (v1 §6.1).
The only surviving five-row statement is existence in degree `<= 4^49` (unreviewed),
which gives no construction. Revise to "launch" only if the slot-01 revision supplies
a construction that survives slot 10's review; until then a launch would be an
unpriced search, and an unsuccessful search excludes nothing.

**Slot 08 (constrained Cayley identities): stop for this batch, unless capacity
remains after the chain and slot 10 asks for it.**
Evidence: the expanded repair already showed that generous operator freedom makes
the identity too easy (rank 28 with 264 free parameters, valid for any
row-multidegree (1,1,1) core, so unlimited rank is too weak); the constrained
question (rank `<= 6`) is open but producer-verified only; there is no polynomial
equation and no closure argument at the end of the route yet, and the board ranks it
below the chain. The board forbids any general solve or saturation without a
separately reviewed budget, and no budget exists. The honest state is "parked with
the precise open question recorded", which is a completion state.

## 10. Next board (justified from the evidence above, not from preference)

Nothing has reported, so the next board is the *decision tree* for when reports
land, plus the one action that is unconditional.

**Unconditional.** Keep this ledger open; update §2a from `docs/b18_10_review.md` as
soon as it exists, claim by claim; move slots to `REPORTED (unreviewed)` only when a
file exists on disk, and to `ACCEPTED` only on a slot 10 line.

**When slot 10 reports on v1 / the slot-01 revision:**
- `dim D45 = 50` and Theorem E: **done** (§2a, review partial). This changed no
  operational plan, as predicted. Still owed by slot 10: Claim 5.1, the ceilings
  6.1–6.3, the missing-theorem section, and the release-gate position. The revision
  (slot 01 rev 2) has not been reviewed at all; its new certificate is unreplayed.
- If Claim 5.1 (H3) is accepted: record it as *aggregate* and forbid its use as a
  cell exclusion in slot 06's shortlist. If rejected: nothing downstream changes,
  because nothing operational depends on it.
- If slot 01's revision supplies a construction slot 10 accepts as concrete: open
  slot 07 with a priced first test. Otherwise slot 07 stays NOT_TRIGGERED.

**When slot 06 reports:**
- Empty shortlist: record it as a success. The next test is then whatever slot 06
  names as "what would change that", priced; do not substitute v1's screen for it
  without the cell list, range and cap written first.
- Non-empty shortlist: for each cell check the 4b columns. A cell with `s = unknown`
  cannot proceed to 03 (no `b_required`). A cell with `b_required > 0` proceeds to
  02 only with slot 10's approval of definitions and cost. A cell with
  `b_required = 0` (`U > s`) still needs `r > B = min(a, s)`, i.e. an actual padding
  rank above `s`; that is a slot-04 question and needs no carrier, but it needs
  circuits and a priced evaluation.

**When slot 02 reports:** if it delivers a basis with `s` for a slot-06 cell and a
price for the forbidden projection under the pilot cap, and slot 10 approves both,
open 03 with that cap. If it delivers a cost barrier, record the barrier as the
missing piece and do not open 03.

**When slot 05 reports:** record 9 or 10, or the price of the bottleneck. No further
action in that cell.

**Not on the next board:** 03, 04, 09 (gated; gates unmet), 08 (stopped for the
batch), any heavy lease (none requested with a measured preflight), any
degree-`4^49` or incidence elimination.

**The single most likely honest close of this batch**, on current evidence: no cell
nominated with a certified `b`, the chain still without a second link, and the
batch's positive content being (i) a corrected five-row existence theorem with its
missing quantity named (`deg P(D45)`), (ii) a theory-only carrier construction with
a price, and (iii) closure of 9 vs 10. That is a legitimate outcome and should be
written as such rather than upgraded.

## 11. Update protocol for this ledger

When a slot's report appears on disk: add a §7 row change to `REPORTED (unreviewed)`
with the path and its SHA256; add its load-bearing claims to §3 as hypotheses; add
any numbers to §4b with `unknown` preserved. When slot 10 rules: move each claim to
§2a with the decision; only then may §4b, §5 gates or §10 change. Never move a claim
into §2 on the strength of a producer label.

## 12. Labelled claims of this slot

- **ADOPTED:** all conventions and the B15–B17 accepted base (§2b), from the preamble,
  the summary and the B17-11 supplements.
- **MEASURED (here):** the absence of any `b18_*` artifact in the twelve worktrees
  at opening, and the later appearance times and SHA256 of three partial reports;
  the absence of `out/` in B15-01; the v1 report's SHA256; the ten excluded-cell
  partitions written out with their sums checked against `4d`.
- **CHECKED (here, elementary, not a review):** `Sym^2(Sym^4 C^5)` has only
  partitions with at most two rows, so five-row cells at `d = 2` have `a = 0`
  (H14); the index-count derivation behind slot 02's weight lemma is internally
  consistent (H12). Neither is a slot-10 decision.
- **NOT REACHED:** nothing about any slot's mathematics is asserted by this ledger.
  No cell, no `s`, no `b`, no `r`, no gap.

**One next sufficient test for this slot:** the arrival of `docs/b18_10_review.md`;
price: none. Until then every batch-18 line in this ledger is a hypothesis.

## 13. Observation log (this session, 2026-09-15, local time)

| Time | Observation |
|---|---|
| open | B15-12 worktree was **not clean** at start: six pre-existing untracked `results/b15_12/*` and `results/logs/b15_12_*` paths (B15-era, not touched by this slot). Recorded per the preamble's "inspect the actual state"; the integrator decides their fate. |
| ~15:55 | No `b18_*` artifact in any of the twelve worktrees. Ledger opened. |
| 16:07 | `B15-01/docs/b18_01_report.md` (65 lines, §§0–2) and `B15-10/docs/b18_10_review.md` (37 lines, §0) appeared, both being written concurrently. Slot 01's certificate files present. Slot 01's revision confirms v1's scripts never existed on disk. |
| 16:09 | Slot 10's review reached 206 lines (§§1–2 with decisions). |
| 16:09–17:04 | No further change to either file; no output from slots 02, 05, 06. Status of the two writing sessions unknown (paused, thinking, or ended). |
| 17:04 | §2a transcribed from the review as it stands. Both reports remain partial. |
| 17:05 | `B15-02/docs/b18_02_report.md` appeared (94 lines, §§0–1). Claims recorded as H12–H14; no candidate, no `b`, no gap; its `d = 2` control is explicitly a method validation. Slots 05 and 06 still silent. |
| 2026-09-16 | Slot 01's revision now reads COMPLETE on disk (names the 23 degree-five five-row cells, all `a = 1`, as its carrier family; one excluded; no equation, no gap). Not yet transcribed claim by claim; unreviewed. On request, this slot wrote a theory note `docs/b18_12_coefficient_algebra.md` (fibre-constancy bound `m_det <= min(a, s - rho_L + u_L)`; contracted locus `Z` nonempty but blind to `>= 5` rows; block-triangular fibres vacuous; one priced diagnostic on `(4^6)`), with two bounded checks under `analysis/b18_12_*` and `results/b18_12/`. It nominates no cell and produces no gap. |

Files produced by this slot: `docs/b18_12_ledger.md` only. No computation was run.
No lease was requested. No git command beyond the two read-only `rev-parse` calls.
