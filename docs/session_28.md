# Session 28 (2026-08-31/09-01) — `D_5`, and making the length theorem sharp

Branch `s28-d5`, fresh clone of public `origin/main`.
**Tip at clone `1203fe4`; ancestry check PASSED** — `6aaab97` is an ancestor,
and `1203fe4` (the integrator review of sessions 25 and 26) is the only commit
above it. No rollback alarm.

Container only; `Projects\gct` not owned and not written (rule 9).
`paper/det3-conductor.tex` **not touched** — the X_-3 grind owns it.
`PROJECT_NOTES.md` and `docs/boundary_deficit.html` not appended to.
Calibration (`analysis/wk6_s26_regress.py`) run and passed **before** anything
new was trusted: all checks, 17 s, including `1, 6, 31, 141, 618, 2488` and the
Jacobian tables.

Deliverables: `results/PREREG_s28.md`, `docs/d5_ideal.md`,
`docs/paper_section4_draft.md`, this record, `analysis/wk7_s28_*.py`, and the
corrected `docs/isotypic_rank.md` §4.

---

## 1. Headline

**Theorem 6 is sharp, and the proof is three lines of classical geometry rather
than a computation.**

> The rank-`<=1` locus of `M_3` is the cone over the Segre `P^2 x P^2 ⊂ P^8`,
> of dimension 4. A five-variable pencil spans a linear `P^4 ⊂ P^8`, and
> `4 + 4 >= 8`, so they meet. At a rank-1 point every `2x2` minor vanishes,
> hence every cofactor, hence every partial of `det`. **Every member of `D_5`
> is a singular quinary cubic**, so the discriminant of quinary cubics — degree
> `5 · 2^4 = 80`, weight `(48^5)`, length exactly 5 — lies in `I(D_5)`.

That is an explicit, nonzero, length-5 element of the ideal. Session 26's honest
boundary item — *"what is not proved is that the ideal actually does bite at
length 5"* — is now proved. And the same count says why `r = 4` is different: a
generic `P^3` misses a codimension-4 subvariety, which is exactly why smooth
determinantal cubic surfaces exist and smooth determinantal cubic threefolds do
not.

**What is not settled** is the *smallest* such degree:

    6 <= delta_0 <= 80   unconditionally;   8 <= delta_0 <= 80   given the
                                            published deficit sequence.

Per kill criterion 1 this is reported as a range. 80 is one explicit equation,
not a computed first degree, and I am not reporting it as the answer.

**A third thing, unlooked-for.** At `delta = 10` three weights have `a = 1` and
`m_det = 0` — `(13,3,2^7)`, `(12,5,2^6,1)`, `(9,9,2^6)` — so `mult = 0 < a` and
the whole isotypic component lies in the ideal. **This is the first degree at
which any part of `I(cO)` is pinned exactly**, and it is at lengths 8 and 9 by
the cheapest possible mechanism: the orbit has no functions of that weight at
all. Note the deficit there is `0`, not full (`def = m − mult = 0 − 0`) — an
ideal element carrying no deficit, which is worth keeping distinct from the
length-5 phenomenon this session was hunting. Verified by two independent
routes (mine and `scripts/ambient_screen.py`).

## 2. Literature pass (done before computing, as instructed)

The variety is classical; the ideal is not.

- **Beauville, Determinantal hypersurfaces, Michigan Math. J. 48 (2000):** the
  generic degree-`d` hypersurface in `P^m` is a linear determinant **only if
  `m = 2`, or `m = 3` and `d <= 3`.** For cubics that is `r <= 4` exactly —
  **Theorem 6's length bound is Beauville's theorem**, and session 26's Jacobian
  crossover was measuring a classical statement. The paper can now cite it.
- **arXiv:0906.3012 (determinantal representations of singular hypersurfaces):**
  in higher dimension determinantal hypersurfaces are necessarily singular, with
  singular locus of dimension at least `m − 4` — isolated points at `m = 4`,
  which is what §1 exhibits.
- No published generating set for `I(D_5)` in the `GL_5`-graded form this
  programme needs.

## 3. Prediction ledger

| # | pre-registered | outcome |
|---|---|---|
| P1 | first length-5 bite at `delta = 8`, alternatives 9 then 10, by the *arithmetic* mechanism `a > m_det` | **REFUTED, twice over.** No `a > m_det` at length 5 through `delta = 10`; no measured bite either. And the mechanism prediction was wrong: the bite that *is* proved comes from the discriminant, i.e. from geometry, not arithmetic. F1 fired. |
| P2 | lowest-degree piece of `I(D_5)` small — one or two length-5 weights, multiplicity `<= 3` | **UNTESTED** — `delta_0` not attained. The witness found is 1-dimensional (`disc` spans one copy of `det^48`), consistent in spirit but not a test of the claim. |
| P3 | `D_5` classical as a variety, not as an ideal | **HIT** — Beauville's theorem is exactly the boundary; no generating set found. |
| P4 | the `delta = 6, 7` residue confirms `mult = a` | **HIT so far** — 17 further weights at `delta = 6` and 16 at `delta = 7`, every one `mult = a`. F4 did not fire. |
| P5 | consistency of the totals identity either way | recorded: the `delta = 10` bites are at `m_det = 0`, where `min(m_det,a) = 0 = mult`, so the identity is unaffected. |

