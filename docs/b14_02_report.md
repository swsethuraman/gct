# B14-02 — exact degree-13 source matrix at `P13`

**This report is delivered in one part (`part00`); the bundle is a single file
well under the split threshold.** Session B14-02, board slot 2, `flint` host
class, `board_numbering: batch14`. **The model that actually ran this session is
`claude-opus-5` (Claude Opus 5)**; the packet named "Claude", and this line
records what ran, not what was scheduled. Pre-registration:
`results/PREREG_b14_02.md`, committed before any matrix entry was computed.

**Base.** Tag `batch14-base` → tag object `4bda8a12433c5965a5df82fef35b4c7220b76756`,
commit `9898e56941a7665f231873481dae956f08509995`, tree
`cb688cd3fe454d638f3202e759e2eaa0c629739f`. Branch `b14-02-source13`.

---

## 1. What was established

| # | statement | label |
|---|---|---|
| R1 | `H₁₃ = (9!)²·2¹⁵·1176¹³` is an upper bound on `\|F_T(f)\|` for every degree-13 climbed LMR filling and every `P13` point, re-derived from the Leibniz definition | **PROVED** |
| R2 | the exact integer matrix `A` (39 × 96) of `F_{T_i^{up13}}(f_j)`, all 3744 entries, by signed CRT over **seven** primes at 217 bits against a 186-bit requirement | **CERTIFIED** |
| R3 | `rank_ℚ(A) = 36`, witnessed by an explicit nonzero exact `36 × 36` integer minor (determinant 3770 bits) | **CERTIFIED** |
| R4 | the **left** kernel `K`, `39 × 3`, with `Aᵀ·K = 0` verified in exact integer arithmetic, `rank(K) = 3`, `rank(A) = 39 − 3` | **CERTIFIED** |
| R5 | **at most 3** genuine relations exist among these 39 transported source vectors on the reducible locus — because a sampled rank is a floor, `rank_true ≥ 36` | **CERTIFIED** (a ceiling on relations, by `rank_floor`) |
| R6 | the three exhibited vectors **are** ideal relations | **CONDITIONAL** — needs slot 1's 73-minor and slot 3's certificate |
| R7 | all three annihilate the 20 held-out points as well; over all 116 reducible points the rank is still exactly 36 | **MEASURED** |
| R8 | the same 39 rows have rank **39** at generic quartic points — the deficiency is a property of the reducible locus, not of the instrument | **MEASURED** |
| R9 | degree-14 pricing for slot 7: **78 ms/entry measured**, `93 × 192 × 7 = 124,992` entries → **2.7 core-hours** | **MEASURED** |
| — | `i_red(13)` | **NOT REACHED — and not claimed** |

**This is a source-matrix result.** Per the board it is not labelled `i_red(13)`
and is not an ideal-relation claim until slot 1's target minor and slot 4's
recount are accepted (`PROVED.md: evaluation_cannot_certify_i_ge_1`).

**Orientation, stated explicitly as slot 3 asks.** Source vectors are **rows**,
points are **columns**. Relation vectors are the **columns of `K`** with
`Aᵀ·K = 0`. The right kernel `A·K = 0` has dimension **60** here (`≥ 96 − 39 = 57`),
and is *not* the object wanted; it is reported only so the two cannot be confused.

## 2. The height bound (R1) — re-derived, then compared

Derivation in full in `PREREG_b14_02.md` §4. In outline: for `f = ℓ·c` with all
coefficients in `[−7,7]`, `m_α = α!·c_α` and `c_α(ℓ·c) = Σ_{i∈supp(α)} ℓ_i c_{α−e_i}`,
so `|m_α| ≤ α!·|supp α|·49`, maximised at `α = (4,0⁸)` giving `M ≤ 24·7² = 1176`.
The bracket sum has exactly `(h!)²·2^{n2}` signed terms, one bijection per column,
each a product of `δ` symbols. Hence `|F_T(f)| ≤ (9!)²·2^{15}·1176^{13}`.

**The `2^{15}` step was checked, not assumed.** Degree 13 only forces
`2·n2 + n1 = 34`, which permits `n2 = 16` or `17`; had any row carried those, the
inherited bound would have been *too small* and every reconstruction unsound. All
39 climbed fillings measure `n2 = 15`, `n1 = 4` (histogram `{15: 39}`).

