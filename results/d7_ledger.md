# Sweep ledger — delta = 7 (n = 4, a >= 2, ell >= 5), the 46 feasible cells
#
# Corrected raising rule E_ij c_alpha = (alpha_i+1) c_{alpha+e_i-e_j} throughout.
# Ranks by python-flint nmod_mat.rank() over primes 2147483647, 2147483629;
# a checked against the plethysm at every cell; rank(R) = N_S - a asserted;
# N_S asserted equal to the census DP value.  D := mult_pad - mult_det;
# an obstruction is D > 0 only (PREREG_s34.md section 0).
# flag: "" normal | DEFER-MEM attempted, deferred (memory) -- not a measurement
#       | EXT beyond the pre-registered frontier | bite:* sceptical branch banked
#
| lam | ell | a | N_S | mult_det | mult_pad | D | flag |
|---|---|---|---|---|---|---|---|
| (18, 5, 2, 2, 1) | 5 | 2 | 1482 | 2 | 2 | +0 |  |
| (15, 9, 2, 1, 1) | 5 | 2 | 1761 | 2 | 2 | +0 |  |
| (17, 5, 4, 1, 1) | 5 | 2 | 2155 | 2 | 2 | +0 |  |
| (13, 11, 2, 1, 1) | 5 | 2 | 2207 | 2 | 2 | +0 |  |
| (17, 6, 2, 2, 1) | 5 | 4 | 2257 | 4 | 4 | +0 |  |
| (16, 7, 3, 1, 1) | 5 | 4 | 2414 | 4 | 4 | +0 |  |
| (18, 4, 2, 2, 2) | 5 | 3 | 2565 | 3 | 3 | +0 |  |
| (15, 7, 4, 1, 1) | 5 | 8 | 4510 | 8 | 8 | +0 |  |
| (15, 8, 3, 1, 1) | 5 | 4 | 3127 | 4 | 4 | +0 |  |
