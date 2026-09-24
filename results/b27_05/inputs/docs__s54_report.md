# Session 54 — Is `R_5 ⊆ D_5^{det_4}`? Exact: no. Closure: open, evidence for no, residue named

Branch `s54-r5d5`, off `origin/main` tip `eb8cecb` (fresh public clone,
container only; not the owner of the laptop folder — delivered by bundle, no
push). Pre-registration `results/PREREG_s54.md` (commit `053f4d0`, before any
measurement). Code `analysis/wk9_s54_*.py`; data `results/s54_*.json`,
`results/s54_cells_d{6,7,8,9}.jsonl`, `results/s54_length5_census.json`.
Labels: **proved** / **measured** / **adopted-from-literature** /
**expectation**.

`python-flint` for every rank; two house primes `2147483647, 2147483629`; every
`mult = a` reading is a certificate (rank a rigorous lower bound, `mult ≤ a`);
`rank(R)=nb−a` self-check passed at every measured cell; the reducible-point
sampler was cross-checked against the padded-permanent evaluation
(`mult_red = mult_pad` at `r=5`) at the calibration cells; the dual-number
tangent machinery was calibrated to `dim D_5 = 50` and `dim T_q R_5 = 39`.

## 0. Verdict

> **Exact question — settled negative (adopted from s32, re-framed here).** A
> general reducible quinary quartic `ℓ·c` is **not** a `4×4` determinant of linear
> forms: `R_5 ⊄ Φ(X_5)`. For a fixed linear factor, `dim{c : ℓ·c ∈ Φ(X_5)} = 31`
> (s32, max over the singular-subspace branches); with the `+4` for the choice of
> `ℓ`, the exactly-determinantal reducibles have dimension **35** — codimension
> **4** in `R_5` (`dim R_5 = 39`).
>
> **Closure question `R_5 ⊆ D_5^{det_4}` — not settled.** The one rigorous fact
> is a lower bound, `dim(R_5 ∩ D_5) ≥ 35` (the exact locus sits inside the
> closure). Containment holds **iff** this is `39`, i.e. iff the boundary `∂D_5`
> supplies the **4** reducible dimensions the exact locus lacks. Equivalently,
> with `W = {s_5·c}` (dimension 35), `R_5 ⊆ D_5 ⟺ dim(D_5 ∩ W) = 35`, and the
> exact part already gives `dim(D_5 ∩ W) ≥ 31`; the question is the `31 → 35` gap.
>
> **Evidence says the boundary supplies none of the four — so `R_5 ⊄ D_5`.** Two
> independent instruments agree, and neither reaches beyond the exact `35`:
> - **Multiplicity (blind in range).** At every reachable length-5 cell through
>   `δ = 9`, `mult_det = mult_red = a` (`D = 0`); no covariant of degree `≤ 9`
>   separates `D_5` from `R_5`. A refutation in range would need
>   `onset I(D_5^{det_4})_{ℓ=5} ≤ 9`; the data (and the onset conjecture, cap 300)
>   say higher.
> - **Base locus (order-1 adds nothing).** The order-1 border reducibles reach
>   only dimension `≤ 29` in every stratum (ker 29, coker 29, (2,1) 28, (3,2) 28,
>   prim 24) — below even the exact `31`. The first order of contact contributes
>   no reducible not already exact.
>
> A complete proof needs one of: the **higher-order** (`q ≥ 2`) border reducible
> dimension — the full Rees/exceptional-image computation, exactly session 53's
> object — or a length-5 equation of `I(D_5^{det_4})` at degree `> 9`, which is
> **outside** the accessible range (this refines the brief's expectation that a
> negative would place an equation _inside_ `δ ≤ 9`: at length 5 there is none
> through `δ = 9`).
>
> **Structural finding.** Reducible quartics are **singular points of `D_5`**:
> summing `im dΦ` over the entire determinantal fibre of one reducible `q`
> saturates the first-order tangent at **64 > 50 = dim D_5** (both primes, stable
> under `GL_4×GL_4` conjugation and richer representations). `D_5` is singular
> along its reducible locus — which is why the exact-reducible pencils are
> rank-deficient (`dim im dΦ ≤ 42`) and why the tangent test cannot be promoted to
> a proof without the ideal `I(D_5)`.
>
> **Pilot result for session 53 (why this session ran first).** The
> base-locus/blow-up machinery is fully tractable at `r = 5` (seconds to a few
> minutes throughout). **Warning that transfers to `r = 10`:** the **order-1**
> exceptional image already _fills_ `D_5` (dimension 50), so first determinant
> polars do **not** isolate the boundary — a concrete confirmation of the brief's
> own §1 reframing that the first-polar version is the wrong object and the
> higher-order Rees analysis is mandatory. The genuine cost at `r = 10` is the
> higher-order exceptional image; even at `r = 5`, where the whole gap is a mere
> **4 dimensions**, order 1 could not close it.
>
> **Correction to flag (single-writer files, not edited).**
> `docs/washout_lemma.md` Theorem 3(3) and `docs/transfer_lemma.md` Theorem 3
> item 4 assert the set-theoretic fact "`R_5 ⊄ D_5^{det_4}`" citing s32 Theorem 5.
> s32 Theorem 5 proves non-containment in the **image** `Φ(X_5)`, **not** in the
> **closure** `D_5^{det_4}`. The closure statement is precisely this session's
> question. This session's evidence supports the conclusion those documents
> assert — so the `ℓ ≤ 5` exclusion is very likely safe — but it currently rests
> on the image result plus measurement plus the dimension evidence here, not on a
> proof of closure non-containment. The distinction should be recorded.