- `H₁₃ = 35503501195553840281013485855286379513864748625244979200` — **185 bits**.
- Equals `P13.json`'s stored `source_value_bound` exactly. The inherited figure is
  **independently confirmed**, which is a different and stronger statement than
  having inherited it.
- Signed reconstruction needs `modulus > 2·H₁₃` = **186 bits**.
- The six primes shipped in `P13.json` give 186 bits, ratio **1.381**.
- **Seven primes**, adding `2147483543`, give **217 bits**, ratio **2.966 × 10⁹** —
  board §1 predicted "~3×10⁹".

Independent corroboration of the board's own arithmetic: the same derivation at
degree 14 with `n2 = 15` (measured over all 93 rows) gives a 195-bit bound and a
seven-prime headroom of **2.522 × 10⁶**, against the board's "2.5 million× on
seven". The two figures were produced from different ends and agree.

## 3. The matrix (R2)

Rows: `entries[0:39]` of `results/s74/source.json` (blob
`ca17e74393228d9c3d9729e7839f0157cb1e21eb`) — 2 at rung 12, 37 at rung 13,
matching `birth_profile {12: 2, 13: 37}` — each climbed to degree 13 by the
source's own rule, transport exponent `13 − d_i`. Columns: the 96
`role == "primary"` points of `results/b14_prep/points/P13.json` (blob
`76e1f2ed7be8ba85e14ba74cae5be76504f67072`), `P13-000 … P13-095`. Both blob ids
match board §1.

All 3744 entries are nonzero. Magnitudes: min 79 bits, median 104, max **124** —
a factor `2⁶¹` below the bound, as expectation E4 anticipated, because the bound
multiplies worst cases that cannot co-occur across all 13 letters.

`results/b14_02/A13_primary.json` carries the integers with a `values_are` field
beside them naming the transform (none), the row and column keys, the seven
primes, the modulus and the bound.

## 4. The left kernel (R3–R6), and what it does and does not mean

`rank_ℚ(A) = 36`, `k = 3`. Consistent at every one of the seven primes
individually (`rank_p = 36` for all seven), as `rank_p ≤ rank_ℚ` requires.

The three kernel vectors have supports of 36, 37 and 37 of the 39 rows and involve
both rungs; coefficients run to 34–39 bits. They are **not** sparse or
rung-localised, which is worth recording because a relation supported on two rows
would have suggested a duplicate source vector rather than a geometric fact.

**The reading, in the direction the programme keeps getting wrong.** Let `ρ` send
`c ∈ ℚ³⁹` to `Σ cᵢFᵢ` restricted to the reducible locus. Sampling 96 points can
only *lose* independence, so

- `rank(A) = 36 ⟹ rank(ρ) ≥ 36` — a **floor**, and this half is exact;
- therefore the space of relations valid on the *whole* reducible locus has
  dimension **`≤ 3`** — a **ceiling**;
- `k ≥ 1` is **not** established. The three vectors annihilate 96 (and then 116)
  sampled points; that is a candidate, not a certificate
  (`PROVED.md: evaluation_cannot_certify_i_ge_1`, and `rank_floor`).

Promoting `k = 3` to an exact value needs all four `complete_interpolation`
conditions, of which this slot supplies exactly one (exact source arithmetic).
Slot 1 owns the `dim N = h` proof, the `h` exhibited members and the nonzero
`h × h` minor at `P`.

## 5. The pre-registered expectation was wrong, and how that was discriminated

**E1 predicted `rank = 39`, `k = 0`, with high confidence. The measurement gave
36 and 3.** The prediction was badly reasoned, and the error is worth recording
because it is available to every other slot on this route: I read s74's
`birth_profile` — rank 2 through rung 12, 37 new directions at rung 13 — as
implying the 39 vectors stay independent here. That profile is independence at
**generic** points. This slot evaluates on the **reducible** locus `ℓ·c`, where a
drop is not an anomaly but the very thing `i_red` names. E1 should have predicted
a deficiency.

E2 said the first hypothesis for any deficiency is an instrument fault — wrong
transport, an `exps`-ordering slip, or a non-separating point set — and that the
controls are ordered to discriminate before anything is reported. They were, and
the discriminating control is §6 C7: **the same 39 rows, the same evaluator, the
same arithmetic, evaluated at 41 generic quartic points, have rank exactly 39.**
A broken climb, a wrong exponent, a mis-ordered `exps` or a stalled evaluator all
depress the generic rank too. None did. The instrument is exonerated and the
deficiency is located on the reducible locus.

