# Is Phi_18 primitive?  (Job 4 — statement, current bound, and the cheap route)

Session 23, 2026-08-31.  **Status: not settled.  This document states the
question precisely, records what is actually known, corrects the size of the
existing bound, and specifies the two runs that would tighten it.**

## The question

`dim C[Sym^3 C^9]^{SL_9}_18 = 1`, so the integral invariants of degree 18 form
a rank-one lattice `L_18` inside a one-dimensional space.  The **canonical**
generator is the primitive one: the generator of `L_18`.  Everything else is a
convention.  The programme's reported

    Phi_18(det_3) = -877,879,296,000 = -2^16 3^7 5^3 7^2

is in the engine's normalisation, and nobody has checked that this normalisation
is the primitive one.  If it is a proper multiple `m . Phi_18^prim`, then the
quoted factorisation is off by `m` and **must be divided through and restated**
— including in `eq:value`, `eq:perm`, `eq:value24`, and the arithmetic-signature
remark, which is the part of the paper a reader is most likely to quote.  The
same question applies to `Phi_24`.

Two things are worth separating, because they are often conflated:

- **content** `c(F)` of an integral invariant `F` = the gcd of its coefficients
  as a polynomial in the 165 coefficients of the cubic.  `F/c(F)` is primitive.
- **`g(F)` = gcd of the values of `F` at integer points.**  Always
  `c(F) | g(F)`, and the inequality can be strict (`x^2 + x` has content 1 and
  `g = 2`).  So evaluations bound the content **from above only**, and no
  finite set of evaluations proves primitivity.

## What is actually known

`engine/br2.c` evaluates the explicit bracket monomial `B(S)` — a product of six
nine-fold brackets — in the normalisation `V = 6^18 . B(S)`, which is a
polynomial with **integer** coefficients in the 165 cubic coefficients.  At
`delta = 18` that normalisation reproduces the banked `Phi_18` exactly, on a
bracket structure independent of the one the original engine used, so the
engine's `Phi_18` *is* `V`, and the question is `content(V)`.

Restricting to the six-dimensional space `U` of cubics
`sum_sigma u_sigma x_{1 sigma 1} x_{2 sigma 2} x_{3 sigma 3}` gives
`Phi_18|_U = sum_{a=0}^{6} K'_a P^a Q^{6-a}` with `K'_a = K'_{6-a}`, and each
`K'_a` **is literally a coefficient of `V`** (the coefficient of
`c_id^a c_c^a c_{c^2}^a c_{t1}^{6-a} c_{t2}^{6-a} c_{t3}^{6-a}`).  So

    content(V)  |  gcd_a K'_a  |  K'_6 .

Measured this session (`br2` with `u` supported on the even permutations):

    K'_6 = K'_0 = -185,794,560 = -2^16 . 3^4 . 5 . 7 .

**And this is exactly the bound the brief calls weak**:
`gcd(Phi_18(det_3), Phi_18(per_3)) = 2^16 3^4 5 . 7 = 185,794,560 = |K'_6|`.
The two bounds coincide, which is not a coincidence — both are dominated by the
same coefficient — and it means the evaluation-gcd route has already saturated
at the level of the two banked values.  Adding more *evaluation points* will
not help much; adding more *coefficients* will.

## RESULT (session 23): the bound tightens by a factor of 4

The `t = 2` run described below was carried out.

    R(2) = -582,204,532,654,080     (u = (1,1,1,2,2,2), delta = 18, final states 1)

With `R(0) = -185,794,560`, `R(1) = +50,536,120,320`, `R(-1) = -877,879,296,000`
already in hand, the four unknowns of the binary sextic are determined:

    K'_0 = K'_6 =        -185,794,560
    K'_1 = K'_5 =      +2,786,918,400
    K'_2 = K'_4 =    -206,649,999,360
    K'_3       =    +458,633,871,360

**All four come out integral** from three equations in three unknowns — an
arithmetic consistency check the run had no way to pass by accident — and all
three defining equations verify exactly.  Hence

    content(Phi_18)  |  gcd(K'_0, K'_1, K'_2, K'_3)  =  46,448,640 = 2^14 . 3^4 . 5 . 7 ,

against the previous bound `185,794,560 = 2^16 3^4 5 . 7`.  A factor of 4.

**What this says about the quoted value.**  Writing `Phi_18^prim` for the
primitive generator,

    18,900  <=  |Phi_18^prim(det_3)|  <=  877,879,296,000 ,

with the lower end attained exactly when `content = 46,448,640`.  And at that
end the numbers are striking:

    Phi_18^prim(det_3) = -18,900 = -2^2 . 3^3 . 5^2 . 7
    Phi_18^prim(per_3) =  +1,088 =  2^6 . 17

whose ratio is `-4725/272`, as it must be.  **We do not claim these are the
primitive values** — the bound is an upper bound on the content, computed from
four of the coefficients, and the true content may be smaller.  But it is now a
live possibility that the paper's headline factorisation
`-2^16 3^7 5^3 7^2` is mostly normalisation, and that the invariant-theoretic
content of the number is `-2^2 3^3 5^2 7`.  That possibility did not exist
before this computation, and it should be settled before the value is quoted
again.

## The same, at degree 24

Two further runs (`t = 2`, `t = 3`) were carried out:

    R(2) = -51,414,646,680,391,680
    R(3) = -402,640,773,292,783,226,880

With `R(0) = K_8 = -1,428,295,680`, `R(1) = Phi_24(per_3)` and
`R(-1) = Phi_24(det_3)` known, the binary octic `Phi_24|_U` is determined:

    K_0 = K_8 =      -1,428,295,680
    K_1 = K_7 =     +20,313,538,560
    K_2 = K_6 =    -720,218,096,640
    K_3 = K_5 =  +5,161,860,587,520
    K_4       = -12,937,581,619,200

