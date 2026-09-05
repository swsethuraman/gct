# The equation census: what is known below degree 24, at `n = 4`

Session 55, branch `s55-census`, off `main` at `eb8cecb`.
Pre-registration: `results/PREREG_s55.md`, committed before any computation.
Measurements: `analysis/wk9_s55_{lmrweight,ranks,ranks2,sing,gauss,macaulay,checks}.py`,
logs `results/logs/s55_{lmrweight,ranks,ranks2,sing,gauss,macaulay,checks}.log`.

The object throughout is

    D_r  =  closure { det_4(s_1 A_1 + ... + s_r A_r) }  in  Sym^4 C^r,

and "degree" always means degree **in the coefficients of the quartic**, never
degree in `s` and never the size of a matrix of linear forms.

---

## 0. The answer in three lines

1. **Nothing below 24 was found**, in the literature or by re-derivation, in any
   of the fourteen rows below. This is a survey result, not a lower bound: no
   theorem of the form "no equation of degree `< X` exists" is known for
   `I(D_r)` or for `Dual_{k,d,N}`, and a search for one came up empty.
2. **24 is the exact floor of the dual-degeneracy family at `n = 4`**, and this
   is now argued rather than assumed (§2.3). The argument needs *two* facts, not
   one: the containment bound `k >= dim X^*(det)` and the non-vacuity bound
   `k <= r-3`. Together they exclude the family entirely for `r <= 8` and fix its
   minimum at 24 for `r >= 9`.
3. **The brief's table compares numbers from different cells.** The LMR module
   has `ell(lambda) = 9` and is *identically zero* on `Sym^4 C^r` for `r <= 8`.
   Our measured range `delta <= 9` is at lengths 5 and 6. So the gap is not
   "24 against 9" in one place; it is 24 at length 9 against 9 at lengths 5–6,
   and no experiment the programme has run compares them.

---

## 1. The census

Columns: construction; reference; lowest degree at `n = 4`; **E**xplicit or
**Ex**istential; **P**roved or **M**easured; and whether the
degeneracy-direction pre-check (`docs/brief_wording.md` §5) passes — i.e.
whether the statistic is strictly *more* degenerate at `det_4` than at the full
ten-variable `l·per_3`.

| # | construction | reference | lowest degree at `n = 4` | E/Ex | P/M | §5 check |
|---|---|---|---|---|---|---|
| 1 | LMR dual-degeneracy module, `k = 6` | LMR Thm 2.3.1 | **24**, for every `r >= 9`; **no equation at all for `r <= 8`** | E (module + explicit divisibility test) | P | **passes**, margin 1 |
| 2 | the rest of the LMR family, `k > 6` | LMR Thm 2.3.1 | `3(k+2)`: 27, 30, … | E | P | **fails from `k = 7` on** |
| 3 | Mignon–Ressayre, converted to equations | MR 2004; LMR §2 | **24** by the binary-division route; `817199` by naive ideal membership at `r = 10` | E | P | passes (it *is* row 1) |
| 4 | "Landsberg–Ressayre Cayley–Bacharach" | — | **no such method exists** | — | — | — |
| 5 | Alper–Bogart–Velasco singular locus → the discriminant | ABV Thm 1.2; GKZ | `r·3^{r-1}`: **405** at `r=5`, 1458 at `r=6`, 196830 at `r=10`; nothing at `r=4` | E, classical | P | **fails** |
| 6 | middle catalecticant `Cat_{2,2}` | Landsberg–Ottaviani; **our s35** | **37** for `r >= 9`; vacuous for `r <= 8` | E | M (exact, `Q` + two primes) | **fails**, 36 vs 18 |
| 7 | `Cat_{1,3}`, and the Koszul flattening `Λ^1` | Landsberg–Ottaviani | **vacuous** — rank 10 and 99 at all four test points | E | M | n/a |
| 8 | Koszul–Young, border-rank route | Farnsworth 2016 | threshold `R >= 38`, so minors of size `>= 39` | Ex | P | fails, same mechanism as 6 |
| 9 | Hüttenhain–Lairez boundary, `n = 3` | H–L 2016 | **no equations**; the boundary lies *inside* the orbit closure | — | — | — |
| 10 | the same at `n = 4` | — | **not done**; open, and stated as open in the literature | — | — | — |
| 11 | Plücker / common isotropic 4-plane | s53 draft (superseded) | **unknown**; the only calibration is `r = 4`, where the pencil elimination is 320112 | Ex | — | ill-posed: not a function of the quartic |
| 12 | Macaulay minors (ours) | s44/s48/s49 | 300 at `r=5`; 661 certified / 1148 proved at `r=6` | E | M/P | **fails** (s48 Prop. D) |
| 13 | `r = 4`: the exact ideal | Leal–Lozano Huerta–Vite 2024 | **320112 exactly** — the ideal is principal, so this is a *lower* bound too | E | P | n/a (`l·per_3` is not a point of `Sym^4 C^4`) |
| 14 | `Λ^5` Fitting minors of a universal presentation | s51, in flight | unknown — the one live candidate below 24 | — | — | to be run |

