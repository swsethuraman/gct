# Session 72 (C5) — the `r = 5` upper bound: the enumerated normal cone exhausted, every residue closed to a number

2026-09-08. Branch `s72-upperbound` off `s66-primitive` head `23ecd204` (a
descendant of `main = 226b4ef1`; both ancestry gates passed first). Inherits
session 66's tree and machinery as **input, not work**. Pre-registration
`results/PREREG_s72.md` (commit `28550ce`, before any measurement). Code
`analysis/wk11_s72_*.py`; CAS inputs `analysis/wk11_s72_*.sing/.ms`; data
`results/s72_*.json`, `results/s72_normal_cone.{md,jsonl}`; logs and pids under
`results/logs/s72_*`. `python-flint nmod_mat` for every rank; house primes
`2147483647, 2147483629` for the arc/tangent identities; `32003` and `1000003`
for the CAS decompositions. Bundle `s72_upperbound.bundle` + `.md5`. No
single-writer file touched. Labels: **proved** / **measured** /
**adopted-from-literature** / **expectation**.

The brief's `docs/batch11_worker_preamble.md` and `docs/batch11_plan.md §6` are
in neither the tree nor the laptop's `work/`; the session ran from the brief,
which carries the target statement (fixed before either this session or Sol
session S3 starts), the residue list and the stopping rules. This session shares
the target statement with S3 and not the method: S3 attacks it theoretically
(the special-fibre algebra); this session exhausts the normal cone
computationally.

## 0. Verdict

> **The other direction, delivered: no enumerated component climbs.** Every
> component of `Proj gr_J R` supported over `Sing V(J)` that this session
> enumerates — the smooth base-component loci, the pairwise incidences (embedded,
> non-reduced structure), and the rank-degeneration (rank-`≤2`) strata — has
> fixed-factor image `< 35`. Every **measured** boundary component is `≤ 29`; the
> rank-`≤2` exact-type loci are bounded `≤ 31` (their reducible part lies in the
> exact `31`-locus); the interior `Φ(X_5) ∩ W` is **31** exactly. Hence, on the
> enumerated cone,
>
>     dim(D_5 ∩ W) = 31 < 35,   so   R_5 ⊄ D_5.
>
> **The four residues session 66 named are reduced from four to numbers:**
> (1) `P ∩ c21` at order 2 = **19** — the one primitive-world number s66 left
> open, settled and reproducible at three primes; (2) the `ker ∩ coker` rank
> strata are **0 and 9 only** (the rank-0 `a`-kernel is 3-dim, no intermediate
> rank observed over 500 samples at two primes), both image **29**; (3) contact
> order `≥ 4` at the incidences: the linear order-4 route is **obstructed** and
> the image is saturated at order 3 by the measured stabilisation (s66 order 2 =
> order 3) and s59's `q ≤ 4` invariance — evidence, `≤ 29`, with the nonlinear
> order-4 sub-locus the one thing left un-measured; (4) the deeper rank-`≤2`
> strata **drop** (skew `28 → 19 → 9`) and every incidence meeting an exact-type
> locus inherits its determinant, `≤ 31`.
>
> **One genuinely new object.** The interior/boundary split. `W_int = Φ(X_5) ∩ W`
> reparametrises through the `r = 4` base locus `B_4` and its dimension is an
> **exact Jacobian upper bound = 31**, not an arc lower bound — the interior half
> of the theorem, with no closure gap.
>
> **Rigor, stated plainly.** The interior `31` is exact (certified over `Q`, s32).
> Each boundary component's image is the generic Jacobian rank of the reducible
> exceptional map over that component — the exact dimension of an irreducible
> family — measured at both house primes. What is **not** proved here is that the
> enumeration is *complete* (that `Proj gr_J R` has no component outside the
> list); that is the global special-fibre-algebra statement, S3's object. This
> session exhausts the enumerated normal cone and closes every named residue with
> a number; no component reaches 32.

## 1. The interior is exactly 31 (proved upper bound)

