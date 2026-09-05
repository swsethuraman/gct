# Session 55 — Equations below degree 24: the census, and what it changes

Branch `s55-census`, off `main` at `eb8cecb37b0ee30d5be76ccbd816ee142618882c`
(sync baseline, rule 10). Pre-registration `results/PREREG_s55.md`, commit
`e7d43a8`, committed before any computation of this session.
Deliverables: `docs/equation_census.md` (the table and the per-row analysis) and
this report. Code `analysis/wk9_s55_*.py`; logs `results/logs/s55_*`. Every run
bounded by `timeout` and `ulimit -v`, pid recorded. Exact arithmetic throughout,
no floating point; ranks over `Q` with mod-`p` cross-checks at
`p = 2147483647` and `p = 1000003`, **except** the Hilbert-function computation
in `wk9_s55_sing.py`, which is mod `p` only (over two primes and two independent
pencils).

---

## 0. Verdict

**No construction producing equations for the determinantal locus below degree
24 at `n = 4` was found, and none below 9.** Fourteen rows examined; nothing
below 24 survives, and the one candidate that could still produce something —
s51's Fitting minors of a universal presentation map — has not been built yet.
This is a survey result and not a lower bound: no theorem of the form "no
equation of degree `< X` exists" is known for `I(D_r)` or for `Dual_{k,d,N}`, and
a search for one came up empty.

**24 is the exact floor of the dual-degeneracy family at `n = 4`.** This was the
brief's stated "best outcome" on the negative side. The argument needs *two*
facts, not one — the first draft of this report claimed it was "one rank" and
that was wrong:

- **containment**: the equations vanish on `D_r` only if `k >= dim X^*(det_4
  pencil at r)`, measured as `min(6, r-2)`;
- **non-vacuity**: `S_{lambda(k,4)} C^r = 0` unless `k <= r-3`.

For `r <= 8` these are incompatible and the family gives *nothing*. For `r >= 9`
the minimum is `3(6+2) = 24`. And `k = 5` is excluded actively, not by default:
`rank Hess = 8 > 7` at a determinantal pencil, so the `k = 5` module does not
vanish on `D_r`.

**The brief's framing of the gap is wrong, and the correct framing is worse.**
The LMR module has `ell(lambda) = 9` and is identically zero on `Sym^4 C^r` for
`r <= 8`. Our measured range `delta <= 9` is at lengths 5 and 6. So "24 against
`delta <= 9`" is not one gap in one cell; it is 24 at length 9 against 9 at
lengths 5–6, and no experiment the programme has run compares them. At the cells
we actually measure, the best known equation degrees are 300 (`r = 5`) and 661
(`r = 6`), and LMR contributes nothing at all.

---

## 1. What was measured

All four points live in `r = 10` variables. The first three are the committed
test set of `docs/brief_wording.md` §5; the generic quartic is a fourth control
added here, because a statistic that is degenerate at *every* quartic is vacuous
and §5 does not test for that.

| | `dim X^*` | `rank Cat_{2,2}` | `Cat_{1,3}` | Koszul `Λ^1` |
|---|---|---|---|---|
| `det_4` pencil | **6** | **36** | 10 | 99 |
| generic quartic | 8 | 55 | 10 | 99 |
| `l·c`, `c` generic | 8 | 20 | 10 | 99 |
| `x_0·per_3`, ten variables | **7** | **18** | 10 | 99 |

Read across the two middle columns: **the same test set passes the check for one
statistic and fails it for the other.** The dual dimension is strictly smaller at
the determinant (6 < 7), so the dual-degeneracy family separates. The
catalecticant rank is much *larger* at the determinant (36 > 18), so every
flattening minor that vanishes on `D_r` also vanishes at the padded permanent.
The §5 pre-check is not a formality; here it kills one family in one column and
clears another in the next.

Supporting measurements:

