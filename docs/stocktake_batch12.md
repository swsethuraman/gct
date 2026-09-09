# Stock-take, batch 12

**2026-09-09, integrator.**  Twelve sessions: six worker sessions (s74–s79) and
six reasoning sessions (S1–S6, with an S3 continuation).  All twelve delivered.
Every worker bundle was verified here against an independent re-derivation
before it was merged; the counts are in the reviews and are quoted below.

## 1. The headline

**The bottleneck is gone, the determinant column is closed, and the statistic
does not see the permanent.**

Three sentences that were not true when batch 12 opened:

1. **A complete, certified 274-vector source exists at the LMR goal cell** (s74).
   Building it was the programme's bottleneck for four batches and S1 had
   recorded candidate discovery as unresolved.  Verified here: generic nullity 0,
   so the 274 transported births *are* a basis of `M₂₄`.
2. **`rank T_det(24) = 273` exactly, `i_det(24) = 1`** — proved, not sampled, on
   the transported δ=23 rows plus the birth-quotient proposition plus LMR.  No
   δ=24 candidate was needed on either side.
3. **`mult_pad = mult_red` wherever anyone has looked** — at `r = 5` (s64), at
   `r = 6` on 682 cells and as a theorem at degree 9 on the length-6 weights
   (s79), at `r = 9` degree 13 (integrator), and at `r = 9` degree 24 (s74).
   Three lengths, four instruments, no exception.

The third is the scientific result of the batch, and it is a negative.  In every
cell measured, `D = mult_pad − mult_det` equals `mult_red − mult_det`: the
padded permanent carries no equation the reducible locus `ℓ·c` does not already
carry, and at the goal cell the **unpadded** `per₄` carries none at all
(`i_per4 = 0`).  Whatever `D` is at these cells, it is a statement about
reducibility against the determinant.  The permanent has dropped out.

## 2. What each session delivered

### Worker sessions

| | mission | delivered | verified here |
|---|---|---|---|
| **s74** | the LMR source by births, then the decision | the complete 274-row source; `rank T_det = 273` exactly; `rank T_pad ≥ 269`; `U_R = U_P`; `i_per4 = 0`; the LMR line `y` identified and shown nonzero at 282/282 padded points | **47/47** then **54/54** |
| **s75** | the `δ = 12` compact control | the control, on the compact circuit | merged |
| **s76** | scale the recursion to `δ = 24` | `C₂₄ = 17 778` exactly (my estimate was 4.4 % low); `B₂₄ = 2 168` channel by channel; `K_{λ₂₄,(4²⁴)}` | merged, three independent derivations of `B₂₄` |
| **s77** | deterministic basis — the bridge | a bracket filling **is** an unlabelled Pieri chain; evaluable by construction | merged |
| **s78** | `r = 5` by bounded elimination | 149 → 98 variables; `W ⊆ D₅ ⇔ G` dominant; ker/coker image exactly 28 at all contact orders | merged |
| **s79** | the two frontiers | Part 1: the sixteen-block weight-13 stable theorem. Part 2: 682 six-row cells all empty on every side; 63 tails closed for every degree; the degree-9 cubic scan | Part 1 **60/60**; Part 2 **17/18** |

### Reasoning sessions

