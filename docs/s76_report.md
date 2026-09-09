# Session 76 — scale the recursion to `δ = 24`, and measure `C₂₄`

*(batch 12; the reconciled proposal's s75, second half.)*

2026-09-09.  Branch `s76-scale24` off `main` at `afb8c3319d3d`.
Pre-registration `results/PREREG_s76.md` committed at `69c5d73` before any
measurement.  Bundle `s76_scale24.bundle` + `.md5`.  House wording
(`docs/brief_wording.md` §2, §4).  Author block where one is needed:
Swami Sethuraman / swsethuraman@beneficus.ai / Beneficus AI.

## 0. What landed

Both halves of the brief's success criterion, not one:

1. **`C₂₄ = 17 778`, exactly** (MEASURED, two independent routes).  The brief's
   estimate `≈ 1.7 × 10⁴` was right to 5 %; `C₂₄/B₂₄ = 8.20`, `C₂₄/a₂₄ = 64.9`.
2. **The recursion scales to the goal cell without stopping anywhere.**  Built
   in Young's seminormal form and memoised over the 7 658-node shape DAG, it
   reaches `λ₂₄ = (65,17,2⁷)` in **32 minutes per prime on two cores**, at both
   house primes, and returns a **deterministic 274-dimensional source** as the
   kernel of an `8 100 × 2 168` system inside the `17 778`-dimensional
   `K′`-invariants.  On the way it re-derives `B₂₄ = 2 168` by a route
   independent of `wk11_int_b24.py`, the ladder predecessor's `273`, the whole
   LMR `a`-ladder, `C₂₄` a second time, and the plethysm coefficient at every
   node of the DAG — `3 677` nonzero multiplicities out of `7 658` — with
   **zero disagreements** against every independent value available
   (§4.3).
3. **The four evaluation columns are not reached** — the pre-registered
   expectation, on the brief's first stopping rule.  The step and the
   quantities are named in §5, and so is what s77 needs from this session.

Everything below separates MEASURED / PROVED / RECORDED / EXPECTATION.

## 1. Gate, environment, base

- `main = afb8c3319d3d1f3afc3d2578c8cb322f2b8a3b92`;
  `docs/batch12_s1_s2_consolidated.md` present.
- `tools/verify/selftest.py`: 12 cases, PASSED — **after installing
  `python-flint`**, which was absent from the container (the preamble says it
  is installed; it was not — an environment gap, recorded here as the preamble
  asks, not a result).  `Singular`, `msolve`, `sympy`, `numpy`, `scipy` present.
- `two_strip_paths(24)`: **160 paths over 42 shapes**, identical to `δ = 14`
  (160 / 42) and against 36 / 23 at `δ = 12` — the saturation the brief states.
- `wk11_int_cdelta.py 12 60` did not finish inside its 60-second budget
  (the first shape alone has 4 374 Weyl terms); the same engine's functions
  were driven with a finer checkpoint instead (§2).
- s75 had not reported; nothing of its interface was in the tree.  The build
  is against the specification, with its assumptions recorded
  (`PREREG_s76.md` §4 and §6 below).

## 2. `C₂₄` exactly (Question A)

`C_δ = Σ_{λ→μ→ν two-strip paths} a_{δ−2}(ν) = Σ_μ B_{δ−1}(μ)` — the dimension
of `(S^{λ_δ})^{K′}`, `K′ = H_{δ−2} × S₄ × S₄`, the space the block swap
actually works in.

**Instrument** (`analysis/wk12_s76_c24.py`): the functions of
`analysis/wk11_int_cdelta.py` — `weyl_terms` (pruned Weyl alternation, terms
collapsed by sorted key) and `wk9_s42_census.N_S_tail_n` (tail DP) — driven
with a per-50-key / 30-second checkpoint, two workers over the 42 shapes, one
banked JSON per shape (`results/s76_c24/shape_NN.json`).  Only the checkpoint
granularity and the worker split differ from the engine that produced `B₂₄`
and `C₁₂`.  94 770 Weyl terms in all; 51 CPU-minutes.

**Result** (`results/s76_c24.json`): `C₂₄ = 17 778` over 160 paths, 42
shapes, all 42 channels nonzero, largest channel 272, smallest 8.

| `ν` at `δ = 22` | `a₂₂(ν)` | paths through `ν` | contribution |
|---|---|---|---|
| `(57,17,2⁷)` | **272** | 1 | 272 |
| `(58,16,2⁷)` | 234 | 2 | 468 |
| `(58,17,2⁶,1)` | 199 | 2 | 398 |
| `(59,15,2⁷)` | 180 | 3 | 540 |
| `(59,16,2⁶,1)` | 163 | 4 | 652 |
| `(59,17,2⁵,1,1)` | 43 | 1 | 43 |
| `(59,17,2⁶)` | 245 | 3 | 735 |
| `(60,14,2⁷)` | 150 | 4 | 600 |
| `(60,15,2⁶,1)` | 130 | 6 | 780 |
| `(60,16,2⁵,1,1)` | 32 | 2 | 64 |
| `(60,16,2⁶)` | 215 | 6 | 1 290 |
| `(60,17,2⁵,1)` | 175 | 2 | 350 |
| `(61,13,2⁷)` | 109 | 5 | 545 |
| `(61,14,2⁶,1)` | 102 | 8 | 816 |
| `(61,15,2⁵,1,1)` | 28 | 3 | 84 |
| `(61,15,2⁶)` | 166 | 9 | 1 494 |
| `(61,16,2⁵,1)` | 145 | 4 | 580 |
| `(61,17,2⁵)` | 211 | 1 | 211 |
| `(62,12,2⁷)` | 88 | 4 | 352 |
| `(62,13,2⁶,1)` | 78 | 8 | 624 |
| `(62,14,2⁵,1,1)` | 19 | 4 | 76 |
| `(62,14,2⁶)` | 141 | 10 | 1 410 |
| `(62,15,2⁵,1)` | 118 | 6 | 708 |
| `(62,16,2⁵)` | 187 | 2 | 374 |
| `(63,11,2⁷)` | 60 | 3 | 180 |
| `(63,12,2⁶,1)` | 58 | 6 | 348 |
| `(63,13,2⁵,1,1)` | 16 | 3 | 48 |
| `(63,13,2⁶)` | 103 | 9 | 927 |
| `(63,14,2⁵,1)` | 94 | 6 | 564 |
| `(63,15,2⁵)` | 146 | 3 | 438 |
| `(64,10,2⁷)` | 47 | 2 | 94 |
| `(64,11,2⁶,1)` | 41 | 4 | 164 |
| `(64,12,2⁵,1,1)` | 10 | 2 | 20 |
| `(64,12,2⁶)` | 85 | 6 | 510 |
| `(64,13,2⁵,1)` | 73 | 4 | 292 |
| `(64,14,2⁵)` | 127 | 2 | 254 |
| `(65,9,2⁷)` | 29 | 1 | 29 |
| `(65,10,2⁶,1)` | 29 | 2 | 58 |
| `(65,11,2⁵,1,1)` | 8 | 1 | 8 |
| `(65,11,2⁶)` | 58 | 3 | 174 |
| `(65,12,2⁵,1)` | 55 | 2 | 110 |
| `(65,13,2⁵)` | 94 | 1 | 94 |
| **`C₂₄`** | | **160** | **17 778** |

The twelve `B₂₃(μ) = Σ_{ν ⊂ μ} a₂₂(ν)`, which are the precursor dimensions of
the predecessors (and the column counts of their kernel systems in §4):

| `μ` | `B₂₃(μ)` | `a₂₃(μ)` (banked) |
|---|---|---|
| `(65,15,2⁶)` | 1 260 | 166 |
| `(65,14,2⁶,1)` | 970 | 102 |
| `(65,13,2⁷)` | 785 | 109 |
| `(64,16,2⁶)` | 1 600 | 215 |
| `(64,15,2⁶,1)` | 1 262 | 130 |
| `(64,14,2⁷)` | 1 062 | 150 |
| `(63,17,2⁶)` | 1 946 | 246 |
| `(63,16,2⁶,1)` | 1 608 | 163 |
| `(63,15,2⁷)` | 1 365 | 180 |
| `(62,17,2⁶,1)` | 1 999 | 199 |
| `(62,16,2⁷)` | 1 756 | 235 |
| `(61,17,2⁷)` | 2 165 | 273 |
| sum | **17 778** | **2 168** |

Pre-registered checks: **A1** every channel `≥ 0` (all 42 are `≥ 8`);
**A2** the ladder shape `(57,17,2⁷)` returns the banked `a₂₂ = 272`
(s57/s63 ladder) — the analogue of `B₂₄`'s `273` self-check; **A3**
`17 778 ≥ 2 168`; **A4** the twelve `B₂₃` sum to `C₂₄`.  All pass.

**Second route.**  The recursion of §4 computes `a₂₂(ν)` at the same 42
shapes as kernel dimensions, with no Weyl alternation and no tail DP: the
values agree at every shape and the sum is again `17 778`.

## 3. The operator, stated and built (Question B, part 1)

`W_δ(ν) = (S^ν)^{K_δ} = ⊕_{ν/ξ} M_{δ−1}(ξ) ⊗ c^{ν/ξ}` and
`M_δ(ν) = W_δ(ν) ∩ Fix(τ)`, where the block swap `τ` is a genuine involution
on `(S^ν)^{K′} = ⊕_{(ξ,η)} M_{δ−2}(η) ⊗ (S^{ν/η})^{S₄×S₄}` (it normalises
`K′`) but does not preserve `W_δ`.  The implementation
(`analysis/wk12_s76_seminormal.py`):

- **Model.**  `S^ν` in Young's seminormal form, uniform rule
  `s_i e_T = ρ e_T + (1 − ρ) e_{s_iT}`, `ρ = 1/(c(i+1) − c(i))`; `+1` / `−1`
  on same-row / same-column pairs.  Coxeter relations verified on assorted
  skew diagrams (`selftest()`).  Every denominator is an axial distance
  `< 97`; both house primes invert it — this is what "no prime below 97"
  buys, and it was honoured everywhere.
- **Strip invariants.**  For a horizontal 4-strip `ξ/η` (a disjoint union of
  row segments, so `S^{ξ/η} ≅ M^{(k₁,k₂,…)}`), the trivial `S₄`-vector
  `c^{ξ/η} = ⋂ ker(s_i − 1)` in the seminormal basis of standard fillings,
  normalised to coefficient 1 on the lexicographically first filling.  It
  depends only on the strip's diagram up to translation.
- **Recoupling.**  For a two-strip skew diagram `D = ν/η`, the block swap
  `τ = (1 5)(2 6)(3 7)(4 8)` acts on the seminormal skew module `S^D` (up to
  1 120 standard fillings at the goal cell, 2 520 in principle); the
  `(S₄×S₄)`-invariants have the basis `u_ξ = c^{ξ/η} ⊗ c^{ν/ξ}` over the
  intermediate shapes `ξ`, with **pairwise disjoint supports** (the first four
  entries of a filling decide `ξ`), so `R^D` is read off the supports and the
  full identity `τu_ξ = Σ_{ξ'} R_{ξ'ξ} u_{ξ'}` is then verified entry by
  entry — that verification *is* the statement that `τ` preserves the
  invariants.  `R² = I` is checked for every diagram.  Computed exactly over
  `Q` for the 42 goal-cell diagrams (`results/s76_recoupling_goal.json`,
  PROVED-by-computation) and in `F_p` with numpy for the bulk
  (`recoupling_modp`; agrees with the exact route on all 42 goal-cell
  diagrams, `selftest()`).
- **Base cases** (B0, PROVED-by-computation): at `δ = 2` the one-dimensional
  channels carry `τ = +1` on `(8), (6,2), (4,4)` and `−1` on `(7,1), (5,3)`,
  i.e. `h₂[h₄] = s₈ + s₆₂ + s₄₄`.
- **The system at a node.**  A vector of `W_d(ν)` is a coefficient vector
  `c ∈ F_p^{B_d(ν)}` over the stored bases of the `M_{d−1}(ξ)`; its
  `K′`-coordinates are read off the stored matrices `E_{d−1}(ξ)`; `τ − I`
  acts block-diagonally over `η` as `(R^{ν/η} − I) ⊗ I_{a_{d−2}(η)}` on the
  `ξ`-index.  Only the `m_η − f_η` independent rows of `R^{ν/η} − I` are used
  (`f_η = dim Fix R^{ν/η}`), so the system has `Σ_η (m_η − f_η) a_{d−2}(η)`
  rows and `B_d(ν)` columns; its kernel, in reduced row echelon form, is
  `E_d(ν)`, an `a_d(ν) × B_d(ν)` matrix.  `python-flint` `nmod_mat` for every
  kernel and rank.

**At the goal cell** (RECORDED in `results/s76_recoupling_goal.json`): 42
channels `η`, `m_η ≤ 10`, `Σ_η m_η a₂₂(η) = 17 778 = C₂₄`;
`dim Fix(τ)` on the `K′`-invariants `= Σ_η a₂₂(η) f_η = 9 678` (B4); the
reduced system is **`8 100 × 2 168`**, and `M₂₄ = W₂₄ ∩ Fix(τ)` is its
kernel, of dimension **274** — not `9 678`, not `2 168`.  Two channels,
`(59,17,2⁵,1,1)` and `(65,11,2⁵,1,1)`, have `m = 1` and `R = −1`: they
contribute nothing to `Fix(τ)`.

**Saturation, made precise.**  At the goal cell the 42 channels use **41**
distinct skew diagrams (two `η` give translates of the same diagram), and
that set is the same for every rung `δ ≥ 14`.  Over the whole DAG, however,
**118 787 distinct two-strip skew diagrams** occur (`results/s76_skew_diagram_census.json`,
peaking at 15 289 per level around `δ = 16`) — the saturation is a statement
about the top of the ladder, not about the recursion below it.  Each diagram's
recoupling is computed once; at 50 ms in `F_p` this is a few minutes in
total, and it was the whole cost until it was moved out of exact rational
arithmetic (the first implementation spent 99 % of its time there).

## 4. The recursion over the DAG (Question B, part 2)

`analysis/wk12_s76_recursion.py`, bottom-up over the shapes reachable from
`λ₂₄` by removing horizontal 4-strips: `7 658` nodes (`1 + 5 + 22 + … + 12 + 1`;
the integrator's `7 656` counts `δ = 1..23`), 585 per level at `δ = 12..16`.
One level of `E` matrices is held at a time; every level is written to disk
(`results/s76_dag/level_DD_pP.npz`, not committed — 128 MB per prime,
regenerated deterministically in 32 minutes) and the dimension table to
`results/s76_dag_dims_pP.json` (committed).

### 4.1 Per-level cost (MEASURED, `p = 2147483647`; the other prime is within seconds)

| `δ` | shapes | nonzero | `Σ a` | `Σ a·B` stored | max `B` | max rows | max `C` | s |
|---|---|---|---|---|---|---|---|---|
| 1 | 5 | 1 | 1 | 1 | 1 | 0 | 0 | 0.0 |
| 2 | 22 | 3 | 3 | 3 | 1 | 1 | 1 | 0.0 |
| 3 | 63 | 8 | 8 | 14 | 3 | 2 | 5 | 0.0 |
| 4 | 127 | 20 | 24 | 78 | 6 | 8 | 15 | 0.3 |
| 5 | 199 | 42 | 63 | 428 | 14 | 22 | 46 | 1.3 |
| 6 | 271 | 72 | 154 | 2 055 | 26 | 59 | 119 | 3.5 |
| 7 | 343 | 113 | 337 | 8 524 | 51 | 127 | 258 | 8.5 |
| 8 | 415 | 162 | 690 | 30 638 | 89 | 275 | 563 | 15.6 |
| 9 | 486 | 220 | 1 308 | 97 241 | 152 | 489 | 1 004 | 27.1 |
| 10 | 545 | 264 | 2 309 | 276 333 | 237 | 884 | 1 817 | 39.3 |
| 11 | 577 | 283 | 3 687 | 697 267 | 370 | 1 415 | 2 918 | 52.4 |
| 12 | 585 | 292 | 5 257 | 1 509 655 | 531 | 2 201 | 4 545 | 65.3 |
| 13 | 585 | 292 | 6 705 | 2 742 280 | 761 | 3 285 | 6 792 | 85.7 |
| 14 | 585 | 292 | 7 837 | 4 193 766 | 1 032 | 4 590 | 9 508 | 113.3 |
| 15 | 585 | 292 | 8 632 | 5 563 030 | 1 304 | 5 839 | 12 123 | 142.0 |
| 16 | 585 | 292 | 9 147 | 6 651 913 | 1 548 | 6 993 | 14 535 | 175.7 |
| 17 | 575 | 290 | 9 459 | 7 416 426 | 1 768 | 7 872 | 16 382 | 185.3 |
| 18 | 441 | 247 | 9 457 | 7 895 323 | 1 935 | 8 419 | 17 537 | 199.4 |
| 19 | 314 | 199 | 9 012 | **8 091 452** | 2 041 | 8 739 | 18 213 | 200.3 |
| 20 | 194 | 147 | 8 065 | 7 905 874 | 2 104 | 8 911 | 18 579 | 193.3 |
| 21 | 100 | 90 | 6 586 | 7 183 944 | 2 139 | 8 996 | 18 760 | 168.5 |
| 22 | 42 | 42 | 4 563 | 5 761 475 | 2 157 | 9 033 | 18 840 | 132.0 |
| 23 | 12 | 12 | **2 168** | 3 449 051 | 2 165 | **9 047** | **18 870** | 77.8 |
| 24 | 1 | 1 | **274** | 594 032 | 2 168 | 8 100 | 17 778 | 13.9 |

`Σ a` is the level's total multiplicity (`Σ_ν a_d(ν)`); `Σ a·B` the entries
stored for the level; `C` the full `K′`-invariant dimension of a node and
"rows" the reduced row count actually solved.  Total: `1 906 s` per prime;
`95 746` multiplicity dimensions over the DAG; `70 070 803` stored entries in
all.

**The peak weighted state count** the brief asks for: **`8 091 452` stored
entries at `δ = 19`** (32 MB as `uint32`; the nodes are cheap, the
multiplicities are not, and the multiplicities are still small).  The largest
system solved is **`9 047 × 1 999`** at `(62,17,2⁶,1)`, `δ = 23`, whose
`K′`-invariants have dimension `18 870` — larger than the goal cell's own
`17 778`.  Peak resident memory, re-measured on the largest node alone, is 0.67 GB (the
system as an `int64` array plus its `python-flint` copy) once the seminormal
caches were bounded (the first implementation reached 2.5 GB at `δ = 7` by
caching every skew module's Fraction matrices; that was a defect in the
worker, not in the route).

### 4.2 What the top returns (MEASURED, both primes)

- `a₂₄(λ₂₄) = 274`: the kernel of the `8 100 × 2 168` system.
- **`B₂₄ = 2 168` re-derived**: the twelve `δ = 23` kernel dimensions are
  `166, 102, 109, 215, 130, 150, 246, 163, 180, 199, 235, 273` — the values in
  `results/wk11_int_b24.json` one by one — by a route with no Weyl
  alternation and no tail DP in it.  The ladder predecessor `(61,17,2⁷)`
  returns `273`.  The brief's worry ("that number now sizes the whole route
  and has one implementation behind it") is closed: it has two.
- **`C₂₄ = 17 778` a second time**, from the 42 `δ = 22` kernels.
- The LMR `a`-ladder from the recursion, `δ = 12..24`:
  `2, 39, 93, 145, 188, 219, 241, 255, 264, 269, 272, 273, 274` — s57/s63's
  values exactly.
- The `δ = 12` control (B2), as a by-product: `B₁₂ = 31`, `C₁₂ = 239`,
  `dim M₁₂ = 2`; the 23 `δ = 10` channels of `results/wk11_int_c12.json`
  reproduced.  This is the *dimension* half of s75's control; its evaluation
  half is not claimed (§5).
- The source `E₂₄`: `274 × 2 168`, reduced row echelon form, column blocks
  over the twelve predecessors in `horiz_strips` order with widths
  `a₂₃(μ)`; `205 998` nonzero entries of `594 032`.  Banked at both primes
  (`results/s76_source24_p2147483647.npz`, `…p2147483629.npz`, 0.9 MB each).
  The two primes give **identical pivot columns and identical zero patterns**
  — what the reductions of one rational object look like.  Deterministic:
  given the prime and the conventions of §3, the recursion returns this
  matrix and no other.

### 4.3 The checks (B1) — 0 mismatches anywhere

| reference | nodes | source | result |
|---|---|---|---|
| symmetric-function plethysm `wk8_s30_pleth.amb`, every DAG node `δ ≤ 8` | 1 446 (of which 1 446 compared, zero and nonzero alike) | independent route (characters, power sums) | agree |
| `results/wk11_int_c12.json`, `δ = 10` | 23 | Weyl alternation | agree |
| s57/s63 LMR ladder, `δ = 12..24` | 13 | banked | agree |
| `results/s76_c24.json`, `δ = 22` | 42 | Weyl alternation (this session) | agree |
| `results/wk11_int_b24.json`, `δ = 23` | 12 | Weyl alternation | agree |
| fresh Weyl-alternation spot checks at unbanked nodes, `δ = 9..23` (`analysis/wk12_s76_spotcheck.py`, seeded sample, `results/s76_weyl_spotchecks.json`) | 106 (65 nonzero, 41 zero) | `wk9_s42_census.a_weyl` | agree |
| second house prime, every node | 7 658 | the same recursion at `2147483629` | agree |

What a dimension check does and does not certify: a wrong recoupling matrix or
a wrong strip invariant changes kernel dimensions generically, and over 1 600
independent values (plus the second prime) leave no room for that.  What it
cannot see is a *consistent* rescaling of the strip invariants — that
conjugates every `R` by a diagonal and rescales the coordinates of every
`E_d(ν)` channel by channel without moving a single dimension.  That freedom
is exactly the normalisation recorded in `PREREG_s76.md` §4.1, and it is the
first thing s77's bridge has to fix (§5).

### 4.4 Two side observations (MEASURED, both primes, not pre-registered)

- **Projection ranks.**  The rank of the projection of `M₂₄` onto each
  predecessor block `M₂₃(μ) ⊗ c^{λ/μ}` (`results/s76_source24_projections.json`)
  is full (`= a₂₃(μ)`) for ten of the twelve channels — including the ladder
  block, `273`, as `uM₂₃ ⊂ M₂₄` requires — and deficient for two:
  `(65,14,2⁶,1)`: `94` of `102`; `(62,17,2⁶,1)`: `156` of `199`.  A modular
  rank is a lower bound, so the two deficits are two-prime evidence, not
  theorems; the ten full ranks are proved (full rank at one prime).
- **Nonzero nodes.**  `3 677` of the `7 658` DAG nodes carry a nonzero
  multiplicity; the per-level count of nonzero shapes is flat at 292 across
  `δ = 12..16`, matching the flat 585-shape plateau.

## 5. The evaluation columns (Question C): not reached, and why

The pre-registered expectation held.  The source of §4 is a vector of
coefficients over bases that are themselves coefficient vectors, down to
`δ = 1`; nothing in it is a polynomial in the 495 coefficients of a quartic,
and nothing in it can be paired with a `det₄` pencil, a reducible `ℓ·c`, the
true padded `ℓ·per₃` or an unpadded `per₄` point.  The brief's first stopping
rule applies.  The step, and the quantities:

- **The step** is the conversion of a compact vector into any evaluable
  representation.  Two routes exist and both are carrier-scale:
  (i) unfolding along the DAG into the native carrier — at each node the
  `a_d(ν)` basis vectors as explicit weight-`ν` polynomials of
  `Sym^d(Sym⁴C⁹)`, i.e. `N_S(ν,d)` coefficients each; at the goal cell that
  is **`274 × N_S = 274 × 1.56 × 10¹¹ ≈ 4.3 × 10¹³`** coefficients (s63's
  `N_S = 156 438 903 314`); (ii) unfolding into the `(S₄)²⁴`-invariant
  Gelfand–Tsetlin basis of `S^λ` — the 4-strip tableaux of `λ₂₄` — of which
  there are **`K_{λ₂₄,(4²⁴)} = 70 233 345 083 979 459 756 ≈ 7.0 × 10¹⁹`**
  (computed here by the strip DP; `7.9 × 10⁷` at `δ = 12`).  The compact
  representation is `C₂₄ = 17 778` coordinates: a compression of `10⁷`
  against the monomial carrier and `10¹⁵` against the GT carrier, which is
  why the recursion runs in half an hour and why it cannot evaluate.
- **Why there is no shortcut inside the recursion.**  The evaluation
  functional at a point `f` is itself a vector `ψ_f ∈ M₂₄` (it is
  `H₂₄`-invariant); the four columns are ranks of Gram-type matrices
  `⟨e_i, ψ_{f_j}⟩`.  Computing `ψ_f`'s 274 compact coordinates is the same
  problem: any transfer-matrix contraction of `f^{⊗24}` along the block chain
  carries a bond space of the size of the weight lattice of `V_{λ^k}` — the
  native carrier in disguise.  This is an argument on the page, not a
  theorem of impossibility; it is recorded as the reason no exploratory
  attempt was made.
- **What s77's bridge needs from here** (the interface, in the tree):
  1. the coordinate conventions of §3 — the seminormal rule, the strip
     invariant normalisation (coefficient 1 on the first standard filling),
     `horiz_strips` order for column blocks, reduced row echelon kernels;
  2. the 42 goal-cell recoupling matrices exactly over `Q`
     (`results/s76_recoupling_goal.json`) and the generator for every other
     diagram (`recoupling_modp`, `recoupling_D`);
  3. the top source at both primes and the dimension table of every node;
     every level's `E` matrices regenerate in 32 minutes;
  4. the one scalar per strip type that relates the seminormal Pieri
     embedding `M_{d−1}(ξ) ⊗ c^{ν/ξ} → M_d(ν)` to the circuit's "adjoin the
     new letter in the strip" map (the antisymmetriser of a column absorbs
     that of its sub-column, so the circuit map is the Pieri map up to a
     scalar depending on the strip and the column lengths) — **not
     computed here**; with it and a straightening basis at each node the
     unfolding costs what the recursion costs, without it the unfolding is
     (i) or (ii) above.

Nothing about `i_det`, `i_pad`, `U_D`, `U_P` or `D` is claimed.  The decision
table was not entered.

## 6. Assumptions carried, corrections, and flags for the integrator

- s75's interface was absent; the assumptions of `PREREG_s76.md` §4 stand:
  every *dimension* in this report is independent of the strip normalisation,
  the *coefficients* of every `E_d(ν)` are not.
- `python-flint` was not installed in the worker container.  The preamble
  states that it is; batch 12's other sessions should check on arrival.
- `results/wk11_int_bdelta.json` in the tree holds only the `δ = 24` row
  (`B₂₄`); the `δ = 12, 13, 14, 16, 18` rows quoted in
  `docs/s1_s6_batch11_review.md` §3 are not in the file, so the predecessor
  multiplicities at `δ = 11, 12, 13, 15, 17` could not be used as references.
  The recursion supplies all of them now (`results/s76_dag_dims_p*.json`).
- The brief's "roughly 90 chunked evaluations of the `B₂₄` cost class" for
  `C₂₄` is not how the cost falls: 94 770 tail DPs at `δ = 22` dominated by
  the 4 374-term nine-row shapes (3 minutes each), 51 CPU-minutes in all.
- `wk11_int_cdelta.py`'s checkpoint is per shape and only when its budget
  expires; a run ended otherwise loses the shape in progress.  The driver
  here checkpoints every 50 keys; the engine itself was not modified.
- The brief says the recoupling combinatorics "at the top of the ladder are
  identical to those at `δ = 14`"; true (41 diagrams, `δ ≥ 14`), but the
  recursion below the top meets 118 787 diagrams, so a session that expected
  ~40 recouplings in total would have been surprised.  It costs minutes, not
  hours, in `F_p`.
- The seminormal caches must be bounded: an unbounded cache of Fraction
  matrices over 100 000 skew modules is a memory fault, not a mathematical
  wall.  Recorded so it is not rediscovered.
- The batch-12 preamble asks for a `Co-Authored-By: Claude Opus 5` trailer.
  The commits here carry `Co-Authored-By: Claude Fable 5.1`, the model that
  did the work; the trailer is otherwise as the preamble asks (no session
  link, no URL).
- No `D`, no obstruction, no verification-protocol trigger.

## 7. Deliverables

| file | what |
|---|---|
| `results/PREREG_s76.md` | pre-registration (`69c5d73`) |
| `analysis/wk12_s76_c24.py`, `results/s76_c24/`, `results/s76_c24.json` | `C₂₄` driver, 42 banked channels, the assembled result |
| `analysis/wk12_s76_seminormal.py` | seminormal form, strip invariants, recoupling (exact and `F_p`), selftest |
| `analysis/wk12_s76_recursion.py` | the memoised recursion over the DAG |
| `analysis/wk12_s76_spotcheck.py`, `results/s76_weyl_spotchecks.json` | 106 independent Weyl values at unbanked nodes |
| `analysis/wk12_s76_summary.py`, `results/s76_recursion_summary.json` | the two-prime summary |
| `results/s76_recoupling_goal.json` | the 42 goal-cell recoupling matrices over `Q`, `Fix(τ)` bookkeeping |
| `results/s76_dag_dims_p2147483647.json`, `…p2147483629.json` | `a_d(ν)` at all 7 658 nodes, per-level statistics |
| `results/s76_source24_p2147483647.npz`, `…p2147483629.npz` | the 274 × 2 168 source at each prime |
| `results/s76_source24_projections.json`, `results/s76_skew_diagram_census.json`, `results/s76_amb_refs.json`, `results/s76_dag_control12_dims.json` | side data |
| `results/logs/s76_*.log` | selftest, gate, both recursion runs, both `C₂₄` workers, spot checks |
| `docs/s76_report.md` | this report |

Not committed (5 MB rule): `results/s76_dag/level_DD_pP.npz`, 128 MB per
prime — the nested source below the top; `python3
analysis/wk12_s76_recursion.py --top 24 --prime P --check-amb 8` regenerates
it bit for bit in 32 minutes.
