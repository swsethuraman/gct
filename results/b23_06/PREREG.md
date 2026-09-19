# B23-06 pilot 1 — pre-registration (written before any launch)

Run name: `b23_06_p1_cellprice`. Wrapper: `analysis/b15_bound.py --seconds 60 --memory-mb 512 --slot 02`.
Script: `analysis/b23_06_p1_cellprice.py`. The sha256 of this file is passed to the script and
written into its JSON output (G25).

## What it computes (pricing only; no multiplicity, no rank, no evaluation at any point)

For `(n, r, d)` it computes the full weight-multiplicity function of `Sym^d(Sym^n C^r)` (the
coordinate ring of `n`-ics in `r` variables in degree `d`), exactly, in unsigned 32-bit
integers. It does this by an unbounded-knapsack DP over the `C(n+r-1, r-1)` exponent vectors.
From that it computes, for every partition `lambda ⊢ nd` with exactly `r` parts:

- `N_S(lambda)` = the dimension of the `lambda`-weight space, which is the size of the linear
  algebra that finds highest-weight vectors (the programme's cost driver: B19-02 §8.1 `K`,
  B20/det_onset `N_S`);
- `a(lambda)` = the multiplicity of `S_lambda(C^r)`, by Weyl alternation over `S_r`.

Configurations, in order: `(4,5,5)` control, `(5,5,5)`, `(6,5,5)`. A deadline guard skips a
configuration if under 15 s remain. JSON is rewritten after each configuration.

It also emits, by exact integer arithmetic: `dim Sym^4 C^16`, `dim Sym^5 C^25`, `cap(n)` for
`n = 2..7`, `C(n,k)^2` for the flattening ranks, and `log10` of the average weight-space
dimension `dim Sym^d(Sym^n C^r) / #weights` at the configurations `(5,6,6)`, `(6,6,6)`,
`(n, 5, cap(n))` for `n = 4, 5, 6`, and `(4, 9, 24)` (the record's LMR cell, for calibration).

## Controls, stated as identities (G21)

- C1: `N_S((4^5))` at `(n,r,d) = (4,5,5)` equals **19834** (B19-02 §8.1, "weight-space dimension K").
- C2: `a((4^5))` at `(4,5,5)` equals **1** (B19-02 §8.1).
- C3: the number of `lambda ⊢ 20` with exactly 5 parts and `a > 0` at `(4,5,5)` equals **23**
  (B19-02 §8, "all 23 five-row cells at d = 5", ADOPTED from B18).
- C4: `sum over all lambda ⊢ nd with <= r parts of a(lambda) · dim S_lambda(C^r) = C(M+d-1, d)`
  with `M = C(n+r-1, r-1)`. This is a total-dimension identity, checked with the Weyl dimension
  formula at every configuration run.
- C5: `dim Sym^4 C^16 = 3876`, `dim Sym^5 C^25 = 118755`; `cap(n) = 5, 65, 300, 900, 2125, 4305`
  for `n = 2..7`.

If C1–C4 fail at `(4,5,5)`, no other configuration's numbers are reported as results.

## Expectation (a prediction, not a claim)

At `(5,5,5)` and `(6,5,5)` I expect the cheapest non-rectangular five-row cell with `a > 0`
to have `N_S` between `10^3` and `10^5`, and the central cells to reach `10^5`–`10^6`. I have
no derivation of either figure.

## Price

Memory: uint32 layers `(nk+1)^5` for `k = 0..5`. At `n = 6` that is about 41M entries, or
165 MB, the largest configuration. Time: about `sum_k (n(k-1)+1)^5` adds per exponent vector:
about `6.7·10^8` element-adds at `n = 5` and `2.6·10^9` at `n = 6`, in numpy. Expected under
40 s total. If the wall is hit at `n = 6`, that configuration is recorded as skipped.
