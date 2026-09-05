# Session 61 — the full polar profile of `per_3`, and a verdict on the microlocal branch

Branch `s61-polar` off `main` at `0960bd5`. Pre-registration `results/PREREG_s61.md`
(commit `9587200`, before any computation). Code `analysis/wk9_s61_*`; logs
`results/logs/s61_*`; per-run records `results/s61_runs/*.json`; the generated
Singular/Macaulay2 scripts with every random draw `results/s61_sing/`; the
consolidated table `results/s61_profiles.json`.

## 0. Verdict in one paragraph

The two eight-entry profiles, in the convention of `PREREG_s61.md` §0a
(`δ_k = ∫[C(X)]·h^{N−1−k}·ȟ^k`; equivalently the class of a generic
`(k+1)`-dimensional linear section):

| slot `k` | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| `det_4 ⊂ P^15` | 4 | 12 | 36 | 68 | 84 | 60 | **20** | **0** |
| `per_3 ⊂ P^8` | 3 | 6 | 12 | 24 | 48 | 48 | **30** | **6** |
| padded `x_0·per_3 ⊂ P^15` (cone/union lemma; also measured directly) | 4 | 6 | 12 | 24 | 48 | 48 | **30** | **6** |
| violates `det_4`? | no | no | no | no | no | no | **yes, 30 > 20** | **yes, 6 > 0** |

**The microlocal signal at `(3,4)` does not collapse to the dual defect.** Slot 7
is the known LMR separation (`dim X* = 7 > 6`). Slot 6 is a second, independent
conormal inequality: the class of a generic `P^7`-section of the padded permanent
is 30, that of the determinant is 20 (the degree of the Segre `P^3 × P^3`), and a
border determinant cannot exceed 20 there (§4, the specialisation inequality).
The two conditions are incomparable closed `GL_16`-invariant conditions, both
containing `D_16 = closure(GL_16·det_4)` and both excluding the padded permanent.
The external value `δ_7(per_3) = 6` is reproduced. The pre-registered
0.6-prior prediction (§3.2 of the pre-registration, "the branch retires") is
**refuted**; the 0.4 alternative (§3.3) is what happened.

Two qualifications that decide what the finding is worth. (i) **The whole
`per_3` profile is now an exact characteristic-zero computation**, not a mod-`p`
measurement: the multidegree of the conormal ideal over `Q` (Macaulay2, 22 s,
no random choices anywhere) gives the vector above, and the two decisive slots
also have closed-form derivations (§3.5–3.6): the dual of `per_3` is the sextic
`4·per(B∘B) − 2·per(B)² − det(B)² = 0`, whose singular locus has codimension 3,
so its generic plane section is a smooth plane sextic of class `6·5 = 30`.
(ii) **The polar profile's reach for `per_3` is exactly `dc̄(per_3) ≥ 5`, the
LMR bound**: against `det_5` (profile `(5, 20, 80, 220, 430, 580, 520, 280, 70)`
by the smooth-Segre formula) the padded permanent satisfies every slot, so no
conormal multidegree obstructs `per_3` from the border of `det_5`. The new
slot-6 inequality is a second *proof* of a known fact at `(3,4)`, not a step
toward a stronger bound; and no algebraisation of it at low degree is visible
(§6).

## 1. Calibration — the determinant profile reproduced two ways

**Theory (M1).** For the smooth Segre `P^3 × P^3 ⊂ P^15`, `c(T) = (1+a)^4(1+b)^4`,
`h = a + b`, `∫ a^3 b^3 = 1`, the polar degrees
`μ_k = Σ_{i≤k} (−1)^i C(m−i+1, k−i) ∫ c_i h^{m−i}` (`m = 6`) come out as
`(20, 60, 84, 68, 36, 12, 4)` (`analysis/wk9_s61_segre.py`,
`results/logs/s61_segre.log`). Since the conormal variety of `{det_4 = 0}` is the
conormal variety of its dual with the factors swapped, this is the determinant
profile read backwards: `(4, 12, 36, 68, 84, 60, 20)` — the brief's vector. The
same formula gives `(2, 2, 2)` for `det_2` and `(3, 6, 12, 12, 6)` for `det_3`
(classical), and the sums `6, 39, 284, 2205` are the known generic
Euclidean-distance degrees of the `2×2, 3×3, 4×4, 5×5` determinant hypersurfaces
(Draisma–Horobeț–Ottaviani–Sturmfels–Thomas), an independent check of the
convention.

