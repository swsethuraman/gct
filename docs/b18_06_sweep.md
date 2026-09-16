# B18-06 sweep — the nineteen untested degree-five cells

15 September 2026. Slot 06 follow-up, batch 18, worktree `work/batch15_workers/B15-06`.
Author: Claude (Opus 5). Written incrementally, one block per cell, as the runs happen.

**Provenance, recorded before any write:**

```
git rev-parse HEAD          8f7ab3bbc1f5352b2ec705894c56f69c93bc6c36
git rev-parse HEAD^{tree}   f0428d8181e067362b71afa663c4b574392777ff
git status --porcelain      only untracked B18 artifacts (b18_06_pilot.py, b18_06_report.md,
                            b18_06_review.md, results/b18_06/, results/logs/b18_06_*)
```

No other git command was run.

## 0. What this does

At `d = 5` there are 23 five-row cells, all with `a = 1`. Four are settled; the
other nineteen are untested. Because `a = 1`, `D > 0` would force `i_det >= 1`,
i.e. the unique highest-weight vector `h_lambda` would have to vanish on the
whole determinant closure. So **one exact nonzero value of `h_lambda` at one
actual determinant point closes the cell**. This document runs that test on all
nineteen, then the two further rungs on any cell that survives.

Ladder, per cell, stopping at the first rung that decides:

1. exact evaluation of `h_lambda` at integer determinant points — nonzero closes
   the cell (`m_det = 1 = a`, so `i_det = 0`, so `D <= 0`);
2. only if it survives: the symmetric rectangular Kronecker `s` — `s = 0`
   certifies `m_det = 0`;
3. only if it survives both: exact evaluation at an actual padding point —
   nonzero gives `m_pad >= 1 = a`, and with rung 2 that is a certified `D = 1`.

A cell passing 2 and 3 goes to slot 10's release gate and nothing else.

## 1. Method, and everything declared before the runs

### 1.1 The highest-weight vector, and why it is exact

Conventions are the preamble's: ordinary coefficients `c_alpha = [x^alpha] f`,
weights `alpha`, and `E_ij c_alpha = (alpha_i + 1) c_(alpha + e_i - e_j)` when
`alpha_j > 0`, extended as a derivation. `h_lambda` spans the common kernel of
the four simple raising operators on the weight-`lambda` space, of dimension `K`.

P1 obtained that kernel by compressed elimination, which needs `O(K^2)` storage
and lost rank in 6/6 cells. `K` here runs to 11640, where that method does not
fit the cap. This sweep uses a different construction:

- Build the weight-`lambda` space and, separately, each shifted weight space
  `lambda + e_i - e_j`. **A raising operator maps into a different weight
  space**; a prototype of mine that indexed its targets in the same space
  produced empty operators and a vacuous "all residues zero" pass. That error is
  what control (b) and the nonempty target dimensions in each certificate now
  guard against.
- Apply the Casimir projector `prod_mu (Omega - c_mu)` over `F_p`, where
  `Omega = sum_(i,j) E_ij E_ji` acts by `c_mu = sum_i mu_i(mu_i + 6 - 2i)` on
  `S_mu`, and `mu` runs over the dominant partitions of 20 with at most five
  rows that dominate `lambda`, excluding `lambda` itself and any `mu` with
  `c_mu = c_lambda`. Cost is a few sparse mat-vecs; memory is `O(K)`.
- Lift the projected vector to `Z` by CRT over 31-bit primes plus rational
  reconstruction, normalised at its first nonzero coordinate, and clear
  denominators to a primitive integer vector `W`.
- **Verify `W` exactly over `Z`**: all four simple raising operators must
  annihilate it, computed in integer arithmetic against the shifted weight
  spaces, whose dimensions are recorded in each certificate. This verification,
  not the projector, is the certificate. The projector is only a generator: if
  it returned something wrong, the exact check rejects it.

With `W` exact and `a = 1`, `W` spans `H_lambda`, so an exact nonzero integer
value of `W` at a determinant point proves `m_det >= 1` with no modular
inference anywhere in the chain.

`a` is **recomputed in-script** by the Weyl alternant
`a = sum_w sgn(w) dim M_(lambda + rho - w rho)` on exact weight multiplicities,
so the sweep does not depend on any census, mine or the integrator's.

### 1.2 Retry policy — declared before running anything

Rank loss reads as a smaller `m` and so a larger `i`, the direction that
manufactures false gaps. P1's pre-declared retry caught exactly that. Here:

