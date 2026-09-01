# The 62 at `delta = 6`, `ell >= 5` — law or artifact?

Session 30, branch `s30-sweep62`.  Clone tip `13fb170`; ancestry verified.
Pre-registration: `results/PREREG_s30.md`, written before any computation.
Per-cell record: `results/sweep62_ledger.md`.

**Verdict in one line.**  The pattern is neither a law nor an artifact of
session 27's sampling: it is a statement about the **degree**, not the weight.
Every cell measured returns `mult_det = mult_pad = a` — both ideals are *empty*
in these isotypic components — and an independent dimension count shows the two
varieties differ in dimension by 11, so `D = 0` **cannot** hold at all degrees.
`delta = 6` is simply below the degree at which either ideal begins at `r = 5`.
The next gate is `delta`, not more weights.

---

## 1. What was measured

Session 27 measured the **nine cheapest** of the 71 cells at `n = 4`,
`delta = 6`, `a >= 2`, `ell >= 5`, and found `mult_det = mult_pad = a` at all
nine.  The question this session was set: do the remaining **62** agree, or did
cheapness select a regime?

Two things had to happen before the 62 could be believed.

**(a) The corrected raising rule.**  `docs/isotypic_rank.md` §1 carries
`E_ij . c_alpha = alpha_j . c_{alpha - e_j + e_i}`, which is the action on
`Sym^n V` monomials, not on the coefficient functionals `c_alpha = e^alpha /
alpha!`.  The correct rule is

    E_ij . c_alpha  =  (alpha_i + 1) . c_{alpha + e_i - e_j}

The two differ by the diagonal `alpha!` rescaling.  They give the same kernel
**dimension** `a` and different kernel **vectors**, so `mult` is affected and
**no `mult = a` calibration can detect the difference** — which is exactly why
the error survived several sessions.  Everything below uses the corrected rule.

**(b) A discriminating calibration.**  A battery that the wrong rule *fails*,
run before any measurement (`analysis/wk8_s30_calib.py`, all five parts
passed):

| check | result |
|---|---|
| witness: binary quartics, `closure{l^3 m}`, `lam = (4,4)`, `delta = 2` | `mult = 0` ✓ (wrong rule gives 1) |
| the witness kernel, explicitly | `(12, -3, 1)` ✓ (wrong rule gives `(1,-4,3)`) |
| 48-cell World A battery against session 24's independent closed forms | 48/48 ✓, **41 discriminating** |
| session 26's five cells | 5/5 reproduced ✓ |
| all 20 weights at `n = 3`, `delta <= 4` | `mult_det = a` ✓ |

**(c) Re-certification of session 27's nine.**  All nine re-measured under the
corrected rule.  **All nine unchanged**: `mult_det = mult_pad = a`, `D = 0`.
This confirms pre-registered prediction **P1** and leaves session 27's record
standing.

---

## 2. Discipline actually applied at every cell

- `a` by **two independent routes** — raising-operator kernel dimension, and
  symmetric-function plethysm (`analysis/wk8_s30_pleth.py`).  They agreed at
  every cell.
- `rank(R) = N_S - a` asserted at every cell, as a structural self-check.
- Ranks over **two word-size primes** (2147483647, 2147483629) via
  `python-flint`'s `nmod_mat.rank()`.  No hand-rolled elimination was written:
  sessions 28 and 29 both tried and both failed their own self-tests.
- A rank **attaining `a`** is a certificate (`rank_p <= rank_Q <= a`).
- A rank **below `a`** — the interesting outcome — is re-run at 3× evaluation
  points on a different seed before it is believed, with the kernel exhibited.
  This branch was never taken: no cell came in below `a`.
- Every cell banked to the ledger and committed as it completed, because the
  container resets.

---

## 3. The sweep

*(table generated from the ledger — see §7 for the coverage fraction)*

<!--GEN:TABLE-->
**Session 27's nine, re-certified under the corrected rule** (9 of 9, all unchanged):

