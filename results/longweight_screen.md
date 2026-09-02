# Long-weight occurrence screen — `a` vs `m_det`, `6 ≤ ℓ(λ) ≤ 10`, `n = 4`

Session 39, 2026-09-02.  Code `analysis/wk9_s39_screen.py` on the exact
C Murnaghan–Nakayama engine `analysis/wk9_s39_chars.{c,py}` (validated:
`results/logs/s39_chars_selftest.log` — house `chi`/`a`/`m_det`, the `n=3`
anchors, the s28 `δ=10` precedent, and s38's length-5 table δ 5–9).  Data:
`results/longweight_screen.csv`.  This screen EXTENDS s38's length-5
`results/occurrence_screen.md` to lengths 6–10 (rows 11–16 excluded by
theorem — see the region statement).

## What is computed, and the eligible region

For every `λ ⊢ 4δ` with `6 ≤ ℓ(λ) ≤ min(δ,10)` and `λ_1 ≥ δ`:

- `a(λ,δ)` = plethysm `⟨h_δ[h_4], s_λ⟩` (ambient room; `mult_det, mult_pad ≤ a`).
- `m_det(λ)` = symmetric rectangular Kronecker coeff, rectangle `(δ^4)`,
  `= (1/2)[g(λ,(δ^4),(δ^4)) + T(λ)]` (`mult_det ≤ m_det`), computed only when `a ≥ 1`.

The eligible region for an occurrence obstruction (`mult_det = 0 < mult_pad`)
or a forced multiplicity drop is bounded, all proved: `a ≥ 1`
(BIP silent at `(3,4)`); `λ_1 ≥ δ` (Kadish–Landsberg via (★),
`docs/stabiliser_reduction.md`); `ℓ ≥ 6` (`ℓ ≤ 5` cannot see the permanent,
`docs/washout_lemma.md`); `ℓ ≤ min(δ,10)` — `ℓ ≤ δ` since every constituent
of `Sym^δ(Sym^4)` has `≤ δ` rows, and **`ℓ ≤ 10`** because the padded
permanent is concise in 10 variables, so `P_r ⊆ Sub_10` and `mult_pad = 0`
for `ℓ ≥ 11` (`results/PREREG_s39.md` §0, proved).  Rows 11–16 are excluded
by that theorem, not by budget.

## Classification

- **one-bit**: `a = 1, m_det = 0` — det side zero for free; pad side a single evaluation.
- **forced**: `a > m_det ≥ 1` — det loses `a − m_det` for free; pad-side rank `≥ m_det+1` certifies an obstruction.
- **silent**: `a ≤ m_det` (no arithmetic bite).

## RESULT: the occurrence route is SILENT at every length 6–10 across the completed region

**No cell has `a = 1, m_det = 0` and no cell has `a > m_det`.** Every cell
with `a ≥ 1` has `a ≤ m_det` — the determinant's symmetric rectangular
Kronecker room dominates the ambient plethysm room at lengths 6–10 just as
s38 found at length 5.  So no occurrence obstruction and no forced
multiplicity drop lives at `6 ≤ ℓ ≤ 10` in the region screened; any
separation here would have to be a genuine multiplicity phenomenon
(`mult_det < a ≤ m_det`), invisible to arithmetic.

## Coverage by `(δ, ℓ)`

“cells” = candidates with `a ≥ 1`; `a = 0` candidates are not cells.
A chunk is COMPLETE iff its `.done` marker exists; else PARTIAL (banked/candidates).

| δ | ℓ | candidates | banked | cells (a≥1) | one-bit | forced | tightest `m_det−a` (λ) | status |
|---|---|---|---|---|---|---|---|---|
| 8 | 6 | 681 | 681 | 591 | 0 | 0 | 12 (`(22, 2, 2, 2, 2, 2)`) | complete |
| 8 | 7 | 779 | 779 | 561 | 0 | 0 | 17 (`(20, 2, 2, 2, 2, 2, 2)`) | complete |
| 8 | 8 | 768 | 768 | 327 | 0 | 0 | 20 (`(18, 2, 2, 2, 2, 2, 2, 2)`) | complete |
| 9 | 6 | 1160 | 1160 | 1079 | 0 | 0 | 12 (`(26, 2, 2, 2, 2, 2)`) | complete |
| 9 | 7 | 1433 | 1433 | 1256 | 0 | 0 | 17 (`(24, 2, 2, 2, 2, 2, 2)`) | complete |
| 9 | 8 | 1512 | 1512 | 1125 | 0 | 0 | 20 (`(22, 2, 2, 2, 2, 2, 2, 2)`) | complete |
| 9 | 9 | 1421 | 1421 | 671 | 0 | 0 | 20 (`(20, 2, 2, 2, 2, 2, 2, 2, 2)`) | complete |
| 10 | 6 | 1874 | 1874 | 1793 | 0 | 0 | 12 (`(30, 2, 2, 2, 2, 2)`) | complete |
| 10 | 7 | 2491 | 2491 | 2330 | 0 | 0 | 17 (`(28, 2, 2, 2, 2, 2, 2)`) | complete |
| 10 | 8 | 2793 | 2793 | 2460 | 0 | 0 | 20 (`(26, 2, 2, 2, 2, 2, 2, 2)`) | complete |
| 10 | 9 | 2773 | 2773 | 2074 | 0 | 0 | 20 (`(24, 2, 2, 2, 2, 2, 2, 2, 2)`) | complete |
| 10 | 10 | 2533 | 2533 | 1318 | 0 | 0 | 17 (`(22, 2, 2, 2, 2, 2, 2, 2, 2, 2)`) | complete |
| 11 | 6 | 2902 | 2902 | 2817 | 0 | 0 | 12 (`(34, 2, 2, 2, 2, 2)`) | complete |
| 11 | 7 | 4123 | 4123 | 3955 | 0 | 0 | 17 (`(32, 2, 2, 2, 2, 2, 2)`) | complete |
| 11 | 8 | 4902 | 4902 | 4593 | 0 | 0 | 20 (`(30, 2, 2, 2, 2, 2, 2, 2)`) | complete |
| 11 | 9 | 5116 | 1356 | 900 | 0 | 0 | 20 (`(28, 2, 2, 2, 2, 2, 2, 2, 2)`) | PARTIAL 1356/5116 |
| 11 | 10 | 4882 | 0 | 0 | 0 | 0 | — | PARTIAL 0/4882 |
| 12 | 6 | 4337 | 0 | 0 | 0 | 0 | — | PARTIAL 0/4337 |
| 12 | 7 | 6561 | 0 | 0 | 0 | 0 | — | PARTIAL 0/6561 |
| 12 | 8 | 8235 | 0 | 0 | 0 | 0 | — | PARTIAL 0/8235 |
| 12 | 9 | 9018 | 0 | 0 | 0 | 0 | — | PARTIAL 0/9018 |
| 12 | 10 | 8961 | 6741 | 5724 | 0 | 0 | 17 (`(30, 2, 2, 2, 2, 2, 2, 2, 2, 2)`) | PARTIAL 6741/8961 |

Totals across banked rows: **33574 cells (a≥1), 0 one-bit, 0 forced.**

_(generated 2026-09-02 16:51 UTC by `analysis/wk9_s39_publish.py`)_
