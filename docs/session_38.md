# Session 38 — where do the determinant's five-row equations begin?

2026-09-02. Branch `s38-onset` off `5367c75` (s35 review). Ancestry gate
`git merge-base --is-ancestor c02cee8 HEAD` passes; `docs/s35_review.md` present.
No session-38 collision. Delivery: `onset.bundle`, single ref `s38-onset`.
Pre-registration `results/PREREG_s38.md` (first commit, before any computation).

Target: the onset degree of `I(D_5^det)` — the first degree at which five-row
determinantal quartic threefolds acquire an equation. Window on entry `[8, 405]`.
This is det-side only and permanent-independent (at ℓ=5 the padded permanent is
washed out, `docs/s35_review.md` §1).

## Verdict in four lines

The occurrence route is **silent** over the whole window it can see (0 of the
2585 ℓ=5 cells at δ=5–10 have `a > m_det`, exhaustively; δ=11,12 clean at both
fire-risk extremes) — so the onset is a genuine multiplicity phenomenon, not an
arithmetic one. δ=8 is **empty on every reachable
cell** (27 of 43, `mult_det = a`, certified). The validation battery passes. The
window is left at `[8, 405]`, with the onset's *character* pinned even though its
degree is not.

## What was done, in order

1. **Flagged a missing dependency.** `docs/s36_prompt.md` and all session-36/37
   material are absent from the repo (no s36 commit, prompt, or code). The brief
   asked for an independent implementation of a session-36 lemma that does not
   exist. Recorded in `PREREG_s38.md` §0 and `docs/det_onset.md` §4; handled by
   reimplementing the *rectangular* reduction that is on record and, for general
   ℓ=5 weights, using the exact unreduced pipeline rather than an uncertified
   home-grown reduction.
2. **Pre-registered** P1–P3 and kill criteria before computing.
3. **Phase 0, the occurrence screen** (`analysis/wk9_s38_screen.py`,
   `results/occurrence_screen.md`): `a` (plethysm) vs `m_det` (symmetric
   rectangular Kronecker) for every ℓ=5 weight with `a≥1`. δ=5–10 exhaustive
   (2585 cells): zero `a > m_det`. δ=11,12 spot-checked at both fire-risk
   extremes (full enumeration over partitions of 44,48 exceeded the character
   budget): the peaked `(4δ−8,2,2,2,2)` family holds `a=1,m_det=8`, the
   `m_det∈{0,1}` cells have `a=0`, and balanced cells keep `a≪m_det`. `m_det`
   dominates `a` by orders of magnitude and the gap widens; the tightest cell is
   the stable family `(4δ−8,2,2,2,2)`, margin 7 at every δ≥6.
4. **Validation battery (P1) — PASS** (`results/s38_validation.md`): K1 witness
   kernel `(12,−3,1)`; rectangular `D_4^det` ladder rungs 4–8 (`a=1,0,1,1,3`,
   the odd-block sign cancellations at rungs 5,7); the nine banked δ=6 ℓ=5 cells
   (`mult_det=a`). The core primitives are the certified `wk8_s30_core.py`
   (corrected raising rule); rung 8 reproduced via the compressed route
   (`a=mult=3`, `n_chi=10738`).
5. **Phase 1, δ=8 rank measurements** (`analysis/wk9_s38_census.py`,
   `results/onset_ledger.md`): census by capped `N_S` counter (verified vs
   `monomials()`); 43 cells reachable unreduced (`N_S ≤ 9000`); the 27 with
   `N_S ≤ 5000` all measured `mult_det = a`, `det_units = 0`, two primes. No bite.

## Kill criteria — none fired

Validation passed (no stop). No `a > m_det` cell existed, so the "Phase-0 cell
fails to bite" kill was never triggered (there was nothing certain-to-bite to
pull forward). Memory-wall cells were reported as not-reached, never estimated.

## Process notes / honesty

- Two-core container; heavy jobs were serialised through a small file-flag
  orchestrator to avoid the OOM the `run62` memory model predicts
  (`7.5e-8·N_S²` GB; three OOM kills observed and worked around, not hidden).
- `a` carries two routes (plethysm `ambient_screen.a`, and `dim ker R` on the
  reachable cells); `m_det` batched == `ambient_screen.m_det` each run;
  `ambient_screen.py --selftest` clean.
- Insurance bundles taken during the run (`onset_insurance_1,2.bundle`).

## The window as left

**`[8, 405]`.** Onset degree not pinned; onset *character* pinned (multiplicity,
not occurrence). Next: build and validate a correct ℓ=5 stabiliser reduction to
reach the balanced `N_S > 9000` δ=8 cells and δ=9, then continue the ascent.

Bundle head: `93788413b80fbe4dc9a79ecc00dfc29147852931 (s38-onset tip at delivery; final bundle head is this commit's child)` (filled at delivery).