| lam | a | `N_S` | `mult_det` | `mult_pad` | `D` |
|---|---|---|---|---|---|
| `(14, 5, 2, 2, 1)` | 2 | 1337 | 2 | 2 | +0 |
| `(13, 5, 4, 1, 1)` | 2 | 1824 | 2 | 2 | +0 |
| `(12, 7, 3, 1, 1)` | 3 | 1884 | 3 | 3 | +0 |
| `(13, 6, 2, 2, 1)` | 3 | 1910 | 3 | 3 | +0 |
| `(11, 8, 3, 1, 1)` | 2 | 2224 | 2 | 2 | +0 |
| `(14, 4, 2, 2, 2)` | 2 | 2337 | 2 | 2 | +0 |
| `(12, 7, 2, 2, 1)` | 3 | 2467 | 3 | 3 | +0 |
| `(12, 6, 4, 1, 1)` | 2 | 2553 | 2 | 2 | +0 |
| `(12, 5, 5, 1, 1)` | 2 | 2795 | 2 | 2 | +0 |

**The 62** — 22 measured, in ascending `N_S`:

| lam | `a` | `N_S` | `mult_det` | `mult_pad` | `D` | balance |
|---|---|---|---|---|---|---|
| `(13, 5, 3, 2, 1)` | 3 | 2800 | 3 | 3 | +0 | 12 |
| `(11, 8, 2, 2, 1)` | 3 | 2919 | 3 | 3 | +0 | 10 |
| `(10, 9, 2, 2, 1)` | 2 | 3176 | 2 | 2 | +0 | 9 |
| `(13, 4, 4, 2, 1)` | 2 | 3199 | 2 | 2 | +0 | 12 |
| `(11, 7, 4, 1, 1)` | 4 | 3209 | 4 | 4 | +0 | 10 |
| `(13, 5, 2, 2, 2)` | 2 | 3672 | 2 | 2 | +0 | 11 |
| `(10, 8, 4, 1, 1)` | 2 | 3686 | 2 | 2 | +0 | 9 |
| `(11, 6, 5, 1, 1)` | 2 | 3818 | 2 | 2 | +0 | 10 |
| `(9, 9, 4, 1, 1)` | 2 | 3852 | 2 | 2 | +0 | 8 |
| `(12, 6, 3, 2, 1)` | 4 | 3942 | 4 | 4 | +0 | 11 |
| `(10, 7, 5, 1, 1)` | 4 | 4672 | 4 | 4 | +0 | 9 |
| `(12, 5, 4, 2, 1)` | 5 | 4942 | 5 | 5 | +0 | 11 |
| `(11, 7, 3, 2, 1)` | 5 | 4978 | 5 | 5 | +0 | 10 |
| `(9, 8, 5, 1, 1)` | 2 | 5159 | 2 | 2 | +0 | 8 |
| `(12, 6, 2, 2, 2)` | 4 | 5194 | 4 | 4 | +0 | 10 |
| `(10, 8, 3, 2, 1)` | 4 | 5731 | 4 | 4 | +0 | 9 |
| `(9, 7, 6, 1, 1)` | 2 | 5967 | 2 | 2 | +0 | 8 |
| `(11, 7, 2, 2, 2)` | 2 | 6563 | 2 | 2 | +0 | 9 |
| `(8, 7, 7, 1, 1)` | 2 | 6718 | 2 | 2 | +0 | 7 |
| `(11, 6, 4, 2, 1)` | 7 | 6789 | 7 | 7 | +0 | 10 |
| `(11, 5, 5, 2, 1)` | 2 | 7461 | 2 | 2 | +0 | 10 |
| `(10, 7, 4, 2, 1)` | 7 | 8337 | 7 | 7 | +0 | 9 |

Every row: `mult_det = mult_pad = a`, `D = 0`.  No cell fell below the ambient cap on either side, so the sceptical re-run branch was never entered.
<!--/GEN:TABLE-->

---

## 4. The dimension count — why `D = 0` cannot be a law

This is a line of evidence **independent of every rank measurement above**.  A
weight of length `r` sees a form `f` only through the short-weight reduction

    D_r^f = closure{ f(s_1 A_1 + ... + s_r A_r) }  <=  Sym^n C^r,

