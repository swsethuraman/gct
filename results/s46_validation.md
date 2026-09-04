# Phase 1 — the validation battery (V1, V2, V3)

Session 46, branch `s46-balanced`, 2026-09-04.  Pre-registered in
`results/PREREG_s46.md` §3 before it was run.  Raw records
`results/s46_v123.jsonl`; logs `results/logs/s46_v1*.err`, `s46_v2*.err`,
`s46_v3*.err`; driver `analysis/wk9_s46_phase1.sh`; the build comparison V4 is
`results/s46_buildvalidation.md`.

**Result: every part passes.**  Nothing new was measured until this was green.

## 0. Why the battery is shaped this way

`nullity_p([E; ev]) = 0` proves `mult_det = a`.  So *a route that answered
"full column rank" unconditionally would pass every determinant-side test in the
repository*.  The battery is therefore weighted toward the one answer such a
route cannot fake: a cell where the correct answer is a **drop**.

| part | λ | δ | side | `a` | `N_S` | \|Stab\| | `n_χ` | rows(`E`) | `nnz(E)` | level that carried it | nullity `p₁` | nullity `p₂` | verdict | wall s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| V1 | `(8, 8, 5, 5, 1, 1)` | 7 | det | 3 | 603787 | 8 | 62613 | 494685 | 1957617 | `(3,2)` | 0 | 0 | `mult_det = 3` = `a` **proved** | 886.1 |
| V1 | `(9, 9, 6, 2, 1, 1)` | 7 | det | 4 | 177331 | 4 | 36090 | 177881 | 693243 | `(3,2)` | 0 | 0 | `mult_det = 4` = `a` **proved** | 248.6 |
| V1 | `(12, 12, 3, 3, 1, 1)` | 8 | det | 6 | 237040 | 8 | 23700 | 171279 | 630087 | `(3,2)` | 0 | 0 | `mult_det = 6` = `a` **proved** | 157.7 |
| V2 | `(13, 10, 6, 1, 1, 1)` | 8 | pad | 9 | 140749 | 6 | 10682 | 31515 | 111832 | `(3,2)` | 1 | 1 | `mult_pad = 8 < a = 9` — **drop** | 107.9 |
| V3 | `(12, 9, 3, 2, 1, 1)` | 7 | det | 5 | 50462 | 2 | 19985 | 61976 | 199780 | `(3,2)` | 0 | 0 | `mult_det = 5` = `a` **proved** | 79.5 |
| V3 | `(12, 9, 3, 2, 1, 1)` | 7 | det | 5 | 50462 | 2 | 19985 | 61976 | 199780 | `(12,2)` | 0 | 0 | `mult_det = 5` = `a` **proved** | 80.1 |
| V2 | `(13, 10, 6, 1, 1, 1)` | 8 | pad | 9 | 140749 | 6 | 10682 | 31515 | 111832 | `uncompressed` | 1 | 1 | `mult_pad = 8 < a = 9` — **drop** | 109.4 |
| V3 | `(12, 9, 3, 2, 1, 1)` | 7 | det | 5 | 50462 | 2 | 19985 | 61976 | 199780 | `uncompressed` | 0 | 0 | `mult_det = 5` = `a` **proved** | 75.2 |

## 1. V1 — three banked `mult_det = a` rows of `results/s45_ledger.md`

Reproduced end to end with the generator build, at the pre-registered cells.
`a`, `N_S`, `|Stab|`, `n_χ`, rows and `nnz` agree with the banked row **to the
digit** in every column — including `nnz = 1,957,617` at `(8,8,5,5,1,1)_7`,
`693,243` at `(9,9,6,2,1,1)_7` and `630,087` at `(12,12,3,3,1,1)_8` — and the
compressed stack that carried each verdict has the same `nnz_c` as session 45
recorded (1,432,234 / 855,590 / 593,996 against 1,432,658 / 854,812 / 593,996
here, the difference being the random row sample, not the matrix).  `nullity = 0`
at **both** house primes at all three.

