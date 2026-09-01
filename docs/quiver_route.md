# The quiver route to `delta_0`: what it gives, and what it cannot

Session 31 (2026-09-01), branch `s31-quiver`.
Pre-registration: `results/PREREG_s31.md` (committed before any computation).
Record: `docs/session_31.md`.

Clone tip `1203fe4`; ancestry check passed. **Session 28's branch `s28-d5` is
not merged**, so its files are absent from `main` and everything cited from it
below is restated rather than assumed.

---

## 0. Verdict

**The route works, the dictionary is exact, and the answer is that this route
cannot find `delta_0`.**

- `SI_{(1,1)}` **is** exactly 35-dimensional and equals `Sym^3 C^5`: the
  coefficients of `det(sum s_k A_k)` are *all* the semi-invariants of that
  weight. Proved, then confirmed numerically. (Integrator's prior: correct.)
- The transpose-refined semi-invariant count **is** session 26's `m_det`. So the
  quiver picture re-derives `mult <= m_det`; it does not sharpen it. Everything
  the route can say pointwise, the programme already had.
- The one new thing it offers — a **dimension crossover** forcing a kernel —
  lands at `delta ~ 145` (`~ 120` for the transpose-refined version), i.e. **far
  above the discriminant's 80**. So it does not improve session 28's upper
  bound. Pre-registered prediction P3 (`delta_x in [25,60]`) is **refuted**.
- What that *means* is the useful part: `I(D_5)` is nonzero at degree 80 while
  dimensions do not force anything until roughly 145. **`delta_0` is a genuinely
  geometric quantity here, not an arithmetic one**, and no counting argument of
  this shape will reach it.

## 1. The dictionary

`Rep(K_5,(3,3)) = (M_3)^5`, `GL_3 x GL_3` acting by `A_k -> P A_k Q`. Because
`det(P A Q) = det P . det Q . det A`, each coefficient `c_alpha` of
`det(sum s_k A_k)` is a semi-invariant of weight `(det_P, det_Q)`; write
`SI_{(d,d)}` for the weight-`(det^d, det^d)` part, automatically homogeneous of
degree `3d`.

**(D1)** By Cauchy in the arrow slot and Kronecker in the two matrix slots,

    Sym^{3d}(C^5 (x) C^3 (x) C^3) = sum_{lam |- 3d} S_lam(C^5) (x) S_lam(C^9),
    S_lam(C^3 (x) C^3)            = sum_{mu,nu} g(lam,mu,nu) S_mu (x) S_nu,

and the `(det^d, det^d)` part selects `mu = nu = (d^3)`:

> **`SI_{(d,d)} = sum_{lam |- 3d, ell(lam) <= 5} g(lam,(d^3),(d^3)) . S_lam(C^5)`.**

**(D2) `SI_{(1,1)} = Sym^3 C^5`, dimension 35.** `chi^{(1,1,1)}` is the sign
character, so `chi^{(1^3)} . chi^{(1^3)} = chi^{(3)}` and
`g(lam,(1^3),(1^3)) = [lam = (3)]`. Hence `SI_{(1,1)} = S_{(3)}(C^5)`, of
dimension `C(7,3) = 35`. **The `c_alpha` span all of it** — there is no
semi-invariant of that weight beyond the coefficients of the pencil
determinant. Confirmed by both computational routes below.

**(D3) The transpose.** `tau : A_k -> A_k^T` commutes with the `GL_5`-action and
fixes `det(sum s_k A_k)`, so `C[D_5] ⊆ SI^tau`, and since
`m_det(lam) = dim (S_lam(C^9))^{H}` with `H = H^0 |x <tau>` while
`dim (S_lam)^{H^0} = g(lam, rect, rect)`,

> **`dim SI^tau_{(d,d)} = sum_{ell(lam) <= 5} m_det(lam) . dim S_lam(C^5)`.**

So `mult <= m_det` *is* the quiver bound. The route explains where session 26's
Peter–Weyl count comes from; it does not beat it.

**(D4) Kernel versus cokernel — the bookkeeping, written before computing.**
For the map `Sym^d(SI_1) -> SI^tau_{(d,d)}`:

- the **kernel** is `I(D_5)_d`. This is what `delta_0` is about.
- the **cokernel** is new generators of `SI^tau`. Irrelevant to `delta_0`.

They are independent and both are nonzero. Reading one as evidence about the
other is the slip this document exists to prevent.

## 2. Two independent routes, cross-checked

**Route (i), Kronecker:** the sums in (D1)/(D3), using session 26's exact
`m_det` machinery and the Weyl dimension formula for `dim S_lam(C^5)`.

**Route (ii), Molien/Kostant:** `dim SI_{(d,d)}` is the multiplicity of
`(d^3) (x) (d^3)`, so by Kostant's alternating sum over `S_3 x S_3`,

    dim SI_{(d,d)} = sum_{u,v in S_3} sgn(uv) . N(d.1+rho−u.rho, d.1+rho−v.rho),

with `N(r,c)` the number of degree-`3d` monomials in the 45 variables having
row-marginals `r` and column-marginals `c`. Only the summed `3x3` exponent
matrix `E` matters and each entry splits among the five arrows in `C(E_ij+4,4)`
ways, so `N(r,c) = sum_E prod_ij C(E_ij+4,4)` over `3x3` non-negative `E` with
those margins — a weighted contingency count.

The routes share no code and no identity. **They agree exactly at every
`delta <= 6`** (brief kill criterion 2 does not fire):

| `d` | `dim Sym^d(SI_1)` | `dim SI_{(d,d)}` (Molien) | (Kronecker) | `dim SI^tau_{(d,d)}` |
|---|---|---|---|---|
| 1 | 35 | 35 | 35 | 35 |
| 2 | 630 | 750 | 750 | 680 |
| 3 | 7 770 | 12 125 | 12 125 | 9 570 |
| 4 | 73 815 | 156 080 | 156 080 | 108 130 |
| 5 | 575 757 | 1 645 456 | 1 645 456 | 1 029 330 |
| 6 | 3 838 380 | 14 550 180 | 14 550 180 | 8 463 645 |

**Consistency with what is certified** (kill criterion 1): at all **68**
length-5 weights with `a > 0` and `delta <= 7`, `a <= m_det <= g` holds with no
exception — so the quiver bound is compatible with the measured, certified
`mult = a` at every one of them.

## 3. The first new generator of `SI^tau` is at `delta = 2`, and it is `S_{(2,2,2)}`

At `delta = 2`: `dim Sym^2(SI_1) = 630`, `dim SI^tau_{(2,2)} = 680`, and
`dim S_{(2,2,2)}(C^5) = 50` **exactly**. Since
`Sym^2(Sym^3 C^5) = S_{(6)} + S_{(4,2)}` contains no `S_{(2,2,2)}` while
`m_det((2,2,2)) = 1`, the cokernel is exactly one copy of `S_{(2,2,2)}(C^5)`,
and `630 = 680 − 50` says the map is **injective** there.

> **`SI^tau` is not generated in degree 1; the first new generator sits at
> `delta = 2`, in one copy of `S_{(2,2,2)}(C^5)`.**

This is pre-registered prediction P2, confirmed on the nose. It is also the
cleanest possible illustration of (D4): a cokernel at `delta = 2` with no kernel
anywhere near. `C[D_5]` is a *proper* subring of `SI^tau`, and it is proper for
reasons that have nothing to do with `I(D_5)`.

## 4. The crossover — where the route was supposed to pay, and does not

Since the image of `Sym^d(SI_1)` lies in `SI^tau ⊆ SI`,

    dim Sym^d(SI_1) > dim SI_{(d,d)}   ==>   I(D_5)_d != 0,

and the kernel is at a length-5 weight (a length-`<= 4` highest-weight vector in
5 variables sees only 4 variables, where `D_4` is everything). The source grows
like `d^34/34!`; `SI` is the graded piece of a 29-dimensional ring, so it grows
like `c . d^28`. The crossover exists — the question is where.

| `d` | 6 | 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 100 |
|---|---|---|---|---|---|---|---|---|---|---|
| `dim SI / dim Sym^d(SI_1)` | 3.79 | 9.14 | 24.34 | **29.48** | 26.44 | 20.87 | 15.58 | 11.36 | 8.24 | 4.38 |

The ratio **peaks near `d = 30` at about 29.5** and then falls at a steady
`~0.73` per ten degrees. Extrapolating that decay puts the crossover at

    d_x  ~  145        (for SI)
    d_x  ~  120        (for SI^tau, whose share of SI runs 0.91, 0.79, 0.69,
                        0.63, 0.58, ... and tends to about 0.5)

Either way: **the crossover is far above 80**, so the dimension route does not
even reach session 28's discriminant bound, let alone beat it. **P3 is refuted**
— it predicted `[25,60]` with a point estimate of 35.

**The negative is informative, and this is the session's real content.**
`I(D_5)` already contains an explicit element at degree 80 (the discriminant of
quinary cubics, of weight `(48^5)`), while *counting* does not force any element
until roughly 145. The ideal appears at least 65 degrees before dimensions
require it. So `delta_0` is not accessible to any argument of this shape, and
the search for it has to be geometric: an explicit low-degree covariant
vanishing on determinantal quinary cubics, not a dimension count.

## 5. The six-nodal identification (task D)

**Proposition.** `D_5` is an irreducible component of the closure of the locus
of six-nodal quinary cubics.

*Proof.* `D_5` is the image of the irreducible variety `(M_3)^5`, hence
irreducible, of dimension `45 − 16 = 29`. Its generic member is six-nodal: a
generic pencil spans a `P^4 ⊂ P^8` meeting the rank-one Segre `P^2 x P^2` (of
dimension 4 and degree 6) transversally in six reduced points, at each of which
every `2x2` minor, hence every cofactor, hence every partial of `det` vanishes;
and the singularity is a node for generic `A` (the Hessian at the rank-one point
`u v^T` is the quadratic form `s -> v^T adj(M(s)) u`). Imposing a node at an
unspecified point costs `5 − 4 = 1` condition, so the six-nodal locus has
dimension `35 − 6 = 29` as well. An irreducible 29-dimensional subvariety of a
29-dimensional locus is a component. ∎

**Equality is open**, and would need the six-nodal locus to be irreducible.
Predicted true (P5), not proved. If it *is* true, `I(D_5)` is the ideal of
six-nodal quinary cubics and `delta_0` becomes a question about multi-node
discriminants, where there is classical literature (GKZ) — that is the most
promising route the session can point at.

## 6. Honest boundary

- **Proved outright:** (D1)–(D4); `SI_{(1,1)} = Sym^3 C^5` of dimension 35; the
  identification `dim SI^tau = sum m_det . dim S_lam`; the `delta = 2` cokernel
  being exactly one `S_{(2,2,2)}`; the six-nodal component statement of §5.
- **Computed exactly, two independent routes agreeing:** the `SI` dimensions at
  `delta <= 6`; the `SI` dimensions alone (Molien route) out to `delta = 100`.
- **Extrapolated, and labelled as such:** the crossover values `~145` and
  `~120`. What is *rigorous* is that at `delta = 100` the source is still 4.4x
  smaller than `SI`, so the crossover is `> 100` — which is already enough to
  make the route useless as a bound, since 80 is known.
- **Not determined:** `delta_0`. The bracket is unchanged by this session:
  `8 <= delta_0 <= 80` (given the published deficit sequence), `6 <=`
  unconditionally.
- **Not done:** the Derksen–Weyman side proper. I used the Cauchy/Kronecker
  decomposition and a Kostant alternating sum, not Schofield semi-invariants
  `c^V` or the Horn-type inequalities. Those would describe *which* weights
  support semi-invariants and give generators; they would not change §4's
  conclusion, because that conclusion is about dimensions and the dimensions are
  now known exactly.
- **Not verified:** that `dim SI^tau / dim SI -> 1/2`. It is 0.91, 0.79, 0.69,
  0.63, 0.58 at `delta = 2..6` and clearly decreasing; the `~120` figure assumes
  it settles near 0.5. Only the `~145` figure rests on exactly computed `SI`.
