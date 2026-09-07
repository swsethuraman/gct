# Session 62 — cost curve

Three scales, kept apart (an earlier draft conflated them; corrected after the adversarial review):

- **`n_lam`** — the weight-space dimension (number of monomials `O`), = s57's `N_S`.
- **`|S|`** — the REDUCED-ROUTE deciding number (integrator note 3): the support of the
  highest-weight vectors in the weight-space / orbit-sum basis, `|S| <= n_lam`. The reduced
  block `A = C_S^T beta_S C_S` is a quadratic form over these, cost `~ a|S|^2 + a^2|S|`.
- **`|H_{4,delta}|`** — the whole Foulkes module; the ENUMERATION route costs `|H| * n_lam`
  per cell, and `Sum_{O in supp}|O|` (= `|H|` when the HWV is dense) is its raw support.


## Measured — `|S|`, `n_lam`, and the enumeration pass


| delta | lambda | a | n_lam | \|S\| (reduced) | \|S\|/n_lam | enum raw (Sum\|O\|) | pass |
|---|---|---|---|---|---|---|---|
| 2 | (8,) | 1 | 1 | 1 | 1.00 | 35 | 0.0 s |
| 2 | (6, 2) | 1 | 2 | 2 | 1.00 | 35 | 0.0 s |
| 2 | (4, 4) | 1 | 3 | 3 | 1.00 | 35 | 0.0 s |
| 3 | (12,) | 1 | 1 | 1 | 1.00 | 5,775 | 0.0 s |
| 3 | (10, 2) | 1 | 2 | 2 | 1.00 | 5,775 | 0.0 s |
| 3 | (9, 3) | 1 | 3 | 3 | 1.00 | 5,775 | 0.0 s |
| 3 | (8, 4) | 1 | 4 | 3 | 0.75 | 2,415 | 0.0 s |
| 3 | (8, 2, 2) | 1 | 8 | 5 | 0.62 | 4,620 | 0.0 s |
| 3 | (7, 4, 1) | 1 | 8 | 6 | 0.75 | 5,600 | 0.0 s |
| 3 | (6, 6) | 1 | 5 | 5 | 1.00 | 5,775 | 0.0 s |
| 3 | (6, 4, 2) | 1 | 15 | 15 | 1.00 | 5,775 | 0.0 s |
| 3 | (4, 4, 4) | 1 | 23 | 23 | 1.00 | 5,775 | 0.0 s |
| 4 | (16,) | 1 | 1 | 1 | 1.00 | 2,627,625 | 0.0 s |
| 4 | (14, 2) | 1 | 2 | 2 | 1.00 | 2,627,625 | 0.0 s |
| 4 | (13, 3) | 1 | 3 | 3 | 1.00 | 2,627,625 | 0.0 s |
| 4 | (12, 4) | 2 | 5 | 5 | 1.00 | 2,627,625 | 0.0 s |
| 4 | (12, 2, 2) | 1 | 9 | 5 | 0.56 | 1,975,050 | 0.0 s |
| 4 | (11, 4, 1) | 1 | 10 | 6 | 0.60 | 1,674,750 | 0.0 s |
| 4 | (11, 3, 2) | 1 | 14 | 11 | 0.79 | 2,182,950 | 0.0 s |
| 4 | (10, 6) | 2 | 7 | 7 | 1.00 | 2,627,625 | 0.0 s |
| 4 | (10, 5, 1) | 1 | 13 | 11 | 0.85 | 2,312,625 | 0.0 s |
| 4 | (10, 4, 2) | 2 | 22 | 22 | 1.00 | 2,627,625 | 0.0 s |
| 4 | (10, 2, 2, 2) | 1 | 55 | 17 | 0.31 | 1,417,500 | 0.0 s |
| 4 | (9, 6, 1) | 1 | 16 | 16 | 1.00 | 2,627,625 | 0.0 s |
| 4 | (9, 5, 2) | 1 | 27 | 24 | 0.89 | 2,300,025 | 0.0 s |
| 4 | (9, 4, 3) | 1 | 35 | 35 | 1.00 | 2,627,625 | 0.0 s |
| 4 | (9, 4, 2, 1) | 1 | 63 | 23 | 0.37 | 1,527,120 | 0.0 s |
| 4 | (8, 8) | 1 | 8 | 6 | 0.75 | 2,157,225 | 0.0 s |
| 4 | (8, 6, 2) | 2 | 33 | 29 | 0.88 | 2,392,425 | 0.0 s |
| 4 | (8, 5, 2, 1) | 1 | 80 | 44 | 0.55 | 1,866,900 | 0.0 s |
| 4 | (8, 4, 4) | 2 | 51 | 42 | 0.82 | 2,392,425 | 0.0 s |
| 4 | (8, 4, 2, 2) | 1 | 136 | 86 | 0.63 | 1,987,860 | 0.0 s |
| 4 | (7, 7, 1, 1) | 1 | 47 | 24 | 0.51 | 1,075,550 | 0.0 s |
| 4 | (7, 6, 3) | 1 | 49 | 41 | 0.84 | 2,469,600 | 0.0 s |
| 4 | (7, 5, 3, 1) | 1 | 127 | 100 | 0.79 | 2,315,950 | 0.0 s |
| 4 | (7, 4, 4, 1) | 1 | 145 | 118 | 0.81 | 1,822,800 | 0.0 s |
| 4 | (6, 6, 4) | 1 | 66 | 66 | 1.00 | 2,627,625 | 0.0 s |
| 4 | (6, 6, 2, 2) | 1 | 180 | 125 | 0.69 | 2,056,650 | 0.0 s |
| 4 | (6, 4, 4, 2) | 1 | 288 | 288 | 1.00 | 2,627,625 | 0.0 s |
| 4 | (4, 4, 4, 4) | 1 | 465 | 465 | 1.00 | 2,627,625 | 0.0 s |

