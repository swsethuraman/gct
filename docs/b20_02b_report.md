# B20-02b — The sixteen-variable `D_8`, blockwise, as priced

17 September 2026. Bounded follow-on to B20-02, same worktree `work/batch15_workers/B15-02`,
branch `b15-02-a1-probes`, HEAD `75ddb900a0b47b911c53f941885bac73b358eacb` (confirmed with
`git rev-parse HEAD` and `git status --porcelain` at 21:36:05Z before the first write; the only
untracked files are B20-02's outputs and the four B15-era receipts of 2026-09-13). Read-only
git; no commit, no push. Author: Claude (Fable 5.1). Everything here is **producer only** (G18).
Conventions are B20-02's (`docs/b20_02_report.md`, sha256 `15ef389b5eb84074…`, §1.2): `k` is
the internal grading, `K_j(k) = Lambda^j C^16 (x) S_{k-3j}`, `d_j^{(k)}` the Koszul differential,
`rho_j(k)` the generic maximum, `L` and `delta_0` unused.

## 0. Plain terms, and the verdict up front

B20-02 closed the higher Koszul differentials in five variables and priced the one open case
that its closure argument cannot reach: the second differential `D_8 = d_2^{(8)}` in sixteen
variables, where the corrigendum's C5 reversal (`rank d_2(pad) > rank d_2(det)`) is still
possible in principle. The user approved the priced blockwise plan. This session runs it and
reports the two exact ranks. *(The verdict is filled in §3–§4 after the run; nothing below §2
existed before the run.)*

## 1. Pre-registered expectations and transcription sentences (written before any run)

**The quantities.** `dim K_2(8) = C(16,2) . dim S_2 = 120 . 136 = 16320`; `dim K_3(8) = 560 . dim S_{-1} = 0`.
Hence `rho_2(8) = dim K_2(8) - dim K_3(8) + ... = 16320`: at a smooth quartic `d_2^{(8)}` is
injective. So `rank_Q d_2^{(8)}(F) = 16320 - dim H_2(F)_8` for every `F`, and the question is the
comparison of `dim H_2(det_4)_8` with `dim H_2(z per_3)_8`.

**Predicted values (my prediction, not a claim).** At `k = 7` the kernels were 16 (`det_4`) and
270 (`z per_3`) (P3, `results/b20_02/inputs/p3_koszul2_exact.json`). I predict both kernels
grow with `k`, the padding one faster, so that

    rank(det_4) = 16320 - (a few hundred)  >  rank(z per_3) = 16320 - (a few thousand),

i.e. **no reversal**, with both ranks deficient below `rho_2(8) = 16320`. I have no derivation
of either number; the values will be whatever the blocks sum to.

**Internal check.** `rank d_1^{(5)}` (`M_5`, `2176 x 15504`): expected `2176 - 464 = 1712` at
`det_4` and `2176 - 932 = 1244` at `z per_3`, so that the quadratic-syzygy dimensions `464` and
`932` recorded in the corrigendum (via the launch prompt) are reproduced. These two numbers
are emitted by the script; if they differ, the block construction is wrong and the `D_8`
numbers are not reported as results.

**Transcription sentences, one of which will be copied into §4 verbatim:**

- If `rank(z per_3) > rank(det_4)`: *"At `N = 16`, `j = 2`, `k = 8`, the padded permanent has
  strictly larger second-differential rank than the determinant: a right-way statistic, the
  first on this record. It is a necessary-condition lead, not a gap, not a cell, and not an
  equation nonzero on padding. The follow-on it justifies is the `GL_16`-decomposition of the
  Fitting ideal of `(rank(det_4)+1)`-minors of `d_2^{(8)}`, priced in §4 and not run here."*
- If `rank(z per_3) <= rank(det_4)`: *"At `N = 16`, `j = 2`, `k = 8`, no reversal: the padded
  permanent's second-differential rank is at most the determinant's, so the ideal of
  `(rank(det_4)+1)`-minors of `d_2^{(8)}` lies in `I(Y_det) ∩ I(Y_pad)` by the `d_2`-version of
  Lemma 3.1–3.2, and the direction reversal holds one level down at `N = 16` exactly as at
  `N = 5`. Scope: `j = 2`, `k = 8` only; nothing is said about `k >= 9` or `j >= 3`."*
- If `rank(det_4) < rho_2(8) = 16320` (expected): *"`d_2^{(8)}(det_4)` is rank-deficient by
  `16320 - rank(det_4) = dim H_2(det_4)_8`, reported as data; the five-variable closure
  argument does not reach `N = 16` and this deficiency is consistent with that."*

## 2. Method, and the two lemmas

**Lemma 2.1 (grading invariance; B20-02 §8).** Let `T` be the torus acting on `C^16` by
weights `w(x_v)` for which `F` is a weight vector of weight `w(F)` (`det_4`: `Z^4 x Z^4`
row/column scalings, `w(x_{ij}) = (e_i, e_j)`, `w(F) = (1^4, 1^4)`; `z per_3`: `Z x Z^3 x Z^3 x Z^6`,
`w(z) = (1, 0, 0, 0)`, `w(y_{ab}) = (0, e_a, e_b, 0)`, `w(w_c) = (0, 0, 0, e_c)`, `w(F) = (1, 1^3, 1^3, 0^6)`).
Give the basis element `e_I (x) m` of `K_j` the weight `w(m) + sum_{v in I} (w(F) - w(x_v))`.
Then every `d_j` preserves weight: `f_v = d_v F` has weight `w(F) - w(x_v)`, so
`f_v m e_{I \ v}` has weight `w(m) + (w(F) - w(x_v)) + sum_{u in I \ v}(w(F) - w(x_u))`, the
weight of `e_I (x) m`. ∎

**Lemma 2.2 (block rank).** If rows and columns of a matrix are partitioned into weight
classes and every nonzero entry has row weight equal to column weight, the matrix is
block-diagonal after permuting rows and columns, and its rank is the sum of the ranks of the
blocks (row and column operations inside one block do not touch another; a block-diagonal
matrix in reduced form has rank equal to the number of pivots, which are counted blockwise). ∎

**Procedure.** For each point, enumerate the row basis of `K_2(8)` (pairs `v < u`, `m in S_2`)
and the column basis of `K_1(8)` (`v`, `m in S_5`), bucket both by weight, and for each weight
with both buckets nonempty build the block of `d_2^{(8)}` (`e_v ^ e_u (x) m -> f_v m e_u - f_u m e_v`)
as a `flint.fmpz_mat`, **transposed to tall form when wider than tall** (rank is invariant;
B20-02 §7.2 found `fmpz_mat.rank` on wide matrices memory-hungry), and take its exact rank
over `Q`. Any entry whose column weight differs from its row weight raises an error (a
runtime check of Lemma 2.1). A block with more than 250 000 entries would fall back to a
single-prime modular floor and be flagged; by the price (largest block `192 x 528 = 101 376`)
none should. The same for `M_5 = d_1^{(5)}` (rows `(v, m in S_2)`, columns `S_5`). Totals of
rows and columns over all buckets are printed and compared with `16320`, `248064`, `2176`,
`15504` (G16). JSON is rewritten every 200 blocks and at the end.

**Pilot 1 — `b20_02b_p1_d8_blockwise`**, both points, both matrices, one wrapped process
(`b15_bound.py --seconds 60 --memory-mb 512 --slot 02`, `PYTHONDONTWRITEBYTECODE=1`). Price
(B20-02 §8): 21.2 MB of blocks at `det_4`, 2.3 MB at `z per_3`, elimination bound
`1.2 x 10^8` operations; expected under 30 s and under 200 MiB. Input pinned: the price file
copied to `results/b20_02b/inputs/p3_price16_blocks.json` (sha256 `54838ca647397a33…`) and
the P3 certificate copied from `results/b20_02/inputs/` (sha256 `a83162c2941e1305…`), both
verified by the script. Pilots 2 and 3 are reserved (second point separately if needed;
retry).

*(End of the pre-registered part. Hash of this file at that point:
`c5c6511b78a081541c75f69c51b817eb13ec96c2bae2a8011b29a520b75e125a`; of the script
`analysis/b20_02b_d8_blockwise.py`: `ae03c0d17115ef1f…`; both at 21:37:49Z, before the launch
at 21:37:57Z. Neither file was edited afterwards except this report below this line.)*

## 3. Results (copied from `results/b20_02b/p1_d8_blockwise.json`, run `b20_02b_p1_d8_blockwise`)

One wrapped pilot held both points and both matrices: exit code 0, wall **3.35 s**, peak job
memory **92.2 MB**, checks passed **15/15** (emitted by the script). Every block was exact over
`Q`; no modular fallback was used; no grading violation occurred; the row and column totals
over the weight buckets equal the full dimensions in all four cases.

| point | matrix | rows | cols | blocks (all exact) | largest block | `rank_Q` | kernel = rows − rank | generic maximum |
|---|---|---|---|---|---|---|---|---|
| `det_4` | `M_5 = d_1^{(5)}` | 2176 | 15504 | 784 | `25 x 33` | **1712** | **464** | 2176 |
| `z per_3` | `M_5 = d_1^{(5)}` | 2176 | 15504 | 850 | `20 x 7` | **1244** | **932** | 2176 |
| `det_4` | `D_8 = d_2^{(8)}` | 16320 | 248064 | 2449 | `192 x 528` | **15660** | **660** | `rho_2(8) = 16320` |
| `z per_3` | `D_8 = d_2^{(8)}` | 16320 | 248064 | 6757 | `138 x 105` | **13490** | **2830** | `rho_2(8) = 16320` |

Internal check: the quadratic-syzygy dimensions `464` and `932` are reproduced exactly, so the
block construction of `d_1^{(5)}` is right, and `d_2^{(8)}` is built from the same partials,
weights and bucketing. Since `K_3(8) = 0`, `kernel(D_8) = dim H_2(F)_8`: **`dim H_2(det_4)_8 = 660`,
`dim H_2(z per_3)_8 = 2830`.** For comparison, at `k = 7` (P3) the kernels were 16 and 270.

The pre-registered prediction (§1) was: both deficient, padding more so, no reversal. That is
what the numbers say; the predicted orders of magnitude ("a few hundred" / "a few thousand")
happened to be right, which is not evidence of anything.

## 4. What this establishes, and what it does not

Transcribed from §1 (second and third sentences apply):

*"At `N = 16`, `j = 2`, `k = 8`, no reversal: the padded permanent's second-differential rank is
at most the determinant's, so the ideal of `(rank(det_4)+1)`-minors of `d_2^{(8)}` lies in
`I(Y_det) ∩ I(Y_pad)` by the `d_2`-version of Lemma 3.1–3.2, and the direction reversal holds
one level down at `N = 16` exactly as at `N = 5`. Scope: `j = 2`, `k = 8` only; nothing is said
about `k >= 9` or `j >= 3`."*

*"`d_2^{(8)}(det_4)` is rank-deficient by `16320 - rank(det_4) = dim H_2(det_4)_8`, reported as
data; the five-variable closure argument does not reach `N = 16` and this deficiency is
consistent with that."*

Precisely: `13490 < 15660 < 16320`. The ideal `J_8^{(2)}(Y_det)` of size-15661 minors of
`d_2^{(8)}` is nonzero as an ideal of the coefficient ring (the generic rank is 16320 > 15660)
and is contained in `I(Y_det) ∩ I(Y_pad)`: the `d_2`-version of the parent's Lemma 3.1
(rank constant on the orbit, semicontinuous on the closure; the matrix is a linear function
of `F`) gives `J_8^{(2)}(Y_det) ⊆ I(Y_det)`, and `rank d_2^{(8)}(z per_3) = 13490 <= 15660` gives the
containment in `I(Y_pad)` by Lemma 3.2. **The corrigendum's C7 list shrinks by exactly one
item:** `d_2` at `k = 8`, `N = 16`, is now assessed, with the same outcome as `k = 7`.

**Not established.** No gap, no cell, no equation nonzero on padding. Nothing about
`d_2^{(k)}` for `k >= 9`, nothing about `d_j` for `j >= 3` at `N = 16`, nothing about individual
minors of size `<= 15660`, nothing about the `GL_16`-decomposition of `J_8^{(2)}(Y_det)`, and no
monotonicity in `k` (C6 stays withdrawn: two data points, `k = 7, 8`, are not a trend).

**Prices of the next things, not run (one table, as instructed).** Sizes are exact; block
counts for `k = 9` were **not** enumerated.

| computation | full size | what is known about cost | status |
|---|---|---|---|
| `d_2^{(9)}`, `N = 16` | `K_2(9) = 120 . 816 = 97920` rows, `K_1(9) = 16 . 54264 = 868224` cols; `K_3(9) = 560` | same grading; blocks not enumerated (the bucketing alone touches 868 224 column keys, itself a pilot); expected well beyond `192 x 528` per block | unpriced beyond size; not run |
| `d_3^{(9)}`, `N = 16` | `560 x 97920` | `rank = 560` iff `d_3^{(9)}` injective; at a smooth quartic it is; tiny under the grading | unpriced beyond size; not run |
| `GL_16`-decomposition of `J_8^{(2)}(Y_det)` (size-15661 minors) | polynomial degree 15661 in 3876 coefficients | not a matrix computation; no method priced on this record for a Fitting ideal of this size | unpriced; not run |

## 5. Labelled ledger (all rows producer only, G18)

| # | claim | status |
|---|---|---|
| L1 | Lemma 2.1 (weight preservation by every `d_j`) and Lemma 2.2 (block-diagonal rank additivity) | PROVED (elementary) |
| L2 | `rank_Q d_1^{(5)}(det_4) = 1712`, `rank_Q d_1^{(5)}(z per_3) = 1244`; kernels 464, 932 | CERTIFIED, exact over `Q`, every block `fmpz_mat`; second lineage for the corrigendum's recorded 464 / 932 (those were single-lineage on this record: the P3 script computed `dim L` only at `k = 7`, and the `k = 8` values entered through the launch prompt) |
| L3 | `rank_Q d_2^{(8)}(det_4) = 15660`, `rank_Q d_2^{(8)}(z per_3) = 13490`, `rho_2(8) = 16320` | CERTIFIED, exact over `Q`, `results/b20_02b/p1_d8_blockwise.json` (per-block ranks, weights, sizes and methods listed) |
| L4 | `dim H_2(det_4)_8 = 660`, `dim H_2(z per_3)_8 = 2830` | CERTIFIED (from L3 and `K_3(8) = 0`) |
| L5 | No reversal at `N = 16`, `j = 2`, `k = 8`; `J_8^{(2)}(Y_det) ⊆ I(Y_det) ∩ I(Y_pad)`, and `J_8^{(2)}(Y_det) != (0)` | PROVED given L3 and the `d_2`-version of the parent's Lemmas 3.1–3.2 (elementary, restated in §4) |
| L6 | No gap, no cell, no equation nonzero on padding; nothing at `k >= 9`, `j >= 3` | — |

Depth sensitivity and `grade = height` are not used in this session; their labels in B20-02 §9
are unchanged (UNREAD; Dimca PRIMARY at statement level). `L` and `delta_0` do not occur.

## 6. Resources, receipts, manifest

Interpreter `.venv/python.exe` (Python 3.12.10, python-flint 0.9.0); wrapper
`analysis/b15_bound.py --seconds 60 --memory-mb 512 --slot 02`; `PYTHONDONTWRITEBYTECODE=1`.
Before the launch: zero `python*` processes (`Get-Process`), and no `B15-01\results\logs\b20_01_*.pid`
file existed. **No unwrapped run of any size was made in this session.**

| run | kind | started (UTC) | wall | peak job memory | exit | receipt |
|---|---|---|---|---|---|---|
| `b20_02b_p1_d8_blockwise` | wrapped, 60 s / 512 MiB | 21:37:57 | 3.35 s | 92.2 MB | 0 | `results/logs/b20_02b_p1_d8_blockwise_resources.json`, `.pid`; console `results/b20_02b/p1_console.log` |

Wrapped launches: 1 of 3; Pilots 2 and 3 unused. Wall spent: 3.35 s of 180 s. No cap hit. No
receipt overwritten. Nothing under `results/b20_02/` was modified; `results/b20_02/MANIFEST.json`
and the price file are re-hashed by the seal script (G11) and reported unchanged there.

**Manifest.** `results/b20_02b/MANIFEST.json`, written by `analysis/b20_02b_seal.py`, which
prints every count it writes (`results/b20_02b/SEAL_LOG.txt`): sha256 of this report, the two
scripts, the pilot JSON, the console log, the two receipt files, the two copied inputs
(checked against their pins), and the re-hash of the two B20-02 files read. New files of this
session: `docs/b20_02b_report.md`, `analysis/b20_02b_d8_blockwise.py`, `analysis/b20_02b_seal.py`,
`results/b20_02b/` (with `inputs/`), and the two `results/logs/b20_02b_*` receipts. Git
read-only; `git status --porcelain` at the end lists only these, B20-02's files and the four
pre-existing 2026-09-13 receipts.
