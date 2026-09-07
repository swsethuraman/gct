# Pre-registration — Session 66 (C5): the `r = 5` special normal cone at the primitive family

Branch `s66-primitive`, off `main` tip `226b4ef1` (fresh public clone, container
only; ancestry gate `git merge-base --is-ancestor 226b4ef1 HEAD` passed before
anything else; delivered by single-ref bundle, not pushed).  Committed **before
any measurement**.  Labels used in the report: **proved** / **measured** /
**adopted-from-literature** / **expectation**.

Two notes on the brief before the science.  (1) `docs/batch10_worker_preamble.md`
and `docs/batch10_plan.md` are named as required reading; neither exists in the
tree at `226b4ef1`, nor in the laptop's `work/docs` or `gct-rewrite/docs`.  The
brief itself carries the correction, the tasks and the stopping rules, and this
session runs from the brief alone.  (2) The brief's preamble rules that could be
recovered from the standing conventions — bound every CAS run and record its
pid, bank every cell with a commit, nothing over 5 MB — are applied as written
in `/areas` memory and `docs/s61_review.md` §7.

## 0. The question, stated exactly

`D_5 = closure Φ(X_5)`, `Φ(M) = det M(s)`, `X_5 = Hom(C^5, M_4)` (dim 80),
`D_5 ⊆ Sym^4 C^5` of dim 50; `W = {s_5·c}` (dim 35).  `R_5 ⊆ D_5 ⟺ dim(D_5∩W) =
35`; `≥ 31` is certified over `Q` (s59).  An upper bound `< 35` is a theorem.

The base locus `B_5 = {M : det M(s) ≡ 0}` is the bounded-rank-`≤3` locus.  The
exceptional divisor `E ⊂ Bl_{J}X_5` maps onto the boundary; over a point
`M_0 ∈ B_5` its fibre is the set of leading forms of arcs based at `M_0`, and a
component of `E` living over a **special** sublocus of `B_5` is exactly the
"hidden climb" s59 could not exclude by generic sampling.  The first-order
signature of such a component is a direction in `ker dΦ_{M_0}` not tangent to any
known component of `B_5` through `M_0` — the **transverse quotient**.  The
integrator's correction to the external audit (`docs/rees_boundary_audit.md`)
found that quotient to be **zero**, not four, at every compression incidence
tested, and ranked the primitive family first.  This session does the primitive
family.

## 1. The components of `B_5` at `r = 5` (expectation, to be verified)

A 5-pencil with `det ≡ 0` has image a bounded-rank-`≤3` subspace of `M_4` of
dimension `≤ 5`.  By s32 Theorem 4 / Atkinson 1983 (Huang–Landsberg's reading:
"the only primitive examples are Example 2.3 and its projections"), the maximal
types are the four compression spaces and two non-compression types, each with
its transpose:

| name | matrices | dim of the pencil locus |
|---|---|---|
| `ker` | `A e = 0` (12-dim space) + flag `P^3` | `3 + 60 = 63` |
| `coker` | `im A ⊆ W_3` + flag | `63` |
| `c21` | `A(U_2) ⊆ W_1` (10-dim) + `Gr(2,4)×Gr(1,4)` | `7 + 50 = 57` |
| `c32` | `A(U_3) ⊆ W_2` + `Gr(3,4)×Gr(2,4)` | `57` |
| `SP` | `[φ N(x) | c]`, `φ: C^3 → C^4` injective, `N(x)` the `3×3` skew matrix, `c` free (7-dim space `S_φ`) + `Gr(3,4)` | `3 + 11 + 35 = 49` |
| `SP^T` | transposes of `SP` | `49` |
| `P` | `M_φ(y) t = φ(y ∧ t)`, `φ ∈ Hom(Λ^2C^4, C^4)` (4-dim space `E_φ`) | `23 + 20 = 43` |
| `P^T` | transposes of `P` | `43` |

