# Provenance of the randomised evaluation pencils

Session 49 (brief §2.6), 2026-09-05.  The Schwartz–Zippel and multimodular
arguments of the programme draw integer pencils from a fixed seed and read a
rank; the honesty of "read a rank at a *fixed* random pencil" depends on the
pencil having been fixed **before** the rank was read, not chosen after seeing
which seed gives the wanted drop.  This page records, from the git history, when
each seed was fixed relative to the runs that used it.  The verdict is mixed and
stated plainly.

## What the git history shows

**Session 44 — the six-row Macaulay ladder and the `d = 7` certificate.**

| commit | time (UTC) | content |
|---|---|---|
| `2e06e3f` | 2026-09-03 02:29 | `results/PREREG_s44.md` — **before any rank**; fixes the *protocol* |
| `e50575a` | 2026-09-03 03:02 | ladder ranks **and** the analysis scripts carrying the seed |
| `ed838d5` | 2026-09-03 03:23 | the multimodular certificate (three pencils, ~1790 primes) |

The pre-registration at `2e06e3f` fixes the **protocol** before any computation:
integer entries in `±BOX`, `BOX = 10^6`; at least three fresh pencils per degree;
both house primes; a drop that appears at one seed or one prime and not another
is to be treated as a bug (`results/PREREG_s44.md` §"Randomised protocol").  It
does **not** commit the concrete seed value.  The seed is
`SEED = 20260903` (the session date), a default constant in
`analysis/wk9_s44_certify.py`, `wk9_s44_ladder.py`, `wk9_s44_anchor.py`,
`wk9_s44_sweep.py`, `wk9_s44_r4.py`, and pencils are drawn as
`random.Random(SEED + offset)` with per-run offsets.  That constant first
entered the repository at **`e50575a`**, in the same commit as the first ranks —
so from the history the seed was fixed **before the `d = 7` certificate**
(`ed838d5`, 03:23) but **committed together with the first ladder ranks**
(`e50575a`, 03:02), not in a separate pre-run artifact.

**Session 48 — the `(5,7)` rank.**  `results/PREREG_s48.md` at `902cccd`
(2026-09-04 03:54, before any computation) fixes the protocol; the concrete
seeds (`random.Random(70000 + sd)` for the quintic controls,
`random.Random(80000 + sd)` for the determinantal pencils, in
`analysis/wk9_s48_ladder57.py`) entered at `ddb76cd` (04:23), together with the
results.  Same pattern as s44.

## Verdict, stated plainly

- **The protocol was pre-registered before any computation** in both sessions
  (`2e06e3f`, `902cccd`): box, number of seeds, both primes, and the "one seed /
  one prime ⇒ bug" rule were all fixed ahead.  This is on the record and is
  solid.
- **The concrete seed was not banked in a pre-run commit.**  In both sessions
  the seed constant appears in git only in the commit that also carries the
  results (`e50575a`, `ddb76cd`).  So *from the git history alone* one cannot
  certify that the seed was chosen before the rank was seen — only that the
  protocol was.
- **Why this is nonetheless not a real p-hacking risk here.**  (i) The seeds are
  the session date (`20260903`) and round constants (`70000`, `80000`), not
  values that look searched-for.  (ii) The drop is not marginal and not
  seed-dependent: `rank = 660` at `d = 7` (drop 6) and `rank = 5859` at `(5,7)`
  (drop 21) reproduce at **every** seed and **both** primes tried, and the
  `d = 7` drop is upgraded to an exact statement over `Q` by a multimodular
  certificate (session 44 and, at the corrected size 661, session 49) that does
  not depend on a lucky seed at all.  A seed chosen to manufacture the drop
  would have to survive both primes and the multimodular certificate, which it
  cannot.  (iii) Session 49 re-read the whole `(4,6)` ladder at a **fresh** seed
  (`20260905`, fixed in `results/PREREG_s49.md` and committed *before* the run,
  `d878b4f`) and reproduced `660` and `1146` exactly — an independent seed
  confirming the numbers.
- **What session 49 changes going forward.**  `results/PREREG_s49.md` fixes the
  concrete seed (`20260905`) and every box and prime in a committed artifact
  **before** any run (`d878b4f`), closing the gap for this session and setting
  the pattern: the seed, not only the protocol, is banked ahead.  Future
  sessions should commit the seed value in the pre-registration, not in the
  results commit.

## Seeds and introducing commits, for the record

| use | seed | drawn in | first in git |
|---|---|---|---|
| s44 six-row ladder / anchors / sweep / `r=4` | `20260903` | `analysis/wk9_s44_*.py` | `e50575a` (with results) |
| s44 `d=7` size-666 certificate | `20260903` (+`5150081·t`) | `analysis/wk9_s44_certify.py` | `e50575a` (with results) |
| s48 `(5,7)` control / determinantal | `70000+sd` / `80000+sd` | `analysis/wk9_s48_ladder57.py` | `ddb76cd` (with results) |
| s49 `(4,6)` ladder recompute | `20260905` | `analysis/wk9_s49_cap.py` | `d878b4f` (**before** the run, in PREREG) |
| s49 `d=7` size-661 certificate | `20260905` (+`7000+5150081·t`) | `analysis/wk9_s49_cap.py` | `d878b4f` (**before** the run, in PREREG) |
| s49 degeneracy test set | `20260905+4900` | `tools/verify/testset/make_testset.py` | this session (committed set) |
