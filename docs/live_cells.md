# The first live cells: measured

Session 26 (2026-08-31), branch `s26-tworank`.
Lemma and proofs: `docs/isotypic_rank.md`. Record: `docs/session_26.md`.
Pre-registration: `results/PREREG_s26.md` (committed before any computation).

---

## 1. The five cells

`a` = ambient room (multiplicity of `S_lam` in `Sym^delta(Sym^3 C^9)`);
`m_det` = the Peter–Weyl count `dim (S_lam^*)^{Stab(det_3)}`;
`mult` = multiplicity in `C[closure]_delta`; `def = m − mult`.

| `lam` | `delta` | rows | `a` | `m_det` | **`mult_det`** | **`def_det`** | `mult_per` |
|---|---|---|---|---|---|---|---|
| **(12,6)**   | 6 | 2 | 2 | 2 | **2** | **0** | 2 |
| **(15,6)**   | 7 | 2 | 2 | 2 | **2** | **0** | 2 |
| (9,4,2)      | 5 | 3 | 2 | 3 | **2** | **1** | 2 |
| (12,4,2)     | 6 | 3 | 2 | 3 | **2** | **1** | 2 |
| (13,6,2)     | 7 | 3 | 3 | 4 | **3** | **1** | 3 |

**Every cell fills the room: `mult = a` in all five, on both sides.**

Rank as a function of the number of evaluation points (determinant side, random
integer tuples in `[-6,6]`):

    (12,6)    1, 2, 2, 2, 2, 2, 2, 2, 2, 2
    (15,6)    1, 2, 2, 2, 2, 2, 2, 2, 2, 2
    (9,4,2)   1, 2, 2, 2, 2, 2, 2, 2, 2, 2
    (12,4,2)  1, 2, 2, 2, 2, 2, 2, 2, 2, 2
    (13,6,2)  1, 2, 3, 3, 3, 3, 3, 3, 3, 3

The rank reaches `a` at exactly `a` points and never rises afterwards — the
pre-registered Q3 prediction, confirmed. Because the rank *attains* `a`, and
`mult <= a` always, each row is a **certificate**, not an estimate: it exhibits
`a` explicit integer points at which the `a` highest-weight vectors are
linearly independent. No probabilistic step enters any entry of the table.

Each number was produced twice, by two implementations that share only the
monomial enumeration: (A) an explicit integer basis of the highest-weight
kernel with the rank of `[h_k(point_j)]` taken over `Q` and modulo `2^61 − 1`;
(B) `rank([R;E]) − rank(R)` modulo two different primes. They agree on all
five cells, on both `det` and `per`.

**On the permanent column.** As the brief instructs: unpadded,
`dim closure(per_3) = 77 > 65 = dim closure(det_3)`, so `per_3` lies outside
`closure(det_3)` for dimension reasons and no obstruction is needed or
expected. `mult_per` here is a **calibration of the method, not a GCT
measurement.** The GCT-relevant comparison is padded at `n = 4` and is not this
session.

## 2. What the table means, and what it does not

The brief's framing was that the programme had never measured a closure
multiplicity that could be anything other than 0, 1, or forced. That is now
false — five cells with `a >= 2` have been measured — but the answer is the
uninteresting one at every cell, and there is a reason:

> **Theorem (`docs/isotypic_rank.md` §4).** `mult_lam = a(lam,delta)` for every
> `lam` with `ell(lam) <= 4`, at every degree, for `det_3`; and for every
> `ell(lam) <= 5` for `per_3`.

All five cells have `ell(lam) <= 3`. So none of them could have come out any
other way, and the honest reading is that **the brief's cell selection —
"start with the two-row weights, they are the cheapest" — selected exactly the
weights the theorem covers.** Cheapness and informativeness ran in opposite
directions here. The measurement was still worth doing: it is what turned the
suspicion into a theorem, and the theorem is worth more than the five numbers.

**Kill criterion 1 fires.** `mult_det = 2` at both two-row cells. The `a = 2`
stratum at `n = 3` is closed — and closed far more completely than the
criterion anticipated: not just the two cells but every weight of length `<= 4`
at every degree, whatever `a` is.

**Kill criterion 3 does not fire.** No cell has `mult_det = 0` with `m_det = 2`;
there is no genuine full deficit here.

**Kill criterion 2 does not fire.** Calibration at every weight with `a > 0` and
`delta <= 4` — 20 of them, all lengths — returns `mult = a`, which is what the
paper's published `1, 6, 31` row requires. The rank method agrees with the
paper wherever the paper already knows the answer.

