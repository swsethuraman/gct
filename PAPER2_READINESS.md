# B24-06 — Paper 2: submission readiness

The judgement is stated as a list of blockers, not as an opinion.
`paper/det4-onset.tex` is **not ready for arXiv**. It becomes ready when these are cleared,
and only the first five are mathematical: **(1)** Corollary 5.3 states the Kadish–Landsberg
padding bound backwards — it concludes `mult_λ C[R_r] = a(λ,δ)` where the record and the
paper's own Corollary 5.2 give `0`; **(2)** Theorem 9.1 is false as written, because it
quantifies over every degree while `I(D_4^{det_4})` is principal and nonzero, and the record
(`docs/blindness_slab.md` Theorem A) splits it at the adopted onset `e = 320112` — the
conclusion `Δ ≤ 0` on the slab survives through Proposition 6.1; **(3)** §9's "length ≥ 6"
excludes the length-five region where 2,571 of the record's 2,734 positive labels are still
open, and contradicts the record's own `ℓ ≥ 5` gate; **(4)** §9's LMR interval `[−4, +1]` is
stale against the committed `D_LMR ∈ [−4, −2]`, which excludes the positive case at that cell,
conditional on the adopted `dim N₁₃ = 73`; **(5)** Landsberg–Manivel–Ressayre is load-bearing at
four points and is UNREAD on the record except for Theorem 1.0.1, and Beauville — the standard
reference for the dimension of determinantal hypersurfaces, the singular locus of the generic
member, and the quinary cubic case, i.e. for Proposition 2.1, Theorem 7.1 Step 2 and
Theorem 7.3 — has no read-status anywhere on the record at all, which is precisely the
attribution failure B23-10 found in Paper 1 and only a full read will settle. The remaining
eleven are corrections and decisions: the wrong citation for the permanent's stabiliser
(Marcus–Minc, where the record names Marcus–May and Botta); Theorem 6.2's statement, which says
"five-dimensional" where its own next sentence says four, offers the classification's obstacle
as its reason, and writes `D^det_4` for `D^det_5`; two garbled formulas, in Proposition 2.1 and
in Lemma 3.3's proof; Remark 6.3, whose interior enumeration B23-03 Theorem 2.1 has since
proved and whose surviving caveat is the boundary gap G-A1; the cap minors' vanishing on the
plane family, now proved and unmentioned; §8's three contradicted quantitative claims about
`n_χ`; §1's and Question 10.5's understatement of a result the record proves for every length;
the malformed `\cite[\S]` locator and the two unlocatable companion references; "the second
author" on a single-author paper; and the acknowledgement line, which is the same credit
decision B24-12 §9 has already reserved for the user on Paper 1. **Not blockers, because the
paper already states them as open in its own voice:** Conjecture 7.2, the boundary obligation
in Remark 6.3, and the sampled-nullity caveat in §9, which is the paper at its most careful and
matches the record's `evaluation_cannot_certify_i_ge_1` exactly. Two things this slot could
**not** do, and they bound everything above: the 2026-09-17 stocktake that describes Paper 2
could not be found anywhere on disk, so the six candidate defects were checked against the
source rather than against it and there may be items it raised that are not on this list; and
no LaTeX toolchain is installed here, so the paper has not been compiled — brace and `$`
balance, label and reference resolution, bibliography keys and theorem numbering were checked
by script and all pass.

**Full lists:** `PAPER2_BLOCKERS.md` (16 blockers, ordered, author-decision items marked, plus
the stocktake verification and the Paper 3 overlap), `PAPER2_CLAIMS.md` (every numbered result
with its label, source, commit, lineage and staleness), `PAPER2_GAPS.md` (17 gaps and 7 record
defects).

**Provenance.** Worktree `work/batch15_workers/B24-06`, branch `b24-06-paper2`, HEAD
`82633a60893236fab4fbc317df416e1b8a349005`, tree `e82fd3291d1a2adc8a577647314c251366ff5142`,
`git status --porcelain` empty at start and at end. `paper/det4-onset.tex` sha256
`7c2bc7365c3aacc75e5d79906a4aaa3364ff015e5bbc91e2f585b1ca45678b7b`, unchanged. Read-only git;
no commit, no push, no computation, no pilot, no `.pid`. Nothing sealed was read or written.

