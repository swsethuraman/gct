# Pre-registration — Session 72 (C5): the `r = 5` upper bound — exhaust the normal cone

Branch `s72-upperbound`, off `s66-primitive` head
`23ecd204ee578887bfbc62d058c28866812e479b` (a descendant of `main` tip
`226b4ef1`; ancestry gate `git merge-base --is-ancestor 226b4ef1 HEAD` and
`... 23ecd204 HEAD` both passed before anything else). Fresh public clone,
container only; delivered by single-ref bundle `s72_upperbound.bundle` + `.md5`,
not pushed. Committed **before any measurement**. Labels used in the report:
**proved** / **measured** / **adopted-from-literature** / **expectation**.

This session inherits session 66's tree and machinery (`analysis/wk10_s66_*.py`,
`results/s66_*.json`, `docs/s66_report.md`) as **input, not work**. It shares its
theoretical statement — but not its method — with Sol session S3. The brief's
`docs/batch11_worker_preamble.md` and `docs/batch11_plan.md §6` were named as
required reading; neither the batch-11 nor the batch-10 preamble/plan exists in
the tree at `226b4ef1` nor on the laptop's `work/docs` or `gct-rewrite/docs`.
The session runs from the brief, which carries the target statement (fixed
before either S3 or this session starts), the residue list and the stopping
rules. The recoverable standing rules (bound every CAS run and record its pid,
bank every cell with a commit, nothing over 5 MB, `python-flint nmod_mat` for
every rank, two house primes, prime agreement on every reported number) are
applied as written.

## 0. The target statement, verbatim (shared with S3, fixed before either starts)

> Let `R` be the coordinate ring of the `r = 5` model and `J` the ideal of the
> base scheme of `Φ`. For every irreducible component `E` of the exceptional
> divisor `Proj gr_J R` of the blow-up of `Spec R` along `J` that is supported
> over `Sing V(J)` — including components supported over proper subloci of an
> irreducible singular component, over the incidence and rank-degeneration
> strata, and components arising from the embedded, non-reduced structure of the
> base scheme — the fixed-factor image of `E` has dimension `< 35`. Together with
> session 66's contact-order lemma, which disposes of every component supported
> over the smooth locus of `V(J)` (there the exceptional fibre is `P(im dΦ)` at
> every order), this exhausts `Proj gr_J R` and yields `R₅ ⊄ D₅`.

The quantifier is over the normal cone, not over `Sing V(J)`. Session 66 §5
measured `in(J) ⊊ in(I₁ ∩ I₂)` at a generic point of every pairwise incidence
(`dim Q₂ = 12 < 16` at `P ∩ SP`, `41 < 69` at `P ∩ coker`, `25 < 49` at
`c21 ∩ c32`, `59 < 144` at `ker ∩ coker`): the base scheme is generically
reduced along every component and non-reduced along every pairwise incidence.
So the normal cone of `J` differs from the normal cone of the reduced base
locus, the exceptional fibre over an incidence is larger than `P(im dΦ)`, and a
component of `E` can sit over a proper sublocus or over embedded structure and be
invisible at the generic point of any component of `Sing V(J)`.

## 1. The decomposition of the proof (the object committed before measurement)

`D_5 = closure Φ(X_5)`, `Φ(M) = det M(s)`, `X_5 = Hom(C^5, M_4)` (dim 80),
`D_5 ⊆ Sym^4 C^5` of dim 50; `W = {s_5·c}` (dim 35). `R_5 ⊆ D_5 ⟺ dim(D_5∩W) =
35`; `≥ 31` is certified over `Q` (s59). An upper bound `< 35` is the theorem.

The proof decomposes as **the smooth locus + four residues**:

- **Smooth locus (disposed of by s66 §4, the contact-order lemma).** At a smooth
  point of `V(J)` the exceptional fibre is `P(im dΦ)` at every contact order, so
  its reducible fixed-factor part is the order-1 image, `≤ 29 < 31 < 35` over
  every component (s54/s59/s66 tables: `ker 29, coker 29, c21 28, c32 28, prim
  24, SP 26`). This is a **theorem** (s66), reproduced here as calibration.

- **Residue 1.** `P ∩ c21` at order 2 — `P` singular there; the reduced `Q₂` is
  18 quadrics in 30 variables, `Q₂^π` is 9 quadrics; neither finished in Singular
  (25 min) nor in Macaulay2's `minimalPrimes` (15 min) in s66; order 1 there is
  10; the locus is 33-dimensional. The one number of the primitive world not on
  s66's table.

