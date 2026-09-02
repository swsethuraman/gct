# Session 35 test ledger — day-one exact computations

All ranks by flint `nmod_mat` over the house primes `P1 = 2147483647`,
`P2 = 2147483629` (both quoted at every deficiency); the two labelled
"exact over Z" are fraction arithmetic with no reduction.  Code:
`analysis/wk9_s35_daytests.py` (parts T1, T1r4, T1w, T2, T2sat, T2node,
T2J, T2Jdet3, T2K, T3, T3v2).  Seed 35 throughout; independent draws per
part.

## T1 — catalecticant `Cat_{2,2}` at `r = 5` (15 x 15)

| point | rank (P1 / P2) |
|---|---|
| pad `x0.c` | 10 / 10 |
| pad `l.c`, generic `l` | 10 / 10 |
| det pencil (random `A_i`, entries in [-9,9]) | **15 / 15** |
| generic quartic | 15 / 15 |
| `q.q'` (product of two quadrics) | 15 / 15 |

`rank <= 10` on the pad locus is a *proof*, not a measurement: for
`F = l.c`, second partials are `l.(d_i d_j c) + (d_i l)(d_j c)` with
`d_i d_j c` linear and `d_i l` scalar, so the image lies in
`l.V + span{d_j c}`, dimension `<= 5 + 5`.  Consequences in
`docs/theory_directions.md` §Direction 1.

## T1r4 — catalecticant at `r = 4` (10 x 10)

pad4 = 8/8, det4-surface pencil = **10/10**, generic = 10/10.
The det4 row was a forced prediction: any drop would put a degree-`<= 10`
element into `I(D_4^det)`, contradicting the s33-certified `e >= 10`.
Passed.

## T1w — the extremal 9-minor of `Cat_{2,2}` at `r = 4` (exact over Z)

The 9x9 minor omitting the lowest-weight row and column (`2e_4`) has torus
weight `(10,10,10,6)` (every Leibniz term has this weight), and it is the
*only* 9-minor of that weight, which is dominance-maximal in the span of
all 9-minors; a nonzero value therefore exhibits a highest-weight vector.

| point | value |
|---|---|
| generic integer quartic | 269637525257856 (nonzero, exact) |
| det4-surface pencil | nonzero, exact (large integer) |
| pad4 `l.c` | 0 (forced by the rank-<=-8 proof) |

Hence `S_(10,10,10,6)` occurs in `I(D_4^pad)_9`, and the same function,
read at `r = 5` (its coefficients only involve `alpha` supported on
`x_1..x_4`, and `c_alpha(F) = c_alpha(F|_{x_5=0})`), lies in
`I(D_5^pad)_9` and is nonzero at a generic point of `D_5^det`.

## T2 — the sigma_2 intersection scheme of a random pencil

- Giambelli degree of `{rank <= 2} subset P(M_4)`: product formula gives
  **20** = codim `D_5^det`.  (First run of the session had a per-factor
  integer-division bug printing 18; fixed to exact rationals before any
  use.  The measured Hilbert function below is the independent check.)
- The 16 3x3 minors of `M(s)` span a **16**-dimensional space of cubics
  (16/16 at both primes) — vs 15 = 35 - 20 for 20 general points.
- Hilbert function of `C[s]/(minors)`: t = 3..9:
  `[19, 20, 20, 20, 20, 20, 20]` — **stabilises at 20** (both primes
  agree at every t).  The intersection scheme has length 20.

## T2sat — cubics through the saturated node scheme

`dim (J : Sym^{T-3})_3 = 16` at `T = 8` and `T = 9` (P1; structure forced
`>= 16` by the minors).  So `h^0(I_Z(3)) = 16` exactly at this pencil:
the 20 nodes impose only 19 conditions on cubics — excess exactly 1.

## T2node — nodality at constructed rank-2 points

Three independent pencils through a random rank-2 matrix at `s = e_1`:
gradient exactly 0 (integer arithmetic), Hessian rank **4 / 4** each —
an ordinary double point every time.

## T2J / T2Jdet3 / T2K — Jacobian-ring Hilbert functions, degree 7

`(R/J_F)_t`, t = 6..10:

| F | t=6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|
| generic quartic | 45 | **30** | 15 | 5 | 1 |
| det pencil | 45 | **31** | 20 | 20 | 20 |
| pad `l.c` | 69 | 86 | 109 | 136 | 166 |

- generic row = coefficients of `(1+z+z^2)^5` exactly (smooth CI Koszul —
  proved, and the run reproduces it).
- det row: `(R/J)_7 = 31 = 30 + 1` at **four** independent pencils (one
  with entries in [-9,9], three fresh with entries in [-99,99]), both
  primes each.
- control (T2K): quartics with `k` nodes at *general* points,
  `k = 1, 5, 11, 13` (5 linear conditions per node; `F(p) = 0` free by
  Euler): `(R/J)_7 = **30 / 30** at every k`.  The +1 is configuration,
  not node count.

## T3 / T3v2 — `dim I(D_5^pad)_delta`, exact, all weight blocks

Per-torus-weight-block symbolic rank of the multiplication comorphism
`mu^*: Sym^delta(Sym^4 C^5) -> Sym^delta(C^5) (x) Sym^delta(Sym^3 C^5)`
(entries are exact integers; every block full rank at P1; any deficiency
would have been re-checked at P2 — none occurred).  T3v2 restricts to
S_5-representative blocks (equivariance) and reproduced T3 at delta = 3.

| delta | dim Sym^delta | rank mu^* | dim I(pad)_delta |
|---|---|---|---|
| 2 | 2 485 | 2 485 | **0** |
| 3 | 59 640 | 59 640 | **0** |
| 4 | 1 088 430 | 1 088 430 | **0** |

`I(D_5^pad)` is exactly zero through degree 4; with T1w it is nonzero at
degree 9.  Pad onset in `[5, 9]`, measured + proved.
