# Session 29 — where the ideals become visible

Branch `s29-visible`.  2026-09-01.  Fresh clone, container only, new files
only.  `paper/det3-conductor.tex`, `PROJECT_NOTES.md` and
`docs/boundary_deficit.html` untouched.  The 62 open cells at `delta = 6`,
`ell >= 5` were not touched (s30 owns them).

Deliverables: `results/PREREG_s29.md` (commit `b927b6c`, before any
computation), `docs/visible_ideals.md`, this record.

## 0. Clone state

`origin/main` at **`1203fe4`**; ancestry check passes.  Sessions 27 and 28 have
**not** landed — `docs/n4_gate.md` and `analysis/wk7_s27_*.py` are absent — so
the rank machinery was rebuilt from scratch as `analysis/wk8_s29_*.py` and
every session-27 fact used here was re-derived, not imported.
`analysis/wk6_s26_regress.py` is present.

## 1. The finding

**The isotypic rank algorithm's action rule is wrong, and could not have been
caught by any calibration the programme had.**  `docs/isotypic_rank.md` §1
states `E_ij c_alpha = alpha_j c_{alpha - eps_j + eps_i}`; that is the action on
the monomials `e^alpha` of `Sym^n V`, whereas the coefficient functionals are
`c_alpha = e^alpha / alpha!` and carry

    E_ij c_alpha = (alpha_i + 1) c_{alpha - eps_j + eps_i}.

The two differ by a diagonal rescaling, so `a` (a kernel *dimension*) is
identical under both and every `a` calibration passed; only the kernel
*vectors* differ, so only `mult` is affected — and **every `mult` the programme
has ever reported equals `a`**, the generic value, which a wrong basis
reproduces anyway.  The convention was therefore never under test.

Corrected, the algorithm passes a battery of 48 World A cells, **41 of them
with `mult < a`**, against session 24's closed forms — which were derived by
substitution ranks and Gaussian binomials with no highest-weight vector
anywhere, so the check is genuinely independent.

**Nothing previously published changes.**  Re-run under the fix: session 26's
five cells, the 20 weights at `delta <= 4`, the `a((delta^4),delta)` row and the
19-cell `delta = 5` gate all reproduce exactly.  Sessions 26 and 27 were right;
they were merely uncertified, and are now certified.  The repair to
`docs/isotypic_rank.md` is one line.

## 2. Prediction ledger

| | prediction | outcome |
|---|---|---|
| Q1 | first `mult_pad < a` at length 3, `delta = 3` (range `delta <= 4`) | **REFUTED** for the object it names.  `per_3^pad` has `mult = a` at *every* length-3 weight through `delta = 7` (all 135, complete) and every length-`<=3` weight through `delta = 5`.  The prediction is right only for the `m = 1, 2` members of the chain, which I had not registered it for |
| Q2 | `e >= 7`, against the integrator's `e = 6` | **UNTESTED** — part B not completed; see §5 of `visible_ideals.md`.  Recorded as untested, per the pre-registration, not as confirmed |
| Q3 | `U_det ⊆ U_pad`, and the chain version, both pass | **CONFIRMED** on **18 non-vacuous tests** (both subspaces nonzero); the det/pad tests are vacuous throughout, as pre-registered |
| Q4 | `D < 0` is the wrong direction and worth only calibration | recorded as registered; the calibration value was obtained from the `m = 1, 2` members instead |

One refutation and one untested.  The unregistered finding — the convention
error — is the session's actual result, and it was found only because Q1's
sweep forced me to look at a locus (`{l^3 m}`) whose answer session 24 already
knew independently.  **The lesson is procedural: a measurement tool whose every
output has been the maximum has not been tested.**

## 3. Verification