- **Residue 2.** the rank-drop strata of `M(a)` at `ker ∩ coker` (`α = β = 12`);
  s66 measured only the two generic-kernel components (29, 29).

- **Residue 3.** contact order `≥ 4` at the incidences, and order `≥ 3` with `M₁`
  outside the tangent spaces where `V(Q₂)` has an extra linear component
  (`P ∩ c32`, `SP ∩ c21`).

- **Residue 4.** deeper strata of the rank-`≤ 2` world — incidences of the four
  rank-2 types (the compressions `(2,0)`, `(3,1)`, `(4,2)`, and the padded `3×3`
  skew type) with each other.

By the contact-order lemma none of the four can be a smooth point of `V(J)`, and
each is a proper closed subset of a locus already measured by s66. Closing this
finite list is the finite obligation this session discharges.

## 2. The interior/boundary split, and the `B_4` reformulation (a new upper-bound ingredient)

`D_5 ∩ W` is the union of an **interior** part and a **boundary** part:

- **Interior `W_int` = `Φ(X_5) ∩ W`** — actual determinants divisible by `s_5`.
  `s_5 | det M(s) ⟺ det M(s)|_{s_5=0} = det(s_1A_1+…+s_4A_4) ≡ 0 ⟺
  (A_1,…,A_4) ∈ B_4`, the base locus of `Φ_4 : Hom(C^4, M_4) → Sym^4 C^4`; `A_5`
  is free. So `W_int = {det M(s)/s_5 : (A_1..A_4) ∈ B_4, A_5 ∈ M_4}` is a
  **finite union of images of irreducible parametrised families** (one per
  component of `B_4`), and `dim W_int = max_C (Jacobian rank of the parametrisation
  at a generic point of component `C` of `B_4`)` — an **exact** value and hence an
  exact *upper* bound on the interior, by a rank computation with no closure gap
  (the image dimension of an irreducible parametrised family is its generic
  Jacobian rank). This is not an arc computation; it is a direct interior bound
  the programme has not run, and it is genuinely an upper bound.

- **Boundary `∂D_5 ∩ W`** — limits, covered by the reducible exceptional images
  of the arcs of s66 over the components of `B_5` (`Sing V(J)`). This is the
  residue list of §1.

`dim(D_5 ∩ W) = max(dim W_int, dim(∂D_5 ∩ W))`. The theorem is that both are
`< 35`.

## 3. What will be computed

All ranks by `python-flint nmod_mat`; house primes `2147483647, 2147483629`;
CAS decompositions at `32003` and `1000003`; Jacobians by dual numbers exactly
as s59/s66; ≥ 2 seeds per point; every V-point verified (`g_1..g_{q-1} ≡ 0`,
`π g_q = 0`) before it is used; every spanning vector of every tangent space
checked to annihilate `dΦ`.

### 3A. The interior bound (§2)
Enumerate the components of `B_4` (the `r = 4` base locus) by the Atkinson /
Huang–Landsberg classification (the same eight types, one length down), build
each as a parametrised family, and compute the Jacobian rank of
`(A_1..A_4 ∈ C, A_5) ↦ [det M(s)/s_5] ∈ Sym^3 C^5` (35 coords) at a generic
point of each. Report `dim W_int` as the max, both primes, two seeds; calibrate
against s32's exact `31` and s59's certified interior.

### 3B. The normal-cone component enumeration (task 2)
For each component and each singular stratum of `V(J)`, the local normal cone —
`gr_J R` restricted to the stratum — via s66's second-order quadrics `Q_2`,
`Q_2^π` and the bilinear reduction, extended to the strata s66 left open. Say
which components of `Proj gr_J R` over `Sing V(J)` are new relative to s66's
eight-component list plus the 49-dimensional `SP` component. Deliver the list
with per-component fixed-factor bounds.

### 3C. The four residues
- **R1 (`P ∩ c21`):** the 9-quadric `Q_2^π` and the 18-quadric `Q_2` in 30
  variables, given a real budget in Singular (`slimgb`/`std` with block and
  weight orderings), msolve, and Macaulay2; each component sampled and its
  fixed-factor image run by s59's identity at orders 2 and 3.
- **R2 (`ker ∩ coker` rank-drop):** the rank stratification of the `12×12`
  bilinear matrix `M(a)` and the fixed-factor image over each rank-drop stratum.
- **R3 (contact ≥ 4):** arcs of contact order 4 at every incidence, and order 3
  with `M_1` in the extra linear component of `V(Q_2)` at `P ∩ c32`, `SP ∩ c21`.
