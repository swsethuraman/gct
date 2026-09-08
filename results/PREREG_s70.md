# Pre-registration — session 70 (C3): the two ranks at LMR, and which needs a source

Branch `s70-tworanks` off `main` at `226b4ef1` (ancestry gate `git merge-base
--is-ancestor 226b4ef1 HEAD` passes). Committed **before any rank is computed.**
Labels: **proved** / **measured** / **adopted** / **expectation**.

The cell: `λ = (65,17,2⁷)`, `δ = 24`, `ℓ = 9`, `a = 274`, `h_pad = 521`,
`mult_det = 273` (`i_det = 1`, LMR + s63 predecessor deduction), the programme's
only theorem-`i_det>0` cell.

## 0. The two objects, and the semantics fixed in advance

**`rank S_{λ,24}` — the reducible-normalisation split.** `S = S_{λ,δ}` is the
map `M⁴_λ → ⊕_μ M³_μ` induced by the comultiplication (split) `Sym⁴V → V ⊗
Sym³V`, `c_α ↦ Σ_{i:α_i≥1} y_i·d_{α−e_i}`, restricted to the `λ`-highest-weight
space; its target is the degree-`δ` part of the **normalisation** of `C[R_r]`,
`D_δ = Sym^δ V ⊗ Sym^δ(Sym³V)`, of dimension `h_pad = 521` (session-42 Pieri
identity). Then

    rank S = mult_red   (= dim of the λ-isotypic image in the normalisation ring),
    i_red  = a − rank S = mult_λ I(R_r)_δ.

Semantics, fixed now (they are **not** symmetric; a report that reads
"success = 274" mis-states both):

* **`rank S < 274`.** Then `mult_pad ≤ mult_red = rank S < 274`, so `i_pad ≥ 1`;
  with `i_det = 1`, `D = i_det − i_pad ≤ 0`. **The LMR cell is settled against a
  `D>0` by a `274×521` reducible rank alone**, before any permanent-specific
  block. Strongest cheap outcome in the batch; a full result.
* **`rank S = 274`.** Then `i_red = 0`. This does **not** establish padded full
  rank: `S` is the universal reducible-normalisation stage; the
  permanent-specific cubic stage `⊕Θ^{per₃}` can still drop rank afterwards
  (`mult_pad = rank[(⊕Θ)∘S] ≤ rank S`). So `i_pad` stays unknown and session 73
  must determine it. The report will say exactly this; it will **not** write that
  padded full rank is established.

