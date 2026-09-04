# `I(D_6^{per_3})_8` — the last nine weights — session 47, Phase C2

Session 41 measured 28 of the 91 length-6 weights `μ ⊢ 24` with `a(μ,8) ≥ 1` in
`Sym^8(Sym^3 C^6)`; session 43 measured 54 more.  All 82 are **empty**
(`mult = a`).  This table measures the **nine** that were left.

*(The brief says "81 of the 91 ... the 10 remaining".  Re-enumerating the
weights here and re-parsing `results/s41_per6.md` and `results/s43_per6.md`
gives 91 total, **82** measured — 28 + 54, disjoint, every `a` agreeing with an
independent plethysm recomputation — and **9** outstanding.  The count is off by
one; the list below is the true remainder.)*

Route: the sparse injectivity certificate `analysis/wk9_s43_inject.py`
(`inject_one`), unchanged, both house primes, `a + 8` points
`per_3(Σ s_i A_i)`.  `[M; Ev]` nonsingular at one prime proves `mult = a` at
that prime; the two primes are asserted to agree.  A kernel vector would prove
`mult < a` and would be the **first permanent-specific equation the programme
has seen** — the run halts there.

If all nine are empty then `I(D_6^{per_3})_8 = 0` outright, and by Prop. 8(1)
of `docs/transfer_lemma.md`, **`mult_pad = mult_red` at every weight of degree
8** — the degree at which every pad-side bite in the six-row record lives.

| `μ` | `a` | `N_S` | Stab | `n_χ` | route | `mult` | units | secs |
|---|---|---|---|---|---|---|---|---|
| `(7, 5, 4, 4, 2, 2)` | 1 | 285313 | 4 | 76792 | inject | 1 | 0 | 2420 |
| `(6, 6, 5, 4, 2, 1)` | 1 | 162385 | 2 | 81865 | inject | 1 | 0 | 2326 |
| `(8, 6, 4, 3, 2, 1)` | 3 | 87432 | 1 | 87432 | inject | 3 | 0 | 2062 |
| `(8, 5, 4, 3, 2, 2)` | 1 | 186426 | 2 | 98732 | inject | 1 | 0 | 2836 |
| `(6, 5, 5, 3, 3, 2)` | 1 | 427388 | 4 | 103510 | inject | 1 | 0 | 6159 |
| `(7, 5, 4, 4, 3, 1)` | 1 | 209713 | 2 | 106508 | inject | 1 | 0 | 4508 |
| `(7, 6, 5, 3, 2, 1)` | 2 | 114502 | 1 | 114502 | inject | 2 | 0 | 3759 |
| `(7, 6, 4, 3, 2, 2)` | 1 | 219449 | 2 | 116083 | inject | 1 | 0 | 4564 |
| `(6, 5, 5, 4, 3, 1)` | 1 | 256941 | 2 | 127182 | inject | 1 | 0 | 7884 |

**All 9 are empty.**  With session 41's 28 and session 43's 54 — 82 weights, all empty — every one of the 91 length-6 weights `μ ⊢ 24` with
`a(μ, 8) ≥ 1` in `Sym^8(Sym^3 C^6)` has `mult = a`, so

> **`I(D_6^{per_3})_8 = 0`** (proved: a nonsingularity certificate at one prime
> proves `mult = a`, and both house primes agree at every weight), and by
> Prop. 8(1) of `docs/transfer_lemma.md`, **`mult_pad = mult_red` at every
> weight of degree 8** — the degree at which every pad-side bite in the six-row
> record lives.  There is no permanent-specific equation in degree 8.

With session 43's `I(D_6^{per_3})_7 = 0` and session 37's `δ ≤ 6`, the
permanent is now proved invisible on the reducible side through degree 8.