All five integral, all four defining equations verify, and the two relations
derived in advance from `R(1) +/- R(-1)` — `K_1 + K_3 = 5,182,174,126,080` and
`2K_2 + K_4 = -14,378,017,812,480` — both hold.  Hence

    content(Phi_24)  |  gcd(K_0, ..., K_4)  =  39,674,880 = 2^10 . 3^3 . 5 . 7 . 41 ,

against the one-coefficient bound `|K_8| = 1,428,295,680 = 2^12 3^5 5 . 7 . 41`.
A factor of **36**.  So

    623,700  <=  |Phi_24^prim(det_3)|  <=  24,745,222,656,000 ,

with the lower end giving

    Phi_24^prim(det_3) = -623,700 = -2^2 . 3^4 . 5^2 . 7 . 11
    Phi_24^prim(per_3) = -101,236 = -2^2 . 25309

whose ratio is `155925/25309`, as it must be.  Note
`623,700 = 33 x 18,900`: the two candidate primitive values at degrees 18 and
24 differ by `3 . 11`, and `11` is exactly the prime that distinguishes
`Phi_24(det_3)` from `Phi_18(det_3)` in the raw factorisations.  We record the
coincidence and claim nothing from it.

## Summary of what is now bounded

| | reported value | content divides | so `|Phi^prim(det_3)|` is at least |
|---|---|---|---|
| `Phi_18` | `-877,879,296,000 = -2^16 3^7 5^3 7^2` | `46,448,640 = 2^14 3^4 5 . 7` | `18,900 = 2^2 3^3 5^2 7` |
| `Phi_24` | `-24,745,222,656,000 = -2^12 3^7 5^3 7^2 . 11 . 41` | `39,674,880 = 2^10 3^3 5 . 7 . 41` | `623,700 = 2^2 3^4 5^2 7 . 11` |

Both bounds come from four or five coefficients of the `U`-restriction, and both
are upper bounds on the content, so neither settles primitivity.  What they do
settle is that **the quoted factorisations cannot be taken at face value**: up to
a factor of `2^14 3^4 5 . 7` at degree 18 and `2^10 3^3 5 . 7 . 41` at degree 24
is potentially normalisation, and the invariant-theoretic content of the two
headline numbers may be as small as `-2^2 3^3 5^2 7` and `-2^2 3^4 5^2 7 . 11`.

**What would settle it.**  Either (i) more coefficients — coefficients outside
`U`, which need a general-support evaluator rather than `br2.c`; or (ii) an
exhibited integral invariant `F` with `V = c . F` and `c` the bound above, which
would prove the content is exactly that.  Route (ii) is the constructive one and
is where to look first.  A third possibility worth checking cheaply: the bracket
monomial `V = 6^18 B(S)` carries an explicit factor of `6^18`, and if the
primitive generator is `B(S)` up to a small integer then most of the content is
that factor and nothing deeper.  `6^18` is not divisible by `5` or `7`, so it
cannot be the whole story at either degree — both bounds contain `5 . 7` — but
it may be most of the power of 2 and 3.

## The route to the bound: the runs (as designed, before they were run)

`Phi_18|_U` is a binary sextic in `(P,Q)` with `K'_a = K'_{6-a}`, so it has four
unknowns `K'_0 = K'_6`, `K'_1 = K'_5`, `K'_2 = K'_4`, `K'_3`.  Running `br2`
with `u = (1,1,1,t,t,t)` returns

    R(t) = sum_a K'_a t^{18-3a} = sum_a K'_a s^{6-a},   s = t^3 .

Three evaluations are already in hand:

    R(0)  = K'_6                = -185,794,560
    R(1)  = Phi_18(per_3)       = +50,536,120,320
    R(-1) = Phi_18(det_3)       = -877,879,296,000

so **one further run at `t = 2` (about 28 minutes) determines all four `K'_a`** — done, see above —
and `gcd(K'_0, K'_1, K'_2, K'_3)` is then a bound that uses four independent
coefficients rather than one.  For `Phi_24|_U` — a binary octic with five
unknowns `K_0 = K_8`, `K_1 = K_7`, `K_2 = K_6`, `K_3 = K_5`, `K_4`, and
`R(0), R(1), R(-1)` known — **two further runs (`t = 2, 3`, about two hours
each)** do the same.

Neither settles primitivity; both replace a one-coefficient bound with a
four- or five-coefficient one, and either could collapse it to a small number.
If `gcd_a K'_a = 1`, the content is 1 and `Phi_18` is primitive — that direction
*is* conclusive, because the content divides the gcd of any set of coefficients.
Only the other direction (a nontrivial gcd) stays inconclusive, and would then
need coefficients outside `U`.

## Honest statement for the paper, until it is settled

The value `-877,879,296,000` should be quoted as *the value in the bracket-
monomial normalisation of Section [method]*, with a remark that the primitive
normalisation may differ by a divisor of `2^16 3^4 5 . 7`, and that the same
caveat attaches to `Phi_24(det_3) = -24,745,222,656,000` with its own bound.
The ratios are unaffected and should carry the weight: `-4725/272` at degree 18,
`17325` at degree 24, `451/16` between them.  Those are normalisation-free and
nothing about primitivity can move them.

## Note on the arithmetic signature

`151,200 = 2^5 3^3 5^2 7` divides every measured `det_3` evaluation.  If the
engine's normalisation turns out to be `m` times primitive, the signature
statement rescales with it, and part or all of `151,200` could be an artefact
of `m` rather than a property of the invariant.  **Settling primitivity is
therefore a prerequisite for taking the `151,200` signature seriously**, and
that connection does not seem to have been noted before.
