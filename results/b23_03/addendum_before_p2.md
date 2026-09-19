# B23-03 addendum, written after pilot 1 and before pilot 2

The pre-registration snapshot (`preregistration_snapshot.md`, sha256
`3cb7b7c9c80e5dd9ef739b0d3a53d23c4e20a9123a06de0059c85555851b08df`, printed by pilot 1) is
not edited. This addendum records what pilot 1 changed and what pilot 2 will do. Its sha256 is
printed by pilot 2.

## What pilot 1 falsified

- **A3 and A4 (T3 smooth, `rank M_4 = 65` on T3): both false.** At four T3 points (two in normal
  form, two with random skew `Phi`), `dim (S/J_C)_k = 10` for every `k = 2..7` (mod `P`), and
  the exact `rank M_4 = 60`. T3's cubics are therefore **not** smooth. MEASURED: the profile is
  the Hilbert function of a length-10 singular scheme (the Segre-cubic profile). This is not
  used as a premise.
- **A6 (the `T1 ⊄ T2` certificate): not obtained.** The four S_3-symmetric `D35` cubics tried
  have `dim (S/J)_k = 17, 21, 25, 29` at `k = 4..7`, so they are singular along a curve. The
  symmetric construction is too special. It is disclosed and not used.

## New hand theorem, found after pilot 1: T3 ⊆ T2

For the normal form `A(x) v = y' (x) v'' - v' (x) y'' + t B v` and `phi = alpha (x) beta` in
`(U' (x) U'')^*`,

`phi(A(x) v) = alpha(y') beta(v'') - alpha(v') beta(y'') + t phi(B v)`. So the `v'`-part of the functional
`phi o A(x)` is `-beta(y'') alpha + t (B^T phi)'` and the `v''`-part is
`alpha(y') beta + t (B^T phi)''`. If `(B^T phi)' = c_1 alpha` and `(B^T phi)'' = c_2 beta`, both
parts vanish on the 3-dimensional subspace
`P_phi = { beta(y'') = c_1 t, alpha(y') = -c_2 t }`. That subspace is not contained in `{t = 0}`,
and on it the constant row vector `phi` kills `A(x)`. So `det A = 0` on `P_phi` and `C` contains
the plane `P(P_phi)`. The two conditions on `(alpha, beta) in P^1 x P^1` are forms of bidegree
`(2,1)` and `(1,2)` with intersection number `2·2 + 1·1 = 5 > 0`, so a solution always exists.
Hence every normal-form T3 cubic lies in `Sigma_Pi`. The normal forms are dense in T3, and T2 is
closed, so **T3 ⊆ T2**. Consequently `closure(D45° ∩ P5) = T1 ∪ T2`, and the cap minors vanish on
T3 (`rank M_4 <= 64` holds on all of `Sigma_Pi`).

## Pilot 2 plan (a disclosed deviation: pilot 2 now also carries Question A items)

- **F1 — `T1 ⊄ T2` certificate, general construction.** Six rank-one matrices summing to zero,
  made from two rank-one decompositions of one invertible `3 x 3` integer matrix `X`:
  `X = sum_i u_i v_i^T = sum_j w_j z_j^T`. Take `M(x) = sum_{i<=5} x_i R_i`; the sixth point is
  `-(1,...,1)`, so the points are in linearly general position by construction. Prediction:
  `dim (S/J)_6 = dim (S/J)_7 = 6`. By Gotzmann, `Sing` is then six reduced points, none four
  coplanar, so the cubic contains no plane.
- **F2.** A sanity check of the theorem above at a `B` whose row `(11)` is `(c1, 0, c2, 0)`: `C`
  should vanish on `{x2 = B00 t, x0 = -B02 t}`.
- **Question B** as pre-registered (§1.3 of the snapshot). Determinant floors run before padding
  measurements, and the padding measurements stop at about 45 s.
