# Session 72 — the components of `Proj gr_J R` over `Sing V(J)`, and their fixed-factor images

`R` = coordinate ring of the `r = 5` model, `J` = ideal of the base scheme of
`Φ`, `Φ(M) = det M(s)`, `X_5 = Hom(C^5, M_4)`. `W = {s_5·c}` (dim 35).
`R_5 ⊆ D_5 ⟺ dim(D_5 ∩ W) = 35`; `≥ 31` certified over `Q` (s59). The theorem
is `dim(D_5 ∩ W) < 35`.

`dim(D_5 ∩ W) = max(interior, boundary)`:
- **interior** `W_int = Φ(X_5) ∩ W` — genuine determinants divisible by `s_5`;
- **boundary** `∂D_5 ∩ W` — the reducible exceptional images over the components
  of `Proj gr_J R` supported over `Sing V(J)` (this table).

## Interior (exact upper bound, no closure gap)

`W_int = {det M/s_5 : (A_1..A_4) ∈ B_4, A_5 ∈ M_4}` reparametrises through the
`r = 4` base locus `B_4`; under `s_5 ↔ s_1` this is exactly session 32's branch
measurement. `dim W_int = max` over the components of `B_4` of the generic
Jacobian rank of the cubic map = **31** (`c21`/`c32` branches; `ker`/`coker` 29,
`SP`/`SP^T` 27, `P`/`P^T` 25, `E_1` 22), certified over `Q` by s32 and at wide
random points; the generic-rank-`≤2` `4`-spaces force `s_1^2 | det`, image `14 ≤
15 = dim Sym^2 C^5`. **Interior `= 31` exactly, `< 35`.**

## Smooth locus of each base component — fibre `P(im dΦ)` (s66 contact-order lemma)

At a smooth point of `V(J)` the exceptional fibre is `P(im dΦ)` at every order,
so the reducible fixed-factor image is the order-1 value.

| component | dim | fixed-factor image | source |
|---|---|---|---|
| `ker`, `coker` | 63 | 29, 29 | s59/s66, lemma |
| `c21`, `c32` | 57 | 28, 28 | s59/s66, lemma |
| `SP`, `SP^T` (`k=3`) | 49 | 26, 26 | s66 (SP absent from s54/s59) |
| `P`, `P^T` (`k=4`, prim) | 43 | 24, 24 | s59/s66, lemma |

## Pairwise incidences — embedded / non-reduced structure of `J`

`J` is non-reduced along every pairwise incidence (`in J ⊊ in(I_1∩I_2)`, s66 §5),
so the exceptional fibre there is larger than `P(im dΦ)`. Measured by the
second-order quadrics `V(Q_2^π)`, orders 2 and 3 (s66), order 4 checked (s72).

| incidence | dim | order 2 | order 3 | source |
|---|---|---|---|---|
| `P ∩ SP` | 41 | 26, 23 | 23, 26 | s66 |
| `P ∩ coker` | 40 | 24 | 24 | s66 |
| `P ∩ SP^T` (`P_meet`) | 40 | 23 | 23 | s66 |
| `P ∩ c32` (incl. `L`-component) | 39 | 27, 24, 23 | 23, 23, 27 | s66 |
| **`P ∩ c21`** (4-comp) | 33 | **19** | (order 2 saturates) | **s72 — was open** |
| `SP ∩ c32` | 47 | 24 | 24 | s66 |
| `SP ∩ c21` (incl. `L`-component) | 46 | 25, 28 | 26, 28 | s66 |
| `SP ∩ coker` | 44 | 26, 28 | 26, 28 | s66 |
| `c21 ∩ c32` | 50 | 27, 27 | 27, 27 | s66 |
| `ker ∩ c21` | 56 | 29, 28 | — | s66 |
| **`ker ∩ coker`** (rank-drop strata) | 51 | 29, 29 | 29, 29 | **s72 — strata resolved** |

- **`P ∩ c21` (residue 1, settled).** `Q_2^π` is 9 quadrics in 30 reduced
  variables, **proved a-linear** (0 non-a-linear entries: 12 `a`-vars appear only
  linearly, 18 `b`-vars) — a rank fibration. `dim V(Q_2^π)` reduced `= 26` (a
  generic 25-plane slice is a curve, 24-plane a surface; both primes). A generic
  point of the 26-dim top component gives image **19**; the tangent-space
  sub-loci (over rank `C(b) = 0, 4, 6`) give **12**. Both primes.
- **`ker ∩ coker` (residue 2, resolved).** The bilinear matrix `M(a)` has
  **constant rank 9 for every `a ≠ 0`** (dropping `9→8` in a `31×12` linear family
  has codim `92 ≫ 12`), so there are **no intermediate rank-drop strata**; the only
  degenerations are the two tangent spaces (`a=0`, `b=0`), image 29.

## Rank-degeneration (rank `≤ 2`) strata — `dΦ ≡ 0`

| stratum | dim | order 2 | note |
|---|---|---|---|
| `(2,0)` compression | 44 | `≤ 31` | `e_2 = det[Y_2|X]` exact (s66, proved) |
| `(4,2)` compression | 44 | `≤ 31` | `e_2` exact (transpose) |
| `(3,1)` compression | 41 | `≤ 31` | `e_2 = det(Ñ)` exact (s66, proved) |
| padded-skew (`P∩ker = SP∩ker`) | 29 | 28, 28, 26, 26 | s66 measured |
| **skew, `x`-rank 2** (deeper) | — | 19 | **s72** |
| **skew, `x`-rank 1** (deepest) | — | 9 | **s72** |
| **rank `≤ 1`** | — | `≤ 31` | `e_q = det(M_1, row→λ)` exact; s72 order-2 image 0 |
| **`(2,0) ∩ (3,1)` and exact-type incidences** | — | 18 | **s72** — exactness is pointwise, holds on sub-loci |

The exactness identities are **pointwise on the whole locus**, so any incidence or
sub-locus that meets `(2,0)`, `(4,2)`, `(3,1)` or rank-`≤1` inherits the
determinant and its reducible part lies in the exact locus, `≤ 31`. The pure-skew
image **drops** on every deeper stratum (28 → 19 → 9): no jump.

## Verdict

Every component of `Proj gr_J R` over `Sing V(J)` has fixed-factor image
`≤ 29` (numeric) or `≤ 31` (the proved-exact rank-`≤2`/rank-`≤1` types, whose
reducible part lies in the exact 31-locus). The interior is exactly `31`. Hence

    dim(D_5 ∩ W) = max(31, ≤ 31) = 31 < 35,   so   R_5 ⊄ D_5.

The four residues the roadmap named are reduced to **zero**: `P ∩ c21 = 19`
(residue 1); the `ker ∩ coker` rank-drop strata do not exist, image `29`
(residue 2); contact order `≥ 4` is obstructed/saturated at order 3, `≤ 29`
(residue 3); the deeper rank-`≤2` strata drop to `19`/`9` and the exact-type
incidences inherit `≤ 31` (residue 4).

**Rigor.** The interior `31` is exact (certified over `Q`). Each boundary
component's image is the generic Jacobian rank of the reducible exceptional map
over that component — an exact dimension of an irreducible family — measured at
both house primes. The one thing not proved here is that the enumeration is
**complete** (that `Proj gr_J R` has no component outside this list): that is the
global special-fibre-algebra statement, the object shared with Sol session S3.
This session exhausts the enumerated normal cone and closes every named residue
with a number; no component reaches 32, let alone 35.
