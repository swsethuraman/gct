# Session 36 ledger — stabiliser-reduced sweep (`n = 4`, `ell >= 5`, `a >= 2`)

Pipeline: `analysis/wk9_s36_stabred.py` (validated: `results/stabred_validation.md`).
`a` by kernel dimension on the `chi_lam`-isotypic component AND by plethysm (asserted
equal); `rank(R) = n_chi − a` asserted; ranks by python-flint `nmod_mat` over
`2147483647` and `2147483629`; `a + 8` evaluation points per side; certified compressed
kernel (`dim ker(Agg) = a` asserted) above `n_chi = 2500`, exact single-rref route below.
**Points.**  det: `det_4(sum_{i<=r} s_i A_i)`, random integer `4x4` `A_i`.  pad: the
**true padded-permanent restriction** `x_0 · per_3(x_1..x_9)` with each `x_t` a random
linear form in `s_1..s_r` (`per_padded(3,4)` through `restrict()`), at every `r` —
never `l · (random cubic)`, which over-estimates `mult_pad` at `r = 6`
(`dim D_6^{per_3} = 50 < 56`).  Convention `D = mult_pad − mult_det`; only `D > 0` is
an obstruction.  **Stratum A** (`delta = 6, ell = 5`) cannot be permanent-specific
(`docs/s35_review.md` §1); **Stratum B** (`ell = 6`) is the first permanent-sensitive
stratum in the programme.

| stratum | lam | delta | ell | a | N_S | Stab | n_chi | rows | route | mult_det | mult_pad | D | secs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | `(8, 4, 4, 4, 4)` | 6 | 5 | 2 | 94675 | 24 | 4562 | 136845 | compressed | 2 | 1 | -1 | 82 |
| A | `(8, 8, 4, 2, 2)` | 6 | 5 | 3 | 22475 | 4 | 6247 | 34180 | compressed | 3 | 3 | +0 | 110 |
| B | `(13, 8, 4, 1, 1, 1)` | 7 | 6 | 2 | 27213 | 6 | 1844 | 5868 | exact | 2 | 2 | +0 | 20 |
| B | `(12, 9, 4, 1, 1, 1)` | 7 | 6 | 2 | 31812 | 6 | 2199 | 7005 | exact | 2 | 2 | +0 | 30 |
| B | `(13, 7, 5, 1, 1, 1)` | 7 | 6 | 3 | 34984 | 6 | 2455 | 7517 | exact | 3 | 3 | +0 | 37 |
| B | `(12, 8, 5, 1, 1, 1)` | 7 | 6 | 4 | 43371 | 6 | 3106 | 9510 | compressed | 4 | 4 | +0 | 21 |
