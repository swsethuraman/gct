# Session brief — s30: the 62  (v2 — supersedes the committed docs/s30_sweep62.md)

**Branch `s30-sweep62`.**  Measurement lineage (25 → 27 → 29).  Pure compute
with one engineering prerequisite done right — and one convention correction
that postdates the v1 brief and is the reason this version exists.

## 0. Standing orders

- Rule 9; new files only; do not touch `paper/`, `PROJECT_NOTES.md`,
  `docs/boundary_deficit.html`.  Ancestry: `13fb170` must be an ancestor of the
  tip; the s29 and s31 merges should sit above it (look for
  `analysis/wk8_s29_*.py`) — if they are absent, everything you need is inline
  here.  Pre-register first; push likely refused — bundle.
- **Your cells are exactly the `delta = 6`, `a >= 2`, `ell >= 5` cells at
  `n = 4`** (71 minus session 27's nine).  Do not touch length-4 or rectangular
  cells (s29's territory), and do not touch `n = 3` except task D.

## 1. THE CONVENTION CORRECTION — read before writing any code

Session 29 found, and the integrator verified three independent ways, that the
raising-operator rule stated in `docs/isotypic_rank.md` §1 is **wrong**.  On
the coefficient functionals `c_alpha` the correct action is

        E_ij . c_alpha  =  (alpha_i + 1) . c_{alpha + e_i − e_j}
                           ^^^^^^^^^^^^^
        NOT  alpha_j . c_{alpha + e_i − e_j}   (the documented rule)

The two differ by the diagonal `alpha!` rescaling, so they give the **same
kernel dimension `a` everywhere** and *different kernel vectors* — hence
possibly different `mult`.  **No `mult = a` calibration can detect the
difference.**  Sessions 26/27 used the wrong rule; their published values were
re-run under the fix and all reproduce, but the wrongness is structural: two
"independent" implementations agreed because both followed the same wrong
sentence.  If the s29 merge has landed, `isotypic_rank.md` carries the repair;
either way, implement the rule above.

**Mandatory discriminating calibration, FIRST, before the sweep:**

1. Binary quartics, closure of `{ell^3 m}`, weight `lam = (4,4)`, `delta = 2`:
   correct answer `mult = 0` (session 24, independent route), with the kernel
   vector proportional to  `c40.c04 − (1/4) c31.c13 + (1/12) c22^2` — the
   classical invariant `I`.  The WRONG rule yields kernel `(1, −4, 3)` and
   `mult = 1`.  If your implementation does not reproduce `mult = 0` here, stop.
2. If `analysis/wk8_s29_*.py` is present: run session 29's discriminating
   battery (48 World A cells, 41 with `mult < a`) and match it exactly.
3. Session 26's five cells and the 20 weights with `a > 0`, `delta <= 4` at
   `n = 3`: all `mult = a` (unchanged by the fix; now genuinely certified).

## 2. Re-certify the nine, as your entry calibration

Session 27's nine length-5 cells at `delta = 6` — `(14,5,2,2,1) (13,5,4,1,1)
(12,7,3,1,1) (13,6,2,2,1) (11,8,3,1,1) (14,4,2,2,2) (12,7,2,2,1) (12,6,4,1,1)
(12,5,5,1,1)`, all reported `mult = a` on both sides — were measured under the
OLD rule.  Re-measure all nine under the corrected rule before touching new
cells.  Integrator's prior: all nine unchanged (`mult = a` is insensitive to
the basis error generically).  **Any change is a headline finding, not a
calibration failure** — verify it at 3x points and both primes and report
immediately, because it would revise session 27's record.

## 3. Why the 62 matter  (unchanged from v1)

They are the only weights anywhere in reach where a multiplicity obstruction is
arithmetically possible (`a >= 2`), not closed by the length-4 containment
(`ell >= 5`, where the containment provably fails — the block construction
needs every 5-ary cubic to be `3x3`-determinantal, and the Jacobian rank is 29
of 35), and not yet measured.  Nine of 71 came back `D = 0`, `mult = a` both
sides — a pattern with no theorem behind it (the integrator's branch
computation, `docs/l5_containment.md`, shows no compression branch rescues the
containment at length 5).  The 62 decide whether that pattern is a law waiting
to be found or an artifact of measuring the cheapest nine.

## 4. The engineering, first and properly  (unchanged)

The wall is exact rank at `N_S` up to ~20,000.  **Do not hand-roll** (sessions
28 and 29 both tried; both failed their own self-tests).  Use `python-flint`
(`nmod_mat.rank()`, two word-size primes) or Sage.  Requirements: the
calibrations of §1–§2 pass first; the structural check `rank(R) = N_S − a` at
every cell; ranks over two primes; a rank attaining `a` is a certificate; a
rank BELOW `a` must be reproduced at 3x evaluation points and both primes;
**bank each cell as it completes** (append to `results/sweep62_ledger.md`,
commit every few cells — containers reset).  Sort by ascending `N_S`; report
partial coverage as a fraction, honestly.

## 5. What to record per cell

`lam, a, N_S, mult_det, mult_pad, D`; and for any cell with `mult < a` on both
sides: the kernel subspaces `U_det, U_pad` as explicit bases and whether
`U_det = U_pad` / one contains the other / neither (two primes).  Equal
multiplicities with different subspaces is the single most valuable outcome
available.

## 6. Pre-registration  (`results/PREREG_s30.md`, committed first)

1. Predicted count of the nine that change under the corrected rule.
2. Predicted count of the 62 with `D = 0` and `mult = a` both sides.
3. Predicted count with `mult < a` (either side), and which side first.
4. A falsifier for "the nine were representative", **with the regime stated**:
   say where the pattern was observed and why you expect it to transfer —
   three pre-registrations in this programme have now died by carrying a
   pattern out of its regime.

Integrator's priors: zero of the nine change; the pattern holds broadly but
not universally; first `mult < a` on the pad side.  Genuinely uncertain.

## 7. Kill criteria

- **Any `D > 0`: STOP EVERYTHING.**  Verify by both routes, both primes, 3x
  points, independent `a` (raising-kernel vs plethysm), under the CORRECTED
  rule only.  If it survives, it is the programme's first multiplicity
  obstruction — full certificate, report immediately, do not resume sweeping.
- The `{ell^3 m}` witness failing under your implementation: your rule is
  wrong; nothing you measure counts until it passes.
- Any of the nine changing: report before continuing (see §2).
- flint/Sage unavailable: fall back to session 27's subsampled two-prime route
  and say so; do not write a new blocked elimination.

## 8. Task D, only if time remains

Re-certify session 28's `n = 3` length-`>= 5` measurements (`delta <= 7`,
`mult = a` everywhere) under the corrected rule, and its `delta = 6, 7`
residue if the fast rank makes it cheap.  This closes the last uncertified
entries in the ledger.

## 9. Deliverables

    results/PREREG_s30.md        first
    results/sweep62_ledger.md    the running ledger, committed as it grows
    docs/sweep62.md              the verdict on the pattern
    docs/session_30.md           record, ledger, honest boundary
    analysis/wk8_s30_*.py        the tooling (with its self-test)
