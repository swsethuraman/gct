# Session 26 (2026-08-31) — the `a = 2` lemma, and the first live cells

Branch `s26-tworank`, cloned fresh from public `origin/main`.
**Tip at clone: `3dfd524`.** The brief names `a3df8ba`; `3dfd524` is one commit
*above* it — the integrator's own correction to the two briefs, committed an
hour after them — with `a3df8ba`, `c9240f3`, `ad9502f` all present beneath in
the stated order. **This is not a rollback alarm**, and the in-repo copy of the
brief already carries the corrected text. Branched from `3dfd524`.

Container only; `Projects\gct` not owned and not written (rule 9). No engine, no
checkpoints, no long runs. Deliverables: `docs/isotypic_rank.md` (the lemma and
the theorem), `docs/live_cells.md` (the measured cells), this record,
`analysis/wk6_s26_*.py`, `results/PREREG_s26.md`.

---

## 1. Headline

**All five cells fill the room, and there is a theorem underneath saying they
had to.**

    lam        delta   a   m_det   mult_det   def_det   mult_per
    (12,6)       6     2     2        2          0         2
    (15,6)       7     2     2        2          0         2
    (9,4,2)      5     2     3        2          1         2
    (12,4,2)     6     2     3        2          1         2
    (13,6,2)     7     3     4        3          1         3

> **Theorem.** `mult_lam C[closure(GL_9 . det_3)]_delta = a(lam, delta)` for
> every `lam` with `ell(lam) <= 4`, at every degree — hence
> `def_det = m_det − a` there. For `per_3` the same holds up to
> `ell(lam) <= 5`. Both length bounds are sharp, and both are set by one
> number: `dim Stab`, which is 16 for `det_3` and 4 for `per_3`.

Two further things fell out:

- **The ideal of `closure(GL_9 . det_3)` is zero in every degree `<= 7`.** The
  paper records this for degrees `<= 4`; this extends it by three.
- **A restatement worth keeping.** For `ell(lam) = r`, the length-`r` stratum of
  `C[closure(det_3)]` *is* the coordinate ring of `D_r`, the variety of `r`-ary
  cubics admitting a `3x3` linear determinantal representation. The deficit at
  short weights is therefore not about the boundary at all; the first length at
  which it can be is `r = 5`, where `D_5` has codimension 6 in `Sym^3 C^5`.

## 2. How it was done

The pre-registration derived, by hand and before any computation, the two steps
that made the session cheap:

1. **The rank lemma, with the dualisation removed.** `mult = a − dim{u :
   sum_k u_k h_k vanishes on the orbit}`, with `h_1..h_a` a basis of the
   highest-weight vectors of weight `lam` in `C[W]_delta`. The `h_k` are
   explicit polynomials in the coefficient coordinates; their torus weights are
   read off their monomials; they are evaluated at explicit orbit points.
   `S_lam` and `S_lam^*` never appear, so session 23's flagged bookkeeping
   hazard cannot arise. (The Borel convention is pinned three ways, §5.)
2. **The short-weight reduction.** Every degree-3 exponent vector has
   *non-negative* entries, so a weight vector of weight of length `r` can only
   involve coefficients supported on `r` variables, and therefore sees
   `g.det_3` only through `det(s_1 A_1 + ... + s_r A_r)` for an arbitrary
   `r`-tuple of `3x3` matrices. The whole question collapses to: **are the
   determinantal `r`-ary cubics dense?**

They are for `r <= 4` — exactly at `r = 2` (every binary cubic splits into
three linear forms, hence is a determinant of a diagonal pencil), classically at
`r = 3, 4`. Measured Jacobian ranks of `(A_i) -> f(sum s_i A_i)`, exact, at
random integer points:

    r        2    3    4    5    6        target C(r+2,3)
    det      4   10   20   29   38        4, 10, 20, 35, 56
    per      4   10   20   35   50

and the two deficiencies are precisely the stabiliser dimensions:
`29 = 45 − 16`, `38 = 54 − 16`, `50 = 54 − 4`. The naive count is attained with
no extra degeneracy anywhere. A full Jacobian rank at one point *proves*
dominance (rank is lower semicontinuous), so the positive half of the theorem
is rigorous; the negative half is rigorous too, since the group action bounds
the rank above by `9r − dim Stab` at every point and the measurement attains
that bound.

