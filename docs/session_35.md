# Session 35 — record

Theory session on the onset window `delta in [9, 405]`, `ell >= 5`.
Branch `s35-theory` off clone tip `c02cee8` (ancestry gate `63fe705`
passed).  No session-35 collision found.  Single-writer files untouched;
no pushes; delivery by bundle.

## Order of work

1. Required reading (s33_review §4, e4_hunt, sweep62 §4–5, s30_review,
   l5_containment, singular_spaces, quiver_route, d5_ideal, s34_prompt,
   house failure classes).
2. `results/PREREG_s35.md` committed — the rubric, discard criteria, and
   the keep rule — before any direction was generated (`db40e1c`).
3. Day-one exact test battery (`analysis/wk9_s35_daytests.py`,
   `results/s35_tests.md`, commit `a270ebe`): catalecticant ranks at
   `r = 4, 5`; the extremal weight-`(10,10,10,6)` 9-minor exact over `Z`;
   sigma_2-scheme length 20; nodality Hessians; `(R/J)_7` at det vs
   k-general-nodal controls; `I(D_5^pad)_{<=4} = 0` exact.
4. Focused literature checks: nodal-threefold factoriality criterion
   (Cheltsov; Clemens/Cynk/Werner chain), DIP multiplicity-obstruction
   paper (setting + technique), IP rectangular-Kronecker pointer, defect
   references (Rams/Cynk).
5. Deliverable `docs/theory_directions.md`: seven directions ranked by the
   pre-registered rubric; top two developed in depth with their first
   tests run and banked.

## The two banked results

- `D((10,10,10,6,0), 9) <= -1`: first proved multiplicity difference in
  the programme (pad side bites, expected direction).  Pad onset pinned to
  `[5, 9]`.  Soft link: principality of `I(D_4^det)` (named; one-cell
  direct measurement removes it — recommended as s36's first act).
- `D_5^det` = 20-nodal with defect exactly 1 (non-Q-factorial); the
  `(R/J)_7 = 31 vs 30` fingerprint with clean k-nodal controls; det onset
  cap `405 -> <= 300` (expectation pending one literature statement + one
  transversality page).

## Failure-class hygiene

Lowest-invariant bias: the catalecticant results were *tested* against the
forced prediction from `e >= 10` (T1r4) rather than assumed to transfer.
Regime transfer: the degree-9 pad equations live at `ell = 4`; nothing
here claims the `ell = 5` onset is 9 (bracket stated as `[5, 9]` for the
total ideal only).  Shared-spec correlation: the defect covariants vanish
on *both* varieties and are reported as cap-movers, not separators.
Quotient blindness: the banked cell is a multiplicity statement with an
exhibited function, not a dimension-count inference.

## Session-arithmetic note

One code bug (per-factor integer division in the Giambelli print: 18)
caught the same hour by the independent Hilbert-function measurement (20);
fixed before any use, recorded in the ledger and the deliverable.

## Recommended next acts (for the integrator to reassign)

1. One-cell `r = 4` measurement of `mult_det((10,10,10,6), 9)` — removes
   the principality soft link from the banked cell (cheap).
2. Direction 1(c): Koszul-homology route, validated against three banked
   s30 `mult_pad` values.
3. Direction 2: pin the degree-7 Milnor-defect statement; hunt the
   explicit degree-7 adjugate syzygy.
4. When s34's ledger lands: re-read its `delta = 7` pad rows against the
   `[5, 9]` bracket (its cells are `ell >= 5`; a pad bite there would date
   the `ell = 5` pad onset and unlock the `U_det` vs `U_pad` probe).
