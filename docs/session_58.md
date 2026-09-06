# Session 58 — symmetric rectangular Kronecker coefficients at scale

Branch `s58-sk` off `main` at `0960bd5` (= `work/main` = `origin/main` at session
start; ancestor test trivial).  Pre-registration `results/PREREG_s58.md`, committed
before any computation.  Deliverables `docs/s58_report.md`, `analysis/wk9_s58_sk.py`
(+ `wk9_s58_chars.c`), `results/s58_calibration.md`; every value in
`results/s58_*.json*`; logs `results/logs/s58_*`.  Bundle `s58_sk.bundle`, single ref
`refs/heads/s58-sk`, prerequisite `0960bd5`.  Nothing pushed.

## Verdict

> **`sk((65,17,2⁷), 24⁴) = 48 825`** (`g = 92 000`, Adams part `A = 5 650`,
> antisymmetric part `43 175`), in 0.2 s, by a first-row reduction whose cost
> depends on the tail `|λ̄| = 31` and not on `N = 96`.  Four internal routes agree;
> calibration against every banked value the brief lists, all 2585 length-5 screen
> cells, 56 137 of the 69 967 long-weight screen cells (lengths 6–10, `N` up to 48), the s39 C engine on the goal family through `N = 64`,
> and brute force at every partition of `N = 20, 24, 28` (sum rules exact):
> **zero disagreements**.
>
> `Θ⁺ : C²⁷⁴ → C⁴⁸ ⁸²⁵`.  The LMR cell is a well-posed finite rank problem —
> `274 × 48 825`, inside the size range the programme has handled (`n_χ` up to
> 65 778 in s52).
>
> **Direct, not extrapolated** (the integrator's mid-session question): the
> reduction is an identity of symmetric functions and computes `sk` *at* `δ = 24`
> with the box condition `β₁ ≤ 24` as part of the exact formula; no stability
> hypothesis enters.  The boundary family `(3k+2m, k, 2^m)`, `δ = k+m`, on which
> the LMR cell sits at exact equality `2δ = |ρ| + ρ₁`, is reproduced at **nineteen
> cells** (the integrator's nine direct-sum values through `N = 40`, and ten more
> through `N = 64` against the s39 C engine, brute force and the house `m_det`),
> zero disagreements.  This independently validates the external audit's
> Manivel-route value (`B_ρ = 92 000`, `T_ρ = 5 650`) at equality.

## The reduction (proved in the pre-registration and the report)

Jacobi–Trudi along the first row, `s_λ = Σ_j (−1)^j h_{λ₁+j} s_{λ̄/(1^j)}`, plus
Frobenius reciprocity with `c^{(δⁿ)}_{αβ} = [β = α^∨]` and the Frobenius–Schur
indicator `⟨1, ψ²χ^α⟩ = 1`:

    g(λ,μ,μ) = Σ_j (−1)^j Σ_{τ: λ̄/τ vertical j-strip} Σ_{β ⊢ |τ|, ℓ(β) ≤ n, β₁ ≤ δ} g(τ,β,β),

same for the Adams part, `sk = (g + A)/2`.  Class sums over `S_{|τ|}` only.
**Corollary:** `sk((N−m, λ̄), (N/4)⁴)` is constant once `δ ≥ (m + λ₂)/2`, i.e.
`λ₁ ≥ m + 2λ₂` (Kronecker depth bound); the LMR cell sits exactly on that line
(`65 = 31 + 34`) and `48 825` is the limit value of its family — measured constant
for `δ = 23 … 32`.  The "length" analogue for `sk` is not a smaller variable count
(16 is already minimal) but this removal of `N` from the cost.

## Numbers to keep

- Goal family `(N−31, 17, 2⁷)`: `2714, 15383, 26654, 35340, 41463, 45366, 47488,
  48435, 48744, 48815, 48824, 48825, 48825` at `δ = 12 … 24`; warm cost
  0.19–0.22 s at every `N` (P3), while the s39 C engine doubles per step of four in
  `N` and stops at its `NMAX = 64` (values agree at 48, 52, 56, 60, 64).
- Partition sum at `N = 96`, in numbers: `p(96) = 118 114 304` classes; the s39
  engine extrapolates to ~5 h and ~10⁹ memo entries (tens of GB) after a rewrite;
  the Python house route to ~5 × 10⁵ s and a terabyte-scale memo.  Memory is the
  wall.  The reduction: 53 829 class-sum terms over `S₂₃ … S₃₁`.
- LMR family: `n = 3`: `(19,7,2⁵)/12 → sk = 10` (brute force agrees; `a = 6`);
  `n = 5`: `(151,31,2⁹)/40`, `N = 200`, `sk = 1 435 445 282` in 645 s.
- Reach: tails ≤ 40 boxes seconds; 48 boxes minutes; wide tails ≥ 52 boxes tens of
  minutes to hours (second reduction step is the next tool).

## Pre-checks and certificates

§5 and §7 vacuous (no statistic or invariant proposed; `sk` is the house `m_det`);
no `gct-cert/1` kind carries a character sum, so no certificate was produced and
`tools/verify` was not run; verification is the calibration plus four-route
agreement.  No prime used anywhere.

## Scorecard

P1 `sk ≥ 274` (0.85) confirmed; P2 `10³ ≤ sk ≤ 10⁶` (0.7) confirmed; P3 flat cost
(0.95) confirmed; P5 constant `δ = 24 … 32` (0.7) confirmed, from 23.  M4 (s57
`pending` column): **dropped by the integrator** — sessions 56/57 have not been run;
replaced by the affordability rule (report §6): cost is set by the tail
`|λ| − λ₁`, ≤ 40 boxes is seconds at any `N`, ≈ 48 minutes, ≥ 52 wide tails
tens of minutes to hours.

## Corrections flagged (not edited)

- `results/occurrence_screen.md`: the δ = 11, 12 length-5 rows are now minutes of
  work, not beyond budget.
- `results/longweight_screen.md` does not state the s39 engine's limits
  (`N ≤ 64`, `λ₁ + 9 < 64`).
