# Pre-registration — session 47 (the exactness conjecture)

Branch `s47-exactness`, clone tip `9aa6a9c`.  Written and committed **before any
measurement of this session**.  Clone check passes: all eight required files
present.  **Flag:** the brief's required reading lists `docs/s43_review.md`; that
file is not in this clone.  Its §2 content — the complete `δ = 8` six-row family
with `h_pad`, and the "fires ⟺ two units" reading — is present in
`results/sixrow_record.md` (pad-side table, "Two readings") and
`docs/sixrow_close.md` §3, and those were read instead.  Nothing else is missing;
this is not a stale clone.

## 0. A correction to the evidence base, before any prior is stated

The brief says the bound "fires at 8 [of session 42's 201 banked cells] and is
exact at all 8", and that `h_pad < a` holds at **411** census cells.  Both
numbers are right, but they are not all evidence, because **at `h_pad = 0`
exactness is a theorem, not a conjecture**: Corollary B2 gives
`mult_red ≤ h_pad = 0`, and `mult_red ≥ 0`, so `mult_red = h_pad = 0` with no
computation and no content.  Splitting the record on that:

| | firing cells | `h_pad = 0` (exact by Cor. B2) | `0 < h_pad < a` (the conjecture) |
|---|---|---|---|
| s42 census `δ = 7, 8` | 411 | 140 | **271** |
| s42 census `δ = 9` (sized) | 62 | 22 | **40** |
| s42's 201 banked cells | 8 | 4 | **4** |

So the conjecture's actual evidence is **seven cells**, not twelve:

- `(10,8,7,1,1,1)_7` `a = 3, h_pad = 2, mult_red = 2`
- `(13,10,5,1,1,1,1)_8` `a = 2, h_pad = 1, mult_red = 1`
- `(14,8,6,1,1,1,1)_8` `a = 2, h_pad = 1, mult_red = 1`
- `(11,9,9,1,1,1)_8` `a = 3, h_pad = 1, mult_red = 1`
- `(11,10,8,1,1,1)_8` `a = 4, h_pad = 2, mult_red = 2`
- `(12,9,8,1,1,1)_8` `a = 6, h_pad = 4, mult_red = 4`
- `(12,10,7,1,1,1)_8` `a = 9, h_pad = 7, mult_red = 7`

Five of the seven are `ℓ = 6`, `δ = 8`, `(λ_1,λ_2,λ_3,1,1,1)`; four of those five
are the two-unit cells the brief's headline finding is about.  The `δ = 8`
"4 of 4, complete family" result stands exactly as stated — it is a closed-set
statement and the strongest single piece of evidence — but the conjecture has
been tested at **two** cells outside `ℓ = 6` (both `ℓ = 7`, both `a = 2`,
`h_pad = 1`, the minimal possible test) and at **one** cell outside `δ = 8`.
The 140 + 22 = 162 `h_pad = 0` cells, and the `(4,4,4,4,4,4)_6` entry of
`results/sixrow_record.md`, are theorems of Corollary B2 and are not counted
here or below.  This session's job is to raise seven.

## 1. The conjecture, restated as a rank statement

This is the framing I will test against and try to prove, derived from
Theorem B1 and Corollary B2 with no new computation.

`C[R_r]_δ = im(μ*_δ)` where `μ*_δ : Sym^δ Sym^4 V → Sym^δ V ⊗ Sym^δ Sym^3 V`
is the generalised Foulkes–Howe map (Kadish–Landsberg Thm 1.7; `docs/reducible_engine.md`
§B, §C).  It is `GL(V)`-equivariant, so in each isotypic component it is a map
of multiplicity spaces

        μ_λ :  C^{a(λ,δ)}  ⟶  C^{h_pad(λ,δ)},        mult_red(λ, δ) = rank μ_λ.

Hence `mult_red ≤ min(a, h_pad)` is Corollary B2 plus the trivial bound, and:

> **The conjecture is: `μ_λ` is surjective whenever `h_pad < a`.**

Equivalently, `mult_red = min(a, h_pad)` on the firing set — `μ_λ` has *maximal
rank* there.  This reformulation is what makes me cautious, because the
maximal-rank statement is **already known to be false off the firing set**.  At
every one of these measured cells `h_pad ≥ a` and yet `rank μ_λ < a`:

