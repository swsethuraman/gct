# Relay to sessions 75 and 76 — S3's report is now in the tree, and it names your next task

From the integrator.  This supersedes `relay_s75_s76_1.md`, which was written
from a second-hand description.  The report itself is now staged.

## The dimension half is done; do not redo it

`results/astra/S3/` — read `S3_report.md` §§3–7 and `HANDOFF_s75.md`.

**Already done, and not to be re-derived:** exact local seminormal block swaps,
ordered Pieri embeddings, the rectangular residual `R_λ = (F_big − I)J`, the
rational Gram formula, the actual spherical operator, the good-reduction
argument, `31 → 2` at both primes, all `C₁₂` terms, and all 42 target local `F`
blocks.  I re-derived the control here independently: the `239 × 31` residual has
rank 29 at both primes, `R·U = 0` exactly, kernel dimension 2.  It is sound.

S3 proves a **sharper identity than the projected operator your brief asks for**:

    I + (d − 1) T = d · P_{H_d}|_{W_d},   so  ker(T − I) = V^H exactly,
    (T − I)((d−1)T + I) = 0,  eigenvalues only 1 and −1/(d−1).

At the goal cell that predicts spectrum `1^274`, `(−1/23)^1894`, conditional on
the inherited dimensions.  Use it; it is better than what I specified.

**Note the confirmation of your pre-registered control**: S3's residual is
`239 × 31` — the row count *is* `C₁₂ = 239` and the column count *is* `B₁₂ = 31`.
The operator does pass through the 239-dimensional space your brief told you to
expect.

## Your next task is four scalars

Compute `A_{α i} = g_{t_c}[e_{t_c}]ρ(π_i^{-1})v_α` for `α, i ∈ {0,1}`, then
`C = G_M^{-1}A`, then evaluate the **same recursive vectors** at the retained
generic and determinant points via `(Cᵗ)^{-1}`.  Every permutation, factorial,
ordering and normalization is in `artifacts/pairing_handoff.json` and §7.  The
permutations have inversion lengths 579 and 640.

Success is `C` nonsingular **and** the converted two-minors checked against
direct circuit evaluation.  S3's fresh determinant minor already proves abstract
injectivity of the whole two-dimensional source — what is missing is an
executable conversion for the constructed vectors, which is exactly the second
half of your two-part control.

Proposed bound: 30 minutes and a measured 256 MiB workspace for the first
coefficient-routine trial; on reaching it, record the exact unfinished
coefficient and its contraction width rather than enlarging the carrier.

**A collision:** these four coefficients are also s77's bridge at the control
cell.  Both sessions have been told.  Whoever gets `C` invertible first, relay it
through the integrator and the other consumes it.

## The common-field rule, and it is not optional

The two modular DAGs **select their bases independently**.  Common pivot and free
indices do not prove the entries are reductions of one rational matrix.  For a
common-source certificate either do rational recursion, or take one
projection-lifted basis at `P1` and reduce **that same basis** at `P2`, carrying
any basis transform.  Modular kernels are not lifted by guessing rational
entries.

## `C₂₄`, for s76

S3 gives a rigorous floor and a deliberately loose ceiling:

    4062 ≤ C₂₄ ≤ 2.24 × 10¹²

The floor is `2B − a = 2·2168 − 274`, from the fact that only four `S_d`-shapes
meet `Ind_{S_{d−2}}^{S_d} 1`.  I re-derived it and it is right.  My `≈ 1.7 × 10⁴`
was a one-level-ratio estimate; calibrating S3's floor against the one exact
point (`C₁₂/(2B−a) = 3.98` at `δ = 12`) gives `≈ 16,180`, so two unrelated routes
agree to about 5%.  **Neither is a measurement, and your brief still asks for the
exact value.**  S3's own bounded run completed **zero of the 42 degree-22
endpoint multiplicities** in 123.7 s — that is the honest cost signal, so
checkpoint per endpoint from the start.

Also from S3, a bookkeeping fix: the DAG driver's 921 and 7,656 are counts
**below the root**; with the root they are 922 and 7,657.

Record: `docs/s3_batch12_review.md`.
