# Pre-registration — Session 54: is `R_5 ⊆ D_5^{det_4}`?

Branch `s54-r5d5`, off `origin/main` tip `eb8cecb` (fresh public clone,
container only; not the owner of the laptop folder, deliver by bundle only).
Committed **before** any measurement. Labels used in the report:
**proved** / **measured** / **adopted-from-literature** / **expectation**.

## 0. The question and the objects

`D_5 := D_5^{det_4} = closure{ det_4(s_1 A_1 + ... + s_5 A_5) : A_i ∈ M_4(C) }
⊆ Sym^4 C^5` (dim 50, washout Cor. 7). `R_5 = {ℓ·c : ℓ ∈ Sym^1 C^5,
c ∈ Sym^3 C^5}` the reducible quinary quartics (dim 39, washout Cor. 7).

> **Is `R_5 ⊆ D_5`?**  A **closure** question: does `ℓ·c` lie in the closure
> of the det_4 pencils, not (settled negatively by s32 Thm 5) in the image.

Two success directions, both good (brief §7):
- `R_5 ⊆ D_5`: upgrades the `ℓ ≤ 5` exclusion from measured to proved.
- `R_5 ⊄ D_5` **with the equation extracted**: an equation of the
  determinantal locus at `r = 5`, inside the measurable range `δ ≤ 9`.

## 1. The reduction that makes it decidable (proved input)

At `r = 5`, washout Theorem 3(1) gives `mult_pad = mult_red := mult_λ C[R_5]`
(since `P_5 = R_5`, washout Thm 2). Functoriality (brief_wording §7):

    R_5 ⊆ D_5  ⟹  I(D_5) ⊆ I(R_5)  ⟹  C[D_5] ↠ C[R_5]
               ⟹  mult_red(λ,δ) ≤ mult_det(λ,δ)  for every (λ,δ),

where `mult_det := mult_λ C[D_5^{det_4}]`. Contrapositive and its scope:

- **T1 (refutation, decidable).** If some length-5 `(λ,δ)` has
  `mult_red(λ,δ) > mult_det(λ,δ)`, then `R_5 ⊄ D_5`, and
  `dim I(D_5)_{λ,δ} > dim I(R_5)_{λ,δ}` exhibits an equation of `D_5` (a
  weight-`λ` covariant of degree `δ`) not vanishing on `R_5`. Since `r ≤ 5`,
  `mult_red = mult_pad`, so such a cell is a genuine `D = mult_pad − mult_det
  > 0` obstruction with **no transfer gap** — it goes through the
  verification protocol before being written as a claim.
- **T2 (only length 5 matters, proved).** For `ℓ(λ) ≤ 4` a length-`k`
  highest-weight vector sees only the `k`-plane restriction (restriction
  lemma), which lies in `D_4^{det_4} ⊇ R_4` (exact block construction,
  s27/s32 §6). So `mult_red ≤ mult_det` automatically at `ℓ(λ) ≤ 4`; the
  test is at length **exactly** 5.
- **T3 (one-sided).** `mult_red ≤ mult_det` at every measured cell is
  *necessary* for containment, **not** sufficient (l5_containment §4: equal
  multiplicities can hide different ideals). The positive direction needs a
  construction (Route A) or the exceptional-image argument (Route B).

## 2. What will be measured, and the stopping/positive rules

### 2A. The multiplicity comparison (primary)
For every length-5 `(λ,δ)`, `δ ∈ {6,7,8,9}`, `a(λ,δ) > 0`, with weight-space
size within budget:
- `a` two ways: plethysm `a_of` (wk8_s30_pleth) **and** raising-operator
  kernel `nb − rank_p(R)` (wk8_s30_core), asserted equal at both primes.
- `mult_det`: evaluation of the weight-`λ` HWV at random `det_4(M(s))` points
  (`det_form(4)`, `N=16`, `r=5`).
- `mult_red`: evaluation at random **reducible** points `ℓ(s)·c(s)`
  (`ℓ` random linear, `c` random quinary cubic) — direct; cross-checked at a
  sample of cells against evaluation at `x_0·per_3` points (`per_padded(3,4)`,
  `N=10`), which equals `mult_red` at `r=5` by washout.
- Two house primes `2147483647, 2147483629`. `rank(R)=nb−a` self-check every
  cell. `mult = a` (rank attains `a`) is a **certificate** (`mult ≤ a` always;
  rank is a rigorous lower bound). A reading `mult < a` at both primes is
  believed only after the re-run discipline; any `mult_red > mult_det` cell is
  re-derived (fresh seeds, both primes, and the equation lifted to an integer
  covariant) before it is called an obstruction.

**Outcome rule.** `mult_red(λ,δ) > mult_det(λ,δ)` at any length-5 cell ⇒
report `R_5 ⊄ D_5`, extract the equation (degree `δ`, weight `λ`), test it
against the degeneracy-direction set §2D, hand to the s49 verifier. Otherwise
record `mult_red ≤ mult_det` over the measured range (necessary condition holds)
and turn to Routes A/B for the positive direction.

### 2B. Route A — border det_3 (cheap, done first)
Establish whether a general quinary cubic is a **border** `3×3` determinant,
i.e. whether `Sym^3 C^5 = closure Φ_3(M_3^5) = D_5^{det_3}`.
- **Prediction (prior 0.9): NO.** `D_5^{det_3}` is a *closed* variety of
  dimension 29 < 35 (washout Cor. 7; s28), so its points are already the
  border-determinantal cubics and a general cubic is not one. Hence the
  block/border route `diag(ℓ, border-N)` cannot reach a general `ℓ·c`, and the
  exact 4×4 route caps at dim-31 cubics (s32 Thm 5). No cheap affirmative.
