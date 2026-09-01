# PRE-REGISTRATION — closing the classification joint (session 32)

Committed **before** any literature reading beyond a list of paper titles, and
before any computation.  Branch `s32-singspaces`, fresh clone of public
`origin/main`.

**Tip at clone: `13fb170`.  Ancestry check PASSED** — `1203fe4` is an ancestor
(commits above it are expected and present).  No rollback alarm.

**Two notes for the integrator, before anything else.**

1. `s28-d5` **is** merged now (`e514b3d`), so `docs/d5_ideal.md`,
   `docs/paper_section4_draft.md`, `results/PREREG_s28.md` and the `r >= 3`
   correction to `docs/isotypic_rank.md` §4 are all on `main`.  Good.
2. **`s31-quiver` is NOT merged.**  `docs/quiver_route.md`,
   `docs/session_31.md`, `results/PREREG_s31.md` and `analysis/wk8_s31_si.py`
   are absent from `main`; they exist only in the delivered bundle.  Session 31's
   headline (the quiver dictionary is exact, `dim SI^tau = sum m_det . dim S_lam`,
   and the dimension crossover lands near 145, far above the discriminant's 80,
   so no counting route reaches `delta_0`) is therefore not in the repository.

Calibration (`analysis/wk6_s26_regress.py`) run before writing this file:
**all checks passed, 18 s**, including `1, 6, 31, 141, 618, 2488` and the det/per
Jacobian tables `4,10,20,29,38` / `4,10,20,35,50`.  The `29` in that first table
is `dim D_5^{det_3}` and is the built-in consistency check the brief names.

Date: 2026-09-01.

---

## 1. The joint, restated exactly

`det(sum_{i=1}^{5} s_i A_i)` is divisible by `s_1` iff
`S_0 := span(A_2,...,A_5)` is a space of **singular** `4x4` matrices, i.e. a
subspace of `M_4(C)` of bounded rank `<= 3`, of dimension `<= 4`.  The
integrator measured four *compression* branches and got `29, 31, 31, 29`
against the `35` that containment needs.

The soft joint as stated in `docs/l5_containment.md` is:

> is every 4-dimensional singular subspace of `M_4(C)` contained in a
> compression space?

A **compression space** here is `{A : A(U) subseteq W}` with `dim W = dim U - 1`;
in a suitable basis it is a mask with a zero block of size `(5-k) x k`,
`k = dim U in {1,2,3,4}` — the four branches measured.

## 2. Hand analysis done before any search (this is the substantive content of
   this pre-registration)

**The answer to the joint as literally stated is NO, and I have an explicit
counterexample.**  Let `N(x)` denote the `3x3` skew-symmetric matrix with
`N(x)y = x times y`, and put

    E_1  =  { [[ N(x), 0 ], [ 0, w ]]  :  x in C^3,  w in C }  subseteq M_4(C).

- `dim E_1 = 4`.
- Every element is singular: the matrix is block diagonal and `det N(x) = 0`
  for every `x` (a `3x3` skew matrix has zero determinant), so
  `det = w . det N(x) = 0` identically.  Bounded rank exactly 3 (generic `x`,
  `w` give `rank N(x) = 2` plus `1`).
- **`E_1` is not contained in any compression space.**  Suppose
  `A(U) subseteq W` with `dim W = dim U - 1` for all `A in E_1`.
  - `k = dim U = 1`: a common kernel vector `u`.  If `u` has a nonzero `4`th
    coordinate, `w u_4 != 0` for `w != 0`; if `u in C^3` then `N(x)u = x times u`
    is nonzero for `x` not parallel to `u`.  No common kernel.
  - `k = 2`: need `A(U)` inside a fixed line.  `U` meets `C^3` in dimension
    `>= 1`; for `0 != u in U cap C^3`, `{ N(x)u : x in C^3 } = u^{perp}` is
    already 2-dimensional.  Impossible.
  - `k = 3`: need `A(U)` inside a fixed plane `W`.  `U` meets `C^3` in
    dimension `>= 2`; for independent `u_1, u_2 in U cap C^3`,
    `u_1^{perp} + u_2^{perp} = C^3 subseteq W`, and `dim W = 2`.  Impossible.
  - `k = 4`: a common cokernel, i.e. all images in a fixed hyperplane.  The
    images of `E_1` span `C^4` (take `w != 0` and three independent `x`).
    Impossible.

  So `E_1` is a genuine **exceptional branch**, and it exists at exactly the
  parameters of the joint.  It is the `3x3` skew example padded by a `1x1`
  block — precisely the thing the brief warns "makes overconfidence here
  embarrassing".  The integrator's own already-ruled-out family (a singular
  4-space *inside* skew `4x4`, killed by the isotropic-dimension bound) is a
  different family and does not cover this one.

- A one-parameter-family generalisation, also singular and also outside every
  compression space by the same `u_1^{perp} + u_2^{perp}` argument:

      E_2(B)  =  { [[ N(x), Bx ], [ 0, w ]] }  ,   B in M_3(C),

  block upper triangular, so `det = w . det N(x) = 0`.  Row operations kill any
  `w`-dependence of the top-right column and column operations move `B` by
  skew matrices, so the parameter is really `B in M_3 / so_3 = Sym^2`.
  `E_2(0) = E_1`.