Row-by-row detail, and what it would take to bring each degree down, in §§2–8.

---

## 2. Rows 1–3: the dual-degeneracy family, and why 24 is exactly its floor

### 2.1 The degree, re-derived rather than quoted

LMR Theorem 2.3.1 gives the equations of `Dual_{k,d,N}` as a copy of the
`SL_N`-module of highest weight

    Omega(k,d) = (d-1)(d-2)(k+2) w_1 + (d(k+2) - 2k - 5) w_2 + 2 w_{k+3}.

As a partition that is `lambda = (a_1+a_2+2, a_2+2, 2^{k+1})`, so

    |lambda| = a_1 + 2a_2 + 2k + 6 = (k+2) d (d-1)   (verified symbolically),

and an equation of degree `delta` on `S^d C^N` lies in `S^delta(S^d C^N)`, whose
summands all have `|lambda| = delta·d`. Hence

    delta = (k+2)(d-1),

with no appeal to the paper's own statement of the degree. This matters, because
LMR's **printed Theorem 1.0.2 says `n(n-1)`**, which would be 12 at `n = 4` and
is inconsistent with the highest weight printed in the same theorem. The
pre-registered factor-of-two question is therefore settled: **24, not 12.**
LMR's own worked instance reproduces exactly — `lambda(4,3) = (19,7,2^5)` at
`delta = 12`, `n = 3`, which is the partition printed in the paper. The `n = 4`
instance `lambda(6,4) = (65,17,2^7)`, `delta = 24` is *derived* from the same
formula and matches the repository's reading; it is not printed anywhere in LMR.

`ell(lambda(k,d)) = k+3`, so at `n = 4`, `ell = 9`.

### 2.2 The dual dimension, measured

At a **general** point `x` of an irreducible component of `X = {P = 0}`,

    dim X^* = rank Hess_x(P) - 2

(proved in §9; the word *general* is load-bearing — `rank Hess` is only lower
semicontinuous, so special smooth points undercount, and §5 of the log for
`wk9_s55_ranks2.py` shows that happening). Measured exactly at `r = 10`, over `Q`
and mod two primes:

| test point | rank Hess on `{P=0}` | `dim X^*` |
|---|---|---|
| `det_4` pencil | 8 | **6** |
| generic quartic | 10 | 8 |
| `l·c`, `c` generic cubic | 2 on `{l=0}`, 10 on `{c=0}` | 8 |
| `x_0 · per_3` (ten variables) | 2 on `{x_0=0}`, 9 on `{per_3=0}` | **7** |

*Sampling note, because the first draft of this document was not careful enough.*
`rank Hess(per_3)` on `{per_3 = 0}` is 9 at a general point but drops to 8 at
points with a zero coordinate; the original sampler drew from `[-6,6]` and
returned 8 on 17 of 40 draws. Re-sampled with all coordinates nonzero:
**40 of 40 draws give rank 9** (`results/logs/s55_checks.log`, C2). The reported
value is the maximum, which is the correct statistic. Rank 10 never occurs, for
the structural reason in §2.4.

A second, independent route to `dim X^*(det pencil) = 6`, using no Hessian at
all: at a rank-3 point, `adj A(s) = c·w z^T`, so `dP/ds_a = c·z^T A_a w` and the
Gauss image is the linear projection of the Segre cone of rank-1 `4×4` matrices.
The Jacobian of `(z,w) ↦ [z^T A_a w]` has rank 7 at `r = 9,10,11,12`, giving
`dim X^* = 6`, agreeing with the Hessian route (`wk9_s55_gauss.py`). *That route
is valid only for `r >= 9`*, where the admissibility conditions `A(s)w = 0`,
`z^T A(s) = 0` (8 linear conditions on `s`) are solvable for every `(z,w)`; below
`r = 9` it computes the projection of the whole Segre and is an upper bound only.

