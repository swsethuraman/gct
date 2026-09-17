# b_L decomposition tables (generated from results/b_L_branching.json)

Cell d = 5, lambda = (4^5). L = grading-preserving Levi. Invariant condition: GL_3 type det^10, (alpha,beta,c) = (5,5,15).

## Formulation I: by Littlewood-Richardson constituent (mu, kappa, tau)

| #v | mu | kappa | tau | c^lambda | dim S_mu(C^4) | dim S_kappa(C^3) | dim S_tau(C^9) | L-invariants | contribution |
|---|---|---|---|---|---|---|---|---|---|
| 11 | (4, 1) | (4, 4, 3) | (4,) | 1 | 84 | 3 | 495 | 6 | 6 |
| 11 | (4, 1) | (4, 4, 3) | (3, 1) | 1 | 84 | 3 | 990 | 19 | 19 |
| 11 | (3, 2) | (4, 4, 3) | (3, 1) | 1 | 60 | 3 | 990 | 13 | 13 |
| 11 | (3, 2) | (4, 4, 3) | (2, 2) | 1 | 60 | 3 | 540 | 7 | 7 |
| 11 | (3, 2) | (4, 4, 3) | (2, 1, 1) | 1 | 60 | 3 | 630 | 11 | 11 |
| 11 | (3, 1, 1) | (4, 4, 3) | (3, 1) | 1 | 36 | 3 | 990 | 10 | 10 |
| 11 | (2, 2, 1) | (4, 4, 3) | (2, 2) | 1 | 20 | 3 | 540 | 4 | 4 |
| 12 | (4, 1) | (4, 4, 4) | (3,) | 1 | 84 | 1 | 165 | 2 | 2 |
| 12 | (3, 2) | (4, 4, 4) | (2, 1) | 1 | 60 | 1 | 240 | 2 | 2 |

Totals: b_L(11) = 70, b_L(12) = 4, b_L = 74.

## Formulation II: by adapted multidegree (#a, #r, #v, #c, #Sigma) (Kostka weight count, S_3 alternant)

| #v | #a | #r | #c | #Sigma | dim of the (10,10,10) weight space | L-invariants |
|---|---|---|---|---|---|---|
| 11 | 1 | 4 | 4 | 0 | 396 | 7 |
| 11 | 2 | 3 | 3 | 1 | 1845 | 31 |
| 11 | 3 | 2 | 2 | 2 | 1812 | 28 |
| 11 | 4 | 1 | 1 | 3 | 318 | 4 |
| 12 | 2 | 3 | 3 | 0 | 33 | 1 |
| 12 | 3 | 2 | 2 | 1 | 66 | 2 |
| 12 | 4 | 1 | 1 | 2 | 18 | 1 |

Totals: b_L(11) = 70, b_L(12) = 4, b_L = 74. Agreement with Formulation I: True.

S0-slice part (#Sigma = 0): 7 + 1 = 8 invariants.

## Controls

- `S21xS21_contains_S222_expect_1`: `1`
- `S2xS2xS2_contains_S222_expect_1`: `1`
- `dim_S21_C3_expect_8`: `8`
- `lr_alt_444_44_to_4^5_expect_1`: `1`
- `lr_alt_444_431_to_4^5_expect_0`: `0`
- `lr_comb_444_44_to_4^5_expect_1`: `1`
- `lr_comb_222_21_21_expect_1`: `1`
- `small_identity_S22_C6`: `{"sum": 105, "expect": 105, "passed": true}`
- `graded_identity`: `{"11": {"kappas": [[4, 4, 3]], "lhs_sum": 10930920, "rhs_coefficient_u_n": 10930920, "triples": 40, "passed": true}, "12": {"kappas": [[4, 4, 4]], "lhs_sum": 496860, "rhs_coefficient_u_n": 496860, "triples": 15, "passed": true}}`
- `kostka_21_111_expect_2`: `2`
- `kostka_lam_lam_expect_1`: `1`
- `SYT_count_hook_formula`: `1662804`
- `kostka_lam_1^20`: `1662804`
- `kostka_SYT_passed`: `true`

Stage times (s): {"small_controls": 0.14, "graded_identity": 13.41, "formulation_I": 14.34, "kostka_controls": 14.34, "done": 14.39}
