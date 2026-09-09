# Batch 13 — the plan (SUPERSEDED)

> **Superseded by `docs/batch13_board.md`.**  This draft's central premise was
> wrong: it treated the cubic screen `I(D_r^{per₃})_δ` as the necessary condition
> for a positive obstruction.  It is the necessary condition for
> `mult_pad < mult_red` — permanent-specific equations — and those are a
> *different* question from `D = mult_pad − mult_det > 0`.  See
> `docs/batch13_corrections.md`.  Kept for provenance; do not run from it.

**Basis:** `docs/stocktake_batch12.md`.  Twelve sessions: eight worker (s80–s87)
and four reasoning (S7–S10).  Board numbering: **batch13**; every report and
manifest carries a `board_numbering` field.

## 0. The one question

Batch 12 measured `mult_pad = mult_red` at three lengths on four instruments and
found no exception, and the transfer lemma says why that is the whole question:

> **Prop. 8(2).**  `mult_pad < mult_red` at length `r`, degree `δ` **requires**
> `I(D_r^{per₃})_δ ≠ 0`.
> **Prop. 8(1).**  `I(D_r^{per₃})_δ = 0` gives `mult_pad = mult_red` at **every**
> weight of that length and degree.

So the batch has one question, asked once per `(r, δ)` instead of once per weight:

> **Is `I(D_r^{per₃})_δ` ever nonzero in reach?**

If it is, that weight is the first place the permanent becomes visible in this
model and Prop. 8(2) names the quartic cells to measure next.  **If it is not,
in the range the programme can reach, then the multiplicity obstruction cannot
separate the permanent there — and that is the result, to be written as one.**
Either outcome is a batch worth running; neither needs a padded point.

Two consequences for how the batch is ordered.  The cubic scan comes **before**
any quartic cell, because it is the necessary condition and it is cheaper per
weight covered.  And the batch opens with an engineering session, because two of
the six open questions are blocked by the same wall.

## 1. The board

