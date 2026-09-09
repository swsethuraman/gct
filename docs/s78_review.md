# Session 78 — integrator review

Branch `s78-elimination`, base `afb8c33`, merged at `5a7bc55`.  Bundle md5
matches; pre-registration is the first commit; **no single-writer file touched**
(checked against the branch, not against my own working tree); nothing over 5 MB;
verifier self-test still passes at twelve cases.

## 1. What it delivered

Job A did not finish — the pre-registered F3 outcome — and the session is worth
having anyway, because of what it did instead.

1. **All three mandatory controls pass**, including the rank-3 arc reproduced
   from S2's base pencil by code that is not S2's.
2. **A certified reduction of Job A from 149 variables to 98, with the
   `f₀`-saturation removed entirely.**  On the chart `y₀ ≠ 0` the source point has
   `det A₅ ≠ 0`, the ratios are invariant under `A_k ↦ P A_k Q`, so `A₅` may be
   normalized to `I`; then `f₀ ≡ 1` and the saturation disappears.
3. **A clean equivalence**: `W ⊆ D₅ ⇔ the char-coefficient map `G : S → 𝔸³⁴` is
   dominant`, so `W ⊄ D₅ ⇔ generic rank ≤ 33`.  This is the sufficient bound
   `dim(D₅ ∩ W) ≤ 34` restated as a rank condition on a 64-variable map.
4. **The ker/coker component image is exactly 28 projective, at every contact
   order.**  This sharpens S2's Theorem 5.1, which bounded only order-two
   fixed-factor leading forms by 29.
5. S2's §5 bound reproduced exactly and independently (`45 − 16 = 29`).
6. No reversal at any tested family — 28, 28, 19, none reaching 34 — giving a
   certified `dim(D₅ ∩ W) ≥ 28`.

## 2. Verified here, on my own points and my own code

`analysis/wk12_int_s78_verify.py`, run at three independent seeds:

- **The grading.**  `det(s₅I₄ + Σ s_k B_k)` has `s₅^{4−j}` coefficient homogeneous
  of degree `j` in `s₁..s₄` — degrees `{4:[0], 3:[1], 2:[2], 1:[3], 0:[4]}` at
  every seed.  The counts `1, 4, 10, 20, 35` are then the combinatorial fact
  `binom(d+3,3)`, giving **34 good + 35 bad = 69**, which is S2's ratio-coordinate
  count exactly, with the bad set being `P₄ ≡ 0` — the 4-pencil spans a space of
  singular matrices.
- **The ker factorization, and why it is exact.**  `det(4×4) − s₅·det(3×3) = 0`
  identically, **and replacing every off-diagonal `r_k` leaves the determinant
  unchanged.**  That second check is the real content of "all contact orders":
  the component's image does not depend on the `r_k` at all, so there is no arc
  or order truncation anywhere in the argument.
- **The dimension, both bounds.**  The `34 × 36` Jacobian has **rank 28 over `Q`**
  — s78 certified it mod both primes; over `Q` is the stronger direction — and the
  commutator map `gl₃ → 𝔸³⁶` has rank 8, so the generic orbit is 8-dimensional
  and the image is `≤ 36 − 8 = 28`.  Both meet.  **28 exactly, confirmed.**

One methodological note, and it is a caution for everyone rather than a finding
against s78.  My first check compared the *observed* coefficient counts at a
random point against `1, 4, 10, 20, 35` and failed at one seed — because
`tr(B_k)` happened to vanish there, so the `s₅³` coefficient showed 3 of its 4
monomials.  An observed count at a sample point is a **lower bound** on the
coefficient-space dimension, never an equality.  That is the same
sampled-versus-generic error the programme refuses elsewhere, and I made it in a
checker; the check now tests the grading empirically and takes the counts as
combinatorics.

## 3. The finding I would elevate above the rest

s78 identifies what the wall actually **is**:

> the completeness half — that the named families exhaust `S` — is precisely the
> **classification of 4-dimensional spaces of singular `4×4` matrices**, i.e. of
> spaces of bounded rank `≤ 3` in `M₄`.

For three batches this has been described as an enumeration-completeness question
to be settled by our own computation.  It is a **named, classical problem with a
substantial literature** — Atkinson's primitive-space classification, Eisenbud–
Harris on vector spaces of matrices of low rank, and a recent Huang–Landsberg
paper on bounded rank.  That literature is adjacent to this programme in more
than subject: Landsberg is a co-author of the Kadish–Landsberg pullback result S4
already cites.

**What I found, and exactly how far it goes.**  The Huang–Landsberg paper states
that at bounded rank `r ≤ 3` *there are no non-classical examples*, attributing it
to Atkinson (1983) — and bounded rank `≤ 3` in `M₄` is precisely our `S`.  If that
holds at our parameters, the completeness half is available by **retrieval and
matching** rather than by elimination.

**I have not verified this and it may not apply.**  One stated hypothesis in the
secondary literature is `n > 1 + r(r−1)/2`, which at `r = 3` reads `n > 4` — and
our `n` is exactly 4, so we sit on the boundary where that hypothesis fails.  I
have a fast summary of two PDFs, not a checked theorem statement.  So the honest
status is: **a strong lead with a borderline hypothesis**, which is precisely why
it deserves a session rather than a footnote.

The redirect is worth stating plainly.  Three sessions have now walled on the same
computation.  If the completeness half is a citation-and-matching task, the
remaining work is: get Atkinson's statement and its hypotheses; decide whether
`n = 4, r = 3` is covered or is the excluded boundary case; if covered, match the
classical list against our named families (ker, coker, C21, C32, P, SP, skew);
then bound the image on each — and s78 has already done ker/coker exactly, at 28.
That is a different shape of work from a 149-variable Gröbner basis and it is much
cheaper.

## 4. What is still open, unchanged

`R₅ ⊄ D₅`.  The wall is a certified generic rank `≤ 33` for `G`, equivalently an
exact image equation.  A timeout is not a reversal certificate and s78 claims
none.  The exact residual is preserved.

## 5. Ledger

| claim | status |
|---|---|
| controls: Singular/msolve, S2's verifier, the rank-3 arc | PROVED (reproduced by s78) |
| 149 → 98 reduction, `f₀`-saturation removed | PROVED; grading and 34/35/69 split **re-derived here** |
| `W ⊆ D₅ ⇔ G dominant`, `W ⊄ D₅ ⇔ generic rank ≤ 33` | PROVED, modulo the inherited irreducibility of `W` |
| ker/coker component image = 28 projective, all contact orders | PROVED; **both bounds re-derived here**, Jacobian rank over `Q` |
| S2 §5 image bound ≤ 29 | PROVED (reproduced independently, twice now) |
| C21/C32 naive images 17–19 | MEASURED; a *different object* from s72's recorded 31, and neither promoted |
| no reversal at any tested family; `dim(D₅ ∩ W) ≥ 28` | MEASURED / certified lower bound |
| Job A, and the reduced `dim S` Gröbner | do not finish in-container; residual preserved |
| completeness = classification of bounded-rank-3 spaces in `M₄` | **the session's best observation**; literature lead identified here, hypothesis unverified |
| `R₅ ⊄ D₅` | OPEN |
