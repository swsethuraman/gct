# Verifier report

362 certificate file(s); verifier tools/verify at 2026-09-06 UTC (run in two halves of 181 files each, results/logs/s60_verify_a.log and s60_verify_b.log)
PASS 362, FAIL 0, UNPARSEABLE 0, ERROR 0

## PASS — `results/certs/s60/10_10_6_1_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((10, 10, 6, 1, 1), 7) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (0.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (10, 10, 6, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis: 1 independent vectors = a — rank 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded det_pencil points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/10_10_6_1_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((10, 10, 6, 1, 1), 7) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (0.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (10, 10, 6, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis: 1 independent vectors = a — rank 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded reducible points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_reducible(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/10_5_3_1_1_d5_det_pencil_p2147483629.json.gz`

*mult_det_pencil((10, 5, 3, 1, 1), 5) = a = 1, mod 2147483629, length-5 balanced complement (session 60)*  (1.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (10, 5, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 20 vs 4*5
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 774, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded det_pencil points has rank a mod 2147483629 — rank 1
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/10_5_3_1_1_d5_det_pencil_p2147483647.json.gz`

*mult_det_pencil((10, 5, 3, 1, 1), 5) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (1.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (10, 5, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 20 vs 4*5
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 774, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded det_pencil points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/10_5_3_1_1_d5_reducible_p2147483629.json.gz`

*mult_reducible((10, 5, 3, 1, 1), 5) = a = 1, mod 2147483629, length-5 balanced complement (session 60)*  (1.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (10, 5, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 20 vs 4*5
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 774, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded reducible points has rank a mod 2147483629 — rank 1
- [x] conclusion: mult_reducible(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/10_5_3_1_1_d5_reducible_p2147483647.json.gz`

*mult_reducible((10, 5, 3, 1, 1), 5) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (1.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (10, 5, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 20 vs 4*5
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 774, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded reducible points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_reducible(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/10_7_5_1_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((10, 7, 5, 1, 1), 6) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (10, 7, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/10_7_5_1_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((10, 7, 5, 1, 1), 6) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (10, 7, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/10_8_2_2_2_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((10, 8, 2, 2, 2), 6) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (1.0s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (10, 8, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/10_8_2_2_2_d6_reducible_p2147483647.json.gz`

*mult_reducible((10, 8, 2, 2, 2), 6) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.9s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (10, 8, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/10_8_4_1_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((10, 8, 4, 1, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (10, 8, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/10_8_4_1_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((10, 8, 4, 1, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (10, 8, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/10_9_2_2_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((10, 9, 2, 2, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (10, 9, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/10_9_2_2_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((10, 9, 2, 2, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (10, 9, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/11_11_4_1_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((11, 11, 4, 1, 1), 7) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (1.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (11, 11, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/11_11_4_1_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((11, 11, 4, 1, 1), 7) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (1.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (11, 11, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/11_4_2_2_1_d5_det_pencil_p2147483629.json.gz`

*mult_det_pencil((11, 4, 2, 2, 1), 5) = a = 1, mod 2147483629, length-5 balanced complement (session 60)*  (1.1s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (11, 4, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 20 vs 4*5
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 705, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded det_pencil points has rank a mod 2147483629 — rank 1
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/11_4_2_2_1_d5_det_pencil_p2147483647.json.gz`

*mult_det_pencil((11, 4, 2, 2, 1), 5) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (1.1s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (11, 4, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 20 vs 4*5
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 705, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded det_pencil points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/11_4_2_2_1_d5_reducible_p2147483629.json.gz`

*mult_reducible((11, 4, 2, 2, 1), 5) = a = 1, mod 2147483629, length-5 balanced complement (session 60)*  (1.0s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (11, 4, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 20 vs 4*5
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 705, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded reducible points has rank a mod 2147483629 — rank 1
- [x] conclusion: mult_reducible(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/11_4_2_2_1_d5_reducible_p2147483647.json.gz`

*mult_reducible((11, 4, 2, 2, 1), 5) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (1.0s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (11, 4, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 20 vs 4*5
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 705, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded reducible points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_reducible(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/11_4_4_4_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((11, 4, 4, 4, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (1.1s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (11, 4, 4, 4, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/11_4_4_4_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((11, 4, 4, 4, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (1.1s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (11, 4, 4, 4, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/11_5_5_2_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((11, 5, 5, 2, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (11, 5, 5, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/11_5_5_2_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((11, 5, 5, 2, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (11, 5, 5, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/11_6_3_3_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((11, 6, 3, 3, 1), 6) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (11, 6, 3, 3, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis: 1 independent vectors = a — rank 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded det_pencil points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/11_6_3_3_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((11, 6, 3, 3, 1), 6) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (11, 6, 3, 3, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis: 1 independent vectors = a — rank 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded reducible points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_reducible(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/11_6_5_1_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((11, 6, 5, 1, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (11, 6, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/11_6_5_1_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((11, 6, 5, 1, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (11, 6, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/11_7_2_2_2_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((11, 7, 2, 2, 2), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (11, 7, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/11_7_2_2_2_d6_reducible_p2147483647.json.gz`

*mult_reducible((11, 7, 2, 2, 2), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (11, 7, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/11_7_4_1_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((11, 7, 4, 1, 1), 6) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (11, 7, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/11_7_4_1_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((11, 7, 4, 1, 1), 6) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (11, 7, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/11_8_2_2_1_d6_det_pencil_p2147483629.json.gz`

*mult_det_pencil((11, 8, 2, 2, 1), 6) = a = 3, mod 2147483629, length-5 balanced complement (session 60)*  (32.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (11, 8, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2919, nullity 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483629 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/11_8_2_2_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((11, 8, 2, 2, 1), 6) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (31.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (11, 8, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2919, nullity 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/11_8_2_2_1_d6_reducible_p2147483629.json.gz`

*mult_reducible((11, 8, 2, 2, 1), 6) = a = 3, mod 2147483629, length-5 balanced complement (session 60)*  (32.1s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (11, 8, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2919, nullity 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483629 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/11_8_2_2_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((11, 8, 2, 2, 1), 6) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (32.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (11, 8, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2919, nullity 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_10_2_2_2_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((12, 10, 2, 2, 2), 7) = a = 7, mod 2147483647, length-5 balanced complement (session 60)*  (5.9s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 10, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 7, claimed 7
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis: 7 independent vectors = a — rank 7, a = 7
- [x] evaluation of the a = 7 highest-weight vectors at 15 recorded det_pencil points has rank a mod 2147483647 — rank 7
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 7 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_10_2_2_2_d7_reducible_p2147483647.json.gz`

*mult_reducible((12, 10, 2, 2, 2), 7) = a = 7, mod 2147483647, length-5 balanced complement (session 60)*  (5.9s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 10, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 7, claimed 7
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis: 7 independent vectors = a — rank 7, a = 7
- [x] evaluation of the a = 7 highest-weight vectors at 15 recorded reducible points has rank a mod 2147483647 — rank 7
- [x] conclusion: mult_reducible(lambda, delta) = a = 7 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_10_4_1_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((12, 10, 4, 1, 1), 7) = a = 5, mod 2147483647, length-5 balanced complement (session 60)*  (2.0s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 10, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis: 5 independent vectors = a — rank 5, a = 5
- [x] evaluation of the a = 5 highest-weight vectors at 13 recorded det_pencil points has rank a mod 2147483647 — rank 5
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 5 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_10_4_1_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((12, 10, 4, 1, 1), 7) = a = 5, mod 2147483647, length-5 balanced complement (session 60)*  (1.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 10, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis: 5 independent vectors = a — rank 5, a = 5
- [x] evaluation of the a = 5 highest-weight vectors at 13 recorded reducible points has rank a mod 2147483647 — rank 5
- [x] conclusion: mult_reducible(lambda, delta) = a = 5 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_11_2_2_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((12, 11, 2, 2, 1), 7) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.9s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 11, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_11_2_2_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((12, 11, 2, 2, 1), 7) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.9s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 11, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_11_3_1_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((12, 11, 3, 1, 1), 7) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 11, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_11_3_1_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((12, 11, 3, 1, 1), 7) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 11, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_2_2_2_2_d5_det_pencil_p2147483629.json.gz`

*mult_det_pencil((12, 2, 2, 2, 2), 5) = a = 1, mod 2147483629, length-5 balanced complement (session 60)*  (0.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 2, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 20 vs 4*5
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 553, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded det_pencil points has rank a mod 2147483629 — rank 1
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_2_2_2_2_d5_det_pencil_p2147483647.json.gz`

*mult_det_pencil((12, 2, 2, 2, 2), 5) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (0.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 2, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 20 vs 4*5
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 553, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded det_pencil points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_2_2_2_2_d5_reducible_p2147483629.json.gz`

*mult_reducible((12, 2, 2, 2, 2), 5) = a = 1, mod 2147483629, length-5 balanced complement (session 60)*  (0.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 2, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 20 vs 4*5
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 553, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded reducible points has rank a mod 2147483629 — rank 1
- [x] conclusion: mult_reducible(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_2_2_2_2_d5_reducible_p2147483647.json.gz`

*mult_reducible((12, 2, 2, 2, 2), 5) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (0.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 2, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 20 vs 4*5
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 553, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded reducible points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_reducible(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_4_4_2_2_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((12, 4, 4, 2, 2), 6) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (1.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 4, 4, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_4_4_2_2_d6_reducible_p2147483647.json.gz`

*mult_reducible((12, 4, 4, 2, 2), 6) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (1.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 4, 4, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_4_4_3_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((12, 4, 4, 3, 1), 6) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 4, 4, 3, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis: 1 independent vectors = a — rank 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded det_pencil points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_4_4_3_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((12, 4, 4, 3, 1), 6) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 4, 4, 3, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis: 1 independent vectors = a — rank 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded reducible points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_reducible(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_5_3_3_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((12, 5, 3, 3, 1), 6) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 5, 3, 3, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis: 1 independent vectors = a — rank 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded det_pencil points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_5_3_3_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((12, 5, 3, 3, 1), 6) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 5, 3, 3, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis: 1 independent vectors = a — rank 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded reducible points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_reducible(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_5_5_1_1_d6_det_pencil_p2147483629.json.gz`

*mult_det_pencil((12, 5, 5, 1, 1), 6) = a = 2, mod 2147483629, length-5 balanced complement (session 60)*  (28.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 5, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2795, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483629 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_5_5_1_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((12, 5, 5, 1, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (28.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 5, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2795, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_5_5_1_1_d6_reducible_p2147483629.json.gz`

*mult_reducible((12, 5, 5, 1, 1), 6) = a = 2, mod 2147483629, length-5 balanced complement (session 60)*  (28.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 5, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2795, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483629 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_5_5_1_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((12, 5, 5, 1, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (28.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 5, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2795, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_6_2_2_2_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((12, 6, 2, 2, 2), 6) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 6, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_6_2_2_2_d6_reducible_p2147483647.json.gz`

*mult_reducible((12, 6, 2, 2, 2), 6) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 6, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_6_3_2_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((12, 6, 3, 2, 1), 6) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 6, 3, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_6_3_2_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((12, 6, 3, 2, 1), 6) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 6, 3, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_6_4_1_1_d6_det_pencil_p2147483629.json.gz`

*mult_det_pencil((12, 6, 4, 1, 1), 6) = a = 2, mod 2147483629, length-5 balanced complement (session 60)*  (21.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 6, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2553, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483629 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_6_4_1_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((12, 6, 4, 1, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (21.9s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 6, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2553, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_6_4_1_1_d6_reducible_p2147483629.json.gz`

*mult_reducible((12, 6, 4, 1, 1), 6) = a = 2, mod 2147483629, length-5 balanced complement (session 60)*  (21.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 6, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2553, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483629 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_6_4_1_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((12, 6, 4, 1, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (21.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 6, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2553, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_7_7_1_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((12, 7, 7, 1, 1), 7) = a = 7, mod 2147483647, length-5 balanced complement (session 60)*  (5.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 7, 7, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 7, claimed 7
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis: 7 independent vectors = a — rank 7, a = 7
- [x] evaluation of the a = 7 highest-weight vectors at 15 recorded det_pencil points has rank a mod 2147483647 — rank 7
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 7 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_7_7_1_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((12, 7, 7, 1, 1), 7) = a = 7, mod 2147483647, length-5 balanced complement (session 60)*  (5.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 7, 7, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 7, claimed 7
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis: 7 independent vectors = a — rank 7, a = 7
- [x] evaluation of the a = 7 highest-weight vectors at 15 recorded reducible points has rank a mod 2147483647 — rank 7
- [x] conclusion: mult_reducible(lambda, delta) = a = 7 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_8_2_1_1_d6_det_pencil_p2147483629.json.gz`

*mult_det_pencil((12, 8, 2, 1, 1), 6) = a = 1, mod 2147483629, length-5 balanced complement (session 60)*  (2.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 8, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 1121, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded det_pencil points has rank a mod 2147483629 — rank 1
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_8_2_1_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((12, 8, 2, 1, 1), 6) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (2.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 8, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 1121, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded det_pencil points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_8_2_1_1_d6_reducible_p2147483629.json.gz`

*mult_reducible((12, 8, 2, 1, 1), 6) = a = 1, mod 2147483629, length-5 balanced complement (session 60)*  (2.9s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 8, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 1121, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded reducible points has rank a mod 2147483629 — rank 1
- [x] conclusion: mult_reducible(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/12_8_2_1_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((12, 8, 2, 1, 1), 6) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (2.9s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (12, 8, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 1121, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded reducible points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_reducible(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_10_2_2_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((13, 10, 2, 2, 1), 7) = a = 6, mod 2147483647, length-5 balanced complement (session 60)*  (2.0s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 10, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis: 6 independent vectors = a — rank 6, a = 6
- [x] evaluation of the a = 6 highest-weight vectors at 14 recorded det_pencil points has rank a mod 2147483647 — rank 6
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_10_2_2_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((13, 10, 2, 2, 1), 7) = a = 6, mod 2147483647, length-5 balanced complement (session 60)*  (1.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 10, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis: 6 independent vectors = a — rank 6, a = 6
- [x] evaluation of the a = 6 highest-weight vectors at 14 recorded reducible points has rank a mod 2147483647 — rank 6
- [x] conclusion: mult_reducible(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_10_3_1_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((13, 10, 3, 1, 1), 7) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 10, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_10_3_1_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((13, 10, 3, 1, 1), 7) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 10, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_13_2_2_2_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((13, 13, 2, 2, 2), 8) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (1.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 13, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis: 1 independent vectors = a — rank 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded det_pencil points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_13_2_2_2_d8_reducible_p2147483647.json.gz`

*mult_reducible((13, 13, 2, 2, 2), 8) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (1.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 13, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis: 1 independent vectors = a — rank 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded reducible points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_reducible(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_13_4_1_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((13, 13, 4, 1, 1), 8) = a = 6, mod 2147483647, length-5 balanced complement (session 60)*  (4.9s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 13, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis: 6 independent vectors = a — rank 6, a = 6
- [x] evaluation of the a = 6 highest-weight vectors at 14 recorded det_pencil points has rank a mod 2147483647 — rank 6
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_13_4_1_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((13, 13, 4, 1, 1), 8) = a = 6, mod 2147483647, length-5 balanced complement (session 60)*  (4.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 13, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis: 6 independent vectors = a — rank 6, a = 6
- [x] evaluation of the a = 6 highest-weight vectors at 14 recorded reducible points has rank a mod 2147483647 — rank 6
- [x] conclusion: mult_reducible(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_4_3_2_2_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((13, 4, 3, 2, 2), 6) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 4, 3, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis: 1 independent vectors = a — rank 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded det_pencil points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_4_3_2_2_d6_reducible_p2147483647.json.gz`

*mult_reducible((13, 4, 3, 2, 2), 6) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (0.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 4, 3, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis: 1 independent vectors = a — rank 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded reducible points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_reducible(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_4_4_2_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((13, 4, 4, 2, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 4, 4, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_4_4_2_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((13, 4, 4, 2, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 4, 4, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_5_2_2_2_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((13, 5, 2, 2, 2), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 5, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_5_2_2_2_d6_reducible_p2147483647.json.gz`

*mult_reducible((13, 5, 2, 2, 2), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 5, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_5_3_2_1_d6_det_pencil_p2147483629.json.gz`

*mult_det_pencil((13, 5, 3, 2, 1), 6) = a = 3, mod 2147483629, length-5 balanced complement (session 60)*  (27.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 5, 3, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2800, nullity 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483629 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_5_3_2_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((13, 5, 3, 2, 1), 6) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (27.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 5, 3, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2800, nullity 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_5_3_2_1_d6_reducible_p2147483629.json.gz`

*mult_reducible((13, 5, 3, 2, 1), 6) = a = 3, mod 2147483629, length-5 balanced complement (session 60)*  (27.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 5, 3, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2800, nullity 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483629 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_5_3_2_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((13, 5, 3, 2, 1), 6) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (27.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 5, 3, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2800, nullity 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_5_4_1_1_d6_det_pencil_p2147483629.json.gz`

*mult_det_pencil((13, 5, 4, 1, 1), 6) = a = 2, mod 2147483629, length-5 balanced complement (session 60)*  (8.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 5, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 1824, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483629 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_5_4_1_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((13, 5, 4, 1, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (9.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 5, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 1824, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_5_4_1_1_d6_reducible_p2147483629.json.gz`

*mult_reducible((13, 5, 4, 1, 1), 6) = a = 2, mod 2147483629, length-5 balanced complement (session 60)*  (8.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 5, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 1824, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483629 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_5_4_1_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((13, 5, 4, 1, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (8.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 5, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 1824, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_6_3_1_1_d6_det_pencil_p2147483629.json.gz`

*mult_det_pencil((13, 6, 3, 1, 1), 6) = a = 1, mod 2147483629, length-5 balanced complement (session 60)*  (5.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 6, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 1463, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded det_pencil points has rank a mod 2147483629 — rank 1
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_6_3_1_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((13, 6, 3, 1, 1), 6) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (5.1s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 6, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 1463, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded det_pencil points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_6_3_1_1_d6_reducible_p2147483629.json.gz`

*mult_reducible((13, 6, 3, 1, 1), 6) = a = 1, mod 2147483629, length-5 balanced complement (session 60)*  (5.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 6, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 1463, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded reducible points has rank a mod 2147483629 — rank 1
- [x] conclusion: mult_reducible(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_6_3_1_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((13, 6, 3, 1, 1), 6) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (5.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 6, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 1463, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded reducible points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_reducible(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_8_5_1_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((13, 8, 5, 1, 1), 7) = a = 10, mod 2147483647, length-5 balanced complement (session 60)*  (4.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 8, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 10, claimed 10
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis: 10 independent vectors = a — rank 10, a = 10
- [x] evaluation of the a = 10 highest-weight vectors at 18 recorded det_pencil points has rank a mod 2147483647 — rank 10
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 10 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_8_5_1_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((13, 8, 5, 1, 1), 7) = a = 10, mod 2147483647, length-5 balanced complement (session 60)*  (4.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 8, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 10, claimed 10
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis: 10 independent vectors = a — rank 10, a = 10
- [x] evaluation of the a = 10 highest-weight vectors at 18 recorded reducible points has rank a mod 2147483647 — rank 10
- [x] conclusion: mult_reducible(lambda, delta) = a = 10 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_9_2_2_2_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((13, 9, 2, 2, 2), 7) = a = 6, mod 2147483647, length-5 balanced complement (session 60)*  (4.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 9, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis: 6 independent vectors = a — rank 6, a = 6
- [x] evaluation of the a = 6 highest-weight vectors at 14 recorded det_pencil points has rank a mod 2147483647 — rank 6
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_9_2_2_2_d7_reducible_p2147483647.json.gz`

*mult_reducible((13, 9, 2, 2, 2), 7) = a = 6, mod 2147483647, length-5 balanced complement (session 60)*  (4.1s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 9, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis: 6 independent vectors = a — rank 6, a = 6
- [x] evaluation of the a = 6 highest-weight vectors at 14 recorded reducible points has rank a mod 2147483647 — rank 6
- [x] conclusion: mult_reducible(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_9_4_1_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((13, 9, 4, 1, 1), 7) = a = 10, mod 2147483647, length-5 balanced complement (session 60)*  (3.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 9, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 10, claimed 10
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis: 10 independent vectors = a — rank 10, a = 10
- [x] evaluation of the a = 10 highest-weight vectors at 18 recorded det_pencil points has rank a mod 2147483647 — rank 10
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 10 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/13_9_4_1_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((13, 9, 4, 1, 1), 7) = a = 10, mod 2147483647, length-5 balanced complement (session 60)*  (3.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (13, 9, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 10, claimed 10
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis: 10 independent vectors = a — rank 10, a = 10
- [x] evaluation of the a = 10 highest-weight vectors at 18 recorded reducible points has rank a mod 2147483647 — rank 10
- [x] conclusion: mult_reducible(lambda, delta) = a = 10 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/14_13_3_1_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((14, 13, 3, 1, 1), 8) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (1.1s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (14, 13, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/14_13_3_1_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((14, 13, 3, 1, 1), 8) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.9s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (14, 13, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/14_4_3_2_1_d6_det_pencil_p2147483629.json.gz`

*mult_det_pencil((14, 4, 3, 2, 1), 6) = a = 1, mod 2147483629, length-5 balanced complement (session 60)*  (8.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (14, 4, 3, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 1785, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded det_pencil points has rank a mod 2147483629 — rank 1
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/14_4_3_2_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((14, 4, 3, 2, 1), 6) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (8.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (14, 4, 3, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 1785, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded det_pencil points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/14_4_3_2_1_d6_reducible_p2147483629.json.gz`

*mult_reducible((14, 4, 3, 2, 1), 6) = a = 1, mod 2147483629, length-5 balanced complement (session 60)*  (8.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (14, 4, 3, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 1785, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded reducible points has rank a mod 2147483629 — rank 1
- [x] conclusion: mult_reducible(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/14_4_3_2_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((14, 4, 3, 2, 1), 6) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (8.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (14, 4, 3, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 1785, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded reducible points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_reducible(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/14_5_2_2_1_d6_det_pencil_p2147483629.json.gz`

*mult_det_pencil((14, 5, 2, 2, 1), 6) = a = 2, mod 2147483629, length-5 balanced complement (session 60)*  (4.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (14, 5, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 1337, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483629 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/14_5_2_2_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((14, 5, 2, 2, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (4.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (14, 5, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 1337, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/14_5_2_2_1_d6_reducible_p2147483629.json.gz`

*mult_reducible((14, 5, 2, 2, 1), 6) = a = 2, mod 2147483629, length-5 balanced complement (session 60)*  (4.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (14, 5, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 1337, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483629 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/14_5_2_2_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((14, 5, 2, 2, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (4.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (14, 5, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 1337, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/14_6_6_1_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((14, 6, 6, 1, 1), 7) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (14, 6, 6, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis: 1 independent vectors = a — rank 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded det_pencil points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/14_6_6_1_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((14, 6, 6, 1, 1), 7) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (14, 6, 6, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis: 1 independent vectors = a — rank 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded reducible points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_reducible(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/14_7_5_1_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((14, 7, 5, 1, 1), 7) = a = 10, mod 2147483647, length-5 balanced complement (session 60)*  (3.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (14, 7, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 10, claimed 10
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis: 10 independent vectors = a — rank 10, a = 10
- [x] evaluation of the a = 10 highest-weight vectors at 18 recorded det_pencil points has rank a mod 2147483647 — rank 10
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 10 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/14_7_5_1_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((14, 7, 5, 1, 1), 7) = a = 10, mod 2147483647, length-5 balanced complement (session 60)*  (3.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (14, 7, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 10, claimed 10
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis: 10 independent vectors = a — rank 10, a = 10
- [x] evaluation of the a = 10 highest-weight vectors at 18 recorded reducible points has rank a mod 2147483647 — rank 10
- [x] conclusion: mult_reducible(lambda, delta) = a = 10 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/14_8_2_2_2_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((14, 8, 2, 2, 2), 7) = a = 9, mod 2147483647, length-5 balanced complement (session 60)*  (4.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (14, 8, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 9, claimed 9
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis: 9 independent vectors = a — rank 9, a = 9
- [x] evaluation of the a = 9 highest-weight vectors at 17 recorded det_pencil points has rank a mod 2147483647 — rank 9
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 9 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/14_8_2_2_2_d7_reducible_p2147483647.json.gz`

*mult_reducible((14, 8, 2, 2, 2), 7) = a = 9, mod 2147483647, length-5 balanced complement (session 60)*  (4.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (14, 8, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 9, claimed 9
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis: 9 independent vectors = a — rank 9, a = 9
- [x] evaluation of the a = 9 highest-weight vectors at 17 recorded reducible points has rank a mod 2147483647 — rank 9
- [x] conclusion: mult_reducible(lambda, delta) = a = 9 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/14_8_4_1_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((14, 8, 4, 1, 1), 7) = a = 7, mod 2147483647, length-5 balanced complement (session 60)*  (1.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (14, 8, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 7, claimed 7
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis: 7 independent vectors = a — rank 7, a = 7
- [x] evaluation of the a = 7 highest-weight vectors at 15 recorded det_pencil points has rank a mod 2147483647 — rank 7
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 7 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/14_8_4_1_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((14, 8, 4, 1, 1), 7) = a = 7, mod 2147483647, length-5 balanced complement (session 60)*  (1.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (14, 8, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 7, claimed 7
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis: 7 independent vectors = a — rank 7, a = 7
- [x] evaluation of the a = 7 highest-weight vectors at 15 recorded reducible points has rank a mod 2147483647 — rank 7
- [x] conclusion: mult_reducible(lambda, delta) = a = 7 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/14_9_2_2_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((14, 9, 2, 2, 1), 7) = a = 7, mod 2147483647, length-5 balanced complement (session 60)*  (1.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (14, 9, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 7, claimed 7
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis: 7 independent vectors = a — rank 7, a = 7
- [x] evaluation of the a = 7 highest-weight vectors at 15 recorded det_pencil points has rank a mod 2147483647 — rank 7
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 7 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/14_9_2_2_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((14, 9, 2, 2, 1), 7) = a = 7, mod 2147483647, length-5 balanced complement (session 60)*  (1.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (14, 9, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 7, claimed 7
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis: 7 independent vectors = a — rank 7, a = 7
- [x] evaluation of the a = 7 highest-weight vectors at 15 recorded reducible points has rank a mod 2147483647 — rank 7
- [x] conclusion: mult_reducible(lambda, delta) = a = 7 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/14_9_3_1_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((14, 9, 3, 1, 1), 7) = a = 5, mod 2147483647, length-5 balanced complement (session 60)*  (0.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (14, 9, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis: 5 independent vectors = a — rank 5, a = 5
- [x] evaluation of the a = 5 highest-weight vectors at 13 recorded det_pencil points has rank a mod 2147483647 — rank 5
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 5 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/14_9_3_1_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((14, 9, 3, 1, 1), 7) = a = 5, mod 2147483647, length-5 balanced complement (session 60)*  (0.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (14, 9, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis: 5 independent vectors = a — rank 5, a = 5
- [x] evaluation of the a = 5 highest-weight vectors at 13 recorded reducible points has rank a mod 2147483647 — rank 5
- [x] conclusion: mult_reducible(lambda, delta) = a = 5 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_12_3_1_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((15, 12, 3, 1, 1), 8) = a = 6, mod 2147483647, length-5 balanced complement (session 60)*  (2.0s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 12, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis: 6 independent vectors = a — rank 6, a = 6
- [x] evaluation of the a = 6 highest-weight vectors at 14 recorded det_pencil points has rank a mod 2147483647 — rank 6
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_12_3_1_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((15, 12, 3, 1, 1), 8) = a = 6, mod 2147483647, length-5 balanced complement (session 60)*  (1.9s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 12, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis: 6 independent vectors = a — rank 6, a = 6
- [x] evaluation of the a = 6 highest-weight vectors at 14 recorded reducible points has rank a mod 2147483647 — rank 6
- [x] conclusion: mult_reducible(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_13_2_1_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((15, 13, 2, 1, 1), 8) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 13, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_13_2_1_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((15, 13, 2, 1, 1), 8) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 13, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_15_4_1_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((15, 15, 4, 1, 1), 9) = a = 9, mod 2147483647, length-5 balanced complement (session 60)*  (17.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 15, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 9, claimed 9
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis: 9 independent vectors = a — rank 9, a = 9
- [x] evaluation of the a = 9 highest-weight vectors at 17 recorded det_pencil points has rank a mod 2147483647 — rank 9
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 9 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_15_4_1_1_d9_red_ideal_p2147483647.json.gz`

*1 highest-weight vector(s) of weight (15, 15, 4, 1, 1), degree 9, in I(R_5) by (star) mod 2147483647 (session 60: mult_red = 8 < a = 9, h_pad = 12)*  (1.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 15, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 9, claimed 9
- [x] vectors parsed — 1 vector(s), supports [6032], modulus 2147483647
- [x] vector 0: shape, degree, canonical terms, weight = lambda
- [x] vector 0: annihilated by every E_(i,i+1) mod 2147483647
- [x] vectors linearly independent — rank 1 mod 2147483647
- [x] vector 0: (star) support for k = 1 (Theorem (star): lies in I({l^1 c}))
- [x] vanishes at 17 recorded point(s) [reducible]
- [x] evaluation at 17 recorded point(s) [det_pencil] has full row rank — rank 1 of 1
- [x] vanishes at 6 fresh reducible points (seed 20260905)
- [x] vanishes at 6 fresh padded_permanent points (seed 20260905)
- [x] evaluation at 6 fresh det_pencil points (seed 20260905) has full row rank — rank 1 of 1
- [x] evaluation at 6 fresh generic points (seed 20260905) has full row rank — rank 1 of 1

## PASS — `results/certs/s60/15_3_2_2_2_d6_det_pencil_p2147483629.json.gz`

*mult_det_pencil((15, 3, 2, 2, 2), 6) = a = 1, mod 2147483629, length-5 balanced complement (session 60)*  (4.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 3, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 1280, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded det_pencil points has rank a mod 2147483629 — rank 1
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_3_2_2_2_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((15, 3, 2, 2, 2), 6) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (4.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 3, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 1280, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded det_pencil points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_3_2_2_2_d6_reducible_p2147483629.json.gz`

*mult_reducible((15, 3, 2, 2, 2), 6) = a = 1, mod 2147483629, length-5 balanced complement (session 60)*  (4.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 3, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 1280, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded reducible points has rank a mod 2147483629 — rank 1
- [x] conclusion: mult_reducible(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_3_2_2_2_d6_reducible_p2147483647.json.gz`

*mult_reducible((15, 3, 2, 2, 2), 6) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (4.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 3, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 1280, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded reducible points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_reducible(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_4_4_4_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((15, 4, 4, 4, 1), 7) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (3.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 4, 4, 4, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_4_4_4_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((15, 4, 4, 4, 1), 7) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (3.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 4, 4, 4, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_6_5_1_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((15, 6, 5, 1, 1), 7) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.9s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 6, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_6_5_1_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((15, 6, 5, 1, 1), 7) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 6, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_7_2_2_2_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((15, 7, 2, 2, 2), 7) = a = 6, mod 2147483647, length-5 balanced complement (session 60)*  (2.1s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 7, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis: 6 independent vectors = a — rank 6, a = 6
- [x] evaluation of the a = 6 highest-weight vectors at 14 recorded det_pencil points has rank a mod 2147483647 — rank 6
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_7_2_2_2_d7_reducible_p2147483647.json.gz`

*mult_reducible((15, 7, 2, 2, 2), 7) = a = 6, mod 2147483647, length-5 balanced complement (session 60)*  (2.0s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 7, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis: 6 independent vectors = a — rank 6, a = 6
- [x] evaluation of the a = 6 highest-weight vectors at 14 recorded reducible points has rank a mod 2147483647 — rank 6
- [x] conclusion: mult_reducible(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_7_4_1_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((15, 7, 4, 1, 1), 7) = a = 8, mod 2147483647, length-5 balanced complement (session 60)*  (1.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 7, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 8, claimed 8
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis: 8 independent vectors = a — rank 8, a = 8
- [x] evaluation of the a = 8 highest-weight vectors at 16 recorded det_pencil points has rank a mod 2147483647 — rank 8
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 8 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_7_4_1_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((15, 7, 4, 1, 1), 7) = a = 8, mod 2147483647, length-5 balanced complement (session 60)*  (1.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 7, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 8, claimed 8
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis: 8 independent vectors = a — rank 8, a = 8
- [x] evaluation of the a = 8 highest-weight vectors at 16 recorded reducible points has rank a mod 2147483647 — rank 8
- [x] conclusion: mult_reducible(lambda, delta) = a = 8 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_8_2_2_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((15, 8, 2, 2, 1), 7) = a = 7, mod 2147483647, length-5 balanced complement (session 60)*  (1.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 8, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 7, claimed 7
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis: 7 independent vectors = a — rank 7, a = 7
- [x] evaluation of the a = 7 highest-weight vectors at 15 recorded det_pencil points has rank a mod 2147483647 — rank 7
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 7 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_8_2_2_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((15, 8, 2, 2, 1), 7) = a = 7, mod 2147483647, length-5 balanced complement (session 60)*  (1.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 8, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 7, claimed 7
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis: 7 independent vectors = a — rank 7, a = 7
- [x] evaluation of the a = 7 highest-weight vectors at 15 recorded reducible points has rank a mod 2147483647 — rank 7
- [x] conclusion: mult_reducible(lambda, delta) = a = 7 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_8_3_1_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((15, 8, 3, 1, 1), 7) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 8, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_8_3_1_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((15, 8, 3, 1, 1), 7) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 8, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_9_2_1_1_d7_det_pencil_p2147483629.json.gz`

*mult_det_pencil((15, 9, 2, 1, 1), 7) = a = 2, mod 2147483629, length-5 balanced complement (session 60)*  (8.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 9, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 1761, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483629 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_9_2_1_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((15, 9, 2, 1, 1), 7) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (8.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 9, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 1761, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_9_2_1_1_d7_reducible_p2147483629.json.gz`

*mult_reducible((15, 9, 2, 1, 1), 7) = a = 2, mod 2147483629, length-5 balanced complement (session 60)*  (8.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 9, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 1761, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483629 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/15_9_2_1_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((15, 9, 2, 1, 1), 7) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (8.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (15, 9, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 1761, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/16_11_3_1_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((16, 11, 3, 1, 1), 8) = a = 9, mod 2147483647, length-5 balanced complement (session 60)*  (2.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (16, 11, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 9, claimed 9
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis: 9 independent vectors = a — rank 9, a = 9
- [x] evaluation of the a = 9 highest-weight vectors at 17 recorded det_pencil points has rank a mod 2147483647 — rank 9
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 9 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/16_11_3_1_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((16, 11, 3, 1, 1), 8) = a = 9, mod 2147483647, length-5 balanced complement (session 60)*  (2.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (16, 11, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 9, claimed 9
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis: 9 independent vectors = a — rank 9, a = 9
- [x] evaluation of the a = 9 highest-weight vectors at 17 recorded reducible points has rank a mod 2147483647 — rank 9
- [x] conclusion: mult_reducible(lambda, delta) = a = 9 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/16_12_2_1_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((16, 12, 2, 1, 1), 8) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (16, 12, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/16_12_2_1_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((16, 12, 2, 1, 1), 8) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (16, 12, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/16_4_4_2_2_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((16, 4, 4, 2, 2), 7) = a = 5, mod 2147483647, length-5 balanced complement (session 60)*  (2.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (16, 4, 4, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis: 5 independent vectors = a — rank 5, a = 5
- [x] evaluation of the a = 5 highest-weight vectors at 13 recorded det_pencil points has rank a mod 2147483647 — rank 5
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 5 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/16_4_4_2_2_d7_reducible_p2147483647.json.gz`

*mult_reducible((16, 4, 4, 2, 2), 7) = a = 5, mod 2147483647, length-5 balanced complement (session 60)*  (2.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (16, 4, 4, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis: 5 independent vectors = a — rank 5, a = 5
- [x] evaluation of the a = 5 highest-weight vectors at 13 recorded reducible points has rank a mod 2147483647 — rank 5
- [x] conclusion: mult_reducible(lambda, delta) = a = 5 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/16_5_3_3_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((16, 5, 3, 3, 1), 7) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (16, 5, 3, 3, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/16_5_3_3_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((16, 5, 3, 3, 1), 7) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (16, 5, 3, 3, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/16_5_5_1_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((16, 5, 5, 1, 1), 7) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (16, 5, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/16_5_5_1_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((16, 5, 5, 1, 1), 7) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (16, 5, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/16_6_2_2_2_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((16, 6, 2, 2, 2), 7) = a = 7, mod 2147483647, length-5 balanced complement (session 60)*  (1.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (16, 6, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 7, claimed 7
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis: 7 independent vectors = a — rank 7, a = 7
- [x] evaluation of the a = 7 highest-weight vectors at 15 recorded det_pencil points has rank a mod 2147483647 — rank 7
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 7 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/16_6_2_2_2_d7_reducible_p2147483647.json.gz`

*mult_reducible((16, 6, 2, 2, 2), 7) = a = 7, mod 2147483647, length-5 balanced complement (session 60)*  (1.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (16, 6, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 7, claimed 7
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis: 7 independent vectors = a — rank 7, a = 7
- [x] evaluation of the a = 7 highest-weight vectors at 15 recorded reducible points has rank a mod 2147483647 — rank 7
- [x] conclusion: mult_reducible(lambda, delta) = a = 7 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/16_6_4_1_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((16, 6, 4, 1, 1), 7) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (16, 6, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/16_6_4_1_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((16, 6, 4, 1, 1), 7) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (16, 6, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/16_7_2_2_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((16, 7, 2, 2, 1), 7) = a = 5, mod 2147483647, length-5 balanced complement (session 60)*  (0.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (16, 7, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis: 5 independent vectors = a — rank 5, a = 5
- [x] evaluation of the a = 5 highest-weight vectors at 13 recorded det_pencil points has rank a mod 2147483647 — rank 5
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 5 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/16_7_2_2_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((16, 7, 2, 2, 1), 7) = a = 5, mod 2147483647, length-5 balanced complement (session 60)*  (0.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (16, 7, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis: 5 independent vectors = a — rank 5, a = 5
- [x] evaluation of the a = 5 highest-weight vectors at 13 recorded reducible points has rank a mod 2147483647 — rank 5
- [x] conclusion: mult_reducible(lambda, delta) = a = 5 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/16_7_3_1_1_d7_det_pencil_p2147483629.json.gz`

*mult_det_pencil((16, 7, 3, 1, 1), 7) = a = 4, mod 2147483629, length-5 balanced complement (session 60)*  (19.1s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (16, 7, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2414, nullity 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483629 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/16_7_3_1_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((16, 7, 3, 1, 1), 7) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (19.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (16, 7, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2414, nullity 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/16_7_3_1_1_d7_reducible_p2147483629.json.gz`

*mult_reducible((16, 7, 3, 1, 1), 7) = a = 4, mod 2147483629, length-5 balanced complement (session 60)*  (19.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (16, 7, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2414, nullity 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483629 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/16_7_3_1_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((16, 7, 3, 1, 1), 7) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (19.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (16, 7, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2414, nullity 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/16_7_7_1_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((16, 7, 7, 1, 1), 8) = a = 13, mod 2147483647, length-5 balanced complement (session 60)*  (15.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (16, 7, 7, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 13, claimed 13
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis vector 12: highest weight mod 2147483647
- [x] basis: 13 independent vectors = a — rank 13, a = 13
- [x] evaluation of the a = 13 highest-weight vectors at 21 recorded det_pencil points has rank a mod 2147483647 — rank 13
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 13 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/16_7_7_1_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((16, 7, 7, 1, 1), 8) = a = 13, mod 2147483647, length-5 balanced complement (session 60)*  (9.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (16, 7, 7, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 13, claimed 13
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis vector 12: highest weight mod 2147483647
- [x] basis: 13 independent vectors = a — rank 13, a = 13
- [x] evaluation of the a = 13 highest-weight vectors at 21 recorded reducible points has rank a mod 2147483647 — rank 13
- [x] conclusion: mult_reducible(lambda, delta) = a = 13 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/17_10_3_1_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((17, 10, 3, 1, 1), 8) = a = 8, mod 2147483647, length-5 balanced complement (session 60)*  (0.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (17, 10, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 8, claimed 8
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis: 8 independent vectors = a — rank 8, a = 8
- [x] evaluation of the a = 8 highest-weight vectors at 16 recorded det_pencil points has rank a mod 2147483647 — rank 8
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 8 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/17_10_3_1_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((17, 10, 3, 1, 1), 8) = a = 8, mod 2147483647, length-5 balanced complement (session 60)*  (0.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (17, 10, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 8, claimed 8
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis: 8 independent vectors = a — rank 8, a = 8
- [x] evaluation of the a = 8 highest-weight vectors at 16 recorded reducible points has rank a mod 2147483647 — rank 8
- [x] conclusion: mult_reducible(lambda, delta) = a = 8 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/17_11_2_1_1_d8_det_pencil_p2147483629.json.gz`

*mult_det_pencil((17, 11, 2, 1, 1), 8) = a = 3, mod 2147483629, length-5 balanced complement (session 60)*  (16.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (17, 11, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2980, nullity 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483629 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/17_11_2_1_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((17, 11, 2, 1, 1), 8) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (17.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (17, 11, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2980, nullity 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/17_11_2_1_1_d8_reducible_p2147483629.json.gz`

*mult_reducible((17, 11, 2, 1, 1), 8) = a = 3, mod 2147483629, length-5 balanced complement (session 60)*  (16.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (17, 11, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2980, nullity 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483629 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/17_11_2_1_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((17, 11, 2, 1, 1), 8) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (16.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (17, 11, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2980, nullity 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/17_15_2_1_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((17, 15, 2, 1, 1), 9) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (17, 15, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/17_15_2_1_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((17, 15, 2, 1, 1), 9) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (17, 15, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/17_4_3_2_2_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((17, 4, 3, 2, 2), 7) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (17, 4, 3, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/17_4_3_2_2_d7_reducible_p2147483647.json.gz`

*mult_reducible((17, 4, 3, 2, 2), 7) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (17, 4, 3, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/17_4_4_2_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((17, 4, 4, 2, 1), 7) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (17, 4, 4, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/17_4_4_2_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((17, 4, 4, 2, 1), 7) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (17, 4, 4, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/17_5_2_2_2_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((17, 5, 2, 2, 2), 7) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (17, 5, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/17_5_2_2_2_d7_reducible_p2147483647.json.gz`

*mult_reducible((17, 5, 2, 2, 2), 7) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (17, 5, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/17_5_3_2_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((17, 5, 3, 2, 1), 7) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (17, 5, 3, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/17_5_3_2_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((17, 5, 3, 2, 1), 7) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (17, 5, 3, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/17_6_2_2_1_d7_det_pencil_p2147483629.json.gz`

*mult_det_pencil((17, 6, 2, 2, 1), 7) = a = 4, mod 2147483629, length-5 balanced complement (session 60)*  (16.1s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (17, 6, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2257, nullity 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483629 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/17_6_2_2_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((17, 6, 2, 2, 1), 7) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (16.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (17, 6, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2257, nullity 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/17_6_2_2_1_d7_reducible_p2147483629.json.gz`

*mult_reducible((17, 6, 2, 2, 1), 7) = a = 4, mod 2147483629, length-5 balanced complement (session 60)*  (16.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (17, 6, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2257, nullity 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483629 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/17_6_2_2_1_d7_reducible_p2147483647.json.gz`

*mult_reducible((17, 6, 2, 2, 1), 7) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (16.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (17, 6, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2257, nullity 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/17_9_4_1_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((17, 9, 4, 1, 1), 8) = a = 17, mod 2147483647, length-5 balanced complement (session 60)*  (8.1s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (17, 9, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 17, claimed 17
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis vector 12: highest weight mod 2147483647
- [x] basis vector 13: highest weight mod 2147483647
- [x] basis vector 14: highest weight mod 2147483647
- [x] basis vector 15: highest weight mod 2147483647
- [x] basis vector 16: highest weight mod 2147483647
- [x] basis: 17 independent vectors = a — rank 17, a = 17
- [x] evaluation of the a = 17 highest-weight vectors at 25 recorded det_pencil points has rank a mod 2147483647 — rank 17
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 17 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/17_9_4_1_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((17, 9, 4, 1, 1), 8) = a = 17, mod 2147483647, length-5 balanced complement (session 60)*  (7.9s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (17, 9, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 17, claimed 17
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis vector 12: highest weight mod 2147483647
- [x] basis vector 13: highest weight mod 2147483647
- [x] basis vector 14: highest weight mod 2147483647
- [x] basis vector 15: highest weight mod 2147483647
- [x] basis vector 16: highest weight mod 2147483647
- [x] basis: 17 independent vectors = a — rank 17, a = 17
- [x] evaluation of the a = 17 highest-weight vectors at 25 recorded reducible points has rank a mod 2147483647 — rank 17
- [x] conclusion: mult_reducible(lambda, delta) = a = 17 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/18_10_2_1_1_d8_det_pencil_p2147483629.json.gz`

*mult_det_pencil((18, 10, 2, 1, 1), 8) = a = 2, mod 2147483629, length-5 balanced complement (session 60)*  (23.0s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (18, 10, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2558, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483629 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/18_10_2_1_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((18, 10, 2, 1, 1), 8) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (23.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (18, 10, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2558, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/18_10_2_1_1_d8_reducible_p2147483629.json.gz`

*mult_reducible((18, 10, 2, 1, 1), 8) = a = 2, mod 2147483629, length-5 balanced complement (session 60)*  (23.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (18, 10, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2558, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483629 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/18_10_2_1_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((18, 10, 2, 1, 1), 8) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (23.1s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (18, 10, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2558, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/18_13_3_1_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((18, 13, 3, 1, 1), 9) = a = 12, mod 2147483647, length-5 balanced complement (session 60)*  (5.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (18, 13, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 12, claimed 12
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis: 12 independent vectors = a — rank 12, a = 12
- [x] evaluation of the a = 12 highest-weight vectors at 20 recorded det_pencil points has rank a mod 2147483647 — rank 12
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 12 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/18_13_3_1_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((18, 13, 3, 1, 1), 9) = a = 12, mod 2147483647, length-5 balanced complement (session 60)*  (5.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (18, 13, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 12, claimed 12
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis: 12 independent vectors = a — rank 12, a = 12
- [x] evaluation of the a = 12 highest-weight vectors at 20 recorded reducible points has rank a mod 2147483647 — rank 12
- [x] conclusion: mult_reducible(lambda, delta) = a = 12 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/18_14_2_1_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((18, 14, 2, 1, 1), 9) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (18, 14, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/18_14_2_1_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((18, 14, 2, 1, 1), 9) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (18, 14, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/18_4_2_2_2_d7_det_pencil_p2147483629.json.gz`

*mult_det_pencil((18, 4, 2, 2, 2), 7) = a = 3, mod 2147483629, length-5 balanced complement (session 60)*  (24.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (18, 4, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2565, nullity 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483629 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/18_4_2_2_2_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((18, 4, 2, 2, 2), 7) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (24.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (18, 4, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2565, nullity 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/18_4_2_2_2_d7_reducible_p2147483629.json.gz`

*mult_reducible((18, 4, 2, 2, 2), 7) = a = 3, mod 2147483629, length-5 balanced complement (session 60)*  (24.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (18, 4, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2565, nullity 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483629 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/18_4_2_2_2_d7_reducible_p2147483647.json.gz`

*mult_reducible((18, 4, 2, 2, 2), 7) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (24.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (18, 4, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2565, nullity 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/18_6_6_1_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((18, 6, 6, 1, 1), 8) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (18, 6, 6, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/18_6_6_1_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((18, 6, 6, 1, 1), 8) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (18, 6, 6, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/18_7_5_1_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((18, 7, 5, 1, 1), 8) = a = 14, mod 2147483647, length-5 balanced complement (session 60)*  (6.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (18, 7, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 14, claimed 14
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis vector 12: highest weight mod 2147483647
- [x] basis vector 13: highest weight mod 2147483647
- [x] basis: 14 independent vectors = a — rank 14, a = 14
- [x] evaluation of the a = 14 highest-weight vectors at 22 recorded det_pencil points has rank a mod 2147483647 — rank 14
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 14 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/18_7_5_1_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((18, 7, 5, 1, 1), 8) = a = 14, mod 2147483647, length-5 balanced complement (session 60)*  (6.1s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (18, 7, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 14, claimed 14
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis vector 12: highest weight mod 2147483647
- [x] basis vector 13: highest weight mod 2147483647
- [x] basis: 14 independent vectors = a — rank 14, a = 14
- [x] evaluation of the a = 14 highest-weight vectors at 22 recorded reducible points has rank a mod 2147483647 — rank 14
- [x] conclusion: mult_reducible(lambda, delta) = a = 14 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/18_8_2_2_2_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((18, 8, 2, 2, 2), 8) = a = 14, mod 2147483647, length-5 balanced complement (session 60)*  (10.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (18, 8, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 14, claimed 14
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis vector 12: highest weight mod 2147483647
- [x] basis vector 13: highest weight mod 2147483647
- [x] basis: 14 independent vectors = a — rank 14, a = 14
- [x] evaluation of the a = 14 highest-weight vectors at 22 recorded det_pencil points has rank a mod 2147483647 — rank 14
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 14 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/18_8_2_2_2_d8_reducible_p2147483647.json.gz`

*mult_reducible((18, 8, 2, 2, 2), 8) = a = 14, mod 2147483647, length-5 balanced complement (session 60)*  (9.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (18, 8, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 14, claimed 14
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis vector 12: highest weight mod 2147483647
- [x] basis vector 13: highest weight mod 2147483647
- [x] basis: 14 independent vectors = a — rank 14, a = 14
- [x] evaluation of the a = 14 highest-weight vectors at 22 recorded reducible points has rank a mod 2147483647 — rank 14
- [x] conclusion: mult_reducible(lambda, delta) = a = 14 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/18_8_4_1_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((18, 8, 4, 1, 1), 8) = a = 11, mod 2147483647, length-5 balanced complement (session 60)*  (3.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (18, 8, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 11, claimed 11
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis: 11 independent vectors = a — rank 11, a = 11
- [x] evaluation of the a = 11 highest-weight vectors at 19 recorded det_pencil points has rank a mod 2147483647 — rank 11
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 11 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/18_8_4_1_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((18, 8, 4, 1, 1), 8) = a = 11, mod 2147483647, length-5 balanced complement (session 60)*  (3.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (18, 8, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 11, claimed 11
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis: 11 independent vectors = a — rank 11, a = 11
- [x] evaluation of the a = 11 highest-weight vectors at 19 recorded reducible points has rank a mod 2147483647 — rank 11
- [x] conclusion: mult_reducible(lambda, delta) = a = 11 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/18_9_2_2_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((18, 9, 2, 2, 1), 8) = a = 11, mod 2147483647, length-5 balanced complement (session 60)*  (3.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (18, 9, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 11, claimed 11
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis: 11 independent vectors = a — rank 11, a = 11
- [x] evaluation of the a = 11 highest-weight vectors at 19 recorded det_pencil points has rank a mod 2147483647 — rank 11
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 11 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/18_9_2_2_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((18, 9, 2, 2, 1), 8) = a = 11, mod 2147483647, length-5 balanced complement (session 60)*  (3.1s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (18, 9, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 11, claimed 11
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis: 11 independent vectors = a — rank 11, a = 11
- [x] evaluation of the a = 11 highest-weight vectors at 19 recorded reducible points has rank a mod 2147483647 — rank 11
- [x] conclusion: mult_reducible(lambda, delta) = a = 11 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/18_9_3_1_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((18, 9, 3, 1, 1), 8) = a = 7, mod 2147483647, length-5 balanced complement (session 60)*  (1.0s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (18, 9, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 7, claimed 7
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis: 7 independent vectors = a — rank 7, a = 7
- [x] evaluation of the a = 7 highest-weight vectors at 15 recorded det_pencil points has rank a mod 2147483647 — rank 7
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 7 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/18_9_3_1_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((18, 9, 3, 1, 1), 8) = a = 7, mod 2147483647, length-5 balanced complement (session 60)*  (1.0s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (18, 9, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 7, claimed 7
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis: 7 independent vectors = a — rank 7, a = 7
- [x] evaluation of the a = 7 highest-weight vectors at 15 recorded reducible points has rank a mod 2147483647 — rank 7
- [x] conclusion: mult_reducible(lambda, delta) = a = 7 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/19_12_3_1_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((19, 12, 3, 1, 1), 9) = a = 12, mod 2147483647, length-5 balanced complement (session 60)*  (5.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (19, 12, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 12, claimed 12
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis: 12 independent vectors = a — rank 12, a = 12
- [x] evaluation of the a = 12 highest-weight vectors at 20 recorded det_pencil points has rank a mod 2147483647 — rank 12
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 12 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/19_12_3_1_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((19, 12, 3, 1, 1), 9) = a = 12, mod 2147483647, length-5 balanced complement (session 60)*  (5.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (19, 12, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 12, claimed 12
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis: 12 independent vectors = a — rank 12, a = 12
- [x] evaluation of the a = 12 highest-weight vectors at 20 recorded reducible points has rank a mod 2147483647 — rank 12
- [x] conclusion: mult_reducible(lambda, delta) = a = 12 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/19_13_2_1_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((19, 13, 2, 1, 1), 9) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (19, 13, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/19_13_2_1_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((19, 13, 2, 1, 1), 9) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (19, 13, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/19_4_4_4_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((19, 4, 4, 4, 1), 8) = a = 5, mod 2147483647, length-5 balanced complement (session 60)*  (5.9s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (19, 4, 4, 4, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis: 5 independent vectors = a — rank 5, a = 5
- [x] evaluation of the a = 5 highest-weight vectors at 13 recorded det_pencil points has rank a mod 2147483647 — rank 5
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 5 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/19_4_4_4_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((19, 4, 4, 4, 1), 8) = a = 5, mod 2147483647, length-5 balanced complement (session 60)*  (5.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (19, 4, 4, 4, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis: 5 independent vectors = a — rank 5, a = 5
- [x] evaluation of the a = 5 highest-weight vectors at 13 recorded reducible points has rank a mod 2147483647 — rank 5
- [x] conclusion: mult_reducible(lambda, delta) = a = 5 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/19_6_5_1_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((19, 6, 5, 1, 1), 8) = a = 5, mod 2147483647, length-5 balanced complement (session 60)*  (1.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (19, 6, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis: 5 independent vectors = a — rank 5, a = 5
- [x] evaluation of the a = 5 highest-weight vectors at 13 recorded det_pencil points has rank a mod 2147483647 — rank 5
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 5 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/19_6_5_1_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((19, 6, 5, 1, 1), 8) = a = 5, mod 2147483647, length-5 balanced complement (session 60)*  (1.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (19, 6, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis: 5 independent vectors = a — rank 5, a = 5
- [x] evaluation of the a = 5 highest-weight vectors at 13 recorded reducible points has rank a mod 2147483647 — rank 5
- [x] conclusion: mult_reducible(lambda, delta) = a = 5 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/19_7_2_2_2_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((19, 7, 2, 2, 2), 8) = a = 9, mod 2147483647, length-5 balanced complement (session 60)*  (4.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (19, 7, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 9, claimed 9
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis: 9 independent vectors = a — rank 9, a = 9
- [x] evaluation of the a = 9 highest-weight vectors at 17 recorded det_pencil points has rank a mod 2147483647 — rank 9
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 9 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/19_7_2_2_2_d8_reducible_p2147483647.json.gz`

*mult_reducible((19, 7, 2, 2, 2), 8) = a = 9, mod 2147483647, length-5 balanced complement (session 60)*  (4.0s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (19, 7, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 9, claimed 9
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis: 9 independent vectors = a — rank 9, a = 9
- [x] evaluation of the a = 9 highest-weight vectors at 17 recorded reducible points has rank a mod 2147483647 — rank 9
- [x] conclusion: mult_reducible(lambda, delta) = a = 9 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/19_7_4_1_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((19, 7, 4, 1, 1), 8) = a = 9, mod 2147483647, length-5 balanced complement (session 60)*  (1.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (19, 7, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 9, claimed 9
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis: 9 independent vectors = a — rank 9, a = 9
- [x] evaluation of the a = 9 highest-weight vectors at 17 recorded det_pencil points has rank a mod 2147483647 — rank 9
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 9 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/19_7_4_1_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((19, 7, 4, 1, 1), 8) = a = 9, mod 2147483647, length-5 balanced complement (session 60)*  (1.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (19, 7, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 9, claimed 9
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis: 9 independent vectors = a — rank 9, a = 9
- [x] evaluation of the a = 9 highest-weight vectors at 17 recorded reducible points has rank a mod 2147483647 — rank 9
- [x] conclusion: mult_reducible(lambda, delta) = a = 9 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/19_8_2_2_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((19, 8, 2, 2, 1), 8) = a = 9, mod 2147483647, length-5 balanced complement (session 60)*  (1.9s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (19, 8, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 9, claimed 9
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis: 9 independent vectors = a — rank 9, a = 9
- [x] evaluation of the a = 9 highest-weight vectors at 17 recorded det_pencil points has rank a mod 2147483647 — rank 9
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 9 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/19_8_2_2_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((19, 8, 2, 2, 1), 8) = a = 9, mod 2147483647, length-5 balanced complement (session 60)*  (1.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (19, 8, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 9, claimed 9
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis: 9 independent vectors = a — rank 9, a = 9
- [x] evaluation of the a = 9 highest-weight vectors at 17 recorded reducible points has rank a mod 2147483647 — rank 9
- [x] conclusion: mult_reducible(lambda, delta) = a = 9 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/19_8_3_1_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((19, 8, 3, 1, 1), 8) = a = 5, mod 2147483647, length-5 balanced complement (session 60)*  (0.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (19, 8, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis: 5 independent vectors = a — rank 5, a = 5
- [x] evaluation of the a = 5 highest-weight vectors at 13 recorded det_pencil points has rank a mod 2147483647 — rank 5
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 5 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/19_8_3_1_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((19, 8, 3, 1, 1), 8) = a = 5, mod 2147483647, length-5 balanced complement (session 60)*  (0.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (19, 8, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis: 5 independent vectors = a — rank 5, a = 5
- [x] evaluation of the a = 5 highest-weight vectors at 13 recorded reducible points has rank a mod 2147483647 — rank 5
- [x] conclusion: mult_reducible(lambda, delta) = a = 5 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/20_11_3_1_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((20, 11, 3, 1, 1), 9) = a = 13, mod 2147483647, length-5 balanced complement (session 60)*  (4.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (20, 11, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 13, claimed 13
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis vector 12: highest weight mod 2147483647
- [x] basis: 13 independent vectors = a — rank 13, a = 13
- [x] evaluation of the a = 13 highest-weight vectors at 21 recorded det_pencil points has rank a mod 2147483647 — rank 13
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 13 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/20_11_3_1_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((20, 11, 3, 1, 1), 9) = a = 13, mod 2147483647, length-5 balanced complement (session 60)*  (4.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (20, 11, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 13, claimed 13
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis vector 12: highest weight mod 2147483647
- [x] basis: 13 independent vectors = a — rank 13, a = 13
- [x] evaluation of the a = 13 highest-weight vectors at 21 recorded reducible points has rank a mod 2147483647 — rank 13
- [x] conclusion: mult_reducible(lambda, delta) = a = 13 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/20_12_2_1_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((20, 12, 2, 1, 1), 9) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (20, 12, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/20_12_2_1_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((20, 12, 2, 1, 1), 9) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (20, 12, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/20_4_4_2_2_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((20, 4, 4, 2, 2), 8) = a = 6, mod 2147483647, length-5 balanced complement (session 60)*  (4.0s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (20, 4, 4, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis: 6 independent vectors = a — rank 6, a = 6
- [x] evaluation of the a = 6 highest-weight vectors at 14 recorded det_pencil points has rank a mod 2147483647 — rank 6
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/20_4_4_2_2_d8_reducible_p2147483647.json.gz`

*mult_reducible((20, 4, 4, 2, 2), 8) = a = 6, mod 2147483647, length-5 balanced complement (session 60)*  (3.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (20, 4, 4, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis: 6 independent vectors = a — rank 6, a = 6
- [x] evaluation of the a = 6 highest-weight vectors at 14 recorded reducible points has rank a mod 2147483647 — rank 6
- [x] conclusion: mult_reducible(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/20_5_3_3_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((20, 5, 3, 3, 1), 8) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (20, 5, 3, 3, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/20_5_3_3_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((20, 5, 3, 3, 1), 8) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (20, 5, 3, 3, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/20_5_5_1_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((20, 5, 5, 1, 1), 8) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (20, 5, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/20_5_5_1_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((20, 5, 5, 1, 1), 8) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (20, 5, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/20_6_2_2_2_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((20, 6, 2, 2, 2), 8) = a = 8, mod 2147483647, length-5 balanced complement (session 60)*  (2.1s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (20, 6, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 8, claimed 8
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis: 8 independent vectors = a — rank 8, a = 8
- [x] evaluation of the a = 8 highest-weight vectors at 16 recorded det_pencil points has rank a mod 2147483647 — rank 8
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 8 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/20_6_2_2_2_d8_reducible_p2147483647.json.gz`

*mult_reducible((20, 6, 2, 2, 2), 8) = a = 8, mod 2147483647, length-5 balanced complement (session 60)*  (2.0s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (20, 6, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 8, claimed 8
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis: 8 independent vectors = a — rank 8, a = 8
- [x] evaluation of the a = 8 highest-weight vectors at 16 recorded reducible points has rank a mod 2147483647 — rank 8
- [x] conclusion: mult_reducible(lambda, delta) = a = 8 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/20_6_4_1_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((20, 6, 4, 1, 1), 8) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (20, 6, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/20_6_4_1_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((20, 6, 4, 1, 1), 8) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (20, 6, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/20_7_2_2_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((20, 7, 2, 2, 1), 8) = a = 6, mod 2147483647, length-5 balanced complement (session 60)*  (0.9s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (20, 7, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis: 6 independent vectors = a — rank 6, a = 6
- [x] evaluation of the a = 6 highest-weight vectors at 14 recorded det_pencil points has rank a mod 2147483647 — rank 6
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/20_7_2_2_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((20, 7, 2, 2, 1), 8) = a = 6, mod 2147483647, length-5 balanced complement (session 60)*  (0.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (20, 7, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis: 6 independent vectors = a — rank 6, a = 6
- [x] evaluation of the a = 6 highest-weight vectors at 14 recorded reducible points has rank a mod 2147483647 — rank 6
- [x] conclusion: mult_reducible(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/20_7_3_1_1_d8_det_pencil_p2147483629.json.gz`

*mult_det_pencil((20, 7, 3, 1, 1), 8) = a = 4, mod 2147483629, length-5 balanced complement (session 60)*  (25.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (20, 7, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2688, nullity 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483629 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/20_7_3_1_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((20, 7, 3, 1, 1), 8) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (26.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (20, 7, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2688, nullity 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/20_7_3_1_1_d8_reducible_p2147483629.json.gz`

*mult_reducible((20, 7, 3, 1, 1), 8) = a = 4, mod 2147483629, length-5 balanced complement (session 60)*  (26.0s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (20, 7, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2688, nullity 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483629 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/20_7_3_1_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((20, 7, 3, 1, 1), 8) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (25.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (20, 7, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2688, nullity 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/21_10_3_1_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((21, 10, 3, 1, 1), 9) = a = 10, mod 2147483647, length-5 balanced complement (session 60)*  (2.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (21, 10, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 10, claimed 10
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis: 10 independent vectors = a — rank 10, a = 10
- [x] evaluation of the a = 10 highest-weight vectors at 18 recorded det_pencil points has rank a mod 2147483647 — rank 10
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 10 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/21_10_3_1_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((21, 10, 3, 1, 1), 9) = a = 10, mod 2147483647, length-5 balanced complement (session 60)*  (2.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (21, 10, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 10, claimed 10
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis: 10 independent vectors = a — rank 10, a = 10
- [x] evaluation of the a = 10 highest-weight vectors at 18 recorded reducible points has rank a mod 2147483647 — rank 10
- [x] conclusion: mult_reducible(lambda, delta) = a = 10 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/21_11_2_1_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((21, 11, 2, 1, 1), 9) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (21, 11, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/21_11_2_1_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((21, 11, 2, 1, 1), 9) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (21, 11, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/21_4_3_2_2_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((21, 4, 3, 2, 2), 8) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (21, 4, 3, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/21_4_3_2_2_d8_reducible_p2147483647.json.gz`

*mult_reducible((21, 4, 3, 2, 2), 8) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (21, 4, 3, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/21_4_4_2_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((21, 4, 4, 2, 1), 8) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (21, 4, 4, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/21_4_4_2_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((21, 4, 4, 2, 1), 8) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (21, 4, 4, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/21_5_2_2_2_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((21, 5, 2, 2, 2), 8) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (21, 5, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/21_5_2_2_2_d8_reducible_p2147483647.json.gz`

*mult_reducible((21, 5, 2, 2, 2), 8) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (21, 5, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/21_5_3_2_1_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((21, 5, 3, 2, 1), 8) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (21, 5, 3, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/21_5_3_2_1_d8_reducible_p2147483647.json.gz`

*mult_reducible((21, 5, 3, 2, 1), 8) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (21, 5, 3, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/21_9_4_1_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((21, 9, 4, 1, 1), 9) = a = 21, mod 2147483647, length-5 balanced complement (session 60)*  (12.1s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (21, 9, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 21, claimed 21
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis vector 12: highest weight mod 2147483647
- [x] basis vector 13: highest weight mod 2147483647
- [x] basis vector 14: highest weight mod 2147483647
- [x] basis vector 15: highest weight mod 2147483647
- [x] basis vector 16: highest weight mod 2147483647
- [x] basis vector 17: highest weight mod 2147483647
- [x] basis vector 18: highest weight mod 2147483647
- [x] basis vector 19: highest weight mod 2147483647
- [x] basis vector 20: highest weight mod 2147483647
- [x] basis: 21 independent vectors = a — rank 21, a = 21
- [x] evaluation of the a = 21 highest-weight vectors at 29 recorded det_pencil points has rank a mod 2147483647 — rank 21
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 21 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/21_9_4_1_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((21, 9, 4, 1, 1), 9) = a = 21, mod 2147483647, length-5 balanced complement (session 60)*  (11.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (21, 9, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 21, claimed 21
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis vector 12: highest weight mod 2147483647
- [x] basis vector 13: highest weight mod 2147483647
- [x] basis vector 14: highest weight mod 2147483647
- [x] basis vector 15: highest weight mod 2147483647
- [x] basis vector 16: highest weight mod 2147483647
- [x] basis vector 17: highest weight mod 2147483647
- [x] basis vector 18: highest weight mod 2147483647
- [x] basis vector 19: highest weight mod 2147483647
- [x] basis vector 20: highest weight mod 2147483647
- [x] basis: 21 independent vectors = a — rank 21, a = 21
- [x] evaluation of the a = 21 highest-weight vectors at 29 recorded reducible points has rank a mod 2147483647 — rank 21
- [x] conclusion: mult_reducible(lambda, delta) = a = 21 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/22_10_2_1_1_d9_det_pencil_p2147483629.json.gz`

*mult_det_pencil((22, 10, 2, 1, 1), 9) = a = 2, mod 2147483629, length-5 balanced complement (session 60)*  (31.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (22, 10, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2885, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483629 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/22_10_2_1_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((22, 10, 2, 1, 1), 9) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (31.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (22, 10, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2885, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/22_10_2_1_1_d9_reducible_p2147483629.json.gz`

*mult_reducible((22, 10, 2, 1, 1), 9) = a = 2, mod 2147483629, length-5 balanced complement (session 60)*  (32.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (22, 10, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2885, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483629 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/22_10_2_1_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((22, 10, 2, 1, 1), 9) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (31.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (22, 10, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2885, nullity 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/22_4_2_2_2_d8_det_pencil_p2147483629.json.gz`

*mult_det_pencil((22, 4, 2, 2, 2), 8) = a = 3, mod 2147483629, length-5 balanced complement (session 60)*  (26.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (22, 4, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2625, nullity 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483629 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/22_4_2_2_2_d8_det_pencil_p2147483647.json.gz`

*mult_det_pencil((22, 4, 2, 2, 2), 8) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (26.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (22, 4, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2625, nullity 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/22_4_2_2_2_d8_reducible_p2147483629.json.gz`

*mult_reducible((22, 4, 2, 2, 2), 8) = a = 3, mod 2147483629, length-5 balanced complement (session 60)*  (27.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (22, 4, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2625, nullity 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483629 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/22_4_2_2_2_d8_reducible_p2147483647.json.gz`

*mult_reducible((22, 4, 2, 2, 2), 8) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (26.9s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (22, 4, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 32 vs 4*8
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2625, nullity 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/22_6_6_1_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((22, 6, 6, 1, 1), 9) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.9s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (22, 6, 6, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/22_6_6_1_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((22, 6, 6, 1, 1), 9) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (22, 6, 6, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/22_7_5_1_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((22, 7, 5, 1, 1), 9) = a = 15, mod 2147483647, length-5 balanced complement (session 60)*  (7.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (22, 7, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 15, claimed 15
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis vector 12: highest weight mod 2147483647
- [x] basis vector 13: highest weight mod 2147483647
- [x] basis vector 14: highest weight mod 2147483647
- [x] basis: 15 independent vectors = a — rank 15, a = 15
- [x] evaluation of the a = 15 highest-weight vectors at 23 recorded det_pencil points has rank a mod 2147483647 — rank 15
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 15 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/22_7_5_1_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((22, 7, 5, 1, 1), 9) = a = 15, mod 2147483647, length-5 balanced complement (session 60)*  (7.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (22, 7, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 15, claimed 15
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis vector 12: highest weight mod 2147483647
- [x] basis vector 13: highest weight mod 2147483647
- [x] basis vector 14: highest weight mod 2147483647
- [x] basis: 15 independent vectors = a — rank 15, a = 15
- [x] evaluation of the a = 15 highest-weight vectors at 23 recorded reducible points has rank a mod 2147483647 — rank 15
- [x] conclusion: mult_reducible(lambda, delta) = a = 15 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/22_8_2_2_2_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((22, 8, 2, 2, 2), 9) = a = 17, mod 2147483647, length-5 balanced complement (session 60)*  (14.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (22, 8, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 17, claimed 17
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis vector 12: highest weight mod 2147483647
- [x] basis vector 13: highest weight mod 2147483647
- [x] basis vector 14: highest weight mod 2147483647
- [x] basis vector 15: highest weight mod 2147483647
- [x] basis vector 16: highest weight mod 2147483647
- [x] basis: 17 independent vectors = a — rank 17, a = 17
- [x] evaluation of the a = 17 highest-weight vectors at 25 recorded det_pencil points has rank a mod 2147483647 — rank 17
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 17 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/22_8_2_2_2_d9_reducible_p2147483647.json.gz`

*mult_reducible((22, 8, 2, 2, 2), 9) = a = 17, mod 2147483647, length-5 balanced complement (session 60)*  (14.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (22, 8, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 17, claimed 17
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis vector 12: highest weight mod 2147483647
- [x] basis vector 13: highest weight mod 2147483647
- [x] basis vector 14: highest weight mod 2147483647
- [x] basis vector 15: highest weight mod 2147483647
- [x] basis vector 16: highest weight mod 2147483647
- [x] basis: 17 independent vectors = a — rank 17, a = 17
- [x] evaluation of the a = 17 highest-weight vectors at 25 recorded reducible points has rank a mod 2147483647 — rank 17
- [x] conclusion: mult_reducible(lambda, delta) = a = 17 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/22_8_4_1_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((22, 8, 4, 1, 1), 9) = a = 12, mod 2147483647, length-5 balanced complement (session 60)*  (3.9s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (22, 8, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 12, claimed 12
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis: 12 independent vectors = a — rank 12, a = 12
- [x] evaluation of the a = 12 highest-weight vectors at 20 recorded det_pencil points has rank a mod 2147483647 — rank 12
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 12 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/22_8_4_1_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((22, 8, 4, 1, 1), 9) = a = 12, mod 2147483647, length-5 balanced complement (session 60)*  (3.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (22, 8, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 12, claimed 12
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis: 12 independent vectors = a — rank 12, a = 12
- [x] evaluation of the a = 12 highest-weight vectors at 20 recorded reducible points has rank a mod 2147483647 — rank 12
- [x] conclusion: mult_reducible(lambda, delta) = a = 12 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/22_9_2_2_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((22, 9, 2, 2, 1), 9) = a = 13, mod 2147483647, length-5 balanced complement (session 60)*  (4.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (22, 9, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 13, claimed 13
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis vector 12: highest weight mod 2147483647
- [x] basis: 13 independent vectors = a — rank 13, a = 13
- [x] evaluation of the a = 13 highest-weight vectors at 21 recorded det_pencil points has rank a mod 2147483647 — rank 13
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 13 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/22_9_2_2_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((22, 9, 2, 2, 1), 9) = a = 13, mod 2147483647, length-5 balanced complement (session 60)*  (4.1s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (22, 9, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 13, claimed 13
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis vector 12: highest weight mod 2147483647
- [x] basis: 13 independent vectors = a — rank 13, a = 13
- [x] evaluation of the a = 13 highest-weight vectors at 21 recorded reducible points has rank a mod 2147483647 — rank 13
- [x] conclusion: mult_reducible(lambda, delta) = a = 13 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/22_9_3_1_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((22, 9, 3, 1, 1), 9) = a = 8, mod 2147483647, length-5 balanced complement (session 60)*  (1.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (22, 9, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 8, claimed 8
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis: 8 independent vectors = a — rank 8, a = 8
- [x] evaluation of the a = 8 highest-weight vectors at 16 recorded det_pencil points has rank a mod 2147483647 — rank 8
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 8 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/22_9_3_1_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((22, 9, 3, 1, 1), 9) = a = 8, mod 2147483647, length-5 balanced complement (session 60)*  (1.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (22, 9, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 8, claimed 8
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis: 8 independent vectors = a — rank 8, a = 8
- [x] evaluation of the a = 8 highest-weight vectors at 16 recorded reducible points has rank a mod 2147483647 — rank 8
- [x] conclusion: mult_reducible(lambda, delta) = a = 8 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/23_4_4_4_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((23, 4, 4, 4, 1), 9) = a = 5, mod 2147483647, length-5 balanced complement (session 60)*  (6.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (23, 4, 4, 4, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis: 5 independent vectors = a — rank 5, a = 5
- [x] evaluation of the a = 5 highest-weight vectors at 13 recorded det_pencil points has rank a mod 2147483647 — rank 5
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 5 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/23_4_4_4_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((23, 4, 4, 4, 1), 9) = a = 5, mod 2147483647, length-5 balanced complement (session 60)*  (6.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (23, 4, 4, 4, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis: 5 independent vectors = a — rank 5, a = 5
- [x] evaluation of the a = 5 highest-weight vectors at 13 recorded reducible points has rank a mod 2147483647 — rank 5
- [x] conclusion: mult_reducible(lambda, delta) = a = 5 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/23_6_5_1_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((23, 6, 5, 1, 1), 9) = a = 5, mod 2147483647, length-5 balanced complement (session 60)*  (1.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (23, 6, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis: 5 independent vectors = a — rank 5, a = 5
- [x] evaluation of the a = 5 highest-weight vectors at 13 recorded det_pencil points has rank a mod 2147483647 — rank 5
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 5 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/23_6_5_1_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((23, 6, 5, 1, 1), 9) = a = 5, mod 2147483647, length-5 balanced complement (session 60)*  (1.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (23, 6, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis: 5 independent vectors = a — rank 5, a = 5
- [x] evaluation of the a = 5 highest-weight vectors at 13 recorded reducible points has rank a mod 2147483647 — rank 5
- [x] conclusion: mult_reducible(lambda, delta) = a = 5 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/23_7_2_2_2_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((23, 7, 2, 2, 2), 9) = a = 10, mod 2147483647, length-5 balanced complement (session 60)*  (5.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (23, 7, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 10, claimed 10
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis: 10 independent vectors = a — rank 10, a = 10
- [x] evaluation of the a = 10 highest-weight vectors at 18 recorded det_pencil points has rank a mod 2147483647 — rank 10
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 10 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/23_7_2_2_2_d9_reducible_p2147483647.json.gz`

*mult_reducible((23, 7, 2, 2, 2), 9) = a = 10, mod 2147483647, length-5 balanced complement (session 60)*  (5.0s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (23, 7, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 10, claimed 10
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis: 10 independent vectors = a — rank 10, a = 10
- [x] evaluation of the a = 10 highest-weight vectors at 18 recorded reducible points has rank a mod 2147483647 — rank 10
- [x] conclusion: mult_reducible(lambda, delta) = a = 10 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/23_7_4_1_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((23, 7, 4, 1, 1), 9) = a = 9, mod 2147483647, length-5 balanced complement (session 60)*  (2.0s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (23, 7, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 9, claimed 9
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis: 9 independent vectors = a — rank 9, a = 9
- [x] evaluation of the a = 9 highest-weight vectors at 17 recorded det_pencil points has rank a mod 2147483647 — rank 9
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 9 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/23_7_4_1_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((23, 7, 4, 1, 1), 9) = a = 9, mod 2147483647, length-5 balanced complement (session 60)*  (1.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (23, 7, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 9, claimed 9
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis: 9 independent vectors = a — rank 9, a = 9
- [x] evaluation of the a = 9 highest-weight vectors at 17 recorded reducible points has rank a mod 2147483647 — rank 9
- [x] conclusion: mult_reducible(lambda, delta) = a = 9 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/23_8_2_2_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((23, 8, 2, 2, 1), 9) = a = 10, mod 2147483647, length-5 balanced complement (session 60)*  (2.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (23, 8, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 10, claimed 10
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis: 10 independent vectors = a — rank 10, a = 10
- [x] evaluation of the a = 10 highest-weight vectors at 18 recorded det_pencil points has rank a mod 2147483647 — rank 10
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 10 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/23_8_2_2_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((23, 8, 2, 2, 1), 9) = a = 10, mod 2147483647, length-5 balanced complement (session 60)*  (2.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (23, 8, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 10, claimed 10
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis: 10 independent vectors = a — rank 10, a = 10
- [x] evaluation of the a = 10 highest-weight vectors at 18 recorded reducible points has rank a mod 2147483647 — rank 10
- [x] conclusion: mult_reducible(lambda, delta) = a = 10 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/23_8_3_1_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((23, 8, 3, 1, 1), 9) = a = 5, mod 2147483647, length-5 balanced complement (session 60)*  (0.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (23, 8, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis: 5 independent vectors = a — rank 5, a = 5
- [x] evaluation of the a = 5 highest-weight vectors at 13 recorded det_pencil points has rank a mod 2147483647 — rank 5
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 5 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/23_8_3_1_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((23, 8, 3, 1, 1), 9) = a = 5, mod 2147483647, length-5 balanced complement (session 60)*  (0.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (23, 8, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis: 5 independent vectors = a — rank 5, a = 5
- [x] evaluation of the a = 5 highest-weight vectors at 13 recorded reducible points has rank a mod 2147483647 — rank 5
- [x] conclusion: mult_reducible(lambda, delta) = a = 5 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/24_12_2_1_1_d10_det_pencil_p2147483647.json.gz`

*mult_det_pencil((24, 12, 2, 1, 1), 10) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (24, 12, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 40 vs 4*10
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/24_12_2_1_1_d10_reducible_p2147483647.json.gz`

*mult_reducible((24, 12, 2, 1, 1), 10) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (24, 12, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 40 vs 4*10
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/24_4_4_2_2_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((24, 4, 4, 2, 2), 9) = a = 6, mod 2147483647, length-5 balanced complement (session 60)*  (4.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (24, 4, 4, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis: 6 independent vectors = a — rank 6, a = 6
- [x] evaluation of the a = 6 highest-weight vectors at 14 recorded det_pencil points has rank a mod 2147483647 — rank 6
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/24_4_4_2_2_d9_reducible_p2147483647.json.gz`

*mult_reducible((24, 4, 4, 2, 2), 9) = a = 6, mod 2147483647, length-5 balanced complement (session 60)*  (4.1s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (24, 4, 4, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis: 6 independent vectors = a — rank 6, a = 6
- [x] evaluation of the a = 6 highest-weight vectors at 14 recorded reducible points has rank a mod 2147483647 — rank 6
- [x] conclusion: mult_reducible(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/24_5_3_3_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((24, 5, 3, 3, 1), 9) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (24, 5, 3, 3, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/24_5_3_3_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((24, 5, 3, 3, 1), 9) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (24, 5, 3, 3, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/24_5_5_1_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((24, 5, 5, 1, 1), 9) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (24, 5, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/24_5_5_1_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((24, 5, 5, 1, 1), 9) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (24, 5, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/24_6_2_2_2_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((24, 6, 2, 2, 2), 9) = a = 9, mod 2147483647, length-5 balanced complement (session 60)*  (2.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (24, 6, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 9, claimed 9
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis: 9 independent vectors = a — rank 9, a = 9
- [x] evaluation of the a = 9 highest-weight vectors at 17 recorded det_pencil points has rank a mod 2147483647 — rank 9
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 9 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/24_6_2_2_2_d9_reducible_p2147483647.json.gz`

*mult_reducible((24, 6, 2, 2, 2), 9) = a = 9, mod 2147483647, length-5 balanced complement (session 60)*  (2.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (24, 6, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 9, claimed 9
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis: 9 independent vectors = a — rank 9, a = 9
- [x] evaluation of the a = 9 highest-weight vectors at 17 recorded reducible points has rank a mod 2147483647 — rank 9
- [x] conclusion: mult_reducible(lambda, delta) = a = 9 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/24_6_4_1_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((24, 6, 4, 1, 1), 9) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (24, 6, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/24_6_4_1_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((24, 6, 4, 1, 1), 9) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (24, 6, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/24_7_2_2_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((24, 7, 2, 2, 1), 9) = a = 6, mod 2147483647, length-5 balanced complement (session 60)*  (0.9s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (24, 7, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis: 6 independent vectors = a — rank 6, a = 6
- [x] evaluation of the a = 6 highest-weight vectors at 14 recorded det_pencil points has rank a mod 2147483647 — rank 6
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/24_7_2_2_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((24, 7, 2, 2, 1), 9) = a = 6, mod 2147483647, length-5 balanced complement (session 60)*  (0.9s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (24, 7, 2, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis: 6 independent vectors = a — rank 6, a = 6
- [x] evaluation of the a = 6 highest-weight vectors at 14 recorded reducible points has rank a mod 2147483647 — rank 6
- [x] conclusion: mult_reducible(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/24_7_3_1_1_d9_det_pencil_p2147483629.json.gz`

*mult_det_pencil((24, 7, 3, 1, 1), 9) = a = 4, mod 2147483629, length-5 balanced complement (session 60)*  (15.1s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (24, 7, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2804, nullity 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483629 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/24_7_3_1_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((24, 7, 3, 1, 1), 9) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (14.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (24, 7, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2804, nullity 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/24_7_3_1_1_d9_reducible_p2147483629.json.gz`

*mult_reducible((24, 7, 3, 1, 1), 9) = a = 4, mod 2147483629, length-5 balanced complement (session 60)*  (15.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (24, 7, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2804, nullity 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483629 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/24_7_3_1_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((24, 7, 3, 1, 1), 9) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (15.0s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (24, 7, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2804, nullity 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/25_10_3_1_1_d10_det_pencil_p2147483647.json.gz`

*mult_det_pencil((25, 10, 3, 1, 1), 10) = a = 11, mod 2147483647, length-5 balanced complement (session 60)*  (1.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (25, 10, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 40 vs 4*10
- [x] cell: a recomputed (Weyl alternation) — recomputed 11, claimed 11
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis: 11 independent vectors = a — rank 11, a = 11
- [x] evaluation of the a = 11 highest-weight vectors at 19 recorded det_pencil points has rank a mod 2147483647 — rank 11
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 11 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/25_10_3_1_1_d10_reducible_p2147483647.json.gz`

*mult_reducible((25, 10, 3, 1, 1), 10) = a = 11, mod 2147483647, length-5 balanced complement (session 60)*  (1.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (25, 10, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 40 vs 4*10
- [x] cell: a recomputed (Weyl alternation) — recomputed 11, claimed 11
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis: 11 independent vectors = a — rank 11, a = 11
- [x] evaluation of the a = 11 highest-weight vectors at 19 recorded reducible points has rank a mod 2147483647 — rank 11
- [x] conclusion: mult_reducible(lambda, delta) = a = 11 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/25_4_3_2_2_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((25, 4, 3, 2, 2), 9) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (25, 4, 3, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/25_4_3_2_2_d9_reducible_p2147483647.json.gz`

*mult_reducible((25, 4, 3, 2, 2), 9) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (25, 4, 3, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/25_4_4_2_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((25, 4, 4, 2, 1), 9) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (25, 4, 4, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/25_4_4_2_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((25, 4, 4, 2, 1), 9) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (25, 4, 4, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis: 3 independent vectors = a — rank 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/25_5_2_2_2_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((25, 5, 2, 2, 2), 9) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (25, 5, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/25_5_2_2_2_d9_reducible_p2147483647.json.gz`

*mult_reducible((25, 5, 2, 2, 2), 9) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (25, 5, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/25_5_3_2_1_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((25, 5, 3, 2, 1), 9) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (25, 5, 3, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded det_pencil points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/25_5_3_2_1_d9_reducible_p2147483647.json.gz`

*mult_reducible((25, 5, 3, 2, 1), 9) = a = 4, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (25, 5, 3, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis: 4 independent vectors = a — rank 4, a = 4
- [x] evaluation of the a = 4 highest-weight vectors at 12 recorded reducible points has rank a mod 2147483647 — rank 4
- [x] conclusion: mult_reducible(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/26_4_2_2_2_d9_det_pencil_p2147483629.json.gz`

*mult_det_pencil((26, 4, 2, 2, 2), 9) = a = 3, mod 2147483629, length-5 balanced complement (session 60)*  (14.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (26, 4, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2635, nullity 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483629 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/26_4_2_2_2_d9_det_pencil_p2147483647.json.gz`

*mult_det_pencil((26, 4, 2, 2, 2), 9) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (14.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (26, 4, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2635, nullity 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded det_pencil points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/26_4_2_2_2_d9_reducible_p2147483629.json.gz`

*mult_reducible((26, 4, 2, 2, 2), 9) = a = 3, mod 2147483629, length-5 balanced complement (session 60)*  (14.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (26, 4, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 2635, nullity 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483629 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/26_4_2_2_2_d9_reducible_p2147483647.json.gz`

*mult_reducible((26, 4, 2, 2, 2), 9) = a = 3, mod 2147483647, length-5 balanced complement (session 60)*  (14.1s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (26, 4, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 4*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 3, claimed 3
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 2635, nullity 3, a = 3
- [x] evaluation of the a = 3 highest-weight vectors at 11 recorded reducible points has rank a mod 2147483647 — rank 3
- [x] conclusion: mult_reducible(lambda, delta) = a = 3 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/27_13_2_1_1_d11_det_pencil_p2147483647.json.gz`

*mult_det_pencil((27, 13, 2, 1, 1), 11) = a = 6, mod 2147483647, length-5 balanced complement (session 60)*  (0.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (27, 13, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 44 vs 4*11
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis: 6 independent vectors = a — rank 6, a = 6
- [x] evaluation of the a = 6 highest-weight vectors at 14 recorded det_pencil points has rank a mod 2147483647 — rank 6
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/27_13_2_1_1_d11_reducible_p2147483647.json.gz`

*mult_reducible((27, 13, 2, 1, 1), 11) = a = 6, mod 2147483647, length-5 balanced complement (session 60)*  (0.5s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (27, 13, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 44 vs 4*11
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis: 6 independent vectors = a — rank 6, a = 6
- [x] evaluation of the a = 6 highest-weight vectors at 14 recorded reducible points has rank a mod 2147483647 — rank 6
- [x] conclusion: mult_reducible(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/27_7_2_2_2_d10_det_pencil_p2147483647.json.gz`

*mult_det_pencil((27, 7, 2, 2, 2), 10) = a = 11, mod 2147483647, length-5 balanced complement (session 60)*  (3.1s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (27, 7, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 40 vs 4*10
- [x] cell: a recomputed (Weyl alternation) — recomputed 11, claimed 11
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis: 11 independent vectors = a — rank 11, a = 11
- [x] evaluation of the a = 11 highest-weight vectors at 19 recorded det_pencil points has rank a mod 2147483647 — rank 11
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 11 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/27_7_2_2_2_d10_reducible_p2147483647.json.gz`

*mult_reducible((27, 7, 2, 2, 2), 10) = a = 11, mod 2147483647, length-5 balanced complement (session 60)*  (3.0s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (27, 7, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 40 vs 4*10
- [x] cell: a recomputed (Weyl alternation) — recomputed 11, claimed 11
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis: 11 independent vectors = a — rank 11, a = 11
- [x] evaluation of the a = 11 highest-weight vectors at 19 recorded reducible points has rank a mod 2147483647 — rank 11
- [x] conclusion: mult_reducible(lambda, delta) = a = 11 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/28_11_3_1_1_d11_det_pencil_p2147483647.json.gz`

*mult_det_pencil((28, 11, 3, 1, 1), 11) = a = 16, mod 2147483647, length-5 balanced complement (session 60)*  (3.6s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (28, 11, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 44 vs 4*11
- [x] cell: a recomputed (Weyl alternation) — recomputed 16, claimed 16
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis vector 12: highest weight mod 2147483647
- [x] basis vector 13: highest weight mod 2147483647
- [x] basis vector 14: highest weight mod 2147483647
- [x] basis vector 15: highest weight mod 2147483647
- [x] basis: 16 independent vectors = a — rank 16, a = 16
- [x] evaluation of the a = 16 highest-weight vectors at 24 recorded det_pencil points has rank a mod 2147483647 — rank 16
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 16 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/28_11_3_1_1_d11_reducible_p2147483647.json.gz`

*mult_reducible((28, 11, 3, 1, 1), 11) = a = 16, mod 2147483647, length-5 balanced complement (session 60)*  (3.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (28, 11, 3, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 44 vs 4*11
- [x] cell: a recomputed (Weyl alternation) — recomputed 16, claimed 16
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis vector 12: highest weight mod 2147483647
- [x] basis vector 13: highest weight mod 2147483647
- [x] basis vector 14: highest weight mod 2147483647
- [x] basis vector 15: highest weight mod 2147483647
- [x] basis: 16 independent vectors = a — rank 16, a = 16
- [x] evaluation of the a = 16 highest-weight vectors at 24 recorded reducible points has rank a mod 2147483647 — rank 16
- [x] conclusion: mult_reducible(lambda, delta) = a = 16 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/30_14_2_1_1_d12_det_pencil_p2147483647.json.gz`

*mult_det_pencil((30, 14, 2, 1, 1), 12) = a = 6, mod 2147483647, length-5 balanced complement (session 60)*  (0.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (30, 14, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 48 vs 4*12
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis: 6 independent vectors = a — rank 6, a = 6
- [x] evaluation of the a = 6 highest-weight vectors at 14 recorded det_pencil points has rank a mod 2147483647 — rank 6
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/30_14_2_1_1_d12_reducible_p2147483647.json.gz`

*mult_reducible((30, 14, 2, 1, 1), 12) = a = 6, mod 2147483647, length-5 balanced complement (session 60)*  (0.8s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (30, 14, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 48 vs 4*12
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis: 6 independent vectors = a — rank 6, a = 6
- [x] evaluation of the a = 6 highest-weight vectors at 14 recorded reducible points has rank a mod 2147483647 — rank 6
- [x] conclusion: mult_reducible(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/30_8_2_2_2_d11_det_pencil_p2147483647.json.gz`

*mult_det_pencil((30, 8, 2, 2, 2), 11) = a = 19, mod 2147483647, length-5 balanced complement (session 60)*  (10.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (30, 8, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 44 vs 4*11
- [x] cell: a recomputed (Weyl alternation) — recomputed 19, claimed 19
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis vector 12: highest weight mod 2147483647
- [x] basis vector 13: highest weight mod 2147483647
- [x] basis vector 14: highest weight mod 2147483647
- [x] basis vector 15: highest weight mod 2147483647
- [x] basis vector 16: highest weight mod 2147483647
- [x] basis vector 17: highest weight mod 2147483647
- [x] basis vector 18: highest weight mod 2147483647
- [x] basis: 19 independent vectors = a — rank 19, a = 19
- [x] evaluation of the a = 19 highest-weight vectors at 27 recorded det_pencil points has rank a mod 2147483647 — rank 19
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 19 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/30_8_2_2_2_d11_reducible_p2147483647.json.gz`

*mult_reducible((30, 8, 2, 2, 2), 11) = a = 19, mod 2147483647, length-5 balanced complement (session 60)*  (10.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (30, 8, 2, 2, 2), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 44 vs 4*11
- [x] cell: a recomputed (Weyl alternation) — recomputed 19, claimed 19
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis vector 9: highest weight mod 2147483647
- [x] basis vector 10: highest weight mod 2147483647
- [x] basis vector 11: highest weight mod 2147483647
- [x] basis vector 12: highest weight mod 2147483647
- [x] basis vector 13: highest weight mod 2147483647
- [x] basis vector 14: highest weight mod 2147483647
- [x] basis vector 15: highest weight mod 2147483647
- [x] basis vector 16: highest weight mod 2147483647
- [x] basis vector 17: highest weight mod 2147483647
- [x] basis vector 18: highest weight mod 2147483647
- [x] basis: 19 independent vectors = a — rank 19, a = 19
- [x] evaluation of the a = 19 highest-weight vectors at 27 recorded reducible points has rank a mod 2147483647 — rank 19
- [x] conclusion: mult_reducible(lambda, delta) = a = 19 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/33_15_2_1_1_d13_det_pencil_p2147483647.json.gz`

*mult_det_pencil((33, 15, 2, 1, 1), 13) = a = 9, mod 2147483647, length-5 balanced complement (session 60)*  (1.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (33, 15, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 52 vs 4*13
- [x] cell: a recomputed (Weyl alternation) — recomputed 9, claimed 9
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis: 9 independent vectors = a — rank 9, a = 9
- [x] evaluation of the a = 9 highest-weight vectors at 17 recorded det_pencil points has rank a mod 2147483647 — rank 9
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 9 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/33_15_2_1_1_d13_reducible_p2147483647.json.gz`

*mult_reducible((33, 15, 2, 1, 1), 13) = a = 9, mod 2147483647, length-5 balanced complement (session 60)*  (1.7s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (33, 15, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 52 vs 4*13
- [x] cell: a recomputed (Weyl alternation) — recomputed 9, claimed 9
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis vector 2: highest weight mod 2147483647
- [x] basis vector 3: highest weight mod 2147483647
- [x] basis vector 4: highest weight mod 2147483647
- [x] basis vector 5: highest weight mod 2147483647
- [x] basis vector 6: highest weight mod 2147483647
- [x] basis vector 7: highest weight mod 2147483647
- [x] basis vector 8: highest weight mod 2147483647
- [x] basis: 9 independent vectors = a — rank 9, a = 9
- [x] evaluation of the a = 9 highest-weight vectors at 17 recorded reducible points has rank a mod 2147483647 — rank 9
- [x] conclusion: mult_reducible(lambda, delta) = a = 9 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/8_7_7_1_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((8, 7, 7, 1, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (8, 7, 7, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/8_7_7_1_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((8, 7, 7, 1, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (8, 7, 7, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/9_7_2_1_1_d5_det_pencil_p2147483629.json.gz`

*mult_det_pencil((9, 7, 2, 1, 1), 5) = a = 1, mod 2147483629, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (9, 7, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 20 vs 4*5
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 621, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded det_pencil points has rank a mod 2147483629 — rank 1
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/9_7_2_1_1_d5_det_pencil_p2147483647.json.gz`

*mult_det_pencil((9, 7, 2, 1, 1), 5) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (9, 7, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 20 vs 4*5
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 621, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded det_pencil points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/9_7_2_1_1_d5_reducible_p2147483629.json.gz`

*mult_reducible((9, 7, 2, 1, 1), 5) = a = 1, mod 2147483629, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (9, 7, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 20 vs 4*5
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483629 has dimension a — N_S = 621, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded reducible points has rank a mod 2147483629 — rank 1
- [x] conclusion: mult_reducible(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/9_7_2_1_1_d5_reducible_p2147483647.json.gz`

*mult_reducible((9, 7, 2, 1, 1), 5) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (0.4s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (9, 7, 2, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 20 vs 4*5
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] kernel of the raising operators mod 2147483647 has dimension a — N_S = 621, nullity 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded reducible points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_reducible(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/9_7_6_1_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((9, 7, 6, 1, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (9, 7, 6, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/9_7_6_1_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((9, 7, 6, 1, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (9, 7, 6, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/9_8_5_1_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((9, 8, 5, 1, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (9, 8, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/9_8_5_1_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((9, 8, 5, 1, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (9, 8, 5, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/9_9_3_2_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((9, 9, 3, 2, 1), 6) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (0.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (9, 9, 3, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis: 1 independent vectors = a — rank 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded det_pencil points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/9_9_3_2_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((9, 9, 3, 2, 1), 6) = a = 1, mod 2147483647, length-5 balanced complement (session 60)*  (0.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (9, 9, 3, 2, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 1, claimed 1
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis: 1 independent vectors = a — rank 1, a = 1
- [x] evaluation of the a = 1 highest-weight vectors at 9 recorded reducible points has rank a mod 2147483647 — rank 1
- [x] conclusion: mult_reducible(lambda, delta) = a = 1 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/9_9_4_1_1_d6_det_pencil_p2147483647.json.gz`

*mult_det_pencil((9, 9, 4, 1, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (9, 9, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/9_9_4_1_1_d6_reducible_p2147483647.json.gz`

*mult_reducible((9, 9, 4, 1, 1), 6) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (0.2s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (9, 9, 4, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 24 vs 4*6
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded reducible points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_reducible(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/9_9_8_1_1_d7_det_pencil_p2147483647.json.gz`

*mult_det_pencil((9, 9, 8, 1, 1), 7) = a = 2, mod 2147483647, length-5 balanced complement (session 60)*  (1.3s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (9, 9, 8, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] basis vector 0: highest weight mod 2147483647
- [x] basis vector 1: highest weight mod 2147483647
- [x] basis: 2 independent vectors = a — rank 2, a = 2
- [x] evaluation of the a = 2 highest-weight vectors at 10 recorded det_pencil points has rank a mod 2147483647 — rank 2
- [x] conclusion: mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a)

## PASS — `results/certs/s60/9_9_8_1_1_d7_red_ideal_p2147483647.json.gz`

*1 highest-weight vector(s) of weight (9, 9, 8, 1, 1), degree 7, in I(R_5) by (star) mod 2147483647 (session 60: mult_red = 1 < a = 2, h_pad = 1)*  (1.1s)

- [x] cell: n = 4 — n = 4
- [x] cell: length(lambda) = r — lambda (9, 9, 8, 1, 1), r 5
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 28 vs 4*7
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] vectors parsed — 1 vector(s), supports [13128], modulus 2147483647
- [x] vector 0: shape, degree, canonical terms, weight = lambda
- [x] vector 0: annihilated by every E_(i,i+1) mod 2147483647
- [x] vectors linearly independent — rank 1 mod 2147483647
- [x] vector 0: (star) support for k = 1 (Theorem (star): lies in I({l^1 c}))
- [x] vanishes at 10 recorded point(s) [reducible]
- [x] evaluation at 10 recorded point(s) [det_pencil] has full row rank — rank 1 of 1
- [x] vanishes at 6 fresh reducible points (seed 20260905)
- [x] vanishes at 6 fresh padded_permanent points (seed 20260905)
- [x] evaluation at 6 fresh det_pencil points (seed 20260905) has full row rank — rank 1 of 1
- [x] evaluation at 6 fresh generic points (seed 20260905) has full row rank — rank 1 of 1

