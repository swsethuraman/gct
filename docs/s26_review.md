# Review of session 26, and the padded case its reduction hands you

Integrator, 2026-08-31.  Independent code, fresh container.

## 1. Verification

Theorem 6 rests on one measurement — the Jacobian rank of
`(A_1..A_r) -> f(s_1 A_1 + ... + s_r A_r)` — so I recomputed it from scratch
(cofactor route, exact, mod `2^61-1`, two seeds):

| n | r | target | det | per | session 26 |
|---|---|---|---|---|---|
| 3 | 2 | 4 | 4 | 4 | 4, 4 |
| 3 | 3 | 10 | 10 | 10 | 10, 10 |
| 3 | 4 | 20 | 20 | 20 | 20, 20 |
| 3 | 5 | 35 | **29** | 35 | 29, 35 |
| 3 | 6 | 56 | **38** | **50** | 38, 50 |
| 4 | 3 | 15 | 15 | 15 | dense |
| 4 | 4 | 35 | **34** | 35 | 34 |
| 2 | 5 | 15 | **14** | 14 | 14 |

**Exact match on every entry**, including the `n=4, r=4` deficiency of exactly 1
— the classical non-determinantality of a general quartic surface, recovered as
a rank drop.  Theorem 6 stands.

## 2. One error, in the bound rather than the results

`docs/isotypic_rank.md` §4 states

    dim D_r  <=  min( C(r+2,3),  9r − 16 ).

At `r = 2` that reads `dim D_2 <= 2`, but the session's own table (and mine)
measures rank **4**, and `D_2` is proved dense by an elementary argument in the
same section.  **The bound is false at `r = 2` and contradicts the document two
paragraphs later.**

The cause: the bound assumes the group acts with *finite* stabiliser on generic
`r`-tuples.  Normalising `A_1 = I` forces `Q = P^{-1}` and then `P` must commute
with `A_2, ..., A_r`.  For `r >= 3` two generic matrices generate `M_n`, so `P`
is scalar and the stabiliser is finite.  At `r = 2` a single generic matrix has
an `(n−1)`-dimensional commutant mod scalars — 2 dimensions at `n = 3` — so the
orbit is 14-dimensional, not 16, and the bound becomes `18 − 14 = 4`.  Which is
the measured value.

**Fix: state the bound for `r >= 3`.**  No conclusion changes — every
conclusion lives at `r >= 3`, and `r = 2` is proved directly — but this must not
reach the paper as written.

## 3. The H1/H2 alarm is closed, in the good direction

I flagged that the paper's deficit table was equally consistent with **H1** (the
ideal really is zero through degree 7) and **H2** (the engine returns the
ambient multiplicity, not the closure one).  Session 26 settles it:

- the rank algorithm is derived from a *proof* (Lemma 2) and shares no code,
  no algorithm and no author with the engine;
- it reproduces `mult = a` at all 20 weights with `a > 0` and `delta <= 4`;
- and Theorem 6 **explains** `mult = a` at short weights rather than merely
  observing it — `D_r` is dense for `r <= 4`, so there is nothing for the ideal
  to contain.

H1, and not by coincidence.  The engine is vindicated.  Raising the alarm was
right; the alarm was false.

## 4. What the reduction gives in the padded case — the part not done

Session 26 recommends `n = 4`, lengths 4 and 5, on the grounds that `det_4`'s
ideal is live from length 4 while `per_4`'s is empty through length 5.  That
comparison is **unpadded**, and unpadded is dimension-decided
(`dim closure(per_4) = 250 > 226 = dim closure(det_4)`).  It is the nursery
again — the third time this distinction has bitten the programme.

The reduction applies verbatim to the padded permanent, and I ran it.
`per_3^pad = x_0 * per_3` uses 10 of the 16 coordinates, so the source is
`(C^10)^r`:

| r | target `C(r+3,4)` | `det_4` | `per_3^pad` |
|---|---|---|---|
| 2 | 5  | 5  | 5  |
| 3 | 15 | **15** | **12** |
| 4 | 35 | **34** | **23** |
| 5 | 70 | — | **39** |

**The asymmetry runs the opposite way once you pad.**  `det_4` fills the
ambient through length 3; `per_3^pad` does not fill it from length 3 onward.

And the padded numbers have a closed form, which makes this a theorem rather
than a measurement:

> **`per_3^pad` is reducible** — it is `x_0` times a cubic — so every
> restriction `per_3^pad|_L` is a linear form times a cubic.  Hence `D_r^{pad}`
> lies in the reducible locus `{ell . c}`, of dimension `r + C(r+2,3) − 1`.
> Since `per_3` is dense in the `r`-ary cubics for `r <= 5` (session 26's own
> table), `D_r^{pad}` **is** exactly that locus for `3 <= r <= 5`.

    r = 3:  3 + 10 − 1 = 12      measured 12
    r = 4:  4 + 20 − 1 = 23      measured 23
    r = 5:  5 + 35 − 1 = 39      measured 39

Three for three, exactly.  So the measured ranks are generic, not sampled — the
image sits inside a variety of exactly the measured dimension, and rank is a
lower bound.  No probabilistic step.

**The consequence is a new necessary condition on obstructions.**  An
obstruction needs `mult_per^pad > mult_det`.  At any weight where `det`'s ideal
is empty, `mult_det = a`, which is the maximum, so `mult_per^pad <= mult_det`
and no obstruction is possible.  Therefore:

> **At `n = 4`, every multiplicity obstruction requires `ell(lam) >= 4`** —
> because `det_4` fills the ambient at lengths `<= 3`, and filling the ambient
> is the largest a closure count can be.

This composes with the ambient screen: the live locus is
`{a >= 2} ∩ {ell(lam) >= (the determinant's crossover length)}`, and both
conditions are decided by cheap easy-side computations before anything is
measured.  It also says the padded permanent is handicapped by its own
reducibility at every length `>= 3` — the padding that makes containment
possible is the same padding that shrinks its closure ring.

## 5. Assessment

The best session of the programme, and for an unusual reason: it hit eight of
eight predictions and then argued that this was a bad sign, correctly.
"The selection rule and the triviality condition were the same condition" is
the sharpest self-criticism in the record — my brief chose the cells for
cheapness, and cheapness was the theorem's hypothesis.  The session was right
to say the five numbers are worth little and the reduction is worth a lot.

Recommended paper additions, on the session's ranking, with my view: **take
(1)** — the length-`<= 4` theorem converts every short-weight deficit into
`m_det − a` with no geometry in it, and that is now the honest description of
the paper's entire deficit dataset.  **Take (2)** with the §5(ii) residue stated.
**(3) should be replaced** by the padded version in §4 above; the unpadded
crossover is a nursery statement and the padded one is a necessary condition on
obstructions.
