# The race: `m_det` against the ambient cap

Session 25, branch `s25-race`.  Companion to `docs/ambient_audit.md`.

**Headline.**  `m_det(lam) >= a(lam,delta)` at **every weight computed** —
`n = 3` through `delta = 8`, `n = 4` through `delta = 5`, `n = 5` through
`delta = 4`; 664 ambient-support weights in all, zero exceptions, worst margin
exactly `0`.  The ratio `sum m_det / sum a` **rises** in `delta` *and* in `n`,
so the integrator's prior (and my own pre-registered S3) are refuted: the
determinant is pulling *away* from the cap, not towards it.  But the pointwise
inequality **provably cannot persist** — a dimension count forces it to fail —
and both sides are so deeply pre-asymptotic that the crossover is far outside
computational reach.  The correct statement is a **bounded-range no-go**, not a
theorem that the profile never occurs.

---

## 1. What the prize profile actually buys — a correction

The brief says an obstruction "comes free" at a weight with `m_det < a`.  It
does not.  There,

    mult_det <= m_det < a  and  mult_per <= a,

which caps the determinant below the ambient by group theory alone but gives no
*lower* bound on `mult_per`.  An obstruction still needs `mult_per > mult_det`,
i.e. an upper bound on `def_per`.  The profile removes the deficit's work on one
side only.  It is **half-free**, and is called that throughout.

## 2. The measurement

Over the ambient support (`a >= 1`) and over the live locus (`a >= 2`):

| `n` | `delta` | supp `a>=1` | `sum a` | `sum m_det` | ratio | `m<a` | `m=a` | tie % | live `a>=2` | ratio (live) | `m<a` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 2 | 2   | 2   | 2    | 1.000 | 0 | 2  | 100%  | – | – | – |
| 3 | 3 | 5   | 5   | 6    | 1.200 | 0 | 4  | 80.0% | – | – | – |
| 3 | 4 | 12  | 12  | 18   | 1.500 | 0 | 7  | 58.3% | – | – | – |
| 3 | 5 | 28  | 29  | 61   | 2.103 | 0 | 11 | 39.3% | 1   | 1.500 | 0 |
| 3 | 6 | 67  | 79  | 279  | 3.532 | 0 | 15 | 22.4% | 12  | 2.333 | 0 |
| 3 | 7 | 161 | 225 | 1356 | 6.027 | 0 | 19 | 11.8% | 50  | 4.368 | 0 |
| 3 | 8 | 371 | 677 | 6634 | 9.799 | 0 | 25 | 6.7%  | 168 | 7.730 | 0 |
| 4 | 2 | 3   | 3   | 3    | 1.000 | 0 | 3  | 100%  | – | – | – |
| 4 | 3 | 9   | 9   | 12   | 1.333 | 0 | 6  | 66.7% | – | – | – |
| 4 | 4 | 28  | 33  | 95   | 2.879 | 0 | 10 | 35.7% | 5   | 1.700 | 0 |
| 4 | 5 | 95  | 142 | 1675 | 11.796| 0 | 16 | 16.8% | 35  | 5.232 | 0 |
| 5 | 2 | 3   | 3   | 3    | 1.000 | 0 | 3  | 100%  | – | – | – |
| 5 | 3 | 13  | 13  | 20   | 1.538 | 0 | 8  | 61.5% | – | – | – |
| 5 | 4 | 60  | 74  | 532  | 7.189 | 0 | 16 | 26.7% | 12  | 2.192 | 0 |

Three readings, all in the same direction:

1. **`min(m_det - a) = 0` in every row.**  There is no half-free weight, and no
   near miss either — the closest approach is a tie, never a deficit of one.
2. **The ratio rises in `delta`** at every `n`: `1.00 -> 9.80` at `n = 3`.
3. **The ratio rises in `n` at fixed `delta`** — `delta = 3`: 1.200, 1.333,
   1.538; `delta = 4`: 1.500, 2.879, 7.189 — and the **tie fraction falls** in
   `n` — `delta = 4`: 58.3%, 35.7%, 26.7%.  Larger `n` makes the profile
   *less* reachable, not more.

`delta = 2` is a tie everywhere, for a reason: `Sym^2(Sym^n)` is
multiplicity-free so `a = 1` on its support; the first partials of `det_n` are
linearly independent so no quadric contains the orbit closure, the degree-2
ideal is zero, `mult_det = a = 1`, and `def >= 0` gives `m_det >= 1 = a`.
(Pre-registered as S5; confirmed at `n = 3, 4, 5`.)

## 3. Why the trend must break — and why we cannot see where

