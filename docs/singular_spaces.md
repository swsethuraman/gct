# Four-dimensional singular subspaces of `M_4(C)`, and the length-5 non-containment

Session 32 (2026-09-01), branch `s32-singspaces`.
Pre-registration: `results/PREREG_s32.md` (committed before any literature
reading or computation).  Record: `docs/session_32.md`.
Clone tip `13fb170`; ancestry check passed (`1203fe4` an ancestor).

---

## 0. Verdict

**The soft joint of `docs/l5_containment.md` is false as stated, and the
conclusion it was protecting is true anyway — now unconditionally.**

- It is **not** true that every 4-dimensional singular subspace of `M_4(C)` is
  contained in a compression space.  The smallest counterexample is the
  4-dimensional space `{ diag(N(x), w) }` of a `3x3` skew matrix padded by a
  scalar; it lies in no compression space of any of the four types.  So the
  branch list in `docs/l5_containment.md` was **incomplete**.
- The missing branches have been classified — completely, with proof (§2) — and
  measured.  There are exactly **two** exceptional strata beyond the four
  compression branches, and their ranks are **27** and **25**, both below the
  compression maximum of 31.
- **The containment therefore fails, and the statement is now a theorem, not a
  theorem-modulo-a-classification.**  The generic reducible quinary quartic
  `ell . c` is *not* a `4x4` determinant of linear forms.  The shortfall is 4
  dimensions, exactly as measured before; the integrator's table survives
  unchanged and gains a proof.
- The integrator's four ranks `29, 31, 31, 29` were independently reproduced by
  a from-scratch implementation sharing neither the derivative mechanism nor the
  arithmetic (§4), and the `29 = dim D_5^{det_3}` coincidence was upgraded from
  an equality of numbers to an **identity of polynomials** (§4, C2).

## 1. The question, self-contained

`M(s) = sum_{i=1}^{5} s_i A_i` with `A_i in M_4(C)`; `F = det M in Sym^4 C^5`.

**Lemma 1.** `s_1 | F` iff `S_0 := span(A_2,...,A_5)` consists of singular
matrices.  *Proof.* `F|_{s_1 = 0} = det M_0(y)`, `y = (s_2,...,s_5)`. ∎

Write `G = F / s_1 in Sym^3 C^5`, the cubic `c` of the question.

**Lemma 2.** `G|_{s_1 = 0} = tr( adj(M_0(y)) . A_1 )`.
*Proof.* Jacobi: `dF/ds_1 = tr(adj(M) A_1)`; and `F = s_1 G` gives
`dF/ds_1 = G + s_1 dG/ds_1`; set `s_1 = 0`. ∎

**Corollary 3 (bounded rank `<= 2` cannot contribute).** If `M_0(y)` has generic
rank `<= 2` then `adj(M_0) = 0` identically, so `s_1 | G`, so `s_1^2 | F` and the
cubic is not generic.  *Hence for this question `S_0` may be assumed to have
generic rank exactly 3.*  (Verified computationally, `wk8_s32_checks.py` C4.)

A **compression space** is `{ A : A(U) subseteq W }` with `dim W = dim U - 1`;
in a basis it is the mask with a zero block of size `(5-k) x k`, `k = dim U`.
Those are the four branches the integrator measured.

## 2. The classification

**Theorem 4.**  Let `S_0 subseteq M_4(C)` be a 4-dimensional space of singular
matrices of generic rank 3, presented as the image of an injective linear
`M_0 : C^4 -> M_4(C)`.  Then, after replacing `M_0` by its transpose if
necessary, there are an integer `k in {1,2,3,4}`, a linear map
`L : C^4 -> C^4` of rank `k`, and a linear map `phi : Lambda^2 C^4 -> C^4`
vanishing on `C^4 ^ ker L`, such that

        M_0(y) L t  =  phi(y ^ t)      for all  y, t in C^4,
        M_0(y) L y  =  0               (the kernel of  M_0(y)  is  L y).

Conversely every such pair `(L, phi)`, with the columns of `M_0` off `im L`
chosen arbitrarily linear in `y`, produces a 4-dimensional singular space.

