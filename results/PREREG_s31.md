# PRE-REGISTRATION — `delta_0` by the quiver route (session 31)

Committed **before any new computation**. Branch `s31-quiver`, fresh clone of
public `origin/main`.

**Tip at clone: `1203fe4` exactly.** Ancestry check passes (`1203fe4` is an
ancestor of `HEAD` — it *is* `HEAD`). **No rollback alarm, but a note the
integrator should see: session 28's branch `s28-d5` is NOT merged.** None of
`docs/d5_ideal.md`, `docs/session_28.md`, `docs/paper_section4_draft.md`,
`results/PREREG_s28.md`, `analysis/wk7_s28_*.py`, or the `r >= 3` correction to
`docs/isotypic_rank.md` §4 is in `main`. Everything this brief cites as "known
(session 28)" lives only in the delivered bundle. I branch from `1203fe4` and
restate what I need rather than assume it is present.

Calibration (brief §4) run before writing this file:
`analysis/wk6_s26_regress.py` — **all checks passed, 18 s**, including
`1, 6, 31, 141, 618, 2488` and the Jacobian tables `4,10,20,29,38` /
`4,10,20,35,50`.

Date: 2026-09-01.

---

## 1. The dictionary, derived by hand before computing

`Rep(K_5, (3,3)) = (M_3)^5`, group `GL_3 x GL_3` acting by `A_k -> P A_k Q`.
Since `det(P A Q) = det P . det Q . det A`, each coefficient `c_alpha` of
`det(sum s_k A_k)` is a semi-invariant of weight `(det_P, det_Q)`. Write
`SI_{(delta,delta)}` for the space of semi-invariants of weight
`(det_P^delta, det_Q^delta)`; a semi-invariant of that weight is automatically
homogeneous of degree `3delta` (scale `P = tI`).

**(D1) The graded decomposition.** As a `GL_5`-module (the five arrows carry
`C^5`), by Cauchy in the arrow slot and then Kronecker in the two matrix slots,

    Sym^{3delta}( C^5 (x) C^3 (x) C^3 )  =  sum_{lam |- 3delta} S_lam(C^5) (x) S_lam(C^9),
    S_lam(C^3 (x) C^3)                   =  sum_{mu,nu} g(lam,mu,nu) S_mu (x) S_nu,

and the `(det^delta, det^delta)` part picks `mu = nu = (delta^3)`. Hence

    SI_{(delta,delta)}  =  sum_{lam |- 3delta, ell(lam) <= 5}
                              g(lam, (delta^3), (delta^3))  S_lam(C^5).

**(D2) `SI_{(1,1)}` is exactly 35-dimensional, and is `Sym^3 C^5`.**
`chi^{(1,1,1)}` is the sign character, so `chi^{(1^3)} . chi^{(1^3)} = chi^{(3)}`
and `g(lam,(1^3),(1^3)) = [lam = (3)]`. Therefore
`SI_{(1,1)} = S_{(3)}(C^5) = Sym^3 C^5`, of dimension `C(7,3) = 35`.
**This is a proof, not a prediction** — it answers pre-registration item 2 in
advance and confirms the integrator's prior. The span of the `c_alpha` is *all*
of `SI_{(1,1)}`: there is no semi-invariant of that weight other than the
coefficients of `det(sum s_k A_k)`.

**(D3) The transpose, and why `m_det` is the right bound.** `tau : A_k -> A_k^T`
commutes with the `GL_5`-action and fixes `det(sum s_k A_k)`, so
`C[D_5] ⊆ SI^tau`. Session 26's Peter–Weyl count is exactly the `tau`-average:

    dim SI^tau_{(delta,delta)}  =  sum_{ell(lam) <= 5} m_det(lam) . dim S_lam(C^5),

because `m_det(lam) = dim (S_lam)^{H}` with `H = H^0 |x <tau>` and
`dim (S_lam)^{H^0} = g(lam, rect, rect)`. So the quiver picture **re-derives**
`mult <= m_det`; it does not improve on it.

**(D4) The bookkeeping the brief asks to be sorted out before computing.**
Two different failures of the map `Sym^delta(SI_1) -> SI^tau_{(delta,delta)}`:

- its **kernel** is `I(D_5)_delta` — this is what `delta_0` is about;
- its **cokernel** is new generators of `SI^tau` — irrelevant to `I(D_5)`.

They are independent, and both are nonzero in general. Reading a cokernel as
evidence about a kernel is exactly the kind of slip that has bitten this
programme twice; it is written down here so it cannot happen quietly.

**(D5) The one genuinely new thing the route offers.** Since the image sits
inside `SI^tau`,

    C(34+delta, 34)  >  dim SI^tau_{(delta,delta)}   ==>   I(D_5)_delta != 0,