| | mission | why now |
|---|---|---|
| **s80** | a leaner raising-row builder; then extend `negative_record()` to sessions 55–79 | the build wall (`N_S·δ ≈ 1.5·10⁸` in 7 GB, the **rows** not the kernel) blocks both the `r = 9` cubic side and the balanced six-row cells |
| **s81** | close `I(D₆^{per₃})₉` — the 365 length-≤5 weights — then `δ = 10` completely | the degree-9 theorem is one quantifier too wide until this runs; it is the cheapest unfinished statement in the programme |
| **s82** | `I(D₇^{per₃})_δ` and `I(D₈^{per₃})_δ`, by degree, as far as cost allows | two lengths nobody has looked at, and the screen covers every weight at once |
| **s83** | `I(D₉^{per₃})₁₃` in full (fifteen weights); `I(D₉^{per₃})₂₃` priced and as far as it fits | rung 13 is where the goal cell's three reducible relations live; rung 23 is the rung that decides `D` |
| **s84** | `i_pad(23)` **exactly**, by S4's factorization on s74's 274-row source | the only route that can prove any value of `D` other than `+1` |
| **s85** | the three rung-13 reducible relations over `Q`, on S3's rational rung-13 source | one certified element of `I(V_red) ∩ M₁₃` settles the LMR cell against, with no sampling anywhere |
| **s86** | the balanced six-row cells (s57's T4, `n_χ ≥ 10⁶`), on s80's builder | the only place a six-row determinant equation of degree ≤ 12 can still hide |
| **s87** | the `n = 3` positive control: the §5 three-point test at the one cell where `D > 0` | the programme's only positive is unpadded; if `mult_pad = mult_red` there too, the padded comparison is degenerate even where the statistic works |
| **S7** | is `mult_pad = mult_red` a **theorem** for this family? | four instruments agree at three lengths; a reason would end the scanning |
| **S8** | the ideal of `V_red = {ℓ·c}` in a given isotypic piece, and a computable membership test | s85 needs it, and it is a classical object with no permanent in it |
| **S9** | sharpen Prop. 8 — which quartic weights does one cubic-side element actually reach? | decides whether a single nonzero `μ` is worth a quartic campaign |
| **S10** | given the negative, which family *could* see the permanent, and at what cost? | S5 fixed this one at quadratic scale; if the answer is "none in reach", say so |

## 2. The worker sessions

### s80 — the row builder, and the record

**Task 1.**  `wk9_s45_build.build_cell`'s raising rows are the wall: s79 killed
`(10,6,6,6,2,2)₈` at `N_S·δ = 1.47·10⁸` with the rows exceeding 4 GB, while its
*kernels* were never the constraint (the largest hybrid phase was 202 s at
`n_χ = 732 815`).  Build the rows in blocks, streaming to disk or to a sparse
accumulator, with a stated peak-memory model.  **Acceptance:** entry-for-entry
agreement with the existing builder on at least fifteen banked cells spanning
`n_χ` from `10³` to `10⁶` and both `n = 3` and `n = 4`, plus a measured
`N_S·δ` ceiling and its memory curve.  Report the new ceiling as a number; every
later session prices against it.

**Task 2.**  `wk9_s57_lib.negative_record()` reads the ledgers of sessions 36–54
and stops.  Add 55–79.  **Acceptance:** the count rises from 326; no ledger
disagreement raised; `wk12_int_w13_census.py` re-run shows the corrected
open-on-both-instruments frontier at every `a_∞` level.

**Falsifier.**  Any disagreement with the existing builder on a banked cell:
stop and report, and no later session runs on the new builder.

### s81 — close the degree-9 cubic theorem at `r = 6`

The 365 partitions of 27 of length ≤ 5 with `a(μ,9) ≥ 1`, `Σa = 1213` — by
length: 1, 11, 48, 117, 188 — on `analysis/wk12_s79_per6.py` unchanged, both
primes, in `N_S` order.  A weight of length `k < 6` sees only `Sym³Cᵏ`, so its
`N_S` is *smaller* than the length-6 weights already done; s79 spent 5 884 s on
the 210 and this should cost the same order.  Then degree 10: the 106 unreached
length-6 weights and every shorter one.

**Prediction (0.7):** all empty, and `I(D₆^{per₃})₉ = 0` becomes a theorem as
stated, with `mult_pad = mult_red` at every six-row weight of degree 9 following
from Prop. 8(1).  **(0.3):** a nonzero weight — then §4's protocol.

**Falsifier.**  Any `δ ≤ 8` re-run disagreeing with s37/s41/s43/s47.

### s82 — `r = 7` and `r = 8` on the cubic side

The same instrument, length-general, at `r = 7` and `r = 8`, by degree from the
bottom, both primes, in `N_S` order, until the wall.  Report the boundary as a
degree with its `N_S·δ`.  Include **every** length ≤ `r`, not only length
exactly `r` — that is what s79's degree-9 scan missed and it is the falsifier
here.

**Prediction (0.6):** empty through `δ = 8` at both lengths.

### s83 — the cubic side at `r = 9`

`I(D₉^{per₃})₁₃` is **fifteen** weights: the horizontal-13-strip predecessors of
`λ₁₃ = (21,17,2⁷)`, priced here — `a` from 1 to 9, `N_S` from `1.59·10⁷` at
`(21,6,2⁷)` to `3.70·10⁸` at `(19,6,2⁷,2)`.  Run them in `N_S` order on s80's
builder.  Then price `I(D₉^{per₃})₂₃` (the horizontal-23-strip predecessors of
`λ₂₃ = (61,17,2⁷)`) **before** attempting any of it, and run what fits.

**Why it matters.**  I measured three reducible relations at rung 13 of the LMR
ladder (`docs/rung13_reducible.md`).  Prop. 8(2) says a permanent-specific
relation there needs a nonzero `I(D₉^{per₃})₁₃`.  Fifteen weights decide it.

**Prediction (0.6):** `I(D₉^{per₃})₁₃ = 0`, which by Prop. 8(1) makes
`mult_pad = mult_red` at rung 13 a theorem and turns my measurement into one.

### s84 — `i_pad(23)` exactly

S4's factorization: `M_λ →^S ⊕_μ M^{(3)}_μ →^Q ⊕_μ N_μ`, so
`rank T_pad = rank S − dim(S(M_λ) ∩ ker Q)`.  Feed it s74's 274-row source
(`results/s74/source.json`), which is the input it has never had.

1. **`rank S`** on the `274 × 521` reducible-normalisation split — an exact rank
   of a structural matrix, not a sampled evaluation.  `rank S < 274` gives
   `mult_pad ≤ mult_red < 274`, so `i_pad ≥ 1` and `D ≤ 0`, **with no padded
   points at all**.  This is the cheapest possible settlement and it was
   pre-registered in `docs/batch11_plan.md` C3 for want of a source.
2. If `rank S = 274`: `dim(S(M_λ) ∩ ker Q)` exactly, over `Q`.  That is `i_pad`,
   and `D = 1 − i_pad` decides the cell.

Do the same at rung 23 on the 273 transported rows, which is where
`D = 1 − i_pad(23)` actually lives.

**Falsifier.**  `rank S > 274` or `< mult_pad`; any disagreement with s74's
certified floor `rank T_pad ≥ 269`.

### s85 — the rung-13 relations over `Q`

I measured, on my own points and my own evaluator, that s74's three padded
kernel directions at rung 13 vanish at every reducible point and span the same
three-space as the reducible kernel, with a 39/39 generic control.  That is a
sampled ceiling.  The question is whether **one** of them is a genuine element
of `I(V_red) ∩ M₁₃` over `Q`.

Instrument: S3's rung-13 source is **rational** by a specified convention, not
reconstructed from residues — the only place in the programme where rung 13
exists over `Q`.  Write the three candidates in that basis, then decide
membership by S8's test (or, failing that, by the pullback along
`(C⁹)* × S³ → S⁴`, which is a linear map between finite-dimensional spaces).

