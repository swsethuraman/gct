# B23-01 — The second-prime test: can the `Q` form of the five-row identity be refuted?

Batch 23, slot 01, Phase 1. Worktree `work/batch15_workers/B15-01`, branch `b15-01-ci159`. Claude Code
(Opus 5), default permission mode. Recorded at 2026-09-18T18:44:32Z, before any write:
`git rev-parse HEAD = 53bdb31e3042acae9464f9025be355ae699a2485` (equal to the brief), `HEAD^{tree} =
af3bd8c3596bdc3d3b7431546b236716630953df`, and `git status --porcelain` showed no tracked change (only
the known untracked `results/` residue). Read-only git throughout; no commit, no push, no stash.

**Inputs** (read-only; each hash checked against its pin before this was written):
- `docs/b22_01_report.md`, sha256 `e2adc0f9…`, and `results/b22_01/MANIFEST.json`, sha256 `1931ab8f…`,
  both at `53bdb31e`, both equal to the working tree.
- `results/b22_01/p2_basis.json`, sha256 `7162d852…`, holding the certified points; bound by that
  manifest.
- `docs/b22_10_review.md` at `2efb7aaf` (B15-10), sha256 `86d8caf9…`: the test design is its §4, the
  gates its §9.
- The pinned runner/carrier as B20-01's manifest binds them. They are fetched here by commit and path,
  with `git show`; nothing under `results/b20_01/`, `results/b21_01/` or `results/b22_01/` is written.

## 0. What this can and cannot establish

- **It can refute the `Q` form.** The test computes, modulo a second prime `P₂`, integer quantities:
  3 × 3 minors of exact integer rows. A nonzero residue proves that the integer is nonzero, so
  `rank(C|_U) = 3` over `Q`, and the five-row identity is false over `Q`.
- **It cannot prove the `Q` form.** If every minor vanishes modulo `P₂` as well, the identity is
  CERTIFIED-modular at two primes. That is evidence: not a proof, not a floor, not a lift, and not
  grounds for the label CERTIFIED. A modular rank bounds the rational rank from below only.
- **What it leaves untouched in either branch.** The `F_P` statement at `P = 524287` (B22-01
  B22-01.14/.16), Theorem M, and the certified 70-point set (B22-01 B22-01.6–.7).
- **The four achievements.** Nothing here is a gap, an equation nonzero on padding, a separation, or a
  cell. In this cell `D = -1`, and no positive multiplicity gap is possible in either branch.
- **G18.** Everything is producer-only.

## 1. Pre-registration (saved and hashed before any computation; G25: the hash is an argument of the pilot, which refuses to run on a mismatch and writes the hash into its own output first)

### 1.1 The second prime

**`P₂ = 524269 = 2^19 − 19`.** Why this prime:
- *Overflow.* `P₂ < P`, so the carrier's overflow guarantee `4^12 · P₂² < 4^12 · P² < 2^63` holds
  unchanged. No other constant of the carrier depends on `P`: its only literal occurrence is the
  line `P = 524287`, and its docstring's arithmetic claim is monotone in `P`.
- *Size.* It is close to `2^19`, so the runner's cost is unchanged. Heuristically, a given nonzero
  integer is divisible by it with chance about `1/P₂` — but this is not a probability claim about the
  result (see §0).

**Primality** is checked twice, before any evaluation:
1. the patched carrier's own `assert isprime(P)` (sympy) runs at import;
2. the pilot checks by trial division up to `√P₂ < 725`.

**What `P₂` must not divide, and how each is checked.**
- *The Vandermonde determinant of the nodes `u = 1..5`.* It is `∏_{i<j}(j − i) = 288 = 2^5·3^2`, so the
  condition is `P₂ > 3`; the pilot also asserts it. This is the only divisor the refutation depends
  on: with it, `[u^11]` and `[u^12]` mod `P₂` are the reductions of the true integer coefficients.
- *`det(g)` of the slice forms used in control 2.* Asserted nonzero mod `P₂` in the pilot.
- *Nothing else.* The certification of B22-01 is a statement over `Q` (a nonzero residue mod `P` of an
  integer determinant), and `P₂` plays no role in it. The sealed values and `(α, β)` are residues
  modulo `P`. They are never reduced or compared modulo `P₂`, so no divisibility condition on `P₂`
  arises from them.

