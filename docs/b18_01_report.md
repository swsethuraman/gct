# B18-01 (revision 2) — The five-variable result, repaired

Status: **COMPLETE.**
- **Corrected finite degree theorem** (§3.5): `d_sep ≤ d_5 ≤ deg P(D45) ≤ 4^49`, conditional on refined Bézout, which is verified only through a secondary source.
- **`dim D45 = 50`**: certified and independently reproduced.
- **Aggregate inequality** kept as an aggregate only; v1's strategic readings, `MN = F·I4`, and two further overstatements are withdrawn.
- **One named carrier family**: the 23 degree-five five-row cells, all with `a = 1`, where separation equals a gap `D = 1`. One of the 23 is excluded; the missing step and a priced two-stage test are stated.
- **No separating equation and no gap is produced.**

## 0. Provenance and intake

**Starting point of this session** (read-only commands, run before anything was written):

```
git rev-parse HEAD        -> f12c024993052a6f8b85c87d00d5e26f8d8b8e0f
git rev-parse HEAD^{tree} -> ce0a5f9221f856bcdc34fcf8577a5a6cba37392d
```

No other git command was run.

**Intake of the prior report (v1).** It is evidence, not a draft. It was copied byte-for-byte before any change:

| Object | Path | SHA-256 | Bytes |
|---|---|---|---|
| v1 report, as attached | `Claude_Handover_B15_B18/batch18_launch/b18_01_report_v1.md` | `d03d5c976405a603abc8831ac20be3673afa2a0117dc31cd2523a58de29fc60c` | 43110 |
| preserved copy | `results/b18_01/intake/b18_01_report_v1.md` | same | 43110 |
| board review of v1 | `Claude_Handover_B15_B18/BATCH18_REVISED_BOARD.md`, §"Intake of the first Slot 01 report" | `beedfa106253f7075b14f8304ed5791b606301ffb681f10c040dc33b50d5b9e5` | — |
| preamble | `Claude_Handover_B15_B18/batch18_launch/B18_PREAMBLE.md` | `633cf39b714d5ce154b1c4cd03edd59965d2bd2cf66607fdf02806883c791acb` | — |
| slot brief | `Claude_Handover_B15_B18/batch18_launch/B18-01.md` | `fc52f7a2c36af61cbff66b78911a6770deb171516d1bb52ebafca3ef30556f2a` | — |

**The v1 scripts do not exist.** v1 names `out/b18_01_pilot.py` and `out/b18_01_control.py` as its evidence. No `out/` directory exists here, and nothing with those names is in this worktree. So v1's rank-50 measurement had no reviewable artifact behind it. All rank evidence in this revision is new, and it is under `analysis/b18_01_*` and `results/b18_01/`.

## 1. Plain terms

Batch 17 proved that one actual five-variable restriction of the padded permanent lies outside the closure of five-variable 4×4 determinants. So **some** determinant equation with exactly five rows fails on padding. v1 set out to put a number on "some". This revision keeps what survives review, proves what v1 only measured, and withdraws what was wrong.

What this revision does, point by point against the board's review:

1. **The degree theorem**, stated with every hypothesis: what "degree" means, which closure, which accepted B17 results it consumes, and what it does *not* say. It is a finite existence bound of astronomical size. It is **not** a search budget and **not** an equation.
2. **`dim D45 = 50`**, now with both halves certified by exact integer computation, not a single modular rank:
   - the lower bound is an exact rational rank of 50;
   - the upper bound is an exact rank-30 matrix of symmetry directions that the differential provably annihilates.

   The scripts and matrices are delivered for independent rerun. I also record which later claims need only the lower bound, so none of them silently relies on equality.
3. **The aggregate five-row inequality** is kept, as an aggregate. The strategic readings v1 drew from it are **withdrawn**: "five rows is where `D` is most negative", "most `U > B` screens must fail", and "move the hunt to six or more rows". It excludes no individual cell.
4. **The `MN = F·I4` criterion is withdrawn.** I say exactly why it fails and give the formulation that correctly enforces the determinant condition and handles limits.
5. **Two v1 overstatements are corrected.**
   - "The degree of `D45` is the only route to a usable equation" is withdrawn.
   - Sufficient kernel inclusion is no longer equated with the necessary multiplicity condition.
6. **References are checked** against primary sources where I could reach them, with versions. Where I could not, I say so and do not use the pointer as if verified. The four-variable literature appears only as a control.

Then **one** forward step, with the argument and the step that still lacks proof, and one priced next test.

Expected and actual outcome: a corrected theorem and a precise construction problem. **No usable separating equation is produced here.**

## 2. Conventions (ADOPTED, unchanged from the preamble and B17-03)

- Forms live in `Sym^4(V*)`. The coefficient ring is `Sym(Sym^4 V)`, with **ordinary** coefficients `c_alpha = [x^alpha] F` of weight `alpha ≥ 0`.
- Raising acts as `E_ij c_alpha = (alpha_i + 1) c_(alpha + e_i - e_j)` if `alpha_j > 0`, and `0` otherwise. No factorial-normalised symbol is used anywhere in this report.
- `a`, `i_det`, `i_pad`, `m_det = a - i_det`, `m_pad = a - i_pad` and `D = m_pad - m_det = i_det - i_pad` are per cell `(d, lambda)`, `lambda ⊢ 4d`, exactly as in the preamble.
- `s` is the **symmetric** rectangular Kronecker number, transposition included. The **ordinary** rectangular Kronecker coefficient is written `g((d^4),(d^4),lambda)`; it is a different number with `s ≤ g`.
- `T` is the product-map target multiplicity and `U = min(a, T)` the clipped padding ceiling. `B = min(a, s - b)` only for a certified boundary rank `b`.

Five-variable objects:

- `V5 = C^5`, `W5 = Sym^4(V5*)`, `dim W5 = 70`.
- `phi : (Mat_4)^5 -> W5`, `phi(B_0,...,B_4) = det(x_0 B_0 + ... + x_4 B_4)`. Each of its 70 coefficient functions is homogeneous of degree 4 in the 80 matrix entries.
- `D45 = Zariski closure of phi((Mat_4)^5)` in `W5`, a closed irreducible cone.
- `R135 = { l·C : l in V5*, C in Sym^3 V5* }`, closed (B17-01).
- `F*` is B17-01's certified actual five-variable padding point, `F* = x_0 · per_3(sum_k x_k A_k)`, with `F* in R135 \ D45` (accepted B17 result; §3.1 gives the exact acceptance label).

## 3. The finite degree theorem, stated precisely

### 3.1 Objects, closures, degree, and the inputs consumed

**Closures.** Every closure in this report is a **Zariski closure** in the named affine space over `C`:

- `X_det` is the Zariski closure of `GL16 · det4` in `W16 = Sym^4((C^16)*)`.
- `X_pad` is the Zariski closure of `GL16 · (z·per3)` in `W16`, with `z` and the nine permanent entries independent coordinates.
- `D45` and `R135` are as in §2.

No Euclidean-closure statement is used anywhere below (see §7 on the dropped Mumford pointer).

