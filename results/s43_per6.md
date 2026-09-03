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
| 7 | `(7, 6, 3, 2, 2, 1)` | 1 | 18214 | 2 | 9789 | dense | 1 | 0 | 383 | 1.22 |
| 7 | `(7, 5, 4, 2, 2, 1)` | 1 | 23438 | 2 | 12564 | dense | 1 | 0 | 717 | 1.96 |
| 7 | `(6, 5, 4, 3, 2, 1)` | 1 | 39921 | 1 | 39921 | inject | 1 | 0 | 482 | 0.15 |

**δ = 7 — CLOSED.  All 27 length-6 weights `μ ⊢ 21` with `a(μ,7) ≥ 1` are now measured (20 by session 41 at
`n_χ ≤ 6000`, 6 here by the dense route, 1 here by the `a = 1` injectivity certificate), every one with
`mult = a = 1`: `I(D_6^{per_3})_7 = 0` outright.  By Prop. 8(1) of `docs/transfer_lemma.md`,
`I(P_6)_7 = I(R_6)_7` and `mult_pad = mult_red` at *every* weight of degree 7 — a theorem, with no points in
it.  The last weight, `(6,5,4,3,2,1)`, has trivial stabiliser and `n_χ = N_S = 39,921`, about twice the dense
frontier; its `[M;Ev]` (134,212 × 39,921, nnz 801,854) was certified NONSINGULAR at both primes by a
Berlekamp–Massey minimal polynomial of degree exactly `n_χ` with `f(0) ≠ 0`, in 482 s at a peak of 0.15 GB.**
| 8 | `(7, 7, 6, 2, 1, 1)` | 1 | 31850 | 4 | 6297 | dense | 1 | 0 | 120 | 0.59 |
| 8 | `(11, 4, 4, 2, 2, 1)` | 2 | 23324 | 4 | 6512 | dense | 2 | 0 | 131 | 0.62 |
| 8 | `(10, 6, 4, 2, 1, 1)` | 2 | 16865 | 2 | 6542 | dense | 2 | 0 | 120 | 0.62 |
| 8 | `(10, 4, 4, 2, 2, 2)` | 2 | 65440 | 12 | 6929 | dense | 2 | 0 | 161 | 0.75 |
| 8 | `(12, 4, 3, 2, 2, 1)` | 1 | 13264 | 2 | 7200 | dense | 1 | 0 | 157 | 0.73 |
| 8 | `(9, 5, 5, 3, 1, 1)` | 3 | 37274 | 4 | 7385 | dense | 3 | 0 | 175 | 0.77 |
| 8 | `(11, 4, 3, 2, 2, 2)` | 1 | 37634 | 6 | 7749 | dense | 1 | 0 | 199 | 0.86 |
| 8 | `(9, 7, 4, 2, 1, 1)` | 2 | 19922 | 2 | 7775 | dense | 2 | 0 | 193 | 0.84 |
| 8 | `(9, 5, 4, 4, 1, 1)` | 1 | 43096 | 4 | 8670 | dense | 1 | 0 | 272 | 1.01 |
| 8 | `(8, 8, 3, 2, 2, 1)` | 1 | 34084 | 4 | 9263 | inject | 1 | 0 | 37 | 0.36 |
| 8 | `(7, 7, 5, 3, 1, 1)` | 1 | 49473 | 4 | 9901 | inject | 1 | 0 | 41 | 0.36 |
| 8 | `(8, 6, 4, 4, 1, 1)` | 1 | 53424 | 4 | 10777 | inject | 1 | 0 | 47 | 0.36 |
