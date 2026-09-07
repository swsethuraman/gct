# Pre-registration — session 64 (batch 10, wave 2, C3): the padded side in the source coordinates

Branch `s64-padded` off `main` at `226b4ef1` (ancestry gate passed:
`git merge-base --is-ancestor 226b4ef1 HEAD`). Written and committed before the
calibration sweep. Labels: **proved** / **measured** / **adopted** / **expectation**.

## 0. Object and question

`D = mult_pad − mult_det = i_det − i_pad`. The determinant and reducible sides
have an instrument (`analysis/wk9_s60_cell.py`):

    mult_det = a − nullity_Q [E; ev_det]      det_4 pencils
    mult_red = a − nullity_Q [E; ev_red]      l . (generic cubic)

with `E` the stacked simple raising operators on the `chi_lam`-isotypic
reduction (`analysis/wk9_s45_build.py`, unchanged). This session adds the one
missing family, in the SAME coordinates and the SAME `E`:

    mult_pad = a − nullity_Q [E; ev_pad],   ev_pad at  l(s) . per_3(A(s)).

**The deliverable is calibration, not a measurement of the LMR cell.** No LMR
cell is attempted (stopping rule S5).

## 1. Architecture claim, to be confirmed in the first hour (Task 1)

**(adopted → to verify)** The common-source architecture the batch plan asks
for already exists. Specifically:

- **(A1)** `E` depends only on `(lam, delta, r)`, not on the evaluation family,
  so the same `E` and the same dense highest-weight kernel serve det, red and
  pad. *Confirm:* one kernel, three point matrices.
- **(A2)** The padded points live in the right ambient. `ev_pad` at
  `l(s).per_3(A(s))` in `Sym^4 C^r` is exactly the TRUE padded permanent
  `PAD34 = per_padded(3,4) = x_0.per_3(x_1..x_9)` in `Sym^4 C^10`
  (`analysis/wk8_s30_core.per_padded`, `analysis/pad.py`) restricted to a
  generic `r`-plane: `restrict(PAD34, 10, 4, r, V)`. *Confirm:* `restrict(PAD34)`
  equals `l(s).per_3(A(s))` built from the frame by hand, at `r = 3..6`.
- **(A3)** The family is already in the repository: `wk9_s36_stabred.py`
  (`FORMS['pad'] = (PAD34, N_PAD)`) and `wk9_s45_cell.py` measured it via the
  general `ev_rows_arr`; session 60's dense engine wired only det and red. So
  the gap is one coefficient-dict producer plus wiring — smaller than the batch
  plan states, and needing no new Sol derivation.

If any of A1–A3 is wrong, that is reported immediately and the critical-path
assumption is corrected before anything else.

## 2. The containment the run must respect (primary calibration)

`R_r = {l.c}` contains the padded-permanent orbit closure, since `per_3` is one
cubic. Hence

    I(R_r) ⊆ I(pad)  ⟹  i_red ≤ i_pad  ⟹  mult_pad ≤ mult_red      (proved)

So at every cell where `mult_red` is banked, the measured `mult_pad` must satisfy
`mult_pad ≤ mult_red`. Likewise `R_r ⊆ D_r^{det_4}` (where it holds) gives
`mult_red ≤ mult_det`; the three sides are ordered `mult_pad ≤ mult_red ≤ mult_det`.

**(measured, this session, Task 4 premise)** At `r ≤ 5` the permanental cubics
`{per_3(A(s))}` fill all cubics (parametrisation rank = `dim Sym^3 C^r`), so
`P_r = R_r` and `I(pad) = I(R_r)`, giving `mult_pad = mult_red` **exactly**. At
`r = 6` the permanental family is strictly smaller (rank `50 < 56`), so only
`mult_pad ≤ mult_red`. This reproduces the transfer lemma (exact at `r ≤ 5`,
upper bound at `r ≥ 6`) from the cubic side and is verified in
`results/s64_calibration.md`.

## 3. Falsifiers and stopping rules

- **F1 (containment).** `mult_pad > mult_red` at any cell. This is a defect in
  the implementation, not a discovery; the run halts and the defect is found
  (stopping rule S2). Expectation: never fires.