`results/b14_02/direction_control.json`.

## 6. Controls — each with the input that made it fail

| control | on the real input | the input that must make it fail | verdict |
|---|---|---|---|
| **C1** forced zero | 3 coordinate-supported points, **0/39** nonzero rows each | a real point `P13-000`: **39/39** nonzero | can fail ✓ |
| **C2** transport | exponent `13−d`: **8/8** identities hold | exponent `24−d` (the value `source.json` stores): **8/8** differ | can fail ✓ |
| **C3** independent exact ℤ evaluator | see below | see below | can fail ✓ |
| **C4** CRT soundness | seven primes, 217 bits: **0/576** entries fail the seven-residue test | three primes, 93 bits < 186: **521/576** fail | can fail ✓ |
| **C5** `u`-nonvanishing | `u(P_j) ≠ 0` for all 96 columns as integers **and** mod all seven primes | — (an assertion, no draw was skipped) | n/a |
| **C6** rank witness | nonzero exact `36×36` minor; `Aᵀ·K = 0` over `ℤ`; `rank(K) = 3` | on a full-row-rank submatrix: duplicate a row → rank `36→35`, `k 0→1`; zero a row → same | can fail ✓ |
| **C7** direction | generic points: rank **39** | reducible points: rank **36** | discriminating ✓ |
| **C8** binary provenance | a freshly compiled `wk12_s74_dpc.so` reproduces the banked residues on **15/15** sampled entries | — | ✓ |

**C1's forced-zero argument, stated precisely.** `F_T` has weight
`λ = (21,17,2⁷)`, whose 9 parts are all nonzero, and `F_T(f)` is a sum of
monomials `Π_l c_{α_l}` with `Σ_l α_l = λ` exactly. If `f` is supported on a
proper **coordinate** subspace then `c_α = 0` unless `supp(α)` lies in it, so no
monomial can sum to a `λ` with `λ_9 = 2 > 0`. Hence `F_T(f) = 0`, forced by the
weight with no computation (`PROVED.md: negative_control_forced`). I state this
for coordinate-supported points only; the general `span < ℓ(λ)` form is not
needed here and is not claimed.

**C3, and two vacuous controls I caught in my own work.** The independent
evaluator (`analysis/b14_02_exact_check.py`) re-derives Identity 3 from the
Leibniz definition, uses its own pairing (order-preserving, not the house
2-edge-maximising heuristic — the identity holds for any such bijection), indexes
symbols by exponent **tuple** so neither `exps` ordering can reach it, and
computes in exact `ℤ`. It agrees with the literal Leibniz sum
(`brute_force_eval`) on **36/36** small-shape cases, **16 of them nonzero**.

Two controls of mine were vacuous on first writing, and both are recorded rather
than quietly repaired (`PROVED.md: check_must_be_able_to_fail`):

1. The first must-fail test shifted `msl[0]`, the symbol at exponent `(0,…,0,n)`,
   which the sampled fillings never use — so the comparison accepted a
   "corrupted" input that was not corrupted at all. Replaced by a perturbation
   *chosen by requiring the definition's own value to move*.
2. The sabotage mode `flipbits` was accepted, and that turned out to be
   mathematics, not a bug: flipping every 2-column bit is the relabelling
   `s → ~s` of the summation variable, so it multiplies the sum by `(−1)^{n2}`
   and is a **genuine symmetry at even `n2`**. My first battery had only even-`n2`
   shapes and would have reported an undetectable mode as a passing check. Three
   odd-`n2` nonzero shapes had to be *searched for* — the first three I tried had
   identically zero bracket spaces. With them the battery reads:

   | sabotage | odd `n2` | even `n2` |
   |---|---|---|
   | `nosign` (drop `sgn π`) | 2/3 | 1/3 |
   | `noparity` (drop `(−1)^{\|s\|}`) | 3/3 | 3/3 |
   | `noincl` (drop inclusion–exclusion parity) | 3/3 | 3/3 |
   | `flipone` (flip one 2-column bit) | 3/3 | 3/3 |
   | `flipbits` (flip all) | **3/3** | **0/3** — the symmetry |

   `nosign` is a no-op wherever `sgn π = +1`, which is why it is not 6/6. The 39
   rows of this session all have `n2 = 15`, odd, so `flipbits` is live on the real
   data.

