# Integrator review — session 64, the padded side on the common source

**Accepted, and it is the cleanest delivery of the batch so far.**  The session
was briefed to build an engine and gated on a Sol derivation that had not
arrived; it found the engine already in the repository, validated it instead,
added a separation test its brief did not ask for, and stopped exactly where its
stopping rule told it to.  Bundle md5 matches, ancestry gate passes against
`226b4ef1`, two commits, 65 files.

## 1. Verified here, independently

**The kernel witnesses.**  This is the check that matters, and it uses the
session's *output* against my own points and my own evaluator
(`analysis/wk10_int_s64_kerncheck.py`, sharing no code with the session):

`(9,9,8,1,1)`, `δ = 7`, `a = 2`, one vector in `U_red` and one in `U_pad`,
13 128 terms each, evaluated at three fresh points of each kind:

    at padded    l(s)·per_3(A(s))   0, 0, 0        in the ideal
    at reducible l(s)·c(s)          0, 0, 0        in the ideal
    at det_4 pencils                nonzero x3     NOT in the ideal

`(13,13,8,1,1)`, `δ = 9`, `a = 19`, the `D = −4` witness — all four `U_pad`
vectors (73 182 terms each) vanish at fresh padded points and are nonzero at
determinant pencils, and their value matrix against six independent pencils has
**rank 4**, so they are genuinely independent.  Hence `i_pad ≥ 4` there, and
with the banked `mult_det = a = 19`, `D ≤ −4`.  The lower bound on `i_pad` is
the checkable half of the claim and it holds.

**The separation dimensions.**  `dim P_r = r + min(9r−4, C(r+2,3)) − 1` and
`dim R_r = r + C(r+2,3) − 1` reproduce the session's table from *my* permanental
cubic ranks (35, 50, 59 at `r = 5, 6, 7`, note 2 §2) with nothing shared but the
arithmetic: `39/39`, `55/61`, `65/90`.  The factorisation `ℓ·c` is unique up to
scalar for generic factors, so the `−1` is right.  **`dim P_6 = 55 < 61` is a
real separation** and it is the one I asked for in note 2 §4.

**The `h_pad` chain.**  Recomputed against the session-42 identity at all 48
cells; `mult_pad ≤ mult_red ≤ h_pad` holds everywhere, and the `h_pad` column
matches the banked ledger.

**The `(8,4,4,4,4)_6` pin.**  `a = 2`, `mult_det = 2`, `mult_red = 1`, and
`P_5 = R_5` forces `mult_pad = 1` exactly.  The engine returns 1.  An engine
returning 0 or 2 would be defective; this is the one calibration in the suite
with a two-sided pin, and it passes.

## 2. One thing I nearly flagged and should not have

I read §5's parenthetical — *"the multiplicity, which is functorial
(`brief_wording.md` §7: `P ⊆ D ⟹ I(D) ↠ I(P) ⟹ mult_pad ≤ mult_det`)"* — as
asserting the containment the programme exists to refute.  **It is not.**  §7
says precisely: "Containment *forces* `D ≤ 0`, so `D > 0` refutes containment."
The citation is faithful and compressed, and `mult_pad ≤ mult_det` at all 48
cells is the null hypothesis holding, not a theorem being assumed.  Recording
the near-miss because a later reader could make the same misreading of the
compressed form; the report would be safer with §7's second clause quoted too.

## 3. The session's own best contribution

**The `r ≥ 6` separation had to be found somewhere other than the
multiplicity**, and the session found where.  My note 2 §4 asked for an `r ≥ 6`
test because `P_r = R_r` makes every `r ≤ 5` calibration blind to a padded
engine that had silently implemented the reducible side.  The session then
established something I had not: **session 47 already proved `mult_pad =
mult_red` at every reachable `r = 6` cell** (`docs/transfer_lemma.md`,
`docs/exactness.md`), reproduced here at three cells — so the *multiplicities*
coincide in reach at `r = 6` as well, and my proposed test would have been
vacuous as stated.

Its replacement is correct and better: separate at the level of the **sample
variety**, by the Jacobian rank of the parametrisation.  `55` against `61`.  An
engine that had implemented `ev_red` would return 61.  That closes the loophole
my note opened and could not itself close.

## 4. What remains unchecked

**The factorized composite identity `mult_pad = rank[(⊕_μ Θ^{per_3}_{μ,δ}) ∘
S_{λ,δ}]`** is still neither reproduced nor banked — correctly carried forward
as such, and correctly *not* attempted here.  Session 65 inherits it.  The 48
`r = 5` cells are now a validated testbed for it, and — per note 2 §3 — they
test it as an **equality**, not an inequality.

**The upper bounds on `i_pad`.**  My verification establishes `i_pad ≥ 1` and
`i_pad ≥ 4` at the two witness cells by exhibiting independent vectors.  The
matching upper bounds rest on the session's own nullity computations (exact per
prime on the sparse route, two seeds and two primes on the dense route with
margin ≥ 6).  I did not reproduce those and the report does not claim I could.

## 5. Provenance, and the fourth instance

The report records the `ev_pad` family as pre-existing (`wk9_s36_stabred` runs
`sides = ('det','pad')`; `wk9_s45_cell` and `wk9_s41_kernel` carry
`forms['pad']`) and names it the third batch-10 item described as missing that
was in fact banked.  §3 above is arguably the **fourth**: session 47's `r = 6`
`mult_pad = mult_red` theorem, which would have saved my note 2 §4 from
proposing a vacuous multiplicity test.  Four instances in one batch is a
finding about the planning, not about the sessions: **batch 10 was specified
from documents and summaries, and the code was ahead of them every time.**
The remedy for batch 11 is in house rule 13's spirit — read the code before
writing the brief, and cite the file, not the memo.

## 6. Verdict

Accepted.  48/48 calibration cells, 12 discriminating, two witnesses verified
here against independently generated points, the separation test established at
the right level, kernel coordinates preserved for session 65, no LMR attempt.
The padded side is no longer the bottleneck: it is exactly as reachable as the
determinant side, and the wall is the one session 63 is measuring.