- **F2 (r ≤ 5 exactness).** `mult_pad ≠ mult_red` at any `r = 5` cell where
  `mult_red` is banked. Since `P_5 = R_5`, the two engines must return the same
  number; a mismatch means the pad engine is wrong at exactly the calibration
  set (stopping rule S1: any unexplained mismatch stops LMR use). Expectation:
  never fires; equality at all measured cells.
- **F3 (prime / seed disagreement).** The two house primes, or two independent
  seeds, return different `mult_pad`. Random evaluation gives a *lower* bound on
  the true rank, so disagreement means undersampling or a bug; the margin
  `K − mult` is reported at every cell. Expectation: agreement, margin ≥ 6.
- **F4 (degeneracy direction).** The committed pre-check
  (`tools/verify/testset/degeneracy_check.py`, `brief_wording.md` §5) is run on
  the finished evaluator against the full ten-variable `l.per_3` (not a
  restriction). Recorded either way; the multiplicity route this engine uses is
  functorial (`brief_wording.md` §7: `I(D) ↠ I(P)`), so `i_pad ≥ i_det` is the
  containment that is being *tested*, not a wrong-direction defect — this is
  stated explicitly to avoid the trap §5 guards against.

**Stopping rules.**
- **S1** Any unexplained mismatch with a banked multiplicity stops LMR use
  immediately; reporting the mismatch is worth more than working around it.
- **S2** `mult_pad > mult_red` anywhere: halt, find the defect.
- **S5** Do not attempt the LMR cell (`r = 9`, `delta = 23, 24`) in this
  session. Calibration is the deliverable.

## 4. Regimes and method

- **Engine.** `analysis/wk10_s64_cell.py`: one `build_cell`, one dense flint
  kernel per prime (exact nullspace ≤ `exact_cap = 2500`, else the certified
  random compression, s41 semantics; every kernel vector verified on the full
  sparse `E`). Three sides as ranks of `T_side = ev_side · kern^T`;
  `i_side = a − rank`, `U_side = ker T_side` in the shared `a`-coordinates on
  `M_lam = span(kern)`. `python-flint` `nmod_mat` for every rank; two house
  primes `2147483647, 2147483629`; `≥ 2` independent seeds for each side.
- **Calibration set.**
  1. Low-degree / cheap dense `r = 5` cells across `delta = 6..9`, spanning
     balance from peaked to balanced.
  2. Every banked `r = 5` cell with `mult_red < a` (the discriminating cells,
     11 in session 60) — the only cells where the check is non-vacuous, since a
     cell with `mult_red = mult_det = a` cannot tell a correct pad engine from
     one that silently measures the determinant.
  3. `r = 3, 4` cells against the banked `mult_pad = a` values (s36 /
     `docs/visible_ideals.md`) and the low chain cells with `mult < a`.
- **Certificates.** Per calibration cell: `full_rank`-style point records
  (det pencil, reducible, padded-permanent in the `tools/verify` `linear_forms`
  layout) and the ideal-slice HWVs of each side expanded to monomial terms, so
  the verifier can recompute membership. Kernel bases `kern`, `U_det`, `U_red`,
  `U_pad` saved as machine-readable artefacts for session 65.
- **Discipline.** Bank each cell as it completes (append to
  `results/s64_calibration.jsonl`); logs under `results/logs/`; nothing over
  5 MB committed; delivery by single-ref bundle, no pushes.

## 5. What counts as success

Exact agreement `mult_pad = mult_red` at every banked `r = 5` cell (and
`mult_pad ≤ mult_red` at `r = 6`), including all discriminating cells; both
primes and ≥ 2 seeds agreeing with a stated margin; a passed/So-recorded
degeneracy pre-check on the full ten-variable object; kernel coordinates
preserved as bases; and a measured cost curve in `r` and `delta` with an honest
statement of where it stops relative to the LMR scale.

## 6. Claim ledger (to be filled by the report)

| claim | label |
|---|---|
| A1–A3 architecture reading | proved/measured (this session) |
| `mult_pad ≤ mult_red` (containment) | proved (Theorem 1, reducible_ideal) |
| `P_r = R_r` at `r ≤ 5`, `⊊` at `r ≥ 6` | measured (parametrisation rank) |
| `mult_pad = mult_red` at every measured `r = 5` cell | measured |
| degeneracy direction of the Macaulay statistic | measured (reproduces Prop D) |
| cost curve; LMR reachability by this route | measured / expectation |
