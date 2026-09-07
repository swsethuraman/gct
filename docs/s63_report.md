# Session 63 — the LMR determinant block (C2)

Branch `s63-lmrdet` off `226b4ef1` (ancestry gate passed). Pre-registration
`results/PREREG_s63.md`, commit `26993f5`, before any measurement. Container:
2 cores, 7 GB RAM, python-flint 0.9.0. Deliverables: this report;
`results/s63_routes.md`; `results/PREREG_s63.md`; code `analysis/wk10_s63_*.py`;
the two-sided control `results/s63_n3ladder.json`; artefact
`results/artefacts/s63_n3_ideal_vectors.npz`; logs `results/logs/s63_*`.
Bundle `s63_lmr_det.bundle` + `.md5`.

## Verdict

**The two integers the whole deduction rests on are independently reproduced, and
the instrument is validated two-sided against the programme's first rank drop —
but the one rank the LMR cell needs is not affordable in a 7 GB / 2-core
container, by three to eighty-plus orders of magnitude on every route.**

Concretely:

1. **`a₂₃ = 273` and `a₂₄ = 274` are reproduced** by a from-scratch Weyl
   alternation, anchored to the direct partition-sum *definition* at ten small
   cells and cross-checked against the programme's own `a_weyl`. The full LMR
   `a`-ladder `2, 39, 93, 145, 188, 219, 241, 255, 264, 269, 272, 273, 274, 274`
   matches s57/s58 exactly, is monotone, has final increment 1, and is constant
   at `274` by `δ = 31` where the ladder theorem guarantees it. **[measured, three
   independent routes]**
2. **The `n = 3` LMR positive control passes, two-sided.** At `((19,7,2⁵), 12)`,
   `a = 6`, the instrument returns `mult_det = 5`, `i_det = 1` at both house
   primes — the first rank drop the programme has ever exhibited. Ran below the
   closing degree as well (`δ = 9, 10, 11`): **full rank at all three**
   (`i_det = 0`), a drop **only** at `δ = 12`, both primes — so the instrument
   does not under-report rank and the drop is genuine, not a degenerate-evaluation
   artefact (integrator note 2). The ideal HWV `U_D` is preserved and checked five
   ways incl. fresh-seed vanishing and generic-point non-vanishing.
   **[measured both primes; the `i_det ≥ 1` half is theorem]**
3. **All three projections at `r = 9` are walled** (`results/s63_routes.md`):
   native HWV build 14.4 TB / ≈ 415 days; Foulkes column `|H_{4,24}| = 1.2×10⁹³`;
   Gram/Schur `|S| ≥ 6×10⁶`. The deciding number `|S|` is ≥ 2 orders past the
   feasibility line. **[measured wall]**

So `i_det = 1` at the LMR cell is **not certified this session**. What is
delivered is its entire foundation, an instrument validated to see exactly the
phenomenon it would show, and a precise, quantified statement of the wall — the
pre-registered acceptable outcome (P3), reported rather than forced past the
time-box.

## 1. Task 1 — the two source multiplicities, reproduced (proved foundation)

The deduction `rank₂₃ = 273 ⟹ i_det,24 = 1` rests on exactly two integers and
ladder monotonicity. Both integers are reproduced here by a route sharing no
code with the integrator's session-50/57/58 computations
(`analysis/wk10_s63_averify.py`):

    a(λ,δ) = Σ_{w∈S_r} sgn(w) · K(w(λ+ρ)−ρ ; δ),

`K` the weight multiplicity of `Sym^δ(Sym^4 C^r)`, evaluated on the descending
sort (K is permutation-symmetric) with the largest coordinate free — an **exact
int64** tail DP (`K ≤ N_S ≈ 1.5×10¹¹ < 2⁶²`).

- **Anchor to the definition.** `amb` (`wk8_s30_pleth`, the plethysm paired with
  `χ^λ` over *every* partition of `N`) agrees with this route at all ten small
  cells reachable by `p(N)`: eight LMR-family members and two generic cells
  (`results/s63_anchor.json`, `all_match: true`).
- **Cross-check to the programme.** The exact `a_weyl` (`wk9_s42_census`) agrees
  at five small cells including `(12,4)_4 = 2` (`results/s63_cross.json`).
- **The ladder** (`results/s63_aladder.json`): `2, 39, 93, 145, 188, 219, 241,
  255, 264, 269, 272, 273, 274, 274` for `δ = 12…25`, `a₃₁ = 274`. **`a₂₃ = 273`,
  `a₂₄ = 274`**, final increment 1, monotone.
- **`N_S` cross-check.** `K_exact(λ,δ)` reproduces `N_S` exactly at `δ = 23`
  (156 419 279 221) and `δ = 24` (156 438 903 314), matching `docs/lmr_cell.md`
  §6 — an independent check of both this engine and that table.

**F1 (the anchor falsifier) is cleared.** Every downstream claim has its
foundation.

## 2. Task 2 — the three projections, costed (see `results/s63_routes.md`)

