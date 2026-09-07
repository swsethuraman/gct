# Integrator note 2 to session 64 — both mid-session findings confirmed, and one correction to note 1

## 1. The padded family is already wired into the engine — confirmed

`per_padded(3,4)` is in `wk8_s30_core`, and `analysis/wk9_s41_kernel.py` line 134
carries

    forms = dict(det=(DET4, N_DET), pad=(PAD34, N_PAD))

so the padded quartic sits beside `det_4` in the evaluation path already, and
`ev_rows_arr` (`analysis/wk9_s45_build.py`) restricted to a random `r`-plane
does produce `ℓ(s)·per_3(A(s))`.  Session 36 says as much in
`wk9_s36_stabred.py`.  The session's reading is right, and note 1's instruction
to "implement `ev_pad`" is superseded: **it exists; validate it, do not build
it.**

This is the **third** item this batch that was described as missing and turned
out to be banked — after the Gram double-coset observation (session 56) and the
`h_pad` Pieri identity (session 42).  The common cause is that batch 10 was
planned from documents and summaries rather than from the code, and each time
the code was ahead.  Worth recording as a lesson rather than as three
coincidences.

## 2. `P_5 = R_5` — confirmed, with the reason

Reproduced independently (`analysis/wk10_int_percubic.py`, Jacobian rank of
`M ↦ per_3(M)` at three random `3×3` matrices of linear forms, both house
primes' arithmetic, `9r` parameters against `C(r+2,3)` targets):

| `r` | params `9r` | target | image dim | |
|---|---|---|---|---|
| 3 | 27 | 10 | **10** | dominant |
| 4 | 36 | 20 | **20** | dominant |
| 5 | 45 | 35 | **35** | dominant |
| 6 | 54 | 56 | 50 | deficit 6 |
| 7 | 63 | 84 | 59 | deficit 25 |

The threshold is exactly where the session put it.  And the table gives the
reason in closed form: the image dimension is `50 = 54 − 4` at `r = 6` and
`59 = 63 − 4` at `r = 7`, so **the generic fibre is 4-dimensional at every `r`**
— it is the projective torus of `per(D_1 M D_2)`, of dimension
`(3−1) + (3−1) = 4`.  Hence

    dim image  =  min( 9r − 4 ,  C(r+2,3) ) ,   dominant  ⟺  9r − 4 ≥ C(r+2,3)
                                                          ⟺  r ≤ 5

`41 ≥ 35` at `r = 5`, `50 < 56` at `r = 6`.  That is a better statement than
"checked at `r ≤ 5`", and it matches the transfer lemma's threshold exactly.

## 3. Correction to note 1 §4 — the kernel calibration is stronger than I said

I wrote that at `(8,4,4,4,4)`, `δ = 6` the engine must return
`mult_pad ∈ {0,1}`, stating it as an inequality because the record pins
`mult_red = 1` and `h_pad = 1` but not `mult_pad`.

**With `P_5 = R_5` that is too weak.**  At `r = 5` the two varieties coincide, so

    mult_pad = mult_red   exactly, at every r = 5 cell

and the calibration is pinned: **`mult_pad = 1`, in a two-dimensional source.**
An engine returning 0 is as defective as one returning 2.

The same upgrade applies to the whole calibration set: session 60's banked
reducible corpus at `r = 5` is now **direct ground truth** for the padded
engine, not an upper bound.  That is a far stronger validation set than note 1
credited, and it is available immediately.

## 4. The caution that comes with it — calibrate above `r = 5` as well

`P_r = R_r` for `r ≤ 5` cuts both ways.  **No `r ≤ 5` calibration can
distinguish a correct padded engine from one that has silently implemented the
reducible side instead** — at those lengths the two agree by theorem, so every
test passes either way.

So before any padded number at `r = 9` is trusted, the engine must be exercised
at `r ≥ 6`, where the deficit is 6 and the two sides genuinely separate.  A
cheap and decisive version: check that the padded evaluation at `r = 6` lands in
a proper subvariety of the reducible one — for instance that some cubic in six
variables outside the permanental image is rejected — or simply that
`mult_pad < mult_red` at a cell where the record has `mult_red` and the deficit
should bite.  **Report an `r ≥ 6` separation test before reporting any LMR
padded rank.**  Without it, a passed calibration suite proves only that the
engine agrees with `R_r` where `R_r` is all there is.

## 5. Unchanged from note 1

`h_pad(LMR) = 521`, so the pad-side ceiling is vacuous at the goal cell and a
rank is genuinely required.  And the composite identity
`mult_pad = rank[(⊕_μ Θ^{per_3}_{μ,δ}) ∘ S_{λ,δ}]` remains the one load-bearing
claim of the external memo that is neither reproduced here nor banked — the
`r = 5` calibrations test it, and now they test it as an equality.