| | delivered |
|---|---|
| **S1** | **PROVED** `ker(M_d → R/(u)) = u·M_{d−1}`, so `M_d/uM_{d−1} ≅ ρ_d(M_d)` of dimension `b_d`.  This is the theorem the whole endgame rests on: it is what makes the `u`-transport exact, and what lets the δ=23 source close the determinant column without a δ=24 candidate. |
| **S2** | chart and jet certificates at `r = 5`, and the handoff that s77 consumed |
| **S3** | the spherical operator `I + (d−1)T = d·P_{H_d}|_{W_d}`, so `ker(T − I) = V^H` and the goal-cell spectrum is `1²⁷⁴ ⊕ (−1/23)¹⁸⁹⁴`.  Then the continuation: a complete **rational** 39-dimensional rung-13 source with certified conversion, generic and determinant rank 39 at both primes |
| **S4** | the padded factorization `M_λ →^S ⊕_μ M^{(3)}_μ →^Q ⊕_μ N_μ`, giving `rank T_pad = rank S − dim(S(M_λ) ∩ ker Q)` — the only exact route to `i_pad`.  Also caught my false claim that the 521-deficit is exactly the cubic-permanent kernels |
| **S5** | the one-block recursion, and the scope limit `2N + 1 ≤ m² + 1`: `n = 4` is the last `ℓ·per₃`-admissible rung and the family probes a quadratic scale only |
| **S6** | the isotypic/Adams audit; and, by rejecting a report over a board-numbering mismatch that did not exist, produced the `board_numbering` convention |

## 3. Negatives, and what each one costs the programme

- **The LMR cell as a permanent obstruction: settled against.**  Not because
  `D < 0` is proved — it is not — but because `U_R = U_P` and `i_per4 = 0` say
  the weight `(65,17,2⁷)` cannot distinguish `ℓ·per₃` from `ℓ·c`.  A cell that
  cannot see the permanent cannot separate it.
- **`D` at the goal cell is still open**, at `D = 1 − i_pad(23) ∈ [−4, +1]`.
  `D = −4` is measured at two primes, two point families and two evaluation
  paths and is not certified; `D = +1` is the only value evaluation alone can
  prove.
- **No six-row equation of any kind** in 682 cells through `δ = 12` at tail
  weights 13–23: no determinant, no permanent-specific, no `per₄`.
- **No weight-13 stable determinant equation with `a_∞ ≤ 4`** — sixteen blocks,
  and by Proposition S every cell of those sixteen ladders at every degree.
- **The family is quadratic-scale** (S5).  Even a positive result here would not
  reach Valiant-level separation; it would be a first working instance of a
  multiplicity obstruction.
- **The `r = 5` local geometry is settled** (s78): the ker/coker image is exactly
  28 at all contact orders, so nothing new comes from higher jets there.

## 4. How the picture changed

**Before batch 12** the programme was blocked on *construction*: 274 spanning
vectors at the goal cell, priced at 12–15 CPU-hours by s69 and declared
unresolved by S1.  Both columns were unknown.

