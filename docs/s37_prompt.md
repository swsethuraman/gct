# Session 37 — theory: the washout, the transfer, and the DIP technique

You are **session 37** of the gct programme, working for the integrator.  Date
your work 2026-09-02 onward.  This is a theory session with four concrete
deliverables, each a short document with proofs; computation is limited to
cheap exact checks.  If the repository already shows a session 37, do not
renumber; flag it and carry on.

## Rules (standing)

- Fresh clone of `github.com/swsethuraman/gct`, branch `s37-dip`, container
  only.  **Ancestry gate**: `git merge-base --is-ancestor c02cee8 HEAD` must
  pass, **and** `docs/s35_review.md` must exist in your clone.
- Single-writer files — never touch: `paper/det3-conductor.tex`,
  `PROJECT_NOTES.md`, `docs/boundary_deficit.html`.
- Delivery by git bundle (`git bundle create dip.bundle s37-dip`, single
  ref).  No pushes.
- `results/PREREG_s37.md` first: for each deliverable, the statement you
  expect to prove, and what would show it false.  Label everything
  proved / measured / adopted-from-literature / expectation.

## Required reading, in order

`docs/s35_review.md` (§1 and §2 are this session's premise),
`docs/theory_directions.md` (Directions 3 and 5 especially),
`docs/s33_review.md` §2–§4, `docs/s30_review.md` §3, `docs/sweep62.md` §4,
`docs/l5_containment.md`, `docs/singular_spaces.md`.

## Deliverable 1 — `docs/washout_lemma.md`: when does the permanent enter?

Prove, cleanly and in the paper's notation:

- **Washout at `r <= 5`.**  The restrictions of `per_3` to `r`-planes are
  dense in `Sym^3 C^r` for `r <= 5` (a full-rank Jacobian at one exact point
  is a proof of dominance; session 26 banked rank 35 at `r = 5` — re-verify
  at one fresh point).  Hence `D_r^pad = {l·c : c any cubic}` for
  `r <= 5`, and **no covariant of length `<= 5` can distinguish the padded
  permanent from `l·(any cubic)`**.  State the consequence for the hunt as a
  theorem: every `D != 0` cell at `ell <= 5` is a statement about
  reducibility versus the determinant, never about the permanent.
- **Entry at `r = 6`.**  `dim D_6^{per_3} = 50 < 56`: lower bound from the
  banked Jacobian rank, upper bound from the stabiliser count
  `9·6 − dim Stab(per_3) = 54 − 4 = 50`.  Make the upper bound rigorous:
  this is the finite-generic-stabiliser page flagged in `docs/s30_review.md`
  §3, written once for `per_3` (`r >= ?`) and once for `det_4` (`r >= 3`),
  with the `r = 2` commutant exception explained.  With that page, the
  dimension tables of sessions 30 and 33 and the `n = 4` codimension table
  become unconditional — say so explicitly.  Conclusion: **`ell = 6` is the
  first length at which any cell can be permanent-sensitive.**

## Deliverable 2 — `docs/transfer_lemma.md`: what a `D` computed against `{l·c}` proves

Formalise the caveat in `docs/s35_review.md` §1.  For any `r`, the true
padded-permanent variety `P_r = closure{l·per_3(A(s))}` sits inside
`R_r = {l·c}`, so `I(R_r) ⊆ I(P_r)` and `mult_{P_r} <= mult_{R_r}`
weight-by-weight.  Prove: a `D < 0` cell computed against `R_r` transfers to
`P_r`; a `D > 0` cell computed against `R_r` does **not** transfer and must
be re-derived against `P_r`.  Then state what the house pipeline actually
computes — evaluation at true padded-permanent points *is* `P_r` — so the
pipeline is correct at every `r` and the caveat bites only on
literature-style arguments about the reducible locus (e.g. catalecticant
minors, Kempf-collapsing of `{l·c}`).  Add the corollary for session 35's
Direction 1: the collapsing computes `mult` for `R_5`, which equals `P_5`
only because of washout; at `r >= 6` it is an upper bound on `mult_pad`.

## Deliverable 3 — `docs/dip_transfer.md`: the technique, tested against our pair

Read Dörfler–Ikenmeyer–Panova (*On geometric complexity theory: multiplicity
obstructions are stronger than occurrence obstructions*, ICALP 2019 / SIAM J.
Appl. Alg. Geom.) with the two varieties `D_6^det` and `P_6` in hand, and
extract: (i) the exact mechanism by which their multiplicity obstruction is
exhibited — which HWVs, evaluated where, and what makes the evaluation
tractable; (ii) which parts of their occurrence-no-go argument are specific
to the fully split type `(1^n)` and which survive splitting type `(1,3)`;
(iii) the honest transfer verdict: is there a permanent-*sensitive*
separator their method could produce at `ell = 6`, and at what cost?  Also
mine Bürgisser–Ikenmeyer's explicit HWV-evaluation technique for the same
question.  If the answer is "their no-go transfers," say so plainly — that
promotes the blindness hypothesis and is a success of this deliverable.
Produce at most three concrete candidate `(lam, delta)` cells or covariant
families for session 36's successors, each with a one-line reason.

## Deliverable 4 — `docs/blindness_slab.md`: the half-theorem, written properly

Session 35 observed that `D <= 0` on the whole `ell <= 4` slab through
degree 9 follows from the length theorem and s33.  Write it as a theorem
with proof (with Deliverable 1's page, through degree `e − 1` given
principality), exhibit the strict cells, and probe the `lam_5 = 1` sub-slab
for a restriction argument — recording precisely where session 32's Theorem
5 stops it, if it does.  Also pin, by a focused literature pass, the graded
degree-`3d−5` Milnor-algebra defect statement session 35's cap rests on
(Dimca / Cynk / Rams); quote it exactly or report that it must be proved.

## Deliverables

The four documents above, `results/PREREG_s37.md`, any exact checks as
`analysis/wk9_s37_*.py` with outputs banked.  Every claim labelled.  End
your report with the one sentence the integrator should carry into the next
brief, and the bundle head hash.
