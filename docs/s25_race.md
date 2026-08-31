# Session brief — the ambient cap, applied backwards and forwards

**Branch `s25-race`, cloned fresh from public `origin/main`.**
Successor to sessions 24 and 24b. Pure easy-side computation: characters,
Kronecker coefficients, plethysm. **No engine, no checkpoints, no closure
geometry.** Expect hours, not days.

---

## 0. Standing orders

- You do **not** own `Projects\gct` (rule 9). Read nothing from it, write
  nothing to it. Work in the container on a fresh clone of the public repo.
- Record the tip at clone time and report it in your session record. `main`
  **should** be at `a3df8ba` ("Add the ambient screen, its verification, and
  the two session briefs"), which sits on top of `c9240f3` (the easy counts)
  and `ad9502f` (the abstract cut). If it is not, say so loudly at the top of
  your record — that is a rollback alarm, not a detail — and branch from
  whatever `origin/main` actually is.
- Write **only new files** where you possibly can, so the merge is clean.
- Do **not** append to `PROJECT_NOTES.md` or `docs/boundary_deficit.html`.
- Push to `origin` will likely be refused by the session's git proxy
  (`swsethuraman/gct` not in the authorised set). If so, deliver a git bundle.
- The ambient screen already lives at `scripts/ambient_screen.py` and passes
  its own `--selftest` (eleven checks against the record). **Derive your own
  routines first** — the programme's habit is independent rederivation — then
  use the screen as a cross-check, never as an input. If your numbers disagree
  with it, that is a finding: report it before proceeding.

---

## 1. What changed, and why this session exists

A critique session found a cap the programme had not been applying, and it has
been verified independently:

> Both `C[closure of det]` and `C[closure of per]` are quotients of the **same
> ambient** `Sym^delta(Sym^n C^{n^2})`. So with `a(lam,delta)` the multiplicity
> of `S_lam` in that ambient,
>
>     mult_det <= a ,  mult_per <= a ,  hence  D = mult_per - mult_det <= a .

Consequences the programme must absorb:

- Where `a = 0`, both closure counts are forced to zero, so `def = m` on both
  sides **identically** and `Def = P` is an algebraic identity. Any `D = 0`
  measured there is information-free.
- **`a((2,2,2),2) = 0`** — because `Sym^2(Sym^3) = s_(6) + s_(4,2)`. Session
  24's flagship "uncanny cancellation" (`P = Def = 3`) at that weight is a
  tautology.
- Where `a = 1`, both counts are 0 or 1, so any obstruction is an *occurrence*
  obstruction — closed by Bürgisser–Ikenmeyer–Panova. **Multiplicity
  obstructions require `a >= 2`.**

Verified stratification for the `det_3` ambient, `lam` with at most 9 rows:

| delta | weights | a=0 | a=1 | a>=2 |
|---|---|---|---|---|
| 2 | 11 | 9 | 2 | 0 |
| 3 | 30 | 25 | 5 | 0 |
| 4 | 73 | 61 | 12 | 0 |
| 5 | 157 | 129 | 27 | **1 — (9,4,2)** |
| 6 | 318 | 251 | 55 | 12 |
| 7 | 598 | 437 | 111 | 50 |

---

## 2. The two questions

### A. The retroactive audit — how much of the corpus was ever informative?

Recompute `a(lam,delta)` for every cell already banked: the **1292 favourable
World A cells** from session 24 (`docs/obstruction_power.md`), and the
determinant/permanent tables at `n <= 5` (`docs/easy_counts.md`). Partition
session 24's **742 zeros** into

- **forced** — `a = 0`, `D = 0` was arithmetic; and
- **genuine** — `a >= 1` and the two closure counts really were equal.

World A's ambient is `Sym^delta(Sym^4 C^2)`; there
`a((4d-b,b),d) = N(b) - N(b-1)` with `N` the Gaussian binomial (partitions in a
`delta x 4` box), so this costs seconds.

**Also audit the paper.** At `delta = 2` the determinant is supported on
`(6), (4,2), (2,2,2)` with `a = 1, 1, 0`, so `def((2,2,2),2) = 1` — the base
point of the flagship conductor result — is ambient arithmetic, not boundary
geometry. Report, for `delta = 2,3,4`, how much of `def_det` is forced. Note
for the record: **the paper contains no deficit measurement at any weight with
`a >= 2`**, because `a >= 2` first occurs at `delta = 5`.

### B. The race — can the cap ever be beaten?

An obstruction comes **free** at any weight with `m_det < a`: then
`mult_det <= m_det < a` while `mult_per` can reach `a`, and no deficit has to do
any work at all.

Measured through `delta = 7` at `n = 3`: **63 live weights, zero with
`m_det < a`.** `m_det >= a` every time.

But the two sides move oppositely in `n`. Rectangular Kronecker coefficients get
sparser (the mean of `m_det` over its own support is exactly **1.00** at
`n = 2,3,4,5`); ambient plethysms in `n^2` variables get richer. **Run the race
directly for `n = 3, 4, 5` and report the ratio.** Both sides are easy counts.
Note `a(lam,delta)` is the same for determinant and permanent at fixed `n` —
padding changes the point, not the ambient — so this question is
padding-independent.

### C. If time remains: the padded easy count

Every `m_per` number in the corpus is **unpadded**, and unpadded is decided by
dimension: `dim closure(per_3) = 81-4 = 77 > 65 = 81-16 = dim closure(det_3)`,
so a 77-dimensional variety cannot sit in a 65-dimensional one and
`per_3 not in closure(det_3)` needs no invariant at all. The real comparison is
`n = 4, m = 3`. Session 24b already has `perms_perpad` / `ok_perpad`; the
margin-pruned power-sum route in `analysis/wk5_easycount.py` runs at `n = 5`
unchanged. It is one substitution.

---

## 3. Pre-registration — commit before computing

Write `results/PREREG_s25.md` and **commit it before any computation**, with:

1. Your predicted forced-fraction of the 742.
2. Your predicted direction for `m_det / a` in `n`, with a falsifier.
3. Whether you expect any weight with `m_det < a` at `n = 4` or `5`, and where.

The integrator's own priors, for you to agree with or beat — these are **not**
your pre-registration:

- Forced fraction of the 742: **under 90%**, probably 40–75%. World A's
  ambient is rich (only 12.2% of its weights have `a = 0` for `delta <= 14`,
  and 61% have `a >= 2`), but `a = 0` *guarantees* `D = 0`, so a=0 cells are
  over-represented among the zeros.
- `m_det / a` **falls** with `n`. Moderate confidence only.

---

## 4. Calibration — reproduce these before trusting anything new

Derive your own routines; these are checks, not inputs.

    Sym^2(Sym^3) = s_(6) + s_(4,2)          so a((2,2,2),2) = 0
    delta=4 split 61 / 12 ; delta=5 split 156 / 1 ; (9,4,2) the unique a>=2
    g((9,4,2), 5^3, 5^3) = 3
    m_det sums   3, 11, 43   at delta = 2,3,4   (n=3)
    m_det supports 3, 10, 34 at delta = 2,3,4   (n=3)
    m_det row at delta=2 : (6):1, (4,2):1, (2,2,2):1
    m_per((2,2,2),3,2) = 4   [unpadded]
    World A, delta <= 14 : a=0 in 27 of 221 ; a>=2 in 134

A usable symmetric-Kronecker form for `m_det`, verified against all of the
above — check it, do not assume it:

    m_det(lam) = (1/2) sum_rho (chi^lam(rho)/z_rho)
                   [ chi^rect(rho)^2 + chi^rect(tau(rho)) ],
    rect = (delta^n),  tau(rho) halves each even part into two equal parts.

---

## 5. Kill criteria — state the outcome plainly either way

- **If >= 90% of the 742 are forced**: retire the saturation-law hypothesis
  outright and strike it from the open problems. It was an artifact of the
  ambient plethysm and there is no law to find.
- **If `m_det / a` rises through `n = 5`**: the multiplicity route is
  structurally capped from both ends. That is a **no-go theorem**, not a
  failure to find something, and it should be written up as one.
- **If any weight with `m_det < a` appears**: stop and report it immediately.
  That is the single most valuable object the programme could produce.

---

## 6. Deliverables

    results/PREREG_s25.md        pre-registration, committed FIRST
    docs/ambient_audit.md        the retroactive audit: forced vs genuine
    docs/race.md                 m_det vs a as a function of n
    docs/session_25.md           session record, prediction ledger, honest boundary
    analysis/wk6_s25_*.py        the routines

Every number twice, by independent routes, in the programme's usual style.
Report refuted predictions as refuted and keep them.
