# Session 66 (C5) — the `r = 5` special normal cone at the primitive family: no exotic direction, no climb

Branch `s66-primitive` off `main` tip `226b4ef1` (fresh public clone, container
only; ancestry gate passed first; delivered by single-ref bundle
`s66_primitive.bundle` + `.md5`, not pushed).  Pre-registration
`results/PREREG_s66.md` (commit `206a6c5`, before any measurement).  Code
`analysis/wk10_s66_*.py`, CAS inputs `analysis/wk10_s66_*.sing`, data
`results/s66_*.json`, primes `results/s66_*primes_*.txt`, logs and pids
`results/logs/s66_*`.  Labels: **proved** / **measured** /
**adopted-from-literature** / **expectation**.  `python-flint nmod_mat` for every
rank; house primes `2147483647, 2147483629` for the tangent tables and arc
identities; `32003` and `1000003` for the Singular decompositions (every
decomposition and every image dimension identical at both).  Every spanning
vector of every tangent space was checked to annihilate `dΦ` before it was
counted (KC2: `bad = 0` on all 76 runs of the table).

The brief's `docs/batch10_worker_preamble.md` and `docs/batch10_plan.md` are not
in the tree at `226b4ef1` nor on the laptop's `work/` or `gct-rewrite/`; the
session ran from the brief, which carries the correction and the tasks.

## 0. Verdict

> **The loophole is closed at first and second order at every point of the
> primitive world, and the primitive world produces no climb.**  At a generic
> point of the primitive component `P` the first-order kernel is exactly its
> tangent space (`rank dΦ = 37`, `ker = 43 = dim P`, transverse quotient **0**),
> as the pre-registration derived from the two-skew-lines structure of the
> cokernel; the same holds at the semi-primitive component `SP` (`31 / 49 / 49 /
> 0`), at their transposes, and at **every** incidence of `P` and `SP` with the
> compression components and with each other — the quotient is **0** at all
> seventeen rank-3 points measured (two primes, two seeds each).  The compression
> and primitive worlds both produce no exotic first-order direction.
>
> **Second order.**  The quadratic initial forms of the base ideal cut out
> **exactly** the union of the tangent spaces of the components through the
> point at `P∩SP`, `P∩coker`, `P∩SP^T`, `SP∩c32`, `SP∩coker`, `c21∩c32`,
> `ker∩c21` — no tangent-cone component that no tangent space sees; at `P∩c32`
> and `SP∩c21` they leave one further linear component, not excluded at second
> order.  The order-2 directions that carry a **reducible** leading form
> (`V(Q_2^π)`) were decomposed completely at every two- and three-component
> incidence, by a reduction proved here (the quadrics are bilinear in the two
> transverse coordinate blocks and blind to the intersection, so the
> decomposition is the rank stratification of a small linear matrix, and
> Singular does in seconds what did not finish in 66 variables), and the
> reducible exceptional image over **every** component is measured:
>
> | incidence | order 1 | order 2 (per component of `V(Q_2^π)`) | order 3 |
> |---|---|---|---|
> | `P` generic / `SP` generic | 24 / 26 | — (smooth: inert, §4) | — |
> | `P ∩ SP` | 16 | 23, 26 | 23, 26 |
> | `P ∩ coker` | 17 | 24, (17) | 24, (17) |
> | `P ∩ SP^T` (`P_meet`) | 17 | 23, (17) | 23, (17) |
> | `P ∩ c32` | 14 | 23, 24, 27 | 23, 23, 27 |
> | `SP ∩ c32` | 18 | 24, (18) | 24, (18) |
> | `SP ∩ c21` | 19 | 25, 28 | 26, 28 |
> | `SP ∩ coker` | 19 | 26, 28 | 26, 28 |
> | `c21 ∩ c32` (audit) | 18 | 27, 27 | 27, 27 |
> | `ker ∩ c21` | 18 | 29, 28 | — |
> | `ker ∩ coker` | 29 | 29, 29 (generic-kernel components) | 29, 29 |
> | `P ∩ ker = SP ∩ ker` = padded-skew rank-2 locus | (`dΦ ≡ 0`) | 28, 28, 26, 26 | 28, 28, 26, 26 |
>
> **Every number is `≤ 29 < 31`** (the certified exact locus) and far from 35.
> Nothing in the primitive world reaches the target, at first, second or third
> order.  `R_5 ⊄ D_5` stays the lean verdict; the mechanism that could have
> reversed it — a component of the exceptional divisor hidden over the
> primitive family — is not there at the orders reachable by arcs.
>
> **Three structural facts, proved, that the programme did not have.**
> (i) *Contact order is inert at every smooth point of the base scheme*
> (§4): the exceptional fibre there is `P(im dΦ)` at every order, so s59's
> "invariance of contact order" is a theorem at generic stratum points and the
> only places a hidden component can live are the singular points of `V(J)` —
> the incidences and the rank-`≤2` loci, which is exactly what this session
> measured.  (ii) *The base scheme is generically reduced along every
> component but not along the incidences*: `dim Q_2 = 12 < 16` at `P∩SP` (and
> `25 < 49`, `41 < 69`, … elsewhere) says `J ⊊ I_1 ∩ I_2` there.  (iii) *On the
> rank-`≤2` compression loci the order-2 leading form is an honest
> determinant* (Laplace / rank-one update, §7), so their exceptional image sits
> in `Φ(X_5)` and their reducible part in the exact locus.
>
> **Two bookkeeping corrections.**  The `k = 3` stratum of s32 — the
> semi-primitive type `SP = {[φN(x) | c]}`, a 49-dimensional component of `B_5`
> whose maximal matrix space is 7-dimensional and lies in no compression space
> — was absent from the five strata s54 and s59 used; it is measured here at
> every order (order 1: 26).  And `P ∩ ker` is not a rank-3 incidence at all:
> a `P`- or `SP`-pencil with a common kernel has rank `≤ 2` (the kernel contains
> the moving vector and the fixed one), and that locus is the padded `3×3`
> skew type — the genuine `n = 4` analogue of the Hüttenhain–Lairez skew
> component — where `dΦ ≡ 0` and every arc has order `≥ 2`.  Its order-2
> V-variety has four explicit components (common kernel, common cokernel,
> rank-one column, rank-one row: the factorisation `m'q' = β'γ'` in a UFD) and
> its order-2 and order-3 reducible images are `28, 28, 26, 26`.

