# Degree 24: the second generator of the invariant semigroup of det_3

Session 21, 2026-08-30/31.  Branch `s21-degree24`.
Pre-registration: `results/PREREG_deg24.md`, commit `f9b4485`, logged before any
value existed; outcome appended to the same file.

## Headline

    Phi_24(det_3)  =  -24,745,222,656,000  =  -2^12 . 3^7 . 5^3 . 7^2 . 11 . 41   != 0

Hence

    24 in E(det_3),   def((8^9), 24) = 0,   mult_{(8^9)} C[Omega-bar]_24 = 1,
    E(det_3)  contains  <18, 24>  =  {0, 18, 24, 36, 42, 48, 54, ...} .

This is the invariant whose existence Corollary 4.7 forces but does not
exhibit: `gcd E = 6` while `min E = 18`, so `E != 18N`, and 24 is the smallest
candidate.  It is a new generator, not a product — there is no degree-6
invariant on `Omega-bar` to multiply `Phi_18` by.

## Why one number decided it in both directions

`analysis/wk4_s21_census.py` computes
`dim C[Sym^3 C^m]^{SL_m}_delta = < h_delta[h_3], s_{((3 delta/m)^m)} >` by
applying the adjoint power-sum operators `p_r^perp` (rim-hook removal) to
`s_lambda`, using

    sum_delta t^delta h_delta[h_3]
        = exp( sum_r (p_r^3 + 3 p_r p_{2r} + 2 p_{3r}) t^r / (6r) ).

Every intermediate partition is a subdiagram of `lambda`, so the whole state
space is the set of partitions inside the `m x (3 delta/m)` box — 24310 of them
for `lambda = (8^9)`.  Exact rational arithmetic; seconds to minutes, not hours.

| delta | 3 | 6 | 9 | 12 | 15 | 18 | 21 | 24 | 27 |
|---|---|---|---|---|---|---|---|---|---|
| `dim C[Sym^3 C^9]^{SL_9}_delta` | 0 | 0 | 0 | 0 | 0 | **1** | 0 | **1** | 1 |

Anchors, all exact:

- ternary cubics (`m = 3`), degrees 1–14: `0,0,0,1,0,1,0,1,0,1,0,2,0,1` — the
  Hilbert function of `C[S,T]` with `deg S = 4`, `deg T = 6`;
- cubic surfaces (`m = 4`): `0` at 4, `1` at 8, `0` at 12, `2` at 16 — the
  classical invariant ring with generators in degrees `8,16,24,32,40,100`;
- `m = 9`: `0` below 18 and `1` at 18 reproduces the banked degree-18 census.

Because the ambient space at 24 is **one-dimensional**, its generator `Phi_24`
is unique up to scale and

    24 in E   <=>   Phi_24(det_3) != 0 ,

so a zero would have been as decisive as a nonzero.  Route (iii) of the brief —
the multiplicity of `(8^9)` in `C[Omega-bar]_24`, a computation strictly larger
than the `delta = 18` run — was never needed.  Note also that `delta = 21` is
*permitted* by the pigeonhole census (`21 <= C(7,3) = 35`) but carries no
invariant at all; the exact multiplicity is strictly sharper than the
combinatorial bound there.

Route (i), the divisorial argument, is dead for structural reasons — see
`docs/degree24_extension.md`.  In one line: `div(phi) = 2P_1 + 3P_2 >= 0`, so
the argument would give `6 in E`, which is false; `Omega-bar` is not normal and
divisors only see the normalisation.

## The evaluator

`engine/br2.c`.  An `SL_9`-invariant of degree 24 is a product of `k = 8`
nine-fold brackets in 24 symbolic letters, each letter in exactly 3 brackets and
no two letters in the same three (else the monomial is its own negative).  So a
bracket monomial is a 24-subset `S` of the 56 triples of `[8]` with every
bracket in exactly 9 of them, and `B(S) = c_S . Phi_24`.

