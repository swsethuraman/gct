# Integrator review — session 41 (the six-row frontier)

2026-09-03.  Branch `s41-sixrow`, delivered head `98a0abe` (44 commits on
`5aa564b`; prereg `4051730` before any measurement; the report's `b2b1f9c`
plus one cleanup commit — logs moved under `results/logs/`, no data
changed).  Single-writer files, `.gitignore` and the shared s30/s36 modules
untouched; nothing over 5 MB.  The session's own claims are the det-side
"empty" verdict at 37 new cells, one new pad-side bite, and the frontier
lift; I checked each by a route the session did not use.

## 1. Verification

- **Every ledger row rebuilt.**  `a` (Kostant alternation) and `m_det`
  (Murnaghan–Nakayama) reproduce at all 37 rows; no duplicate cells; the
  stabiliser orders, `D = mult_pad − mult_det`, `mult_pad ≤ mult_red ≤ a`
  and `a ≤ m_det` hold on every row.  `mult_det = a` at all 37 — and this
  direction is exact: full rank of the evaluation matrix over `F_p` forces
  full rank over `Q`, so the 90 "empty" verdicts are theorems given honest
  determinant points and correct highest-weight vectors.
- **The bite `(13,10,6,1,1,1)`, δ=8, a=9.**  The session's two mod-p
  vanishing vectors (28,248 monomials, both primes) pass my checks with the
  house convention: weight, (★) on every monomial, all five simple raising
  operators zero mod p, zero at true padded-permanent points, nonzero at det
  pencils and a generic quartic.  A mod-p vector proves only `mult_red ≥ 8`,
  so I ran session 42's lift (`analysis/wk9_s42_lift.py`, branch `s42-redengine`
  at `1538f56`) at this cell: 117 s, one integer highest-weight vector,
  max coefficient 1,280, `E v = 0` over ℤ.  Expanded and audited
  independently (weight, (★), raising operators over ℤ, zero at 8 pad
  points, nonzero at 4 det pencils and a generic point), and proportional
  mod `2147483647` to the session's vector — same support.  Hence
  `mult_red ≤ 8` proved, `mult_pad ≥ 8` proved (rank at 51 points), so
  **`mult_pad = mult_red = 8`, `mult_det = 9`, `D = −1` is proved**, not
  measured.  Certificate: `results/s41_cells/13_10_6_1_1_1_d8_cert_chi.txt`.
  Note the normalisation bound does not see this bite (`h_pad = 9 = a`),
  exactly as at `(12,4,4,4,4)_7`; the lift is the only proof.
- **Phase 0b coverage counted.**  Length-6 constituents of
  `Sym^δ(Sym^3 C^6)`: 27 weights at δ=7 (all `a=1`), 91 at δ=8 (Σa = 139),
  by my cubic plethysm.  Phase 0b measured 20 and 28 of them (`mult = a`
  at all, the `a` values agree with mine); the 7 and 63 unmeasured are
  exactly the doc's honest-boundary numbers, and the one measured cell whose
  transport weight `(9,4,3,2,2,1)` is unmeasured is correctly flagged.
- **Cross-route validation** is in the record: the in-place kernel route
  reproduces the exact and compressed routes' *kernel spans* (not just
  multiplicities) at both primes on the six s36 δ=6 cells and on three
  banked ℓ=6 cells including the discriminating `(10,8,7,1,1,1)` `D=−1`.
- **Session 42's bound applied to session 41's cells:** `mult_red ≤
  min(a, h_pad)` holds at all 37; no violations.

## 2. What the result establishes — and one sentence to change

At every one of the 90 measured six-row cells (δ = 6, 7, 8; `n_χ ≤ 19,985`)
the determinant has no equation: the six-row determinant ideal is zero on
the measured set.  Since `D > 0` needs `mult_det < a`, no obstruction was
possible there and none appeared; `D ≤ 0` everywhere, `D = −1` at three
reducibility bites, `mult_pad = mult_red` at every cell (forced by the
transport theorem at 89 of 90).  The frontier moved from `n_χ ≈ 15,500` to
`≈ 20,000` at 4.7 GB.

The sentence to change is "the six-row onset is bracketed `≥ 9` in reach".
An onset is a property of a degree, and δ=7 is 20% measured (52 of 258
eligible cells), δ=8 4% (22 of 591); 6 + 43 eligible cells *inside* the
frontier were left unmeasured for time, and everything measured is peaked
(long first row).  The defensible statement, for paper 2: *no six-row
determinant equation occurs at any of the 90 measured cells of degree ≤ 8;
the balanced cells, where a low onset would sit, are unmeasured.*  Likewise
"`I(R_6)` gained a degree-8 generator" should read "has a degree-8 element in
a new weight" — the certificate does not show it is outside the ideal
generated in lower degree.

## 3. Standing after session 41

The multiplicity route at ℓ = 6 is open above the frontier, not closed
below it.  Cheap next work, in order: the 49 reachable-unmeasured cells
(one long session at 15–40 min each); s42's engine as the pad side
(a lookup, and the lift for any bite); the seven δ=7 Phase-0b weights above
`n_χ = 6,000` (would make `I(D_6^{per_3})_7 = 0` a full theorem and force
`mult_pad = mult_red` in every weight of degree 7 by Prop. 8(1)).  The
balanced corner needs a second reduction axis or a six-row cap theorem.

## 4. Process

Prereg first, census before measurement, `a` by two routes asserted equal at
849 census cells, kernel spans validated before use, one process per cell
with the true peak recorded, per-cell commits through two suspensions and
one out-of-memory event with no cell lost.  The report's `docs/s41_prompt.md`
carries the pre-`brief_wording.md` vocabulary; it is history, left as is.