Concretely, in bases with `ker L = <f_{k+1},...,f_4>` and `L f_j = f_j` for
`j <= k`, writing `phi_{ij} = phi(f_i ^ f_j)` (`= 0` unless `i, j <= k`):

        column j of M_0(y)  =  sum_i y_i phi_{ij}        for j <= k
        column j of M_0(y)  =  arbitrary linear in y     for j >  k

*Proof.*  `adj(M_0(y))` is a `4x4` matrix of **cubic** forms in `y`, not
identically zero (generic rank 3), and of rank `<= 1` at every `y`.  All its
`2x2` minors therefore vanish identically; over the UFD `C[y]` such a matrix
factors as `adj(M_0) = f . u v^T` with `u`, `v` vectors of forms whose entries
are coprime and `f` a form, so `deg f + deg u + deg v = 3`.  From
`M_0 . adj(M_0) = det(M_0) I = 0` and `f v^T != 0` we get `M_0(y) u(y) = 0`;
dually `v(y)^T M_0(y) = 0`.

Transposing `S_0` leaves `det(s_1 A_1 + M_0(y))` unchanged (`det X^T = det X`,
and `A_1` is free), and replaces `adj(M_0)` by its transpose, exchanging `u` and
`v`.  So **WLOG `deg u <= deg v`, hence `deg u <= 1`.**

- `deg u = 0`: `u` constant, `M_0(y) u = 0` for all `y` — a common kernel, i.e.
  `S_0` is inside the `k = 1` compression space.  (This is the `k = 1` case of
  the display above: with no pairs `i < j <= 1` the first column of every
  `M_0(y)` is zero and the rest are free.)
- `deg u = 1`: write `u(y) = L y`.  Then `beta(y,t) := M_0(y) L t` is bilinear
  with `beta(y,y) = M_0(y) u(y) = 0`, hence **alternating**, hence factors
  through `Lambda^2 C^4`: `beta(y,t) = phi(y ^ t)` for a unique `phi`.  Since
  `beta(y,t)` depends on `t` only through `L t`, `phi(y ^ t) = 0` whenever
  `L t = 0`, i.e. `phi(C^4 ^ ker L) = 0`.  Normalising `L` (a change of basis in
  the `y`-space and a constant right multiplication of `M_0`) gives the display.

Conversely, for any such `(L, phi)`, `M_0(y) L y = phi(y ^ y) = 0`, so `M_0(y)`
is singular wherever `L y != 0`, hence identically. ∎

**Which strata are compression spaces.**

- `k = 1` **is** the common-kernel compression space, as just noted.
- `k = 2` **is** the `2 -> 1` compression space.  Only `phi_{12}` survives, so
  columns 1 and 2 of `M_0(y)` are `-y_2 phi_{12}` and `y_1 phi_{12}`: every
  member compresses `<f_1, f_2>` into the fixed line `<phi_{12}>`.  Conversely a
  `2 -> 1` compression space has kernel `beta(y) f_1 - alpha(y) f_2` with
  `alpha, beta` linear, i.e. `deg u = 1` and `rank L = 2`.
- `k = 3` and `k = 4` are **not**, in general.  Explicitly:
  - `k = 3` contains `E_1 = { diag(N(x), w) }`, `N(x) y = x times y` the `3x3`
    skew matrix (kernel `(x,0)`, so `L = diag(1,1,1,0)`).  `E_1` lies in no
    compression space: a common kernel is impossible because `N(x) u != 0` for
    `x` not parallel to `u` and `w u_4 != 0` for `w != 0`; for `dim U = 2` any
    `0 != u in U cap C^3` already has `{N(x) u} = u^{perp}` of dimension 2; for
    `dim U = 3` two independent `u_1, u_2 in U cap C^3` give
    `u_1^{perp} + u_2^{perp} = C^3` inside a 2-dimensional `W`; and the images
    span `C^4`, so there is no common cokernel.
  - `k = 4` (`L` invertible, so `M_0(y) t = phi(y ^ t)` after normalisation) is
    in no compression space whenever `phi` is surjective, i.e. for generic
    `phi`.  A common kernel would need the 3-dimensional `C^4 ^ t` inside the
    2-dimensional `ker phi`; a common cokernel would need
    `phi(Lambda^2 C^4) = C^4` inside a hyperplane; a `2 -> 1` compression would
    need `phi` to send `C^4 ^ t_1 + C^4 ^ t_2` (dimension `>= 5`) into a line,
    forcing `dim ker phi >= 4`; a `3 -> 2` compression would need
    `phi(C^4 ^ U) = phi(Lambda^2 C^4) = C^4` inside a plane.  All impossible.