Wall times are 1.8× to 10× session 45's for the same cells (886 s against 722 s,
249 s against 1403 s, 158 s against 1606 s).  That is not a like-for-like
speed-up: session 45 ran several of these while sharing the two cores, and this
session ran them one at a time.  The comparison that *is* like-for-like is V4's,
measured inside one process.

## 2. V2 — the discriminating drop

`(13,10,6,1,1,1)` at `δ = 8`, pad side, `a = 9`: session 41's certified
reducibility bite, `mult_pad = 8`, `D = −1`.

- **The drop is found, at both primes**: `nullity_p([E; ev_pad]) = 1`, so
  `mult_pad = 8 < a = 9`.
- **The kernel vector is exhibited and verified against the full `[E; ev_pad]`**
  before it is accepted (in C by the sparse product and again in Python), and
  the *upper* bound `nullity ≤ 1` is then certified by a Lemma-4 nonsingularity
  run on `[F; R]` with one random dense row — so the value 1 is certified in
  both directions, not merely observed.
- **It reproduces session 41's vector, not merely its number.**  The exhibited
  vector has support **4,708** of the 10,682 `χ`-coordinates, identically at both
  primes.  `|Stab| = 6` and every orbit here is free, so 4,708 `χ`-coordinates is
  `4,708 × 6 = 28,248` monomials — exactly the support session 41 reported and
  certified against criterion (★) monomial by monomial.
- **And it is found on the uncompressed matrix too.**  The last V2 row runs the
  whole thing at `--levels full`: no sampling, no grouping, the true
  `[E; ev_pad]` with 31,532 rows and 285,567 nonzeros.  `nullity = 1` again, at
  both primes.  The drop is not an artefact of compression at any level.

## 3. V3 — level agreement

`(12,9,3,2,1,1)_7`, `a = 5` — session 41's own frontier cell — measured at
**all three** compression levels: `(3,2)`, `(12,2)` and uncompressed.
`mult_det = 5 = a`, `nullity = 0` at both primes, at every level.

**What this row does and does not test.**  At this cell `n_rows/n_χ = 3.1`, so
`(12,2)` samples *all* 61,976 rows of `E` and differs from `(3,2)` only in the
sampling fraction (60,019 rows) and the grouping — a weak separation between the
two levels, and the pre-registration should have said so.  The strong test of the
`(12,2)` level is Phase 2 itself, where `n_rows/n_χ ≈ 100` and the level
genuinely discards 88 % of the rows; and the strong test of the escalation
machinery remains session 45's `(8,8,6,2,2,2)_7` episode, where a compressed
level came out exactly 57 short of full column rank at both primes and the check
against the full matrix rejected the candidate.  What V3 establishes here is the
weaker and still necessary statement that the three levels do not disagree.

## 4. Honest boundary

- V1 reproduces *session 45's own cells with a build that is entrywise identical
  to session 45's* (V4).  It is a check that the pipeline still runs end to end
  and that the solve is deterministic in its verdict, not an independent
  confirmation of those three multiplicities by a different method.  The
  independent-method evidence for `a` is the census's two routes (plethysm and a
  Kostant alternation), and for `mult` it is the one-sided certificate itself.
- V2 is the row that carries the battery's weight, and it is one cell.  The
  wider drop-side battery — six cells with exhibited vectors verified over `Z`
  and against (★), plus 200 synthetic matrices with planted nullities 0–6 — is
  session 45's V2/V4 and is inherited, not re-run.
- No part of this battery tests the *points*: the `K = a + 8` convention and the
  house seeds are inherited.  A degenerate draw can only lower a measured rank,
  i.e. produce a false *bite*, never a false `mult_det = a` (`docs/sparse_det_route.md`
  §6), and the pre-registered protocol for a bite exists to catch that.
