# R27-02: cross-lineage review of B27-02 (Astra), producer tip `35eeff49`

Reviewer: Claude Code (Opus 5.5), 2026-09-23, branch `b27-02r`. **Verdict: ACCEPT outcome 3**
(rejection of the single candidate), with one clerical REPAIR and one added finding. The finding
is that B26-02's padding witness `p4` is itself a literal determinant point (§4). Achievement
level: none of the four. The binding constraint is unchanged.

## 0. Preflight and bindings (READ, administrative)

- **Prior exposure: none.** I did not produce B27-02 and saw none of it during production. I did
  not read B27-01's payload.
- **Brief hashes (raw SHA-256).** They match `BATCH27_BOARD.md`:
  - `B27_COMMON.md`: `891e3ca872bc795b6f943ac89f55112573803f006e0208940dd6cad1f750d6ee`
  - `R27-REVIEWS.md`: `916de53ab8c31c3d4242a84d8a894ce9ceecc75d76ef83dea8d4d87b3edddaa9`
  - `BATCH27_BOARD.md`: `b0bc2501aba62d49b91862d821232ac1b9904480057a8dcdb4cbc03fbd86efec`
  - `B27-02.md`: `8dbb0a0d1bd56fd5a1c5995254cf6c200b3f45698635f3f3f3daf6cbd42635d5`
- **Branch and worktree.** Branch `b27-02r`. HEAD at start was
  `fcff7eeaa491aab4a3b1d1ba1161c24a89dae818`, which is the PART 25 receipt row for `b27-02r`. No
  untracked files. The output paths were absent.
- **Producer tip.** `origin/b27-02` = `35eeff499f0336358630d4d35e61bb76d2ab8edf`, a single commit
  on setup `6dea55ec`.
  - It touches exactly 15 paths, all inside the slot's output patterns.
  - `results/b27_02/MANIFEST.json` at the tip: raw SHA-256
    `bb55a4e55ed61306d2c5a8d84a4fe7a5488257930c3bee30861237d767ebe40a`, 3324 bytes, blob
    `be9230ff`.
  - All 14 payloads match the manifest in bytes, raw SHA-256 and blob OID, read from
    `git show 35eeff49:<path>`.
- **Producer premises.** I re-hashed these committed blobs; they equal the producer's
  `INPUT_BINDINGS.json`. Each hash names the exact blob payload, with no newline conversion.
  - READ: `a7b7c19f:docs/b26_10c_review.md` `3b64b41f…` (Part 2).
  - READ: `cdf6839c:docs/b26_02_review.md` `14de8f0f…` (items 3, 5; §4).
  - `f7967d17:results/a26_03/PROOF.md` `ff9507bb…`: its hash is confirmed. Its content is UNREAD
    by me, and the `K_Q` it supplies is re-derived below.
- **Fallback timing (READ).** `b27-01`'s first payload commit `01f78eb2` is dated
  2026-09-23T04:08:03Z. B27-02 committed at 03:59:11Z. So using the `p4` fallback in 2d was
  correct under the brief.

## 1. Claim check

In each row, H is my own hand derivation and C is my COMPUTED re-run (§3).

