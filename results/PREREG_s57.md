# PRE-REGISTRATION — session 57, the rank-loss selector

Committed **before** any computation of this session.  Branch `s57-selector`,
off `main` at `0960bd548eae4a9767276f9a1f20d686538c3374` (the tip of the clone;
`git merge-base --is-ancestor` passes for `6cef4a2` (s54), `3f65cca` (s51),
`0f8c08a` (integrator batch review) and `92f7887` (s55 merge)).

Two things were done before this commit and are disclosed: (i) the record was
read (`docs/s52_report.md`, `docs/s55_report.md`, `docs/pieri_transport.md`,
`results/sixrow_record.md`, `results/occurrence_screen.md`,
`results/longweight_screen.md`, the ledgers, the s39/s42/s52 code); (ii) the
number of cells in the brief's region was counted by a partition-counting
recursion (arithmetic, not a measurement): **12,707,460 cells**, of which
12,464 / 21,925 / 37,112 at `δ = 10 / 11 / 12` — the counts at `δ = 10, 11, 12`
agree with the candidate counts of `results/longweight_screen.md` per `(δ, ℓ)`.
No `a`, `sk`, `h_pad`, `N_S` or rank was computed before this commit.

Labels throughout: **proved** / **measured** / **adopted-from-literature** /
**expectation**.  This session performs **no rank measurement** and reports no
`D`; the `D > 0` verification protocol therefore cannot be entered.  Any
statement of the form `i_det ≥ 1` that this session makes is a *theorem
conditional on exact integers computed here* (two routes or two moduli), and is
labelled so — never as a measured `D`.

## 0. What the brief asks, and the two pre-checks

The brief (`docs/s57_prompt.md`, this batch) asks for (1) a table over the
region `6 ≤ ℓ(λ) ≤ 10`, `10 ≤ δ ≤ 24`, `|λ| = 4δ`, `λ_1 ≥ δ` of `a`, `sk`,
`h_pad`, `ℓ`, `δ`, balance and an `n_χ` estimate; (2) a prior for where
`rank Θ⁺_{λ,δ} < a(λ,δ)` (`i_det ≥ 1`), argued against evidence; (3) the score
of that prior against the negative record.

**§7 (functoriality) pre-check.**  No new invariant is proposed.  The statistic
whose rank drop is being located is `mult_λ C[D_ℓ]` (coordinate-ring
multiplicities), the first row of the §7 table, which passes by the surjection
`C[W] ↠ C[D_ℓ]`.  A selector ranks cells for that statistic; it is not itself a
statistic evaluated at points.  Passed by construction.

**§5 (degeneracy-direction) pre-check.**  Not applicable as a point evaluation
(nothing here is evaluated at a `det_4` pencil, at `ℓ·c`, or at the ten-variable
`ℓ·per_3`).  Its substance — *does the proposal also fire on the padded
permanent side?* — is carried by the `h_pad` column: at every nominated cell the
table states the pad-forced kernel `max(0, a − h_pad) ≤ i_pad`, so that a cell
where `D > 0` would need `i_det > a − h_pad` is never nominated as if one kernel
vector sufficed, and `h_pad = 0` cells (Lemma A of s52: `mult_pad = 0 ⇒ D ≤ 0`)
are excluded from the ranking.

## 1. The one piece of theory the session will use (stated now, proved in the report)

**Lemma L (first-row transport).**  Fix `ℓ`, `W = Sym^4 (C^ℓ)^*`, and let
`c ∈ C[W]_1` be the coefficient of `s_1^4` — the highest-weight vector of
`C[W]_1`, of weight `(4)`.  Let `X ⊆ W` be an irreducible `GL_ℓ`-stable closed
cone not contained in `{c = 0}` (`X = W, D_ℓ, P_ℓ, R_ℓ` all qualify).  Write
`λ⁺ = (λ_1 + 4, λ_2, …, λ_ℓ)`.  Multiplication by `c` induces injections of
highest-weight spaces

    (C[W]_δ)^{hw}_λ ↪ (C[W]_{δ+1})^{hw}_{λ⁺},   (I(X)_δ)^{hw}_λ ↪ (I(X)_{δ+1})^{hw}_{λ⁺},   (C[X]_δ)^{hw}_λ ↪ (C[X]_{δ+1})^{hw}_{λ⁺},

