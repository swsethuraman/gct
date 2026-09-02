# Integrator review — session 36 (the stabiliser reduction, and the first six-row cells)

2026-09-02.  Branch `s36-stabred`, final head `326dd8b` (104 commits on
`5367c75`).  Everything checkable was re-verified independently; one
certificate was audited from scratch.

## 1. Verification — all pass

- **Provenance.**  Ancestry off `5367c75` passes; the disclosed history
  rewrite (to drop two 200 MB mod-p dumps) is confirmed benign: the insurance
  head `f82ea64` is still an ancestor, the largest surviving blob is a 12 MB
  certificate, and only session files plus two new docs are touched.  Rewriting
  delivered history is otherwise forbidden; this instance is accepted because
  it was disclosed, the ancestors are intact, and the cause was a mistake we
  now legislate against (no dump over 5 MB may be committed).
- **The ledger.**  91 rows across strata A, A7, B.  `mult_det = a` at every
  cell (a up to 21); exactly five `D = −1` cells, no `D > 0`; `|λ| = 4δ`
  everywhere.  My Kostant-alternation DP reproduces `a` **and** `N_S` on all
  91 rows, including the six-variable cells.
- **One certificate audited end to end.**  `(8,4,4,4,4)` at δ = 6, 19,834
  integer terms in the plain coefficients.  Every monomial has the right
  weight and degree; the (★) condition holds on every monomial; all four
  simple raising operators kill the vector over ℤ; it evaluates to 0 at a
  true padded-permanent point and at `l·(random cubic)`, and to nonzero at a
  `det_4` pencil and a generic quartic, at both primes.  So `pad_units ≥ 1`
  and `v ∉ I(det)` by a route sharing no code with the session; with their
  rank certificate `mult_det = 2 = a`, the cell is `D = −1` exactly.
- **The lemma's validation.**  18 rows, 7 cells, every candidate character of
  the weight-stabiliser: the unreduced kernel lands entirely in `χ_λ` and is
  empty elsewhere.  Even-valued blocks → trivial character, odd-valued → sign,
  and the two-block cells `(12,5,5,1,1)`, `(7,7,4,1,1)` discriminate all four
  combinations.  That is precisely the test the formula `∏ sgn(w_B)^{m_B}`
  would fail if wrong, and it passed in every direction.  The six s30 ledger
  reproductions, the compressed-vs-exact span checks, the witness and the
  41/48 battery all pass.

## 2. What is new and durable

**The reduction is real and in the tree.**  Frontier `n_χ ≈ 15,500` (flint's
nullspace holds three `8n²` copies); cells of `N_S` up to 1.5 million measured
in a laptop-class container.  The one-operator shortcut of s33 correctly noted
as *not* generalising; the isotypic restriction does.  Session 38's "does not
port" sentence is now superseded by a validated implementation.

**The (★) criterion is a theorem and a tool.**  A highest-weight vector
vanishes on the reducible locus `{l·c}` iff every one of its monomials misses
some variable — I re-derived it (Bruhat decomposition reduces vanishing on
`G·(x_1 c)` to vanishing on `x_i·(all cubics)` for each `i`; the latter is a
coordinate subspace).  It makes every pad-side bite a *theorem* by
inspection, gives a point-free `mult_red` that agreed with the point-based
`mult_pad` at all 91 cells, and yields Kadish–Landsberg's padding bound in one
line: if `λ_1 < δ` the condition is automatic, so the reducible locus has no
functions of that weight and no obstruction can live there.

**The pad onset is settled, and the gate was blind.**  `I(D_5^pad)` begins
at δ = 5 with the unique degree-5 invariant `I_5` (an `a = 1` cell the
`a ≥ 2` gate excluded); `(8,4,4,4,4)` and `(12,4,4,4,4)` are `c·I_5` and
`c²·I_5` exactly, identified by the session rather than counted as new;
`(9,9,8,1,1)` and `(8,8,8,2,2)` are genuinely new degree-7 generators.  At
`r = 6` the degree-6 invariant `I_6` plays the same role.  This closes s37's
"5 or 6" question at 5 and vindicates its `a ≥ 1` point within a day.
**Gate blindness** joins the house failure ledger.

**At the first cells that can carry the permanent, it does not.**  All 34
reachable six-row cells at δ = 6, 7: det ideal empty, and `mult_pad = mult_red`
everywhere — no permanent-specific equation through degree 7.  Session 37's
Prop. 8 gives `pad = red` at δ = 6 for free; at δ = 7 this is new information.

## 3. Refinements to carry

- My s36 brief called Stratum B "the first permanent-sensitive cells"; per
  s37, read "the first *possibly* permanent-sensitive cells, at δ ≥ 7."
- `P1.4` (`mult_det((10,10,10,6),9)`) is out of reach at ~300 GB even
  reduced; the cell stands on the Beauville-principality argument
  (`docs/s35_review.md` §2), which needs no measurement.
- The five `D < 0` cells are reducibility equations, in the expected
  direction, and are not obstructions — stated correctly throughout.
- The obstruction-eligible region is now sharply characterised: `a ≥ 1`
  (BIP silent at (3,4)), `ℓ ≥ 5` (≥ 6 to be permanent-flavoured),
  `λ_1 ≥ δ` (KL via (★)), and `δ ≥ 8` (det ideal empty below on every
  measured cell).

## 4. Standing after session 36

The tools are in-tree (`wk9_s36_stabred.py`, `wk9_s36_red.py`,
`wk9_s36_exact.py`); the reducible locus is understood; the permanent is
invisible through degree 7 at six rows; the det-side onset is ≥ 8 and, by the
Jacobian family, ≤ 300 with a conjectured exact formula.  Next: the
long-weight occurrence screen (s39 — the one region never examined, where the
`n = 3` ideal was actually first pinned) and the onset conjecture made
rigorous (s40).  Process: prereg first, every prediction scored, the two
P2 failures recorded as the findings they led to, one `pgrep` near-miss caught
by the read-back rule.  A model compute session.