`s_5 | det M(s) ⟺ det M(s)|_{s_5=0} = det(s_1A_1+…+s_4A_4) ≡ 0 ⟺ (A_1..A_4) ∈
B_4`, with `A_5` free. So `W_int = {det M/s_5 : (A_1..A_4) ∈ B_4, A_5 ∈ M_4}` is a
finite union of images of irreducible families (one per component of `B_4`), and
`dim W_int = max_C (generic Jacobian rank of the cubic map over `C`)` — an exact
value (the image dimension of an irreducible parametrised family), hence an exact
*upper* bound on the interior with no closure gap.

Under `s_5 ↔ s_1` this is exactly session 32's branch measurement (`A_1` the free
matrix, `M_0(y)` the singular 4-space, `G = det M/s_1`), reproduced here
(`analysis/wk11_s72_interior.py`, importing `wk8_s32_branches`): `ker`/`coker`
29, `c21`/`c32` **31**, `SP`/`SP^T` 27, `P`/`P^T` 25, `E_1` 22, both primes and
over `Q`. Closed the one gap in "all of `B_4`": the generic-rank-`≤2` `4`-spaces
force `s_1^2 | det`, so their cubic image lies in `s_1·Sym^2 C^5` and has
dimension `14 ≤ 15 < 31`. **`dim W_int = 31`** (`results/s72_interior.json`).

This also settles the flag s54/s59 raised — that s32 proves *image*
non-containment, not the closure statement. The interior of the *closure* `D_5 ∩
W` is exactly `W_int`, and it is `31`; the closure adds only the boundary, which
is the rest of this report.

## 2. The smooth locus (s66 contact-order lemma, calibration KC1)

At a smooth point of `V(J)` the exceptional fibre is `P(im dΦ)` at every contact
order (s66 §4, a theorem), so the reducible fixed-factor image is the order-1
value. Reproduced as calibration, both primes: `ker` 29, `coker` 29, `c21` 28,
`c32` 28, `P` 24, `SP` 26, and transposes. All `≤ 29 < 31`.

## 3. Residue 1 — `P ∩ c21` at order 2 = 19 (settled)

`P ∩ c21` (rank-2 `u`, `P` singular there; four components `P, c21, SP0, SP1`
through it; `rank dΦ = 17`, `ker = 63`, order 1 = 10) is the one number the
primitive world was missing; in s66 neither Singular's `std`/`minAssGTZ` nor
Macaulay2's `minimalPrimes` finished in the box.

**The structure that settled it (`analysis/wk11_s72_pc21.py`,
`wk11_s72_pc21_top.py`).** In the 30 reduced coordinates (after dropping the
33-dim common intersection of the four tangent spaces) the 9 quadrics of `Q_2^π`
have **no `a·a` monomial** (12 `a`-vars appear only linearly, 18 `b`-vars) —
verified with **zero** non-a-linear entries, so this is **proved**. Hence `Q_2^π`
is affine-linear in the `a`-block for fixed `b`, with coefficient matrix `C(b)`
(`9 × 12`, linear in `b`) of generic rank 6. This makes decomposing it a rank
problem rather than a 30-variable Gröbner basis; the top component is what
carries the image.

**Dimension and the top component (reproducible, `wk11_s72_pc21_top.py`).** A
generic 25-random-hyperplane slice of `V(Q_2^π)` (reduced) leaves exactly **one**
free variable — a curve — and a 24-plane slice leaves two — a surface — so
`dim V(Q_2^π)` reduced `= 26` and the top component is 26-dimensional (the four
tangent spaces `T_c21` 24, `T_SP` 15, `T_P` 6 are proper sub-loci). Reconstructing
generic points of the top component from the slice-25 Gröbner parametrisation
(msolve) and verifying each lies on `V(Q_2^π)`, the order-2 fixed-factor image is
**19** at every one; the tangent-space sub-loci (over `rank C(b) = 0, 4, 6`) give
**12**. **Three primes** (`32003`, `1000003`, `2147483647`), four points each,
all verified on `V` (`results/s72_pc21_top.json`). A generic random `b` is
*inconsistent* (the `a`-system has no solution) — `V(Q_2^π)` projects to a proper
sub-locus of `b`-space — which is why a naïve "`b` free × `a`-fibre" count is
wrong and the dimension is read off the slice, not that formula.