**Degree.** "An equation of degree `d`" means an element of `I(X)_d`: the homogeneous degree-`d` part of the vanishing ideal of `X` inside `Sym^d(Sym^4 C^16)`. It is a polynomial of degree `d` in the ordinary coefficients `c_alpha`, carrying `GL16`-weights `lambda ⊢ 4d`. It is **not** the degree `4` of the forms and **not** a degree in the variables `x`. The same meaning applies in five variables, with `Sym^d(Sym^4 C^5)`.

**Inputs consumed.** These are accepted in `B15-11/docs/b17_11_report.md`, claim table. Nothing else from B17 is used.

| Label | Accepted statement (B17-11 wording, abridged) | Used for |
|---|---|---|
| **01-A** | the actual five-variable `per3` restriction map is dominant onto cubic forms | `closure(rho_5(X_pad)) = R135` |
| **01-C** | for every smooth cubic threefold `C` and nonzero `l`, `lC` is outside the det4 coefficient closure; the supplied point `F* = x_0·C*` is an actual padding restriction (smoothness and frame certificates) | a point of `rho_5(X_pad)` outside `D45` |
| **03-A** | for `ell(lambda) ≤ r`, highest-weight spaces and restriction kernels identify between `GL_r` and `GL16` | transporting cells between 5 and 16 variables |
| **03-C** | for every `d` and `ell(lambda) ≤ 4`, `K_det ⊆ K_pad` | only to exclude `ell(lambda) ≤ 4` in the conclusion |

B17-03's Lemma 2 (arbitrary substitutions `f∘T`, `T ∈ Hom(C^r, C^16)`, not only injective frames) is part of the argument accepted under 03-A/03-C. It gives `closure(rho_5(X_det)) = D45`, because `det4∘T` for arbitrary `T` is exactly `det(sum_k x_k B_k)` for arbitrary `B`.

**One external theorem** is consumed: the refined Bézout inequality in Lemma B. Its verification status is in §7: secondary quotation only, unverified against the primary text.

### 3.2 The dimension of `D45` (review point 2: repaired and closed)

**Proposition 3.2 (PROVED; the certificate was independently reproduced by the integrator).** `dim D45 = 50` as an affine cone in `C^70`, so `dim P(D45) = 49`.

*Upper bound — the proof is the group action.*
1. **`phi` is constant on orbits.** Let `G = {(P,Q) ∈ GL4 × GL4 : det P · det Q = 1}`, of dimension 31, acting by `B_k ↦ P B_k Q`. Then `phi(P B Q) = det(P)·det(Q)·phi(B) = phi(B)`, so `phi` is constant on every `G`-orbit.
2. **The orbit directions are in the kernel at every point.** The tangent vectors `(X B_k + B_k Y)_k` with `tr X + tr Y = 0` lie in `ker dphi_B` for **every** `B`. Equivalently, by Jacobi's formula, `d/dt det((1+tX) M (1+tY)) = (tr X + tr Y)·det M`.
3. **Generic orbit dimension is at least 30.**
   - The orbit map `G → (Mat_4)^5`, `g ↦ g·B'`, has constant differential rank along `G` by translation.
   - For any morphism from an irreducible variety, the differential rank at a general point is at most the dimension of the image closure. So `dim(G·B') ≥ rank T(B')`, where `T(B')` is the `31 × 80` matrix of tangent vectors.
   - `rank T` is lower semicontinuous and equals 30 at the recorded point. So `dim(G·B') ≥ 30` for `B'` in a dense open set.
4. **Conclusion.** The fibre of `phi` through such a `B'` contains `G·B'`. By the fibre-dimension theorem, `dim D45 ≤ 80 - 30 = 50`.

The two-point check `T·J = 0` is a consistency check on the implementation. It is not the proof of the upper bound: the proof is steps 1–4.

*Lower bound.* The Jacobian `J(B)` of `phi` (80 × 70, ordinary coefficients) has exact rational rank 50 at the recorded integer point. At a general point `B'`:
- `phi(B')` is a smooth point of `D45`;
- `dphi_{B'}` maps into `T_{phi(B')} D45`, which has dimension `dim D45`;
- rank is lower semicontinuous, so the rank at any point is at most the rank at a general point.

Hence `dim D45 ≥ rank_Q J(B) = 50`. Note that `rank_Q` is used, not a modular rank. The modular ranks recorded alongside (50 mod `2^31−1` and mod 65521) are consistent but unused.

*Evidence.*
- Script: `analysis/b18_01_rank_certificate.py`.
- Output: `results/b18_01/rank_certificate.json`, with the full matrices in `rank_certificate_matrices.json`.
- Two points: v1's point and seed 1801. Each has `rank_Q J = 50`, `rank_Q T = 30` and `T·J = 0`.
- Controls: the adjugate identity, the Euler identity, and all 70 monomials of the determinant present.
- Negative controls, both failing as required: a sign-flipped cofactor breaks the identities, and a trace-one direction is not annihilated.
- The integrator reproduced all three facts with an independent Leibniz / `Fraction` implementation.

*Which later claims need which half.*
- Theorem 3.5 needs **only** the upper bound `dim P(D45) ≤ 49`.
- §4 needs **only** the lower bound `dim P(D45) > 38`.
- Nothing in this report needs the equality itself.

### 3.3 Lemma A — separating a point from a projective variety in degree at most its degree (PROVED)

**Lemma A.** Let `Y ⊆ P^m` be closed and irreducible, of dimension `k` and degree `delta`, and let `p ∉ Y`. Then there is a form `f` with `deg f ≤ delta`, `f|_Y = 0` and `f(p) ≠ 0`.

*Proof.*
1. **A linear space through `p` avoiding `Y`.**
   - Projection from `p` is a morphism on `Y`, with image `Y' ⊆ P^(m−1)` of dimension `≤ k`.
   - A general linear `Lambda' ⊆ P^(m−1)` of dimension `m−k−2` misses `Y'`, because `(m−k−2) + k < m−1`.
   - The cone `Lambda` over `Lambda'` with vertex `p` is linear of dimension `m−k−1` and meets `Y` in no point: a point `y ∈ Lambda ∩ Y` would have `pi_p(y) ∈ Lambda' ∩ Y'`, and `p ∉ Y`.
2. **A finite projection.**
   - Choose a hyperplane `L ⊂ Lambda` with `p ∉ L`. Then `dim L = m−k−2` and `L ∩ Y = ∅`.
   - Projection from `L` is finite on `Y`, so its image `Z ⊆ P^(k+1)` is an irreducible hypersurface.
   - `deg Z · deg(Y → Z) = delta`, so `deg Z ≤ delta`.
3. **The form.** Let `g` define `Z` and put `f = pi_L^* g`. It has degree `deg Z` and vanishes on `Y`.
4. **It does not vanish at `p`.** If `f(p) = 0`, then `pi_L(p) ∈ Z`, so the fibre `<L,p> \ L = Lambda \ L` meets `Y`, contradicting step 1. ∎

### 3.4 Lemma B — degree of an image closure (PROVED, conditional on the refined Bézout inequality)

**Lemma B.** Let `psi : P^n ⇢ P^M` be given by forms `f_0..f_M` of common degree `D`, not all zero, with base locus `Zb`. Let `Y` be the closure of `psi(P^n \ Zb)` and `k = dim Y`. Then `deg Y ≤ D^k`.

