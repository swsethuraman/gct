# Session 32 (2026-09-01) — closing the classification joint

Branch `s32-singspaces`, fresh clone of public `origin/main`.
**Tip at clone `13fb170`; ancestry check PASSED** (`1203fe4` is an ancestor;
`e514b3d`, `ffe50b3`, `13fb170` and the rest are the expected commits above it).
Container only; rule 9 respected.  `paper/det3-conductor.tex`,
`PROJECT_NOTES.md`, `docs/boundary_deficit.html` untouched, and the
integrator's `analysis/l5contain.py` and `docs/l5_containment.md` untouched —
I wrote my own and report against theirs.
Calibration (`analysis/wk6_s26_regress.py`) passed first: all checks, 18 s.

**Flags for the integrator.**
1. `s28-d5` is merged (`e514b3d`) — good, that fixes what session 31 flagged.
2. **`s31-quiver` is still NOT merged.**  `docs/quiver_route.md`,
   `docs/session_31.md`, `results/PREREG_s31.md`, `analysis/wk8_s31_si.py` are
   absent from `main` and exist only in the delivered bundle.  Session 31's
   result — the quiver dictionary is exact,
   `dim SI^tau_{(d,d)} = sum m_det(lam) dim S_lam(C^5)`, and the dimension
   crossover lands near 145, far above the discriminant's 80, so no counting
   route reaches `delta_0` — is therefore not in the repository.
3. `docs/l5_containment.md` §4 needs one word changed: its soft joint is
   **false as stated**, but its table and its conclusion are both correct.  I
   have not edited it; §5 of this record says exactly what to change.

Deliverables: `results/PREREG_s32.md`, `docs/singular_spaces.md`, this record,
`analysis/wk8_s32_branches.py`, `analysis/wk8_s32_checks.py`.

---

## 1. Headline

**The joint was false and the conclusion is true.**

The integrator's soft joint — *is every 4-dimensional singular subspace of
`M_4(C)` contained in a compression space?* — is **no**.  The `3x3` skew matrix
padded by a scalar, `E_1 = { diag(N(x), w) }`, is a 4-dimensional singular
subspace lying in no compression space of any type.  So the branch list in
`docs/l5_containment.md` was incomplete, and the "modulo a classification"
caveat was pointing at a real hole.

I classified the missing spaces completely and proved the classification
(`docs/singular_spaces.md` §2, Theorem 4): up to transpose, every such space has
kernel vector `u(y) = L y` and satisfies `M_0(y) L t = phi(y ^ t)` for a linear
`phi : Lambda^2 C^4 -> C^4` killing `C^4 ^ ker L`.  That gives exactly four
strata indexed by `k = rank L`; `k = 1` and `k = 2` **are** the common-kernel and
`2 -> 1` compression spaces, and `k = 3, 4` are the exceptional ones.

Measured: **27** and **25**, against the compression branches' 31.

> **Maximum 31 of 35 over a now-complete list.  Containment fails, and it is a
> theorem.**  The generic reducible quinary quartic `ell . c` is not a `4x4`
> determinant of linear forms.

No reversal.  The integrator's numbers, the 4-dimensional shortfall, and every
consequence drawn from them stand exactly as written.

## 2. Prediction ledger

| # | pre-registered | outcome |
|---|---|---|
| P1 | verdict: exceptional branch exists **and** the literature covers the classification | **HIT.** `E_1` was exhibited in the pre-registration itself; Atkinson (1983), as restated by Huang–Landsberg (2026), classifies bounded rank `<= 3` and its `r = 3` primitive example is exactly the `k = 4` stratum. F1 not fired. |
| P2 | exceptional rank `< 35`, in `[20,27]`, best guess 26 | **HIT on the number, half-wrong on the reasoning.** Ranks 27 (`k=3`) and 25 (`k=4`), both in range. But my interval was derived from `E_1` alone, and `E_1` measures **22**; I had not seen that the exceptional stratum is a 60-parameter family containing `E_1`'s 32. The interval covered the truth by margin, not by understanding. F2 (`>= 28`) not fired; F3 (`= 35`, the reversal) not fired. |
| P3 | own implementation reproduces `29, 31, 31, 29` and `29 = dim D_5^{det_3}` | **HIT**, and better than predicted: the `29` coincidence was upgraded to an identity of polynomials, not just equal dimensions. F4 not fired. |
| P4 | max over all branches stays 31 | **HIT.** F5 not fired. |
| P5 | task E: stacking survives exactly while every `r`-ary cubic is `3x3`-determinantal, i.e. `r <= 4` | **HIT.** `dim D_r^{det_3} = 10, 20, 29, 38` against `10, 20, 35, 56`. F6 not fired. |

Five for five, and I do **not** read that as calibration improving after the
refutations of sessions 28 and 31.  The pre-registration here was written
*after* the decisive hand analysis — I found `E_1` and proved it lies in no
compression space before writing the file — so P1 and P2 were made from a
position sessions 28 and 31 did not have.  A prediction made after the hard
part is cheap.  The honest content of this ledger is P2's second half: the
number landed and the mechanism did not.

## 3. What was established

1. **Theorem 4** (`docs/singular_spaces.md` §2): the classification of
   4-dimensional singular subspaces of `M_4(C)` of generic rank 3, proved from
   scratch in about a page — the adjugate factors as `f u v^T`, transposing
   makes `deg u <= 1`, and `deg u = 1` forces an alternating form, hence `phi`.
2. **`E_1` is in no compression space** (elementary, four cases), and neither is
   the generic `k = 4` member (four cases, using `dim ker phi = 2`).
