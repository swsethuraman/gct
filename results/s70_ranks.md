# Session 70 — the reducible-normalisation split `S`: exact ranks

`S = S_{λ,δ} : M⁴_λ → ⊕_μ M³_μ`, the split (comultiplication) map into the
degree-`δ` normalisation `D_δ = Sym^δ V ⊗ Sym^δ Sym³V`; `rank S = mult_red`,
`i_red = a − rank S`. Code `analysis/wk11_s70_split.py`; raw
`results/s70_ranks.jsonl`; certificates `results/certs/s70/*_split.json`. Both
house primes `2147483647, 2147483629`, and two independent codomain multiset-hash
seeds; the `(★)/E_red` route `rank kern[:,¬red]` (docs/reducible_ideal.md Thm 1)
computed on the **same** HWVs as an independent confirmation.

| λ | δ | a | h_pad | **rank S** | i_red | banked mult_red | (★) route | primes×seeds | n_χ | N_S | μ\* terms | role |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| (10,6,4,2,2) | 6 | 6 | 24 | **6** | 0 | 6 (= a, s42 anchor) | 6 | 6,6,6,6 | 9743 | 17 932 | 3.59 M | full-rank control |
| (8,4,4,4,4) | 6 | 2 | 1 | **1** | 1 | 1 | 1 | 1,1,1,1 | 4562 | 94 675 | 30.04 M | discriminating (bite) |
| (12,9,9,1,1) | 8 | 7 | 6 | **5** | 2 | 5 | 5 | 5,5,5,5 | 9800 | 49 820 | 35.59 M | discriminating (bite) |

**Reading.** The instrument is two-sided. At the non-bite anchor `(10,6,4,2,2)₆`
it returns `rank S = a = 6` (`i_red = 0`) — it does **not** spuriously drop rank.
At the two bites it returns exactly the banked reduced value, `1 < 2` and
`5 < 7` — the regime that matters at LMR (`rank S < a`). Every entry agrees across
both primes, both hash seeds, the `(★)` route, and the session-60/64 banked
record. A construction returning `a` at either bite would be wrong; none does.

Costs (this 2-core / 7 GB container): the `μ*` split rank is 11 s
(`(10,6,4,2,2)₆`) to 162 s per cell; the binding cost is the shared dense HWV
kernel of `E` (30–166 s per prime). `μ*` expansion is 30–36 M terms in 12–14 s.

Falsifiers (PREREG §2): **F-B1** (`rank S ≠ banked`) unfired; **F-B2** (prime /
seed disagreement) unfired; **F-B3** (`(★)` disagreement) unfired.
