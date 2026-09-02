# The long-weight hunt — the occurrence route at `6 ≤ ℓ ≤ 10`, `n = 4`

Session 39, branch `s39-longweights`, 2026-09-02.  Clone tip `e9cb8dd` (the
s36 merge).  Ancestry gate `git merge-base --is-ancestor 48bbdc3 HEAD` passes
and `docs/s36_review.md` is present.  Pre-registration `results/PREREG_s39.md`,
committed before any screen row or evaluation.  No session-39 collision in the
record (only the brief `docs/s39_prompt.md` was present).

Labels: **proved** / **measured** / **expectation**, per the pre-registration.

This is the programme's first direct screen of the long-weight region — weights
with six or more rows at `n = 4` — where at `n = 3` the determinant's ideal was
first pinned (`docs/d5_ideal.md` §0: `a = 1, m_det = 0` cells at lengths 8, 9,
`δ = 10`).  It extends s38's length-5 occurrence screen
(`results/occurrence_screen.md`) upward in length.

---

## 0. Verdict

**The occurrence route is silent across the entire long-weight region — an
exhaustive negative.**  Every one of the **79,255** weights `λ ⊢ 4δ` with
`6 ≤ ℓ(λ) ≤ 10` and `λ_1 ≥ δ`, for `δ = 8, 9, 10, 11, 12`, was screened; of the
**69,967** with `a ≥ 1`, **not one** has `a = 1, m_det = 0` (one-bit) and **not
one** has `a > m_det` (forced).  Phase 1 therefore had no obstruction test to
run.  Three proved-and-measured statements:

1. **The eligible region is now bounded on all four sides, all proved.**  An
   occurrence obstruction (`mult_det = 0 < mult_pad`) or a forced multiplicity
   drop can live only at a weight with `a ≥ 1`, `λ_1 ≥ δ`, and
   **`6 ≤ ℓ(λ) ≤ 10`**.  The upper bound `ℓ ≤ 10` is new this session
   (§1): the padded permanent is concise in ten variables, so its orbit
   closure lies in the subspace variety `Sub_10`, whose coordinate ring
   carries no weight of length `> 10`; hence `mult_pad = 0` and no obstruction
   for every `ℓ ≥ 11`.  With `ℓ ≤ 5` unable to see the permanent at all
   (`docs/washout_lemma.md`) and `ℓ ≤ δ` free from Pieri, the whole
   permanent-sensitive long-weight region is `6 ≤ ℓ ≤ min(δ, 10)`.

2. **The occurrence route is silent, and not narrowly.**  For every screened
   cell `a(λ,δ) ≤ m_det(λ)`.  The margin is enormous and grows with `δ`: at the
   most-balanced cell of each degree `m_det` outruns `a` by orders of magnitude
   (δ = 12: `a = 87,405` against `m_det = 482,821,387` at `(16,11,8,6,4,2,1)`),
   and the *tightest* cell anywhere — the closest the screen ever comes to
   firing — is the peaked length-6 family `(4δ−10, 2,2,2,2,2)`, with `a = 1`,
   `m_det = 13`, **margin 12 at every `δ`**.  It never closes.  So no occurrence
   obstruction and no forced multiplicity drop lives at lengths 6–10: any
   separation here would be a genuine multiplicity phenomenon
   (`mult_det < a ≤ m_det`), invisible to arithmetic — the same character s38
   found at length 5, now with a widening gap.

3. **The `n = 3` precedent does not transfer, and now we can say why.**  At
   `n = 3` the one-bit cells sat at `ℓ = 8, 9`, the top of the Kronecker length
   bound `ℓ ≤ n² = 9`, where the two-rectangle coefficient is sparse.  At
   `n = 4` that edge is near `ℓ = 16`, excluded by the `ℓ ≤ 10` theorem; the
   region that *can* carry a pad obstruction (`ℓ ≤ 10`) sits well below it, and
   there `m_det` is large.  The pre-registered P2 (silence expected, from this
   regime argument rather than a naive transfer) is **confirmed** in the
   completed region.

---

## 1. The length bound `ℓ ≤ 10` (proved)