## 1. The components of `B_5` (adopted + measured)

`M(s) = Σ s_k B_k`, `Φ(M) = det M(s)`, `B_5 = V(J)`, `J` = the 70 coefficient
functions.  A bounded-rank-3 subspace of `M_4` is a compression space or is
built on a primitive core; for rank 3 the primitive cores are Atkinson's
Example 2.3 at `a = 4` and its projections (Huang–Landsberg's reading, s32 §3 —
**adopted**), which gives eight maximal types and eight components:

| component | matrices | dim (pre-reg) | `rank dΦ` / `dim ker` at a generic point (measured) | `ker = T`? |
|---|---|---|---|---|
| `ker`, `coker` | `A e = 0` / `im A ⊆ W_3` | 63 | 17 / 63 | yes |
| `c21`, `c32` | `A(U_2) ⊆ W_1` / `A(U_3) ⊆ W_2` | 57 | 23 / 57 | yes |
| `SP`, `SP^T` | `[φN(x) | c]`, `φ: C^3 → C^4`, `N(x)y = x × y` | 49 | 31 / 49 | yes |
| `P`, `P^T` | `M_φ(y)t = φ(t ∧ y)`, `φ ∈ Hom(Λ²C^4, C^4)` | 43 | 37 / 43 | yes |

"`ker = T`" is the verification rule of the pre-registration: at a generic
point the Jacobian image of the parametrisation equals `ker dΦ`, so the family
is a component (a bigger one through the point would enlarge the kernel) and
`J` is reduced along it.  All eight pass (C0 **confirmed**).  `P^T ≠ P` and
`SP^T ≠ SP` as families: in `E_φ` the kernel vector is linear and the cokernel
vector is the vector of four quadrics through two skew lines (the rank-2 locus
of `E_φ`, `K = ker φ` meeting the Klein quadric in two points with
complementary planes), so no linear reparametrisation of `E_φ^T` has a linear
kernel; the transposes are measured once each and give identical numbers.

The `37` at `P` is the pre-registered count: with `adj M_0 = y · v(y)^T`,
`dΦ(N) = v^T N y`, and in coordinates `(y, s_5)` with `s_5` spanning `ker u`,
`im dΦ = S_1 · I_3 ⊕ s_5 · I_3` for `I` the ideal of the two skew lines, of
dimension `25 + 12 = 37` (Hilbert function `2d + 2`).  **Measured 37, both
primes, two seeds** (T0 confirmed).  At `P ∩ SP` the same count with the ideal
of two points of `P²` gives `13 + 8 + 8 = 29`: **measured 29** (T3 confirmed on
the kernel; its "Jacobian image `≤ 40`" clause was a slip — `Y_3 ∧ C^4 = Λ²C^4`,
so the fibre of `(φ, u) ↦ M` does not jump at rank-3 `u` and the Jacobian image
is the full 43; it does jump at rank-2 `u`, to 5 dimensions, and there the
image is 39 and the limit-tangent correction is what restores 43).

## 2. Machinery and calibration (KC1)

`analysis/wk10_s66_core.py`: ring-generic parametrisations of the eight types
(so the same code runs over `F_p` and over `F_p[ε]/ε^K`), `dΦ` by dual numbers
on the 70 coefficients (`wk9_s59_core.det_arc`), tangent spans as the images of
each component's own parametrisation at the point plus the `GL_4 × GL_4 × GL_5`
directions, a valuation-pivoted elimination over `F_p[ε]/ε^K` for the limit of
tangent spaces along a curve (used where a parametrisation is not submersive),
and the second-order spaces `Q_2`, `Q_2^π` in kernel coordinates.
`wk10_s66_points.py` builds every point spec; `wk10_s66_tangent.py` the table;
`wk10_s66_orderq.py` the order-1 image over a parametrised locus by s59's
identity with the locus parameters `θ` differentiated through the builder;
`wk10_s66_bilinear.py` the second-order reduction, the Singular runs, the
order-2 and order-3 images; `wk10_s66_rank2.py` the rank-`≤2` loci.