- If, contrary to prediction, the border cubic locus were dense, Route A would
  close the question affirmatively; this is checked (a dimension/Jacobian
  recomputation) before Route B.

### 2C. Route B — viability of the exceptional-image (base-locus) route
Monte-Carlo viability experiment at `r = 5` (brief §9 / s53 §10), **before** any
Rees/elimination algebra:
- For each bounded-rank-3 base stratum `E ⊆ M_4` available at `dim E ≤ 5`
  (the four compression types, dims 12/10/10/12 as spaces; and the primitive
  family `C^4 ⊂ Hom(C^4, Λ^2 C^4)` composed to `M_4`, dim 4 — s32 Thm 4,
  verified against Atkinson/Huang–Landsberg): choose a generic 5-variable pencil
  `M_0(s)` with image in `E` (`det M_0 ≡ 0`), take random jets
  `M(t,s) = M_0 + tM_1 + ... + t^k M_k`, impose exact cancellation through
  `t^{q−1}`, collect the first non-zero quartic `f(s)` (the `t^q` coefficient),
  and estimate the **tangent dimension** of the family of such `[f]` for
  `k,q ∈ {1..4}`.
- **Reducibility screen** on each leading quartic `f`: does it factor as
  (linear)·(cubic)? (Most normal forms will not factor at all.) The set of
  `ℓ·c` that appear, and the dimension the exceptional image reaches against
  `dim D_5 = 50` and `dim R_5 = 39`, is the evidence.

Predictions: (B1, prior 0.5) the exceptional image over at least one stratum
contains reducibles `ℓ·c`; (B2, prior 0.4) the reducibles reached fill a family
of dimension **< 39** (so `R_5` is not covered by the tested strata → leans
`R_5 ⊄ D_5` or "resists in one stratum"); (B3, prior 0.35) the primitive-family
stratum is the one carrying reducibles, by analogy with Hüttenhain–Lairez at
`n=3`.

### 2D. Degeneracy-direction pre-check (brief_wording §6, mandatory)
The multiplicity comparison of §2A is functorial in the right direction
(coordinate-ring multiplicities; brief_wording §7 row 1) and needs no
separate pre-check. For **any** scalar statistic introduced to separate `D_5`
from `R_5` (e.g. a candidate low-degree equation from a negative outcome, or a
Route-B separating invariant), evaluate it at the committed three-point set
before trusting it:
1. a `det_4` pencil (a point of `D_5`);
2. a reducible `ℓ·c`, `c` generic (a point of `R_5`);
3. the full ten-variable `ℓ·per_3` restricted to five variables.
A statistic at least as degenerate at (3) as at (1) separates the wrong way and
is discarded. A negative-outcome equation is additionally evaluated exactly at
all three (brief §6).

## 3. Named falsifiers / kill criteria
- **KC1 (calibration).** Reproduce a known length-5 cell: the nine `δ=6`
  length-5 cells of s27 all had `mult_pad = mult_det` (`D=0`). Since
  `mult_pad = mult_red` at `r=5`, my `mult_red` and `mult_det` must agree with
  `D=0` at those nine. If they do not, the harness is wrong and no result is
  reported until it is fixed.
- **KC2 (self-check).** `rank_p(R) = nb − a` must hold at both primes for every
  cell; a mismatch halts that cell.
- **KC3 (prime agreement).** `mult` must agree across both primes; disagreement
  triggers a third prime and re-derivation.
- **KC4 (equation reality).** A `mult_red > mult_det` cell is not a claim until
  the separating covariant is lifted to an explicit integer highest-weight
  vector, verified to vanish on `D_5` points and not on `R_5` points exactly.

## 4. Prediction ledger (priors set now)
| id | prediction | prior |
|---|---|---|
| A | general quinary cubic is NOT a border 3×3 determinant (`dim D_5^{det_3}=29<35`) | 0.90 |
| M1 | no length-5 cell with `mult_red > mult_det` at `δ ≤ 9` (necessary condition for containment holds) | 0.65 |
| M2 | at every measured length-5 cell `mult_red = mult_det = a` (both ideals empty in range) | 0.55 |
| M3 | if any bite, det side bites no earlier than reducible side (`mult_det ≤ mult_red` fails ⇒ negative) | 0.30 for a negative |
| B1 | exceptional image over some stratum contains reducibles `ℓ·c` | 0.50 |
| B2 | reducibles reached fill dim < 39 (R_5 not covered by tested strata) | 0.40 |
| V | net verdict is `R_5 ⊆ D_5` (positive) rather than refuted | 0.55 |

## 5. Infrastructure
`python-flint` for every rank (no hand-rolled elimination). Every long run
bounded by `timeout` and `ulimit -v`, pid to `results/logs/<run>.pid`, ended
only by recorded pid, never by name pattern. Bank per cell as JSONL
(`results/s54_cells.jsonl`) with a commit at each milestone (container is
scratch). Logs under `results/logs/`. No committed file over 5 MB. Deliver by
git bundle; do not push. Commit messages carry a `Co-Authored-By` trailer only
(no session-link trailer or URL, per brief §0).