**After batch 12** construction is finished, the determinant column is a
theorem, and the open question has moved twice:

    D = mult_pad - mult_det          (the programme's object)
      = 1 - i_pad(23)                (s74 + the birth quotient; eps_pad = 0 proved)
      = 1 - i_red(23)                (U_R = U_P at every rung measured)
      and  i_red < a  requires  I(D_9^{per_3})_delta != 0   (transfer lemma Prop. 8(2))

The last line is the change that matters.  **`mult_pad < mult_red` at length `r`
and degree `δ` requires the cubic-side ideal `I(D_r^{per₃})_δ` to be nonzero** —
a condition with no padded points in it, no orbit closure, and no degree-`δ`
quartic build.  And Prop. 8(1) is the converse: an empty cubic ideal gives
`mult_pad = mult_red` at **every** weight of that length and degree at once.

So the programme has a screen that is one computation per `(length, degree)`
instead of one per weight, and it is the *necessary* condition for everything
else.  s79 ran it at `r = 6`, `δ = 9` and found nothing — with the hole in §5.

## 5. The most critical new learnings

1. **The cubic ideal is the whole question.**  Scan `I(D_r^{per₃})_δ`, not
   quartic cells.  One scan per `(r, δ)` covers every weight.
2. **`u`-transport makes rank floors free and exact.**  Evaluation is a ring
   homomorphism, so a transported row is the native row with column `j` scaled
   by `u(P_j)^k`.  A rank floor transports **unconditionally** — no primality,
   no ideal — provided no sampled point is a `u`-zero, which must be *recorded*
   per point.  Primality of `I(X)` with `u ∉ I(X)` is what upgrades it to the
   exact `rank T_X|_{u^k M_{d−k}} = a_{d−k} − i_X(d−k)`.
3. **The cost asymmetry is now in force at the goal cell in its sharpest form.**
   A nonzero minor is a rank floor and can only push `i` down, so `D = +1` is the
   **only** value evaluation alone can prove.  Everything else needs a membership
   statement — which is why S4's factorization and the cubic screen matter more
   than more points.
4. **Prop. S closes ladders wholesale.**  A first stable cell (`a = a_∞`) with a
   full rank closes its tail at *every* degree.  s79 closed 63 tails with 69
   cells.  Any sweep should sort first-stable cells to the front.
5. **A frontier count must mean open on *both* instruments** — and the record
   itself must be current.  `wk9_s57_lib.negative_record()` reads the ledgers of
   sessions 36–54 and stops; five sessions of measurements are missing from it.
6. **The `exps` ordering trap bit for the third time**, this time in my own
   verifier, and it was hidden by a check that silently dropped the terms it
   could not place.  A check that can skip its own targets is not a check.
7. **Stored values must say what transform they are under.**  s74's
   `rows_native` are native values scaled at read time; I read them as the rows
   and got determinant rank 274, contradicting LMR.  A `values_are` field beside
   the numbers would have caught it at the first read.
8. **A transported certificate must ship its points and its `u`-values.**  S1's
   artefact verified only because its own control matrix happened to be in the
   package.

## 6. Defects found and fixed, both sides

| where | what | by |
|---|---|---|
| `tools/verify/layer3.py` | the size guard ran *after* the routine that materialises every monomial — 1.56·10¹¹ rows at the goal cell | s74 → fixed: `chi_build.weight_monomials_count`, a three-second tail DP, runs first |
| `analysis/wk12_int_w13_census.py` | counted "open" against one instrument | s79 → fixed: joins the quartic record, reports open on both |
| `analysis/wk9_s57_lib.py` | `negative_record()` stops at session 54 | integrator → flagged; extending it is a batch-13 task |
| `analysis/wk11_s71_cell.py` | ideal vectors as `nullspace(Gᵀ)` — combinations of *points* | s79 → fixed to `nullspace(G)` in the length-5 driver too |
| five `wk*_int_*` scripts | fixed output path with a variable argument, the bank-clobbering class | integrator |
| `docs/batch12_worker_preamble.md` | claimed the toolchain is installed; three containers had no `python-flint` | integrator → check-and-install |
| s79's degree-9 cubic scan | the claim is one quantifier too wide: 365 weights of length ≤ 5 with `a ≥ 1` were not run | integrator → §5 of `docs/s79_part2_review.md` |
| s74's report | `D = −4` entered the negative branch on a sampled nullity | integrator + reasoning side → withdrawn |

## 7. Where the open questions live now

| question | where it lives | cost |
|---|---|---|
| `I(D₆^{per₃})₉ = 0` as stated | 365 length-≤5 weights, `Σa = 1213` | smaller than the 210 already done |
| `I(D₆^{per₃})₁₀` | 106 unreached length-6 weights + all shorter | 69 below `N_S = 5·10⁶`, eleven above `10⁷` |
| `i_red(23)` at the goal cell | S4's factorization on s74's source | the only exact route |
| the three rung-13 reducible relations over `Q` | S3's rational rung-13 source | 39 dimensions |
| `I(D₉^{per₃})₁₃` | **fifteen** horizontal-13-strip predecessors of `λ₁₃`, `a` from 1 to 9, `N_S` from `1.6·10⁷` to `3.7·10⁸` | above s79's `1.5·10⁸` build wall — the row builder is the wall, not the kernel |
| a six-row determinant equation | the balanced cells, `n_χ ≥ 10⁶`, `N_S·δ ≥ 10⁸` | same wall |

Two of those six are blocked by the same thing: **the raising-row builder**.
That makes a leaner row builder the highest-leverage engineering task in the
programme, and it is why batch 13 opens with it.

Author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
board_numbering: batch12