Calibration, before anything new (both primes): the audit's two tables
reproduce exactly — `c21 ∩ c32`: `16 / 64 / 57 / 57 / 50 / 64 / 0`;
`ker ∩ coker`: `5 / 75 / 63 / 63 / 75 / 0`; generic `c21`: `23 / 57 / 57`; and
s59's order-1 row `29, 29, 28, 28, 24` over `ker, coker, c21, c32, prim`, with
the audit's `18` at `c21 ∩ c32` and the audit's `27` for the second-order mixed
direction (§6).

## 3. The tangent table (3A) — every point, two primes, two seeds

`T` is the component's tangent space at the point (Jacobian image, with the
limit tangent added where the Jacobian image fell short of the component's
dimension — `P` at rank-2 `u`, the `SP` frames there, `P` and `SP` at the
rank-2 locus).  Four runs per row (`2147483647, 2147483629` × seeds `1, 2`);
every row's numbers are identical across the four (KC3).

| point | components through it, with `dim T` | `rank dΦ` | `dim ker dΦ` | span of the `T` | **transverse quotient** | `dim Q_2` | `I(∪T)_2` |
|---|---|---|---|---|---|---|---|
| generic `c21` | c21 57 | 23 | 57 | 57 | **0** | 0 | 0 |
| generic `ker` | ker 63 | 17 | 63 | 63 | **0** | 0 | 0 |
| `c21 ∩ c32` (audit) | c21 57, c32 57 | 16 | 64 | 64 | **0** | 25 | 49 |
| `ker ∩ coker` (audit) | ker 63, coker 63 | 5 | 75 | 75 | **0** | 59 | 144 |
| generic `P` | P 43 | 37 | 43 | 43 | **0** | 0 | 0 |
| generic `P^T` | P^T 43 | 37 | 43 | 43 | **0** | 0 | 0 |
| generic `SP` | SP 49 | 31 | 49 | 49 | **0** | 0 | 0 |
| generic `SP^T` | SP^T 49 | 31 | 49 | 49 | **0** | 0 | 0 |
| `P_tan` (`K` tangent to the Klein quadric) | P 43 | 37 | 43 | 43 | **0** | 0 | 0 |
| `P ∩ coker` (rank-3 `φ`) | P 43, coker 63 | 14 | 66 | 66 | **0** | 41 | 69 |
| `P ∩ SP` (rank-3 `u`) | P 43, SP 49 | 29 | 51 | 51 | **0** | 12 | 16 |
| `P ∩ c32` (rank-3 `u`, `K ∩ Λ²(im u) ≠ 0`) | P 43, SP 49, c32 57 | 19 | 61 | 61 | **0** | 28 | 56 |
| `P ∩ c21` (rank-2 `u`) | P 39→43, c21 57, SP 48→49 (×3 frames) | 17 | 63 | 63 | **0** | 18 | 6 |
| `P_meet` = `P ∩ SP^T` (`K` a line of the Klein quadric) | P 43, SP^T 49 | 28 | 52 | 52 | **0** | 19 | 27 |
| `SP ∩ c32` (rank-2 `φ`) | SP 49, c32 57 | 21 | 59 | 59 | **0** | 17 | 20 |
| `SP ∩ c21` (rank-2 `x`) | SP 49, c21 57 | 20 | 60 | 60 | **0** | 15 | 33 |
| `SP ∩ coker` (`c ∈ im φ`) | SP 49, coker 63 | 12 | 68 | 68 | **0** | 41 | 95 |
| `P ∩ ker` (rank-3 `φ`, `ker φ = a ∧ C^4`) | P 38→43, ker 63, coker 63 | **0** | 80 | 78 | (2) | 53 | 378 |
| `SP ∩ ker` (`c = φN(x)w`) | SP 46→49, ker 63 | **0** | 80 | 80 | 0 | 53 | 527 |

Readings.  (a) At every rank-3 point the first-order kernel is exactly the span
of the tangent spaces of the known components: **no exotic first-order
direction anywhere in the primitive world**, matching the audit's finding in
the compression world.  (b) The two `ker`-incidences have `rank dΦ = 0`: they
are rank-`≤2` pencils (§7), where "transverse quotient" is void (every direction
is a first-order kernel direction); the `(2)` at `P ∩ ker` is the two further
components through the padded-skew locus that the row does not list (`SP`,
`P^T`, `SP^T`), not a transverse direction.  (c) `P_meet` needed `SP^T`: for
`K = a ∧ U_3` the cokernel vector becomes `ℓ_U(y)·w(y)` with `w` linear of rank
3, so the pencil lies on `SP^T` (`sp_frame_from_pencil` recovers the frame of
its transpose exactly); without that component the quotient reads 9, with it
0 — the pre-registered "`P_meet`: none" was wrong and is corrected.  (d)
`P_tan` is a smooth point of `V(J)` (`43 = 43`): the codimension-one
degeneration of `K` does not touch the scheme structure (T5 confirmed there).
(e) At `P ∩ c21` and `SP ∩ c21` the `Q_2` quadrics do **not** vanish on the
limit tangent space of `P` (rank-2 `u`) — `P` is singular along that locus and
its tangent cone is smaller than the limit tangent; the kernel is still
spanned.  (f) `dim T_1 ∩ T_2 = dim(C_1 ∩ C_2)` at every two-component
incidence (`41` at `P∩SP`, `40` at `P∩coker`, `50` at `c21∩c32`, …): the
intersections are clean.