### 2.3 Why 24 is the floor — the argument, in full

Two conditions must both hold for the `k`-th member of the family to give an
equation for `D_r`.

**(i) Containment.** The equations vanish on `D_r` only if every determinantal
quartic satisfies `rank Hess <= k+2` at **every** point of its hypersurface —
the divisibility is a statement about all of `{P = 0}`, not about general points.
That holds iff `k >= dim X^*(det pencil at r)`, which is measured as
`min(6, r-2)`:

| `r` | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|
| `dim X^*(det_4 pencil)` | 3 | 4 | 5 | 6 | **6** | **6** | **6** |
| generic `r-2` | 3 | 4 | 5 | 6 | 7 | 8 | 9 |

The "every point" half is a *proof*, not a sample: `rank Hess(det_4)(M)` is
constant on `GL_4 × GL_4` orbits, each rank stratum of `M_4` is one such orbit,
and the measured values are 16, 8, 4, 0, 0 for `rank M` = 4, 3, 2, 1, 0. Every
point of `{det A(s) = 0}` has `rank A(s) <= 3`, hence `rank Hess <= 8`. ✓

**(ii) Non-vacuity.** `S_{lambda(k,4)} C^r = 0` unless `r >= ell(lambda) = k+3`,
i.e. `k <= r-3`. Geometrically the same thing: a hypersurface in `P^{r-1}` has
dual of dimension at most `r-2`, so "dual dimension `<= k`" says nothing when
`k >= r-2`.

Now combine. For `r <= 8`, (i) forces `k >= r-2` while (ii) forces `k <= r-3` —
**no member of the family gives any equation at all**. For `r >= 9`, (i) forces
`k >= 6`, (ii) permits it, and `3(k+2)` is strictly increasing in `k`, so the
minimum is at `k = 6`: **degree 24**.

**And `k = 5` really is excluded, not merely unproved.** The `k = 5` equations
express "`P` divides `det(Hess P|_F)` for every 8-plane `F`". At a rank-3 point
of a determinantal pencil `rank Hess = 8 > 7 = k+2`, so some `8×8` minor is
nonzero there and is not divisible by `P`; the `k = 5` module is *nonzero* on
`D_r`. So the exclusion is by the same measurement that establishes containment
at `k = 6`, in the opposite direction.

This answers the brief's question — 24 is the minimum over the family, not an
artefact of one choice — and it is the brief's stated "best outcome" on the
negative side. It is a statement about *this family*, not a lower bound on
`I(D_r)`.

### 2.4 The separating window is one step wide, and the padded permanent is already degenerate

For `P = l·q` with `l` a variable not occurring in `q`, write `H = Hess P` at a
point of `{q = 0}` with `l ≠ 0`. In block form `H = [[0, g^T],[g, l·K]]` with
`g = grad q`, `K = Hess q`, and `det[[0,g^T],[g,M]] = -g^T adj(M) g`. Euler gives
`K·x = (deg q - 1)·g` and `g·x = (deg q)·q(x) = 0`, so
`g^T adj(lK) g = det(lK)·g^T(lK)^{-1}g = det(lK)·(g·x)/((deg q - 1) l) = 0` and
`det H = 0` identically on `{q = 0}`. **Every padded form has dual defect at
least 1, with no hypothesis on `q`.** Confirmed: rank 9, never 10, in 40 of 40
clean draws.

Consequence: `l·per_3` lies in `Dual_{7,4,10}` and **not** in `Dual_{6,4,10}`,
while `D_10 ⊆ Dual_{6,4,10}`. **Only `k = 6` separates**; `k = 7`, at degree 27,
does not. The dual-degeneracy family has exactly one usable member at `n = 4`, it
is the cheapest one, and the margin is a single step in `k`. The "padded
permanent is more degenerate than the determinant" failure mode came within one
step of biting here too.

### 2.5 Mignon–Ressayre as equations (row 3)

