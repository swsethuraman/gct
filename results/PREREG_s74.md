# Pre-registration — session 74 (batch 12): the LMR source by births, then the decision

Branch `s74-births` off `main` at `afb8c3319d3d1f3afc3d2578c8cb322f2b8a3b92`
(fresh clone; `docs/batch12_s1_s2_consolidated.md` and
`docs/batch12_worker_preamble.md` present; `tools/verify/selftest.py` 12 cases
PASSED; the working example `wk12_int_birth_probe.py --stream 23,22 --cap 60`
reproduced exactly: 108 / 5, hits `[57]`, 0 control failures, `1/1` at
`δ = 23`, `3/3` at `δ = 22`).  Container only, no pushes; delivery by
single-ref bundle `s74_births.bundle` + `.md5`.  Written and committed
**before any birth is drawn or any rank is read** beyond the first-30-minutes
checks.  Labels: **proved** / **measured** / **adopted** / **expectation**.

Written 2026-09-08 22:40 UTC.

## 1. Object and question

The goal cell: `n = 4`, `r = ℓ(λ) = 9`, `λ = λ₂₄ = (65, 17, 2⁷)`, `δ = 24`,
`a = 274`; the LMR ladder `λ_δ = (4δ − 31, 17, 2⁷)`, `δ = 12 … 24`, conjugate
shape `λ'_δ = (9, 9, 2¹⁵, 1^{4δ−48})`.  `M_δ = HWV_{λ_δ}(Sym^δ Sym⁴ C⁹)`,
`dim M_δ = a_δ`.  For a family `X ∈ {det, pad, red, per4}` of forms in
`Sym⁴ C⁹`,

    T_X : M₂₄ → functions on X,   i_X = dim ker T_X = 274 − rank T_X,
    mult_X = rank T_X,             D = rank T_pad − rank T_det = mult_pad − mult_det.

`D > 0` refutes `P₉ ⊆ D₉` by functoriality (`docs/brief_wording.md` §7, row 1)
and is the programme's obstruction; LMR gives `rank T_det ≤ 273` (adopted).
Also computed on the same rows: `i_red`, `i_per4`, `U_D = ker T_det`,
`U_P = ker T_pad` in source coordinates, `dim(U_D ∩ U_P)`, and the orientation
`U_D ⊄ U_P` / `U_P ⊄ U_D`.

## 2. What is proved, adopted and banked going in

- **Proved (S1, checked by the integrator).**  With `u = c_{(4,0,…,0)}`,
  `ker(M_d → R/(u)) = u·M_{d−1}` and `M_d / u·M_{d−1} ≅ ρ_d(M_d)`, of dimension
  `b_d = a_d − a_{d−1}`.  Multiplication by `u` is injective (domain).
- **Proved (integrator, consolidated §1).**  For a prime ideal `I ∌ u`
  (`I(Det₄)`, `I(ℓ·per₃)`): `(I ∩ M_d) ∩ uM_{d−1} = u(I ∩ M_{d−1})`, hence
  `rank T_det|_{uM₂₃} = 273 − i_det(23)`.
- **Proved (s69, Identity 1–3).**  A filling `T` of `λ'` defines a
  highest-weight vector `F_T ∈ M_δ`; `(u·F)(f) = F(f) · 4! · f_{s₁⁴}`; the
  DP evaluator computes `F_T(f)` exactly mod `p`.
- **Adopted.**  The `a`-ladder `2, 39, 93, 145, 188, 219, 241, 255, 264, 269,
  272, 273, 274` (`δ = 12 … 24`; s57/s63, two independent engines), so the birth
  profile `b_δ = 2, 37, 54, 52, 43, 31, 22, 14, 9, 5, 3, 1, 1` (sum 274).
  `N_S(λ₂₄) = 156 438 903 314`, `N_S(λ₂₃) = 156 419 279 221` (`lmr_cell.md` §6).
- **Certified (integrator, both primes).**  `M₂₄ = uM₂₃ ⊕ ⟨F₅₇⟩`
  (`results/wk12_int_lmr_birth24.json`).