## 1. Objects and the reduction that makes the question sharp

`D_5 := D_5^{det_4} = closure{ det_4(s_1A_1+...+s_5A_5) : A_i ∈ M_4 } ⊆ Sym^4 C^5`,
`dim 50`; `R_5 = {ℓ·c} ⊆ Sym^4 C^5`, `dim 39` (both **proved**, washout Cor. 7).
`Φ : X_5 = Hom(C^5,M_4) → Sym^4 C^5`, `Φ(M) = det M(s)`; `D_5 = closure Φ(X_5)`
is a **closure**, so `R_5 ⊆ D_5` asks whether `ℓ·c` is a _limit_ of `det_4`
pencils, not (settled no, s32) whether it is one.

**Only length exactly 5 matters** (**proved**; PREREG T2). A length-`k`
highest-weight vector sees only the `k`-plane restriction (restriction lemma);
for `k ≤ 4` that lands in `D_4^{det_4} ⊇ R_4` (exact block construction,
s27/s32 §6), so `mult_red ≤ mult_det` automatically at `ℓ(λ) ≤ 4`.

**At `r = 5`, `mult_red = mult_pad`** (**proved**, washout Thm 3(1), `P_5 = R_5`).
Functoriality (brief_wording §7): `R_5 ⊆ D_5 ⟹ mult_red ≤ mult_det` for every
length-5 `(λ,δ)`; a cell with `mult_red > mult_det` refutes containment (and,
`r ≤ 5`, is a genuine `D > 0` with no transfer gap). The converse fails
(l5_containment §4), so the multiplicity route can only refute; the positive
direction is geometric.

## 2. Route A — general quinary cubic is not a border `3×3` determinant *(proved; closed)*

The cheap affirmative the brief flags — realise `ℓ·c` as `diag(ℓ, border-N)` —
needs a general quinary cubic to be a **border** `3×3` determinant, i.e.
`D_5^{det_3} = Sym^3 C^5`. It is not: `D_5^{det_3}` is a **closed** variety of
dimension `29 < 35` (**proved**, washout Cor. 7; s28), so a general cubic is not a
border `det_3`. The block route reaches only `ℓ·(dim-29 cubics)`, and the exact
`4×4` route caps at `dim-31` cubics (s32). No cheap affirmative; the question is
the higher-order border (Route B).

## 3. Multiplicity sweep — clean, and blind in range *(measured)*

Census (`analysis/wk9_s54_census.py`) and sweep (`analysis/wk9_s54_measure.py`,
ascending weight-space size, both primes, `mult_det` at `det_4` points and
`mult_red` at reducible `ℓ·c` points):

| `δ` | length-5 cells (`a>0`) | measured (`nb ≤ 2500`) | result | balanced cells (skipped) |
|---|---|---|---|---|
| 6 | 105 | 17 | `mult_det = mult_red = a` (all `D=0`) | 88 |
| 7 | 239 | 15 | `mult_det = mult_red = a` | 224 |
| 8 | 435 | 12 | `mult_det = mult_red = a` | 423 |
| 9 | 708 | 12 | `mult_det = mult_red = a` | 696 |

