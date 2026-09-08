# Batch-10 housekeeping — what was done, and what was left undone

A pass over everything batch 10 deferred, run while batch 11 is in flight.
Ordered by whether it was fixed, recorded, or left for a session.  The audit
that produced the list swept the five worker reports, the four integrator
reviews and the seven integrator notes.

---

## 1. Fixed

**Two live session URLs in scripts that write commits.**
`analysis/wk9_s36_sweep.py` and `analysis/wk9_s41_sweep.py` each appended a
`Claude-Session:` trailer to every commit they made.  The history rewrite at the
batch-9/10 boundary removed 260 such trailers from commit *messages*, but these
two scripts survived it and would have re-injected one on every run — and
session 43's brief had already flagged the pattern ("sweep scripts do; do not
copy that pattern") without anyone fixing the scripts.  Both now end at the
`Co-Authored-By` line.  **No live session URL remains anywhere in the
repository**; the surviving `claude.ai` strings are the rule being stated and
the rewrite tooling that enforces it.

**`docs/lmr_cell.md` §3a claimed the `δ = 23` predecessor was cheaper.**  It is
sharper, not cheaper.  Batch-10 integrator note 2 corrected this and the file
never carried the correction.  Re-measured independently for this pass:
`N_S(23) = 1.56419×10¹¹` against `N_S(24) = 156 438 903 314`, ratio `0.99987`,
with `n_χ` agreeing to three significant figures at `3.104×10⁷`.  The section
now says so; its *deduction* — full rank at 23 forces `i_det(24) = 1` — is
untouched and remains the useful half.  Session 70 is reading this file.

**`results/s60_tail_census.md` undercounted the buildable closing cells.**  It
records 892, computed against session 60's conservative `CODE_SAFE_DELTA = 18`;
the true int64 reach at `r = 5` is `δ ≤ 19`, and session 67 then widened the
monomial code so **all 1 075 build**.  The census carries the correction in its
header, and `analysis/wk9_s60_tails.py` now carries a `REGEN_ALL_BUILDABLE` flag
so a regeneration cannot silently reproduce 892.  Session 71 uses this file as
its work queue.

**Session 62's 44 Gram certificates did not certify what their titles claimed.**
Produced in wave 1, before session 67's declared-field rule landed, they carried
neither `matrix_role` nor `field` — so the verifier read them as plain matrix
ranks, which is exactly the reading that stops an unlabelled Gram from being
taken for `rank Θ⁺`.  Relabelled `matrix_role: "gram"`, `field: "Q"`
(`analysis/wk11_int_s62_relabel.py`); all 44 re-verify `PASS`.  Sound because
each claims a rank over `Q` with an integer minor exhibited, and the
characteristic-zero Gram identity is what the label asserts.

**My own arithmetic slip.**  `docs/s67_S4_S5_S6_review.md` said
`CODE_SAFE_DELTA = 18` was "conservative by two"; it is conservative by one
(18 against a true reach of 19 — 20 is where the overflow begins, which is the
number I had subtracted from).

**The family-wide stable threshold, which S6 measured and did not draw.**
Added to `docs/stable_coordinates.md` §2: with `t_n = |ρ_n| = 2n²−1` and
`δ_n = 2n(n−1)`, `t_n − δ_n = 2n−1 > 0` at every `n`, so **every LMR cell lies
strictly below its proved stable threshold** and the monotonicity route is
available for the whole family, not for `n = 4` alone.  Checked at
`n = 2,3,4,5`.

## 2. Placed in the single-writer files

**`paper/det4-onset.tex`, §"Containment at `r≤4`, non-containment at `r=5`" —
a status remark.**  The section states the non-containment as an *unconditional*
theorem resting on a classification of the 4-dimensional singular matrix spaces.
The current record does not support the adverb.  The new remark
`rem:noncontain-status` records what is now proved (the contact-order lemma; the
eight-component list with `SP` plus a 49-dimensional semi-primitive component
absent from every earlier stratum list; `P ∩ ker` a rank-`≤2` locus, not the
rank-3 incidence it was taken for), the measured non-reducedness of the base
scheme at every pairwise incidence with its four `dim Q₂` numbers, and — the
consequence — that the bound must be quantified over the **normal cone**
`Proj gr_J R`, not over the reduced singular locus.  It names the four residual
loci and states plainly that the non-containment holds modulo the
exhaustiveness of the stratum classification, which the record has already had
to extend once.

