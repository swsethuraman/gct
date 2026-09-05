# Session 39 — the long-weight occurrence screen (`ℓ = 6..10`) and one-bit tests

Branch `s39-longweights` off `e9cb8dd` (the s36 merge).  Ancestry gate
`git merge-base --is-ancestor 48bbdc3 HEAD` passes; `docs/s36_review.md`
present.  No session-39 collision (only `docs/s39_prompt.md` was in the tree).
Delivery: `longweights.bundle`, single ref `s39-longweights`.

## What this session did

The programme's first direct screen of the long-weight region at `n = 4` —
weights of six or more rows — for an occurrence obstruction
(`mult_det = 0 < mult_pad`) or a forced multiplicity drop (`a > m_det ≥ 1`),
the two things arithmetic alone can certify.  It extends s38's length-5
occurrence screen (`results/occurrence_screen.md`) upward in length, into the
region where the `n = 3` ideal was first pinned (`docs/d5_ideal.md` §0).

## Headline results

1. **Permanent-sensitive region bounded on all four sides.**  A *permanent-
   specific* obstruction can live only at `a ≥ 1`, `λ_1 ≥ δ`, `6 ≤ ℓ(λ) ≤ 10`.
   The new bound this session is **`ℓ ≤ 10`** (`docs/longweight_hunt.md` §1, from
   the integrator's addendum): the padded permanent is concise in ten variables,
   so `P_r ⊆ Sub_{10}` and `mult_pad = 0` for every `ℓ ≥ 11`.  With `ℓ ≤ δ` from
   Pieri, the permanent-sensitive long-weight region is `6 ≤ ℓ ≤ min(δ, 10)`.
   **The lower bound `ℓ ≥ 6` is where the permanent first *enters* (washout_lemma
   Thm 6), not a proof that no obstruction exists at `ℓ ≤ 5`** — corrected in
   session 49.  At `ℓ ≤ 5`, washout gives `D = mult_R − mult_det`: an obstruction
   there would be a statement about *reducibility*, not the permanent.  `ℓ ≤ 4`
   is closed by containment (`D ≤ 0` proved, `docs/r4_containment.md`); `ℓ = 5`
   is closed only because it was *measured* (`D ≤ 0` at the nine s27/s30 cells
   and s38's exhaustive occurrence screen), `R_5 ⊆ D_5` being open.

2. **The occurrence route is silent — an exhaustive negative.**  All **79,255**
   weights with `6 ≤ ℓ ≤ 10`, `λ_1 ≥ δ`, `δ = 8..12` were screened; of the
   **69,967** with `a ≥ 1`, **0** are one-bit (`a=1, m_det=0`) and **0** are
   forced (`a>m_det`).  Every cell has `a ≤ m_det`, not narrowly: the balanced
   extreme has `m_det` outrunning `a` by orders of magnitude (δ=12:
   `a=87,405` vs `m_det=4.8×10⁸`), and the tightest cell anywhere is the peaked
   `(4δ−10, 2^5)` (ℓ=6, `a=1, m_det=13`, **margin 12 at every δ**, never
   closing).  So no occurrence obstruction and no forced multiplicity drop lives
   at lengths 6–10; any separation there would be a genuine multiplicity
   phenomenon (`mult_det < a ≤ m_det`), invisible to arithmetic — exactly s38's
   length-5 finding, now extended to 6–10 with the gap *wider* (margin grew from
   7 at ℓ=5 to 12 at ℓ=6).  Pre-registered **P2 confirmed**; Phase 1 had no cell
   to test.

3. **The `n = 3` precedent is explained away, not transferred.**  Its one-bit
   cells sat at `ℓ = 8, 9 ≈ n² = 9`; at `n = 4` that edge is near `ℓ = 16`,
   outside the pad-eligible `ℓ ≤ 10`.  Inside `ℓ ≤ 10`, `m_det` is large (the
   tightest cells are the peaked `(4δ−8, 2^{ℓ−1})` families, `a = 1`,
   `m_det ≥ 13`, margin growing with `ℓ`).

## Validation done before any result

- **P1 (reduction reproduces s36):** `(8,4,4,4,4)` d6, `(11,4,4,4,1)` d6,
  `(13,8,4,1,1,1)` d7 reproduced exactly (a, N_S, |Stab|, n_χ, mult_det,
  mult_pad) at both primes; `l^3 m` witness kernel `(12,−3,1)`.
  `results/s39_validation.md`.
- **The `m_det` engine** (`analysis/wk9_s39_chars.c`, written from the rule,
  independent of the house python) reproduces the house `chi`/`a`/`m_det`, the
  `n=3` anchors (`Σ m_det = 3,11,43`), the s28 `δ=10` precedent cells
  (`a=1, m_det=0`), and **s38's full length-5 table at δ=5..9** — the brief's
  "validate against s38's length-5 table before extending", and simultaneously
  the second independent `m_det` implementation the obstruction protocol
  requires.  `results/logs/s39_chars_selftest.log`.

## Deliverables

`results/PREREG_s39.md`, `results/longweight_screen.md` (+`.csv`),
`results/onebit_ledger.md`, `results/s39_validation.md`,
`docs/longweight_hunt.md`, this record; code
`analysis/wk9_s39_{chars.c,chars.py,screen.py,onebit.py,validate.py,publish.py}`;
logs under `results/logs/`.  Per-cell CSVs under `results/s39_screen/`.

## The window as left

- Occurrence route: **silent** at `6 ≤ ℓ ≤ 10` across the completed `δ` range.
- Obstruction window (proved bounds): `a ≥ 1`, `λ_1 ≥ δ`, `6 ≤ ℓ ≤ 10`.
- Open, untouched by this session: the **multiplicity** route at `6 ≤ ℓ ≤ 10`
  (`mult_det < a ≤ m_det`), which needs a rank, not arithmetic — the natural
  successor (the reduction reaches `n_χ ≈ 15,500`; the peaked cells are cheap,
  `n_χ = 200`).
- Coverage: **exhaustive** — 100% of the eligible region (`δ=8..12`,
  `6 ≤ ℓ ≤ min(δ,10)`, `λ_1 ≥ δ`), candidate count = banked count at every
  chunk.  Not reached, by theorem not budget: `11 ≤ ℓ ≤ 16` (`mult_pad = 0`);
  `δ ≥ 13` (pre-registered stop, a stable `δ`-family with no expected boundary).
- Independent verification (`results/s39_verify.md`): the `m_det` engine's `a`
  re-confirmed against the house plethysm and a character-free reduced kernel at
  `δ=10,11,12`; `m_det` against the house at `δ=10` and by its exact invariants
  at `δ=11,12`; the classification invariant `a ≤ m_det` holds on all 69,967
  cells.  **VERIFICATION PASS.**