*Proof.*
1. **General points of `Y`.** Let `U ⊆ Y` be dense open, contained in the image, with every fibre of `psi` over `U` of pure dimension `n−k` (fibre-dimension theorem). For general hyperplanes `H_1..H_k`, the set `Y ∩ H_1 ∩ … ∩ H_k` is `deg Y` reduced points `y_1..y_delta`. All of them lie in `U`, because a general codimension-`k` linear section misses the proper closed subset `Y \ U`.
2. **The hypersurfaces.** Write `H_i = V(sum_j a_ij y_j)` and put `G_i = V(sum_j a_ij f_j)`, a hypersurface of degree `D` for general `a_i`. Let `G = G_1 ∩ … ∩ G_k`.
3. **Each `y_j` gives a component of `G`.** Let `W_j` be an irreducible component of `closure(psi^{-1}(y_j))` of dimension `n−k`, and let `W ⊇ W_j` be an irreducible component of `G`.
   - `W ⊄ Zb`, so `W \ Zb` is irreducible and dense in `W`.
   - `psi(W \ Zb)` lies in the finite set `Y ∩ ∩_i H_i`, so it is a single point, necessarily `y_j`.
   - Hence `W ⊆ closure(psi^{-1}(y_j))`, so `dim W ≤ n−k`, so `W = W_j`.

   Distinct `j` give distinct components. Therefore `deg Y ≤` the sum of the degrees of the irreducible components of `G`.
4. **Reducible hypersurfaces — a repair of v1.** v1 applied the inequality directly to the `G_i`. A general `G_i` need not be irreducible, while the inequality is stated for irreducible subvarieties. So write `G_i = ∪_t G_{i,t}` with each `G_{i,t}` irreducible and `sum_t deg G_{i,t} ≤ D`. Each irreducible component of `G` is an irreducible component of some `∩_i G_{i,t_i}`.
5. **Refined Bézout.** For irreducible `V_1..V_s ⊆ P^n`, the degrees of the irreducible components of `∩ V_i` sum to at most `prod_i deg V_i`. Hence

       sum over components of G of deg  ≤  sum over (t_1..t_k) of prod_i deg G_{i,t_i}  =  prod_i ( sum_t deg G_{i,t} )  ≤  D^k.   ∎

### 3.5 Theorem 3.5 — the finite degree theorem

**Theorem 3.5 (PROVED, conditional only on the refined Bézout inequality in Lemma B, step 5).**

*Hypotheses.* Accepted results 01-A, 01-C, 03-A and 03-C (§3.1), and B17-03 Lemma 2; Proposition 3.2 (upper bound only); Lemmas A and B. Put `delta_45 = deg P(D45)`, the degree of the projectivised determinant pencil closure in `P^69`.

*Conclusions.*
1. **Five-variable separator.** There is a form `h ∈ Sym^d(Sym^4 C^5)`, in the ordinary coefficients of five-variable quartics, that vanishes on `D45`, has `h(F*) ≠ 0`, and has degree

       d = deg h ≤ delta_45 ≤ 4^(dim P(D45)) ≤ 4^49 = 316912650057057350374175801344.

2. **A five-row cell.** For this `d` there is a partition `lambda ⊢ 4d` with **exactly five rows** such that `K_det(d,lambda) ⊄ K_pad(d,lambda)` inside `H^16_{d,lambda}`. That is, some highest-weight polynomial of degree `d` in the ordinary coefficients of 16-variable quartics lies in `I(X_det)` and not in `I(X_pad)`.
3. **The minimal degrees.** Put

       d_5   = min{ d : some cell (d,lambda) with ell(lambda) = 5 has K_det ⊄ K_pad }
       d_sep = min{ d : I(X_det)_d ⊄ I(X_pad)_d }.

   Then `d_sep ≤ d_5 ≤ delta_45 ≤ 4^49`.

*Proof.*
1. **The separator.**
   - The 70 coefficients of `phi` are forms of degree `D = 4` in the 80 matrix entries. `P(D45)` is the closure of the image of the induced rational map `P^79 ⇢ P^69`, and it is irreducible because `(Mat_4)^5` is.
   - Proposition 3.2 gives `dim P(D45) ≤ 49`.
   - Lemma B gives `delta_45 ≤ 4^(dim P(D45)) ≤ 4^49`.
   - By 01-C, `F* ≠ 0` and `[F*] ∉ P(D45)`.
   - Lemma A applied to `Y = P(D45)` and `p = [F*]` gives `h`.
2. **Separation in five variables.**
   - `A_5 = Sym(Sym^4 C^5)` is a `GL5`-algebra, and `I(D45)_d` and `I(R135)_d` are `GL5`-submodules.
   - `h ∈ I(D45)_d` and `h(F*) ≠ 0` with `F* ∈ R135`, so `I(D45)_d ⊄ I(R135)_d`.
   - In characteristic zero, one `GL5`-submodule is contained in another iff the containment holds on the highest-weight vectors of every weight. So for some `lambda ⊢ 4d` with `ell(lambda) ≤ 5`,

         I(D45)_d ∩ H^5_{d,lambda}  ⊄  I(R135)_d ∩ H^5_{d,lambda}.

3. **Transport to 16 variables.**
   - By 03-A, `H^5_{d,lambda}` identifies with `H^16_{d,lambda}`.
   - Using `closure(rho_5 X_det) = D45` (B17-03 Lemma 2) and `closure(rho_5 X_pad) = R135` (01-A with Lemma 2), the two kernels become `K_det(d,lambda)` and `K_pad(d,lambda)`.
   - 03-C excludes `ell(lambda) ≤ 4`, so `ell(lambda) = 5`.
4. **The minima.** Step 3 gives `d_5 ≤ d ≤ delta_45`. A separation in one cell is a separation of the full degree-`d` ideals, so `d_sep ≤ d_5`. ∎

### 3.6 What Theorem 3.5 does **not** say

- **It is not a search budget.** `4^49 ≈ 3.2·10^29`. It does not predict separation at any feasible degree. It is compatible with `d_5` being very small, and equally with `d_5` being enormous.
- **It is not an equation.** It names no `h`, no `lambda` and no module. The `h` of Lemma A comes from unconstructed general projections.
- **It concerns separation, not multiplicities.** In the cell of part 2 it gives `i_det ≥ 1` and `m_pad ≥ 1`, and nothing more. It gives **no** inequality between `i_det` and `i_pad`, so **no** sign for `D`. Two distinct lines in a plane already realise `K_det ⊄ K_pad` with `i_det = i_pad`.
- **It is not specific to padding.** The same bound separates every point outside `P(D45)`. It uses only `F* ∉ D45`.
- **Dependence.**
  - Only the upper bound `dim P(D45) ≤ 49` enters. Without it, Lemma B with `k ≤ 69` would still give `4^69`.
  - If the refined Bézout inequality were rejected, the theorem degrades to "`d_5` is finite". That follows from 01-C and the Nullstellensatz alone, with no explicit number.