Summing against Weyl dimensions,

    Sigma_a(delta) = sum_lam a(lam,delta) dim S_lam(C^{n^2})
                   = dim Sym^delta(Sym^n C^{n^2}) = binom(A + delta - 1, delta),
                     A = dim Sym^n C^{n^2} = binom(n^2+n-1, n),

which is a polynomial in `delta` of degree `A - 1`, while

    Sigma_m(delta) = sum_lam m_det(lam) dim S_lam(C^{n^2})

grows with degree `d - 1`, `d = dim closure(GL_{n^2}.det_n) = n^4 - 2n^2 + 2`,
because `m_det(lam)` is the stabilised value of `mult` along the `Phi`-ray and
the Hilbert function of a `d`-dimensional cone has degree `d - 1`.

**If `m_det >= a` held pointwise for all `delta`, then `supp(a)` would lie
inside `supp(m_det)` and `Sigma_m >= Sigma_a` for all `delta`.**  But
`A - 1 >> d - 1`:

| `n` | `A - 1` (ambient) | `d - 1` (orbit) |
|---|---|---|
| 3 | 164 | 64 |
| 4 | 3875 | 225 |

so `Sigma_a` eventually dominates and the pointwise inequality **must fail**.
A half-free weight exists.  This is a proof, not a conjecture.

Where?  Not visible from here.  Measured:

| `delta` | `Sigma_a` (n=3) | `Sigma_m` (n=3) | ratio |
|---|---|---|---|
| 2 | 13,695 | 16,215 | 1.184 |
| 3 | 762,355 | 1,241,190 | 1.628 |
| 4 | 32,018,910 | 78,138,270 | 2.44 |
| 5 | 1,082,239,158 | 3,984,487,452 | 3.682 |
| 6 | 30,663,442,810 | 163,360,154,970 | 5.328 |
| 7 | 749,064,102,930 | 5,437,084,923,930 | 7.259 |

`Sigma_m / Sigma_a` is still *rising* at `delta = 7`, and both sides are far
from their asymptotic regimes — a polynomial of degree 164 does not look like
`delta^164` until `delta >> 164`, and we are at `delta <= 8`.  Any extrapolation
of the crossover from six pre-asymptotic points would be worthless, so none is
offered.  What can be said exactly: the crossover degree is an **upper bound**
on the first half-free weight, it is finite, and it is far beyond `delta = 8`.

## 4. Verdict

The brief's kill criterion — *"if `m_det / a` rises through `n = 5`, that is a
no-go theorem"* — fires.  It should be written up, but with its scope stated
honestly:

> **In the computationally reachable range the multiplicity route is capped
> from both ends.**  `mult_det` is capped above by `a` and `mult_per` is capped
> above by `a`; the determinant's Peter–Weyl count never falls below `a`, so
> the half-free profile does not occur, and the gap widens in both `delta` and
> `n`.  This is a no-go over a bounded range, not a structural impossibility:
> a dimension count proves the half-free profile exists at some larger
> `delta`, and the measured trend says only that it is not near.

Reporting it as an unqualified no-go would be the same error as reporting
`def_det((2,2,2),2) = 1` as boundary geometry — true arithmetic, wrong claim
attached.

## 5. Where the padded problem first becomes live

A multiplicity obstruction needs `a >= 2`; the padded permanent's count
vanishes unless `ell(lam) <= m^2 + 1` (session 24b's row bound).  The padded
live locus is therefore `{lam : a >= 2, ell(lam) <= m^2+1}`, computable from
the ambient alone.

| `(n,m)` | `delta` | ambient support | `a >= 2` | of those `ell <= m^2+1` |
|---|---|---|---|---|
| (4,3) | 2 | 3 | 0 | 0 |
| (4,3) | 3 | 9 | 0 | 0 |
| (4,3) | 4 | 28 | 5 | **5** |
| (4,3) | 5 | 95 | 35 | **35** |
| (4,3) | 6 | 299 | 175 | **175** |
| (5,3) | 4 | 60 | 12 | **12** |
| (6,3) | 3 | 19 | 1 | **1** |

Two things follow.  The padded problem at `(4,3)` is **dead below
`delta = 4`** — session 24b's screen was run entirely inside the region where
no multiplicity obstruction was arithmetically possible, which strengthens its
negative rather than weakening it.  And the row bound is **not binding**: every
`a >= 2` weight in this range already has at most `m^2 + 1` rows, because the
ambient's own constituents at low `delta` are short.  `m_det >= a` at all of
them, so the half-free profile is absent in the padded setting too.