*(integrator's addendum, `results/PREREG_s39.md` §0; restated here for the
record.)*  Every pad point of the pipeline is `l(s)·per_3(A(s))`, a linear
pullback of the concise form `x_0·per_3(x_1..x_9) ∈ Sym^4 C^{10}` along
`C^r → C^{10}`.  So `P_r = D_r^{pad} ⊆ Sub_{10} := \overline{GL_r · Sym^4(C^{10})}`,
the quartics writable in ten linear forms.  A highest-weight vector `v` of
weight `λ` with `ℓ(λ) ≥ 11` vanishes on `Sym^4(C^{10})`: at `F_0` supported on
`x_1..x_{10}`, only monomials `∏ c_{α_j}` with every `α_j` supported on
`{1..10}` survive, so only weights `μ` with `μ_{11}=…=0` contribute; but every
weight of `V_λ` satisfies `sort(μ) ⊴ λ`, and `Σ_{i≤10} μ_i = |λ| ≤ Σ_{i≤10}
λ_i` forces `λ_{11} = 0`, a contradiction.  Since `v` is `GL_r`-covariant it
then vanishes on `GL_r · Sym^4(C^{10}) ⊇ P_r`, so `mult_pad(λ,δ) = 0`.  ∎

The same argument with 16 in place of 10 is the determinant's `ℓ ≤ 16`
(`det_4 ∈ Sym^4 C^{16}`), and with `k = ℓ(λ)` it is the restriction lemma of
`docs/washout_lemma.md`.  So the two sides' concision numbers, 10 and 16,
bracket the rows that can matter: `mult_pad` needs `ℓ ≤ 10`, `mult_det` needs
`ℓ ≤ 16`; at `11 ≤ ℓ ≤ 16` the determinant can be nonzero while the permanent
is forced to zero — but that is `mult_pad = 0 ≤ mult_det`, the wrong sign, never
an obstruction.  The obstruction window is exactly `ℓ ≤ 10`.

---

## 2. The screen (measured)

*Code.*  The screen runs on an exact `__int128` Murnaghan–Nakayama engine
written for this session from the rule, independent of the house python
(`analysis/wk9_s39_chars.c`, driver `analysis/wk9_s39_chars.py`);
`a(λ,δ) = ⟨h_δ[h_4], s_λ⟩` and `m_det(λ)` (symmetric rectangular Kronecker,
rectangle `(δ^4)`) are accumulated as weighted character sums over two 61-bit
primes and CRT-reconstructed with exact bound and parity checks.  It reproduces
the house `chi`, `a`, `m_det`; the `n = 3` anchors (`Σ m_det = 3, 11, 43`); the
s28 `δ = 10` precedent cells (`a = 1, m_det = 0`); and **s38's entire length-5
table at `δ = 5..9`** before extending it (`results/logs/s39_chars_selftest.log`,
`results/logs/s39_engine_timing.log`).  The driver
(`analysis/wk9_s39_screen.py`) walks `(δ, ℓ)` chunks under an `O_EXCL` claim
queue with PID-owned claims and dead-owner reconcile, banking each row
(flush + fsync) as it is computed.

*Result.*  `results/longweight_screen.md` (+`.csv`).  Exhaustive; every `(δ,ℓ)`
chunk carries a `.done` marker and the banked unique-row count equals the
candidate count (79,255) exactly.

| δ | candidates | cells (`a≥1`) | one-bit | forced | max `a` (cell) — its `m_det` | tightest cell — margin |
|---|---|---|---|---|---|---|
| 8 | 2,228 | 1,479 | 0 | 0 | 91 `(11,8,6,4,2,1)` — 244,549 | `(22,2,2,2,2,2)` a1/m13 — 12 |
| 9 | 5,526 | 4,131 | 0 | 0 | 504 `(14,9,6,4,2,1)` — 2,226,605 | `(26,2,2,2,2,2)` a1/m13 — 12 |
| 10 | 12,464 | 9,975 | 0 | 0 | 2,269 `(14,10,7,5,3,1)` — 24,166,182 | `(30,2,2,2,2,2)` a1/m13 — 12 |
| 11 | 21,925 | 19,552 | 0 | 0 | 13,339 `(15,11,7,5,3,2,1)` — 247,341,470 | `(34,2,2,2,2,2)` a1/m13 — 12 |
| 12 | 37,112 | 34,830 | 0 | 0 | 87,405 `(16,11,8,6,4,2,1)` — 482,821,387 | `(38,2,2,2,2,2)` a1/m13 — 12 |
| **Σ** | **79,255** | **69,967** | **0** | **0** | — | margin 12 throughout |

Cells by length (`a≥1`): ℓ6 10,528; ℓ7 14,490; ℓ8 16,422; ℓ9 15,668; ℓ10 12,859.