| cell | `a` | `h_pad` | `mult_red` | rank deficit below `min(a,h_pad)` |
|---|---|---|---|---|
| `(12,4,4,4,4)_7` | 4 | 4 | 3 | 1 |
| `(13,12,4,1,1,1)_8` | 3 | 3 | 2 | 1 |
| `(13,8,8,1,1,1)_8` | 3 | 3 | 2 | 1 |
| `(13,9,7,1,1,1)_8` | 11 | 11 | 10 | 1 |
| `(14,8,7,1,1,1)_8` | 9 | 11 | 8 | 1 |
| `(13,10,6,1,1,1)_8` | 9 | 9 | 8 | 1 |
| `(16,13,4,1,1,1)_9` | 7 | 9 | 6 | 1 |
| `(17,12,4,1,1,1)_9` | 8 | 12 | 7 | 1 |

So `μ_λ` drops rank by exactly one below `min(a, h_pad)` at eight known cells,
all of them with the bound silent.  The conjecture asserts that this
rank-dropping mechanism — which is real, and which the normalisation by
construction cannot see — switches off precisely on the components where the
target happens to be smaller than the source.  I know of no reason it should.

The base rate matters.  Among the ~190 cells of the record where `h_pad ≥ a` and
`mult_red` is known, the drop happens at 8 — about 4%; inside the `ℓ = 6`
`(λ_1,λ_2,λ_3,1,1,1)` family at `δ = 8` it happens at 5 of the 29 non-firing
cells, about 17%.  If either rate carried over to the firing set, a sweep of
25–35 firing cells would be expected to produce roughly one to five refutations.
The conjecture is the claim that the rate there is zero.

## 2. Predictions

**P1 — prior that the conjecture survives Phase A: 0.40.**

Reasoning, both directions, stated so it can be scored:

*Against (why not higher).*  (i) The rank-deficiency mechanism above exists, is
invisible to `h_pad` by construction, and has no known reason to avoid the
firing set; at a 4% base rate a 30-cell sweep refutes with probability ~0.7.
(ii) The evidence is seven cells, five of them in one family at one degree, and
two of them (`a = 2, h_pad = 1`) are the smallest test the statement admits.
(iii) The bound is lossy in general — `h_pad > mult_red` at 84 of 91 banked
cells — so the normalisation quotient `D/C[R_r]` does carry `λ`-isotypic weight
at most weights; the conjecture is a strong closure statement about when it
stops.  (iv) The most exposed cells are cheap and untested: `ℓ = 6`, `δ = 9`,
in-family, large `a`, gap `a − h_pad = 1`, e.g. `(16,10,7,1,1,1)_9`
(`a = 30, h_pad = 29`) and `(15,12,6,1,1,1)_9` (`a = 21, h_pad = 19`), where
exactness demands a `30 × 29` (resp. `21 × 19`) multiplicity-space matrix be of
full rank on the nose.

*For (why not lower).*  (i) The `δ = 8` family result is a **closed-set**
statement: on all 33 in-family cells with `a ≥ 1`, the bound fires at exactly
the four two-unit cells and is exact at each, and is silent at all 29 others —
a coincidence of that shape on an exhausted set is not cheap.  (ii) A heuristic
mechanism exists: `h_pad < a` says `D_δ` is *atypically deficient* in the `λ`
component, and the quotient `D/C[R_r]` is supported on the codimension-`≥ 1`
non-normal locus `{ℓℓ'q} ∪ {ℓ²q}`; deficiency of the ambient and support of the
quotient plausibly pull in opposite directions.  (iii) No counterexample exists
in a record of ~190 measured cells.

I will call 0.40 my prior and record it as genuinely uncertain rather than
sceptical: I expect this session to settle the question one way or the other,
and I would not be surprised by either outcome.

Refined sub-predictions, scoreable separately:

- **P1a (0.75):** if a counterexample exists, it has `a − h_pad = 1` and
  `mult_red = h_pad − 1`, i.e. the same drop-by-one mechanism as the eight
  cells above, not a large deficit.
- **P1b (0.65):** if a counterexample exists, it is at `ℓ = 6` rather than
  `ℓ = 7, 8` — the family where every known rank drop lives.
