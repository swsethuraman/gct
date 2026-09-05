# PRE-REGISTRATION — session 58, symmetric rectangular Kronecker coefficients at scale

Committed **before** any computation of this session.  Branch `s58-sk`, off
`main` at `0960bd548eae4a9767276f9a1f20d686538c3374` (sync baseline, rule 10:
this is `work/main` on the laptop and `origin/main`, identical at session start;
the ancestor test is trivially satisfied since the branch is cut from that
commit).  Delivery by bundle only; nothing is pushed.

Nothing below has been measured at the time of this commit.  §1 is
mathematics done on paper before the commit; every number it will produce is
listed in §2 as a measurement with a falsifier.

## 0. Prior information carried into the session

From the repository record:

- The house quantity.  `scripts/ambient_screen.m_det(lam, n, delta)` and the
  batched route of `analysis/wk9_s38_screen.py`, and the C engine of
  `analysis/wk9_s39_chars.c`, all compute

      sk(λ, n×δ) = (1/2) Σ_{ρ ⊢ N} χ^λ(ρ) [ χ^{(δ^n)}(ρ)^2 + χ^{(δ^n)}(ρ²) ] / z_ρ ,   N = nδ,

  where `ρ²` is the cycle type of `σ²` (`2k → k, k`; odd parts fixed).  This is
  `⟨χ^λ, Sym² χ^{(δ^n)}⟩`, the multiplicity of `S_λ(C^{n²})^*` in the coordinate
  ring of the `GL_{n²}`-orbit of `det_n` in degree `δ` (`n ≥ 3`).  All routes
  sum over every partition of `N`.
- Calibration values, all by that partition sum: `(16,2,2,2,2)/6`,
  `(20,2^4)/7`, `(24,2^4)/8` → **8**; `(30,2^5)/10` → **13**;
  `(29,4,2,2,2,1)/10` → **78**; `(29,3,2,2,2,2)/10` → **30**; `(4,4,4,4,4)/5` →
  **5**; the 2585 length-5 cells of `results/occurrence_screen.csv` (δ = 5–9)
  and `results/screen_d10_12.csv` (δ = 10); and — beyond the brief — the
  69,967 length-6..10 cells with `m_det ≥ 0` in `results/longweight_screen.csv`
  (δ = 8–12, so `N` up to 48, C engine of s39), and the s39 timing-log cells
  `(22,2^9)/10 → 18`, `(26,2^9)/11 → 18`, `(30,2^9)/12 → 18`,
  `(10,4,4,4,3^6)/10 → 4988`, `(11,4^6,3^3)/11 → 14123`, `(12,4^9)/12 → 2254`.
- `a((65,17,2^7), 24) = 274` (s50 integrator, two moduli; external reviewer
  by Weyl alternant).  `mult_det = rank(Θ^+: C^274 → C^{sk})` (s56, as quoted
  by the brief).  `p(96) = 118,114,304`.
- Sessions 56 and 57 are **not** in the repository, in `Projects\gct`, or in the
  project docs at session start.  Deliverable 3 (the s57 `pending` column) is
  conditional on their arrival; if they do not arrive the session reports that
  and computes nothing in their name.

The brief's standing constraints are read as follows for this session:

- **§5 degeneracy-direction pre-check.**  No statistic is developed here.  The
  quantity is the house `m_det`, the coordinate-ring multiplicity of the
  `det_4` *orbit* — the programme's base invariant, not a new characterisation
  of determinant type.  The session changes how it is computed, not what it is.
  The check is therefore vacuous, and it is recorded as such rather than
  skipped.