| quantity | route 1 | route 2 | independent check |
|---|---|---|---|
| `a` | raising-operator kernel dimension | symmetric-function plethysm | agree on all length-`<=4` weights, `n = 3, 4`, `delta <= 5` |
| `mult` | rank mod `2147483647` | rank mod `2147483629` | **48 World A cells (41 with `mult < a`) against session 24's closed forms** |
| `U` (ideal slice) | kernel of the evaluation matrix on a fixed basis of `ker R` | `dim U = a - mult` asserted at every cell | 18 containment tests |
| the chain | `mult_det >= mult_{m3} >= mult_{m2} >= mult_{m1}` asserted at every cell | — | no violation in 64 cells |

## 4. Three errors of mine, all caught

* **Blocked elimination.**  My first `(6^4)` solver applied the rank-`k`
  trailing update with panel pivot rows that had not been reduced among
  themselves.  It reported rank 11,588 where `a = 1` demands 12,651 — caught by
  the `a` self-check, which is why that self-check exists.
* **Sweep scoping.**  I filtered weights by `len(lam) == ELL` instead of
  `<= ELL`, which hid every short weight — including the `(4,4)` cell that
  turned out to carry the whole finding.  Caught by noticing that a
  codimension-10 locus was reporting no ideal anywhere, which is impossible.
* **`pkill -f` matched my own shell** and killed the compound command
  mid-patch (infrastructure rule 4, exactly as documented).  Recovered by
  re-applying the patch and killing by explicit PID thereafter.

## 5. Honest boundary

* The convention fix is verified on binary quartics (`r = 2`) and used at
  `r = 3, 4`.  The derivation is general and the `r = 3` chain results are
  internally consistent (the four-term chain never inverts in 64 cells), but
  the *external* check exists only at `r = 2`, where session 24's closed forms
  live.  A length-3 external check would need a closed form nobody has.
* Part A is a complete sweep at length exactly 3 through `delta = 7`, and at
  length `<= 3` through `delta = 5` only.  Length 4 was not swept at all this
  session.
* Part B is not done.  `e >= 6` is all that is established, exactly as at the
  end of session 27.
* The 18 containment tests are all of the form `U_{m=2} ⊆ U_{m=1}`.  The
  det/pad containment — the one the programme cares about — remains untested
  because both its subspaces are zero everywhere reachable.

## 6. Files added

    results/PREREG_s29.md          pre-registration, committed first
    docs/visible_ideals.md         the convention error, the sweep, the subspace tests
    docs/session_29.md             this record
    analysis/wk8_s29_core.py       the rank machinery (with the corrected rule)
    analysis/wk8_s29_pleth.py      plethysm, the independent route for `a`
    analysis/wk8_s29_calib.py      the old calibration battery
    analysis/wk8_s29_discrim.py    the DISCRIMINATING battery (41 cells with mult < a)
    analysis/wk8_s29_sweep.py      the length-3 sweep
    analysis/wk8_s29_chain.py      the four-term chain and the subspace protocol
    analysis/wk8_s29_hilb.py       the whole-Hilbert-function detector
    analysis/wk8_s29_bigrank.py    the (6^4) solver (unblocked; not run to completion)

## 7. What a successor should do first

1. **Apply the one-line fix to `docs/isotypic_rank.md` §1**, and add the
   discriminating battery to `wk6_s26_regress.py` so no future session can ship
   an untested `mult`.
2. **Finish `(6,6,6,6)`.**  The cost is now known: one 12,652-column exact
   elimination, ~20–40 min of numpy per prime, with the corrected rule.  It
   settles `e` and my `e >= 7` against the integrator's `e = 6`.
3. **Sweep length 4 for `mult_{per_3^pad} < a`.**  Length 3 is exhausted
   through `delta = 7`; the codimension there is 3, but at length 4 it is 12,
   so the ideal should surface earlier in relative terms.
4. **Re-run session 26's and 27's headline cells under the corrected rule** if
   any of them are ever re-used for a `mult < a` claim.  The ones re-run here
   are unchanged, but only the ones re-run here.
