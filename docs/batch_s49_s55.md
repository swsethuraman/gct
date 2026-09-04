# Batch s49–s55 — launch order, dependencies, and housekeeping

## The seven sessions

| # | session | category | depends on | can run tonight |
|---|---|---|---|---|
| 49 | Foundations audit + two-layer verifier | infrastructure | — | yes, first |
| 50 | LMR equation: derive, then evaluate | GCT / equations | — | yes |
| 51 | `Λ^5` from the Gulliksen–Négård resolution | GCT / caps | — | yes |
| 52 | The `a = 1` census, BIP gate first | GCT / multiplicities | — | yes |
| 53 | Border degenerations of `det_4`, first layer | border complexity | — | yes |
| 54 | Is `R_5 ⊆ D_5`? | border complexity | shares method with 53 | yes |
| 55 | Equations below degree 24 | literature census | — | yes |

All seven are self-contained.  None blocks another.  s49 should be launched
first only because the others hand certificates to its verifier; if it has not
finished, they serialise their certificates in the declared format and the
verifier runs over them afterwards.

If only three slots are available tonight: **50, 54, 49**.  s50 is the highest
information per unit of compute in the whole programme.  s54 is the only session
whose upside lands inside our measurable range.  s49 is the one everything else
is graded against.

## Two categories, kept separate

- **GCT track** (49, 50, 51, 52, 55): multiplicities, ideals, equations in
  `Sym^δ Sym^4 C^r`.  This is the existing programme.
- **Border track** (53, 54): direct non-membership arguments through the base
  locus of a degeneration.  This abandons the multiplicity statistic rather than
  sharpening it.  It is a legitimate second line and it should not be folded
  into the first.  s54 sits in the border track but its negative outcome feeds
  the GCT track directly, which is why it is the more valuable of the two.

## Changes from the previous plan

- The old s52 (`ℓ = 9` sweep) was killed and replaced by the `a = 1` census.
- The old s53 (below degree 24) is now s55, narrowed to a census with re-derived
  degrees.
- s53 and s54 are new, from the external E7/SL_8 session — restaged as
  bounded-rank-matrix-space sessions, since by that session's own account the
  exceptional-group content drops out of the argument entirely.
- s49 gains the degeneracy-direction pre-check as a house rule.

## Housekeeping — do these before launching

1. **Merge the outstanding bundles** for s46, s47, s48.
2. **Commit the seven briefs** and `brief_wording.md` to `docs/`, so the workers
   can be pointed at committed documents.
3. **Rebuild `sixrow_record.md`** to 193 cells / 593 units after the merges.
4. **Remove "exact whenever it fires"** from `docs/s43_review.md` and from the
   six-row record.  s47 refuted it.  (s49 will sweep for the rest, but these two
   are known.)
5. **Commit `docs/critique_response.md`** with the two corrected citations —
   Kronecker-positivity hardness is Ikenmeyer–Mulmuley–Walter, *Comput.
   Complexity* **26** (2017), and Gulliksen–Négård is *C. R. Acad. Sci. Paris
   Sér. A* **274** (1972), 16–19 — and `docs/critic_e7_response.md`.

## Housekeeping — the ordering constraint that matters

The repository privacy switch (private archive, new public repository, history
scrubbed with `git-filter-repo`) **rewrites every commit hash**.  Bundles created
against the old history will not apply cleanly afterwards.

So do not run the rewrite in the middle of this batch.  Either:

- run it **tonight, before launching**, and point every worker at the new
  repository; or
- **postpone it** until the whole s49–s55 batch has been merged.

The exposure is unchanged either way — the session links are already in a public
history and a few more days does not change that — whereas rewriting mid-batch
guarantees that every in-flight bundle has to be rebased by hand.  Postponing is
the lower-risk choice unless the switch can be finished before the first worker
starts.
