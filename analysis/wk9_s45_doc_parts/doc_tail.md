
## 5. The balanced corner as this session leaves it

The reason the balanced cells were out of reach is structural, not incidental:
the stabiliser reduction divides the weight space by `|Stab_W(λ)|`, which is `1`
when the parts of `λ` are distinct and small when they are nearly distinct.  So
the cells with `λ_1 − λ_ℓ` small — exactly where a determinant equation is most
plausible, because the `SL_4 × SL_4 ⋊ Z/2` stabiliser of `det_4` leaves most room
in the near-rectangular weights — get the least reduction, and their `n_χ` is
the largest in the region.  That is why session 41's `n_χ ≤ 20,000` frontier saw
nothing below balance 8, and why every cell it measured at balance 8 or 9 had
`n_χ` under 5,000 (`(9,9,7,1,1,1)_7`, `n_χ = 3086`) or sat at the edge.

PLACEHOLDER_CORNER

## 6. Honest boundary

**The certificates are one-sided by construction.**  `nullity_p([E; ev]) = 0`
proves `mult_det = a` over `Q` at a single prime, with no probabilistic step in
the implication (Lemma 2, Lemma 4).  A *positive* nullity would prove only
`mult_det ≥ a − k`; the reverse needs exhibited rational vectors, exact
verification and fresh randomness, and that branch was pre-registered
(`results/PREREG_s45.md` §6) but never taken on the determinant side this
session — every swept cell came out full rank.  The branch is not untested: V2
exercises it end to end at six cells where the answer is a drop.

**Randomness enters only through conclusiveness, never through correctness.**
`D_1, D_2, u, b`, the row sampling and the seeds decide whether a run reaches a
verdict; they cannot make a wrong verdict.  A kernel candidate is reported only
after `F y = 0` is checked against the **full** `[E; ev]`; a nonsingularity
certificate is emitted only after Berlekamp–Massey's output is checked to
annihilate the whole sequence.  Berlekamp–Massey is the one hand-written exact
routine in the chain, and V4 is its validation (300 matrices, planted nullities
0–6, against `python-flint`).

**What a `mult_det = a` row does and does not say.**  It says the determinant
ideal `I(D_6^{det_4})` is empty in that cell, so no obstruction can live there:
`mult_pad ≤ a = mult_det` forces `D ≤ 0`.  It says nothing about neighbouring
cells, and nothing about degrees above 8.  The six-row onset is bracketed from
below only; this session pushes that bracket outward in the balanced direction
without closing it.

**The `a + 8` points are a convention, not a theorem.**  `K = a` points suffice
for the rank of the evaluation pairing at a generic draw, and the eight extra
are the house margin (`wk8_s30_core.measure`).  A degenerate draw would *lower*
the measured rank, i.e. report `mult_det < a` — so it can only produce a false
*bite*, never a false `mult_det = a`, and the pre-registered sceptical branch
(fresh points, fresh seeds, a second prime, 20 fresh pencils) exists precisely
to catch that.  No such branch was needed.

**The build's ceiling is now `N_S`, and it is a soft one.**  Nothing in the
route needs `O(N_S)` memory in principle — the monomial array could be
streamed to disk and the group passes done blockwise — so the cells beyond this
session's reach are beyond its *time*, not its method.  The one place the
current implementation genuinely stops is `|Stab|` large *and* `N_S` large
together: `(8,4,4,4,4,4)_7` (`N_S = 10,060,304`, `|Stab| = 120`, balance 4, the
most balanced obstruction-eligible `δ = 7` cell of all) enumerates its monomials
in 11 s but needs 240 group passes over that array, and it did not finish inside
this session's build budget.  It is the natural first target for a successor.

**Two conventions inherited without re-derivation** (adopted-from-literature
within the programme): the corrected raising rule
`E_ij c_α = (α_i + 1) c_{α + e_i − e_j}` (`wk8_s30_core`, calibrated by the
`l^3 m` witness in V1), and the stabiliser-reduction lemma
`HWV_λ ⊆ V_χ` (`docs/stabiliser_reduction.md`).  Both are load-bearing here and
neither is re-proved in this document.
