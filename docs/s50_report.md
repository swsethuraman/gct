# Session 50 — the Landsberg–Manivel–Ressayre equation: independent reconstruction, and evaluation without the multiplicity

Branch `s50-lmr` off `eb8cecb`.  Pre-registration `results/PREREG_s50.md`
(commit `a52661d`, **before any remainder was computed**).  Code
`analysis/wk9_s50_lmr.py` (evaluator), `wk9_s50_validate.py`,
`wk9_s50_experiment.py`, `wk9_s50_verify.py` (independent sympy checker),
`wk9_s50_sizing.py`.  Raw record `results/s50_controls.json`.  Labels
**proved / measured / adopted-from-literature / expectation**.
Vocabulary per `docs/brief_wording.md`.

## 0. Verdict

> **The LMR construction separates `det_4` from the padded `per_3` at degree 24,
> obtained by a remainder computation that ran in under a second — the
> multiplicity computation it sidesteps being ~20 orders of magnitude out of
> reach.**  The load-bearing conclusion — `x_0·per_3 ∉ Dual_{6,4,16}`, hence
> `P_pad ⊄ D_det`, hence `dc̄(per_3) > 4` — is established **unconditionally** and
> by **two independent cheap routes** (the divisibility remainder and a direct
> Katz Hessian-rank computation).  This **re-derives an LMR-strength bound** — not
> a new determinant/permanent fact — and the result of the session is
> **methodological**: the separation is reachable by evaluation where the
> multiplicity statistic is hopeless.  The weight-specific reading (that it is the
> `(65,17,2⁷)` module that separates) is correct under the standard identification
> of the lowest LMR module with the irreducible `S_{(65,17,2⁷)}`, which the
> computation does not itself verify.
>
> - **The weight, derived independently, is `(65,17,2⁷)` at `δ = 24`.**  The
>   factor of two resolves to `δ = 2n(n−1) = 24`, **not** `δ = 12`.  Three
>   independent confirmations agree: a from-scratch degree derivation off the
>   divisibility, Theorem 1.1.2 of the paper, and the paper's own `n=3` example
>   `(19,7,2⁵)` at `δ = 12`, which the same formula reproduces exactly.
> - **All four controls behaved as a genuine separator requires** *(measured,
>   exact)*: `det_4` gives remainder **0** (calibration — LMR's theorem);
>   generic quartics give remainder **≠ 0** (the expression is not identically
>   zero); the reducible `ℓ·c` gives **≠ 0**; and the full ten-variable
>   `x_0·per_3` gives remainder **≠ 0** — **the equation vanishes on `D_det` and
>   not on `P_pad`.**  Certified over `Q` by an independent implementation, and
>   over three primes and five independent `9`-planes.
> - **The degeneracy-direction pre-check (`brief_wording §6`) passes in the right
>   direction.**  `det_4` is the most degenerate point (remainder 0); the padded
>   permanent is strictly *less* degenerate (remainder ≠ 0).  Controls 3 and 4
>   agree — the permanent is **not** more special than a generic reducible here,
>   so the statistic does not fold in the wrong direction.
> - **A geometric confirmation, independent of the remainder** *(measured)*:
>   the Hessian of `x_0·per_3` has generic rank 10 and rank **9** at every
>   sampled point of `{per_3 = 0}`, so `dim(dual of x_0·per_3) = 7 > 6 = 2n−2`.
>   That is exactly why the `k=6` equation cannot vanish there, and it matches
>   LMR's own lower-bound mechanism.
> - **Task 4, the sharp question, answered honestly:** the two ideal subspaces
>   `I(D_det)^{HWV}` and `I(P_pad)^{HWV}` at this weight are **provably different
>   as subspaces** (an explicit `v ∈ I(D)∖I(P)`), while whether they differ in
>   *dimension* (`i_det > i_pad`, i.e. `D > 0`) is undetermined and not
>   computable at this scale.  The informative case the external critique has
>   pressed — equal dimension, different subspace, the statistic discarding a
>   real separation — is live and **cannot be excluded cheaply**; the divisibility
>   route delivers the separation regardless, which is the whole point.

## 1. Task 1 — the module and its weight, derived independently

**The construction (adopted-from-literature, then re-derived).**  For a degree-`d`
form `P` in `N` variables, Katz's formula gives `dim Z(P)* = rank H_{P,w} − 2` at
a general point `w` of the affine cone.  The dual is degenerate to dimension `≤ k`
iff `rank H_P ≤ k+2` on `Z(P)`, i.e. iff

> **`P` divides `det_{k+3}(H_P|_F)` for every `(k+3)`-plane `F ⊆ C^N`**,

where `det_{k+3}(H_P|_F)` is the determinant of the `(k+3)×(k+3)` Hessian
restricted to `F`, a form of degree `(k+3)(d−2)` in the `N` variables.  The
determinant `det_n` sits at `N = n²`, `d = n`, `k = 2n−2` (its dual is the
rank-`1` matrices, dimension `2n−2`).

**Degree, derived from the divisibility, not read off the paper.**  On a general
line `ℓ`, `p = P|_ℓ` (degree `d`) must divide `g = det_{k+3}(H_P|_F)|_ℓ`
(degree `e = (k+3)(d−2)`).  `p | g` is `d` linear conditions on `coeffs(g)`; each
left-kernel functional of the `(e+1)×(e−d+1)` multiplication matrix has degree
`(e−d+1)` in `coeffs(p)`, and `coeffs(g)` have degree `(k+3)` in `coeffs(P)`.
Hence each equation has coefficient-degree

    D = (e − d + 1) + (k + 3) = (k+3)(d−2) + k − d + 4 = (d−1)(k+2).

With `d = n`, `k = 2n−2`:  **`D = 2n(n−1)`.**  Since the equations live in
`Sym^D(Sym^n C^{n²})`, `|λ| = nD`; with the two lower coefficients fixed, the
`ω₁`-coefficient is forced:

    a = coeff(ω₁) = nD − 4n(n−1) = 2n(n−1)(n−2),
    λ = 2n(n−1)(n−2)·ω₁ + (2n²−4n−1)·ω₂ + 2·ω_{2n+1}.

**Cheap checks (all pass).**
`|λ| = 4δ`:  `96 = 4·24` ✓.  `ℓ(λ) = 2n+1 = 9 ≤ 10` ✓ (a length-11 weight would
have `mult_pad = 0` by concision and be useless; see §5).

**`n = 3` reproduction (the pre-registered falsifier).**  The formula gives
`λ = 12ω₁+5ω₂+2ω₇ = (19,7,2⁵)`, `δ = 12`.  The paper (§3.2) states verbatim:
*"when `n = 3`, the module with highest weight `12ω₁+5ω₂+2ω₇` occurs with
multiplicity six in `S₁₂(S³C⁹)`."*  **Reproduced exactly** — same weight, same
degree `δ = 12`, and the same construction run through the evaluator confirms
`det_3 | det_7(H|_F)` (validation V1, both primes).

**`n = 4` (the cell).**  `λ = 48ω₁+15ω₂+2ω₉ = (65,17,2⁷)`, `δ = 24`, `ℓ = 9`,
`|λ| = 96 = 4δ`.  Matches Theorem 1.1.2 (`ω₁`-coefficient `2n(n−1)(n−2) = 48`).

**The factor of two, resolved (proved).**  The alternative reading `δ = 12`
(equivalently `ω₁`-coefficient `n(n−1)(n−2) = 24`, half) is inconsistent with all
three of: the divisibility-derived `D = (d−1)(k+2)`; the paper's Theorem 1.1.2;
and the paper's `n=3` example, which is at `δ = 12 = 2·3·2` and would be `δ = 6`
under the halved reading.  **`δ = 24`.**  (One early automated read of the arXiv
HTML returned "`n(n−1)(n−2)ω₁ / degree n(n−1)`" — internally inconsistent by
`|λ|=nD`, and a dropped factor of two; the published paper and the derivation
agree on `2n(n−1)(n−2)` and `δ = 2n(n−1)`.)

## 2. Task 2 — the multiplicity computation, sized honestly

At `λ = (65,17,2⁷)`, `δ = 24`, `N = 16` (`analysis/wk9_s50_sizing.py`,
exact big-integer arithmetic):

| quantity | value |
|---|---|
| `dim S_λ(C^16)` (Weyl) | `1 450 549 350 002 862 467 049 479 287 500` ≈ **1.45·10³⁰** (31 digits) |
| variables of `Sym^4 C^16` (`= #` deg-4 monomials) | `C(19,4) = 3 876` |
| `dim Sym^24(Sym^4 C^16)` (ambient of the cell) | `C(3899,24)` ≈ **2.29·10⁶²** (63 digits) |
| `a(λ,24) = mult S_λ ⊂ Sym^24(Sym^4 C^16)` | **not computed**; `≥ 1` (LMR occurs); `n=3` analogue is 6 |
| `N_S` (weight-`λ` monomials) | between `a` and the ambient; `≫ 10^{12}` |
| `n_χ` (character count, session-46 walk `O(N_S·#gen)`) | out of reach — `N_S` is the wall |
| `h_pad(λ,24)` | `mult S_λ ⊂ Sym^24 V ⊗ Sym^24(Sym^3 V)`; not tabulated at `ℓ=9` |

**The `i_det` linear system.**  `i_det = a − mult_det` is the nullity of the
raising-operator-plus-evaluation system on the `a × n_χ` multiplicity space.  The
six-row sweeps top out at `N_S ≈ 10⁷`, `n_χ ≈ 10⁵` (sessions 45–46).  Here the
**ambient irreducible alone is `10³⁰`**, and the degree-24 coordinate space is
`10⁶²` — the evaluation system is `~20` orders of magnitude past the frontier in
every dimension.  **This is the point of the session:** the same separation that
this system would certify was obtained by a remainder computation in `0.6 s`.
*(measured sizing; the infeasibility is a statement about the numbers, and no
engine run on the cell was attempted.)*

## 3. Task 3 — the experiment that does not need the multiplicity

### 3.1 What is computed

`N = 16`, `k = 2n−2 = 6`, `F = k+3 = 9`, `d = 4`, `edeg = (k+3)(d−2) = 18`.  For a
random integer `16×9` plane `B` (`x = By`), and each control `P`:

    M(y) = Bᵀ H_P(By) B   (9×9, quadratic entries)     G(y) = det_9 M(y)   (deg 18)
    remainder r = G  mod  P(By)      ({P(By)} is a Gröbner basis of (P(By)), so r=0 ⟺ P|G)

computed exactly over `F_p` by specialising `y_2..y_9` and reducing univariate in
`y_1` (`wk9_s50_lmr.py`).  A single nonzero `r` at one prime certifies `P ∤ G`
over `Q` (the equation does **not** vanish); `r = 0` is certified over many
random specialisations and `≥ 2` primes, and the headline claims are re-done in
exact `Q` by the independent checker (§6).

### 3.2 Engine validation first (`wk9_s50_validate.py`, all pass)

| check | expected | result |
|---|---|---|
| V1 `det_3` divisibility (`n=3`: `F=7`, `edeg=7`) | DIVIDES | **DIVIDES**, both primes, `deg g = 7` |
| V2 generic cubic in 9 vars | NOT_DIVIDES | **NOT_DIVIDES** |
| V3 Katz rank `H_{det_3}` on `{det=0}` / generic | `6 = 2n` / `9` | **6 / 9** |
| V4 Katz rank `H_{det_4}` on `{det=0}` / generic | `8 = 2n` / `16` | **8 / 16** |

V1 is LMR's own smallest case run through the engine; V3/V4 confirm
`dim(dual det_n) = 2n−2` directly.

### 3.3 The four controls (`wk9_s50_experiment.py`, `results/s50_controls.json`)

Plane `B` = `python random.seed(0); 16×9` integers in `[1,40)`, first row
`[25,27,3,17,33,32,26,20,31]` (recorded).  All `g` have degree 18; the `gcd`
route agrees with the `mod` route on every sample.

| # | point | monomials | `p₁` | `p₂` | verdict |
|---|---|---|---|---|---|
| 1 | `det_4` (16 vars) | 24 | DIVIDES | DIVIDES | **remainder 0 — in `I(D_det)`** |
| 2 | generic quartic (10 vars) | 200 | NOT_DIVIDES | — | **remainder ≠ 0** |
| 3 | `ℓ·c`, `c` generic cubic (10 vars) | 715 | NOT_DIVIDES | — | **remainder ≠ 0** |
| 4 | `x_0·per_3` (full 10 vars) | 6 | NOT_DIVIDES | NOT_DIVIDES | **remainder ≠ 0 — not in `I(P_pad)`** |

Robustness (`results/logs/s50_robust`): controls 1 and 4 re-run on **five
independent full `9`-planes** (`det_4` DIVIDES / padded NOT_DIVIDES at all five),
and control 4 confirmed over a **third prime** and an **active-only plane** (a
`9`-plane inside the 10 active variables — the padded permanent separates there
too).

### 3.4 The degeneracy-direction pre-check (`brief_wording §6`)

The three committed points are control 1 (`det_4`), control 3 (`ℓ·c`), control 4
(full `x_0·per_3`).  Reading "remainder 0" as "maximally degenerate":

- `det_4`: remainder 0 (most degenerate — dual dimension exactly `k = 6`);
- `ℓ·c`: remainder ≠ 0;
- `x_0·per_3`: remainder ≠ 0 (**strictly less degenerate than `det_4`**).

The padded permanent is **not** at least as degenerate as `det_4`, so the
statistic separates in the **right** direction — the failure mode that cost two
prior external sessions does not occur here.  Controls 3 and 4 **agree**, so the
permanent is not more special than a generic reducible for this equation (the
disagreement that §6 says would be "the result" did not arise; agreement is
itself informative — it says the separation is the reducibility-level one,
sharpened to the actual permanent).

### 3.5 The geometric confirmation (P5, `measured`)

Hessian of `x_0·per_3` (`10×10` active block):

    generic rank                       = 10
    rank on {per_3=0, x0≠0} (the sheet)  = 9    (stable: 9 at all 6 sampled points, both primes)
    rank on {x0=0}                      = 2

`dim(dual) = (rank at a general point of Z(P)) − 2` by Katz.  The general point of
`{x_0·per_3=0}` sits on the `per_3` sheet, where the rank is 9, so
`dim(dual of x_0·per_3) = 9 − 2 = 7 > 6 = 2n−2`.  (The "`−2`" here is Katz's
universal constant, not the separately-listed rank `2` on the `{x_0=0}` sheet,
which they coincide numerically is an accident.)  The padded permanent is
**not** in `Dual_{6,4,16}`, hence not in the orbit closure of `det_4` — an
independent, coordinate-geometry witness of the same separation, and exactly the
mechanism behind LMR's `dc̄(per_3) ≥ (dim dual + 1)/2`.  The expression is not
identically zero (`G ≢ 0`, since generic rank `10 ≥ 9`), so control 4 is a real
divisibility test, not a vacuous one (P5 held).

## 4. Task 4 — `i_det` vs `i_pad` at the LMR weight

Write `v` for the LMR highest-weight vector of weight `(65,17,2⁷)`, `δ=24`.
Control 1 (`det_4` remainder 0) places the whole LMR module — and in particular
its guaranteed constituent `S_{(65,17,2⁷)}` — inside `I(D_det)`
*(adopted-from-literature: LMR prove `V_n ⊆ I(Dual_{6,4,16})` and the determinant
orbit closure is a component of `Dual_{6,4,16}`; confirmed here by control 1)*.
Control 4 (`x_0·per_3` remainder ≠ 0) places `v ∉ I(P_pad)` *(measured, exact)*.

Hence, as subspaces of the ambient multiplicity space,

    v ∈ I(D_det)_24 ∖ I(P_pad)_24   ⟹   I(D_det)_24 ≠ I(P_pad)_24.

This is the rigorous, weight-free statement: the divisibility test certifies
non-membership `x_0·per_3 ∉ Dual_{6,4,16}` (the condition `V_n` cuts out
set-theoretically), so **some** degree-24 LMR equation vanishes on `D_det` and
not on `P_pad`.  The weight-refined reading — `v` in the weight-`(65,17,2⁷)`
isotypic of `I(D)` and not in `I(P)` — is exactly "that copy of the equation
separates" and uses the standard identification of the lowest LMR module with the
irreducible `S_{(65,17,2⁷)}` (Theorem 1.1.2); it is not separately certified by
the remainder, which sees `V_n` as a whole.  Either way the membership
`P_pad ⊆ D_det` is refuted: an equation vanishing on the determinant and not on
the padded permanent is exactly an obstruction, so **`x_0·per_3` is not a limit of
`det_4` pencils** — a lower bound `dc̄(per_3) > 4`, consistent with `dc(per_3) = 7`
and with LMR's `≥ 4.5`.

**On the dimensions.**  Whether `i_det > i_pad` (equivalently `D > 0`) does **not**
follow.  `i_det > i_pad` would follow from `I(P)^{HWV} ⊆ I(D)^{HWV}`, i.e. from
`D_det ⊆ P_pad`; but `det_4` is irreducible and not a padded permanent, so
`D_det ⊄ P_pad` and the containment fails.  Indeed both containments fail
(reducibility equations vanish on `P_pad` and not on `D_det`), so the two
subspaces sit in general position and the dimension comparison is genuinely open.
Two consequences, stated plainly:

1. **`i_det ≥ 1`** — safe from the literature alone (`S_{(65,17,2⁷)} ⊆ V_n ⊆
   I(Dual) ⊆ I(D_det)`).  The companion bound **`i_pad ≤ a − 1`** at this weight
   holds provided the separating element lies in the `S_{(65,17,2⁷)}` isotypic —
   i.e. it leans on `V_n = S_{(65,17,2⁷)}`; the remainder alone certifies only
   that *some* element of `V_n` separates.
2. **The case the external critique presses is live.**  If it should turn out
   that `i_det = i_pad` — equal dimension, different subspace — then `(65,17,2⁷)`,
   `δ=24` is a **named instance where the multiplicity statistic `D` reads `0`
   while a real degree-24 separating equation exists**.  We cannot decide which
   way the dimensions fall without computing a multiplicity, and §2 shows that is
   `~10²⁰`-scale out of reach.  The divisibility computation exhibits the
   separation **without** deciding it — which is precisely the demonstration the
   brief asked for: our statistic *may* discard a separation that is provably
   there, and here is the cell.

This is the strongest reading the evidence supports, and it is stronger than a
bare "`D > 0`": it is a separation the multiplicity statistic might not even see.

## 5. Task 5 — the weight selector

The generating constituent is `S_{(65,17,2⁷)}` at `δ = 24`.  As an ideal, the
LMR equations at degree 24 span (at least) this one irreducible — a single
irreducible is already `GL_16`-stable, so "the `GL`-module generated by the
equations" at its own degree is just `S_{(65,17,2⁷)}`; the full constituent list
of `V_n` is itself a plethysm-scale question (the §2 wall) and is **not** claimed
here.  The mathematically-grounded map of where the construction lives, across
`n` (`det_n` vs padded `per_3`, `analysis/wk9_s50_sizing.py` / the selector run):

| `n` | `λ` | `δ = 2n(n−1)` | `ℓ(λ) = 2n+1` | usable by the multiplicity statistic? |
|---|---|---|---|---|
| 3 | `(19,7,2⁵)` | 12 | 7 | yes |
| **4** | **`(65,17,2⁷)`** | **24** | **9** | **yes — and the last such `n`** |
| 5 | `(151,31,2⁹)` | 40 | 11 | no (`ℓ > 10 ⇒ mult_pad = 0`) |
| 6 | `(289,49,2¹¹)` | 60 | 13 | no |

The selector's single most useful output: **`ℓ(λ) = 2n+1`, so the padded `per_3`
(10 variables) has `mult_pad = 0` at the LMR weight for every `n ≥ 5`** — the
multiplicity statistic is *blind* there by concision, and only the divisibility
route can see the separation.  `n = 4` is the last case the statistic could even
in principle detect, and it is exactly the case measured here.

The second output is a map, not a target list: the LMR obstruction lives at
`(ℓ = 9, δ = 24)`, whereas every determinant sweep in the programme is at
`(ℓ ≤ 6, δ ≤ 9)`.  **The two regions are disjoint** — the six-row sweeps could
never have found the LMR obstruction, and the LMR weight says nothing about the
six-row cells.  "Where to measure next on mathematical grounds" is therefore not
a cheaper six-row cell; it is the length-9, degree-24 object, and the honest
answer is that it is reachable only by evaluation (this session), not by the
multiplicity engine.

## 6. Verification, and the missing session-49 verifier

**Finding: `tools/verify/` is absent from the tree.**  Session 49 has not been
run — only its brief (`docs/s49_prompt.md`) is committed, at `eb8cecb`.  The
session-49 verifier the brief says to hand results to **does not exist yet**.
In its place this session used:

- **An independent re-implementation** (`wk9_s50_verify.py`) that shares no code
  with the evaluator (a separate module with its own routines): forms built and
  evaluated in pure-python integers, the `9×9` determinant by exact Gaussian
  elimination over `Q`, interpolation over `Q` (`fractions.Fraction`), and the
  final remainder by **sympy** `div` over `Q`.  It also builds the full Hessian
  at every node with **no quadratic-in-`t` assumption**, so it cross-checks that
  modelling choice in the evaluator.  It re-derives, exactly over `Q`:
  - control 1 (`det_4`): **remainder `= 0`** (exact division certificate);
  - control 4 (`x_0·per_3`): **remainder `≠ 0`** — an explicit nonzero rational
    polynomial in `t` — on **two** independent planes `B`, `B'`.
- a **`gcd` cross-route** inside the evaluator (`p | g ⇔ deg gcd(p,g) = deg p`)
  agreeing with the `mod` route on every sample;
- **three primes** and **five planes** for the mod-`p` claims;
- the **Katz rank audit** (V3/V4) as a structural check that the Hessian code is
  correct where the answer is known.

The two implementations — flint mod-`p` and sympy exact-`Q` — agree on every
control.  They re-implement the same power-rule Hessian *algorithm* (in separate
code), so a conceptual error in "how to build a Hessian" would survive both; that
residual is covered independently by the **Katz rank audit V3/V4**, which checks
the Hessian against the externally known dual dimensions `2n−2` (`= 6` for
`det_4`, `= 4` for `det_3`).  When `tools/verify/` lands, the recorded remainders,
points `B`, primes and seeds in `results/s50_controls.json` are in a form it can
re-check.

## 7. Honest boundary

- **Proved:** the degree derivation `D = (d−1)(k+2) = 2n(n−1)` from the
  divisibility; the factor-of-two resolution `δ = 24`; `x_0·per_3 ∉ Dual_{6,4,16}`
  (two independent routes) and hence `I(D_det)_24 ≠ I(P_pad)_24` and
  `P_pad ⊄ D_det`.  **Conditional on `V_n = S_{(65,17,2⁷)}`** (the standard
  reading of Thm 1.1.2, not verified here): that the separating equation is the
  weight-`(65,17,2⁷)` module, i.e. `v ∈ I(D)^{[λ]}_24 ∖ I(P)_24`.
- **Measured (exact):** all four control remainders (over `F_p` and, for controls
  1 and 4, over `Q`); the Hessian ranks giving `dim(dual x_0 per_3) = 7`; the
  engine validations V1–V4.
- **Adopted-from-literature:** the LMR construction and Theorem 1.1.2 (weight and
  divisibility); `V_n ⊆ I(Dual)` and the determinant as a component of
  `Dual_{2n−2,n,n²}`.  Control 1 confirms the piece we rely on
  (`v` vanishes at `det_4`).
- **Not computed, and stated as such:** `a(λ,24)`, `N_S`, `n_χ`, `h_pad`,
  `i_det`, `i_pad` — all beyond reach (§2); hence the dimension comparison
  `i_det` vs `i_pad` (§4) is **open**, and the "equal-dimension, different-subspace"
  reading is neither confirmed nor excluded.
- **Scope of the separation.**  The remainder is a faithful proxy for
  membership in `Dual_{6,4,16}`, which `V_n` cuts out set-theoretically; the
  claim is set-theoretic non-membership `x_0·per_3 ∉ D_det`, witnessed by an LMR
  equation.  It is a lower bound on `dc̄(per_3)`, not a new numerical value of it.
- **One implementation assumption, discharged:** the evaluator models
  `H_P(x(t))` as quadratic in `t`, valid because `d ≤ 4` (Hessian entries have
  degree `d−2 ≤ 2`).  The `n=3` validation (`d=3`, linear entries) exercises the
  same code path and passes.

## 8. Pre-registration scorecard (`results/PREREG_s50.md`, committed `a52661d`)

| prediction | prior | outcome |
|---|---|---|
| weight `(65,17,2⁷)`, `δ = 24` (factor of two → 24) | — (pre-derived) | **confirmed** against Thm 1.1.2 and the paper's `n=3` example |
| C1 `det_4` remainder `= 0` (calibration) | 0.90 | **held** — DIVIDES, exact over `Q`, 5 planes, 2 primes |
| C2 generic quartic remainder `≠ 0` | 0.95 | **held** |
| C3 `ℓ·c` remainder `≠ 0` | 0.85 | **held** |
| C4 `x_0·per_3` remainder `≠ 0` ⇒ separation | 0.75 | **held** — NOT_DIVIDES, exact over `Q`, 3 primes, robust to plane |
| P5 `G ≢ 0` for padded (generic rank `≥ 9`) | 0.70 | **held** — generic rank 10, rank 9 on `{per_3=0}` |
| P6 controls 3, 4 agree | 0.75 | **held** — both `≠ 0` |

**Headline positive result achieved:** control 1 `= 0` **and** control 4 `≠ 0`.
No control-1 or control-2 failure (the two failures the brief said to stop and
report); nothing was adjusted.