MR's bound is exactly `rank Hess <= 2n` on the hypersurface, i.e.
`dim X^* <= 2n-2`; the geometry is LMR's, and converting it to equations gives
the same 24 by the same route. The degree comes from two steps: a `(k+3) = 9`
minor of `Hess P` is degree 9 in the coefficients and degree `9(d-2) = 18` in
`x`; requiring `P` to divide it is a Euclidean division of binary forms after
restriction to a line, and the division matrix has determinant `p_d^{D-d+1}`, so
the remainder's numerator has degree `18 - 4 + 1 = 15` in the coefficients of
`P`. Total `15 + 9 = 24`, and in general `s(d-2) - d + 1 + s = (s-1)(d-1) =
(k+2)(d-1)`. Two independent derivations of 24 agree.

### 2.6 What it would take to bring 24 down

Three places have slack; all three are closed at `n = 4`.

1. *A smaller minor.* Needs `rank Hess(det_4)` on the hypersurface below 8. It is
   exactly 8, on every stratum. Closed.
2. *A cheaper divisibility certificate.* The 15 is `deg_x(minor) - d + 1`, which
   is Cramer's cost on the binary division; a cheaper certificate of "`P` divides
   `M`" would have to beat Cramer. Nothing in the literature. The naive
   alternative — ideal membership via the multiplication matrix — costs
   `dim S^{14} C^{10} + 9 = C(23,9) + 9 = 817199` at `r = 10`, four orders of
   magnitude worse.
3. *A different `k`.* Ruled out by §2.3 in both directions.

---

## 3. Row 4: the Cayley–Bacharach row does not exist

There is no Landsberg–Ressayre paper using Cayley–Bacharach for equations of
determinantal loci. Full-text checks of the three candidates —
Landsberg–Ressayre, *Permanent v. determinant: an exponential lower bound
assuming symmetry* (arXiv:1508.05788, ITCS 2016), Alper–Bogart–Velasco
(arXiv:1505.02205), and Kumar–Volk (arXiv:2009.02452) — find the term in none of
them. Cayley–Bacharach does appear in the neighbouring literature on **Waring
rank** (Buczyński–Han–Mella–Teitler, arXiv:1703.02829), the likely source of the
conflation.

What the two real papers give:

- **ABV Thm 1.2**: `dc(f) >= codim Sing(f) + 1` for `deg f > 2` and
  `codim Sing(f) > 4`. A numerical lower bound from a geometric property, with no
  polynomial in the coefficients anywhere; not constructive. Its consequence for
  equations is the discriminant row (§4), which ABV do not state.
- **Landsberg–Ressayre ITCS 2016**: an exponential bound *conditional on
  equivariance*. No equations.

**Row 4 should be struck from the standing table**, and replaced by ABV with an
explicit note that it yields a bound and not equations.

---

## 4. Row 5: the discriminant — explicit, classical, and pointing the wrong way

For `P = det_4(A(s))`, `dP/ds_a = tr(adj A(s)·A_a)`, and `adj M = 0` exactly when
`rank M <= 2`. The rank-`<=2` locus in `P^15` has codimension 4 and degree 20
(Giambelli–Thom–Porteous, anchored here on `deg Seg(P^2×P^2) = 6` and
`deg Seg(P^3×P^3) = 20`), so a generic `P^4` of matrices meets it in a
zero-dimensional scheme of length 20.

Measured: the ideal of `3×3` minors on a random 5-dimensional pencil has Hilbert
function `19, 20, 20, 20, …` — **length exactly 20** — at two primes with a
different random pencil for each; at `r = 4` it reaches 0, so a generic
determinantal quartic *surface* is smooth. Separately, at a constructed rank-2
point of a 5-dimensional pencil the gradient vanishes and the projective Hessian
has rank exactly `r-1 = 4` at four independent seeds, which is precisely the
condition for an **ordinary node**. So the length-20 scheme is 20 nodes.

Hence

    D_5 ⊆ { disc = 0 },   deg disc(Sym^4 C^r) = r·3^{r-1} = 405 at r = 5,

an explicit classical equation, and `D_4 ⊄ {disc = 0}`. (The length-20 statement
is also banked at `docs/theory_directions.md` §F; the node-ness measurement is
new here.)

**It fails the degeneracy-direction check trivially and terminally.** `l·per_3`
is reducible, its two components meet, so it is singular and the discriminant
vanishes at it. Bringing the degree down does not help: the whole family
"detects extra singularity" is on the wrong side, because the padded permanent is
maximally singular. This is s48's Proposition D reached by a different
construction — see §8 for a correction to how broadly that proposition is stated.

---

## 5. Rows 6–8: the flattening family

