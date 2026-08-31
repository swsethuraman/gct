# TOTAL at X_{-3}: the first test of the totals law at a negative gauge value

Session 23, 2026-08-31.  Branch `s21-xm3`.
Pre-registration: `results/PREREG_Xm3.md`, commit `b6ab472`, logged before any
value beyond the banked `f1Xm3_00` existed in this session.

**STATUS: IN PROGRESS.  Four of twelve values in.  The total is not yet
assembled and no verdict on Theorem 5.5 is stated here.**

Point: `X_{-3} = (x3+=x2, x4+=x1, x7+=x1, x8+=x0)`, i.e.
`A = E(0,2)+E(1,1)`, `B = E(1,1)+E(2,0)`; `Psi(X_{-3}) = -3`, re-derived here
from the substitution before anything was run.  Target:

    TOTAL(X_{-3}) = -3 x 1,152,144,000 = -3,456,432,000 .

## Values

| rep | weight | VALUE | / 151,200 | / 75,600 | states |
|---|---|---|---|---|---|
| 00 | 2 | +893,138,400 | +5907 | +11814 | 1 (banked, session 16) |
| 01 | 4 | −602,834,400 | −3987 | −7974 | 1 |
| 02 | 4 | −602,834,400 | −3987 | −7974 | 1 |
| 03 | 4 | −237,459,600 | **−1570.5** | −3141 | 1 |

Weighted so far: **−3,986,236,800** of a target −3,456,432,000, with weight 14
of 36 assigned.  The remaining eight representatives (weight 22) must supply
**+529,804,800**.

Note the direction has reversed twice.  After `00` alone the running sum was
`+1,786,276,800` and the rest had to be strongly negative; after `03` it has
overshot and the rest must come back up.  Nothing is concluded from this; it is
recorded because the X4 test had the same shape and the shape is what makes the
test demanding.

## Gate: the point symmetry — HIT

Pre-registered blind (commit `b6ab472`): `V01 = V02`, `V03 = V04`,
`V07 = V14`, `V09 = V16`, from a point symmetry derived independently and
validated against three banked points (it reproduces `C`'s and `R`'s recorded
`pi` and `rho`, and `X4`'s recorded assembly weights).

    V01 = V02 = -602,834,400    MATCH (exact)

The other three gates are queued.  **The assembly does not use the symmetry**:
the twelve representatives are the orbits of the point-*independent* scheme
automorphisms alone.

## REFUTATION: the 151,200 arithmetic signature is wrong — it is 75,600

Pre-registered prediction 4 was "every value is `151,200 x` an integer".  It
**MISSED**:

    f1Xm3_03 = -237,459,600 = -2^4 . 3^5 . 5^2 . 7 . 349
             = 75,600 x (-3141),   and  -237,459,600 / 151,200 = -1570.5 .

The run is clean — `final states 1`, and the `evalopts` checkpoint is keyed to
the input filename (`CKIN`), so a leftover checkpoint from the previous
subproblem in the same directory is rejected and the run restarts from scratch;
there is no cross-subproblem contamination.

Checking the claim against the whole banked record then turns up something that
was already there.  **`W(3-cycle) = +301,870,800 = 75,600 x 3993` is not a
multiple of 151,200 either** — `301,870,800 / 151,200 = 1996.5`.  It appears in
`results/results_f1C.md`, in `results/results_R.md`, and in the paper.

The gcd of all seventeen measured subvalues now on record — the five `W`-table
values, X4's eight, and X_{-3}'s four — is exactly

    75,600 = 2^4 . 3^3 . 5^2 . 7 ,

one factor of 2 below the claimed 151,200.

What was true, and remains true, is the narrower statement the README's own list
makes: the **ten** values it enumerates (cofactors 719, −2038, 5907, −4372,
4338, 3567, 3843, −5188, −258, −4552 — that is `W(id)`, X4's eight, and
`Xm3_00`) are all multiples of 151,200.  The sentence generalising that to
"every measured subvalue" is false, and was already false before this session
by the `W(3-cycle)` value sitting in the same table.

**Corrections required:** README ("Arithmetic signature"), the paper's
Remark `rem:arith`, and `PROJECT_NOTES` should read 75,600 and drop the
universal claim for 151,200, or restate it explicitly over the ten enumerated
values.  The totals are unaffected: `-3,456,432,000 = 75,600 x (-45,720)`.

This also sharpens `docs/primitivity.md`: if the engine normalisation is `m`
times primitive, the signature rescales with `m`, so the object to explain is
now `75,600` and not `151,200`.
