# Session 49 — Foundations audit, and an independent two-layer verifier

**No new science this session.**  Nothing in the s50–s55 batch is trusted until
this one passes.  Every item is a correction to something committed, or a piece
of verification infrastructure.

## 0. Standing constraints

- Deliver by git bundle only.  Do not push.
- Do not edit `paper/det3-conductor.tex`, `paper/det4-onset.tex`,
  `PROJECT_NOTES.md`, or `docs/boundary_deficit.html`.  Those have a single
  writer.  If you believe one is wrong, say so in your report.
- Commit messages carry a `Co-Authored-By` trailer only.  No session-link
  trailer, in commits or in any script that commits.  No session-link URL in
  any file you write.
- Bound every run with `timeout` and `ulimit -v`.  Record the process id to
  `results/logs/<run>.pid` and end a run only by that recorded id.  Do not
  select processes by name pattern.
- No committed file over 5 MB.  Logs under `results/logs/`.  Config is
  append-only.
- Pre-registration first: state what will be measured and what would count as a
  positive result before running it.  Bank the result per cell.
- `python-flint` only for exact linear algebra.
- Any cell reporting `D > 0` goes through the verification protocol before it is
  written down as a claim.
- Before developing any statistic meant to characterise determinant type, run
  the degeneracy-direction pre-check in `docs/brief_wording.md` §5.

## 1. Background you need

`mult_λ C[GL_16·det_4]_δ` equals the multiplicity of `S_λ(C^r)` in `C[D_r]_δ`
for `ℓ(λ) = r`, where `D_r = closure{det_4(Σ s_i A_i)} ⊆ Sym^4 C^r`.  On the pad
side `P_r = closure{ℓ(s)·per_3(A(s))}` and `R_r = {ℓ·c}`, with `P_r ⊆ R_r`.

With `i_X = dim I(X)^{HWV}_{λ,δ}`, `a = a(λ,δ)`, `mult_X = a − i_X`:

    D := mult_pad − mult_det = i_det − i_pad.

A separation needs `i_det > i_pad`.  `mult_det < a` is necessary and nowhere
near sufficient.  Several committed documents still read as if it were
sufficient; fixing that is part of this session.

## 2. Tasks

### 2.1 Both cap degrees are wrong in the repository

`docs/sixrow_cap.md` and `docs/sixrow_cap_closed.md` quote 1197 (proved) and 666
(certified).  Both came from the **generic** rank `ρ_d` of the Macaulay matrix
`M_d(F)` of the `r` partials.  The smallest usable minor is **(rank of the
determinantal specialisation) + 1**, not `ρ_d`.  Corrected: **1148** proved,
**661** certified.

Recompute both from scratch, showing `ρ_d`, `h_d = [t^d]((1−t^{n−1})/(1−t))^r`,
the determinantal rank at the relevant `d`, and the resulting minor size.
Correct both documents.  Check whether the same slip is in paper 1 at
`prop:jaccap`; if so, report it — do not edit the paper.

### 2.2 Write out the `r ≤ 4` proof properly

We claim `R_r ⊆ D_r` for `r ≤ 4` via the 72 determinantal representation classes
of a smooth cubic surface, with the count exactly tight: `9·4 − 16 = 20 =
dim Sym^3 C^4`.  The committed argument covers the smooth case only.  Write out:

1. which `ℓ·c` the smooth-cubic-surface argument handles directly;
2. which need degeneration (`c` singular, `c` non-reduced, `ℓ` a component of
   `c`), and give that argument — we work with closures, so a limit suffices;
3. a confirmation that tightness is respected: with no slack in the count, the
   argument must not quietly assume a general member where a special one is
   needed.

### 2.3 Isolate `r = 5` correctly — and hand it to session 54

For `r = 5`, `9·5 − 16 = 29 < 35 = dim Sym^3 C^5`, so a general cubic in five
variables is not a `3×3` determinant and the block construction `diag(ℓ, N)`
fails.  That rules out the construction, not the question: `R_5 ⊆ D_5` asks whether
`ℓ·c` is a **limit** of `det_4` pencils.  Record it as open and as the subject
of session 54.  Do not attempt to settle it here.