The tightest cell at every degree is the **peaked length-6 family**
`(4δ−10, 2,2,2,2,2)` with `a = 1`, `m_det = 13`, **margin 12** — the length-6
analogue of s38's length-5 `(4δ−8, 2,2,2,2)` family (`a = 1`, `m_det = 8`,
margin 7).  The margin *grew* from 7 at length 5 to 12 at length 6, and holds
constant in `δ`.  The largest-`a` fire-risk extreme (balanced cells, `a` up to
87,405) is covered at every length and clean by orders of magnitude.  Both of
s38's fire-risk extremes are covered at every length 6–10, and both are silent.

---

## 3. Phase 1 — one-bit and forced tests

**Empty by the screen: no one-bit or forced cell exists in the eligible region,
so Phase 1 ran no obstruction test** (`results/onebit_ledger.md`; the harness
`analysis/wk9_s39_onebit.py --runall` over the screen csv returns "no
obstruction candidate").  Had a cell existed, the harness would build the unique
HWV by the validated stabiliser reduction (P1 reproduced three s36 ledger cells
and the witness exactly, `results/s39_validation.md`), reconstruct it over `Z`,
verify every raising operator kills it, then audit `m_det = 0` at 20 `det_4`
pencils (must vanish) and test 20 independent true padded-permanent points (a
one-bit cell), or take the pad-side rank at `3(a+8)` true-pad points (a forced
cell) — `STOP-EVERYTHING` on any candidate.  The harness is delivered validated
(its build/kernel/evaluation path is the P1-validated one; its exact
reconstruction and independent point construction are the s36-audited
`wk9_s36_exact` / `wk9_s36_bite` paths) and, correctly, unused.

---

## 4. The window as left, and coverage

- **Obstruction window (proved bounds):** `a ≥ 1`, `λ_1 ≥ δ`, `6 ≤ ℓ ≤ 10`.
- **Screened exhaustively (measured):** `δ = 8, 9, 10, 11, 12`, `6 ≤ ℓ ≤
  min(δ,10)`, every `λ_1 ≥ δ` — 79,255 weights, 100% of the region, no cell
  skipped (the candidate count equals the banked count at every `(δ,ℓ)` chunk).
- **Occurrence route:** **silent** — no `a > m_det`, no `a = 1, m_det = 0`,
  anywhere; margin ≥ 12 everywhere and growing with `δ` at the balanced end.
- **Not reached, by theorem not budget:** rows `11 ≤ ℓ ≤ 16` (`mult_pad = 0`
  there, §1); `δ ≥ 13` (the screen stops at 12, as pre-registered — the pattern
  is a stable one-parameter family in `δ`, so no boundary is expected there, but
  it is not measured).
- **What is not touched:** the multiplicity route (`mult_det < a ≤ m_det`
  requires a rank, not arithmetic).  Whether a *multiplicity* obstruction lives
  at `6 ≤ ℓ ≤ 10` — the one thing the arithmetic screen cannot see — is open,
  and is the natural successor probe (the reduction reaches `n_χ ≈ 15,500`; the
  peaked cells are cheap, `n_χ = 200` at `(4δ−10,2^5)`).

---

## 5. Honest boundary

- **Proved:** the `ℓ ≤ 10` bound (§1); the eligible-region characterisation;
  the engine's exactness (two primes, CRT, bound + parity asserts on every
  cell).
- **Measured:** the screen values `a`, `m_det` — each exact (two 61-bit primes,
  CRT, per-cell bound and parity asserts); validated against the house routines,
  the `n=3` anchors and s38's length-5 table before use, and re-verified
  independently after (`results/s39_verify.md`: `a` vs the house plethysm and vs
  a character-free reduced kernel at `δ = 10,11,12`; `m_det` vs the house at
  `δ = 10`).
- **Expectation confirmed:** P2 (silence expected at `6 ≤ ℓ ≤ 10` by `δ = 12`,
  from the regime argument, not a transfer) — confirmed exhaustively, with the
  gap wider than at length 5.  P3 (would a one-bit vector vanish at the pad) is
  vacuous: no one-bit vector exists.  P1 held (`results/s39_validation.md`).
- **Regime:** the silence is an arithmetic statement about `a` vs `m_det` at
  `6 ≤ ℓ ≤ 10`; it says nothing about the multiplicity route, and it is not a
  transfer of the `n = 3` precedent (which lived at `ℓ` near `n²`, outside the
  pad-eligible region here).

_(house style: proved / measured / expectation, each labelled.)_