**One from four, and the one that mattered most was refuted.** The
pre-registration's confident `delta = 8` rested on "the plethysm is already
level with the Kronecker count at 59 of 172 short weights, so it should overtake
within a degree or two". That reasoning was about *short* weights and I applied
it to *long* ones without checking that the tie pattern transfers. It does not:
at length `>= 5` the ties only begin at `delta = 8` (one of them) and even at
`delta = 10` there are 16 ties and the only strict wins are the degenerate
`m_det = 0` ones. The arithmetic route is simply not how length-5 bites.

**Kill criteria.** Criterion 1 applies and is honoured — the range is reported,
the bound is not claimed as attained. Criterion 2 did not fire: `I(D_5)` is
provably nonzero, so the Jacobian rank 29 and Theorem 6's boundary stand (and
are now independently confirmed by Beauville). Criterion 3 did not fire: nothing
in the residue disagrees with the published sequence.

## 4. What was done, in order

- **Task A (done first, committed separately).** `docs/isotypic_rank.md` §4 now
  states the bound for `r >= 3`, with the stabiliser argument written out as
  Lemma 5b and the `r = 2` exception explained rather than quietly patched.
  Error found by the integrator; recorded as theirs to find and mine to fix.
- **Tasks B and C** are the same computation (`I(D_5)` is concentrated at
  weights of length exactly 5 — proved in `docs/d5_ideal.md` §3), and both are
  answered in `docs/d5_ideal.md`.
- **Task D**, partially: `delta = 6` is down from 16 unmeasured units of ambient
  room to **3**; `delta = 7` from 96 to **80**. Every newly measured weight
  returns `mult = a`, by a certificate (the rank attains `a`, and `mult <= a`).
- **Paper-ready text** in `docs/paper_section4_draft.md`, written to be copied.

## 5. Honest boundary

- **Proved outright, no computation:** the singularity lemma and
  `disc ∈ I(D_5)`; the length-5 concentration of `I(D_5)`; Lemma 5b and its
  `r = 2` exception.
- **Proved by certificate:** every `mult = a` reported. The rank is a rigorous
  lower bound and `mult <= a` an upper one, so attaining `a` is a proof, not a
  sample. Every measurement in this session attained `a`.
- **Proved arithmetically, two routes:** the three `delta = 10` components.
- **Not determined:** `delta_0`. The bracket is honest at both ends — the lower
  end is where measurement stopped, the upper end is one equation that is
  certainly not the lowest.
- **Not closed:** 3 units of residue at `delta = 6` and 80 at `delta = 7`, so
  Corollary 9 still leans on the published sequence there, less than before.
- **An engineering failure, recorded rather than hidden.** I wrote a blocked
  BLAS-based modular elimination (`wk7_s28_rank.py`) to clear the residue — the
  deferred rank-1 update flushed `block` at a time as one float64 matmul, which
  is exact for `p = 46337` and would have been roughly 30x faster. Its own
  self-test caught two bugs: the first real (updates restricted to unflushed
  columns left pivot rows unscaled), the second not diagnosed within budget. I
  **deleted the file rather than ship code whose self-test fails.** The residue
  is therefore still open, and still pure compute: the wall is an `O(N^3)`
  scalar elimination at `N` up to 4456, not the mathematics. A successor should
  either write this correctly or use an existing exact linear-algebra library.
- **Time went to the wrong place.** Roughly a third of the session went into
  that optimisation and into measuring long weights, i.e. into task D — which is
  cleanup — while the session's actual result (§1) is a three-line argument that
  needed no computation at all and could have been found in the first ten
  minutes. The lesson is the same one session 26 recorded from the other side:
  the expensive route and the informative route were not the same route.

## 6. What to do next

1. **Find a lower-degree element of `I(D_5)`.** Six nodes are six conditions;
   the discriminant is the shadow of one of them. A `GL_5`-covariant vanishing on
   six-nodal quinary cubics, of degree well under 80, would collapse the
   `delta_0` bracket at once. This is the highest-value open question the
   session leaves.
2. **Then, and only then, measure.** Length-5 weights from `delta = 8` are
   affordable at the cheap end (a few hundred to a few thousand columns); the
   wall is the elimination, not the weights.
3. **The invariant-theoretic route**, unused so far: `C[D_5]` is the subring of
   the `SL_3 x SL_3` semi-invariants of `(M_3)^5` generated in degree 1, and
   `delta_0` is the first degree where that inclusion is proper. Semi-invariants
   of quivers have combinatorial descriptions this programme has not touched.
4. **For the paper:** `docs/paper_section4_draft.md` is meant to be copied.
   Theorems D and E there are the length theorem and its sharpness; the open
   `delta_0` bracket should be stated as open if they are used.

## 7. Assets

    analysis/wk7_s28_bite.py     the arithmetic sweep (a vs m_det, length >= 5)
    analysis/wk7_s28_measure.py  the rank measurement with row subsampling and
                                 the rank(R) = N_S - a self-check, plus the
                                 certification rules
    analysis/wk7_s28_sing.py     the rank-1 point / singularity verification
    docs/d5_ideal.md             D_5, the sharpness proof, the delta_0 bracket
    docs/paper_section4_draft.md publication-form Lemmas A-B, Prop C, Thms D-E
    docs/isotypic_rank.md        corrected in place (task A, Lemma 5b)
    results/PREREG_s28.md        pre-registration
