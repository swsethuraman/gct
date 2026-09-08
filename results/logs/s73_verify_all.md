# Verifier report

16 certificate file(s); verifier tools/verify at 2026-09-08 03:09:42 UTC
PASS 16, FAIL 0, UNPARSEABLE 0, ERROR 0

## PASS — `results/certs/s73/s73_19_7_2_2_2_2_2_d12_n3_det_kernel_vec0_int.json.gz`

*s73: integer highest-weight vector of weight (19, 7, 2, 2, 2, 2, 2) (delta=12, n=3, r=7) in the kernel of the det_pencil evaluation pairing: an element of I(D_7)^HWV not vanishing on P_7*  (69.1s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (19, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 3*12
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] vectors parsed — 1 vector(s), supports [240510], integer coefficients
- [x] vector 0: shape, degree, canonical terms, weight = lambda
- [x] vector 0: annihilated by every E_(i,i+1) over Z
- [x] vectors linearly independent — rank 1 over Q (lower bound from primes [1, 1]; equals the count so exact)
- [x] vanishes at 14 recorded point(s) [det_pencil]
- [x] evaluation at 14 recorded point(s) [permanent_pencil] has full row rank — rank 1 of 1
- [x] vanishes at 6 fresh det_pencil points (seed 20260908)
- [x] evaluation at 6 fresh permanent_pencil points (seed 20260908) has full row rank — rank 1 of 1
- [x] evaluation at 6 fresh generic points (seed 20260908) has full row rank — rank 1 of 1

## PASS — `results/certs/s73/s73_19_7_2_2_2_2_2_d12_n3_det_p2147483629_sparse_nullity.json`

*s73: nullity_p([E; ev_det]) = 1 at p = 2147483629 for lambda = (19, 7, 2, 2, 2, 2, 2), delta = 12 (n = 3, r = 7): mult_det = 5 (>= 5 proved, = 5 measured)*  (10.7s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (19, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 3*12
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 1, mult 5
- [x] claim: 0 <= nullity <= a
- [x] 14 recorded det_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 6 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17047 vs n_chi 17047, f(0) = 1598420533
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 1, nullity 1
- [x] nullity 1: 1 companion hwv certificate(s) named and present — named ['s73_19_7_2_2_2_2_2_d12_n3_det_kernel_vec0_int.json.gz'], present [True]
- [x] conclusion: nullity_p = 1 at p = 2147483629: mult >= 5 proved; = 5 measured, carried to Q by the companion hwv certificate(s) (integer vectors annihilated by the raising operators over Z, vanishing at fresh det_pencil points)
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_19_7_2_2_2_2_2_d12_n3_det_p2147483647_sparse_nullity.json`

*s73: nullity_p([E; ev_det]) = 1 at p = 2147483647 for lambda = (19, 7, 2, 2, 2, 2, 2), delta = 12 (n = 3, r = 7): mult_det = 5 (>= 5 proved, = 5 measured)*  (10.5s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (19, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 3*12
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 1, mult 5
- [x] claim: 0 <= nullity <= a
- [x] 14 recorded det_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 6 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17047 vs n_chi 17047, f(0) = 1438652706
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 1, nullity 1
- [x] nullity 1: 1 companion hwv certificate(s) named and present — named ['s73_19_7_2_2_2_2_2_d12_n3_det_kernel_vec0_int.json.gz'], present [True]
- [x] conclusion: nullity_p = 1 at p = 2147483647: mult >= 5 proved; = 5 measured, carried to Q by the companion hwv certificate(s) (integer vectors annihilated by the raising operators over Z, vanishing at fresh det_pencil points)
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_19_7_2_2_2_2_2_d12_n3_fullE_p2147483647_sparse_nullity.json`

*s73: nullity_p(E) = 6 = a at p = 2147483647 for lambda = (19, 7, 2, 2, 2, 2, 2), delta = 12 (n = 3, r = 7): the raising operators on V_chi have kernel of the plethysm dimension*  (10.4s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (19, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 3*12
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 6, mult 0
- [x] claim: 0 <= nullity <= a
- [x] variety none: no evaluation rows (the kernel of E alone, nullity = a expected) — 0 points, nullity 6, a 6
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17047 vs n_chi 17047, f(0) = 771177339
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 6, nullity 6
- [x] conclusion: nullity_p(E) = 6 = a at p = 2147483647: the 6 kernel vectors (an explicit basis of the highest-weight space mod p) are banked as an artefact by the producer and are NOT certified here (a mod-p basis of this size does not fit a certificate); the count is closed by the Berlekamp-Massey record above
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_19_7_2_2_2_2_2_d12_n3_permanent_p2147483629_sparse_nullity.json`

*s73: nullity_p([E; ev_per]) = 0 at p = 2147483629 for lambda = (19, 7, 2, 2, 2, 2, 2), delta = 12 (n = 3, r = 7): mult_per = 6 = a, proved over Q*  (10.4s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (19, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 3*12
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 0, mult 6
- [x] claim: 0 <= nullity <= a
- [x] 14 recorded permanent_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 6 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17047 vs n_chi 17047, f(0) = 1485065476
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 0, nullity 0
- [x] conclusion: nullity_p([E; ev]) = 0 at p = 2147483629, so mult_permanent_pencil(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a); the row sampling/grouping of E can only lose rank, so the compressed certificate implies the full one
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_19_7_2_2_2_2_2_d12_n3_permanent_p2147483647_sparse_nullity.json`

*s73: nullity_p([E; ev_per]) = 0 at p = 2147483647 for lambda = (19, 7, 2, 2, 2, 2, 2), delta = 12 (n = 3, r = 7): mult_per = 6 = a, proved over Q*  (10.1s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (19, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 3*12
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 0, mult 6
- [x] claim: 0 <= nullity <= a
- [x] 14 recorded permanent_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 6 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17047 vs n_chi 17047, f(0) = 1812513685
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 0, nullity 0
- [x] conclusion: nullity_p([E; ev]) = 0 at p = 2147483647, so mult_permanent_pencil(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a); the row sampling/grouping of E can only lose rank, so the compressed certificate implies the full one
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_22_7_2_2_2_2_2_d13_n3_det_kernel_vec0_int.json.gz`

*s73: integer highest-weight vector of weight (22, 7, 2, 2, 2, 2, 2) (delta=13, n=3, r=7) in the kernel of the det_pencil evaluation pairing: an element of I(D_7)^HWV not vanishing on P_7*  (70.3s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (22, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 39 vs 3*13
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] vectors parsed — 1 vector(s), supports [240510], integer coefficients
- [x] vector 0: shape, degree, canonical terms, weight = lambda
- [x] vector 0: annihilated by every E_(i,i+1) over Z
- [x] vectors linearly independent — rank 1 over Q (lower bound from primes [1, 1]; equals the count so exact)
- [x] vanishes at 14 recorded point(s) [det_pencil]
- [x] evaluation at 14 recorded point(s) [permanent_pencil] has full row rank — rank 1 of 1
- [x] vanishes at 6 fresh det_pencil points (seed 20260908)
- [x] evaluation at 6 fresh permanent_pencil points (seed 20260908) has full row rank — rank 1 of 1
- [x] evaluation at 6 fresh generic points (seed 20260908) has full row rank — rank 1 of 1

## PASS — `results/certs/s73/s73_22_7_2_2_2_2_2_d13_n3_det_p2147483629_sparse_nullity.json`

*s73: nullity_p([E; ev_det]) = 1 at p = 2147483629 for lambda = (22, 7, 2, 2, 2, 2, 2), delta = 13 (n = 3, r = 7): mult_det = 5 (>= 5 proved, = 5 measured)*  (11.7s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (22, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 39 vs 3*13
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 1, mult 5
- [x] claim: 0 <= nullity <= a
- [x] 14 recorded det_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 6 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17306 vs n_chi 17306, f(0) = 1160250683
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 1, nullity 1
- [x] nullity 1: 1 companion hwv certificate(s) named and present — named ['s73_22_7_2_2_2_2_2_d13_n3_det_kernel_vec0_int.json.gz'], present [True]
- [x] conclusion: nullity_p = 1 at p = 2147483629: mult >= 5 proved; = 5 measured, carried to Q by the companion hwv certificate(s) (integer vectors annihilated by the raising operators over Z, vanishing at fresh det_pencil points)
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_22_7_2_2_2_2_2_d13_n3_det_p2147483647_sparse_nullity.json`

*s73: nullity_p([E; ev_det]) = 1 at p = 2147483647 for lambda = (22, 7, 2, 2, 2, 2, 2), delta = 13 (n = 3, r = 7): mult_det = 5 (>= 5 proved, = 5 measured)*  (11.5s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (22, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 39 vs 3*13
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 1, mult 5
- [x] claim: 0 <= nullity <= a
- [x] 14 recorded det_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 6 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17306 vs n_chi 17306, f(0) = 1190862143
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 1, nullity 1
- [x] nullity 1: 1 companion hwv certificate(s) named and present — named ['s73_22_7_2_2_2_2_2_d13_n3_det_kernel_vec0_int.json.gz'], present [True]
- [x] conclusion: nullity_p = 1 at p = 2147483647: mult >= 5 proved; = 5 measured, carried to Q by the companion hwv certificate(s) (integer vectors annihilated by the raising operators over Z, vanishing at fresh det_pencil points)
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_22_7_2_2_2_2_2_d13_n3_permanent_p2147483629_sparse_nullity.json`

*s73: nullity_p([E; ev_per]) = 0 at p = 2147483629 for lambda = (22, 7, 2, 2, 2, 2, 2), delta = 13 (n = 3, r = 7): mult_per = 6 = a, proved over Q*  (11.4s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (22, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 39 vs 3*13
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 0, mult 6
- [x] claim: 0 <= nullity <= a
- [x] 14 recorded permanent_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 6 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17306 vs n_chi 17306, f(0) = 2051383523
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 0, nullity 0
- [x] conclusion: nullity_p([E; ev]) = 0 at p = 2147483629, so mult_permanent_pencil(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a); the row sampling/grouping of E can only lose rank, so the compressed certificate implies the full one
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_22_7_2_2_2_2_2_d13_n3_permanent_p2147483647_sparse_nullity.json`

*s73: nullity_p([E; ev_per]) = 0 at p = 2147483647 for lambda = (22, 7, 2, 2, 2, 2, 2), delta = 13 (n = 3, r = 7): mult_per = 6 = a, proved over Q*  (11.4s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (22, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 39 vs 3*13
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 0, mult 6
- [x] claim: 0 <= nullity <= a
- [x] 14 recorded permanent_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 6 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17306 vs n_chi 17306, f(0) = 1861182039
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 0, nullity 0
- [x] conclusion: nullity_p([E; ev]) = 0 at p = 2147483647, so mult_permanent_pencil(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a); the row sampling/grouping of E can only lose rank, so the compressed certificate implies the full one
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_25_7_2_2_2_2_2_d14_n3_det_kernel_vec0_int.json.gz`

*s73: integer highest-weight vector of weight (25, 7, 2, 2, 2, 2, 2) (delta=14, n=3, r=7) in the kernel of the det_pencil evaluation pairing: an element of I(D_7)^HWV not vanishing on P_7*  (73.5s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (25, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 42 vs 3*14
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] vectors parsed — 1 vector(s), supports [240510], integer coefficients
- [x] vector 0: shape, degree, canonical terms, weight = lambda
- [x] vector 0: annihilated by every E_(i,i+1) over Z
- [x] vectors linearly independent — rank 1 over Q (lower bound from primes [1, 1]; equals the count so exact)
- [x] vanishes at 14 recorded point(s) [det_pencil]
- [x] evaluation at 14 recorded point(s) [permanent_pencil] has full row rank — rank 1 of 1
- [x] vanishes at 6 fresh det_pencil points (seed 20260908)
- [x] evaluation at 6 fresh permanent_pencil points (seed 20260908) has full row rank — rank 1 of 1
- [x] evaluation at 6 fresh generic points (seed 20260908) has full row rank — rank 1 of 1

## PASS — `results/certs/s73/s73_25_7_2_2_2_2_2_d14_n3_det_p2147483629_sparse_nullity.json`

*s73: nullity_p([E; ev_det]) = 1 at p = 2147483629 for lambda = (25, 7, 2, 2, 2, 2, 2), delta = 14 (n = 3, r = 7): mult_det = 5 (>= 5 proved, = 5 measured)*  (13.3s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (25, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 42 vs 3*14
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 1, mult 5
- [x] claim: 0 <= nullity <= a
- [x] 14 recorded det_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 6 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17379 vs n_chi 17379, f(0) = 873341137
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 1, nullity 1
- [x] nullity 1: 1 companion hwv certificate(s) named and present — named ['s73_25_7_2_2_2_2_2_d14_n3_det_kernel_vec0_int.json.gz'], present [True]
- [x] conclusion: nullity_p = 1 at p = 2147483629: mult >= 5 proved; = 5 measured, carried to Q by the companion hwv certificate(s) (integer vectors annihilated by the raising operators over Z, vanishing at fresh det_pencil points)
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_25_7_2_2_2_2_2_d14_n3_det_p2147483647_sparse_nullity.json`

*s73: nullity_p([E; ev_det]) = 1 at p = 2147483647 for lambda = (25, 7, 2, 2, 2, 2, 2), delta = 14 (n = 3, r = 7): mult_det = 5 (>= 5 proved, = 5 measured)*  (12.7s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (25, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 42 vs 3*14
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 1, mult 5
- [x] claim: 0 <= nullity <= a
- [x] 14 recorded det_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 6 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17379 vs n_chi 17379, f(0) = 386655928
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 1, nullity 1
- [x] nullity 1: 1 companion hwv certificate(s) named and present — named ['s73_25_7_2_2_2_2_2_d14_n3_det_kernel_vec0_int.json.gz'], present [True]
- [x] conclusion: nullity_p = 1 at p = 2147483647: mult >= 5 proved; = 5 measured, carried to Q by the companion hwv certificate(s) (integer vectors annihilated by the raising operators over Z, vanishing at fresh det_pencil points)
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_25_7_2_2_2_2_2_d14_n3_permanent_p2147483629_sparse_nullity.json`

*s73: nullity_p([E; ev_per]) = 0 at p = 2147483629 for lambda = (25, 7, 2, 2, 2, 2, 2), delta = 14 (n = 3, r = 7): mult_per = 6 = a, proved over Q*  (12.6s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (25, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 42 vs 3*14
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 0, mult 6
- [x] claim: 0 <= nullity <= a
- [x] 14 recorded permanent_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 6 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17379 vs n_chi 17379, f(0) = 1703448158
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 0, nullity 0
- [x] conclusion: nullity_p([E; ev]) = 0 at p = 2147483629, so mult_permanent_pencil(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a); the row sampling/grouping of E can only lose rank, so the compressed certificate implies the full one
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_25_7_2_2_2_2_2_d14_n3_permanent_p2147483647_sparse_nullity.json`

*s73: nullity_p([E; ev_per]) = 0 at p = 2147483647 for lambda = (25, 7, 2, 2, 2, 2, 2), delta = 14 (n = 3, r = 7): mult_per = 6 = a, proved over Q*  (12.9s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (25, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 42 vs 3*14
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 0, mult 6
- [x] claim: 0 <= nullity <= a
- [x] 14 recorded permanent_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 6 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17379 vs n_chi 17379, f(0) = 258167334
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 0, nullity 0
- [x] conclusion: nullity_p([E; ev]) = 0 at p = 2147483647, so mult_permanent_pencil(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a); the row sampling/grouping of E can only lose rank, so the compressed certificate implies the full one
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

