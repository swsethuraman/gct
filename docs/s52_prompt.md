# Session 52 — The `a = 1` census: where the statistic is lossless, and what that costs

## 0. Standing constraints

- Deliver by git bundle only.  Do not push.
- Do not edit `paper/det3-conductor.tex`, `paper/det4-onset.tex`,
  `PROJECT_NOTES.md`, or `docs/boundary_deficit.html`.  Those have a single
  writer.  If you believe one is wrong, say so in your report.
- Commit messages carry a `Co-Authored-By` trailer only.  No session-link
  trailer, in commits or in any script that commits.  No `claude.ai/...` URL in
  any file you write.
- Bound every run with `timeout` and `ulimit -v`.  Record the process id to
  `results/logs/<run>.pid` and end a run only by that recorded id.  Do not
  select processes by name pattern.
- No committed file over 5 MB.  Logs under `results/logs/`.  Config is
  append-only.
- Pre-registration first: state what will be measured and what would count as a
  positive result before running it.  Bank the result per cell.
- `python-flint` only for exact linear algebra.
- Any cell reporting `D > 0` goes through the verification protocol before it is
  written down as a claim.
- Before developing any statistic meant to characterise determinant type, run
  the degeneracy-direction pre-check in `docs/brief_wording.md` §6.

## 1. The argument for `a = 1`, stated precisely

With `i_X = dim I(X)^{HWV}_{λ,δ}`, `a = a(λ,δ)`, `mult_X = a − i_X`:

    D = mult_pad − mult_det = i_det − i_pad.

A multiplicity obstruction can fail for a reason that has nothing to do with the
varieties being close: `dim U_D = dim U_P` with `U_D ≠ U_P` gives `D = 0` even
though the ideals are genuinely different subspaces.  The statistic discards the
orientation of the subspace and keeps only its dimension.

**At `a = 1` that failure mode is impossible.**  The highest-weight space is a
line, so `i_det, i_pad ∈ {0,1}` and equal dimensions forces equal subspaces.
These are also our cheapest cells: `i_det ∈ {0,1}` is decided by a single
non-vanishing check on one vector, not by a rank computation on a large matrix.

## 2. The argument against `a = 1`, which must be stated too

At `a = 1`, `D > 0` requires `i_det = 1`, `i_pad = 0`, that is `mult_pad = 1`
and `mult_det = 0`: the weight occurs on the pad side and not at all on the
determinant side.  That is exactly an **occurrence obstruction**.

Two facts from the literature, to be recorded in the report before any compute:

1. **Bürgisser–Ikenmeyer–Panova** (arXiv:1604.06431; FOCS 2016; *J. Amer. Math.
   Soc.* **32** (2019), 163–193) prove occurrence obstructions do not exist — but
   Theorem 1.4 requires `n ≥ m^25`.  At `n = 4`, `m = 3` that hypothesis is not
   remotely met and the theorem says nothing about our regime.  Confirm this
   reading against the paper.  Then the harder question: does their **mechanism**
   — the argument producing a determinant-side weight from every padded-permanent
   weight — depend essentially on heavy padding, or does some form survive at
   `n = 4`?  A short argument either way is worth more than the census below.
2. **Ikenmeyer–Panova**, *Multiplicity obstructions are stronger than occurrence
   obstructions* (ICALP 2019).  At `a = 1` a multiplicity obstruction *is* an
   occurrence obstruction, so restricting to `a = 1` gives up precisely the
   strength gap between the two notions.  That is the real cost of the `a = 1`
   prior and it should be stated plainly: we buy losslessness against orientation
   by giving up the strictly stronger of the two obstruction notions.

**Task 0 is to resolve point 1.**  If the mechanism transfers to `n = 4`, this
session's result is a proof that the cheapest lossless route is closed — a good
outcome, retiring a direction for one session's cost.  Only if it does not
transfer does the census proceed.

## 3. The census

The integrator has already counted, with an independent implementation:

- `δ = 7`: **64** cells with `a = 1`, of 258 eligible.
- `δ = 8`: **45** cells with `a = 1`, of 591 eligible.
- `δ = 9`: not counted — the enumeration exceeded a ten-minute bound.

For `δ = 9` use a better enumeration, not a longer bound.  `a(λ,δ)` is a Kostant
alternation over interlacing `ν`; the enumeration over `ν` is what blows up and
can be pruned by `|ν| = |λ| − δ` before the alternation runs at all.

Extend to `δ = 9` and, if affordable, `δ = 10`.  Record per cell: `λ`, `δ`,
`ℓ(λ)`, `a`, `h_pad`, and whether `mult_pad > 0`.  Cells with `h_pad = 0` are
theorems of Corollary B2, not measurements — mark them and exclude them from any
count of informative cells.  (Session 47 was refuted partly because `h_pad = 0`
cells were counted as evidence.)

## 4. The measurements

At each `a = 1` cell with `mult_pad > 0`, decide `i_det ∈ {0,1}`.  The space is
one-dimensional, so this is a single question: is the unique highest-weight
vector of weight `λ` in the ideal of `D_r`?

Do the cheap direction first — a non-vanishing evaluation at a single determinant
pencil proves `i_det = 0` immediately.  Only cells surviving every evaluation
need exact treatment.  Order the work by cost.  Record `i_pad` at the same cells;
that side is the `h_pad` computation and is cheap.

## 5. Calibration against the existing record

Our reconciled six-row record covers 193 cells and reports `i_det = 0` at every
one.  The prior going in is that `i_det = 0` here too.  The reason to run the
census is not that `a = 1` cells are more likely to fire — it is that if one
fires, the result is not degraded by the orientation problem.  State this
honestly.  Do not present the `a = 1` restriction as raising the chance of a
separation.

## 6. Success and failure

**Success:** a resolved answer to Task 0, or a measured `a = 1` record across
`δ = 7, 8, 9`.

**Surprise worth stopping the batch for:** any `a = 1` cell with `i_det = 1`.
That is an occurrence obstruction at `n = 4`; verify it twice — once by the
session-49 verifier and once by exact arithmetic over `ℤ` — before writing it
down as a claim.

**Negative worth having:** a demonstration that the BIP mechanism transfers to
small `n`.  That closes the occurrence route on grounds better than measurement.

## 7. Report

`docs/s52_report.md` with the Task 0 determination first, then the census table,
then the measurements.  Deliver as a bundle.