so that, with `i_X = a − mult_X`,

    a(λ⁺, δ+1) ≥ a(λ, δ),   mult_X(λ⁺, δ+1) ≥ mult_X(λ, δ),   i_X(λ, δ) ≤ i_X(λ⁺, δ+1) ≤ i_X(λ, δ) + [a(λ⁺, δ+1) − a(λ, δ)].

In particular `a(λ⁺, δ+1) = a(λ, δ)` forces `i_X(λ⁺, δ+1) = i_X(λ, δ)`.
*(Proof sketch: `c` is `U`-invariant of weight `(4)`, `C[W]` and `C[X]` are
domains, `c ≠ 0` on `X`.  Full proof in the report.)*

A **ladder** is the set of cells `{(4δ − |λ̄|, λ̄) : δ}` for a fixed tail
`λ̄ = (λ_2, …, λ_ℓ)`; every cell of the region lies on exactly one ladder, and
Lemma L makes `a`, `mult_det` and `i_det` non-decreasing up each ladder.  The
session will use Lemma L in three ways, all mechanical once `a` is known:

- **dead by transport**: a cell above a measured `i_det = 0` cell on its ladder,
  with the same `a`, has `i_det = 0` (proved, given the measurement);
- **live room**: above a dead cell, `i_det ≤ a(cell) − a(dead cell)`;
- **downward forcing**: `i_det(λ, δ) ≥ i_det(λ⁺, δ+1) − [a(λ⁺, δ+1) − a(λ, δ)]`;
  applied below the one cell of the region where `i_det ≥ 1` is known —
  `(65, 17, 2^7)` at `δ = 24`, `ℓ = 9`, the LMR module (s50, s55).

## 2. The table — columns, sources, and coverage fixed now

