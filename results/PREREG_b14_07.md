# PREREG — B14-07: exact degree-14 source matrix at `P14`

**Session** B14-07, batch 14, slot 7 (`flint` host class).
**Model that actually ran this session** `claude-opus-5` (Claude Opus 5). The
packet names "Claude"; this line records the serving configuration, per §5 of the
board and the packet's own instruction.
**Written and committed before any measurement.** Instrument validation and
toolchain checks that preceded this file are listed in §8 and are labelled as
such; no entry of the matrix was computed before this commit.

---

## 0. Base, resolved not inherited

| item | value |
|---|---|
| tag `batch14-base` (tag object) | `4bda8a12433c5965a5df82fef35b4c7220b76756` |
| **commit** (`git log -1 --format=%H batch14-base`) | `9898e56941a7665f231873481dae956f08509995` |
| **tree** (`git log -1 --format=%T batch14-base`) | `cb688cd3fe454d638f3202e759e2eaa0c629739f` |

**Defect reported (D1).** The packet states "Your dispatch message states the
expected commit and tree." No dispatch message accompanied this packet, so there
was no value to check the tag against. The pair above was recovered from the tag
and independently corroborated by `git ls-remote`, which peels server-side and
returns `refs/tags/batch14-base^{}` = `9898e569…`. Two independent peels agree.

**Defect reported (D2).** This session began with no clone of the repository at
all — a state the packet does not anticipate (it anticipates only a clone that
predates the freeze). The user's laptop clone is fully packed and its 183 MB main
pack would not cross the device bridge. The base was obtained by cloning
`https://github.com/swsethuraman/gct.git`, which carries `batch14-base` as an
annotated tag; the resulting object is identical. Recorded for the other eleven
sessions: **the bridge cannot move this repository, the remote can.**

## 1. Question

Compute, **exactly over ℚ**, the degree-14 source matrix `A14` of the LMR ladder
at the point set `P14`, and its **left** kernel.

- `A14` is `93 × 192`: rows are the source fillings born by degree 14 (rungs
  12, 13 and 14 of `results/s74/source.json`: 2 + 37 + 54 = 93), columns are the
  192 `role == "primary"` points of `results/b14_prep/points/P14.json`.
- Row system, at degree 14, following s74's declared convention with the
  transport exponent changed from `24 − d_i` to **`14 − d_i`**:

      A14[i][j] = F_{T_i}(f_j) · msym_u(f_j)^(14 − d_i),
      msym_u(f) = 4! · [s_1^4] f,   d_i = native degree of row i ∈ {12, 13, 14}.

  Rows are **literal** transported fillings (not `u`-normalised; the s74
  alternative divides by `24^(14−d_i)`). Every stored value matrix carries a
  `values_are` field naming this.
- `K14` is a basis of `{x ∈ ℚ^93 : xᵀ A14 = 0}`, of size `93 × k`.

**Orientation, stated explicitly because the board says two sessions have had it
backwards:** source vectors are ROWS, points are COLUMNS, so ideal relations live
in the **LEFT** kernel: `Σᵢ cᵢ Fᵢ` is a candidate relation iff `cᵀA14 = 0`. The
right kernel `A14·K = 0` has dimension ≥ 99 and is **not** the object wanted.

## 2. What this is NOT

Per the board, slot 7 and `PROVED.md: evaluation_cannot_certify_i_ge_1`:

- This is a **source-matrix result**. It is not `i_red(14)`, and it will not be
  labelled `i_red(14)` in any artefact or in the report.
