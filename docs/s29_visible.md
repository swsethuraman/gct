# Session brief — s29: where the ideals become visible

**Branch `s29-visible`.**  Measurement lineage (25 → 27).  Exact arithmetic, no
engine.  Goal: produce the programme's **first strict multiplicity inequality**,
pin the degree of the determinantal-quartic hypersurface, and run the first
non-vacuous subspace comparison.

## 0. Standing orders

- Rule 9: fresh clone, container only, new files only.  Do **not** touch
  `paper/det3-conductor.tex` (the X_-3 grind owns it), `PROJECT_NOTES.md`, or
  `docs/boundary_deficit.html`.
- **Ancestry, not equality**: `1203fe4` must be an ancestor of `origin/main`.
  Commits above it are expected (the s27/s28 merges and integrator files may or
  may not have landed — every fact you need is inline here).
- Pre-register (`results/PREREG_s29.md`) and commit BEFORE computing.
  Calibration battery (`analysis/wk6_s26_regress.py` if present, else the
  numbers in §3) before trusting anything.  Push likely refused; deliver a
  bundle.
- **Do not touch the 62 open cells at `delta = 6`, `ell >= 5`** — session s30
  owns those.  Your cells are length-4 and rectangular ones only.

## 1. Context, self-contained

At `n = 4`: session 27 proved `D_4^{per_3^pad} ⊆ D_4^{det_4}`
(`ell.c = det_4 diag(ell, M)`), so at every weight of length `<= 4`,
`mult_pad <= mult_det` — i.e. `D <= 0`.  All 19 measured cells at `delta = 5`
gave `mult = a` on both sides (`D = 0`, ideals invisible).  Also measured:
`a((delta^4), delta) = 0,0,0,1,0,1,1,3` for `delta = 1..8`, `mult_det = a = 1`
at `delta = 4`, so the determinantal hypersurface `D_4^{det_4} = {F = 0}` has
degree `e >= 6`.  `D_4^pad` (the reducible quartics `ell.c` in 4 variables) has
codimension **12**, so its ideal is large — yet no element of it has ever been
seen in an isotypic slice.

**Every `D` the programme has ever measured is 0.**  This session's job is to
find the cells where that stops — which the containment theorem guarantees
exist on the pad side — and to look at the ideals themselves, not just their
dimensions.

## 2. The work

**A. First strict inequality.**  Find the cheapest weights (any `a >= 1` —
`a = 1` cells are cheap and legitimate here) of length `<= 4` at
`delta = 5, 6, 7` where `mult_pad < a`.  By containment `mult_det >= mult_pad`,
so any such cell with `mult_det = a` gives the first strict `D < 0`.
`D_4^pad` has codimension 12; its ideal must appear at modest degree.  Sweep by
ascending weight-space size.  **State plainly in the record**: `D < 0` says
nothing about separating permanent from determinant (it is the wrong
direction); its value is calibration — the first proof the machinery can see an
ideal at all, and the raw material for C.

**B. Pin `e`** (session 27's unfinished item 4): measure `mult_det((6^4), 6)`.
Weight space ~12,000 in `Sym^6(Sym^4 C^4)`; `a = 1`, so one bit.  If the
degree-6 invariant vanishes on `D_4^{det_4}`, `e = 6`; else `e >= 7` (then try
`(7^4)`, `a = 1`).  Use row-subsampling with the `rank(R) = N_S − a`
self-check; a rank attaining `a` is a certificate, and `mult < a` needs the
kernel exhibited and double-checked mod a second prime.

**C. The subspace protocol.**  At every cell from A where BOTH ideals are
nonzero (`mult_det < a` and `mult_pad < a`), compute the ideal slices as
explicit subspaces `U_det, U_pad ⊆ C^a` (kernel bases from `[R;E]`
elimination over two primes, rationally reconstructed if small), and test
`U_det ⊆ U_pad` — which containment PREDICTS.  Report dimensions AND the
containment verdict.  This is the dress rehearsal for the length-5 version:
**"equal multiplicities, different ideals"** is the sharpest form of the
question why multiplicity methods fail, and this session builds the tool that
detects it.

## 3. Calibration (reproduce first)

    a((6,6,6,6), 6) = 1 ;  a((delta^4),delta) row = 0,0,0,1,0,1,1,3
    session 27's five s26 cells and the 19-cell table: mult = a everywhere
    the containment direction: at ell <= 4, mult_pad <= mult_det ALWAYS -- a
    single violation means your orientation or evaluation is wrong: STOP.

## 4. Pre-registration

1. Predicted first degree and weight where `mult_pad < a` at length 4.
2. Predicted `e` (6 or 7+), with a falsifier.
3. Predicted verdict of `U_det ⊆ U_pad` (it must hold if the theorem and the
   code are both right — treat any failure as a bug first, a discovery second).

Integrator's priors: `mult_pad < a` appears by `delta = 6` at some length-4
weight; `e = 6`; the containment check passes.  Low-to-moderate confidence.

## 5. Kill criteria

- Any cell with `mult_pad > mult_det` at `ell <= 4`: **bug**.  Stop.
- `U_det ⊄ U_pad` at a verified cell: stop, re-derive both kernels
  independently; if it survives, the containment proof or the evaluation
  convention is wrong and everything downstream pauses.
- If no `mult_pad < a` exists through `delta = 7`: report the sweep range and
  stop — that itself would mean the reducible locus's ideal starts remarkably
  late, worth knowing.

## 6. Deliverables

    results/PREREG_s29.md      first
    docs/visible_ideals.md     the strict-D cells, e, the subspace verdicts
    docs/session_29.md         record, ledger, honest boundary
    analysis/wk8_s29_*.py      sweep, rank, kernel/subspace comparison