**The artifact** (G8/G11). The pilot materialises a new carrier under `results/b23_01/pinned_P2/`. It is
the pinned carrier bytes (`8670040e…` at `75ddb900`) with exactly one line changed,
`P = 524287  # 2**19 - 1, Mersenne prime` → `P = 524269  # B23-01 second prime 2**19 - 19`, and the pilot
asserts that the line occurs exactly once. The runner copy is the pinned runner (`33c81c96…` at
`82633a60`) with B20-01's one-line path patch, pointing at that carrier. Both sha256 are recorded.
The unmodified pair is materialised byte-identically under `results/b23_01/pinned_P1/`, and the runner
there is asserted equal to `e7ba4ff7…`.

**Integer points, not residues.** The certified points are the integer matrices `Z_1, Z_2, Z` recorded in
`p2_basis.json`, with entries in `[0, 524287)`. `ν_k` is the integer matrix `(ν_k)_{1+i,1+j} = −ε_{ijk}`.
At `P₂` every entry is reduced from these integers. B20-01's stored `NU` holds `−1` as `524286`, a
residue mod `P`; it is **not** used at `P₂`, because it would be a different integer tuple, off the
flag locus.

### 1.2 The test, exactly as B22-10 §4 specifies it (not redesigned)

B22-10 §4, verbatim: *"Patch the runner's module constant to a second prime `P_2` as a new, hashed
artifact (G8/G11). Evaluate `q_3, q_7, n02` at 3 of the certified points (`3 × 15 = 45` evaluations).
A nonzero `3 × 3` minor mod `P_2` of those integer rows proves `rank(C|_U) = 3` over `Q` … A zero minor
is MEASURED evidence at two primes and proves nothing."*

- **Points.** The certified points `p_1, p_2, p_3` (`points[0..2]`, labels `cert_00, cert_01, cert_02`),
  chosen now as the first three.
- **Rows.** At each point, the tuple `(Z_1, Z_2, Z + u ν_1, u ν_2, u ν_3)` mod `P₂`, `u = 1..5`. Each of
  `q_3, q_7, n02` is evaluated with the `P₂` runner (5 × 3 = 15 evaluations per point, 45 in all), and
  the Vandermonde solve in degrees `8..12` mod `P₂` gives the degree-11 row `[u^11]` and the degree-12
  row `[u^12]` (the nodes determine all five coefficients and leave nothing free, G22). That makes six
  rows × three columns `(q_3, q_7, n02)`.
- **Minors.** All `C(6,3) = 20` `3 × 3` minors of the `6 × 3` matrix, mod `P₂`, by row elimination on
  Python integers, plus the rank mod `P₂`.
- **Why 45 evaluations suffice.** They suffice for the refutation direction only. Any single nonzero
  minor is a complete certificate, because the rows are reductions of integers. They are not meant to
  establish anything in the other direction, and they do not: six rows are not an injective set, and
  a zero minor at `P₂` is compatible with rank 3 over `Q`.
- **Descriptive only** (MEASURED; decides nothing and moves no label). If the rank mod `P₂` is 2:
  - record the relation `(α₂, β₂)` mod `P₂` and the degree-12 ratios mod `P₂`;
  - combine with `(α, β)` mod `P` by CRT and attempt a rational reconstruction modulo `P·P₂`. A
    reconstructed fraction is a candidate, not a lift, and is reported as such.
- **Internal consistency, after the test** (if time remains): a sixth node `u = 6` at `p_1` for the three
  vectors, with the solve in degrees `7..12`. Its `u^7` coefficient must be `0` (Theorem A(v): only
  `u^8..u^12` occur).

### 1.3 The controls (G21), run before any new evaluation

The brief asks for the six sealed values and a subset of the 19 recorded points "replayed at `P₂`". **As
literally written, that cannot be done.** Those values are residues modulo `P = 524287` of integers
nobody has computed. Their residues modulo `P₂` are unknown, and no equality at `P₂` can be tested
against them. I am not redesigning B22-10's test; I record the defect in the control specification and
run the controls in the only form in which each is an identity it tests:

