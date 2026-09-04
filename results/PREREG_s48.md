# Pre-registration — session 48

Branch `s48-theorems`, off `9aa6a9c` (main tip at clone).  Written and
committed **before any rank, Jacobian or nullspace was computed** in this
session.  Labels, as in sessions 37/44: **proved** / **measured** /
**certified** / **adopted-from-literature** / **expectation**.

Three independent targets, in the brief's priority order.  Stopping rule
(standing): target A gets the first half of the session; if it stalls it is
written up as a narrowed search and B and C are run regardless.  A rank
modulo `p` at a point is a **lower** bound on the generic rank; a drop is
therefore *certified*, never *proved*, by that route (`docs/sixrow_cap.md` §4),
and every claim below inherits that direction of inference.

---

## Target A — the six non-Koszul syzygies at `(n, r, d) = (4, 6, 7)`

**What would close it.**  Six degree-4 logarithmic derivations
`δ = Σ_k G_k ∂/∂s_k` with `δ(F) = 0`, in closed form, valid for every pencil.
Equivalently: `W(s) = Σ_k G_k A_k ∈ L ⊗ S_4` with `tr(adj M(s) · W(s)) ≡ 0`,
six of them independent modulo the 90 Koszul.

**A1 (headline).**  I find all six in closed form and verify symbolically at a
general pencil.  **Prior 0.30.**

**A2.**  I identify the `GL(L)`-equivariance type of the 6-dimensional space —
i.e. which rank-6 representation of `GL_6 = GL(L)` it is — by transporting the
computed space along a random `g ∈ GL_6`.  **Prior 0.75.**

**A3 (the structural guess I am pre-registering, because it is falsifiable).**
The measured drops are `C(r,5) = 0, 1, 6` at `r = 4, 5, 6`, and
`C(r,5) = dim Λ^5 C^r`.  I predict the six-dimensional space is
`Λ^5 L ≅ L^* ⊗ det L` as a `GL(L)`-representation — so the six syzygies are
naturally indexed by the six 5-element subsets of a basis of `L`, not by the
six basis vectors.  Concretely: transporting the space along `g ∈ GL_6` should
multiply it by `det(g) · (g^{-1})^T`, not by `g`.  **Prior 0.45** that the type
is `Λ^5 L` up to a determinant twist; **prior 0.25** that it is `L` (or `L^*`)
untwisted; **prior 0.30** that it is neither / the test is inconclusive.

**A4 (the new family to test, which session 44 did not).**  Session 44 ruled
out `W = F·B − ¼(∂_BF)·M(s)` (the `𝒳 = B·adj M` branch) as entirely Koszul.
The *other* branch of the Gulliksen–Négård kernel is untested:
`𝒳 = adj(M)·B`, giving `W = adj(M)·B·M(s) − ¼ tr(adj(M)B)·M(s)`, and its
transpose-side twin `W = M(s)·B·adj(M) − ¼ tr(B adj M)·M(s)`.  These are
degree 4, lie in the GN kernel by construction, and are **not** of the form
`F·B`.  I predict the six extra syzygies lie in the span of
`π_L`-corrected members of these two families, together with `S_1`-multiples
of the degree-3 branch.  **Prior 0.40.**

**A5 (falsifier I will run either way).**  Whatever the six are, their
coefficient forms `G_k` are not in `J(M)_4` (s44, measured).  I will re-measure
this and additionally report `dim (span of the six ∩ J(M)_4 ⊗ L)` and whether
the six span a `GL(L)`-irreducible.

**Stopping rule A.**  If after the first half of the session no closed form and
no equivariance type is in hand, A is written up as: the space computed
explicitly at two pencils and both primes, the families ruled out, and the
search narrowed.  A is not allowed to consume B or C.

---

## Target B — the discriminating rank at `(n, r) = (5, 7)`, `d = 3n−5 = 10`

Two formulas fit `0, 1, 6` at `r = 4, 5, 6`:

    C(r,5)          →  21 at r = 7
    (r−4)(2r−9)     →  15 at r = 7

**B1 (headline prediction).**  The drop at a determinantal pencil is **21**.
**Prior 0.55.**  `P(15) = 0.20`.  `P(anything else, including a
ceiling-forced value) = 0.25`.

**Reason for the 0.55.**  `C(r,5) = dim Λ^5 C^r` has a structural reading
(A3 above) and gets the `r = 4` leg — a genuine zero, the smoothness of the
generic determinantal hypersurface in `P^3` — for a reason;
`(r−4)(2r−9)` is a two-parameter fit to three points with a spurious zero at
`r = 4.5`.  The 0.25 residue is mostly the risk that the Gulliksen–Négård
ceiling binds at `(5,7,10)` and forces a larger drop, exactly as it does at
`(3,6)`, `(4,7)` and `(4,8)`.  I will compute the `n = 5` GN ceiling
(`0 → S(−10) → S(−6)^25 → S(−5)^48 → S(−4)^25 → S`) **before** reading any
determinantal rank, and report `ceiling − ρ_10` as a pre-condition on the
test's validity.

**B2 (control, must pass first).**  A random quintic in 7 variables returns
`rank M_10 = ρ_10 = C(16,6) − h_10(5,7)` at both house primes.  If the control
fails the determinantal ranks are not read.  **Prior 0.95.**

**B3.**  The matrix shape.  The brief says `12012 × 8008`.  With the house
convention (`docs/sixrow_cap.md` §1, `analysis/wk9_s44_poly.py`) rows are
`r · dim S_{d−n+1} = 7 · C(12,6) = 7 · 924 = 6468` and columns
`dim S_10 C^7 = C(16,6) = 8008`.  I predict the true shape is **6468 × 8008**
and that `12012 = 7 · 1716 = 7 · dim S_7 C^7` is the shape at `d = 11`, one
degree too high.  **Prior 0.85.**  I will report the shape I actually build and
will additionally run `d = 11` if `d = 10` is inconclusive.