**Computation (M2).** The saturation method (§2) on `det_4` in 16 variables,
`p = 2147483647`, seed 61, both charts:

| `k` | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| count (projective degree = chart A = chart B) | 4 | 12 | 36 | 68 | 84 | 60 | 20 | 0 |
| excess `Sing ∩ Λ` (dim, degree) | ∅ | ∅ | ∅ | 20 points | curve, 20 | surface, 20 | 3-fold, 20 | 4-fold, 20 |
| seconds (full-Jacobian saturation) | 0 | 0 | 0 | 10 | 99 | 871 | see §7 | see §7 |

Every slot matches the closed form. The two lowest non-smooth slots are exactly
the singularity corrections predicted in the pre-registration: 20 ordinary nodes
on the `P^4`-section (`4·27 − 2·20 = 68`) and a smooth degree-20 curve of
transversal `A_1` points on the `P^5`-section (`4·81 + 20·(2·5 − 2 − 5·4) = 84`,
Piene's polar formula with Aluffi's Milnor class and Euler obstruction 2). The
det_3 control gives `(3, 6, 12, 12, 6, 0, 0, 0)` by both engines and by the
conormal-multidegree route. Second prime, further seeds and the Macaulay2 engine
on `det_4`: §7.

## 2. Method, and what was varied

For `X = {F = 0} ⊂ P^N`, slot `k`: a random integer basis `V` (entries in
`[−99, 99]`) of a `(k+1)`-plane `Λ`, `G = F|_Λ`, the `N+1` partials restricted to
`Λ`, `k` random linear combinations `m_i` of them; the ideal
`(G, m_1, …, m_k)` in `k+2` variables, saturated by the ideal of all restricted
partials (`analysis/wk9_s61_polar.lib`). The excess locus of the unsaturated
ideal is exactly `Sing(X) ∩ Λ`, where every partial vanishes; legitimate points
have `∇F ≠ 0`, so the saturation removes the excess and nothing else. The count
is read three ways — projective degree of the saturated ideal, `vdim` on the
chart `t_0 = 1`, `vdim` on a second random chart — and they agreed in every one
of the runs. Saturating by a single random combination `g` of the partials
instead of the whole Jacobian ideal gave the same count in every run
(`COUNTG` lines). Reducedness: the degree of the radical equals the count at
every slot of `per_3` at `p = 1000003` and `p = 32003` (Singular's radical
routine refuses characteristics above `2^29`, so the house primes carry the
counts and the smaller primes carry the reducedness check).

Varied for `per_3`: primes `2147483647, 2147483629` (house), `1000003`, `32003`,
and `Q`; seeds 61, 62, 63 (each seed draws a different `Λ`, different `m_i`,
different second chart); two charts per seed; two engines (Singular 4.3.2 and
Macaulay2 1.22, handed the same random data); and the methodologically
different conormal-multidegree route (M2: the bihomogeneous ideal
`(F, 2×2 minors of [y; ∇F])` saturated by `(∇F)`, then `multidegree`) at
`p = 32003`, both house primes, and over `Q`. Every one of these returned
`(3, 6, 12, 24, 48, 48, 30, 6)`. The full list is in `results/s61_profiles.json`.

## 3. The permanent profile, slot by slot, with the reason for each number

