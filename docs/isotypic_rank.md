# The isotypic rank lemma, and how far the determinant fills the ambient

Session 26 (2026-08-31), branch `s26-tworank`.
Pre-registration: `results/PREREG_s26.md` (committed before any computation).
Measured cells: `docs/live_cells.md`. Session record: `docs/session_26.md`.

Clone tip `3dfd524` — one commit *above* the `a3df8ba` the brief names, and not
a rollback: it is the integrator's own correction to the briefs, with `a3df8ba`,
`c9240f3`, `ad9502f` all present beneath it in the stated order.

---

## 0. What this document contains

1. The `a >= 2` generalisation of the paper's one-bit argument, proved, in a
   form with **no `S_lam` versus `S_lam^*` bookkeeping anywhere**.
2. A reduction that makes the whole question elementary: a highest-weight
   vector of weight of **length `r`** sees the orbit only through the `r`-ary
   cubic `det(s_1 A_1 + ... + s_r A_r)`.
3. The consequence: **`mult_lam C[closure(det_3)]_delta = a(lam,delta)` for
   every `lam` with `ell(lam) <= 4`, at every degree** — and the same for the
   permanent up to `ell(lam) <= 5`. Both bounds are sharp, and both are
   explained by one number: the dimension of the stabiliser.
4. The practical algorithm, and two independent implementations of it.

---

## 1. Conventions, fixed once

`V = C^9 = M_3(C)` with basis `e_1..e_9` (the matrix coordinates) and dual
basis `y_1..y_9` (the linear forms). `W = Sym^3 V^*` is the space of cubic
forms on `V`; `det_3 in W`; `G = GL(V)` acts by `(g.F)(v) = F(g^{-1} v)`.

`C[W]_delta = Sym^delta(W^*)` is the space of degree-`delta` polynomials in the
**coefficient functionals** `c_alpha`, where `alpha` runs over the exponent
vectors of degree 3 and `c_alpha(F)` is the coefficient of `y^alpha` in `F`.
Under the action above, `c_alpha` transforms exactly as `e^alpha in Sym^3 V`:

    weight(c_alpha) = alpha        (non-negative, |alpha| = 3)
    E_ij . c_alpha  = alpha_j c_{alpha - eps_j + eps_i},   extended as a derivation.

`a(lam,delta)` denotes the multiplicity of `S_lam` in `C[W]_delta`, i.e. the
plethysm coefficient of `h_delta[h_3]`.

**On the orientation.** Session 23's honest boundary flagged that its
`tau`-grading orientation had been pinned by consistency rather than by
tracking `V <-> V*` through Peter–Weyl. Here the same trap is avoided by
construction rather than by argument: the objects computed below are *explicit
polynomials in the `c_alpha`*, their torus weights are read off their monomials
directly, and they are *evaluated at explicit points of the orbit*. At no point
is `S_lam` or `S_lam^*` written down, so there is no dualisation to get wrong.
The only convention that enters is which Borel is called "raising" — and that
is pinned three ways, all of which would visibly fail under the opposite
choice:

- the multiset of weights `lam` for which the explicitly constructed
  highest-weight space is nonzero agrees with the plethysm `h_delta[h_3]`
  computed from symmetric functions, on all 322 weights of length `<= 4` with
  `delta <= 7`, and with `scripts/ambient_screen.py` on all 1190 weights with
  `delta <= 7` (this multiset is very asymmetric: at `delta = 2` it is exactly
  `{(6), (4,2)}`);
- the counts reproduce `m_det((2,2,2)) = 1` and the published `m_det` row sums
  `3, 11, 43` and supports `3, 10, 34`;
- the measured multiplicities reproduce the paper's published total-deficit
  sequence (§5).

## 2. The lemma

Let `X` be any `G`-stable closed cone in `W`, `I` its ideal, and `M_lam` the
`lam`-isotypic component of `C[W]_delta`, so `M_lam = S_lam (x) C^a` with `C^a`
the multiplicity space carrying the trivial action.