**The direction failure here is not new — it is s35's, and it is proved.**
`docs/theory_directions.md` §B(a): for `F = l·c` the second partials are
`l·(∂_i∂_j c) + (∂_i l)(∂_j c)` with `∂_i∂_j c` linear, so the image of
`Cat_{2,2}` lies in `l·V + span{∂_j c}` and `rank <= 2r`. Measured here at
`r = 10`: `rank Cat_{2,2}(l·c) = 20 = 2r` exactly, and `rank Cat_{2,2}(l·per_3)
= 18`. What is new in this session is the **determinant side** and the resulting
minor size.

| test point (`r = 10`) | `rank Cat_{2,2}` | smallest vanishing minor |
|---|---|---|
| generic quartic | 55 | — |
| `det_4` pencil | **36** | **37** |
| `l·c` | 20 | 21 |
| `x_0·per_3` | **18** | 19 |

Rank 36 at a determinant is structural: the second partials of `det_4` are the
`C(4,2)^2 = 36` complementary `2×2` minors. It is 36 for every `r >= 8` and full
rank for `r <= 7`, so the family is vacuous below `r = 9` — the same threshold as
LMR, for a different reason. **The smallest flattening minor that vanishes on
`D_r` has size 37, and that is its degree**; the number appears to be new, though
the mechanism it rests on is banked (s35, and `docs/blindness_slab.md` for the
`r = 4, 5` values).

`18 < 36`: every `37×37` minor of `Cat_{2,2}` that vanishes on `D_r` also
vanishes at `l·per_3`. The inequality runs the wrong way even for the reducible
control (`20 < 36`), so the failure is caused by the padding, not by the
permanent.

Two companions, both measured over `Q` and at both primes:

- `Cat_{1,3}` has rank 10 — full — at all four points: vacuous.
- the Koszul flattening `Λ^1 : V ⊗ V^* → Λ^2 V ⊗ S^2 V` has rank **99 at all
  four points**. Its corank is at least 1 for every `P`, since
  `Σ_c e_c ⊗ ∂_c` maps to zero by symmetry of second partials; corank exactly 1
  is measured, not proved. It detects nothing.
- Farnsworth (arXiv:1505.05079) proves `R_S(det_4) >= 38`, so any border-rank
  equation vanishing at the determinant needs a threshold `R >= 38` and minors of
  size at least 39 — worse than 37, and subject to the same direction failure.

**Rows 6–8 are closed.** A flattening equation vanishes on `D_r` only if its
threshold is at least the determinantal rank, and every such threshold also
catches the padded permanent, whose rank is strictly smaller. Only a flattening
whose rank at `l·per_3` *exceeds* its rank at a determinant could help; none of
the three tested behaves that way, and s35's proved bound explains why not.

---

## 6. Rows 9–10: boundary equations

Hüttenhain–Lairez (arXiv:1512.02437, C. R. Acad. Sci. Paris 354 (2016)) prove the
boundary of `GL_9·det_3` has exactly two irreducible components — the orbit
closure of the determinant of the generic traceless matrix, and that of the
universal quadric — by a single blow-up of `P(E)^{ss}` along the smooth centre of
skew-symmetric matrices.

**It produces no equations, and structurally cannot.** The boundary
`∂Ω = Ω̄ \ Ω` lies *inside* `Ω̄`, so describing it gives no polynomial vanishing
on `Ω̄`. The one route by which it could bear on equations —
Bürgisser–Ikenmeyer's Thm 3.10, `O(Ḡw) = O(Gw)` localised at the fundamental
invariant, so that the boundary determines the coordinate ring — holds only
set-theoretically when `b(w) < e(w)`, which is the non-normal case Kumar proved
`Det_n` is in for `n >= 3`. This programme already owns the matching local fact:
`docs/degree24_extension.md` shows the divisorial argument on `Ω̄(det_3)` predicts
a false statement, because divisors only see the normalisation.

**At `n = 4` the boundary is not known.** Hüttenhain's thesis has a section on it
(§8.4) and leaves it open; Bürgisser's survey states that for `n = 4` the
boundary "is already unknown". Row 10 is honestly empty, and it is the one place
in this census where new work could produce something rather than confirm an
absence — which is what s53 is for.

---

## 7. Row 11: the Plücker route, and a correction to the brief