Evaluated at a cubic supported on the six `3x3` permutation monomials, each
letter chooses a permutation `sigma` and a bijection of its three cells
`(r, sigma(r))` to its three brackets; a bracket contributes the sign of the
resulting bijection (its 9 letters) -> (the 9 cells), and vanishes unless that
map is a bijection.  The DP state is the 9-bit used-cell masks of the
**partially filled** brackets only (empty and full are implicit), packed 9 bits
each into a `u64` — at most 7 partial brackets in the orders used, so 63 bits.
Exact `__int128` accumulation (`|V| <= 36^24 = 2.2e37 < 2^127`).  Per level,
`P` sharded passes over the previous level file, `P` doubling on table
overflow, so no result depends on the shard count.

## Runs

Bracket structure `S` (also the DP order):

    (1,4,7) (3,4,7) (1,3,4) (1,3,7) (3,6,7) (3,4,6) (1,3,6) (1,6,7)
    (0,1,3) (1,2,3) (1,2,7) (1,4,5) (2,4,6) (0,4,6) (0,3,5) (0,4,5)
    (2,4,5) (2,5,7) (0,2,7) (0,5,7) (2,5,6) (0,2,6) (0,2,5) (0,5,6)

Second structure `S'` (pair-degree profile `((1,1),(2,14),(3,5),(4,7))` against
`S`'s `((1,4),(2,10),(3,10),(4,2),(5,2))`, so the two are not related by any
relabelling of the eight brackets):

    (0,2,5) (1,2,5) (0,1,2) (1,2,6) (1,2,3) (0,2,3) (2,3,5) (2,3,6)
    (1,3,5) (0,1,3) (0,2,7) (0,1,7) (3,6,7) (0,6,7) (5,6,7) (3,4,7)
    (3,4,5) (1,4,7) (1,4,6) (4,6,7) (4,5,7) (0,4,5) (4,5,6) (0,4,6)

| run | weights `u_sigma` | returns | value | wall |
|---|---|---|---|---|
| `d24_det`  | `sgn`           | `c_S . Phi_24(det_3)` | **−24,745,222,656,000** | 6255 s |
| `d24_even` | `(1,0,0,1,1,0)` | `c_S . K_8`  | −1,428,295,680 | 114 s |
| `d24_odd`  | `(0,1,1,0,0,1)` | `c_S . K_0`  | −1,428,295,680 | 114 s |
| `e24_even` | even only, `S'` | `c_S' . K_8` | −203,212,800 | 152 s |
| `e24_odd`  | odd only, `S'`  | `c_S' . K_0` | −203,212,800 | 152 s |
| `e24_det`  | `sgn`, `S'`     | `c_S' . Phi_24(det_3)` | (see ledger) | — |

Peak DP size of `d24_det`: 258,319,584 states at level 14.

## The restriction to U, and what the cheap runs are

Let `U` be the 6-dimensional space of cubics
`F = sum_sigma u_sigma x_{1 sigma 1} x_{2 sigma 2} x_{3 sigma 3}`; it contains
`det_3` (`u = sgn`) and `per_3` (`u = 1`).  The 9-dimensional diagonal torus of
`GL_9` preserves `U`, and the weight condition `sum_sigma e_sigma M_sigma = 8J`
has exactly the nine solutions `e = (a,a,a,8-a,8-a,8-a)`, `a = 0..8`.  Hence

    Phi_24|_U  =  sum_{a=0}^{8} K_a P^a Q^{8-a},
    P = u_id u_c u_{c^2},   Q = u_{t1} u_{t2} u_{t3},

a binary octic in `(P,Q)`.  A row/column permutation `g` with
`sgn(rho) sgn(pi) = -1` swaps `P` and `Q` and has `det(g)^8 = 1`, so

    K_a = K_{8-a} ,

and with `P(det_3) = 1`, `Q(det_3) = -1`,

    Phi_24(det_3) = sum_a (-1)^a K_a,     Phi_24(per_3) = sum_a K_a .

