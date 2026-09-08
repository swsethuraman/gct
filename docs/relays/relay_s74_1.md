# Relay to session 74 — one sequencing correction, and two consequences

From the integrator, mid-flight.  **Nothing in your brief is withdrawn.**  This
changes the *order* of one thing and adds two cheap deliverables.  If you have
already started, you do not need to re-plan.

## 1. The correction — `i_det(23)` is not a preliminary check

Your brief says measuring `i_det(23)` is "the cheapest path to half the answer."
That is wrong and it could mislead your sequencing.  Building the `δ = 23` source
means rungs 13 through 23 — **273 of the 274 directions**.  It is the entire
source construction minus one vector, not a cheap first step.

What is true is only that it is *sufficient* for the determinant side: it does
not need the 274th vector.

**Do this instead of treating evaluation as a final step.**  The determinant
column accumulates incrementally.  Any partial `δ = 23` source of dimension `m`
on which the determinant evaluation has rank `m` gives

    rank T_det(24)  ≥  m

immediately, by transport — the argument is `ker(T_det) ∩ uM₂₃ = u·(I(Det) ∩ M₂₃)`,
which holds because `I(Det)` is prime and `u ∉ I(Det)`.  So:

- evaluate the determinant column **rung by rung, as rungs land**, not once at
  the end;
- carry `rank T_det` as a running lower bound;
- **stop the determinant side the moment it reaches 273**, whatever is still
  unbuilt.  With LMR's `rank T_det ≤ 273` that is the exact value, and
  `i_det(24) = 1`.

A night that ends with a partial source and a *finished determinant column* is a
much better night than one that ends with a fuller source and no evaluations.

## 2. `ε_det` is forced, so the obstruction vector is a linear solve

Write `M₂₄ = uM₂₃ ⊕ ⟨v⟩` with `v = F_{T₅₇}` (`results/wk12_int_lmr_birth24.json`;
renamed from `F₅₇` — `T₅₇` is the filling, `F_T` is the house convention).  For a
prime ideal `I_X` with `u ∉ I_X`,

    i_X(24) = i_X(23) + ε_X,   ε_X ∈ {0,1},
    ε_X = 1  ⟺  ∃ w ∈ M₂₃ with v + u w ∈ I_X.

LMR gives `i_det(24) ≥ 1`.  So **if you measure `i_det(23) = 0`, then `ε_det = 1`
necessarily** — the determinant ideal meets the birth line, no search required.

That makes the goal-cell determinant obstruction **explicitly constructible**:
solve the linear system for the `w ∈ M₂₃` with `v + u w ∈ I(Det)`.  Once you have
the `δ = 23` source and its determinant evaluation matrix, this is one solve.
**Bank that vector if you get it** — it is the first explicit determinant
obstruction the programme would own at the goal cell.

## 3. Where to spend whatever time is left

With `i_det(23) = 0` forcing `i_det(24) = 1`,

    D(24) = 1 − i_pad(24),        i_pad(24) = i_pad(23) + ε_pad.

So `D = +1` iff `i_pad(24) = 0`.  **Every remaining unknown is on the padded
side.**  Prioritise the true padded column (`ℓ · per₃`, not `ℓ · c`) over the
reducible and `per₄` columns if you are short of time — and note that a nonzero
padded evaluation of `v` alone does **not** give `ε_pad = 0`.  What is needed is
that `T_pad(v)` lies outside `T_pad(uM₂₃)`.

Record: commits `2ba3519` and earlier on `origin/main`;
`docs/batch12_integrator_note3.md`.
