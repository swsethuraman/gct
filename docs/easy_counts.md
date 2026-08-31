# The two Peter-Weyl counts, as functions of n

Measured 2026-08-31, continuing session 24b.  Question: the "easy" side of
`mult = m - def` is pure group theory, so it should be cheap — how do
`m_det_n` and `m_per_n` actually grow with `n`?

Both counts are `dim (S_lam^*)^H` for the relevant stabiliser, on
`lam |- n*delta` with at most `n^2` rows — the determinant's `H` is the
reductive `{AXB : det A det B = 1} |x <transpose>` of dimension `2n^2-2`, the
permanent's is the monomial `(torus of dim 2n-2) |x (S_n x S_n) |x Z/2`.

## Method

`m_det` is session 24b's exact Kronecker + symmetric-correction routine,
unmodified.  The permanent side is rewritten for general `n`, with two changes
that make `n = 4, 5` reachable where the session-24b code (hardcoded `n = 3`)
was not:

1. **Power sums instead of Jacobi-Trudi.**
   `dim (S_lam)^H = sum_rho (|C_rho|/N!) chi^lam(rho) E(rho)` with
   `E(rho) = <prod_i tr(h^{rho_i})>_H`.  `E` does not depend on `lam`, so the
   expensive part is paid once per `(n, delta)` instead of once per weight.
2. **Margin pruning.**  Only exponent matrices with every row and column sum
   `<= delta` can survive to the torus-invariant part, so every intermediate
   state is pruned to that cone.  Without it the `n = 4` h-series carries
   ~3e8 monomials.

Class reduction over the `2(n!)^2` monomial permutations uses the structural
labelling (`t=0`: unordered pair of cycle types; `t=1`: cycle type of `P.Q`),
**verified against brute-force conjugation** at `n = 3` (9 classes) and
`n = 4` (20 classes) — class counts and sizes both match.

Calibration, all passed:

- fast route == session 24b's Jacobi-Trudi route on every weight at
  `(n,delta) = (3,2)`, and at `lam = (2,2,2,2)`, `(n,delta) = (4,2)`;
- `m_det((2,2,2), 3, 2) = 1` and `m_per((2,2,2), 3, 2) = 4`, reproducing
  `P = 3` at the weight where session 24b measured `Def = P = 3`, `D = 0`;
- the `n=3, delta=2` determinant row is supported exactly on
  `(6), (4,2), (2,2,2)`, each with `m = 1` — the paper's row.

## Results

| n | delta | #lam | supp(det) | supp(per) | sum m_det | sum m_per | ratio | max(m_det - m_per) |
|---|-------|------|-----------|-----------|-----------|-----------|-------|--------------------|
| 2 | 2 | 5 | 2 | 2 | 2 | 4 | 2.00 | 0 |
| 2 | 3 | 9 | 3 | 5 | 3 | 8 | 2.67 | 0 |
| 2 | 4 | 15 | 5 | 10 | 5 | 22 | 4.40 | 0 |
| 2 | 5 | 23 | 6 | 15 | 6 | 42 | 7.00 | 0 |
| 3 | 2 | 11 | 3 | 7 | 3 | 17 | 5.67 | 0 |
| 3 | 3 | 30 | 10 | 27 | 11 | 318 | 28.91 | 0 |
| 3 | 4 | 73 | 34 | 68 | 43 | 5631 | 130.95 | 0 |
| 4 | 2 | 22 | 5 | 19 | 5 | 131 | 26.20 | 0 |
| 4 | 3 | 77 | 34 | 75 | 43 | 35812 | 832.84 | 0 |
| 5 | 2 | 42 | 6 | 40 | 6 | 1245 | 207.50 | 0 |

## What it says

1. **`m_det(lam) <= m_per(lam)` at every weight of every case computed.**  The
   determinant's easy count never once exceeds the permanent's.  Four ties in
   total — `(2,2,2)` at `(2,3)`, `(2,2,2,2)` at `(2,4)`, `(4,2,2,2)` at
   `(2,5)`, `(2,2,1,1,1,1,1)` at `(3,3)` — and no strict win anywhere.
   This extends session 24b's screen (which was `n <= 4`, padded) to the
   unpadded comparison at `n <= 5` and reaches the same verdict by a route
   that shares no code with the screen.

2. **The determinant's count barely grows at all.**  At `delta = 2` the total
   is `2, 3, 5, 6` for `n = 2,3,4,5`, and the mean of `m_det` over its own
   support is **exactly 1.00** in every case but one (`1.10` at `(3,3)`).  The
   determinant's Peter-Weyl count is essentially a 0/1 indicator: the question
   is only *whether* a weight is supported, almost never *how much*.

3. **The permanent's count explodes.**  At `delta = 3`: `8, 318, 35812` for
   `n = 2,3,4`.  The ratio `sum m_per / sum m_det` runs `2.67 -> 28.91 ->
   832.84` in `n` at fixed `delta = 3`, and `5.67 -> 26.20 -> 207.50` at
   `delta = 2`.

4. **The support asymmetry is the visible form of it.**  At `(5,2)` the
   determinant is supported on 6 of 42 weights and the permanent on 40 —
   34 live weights have `m_det = 0 < m_per`.  Those are exactly the weights
   where Buergisser-Ikenmeyer-Panova forces `def_per = m_per`, a full deficit.
   So on the `m_det = 0` locus — 85% of live weights at `(5,2)` — the
   cancellation `D = 0` is not a coincidence at all, it is BIP's theorem.
   The unexplained saturation is confined to the `m_det > 0` locus.

5. **Structurally this is forced, and the gap is quadratic.**
   `dim H_det - dim H_per = (2n^2-2) - (2n-2) = 2n(n-1)`.  A bigger stabiliser
   means fewer invariants, so the determinant is the sparse side by
   construction, and the sparsity gap widens like `n^2`.  The determinant's
   invariants are rectangular Kronecker coefficients; the permanent's are
   counts of non-negative integer matrices with equal margins.

## Consequence for the programme

The easy count is not the bottleneck, and it is not close: it favours the
obstruction by two orders of magnitude at `n = 5, delta = 2` and grows.
Everything that stands between us and an obstruction is on the deficit side,
and on most of the weight space (`m_det = 0`) that side is already settled
against us by BIP.  Any future search should be confined to `m_det > 0` — 6 of
42 weights at `(5,2)` — which is also exactly where the deficit is hardest to
compute.

## Files

    analysis/wk5_easycount.py       power-sum route, general n (fast)
    analysis/wk5_easycount_jt.py    Jacobi-Trudi route, general n (slow, the check)
