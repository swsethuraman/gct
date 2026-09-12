---
session: B14-01
board_numbering: batch14
model_actually_run: claude-opus-5 (configured identifier; the serving model may differ and is not independently observable from inside the session)
base_commit: 9898e56941a7665f231873481dae956f08509995
base_tree: cb688cd3fe454d638f3202e759e2eaa0c629739f
base_tag_object: 4bda8a12433c5965a5df82fef35b4c7220b76756
author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI
---

# PREREG B14-01 — mixed-letter bracket evaluator, and a nonzero 73-minor at `P13`

Written and committed **before** any measurement listed in §5 onward. The
preflight in §0.3 was run *before* this file existed and is therefore reported
as **exploratory**, not as a pre-registered result.

## 0. Base, inputs, host

### 0.1 Base (verified, not inherited)

`batch14-base` is an annotated tag. Resolved with the packet's exact commands:

    git log -1 --format=%H batch14-base   ->  9898e56941a7665f231873481dae956f08509995   (commit)
    git log -1 --format=%T batch14-base   ->  cb688cd3fe454d638f3202e759e2eaa0c629739f   (tree)
    git rev-parse batch14-base            ->  4bda8a12433c5965a5df82fef35b4c7220b76756   (TAG OBJECT, not used as base)

**Defect, reported here and in the report: my dispatch message did not state the
expected commit and tree.** The packet says "Your dispatch message states the
expected commit and tree ... Record both values in your pre-registration and
check they match what the tag resolves to." No such message reached this
session, so the prescribed cross-check had no second value to compare against.
Substituted cross-check, which is independent of the clone used here: the tag
object id recorded in the dispatching workstation's own
`.git/refs/tags/batch14-base` is `4bda8a12433c5965a5df82fef35b4c7220b76756`,
byte-identical to the tag object served by `origin`; that workstation's
`refs/heads/integration/batch13` and `refs/remotes/origin/main` both hold
`9898e569...`, the peeled commit. Two independent sources agree on the tag
object and on the commit. This is weaker than a stated hash in the dispatch and
is labelled as such.

Required files present at this tree: `docs/batch14_board.md` (**v0.4**),
`docs/PROVED.md`, `docs/brief_wording.md`, `docs/b14_claude_scratch_code.md`,
`docs/batch14_reconciliation.md`.

### 0.2 Input contract (blob ids at the base tree — all three match the board)

| file | blob at base | board | match |
|---|---|---|---|
| `results/b14_prep/points/P13.json` | `76e1f2ed7be8ba85e14ba74cae5be76504f67072` | same | yes |
| `results/b14_prep/points/P14.json` | `ebb595c0e61b85bbb1d380caa58d90d80ad133f2` | same | yes |
| `results/s74/source.json` | `ca17e74393228d9c3d9729e7839f0157cb1e21eb` | same | yes |

Other inputs read: `analysis/wk11_s69_circuit.py`, `analysis/wk12_s74_dpc.c`,
`analysis/wk12_s74_dp.py`, `analysis/wk12_s74_columns.py`,
`analysis/wk8_s30_core.py`, `docs/b13_01_report.md`, `results/b13_01_hpad.json`.

### 0.3 Exploratory preflight (run before this file; NOT pre-registered)

1. Toolchain: `python3 -c "import flint, sympy, numpy, scipy; print('ok')"` -> ok.
   Installed in-session: `python-flint 0.9.0`, `sympy 1.14.0`, `mpmath 1.3.0`.
   Already present: `numpy 2.4.4`, `scipy 1.17.1`, `gcc 13.3.0`, Python 3.11.15.
2. **`exps` ordering.** `wk8_s30_core.exps(3,9)[0] = (0,...,0,3)` — first exponent
   **up** from 0. `P13.json`'s `cubic_exponents[0] = (3,0,...,0)` — first exponent
   **down** from 3. Same set, opposite order (verified: sets equal, sequences not).
   Every cubic coefficient is therefore resolved by `E3.index(tuple(exponent))`.
   No positional read of a coefficient array appears anywhere in this session's code.
3. **Coefficient convention cross-check against two independently shipped
   quantities**, at all 116 `P13` and all 212 `P14` points:
   `u_symbol == 24 * linear[0] * c_{(3,0^8)}` (116/116, 212/212) and
   `max_abs_quartic_symbol == max_beta |beta! * coeff_beta(l*c)|` (116/116, 212/212).
   This fixes `linear[i]` = coefficient of `x_i` and `cubic_coefficients[k]` =
   coefficient of `cubic_exponents[k]`. It is a check that can fail: a transposed
   linear convention or a positional cubic read breaks both identities.
   `u(P_j) != 0` at every one of the 328 points (0 `u`-zeros), so no transported
   row is silently voided in any column of either point set.
