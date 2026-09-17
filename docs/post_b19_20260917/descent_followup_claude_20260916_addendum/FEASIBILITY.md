# Sparse-evaluator feasibility at `d = 5`, `lambda = (4^5)` — one cell only

Claude session, 17 September 2026. Fresh directory
`work/descent_followup_claude_20260916_addendum/` (did not exist at session start). The sealed
packet is read-only. Written incrementally; the decision line is at the end.

## 0. Question, scope, and what would count as an answer

**Question.** Can a sparse representation of the column tensor evaluate additional full-`H`
epsilon contractions of `M_(4^5)` at both (i) the transverse points `K5, K5+S, K5+2S`
(`S = x1 I4`) and (ii) useful old-arc forbidden-coefficient points, within one process, one
BLAS thread, 60 s and 512 MiB under the Windows Job Object wrapper?

**Not in scope.** The family `(4k)^5`, any census, any new carrier search, any heavy lease.
At most two numerical pilots, 120 s total including failures; stop on cap failure or
disagreement.

**Distinctions kept.** A rank-four old-arc minor would prove exactness in this cell; a
globally certified `z in ker C` with `C2(z) != 0` would prove an additional constraint;
neither produces a positive gap in this already excluded cell. This note produces
neither; it prices and (if priced in) verifies an evaluator.

## 1. Process state and inputs (read-only)

No `python` process was running at session start (`tasklist`). The sealed packet's 33
output hashes were re-verified (no mismatch). Inputs used: the two certified vectors
`q3, q7` (slot lists in `…/pilots/p6_basis.json`, fields `pi`, `rho`, listed slot order),
the transverse values in `…/pilots/p7_arc_S0.json` (`C2_values_at_K5_K5S_K52S`, modulo
`524287`), the P7 symmetric-part-zero points, the historical dense evaluator
`work/batch15_workers/B15-02/analysis/b18_02_carrier.py` (column tensors and
`Net.contract_pair`, SHA-256 `8670040e…`) and the sealed hand-ordered runner
`…/pilots/paired_runner.py`.

## 2. The sparse design (written before pricing)

Notation: columns `j = 0..3` (all four column tensors are the same wedge `D` of the five
matrices, heights `(5,5,5,5)`), slots `(j,k)`, `k = 0..4`, positions `c = 4a + b in {0..15}`.

`P_{pi,rho}(Y) = sum_{c: slots -> positions} prod_j D[c(j,·)] · prod_{B in pi} eps(a-values of B, listed order) · prod_{B in rho} eps(b-values of B, listed order)`.

- **Sparse column tensor.** `D[c_0..c_4] = det[(Y_i)_{c_k}]_{i,k}` is nonzero only if the
  five positions are distinct nonzero positions admitting a nonzero `5 x 5` minor. Store
  the minor for each *sorted* 5-subset of nonzero positions; an ordered entry is the sorted
  minor times the sign of the ordering. Sparse input does **not** make the contraction
  intermediates sparse by itself; the cost lives in the dynamic programme below.
- **Dynamic programme over columns.** Process columns in order `0,1,2,3`. Fix each block's
  argument order to be the *processing order* of its slots (column-major); the listed
  order of the sealed vectors differs from it by a fixed permutation per block, whose sign
  is a constant factor applied once. State = tuple of ten 4-bit masks (the values already
  inserted into each of the five row-epsilon blocks and five column-epsilon blocks).
  Inserting value `v` into a block with mask `m` contributes the sign `(-1)^{#(bits of m above v)}`
  and is zero if `v` is already in `m`.
- **Aggregation per column (the Astra trick).** For a column, an ordered entry affects the
  state only through, for each block touched, the *set* of values inserted and an internal
  sign; so ordered entries are aggregated into keys `(block -> mask)` with summed signed
  minors before the state update. Keys per column are bounded by the product over touched
  blocks of `C(4, slots of that block in the column)` and are counted exactly where
  affordable.
- **Transposed term.** `P_{rho,pi}` runs the same programme with row and column blocks
  exchanged; `q = P_{pi,rho} + P_{rho,pi}`.
- **Forbidden coefficients.** At points with all symmetric parts zero, scaling `a -> t a`
  gives `q(t) = q10 + t q11 + t^2 q12` (sealed §C.5, Lemma 4.1 plus the skew-degree bound
  12); `t = 0,1,2` determine the forbidden components and `t = 3` is a control node.
  **This holds for every such point, sparse or not**: the argument uses only `#Sigma = 0`
  and the degree bound, never genericity. Sparse arc points therefore yield valid rows of
  the forbidden matrix; whether the rows are nonzero or independent is a separate,
  measurable fact, and zero rows are not evidence of anything.