**One certified element gives `i_red(13) ≥ 1`, hence `i_pad(13) ≥ 1`, hence
`i_pad(23) ≥ 1` by monotonicity, hence `D ≤ 0` at the goal cell** — with no
sampling anywhere in the chain.

### s86 — the balanced six-row cells

s57 named them and s79 confirmed they are where a six-row determinant equation
of degree ≤ 12 can still hide: `n_χ ≥ 10⁶`, `N_S·δ ≥ 10⁸`, priced out of reach
until s80.  Run them in `N_S·δ` order on the new builder, four families, both
primes, first-stable cells sorted to the front (a full rank at `a = a_∞` closes
its tail at every degree by Prop. S, and s79 closed 63 tails with 69 cells).

### s87 — the positive control, and the three-point test where it works

The programme's only `D > 0` is at `n = 3`, `λ = (19,7,2⁵)`, `δ = 12`, `r = 7`,
**unpadded**: `mult_det = 5`, `mult_per = 6`.  Nobody has run the padded
comparison there.  Run `docs/brief_wording.md` §5's committed three-point test at
that cell and at its neighbours: `det₃` pencils, reducible `ℓ·c`, and the true
padded form.

**Why it is worth a session.**  If `mult_pad = mult_red` even at the cell where
the unpadded statistic separates, then the padded comparison is degenerate
wherever it has been tried, and the negative of §0 is not a property of the LMR
cell but of the padding.  If instead `mult_pad < mult_red` there, that is the
first permanent-specific equation in the record and it is at `a = 6`.

## 3. The reasoning sessions

