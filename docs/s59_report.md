# Session 59 — the higher-order Rees exceptional image at `r = 5`: contact order does not climb

Branch `s59-rees5`, off `main` tip `0960bd5` (fresh public clone, container only;
delivered by bundle, not pushed). Pre-registration `results/PREREG_s59.md`
(commit `5ae85ae`, before the higher-order measurement). Code
`analysis/wk9_s59_*.py`; data `results/s59_*.json`; certificate
`results/certs/s59_exact31.json`; logs `results/logs/s59_*`. Labels:
**proved** / **measured** / **adopted-from-literature** / **expectation**.

`python-flint` for every rank; house primes `2147483647, 2147483629`, third prime
`2147483587` for certification; Jacobians by dual numbers `ε²=0`. The exact-locus
lower bound is additionally certified **over `Q`** by `tools/verify` (six
certificate primes) and the two anchors are reproduced by an independent
sympy-adjugate implementation at a fourth prime.

## 0. Verdict

> **The object computed.** For each bounded-rank-3 stratum and each contact order
> `q`, the dimension of the reducible exceptional image at a **generic** V-point
> — a generic arc `M_0 + tM_1 + … + t^q M_q` with `M_0 ∈ E`, cancellation
> `g_1 ≡ … ≡ g_{q−1} ≡ 0`, and leading quartic `g_q ∈ W` — is the **generic
> special fibre** of the Rees blow-up restricted to the reducible locus. It is a
> rigorous lower bound on `dim(D_5 ∩ W)`; it is **not** the full exceptional image
> over the stratum, because the exact interior (dimension 31) sits over special
> `M_0` that generic sampling does not see.

> **The question s54 named, answered.** s54 reduced everything to one 4-dimensional
> gap: does `dim(D_5 ∩ W)` climb from 31 to 35 once arcs of contact order `q ≥ 2`
> enter? **At generic configurations it does not, through `q = 4`.** The reducible
> exceptional image is **invariant of contact order**:
>
> | `q` | ker | coker | c21 | c32 | prim |
> |---|---|---|---|---|---|
> | 1 (s54, reproduced) | 29 | 29 | 28 | 28 | 24 |
> | 2 | 29 | 29 | 28 | 28 | 24 |
> | 3 | 29 | 29 | 28 | 28 | 24 |
> | 4 | 29 | 29 | 28 | 28 | 24 |
>
> — **measured**, three primes, three seeds, every V-point verified
> (`g_1..g_{q−1} ≡ 0`, `π g_q = 0`). The second- and higher-order contact terms
> (the Hessian-of-`det` pieces `e_q(M_0; M_1,…)`) produce **no reducible not
> already present at order 1**. The mechanism s54 hypothesised might supply the
> four missing dimensions demonstrably does not, at generic configurations.

> **The rigorous lower bound.** `dim(D_5 ∩ W) ≥ 31` — the exact reducible
> determinantal locus (s32), reproduced here and now **certified over `Q`**
> (`results/certs/s59_exact31.json`, `tools/verify` PASS: rank 31 over `Q` by six
> certificate primes, both house primes, a `31×31` minor nonzero over `Z`). Every
> arc value (`≤ 29`) is **below** this; the 31 is interior, not boundary.

> **Verdict, unchanged in direction, sharpened in content.** `R_5 ⊆ D_5 ⟺
> dim(D_5 ∩ W) = 35`. No instrument reaches 35; every instrument that resolves a
> component lands at `≤ 31`. So the evidence leans **`R_5 ⊄ D_5`**, as in s54 —
> now with the specific higher-contact-order mechanism **eliminated as a source of
> a climb** (through `q = 4`, generic). It is **not a proof**: generic V-point
> sampling cannot exclude a component of `D_5 ∩ W` hidden over special `M_0` (the
> exact 31-locus is itself such a special component), and a proof of the negative
> needs an **upper** bound on `dim(D_5 ∩ W)` — the full special-fibre algebra
> `F(J_C)` (a Gröbner/elimination object) or a length-5 equation of `I(D_5)` at
> degree `> 9`. Neither is reachable in this container (no CAS; the equation is out
> of the measurable range, s54/s55).

> **What this buys session 53 (the stopping-rule call).** The `r = 5` arc-jet
> machinery is fully tractable — seconds to a couple of minutes, running to contact
> order 4 at three primes — but it yields **only lower bounds** (the generic
> special fibre). It cannot **close** the question even at `r = 5` (`P^69`); the
> decisive object is the special-fibre algebra, which needs a CAS the programme's
> `python-flint`-only rule does not provide. At `r = 10` (`P^714`) the arc route is
> *a fortiori* only evidential and an order of magnitude heavier. **s53 as a
> separation session is not worth briefing on this machinery**; its original
> motivation is already gone (`ℓ·per_3 ∉ D_10` is known — s55, integrator notes),
> and as a boundary-description session it needs a CAS-backed Rees computation, for
> which this pilot has specified exactly the deliverable (an upper bound on
> `dim(D_5 ∩ W)`, or `dim F(J_C)`) that the arc route cannot produce.

