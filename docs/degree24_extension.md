# Route (i): the divisorial extension argument, and why it cannot decide

Session 21, 2026-08-30.  This settles the "try it by hand first" branch of the
degree-24 brief — in the negative, but with a corollary worth keeping.

## The set-up

On the dense orbit `O = G . det_3` define

    phi(g . det_3) = det(g)^2 .

This is well defined: for `h` in `H = stab(det_3)` we have `det(h) = ±1`
(the `X -> AXB` component has `det = (det A det B)^3 = 1`, and the transpose
coset has `det = (-1)^3 = -1`), so `det(h)^2 = 1`.  `phi` is a regular
`SL_9`-invariant function of degree 6 on the orbit, and every `SL_9`-invariant
of degree `6k` on the orbit is a scalar multiple of `phi^k`.  This is
Buergisser-Ikenmeyer Lemma 3.2 in our normalisation, and it is the reason
`b(det_3) = 6`.  Hence

    E(det_3) = { 6k : phi^k extends regularly to Omega-bar } .

Restriction of `Phi_18` to the orbit is `Phi_18(det_3) . phi^3`, so
`Phi_18|_O = Phi_18(det_3) . phi^3` as rational functions on `Omega-bar`.

## The argument, and where it breaks

From `div(Phi_18|_O) = 6P_1 + 9P_2` (Proposition `prop:divisor`) and
`Phi_18|_O = const . phi^3`:

    3 . ord_{P_1}(phi) = 6,    3 . ord_{P_2}(phi) = 9,

so

    ord_{P_1}(phi) = 2,    ord_{P_2}(phi) = 3,    div(phi) = 2P_1 + 3P_2 >= 0 .

Now `phi^4` has divisor `8P_1 + 12P_2 >= 0`, and the divisorial argument would
conclude that `phi^4` extends regularly, i.e. `24` in `E`.

**That argument is invalid, and provably so.**  The very same argument applied
to `phi^1` gives `div(phi) = 2P_1 + 3P_2 >= 0` and would conclude `6` in `E`.
But `6` is not in `E`: the ambient census gives
`dim C[Sym^3 C^9]^{SL_9}_6 = 0`, so there is no degree-6 invariant to restrict,
and independently `min E = e(det_3) = 18`.  The divisorial calculus therefore
predicts a false statement at `k = 1`, and nothing it says at `k = 4` can be
trusted.

The reason is not subtle once stated: "effective divisor implies regular" is
Serre's criterion, and it needs `Omega-bar` **normal**.  The orbit closure of
`det_n` is not normal for `n > 2` (Kumar), and `P_2` is exactly where the
non-normality sits — the paper already says so, and says that the two
multiplicities `6` and `9` are not both read off the character for that reason.
Route (i) is dead.  No divisor computation on `Omega-bar` can decide degree 24,
because divisors only see the normalisation.

## The corollary that survives (and is new)

The failed argument is a correct statement about the normalisation.  Let
`nu : Omega-bar^nu -> Omega-bar` be the normalisation.  Since
`div(phi) = 2P_1 + 3P_2` is effective and `Omega-bar^nu` is normal and affine,

    phi  in  C[Omega-bar^nu] ,

and therefore

    C[Omega-bar^nu]^{SL_9} = C[phi],   a polynomial ring,   with degree
    monoid exactly 6N .

So the invariant ring of the closure sits inside a polynomial ring on one
generator of degree 6:

    C[Omega-bar]^{SL_9}  =  C[S]  subset  C[phi]  =  C[Omega-bar^nu]^{SL_9},
    S = E(det_3)/6  a numerical semigroup.

`S` is a numerical semigroup of multiplicity 3: `3` in `S` (that is
`e = 18`), `1, 2` not in `S`, `gcd S = 1`.  Its **gaps are exactly the degrees
at which the non-normality of `Omega-bar` is arithmetically visible on
invariants**, and the conductor of the semigroup `S` is literally the conductor
of `C[Omega-bar]^{SL_9}` in its normalisation.  This is the programme's own
conductor notion, applied to the invariant ring itself rather than to a
Peter-Weyl weight; degree 24 asks whether `4` is in `S`.

Known gaps so far: `1, 2` (degrees 6 and 12).  A numerical semigroup of
multiplicity 3 with `1, 2` gaps is `<3, 3a+1, 3b+2>` for the smallest
`3a+1` and `3b+2` it contains; degree 24 asks for the first, degree 30 for the
second.

## What replaced route (i)

The ambient census (`analysis/wk4_s21_census.py`) gives
`dim C[Sym^3 C^9]^{SL_9}_24 = 1`, so the degree-24 ambient invariant `Phi_24`
is unique up to scale and

    24 in E   <=>   Phi_24(det_3) != 0 ,

with a zero as decisive as a nonzero.  That is the computation actually run.
