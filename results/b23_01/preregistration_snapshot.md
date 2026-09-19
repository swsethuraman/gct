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