**C3 on the real matrix.** Selected entries were recomputed in exact integers by
that evaluator and compared with the seven-prime CRT reconstruction:

| entry | column | bits | exact-ℤ value | matches CRT | time |
|---|---|---|---|---|---|
| `A[0][0]` | `P13-000` | 107 | `-153648258287108961685…114176` | **yes** | 362 s |
| `A[1][7]` | `P13-007` | 101 | `1658137698903574783077…905600` | **yes** | 320 s |
| `A[2][0]` | `P13-000` | 104 | `-133994630495628331758…383552` | **yes** | 363 s |
| `A[20][50]` | `P13-050` | 96 | `71418422601637390598017351680` | **yes** | 367 s |
| `A[38][95]` | `P13-095` | 116 | `-476704445878546998689…809088` | **yes** | 354 s |

All five agree with the seven-prime reconstruction exactly, sign included, and the comparison rejects a `±1` perturbation of any of them. Rows 0 and 1 are rung-12 rows, so their transport exponent is 1 and the check covers the transported case as well as the untransported one. These are integer identities on those entries, not a further modular check.

## 7. What was not done, and what it costs

- **The target half.** No 73-minor, no membership, no spanning claim, no
  `complete_interpolation` certificate. Slot 1 and slot 3 own these. Until they
  land, R6 stays CONDITIONAL and `i_red(13)` is not a number this slot produced.
- **`i_red(13)`.** NOT REACHED. It combines this matrix with slots 1, 3 and 4.
  What this slot contributes to it is the exact source side and the ceiling `≤ 3`.
- **Degree 14.** Not this slot's (slot 7's). **Priced, since the board says the
  memo's "indicative seven hours" is not a validated timing and the rung-13 rate
  is not a rung-14 rate:** all 93 rung-`≤14` rows climb to `n2 = 15`, `n1 = 8`,
  pathwidth 4–6, and the measured evaluator rate is **78 ms/entry** against 65.5
  at degree 13. `93 × 192 × 7 = 124,992` entries → **2.7 core-hours**, about
  **1.4 h on two cores**. That is well inside a session, and the seven-hour figure
  should not be used for planning. `results/b14_02/degree14_pricing.json`.
- **Whether the three relations are genuine.** The strongest evidence available
  without the certificate is the holdout: 20 fresh reducible points, not used to
  build `K`, and all three vectors annihilate every one; the rank over all 116
  points is still 36. That raises confidence and settles nothing.
- **`fast_eval_c` as a sweep instrument.** Measured at **49.5 s per entry** here
  against the DP's 65.5 ms — a factor of 756. Recorded so no one re-discovers it:
  it is a spot-check tool only.

## 8. Defects in the assignment

- **D1 — no dispatch message arrived.** The packet says "Your dispatch message
  states the expected commit and tree… Record both values in your
  pre-registration and check they match what the tag resolves to." No dispatch
  message accompanied this session. The packet's reasoning for keeping hashes out
  of the file is right; the carrier it delegates them to did not arrive. The check
  was discharged against an independent second source instead: `git ls-remote`
  lists `refs/tags/batch14-base` → `4bda8a12…` and `refs/tags/batch14-base^{}` →
  `9898e569…`, agreeing with the local peel. Recommend the dispatch values be
  echoed into a small committed file (a `results/b14_prep/dispatch.json`), which
  has no self-reference problem because it is not the board.
- **D2 — `P13.json` and the board disagree on the number of primes, and the point
  file looks authoritative.** `P13.json` ships `crt_primes` with **six** entries,
  a `crt_modulus` of 1.381× headroom, and `signed_uniqueness_verified: true` —
  true only with respect to its own six-prime modulus. Board §1 requires seven at
  degree 13. **`P14.json` ships seven.** So the inconsistency is specific to
  `P13.json`, and a session reading the pinned contract file alone would use six
  primes and believe uniqueness verified. Recommend amending `P13.json`.
- **D3 — `source.json`'s `literal` field is the wrong degree for this slot and
  for slot 7.** It is climbed to degree **24**, with `exponent` and
  `factorial_scalar` to match. Slot 2 needs degree 13, slot 7 needs degree 14, and
  nothing in either slot's text warns that the field named `literal` is right for
  neither. A session that used it would produce a degree-24 row; combined with an
  inherited degree-13 bound that is a silent bound violation. This session
  recomputes the climb from `native` and uses `literal` nowhere. Recommend the
  slot text say so.