**Completeness.**  Up to transpose (which does not change the cubic) and
excluding generic rank `<= 2` (Corollary 3), the four strata `k = 1,2,3,4`
exhaust the 4-dimensional singular subspaces of `M_4(C)`.

## 3. The literature, and how it matches

The classification of spaces of matrices of bounded rank is classical.

- **M. D. Atkinson and S. Lloyd, "Primitive spaces of matrices of bounded
  rank", J. Austral. Math. Soc. Ser. A 30 (1981), no. 4, 473–482**
  (doi:10.1017/S144678870001795X).  A weak canonical form reduces the structure
  of any space of bounded rank `r` to that of an associated *primitive* space,
  and bounds the size of primitive spaces by functions of `r`.  They classify
  `r <= 2`: the only primitive space is the `3x3` skew-symmetric space.
- **M. D. Atkinson, "Primitive spaces of matrices of bounded rank. II",
  J. Austral. Math. Soc. Ser. A 34 (1983), no. 3, 306–315**
  (doi:10.1017/S1446788700023740).  Classifies the primitive spaces of bounded
  rank 3 and thereby, in the abstract's own words, gives a complete description
  of "spaces whose matrices have rank at most 3".
- **D. Eisenbud and J. Harris, "Vector spaces of matrices of low rank",
  Adv. Math. 70 (1988), 135–155.**  Re-proves and extends the above by vector
  bundle methods over an algebraically closed field.
- **C. de Seguins Pazzis, "The classification of large spaces of matrices with
  bounded rank", Israel J. Math. (arXiv:1004.0298).**  Extends Atkinson–Lloyd
  to all fields, for spaces of dimension `>= nr - r + 1`.  *Not applicable
  here*: our spaces have dimension 4 while `nr - r + 1 = 4.3 - 3 + 1 = 10`, so
  they are far below the "large" regime.  This is worth recording because the
  most easily found modern reference is the one that does **not** cover this
  case.
- **H. Huang and J. M. Landsberg, "On linear spaces of matrices of bounded
  rank", Selecta Math. (N.S.) 32 (2026), no. 2, Paper No. 30**
  (doi:10.1007/s00029-026-01137-x).  Modern account; classifies the *fundamental*
  bounded-rank-4 spaces, and restates the earlier results.  It records that
  "there are no non-classical examples of spaces of bounded rank when `r <= 3`",
  and that for `r = 3` **"the only primitive examples are Example 2.3 and its
  projections"**, Example 2.3 being

        C^a  ->  Hom(C^a, Lambda^2 C^a),   e |-> (v |-> e ^ v),

  of bounded rank `a - 1`.

**The match is exact.**  For `r = 3` take `a = 4`: the primitive example is
`e |-> e ^ .` from `C^4` to `Hom(C^4, Lambda^2 C^4)`, and its *projections* are
the composites with a linear `phi : Lambda^2 C^4 -> C^4`.  That is precisely the
`k = 4` stratum of Theorem 4, and the `k < 4` strata are its degenerations
(`L` non-invertible, with the columns off `im L` free).  So Theorem 4 is the
`4x4`, dimension-4 case of Atkinson's 1983 classification, re-derived here from
scratch so that nothing downstream rests on a reading of a paywalled 1983
paper.

**A caution about the phrase "no non-classical examples".**  It refers to
*primitive* spaces, and does **not** say that every bounded-rank space is a
compression space.  `E_1` is entirely classical — it is the `3x3` skew space
padded by a block, and it is imprimitive (restrict to the hyperplane `w = 0` and
the bounded rank drops to 2) — and it is still in no compression space.  That is
exactly the gap the integrator's soft joint fell into.

## 4. The measurements

