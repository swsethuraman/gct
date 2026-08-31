# The n=4 padded gate: the nineteen cells, measured

Session 27, branch `s27-n4gate`, 2026-08-31.  Clone tip `1203fe4`
(`6aaab97` verified as an ancestor).
Pre-registration: `results/PREREG_s27.md`, committed before any computation.

**Headline.**  All nineteen close, and they close harder than expected:
`mult_det_4 = mult_per_3^pad = a` at **every** one of them.  Neither ideal
bites at `delta = 5`.  Moreover the closure is not a coincidence of degree 5 —
a containment theorem shows **no weight of length `<= 4` can ever carry an
obstruction, at any degree**, so the 65 length-4 cells of the `delta = 6` gate
are closed a priori too.  The genuinely open region is `ell(lam) >= 5`, where
the containment argument provably breaks; there are **71** such cells at
`delta = 6`, and the three cheapest of them also measure `D = 0`.

---

## 1. The containment theorem — why length 4 was never open

**Theorem.**  `D_4^{per_3^pad} ⊆ D_4^{det_4}`.  Consequently
`mult_lam C[closure(per_3^pad)]_delta <= mult_lam C[closure(det_4)]_delta` for
every `lam` with `ell(lam) <= 4` and every `delta`, so `D <= 0` there.

*Proof.*  Restricting `x_0 . per_3` to a 4-plane gives `ell(s) . c(s)`, with
`ell` the restriction of the padding variable and `c` the restriction of
`per_3`.  `per_3` is dense in the 4-ary cubics (Jacobian rank 20 of 20,
re-measured below), so `D_4^pad` is the whole reducible locus
`closure{ell . c}`, of dimension `4 + C(6,3) - 1 = 23` — exactly the measured
rank.  Every 4-ary cubic is `3x3` linear-determinantal (classical for smooth
cubic surfaces; density re-measured below as rank 20 of 20), so for generic `c`
write `c = det_3 M(s)` and then

    ell . c  =  det_4 diag( ell(s), M(s) ),

a `4x4` linear determinantal representation.  `D_4^{det_4}` is closed, so it
contains the closure of the generic reducible quartics, i.e. all of `D_4^pad`.
Containment of varieties gives a surjection `C[D_4^{det_4}] ↠ C[D_4^pad]` of
`GL_4`-algebras, hence the multiplicity inequality at every length-4 weight
(session 26, Prop. 5). ∎

**Where it stops.**  At `r = 5` the same construction needs every 5-ary cubic
to be `3x3`-determinantal, and it is not: the Jacobian rank is 29 of 35.  The
block trick reaches only `closure{ell . det_3 M}`, of dimension
`5 + 29 - 1 = 33`, inside a 39-dimensional `D_5^pad`.  So the argument breaks
**exactly at length 5**, which is where the open cells are.

## 2. The gate, reproduced

Two conditions must both hold: ambient room `a >= 2` (below that any
obstruction is an occurrence obstruction, closed by BIP) and length
`ell(lam) >= 4` (at `ell <= 3`, `det_4` restricted to any 3-plane is every
ternary quartic — rank 15 of 15 — so `mult_det = a`, the maximum possible, and
`mult_per^pad <= mult_det` trivially).

| `delta` | weights | `a >= 2` | and `ell >= 4` | and `ell >= 5` |
|---|---|---|---|---|
| 2 | 22   | 0   | 0   | 0 |
| 3 | 77   | 0   | 0   | 0 |
| 4 | 231  | 5   | **0** | 0 |
| 5 | 620  | 35  | **19** | **0** |
| 6 | 1530 | 175 | 136 | **71** |

Reproduced from my own plethysm; the brief's four rows agree exactly, including
the six named weights.  Note the last column: **every one of the nineteen has
length exactly 4**, so §1 disposes of all of them before any measurement.

## 3. The nineteen, measured

Algorithm: monomial basis of the weight-`lam` subspace of
`Sym^delta(Sym^4 C^4)` in the coefficient functionals; `R` the matrix of the
simple raising operators, `a = dim ker R`; `E` the evaluation at points
`f(s_1 A_1 + ... + s_4 A_4)` for random integer tuples;
`mult = rank([R;E]) - rank(R)`.  Ranks modulo two large primes throughout, plus
exact `Q` wherever the weight space is at most 200.  **A rank attaining `a` is
a certificate, not a sample**: `rank_p <= rank_Q <= a`, so `mult_p = a` forces
equality.  Every measurement below attains `a`, so no probabilistic step enters
any conclusion.

