# Review of session 25, and one consequence it did not draw

Integrator, 2026-08-31.  Every figure below recomputed from scratch in a fresh
container (no repo, no session-25 code, no `ambient_screen.py`) — independent
Murnaghan–Nakayama, plethysm, symmetric Kronecker and Weyl dimensions.

## 1. Verification of session 25

| claim | checked | result |
|---|---|---|
| `n=3` ambient stratification, `delta = 2..8`: support / `sum a` / live | all 7 rows | **exact match**, including `delta=8`: 371 / 677 / 168 |
| `Sigma_a(delta) = C(164+delta, delta)` | `delta = 2..7` | **exact match** on all six, to 749,064,102,930 |
| `Sigma_m(delta) = sum m_det dim S_lam(C^9)` | `delta = 2,3,4` | **exact match**: 16,215 / 1,241,190 / 78,138,270 |
| paper deficit totals `= sum m_det − sum a` | `delta = 2,3,4` | **exact match**: 1, 6, 31 |
| `Sym^2(Sym^5)` has 3 constituents, `m_det = 1` on each | recomputed | **confirmed**: `(10), (8,2), (6,4)` |
| `A − 1 = 164`, `d − 1 = 64` at `n = 3` | `binom(11,3) = 165`; `81−18+2 = 65` | **confirmed** |

The two mechanisms session 25 found — **hypersurface blindness** and
**saturation at the ceiling** — are both correct, and neither the critique nor
I named either. The hypersurface argument is the crisp one: for a hypersurface
of degree `e` and weight `det^w`,
`mult(lam) = a(lam,delta) − a(lam − w.1, delta − e)`, a function of the ambient
and one `(degree, weight)` pair. Two such closures have identical multiplicity
functions, so `D = 0` between them carries no geometry. 80.9% of the 742.
**Retire the saturation law on that ground.**

Three of my own claims are refuted here and I record them as refuted:

1. **"An obstruction comes free at `m_det < a`"** (my brief, §2B). Wrong. It caps
   `mult_det` but gives no lower bound on `mult_per`; the deficit still has to
   work on the permanent side. Session 25's "half-free" is the correct term.
2. **The BIP attribution in `docs/easy_counts.md`.** All 36 weights at `(5,2)`
   with `m_det = 0` have `a = 0`. It is ambient arithmetic; BIP is not doing the
   work. Confirmed independently: `Sym^2(Sym^5)` has exactly three
   constituents and `m_det = 1` on all three.
3. **My prior that `m_det / a` falls with `n`.** It rises, at every `delta`.

## 2. The consequence session 25 did not draw

Session 25 reports the paper audit as **80.6% forced** at `delta = 4`. Its own
numbers say something much stronger, and its §7 states the premise without
drawing the conclusion.

**The argument.** `def(lam) = m_det(lam) − mult(lam) >= 0` pointwise, and
`mult(lam) <= a(lam)` pointwise. If the total deficit equals
`sum m_det − sum a`, then `sum mult = sum a`, so `sum (a − mult) = 0` with every
term non-negative, hence

        mult_det(lam) = a(lam, delta)   at EVERY weight.

**The measurement**, extended three degrees past session 25:

| delta | `sum m_det` | `sum a` | difference | paper's published deficit |
|---|---|---|---|---|
| 2 | 3 | 2 | **1** | 1 |
| 3 | 11 | 5 | **6** | 6 |
| 4 | 43 | 12 | **31** | 31 |
| 5 | 170 | 29 | **141** | 141 |
| 6 | 697 | 79 | **618** | 618 |
| 7 | 2713 | 225 | **2488** | 2488 |

Six consecutive degrees, exact. So:

> **The ideal of `closure(GL_9 . det_3)` is zero in every degree through 7, and
> every deficit number in the paper is `m_det − a` — the ambient cap, with no
> boundary content whatever.**

Not 80.6%. **All of it**, at every degree the paper reports. The "unforced"
remainder session 25 identifies is the same cap acting at weights where
`a = 1 < m_det`.

## 3. Two hypotheses that predict this table identically

This needs separating before the paper goes anywhere.

* **H1 — the geometry.** `Ω̄(det_3)` genuinely has no equations below degree 8.
  Striking for a 65-dimensional cone in a 165-dimensional space, but not
  absurd: the degree of the variety is large and nothing here is asymptotic.
* **H2 — the instrument.** The engine has been returning the ambient
  multiplicity rather than the closure multiplicity, in which case
  `def = m − a` is what it would print whether or not the ideal is zero.

Both predict the table above exactly. Nothing in the corpus separates them,
because the ambient was never computed alongside the engine's output until now.

**The decisive test is cheap and it is session 26's cell.** `(12,6)` at
`delta = 6` has `a = 2`, `m_det = 2`, so H1 and H2 both predict `mult_det = 2`,
`def_det = 0`. The isotypic-rank method shares no code and no algorithm with the
engine. If it returns 2, H1 stands and the engine is vindicated at a live
weight. If it returns 0 or 1, the paper's `delta = 6` total is wrong and so is
everything downstream of the engine.

## 4. Predictions for session 26, registered now

If `mult = a` holds pointwise through `delta = 7`, then every cell in session
26's brief is already determined:

| lam | delta | a | m_det | predicted `mult_det` | predicted `def_det` |
|---|---|---|---|---|---|
| (9,4,2) | 5 | 2 | 3 | **2** | **1** |
| (12,6) | 6 | 2 | 2 | **2** | **0** |
| (12,4,2) | 6 | 2 | 3 | **2** | **1** |
| (15,6) | 7 | 2 | 2 | **2** | **0** |
| (13,6,2) | 7 | 3 | 4 | **3** | **1** |

Session 26's brief said its payoff was the first deficit measured where the
ambient had room. That is now wrong twice over: the answers are predicted, and
`(12,6)` returning `2` fires its own kill criterion ("the determinant filling
the room — the `a = 2` stratum at `n = 3` is closed").

**Its real payoff is now an independent audit of the engine**, at a cell where
the answer is predicted in advance by two competing hypotheses that this
measurement separates. That is a better job than the one it was given.

## 5. Two smaller notes on session 25

- **§5 of `race.md`, on session 24b.** "The screen was run entirely inside the
  dead region, which strengthens its negative rather than weakening it" — both
  readings are true and the record should carry both. It confirms 24b's
  conclusion by a second independent mechanism; it also means that range was
  never capable of producing evidence about obstructions, so it is weaker
  evidence than it looked.
- **The existence proof in `race.md` §3** leans on `Sigma_m` having degree
  `d − 1 = 64`. `Sigma_m` sums the *orbit* count, and `C[G.v]` is a
  localisation `C[Ω̄][1/Δ]`, so "the Hilbert function of a `d`-dimensional cone
  has degree `d−1`" does not apply directly. The conclusion is very likely
  right — Ikenmeyer–Kandasamy's uniform ray bound transfers the growth rate —
  and only an upper bound `o(delta^163)` is needed. But it is asserted, and it
  is the one load-bearing step in the only proof the session offers. Session
  25's successor item 2 already queues this; it should be flagged as blocking
  the existence claim, not just the crossover estimate.