**S7 — is `mult_pad = mult_red` a theorem here?**  Four instruments, three
lengths, every weight measured.  Either exhibit the structural reason
(a containment, a degeneration, an equality of the two ideals in this range) or
exhibit a cell where they must differ.  A theorem ends the scanning; a
counterexample redirects it.  The obvious route is through
`I(D_r^{per₃})_δ = 0`: prove *that* in a range, and Prop. 8(1) does the rest.

**S8 — the ideal of `V_red`.**  `V_red = {ℓ·c}` is the image of
`(C⁹)* × S³(C⁹)* → S⁴(C⁹)*`.  Give its `λ`-isotypic pieces in the degrees the
programme needs, and a **computable membership test** for a given
highest-weight vector: `F ∈ I(V_red)` iff `F` is in the kernel of the pullback,
a linear map between finite-dimensional spaces.  s85 consumes this directly.

**S9 — sharpen Prop. 8.**  Prop. 8(2) pairs a quartic `λ` with a cubic `μ` such
that `λ/μ` is a horizontal `δ`-strip.  Is the pairing tight — does a single
nonzero `μ` actually produce a drop at some `λ`, or only permit one?  Which `λ`?
The answer decides whether a nonzero cubic weight is worth a quartic campaign or
is a false start.  Note that `μ` may be **shorter** than `λ` (it interlaces, so
`μ_r` may be 0), which is exactly the quantifier s79's degree-9 scan missed.

**S10 — scope.**  S5 fixed this family at quadratic scale: `2N + 1 ≤ m² + 1`, so
`n = 4` is the last `ℓ·per₃`-admissible rung.  Given batch 12's negative, is
there a family — larger `r`, a different padding, a different pair of orbits —
where the multiplicity statistic can see the permanent at all?  What would one
cell of it cost on the instruments the programme now has?  An honest "none in
reach" is an acceptable and useful answer.

## 4. Protocols, unchanged and in force

- **Any `D > 0`, or any nonzero `I(D_r^{per₃})_δ`:** halt the sweep; the
  verification protocol takes over before anything is reported anywhere —
  second prime on every rank, two independent point families, characteristic
  zero where a kernel is claimed, an independent source, and the degeneracy
  pre-check of `docs/brief_wording.md` §5.
- **A sampled nullity is a ceiling.**  A nonzero minor is a rank floor and
  proves `i ≤ a − k`.  Nothing proves `i ≥ 1` except a membership statement.
  No report enters a negative decision-table branch on a sampled kernel.
- **Pre-registration before computation**, in `results/PREREG_s<n>.md`, committed
  before the first measurement, with dated addenda.
- **Delivery by bundle only.**  Split bundles are numbered from `part00` and the
  report states how many parts there are; the `.md5` names the bare filename,
  never a path.  (Batch 12 lost a part twice.)
- **Transported certificates ship their points and their `u`-values**, and record
  `u(P_j) ≠ 0` at each one.
- **Stored value matrices carry a `values_are` field** naming any transform, next
  to the numbers.
- **`board_numbering`** in every report and manifest.
- Runs bounded with `timeout` and `ulimit -v`, pid to `results/logs/<run>.pid`,
  ended only by that recorded id.  No file over 5 MB.  Repository config
  append-only.  `python-flint` **checked and installed**, not assumed.
- Commit trailer: the model that actually ran the session, no session-link
  trailer.

## 5. What this batch does not fund

- More padded points at the goal cell.  They can only prove `D = +1`, s74 has
  already run two families and a box-1000 replay, and the exact routes (s84,
  s85) subsume them.
- Rebuilding any part of the 274-row source.  It exists, it is certified, and
  its generic nullity is 0.
- An `a_∞ = 5` stable census before s80's Task 2 has corrected the
  open-on-both-instruments count.
- Any quartic sweep at a new length before the cubic screen at that length has
  run.  That is the batch's central discipline and it is what §0 buys.

Author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
board_numbering: batch13