- primes, in order: 2147483647, 2147483629, 2147483587, 2147483579, 2147483563,
  2147483549, 2147483543, 2147483497; seeds, in order: 7, 11, 13.
- For a seed, add primes one at a time. After each prime, attempt
  reconstruction and the exact verification. Success stops the ladder.
- `reconstruction_incomplete` (rational reconstruction not yet determined) or
  `exact_verification_failed`: add the next prime, up to 8.
- A zero projection or a vanishing pivot coordinate: abandon that seed, move to
  the next.
- All seeds exhausted: status `NOT_REACHED_no_exact_hwv`. That is a failure to
  compute, never an exclusion and never a survivor.
- Every attempt, including every failure, is recorded in the certificate under
  `lift_attempts`.
- If the in-script `a` is not 1, the cell is recorded and its inference is
  redone for that `a`; a single nonzero value would no longer close it.

### 1.3 Points, and what makes them valid

- **Determinant point**: `f = det(sum_k x_k A_k)`, integer `A_k`, entries in
  `[-5,5]`. It is used only if its 16×5 coefficient block has rank 5 over `Q`,
  which is exactly the condition for the 16 entry forms to be the first five
  columns of an invertible 16×16 substitution. So `f` is the five-variable
  restriction of an actual point of `GL16 · det4`.
- **Padding point**, the `F*` shape: `l(x) · per_3(sum_k x_k N_k)` with all ten
  linear forms nonzero, integer entries in `[-5,5]`. Any such 10×5 block
  completes to an invertible 16×16 substitution of independent `z·per_3`.
  Smoothness of the cubic factor is not needed for `m_pad >= 1`.
- Three determinant points and three padding points per cell.

### 1.4 Direction of inference, as instructed

- A determinant **nonzero** closes the cell. Used only that way.
- A determinant **zero at sampled points proves nothing**: recorded as
  `NOT_CLOSED_sampled_zero_only`, never as "survived" in an evidential sense.
- `s` bounds `m_det` above: `s = 0` certifies `m_det = 0`; `s >= 1` certifies
  nothing.
- A padding **nonzero** certifies `m_pad >= 1`. It is the only sampled result in
  this ladder that establishes something positive.

### 1.5 Controls that must be able to fail

Run before the sweep, as `controls`:

| id | control | required outcome |
|---|---|---|
| a | the exact `h_lambda` for the known cell `(12,2,2,2,2)` must be proportional to `det Hess_5(f)(e_1)` at three determinant points, with one constant ratio | pass |
| b | rebuild `h_lambda` with the **wrong** raising convention (`alpha_i` instead of `alpha_i + 1`, the factorial-normalised symbol) and verify it against the correct operators | **must be rejected** |
| c | corrupt one coordinate of the verified `W` | **must be rejected** |
| d | a rank-deficient 16×5 determinant point | **must be rejected** before use |
| e | the symmetric Kronecker routine on `(12,2,2,2,2)`, where the integrator computed `s = 8` | must return 8 |
| f | the Weyl alternant on `(14,4,2,2,2)` at `d = 6`, where `a = 2` | must return 2, not 1 |

Controls (b), (c), (d) can fail and would invalidate the sweep; (a), (e), (f)
check the machinery against values obtained by other people or other methods.

### 1.6 Cap

One process at a time, one BLAS thread, `analysis/b15_bound.py --seconds 60
--memory-mb 512`, one run per cell, 19 cells plus 2 known-outcome replays plus
one control run. **No heavy lease is active.** A cap hit is recorded as
NOT REACHED and the cell is priced from the measured cells, not estimated.

## 2. Controls — run before the sweep

`analysis/b18_06_sweep.py controls`, certificate
`results/b18_06_sweep/controls.json`, 3.7 s, exit 0. **All six passed.**

| id | control | outcome |
|---|---|---|
| a | `h_lambda` for `(12,2,2,2,2)` against `det Hess_5(f)(e_1)` at three determinant points | pass: ratio is exactly 6 at all three (e.g. `2351870305566390 = 6 x 391978384261065`) |
| b | wrong raising convention (`alpha_i` in place of `alpha_i + 1`) | rejected |
| c | one coordinate of the verified `W` corrupted | rejected, by nonzero exact raising residues |
| d | rank-deficient 16x5 determinant point | rejected, block rank 1 |
| e | symmetric Kronecker on `(12,2,2,2,2)` | returned `s = 8`, matching the integrator; also `g = 8`, transpose trace 8 |
| f | Weyl alternant on `(14,4,2,2,2)` at `d = 6` | returned `a = 2`, not 1 |