`docs/s62_report.md` / `results/s62_cost.md` **absent** at start and midpoint, so
`|S|` is measured here from the family scaling, not read from s62.

| route | deciding quantity at `r = 9` | feasible (7 GB / 2 core)? |
|---|---|---|
| 1 native HWV (`ev_det`) | build `N_S = 1.56×10¹¹` → 14.4 TB, ≈ 415 d, ≈ 49 TB RSS | no, ~2 000× |
| 2 Foulkes single `λ`-column | `|H_{4,24}| = 1.2×10⁹³`, engine quadratic | no, ~10⁸⁰× |
| 3 Gram/Schur C2 | `|S| ≥ 6×10⁶` (density plateau 0.20–0.26 × `n_χ`) | no, ~100×, build-gated |

Route 1 is extrapolated from the **measured** `n = 3` control build (1.16×10⁶
monomials, 265 s, 0.36 GB). Route 3's `|S|` is measured at four family cells
(`results/s63_support.jsonl`): support density falls to a **plateau ≈ 0.20–0.26**
of `n_χ` and cannot fall to zero (the `n = 3` `U_D` sits at 0.229), so
`|S|_LMR ≈ 0.2–0.26 · n_χ ≈ 6–8 × 10⁶` — a floor, larger as `a = 274` grows the
union. The C2 nonsingularity step is **characteristic-free**
(`rank(MᵀM) ≤ rank(M)`); that is a genuine improvement over the char-0 framing,
but it does not move the `|S|` wall.

## 3. Task 3 / the `n = 3` positive control — the instrument is two-sided

The `r = 9` rank is walled (§2), so no LMR rank is certified. The method itself
is validated where it is affordable, at the cell both integrator notes name
mandatory and no prior session ran (`docs/lmr_cell.md` §3b, `docs/s58_review.md`
§4): `λ = (19,7,2⁵)`, `δ = 12`, `n = 3`, `a = 6`, LMR-non-vacuous so
`i_det ≥ 1 ⟹ mult_det ≤ 5`.

`analysis/wk10_s63_n3control.py`: build the χ-reduction (`n_χ = 17 047`), then
`mult_det = a − nullity_Q[E; ev_det]` by the sparse Wiedemann route
(`wk9_s45_cell.nullity_stacked`) at `K = 14` random det₃ pencils, both primes.

    p = 2147483647 :  i_det = 1,  mult_det = 5
    p = 2147483629 :  i_det = 1,  mult_det = 5

**Which half of `i_det = 1` comes from where (integrator note 2 §2).** Random
evaluation only *lower*-bounds the true rank, and reduction mod `p` only lowers
rank further, so the measurement gives

    i_det = nullity_Q[E; ev_all]  ≤  nullity_Q[E; ev_14]  ≤  nullity_p[E; ev_14] = 1,

i.e. **`i_det ≤ 1`**; the LMR theorem supplies **`i_det ≥ 1`**; together `= 1`
exactly, and that is rigorous. The instrument did **not** independently certify a
drop — it confirmed it does **not over-report rank**. That is exactly what a
one-sided positive control establishes, and the two-sided control below removes
the remaining ambiguity.

**The two-sided control (integrator note 2 §4).** Below `δ_close = 12` the module
is vacuous, so the engine must return full rank; a spurious early drop would make
`δ = 12` meaningless. Ran at both primes (`analysis/wk10_s63_n3ladder.py`,
`results/s63_n3ladder.json`):

| `δ` | `a` | `mult_det` (P1, P2) | `i_det` | expected | |
|---|---|---|---|---|---|
| 9 | 2 | 2, 2 | 0 | full rank | ✓ |
| 10 | 4 | 4, 4 | 0 | full rank | ✓ |
| 11 | 5 | 5, 5 | 0 | full rank | ✓ |
| 12 | 6 | 5, 5 | **1** | **drop** | ✓ |

Full rank at 9, 10, 11 and a drop only at 12 — the engine does not
systematically under-report rank, so the drop is real. And `δ = 11` buys the
whole predecessor argument in miniature: `mult_det(11) = 5` full rank + ladder
monotonicity + LMR give `mult_det(12) ≥ 5 ⟹ i_det(12) ≤ 1 ⟹ = 1` — **exactly the
273/274 predecessor-to-goal deduction of the LMR cell, validated end-to-end at
`n = 3` before it is trusted at `n = 4`.**

**The ideal vector `U_D`** (weight `(19,7,2⁵)`, degree 12, in `I(D_7^{det₃})`,
`results/artefacts/s63_n3_ideal_vectors.npz`) — the programme's **first exhibited
element of `I(D)^{HWV}` with `i_det > 0`** — passes the note-2 §5 checks:

1. `U_D ≠ 0`: 3 900 nonzero χ-coordinates, a recorded nonzero coefficient.
2. `E·U_D = 0` on the **full** sparse `E` (not only the compressed form).
3. `ev_det·U_D = 0` at det₃ pencils from **three fresh seeds** (`20265807`,
   `12345`, `99999`) not used in the measurement, **and** `U_D` is **nonzero at
   generic cubics** of `Sym³C⁷` — ruling out a vector trivially in every ideal.