## 3. The deficit at short weights, in closed form

Theorem 6 turns the deficit at every weight of length `<= 4` into a difference
of two classical quantities with no geometry between them:

    def_det(lam, delta)  =  m_det(lam) − a(lam, delta)
                         =  (symmetric rectangular Kronecker)  −  (plethysm coefficient)

both computable in milliseconds. In particular the deficit at such a weight is
**never** about the boundary — it is entirely about the plethysm's failure to
supply room. The first place the deficit can be about boundary geometry is
`ell(lam) = 5`.

The sharpest consequence, pre-registered as falsifier F5 and not fired:

    a(lam,delta) <= m_det(lam)   for every lam with ell(lam) <= 4.

Checked on all 172 weights of length `<= 4` with `a > 0` and `delta <= 7`; it
holds, and it is **tight at 59 of them**, including both two-row cells of this
session. A single counterexample would have refuted the theorem outright.

## 4. The degree-by-degree ledger, and a three-degree extension

`mult <= min(m_det, a)` always, so
`total_def(delta) >= sum_lam (m_det − min(m_det, a))`, with equality iff
`mult = min(m_det, a)` everywhere. Both sides, computed exactly:

| `delta` | `sum m_det` | `sum a` | `sum (m_det − a)` | published total deficit | measured directly |
|---|---|---|---|---|---|
| 2 | 3    | 2   | 1    | 1    | all |
| 3 | 11   | 5   | 6    | 6    | all |
| 4 | 43   | 12  | 31   | 31   | all |
| 5 | 170  | 29  | 141  | 141  | all |
| 6 | 697  | 79  | 618  | 618  | 62 of 79 measured, 1 by Theorem 6, 16 assumed |
| 7 | 2713 | 225 | 2488 | 2488 | 104 of 225 measured, 25 by Theorem 6, 96 assumed |

`a <= m_det` at **every** weight in this range, not merely the short ones, so
the third and fourth columns coincide; and the published sequence matches at all
six degrees. Since `mult <= a` pointwise, equality of the totals forces:

> **The ideal of `closure(GL_9 . det_3)` is zero in every degree `<= 7`.**

The paper currently records this for degrees `<= 4`. This extends it by three
degrees. Two independent supports, and it is worth separating them:

- *Conditional on the published total-deficit sequence*, the argument above is
  a proof — `Σ(m − mult) = Σ m − Σ a` with `mult <= a` pointwise forces
  `mult = a` pointwise.
- *Independently of it*, direct measurement returns `mult = a` at every weight
  actually reached: all of `delta <= 5`, 62 of the 79 units of ambient room at
  `delta = 6`, and 104 of 225 at `delta = 7`, with a further 1 and 25 units
  proved by Theorem 6. Nothing measured or proved disagrees.

The residue is honest and small: at `delta = 6, 7` the weights whose weight
space exceeded the computational cap (700 and 600 monomials respectively) and
whose length is `>= 5` were not measured — 16 units of room at `delta = 6` and
96 at `delta = 7`. Those are the entries carried by the published sequence
rather than re-derived. They are pure compute, not new mathematics.

## 5. Where to look next, and why the cheap cells were the wrong ones

The theorem says the first weight at which the determinant's ideal can contain
anything has **length 5**, because `D_5^det` — the variety of quinary cubics
admitting a `3x3` linear determinantal representation — has dimension
`45 − 16 = 29` inside a 35-dimensional space, codimension 6. Equivalently, by
Proposition 5 of `docs/isotypic_rank.md`, the length-5 stratum of
`C[closure(det_3)]` **is** the coordinate ring of `D_5^det`, and the deficit
there is the first one that is genuinely about the geometry of determinantal
representations rather than about the plethysm.

So the next search should be:

1. **Length exactly 5, smallest `delta` with `a >= 2` there.** Not "cheapest
   weight space" — that heuristic is what produced this session's five
   guaranteed answers.
2. `delta >= 8`, since `delta <= 7` is now closed.
3. The permanent's crossover is at length 6, one later, so a *comparison* at
   length 5 has the determinant's ideal live and the permanent's still empty —
   the first weights where the two rings can differ for a structural reason
   rather than an arithmetic one. That asymmetry is a direct consequence of
   `dim Stab(det_3) = 16` against `dim Stab(per_3) = 4`, and it is the single
   most usable thing this session found.