## 1. The objects, and a reformulation

`D_5 = closure{det_4(Σ s_i A_i)} ⊆ Sym^4 C^5`, dim 50; `R_5 = {ℓ·c}`, dim 39;
`W = {s_5·c}`, dim 35 (fix `ℓ = s_5`). All **proved/adopted** (washout Cor. 7,
s32).

**Reformulation (proved, elementary; used throughout).** Let `π : Sym^4 C^5 →
Sym^4 C^4`, `π(f) = f|_{s_5=0}`. Then `W = ker π`, and for `f = det M(s)`,
`π(f) = det(M'(s'))` with `M' = s_1A_1+…+s_4A_4`. Hence

    D_5 ∩ W  =  the fibre of  (π|_{D_5} : D_5 → D_4^{det_4})  over 0.

`dim D_4^{det_4} = 34` (the determinantal hypersurface in `Sym^4 C^4`), so the
generic fibre is `50 − 34 = 16`; the fibre over `0` has jumped to `≥ 31`. Its
interior `{det M : (A_1..A_4) a singular 4-space}` is exactly the s32
configuration and equals the exact 31-family. The whole question is whether the
**closure** of that fibre adds a boundary component reaching 35. This gives the
programme a clean statement of the object and why it is a special (jumping) fibre.

## 2. Machinery, validated before use (§calibration, KC1/KC2)

`analysis/wk9_s59_core.py` builds `det M(t,s)` for an arc as a `t`-series of
quartics-in-`s` in dual numbers; ranks are `nmod_mat` only. Before any
higher-order work every s54/s32 anchor was reproduced at both house primes
(`ea8183e`, `0d3d627`):

- `dim D_5 = 50` (tangent at a generic determinantal point) — **measured**;
- order-1 exceptional image `50, 50, 47, 47, 49` over `ker,coker,c21,c32,prim`
  (fills `D_5`) — **measured**, matches s54;
- order-1 reducible border `29, 29, 28, 28, 24` at a V-point — **measured**,
  matches s54;
- exact reducible locus `29, 29, 31, 31, 25`, maximum **31** on `c21/c32` —
  **measured**, matches s32 Theorem 5;
- independent confirmation of `dim D_5 = 50` and the exact `31` by a
  sympy-adjugate Jacobian sharing no code with `det_arc`, at a fourth prime
  (`analysis/wk9_s59_indep.py`).

If the order-1 row had not reproduced, the session would have stopped (it did
not).

## 3. The higher-order computation (§2B, primary)

For order `q`, the reducible family `[g_q/s_5]` at a generic V-point has dimension

    rank d(g_1,…,g_q)  −  rank d(g_1,…,g_{q−1}, π g_q)

(the identity `dim B(ker A) = rank[A;B] − rank A`, with the constraint
`{g_1=…=g_{q−1}=0, π g_q=0}` and `(π g_q, c)` reparametrising `g_q`). The V-point
is built iteratively: `M_1` generic in the homogeneous `{g_1 ≡ 0}`; each `M_j`
(`2 ≤ j ≤ q−1`) solving the inhomogeneous `g_j ≡ 0` (linear in `M_j` via
`tr(adj M_0 M_j)`); `M_q` solving `π g_q = 0`. `analysis/wk9_s59_orderq.py`,
calibrated to reproduce the order-2 row before running `q = 3, 4`.

**Result (measured, three primes, three seeds):** the table in §0 — `29, 29, 28,
28, 24` at every order `q = 1, 2, 3, 4`. Contact order is inert for the reducible
part. `rank_full`/`rank_con` are healthy and prime-stable (e.g. c21 `q=3`:
`68 − 40 = 28`).

**Why the route runs to `q = 4` at all (order-3 solvability probe,
`wk9_s59_order3probe.py`).** Extending contact to order 3 needs
`tr(adj M_0 M_2) = −e_2(M_0;M_1)` solvable in `M_2`. The pre-registered guess was
that `−e_2(M_1)` generically escapes the image of `M_2 ↦ tr(adj M_0 M_2)`, forcing
`M_1` onto a nonlinear (higher-Rees) locus and halting the order-by-order route.
**That guess was wrong:** the cancellation is solvable at a generic `M_1` (codim
0, both primes, every stratum), so the route runs cleanly. A productive miss —
recorded in the ledger — and it is *why* the invariance is visible through `q=4`
rather than stopping at 2.

