# Draft §4 material, in publication form

Session 28. **Written to be copied, not rewritten** — the brief asks for the
length-`<= 4` theorem in publication form with a complete proof, the sharpness
statement, and one sentence on what `D_5` is. `paper/det3-conductor.tex` is not
touched on this branch; the X_-3 grind owns it.

Notation as in the paper: `W = Sym^3 C^{n^2}`, `G = GL_{n^2}`,
`cO = closure(G . det_n)`, `a(lam,delta)` the multiplicity of `S_lam` in
`C[W]_delta` (a plethysm coefficient of `h_delta[h_3]`), and
`m(lam) = dim (S_lam^*)^{Stab(det_n)}` the Peter–Weyl count.

---

## Proposed text

**Lemma A (isotypic rank).** *Let `X ⊆ W` be a `G`-stable closed cone with dense
orbit `G.x`, let `M_lam` be the `lam`-isotypic component of `C[W]_delta`, and
let `h_1, ..., h_a` be a basis of the highest-weight vectors of weight `lam` in
`C[W]_delta`, where `a = a(lam,delta)`. Then*

        mult_lam C[X]_delta  =  a  −  dim { u : sum_k u_k h_k vanishes on G.x }.

*Proof.* `I(X) ∩ M_lam` is a `G`-submodule of `S_lam ⊗ C^a`, hence of the form
`S_lam ⊗ U`. Under that identification the highest-weight vectors are the
`v ⊗ u` with `v` the highest weight vector of `S_lam`, i.e. exactly the
`sum_k u_k h_k`. Since `v` generates `S_lam` and `I(X)` is `G`-stable and
closed, `v ⊗ u ∈ I(X)` iff `S_lam ⊗ u ⊆ I(X)` iff `sum_k u_k h_k` vanishes on
the dense orbit. ∎

At `a = 1` this is the one-bit argument already used in §4; at `a >= 2` it is a
rank, and it is what makes weights with ambient room computable.

**Lemma B (short weights see few variables).** *Let `h ∈ C[W]_delta` be a weight
vector of weight `lam` with `ell(lam) = r`. Then `h(F)` depends only on the
restriction of `F` to `L = span(e_1, ..., e_r)`; and for `F = g . det_n`,*

        F|_L (s_1, ..., s_r)  =  det( s_1 A_1 + ... + s_r A_r ),   A_i = g^{-1} e_i,

*with `(A_1, ..., A_r)` ranging over a dense subset of `(M_n)^r`.*

*Proof.* `C[W]_delta` is spanned by monomials in the coefficient functionals
`c_alpha`, whose weight is the sum of the participating exponent vectors
`alpha`. Every `alpha` has non-negative entries, so a monomial of weight `lam`
with `lam_j = 0` for `j > r` cannot involve any `c_alpha` with `alpha_j > 0`;
and killing those coordinates is restriction to `L`. The second statement is the
definition of the `G`-action. ∎

**Proposition C.** *For `ell(lam) = r`,*

        mult_lam C[cO]_delta  =  mult_{S_lam(C^r)} C[D_r]_delta ,

*where `D_r ⊆ Sym^n C^r` is the closure of the set of `r`-ary forms of degree
`n` admitting an `n x n` linear determinantal representation. In particular, if
`D_r = Sym^n C^r` then `I(cO)` has no length-`r` part in any degree.*

**Theorem D.** *For `n = 3`, every `delta`, and every `lam` with
`ell(lam) <= 4`,*

        mult_lam C[cO]_delta = a(lam,delta),     def(lam,delta) = m(lam) − a(lam,delta).

*Proof.* By Proposition C it suffices that `D_r = Sym^3 C^r` for `r <= 4`. For
`r = 2` this is elementary: every binary cubic splits as
`prod_{i<=3}(alpha_i s + beta_i t) = det(s D_alpha + t D_beta)` with `D`
diagonal. For `r = 3` and `r = 4` it is classical — every plane cubic and every
smooth cubic surface admits a `3x3` linear determinantal representation
(Dickson; Grassmann), and by Beauville [Determinantal hypersurfaces, Michigan
Math. J. 48 (2000)] the generic hypersurface of degree `d` in `P^m` is
determinantal precisely when `m = 2`, or `m = 3` and `d <= 3`. ∎

**Theorem E (sharpness).** *The hypothesis `ell(lam) <= 4` cannot be weakened:
`I(cO)` contains highest-weight vectors of length 5.*

*Proof.* The rank-`<=1` locus of `M_3` is the cone over the Segre
`P^2 x P^2 ⊂ P^8`, of dimension 4. For `r = 5` the pencil `s -> sum s_i A_i`
spans a linear `P^4 ⊂ P^8`, and `4 + 4 >= 8`, so the two meet. At a point where
`rank M(s) <= 1` all `2x2` minors vanish, hence all cofactors, hence all
partials `dF/ds_k = tr(adj M(s) . A_k)`: every member of `D_5` is a singular
quinary cubic. Therefore the discriminant of quinary cubics — irreducible of
degree `5 · 2^4 = 80`, a `GL_5` semi-invariant, of weight `(48^5)` — lies in
`I(D_5)`, and by Proposition C the corresponding highest-weight vector of length
5 lies in `I(cO)`. ∎

**Remark F.** *The same count is why `r = 4` behaves differently: a generic
`P^3 ⊂ P^8` misses a codimension-4 subvariety, which is exactly why smooth
determinantal cubic surfaces exist and smooth determinantal cubic threefolds do
not. The length at which Theorem D fails is therefore governed by
`dim Stab(det_n)`: `dim D_r <= min( C(r+n-1,n), n^2 r − dim Stab )` for
`r >= 3` (the hypothesis is needed — at `r = 2` the stabiliser of a generic
pair is positive-dimensional), and the crossover is where the two arguments of
the minimum change places. For `det_3` that is between `r = 4` and `r = 5`; for
`per_3`, whose stabiliser has dimension 4 rather than 16, it is between `r = 5`
and `r = 6`; for `det_4` it is between `r = 3` and `r = 4`.*

**One sentence on `D_5`, for wherever it is first mentioned.** *`D_5` is the
variety of quinary cubics admitting a `3x3` linear determinantal representation
— equivalently the restriction of `cO` to a 5-plane — of dimension `45 − 16 =
29` and codimension 6 in `Sym^3 C^5`; its generic member is a cubic threefold
with six nodes, at the six points where the pencil meets the rank-one locus.*

---

## Notes for the integrator

- Theorem D is what converts the paper's entire short-weight deficit dataset
  into `m − a`, a difference of a symmetric rectangular Kronecker coefficient
  and a plethysm coefficient. It is the piece worth the most space.
- Theorem E makes D sharp. It is short, elementary and self-contained; it needs
  no computation, and it supersedes session 26's honest boundary item "what is
  not proved is that the ideal actually does bite at length 5".
- **What is still open, and should be stated as open if D and E are used:** the
  smallest degree at which a length-5 weight has `mult < a` is not known. The
  bracket established here is `6 <= delta_0 <= 80` unconditionally and
  `8 <= delta_0 <= 80` given the published deficit sequence; 80 comes from one
  explicit equation and is surely far from tight. See `docs/d5_ideal.md` §5.
- `dim Stab(det_3) = 16`, not 17 — the vector stabiliser, which is what
  Peter–Weyl and Lemma A require. Sessions 24b and 26 both flagged this; the
  session-28 Jacobian deficiencies `45 − 29 = 16` and `54 − 38 = 16` measure it
  a third way.