- `rank Hess(det_4)(M)` = 16, 8, 4, 0, 0 for `rank M` = 4, 3, 2, 1, 0, identical
  on 12 draws per stratum. This is a **proof** for the whole stratum, not a
  sample: `rank Hess(det_4)` is constant on `GL_4 × GL_4` orbits and each rank
  stratum is one orbit. Every point of `{det A(s) = 0}` has `rank M <= 3`, so the
  LMR rank condition holds at every point of the hypersurface — which is what the
  divisibility needs, and not merely at generic points.
- `dim X^*(det_4 pencil)` by `r`: 3, 4, 5, 6, 6, 6, 6 for `r = 5..11`, against the
  generic `r-2`. First non-vacuous at `r = 9`. Independently confirmed at
  `r = 9..12` by a second route that uses no Hessian at all — the Gauss map is
  `(z,w) ↦ [z^T A_a w]`, a linear projection of the Segre cone of rank-1 `4×4`
  matrices, of rank 7. That route is valid only for `r >= 9`, where the
  admissibility conditions on `s` are solvable for every `(z,w)`.
- The 3×3-minor ideal on a random 5-dimensional pencil has Hilbert function
  `19, 20, 20, 20, …` at two primes with a different pencil each: a
  zero-dimensional singular scheme of **length 20**. At a constructed rank-2
  point of such a pencil the gradient vanishes and the projective Hessian has
  rank exactly `r-1 = 4` at four seeds — an **ordinary node**. So the
  discriminant, of degree `5·3^4 = 405`, vanishes on `D_5`. At `r = 4` the length
  is 0 and it does not.
- `|lambda(k,d)| = (k+2)d(d-1)` verified symbolically, so `delta = (k+2)(d-1)`.
  LMR's printed `n = 3` instance `(19,7,2^5)` at `delta = 12` reproduces; the
  `n = 4` instance `(65,17,2^7)` at `delta = 24` is derived from the same formula
  and is not printed in the paper.

*A sampling defect found in the verification pass and fixed.* `rank Hess(per_3)`
on `{per_3 = 0}` is 9 at a general point and drops to 8 at points with a zero
coordinate. The first run drew coordinates from `[-6,6]` and returned rank 8 on
17 of 40 draws; one seed in the genericity table reported `dim X^*(pad) = 6`,
which as printed would have *failed* the §5 check. Re-sampled with all
coordinates nonzero: **40 of 40 give rank 9**. The dual dimension is the value at
a general point, i.e. the maximum of a lower-semicontinuous function, so 7 is
correct — but the first draft cited a log that contradicted its own headline half
the time, and that has been corrected rather than left to be found later.

---

## 2. Four things that are new, in order of how much they should change plans

**(a) The equation degree falls as `r` grows, and the programme measures at small
`r`.** Collecting the census by cell:

| `r` | 4 | 5 | 6 | 9, 10 |
|---|---|---|---|---|
| best known equation degree | **320112** (exact — the ideal is principal) | 300 | 661 | **24** |
| LMR available? | no | no | no | yes |
| our measured `delta` | — | `<= 9` | `<= 9` | nothing measured |

Cheap equations live where we cannot measure, and the cells we can measure are
exactly the ones where the equations are most expensive. That is the real shape
of the difficulty, and it is not what the brief's single-column table conveys.

**(b) The padded permanent is already dual-degenerate, and the separating window
is one step wide.** For `P = l·q` with `l` a variable not occurring in `q`, the
Hessian on `{q = 0}` is singular identically: in block form
`H = [[0, g^T],[g, l·K]]` with `det[[0,g^T],[g,M]] = -g^T adj(M) g`, Euler gives
`K x = (deg q - 1) g` and `g·x = (deg q) q(x) = 0`, so the bordered determinant
vanishes. **Every padded form has dual defect at least 1, with no hypothesis on
`q`.** Measured: rank 9, never 10, in 40 of 40 clean draws.

