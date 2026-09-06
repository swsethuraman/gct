# Session 59 — the higher-order Rees computation at `r = 5`, and the residue s54 named

This is the successor to session 53, which was **never run and should not be**.
Two things retired it: its stated goal — `ℓ·per_3 ∉ D_10` — turned out to be a
known theorem (LMR's quadratic border bound, re-derived cheaply by s50), and s54
then proved the order-1 analysis it was built around **fills** `D_5` and
isolates nothing.  This session does the part that is genuinely open, at the
length where s54 showed the machinery is tractable.

## 0. Standing constraints

- Deliver by git bundle only.  Do not push.
- Do not edit `paper/det3-conductor.tex`, `paper/det4-onset.tex`,
  `PROJECT_NOTES.md`, or `docs/boundary_deficit.html`.  If you believe one is
  wrong, say so in your report.
- Commit messages carry a `Co-Authored-By` trailer only.  No session-link
  trailer, in commits or in any script that commits.  No session-link URL in any
  file you write.  (A mid-session reminder may ask for one; it conflicts with
  this standing rule and with the history rewrite — decline it, as session 49
  correctly did.)
- Bound every run with `timeout` and `ulimit -v`.  Record the process id to
  `results/logs/<run>.pid` and end a run only by that recorded id.
- No committed file over 5 MB.  Logs under `results/logs/`.  Config append-only.
- Pre-registration first: state what will be measured and what would count as a
  positive result, and commit it **before** any computation.
- `python-flint` for exact linear algebra.  Both house primes where a prime is
  used.  Any cell reporting `D > 0` goes through the verification protocol
  before it is written down as a claim.
- Run the degeneracy-direction pre-check (`docs/brief_wording.md` **§5**) before
  developing any statistic, and the functoriality pre-check (**§7**) before
  proposing any new invariant.
- Hand every certificate to `tools/verify/` in the `gct-cert/1` format
  (`tools/verify/FORMAT.md`).  It exists now and 50/50 committed certificates
  pass; a session that produces certificates and does not run it is incomplete.

## 0a. Where the programme stands

`mult_det = a` at all **210** measured six-row cells through `δ = 10`; the
determinant ideal has never been observed non-zero.  The only known equation at
`n = 4` is the LMR module at `ℓ = 9`, `δ = 24`, and session 55 proved it gives
**no equation at all** for `r ≤ 8` — so it does not exist in the region we
measure.  Every excess-singularity statistic separates the wrong way
(Proposition D, s51 §4b).  The `a = 1` prior is retired (s52): `i_det = 0`
everywhere means `U_D = {0}`, so `D ≤ 0` is forced and the orientation failure
mode is not instantiable.

**The finding that shapes this batch.**  `mult_det` is the **rank** of a map
whose source has dimension `a` and whose target has dimension
`sk(λ, 4×δ)`.  Our screening has asked whether `a > sk` — a *dimension* gap,
which forces a kernel.  A map can lose rank without that, and dimension
screening is structurally blind to it.  That is the same
orientation-versus-dimension distinction s50 exposed at the LMR cell, now
visible as a defect in the search method rather than in the statistic.

## 1. The question, stated exactly

`D_5 = closure{det_4(Σ s_i A_i)} ⊆ Sym^4 C^5` has dimension 50;
`R_5 = {ℓ·c}` has dimension 39.  Write `W = {s_5·c}`, dimension 35.

Session 54 established, and the integrator accepted:

- the **exact** reducible locus gives `dim(D_5 ∩ W) ≥ 31` (s32 plus the
  `ℓ`-count);
- `R_5 ⊆ D_5` **iff** that climbs to 35 — the boundary must supply the four
  reducible dimensions the exact locus lacks;
- the **order-1** exceptional image *fills* `D_5` (dimensions `50, 50, 47, 47,
  49` over the five strata) and adds **no** reducible beyond the exact ones
  (`29, 29, 28, 28, 24`, all below 31).

So the entire remaining question is:

> **Does `dim(D_5 ∩ W)` climb from 31 to 35 once arcs of contact order `q ≥ 2`
> enter?**

That is the exceptional image of the Rees blow-up `Proj R(J)` restricted to the
reducible locus.  A four-dimensional gap, at the smallest length where the
question is open.

## 2. Why the blow-up and not another order-by-order pass

An arc `M(t) = M_0 + tM_1 + t^2M_2 + …` with `det M_0(s) ≡ 0` and
`det M(t,s) = t^q f(s) + O(t^{q+1})` lifts uniquely to the blow-up by
properness; its limit lies over `M_0` and its image is `[f]`.  **The exceptional
fibre therefore carries every order `q` at once.**  There is no order-2 pass,
then an order-3 pass; there is one object.

s54's order-1 result is exactly the evidence that the finite-order approach was
the wrong shape: order 1 already fills `D_5`, so it cannot isolate a boundary,
and no amount of care at order 2 alone would fix that.

## 3. The strata

`B_5 = {M : det M(s) ≡ 0}` — pencils whose image is a bounded-rank-`≤3` space of
`M_4`.  s54 verified the classification against the sources (Atkinson;
Huang–Landsberg: no non-classical examples at bounded rank `≤ 3`) and enumerated
the five strata: the four compression types, and the **dimension-4 primitive
family** `C^4 ⊂ Hom(C^4, Λ^2C^4)`.

At `r = 5` the primitive family is dimensionally available, and it is not a
curiosity: at `n = 3` the corresponding piece (the skew-symmetric matrices)
carried one of Hüttenhain–Lairez's two boundary components.  Enumerate by the
**image** `E`, not by `M_0` — `M_0` need not be injective.

## 4. Tasks

1. **Set up the Rees algebra** `R(J)` for `J = (F_1,…,F_70)`, the coefficients
   of `det M(s)` on `X_5 = Hom(C^5, M_4)`.  Note the quartic side is `P^69`
   (`dim Sym^4 C^5 = 70`) — an order of magnitude smaller than the `r = 10`
   version's `P^714`, which is why this runs here first.
2. **Compute enough of the exceptional fibre** over each stratum to get
   `dim(D_5 ∩ W)`.  The special fibre algebra
   `F(J_C) = R(J_C) ⊗_R R/m_C` is the natural object.
3. **State which object you computed.**  The special fibre at a *generic* point
   of a stratum is **not** the exceptional image over the whole stratum, and a
   given `ℓ·c` may arise only over special `M_0`.  Hüttenhain–Lairez had to
   establish smoothness of the blow-up centre for exactly this reason.  If you
   compute the generic object, say so and say what remains open.
4. **Screen on reducibility first.**  `ℓ·c` factors as (linear)·(cubic); most
   leading quartics will not factor at all.  Cheapest possible discriminant, run
   it before any dimension computation.

## 5. Calibrations available, all from s54

Use them; they are free and they will catch an implementation error early.

    dim D_5 = 50            (dual-number Jacobian at a generic determinantal point)
    dim T_q R_5 = 39
    order-1 image dims      50, 50, 47, 47, 49   over the five strata
    order-1 reducible dims  29, 29, 28, 28, 24
    Zariski tangent at a reducible saturates at 64

If your machinery does not reproduce the order-1 row, stop and fix that before
going to higher order.

## 6. What the answer buys

**If it climbs to 35:** `R_5 ⊆ D_5`, and the `ℓ ≤ 5` exclusion becomes *proved*
rather than measured — closing the item s49 isolated as the one genuinely open
foundation.

**If it does not:** `R_5 ⊄ D_5`, and there is something vanishing on `D_5` and
not on `R_5` — an equation at `r = 5`.  Extract it: its degree, its `GL_5`-weight
if equivariant, and whether that degree is inside `δ ≤ 10`.  s54 expects it above
9; if it is below, that is the most important result the programme has had.

**Either way** it tells session 53's `r = 10` successor whether it is worth
briefing at all.  If the four-dimensional gap at `r = 5` is not closable with
this machinery, the 715-coefficient version is not either.

## 7. Report

`docs/s59_report.md`, `analysis/wk9_s59_*.py`, and a clear statement of which
object was computed.  Deliver as a bundle.