`P` is the programme's `prim` stratum (`wk9_s59_core.stratum_E_basis('prim')`):
the s32 `k = 4` stratum, Atkinson's Example 2.3 at `a = 4` composed with a
projection `φ`.  `SP` is the s32 `k = 3` stratum (`E_1 = diag(N(x), w)` is its
smallest member); its maximal matrix space is 7-dimensional, it lies in no
compression space, and **it is absent from the five-stratum list s54 and s59
used** — flagged here, measured below.  `P^T` and `SP^T` are genuinely distinct
from `P` and `SP`: in `E_φ` the kernel vector is linear in `y` and the cokernel
vector is quadratic (the four quadrics through two skew lines of `P^3`, the
rank-`≤2` locus of `E_φ`), so no linear reparametrisation makes `E_φ^T` a `P`-type
space.  Transposition `M ↦ M^T` preserves `Φ`, so every number below is the same
for a type and its transpose; `P^T` and `SP^T` are measured once each as a check
of that symmetry, not as new science.

**Verification rule for "component".**  A family `C` is accepted as an
irreducible component of `B_5` when, at a generic point, `dim ker dΦ_{M_0} =
rank(Jacobian of the parametrisation) = the table dimension`: a bigger
component through `M_0` would force a bigger kernel.  The same equality proves
`J` is generically reduced along `C`.

## 2. The incidences of `P` (expectation, derived from the structure of `E_φ`)

`M(s) = M_φ(u(s))`, `u : C^5 → C^4`, `K = ker φ ⊂ Λ^2C^4` (2-dim for rank-4 `φ`).

| locus | condition | dim | other components through it |
|---|---|---|---|
| `P ∩ coker` | `rank φ = 3` | `40` | `coker` only |
| `P ∩ ker` | `rank φ = 3`, `ker φ = a ∧ C^4` | `34` | `ker`, `coker` |
| `P ∩ SP` | `rank u = 3` | `41` | `SP` (with `U = im u`, `φ' = φ|_{Λ^2 U}`) |
| `P ∩ c32` | `rank u = 3`, `K ∩ Λ^2(im u) ≠ 0` | `39` | `SP`, `c32` |
| `P ∩ c21` | `rank u = 2` | `37` | `c21` (`U_2 = im u`, `W_1 = φ(Λ^2 U_2)`), `SP`, `c32` |
| `P_tan` | `K` tangent to the Klein quadric | `42` | none (interior special locus of `P`) |
| `P_meet` | the two lines meet (`ω_1 ∧ ω_2 = 0`) | `42` | none |

For rank-4 `φ` the space `E_φ` lies in no compression space whatever `K` is, so
`P_tan` and `P_meet` are special points of `P` alone; they are where a
non-reduced structure of `J` along a sublocus of `P` would show, and they are
measured for that reason.

## 3. What will be measured

All ranks by `python-flint nmod_mat`; two house primes `2147483647, 2147483629`;
Jacobians by dual numbers `ε² = 0` on the 70 coefficients of `det`, exactly as
s59; ≥ 2 seeds per point.

### 3A. The tangent table (primary)
At a generic point of each row of §1 and §2: `rank dΦ`, `dim ker dΦ`, the
tangent space of every component through the point, their span, and the
transverse quotient `dim ker dΦ − dim(span)`.  Tangent spaces of compression
components as the audit built them (`δP·B_i + B_i·δQ + δB_i`); of `P` as the
image of `d(φ, u)`; of `SP` as the image of `d(φ, x, c)` plus the `Gr(3,4)`
directions `c(s) w^T`.  **Every spanning vector is checked to annihilate `dΦ`**
before it is counted.