For each branch: parametrise, form `M(s) = s_1 A_1 + M_0(y)`, assert
`s_1 | det M` and `s_1 | d(det M)` along every tangent direction (so the
parametrisation provably stays inside the branch), and take the exact rank of
`params -> coefficients of G = det M / s_1` in `Sym^3 C^5` (35 coordinates).
`rank = 35` would mean containment.

Implementation `analysis/wk8_s32_branches.py` shares nothing with
`analysis/l5contain.py`: the determinant is expanded by Leibniz over **dual
numbers** (`a + eps b`, `eps^2 = 0`), so the `eps`-part *is* the directional
derivative and no adjugate/cofactor identity is used; and ranks are taken
exactly over **Q** and modulo two primes unrelated to `2^61 - 1`.

| branch | rank | of 35 | compression? |
|---|---|---|---|
| `k = 1` common kernel `A(V_1) = 0` | **29** | | yes |
| `k = 2` compression `A(V_2) <= W_1` | **31** | | yes |
| `k = 3` compression `A(V_3) <= W_2` | **31** | | yes |
| `k = 4` common cokernel `im A <= W_3` | **29** | | yes |
| stratum `rank L = 1` (reproduces `k = 1`) | **29** | | yes |
| stratum `rank L = 2` (reproduces `k = 2`) | **31** | | yes |
| **stratum `rank L = 3`** | **27** | | **no** |
| **stratum `rank L = 4`** | **25** | | **no** |
| transposes of the two exceptional strata | 27, 25 | | |
| `E_1 = { diag(N(x), w) }` alone | 22 | | no |

**Maximum 31 of 35, over a now-complete branch list.**

Internal checks, all passing (`analysis/wk8_s32_checks.py`):

- **C1.** `dim D_r^{det_3}` recomputed from scratch: `10, 20, 29, 38` for
  `r = 3,4,5,6`.  `dim D_5^{det_3} = 29` is the common-kernel branch rank, and
  `dim D_4^{det_3} = 20 =` all 4-ary cubics is session 27's fact.
- **C2.** The common-kernel branch cubic **is** a `3x3` determinant of linear
  forms — verified as an identity of polynomials at three independent points,
  not merely as an equality of dimensions.  This upgrades the brief's "built-in
  consistency check" from a numerical coincidence to a proof.
- **C3.** `E_1`'s cubic reduces mod `s_1` to (linear) x (quadratic), by exact
  factorisation — the structure predicted in `results/PREREG_s32.md` §3.
- **C4.** Corollary 3, checked: a generic-rank-`<=2` branch gives `G` vanishing
  identically on `s_1 = 0`.
- **Transpose symmetry.**  The table is transpose-symmetric (`29/29`, `31/31`,
  `27/27`, `25/25`), as Theorem 4's WLOG requires.
- **The Grassmannian diagnostic.**  Measuring each stratum on the slice where
  `L` is normalised, *without* restoring the `GL_4` acting on `(s_2..s_5)`,
  gives `29, 27, 24, 25`; the deficits against the true `29, 31, 27, 25` are
  `0, 4, 3, 0 = k(4-k)`, the dimension of the Grassmannian freedom that the
  normalisation consumes.  This is the sharpest confirmation that the
  stratification bookkeeping is right — and it caught a real bug (see
  `docs/session_32.md` §4).

**Upper-bound certification.**  A Jacobian rank at a point is only a *lower*
bound for the generic rank, and the claim needs the upper bound.  If the generic
rank of a branch were `>= 32`, some `32 x 32` minor of the Jacobian would be a
nonzero polynomial in the parameters of degree `<= 32 . 3 = 96` (each Jacobian
entry is a cubic in the parameters).  Re-running every branch with parameters
drawn uniformly from a box of half-width `10^9`, modulo two large primes,
returns the same ranks at all three points; Schwartz–Zippel bounds a false low
reading by `96 / (2.10^9 + 1) < 5 . 10^{-8}` per point.  Certified maximum: 31.

## 5. The theorem

> **Theorem 5.**  Let `c` be a general cubic form in five variables and `ell` a
> linear form.  Then `ell . c` is **not** the determinant of a `4x4` matrix of
> linear forms in five variables.  The locus of cubics `c` for which `ell . c`
> *is* such a determinant is irreducible-component-wise of dimension at most
> **31** inside the 35-dimensional space of quinary cubics; the maximum is
> attained, on the two middle compression branches.