- **§7 functoriality pre-check.**  No new invariant is proposed.  For the
  record: `C[D̄] ↪ C[GL_{16}·det_4]` (the closure's ring injects into the
  orbit's), so `mult_λ C[D̄]_δ ≤ sk(λ, 4×δ)`; the identity `mult_det = rank Θ^+`
  is that inclusion written as a map.  It passes for the same reason the
  coordinate-ring row of §7's table passes.
- **Certificates.**  `tools/verify/FORMAT.md` declares three kinds (`hwv`,
  `matrix`, `full_rank`); none can carry a character-sum value.  This session
  produces no `gct-cert/1` certificate, and says so.  Its verification is by
  independent routes (§2), not by the verifier.
- Primes: no linear algebra is done; everything is exact integer arithmetic
  (Python integers / `python-flint` `fmpz` matrices for the dot products).

## 1. The algorithm, on paper (stated before it is run)

Notation: `μ = (δ^n)` the rectangle, `N = nδ`, `λ ⊢ N` with `λ_1` its first
row and `λ̄ = (λ_2, λ_3, …)` its **tail**, `m = |λ̄|`.  `g(α, β, γ)` the
Kronecker coefficient `⟨χ^α, χ^β χ^γ⟩`, `A(α, β) := ⟨χ^α, ψ²χ^β⟩` the Adams
pairing (`ψ²χ(σ) = χ(σ²)`), so that `sk(λ, n×δ) = (g(λ, μ, μ) + A(λ, μ))/2`.

**Lemma 1 (restriction of the two class functions).**  For `k + m = N`,
`τ ⊢ m`:

    ⟨ h_k s_τ , s_μ ∗ s_μ ⟩  =  Σ_{α ⊢ k, α ⊂ μ}  g(τ, α^∨, α^∨),
    ⟨ h_k s_τ , ψ²χ^μ ⟩      =  Σ_{α ⊢ k, α ⊂ μ}  A(τ, α^∨),

where `α^∨ ⊢ m` is the complement of `α` in the rectangle (rotated by 180°).

*Proof.*  Frobenius reciprocity: `⟨h_k s_τ, F⟩_{S_N} = ⟨ 1 ⊠ χ^τ, Res F
⟩_{S_k × S_m}`.  `Res χ^μ = Σ_{α,β} c^μ_{αβ} χ^α ⊠ χ^β`, and for a rectangle
`c^μ_{αβ} = [β = α^∨]` (`s_{μ/α} = s_{α^∨}`).  For `F = χ^μ χ^μ`:
`Res F = Σ_{α,α'} (χ^α χ^{α'}) ⊠ (χ^{α^∨} χ^{α'^∨})`, and `⟨1, χ^α χ^{α'}⟩ =
δ_{αα'}`, giving the first line.  For `F = ψ²χ^μ`: `(σ_1σ_2)² = σ_1²σ_2²`, so
`Res ψ²χ^μ = Σ_α ψ²χ^α ⊠ ψ²χ^{α^∨}`, and `⟨1, ψ²χ^α⟩ = (1/k!) Σ_σ χ^α(σ²)` is
the Frobenius–Schur indicator of `χ^α`, which is `1` for every irreducible
character of a symmetric group (all are realisable over `Q`).  ∎

**Lemma 2 (Jacobi–Trudi along the first row).**

    s_λ = Σ_{j ≥ 0} (−1)^j  h_{λ_1 + j}  s_{λ̄ / (1^j)},   s_{λ̄/(1^j)} = Σ_{τ ∈ V_j(λ̄)} s_τ,

`V_j(λ̄)` the set of `τ ⊂ λ̄` with `λ̄/τ` a vertical strip of `j` boxes.
*Proof.*  Expand `det(h_{λ_i − i + j'})` along its first row; the `(1, j+1)`
minor is the skew Jacobi–Trudi determinant of `λ̄/(1^j)`.  ∎

**Theorem (first-row reduction).**  With `T(λ) = { (j, τ) : τ ∈ V_j(λ̄) }` and
`B_m(δ, n) = { β ⊢ m : ℓ(β) ≤ n, β_1 ≤ δ }`,

    g(λ, μ, μ) = Σ_{(j,τ) ∈ T(λ)} (−1)^j Σ_{β ∈ B_{|τ|}(δ,n)} g(τ, β, β),
    A(λ, μ)    = Σ_{(j,τ) ∈ T(λ)} (−1)^j Σ_{β ∈ B_{|τ|}(δ,n)} A(τ, β),
    sk(λ, n×δ) = (g(λ, μ, μ) + A(λ, μ)) / 2.

The inner quantities are class sums over `S_{|τ|}`, `|τ| ≤ m`.  **The cost
depends on the tail `λ̄` and on `n`, and on `N` only through the box condition
`β_1 ≤ δ`, which is vacuous for `δ ≥ m`.**  Hence:

**Corollary (stability in the tail).**  For fixed `λ̄` and `n`,
`sk((N − m, λ̄), n×(N/n))` is constant for `N ≥ n·m`, i.e. `δ ≥ |λ̄|`.  (A
stabilisation of rectangular Kronecker coefficients when the rectangle grows
is Manivel's, arXiv:0907.3351, J. Algebraic Combin. 33 (2011); here it is a
one-line corollary and comes with the computation.)

Sanity checks done by hand before this commit: `λ = (N)` gives `g = A = 1`,
`sk = 1`; `λ = (N−1, 1)` gives `g = 1 − 1 = 0`, `A = 0`, `sk = 0`, agreeing with
the number of removable corners of a rectangle minus one; `λ = μ = (2,2)` gives
`g = 2 − 1 = 1`, `A = 1`, `sk = 1`, agreeing with `Sym²(S^{(2,2)}) = S^{(4)} ⊕
S^{(2,2)}`.

This is the algorithm the brief's §3 asks for: the analogue of the length trick
is not a smaller variable count (the `n² = 16`-variable model is already
minimal, since the rectangle needs `n` rows on each side) but the removal of
`N` from the cost altogether, with the tail as the size parameter.

## 2. The measurements, fixed now

Code `analysis/wk9_s58_sk.py`, one file, two independent routes inside it: the
reduction (§1) and a brute-force partition sum with its own Murnaghan–Nakayama
(β-numbers, written afresh; the house `chi` is imported only for comparison).
Every run under `timeout` and `ulimit -v`, pid to `results/logs/s58_*.pid`.
Exact integers throughout; a non-integer at any division is an error, not a
rounding.

### M1 — calibration (mandatory; one disagreement and the algorithm is wrong)

Reproduce, exactly: the seven values of the brief's table; every cell of
`results/occurrence_screen.csv` and `results/screen_d10_12.csv` (2585 cells,
δ = 5–10); every `m_det ≥ 0` cell of `results/longweight_screen.csv` (69,967
cells, δ = 8–12, lengths 6–10); the six s39 timing-log cells.  Also: the
reduction against the house `m_det` and against the brute force on a random
sample of cells of *every* length `1 ≤ ℓ ≤ 16` at `N = 20, 24, 28` (where the
reduction is non-trivial in every term), and the two sum rules
`Σ_{λ ⊢ N} f^λ · sk(λ) = f^μ (f^μ + 1)/2` and `Σ_λ f^λ · g(λ,μ,μ) = (f^μ)²`
over **all** `λ ⊢ N` at `N = 20, 24`.

- **Positive:** every value equal.  **Falsifier:** any single disagreement —
  reported as such in `results/s58_calibration.md`, with the algorithm *not*
  adjusted to fit.

### M2 — cost curve

Wall time of the reduction (i) at fixed tail `(17, 2^7)` for `δ = 11 … 24`
(`N = 44 … 96`), (ii) at fixed `δ = 10` for tails of size 4 … 36, and of the
house partition sum (Python `m_det`; the s39 C engine if it builds) for
`N = 20 … 48`.  Reported as a table, with the operation count of the inner
class sums (`Σ_τ Σ_β p(|τ|)`) beside the timings.

- **Prediction P3 (prior 0.95):** the reduction's wall time at fixed tail is
  flat in `N` to within a factor 2 across `N = 44 … 96` once `δ ≥ 17`
  (`B_m` saturates), while every partition-sum route grows at least like
  `p(N)`.

### M3 — the goal cell

`g((65,17,2^7), 24^4, 24^4)`, `A`, and `sk((65,17,2^7), 24^4)`, by the
reduction, with the run bounded and logged.  A second, independent
organisation of the same reduction (the Pieri inversion: `⟨s_λ, F⟩ =
⟨h_{λ_1} s_{λ̄}, F⟩ − Σ_{γ ≠ λ} ⟨s_γ, F⟩` over the other terms of
`h_{λ_1} s_{λ̄}`, recursing on the tail) must return the same three integers.

- **Prediction P1 (prior 0.85):** `sk ≥ 274 = a`, i.e. the source of `Θ^+` is
  not larger than its target and the LMR cell shows no *dimension* gap (the
  screen's `a ≤ m_det` regularity persists; margins widen with degree).
- **Prediction P2 (prior 0.7):** `10^3 ≤ sk ≤ 10^6`.  Stated so that the
  magnitude is a prediction and not a post-hoc reading.
- **Prediction P5 (prior 0.7):** `sk((N−31, 17, 2^7), (N/4)^4)` takes the same
  value at `δ = 24, 25, …, 32`: the corollary guarantees constancy from
  `δ = 31`, and the Kronecker support bound `|τ| − τ_1 ≤ 2(|τ| − β_1)` kills
  every `β` with `β_1 > 24` in the `g`-part already at `δ = 24`; the `A`-part
  is the uncertainty.  Falsifier: any change of value across `δ = 24 … 32`.

### M4 — session 57's `pending` column

Conditional on the s57 table arriving.  Every pending cell the reduction
reaches within the session's budget (a cell with tail size `m ≤ 40` is expected
to take seconds; `m ≤ 50` minutes) is filled and marked with this session; a
cell not reached is left `pending` with its tail size and the estimated cost
written beside it.

### M5 — `g` alone

The reduction computes `g(λ, δ^4, δ^4)` and `A` separately, so `g` comes for
free at every cell above; it is reported beside `sk` (deliverable 4), together
with the antisymmetric coefficient `(g − A)/2`, which must be a non-negative
integer at every cell (a free consistency check, as in s39).

## 3. Stopping rules

- A calibration mismatch halts everything downstream: the mismatch is
  reported, the code is not tuned, and the goal cell is not computed by the
  failing route.
- The goal cell is bounded at `timeout 3600` and `ulimit -v 6000000`; if it
  does not finish, the cost is stated in numbers from M2's curve and the run is
  not extended.

## 4. Deliverables

`analysis/wk9_s58_sk.py`, `results/s58_calibration.md`, `results/s58_cells.jsonl`
(every value computed, one JSON per cell with `g`, `A`, `sk`, timing),
`docs/s58_report.md`, logs under `results/logs/s58_*`.  Bundle
`s58_sk.bundle`, single ref `refs/heads/s58-sk`, prerequisite `0960bd5`.