Honest detail on (b): the wrong convention was rejected **at the lift stage** —
no vector could be reconstructed at all — rather than by the residue check. So
(b) shows the wrong convention cannot masquerade as a result, while (c) is what
demonstrates the residue check itself rejecting a bad vector. Both must fail to
pass, and both did.

Control (a) is the one that is not self-referential: `det Hess_5(f)(e_1)` is
computed from the form directly, with no raising operator anywhere in it, and
`h_lambda` reproduces it up to one constant.

## 3. The sweep — all nineteen cells

`analysis/b18_06_sweep.py <id>`, SHA-256
`a75db90a572723886e3231cdb51477b7a48eb18eacb568323d2b525dea254e01`, unchanged
after the runs. One process per cell under the declared cap. Certificates
`results/b18_06_sweep/S01.json` ... `S19.json`, each holding the points used,
the exact integer values, the lift record and the shifted-weight dimensions.

`a` is the in-script Weyl alternant. "det" and "pad" are the exact integer
values of `h_lambda` at the **first** determinant and padding point.

| id | lambda | K | a | max abs coeff of W | nonzeros of W | det value (exact) | pad value (exact) | wall s |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| S01 | (11, 4, 2, 2, 1) | 705 | 1 | 48 | 109 | -13974598705210267 | 1855087339360 | 1.9 |
| S02 | (10, 5, 3, 1, 1) | 774 | 1 | 24 | 116 | -2989319953640328 | 0 | 2.0 |
| S03 | (10, 5, 2, 2, 1) | 1008 | 1 | 256 | 299 | -2971444470817191 | 160899796681600 | 2.5 |
| S04 | (8, 7, 3, 1, 1) | 1091 | 1 | 96 | 398 | 9274809748161774 | -157944977128448 | 2.5 |
| S05 | (9, 5, 4, 1, 1) | 1215 | 1 | 144 | 420 | 135653108939910 | -2363085060001680 | 2.7 |
| S06 | (9, 6, 2, 2, 1) | 1275 | 1 | 768 | 528 | 46416772160167680 | -2611604009949660 | 2.9 |
| S07 | (8, 5, 5, 1, 1) | 1610 | 1 | 384 | 758 | 46406135311166840 | 2137078268177168 | 3.2 |
| S08 | (10, 4, 2, 2, 2) | 1761 | 1 | 1536 | 579 | -23562172552577898 | -4466584937538660 | 3.9 |
| S09 | (9, 5, 3, 2, 1) | 1860 | 1 | 1152 | 985 | -481887838773963898 | 61802567469769750 | 4.0 |
| S10 | (9, 4, 4, 2, 1) | 2123 | 1 | 1152 | 1152 | -166825128188045696 | 729022173241700 | 4.9 |
| S11 | (8, 6, 3, 2, 1) | 2261 | 1 | 13824 | 1450 | -13491251500980644724 | 540763435182 | 4.5 |
| S12 | (8, 5, 4, 2, 1) | 2825 | 1 | 20736 | 2053 | -12772846894803968056 | 5861869491066912 | 5.3 |
| S13 | (8, 6, 2, 2, 2) | 2972 | 1 | 3456 | 1292 | -352808696348274603 | -30169810736001748 | 5.6 |
| S14 | (7, 6, 4, 2, 1) | 3260 | 1 | 5184 | 2255 | 1294910648297726706 | 210216214527284 | 5.7 |
| S15 | (7, 5, 4, 3, 1) | 4807 | 1 | 5184 | 3945 | 103980622526840690 | 1388964178855548 | 7.9 |
| S16 | (8, 4, 4, 2, 2) | 4988 | 1 | 20736 | 3287 | 16451915043752937828 | -47302361423188160 | 8.3 |
| S17 | (7, 4, 4, 4, 1) | 5490 | 1 | 3456 | 4076 | -3496636140174903008 | -9373945506050528 | 8.3 |
| S18 | (6, 6, 4, 2, 2) | 6869 | 1 | 27648 | 5170 | -1919964777903264789 | -285903336233194496 | 10.3 |
| S19 | (6, 4, 4, 4, 2) | 11640 | 1 | 82944 | 11640 | 33900369404217588856 | 161647243333770704 | 14.0 |

**Every cell closed at rung 1, at its first determinant point.** No cell reached
rung 2, so no symmetric Kronecker `s` was computed in the sweep; the routine was
exercised only in control (e).

