# PREREG — B14-02: exact degree-13 source matrix at `P13`

**Session** B14-02, board slot 2 (`flint` host class), `board_numbering: batch14`.
**Model actually running this session** `claude-opus-5` (Claude Opus 5). The packet
named "Claude"; this records what ran.
**Base** tag `batch14-base` → tag object `4bda8a12433c5965a5df82fef35b4c7220b76756`,
commit `9898e56941a7665f231873481dae956f08509995`, tree
`cb688cd3fe454d638f3202e759e2eaa0c629739f`. Both peeled values were obtained twice
and independently: locally via `git log -1 --format=%H batch14-base` /
`--format=%T`, and from the remote via `git ls-remote`, which lists
`refs/tags/batch14-base` → `4bda8a12…` and `refs/tags/batch14-base^{}` →
`9898e569…`. They agree. (See §10 defect D1: no dispatch message carrying the
expected commit and tree reached this session, so the packet's instruction to
check them against the tag was discharged by this second, independent route.)
**Branch** `b14-02-source13`.

Written and committed **before** any matrix entry was computed. Timings quoted in
§7 are pre-registration instrument calibration on 5 of the 39 rows at one point,
and are labelled as such; no row of `A` was reconstructed before this file was
committed.

---

## 1. Question

Two questions, one instrument.

**Q1.** What is the **exact integer** `39 × 96` matrix `A` whose row `i` is the
degree-13 transported LMR source vector `F_{T_i^{up13}}` and whose column `j` is
the primary point `P13-j`?

**Q2.** What is the **exact rational left kernel** of `A` — `K` of size `39 × k`
with `Aᵀ·K = 0`, `rank(K) = k`, `rank(A) = 39 − k` over `ℚ`?

This is a **source-matrix** result. Per the board it is **not** labelled
`i_red(13)` and is not an ideal-relation claim until slot 1's target minor and
slot 4's recount are accepted (`PROVED.md: evaluation_cannot_certify_i_ge_1`).

## 2. Objects, fixed by blob id

| object | path | blob | checked |
|---|---|---|---|
| source | `results/s74/source.json` | `ca17e74393228d9c3d9729e7839f0157cb1e21eb` | ✓ matches board §1 |
| points | `results/b14_prep/points/P13.json` | `76e1f2ed7be8ba85e14ba74cae5be76504f67072` | ✓ matches board §1 |

**Rows (39).** The entries of `source.json` with `rung ≤ 13`: 2 at rung 12 (the
s69 seeds) and 37 at rung 13, matching `birth_profile` `{12: 2, 13: 37}` and the
reconciliation note "exactly 39 rows through degree 13". These are exactly
`entries[0:39]` in file order, verified equal to the filtered set; that file order
**is** the pre-registered row order, and row `i` carries `entries[i]["index"] = i`.

**Transport.** Row `i` is `F_{T_i^{up13}}` where `T_i^{up13}` is the native filling
climbed to degree 13 by the source's own rule — each added degree contributes one
fresh letter occupying `n = 4` one-columns. `source.json`'s stored `literal` field
is climbed to degree **24** and is *not* used; the degree-13 climb is recomputed
from `native`. The transport exponent is therefore `13 − native_degree`: **1** for
the two rung-12 rows, **0** for the 37 rung-13 rows. By the s74 row-system identity
this equals `F_{T_i}(f) · msym_u(f)^{13 − d_i}` with `msym_u = 4!·[s_1^4] f`; that
identity is a control, not an assumption (§6 C2).

All 39 climbed fillings have `h = 9`, `n = 4`, `δ = 13`, `n2 = 15`, `n1 = 4`,
`λ = (21, 17, 2⁷)`, `|λ| = 52 = 4·13`, `ℓ(λ) = 9`. Verified before pre-registration.

**Columns (96).** The `role == "primary"` points of `P13.json` in file order,
`P13-000 … P13-095`. Each is a **reducible** quartic `f = ℓ·c`, `ℓ ∈ [−7,7]^9`,
`c` a cubic with 165 coefficients in `[−7,7]`. The 20 `role == "holdout"` points
are not used for `A` and are reserved (§8).

