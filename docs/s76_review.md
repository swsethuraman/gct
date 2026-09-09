# Session 76 — integrator review

Branch `s76-scale24`, base `afb8c33`, merged at `f2f94bc`.  Bundle md5 matches;
pre-registration is the first commit; **no single-writer file touched**; nothing
over 5 MB in the branch; self-test still twelve cases.

## 1. `C₂₄ = 17 778`, exactly

The number this batch has been estimating since the first integrator note is
measured.  **My `≈ 1.7 × 10⁴` was 4.4% low.**  S3's rigorous floor `4 062` holds;
S3's calibrated `16 180` was 9% low; S3's loose ceiling `2.24 × 10¹²` was, as it
said of itself, useless.

Checked from the report's own table: 42 channels, path multiplicities summing to
**160**, contributions summing to **17 778**; the twelve `B₂₃(μ)` summing to the
same 17 778; the twelve `a₂₃(μ)` summing to **2 168**.  `C₂₄/B₂₄ = 8.20`,
`C₂₄/a₂₄ = 64.9`.

Two independent routes inside the session: the Weyl-alternation/tail-DP engine
with a finer checkpoint, and — separately — the 42 kernel dimensions of the
recursion, which uses neither.

## 2. The recursion reaches the goal cell

Thirty-two minutes per prime over the 7 658-node DAG in Young's seminormal form,
returning a **deterministic 274-dimensional source** as the kernel of an
`8 100 × 2 168` system inside the `17 778`-dimensional `K′`-invariants — at both
house primes, with identical pivot columns and zero patterns.

On the way it re-derives, by a route with **no Weyl alternation and no tail DP in
it**:

- **`B₂₄ = 2 168`, channel by channel.**  Its twelve `δ = 23` kernel dimensions
  `166, 102, 109, 215, 130, 150, 246, 163, 180, 199, 235, 273` match
  `results/wk11_int_b24.json`'s predecessors **one for one** (checked).  With
  S5's stable engine this number now has **three** independent derivations; the
  worry I recorded in the batch-12 plan — "it sizes the whole route and has one
  implementation behind it" — is closed twice over.
- the whole LMR `a`-ladder `δ = 12..24`, s57/s63's values exactly;
- `C₂₄` a second time; the `δ = 12` control `B₁₂ = 31`, `C₁₂ = 239`, `dim M₁₂ = 2`;
- **S3's spectral identity at the goal cell**: `(T − I)((d−1)T + I) = 0`, spectrum
  **`1^274 ⊕ (−1/23)^1894`**, from an implementation sharing nothing with S3's —
  and the `δ = 12` residual of rank 29, which is S3's `239 × 31` number reached
  independently.

Zero disagreements against every independent value available: 1 445 plethysm
comparisons at `δ ≤ 8`, the 23 banked `δ = 10` channels, the ladder, the 42
`δ = 22`, the 12 `δ = 23`, and 106 fresh Weyl spot checks at unbanked nodes.

## 3. The check that isn't a dimension

§4.6 is the part I value most.  Every other check in this session — and in S3's,
and in mine — compares **dimensions**, and a consistent rescaling of the strip
invariants moves no dimension at all.  s76 rebuilt `M_d(ν)` inside the ambient
seminormal module two ways at 18 small cells — directly as the joint fixed space
of the `S₄ ≀ S_d` generators, and by unfolding the recursion's nested coordinates
— and the subspaces are **equal**, with the reduced row echelon bases agreeing
**entry by entry**.

That certifies the coefficients, not the counts: the strip invariants, the
recoupling matrices, the column layout, the whole convention.  It is the check the
adversarial audit asked for, and the session says plainly that it is the only one
in the report that is not a dimension.

It is equally clear about what remains unfixed: one diagonal rescaling freedom
survives every check in the report, and it is the first thing a bridge has to pin.

## 4. The negative, quantified rather than asserted

