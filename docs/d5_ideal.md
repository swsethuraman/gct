# `D_5`, and the sharpness of the length theorem

Session 28 (2026-08-31/09-01), branch `s28-d5`.
Pre-registration: `results/PREREG_s28.md` (committed before any computation).
Record: `docs/session_28.md`. Corrected lemma: `docs/isotypic_rank.md` §4.

Clone tip `1203fe4`; ancestry check passed (`6aaab97` is an ancestor).
Calibration (`analysis/wk6_s26_regress.py`) passed in this container first.

---

## 0. The result

> **Theorem 6 is sharp.** The ideal of `closure(GL_9 . det_3)` *does* contain a
> highest-weight vector of length 5, so the hypothesis `ell(lam) <= 4` cannot be
> weakened. The witness is explicit and elementary: **the discriminant of
> quinary cubics**, of degree 80 and weight `(48^5)`.

What is **not** determined is the *smallest* degree at which a length-5 weight
has `mult < a`. Writing `delta_0` for it:

    6  <=  delta_0  <=  80          (unconditionally)
    8  <=  delta_0  <=  80          (given the paper's published deficit sequence)

Per the brief's kill criterion 1, this is reported as a range, not as an
attained bound. The lower end is where measurement stopped, not where the
phenomenon starts.

One genuinely new thing did turn up in the search, at a different length:

> **From degree 10 the ideal is provably nonzero, at weights of length 8 and 9.**
> At `delta = 10`, three weights have `a = 1` and `m_det = 0`:
> `(13,3,2,2,2,2,2,2,2)`, `(12,5,2,2,2,2,2,2,1)`, `(9,9,2,2,2,2,2,2)`.
> Since `mult <= m_det`, the whole isotypic component lies in the ideal. This is
> the first degree at which any part of the ideal is pinned down exactly, and it
> is by the cheapest possible mechanism — the orbit simply has no functions of
> that weight. **The deficit there is `0`, not full**: `def = m − mult = 0 − 0`.
> So it is an ideal element that carries no deficit, which is worth keeping
> distinct from the length-5 phenomenon the session was after.
> (Verified two ways: my routines and `scripts/ambient_screen.py` agree on both
> `a` and `m_det` at each.)

---

## 1. What `D_5` is

`D_5 = closure{ det(s_1 A_1 + ... + s_5 A_5) : A_i in M_3 } ⊆ Sym^3 C^5`: the
quinary cubics admitting a `3x3` linear determinantal representation —
equivalently, the linear pullbacks of `det_3` along `C^5 -> M_3`, equivalently
the restriction of `closure(GL_9 . det_3)` to a fixed 5-plane. Dimension
`45 − 16 = 29` in a 35-dimensional space, codimension 6.

**Literature pass (done before computing, as the brief requires).** The variety
is classical; the ideal, in the `GL_5`-graded form this programme needs, does
not appear to be.

- **Beauville, *Determinantal hypersurfaces* (Michigan Math. J. 48, 2000):** the
  generic hypersurface of degree `d` in `P^n` is expressible as a linear
  determinant **only if `n = 2`, or `n = 3` and `d <= 3`.** For cubics that is
  exactly `r <= 4` — *Theorem 6's length bound is Beauville's theorem*, and the
  crossover session 26 measured as a Jacobian rank is a classical statement.
  This is worth having: the paper can cite rather than measure.
- **Determinantal representations of singular hypersurfaces** (arXiv:0906.3012):
  in higher dimensions determinantal hypersurfaces are *necessarily singular*,
  with singular locus of dimension at least `n − 4`. For `n = 4` that is
  isolated singular points — which is what §2 exhibits.
- No published generating set for `I(D_5)` was found. **P3 as predicted:
  classical as a variety, not as an ideal.**

## 2. Why the ideal is nonzero, with an explicit element

**Lemma.** Every member of `D_5` is a *singular* quinary cubic.

*Proof.* The rank-`<=1` locus of `M_3` is the affine cone over the Segre
`P^2 x P^2 ⊂ P^8`, of dimension 4. A pencil `s -> M(s) = sum s_i A_i` in five
variables spans a linear `P^4 ⊂ P^8`. Since `4 + 4 >= 8`, the projective
dimension theorem forces the two to meet: there is `s != 0` with
`rank M(s) <= 1`. At such a point every `2x2` minor of `M(s)` vanishes, hence
every cofactor, hence — since `dF/ds_k = tr(adj M(s) . A_k)` — every partial
derivative of `F = det M`. So `F` is singular at `s`. ∎

(By Giambelli the intersection has degree 6, so the generic member has **six**
nodes, and codimension 6 in `Sym^3 C^5` is the codimension of the six-nodal
locus — the two 6's match, and that is the geometric content of
`dim D_5 = 29`.)

**Corollary.** `disc ∈ I(D_5)`, where `disc` is the discriminant of quinary
cubics: irreducible of degree `n(d−1)^{n−1} = 5 · 2^4 = 80` in the 35
coefficients, and a `GL_5` semi-invariant. Its weight is forced by degree:
total weight `3 · 80 = 240` spread equally over five rows, so
`lam = (48,48,48,48,48)` — **length exactly 5**, as `I(D_5)` must be
(§3 below). Hence `mult_{(48^5)} < a((48^5), 80)`, and Theorem 6's length bound
is sharp.

**Verification** (`analysis/wk7_s28_sing.py`, verification of a proof, not a
substitute for it): at six random integer pencils, Newton on the nine `2x2`
minors finds an explicit rank-1 point in every case — singular values
`(x, 0, 0)` — and the cubic's gradient there is zero to `1e-14`.

**The same count explains `r = 4`.** A generic `P^3 ⊂ P^8` *misses* a
codimension-4 subvariety. That is why smooth determinantal cubic surfaces exist
and smooth determinantal cubic threefolds do not, and it recovers Beauville's
dichotomy as one dimension count. The Jacobian ranks session 26 measured —
`20 = 20` at `r = 4`, `29 < 35` at `r = 5` — are the algebraic shadow of it.

## 3. Why `I(D_5)` lives only at length 5

A highest-weight vector of weight `mu` with `ell(mu) = k` inside
`C[Sym^3 C^5]_delta` involves only coefficients supported on `k` of the five
variables (the non-negativity argument of Lemma 3, applied inside 5 variables),
so it sees a point of `D_5` only through its restriction to a `k`-plane — and
that restriction ranges over `D_k`, which is *everything* for `k <= 4`. So no
such vector vanishes on `D_5`:

> **`I(D_5)` is concentrated at weights of length exactly 5.**

This is why tasks B and C of the brief are the same computation, and why the
discriminant — a length-5 weight — is a legitimate witness rather than an
accident of one degree.

## 4. Where the search actually got to

**The arithmetic route.** `mult <= min(a, m_det)`, so `a > m_det` at a weight
*proves* `mult < a` with no geometry. Sweeping all weights of length `>= 5`:

| `delta` | weights with `a > 0`, length 5–9 | `a > m_det` | ties `a = m_det` |
|---|---|---|---|
| 5 | 3 | 0 | 0 |
| 6 | 20 | 0 | 0 |
| 7 | 81 | 0 | 0 |
| 8 | 246 | 0 | 1 |
| 9 | 620 | 0 | 4 |
| 10 | 1426 | **3** (lengths 8, 9, 9) | 16 |

So the arithmetic route never fires at length 5 in this range, and when it does
fire at `delta = 10` it is at lengths 8 and 9 and by the degenerate mechanism
`m_det = 0`.

**Direct measurement** (the session-26 rank algorithm, `r = 5..9`, exact,
two primes, with the `rank(R) = N_S − a` self-check passing every time):

| `delta` | length-`>=5` weights measured | units of `a` measured / total | result |
|---|---|---|---|
| 5 | 3 of 3 | 3 / 3 | `mult = a` everywhere |
| 6 | 17 of 20 | 17 / 20 | `mult = a` everywhere |
| 7 | 16 of 81 | 19 / 99 | `mult = a` everywhere |
| 8–10 | none affordable | 0 | — |

Every measurement attained `a`, which is a *certificate*: the rank is a rigorous
lower bound for `mult`, and `mult <= a`, so attaining `a` proves equality.
**Nothing measured anywhere in this session contradicts `mult = a` at length 5.**

## 5. Honest boundary

- **Proved outright:** the singularity lemma of §2 and its corollary
  `disc ∈ I(D_5)`; the length-5 concentration of §3; the corrected `r >= 3`
  stabiliser bound (`docs/isotypic_rank.md`, Lemma 5b). Together these make
  **Theorem 6 sharp**, which was the session's object.
- **Proved by certificate:** every `mult = a` in §4 (rank attains `a`).
- **Proved arithmetically:** the three `delta = 10` ideal components at lengths
  8 and 9 (`mult <= m_det = 0 < a = 1`), verified by two independent routes.
- **NOT determined:** `delta_0`, the smallest degree at which a length-5 weight
  has `mult < a`. The bracket is `6 <= delta_0 <= 80` unconditionally,
  `8 <= delta_0 <= 80` given the published deficit sequence. The upper end comes
  from one explicit equation and is certainly not tight — a codimension-6
  variety has six generators' worth of ideal and the discriminant is only the
  one that is easy to name. **I am not reporting 80 as the answer.**
- **NOT closed:** the ledger residue. `delta = 6` is down from 16 unmeasured
  units of ambient room to **3** (the three weights with `N_S` = 3988, 4028,
  4456); `delta = 7` is down from 96 to **80**. A blocked BLAS-based modular
  elimination was written to clear these, failed its own self-test twice, and
  was cut rather than shipped — see `docs/session_28.md` §5. So Corollary 9
  still leans on the published sequence at those weights, less than before.

## 6. What would settle `delta_0`

1. **Find a lower-degree element of `I(D_5)` by hand.** The six nodes are six
   conditions; the discriminant is the trace of just one of them. A
   `GL_5`-covariant vanishing on six-nodal cubics, of degree well below 80, is
   the natural object and would collapse the bracket immediately.
2. **Compute `I(D_5)` degree by degree at length-5 weights from `delta = 8`.**
   Feasible once the elimination is fast enough — the weight spaces at the
   cheap length-5 weights are only a few hundred to a few thousand columns, and
   the wall is entirely the `O(N^3)` scalar elimination, not the mathematics.
3. **The invariant-theoretic route.** `C[D_5]` is the subring of the
   `SL_3 x SL_3` semi-invariants of `(M_3)^5` generated in degree 1;
   `delta_0` is the first degree in which that subring is a proper subspace.
   Semi-invariants of quivers have combinatorial descriptions that this
   programme has not yet used.
