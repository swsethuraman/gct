# B18-01 — Making the five-variable separation effective

**Status: COMPLETE. Deliverable 1 (a proved finite degree bound) and deliverable 4
(the precisely stated missing theorem) are both supplied. Deliverables 2 and 3 are
NOT REACHED and I explain why, in a way that is meant to be checkable rather than
suggestive.**

## Plain terms, before any formulas

Batch 17 proved a real fact: five-variable padding is *not* inside the determinant
pencil closure, so somewhere there is a determinant equation with exactly five rows
that does not vanish on padding. But B17 gave no degree. The question put to this
slot is whether "somewhere" can be turned into "at or below degree `d`".

Three things came out.

**(1) Yes, there is a finite bound, and it does not come from the ruledness proof.**
The ruledness argument is used only as a black box that names one point outside a
closed set. Once you have *any* point outside a closed projective variety `Y`, a
completely classical projection argument produces a hypersurface of degree at most
`deg Y` through `Y` missing that point, and a refined-Bézout argument bounds `deg Y`
for a variety parametrised by forms of degree 4. Assembling these gives a separating
equation of degree at most `4^49`, in a partition with exactly five rows. That is a
real, derived, finite bound. It is also about `10^29`, so it is useless as a search
target, and I say so plainly. The honest content of the result is: *the effectivity
obstruction is not the ruledness proof; it is the degree of the determinant pencil
variety, and nobody knows that degree.*

**(2) Making ruledness itself effective is the wrong target.** Non-membership
of `lC` in the pencil closure is proved by a chain — Matsusaka specialization,
then Clemens–Griffiths irrationality — in which no step carries a coefficient
degree. There is no "quantified step" waiting to be filled in. Any effective bound
must come from elimination theory on the determinant side, not from the geometry of
cubic threefolds. This retires an intuition that the board's phrasing ("an effective
version would bound the degree at which the non-containment is witnessed by
coefficients") could be read as endorsing.

**(3) A warning the board should act on.** The five-row regime is governed entirely
by two explicit cones in the 70-dimensional space of five-variable quartics: the
determinant pencil closure, of dimension 50, and the padding restriction, of
dimension 39. The *padding* side is the smaller one. The configuration that yields a
positive multiplicity gap `D = i_det - i_pad > 0` is the determinant side being the
more special one. So the length-five cells, where separation first appears, are
structurally the wrong place to look for `D > 0` — and I give the precise sense in
which that is a theorem (an aggregate Hilbert-function inequality) and the precise
sense in which it is only a heuristic (individual cells are not controlled).

What I therefore hand on is: a proved effective degree bound; a proof that the
effectivity bottleneck is exactly one classical unknown quantity (`deg` of the
determinant pencil variety); and a formal statement of the missing theorem for a
positive gap, with the triage the assignment asked for.

## Conventions used here

ADOPTED from the preamble and from B17-03, without alteration:
forms in `Sym^4(V*)`; coefficient ring `Sym(Sym^4 V)`; ordinary coefficients
`c_alpha = [x^alpha] F`; weights `wt(c_alpha) = alpha`, all entries nonnegative;
raising `E_ij c_alpha = (alpha_i + 1) c_(alpha + e_i - e_j)` when `alpha_j > 0` and
`0` otherwise. No factorial-normalised symbol is used anywhere in this report.
`a`, `i_det`, `i_pad`, `m_det`, `m_pad`, `D = m_pad - m_det = i_det - i_pad` are as
in the preamble. `H^N_{d,lambda}` is the highest-weight space in `(A_N)_d`;
`K_X = I(X)_d ∩ H^N_{d,lambda}`; `i_X = dim K_X`; `m_X = a - i_X`.

Five-variable objects, following B17-01:

- `V5 = C^5`, `W5 = Sym^4(V5*)`, `dim W5 = 70`.
- `D45 = closure{ det(x_0 B_0 + ... + x_4 B_4) : B_k in Mat_4(C) }` — the
  **coefficient closure** of the five-variable determinant pencil family.
- `R135 = { l·C : l in V5*, C in Sym^3 V5* }` — the product locus, which B17-01
  proves (via dominance of the permanent restriction) equals `D_pad,5`, the closure
  of the actual five-variable restrictions of `GL16 · (z per_3)`.
- `F* = x_0 · per_3(sum x_k A_k)` is B17-01's certified actual padding point with
  smooth cubic factor; `F* in R135 \ D45`.

## 1. Closure audit: which closure, which topology, and whether it matters

The assignment flags this first, because the two topologies "differ in consequence".
Here they do not, and the reason is worth recording so that no later slot has to
re-litigate it.

**Claim 1.1 (PROVED, standard).** Let `S ⊆ C^N` be a constructible set. Then the
Zariski closure and the Euclidean closure of `S` coincide.

*Justification.* A constructible `S` contains a Zariski-dense Zariski-open subset `U`
of its Zariski closure `Z = closure_Zar(S)`; `Z \ U` is a proper closed subset of
`Z`. Every point of an irreducible complex variety lies in the Euclidean closure of
any nonempty Zariski-open subset (Mumford, *Red Book*, I.10, Corollary 1). Hence
`Z ⊆ closure_Eucl(U) ⊆ closure_Eucl(S) ⊆ closure_Zar(S) = Z`. ∎

**Claim 1.2 (PROVED).** `D45` is the Zariski closure of the image of the polynomial
map `phi : (Mat_4)^5 → W5`, `phi(B) = det(sum_k x_k B_k)`, and by Chevalley that
image is constructible; so `D45` is simultaneously the Zariski and the Euclidean
closure of the set of *honest* five-variable `4x4` linear determinants. The same
applies to `R135`, which is in fact already Zariski **closed**: it is the affine cone
over the image of the projective morphism
`P(V5*) x P(Sym^3 V5*) → P(W5)`, and images of projective varieties under morphisms
are closed. B17-01 uses exactly this.

**Consequence 1.3.** The phrase "dense among five-variable cubics" in the B17
statement is unambiguous: the permanent restriction map `Phi` is *dominant*, its
image is constructible, hence it contains a Zariski-dense Zariski-open subset of
`Sym^3 V5*` and is also Euclidean-dense. So `D_pad,5 = R135` holds in either
topology, and the non-containment `R135 ⊄ D45` is a statement about two honest
Zariski-closed cones in `C^70`. No coefficient-level consequence is lost or gained
by the choice of topology.

