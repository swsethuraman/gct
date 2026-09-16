# B18-01 review — the five-variable result, repaired

Integrator review. Report: `work/batch15_workers/B15-01/docs/b18_01_report.md`,
527 lines, sha256 `2ba3fc9c…2256` (confirmed here against the file on disk).
Worktree `B15-01`, started from `HEAD f12c0249`, `tree ce0a5f92`.

## Verdict

**ACCEPT.** The slot did what the board asked: it repaired what could be repaired,
withdrew what could not, and produced no separating equation — which was the expected
and correct outcome. Every measured claim I could check, I checked with my own code,
and all of them hold.

Two things make this a better delivery than its brief required. It caught that v1's
evidence did not exist, and it rebuilt rather than inheriting an unverifiable number.
And §8 poses the first concrete, cheap, well-formed test for a positive gap this
programme has had.

## 1. What I verified independently

Written from the statements, not from the slot's scripts. Different implementations,
different libraries.

| Claim | My method | Result |
|---|---|---|
| `dim D45 = 50` (review point 2) | Leibniz cofactor expansion, exact `Fraction` elimination, versus their `python_flint` | `rank_Q J = 50`, `rank_Q T = 30`, `T·J = 0` at **both** points — agrees exactly |
| No five-row cell below `d = 5` | plethysm `h_d[h_4]` by DP over multisets, Schur coefficients by the Weyl alternant | 0 five-row cells with `a > 0` at `d = 2, 3, 4` |
| Exactly 23 five-row cells at `d = 5` | same | **23**, exact |
| All 23 have `a = 1` | same | **all 23**, exact |
| `(4,4,4,4,4)` is among them | same | present |
| `d = 6`: 105 cells, 38 with `a = 1`, max `a = 7` | same | **105 / 38 / 7**, exact |
| The 23 `K(lambda)` weight multiplicities | coefficient of `x^lambda` in my monomial expansion | **23/23 agree**, including `K = 19834`, `11640`, `6869` |
| The slot's own control `sum a·dim S_lambda = C(69+d, d)` | recomputed independently | holds at `d = 2…6` |
| Prop 8.4 arithmetic | direct | `<mu,r> = 0`; `min <e_0+beta, r> = 1 > 0` |

Nothing disagreed. My scripts are `integrator_verify_b18_01_dim45.py` and
`verify_b18_01_deg5.py` / `_deg6.py`.

## 2. Direction of inference — checked line by line, and it is right

This is the programme's most expensive recurring error, so I read §8.3 adversarially.
It is correct throughout, and unusually explicit about it:

- `i_pad = 0` is certified by a **sampled nonzero** at a point of `R135`. Valid: a
  nonzero evaluation proves the function is not in the ideal, so `m_pad ≥ 1 = a`.
- `i_det = 1` is explicitly stated to be **unreachable by sampling** — "a sampled zero
  never gives `i ≥ 1`". Correct, and rarely said out loud.
- `m_det ≤ s ≤ g` is used as a **ceiling**: `g = 0` gives `m_det = 0`. A ceiling used
  as a ceiling.
- One exact nonzero `h_lambda(phi(B)) ≠ 0` retires a cell. Correct.
- §8.5: "there is **no** argument that `m_det = 0` in any of them. Equally, there is no
  argument that it fails." And: "It is **not** evidence that one exists."
- §8.6: a stage-1 sweep certifying nothing retires the family "**for the
  Kronecker-bound certificate route only** … not an exclusion of five rows."

That last one is `a failed method is not an excluded cell`, applied without being
prompted. The three strategic readings of v1 are withdrawn in the report's own words
and no row length is recommended or abandoned.

## 3. The result worth carrying

**In a cell with `a = 1`, separation and a positive multiplicity gap are the same
statement.** `m + i = a = 1` puts both kernels inside a line, so `K_det ⊄ K_pad` iff
`i_det = 1` and `i_pad = 0` iff `D = 1`. The coincidence is structural — it follows
from `a = 1`, not from anything B17 proved.

At `d = 5`, **every** five-row cell has `a = 1`. That is 23 cells, of which
`(4,4,4,4,4)` is excluded outright by a clean null-cone argument, leaving **22**.

So the degree-five family is the one place where the separation B17 established would,
if it landed there, *be* a gap rather than merely permit one. That is a genuinely new
handle and it costs about a minute to screen.

It is also, as the report insists, a construction problem and not a result. Nothing
proved here makes `d_5 = 5` more or less likely, and `dim D45 = 50` in `C^70`
constrains nothing at degree 5.

## 4. Conditions on acceptance

1. **Theorem 3.5's number is conditional and must never travel without its
   condition.** The bound `deg ≤ 4^49` rests on the refined Bézout inequality, which
   the slot could verify only through a secondary quotation (Sharir–Solomon,
   `arXiv:1411.0777`); the primary CBMS text was not reachable. The slot says so
   plainly and says that without it "only *finite* survives". The index entry carries
   that dependency in the status, not in a footnote. This is
   `boolean_without_its_margin`: a claim that asserts a bound ships what the bound
   rests on.