## 3. Predictions, with falsifiers

**P1 — the verdict.  "Exceptional branch exists", and the literature covers the
classification.**  I predict the classification of spaces of bounded rank `<= 3`
is in the literature (Atkinson's primitive-space classification, and the recent
Huang–Landsberg / de Seguins Pazzis work), that it does contain
non-compression examples at `4x4` of dimension 4, and that `E_1` (equivalently
the "skew `3x3` plus a block" construction) is on the list.  So the brief's
three-way choice resolves as *both* "covered by literature" *and* "exceptional
branch exists" — the joint as stated in `docs/l5_containment.md` is false as
stated, and the conclusion has to be re-derived rather than cited.
*Falsifier F1: a literature theorem saying every 4-dimensional singular
subspace of `M_4(C)` IS contained in a compression space.  That would
contradict §2, so if I meet such a statement I stop and reconcile — either my
counterexample or my reading of the theorem is wrong (brief kill criterion 2).*

**P2 — the effect: rank still `< 35`.  No reversal.**  I predict the
exceptional branch does not reach 35, and specifically that it falls **below**
the compression branches' 31.  Reasoning logged now, before computing.  Write
`G = det M / s_1` and restrict to `s_1 = 0`: on the exceptional branch with
`ell = s_1` and coordinates `(x, w)` on `span(s_2..s_5)`, expanding
`det [[N + s_1 P, s_1 q],[s_1 r^T, w + s_1 t]]` and using
`adj N(x) = x x^T` gives

    G  =  w . (x^T P x)  +  s_1 . (...)  +  s_1^2 . (...)  +  s_1^3 . (...).

So `G mod s_1` is `w` times a **quadratic in `x` alone** — a reducible cubic in
4 variables whose quadratic factor has rank `<= 3`.  Those form a
12-dimensional family inside the 20-dimensional space of cubics in 4 variables
(`4` for the linear factor, `9` for a rank-`<=3` quadric, `-1` for scale).
A cubic `G` in 5 variables decomposes as `20 + 10 + 4 + 1 = 35` by `s_1`-degree,
so the leading part alone costs `20 - 12 = 8`, giving `rank <= 27`.  The `s_1`
part carries a further restriction (no `w^2` term at fixed frame), so I expect
less.  **Point prediction: rank in `[20, 27]`, best guess 26.**
*Falsifier F2: rank `>= 28` on any exceptional branch — the reasoning above is
then wrong.  Falsifier F3 (the kill criterion): rank `= 35` on any branch,
which reverses the headline: the length-5 stratum closes, the nine measured
`D = 0` cells are explained, and s30's sweep becomes confirmation.*

**P3 — re-verification reproduces the integrator exactly.**  My own
implementation, exact over `Q` and by a derivative mechanism that does not use
the cofactor identity, will return `29, 31, 31, 29` and will confirm
`29 = dim D_5^{det_3}` from the independent `wk6_s26_density` route.
*Falsifier F4: any disagreement.  Then the integrator's table is in question and
nothing downstream can be written until it is resolved.*

**P4 — completeness of the branch list.**  I predict that after adding the
exceptional families the maximum over all branches is still `31`, attained by
the two middle compression branches, so the containment failure stands with the
same 4-dimensional shortfall.
*Falsifier F5: a branch strictly between 31 and 35 — the shortfall number in
`docs/l5_containment.md` §4 would need correcting even without a reversal.*

**P5 — bonus (task E).**  For `{ell . c}` with `c` a general `r`-ary cubic:
containment in `D_r^{det_n}` holds for `r <= 4` at `n = 4` (session 27) and I
predict it fails for every `r >= 5` at `n = 4`, and more generally that the
stacking trick survives exactly while every `r`-ary cubic is
`3x3`-determinantal, i.e. `r <= 4`.
*Falsifier F6: a rank-35-analogue at some `(n, r)` I predict fails.*

## 4. Method, fixed in advance

- **Own implementation first** (brief task D), before extending: exact
  arithmetic over `Q` for the ranks, with the determinant differentiated by
  carrying a first-order truncated polynomial in an auxiliary `epsilon` rather
  than by the adjugate/cofactor identity the integrator used, so that the two
  routes share no algebraic identity.  A second run mod a different prime as a
  cross-check.  Divisibility by `s_1` asserted, never assumed.
- **Branches added as masks or as parametrised families**, whichever the
  structure needs; every new branch gets the same `s_1`-divisibility assertion,
  which is itself a proof that the parametrised space really is singular.
- Ranks reported as the maximum over at least three independent random
  parameter points, as the integrator did.
- Exact arithmetic only.  Honest negatives are results.

## 5. What is not touched

`paper/det3-conductor.tex`, `PROJECT_NOTES.md`, `docs/boundary_deficit.html`,
and `analysis/l5contain.py` / `docs/l5_containment.md` (the integrator's files —
I write my own and report differences rather than editing theirs).