- **Calibration, not evidence about `D45`.** For four-variable linear determinantal quartics, the analogous Bézout bound is `4^33 ≈ 7.4·10^19`. The actual degree of that divisor is `deg F1 = 320112` (§7, verified). So the Bézout bound can be loose by many orders of magnitude. This says nothing about `delta_45`, which remains unknown.

## 4. The aggregate five-row inequality — kept as an aggregate only

### 4.1 Statement and proof

**Lemma 4.1 (PROVED).** `dim R135 = 39`.

*Proof.* The map `mu : V5* × Sym^3 V5* → W5`, `(l, C) ↦ lC`, has image `R135`. Take `l ≠ 0` and `C` irreducible and not divisible by `l`; such pairs are dense. By unique factorisation, `mu^{-1}(lC) = {(t l, t^{-1} C) : t ≠ 0}`, which has dimension 1. So `dim R135 = 5 + 35 − 1 = 39`. ∎

**Proposition 4.2 (PROVED).** There is `d_0` such that for every `d ≥ d_0`:

    S_5(d)  :=  sum over lambda ⊢ 4d with ell(lambda) = 5 of  dim S_lambda(C^5) · D(d,lambda)  <  0.

*Hypotheses.* 03-A, so that five-variable and 16-variable cells coincide for `ell ≤ 5`. The **lower** bound `dim P(D45) ≥ 49` from Proposition 3.2; any value `> 38` would do. Lemma 4.1.

*Proof.*
1. **The whole-degree sum.** For a closed `GL5`-stable cone `X ⊆ C^70`,

       dim I(X)_d = sum over lambda ⊢ 4d, ell(lambda) ≤ 5 of  i_X(d,lambda) · dim S_lambda(C^5).

   So `S(d) := sum over ell ≤ 5 of dim S_lambda(C^5)·D(d,lambda) = dim I(D45)_d − dim I(R135)_d = h_R135(d) − h_D45(d)`, where `h_X` is the Hilbert function of `C[X]`.
2. **Leading behaviour.** For `d ≫ 0`, `h_X(d)` is a polynomial of degree `dim P(X)` with leading coefficient `deg P(X)/(dim P(X))!`. Here `dim P(D45) ≥ 49` and `dim P(R135) = 38`, so `S(d) ≤ −c·d^49` for large `d`, with `c > 0`.
3. **Rows up to four are negligible.** Split `S = S_≤4 + S_5`. For `ell(lambda) ≤ 4`, `|D| ≤ a`.
   - By 03-A, `sum over ell ≤ 4 of a(d,lambda)·dim S_lambda(C^4) = dim Sym^d(Sym^4 C^4) = binom(34+d, 34)`.
   - By Weyl's formula, `dim S_lambda(C^5)/dim S_lambda(C^4) = prod_{i=1..4} (lambda_i + 5 − i)/(5 − i) ≤ (4d+4)^4/24` when `lambda_5 = 0`.
   - Hence `|S_≤4(d)| ≤ ((4d+4)^4/24)·binom(34+d, 34) = O(d^38)`.
4. **Conclusion.** `S_5(d) = S(d) − S_≤4(d) < 0` for all large `d`. ∎

`d_0` is **not effective**: the leading constant involves the unknown `delta_45`.

### 4.2 What Proposition 4.2 says, and what it does not

It says only this: for all sufficiently large `d`, the `dim S_lambda(C^5)`-weighted sum of `D` over the five-row cells of degree `d` is negative.

**It excludes no individual cell.** In degree `d` there are `O(d^4)` five-row partitions of `4d`, with weights ranging over many orders of magnitude. A negative weighted sum is compatible with `D(d,lambda) > 0` in any particular cell. It is even compatible with `D > 0` in most cells by count, if a few heavily weighted cells carry the negative mass. Nothing here bounds any single `D(d,lambda)`.

### 4.3 Withdrawn strategic readings of v1

v1 drew three strategic conclusions from this aggregate. All three are **withdrawn**.

1. **Withdrawn: "Five rows is where separation begins and, on the aggregate, where `D` is most negative"** (v1 §7.2). Also withdrawn with it: the v1 heading "five rows is the wrong regime for `D > 0`", and v1's "structurally the wrong place to look for `D > 0`" (§1(3) and §5).
   - "Most negative" compares five rows with other lengths. No aggregate for `ell(lambda) = 6..10` was computed or bounded, so no comparison exists.
   - "Wrong regime" and "wrong place" assert a per-cell tendency. The aggregate has no per-cell content (§4.2).
   - What survives: five rows is the **first** length at which separation is proved (Theorem 3.5 with 03-C). No length is known to be better or worse for a positive gap.
2. **Withdrawn: "Claim 5.1 says the screen `U > B` must fail for most five-row cells in each large degree"** (v1 §6.3).
   - `U ≥ m_pad` and `B ≥ m_det` are ceilings, not the multiplicities. A statement about a weighted sum of `m_pad − m_det` constrains neither ceiling in any cell.
   - Nothing about the aggregate predicts how often `U > B`. Only the per-cell screen itself answers that.
3. **Withdrawn: "that pushes any serious `D > 0` hunt into `6 ≤ ell(lambda) ≤ 10`"** (v1 §5, and the related sentence in v1 §9).
   - The only proved non-positivity is 03-C, for `ell(lambda) ≤ 4`.
   - Five-row cells are neither excluded nor deprioritised by anything proved here or in B17.
   - **This report does not recommend abandoning five rows.** Cell selection belongs to Slot 06, on per-cell evidence.

v1's claim ledger labelled its Claim 5.1 "PROVED (aggregate only)", which was correct. The error was in the surrounding prose that drew strategy from it, and that prose is corrected here.

## 5. The `MN = F·I4` criterion — withdrawn

### 5.1 The withdrawn statement and why it fails

v1 §6.1 asserted: "`F ∈ D45` (for reduced `F`) iff there are a linear `M` and a cubic `N`, both `4×4`, with `MN = F·I_4`." **This is withdrawn.**

**Counterexample (PROVED).** Take `F = lC` with `l ≠ 0` linear and `C` a smooth cubic threefold, for example `F*`. `F` is reduced. Put `M = l·I_4` and `N = C·I_4`; then `MN = lC·I_4 = F·I_4`. So the criterion places `F` in `D45`. But `F ∉ D45` by the accepted result 01-C.

**What went wrong.** `MN = F·I_4` implies only `det M · det N = F^4`. It does not force `det M = F`: here `det M = l^4`. The criterion never imposes the determinant condition it was meant to encode. A second, independent defect remains even after that is repaired.
- **(i) Missing determinant condition.** Adding `det M = c·F` with `c ≠ 0` removes the scalar-matrix witness. `N = adj(M)` is then automatic up to scale when `F ≠ 0`.
- **(ii) Limits.** Even so repaired, an existential condition over finite matrices describes the **image** `phi((Mat_4)^5)`, not its closure `D45`. B17-01's accepted proof explicitly covers "limits whose matrix entries cannot be specialized to finite matrices". Whether every point of `D45` is an honest determinant is not established here, and no criterion of the form "there exist finite `M`, `N` with…" may be used as if it characterised the closure.