| `lam` | `a` | dim | `mult_det` | `mult_pad` | `D` |
|---|---|---|---|---|---|
| (8,6,4,2)  | 3 | 939  | 3 | 3 | 0 |
| (9,6,4,1)  | 3 | 414  | 3 | 3 | 0 |
| (10,4,4,2) | 3 | 572  | 3 | 3 | 0 |
| (10,6,2,2) | 3 | 352  | 3 | 3 | 0 |
| (8,4,4,4)  | 2 | 1550 | 2 | 2 | 0 |
| (8,7,4,1)  | 2 | 459  | 2 | 2 | 0 |
| (8,8,2,2)  | 2 | 427  | 2 | 2 | 0 |
| (9,5,4,2)  | 2 | 774  | 2 | 2 | 0 |
| (9,6,3,2)  | 2 | 625  | 2 | 2 | 0 |
| (9,7,3,1)  | 2 | 309  | 2 | 2 | 0 |
| (10,5,4,1) | 2 | 331  | 2 | 2 | 0 |
| (10,6,3,1) | 2 | 269  | 2 | 2 | 0 |
| (10,7,2,1) | 2 | 175  | 2 | 2 | 0 |
| (11,4,4,1) | 2 | 237  | 2 | 2 | 0 |
| (11,5,2,2) | 2 | 269  | 2 | 2 | 0 |
| (11,5,3,1) | 2 | 207  | 2 | 2 | 0 |
| (11,6,2,1) | 2 | 147  | 2 | 2 | 0 |
| (12,4,2,2) | 2 | 191  | 2 | 2 | 0 |
| (12,5,2,1) | 2 | 112  | 2 | 2 | 0 |

    weights with mult_det   < a : 0 of 19
    weights with mult_pad   < a : 0 of 19
    weights with D > 0          : 0
    weights with D = 0          : 19

**The surprise is the second row of that summary.**  `D_4^pad` has
codimension **12** in the 35-dimensional space of quaternary quartics, and its
coordinate ring nevertheless carries the *full* ambient multiplicity in all
nineteen isotypic components at `delta = 5`.  I pre-registered the opposite
(19 of 19 strictly below `a`) on the grounds that a codimension-12 variety must
have a large ideal.  It does — but none of it lands in these nineteen isotypic
components at this degree.  This is the brief's own warning about dimension
versus isotypic multiplicity, and I walked into it in P2b after flagging it in
P1.

## 4. The Jacobian table, re-measured independently

Chain rule: the column of `dPhi` for the coordinate `(A_k)_t` is
`s_k . (df/dx_t)(sum s_i A_i)`.  Rank at an integer point, two primes; a rank
attaining the target is a proof of dominance by lower semicontinuity.

| `f` | `n` | `r` | rank | target `C(r+n-1,n)` | dense? | bound `n^2 r - dim Stab` |
|---|---|---|---|---|---|---|
| `det_3` | 3 | 2 | 4  | 4  | yes | — |
| `det_3` | 3 | 3 | 10 | 10 | yes | — |
| `det_3` | 3 | 4 | 20 | 20 | **yes** | — |
| `det_3` | 3 | 5 | 29 | 35 | no  | 45−16 = 29 |
| `det_3` | 3 | 6 | 38 | 56 | no  | 54−16 = 38 |
| `per_3` | 3 | 4 | 20 | 20 | yes | — |
| `per_3` | 3 | 5 | 35 | 35 | **yes** | — |
| `per_3` | 3 | 6 | 50 | 56 | no  | 54−4 = 50 |
| `det_4` | 4 | 3 | 15 | 15 | **yes** | — |
| `det_4` | 4 | 4 | 34 | 35 | no  | 64−30 = 34 |
| `det_4` | 4 | 5 | **50** | 70 | no | 80−30 = **50** |
| `per_3^pad` | 4 | 3 | 12 | 15 | no | reducible locus |
| `per_3^pad` | 4 | 4 | 23 | 35 | no | reducible locus |
| `per_3^pad` | 4 | 5 | 39 | 70 | no | reducible locus |
| `per_3^pad` | 4 | 6 | 55 | 126 | no | see below |

