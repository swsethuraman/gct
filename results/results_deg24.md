# Degree 24: is there an SL_9-invariant on the orbit closure of det_3?

Session 21, 2026-08-30/31.  Branch `s21-degree24`.
Pre-registration: `results/PREREG_deg24.md`, commit `f9b4485`, logged before any
value existed.

**STATUS: IN PROGRESS — this file is written up to the regression gates.  The
degree-24 value is not yet in it.**

## The reduction (this is what made the question cheap)

`analysis/wk4_s21_census.py` computes

    dim C[Sym^3 C^m]^{SL_m}_delta  =  < h_delta[h_3] , s_{((3 delta/m)^m)} >

by applying the adjoint power-sum operators `p_r^perp` (rim-hook removal) to
`s_lambda`, using

    sum_delta t^delta h_delta[h_3]
        = exp( sum_r (p_r^3 + 3 p_r p_{2r} + 2 p_{3r}) t^r / (6r) ).

Every intermediate partition is a subdiagram of `lambda`, so the entire state
space is the set of partitions inside the `m x (3 delta/m)` box — 24310 of them
for `lambda = (8^9)`.  Exact rational arithmetic.  Result for `m = 9`:

| delta | 3 | 6 | 9 | 12 | 15 | 18 | 21 | 24 |
|---|---|---|---|---|---|---|---|---|
| dim | 0 | 0 | 0 | 0 | 0 | **1** | 0 | **1** |

Anchors (all exact):

- ternary cubics `m = 3`: dims `0,0,0,1,0,1,0,1,0,1,0,2,0,1` for
  `delta = 1..14` — the Hilbert function of `C[S,T]`, `deg S = 4`, `deg T = 6`;
- cubic surfaces `m = 4`: `0` at `delta = 4`, `1` at `8`, `0` at `12`, `2` at
  `16` — the invariant ring with generators in degrees `8, 16, 24, 32, 40, 100`;
- `m = 9`: `0` below 18 and `1` at 18 reproduces the banked degree-18 census.

Because the ambient degree-24 space is **one-dimensional**, its generator
`Phi_24` is unique up to scale, and

    24 in E(det_3)   <=>   Phi_24(det_3) != 0 ,

with a **zero as decisive as a nonzero**.  The expensive route (iii) of the
brief — the multiplicity of `(8^9)` in `C[Omega-bar]_24` — is not needed: the
ambient census does that job.

Route (i), the divisorial extension argument, is dead for structural reasons;
see `docs/degree24_extension.md`.  In one line: `div(phi) = 2P_1 + 3P_2 >= 0`,
so the argument would give `6 in E`, which is false — `Omega-bar` is not normal
and divisors only see the normalisation.

## The evaluator

`engine/br2.c`.  Streamed level DP over the 24 letters; state = the 9-bit
used-cell masks of the partially filled brackets only (empty and full brackets
are implicit), packed 9 bits each into a `u64`; exact `__int128` accumulation
(the crude bound `|V| <= 36^24 = 2.2e37 < 2^127` is safe); per level, `P`
sharded passes over the previous level file with `P` doubling on table
overflow, so the in-RAM table never overflows and no result depends on the
shard count.

Input is a bracket structure `S`: a 24-subset of the 56 triples of `[8]` in
which each bracket lies in exactly 9 triples, plus a DP order.  For any such
`S` the bracket monomial `B(S)` is `c_S . Phi_24` for some scalar `c_S`.
Restricted to the 6-dimensional space `U` of cubics
`sum_sigma u_sigma x_{1 sigma 1} x_{2 sigma 2} x_{3 sigma 3}`, the six weights
`u_sigma` are the only input, so

- `u = sgn` evaluates at `det_3`,
- `u = 1` evaluates at `per_3`,
- `u = (1,0,0,1,1,0)` (even permutations only) returns `K_8`,
- `u = (0,1,1,0,0,1)` (odd only) returns `K_0`,

where `Phi_24|_U = sum_{a=0}^{8} K_a P^a Q^{8-a}`, `P = u_id u_c u_{c^2}`,
`Q = u_{t1} u_{t2} u_{t3}` (the weight condition
`sum_sigma e_sigma M_sigma = 8J` has exactly these nine solutions
`e = (a,a,a,8-a,8-a,8-a)`), and `K_a = K_{8-a}` because a row/column
permutation with `sgn(rho) sgn(pi) = -1` swaps `P` and `Q` and has
`det^8 = 1`.

## Regression gates — PASSED

The same evaluator, same code path, at `delta = 18` (6 brackets, 18 letters,
`S = C(6,3)` minus a complementary pair, annealed DP order):

    u = sgn   ->   VALUE  -877,879,296,000     = banked Phi_18(det_3)   EXACT
    u = 1     ->   VALUE  +50,536,120,320      = banked Phi_18(per_3)   EXACT
    ratio                  -4725/272                                   EXACT

These are two independently banked integers from an entirely different engine
(`engine/dp.c`, factored 36-subproblem route) and a different bracket
structure, reproduced to the last digit by new code on a new formulation.

Peak DP size at `delta = 18`: 138,241,908 states at level 8; 1678 s wall.

## Degree-24 runs

| run | weights | what it returns | status |
|---|---|---|---|
| `d24_det`  | `sgn`            | `c_S . Phi_24(det_3)` — **the answer** | running |
| `d24_even` | `(1,0,0,1,1,0)`  | `c_S . K_8` — certifies `c_S != 0`     | running |
| `d24_odd`  | `(0,1,1,0,0,1)`  | `c_S . K_0`; gate `K_0 = K_8`          | queued |
| `d24_perm` | `1`              | `c_S . Phi_24(per_3)`                  | queued |
| second `S'`| `sgn`, `even`    | proportionality gate `c_{S'}/c_S`      | queued |

Bracket structure in use:

    S = (1,4,7) (3,4,7) (1,3,4) (1,3,7) (3,6,7) (3,4,6) (1,3,6) (1,6,7)
        (0,1,3) (1,2,3) (1,2,7) (1,4,5) (2,4,6) (0,4,6) (0,3,5) (0,4,5)
        (2,4,5) (2,5,7) (0,2,7) (0,5,7) (2,5,6) (0,2,6) (0,2,5) (0,5,6)

(also the DP order; every bracket occurs in exactly 9 triples; at most 7
brackets are partially filled at any level, so the packed state fits in 63
bits).