**B25-02 update (2026-09-22, UNCOMMITTED, producer-only; the paragraph above is B24-06's and
unchanged).** Still **not ready**. Theorem 9.1 is repaired to the record's Theorem A (Δ ≤ 0 on
the slab by containment in every degree; `mult = a` at length ≤ 3 always and at length 4 only
below e, e ≥ 10 certified, e = 320112 adopted), and blockers 1, 3–9, 11–13 and 15 are repaired or
qualified in the TeX, with Beauville, Kadish–Landsberg, LMR and LLV read in the primary. What
still stands between the draft and submission: no compile has ever been run (no toolchain on
this host); Theorem 6.2 now proves only the determinant part, and the closure non-containment
it used to claim is carried as ADOPTED from an unreviewed programme result, with G-A1 open; C45
remains PROVED modulo (★); several results are cited only through unlocatable companion
material; and the author decisions B14/B16 and the Paper 3 overlap are unresolved. Details:
`docs/b25_02_report.md`.

**B26-05 current-state amendment (2026-09-22, PROPOSED, UNCOMMITTED, producer-only; the B24-06
paragraph and the B25-02 update above are kept as written).** The subject is the after-state
`paper/det4-onset.tex` at `79b68dcf` (raw CRLF sha256 `065f8799…`). **It is still not ready.** No
readiness is declared here. Five statements in the B25-02 update are now stale:
(a) "C45 remains PROVED modulo (★)". The `n = 3` control, `λ = (19,7,2^5)`, `δ = 12`,
`Δ = +1`, is now **PROVED**, because the length-restriction lemma is PROVED (B25-10 §2.4 @
`42e7f4ba`), and the TeX says so. That ruling covers the base rung only; any higher rung keeps its
s73 lineage, and Paper 2 claims none.
(b) "no compile has ever been run". The integrator built these bytes: 0 errors, 0 undefined
references or citations, 15 pages (`build_evidence_20260922_close`, `SHA256SUMS.txt`
`c4c56d0d…`; the artefacts are uncommitted).
(c) The closure non-containment is still ADOPTED, but it is now worded as B25-10 §4.3 requires
(PART 17b). Only the narrow, one-witness reading is used.
(d) "cited only through unlocatable companion material". B14 is repaired. Three placeholders
remain, to be filled at submission (G-P2-SUB): Paper 1's arXiv identifier, and the repository URL
in `Companion2` and `Companion3`.
(e) "the author decisions B14/B16 … are unresolved". B14 and B16 were decided and applied on
2026-09-22 (PART 17b).
**What still stands:**
(1) The `n = 4` sixteen-to-nine transfer **stays flagged** (G-P2-19). B26-04 is checking it, and
nothing from it has been independently accepted. Note also that §2 asserts the length reduction
(2.1) for `det_4` and `x_0 per_3` without a flag, and the paper uses it at several points. So the
flag at the length-nine cell is narrower than the paper's own unflagged uses of the same
transport. See `docs/b26_05_report.md` §5.
(2) Terminology. Three `$(\star)$` occurrences (L1003, L1020, L1061) should read "the
length-restriction lemma", as Paper 3 writes it. A proposed diff is in
`results/b26_05/proposed/`. The label `thm:star` (Theorem 5.1, the reducible criterion) is a
different object and is not renamed.
(3) [AUTHOR]/locator: `Companion2` must actually contain the `s_5·C*` witness (B25-10 §4.3).
(4) [AUTHOR]: the Paper 2 / Paper 3 overlap. Advice only is in `docs/b26_05_report.md` §4. It
found no contradiction between the two papers, but it did find label and scope discrepancies and
no cross-reference in either direction.
(5) The G-P2-SUB placeholders, at submission.
(6) B25-02's remaining outcome-(2) items (`docs/b25_02_report.md` §6), which were not re-assessed
here.