**A parametrisation artefact, declared in advance.**  At a rank-3-`u` point the
fibre of `(φ, u) ↦ M` jumps from 1 to 2 dimensions, so the Jacobian image of `P`
there is at most `42 < 43` (the count in §4 gives `≤ 40`).  A positive quotient
produced only by that shortfall is not an exotic direction.  Where a Jacobian
image falls short of the component's dimension, the **limit tangent space** along
a random curve inside the component (the reduction mod `ε` of the saturated
column module of the Jacobian over `F_p[ε]`, computed by valuation-pivoted
elimination over `F_p[ε]/ε^K`) is added; it has the component's dimension and
lies in the Zariski tangent space.  Only a quotient that survives this is
reported as transverse.

### 3B. The second-order quadrics (the audit's §11 object, without the reduction)
At each point, `Q_2 = {Σ_j c_j e_{2,j}|_{ker dΦ} : c ⊥ im dΦ}`, the space of
quadratic initial forms of `J` restricted to the kernel (`e_{2,j}` the `t²`
coefficient of `det(M_0 + tN)`).  Its dimension is linear algebra.  The tangent
cone of `V(J)` at `M_0` lies in `V(Q_2)`.  If the components through `M_0` have
tangent spaces `T_i` with `Σ T_i = ker dΦ` and pairwise-transversal linear ideals,
`dim I(∪T_i)_2 = Σ_{i<j} codim T_i · codim T_j`, and `dim Q_2` is at most that,
with equality iff the quadrics cut out `∪T_i` exactly.  **Counting facts fixed
now:** at `P ∩ SP` (codims 8 and 2 in a 51-dim kernel) the bound is 16 and
`Q_2` has at most `70 − 29 = 41` generators, so equality is possible; at `P ∩
coker` (codims 23 and 3 in a 66-dim kernel) the bound is 69 but `Q_2` has at most
`70 − 14 = 56` generators, so `V(Q_2) ⊋ T_P ∪ T_coker` **with certainty** and the
second order cannot decide there; the same counting at the audit's `c21 ∩ c32`
(codims 7, 7 in 64: bound 49, audit found 23) says its proposed primary
decomposition would have found extra second-order components necessarily.
Where `dim Q_2` is below the bound and the number of variables allows, the
minimal primes of `Q_2` are computed in Singular / Macaulay2 / msolve, bounded
and pid-logged, **time-boxed to 30 minutes per run**, partial output reported.

### 3C. The reducible exceptional image over each incidence (s59's identity)
For each incidence locus of §2 (and `SP`, `SP^T`), the dimension of the
reducible family `[g_q/s_5]` at a generic V-point at contact orders `q = 1, 2`
(and 3 where the order-2 run is cheap), by `rank d(g_1..g_q) − rank d(g_1..g_{q-1},
π g_q)` with the V-point verified.  This is the audit's "first-order reducible
dimension at the intersections" extended to the primitive world, and is the
number compared against 31 and 35.

