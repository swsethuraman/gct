# Session 33 — pin `e`: the degree of the determinantal-quartic hypersurface at `r = 4`

You are **session 33** of the gct programme, working for the integrator.  Date
your work 2026-09-01 onward.  If the repository already shows a session
claiming number 33, do **not** renumber yourself — flag the collision in your
report and carry on (two sessions once independently took 23; the record keeps
collisions, it does not hide them).

## Rules (standing)

- Fresh clone of the public repository `github.com/swsethuraman/gct`.  Work on
  branch `s33-e4`, container only.
- **Ancestry check before anything else**: `git merge-base --is-ancestor
  29bea5f HEAD` must succeed — `29bea5f` (the s30 integrator review) must be
  an ancestor of the tip you cloned.  Ancestry, not equality; ancestry does not
  self-defeat.  If it fails, stop and report.
- Single-writer files — never touch: `paper/det3-conductor.tex`,
  `PROJECT_NOTES.md`, `docs/boundary_deficit.html`.
- Delivery is a **git bundle** (`git bundle create e4.bundle s33-e4`, single
  ref).  Do not push to the repository; the proxy will refuse, and that is an
  access control, not an obstacle to route around.
- Pre-registration first.  `results/PREREG_s33.md` is committed before any
  Phase-1 number exists, with named falsifiers and kill criteria, and a
  **regime statement**: say what regime each prediction's reasoning comes from.
  This house has been burned three times by carrying a pattern out of its
  regime.
- Bank incrementally: every result committed as it completes; the container
  resets.

## Context (read these first, in this order)

`docs/sweep62.md` §4 and `docs/s30_review.md` §3.  Established there:
`D_4 := closure{det_4(s_1 A_1 + ... + s_4 A_4)} ⊆ Sym^4 C^4` has codimension
**exactly 1** (Jacobian lower bound 34 meets the stabiliser upper bound
`16·4 − 30 = 34`).  Its ideal is therefore principal: one irreducible
polynomial `h` of some degree `e`, necessarily an `SL_4`-invariant of quartic
surfaces, of weight `(e,e,e,e)`.  **`e` is this session's entire object.**  It
is the onset degree of the determinant's ideal at four rows, and it calibrates
where the `r = 5` hunt should look.  Session 29's task B aimed at it
(`docs/visible_ideals.md`) and did not finish.

The corrected raising rule is now on `main` (`docs/isotypic_rank.md` §1 is
correct as of commit `7d93449`); you do not need to patch anything, but you do
run the witness (below) — it costs seconds and guards against a stale clone.

## Phase 0 — literature, before any computation

Determinantal quartic surfaces are classical: the generic quartic surface is
*not* determinantal (that is the codimension 1), and the determinantal ones
are classically characterised (smooth case: those containing a certain
degree-6, genus-3 curve).  The **degree of this hypersurface in
`P^34 = P(Sym^4 C^4)`** may be in the literature.  The model for what you are
looking for: the Lüroth hypersurface of plane quartics has degree 54 (Morley
1919; Ottaviani–Sernesi) — such degrees are sometimes classical and always
hard-won.  Search: "determinantal quartic surface", "degree of the
determinantal locus", Beauville *Determinantal hypersurfaces* (Michigan Math.
J. 48 (2000)) §6 and papers citing it, Ottaviani's surveys on determinantal
representations.  **Caution**: "quartic symmetroid" is the *symmetric*
determinantal locus — a different, smaller variety; do not conflate.  If a
value is found, pre-register it as P1 *with the source*, then certify it in
Phase 2 rather than trusting it.  If nothing is found after a genuine pass,
say so and list the searches.

## Phase 1 — the ambient ladder (cheap, exact, do it all before measuring)

`a(δ) := ⟨h_δ[h_4], s_{(δ^4)}⟩`, the multiplicity of `S_{(δ^4)}` in
`Sym^δ(Sym^4 C^4)`, for `δ = 2` up to at least `20`.  Adapt the method of
`analysis/wk8_s30_pleth.py` (it did `d = 4` plethysms already).  Every `δ`
with `a(δ) = 0` is excluded **for free** — no equation can live there.
Publish the full ladder in `results/e4_ledger.md` before any rank is
computed, together with each live rung's `N_S` (weight-space dimension) and
predicted memory at `5.6e-8 · N_S^2` GB against the ~6.5 GB usable budget.
That table is the map of what is reachable; commit it before Phase 2.

## Phase 2 — measure the live rungs, ascending

At each `δ` with `a(δ) > 0`, in ascending order with no rung skipped:
`mult_{(δ^4)} C[D_4]_δ` by the isotypic-rank method, corrected rule.

- **Witness first**: binary quartics, `closure{l^3 m}`, `λ = (4,4)`,
  `δ = 2` must give `mult = 0` with kernel `∝ (12, −3, 1)` (the wrong rule
  gives `(1, −4, 3)`).  Seconds.  If it fails: stop, report, touch nothing.
- Evaluation points: random 4-tuples `(A_1,...,A_4)` of `4×4` matrices over
  two word-size primes.  `python-flint` `nmod_mat` only — **no hand-rolled
  elimination**; it has failed two sessions' own self-tests.
- Per rung: `a` by kernel dimension must equal Phase 1's plethysm;
  `rank(R) = N_S − a` asserted; rank attaining `a` certifies `mult = a`.
- **The first rung with `mult < a` is the candidate `e`** — but only after
  the sceptical protocol: re-run at 3× evaluation points on a second prime
  and fresh seed; exhibit the kernel vector; verify it vanishes at 10 fresh
  determinantal points and does **not** vanish at several random
  non-determinantal quartics (if it vanishes everywhere you test, something
  is wrong — investigate before reporting).  Expected structure at the first
  rung: the ideal contributes exactly one unit (`mult = a − 1`), since the
  ideal is principal and `h` is its lowest piece.  If budget allows one rung
  above `e`, check consistency there too (the ideal's dimension at `e + k`
  is the dimension of degree-`k` invariants times… state what you expect
  *before* measuring it).

## Pre-registration contents (minimum)

- **P1**: the literature value of `e`, if found, with source; else "none
  found", with the search list.
- **P2**: your committed guess for `e`, with the reasoning *and its regime*
  stated.
- **P3**: every rung below `e` returns `mult = a` exactly.
- **Kill criteria**: (i) witness gate fails → stop; (ii) `mult < a` at two
  rungs with no consistent principal-ideal structure → the codimension-1
  premise is in question: re-run `analysis/wk8_s30_dims.py` at `r = 4` with
  fresh points before believing anything; (iii) memory wall → report the
  bracket `e > δ_reached` honestly, with the exact wall.  A bracket is a
  result; heroics are not.

## Deliverables

`results/PREREG_s33.md`, `results/e4_ledger.md` (ladder + per-rung record,
banked as completed), `docs/e4_hunt.md` (findings in the house style: proved /
measured / expectation, each labelled, honest boundary section), code as
`analysis/wk9_s33_*.py`.  Reuse s30's tooling wherever it fits; do not
rewrite what exists.  End your report with the bundle head hash.