**Ordering trap, resolved explicitly.** `P13.json`'s `cubic_exponents` is the exact
**reverse** of `wk8_s30_core.exps(3,9)`: its entry 0 is `(3,0⁸)` where
`exps(3,9)[0]` is `(0⁸,3)`. This is `PROVED.md`-adjacent house hazard "two `exps`
orderings exist and they are opposite", and three sessions have paid for it. Every
exponent in this session is resolved by `list.index(...)` in the ordering of the
structure being indexed — never by a literal position. Cross-check already passed:
`24·ℓ_1·c_{(3,0⁸)}` reproduces the file's own `u_symbol` on the points tested.

## 3. Instrument

**Evaluator.** `wk12_s74_dp.dp_eval_compact` (compact-state DP, `wk12_s74_dpc.c`),
which is the path `wk12_s74_columns.ev()` takes first. Measured pathwidth `W ∈
{4,5}` on these fillings, inside its `max_W = 8`. Its packing comes from
`wk11_s69_circuit.dp_pack`.

**Arithmetic.** Seven primes, signed CRT, symmetric reconstruction (§4).

**Exactness chain.** The DP is modular. The exact integer matrix comes from CRT
over seven primes against a bound re-derived in §4. Integer identity is then
established on selected entries by an **independent exact-integer evaluator**
written for this session (§6 C3) — not by a further modular check, which the board
correctly says is not an integer identity proof.

## 4. The height bound — re-derived here, not inherited

`P13.json` ships `source_value_bound` with derivation string
`(9!)^2 * 2^15 * (24*7^2)^degree`. The board instructs the bound to be re-derived
rather than inherited, so the following is derived from the Leibniz definition and
only then compared.

**Step 1 — the symbol bound.** For a filling, `F_T(f) = Σ_σ Π_j sgn(σ_j) Π_l
m_{α_l(σ)}(f)` with `m_α = α!·c_α`. For `f = ℓ·c` with `|ℓ_i| ≤ 7`, `|c_β| ≤ 7`:
`c_α(ℓ·c) = Σ_{i ∈ supp(α)} ℓ_i·c_{α−e_i}`, so `|m_α| ≤ α!·|supp(α)|·49`. Over the
five types of `α` with `|α| = 4`:

| `α` type | `α!` | `\|supp\|` | bound |
|---|---|---|---|
| `(4)` | 24 | 1 | **1176** |
| `(3,1)` | 6 | 2 | 588 |
| `(2,2)` | 4 | 2 | 392 |
| `(2,1,1)` | 2 | 3 | 294 |
| `(1,1,1,1)` | 1 | 4 | 196 |

so `M := max_α |m_α(f)| ≤ 1176 = 24·7²`, attained only at `α = (4,0⁸)`, i.e. by
the `u`-symbol itself.

**Step 2 — the term count.** The bracket sum runs over one bijection per column:
`h!` for `C1`, `h!` for `C2`, `2` for each of the `n2` two-columns, `1` for each
one-column. So there are exactly `(h!)²·2^{n2}` signed terms, each a product of
`δ` symbols.

**Step 3.** `|F_T(f)| ≤ (h!)²·2^{n2}·M^δ`. With `h = 9`, `n2 = 15`, `δ = 13` — the
climbed fillings' actual invariants, all 39 measured, not assumed:

    H₁₃ = (9!)² · 2^15 · 1176^13
        = 35503501195553840281013485855286379513864748625244979200   (185 bits)

The transport needs no separate factor: the climbed filling *is* a degree-13
filling with `n2 = 15`, so the bound applies to the literal row directly, and
`|msym_u| ≤ M` is consistent with it.

**Comparison, after deriving.** This equals `P13.json`'s stored
`source_value_bound` exactly. The inherited figure is **confirmed**, independently.
The board's own `2^15` factor is valid here only because all 39 climbed fillings
have `n2 = 15`; that was checked (histogram: `{15: 39}`), not assumed, and it is
the step that would have broken had any row carried `n2 = 16` or `17`, which the
degree-13 constraint `2n2 + n1 = 34` permits in principle.

**Signed reconstruction needs modulus > 2·H₁₃** (186 bits).

| primes | modulus bits | `modulus / 2H₁₃` |
|---|---|---|
| the 6 in `P13.json` | 186 | **1.381** |
| **7 (this session)** | **217** | **2.966 × 10⁹** |

Seventh prime **`2147483543`** — the next prime below the file's smallest, keeping
every modulus under `2³¹` so the evaluator's `int64` products stay exact. Board §1
predicted "~3×10⁹"; the realised margin is `2.966×10⁹`.