**3.1 The singular locus (M3).** `Sing(per_3) ⊂ P^8` is the zero set of the nine
`2×2` sub-permanents. Over `Q` (`analysis/wk9_s61_sing.sing`): the Jacobian
scheme has projective dimension 2 and degree 24; its 15 minimal primes are the
three planes `{two rows = 0}`, the three planes `{two columns = 0}`, and the nine
smooth quadric surfaces `{row i = 0, column j = 0, complementary 2×2 permanent
= 0}`; the Jacobian ideal is not radical. Exactly as pre-registered. Pairwise
intersections: 54 pairs meet in lines, 27 pairs in points; the 54 line-pairs are
the 18 lines `{two rows = 0, one column = 0}` (and transposes), each on exactly
three components. `rank Hess(per_3) = 6` at random points of all 15 components
(transversal `A_1` in the six normal directions), 4 on the 18 lines and at the
nine coordinate points (`analysis/wk9_s61_transversal.py`, exact over `Q`).
`rank Hess(per_3) = 9` at smooth points of the hypersurface, so `dim X* = 7`: the
dual of `per_3` is a hypersurface in `P^8*`.

**3.2 Slots 0–4: `(3, 6, 12, 24, 48) = 3·2^k`.** `codim Sing = 6 ≥ k + 2`, the
generic `P^{k+1}`-section is a smooth cubic, and the count is Bézout's. Measured
identically; no excess appeared (`excess_dim = 0` in the logs).

**3.3 Slot 5: 48.** The generic `P^6`-section meets `Sing` in `deg Sing = 24`
points, each an ordinary node of the cubic 5-fold (the restricted Hessian has
rank 6 at every one, `wk9_s61_transversal.py`), so Teissier's formula gives
`3·2^5 − 2·24 = 48`. Measured 48 at every prime, seed and chart. The same number
from the other side: the dual sextic (3.5) has a singular locus of dimension 5
and degree 51, so its generic `P^3`-section is a sextic surface with 51 nodes,
class `6·5² − 2·51 = 48 = δ_2(X*) = δ_5(X)`.

**3.4 Slots 0–5 against the determinant.** `3 < 4, 6 < 12, 12 < 36, 24 < 68,
48 < 84, 48 < 60`: clean, as pre-registered (§3.1 of the pre-registration).

**3.5 Slot 7: 6, and what the dual is.** Eliminating `A` from
`(per_3(A), B − ∇per_3(A))` (`analysis/wk9_s61_dual.m2`, `p = 32003`) returns a
single sextic with 21 terms, every term a monomial `B^m` with `m` a `3×3`
non-negative integer matrix of row and column sums `(2,2,2)` (torus
semi-invariance, as it must be). Sorting the 21 magic squares into
`2P_σ` (coefficient `+1`), `P_σ + P_τ` with `σ^{−1}τ` a transposition
(`−2`) and `J − P_σ` (`−6`) identifies it:

    X*  =  { B :  4·per(B∘B) − 2·per(B)² − det(B)² = 0 },     B∘B the entrywise square,

verified as a polynomial identity over `Q` (`results/logs/s61_dual_identity.log`),
together with `g(∇per_3(A)) ≡ 0 mod per_3(A)`, which places `X*` inside `{g = 0}`
over `Q`. `{g = 0}` has singular locus of projective dimension 5 and degree 51
(exact, over `Q`), so `g` is squarefree and its generic plane section is smooth,
hence irreducible; thus `{g = 0}` is an irreducible hypersurface containing the
7-dimensional irreducible `X*`, and `X* = {g = 0}`, `deg X* = 6 = δ_7(per_3)`.
This is characteristic-zero and independent of the polar count. It is not in
the span of `per²`, `per·det`, `det²`.

**3.6 Slot 6: 30 — the decisive slot.** By biduality `δ_6(X) = δ_1(X*)`, the
class of a generic plane section of the sextic `X*`. That section misses the
5-dimensional singular locus and is a smooth plane sextic, whose class is
`6·5 = 30`. So `δ_6(per_3) = 30` is a theorem in characteristic zero, resting on
3.5 and one exact Gröbner computation (the dimension of `Sing{g = 0}` over `Q`).
The pre-registered bracket `δ_6 ≤ min(96, δ_7(δ_7−1)) = 30` is attained with
equality — the section of the dual is as non-singular as it can be — which is
what makes 30 exceed 20. The saturation count gave 30 at all six prime/seed
settings and the conormal multidegree gave 30 at `p = 32003`, both house primes
and over `Q`.