**The brief's row 6 rests on a superseded draft.** The committed
`docs/s53_prompt.md` contains no common-isotropic-4-plane route: s53 was rebuilt
around the blow-up of the determinant coefficient ideal (the `n = 4` analogue of
Hüttenhain–Lairez), and the isotropic statement was recorded in
`docs/critic_e7_response.md` §5 as a corollary of Alper–Bogart–Velasco, with an
explicit instruction to deprioritise `I_2`. The `I_1(B_9) = I_1(B_10) = 0` result
stands as reported by the external session and has not been reproduced here or
anywhere in the repository — that document itself asks for reproduction.

The caveat the brief asks for, stated plainly: `B_r ⊆ Gr(r, Λ^2 W)` is a locus of
**`r`-planes of skew forms**, and its equations are functions of the Plücker
coordinates of the pencil; our object is a function of the 715 coefficients of a
quartic. These are not the same ring, and the conversion is an elimination of the
pencil. This is also the row that fails `docs/brief_wording.md` §7 as stated: an
invariant of the pencil is not functorial in the coefficient ring at all until
the elimination is done.

**The estimate.** There is exactly one cell where this elimination has actually
been carried out. At `r = 4`, Leal–Lozano Huerta–Vite (arXiv:2303.09028, Math.
Nachr. 2024) determine that the determinantal quartic surfaces form an
irreducible divisor of degree **320112** in the `P^34` of quartic surfaces. So
the one *known* conversion, at the smallest cell, lands at `320112`, which is
`1.3 × 10^4` times 24 — four orders of magnitude — with no low-degree equation
anywhere below it, since the ideal there is principal.

At `r >= 5` the image is no longer a hypersurface (codimension 20 at `r = 5`, 60
at `r = 6`, 381 at `r = 9`), and no bound on the generator degrees of an
elimination ideal of that shape is available that is anywhere near 24. The
general-purpose bounds (Bézout on the pushforward, Perron-type `d^n`) return
numbers of the form `4^{dim D_r}`, which are not estimates so much as statements
that the method gives no estimate.

**Verdict for row 11: unknown, with a named reason** — the only anchor puts it
four orders of magnitude above 24, and nothing suggests the anchor is misleading.

---

## 8. Rows 12–14: our own constructions, and one correction to the record

**Row 12, Macaulay minors.** Re-derived from `rho_d = dim Sym^d C^r - h_d`,
`h_d = [t^d](1+t+t^2)^r`, and the determinantal rank:

| `r` | `d` | `dim Sym^d C^r` | `h_d` | `rho_d` | drop | det rank | minor size = degree |
|---|---|---|---|---|---|---|---|
| 5 | 7 | 330 | 30 | 300 | 1 | 299 | **300** |
| 6 | 7 | 792 | 126 | 666 | 6 | 660 | **661** |
| 6 | 8 | 1287 | 90 | 1197 | 50 | 1147 | **1148** |

The brief's 300 and 661/1148 are reproduced. The s49 correction (determinantal
rank, not generic rank) happens to leave `r = 5` unchanged, since
`rho_7 - 1 + 1 = 300`; that coincidence does not generalise, `r = 6` moving
`666 → 661`. *Honest boundary:* `rho_d` and the ambient dimensions are re-derived
here; the drops are not — `drop = C(6,5) = 6` at `(6,7)` is the repository's
measured value and is consistent, while the `d = 8` drop of 50 is back-solved
from the quoted 1148 and is **not** independently checked by this session.

**A correction to `docs/excess_singularity.md`.** That document's §"what it
closes" extends Proposition D from Macaulay minors to *"anything that reads
'the singular locus is bigger than expected': **Hessian-rank conditions**,
Jacobian-ideal Hilbert-function conditions, Milnor-number conditions"*, on the
ground that any functional monotone in `dim (S/J_F)_d` inherits the inequality.
**The clause "Hessian-rank conditions" is too broad, and row 1 is the
counterexample.** The LMR/Mignon–Ressayre condition is a rank of the Hessian
*matrix evaluated at points of the hypersurface*, which is not a functional of
the Milnor algebra and is not monotone in it: measured here, the determinant sits
at 8 and the padded permanent at 9, so the inequality runs the *opposite* way to
the Milnor-algebra one. The rest of the proposition — the Macaulay-minor and
Milnor-corank statements — is untouched; only the generalising clause needs
narrowing to "functionals monotone in `dim (S/J_F)_d`", which is what its own
proof gives.

