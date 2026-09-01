# Pre-registration — session 30: the 62

Written **before** any computation.  Branch `s30-sweep62`, 2026-09-01.

**Clone state.**  `origin/main` at **`13fb170`**; ancestry check passes.
Sessions 27 and 28 are merged.  **Session 29 has NOT landed** —
`analysis/wk8_s29_*.py` is absent and `docs/isotypic_rank.md` still carries the
wrong raising rule — so the corrected rule is implemented inline from this
brief and session 29's discriminating battery is rebuilt rather than imported.

**Engineering.**  `python-flint` 0.9.0 installed; `nmod_mat.rank()` verified.
No hand-rolled elimination will be written (sessions 28 and 29 both tried and
both failed their own self-tests; I was session 29).

## 0. The convention, restated as I will implement it

    E_ij . c_alpha  =  (alpha_i + 1) . c_{alpha + e_i - e_j}

Witness, run before anything else: binary quartics, `closure{l^3 m}`,
`lam = (4,4)`, `delta = 2` — correct `mult = 0`, kernel proportional to
`c40.c04 - (1/4) c31.c13 + (1/12) c22^2`, i.e. `(12, -3, 1)` after clearing
denominators.  The wrong rule gives kernel `(1,-4,3)` and `mult = 1`.

## 1. Pre-registered predictions

**P1 — how many of session 27's nine change under the corrected rule?**
**Zero.**  Reasoning: the two rules differ by the diagonal `alpha!` rescaling,
so a wrong basis of a right-dimensional space still has full rank generically;
`mult = a` is exactly the outcome that cannot detect the error.  Session 29
re-ran session 26's five cells, the 20 weights at `delta <= 4` and the 19
length-4 cells at `delta = 5` under the fix and all reproduced.  Confidence:
high.  *Falsifier:* any of the nine changing — which I would report before
continuing, since it revises session 27's record.

**P2 — how many of the 62 give `D = 0` with `mult = a` on both sides?**
**62 of 62.**  Confidence: moderate.  *Falsifier:* any cell with `mult < a` on
either side.

**P3 — how many with `mult < a`, and which side first?**  **Zero**; if any,
the **pad** side first, because at length 5 the padded permanent's stratum has
codimension 31 of 70 against the determinant's 20 of 70.

**P4 — the falsifier for "the nine were representative", with the regime
named.**  This is the prediction I care most about getting right, because three
pre-registrations in this programme have died by carrying a pattern out of its
regime, and one of them was mine (session 29, Q1).

*Where the pattern was observed:* session 27 measured the **nine cheapest** of
the 71 by weight-space dimension `N_S` (1337 to 2795).  Cheapness is not a
neutral selector: small `N_S` means a **lopsided** weight — large `lam_1`, short
tail — and those nine have `a in {2,3}` only.

*Why I expect it to transfer, and where I expect it to break if it does not:*
the mechanism I believe is operating is that the ideal of `D_5^pad` simply has
no component at `delta = 6` at all, which is a statement about the degree, not
the weight — the parametrisation `C^5 x C^35 -> Sym^4 C^5` has
`binom(10,4) binom(40,6) ~ 8.1e8` degrees of freedom at `delta = 6` against an
ambient `binom(75,6) ~ 1.2e8`, so there is no dimension obstruction anywhere
near `delta = 6` and the ideal may well start much later.  If instead the ideal
*is* present at `delta = 6` and the nine missed it, it will show up first on
the **balanced, large-`a`** end of the 62 — the opposite end from the one
session 27 sampled.

*Consequence for method, adopted in advance:* I will **not** sweep purely in
ascending `N_S`.  I will interleave — the ascending sweep for coverage, plus a
deliberate early pass over the largest-`a` and most balanced cells that the
budget can reach — so that the regime is tested rather than merely extended.
If the session ends with partial coverage, the report will state which cells
were sampled and that the balanced end was probed on purpose.

## 2. What I expect the verdict to be

That the 62 come back uniformly `D = 0` with `mult = a` on both sides, and that
the honest conclusion is **not** "the pattern is a law" but "the ideals of both
strata are invisible at `delta = 6`, and `delta`, not the weight, is the axis
that matters".  The next gate should then be `delta = 7` at `ell >= 5`, not more
weights at `delta = 6`.

## 3. Discipline

`a` by two routes (raising-operator kernel dimension, and symmetric-function
plethysm) at every cell; `rank(R) = N_S - a` asserted at every cell; ranks over
two word-size primes; a rank attaining `a` is a certificate; a rank **below**
`a` re-run at 3x evaluation points and both primes before it is believed, with
the kernel exhibited.  Every cell banked to `results/sweep62_ledger.md` and
committed as it completes, because the container resets.