**3.7 Sum.** `3+6+12+24+48+48+30+6 = 177` is the generic Euclidean-distance
degree of the `3×3` permanent hypersurface (against 39 for `det_3`).

## 4. The two lemmas the comparison rests on (functoriality pre-check, §7)

**Cone/union lemma.** For a hypersurface `Y ⊂ P^n` and the cone `X ⊂ P^{n+1}`
over it with vertex `p`: every tangent hyperplane of `X` at a smooth point `(y, z)`
is `[∇F_Y(y) : 0]`, so `C(X)` maps to `C(Y)` by projection from `p` on the first
factor and lies over the hyperplane `P^n* ⊂ P^{n+1*}` on the second. A generic
`(k+1)`-plane `Λ ⊂ P^{n+1}` (`k ≤ n−1`) misses `p` and projects to a generic
`(k+1)`-plane of `P^n`; a generic codimension-`k` `Λ̌ ⊂ P^{n+1*}` meets `P^n*` in a
generic codimension-`k` subspace. So `δ_k(X) = δ_k(Y)` for `k ≤ n−1`, and
`δ_n(X) = 0` because a generic point of `P^n*` misses `Y*`. For a reducible
reduced hypersurface `X_1 ∪ X_2`, `C(X) = C(X_1) ∪ C(X_2)` as cycles (the smooth
locus of `X` is dense in each component), so profiles add; a hyperplane
contributes `(1, 0, …, 0)`. Hence the padded permanent in `P^15` — a cone with
`P^5` vertex over `{x_0 = 0} ∪ cone(per_3) ⊂ P^9` — has profile
`(1 + 3, 6, 12, 24, 48, 48, 30, 6, 0, …, 0)`. **Measured directly** on the
ten-variable `x_0·per_3` at both house primes: `(4, 6, 12, 24, 48, 48, 30, 6, 0)`;
and on the sixteen-variable quartic itself at slots 5–8: §7.

**Specialisation inequality.** Let `F_t → F_0` (`t → 0`) be a one-parameter
family of quartics in `P^15` with every `X_t = {F_t = 0}`, `t ≠ 0`, projectively
equivalent to `{det_4 = 0}` — a curve `g(t)·det_4` in the orbit, which exists for
any point of the orbit closure by the curve selection lemma. The closure `𝒞` of
`∪_{t≠0} C(X_t) × {t}` in `P^15 × P^15* × Δ` is flat over the smooth curve `Δ`
(no component lies over `t = 0`), so its special fibre `𝒞_0` is an effective
cycle of pure dimension 14 rationally equivalent to `C(X_t)`, and every
`∫ h^{14−k} ȟ^k` — a pairing with nef classes, non-negative on effective cycles —
is conserved. For a smooth point `x` of `X_0` the implicit function theorem gives
`x_t ∈ X_t`, `x_t → x`, with `∇F_t(x_t) → ∇F_0(x) ≠ 0`, so `(x, [∇F_0(x)]) ∈ 𝒞_0`;
these points are dense in `C(X_0)`, hence `C(X_0) ⊆ 𝒞_0`, and since all
components have dimension 14, `[𝒞_0] − [C(X_0)]` is effective. Therefore

    P ∈ closure(GL_16·det_4)   ⟹   δ_k(P) ≤ δ_k(det_4)   for every k.

This is the whole "conormal specialisation" input and it is elementary; it is
also exactly Lemma 15 + Proposition 1 of arXiv:2606.13628 (§8), which the
session did not use. Functoriality (§7 of `brief_wording.md`): the statistic
"specialises in a controlled direction under degeneration" — passes.