**Row 13, `r = 4`.** `I(D_4)` is principal of degree 320112 — a *lower* bound as
well as an upper one, and the only cell where the onset is known exactly. Small
`r` has nothing remotely cheap, which is consistent with the `r`-dependence in
§2.3: cheap equations live at large `r`. The §5 check is not well posed here,
since `l·per_3` is not a point of `Sym^4 C^4`.

**Row 14, the `Λ^5` Fitting minors (s51).** The only live candidate below 24 in
the programme. Its degree is set by the size of the universal presentation map
`Ψ_f`, which is not yet built. Two things this census contributes: its rank
condition must be checked against the §2.2/§5 tables *before* the Fitting degree
is computed — rows 5, 6 and 12 all died at exactly that step, and each cost a
session; and it must be built from `f` alone, since eliminating the pencil is
what row 11 shows costs four orders of magnitude.

---

## 9. The one lemma used throughout

*At a **general** point `x` of an irreducible component of a hypersurface
`X = {P = 0}` in `P(V)`, `dim X^* = rank Hess_x(P) - 2`.*

Let `u = grad P(x) ≠ 0` and `H = Hess_x(P)`. Euler gives `Hx = (d-1)u ≠ 0`, so
`x ∉ ker H`. For `w ∈ ker H`, `(d-1)⟨u,w⟩ = ⟨Hx, w⟩ = ⟨x, Hw⟩ = 0`, so
`ker H ⊆ u^⊥ = T_x X̂`. The cone over `X^*` is the image of the Gauss map
`grad P`, whose differential at `x` is `H`, so its dimension is
`dim H(u^⊥) = (N-1) - dim ker H = rank H - 1`, and projectively
`dim X^* = rank H - 2`. ∎

"General" is required: `rank H` is lower semicontinuous, so at a special smooth
point the formula undercounts, and the maximum over the component is the value to
take. Sanity: `det_4` gives `8 - 2 = 6 = 2n-2` ✓; a generic quartic in `P^9`
gives `10 - 2 = 8 = N-2` ✓.

---

## 10. Provenance of every number quoted here

| number | status |
|---|---|
| `delta = (k+2)(d-1)`, 24 at `n=4` | **re-derived** symbolically from the highest weight |
| `(19,7,2^5)` at `delta = 12` | **re-derived** and matches the partition printed in LMR |
| `(65,17,2^7)` at `delta = 24` | **derived** from the same formula; not printed in LMR |
| `ell(lambda) = 9`, module zero for `r <= 8` | **re-derived**; independently confirmed geometrically |
| `dim X^*` = 6 / 8 / 8 / 7 at `r = 10` | **measured** exactly, `Q` and two primes, several seeds; the pad value re-sampled cleanly (40/40) |
| `dim X^*(det)` = 3,4,5,6,6,6,6 for `r = 5..11` | **measured**; confirmed at `r >= 9` by the independent Gauss route |
| `rank Hess(det_4)` = 16/8/4/0/0 by rank of `M` | **measured** on 12 draws per stratum, and **proved** to be the whole stratum by orbit-constancy |
| 15 (the division step) | **re-derived** by Cramer, `det = p_d^{D-d+1}` |
| 817199 | **re-derived**: `C(23,9) + 9` |
| length-20 singular scheme; ordinary nodes | **measured** (Hilbert function, two primes, two pencils; Hessian rank 4 at the singular point, four seeds) — mod `p` only for the Hilbert function |
| `deg disc = r·3^{r-1}` = 405 | **re-derived** (GKZ formula, arithmetic) |
| GTP degree 20, codim 4 | **re-derived**, anchored on two Segre degrees |
| `Cat_{2,2}` 55/36/20/18; `Cat_{1,3}` 10; Koszul 99 | **measured** exactly over `Q` and both primes |
| `rank Cat_{2,2}(l·c) <= 2r` | **quoted and proved** at s35 (`theory_directions` §B(a)); the `r = 10` value 20 measured here |
| `R_S(det_4) >= 38` | **quoted** (Farnsworth); not re-derived |
| 300, 661, 1148 | `rho_d` **re-derived**; the drops quoted (see §8) |
| 320112 | **quoted**, one source (Leal et al.); `docs/e4_hunt.md` adopts the same value and labels it "adopted, not certified" — it is **not** an independent confirmation |
| BIP needs `n >= m^25` | **quoted**; it does not apply at `n=4, m=3` |