### 3D. Calibration (KC1), before anything new
Reproduce the audit's table at `c21 ∩ c32`: `rank dΦ = 16`, `ker = 64`, `T c21 =
T c32 = 57`, intersection `50`, span `64`, quotient `0`; and at `ker ∩ coker`:
`5 / 75 / 63 / 63 / 75 / 0`; and s59's order-1 reducible row `29, 29, 28, 28, 24`
over `ker, coker, c21, c32, prim`.

## 4. Predictions, with priors

Derivations behind T0–T3 use `adj M_0(s) = u(s)·v(s)^T` (kernel × cokernel
vector) and `dΦ(N) = v^T N u`, so `im dΦ` is a product of ideal pieces whose
dimensions are Hilbert-function counts; they are recorded here as the
**expectation** they are, to be confirmed or refuted by the measurement.

| id | prediction | prior |
|---|---|---|
| C0 | the eight families of §1 are components with the stated dimensions, and `dim ker dΦ = dim` at a generic point of each (`J` generically reduced along every component) | 0.75 |
| T0 | generic `P`: `rank dΦ = 37` (`= dim I_4 + dim I_3 = 25 + 12` for the ideal of two skew lines), `ker = 43 = T_P`, quotient **0** | 0.80 |
| T0' | generic `P^T`, `SP^T`: same numbers as `P`, `SP` | 0.95 |
| T1 | generic `SP`: `ker dΦ = 49 = T_SP`, quotient 0 | 0.60 |
| T2 | `P ∩ coker` (rank-3 `φ`): `rank dΦ = 14`, `ker = 66`, `T_P + T_coker = 66`, quotient 0 | 0.60 |
| T3 | `P ∩ SP` (rank-3 `u`): `rank dΦ = 29` (`13 + 8 + 8`, ideal of two points in `P^2`), `ker = 51`, quotient 0 after the limit-tangent correction; the raw Jacobian image of `P` is `≤ 40` | 0.55 |
| T4 | `P ∩ c21`, `P ∩ c32`, `P ∩ ker`: quotient 0 | 0.50 each |
| T5 | `P_tan`, `P_meet`: `ker dΦ = 43 = T_P`, quotient 0 | 0.50 each |
| Q0 | generic `P`: `dim Q_2 = 0` | 0.90 |
| Q1 | `P ∩ SP`: `dim Q_2 = 16` (the quadrics cut out `T_P ∪ T_SP` exactly) | 0.40 |
| E1 | reducible exceptional image over every incidence at `q = 1, 2`: `≤ 31` | 0.75 |
| V | no transverse direction anywhere tested in the primitive world; verdict "the compression and primitive worlds both produce no exotic first-order direction" | 0.55 |

The **dangerous** outcomes, named: a transverse quotient `> 0` surviving 3A's
correction at any point; a minimal prime of `Q_2` that is not the tangent space
of a known component and carries a reducible image `≥ 32`; any E1 value `≥ 32`.
Any of these is reported first and is not extracted further than the brief asks.

## 5. Named falsifiers / stopping rules

- **KC1.** The audit's two incidence tables and s59's order-1 row must reproduce
  at both primes before any new number is reported.
- **KC2.** Every spanning vector of every tangent space must annihilate `dΦ`; a
  vector that does not is a bug in the parametrisation, and the point is not
  reported until it is fixed.
- **KC3.** Prime agreement on every reported number; disagreement → third prime
  `2147483587` and re-derivation.
- **KC4.** A V-point is used only after `g_1..g_{q−1} ≡ 0` and `π g_q = 0` are
  verified at that point.
- **No generic `q > 4` sweep** (s59: `29,29,28,28,24` invariant in `q`); no broad
  brute-force Rees algebra; every CAS run launched with `timeout`, pid recorded
  under `results/logs/`, primary decomposition time-boxed at 30 min per run.
- If the primitive locus and all of §2 give quotient 0, the session says so,
  records the strengthening, and moves to `SP` and its incidences (the next base
  type in the audit's order) with the same table.

## 6. What a result would mean (stated before the measurement)

- Quotient 0 everywhere tested, `Q_2` cutting out the unions where the count
  allows, E1 `≤ 31`: the special-normal-cone loophole is closed **at first and
  second order at generic points of every base type and every listed
  incidence** — a real strengthening of the negative, not a proof of it.  What
  remains open is a component of `E` over a locus deeper than the ones listed,
  or one visible only at contact order `≥ 3` at a special point; the report will
  say so in those words.
- A transverse direction, or an extra minimal prime with reducible image
  `≥ 32`: the first candidate for the hidden component; its reducible image
  against 35 is the number that matters, reported with the arc that produces it.

## 7. Deliverables

`results/PREREG_s66.md` (this file, committed first); `docs/s66_report.md` with
the tangent table in the audit's shape for every point tested; code
`analysis/wk10_s66_*.py`; CAS inputs and outputs `analysis/wk10_s66_*.sing/.m2`;
data `results/s66_*.json`; logs `results/logs/s66_*`; bundle
`s66_primitive.bundle` + `.md5`.  No single-writer file is touched.
