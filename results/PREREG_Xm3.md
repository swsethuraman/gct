# PRE-REGISTRATION — TOTAL at X_{-3} (session 23)

Committed **before** any X_{-3} subproblem beyond the banked `f1Xm3_00` has been
run in this session.  Branch `s21-xm3`, off `main` at `5cdc29c`.

## What is being tested, and why it is the sharp test

Session 22 proved the totals law `TOTAL(N) = Psi(N) x 1,152,144,000`
(Theorem 5.5), and pre-registered

    TOTAL(X_{-3})  =  -3,456,432,000  =  -3 x 1,152,144,000
                   =  151,200 x (-22,860) .

The proof is a parity argument: `chi(q) = det(q|_{V/W})^8 det(q|_W)^6` with
`8 = 6 + 2`, `det(q)^6 = 1` on both cosets because `det t = ±1` on `H` and 6 is
even, so the transpose coset — where `det(transpose) = (-1)^3 = -1` on `M_3` —
cannot contribute.  Every total ever measured sits at `Psi` in `{0, 1, 4}`, all
non-negative.  **`Psi(X_{-3}) = -3` is the first negative gauge value in the
banked set, and therefore the only available point at which a sign error in
that argument can show up.**

Independently re-derived here before anything else was run
(`analysis/wk4_s23_xm3orbits.py` reads the point off the substitution
`x3 += x2, x4 += x1, x7 += x1, x8 += x0`, giving `A = E(0,2)+E(1,1)`,
`B = E(1,1)+E(2,0)`, matching `analysis/wk4_s19_bank.py`):

    Psi(X_{-3}) = 2u_1 - 4u_2 - D = -3 ,   so the target is -3,456,432,000 .

## The run design — and it assumes no unproven symmetry

The 36 subproblems `(sigma_6, sigma_7)` in `S_3 x S_3` carry two
**point-independent** scheme automorphisms, proved in session 12: `swap`
`(s6,s7) -> (s7,s6)` and `post` `(s6,s7) -> (s6 w, s7 w)` with `w = (0 2)`.
Their orbits give **12 representatives**, with weights summing to 36:

| rep | 00 | 01 | 02 | 03 | 04 | 05 | 07 | 08 | 09 | 10 | 14 | 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| weight | 2 | 4 | 4 | 4 | 4 | 2 | 2 | 4 | 2 | 4 | 2 | 2 |

    TOTAL(X_{-3}) = 2V00 + 4V01 + 4V02 + 4V03 + 4V04 + 2V05
                  + 2V07 + 4V08 + 2V09 + 4V10 + 2V14 + 2V16 .

All twelve will be run.  Nothing in the assembly uses the point symmetry.

## The point symmetry, derived and validated, used only as free gates

A monomial symmetry of a balanced point `N = E10 (x) A + E20 (x) B` is a pair
`(alpha, beta)` in `S_3 x S_3` acting on the `3x3` grid by
`(r,c) -> (alpha r, beta c)` and preserving the arrow set of `N`; the induced
action on the subproblem index is precomposition by `rho = beta`.  The
derivation was validated against three banked points before being used:

- `C`: gives `pi = (0,2,1,6,8,7,3,5,4)`, `rho = (1 2)` — the recorded values;
- `R`: gives `pi = (1,0,2,7,6,8,4,3,5)`, `rho = (0 1)` — the recorded values;
- `X4`: gives orbit weights `{00:4, 01:4, 02:8, 03:4, 04:8, 05:4, 14:2, 16:2}`
  — exactly the assembly used in `results/results_T4.md`.

For `X_{-3}` it gives the unique nontrivial symmetry
`(alpha, beta) = ((1 2), (0 2))`, i.e. `pi = (2,1,0,8,7,6,5,4,3)` with
`sgn(alpha) sgn(beta) = +1`, and `rho = (0 2)`.  Merging the twelve
point-independent orbits under it predicts, **and this is logged as four blind
gates before any of these values exist**:

    V01 = V02,    V03 = V04,    V07 = V14,    V09 = V16 .

A gate failure means the symmetry derivation is wrong; the assembly is
unaffected either way, because it does not use it.

## The banked value, and the shape of the bet