4. Baseline instrument cost, uniform quartic `n=4`, `h=9`, `n2=15`, `n1=4`,
   `delta=13`, `dp_eval_compact`: 5 fillings, mean **0.174 s** per evaluation
   (`W=3` typical, one `W=4` at 0.418 s).

### 0.4 Host resources, declared

2 cores, 8.0 GB total / ~7.4 GB available, ~30 GB writable disk, single container.
**Twelve sessions do not imply twelve independent memory budgets**; every run here
is bounded at launch and sized to stay inside ~2 GB so that concurrent sessions on
a shared box are not displaced. No run is permitted above `ulimit -v 3000000` (3 GB).

## 1. The question

At `lambda_13 = (21,17,2^7)`, `delta = 13`, `r = 9`:

**Q1 (core).** Exhibit explicit highest-weight vectors of the reducible
normalisation target `N_13`, built as *mixed-letter* bracket monomials on the
shape `lambda' = (9,9,2^15,1^4)` with two letter types — `l` of valence 1 and
`c` of valence 3 — and certify a **nonzero `73 x 73` minor** of the
(members x `P13` points) evaluation matrix at **both** house primes
`2147483647` and `2147483629`.

**Q2 (stretch, this slot's alone).** The same at `delta = 14`,
`lambda_14 = (25,17,2^7)`, shape `(9,9,2^15,1^8)`: mixed target members and a
nonzero **`159 x 159`** minor at `P14`, with the same membership and replay data.

## 2. Why the object is what it is (stated before computing, so it can be wrong)

The normalisation is `nu : (l, c) |-> l.c`. Degree-`delta` forms pull back to
bidegree `(delta, delta)` functions of `(l, c)`, i.e. to
`Sym^13(V*) (x) Sym^13((Sym^3 V)*)`. Since `l` is linear, its factor is the single
irreducible `S_(13)`, so by Pieri

    dim N_13 = sum_{mu : lambda/mu a horizontal 13-strip} a_3(mu, 13),

which is `h_pad(21,17,2^7;13)`. B13-01 computed this exactly by Weyl alternation
as **73** over **15** strips with `a_3 = [1,2,2,3,3,4,4,5,5,5,6,7,8,9,9]`; the
board records a second, independent power-sum/Murnaghan-Nakayama route agreeing
**channel by channel**. I **adopt 73 as an upper bound** and do not recount it
(slot 4 owns the recount).

**Pre-registered structural claim, checkable and falsifiable.** The 15 strips are
exactly `mu = (mu_1, mu_2, 2^6, mu_9)` with `17 <= mu_1 <= 21`, `0 <= mu_9 <= 2`,
`mu_1 + mu_2 + mu_9 = 27`. I predict, before enumerating in code, that this count
is **15**. If the enumeration returns any other number my reading of the target is
wrong and Q1 stops.

**Why this shape and not the strip-by-strip route.** B13-01 §6 records that only
10 of the 15 `mu` have conjugate in the compact-circuit family; the other 5 have
*unequal* tall columns (`mu_9 = 1` gives `mu'_1 = 9`, `mu'_2 = 8`) and would need a
two-different-height evaluator. On the **full** `lambda'` the two tall columns are
both height 9 for all 15 strips, and the height mismatch is absorbed by an
`l`-letter sitting at row 9 of a tall column. This is the stated reason the board
calls `(9,9,2^15,1^4)` "already in the evaluator's class", and it is why the mixed
route is cheaper than the strip route. **Nothing downstream depends on this being
the right explanation** — it is a search heuristic only (§4).

## 3. Instrument, and the reuse condition

`Filling`/`dp_pack` (`wk11_s69_circuit.py`) + the compact C core
`dp_eval_compact` (`wk12_s74_dpc.c`).

**The C core is reused only under a proved compatibility condition, stated now.**
Reading `wk12_s74_dpc.c`, its interface contract is: per letter, `inC1` in {0,1},
`inC2` in {0,1}, `d2` legs in 2-columns, and a tensor `T[((i*nj)+j)<<d2 | bits]`;
**the valence `n` appears nowhere in the C source** — remaining legs (1-columns)
are folded into the tensor *value* by the Python packer, never into an index.
Therefore the core computes the Leibniz sum for **any** assignment of legs
satisfying "at most one box per letter per column", which is exactly
column-strictness. The mixed packing satisfies it by construction.

**This argument is not accepted on its own.** It is discharged only if control
C1 (§5) passes: the literal Leibniz brute force must agree with the C core on
mixed shapes, exactly, mod `p`. If C1 fails, the C core is not reused and the
session falls back to the Python path at whatever cost that imposes.

### 3.1 Conventions, defined separately per letter type (required by the board)

- **`l`-letter (valence 1).** One leg. Symbol at index `i`: `m_{e_i}(l) = 1! * l_i
  = l_i`. Symmetry: the 13 `l`-letters are interchangeable; the evaluation
  substitutes the *same* `l` into every one of them.
- **`c`-letter (valence 3).** Three legs at indices `(i,j,k)` (a multiset).
  Symbol: `m_alpha(c) = alpha! * c_alpha`, `alpha` the multiplicity vector of
  `(i,j,k)`, `c_alpha` resolved by `exps(3,9).index(alpha)`. Symmetry: the 13
  `c`-letters are interchangeable; the same `c` is substituted into each.
- **Column rule (both types).** No letter twice in a column. Tall columns `C1`,
  `C2` carry 9 distinct letters each; each 2-column carries 2 distinct letters;
  each 1-column carries 1.
- **Sign.** Unchanged from `dp_pack`: `rho_sign(C1) * rho_sign(C2)` times the
  DP's internal mask/2-column signs. Not re-derived; validated by C1.

## 4. Objects and the directed search

Members are mixed fillings. The pre-registered search is **strip-directed**, in
this order, and then a fallback:

- **S1 (directed).** For each of the 15 strips `mu`, place the 13 `l`-letters on
  the cells of `lambda/mu` — `(21-mu_1)` in 1-columns at row 1, `(17-mu_2)` at row
  2 of distinct 2-columns, `(2-mu_9)` at row 9 of the tall columns — and fill the
  remaining 39 cells (the diagram of `mu`) with 13 valence-3 `c`-letters,
  column-strict, sampled at random. Quota: up to `4 * a_3(mu,13)` draws per strip
  in the first pass.
- **S2 (deterministic semistandard pass).** One deterministic pass over
  semistandard-ordered `c`-fillings per strip, in a fixed enumeration order, taking
  the first `a_3(mu,13)` that raise the rank. **This is the single deterministic
  pass the budget rule allows; there is no second one.**
- **S3 (fallback only).** Unconstrained random mixed fillings.

A candidate is **accepted** iff it strictly raises the rank of the accepted
matrix over `p = 2147483647`. Search runs at `P1` only; accepted members are then
re-evaluated at `P2` independently.

Points: the **96 `primary`** `P13` points, in file order, `role == "primary"`.
The 20 `holdout` points are not used in the search and are reserved for §5 C6.

## 5. Controls — each one with the input that must make it fail

Every control below is run **twice**: once on the honest input, once on an input
constructed to break it. **A control is only reported as passing if its negative
instance was also run and did fail.** (`PROVED.md: check_must_be_able_to_fail`;
the seventh instance was an `all()` over an empty census.)

| id | control | must PASS on | must FAIL on |
|---|---|---|---|
| C1 | literal Leibniz brute force == C core, mod `p` | random mixed fillings on small in-class shapes (`h=3,4`, `delta` small, both letter types present, `>= 20` pairs) | the same with one letter's tensor perturbed in a single entry |
| C2 | torus weight: `F_T(f(t.x)) == (prod t_i^{lambda_i}) * F_T(f)` mod `p` | random mixed fillings, random diagonal `t` | a filling whose `l`-count is altered so the weight is not `lambda` |
| C3 | raising / highest weight: `F_T` invariant under the strictly-triangular substitution in the highest-weight direction, and **not** invariant in the opposite direction | random mixed fillings | the opposite direction must move the value — if *both* directions are constant the test has no teeth and is void |
| C4 | **deliberately wrong tensor normalisation is rejected**: `c`-letter symbol taken as `c_alpha` (no `alpha!`) and, separately, as `4!`-scaled | honest normalisation passes C2+C3 | the two wrong normalisations must **fail** C2 or C3 |
| C5 | `negative_control_forced` (required on every evaluation-rank sweep): `lambda` has 9 parts, so every weight vector of weight `lambda` vanishes at any point of span `< 9`. Points `(l,c)` supported on 8 variables must give **0** for **every** member | all members, all 8-variable points | a 9-variable generic point must give a nonzero value for at least one member — otherwise the evaluator is returning 0 identically and C5 is vacuous |
| C6 | rank on the 20 **holdout** points, unused in the search, must not exceed the search rank; and the full 116-point rank must equal the 96-point rank | — | a holdout rank *above* the target dimension 73 falsifies the adopted `dim N_13 = 73` |
| C7 | **rank ceiling**: measured rank `<= 73` at every stage | — | rank `> 73` contradicts the adopted Weyl count and stops the session |
| C8 | both primes agree on the rank, and `rank_p <= rank_Q` is respected in every statement made | — | a rank differing between primes is reported, never averaged |

## 6. Decision table (fixed before computing)

| outcome at `delta = 13` | label | what I may say |
|---|---|---|
| rank 73 at both primes, nonzero `73x73` minor exhibited, C1–C8 all passed with their negatives failing | **CERTIFIED** | evaluation on those 73 points is **injective** on `N_13`; condition (iii) of `complete_interpolation` is met, and `dim N_13 >= 73` is certified *by me*, independently of the Weyl count. **I may not say `i_red(13)` at all** — that needs slot 2's exact source arithmetic and slot 3's verifier |
| rank `k < 73` at both primes | **MEASURED, partial** | a nonzero `k x k` minor; a rank **floor** `k` on the target; `dim N_13 >= k`. **Not** a claim that the target is `k`-dimensional, and **not** `i_red` anything |
| ranks differ between primes | **MEASURED** | report both; the smaller is the certified floor (`rank_p <= rank_Q`) |
| rank `> 73` | **STOP** | the adopted `dim N_13 = 73` is contradicted; stop, report, do not proceed to `delta = 14` |
| any of C1–C5 fails on its honest input | **STOP** | the evaluator is not validated; report the obstruction, claim no rank |
| any of C1–C5 **passes** on its negative input | **STOP** | the control has no teeth; it is reported as void, not as a pass |

The same table governs `delta = 14` with 73 -> 159 and `P13` -> `P14`.

**A nonzero minor is a rank FLOOR.** It bounds `i <= a - k` on the *source* side;
on the *target* side it is exactly what `complete_interpolation` condition (iii)
asks for and nothing more. Nothing in this session establishes `i >= 1`, and no
statement here will assert `D` at LMR.

## 7. Falsifiers

1. The strip enumeration returns a count other than 15 -> §2 reading is wrong.
2. C1 fails -> the C core is not compatible with mixed packing; the §3 argument is
   refuted and the reuse is withdrawn.
3. Rank exceeds 73 -> the adopted target dimension is wrong.
4. C5's forced zero is violated (a nonzero value at an 8-variable point) -> the
   evaluator does not compute a weight-`lambda` vector.
5. C3 shows invariance in **both** triangular directions -> the highest-weight test
   is vacuous and is reported as void rather than as a pass.

## 8. Stopping rules and budget

- **Budget stop (from the packet):** after the pre-registered directed search S1
  plus **one** deterministic semistandard pass S2, record the partial rank and do
  **not** claim the target complete. S3 is entered only if S1+S2 leave rank `< 73`
  and time remains; anything found in S3 is labelled exploratory.
- Any run: `timeout` and `ulimit -v` at launch, pid to `results/logs/<run>.pid`,
  ended only by that recorded id.
- `delta = 14` is entered **only** after `delta = 13` reaches a CERTIFIED or
  MEASURED-partial verdict and its controls are banked.
- Files over 5 MB are not committed. Logs under `results/logs/`.
- `paper/det3-conductor.tex`, `paper/det4-onset.tex`, `PROJECT_NOTES.md`,
  `docs/boundary_deficit.html` are not touched.

## 9. Labelled expectations (recorded so they can be wrong)

| # | expectation | confidence |
|---|---|---|
| E1 | the strip enumeration returns exactly 15 | high |
| E2 | C1 passes: the C core is mixed-compatible unchanged | high — the source contains no valence |
| E3 | rank 73 is reached at `delta = 13` within S1+S2 | **medium** — B13-01 measured coupon-collector under-spanning (span 1/2, 4/9, 3/7, 2/5 in a few hundred draws) on the cubic blocks; the strip direction is designed against exactly that, and is untested |
| E4 | mixed evaluation costs within 3x the 0.174 s uniform baseline | medium |
| E5 | the `delta = 14` stretch (159-minor) is reached | **low** — 159 x 192 x 2 evaluations plus a harder search, on 2 cores |
| E6 | no member evaluates nonzero at an 8-variable point | high — forced by representation theory |

**E5 is low and is stated as low.** If the stretch is not reached I will say so
explicitly, and record that `D = -4` is then not reached either.

## 10. What this session will *not* claim

- Not `i_red(13)` or `i_red(14)` — those need slots 2, 7, 3 and 4.
- Not `i >= 1` anywhere, from any rank.
- Not `D` at LMR, in any direction.
- Not a recount of 73 or 159 (slot 4's, and already two-method per the board).
- No external announcement or publication.