## 4. Tangent corroboration (§2C)

`analysis/wk9_s59_tangent.py`, at two kinds of reducible:

- **Special `q = s_5·det_3(N)`** (`c_0` a `3×3` determinant, s54's point): the
  union of `im dΦ` over inequivalent **block** representations
  (`[[s_5, r],[0,N]]` and `[[s_5,0],[c,N]]`, both in the fibre for all `r,c`, plus
  `GL_3` on `N`) saturates at **64**, reproducing s54 exactly (single rep 33 ≤ 42;
  curve `33, 42, 51, 60, 64`). `dim(T ∩ W) = 29`.
- **Generic `q = s_5 c_0`** (`c_0` in the 31-family, c21 config, not a `3×3`
  determinant): no block representation exists; the natural representation gives
  `im dΦ = 48` and `dim(im dΦ ∩ W) = 31`, matching the exact locus.

Both `≤ 31`, neither near 35. The tangent is a lower bound on
`dim T_{q_0}(D_5 ∩ W)` (an upper bound on the local dimension only at a smooth
point, and `q_0` is singular), so it is corroborating, not decisive; its value
`31` at the generic reducible is the sharpest such corroboration available.

## 5. Honest boundary

- **Proved / certified over `Q`:** the reformulation (fibre of `π|_{D_5}` over 0);
  `dim(D_5 ∩ W) ≥ 31` (the certificate, `tools/verify` PASS, six certificate
  primes + a `31×31` integer minor).
- **Measured (exact, ≥ two primes, V-points verified):** contact-order invariance
  `29,29,28,28,24` for `q = 1..4` (three primes, three seeds); the saturated
  tangent 64 (special) and `∩W` values 29/31; the order-3 solvability (codim 0).
- **Adopted:** `dim D_5 = 50`, `dim R_5 = 39`, `dim D_4^{det_4} = 34` (washout);
  s32's exact-reducible classification and the maximum 31.
- **Not proved:** the closure verdict. Evidence leans `R_5 ⊄ D_5`, now with the
  higher-contact-order mechanism eliminated (generic, `q ≤ 4`). A proof needs an
  **upper** bound on `dim(D_5 ∩ W)` — the special-fibre algebra `F(J_C)` (needs a
  CAS) or a degree-`>9` equation of `I(D_5)` (out of range).
- **Not done (needs a CAS, flagged for s53):** the special-fibre algebra / an
  elimination giving the upper bound; the balanced-cell sparse route (s42), the
  standing continuation of the multiplicity side.
- **Single-writer files:** none edited. The s54/s55 citation corrections
  (`washout_lemma`, `transfer_lemma`: s32 proves image, not closure,
  non-containment) are already applied per the integrator notes; nothing new to
  flag.

## 6. Pre-registration scorecard

| id | prediction | prior | outcome |
|---|---|---|---|
| E0 | §2A reproduces exact `dim = 31` | 0.90 | **confirmed** (certified over `Q`) |
| Q1 | order-2 reducible does not exceed 31 | 0.70 | **confirmed** (`= 29,29,28,28,24`, `< 31`) |
| Q2 | no stratum, any `q ≤ 3`, reaches 35 | 0.72 | **confirmed**, and extended to `q = 4` |
| T1 | saturated tangent `∩ W` in `[33,35)` | 0.55 | **missed low** — `31` (generic), `29` (special); *below* 33, further from a climb than predicted |
| V | verdict stays lean `R_5 ⊄ D_5`, not proved | 0.70 | **confirmed**, mechanism sharpened |
| S | special-fibre algebra intractable without a CAS; `r=10` a fortiori | 0.75 | **confirmed for the decisive object**; the *arc* route was more tractable than expected (ran to `q=4`) — the lower-bound half is cheap, the upper-bound half is what needs the CAS |

New (unregistered) findings: (1) the reducible exceptional image is **invariant of
contact order** `q = 1..4` — the sharp form of "order does not climb"; (2) the
order-3 cancellation is **unobstructed** (codim 0), correcting the pre-registered
nonlinear-obstruction guess and explaining why the order-by-order route runs to
`q = 4`; (3) the clean fibre reformulation `D_5 ∩ W = (π|_{D_5})^{-1}(0)`.

## 7. One line for the roadmap

s54 said the whole remaining question was whether `q ≥ 2` climbs. **It does not,
generically, through `q = 4`** — so the residue is now precisely a hidden climb at
special configurations, visible only to the special-fibre algebra, which needs a
CAS. That is the same wall at `r = 5` and at `r = 10`; the arc route does not scale
to a proof, and s53 should be re-scoped or parked accordingly.