A narrower true statement, for the record, and not used: if `F` is irreducible, `MN = F·I_4` and `det M ≢ 0`, then `det M` is a quartic divisor of `F^4`, so `det M = c·F` with `c ≠ 0` and `F ∈ phi(...)`. This concerns the image only. It says nothing about boundary points of `D45`, and nothing about reducible `F`, where the separating points live.

### 5.2 The formulation that enforces the determinant condition and handles limits

**Proposition 5.2 (PROVED, standard).** Let `phi^* : Sym(Sym^4 C^5) → C[(Mat_4)^5]` be the pullback, with `phi^*(c_alpha) = [x^alpha] det(sum_k x_k B_k)`. Then

    I(D45) = ker phi^*,   and, degreewise,   I(D45)_d = ker( phi^*_d : Sym^d(Sym^4 C^5) → C[(Mat_4)^5]_{4d} ).

Equivalently, `I(D45) = ⟨c_alpha − phi_alpha(B)⟩ ∩ C[c]`, the elimination ideal of the graph of `phi`.

*Proof.* A polynomial `h` in the `c_alpha` vanishes on the image of `phi` iff `h∘phi = phi^*(h) = 0`. By continuity in the Zariski topology, it then vanishes on the image closure `D45`, and conversely. So `ker phi^* = I(phi(…)) = I(D45)`. The elimination description is the same statement for the graph ideal. ∎

**Why this is the right repair.**
- **The determinant condition is built in.** `phi_alpha(B)` are the coefficients of `det(sum_k x_k B_k)` itself. No auxiliary factor `N` appears, so no scalar-matrix witness can arise.
- **Limits are handled automatically.** The kernel of a pullback is the ideal of the Zariski closure of the image. Every limit point of `D45`, including those not attained by finite matrices, satisfies every element of `ker phi^*`.
- **The trivial witness cannot defeat it.** There is no existential quantifier over matrices. A point `F` is tested by evaluating the elements of the kernel. `(l·I_4, C·I_4)` is not a point of `(Mat_4)^5` mapping to `lC`, because `det(l·I_4) = l^4`. So it plays no role, and `lC` fails the test by 01-C.
- **It is finite linear algebra in each degree.** The image of `phi^*_d` lies in the `SL4 × SL4`-invariants of degree `4d` that are also invariant under transposition. Weight by weight, `K_det(d,lambda)` is the kernel of `phi^*` restricted to `H^5_{d,lambda}`.

**Cost, stated so it is not mistaken for a plan.**
- `dim Sym^d(Sym^4 C^5) = binom(69 + d, d)` is 2485 for `d = 2`, 59640 for `d = 3` and 1,088,430 for `d = 4`.
- The target `C[(Mat_4)^5]_{4d}` has `binom(79 + 4d, 4d)` monomials: about `5.8·10^10` at `d = 2` and `3.2·10^14` at `d = 3`.
- A symbolic kernel computation is therefore not feasible beyond the smallest degrees. Any use must be cellwise and sampling-based, with a certificate for the rank. §8 states exactly what such a certificate requires.
- **No incidence or elimination computation was run in this session.**

## 6. Two further overstatements in v1 — withdrawn

### 6.1 Withdrawn: "the degree of `D45` is the only route to a usable equation"

v1 stated this in several forms, all **withdrawn**:
- "the only quantity standing between this and a usable bound is `deg P(D45)`" (§3.5);
- "any effective bound must come from elimination theory on the determinant side" (plain terms, item 2);
- "the degree must come from the determinant side" and "effort spent there is misdirected" (§7.1(c));
- "both missing theorems reduce to facts about the single variety `D45`" (§7.3).

**Why these are wrong.**
1. **A bound is not the quantity.** `delta_45` bounds `d_5` from above through Lemma A. It is not `d_5`. A separating equation of degree far below `delta_45` may exist and may be found without knowing `delta_45`. Improving the upper bound is one route. Finding an actual low-degree separator is a different route that bypasses it.
2. **Routes that do not pass through `deg P(D45)`:**
   - **Direct certified construction in a cell.** Exhibit `h ∈ K_det(d,lambda)` with `h(F*) ≠ 0` at some small `d`, certified as in §8. That gives `d_5 ≤ d` outright.
   - **Regularity or generator degrees.** Any bound on the generating degrees of `I(D45)`, obtained by whatever method, gives `d_5 ≤` that bound (§3.6, dependence).
   - **Explicit geometric equations.** A closed condition satisfied by every member of `D45` and failed by `lC`, given by explicit covariants, is a separator of known degree. An example of a structurally blocked candidate, recorded as a control: restriction to four variables. By the accepted 03-B, every `lC` restriction lies in the four-variable determinant closure, so no equation of that closure pulled back along restrictions can separate. That failure is structural, not a degree problem.
   - **An effective form of the specialization argument.** v1 §7.1(c) asserted that the ruledness and specialization argument "cannot yield a degree bound". That assertion was never proved; v1 itself labelled it "ASSESSED". It is **withdrawn** together with the recommendation that such effort is misdirected. Whether boundedness arguments, for example for the family of limit cycles, can make the specialization quantitative is **open and unassessed** here.
3. **The two missing theorems do not reduce to `D45` alone.** A positive gap concerns `m_pad`, a property of `R135` and of `X_pad`, as much as `m_det`.

### 6.2 Withdrawn: equating a sufficient kernel inclusion with the necessary multiplicity condition

v1 §7.2, under "exactly what would have to be true", offered two forms and wrote "These are the same statement":
- (1) a five-row cell with `K_det ⊄ K_pad` and `K_pad ⊆ K_det`;
- (2) a certified `B ≥ m_det` with an actual padding minor of size `B + 1`.

**Withdrawn.** The corrected logic:

- **The condition itself.** A positive gap in a cell **is** `D(d,lambda) = i_det − i_pad > 0`, a comparison of **dimensions**. That is both necessary and sufficient.
- **(1) is sufficient, not necessary.** `K_pad ⊊ K_det` forces `i_det > i_pad`. But `i_det > i_pad` can hold with `K_pad ⊄ K_det`: a plane and a line not in it, inside a 3-dimensional `H`. Inclusion is one way to obtain the dimension comparison. It is not what the comparison means.
- **(2) is sufficient, not necessary in any usable sense.** `r > B` with `B ≥ m_det` and `r ≤ m_pad` implies `m_pad > m_det`. Conversely, `D > 0` guarantees a certificate only with `B = m_det` exactly. With the available ceilings (`s`, `s − b`), no certificate need exist even when `D > 0`.
- **(1) and (2) are not the same statement.** (1) produces no numbers and (2) produces no inclusion. Neither implies the other.
- **The same applies to v1's "cleanest sufficient statement"** (`i_pad = 0` in a separating cell). It is sufficient, and its hypothesis is not known to hold in any cell.

### 6.3 Convention corrections carried with these withdrawals

