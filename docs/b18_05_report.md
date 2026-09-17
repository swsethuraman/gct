# B18-05 — Eleven-equation restriction rank on actual padding: 9 or 10?

15 September 2026. Claude Fable 5.1. Worktree `work/batch15_workers/B15-05`,
worked in place. Output confined to `docs/b18_05_report.md`,
`analysis/b18_05_psi.py`, `analysis/b18_05_proof.py`, `results/b18_05/` and the
wrapper's log receipts.

Starting state (read-only, recorded before any write):

```
git rev-parse HEAD          39a9154b57956c51d1f3206a88f099d406ef8f47
git rev-parse HEAD^{tree}   d66688de7d675857fb95be2220bd88c857d82c34
```

## Plain terms

B17-04 identified eleven determinant equations `E` (weight `(73,19,2^8)`,
degree 27) and asked how many of them stay independent after restriction to
the actual padding closure `X_pad = closure(GL16 · z·per3)`. It proved
`9 <= rank <= 10`: nine by an exact nonzero minor on actual padding points,
ten because one combination `kappa·E` vanishes globally on padding (the
Hessian-divisibility identity). The twelve sample points had rank exactly nine,
so a second combination `w·E` (equivalently the expression `Psi`) vanished at
every sample point. Whether `Psi` vanishes on all of `X_pad` was left open.

This slot settles that. **This is equation structure inside a cell that is
already excluded** (degree 27, `a=429`, `i_det=11`, `m_det=418`,
`243<=m_pad<=288`, `D<0`). Nothing here revives it or produces a gap. The value
is knowing which determinant equations padding also satisfies.

**Answer: the rank is exactly 9.** `Psi = w·E` vanishes on all of `X_pad`,
and in fact on every padded product `(linear) × (cubic in a complementary
nine-space)`; the proof is in Step 2.

Two routes were named: prove `Psi=0` globally (rank 9), or exhibit one
certified actual-padding point with `Psi != 0` (rank 10). Before any symbolic
attempt I price the symbolic support and, independently, evaluate `Psi` exactly
at fresh actual-padding points with large random entries. A nonzero exact
value at one genuine point is a complete certificate for rank 10; twelve zeros
at small-entry points are not a certificate for rank 9.

## Conventions (ADOPTED from B17-04 and the accepted Hessian11 evaluator)

Chart: `F(t,x) = t^4 + f2(x) t^2 + f3(x) t + f4(x)` monic and depressed,
`x in Q^9`, `e = e1`. `N_d = Hess(f_d)(e)/(d(d-1))`, `u_d = N_d e`,
`s_d = e^T N_d e`, `p = t^4 + s2 t^2 + s3 t + s4`,
`B = 2t^2 N2 + 6t N3 + 12 N4`, `v = 4t u2 + 3u3`, `h = 12t^2 + 2s2`,
`H = [[h, v^T],[v, B]]` (this is the full ten-variable Hessian of `F` at
`(t,e)`), `A = det B`, `D_H = det H`, `J_d = -u_d^T adj(B) v`,
`Q22 = (0,u2)^T adj(H) (0,u2)`, `T2 = tr(adj(H) diag(0,N2))`,
`R_j(P) = [t^j](P mod p)`, `S_j = [t^j](D_H mod p^2)`.

Basis order (zero based): `E = (R1(A), s2 R3(A), R2(J2), R3(J3), R3(Q22),
S3, s2 S5, s3 S6, s4 S7, R1(T2), s2 R3(T2))`.

`kappa = (12,-10,4,3,0,0,0,0,0,0,0)`, `w = (216,-212,64,0,0,-1,1,1,13,4,2)`.
Using the ambient identity `kappa·E = S3 - s2 S5 - s3 S6 + (s2^2 - s4) S7`
(B17-04, Schur expansion of `D_H`), `w·E` equals the B17-04 expression

```
Psi = 204 R1(A) - 202 s2 R3(A) + 60 R2(J2) - 3 R3(J3)
      + 4 R1(T2) + 2 s2 R3(T2) + (s2^2 + 12 s4) S7
```