- **P1c (0.80):** the conjecture survives at every `ℓ = 7` and `ℓ = 8` cell I
  measure.  (The two `ℓ = 7` cells already tested are the only evidence off
  `ℓ = 6`, and the rank drops of the record are an `ℓ = 6` phenomenon.)
- **P1d (0.55):** the `δ = 8` in-family statement "fires ⟺ two units" does
  **not** extend to `δ = 9` in-family cells — I expect to find a `δ = 9`
  in-family cell where the bound fires and the deficit `a − mult_red ≠ 2`.

**P2 — how many cells, to what `n_red`.**  I expect to measure **30 ± 10**
previously unmeasured cells with `0 < h_pad < a`, at `n_red` up to about
`2·10^4` and `N_S` up to about `2·10^6`, using the sparse route throughout and
the exact route below `n_red = 2500`.  Composition target, so the test is not
confined to the family the pattern was found in: at least 8 cells at `ℓ = 7`,
at least 2 at `ℓ = 8`, at least 8 at `δ = 9`, at least 8 at `δ = 7` or outside
the `(λ_1,λ_2,λ_3,1,1,1)` family, and at least 6 with `a ≥ 10`.  Calibration
from the 201 banked cells: build ≈ `1.1·10⁻⁴ s` per monomial (`N_S`), solve
≈ `3.6·10⁻⁸ · n_red · nnz_red` seconds per prime.  Note that the census field
`nchi_lb` is `N_S / stab` and **over**estimates `n_chi` badly (20444 against a
measured 3881 at `(13,10,5,1,1,1,1)_8`), so `N_S` is the ordering key, not
`nchi_lb`; the work list will say so.

**P3 — the 10 remaining `δ = 8` permanent weights: all ten empty**, so
`I(D_6^{per_3})_8 = 0` and `mult_pad = mult_red` at every degree-8 weight, by
Prop. 8(1) of `docs/transfer_lemma.md`.  Probability **0.88**.  Reasoning: 81 of
the 91 are already measured empty; degree 7 is fully proved empty
(`docs/sixrow_close.md` §4); and across the entire six-row record — 188 cells,
585 ambient units — `mult_pad = mult_red` at every cell where both are known, so
no permanent-specific equation has ever been seen at any degree.  The 12%
against is not negligible: the 10 left are the 10 the session could not reach,
and "the ones left over" is exactly where a surprise would hide.

## 3. Stopping rules (from the brief, adopted verbatim in force)

1. **`mult_red > h_pad` at any cell ⇒ a bug, not a discovery.**  Corollary B2
   forbids it.  Stop the sweep, find it, report it.  I will assert
   `a − nullity_p ≤ h_pad` at every cell in my own wrapper; the s42 engine
   asserts only `nullity_p ≤ a` and does not know about `h_pad`.
2. **`mult_red < h_pad` at a firing cell ⇒ the conjecture is refuted.**  Stop
   the sweep; certify that cell hard (both primes, exhibited kernel verified
   against the uncompressed rows, exact integer lift via
   `analysis/wk9_s42_lift.py`); write it up as the counterexample.  This is a
   result, and a better one than survival.
3. **A non-empty `δ = 8` permanent weight ⇒ stop everything else and certify.**
   It would be the first permanent-specific equation the programme has seen.
4. Primes disagreeing on a nullity ⇒ re-run at a third prime; do not bank.

## 4. What would falsify what

- The **conjecture** is falsified by a single firing cell with
  `mult_red < h_pad`, certified at both primes.
- **P3** is falsified by one non-empty permanent weight.
- The **restatement in §1** ("`mult_red = rank μ_λ`") is not a prediction; it is
  a consequence of Theorem B1 and KL Thm 1.7 and is asserted as proved.  If a
  measured cell ever gives `mult_red > min(a, h_pad)`, the restatement is wrong
  and so is Corollary B2 — that is stopping rule 1.
- A **proof** in Phase B must not assume the sweep; if the sweep refutes the
  conjecture, any Phase B argument that "proved" it is wrong and the error is
  the deliverable.

## 5. Labels

Everything below is labelled **proved** / **measured** / **adopted-from-literature**
/ **expectation**, per the house convention.  Measured means both house primes
agree; proved on the reducible side means either `nullity_p = 0` at one prime
(Lemma A2), or `h_pad = 0` (Corollary B2), or an exhibited exact integer kernel
basis of the right size.
