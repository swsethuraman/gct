# Integrator note 2 — corrections taken, and the birth test run on real candidates

8 September 2026.  Three things: the corrections to my S1 review, which I accept;
what happened when I ran the proposed experiment and then kept going; and S2.

---

## 1. Corrections accepted

**The quotient certifies newness, not membership.**  Right, and my phrasing was
wrong.  A filling with nonzero class *spans* the birth quotient when `b_d = 1`;
it is not thereby an element of any ideal.  An ideal element of that class
differs from it by a transported `u w`, `w ∈ M_{d−1}`, and finding `w` needs the
lower source.  "The single `δ = 24` birth direction *is* the determinant ideal
vector" is true of the class and false of the representative.  Withdrawn, and
corrected in `PROJECT_NOTES.md` and `docs/s1_batch12_review.md`.

What survives untouched: `i_X(d) − i_X(d−1) ≤ b_d`, and the `δ = 23` shortcut —
`rank T_det|_{uM₂₃} = 273 − i_det(23)`, so certifying determinant rank 273 at
degree 23 settles it at degree 24 without the final birth.

**The 23-fold compression is a coordinate-implementation saving, not an
evaluation speedup.**  Also right.  The compact circuit evaluator never forms
those coordinates.  I claim no circuit speedup; using the restriction inside that
evaluator would need its own algorithm and benchmark.  Narrowed in both files.

**"The only thing between us and `D(24)`" was too strong.**  Determinant and
true-padded evaluation and certification remain.  Conceded.

**The board numbering collides and that is a real hazard.**  My
`docs/batch12_claude_board.md` renumbers: my `s77` is the Pieri-to-circuit
bridge, the finalized `s77` is r = 5 completeness.  Nobody should have to guess.
From here on I name every session by mission and carry the mapping explicitly:

| finalized | mine | mission |
|---|---|---|
| s74 | s74 | sampling to the LMR decision |
| s75 (both halves) | s75 | the `δ = 12` compact control |
|  | s76 | scale the recursion to `δ = 24`, and exact `C₂₄` |
| s76 | s77 | deterministic circuit basis — bridge first, then straightening |
| s77 | s78 | r = 5 Rees / special-fibre completeness |
| s78 + s79 | s79 | the two independent frontiers |

The briefs will carry this table on the first page.

---

## 2. The experiment, and what it found

The proposal was sharp: of s69's 113 saved `δ = 24` fillings, only five have no
visible pure-`u` letter; the other 108 are `n! u (something)` and vanish
identically in the birth test.  Test those five.

**Census confirmed exactly.**  108 with a pure-`u` letter, 5 without —
indices 18, 49, 50, 57, 67.  The distribution is worth seeing: 5 fillings have
none, 20 have one, 39 have two, 31 have three, 16 have four, 2 have five.

**One of the five is nonzero mod `u`, at both primes.**

    filling 57   P1: 24/24 nonzero at u = 0    P2: 24/24
    fillings 18, 49, 50, 67   0/24 at both primes
    control: 20 pure-u fillings, 0 nonzero  (they must vanish identically, and do)

A nonzero residue at an integer point proves `F₅₇|_{u=0} ≠ 0` over `Q` — a
certificate, not sampling.  So `F₅₇ ∉ uM₂₃`, and since `b₂₄ = 1`,

    M₂₄ = uM₂₃ ⊕ ⟨F₅₇⟩.

**The `δ = 24` birth class has an explicit representative**, banked at
`results/wk12_int_lmr_birth24.json` (`k = |C₁ ∩ C₂| = 9`).  Per §1 this is a
source statement, not an ideal statement.  It is the one direction the padded
side cannot skip.

The four clean-but-vanishing fillings are the useful negative: **the syntactic
filter is necessary and far from sufficient.**  It removes 96% of the saved
candidates for free, and 4 of the 5 survivors still vanish.

### Then I kept going, on fresh candidates

The saved fillings only cover `δ = 24`.  The real question is whether the birth
test helps when candidates must be *generated*.  So: draw random fillings at a
rung, reject pure-`u` syntactically, evaluate on `b_d + 8` points with `u = 0`,
keep one only when it raises the birth rank, stop at `b_d`
(`analysis/wk12_int_birth_probe.py`, seeds recorded).

| `δ` | `b_δ` | birth rank reached | draws | past the filter | time |
|---:|---:|---:|---:|---:|---:|
| 23 | 1 | **1 / 1** | 33 | 10 | 5.9 s |
| 22 | 3 | **3 / 3** | 142 | 42 | 31.8 s |
| 21 | 5 | **5 / 5** | 131 | 47 | 41.5 s |
| 20 | 9 | **9 / 9** | 41 | 26 | 31.0 s |
| 17 | 31 | 17 / 31 | 39 | 36 | time-capped at 150 s |
| 14 | 54 | 14 / 54 | 15 | 15 | time-capped at 150 s |

