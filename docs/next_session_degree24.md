You are continuing a mathematics research programme called **gct** — conductors
and deficits of orbit closures. Everything you need is in the public repository
`https://github.com/swsethuraman/gct`.

**Start here.** Clone the repo and read `PROJECT_NOTES.md` in full before doing
anything else — the results bank and the infrastructure protocol (rules 1–12)
are both there and both are binding. Then read `results/results_f1C.md` and
`results/results_R.md` for how a value gets recorded.

**Branch discipline — read this before your first commit.** A second session is
working the theory track on this same repository in parallel. Neither of you
owns `main`. Work on your own branch and push only that:

```
git clone https://github.com/swsethuraman/gct.git
cd gct
git checkout -b s21-degree24
```

Commit and push to `s21-degree24` only. Do not push to `main`, do not rebase
`main`, and do not write to any local durable copy on the user's machine. The
user merges. This is not bureaucracy — a stale session overwrote the durable
repo in week 3 and the recovery cost a day.

## The task

Decide whether the orbit closure of the 3×3 determinant carries a nonzero
SL_9-invariant in **degree 24**.

Let `G = GL_9` act on `W = Sym^3 C^9`, let `Ω̄ = closure(G · det_3)`, and let
`E(det_3) = { δ : C[Ω̄]^{SL_9}_δ ≠ 0 }`. Degree 24 corresponds to the
rectangular weight `λ = (8^9)`, since an SL_9-invariant of degree δ carries
GL_9-weight `det^{δ/3}`. Determine whether `C[Ω̄]^{SL_9}_24` is zero or
one-dimensional.

## Why the answer is forced to exist somewhere

1. **Bürgisser–Ikenmeyer** (arXiv:1511.02927) Theorem 3.4: for polystable `w`
   the degree monoid generates `b(w)·Z`, with degree period `b(w) = (m/D)·a(w)`.
   Their Theorem 2.5 gives stabilizer period `a(det_n) = 2` when
   `n ≡ 2, 3 (mod 4)`. For `det_3`: `m = 9`, `D = 3`, `a = 2`, so
   **`b(det_3) = 6`**, hence `E ⊆ 6Z` and **`gcd E = 6` exactly**.
2. Ours: `min E = e(det_3) = 18`, with
   `Φ_18(det_3) = −877,879,296,000 = −2^16·3^7·5^3·7^2`.
3. Therefore **`E ≠ 18N`** — if it were, the gcd would be 18, not 6. So an
   invariant exists in some degree that is a multiple of 6 and not of 18.
   Candidates in order: **24, 30, 42**. (36 = 2·18 is automatic; 12 ∉ E.)

The search terminates. The answer at 24 is informative either way: nonzero
gives the second generator of the invariant semigroup; zero tightens the
constraint and makes 30 the target.

A degree-24 invariant, if it exists, is a **new generator**, not a product —
there is no degree-6 invariant on Ω̄ to multiply `Φ_18` by.

## The bracket census does not decide this one

An SL_9-invariant of degree δ on `Sym^3 C^9` is spanned by products of
`k = δ/3` nine-fold brackets in δ symbolic letters, each letter occupying
exactly 3 brackets. If two letters occupy the same three brackets, the
transposition exchanging them multiplies the monomial by `(−1)^3 = −1` while
the invariant it evaluates to is unchanged, so that invariant vanishes. Rows
are 3-subsets of `[k]`, so everything with `δ > C(δ/3, 3)` dies — which is
exactly `δ ≤ 15`, and is what proves `e(det_3) ≥ 18` with no computation.

At δ = 24: `k = 8` and `C(8,3) = 56 ≥ 24`. The census permits it. No hand
argument currently settles degree 24 in either direction. That is why this is
an engine question.

## Strategy — cheapest route first

The two outcomes cost very different amounts, and that should drive the plan.

**(i) Try the extension question by hand first.** On the *orbit* there is an
invariant `φ` of degree `b = 6` (Bürgisser–Ikenmeyer Lemma 3.2), and
`E = { 6k : φ^k extends regularly to Ω̄ }`. So `Φ_18 ∝ φ^3`, and the question is
exactly **whether `φ^4` extends regularly across the boundary.** We know
`div(Φ_18) = 6P_1 + 9P_2`, where `P_1` and `P_2` are the two boundary
components of Hüttenhain–Lairez (orbit closures of the determinant of the
generic traceless matrix, and of the universal quadric). This may settle the
question with no computation at all. Try it before touching the engine.

**(ii) If that fails, prove membership by evaluation.** It suffices to exhibit
*one* SL_9-invariant of degree 24 on the ambient `Sym^3 C^9` whose value at
`det_3` is nonzero — a nonzero value at a point of the orbit means the
restriction to Ω̄ is not identically zero. One number.

**(iii) Only if both fail, the full census.** The multiplicity of
`λ = (8^9)` in `C[Ω̄]_24`. This is the only route that can prove
*non*-membership, and it is strictly larger than the δ = 18 run. Checkpoint
from the start and budget accordingly.

Failing to find an invariant in (ii) is **not** a proof of vanishing. If that
is where you end up, say so plainly rather than reporting a negative.

## Discipline — non-negotiable

- **Pre-register.** Commit your prediction *with its reasoning* to git before
  the value exists. Which of 24, 30, 42 do you expect, and why? The repository
  README argues the commit history is part of the evidence, and two
  pre-registered hypotheses have already been refuted and kept in the record.
  A refutation logged honestly is a result.
- **Exact arithmetic only.** No floating point anywhere in the pipeline.
- **Run the regression suite before any reported value.** Expected:
  `quad = 24`, `quad0 = 0`, `quadq raw 6×4 = 24`; `det3 L2 = 29/29/29` through
  `L6 = 1818118/2336283/2686868`; `f1C_00 L7 = 54685987/100774838/141001840`,
  `L8 = 128027708/422952740/603408404`. Any deviation aborts the run.
- **Two independent routes** for any value you intend to report.
- The container is scratch and can reset without warning — this has happened
  five times. The git repository is the only durable copy. Commit early, and
  re-clone rather than trusting anything left in a container.

## Deliverables, on your branch

1. A pre-registration commit, before any value exists.
2. The answer with its independent confirmation, recorded in
   `results/results_deg24.md` in the style of the existing results files.
3. A session record appended to `PROJECT_NOTES.md`, and a session entry added
   to `docs/boundary_deficit.html` immediately before its `§5` heading.
4. A revision of the **semigroup corollary** (currently Cor. 4.8) in
   `paper/det3-conductor.tex` — which currently states this question as open and names
   24 as the smallest candidate. If 24 ∉ E, revise it to the sharpened
   constraint and make the case for 30.
