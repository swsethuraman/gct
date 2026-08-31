You are joining a mathematics research programme called **gct** — conductors and
deficits of orbit closures. The repository is
`https://github.com/swsethuraman/gct` (public).

**Read first:** `PROJECT_NOTES.md` in full, then `paper/det3-conductor.tex`
Sections 1–4. The infrastructure protocol (rules 1–12) is binding.

**Branch discipline.** Three other sessions are working this repository in
parallel. Nobody owns `main`.

```
git clone https://github.com/swsethuraman/gct.git
cd gct
git checkout -b s24-obstruction
```

Push only that branch; if the git proxy refuses, commit locally and bundle.

**Record-keeping — changed protocol.** Do **not** append to `PROJECT_NOTES.md`
or `docs/boundary_deficit.html`; with four sessions running that produces
four-way conflicts. Write your record to a new file, `docs/session_24.md`.

---

## The question

This programme has computed the deficit carefully. It has not asked whether the
deficit is **good for anything** — specifically, whether it can serve as a
separation obstruction in the sense geometric complexity theory needs. That is
your task, and the honest answer may be no.

Start from the identity that makes the question precise. By definition

```
def(λ,δ) = m(λ) - mult_λ C[closure]_δ ,    so    mult_λ C[closure]_δ = m(λ) - def(λ,δ)
```

where `m(λ) = dim (S_λ^*)^H` is a pure stabiliser count — group theory, no
geometry. A **multiplicity obstruction** separating two orbit closures needs a
weight where `mult_λ` differs. By the identity, any such difference decomposes:

```
mult_λ(A) - mult_λ(B)  =  [ m_A(λ) - m_B(λ) ]  -  [ def_A(λ,δ) - def_B(λ,δ) ]
                            Peter-Weyl part         deficit part
```

**The Peter–Weyl part is the classical, well-studied side.** Bürgisser,
Ikenmeyer and Panova proved that occurrence obstructions — the special case where
one multiplicity is zero — cannot separate the padded permanent from the
determinant. **The deficit part is the side nobody has quantified.**

So the question, sharply: **can the deficit difference ever exceed the
Peter–Weyl difference, and thereby produce an obstruction that the classical
side does not see?**

## Do not attempt the real GCT case

The genuine question concerns `per_m` padded into `Sym^n C^{n^2}` against
`det_n`, and that is out of reach here: for `n = 4` the ambient space is
3876-dimensional against 165 for `n = 3`, and the stabiliser jumps from
dimension 17 to 31. A session that starts there will produce nothing.

**Work instead where complete deficit data already exists.** This programme has
two worlds with closed forms:

- **Binary quartics** (`Sym^4 C^2`, `v = x^4 + y^4`, `H` of order 32): Theorem 2.1
  gives `def = c = max(0, floor((a-3b)/8))` in closed form, total deficit
  `floor(δ^2/4)` at degree `δ`, all verified.
- **Ternary cubics** (`Sym^3 C^3`, Fermat, `H` of order 162): 254 deficit-positive
  weights through `δ = 10`, with the transport formula.

And for `det_3` itself there is a full census and the conductor at `(2,2,2)`.

## The concrete tasks

1. **Establish the decomposition properly.** State and prove the identity above
   as a lemma, with hypotheses. It is elementary but it is the frame for
   everything else, and stating it well may itself be the contribution.

2. **Find out whether the deficit part can ever dominate.** In the worlds where
   both terms are computable, construct or rule out a pair of orbit closures in
   the same ambient space, and a weight, where the deficit difference exceeds the
   Peter–Weyl difference in the direction that gives an obstruction. Any pair will
   do — this is a proof of concept, not the permanent.

3. **If you find one, say exactly how special it is.** Does it rely on the two
   stabilisers being non-conjugate? On one closure being non-normal and the other
   not? A separating example that depends on a feature the `per`/`det` pair does
   not have is a negative result dressed as a positive one, and should be
   reported as such.

4. **If you cannot find one, try to prove you cannot.** A theorem of the form
   "the deficit difference is bounded by the Peter–Weyl difference" would be a
   strong negative — it would say this programme computes a real invariant that
   is useless for separation, which is worth knowing and worth publishing.

## The standard you are held to

The honest outcome here is more likely negative than positive, and a negative
result reported clearly is the success condition for this session. This
programme has three pre-registered hypotheses that were refuted and kept in the
record, and the paper is stronger for them. Do not manufacture an obstruction.

Specifically, resist these:

- Comparing `per_3` and `det_3` as separate orbit closures in `Sym^3 C^9` and
  calling it a GCT statement. It is a model problem — there is no padding, the
  degrees match by accident of `n = m = 3`, and the real question has different
  shape. If you use it, label it.
- Concluding from one example that the deficit "gives new obstructions". One
  example shows the mechanism is not vacuous. That is all it shows.

## Discipline

Pre-register before computing, with named falsifiers. Exact arithmetic only.
Two independent routes for any reported value. The container is scratch — it has
been lost six times — and the repository is the only durable copy.

## Deliverables, on your branch

1. A pre-registration commit stating what you expect and what would falsify it.
2. `docs/obstruction_power.md` — the decomposition lemma, what you found or
   ruled out, and an explicit statement of what it would take to carry the
   argument to the real `per`/`det` case.
3. `docs/session_24.md` — the session record.
4. A recommendation, in one paragraph: is this a line of attack worth the
   engineering cost of `n = 4`, or is it a category error? That recommendation is
   the actual deliverable; everything else is the evidence for it.