**Cost model (labelled).** Transitions `= sum_j states(j-1) · keys(j)` where
`states(j) <= min(prod_{partially filled blocks} C(4, filled), states(j-1) · keys(j))`.
ESTIMATE: 2–5 µs per transition in CPython dict arithmetic; about 200 bytes per live
state (a 10-tuple of small ints plus a Python integer); live arrays: the support dict,
one column's key dict, two consecutive state dicts; the transposed term doubles the work.
Pricing is exact for supports and for the key counts listed in `q1_price.json`; all
timing numbers are estimates until measured in Stage B.

**Patterns priced.** `q3`, `q7` (certified) and one additional cross-pairing pattern
`cross_x` (row blocks pair columns `(0,1),(2,3)`, column blocks pair `(0,2),(1,3)`, one
leftover block each; explicit slot lists in `q1_price.json`) — the kind whose dense plan
needed `4^14` intermediates.

**Points priced.** `K5, K5+S, K5+2S`; two proposed sparse symmetric-part-zero points
`S0A`, `S0B` (each matrix: one entry among `a, r_i, c_i` and one skew pair) at nodes
`t = 0..3`; the recorded P7 point 0 (dense, 10–13 nonzeros per matrix) for comparison.

**Stage A pass criterion.** The Stage B check (two vectors at three transverse points and
at one sparse arc point with four nodes, both orientations, plus one corrupted-input
control) must have a transition bound consistent with well under 60 s at 5 µs per
transition, i.e. below about `5·10^6` transitions, and a state bound below about `10^6`.
Otherwise: feasibility unresolved, no Stage B.

## 3. Stage A results (pilot Q1, `pilots/q1_price.py` → `q1_price.json`; MEASURED counts, bounds as labelled)

Run under the Job Object wrapper: 1.69 s wall, peak job memory 14,614,528 bytes, exit 0
(`results/logs/q1_price_resources.json`). Exact key counts were computed for `K5` (`t = 0, 1`,
all patterns and orientations), for `K5+2S` (`q3` only) and for the sparse arc point `S0A`
at node `t = 1` (`q3`, one orientation); every other entry uses the product bound
`prod C(4, slots in column)` = 20736 per column.

### 3.1 Supports (exact)

| point | nonzeros per matrix | nonzero positions | 5-subsets with nonzero minor | ordered entries |
|---|---|---|---|---|
| `K5` | 4,2,2,2,2 | 12 | 64 | 7,680 |
| `K5+S`, `K5+2S` | 8,2,2,2,2 | 16 | 128 | 15,360 |
| `S0A` (`t=1,2,3`) | 3,3,3,3,3 | ≤ 15 | 48 | 5,760 |
| `S0A` (`t=0`) | 3,3,3,3,2 | | 32 | 3,840 |
| `S0B` (`t=1`) | 3,3,3,3,3 | | 30 | 3,600 |
| P7 point 0 (dense, for comparison) | 11,10,13,13,12 | 13 | 819 | 98,280 |

Sparse input does give a small column support. It does **not** give small intermediates,
as the next table shows.

### 3.2 Keys, state bounds and transition bounds

`states(j) <= min(prod_{partially filled blocks} C(4, filled), states(j-1)·keys(j))`;
transitions `= sum_j states(j-1)·keys(j)`. Per orientation (the symmetrised vector needs two).

| point | pattern | exact keys per column | state bound after col. 0,1,2 (tightened) | transitions (bound) |
|---|---|---|---|---|
| `K5` | `q3` | 1308, 1308, 1308, 1308 | 1308, 36, 20736 | `2.9·10^7` |
| `K5` | `q7` | 1064, 1308, 1064, 1308 | 1064, 1,391,712, 20736 | `1.5·10^9` |
| `K5` | `cross_x` | 1064 ×4 | 1064, 46656, 20736 | `7.3·10^7` |
| `K5+S` | `q3` | 2720 ×4 | 2720, 36, 20736 | `6.4·10^7` |
| `K5+S` | `q7` | 2256, 2720, 2256, 2720 | 2256, 6,136,320, 20736 | `1.4·10^10` |
| `K5+S` | `cross_x` | 2256 ×4 | 2256, 46656, 20736 | `1.6·10^8` |
| `K5+2S` | `q3` | 2720 ×4 | as `K5+S` | `6.4·10^7` |
| `S0A, t=1` | `q3` (one orientation) | 1170 ×4 | 1170, 36, 20736 | `2.6·10^7` |

Where keys were not counted exactly the bound is `8.6·10^8` (`q3`), `1.3·10^12` (`q7`),
`1.8·10^9` (`cross_x`) per orientation and is not informative.

