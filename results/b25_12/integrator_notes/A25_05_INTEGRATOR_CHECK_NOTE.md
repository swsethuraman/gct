# Integrator check note — A25-05

**For intake by the B25-12 coordinator.** Integrator (Claude, Cowork), 2026-09-21. **Not a review;
accepts nothing.** A25-10 governs. The packet stays UNCOMMITTED / NOT RELEASED.

Checked against `work/batch15/docs/a25_05_report.md` as staged from the user's machine, sha256
`c254bbf71e6f255558edc400a55b5973077f95b8172a66fd848952cfb3458671` (13,118 B). Supporting files
(`STRUCTURAL_MAP.md`, `PADDING_FIBERS.md`, `FIVE_CENTER_REDUCTION.md`, `NEXT_CERTIFICATE.md`) were
**not** read.

## INDEPENDENT EVALUATOR — exact, by `a25_05_integrator_check.py` (sympy; seconds)

| claim (report §) | computed | status |
|---|---|---|
| `dim J_m = 15m − binom(m,2)` = 42, 54, 65 for m = 3, 4, 5 (§1) | 42, 54, 65; omitted 28, 16, 5 | **exact** |
| padding-fibre kernel `dim = [t³](1+t)^(m−r)/(1−t)^(5−m)` (§2) | matches at (m,r) = (3,3), (4,4), (5,5), (5,2), (5,3), (4,2), (3,1) | **exact at all seven** |
| invisible cubic spaces 4, 1, 0 when `l` is nonzero at every selected center (§2) | 4, 1, 0 | **exact** |
| injectivity at five centers once `l` is nonzero at ≥ 3 centers (§2) | kernel 0 at r = 3; 1 at r = 2 | **exact** |
| `z·per[a d e; d b f; e f c] − det diag(z, [a d e; −d b f; −e −f c]) = 2x₁x₂x₃x₄` for arbitrary linear `a, b, c` (§2) | verified with fully general linear forms | **exact** |

The six-term identity is the most consequential of these: it shows this actual-padding family has
an exact determinant completion modulo a squarefree quartic, which lies in the five-dimensional
omitted space `K_5` at every m ≤ 5. **It kills A25-04's integer witness `T` in the five-center ring
in every degree**, as the report states. Note that `T` comes from A25-04, which is itself still
unreviewed — a dependency between two unreviewed packets that A25-10 should see together.

Consistency check, by hand: the product locus `{l·C}` has affine dimension `5 + 35 − 1 = 39`, and
subtracting the fibre dimensions 4, 1, 0 gives 35, 38, 39 — matching the report's proved
product-locus dimensions.

## Not checked

§3's 33-parameter / 48-coordinate reduction and the four affine 22-planes; the diagonal-plus-rank-one
claim that every `Σ b_i q_i` is an actual determinant; §4's differential-rank bound `≤ 39 < 42`;
anything conditional on C_PER or Dubé Cor. 8.3.

## The timing exception

The report discloses a **7h25m56s** interval between clock checkpoints (`04:26:41Z → 11:52:37Z`)
with no instrumentation, and states that compliance with the 90-minute theory ceiling is
**unverified**. It did not relabel the interval, and stopped research on observing it. That is the
correct handling and should be recorded as a **timing-control exception**, not resolved by
inference.

In local time the gap runs from about 00:26 to 07:52 EDT — overnight, which is consistent with the
host machine sleeping. **The integrator does not assert that.** Only the user can attest whether
the machine was idle; if so, that attestation should be recorded *beside* the exception, not in
place of it.

## One planning item for the coordinator

A25-10 was scoped for A25-01, A25-02 and B25-04. A25-03, A25-04 and A25-05 have since been added,
and A25-05 depends provisionally on A25-04. That review is now roughly twice its original scope and
contains a dependency chain among unreviewed packets; it should be re-scoped or split before
launch.