Uniformly across all nineteen:

- `a = 1` by the in-script Weyl alternant, agreeing with the census in all 19
  cells (and with the integrator's independent recomputation where they overlap);
- the exact integer `h_lambda` was reconstructed from a **single** 31-bit prime,
  with coefficients at most 82944 in absolute value, and **verified exactly over
  `Z`**: all four simple raising operators annihilate it, against shifted weight
  spaces of dimension 354 to 11640 (recorded per cell), so the verification is
  not vacuous;
- `m_det >= 1` and `m_pad >= 1` by exact nonzero integer values at actual
  substitutions; with `a = 1` this gives `m_det = m_pad = 1`, hence
  `i_det = i_pad = 0` and **`D = 0` exactly**, not merely `D <= 0`;
- no retry beyond the first prime and first seed was needed; `lift_attempts` is
  empty in every certificate.

One recorded sampled zero, which is exactly the situation the direction rule is
about: in S02 the **first** padding point gave the value 0, because its linear
factor `l = (0,-1,-3,2,-3)` vanishes at `e_1`. The second and third padding
points gave `29176740495576` and `55944040916860`. The zero established nothing;
the nonzeros established `m_pad >= 1`.

## 4. Cross-method control

The sweep's Casimir projector and P1's compressed elimination are independent
code paths. `analysis/b18_06_cross.py`, SHA-256
`350c6aca94992b788b89f278ae3278b6bd46e9c78f573d25a60e51458bb879c5`:

| cell | K | elimination nullity, first sketch | after declared retry | proportional to the exact `W` mod p |
|---|---:|---:|---:|---|
| S01 | 705 | 56 | 1 | yes |
| S12 | 2825 | 197 | 1 | yes |

The elimination again lost rank on the first sketch, in both cells, as in all six
P1 cells; the pre-declared retry recovered `nullity = 1` and the resulting kernel
is a scalar multiple of the sweep's exactly verified `W`. Two methods, one answer.

This also shows why the method was changed. At `K = 2825` the elimination path
peaked at **426 MiB**; the projector at `K = 11640`, four times larger, peaked at
**80 MiB** and took 14.0 s. The largest cell was never near the cap.

## 5. The two known-outcome replays

| id | lambda | K | a | det value (exact) | P1 verdict | this sweep |
|---|---|---:|---:|---:|---|---|
| R01 | (9,7,2,1,1) | 621 | 1 | -564187728262832 | CLOSED (modular, P1 cell C1) | CLOSED, `D = 0` |
| R02 | (12,2,2,2,2) | 553 | 1 | 4756517324094345 | CLOSED (modular, P1 cell C0) plus Prop. 4.1 | CLOSED, `D = 0` |

Both reproduce P1's verdicts by an independent construction and in exact
integer arithmetic rather than modulo `p`, and R02 additionally matches the
Hessian covariant of Proposition 4.1 (control (a)).

## 6. Verdict — the degree-five family is retired

**All 23 five-row cells at `d = 5` are now settled, and every one has `D <= 0`.**

| cells | how |
|---|---|
| 1 — `(4,4,4,4,4)` | excluded by B18-01's null-cone argument (ADOPTED; not rechecked here) |
| 1 — `(12,2,2,2,2)` | Hessian covariant, Prop. 4.1 of `b18_06_report.md`; replayed here as R02 |
| 2 — `(9,7,2,1,1)`, `(7,7,4,1,1)` | P1, first determinant point; `(9,7,2,1,1)` replayed here as R01 |
| **19** | **this sweep, each at its first determinant point** |

The 19 swept cells plus the 4 settled ones are **exactly** the 23 five-row
`d = 5` cells of the census — checked here by set comparison against
`toy_character_screen_d5_d6.json`: no cell missing, none counted twice. In 22 of
the 23 the result is the sharp `D = 0`, since `m_pad = 1` was certified too; in
`(4,4,4,4,4)` I inherit B18-01's exclusion and claim nothing further.

**What this retires.** The natural close-out the review asked for: no `d = 5`
five-row cell has `m_det = 0`, so none can carry a determinant equation, and by
Lemma 2.1 none can have `D > 0`. The Kronecker rung, which was the only route
that could have come back positive, is now irrelevant **at this degree**: it was
never reached, because rung 1 decided every cell.

**What it does not retire.** Nothing beyond `d = 5`. The family closed here is
one degree, not the five-row regime. `d = 6` has 105 five-row cells and `d = 7`
more; only 3 of those are settled (two in P1, plus `(16,2^4)` and `(20,2^4)` in
the Prop. 4.1 family). The evidence now stands at **34 of 34 cells closed at the
first determinant point** — 19 here, 6 in P1, 9 in B15-02 — but that is still a
prior, not a theorem, and it says nothing about any untested cell. The honest
statement is the one the review made: a determinant nonzero can only subtract.

## 7. Claim ledger

| # | claim | label |
|---|---|---|
| 1 | Provenance `8f7ab3bb…` / `f0428d81…`; `git status --porcelain` shows only untracked B18 artifacts | MEASURED |
| 2 | For each of the 19 cells, an explicit primitive integer `h_lambda`, annihilated by all four simple raising operators, verified in exact integer arithmetic against shifted weight spaces of dimension 354–11640 | PROVED (certificates hold the vectors' size data; the vectors themselves are reproducible from the recorded seed and prime) |
| 3 | `a = 1` in all 19 cells, by the in-script Weyl alternant, independent of any census | PROVED |
| 4 | `m_det = 1` and `m_pad = 1`, hence `i_det = i_pad = 0` and `D = 0`, in all 19 cells | PROVED (exact nonzero integer values at substitutions verified to be restrictions of invertible ones) |
| 5 | The 19 plus the 4 settled cells are exactly the 23 five-row `d = 5` cells | MEASURED (set comparison against the census) |
| 6 | The degree-five five-row family is retired: no cell there has `D > 0` | PROVED, modulo B18-01's null-cone exclusion of `(4^5)`, which is ADOPTED |
| 7 | All six controls passed, three of them rejections that had to be able to fail | MEASURED |
| 8 | Projector and elimination agree (S01, S12); elimination lost rank on the first sketch in both, recovered by the declared retry | MEASURED; recorded defect, as in P1 |
| 9 | Any statement about five-row cells at `d >= 6` | NOT REACHED |
| 10 | Any positive gap anywhere | NOT REACHED |

**Honest negatives.** No cell reached rung 2 or rung 3, so this sweep says
nothing about the symmetric Kronecker route beyond control (e). The sweep tests
`m_det >= 1`; it cannot and does not bound `m_det` above. `(4,4,4,4,4)` is
inherited, not rechecked. Nothing here touches six-to-ten-row cells or any
degree above five.

## 8. What I would do next, and its price

The natural continuation is `d = 6`: 105 five-row cells, of which 3 are settled.
Measured cost here is 1.9 s at `K = 705` and 14.0 s at `K = 11640`, with peak
memory 80 MiB at the largest; the run time grew sublinearly in `K` over that range (a factor 7.4 across a factor 16.5 in `K`), and memory stayed far below the cap throughout. `d = 6` weight spaces are
larger — `(14,4,2,2,2)` at `d = 6` has `K = 2337`, and the balanced shapes will
be well above `K = 11640` — so a `d = 6` sweep needs its own `K` census first.
I am **not** requesting it: it is another degree of the same negative, and the
programme's binding constraint is unchanged — no determinant equation of length
5–8 is known in any degree, and no mechanism in the tree can produce one
(Lemmas 3.1–3.2 of `b18_06_report.md`).

The one test that could still change the picture is unchanged from that report:
**a certified determinant equation of length 5–8, in any degree**. With one in
hand, the cell it lives in is decided by the machinery now built and measured
here, in seconds.

## 9. Resources and files

- 21 cell runs (S01–S19, R01, R02) plus 1 control run plus 2 cross-method runs, each
  `.venv/python.exe -B analysis/b15_bound.py --slot 06 --name b18_06_… --seconds 60
  --memory-mb 512`, one process, one BLAS thread. Total wall 123.5 s across all 24 runs.
  Peak job memory: 80 MiB (sweep, `K = 11640`); 426 MiB (cross-method at
  `K = 2825`, the elimination path). No cap was hit; every exit code 0.
- Written: `docs/b18_06_sweep.md`, `analysis/b18_06_sweep.py`,
  `analysis/b18_06_cross.py`, `results/b18_06_sweep/` (controls, S01–S19, R01,
  R02, cross_S01, cross_S12), receipts `results/logs/b18_06_sweep_*` and
  `results/logs/b18_06_cross_*`. No historical artifact was modified; the B18
  report, its pilot and its certificates are untouched. No git command other
  than the two `rev-parse` calls and one `git status --porcelain`.
