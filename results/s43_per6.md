# `I(D_6^{per_3})` in `C[Sym^3 C^6]` above session 41's cap — session 43, Phase B

Continuation of `results/s41_per6.md` (which measured every length-6 weight `μ ⊢ 3δ`, `a(μ,δ) ≥ 1`, with
`n_χ ≤ 6000`).  Same reduced pipeline (`wk9_s36_stabred`, `n = 3`, `r = 6`), points `per_3(Σ s_i A_i)`, both
house primes, `a + 8` points; independent re-check at `3a + 24` points (seed 907, both primes) on any
`mult < a`.  `units = a − mult` is the ideal's share.  By Prop. 8(1) of `docs/transfer_lemma.md`,
`I(D_6^{per_3})_δ = 0` ⇒ `mult_pad = mult_red` at **every** weight of degree `δ`.  `route` is `dense` for the
in-place rref of `analysis/wk9_s41_kernel.py`, `inject` for the `a = 1` sparse injectivity certificate of
`analysis/wk9_s43_inject.py` (pre-registered in `results/PREREG_s43.md` §2 P3, validated before use).

| delta | mu | a | N_S | Stab | n_chi | route | mult | units | secs | HWM |
|---|---|---|---|---|---|---|---|---|---|---|
| 7 | `(9, 4, 3, 2, 2, 1)` | 1 | 11412 | 2 | 6167 | dense | 1 | 0 | 110 | 0.56 |
| 7 | `(7, 5, 4, 3, 1, 1)` | 1 | 17371 | 2 | 6895 | dense | 1 | 0 | 146 | 0.67 |
| 7 | `(6, 6, 4, 2, 2, 1)` | 1 | 25580 | 4 | 6982 | dense | 1 | 0 | 153 | 0.70 |
| 7 | `(8, 5, 3, 2, 2, 1)` | 1 | 15611 | 2 | 8402 | dense | 1 | 0 | 236 | 0.96 |
