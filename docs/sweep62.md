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