Separately: several documents justify excluding `ℓ ≤ 5` by appealing to washout
(`P_r = R_r` for `r ≤ 5`).  That is the wrong justification — `P_r = R_r` does
not preclude an obstruction at those lengths.  The real justification is that we
measured them and found nothing.  Fix the wording wherever it appears.

### 2.4 Re-prove the Pieri transport step

Give it with explicit maps on multiplicity spaces rather than by a dimension
count.  Note in the write-up that the direction we use is the easy one and needs
no surjectivity — the external audit read it as needing surjectivity, which says
the write-up is unclear even though the statement is fine.

### 2.5 Proved versus measured

- **Proposition D.**  Is the upper bound on the determinantal Milnor corank
  proved, or only measured?  If measured, say so in the statement and rename the
  proposition for the Macaulay-minor mechanism specifically.
- **Theorem C.**  It asserts `r*(m) = 3` for all `m ≥ 17`.  Finitely many
  Jacobian evaluations do not prove an infinite family.  Supply a uniform
  argument or restate as proved on the checked range, conjectural beyond.
- Fold in session 48's two washout-table corrections: the orbit term `2m − 2`
  was missing from one row, and `m = 2` needs the `O(4)` stabiliser.  At our own
  row `(m,r) = (3,6)` the deficit is 6, not 2.

### 2.6 Randomised-test provenance

Confirm from the git history that the Schwartz–Zippel evaluation pencils were
fixed **before** the exploratory runs that used them.  Record the seed and the
introducing commit in `docs/randomised_protocol.md`.  If the history says
otherwise, say so plainly.

### 2.7 The verifier — the main deliverable

Build `tools/verify/` as a standalone checker sharing **no code** with the worker
pipeline.  It reads a declared format and errors on anything it cannot parse; it
never guesses at malformed input.

**Layer 1 — syntactic.**  Given serialised integer matrices and a claim:
recompute the rank over `ℚ` exactly and over at least two distinct primes;
recompute any claimed non-vanishing minor exactly over `ℤ`; recompute any
claimed nullity-zero certificate and report the prime.

**Layer 2 — semantic.**  This is the layer that matters.  Layer 1 catches a
wrong computation; layer 2 catches a **correct computation of the wrong
object**, which is our recorded failure mode.  For a highest-weight-vector
certificate, check: the weight of the vector equals the claimed `λ`; every
raising operator annihilates it over `ℤ`, not modulo a prime; the claimed
evaluation points genuinely lie on the claimed variety (pad points really are
`ℓ(s)·per_3(A(s))` for the recorded `s`; det pencils really are `det_4` of the
recorded pencil); and the degree, variable count and `|λ| = 4δ` are mutually
consistent with the cell claimed.

Then run the verifier over every certificate in `results/certs/` and report
failures.

### 2.8 Wording corrections

Remove or restate, everywhere in the repository: "onset ≥ 10" and any lower
bracket on the onset; "the occurrence route is empty"; and "exact whenever it
fires" in `docs/s43_review.md` and in the six-row record — the exactness
conjecture was refuted in s47.

### 2.9 A new house rule to write down

Two external sessions in a row produced an invariant of the form "determinant
type is special in way `X`", and in both the padded permanent turned out to be
*more* special in way `X`, so the invariant separated in the wrong direction.
The same shape appears in our own Milnor-corank work.

Add to `docs/brief_wording.md` §5 a **degeneracy-direction pre-check**, with a
fixed committed test set of three evaluation points: a determinant pencil, a
reducible `ℓ·c`, and the full ten-variable `ℓ·per_3`.  Any proposed statistic is
evaluated at all three before anything is proved about it.

## 3. Success and failure

**Success:** every item resolved or explicitly labelled open, with the verifier
running clean or reporting specific failures.

**The failure that matters:** `2.3` turning out to admit an obstruction at
`ℓ = 5` that we have been excluding on bad grounds.  Stop and say so if it does.

## 4. Report

`docs/s49_report.md`, plus corrected documents and `tools/verify/`.  List
separately: corrections made, items confirmed correct, items now open.  Deliver
as a bundle.