3. **The two exceptional ranks, 27 and 25**, exact over `Q` and modulo two
   primes, and certified against a spuriously low reading by Schwartz–Zippel at
   wide random points.
4. **Theorem 5**: the generic reducible quinary quartic is not a `4x4` linear
   determinant; the reachable locus of cubics has dimension 31 of 35.
   **Unconditional.**
5. **The `29` coincidence is an identity.**  The common-kernel branch cubic *is*
   `det_3` of an explicit `3x3` matrix of linear forms, verified as an equality
   of polynomials at three points — so `D_5^{det_3}` is not merely the same size
   as that branch's image, it *is* it.
6. **Task E**: stacking works iff `D_r^{det_{n-1}} = Sym^{n-1} C^r`, i.e. (at
   `n = 4`) iff `r <= 4`; and at `(4,5)` the failure is not repaired by any
   other representation.
7. The classification agrees exactly with Atkinson's, which is corroboration
   rather than a dependency.

## 4. The bug, because it is a new failure class

My first parametrisation of the strata normalised `L` to `[I_k | 0]`.  It gave

    rank L = 1 : 29     rank L = 2 : 27     rank L = 3 : 24     rank L = 4 : 25

and the `27` is wrong: the `rank L = 2` stratum **is** the `2 -> 1` compression
space, whose rank is 31.  Normalising `L` consumes the `GL_4` acting on the
coordinates `(s_2, ..., s_5)` — and that `GL_4` **moves the cubic**, so the
normalised slice sees a smaller image than the stratum does.  Restoring it (by
carrying a general substitution `y -> g y` as a parameter) gives
`29, 31, 27, 25`, and the deficits of the slice against the stratum are
`0, 4, 3, 0 = k(4-k)` — exactly the Grassmannian freedom the normalisation ate.
That identity is now a printed diagnostic in the script.

Two things worth recording.

- **The failure class is new to this programme.**  Sessions 28 and 31 both
  failed by *transferring an observation across regimes*.  This one is
  different: **quotienting by a group that acts non-trivially on the target**.
  A normalisation is free only when the group used to achieve it fixes what is
  being measured.  Here the right multiplication that normalises `im L` is free
  (it only rescales the determinant); the `y`-substitution that normalises `L`
  itself is not.
- **What caught it was a redundancy that was designed in.**  The `k = 1` and
  `k = 2` strata *had* to reproduce the compression ranks 29 and 31, because
  Theorem 4 says they are those compression spaces.  `k = 2` came out at 27 and
  the contradiction was immediate.  Without that overlap the wrong numbers 24
  and 25 would have been reported, would still have been below 35, and the
  headline would have been right for the wrong reason.  **Design the overlap in;
  it is cheaper than being right by luck.**

A smaller one: my first exact-rank routine was a fraction-free Bareiss
elimination that returned 34 where two primes agreed on 29.  Column skipping
breaks Bareiss's exact-division invariant.  I replaced it with plain `Fraction`
elimination rather than debug it — 35 columns do not need fraction-free
arithmetic — and every branch is now checked over `Q` and two primes.

## 5. What `docs/l5_containment.md` needs

One paragraph, §4.  Its soft joint is stated as *"provided every such space lies
in a compression space"*, and that is false.  The replacement:

> Modulo nothing.  Every 4-dimensional singular subspace of `M_4(C)` of generic
> rank 3 falls, up to transpose, into one of four strata indexed by the rank of
> the kernel map (`docs/singular_spaces.md`, Theorem 4); two of them are the
> compression spaces measured above and two are exceptional, with ranks 27 and
> 25.  The maximum over the complete list is 31.

Its table, its `29 = dim D_5^{det_3}` remark, its 4-dimensional shortfall, and
both consequences in §4 are unchanged and now unconditional.  I have not edited
the file (single-writer discipline); this is the diff to apply.

## 6. What to do next

1. **The subspace test, not the dimension test.**  `docs/l5_containment.md` §4
   ends by proposing: at one length-5 weight, compute `U_det` and `U_pad` as
   *subspaces* of the multiplicity space and ask whether they coincide, rather
   than comparing their dimensions.  With the containment now definitively dead,
   that is the only computation in view that can distinguish "the closures are
   different but multiplicities cannot see it" from "the method is simply
   blind".  It is the sharpest available statement about *why* the multiplicity
   method is failing, and it uses data already in hand.
2. **The 62 unmeasured cells at `delta = 6`** (s30) are genuinely open, as the
   integrator said — the foreclosure argument really is gone.
3. **Do not spend more on `delta_0`.**  Session 31's recommendation stands and
   this session reinforces it from a different direction: two independent
   routes (counting, and now containment) have each turned out to be answering
   a question adjacent to the one being asked.
4. If `(n, r) = (4, 6)` ever matters, the object needed is the classification of
   **5-dimensional** singular subspaces of `M_4(C)`.  That is a strictly harder
   classification and Huang–Landsberg 2026 is the place to start.

## 7. Assets

    analysis/wk8_s32_branches.py  the classification family, all eight branches,
                                  dual-number derivatives, exact-Q and two-prime
                                  ranks, the Grassmannian diagnostic, and the
                                  Schwartz-Zippel certification pass
    analysis/wk8_s32_checks.py    dim D_r^{det_3} from scratch; the common-kernel
                                  cubic AS a 3x3 determinant (polynomial
                                  identity); E_1's leading part factorised;
                                  bounded rank <= 2 excluded; task E's table
    docs/singular_spaces.md       the classification with proof, the literature
                                  with exact citations, the branch table, the
                                  theorem, task E, honest boundary
    results/PREREG_s32.md         pre-registration, with E_1 exhibited in it