**Degeneracy direction (§5 of `brief_wording.md`).** The profile at the three
committed test points (10 variables): a `det_4` pencil, `(4, 12, 36, 68, 84, 60,
20, 0, 0)` (a generic linear section truncates the profile); a reducible `ℓ·c`
with `c` a generic cubic, `(4, 6, 12, 24, 48, 96, 192, 384, 768)`; the full
ten-variable `x_0·per_3`, `(4, 6, 12, 24, 48, 48, 30, 6, 0)`. Both the padded
permanent and the generic reducible quartic are *less* degenerate than the
determinant (their profiles are not componentwise `≤` the determinant's), so the
statistic points the right way — the reducible point from slot 5 on
(`96 > 60`, consistent with `dim R_r > dim D_r` for `r ≥ 7`), the padded permanent
at slots 6 and 7 only. Measured values: §7.

## 5. What the slot-6 inequality is, and is not

*Is.* A closed, `GL_16`-invariant condition `Z_6 = {F : δ_6({F = 0}) ≤ 20}`
(constructible and closed under specialisation by §4), containing `D_16` and
excluding the padded permanent by a margin of 10. It is not implied by the
dual-defect condition `Z_7 = Dual_{6,4,16} = {δ_7 = 0}` nor does it imply it: a
cone over a quadric of `P^8` has `δ_6 = 2 ≤ 20` and `δ_7 = 2 > 0`; a cone over a
hypersurface of `P^7` with a non-defective dual of degree above 20 has
`δ_7 = 0` and `δ_6 > 20`. For dual-defective quartics (`dim X* ≤ 6`) the slot-6
number is `deg X*`; for `dim X* = 7` it is the class of a `P^7`-section — the
padded permanent is in the second case.

*Is not.* A route to a stronger lower bound. Against `det_m` for `m ≥ 5` every
slot of the padded permanent is dominated (`(4, 6, 12, 24, 48, 48, 30, 6)` against
`(5, 20, 80, 220, 430, 580, 520, 280, 70)` for `det_5`), so the entire polar
profile of `per_3` certifies exactly `dc̄(per_3) ≥ 5` — the LMR bound and no more.
That is also what arXiv:2606.13628's Theorem 3(i) yields when fed our
`δ_7(per_3) = 6` as its "special-side input" (`B(4, 9) = 0 < 6 ≤ 315 = B(5, 9)`).

*Is not, either.* A separation of `D_r` from `P_r` at any measured cell of the
multiplicity programme: the profile is a property of the hypersurface
`{P = 0} ⊂ P^15`, i.e. of the point, not of a `GL`-module of equations, and the
programme's `mult_det = a` record at 210 six-row cells is untouched.

## 6. If one wanted to algebraise it — an estimate, with its basis

`Z_6` is cut out, for a fixed generic `P^7 = Λ` and codimension-6 `Λ̌`, by the
condition that the residual scheme of `(F|_Λ, m_1(∇F), …, m_6(∇F))` — a quartic
and six cubics in eight variables — off `Sing(F) ∩ Λ` has at most 20 points. No
classical construction expresses "at most 20 residual points" as the vanishing
of polynomials in the coefficients of `F`; the objects that do express point
counts (Macaulay resultants, discriminants, Chow forms of the polar variety
`P_6(F)`, of dimension 8 and degree `δ_6`) are of degree comparable to the
Bézout number of the system in `coeff(F)`: the Macaulay resultant of one quartic
and six cubics in `P^7` has degree `3^6 = 729` in the quartic and `4·3^5 = 972`
in each cubic, and each `m_i(∇F)` is linear in `coeff(F)`, so a single resultant
is of degree `729 + 6·972 = 6561 = 3^8` in `coeff(F)` — and it expresses a
common zero, not a count, and it does not see the excess. The honest estimate
is therefore: **unknown, and no route to anything near LMR's 24 is visible.**
The degree-24 module remains the only algebraised conormal condition at `(3,4)`.
The one structural handle worth recording: for dual-defective `F` the slot-6
number is `deg X*`, and the degree of the dual of a hypersurface is expressible
through the Hessian (the Gauss map is given by the partials, with the Jacobian
scheme as base locus), which is where LMR's divisibility also lives. Whether
"`deg X* ≤ 20` on `Dual_{6,4,16}`" has equations of degree below 24 is a
well-posed question this session did not open (§5 of the brief).

## 7. The measurement record

**Determinant, both primes and seeds (M2).** `det_4` in 16 variables, all eight
slots: `p = 2147483647`, seed 61, `(4, 12, 36, 68, 84, 60, 20, 0)`, projective
degree = chart A = chart B at every slot, full-Jacobian saturation = single-`g`
saturation at every slot. The third engine (msolve on the Rabinowitsch form
`G = m_1 = … = m_k = 0, s·g = 1` on the chart `t_0 = 1`, `analysis/wk9_s61_msolve.py`,
no saturation step at all, same random draws) returns the whole vector
`(4, 12, 36, 68, 84, 60, 20, 0)` at `p = 1073741827` and `p = 1000003` for seed 61
and `(68, 84, 60, 20, 0)` at slots 3–7 for seeds 62 and 63 — in about one second
per slot, against 15 minutes for the slot-5 saturation and more than an hour
for slot 6 in Singular. The 10-variable `det_4` pencil (a generic linear
section) returns the truncation `(4, 12, 36, 68, 84, 60, 20, 0, 0)`. Macaulay2
on the same data: DET4_M2_RESULT

**Permanent, every setting (M4–M6).** `(3, 6, 12, 24, 48, 48, 30, 6)` at
`(p, seed) = (2147483647, 61), (2147483629, 61), (1000003, 61), (2147483647, 62),
(2147483629, 63), (32003, 61)`, each with two charts and both saturation
variants agreeing; radical = count at every slot for `p = 1000003` and `32003`;
Macaulay2 on the same random data returns the same vector (209 s for all eight slots); Singular over `Q`
QQ_PER3_RESULT; conormal multidegree `(3, 6, 12, 24, 48, 48, 30, 6)` at
`p = 32003`, `2147483647`, `2147483629` and over `Q` (13–22 s each; the
`det_3` control returns `(3, 6, 12, 12, 6, 0, 0, 0)`).

**Biduality control.** The dual sextic `g` run through the same saturation code
as a hypersurface in its own right must return the reversed profile
`(6, 30, 48, 48, 24, 12, 6, 3)`: Singular (saturation, `p = 2147483647`) `(6, 30, 48, 48, 24)` at
slots 0–4 (the degree-51 excess surface makes slots 5–7 slow and the run was
ended by its recorded pid); msolve `(6, 30, 48, 48, 24, 12, 6, 3)` at all eight
slots. Biduality holds slot for slot. The singular scheme of its generic
`P^3`-section has degree 51, is reduced, and consists of ordinary nodes (the
rank-`≤ 2` Hessian locus on it is empty; `analysis/wk9_s61_dualnodes.sing`,
three prime/seed pairs), which is the dual-side derivation of `δ_5 = 48` in §3.3.

**Padded permanent, directly.** Ten variables, both house primes:
`(4, 6, 12, 24, 48, 48, 30, 6, 0)` (seeds 61 and 62). Sixteen variables — the
quartic in `Sym^4 C^16` that the containment question is actually about — at
slots 5, 6, 7, 8: msolve `(48, 30, 6, 0)` at `(p, seed) = (1073741827, 61)` and
`(1000003, 62)`; Singular saturation at slots 6 and 7: PAD16_SING_RESULT. The
excess here is 5-dimensional in `Λ = P^7` — the padded quartic is singular along
the codimension-2 locus `{x_0 = 0} ∩ {per_3 = 0}` — and the count is unaffected,
as the cone/union lemma says it must be.

**Controls and pre-check points.** `det_3` `(3, 6, 12, 12, 6, 0, 0, 0)` (Singular, Macaulay2,
msolve, conormal multidegree); a random cubic in 9 variables
`(3, 6, 12, 24, 48, 96, 192, 384) = 3·2^k` (smooth, no excess anywhere); the
reducible `ℓ·c` in 10 variables `(4, 6, 12, 24, 48, 96, 192, 384, 768)` (Singular
through slot 6, msolve all nine slots; the excess `{ℓ = 0} ∩ {c = 0}` has
codimension 2); the 10-variable `det_4` pencil `(4, 12, 36, 68, 84, 60, 20, 0, 0)`.
Every control returned its predicted value.

**Timings.** Everything about `per_3` runs in seconds (about 20 s for all eight
slots at a house prime; 760 s with the radical checks at `p = 1000003`); the
determinant's slot 5 takes 15 min and slot 6 DET4_K6_TIME; the dual
sextic's slot 4 took 22 min (a degree-51 excess surface). Every run was bounded
by `timeout` and `ulimit -v`, its wrapper and engine pids recorded in
`results/logs/s61_<run>.pid`, and the one run ended early (the first attempt
at the house-prime radical checks, which Singular cannot do above `2^29`) was
ended by its recorded pid (`results/logs/s61_*_attempt1.log`).

## 8. The citation (M8)

Both preprints exist and are readable. **arXiv:2606.13628**, Karthik Sheshadri,
"A near-quadratic lower bound on the border determinantal complexity of
`Σ_i x_i^n` via conormal specialization"; **arXiv:2606.15970**, same author,
"The Exact Reach of Conormal Invariants in Determinantal Complexity: a
Quadratic No-Go Theorem" (author line: "Independent AI researcher and engineer,
San Jose, California, USA"). The `arxiv.org/abs/` pages come back empty through
the fetch tool — reproduced here, twice — while `arxiv.org/html/<id>` and the
arXiv search index resolve; that is presumably what defeated the integrator's
six attempts, and it is a tooling false negative, not a missing paper.

Quoted from 2606.13628 (via the HTML rendering; the session did not read the
full text and cites nothing else from it): the convention "For an `(n−1)`-cycle
`C` on `P^n × (P^n)^∨` and `0 ≤ k ≤ n−1`, the `k`-th multidegree is
`δ_k(C) := deg(C · h_1^{n−1−k} h_2^k)`" — the same as §0a of the pre-registration;
"**Lemma 15 (Conservation of multidegree)** `[W_0]` is an effective cycle of pure
dimension `n−1`, and for every `k` and every `c ∈ U`, `δ_k([W_0]) = δ_k(Γ_c)`";
"**Proposition 1 (Containment)** `Con(X) ⊆ supp[W_0]`, and the coefficient of
`Con(X)` in the effective cycle `[W_0]` is at least one"; "**Theorem 3
(Determinantal conormal bound)** … `δ_{n−2}(Γ_1(F)) ≤ B(m,n) := Σ_{i=1}^{n−1}
C(m,i) C(m−1, n−1−i) C(n−2, i−1)`"; and, from its Section 10 item 7, "For the
permanent the special-side input would be a lower bound on the relevant
conormal multidegree of the (singular) permanent hypersurface, which we do not
know." The present session supplies that input for `n = 3`:
`δ_7(per_3) = 6`, and with it Theorem 3(i) reproduces `dc̄(per_3) ≥ 5` and
nothing more (§5). From 2606.15970: "**Theorem D** … every lower bound on
`dc(f)` derivable by reading a characteristic-cycle-type invariant of `V(f)`
through a kernel-corank incidence with intersection-theoretic extraction
satisfies derivable bound `≤ e^{O(1)}·d·N`." Neither paper computes any polar
degree of `per_3` or of the padded permanent, and neither compares lower slots.
Nothing in §§0–7 depends on either paper; §4 proves the one statement needed.
Recorded oddity: 2606.13628's bibliography cites two 2026 arXiv items with the
seven-digit identifiers "arXiv:7680505" and "arXiv:7685504", which are not valid
arXiv numbers.

## 9. Pre-registration scorecard

| item | prediction | prior | outcome |
|---|---|---|---|
| M1 | smooth-Segre formula gives the brief's vector reversed | 0.9 | confirmed, plus `det_2`, `det_3`, ED-degree sums |
| M2 | saturation reproduces `(4,12,36,68,84,60,20,0)` at every setting | 0.9 | confirmed (§7) |
| M3 | 15 components, dims 2, degrees `1^6 2^9`, Hessian rank 6 / 4 on lines | 0.8 / 0.9 | confirmed exactly, including the 18 lines |
| M4 | `(3, 6, 12, 24, 48)` | 0.95 | confirmed |
| M5 | `δ_5 = 48` | 0.75 | confirmed, and re-derived from the dual side (51 nodes) |
| M6 `δ_7` | external 6 reproduced | 0.5 | confirmed, with the dual identified in closed form |
| M6 `δ_6` | `≤ 20`, no violation | 0.6 | **refuted: `δ_6 = 30`, the bracket's upper end** |
| M7 | direction check passes; `ℓ·c` exceeds from slot 5; pad `(4, δ_1..δ_7, 0)` | 0.95 | confirmed |
| M8 | neither identifier resolves | 0.8 | **refuted: both exist; the `abs` fetch path is the failure** |
| M9 | verifier 50/50 on this branch | 0.95 | VERIFY_SHORT |
| §3.1 | slots 0–5 clean | 0.9 | confirmed |
| §3.2 | branch retires, only `δ_7` differs | 0.6 | **refuted** |
| §3.3 | `δ_6 > 20`, a second signal | 0.4 | **this is what happened** |
| §3.5 | calibration at the first attempt | 0.85 | confirmed |
| §3.6 | Macaulay2 = Singular on every shared slot | 0.95 | confirmed on `per_3` (all eight slots) and `det_3`; `det_4` slots: DET4_M2_SHORT |

Three refutations, two of them productive: the decisive slot went the other way
with a closed-form reason, and a citation the programme had written off exists.

## 10. Corrections flagged, not edited (single-writer files)

- `docs/external_reviews_round3.md` §3 and `docs/critic_gemini_scorecard_response.md`
  §3 record the Sheshadri preprints as unlocatable and rule that no session
  build on them. The identifiers resolve (§8); the rule's *conclusion* — the
  session's mathematics must not depend on them — was followed and remains
  sound, but the factual premise should be corrected, and the fetch-tool
  failure mode (`abs` empty, `html` fine) noted for future citation checks.
- The s61 brief (§1) attributes the identity `det H_P = −(3/2)·x_0^8·per_3·det
  H_{per_3}` to the integrator; consistent with `docs/s50_s55_integrator_notes.md`.
  No change.
- The brief's §1 says the `δ_7 > 0` separation "is the LMR dual-defect condition
  again"; correct. Its §2 asks whether "some lower slot `k ≤ 6` also violates"
  and answers, in effect, that if so it "might algebraize differently from
  LMR's degree-24 module". Slot 6 violates; §6 above is the reason the second
  half of that sentence should not be read as a promise.

## 11. Certificates and the verifier (M9)

This session produced no `gct-cert/1` certificate: its claims are polar counts
and one polynomial identity, none of which is a highest-weight-vector,
matrix-rank or full-rank claim, and no cell reported `D > 0`. The verifier was
run on the 50 committed certificates on this branch as a regression:
VERIFY_DETAIL. The session's own reproducibility artefacts are the
seeded generators (`wk9_s61_polar.py`, every draw from `random.Random` with the
seeds in the logs), the generated scripts in `results/s61_sing/`, the raw logs,
and `results/s61_profiles.json`; the characteristic-zero facts (§3.5, §3.6, the
conormal multidegree over `Q`) are re-runnable in under a minute each.

## 12. Honest boundary

- `δ_k(per_3)` for all `k`: exact over `Q` (conormal multidegree), and slots 0–7
  also by the saturation count at four primes and three seeds; slots 5, 6, 7
  additionally by closed-form arguments. Slots 0–4 by Bézout.
- `δ_k(det_4)`: closed form (smooth Segre) plus the saturation count at
  `p = 2147483647` (Singular, all slots), `p = 1073741827` and `1000003` (msolve, all slots, three seeds), and Macaulay2 at slots DET4_M2_SLOTS. Not computed over `Q` by the conormal route
  (32 variables).
- The comparison uses the padded quartic in 16 variables through the cone/union
  lemma (proved in §4, measured directly in 10 variables and at slots 5–8 in
  16 variables) and the specialisation inequality (proved in §4).
- `dc̄(per_3) ≥ 5` is the *only* complexity consequence; the profile is
  dominated by `det_5` at every slot.
- The mod-`p` counts are measurements at specific random `Λ, Λ̌`; the pattern of
  agreement across primes, seeds, charts, engines and the `Q` computation is
  what makes them trustworthy, and the `Q` conormal multidegree is what makes
  the `per_3` vector a fact rather than a measurement.