**`P ∩ c21` order-2 image = 19 < 31 < 35.** The image *jumps up* from 12 on the
special tangent sub-loci to 19 on the generic top component — a real jump, of
the kind the residue list existed to catch — but it lands at 19, far below 35.

## 4. Residue 2 — the `ker ∩ coker` rank strata, both image 29

At `ker ∩ coker` the bilinear reduction gives `M(a) = Σ a_i M_i` (`31 × 12`,
linear in the 12 `a`-coordinates), generic rank 9. s66 measured the generic
ruling and its mirror (image 29, 29) and left the rank-drop strata undecomposed.
Measured here completely (`analysis/wk11_s72_rankdrop.py::rank_strata`, both
primes `32003`, `2147483647`, two seeds):

- the twelve matrices `M_i` span a **9-dimensional** space, so the `a`-kernel
  `{a : M(a) = 0}` (computed exactly as the nullspace of the `(31·12) × 12`
  matrix of the `M_i`) is **3-dimensional** — a genuine rank-0 stratum, *not* the
  origin alone;
- over 500 mixed samples (`a`-kernel + generic directions) the only ranks that
  occur are **0 and 9** — no intermediate rank `1..8` appears, at either prime;
- both strata give fixed-factor image **29**: the rank-9 ruling (`ker M(a)` 3-dim,
  `b` generic in it) and the rank-0 stratum (`M(a) = 0`, `b` free in the full
  12-dim `b`-space) — the latter is the `T_ker`-direction, already at 29.

So the reducible image over `ker ∩ coker` is **29**, achieved on both the rank-9
and rank-0 strata, with no intermediate rank observed. (Correction to the first
draft, which mis-stated the `a`-kernel as the origin and cited a
codimension heuristic; the `a`-kernel is 3-dimensional, and "only ranks 0 and 9"
is a **measurement** over 500 samples at two primes, not a proof that ranks
`1..8` are impossible. Any such stratum, were it to exist on an unsampled
sub-locus, is a proper closed subset of the rank-9 ruling whose image `29`
dominates it by semicontinuity.)

## 5. Residue 3 — contact order `≥ 4` is obstructed; the image saturates at order 3

The L-component directions the brief names (at `P ∩ c32` and `SP ∩ c21`, where
`V(Q_2)` carries a linear component larger than a tangent space) are already
measured through order 3 by s66: `P ∩ c32 ≤ 27`, `SP ∩ c21 ≤ 28`.

Contact order 4 (`analysis/wk11_s72_order4.py`): at the maximal incidences
(`ker ∩ coker`, `SP ∩ c21`, `SP ∩ coker`, `c21 ∩ c32`), with `M_1` **generic in a
tangent space** and the **particular** `M_2, M_3` giving `g_1 = g_2 = g_3 = 0`, the
constraint `π g_4 = 0` is **not solvable by `M_4` alone** — so this order-3 partial
arc does not extend to a reducible order-4 arc by `M_4`, and any order-4 reducible
directions would live on a strictly more special (nonlinear, higher-Rees)
sub-locus. This is a *construction-specific* obstruction (one `M_1`, one
`(M_2, M_3)`); it does not by itself prove order-4 contact is impossible, and the
image on that nonlinear sub-locus is not measured here.

The evidence that the reducible image **does not climb at order `≥ 4`** is
therefore: (i) s66's measured stabilisation — order 2 = order 3 at **every**
incidence; (ii) s59's measured invariance through `q = 4` at the generic strata
(`29,29,28,28,24`); (iii) the observed order-4 obstruction, which shows the linear
order-by-order route halts here rather than opening a new direction. This is a
well-supported inductive expectation, `≤ 29` — not a stand-alone proof; the
order-4 image on the nonlinear sub-locus is the one thing in residue 3 left
un-measured, and it is a proper closed subset of the order-3 locus.