**Pre-registered rule:** reconstruct signed integers **only** from the full
seven-prime modulus, in symmetric range, and only after asserting
`modulus > 2·H₁₃`. A sharper per-column bound `H_j = (9!)²·2^15·M_j^13` with `M_j`
the exact measured maximum symbol at point `j` is recorded alongside, and every
reconstructed entry is checked against `min(H₁₃, H_j)`.

## 5. Decision table

Let `k = dim_ℚ ker_left(A) = 39 − rank_ℚ(A)`.

| outcome | what is established | label |
|---|---|---|
| `k = 0` | `rank_ℚ(A) = 39`, witnessed by one nonzero exact `39×39` minor. Shape gives `rank ≤ 39`, so this is **exact, not a floor**: the 39 transported source vectors are linearly independent, full stop. No completeness certificate needed. | **PROVED** (about the source vectors) |
| `k ≥ 1` | `Σ cᵢFᵢ` vanishes at all 96 primary points for each column `c` of `K`. On a *sampled* point set this is a **ceiling** on independence and a **candidate** relation only. | **MEASURED / CONDITIONAL** on slot 1's 73-minor and slot 4's recount |

The asymmetry is `PROVED.md: rank_floor` and `evaluation_cannot_certify_i_ge_1`:
a nonzero minor bounds rank from **below** and here meets the shape ceiling, so it
is exact; a deficiency bounds it from **above** only.

Either way the deliverable is reported as a **source-matrix** result. `i_red(13)`
is not this number and is not claimed.

## 6. Controls — each with the input that must make it fail