| # | producer claim (level) | my check | verdict |
|---|---|---|---|
| 1 | 2a: candidate `f = f_T1 − 567 f_T2`, shape (24,4,4,4,4), content 10×4 (HAND) | H+C: content, shape and distinct labels hold. Both tableaux pair every column with an identical, same-order partner, so `ε_T = +1`. Signed coefficients +1 and −567 are mixed, which meets B26-10C §2.4 repair 2(b), READ. | ACCEPT |
| 2 | `f_T1 = a^5 F`, `f_T2 = H^2`, `H = 5! det C` (HAND) | H: labels 6–10 in T1 see only coordinate 1, giving `a` each. In T2 each label 1–5 has two legs on `e1`, giving `C` on the others, and the two ε's give `5! det C`. C: `H` computed as a direct double-ε sum equals `120 det C` at all four points. | ACCEPT |
| 3 | highest weight in this convention (HAND) | H: a lower-unitriangular change of evaluation vectors fixes the top-h minors. The torus weight is (24,4,4,4,4). Not load-bearing. | ACCEPT |
| 4 | `F(Q^2) = 11200/9` by the cycle-type table (HAND) | H: the scaled tensor is δδ+δδ+δδ. A nontrivial cycle of σ gives 2 consistent choices, and fixed points give `a_k = Σ_τ 3^{fix τ}`. I re-derived all seven rows: 872+760+180+400+80+180+48 = 2520, and 120·2520/3^5 = 11200/9. C: a general algorithm (fix column 1 by label symmetry; column 4 as a 5×5 determinant; no even-support shortcut) gives 11200/9. | ACCEPT |
| 5 | `H = 5α²β³/27` on `αA²+βAB+γB²`; `H(Q²)=40/27`, `H(D4)=H(p4)=5/27` (HAND) | H: `C = diag(α, α/3, β/6, β/6, β/6)`. C: agrees. | ACCEPT |
| 6 | 2c: `f(Q²) = f(D4) = 0`; both literal determinants (HAND) | H: both Pfaffians are correct (`zw+uv+t² = Q`, `zw+uv/2+t²/2 = A+B/2`), with `x1` coefficient `diag(J,J)` and determinant 1. `F(D4) = F(Q²)/64` by weight. C: `det` of both skew pencils computed literally. **Note:** 2c passes *by construction*. The 567 was fitted at `Q²`, and `D4` then follows by the diagonal weight. The producer says this openly; the pass carries no evidential weight. | ACCEPT |
| 7 | 2b: `f(p4) = −175/9`, `f(p4 + B²/4) = f(D4) = 0`, so `t ↦ f(p4 + tB²)` is nonconstant (HAND) | H: `F(p4) = 0` by the linear-factor pigeonhole (five `l`-legs, four alternating columns). C: `F(p4) = 0` computed directly, without that argument, and `p4 + B²/4 = D4` as polynomials. | ACCEPT |
| 8 | 2d: `p4 = z·per_3(Y)` literal actual padding with `Y` nonsymmetric; `f(p4) ≠ 0` (HAND) | H: `M(−I+J/2) = I`, and `per Y = w·rᵀMb = wQ`. C: `per_3(Y)` expanded literally with linear entries over Q(i); `Y ≠ Yᵀ`. **True as stated, but see §4.** `p4` is also a determinant point, so this nonvanishing carries no separation content. | ACCEPT (scope note §4) |
| 9 | universal identity false: `E = det L_E = x1²(x1²+x1x2−B)`, `x1` coefficient `I4`, `f(E) = −175/256` (HAND) | H: Schur complement gives `x1³(x1+x2) − x1²B`. `C(E) = [[1,1/4],[1/4,0]] ⊕ (−1/6)I3`, `det = 1/3456`, `H = 5/144`, `F(E) = 0` (the `x1²` factor). C: `F(E) = 0` computed directly, and all values agree. | ACCEPT |
| 10 | span obstruction: `(a^5F, H²)` at `(Q², E)` has determinant 4375/2916 (HAND) | H: `(11200/9)(25/20736) = 4375/2916`. C: agrees. This is scoped to that 2-dimensional span only, as the producer states. | ACCEPT |
| 11 | registered outcome 3; no achievement among the four (HAND) | Consistent with 1–10 and with §4. | ACCEPT |
| 12 | COMPUTED runs 1–2 (output hashes `a4ae4176…`, `92d8fbe9…`) | C: re-run from committed blobs. **Both output hashes match byte for byte.** | ACCEPT |
| 13 | report table, raw SHA-256 of `B27-02.md` (READ) | The report prints a 62-character value that drops one `f3`. `INPUT_BINDINGS.json` and the board have the correct 64-character hash. | REPAIR (clerical): read `8dbb0a0d…35f3f3f3daf6cbd42635d5` |