*This is the item worth a second reading.*  Sessions 66 and 72 both treat the
`r = 5` upper bound as open; the paper asserts it as closed.  I have not touched
the theorem statement, only recorded what it rests on.

**`paper/det4-onset.tex`, §"Negative results" — two additions.**  First, the
`n = 3` `D = +1` written up as what it is: the method exhibited on a separation
of its own size, with the two halves of the rigour separated (a modular rank on
the permanent side, `LMR`'s own bound on the determinant side), the terminology
correct (a *multiplicity* obstruction, not an occurrence obstruction, since both
multiplicities are nonzero — the reading `BIP` leaves open), and the honest
statement that `59 > 47` already gives the separation by a dimension count so
the content is the certificate.  Second, session 63's drafted paragraph on what
the length-nine cell reduces to: a single rank lower bound `rank Θ⁺ ≥ 273`, in
its room-one form, with the Schwartz–Zippel caveat travelling with it as the
batch-10 review required.  The file compiles.

**`PROJECT_NOTES.md` — the standing context now describes the active
programme.**  It had not been updated since session 23 and still opened on the
conductor thread, while sessions 24–73 have been the separation programme.  It
now opens with a thread-2 status block (the quantity, the goal cell, the first
`D > 0`, the bottleneck in one line, what is proved, what is dead, what is open)
and a thread-2 roadmap, with the conductor material intact below and labelled as
thread 1.  The process section carries the four rules batch 10 paid for.

**`docs/artifacts.md`** — an honest compliance scorecard for batch 10, the
`PASS`/`RECORDED` distinction recorded as a standing convention rather than a
batch detail, and the `n = 3` acceptance with its first certificates.

## 3. Relayed to the running sessions

`docs/batch11_integrator_note1.md`, to sessions 68, 70, 71 and 73: the two
document corrections above; the three cost measurements that fell out of session
68's brief in the rewrite (`|R(S)|`, the distinct row-profiles of `β_S`, and the
inter-rung support overlap); and the caution that session 73 must not compare
`U_P` against the `n = 3` artefact, which lives in a different cell and
different coordinates.

## 4. Recorded, not repaired

**Sessions 63, 64 and 66 shipped no certificates at all**, against the batch-10
coordination rule that every new `Θ⁺`, Gram and padded output must land as a
certificate with a declared field.  The 48-cell padded calibration — including
the two kernel witnesses I re-verified independently — is uncertified.  This
cannot be fixed from here: back-filling needs the producing session's artefacts,
not its report.  It is recorded in `docs/artifacts.md` and is the clearest
process failure of batch 10 after the plan-not-pushed one.

**The composite padded identity is unowned.**
`mult_pad = rank[(⊕_μ Θ^{per₃}_{μ,δ}) ∘ S_{λ,δ}]` was left "unchecked and handed
to session 65", which never ran.  Session 70 calibrates the `S` stage alone and
the plan is explicit that this does not establish padded full rank, so the
permanent-specific stage is assigned to nobody.  Note 1 §5 asks whichever of 70
or 73 touches the padded side first for a one-line disposition.

**Session 62's handoff of `(12,4)` at `δ = 4` to S1** was never consumed; S1
tested only the three weight-13 tails.  Low value now that those are closed, but
the handoff is dangling and is recorded here rather than silently dropped.

**The Sol reports S1–S6 are not committed anywhere.**  Every Claude session's
report is in `docs/`; the Sol side survives only through my assessments, which
attribute substantive corrections to memos a reader cannot consult.  Worth
fixing at the next batch boundary if the memos still exist.
