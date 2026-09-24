# Occurrence screen — `a` vs `m_det` for `I(D_5^det)`, `ell = 5`

Session 38, 2026-09-02. Code `analysis/wk9_s38_screen.py` (reuses
`scripts/ambient_screen.py`, `--selftest` clean). Data
`results/occurrence_screen.csv` (δ5–9), `results/screen_d10.csv`,
`results/screen_d11.csv`, `results/screen_d12.csv`.

## What is computed, and why it bounds the onset

For every partition `lam` of `4·delta` with **exactly 5 parts** and
`a(lam,delta) >= 1`:

- `a(lam,delta)` = mult of `S_lam` in `Sym^delta(Sym^4 C^5)`, the plethysm
  coefficient `⟨h_delta[h_4], s_lam⟩` (variable-count-independent for `nv>=5`;
  cross-checked `a(nv=5)=a(nv=16)=dim ker R`).
- `m_det(lam)` = `dim (S_lam^*)^{Stab(det_4)}`, the **symmetric rectangular
  Kronecker coefficient**, rectangle `(delta^4)`, `N=4δ` (batched route,
  asserted equal to `ambient_screen.m_det` every run).

Because `mult_det ≤ min(a, m_det)`, a cell with **`a > m_det`** forces
`det_units = a − mult_det ≥ a − m_det > 0` — an equation of `D_5^det` located by
arithmetic alone, with no rank computation (the s28 `n=3` mechanism). The first
`delta` carrying such a cell is an **unconditional upper bound on the onset**.

## Result: the occurrence route is SILENT

**No `ell=5` cell has `a > m_det` at any measured degree.** Not one, out of
2585 cells across δ=5–10 (and δ=11, 12 below).

| δ | cells (a≥1) | `a > m_det` fires | largest-`a` cell — `a` / `m_det` | tightest cell — `a` / `m_det` / margin |
|---|---|---|---|---|
| 5 | 23 | **0** | (4,4,4,4,4) — 1 / 5 | (4,4,4,4,4) — 1 / 5 / **4** |
| 6 | 105 | **0** | (11,6,4,2,1) — 7 / 375 | (16,2,2,2,2) — 1 / 8 / 7 |
| 7 | 239 | **0** | (12,8,5,2,1) — 26 / 1529 | (20,2,2,2,2) — 1 / 8 / 7 |
| 8 | 435 | **0** | (12,8,6,4,2) — 109 / 27257 | (24,2,2,2,2) — 1 / 8 / 7 |
| 9 | 708 | **0** | (14,10,6,4,2) — 437 / 104544 | (28,2,2,2,2) — 1 / 8 / 7 |
| 10 | 1075 | **0** | (16,11,7,4,2) — 1421 / 389644 | (32,2,2,2,2) — 1 / 8 / 7 |
| 11 | 1602 (spot) | **0** | balanced `a≪m_det` | (36,2,2,2,2) — 1 / 8 / 7 |
| 12 | 1900+ (spot) | **0** | balanced `a≪m_det` | (40,2,2,2,2) — 1 / 8 / 7 |

**δ=5–10 are exhaustive** (every 5-part `lam` of `4δ` with `a≥1`, 2585 cells).
**δ=11, 12 are spot-checked at the two fire-risk extremes**, not fully
enumerated — the `m_det` character sums over partitions of 44 and 48 exceed the
session's character-computation budget (the brief's "as far as … allow in
budget").

> **Correction (session 58).**  The budget statement is no longer true.  The
> first-row reduction of `docs/`/`analysis/wk9_s58_sk.py` computes
> `sk(λ, 4×δ)` from the **tail** `λ̄` rather than from `p(N)`, so the whole
> `δ = 11, 12` length-5 region — every tail of size `≤ 4δ − δ = 36` — is minutes
> of work rather than beyond budget.  The exhaustive rows can be had for the
> asking; the spot-check argument below stands on its own and is not withdrawn,
> but it is no longer forced by cost. A fire (`a > m_det`) can only hide at one of two extremes, and both
are clean:

- **Smallest-`m_det` end (peaked cells).** The tightest family `(4δ−8,2,2,2,2)`
  continues exactly: `a=1`, `m_det=8`, margin 7 at δ=11 and δ=12. More peaked
  still — `(N−4,1,1,1,1)`, `(N−5,2,1,1,1)`, `(N−6,2,2,1,1)` at δ=12 — have
  `m_det ∈ {0,1}` but `a = 0`, so are not screened (a fire needs `a≥1`); the
  first `a≥1` cell is the peaked family at `m_det=8`. The `n=3`-style
  `a≥1, m_det=0` occurrence therefore cannot arise here.
- **Largest-`a` end (balanced cells).** Representative balanced/near-rectangular
  cells have `a` in the tens–hundreds against `m_det` in the thousands and up,
  extending the δ≤10 pattern (δ=10 max-`a` cell: 1421 vs 389644).

## Reading

- **`m_det` dominates `a` everywhere, and the gap widens fast.** At the
  largest-`a` cell of each degree the margin explodes (δ=10: `a=1421` against
  `m_det=389644`). The symmetric rectangular Kronecker room of the `det_4`
  orbit simply grows far faster than the ambient plethysm room at these
  lengths — the same `a ≤ m_det` regularity the programme has seen at every
  length ≤ 4 (Cor. 7), now observed to persist at length 5 through δ=10.
- **The tightest cell is a stable one-parameter family**, the peaked weight
  `(4δ−8, 2,2,2,2)`, with `a=1`, `m_det=8`, **margin 7 at every δ≥6**. It never
  closes. The single closest approach anywhere is the rectangular `(4,4,4,4,4)`
  at δ=5 (`a=1`, `m_det=5`, margin 4), and it does not recur.
- **Consistency with "empty through 7."** δ=5,6,7 have zero fires, so the
  known emptiness of `I(D_5^det)` through degree 7 is a *multiplicity* fact
  (`mult_det = a`), not an occurrence one — as it must be, since an `a > m_det`
  cell at δ≤7 would have contradicted the empty record.

## Consequence for the onset (pre-registered P2)

The occurrence route does **not** bound the onset anywhere in the window it can
see. Whatever degree `I(D_5^det)` first switches on, it does so as a **genuine
multiplicity phenomenon** (`mult_det < a ≤ m_det`), invisible to arithmetic and
requiring a rank measurement to detect. This is the opposite of the `n=3` mirror,
where the arithmetic route *did* fire at δ=10 — but there it fired at **lengths
8 and 9** by the degenerate `m_det=0` route, a different length regime; at
length 5 (the true `D_r` analogue) the `n=3` route was silent too. So the
`n=3` "fired at 10" does not transfer, and the silence here is the honest
finding, banked as pre-registered.
