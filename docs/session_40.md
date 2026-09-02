# Session 40 — record

Theory session: the onset conjecture, the `n = 3` twin, three write-ups.
Branch `s40-onset` off `e9cb8dd` (main, the s36 merge).  Ancestry gate
`git merge-base --is-ancestor 48bbdc3 HEAD` passed; `docs/s36_review.md`
present.  No prior session 40 in the tree.  Single-writer files untouched;
no pushes; delivery by `onsetconj.bundle` (single ref `s40-onset`).
Pre-registration `results/PREREG_s40.md` committed first (`d8a50f2`).

## Order of work

1. Required reading (theory_directions §C, blindness_slab, d5_ideal,
   paper_section4_draft, s35/s36/s37/s38 reviews, stabiliser_reduction,
   e4_hunt §4, paper 1's length-theorem subsection and Question 8.5).
2. `results/PREREG_s40.md`: expected statements and falsifiers per
   deliverable; the prior on the conjecture recorded as low-to-moderate.
3. Exact checks (`analysis/wk9_s40_*.py`, logs under `results/logs/`):
   - `wk9_s40_cap.py`: `cap(n)`, `ν(n)`, the GN Hilbert function; the
     identities `H_J(2n−5) = ν−1`, `H_J(2n−4) = ν`, `H_J(n) = codim`, `ν −
     H_J(n) = C(n−1,4)`, `cap = 5n(n−1)²(7n−8)/12` proved symbolically.
   - `wk9_s40_jacobian.py`: corank of `M_{3n−5}` at fresh pencils, `n = 3..7`:
     `6/31/102/256/541` vs smooth `5/30/101/255/540`; controls; minor-ideal
     Hilbert functions = GN in every degree; saturated `def_{2n−5} = 1` and
     `def_n = 0, 0, 1, 5, 15` at `n = 3..7`; both primes (`n = 7` run as the
     verification step).
   - `wk9_s40_jacobian_n3t.py`: the Milnor row `10,10,6,6,6,6` at `n = 3`.
   - `wk9_s40_frame.py`: the six nodes of an explicit determinantal cubic
     are a projective frame (exact over `Q`); 30 independent node conditions
     at the standard frame.
   - `wk9_s40_n3census.py`, `wk9_s40_n3cells.py`: the `n = 3` census
     (`δ = 8..12`, 1748 cells) and the det-side runs (gates passed; `δ = 8`
     all 60 cells with `n_χ ≤ 5000`, `δ = 9` all 49 with `n_χ ≤ 2500`, the
     degree-10 invariant cell, then `δ = 8` cells up to the bundling time) —
     every cell `mult_det = a`; three ledger cells re-measured unreduced with
     a fresh seed as a spot check (`s40_spotcheck_d8.log`), same values.
4. Deliverables: `docs/onset_conjecture.md`, `docs/paper1_delta0_patch.md`,
   `docs/reducible_ideal.md`, `results/n3_length5_plan.md`.

## Results in one paragraph

The cap theorem holds at every `n ≥ 2` with one formula, `cap(n) =
5n(n−1)²(7n−8)/12 = 5, 65, 300, 900, 2125, ...`, proved modulo Kleiman
(adopted), Dimca (adopted, pinned by s37) and Gulliksen–Negård (adopted);
the defect step is now proved at every `n` (the GN Hilbert function of the
minor ideal in degree `2n − 5` is `ν(n) − 1`), and the mechanism was
measured fresh at `n = 5, 6, 7` where nothing had been looked at.  Paper 1's
bracket becomes `8 ≤ δ_0 ≤ 65`.  The `n = 5` anomaly is explained
(`codim = ν − C(n−1,4)`; the nodes fail forms of degree `n` from `n = 5` on;
`D_5^{det_n}` is a superabundant component of the `ν`-nodal locus) and does
not touch the cap.  Bonus: `D_5^{det_3}` is the closure of the cubics
singular at six points in linearly general position, answering the first
sub-question of Question 8.5.  (★) is a theorem for every `n, r, δ` and
every padding exponent `k`, with Kadish–Landsberg's bound as its automatic
case; the onset of `I(R_r)` for quartics is 5 for all `r ≥ 5` (s36's
"`I(D_6^{pad})` begins at 6" corrected to "its length-6 part begins at 6").
The conjecture `onset = cap(n)` is stated, proved at `n = 2`, and survives
121 empty cells at `δ = 8, 9` and the degree-10 invariant at `n = 3`.

## Pre-registration scorecard

- P1.1 (cap theorem provable modulo Kleiman/Dimca): **held**, with GN as one
  more adopted piece for the general-`n` defect step (routes (a), (b) need
  it only at `n ≥ 5`).
- P1.2 (defect at every `n` via GN; identity `H(2n−5) = ν − 1`): **held**,
  symbolically and at `n = 3..7` numerically; measured `dim J_{2n−5}` never
  below the GN value.
- P1.3 (`n = 3` corank 6 at fresh pencils): **held** (3 pencils, both primes).
- P1.4 (conjecture; prior low-to-moderate): untested beyond silence; every
  cell run was empty, including the invariant cell.  Prior unchanged in
  kind, slightly raised in degree.
- P1.5 (`n = 5` anomaly reading; `h^0(I_N(5)) = 77`): **held** (77 at two
  pencils; coranks 102, 256 and 541 as predicted at `n = 5, 6, 7`).
- P2.1: written.  P2.2 (frame theorem): **held** (rank 30; frame at the
  explicit pencil).
- P3.1–P3.3: theorem written with the general `k`; literature verdict as
  predicted (technique standard, statement not found); the `I(R_6)`
  onset phrasing corrected.
- P4.1–P4.3: census built; gates passed; 122 cells run (72 at `δ = 8`, 49 at
  `δ = 9`, the invariant at `δ = 10`), all empty (P4.3's prediction held at
  every cell).

## Process notes / honesty

- One house-rule breach: a `pkill -f wk9_s40_frame.py` was used to stop a
  slow sympy rank computation; it matched the calling shell and killed it
  (exit 144).  No data was lost (the background runs were untouched and
  the census had finished), but the rule (`pkill -f` banned; kill by PID
  read back) exists for exactly this reason and was broken once.  Recorded.
- The first frame-check attempt used sympy's rational rank on a `315 ×
  126` matrix and did not finish in ten minutes; replaced by flint
  `fmpz_mat` (under a second).  No result depended on the aborted run.
- The census enumerates `n_χ` exactly only where `N_S ≤ 250000`; 20–25% of
  the cells at each `δ` carry the lower bound `N_S/|Stab|` marked `~` —
  all of them above the frontier regardless.
- Directions of promotion are stated everywhere: ranks at points bound
  generic ranks below; dimensions of linear systems through a point set
  bound the generic value above.
- Nothing here is about the permanent.  The det-side cap and the `n = 3`
  runs are permanent-independent; no obstruction claim of any sign is
  made.

## What next (for the integrator to reassign)

1. Place the paper patch; decide on the optional Question 8.5 paragraph.
2. A compute session on `results/n3_length5_plan.md`: finish `δ = 8` (24
   fitting cells), then `δ = 9, 10` — each empty cell is weak evidence, one
   bite pins `δ_0`.
3. Paper 2 material: Theorem 1 at general `n`, the `n = 5` anomaly, and
   the GN/stabiliser remark (`2n² − 2` linear syzygies = the infinitesimal
   stabiliser).
4. The `n = 4` analogue of the invariant test: `(8^5)` at `δ = 10` under
   the reduction (`|Stab| = 120`), the unique candidate invariant cell
   below the frontier.