Consequence: `l·per_3` sits in `Dual_{7,4,10}` and not in `Dual_{6,4,10}`, while
`D_10 ⊆ Dual_{6,4,10}`. **Only `k = 6` separates.** `k = 7`, at degree 27, does
not. The dual-degeneracy family has exactly one usable member at `n = 4`, it is
the cheapest one, and the margin is a single step in `k`. Carry this into s50:
there is no slack to trade degree against safety.

**(c) A correction to `docs/excess_singularity.md`, which is more consequential
than the cross-reference fixes in §4.** That document extends Proposition D from
Macaulay minors to *"anything that reads 'the singular locus is bigger than
expected': **Hessian-rank conditions**, Jacobian-ideal Hilbert-function
conditions, Milnor-number conditions"*, on the ground that any functional
monotone in `dim (S/J_F)_d` inherits the inequality. **The clause "Hessian-rank
conditions" is too broad, and row 1 of the census is the counterexample.** The
LMR/Mignon–Ressayre condition is a rank of the Hessian *matrix evaluated at
points of the hypersurface*; it is not a functional of the Milnor algebra and is
not monotone in it. Measured: determinant 8, padded permanent 9 — the inequality
runs the *opposite* way. Only the generalising clause needs narrowing, to
"functionals monotone in `dim (S/J_F)_d`", which is exactly what the
proposition's own proof gives. The Macaulay-minor and Milnor-corank statements
are untouched.

**(d) The flattening family is closed, and the number 37 is the new part.** The
*direction failure* is not new — it is s35's, proved: `docs/theory_directions.md`
§B(a) shows `rank Cat_{2,2}(l·c) <= 2r` because the second partials of `l·c` lie
in `l·V + span{∂_j c}`. Measured here at `r = 10`: exactly 20, and 18 at
`l·per_3`. What is new is the determinant side — `rank Cat_{2,2}` is 36 at a
`det_4` pencil for every `r >= 8`, full rank below — so the smallest flattening
minor vanishing on `D_r` has size **37**, first non-vacuous at `r = 9`. That
number appears not to be in the record. It is above 24, and it fails the §5 check
at 36 against 18, so the family is closed on both counts. `Cat_{1,3}` (rank 10
everywhere) and the Koszul flattening `Λ^1` (rank 99 everywhere, universal corank
at least 1) detect nothing at all.

---

## 3. Pre-registration scorecard

| # | logged at `e7d43a8` | prior | outcome |
|---|---|---|---|
| M1 | `delta = 24`, the printed `n(n-1) = 12` is a typo | 0.90 | **HIT** — `|lambda| = (k+2)d(d-1)` symbolically; the published `n=3` instance reproduces |
| M2a | `rank Hess` = 8 at a `det_4` pencil | — | **HIT** |
| M2b | 10 at a generic quartic | — | **HIT** |
| M2c | 2 on `{l=0}`, 10 on `{c=0}` | — | **HIT** |
| M2d | 2 on `{x_0=0}`, **10** on `{per_3=0}` | 0.85 (pair) | **MISS — 9.** The direction conclusion survives and is sharpened: the margin is 1, not 2, and the padding identity in §2(b) is the reason |
| M2e | minimal `k` = `dim X^*(det)`, family floor `3(k+2)` | 0.80 | **HIT on the value, MISS on the argument** — the containment bound alone does not give 24; non-vacuity `k <= r-3` is needed and was not in the pre-registration |
| M3 | `Cat_{2,2}` = 55 / 36 / 20 / 18 | 0.70 (quadruple) | **HIT**, exact quadruple. `Cat_{1,3}` was pre-registered, initially skipped, and measured in the verification pass: 10 everywhere |
| M4 | exactly 20 nodes at `r = 5` | 0.85 | **HIT** for length 20; node-ness was not pre-registered as a separate measurement and was added in the verification pass |
| M5 | Plücker row: estimate, plus the superseded-draft correction | — | **delivered** as §7 of the census; no computation, as pre-registered |
| S1 | nothing below 24 will be found | 0.85 | **HIT** |
| S2 | 24 shown to be the exact family floor | 0.80 | **HIT** (see M2e on the argument) |
| S3 | the Cayley–Bacharach row will not survive | 0.75 | **HIT** |
| S4 | the flattening row fails on *direction*, not degree | 0.70 | **HIT**; and the mechanism turns out to be banked at s35 |
| S5 | LMR identically zero for `r <= 8`; different cell from `delta <= 9` | 0.60 | **HIT**, two independent routes |