- `k` becomes an **ideal** kernel dimension only after the degree-14 target
  certificate (slot 1's stretch), the recount (slot 4) and the interpolation
  check (slot 3) all pass. Until then every statement about `k` is about a
  sampled matrix.
- A deficient rank is a **ceiling** on `i` and a **floor** on the rank
  (`PROVED.md: rank_floor`). Nothing here establishes `i ≥ 1`.
- If the matrix is only partially completed, its nullity is a **ceiling** on `k`
  and will be reported as one.

## 3. Instrument

| component | choice | why |
|---|---|---|
| evaluator | `wk12_s74_dp.dp_eval_compact` (compact-state DP, `wk12_s74_dpc.c`) | validated in §8 against banked `rows_native`; 0.056 s/eval vs 41 s for `fast_eval_c` |
| independent evaluator | `wk11_s69_circuit.fast_eval_c` (Identity 3: inclusion–exclusion over subsets + determinants) | a different algorithm, not a different implementation of the same one |
| exact-integer evaluator | Identity 3 carried out in exact `ℤ` arithmetic (flint `fmpz_mat` determinants, no modulus) | the board's required "small exact integer evaluator independent of the fast modular path" |
| exact linear algebra | `python-flint` `fmpq_mat` / `fmpz_mat` | house rule |
| primes | the seven in `P14.json`: 2147483647, 2147483629, 2147483587, 2147483579, 2147483563, 2147483549, 2147483543 | house primes first; primality re-verified here, not inherited |

**Letter-ordering rule observed.** `msym_u`'s index is resolved by
`exps(4,9).index((4,0,…,0))`, never by a literal. Measured: index **494**, and
`exps(4,9)[0] = (0,…,0,4)` — `wk8_s30_core.exps` runs the first exponent **up**
from 0, the ordering the board warns has cost three sessions.

## 4. Height bound — re-derived, not inherited

From the Leibniz form of `F_T` (`wk11_s69_circuit.brute_force_eval`):

    F_T(f) = Σ_{s ∈ {0,1}^{n2}} (−1)^{|s|} Σ_{π1 ∈ S_h} Σ_{π2 ∈ S_h} sgn(π1) sgn(π2) ∏_{l=0}^{d−1} m_{α(l)}

so the term count is `2^{n2}·(h!)²` and each term is a product of `d` symbols:

    |F_T(f)| ≤ 2^{n2} · (h!)² · M^d,    M = max_α |α! · c_α(f)|.

Here `h = 9`, `n2 = 15`, `d = 14`. For the bound on `M`: `f = ℓ·c` with `ℓ` and
`c` integer, all coefficients in `[−7, 7]` (`P14.json: integer_bound = 7`). For
`|α| = 4` with `k` distinct indices and parts `a_1..a_k`,

    c_α(f) = Σ_{i : α_i ≥ 1} ℓ_i · c_{α−e_i}   →   |c_α| ≤ k·49,   α! = ∏ a_i!

so `|m_α| ≤ (∏ a_i!)·k·49`, maximised over the partitions of 4:

| shape | `α!` | `k` | bound |
|---|---|---|---|
| (4) | 24 | 1 | **1176** |
| (3,1) | 6 | 2 | 588 |
| (2,2) | 4 | 2 | 392 |
| (2,1,1) | 2 | 3 | 294 |
| (1,1,1,1) | 1 | 4 | 196 |

`M ≤ 1176 = 24·7²`, attained shape-wise at `α = (4,0,…,0)`. Hence

    H_14 = 2^15 · (9!)² · 1176^14 = 41752117405971316170471859365816782308304944383288095539200

(195 bits; `2·H_14` is 196 bits). The seven-prime product is 217 bits, margin
**2.522 × 10⁶**. Signed CRT is therefore valid on seven primes.

**This agrees exactly with the delivered `source_value_bound` and its
derivation `(9!)²·2^15·(24·7²)^degree`.** The agreement is recorded as a
re-derivation reaching the same number by the same route, which is *confirmation,
not method diversity*; the board asked me not to inherit it, and I did not.

## 5. Decision table

Let `r_p = rank_{F_p}(A14)` and `r_ℚ = rank_ℚ(A14)`, `k = 93 − r_ℚ`.
Sampled prior (`results/s74/ladder_ranks.json`, δ=14, both house primes, s74's
282 red points): `rank_red = 88`, nullity 5.

| observation | conclusion | label |
|---|---|---|
| `r_ℚ = 88`, `A14ᵀK14 = 0` exactly, `rank(K14) = 5` | `k = 5` exactly; matches the sampled prior | **CERTIFIED** (source matrix only) |
| `r_ℚ = 88 + t`, `t ≥ 1` | `k = 5 − t`; the sampled nullity was a strict ceiling | **CERTIFIED** (source matrix only) |
| `r_ℚ < max_p r_p` | **impossible** — contradicts `rank_floor` | **STOP**, instrument fault |
| matrix completed for only `c < 192` columns | nullity of the prefix is a **ceiling** on `k` | **MEASURED**, ceiling stated |
| any `|reconstructed entry| > H_14` | bound violation | **STOP** (§7) |

**Expectation, labelled.** I expect `r_ℚ = 88`, `k = 5`. This is a *prediction
from an already-observed sampled value*, not a blind one: `ladder_ranks.json`
records nullity 5 at δ=14 at both house primes. It is stated so that a different
answer is visibly a surprise, not so that agreement can be presented as
confirmation of anything.

## 6. Controls — each must be fed an input that makes it fail

Every control below is run **twice**: once on the true input, once on a
deliberately corrupted input that must make it report failure. Both outcomes are
recorded. A control whose failing run does not fail is reported as a defective
control, not as a pass.

| id | control | deliberate failure injected |
|---|---|---|
| **C1** | DP evaluator reproduces banked `rows_native` (`results/s74/columns_red_2147483647.json`) for all 93 rows on a sample of s74's own red points | two letters swapped in one filling's first tall column |
| **C2** | row-system identity: the literal filling climbed to degree 14 and evaluated directly equals `native × u^(14−d_i)` | transport exponent replaced by `13 − d_i` |
| **C3** | independent algorithm: `fast_eval_c` (Identity 3) agrees with `dp_eval_compact` on sampled (row, point, prime) triples | one symbol `m_α` incremented by 1 |
| **C4** | `u(P_j) ≠ 0` at every point and every prime, recorded per point | a synthetic point with `ℓ_1 = 0` (forcing `u = 0`) inserted |
| **C5** | signed CRT round-trip on integers drawn near ±`H_14` | an integer of magnitude `> H_14` must **fail** to round-trip, demonstrating the `|x| ≤ H` check has teeth |
| **C6** | exact **integer** evaluator (Identity 3 over ℤ, no modulus) agrees with the CRT-reconstructed entry, on selected entries | one reconstructed entry altered by 1 |
| **C7** | primality of all seven CRT primes re-verified in-house | a composite substituted into the list |
| **C8** | **holdout**: every vector of `K14` found on the 192 primary points must also annihilate the 20 `role == "holdout"` columns | a random non-kernel vector must fail the same test |
| **C9** | `negative_control_forced` (`PROVED.md`): a diagonal pencil makes the quartic a product of linear forms of span ≤ 3; a length-9 weight must read rank 0 | the same sweep on a generic point must **not** read 0 |

**C8 is the one that matters most and is cheap.** A left-kernel vector of the
sampled matrix that fails on held-out columns is an artefact of the point set,
not a candidate relation. The holdout columns are computed but are **not** used
to determine `k`.

## 7. Stopping rules

Computation stops — and the partial result is reported as partial — on any of:

1. **Bound violation.** Any signed-CRT reconstruction with `|x| > H_14`.
2. **Source-control inconsistency.** C1, C2, C3, C6 or C7 failing on true input.
3. **Rank contradiction.** `r_ℚ < max_p r_p`.
4. **A `u`-zero.** Any point with `u(P_j) ≡ 0` at any prime voids that column;
   the column is dropped, recorded, and the matrix reported at reduced width.
5. **A control that cannot fail.** If any deliberately corrupted input in §6
   does not produce a failure, that control is void and is reported as void.
6. **Budget.** See §9.

Runs are bounded at launch with `timeout` and `ulimit -v`; the pid is written to
`results/logs/<run>.pid` and a run that must end early is ended by that recorded
id.

## 8. Instrument validation performed BEFORE this pre-registration

Declared here for honesty; none of it is a measurement of `A14`.

1. Toolchain: `python3 -c "import flint, sympy, numpy, scipy"` → ok.
   python-flint 0.9.0, sympy 1.14.0, numpy 2.4.4, scipy 1.17.1, gcc 13.3.0,
   CPython 3.11.15. `python-flint` and `sympy` were **installed** by this
   session; numpy, scipy and gcc were present.
2. Input contract by git blob id — all three match:
   `P13.json` `76e1f2ed…`, `P14.json` `ebb595c0…`, `source.json` `ca17e743…`.
3. `fast_eval_c` reproduced 12/12 banked `rows_native` values (rungs 12, 13, 14)
   — and cost 41 s per evaluation, which is why it is the *control* evaluator
   and not the production one.
4. `dp_eval_compact` reproduced 30/30 banked `rows_native` values at 0.056 s per
   evaluation. Pathwidths measured 4–5 against `max_W = 8`.
5. `exps(4,9).index((4,0,…,0)) = 494` and `exps(4,9)[0] = (0,…,0,4)`.

## 9. Budget and stopping

Measured unit cost 0.056 s/evaluation × 93 rows × 192 points × 7 primes =
**124,992 evaluations ≈ 6,980 s single-core**; the host has **2 cores**, so the
planned wall clock is ≈ 1 hour with a two-worker pool, plus holdout columns
(20/192 more ≈ 7 min) and CRT/linear algebra.

**The memo's indicative "seven hours across seven primes" is not validated and is
not adopted.** The figure above is this session's own measurement on this host.

Order of work, so that a truncated session still delivers something exact:

1. prime 1 (2147483647) — all 93 × 212 columns, then rank and left nullity mod p;
2. prime 2 (2147483629) — same, cross-checking the mod-p rank;
3. primes 3–7;
4. signed CRT, bound check, exact ℚ rank and left kernel;
5. controls C1–C9 with their failure injections;
6. exact-integer entry checks (C6) on as many entries as the remaining budget
   allows, minimum 3.

**Budget stop.** If primes 3–7 cannot complete, the deliverable is the exact
matrix modulo the primes that did complete, the mod-p left nullity as a
**ceiling** on `k`, and a costed completion plan — which the board names as an
acceptable success mode ("a certified prefix with a reproducible completion
plan").

## 10. Host resources, declared

One container: **2 cores, 7 GB RAM, ~30 GB disk**. Twelve sessions do not imply
twelve independent memory budgets; if the other flint slots are sized against
this same class, they are sharing it.

## 11. Files this session will write

- `results/PREREG_b14_07.md` (this file)
- `results/b14_07/A14_mod_<prime>.json` — per-prime value matrices, each with a
  `values_are` field
- `results/b14_07/A14_exact.json[.gz]` — the exact integer matrix
- `results/b14_07/K14.json` — the exact left kernel with its verification record
- `results/b14_07/controls.json` — every control, true run and failure-injected run
- `results/logs/*.log`, `results/logs/*.pid`
- `docs/b14_07_report.md`

Nothing outside `results/`, `docs/` and `analysis/` is touched. The four
single-writer files (`paper/det3-conductor.tex`, `paper/det4-onset.tex`,
`PROJECT_NOTES.md`, `docs/boundary_deficit.html`) are not touched.