**Zero refutations; `mult_det < a` and `mult_red < a` never occurred.**
Calibration (KC1) passed: `mult_det = mult_red = mult_pad = a` at every `δ=6`
cell, reproducing s27's nine `δ=6` cells and the washout identity; `rank(R)=nb−a`
held at both primes on every cell.

**Scope, stated plainly.** The dense flint rank reaches only **skewed** weights
(`nb ≤ 2500`); **balanced** cells — where an equation of a `GL_5`-variety first
tends to appear — have `nb ~ 10^4`–`10^5` and are beyond the dense route (the
s42 sparse Wiedemann route would extend this; it is the natural continuation). So
the sweep rules out a refutation among skewed weights through `δ = 9` and is
consistent with `onset I(D_5^{det_4})_{ℓ=5} > 9`; a refutation needs `onset ≤ 9`.
The route is **blind to this closure question in range** — the situation
l5_containment §4 anticipated.

## 4. Route B — base-locus method; order 1 fills `D_5` and adds no reducibles

`X_5 = Hom(C^5, M_4)`, base locus `B_5 = {M : det M(s) ≡ 0}` = pencils whose
image is a bounded-rank-`≤3` space of `M_4`. Over `M_0 ∈ B_5`, an arc
`M_0 + tM_1 + …` has `det = t^q f(s) + O(t^{q+1})`; the order-1 leading quartic is
`f_1 = tr(adj M_0(s) M_1(s))`, and `[f_1] ∈ D_5`.

- **Calibration (measured).** The dual-number Jacobian reproduces `dim D_5 = 50`
  as the tangent at a generic determinantal point (`analysis/wk9_s54_bdim.py`,
  `Honly = 50`, both primes).
- **Order-1 image fills `D_5` (measured).** Over each bounded-rank-3 stratum (the
  four compression types and the dimension-4 primitive family
  `C^4 ⊂ Hom(C^4, Λ^2 C^4)`, s32 Thm 4 / Atkinson–Huang–Landsberg, verified
  against the sources), `dim{f_1}` is `50, 50, 47, 47, 49`. So the order-1 special
  fibre is **not** a proper boundary component — it recovers `D_5`. First
  determinant polars do not isolate the boundary at `r = 5` (pilot warning for
  s53), and will not at `r = 10`.
- **Order-1 reducible border (measured).** `dim{c : s_5·c ∈ order-1 image}` per
  stratum, at a generic point of `V = {f_1 divisible by s_5}`
  (`analysis/wk9_s54_dimDW.py`, constrained Jacobian `rank(dG) − rank(π·dG)`, both
  primes): ker 29, coker 29, `(2,1)` 28, `(3,2)` 28, prim 24 — all **below** the
  exact `31`. The order-1 border adds no reducible beyond the exact ones.

## 5. Reducibles are singular points of `D_5` *(measured)*

At an exact reducible `q = s_5·c_0 = det M_*` (`analysis/wk9_s54_tangent.py`,
`_union.py`, `_saturate.py`):

- A single representation gives `dim(im dΦ_{M_*}) ≤ 42 < 50`; summing `im dΦ_M`
  over the determinantal fibre of the _same_ `q` (block, upper/lower-triangular,
  `GL_4×GL_4` conjugates) **saturates at 64** — stable from 7 representations on,
  both primes. Since `im dΦ ⊆ T_q^{Zar} D_5`, the Zariski tangent is `≥ 64 > 50`:
  **`D_5` is singular along the reducible locus.**
- `dim T_q R_5 = 39` (validated); `dim(T_q R_5 ∩ (64-dim first-order tangent)) =
  33`, stable across representations and primes.

Why the tangent test is not a proof. The saturated first-order tangent (64) is a
_lower_ bound on `T_q^{Zar} D_5`; the exact-reducible sublocus already forces
`T_q R_5 ∩ T_q^{Zar} D_5 ≥ 35`, so the 64-dim space understates the true
intersection, and turning "`T_q R_5 ⊄` tangent" into "`R_5 ⊄ D_5`" needs an
_upper_ bound on `T_q^{Zar} D_5` — equivalently a low-degree equation of
`I(D_5)`, which the §3 sweep shows does not exist through `δ = 9`. So this finding
sharpens the geometry (`D_5` is genuinely singular at reducibles) without closing
the question; the decisive quantity remains the §4/§6 dimension.