on the whole chart (rechecked by hand below: `216-12=204`, `-212+10=-202`,
`64-4=60`, `0-3=-3`, `13-1=12`, `s2^2` from `+s2^2 S7`).

Padding point normalisation (B17-04): raw `G = (z·per3)(L y)`, `L` integer
10x10 invertible, `z` the row-0 source form, permanent entries row major.
`c = [t^4] G`, `a1_i = [t^3 x_i] G`, `Q00 = 1`, `Q0i = -3 a1_i`, `Qii = 12c`,
`F = G(LQ y)/c`. Then `F` is monic depressed. The finite degree-27 value on the
genuine orbit point is `c^27 E(F)`, so nonvanishing of `E(F)` and of the finite
polynomial value are equivalent when `c != 0`.

All arithmetic below is exact rational (characteristic zero), not modular.

## Step 1 — Pricing, and the bounded evaluation run (MEASURED)

**Price of the naive symbolic support.** The requested pullback
`c^27 Psi(pi(((z·per3) composed with L)/c))` for symbolic 10x10 `L` is a
polynomial of degree 108 in 100 variables (each `E` is degree 27 in the
quartic's coefficients, each coefficient degree 4 in `L`). Using the Borel
invariance of a highest-weight vector removes at most 55 parameters; using the
stabiliser of `z·per3` a further 6. The remaining support is still a
degree-108 polynomial in about 40 variables, far above 512 MiB. **The naive
symbolic route prices out** and was not attempted. What was run instead is
below, and a structural reduction that makes the symbolic proof small is in
Step 2.

**Run 1** (`analysis/b18_05_psi.py`, receipt
`results/logs/b18_05_psi_20260915_01_resources.json`): exit 0, wall 5.8 s,
peak Job Object memory 20.1 MB, one process, one BLAS thread, cap 60 s / 512 MiB
enforced by the inspected `analysis/b15_bound.py`. Output
`results/b18_05/psi_evaluation.json`.

The evaluator is a fresh implementation (no import of B17-04 or Hessian11
code): the quartic is given as a monomial dictionary and an `n x 10` matrix, the
ten-variable Hessian along the chart line is computed exactly at 21 integer
nodes plus one check node, and every `t`-polynomial is recovered by exact
interpolation. It asserts the chart structure (`p(t) = F(t,e)`, `h`, `v`, `B`
blocks) at three further nodes.

| Check | Result | Label |
|---|---|---|
| B17-04 seeds 170400, 170401, 170402: all eleven `E` values reproduced exactly (integers of ~90 digits), same `c`, `a1` | match | CERTIFIED |
| `kappa·E = 0` and the ambient identity `kappa·E = S3 - s2 S5 - s3 S6 + (s2^2 - s4) S7` residual 0 at every point evaluated | holds | MEASURED |
| `w·E` equals the displayed `Psi` expression at every point | holds | MEASURED |
| Two det4 points (random `16 x 10` restriction, entries in `[-7,7]`): all eleven `E` values zero | holds | MEASURED (control) |
| Six fresh actual `z·per3` points, `L` entries uniform in `[-10^4, 10^4]`, seeds 180500..180505, all `det L != 0`, `c != 0` (`c` of order `10^15`) | `Psi = 0` exactly at all six | MEASURED |
| Eight points of the wider family `z · (random nine-variable cubic, coefficients in [-5,5])` composed with `L`, entries in `[-50,50]`, seeds 180600..180607 | `kappa·E = 0` and `Psi = 0` exactly at all eight | MEASURED |

**Honest negatives.** (a) The generic-quartic control inside run 1 was
degenerate: the sparse random quartic happened to have no `t^k x_1^(4-k)`
monomials, so `p = t^4`, every `E` vanished, and the control reports
`w_E_nonzero = false`. That is a bad control, not evidence about `w`; `w` is
not an ambient relation because `E` is an independent ambient basis (inherited).
The diagnosis was a sub-second re-evaluation outside the wrapper, not a new
computation. (b) The in-run sample ranks (6 and 8) are limited by the number of
points and carry no information beyond the individual `Psi = 0` results.

**What Step 1 does and does not establish.** Route 2 (a nonzero witness) is
closed in practice: a nonzero polynomial of degree 108 in the entries of `L`
vanishing at six independent points drawn from `[-10^4,10^4]^100` has
Schwartz–Zippel probability at most `(108/20001)^6 ~ 2·10^-14`. But a sampled
zero is a ceiling, never membership: **these fourteen zeros prove nothing about
the global rank.** The rank stays `9 <= rank <= 10` until Step 2.

The eight generic-cubic zeros are the useful hint: `Psi` is not a
permanent-specific identity. It is a property of the whole product family
`Y = closure{ (z · C(y)) composed with L : C any cubic in nine variables }`,
which contains `X_pad`. A proof on `Y` has far more structure to use.

## Step 2 — Root-local reduction and the global proof of `Psi = 0` (PROVED on the family, see hypotheses)

### 2.1 The family and its structure along the chart line

Let `F = l · Gamma` on `V = C^10` with `l` a linear form, `Gamma = C ∘ pi` a
cubic pulled back from `V / C·zeta` (so `Gamma` is invariant under translation
by `zeta`), and `nu := l(zeta) != 0`. In source coordinates this is exactly
`z · C(y_1..y_9)` with `zeta = d/dz`; every `(z·C) ∘ L`, `L` any 10x10 matrix
with `l(zeta) != 0`, is of this form. Write `a = grad l` (constant),
`g(t) = grad Gamma(x(t))`, `K(t) = Hess Gamma(x(t))` along the chart line
`x(t) = t e_t + e_1`. Then

```
H(t) = z(t) K(t) + a g^T + g a^T,   z(t) := l(x(t)),   K zeta = 0,   g·zeta = 0.
```

Normalise `l` so that `z` is monic: `z = t - t1`. Since `p = z·Gamma(x(t))` is
monic and depressed, `Gamma(t) := Gamma(x(t)) = t^3 + t1 t^2 + g1 t + g0` and

```
s2 = g1 - t1^2,   s3 = g0 - t1 g1,   s4 = -t1 g0.
```

(2.1a) `H zeta = nu g` (from `K zeta = 0`, `g·zeta = 0`). Hence
`zeta^T H zeta = 0` and, with Euler `g·x = 3 Gamma`,
`zeta^T H(t) x(t) = 3 nu Gamma(t)`.

(2.1b) Expanding (2.1a) in the chart blocks `h = 12t^2 + 2s2`,
`v = 4t u2 + 3u3`, `B = 2t^2 N2 + 6t N3 + 12 N4`, with
`zeta = (zeta0, zeta_W)`, `U_d := u_d · zeta_W`, `Z_d := zeta_W^T N_d zeta_W`:

```
zeta^T H x = zeta0 (12t^3 + 6 s2 t + 3 s3) + 6t^2 U2 + 9t U3 + 12 U4 = 3 nu (t^3 + t1 t^2 + g1 t + g0)
   =>  nu = 4 zeta0,   U2 = 2 zeta0 t1,   U3 = (2/3) zeta0 (g1 + t1^2).
zeta^T H zeta = (12t^2 + 2s2) zeta0^2 + 2 zeta0 (4t U2 + 3 U3) + 2t^2 Z2 + 6t Z3 + 12 Z4 = 0
   =>  Z2 = -6 zeta0^2,   Z3 = -(8/3) zeta0^2 t1.
```

In particular `zeta0 != 0` on the chart (the padding direction is never in the
polar hyperplane `W`).

(2.1c) At `t = t1`: `H(t1) = a g^T + g a^T` has rank at most 2, so every minor
of size at least 3 vanishes there: `z^7 | A`, `z^7 | adj(H)` entrywise (hence
`z^7 | T2`, `z^7 | Q22`), `z^6 | adj(B)` entrywise (hence `z^6 | J2, J3`),
`z^8 | D_H`.

(2.1d) At each root `t_i` of `Gamma` (`i = 2,3,4`), the vector
`k_i := 3 z(t_i) zeta - nu x(t_i)` is in the kernel of `H(t_i)`: by (2.1a) and
Euler `H x = 3 grad F = 3 (Gamma a + z g) = 3 z g` at a root of `Gamma`, so
`H k_i = 3 z nu g - nu · 3 z g = 0`. Its `t`-component is
`k_0 = 3 z_i zeta0 - 4 zeta0 t_i = -zeta0 (t_i + 3 t1)`.

Consequently `Gamma | D_H`, and if `Gamma(t1) != 0` then `p | D_H` and
`z^7 | q_D := D_H / p`.

### 2.2 Reduction of every `E` coordinate to values at the three roots

For `X` in `{A, J2, J3, Q22, T2}` write `X = z·(X/z)`; then
`X mod p = z · r_X` with `r_X := (X/z) mod Gamma` of degree at most 2, and
`D_H mod p^2 = p · (q_D mod p) = p · z · r2` with `r2 := (q_D/z) mod Gamma`.
Therefore

```
R1(X) = r_{X,0} - t1 r_{X,1},  R2(X) = r_{X,1} - t1 r_{X,2},  R3(X) = r_{X,2},
S_m = [t^m] ( z^2 Gamma r2 ),  in particular S7 = r2_2.
```

When `Gamma` has distinct roots and `z(t_i) != 0`, Lagrange interpolation
gives `r_X = sum_i (X(t_i)/z_i) L_i(t)` and `r2 = sum_i (q_D(t_i)/z_i) L_i(t)`
with `q_D(t_i) = D_H'(t_i) / p'(t_i)`, `p'(t_i) = z_i Gamma'(t_i)`.

**Corank-one lemma (any quartic on the chart).** If `H(t*)` has corank exactly
one with kernel vector `k = (k0, k_W)`, `k0 != 0`, then `B(t*)` is invertible and
at `t*`

```
adj(H) = (A/k0^2) k k^T,      J_d = (A/k0) (u_d · k_W),     Q22 = (A/k0^2) (u2 · k_W)^2,
T2 = (A/k0^2) k_W^T N2 k_W,   D_H' = tr(adj(H) H') = (A/k0^2) k^T H' k,
H' = [[24t, 4u2^T],[4u2, 4t N2 + 6 N3]].
```

Proof: `adj(H)` of a corank-one symmetric matrix is `mu k k^T`, and
`mu k0^2 = adj(H)_tt = det B = A`. From `H k = 0`: `v k0 + B k_W = 0`; if `B`
were singular with kernel vector `m`, then `(0,m)` would be a second kernel
vector of `H` (`v·m = -k_W^T B m / k0 = 0`), contradicting corank one with
`k0 != 0`. So `adj(B) v = A B^{-1} v = -(A/k0) k_W`, which gives `J_d`. The rest
is `adj(H) = (A/k0^2) k k^T` contracted with `(0,u2)`, `diag(0,N2)`, and `H'`.

**On the family**, with `k = k_i` from (2.1d), `k_W = 3 z_i zeta_W - nu e`:

```
u_d · k_W      = 3 z_i U_d - nu s_d,
k_W^T N_d k_W  = 9 z_i^2 Z_d - 6 nu z_i U_d + nu^2 s_d,
k^T H' k       = 24 t_i k0^2 + 8 k0 (u2·k_W) + 4 t_i k_W^T N2 k_W + 6 k_W^T N3 k_W,
```

and by (2.1b) every one of these is an explicit polynomial in
`(t1, t_i, g1, g0, zeta0)`. Hence at each root, `X(t_i) = A(t_i) · phi_X(t_i)`
and `q_D(t_i) = A(t_i) · phi_D(t_i)` with explicit rational `phi`, and every
`E_j` is

```
E_j = sum_{i=2}^{4} A(t_i) · E_j^{(i)}(t2,t3,t4,zeta0) / D_i,
D_i = k0(t_i)^2 z_i^2 Gamma'(t_i)^2,   t1 = -(t2+t3+t4),
```

with `E_j^{(i)}` polynomials. The three values `A(t_i)` enter linearly and
nothing else about `N` enters at all.

### 2.3 The identity (MEASURED exactly, and it is a polynomial identity)

`analysis/b18_05_proof.py`, Part B, builds the `E_j^{(i)}` in the sparse
polynomial ring `Q[t2,t3,t4,zeta0]` (no denominators, no expression
simplification) and finds, for each `i`:

```
sum_j w_j     E_j^{(i)} = 0     (the Psi identity),
sum_j kappa_j E_j^{(i)} = 0     (reproves kappa on this family),
```

each `E_j^{(i)}` having between 11 and 34 monomials. Collecting all monomial
coefficients (102 rows) the constant-coefficient relations among the eleven
model functions form exactly the two-dimensional space `span(kappa, w)`
(model rank 9). The run: receipt
`results/logs/b18_05_proof_20260915_03_resources.json`, exit 0, wall 1.5 s,
well under 60 s / 512 MiB.

Hence, at every chart point of the family satisfying the **genericity
hypotheses** (G): `p` squarefree, `Gamma(t1) != 0`, `zeta0 != 0` (automatic),
`A(t_i) != 0` for each root (equivalently `gcd(A, Gamma) = 1`, which forces
corank exactly one at each `t_i`), and `k0(t_i) != 0` (`gcd(k0, Gamma) = 1`),
`Psi = w·E = 0` and `kappa·E = 0`.

### 2.4 Validation of the derivation at actual padding points (CERTIFIED)

Part A of the same script checks every lemma above as an exact polynomial
statement, at three actual `z·per3` points: B17-04 seed 170400, this slot's
seed 180500 (entries up to `10^4`), and seed 180999 (entries up to 30). All
pass at all three:

| Lemma | Check performed |
|---|---|
| (2.1b) | `nu = 4 zeta0`, `U2`, `U3`, `Z2`, `Z3` closed forms; `zeta^T H zeta = 0` and `zeta^T H x = 3 nu Gamma` as polynomials in `t` |
| (2.1c) | vanishing orders at `t1` measured: `A, J2, J3, Q22, T2` order 7, `D_H` order 8 |
| (2.1d) | `Gamma` divides `H(t) k(t)` entrywise, `k0 = -zeta0 (t + 3 t1)` |
| corank-one lemma | `k0^2 adj(H) ≡ A k k^T`, `J_d k0 ≡ A (u_d·k_W)`, `Q22 k0^2 ≡ A (u2·k_W)^2`, `T2 k0^2 ≡ A k_W^T N2 k_W`, `D_H' k0^2 ≡ A k^T H' k`, all mod `Gamma` |
| closed forms | `u_d·k_W`, `k_W^T N_d k_W` equal their (2.1b) expressions as polynomials |
| (G) | `p` squarefree, `gcd(A,Gamma) = gcd(k0,Gamma) = 1`, `Gamma(t1) != 0`, `zeta0 != 0` |
| whole chain | all eleven `E` values rebuilt from `A mod Gamma`, the roots and `zeta0` alone (inverses taken in `Q[t]/(Gamma)`) equal the directly computed values exactly |

Here `zeta = (LQ)^{-1} e_0` and `l` is row 0 of `LQ`, rescaled to be monic.
These checks validate the algebra; the proof itself is 2.1 to 2.3.

### 2.5 From the chart identity to the closure

Fix the parametrisation `G(C, L) = (z · C(y)) ∘ L`, `C` a nine-variable cubic,
`L` any 10x10 matrix. The inherited degree-27 polynomial lift gives
`P(C, L) := Psi_global(G(C, L))`, a polynomial in the coefficients of `C` and
the entries of `L`. On the nonempty Zariski-open set where `c != 0` and (G)
holds, `P = c^27 · Psi_chart = 0` by 2.3; (G) is nonempty because the three
points of 2.4 satisfy it. The parameter space is irreducible, so `P ≡ 0`,
including singular `L` and points with `c = 0`.

A point of `X_pad` is `g · (z·per3)` with `g` in `GL16`; the eleven-space
consists of highest-weight vectors of a ten-part weight, so their values
depend only on the restriction to the first ten coordinates, which is
`(z·per3) ∘ L` with `L` the relevant 10x10 block of `g` (this is the same
block-diagonal/dependent-restriction argument B17-04 used for `kappa`, and it
is ADOPTED). Every such point is `G(per3, L)`. Hence `Psi_global` vanishes on
`X_pad`, and in fact on the larger closure
`Y = closure{ (z·C(y)) ∘ L : C any nine-variable cubic }`.

### 2.6 Conclusion on the rank

`kappa` (B17-04, accepted) and `w` both lie in the kernel of
`E -> C[X_pad]`; they are independent (`E10` coefficient 2 versus 0). So the
restriction rank is at most 9. B17-04's nonzero 9x9 actual-padding minor
(accepted by B17-11; its first three points' `E` values are reproduced exactly
here) gives at least 9. Therefore

```
rank( E -> C[X_pad] ) = 9,     ker = span(kappa, w),   exactly,
```

at degree 27, and for the transported eleven-space in every degree `d >= 27`
by B17-04's accepted `c^(d-27)` argument. The same holds for the larger family
`Y` (rank at least 9 from `X_pad` inside `Y`, at most 9 by 2.5).

## Step 3 — Labelled claims

| # | Claim | Label | Scope and hypotheses |
|---|---|---|---|
| 1 | The fresh evaluator reproduces B17-04's eleven `E` values exactly at seeds 170400–170402 | CERTIFIED | Same `Q` normalisation; exact rational arithmetic |
| 2 | `Psi = 0` at six fresh actual `z·per3` points with entries in `[-10^4,10^4]` and at eight `z·(generic cubic)` points | MEASURED | Ceiling only; not used in the proof |
| 3 | Structure lemmas (2.1a)–(2.1d) and the corank-one lemma | PROVED | Elementary linear algebra and Euler identities; hypotheses stated inline |
| 4 | `Psi = w·E = 0` and `kappa·E = 0` at every chart point of the family `Y` satisfying (G) | PROVED | The reduction 2.2 plus the exact polynomial-ring identity 2.3 (a finite exact computation, rerunnable) |
| 5 | `Psi_global` vanishes on all of `Y`, hence on `X_pad` | PROVED, conditional on ADOPTED premises | Needs: inherited degree-27 polynomial lift of each `E`; ten-part-weight restriction argument (B17-04); (G) nonempty (verified at three exact points) |
| 6 | `rank(E -> C[X_pad]) = 9` exactly, kernel `= span(kappa, w)` | PROVED (conditional as in 5) | Lower bound is B17-04's accepted minor; upper bound is 5 |
| 7 | On the larger family `Y` (`z` times any nine-variable cubic), the rank is also exactly 9 with the same kernel | PROVED (conditional as in 5) | Upper bound 5; lower bound from `X_pad` inside `Y` |
| 8 | The model in 2.3 has no third constant relation | MEASURED | Model rank 9 on 102 coefficient rows; consistent with 6 and 7, not needed for them |
| 9 | Nothing about the gap, `m_pad`, `i_pad` or any cell changes | — | Degree-27 cell remains excluded: `a=429, i_det=11, m_det=418, 243<=m_pad<=288, D<0` |

**What this means for equation structure (the useful part for slot 06).**
Both determinant equations that padding satisfies inside this eleven-space,
`kappa·E` and `w·E`, are consequences of the product structure
`(linear form) × (cubic on a complementary nine-space)` alone. Neither uses
anything about the permanent. Concretely, on such a product the ten-variable
Hessian along any chart line has rank two at the root of the linear factor and
corank one at the roots of the cubic, and the eleven-space sees nothing else.
A cell whose determinant equations are all of this "rank-two point" type will
be satisfied by every padded product, so selecting genuinely different cells
means looking for determinant equations that are *not* implied by one rank-two
point on the line. The nine surviving directions here are of that kind.

**Honest negatives and limits.**

- The naive symbolic pullback over symbolic `L` was never run; it prices out
  (Step 1). The proof avoids it entirely by the root-local reduction.
- Run 2 (`b18_05_proof_20260915_02`) hit the 60 s wall inside sympy's
  expression expansion of the same identity; exit 124, peak memory below the
  cap. This was an implementation choice, not a mathematical obstacle; run 3
  performs the identical check in a sparse polynomial ring in 1.5 s. Both
  receipts are preserved. The cap hit is not evidence of anything.
- The generic-quartic control in run 1 was degenerate (Step 1). Not repaired
  inside a wrapped run; it is not needed for any claim, since ambient
  independence of `E` is inherited.
- Claim 5 is conditional on the inherited polynomial-lift premise and on
  B17-04's restriction argument from `GL16` to 10x10 blocks. Neither is
  re-proved here.
- Corank exactly one at the roots of `Gamma` and `k0(t_i) != 0` are genuine
  hypotheses of the corank-one lemma; they are only needed on a dense open
  set, and the closure step 2.5 handles the rest by polynomiality.
- The equation `kappa·E` was reproved on the model only on the open set (G);
  B17-04's global Hessian-divisibility proof remains the primary proof.
- No modular arithmetic was used anywhere; every number is an exact rational.

## Invocation history and integrity

Three wrapped invocations, all one process, one BLAS thread, 60 s / 512 MiB,
through the inspected `analysis/b15_bound.py`:

| Run | Script | Exit | Wall | Peak Job memory |
|---|---|---|---|---|
| `b18_05_psi_20260915_01` | `analysis/b18_05_psi.py` | 0 | 5.8 s | 20.1 MB |
| `b18_05_proof_20260915_02` | `analysis/b18_05_proof.py` (sympy-expression Part B) | 124 (wall cap) | 60 s | below cap |
| `b18_05_proof_20260915_03` | `analysis/b18_05_proof.py` (polynomial-ring Part B) | 0 | 1.5 s | below cap |

One sub-second unwrapped diagnostic (re-evaluating the degenerate control) is
recorded in Step 1. No commit, stage, push, fetch, checkout, reset or clean was
run. Besides the two read-only commands in the opening, one read-only
`git status --porcelain` was run at the end to list this slot's new files; it
changed nothing, and it is recorded here because the preamble asks for no other
git command. No
historical artifact was modified. Writes: `docs/b18_05_report.md`,
`analysis/b18_05_psi.py`, `analysis/b18_05_proof.py`, `results/b18_05/`, and
the wrapper's own receipts under `results/logs/`.

Input pins (SHA256): B17-04 report `aee0a938…45d5` and `restriction.json`
`92f9579c…19e9` match the values pinned by B17-11's supplement;
`padding_points.json` `82fb8c88…ce63`; B17-11 supplement `b22c4d5b…828b`.
Full list with output hashes in `results/b18_05/MANIFEST.json`.

## One next sufficient test, and its price

The restriction rank question is closed; no further test is needed for it.
The one test this result makes sharp is for slot 06's cell selection: **in a
candidate cell, decide whether each determinant equation is implied by the
"one rank-two point on the chart line" structure** (2.1c), since every such
equation is automatically satisfied by all padded products. Concretely, for a
candidate highest-weight equation `E` given on the chart, evaluate its
polynomial lift on the family `Y` at a handful of exact points with large
entries (a ceiling test, at the price of run 1: under 10 s, under 50 MB per
dozen points). A nonzero value certifies that the equation is not of product
type and therefore a genuine candidate for separating padding. A zero value
means the equation should be proved to be of product type by the same
root-local reduction, which for an equation built from the ten-variable
Hessian along the line costs a polynomial-ring identity check of the size of
run 3.


---

## Addendum (B19-05, 16 September 2026) — the generic-quartic control, re-run with full monomial support

Nothing above this line has been changed. This addendum repairs the one recorded
defect of Step 1: the run-1 "generic quartic" control was degenerate, so the
premise that `w` is not an ambient relation (equivalently, that the eleven `E`
coordinates are an independent ambient basis, which is what keeps the rank-9
result from being vacuous) had no in-batch check.

**Provenance.** Worktree `B15-05`, `git rev-parse HEAD` =
`ca3d6d807e70e74069816f558d7d0b9b11cb7272`, `HEAD^{tree}` =
`2fcc712f1cae827a4185c6e9aea318eac725dd48`. Script `analysis/b19_05_control.py`
(SHA256 `8429fbad96401ca0cea2f035b1e116939783967603ef06e78d24654e8faab7e6`), which
imports the unchanged B18-05 evaluator `analysis/b18_05_psi.py` and copies nothing
from it. One wrapped run through `analysis/b15_bound.py --seconds 60 --memory-mb 512`,
name `b19_05_control_20260915_01`: exit 0, wall 3.9 s, peak Job Object memory 37.6 MB.
Output `results/b19_05/control_full_support.json`
(SHA256 `d6d1c017f930af85481dcfafe79cc94fc2f59984582525c0783cd3bcd92ea162`); receipt
`results/logs/b19_05_control_20260915_01_resources.json`
(SHA256 `529853da908cc7fddecfa32a226fdfd00707efb5919973128305919fbc310924`).

**(A) The original control, reproduced exactly** (same `random.Random(1805)` stream,
after the two det4 draws it consumed): the sparse quartic has **46** nonzero
monomials out of 715, and of the five monomials `t^k x_1^(4-k)` only `t^4` is
present. Hence `p(t) = t^4` (coefficients low-to-high `0,0,0,0,1`), every
interpolated chart polynomial has degree 0, all eleven `E` are 0, `w·E = 0`,
`kappa·E = 0`. **The original control measured nothing**, exactly as Step 1 recorded.

**(B) Full-support quartics.** Three quartics in the ten chart variables with
**all 715** degree-4 monomials carrying a nonzero integer coefficient in `[-9,9]`,
`[t^4] = 1` (so `c = 1`, on chart), identity `M`, seeds 190501–190503. Size of what
was checked, per seed: all five `t^k x_1^(4-k)` monomials present; `p(t)` has
nonzero `t^0, t^1, t^2` coefficients (e.g. seed 190501:
`p = t^4 - 2016 t^2 - 31104 t - 186624`); interpolated degrees
`A:18, J2:17, J3:17, Q22:18, D_H:20, T2:18`; all eleven `E` values nonzero;
the ambient identity residual is 0 and `psi_direct = w·E` at every seed.

| seed | `w·E` | `kappa·E` |
|---|---|---|
| 190501 | `4839473560902601997041993972171460577182755285131437126272942080` (nonzero) | nonzero |
| 190502 | `-38668576973576082000957450265474957703355767212021520915847519928320` (nonzero) | nonzero |
| 190503 | `-6446625917823947507149396891377810711709707562163942977437696` (nonzero) | nonzero |

**(C) The det4 control, unchanged**: at a random `16 x 10` restriction of `det4`
all eleven `E` are 0 and `w·E = 0`, as in run 1.

**What this establishes (CERTIFIED).** `w·E` is a nonzero function on the ambient
chart: an exact nonzero rational value at an explicit point. So `w` is **not** an
ambient linear relation among the eleven `E` coordinates, and likewise `kappa`
is not. Combined with Step 2's global `Psi = w·E = 0` on the product family
`Y ⊇ X_pad`, the vanishing of `w·E` on padding is a genuine restriction
identity and not an artefact of a dependent basis: the rank-9 conclusion of
§2.6 is non-vacuous. This is a control on the premise, not a new bound; it does
not change `9 <= rank <= 10` into anything other than the exact 9 already proved
in Step 2, and it does not touch any multiplicity.

**What it does not establish.** Three nonzero values show `w·E` is not
identically zero; they say nothing about which other linear combinations of the
`E` vanish on the ambient space (none should, if the inherited independence of the
eleven-space holds, but that inheritance is B17-04's and is not re-proved here).