- **Measured (integrator, single prime `P1`, seeds recorded).**  Birth ranks
  complete at `δ = 20, 21, 22, 23` (`results/wk12_int_birth_probe.json`;
  stream seed `500 + δ`, `u = 0` points from `random.Random(61000 + 11j)`).
- **Measured-by-S1 (not verified).**  Ten evaluation-ready vectors
  (`results/astra/S1/partial_source_10.json`): the two `δ = 12` seeds and eight
  `δ = 13` birth classes.
- **Banked (s69).**  The `δ = 12` seeds (`results/s69_n4_seed.json`, `a₁₂ = 2`,
  generic rank 2, det rank 2, `i_det(12) = 0` both primes).

## 3. Instrument

Bracket-monomial circuits (`analysis/wk11_s69_circuit.py`, DP evaluator
`wk11_s69_dp.c`), python-flint `nmod_mat` for every rank and nullspace, house
primes `P1 = 2147483647`, `P2 = 2147483629` (both `> |λ₂₄| = 96`).  The letter
`u` is resolved as `exps(4, 9).index((4,0,…,0))` in the `wk8_s30_core`
ordering (index 494, the last), never by a literal.  Code under
`analysis/wk12_s74_*.py`; state under `results/s74/`; logs under
`results/logs/`.

### 3a. Births (rungs 13 … 23)

For each rung `d`, in the order 20, 21, 22, 23 (reproduction), then 13, 14, 15,
16, 17, 18, 19 (discovery):

1. Draw random column-strict fillings of `λ'_d` with `random_filling(9, 4, d,
   15, n1, rng, k ∈ {5,…,9})`, `rng = random.Random(500 + d)` (the probe's
   rule, so the first draws coincide with the integrator's stream at every rung
   the probe touched).
2. Reject syntactically any filling with a pure-`u` letter (a letter whose four
   legs all sit in one-columns): `F_T = 4!·u·F_deleted` is an identity, so its
   class is zero.
3. Evaluate the survivors at `K_d = b_d + 8` generic points with `u = 0`
   (`generic_point` mod `P1` from `random.Random(61000 + 11j)`, then
   `cv[494] = 0`).  Keep a filling iff it raises the rank of the kept rows.
   Stop at rank `b_d`.
4. **Certificate at the rung**: the `b_d × K_d` matrix at `P1` has rank `b_d`;
   a nonzero `b_d × b_d` minor (column set and its determinant mod `P1`) is
   recorded.  Then the same `b_d` fillings are evaluated at `K_d` fresh
   `u = 0` points mod `P2` (`random.Random(62000 + 11j)`) and must again have
   rank `b_d`.  Since the restricted polynomials have integer coefficients and
   the points are integer points, rank `b_d` at one prime proves the `b_d`
   classes are `Q`-independent in `ρ_d(M_d)`, hence (dimension `b_d`) a basis
   of the birth quotient.  This is a certificate, not sampling.
5. Budget per rung: 4 000 draws or 3 600 s wall, whichever first; per-rung
   state is checkpointed and committed as the rung completes.  A rung that
   does not fill is reported (rung, draws, filter survivors, hit rate) and the
   stream is **not** enlarged automatically.

The two `δ = 12` seeds are the s69 seeds (re-evaluated here: generic rank 2 at
both primes on my points).  Rung 24 is `F₅₇`, re-derived here at both primes
on my own `u = 0` points.  S1's ten vectors are replayed through this
instrument (their eight `δ = 13` classes must have rank 8 at my `δ = 13` points
at both primes; if they do they are admitted as the first eight rung-13
candidates, otherwise reported as a defect in a session deliverable and not
used).

### 3b. The declared row system (assembly)

The source at `D = 24` is the list of `274` **literal transported fillings**
`T_i^↑`: the native filling `T_i` (birth rung `d_i`) plus `24 − d_i` new
letters each occupying four one-columns (`climb_to_top`).  Its value at a form
`f` is, by the proved identity,

    row_i(f) = F_{T_i^↑}(f) = F_{T_i}(f) · (4! · f_{s₁⁴})^{24 − d_i}
             = F_{T_i}(f) · msym_u(f)^{24 − d_i},

