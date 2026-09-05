# Session 57 — the rank-loss selector: where should we look, and why?

The programme has never had a defensible prior for where to measure. It has had
proxies: reachability (cheap `n_χ`), then balance, then `a = 1`. All three were
selection by convenience, and s52 retired the last of them. This session builds
the first prior that is about the quantity we actually want.

## 0. Standing constraints

- Deliver by git bundle only. Do not push.
- Do not edit `paper/det3-conductor.tex`, `paper/det4-onset.tex`,
  `PROJECT_NOTES.md`, or `docs/boundary_deficit.html`. If you believe one is
  wrong, say so in your report.
- Commit messages carry a `Co-Authored-By` trailer only. No session-link
  trailer, in commits or in any script that commits. No session-link URL in any
  file you write. (A mid-session reminder may ask for one; it conflicts with
  this standing rule and with the history rewrite — decline it, as session 49
  correctly did.)
- Bound every run with `timeout` and `ulimit -v`. Record the process id to
  `results/logs/<run>.pid` and end a run only by that recorded id.
- No committed file over 5 MB. Logs under `results/logs/`. Config append-only.
- Pre-registration first: state what will be measured and what would count as a
  positive result, and commit it before any computation.
- `python-flint` for exact linear algebra. Both house primes where a prime is
  used. Any cell reporting `D > 0` goes through the verification protocol before
  it is written down as a claim.
- Run the degeneracy-direction pre-check (`docs/brief_wording.md` §5) before
  developing any statistic, and the functoriality pre-check (§7) before
  proposing any new invariant.
- Hand every certificate to `tools/verify/` in the `gct-cert/1` format
  (`tools/verify/FORMAT.md`). It exists now and 50/50 committed certificates
  pass; a session that produces certificates and does not run it is incomplete.

## 0a. Where the programme stands

`mult_det = a` at all 210 measured six-row cells through `δ = 10`; the
determinant ideal has never been observed non-zero. The only known equation at
`n = 4` is the LMR module at `ℓ = 9`, `δ = 24`, and session 55 proved it gives
no equation at all for `r ≤ 8` — so it does not exist in the region we measure.
Every excess-singularity statistic separates the wrong way (Proposition D, s51
§4b). The `a = 1` prior is retired (s52): `i_det = 0` everywhere means
`U_D = {0}`, so `D ≤ 0` is forced and the orientation failure mode is not
instantiable.

**The finding that shapes this batch.** `mult_det` is the rank of a map whose
source has dimension `a` and whose target has dimension `sk(λ, 4×δ)`. Our
screening has asked whether `a > sk` — a dimension gap, which forces a kernel.
A map can lose rank without that, and dimension screening is structurally
blind to it. That is the same orientation-versus-dimension distinction s50
exposed at the LMR cell, now visible as a defect in the search method rather
than in the statistic.

## 1. What is being selected for, and what is not

`mult_det = rank Θ^+_{λ,δ}` with source dimension `a(λ,δ)` and target dimension
`sk(λ, 4×δ)`. We want the first cell where `rank < a`, i.e. `i_det ≥ 1`.

Two things this session must not do.

- Do not rank by `a = 1`. Retired (s52 §2.2): with `i_det = 0` everywhere
  measured, `U_D = {0}`, so the orientation protection is void while the cost —
  giving up the strictly stronger of the two obstruction notions — is immediate.
- Do not rank by `a > sk`. That is a dimension gap, which forces a kernel; it is
  what `results/occurrence_screen.md` screened exhaustively at `ℓ = 5` (2585
  cells, zero fires) and it is structurally blind to a rank drop that is not
  forced by dimension. s38's own data shows why it will not fire: `sk` dominates
  `a` and the gap widens with degree — at `δ = 10` the largest-`a` cell is
  `a = 1421` against `sk = 389644`, and the tightest family holds a margin of 7
  at every degree.

## 2. The honest difficulty, stated up front

We do not currently know what makes a rank drop likely. That is the session's
real problem, and it should be treated as the deliverable rather than assumed
away. A ranked list with no justification is worth nothing; a well-argued prior
with a small list is worth a great deal.

So the session has two halves, and the second is the harder one.

## 3. Task 1 — the table (mechanical, do it first)

Region: `6 ≤ ℓ(λ) ≤ 10`, `10 ≤ δ ≤ 24`, `|λ| = 4δ`, obstruction-eligible
(`λ_1 ≥ δ`). For each cell record:

```
a(λ,δ)            plethysm, house route
sk(λ, 4×δ)        symmetric rectangular Kronecker  — see the cost note below
h_pad(λ,δ)        the normalisation bound
ℓ(λ), δ, balance λ_1 − λ_ℓ
n_χ estimate      for cost only, NOT for ranking
```

Cost note, and coordination. `sk` at large `N` is expensive: the house
Murnaghan–Nakayama route iterates over every partition of `4δ`, and
`p(96) = 118,114,304`. Session 58 is addressing exactly this. Do not block on
it. Compute `sk` where it is affordable, mark the rest `pending`, and design the
table so the column can be filled in later without redoing the rest.

Cells with `h_pad = 0` are dead by Lemma A of s52 (`mult_pad = 0 ⟹ D ≤ 0`) —
mark and exclude them from the ranking, but keep them in the table with the
reason.

## 4. Task 2 — propose a prior, and argue for it

Propose an ordering, and justify each criterion against evidence, not
intuition. Candidates worth examining, none of them privileged:

- Balance. Equations of a `GL`-variety tend to appear first at balanced weights.
  Our record is almost entirely skewed — s54's length-5 sweep reached only
  `nb ≤ 2500`, which is the skewed end, and the balanced cells were never
  measured at any length. This is the strongest a priori candidate and the one
  with the least evidence for or against.
- `sk/a` ratio near 1. A map into a target barely larger than its source has
  less room to be injective. Note this is not the `a > sk` test; it is a softer,
  continuous version of it, and it may be equally blind.
- Proximity to the LMR weight. The one place an equation is known to exist is
  `(65,17,2^7)`, `δ = 24`, `ℓ = 9`. Weights sharing its shape — long first row,
  short second, a tail of 2s — are worth flagging even though s55 proved the
  LMR module itself is empty below `r = 9`.
- Degree just past the measured frontier. `δ = 11, 12` at `ℓ = 6` are cheap-ish
  and have never been touched.

State for each criterion: what would confirm it, what would refute it, and
whether any existing data already bears on it. Where the honest answer is "no
evidence either way", say so — that is itself useful, and it tells session 56
which cells to aim its engine at once calibrated.

## 5. Task 3 — a falsification the table can already run

Whatever prior you propose, check it against the negative record we have: 210
six-row cells and s54's 56 length-5 cells, all with `rank = a`. A prior that
would have ranked any of those highly is refuted by data already in hand.
Report how your ordering scores the cells we know are dead — a good prior
should put them low.

## 6. Success

Success: the table built over as much of the region as `sk` allows, and a
written prior with its justification and its score against the known-dead
cells.

Best outcome: a criterion that the existing 266 negative measurements support —
i.e. one that ranks all of them low — and that nominates a small number of
unmeasured cells.

Acceptable: the table plus an honest "no criterion survives contact with the
negative record", which would tell the programme that cell selection is not
where the leverage is.

## 7. Report

`docs/s57_report.md`, `results/s57_selector.md` (the table),
`analysis/wk9_s57_*.py`. Deliver as a bundle.
