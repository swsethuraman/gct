# s38 onset ledger — det-side measurements of `I(D_5^det)`, ell=5

Each row: unreduced `measure(det_4, 16, 4, 5, delta, lam)` (wk8_s30_core, corrected
raising rule), two primes P1=2147483647, P2=2147483629; `a` cross-checked against
the plethysm (`a_expect` assert) and `rank(R) = N_S − a` asserted inside measure;
a rank attaining `a` is a certificate that `det_units = a − mult_det`. A bite
(`mult_det < a`) is re-measured at 3× points and seed 907 before it is believed.

Convention: `det_units = a − mult_det` = multiplicity of `I(D_5^det)` at (lam,delta).
`det_units = 0` ⇔ the cell is empty (no equation); `det_units > 0` ⇔ a bite.

| lam | ell | a | m_det | N_S | mult_det | det_units | note |
|---|---|---|---|---|---|---|---|
| (24, 2, 2, 2, 2) | 5 | 1 | 8 | 619 | 1 | +0 | =a |
| (23, 4, 2, 2, 1) | 5 | 1 | 28 | 900 | 1 | +0 | =a |
| (22, 5, 3, 1, 1) | 5 | 1 | 45 | 1179 | 1 | +0 | =a |
| (21, 7, 2, 1, 1) | 5 | 1 | 38 | 1192 | 1 | +0 | =a |
| (23, 3, 2, 2, 2) | 5 | 1 | 15 | 1349 | 1 | +0 | =a |
| (22, 5, 2, 2, 1) | 5 | 2 | 53 | 1527 | 2 | +0 | =a |
| (20, 8, 2, 1, 1) | 5 | 1 | 45 | 1623 | 1 | +0 | =a |
| (21, 6, 3, 1, 1) | 5 | 1 | 75 | 1849 | 1 | +0 | =a |
| (22, 4, 3, 2, 1) | 5 | 1 | 66 | 2014 | 1 | +0 | =a |
| (19, 9, 2, 1, 1) | 5 | 2 | 59 | 2087 | 2 | +0 | =a |
| (21, 5, 4, 1, 1) | 5 | 2 | 69 | 2285 | 2 | +0 | =a |
| (21, 6, 2, 2, 1) | 5 | 4 | 91 | 2403 | 4 | +0 | =a |
| (18, 10, 2, 1, 1) | 5 | 2 | 57 | 2558 | 2 | +0 | =a |
| (22, 4, 2, 2, 2) | 5 | 3 | 47 | 2625 | 3 | +0 | =a |
| (20, 7, 3, 1, 1) | 5 | 4 | 121 | 2688 | 4 | +0 | =a |
| (17, 11, 2, 1, 1) | 5 | 3 | 62 | 2980 | 3 | +0 | =a |
| (16, 12, 2, 1, 1) | 5 | 2 | 45 | 3331 | 2 | +0 | =a |
| (21, 5, 3, 2, 1) | 5 | 4 | 155 | 3475 | 4 | +0 | =a |
| (20, 7, 2, 2, 1) | 5 | 6 | 134 | 3505 | 6 | +0 | =a |
| (15, 13, 2, 1, 1) | 5 | 2 | 37 | 3553 | 2 | +0 | =a |
| (20, 6, 4, 1, 1) | 5 | 3 | 137 | 3611 | 3 | +0 | =a |
| (19, 8, 3, 1, 1) | 5 | 5 | 162 | 3673 | 5 | +0 | =a |
| (20, 5, 5, 1, 1) | 5 | 3 | 79 | 3946 | 3 | +0 | =a |
| (21, 4, 4, 2, 1) | 5 | 3 | 95 | 3950 | 3 | +0 | =a |
| (21, 5, 2, 2, 2) | 5 | 4 | 77 | 4538 | 4 | +0 | =a |
| (18, 9, 3, 1, 1) | 5 | 7 | 200 | 4730 | 7 | +0 | =a |
| (19, 8, 2, 2, 1) | 5 | 9 | 181 | 4803 | 9 | +0 | =a |

**delta=8 reachable summary (N_S ≤ 5000).** 27 of the 43 reachable cells
(N_S ≤ 9000) measured, all with `mult_det = a` ⇒ `det_units = 0` — every one
empty, two primes, rank(R)=N_S−a asserted, `a` matched to plethysm. No bite.
The remaining 16 reachable cells (5000 < N_S ≤ 9000) and the 392 cells with
N_S > 9000 (the unreduced memory wall; no certified ell=5 reduction available,
see PREREG §0) were not measured this session.
