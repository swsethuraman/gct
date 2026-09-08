# Batch 11 — integrator note 1, to sessions 68, 70, 71 and 73

Written after the batch-10 housekeeping pass, while you are running.  Four
items: two corrections to documents your brief points you at, one measurement
your brief dropped, and one caution.  Nothing here changes a pre-registration;
if an item arrives after you have already committed to a plan, record it and
carry on.

---

## 1. To session 70 — `docs/lmr_cell.md` §3a was wrong about cost, and is fixed

§3a used to be headed "the sharper and **cheaper** experiment".  The first half
is right; the second is false and is now corrected in the file.  The `δ = 23`
predecessor is one column narrower as a matrix, but it is **not a cheaper
cell**:

    N_S(23) = 1.56419×10¹¹      N_S(24) = 156 438 903 314      ratio 0.99987
    n_χ agrees to three significant figures at 3.104×10⁷

(`analysis/wk11_int_ladder_size.py`; session 57 sized it the same way and called
it "the same as the LMR cell itself".)  So if you were planning to reach `δ = 23`
as a cheaper route to the same conclusion, that plan does not exist.  What §3a
still gives you — and this is the useful half — is the *deduction*: full rank at
23 forces `i_det(24) ≤ 1`, hence `= 1` with LMR's lower bound, using only the two
ambient values and monotonicity.

## 2. To session 71 — the closing-cell census undercounts, and is annotated

`results/s60_tail_census.md` says `buildable closing cells: 892`.  That is
session 60's number, computed against its conservative `CODE_SAFE_DELTA = 18`
(the true int64 reach at `r = 5` is `δ ≤ 19`; overflow begins at 20).  Session 67
then widened the monomial code — byte-for-byte identical wherever the int64 path
already worked — and **all 1 075 closing cells build**.  Your brief already says
1 075; the census file now carries the correction in its header, and
`analysis/wk9_s60_tails.py` carries a `REGEN_ALL_BUILDABLE` flag so a
regeneration does not silently reproduce 892.  Every other column of that census
stands and it is your work queue.

## 3. To session 68 — three cost measurements that fell out of your brief

Integrator note 3 of batch 10 listed five measurements for the restricted-solve
route; your brief carries two of them (live support as a fraction of `n_χ`, and
the birth dimension against `a_δ − a_{δ−1}`).  These three were dropped in the
rewrite, and since your whole method **is** the restricted solve, they are the
other half of its cost model:

- **`|R(S)|`, the number of equation rows touched by the restricted support `S`.**
  Nobody has named this number.  Support size bounds the columns; `|R(S)|` bounds
  the rows, and the two together decide whether the restricted solve is actually
  cheap or merely narrower.  Report it at every rung.
- **The distinct row-profiles of `β_S`** — of the Gram restricted to `S`, not of
  `T_S`.  The count of distinct profiles is what says whether the restricted
  system has exploitable structure or is just smaller.
- **Overlap statistics between the source supports** at consecutive rungs: how
  much of `supp J(M_{δ−1})` the new births actually reuse.  Transport preserves
  support size exactly, so this is cheap to compute and it predicts the next
  rung's cost.

Add them to your per-rung table if you can.  If you cannot, say so and the drop
is deliberate rather than silent.

## 4. To session 73 — do not compare `U_P` against the `n = 3` artefact

There is **no `n = 4` line in common source coordinates**.  The banked
`results/artefacts/s63_n3_ideal_vectors.npz` is the `n = 3` calibration and is
not a substitute for one: it lives in a different cell, a different ambient
space and different `χ` coordinates.  In Mode A, `U_D` and `U_P` must both come
from the LMR source that arrives, and `dim(U_D ∩ U_P)` is meaningful only inside
that one space.  In Mode B the comparison is internally consistent by
construction and this caution does not bite.

---

## 5. A disposition the plan owes, for whoever reaches it first (70 or 73)

Session 64 left an identity **unchecked and handed to the session that never
ran**:

    mult_pad = rank [ (⊕_μ Θ^{per_3}_{μ,δ}) ∘ S_{λ,δ} ]

Session 70 calibrates the `S` stage alone, and the batch-11 plan is explicit
that a full-rank `S` does not establish padded full rank because the
permanent-specific `⊕Θ^{per_3}` stage can still drop rank afterwards.  But the
composite identity itself — the thing session 64's 48 `r = 5` cells were made a
testbed for — is currently assigned to **nobody**.

It is not work either of you should take on unasked.  What is asked: whichever
of you touches the padded side first, state in your report whether the composite
identity is (a) reproduced, (b) needed for your conclusion, or (c) neither.  A
one-line disposition is enough; what must not happen again is a load-bearing
identity sitting unowned across two batches.
