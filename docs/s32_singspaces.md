# Session brief — s32: closing the classification joint

**Branch `s32-singspaces`.**  Theory lineage (26 → 28).  A literature task with
a theorem at the end.  Goal: turn the integrator's length-5 non-containment
computation from "modulo a classification" into an unconditional statement —
or find the exceptional branch that changes it.

## 0. Standing orders

- Rule 9; new files only; no `paper/`, no `PROJECT_NOTES.md`, no
  `boundary_deficit.html`.  Ancestry: `1203fe4` an ancestor; commits above
  expected.  Pre-register first.  Bundle on push refusal.

## 1. The computation to be closed, self-contained

Question (from session 27): is `D_5^{per_3^pad} ⊆ D_5^{det_4}` — i.e. is
`s_1 . c` a `4x4` linear determinant for generic quinary cubic `c`?  If yes,
the whole length-5 stratum at `n = 4` closes (`D <= 0` a priori) and the nine
measured `D = 0` cells are explained; if no, they are unexplained and the
`ell >= 5` cells stay live.

`det(sum s_i A_i)` divisible by `s_1` forces `span(A_2..A_5)` to be a
4-dimensional space of **singular** `4x4` matrices.  The integrator
(`analysis/l5contain.py`, `docs/l5_containment.md` if merged) parametrised the
standard branches and measured the reachable cubic family exactly (Jacobian
rank mod `2^61-1`, target 35 = all quinary cubics):

    common kernel   A(V_1) = 0      rank 29   (= the 3x3-determinantal cubics)
    compression     A(V_2) <= W_1   rank 31
    compression     A(V_3) <= W_2   rank 31
    common cokernel im A <= W_3     rank 29

**Max 31 < 35.**  Also proved: no exceptional branch inside skew `4x4`
(a singular 4-space there would be a 4-dim isotropic of the rank-6 Pfaffian
quadric; max isotropic is 3).  The soft joint: is every 4-dimensional singular
subspace of `M_4(C)` contained in a compression space?

## 2. The work

**A. Literature, thoroughly.**  Atkinson (*Primitive spaces of matrices of
bounded rank*, J. Austral. Math. Soc. 1980s); Atkinson–Lloyd; Eisenbud–Harris
(*Vector spaces of matrices of low rank*, Adv. Math. 1988); Fillmore–Laurie–
Radjavi; de Seguins Pazzis (several papers on large spaces of singular
matrices, 2010s).  The needed statement is about spaces of bounded rank `<= 3`
in `M_4` of dimension 4 — small on every parameter, likely inside known
classifications.  Extract the exact statement with the exact hypotheses
(algebraically closed field, dimension ranges).

**B. If the literature covers it**: write the containment-failure theorem
cleanly — *the generic reducible quinary quartic `ell.c` is not a `4x4` linear
determinant* — with the citation, the branch table, and the corollary: the
length-5 stratum at `n = 4` is not closed by containment.

**C. If it does not, or the classification has exceptional branches at this
size**: enumerate them, add each as a parametrised branch to the Jacobian
computation (the integrator's script generalises: mask + rank), and re-measure.
A branch reaching 35 would REVERSE the conclusion — that outcome must be
reported as the headline, not buried.

**D. Independent re-verification** (house style): rerun the four branch ranks
with your own implementation before extending; and verify the `29 =
dim D_5^{det_3}` coincidence, which is the built-in consistency check.

**E. Bonus, if cheap**: the same question one degree of generality up — for
which `(n, r)` is `{ell . c}` (with `c` in `D_{r}^{det_{n-1}}`-closure)
contained in `D_r^{det_n}`?  Session 27 proved yes for `(4, 4)`; the pattern of
where the stacking trick is and is not rescueable is the structural heart of
the padded comparison.

## 3. Pre-registration

1. Predicted verdict: covered by literature / needs a new proof / exceptional
   branch exists.
2. Predicted effect of any exceptional branch (rank still `< 35`, or 35).

Integrator's prior: covered, no exceptional branch at these parameters, the
non-containment stands.  Moderate confidence — the `3x3` skew example is
exactly the kind of thing that makes overconfidence here embarrassing.

## 4. Kill criteria

- An exceptional branch reaching rank 35: headline reversal — the length-5
  stratum closes, the nine cells are explained, sessions s30's sweep becomes
  confirmation rather than exploration.  Report immediately (it changes what
  s30's results mean).
- A literature statement contradicting the measured 31s: stop; either the
  reading or the computation is wrong; reconcile before writing anything.

## 5. Deliverables

    results/PREREG_s32.md      first
    docs/singular_spaces.md    the classification, the theorem or the reversal
    docs/session_32.md         record, ledger, honest boundary
    analysis/wk8_s32_*.py      re-verification + any new branches