so `dim D_r^f` says how much room there is for an ideal at all, before any
multiplicity is computed.  Taking the generic rank of the parametrisation's
Jacobian — exact derivatives via dual numbers `F_P[t]/(t^2)`, agreed at three
random points over two primes (`analysis/wk8_s30_dims.py`):

| `r` | `dim Sym^4 C^r` | `dim D_r^det4` | `dim D_r^pad` | codim det | codim pad |
|---|---|---|---|---|---|
| 3 | 15 | 15 | 12 | **0** | 3 |
| 4 | 35 | 34 | 23 | **1** | 12 |
| 5 | 70 | 50 | 39 | **20** | 31 |

Three things fall out, and they reorganise the whole picture.

**(i) At `r = 3` the determinant has no ideal at all.**  `codim = 0`: `D_3^det`
is the whole of `Sym^4 C^3`.  Every length-3 weight is therefore forced to
`mult_det = a`, for every degree, by dimension alone — no computation needed.

**(ii) At `r = 4` the determinant's ideal is principal.**  `codim = 1` exactly:
`D_4^det` is a *hypersurface* in `Sym^4 C^4`, so `I(D_4^det)` is generated by a
single polynomial of some degree `e`.  This independently confirms the object
session 29 set out to pin down in its task B (`mult_det((6^4), 6)`), and it is
also exactly the configuration session 24's Prop. 4 calls *hypersurface
blindness*.  Below degree `e` the determinant's ideal is empty at `r = 4` too.

**(iii) At `r = 5` the codimension jumps to 20 and 31.**  Both ideals are
**nonzero**, and — this is the load-bearing point — `dim D_5^pad = 39` is
strictly less than `dim D_5^det = 50`, so the two varieties are *different*
and their ideals are different.  Consequently the Hilbert function of
`C[D_5^pad]` is eventually strictly smaller than that of `C[D_5^det]`, and
there must exist some `(lam, delta)` with `mult_pad != mult_det`.

**Therefore `D = 0` cannot hold at every degree.**  The uniform `D = 0` this
sweep found is not a law about weights; it is the statement that `delta = 6`
is *below the degree at which either ideal begins* at `r = 5`.  The measured
cells all report `mult = a` on both sides — i.e. both ideals are literally
empty in those isotypic components — which is precisely what "too early"
looks like.

Note also that session 27's containment theorem (`D_4^pad <= D_4^det`, via
"a general cubic surface is determinantal", so `l . det_3(M) = det_4 diag(l, M)`)
is consistent with the `r = 4` row, `23 <= 34`, but its proof **does not extend
to `r = 5`**: cubics in five variables are not generally `3x3` determinantal.
That is exactly why `ell >= 5` was the open frontier, and this sweep does not
close it — it dates it.

---

## 5. Verdict: law or artifact?

**Neither, and the dichotomy in the question is the thing to drop.**

*Not an artifact of session 27's sampling.*  Session 27 took the nine cheapest
cells, and cheapness selects lopsided weights with small `a`.  The obvious
worry was that the balanced, large-`a` end behaves differently.  It does not:
this sweep deliberately probed that end first rather than merely extending the
ascending sweep, and **both `a = 7` cells of the 62 — the largest ambient
multiplicity present — return `mult_det = mult_pad = a`, `D = 0`**, as does
every intermediate `a` reached.  The pre-registered falsifier for "the nine
were representative" (P4) was named in advance and was **not** triggered.

*Not a law either.*  §4 shows the two varieties have different dimensions, so
some `(lam, delta)` must separate them.  Reporting `D = 0` over 62 weights at
one degree as though it were a general phenomenon would be the same error this
programme has already made three times — carrying a pattern out of its regime.

*What it actually is.*  `delta`, not the weight, is the axis that matters.
This was pre-registered as the expected verdict (`PREREG_s30.md` §2) and the
measurements are consistent with it at every cell.

---

## 6. Coverage, and the boundary of what was reachable

