# Where we stand after sessions 49–55

Integrator. Every load-bearing claim below re-derived independently before writing.

## 1. The batch in one paragraph

Six sessions ran; five closed a route and one (s49) hardened the foundations.
**Nothing found an obstruction, and that is now a structural statement rather
than a run of bad luck.** The determinant ideal is empty at **210** measured
cells across `δ = 6..10` — `i_det = 0` at every one, without exception, since
session 36. The one known equation lives at a length the programme provably
cannot reach with the statistic it uses. Every cheap statistic tried either
points the wrong way or is vacuous in range. The gap is not compute.

## 2. The organising fact the batch established

There are exactly **two families** of statistic, and they run in **opposite
directions**:

| family | at `det_4` | at `ℓ·per_3` | separates |
|---|---|---|---|
| excess-singularity (Milnor corank, Macaulay drop, Λ⁵ Fitting) | *less* degenerate | *more* degenerate | **wrong way** |
| dual-degeneracy (Hessian rank, LMR divisibility) | *more* degenerate | *less* degenerate | **right way** |

Three independent confirmations of the first row: Proposition D (s48), s51 §4b
(`det_4` 980 vs `ℓ·per_3` 2141 at `r=10, d=7`), and my own re-derivation at
`d = 5` with independent code — **generic 0, `det_4` 0, `ℓ·c` 36,
`x_0·per_3` 86.** At `d = 5` the determinant is *indistinguishable from
generic* while the padded permanent is already deeply degenerate. That is a
sharper statement than s51's and it makes the direction failure structural, not
marginal.

s55 §3 is right that `docs/excess_singularity.md` overstates Proposition D by
extending it to "Hessian-rank conditions": those are the *second* row and run
the other way. Narrow it to functionals monotone in `dim(S/J_F)_d`.

**Consequence.** Any future proposal must be classified into a row *before* any
work. Row one is closed by three independent instances. This is the
degeneracy-direction pre-check earning its place — it killed s51's §4b, which
was the batch's most-hyped item, at the gate rather than after the work.

## 3. The LMR route is now completely mapped, and it is out of range

s55 proves **24 is the exact floor** of the dual-degeneracy family at `n = 4`, by
two conditions rather than one — containment forces `k ≥ min(6, r−2)`;
non-vacuity forces `k ≤ r−3` since `ℓ(λ(k,4)) = k+3`. I reproduced the table:

| `r` | admissible `k` | lowest degree |
|---|---|---|
| 4–8 | **none** | **the LMR module gives no equation at all** |
| 9 | 6 | 24 |
| 10+ | 6 | 24 |

So at `r = 5, 6` — the entire measured region — **LMR contributes nothing**.
The best known degrees there remain 300 and 661. The standing "24 vs `δ ≤ 9`"
table was comparing different cells; s55 is right to retire it and re-scope by
`r` rather than `δ`.

Two sessions corroborate across a boundary: **s55 predicted, before s50 ran,
that s50's control-4 remainder must be nonzero** (`rank Hess(ℓ·per_3) = 9` on
`{per_3=0}`). s50 found it nonzero. Independent agreement on the batch's one
positive result.

## 4. Correction to s50 that must be applied at merge

s50 §2 states `a(λ,24)` is "not computed" and infers the multiplicity question
is "~20 orders of magnitude past the frontier" from the ambient dimensions
`dim S_λ(C^16) ≈ 10^30` and `dim Sym^24(Sym^4 C^16) ≈ 10^62`.

**That inference is invalid, and the number is small.** Plethysm multiplicities
do not depend on the variable count once `N ≥ ℓ(λ)`; here `ℓ(λ) = 9`, so this is
a **nine-variable** computation, not sixteen. I computed it:

    a((65,17,2^7), 24) = 274

in two minutes, confirmed under two independent moduli, with the same code
reproducing LMR's stated `n = 3` value of 6. The external reviewer obtained 274
independently by a different method (Weyl alternant). s50's own text contains
the refutation — it notes the `n = 3` analogue is 6, also inside a huge ambient.

This does **not** revive the cell (see §5), but §2 as written is wrong and would
mislead any future session. Fix at merge.

## 5. The `a = 1` prior is dead, and s52 killed my own recommendation correctly

I endorsed the `a = 1` selector two days ago. s52 refutes it, and the argument
is right:

> `D = i_det − i_pad`, and `i_det = 0` at **all 210** measured cells, so
> `U_D = {0}` at every one. A zero subspace has no orientation: `U_D ⊆ U_P`
> holds trivially and `D ≤ 0` is *forced*, not measured. The failure mode the
> `a = 1` prior protects against — `dim U_D = dim U_P` with `U_D ≠ U_P` — is
> **not instantiable anywhere the programme has measured.**

The protection is void until `i_det ≥ 1` is first observed; the cost (giving up
the strictly stronger of the two obstruction notions) is paid immediately.

