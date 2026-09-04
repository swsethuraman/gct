# Integrator review — session 45 (the determinant side at O(nnz) memory)

2026-09-03.  Branch `s45-sparsedet`, head `b8e3ed1` (13 commits on `0c229c1`;
pre-registration `bbd7d06` before any measurement).  Pure additions, nothing
over 5 MB added, no session link in any of its own commits.  The verdict —
frontier `n_χ = 19,985 → 114,875`, nine cells, `mult_det = a` proved at every
one — is accepted.  Declining to push against the brief was right, twice over.

## 1. Verification

- **Every `a` rebuilt.**  All 14 V3 rows and all 9 sweep cells reproduce with
  my own Kostant alternation.  No mismatch.
- **The verdict is robust to `a` anyway**, and this is worth stating in the
  write-up because it strengthens the result: `nullity_p([E; ev]) = 0` says
  `HWV_λ ∩ ann(points) = 0`, hence `mult_det = dim HWV_λ`.  That conclusion
  does not depend on the *numerical value* of `a` at all — a wrong plethysm
  would misreport the number but could never turn a real drop into a
  full-rank verdict.  The certificate's one-sidedness protects the load-bearing
  direction twice.
- **The validation battery is the right shape.**  V2 is the test that matters
  and it is six cells where the answer is *not* full rank, each returned with an
  exhibited rational vector verified over ℤ and against (★) — I audited four of
  those vectors myself when they came through s42 and s41, and the values here
  match.  V3's 14 rows are the same cells s41 measured densely, at
  `(12,9,3,2,1,1)_7` in 62 s against s41's 2500 s and 4.68 GB.  V5's build
  comparison checks order, orbits, signs, row counts, `nnz` and row space
  against two prior implementations at 16 cells.
- **The compression episode is the strongest evidence in the session.**  At
  `(8,8,6,2,2,2)_7` the cheap level came out exactly 57 short of full column
  rank at *both* primes with independent randomness — precisely the shape a
  false onset would take — and the check against the full `[E; ev]` rejected it.
  The safety property held under the one condition that could have broken it.

## 2. What is new, and what it is worth

The memory wall is genuinely gone, not merely pushed: `8n_χ²` bytes became
`O(nnz + n)`, so 106 GB became 1 GB, and the binding constraint moved to `N_S`
(build time), which the session itself says is soft.  Balance 4 at δ=7 is the
first measurement anywhere near the rectangular corner; before this session
nothing below balance 8 had ever been measured at six rows.  The two cost laws
(`nnz ≈ 3.5 N_S`; a cell costs `≈ 10.6·10⁻⁹ · n_χ · nnz_c` seconds) are the most
useful planning artefacts the programme has produced, and the reach table built
from them is correctly labelled an expectation.

## 3. Three free readings the session left on the table

`h_pad` (s42's normalisation bound) costs milliseconds and was not applied to
these nine cells.  Doing it now:

| cell | `a` | `h_pad` | consequence |
|---|---|---|---|
| `(7,7,6,6,1,1)_7` | 1 | **0** | `mult_red = 0`, so `mult_pad = 0` and **`D = −1` exactly, proved** |
| `(6,6,6,6,2,2)_7` | 1 | **0** | same — **`D = −1` exactly, proved** |
| `(8,8,5,5,1,1)_7` | 3 | 2 | predicted pad bite, `D ≤ −1` |
| `(9,9,9,3,1,1)_8` | 3 | 2 | predicted pad bite, `D ≤ −1` |

So three of the nine rows upgrade from "`D ≤ 0` because the det side is full"
to an exact or bounded `D`, with no computation — including the balanced-corner
cell itself.  The two `h_pad = 0` cells are also two more negative instances of
Kadish–Landsberg Question 1.5, at balances 6 and 4 where nobody has been.  And
`(8,8,5,5,1,1)_7` and `(9,9,9,3,1,1)_8` are two more tests of the exactness
conjecture (`h_pad < a ⟹ mult_red = h_pad`) at balances the conjecture has
never been probed at — each is one sparse nullity through s42's engine, minutes
of work, and would take the count to 13.

## 4. A bookkeeping item for the merge

s43 and s45 both branched from `0c229c1` and ran concurrently, so **neither
knows about the other's cells**.  s45's "99 cells / 223 ambient units" and
s43's coverage table are each correct in isolation and both are stale the
moment they are merged.  The cell sets are disjoint (s43 worked at
`n_χ ≤ 20,000`, s45 at `n_χ ≥ 23,700`), so the merged record is an addition and
not a reconciliation — but the number must be recomputed rather than either doc
copied, and `results/s41_coverage.md`, s43's coverage doc and
`docs/sparse_det_route.md` §7 will each claim to be current.  I will rebuild
the six-row record once from the three ledgers at the merge and correct all
three in one pass.

## 5. Wording and small items

- "the obstruction question is untouched" and the §7 phrase "the bracket `≥ 9`
  in every component reached" carry the same overreach I flagged in the s41
  review: what is established is *no six-row determinant equation at any
  measured cell of degree ≤ 8*, not a property of the degrees.  The balance
  extension makes the evidence much better and the wording no more earned.
- The reach table's "48 h" columns assume the fitted `nnz_c/n_χ = 60` and
  2.3 ns/op hold at cells nobody has built; the doc says so, and the successor
  brief should repeat it rather than quote the counts flat.
- `(8,4,4,4,4,4)_7` as the named next target is right, and the diagnosis — 240
  group passes over a 10 M-monomial array, embarrassingly parallel, blocked only
  by two cores — is a concrete ask rather than a wish.

## 6. Process

Pre-registration before any measurement with a stated confidence that was then
scored; the validation battery deliberately weighted toward non-full-rank
answers; per-cell banking with commits; the compression finding reported as a
cost as well as a result; the honest boundary section states both what a
`mult_det = a` row does not say and which two conventions are inherited without
re-derivation.  The refusal to push on a hook's say-so, with the reasoning
given and the override left to the user, is exactly the behaviour the standing
rules are for.