**Lemma 1.** `I ∩ M_lam = S_lam (x) U` for a subspace `U <= C^a`.
*Proof.* `I ∩ M_lam` is a `G`-submodule of an isotypic module; the submodules
of `S_lam (x) C^a` are exactly the `S_lam (x) U`. ∎

**Lemma 2 (the rank lemma).** Let `h_1..h_a` be a basis of the space of
highest-weight vectors of weight `lam` in `C[W]_delta`, and let
`x in X` have dense orbit. Then

    mult_lam C[X]_delta  =  a  −  dim { u in C^a : sum_k u_k h_k vanishes on G.x }.

*Proof.* Under `M_lam = S_lam (x) C^a` the highest-weight vectors are exactly
`v (x) u` with `v` the highest-weight vector of `S_lam`, so `sum_k u_k h_k`
*is* `v (x) u`. Since `v` generates `S_lam` under `G`, the `G`-module generated
by `v (x) u` is `S_lam (x) u`; and `I` is `G`-stable and closed, so
`v (x) u in I` iff `S_lam (x) u <= I` iff `sum_k u_k h_k` vanishes on the dense
orbit. Hence `U` is exactly the stated space, and
`mult = a − dim U` by Lemma 1. ∎

At `a = 1` this is "`h_1` does not vanish on the orbit", which is the paper's
one bit. At `a = 2` it is a rank: the two functionals are both dead
(`mult = 0`), proportional (`mult = 1`), or independent (`mult = 2`).

**The dual form** in the brief — `mult = dim span{phi_1..phi_a}` with
`ev_x|_{M_lam} = sum_k phi_k (x) e_k^*` — is the same statement transposed:
`phi_k(g v) = h_k(g^{-1} x)`. We use the form above because it never leaves
`C[W]`.

**Corollary (the practical matrix).** For any finite set `g_1..g_K`,

    rank [ h_k(g_j . x) ]_{k,j}  <=  mult_lam C[X]_delta ,

with equality for generic `g_j`, and certainly once the rank reaches `a`.
So the matrix rank is always a *rigorous lower bound*, and it is a proof of
equality whenever it attains `a`. **Every measurement reported in this session
attains `a`**, so no probabilistic step enters any conclusion: each is a
certificate that `a` specific polynomials are linearly independent, exhibited
by explicit integer points.

## 3. The short-weight reduction

This is what makes the cells computable by hand rather than by a general
algorithm, and it is where the session's leverage comes from.

**Lemma 3.** Let `h` be a weight vector in `C[W]_delta` of weight
`lam = (lam_1,...,lam_r,0,...,0)`. Then `h` involves only the coefficients
`c_alpha` with `alpha` supported on the first `r` coordinates; consequently

    h(F) = h( F|_L ),      L = span(e_1,...,e_r).

*Proof.* `C[W]_delta` is spanned by monomials in the `c_alpha`, whose weight is
the sum of the participating `alpha`s. Every `alpha` has **non-negative**
entries, so a monomial of weight `lam` with `lam_j = 0` for `j > r` cannot use
any `c_alpha` with `alpha_j > 0` for `j > r`. Setting the coordinates
`y_{r+1},...,y_9` to zero is exactly restriction to `L`. ∎

**Lemma 4 (the evaluation).** For `F = g.det_3` and `L` as above,

    F|_L (s_1,...,s_r) = det( s_1 A_1 + ... + s_r A_r ),   A_i = g^{-1} e_i,

and as `g` runs over `GL_9` the tuple `(A_1..A_r)` runs over all linearly
independent `r`-tuples of `3x3` matrices — a dense subset of `(M_3)^r`.

Combining Lemmas 2–4:

> **Proposition 5.** For `ell(lam) = r`,
>
>     mult_lam C[closure(GL_9 . f_3)]_delta
>         =  mult of S_lam(C^r) in C[D_r^f]_delta ,
>
> where `D_r^f = closure{ f(s_1 A_1 + ... + s_r A_r) } ⊆ Sym^3 C^r` is the
> variety of `r`-ary cubics that admit a `3x3` linear representation by `f`.