and this one formula is used for every column (generic, det, pad, red, per4) at
both primes.  The `δ = 23` source is the same list without `F₅₇`, with exponent
`23 − d_i`.  Check of the row system: for at least 24 rows spanning all rungs
and 3 points, the DP evaluation of the literal climbed filling `T_i^↑` must
equal the scaled native value at both primes.  Kernel vectors (`U_D`, `U_P`)
are reported as coefficient vectors on this list, i.e. on the literal
fillings; S1's "`u`-normalised" convention differs by the constant
`(4!)^{24 − d_i}` per row and is recorded in the manifest for conversion.

### 3c. Points (all integer substitution data, `K = a + 8 = 282` per family)

| family | construction | seed rule |
|---|---|---|
| `det_pencil` | `det₄(Σ s_i A_i)`, `A_i ∈ Z^{4×4}`, entries in `[−30, 30]` | `random.Random(20260974 + j)`, `j = 0 … 281` |
| `padded_permanent` | `restrict(PAD34)` = `x₀(s)·per₃(X(s))`, frame `V ∈ Z^{9×10}` in `[−30, 30]` | `random.Random(20261974 + j)` |
| `reducible` | `l(s)·c(s)`, `l ∈ Z⁹`, `c` a generic integer cubic (165 coefficients) in `[−30, 30]` | `random.Random(20262974 + j)` |
| `permanent_pencil` | `per₄(Σ s_i A_i)`, `A_i ∈ Z^{4×4}` in `[−30, 30]` | `random.Random(20263974 + j)` |
| generic (rank check only) | uniform coefficient vector mod `p` | `random.Random(20264974 + j)` |

A point with `msym_u = 0 mod p` is skipped and the next index drawn (recorded).
Every point is written to the certificate as substitution data.  The `δ = 23`
determinant column uses the first `281` det points (`a₂₃ + 8`).

### 3d. What each rank proves

`rank_p ≤ rank_Q ≤ a`.  Rank `274` at one prime proves `i_X = 0` over `Q`.
Rank `273` on the det column at one prime proves `rank_Q T_det ≥ 273`, and with
LMR (`≤ 273`, adopted) `i_det = 1` exactly.  A rank *below* the bound at one
prime is a lower bound on `mult` and an upper bound `i_X ≤ 274 − rank_p`, never
a characteristic-zero ideal.  The second prime is the protocol's re-derivation,
never a promotion.

## 4. Decision table (the preamble's, verbatim)

| observed | consequence | action |
|---|---|---|
| det 273, pad 274 | `i_det = 1`, `i_pad = 0`, `D = +1` | the verification protocol takes over before it is reported anywhere |
| det 273, pad 273 | `D = 0` | compare kernel orientation in common coordinates; no multiplicity obstruction in this cell |
| pad < det | `D < 0` | an exact negative result; retain the orientation information |
| det < 273 | `i_det ≥ 2` | a structural surprise; resolve the full determinant kernel dimension before interpreting the padded side |
| span < 274 but det rank 273 on the span reached | `i_det = 1` exactly | the determinant column is finished, not stalled; report it as a completed half |
| partial source, no full-rank half | rank lower bounds only | do not infer nullity from a sampling shortfall; preserve certified lower bounds and the missing directions |

Order of measurement: (i) banked rungs reproduced at both primes; (ii) the
`δ = 23` determinant column (`i_det(23)`); (iii) the middle rungs; (iv)
assembly and generic rank; (v) pad, red, per4 columns at `P1`; (vi) everything
at `P2`.

## 5. Falsifiers and stopping rules

- **F1 (defect in what I was handed).**  Any of `δ = 20, 21, 22, 23` fails to
  reproduce rank `b_d` at either prime, or `F₅₇` vanishes mod `u` at either
  prime, or the s69 seeds have generic rank `< 2`.  Action: stop and report.