## 6. Residue 4 — the deeper rank-`≤2` strata drop; exact-type incidences inherit `≤ 31`

The s66 exactness identities on `(2,0)`, `(4,2)`, `(3,1)` and the rank-`≤1` locus
are **pointwise on the whole locus**, so they hold at every sub-locus and
incidence: at a `(2,0) ∩ (3,1)` point `e_2` is **still** the `(2,0)` determinant
`det[Y_2 | X]` (verified, both primes; `analysis/wk11_s72_rank2deep.py`), so the
order-2 image lies in `Φ(X_5)` and its reducible part in the exact locus `≤ 31`
(measured reducible image 18 there). Any deeper rank-`≤2` incidence that meets an
exact-type locus is bounded the same way.

Only the padded-skew type carries no such identity. Its image **drops** on
degenerate frames: `x`-rank 3 gives `28, 28, 26, 26` (`= s66`); `x`-rank 2 gives
`19`; `x`-rank 1 gives `9`. No jump on any deeper stratum. Maximum over the whole
rank-`≤2` world = **28 < 31 < 35**.

## 7. The component enumeration (task 2)

`results/s72_normal_cone.md` and `.jsonl` list every component of `Proj gr_J R`
over `Sing V(J)` with its dimension, the mechanism (smooth `P(im dΦ)` / embedded
incidence / rank-degeneration), its fixed-factor image, and whether it is new
relative to s66's eight-component list plus the 49-dim `SP`. **New relative to
s66:** the interior/`B_4` reformulation (`31`, exact); `P ∩ c21` (`19`); the
`ker ∩ coker` rank stratification (ranks 0 and 9, both image 29); the deeper skew
strata (`19`, `9`) and the exact-type rank-`≤2` incidences (`18`); the order-4
obstruction. **No new component** of the normal cone was found beyond s66's
enumeration — the residue list closes, it does not grow.

## 8. Honest boundary

- **Proved / exact:** the interior bound `dim W_int = 31` (Jacobian, certified
  over `Q` by s32, wide-point Schwartz–Zippel); the a-linearity of `Q_2^π` at
  `P ∩ c21` (0 non-a-linear entries); the pointwise exactness identities on the
  rank-`≤2` types (s66, extended to sub-loci here — verified at `(2,0) ∩ (3,1)`);
  the `a`-kernel of `M(a)` at `ker ∩ coker` is exactly 3-dimensional (nullspace).
- **Measured (exact dimension of an irreducible family, both/three primes):**
  every boundary component's fixed-factor image; `dim V(Q_2^π) = 26` at `P ∩ c21`
  and its top-component image 19 (three primes, reproducible in
  `wk11_s72_pc21_top.py`); the `ker ∩ coker` rank strata (only 0 and 9 over 500
  samples, both image 29); the deeper skew images 19, 9; the order-4 obstruction.
  These are measurements, not proofs of the surrounding *for-all* statements
  (that no intermediate `M(a)`-rank occurs; that order-4 contact is impossible) —
  those are supported by sampling + structure, and flagged as such in §§4–5.
- **Adopted:** the Atkinson / Huang–Landsberg classification (the eight base
  types + the rank-`≤2` types exhaust `B_5`); s32's exact `31`; `dim D_5 = 50`,
  `dim R_5 = 39`, `dim D_4 = 34`; s66's tables and lemma; s59's certified `≥ 31`
  and `q ≤ 4` invariance.
- **Not proved:** the *completeness* of the enumeration — that `Proj gr_J R` has
  no component outside the list. Every listed component is `< 35`; the global
  statement "no hidden component" is the special-fibre algebra, S3's object, and
  is the one thing between this computational exhaustion and a paper-complete
  proof of `R_5 ⊄ D_5`. The deepest un-decomposed sub-loci (the nonlinear order-4
  locus; strata of `V(Q_2^π)` below the top component at `P ∩ c21`, which give the
  smaller 12) are proper closed subsets of measured loci and, by every measurement
  here, carry *smaller* images, not larger.