## 6. What is settled, what resists

**Settled (at the stated rigor):**
- Route A closed: general quinary cubic is not a border `3×3` determinant
  (`dim D_5^{det_3} = 29 < 35`) — **proved**.
- `dim(R_5 ∩ D_5) ≥ 35`, from the exact reducible locus (**adopted** from s32 +
  the `ℓ`-count).
- No multiplicity refutation among skewed length-5 weights through `δ = 9`;
  `mult_det = mult_red = a` there — **measured**, both primes, certificate.
- Order-1 exceptional image fills `D_5` (dim 50); order-1 border reducibles
  `≤ 29 < 31` — **measured**.
- Reducible quartics are singular points of `D_5` (Zariski tangent `≥ 64`) —
  **measured**.

**Resists — one case, stated exactly:** the **higher-order (`q ≥ 2`) border
reducible dimension** — whether `dim(D_5 ∩ W)` climbs from `31` to `35` once arcs
of contact order `≥ 2` enter. This is the exceptional image of the Rees blow-up
`Proj R(J)` restricted to the reducible locus, session 53's object at `r = 10`;
the `r = 5` pilot shows it is the whole remaining cost (a 4-dimensional gap here),
not a formality. Equivalently: the separating equation of `I(D_5^{det_4})` at
length 5, which must exist if `R_5 ⊄ D_5`, sits at degree `> 9`.

## 7. Honest boundary

- **Proved:** the length-exactly-5 reduction (T2); Route A's negative; the
  calibrations (`dim D_5 = 50` two ways; `dim T_q R_5 = 39`; `rank(R)=nb−a`).
- **Measured (exact, two primes, certificate where `mult = a`):** the §3 sweep
  (`D = 0` at 56 reachable cells); §4 order-1 dimensions (`50,50,47,47,49`;
  reducible `29,29,28,28,24`); §5 tangent saturation (`64`) and intersection
  (`33`).
- **Adopted:** s32 Thm 5 (exact non-containment; `dim{c : ℓc det} = 31`); washout
  Cor. 7 dimensions; Atkinson–Huang–Landsberg bounded-rank-3 classification.
- **Not proved:** the closure verdict, in either direction. Evidence leans to
  `R_5 ⊄ D_5`. A proof needs the higher-order exceptional-image dimension or the
  degree-`>9` equation.
- **Not done (natural continuation):** the s42 sparse Wiedemann route on the
  balanced length-5 cells (to test `mult_det = a` beyond skewed weights); the
  order-`≥2` Rees computation over the strata (the §6 residue, shared with s53).
- **Flagged for the single writer:** washout Thm 3(3) / transfer_lemma item 4
  cite s32 for closure non-containment; s32 proves only image non-containment.

## 8. Pre-registration scorecard

| id | prediction | prior | outcome |
|---|---|---|---|
| A | general quinary cubic not a border `3×3` determinant | 0.90 | **confirmed** (`dim D_5^{det_3}=29<35`) |
| M1 | no length-5 cell with `mult_red > mult_det`, `δ ≤ 9` | 0.65 | **held on reachable (skewed) cells**; balanced cells not reached |
| M2 | every measured length-5 cell has `mult_red = mult_det = a` | 0.55 | **confirmed** on the 56 reachable cells |
| M3 | a negative shows up as a det-side bite in range | 0.30 | **not seen** — det side clean through `δ=9`; any separation is at higher degree |
| B1 | some stratum's exceptional image contains reducibles | 0.50 | **yes** (order 1), only the dim-`≤29` block-type reducibles |
| B2 | reducibles reached fill dim `< 39` | 0.40 | **confirmed** in every route (exact 35, order-1 border ≤ 33) |
| V | net verdict `R_5 ⊆ D_5` (positive) | 0.55 | **revised to lean `⊄`**; not proved |

New (unregistered) findings: reducible quartics are singular points of `D_5`
(Zariski tangent `≥ 64`); the order-1 exceptional image fills `D_5` — the two
facts that make the pilot's message to s53 concrete.
