# Session 36 — record

Compute session: the stabiliser reduction at general weights, then the
first six-row cells.  Branch `s36-stabred` off clone tip `5367c75` (ancestry
gate `c02cee8` passed; `docs/s35_review.md` present).  No session-36
collision.  Session 34 had not landed (its `delta = 7, ell = 5, N_S <= 11269`
domain left alone).  Single-writer files untouched; no pushes; delivery by
bundle (insurance bundles posted to the conversation at ~4 h intervals).
Container: 7 GB, 2 cores; `python-flint` 0.9.0 for every rank.

## Order of work

1. Required reading (s35_review, e4_hunt §4, sweep62, sweep62 ledger,
   s34_prompt, s33_review §2) and the s30/s33 code.
2. `results/PREREG_s36.md` committed before any measurement (`8aa3ef6`):
   lemma stated with proof, P1–P4, exact sweep order, kill criteria, the
   `(10,10,10,6)` cell sized and declared out of reach (`n_chi = 111508`).
3. Validation battery (`analysis/wk9_s36_validate.py`,
   `results/stabred_validation.md`): all four parts pass; discriminating
   counts quoted (7 cells × every candidate character; 41/48).
4. Reduced census (`results/s36_census.md`) published, then the sweep
   (`analysis/wk9_s36_sweep.py`, claim queue, memory guard waits): 91 cells
   banked with a commit each (`results/s36_ledger.md`).
5. Each pad bite: sceptical branch in-run, then `wk9_s36_bite.py`
   (independent symbolic point families) and `wk9_s36_exact.py` (exact
   integer HWV; Bruhat proof of vanishing on the reducible locus).
6. Post-hoc, labelled: the point-free `mult_red` (`wk9_s36_red.py`), the
   `delta = 5` onset check (`wk9_s36_onset5.py`), the `a = 1` extension
   (`wk9_s36_aone.py`).
7. `docs/stabiliser_reduction.md`: lemma, two proofs, pipeline, porting
   note, validation, findings, honest boundary, coverage, scorecard.

## Banked

- The lemma `P_w v = chi_lam(w) v`, `chi_lam = prod sgn^{m_B}`, proved two
  ways and validated against unreduced kernels per character.
- 91 cells, `D <= 0` everywhere, `mult_det = a` everywhere (`a` up to 21).
- Five `D = −1` cells, all proved equations of the reducible locus via (★):
  a HWV vanishes on `{l · c}` iff every monomial misses some `x_i` for every
  `i`.  Automatic when `lam_1 < delta` (the Kadish–Landsberg padding bound).
- `I(D_5^pad)` begins at `delta = 5` (the degree-5 invariant `I_5`; s35 had
  `I(D_5^pad)_{<= 4} = 0`, so the onset is exactly 5); `I(D_6^pad)` begins at
  `delta = 6` (`I_6`).  `(8,4,4,4,4) = c I_5`, `(12,4,4,4,4) = c^2 I_5`;
  `(9,9,8,1,1)`, `(8,8,8,2,2)` new degree-7 generators.
- `ell = 6`: 34 cells, `mult_pad = mult_red` at all — no permanent-specific
  equation through `delta = 7` in any component reached.

## Not done / boundary

- `mult_det((10,10,10,6), 9)` not measured (out of reach by ~48×).
- Frontier `n_chi ~ 15500`; 4 cells above it left unmeasured and named.
- Nothing about the permanent; the det side is untouched through `delta = 7`.
