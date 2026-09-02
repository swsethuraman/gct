# Session 42 — the reducible-locus multiplicity engine (draft record; final numbers in docs/reducible_engine.md)

Branch `s42-redengine` on `5aa564b`; prereg `results/PREREG_s42.md` (bb406e0) before any measurement.

## What was built
- `analysis/wk9_s42_redengine.py` — mult_red = a − nullity(E_red); dense flint routes (exact / compressed rref-inplace) and the sparse route.
- `analysis/wk9_s42_wied.c` + `wk9_s42_sparse.py` — Wiedemann nonsingularity / kernel certificates over F_p (Berlekamp–Massey, verified kernel vectors, [E; R] certificate for the upper bound on nullity); self-test 200/200 with true nullities up to 55.
- `analysis/wk9_s42_orbits.py` — vectorised isotypic basis and raising-operator rows (validated: identical orbits up to sign, identical row spaces).
- `analysis/wk9_s42_hpad.py` — the normalisation bound h_pad (Pieri × cubic plethysm).
- `analysis/wk9_s42_census.py` — region census (symmetric-function plethysm at δ = 7, 8; Weyl alternation + tail DP at δ ≥ 9 with a dominance prefilter).
- `analysis/wk9_s42_sweep.py`, `wk9_s42_validate.py`, `wk9_s42_table.py`, `wk9_s42_lift.py`, `wk9_s42_detcert.py`.

## Findings (see docs/reducible_engine.md)
1. Route B computes the normalisation D = ⊕ Sym^δ V ⊗ Sym^δ Sym^3 V (= KL Prop. 1.8), not C[R_r]; R_r non-normal from degree 1; H^1(P, ξ) ≠ 0; output = h_pad ≥ mult_red, strict at 84/91 banked cells.
2. h_pad < a proves a bite with no rank: 411 of 1877 cells at δ = 7, 8; h_pad = 0 at 140 → mult_red = 0 proved → negative instances of Kadish–Landsberg Question 1.5 (n = 4, m = 3); four verified directly by the engine.
3. h_pad detects exactly 4 of the 5 s36 bites (misses c²·I_5).
4. The sparse certificate: mult_red = a proved in seconds–minutes at n_red ~ 10^4; same tool proves mult_det = a (demo: 5 s36 cells incl. a = 21 in ~70 s).
5. Two container resets survived by per-cell JSON banking.
