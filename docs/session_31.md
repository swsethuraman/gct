# Session 31 (2026-09-01) — `delta_0` by the quiver route

Branch `s31-quiver`, fresh clone of public `origin/main`.
**Tip at clone `1203fe4`; ancestry check PASSED** (it *is* the tip).
Container only; rule 9 respected. `paper/det3-conductor.tex`,
`PROJECT_NOTES.md`, `docs/boundary_deficit.html` untouched.
Calibration (`analysis/wk6_s26_regress.py`) passed first: all checks, 18 s.

**Flag for the integrator, before anything else: session 28's branch `s28-d5`
is not merged.** `docs/d5_ideal.md`, `docs/session_28.md`,
`docs/paper_section4_draft.md`, `results/PREREG_s28.md`,
`analysis/wk7_s28_*.py` and the `r >= 3` correction to `docs/isotypic_rank.md`
§4 are all absent from `main`. Everything this brief cites as "known (session
28)" lives only in the delivered bundle. I branched from `1203fe4` and restated
what I needed rather than assuming it; I did **not** re-apply the §4 correction,
because doing so would conflict with the unmerged branch.

Deliverables: `results/PREREG_s31.md`, `docs/quiver_route.md`, this record,
`analysis/wk8_s31_si.py`.

---

## 1. Headline

**The dictionary is exact and the route is a dead end, for a reason worth
knowing.**

- `SI_{(1,1)}` is exactly 35-dimensional and equals `Sym^3 C^5` — the
  coefficients of `det(sum s_k A_k)` are *all* the semi-invariants of that
  weight. Proved by a two-line Kronecker argument
  (`g(lam,(1^3),(1^3)) = [lam = (3)]`), then confirmed by both computational
  routes.
- **The transpose-refined semi-invariant count is exactly session 26's
  `m_det`.** So the quiver picture *re-derives* `mult <= m_det` rather than
  improving it: everything it can say pointwise, the programme already had.
  That is a satisfying structural identification and a null result at the same
  time.
- The one thing the route could have added — a **dimension crossover** forcing a
  kernel — lands near `delta = 145` (`~120` for the transpose-refined version).
  **Far above the discriminant's 80.** So it cannot improve session 28's bound.
- **The informative reading:** `I(D_5)` already contains an explicit element at
  degree 80 while counting forces nothing until roughly 145. The ideal shows up
  at least 65 degrees before dimensions require it. **`delta_0` is a genuinely
  geometric quantity, and no counting argument of this shape can reach it.**

One clean positive alongside: `SI^tau` is **not** generated in degree 1, and the
first new generator is at `delta = 2`, in exactly one copy of
`S_{(2,2,2)}(C^5)` — the arithmetic is `630 = 680 − 50` on the nose.

## 2. Prediction ledger

| # | pre-registered | outcome |
|---|---|---|
| P1 | `SI_{(1,1)} = 35` | **HIT** — and settled by proof in the pre-registration itself, then confirmed by both routes. F1 not fired. |
| P2 | `SI`/`SI^tau` not generated in degree 1; first cokernel at `delta = 2`, type `S_{(2,2,2)}(C^5)` | **HIT exactly** — cokernel `680 − 630 = 50 = dim S_{(2,2,2)}(C^5)`, one copy. F2 not fired. |
| P3 | crossover `delta_x in [25,60]`, point estimate 35 | **REFUTED.** The ratio `SI / Sym^d(SI_1)` *rises* to about 29.5 at `d = 30` before turning, and is still 4.4 at `d = 100`. `delta_x ~ 145` (`~120` for `SI^tau`). F3 fired. |
| P4 | `delta_0` not attained; bracket improves at the top only | **HALF-HIT.** `delta_0` indeed not attained — but the bracket did **not** improve at all, because the crossover is worse than the bound we already had. F4 not fired (no bite exhibited), but the predicted gain did not materialise. |
| P5 | `D_5` an irreducible component of the six-nodal closure (provable); equality true but unproved | **HIT** on the provable half (§5 of `docs/quiver_route.md`); equality remains open, as predicted. F5 not fired. |

Three hits, one half, one refutation — and the refutation is the one that
mattered. **P3 was the session's whole reason for existing.**

**Where P3 went wrong, precisely.** I reasoned from the leading-order comparison
`d^34/34!` against `c . d^28/28!`, which crosses at `d^6 ~ 9.7e8 . c`, and
guessed `c` small. That is the right asymptotic and the wrong regime: at
`d <= 30` neither sequence is anywhere near its leading term, and `SI` *gains*
on the source for the first thirty degrees before losing. Using an asymptotic
formula in a range where the asymptotics have not started is the same error in
kind as session 28's — transferring a pattern from the regime where it was
observed to one where it was not. Two sessions running.