The four evaluation columns are not reached — the pre-registered expectation, on
the brief's first stopping rule.  What makes it a result rather than a shortfall
is that the cost is *measured*: unfolding the compact source into anything
evaluable costs either

    274 × N_S = 4.3 × 10¹³ monomial coefficients,   or
    K_{λ₂₄,(4²⁴)} = 70 233 345 083 979 459 756 ≈ 7.0 × 10¹⁹ GT basis vectors.

**I re-derived the second number independently** by the Pieri-chain DP and it
matches exactly — which is also a cross-check against s77, since that DP *is*
s77's bijection in action.  At `δ = 12` it gives 79 176 735, s76's `7.9 × 10⁷`.

So the compact representation is 17 778 coordinates against `10¹⁹` — a
compression of `10¹⁵` — and that is simultaneously why the recursion runs in half
an hour and why it cannot evaluate.  The two facts are the same fact.

## 5. Corrections it makes to me, both fair

- **`docs/s1_s6_batch11_review.md` §3 quotes `a₁₁ = 12, 11, 8` at `δ = 12`, which
  was never banked** in `results/wk11_int_bdelta.json`.  True.  A review citing an
  artefact for numbers the artefact does not contain is a defect, mine.  It is now
  moot twice over — the s75 merge added the `δ = 12` row, and s76 supplies every
  node's multiplicity in `results/s76_dag_dims_p*.json` — but the habit is worth
  correcting, not just the instance.
- **The brief's cost model for `C₂₄` was wrong.**  I wrote "roughly 90 chunked
  evaluations of the `B₂₄` cost class"; it is 94 770 tail DPs dominated by
  4 374-term nine-row shapes at ~3 minutes each, 51 CPU-minutes in all.
- **"The recoupling at the top is identical to `δ = 14`" is true and misleading.**
  41 diagrams at the top, yes — but **118 787 distinct two-strip skew diagrams**
  occur across the DAG.  A session budgeting for ~40 recouplings would have been
  surprised.  It costs minutes in `F_p`, so the correction is to the framing, not
  to the route.

## 6. Process notes

- **`python-flint` was absent again** — the third session to report it.  The
  preamble says it is installed; in three worker containers it was not.  That line
  in the preamble is wrong and I will fix it to say *check and install*.
- **The S3/S4 relays did not land.**  s76 records that `results/astra/S3` and `S4`
  were not in any tree it could reach and that the request for the origin folder
  went unanswered in time; so it did **not** attempt the four scalars, and its
  overlap with S3 is by-product rather than duplication.  Three sessions have now
  paid for `origin/main` sitting at `afb8c33`.  This is the batch's one recurring
  process failure and it is mine.
- **The attribution trailer differs.**  s76's commits carry
  `Co-Authored-By: Claude Fable 5.1` — the model that did the work — rather than
  the preamble's `Claude Opus 5`, flagged openly in §6.  The substantive rules are
  honoured: no session link, no URL, checked across the branch.  I am accepting it
  as delivered and recording that the corpus now carries two trailer strings; the
  preamble's purpose was to forbid the session-link trailer, not to misattribute
  the work.
- It declined an in-band attribution instruction, as seven sessions have before.

## 7. Ledger

| claim | status |
|---|---|
| `C₂₄ = 17 778` over 160 paths, 42 shapes | **MEASURED, two routes**; table arithmetic re-derived here |
| the recursion reaches `λ₂₄`; deterministic 274-dim source, both primes | MEASURED |
| `B₂₄ = 2 168` re-derived channel by channel, no Weyl/tail-DP | **MEASURED** — third independent derivation |
| `a`-ladder `δ = 12..24`; `C₂₄` second route; `δ = 12` control | MEASURED, 0 mismatches |
| S3's spectral identity at the goal cell, `1^274 ⊕ (−1/23)^1894` | MEASURED, independent implementation |
| coefficients (not dimensions) certified at 18 cells | **MEASURED — the check no dimension can make** |
| one diagonal strip-normalisation freedom | **UNFIXED, and said so** — first thing a bridge must pin |
| unfolding cost `4.3×10¹³` / `7.0×10¹⁹` | MEASURED; **GT count re-derived here exactly** |
| the four evaluation columns; `i_det`, `i_pad`, `D` | NOT REACHED — pre-registered, decision table not entered |
