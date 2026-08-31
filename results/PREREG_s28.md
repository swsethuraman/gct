# PRE-REGISTRATION — `D_5`, and making the length theorem sharp (session 28)

Committed **before any new computation** in this session. Branch `s28-d5`,
cloned fresh from public `origin/main`.

**Tip at clone: `1203fe4`** ("Integrator review of sessions 25 and 26"). The
ancestry check passes: `6aaab97` **is** an ancestor of `HEAD`, and `1203fe4` is
the only commit above it. No rollback alarm.

Calibration run before writing this file (the brief's §4):
`analysis/wk6_s26_regress.py` — **all checks passed in 17 s**, including the
`delta = 2..7` deficit identity `1, 6, 31, 141, 618, 2488`, the Jacobian tables
`det: 4,10,20,29,38` and `per: 4,10,20,35,50`, and `mult = a` at all five
session-26 cells.

Date: 2026-08-31.

---

## 1. What is already derived, by hand, before this commit

### 1.1 The `r >= 3` correction (task A) — not a prediction, a fix

`docs/isotypic_rank.md` §4 states `dim D_r <= min( C(r+2,3), 9r − 16 )`. The
integrator is right that this is false at `r = 2`. The correct statement and
its proof:

> Let `(A_1..A_r)` be generic, so `A_1` is invertible; normalise `A_1 = I` by
> replacing `A_i` with `A_1^{-1} A_i`. A stabiliser element `(P,Q)` with
> `det P det Q = 1` satisfies `P A_1 Q = A_1`, i.e. `Q = P^{-1}`, and then
> `P A_i P^{-1} = A_i` for `i >= 2`. So `P` lies in the commutant of
> `{A_2,...,A_r}`.
> - For `r >= 3`: two generic `3x3` matrices generate `M_3` as an algebra, so
>   the commutant is the scalars, the stabiliser is finite, the orbit is
>   16-dimensional, and `dim D_r <= 9r − 16`.
> - For `r = 2`: a single generic matrix has a 3-dimensional commutant (2
>   dimensions mod scalars), the orbit is 14-dimensional, and the bound reads
>   `18 − 14 = 4` — exactly the measured rank, and consistent with the
>   elementary proof that `D_2` is everything.

So the bound is to be stated **for `r >= 3`**. Nothing downstream changes: every
use of it is at `r >= 3`, and `r = 2` is proved directly.

### 1.2 `I(D_5)` has no isotypic component of length `<= 4`

A highest-weight vector of weight `mu` with `ell(mu) = k <= 4` inside
`C[Sym^3 C^5]_delta` involves only coefficients supported on `k` of the five
variables (the same non-negativity argument as Lemma 3), so it sees a point of
`D_5` only through its restriction to a `k`-plane — and that restriction ranges
over `D_k`, which is everything for `k <= 4`. So no such vector vanishes on
`D_5`. **`I(D_5)` is concentrated at weights of length exactly 5.**
Consequently tasks B and C are the *same* computation: the lowest degree of
`I(D_5)` is the smallest `delta` at which some length-5 weight has
`mult < a`.

### 1.3 An arithmetic sufficient condition for the ideal to bite — cheap

By Proposition 5, for `ell(lam) = 5`,
`mult_lam C[D_5]_delta = mult_lam C[closure(GL_9 det_3)]_delta`, and the latter
is at most `m_det(lam)` by Peter–Weyl. So

    a(lam, delta) > m_det(lam)  for some lam of length 5
        ==>  mult_lam < a(lam,delta)  ==>  I(D_5)_delta != 0.

This is a **proof** of biting, from two classical counts with no geometry in
them — a plethysm coefficient and a symmetric rectangular Kronecker
coefficient. Session 26 verified `a <= m_det` at *every* weight with
`delta <= 7`, which is why nothing bites there. So the search is: sweep
`delta = 8, 9, 10, ...` over length-5 weights for the first `a > m_det`.

The condition is sufficient, not necessary: the ideal could bite earlier at a
weight where `mult < min(a, m_det)` for a purely geometric reason. Both will be
tested.

### 1.4 What `D_5` is, geometrically (recorded before the literature pass)

`D_5 = closure{ det(s_1 A_1 + ... + s_5 A_5) }` is the variety of quinary
cubics with a `3x3` linear determinantal representation — equivalently the
restriction of `closure(GL_9 . det_3)` to a fixed 5-plane, equivalently the
cubic forms in 5 variables that are linear pullbacks of `det_3`. Two structural
facts I expect to matter:

- **Every member is singular.** For a `3x3` matrix `M(s)` of linear forms in 5
  variables, the rank-`<=1` locus is cut by the nine `2x2` minors, of expected
  codimension `(3−1)(3−1) = 4` in `P^4` — dimension 0, and by Giambelli of
  degree 6. At a rank-1 point every first partial of `det M` vanishes, so
  `det M` is singular there. So a generic member of `D_5` is a **cubic
  threefold with 6 nodes**, and imposing `k` nodes is `k` conditions — giving
  codimension 6, which is exactly `35 − 29`.
- **Smooth cubic threefolds are never determinantal**, by Grothendieck–Lefschetz:
  a smooth hypersurface of dimension `>= 3` has `Pic = Z<O(1)>`, so a rank-one
  ACM sheaf is `O(k)` and a linear determinantal resolution would force
  degree 1.

## 2. Predictions, with falsifiers

**P1 — the first bite.** The smallest `delta` at which some `lam` of length 5
has `mult_lam < a(lam,delta)` is **`delta = 8`**. Ranked alternatives if not 8:
**9**, then **10**. I predict the mechanism is the *arithmetic* one of §1.3 —
the first bite is at a weight with `a > m_det` — rather than a geometric drop
below `min(a, m_det)`.
*Falsifier F1: no length-5 weight with `mult < a` at `delta = 8, 9, 10`.*
*Reasoning, logged: session 26 found `a <= m_det` at all 172 length-`<=4`
weights with `delta <= 7` but with equality at 59 of them — the bound is
frequently tight, so the plethysm is already level with the Kronecker count and
should overtake it within a degree or two of the swept range. `delta = 8` is
the first untested degree.*

**P2 — the lowest-degree part of `I(D_5)`.** Its lowest degree equals the P1
answer, and the piece there is small: I predict **one or two** length-5 weights
carrying total multiplicity `<= 3`, not a large space.
*Falsifier F2: the lowest-degree piece carries multiplicity `> 3`, or sits at a
weight of length `< 5` (which would contradict §1.2 and would mean the
non-negativity argument is wrong).*

**P3 — is `D_5` classical?** I predict **yes as a variety, no as an ideal**:
determinantal cubic threefolds / 6-nodal cubic threefolds are classical, but I
do **not** expect a published generating set for `I(D_5)` in the `GL_5`-graded
form this programme needs. A literature pass will be made before computing, and
whatever it returns will be recorded whether or not it helps.
*Falsifier F3: a named classical generating set turns up, in which case my
computation should reproduce it and that becomes the check.*

**P4 — the residue (task D).** The 16 units of ambient room at `delta = 6` and
96 at `delta = 7` that session 26 left carried by the published sequence
**confirm** `mult = a`. I expect no bite at `delta <= 7`, and therefore expect
task D to remove Corollary 9's dependence on the published sequence rather than
to break it.
*Falsifier F4: any weight in the residue with `mult < a`. That fires the
brief's kill criterion 3 and stops the session — it would mean either the
engine or the rank algorithm is wrong, and it bears on the paper's
degree-`<= 7` claim.*

**P5 — a consistency check I will run either way.** If P1 lands at `delta = d`,
then `sum_lam (m_det − min(m_det, a))` must *stop* agreeing with the true total
deficit at `delta = d` if the mechanism is geometric, and must *continue* to
agree if the mechanism is arithmetic (because `min(m_det,a) = m_det < a` there
already accounts for it). Whichever happens is recorded.

## 3. Method, fixed in advance

- Calibration first (done, above); nothing new is trusted until
  `wk6_s26_regress.py` passes in this container.
- Exact arithmetic only. Ranks over `Q` and/or two distinct primes.
- The rank algorithm is the session-26 one, which is a **certificate** whenever
  the rank attains `a`: it exhibits `a` explicit integer points at which `a`
  highest-weight vectors are independent. A rank *below* `a` is only a lower
  bound on independence and therefore an upper bound on `mult`; to claim
  `mult < a` I need the *arithmetic* bound `mult <= m_det < a`, or a
  symbolic/large-sample certificate of identical vanishing. **I will not report
  a bite from a rank deficiency alone.**
- Literature pass before the `D_5` computation, per the brief.

## 4. What is NOT claimed, and what is not touched

`paper/det3-conductor.tex` is **not** to be edited — the X_-3 grind owns it.
`PROJECT_NOTES.md` and `docs/boundary_deficit.html` are not appended to.
`docs/isotypic_rank.md` is this line of work's own file and is corrected in
place (task A only).