The whole length-`r` stratum of the determinant's closure ring **is** the
coordinate ring of the determinantal `r`-ary cubics. In particular, if
`D_r^f` is everything, the ideal has no length-`r` part at any degree.

## 4. Where `D_r` is everything

**`r = 2`, exactly.** Every binary cubic over `C` factors as
`prod_{i=1}^3 (alpha_i s + beta_i t) = det(s D_alpha + t D_beta)` with `D`
diagonal — and `per` of a diagonal matrix is its determinant, so the same
tuple works for the permanent. So `D_2^det = D_2^per = Sym^3 C^2`, with no
computation at all.

**`r = 3, 4`, classically.** Every plane cubic has a `3x3` linear determinantal
representation (Dickson), and every smooth cubic surface has one (Grassmann;
72 inequivalent ones).

**The count that says where it must stop.** The map
`(A_1..A_r) -> det(sum s_i A_i)` is invariant under
`(P,Q).A_i = P A_i Q` with `det P det Q = 1`; that group has dimension 17 and
its scalar subgroup `(mu I, mu^{-1} I)` acts trivially, so the **effective**
group has dimension **16 = dim Stab(det_3)**.

> **Lemma 5b (the stabiliser of a generic tuple).** For `r >= 3` the stabiliser
> of a generic `r`-tuple in the effective group is finite, so the orbit is
> 16-dimensional and
>
>     dim D_r^det  <=  min( C(r+2,3),  9r − 16 )        (r >= 3).
>
> *Proof.* A generic tuple has `A_1` invertible; replacing each `A_i` by
> `A_1^{-1} A_i` we may take `A_1 = I`. If `(P,Q)` stabilises the tuple then
> `P A_1 Q = A_1` gives `Q = P^{-1}`, and `P A_i P^{-1} = A_i` for `i >= 2`, so
> `P` lies in the commutant of `{A_2, ..., A_r}`. For `r >= 3` two generic
> `3x3` matrices generate `M_3` as an algebra, so that commutant is the
> scalars and the stabiliser is finite. ∎
>
> **The hypothesis `r >= 3` is necessary.** At `r = 2` the commutant of a
> single generic matrix is 3-dimensional (2 dimensions modulo scalars), so the
> orbit is 14-dimensional, not 16, and the correct bound is `18 − 14 = 4` —
> which is the measured rank in the table below, and consistent with the
> elementary proof just given that `D_2` is *everything*. Stating the bound
> without the hypothesis would read `dim D_2 <= 2` and contradict this section
> two paragraphs later. (Error found by the integrator, `docs/s26_review.md`
> §2; recorded here rather than quietly patched. No conclusion changes: every
> use of the bound is at `r >= 3`, and `r = 2` is proved directly.)

For the permanent the effective group is the monomial one, of dimension
`2n − 2 = 4`, giving `dim D_r^per <= min( C(r+2,3), 9r − 4 )` under the same
`r >= 3` hypothesis (there the commutant argument is replaced by the diagonal
one, but the exception at `r = 2` is the same in kind).

**Measured (`analysis/wk6_s26_density.py`, exact integer rank of the
differential at random points, two independent arithmetic routes):**

| r | 9r | `rank d(det)` | `rank d(per)` | target `C(r+2,3)` | det dense? | per dense? |
|---|---|---|---|---|---|---|
| 2 | 18 | 4  | 4  | 4  | **yes** | **yes** |
| 3 | 27 | 10 | 10 | 10 | **yes** | **yes** |
| 4 | 36 | 20 | 20 | 20 | **yes** | **yes** |
| 5 | 45 | **29** | 35 | 35 | no | **yes** |
| 6 | 54 | **38** | **50** | 56 | no | no |

The two rank deficiencies are *exactly* the two stabiliser dimensions:
`29 = 45 − 16`, `38 = 54 − 16`, `50 = 54 − 4`. The naive count is attained with
no extra degeneracy, in both worlds and at every `r` past the crossover. So:

> **Theorem 6.** For every `delta` and every `lam` with `ell(lam) <= 4`,
>
>     mult_lam C[closure(GL_9 . det_3)]_delta  =  a(lam, delta),
>     def_det(lam, delta)                      =  m_det(lam) − a(lam, delta).
>
> For every `delta` and every `lam` with `ell(lam) <= 5`, the same holds for
> `per_3`. Both length bounds are sharp: `D_5^det` has codimension 6 in
> `Sym^3 C^5` and `D_6^per` has codimension 6 in `Sym^3 C^6`.

**Corollary 7.** `a(lam,delta) <= m_det(lam)` for every `lam` of length `<= 4`,
and `a(lam,delta) <= m_per(lam)` for every `lam` of length `<= 5` — because
`mult <= min(m, a)` always. This is a statement about a plethysm coefficient
and a symmetric rectangular Kronecker coefficient with no geometry in it, and
it was pre-registered as the sharpest falsifier of Theorem 6. It holds on all
172 weights of length `<= 4` with `a > 0` and `delta <= 7`, and is **tight
(`a = m_det`) at 59 of them** — including both two-row cells of this session.

**Theorem 6' (general `n`, measured the same way).** The reduction is not
special to `n = 3`: for `f = det_n` or `per_n`, a weight of length `r` sees only
`f(s_1 A_1 + ... + s_r A_r)`, an `r`-ary form of degree `n`, and the crossover is
again where `n^2 r − dim Stab(f)` falls below `C(r+n-1, n)`. Exact Jacobian
ranks (`analysis/wk6_s26_density.py::crossover_table`, whose `n = 3` row
reproduces the table above from independent general-`n` code):

| `n` | `det_n` dense up to | `per_n` dense up to | first deficient rank (det) | target |
|---|---|---|---|---|
| 2 | `r = 4` | `r = 4` | 14 at `r = 5` | 15 |
| 3 | `r = 4` | **`r = 5`** | 29 at `r = 5` | 35 |
| 4 | **`r = 3`** | **`r = 5`** | 34 at `r = 4` | 35 |

Every deficient rank is exactly `n^2 r − dim Stab(f)`: `14 = 20 − 6`,
`29 = 45 − 16`, `34 = 64 − 30`, and on the permanent side `50 = 54 − 4`,
`90 = 96 − 6`. (At `n = 2`, `per_2` is linearly equivalent to `det_2`, so its
stabiliser is the 6-dimensional one and the two columns must agree — they do,
which is a free consistency check on the general-`n` code.) The `n = 4`,
`r = 4` entry is the classical fact that a *general* quartic surface is **not**
determinantal, recovered here as a rank deficiency of exactly 1.

So the picture inverts with `n`: at `n = 3` the determinant covers lengths
`<= 4` and the permanent `<= 5`; at `n = 4` the determinant covers only
`<= 3` while the permanent still covers `<= 5`. **At `n = 4`, lengths 4 and 5
are weights where the determinant's ideal is live and the permanent's is
provably empty** — the first weights where the two closure rings can differ for
a structural reason rather than an arithmetic one.

**Corollary 8 (the reason the determinant fills so much).** The determinant
fills the ambient at short weights not because its ring is large but because
its stabiliser is: 16 dimensions of symmetry are 16 dimensions the map
`(A_i) -> det(sum s_i A_i)` cannot use, and the first length at which that
matters is `r = 5`. The permanent, whose stabiliser is only 4-dimensional,
stays surjective one length longer. **The crossover length is a function of the
stabiliser dimension alone.**

## 5. What the paper's published numbers then say

`mult <= min(m_det, a)` gives `total_def(delta) >= sum_lam (m_det − min(m_det,a))`,
with equality iff `mult = min(m_det,a)` at every weight. Computing both sides
exactly (`analysis/wk6_s26_sweep.py`):

| delta | `sum m_det` | `sum a` | `sum m_det − sum a` | published total deficit |
|---|---|---|---|---|
| 2 | 3    | 2   | 1    | 1 |
| 3 | 11   | 5   | 6    | 6 |
| 4 | 43   | 12  | 31   | 31 |
| 5 | 170  | 29  | 141  | 141 |
| 6 | 697  | 79  | 618  | 618 |
| 7 | 2713 | 225 | 2488 | 2488 |

