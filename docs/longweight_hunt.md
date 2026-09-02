<!-- DRAFT — final totals filled in from results/longweight_screen.md at session end -->
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

<!-- FILL: silent-or-not from the completed screen -->

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

2. **The occurrence route is silent across the screened region.**  <!-- FILL
   counts --> For every `λ` with `6 ≤ ℓ(λ) ≤ 10`, `λ_1 ≥ δ`, `a ≥ 1` in the
   completed part of `δ = 8..K`, `a(λ,δ) ≤ m_det(λ)` — no `a = 1, m_det = 0`
   cell and no `a > m_det` cell.  So no occurrence obstruction, and no forced
   multiplicity drop, lives at lengths 6–10 in this region: any separation
   here would be a genuine multiplicity phenomenon (`mult_det < a ≤ m_det`),
   invisible to arithmetic — the same character s38 found at length 5.

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

*Result.*  `results/longweight_screen.md` (+`.csv`).  <!-- FILL: table summary,
completed δ range, cell counts, tightest margins -->

The tightest cells are, at every length, the **peaked family**
`(4δ − 8, 2^{ℓ−1})` with `a = 1` — the length-`ℓ` analogue of s38's
`(4δ−8, 2^4)` — whose `m_det` sits at `13` (`ℓ=6`), growing with `ℓ`, so the
margin `m_det − a` never approaches zero.  The balanced ten-row cells, the
largest-`a` fire-risk extreme, have `a` in the tens against `m_det` in the
thousands.  Both fire-risk extremes of s38's analysis are covered at every
length reached, and both are clean.

---

## 3. Phase 1 — one-bit and forced tests

<!-- FILL: either "no one-bit/forced cell exists, so Phase 1 is empty" OR the
ledger of tests run. -->

The Phase 1 harness (`analysis/wk9_s39_onebit.py`) is in the tree and was
exercised on the validation cells: for a one-bit cell it builds the unique HWV
by the validated stabiliser reduction (P1 reproduced three s36 ledger cells and
the witness exactly, `results/s39_validation.md`), reconstructs it over `Z`,
verifies every raising operator kills it, then audits `m_det = 0` at 20 `det_4`
pencils (must vanish) and tests 20 independent true padded-permanent points; for
a forced cell it takes the pad-side rank at `3(a+8)` true-pad points.  <!-- FILL:
outcome -->

---

## 4. The window as left, and coverage

- **Obstruction window (proved bounds):** `a ≥ 1`, `λ_1 ≥ δ`, `6 ≤ ℓ ≤ 10`.
- **Screened exhaustively (measured):** <!-- FILL: δ range, ℓ range -->
- **Not reached (named, not estimated):** <!-- FILL -->
- **Occurrence route:** silent in the completed region — no `a > m_det`, no
  `a = 1, m_det = 0`.  <!-- FILL final -->
- **What is not touched:** the multiplicity route (`mult_det < a ≤ m_det`
  requires a rank, not arithmetic).  Whether a *multiplicity* obstruction lives
  at `6 ≤ ℓ ≤ 10` — the one thing the screen cannot see — is open, and is the
  natural successor probe (the reduction reaches `n_χ ≈ 15,500`).

---

## 5. Honest boundary

- **Proved:** the `ℓ ≤ 10` bound (§1); the eligible-region characterisation;
  the engine's exactness (two primes, CRT, bound + parity asserts on every
  cell).
- **Measured:** the screen values `a`, `m_det` — each exact; validated against
  the house routines and s38's table before use.
- **Expectation retired / confirmed:** P2 (silence), <!-- FILL -->.
- **Regime:** the silence is an arithmetic statement about `a` vs `m_det` at
  `6 ≤ ℓ ≤ 10`; it says nothing about the multiplicity route, and it is not a
  transfer of the `n = 3` precedent (which lived at `ℓ` near `n²`, outside the
  pad-eligible region here).

_(house style: proved / measured / expectation, each labelled.)_