`|S| = n_lam` (the HWVs reach the whole weight space) at **11 of 28** `δ = 4` cells — the rectangular and near-rectangular ones; at the skewed cells `|S| < n_lam` but stays the same order. So the reduced-route cost is set by `n_lam`, the weight-space dimension.


Measured enumeration rate: **173.7 ns per element of `H` per representative** (`δ = 4`, 0.456 s/rep over 2,627,625).


## The enumeration wall — `|H_{4,delta}|` and the projected single-pass time


| delta | \|H_{4,delta}\| | one pass (projected) |
|---|---|---|
| 2 | 35 | 0.0 s |
| 3 | 5,775 | 0.0 s |
| 4 | 2,627,625 | 0.5 s |
| 5 | 2,546,168,625 | 7.4 min |
| 6 | 4,509,264,634,875 | 9.06 d |
| 7 | 13,189,599,057,009,375 | 2.65e+04 d |
| 8 | 59,287,247,761,257,140,625 | 1.19e+08 d |
| 9 | 388,035,036,597,427,985,390,625 | 7.8e+11 d |
| 10 | 3,546,252,199,463,894,358,484,921,875 | 7.13e+15 d |
| 11 | 43,764,298,393,583,920,278,062,420,859,375 | 8.8e+19 d |
| 12 | 709,638,098,451,963,267,308,782,154,234,765,625 | 1.43e+24 d |
| 13 | 14,778,213,400,262,135,041,705,388,361,938,994,140,625 | 2.97e+28 d |
| 14 | 387,706,428,555,877,112,819,140,863,675,469,511,279,296,875 | 7.79e+32 d |
| 15 | 12,603,948,285,923,009,060,637,450,337,225,838,342,178,662,109,375 | 2.53e+37 d |
| 16 | 500,515,390,382,288,612,806,973,790,341,575,266,406,256,851,025,390,625 | 1.01e+42 d |
| 17 | 23,977,189,776,263,535,996,518,079,426,313,163,137,191,734,448,371,337,890,625 | 4.82e+46 d |
| 18 | 1,370,416,281,662,342,399,880,990,829,610,928,839,106,193,582,396,663,817,138,671,875 | 2.75e+51 d |
| 19 | 92,537,359,419,249,670,551,963,905,769,477,969,860,645,721,651,334,724,252,288,818,359,375 | 1.86e+56 d |
| 20 | 7,317,761,845,514,844,697,578,753,704,344,548,378,610,003,022,465,898,659,146,747,467,041,015,625 | 1.47e+61 d |
| 21 | 672,363,276,127,749,445,658,233,469,108,881,449,575,065,687,707,189,234,701,062,304,019,195,556,640,625 | 1.35e+66 d |
| 22 | 71,267,145,453,160,802,492,544,456,558,195,889,247,709,087,568,523,522,932,139,098,914,514,633,026,123,046,875 | 1.43e+71 d |
| 23 | 8,657,889,165,377,240,090,806,763,304,972,427,605,257,938,503,262,080,183,410,918,431,629,810,193,178,558,349,609,375 | 1.74e+76 d |
| 24 | 1,198,381,728,825,690,687,169,018,142,857,758,566,981,777,557,929,020,828,586,822,274,714,040,177,888,810,153,961,181,640,625 | 2.41e+81 d |

`δ = 5` is 7.4 min per single weight-pass (× ~192 weights per length-5 cell ≈ 24 h, matching s56's measured wall) and `δ = 6` is 9 days per pass. The **enumeration route is dead at `δ = 5`** (stopping rule 2).


## The LMR cells — where `|S|` decides session 63

- **n = 4, δ = 24** (`(65,17,2^7)`, a = 274): reduced-route `|S| <= n_lam = 156,438,903,314` (s57). With 273 transported source vectors the union of supports is a large fraction of `n_lam`, so `|S| ~ 10^11` — far past the `10^5` 'out of reach' regime of integrator note 3. The reduced `273×273` block is trivial as a determinant, but its **entries** cost `~273·|S|^2 ~ 6·10^24`. Out of reach. (Enumeration is worse: `|H_{4,24}| ~ 1.2·10^93`.)

- **n = 3, δ = 12** (`(19,7,2^5)`, a = 6, the mandatory control): `n_lam = 1,155,302`, `|H_{3,12}| ~ 3.6·10^23`. The Foulkes Gram (orbit-basis `|S|` up to `1.16·10^6`, enumeration `|H|` astronomically larger) is out of reach **even for the control** — its ground truth is taken by the evaluation engine on the `n_chi = 17,047` reduction. This is the concrete proof that the Gram route cannot reach an LMR cell.


**Consequence for session 63.** Neither the enumeration Gram nor the reduced block route reaches `δ = 24` (`|S| ~ 10^11`). Session 63 should report `|S|` at `r = 9` as its first deliverable and run the **direct `λ`-block (evaluation) route**, exactly as the `n = 3` control is done here.