**Why the distinction could have mattered, and why it does not.** A "closure" that
was merely Euclidean, or a limit set that was not constructible, would have no
associated homogeneous vanishing ideal and no degree filtration, and then *no*
degree bound could be extracted even in principle. That failure mode is excluded by
1.1–1.2. What is *not* excluded, and is the real obstruction, is quantitative: an
ideal-theoretic non-containment of two closed cones carries no a-priori degree
information. Section 3 supplies that information from elsewhere.

**Claim 1.4 (ADOPTED from B17-03, Lemmas 1 and 2; re-checked).** For
`ell(lambda) ≤ r` the restriction `rho_r : W_16 → W_r` induces isomorphisms
`H^r_{d,lambda} ≅ H^16_{d,lambda}` carrying `K_{X_r}` to `K_X`, and
`closure(rho_r(closure(GL16·f))) = closure{f ∘ T : T in Hom(C^r, C^16)}`.
I re-derived both: the first from nonnegativity of coefficient weights plus the
vanishing case of the raising rule, the second from density of full-rank frames and
polynomiality of `q ∘ Phi_{f,r}` in the frame entries. I use them exactly as stated,
with `r = 5`.

## 2. What the B17 non-containment does and does not say, at cell level

**Claim 2.1 (PROVED, from accepted B17 inputs).** There exists a degree `d ≥ 1` with
`I(D45)_d ⊄ I(R135)_d`.

*Proof.* `F* in R135 \ D45` and `D45` is Zariski closed, so some homogeneous
`h` in `I(D45)` has `h(F*) ≠ 0`; take `d = deg h`. ∎

**Claim 2.2 (PROVED).** For any such `d`, there is a partition `lambda ⊢ 4d` with
`ell(lambda) = 5` and `K_det(d,lambda) ⊄ K_pad(d,lambda)` inside the common
highest-weight space `H^16_{d,lambda}`.