Per cell: `δ, ℓ, λ, a, sk, h_pad, bal = λ_1 − λ_ℓ, N_S, |Stab|, n_χ~ = ⌈N_S/|Stab|⌉`
(an **estimate**, per s46's correction, not a bound), `pad_forced = max(0, a − h_pad)`,
a status per column (`value` / `pending` / `lower bound`), and the ladder tail `λ̄`.

Sources and routes:
- `a`: for `δ ≤ 12` the s39 C engine table `results/longweight_screen.csv`
  (re-verified here: every `δ = 10, ℓ = 6` cell recomputed by the independent
  Weyl-alternation route `wk9_s42_census.a_weyl`, plus a random sample of 60
  cells across the other `(δ, ℓ)` chunks); for `δ ≥ 13` the C plethysm engine
  (`wk9_s39_chars.PlethEngine`, `N ≤ 64`) where affordable and the Weyl route
  above that, each cell by two routes or two moduli.
- `sk`: for `δ ≤ 12` the s39 table; for `13 ≤ δ ≤ 16` the C engine
  (`MdetEngine`, `N ≤ 64`) on the targeted families of §3 only; **`δ ≥ 17`:
  `pending`** (session 58's problem, per the brief).  Where the C engine is used
  at `N > 48` the CRT bound is re-checked against `f^λ` (not `f^rect`) before a
  value is accepted.
- `h_pad`: the s42 definition (`mult S_λ ⊂ Sym^δ V ⊗ Sym^δ(Sym^3 V)`, the Pieri
  sum over the cubic plethysm), cubic plethysm by the C engine at `d = 3`.
- `N_S`: the tail DP (`wk9_s42_census.N_S_tail_n`) where the tail box is at most
  `2·10^7` entries; otherwise the 5-variable merged-weight **lower bound** and
  the status `lower bound`.

Coverage, fixed now:
- **C1** census counts for every `(δ, ℓ)` of the region (exact, all 75 chunks);
- **C2** every cell at `δ = 10, 11, 12` (71,501 cells): all columns;
- **C3** `13 ≤ δ ≤ 16`: the targeted families F1–F5 of §3, all columns
  (`sk` included);
- **C4** `17 ≤ δ ≤ 24`: the families F1–F4, `a`, `h_pad`, `N_S` only; `sk`
  pending;
- **C5** if time allows after C1–C4: `a` for every `ℓ = 6` cell at `δ = 13`
  (6,288 cells), extending the ladder profiles one degree.
Everything else is `pending`, keyed by `(δ, λ)` so it can be filled without
redoing the rest.  The committed table is `results/s57_selector.md` (summary
tables and the nominee list) plus per-chunk `results/s57_cells/*.csv.gz`, each
under 5 MB.

## 3. The families (fixed now, before any value is seen)

- **F1 — the LMR ladder**, `λ̄ = (17, 2^7)`, `ℓ = 9`: cells
  `(4δ − 31, 17, 2^7)` for `δ = 12, …, 24` (`δ = 12` is the ladder bottom,
  `(17,17,2^7)`; all thirteen are in the region since `4δ − 31 ≥ δ` for `δ ≥ 11`).
- **F2 — the peaked ladders** `λ̄ = (2^{ℓ−1})`, `ℓ = 6..10`: the tightest
  `sk − a` family of s38/s39.
- **F3 — the LMR shape at the other lengths**, the weights `λ(k,4) =
  (8k+17, 2k+5, 2^{k+1})` at `δ = 3(k+2)`: `k = 3, 4, 5` (`ℓ = 6, 7, 8`,
  `δ = 15, 18, 21`) and `k = 7` (`ℓ = 10`, `δ = 27`, outside the region; its
  ladder `λ̄ = (19, 2^8)` enters the region at `δ = 14`), and their ladders.
- **F4 — the most balanced eligible cell of each `(δ, ℓ)`**: `λ_1 = δ`, the
  remaining `3δ` boxes spread as evenly as possible over `ℓ − 1` rows (the
  minimiser of `λ_1 − λ_ℓ` subject to `λ_1 ≥ δ`), plus the next four in the
  balance ordering.
- **F5 — the record's ladders**: every ladder through a measured cell of the
  negative record (`results/sixrow_record.md` plus the length-5 ledgers of
  s36 and s54), continued to `δ = 16`.

## 4. The criteria to be scored (fixed now)

Each criterion is an ordering of the cells of a `(δ, ℓ)` slice; a cell's
*percentile* is its rank divided by the slice size (0 = first nominee).

- **K1 balance**: ascending `λ_1 − λ_ℓ` (most balanced first).
- **K2 closeness**: ascending `sk/a` (target barely larger than source first).
- **K3 LMR proximity**: ascending distance to the LMR shape, measured as
  `|λ_2 − (2k+5)| + Σ_{i≥3} |λ_i − 2|` with `k = ℓ − 3`, ties by `λ_1`.
- **K4 frontier**: ascending `δ` then ascending `n_χ~` among cells not dead by
  transport.
- **K5 new room** (from Lemma L): descending `a(cell) − a(last dead cell below
  on the ladder)`, with cells dead by transport removed and cells with no dead
  cell below scored by `a`.

The negative record used for scoring: the 210 six-row cells of
`results/sixrow_record.md` (rebuilt from the ledgers by the s52 parser plus
`results/s52_ledger.jsonl`), and the length-5 cells with a measured `mult_det`
in `results/s36_ledger.md`, `results/s36_aone.md` and
`results/s54_cells_d*.jsonl`.  The brief counts 266; the ledgers may hold more
length-5 cells than s54's 56, and the reconciled count is reported, every row
checked to carry `mult_det = a`.

## 5. Predictions, with priors

| # | prediction | prior |
|---|---|---|
| P1 | The s39 `a` values at `δ = 10, ℓ = 6` reproduce by the Weyl route at all 1,874 cells, and the 60 sampled cells elsewhere reproduce. | 0.95 |
| P2 | **K2 is refuted as a closeness prior**: at least 90% of the dead six-row cells lie in the first quartile (percentile ≤ 0.25) of K2 in their slice — the criterion nominates exactly the cells known to be dead. | 0.85 |
| P3 | **K1 has no positive support in the region**: the one known live cell, `(65,17,2^7)_24`, lies in the *last* decile of K1 in its slice (`ℓ = 9`, `δ = 24`) — it is among the most skewed eligible weights there. | 0.85 |
| P4 | The dead cells are mostly in the skewed half of K1 (median percentile > 0.5), but K1's *first* nominee at `(δ, ℓ) = (7, 6)`, `(8,4,4,4,4,4)`, is dead (already on record), so K1 is refuted at `δ ≤ 7` and untested at `δ ≥ 8`, where its nominees are all above the reach frontier (`n_χ~ > 3·10^5`). | 0.8 |
| P5 | **Transport is already in the record**: at least 40% of the 210 six-row dead cells sit above another dead cell on their ladder with equal `a`, i.e. were dead by Lemma L before they were measured (they are confirmations, not information). | 0.6 |
| P6 | At `δ = 10, 11, 12` the number of eligible cells dead by transport from the record is at least 40 and includes every cell of every peaked ladder `(4δ−2(ℓ−1), 2^{ℓ−1})` whose `δ = 6` (`ℓ = 6`) or lowest banked member is dead. | 0.8 |
| P7 | **The LMR ladder** `a(4δ−31, 17, 2^7; δ)` is non-decreasing over `δ = 12..24` and `a(24) = 274` reproduces (two moduli). | 0.95 |
| P8 | `a` on the LMR ladder is *not yet stable at the top*: `a(23) < a(24) = 274`. If instead `a(23) = 274`, Lemma L (downward forcing) proves `I(D_9)_{23} ⊇ S_{(61,17,2^7)} ≠ 0` — an equation of degree 23, below every construction in s55's census; the report will say so with the label *proved, conditional on the two-route `a` values*, and will name the lowest degree the forcing reaches. | 0.5 |
| P9 | `h_pad` at the LMR cell is below `a`: `h_pad((65,17,2^7), 24) < 274`, so the pad ideal is forced non-zero there and `D > 0` at the LMR cell would need `i_det ≥ 275 − h_pad`. | 0.7 |
| P10 | `sk ≫ a` on every F1 cell with `sk` computed (`δ ≤ 16`): `sk/a ≥ 10` at each. | 0.9 |
| P11 | The peaked ladders (F2) have `a = 1` at every cell of the region and `sk` constant in `δ` (`sk = 8, 13, 18, 21, 21, 18` for `ℓ = 5, …, 10`, i.e. the constant margins 7 / 12 / 17 / 20 / 20 / 17 of s38/s39), so by Lemma L and the `δ ≤ 10` record every `ℓ = 6` peaked cell of the region is dead; the `ℓ = 7..10` peaked cells are dead by transport iff their lowest member is on record (it is not — no `ℓ ≥ 7` cell has ever been measured — so they are *unconstrained*, with `i_det ≤ 1`). | 0.9 |
| P12 | **K4 (frontier)** at `ℓ = 6`, `δ = 11, 12`: after removing cells dead by transport, fewer than 40 eligible cells with `a ≥ 1` remain inside the dense frontier `n_χ~ ≤ 20,000`, and every one of them has `a ≤ 3`. | 0.6 |
| P13 | **No criterion has positive support in the region except K3, and K3's support is one cell** whose mechanism is proved empty at `ℓ ≤ 8` (s55). The session's honest outcome is the brief's "acceptable" one — the table plus a prior whose only evidence-backed component is Lemma L pruning around the LMR ladder — unless P8 fails, in which case the LMR ladder itself becomes the nominee list. | 0.7 |

## 6. Stopping rules and bounds

- Every run: `timeout` (≤ 4 h per run) and `ulimit -v 6300000`; pid to
  `results/logs/s57_<run>.pid`; a run that must be ended early is ended by that
  id and its cells are marked `pending`, never estimated.
- The C engine is never asked for `N > 64` or `λ_1 + ℓ − 1 ≥ 64` (its packing
  limits); such cells are `pending` for `sk` and go to the Weyl route for `a`.
- `a` values are accepted only when two routes (or the engine's two moduli
  agreeing with the CRT bound checked) agree; a disagreement is reported as a
  disagreement, not resolved by choosing one.
- No value is written into `results/s57_selector.md` that is not in a banked
  per-chunk file with its route named.
- Nothing is pushed; delivery by bundle; single-writer files untouched.