Two misses, and both were productive. M2d — predicting rank 10 at the padded
permanent and measuring 9 — is what exposed the padding identity and the
one-step separating window. M2e is the more instructive: the pre-registered
argument for the floor was incomplete, and an adversarial pass on the first draft
of the census caught it. The first draft asserted `D_r ⊆ Dual_{k,4,r}` iff
`k >= 6` for all `r`, which its own table contradicted at `r = 5,6,7`.

---

## 4. Corrections to the record

Flagged, not edited — none of these files is mine to write.

1. **Every brief in the batch cites `docs/brief_wording.md` §6 for the
   degeneracy-direction pre-check. It is §5.** Counted: s49 twice, s50 once,
   s51 once, s52 once, s53 once, s54 once, s55 twice — nine occurrences, all
   wrong. §6 of the committed file is the citation-corrections section; §7 is
   the functoriality pre-check. The single correct citation in the batch is
   `docs/s51_prompt.md` §4b(3), which says §5. Worth a one-line fix across all
   seven before the other workers hit it.
2. **The standing table row "Landsberg–Manivel–Ressayre | 24" needs "for
   `r >= 9`; identically zero for `r <= 8`."** As printed it invites exactly the
   comparison §0 shows is not available.
3. **Candidate 3 of the brief ("Landsberg–Ressayre Cayley–Bacharach") should be
   struck**, and replaced by Alper–Bogart–Velasco with an explicit note that it
   yields a bound and not equations.
4. **Candidate 6 rests on a superseded draft.** The committed
   `docs/s53_prompt.md` has no common-isotropic-4-plane route;
   `docs/critic_e7_response.md` §5 records the isotropic statement as a corollary
   of ABV and asks to deprioritise `I_2`. `I_1(B_9) = I_1(B_10) = 0` remains
   unreproduced in this repository.
5. **`docs/excess_singularity.md`: the clause "Hessian-rank conditions" in the
   extension of Proposition D is refuted** — see §2(c). This is the substantive
   one.
6. **`docs/s53_prompt.md` §6 has an off-by-one: `dim D_10 <= 128` should be
   `<= 129`.** The group `{(P,Q) : det P det Q = 1}` has dimension 31 but acts
   with a one-dimensional kernel `(lambda I, lambda^{-1} I)`, so the effective
   fibre dimension is 30 and `dim D_r <= 16r - 30` as an affine cone — the
   convention `docs/n4_gate.md` §4 already uses for `dim D_5 = 50`. So
   `dim D_10 <= 130` affine, `<= 129` in `P^714`. (Equality needs the
   finite-stabiliser argument that `docs/e4_hunt.md` flags as unwritten; this
   session does not supply it.) The stopping-rule arithmetic in that brief is
   unaffected; the baseline it measures against is.
7. **A naming collision worth a footnote somewhere permanent.** "Degree 24"
   already means something else here: `Phi_24`, the second generator of the
   invariant semigroup of `det_3` (`results/results_deg24.md`,
   `docs/degree24_extension.md`). It has nothing to do with LMR's degree-24
   equation module for `det_4`. Two sessions from now this will cost someone an
   hour.
8. **`docs/theory_directions.md` §(d) says "nothing in this family goes below
   300"** for the Macaulay minors at `r = 5`. That remains right, and the s49
   correction happens to leave 300 unchanged because `rho_7 - 1 + 1 = 300`; the
   coincidence should not be read as the correction not applying (it moves
   `666 → 661` at `r = 6`).

---

## 5. Honest boundary