- **Which Kronecker number.** v1 Claim 6.1 proved `m_det ≤ g((d^4),(d^4),lambda)`, the **ordinary** rectangular Kronecker coefficient. v1 §7.2 then called it "the symmetric rectangular Kronecker number". These differ.
  - The pullback argument, together with invariance of `phi^*` under transposition `B_k ↦ B_k^T`, places `C[D45]_d` in the transposition-fixed part. That gives `m_det ≤ s ≤ g`, with `s` the **symmetric** number of the preamble.
  - Neither `g` nor `s` was computed in v1 or here. The global bound to quote is `B = min(a, s − b)`, and only for a certified `b`; with `b = 0`, `B = min(a, s)`.
- **Clipping.** v1 Claim 6.2's `U` is the unclipped product-target multiplicity `T`. The board requires the clipped `U = min(a, T)`. v1's §9 screen "`U > B`" is restated as `min(a,T) > min(a, s − b)`, with the same "screen, not candidate" reading.

## 7. References — citation pass

Fetched primary sources are stored under `results/b18_01/literature/` with their SHA-256. A pointer that could not be checked against its primary source is marked **UNVERIFIED** and is not used as if checked. Citation fetching was capped as instructed.

| # | Citation | Used for | Status |
|---|---|---|---|
| R1 | M. Leal, C. Lozano Huerta, M. Vite, *The Noether–Lefschetz locus of surfaces in P^3 formed by determinantal surfaces*, arXiv:2303.09028 **v3** (1 Nov 2024); journal reference on arXiv: Mathematische Nachrichten, 2024 | §3.6 calibration only (four-variable **control**) | **VERIFIED against primary PDF v3** (`arXiv_2303.09028v3.pdf`, sha256 `67b1701f…4b22`; extracted text `llv_v3.txt`, sha256 `3dcd9ce1…ded7`). See note below |
| R2 | W. Fulton, refined Bézout inequality: *Introduction to Intersection Theory in Algebraic Geometry*, CBMS Regional Conf. Ser. Math. 54 (AMS, 1984), Prop. 2.3; also commonly cited as *Intersection Theory*, 2nd ed. (Springer, 1998), Example 8.4.6 | Lemma B, step 5 | **SECONDARY ONLY, UNVERIFIED against the primary.** Neither Fulton text was reachable. The statement as used matches the quotation in M. Sharir, N. Solomon, *Incidences between points and lines in R^4*, arXiv:1411.0777 **v2** (25 Mar 2015), Theorem 2.2, citing Fulton CBMS 54, Prop. 2.3 (`arXiv_1411.0777_latest.pdf`, sha256 `0741e2d2…4589`). The Example 8.4.6 numbering is **not** confirmed. |
| R3 | D. Mumford, *The Red Book of Varieties and Schemes*, 2nd expanded ed., LNM 1358 (Springer, 1999), Ch. I §10 (Zariski versus classical closure) | **Nothing.** v1 used it for a Euclidean/Zariski comparison that this revision does not need. | **UNVERIFIED; primary not reachable.** The pointer is dropped, and every closure in this report is Zariski (§3.1). |
| R4 | B17 accepted results 01-A, 01-C, 03-A, 03-B, 03-C | §3, §4, §6 | **VERIFIED in tree**: `B15-11/docs/b17_11_report.md` claim table, together with `B15-01/docs/b17_01_report.md` (point `F*`, lines 163–190) and `B15-03/docs/b17_03_report.md` (Lemmas 1–2). |
| R5 | Standard facts: fibre-dimension theorem; lower semicontinuity of rank; `deg Z · deg(Y→Z) = deg Y` for a finite linear projection; Hilbert polynomial degree and leading coefficient; Weyl dimension formula; complete reducibility in characteristic zero | throughout | **Standard, cited by statement only.** No page locations are claimed. v1's specific locations (Mumford I.10 Cor. 1, Fulton Ex. 12.3.1) are **withdrawn as unverified pointers**. |

**Note on R1, the four-variable control.** Verbatim from v3:
- **Theorem 2.** "The family of determinantal quartic surfaces consists of 5 prime divisors F1, …, F5 ⊂ |O_P3(4)| … deg(F1) = 320112, deg(F2) = 136512, deg(F3) = 38475, deg(F4) = 320, deg(F5) = 2508."
- **Table 2, row F1.** `a = (5,5,5,5)`, `b = (6,6,6,6)`, `d_1 = 6`, `g_1 = 3`, discriminant 20. This is the admissible pair of a 4×4 matrix of linear forms, which Corollary 3.1's proof identifies as the linear determinantal case, of dimension `2d^2 + 1 = 33`.
- **Abstract.** The results concern **smooth** determinantal quartic surfaces.

How R1 is used here:
- It concerns **four variables**, surfaces in `P^3`. It does not settle `D45` and gives no five-row separator.
- It does not circumvent 03-C: every `lC` restriction to four variables already lies in the four-variable determinant closure (03-B).
- It is used only to show that the Bézout-type bound can exceed a known actual degree by many orders of magnitude (§3.6).
- The board quoted "Table 2 and Theorem 2": the degree is stated in Theorem 2, and Table 2 identifies F1 by its admissible pair. Both are confirmed.

## 8. One forward step: the degree-five, five-row, `a = 1` carrier family

This is the single forward step: one **named carrier family**, with the argument. It is not a separator, and no test was run on it.

### 8.1 Five-row cells cannot occur below degree five, and at degree five every one has `a = 1`

**Lemma 8.1 (PROVED).** If `S_lambda(C^5)` occurs in `Sym^d(Sym^4 C^5)`, then `ell(lambda) ≤ d`. Hence `d_5 ≥ 5`.

*Proof.* `Sym^d(Sym^4 V) ⊆ (Sym^4 V)^{⊗d}`. By Pieri's rule, tensoring with a one-row module adds at most one row. ∎

**Measurement 8.2 (MEASURED, exact).** Script: `analysis/b18_01_cell_sizes.py`, sha256 `23e0c076…1b82`. Output: `results/b18_01/cell_sizes.json`, sha256 `1bdd88be…825f`. It computes the exact weight multiplicities of `Sym^d(Sym^4 C^5)` in ordinary coefficients and extracts `a(d,lambda)` by the Weyl alternation.
- **Control.** `sum_lambda a · dim S_lambda(C^5) = binom(69+d, d)` for every `d ≤ 6`.
- **Cost.** One process, `timeout 60`, 0.3 s.
- **`d ≤ 4`.** No five-row cell, consistent with Lemma 8.1.
- **`d = 5`.** Exactly **23** five-row cells, and **all have `a = 1`**.
- **`d = 6`.** 105 five-row cells, of which 38 have `a = 1`; the largest `a` is 7.

The 23 degree-five cells, with `K(lambda)` = dimension of the weight-`lambda` space, i.e. the size of the linear problem that defines the highest-weight vector:

