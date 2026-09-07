# P_r = R_r : does {per_3(A(s))} fill all cubics in r variables?

Rank of the differential of the permanent parametrisation `M (3x3 linear forms) -> per_3(M(s))` at a generic `M`, over both house primes, vs `dim Sym^3 C^r`.  Equality => `P_r = R_r` => `I(pad) = I(R_r)` => `mult_pad = mult_red` exactly.

| r | dim Sym^3 C^r | param rank (P1, 3 seeds) | param rank (P2) | P_r = R_r ? |
|---|---|---|---|---|
| 2 | 4 | 4 | 4 | **yes** |
| 3 | 10 | 10 | 10 | **yes** |
| 4 | 20 | 20 | 20 | **yes** |
| 5 | 35 | 35 | 35 | **yes** |
| 6 | 56 | 50 | 50 | no (P_r ⊊ R_r) |
| 7 | 84 | 59 | 59 | no (P_r ⊊ R_r) |

Reading: `P_r = R_r` for `r ≤ 5` (permanental cubics are all cubics), so the r ≤ 5 calibration demands `mult_pad = mult_red` exactly; `P_r ⊊ R_r` for `r ≥ 6`, so there only `mult_pad ≤ mult_red` (the transfer lemma's exact/upper-bound split, seen from the cubic side).
