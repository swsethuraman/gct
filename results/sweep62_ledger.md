# Sweep ledger — the 62 (n = 4, delta = 6, a >= 2, ell >= 5)

Corrected raising rule `E_ij c_alpha = (alpha_i+1) c_{alpha+e_i-e_j}` throughout.
Ranks by python-flint `nmod_mat.rank()` over two word-size primes; `a` checked
independently against the plethysm at every cell; `rank(R) = N_S - a` asserted.

## Session 27's nine, RE-CERTIFIED under the corrected rule — all unchanged

| lam | ell | a | N_S | mult_det | mult_pad | D |
|---|---|---|---|---|---|---|
| (14, 5, 2, 2, 1) | 5 | 2 | 1337 | 2 | 2 | +0 |
| (13, 5, 4, 1, 1) | 5 | 2 | 1824 | 2 | 2 | +0 |
| (12, 7, 3, 1, 1) | 5 | 3 | 1884 | 3 | 3 | +0 |
| (13, 6, 2, 2, 1) | 5 | 3 | 1910 | 3 | 3 | +0 |
| (11, 8, 3, 1, 1) | 5 | 2 | 2224 | 2 | 2 | +0 |
| (14, 4, 2, 2, 2) | 5 | 2 | 2337 | 2 | 2 | +0 |
| (12, 7, 2, 2, 1) | 5 | 3 | 2467 | 3 | 3 | +0 |
| (12, 6, 4, 1, 1) | 5 | 2 | 2553 | 2 | 2 | +0 |
| (12, 5, 5, 1, 1) | 5 | 2 | 2795 | 2 | 2 | +0 |

## The 62, in interleaved order (3 cheapest : 1 most-balanced/largest-a)

| lam | ell | a | N_S | mult_det | mult_pad | D |
|---|---|---|---|---|---|---|
| (13, 5, 3, 2, 1) | 5 | 3 | 2800 | 3 | 3 | +0 |
| (11, 8, 2, 2, 1) | 5 | 3 | 2919 | 3 | 3 | +0 |
| (10, 9, 2, 2, 1) | 5 | 2 | 3176 | 2 | 2 | +0 |
| (10, 7, 4, 2, 1) | 5 | 7 | 8337 | 7 | 7 | +0 |