| `lambda` | `K` | `lambda` | `K` | `lambda` | `K` |
|---|---:|---|---:|---|---:|
| (12,2,2,2,2) | 553 | (9,6,2,2,1) | 1275 | (8,6,2,2,2) | 2972 |
| (9,7,2,1,1) | 621 | (7,7,4,1,1) | 1564 | (7,6,4,2,1) | 3260 |
| (11,4,2,2,1) | 705 | (8,5,5,1,1) | 1610 | (7,5,4,3,1) | 4807 |
| (10,5,3,1,1) | 774 | (10,4,2,2,2) | 1761 | (8,4,4,2,2) | 4988 |
| (10,5,2,2,1) | 1008 | (9,5,3,2,1) | 1860 | (7,4,4,4,1) | 5490 |
| (8,7,3,1,1) | 1091 | (9,4,4,2,1) | 2123 | (6,6,4,2,2) | 6869 |
| (9,5,4,1,1) | 1215 | (8,6,3,2,1) | 2261 | (6,4,4,4,2) | 11640 |
| | | (8,5,4,2,1) | 2825 | (4,4,4,4,4) | 19834 |

### 8.2 Why this family matters: in an `a = 1` cell, separation **is** a positive gap

**Proposition 8.3 (PROVED).** Let `a(d,lambda) = 1`, with `h_lambda` spanning `H_{d,lambda}`. The following are equivalent:
1. `K_det(d,lambda) ⊄ K_pad(d,lambda)`;
2. `i_det = 1` and `i_pad = 0`;
3. `D(d,lambda) = 1`.

*Proof.* Both kernels are subspaces of a line. `K_det ⊄ K_pad` holds iff `K_det` is the line and `K_pad = 0`, which is `D = i_det − i_pad = 1`. ∎

This is the only situation in the programme where the separation of Theorem 3.5 and a multiplicity gap coincide. The coincidence is **structural** (`a = 1`), not an inference from separation. At `d = 5` it holds in **every** five-row cell. So if `d_5 = 5`, the batch's stretch goal is met at degree 5.

### 8.3 The two certificates such a cell needs