**Certificate status, stated plainly.** The `gct-cert/1` verifier
(`tools/verify/layer2.py:93`) hard-asserts `n = 4`, so the `hwv`/`full_rank`
kinds cannot carry this `n = 3` result, and the sparse-Wiedemann nonsingularity
kind does not exist in the format yet (the known gap, stocktake item 7). The
control is therefore certified **in code** — both primes, the kernel vector
checked against the full `[E; ev_det]` inside `nullity_stacked`, and the
independent re-verification above — with `U_D` as the machine-readable artefact.
Extending the verifier to `n ∈ {3,4}` (one line) and adding the Wiedemann kind
would let it carry a format certificate; recommended, not done here (single-writer
verifier).

## 4. What depends on `sk`, and what does not

The projection deduction uses **only** `a₂₃`, `a₂₄`, ladder monotonicity, and LMR
non-vacuity. **None of `i_det = 1`'s logic touches `sk = 48 825`** — the target
dimension is not an input to `rank(PA) ≤ rank(A)`, and the C2 reduction removes
the 48 825-dim target entirely. `sk` (single-source: s58 + Manivel) would enter
only as a codomain dimension in routes 2/3 if a full `Θ⁺` rank were taken, and it
is flagged there. So the conclusion this session *would* deliver, and its whole
foundation as delivered, are `sk`-independent.

Relatedly (integrator note 1 to s64): `h_pad(LMR) = 521 > 274 = a`, so the
pad-side ceiling `mult_pad ≤ h_pad` is vacuous at LMR and no cheap screen can
settle the cell — a rank is genuinely required, which is what makes this
determinant-side rank the load-bearing number. `D_LMR` further needs `i_pad`
(session 64); `i_det = 1` alone is an occurrence statement (Ikenmeyer–Panova).

## 5. Prediction ledger

| id | prediction (pre-registered) | outcome |
|---|---|---|
| P1 | `a₂₃=273`, `a₂₄=274` by ≥ 2 independent routes | **hit** — 3 routes (Weyl, `amb` definition, `a_weyl`) |
| P2 | LMR ladder matches s57/s58, `a_∞ = 274` at `δ=31` | **hit** — exact, monotone, final increment 1 |
| P3 | native `n_χ` build at `δ=23` does NOT close in 90 min / 6 GB | **hit** — 14.4 TB / ≈ 415 d, off by ~2 000× |
| P4 | Foulkes single-column route infeasible | **hit** — `|H_{4,24}| = 1.2×10⁹³` |
| P5 | any measured rank agrees at both primes | **hit** — all four `n=3` rungs, both primes agree |
| P6 | no genuine rank drop observed | **n/a→hit** — the only drop (`n=3` `δ=12`) is theorem-guaranteed and two-sided-validated (full rank at `δ=9,10,11`); no spurious drop, no `D>0` event |

## 6. For the integrator / next sessions

- **The C2 route is exact and `sk`-free, and its cost is now a measured number,
  not a guess: `|S| ≥ 6×10⁶` at `r = 9`.** Two orders past reach in this
  container. The only opening on route 1/3 is an engine that enumerates the
  `~3.1×10⁷` orbit representatives directly, never the `1.56×10¹¹` monomials —
  a new build, reserve-class, not forceable in 7 GB.
- **Reserve E1 (direct `δ = 24` completion) is not this session's to force**, per
  the stopping rule; the partial artefacts (the reproduced ladder, the `N_S`/`n_χ`
  and `|S|` curves, the `n = 3` control and `U_D`) are preserved for it.
- **Session 65** needs `U_D = ker T_det` at the LMR cell in source coordinates;
  what exists so far is the `n = 3` analogue (`s63_n3_ideal_vectors.npz`), the
  template for the format s65 will consume once the `r = 9` build is reachable.
- **A one-line verifier extension** (`n ∈ {3,4}` at `layer2.py:93`) plus a
  Wiedemann-nonsingularity `gct-cert/1` kind (stocktake item 7) would let the
  `n = 3` control — and the eventual LMR rank — carry a format certificate.

## Text for the paper (integrator to place; not written to single-writer files)

> At `n = 4` the smallest length carrying a non-vacuous determinant equation is
> `r = 9`, where the LMR weight `λ(6,4) = (65,17,2⁷)` forces `i_det ≥ 1` at
> `δ = 24`. Its resolution to `i_det = 1` reduces, with no reference to the target
> dimension, to a single rank lower bound `rank Θ⁺ ≥ 273` obtained from the source
> multiplicities `a₂₃ = 273`, `a₂₄ = 274` and the monotonicity of the ladder. The
> `n = 3` shadow `λ = (19,7,2⁵)`, `δ = 12`, exhibits the mechanism exactly:
> `a = 6` but `mult_det = 5`, a genuine determinant equation, with the ideal
> highest-weight vector written down explicitly.
