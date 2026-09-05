# Session 53 — Border degenerations of `det_4`: the finite first layer

A different category of argument from the rest of the batch.  This session does
not compute a multiplicity and does not use the `GCT` statistic.  It addresses
`ℓ·per_3 ∉ D_10` directly, through the base locus of a border degeneration.

## 0. Standing constraints

- Deliver by git bundle only.  Do not push.
- Do not edit `paper/det3-conductor.tex`, `paper/det4-onset.tex`,
  `PROJECT_NOTES.md`, or `docs/boundary_deficit.html`.  Those have a single
  writer.  If you believe one is wrong, say so in your report.
- Commit messages carry a `Co-Authored-By` trailer only.  No session-link
  trailer, in commits or in any script that commits.  No session-link URL in
  any file you write.
- Bound every run with `timeout` and `ulimit -v`.  Record the process id to
  `results/logs/<run>.pid` and end a run only by that recorded id.  Do not
  select processes by name pattern.
- No committed file over 5 MB.  Logs under `results/logs/`.  Config is
  append-only.
- Pre-registration first: state what will be measured and what would count as a
  positive result before running it.  Bank the result per cell.
- `python-flint` only for exact linear algebra.
- Any cell reporting `D > 0` goes through the verification protocol before it is
  written down as a claim.
- Before developing any statistic meant to characterise determinant type, run
  the degeneracy-direction pre-check in `docs/brief_wording.md` §6.

## 1. What changed since the first draft of this brief

The earlier version proposed classifying first determinant polars over the
compression strata and hoping higher-order contact behaved.  That was the wrong
object: an arc need not have its first nonzero normalised coefficient at order
one, and there is no bound on the order.

The replacement is the **blow-up of the determinant coefficient ideal**, which
captures every order at once.  This session is the `n = 4` analogue of
Hüttenhain–Lairez, *The boundary of the orbit of the 3 by 3 determinant
polynomial* (arXiv:1512.02437), who carried out exactly this computation at
`n = 3` — resolving the indeterminacy of the coefficient map by a blow-up, using
the classification of maximal singular matrix spaces, and reading the boundary
off the exceptional divisors.  They found the boundary has **two irreducible
components**.  Read that paper first.  It is the method, the calibration, and
the warning about scale: their ambient is dimension 80 and it took a paper with
computer assistance; ours is dimension 159.

## 2. Setup

Let `X_r = Hom(C^r, M_4)` and

    Φ : X_r → Sym^4(C^r)^*,   M ↦ det M(s),

with coefficient functions `F_1, ..., F_N`, `N = C(r+3, 4)`; at `r = 10`,
`N = 715`.  The base locus `B_r = V(F_1, ..., F_N) = {M : det M(s) ≡ 0}` consists
exactly of the `M` whose image is a space of singular `4×4` matrices, that is of
bounded rank `3`.  With `J = (F_1, ..., F_N)`,

    Proj R(J) = Bl_J(P X_r)

is the closure of the graph of `P X_r ⇢ P(Sym^4 C^r)^*`, and its image on the
quartic side is `D_r`.

**Why this settles the order question.**  Given any arc
`M(t) = M_0 + t M_1 + t^2 M_2 + ...` with `det M_0(s) ≡ 0` and
`det M(t,s) = t^q f(s) + O(t^{q+1})` for any `q`, the arc lifts uniquely to the
blow-up by properness, its limit lies over `M_0`, and its image is `[f]`.  The
exceptional fibre therefore carries every order-`q` degeneration simultaneously.
No separate treatment of `q = 1, 2, 3, ...` is needed.

## 3. Phase 1 — statements only, no computation

Write these out correctly before any algebra.

