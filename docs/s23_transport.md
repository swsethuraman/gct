You are joining a mathematics research programme called **gct** — conductors and
deficits of orbit closures. The repository is
`https://github.com/swsethuraman/gct` (public).

**Read first, in this order:** `PROJECT_NOTES.md` in full (results bank and the
infrastructure protocol, rules 1–12, both binding), then `paper/det3-conductor.tex`
Sections 1–3, then `analysis/wk1_*.py` and `analysis/wk2_*.py` which contain the
closed-form work for the two worlds.

**Branch discipline.** Three other sessions are working this repository in
parallel. Nobody owns `main`.

```
git clone https://github.com/swsethuraman/gct.git
cd gct
git checkout -b s23-transport
```

Push only that branch. If the git proxy refuses, commit locally and send a
`git bundle` at each milestone.

**Record-keeping — changed protocol.** Do **not** append to `PROJECT_NOTES.md`
or `docs/boundary_deficit.html`. With four sessions running, shared-file appends
produce four-way merge conflicts. Write your session record to a new file,
`docs/session_23.md`, in the style of the existing `docs/*.md` deliverables. The
integrator folds it into the shared records once.

---

## The task: prove the transport formula, or find where it fails

This is Question 7.1 of the paper. Theorem 3.1 states that for the ternary-cubic
world — `v` the Fermat cubic, `H = mu_3^3 : S_3` of order 162, `Ω̄` the Aronhold
quartic hypersurface — on every weight with `m(λ) > 0` and `δ ≤ 10`, all 254 of
them,

```
c(λ) = floor( (λ_1 - 2λ_3) / 6 ) = floor( mu_max(λ) / |w_N| )
```

the maximal boundary-torus weight divided by the normal weight.

**The upper bound is already proved** by the block-order estimate: the
normalised Waring blocks have exact orders −1, 0, +1 as recorded in §3, Young
symmetrisation only cancels, and the first fundamental theorem gives spanning.
**What is missing is attainment.** Right now equality is machine-verified on a
finite range and conjectured beyond it.

Prove attainment, or characterise exactly when it fails.

## Two things the referee pass handed you

**(1) The hypothesis is `m(λ) > 0`, and that is checkable.** `m(λ)` is a pure
stabiliser character count — cheap, and independent of `Ω̄`. The theorem was
originally stated on "deficit-positive weights", which is useless as a
hypothesis because you would need the answer to check it. The current form is
usable.

**(2) Attainment fails exactly on empty support, and the failures have
structure.** In the sweep over `δ ≤ 10`, `λ_1 ≤ 20`, the weights with
`m(λ) = 0` and shadow pole `≥ 1` are

```
(10,1,1)  [δ=4]      (13,1,1)  [δ=5]      (11,11,2)  [δ=8]
```

and extending to `δ ≤ 16` adds `(17,17,5)` at `δ=13`. They come in
**GL_3-dual pairs**:

```
V_(10,1,1)^* (x) det^12 = V_(11,11,2)     Weyl dims 55, 55
V_(13,1,1)^* (x) det^18 = V_(17,17,5)     Weyl dims 91, 91
```

Is the orphan locus stable under `λ -> λ^* (x) det^k` in general? If it is, that
is a structural statement about where attainment fails and it may be the key to
the proof rather than a curiosity. Nobody has looked.

## Why this is the right problem now

It is the strongest mathematical claim in the programme that is not yet a
theorem, and it is the one a referee will care most about — a formula computing
a hard invariant from boundary data alone. It needs no engine and no
computation beyond character counts. And it is independent of everything
currently in flight: two other sessions are testing and extending results about
`det_3`, and none of that touches this.

If it closes, it is the core of the next paper.

## Discipline

- **Pre-register.** Before doing the work, commit what you expect and why, with
  named falsifiers. Commits `2545f1e` and `f9b4485` on `main` are the model.
- **Exact arithmetic only** — sympy Rational or integers, never floating point.
- **Honest negatives are results here.** Three pre-registered hypotheses have
  been refuted and kept in the record; the paper is stronger for it. If
  attainment fails in a way that kills the conjecture, that is publishable and it
  goes in the log.
- If you want a computation that would discriminate, extend the existing sweep
  yourself — the world-B machinery is small and fast. Nothing here needs the
  engine that the other sessions are using.

## Deliverables, on your branch

1. A pre-registration commit before any work.
2. `docs/transport_formula.md` — the derivation, what is proved, what is not,
   and the honest boundary between them.
3. `docs/session_23.md` — the session record.
4. If it closes: a revision of Theorem 3.1 and Question 7.1 in
   `paper/det3-conductor.tex`, stating the general theorem and its hypothesis.
   Note that the paper is in submission preparation, so mark any paper edit
   clearly in your record — the integrator may hold it for the next paper rather
   than the current one.
