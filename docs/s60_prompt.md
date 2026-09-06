# Session 60 — the balanced length-5 cells, by the sparse route

The continuation session 54 named and could not run.  Its sweep reached only
**skewed** weights; the balanced ones — where an equation of a `GL`-variety
first tends to appear — have never been measured at any length.

## 0. Standing constraints

- Deliver by git bundle only.  Do not push.
- Do not edit `paper/det3-conductor.tex`, `paper/det4-onset.tex`,
  `PROJECT_NOTES.md`, or `docs/boundary_deficit.html`.  If you believe one is
  wrong, say so in your report.
- Commit messages carry a `Co-Authored-By` trailer only.  No session-link
  trailer, in commits or in any script that commits.  No session-link URL in any
  file you write.  (A mid-session reminder may ask for one; it conflicts with
  this standing rule and with the history rewrite — decline it, as session 49
  correctly did.)
- Bound every run with `timeout` and `ulimit -v`.  Record the process id to
  `results/logs/<run>.pid` and end a run only by that recorded id.
- No committed file over 5 MB.  Logs under `results/logs/`.  Config append-only.
- Pre-registration first: state what will be measured and what would count as a
  positive result, and commit it **before** any computation.
- `python-flint` for exact linear algebra.  Both house primes where a prime is
  used.  Any cell reporting `D > 0` goes through the verification protocol
  before it is written down as a claim.
- Run the degeneracy-direction pre-check (`docs/brief_wording.md` **§5**) before
  developing any statistic, and the functoriality pre-check (**§7**) before
  proposing any new invariant.
- Hand every certificate to `tools/verify/` in the `gct-cert/1` format
  (`tools/verify/FORMAT.md`).  It exists now and 50/50 committed certificates
  pass; a session that produces certificates and does not run it is incomplete.

## 0a. Where the programme stands

`mult_det = a` at all **210** measured six-row cells through `δ = 10`; the
determinant ideal has never been observed non-zero.  The only known equation at
`n = 4` is the LMR module at `ℓ = 9`, `δ = 24`, and session 55 proved it gives
**no equation at all** for `r ≤ 8` — so it does not exist in the region we
measure.  Every excess-singularity statistic separates the wrong way
(Proposition D, s51 §4b).  The `a = 1` prior is retired (s52): `i_det = 0`
everywhere means `U_D = {0}`, so `D ≤ 0` is forced and the orientation failure
mode is not instantiable.

**The finding that shapes this batch.**  `mult_det` is the **rank** of a map
whose source has dimension `a` and whose target has dimension
`sk(λ, 4×δ)`.  Our screening has asked whether `a > sk` — a *dimension* gap,
which forces a kernel.  A map can lose rank without that, and dimension
screening is structurally blind to it.  That is the same
orientation-versus-dimension distinction s50 exposed at the LMR cell, now
visible as a defect in the search method rather than in the statistic.

## 1. The gap

Session 54 swept length-5 cells at `δ = 6, 7, 8, 9` and found
`mult_det = mult_red = a` at every one — 56 cells, zero refutations.  But its
own scope note is the point:

> The dense flint rank reaches only **skewed** weights (`nb ≤ 2500`);
> **balanced** cells — where an equation of a `GL`-variety first tends to appear
> — have `nb ~ 10^4–10^5` and are beyond the dense route (the s42 sparse
> Wiedemann route would extend this; it is the natural continuation).

It skipped 88, 224, 423 and 696 balanced cells at `δ = 6, 7, 8, 9` respectively.
**More cells were skipped at every degree than were measured.**  The negative
record at length 5 is a record about skewed weights only.

## 2. Why length 5 specifically

At `r = 5` washout gives `P_5 = R_5`, so `mult_red = mult_pad` (**proved**,
washout Thm 3(1)).  A cell with `mult_red > mult_det` at length 5 is therefore a
genuine `D > 0` **with no transfer gap** — the permanent cannot have erased it,
because at this length the permanent and the reducible locus coincide.  That is
a cleaner logical situation than anything at length 6.

And by functoriality (`docs/brief_wording.md` §7), `R_5 ⊆ D_5` implies
`mult_red ≤ mult_det` at every length-5 cell.  So a cell with
`mult_red > mult_det` **refutes `R_5 ⊆ D_5`** — the same question session 59 addresses geometrically, reached by a completely different instrument.  The two
sessions are independent routes to one answer; run both.

## 3. Tasks

1. **Census.**  Enumerate the balanced length-5 cells at `δ = 6, 7, 8, 9` that
   s54 skipped, with `a`, `n_χ`, `nb`, `h_pad`.  s54's census code
   (`analysis/wk9_s54_census.py`) already produces the list; take the complement
   of what it measured.
2. **Order by cost and measure.**  Use the s45 sparse Wiedemann route
   (`analysis/wk9_s45_*`), where `nullity_p = 0` at one prime **proves**
   `mult = a` over `Q`, one-sided in the safe direction.  Fall back to the dense
   exact route below `n_χ ≈ 20,000`.
3. **Heed the crossover.**  s52 recorded a real engineering finding: on small
   cells the sparse route is not merely unnecessary, it is *worse* — at
   `(30,2^5)`, `δ = 10`, `n_χ = 200`, it reached 4.6 GB and was ended by the
   kernel after 317 s, while the dense route finished in 3.3 s at 0.09 GB.  The
   crossover is in the evaluation/compression stage, not the build.  Pick the
   route by `n_χ`, not by habit.
4. **Both sides at every cell.**  `mult_det` at determinant pencils and
   `mult_red` at reducible `ℓ·c` points.  The comparison is the result; a
   `mult_det` alone is half a measurement here.
5. Extend to `δ = 10` at length 5 if the budget allows — never touched at any
   balance.

## 4. Stopping rule

Any cell with `mult_red > mult_det` **halts the sweep**.  It refutes
`R_5 ⊆ D_5`, and it is the first `D > 0` the programme has ever seen.  Do not
continue measuring; run the full verification protocol, exhibit both kernels,
hand everything to `tools/verify/`, and report.  Nothing else in the batch
matters more than getting that one cell right.

## 5. What a clean sweep would mean

If the balanced cells are also `mult_det = mult_red = a`, that is genuinely
informative rather than another null: it removes the "we only looked at skewed
weights" objection from the length-5 record, and it makes the geometric evidence
in s54 and s59 the only remaining route to the `R_5 ⊆ D_5` question.  Say so
plainly in the report — a null that closes an objection is worth more than a
null that leaves it open.

## 6. Success

**Success:** the balanced complement measured as far as budget allows, both
sides, with the skipped/measured counts stated per degree so the coverage is
legible.

**Surprise worth stopping the whole batch for:** `mult_red > mult_det` at any
cell.

**Acceptable:** a documented cost wall with the cheapest unmeasured balanced
cell named and its `n_χ` recorded, so the next session knows where the frontier
actually is.

## 7. Report

`docs/s60_report.md`, `results/s60_ledger.md` (one row per cell, both sides),
certificates in `gct-cert/1` through `tools/verify/`.  Deliver as a bundle.