1. **The classification of bounded-rank-3 spaces.**  Two independent routes; use
   both and depend on neither alone.  (a) Atkinson–Lloyd 1980, whose equality
   case at `dim E = nr − r + 1 = 10` is reported to give the four families
   directly — verify this against the paper, it is asserted in our
   correspondence and unverified here.  (b) The full classification: Atkinson
   1983 for `r = 3`, with Huang–Landsberg (*On linear spaces of matrices of
   bounded rank*, Selecta Math.) confirming *there are no non-classical examples
   of spaces of bounded rank when `r ≤ 3`*, the only primitive family being
   `E = C^a ⊂ Hom(E, Λ^2 E)`, `e ↦ (v ↦ e ∧ v)`, of bounded rank `a − 1`.  Route
   (b) has a gap that must be closed: "not primitive" does not immediately give
   "contained in a single compression space".

2. **The case list, which is not four.**  The four compression types below are
   the list for **injective** `M_0` only.  A non-injective `M_0` has
   `dim E ≤ 9`, and there the primitive family (dimension 4 at bounded rank 3)
   and its projections are available.  **Do not skip this branch.**
   Hüttenhain–Lairez's case list at `n = 3` is three compression spaces *and the
   skew-symmetric matrices* — which are exactly the primitive example at `a = 3`
   — and one of their two boundary components comes from that piece.  At the one
   value of `n` where this computation has been done, the primitive family
   carried half the answer.

   For injective `M_0`, indexed by `(k,i)` with `(4 − k) + i = 3`:

   | `(k,i)` | `dim` |
   |---|---|
   | `(1,0)` common kernel vector | 12 |
   | `(2,1)` | 10 |
   | `(3,2)` | 10 |
   | `(4,3)` common image hyperplane | 12 |

   so `dim E = 10` means the two ten-dimensional types, or a ten-dimensional
   subspace of one of the twelve-dimensional ones.

3. **The blow-up formulation and the arc lifting**, as in §2, following
   Hüttenhain–Lairez §2–3.

4. **Why the exceptional image is the whole remaining question.**  This is the
   step that makes the session bear on anything, and it must be stated:
   (i) `ℓ·per_3 ∈ Φ(X_10)` is excluded, since an exact representation gives on
   `ℓ = 1` an affine `4×4` determinantal representation of `per_3`, so
   `dc(per_3) ≤ 4 < 7` against Alper–Bogart–Velasco;
   (ii) so if `ℓ·per_3 ∈ D_10` it is in the closure and not the image;
   (iii) by curve selection over `C` it is then a limit along an arc;
   (iv) hence it lies in the exceptional image.

   Note also that ABV's bound is for **exact** representations and their
   Remark 1.9 shows `dc` is not upper semicontinuous — `xy^2 + yt^2 + z^3` has
   `dc > 3` and degenerates to `z^3` with `dc = 3` — so nothing about
   `dc(per_3) = 7` survives to the border by general principle.  The question is
   genuinely open.

## 4. Phase 2 — the four charts

Derive each explicitly and symbolically, then regenerate independently and
compare.  The integrator has checked all four; they are recorded here so that a
disagreement is visible rather than silent.

**Common left kernel.**  `M = (A ; w)` with `A` a `3×4` matrix of linear forms
and `w` the last row; the compression space is `w = 0`.  Exactly,

    det M = Σ_{j=1..4} (−1)^{4+j} w_j det A_ĵ,

so the determinant is **linear** in the normal directions.  Common right kernel
is the transpose.

**The `(2,1)` type.**  Write `M` in block columns of widths 1 and 3, with
`x_1, x_2, z_3, z_4 ∈ V^*` in the first and `y_1, y_2, w_3, w_4 ∈ (V^*)^3` in the
second; the compression locus is `w_3 = w_4 = 0`.  Laplace along the first
column gives exactly

    det M = x_1 det(y_2,w_3,w_4) − x_2 det(y_1,w_3,w_4)
          + z_3 det(y_1,y_2,w_4) − z_4 det(y_1,y_2,w_3),

so `det M = P_1 + P_2` with `P_1` linear and `P_2` quadratic in the normal block,
and no cubic or quartic terms.  Equivalently
`P_1 = (y_1 × y_2) · (z_3 w_4 − z_4 w_3)`.  The `(1,2)` type is the transpose.

Normal degrees across the four charts: **1, 2, 2, 1**.