**`det A₂₄` — the room-one denominator.** `A₂₄` is the degree-24 Gram `B|_{J(M₂₃)}`
restricted to the transported predecessor `J(M₂₃)` (the *corrected* denominator,
not the predecessor's own Gram), a `273×273` determinant; `s = det G₂₄/det A₂₄`,
`s = 0 ⟺ i_det(24) ≥ 1`. `det A₂₄ ≠ 0 ⟹ i_det = 1`; `det A₂₄ = 0` is the stronger
outcome (a determinant equation at `ℓ=9`, degree 23, `i_det(23) ≥ 1`, strictly
stronger than LMR). Both primes; `rank(MᵀM) ≤ rank M` makes the nonsingularity
step **characteristic-free** (`rank(Θ*Θ)=rank Θ` is char-0 only and is not used).

## 1. Part A — the determination (ungated, first hour)

**Question.** `det A₂₄` needs the explicit source (the `273`-dim predecessor
HWV image). Does `rank S_{λ,24}`? I.e. can `S` be built with rows indexed by the
Pieri shapes and **columns indexed by the ambient multiplicity abstractly**,
rather than by explicit source vectors — making the LMR half ungated?

**Expectation (to be settled in writing, either branch reported).** `rank S` is
**source-dependent**: its target/rows (`⊕_μ M³_μ`, the 48 Pieri/cubic blocks at
LMR) and the split map are source-free, but its columns are a basis of
`M⁴_λ = HWV_λ(Sym^δ Sym⁴V)` — the `a=274` quartic source — and there is no basis
of that space that is not explicit source vectors. Grounds, stated before the
calibration: (i) if `rank S` were a function of `λ,δ` alone, `mult_red` would be,
contradicting s42-§B (`h_pad − mult_red` = normalisation-quotient multiplicity on
the non-normal locus, "computing it is exactly the original problem") and s60
(eight cells with `mult_red < min(a,h_pad)`, no combinatorial formula); (ii)
s64-§7 states the factorized route's fast branch is "gated on the same wall
(building/evaluating the common source at `r=9,δ=24`)" — the 48-block advantage
is on the target, not the source. If so, LMR is gated exactly as `det A₂₄` is,
and the branch taken is the ungated fallback (§3).

**Falsifier F-A.** If a source-free construction of the *matrix* `S` (columns
from `λ,δ` only) is exhibited and validated on the calibration cells, the
expectation is refuted and the LMR `274×521` rank is attempted.

## 2. Part B calibration — the two n=4 ranks (the measurement)

Implement `S` (the split, `analysis/wk11_s70_split.py`) and report `rank S`
exactly at two banked, discriminating `n=4` cells, both primes:

| λ, δ | a | h_pad | banked mult_red | i_red | **rank S must be** |
|---|---|---|---|---|---|
| (8,4,4,4,4), 6 | 2 | 1 | 1 | 1 | **1** |
| (12,9,9,1,1), 8 | 7 | 6 | 5 | 2 | **5** |

Both are strictly below `a` — the regime that matters at LMR. Each is
independently cross-checked by the (★)/`E_red` route on the **same** HWVs
(`mult_red = rank kern[:,non-red]`), which must agree, and against the banked
session-60/64 value.

**Falsifiers / kill criteria.**
* **F-B1 (halt).** `rank S ≠ banked mult_red` at either cell — in particular
  `rank S = a` (2 or 7) — halts all LMR use of `S`. The construction is wrong;
  report the mismatch (worth more than an LMR number that could not be trusted).
* **F-B2.** `rank S` disagrees across the two primes, or across two independent
  codomain hash seeds — halt, report.
* **F-B3.** the (★) cross-check disagrees with `rank S` — the split identity
  `rank S = mult_red` is refuted; report.

**Predictions (scored at close).** P1 `rank S = 1` at (8,4,4,4,4)₆ (0.9). P2
`rank S = 5` at (12,9,9,1,1)₈ (0.9). P3 both primes + both hash seeds agree
(0.97). P4 (★) route agrees at both cells (0.95). P5 Part A resolves
source-**dependent** (0.85).

## 3. The branch, and the stopping rules

* Part A resolves source-dependent ⟹ LMR `rank S` and `det A₂₄` are both **gated**
  on the `r=9,δ=24` source that s63 measured walled on all three realisations
  (`N_S=1.56·10¹¹`; Foulkes `1.2·10⁹³`; Gram/Schur `|S|≥6·10⁶`). Neither is
  attempted this session. The ungated deliverable is Part A + the two calibration
  ranks + the written construction, reusable when the source becomes reachable.
* **Do not attempt the LMR carrier build under any circumstance** (S5).
* **Do not attempt the LMR carrier-space engine** that s63 measured dead on all
  three realisations.
* If `rank S < 274` were ever obtained at LMR, that settles the cell — do not
  then spend effort on `det A₂₄`, whose answer no longer changes the verdict.
* A calibration cell disagreeing with its banked `mult_red` halts LMR use of `S`
  immediately (F-B1); report the mismatch, not a workaround.

## 4. Deliverables

`results/PREREG_s70.md` (this file); `docs/s70_report.md` (Part A determination
in its first paragraph); the `S` construction written out in `docs/s_split.md`;
ranks and costs `results/s70_ranks.md` + `.jsonl`; certificates for any exact
rank claim under `results/certs/`; code `analysis/wk11_s70_*.py`; bundle
`s70_tworanks.bundle` + `.md5`. Nothing pushed; single-writer files
(`paper/*.tex`, `PROJECT_NOTES.md`, `docs/boundary_deficit.html`) untouched.