**Kill criteria.** Criterion 1 does not fire: `a <= m_det <= g` holds at all 68
length-5 weights with `a > 0` and `delta <= 7`, so the quiver bound is
consistent with every certified `mult = a`. Criterion 2 does not fire: the
Kronecker and Molien routes agree exactly at every `delta <= 6`. Criterion 3 is
not reached (no six-nodal counterexample; the identification survives as a
component statement).

## 3. What was actually established

1. **A structural identification worth keeping.** `dim SI^tau_{(d,d)} =
   sum_{ell(lam) <= 5} m_det(lam) dim S_lam(C^5)`. The Peter–Weyl count that has
   run through this programme since session 24b *is* the transpose-invariant
   semi-invariant count of the 5-arrow Kronecker quiver at `(3,3)`. That is a
   genuine dictionary entry, and it explains why `m_det` and not something
   larger is the right ceiling.
2. **`SI_{(1,1)} = Sym^3 C^5`**, so `C[D_5]` is exactly the subring of `SI^tau`
   generated in the lowest weight — the object is correctly identified, with no
   hidden degree-1 semi-invariants.
3. **Exact `SI` dimensions** at `delta = 1..100` by a route (Kostant + weighted
   contingency counts) that shares nothing with the Kronecker one, agreeing with
   it wherever both are affordable.
4. **`D_5` is an irreducible component of the six-nodal closure**, proved.
5. **The negative:** the dimension route cannot reach `delta_0`.

## 4. Honest boundary

- **Proved:** the dictionary (D1)–(D4); `SI_{(1,1)} = 35`; the `m_det`
  identification; the `delta = 2` cokernel; the six-nodal component statement.
- **Exact computation, two agreeing routes:** `SI` at `delta <= 6`; `SI` alone
  out to `delta = 100`.
- **Extrapolated and labelled:** the crossover figures 145 and 120. The
  *rigorous* content is only that the crossover exceeds 100 — which already
  suffices, since 80 is known.
- **Assumed, not verified:** that `dim SI^tau / dim SI` settles near `1/2`. It
  runs `0.91, 0.79, 0.69, 0.63, 0.58` at `delta = 2..6`. Only the `145` figure
  is free of this.
- **Not done:** Derksen–Weyman proper — Schofield semi-invariants `c^V`, the
  saturation theorem, Horn-type inequalities. I used Cauchy/Kronecker and a
  Kostant alternating sum instead. That machinery would give *generators* and
  the support of the weight semigroup; it would not change §1's conclusion,
  which is about dimensions, and the dimensions are now known exactly.
- **`delta_0` unchanged:** `8 <= delta_0 <= 80` given the published deficit
  sequence, `6 <=` unconditionally. This session moved neither end.
- **Session 28's residue** (3 units of ambient room at `delta = 6`, 80 at
  `delta = 7`) is untouched here and still open.

## 5. What to do next

The session's own conclusion is that the counting routes are exhausted. Ranked:

1. **A low-degree covariant vanishing on six-nodal quinary cubics.** This is now
   clearly the only live route to `delta_0`. If the six-nodal locus is
   irreducible then `I(D_5)` is its ideal, and multi-node discriminants have
   classical literature (GKZ). Settling irreducibility of that locus is the
   gateway question and is a well-posed piece of classical geometry.
2. **Decide whether `delta_0` is worth the effort at all.** What the paper needs
   is that Theorem 6's length bound is *sharp*, and session 28 proved that with
   the discriminant. The exact first degree is a refinement, not a gap. On the
   evidence of sessions 28 and 31 — two sessions, two refuted predictions, no
   movement in either end of the bracket — I would say the honest thing is to
   state the bracket in the paper and stop hunting.
3. If it is pursued anyway, the *only* remaining computational handle is direct
   measurement at length-5 weights from `delta = 8` upward, which needs a fast
   exact null-space at a few thousand columns. Session 28 tried and failed to
   build one; that is a well-defined engineering task, not a mathematical one.

## 6. Assets

    analysis/wk8_s31_si.py   the dictionary, both dimension routes (Kronecker
                             sums and the Kostant/contingency Molien count), the
                             Weyl dimension formula, and the crossover test
    docs/quiver_route.md     the dictionary, the cross-check, the crossover
                             negative, the six-nodal proposition
    results/PREREG_s31.md    pre-registration