*Proof.* `A_5 = Sym(Sym^4 V5)` is a `GL5`-algebra and `I(D45)_d`, `I(R135)_d` are
`GL5`-submodules of `(A_5)_d`. A containment of submodules holds iff it holds on
every isotypic component, and on an isotypic component iff it holds on the
highest-weight subspace (complete reducibility, characteristic zero). So some
`lambda` with `ell(lambda) ≤ 5` and `lambda ⊢ 4d` has
`I(D45)_d ∩ H^5_{d,lambda} ⊄ I(R135)_d ∩ H^5_{d,lambda}`. Claim 1.4 transports both
sides isomorphically into `H^16_{d,lambda}`, where they become `K_det` and `K_pad`
(using `closure(rho_5 X_det) = D45` and `closure(rho_5 X_pad) = R135`, which is
B17-03 Lemma 2 plus B17-01's density theorem). `ell(lambda) ≤ 4` is impossible: that
is exactly B17-03's main theorem `K_det ⊆ K_pad`. Hence `ell(lambda) = 5`. ∎

**Claim 2.3 (the negative half; PROVED).** Claim 2.2 gives, in that cell,
`i_det ≥ 1` and `i_pad < dim(K_det + K_pad) ≤ a`, hence `m_pad ≥ 1`. It gives
**no** inequality between `i_det` and `i_pad`, hence none between `m_det` and
`m_pad`, hence no sign for `D`.

*Why.* `K_det ⊄ K_pad` is a statement about two subspaces of one vector space.
Two distinct lines in a 2-dimensional `H` already realise
`K_det ⊄ K_pad` with `i_det = i_pad`; a line and a plane realise it with
`i_det < i_pad`. This is exactly the preamble's rule and the reviewer's rejected
promotion. **So B17-01+03 prove geometric separation in a five-row cell and nothing
about the multiplicity gap.** Everything below respects that.

**Claim 2.4 (the one implication that *would* close it; PROVED, conditional form).**
Fix a cell `(d,lambda)` in which `K_det ⊄ K_pad`. If in addition
`K_pad ⊆ K_det` in that cell, then `K_pad ⊊ K_det`, so `i_det > i_pad`, so
`D = i_det - i_pad ≥ 1 > 0`.

*Proof.* Immediate: proper containment of finite-dimensional subspaces is strict
inequality of dimensions. ∎

Claim 2.4 is the shape of the missing theorem; Section 6 states it formally and says
what it would take. The special case `i_pad = 0` (equivalently `m_pad = a`: the whole
ambient highest-weight space restricts faithfully to padding) makes the hypothesis
of 2.4 automatic, so *the single cleanest sufficient statement is: a five-row cell
with an actual determinant equation and with no padding equation at all.*

## 3. The effective degree bound

The whole of this section is elementary projective geometry plus one standard
citation. Nothing in it uses ruledness, cubic threefolds, or permanents; the B17
input enters only as "there is a point of `R135` outside `D45`".

### 3.1 Lemma A — separating a point from a variety in degree at most its degree

**Lemma A (PROVED).** Let `Y ⊆ P^m` be a Zariski-closed subset (reduced, possibly
reducible, of pure or mixed dimension) and let `p in P^m \ Y`. Then there is a
homogeneous form `f` of degree `deg f ≤ deg Y` with `f|_Y = 0` and `f(p) ≠ 0`.
Here `deg Y = sum_i deg Y_i` over the irreducible components.

*Proof.* First suppose `Y` irreducible, `dim Y = k`, `deg Y = delta`. Since
`p ∉ Y`, projection from `p`, `pi_p : P^m \ {p} → P^{m-1}`, is a morphism on `Y`;
put `Y' = pi_p(Y)`, closed of dimension at most `k`. A general linear subspace
`Lambda' ⊆ P^{m-1}` of dimension `m - k - 2` is disjoint from `Y'`, because
`(m-k-2) + k = m - 2 < m - 1`. Let `Lambda ⊆ P^m` be the cone over `Lambda'` with
vertex `p`: a linear subspace of dimension `m-k-1` containing `p`, with
`Lambda ∩ Y = ∅` (a point of `Lambda ∩ Y` other than `p` would map into
`Lambda' ∩ Y'`, and `p ∉ Y`). Choose a hyperplane `L ⊂ Lambda` with `p ∉ L`; then
`dim L = m-k-2` and `L ∩ Y = ∅`.

Projection from `L`, `pi_L : P^m \ L → P^{k+1}`, is therefore a *finite* morphism on
`Y`, so `Z = pi_L(Y)` is closed of dimension `k`, i.e. a hypersurface in `P^{k+1}`,
and `deg Z · deg(Y → Z) = delta`, so `deg Z ≤ delta`. Let `g` be the defining form
of `Z`, `deg g = deg Z`. Because `pi_L` is a linear projection, `f := pi_L^* g` is a
form of the same degree in the coordinates of `P^m`, and `f|_Y = 0`. Finally
`f(p) ≠ 0`: otherwise `pi_L(p) in Z = pi_L(Y)`, i.e. the span `<L, p> = Lambda` would
meet `Y`, contradicting `Lambda ∩ Y = ∅`.

For reducible `Y = union_i Y_i`, apply the above to each component to get `f_i` with
`deg f_i ≤ deg Y_i`, `f_i|_{Y_i} = 0`, `f_i(p) ≠ 0`, and take `f = prod_i f_i`. ∎

(This is the classical statement that a projective variety is cut out
set-theoretically in degrees at most its degree. I give the proof in full because
the bound, not the existence, is the whole point here.)

### 3.2 Lemma B — degree of the image of a rational map given by degree-`D` forms

**Lemma B (PROVED, using refined Bézout).** Let `psi : P^n ⇢ P^M` be given by forms
`f_0, ..., f_M` of common degree `D`, not all zero, with base locus `Z = V(f_0,...,f_M)`.
Let `Y = closure(psi(P^n \ Z))` and `k = dim Y`. Then `deg Y ≤ D^k`.

*Proof.* Let `H_1, ..., H_k ⊆ P^M` be general hyperplanes. Then
`Y ∩ H_1 ∩ ... ∩ H_k` is a reduced set of `delta = deg Y` points `y_1, ..., y_delta`,
each a general point of `Y`; in particular (a general zero-dimensional linear
section avoids any fixed proper closed subset of `Y`) each `y_j` lies in the actual
image `psi(P^n \ Z)`, and each fibre `psi^{-1}(y_j)` has dimension exactly `n - k`
by the fibre-dimension theorem applied to `psi` on `P^n \ Z`.

Put `G_i = psi^{-1}(H_i) = V(sum_j a_{ij} f_j)`, a hypersurface of degree `D` in
`P^n`, and `G = G_1 ∩ ... ∩ G_k`. For each `j` choose an irreducible component `W_j`
of `closure(psi^{-1}(y_j))` of dimension `n - k`. I claim each `W_j` is an
irreducible component of `G`. Let `W ⊇ W_j` be the component of `G` containing it.
`W_j ⊄ Z` (it contains points of the fibre, which are outside `Z`), so `W ⊄ Z`, so
`W \ Z` is dense open in `W` and irreducible; `psi(W \ Z) ⊆ Y ∩ H_1 ∩ ... ∩ H_k`,
a finite set, so `psi(W \ Z)` is a single point, necessarily `y_j` because
`W_j \ Z ≠ ∅` maps to `y_j`. Hence `W ⊆ closure(psi^{-1}(y_j))`, so
`dim W ≤ n-k = dim W_j`, so `W = W_j`. Distinct `j` give distinct `W_j` (different
images). Therefore

    delta = #{j} ≤ sum_j deg W_j ≤ sum over all irreducible components of G of deg,

and the refined Bézout theorem for an intersection of `k` hypersurfaces of degree
`D` bounds the latter sum by `D^k`. ∎

*Citation for the last step (ADOPTED).* Fulton, *Intersection Theory*, 2nd ed.,
Example 12.3.1 (refined Bézout): if `V_1, ..., V_r ⊆ P^n` are hypersurfaces of
degrees `d_1, ..., d_r`, the sum of the degrees of the irreducible components of
`V_1 ∩ ... ∩ V_r` is at most `prod_i d_i`. (Equivalently Fulton Prop. 8.4 /
Ex. 8.4.6; see also Vogel, *Results on Bézout's theorem*, for the same inequality.)
I did not re-prove this; it is a standard theorem and is the only non-elementary
ingredient of Section 3. **HYPOTHESIS FLAG:** the inequality is for the *sum over
irreducible components*, which is what I use; the stronger "with multiplicities"
statement is not needed.

### 3.3 Lemma C — the dimension of the determinant pencil variety is at most 49

**Lemma C (PROVED).** `dim D45 ≤ 50` as an affine cone in `C^70`; equivalently
`dim P(D45) ≤ 49`.

*Proof.* Let `G = { (P,Q) in GL_4 x GL_4 : det P · det Q = 1 }`, `dim G = 31`, acting
on `(Mat_4)^5` by `(P,Q)·(B_k) = (P B_k Q)`. Since
`det(sum x_k P B_k Q) = det P det Q det(sum x_k B_k) = det(sum x_k B_k)`, every
`G`-orbit lies in a fibre of `phi`. Compute the stabiliser at a generic point. The
locus where `B_0` is invertible is dense open; there, `P B_0 Q = B_0` forces
`Q = B_0^{-1} P^{-1} B_0`, and conjugating we may assume `B_0 = I`, so `Q = P^{-1}`
and `P B_k P^{-1} = B_k` for `k = 1,...,4`. For `B_1` regular semisimple (a dense
open condition) the centraliser of `B_1` is the 4-dimensional diagonal torus in the
eigenbasis of `B_1`; writing `P = diag(p_1,...,p_4)` there,
`(P B_2 P^{-1})_{st} = p_s p_t^{-1} (B_2)_{st}`, and for `B_2` with all entries
nonzero in that basis (again dense open) this forces all `p_s` equal, i.e. `P = cI`,
`Q = c^{-1} I`. So `Stab_G(B) ≅ C^*` has dimension 1 at every point of a dense open
subset, the orbit has dimension `31 - 1 = 30`, and every fibre of `phi` through such
a point has dimension at least 30. Hence
`dim closure(im phi) ≤ 80 - 30 = 50`. ∎

### 3.4 The theorem

**Theorem E (PROVED, modulo the ADOPTED refined-Bézout citation).**
Put `k = dim P(D45) ≤ 49`. There exist an integer `d` with

    d ≤ deg P(D45) ≤ 4^k ≤ 4^49 = 316 912 650 057 057 350 374 175 801 344

and a partition `lambda ⊢ 4d` with `ell(lambda) = 5`, such that
`K_det(d,lambda) ⊄ K_pad(d,lambda)`. Equivalently: there is a highest-weight
determinant equation of type `S_lambda(C^16)` with exactly five rows, of degree
`d ≤ 4^49`, which does not vanish identically on `X_pad`.

*Proof.* `psi : P^79 ⇢ P^69` given by the 70 coefficients of
`det(sum_k x_k B_k)`, each a form of degree `D = 4` in the 80 matrix entries, has
`closure(im psi) = P(D45)`. Lemma C gives `k ≤ 49`; Lemma B with `D = 4` gives
`deg P(D45) ≤ 4^k`; Lemma A applied to `Y = P(D45)` and `p = [F*] ∉ P(D45)` (B17-01)
gives a form `bar h` of degree `d ≤ deg P(D45)` with `bar h|_{D45} = 0`,
`bar h(F*) ≠ 0`. Then `h = rho_5^* bar h` lies in `I(X_det)_d` (Claim 1.4) and
`h(F*') ≠ 0` for the ambient padding point `F*'` whose five-variable restriction is
`F*` (B17-01 supplies the invertible ambient frame). So `I(D45)_d ⊄ I(R135)_d`, and
Claim 2.2 yields `lambda` with `ell(lambda) = 5`. Finally `4^k ≤ 4^49` since `k ≤ 49`.
∎

### 3.5 Honest assessment of Theorem E

- It is a **derivation**, not a dimension heuristic: Lemma C is a stabiliser
  computation (used only to bound an exponent), Lemma B is refined Bézout, Lemma A
  is a linear projection. At no point is "dim source vs dim target" used to conclude
  anything.
- It is **astronomically weak**: `4^49 ≈ 3.2 x 10^29`. For comparison the largest
  degree any cell in this programme has touched is 27. No search is implied.
- It is **uniform**: the same bound separates *every* point outside `P(D45)`, so it
  is really a statement that `P(D45)` is set-theoretically cut out in degrees
  `≤ deg P(D45)`. It uses nothing specific about `F*`. That is simultaneously its
  robustness and its weakness.
- The **only** quantity standing between this and a usable bound is `deg P(D45)`,
  the degree of the variety of five-variable `4x4` linear determinantal quartics.
  This is a classical, apparently unknown, number. Section 6 makes that the formal
  content of "what is missing for option 1".

## 4. One bounded pilot: the exact dimension of `D45`, and why it was needed

Lemma C gives `dim D45 ≤ 50`. Section 5 needs the *strict* inequality
`dim D45 > dim R135 = 39`, and Theorem E's exponent is `dim P(D45)`, so an exact
value both sharpens (or confirms) the bound and licenses the structural conclusion.
An exact lower bound follows from the rank of the differential at a single point, so
this is a 70-column linear-algebra check, not a search. That is why the pilot was
run; nothing else in this report required computation.

**Setup.** `d phi_B` sends `E = (E_0,...,E_4)` to `sum_k x_k · tr(adj(M(x)) E_k)`,
where `M(x) = sum_k x_k B_k`, so the `(k,i,j)` row of the Jacobian in the monomial
basis is `[x^alpha]( x_k · adj(M)_{ji} ) = [x^alpha]( x_k · cofactor_{ij}(M) )`.
The Jacobian is `80 x 70`. In characteristic zero
`dim closure(im phi) = max_B rank d phi_B ≥ rank d phi_B` for any single `B`, and
`rank mod p ≤ rank over Q`, so a full modular rank at one integer point is a valid
**lower** bound (this respects the preamble's direction-of-inference rule: a
deficient modular rank would have proved nothing here, a full one proves the bound).

**Point used (fixed, reproducible):**

```
B0 = [[1,0,2,-1],[3,1,0,4],[-2,5,1,0],[0,-3,2,1]]
B1 = [[2,-1,1,0],[0,3,-2,1],[1,0,4,-3],[5,2,0,1]]
B2 = [[-1,4,0,2],[1,-2,3,0],[0,1,-1,5],[2,0,1,-4]]
B3 = [[3,1,-2,0],[-1,0,1,2],[4,-3,0,1],[0,2,5,-1]]
B4 = [[0,2,1,3],[2,-1,0,1],[-3,1,2,0],[1,4,-2,0]]
```

**MEASURED.** `rank_{F_p}(d phi_B) = 50` at `p = 2147483647`.
Controls run in the same bounded process and all passed:
`M · adj(M) = det(M) · I` as polynomial identities in all 16 entries;
the Euler identity `sum_{k,i,j} (B_k)_{ij} · x_k · cofactor_{ij}(M) = 4 det M`
(this checks every Jacobian entry simultaneously against `det M`); `det M` has all
70 monomials present; and a deliberately sign-flipped cofactor makes the first
control fail, as it must.

**Claim 4.1 (PROVED).** `dim D45 = 50` and `dim P(D45) = 49`.
*Proof.* `≥` from the pilot (`50 ≤ rank over Q ≤ dim`), `≤` from Lemma C. ∎

So Theorem E's exponent is exactly 49 and cannot be improved by improving Lemma C:
**`deg P(D45) ≤ 4^49` and `d ≤ 4^49`, with `49` the true dimension.**

**Claim 4.2 (PROVED).** `dim R135 = 39`.
*Proof.* `mu : V5* x Sym^3 V5* → W5`, `(l,C) ↦ lC`, has image `R135` (closed, 1.2).
For `l ≠ 0` and `C` irreducible and not a multiple of `l`, unique factorisation in
`Sym(V5*)` makes `mu^{-1}(lC) = {(tl, t^{-1}C) : t ≠ 0}`, of dimension 1. Such pairs
are dense. Hence `dim R135 = 5 + 35 - 1 = 39`. ∎

**Resource receipt.** Two invocations of `python3`, one process each, no BLAS, pure
integer arithmetic modulo one prime, run under `timeout 60` and
`ulimit -v 524288`. Both returned in well under a second. Scripts:
`out/b18_01_pilot.py` (rank) and `out/b18_01_control.py` (controls), delivered
alongside this report. Reproduction is the same two bounded commands:
`(ulimit -v 524288; timeout 60 python3 b18_01_pilot.py)` and likewise for the
control. No lease was requested or used; no background process remains.

## 5. A structural obstruction the board should weigh: five rows is the wrong regime for `D > 0`

By Claim 1.4 the whole `ell(lambda) ≤ 5` regime is *identical* to the `GL5` problem
for two explicit cones in `C^70`:

    D45   (determinant side)   dim 50   [Claim 4.1, PROVED]
    R135  (padding side)       dim 39   [Claim 4.2, PROVED]

`D = i_det - i_pad > 0` asks the determinant side to have **more** equations of shape
`lambda` than the padding side. Dimension-wise that is the wrong way round, and this
can be turned into a theorem about the aggregate.

**Claim 5.1 (PROVED).** There is `d_0` such that for every `d ≥ d_0`,

    sum over lambda ⊢ 4d with ell(lambda) = 5 of  dim S_lambda(C^5) · D(d,lambda)  <  0.

*Proof.* For a closed cone `X ⊆ C^70` with `I(X)` homogeneous and `GL5`-stable,
`dim I(X)_d = sum_{lambda ⊢ 4d, ell ≤ 5} i_X(d,lambda) · dim S_lambda(C^5)`,
and `dim I(X)_d = binom(69+d, 69) - h_X(d)` with `h_X` the Hilbert function of
`C[c]/I(X)`. Hence

    S(d) := sum_{ell ≤ 5} dim S_lambda(C^5) · D(d,lambda)
          = dim I(D45)_d - dim I(R135)_d
          = h_{R135}(d) - h_{D45}(d).

For `d` large, `h_{D45}(d)` is the Hilbert polynomial of the reduced 49-dimensional
`P(D45)`, of degree 49 in `d` with positive leading coefficient, while
`h_{R135}(d)` has degree 38. So `S(d) ~ -(deg P(D45)/49!)·d^49 < 0` for large `d`.

Split `S(d) = S_{≤4}(d) + S_5(d)`. Bound `|S_{≤4}(d)|`: since
`|D(d,lambda)| = i_pad - i_det ≤ a(d,lambda)` for `ell ≤ 4` (B17-03 gives
`i_det ≤ i_pad ≤ a` there),

    |S_{≤4}(d)| ≤ sum_{ell ≤ 4} a(d,lambda) · dim S_lambda(C^5).

By Claim 1.4, `a(d,lambda)` for `ell(lambda) ≤ 4` is also the multiplicity of
`S_lambda(C^4)` in `Sym^d(Sym^4 C^4)`, so
`sum_{ell ≤ 4} a(d,lambda) · dim S_lambda(C^4) = binom(34+d, 34)`. Weyl's formula
gives, for `lambda ⊢ 4d` with `lambda_5 = 0`,

    dim S_lambda(C^5) / dim S_lambda(C^4) = prod_{i=1..4} (lambda_i + 5 - i)/(5 - i)
                                          ≤ (4d+4)^4 / 24.

Hence `|S_{≤4}(d)| ≤ ((4d+4)^4/24) · binom(34+d,34) = O(d^38)`. Since
`S(d) ~ -c·d^49` with `c > 0`, `S_5(d) = S(d) - S_{≤4}(d) < 0` for `d` large. ∎

**Reading of Claim 5.1 (and its limits).**

- It is an **aggregate** statement. It does **not** say every five-row cell has
  `D ≤ 0`; individual cells with `D > 0` are not excluded by it, and Theorem E shows
  five-row cells are certainly special (some of them carry a determinant equation
  that padding does not satisfy).
- It does say that, weighted by `dim S_lambda(C^5)`, the five-row cells are on
  balance *negative* in every sufficiently large degree, and increasingly so
  (`~ d^49` against a `O(d^38)` correction). Any positive five-row cell is a local
  exception inside a strongly negative aggregate.
- `d_0` is **not effective** here, because the leading constant is
  `deg P(D45)`, the same unknown that blocks Theorem E.
- The logic is a Hilbert-function identity plus Weyl's formula, not a comparison of
  `dim source` with `dim target`. I flag this explicitly because the shape of the
  conclusion ("50 beats 39") could be mistaken for the forbidden heuristic. The
  heuristic version — "the bigger variety has fewer equations, so `D < 0`" — is
  *false as stated cell by cell*; Claim 5.1 is the only form of it I am asserting.

**Consequence for the board.** The five-row regime delivers *separation*
(Theorem E) but is aggregate-hostile to a *gap*. B17-03 already proves `D ≤ 0` for
`ell ≤ 4`. So within `ell(lambda) ≤ 5` the programme now has: `≤ 4` proved
non-positive; `= 5` proved separating and proved aggregate-negative. That pushes any
serious `D > 0` hunt into `6 ≤ ell(lambda) ≤ 10`, where the padding restriction
`R_{1,3,r}` is no longer the object (it is the honest `r`-variable image of
`z·per_3`, whose restricted dimension can approach that of the determinant side).

## 6. Deliverables 2 and 3: why they are NOT REACHED, and what is actually available

### 6.1 Option 2 (an explicit five-row separating equation) — NOT REACHED

An explicit equation would have to vanish on **all** of `D45`, i.e. be an actual
element of `I(D45)`. Writing one down is the classical problem of finding equations
for the variety of `4x4` linear determinantal quartic threefolds in `P^4`, which is
codimension `70 - 50 = 20` and, as far as I could establish, has no known explicit
equations. Two specific routes were examined and both fail for stated reasons:

- **B15's Hessian-divisibility mechanism does not transfer.** It works in 16
  variables because `det_4` has Hessian rank at most 8 *on its own hypersurface*, a
  structural degeneracy that yields divisibility identities valid on the entire
  closure. The five-variable restriction has no such degeneracy: the Hessian of
  `det(sum x_k B_k)` is a `5x5` matrix and there is no forced rank drop (the pilot's
  `det M` already has all 70 monomials). Producing a five-variable analogue is
  equivalent to producing equations of `D45`, i.e. to the open problem itself.
  **NOT REACHED**, with the mechanism identified rather than merely not found.
- **Matrix-factorisation elimination.** `F in D45` (for reduced `F`) iff there are a
  linear `M` and a cubic `N`, both `4x4`, with `MN = F·I_4`. For fixed `M` this is
  linear in `(N, F)`, so `I(D45)` is the elimination of `M` from a determinantal
  condition on a linear map depending on `M`. This is a correct reformulation and it
  is where any explicit construction would have to start; I did not carry it out and
  I am not pricing it, because the elimination is over 80 variables.

An honest caution the reviewer should hold me to: Theorem E proves such an equation
exists in degree `≤ 4^49`; it gives **no** construction, and no degree at which a
search is warranted.

### 6.2 Option 3 (one named carrier family `S_lambda`, `ell(lambda) = 5`) — NOT REACHED

I can name the *constraints* a carrier must satisfy, but not a family. Two exact
ceilings are available and both are already in the programme; I re-derive them from
the five-variable picture because in that picture they are closure statements with
no orbit-versus-closure caveat.

**Claim 6.1 (PROVED; = B17-02's `s`, re-derived).** For every `d` and every
`lambda ⊢ 4d` with `ell(lambda) ≤ 5`,

    m_det(d,lambda)  ≤  g( (d,d,d,d), (d,d,d,d), lambda ),

the Kronecker coefficient with two `4 x d` rectangles.

*Proof.* `phi^*(c_alpha) = [x^alpha] det(sum x_k B_k)` is invariant under
`B_k ↦ P B_k Q` with `det P = det Q = 1`, so `phi^*` maps `(A_5)_d` into
`C[C^4 ⊗ C^4 ⊗ C^5]_{4d}^{SL_4 x SL_4}` and its image is `C[D45]_d`. Cauchy/Kronecker
gives `Sym^{4d}(C^4 ⊗ C^4 ⊗ C^5) = ⊕ g(mu,nu,lambda) S_mu(C^4) ⊗ S_nu(C^4) ⊗ S_lambda(C^5)`,
and `S_mu(C^4)^{SL_4} ≠ 0` iff `mu` is the rectangle `(d^4)`, when it is one
dimensional. So the `S_lambda(C^5)`-multiplicity of the invariant ring in degree `4d`
is `g((d^4),(d^4),lambda)`; `C[D45]_d` is a `GL5`-submodule of it, and `m_det` is its
`S_lambda`-multiplicity, using Claim 1.4 to identify `m_det^{16} = m_det^{5}`. ∎
(Transposition `B_k ↦ B_k^T` also preserves `phi^*`, so the bound may be refined to
the `Z_2`-symmetric part — which is exactly the "symmetric rectangular Kronecker,
including transpose" of B17-02. I claim no improvement on that.)

**Claim 6.2 (PROVED; = B17-08's product ceiling, in explicit Pieri form).** For every
`d` and every `lambda ⊢ 4d` with `ell(lambda) ≤ 5`,

    m_pad(d,lambda) ≤ U(d,lambda) := sum over nu with lambda/nu a horizontal d-strip
                                     of  mult( S_nu(C^5) , Sym^d( Sym^3 C^5 ) ).

*Proof.* `mu^*: (A_5)_d → C[b]_d ⊗ C[a]_d = Sym^d(C^5) ⊗ Sym^d(Sym^3 C^5)` is the
`GL5`-equivariant pullback along `(l,C) ↦ lC`, with image `C[R135]_d`; so `m_pad` is
at most the `S_lambda`-multiplicity of the target, which by Pieri (the first factor
is the one-row `S_{(d)}`) is the displayed sum. ∎

**Claim 6.3 (necessary condition for the programme's standard certificate; PROVED).**
Let `B(d,lambda)` be any certified global upper bound for `m_det` in a cell — for
instance Claim 6.1's `g((d^4),(d^4),lambda)`, or its `Z_2`-symmetric refinement. The
programme's certificate ("an actual padding lower bound `r > B`") can exist in a cell
`(d,lambda)` only if `U(d,lambda) > B(d,lambda)`.
*Proof.* Any actual padding rank satisfies `r ≤ m_pad ≤ U` by Claim 6.2. So `r > B`
forces `U > B`. ∎

**Careful statement of what this does and does not exclude.** `U ≤ B` in a cell
retires that cell **for this certificate route only**: it shows no actual padding
rank can exceed that particular `B`. It does **not** prove `D ≤ 0` there, because `B`
bounds `m_det` from above, so `m_pad ≤ B` is compatible with `m_pad > m_det`. A
source ceiling `U` proves nothing on its own; `U > B` is a **screen**, not a
candidate.

This is as close to a named family as I can get: **no `lambda` is nominated**, and
Claim 5.1 says the screen `U > B` must fail for most five-row cells in each large
degree. I explicitly decline to nominate a cell on intuition.

## 7. Deliverable 4: the missing theorems, stated formally

There are **two** distinct missing theorems, and conflating them is how this gap has
stayed open. One is about effectiveness of the separation; the other is about a
multiplicity gap. Theorem E settles the first in principle and leaves it open in
practice; the second is untouched by anything in B17 or here.

### 7.1 Missing Theorem 1 (effectiveness)

**Proposition M1.** *There is an explicit integer `d_1` of practical size (say
`d_1 ≤ 10^3`) with `I(D45)_{d_1} ⊄ I(R135)_{d_1}`.*

- **What is proved (here).** Such a `d_1` exists with `d_1 ≤ deg P(D45) ≤ 4^49`,
  and the partition may be taken with `ell(lambda) = 5` exactly.
- **Why the existing argument does not give it.** B17-01's ruledness proof is a
  *non-membership certificate at one point*. Formally it establishes
  `F* ∉ D45`, and nothing more; Lemma A then converts any such certificate into a
  degree bound, but the bound it produces depends only on `P(D45)`, not on `F*`.
  There is no residue of the ruledness argument left in the bound.
- **Exactly what would have to be true.** Any of:
  1. an upper bound on `deg P(D45)`, the degree of the 49-dimensional variety of
     `4x4` linear determinantal quartic threefolds in `P^69`;
  2. an upper bound on the Castelnuovo–Mumford regularity of `I(D45)` (regularity
     bounds the generating degrees, hence a fortiori a separating degree);
  3. an explicit finite set of equations of `D45` of low degree whose common zero
     locus does not contain `F*`.
  Any one of these *immediately* replaces `4^49` in Theorem E.
- **Triage.**
  - **(b) follows from known results nobody here had connected:** the *existence* of
    a finite effective bound. Refined Bézout plus the classical projection lemma is
    textbook material; it was simply never applied to this pair of cones. That part
    is now done and is the main positive content of this slot.
  - **(a) genuinely open:** a *usable* bound. `deg P(D45)` is, as far as I can tell,
    an uncomputed classical enumerative number. (The analogous four-variable object
    `D44` has `dim ≤ 34` in a 35-dimensional space, i.e. determinantal quartic
    *surfaces* form at most a hypersurface; even that degree I could not source.)
  - **(c) does NOT apply.** There is no quantified step in the ruledness argument
    waiting to be filled in. Its two non-elementary ingredients — Matsusaka
    specialization of ruledness across a DVR, and Clemens–Griffiths irrationality via
    the intermediate Jacobian — both consume and produce *birational* invariants of
    the special fibre. A birational invariant of `V(F)` is constant on a dense subset
    of every coefficient stratum and carries, by itself, no information about the
    degree of a polynomial in the `c_alpha`. Even a completely effective statement of
    "no smooth cubic threefold is ruled" would output nothing of the form "there is a
    coefficient polynomial of degree `d`". **This is the finding I would most want
    the integrator to record:** the natural-sounding programme "make the ruledness
    argument effective" is not a route to a degree bound, and effort spent there is
    misdirected. The degree must come from the determinant side.

### 7.2 Missing Theorem 2 (a positive multiplicity gap at five rows)

**Proposition M2.** *There exist `d ≥ 1` and `lambda ⊢ 4d` with `ell(lambda) = 5`
such that `i_det(d,lambda) > i_pad(d,lambda)`, equivalently
`D = m_pad - m_det > 0`.*

- **What is proved.** Only `K_det ⊄ K_pad` in some five-row cell with `d ≤ 4^49`
  (Theorem E). By Claim 2.3 this orders nothing.
- **Why the existing argument does not give it.** Non-containment of two subspaces of
  one space is compatible with `i_det = i_pad` and with `i_det < i_pad`. B17-01/03
  and Theorem E are all statements about *which* equations exist, never about *how
  many*.
- **Exactly what would have to be true.** Either
  1. **(cell-inclusion form)** a five-row cell with `K_det ⊄ K_pad` *and*
     `K_pad ⊆ K_det`; the cleanest instance is `i_pad(d,lambda) = 0`, i.e.
     `m_pad = a`; or
  2. **(programme-certificate form)** a five-row cell with a certified global
     `B ≥ m_det` — Claim 6.1 supplies such a `B`, the symmetric rectangular
     Kronecker number — together with `B+1` highest-weight coefficient polynomials
     whose evaluations on *actual* five-variable restrictions of `z·per_3` have a
     nonzero `(B+1)`-minor.
  These are the same statement; (2) is the operational form.
- **Triage.**
  - **(a) genuinely open**, and this slot supplies *evidence against it in this
    regime*: Claim 5.1 proves that for all large `d` the `dim S_lambda`-weighted sum
    of `D(d,lambda)` over all five-row cells is negative, at order `d^49` against an
    `O(d^38)` correction. Five rows is where separation begins and, on the aggregate,
    where `D` is most negative.
  - **(b)** nothing known to me supplies it.
  - **(c)** does not apply; there is no near-miss.

### 7.3 The one thing that changes the picture

Both missing theorems reduce to facts about the single variety `D45` (dimension 50,
codimension 20 in `C^70`, `SL_4 x SL_4 x Z_2`-invariant-theoretic in origin). Its
degree gives M1; its cellwise multiplicities `m_det(d,lambda) ≤ g((d^4),(d^4),lambda)`
bound one side of M2. Neither concerns permanents, ruledness, or cubic threefolds.

## 8. Claim ledger

| # | Claim | Label |
|---|---|---|
| 1.1 | Zariski and Euclidean closure agree on constructible sets | PROVED (standard) |
| 1.2 | `D45` is a Zariski-closed cone, `R135` is Zariski closed; both closures coincide | PROVED |
| 1.3 | "Dense among five-variable cubics" is unambiguous; `D_pad,5 = R135` in either topology | PROVED |
| 1.4 | B17-03 restriction/kernel identification for `ell(lambda) ≤ r` | ADOPTED, re-derived |
| 2.1 | Some degree `d` has `I(D45)_d ⊄ I(R135)_d` | PROVED (from accepted B17) |
| 2.2 | Such a `d` admits `lambda ⊢ 4d`, `ell(lambda) = 5`, with `K_det ⊄ K_pad` | PROVED |
| 2.3 | That gives **no** order between `i_det` and `i_pad`; `D` is unsigned | PROVED (negative) |
| 2.4 | If additionally `K_pad ⊆ K_det` in that cell then `D ≥ 1` | PROVED (conditional) |
| A | Point/variety separation in degree `≤ deg Y` | PROVED |
| B | `deg(image) ≤ D^{dim image}` for a map by degree-`D` forms | PROVED modulo ADOPTED refined Bézout (Fulton, Ex. 12.3.1) |
| C | `dim D45 ≤ 50` by the `(P,Q)`-stabiliser computation | PROVED |
| **E** | **A five-row separating equation exists in degree `d ≤ 4^49`** | **PROVED** (modulo the refined-Bézout citation) |
| 4.1 | `dim D45 = 50` exactly; `dim P(D45) = 49` | PROVED (`≥` MEASURED at one point mod `p`, `≤` from C) |
| 4.2 | `dim R135 = 39` | PROVED |
| 5.1 | For `d` large, `sum_{ell(lambda)=5} dim S_lambda(C^5) · D(d,lambda) < 0` | PROVED (aggregate only) |
| 6.1 | `m_det(d,lambda) ≤ g((d^4),(d^4),lambda)` for `ell(lambda) ≤ 5` | PROVED; = B17-02's `s`, re-derived as a closure bound |
| 6.2 | `m_pad(d,lambda) ≤ U(d,lambda)` (Pieri × plethysm) | PROVED; = B17-08's product ceiling, made explicit |
| 6.3 | A five-row cell admits the standard certificate only if `U > B` | PROVED (screen, not candidate) |
| 7.1 | The ruledness argument cannot yield a degree bound | ASSESSED (argued, not a theorem) |
| — | Explicit five-row equation; named carrier `lambda`; any positive `D` | NOT REACHED |

**Honest negatives, stated plainly.**

1. The degree bound `4^49` is useless for search. It is a proof of principle and a
   relocation of the obstruction, not progress toward a computation.
2. Nothing here produces an equation, a partition, a multiplicity, or a gap.
3. Claim 5.1 is aggregate. It does not prove `D ≤ 0` for any individual five-row
   cell, and I do not claim it does.
4. Claim 6.3's screen is necessary, not sufficient: `U ≤ B` in a cell retires that
   cell **for the standard certificate route only** (there is no `r > B` to be had
   when `m_pad ≤ U ≤ B`); it does not prove `D ≤ 0` there, because `B` is only an
   upper bound for `m_det`.
5. The refined Bézout inequality is cited, not re-proved here. If a reviewer rejects
   the citation, Theorem E degrades to "some finite bound exists by general
   elimination theory", which is still true but without the explicit `4^49`.
6. The pilot's rank is modular at a single point. A deficient rank would have proved
   nothing; the full rank 50 is a valid lower bound and is used only as such.

## 9. One next sufficient test, and its price

**Test.** For `d = 2, ..., d_max` and every `lambda ⊢ 4d` with `ell(lambda) = 5`,
compute the three exact integers

    a(d,lambda)  = mult( S_lambda(C^5), Sym^d(Sym^4 C^5) )
    B(d,lambda)  = symmetric rectangular Kronecker  g_sym( (d^4), (d^4), lambda )   [Claim 6.1]
    U(d,lambda)  = sum over nu, lambda/nu a horizontal d-strip, of
                   mult( S_nu(C^5), Sym^d(Sym^3 C^5) )                              [Claim 6.2]

and report every cell with `U > B`.

**Why this is the right next test.** It is the *only* screen that can either nominate
a five-row candidate for B18-04/09 or, if it never fires, retire the entire five-row
regime for the programme's standard certificate — which, given Claim 5.1, is the
outcome I expect. Either way the board learns whether to move the `D > 0` hunt to
`6 ≤ ell(lambda) ≤ 10`. It uses only symmetric-function arithmetic; it needs no
padding evaluation, no orbit sampling, and no new geometry.

**Price.** The plethysms `Sym^d(Sym^3 C^5)` and `Sym^d(Sym^4 C^5)` in five variables
are degree-`3d` and `4d` symmetric-function computations and are cheap; the binding
cost is the rectangular Kronecker number. For `d ≤ 5` (`|lambda| ≤ 20`, a few hundred
shapes) I estimate one process, well under the default 60 s / 512 MiB pilot cap. For
`d ≤ 8` (`|lambda| ≤ 32`) I estimate minutes and under 2 GiB, i.e. a small explicit
lease, and I recommend asking for it only if the `d ≤ 5` run shows any cell with
`U/B` close to 1. I am not self-issuing either run.

**What it is not.** A nonzero count of `U > B` cells is not a candidate; it is
headroom. A candidate additionally requires `B+1` explicit highest-weight circuits
and an actual-padding minor, which is B18-04's gate, not this test's.

## 10. Provenance and resources

Inputs read: `inputs/PREAMBLE.md`, `inputs/b17_01_report.md`,
`inputs/b17_03_report.md`, `inputs/b17_11_report.md`, `inputs/SUMMARY_B15_B17.md`,
`inputs/BATCH18_PROPOSED_BOARD.md`. All B17 results are used exactly in the scopes
the reviewer (B17-11) accepted: 01-B/01-C (`F* ∉ D45`, with `F*` an actual padding
restriction), 01-A (dominance, hence `D_pad,5 = R135`), 03-A (restriction identity),
03-C (`ell ≤ 4` ⟹ `K_det ⊆ K_pad`), 03-D (lengths 5–10). 01-D is *not* used — it is
precisely what this slot had to supply and what Theorem E supplies in the weakened,
astronomical form recorded above.

Literature used as black boxes, none re-proved here: Chevalley constructibility and
Mumford, *Red Book* I.10 Cor. 1 (Claim 1.1); Fulton, *Intersection Theory* 2nd ed.,
Ex. 12.3.1, refined Bézout (Lemma B); Weyl dimension formula and Pieri's rule
(Claims 5.1, 6.2); the Cauchy/Kronecker decomposition of `Sym(A ⊗ B ⊗ C)` (Claim
6.1). No literature was fetched over the network in this session; the citations are
to standard results and a reviewer should treat the exact reference locations as
unverified pointers, while the statements themselves are standard.

Computation: two `python3` processes, each under `timeout 60` and
`ulimit -v 524288`, one BLAS-free pure-integer workload each, both returning in well
under one second. No lease was requested, issued, or consumed. No background process
remains. Nothing in Sections 1–3 and 5–7 depends on computation; the pilot is used
only to upgrade `dim D45 ≤ 50` to `= 50` (Claim 4.1), which is needed for Claim 5.1
and which confirms — rather than improves — the exponent in Theorem E.

Scope discipline: the ten excluded cells and the original-entry diagonal method were
not reopened. No new question was substituted for the assigned one; the assigned
question was answered in form (1) and form (4), and forms (2) and (3) are recorded
as NOT REACHED with mechanisms identified.
