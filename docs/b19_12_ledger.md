# B19-12 — Evidence ledger, stop decision and plain-language stocktake

**Slot:** 12 (ledger; stays open across batch 19)
**Worktree:** `work/batch15_workers/B15-12`
**Opened:** 2026-09-15, 23:17 local (America/New_York)
**Model:** Claude Fable 5.1 (Claude Code)
**Starting commit (recorded before any write):**

```
git rev-parse HEAD          c0cd755be9aa4a9a605f4dc875e7de744517a67b
git rev-parse HEAD^{tree}   4b95072d8d41a27ec7e66b1687f8209f9e3998d6
```

Git commands used: the two above and `git status --porcelain` (permitted by the
batch-19 preamble). Nothing else. No computation, no lease.

**Closed 2026-09-16, 07:19 local. The continue-or-stop decision this ledger
exists to make is §8.4: STOP. The plain-language stocktake is §11. Sections
0–8.3 are left exactly as they were written before slot 02 reported; §7e
records what superseded them and what slot 10's silence does to the whole
batch's review lineage.**

## 0. Plain terms

This ledger keeps six things in separate boxes and never lets one leak into
another: what an independent reviewer has actually accepted; what is merely
plausible and who is leaning on it; the exact numbers per cell, with `unknown`
where unknown; which slot is gated on what and whether the gate is met; what
has been priced versus what has been measured; and each slot's completion
state, where `NOT_TRIGGERED` is a completion state.

It also has one decision to make. The board's stopping rule is that if slots
01 and 02 supply no concrete construction, no useful boundary criterion and no
justified candidate, the batch stops there, and a focused two-session negative
is the batch's result. This ledger records that decision as soon as 01 and 02
have reported, and does not wait for twelve sessions.

**State at opening (23:17).** Slot 01 has a partial report on disk (140 lines,
§§0–4 written, status line reads IN PROGRESS, last write 23:15). Slot 02 has
written nothing. Slots 05, 10 and 11 have written nothing. Slots 03, 04, 06,
07, 08 and 09 are held by the board and have no batch-19 artefact. Therefore,
at opening:

- **Reviewed batch-19 facts: none.** Slot 10 has ruled on nothing in batch 19.
- **Positive gaps: none.** Unchanged since batch 15.
- **Nominated cells: none.** Slot 05 is intake-only this batch and nominates
  nothing in its first pass by its own brief.
- **New determinant equations of length 5 to 8: none.** This is still the
  programme's binding constraint, exactly as B18-06 named it.
- **Continue-or-stop: NOT YET DECIDABLE.** Slot 02 has not reported. The
  criteria are written in §8 now so that the decision, when it comes, is read
  off the evidence rather than composed after it.

## 1. Inputs read, with hashes

All paths relative to `C:/Users/swami/Projects/gct-gpt/`. SHA256 as read at
opening. A hash pins what was read; it says nothing about whether a claim is
true.

| Input | Path | SHA256 (prefix) | Role |
|---|---|---|---|
| Batch-19 preamble | `Claude_Handover_B15_B18/batch19_launch/B19_PREAMBLE.md` | `4286e214…` | conventions, what batch 18 settled, three rules |
| Batch-19 board | `Claude_Handover_B15_B18/BATCH19_PROPOSED_BOARD.md` | `d1690a3f…` | slot roles, gates, stopping rule |
| Integrator board assessment | `Claude_Handover_B15_B18/B19_BOARD_INTEGRATOR_ASSESSMENT.md` | `915e2325…` | integrator source |
| Batch-18 roadmap | `Claude_Handover_B15_B18/BATCH18_REVIEW_AND_NEXT_ROADMAP.md` | `14d80816…` | integrator source; ten corrections to carry |
| Slot-12 brief | `Claude_Handover_B15_B18/batch19_launch/B19-12.md` | `5489bbbc…` | this slot's assignment |
| Slot briefs 01, 02, 05, 10, 11 | `batch19_launch/B19-0{1,2,5}.md`, `B19-1{0,1}.md`, `LAUNCH.md` | read | who does what this batch |
| Batch-18 ledger (this slot) | `B15-12/docs/b18_12_ledger.md` | `a4520e2a…` | previous ledger |
| Batch-18 ledger review | `B15-12/docs/b18_12_review.md` | `ebc39b2c…` | integrator source; updates to transcribe |
| Slot 10 batch-18 review | `B15-10/docs/b18_10_review.md` | `dc1cc655…` | **slot 10 source**; §5 ledger, §7 gates, §9 length sweep |
| Integrator review of slot 10 | `B15-10/docs/b18_10_integrator_review.md` | `036c1616…` | integrator source |
| Integrator reviews of 01, 02, 05, 06, 06-sweep | `B15-0N/docs/b18_0N_review.md`, `b18_06_sweep_review.md` | `95e93dd1…`, `0d30ec90…`, `4378c189…`, `d0eb1742…`, `8a321a18…` | integrator sources |
| B18-02 report | `B15-02/docs/b18_02_report.md` | `dca6de94…` | the twenty controls, the price |
| B18-06 report and sweep | `B15-06/docs/b18_06_report.md`, `b18_06_sweep.md` | `60392996…`, `6ac744d6…` | exact cells, empty shortlist, 23 degree-five cells |
| **Slot 01 batch-19 report (partial)** | `B15-01/docs/b19_01_report.md` | `70fa44d8…` at 23:15, 140 lines | unreviewed research input |

Two review lineages are kept apart throughout: **slot 10** (the independent
adversarial reviewer) and **the integrator** (the reviews named
`b18_NN_review.md`, the roadmap, the board assessment). Where both ruled on the
same object, the ledger says so; where only one did, the ledger says which.

## 2. Reviewed facts

### 2a. Batch-19 decisions by slot 10

**None.** `B15-10/docs/b19_10_review.md` does not exist at opening. When it
does, decisions are transcribed only from its closing ledger, never from its
intermediate sections (rule carried from batch 18, accepted there).

### 2b. Batch-18 base, by review lineage

Two independent sources. "Slot 10" means `b18_10_review.md` (its §5 ledger,
§7 gates, §9 length sweep). "Integrator" means the `b18_NN_review.md` files,
the roadmap and the board assessment. **Slot 10's batch-18 review adjudicated
the slot-01 v1 report only.** It did not rule on B18-02, B18-05 or B18-06; for
those the only review on disk is the integrator's, and the table says so.

| # | Statement | Slot 10 | Integrator | Ledger status |
|---|---|---|---|---|
| F1 | `dim D45 = 50` exactly; `dim R135 = 39` | ACCEPTED, PROVED over `Q` by replay at two points, stabiliser nullity 1 | ACCEPT (b18_01_review; b18_10_integrator_review: own Leibniz/Fraction replay agrees) | ACCEPTED by both, independently reached |
| F2 | Some exactly-five-row cell carries a determinant equation failing on padding, degree `<= 4^49` | ACCEPTED, PROVED modulo the refined-Bézout citation (pointer: Fulton Ex. 8.4.6 / Thm 12.3) | ACCEPT, **conditional**: refined Bézout verified only through a secondary quotation (b18_01_review §4) | ACCEPTED by both; the number never travels without its condition; not a search budget |
| F3 | Refined Bézout overshoots the true degree by ~15 orders of magnitude in the four-variable control (LLV 320112) | MEASURED by slot 10 (§2 calibration) | carried into the board assessment §4 | ACCEPTED by both; `4^49` is an existence statement |
| F4 | Claim 5.1 (weighted five-row sum negative for large `d`) is a theorem about an aggregate; every cellwise or regime-wise use of it is rejected | ACCEPTED as aggregate; uses REJECTED (§3.2, §5) | agrees (roadmap §2; b18_10_integrator_review §1) | ACCEPTED by both; never used to nominate, exclude or rank a cell |
| F5 | `MN = F·I4` membership criterion is false (witness `M = l·I4`, `N = C·I4`) | REJECTED; **not independent** (preamble supplied the witness; disclosed) | REJECTED (preamble, board) | REJECTED; in force |
| F6 | `s` must be the symmetric rectangular Kronecker (transposition included), never ordinary `g` or `g` times a constant; `U = min(a, T)`, never unclipped `T` | CONDITIONAL relabels of v1 Claims 6.1, 6.2 (§4.1, §4.2) | same corrections found independently by B18-02 and B18-01; three lineages (b18_10_integrator_review) | ACCEPTED by both; convention |
| F7 | `P_L = closure{(z·per3) ∘ T}`, the honest `L`-variable restriction of `X_pad`, has `dim P_L = 10L - 5` for `L >= 6`, strictly inside `R13L` (all linear × cubic, `dim = L + C(L+2,3) - 1`); equality only at `L = 5` | MEASURED and PROVED (§9: exact Jacobian ranks meeting the `10L - 5` upper bound) | the integrator's own table had measured `R13L`; corrected on slot 10's finding and recorded as the integrator's defect (b18_10_integrator_review §2; board assessment §2d) | ACCEPTED by both; **an evaluation on an arbitrary product above five variables is not an actual-padding certificate** |
| F8 | Full-`H` carrier built; weight lemma `gamma-weight = 2d - skew degree`; forbidden projection = skew-degree `> 2d`; twenty certified cells at `d <= 3` with `s - b = a` in every one | **NOT RULED** (outside the object slot 10 reviewed) | ACCEPT with one condition: `a >= 1` beside the warning (b18_02_review) | integrator-only acceptance; `a >= 1` precondition ADOPTED into the board |
| F9 | Eleven-equation restriction rank on `X_pad` is exactly 9, kernel `span(kappa, w)`, conditional on inherited degree-27 lifts and the `GL16 -> 10x10` restriction argument; both kernel identities hold on the wider product family | **NOT RULED** | ACCEPT conditional as labelled (b18_05_review); one repair requested (degenerate generic-quartic control), assigned to B19-05 | integrator-only acceptance; conditions travel with it; changes no cell |
| F10 | Six pilot cells closed at `D = 0`; `(4d-8, 2^4)` closed by the leading 5×5 Hessian covariant wherever `a = 1` (certified `d = 5, 6, 7`); empty shortlist | **NOT RULED** | ACCEPT; `a` recomputed independently in all 8 cells (b18_06_review) | integrator-only acceptance |
| F11 | Nineteen remaining degree-five five-row cells closed at `D = 0`; degree-five family retired | **NOT RULED** | ACCEPT (b18_06_sweep_review); own wording corrected: 22 at `D = 0`, `(4^5)` at `D <= 0` only | integrator-only acceptance |
| F12 | Slot 10's review itself | — | ACCEPT in full; the integrator's one challenge (F7) was wrong and is recorded as such | — |
| F13 | Release gates G1–G7 for numerical releases | slot 10's, written before reading the intake | roadmap correction 3 proposes generalising G5 to any certified `B` with `r > B`, including `B = a - q`, with the `a = 1` exception explicit | G1–G7 in force as slot 10 wrote them; the generalisation is an **integrator proposal, not yet adopted by slot 10** |
| F14 | Polynomial multiples of the enumerated nine-/ten-row generator modules cannot create five-to-eight-row modules (Littlewood–Richardson containment) | NOT RULED | accepted with scope (roadmap §2; board) | integrator-only; scope: that generated ideal only, not saturation, not the full ideal |

Where the two lineages both ruled (F1–F7) they agree, and the agreement is
meaningful because slot 10's verdicts were formed before reading the intake
(its §6 says which). Where only the integrator ruled (F8–F11, F14) the
acceptance is single-lineage and is recorded as such; the board treats them as
starting points, and this ledger does the same, labelled.

