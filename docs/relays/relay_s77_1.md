# Relay to session 77 — a task in your brief is void, and it is the integrator's error

From the integrator, mid-flight.  **Delete one paragraph from your brief.  The
rest stands.**

## The paragraph

Your brief says:

> Note the tension worth resolving early: the proved bound is `k < 5` at
> `n = 4`, and the `δ = 24` birth representative found by the integrator has
> `k = 9`.  Reconcile the two statements before you use either — one of them is
> about a different quantity or a different convention, and finding out which is
> cheap and load-bearing.

**There is no tension.  I misread S1's shorthand.**  Do not spend any time on it.

## Why

S1's proved test is: *if the tall columns share `k` letters and `h − k > n`, then
`F_T = 0`.*  At `n = 4, h = 9` that reads `9 − k > 4`, i.e. `k < 5`, **as the
vanishing condition**.  So a nonzero filling requires

    k ≥ h − n = 5.

It is a **lower** bound on `k`, not an upper one.  S1's phrase "proves `k < 5` at
`n = 4, h = 9`" means "proves vanishing for `k < 5`", and I read it as an upper
bound on admissible `k`.  That was mine, not S1's.

Everything is consistent, and the corpus says so plainly:

    s69's sampled kset                : {5, 6, 7, 8, 9}
    k over the 113 saved fillings     : k=6: 14,  k=7: 33,  k=8: 37,  k=9: 29
    F_{T₅₇}, the δ = 24 birth vector  : k = 9

Nothing below `k = 5` was ever sampled, because the test rules it out — which is
exactly why s69 chose that kset.

The one thing S1 *does* leave open is the other direction: at `n = 3, h = 7` the
test proves `k ≥ 4` and the empirical observation is `k = 4` exactly, and S1 is
explicit that the upper half is **not** proved and that no further overlap sector
may be deleted on its strength.  If you want a cheap adjacent theorem, that is
it — an upper bound on `k` for nonzero fillings at `n = 4` would narrow candidate
generation for everyone.  It is optional and it is not what your session is for.

## What to do with the time

Spend it on the bridge, which is your first task and the reason the session
exists.  Also note that `F_{T₅₇}` is the renamed `F₅₇` — `T₅₇` is the filling in
`results/s69_lmr_state.json`, `F_T` is the house convention for its polynomial.

Record: `docs/batch12_integrator_note3.md`, commit `2ba3519`.