Every session-26 entry reproduces.  Two additions:

* **`det_4` at `r = 5` is 50**, which the brief left blank, and it is exactly
  `16·5 − 30`: the naive stabiliser count is attained with no extra degeneracy
  at `n = 4` too.
* The padded closed form `r + C(r+2,3) − 1` gives **12, 23, 39** at
  `r = 3,4,5`, matching all three measured ranks — which is what proves the
  ranks are generic rather than sampled.  At `r = 6` the closed form predicts
  61 but the measurement is **55**.  That is not a failure: the closed form
  assumes `per_3` is dense in the `r`-ary cubics, and at `r = 6` it is not
  (rank 50 of 56).  The corrected prediction is `6 + 50 − 1 = 55` — exact.
  The place the formula stops is the place its hypothesis stops, which is a
  free consistency check on both.

## 5. By-product: the determinantal hypersurface has degree at least 6

`D_4^{det_4}` has codimension 1, so its ideal is principal, generated by an
irreducible `GL_4`-semi-invariant `F`; a semi-invariant of degree `e` on
`Sym^4 C^4` has weight `det^e`, i.e. sits at `lam = (e,e,e,e)`.  So `e` is the
least `delta` at which `mult_det((delta^4), delta) < a`.  Measured (and `a`
cross-checked against symmetric-function plethysm):

| `delta` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| `a((delta^4), delta)` | 0 | 0 | 0 | **1** | 0 | 1 | 1 | 3 |
| `mult_det` | – | 0 | 0 | **1** | 0 | – | – | – |

There is no invariant at all in degrees 1, 2, 3, 5, and at `delta = 4` the sole
invariant does **not** vanish on `D_4^{det_4}` (`mult = a = 1`).  Hence
`e >= 6`.  This is consistent with, and independent of, `mult_det = a` at all
nineteen: no length-4 weight can lose ambient room below degree 6.

## 6. Where the gate goes next

Kill criterion 3 fires — `mult_det = a` at all nineteen — but the gate does
**not** simply move to `delta = 6`.  Of the 136 cells at `delta = 6` with
`a >= 2` and `ell >= 4`:

* **65 have `ell = 4`** and are closed by the theorem of §1, at this degree and
  every other;
* **71 have `ell >= 5`** and are genuinely open: the containment argument fails
  there because 5-ary cubics are not all `3x3`-determinantal.

**Nine of the 71 measured** — every cell whose weight space is under 2800,
taken in order of cost:

| `lam` | `ell` | `a` | dim | `mult_det` | `mult_pad` | `D` |
|---|---|---|---|---|---|---|
| (14,5,2,2,1) | 5 | 2 | 1337 | 2 | 2 | 0 |
| (13,5,4,1,1) | 5 | 2 | 1824 | 2 | 2 | 0 |
| (12,7,3,1,1) | 5 | 3 | 1884 | 3 | 3 | 0 |
| (13,6,2,2,1) | 5 | 3 | 1910 | 3 | 3 | 0 |
| (11,8,3,1,1) | 5 | 2 | 2224 | 2 | 2 | 0 |
| (14,4,2,2,2) | 5 | 2 | 2337 | 2 | 2 | 0 |
| (12,7,2,2,1) | 5 | 3 | 2467 | 3 | 3 | 0 |
| (12,6,4,1,1) | 5 | 2 | 2553 | 2 | 2 | 0 |
| (12,5,5,1,1) | 5 | 2 | 2795 | 2 | 2 | 0 |

**Both sides still fill the room at length 5**, in all nine — including three
cells with `a = 3`.  So the pattern that closed length 4 survives the failure
of the argument that explained it: at length 5 there is no containment theorem
to appeal to, and the multiplicities coincide anyway.  Whether that is a second
theorem waiting to be found, or the first 9 of 71 being unrepresentative, is
the open question this session hands on.  The next session should be given
the **`ell >= 5` gate**, not `delta = 6` wholesale — the length axis is the one
that carries the mathematics, and 65 of the 136 cells are already decided.
