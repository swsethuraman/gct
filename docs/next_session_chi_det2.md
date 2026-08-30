You are continuing a mathematics research programme called **gct** — conductors
and deficits of orbit closures. Everything you need is in the public repository
`https://github.com/swsethuraman/gct`.

**This is a math-only session. No engine runs are required.** Sessions 15, 17
and 19 were run this way and each produced a deliverable; that is the
established mode for this kind of work.

**Start here.** Clone the repo and read `PROJECT_NOTES.md` in full. Then read,
in this order: `docs/evaluation_symmetry.md` (session 17, the double-coset
theorem), `docs/psi_identification.md` (session 18, Ψ derived), and
`docs/i6_identification.md` (session 19, Ψ = Aronhold). Also read
`docs/rigidity_theorem.md` — note the retraction notice at its top, which
matters for what you may assume.

**Branch discipline — read this before your first commit.** A second session is
working the engine track on this same repository in parallel. Neither of you
owns `main`. Work on your own branch and push only that:

```
git clone https://github.com/swsethuraman/gct.git
cd gct
git checkout -b s22-chi
```

Commit and push to `s22-chi` only. Do not push to `main`, do not rebase `main`,
and do not write to any local durable copy on the user's machine. The user
merges. A stale session overwrote the durable repo in week 3; this is why the
rule exists.

## The task

Close, or refute, **step (iii)** of the proof route for the totals law.

The law, currently empirical:

```
TOTAL(N) = Ψ(N) × 1,152,144,000
```

tested at Ψ = 1 (points C and R), Ψ = 4 (X4), and Ψ = 0 (P and four
compression points), and **at no other value** — `X_{-3}`, where Ψ = −3, has
never been measured. Here Ψ is the gauge `2u_1 − 4u_2 − D` on the slab normal
form, which session 19 identified exactly: `I_6(I, A, B) = −6·Ψ(A, B)` as an
identity in all 18 pencil indeterminates, so Ψ is the Aronhold degree-6
invariant of `C^3⊗C^3⊗C^3` restricted to the slab.

The route to a proof has four steps. Three are done:

- **(i)** TOTAL is bidegree (2,2). *Proved* — session 15 counting lemma.
- **(ii)** TOTAL is constant on the double coset `Q·u·H` up to a character χ,
  and that coset is the H-orbit of the net `Γ_N` **as a subspace**. *Proved* —
  session 17.
- **(iii)** Dependence on the subspace alone would make the net's basis change
  (the third tensor slot) act trivially, so TOTAL would be a conjugation
  invariant carrying a slab equivariance of character χ. **NOT VERIFIED. This
  is your task.** Specifically the *transpose coset* and the *slot dictionary*
  both need checking.
- **(iv)** If χ = det², session 19's uniqueness forces `TOTAL = c·Ψ`, and the
  value at C gives `c = 1,152,144,000`. *Proved, conditional on (iii).*

The single unproved link is **χ ↔ det²**. Session 17 found χ = Ψ on 120 of 120
same-coset pairs tested. That is evidence, not proof — a tensor semi-invariant
must transform by its character, so the agreement is expected if the
identification holds and says little if it does not.

Session 19's uniqueness statement is the one that makes step (iv) work, and it
is stronger than the form used in session 18: the bidegree-(2,2)
simultaneous-conjugation space is **9-dimensional**, not 10 — the ten trace
words satisfy exactly one relation, the polarised Cayley–Hamilton identity in
rank 3 — and inside it, **slab-equivariance alone leaves exactly one
dimension, spanned by Ψ.** The det²-slot is not needed for the
characterisation.

## Concretely, what to check

1. **The transpose coset.** H contains the transpose involution. Work out how
   it acts on the net `Γ_N` and on χ. This is named in the notes as one of the
   two unchecked pieces.
2. **The slot dictionary.** Pin down the correspondence between the net's third
   tensor slot (basis change) and the slab structure `(I, A, B)`. Step (iii)
   asserts that dependence on the subspace alone makes that basis change act
   trivially. Verify it or break it.
3. **If (iii) holds**, compute χ explicitly and compare it with det² on the
   slab. If they agree, the totals law is a theorem.
4. **If (iii) fails**, produce the counterexample — two points with the same
   net-as-a-subspace but different TOTAL, or a case where the third-slot change
   acts nontrivially. This is equally publishable and goes in the log either
   way.

## Traps this programme has already fallen into

Read these before starting; each cost a session.

- **Totals, not per-σ.** The double-coset theorem constrains *totals*. The
  σ-decomposition is scheme bookkeeping and is stable under neither Q nor H.
  Testing the theorem per-σ produces a spurious contradiction — session 17
  caught this mid-session. Relatedly, session 16 refuted both that the per-σ
  values inherit GL₂-covariance (`f1X4_00 = −308,145,600` against a
  pre-registered `+434,851,200`) and that they are simultaneous-conjugation
  invariants (a rank-9 parameter-free fit predicted `f1Y4_00 = +69,854,400`;
  the engine returned 0). Do not reintroduce either assumption.
- **The orientation of Q.** Q is the parabolic in which the weight-8 block
  *receives from* the weight-6 block. The opposite orientation puts every `u_N`
  inside Q and predicts `V ≡ 0`, which is refuted instantly. Check your
  orientation before building on it.
- **The homogeneity check.** `V(2N) = 16·V(N)` forces
  `χ = det(q|quotient)^8 · det(q|W)^6`, which returns exactly 16. Use it to pin
  conventions rather than assuming them.
- **The group has been smaller than the phenomenon before.** Session 17's
  honest negative: C and R lie in *different* cosets (vertex-rank invariant
  [1,2,2] against [1,1,1], transpose-stable) and yet have equal totals. So the
  double-coset symmetry does not by itself explain the universality of the two
  certificate points. Do not assume it does.

## Discipline

- **Pre-register.** Before you do the work, commit what you expect step (iii)
  to yield and why. Honest negatives are results here and are kept in the
  record.
- **Exact arithmetic only** for anything symbolic — sympy Rational or integers,
  never floating point.
- If you find that a single discriminating engine value would settle
  something, **do not run it** — pre-register the prediction, state what it
  would cost, and hand it to the engine track. `X_{-3}` (Ψ = −3) is the obvious
  candidate and has never been measured.
- The container is scratch and can reset without warning. The repository is the
  only durable copy.

## Deliverables, on your branch

1. A pre-registration commit, before the work.
2. `docs/chi_det2.md` — the deliverable, in the style of the other `docs/*.md`
   derivations: what was checked, what holds, what does not, and the honest
   boundary of what it proves.
3. A session record in `PROJECT_NOTES.md`, and a session entry in
   `docs/boundary_deficit.html` before its `§5` heading.
4. **If the gap closes:** revise `paper/det3-conductor.tex` — the totals law
   (currently Conjecture 5.5) becomes a theorem, and Question 7.2,
   which currently states this as the whole remaining gap, is rewritten or
   removed. This would be the largest single upgrade available anywhere in the
   programme.
5. **If it does not:** state precisely which of the two pieces failed and what
   the obstruction is, so the next session starts from a sharper question than
   you did.