2. **`dim D45 = 50` is proved by the group action, not by the two points.** The ceiling
   holds because `phi(PBQ) = det(P)det(Q)·phi(B) = phi(B)` makes `phi` constant on
   `G`-orbits, so the 30 orbit directions lie in `ker dphi` everywhere. The two-point
   check is a consistency check on the implementation. The report states this
   correctly; the index entry must too.
3. **The Mumford pointer is unverified and is not used.** Correct handling. It stays
   out of the index.
4. **Stage-2 pricing is an estimate, not a measurement.** Batch 14's `cost_model` was
   2.4x low on the one slot where the window mattered. The 15 cells with `K ≤ 2825`
   are plausibly inside the default pilot; the five with `K` from 4,807 to 11,640 are
   not, and their "minutes and under 2 GiB" is unmeasured. No lease on that estimate —
   measure one mid-size cell first and re-price from it.

## 5. The gate is wrong for this route, and that needs fixing before anything is run

The board gates Slot 04 on "a reviewed cell with `B < U`" and Slot 09 on "an actual
`r > B`". **The degree-five `a = 1` route uses none of `U`, `B` or `r`.** With `a = 1`
the question is not a bound comparison at all; it is a direct occurrence question
answered by a Kronecker zero plus one exact nonzero evaluation.

Applied literally, the current gate either blocks the cheapest decisive test in the
batch or is satisfied vacuously. It should be amended to admit the `a = 1` route on
its own terms, with its own two certificates as §8.3 states them. That is a board
change, and I would not run stage 1 under the existing wording.

I have also not run stage 1 myself, deliberately. Producing that result and verifying
it in the same place would leave it with no independent check — which is the whole
point of this seat.

## 6. Coordination — two live sessions are affected

- **Slot 06** is running now, choosing cells by the size of the missing proof. It does
  not know about §8. The degree-five `a = 1` family is exactly the kind of thing it is
  meant to surface, and it is now settled fact rather than a candidate. 06's output
  should be read against §8 rather than merged with it blindly; if it nominates cells
  without reference to `a`, that is a gap in its brief, not a disagreement.
- **Slot 10** is reviewing the **v1** report. That is still the right job — v1's
  claims are what the board asked it to adjudicate — but its verdict lands against a
  report that has since been substantially withdrawn and repaired. Its findings on the
  degree bound, `dim D45` and `MN = F·I4` should be read as confirmation or challenge
  of the repair, not as live defects.

## 7. What enters the index

Proposed, pending the batch-18 close:

| id | statement | status |
|---|---|---|
| `dim_d45_is_50` | `dim D45 = 50` in `C^70`, `dim P(D45) = 49`. Lower bound an exact rational rank at an integer point; upper bound the 30-dimensional `G`-orbit directions in `ker dphi` at every point, `G = {(P,Q) : det P det Q = 1}` | PROVED; recomputed independently here |
| `a_one_is_separation_equals_gap` | In a cell with `a = 1`, `K_det ⊄ K_pad`, `(i_det, i_pad) = (1,0)` and `D = 1` are the same statement. Structural in `a`, not an inference from separation | PROVED |
| `five_row_cells_start_at_degree_five` | No five-row cell occurs in `Sym^d(Sym^4 C^5)` for `d < 5`. At `d = 5` there are exactly 23, **all** with `a = 1`. At `d = 6` there are 105, of which 38 have `a = 1` and the largest is 7 | MEASURED, exact; recomputed independently here |
| `rect_cell_is_in_the_null_cone` | `(4,4,4,4,4)` at `d = 5` has `i_pad = 1 = a`, so `D ≤ 0` and it cannot separate: `x_0 C` is destabilised by `r = (4,−1,−1,−1,−1)`, under which `h_lambda` has weight 0 | PROVED |
| `finite_degree_five_row` | Some exactly-five-row cell carries a determinant equation failing on padding, of degree at most `4^49` — **conditional on the refined Bézout inequality, which is verified only through a secondary quotation**. Without it, only finiteness survives. Not a search budget, not an equation, and it says nothing about `D` | PROVED conditional; dependency unverified against primary |
| `v1_evidence_did_not_exist` | The first B18-01 report named `out/b18_01_pilot.py` and `out/b18_01_control.py` as the evidence for its rank-50 measurement. Neither file existed anywhere. A measurement whose script is gone is not reviewable and must be rebuilt, not inherited | RECORDED defect, integrator's own |

## 8. The defect is mine

`v1_evidence_did_not_exist` is a consequence of the preamble I wrote, which told the
slot to write into `out/` — a directory with no meaning in the worktree model, in a
container that no longer exists. The first B18-01 run therefore produced a number with
no artifact behind it. I corrected the preamble before this batch launched, and this
session's report is the first under the corrected one; the slot found the problem
itself and rebuilt from scratch, which is the right response.

Third defect of mine this batch, and the same species as the other two: a document
whose parts disagreed with each other and which I did not read against itself before
issuing it.
