# Session 66 (C5) — the r = 5 special normal cone, at the primitive family

Batch 10, wave 3, **runnable now**.  The plan gates this on a Sol session
nominating a locus; the correction below already tells you which locus, so it is
not blocked.  Base commit `226b4ef1`.
**Read `docs/batch10_worker_preamble.md` first**, then `docs/batch10_plan.md`
§4 (S4, C5) and §5, `docs/rees_boundary_audit.md` **in full**,
`docs/s59_report.md`, and `analysis/wk9_s59_tangent.py`.

## The question

Is `R_5 ⊆ D_5`?  Equivalently — `R_5 ⊆ D_5 ⟺ dim(D_5 ∩ W) = 35`, and `≥ 31` is
certified over `Q`.  **An upper bound below 35 is a theorem, not a
measurement**, and this is the only route in the programme to one.

## The correction that defines this session

Three documents in this programme have stated that there are **four transverse
directions** at the compression incidence `C_21 ∩ C_32`, and that a CAS session
should adapt coordinates to 60 tangent plus 4 transverse variables and eliminate
the tangential ones.

**That four is zero.**  Measured, with every spanning vector verified to
annihilate `dΦ` (`docs/rees_boundary_audit.md`, method in §5 there):

| point | `dim ker dΦ` | span of component tangents | transverse quotient |
|---|---|---|---|
| generic point of `C_21 ∩ C_32` | 64 | 57 + 57 → **64** | **0** |
| generic point of `C_21` alone | 57 | 57 | **0** |
| generic point of `ker ∩ coker` | 75 | 75 | **0** |

The erroneous 60 came from counting fixed-flag tangents (`5 × 10 = 50` per
component); the flag motion in `Gr(2,4) × Gr(1,4)` supplies the missing 7 each.

**There is no transverse complement to eliminate.**  If you find yourself
writing a coordinate change that separates 60 tangential from 4 transverse
variables, you have reconstructed the wrong version from an older document —
stop and re-read the table above.

A second consequence, and it makes a banked number better rather than worse:
with `ker dΦ = T C_21 + T C_32`, the "genuinely mixed" second-order direction
`M_1 = u + v` is **not** special — every kernel direction is such a sum — so the
reducible image dimension 27 is the value at a generic second-order-solvable
point of the incidence, not at an exotic one.

## Where to look instead

**The primitive family and its incidences.**  This is what the boundary audit
itself ranked third and what survives its own correction.  It is the genuine
analogue of the `n = 3` skew-symmetric component that Hüttenhain–Lairez show
generic compression analysis provably misses, and it is the **only base-locus
type at `r = 5` where nobody has yet looked for a transverse direction**.  The
compression world has produced no exotic first-order direction at any point
tested.

The audit's `n = 3` calibration argument — that compression analysis provably
misses a real boundary component there — is untouched by any of the above and is
the reason to fund this track rather than more compression work.

## Tasks

1. Construct the primitive family at `r = 5` explicitly and characterise its
   incidences with the compression components.  Session 59's machinery
   (`wk9_s59_tangent.py`, `wk9_s59_order2.py`, `wk9_s59_orderq.py`) computes
   `dΦ` by dual numbers on the 70 coefficients of `det(Σ s_i A_i)` and builds
   tangent spans as images of `δP·B_i + B_i·δQ + δB_i`; reuse it.
2. At a generic point of the primitive locus, measure `rank dΦ`, `dim ker dΦ`,
   the span of the tangent spaces of the components through the point, and the
   **transverse quotient**.  Verify every spanning vector annihilates `dΦ`, as
   the audit did — that check is what caught the error above.
3. If a transverse direction exists, form the quadratic obstruction ideal on it,
   compute radical and minimal primes, and measure the reducible image dimension
   of every component against the certified 31 and the target 35.  Singular,
   msolve and Macaulay2 are all available; `analysis/wk9_s61_*.sing`, `.m2` and
   `docs/s61_review.md` §7 record the discipline, including the trap that cost
   session 61 an afternoon: **bind a `sat` result to a named list before
   `std`** — inline `std(sat(I,P)[1])` silently returns a wrong ideal.
4. If the primitive locus is exhausted with quotient 0 as well, move to the next
   incidence in the audit's order and say so.  Recording that the compression
   *and* primitive worlds both produce no exotic first-order direction is a real
   strengthening of the negative, not a failure.
5. Keep in view what a spanning tangent cone does and does not settle: **a
   normal cone can carry components that no tangent space sees.**  "The tangent
   cone spans" does not close the loophole; the quadric system and its minimal
   primes remain a legitimate object.  What is unavailable is the coordinate
   reduction, because there is no complement.

## Stopping rules

- **No generic `q > 4` sweep.**  Session 59 measured `29, 29, 28, 28, 24`
  invariant in `q` at `q = 2, 3, 4`; higher contact order at a generic point is
  a closed route.
- No broad brute-force Rees algebra.
- Bound every CAS run at launch and record the process id, per the preamble.
  Primary decomposition is where this session will spend its time; time-box it
  and report partial minimal primes rather than extending.

## Success

A dangerous hidden component found — or this special-normal-cone loophole
rigorously closed at the primitive family, which is the last base type where it
could hide.

## Deliverables

`results/PREREG_s66.md`; `docs/s66_report.md`; the measured tangent table in the
same shape as the one above, for every point tested; CAS inputs and outputs
under `analysis/wk10_s66_*` with logs under `results/logs/`; code; bundle
`s66_primitive.bundle` + `.md5`.