- **R4 (deeper rank-2):** the incidences of the four rank-`≤ 2` types with each
  other, built and measured with `wk10_s66_rank2.py`.

## 4. Predictions, with priors

| id | prediction | prior |
|---|---|---|
| I | `dim W_int = 31` exactly (the interior is the exact s32 locus; an exact upper bound, no boundary jump) | 0.75 |
| N | the components of `Proj gr_J R` over `Sing V(J)` are the incidence-supported and rank-degeneration-supported components already enumerated by s66 (8 base components + `SP` + their pairwise incidences + the rank-`≤2` loci), with **no new component** beyond the residue list | 0.60 |
| R1 | `P ∩ c21` order-2 fixed-factor image `< 31` (`≤ 29`, in line with every other primitive-world incidence) once `Q_2^π` is decomposed | 0.70 |
| R2 | every rank-drop stratum of `M(a)` at `ker ∩ coker` has fixed-factor image `≤ 29` (`= rank dΦ`-controlled; `ker∩coker` order 1 is 29) | 0.65 |
| R3 | contact order `≥ 4` and order `≥ 3` off the tangent spaces add no reducible image above 29 (s59 invariance through `q=4` at generic strata; s66 through `q=3` at incidences) | 0.70 |
| R4 | the deeper rank-`≤2` incidences have fixed-factor image `< 35` (`≤ 31`; the rank-2 order-2 leading forms are honest `4×4` determinants, s66 §7, so their reducible part lies in the exact `≤31` locus) | 0.60 |
| V | every component `< 35`; the theorem holds and `R_5 ⊄ D_5` is **proved** subject to the honestly-stated CAS/closure caveats | 0.45 |

The **dangerous** outcomes, named and reported first if they occur: any
component with fixed-factor image `≥ 32` (the first candidate for a climb), and
in particular any reaching `35` (see stopping rules). A `dim W_int > 31` would
already be a partial reversal (the interior alone would carry unexpected
reducibles) and is reported immediately.

## 5. Named falsifiers / stopping rules

- **A rank-35 component settles the question the other way and is a first-class
  result.** If any component of the normal cone (interior or boundary, any order)
  has fixed-factor image `35`, stop, verify it (second prime, char-0 where
  possible, an independent parametrisation, an explicit arc/limit exhibiting a
  reducible quartic in `D_5 ∩ W` off the 31-family), and report it as
  `R_5 ⊆ D_5` — the headline reversal, not buried.
- **KC1.** s66's order-1 reducible row `29, 29, 28, 28, 24` (`ker, coker, c21,
  c32, prim`) and `SP` at 26 must reproduce at both primes before any new number
  is reported; the interior bound must reproduce s32's exact `31`.
- **KC2 / KC3 / KC4.** Every tangent spanning vector annihilates `dΦ`; prime
  agreement on every reported number (disagreement → third prime `2147483587` and
  re-derivation); a V-point is used only after `g_1..g_{q−1} ≡ 0` and `π g_q = 0`
  are verified there.
- Do not re-measure images session 66 already has; its table is the input.
- A component that cannot be bounded is **named** and left named, with its
  dimension and what is known about it. An unnamed gap is worse than a named one.
- Every CAS run under `timeout` with pid logged; nothing over 5 MB committed.

## 6. What a result would mean (stated before the measurement)

- **All residues closed, every component `< 35`, the interior at `31`:** the
  normal cone `Proj gr_J R` is exhausted, the special-normal-cone loophole is
  closed at every component over `Sing V(J)`, and `R_5 ⊄ D_5` becomes a theorem
  (with the exact status — proved / measured / CAS-certified — recorded
  per component). This is the upper bound s54/s59/s66 named as the missing object.
- **Some residues closed, the list reduced from four to fewer:** the partial
  result the brief accepts as success short of the theorem — the component
  enumeration with each remaining residue stated precisely (its dimension, its
  order-1 image, why the box did not finish).
- **A rank-35 component:** the reversal (§5).

## 7. Deliverables

`results/PREREG_s72.md` (this file, committed first); `docs/s72_report.md`; the
component enumeration and per-component bounds as `results/s72_normal_cone.md`
and `results/s72_normal_cone.jsonl`; code under `analysis/wk11_s72_*.py`; CAS
inputs `analysis/wk11_s72_*.sing/.m2`; logs and pids under `results/logs/s72_*`;
bundle `s72_upperbound.bundle` + `.md5`. No single-writer file is touched
(`paper/det3-conductor.tex`, `PROJECT_NOTES.md`, `docs/boundary_deficit.html`).