Session 16 measured `f1Xm3_00 = +893,138,400 = 151,200 x 5907`.  With weight 2
it contributes `+11,814` cofactor units toward a target of `-22,860`, so

    **the remaining eleven values must contribute -34,674 cofactor units,
    i.e. -5,242,708,800 in weighted total.**

This is the same shape as the X4 test: the one value in hand is positive while
the predicted total is strongly negative, so the unmeasured values must
overturn it.  `f1Xm3_00` will also be re-run here as a pipeline regression on
this container; it must return `+893,138,400`.

## Predictions, logged now

1. **`TOTAL(X_{-3}) = -3,456,432,000`.**  This is session 22's prediction; this
   session's contribution is to measure it.
2. `V01 = V02`, `V03 = V04`, `V07 = V14`, `V09 = V16` (the point-symmetry gates).
3. Re-run `f1Xm3_00 = +893,138,400`.
4. Every value is `151,200 x` an integer (the programme's arithmetic signature).
5. Every run ends with `final states 1`, or with an exact `(0, 0)`.

## If it misses

No parameter will be adjusted to fit.  A miss will be logged as a refutation in
the session-16 style, and it falsifies one of the two inputs the proof consumes:
either the character computation `chi = det(q|_{V/W})^2` (the parity step, where
a sign error would show up first at negative `Psi`), or the slot dictionary
identifying `det(q|_{V/W})^{-1}` with the third-slot change of parameter.  Which
one is implicated is determined by the sign and size of the miss: a total equal
to `+3,456,432,000` implicates the parity step directly; anything else
implicates the dictionary or the law itself.  Theorem 5.5 would then be
retracted and the paper would revert to the conjecture form.

## Regression, run before this commit

    quad = 24;  quad0 = 0;  quadq raw 6 x 4 = 24
    det3 6 -> L2 29/29/29, L3 623/656/656, L4 13595/13595/14314,
              L5 197501/224542/235558, L6 1818118/2336283/2686868
    f1C_00 L7 = 54685987/100774838/141001840          (exact)
    f1C_00 L8 and its VALUE: running at the time of this commit

---

# ADDENDUM — the forced constraint, logged with `09` and `05` both unmeasured

2026-08-31, ~16:00Z.  Seven of the twelve values are in; `f1Xm3_09` is running
and `f1Xm3_05` has not started.  Neither value has been seen.

Measured so far (all with `final states 1`):

| rep | weight | VALUE | /75,600 |
|---|---|---|---|
| 00 | 2 | +893,138,400 | +11,814 | (banked, session 16; re-run queued)
| 01 | 4 | −602,834,400 | −7,974 |
| 02 | 4 | −602,834,400 | −7,974 |
| 03 | 4 | −237,459,600 | −3,141 |
| 07 | 2 | +416,858,400 | +5,514 |
| 08 | 4 | +340,880,400 | +4,509 |
| 10 | 4 | −677,678,400 | −8,964 |

Weighted sum of those seven: **−4,499,712,000**, against a target of
−3,456,432,000.  So the remaining five (`04, 05, 09, 14, 16`, weight 12) must
supply **+1,043,280,000** — the running sum has overshot downward and the rest
must come back up, exactly the shape the X4 test had.

Imposing the point symmetry — `V04 = V03`, `V14 = V07`, `V16 = V09`, whose first
instance `V01 = V02` has already been confirmed exactly — those contribute
`4V03 + 2V07 = -116,121,600`, and the totals law then forces

    **V05 + 2 * V09  =  +579,700,800  =  75,600 x 7,668 .**

**This is a point constraint with no freedom left, logged before either value
exists.**  It is the analogue of session 18's `4c03 + 2c16 = -10,136` at X4.

Note what it demands.  Five of the seven measured values are negative and the
weighted sum is 1.3x below the target; for the law to hold, `V05` and `V09`
must between them be strongly *positive*.  If either lands negative enough that
`V05 + 2V09 != 579,700,800`, the totals law fails at the first negative gauge
value it has ever been tested at, and Theorem 5.5 is refuted.

Two further gates remain live and independent of this: `V03 = V04` and
`V07 = V14`, plus `V09 = V16` once `09` is known.  If a *gate* fails instead,
the point-symmetry derivation is wrong and the constraint above is void — but
the twelve-run assembly still stands, because it never used the symmetry.
