# Session 68 — per-rung cost, support and by-products (validation ladders)

All cells built and solved exactly over F_p at both house primes;  = flint
nullity of E, cross-checked by the plethysm  at every cell (V-check, all
match). Births = , recovered by the transport+deflate construction
and certified by the three-part rung certificate (all True, both primes).
 = fraction of n_χ the highest-weight space touches;  = the
u-free column fraction (where births are represented as a quotient); 
by the s45 evaluation pairing.

| ladder | δ | λ | n_χ | \|Stab\| | N_S | a | role | birth (=aδ−aδ₋₁) | cert | supp(HWV) | idx0-free% | i_det | i_pad | build s | cert s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L1 | 5 | (8, 6, 4, 2) | 939 | 1 | 939 | 3 | seed | 3 (seed) | PASS | 0.950 | 69.3% | 0 | 0 | 1.6 | 0.0 |
| L1 | 6 | (12, 6, 4, 2) | 1626 | 1 | 1626 | 11 | rung | 8 / 8 | PASS | 0.999 | 42.2% | 0 | 0 | 4.4 | 6.2 |
| L1 | 7 | (16, 6, 4, 2) | 2087 | 1 | 2087 | 18 | rung | 7 / 7 | PASS | 0.997 | 22.1% | 0 | 0 | 7.5 | 11.5 |
| L1 | 8 | (20, 6, 4, 2) | 2318 | 1 | 2318 | 22 | rung | 4 / 4 | PASS | 0.992 | 10.0% | 0 | 0 | 9.4 | 15.2 |
| L2 | 4 | (6, 4, 4, 2) | 160 | 2 | 288 | 1 | seed | 1 (seed) | PASS | 1.000 | 79.4% | 0 | 0 | 0.0 | 0.0 |
| L2 | 5 | (10, 4, 4, 2) | 312 | 2 | 572 | 3 | rung | 2 / 2 | PASS | 0.974 | 48.7% | 0 | 0 | 0.1 | 0.2 |
| L2 | 6 | (14, 4, 4, 2) | 416 | 2 | 764 | 5 | rung | 2 / 2 | PASS | 1.000 | 25.0% | 0 | 0 | 0.3 | 0.5 |
| L2 | 7 | (18, 4, 4, 2) | 463 | 2 | 850 | 6 | rung | 1 / 1 | PASS | 0.937 | 10.2% | 0 | 0 | 0.3 | 0.6 |
| L2 | 8 | (22, 4, 4, 2) | 479 | 2 | 877 | 6 | rung | 0 / 0 | PASS | 0.906 | 3.3% | 0 | 0 | 0.4 | 0.7 |

## Certificate detail (per rung, both primes)

(i) transported vectors ∈ ker E (full E) and J injective; (ii) dim ker[E;R] = birth
and R nonsingular on J(M_{δ−1}); (iii) new vectors pass full raising and
span(J(M_{δ−1}) ⊕ B_δ) = ker_Q E_δ. Every box below is True at P1 and P2.

| ladder | δ | transport_rank (=n_χ prev) | transported_rank (=a_prev) | (i) | (ii) birth | (ii) R⊥J | (iii) raise | (iii) complete |
|---|---|---|---|---|---|---|---|---|
| L1 | 6 | 939 | 3 | True | True | True | True | True |
| L1 | 7 | 1626 | 11 | True | True | True | True | True |
| L1 | 8 | 2087 | 18 | True | True | True | True | True |
| L2 | 5 | 160 | 1 | True | True | True | True | True |
| L2 | 6 | 312 | 3 | True | True | True | True | True |
| L2 | 7 | 416 | 5 | True | True | True | True | True |
| L2 | 8 | 463 | 6 | True | True | True | True | True |