*Proof.*  Lemma 1 reduces the question to 4-dimensional singular subspaces
`S_0 subseteq M_4(C)`; Corollary 3 discards generic rank `<= 2`; Theorem 4
classifies the rest into four strata up to transpose, and the transpose does not
change the cubic; §4 measures each stratum's reachable family and certifies the
maximum as 31 `< 35`. ∎

> **Corollary 6.**  `D_5^{per_3^{pad}}` is **not** contained in `D_5^{det_4}`.
> The length-5 stratum at `n = 4` is *not* closed by containment.

Consequences, as `docs/l5_containment.md` §4 already set out and which now hold
without a caveat: the nine measured `D = 0` cells at length 5 are **unexplained**
— no containment forces them — and the 62 unmeasured cells at `delta = 6` are
genuinely open.  The caution there also stands unchanged: non-containment
removes the argument that `D <= 0`; it does not produce `D > 0` anywhere, and
the two ideals can still have equal multiplicities at every weight while being
different subspaces.

## 6. Task E: where the stacking trick lives and dies

`{ell . c}` is contained in `D_r^{det_n}` **by stacking** — `ell . c =
det diag(ell, M)` — exactly when every `r`-ary form of degree `n - 1` is an
`(n-1) x (n-1)` determinant of linear forms, i.e. when
`D_r^{det_{n-1}} = Sym^{n-1} C^r`.  Measured (C1/C5):

| `r` | 3 | 4 | 5 | 6 |
|---|---|---|---|---|
| `dim D_r^{det_3}` | 10 | 20 | 29 | 38 |
| `dim Sym^3 C^r` | 10 | 20 | 35 | 56 |
| stacking | works | works | fails by 6 | fails by 18 |

So at `n = 4` the stacking trick survives exactly for `r <= 4` — session 27's
theorem — and this is the Beauville criterion in the programme's own notation: a
general hypersurface of degree `d` in `P^{r-1}` is a linear determinant only for
`r <= 3`, or `r = 4` and `d <= 3`.  What this session adds is that at `(n,r) =
(4,5)` the failure of stacking is **not** repaired by any other representation:
the shortfall is not an artefact of the construction.  For `r >= 6` at `n = 4`
the stacking gap widens and the branch classification needed to close the
question the same way is the classification of 5-dimensional singular subspaces
of `M_4(C)`, which is a strictly harder object and is not attempted here.

## 7. Honest boundary

- **Proved outright:** Lemmas 1–2, Corollary 3, Theorem 4 (the classification,
  with the non-containment-in-a-compression-space arguments for `E_1` and for
  surjective `phi`), the transpose reduction, and the identification of the
  `k = 1, 2` strata with compression spaces.
- **Computed exactly, and certified:** the eight branch ranks, over `Q` and
  modulo two primes at small points, and modulo two large primes at wide random
  points with the Schwartz–Zippel bound above.  Theorem 5's `31` is therefore a
  computation with an explicit failure probability `< 10^{-7}`, not a
  closed-form proof.  **That is the one place where the result is
  computer-assisted rather than proved on paper.**
- **Independently reproduced:** the integrator's `29, 31, 31, 29`, by code
  sharing neither derivative mechanism nor arithmetic with `l5contain.py`.
- **Read, not verified first-hand:** Atkinson's 1983 classification.  Its
  statement is quoted here from Huang–Landsberg 2026; the 1983 paper itself is
  paywalled and was not read.  **Nothing in §5 depends on it** — Theorem 4 is
  proved here — so this is corroboration, not a load-bearing citation.
- **Not determined:** whether the `k = 3` and `k = 4` strata are *irreducible*
  as varieties of subspaces (irrelevant to the dimension count, since the
  Jacobian rank at a random point bounds every component through that point,
  and the certification was run per stratum).
- **Not attempted:** `r >= 6` at `n = 4`; `n = 5`; and the ideal-versus-dimension
  question flagged at the end of `docs/l5_containment.md` §4 (compute `U_det`
  and `U_pad` as subspaces at one length-5 weight, not just their dimensions).
  That last one is, on the evidence here, the most informative next computation.
