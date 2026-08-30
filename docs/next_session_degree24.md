# Session prompt — the degree-24 question

Paste the block below into a fresh session. It is written to stand alone:
assume the session has no memory of this conversation.

---

## The prompt

You are continuing a mathematics research programme called **gct** —
conductors and deficits of orbit closures. The repository is
`https://github.com/swsethuraman/gct` (public). Clone it and read
`PROJECT_NOTES.md` in full before doing anything else; the infrastructure
protocol (rules 1–12) and the results bank are both there, and both are
binding.

### The one task

Decide whether the orbit closure of the 3×3 determinant carries a nonzero
SL_9-invariant in **degree 24**.

Formally: let `G = GL_9` act on `W = Sym^3 C^9`, let `Ω̄ = closure(G · det_3)`,
and let `E(det_3) = { δ : C[Ω̄]^{SL_9}_δ ≠ 0 }` be the degree monoid. Degree 24
corresponds to the rectangular weight `λ = (8^9)` (since an SL_9-invariant of
degree δ has GL_9-weight `det^{δ/3}`). Determine whether
`C[Ω̄]^{SL_9}_24 = 0` or is one-dimensional.

### Why this is forced, and why it is worth doing

Three established facts, two from the literature and one ours:

1. **Bürgisser–Ikenmeyer** (arXiv:1511.02927), Theorem 3.4: for polystable `w`
   the degree monoid generates `b(w)·Z`, where the degree period is
   `b(w) = (m/D)·a(w)` and `a(w)` is the stabilizer period. Their Theorem 2.5
   gives `a(det_n) = 2` when `n ≡ 2, 3 (mod 4)`. For `det_3`: `m = 9`, `D = 3`,
   `a = 2`, so **`b(det_3) = 6`**. Hence `E(det_3) ⊆ 6Z` and
   **`gcd E(det_3) = 6` exactly**.
2. Ours: `min E(det_3) = e(det_3) = 18`, with `Φ_18(det_3) = −877,879,296,000`
   and `C[Ω̄]^{SL_9}_12 = 0`.
3. Therefore **`E(det_3) ≠ 18N`** — if it were, its gcd would be 18, not 6. The
   orbit closure must carry an invariant in some degree that is a multiple of 6
   but not of 18. The candidates in order are **24, 30, 42, 48**. (36 = 2·18 is
   automatic; 30 = 18+12 is not, since 12 ∉ E.)

**The bracket census does not help here.** An SL_9-invariant of degree δ on
`Sym^3 C^9` is spanned by products of `k = δ/3` nine-fold brackets in δ letters,
each letter in exactly 3 brackets; if two letters occupy the same three
brackets the monomial is its own negative and dies. That pigeonhole kills every
δ with `δ > C(δ/3, 3)`, which is exactly `δ ≤ 15` — it is what proves
`e(det_3) ≥ 18` without computation. At δ = 24 we have `k = 8` and
`C(8,3) = 56 ≥ 24`, so the census permits it. No hand argument is currently
known that settles degree 24 in either direction. That is why this is an engine
question.

So the answer at 24 is informative either way. Nonzero: you have found the
second generator of the invariant semigroup, and `E ⊇ ⟨18, 24⟩`. Zero: the
constraint tightens and 30 becomes the target. This is not an open-ended
search — the theory guarantees the sequence terminates.

Note that a degree-24 invariant, if it exists, is a **new generator**, not a
product: there is no SL_9-invariant of degree 6 on Ω̄ to multiply Φ_18 by.

### Strategy — try the cheap direction first

The two outcomes cost very different amounts, and this asymmetry should drive
the plan:

- **Proving 24 ∈ E is cheap in principle.** It suffices to exhibit *one*
  SL_9-invariant of degree 24 on the ambient `Sym^3 C^9` whose value at `det_3`
  is nonzero. A nonzero value at a point of the orbit means the restriction to
  Ω̄ is not the zero function. One evaluation, one number.
- **Proving 24 ∉ E is expensive.** It requires the full multiplicity
  computation of `λ = (8^9)` in `C[Ω̄]_24` — the same machinery as the δ = 18
  census, at a strictly larger level, so budget accordingly and checkpoint from
  the start.

Attempt the evaluation route first. Only fall back to the full census if no
ambient invariant you can construct evaluates nonzero — and note that failing
to find one is *not* a proof of vanishing, so say so plainly if that is where
you end up.

An equivalent formulation that may be easier to work with (Bürgisser–Ikenmeyer,
Lemma 3.2): on the *orbit* there is an invariant `φ` of degree `b = 6`, and
`E = { 6k : φ^k extends regularly to Ω̄ }`. So `Φ_18 ∝ φ^3`, and the question is
exactly **whether `φ^4` extends regularly across the boundary.** That may admit
a direct answer via the divisor `div(Φ_18) = 6P_1 + 9P_2` and the orders of
vanishing along the two boundary components, without any large computation.
Try this before the engine.

### Discipline — non-negotiable

- **Pre-register.** Commit your prediction, with reasoning, to git *before* the
  value exists. This is the programme's core practice and the repository README
  argues the commit history is part of the evidence. Two pre-registered
  hypotheses have already been refuted and are kept in the record; a refutation
  logged honestly is a result.
- **Exact arithmetic only.** No floating point anywhere.
- **Run the regression suite before any reported value.** Expected:
  `quad = 24`, `quad0 = 0`, `quadq raw 6×4 = 24`; `det3 L2 = 29/29/29` through
  `L6 = 1818118/2336283/2686868`; `f1C_00 L7 = 54685987/100774838/141001840`,
  `L8 = 128027708/422952740/603408404`. Any deviation aborts.
- **Two independent routes** for any value you intend to report.
- The container is scratch and can reset without warning. The git repository is
  the only durable copy; commit early and often, and stage from the repo rather
  than trusting anything left in the container.

### Deliverables

1. A pre-registration commit, before any value.
2. The answer, with its independent confirmation.
3. An update to `PROJECT_NOTES.md` (session record, results bank) and a new
   session entry appended to `docs/boundary_deficit.html` before its §5.
4. If 24 ∈ E: the value, its factorisation, and a revision of Corollary 4.5 in
   `paper/det3-conductor.tex`, which currently states the existence question as
   open.
5. If 24 ∉ E: the same, plus the sharpened constraint and the case for 30.