<!--GEN:COVERAGE-->
**Coverage: 22 of the 62 cells, 35%** — and 72 of the 62's 189 units of ambient multiplicity, 38%.

| axis | measured | across the 62 |
|---|---|---|
| `N_S` | 2800 – 8337 | 2800 – 97713 |
| `a` | 2 – 7 | 2 – 7 |
| balance | 7 – 12 | 4 – 12 |
<!--/GEN:COVERAGE-->

The limit is **memory, not patience**.  Peak RSS is quadratic in the
weight-space dimension `N_S` — fitted across three observed OOM kills at
roughly `7.5e-8 . N_S^2` GB — against a usable budget of about 6.5 GB.  That
puts a hard ceiling near `N_S ~ 9000` with two workers and near `N_S ~ 11500`
with one, while the 62 run from `N_S = 2800` to `N_S = 97713` with median
12445.  Full coverage was never available in this session and the
pre-registration said so in advance; what follows is which part of the space
was actually reached.

**What was reached.**  The cheap end exhaustively, and — deliberately, per the
pre-registered order — the extreme of every axis that the budget permits:

- **both `a = 7` cells**, `(11,6,4,2,1)` and `(10,7,4,2,1)`: the largest
  ambient multiplicity anywhere in the 62;
- `(8,7,7,1,1)`, **balance 7** — the most balanced cell in the 62 that fits in
  memory at all;
- every value of `a` from 2 to 7 that occurs among the reachable cells.

**What was not reached, stated plainly.**  The genuinely balanced end.  The
`balance <= 6` cells of the 62 are

| lam | balance | a | `N_S` | GB needed |
|---|---|---|---|---|
| `(8,4,4,4,4)` | 4 | 2 | 94675 | ~670 |
| `(8,8,4,2,2)` | 6 | 3 | 22475 | ~38 |
| `(8,6,6,2,2)` | 6 | 3 | 31356 | ~74 |
| `(8,7,4,3,2)` | 6 | 2 | 39362 | ~116 |
| `(8,6,4,4,2)` | 6 | 4 | 54343 | ~222 |
| `(7,7,4,4,1,1)` | 6 | 2 | 97713 | ~716 |

Every one of them is one to two orders of magnitude beyond this container.
**So the sweep probed the balanced end down to balance 7 and no further**, and
the strongest honest statement about `balance <= 6` is that it is untested —
not that it agrees.  Whether that matters is a fair question: §4's dimension
count says the ideals are empty at `delta = 6` for structural reasons that have
nothing to do with the weight's shape, which is a reason to expect agreement
there — but it is an expectation, not a measurement, and it is recorded here
as one.

---

## 7. Recommendation

**Stop adding weights at `delta = 6`.  Move the degree.**

The evidence that the remaining cells will not repay their cost is now
structural rather than merely inductive.  §4 shows both ideals at `r = 5` are
nonzero but that their onset degree is what is being probed, and every cell
measured says `delta = 6` is before that onset.  Forty-two more cells at the
same degree test the same thing again.

Concretely, in priority order:

1. **`delta = 7` at `ell = 5`, cheapest weights first.**  This is the only
   axis the sweep leaves genuinely open, and the cheap cells at `delta = 7`
   cost far less than the balanced cells at `delta = 6` that this session
   could not reach.
2. **Pin the onset degree at `r = 4` first, as a calibration.**  `D_4^det` is a
   hypersurface (codim exactly 1, §4), so its ideal is principal of some degree
   `e`; `e` is a single number and it bounds where to start looking at `r = 5`.
   Session 29's task B was aimed at exactly this.
3. **Only then return to the balanced `delta = 6` cells**, and only with more
   memory than this container has — `(8,8,4,2,2)` at ~38 GB is the cheapest of
   them and is the right single test if one is wanted.

The `n = 4` engineering has now paid for itself in the sense session 24 asked
about: it produced a structural statement (the codimension table) that no
amount of `n = 3` work would have reached.  But the next marginal cell at
`delta = 6` is worth very little, and the next degree is worth a lot.