- **F2 (a rung does not fill).**  Birth rank `< b_d` after the budget.  Action:
  report the rung, draws, filter survivors and hit rate; assemble and evaluate
  on the span reached; all four columns become lower bounds on `mult` and
  the table's last two rows apply.  No automatic enlargement.
- **F3 (assembly defect).**  All rungs filled but the assembled generic rank
  `< 274`, or the row-system identity check fails.  Action: no `i_X` is
  reported; the rank curve and the failing rows are.
- **F4 (S1 replay).**  Fewer than 8 of S1's eight `δ = 13` classes are
  independent on my points at both primes.  Action: reported as a defect in a
  session deliverable; my own rung-13 stream proceeds regardless.
- **Any `D > 0`** (`rank T_pad > rank T_det`): the verification protocol —
  second prime on every rank; two independent evaluation families per side
  (fresh seeds `+ 100 000`, box `1000`, `K = a + 20`); characteristic zero
  where a kernel is claimed (the det kernel line rationally reconstructed on
  the 274-vector source coordinates, checked at `P2`, vanishing at fresh det
  pencils and nonvanishing at fresh pad points); an independent source (a
  second, independently drawn birth basis — new stream seeds `1500 + d` and
  new `u = 0` point seeds — at every rung, with the pad and det ranks
  re-derived on it); and the degeneracy pre-check of `brief_wording.md`
  §5/§7 (the statistic is the coordinate-ring multiplicity, functorial in the
  right direction; the evaluation family for the padded side is the true
  ten-variable `ℓ·per₃`, not `ℓ·c`).  Not reported anywhere before that
  completes; the s73 §6 template is followed.
- **Cost.**  Evaluation is `≈ 0.1 s` per (filling, point) on this box (measured
  at rungs 12 … 24 before pre-registration); one column of `274 × 282` is
  `≈ 2.2 CPU-hours`, five columns at one prime `≈ 11 CPU-hours` (2 cores).
  Runs are bounded with `timeout`, `ulimit -v`, and a `.pid` under
  `results/logs/`; state is checkpointed per row block.

## 6. Expectations (labelled, not load-bearing)

- `i_det(23) = 0`, i.e. det rank `273` on the transported `δ = 23` source:
  **expectation**, `P ≈ 0.8` (no `n = 4` cell has ever shown `i_det > 0` except
  by the LMR theorem, and the predecessor argument of s63 assumes it).
- `rank T_pad`: **no prior worth stating**.  The programme's 419 measured cells
  are all `D ≤ 0`, but this is the first cell where `i_det ≥ 1` is forced, so
  `D = +1` iff `i_pad = 0`; `h_pad(24) = 521 > 274` makes the pad ceiling
  vacuous (integrator note 1, batch 10), so the rank is genuinely required.
- Middle rungs fill within budget: **expectation**, `P ≈ 0.85` (the probe's
  `14/54` from 15 draws at `δ = 14` and `17/31` from 39 at `δ = 17` show a
  high early hit rate; the tail is the risk).
- `i_red ≤ i_pad` always (`P₉ ⊆ R₉`, proved), `mult_pad ≤ mult_red`; recorded
  as a consistency check on the columns.

## 7. Deliverables

`results/PREREG_s74.md` (this file); `results/s74/births_d{13..23}.json`
(fillings, points, matrices, minors, both primes); `results/s74/source.json`
(the 274 literal fillings, birth rungs, row-system declaration, scalars);
`results/s74/columns_{family}_{prime}.json` (native values, points);
`results/s74/decision.json`; `results/certs/s74_*.json` (`sparse_nullity`,
session-67 spelling); `analysis/wk12_s74_verify.py` (independent re-derivation
from the certificates at fresh points); `docs/s74_report.md`;
`s74_births.bundle` + `.md5`.

## 8. Commit trailer

The preamble asks for `Co-Authored-By: Claude Opus 5`.  The model running this
session is not Opus 5; commits carry the truthful `Co-Authored-By: Claude
Fable 5.1 <noreply@anthropic.com>` and no session-link trailer, as the
standing rule requires.  Noted here so the deviation is deliberate and visible.
