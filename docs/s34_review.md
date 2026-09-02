# Integrator review — session 34 (δ = 7 at ℓ ≥ 5, n = 4: census + sweep)

2026-09-02.  Branch `s34-d7`, final head `2f6b9c4` (37 commits on `29bea5f`;
measured record closed at `7a2c811`, two housekeeping commits above).
Ancestry verified.  Everything checkable below was re-verified independently.

## 1. Verification — all pass, by a third route

- **Ledger arithmetic.**  46 rows, all `|λ| = 28`, all `ℓ = 5`, every row
  `mult_det = mult_pad = a` and `D = 0`; ambient units sum to exactly 258;
  `a` ranges to 15; `N_S` 1482–11269; no `DEFER-MEM` flag survives — the five
  giants were completed, as claimed.
- **The caps themselves.**  "`mult = a`" is only as strong as `a`.  I
  recomputed `a(λ, 7)` **and** `N_S` for all 46 cells by Kostant alternation
  over weight multiplicities in five variables (per-cell capped DP) — a route
  sharing nothing with either of the session's two plethysm implementations.
  All 46 match on both numbers.  The δ = 8 scoping appendix's cheapest cell
  `(22,5,2,2,1)` also reproduces (`a = 2`, `N_S = 1527`).
- **Discipline.**  Prereg first; witness exact; battery quoted by its
  discriminating count (41 of 48); three hash-rule re-certs exact on s30's
  own code path; census committed before the sweep; pre-registered interleave
  kept with the `a = 15` probe early; sceptical branch never entered because
  nothing was ever below `a`.

## 2. What the result means — read with the washout in hand

Every reachable cell at δ = 7 has both ideals empty.  Two readings, kept
separate:

- **On the determinant side this is a real number**: the onset of
  `I(D_5^det)` is above 7 on the measured corner (`ℓ = 5`, `N_S ≤ 11269`,
  `a ≤ 15`, balance ≥ 10).  Together with s30 and the 405 cap the det-side
  window is `[8, 405]` — session 38 starts exactly here.
- **On the permanent it says nothing, and could not have** (`docs/s35_review.md`
  §1): at five rows the padded permanent's restriction is `l·(any cubic)`, so
  this sweep — like every ℓ = 5 sweep — measured reducibility against the
  determinant.  The session did not know this when it ran (it cloned before
  s35 landed) and its verdict is worded correctly anyway: "both ideals still
  empty," no more.  Its P4-style representativeness result stands: through
  `a = 15` and down to balance 10 the reachable corner is uniform.

The census is the durable deliverable: 433 cells / 2708 units at the gate,
`ℓ = 5/6/7 = 210/194/29`, the ℓ ≥ 6 strata starting at `N_S = 20850`, the
`a = 26` summit at ~38 GB, and the δ = 8 scoping (1569 cells / 24,964 units,
~46 reachable) that session 38 inherits.

## 3. Catches

- **The `.gitignore` overwrite (fixed at merge).**  The session's final
  housekeeping replaced the repository's 23-line `.gitignore` with three
  lines, dropping the rules for container-built binaries, `*.dat` level
  files, `*.bundle`, and every `paper/*` build artifact.  Merged blind, the
  next `git add` would have tracked PDFs and bundles.  Restored at the merge
  (original file plus `results/claims_d7/`).  **New house rule for briefs**:
  a session may append to repository-wide configuration, never rewrite it,
  and must diff any such file against its base before committing.
- **A stale recommendation.**  "Pin `e` (literature-first, Lüroth analogy)"
  was already done by session 33 (`e = 320112`, verified); s34 could not know.
  No action.
- **The memory constant moved again**: 3.2–3.4e-8 observed in fresh per-cell
  processes versus the 5.6e-8 planning figure.  The frontier is set by process
  hygiene as much as by `N_S`; the s36/s38 briefs planned on 5.6e-8 and will
  simply reach further than they expect.  Harmless.
- **The 40 GB box.**  s34 is right that one memory upgrade would retire three
  sessions' honest-boundary caveats at once — but session 36's stabiliser
  reduction may retire most of the same cells for free (the balanced ones
  shrink by up to 24×).  Decide on hardware after s36 reports, not before.

## 4. Standing after session 34

The δ = 7 five-row corner is closed, 100% of the feasible set, uniform.  The
det-side window is `[8, 405]`.  Nothing at ℓ = 5 can see the permanent; the
first cells that can are ℓ = 6, which s36 is measuring now.  Process: the
claim queue and PID discipline ran three worker generations with zero races —
the s30 engineering has fully paid for itself.
