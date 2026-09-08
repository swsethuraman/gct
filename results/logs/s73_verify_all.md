# Verifier report

46 certificate file(s); verifier tools/verify at 2026-09-08 05:27:27 UTC
PASS 46, FAIL 0, UNPARSEABLE 0, ERROR 0

## PASS — `results/certs/s73/s73_10_7_2_2_2_2_2_d9_n3_det_p2147483629_sparse_nullity.json`

*s73: nullity_p([E; ev_det]) = 0 at p = 2147483629 for lambda = (10, 7, 2, 2, 2, 2, 2), delta = 9 (n = 3, r = 7): mult_det = 2 = a, proved over Q*  (4.8s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (10, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 27 vs 3*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] claim: mult = a - nullity — a 2, nullity 0, mult 2
- [x] claim: 0 <= nullity <= a
- [x] 10 recorded det_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 2 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 11425 vs n_chi 11425, f(0) = 133709641
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 0, nullity 0
- [x] conclusion: nullity_p([E; ev]) = 0 at p = 2147483629, so mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a); the row sampling/grouping of E can only lose rank, so the compressed certificate implies the full one
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_10_7_2_2_2_2_2_d9_n3_det_p2147483647_sparse_nullity.json`

*s73: nullity_p([E; ev_det]) = 0 at p = 2147483647 for lambda = (10, 7, 2, 2, 2, 2, 2), delta = 9 (n = 3, r = 7): mult_det = 2 = a, proved over Q*  (4.3s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (10, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 27 vs 3*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] claim: mult = a - nullity — a 2, nullity 0, mult 2
- [x] claim: 0 <= nullity <= a
- [x] 10 recorded det_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 2 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 11425 vs n_chi 11425, f(0) = 657914641
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 0, nullity 0
- [x] conclusion: nullity_p([E; ev]) = 0 at p = 2147483647, so mult_det_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a); the row sampling/grouping of E can only lose rank, so the compressed certificate implies the full one
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_10_7_2_2_2_2_2_d9_n3_fullE_p2147483647_sparse_nullity.json`