1. **Certify `i_pad = 0`.** It suffices to find **one** point `P ∈ R135`, for example `F*` or any exact `lC`, with `h_lambda(P) ≠ 0`. An exact nonzero value at a point of `R135 = closure(rho_5 X_pad)` proves `m_pad ≥ 1 = a`. This is a sampled **nonzero**, the valid direction.
2. **Certify `i_det = 1`**, i.e. `h_lambda ∈ I(D45)`. Sampling cannot establish this: a sampled zero never gives `i ≥ 1`. Valid certificates:
   - (a) `m_det ≤ 0` from a global upper bound: symmetric `s(5,lambda) = 0`, or already ordinary `g((5^4),(5^4),lambda) = 0`, since `s ≤ g`.
   - (b) With `s ≥ 1`, a certified boundary rank `b = s` (Slot 03's object).
   - (c) An exact symbolic proof that `h_lambda∘phi ≡ 0`.

   Conversely, **one exact nonzero evaluation `h_lambda(phi(B)) ≠ 0` at an integer point kills the cell**: it proves `m_det = 1`, hence `i_det = 0`.

### 8.4 One member of the family is excluded outright

**Proposition 8.4 (PROVED).** In the cell `lambda = (4,4,4,4,4)`, `d = 5`, we have `i_pad = 1 = a`. So `D ≤ 0`, and the cell cannot separate.

*Proof.*
1. **The module.** `S_(4^5)(C^5) = det^4` is one-dimensional, so its only weight is `mu = (4,4,4,4,4)`. Every element of `R135` is `g·(x_0 C)` for some `g ∈ GL5`, and `h(g·F) = (g^{-1}·h)(F)`. So it suffices to show `h_lambda(x_0 C) = 0` for every cubic `C`.
2. **A destabilising torus.** Let `t` act by `x_0 ↦ t^4 x_0`, `x_j ↦ t^(−1) x_j` for `j = 1..4`, i.e. `r = (4,−1,−1,−1,−1)`. Then `c_alpha(t·F) = t^{<alpha,r>} c_alpha(F)`. Every monomial `x_0 x^beta` of `x_0 C` has `<e_0 + beta, r> = 1 + 5·beta_0 > 0`, so `t·(x_0 C) → 0` as `t → 0`.
3. **Scaling.** Since `h_lambda` has weight `mu` and degree `5 ≥ 1`, `h_lambda(t·F) = t^{<mu,r>} h_lambda(F)`, with `<mu,r> = 16 − 16 = 0`. So `h_lambda(x_0 C) = lim_{t→0} h_lambda(t·(x_0 C)) = h_lambda(0) = 0`. ∎

(Equivalently: `x_0 C` lies in the `SL5` null cone, and `h_(4^5)` is the degree-5 `SL5`-invariant.) The same destabilising 1-parameter subgroup gives a cheap **necessary** condition for `m_pad ≥ 1` in other cells. Beyond this one cell it is not developed here.

### 8.5 What still lacks a proof

**The missing step:** for the 22 remaining cells, there is **no** argument that `h_lambda ∈ I(D45)`, i.e. that `m_det(5,lambda) = 0`, in any of them. Equally, there is no argument that it fails.
- Theorem 3.5 gives only `d_5 ≤ 4^49`.
- Nothing proved here or in B17 makes `d_5 = 5` likely or unlikely.
- `dim D45 = 50` in `C^70` (codimension 20) constrains nothing at degree 5.

The family is a precisely posed test with a large payoff: if it succeeds it gives a positive gap. It is **not** evidence that one exists.

**Expected outcome of this report, restated:** no usable separating equation is produced. The family of §8 is a construction problem, not a result.

### 8.6 The one next test, and its price

**Test (bounded, two stages, not run).**
1. **Kronecker screen.** For the 22 cells, compute the ordinary coefficient `g((5^4),(5^4),lambda)` for `lambda ⊢ 20`. That needs characters of `S_20`, which has 627 conjugacy classes, via the Murnaghan–Nakayama rule. Controls:
   - `sum over lambda ⊢ 20 of g(mu,mu,lambda)·f^lambda = (f^mu)^2`, with `mu = (5^4)` and `f` the number of standard tableaux;
   - `g(mu,mu,(20)) = 1`.

   The inequality `m_det ≤ g` is v1 Claim 6.1, re-checked: `phi^*` lands in the `SL4 × SL4`-invariants of `Sym^{4d}(C^4 ⊗ C^4 ⊗ C^5)`, whose `S_lambda(C^5)`-multiplicity is `g((d^4),(d^4),lambda)`. Transposition invariance refines this to `m_det ≤ s ≤ g` (§6.3).
   - Any cell with `g = 0` has `m_det = 0` certified, since `s ≤ g`.
   - For cells with `g ≥ 1`, compute the transposition-symmetric `s` (Slot 02/06 conventions). `s = 0` also certifies.
2. **Padding and determinant evaluations**, only in cells certified in stage 1.
   - Construct `h_lambda` as the common kernel of the four raising operators `E_{i,i+1}` (ordinary rule) on the `K(lambda)`-dimensional weight space.
   - Evaluate it exactly at `F*` and at a few exact `lC`. **A nonzero value is a certified positive gap `D = 1` in that cell**, pending independent review.
   - Optionally, in cells that fail stage 1, evaluate `h_lambda` at one integer determinant point first. A nonzero value retires the cell for good.

**Price (estimated, not measured).**
- **Stage 1.** Character evaluation for 23 partitions over 627 classes. One process, well under the default 60 s / 512 MiB pilot. The symmetric `s` for surviving cells: minutes, one process.
- **Stage 2.** An exact kernel of about `4K × K` for `K ≤ 2000`, and one evaluation of a `K`-term polynomial in the 70 coefficients. Seconds per cell for the smallest cells, within the default pilot. The `K = 19834` cell is already excluded (Prop. 8.4). `K ≈ 5000–12000` needs sparse or modular-then-lift linear algebra: minutes and under 2 GiB, i.e. a small explicit lease. It is requested only if a large cell survives stage 1.
- **No incidence elimination and no degree-`4^49` computation.** Nothing in either stage is heavy.

What the outcomes mean:
- If stage 1 certifies no cell, the degree-five family is retired **for the Kronecker-bound certificate route only**. That is not a proof that `m_det(5,lambda) ≥ 1`, and not an exclusion of five rows.
- If a cell passes both stages, it goes to Slot 09 and Slot 10.

## 9. Claim ledger, honest negatives, resources

### 9.1 Claims in this revision

| # | Claim | Label |
|---|---|---|
| 3.2 | `dim D45 = 50`, `dim P(D45) = 49`. Upper bound by the `G`-action (orbits in fibres, generic orbit dimension ≥ 30); lower bound by `rank_Q J = 50` | **PROVED**. Certificate CERTIFIED by the integrator's independent reimplementation |
| A | point/variety separation in degree `≤ deg Y` | **PROVED** |
| B | `deg Y ≤ D^{dim Y}` for an image closure under degree-`D` forms; reducible-hypersurface gap of v1 repaired | **PROVED, conditional on refined Bézout** (R2: secondary quotation only, unverified against the primary) |
| 3.5 | Theorem: five-variable separator `h` with `deg h ≤ delta_45 ≤ 4^49`; a five-row cell with `K_det ⊄ K_pad` in that degree; `d_sep ≤ d_5 ≤ delta_45 ≤ 4^49` | **PROVED**, conditional as in B; consumes 01-A, 01-C, 03-A, 03-C and B17-03 Lemma 2; uses only the upper bound of 3.2 |
| 3.6 | the theorem is not a search budget, not an equation, and says nothing about `D` | stated limitations |
| 4.1 | `dim R135 = 39` | **PROVED** |
| 4.2 | for `d ≫ 0`, the `dim S_lambda(C^5)`-weighted sum of `D` over five-row cells is negative; `d_0` not effective | **PROVED (aggregate only)**; uses only the lower bound of 3.2 |
| 5.1 | `MN = F·I4` criterion | **WITHDRAWN**: counterexample `M = l·I4`, `N = C·I4` at `F = lC ∉ D45` |
| 5.2 | `I(D45) = ker phi^*` (elimination of the graph): enforces `det` exactly and contains all limits | **PROVED (standard)** |
| 6.3 | `m_det ≤ s ≤ g`; clipped `U = min(a,T)`, `B = min(a, s − b)` | **ADOPTED/re-checked** (v1 Claim 6.1 argument plus transposition) |
| 8.1 | `ell(lambda) ≤ d` in `Sym^d(Sym^4)`, so `d_5 ≥ 5` | **PROVED** |
| 8.2 | at `d = 5` there are exactly 23 five-row cells, all with `a = 1`; at `d = 6`, 105 cells (38 with `a = 1`) | **MEASURED** (exact; control passes) |
| 8.3 | if `a = 1`, then separation ⇔ `D = 1` | **PROVED** |
| 8.4 | `lambda = (4^5)`, `d = 5`: `i_pad = a`, so the cell cannot separate | **PROVED** |
| 8.5 | any degree-five cell has `m_det = 0` | **NOT REACHED** (the missing step) |
| — | an explicit separating equation; any positive `D` | **NOT REACHED** |
| R1 | LLV v3, Theorem 2 / Table 2 row F1, `deg F1 = 320112` (four-variable control) | **VERIFIED against primary** |

**Withdrawn from v1:**
- the `MN = F·I4` equivalence;
- "five rows is where `D` is most negative" and "wrong regime / wrong place";
- "most `U > B` screens must fail";
- "move the hunt to six or more rows";
- "the degree of `D45` is the only route" and "the degree must come from the determinant side";
- "the ruledness argument cannot yield a degree bound; effort there is misdirected";
- "(1) inclusion form and (2) certificate form are the same statement";
- calling the ordinary Kronecker bound "symmetric";
- the unclipped `U`;
- the unverified page pointers to Mumford I.10 and Fulton Ex. 12.3.1;
- the nonexistent `out/` scripts.

### 9.2 Honest negatives

1. **No separating equation, no named nonzero multiplicity, no gap.** The finite degree theorem is astronomically weak (`4^49`) and gives no construction.
2. **The aggregate inequality has no per-cell or strategic content.** It excludes no cell and recommends no length.
3. **The degree theorem leans on refined Bézout**, checked only through a secondary quotation. Without it, only "`d_5` finite" remains.
4. **The forward step is a posed test.** No argument makes any degree-five cell likely to carry a determinant equation.
5. **§8.6 prices are estimates, not measured feasibility.**

### 9.3 Resources and provenance of runs

| Run | Command | Wall time | Log (sha256) | Output (sha256) |
|---|---|---|---|---|
| rank certificate (previous session, accepted) | `timeout 60 python analysis/b18_01_rank_certificate.py` | 0.095 s | `results/logs/b18_01_rank_certificate_output.txt` (`e63962f0258b1f7d67da4d1f12d35a3c4428c7f2de107fb13f8ec87d237d6f38`) | `rank_certificate.json` (`53b665440623f70d533eabd114f550f8bac489ad5293d9afad6bb6f4726f1398`); `rank_certificate_matrices.json` (`5f39725c185d9500edf6b225780e32a631ea629e22edc58c06f534b834d4e8d5`); script `3e9d262f85e6c7950dad10fea3cf829d77f4afaf63171f58f57e679340c0c80f` |
| cell sizes (this session) | `timeout 60 python analysis/b18_01_cell_sizes.py 6` | 0.32 s | `results/logs/b18_01_cell_sizes_output.txt` (`618fcdd23254edef165d0efd18861591d46b1fc375ff5a40ff83266836622a0b`) | `cell_sizes.json` (`1bdd88bebee5627d76c39ac193d3204304b80e785f6bb2f2091fe8337911825f`); script `23e0c076b6d9b1c625075535ed894507629c51a28e2e902b9d1b099d350b1b82` |

Each run was one process, with `OMP_NUM_THREADS=1` and `OPENBLAS_NUM_THREADS=1`, under `timeout 60` and `ulimit -v 524288`. The shell accepted `ulimit -v`; whether it is enforced on a native Windows `python.exe` was **not** verified. No lease was requested or used, and no background process remains.

The cell-size pilot was needed only to price the forward step. It performs no determinant or padding evaluation.

**Literature files** in `results/b18_01/literature/`:
- `arXiv_2303.09028v3.pdf` (`67b1701f…4b22`) and `llv_v3.txt` (`3dcd9ce1…ded7`);
- `arXiv_1411.0777_latest.pdf`, which is v2 (`0741e2d2…4589`), and `ss.txt` (`47408e0e…c767`).

No git command was run in this session. §0 records the starting commit.
