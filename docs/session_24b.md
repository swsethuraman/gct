# Session 24b — the two cheap steps

Branch `s24-screen`.  2026-08-31.  Cloud container, fresh clone of the public
GitHub repo.  Per the changed record-keeping instruction, nothing was appended
to `PROJECT_NOTES.md` or `docs/boundary_deficit.html`.

Deliverables: `results/PREREG_s24b.md` (commit `aa932cc`, before any
computation), `docs/screen_results.md`, this file.

## 0. SYNC ALARM — read first

The session brief states that session 24's branch is merged and that
`main` contains commit `99b0c7b`.  **It does not.**  At clone time:

    origin/main            = 5cdc29c  "Merge s22-chi: the totals law is a theorem"
    git cat-file -t 99b0c7b -> fatal: Not a valid object name
    docs/obstruction_power.md, docs/session_24.md,
    results/PREREG_s24.md, analysis/wk5_s24_*.py   -- all ABSENT

Session 24's work is not on GitHub.  It may have been merged into the laptop's
`work/` clone without being pushed; it may not have been merged at all.  Under
rules 9 and 10 this is a rollback alarm, not a detail, so:

* this session branched from `origin/main` and wrote **only new files**, so
  nothing here conflicts when the real merge lands;
* session 24's results are cited as established-but-unmerged and were **not**
  re-derived and re-presented as new;
* the session-24 bundle was re-delivered alongside this one.

Someone should confirm where session 24's commits actually are before the
paper cites them.

## 1. What was asked and what came back

Asked: run the two steps session 24 recommended — the Peter–Weyl pre-screen
for `per^pad` against `det`, and the permanent's deficit at `n = m = 3`.

Came back, in one line each:

* **The screen fails everywhere.**  Exhaustively over six `(n,m,delta)` cases,
  every *live* weight (one where an obstruction is possible at all) has
  `m_{per^pad} > m_det`, i.e. `P > 0`.  No obstruction in range can be
  deficit-driven.  **The line is closed in accessible range.**
* **The one formal pass is vacuous**: `lam = (n)` at `delta = 1`, where both
  closures span the irreducible ambient, `mult = 1` and `def = 0` on both
  sides, and `D = 0` identically.
* **The first permanent deficit is 4**: `def_{per_3}((2,2,2),2) = 4` against
  the determinant's 1, computed two ways.  The deficit difference there
  exactly cancels the Peter–Weyl difference (`Def = P = 3`, `D = 0`) — the
  same saturation-at-zero session 24 measured 742 times in World A.
* **A calibration that doubles as a result**: this pipeline reproduces the
  paper's determinant total-deficit sequence `1, 6, 31` at `delta = 2,3,4`
  from a completely independent route (Schur–Weyl + Kronecker, no engine).
* **A correction to the paper**: `dim Stab(det_n)` is `2n^2 − 2`, not
  `2n^2 − 1`.  §4 of `paper/det3-conductor.tex` and the session-24 brief say
  17 (and 31 for `n = 4`); the correct values for the *vector* stabiliser,
  which is what Peter–Weyl requires, are 16 and 30.  17 is the dimension of
  the stabiliser of the *point* `[det_3]`.
* **A free statement about the permanent, from BIP**: at every weight where
  `m_det(lam) = 0` — 14 of the 19 live weights at `(n,m,delta) = (4,3,2)` —
  Bürgisser–Ikenmeyer–Panova's theorem forces
  `def_{per^pad}(lam) = m_{per^pad}(lam)`, a *full* deficit.

## 2. Pre-registration outcomes

| | prediction | outcome |
|---|---|---|
| E1 | `m_{per_3}((2,2,2)) > 1`; predicted value **2** | inequality **CONFIRMED**; point value **REFUTED** — it is **4** |
| E2 | no weight passes the screen at `n = m = 3` | **CONFIRMED**, `delta <= 4`, exhaustive |
| E3 | the padded screen passes broadly | **REFUTED** — it passes nowhere; see §4 for why my reasoning was wrong |
| E4 | hence every per/det obstruction must be deficit-driven | **REFUTED** with E3; the opposite holds |
| E5 | `m_{per^pad}(lam) = 0` for `ell(lam) > m^2+1` | **CONFIRMED**, and upgraded from assumption to a proved lemma |
| E6 | calibrations (a) `m_det_3` on `lam ⊢ 6`, (b) `def=1`, (c) `SL_9` census | **ALL CONFIRMED**; plus the `delta = 3,4` totals 6 and 31 |
| E7 | verdict: "live, for an uncomfortable reason" | **REFUTED** — the verdict is the opposite: closed, and session 24's recommendation is strengthened |