1. **Six sealed values, at `P`, with the unmodified pinned pair, `det(g)^{-4}` normalisation (45
   evaluations).** At P6 point 0 (which is one of the recorded points: rows `full_P6pt0_d11/d12`), the
   slice form `g` (B20-01's `slice_form`, mod `P`), `F_1 + F_2 + F_3` and the top by five nodes. The
   identity tested is `slice = det(g)^4 · full`, and the script derives `full = det(g)^{-4} · slice`
   (B21-10 R3; never `det(g)^4`). **Pass:** all six equal `86170, 71919, 226580; 376209, 469277, 41046`.
   This controls the runner code the `P₂` artifact is made from; the artifact differs from it in one
   line.
2. **`det(g)^{-4}` normalisation at `P₂` (6 evaluations).** At P6 point 0 reduced mod `P₂`, two slice
   forms computed mod `P₂`: `g₁` from the elimination, and `g₂ = g₁` with row 1 doubled and row 1 added
   to row 3 (still a slice form: `v u_1 = 0`; `det g₂ = 2 det g₁`). On the tuple
   `(Z_1, Z_2, ν_1, ν_2, ν_3)`, `D = D_3` exactly, so one evaluation per vector gives the top.
   - Identity: `det(g₁)^{-4} top(g₁) = det(g₂)^{-4} top(g₂)` for `q_3, q_7, n02` — the full `z^{[12]}(Y_0)`
     mod `P₂` is `g`-independent.
   - Teeth: the inverted recipe `det(g)^{+4}` must **fail** (it would need `2^8 ≡ 1 mod P₂`).
   - **Pass** = identity true and teeth fail, for all three vectors.
3. **Recorded rows (arithmetic, no runner).** The relation residual `n02 − α q_3 − β q_7` mod `P` on every
   recorded row (the 30 rows B22-01 §4.1 replayed). **Pass:** all zero.

**Stop rule.** If any control fails, the pilot writes the failure, **does not run the test**, and the
result is (c).

### 1.4 Budget

One wrapped pilot, `b23_01_p1_secondprime`, 60 s / 512 MiB, `PYTHONDONTWRITEBYTECODE=1`, JSON written
after every stage, internal deadline 55 s. The test does not start unless 30 s remain. Runner
evaluations: 45 (control 1) + 6 (control 2) + 45 (test) + 3 (sixth node, optional) = 99, about 45 s at
the B22-01 rate of 0.43 s per evaluation. **No other launch.** If the test cannot complete in this
pilot, the result is (c) with the price stated. No exceedance is approved, and none is used. Before
launch, `..\B15-02\results\logs\b23_02_*.pid` and the `python.exe` process list are checked.

### 1.5 The three transcription sentences (one is copied verbatim into §5)

- **(a) A nonzero `3 × 3` minor at `P₂`.** *At `P₂ = 524269` the minor of rows [R₁, R₂, R₃] of the integer
  evaluation rows of `(q_3, q_7, n02)` at the certified points is [value] ≢ 0 mod `P₂`; the rows are
  reductions of integers (Vandermonde determinant 288, `P₂ ∤ 288`), so the integer minor is nonzero and
  `rank(C|_U) ≥ 3`, hence `= 3`, over `Q`. The five-row identity is **REFUTED over `Q`**, the `Q` form of
  `arc_target` Prop. 7.1 is dead, and the diagnostic closes negatively. What survives unchanged: the
  identity modulo `P = 524287` (CERTIFIED-modular, B22-01), Theorem M, and the certified 70-point set.*
- **(b) Every `3 × 3` minor vanishes at `P₂` as well.** *All twenty `3 × 3` minors of the six rows vanish
  modulo `P₂ = 524269`. The identity is CERTIFIED-modular at two primes. **This is evidence, not a proof,
  and the label does not move**: it is not a floor, not a lift, and not grounds for writing "CERTIFIED".
  Rank 3 over `Q` remains possible, exactly when both `P` and `P₂` divide every `3 × 3` minor of the exact
  integer rows at the points used. The `Q` form stays OPEN, and the `Q` form of Prop. 7.1 stays
  CONDITIONAL.*
- **(c) Inconclusive.** *[A cap hit / a control failure: which control, which values / a runner
  disagreement: which.] No new evaluation is interpreted, and nothing about the `Q` form is concluded.
  This is not (b).*

---

*Everything below §1 was written after the pilot. §§0–1 are byte-identical to the snapshot
`e265f969…` (checked at sealing), and the pilot recorded that hash as its first act (G25): its
output's `preregistration` field was written at 0.0003 s elapsed, before any artifact, import of
numpy, or evaluation, and the pilot was launched with the hash as a required argument it verified.*

## 2. Controls (all before the test; all passed)

The numbers are copied from `results/b23_01/p1_secondprime.json`.

| control | what it tests | outcome |
|---|---|---|
| **c1**: six sealed values at `P`, unmodified pinned pair (`8670040e…` carrier, `e7ba4ff7…` runner, both re-materialised byte-identically under `results/b23_01/pinned_P1/`), 45 evaluations | `slice = det(g)^4 · full` at P6 point 0, solved in the script as `full = det(g)^{-4} · slice` (`det g = 199728`, `det(g)^{-4} = 252079`) | identity true in both degrees for all three vectors; `86170, 71919, 226580; 376209, 469277, 41046`: **6 of 6**; top equal across `k` |
| **c2**: `det(g)^{-4}` normalisation at `P₂` (6 evaluations) | g-independence of `det(g)^{-4} · top(g · Y_0)` for two slice forms mod `P₂` (`det g₁ = 49930`, `det g₂ = 99860 = 2 det g₁`) | identity true for `q_3, q_7, n02`; **the inverted recipe `det(g)^{+4}` fails for all three** (the test bites); full `z^{[12]}(Y_0)` mod `P₂` = `150759, 332281, 503044` |
| **c3**: recorded rows (arithmetic, mod `P`) | relation residual `n02 − α q_3 − β q_7` | **30 of 30 rows zero** |

What c1 and c2 do and do not establish. c1 shows that the code the `P₂` artifact was made from
reproduces the sealed record. The `P₂` artifact differs from it in exactly one line (recorded in the
output: `P = 524287  # 2**19 - 1, Mersenne prime` → `P = 524269  # B23-01 second prime 2**19 - 19`;
carrier sha256 `16a9aa75…`; runner bytes unchanged, `e7ba4ff7…`). c2 shows that the `P₂` runner
satisfies Theorem A(i)'s covariance with the correct exponent. No control compares a value at `P₂`
with a recorded value, because none exists (§1.3). The recorded points are not "replayed at `P₂`" in
any sense stronger than this, and I do not claim otherwise.

## 3. The test

`P₂ = 524269`, prime (trial division, and the carrier's `isprime` assertion at import), `P₂ ∤ 288`,
`P₂ < P`. At the certified points `cert_00, cert_01, cert_02`, each tuple was built from the integer `Z`'s
and the integer `ν_k = −ε`, reduced mod `P₂`: 45 evaluations with the `P₂` runner. The six rows mod `P₂`,
as columns `(q_3, q_7, n02)`:

| row | `q_3` | `q_7` | `n02` |
|---|---:|---:|---:|
| `cert_00` d11 | 27584 | 18096 | 154260 |
| `cert_00` d12 | 452721 | 62665 | 501156 |
| `cert_01` d11 | 106259 | 105559 | 231269 |
| `cert_01` d12 | 299003 | 30949 | 169404 |
| `cert_02` d11 | 354414 | 320659 | 412386 |
| `cert_02` d12 | 444066 | 497271 | 511044 |

- **All 20 `3 × 3` minors are `0` mod `P₂`.** The rank mod `P₂` is 2 (degree-11 rows: 2; degree-12 rows: 1).
- **Consistency after the test.** A sixth node `u = 6` at `cert_00` (3 evaluations; degrees `7..12`) gives
  `u^7` coefficient `0` for all three vectors, and `c_11`, `c_12` equal to the five-node values.

**Descriptive (MEASURED; decides nothing; pre-registered in §1.2).**
- The relation mod `P₂` is `n02 = 109562 q_3 + 163393 q_7` (residual 0 on all six rows).
- The degree-12 ratios mod `P₂` are `(14427, 266949)` at all three points.
- CRT with `(α, β)` mod `P`, followed by rational reconstruction modulo `P·P₂ = 274867421203` (bound
  `√(M/2) ≈ 3.7·10^5`), returns

      alpha ≡ 737/646,   beta ≡ −1421/969      (i.e. (2211, −2842)/1938 over the common denominator 1938 = 2·3·17·19),

  each consistent with both residues.

**Why the candidate is interesting, and what it is not.**
- *Why interesting.* Numerators and denominators near `10^3`, from a modulus near `3·10^11`, are far
  smaller than a reconstruction from unrelated residues would typically give. Heuristically, residues
  not coming from a small fraction land on one of height `<= 1000` with frequency of order `10^{-5}`
  per coefficient. That is a heuristic about typical residues, not a probability of anything
  established here.
- *What it is not.* It is **a candidate `(α*, β*)`**, not a lift and not a proof. Under the hypothesis
  of the `Q` form, `α*, β*` are fixed rationals whose denominators divide the `2 × 2` integer minor of
  `arc_target` Prop. 7.1. The reconstruction is what that hypothesis would predict, but nothing here
  makes the hypothesis true.

**Provenance note.** `arc_target` C3 and `final_arc_diagnostic` record that `(265391, 275398)` has "no
small-height rational lift (bound 2000)". The definition of height used there is not on the record: I
found no search code at `82633a60`, so it is UNREAD.
- If it bounds each coefficient separately, `737/646` (≡ `265391` mod `P`, verified) contradicts it.
- If it bounds a common-denominator form `max(|a|, |b|, d)`, the candidate's form `(2211, −2842; 1938)`
  has height `2842 > 2000`, and there is no conflict.

I record this and do not resolve it.

## 4. Exact scope

- **Established.** At `P₂ = 524269`, the six integer evaluation rows of `(q_3, q_7, n02)` at three
  certified flag points have rank 2 modulo `P₂`, and every `3 × 3` minor is divisible by `P₂`. Together
  with B22-01, the same integer rows (at those three points; at all 70 for `P`) have every `3 × 3` minor
  divisible by `P` and, at these three points, by `P₂`.
- **Not established.**
  - Rank 2 over `Q`. Six rows are not an injective set, and a modular vanishing is never an upper
    bound on the rational rank.
  - Anything at `P₂` about the other 67 points.
  - The polynomial identity modulo `P₂` (the certificate's injectivity mod `P₂` was not computed and was
    not part of the design).
  - That `737/646`, `−1421/969` are the coefficients.
- **Unchanged.** B22-01's CERTIFIED-modular statement at `P`, Theorem M, and the certified set.
- **The four achievements.** Nothing here is a gap, an equation nonzero on padding, a separation or a
  cell. `D = -1`.
- **G18.** Producer-only: one session, one lineage.
- **G24.** No dimension is stated in this report.

## 5. Ledger and transcription

**Transcription sentence (b), verbatim from §1.5:**

> *All twenty `3 × 3` minors of the six rows vanish modulo `P₂ = 524269`. The identity is
> CERTIFIED-modular at two primes. **This is evidence, not a proof, and the label does not move**: it is
> not a floor, not a lift, and not grounds for writing "CERTIFIED". Rank 3 over `Q` remains possible,
> exactly when both `P` and `P₂` divide every `3 × 3` minor of the exact integer rows at the points used.
> The `Q` form stays OPEN, and the `Q` form of Prop. 7.1 stays CONDITIONAL.*

One precision on the words "CERTIFIED-modular at two primes". At `P` the statement is a polynomial
identity (B22-01, through the certified injective set). At `P₂` it is the vanishing of the 20 minors at
three points only. The label of the identity remains **CERTIFIED-modular** (B22-01, B22-10), and
nothing here moves it.

| id | statement | label | basis |
|---|---|---|---|
| B23-01.1 | Session state recorded before any write: HEAD `53bdb31e`, tree `af3bd8c3`, no tracked change; read-only git | VERIFIED | header |
| B23-01.2 | §§0–1 saved as `results/b23_01/preregistration_snapshot.md` (`e265f969…`) before any computation; the pilot verified the hash as a required argument and wrote it first (0.0003 s); §§0–1 unchanged at sealing | VERIFIED (G25 satisfied) | §2 note; the pilot's output |
| B23-01.3 | The brief's "six sealed values and recorded points replayed at `P₂`" is not testable as written (recorded values are residues mod `P`); controls run as the identities they test (c1 at `P`, c2 at `P₂`, c3 arithmetic) | specification defect, recorded before the run | §1.3 |
| B23-01.4 | c1: six sealed values reproduced at `P` with `det(g)^{-4}`, 6 of 6 | PASSES | §2 |
| B23-01.5 | c2: `det(g)^{-4}` normalisation at `P₂` is g-independent for all three vectors; the inverted recipe fails | PASSES (the test bites) | §2 |
| B23-01.6 | c3: 30 of 30 recorded rows with relation residual 0 | PASSES | §2 |
| B23-01.7 | The `P₂` artifact differs from the pinned carrier in exactly one line; the runner bytes are unchanged | VERIFIED (hashes recorded) | §2 |
| B23-01.8 | At `P₂ = 524269`, all 20 `3 × 3` minors of the six rows at `cert_00..02` vanish; rank 2 | MEASURED (the data) | §3 |
| B23-01.9 | **Transcription (b): CERTIFIED-modular at two primes; evidence, not proof; the label does not move; `Q` form OPEN; Prop. 7.1's `Q` form CONDITIONAL** | **ruling** | §5 |
| B23-01.10 | The `Q` form is **not refuted** by this test | MEASURED (a refutation was possible and did not occur) | §3 |
| B23-01.11 | Sixth-node consistency: `u^7` coefficient `0`, and `c_11`, `c_12` reproduced | PASSES | §3 |
| B23-01.12 | Candidate `(α*, β*) = (737/646, −1421/969)` from CRT + rational reconstruction mod `P·P₂` | **MEASURED candidate only**: not a lift, not a proof | §3 |
| B23-01.13 | Earlier "no lift of height ≤ 2000" (definition of height UNREAD): contradicted by `737/646` under a per-coefficient reading, consistent under a common-denominator reading | provenance note, unresolved | §3 |
| B23-01.14 | Nothing here is a gap, a cell, an equation nonzero on padding, or a separation | standing | §0 |
| B23-01.15 | Everything is producer-only | G18 | — |

**For the next board, not for me:** a third prime is not run here. If the candidate holds, then
`1938 n02 − 2211 q_3 + 2842 q_7` is an explicit integer combination predicted to lie in `ker C`, and an
exact route could aim at it directly.

## 6. Resources, receipts, manifest

| run | exit | wall | peak job memory | runner evaluations |
|---|---|---|---|---|
| `b23_01_p1_secondprime` | 0 | 45.452 s | 267.1 MiB (280088576 B) | 99: 45 at `P` (c1), 54 at `P₂` (6 c2 + 45 test + 3 sixth node) |

- **Launches and caps.** One wrapped launch, of the one permitted; no cap hit (76% of the wall cap, 52%
  of the memory cap). The runner wall was 19.3 s at `P` and 22.6 s at `P₂`. Interpreter
  `..\B15-02\.venv\python.exe` (Python 3.12.10); `PYTHONDONTWRITEBYTECODE=1`; the receipt shows
  `job_object_enforced: true`.
- **Before launch.** `..\B15-02\results\logs\b23_02_*.pid`: none existed. `python.exe` processes: none.
- **Unwrapped, non-numerical.** Read-only `git show` / `rev-parse` / `status` / `grep` / `check-ignore`;
  `sha256sum`; `tasklist`; an `ast` parse check; JSON field inspection; the seal script. No unwrapped
  numerical run (G19).
- **Receipts.** `results/logs/b23_01_p1_secondprime_resources.json` and `.pid`. **Negation missing for
  `b23_01_`**: `git check-ignore -v` reports the `.pid` ignored by `.gitignore:51` (`results/logs/*.pid`).
  Left to housekeeping.
- **Write footprint (all new).** `docs/b23_01_report.md`, `analysis/b23_01_p1_secondprime.py`,
  `results/b23_01/` (snapshot, `p1_secondprime.json`, `pinned_P1/`, `pinned_P2/`, `MANIFEST.json`,
  `SEAL_LOG.txt`), and the two receipts. Nothing under `results/b20_01/`, `results/b21_01/` or
  `results/b22_01/` was written; they were read against their hashes, and their manifests are
  re-hashed at sealing.
- **Manifest.** `results/b23_01/MANIFEST.json` binds every file above, with sha256 and bytes, plus the
  pinned inputs. `SEAL_LOG.txt` prints every count it writes. Neither binds itself, and this report
  does not name its own hash.
- **G9′.** No tool memory was used as an input. Every value above comes from a pinned file or from the
  pilot's output.

**Deviations.**
1. The controls could not be run "at `P₂`" as literally specified; recorded in §1.3 before the run.
2. The descriptive CRT reconstruction and the sixth-node check go beyond B22-10's bare design. Both
   were pre-registered (§1.2), decide nothing, and use 3 extra evaluations. The test itself is exactly
   B22-10's: three certified points, 45 evaluations, twenty minors.
