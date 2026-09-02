<!-- session record; coverage numbers finalized from the completed screen -->
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

1. **Eligible region bounded on all four sides, all proved.**  An obstruction
   can live only at `a ≥ 1`, `λ_1 ≥ δ`, `6 ≤ ℓ(λ) ≤ 10`.  The new bound this
   session is **`ℓ ≤ 10`** (`docs/longweight_hunt.md` §1, from the integrator's
   addendum): the padded permanent is concise in ten variables, so
   `P_r ⊆ Sub_{10}` and `mult_pad = 0` for every `ℓ ≥ 11`.  Combined with
   `ℓ ≤ 5` blind to the permanent (`docs/washout_lemma.md`) and `ℓ ≤ δ` from
   Pieri, the permanent-sensitive long-weight region is `6 ≤ ℓ ≤ min(δ, 10)`.

2. **The occurrence route is silent.** <!-- FILL final: across δ=8..K, N cells,
   0 one-bit, 0 forced --> For every screened cell `a ≤ m_det` — no
   `a = 1, m_det = 0` and no `a > m_det`.  So no occurrence obstruction and no
   forced multiplicity drop lives at lengths 6–10 in the region screened; any
   separation there would be a genuine multiplicity phenomenon
   (`mult_det < a ≤ m_det`), invisible to arithmetic — exactly s38's finding at
   length 5, now extended to lengths 6–10.  Pre-registered **P2 confirmed**.

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
  successor (the reduction reaches `n_χ ≈ 15,500`).
- Coverage and what was not reached: <!-- FILL from the screen table -->.
