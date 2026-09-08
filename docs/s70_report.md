# Session 70 (C3) — the two ranks at LMR, and which of them needs a source

Branch `s70-tworanks` off `main` at `226b4ef1` (ancestry gate
`git merge-base --is-ancestor 226b4ef1 HEAD` passes). Pre-registration
`results/PREREG_s70.md` committed at `f3b8eda`, before any rank was computed.
Construction `docs/s_split.md`; ranks `results/s70_ranks.md` + `.jsonl`;
certificates `results/certs/s70/`; code `analysis/wk11_s70_split.py`; bundle
`s70_tworanks.bundle` + `.md5`. Container: 2 cores, 7 GB. Nothing pushed;
single-writer files untouched. Labels: **proved** / **measured** / **adopted**.

## 0. The determination (Part A), first

**`rank S_{λ,24}` is source-dependent — it needs the explicit `a = 274`
quartic source exactly as `det A₂₄` needs the `273`-dimensional predecessor
image, so both LMR numbers are gated on the same `r = 9, δ = 24` source that
session 63 measured walled on all three realisations.** The reducible-normalisation
split `S = S_{λ,δ} : M⁴_λ → ⊕_μ M³_μ` (the comultiplication `Sym⁴V → V⊗Sym³V`
restricted to the `λ`-highest-weight space, `rank S = mult_red`) has a
**source-free target** — the 48 Pieri/cubic blocks `⊕_μ M³_μ` of dimension
`h_pad = 521`, from the session-42 identity — and a source-free map, but its
**columns are a basis of `M⁴_λ = HWV_λ(Sym^δ Sym⁴V)`, the `a = 274` quartic
source, for which no basis exists that is not explicit highest-weight vectors.**
The brief's ungating conditional ("columns indexed by the ambient multiplicity
rather than by explicit source vectors") therefore fails at its antecedent. Three
independent grounds, in `docs/s_split.md` §5: (i) no combinatorial model of the
`a`-dimensional multiplicity space `M⁴_λ` carries the `μ*` action — any handle on
one of its vectors is an explicit quartic HWV; (ii) a source-free *matrix* would
make `mult_red` a closed form of `λ,δ`, contradicting s42 §B (the
normalisation-quotient multiplicity is supported on the non-normal locus and
"computing it is exactly the original problem") and s60's eight measured
`mult_red < min(a,h_pad)` cells with no combinatorial law; (iii) s64 §7 states
the factorized route's fast branch "is gated on the same wall (building /
evaluating the common source at `r=9, δ=24`)" — the 48-block advantage is on the
target, not the source. Since no source lands and the LMR carrier build is
forbidden, the ungated deliverable is the construction, written out for the first
time, plus its `n=4` calibration; the LMR rank is reusable the moment a streaming
orbit-rep source engine reaches the cell (session 63's reserve-class opening).

## 1. What was asked, and what a session can deliver here

Batch 11 is partially gated. `rank S` was to be run first — the cheaper number,
the one that can settle the cell alone — and its outcome decides whether
`det A₂₄` is worth the night. Part A determines that both numbers sit behind the
same `r = 9, δ = 24` source wall (`N_S = 1.56·10¹¹`; Foulkes `1.2·10⁹³`;
Gram/Schur `|S| ≥ 6·10⁶`, `docs/lmr_cell.md` §6, `results/s63_routes.md`). So the
session's product is the **ungated fallback the brief marks required, not
optional**: the determination in writing, the `S` construction written out
(nobody had), and its exact ranks at two banked, discriminating `n=4` cells that
calibrate `S` against banked truth rather than against a tautology.

## 2. `rank S`, calibrated *(measured, exact, both primes)*

`S` and `rank S = mult_red` are derived and written out in `docs/s_split.md`
(the map `μ*(c_α) = Σ_{i:α_i≥1} y_i⊗d_{α−e_i}`; `rank S = mult_λ C[R_r]_δ` by
Schur). Implemented in `analysis/wk11_s70_split.py` and run at three cells
(`results/s70_ranks.md`):

| λ | δ | a | h_pad | **rank S** | i_red | banked mult_red | (★) route | role |
|---|---|---|---|---|---|---|---|---|
| (10,6,4,2,2) | 6 | 6 | 24 | **6** | 0 | 6 (s42 anchor) | 6 | full-rank control |
| (8,4,4,4,4) | 6 | 2 | 1 | **1** | 1 | 1 | 1 | discriminating (bite) |
| (12,9,9,1,1) | 8 | 7 | 6 | **5** | 2 | 5 | 5 | discriminating (bite) |

Both calibration cells are strictly below `a` — the LMR regime. `rank S = 1` and
`5` reproduce the banked `mult_red` exactly; a construction returning `a` (`2` or
`7`) would be wrong and neither does. The control `(10,6,4,2,2)₆` returns
`rank S = a = 6`: the instrument does **not** drop rank spuriously. Every number
agrees across **both house primes, two independent codomain hash seeds, the
`(★)/E_red` route on the same HWVs, and the session-60/64 banked record**. All
three PREREG falsifiers (F-B1 `rank S ≠ banked`; F-B2 prime/seed disagreement;
F-B3 `(★)` disagreement) are unfired.

This also checks, at the `S` stage, the composite identity session 64 §7 flagged
"unchecked and unbanked": `rank S = mult_red` holds at all three cells, so
`⊕Θ ∘ S` is being composed on a validated `S`.

## 3. `rank S` at LMR — the semantics, for when the source is reached

Not computed (gated, §0). The outcome semantics are **not symmetric** and are
fixed so a future run cannot mis-report them (PREREG §0):

* **`rank S < 274`.** Then `mult_pad ≤ mult_red = rank S < 274`, so `i_pad ≥ 1`;
  with `i_det = 1` (LMR + s63 predecessor), `D = i_det − i_pad ≤ 0`. **The LMR
  cell is settled against a `D > 0` by the `274 × 521` reducible rank alone**,
  before any permanent-specific block — the strongest cheap outcome in the batch,
  and a full result. If this is ever obtained, stop: `det A₂₄` no longer changes
  the verdict.
* **`rank S = 274`.** Then `i_red = 0` only. This does **not** establish padded
  full rank: `S` is the universal reducible-normalisation stage; the
  permanent-specific cubic stage `⊕Θ^{per₃}` can still drop rank
  (`mult_pad = rank[(⊕Θ)∘S] ≤ rank S`). `i_pad` stays unknown; session 73 must
  determine it. Do **not** write that padded full rank is established.

## 4. `det A₂₄` (Part C) — definition and semantics, also gated

Not computed (gated on the same source; `A₂₄` needs the explicit predecessor
image `J(M₂₃)`). Recorded verbatim so it composes with session 68's terminal
rung. `A₂₄ = B|_{J(M₂₃)}` is the degree-24 Gram restricted to the **transported
predecessor** `J(M₂₃)` — the corrected denominator, *not* the predecessor's own
Gram — a `273 × 273` determinant; with `G₂₄ = [[A₂₄, b],[bᵀ, c]]`,
`s = c − bᵀA₂₄⁻¹b = det G₂₄ / det A₂₄`, and `s = 0 ⟺ i_det(24) ≥ 1`. The
`a`-ladder ends `…,272,273,274` (final increments exactly 1), so `δ = 23, 24` are
room-one rungs. Outcomes:

* `det A₂₄ ≠ 0 ⟹ i_det = 1` outright.
* `det A₂₄ = 0` is the **stronger** outcome, not a failure: `mult_det(23) < 273`,
  i.e. `i_det(23) ≥ 1` — a determinant equation at `ℓ = 9`, degree 23, strictly
  stronger than LMR (s57's sharpest "nothing below 24" test).

The nonsingularity step is **characteristic-free**: `rank(MᵀM) ≤ rank M` in every
characteristic, so `det A₂₄ ≢ 0 mod p ⟹ rank ≥ 273 over Z`, both house primes;
`rank(Θ*Θ) = rank Θ` is char-0 only and is not used.

## 5. Honest boundary

* **Proved:** `rank S = mult_red` (Schur, §3 of `docs/s_split.md`); the target
  decomposition `⊕_μ M³_μ` and `dim = h_pad` (session-42 identity); the Part A
  source-dependence determination (§5 of `docs/s_split.md`), resting on s42 §B,
  s60's measured bites, and s64 §7; the characteristic-freeness of the `det A₂₄`
  nonsingularity step.
* **Measured, exact, both primes (+ two hash seeds + `(★)` route + banked):**
  `rank S = 6, 1, 5` at the three `n=4` cells; `nullity(E) = a_weyl`; every HWV
  verified `E·v = 0` on the full sparse `E`.
* **Not computed (gated):** `rank S` at LMR and `det A₂₄` at LMR — both behind
  the `r = 9, δ = 24` source wall (s63); the carrier build is forbidden (S5) and
  was not attempted; the LMR carrier-space engine s63 measured dead was not
  attempted.
* **Adopted:** `a = 274`, `h_pad = 521`, `i_det = 1`, `mult_det = 273` and the
  ladder from `docs/lmr_cell.md`, `docs/s64_report.md`, session 63; the
  `P_r = R_r` ⟹ `mult_pad = mult_red` (`r ≤ 5`) split.
* **Certificates:** `results/certs/s70/*_split.json` record each `rank S` with
  its four-way cross-check; the exact-rank claims rest on `python-flint`
  `nmod_mat.rank()` at two primes, reproducible from the seeds in the code.
  `gct-cert/1` has no kind for a split-rank claim (as for the sparse-nullity
  claims, a registered gap); the `split_rank` records are reproducible, not
  independently verifier-checked.
* **Engineering:** the `μ*` expansion (30–36 M terms) peaks at ~4.3 GB with the
  dense HWV kernel; the binding cost is the shared kernel of `E` (30–166 s/prime),
  not the split. No prime, seed, or route ever disagreed.

## 6. Scorecard (`results/PREREG_s70.md`)

| id | prediction | prior | outcome |
|---|---|---|---|
| P1 | `rank S = 1` at (8,4,4,4,4)₆ | 0.90 | **confirmed** |
| P2 | `rank S = 5` at (12,9,9,1,1)₈ | 0.90 | **confirmed** |
| P3 | both primes + both hash seeds agree | 0.97 | **confirmed** (12/12 numbers) |
| P4 | `(★)` route agrees at both cells | 0.95 | **confirmed** (+ the control) |
| P5 | Part A resolves source-**dependent** | 0.85 | **confirmed**, three grounds |

Unregistered addition: the full-rank control `(10,6,4,2,2)₆` (`rank S = a = 6`),
making the calibration two-sided.

## 7. For the integrator / downstream

* `S` is now written down and validated; `rank S = mult_red` holds at every
  calibration cell, so session 64 §7's `S` stage is banked and `⊕Θ ∘ S` composes
  on a checked `S`. The `Θ^{per₃}` stage (`rank S → mult_pad`) and the LMR run
  remain gated on the quartic source.
* The two LMR numbers are **not asymmetric in cost** but they **are asymmetric in
  what they settle**: `rank S < 274` settles `D ≤ 0` alone; `rank S = 274` leaves
  `i_pad` (hence `D`) to session 73; `det A₂₄` settles `i_det` only. §3–4 hold the
  exact semantics for whichever lands first once the source is reachable.
* The single remaining opening for LMR is s63's reserve-class streaming
  orbit-rep engine (enumerating the `~3.1·10⁷` `χ`-orbit reps directly, never the
  `1.56·10¹¹` monomials). `S` and `det A₂₄` both consume its output; neither has
  any cheaper door, and this session proves it for `S`.