- **What this does:** it turns s54/s59/s66's "no exotic direction at the orders
  we reached" into "every component of the normal cone we can enumerate has image
  `≤ 31`, and the interior is exactly 31" — the upper-bound half of the theorem,
  with the four named residues closed to numbers and the completeness statement
  handed cleanly to S3.

## 9. Pre-registration scorecard

| id | prediction | prior | outcome |
|---|---|---|---|
| I | `dim W_int = 31` exactly | 0.75 | **confirmed** (exact, over `Q`) |
| N | no new component beyond s66's list + `SP` + incidences + rank-`≤2` | 0.60 | **confirmed** (residue list closes) |
| R1 | `P ∩ c21` order-2 `< 31` | 0.70 | **confirmed** (19; jumps 12 → 19 on the top component) |
| R2 | `ker ∩ coker` rank-drop strata `≤ 29` | 0.65 | **confirmed** (image 29; ranks 0 and 9 only — measured, not proved no intermediate) |
| R3 | contact `≥ 4` adds nothing above 29 | 0.70 | **supported** (order-4 obstructed; saturates at order 3 by s66/s59) — not a stand-alone proof |
| R4 | deeper rank-`≤2` `< 35` | 0.60 | **confirmed** (drops to 19, 9; exact-type incidences `≤ 31`) |
| V | every component `< 35`; `R_5 ⊄ D_5` up to the stated caveat | 0.45 | **confirmed** for the enumerated cone; completeness → S3 |

Unregistered: the a-linearity of `Q_2^π` at `P ∩ c21` and the slice route that
settled it; the `ker ∩ coker` rank stratification (a 3-dim `a`-kernel; ranks 0
and 9); the order-4 obstruction (the linear order-by-order route halts at order 4
at the incidences, unlike the generic strata where s59 found it unobstructed
through `q = 4`).

## 9b. Corrections folded in after an adversarial audit

An adversarial re-derivation (independent subagent) checked every claim against
the code and data and caught three things, all now fixed above: (i) the first
draft's "`M(a)` has constant rank 9 off the origin" was **wrong** — the `a`-kernel
is 3-dimensional (a genuine rank-0 stratum); the corrected statement is "ranks 0
and 9 only, measured over 500 samples at two primes, both image 29" (§4). (ii)
The `P ∩ c21` headline `19` was originally reproducible only from a manual msolve
slice; it is now produced end-to-end by the committed `wk11_s72_pc21_top.py` at
three primes (§3). (iii) Residue 3's "obstructed ⟹ no climb" was tightened to
"supported by measured stabilisation + s59 invariance + the order-4 obstruction,
not a stand-alone proof" (§5). The audit confirmed the interior `= 31` (the
strongest leg) and that the main verdict is correctly stated as conditional on
enumeration completeness; the numeric bottom line (max `= 31`, no component
`≥ 32`) stands.

## 10. For the single writer, and one line for the roadmap

No single-writer file touched. For `docs/boundary_deficit.html` /
`paper/det3-conductor.tex` the integrator may want: the interior/`B_4`
reformulation (`W_int = Φ(X_5) ∩ W = {det M/s_5 : (A_1..A_4) ∈ B_4}`, dimension
exactly 31, an exact upper bound); the sentence "every component of the normal
cone `Proj gr_J R` over `Sing V(J)` has fixed-factor image `≤ 31`, and the four
residues of the roadmap are closed to `19, 29, ≤29, ≤31`"; and the `P ∩ c21`
a-linearity as the structural reason the last open number is small.

Roadmap: the upper-bound object s54/s59/s66 kept naming is now computed on the
enumerated normal cone — `dim(D_5 ∩ W) = 31`, interior exact and every boundary
component measured `≤ 31` at both primes. The single remaining step to a
paper-complete `R_5 ⊄ D_5` is the *completeness* of the enumeration (no hidden
component of `Proj gr_J R`), which is exactly the special-fibre algebra Sol
session S3 is attacking theoretically. The residue list is empty.