**Independent confirmation of session 24b's correction.** That session recorded
that the paper's §4 says `dim Stab(det_3) = 17` where the vector stabiliser is
16, and recommended `17 -> 16`, `31 -> 30`. The rank deficiencies above measure
that dimension directly and geometrically — `45 − 29 = 16`, `54 − 38 = 16` —
from a computation that shares nothing with session 24b's. **The correction is
confirmed by a second, independent route.**

## 3. Prediction ledger

| # | pre-registered | outcome |
|---|---|---|
| Q1 | `mult_det = 2` at both two-row cells | **HIT** (F1 not fired) |
| Q2 | `m_det = 2` and `def_det = 0` at both; deficit **not** expected nonzero | **HIT** (F2 not fired) |
| Q3 | rank reaches `a` at `a` points and does not rise after | **HIT** — `1,2,2,…` and `1,2,3,3,…` exactly |
| Q4 | the full five-cell table `mult = a`, `def = 0,0,1,1,1` | **HIT** (F4 not fired) |
| Q5 | `a <= m_det` for every `ell(lam) <= 4` — the sharpest falsifier | **HIT**: 172 weights, 0 violations, tight at 59 (F5 not fired) |
| Q6 | `mult_per = a` at all five; permanental Jacobian rank 10 at `r = 3` | **HIT**, and better than predicted: `per` stays dominant to `r = 5` (F6 not fired) |
| Q7 | the total-deficit identity continues to `141, 618, 2488` | **HIT** at all three (F7 not fired) |
| Q8 | length 5 is where the argument stops; `r = 4` still dominant | **HIT**: `r=4` rank 20 = target, `r=5` rank 29 < 35 (F8 not fired) |

Eight for eight. That is a worse sign than it looks — see §4.

**Kill criteria.** Criterion 1 **fires**: `mult_det = 2` at both two-row cells,
so the `a = 2` stratum at `n = 3` is closed — and closed far beyond the
criterion's scope, at every weight of length `<= 4` and every degree. Criterion
2 does not fire: the method reproduces the paper wherever the paper already
knows the answer (all 20 weights with `a > 0` and `delta <= 4`). Criterion 3
does not fire: no full deficit with room available.

## 4. The honest reading, which is not the flattering one

Every prediction hit, and that is because **the cells could not have come out
any other way.** All five have `ell(lam) <= 3`, and the theorem covers
`ell(lam) <= 4`. The brief chose them for cheapness — "two-row weights in a
plethysm of a cubic are the classical transvectant case, constructible by hand"
— and cheapness is exactly what the theorem's hypothesis measures: short
weights are cheap *because* they see only a few variables, and they are
guaranteed *because* seeing only a few variables means seeing a cubic that is
always determinantal. **The selection rule and the triviality condition were
the same condition.** The five numbers are worth little; what they were worth
is that computing them forced the reduction that produced the theorem.

The integrator's stated prior — "no confident prior; `closure(det_3)` has
dimension 65 inside a 165-dimensional ambient, so its ideal is large and
`mult_det < a` is entirely possible" — is right about the ideal and wrong about
where to find it. The ideal *is* large; it is simply invisible at short
weights, because a highest-weight vector of length `r` is blind to all but `r`
of the nine matrix coordinates, and in `r <= 4` coordinates a generic cubic is
determinantal.

## 5. Honest boundary

- **Proved outright, no computation:** Lemmas 1–4 and Proposition 5 of
  `docs/isotypic_rank.md`; the `r = 2` density; Corollary 7 (`a <= m_det` for
  short weights) as a consequence of the theorem.
- **Proved with a computation that is a certificate, not a sample:** every
  measured `mult`. The rank matrix is a rigorous *lower* bound for any finite
  point set, and `mult <= a` is a rigorous upper bound, so a measured rank equal
  to `a` is a proof. Every rank in this session attained `a`. No probabilistic
  step enters any reported number.
- **Proved modulo a classical citation:** the `r = 3, 4` density is quoted
  (Dickson; Grassmann) *and* independently confirmed here by exact Jacobian
  rank, so the citation is not load-bearing.
- **Orientation.** Pinned by construction (nothing is dualised) and checked
  three ways: the highest-weight multiset matches the symmetric-function
  plethysm on 322 weights and `scripts/ambient_screen.py` on 1190; `m_det`
  reproduces the published row sums `3, 11, 43` and `m_det((2,2,2)) = 1`; and
  the measured multiplicities reproduce the published total-deficit sequence.
  All three would visibly fail under the opposite Borel.