and by session 28's concentration lemma (a length-`<= 4` highest-weight vector
in 5 variables sees only 4 variables, where `D_4` is everything) that kernel
sits at a length-5 weight. So the first crossover `delta_x` of those two
sequences is a **rigorous upper bound on `delta_0`**, computed from dimensions
alone. The source grows like `delta^34/34!`; the target is the graded piece of a
29-dimensional ring, so it grows like `c . delta^28`. The crossover therefore
exists and is finite.

## 2. Predictions, with falsifiers

**P1 — `SI_{(1,1)} = 35`.** Settled by (D2) above; recorded as pre-registered
because the brief asks for it. *Falsifier F1: a computed `dim SI_{(1,1)} != 35`,
which would mean the Cauchy/Kronecker dictionary (D1) is misapplied and
everything downstream is void.*

**P2 — the quiver route will not compute `delta_0`, and its pointwise bound is
weaker than the programme's.** Concretely I predict `SI` and `SI^tau` are **not**
generated in degree 1, with the first cokernel already at `delta = 2` at the
`GL_5`-type `S_{(2,2,2)}(C^5)`: `a((2,2,2),2) = 0` (from
`Sym^2 Sym^3 = S_(6) + S_(4,2)`) while `m_det((2,2,2)) = 1`, so
`Sym^2(SI_1) -> SI^tau_{(2,2)}` misses a whole isotypic piece.
*Falsifier F2: that map is surjective at `delta = 2`.*

**P3 — the crossover, and the number this session is actually after.**
`delta_x = min{ delta : C(34+delta,34) > dim SI^tau_{(delta,delta)} }`.
**Predicted `delta_x` in `[25, 60]`, point estimate 35.** Reasoning logged: the
leading-order comparison `delta^34/34!` against `c . delta^28/28!` crosses at
`delta^6 ~ c . (34.33.32.31.30.29) ~ 9.7e8 . c`, giving `delta ~ 31` at `c = 1`
and `~ 68` at `c = 100`; small-`delta` behaviour will move it but not by orders.
*Falsifier F3: `delta_x` outside `[25,60]`.*

**P4 — `delta_0` itself will NOT be attained.** I expect to improve the bracket
only at the top: from `8 <= delta_0 <= 80` to `8 <= delta_0 <= delta_x`. I do
**not** expect to find the first bite. *Falsifier F4: an actual length-5 weight
with `mult < a` exhibited at a specific degree.*

**P5 — the six-nodal question (task D).** `D_5` is irreducible (image of an
irreducible variety) of dimension 29; its generic member has six nodes (the
pencil meets the rank-one Segre, of dimension 4 in `P^8`, in `deg = 6` points by
Giambelli); and the six-nodal locus has dimension `35 − 6 = 29`. So **`D_5` is
an irreducible component of the closure of the six-nodal locus** — that much I
predict is provable outright. **Equality** holds iff that locus is irreducible,
which I predict is true but do **not** expect to prove.
*Falsifier F5: a six-nodal quinary cubic provably outside `D_5`, or a dimension
count that diverges — either would mean `D_5` is cut out by more than nodality
and would change the `delta_0` hunt.*

## 3. Method, fixed in advance

- **Two independent routes to `dim SI_{(delta,delta)}`**, cross-checked at
  `delta <= 6` as the brief requires:
  (i) the Kronecker route (D1): `sum_lam g(lam,rect,rect) dim S_lam(C^5)`,
  reusing session 26's exact `m_det` machinery for the `tau`-refined version;
  (ii) a **Molien/Weyl route**: `dim SI_{(delta,delta)}` is the multiplicity of
  `(delta^3) (x) (delta^3)`, so by Kostant's alternating sum it is
  `sum_{u,v in S_3} sgn(uv) N(delta.1 + rho − u.rho, delta.1 + rho − v.rho)`
  with `N(r,c)` the number of degree-`3delta` monomials in the 45 variables
  with row-marginals `r` and column-marginals `c` — a weighted 3x3 contingency
  count, `sum_E prod_{ij} C(E_ij + 4, 4)`.
  These share no code and no identity. A disagreement at any `delta <= 6` stops
  the session (brief kill criterion 2).
- **Consistency with what is certified** (brief kill criterion 1): the framework
  must reproduce `mult = a` at every length-5 weight with `delta <= 7`, and must
  not contradict `disc ∈ I(D_5)` at `delta = 80`. Checked before any new claim.
- Exact arithmetic only; Python integers throughout (the numbers exceed 64 bits
  well before the crossover).

## 4. What is not touched

`paper/det3-conductor.tex`, `PROJECT_NOTES.md`, `docs/boundary_deficit.html`.
New files only, except that `docs/isotypic_rank.md` is this line's own file —
and since session 28's correction to its §4 is not in `main`, I will **not**
re-apply it here (that would create a merge conflict with the unmerged `s28-d5`
branch); I flag it instead.