### 2c. The four carry-forward items, reconciled with their sources

1. **Four settled degree-six five-row cells, not three.** `(16,2^4)` by
   Proposition 4.1 of `b18_06_report.md` (the covariant family, `a = 1`
   verified by the integrator); `(15,3,2,2,2)`, `(11,9,2,1,1)`, `(14,4,2,2,2)`
   by pilot P1 (cells C2, C4, C5). The sweep report's §8 says "3 are settled";
   the integrator flagged it; four is correct. **A fifth settled cell outside
   degree six:** `(20,2^4)` at `d = 7`, same proposition, `a = 1` verified by
   the integrator. Recorded for slot 05's intake.
2. **All 23 degree-five five-row cells excluded.** 22 at `D = 0` exactly (19
   swept, `(9,7,2,1,1)`, `(7,7,4,1,1)`, `(12,2^4)`); the rectangle `(4^5)` at
   `D <= 0` only, by padding vanishing (`i_pad = 1 = a`, so `m_pad = 0`), its
   `m_det` undetermined. Two descriptions of the same fact are on disk ("null
   cone" in the sweep, "padding vanishing, Prop 8.4" in its review); they are
   one fact. Consequence, integrator-stated: at `d = 5` all 22 non-rectangular
   cells have `m_det = a = 1`, so no determinant equation exists in them, and
   the first possible five-row separator has degree at least six.
3. **H7 has evidence and it leans against.** `s - b = a` in all twenty
   certified controls at `d <= 3`. Precision on the brief's wording: `b = s`
   *has* been observed, but only in the nine `a = 0` cells, where it is forced
   by `s - b = a = 0` and buys nothing; in an `a >= 1` cell `b = s` has never
   been seen, and `b > s - a` has never been seen in any cell. A usable `b`
   needs `b >= s - U + 1 > s - a` when `U <= a`. Source: `b18_02_report.md` §6
   item 2, integrator-accepted.
4. **`P_L` is not all linear × cubic above five variables.** F7 above, with
   the dimensions. The operational half is the one that matters: a product
   evaluation is a padding certificate only at `L = 5`.

### 2d. Ten integrator corrections from the roadmap, and where each stands

| # | Correction (roadmap §3) | Status in this ledger |
|---|---|---|
| 1 | No rerun of the degree-five/six symmetry census | board gate for slot 05; honoured here (no census, no `s` re-extracted) |
| 2 | The Kronecker route is not the only positive route; direct identities and certified boundary loss remain possible | recorded in §4e |
| 3 | Generalise G5 to any certified `B`, `r > B`, incl. `B = a - q`; state the `a = 1` exception | F13: proposal, not yet slot 10's |
| 4 | "One nonzero determinant evaluation closes the cell" only for `a = 1`; general `a` needs full rank | applied in §4b–4c wording |
| 5 | No sampled zero as a global identity; no failed spanning as a nonspanning theorem | rule, applied throughout |
| 6 | Five rows are not the only separation evidence; higher-row equations survive on padding | §4e |
| 7 | Computing the exact variety degree could help; it is neither the only route nor a guarantee | §3, H-Bez |
| 8 | Attribute larger-row dimension measurements to their precise varieties | F7 |
| 9 | Copy review replay scripts out of scratch storage | slot 11's item; slot 10's batch-18 replays were in a scratchpad by its own §8 |
| 10 | Read-only git status is not a defect; no push, no publication | preamble now permits `git status --porcelain` |

## 3. Hypotheses: plausible, unproved, and who relies on each

None of these is a fact. Producer labels are the producer's.

| ID | Hypothesis | Source | Producer label | Relied on by | Evidence and ledger note |
|---|---|---|---|---|---|
| H7 | A usable `b` exists: some cell with `a >= 1`, `U >= 1` and certified `b >= b_required = s - U + 1` | programme goal | — | slots 03, 06 (boundary route), 09 | **Leans against**: `s - b = a` in 20/20 controls; `b > s - a` never observed. Slot 01's partial report (H-01b) says `b = 0` provably in a band of 6–10-row cells, so the arc cannot reach `b_required` there at all. |
| H1 | B18-02's column-local contraction family spans `M_lambda` | B18-02 §5 | hypothesis | B18-02's hour-scale prices only | Not needed for a rank floor (a nonzero minor on any correctly built subfamily is a floor); needed only for "basis certified". |
| H-a | Astra census values of `a` | tree | ADOPTED | B18-06 closures | Discharged by integrator recomputation in the 8 pilot/family cells and the 19 swept cells; still ADOPTED elsewhere. |
| H-Bez | Refined Bézout, primary-source location | B18-01 | PROVED conditional | Theorem E's number only; nobody operationally | Pointer Fulton Ex. 8.4.6 / Thm 12.3 (slot 10). Roadmap: an exact `deg P(D45)` could improve the bound; not the only route. |
| H-inh | Degree-27 polynomial lifts of the eleven-space; `GL16 -> 10x10` restriction argument | B15/B16, B17-04 | ADOPTED | F9 | Inherited, accepted in earlier batches, not re-proved in batch 18. Nothing operational depends on F9. |
| H-01a | **Grading identity** (B19-01 Prop 3.1): every full-`H` invariant component has `W_{-1}`-degree `d`, `W_0`-degree `#v`, `gamma`-weight `2d - #v` | `b19_01_report.md` §3 (partial) | PROVED (producer) | everything else in B19-01 | Unreviewed. Re-derives B18-02 Lemma 4.1 from the Littlewood–Richardson decomposition; consistent with the ledger's batch-18 sanity check of H12. |
| H-01b | **Silence theorem** (B19-01 Thm 4.1): if `lambda_1 + lambda_2 + lambda_3 <= 2d` the forbidden part of `S_lambda W` is zero, so `b = 0` and `B = min(a, s)` | `b19_01_report.md` §4.1 | PROVED (producer) | H7 (against); slot 03 (a region where no carrier should be run); slot 05's intake | Unreviewed. Proof is three lines from H-01a: a `kappa` with at most three rows inside `lambda` has size at most `lambda_1 + lambda_2 + lambda_3`. Independent of `H`, of `s`, of spanning. |
| H-01c | The silent band is empty for `ell(lambda) <= 5`, a single rectangle at `ell = 6` (when `3 | 2d`), a non-trivial band for `7 <= ell <= 16` (Prop 4.4); so the twenty controls could not have seen it | `b19_01_report.md` §4.3 | PROVED (producer) | interpretation of H7's evidence | Unreviewed. Elementary averaging. **Consequence if accepted:** the `s - b = a` regularity is evidence about a region that provably excludes the band; it neither confirms nor refutes exactness there. |
| H-01d | Sharper LR criterion (Thm 4.2), length bound `ell(lambda) <= 7 + min(9, d - 1)` for `b > 0` (Cor 4.3) | `b19_01_report.md` §4.2 | PROVED (producer) | slot 05 pre-screen | Unreviewed. |
| H-01e | Counterexample to exactness (§5) and Levi reduction (§6) | announced in `b19_01_report.md` §1, **not on disk** | — | — | NOT ON DISK at opening. |
| H-02 | (nothing) | `b19_02_report.md` does not exist | — | — | NOT ON DISK. |

**Rejected, not hypotheses:** `MN = F·I4`; four-variable LLV literature as a
shortcut; any aggregate-to-cell inference; any general-product evaluation above
five variables presented as actual padding.

## 4. Exact cells

Conventions (preamble): ordinary coefficients; `s` symmetric rectangular
Kronecker, transposition included; `U = min(a, T)`; `B = min(a, s - b)` only
with certified `b`; `b_required = max(0, s - U + 1)`. **`a` is recorded first
in every row; `a = 0` is a method control, never a candidate.** "`b`: none"
means no certified `b >= 1` exists anywhere in the tree; the trivial floor
`b = 0` is always available and is not a result.

### 4a. The ten excluded ten-row cells (B15–B17; carried, every row verified by the integrator in `b18_12_review.md` §1)

| d | lambda | a | i_det (floor) | m_det | U | s | b | b_required | D upper | status |
|---|---|---:|---:|---:|---:|---|---|---|---:|---|
| 23 | (61,15,2^8) | 189 | 1 | 188 | 158 | unknown | none | unknown | -30 | EXCLUDED (B16) |
| 25 | (67,17,2^8) | 294 | 4 | 290 | 218 | unknown | none | unknown | -72 | EXCLUDED (B16) |
| 26 | (71,17,2^8) | 294 | 4 | 290 | 218 | unknown | none | unknown | -72 | EXCLUDED (B16) |
| 27 | (73,19,2^8) | 429 | 11 | 418 | 288 | unknown | none | unknown | -130 | EXCLUDED (B16; padding floor 243, `D` in `[-175, -130]`; eleven-space rank 9 on padding, F9) |
| 23 | (59,17,2^8) | 292 | 2 | <= 290 | 218 | unknown | none | unknown | -72 | EXCLUDED (B17 screen) |
| 24 | (63,17,2^8) | 293 | 3 | <= 290 | 218 | unknown | none | unknown | -72 | EXCLUDED (B17 screen) |
| 23 | (57,19,2^8) | 419 | 4 | <= 415 | 288 | unknown | none | unknown | -127 | EXCLUDED (B17 screen) |
| 24 | (61,19,2^8) | 424 | 7 | <= 417 | 288 | unknown | none | unknown | -129 | EXCLUDED (B17 screen) |
| 25 | (65,19,2^8) | 427 | 9 | <= 418 | 288 | unknown | none | unknown | -130 | EXCLUDED (B17 screen) |
| 26 | (69,19,2^8) | 428 | 10 | <= 418 | 288 | unknown | none | unknown | -130 | EXCLUDED (B17 screen) |

Closed by exact determinant floors against a reviewed padding ceiling;
independent of `s` and `b`. `U/a` in `[0.671, 0.836]`. Do not rank-hunt here.

### 4b. Degree five, five rows: 23 cells, all `a = 1`, all EXCLUDED (batch 18, integrator-accepted, F10–F11)

| lambda | a | s | U | b | b_required | D | closed by |
|---|---:|---:|---:|---|---:|---|---|
| (12,2,2,2,2) | 1 | 8 | 1 | none | 8 | = 0 | Prop 4.1 covariant; P1 control C0 |
| (9,7,2,1,1) | 1 | 15 | 1 | none | 15 | = 0 | P1 cell C1 |
| (7,7,4,1,1) | 1 | 19 | 1 | none | 19 | = 0 | P1 cell C3 |
| (8,5,5,1,1) | 1 | 23 | 1 | none | 23 | = 0 | sweep S07 |
| (8,7,3,1,1) | 1 | 23 | 1 | none | 23 | = 0 | sweep S04 |
| (4,4,4,4,4) | 1 | census (`s - a = 4`) | **0** | none | 0 (`U = 0`: no gate) | **<= 0** only; `m_det` undetermined | padding vanishing, `m_pad = 0` (B18-01 Prop 8.4) |
| the other 17 swept cells S01–S03, S05, S06, S08–S19 | 1 each | census, 8–89 across the 22 non-rectangular cells, **not re-extracted here** | 1 | none | `s` each (`= s - U + 1`) | = 0 | sweep, first determinant point, `m_pad >= 1` at an actual point |

Integrator-stated consequence: `m_det = a = 1` in the 22 non-rectangular
cells, so `i_det = 0` and **no determinant equation exists in any of them**.
The first possible five-row separator has degree at least six.

### 4c. Degree six and seven, five rows: settled cells (batch 18, integrator-accepted, F10)

| d | lambda | a | s | U | b | b_required | D | closed by |
|---:|---|---:|---:|---:|---|---:|---|---|
| 6 | (16,2,2,2,2) | 1 | 8 | 1 | none | 8 | = 0 | Prop 4.1 covariant family |
| 6 | (15,3,2,2,2) | 1 | 15 | 1 | none | 15 | = 0 | P1 cell C2 |
| 6 | (11,9,2,1,1) | 1 | 22 | 1 | none | 22 | = 0 | P1 cell C4 |
| 6 | (14,4,2,2,2) | **2** | 45 | 2 | none | 44 | = 0 | P1 cell C5 (all six 2×2 minors nonzero on each side) |
| 7 | (20,2,2,2,2) | 1 | unknown | 1 (`m_pad = 1 = a`) | none | unknown | = 0 | Prop 4.1 covariant family (`a = 1` integrator-verified) |

**Four** degree-six cells, plus one at degree seven. Priced and NOT REACHED in
batch 18: `(8,7,7,1,1)_6` (`a = 2`, `s = 30`, `U = 2`, `b_required = 29`;
weight space 6718, dense kernel above cap) and the six-row `(14,2^5)_6`
(`a = 1`, `s = 13`, `U` only a generic-product ceiling, weight space 7508).
The remaining 100 degree-six five-row cells (38 of 105 have `a = 1`, census)
are **untested**: not candidates, not excluded. No degree-six sweep is
requested by the board.

### 4d. Cells nominated in batch 19

| d | lambda | a | s | U | b | b_required | padding evidence | cost | nominated by | reviewed by 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| — | (none) | | | | | | | | nobody; slot 05 is intake-only and nominates nothing in its first pass | — |

**No cell is nominated.** No cell anywhere in the programme has a certified
`b >= 1`, a certified `B < U`, or a certified `q >= 1` in a type of length 5–8.

### 4e. Regime facts that constrain where a cell can be

- Length at most 4: `D <= 0` in every degree (B17-03). Closed.
- Length 5: geometric separation exists in some cell of degree at least 6 and
  at most `4^49` (F2, F11). No such equation has been written down. Five rows
  are distinctive only because the existence theorem has not yielded an
  explicit equation there (roadmap correction 6); higher-row equations already
  survive on padding (F9: nine directions survive in the degree-27 cell).
- Lengths 6–10: no theorem either way. `U` is the honest `P_L` ceiling, not
  the product ceiling (F7). If H-01b–c are accepted: the B17-02 arc is
  provably blind in the band `lambda_4 + ... + lambda_L >= 2d`, which is
  non-empty exactly here. A blind instrument is not an exclusion; other routes
  (direct identities, other arcs, geometric constructions) are untouched.
- Length above 10: `m_pad = 0` (B17-03). Closed.
- In every admissible cell for which `s` is on disk (lengths 5 and 6, `d <= 6`;
  the seven degree-7 cells), `s >= a`, so `B0 = min(a, s) = a` and the first
  `s - a` dimensions of any boundary loss are dead loss (B18-06 §1.4).

## 5. Prerequisites and gates

| Slot | Gated on (board) | Gate met? | State of the premise |
|---|---|---|---|
| 01 | theory first; no large carrier; hand any new cell to 05 and 10 before numerics | launched; theory-only, heavy-eligible, no lease | in progress, §4 on disk |
| 02 | theory first; no unconstrained 80-variable elimination; no bare `MN = F·I4`; no "degree is the only route" | launched; theory-only, heavy-eligible, no lease | **nothing on disk** |
| 03 | HOLD until 01 or 02 supplies a question that needs the computation | **not met** | 01 so far supplies a region where *no* computation should be run; no finite problem yet |
| 04 | HOLD for an explicit equation or well-defined finite family from 01/02 | **not met** | no equation exists |
| 05 | initial intake only; candidate experiments held for new evidence; no census | launched (intake) | nominates nothing in this pass by brief; also owns the B18-05 control repair |
| 06 | HOLD for reviewed candidate and cost | **not met** | no candidate |
| 07 | HOLD for reviewed bound with `B < U` and feasible costs | **not met** | no `B < U` anywhere |
| 08 | no assignment; integrator must write question, output and budget first | **not met** | NOT_TRIGGERED |
| 09 | `r > B` | **not met** | NOT_TRIGGERED |
| 10 | factual objections only during development; frozen-hash verdict on completed deliverables | launched | nothing on disk |
| 11 | delivery, contract additions, literature inventory; commits nothing | launched | nothing on disk |
| 12 | 01 and 02 reports | this file | decision criteria in §8; decision pending 02 |

Rule for later launches (LAUNCH.md): `B19_RULES.ps1` was to add byte-preservation
rules to all twelve worktrees before any session; this ledger did not verify
that it ran (not its remit) and records only that the batch-18 trap — a gated
slot launched without its rules — is what the instruction is for.

## 6. Costs: measured versus estimated

Standing limits: one process, one BLAS thread, 60 s / 512 MiB through the
inspected wrapper; heavy eligibility 01 and 02 only, at most two heavy jobs,
**active leases: none**; the board issues none.

| Item | Slot | MEASURED or ESTIMATED | Number | Note |
|---|---|---|---|---|
| Lemma 2.1 determinant/padding evaluation, weight dim `<= 2337`, `a <= 2` | B18-06 P1 | MEASURED | `<= 5.2 s`, `<= 289 MiB` per cell | the cheap decision procedure; six cells, six closed |
| Same, sweep, `K` up to 11640 | B18-06 sweep | MEASURED | 1.9–14.0 s, peak 80 MiB; 24 runs, 123.5 s total | sublinear in `K` over that range |
| Same, above `n ≈ 5000` (dense sketch limit) | B18-06 | **unpriced** | sparse kernel method needed | `(8,7,7,1,1)_6` and `(14,2^5)_6` NOT REACHED for this reason |
| Carrier controls, all 47 partitions of 12, `<= 5` rows | B18-02 run B | MEASURED | 55.35 s, 447 MiB | twenty cells certified |
| Carrier at `d = 7`, five rows | B18-02 §5.3 | ESTIMATED | `132 s (s+2)` evaluations at ~17 ms: `s = 100` ≈ 6.4 h, `s = 300` ≈ 57 h | conditional on H1; **no lease; does not authorise execution** |
| Eleven-space evaluation and proof | B18-05 | MEASURED | 5.8 s / 20 MB; 1.5 s; one 60 s cap hit recorded | done |
| Slot 10 batch-18 replays | B18-10 | MEASURED (by inspection, no wrapper) | seconds, largest matrix 160×715 | scripts were in a scratchpad; roadmap item 9 |
| B19-01 band pilot (`analysis/b19_01_band.py`, `results/b19_01/band_cells.json`) | B19-01 | **receipt not yet on disk** | unknown | recorded as run; cost awaits the report's resource section |
| B19-02 | — | nothing | — | — |
| Degree-six five-row sweep (105 cells) | — | **unpriced**, needs a `K` census | — | not requested by the board |

Nothing in batch 19 has been measured yet. The only measured-cheap procedure
in the tree is the full-rank determinant evaluation, and it closes cells; it
cannot open one.

## 7. Completion states

`NOT_TRIGGERED` is a completion state, not a failure. A report on disk is not
an accepted result: `REPORTED (unreviewed)` moves to `ACCEPTED (scoped)`,
`CONDITIONAL` or `REJECTED` only on a slot-10 line.

| Slot | State at opening (23:17) | On disk |
|---|---|---|
| 01 | IN PROGRESS, partial (140 lines, §§0–4; §§5–6 announced) | `B15-01/docs/b19_01_report.md` `70fa44d8…`; `analysis/b19_01_band.py`; `results/b19_01/band_cells.json` |
| 02 | IN PROGRESS, **nothing on disk** | — |
| 03 | NOT_TRIGGERED (held) | — |
| 04 | NOT_TRIGGERED (held) | — |
| 05 | IN PROGRESS, nothing on disk | — |
| 06 | NOT_TRIGGERED (held) | — |
| 07 | NOT_TRIGGERED (held) | — |
| 08 | NOT_TRIGGERED (no assignment) | — |
| 09 | NOT_TRIGGERED | — |
| 10 | IN PROGRESS, nothing on disk | — |
| 11 | IN PROGRESS, nothing on disk | — |
| 12 | OPEN (this file) | `B15-12/docs/b19_12_ledger.md` |

Batch-18 completion states, as reconciled by the integrator's review of the
previous ledger and not re-litigated here: 01, 02, 05, 06, 10, 11 COMPLETE and
reviewed (slot 10's review by the integrator; 01 v1 by slot 10; 02, 05, 06 by
the integrator only, F8–F11); 12 accepted; 03, 04, 07, 08, 09 NOT_TRIGGERED.
The batch-18 administrative closeout is still the integrator's and is not
re-opened by this batch.

## 7a. Update 23:23 — slot 01 COMPLETE (unreviewed); slot 11 writing; slot 02 still silent

`B15-01/docs/b19_01_report.md` reached 297 lines at 23:21, status line
**COMPLETE**, SHA256 `aa136106…`. Artefacts: `analysis/b19_01_band.py`
(`3b15bbd2…`), `analysis/b19_01_band6.py` (`908cc1ee…` per the report),
`results/b19_01/band_cells.json` (`346630587a…`), `band_cell_d6.json`,
two output captures. `B15-11/docs/b19_11_report.md` appeared at 23:20 (partial,
`9b766611…`). `B15-02`, `B15-05`, `B15-10`: nothing.

**§7 change.** 01: `REPORTED (unreviewed)`. 11: IN PROGRESS, partial on disk.

**§3 change.** H-01e is now on disk and splits:

| ID | Hypothesis | Producer label | Relied on by | Ledger note |
|---|---|---|---|---|
| H-01e | **Counterexample to exactness** (Thm 5.1): at `d = 6`, `lambda = (4^6)`: `a = 1`, `g = 13`, `s = 10` (MEASURED, seven controls pass incl. reproduction of B18-02's `s` in seven cells), `b = 0` by Thm 4.1, so `ker C = M_lambda` has dimension 10 against `m_det <= 1`; the arc gives `B = a` and can never certify a gap in a band cell | PROVED given MEASURED `a`, `s` | H7 (against, in the band); nobody downstream | Unreviewed. Ledger check (elementary, not a review): `4+4+4 = 12 = 2d`, so the band condition holds with equality; a `kappa` with at most three rows inside `(4^6)` has size at most 12, so Thm 4.1's hypothesis is met. The conclusion needs only `m_det <= a`. Refutes the general exactness conjecture, **not** its length-at-most-five form, where the band is empty. |
| H-01f | **Levi reduction** (Thm 6.2): `b <= dim((S_lambda W)_{<0})^L`, a finite branching number computable from `lambda` alone; a pre-screen returning `b_max <= s - a` proves the cell cannot give `B < a` by this arc | PROVED (inequality); screen NOT REACHED (step 2 unimplemented) | any future carrier run (slot 03) | Unreviewed. It is an **upper** bound on `b`; it can only say "do not run". It cannot certify a `b`, a `B < U`, or a gap. |

**§4 change — one new cell with exact data (batch 19, unreviewed).**

| d | lambda | ell | a | s | g | U | b | b_required | m_det | m_pad | D | status |
|---:|---|---:|---:|---:|---:|---|---|---|---|---|---|---|
| 6 | (4,4,4,4,4,4) | 6 | 1 | 10 | 13 | **unknown** (six rows: honest `P_6` ceiling, not the product ceiling) | **0, PROVED by 01 (Thm 4.1)** | `>= 10` if `U >= 1`; unreachable since `b = 0` | unknown (`<= 1`) | unknown | unknown | **NOT A CANDIDATE by this arc**: `B = min(a, s - b) = 1 = a`; an `m_det`, `m_pad` computation would decide `D` but the arc cannot |

The producer records `a = 1` (its P1/P2 controls: the `d = 6` six-variable
dimension check `6,249,655,776` and `f^R = f^lambda = 140,229,804`). It is the
only band cell with `a >= 1` at `d <= 6`; three band cells at `d = 3, 4` have
`a = 0` and are method controls. Caution noted by the ledger: the five-row
rectangle `(4^5)_5` had `m_pad = 0` by padding vanishing; whether the six-row
rectangle behaves the same is **untested and not inferred**.

**§6 change.** B19-01 MEASURED: `b19_01_band.py` 7.84 s, `b19_01_band6.py`
2.31 s, exit 0, one process, one BLAS thread, under `timeout 60` and
`ulimit -v 524288` from the shell — **not** through the inspected Job-Object
wrapper, and the report itself says `ulimit -v` enforcement against a native
Windows `python.exe` is unverified. Peak memory "well under the cap" is the
producer's statement, not a receipt. Recorded as measured wall time with an
unverified memory bound. Estimated, not measured: the Levi screen at `d <= 7`,
"seconds to a few minutes per cell", at most 10,505 triples per cell; at
`d = 26` about `4.2·10^8` triples, out of scope.

**§5 change: no gate opens.** 01 hands no new cell to 05 or 10 for numerical
work (its own §8.3). Its next test is a pre-screen that only ever says "do not
run the carrier"; nobody is proposing to run the carrier, because no cell is
nominated. So 03 stays HOLD: there is no question that needs the computation.
04, 06, 07, 09 unchanged.

## 8. The decision this ledger exists to make

### 8.1 Criteria, written before slot 02 reported

The board's rule: stop after the first wave if 01 and 02 supply **no concrete
construction, no useful boundary criterion and no justified candidate**. Read
strictly:

- *Concrete construction* (02): explicit variables and equations, degree/type
  where known, a proof that its polynomial consequences vanish on the entire
  determinant closure, either an exclusion of the padded example or the exact
  lemma that would give it, and a bounded elimination or linear-algebra
  problem priced **before** computation. A construction whose unresolved step
  is itself an unbounded elimination is not concrete in this sense.
- *Useful boundary criterion* (01): a criterion under which `b > s - a` is
  provable or cheaply detectable in a cell with `a >= 1`, `U >= 1`, or a
  family that always survives the test, or a reduction of the `ell <= 5`
  exactness question to a named finite problem of stated size. A theorem that
  the arc is blind somewhere is a valuable negative and is **not** a useful
  criterion in the sense that opens 03.
- *Justified candidate*: a cell with `a >= 1` recorded first, exact `s` and
  `U`, and either a certified `B < U` or a certified `q >= 1` in a type of
  length 5–8. None exists.

Continue means: pick one path, develop its tool in 03, test product
compatibility in 04, nominate through 05. Stop means: write the batch's result
as the two-session negative and open nothing.

### 8.2 Reading of slot 01 alone (unreviewed)

Slot 01 delivered the second of the two outcomes its brief called a surprise:
**a theorem showing this arc cannot improve the ceiling in a specified
region** (the band `lambda_1 + lambda_2 + lambda_3 <= 2d`, non-empty exactly for
lengths 6–10), a proved counterexample to exactness inside it, and an
unevaluated pre-screen. Against the criteria:

| Criterion | Met by 01? |
|---|---|
| concrete construction | not its remit; none |
| useful boundary criterion (opens 03) | **no**: what is proved is where the arc is silent; the `ell <= 5` question is explicitly untouched (its §7.1); the Levi screen is an upper bound on `b` and can only forbid runs |
| justified candidate | **no**; `(4^6)_6` is recorded as a cell where this arc is provably useless |

So, **on slot 01 alone, nothing continues.** What 01 adds to the programme is
a spending rule: before any carrier time on a 6–10-row cell, check three
parts of `lambda` against `2d`; and the twenty-control regularity
`s - b = a` is now explained as an artefact of a region that excludes the band,
neither confirming nor refuting exactness at five rows. That is the "useful
theory" line of the board's worthwhile list, and it is a negative.

### 8.3 Decision status

**PENDING slot 02.** The decision cannot be recorded as final until 02 has
reported, because 02 is the one route that could still supply a construction.
The two possible outcomes are written now, so that the one that occurs is
transcribed rather than composed:

- **If 02 delivers a construction meeting the definition in 8.1**: CONTINUE on
  that single path — 10 reviews it frozen, 04 tests it against the product
  family (with the F7 caveat that a general-product nonzero above five
  variables is not a padding nonzero), then 05 assesses. 03 opens only if the
  construction's bounded problem needs the carrier, which on present evidence
  it would not.
- **If 02 delivers a rigorous failure, or a construction whose unresolved step
  is an unbounded elimination, or nothing**: **STOP.** The batch's result is
  the focused two-session negative: (i) the B17-02/B18-02 boundary arc is
  provably blind in the band `lambda_4 + ... + lambda_L >= 2d` and not exact
  there, with the five-row question untouched; (ii) 02's scoped failure,
  stated as its own report states it. No downstream slot opens. This is a
  success by the board's own rule and is to be written as such.

**Provisional reading, on the evidence at 23:23:** the second outcome is the
more likely one, because every mechanism in the tree has already been shown
blind to length at most eight (B18-06 Lemmas 3.1–3.2, integrator-accepted),
and 02's brief already lists a rigorous failure as a complete deliverable. A
provisional reading is not the decision.

## 9. Labelled claims of this slot

- **ADOPTED:** all conventions; the batch-18 base of §2b with its lineage
  labels; the ten integrator corrections.
- **MEASURED (here):** presence, timestamps, line counts and SHA256 of every
  batch-19 artefact named in §1 and §7a; the absence of any `b19_*` artefact
  under B15-02, B15-05, B15-10 at 23:23; the absence of any artefact under the
  held slots.
- **CHECKED (here, elementary, not a review):** the band condition and the
  three-row containment bound at `(4^6)`, `d = 6` (H-01e note); the arithmetic
  `b_required = s - U + 1` in every §4b–4c row where `s` and `U` are on disk.
- **NOT REACHED:** nothing about any slot's mathematics is asserted by this
  ledger. No cell, no `s` of its own, no `b`, no `r`, no gap. The
  continue-or-stop decision is written as criteria plus a provisional reading,
  and is not final until 02 reports.

**One next sufficient test for this slot:** the arrival of
`B15-02/docs/b19_02_report.md`; price: none. On arrival, §8.3 is completed
from its stated result in one paragraph, and slot 10's closing ledger, when it
exists, is transcribed into §2a.

## 10. Observation log (2026-09-15, local time)

| Time | Observation |
|---|---|
| 23:17 | Worktree not clean at start: six pre-existing untracked B15-era paths under `results/b15_12/sources/` and `results/logs/` (13 September), not touched. Only `B15-01` had batch-19 output (140 lines, §§0–4). Ledger opened. |
| 23:18 | Inputs hashed (§1). Batch-18 review lineages separated (§2b). |
| 23:21 | `B15-01/docs/b19_01_report.md` reached 297 lines, status COMPLETE. `B15-11/docs/b19_11_report.md` appeared (partial). |
| 23:23 | §7a, §8 written. `B15-02`, `B15-05`, `B15-10` still silent. |

Files produced by this slot: `docs/b19_12_ledger.md` only. No computation, no
lease, no git beyond `rev-parse` (twice) and `status --porcelain`.

## 7b. Update 23:25 — slot 02 writing (partial); slot 05 running its control

`B15-02/docs/b19_02_report.md` appeared at 23:23 (13 KB, §§0–4 of eleven
announced sections; author line reads "Claude (Opus 5)"; status not yet
COMPLETE). `B15-05/analysis/b19_05_control.py` appeared at 23:23 and
`B15-05/docs/b18_05_report.md` was modified at 23:24 — slot 05 is appending the
generic-quartic control addendum its brief assigns, to the batch-18 report, as
that brief permits. `B15-10`: still nothing.

**§7 change.** 02: IN PROGRESS, partial on disk. 05: IN PROGRESS (control
script on disk; addendum in progress). 11: IN PROGRESS, 208 lines.

**§3 change — slot 02's announced claims, recorded as hypotheses from its
partial text** (its §§5–11 are not on disk; nothing below is a decision):

| ID | Hypothesis | Producer label | Relied on by | Ledger note |
|---|---|---|---|---|
| H-02a | `I(D45) = ker phi^*` degreewise, and `C[D45]_d` embeds in `R_d`, the weight-`d` semi-invariants of the 5-Kronecker quiver at `(4,4)`; hence the **counting criterion** `r(d) < A(d)` implies `I(D45)_d != 0` (Thm 4.2), closure-correct via `phi^*(h) = 0` on `im phi` (Lemma 3.1) | PROVED (producer) | H-02c | Unreviewed. Lemma 3.1 is B18-01 Prop 5.2 restated; the construction quantifies over no auxiliary matrix, which is what the rejected `MN = F·I4` did. |
| H-02b | `r(d) = sum_{rho ⊢ 4d} 5^{ell(rho)} chi_{(d^4)}(rho)^2 / z_rho` (Lemma 4.1); cell form `m_det <= s <= g` (Thm 4.4, = B18-01 Claim 6.1 with slot 10's relabel) | PROVED (producer) | H-02c | Unreviewed; Thm 4.4 is already F6. |
| H-02c | **The verdict, announced in §0:** the criterion provably cannot fire below degree 320112 in four variables (where the truth is known, LLV), the measured ratio `r(d)/A(d)` grows (75.8 at `d = 12`), and five variables behave the same; so this construction cannot produce the missing equation at any reachable degree | producer's verdict; proofs in §§5–6 **not yet on disk** | the batch decision (§8) | Recorded from the plain-terms section only; the ledger transcribes its final form when the sections exist. |
| H-02d | Corollary 4.3: for `d < 320112`, a nonzero `I(D45)_d` contains a highest-weight vector of length exactly five | CONDITIONAL on LLV (secondary quotation) and 03-A | nobody operationally | Unreviewed. |
| H-02e | Announced §8 corollary: `I(D45)_d = 0` for `d <= 5`, so the first five-variable determinant equation has degree at least six | announced; not on disk | consistency with F11 | Same statement the integrator drew from the degree-five sweep (§2c item 2); a second lineage if its proof lands. |
| H-02f | Announced §7: a certification scheme promoting a sampled rank drop into a proved equation, with its exact missing lemma (§7.3) | announced; not on disk | nobody | If it lands, it is the kind of "missing lemma" deliverable the board asks for, not a construction. |

**Reading against §8.1 so far:** the construction is explicit and
closure-correct, and its author's own verdict is that it cannot fire at any
reachable degree. If §§5–6 deliver that as proved, this is "a rigorous reason
the chosen construction fails" — a complete deliverable by the brief, and the
**STOP** branch of §8.3. Not decided until the sections are on disk.

| 23:25 | `B15-02/docs/b19_02_report.md` at 235 lines (§§0–4), SHA256 `1bee265d…`. `B15-05/analysis/b19_05_control.py` (`8429fbad…`); `B15-05/docs/b18_05_report.md` gained an addendum (three full-support quartics, `w·E` and `kappa·E` nonzero at each; the degenerate control reproduced and explained), file now `1af53479…`, 473 lines. §7b written. |

## 7c. Update 23:27 — slot 11 partial findings that bear on this ledger

From `B15-11/docs/b19_11_report.md` (208 lines at 23:24, §§0–3 on disk;
unreviewed; MEASURED by that slot, read here):

- **The nineteen sweep certificates do not ship the vector or its monomial
  ordering.** `B15-06/results/b18_06_sweep/S01..S19.json` record sizes, values
  at points and lift data, and say the vector is "reproducible from seed and
  prime". Slot 11 is regenerating each vector by the same construction and
  replaying the recorded values; whether the replay reproduces every recorded
  number is to be stated cell by cell in its §3, not yet on disk. Until then
  F11's certificates are **exact but not yet independently replayable from the
  tree**; the sweep's conclusions are unchanged, and the gap is a delivery
  gap, not a mathematical one.
- **Four third-party PDFs are committed on this worktree's own branch**
  (`b15-12-padding-orbit-bounds`, under `results/b15_12/sources/`, about
  1.2 MB, B15-era), and the four untracked PNG files this ledger noted at
  opening are page images of them. Two more PDFs and two full-text extractions
  sit untracked under `B15-01/results/b18_01/literature/`. Inventory only;
  remediation is the integrator's under separate authorisation. Recorded here
  so the ledger does not describe its own worktree as clean of literature.
- The first-wave input freeze (`results/b19_11/input_freeze.json`) pins the
  same hashes this ledger recorded in §1 for the documents both read
  (`4286e214…`, `d1690a3f…`, `14d80816…`, `a4520e2a…`, `ebc39b2c…`,
  `dc1cc655…`, `dca6de94…`, `0d30ec90…`, `60392996…`, `6ac744d6…`), and pins
  `b18_05_report.md` at `60979684…` **before** slot 05's addendum; the file is
  now `1af53479…`. Two independent pins, one difference, explained.
- Every inspected worktree is exactly one commit ahead of its pushed branch
  (the rules commit, ADOPTED by slot 11 from the launch note). No fetch since
  12 September. Consistent with the board assessment's published-state note.

## 7d. Update 23:28 — slot 05 intake (partial) and a correction to §4a

`B15-05/docs/b19_05_intake.md` appeared at 23:25 (63 lines, §§0–1, status IN
PROGRESS, SHA256 `7248272a…`). It nominates nothing, as briefed. Its §0 item 1
raises a point about the ten excluded ten-row cells that this ledger checked
and accepts as a correction to its own §4a:

**The nine cells other than `d = 27` are excluded only under an inherited
premise.** Exclusion of a positive gap needs a **lower** bound on `m_det`
against the padding ceiling `U`. An ideal floor `i_det >= k` gives only
`m_det <= a - k`, the wrong direction. The "D upper `= U - (a - i_det)`"
column in `b18_12_ledger.md` §4a (carried into §4a above) is therefore valid
exactly when `i_det` is **exact**, i.e. `m_det = a - i_det`. For the tail
`(19,2^8)` cell at `d = 27` the value `m_det = 418` is a determinant floor in
its own right (B15, and slot 05's "evaluation floor"), so that exclusion is
unconditional given `U = 288`. For the other nine, `i_det` is exact under
**premise P-S57**: the finite determinant ideal equals the stable ideal
intersected with the finite ambient filtration (`B15-04/docs/b16_04_proof.md`
§5, line "With S57's identification…"; accepted in the Batch 16 intake). Under
P-S57 every row's exclusion holds as tabulated; without it those nine rows
carry only a ceiling on `m_det` and exclude nothing.

Ledger action: the nine rows of §4a are relabelled **EXCLUDED under P-S57
(ADOPTED, B15/B16)**; the `d = 27` row stays **EXCLUDED, unconditional given
`U`**. The integrator's batch-18 check of §4a verified the arithmetic of every
row, not the direction of the `i_det` entries; the arithmetic is unchanged.
B17-12's closeout wrote "exact, conditional" and this slot's batch-18 ledger
wrote "floor"; slot 05 is right that those are opposite readings, and the
reconciled reading is the one above. **Nothing operational changes**: the ten
cells stay closed for every purpose the board has, since P-S57 is an accepted
premise and no slot proposes to revisit it; but a reader must not cite the
nine as premise-free exclusions.

Also from slot 05: the B18-05 generic-quartic control is repaired and
non-vacuous (§7b), so F9 no longer carries the integrator's repair condition,
only its two inherited premises.

## 7e. Update 2026-09-16, 07:19 — the first wave is closed; slot 10 never reported

Eight hours separate this entry from the last one (15 September, 23:28). This
slot wrote nothing in between. Everything below is read at 07:19 local
(America/New_York), not inferred from the gap.

**Every batch-19 artefact on disk, with bytes and hash as read at 07:19.**

| Slot | File | Lines | Bytes | Last write | SHA256 (prefix) |
|---|---|---:|---:|---|---|
| 01 | `B15-01/docs/b19_01_report.md` | 297 | 28821 | 15 Sep 23:21 | `aa136106…` — unchanged since §7a |
| 01 | `B15-01/docs/b19_01_review.md` | 110 | 7251 | 16 Sep 06:42 | `33b154e6…` |
| 02 | `B15-02/docs/b19_02_report.md` | 480 | 26915 | 15 Sep 23:31 | `52a9e474…` |
| 02 | `B15-02/docs/b19_02_review.md` | 113 | 8052 | 16 Sep 06:48 | `e28bcc93…` |
| 05 | `B15-05/docs/b19_05_intake.md` | 367 | 29818 | 15 Sep 23:33 | `dc074191…` |
| 11 | `B15-11/docs/b19_11_report.md` | 434 | 27479 | 15 Sep 23:27 | `30942342…` |
| 11 | `B15-11/docs/b19_11_review.md` | 131 | 7889 | 16 Sep 06:55 | `c9604f9e…` |
| 12 | `B15-12/docs/b19_12_ledger.md` | 595 | 46579 | 15 Sep 23:27 | `13d8e980…` — this file, before this entry |

**Absences, MEASURED at 07:19, not inferred.** `B15-10` holds no `b19_*`
artefact of any kind: neither `b19_10_review.md` nor `b19_10_report.md`
exists. `B15-05/docs/b19_05_review.md` does not exist. Slots 03, 04, 06, 07,
08 and 09 have no batch-19 artefact. No file in the batch has been written
since 06:55.

### 7e.1 Slot 02's report is substantively complete and textually truncated

`b19_02_report.md` carries **no status line**. Its §0 sets out eleven
sections and the file ends inside §8.1, at line 480.

| Announced in §0 | On disk |
|---|---|
| §§0–8.1 (verdict, intake, construction, closure lemma, criterion, pilots, verdict, what survives, lower bound) | present, self-contained |
| §9 the padded example and which lemma excludes it | **absent** |
| §10 the smallest linear-algebra problem, priced before computing | **absent** |
| §11 claims, negatives, one next test | **absent** |

The file has not changed since 23:31:57, so the session ended there rather
than pausing. This is recorded because it bears directly on §8.1's test and
not as a complaint: §9 and §10 are two of the four elements §8.1 required of
a *concrete construction*, and §11 is the labelled-claims section every other
slot in this batch delivered. **The integrator's review does not mention the
truncation**; it reviews §§0–8.1 and accepts them. Both facts are recorded;
neither is adjudicated here.

### 7e.2 The lineage fact that governs everything else in this batch

**Slot 10 produced nothing.** Whether it was launched and wrote nothing, or
never ran, is not visible to this ledger; only the absence is.

Consequence, and it is the most important structural fact about batch 19:
**every batch-19 acceptance is single-lineage.** What made the batch-18 base
of §2b strong was two independent lineages reaching the same verdicts
(F1–F7), with slot 10's verdicts formed before it read the intake. Nothing in
batch 19 has that. Both reviews say so in their own words and defer named
items to slot 10:

- B19-01 review §4: the Levi count (about 10,505 triples at `d = 7`) and the
  commutation argument are "marked as the slot's, pending slot 10"; §6 item 4:
  "Slot 10 should verify the Levi commutation argument and the 10,505 count;
  I did not."
- B19-11 review §1: its own cross-seam rebuild "is not a third lineage for
  the highest-weight construction itself".

So every batch-19 result enters this ledger as **REPORTED (unreviewed by 10)**
or **ACCEPTED (integrator only)**, and never as accepted by both. §2a stands
unchanged: **slot 10 has ruled on nothing in batch 19.**

### 7e.3 §3 resolution — slot 02's hypotheses, as they landed

The §7b table was written from a 13 KB partial. Here is where each entry
stands against the finished text. Producer labels are the producer's;
"integrator" means `b19_02_review.md`.

| ID | Where it landed | Label now | Ledger note |
|---|---|---|---|
| H-02a | Lemma 3.1 + §2: `I(D45) = ker phi^*`, `im phi^*_d ⊆ R_d` | PROVED (producer); formula and controls recomputed by the integrator at `d <= 4` | Lemma 3.1's proof is two lines and is the closure-correctness the rejected `MN = F·I4` lacked. Integrator-only acceptance. |
| H-02b | Lemma 4.1, Theorem 4.4 | PROVED (producer); `r_n(d)` recomputed independently by the integrator from `S_{4d}` characters | Thm 4.4 is F6 with slot 10's batch-18 relabel already applied: `m_det <= s <= g`. |
| H-02c | **The verdict**, Claim 6.1 + §5 | PROVED (producer), conditional on LLV — and **the LLV condition is now discharged** (below) | In the one case where the truth is known the criterion is provably silent across 320111 degrees, and `r/A` is *increasing* at every computed degree in both `n = 4` and `n = 5`. Integrator-only acceptance. |
| H-02d | Corollary 4.3 | PROVED on LLV and 03-A | Unchanged in substance; its LLV condition is discharged. |
| H-02e | **Corollary 8.1** — on disk and proved, not merely announced | PROVED on LLV and 03-A | *Stronger* than §2c item 2: batch 18 gave "no five-row separator below degree six"; this gives `I(D45)_d = 0` for **all** `d <= 5`, `ell(lambda) <= 4` included, via LLV and 03-A. A second lineage for the programme's own statement and an extension of it. |
| H-02f | **Theorem 7.1** (certification) on disk; **§7.3** states the missing lemma exactly | Thm 7.1 PROVED; the Missing Lemma is a statement of what nobody has, not a result | See 7e.4 for why Thm 7.1 changes no cell. |
| **H-02g** (new) | **Proposition 7.2**: `b` is the `S_lambda`-multiplicity of `R_d / (A_1)_d`, transposition-fixed part | PROVED (producer), flagged by the producer as definition-level | See 7e.5 — this is the entry that has to be read jointly with B19-01, and it is the one place where the two reports say something neither says alone. |

**LLV is no longer a hypothesis.** The integrator verified the citation
against the primary text, `arXiv:2303.09028v3`, and records the chain:
Corollary 3.1 identifies the linear determinantal family as `det(a,b)` with
`a_i = d+1`, `b_j = d+2`, which at `d = 4` is the pair `(5^4)/(6^4)`; Table 2
row `F1` carries that pair; Theorem 2 gives `deg F1 = 320112`; Proposition 1.1
gives irreducibility, so its ideal is principal. The CONDITIONAL flag is
lifted in Claim 6.1, Corollary 4.3 and Corollary 8.1.

**Precision that must travel with it (integrator):** the determinantal
quartic locus has **five** components, of degrees 320, 2508, 38475, 136512
and 320112. `D44` is `F1` specifically — the linear `4x4` family — and not
the union. "The four-variable determinantal locus has degree 320112" is
correct only with that reading, and this ledger uses no other.

Note that this discharges a *different* citation from H-Bez. **H-Bez
(refined Bézout, Fulton Ex. 8.4.6 / Thm 12.3) remains a secondary
quotation** and is untouched by this batch.

### 7e.4 §4b correction — the last degree-five cell is closed, and `D = -1`

§4b carried `(4,4,4,4,4)` as the one cell of the degree-five family with
`m_det` **undetermined**, closed only at `D <= 0` by padding vanishing. B19-02
§8.1 determines it, by a wrapped exact computation:

| quantity | value |
|---|---|
| `a`, by the Weyl alternant computed in-script | 1 |
| weight-space dimension `K` | 19834 |
| raising operators `E_12, E_23, E_34, E_45` | targets of dimension 17329, **51723 nonzero entries each** |
| highest-weight vector | primitive integer, 19834 nonzeros, max abs 41472, reconstructed from 2 primes |
| exact raising residues | all zero over `Z` |
| exact values at three determinant points | `-481390358496125537`, `6830962538921450404`, `4457433896125063706` |
| run | `analysis/b19_02_rect.py` `26f66bc4…`, one capped process, 19.7 s, 123 MiB, exit 0; certificate `results/b19_02/rect_4_4_4_4_4.json` |

A nonzero exact integer at an actual determinant point gives `m_det >= 1 = a`,
so `m_det = 1` and `i_det = 0`.

**The §4b row is replaced:**

| lambda | a | s | U | b | b_required | m_pad | m_det | D | closed by |
|---|---:|---:|---:|---|---:|---:|---:|---:|---|
| (4,4,4,4,4) | 1 | census (`s - a = 4`) | 0 | none | 0 (`U = 0`: no gate) | **0** | **1** | **−1** | `m_pad = 0` by padding vanishing (B18-01 Prop 8.4); `m_det = 1` by B19-02 §8.1 |

`D = -1` is the **integrator's arithmetic on the slot's measurement**: the
report stops at `i_det = 0` and does not state `D`. Recorded with that
attribution.

**Consequence for §4b as a whole.** The degree-five five-row family is no
longer "22 determined and one bounded". It is **fully determined: 22 cells at
`D = 0` exactly, one at `D = -1`.** The integrator's own batch-18
carry-forward — that `m_det` at `(4^5)` was knowable and unknown — is
retired. The §2c item 2 wording ("the rectangle `(4^5)` at `D <= 0` only, its
`m_det` undetermined") is superseded.

Three padding values in that cell were sampled zero. The report uses them for
nothing and so does this ledger: a sampled zero is not an identity, and
`U = 0` already gives `m_pad = 0` (roadmap correction 5).

**Ledger checks on §§5, 8.1 (elementary, not a review).** `A(d) = binom(69+d, d)`
reproduces 70, 2485, 59640, 1088430 at `d = 1..4`, matching the pilot table;
`28567510572002850 / 70724320184250 = 403.9`, matching the reported ratio;
`dim R = 80 - dim(SL4 x SL4) = 80 - 30 = 50` agrees with `dim D45 = 50` (F1),
and `64 - 30 = 34` agrees with `D44` being a hypersurface in the
35-dimensional space of four-variable quartics — two independent consistency
checks on the construction's frame. **One loose statement, which changes
nothing:** §5 says the ambient local exponent is "`K_A = 69` exactly" for
`n = 5`, but `K_A(d) = 69d/(d+1)` is 69 only in the limit (63.7 at `d = 12`).
It feeds only Claim 6.2, which its own author labels HEURISTIC, NOT PROVED,
and gives no weight; so it is noted, not carried.

### 7e.5 What the two reports say jointly, which neither says alone

This is the batch's substantive finding and it belongs in the ledger rather
than in either slot's report.

- **B19-02 Proposition 7.2** identifies the quantity the programme calls `b`:
  it is the `S_lambda`-multiplicity of `R_d / (A_1)_d`, the semi-invariant
  ring modulo the subalgebra generated by the determinant's own 70
  coefficients. That is the *ideal* boundary loss — what a perfect boundary
  test would return.
- **B19-01 Theorem 4.1 + §5** show that at `d = 6`, `lambda = (4^6)`, the
  B17-02/B18-02 arc returns `b = 0`, while `s - m_det >= 10 - 1 = 9`.

So: **here is what `b` ought to be, and here is a named cell where the
instrument returns zero instead.** The arc's `b` is a lower bound for the
ideal `b` and B19-01 shows it can be off by at least nine. Recorded as the
integrator states it, single-lineage, unreviewed by slot 10.

- **B19-02 §7.3's Missing Lemma** — exhibit one cell with a subspace
  `V ⊆ R_{d,lambda}`, `V ∩ (A_1)_{d,lambda} = 0`, `s - dim V < a` — is the
  same wall B19-01 reaches from the boundary side. Stated plainly: **nobody
  has exhibited one semi-invariant direction provably outside `C[D45]` in a
  named cell.** Two independent routes arriving at one obstruction is
  information, and it is the form in which this batch's negative should be
  written.

### 7e.6 §5 gates — no gate opens; one integrator proposal for slot 03

| Slot | Gate | Met? | State of the premise at close |
|---|---|---|---|
| 01 | theory first; hand any new cell to 05 and 10 before numerics | n/a | COMPLETE. Handed no cell (its §8.3). |
| 02 | theory first; no unconstrained 80-variable elimination; no bare `MN = F·I4`; no "degree is the only route" | **honoured** | Its §2 quantifies over no auxiliary matrix; §1 states the withdrawal explicitly; §6 disclaims the degree route. Report truncated at §8.1. |
| 03 | HOLD until 01 or 02 supplies a question that needs the computation | **not met** | 01 supplies a method and no target cell; 02 supplies a construction it proves cannot fire. No cell is nominated anywhere in the tree. |
| 04 | HOLD for an explicit equation or well-defined finite family | **not met** | No equation exists. `6 <= d_5 <= 4^49` is a bracket, not a family. |
| 05 | initial intake only; no census; nominate nothing in the first pass | **honoured** | COMPLETE (intake), nothing nominated, no census run, one 3.9 s control. |
| 06, 07, 09 | reviewed candidate / `B < U` / `r > B` | **not met** | No candidate; no `B < U` anywhere; §2.7 of the intake shows every open cell has `s >= a`, hence `B = a` and no headroom. |
| 08 | no assignment | **not met** | NOT_TRIGGERED. |
| 10 | frozen-hash verdict on completed deliverables | — | **no artefact** |
| 11 | delivery, contract additions, literature inventory; commits nothing | **honoured** | Report and packet delivered; one tracked contract edit left to the integrator. |

**One integrator proposal, recorded as a proposal and not as an opened gate.**
The B19-01 review §4 recommends that slot 03 be scoped to implementing the
Levi reduction and validating it against B18-02's twenty certified controls,
where `b` is already known to be `s - a` — a bounded task that needs no
nominated cell, and whose first outputs would reproduce twenty known values.
The ledger records this the way it records roadmap correction 3 (F13): **the
board's gate language is unchanged, no cell is nominated, and this is the
integrator's proposal awaiting the board.** It is also, on its own terms, a
validation task and not a search.

### 7e.7 §6 costs — everything batch 19 measured

| Item | Slot | MEASURED or ESTIMATED | Number | Note |
|---|---|---|---|---|
| `b19_01_band.py`, `b19_01_band6.py` | 01 | MEASURED wall time; memory bound **unverified** | 7.84 s, 2.31 s, exit 0 | as §7a: run under `timeout 60` / `ulimit -v`, **not** through the inspected Job-Object wrapper |
| Counting controls | 02 | MEASURED | 0.05 s | six controls, two of which had to fail and did |
| `n = 5` and `n = 4` sweeps to `d = 12` | 02 | MEASURED | 246 MiB and 486 MiB peaks, split one degree per process | **two cap hits recorded as cap hits**: `d = 1..12` in one process died `MemoryError` at 440 MiB under the 512 MiB Job Object, exit 1. Not a mathematical statement about `d >= 13`. |
| `b19_02_rect.py`, the `(4^5)` cell, `K = 19834` | 02 | MEASURED | 19.7 s, 123 MiB, exit 0 | the computation that closed the degree-five family |
| B18-05 generic-quartic control, full support | 05 | MEASURED | 3.9 s, 37.6 MB, exit 0 | through `b15_bound.py --seconds 60 --memory-mb 512` |
| Batch-18 vector regeneration and replay, 21 cells / 126 values | 11 | MEASURED (its own) | 21/21 `REPLAYED_ALL_MATCH` | integrator re-ran the `S19` cross-seam test independently and it passed |
| Levi screen at `d <= 7` | 01 | **ESTIMATED** | "seconds to a few minutes per cell", `<= 10,505` triples | count **not verified** by the integrator; pending slot 10 |
| Degree-six five-row sweep (105 cells) | — | **unpriced** | — | still not requested by the board |

**Active leases: none, for the whole batch.** No slot took one and the board
issued none.

### 7e.8 §7 completion states at close

| Slot | State | Review lineage |
|---|---|---|
| 01 | **COMPLETE** | ACCEPTED (integrator only); two items explicitly pending slot 10 |
| 02 | **COMPLETE IN SUBSTANCE, TRUNCATED IN TEXT** — §§0–8.1 delivered, §§9–11 announced and absent, no status line | ACCEPTED (integrator only), which does not remark on the truncation |
| 03, 04, 06, 07, 08, 09 | **NOT_TRIGGERED** | — |
| 05 | **COMPLETE (intake)**, nothing nominated | **unreviewed by anyone** |
| 10 | **NO ARTEFACT** | — |
| 11 | **COMPLETE** | ACCEPTED (integrator only) |
| 12 | **OPEN → CLOSED at §8.4 below** | — |

One correction to §7c, from the B19-11 review: the batch-18 sweep vectors
have since been **regenerated with explicit ordering and an expanded-ordering
hash and replayed against all 126 recorded point values, 21/21 matching**, and
the integrator independently rebuilt `S19`'s four raising operators across the
seam without project code and reproduced the recorded value
`33900369404217588856`. So the delivery gap §7c recorded is **closed**;
F11's certificates are now replayable from the tree as data. The remaining
small gap is that the packets carry values but not evaluation points.

## 8.4 The decision, transcribed

**STOP.**

The criteria in §8.1 were written at 23:23 on 15 September, before slot 02
had put anything on disk, precisely so that this paragraph would be a
transcription and not a composition. Read against them:

| Criterion (§8.1) | Slot 02 |
|---|---|
| **concrete construction** | **Partly delivered, then disproved by its author.** Delivered: explicit variables (70 `c_alpha`, 80 `b^(k)_ij`), explicit equations (the graph of `phi`), and a proof that its consequences vanish on the *entire* closure (Lemma 3.1) — the exact thing `MN = F·I4` lacked. Not delivered: the exclusion of the padded example or the lemma that would give it (§9, absent) and the bounded problem priced before computation (§10, absent). Decisively: Claim 6.1 **proves** the criterion cannot fire below degree 320112 in the one case where the truth is known, and `r/A` is measured increasing at every computed degree in both four and five variables. |
| **useful boundary criterion** | **No.** Proposition 7.2 says what `b` *is*; it certifies no `b` anywhere. §7.3 states exactly what is missing and says nothing in the tree supplies it. |
| **justified candidate** | **No.** No cell with `a > s` is known. Slot 05's intake nominates nothing and shows every open cell has `s >= a`, hence `B = a` and no headroom. |

That is the second branch of §8.3, and it is the branch the provisional
reading at 23:23 expected: **02 delivered a rigorous failure of its chosen
construction.** No downstream slot opens. 03, 04, 06, 07, 08 and 09 stay
NOT_TRIGGERED. By the board's own stopping rule this is the batch's result
and a success, not a shortfall.

**What the batch's result actually is.** The §8.3 sketch anticipated a
two-part negative. What landed is four parts, and two of them are positive
results that the §8.1 criteria could not register because neither opens a
slot:

1. **The arc is provably blind in a named region, and not exact there.**
   B19-01: if `lambda_1 + lambda_2 + lambda_3 <= 2d` then `b = 0` and
   `B = min(a, s)`, so no gap certificate is possible. The band is empty for
   `ell <= 5`, is the single rectangle `((2d/3)^6)` at `ell = 6` and only when
   `3 | d`, and is non-empty for `ell = 7..10`. At `(4^6)`, `d = 6`: `a = 1`,
   `g = 13`, `s = 10`, `b = 0` — nine dimensions the arc admits that cannot
   extend, so any exactness conjecture for this instrument is refuted, with no
   carrier run. **The five-row question is untouched**; the band is empty
   exactly where the search wants to look.
2. **The counting construction fails, quantified.** B19-02, above.
3. **The degree-five five-row family is now fully determined** — 22 cells at
   `D = 0`, `(4^5)` at `D = -1` — and **`I(D45)_d = 0` for every `d <= 5`**,
   all lengths, so the first five-variable determinant equation has degree at
   least six. The bracket is `6 <= d_5 <= 4^49`, lower end certified, upper
   end an existence statement that is never a budget.
4. **The two routes converge on one obstruction.** Nobody has exhibited one
   semi-invariant direction provably outside `C[D45]` in a named cell. That
   sentence is B19-02 §7.3 and B19-01's wall, and it is the same sentence.

**Two things this ledger will not let the result be written as.** First, "the
arc is blind" is **not** a general statement: it is blind in a precisely
identified region that does not contain the target, and the live question is
five rows at degree six or more. Second, every batch-19 result above is
**integrator-accepted only**; slot 10 ruled on nothing, and the Levi count and
commutation argument in particular are explicitly unverified. The batch's
negative is strong; its review lineage is half of what batch 18's was, and the
close document should say so.

**A third instance of the same failure mode, worth carrying.** B19-02's own
extrapolation, run on the four-variable control where the answer is known,
overshoots 320112 by a factor of `4.1 x 10^12`. The author therefore attaches
no weight to its five-variable figure and records it only as evidence against
the procedure. That is the second such instance after refined Bézout's
fourteen-to-fifteen orders (F3). **Two independent degree-estimating routes
have now each failed by twelve or more orders of magnitude in the one case
where they can be checked.** The programme should treat that as a standing
fact about degree estimates, not as two anecdotes.

## 11. Plain-language stocktake

Where the programme stands, in the terms of §0, with nothing smuggled between
boxes.

**What is actually known.** Below five rows, and above ten, there is nothing
to find: `D <= 0` in every degree at length at most four, and `m_pad = 0`
above length ten. At five rows, every cell of degree five is now closed, and
so is every equation of degree at most five in any number of rows — so the
first five-variable determinant equation, which B17 proved exists, has degree
between six and `4^49`. The ten ten-row cells stay closed, nine of them under
an accepted premise that a reader must not drop (§7d). Four degree-six
five-row cells and one at degree seven are settled. Everything else in the
admissible range is untested, which is not the same as excluded.

**What has never been produced, in four batches.** A single determinant
equation of length five to eight, written down. A single cell with a
certified `b >= 1`. A single cell with `B < U`. A single nominated candidate.
The binding constraint B18-06 named is still binding, unchanged.

**What batch 19 added.** Two instruments were pushed until they broke, and
both broke rigorously rather than ambiguously — which is the useful kind of
failure, because it says where not to spend. The boundary arc is provably
silent in a region that can now be tested for free by adding three parts of a
partition and comparing with `2d`. The semi-invariant counting criterion is
provably silent below degree 320112 in the one case anyone can check, and its
weakness has a named cause: it pays for the weight-`>= 2` semi-invariants,
which inflate the target ring without inflating the coordinate ring of `D45`.
Between them they closed the last open degree-five cell and tightened the
lower bound on the first equation to six. And they identified — from two
sides, independently — the one thing nobody in this programme has ever done:
exhibit a single direction provably outside `C[D45]` in a named cell.

**What would change the picture.** Not another sweep, and not another degree
estimate: two of those have now failed by twelve orders of magnitude apiece in
the only cases where they could be graded. What would change it is one
direction, in one named cell, proved new. Until someone has that, the honest
description of the programme is that it has excellent instruments for closing
cells and none for opening one.

**What this ledger is not saying.** It is not saying the five-row question is
closed; it is saying nothing in this batch touched it. It is not saying the
arc is useless; it is saying where it is silent. It is not saying `4^49` is a
search budget; the preamble forbids that and so does F3. And it is not saying
any batch-19 result has been adversarially reviewed, because none has.

## 9a. Labelled claims of this slot, at close

- **ADOPTED:** everything in §9; and LLV as a fact rather than a hypothesis,
  on the integrator's verification against `arXiv:2303.09028v3`, with the
  five-component precision of 7e.3 attached.
- **MEASURED (here):** presence, timestamps, line counts, byte counts and
  SHA256 of all eight batch-19 artefacts (7e); the absence of any `b19_*`
  artefact under `B15-10` and of `b19_05_review.md`, at 07:19; the truncation
  of `b19_02_report.md` after §8.1 and its lack of a status line.
- **CHECKED (here, elementary, not a review):** `A(d)` at `d = 1..4`; the
  `r/A` ratio at `d = 12`; `dim R = 80 - 30 = 50` against `dim D45 = 50`, and
  `64 - 30 = 34` against `D44` a hypersurface in 35-space; the `D = -1`
  arithmetic at `(4^5)`; the loose `K_A = 69` (7e.4), which carries nothing.
- **NOT REACHED:** no mathematics of any slot is asserted by this ledger. No
  cell, no `s` of its own, no `b`, no `r`, no gap.
- **DECIDED:** §8.4, STOP, by transcription from §8.1's criteria.

**One next sufficient test for whoever opens batch 20:** not a computation.
Read §7e.2 first and decide whether a batch whose every result rests on one
review lineage is closed out as it stands, or held for slot 10.

## 10a. Observation log, continued (2026-09-16, local time)

| Time | Observation |
|---|---|
| 16 Sep 07:19 | First wave read at close. 01, 05, 11 COMPLETE; 02 complete through §8.1 and truncated; three integrator reviews (06:42, 06:48, 06:55); `B15-10` empty. §§7e, 8.4, 11, 9a written. **Decision: STOP.** |


## 7e-bis. Update 2026-09-16 18:45 — state after the first wave (DUPLICATE of §7e, written without re-inspecting the file; superseded where it differs, see §12)

The background watch this slot set on slot 02 was killed by the system for
memory overnight; nothing was lost, and the state was re-read directly.

| Slot | State | On disk (SHA256 prefix) |
|---|---|---|
| 01 | REPORTED (unreviewed); status line COMPLETE | `b19_01_report.md` `aa136106…`, 297 lines, unchanged since 23:21 |
| 02 | REPORTED, **incomplete file** (§§0–8 of eleven announced; §§9–11 and a status line absent; unchanged since 23:31, nineteen hours); unreviewed | `b19_02_report.md` `52a9e474…`, 480 lines; `analysis/b19_02_{counting,extrapolate,rect}.py`; `results/b19_02/` (controls, `sweep_n5_*`, `sweep_n4_*`, `extrapolation.json`, `rect_4_4_4_4_4.json`) |
| 05 | REPORTED (unreviewed); COMPLETE (intake); nominates nothing | `b19_05_intake.md` `dc074191…`, 367 lines |
| 10 | **nothing on disk** after nineteen hours; no batch-19 ruling exists | — |
| 11 | REPORTED (unreviewed); COMPLETE (delivery) | `b19_11_report.md` `30942342…`, 434 lines; `results/b19_11/` (input freeze, literature inventory, 21 vector packets, manifest); `docs/delivery_contract.md` §11 appended (tracked file modified, as briefed) |
| 03, 04, 06, 07, 08, 09 | NOT_TRIGGERED | — |
| 12 | OPEN (this file) | — |

**Slot 02's verdict, transcribed from its §6 as written (unreviewed).** The
construction is the invariant-theoretic one: `C[D45]` is the subalgebra of the
`SL4 x SL4` semi-invariant ring `R` of five `4x4` matrices generated by the
seventy weight-one semi-invariants, and `r(d) < A(d)` would force a
determinant equation (Thm 4.2, closure-correct by Lemma 3.1 = B18-01 Prop 5.2).
Measured (`analysis/b19_02_counting.py`, six controls incl. two that had to
fail): in five variables `r/A` rises monotonically from 1.000 at `d = 1` to
403.9 at `d = 12`; in the four-variable control from 1.000 to 75.8. Claim 6.1
(PROVED conditional on LLV): in four variables the criterion cannot fire below
degree 320112. Claim 6.2 (HEURISTIC, not proved): the extrapolation that would
give a five-variable crossover near 700 overshoots the known four-variable
answer by `4.1·10^12`, so the producer attaches no weight to it and neither
does this ledger. **Verdict: as an instrument for producing the five-row
equation the construction fails, for a quantified reason.** Its §7.3 states
the missing lemma exactly: exhibit one five-row cell and a subspace
`V ⊆ R_{d,lambda}` with `V ∩ C[D45]_{d,lambda} = 0` and `s - dim V < a`.
Nothing in the tree exhibits one such direction. Its §7.2 identifies the
programme's `b` as the `S_lambda`-multiplicity of `R/C[D45]`: the same wall
the boundary arc hits, reached from the other side.

**§4 change — one degree-five cell sharpened (slot 02 §8.1, unreviewed).**
`(4,4,4,4,4)` at `d = 5`: `a = 1` (in-script Weyl alternant), weight space
19834, four raising operators with nonempty targets and 51723 nonzero entries
each, exact primitive highest-weight vector reconstructed from two primes (the
first attempt left it undetermined and is recorded), all residues zero over
`Z`, three exact nonzero values at determinant points. Hence `m_det = 1 = a`,
`i_det = 0`. With the inherited `m_pad = 0`:

| lambda | a | s | U | m_det | m_pad | D | closed by |
|---|---:|---:|---:|---:|---:|---:|---|
| (4,4,4,4,4), `d = 5` | 1 | 5 | 0 | **1** (was unknown) | 0 | **= -1** (was `<= 0`) | padding vanishing (B18-01) + determinant evaluation (B19-02 §8.1) |

So, if slot 02's certificate stands review, every one of the 23 degree-five
five-row cells has exact `D`: 22 at `D = 0` and one at `D = -1`; and
Corollary 8.1 (conditional on LLV and 03-A) reads `I(D45)_d = 0` for all
`d <= 5` with no exception. The first five-variable determinant equation has
degree at least six, now with the last cell certified rather than bracketed.

**§2c/§7d reconciliation.** Slot 05's intake independently reached the P-S57
labelling of the ten ten-row cells that §7d adopted; this ledger's adoption
was made *after* reading slot 05's §0, so the agreement is not two
independent lineages, and is recorded as one finding (slot 05's) checked here
against B16-04 §5. Slot 05's reconciled table (its §2) is the most complete
single cell table in the tree and supersedes §4a–4c above for any later
reader: it records `s`, `T`, `U` for all 23 degree-five and 4 degree-six cells
from the census, lists the open cells named in sources (§2.7), and labels
every screen by what it retired. It nominates nothing.

**§6 change — costs, all MEASURED, all under the cap.**

| Slot | Runs | Wall | Peak | Cap hits |
|---|---|---|---|---|
| 02 | counting sweeps `n = 5, 4`, split by degree; rectangle cell | `d = 11, 12` runs 246 and 486 MiB; rectangle 19.7 s, 123 MiB | 486 MiB | **two**: the single-process `d = 1..12` runs died with `MemoryError` at 440 MiB (receipts `b19_02_n5`, `b19_02_n4`, exit 1); recorded as cap hits, not as statements about `d >= 13` |
| 05 | one control run | 3.9 s | 37.6 MB | none |
| 11 | 21 replay runs | largest 14.56 s (S19) | 80.5 MiB | none |
| 01 | two runs (shell `timeout`/`ulimit`, not the Job-Object wrapper) | 7.84 s, 2.31 s | unverified | none |

Nothing in batch 19 needed or requested a lease.

## 8.4-bis The decision (recorded 2026-09-16 18:45; DUPLICATE of §8.4, same outcome; see §12)

**STOP. The batch's result is the focused two-session negative.**

Against the criteria of §8.1, on the evidence on disk:

| Criterion | 01 | 02 |
|---|---|---|
| concrete construction that can produce a five-row equation | not its remit | **no**: an explicit, closure-correct construction, shown by its own author to be unable to fire at any reachable degree, calibrated in the one case where the truth is known |
| useful boundary criterion (one that makes `b > s - a` provable or detectable in a cell with `a >= 1`, `U >= 1`) | **no**: a proved region where the arc is blind, a proved counterexample to exactness there, an unevaluated pre-screen that can only forbid runs | **no**: an exact identification of what `b` is (`R/C[D45]`) and the missing lemma, with no direction exhibited |
| justified candidate | **no** | **no** |

No gate in §5 opens: 03 has no question that needs the carrier; 04 has no
equation; 06, 07, 09 have no `B < U`, no `q`, no `r`. 08 has no assignment.
Slot 05's intake confirms, from every exclusion and screen in the tree, that
every open cell has `s >= a` and no certified `b`, hence no headroom.

**The batch's result, stated as the board's stopping rule asks:**

1. *Boundary side (01).* The B17-02/B18-02 arc is provably silent — `b = 0`,
   `B = min(a, s)` — in every cell with `lambda_1 + lambda_2 + lambda_3 <= 2d`,
   a band empty at length at most five and non-empty exactly at lengths six to
   ten; in that band exactness fails (`(4^6)_6`: `s = 10`, `a = 1`, `b = 0`),
   so the twenty-control regularity `s - b = a` was an artefact of a region
   that excludes the band. The five-row exactness question is untouched, and
   `b` is bounded above by a Levi branching number that has not been evaluated.
2. *Geometric side (02).* The semi-invariant-ring counting criterion, the only
   construction in the tree that reaches every determinant equation and is
   closure-correct without an existential quantifier, cannot fire below degree
   320112 in four variables and is measured moving away from firing in five;
   what is missing is one semi-invariant direction provably outside `C[D45]`
   in a named five-row cell (its §7.3), and no such direction is known.
3. *Side results that survive as scoped facts, pending review:* the last
   degree-five cell `(4^5)` closed with `D = -1` exactly, so the first
   five-variable equation has degree at least six with no exception; the ten
   ten-row exclusions relabelled with their premise (nine under P-S57, one
   unconditional); the nineteen sweep vectors now portable with their monomial
   orderings; the B18-05 control repaired and non-vacuous.

**What this decision is not.** It is not a theorem that no five-to-eight-row
determinant equation exists, that no multiplicity obstruction exists, or that
the boundary can never help; the board forbids all three readings and slots 01
and 02 both say so in their own honest-negatives sections. It is a decision
not to open six downstream sessions on premises that do not exist.

**Caveats that travel with the decision.** (a) Slot 02's report lacks its
announced §§9–11 and a status line; its verdict and missing lemma are
nonetheless fully on disk with certificates and receipts, and nothing the
absent sections could contain would supply a construction its §6 says does
not exist. (b) Slot 10 has ruled on nothing in batch 19; every batch-19 line
in this ledger is `REPORTED (unreviewed)`. If slot 10's closing ledger, when
it exists, rejects a load-bearing claim — Thm 4.1 of 01, Lemma 3.1 or
Claim 6.1 of 02, or the `(4^5)` certificate — the decision is re-read from
the §8.1 criteria, not re-argued. (c) The stop is the research launch's; the
administrative work of slots 10, 11 and the integrator's batch-18 closeout
continues and is not affected.

**One next sufficient test for the programme, with its price**, drawn from
the two reports rather than invented here: the cheapest test that could
reverse the negative is 02's missing lemma tried in one cell — take the
smallest five-row cell with `a >= 1` not yet closed (slot 05's §2.7 lists
`(8,7,7,1,1)_6`, `a = 2`, `s = 30`), and test whether the products of
weight-two semi-invariants with weight-one ones span any direction of
`R_{6,lambda}` outside the weight-one subalgebra; a single such direction
would give `b >= 1` and, since `s - 1 = 29 >= a`, would still not give
`B < a` there — so the test is a method proof, not a gap route, and it is
priced by 02 at the same order as its counting pilot (minutes, under
512 MiB) **only if** the `R_{6,lambda}` isotypic piece is built by characters
rather than by expansion. If that price does not hold on inspection, the
test is not affordable and the negative stands as the batch's last word.

## 11-bis. Closing log of the 18:45 session

| Time | Observation |
|---|---|
| 09-15 23:31 | Last write to `b19_02_report.md` (480 lines, §§0–8). Its §§9–11 never appeared. |
| 09-15 23:33 | `b19_05_intake.md` COMPLETE (367 lines). |
| 09-16 ~00:xx | Background watch killed by the system for memory (no data lost). |
| 09-16 18:41 | State re-read directly. Slot 10: still nothing. Receipts verified: slot 02's two `MemoryError` runs exit 1 at 462,118,912 / 462,602,240 bytes peak (about 440 MiB); split runs `d = 11, 12` exit 0 at 259 / 510 MB; rectangle cell exit 0, 19.7 s, 129 MB. |
| 09-16 18:45 | §7e and §8.4 written. **Decision recorded: STOP; the batch's result is the two-session negative.** |

Write footprint of this slot (`git status --porcelain`, this worktree):
`?? docs/b19_12_ledger.md` plus the six pre-existing untracked B15-era paths
noted at opening (four page images under `results/b15_12/sources/`, two
runtime receipts under `results/logs/`), none touched. No computation, no
lease, no git beyond the two `rev-parse` calls and `status --porcelain`.

## 12. Reconciliation of the two closes (written 2026-09-16 18:55)

This file was closed twice by the same slot, in two sessions that did not see
each other. The 07:19 session (§§7e, 8.4, 11, 9a, 10a) read the three
integrator reviews written at 06:42–06:55 and closed the ledger. The 18:45
session (§§7e-bis, 8.4-bis, 11-bis) resumed after its background watch was
killed overnight, re-read the slot reports directly, and appended a second
close **without re-inspecting this file first** — the very mistake the
preamble's "inspect the actual state before writing" exists to prevent. It is
recorded as this slot's own procedural error. Nothing is deleted; the
duplicate headings are marked and this section says which text governs.

**The decision is the same in both: STOP, the batch's result is the focused
first-wave negative.** Both closes read it off the §8.1 criteria written on
15 September before slot 02 had reported. No downstream slot opens.

**Where the two closes differ, §7e/§8.4 (07:19) govern**, because they read
the integrator reviews and the 18:45 text did not know they existed:

| Point | 18:45 text (superseded) | 07:19 text (governs) |
|---|---|---|
| Review status of 01, 02, 11 | "unreviewed" | ACCEPTED by the integrator (`b19_01_review.md` `33b154e6…`, `b19_02_review.md` `e28bcc93…`, `b19_11_review.md` `c9604f9e…`, all ACCEPT); **unreviewed by slot 10**, which produced nothing |
| LLV (degree 320112, the linear component `F1`) | kept CONDITIONAL | discharged by the integrator against `arXiv:2303.09028v3` (Cor. 3.1, Table 2, Thm 2, Prop. 1.1); five-component precision attached |
| The §7c delivery gap (sweep vectors without ordering) | still open | **closed**: 21/21 replayed, cross-seam test independently passed by the integrator |
| `(4^5)` at `D = -1` | unreviewed | integrator-accepted; `D = -1` is the integrator's arithmetic on the slot's measurement |
| Next test | the missing lemma tried at `(8,7,7,1,1)_6` (a method proof, not a gap route; price conditional) | "not a computation: decide whether a single-lineage batch is closed out or held for slot 10" |
| Slot 03 | HOLD, nothing needs it | HOLD, with the integrator's **proposal** (validate the Levi reduction against B18-02's twenty known controls) recorded as a proposal awaiting the board |

Where the 18:45 text adds something the 07:19 text lacks, it stands as a
supplement: the receipt-level verification of slot 02's runs (two
`MemoryError` cap hits at about 440 MiB, exit 1; split runs and the
rectangle cell exit 0) in §7e-bis; and slot 05's own cost line.

**Other changes to this worktree today, by another session of this slot at
18:05, not adjudicated here.** `docs/b18_12_ledger.md` was modified (its §13
log gained a 2026-09-16 row; hash now `575b1cae…`, so the pin `a4520e2a…` in
§1 above is the pre-modification value, and slot 11's freeze holds the same
pre-modification value); a batch-18 theory note
`docs/b18_12_coefficient_algebra.md` (`b998182a…`) with two bounded checks
under `analysis/b18_12_*` and `results/b18_12/` was written on request. That
note nominates no cell and produces no gap by its own §0; it is a batch-18
path, outside this ledger's remit, and is listed so the write footprint below
is complete.

**Write footprint of this worktree at 18:55** (`git status --porcelain`):
` M docs/b18_12_ledger.md`; `?? docs/b19_12_ledger.md`;
`?? docs/b18_12_coefficient_algebra.md`; `?? analysis/b18_12_ambient_table.py`;
`?? analysis/b18_12_fibre_check.py`; `?? results/b18_12/`; plus the six
pre-existing untracked B15-era paths (four page images of committed PDFs, two
runtime receipts). This session wrote only `docs/b19_12_ledger.md`. No
computation, no lease, no git beyond `rev-parse` (twice) and
`status --porcelain`.

**Status: CLOSED. Decision: STOP (§8.4).**