Every control below is run twice: once on the real input, and once on an input
constructed so that a working control **must** report failure. Both results are
reported (`PROVED.md: check_must_be_able_to_fail`, seventh instance was the
integrator's vacuous-census script; this section exists so there is no eighth).

**C1 — forced zero (`negative_control_forced`).** `λ = (21,17,2⁷)` has `ℓ(λ) = 9`.
A weight vector of weight `λ` vanishes at every point whose form has span `< 9`
essential variables. Control points are built with `c` supported on `≤ 7` of the 9
variables and `ℓ` in the same span, giving span `≤ 8`.
*Must-pass:* every one of the 39 rows returns exactly 0.
*Must-fail input:* a full-span primary point, which must return a nonzero row —
otherwise the evaluator has stopped computing (A1's failure mode).

**C2 — transport identity.** For each of the two rung-12 rows,
`F_{T^{up13}}(f) ≟ F_T(f)·msym_u(f)^{1}`; for the 37 rung-13 rows, exponent 0, so
`F_{T^{up13}} ≟ F_T`.
*Must-fail input:* the wrong exponent `24 − d_i` (the stored `literal`'s exponent),
which must disagree — this is the board's "wrong transport" stopping rule made
detectable.

**C3 — independent exact-integer evaluator.** A second evaluator written for this
session, in exact `ℤ`, sharing no code with the DP: it evaluates the bracket by
inclusion–exclusion over row subsets with exact integer determinants, and is itself
validated against the *literal* Leibniz sum (`brute_force_eval`) on small shapes
where the definition is directly computable. Selected entries of `A` are computed
with it and compared to the CRT reconstruction.
*Must-fail input:* a reconstructed entry perturbed by `±1`, which must be rejected.

**C4 — CRT soundness.** Each reconstructed integer is verified to reproduce all
seven residues and to satisfy `|x| ≤ min(H₁₃, H_j)`.
*Must-fail input:* reconstruction from a deliberately insufficient sub-modulus
(three primes, 93 bits < 186), which must produce entries failing the residue or
range check — demonstrating the seven-prime requirement is load-bearing and not
decoration.

**C5 — `u`-nonvanishing.** `u(P_j) = msym_u(f_j) ≠ 0` recorded for every column, as
an integer **and** modulo each of the seven primes. One `u`-zero voids a whole
transported column silently, so this is asserted, not assumed. Already known from
the file to be nonzero as integers (max `|u| = 1176`); the modular check is new
because the seventh prime is new.

**C6 — rank witness.** The claimed `rank(A) = 39 − k` is certified by an exact
nonzero `(39−k)×(39−k)` minor over `ℚ` and by `Aᵀ·K = 0` verified in exact
integer arithmetic, with `rank(K) = k` also witnessed.
*Must-fail input:* a row of `A` replaced by a copy of another row, which must lower
the computed rank by exactly 1 and raise `k` by 1.

## 7. Stopping rules

The board's three, plus the operational ones:

1. **Wrong transport** — C2 fails on any row → that calculation stops; report the
   discrepancy rather than the matrix.
2. **Failed signed reconstruction** — any entry not reproducing its seven residues,
   or exceeding `min(H₁₃, H_j)` → stop.
3. **Failed independent entry check** — C3 disagrees on any selected entry → stop.
4. C1 forced-zero returns nonzero, or C5 finds a `u`-zero → stop.
5. Wall clock: pre-registration calibration measured **65.5 ms** per (row, point)
   for the DP on this host — 4.1 min per prime for 39×96 single-core, ≈29 min for
   seven primes single-core, ≈15 min on the two cores available. `fast_eval_c` was
   also timed at **49.5 s** per entry and is therefore usable only for spot checks,
   never for the sweep — recorded so the next batch does not rediscover it. If the
   seven-prime sweep exceeds 4 h wall clock it is cut to a certified prefix of
   whole columns and the remainder is priced.

Runs are bounded at launch with `timeout` and `ulimit -v`, pid written to
`results/logs/<run>.pid`, and ended only by that recorded id.

## 8. What is deliberately **not** done

- The 20 holdout points are **not** used to build `A`. They are held for an
  out-of-sample check of any left-kernel vector found: a relation that is genuine
  must also annihilate the holdout columns. A relation surviving 96 points but
  dying on the holdout is a sampling artefact, and I would rather find that here
  than have slot 3's verifier find it later.
- No target-side work. No 73-minor, no membership, no spanning claim, no
  `complete_interpolation` certificate. Slot 1 owns those.
- No degree-14 matrix. Slot 7 owns it.
- `i_red(13)` is not computed and not claimed.

## 9. Labelled expectations, stated before computing

- **E1 (high confidence).** `rank_ℚ(A) = 39`, `k = 0`. Reason: s74's birth
  procedure recorded rank 2 through rung 12 and 37 *new* independent directions at
  rung 13 (`birth_profile`), at both house primes, so the 39 are expected
  independent; 96 columns ≥ 39 rows, so no left kernel is forced by shape.
- **E2.** If instead `k ≥ 1`, the first hypothesis is **not** a mathematical
  discovery but an instrument fault — wrong transport exponent, an `exps`-ordering
  slip, or a point set that fails to separate. C1–C6 are ordered to discriminate
  these before any relation is reported.
- **E3.** The re-derived bound will equal the inherited one. *(Recorded before the
  comparison in §4 was written up; it did.)*
- **E4.** Entry magnitudes will run well below `H₁₃`: the bound multiplies worst
  cases that cannot co-occur across all 13 letters. A typical `|A_ij|` at or below
  ~10⁴⁰ against a 10⁵⁵ bound would be unsurprising and is not evidence of error.

## 10. Defects in the assignment, reported as the packet asks

- **D1.** The packet says "Your dispatch message states the expected commit and
  tree… Record both values in your pre-registration and check they match what the
  tag resolves to." **No dispatch message accompanied this session** — the packet
  arrived alone. The check was therefore performed against an independent second
  source (`git ls-remote`) rather than against the dispatch values, as recorded
  above. The packet's own reasoning for keeping the hashes out of the file is
  sound; the gap is that the carrier it delegates them to did not arrive.
- **D2.** `P13.json` ships `crt_primes` with **six** entries and a `crt_modulus`
  of 1.381× headroom, while board §1 requires **seven** primes at degree 13. The
  file also carries `signed_uniqueness_verified: true`, which is true only with
  respect to its own six-prime modulus. A session reading the point file alone and
  trusting those two fields would use six primes and believe it had verified
  uniqueness. The two artefacts are inconsistent; the board governs, and the
  seventh prime is chosen here. Recommend the contract file be amended, since it is
  pinned by blob id and reads as authoritative.
- **D3.** `source.json`'s `literal` field is climbed to degree **24**, and its
  `exponent`/`factorial_scalar` fields are the degree-24 transport. Slot 2 needs the
  degree-13 transport. Nothing in the slot text warns that the field named
  `literal` is the wrong degree for this slot; a session that used it would compute
  a degree-24 row and get a bound violation, or worse, silently wrong values if it
  also inherited the degree-24 bound. Flagging because slot 7 has the same shape at
  degree 14 and the field is right for neither.

---

*Pre-registered by B14-02 before computation. Dated addenda permitted, committed
before the measurements they govern.*