**B4.**  Several seeds, both house primes, determinantal pencils and random
controls.  If the drop is large enough that a multimodular certificate is
affordable, run one; I predict it is **not** affordable at this size
(`ρ_10 ≈ 7000`, Hadamard exponent ~7000, ~10× the `s44` `d = 7` certificate at
size 666 which already cost 7.6 min per pencil).  **Prior 0.80 that no
certificate is run**, and the result is labelled *certified at explicit
pencils modulo `p`* — one label weaker than s44's `d = 7`.

---

## Target C — the washout threshold as a function of `m`

`P_r = R_r` requires `{per_m(A(s))}` dense in `Sym^m C^r`, `A(s)` an `m × m`
matrix of linear forms in `r` variables.

**C1 (the naive count, which I will re-derive).**  `m² r ≥ C(r+m−1, m)` is
necessary and free.  I predict it reproduces the integrator's table
`r* = 7, 5, 5, 4, 4, …` at `m = 2, 3, 4, 5, …`.  **Prior 0.9.**

**C2 (the correction I am pre-registering as a prediction, before computing
anything).**  The naive count is **not** the sharp necessary condition,
because the fibres of `Φ_{m,r} : (M_m)^r → Sym^m C^r` are positive-dimensional:
the connected symmetry group of `per_m` inside `GL_{m²}` is the torus
`{A ↦ D A E, det(DE) = 1}` of dimension `2m − 1` (Marcus–May / Botta), so

    dim image  ≤  m² r − (2m − 1)      for m ≥ 3,

and the sharp necessary condition is `m² r − (2m−1) ≥ C(r+m−1, m)`.
**Prior 0.85** that this is the right correction for `m ≥ 3`.

**C3 (the specific falsifiable consequence — the `m = 2` row is wrong).**
`per_2(A) = a₁₁a₂₂ + a₁₂a₂₁` is a **nondegenerate quadratic form in 4
variables**, so `per_2(A(s))` is the pullback of a rank-4 quadric along a
linear map `C^r → C^4` and therefore has rank `≤ 4` **for every** `A`.  Hence
`D_r^{per_2} = {quadrics of rank ≤ 4} ⊊ Sym^2 C^r` as soon as `r ≥ 5`, and

    r*(2) = 4,  not 7.

The naive count says `r ≤ 7` because it misses the `dim O(4) = 6` stabiliser
of the smooth quadric (`per_2 ≅ det_2`; its symmetry group is larger than the
`2m−1` torus).  I predict the Jacobian rank at `m = 2` is `4r − 6` for `r ≥ 4`,
i.e. `20 < 21` at `r = 6` and `22 < 28` at `r = 7`.  **Prior 0.90.**
If this is right the integrator's table has an error in its first row and the
theorem must be stated for `m ≥ 3`.

**C4 (the Jacobian checks — the sufficiency half).**  At every `(m, r)` with
`r ≤ r*(m)` I compute `rank dΦ_{m,r}` at a random integer point modulo both
house primes, using `∂ per_m(A(s)) / ∂(A_k)_{ij} = s_k · per_{m−1}(A(s)^{(i,j)})`.
Full rank `C(r+m−1, m)` at one point **proves** density (Lemma 1 of
`docs/washout_lemma.md`; a rank at a point is a lower bound on the generic
rank, which is the *right* direction here).  I predict full rank at every
`(m, r)` with `r ≤ r*(m)` and `m ≥ 3`.  **Prior 0.70** for all of them;
**prior 0.90** for the `m = 3, 4` rows individually.  The risk is that the
counting threshold is not sharp somewhere — that some `(m, r)` satisfies the
inequality but the map still is not dominant, as C3 says happens at `m = 2`.

**C5 (framing, pre-registered so it cannot drift).**  Whatever comes out, this
is a limitation on the **length-reduced model** — on what a covariant of
bounded length can see — and not a barrier theorem about GCT.  It will **not**
be described as a natural-proofs barrier (natural proofs is constructivity plus
largeness; the known GCT barriers are Bürgisser–Ikenmeyer–Panova on occurrence
obstructions).  I predict the threshold itself is **not** in the literature in
this form.  **Prior 0.6 unknown, 0.4 known** (the density of permanental
pencils / dimension of `D_r^{per_m}` is close to published work on
permanental-vs-determinantal varieties, so partial priority is likely).

---

## Target D (only if time remains) — the excess-singularity proposition

Session 44: `ℓ·c` is singular in codimension 2 (a threefold in `P^5`) against
the determinantal curve, so the pad-side Milnor algebra grows like `d³` where
the determinantal one grows like `d`.  **D1:** I can make the threshold
explicit and state, as a proposition, that no construction reading excess
singularity produces `D > 0` at `n = 4`.  **Prior 0.5** that it is written this
session at all; if written, prior 0.8 that the degree bound is explicit rather
than asymptotic.

---

## Deliverables (fixed here)

`results/PREREG_s48.md` (this file); `docs/sixrow_cap_closed.md` (A and B);
`docs/washout_threshold.md` (C); `results/s48_*.md` raw ranks;
`analysis/wk9_s48_*.py`; logs under `results/logs/`.

Single-writer files never touched: `paper/det3-conductor.tex`,
`paper/det4-onset.tex`, `PROJECT_NOTES.md`, `docs/boundary_deficit.html`.
Delivery by `git bundle` on `s48-theorems` only; no push.