And the headline experiment died. **`(30,2^5)` at `δ = 10` — the cell the
external reviewer and I both named as the single best next test — was measured
by s52: `mult_det = mult_pad = mult_red = 1 = a`, so `i_det = 0`, `D = 0`.**
Twelve more `δ = 10` `a = 1` cells with it, all dead. My `h_pad ≥ 1` gate was
correct but not sufficient: it excludes cells that *cannot* fire, not cells that
*do not*.

s52's successor test is the right one and I endorse it: **`U_D ⊆ U_P`**, which
refutes containment whenever it fails, is strictly stronger than `D > 0`, is
available at every `a`, and costs nothing beyond what a measured cell already
exhibits. It needs one cell with `i_det ≥ 1` to become usable.

## 6. s51 and s54: routes closed cleanly, with two structural gains

**s51.** The `Λ⁵` module is **proved** (dimension-polynomial argument plus the
centre-weight at `r = 5`; the "5" is `codim(Σ_{n−2}) + 1 = 4+1`, hence
`n`-independent — a genuinely satisfying identification that settles s48's open
A2/A3). The `r = 5` syzygy is exhibited and ℤ-verified. Then §4b — the step I
added and called the batch's highest-value item — **halted at the gate I
insisted on**. That is the process working: the expensive half was never run
because the cheap check said it could not separate.

**s54.** `R_5 ⊆ D_5` leans **no**, not settled. Two structural gains beyond the
verdict:

- **The order-1 exceptional image *fills* `D_5`** (dim 50 of 50). First
  determinant polars do not isolate the boundary — a concrete vindication of the
  Rees reframing, and proof that s53's higher-order analysis is *mandatory*, not
  a refinement. Even at `r = 5`, where the whole gap is four dimensions, order 1
  could not close it.
- **Reducible quartics are singular points of `D_5`** (Zariski tangent `≥ 64 >
  50`). New, and it explains why the exact-reducible pencils are rank-deficient.

## 7. Corrections to apply, several of them mine

1. **`brief_wording` §6 vs §5.** All seven briefs cite §6 for the
   degeneracy-direction pre-check; it is **§5** (§6 is citations, §7 is
   functoriality). Nine occurrences, my error. s50 and s51 both propagated it.
2. **`s53_prompt` §6:** `dim D_10 ≤ 128` should be **`≤ 129`** — the
   31-dimensional group acts with a 1-dimensional kernel, so `dim D_r ≤ 16r−30`.
   My error.
3. **`docs/washout_lemma.md` Thm 3(3) and `docs/transfer_lemma.md` Thm 3 item 4**
   assert closure non-containment `R_5 ⊄ D_5` citing s32 Theorem 5 — but s32
   proves non-containment in the **image** `Φ(X_5)`, not the closure. The
   conclusion is probably safe; the citation is wrong. Record the distinction.
4. **`docs/excess_singularity.md`** — narrow Proposition D per §2 above.
5. **s50 §2** — per §4 above.
6. **s49's `9 ≤ onset`** — already struck in my s49 merge; the bracket is
   `≤ 661` certified, `≤ 1148` proved, with no earned lower bound.
7. Three `results/s36_cells/*.txt` blobs (12–13 MB) still over the limit — on
   the post-batch rewrite list.

## 8. What is actually still live

Ranked by whether a mechanism reaching the statistic exists:

1. **The onset.** `i_det ≥ 1` has never been observed at any cell, at any
   length, at any degree. *Everything* depends on it: the `a = 1` prior, the
   `U_D ⊆ U_P` test, and the orientation question are all dormant until it
   happens once. The certified bracket is `≤ 661`; the measured range is
   `δ ≤ 10`. **This gap is the programme.**
2. **s53's higher-order Rees computation.** s54 proved order 1 is insufficient
   and the machinery is tractable at `r = 5`. But note §3: s53's original
   motivation is gone (`ℓ·per_3 ∉ D_10` is known), so it is now a boundary-
   description session, not a separation session. Re-brief before launching.
3. **`R_5 ⊆ D_5`** — leaning no, needs either the higher-order dimension or a
   length-5 equation at degree `> 9`. Same object as (2).
4. **The 274-dimensional LMR multiplicity space.** Now known small. But `a`
   small does not make `i_det`/`i_pad` cheap — the wall is `N_S`, the
   weight-monomial count, which nobody has sized. Size `N_S` before committing.

## 9. The honest summary

The programme set out to find a representation-theoretic obstruction separating
`per_3` from `det_4`. After 55 sessions:

- the separation itself is **known** (LMR, re-derived cheaply by s50);
- the multiplicity statistic has **never once** seen a nonzero determinant ideal
  across 210 cells;
- the only equation that exists at `n = 4` sits at a length where our sweeps have
  never reached and, at lengths where they have, **provably does not exist**;
- and every cheap statistic that could bridge the gap has now been shown to
  point the wrong way.

That is not a failure of execution — the execution has been unusually clean, and
five of six sessions closed their question. It is the shape of the problem
becoming visible. The next decision is strategic, not computational: whether to
push on the onset in the measurable region, or to accept that the statistic is
the wrong instrument at `n = 4` and change instruments.