Three clean refutations (E1's point value, E3/E4, E7), all kept.  E7 is the one
that matters: I pre-registered that I expected to have to reverse session 24's
recommendation, and the computation said no.

## 3. Verification — every number twice

| quantity | route 1 | route 2 | external check |
|---|---|---|---|
| `chi^lam(rho)` | Murnaghan–Nakayama with memoisation | `sum_lam chi^lam(1^N)^2 = N!` for `N <= 7` | — |
| `Sym^delta(Sym^3)` plethysm | power-sum plethysm → Schur | — | `Sym^2(Sym^3) = S_(6)+S_(4,2)` (paper Prop. 4.15); `SL_9` census 0,0,0 at `delta = 3,6,9` (session 21) |
| `m_det_3(lam)` | Kronecker + symmetric correction | — | **paper**: `delta=2` row `(0,0,1)`, `def((2,2,2),2)=1`, totals **1, 6, 31** at `delta = 2,3,4` |
| `m_{per_3}(lam)` | Jacobi–Trudi coefficient extraction | Schur–Weyl power-sum average | agree on every spot-checked weight at each degree |
| `m_{per^pad}(lam)` | same two routes | same | row bound proved, not assumed |
| screen | brute force over all `lam` | optimised: enumerate `supp(m_det)` first | identical live/pass counts where both were run |

Structural gates: `def >= 0` everywhere; `mult <= min(m, ambient)`; and the
`delta = 1` sanity that both closures span an irreducible ambient.

## 4. The instructive error

E3 predicted the screen would pass, on the grounds that `H_{per^pad}` has
dimension 101 inside `GL_16` against `dim H_{det_4} = 30`, so the padded
permanent's Peter–Weyl count should be the smaller one.  That is wrong, and the
reason is worth carrying forward:

> 96 of those 101 dimensions — all of `GL(Z)` and the whole `Hom` block — do
> nothing but cut `S_lam(C^16)` down to `S_lam(C^10)`.  After the reduction the
> **effective** group is only 5-dimensional.  The real comparison is a
> *reductive* group of dimension `2n^2−2` on `C^{n^2}`, whose invariants are
> sparse rectangular Kronecker coefficients, against a *5-dimensional* group on
> `C^10`, whose invariants are broad monomial counts.

Raw stabiliser dimension inside `GL_{n^2}` is the wrong statistic.  Session 24
made the mirror-image mistake in the other direction, reading `def ~ 1/|H|` off
World A and expecting it to transfer.  Both times the fix was the same: reduce
to the effective group first, then compare.

## 5. Files added

    results/PREREG_s24b.md          pre-registration (committed first)
    docs/screen_results.md          the deliverable: what the screen covered,
                                    what it returned, exhaustive ranges, verdict
    docs/session_24b.md             this record
    analysis/wk5_s24b_sf.py         partitions, Murnaghan-Nakayama, Kronecker,
                                    symmetric Kronecker (m_det), plethysm,
                                    monomial-stabiliser invariants
    analysis/wk5_s24b_per.py        per_3 and padded-per_3 stabilisers, both routes
    analysis/wk5_s24b_step1.py      the screen, brute force over all lam
    analysis/wk5_s24b_screen2.py    the screen, optimised (det support first)
    analysis/wk5_s24b_step2.py      n = m = 3 deficit rows
    analysis/wk5_s24b_cross.py      crossover probe at det-favourable weights

Pure Python, exact integers and `Fraction`, no engine, no checkpoints, ~2 hours
wall clock — about four orders of magnitude cheaper than the `n = 4` grind the
screen was run to avoid.

## 6. What a successor should do next

1. **Push the crossover probe.**  The only route by which the line reopens is
   `m_det` overtaking `m_{per^pad}` at larger `delta`.  The probe at the
   determinant-favourable weights (nearest the rectangle `(delta^n)`) shows the
   margin growing, not shrinking, through the range reached.  Extending it is
   cheap per weight and is the single highest-value follow-up.
2. **Correct `2n^2 − 1` to `2n^2 − 2`** in §4 of the paper and anywhere the
   brief's `17 → 31` is quoted.
3. **Record `def_{per_3}((2,2,2),2) = 4`** beside the determinant's 1.  It is
   the first permanent deficit and it cost seconds.
4. **Do not start `n = 4` for separation purposes.**  Even if the crossover
   existed, `n = 4` computes `def_det` alone, and the separating quantity is a
   difference of deficits whose permanent half would still be missing.
5. **Resolve the sync alarm in §0** before the paper cites session 24.

## 7. Delivery

Push to `origin` was attempted.  The branch is `s24-screen`; if the git proxy
refuses, it is delivered as a git bundle, as sessions 21 and 24 were.
