# Session 65 (C4) — the LMR cell resolved: rank, and orientation

Batch 10, wave 3.  **Gated on sessions 63 and 64 both landing.**  Do not start
this session until `docs/s63_report.md` and `docs/s64_report.md` are in the
repository and the integrator has reviewed them.  Base commit: whatever `main`
is at the time; name it in your pre-registration.

**Read `docs/batch10_worker_preamble.md` first**, then `docs/batch10_plan.md`
§4 (C4), `docs/lmr_cell.md`, and both gate reports in full.

## The question

At the LMR source `M_λ ≅ C²⁷⁴`, what is `U_P = ker T_pad` relative to
`U_D = ker T_det`?

## Why this is the session the batch exists for

`i_det = 1` is not `D > 0`.  `D = i_det − i_pad`, and with `i_det = 1` from
session 63 the whole question reduces to `i_pad`.  Compute, in the same
274-dimensional source:

    mult_pad ,  i_pad
    U_D = ker T_det ,  U_P = ker T_pad     (bases, not just dimensions)
    dim(U_D ∩ U_P)
    whether the known LMR determinant kernel line lies in U_P

## The decision table — all three outcomes are results

| outcome | reading |
|---|---|
| `i_pad = 0` | `D = +1`.  **The first multiplicity obstruction in the programme.** |
| `i_pad = 1` | `D = 0`.  Then test orientation: `U_D ≠ U_P` is a clean demonstration that the multiplicity statistic loses orientation exactly where geometry does not. |
| `i_pad ≥ 2` | `D < 0`.  The statistic points the wrong way despite a known geometric separator. |

**Success is any one of the three, exactly established.  Do not define success
as `D > 0`.**  The second and third are results about the limits of the
multiplicity statistic, which a GCT programme is obliged to report and which no
one has yet exhibited at a cell where a separator is known to exist.  Write the
report so that whichever outcome occurs reads as the finding it is.

## If `D > 0`

**Stop and invoke the verification protocol before reporting it anywhere,
including in conversation.**  Second house prime, characteristic zero, an
independent construction of the source basis, an independent evaluation family,
and the degeneracy-direction pre-check at all three points of
`brief_wording.md` §5.  A first positive after 419 negatives is exactly the
circumstance in which a defect is most likely and most costly.

Note also what it would and would not prove.  It would be the first explicit
permanent-versus-determinant multiplicity obstruction in this programme.  It
would **not** prove Valiant's conjecture: the padded side imposes
`ℓ(λ) ≤ m² + 1`, and LMR's own family has `ℓ(λ(k,n)) = k + 3` with the census
forcing `k ≥ min(6, r−2)`, so rows grow with `n` and the family cannot scale.
State that in the report rather than leaving it to be inferred.

## Tasks

1. Re-derive `i_det = 1` from session 63's certificate rather than accepting the
   claim; you are the last check before it becomes load-bearing.
2. Extend session 64's calibrated `ev_pad` to `r = 9`, `δ = 24`.  If the cost
   curve says it does not reach, say so and stop — an honest wall is a
   deliverable and the reserve list has E1 for the analogous determinant case.
3. Compute `i_pad`, then the orientation quantities above.
4. Whichever branch of the table you land in, certify it in the declared format
   and state the prime or characteristic-zero status of every rank.

## Stopping rules

- If sessions 63 and 64 disagree about the source basis, stop.  Orientation is
  meaningless unless both kernels live in literally the same coordinates.
- Do not report `D > 0` before the verification protocol completes.

## Deliverables

`results/PREREG_s65.md`; `docs/s65_report.md` with the decision-table branch
stated in the first paragraph; kernel bases and the intersection computation as
artefacts; certificates for every rank; code under `analysis/wk10_s65_*.py`;
bundle `s65_orientation.bundle` + `.md5`.