- **Not proved.** (i) That the ideal actually *does* bite at length 5 — only
  that the `mult = a` argument stops there. (ii) The degree-`<= 7` vanishing of
  the ideal at the *long* weights past the compute cap: 16 units of ambient room
  at `delta = 6` and 96 at `delta = 7` were not measured directly and are
  carried by the published total-deficit sequence. That residue is pure compute,
  not new mathematics, and everything measured agrees with it.
- **The screen was used only as a cross-check.** My own `a` and `m_det` were
  written and validated against each other first (three routes for `a`, and a
  fresh derivation of both halves of the symmetric-Kronecker formula for
  `m_det`); `scripts/ambient_screen.py` was called afterwards and agrees on all
  1190 weights with `delta <= 7`. No disagreement to report.

## 6. Paper: recommended, NOT made

**No edit to `paper/det3-conductor.tex` was made on this branch.** Session 23
edited the paper because the paper contained something false; nothing here
does. What is here is additive, and the paper is in submission preparation, so
the integrator should decide. The three candidates, in order of value:

1. **The length-`<= 4` theorem**, with the two-line reduction. It converts the
   deficit at every short weight into `m_det − a`, a difference of a symmetric
   rectangular Kronecker coefficient and a plethysm coefficient, computable in
   milliseconds and with no geometry in it. It also explains, in one number,
   why the determinant has filled every ambient slot the programme has looked
   at: `dim Stab = 16`.
2. **The degree-`<= 7` vanishing of the ideal**, upgrading the current
   degree-`<= 4` remark — with the caveat in §5(ii) stated.
3. **The `det`/`per` crossover at lengths 4 and 5.** The permanent fills *more*
   of the ambient than the determinant does, one length further, and for the
   structural reason that its stabiliser is smaller. Given how much of the
   programme's recent work has been about `m_per > m_det`, a place where the
   permanent's smaller symmetry group makes its closure ring *larger* is worth
   a remark.

Also: this session independently confirms session 24b's `17 -> 16` /
`31 -> 30` correction to §4 (see §2).

## 7. What to do next, and what not to

**Do not** pick the next cell by cheapness. That heuristic is precisely
anti-correlated with informativeness here.

1. **Length exactly 5, `delta >= 8`, smallest weight with `a >= 2`.** This is
   the first place the determinant's ideal can contain anything. By Proposition
   5 it is a question about `D_5`, the quinary determinantal cubics — a
   29-dimensional variety in a 35-dimensional space, codimension 6 — and its
   ideal is a concrete, small, classical object worth identifying directly. The
   equations of `D_5` are probably more interesting than any single cell.
2. **The length-5 `det`/`per` comparison.** At length 5 the determinant's ideal
   is live and the permanent's is still empty, so this is the first family of
   weights where the two closure rings can differ for a structural reason.
3. **Finish the ledger residue** (§5(ii)): 16 units at `delta = 6`, 96 at
   `delta = 7`. Pure compute — a faster modular kernel would clear it.
4. **`n = 4` is already measured, and it is more favourable than `n = 3`.**
   The same reduction and the same Jacobian rank give the crossover at every
   `n` (`docs/isotypic_rank.md`, Theorem 6'):

       n        det_n dense up to      per_n dense up to
       2        r = 4                  r = 4
       3        r = 4                  r = 5
       4        r = 3                  r = 5

   At `n = 4` the determinant's ideal is live from **length 4**, while the
   permanent's is provably empty through length 5. So lengths 4 and 5 at
   `n = 4` are the first weights anywhere in this programme where the two
   closure rings can differ for a structural reason rather than an arithmetic
   one — and the ambient census there is cheap. That is a far better target
   than any further `n = 3` cell, and it needs no engine.

## 8. Assets

    analysis/wk6_s26_core.py     partitions, MN characters, m_det (symmetric
                                 rectangular Kronecker, both halves rederived),
                                 and TWO independent routes to a(lam,delta)
    analysis/wk6_s26_hwv.py      weight-targeted monomial enumeration, raising
                                 operators, the highest-weight kernel, exact
                                 evaluation at det/per of a matrix pencil, and
                                 two implementations of the rank measurement
    analysis/wk6_s26_density.py  Jacobian ranks: where D_r is everything
    analysis/wk6_s26_sweep.py    the degree-by-degree ledger
    docs/isotypic_rank.md        the lemma, the theorem, the algorithm
    docs/live_cells.md           the five cells and the ledger
    results/PREREG_s26.md        pre-registration