## 4. Contact order is inert at smooth points of the base scheme (proved)

**Lemma.**  Let `M_0 ∈ V(J)` with `dim ker dΦ_{M_0} = dim_{M_0} V(J) = d`
(equivalently: `V(J)` is smooth at `M_0`).  Then for every arc `M(t)`,
`M(0) = M_0`, `det M(t) ≢ 0`, the leading form of `det M(t)` lies in
`im dΦ_{M_0}`, and every nonzero element of `im dΦ_{M_0}` is the leading form of
an arc.  The exceptional fibre over `M_0` is `P(im dΦ_{M_0})` at every contact
order.

*Proof.*  Let `c = 80 − d = rank dΦ_{M_0}` and pick `f_1..f_c` among the 70
coefficient functions with independent differentials at `M_0`.  They cut out a
smooth germ of dimension `d` containing `V(J)`, whose local ring is regular
hence reduced, so `J = (f_1..f_c)` in `O_{M_0}` and the coefficient vector is
`c(M) = H(M) f(M)` with `H` a `70 × c` matrix of functions.  Differentiating
at `M_0`, `dc = H(M_0) df`, and since the `dc_i` span a `c`-dimensional space
while the `df_j` are independent, `H(M_0)` is injective with column span
`im dΦ_{M_0}`.  Along an arc, `f(M(t)) = t^q v(t)` with `v(0) = v ≠ 0`, so
`c(M(t)) = t^q H(M(t)) v(t)` has leading form `H(M_0) v ≠ 0`.  Conversely
`(f_1..f_c, y_1..y_d)` are local coordinates, and the arc `f = t v`, `y = y_0`
has leading form `H(M_0) v`. ∎

Consequences.  s59 measured `29, 29, 28, 28, 24` at `q = 1, 2, 3, 4` at generic
stratum points and called it "invariance of contact order"; by §1 those points
are smooth points of `V(J)`, so the invariance is this lemma (and the order-3
cancellation being "unobstructed" is the smoothness).  The reducible exceptional
image over the smooth locus of `B_5` is the order-1 image, `≤ 29`, at every
order.  A component of the exceptional divisor `E` not visible at order 1 can
only lie over `Sing V(J)` — the incidences and the rank-`≤2` loci.  That is
the locus this session measured, and it is why §6 is organised by incidence.

## 5. Second order: the bilinear reduction, the decompositions, and the reducedness of `J`

`Q_2 = {Σ_j c_j e_{2,j}|_{ker dΦ} : c ⊥ im dΦ}` (`e_{2,j}` the `t²` coefficient
of `det(M_0 + tN)`) is the space of quadratic initial forms of `J` on the kernel;
`V(Q_2)` contains the tangent cone of `V(J)`.  `Q_2^π ⊆ Q_2` uses only `c ⊥
(im dΦ + W)`: `V(Q_2^π) ⊆ ker dΦ` is the set of first-order directions `M_1`
along which an arc `M_0 + tM_1 + t²M_2` can have a reducible leading form
(`π g_2 = 0` solvable in `M_2`) — the audit's "23 quadrics in the 64-dimensional
kernel" at `c21 ∩ c32` are the `35 − rank(π dΦ) = 23` generators of `Q_2^π`
there (13 of them independent).

**Bilinear lemma (proved).**  At `M_0` on two components `C_1, C_2`, smooth at
`M_0`, with `T_1 + T_2 = ker dΦ`, choose kernel coordinates `(i, a, b)` with
`T_1 ∩ T_2 = {a = b = 0}`, `T_1 = {b = 0}`, `T_2 = {a = 0}`.  A quadric
vanishing on `T_1` and on `T_2` has no `ii, ia, ib, aa, bb` monomials, so every
element of `Q_2` (and of `Q_2^π`) is bilinear, `q = a^T C_q b`, and independent
of `i`.  Hence `V(Q) = (i-space) × {(a, b) : M(a) b = 0}` with `M(a) = Σ a_i M_i`
a `(#q) × β` matrix of linear forms in the `α` coordinates `a`, and the
components of `V(Q)` are `{a = 0} = T_2` and the closures of `{(a, b) : rank
M(a) = r, b ∈ ker M(a)}` over the rank strata of `M(a)` (`{b = 0} = T_1` when
the generic rank is `β`).  With three or more components through the point and
`Σ T_i = ker dΦ`, the same argument (polarise `q(i + w) = 0` for `w ∈ T_j`)
shows `q` is independent of `i = ∩T_i`, which is the reduction used at
`P ∩ c32` and `P ∩ c21`.