**Do not conclude anything from that.**  Normal degree `≤ 2` does not bound
contact order: the tangential blocks move too, and cancellation can persist to
any order.  The blow-up is what handles this; the normal degrees are a hint that
the algebra may be small, nothing more.

## 5. Phase 3 — pull back the coefficient ideal

For each chart compute the pulled-back ideal `J_C` of the coefficients of
`det M(s)`, and then enough of the Rees algebra `R(J_C)` — or of the special
fibre algebra `F(J_C) = R(J_C) ⊗_R R/m_C` — to describe the projective
exceptional fibre.

**State which object you computed.**  The special fibre at a *generic* point of
the stratum is not the exceptional image over the stratum, and `ℓ·per_3` may
arise only over special `M_0`.  Hüttenhain–Lairez had to establish smoothness of
the blow-up centre precisely to control this.  If you compute the generic
object, say explicitly what remains open.

## 6. Phase 4 — dimension before membership

`dim X_10 = 160`.  The subgroup preserving `det M(s)`, `M ↦ P M Q` with
`det P · det Q = 1`, has dimension 31, so the generic fibre of `Φ` is at least
`31`-dimensional and `dim D_10 ≤ 128` inside `P^714`.  The exceptional image is a
proper closed subset of `D_10`, hence of dimension `≤ 127`.

Measure the exceptional image's dimension against that baseline before testing
membership.  If a component already fills most of `D_10`, this route buys
nothing and the stopping rule in §8 applies.

What the exceptional image *is*, stated plainly: the boundary `∂D_10`.  This
session is the `n = 4` analogue of Hüttenhain–Lairez and should be read as such.

## 7. Phase 5 — membership, only at the end

Only once the exceptional image is defined correctly, ask whether `[ℓ·per_3]`
lies in it up to `GL_10`.  Filters first, and they are filters and not proofs:
singular-locus dimension and degree, the module of partial derivatives, apolar
Hilbert function, Hessian and polar data, Betti table, stabiliser.  Explicit
elimination last.

Screen on **reducibility** before any of these — `ℓ·per_3` is a linear form times
a cubic, most normal forms will not factor at all, and this is the cheapest
discriminant available.

## 8. The stopping rule, which is hard

If, after pulling the coefficient ideal back to the charts, the Rees or special
fibre description is computationally intractable **and** no invariant survives
from it into coefficient space, park the whole direct-border track and say so.
Do not spend sessions cataloguing normal forms.  The bounded-rank classification
earns its place only if it makes the graph boundary tractable.

## 9. Run session 54 first

Session 54 asks `R_5 ⊆ D_5` by the same machinery at `r = 5`, where the quartic
side is `P^69` rather than `P^714` — `dim Sym^4 C^5 = 70` against 715.  It is the
pilot for this session: if the special-fibre computation is intractable at 70
coefficients it is certainly intractable at 715, and the stopping rule above
fires a session earlier and far more cheaply.  If it is tractable, this session
inherits working code and a validated formulation.

Before any algebra, run the viability experiment at both `r = 5` and `r = 10`:
choose a generic `M_0` in each stratum, take random jets
`M(t) = M_0 + tM_1 + ... + t^k M_k`, impose exact cancellation through `t^{q−1}`,
collect the first nonzero quartics, and estimate the tangent dimension of their
image, for `k, q` from 1 to about 4.  This is not evidence of non-membership; it
is a branch viability test.  If the dimensions rapidly approach the expected
dimension of `D_r`, the compression stratification is buying little.

## 10. Success and failure

**Success:** Phase 1 written correctly, including the non-injective branch and
the ABV link, and the viability experiment run.

**Best outcome:** an exceptional image with real codimension in `D_10`, and a
filter that `ℓ·per_3` fails.

**Acceptable outcome:** the stopping rule firing, documented.  Parking the track
on a clear computation is a result.

**Failure mode to avoid:** treating the four compression types as the case list
and skipping non-injective `M_0`, which is where the analogue of
Hüttenhain–Lairez's second component would live.

## 11. Report

`docs/s53_report.md`.  Deliver as a bundle.