`a <= m_det` at **every** weight in this range, not only the short ones, and
the two columns agree at all six degrees. Since `mult <= a`, equality of the
totals forces `mult = a` at every single weight with `delta <= 7`:

> **Corollary 9.** The ideal of `closure(GL_9 . det_3)` has **no isotypic
> component at all in degrees `<= 7`** — it is zero there. This extends the
> paper's "the degree-`<= 4` part of the ideal is zero" by three degrees.

Theorem 6 proves the length-`<= 4` part of this outright, with no appeal to the
published totals. The length-`>= 5` weights were then measured directly by the
rank algorithm (§6), which confirms the same conclusion independently of the
published sequence wherever it reaches: all of `delta <= 5`, 62 of the 79 units
of ambient room at `delta = 6`, and 104 of 225 at `delta = 7`, with a further 1
and 25 units covered by Theorem 6. The remainder — 16 units at `delta = 6` and
96 at `delta = 7`, all at weights of length `>= 5` whose weight space exceeded
the computational cap — is carried by the published sequence rather than
re-derived, and is pure compute rather than new mathematics. Nothing measured
or proved disagrees. See `docs/live_cells.md` for the degree-by-degree ledger.

## 6. The algorithm, and the two implementations

Fix `lam` of length `r` and degree `delta`.

1. Enumerate the degree-`delta` monomials in the `c_alpha` (`alpha` of degree 3
   in `r` variables) of weight exactly `lam` — directly, never by filtering.
2. Build `R`, the matrix of the raising operators `E_{i,i+1}` restricted to
   that weight space. Then `a = dim ker R`.
3. Pick random integer tuples `(A_1..A_r)`, form the cubic
   `det(sum s_i A_i)` exactly, and read off its coefficients `c_alpha`.
   Build the evaluation matrix `E` on the same monomial basis.
4. `mult = rank([R;E]) − rank(R)`.

Step 4 is the rank lemma with the kernel eliminated: the multiplicity is the
codimension, inside `ker R`, of `ker R ∩ ker E`.

**Two implementations, used against each other on every reported number.**
Route A forms an explicit integer basis of `ker R` and takes the rank of
`[h_k(point_j)]` over `Q` *and* modulo `2^61 − 1`. Route B never forms a kernel
and takes `rank([R;E]) − rank(R)` modulo two different primes (and over `Q`
where the weight space is small enough). They agree on every cell.

**Calibration, run before any new cell was measured** (this is the brief's kill
criterion 2): at every weight with `a > 0` and `delta <= 4` — 20 of them, all
lengths — the algorithm returns `mult = a`, which is what the paper's
`1, 6, 31` row requires. The criterion did not fire.

## 7. Honest boundary

- **Lemmas 1–5 and Corollaries 7–9 are proved.** Lemma 3's non-negativity
  argument and Lemma 4's identification are elementary and complete.
- **Theorem 6 rests on the density of `D_r`**, which is (i) an exact elementary
  argument at `r = 2`, (ii) classical at `r = 3, 4`, and (iii) confirmed here
  by an exact Jacobian rank at a random integer point. A Jacobian rank at one
  point is a *proof* of dominance (rank is lower semicontinuous, so a full rank
  somewhere is full rank generically) — so (iii) is rigorous. The *non*-density
  at `r = 5, 6` is likewise rigorous in the direction that matters: the rank is
  bounded above by `9r − 16` for every point by the group action, and the
  measured rank attains that bound.
- **What is not proved** is that the ideal actually *does* bite at length 5 —
  only that the argument for `mult = a` stops there. `D_5^det` has codimension
  6, so its ideal is certainly nonzero; whether any of its generators sits in a
  `GL_5`-isotypic component reachable at small `delta` is a separate question,
  and §5 shows it does not happen at `delta <= 7`.
- Corollary 9 for lengths `>= 5` is a *measurement* (rank attaining `a`), not a
  structural theorem; it is certified in the strong sense of §2, but only at
  the degrees actually swept.