This is what made the CAS stage finish.  In 64–66 variables Singular's `std` of
`Q_2^π` did not complete in the 30-minute box at `P ∩ coker`; after the
reduction (`α + β = 26` variables, bilinearity verified with zero non-bilinear
entries at every point) every `minAssGTZ` returned in `0–90 s`, at `32003` and
again at `1000003`.  Every minimal prime found is **linear**.

| point | `α, β` (codims of `T_2, T_1` in the kernel) | `V(Q_2)` | `V(Q_2^π)` (dims in `(a,b)`; `+ dim I`) |
|---|---|---|---|
| `P ∩ SP` | 2, 8 | **`= T_P ∪ T_SP`** | `H` (9: hyperplane ⊃ `T_SP`), `L` (6: ⊃ `T_P`) |
| `P ∩ coker` | 3, 23 | **`= T_P ∪ T_coker`** | `T_coker`, `L` (11 ⊃ `T_P`) |
| `P ∩ SP^T` | 3, 9 | **`= T_P ∪ T_{SP^T}`** | `T_{SP^T}`, `L` (6 ⊃ `T_P`) |
| `SP ∩ c32` | 2, 10 | **`= T_SP ∪ T_c32`** | `T_c32`, `L` (5 ⊃ `T_SP`) |
| `SP ∩ c21` | 3, 11 | `T_c21 ∪ L_6` (`L_6 ⊋ T_SP`, dim 6 vs 3) | `L_9 ⊃ T_SP`, `L_12 ⊃ T_c21` |
| `SP ∩ coker` | 5, 19 | **`= T_SP ∪ T_coker`** | `L_11 ⊃ T_SP`, `L_20 ⊃ T_coker` |
| `c21 ∩ c32` | 7, 7 | **`= T_c21 ∪ T_c32`** | `L_9 ⊃ T_c21`, `L_9 ⊃ T_c32` |
| `ker ∩ c21` | 10, 4 | **`= T_ker ∪ T_c21`** | `L_11 ⊃ T_ker`, `L_7 ⊃ T_c21` |
| `ker ∩ coker` | 12, 12 | (not decomposed in the box) | generic-kernel components sampled directly (§6) |
| `P ∩ c32` (three components, 22 reduced variables) | — | `T_c32 ∪ T_SP ∪ L_8` (`L_8 ⊋ T_P`, dim 8 vs 4) | three linear primes (19, 13, 14) |
| `P ∩ c21` (four spaces, 30 reduced variables) | — | `std` did not finish in the box | `Q_2^π` (9 quadrics): Singular and Macaulay2 both timed out; see §8 |

**No tangent-cone component beyond the tangent spaces** at seven of the nine
decomposed points.  At `P ∩ c32` and `SP ∩ c21` the quadrics leave one further
linear component containing `T_P` (resp. `T_SP`); since the eight components of
§1 exhaust `B_5` (**adopted** classification), such a component is not the
tangent space of a hidden component of the base locus — it is a second-order
candidate that cubic initial forms must cut down, or a non-reduced structure —
and in either case what it contributes to the exceptional divisor is measured
in §6 through `V(Q_2^π)`.

**`J` is not reduced along the incidences (measured).**  In the coordinates of
the lemma, `I_1 ∩ I_2 = (u) + (a_i b_j)` locally (clean intersection, §3(f)),
whose degree-2 initial part on the kernel is all `αβ` products; `in(J)_2` on
the kernel is `Q_2`.  `dim Q_2 = 12 < 16` at `P∩SP`, `41 < 69` at `P∩coker`,
`25 < 49` at `c21∩c32`, `59 < 144` at `ker∩coker`: `in(J) ⊊ in(I_1 ∩ I_2)`, so
`J ⊊ I_1 ∩ I_2` at a generic point of every incidence — the base scheme of `Φ`
carries embedded structure along the pairwise incidences of its components,
while being reduced along each component (§1).  This is the precise sense in
which the normal cone of `J` differs from the normal cone of the reduced base
locus, and it is why the exceptional fibre over an incidence is larger than
`P(im dΦ)` (`rank dΦ` drops to 29, 14, 16, 5 there) and why §6 is needed.

## 6. The reducible exceptional image over every incidence, orders 1, 2, 3 (measured)