*s73: nullity_p(E) = 2 = a at p = 2147483647 for lambda = (10, 7, 2, 2, 2, 2, 2), delta = 9 (n = 3, r = 7): the raising operators on V_chi have kernel of the plethysm dimension*  (4.4s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (10, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 27 vs 3*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] claim: mult = a - nullity — a 2, nullity 2, mult 0
- [x] claim: 0 <= nullity <= a
- [x] variety none: no evaluation rows (the kernel of E alone, nullity = a expected) — 0 points, nullity 2, a 2
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 11425 vs n_chi 11425, f(0) = 114495520
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 2, nullity 2
- [x] conclusion: nullity_p(E) = 2 = a at p = 2147483647: the 2 kernel vectors (an explicit basis of the highest-weight space mod p) are banked as an artefact by the producer and are NOT certified here (a mod-p basis of this size does not fit a certificate); the count is closed by the Berlekamp-Massey record above
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_10_7_2_2_2_2_2_d9_n3_permanent_p2147483629_sparse_nullity.json`

*s73: nullity_p([E; ev_per]) = 0 at p = 2147483629 for lambda = (10, 7, 2, 2, 2, 2, 2), delta = 9 (n = 3, r = 7): mult_per = 2 = a, proved over Q*  (4.3s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (10, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 27 vs 3*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] claim: mult = a - nullity — a 2, nullity 0, mult 2
- [x] claim: 0 <= nullity <= a
- [x] 10 recorded permanent_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 2 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 11425 vs n_chi 11425, f(0) = 314844569
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 0, nullity 0
- [x] conclusion: nullity_p([E; ev]) = 0 at p = 2147483629, so mult_permanent_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a); the row sampling/grouping of E can only lose rank, so the compressed certificate implies the full one
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_10_7_2_2_2_2_2_d9_n3_permanent_p2147483647_sparse_nullity.json`

*s73: nullity_p([E; ev_per]) = 0 at p = 2147483647 for lambda = (10, 7, 2, 2, 2, 2, 2), delta = 9 (n = 3, r = 7): mult_per = 2 = a, proved over Q*  (4.3s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (10, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 27 vs 3*9
- [x] cell: a recomputed (Weyl alternation) — recomputed 2, claimed 2
- [x] claim: mult = a - nullity — a 2, nullity 0, mult 2
- [x] claim: 0 <= nullity <= a
- [x] 10 recorded permanent_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 2 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 11425 vs n_chi 11425, f(0) = 1520593790
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 0, nullity 0
- [x] conclusion: nullity_p([E; ev]) = 0 at p = 2147483647, so mult_permanent_pencil(lambda, delta) = a = 2 over Q (rank_p <= rank_Q <= a); the row sampling/grouping of E can only lose rank, so the compressed certificate implies the full one
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_13_7_2_2_2_2_2_d10_n3_det_p2147483629_sparse_nullity.json`

*s73: nullity_p([E; ev_det]) = 0 at p = 2147483629 for lambda = (13, 7, 2, 2, 2, 2, 2), delta = 10 (n = 3, r = 7): mult_det = 4 = a, proved over Q*  (5.9s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (13, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 30 vs 3*10
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] claim: mult = a - nullity — a 4, nullity 0, mult 4
- [x] claim: 0 <= nullity <= a
- [x] 12 recorded det_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 4 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 14598 vs n_chi 14598, f(0) = 2037995495
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 0, nullity 0
- [x] conclusion: nullity_p([E; ev]) = 0 at p = 2147483629, so mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a); the row sampling/grouping of E can only lose rank, so the compressed certificate implies the full one
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_13_7_2_2_2_2_2_d10_n3_det_p2147483647_sparse_nullity.json`

*s73: nullity_p([E; ev_det]) = 0 at p = 2147483647 for lambda = (13, 7, 2, 2, 2, 2, 2), delta = 10 (n = 3, r = 7): mult_det = 4 = a, proved over Q*  (5.8s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (13, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 30 vs 3*10
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] claim: mult = a - nullity — a 4, nullity 0, mult 4
- [x] claim: 0 <= nullity <= a
- [x] 12 recorded det_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 4 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 14598 vs n_chi 14598, f(0) = 426190755
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 0, nullity 0
- [x] conclusion: nullity_p([E; ev]) = 0 at p = 2147483647, so mult_det_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a); the row sampling/grouping of E can only lose rank, so the compressed certificate implies the full one
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_13_7_2_2_2_2_2_d10_n3_fullE_p2147483647_sparse_nullity.json`

*s73: nullity_p(E) = 4 = a at p = 2147483647 for lambda = (13, 7, 2, 2, 2, 2, 2), delta = 10 (n = 3, r = 7): the raising operators on V_chi have kernel of the plethysm dimension*  (5.8s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (13, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 30 vs 3*10
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] claim: mult = a - nullity — a 4, nullity 4, mult 0
- [x] claim: 0 <= nullity <= a
- [x] variety none: no evaluation rows (the kernel of E alone, nullity = a expected) — 0 points, nullity 4, a 4
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 14598 vs n_chi 14598, f(0) = 1436579530
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 4, nullity 4
- [x] conclusion: nullity_p(E) = 4 = a at p = 2147483647: the 4 kernel vectors (an explicit basis of the highest-weight space mod p) are banked as an artefact by the producer and are NOT certified here (a mod-p basis of this size does not fit a certificate); the count is closed by the Berlekamp-Massey record above
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_13_7_2_2_2_2_2_d10_n3_permanent_p2147483629_sparse_nullity.json`

*s73: nullity_p([E; ev_per]) = 0 at p = 2147483629 for lambda = (13, 7, 2, 2, 2, 2, 2), delta = 10 (n = 3, r = 7): mult_per = 4 = a, proved over Q*  (5.7s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (13, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 30 vs 3*10
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] claim: mult = a - nullity — a 4, nullity 0, mult 4
- [x] claim: 0 <= nullity <= a
- [x] 12 recorded permanent_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 4 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 14598 vs n_chi 14598, f(0) = 931638220
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 0, nullity 0
- [x] conclusion: nullity_p([E; ev]) = 0 at p = 2147483629, so mult_permanent_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a); the row sampling/grouping of E can only lose rank, so the compressed certificate implies the full one
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_13_7_2_2_2_2_2_d10_n3_permanent_p2147483647_sparse_nullity.json`

*s73: nullity_p([E; ev_per]) = 0 at p = 2147483647 for lambda = (13, 7, 2, 2, 2, 2, 2), delta = 10 (n = 3, r = 7): mult_per = 4 = a, proved over Q*  (5.6s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (13, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 30 vs 3*10
- [x] cell: a recomputed (Weyl alternation) — recomputed 4, claimed 4
- [x] claim: mult = a - nullity — a 4, nullity 0, mult 4
- [x] claim: 0 <= nullity <= a
- [x] 12 recorded permanent_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 4 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 14598 vs n_chi 14598, f(0) = 149152229
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 0, nullity 0
- [x] conclusion: nullity_p([E; ev]) = 0 at p = 2147483647, so mult_permanent_pencil(lambda, delta) = a = 4 over Q (rank_p <= rank_Q <= a); the row sampling/grouping of E can only lose rank, so the compressed certificate implies the full one
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_16_7_2_2_2_2_2_d11_n3_det_p2147483629_sparse_nullity.json`

*s73: nullity_p([E; ev_det]) = 0 at p = 2147483629 for lambda = (16, 7, 2, 2, 2, 2, 2), delta = 11 (n = 3, r = 7): mult_det = 5 = a, proved over Q*  (7.2s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (16, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 33 vs 3*11
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] claim: mult = a - nullity — a 5, nullity 0, mult 5
- [x] claim: 0 <= nullity <= a
- [x] 13 recorded det_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 5 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 16318 vs n_chi 16318, f(0) = 2051157413
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 0, nullity 0
- [x] conclusion: nullity_p([E; ev]) = 0 at p = 2147483629, so mult_det_pencil(lambda, delta) = a = 5 over Q (rank_p <= rank_Q <= a); the row sampling/grouping of E can only lose rank, so the compressed certificate implies the full one
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_16_7_2_2_2_2_2_d11_n3_det_p2147483647_sparse_nullity.json`

*s73: nullity_p([E; ev_det]) = 0 at p = 2147483647 for lambda = (16, 7, 2, 2, 2, 2, 2), delta = 11 (n = 3, r = 7): mult_det = 5 = a, proved over Q*  (7.2s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (16, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 33 vs 3*11
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] claim: mult = a - nullity — a 5, nullity 0, mult 5
- [x] claim: 0 <= nullity <= a
- [x] 13 recorded det_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 5 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 16318 vs n_chi 16318, f(0) = 910563636
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 0, nullity 0
- [x] conclusion: nullity_p([E; ev]) = 0 at p = 2147483647, so mult_det_pencil(lambda, delta) = a = 5 over Q (rank_p <= rank_Q <= a); the row sampling/grouping of E can only lose rank, so the compressed certificate implies the full one
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_16_7_2_2_2_2_2_d11_n3_fullE_p2147483647_sparse_nullity.json`

*s73: nullity_p(E) = 5 = a at p = 2147483647 for lambda = (16, 7, 2, 2, 2, 2, 2), delta = 11 (n = 3, r = 7): the raising operators on V_chi have kernel of the plethysm dimension*  (7.1s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (16, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 33 vs 3*11
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] claim: mult = a - nullity — a 5, nullity 5, mult 0
- [x] claim: 0 <= nullity <= a
- [x] variety none: no evaluation rows (the kernel of E alone, nullity = a expected) — 0 points, nullity 5, a 5
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 16318 vs n_chi 16318, f(0) = 138488864
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 5, nullity 5
- [x] conclusion: nullity_p(E) = 5 = a at p = 2147483647: the 5 kernel vectors (an explicit basis of the highest-weight space mod p) are banked as an artefact by the producer and are NOT certified here (a mod-p basis of this size does not fit a certificate); the count is closed by the Berlekamp-Massey record above
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_16_7_2_2_2_2_2_d11_n3_permanent_p2147483629_sparse_nullity.json`

*s73: nullity_p([E; ev_per]) = 0 at p = 2147483629 for lambda = (16, 7, 2, 2, 2, 2, 2), delta = 11 (n = 3, r = 7): mult_per = 5 = a, proved over Q*  (7.2s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (16, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 33 vs 3*11
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] claim: mult = a - nullity — a 5, nullity 0, mult 5
- [x] claim: 0 <= nullity <= a
- [x] 13 recorded permanent_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 5 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 16318 vs n_chi 16318, f(0) = 707519748
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 0, nullity 0
- [x] conclusion: nullity_p([E; ev]) = 0 at p = 2147483629, so mult_permanent_pencil(lambda, delta) = a = 5 over Q (rank_p <= rank_Q <= a); the row sampling/grouping of E can only lose rank, so the compressed certificate implies the full one
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_16_7_2_2_2_2_2_d11_n3_permanent_p2147483647_sparse_nullity.json`

*s73: nullity_p([E; ev_per]) = 0 at p = 2147483647 for lambda = (16, 7, 2, 2, 2, 2, 2), delta = 11 (n = 3, r = 7): mult_per = 5 = a, proved over Q*  (7.1s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (16, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 33 vs 3*11
- [x] cell: a recomputed (Weyl alternation) — recomputed 5, claimed 5
- [x] claim: mult = a - nullity — a 5, nullity 0, mult 5
- [x] claim: 0 <= nullity <= a
- [x] 13 recorded permanent_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 5 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 16318 vs n_chi 16318, f(0) = 1088868352
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 0, nullity 0
- [x] conclusion: nullity_p([E; ev]) = 0 at p = 2147483647, so mult_permanent_pencil(lambda, delta) = a = 5 over Q (rank_p <= rank_Q <= a); the row sampling/grouping of E can only lose rank, so the compressed certificate implies the full one
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_19_7_2_2_2_2_2_d12_n3_det_kernel_vec0_int.json.gz`

*s73: integer highest-weight vector of weight (19, 7, 2, 2, 2, 2, 2) (delta=12, n=3, r=7) in the kernel of the det_pencil evaluation pairing: an element of I(D_7)^HWV not vanishing on P_7*  (61.0s)

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

*s73: nullity_p([E; ev_det]) = 1 at p = 2147483629 for lambda = (19, 7, 2, 2, 2, 2, 2), delta = 12 (n = 3, r = 7): mult_det = 5 (>= 5 proved, = 5 measured)*  (9.3s)

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

*s73: nullity_p([E; ev_det]) = 1 at p = 2147483647 for lambda = (19, 7, 2, 2, 2, 2, 2), delta = 12 (n = 3, r = 7): mult_det = 5 (>= 5 proved, = 5 measured)*  (9.1s)

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

*s73: nullity_p(E) = 6 = a at p = 2147483647 for lambda = (19, 7, 2, 2, 2, 2, 2), delta = 12 (n = 3, r = 7): the raising operators on V_chi have kernel of the plethysm dimension*  (9.2s)

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

*s73: nullity_p([E; ev_per]) = 0 at p = 2147483629 for lambda = (19, 7, 2, 2, 2, 2, 2), delta = 12 (n = 3, r = 7): mult_per = 6 = a, proved over Q*  (8.8s)

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

*s73: nullity_p([E; ev_per]) = 0 at p = 2147483647 for lambda = (19, 7, 2, 2, 2, 2, 2), delta = 12 (n = 3, r = 7): mult_per = 6 = a, proved over Q*  (8.7s)

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

## PASS — `results/certs/s73/s73_19_7_2_2_2_2_2_second_d12_n3_det_kernel_vec0_int.json.gz`

*s73: integer highest-weight vector of weight (19, 7, 2, 2, 2, 2, 2) (delta=12, n=3, r=7) in the kernel of the det_pencil evaluation pairing: an element of I(D_7)^HWV not vanishing on P_7*  (68.2s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (19, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 3*12
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] vectors parsed — 1 vector(s), supports [240510], integer coefficients
- [x] vector 0: shape, degree, canonical terms, weight = lambda
- [x] vector 0: annihilated by every E_(i,i+1) over Z
- [x] vectors linearly independent — rank 1 over Q (lower bound from primes [1, 1]; equals the count so exact)
- [x] vanishes at 26 recorded point(s) [det_pencil]
- [x] evaluation at 26 recorded point(s) [permanent_pencil] has full row rank — rank 1 of 1
- [x] vanishes at 6 fresh det_pencil points (seed 20260908)
- [x] evaluation at 6 fresh permanent_pencil points (seed 20260908) has full row rank — rank 1 of 1
- [x] evaluation at 6 fresh generic points (seed 20260908) has full row rank — rank 1 of 1

## PASS — `results/certs/s73/s73_19_7_2_2_2_2_2_second_d12_n3_det_p2147483629_sparse_nullity.json`

*s73: nullity_p([E; ev_det]) = 1 at p = 2147483629 for lambda = (19, 7, 2, 2, 2, 2, 2), delta = 12 (n = 3, r = 7): mult_det = 5 (>= 5 proved, = 5 measured)*  (9.1s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (19, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 3*12
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 1, mult 5
- [x] claim: 0 <= nullity <= a
- [x] 26 recorded det_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 6 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17047 vs n_chi 17047, f(0) = 1095758389
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 1, nullity 1
- [x] nullity 1: 1 companion hwv certificate(s) named and present — named ['s73_19_7_2_2_2_2_2_second_d12_n3_det_kernel_vec0_int.json.gz'], present [True]
- [x] conclusion: nullity_p = 1 at p = 2147483629: mult >= 5 proved; = 5 measured, carried to Q by the companion hwv certificate(s) (integer vectors annihilated by the raising operators over Z, vanishing at fresh det_pencil points)
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_19_7_2_2_2_2_2_second_d12_n3_det_p2147483647_sparse_nullity.json`

*s73: nullity_p([E; ev_det]) = 1 at p = 2147483647 for lambda = (19, 7, 2, 2, 2, 2, 2), delta = 12 (n = 3, r = 7): mult_det = 5 (>= 5 proved, = 5 measured)*  (8.8s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (19, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 3*12
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 1, mult 5
- [x] claim: 0 <= nullity <= a
- [x] 26 recorded det_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 6 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17047 vs n_chi 17047, f(0) = 1198547695
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 1, nullity 1
- [x] nullity 1: 1 companion hwv certificate(s) named and present — named ['s73_19_7_2_2_2_2_2_second_d12_n3_det_kernel_vec0_int.json.gz'], present [True]
- [x] conclusion: nullity_p = 1 at p = 2147483647: mult >= 5 proved; = 5 measured, carried to Q by the companion hwv certificate(s) (integer vectors annihilated by the raising operators over Z, vanishing at fresh det_pencil points)
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_19_7_2_2_2_2_2_second_d12_n3_permanent_p2147483629_sparse_nullity.json`

*s73: nullity_p([E; ev_per]) = 0 at p = 2147483629 for lambda = (19, 7, 2, 2, 2, 2, 2), delta = 12 (n = 3, r = 7): mult_per = 6 = a, proved over Q*  (8.8s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (19, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 3*12
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 0, mult 6
- [x] claim: 0 <= nullity <= a
- [x] 26 recorded permanent_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 6 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17047 vs n_chi 17047, f(0) = 219364277
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 0, nullity 0
- [x] conclusion: nullity_p([E; ev]) = 0 at p = 2147483629, so mult_permanent_pencil(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a); the row sampling/grouping of E can only lose rank, so the compressed certificate implies the full one
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_19_7_2_2_2_2_2_second_d12_n3_permanent_p2147483647_sparse_nullity.json`

*s73: nullity_p([E; ev_per]) = 0 at p = 2147483647 for lambda = (19, 7, 2, 2, 2, 2, 2), delta = 12 (n = 3, r = 7): mult_per = 6 = a, proved over Q*  (8.8s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (19, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 36 vs 3*12
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 0, mult 6
- [x] claim: 0 <= nullity <= a
- [x] 26 recorded permanent_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 6 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17047 vs n_chi 17047, f(0) = 1425553630
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 0, nullity 0
- [x] conclusion: nullity_p([E; ev]) = 0 at p = 2147483647, so mult_permanent_pencil(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a); the row sampling/grouping of E can only lose rank, so the compressed certificate implies the full one
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_22_7_2_2_2_2_2_d13_n3_det_kernel_vec0_int.json.gz`

*s73: integer highest-weight vector of weight (22, 7, 2, 2, 2, 2, 2) (delta=13, n=3, r=7) in the kernel of the det_pencil evaluation pairing: an element of I(D_7)^HWV not vanishing on P_7*  (64.6s)

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

*s73: nullity_p([E; ev_det]) = 1 at p = 2147483629 for lambda = (22, 7, 2, 2, 2, 2, 2), delta = 13 (n = 3, r = 7): mult_det = 5 (>= 5 proved, = 5 measured)*  (11.3s)

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

*s73: nullity_p([E; ev_det]) = 1 at p = 2147483647 for lambda = (22, 7, 2, 2, 2, 2, 2), delta = 13 (n = 3, r = 7): mult_det = 5 (>= 5 proved, = 5 measured)*  (11.3s)

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

*s73: nullity_p([E; ev_per]) = 0 at p = 2147483629 for lambda = (22, 7, 2, 2, 2, 2, 2), delta = 13 (n = 3, r = 7): mult_per = 6 = a, proved over Q*  (11.5s)

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

*s73: nullity_p([E; ev_per]) = 0 at p = 2147483647 for lambda = (22, 7, 2, 2, 2, 2, 2), delta = 13 (n = 3, r = 7): mult_per = 6 = a, proved over Q*  (11.6s)

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

*s73: integer highest-weight vector of weight (25, 7, 2, 2, 2, 2, 2) (delta=14, n=3, r=7) in the kernel of the det_pencil evaluation pairing: an element of I(D_7)^HWV not vanishing on P_7*  (71.6s)

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

*s73: nullity_p([E; ev_det]) = 1 at p = 2147483647 for lambda = (25, 7, 2, 2, 2, 2, 2), delta = 14 (n = 3, r = 7): mult_det = 5 (>= 5 proved, = 5 measured)*  (13.6s)

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

*s73: nullity_p([E; ev_per]) = 0 at p = 2147483629 for lambda = (25, 7, 2, 2, 2, 2, 2), delta = 14 (n = 3, r = 7): mult_per = 6 = a, proved over Q*  (13.6s)

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

*s73: nullity_p([E; ev_per]) = 0 at p = 2147483647 for lambda = (25, 7, 2, 2, 2, 2, 2), delta = 14 (n = 3, r = 7): mult_per = 6 = a, proved over Q*  (13.2s)

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

## PASS — `results/certs/s73/s73_28_7_2_2_2_2_2_d15_n3_det_kernel_vec0_int.json.gz`

*s73: integer highest-weight vector of weight (28, 7, 2, 2, 2, 2, 2) (delta=15, n=3, r=7) in the kernel of the det_pencil evaluation pairing: an element of I(D_7)^HWV not vanishing on P_7*  (76.3s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (28, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 45 vs 3*15
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

## PASS — `results/certs/s73/s73_28_7_2_2_2_2_2_d15_n3_det_p2147483629_sparse_nullity.json`

*s73: nullity_p([E; ev_det]) = 1 at p = 2147483629 for lambda = (28, 7, 2, 2, 2, 2, 2), delta = 15 (n = 3, r = 7): mult_det = 5 (>= 5 proved, = 5 measured)*  (15.5s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (28, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 45 vs 3*15
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 1, mult 5
- [x] claim: 0 <= nullity <= a
- [x] 14 recorded det_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 6 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17399 vs n_chi 17399, f(0) = 582387965
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 1, nullity 1
- [x] nullity 1: 1 companion hwv certificate(s) named and present — named ['s73_28_7_2_2_2_2_2_d15_n3_det_kernel_vec0_int.json.gz'], present [True]
- [x] conclusion: nullity_p = 1 at p = 2147483629: mult >= 5 proved; = 5 measured, carried to Q by the companion hwv certificate(s) (integer vectors annihilated by the raising operators over Z, vanishing at fresh det_pencil points)
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_28_7_2_2_2_2_2_d15_n3_det_p2147483647_sparse_nullity.json`

*s73: nullity_p([E; ev_det]) = 1 at p = 2147483647 for lambda = (28, 7, 2, 2, 2, 2, 2), delta = 15 (n = 3, r = 7): mult_det = 5 (>= 5 proved, = 5 measured)*  (15.1s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (28, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 45 vs 3*15
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 1, mult 5
- [x] claim: 0 <= nullity <= a
- [x] 14 recorded det_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 6 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17399 vs n_chi 17399, f(0) = 1912379280
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 1, nullity 1
- [x] nullity 1: 1 companion hwv certificate(s) named and present — named ['s73_28_7_2_2_2_2_2_d15_n3_det_kernel_vec0_int.json.gz'], present [True]
- [x] conclusion: nullity_p = 1 at p = 2147483647: mult >= 5 proved; = 5 measured, carried to Q by the companion hwv certificate(s) (integer vectors annihilated by the raising operators over Z, vanishing at fresh det_pencil points)
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_28_7_2_2_2_2_2_d15_n3_permanent_p2147483629_sparse_nullity.json`

*s73: nullity_p([E; ev_per]) = 0 at p = 2147483629 for lambda = (28, 7, 2, 2, 2, 2, 2), delta = 15 (n = 3, r = 7): mult_per = 6 = a, proved over Q*  (15.7s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (28, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 45 vs 3*15
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 0, mult 6
- [x] claim: 0 <= nullity <= a
- [x] 14 recorded permanent_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 6 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17399 vs n_chi 17399, f(0) = 1749652934
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 0, nullity 0
- [x] conclusion: nullity_p([E; ev]) = 0 at p = 2147483629, so mult_permanent_pencil(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a); the row sampling/grouping of E can only lose rank, so the compressed certificate implies the full one
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_28_7_2_2_2_2_2_d15_n3_permanent_p2147483647_sparse_nullity.json`

*s73: nullity_p([E; ev_per]) = 0 at p = 2147483647 for lambda = (28, 7, 2, 2, 2, 2, 2), delta = 15 (n = 3, r = 7): mult_per = 6 = a, proved over Q*  (15.8s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (28, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 45 vs 3*15
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 0, mult 6
- [x] claim: 0 <= nullity <= a
- [x] 14 recorded permanent_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 6 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17399 vs n_chi 17399, f(0) = 1426778315
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 0, nullity 0
- [x] conclusion: nullity_p([E; ev]) = 0 at p = 2147483647, so mult_permanent_pencil(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a); the row sampling/grouping of E can only lose rank, so the compressed certificate implies the full one
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_31_7_2_2_2_2_2_d16_n3_det_kernel_vec0_int.json.gz`

*s73: integer highest-weight vector of weight (31, 7, 2, 2, 2, 2, 2) (delta=16, n=3, r=7) in the kernel of the det_pencil evaluation pairing: an element of I(D_7)^HWV not vanishing on P_7*  (83.9s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (31, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 48 vs 3*16
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

## PASS — `results/certs/s73/s73_31_7_2_2_2_2_2_d16_n3_det_p2147483629_sparse_nullity.json`

*s73: nullity_p([E; ev_det]) = 1 at p = 2147483629 for lambda = (31, 7, 2, 2, 2, 2, 2), delta = 16 (n = 3, r = 7): mult_det = 5 (>= 5 proved, = 5 measured)*  (17.6s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (31, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 48 vs 3*16
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 1, mult 5
- [x] claim: 0 <= nullity <= a
- [x] 14 recorded det_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 6 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17403 vs n_chi 17403, f(0) = 1988851195
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 1, nullity 1
- [x] nullity 1: 1 companion hwv certificate(s) named and present — named ['s73_31_7_2_2_2_2_2_d16_n3_det_kernel_vec0_int.json.gz'], present [True]
- [x] conclusion: nullity_p = 1 at p = 2147483629: mult >= 5 proved; = 5 measured, carried to Q by the companion hwv certificate(s) (integer vectors annihilated by the raising operators over Z, vanishing at fresh det_pencil points)
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_31_7_2_2_2_2_2_d16_n3_det_p2147483647_sparse_nullity.json`

*s73: nullity_p([E; ev_det]) = 1 at p = 2147483647 for lambda = (31, 7, 2, 2, 2, 2, 2), delta = 16 (n = 3, r = 7): mult_det = 5 (>= 5 proved, = 5 measured)*  (17.0s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (31, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 48 vs 3*16
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 1, mult 5
- [x] claim: 0 <= nullity <= a
- [x] 14 recorded det_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 6 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17403 vs n_chi 17403, f(0) = 2084865851
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 1, nullity 1
- [x] nullity 1: 1 companion hwv certificate(s) named and present — named ['s73_31_7_2_2_2_2_2_d16_n3_det_kernel_vec0_int.json.gz'], present [True]
- [x] conclusion: nullity_p = 1 at p = 2147483647: mult >= 5 proved; = 5 measured, carried to Q by the companion hwv certificate(s) (integer vectors annihilated by the raising operators over Z, vanishing at fresh det_pencil points)
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_31_7_2_2_2_2_2_d16_n3_permanent_p2147483629_sparse_nullity.json`

*s73: nullity_p([E; ev_per]) = 0 at p = 2147483629 for lambda = (31, 7, 2, 2, 2, 2, 2), delta = 16 (n = 3, r = 7): mult_per = 6 = a, proved over Q*  (16.9s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (31, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 48 vs 3*16
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 0, mult 6
- [x] claim: 0 <= nullity <= a
- [x] 14 recorded permanent_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 6 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17403 vs n_chi 17403, f(0) = 201494028
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 0, nullity 0
- [x] conclusion: nullity_p([E; ev]) = 0 at p = 2147483629, so mult_permanent_pencil(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a); the row sampling/grouping of E can only lose rank, so the compressed certificate implies the full one
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

## PASS — `results/certs/s73/s73_31_7_2_2_2_2_2_d16_n3_permanent_p2147483647_sparse_nullity.json`

*s73: nullity_p([E; ev_per]) = 0 at p = 2147483647 for lambda = (31, 7, 2, 2, 2, 2, 2), delta = 16 (n = 3, r = 7): mult_per = 6 = a, proved over Q*  (17.6s)

- [x] cell: n in {3, 4} — n = 3
- [x] cell: length(lambda) = r — lambda (31, 7, 2, 2, 2, 2, 2), r 7
- [x] cell: lambda weakly decreasing
- [x] cell: |lambda| = n*delta — 48 vs 3*16
- [x] cell: a recomputed (Weyl alternation) — recomputed 6, claimed 6
- [x] claim: mult = a - nullity — a 6, nullity 0, mult 6
- [x] claim: 0 <= nullity <= a
- [x] 14 recorded permanent_pencil points rebuilt from substitution data (each a nonzero form of degree 3) — 0 zero forms; need at least a = 6 points
- [x] reduction sizes recorded (N_S, n_chi, |Stab|, rows and nnz of E)
- [x] closing Berlekamp-Massey record: degree = n_chi and f(0) != 0 (Lemma 4: [E_c; ev; R] nonsingular) — degree 17403 vs n_chi 17403, f(0) = 644468686
- [x] closing run pinned k_extra = nullity random dense rows (so nullity_p <= k) — k_extra 0, nullity 0
- [x] conclusion: nullity_p([E; ev]) = 0 at p = 2147483647, so mult_permanent_pencil(lambda, delta) = a = 6 over Q (rank_p <= rank_Q <= a); the row sampling/grouping of E can only lose rank, so the compressed certificate implies the full one
- [x] NOT re-done here: the chi-isotypic build and the Wiedemann sequence (re-runnable from the recorded seeds: analysis/wk11_s73_cell.py)