## 2. Heaviest-scrutiny items

B27-02 does not claim a coefficient equation that is nonzero on padding (outcomes 1–2), so the
brief's heaviest-scrutiny rule is not triggered. I nonetheless checked the actual-padding point
literally (row 8) and the determinant-side counterexample (row 9) in exact arithmetic, and
re-derived both by hand.

## 3. What I computed (COMPUTED; receipt in `results/b27_02r/RESOURCE_RECEIPT.md`)

- **Runs 1–2:** the producer's own replays, re-run. Their output hashes match.
- **Run 3:** `analysis/b27_02r_check.py`, which shares no code with the producer.
  - Every quartic is built from its literal matrix: two skew pencils, `z·per_3(Y)`, and `L_E`.
  - Tensor entries come from the expanded coefficients.
  - `F` is computed for arbitrary quartics, not only even ones, and `H` by a direct double-ε sum.
  - It also checks the tableau content, shape and pairing.
  - Every value in the producer's table is reproduced: `F`, `H`, `f` at `Q²`, `D4`, `p4` and `E`;
    567 = `F/H²` at `Q²`; and span determinant 4375/2916.
- **Run 4:** `analysis/b27_02r_p4det.py`, the §4 certificate.

## 4. Added finding: `p4` lies in the determinant variety

**HAND, replayed COMPUTED (run 4).** Let `M = [[w, −u, −t], [v, z, 0], [t, 0, z]]`. Expanding
along the first row:

    det M = w·z² + u·(vz) − t·(−zt) = z(zw + uv + t²) = zQ.

With `L = diag(w, M)`, a 4×4 matrix of linear forms in `x1..x5` over Q(i),

    det L = w·z·Q = A(A+B) = p4,

and the `x1` coefficient of `L` is exactly `I4`. So B26-02's actual-padding witness `p4` is a
literal point of the normalized determinant chart. For `n > 4`, `diag(z I_{n−4}, w, M)` gives
`p_n = z^{n−4} p4` the same way (HAND).

**Consequences** (HAND, scoped):

1. **A second rejection.** `f(p4) = −175/9 ≠ 0` already shows that `f` is not a determinant
   equation, independently of `E`. Row 9 and the span obstruction remain correct, and `E` is
   still a useful point, since `F(E) = 0` isolates `H²`.
2. **No separation at `p4`, for any candidate.** No function that vanishes on the determinant
   variety can be nonzero at `p4`, or at any `p_n`.
   - Rung 2d's fallback point cannot yield outcome 1 or 2 for *any* candidate.
   - A nonzero value at `p4` is therefore always a determinant-side rejection, never evidence of
     separation.
   - This is consistent with B26-02 §3 (READ), which already ruled out the pair `(p4, D4)` as a
     separation witness for the old family. The reason is now visible: `p4 ∈ P ∩ D`.
3. **For later work.** Any padding witness offered for separation must lie in `P \ D`, which
   needs its own proof. Committed text I read never claims `p4 ∉ D`, so no accepted result is
   contradicted.
4. **Not affected:** B26-02's rejections, A26-03 with B26-10C, and the visibility certificate
   (row 7), which is an ambient calculation. I did not examine whether B27-01's `T*` lies in `D`.

## 5. Verdicts and levels

- **ACCEPT:** rows 1–12; registered outcome 3.
- **REPAIR:** row 13, clerical only.
- **Added finding:** §4 (HAND plus COMPUTED). DEFER and REJECT: none.
- **Achievements reached:** none of source condition, coefficient equation, separation on
  padding, or positive multiplicity gap. There is also no geometric noncontainment and no
  asymptotic bound.
- **Binding constraint, unchanged:** "No five-row determinant equation is known to be nonzero on
  padding." A25-10's decision stands: no construction ready.