- **D4 — the slot text's `39 × 96` is right, but only because "primary" is
  implicit.** `P13.json` holds **116** points, 96 primary and 20 holdout. The slot
  says "the full `39 × 96` integer matrix" without saying which 96. It is
  unambiguous once the file is open, and the holdout points turned out to be the
  most useful control available for the result; worth naming explicitly so a
  session does not build `39 × 116` and then have no out-of-sample check left.

- **D5 — the packet's own bundle command is the defect `check_delivery.py`
  exists to catch.** The Delivery section says

      git bundle create b14_02_<name>.bundle batch14-base..HEAD

  A range-only bundle carries `HEAD` and no named ref, which is exactly check #5
  in `tools/delivery/check_delivery.py` — "the bundle must carry the NAMED ref,
  not just HEAD", whose own fix text gives the right form,
  `git bundle create <file> <base>..<branch> <branch>`, and whose docstring lists
  HEAD-only bundles as one of the four defects batch 13 shipped repeatedly. Board
  §5 also says "Bundle carries the named ref". The packet contradicts both. This
  delivery uses the named-ref form; a session following the packet literally
  would fail its own gate. Recommend the packet be corrected.

## 9. Reproduction

    git checkout batch14-base && git checkout -b b14-02-source13
    for p in 2147483647 2147483629 2147483587 2147483579 2147483563 2147483549 2147483543; do
      python3 analysis/b14_02_source13.py --residues --prime $p --workers 2
    done
    python3 analysis/b14_02_source13.py --reconstruct
    python3 analysis/b14_02_kernel.py --holdout
    python3 analysis/b14_02_controls.py --prime 2147483647
    python3 analysis/b14_02_controls.py --crt
    python3 analysis/b14_02_direction.py
    python3 analysis/b14_02_exact_check.py --validate --entries 0:0,1:7,2:0,20:50,38:95

Seven-prime sweep: 39 × 96 × 7 = 26,208 evaluations, **≈16 min on two cores**
(140 s per prime). Every run was launched under `timeout` with `ulimit -v
6291456`, pid written to `results/logs/<run>.pid`, and ended only by that
recorded id.

**Declared host resources.** 2 vCPU (Intel Xeon @ 2.10 GHz), 8.0 GB RAM total
(7.4 GB available), one shared 252 GB filesystem. Twelve sessions do not imply
twelve independent memory budgets, and this one was sized on the assumption that
they do not: peak resident use stayed under 400 MB, and the two-worker pool was
chosen to match the 2 vCPU rather than to claim more. `python-flint 0.9.0`,
`sympy 1.14.0`, `numpy 2.4.4`, `scipy 1.17.1` were installed into the container
(only numpy and scipy were preinstalled); gcc 13.3.0 present.

## 10. Files delivered

| path | what |
|---|---|
| `results/PREREG_b14_02.md` | pre-registration, committed before computing |
| `analysis/b14_02_source13.py` | residue sweep + signed CRT reconstruction |
| `analysis/b14_02_exact_check.py` | independent exact-ℤ evaluator (C3) and its sabotage battery |
| `analysis/b14_02_controls.py` | C1, C2, C4, C5 |
| `analysis/b14_02_kernel.py` | left kernel, rank witness, C6, holdout |
| `analysis/b14_02_direction.py` | C7, the discriminating control |
| `results/b14_02/A13_primary.json` | **the exact 39 × 96 integer matrix** |
| `results/b14_02/A13_holdout.json` | the exact 39 × 20 holdout matrix |
| `results/b14_02/kernel_primary.json` | `K`, rank witness, must-fail records, holdout check |
| `results/b14_02/residues_{primary,holdout}_<p>.json` | the 14 residue blocks |
| `results/b14_02/{controls,crt_soundness,direction_control,combined_116,small_shape_validation,binary_provenance,degree14_pricing}*.json` | controls and pricing |
| `results/logs/b14_02_*.log`, `*.pid` | bounded-run logs and recorded pids |

Every stored value matrix carries a `values_are` field beside the numbers naming
the transform, which for all of them is none.

No external announcement or publication was made; none was part of this
assignment.