**The four top rungs of the LMR ladder — 18 of the 274 directions — completed in
under two minutes.**  Nothing stalled; the two incomplete rows are wall-clock
caps, and at `δ = 14` every one of the 15 filtered draws raised the rank.

That is the tail the programme has been describing as its remaining cost.  It was
never a coupon-collector problem in the usual sense: it was that almost every
candidate lay in the transported source, and the birth quotient both explains
that (a pure-`u` letter *is* transport) and removes it (a syntactic filter, then
a `b_d`-dimensional test).

**What this does not do**, and I want to be exact after §1.  It does not build
`M₂₄`: the per-rung classes still have to be transported up with the correct
`(n!)^{D−d} u^{D−d}` normalization — S1's warning, which is where a silent error
would live — and assembled into one row system.  It does not touch either
evaluation column.  It is single-prime for the exploratory rungs; the two
`b = 1` hits are confirmed at both.  And a birth representative is not an ideal
element.  What it does establish is that **discovery is no longer the binding
constraint**; the binding constraints are assembly, and the determinant and
true-padded ranks.

s74's brief changes accordingly: replay the saved candidates through the birth
test first, then work *down* the ladder from `δ = 24` with the rungs that are
already done, and spend the budget on the middle rungs where `b_d` is 43–54.

---

## 3. S2

A strong session, and mostly a corrective one.  Four things I would bank and one
that changes my board.

**Bank.**  The integral-cubic rank theorem (ranks 0 and 9 only, parameter kernel
3) and the uniform order-two image bound ≤ 29 on that locus — these replace
sampling with proof on a stated open locus.  The certified rank-3 counterexample,
which falsifies an unqualified rank dichotomy and shows ranks 1–8 cannot be
discarded globally.  The vertex correction: the exceptional fibre over the zero
pencil *is* `P(D₅)`, so bounding it as an independent low-rank residue is
circular, and projectivizing the source removes it.

**The correction that changes my board.**  s72's interior value 31 was obtained
by a probabilistic protocol — pointwise Jacobian ranks as lower bounds plus a
Schwartz–Zippel argument against a missed higher minor — not an exact identity
over `Q`.  I have been quoting `dim(D₅ ∩ W) = 31 < 35` as the second-most-likely
theorem in the batch.  It is source-recorded evidence, not a deterministic bound,
and my r = 5 session must now deliver *both* completeness and an exact image
bound.  S2 says the same and supplies the sufficient global bound: 34.

**And it makes that session concrete rather than open-ended.**  S2's finite
fallback is two explicit projective-source chart elimination ideals that decide
noncontainment, covering all schemes and all contact orders without the old
support enumeration — with complete rational inputs generated.  They were not
run, because that host had no CAS.

    This host does.  Singular and msolve are both installed here and
    both work; sympy and python-flint are present.

So the r = 5 session is no longer "prove a completeness statement."  It is: run a
resource-bounded pilot on one of the two chart jobs, under S2's own economics
warning — 149 variables in lex order, begin with algebraic reductions, a bounded
pilot first, preserve the exact residual ideal if the pilot fails, and never
launch an unbounded lex run merely because the inputs exist.  That is a well-posed
implementation session with a real chance of closing `R₅ ⊄ D₅`.

**One thing I will not do**, and the briefs will say so: promote the recorded 19
on `P ∩ C21`, or any of the recorded interior values, into a deterministic global
proof.  S2's requirement is the right one — every fixed-factor image needs affine
dimension ≤ 34 by exact target elimination, and a slice dimension with a few
reconstructed points is not a component certificate.

---

## 4. Ledger

| | status |
|---|---|
| `F₅₇` represents the `δ = 24` birth class, `M₂₄ = uM₂₃ ⊕ ⟨F₅₇⟩` | **CERTIFIED** (both primes, 48 points, controls clean) |
| birth ranks complete at `δ = 20, 21, 22, 23` | **MEASURED**, single prime, seeds recorded |
| discovery is no longer the binding constraint on the LMR source | **MEASURED**, and stated as an economics claim, not a theorem |
| a birth representative is an ideal element | **FALSE** — withdrawn, §1 |
| 23-fold compression speeds up circuit evaluation | **NOT CLAIMED** — coordinate implementations only, §1 |
| `rank T_det|_{uM₂₃} = 273 − i_det(23)`; the `δ = 23` shortcut | **PROVED**, unaffected |
| `dim(D₅ ∩ W) = 31` as a deterministic bound | **NO** — probabilistic protocol; needs exact elimination, §3 |
| `R₅ ⊄ D₅` | **OPEN**, and now a specified two-chart computation with a CAS that exists here |