- **Re-derived here:** the LMR degree formula and its published `n = 3` instance;
  the length of the weight; the dual-dimension lemma; every rank in §1; the GKZ
  and Giambelli–Thom–Porteous degrees, the latter anchored on two Segre degrees;
  `rho_d` and the ambient dimensions in the Macaulay rows; the `817199`
  naive-ideal-membership figure; the Cramer cost of the binary division.
- **Proved, not merely sampled:** `rank Hess(det_4)(M) <= 8` on the whole rank-3
  stratum, by orbit-constancy.
- **Quoted, not re-derived:** `R_S(det_4) >= 38` (Farnsworth); the `d = 8`
  Macaulay drop of 50, back-solved from the repository's own 1148; the degree
  320112 (Leal–Lozano Huerta–Vite). **The first draft of the census claimed
  320112 was "confirmed twice from different directions"; it is not.**
  `docs/e4_hunt.md` labels its own value "adopted, not certified" and adopts it
  from the same literature, so this is one source, not two.
  Bürgisser–Ikenmeyer–Panova's `n >= m^25` is quoted.
- **Not established, and not claimed:** that 24 is a lower bound on the onset of
  `I(D_r)`. §2 of the census bounds *one family* from below. A search for a
  theorem of the form "no equation of degree `< X` exists" for the
  Mulmuley–Sohoni variety or for `Dual_{k,d,N}` found nothing; on the evidence
  gathered this looks open, and absence of search hits is not proof.
- **Not measured:** a general Young flattening. Three members of the family were
  measured (`Cat_{2,2}`, `Cat_{1,3}`, Koszul `Λ^1`) and the border-rank route was
  bounded by citation. Whether some exotic Young flattening has rank at
  `l·per_3` exceeding its rank at a determinant is **unknown**; s35's proved
  bound `rank Cat_{2,2}(l·c) <= 2r` argues against it for the catalecticant, and
  nothing suggests it elsewhere.
- **Not checked:** `I_1(B_9) = I_1(B_10) = 0`. Out of scope for a census, and
  already flagged for independent reproduction elsewhere.
- **Method boundary:** every rank is exact over `Q` with two mod-`p` checks,
  except the Hilbert function of the 3×3-minor ideal, which is mod `p` only (two
  primes, two independent pencils). The corank-1 statement for the Koszul
  flattening is proved in the `>= 1` direction and measured in the `= 1`
  direction.

---

## 6. What this changes

The brief said: "If a documented argument says nothing can go below 24, the
measured range and the equation range never meet by this route, and the
programme's shape has to change accordingly." That is where we are, with one
refinement — the two ranges are further apart than the table suggested, because
they are not in the same cell.

1. **s50 is now the whole of the dual-degeneracy line, and its margin is one
   step.** There is no cheaper member of the family and no safer one. The census
   hands s50 two usable facts: the rank condition holds at *every* point of the
   determinantal hypersurface, proved by orbit-constancy, which is what its
   divisibility test needs; and `rank Hess(l·per_3)` on `{per_3 = 0}` is 9 at a
   general point, so **the remainder it computes at control 4 must be nonzero.**
   That is a pre-registered prediction from this session, not a hope. Its control
   3 (`l·c`) should also be nonzero, at `dim X^* = 8`.
2. **s51 is the only route that could still go below 24**, and the census
   sharpens its acceptance test: whatever rank condition it produces must be
   evaluated at the four points of §1 *before* the Fitting degree is computed.
   Rows 5, 6 and 12 of the census all died at exactly that step, and each cost a
   session.
3. **The obstruction-by-multiplicity line should be re-scoped by `r`, not by
   `delta`.** Everything cheap lives at `r >= 9`, where the equations exist and
   the multiplicities are unreachable; everything reachable lives at `r <= 6`,
   where the cheapest equation is 300. Deciding which side to attack is a
   different question from pushing `delta` from 9 to 10, and it is the question
   the census says is now on the table.