**Reading.** The dominant term is always the third column: after two columns the number
of partially filled blocks makes the state bound 20736 (`q3`, `cross_x`) or `1.4·10^6`
to `6·10^6` (`q7`, whose pairing leaves both leftover blocks and one whole column pair
open), and the third column contributes `states · keys ≈ 2·10^4 · 10^3` at best. The
symmetrised vector doubles this. At the labelled estimate of 2–5 µs per CPython transition,
even the cheapest single evaluation (`q3` at `K5`, `2.9·10^7` per orientation) is
60–300 s, above the 60 s cap, and the full Stage B check (two vectors, three transverse
points, four arc nodes, both orientations, plus a corrupted control) is bounded by about
`2.3·10^13` transitions with the loose entries, and by well over `10^10` with the exact
ones because of `q7`. **The pre-registered pass criterion (`< 5·10^6` transitions,
`< 10^6` states) fails for every pattern at every point.** Stage B was therefore not run.

**What this does and does not show.** These are upper bounds on the state dynamic
programme as designed; reachable states may be fewer than the bound (the tightening
`states(j-1)·keys(j)` is already applied, and the bound after the third column is the
loose `20736`). No measurement of actual reachable states exists, so the sparse method
is **not shown to exceed the cap**; it is shown to be **unpriceable below the cap with
the available bounds**. The 2-GiB dense intermediate of the sealed report and these
bounds are both costs of particular evaluators, not of the mathematics (corrigendum B).

### 3.3 Memory (estimate)

At most one column's key dictionary (≤ 2720 keys × ~100 bytes) and two consecutive state
dictionaries are live. With states bounded by `2·10^4` (`q3`, `cross_x`) memory is a few
megabytes; for `q7` the `6·10^6` state bound would be about 1.2 GB at 200 bytes per
state and is over the cap on its own, if reached. ESTIMATE, not measured.

## 4. Decision

**Feasibility unresolved within this bounded attempt.** One of two pilots was used
(1.7 s of the 120 s). Stage A's bounds exceed the pass criterion for all three patterns
at every required point, dominated by the third-column state count, so the smallest
implementation check was not executed, and no sparse evaluation was cross-checked against
the preserved values. Nothing here changes the certified partial result (`s = 5`,
`a = m_det = 1`, `2 <= rank C <= 4`, `C2` globally necessary and nonzero, independence
from `C` unresolved).

## 5. If a continuation is wanted (not launched here)

- **Exact inputs.** `q3`, `q7` slot lists (`…/p6_basis.json`), the transverse points
  `K5, K5+S, K5+2S`, the sparse points `S0A`, `S0B` (`q1_price.json`, field
  `proposed_sparse_S0_points`) at nodes `t = 0..3`, the preserved P7 values for the
  transverse cross-check, and the historical dense evaluator for the arc cross-check at
  the sparse points (about 0.55 s per vector per node, so ~9 s for both vectors at four
  nodes: affordable and already measured in the sealed packet).
- **Engine.** The same state dynamic programme with masks packed into one 40-bit integer
  and a compiled inner loop (`numba` is present in the inspected environment,
  `b15_runtime_control.py` imports it; no dependency change). ESTIMATE 10–50 ns per
  transition compiled, i.e. `2.9·10^7` transitions in about a second and `q7`'s `10^9`–`10^10`
  in 10–500 s: `q7` may still fail the cap and would be the first thing measured.
- **Maximum new contractions.** None in the first run: the run is the Stage B check
  (two certified vectors, three transverse points, one sparse arc point with four nodes,
  one corrupted-input control). If it passes within 60 s, at most **12 new
  contraction patterns** in a second run, chosen with `q3`-type pairings only (third-column
  state bound `20736`), each evaluated at the three transverse points and at `S0A`/`S0B`
  with three nodes; independence tested by modular rank against the preserved `q3, q7`
  values at the same points.
- **Resource estimate.** Two pilots, 60 s / 512 MiB each, compiled; measured reachable
  states recorded per column. ESTIMATE, not feasibility.
- **Stopping rule.** Stop at the first disagreement with a preserved value, at the first
  cap hit, or when three further independent vectors are certified (then the sealed
  rank-four test applies, with the sealed S0 three-node extraction, in this cell only).
  A rank-four forbidden minor would prove exactness here; a certified kernel vector with
  `C2 != 0` would prove an additional constraint; neither gives a gap.

## 6. Receipts and labels

- Pilot Q1: wrapped, 1.69 s, 14.6 MB peak, exit 0. No other numerical pilot was run.
- **MEASURED:** supports, exact key counts where listed, state products.
- **ESTIMATE:** all timings and memory; the per-transition constants; the compiled-engine
  figures.
- **NOT REACHED:** any sparse evaluation, any cross-check, the corrupted-input control,
  any new contraction.

Decision: **feasibility unresolved within this bounded attempt.**
