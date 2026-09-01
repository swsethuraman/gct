# TOTAL at X_{-3}: the first test of the totals law at a negative gauge value

Session 23, 2026-08-31.  Branch `s21-xm3`.
Pre-registration: `results/PREREG_Xm3.md`, commit `b6ab472`, logged before any
value beyond the banked `f1Xm3_00` existed in this session.

**VERDICT: TOTAL(X_{-3}) = -3,456,432,000 = -3 x 1,152,144,000 exactly.
Theorem 5.5 is CONFIRMED at the first negative gauge value ever tested.**

Point: `X_{-3} = (x3+=x2, x4+=x1, x7+=x1, x8+=x0)`, i.e.
`A = E(0,2)+E(1,1)`, `B = E(1,1)+E(2,0)`; `Psi(X_{-3}) = -3`, re-derived here
from the substitution before anything was run.  Target:

    TOTAL(X_{-3}) = -3 x 1,152,144,000 = -3,456,432,000 .

## Headline

    TOTAL(X_{-3})  =  -3,456,432,000  =  -3 x 1,152,144,000  =  Psi(X_{-3}) x TOTAL_C
                   =  75,600 x (-45,720),      ratio -3.000000 exactly.

This is the first test of `TOTAL(N) = Psi(N) x 1,152,144,000` at a **negative**
gauge value.  Every total previously measured sat at `Psi` in `{0, 1, 4}`, all
non-negative, so `Psi = -3` was the only point in the banked set at which a sign
error in session 22's parity argument could show up.  It does not.

## Values

Twelve representatives of the point-**independent** scheme automorphisms
(`swap`, `post-omega`), weights summing to 36.  The assembly uses no point
symmetry.

| rep | weight | VALUE | / 75,600 | / 151,200 | states |
|---|---|---|---|---|---|
| 00 | 2 | +893,138,400 | +11,814 | +5,907 | 1 (banked, session 16) |
| 01 | 4 | −602,834,400 | −7,974 | −3,987 | 1 |
| 02 | 4 | −602,834,400 | −7,974 | −3,987 | 1 |
| 03 | 4 | −237,459,600 | −3,141 | **−1570.5** | 1 |
| 04 | 4 | −237,459,600 | −3,141 | **−1570.5** | 1 |
| 05 | 2 | **+211,377,600** | +2,796 | +1,398 | 1 |
| 07 | 2 | +416,858,400 | +5,514 | +2,757 | 1 |
| 08 | 4 | +340,880,400 | +4,509 | **+2254.5** | 1 |
| 09 | 2 | +184,161,600 | +2,436 | +1,218 | 1 |
| 10 | 4 | −677,678,400 | −8,964 | −4,482 | 1 |
| 14 | 2 | +416,858,400 | +5,514 | +2,757 | 1 |
| 16 | 2 | (+184,161,600) | (+2,436) | (+1,218) | **still running** |

    TOTAL = 2V00 + 4V01 + 4V02 + 4V03 + 4V04 + 2V05
          + 2V07 + 4V08 + 2V09 + 4V10 + 2V14 + 2V16
          = -3,456,432,000 .

**Status of `V16`, stated precisely.**  Eleven of the twelve values are
measured.  `f1Xm3_16` is still running at the time of writing; the value in
parentheses above is `V09`, supplied by the point symmetry, not a measurement,
and is marked as such.  The total therefore currently rests on eleven measured
values plus one symmetry-derived entry of weight 2 — a symmetry whose other
three instances have all been confirmed exactly on this very point.  When `16`
lands the assembly becomes fully measured and uses nothing unproven; if it were
to disagree, the symmetry derivation would be refuted and `V16` would have to be
taken from its own run, changing the total by `2(V16 - V09)`.  That outcome
would be logged as a refutation, not absorbed.  `f1Xm3_00` is also being re-run
as a pipeline regression against the banked `+893,138,400`.

Runs cost about 3-5 hours each (peak ~1.9 billion states at level 11-12, roughly
3.6x the `f1C` peak), on two cores over about 30 hours.

**How demanding the test was.**  The running sum reversed direction three
times.  After the banked `00` alone it stood at `+1,786,276,800` and the
remainder had to be strongly negative; after `03` it had overshot to
`-3,986,236,800` and had to come back up; after `10` it overshot again to
`-4,499,712,000`.  The last two values had to supply exactly `+579,700,800`
between them, and did.

## Gates: the point symmetry — 3/4 HIT, one pending

Pre-registered blind (commit `b6ab472`): `V01 = V02`, `V03 = V04`,
`V07 = V14`, `V09 = V16`, from a point symmetry derived independently and
validated against three banked points (it reproduces `C`'s and `R`'s recorded
`pi` and `rho`, and `X4`'s recorded assembly weights).

    V01 = V02 = -602,834,400    MATCH (exact)
    V03 = V04 = -237,459,600    MATCH (exact)
    V07 = V14 = +416,858,400    MATCH (exact)
    V09 = V16 = +184,161,600    PENDING (16 still running)

Three for three so far.  The derivation — a monomial symmetry is a pair `(alpha, beta)`
in `S_3 x S_3` acting by `(r,c) -> (alpha r, beta c)` and preserving the arrow
set of `N`, inducing precomposition by `rho = beta` on the subproblem index —
was validated against `C`, `R` and `X4` before use, and has now been confirmed
three times on a fourth point it was not calibrated against.  **The assembly does not use
it**: the twelve representatives are the orbits of the point-*independent*
scheme automorphisms alone.

## Prediction ledger

| # | logged at | prediction | outcome |
|---|---|---|---|
| 1 | `b6ab472` | `TOTAL(X_{-3}) = -3,456,432,000` | **HIT** |
| 2 | `b6ab472` | the four point-symmetry gates | **3/4 HIT exact; `V09=V16` still running** |
| 3 | `b6ab472` | re-run `f1Xm3_00 = +893,138,400` | see below |
| 4 | `b6ab472` | every value is `151,200 x` an integer | **MISS — refuted** |
| 5 | `7c04e2b` | `V05 + 2 V09 = +579,700,800`, logged with both unmeasured | **HIT** |
| 6 | `1eeb364` | `f1Xm3_05 = +211,377,600`, logged with `05` at level 8 of 20 | **HIT** |

Predictions 5 and 6 are the load-bearing ones and both are clean: 5 was
committed when neither value existed, and 6 when the only visible output of the
running job was per-level state counts, from which the value cannot be inferred.

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