Order 1: s59's identity `rank d(g_1) − rank d(π g_1)` over `(θ, M_1)` with `θ`
the parameters of the incidence locus (differentiated through the family
builder) and `M_1` generic in `ker(π dΦ)`; both house primes, two seeds, every
V-point verified.  Order 2: for each minimal prime of `Q_2^π` that is not a
tangent space, `M_1` generic in it (in kernel coordinates, mapped back), `M_2`
solving `π g_2 = 0`, and `rank d(g_1, g_2) − rank d(g_1, π g_2)` over
`(θ, M_1, M_2)`; `g_2 ∉ im dΦ` at every such point (they are genuinely new
leading forms).  A prime that is a tangent space adds nothing: `M_1 ∈ T_i`
extends to a curve in `C_i`, after which `g_2 = dΦ(N)` is an order-1 form
(proved in §4's terms; measured as "`g_2 ∈ im dΦ`, image = the order-1 value").
Order 3: `M_1` generic in `T_i` (the only second-order-solvable directions
where `V(Q_2) = T_1 ∪ T_2`), `M_2` cancelling `g_2` plus a kernel part solved
jointly with `M_3` for `π g_3 = 0`, and `rank d(g_1, g_2, g_3) − rank d(g_1,
g_2, π g_3)`.

| locus (dim) | `rank dΦ` | order 1 | order 2, per component of `V(Q_2^π)` | order 3, `M_1 ∈ T_1 / T_2` |
|---|---|---|---|---|
| `P` (43) | 37 | **24** | inert (§4) | inert |
| `SP` (49) | 31 | **26** | inert | inert |
| `ker`, `coker`, `c21`, `c32` | 17, 17, 23, 23 | 29, 29, 28, 28 (s59) | inert | inert |
| `P ∩ SP` (41) | 29 | 16 | **26** (`H`), **23** (`L`) | 23, 26 |
| `P ∩ coker` (40) | 14 | 17 | **24** (`L`); `T_coker`: 17 | 24; 17 (`g_3 ∈ im dΦ`) |
| `P ∩ SP^T` (40) | 28 | 17 | **23** (`L`); `T_{SP^T}`: 17 | 23; 17 |
| `P ∩ c32` (39) | 19 | 14 | **27, 24, 23** | 23, 23, 27 (`T_P`, `T_SP`, `T_c32`) |
| `P ∩ c21` (33) | 17 | 10 | see §8 | — |
| `P_tan` (42) | 37 | 23 | smooth point: inert | inert |
| `SP ∩ c32` (47) | 21 | 18 | **24** (`L`); `T_c32`: 18 | 24; 18 |
| `SP ∩ c21` (46) | 20 | 19 | **25, 28** | 26, 28 |
| `SP ∩ coker` (44) | 12 | 19 | **26, 28** | 26, 28 |
| `c21 ∩ c32` (50) | 16 | 18 | **27, 27** | 27, 27 |
| `ker ∩ c21` (56) | 13 | 18 | **29, 28** | — |
| `ker ∩ coker` (51) | 5 | 29 | **29, 29** (the two generic-kernel components; rank-drop strata not decomposed) | 29, 29 |
| padded-skew rank-2 locus (29) = `P∩ker` = `SP∩ker` | 0 | — | **28, 28, 26, 26** (§7) | 28, 28, 26, 26 |

Maximum over the primitive and semi-primitive world: **28**; over everything
measured: **29**, at `ker ∩ coker`, its own order-1 value.  Nothing reaches
31, let alone 35 (E1 **confirmed**; V **confirmed**).  The audit's `27` for
the "genuinely mixed" second-order direction at `c21 ∩ c32` is reproduced and
placed: it is the image over either of the two extra components of `V(Q_2^π)`
there (the integrator's reading that every kernel direction is such a sum is
right; the second-order-solvable ones form two 59-dimensional linear spaces,
one through each tangent space, and both give 27).

## 7. The rank-`≤2` loci: where `dΦ ≡ 0` (proved + measured)

A pencil of matrix rank `≤ 2` has `adj M_0(s) ≡ 0`, so `dΦ_{M_0} = 0`, every
direction is a first-order kernel direction and every arc has order `≥ 2` with
leading form `e_2(M_0; M_1)`, `M_1` free — the one place where the exceptional
fibre is a quadratic image of all of `X_5`.  This is where `P ∩ ker` and
`SP ∩ ker` live (§0), and it is the "next incidence" of the brief's task 4.
The types (bounded rank 2 in `M_4`): the compressions `(2,0)` [`A(U_2) = 0`,
dim 44], `(4,2)` [dim 44], `(3,1)` [`A(U_3) ⊆ W_1`, dim 41, self-transpose],
and the padded `3×3` skew type `{P·diag(N(x), 0)·Q}` (dim 29), which is
`P ∩ ker`: a rank-3 `φ` with `ker φ = a ∧ C^4` factors through `Λ²(C^4/a) ≅ C^3`
and `M_φ` is the cross-product matrix on `C^4/a`.

**Exactness on the compressions (proved, verified at both primes).**  Over
`(2,0)`, `M_0 = [0 | 0 | X(s)]`, `M_1 = [Y_2 | ∗]`: `e_2 = det[Y_2 | X]`.  Over
`(3,1)`, `M_0 = [w ℓ(s)^T | y(s)]`, `M_1 = [Y | ∗]`: the rank-one update formula
gives `e_2 = ℓ^T adj([Y | y]) w = det(Ñ)` with `Ñ` the pencil whose row 0 is
`(ℓ_0, ℓ_1, ℓ_2, 0)` and rows 1–3 are those of `[Y | y]` (Laplace along row 0).
Both are honest `4×4` determinants of linear pencils (`analysis/wk10_s66_rank2.py::verify_exactness`, equal coefficient-by-coefficient at
random points, both primes, two seeds), so the order-2 exceptional image over
these loci lies in `Φ(X_5)` (measured dimension 50 = dense in `D_5`) and its
reducible part in the exact locus, `≤ 31` by s32/s59.  `(4,2)` by transposition;
the rank-`≤1` locus `{wλ(s)^T}` gives at order 3 `λ^T adj(M_1) w = det(M_1 with
row 0 → λ)`, exact again.

**The padded-skew type (measured).**  In the standard frame, with `M_1 =
[[A, b],[c^T, m]]`, `e_2 = m·(x^T A x) − (x^T b)(c^T x) = m q − βγ`; the full
order-2 image has dimension **49** (both primes): a divisor of `D_5`, the
candidate for the `n = 4` analogue of the Hüttenhain–Lairez skew component.
`π e_2 = 0` reads `m'q' = β'γ'` in `F[s_1..s_4]`; `m'` is linear and the ring a
UFD, so the V-variety is the union of **four** explicit components — `(i)
m' = β' = 0` (`M_1'e_3 = 0`, common kernel with `M_0'`), `(ii)` common cokernel,
`(iii)` `M_1' = v·w(s')^T` (rank-one pencil with a fixed column), `(iv)` its
transpose — and their order-2 reducible images are **28, 28, 26, 26**; the
order-3 arcs (`M_1` in each of the four types with `e_2 ≡ 0`, `M_2` solving
`π g_3 = 0`) give **28, 28, 26, 26** again.  Both primes, two seeds
(`results/s66_skew_orders.json`).  Note that the naive V-points on the
compression loci (`M_1'` inside a compression space through `M_0'`) are
singular points of the V-variety (the constraint differential vanishes there:
`rank_con = 0`), where s59's identity is not valid — the number it returns
there (33 at `(3,1)`) is not a bound in either direction and is recorded only
so that no one re-derives it; the exactness argument settles those loci.

## 8. Honest boundary

- **Proved:** the contact-order lemma (§4); the bilinear reduction and its
  multi-component form (§5); the exactness identities on the rank-2
  compression loci and the four-component factorisation on the padded-skew
  locus (§7); the identification of `P ∩ ker` with the padded-skew locus, of
  `P_meet` with `P ∩ SP^T`, and of the `k = 3` stratum with a 49-dimensional
  component absent from s54/s59.
- **Measured (exact, two primes, two seeds, KC2–KC4 on every run):** the
  tangent table (§3); `dim Q_2` and the union-ideal bounds; the decompositions
  of `Q_2` and `Q_2^π` at nine incidences (at `32003` and `1000003`, identical);
  the order-1 images over every locus; the order-2 images over every component
  of `V(Q_2^π)` found; the order-3 images at every two-component incidence and
  on the skew locus.
- **Independently re-derived (third prime `2147483587`, `analysis/wk10_s66_indep.py`,
  no shared code):** `dΦ` by an explicit cofactor adjugate and the tangent
  spaces by sympy's symbolic Jacobian give generic `P`: `37 / 43 / 43 / 0`;
  generic `SP`: `31 / 49 / 49 / 0`; `P ∩ SP`: `rank 29`; `P ∩ coker`: `rank 14`.
- **Adopted:** Atkinson's classification of bounded-rank-3 spaces through
  Huang–Landsberg and s32 Theorem 4 (the eight types exhaust `B_5`; used to say
  that an extra linear component of `V(Q_2)` is not a hidden base-locus
  component); s32/s59 for the certified `31`; `dim D_5 = 50`.
- **Not done / open:** (1) `P ∩ c21` (rank-2 `u`, `P` singular there): the
  reduced `Q_2` (18 quadrics, 30 variables) did not finish in the 25-minute
  box, and `Q_2^π` (9 quadrics) did not finish in Singular (25 min) or in
  Macaulay2's `minimalPrimes` (15 min) — its order-2 image is the one number of
  the primitive world not on the table (order 1 there is 10; the locus is
  33-dimensional and every direction in it is a first-order direction of the
  singular locus of `P`); (2) the rank-drop strata of `M(a)` at `ker ∩ coker` (a compression-world
  point, outside the brief's target); (3) contact order `≥ 4` at the
  incidences, and order `≥ 3` with `M_1` outside the tangent spaces where
  `V(Q_2)` has an extra component (`P ∩ c32`, `SP ∩ c21`); (4) deeper strata of
  the rank-`≤2` world (incidences of the four rank-2 types with each other).
  By the lemma of §4 none of these can be a smooth point of `V(J)`, and every
  one of them is a proper closed subset of a locus already measured; a hidden
  component of `E` over them would have to have a fibre of dimension
  `79 − dim(locus)` larger than anything seen here.  It is not excluded; it is
  named.
- **What this does not do:** prove `R_5 ⊄ D_5`.  That still needs the upper
  bound — the special-fibre algebra of `J`, or a length-5 equation of `I(D_5)`
  above degree 9.  What it does is remove, at orders 1–3 and at every
  incidence of the primitive family, the last mechanism the roadmap had for
  a climb, and replace "no exotic direction at the compression incidences"
  with "no exotic direction anywhere, and no reducible image above 29 anywhere".

## 9. Pre-registration scorecard

| id | prediction | prior | outcome |
|---|---|---|---|
| C0 | eight components with the stated dimensions, `ker = T` at generic points | 0.75 | **confirmed** (all eight) |
| T0 | generic `P`: `37 / 43 / 43 / 0` | 0.80 | **confirmed** exactly |
| T0' | `P^T`, `SP^T` as `P`, `SP` | 0.95 | **confirmed** |
| T1 | generic `SP`: `ker = 49 = T`, quotient 0 | 0.60 | **confirmed** (`31 / 49 / 49 / 0`) |
| T2 | `P ∩ coker`: `14 / 66 / 66 / 0` | 0.60 | **confirmed** exactly |
| T3 | `P ∩ SP`: `29 / 51`, quotient 0; Jacobian image of `P` `≤ 40` | 0.55 | kernel and quotient **confirmed**; the `≤ 40` clause **refuted** (43 — `Y_3 ∧ C^4 = Λ²C^4`); the artefact appears at rank-2 `u` instead (39 → 43) |
| T4 | `P ∩ c21`, `P ∩ c32`, `P ∩ ker`: quotient 0 | 0.50 | `P ∩ c21`, `P ∩ c32` **confirmed**; `P ∩ ker` **void** (rank-`≤2`, `dΦ ≡ 0`) — the pre-registered dims 37 and 34 for these loci were miscounted (33, and not a rank-3 locus) |
| T5 | `P_tan`, `P_meet`: `43 = T_P`, quotient 0 | 0.50 | `P_tan` **confirmed** (smooth); `P_meet` quotient 0 **only with `SP^T`** — the pre-registration's "no other component" was wrong, and the locus is codimension 3, not 1 |
| Q0 | generic `P`: `Q_2 = 0` | 0.90 | **confirmed** |
| Q1 | `P ∩ SP`: `dim Q_2 = 16` | 0.40 | **refuted** (12) — yet `V(Q_2) = T_P ∪ T_SP` exactly; the shortfall is the non-reducedness of `J` (§5), a better result than the prediction |
| E1 | every incidence image `≤ 31` at `q = 1, 2` | 0.75 | **confirmed**, extended to `q = 3` and to the rank-2 loci; maximum 29 |
| V | no transverse direction anywhere in the primitive world | 0.55 | **confirmed** at all 17 rank-3 points |

Unregistered findings: the contact-order lemma; the bilinear reduction; the
non-reducedness of `J` along incidences; `SP` as a missing component; `P ∩ ker`
as the padded-skew rank-2 locus with its four-component V-variety; the
exactness identities on the rank-2 compressions; the 49-dimensional order-2
image over the padded-skew locus.

## 10. Engineering notes worth keeping

- Singular `minAssGTZ` on the second-order systems is instantaneous **after**
  the bilinear reduction and hopeless before it (`std` alone exceeded 30 min at
  66 variables).  Drop the intersection coordinates first; then decompose.
- The limit tangent space along a curve (Smith-type elimination over
  `F_p[ε]/ε^4`, `wk10_s66_core.limit_colspace`) is the right tool where a
  parametrisation's fibre jumps (rank-2 `u`); it restored `39 → 43` and
  `48 → 49` and never produced a vector outside `ker dΦ`.
- s59's identity is valid only at smooth points of the constraint variety.
  Check `rank_con` against the expected codimension; `rank_con = 0` at a
  V-point built inside a compression space (§7) is the signature of a singular
  V-point and the number returned there is meaningless.
- All CAS runs launched under `timeout` with pids in `results/logs/`; the two
  full-variable sweeps were ended by explicit pid (`5459/5473`, `5656/5657` and
  their Singular children) when the reduction made them redundant, and the
  logs say so in place.
- Commit trailers carry `Co-Authored-By` only (standing rule; the harness's
  session-link line was removed from the first commit before it was banked).

## 11. Flags for the single writer, and one line for the roadmap

No single-writer file touched.  For `docs/boundary_deficit.html` /
`paper/det3-conductor.tex` the integrator may want: the contact-order lemma
(§4) as the statement that makes s59's table a theorem; the eight-component
list with `SP` (§1); and the sentence "the base scheme of `Φ` at `r = 5` is
generically reduced along every component and non-reduced along every pairwise
incidence".

Roadmap: the special-normal-cone loophole at the primitive family is closed at
orders 1–3 at every listed incidence, with maximum reducible image 28 in the
primitive world and 29 overall; the remaining hiding places are named in §8
(`P ∩ c21` at order 2, the rank-drop strata at `ker ∩ coker`, orders `≥ 4`, the
deeper rank-2 strata) and each is a proper closed subset of a measured locus.
The proof of `R_5 ⊄ D_5` still needs an upper bound, and nothing in this
session changes what that object is.
