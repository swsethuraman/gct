# Session 68 (C1) — the ladder source: seed at `δ = 12`, then births

Batch 11, **ungated, runnable immediately**.  This is one of three independent
approaches to the single bottleneck of the programme, and on the plan's own
ranking it is at the top with S1.  **Read `docs/batch11_worker_preamble.md`
first**, then `docs/batch11_plan.md` §2.1, §2.3 and §5(iii) — those three
sections are your brief's mathematics — then `docs/s57_report.md` (the ladder
theorem and Lemma L), `docs/stocktake_batch10.md` §4 (the diagnosis), and
`analysis/wk9_s45_build.py`, `analysis/wk9_s45_cell.py`,
`analysis/wk10_s63_support.py`.

## The question

Can the 274-dimensional LMR source `M_λ` at `λ = (65,17,2⁷)`, `δ = 24` be built
**incrementally**, one ladder rung at a time, without ever forming the full
carrier?

## What the batch already knows, and what it changes

`M_λ ≅ [λ]^{S₄≀S₂₄}` has dimension 274 from birth.  Every construction the
programme owns realises it as a kernel inside a carrier of size `≥ 10⁷`, and
that — not the rank, not the target, not the field — is why the cell is out of
reach.  Two measurements made while the plan was written change how you should
approach it.

**The ladder does not thin downward** (plan §2.1, `analysis/wk11_int_ladder_size.py`).
Along `λ_δ = (4δ − 31, 17, 2⁷)`:

    δ    12      13      14      16      19      24
    a_δ   2      39      93     188     255     274
    n_χ  5.10e6  1.61e7  2.11e7 2.75e7  3.06e7  3.10e7

The carrier is at 16% of full size where the multiplicity is 2, and at 89% by
`δ = 16`.  **Do not plan on the bottom of the ladder being cheap.**  Any saving
you achieve comes from support restriction, whose density was measured at
`0.20–0.26` — at `δ = 4`, not here.  Measuring it here is itself a deliverable.

**No rung introduces more than 54 new vectors** (plan §2.3).  The ladder theorem
gives `dim J(M_{δ−1}) = a_{δ−1}` exactly, so

    M_δ = J(M_{δ−1}) ⊕ B_δ ,    dim B_δ = a_δ − a_{δ−1}

and the birth sequence is `2, 37, 54, 52, 43, 31, 22, 14, 9, 5, 3, 1, 1`.  The
nullity you must find at each rung is `dim B_δ`, **not** `a_δ`, provided the
system is deflated by the `a_{δ−1}` vectors you already have.  That is the
algorithmic content of this session.

## Part A — the seed, pre-registered separately

`M₁₂` is a **2-dimensional** kernel inside `n_χ ≈ 5.10×10⁶` coordinates
(`N_S = 51 446 325 457`, `|Stab| = 10 080` because `λ₁ = λ₂ = 17`).  It is the
one genuinely hard object in the scheme, and it has its own budget and its own
verdict:

> Obtain the two `M₁₂` highest-weight vectors and certify them against the
> **full** raising action — not the support-restricted one — with `dim = a₁₂ = 2`
> exactly.  Any method is admissible: block Wiedemann (the repository builds the
> binary from `analysis/wk9_s42_wied.c` via `analysis/wk9_s42_sparse.py`),
> structured sparse elimination, or a construction of your own.

A nullity-2 kernel is the most favourable case a black-box method ever sees, and
`δ = 12` is the cheapest point on this ladder — the ladder begins there because
`4δ − 31 ≥ 17` fails below it, and every higher rung is more expensive.

**If the seed cannot be materialised inside the budget, say so and stop.**  That
is the first wall, it is a full result, and it must be reported as a seed
failure and **not** as a failure of the ladder algorithm, which will not have
been tested.  Report the cost curve you saw and where it went out of reach.

## Part B — the rungs

For `δ = 13, 14, …` as far as you get:

1. **Transport.**  Multiply each vector of `M_{δ−1}` by `u = c_{(4,0,…,0)}` to
   get `a_{δ−1}` vectors of `M_δ`.  Transport preserves monomial-support size
   exactly (adding one element to distinct multisets gives distinct multisets),
   so the support of `J(M_{δ−1})` is known before you compute anything.
2. **Deflate.**  Restrict the raising system to a complement of `J(M_{δ−1})` and
   solve for a kernel of dimension `a_δ − a_{δ−1}`.
3. **Certify the rung.**  Three things together, and all three are required:
   - the `a_{δ−1}` transported vectors lie in the restricted nullspace;
   - the restricted nullspace has dimension exactly `a_δ` (independently known);
   - each of the `≤ 54` new vectors passes the **full** raising action,
     including target rows outside the current support.

   A restricted nullspace of the right dimension proves nothing on its own
   unless every omitted raising equation is provably irrelevant.  The three
   conditions together do certify completeness, and they cost `≤ 54`
   full verifications per rung instead of 274.
4. **Measure, and record.**  At every rung: live support size as a fraction of
   `n_χ`, wall clock, peak memory, and the birth dimension you actually found
   against the known `a_δ − a_{δ−1}`.  The support fraction is the number the
   rest of the batch needs whether or not you reach 24.

## Part C — two free by-products

- **`i_pad(12)` and `i_det(12)`.**  Once `M₁₂` exists, evaluating it against the
  padded and determinant families is two evaluation rows on a 2-dimensional
  space.  Lemma L makes `i_X` non-decreasing along the ladder for every
  `GL`-stable ideal, so `i_det(12) ≥ 1` would be a determinant equation of
  degree 12 at `ℓ = 9` — far stronger than LMR and it would make this whole cell
  unnecessary.  `i_pad(12) ≥ 1` forces `i_pad(24) ≥ 1`, which with `i_det = 1`
  would settle `D ≤ 0` at LMR.  Both are cheap; do them at every rung you reach.
- **`A₂₄`, if you get there.**  The last two ladder increments are exactly one,
  so `δ = 23` and `δ = 24` are room-one rungs and `det A₂₄` — the degree-24 Gram
  restricted to `J(M₂₃)` — is your terminal step, not a separate computation
  (plan §2.2).  Session 70 is computing the same object; **use the plan's
  definition verbatim** so the two results compose.

## Success

The seed, certified.  Then as many rungs as the budget allows, each with its
three-part completeness certificate and its cost row.  All 274 vectors is the
full result; the first `k` rungs with an honest cost curve is a real one.

## Stopping rules

- The seed is unreachable in budget → stop, report Part A only (§Part A).
- Live support at a rung with small `a_δ` grows to carrier scale → the support
  restriction does not do the work, which is the plan's stated risk; report the
  measured densities and stop.
- Do **not** fall back to building the full carrier at any rung.  Session 63
  quantified that wall on all three existing realisations; reconfirming it is
  not a use of a night.

## Deliverables

`results/PREREG_s68.md` with Part A budgeted separately; `docs/s68_report.md`;
the seed vectors and every rung's basis as machine-readable artefacts under
`results/artefacts/`; the per-rung cost and support table as
`results/s68_rungs.md` and `.jsonl`; code under `analysis/wk11_s68_*.py`;
bundle `s68_ladder.bundle` + `.md5`.