Setting `u` to be supported on the even permutations returns `K_8`; on the odd
permutations, `K_0`.  These runs are ~55x cheaper (3 permutations per letter
instead of 6, and much tighter masks) and they do two jobs at once: a nonzero
value certifies `c_S != 0` **and** `Phi_24|_U != 0`, which is exactly what makes
the main run decisive in the vanishing direction too.

## Prediction ledger

Everything below was committed to git before the corresponding value existed.

| # | logged at | prediction | outcome |
|---|---|---|---|
| 1 | `f9b4485` | `Phi_24(det_3) != 0`, i.e. `24 in E`; ranked alternatives 30, then 42 | **HIT** |
| 2 | `f9b4485` | `K_a = K_{8-a}`, derived from the `P <-> Q` symmetry, so the even-only and odd-only runs must agree | **HIT**, `-1,428,295,680` twice at `S` |
| 3 | `f9b4485` | that same symmetry does **not** force `sum_a (-1)^a K_a = 0`, because `a` and `8-a` have equal parity | **HIT** (the alternating sum is nonzero) |
| 4 | `b0401a8` | `c_S'/c_S = 35/246`, hence `V(det_3, S') = (35/246) V(det_3, S)`, logged before either `sgn` value existed | see below |
| 5 | `b0401a8` | odd-only at `S'` equals even-only at `S'` | **HIT**, `-203,212,800` twice |

Prediction 4 forces `V(det_3, S') = -3,520,661,760,000` once
`V(det_3, S) = -24,745,222,656,000` is known; the confirming run is recorded in
the run table above.

## Regression gates — all exact

The same evaluator and the same code path at `delta = 18` (6 brackets, 18
letters, `S_18 = C(6,3)` minus a complementary pair, annealed DP order),
against two independently banked integers produced by a different engine
(`engine/dp.c`, factored 36-subproblem route) on a different bracket structure:

    u = sgn  ->  -877,879,296,000   = banked Phi_18(det_3)      EXACT
    u = 1    ->  +50,536,120,320    = banked Phi_18(per_3)      EXACT
    ratio        -4725/272                                       EXACT
    even only -> -185,794,560       = K'_6 (in the same scale)

Peak at `delta = 18`: 138,241,908 states at level 8; 1678 s.

## Normalisation-free numbers

`c_S` depends on the bracket monomial chosen, so the raw integers do not by
themselves name a canonical `Phi_24`.  The following ratios are independent of
that choice (numerator and denominator both scale by `c_S`), and they are the
right things to quote:

    delta = 18:   Phi_18(det_3) / K'_6  =  4725  =  3^3 . 5^2 . 7
                  Phi_18(per_3) / K'_6  =  -272  =  -2^4 . 17
                  (and indeed the banked ratio is -4725/272)

    delta = 24:   Phi_24(det_3) / K_8   =  17325 =  3^2 . 5^2 . 7 . 11
                  — identical at S and at S'.

## Arithmetic signature

`-24,745,222,656,000 = 151,200 x (-163,658,880)`, so the programme's
`151,200 = 2^5 3^3 5^2 7` divisibility — observed on every measured subvalue of
the `delta = 20` functional and never imposed anywhere in the code — survives
into an entirely different computation at a different degree with a different
engine.  Still no proof of it.

Also worth noting: `Phi_18(det_3) = -2^16 3^7 5^3 7^2` and
`Phi_24(det_3) = -2^12 3^7 5^3 7^2 . 11 . 41` share the odd part `3^7 5^3 7^2`
exactly; the ratio is `451/16 = 11 . 41 / 2^4`.  We have no explanation.

## What is now known about the semigroup

`E/6` is a numerical semigroup of multiplicity 3 containing `3` and `4`, so it
contains `<3,4> = {0,3,4,6,7,8,...}` — every integer except `1, 2, 5`.  The only
remaining question is whether `5` belongs, i.e. whether `30 in E`.  See the
degree-30 line in the session record.
