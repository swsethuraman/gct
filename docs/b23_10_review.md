# B23-10 — Independent review of Batch 23, and gates for Batch 24

19 September 2026 (UTC). Slot 10, Batch 23, Phase 2. Worktree `work/batch15_workers/B15-10`, branch
`b15-10-portable-witness`. Author: Claude (Opus 5, 1M context), default permission mode. Reviewer
only: no cell, no gap claim, no worker. Git was used read-only (`rev-parse`, `status`, `show`, `grep`,
`log`, `ls-tree`, `cat-file`, `diff`, `check-ignore`). No commit, push, fetch, stash or checkout.

**Provenance.** This slot ran in **two sessions**. Session 1 recorded the state below, wrote
`results/b23_10/preverdicts_formed_before_reading.md` (01:40–01:46Z), and ran pilots 1–2
(01:53Z, 01:57Z). It wrote no report. Session 2 (this one) re-recorded the state before its first
write, found session 1's files untracked and unedited, and wrote everything else. I have **no
transcript of session 1**. Its record is its files, and I do not attest to anything it did not write
down (§11, negative 1).

```
git rev-parse HEAD          2efb7aaf1927e8d2785dfbbcc78b847592c204f5   (= the brief; session 1 and session 2)
git rev-parse HEAD^{tree}   d922720ff27092578b8c59aefc80f6216c1a5a73
git status --porcelain      session 1 (01:40:49Z): the two 2026-09-13 b15_10_runtime receipts only
                            session 2 (15:33:22Z): those, plus session 1's untracked b23_10 files
                            (two scripts, results/b23_10/, two _resources.json); 0 tracked changes
```

**Method (B20-10 §0, B21-10 §0, B22-10, verbatim in force).** Verdicts were formed before reading
each deliverable's defence, are marked **[pre-formed]**, and are preserved byte-for-byte in
`results/b23_10/preverdicts_formed_before_reading.md`. That file is not edited. Where I now depart
from it, the correction is here, with a pointer (§1.4). Committed bytes only, via `git show
<commit>:<path>`. Every verdict names its method: **READ**, **REPLAY**, or **INDEPENDENT EVALUATOR**
(my own code or hand derivation). Later corrigenda govern (G15, G15′). I edit no sealed report.
Decisions are transcribed from the **closing ledger (§12)**, never from the sections before it.

**Delegated reading, disclosed.** Three read-only helper agents did three mechanical walks, each
restricted to `git show` on pinned commits with no writes: the B23-04 claims table (§6.1), the
B23-05 change list (§6.2), and a transcription audit of the B23-12 ledger (§9). I checked each by
hand at the lines named in §§6 and 9. Every ruling in this report is my own.

## Plain terms, up front

1. **The two defects alleged against B22-10 are real, and each is narrower than alleged.**
   - **G-17.** B22-10's "the cap minors do vanish on the plane family" rested on one exact rank at
     one point. That is a floor and cannot give "vanish on the family". B23-04 was right to call it
     OPEN, and B23-03's Proposition 2.5 now **closes it (PROVED)**. One detail of B23-04 is wrong:
     the rank was computed **exactly over `Q`**, not "mod `2^31 − 1`".
   - **G-18.** The "iff" is wrong. The same error recurs in B23-01's own transcription sentence (b).
     One corrigendum covers all three places (§12, K1–K2).
2. **The dimension "reversal" did not happen as the integrator describes it.** B22-10 never wrote
   "projective dimension `>= 35`". That phrase is the integrator's own brief. B23-03 corrected it as
   "the brief's line", and the B23-12 ledger then pinned it on B22-10.
   - B22-10's numbers stand: `>= 35` and `33`, both affine, with `33 aff / 32 proj` stated.
   - B23-03's exact values stand: **T2 = 35 aff / 34 proj; T1 = 33 aff / 32 proj.**
   - What falls is B22-10's sentence "the record is off by one" (§1 and the §7 header). B22-02
     stated 32 bare, with no convention and no derivation, and 32 is the correct projective value.
   - G24 is vindicated, not undermined.
3. **B23-03's two theorems stand.** Replayed with code written here.
   - Proposition 2.5: PROVED. The witness syzygy replays. I also recomputed the generic value 64 at
     a fresh random plane cubic (exact). One surprise: the witness itself has rank **58**, not 64.
     It is a special member, and B23-03 never claims otherwise.
   - Theorem 3.2: PROVED. All eight shipped determinant floors, all eight padding ceilings, and all
     three Newton certificates replay exactly.
   - Row 1 is a **PROVED-kill at `N = 6, 7, 8` with no adopted input**. At `N = 5` it stays what the
     record says: GKZ Theorem B, which at `k >= 7` rests on Kleiman (ADOPTED, SECONDARY). So "PROVED
     across `N = 5..8`" needs that one qualifier.
   - G-A1 is genuinely open (§3.3).
4. **The Bürgisser–Ikenmeyer allegation is right in substance and wrong in its wording.** Paper 1's
   bracket census (Prop. 4.1) is **not new**. It is the pigeonhole case of BI Cor. 7.2, and exactly
   the counting step of BI Prop. 3.24(3).
   - It is **not "equivalent to Cor. 7.2 with Prop. 7.3"**. It is strictly weaker than Cor. 7.2 and
     does not need Prop. 7.3, which BI state without proof.
   - Replacement wording is in §4.4. The two proofs are the same antisymmetry, so one remark
     sentence is warranted, and no novelty claim.
5. **Claims tables.**
   - B23-04: 46 of 46 rows match their cited sources. Five rows are stale against B23-03/B23-02,
     which were committed in the same second.
   - B23-05: 7 of 7 paper edits are present and authorised. Three cite their record lines
     incompletely or loosely.
   - Details in §6.
6. **Lineage gaps.** Ranked: the `n = 3` positive control (LMR read-status) first, then the Astra
   theorem. The washout theorem's premise is **closed here by replay**, and the deficit lemma
   **closed here by a two-line re-derivation**; residues are named.
7. **The height-2000 claim needs scoping, not striking.** Its definition is unrecoverable. Under a
   per-coefficient reading it is **false** at `P` alone: 15 lifts of `α` and 16 of `β` have height
   `<= 2000`, including `737/646`. Under a common-denominator reading it is **true**, and the
   candidate has height 2842.
8. **G19: not touched** by B23-03's `print('x')` and empty program. One sentence is added to the
   definition (§8).
9. **The integrator's record.** Transcriptions are mostly faithful. It contains **eight further
   errors it does not admit**, the largest being the misattribution in item 2. One of its four
   admissions is itself inaccurate.

Pilots: **3 of 3 used, 9.25 s of 180 s**. No cap was hit, and there was no crash or retry.

---

## 1. Pre-formed verdicts, and where I now depart from them

`results/b23_10/preverdicts_formed_before_reading.md` (sha256 in the manifest) holds five blocks,
Q1–Q5, each timestamped before the matching section was opened. In summary:

- Q1: G-17, G-18 and the dimension reversal, formed from B22-10 alone.
- Q2: Prop. 2.5, Thm 3.2 and G-A1, from the statements only.
- Q3: B23-01 §3.
- Q4: B23-02 Prop. 1.1, from the statement.
- Q5: the BI attribution, formed from the archived paper and BI §7.1 **before** B23-05's `GAPS.md`
  was opened.

### 1.4 Departures (the pre-verdict file is unedited; these govern)

- **Q2, the witness.** I wrote "I will replay `rank M_4 = 64` at the witness exactly". Pilot 1
  gives **58**.
  - The witness `x_1(x_3² + x_4²) + x_2(x_5² + x_3x_4)` is a special member of `Sigma_Pi`. B23-03
    uses it only for the two open conditions (independent partials; `M_45` has a monomial free of
    `x_1, x_2`), never as a floor point. The floor comes from random points.
  - My expectation was wrong. B23-03 is not.
- **Q2, Theorem 3.2's route.** I expected a grade-4 regular-sequence ceiling on `dim(S/J_F)_k`, and
  named "grade measured, not certified" as the likely weak point. B23-03 uses a better route: an
  explicit determinantal point `F_0` with a **monomial** Jacobian ideal, whose Hilbert function is
  exact for every `k`. The weak point I anticipated does not arise.
- **Q1, "a single-point modular rank".** The brief's wording, and B23-04's, is that B22-10's rank
  was modular. It was exact. See §2.1. The substance of my pre-verdict is unchanged.

Every other pre-formed verdict stands as written, and is confirmed below with the method named.

---

## 2. Priority 1 — the two defects alleged against B22-10

### 2.1 G-17 (cap minors "do vanish" on the plane family)

**B22-10's text** (`2efb7aaf`, `docs/b22_10_review.md` L313–316): "The cap minors do vanish on the
plane family too (rank 64 there, pilot 2), so the right-way cubic separation survives the
correction."

**Its evidence.** `analysis/b22_10_p2_D45_cap_P5.py` L17–18, L136–137, L277–280 computes `rank M_4`
**exactly over `Q`** (Bareiss) at one random cubic through a plane: 64. The Jacobian ranks in the
same pilot are modular; `rank M_4` is not.

- **(i) Was B22-10's claim over-stated on its evidence? Yes. [pre-formed, READ]**
  - A rank at one point bounds the generic rank from **below**.
  - "The 65-minors vanish on the family" is the **ceiling** `rank <= 64` at every member.
  - B22-10's own S18 labels the same numbers MEASURED. §7 states them as fact and draws a
    conclusion from them.
- **(ii) Was B23-04 right to call it OPEN? Yes, with one correction. [READ]**
  - C37's label, "vanishing OPEN; single-point MEASURED evidence", is right.
  - G-17's description of the evidence, "rank measured mod `2^31 − 1`", is **wrong**: it was
    exact. That is a misdescription of method, not of force. A single exact rank is still only a
    floor.
- **(iii) Does Prop. 2.5 close it? Yes: PROVED. [pre-formed, READ + INDEPENDENT (hand) +
  INDEPENDENT EVALUATOR, pilots 1 and 3]**
  - The mechanism in §2.5 is the one I derived before reading it. Details in §3.1.

**Ruling.** B22-10 §7's sentence is **SUPERSEDED** by B23-03 Prop. 2.5 (a stronger statement,
proved). Until B23-03, the right label was MEASURED. The corrigendum is §12, K3.

### 2.2 G-18 (S11's "iff")

**B22-10's text** (L427, S11): "OPEN — rank 3 **iff** `P` divides every `3 × 3` minor of the exact
`Z[1/2]` rows". §3.2 (L175) says the same: "Rational rank 3 is possible exactly when `P` divides
every `3 × 3` minor".

**Ruling: the allegation is right. [pre-formed, READ + INDEPENDENT (hand)]**
- Rank 2 mod `P` is already established. Given that, "`P` divides every minor" is **necessary**
  for rational rank 3, but not sufficient: it also holds when every minor is `0` over `Q`
  (rational rank 2).
- The correct biconditional is: rational rank 3 **iff some `3 × 3` minor of the exact rows at the
  70 certified points is nonzero over `Q`**. Every such minor is then necessarily divisible by `P`.
- B22-01 §4.3's "would require `P` to divide every `3 × 3` minor" is correct, and B23-04's C42
  uses it.

**The same defect recurs in B23-01** (`cc14e88c`, §1.5(b), copied verbatim into §5): "Rank 3 over
`Q` remains possible, **exactly when** both `P` and `P₂` divide every `3 × 3` minor of the exact
integer rows at the points used." It has two faults:
- "exactly when" should be "only if";
- "at the points used" is wrong in scope. Rational rank is decided on the injective set, which is
  the 70 points at `P`. `P₂` was tested at three points only.

B23-01 is sealed and is not edited. The corrigendum is §12, K1–K2.

---

## 3. Priorities 2–3 — the dimension ruling, B23-03's theorems, and G-A1

### 3.0 The dimension reversal: which stands [pre-formed, READ]

**What each packet says, in committed bytes.**
- **B22-10** (`2efb7aaf`):
  - L65–66: the plane family has "dimension `>= 35`" and `{l·C}` "exactly `33` (not 32 — the
    record is off by one)".
  - L298–300: the table gives Jacobian ranks 35 and 33 (maps into `C^70`, hence **affine**).
  - L303: "`= 33` exactly (affine)".
  - L308–311: "**The record's 'dimension 32' is off by one.** … `{l·C : C ∈ D35}` is 33 affine
    (32 projective). B22-02 … mix the conventions: `D45` is quoted affine (50), this family
    projective (32). Wording only; see G24."
  - S24 (L440): "33 affine (32 projective)".
  - **No line says "projective dimension `>= 35`".** I searched for "projective" within reach of
    "35".
- **B22-02** (`e22a41b1` L208): "`{l·C : C in D35}` of dimension 32". It is bare, with no
  convention and **no derivation**, beside "`D45` … (dim 50)" at L23.
- **B23-03** (`3bcad666` §2.4, L284–296):
  - Correction 1: "**The brief's line** 'that family has **projective** dimension `>= 35`' …
    mislabels both numbers."
  - Correction 2: "§7 says 'wording only'. The second is right: B22-02's 32 is the correct
    **projective** value."
- **B23-12 ledger** (`60a88025`):
  - L205–209: "B22-10 reported 'projective dimension ≥ 35' … B23-03 finds the reverse … the
    record's §7 value of 32 was correct all along … First time on this record a producer has
    corrected a reviewer."
  - L40: "≥ 35 against 33, projective (B22-10 pilot 2)".

**Rulings.**
- **The numbers.** T2 is **exactly 35 aff / 34 proj**, and T1 is **exactly 33 aff / 32 proj**
  (B23-03 L8, PROVED; the floors are exact Jacobian ranks and the ceilings are by hand). B22-10's
  `>= 35` (aff) and `33` (aff) are consistent with these and **stand** as floors. B22-10 never
  gave a projective 35.
- **"The record is off by one" (B22-10 L65–66 and the bold header at L308): SUPERSEDED.**
  - B22-02 gives no derivation. B22-10's "orbit rank 17, not 18" guesses one (`50 − 18 = 32`, the
    naive stabiliser count), and nothing in B22-02's bytes supports that guess.
  - Read as projective, B22-02's 32 is correct. Read as affine, it is wrong.
  - B22-10's own "mix the conventions … Wording only" (L310–311) is the defensible sentence. It
    stands, and B23-03 agrees with it.
- **"The reviewer was wrong and the record was right" (B23-12 L205–209): REJECTED as stated.**
  - The "projective" mislabel originated in the integrator's brief, not in B22-10.
  - What B23-03 corrected in B22-10 is narrower:
    - the "off by one" sentence (§1 and the §7 header);
    - the one-point cap-minor sentence (G-17).
  - "First producer correction of a reviewer" therefore **holds, but for those two sentences, not
    for the dimensions**. It is recorded as such in §12.
- **G24.** Vindicated. The defect G24 targets (a bare 32 beside an affine 50) is exactly what
  B22-02 did. The later confusion arose from a brief that did not follow G24. Its author, the
  integrator, is not bound by producer gates. §10 closes that hole (G28).

### 3.1 Proposition 2.5 — PROVED [pre-formed on the statement; READ + INDEPENDENT (hand) + INDEPENDENT EVALUATOR]

**The statement** (L306–309): `rank M_4(C) <= 64` for every `C ∈ Sigma_Pi`, with generic value 64.

**The proof** (L310–323) has the shape I pre-formed:
- `C = x_1q_1 + x_2q_2`;
- `g = (M_45, −M_35, M_34)`, the `2 × 2` minors of `(d_jq_1, d_jq_2)_{j=3,4,5}`, i.e. `u × v`;
- `Σ_{j>=3} g_j d_jC = x_1(g·u) + x_2(g·v) = 0`.

I checked the non-Koszul step independently.
- Suppose the partials are linearly independent, and a combination `Σ c_{ij}(d_jC e_i − d_iC e_j)`
  has components 1 and 2 equal to zero. Then `c_{1j} = c_{2j} = 0` for every `j`, so components 3–5
  are combinations of `d_3C, d_4C, d_5C`, all in `(x_1, x_2)`.
- `g_3 = M_45` has a monomial outside `(x_1, x_2)`. So `g` is not Koszul, `dim ker M_4 >= 11`, and
  `rank <= 64`.
- Both conditions are open and nonempty on the irreducible space `(x_1, x_2)_3`. `{rank <= 64}` is
  closed. `GL_5` carries the result to all of `Sigma_Pi`.

**Replay** (pilot 1, part A; exact integer arithmetic, no project code):
- the syzygy identity is `0`;
- `g = (4x_4x_5, −4x_3x_5, 2x_3² − 2x_4²)`, so `g_1` has a monomial free of `x_1, x_2`;
- the partials have rank 5;
- `rank M_4 = 58` at the witness (§1.4);
- control: Fermat cubic 65.

**Generic value 64**, from three independent lineages, each an exact rank over `Q` at a random
plane cubic:
- B22-10 pilot 2: 64;
- B23-03 pilot 1 E6: 64;
- **B23-10 pilot 3**, with a fresh seed (20260922) and `fmpz_mat.rank`: **64**. Control: a random
  cubic, 65.

**Label: PROVED.** It closes G-17 (§2.1).

### 3.2 Theorem 3.2 — PROVED; row 1 is a PROVED-kill at `N = 6, 7, 8` [pre-formed on the statement; READ + INDEPENDENT EVALUATOR, pilots 1 and 3]

**Premises, checked.**

(1) **Padding ceiling.** `J_{lP} ⊆ (l, P)` gives `rank M_k(lP) <= dim S_k − h_N(k)`, with
`h_N(k) = C(k+N−2, N−2) − C(k+N−5, N−2)`. That is the Hilbert function of the complete intersection
`(l, P)`, and it also bounds the case `l | P`. The universal ceilings at `k = 3..6` are:
- the column count at `k <= 5`;
- `N·dim S_3 − C(N, 2)` at `k = 6`.

I checked `k = 6` by hand (6·56 − 15 = 321; 7·84 − 21 = 567; 8·120 − 28 = 932). Pilot 1 recomputed
all eight padding ceilings at `k = 6..8`. **8 of 8 equal the shipped values.**

(2) **Determinant floors at `k = 6..8`.** Pilot 3 used my own code:
- a random `4 × 4` matrix of integer linear forms in `N` variables;
- the determinant computed exactly over `Z`;
- `rank M_k` mod `2^31 − 1`, which is a floor at an integer point.

| `N` | `k` | my floor | shipped floor | ceiling (pilot 1) | margin |
|---|---|---|---|---|---|
| 6 | 6 / 7 / 8 | 321 / 660 / 1146 | 321 / 660 / 1146 | 287 / 532 / 918 | **+34 / +128 / +228** |
| 7 | 6 / 7 / 8 | 567 / 1279 / 2435 | 567 / 1279 / 2435 | 518 / 1050 / 1968 | **+49 / +229 / +467** |
| 8 | 6 / 7 | 932 / 2248 | 932 / 2248 | 876 / 1926 | **+56 / +322** |

**All eight floors equal the shipped values**, so all eight margins replay. At `k = 6` the floor
equals the universal ceiling, so the determinant's rank is exact there.

(3) **The tail `k >= k_1`.** Each `F_0 = x_1x_2x_3x_4 − o_1o_2o_3o_4` is the determinant of the
displayed cyclic matrix. Expanding along the 4-cycle gives the sign −1, so `F_0 ∈ D_N`. Its Jacobian
ideal is generated by monomials in disjoint variable blocks, so `S/J = A ⊗ B` and `H = A * B`.

Pilot 1 computed `A` and `B_N` by brute-force monomial enumeration. It confirmed:
- `A(a) = 6a − 2` for `a >= 1`;
- the Newton coefficients at `k_1` (**3 of 3 match exactly**: `11, 50, 21, 3, 0`;
  `119, 216, 117, 30, 3, 0`; `69, 420, 371, 163, 36, 3, 0`);
- all margins are positive on `[k_1, 60]`;
- sixth differences vanish there.

Eventual polynomiality is proved: both factors are eventually polynomial, and the convolution is
polynomial past the finitely many exceptional terms. So nonnegative Newton coefficients with
`e_0 > 0` prove `D(k) > 0` for every `k >= k_1`. **Spot check of one margin in full:** `(N, k) =
(7, 8)`, +467, replayed on both sides.

**Ruling.**
- **Theorem 3.2 PROVED** at `N = 6, 7, 8` for every `k`. It uses no Kleiman, Dimca,
  Gulliksen–Negård or depth sensitivity.
- **Row 1** is a **PROVED-kill at `N = 6, 7, 8`**. B22-10's ASSESSED label (its §6 row 1) is
  **discharged** there.
- **At `N = 5`, "PROVED" needs its qualifier.** GKZ Theorem B at `k >= 7` rests on Kleiman
  (ADOPTED, SECONDARY; GKZ corrigendum C2: "Kleiman remains the only adopted input for `k >= 7`").
  So B23-03's "PROVED-kill in the whole window `N = 5..8`" should read: PROVED at `N = 6..8`, and
  PROVED at `N = 5` modulo Kleiman at `k >= 7`.
- **Cheap discharge of that qualifier (for Batch 24).** B23-03's own method runs at `N = 5` with
  `F_0 = x_1x_2x_3x_4 − x_5^4` (the same cyclic matrix with every `o_i = x_5`). By hand:
  - `H(k) = 18k − 24` for `k >= 3`, and `h_5(k) = (3k² + 3k + 2)/2`;
  - so `D(k) = (3k² − 33k + 50)/2`, which is **positive for every `k >= 10`**;
  - `k = 7, 8, 9` need three modular floors at a random `D45` point.

  One pilot of seconds. Not run here: no pilot remained, and it is producer work. INDEPENDENT
  (hand), for the `k >= 10` tail only.

### 3.3 G-A1, the boundary — genuinely not excluded [pre-formed; READ + INDEPENDENT (hand)]

Theorem 2.1 classifies `closure(D45° ∩ P5)`, the closure of the **actual** determinants in `P5`. A
point of `(D45 \ D45°) ∩ P5` is a limit of determinants that is not itself one.
- Nothing on the record excludes such a point of the form `l·C*` with `C*` smooth.
- B17-01-C (ADOPTED) excludes one specific `F*`, not a family.
- "`D45°` is closed" is not to be expected by default. Landsberg (arXiv 1305.7387v3, read here via
  ar5iv, sha256 in the manifest) defines `dcbar` and `dc` in §2. Later, with the polynomials
  `P_{Λ,m}`, he exhibits "`dcbar(P_{Λ,m}) = m < dc(P_{Λ,m})`": limits of determinantal expressions
  that are not themselves determinantal. That concerns
  `Det_n`, not `D45`, so it only shows the phenomenon is real. It does not place one in `D45 ∩ P5`.
- Two natural invariants fail to exclude it:
  - **Rank thresholds of `F`.** They are the wrong way on padding (Thm 3.2; GKZ B).
  - **Semicontinuity of the singular locus.** The 20 nodes of a generic `det A` can converge onto
    the surface `{l = 0} ∩ C*`, where `l·C*` is singular.

**What would exclude it.** Any one of the following, in increasing strength:
- **(a) A boundary description.** Every one-parameter degeneration `det A(t) → l·C*` with `A(t)`
  divergent, put in normal form (curve selection plus a normal form for linear `4 × 4` pencils in
  five variables through the singular-pencil locus `Z`), lands in `T1 ∪ T2`. This is B20-10 R11's
  territory, and it inherits EH C1/C3's conditional status. One theory slot, paragraph-first;
  **no pilot can close it**, since sampled degenerations are only MEASURED.
- **(b) A direct proof** that the projection `{C : l·C ∈ D45}` equals `D35 ∪ Sigma_Pi` for fixed
  `l`.
- **(c) A proof that `D45°` is closed.** Not expected, as above.

**Label:** OPEN, correctly named by B23-03. Consequence: the "right-way corner survives" is
PROVED **on the determinant part only**. Paper 3 must say so.

### 3.4 The rest of B23-03, briefly [READ]

- Theorem 2.1's case analysis (L1).
- `T3 ⊆ T2` (L4). I followed the intersection-number argument: bidegrees `(2,1)` and `(1,2)` on
  `P^1 × P^1`, with intersection number 5 > 0.
- The skew-bordered type `⊆ T2` (L2).
- `T1 ⊄ T2` (L9, with its two UNREAD-CLASSICAL Hilbert-function facts).

I read all four and found no gap. I did not replay pilots 1–2 of B23-03 beyond §3.1–3.2, so for
these rows my verdict is **READ, affirmed**, not REPLAY. The integrator's "`T1 ⊄ T2` is certified"
drops the packet's two UNREAD-CLASSICAL qualifiers (§9).

---

## 4. Priority 4 — the attribution ruling (Paper 1 Prop. 4.1 vs Bürgisser–Ikenmeyer)

### 4.1 What I read, hashed

| object | sha256 |
|---|---|
| arXiv:1511.02927**v2** PDF (current), fetched 2026-09-19 | `a4138fc3ef45f144f367f227514b8345ddd74690c19ca07e1ef4be707fd6ea7b` |
| arXiv:1511.02927**v1** PDF | `c2584469cc1591b010ae758a7027367a1008ca61156e302762ce2bae64b8c62a` |
| ar5iv HTML rendering (the text I read) | `14b94adfa7b05d1dc143aca55cea25ed26d67384759886a466938e44df41cbca` |
| my tag-stripped text of that HTML | `94aae3ee34e5b1871c5fd4aa084b67527e7a5260cdbf3ccdd97d12011927614e` |

- Session 1 and session 2 fetched independently, about 14 hours apart. Their PDF and HTML hashes
  are **identical**.
- There is no local PDF text tool (`pdftoppm` is absent), so I read the ar5iv rendering, not the
  PDF bytes. The PDF hashes pin the version only.
- Read in full: §7.1 (Prop. 7.1 with its proof, Cor. 7.2, Prop. 7.3), Prop. 3.24 with its proof,
  and the introduction's paragraph pointing to it.
- The paper: `paper/det3-conductor.tex` at `82633a60` (sha256 `dd0d2abf…`), L160–176 and L470–545.
  At `bbd1d12e` (sha256 `2cc15d3f…`) Prop. 4.1 is unchanged; B23-05 proposed its wording and did
  not apply it.

### 4.2 The statements side by side

- **BI Cor. 7.2** (verbatim substance): for `D` odd and `m | dD`, `dim O(Sym^D C^m)_d^{SL_m}` is at
  most the number of **sets** of `d` distinct `D`-subsets of `{1..dD/m}` in which each number occurs
  in exactly `m` subsets.
- **BI Prop. 3.24(3), proof:** "There is no nonzero `SL_m`-invariant in degree `2m` if
  `C(2D, D) < 2m`. For the proof of the upper bound we use … Corollary 7.2. It suffices to show that
  there are less than `2m` distinct cardinality `D` subsets of `{1..2D}`."
- **Paper Prop. 4.1:** for `D` odd, `m | δD`, `k = δD/m`: if `δ > C(k, D)` then
  `C[Sym^D C^m]^{SL_m}_δ = 0`.

### 4.3 Ruling: RELATED — a special case, not an equivalent [pre-formed, READ + INDEPENDENT (hand)]

- **Contained in BI.** Put `d = δ`. If `δ > C(k, D)`, no family of `δ` distinct `D`-subsets of
  `[k]` exists, so BI's count is 0. **Prop. 4.1 is the pigeonhole case of Cor. 7.2.**
- **At `δ = 2m`, `k = 2D`, it is exactly BI's Prop. 3.24(3) counting step**, word for word ("less
  than `2m` distinct cardinality `D` subsets").
- **Cor. 4.2 (`e(det_3) >= 18`) follows from BI alone.**
  - At `m = 9`, `D = 3`, Cor. 7.2's pigeonhole excludes `δ = 3, 6, 9, 12, 15` (`C(k, 3) = 0, 0, 1,
    4, 10 < δ`; pilot 2 recomputed the table).
  - BI's period theorem already restricts to multiples of 6.
  - So the paper's "turns out to need no computation … already excludes every smaller degree" is
    BI's argument and needs their name.
- **"Equivalent" (B23-05's proposed wording, and the ledger's gloss) is wrong in two ways.**
  1. Cor. 7.2 is **strictly stronger** than Prop. 4.1. It counts, and it imposes regularity (each
     element in exactly `m` subsets), so it can vanish where `δ <= C(k, D)`. Prop. 4.1's statement
     is only the "no distinct family at all" case.
     - B23-05's "the case of Cor. 7.2 … in which no admissible set exists" is **also** not
       Prop. 4.1. That case includes the regularity failures, which Prop. 4.1's statement does
       not use.
  2. **Prop. 7.3 is not needed** for this implication, and **BI state it without proof** ("We
     state without proof …"). Citing it as a source of the census imports an unproved statement
     for nothing.
- **What B23-05 got right.** The substance: the census is not the paper's, BI prove it (Cor. 7.2)
  and use it (Prop. 3.24(3)), and the "no computation" framing must be credited. **This is a
  blocker for submission**, as READINESS item 1 says.

### 4.4 Wording (for the author; not applied by me)

After "we state it in general because the statement costs nothing extra", replace B23-05's
sentence with:

> "Proposition 4.1 is the case of Bürgisser and Ikenmeyer's plethysm bound
> \cite[Cor.~7.2]{BI} in which no family of $\delta$ distinct $D$-subsets of $[k]$ exists at all,
> and for $\delta=2m$, $k=2D$ it is the counting step of \cite[Prop.~3.24(3)]{BI}. We include the
> bracket-monomial proof because it is short and self-contained."

Then:
- the introduction's "turns out to need no computation: an elementary parity count … already
  excludes every smaller degree" should credit BI;
- Cor. 4.2's "with no computation" should read "by \cite[Cor.~7.2]{BI} and the period theorem"
  (or keep "with no computation" and add the citation).

### 4.5 Do the proofs differ in substance? No: one remark sentence, no novelty claim

- **BI:** `mult_λ(O(Sym^D)_d) = mult_{λ^t}(Λ^d Λ^D C^m)` for odd `D` ([34, Fact 6.1]), then a
  weight-space bound. The `Λ^d` is what forbids repeated `D`-subsets.
- **The paper:** the first fundamental theorem for `SL_m`, then the transposition sign
  `(−1)^D = −1`, which kills repeated rows.

Both are the same antisymmetry of odd-degree letters. Run to completion, the paper's argument bounds
the dimension by the number of admissible row-*sets*, which is Cor. 7.2 itself. That is worth
**one sentence** in a remark ("an elementary route via the first fundamental theorem, avoiding the
plethysm transposition fact"), and **not** a claim of a new result.

---

## 5. Priority 7 — B23-01 and B23-06, briefly

### 5.1 B23-01 [pre-formed on §3; READ + REPLAY of the arithmetic (pilot 1, part C)]

- **The design matches B22-10 §4 exactly.**
  - `P₂ = 524269`, three certified points, 45 evaluations, all 20 minors.
  - B22-10's §4 text is quoted verbatim at B23-01 §1.2.
  - The sixth node and the CRT reconstruction were pre-registered as descriptive extras.
  - **Confirmed.**
- **The control substitution was pre-registered before the run, and is sound.**
  - §1.3 records the specification defect. The sealed values are residues mod `P` of integers
    nobody computed, so nothing can be compared at `P₂`.
  - That text is in the snapshot `e265f969…`. I re-hashed it from `cc14e88c`: it matches.
  - The pilot's first output field records it at 0.0003 s, and the receipt's `started_utc` is
    18:50:52Z, so the ordering is proved by G25.
  - The substituted controls (c1 at `P`, c2's `g`-independence at `P₂` with teeth, c3 arithmetic)
    are each the identity they test (G21).
  - The defect was the brief's, so this is also an integrator item (§9).
- **Outcome (b) is correctly labelled as evidence.** No label moves. The one defect is the "exactly
  when" in the transcription sentence (§2.2, K1).
- **Replay.** With my own arithmetic (pilot 1, part C):
  - all 20 minors of the shipped six rows vanish mod `P₂`;
  - the relation residual is 0 on all six rows at `P₂`;
  - `737/646` and `−1421/969` reduce to the recorded residues at **both** primes.

  The reconstruction is consistent. It is a MEASURED candidate: B23-01's label is right.

### 5.2 The height-2000 question (carried over from B22-10) [READ + INDEPENDENT EVALUATOR]

**Where the claim lives** (`82633a60`):
- routeA §5.3 (REPORT.md L224): "no small-height rational lift found";
- its certificate (`arc_rows_and_sampled_kernel_candidate.json` L380): "not reconstructible with
  small height";
- CURRENT_DIAGNOSTIC_STATE L50: "no small-height rational lift exists (bound 2000)";
- arc_target CORRIGENDUM C3 L43: "no small-height lift exists (parent, bound 2000)".

**The definition of height appears nowhere.**
- None of the routeA pilots or verifiers contains a reconstruction. A `git grep` for
  `height|ratrec|rational|reconstr|lift` over their `.py` files finds nothing.
- The search that produced "2000" has no surviving code at `82633a60`.
- **The definition is unrecoverable from committed bytes.**

**What each reading gives** (pilot 1, part C, exhaustive):
- **(i) Per-coefficient, `max(|a|, |b|) <= 2000` for each of `α`, `β` separately.**
  - At `P ≈ 5.2·10^5` such lifts are **not unique**: `2·2000² > P`. They exist in number: **15
    for `α`** (including `737/646`) and **16 for `β`** (including `−1421/969`).
  - Under this reading the claim is **false**.
- **(ii) Common denominator: `(a, b; d)` with `α ≡ a/d`, `β ≡ b/d` and `max(|a|, |b|, d) <= 2000`.**
  - **None exists.** The first at height `<= 3000` is `(2211, −2842; 1938)`, B23-01's candidate,
    of height 2842.
  - Under this reading the claim is **true**.
  - This is the natural reading for a **vector** lift: the primitive integer vector
    `(1938, −2211, 2842)` of `1938·n02 − 2211·q_3 + 2842·q_7`.

**Ruling: SCOPE, do not strike.** Replace the phrase wherever it stands with:

> "No common-denominator lift `(a, b; d)` of `(α, β)` with `max(|a|, |b|, d) <= 2000` exists modulo
> `P` (B23-10 pilot 1, exhaustive). Per-coefficient lifts of height `<= 2000` are not unique at a
> single prime of this size and do exist. A two-prime reconstruction gives the MEASURED candidate
> `(2211, −2842; 1938)`, height 2842 (B23-01)."

The original is **SUPERSEDED** by this sentence. It is not refuted, because its intended definition
cannot be recovered.

### 5.3 B23-06 [READ + source check]

- **`dc` against `dc̄`: CONFIRMED.** I fetched Landsberg arXiv 1305.7387 via ar5iv (sha256 in the
  manifest). Its §2 reads "it is known … that `5 ≤ dc̄(perm_3) ≤ dc(perm_3) ≤ 7`", followed by
  "Problem 2.4. Determine `dc̄(perm_3)`". It defines `dc̄` through `Det_n` (the closure) and `dc`
  through `End(W)·det_n`, and notes `dc̄ ≤ dc`.
  - ABV (arXiv 1505.02205, ar5iv, sha256 in the manifest), Cor. 1.4, is the exact-`dc` statement,
    as B23-06 says.
  - The correction stands: `(3,5)` and `(3,6)` are open at the orbit-closure level.
- **"Visible rows exist iff `n <= m²/2`": PROVED, with one boundary precision.**
  - The padded support has `m² + 1` variables, and the second fundamental form is blind iff
    `N <= 2n`. So visible rows exist iff `m² + 1 > 2n` iff `n <= m²/2` (integers). Correct.
  - The companion phrase "exactly the LMR range" is off at one point. LMR's Thm 1.0.1 is
    `dc̄(per_m) >= m²/2`, so it proves separation for `n < m²/2`.
  - At `n = m²/2` (`m` even) one row is visible, but LMR's inequality is not strict there.
  - At `m = 3` (`m²/2 = 4.5`) nothing changes.
- **The integrator's "pin `dc̄(per_3)`"** overstates B23-06 L237: a separation at `(3,5)` would prove
  only `dc̄(per_3) >= 6` (§9).

### 5.4 B23-02 [pre-formed on Prop. 1.1; READ + INDEPENDENT (hand)]

- **Prop. 1.1 (a)–(d): PROVED**, on the UNREAD-CLASSICAL Hilbert–Burch and `grade = ht`, as
  labelled.
- **My pre-formed caveat stands, and B23-02 half-states it.** (c) needs **scheme-theoretic**
  containment. B23-02 itself exhibits a genuine member that is non-reduced: the triple structure
  `V((y_1, y_2)³)` on a plane.
  - That member lies set-theoretically in every hyperplane through its plane. So under a
    **set-theoretic** reading of row 10's condition, **every** padding point `l·C` (with `{l = 0}`
    containing some plane) satisfies it.
  - Under that reading row 10 is a **direct PROVED-kill**: the condition holds on all of `P5`.
- **Either reading closes row 10:** PROVED-merge into row 11 (scheme-theoretic, B23-02) or
  PROVED-kill (set-theoretic, this review, INDEPENDENT hand).
- **B23-02's L5** "genuine members add no padding point outside `D45`" must carry the word
  "scheme-theoretically".

---

## 6. Priority 5 — the claims tables (G26), against packets, not prose

### 6.1 B23-04 `CLAIMS.md` (`ce43cdb7`, sha256 `2b7ba688…`)

**Count: 46 of 46 numbered rows (C01–C46, no gaps or duplicates), plus the unnumbered standing-rule
row.** Each row was checked for three things: its label against the cited source (or a later
governing review/ledger), its commit exists and holds the cited path, and the claim is stated there.
All 21 cited commits exist.

**Mismatches against the rows' own cited sources: 0** (label 0, commit 0, lineage 0, unverifiable
0). The `\prov{}` labels in the `.tex` match `CLAIMS.md` row by row.

**Stale against packets committed at the same second** (B23-01/02/03/04/06 all at 21:02:49–50;
B23-03 is not an ancestor of `ce43cdb7`): **5 rows**, which Paper 3 must update after this review.

| row | says | now | governing |
|---|---|---|---|
| C23 | rows 1–2 ASSESSED at `N = 6..8` | row 1 PROVED-kill at 6–8 (qualifier at `N = 5`, §3.2); row 2: `j >= N−3` CONDITIONAL zero ideal, `2 <= j <= N−4` OPEN | B23-03 Thm 3.2, L15–L16; §12 K5 |
| C30 | kill table; row 1, row 10, row 13 premise | row 1 as C23; row 10 PROVED-merge (10a/b/d) / PROVED-kill at `N = 5` (10c), and PROVED-kill under the set-theoretic reading (§5.4); row 13's premise superseded by Thm 2.1 | B23-02; B23-03 |
| C35 | plane family `>= 35` | **exactly 35 aff / 34 proj**; `Sigma_Pi` 31 aff / 30 proj | B23-03 L8 |
| C36 | classification OPEN | `closure(D45° ∩ P5) = T1 ∪ T2` PROVED; boundary OPEN (G-A1) | B23-03 Thm 2.1 |
| C37 | cap-minor vanishing on the plane family OPEN | **PROVED** (Prop. 2.5), on the determinant part | B23-03 Prop. 2.5 |

**Informational (not mismatches).**
- C42/C43's lineage note "B23-01 in flight" is out of date. The labels stand.
- C13's citation points at S19. The wording is in B22-10 §6 row 1, which S19 summarises.
- GAPS G-17's description of the evidence as "mod `2^31 − 1`" is wrong: the rank was exact (§2.1).

**Hand spot-checks.** C03 (B22-10 L303–311), C37 (B23-03 L306–323), C42 (the "would require"
wording), C45 (the LMR dependence, §7).

### 6.2 B23-05 `CHANGES.md` (`bbd1d12e`, sha256 `b9d6daff…`)

**Count: 7 paper edits (P1–P7) checked, against 8 hunks of `git diff 82633a60 bbd1d12e --
paper/det3-conductor.tex`.** Every hunk is covered by an entry (**0 unauthorised hunks**), and every
entry is present in the diff. B23-05's three corrections to the integrator's brief also verify:
- the remark numbers 4.7 and 5.10;
- no `README_public` file has ever existed;
- none of the 20 paper versions mentions "rigidity" or "TOTAL_G".

**Fully authorised: P1, P2, P3, P6.** P2 contains one gloss, "we give no reference": it is true of
the paper and absent from the record, and harmless.

**Mismatches (3).**
- **P4 and P5 — incomplete authority.** They cite `boundary_deficit.html` session 9 ("derived, not
  proved") and omit that session 10 of the same file upgraded `m₂ = 9` "from derived to confirmed".
  - B23-05 itself logs the conflict as G-S3, and READINESS lists it as blocker 3. So it is
    disclosed, not hidden.
  - The edits keep "not proved", which is defensible because "confirmed" is a computational
    cross-check. But the CHANGES entries should cite session 10 too.
- **P7 — attribution not supported by the record.** The new sentence says the predicted total at G
  "rested on the fits refuted in (b)". I checked `PROJECT_NOTES.md` at `82633a60`:
  - L755 logs `TOTAL_G` in session 13;
  - L775 carries it through session 14;
  - L829 withdraws it as having "rested on the refuted fits", with no letter.

  Session 13/14 is the det²-slot hypothesis, which is (a). The record supports "(a)", or no
  letter. It does not support "(b)". **One-word edit for the author.**

**Not walked line by line:** README rows R1–R6. They lie outside the `.tex` diff. Their
PROJECT_NOTES anchors were spot-checked by the delegated reader (§11, negative 3).

---

## 7. Priority 6 — the four lineage gaps, priced and ranked

The brief calls them "B23-04 G-15". In `GAPS.md` they are G-14 (deficit lemma), G-15 (LMR at the
base rung only), G-23 (Astra) and G-29 (the pre-Batch-15 documents). That is an integrator
mislabel (§9).

| rank | gap | Paper 3 rows | what closing costs | status after this review |
|---|---|---|---|---|
| **1** | **`n = 3` positive control, base rung `i_det((19,7,2^5), 12) >= 1` from LMR** | C45 (Thm 8.1, labelled PROVED) | **A reading.** LMR's construction at this weight: confirm that the LMR module is non-vacuous at `(19,7,2^5)`, `δ = 12`, and state its read-status at the point of use. B23-06 read LMR Thm 1.0.1 PRIMARY, but that is the `dc̄ >= m²/2` bound, not the module at this cell. `lmr_cell.md` §3b cites "LMR's own value" `a = 6`. About one reviewer-hour, no pilot. Record-internal alternative: a proof that the exhibited `U_D` lies in `I(D)`. s62 is explicit that its finite-point vanishing is Schwartz–Zippel evidence, not membership, so this needs an injective evaluation set: B22-01-sized, one or two pilots. | **OPEN.** Until closed, C45's `D = +1` at the base rung is CONDITIONAL on LMR at this use, and every rung above it inherits that. |
| **2** | **Astra five-block theorem (Thms 8.1, 8.2, Cor. 8.3)** | C24 (Thm 4.12) | **A reading plus a small independent evaluator.** §§3–8 of the Astra REPORT are about 200 lines. The all-degree content is the identity `N_w = L_w C` and the sumset lemma (8.1), both short. The Astra report prices its own review at "a short symbolic/weight-identity audit; exact pilot under five seconds". A replay of `pilot_exact.py` would not be independent, so it needs new code for the weight formula and (8.1). One review slot-part plus one pilot. | **OPEN.** Not closed here: longer than minutes, and no pilot remained. |
| **3** | **Washout results** | C32 (Record 5.2); C33 (Record 5.3) | C32 needs Thm 2's premise (Jacobian rank 35 at `r = 5`) plus the restriction lemma, Lemma 1 and Thm 3, which are proofs I read. C33 (`degree8_global`) is a separate integrator reconciliation of several batch-13 producers. | **C32 CLOSED here.** Pilot 2, with code written here, a fresh seed (20260919) and two primes, gives ranks **4, 10, 20, 35** at `r = 2..5` (full, so `Phi_r` is dominant by Lemma 1) and floor **50** at `r = 6`, matching the recorded table. I read and re-derived the restriction lemma, Lemma 1 (generic smoothness; a modular rank at an integer point is a floor) and Thms 2–3. A minutes-long replay, so closed as the brief allows. **Residues, OPEN:** Thm 6's exactness (`dim D_6^{per_3} = 50`; the replay is a floor only), and C33. |
| **4** | **Deficit lemma** (`obstruction_power.md` §1, Lemma 1, and (SUR)) | C04 (Lemma 2.4) | A reading. Lemma 1 is the substitution of (RES) into both sides. (PW) and (RES) are the standard facts it names. | **CLOSED here** (READ + INDEPENDENT hand; two lines). (PW)'s non-reductive clause (`C[O_v] = C[G]^H`, `dim (S_λ^*)^H` finite) and (SUR)'s surjection for closed `G`-stable cones are standard and correctly stated. This closes **Lemma 1 and (SUR) only**, which is what C04 uses. Prop. 3, Thm 2 and Thm 5 of that file are not reviewed. Strictly, this is a two-line re-derivation rather than a replay, done within the brief's minutes-long allowance, and I say so. |

**Why this order.** The ranking is by load on Paper 3, then by cost.
- C45 is a PROVED-labelled theorem with an unread dependency.
- C24 is a PROVED-labelled theorem with a single lineage.
- The two I closed were cheap.

**Also noted.** G-29 lists C11, the cap theorem, among the single-lineage rows, and the ledger
drops it. C11 is ADOPTED, not PROVED. Its `n = 3` instance has B22-10 S18's second derivation. It
is not a lineage gap of the same kind, and I do not rank it.

---

## 8. Priority 8a — G19 and B23-03's two unwrapped interpreter launches

**Ruling: not a G19 violation.** [READ]
- B21-10 R22 defines G19 as "no unwrapped execution of a program that performs mathematical
  computation on the objects under study".
- `print('x')` and an empty program perform none. B23-03 disclosed both, with their full text, in
  §1 and §6.

**The definition needs one sentence**, because "a program" is otherwise ambiguous about bare
interpreter launches, and the next case (an `import flint` "to check the version") would be
arguable. Add to G19:

> *An interpreter invocation whose full program text is recorded in the packet, which imports
> nothing beyond the standard library, and which computes nothing on the objects under study
> (version probes, `print`, syntax or `ast` checks, JSON field inspection) is not a numerical run.
> It needs no wrapper and consumes no launch, and its text is listed verbatim in the resource
> table. An invocation whose text is not recorded is presumed numerical.*

Under this sentence, B23-03's two launches comply. B23-01's "an `ast` parse check; JSON field
inspection" complies **if** its text was recorded. It was not quoted, so that is a disclosure
defect, not a violation.

**This session** ran no interpreter outside the wrapper. Text extraction from the ar5iv HTML used
`sed`/`tr`, and hashing used `sha256sum`.

---

## 9. Priority 8b — the integrator's record (`docs/b23_12_ledger.md` @ `60a88025`, sha256 `6fffc282…`)

**Transcriptions: mostly faithful.** Every packet hash quoted in the ledger matches. These
transcriptions are exact:
- B23-01's numbers, controls, candidate and labels;
- B23-02's mechanism, prices and labels;
- B23-03's families, dimensions, margins and prices;
- B23-06's facts and counts;
- B23-05's five blockers.

**The four admitted errors.**

| admission | verdict |
|---|---|
| `dc`/`dc̄` conflation | **accurate** |
| criteria written on the wrong axis (B23-02) | **accurate**. §8.7 calls the other failures by the same name, but §8.4's was a control specification in the brief, not an axis. |
| criteria not written for two slots | **the count is wrong: three** (B23-03, B23-04, B23-05). The explanation "fired in the gap between the board being drafted and this ledger being opened" contradicts the ledger's own §9: B23-03's worktree was created after the ledger opened, and its provenance is 20:47:28Z. |
| three wrong references in the B23-05 brief | rows 1–2 **accurate**. Row 3 **inaccurate**: "the paper never mentioned any of them" is wrong about `V^h_σ` (CHANGES.md: `rem:fails` (a) was always present). "The producer added them to `RETRACT_NOTES.md` and `docs/rigidity_theorem.md` instead" is wrong. The commit touches no such file; the retractions went into the paper (P7) and `README.md` (R6). |

**Further integrator errors the ledger does not admit.** I checked each at the ledger lines.
- **E1 — the "projective ≥ 35" misattribution** (L40, L204–209; §3.0).
  - The mislabel was the integrator's own brief, and the ledger pins it on B22-10.
  - L40 repeats it in the ledger's own state table.
  - "B23-03 finds the reverse" is false. B23-03 correction 2 **agrees** with B22-10 §7.
- **E2 — "(G-15)" for the four lineage gaps** (L89–93; §8.10 L499). They are G-14, G-15, G-23 and
  G-29. G-29 names six rows (C04, C11, C24, C32, C33, C45), and the ledger drops C11.
- **E3 — "one in the reviewer's packet"** (L489–491). Both G-17 and G-18 are in B22-10. The §4
  heading "two committed packets" is also wrong.
- **E4 — times labelled UTC are local (UTC−4).** Examples:
  - "~15:00 UTC" for B23-01's transcription, while B23-01's provenance is 18:44:32Z and its pilot
    started 18:50:52Z;
  - B23-06 "~17:45" against its 21:12:01Z start.

  Every "UTC" in the ledger's timeline is about 4 h early.
- **E5 — §3 is stale against §4.** L40–42 still say the cap minors on the second family are OPEN
  and rows 1–2 are "PROVED-kills only at `N = 5`", after §4 L212/L239 record Prop. 2.5 and Thm 3.2.
- **E6 — stale rows in §5 and §7.** B23-03/04/05 are "READY, NOT LAUNCHED" beside COMPLETE rows.
  "B23-04 (superseded row) RUNNING" is still present.
- **E7 — §8.10 L481–483.** It credits B23-02's three-kinds caveat as "carried correctly into prose"
  by B23-04. B23-04 opened no Batch 23 output (its GAPS §A), and its caveat is about its own thesis
  (G-16).
- **E8 — the "convergence" paragraph** (L493–496). G-17 itself says B23-03's brief assigned the
  question. That is not two slots independently reaching one defect. Minor.

**Loosened transcriptions (minor).**
- B23-02: "none lies in a hyperplane" drops "scheme-theoretically". The Hilbert–Burch qualifier is
  dropped, and "an ASSESSED summary … not a theorem that no other mechanism exists" is shortened.
- B23-03: "`T1 ⊄ T2` is certified". The packet says PROVED, with two UNREAD-CLASSICAL facts.
- B23-06: "no separating equation sits below degree 900" is scoped in the packet to length-5 cells
  under Conjecture 2. "Pin `dc̄(per_3)`" overstates `>= 6`.
- B23-01: "the extra are the controls". Three of the 54 were the sixth node.
- B23-05: "equivalent to Cor. 7.2 with Prop. 7.3" is B23-05's own over-strong wording, transcribed
  faithfully (see §4.3). The ledger's aside "corroborates B23-06's `dc̄(per_3) >= 5`" is the
  integrator's own gloss inside a transcription, without attribution.
- The brief's control specification for B23-01 ("replayed at `P₂`") was untestable as written.
  B23-01 caught it before the run (§5.1).

**Verdict.** The ledger is a usable record of **what each packet found**. It is **not** a reliable
record of **who said what** (E1, E3, E7), of **when** (E4), or of its **own current state**
(E5, E6). G28 in §10 addresses the first two.

---

## 10. Priority 9 — gates, and the Batch 24 ranking

### 10.1 Gates

**G1–G26, G9′, G14′, G15′, G20′ stand.** G19 gains the sentence in §8. Two additions, each traceable
to a defect above:

- **G27 — conditions inferred from modular data state their direction.** A statement about the
  rational rank, or rational truth, of something known modulo primes says "requires", "only if" or
  "implies", never "iff" or "exactly when", unless both directions are proved. (§2.2: B22-10 S11
  and §3.2, and again B23-01 §1.5(b) and §5.)
- **G28 — the integrator's record meets the producer gates it enforces.** Specifically:
  - (a) a ledger or brief sentence that attributes a statement to a packet quotes it with
    `file:line` at the pinned commit;
  - (b) times are UTC with `Z`, copied from receipts, or marked local;
  - (c) a brief's dimensions carry their convention (G24).

  (§9, E1 and E4; §3.0.)

The G-17 lesson (a method misdescribed in a GAPS entry) is covered by G26 plus G28(a), and needs no
gate of its own.

### 10.2 Batch 24: what the record supports, in order, with prerequisites

No cell is nominated.

1. **(f-1) Paper 1 blockers** (author work, no slot needed):
   - the attribution, in §4.4's wording;
   - G-S1, G-S2, G-S3;
   - P7's "(b)", which should read "(a)" or carry no letter;
   - the reading of IK Lem. 5.2.

   This is cheap and correctness-critical, and blocks arXiv. Its prerequisite is this ruling.
2. **(b) Lineage gaps, C45 then C24** (§7). This is one review slot, at about one reading and one
   pilot. It is a prerequisite of (f-3), since Paper 3's Thm 8.1 and Thm 4.12 are labelled PROVED.
   - Attach the **`N = 5` Kleiman discharge for row 1** (§3.2): one pilot of seconds.
3. **(f-3) Paper 3 corrections.**
   - C23, C30, C35, C36, C37 go to B23-02/B23-03 as ruled here.
   - Corrigenda K1–K4 apply to C42 and C37's lineage notes.
   - The "right-way corner" sentence is scoped to the determinant part (G-A1).
   - Prerequisites: this review, and (b) for C24/C45.
4. **(a) The small-tail question.** B23-06 proved that a cell's cost depends on its tail, not its
   degree. Whether a separating equation can lie in a small-tail cell has no price at all.
   - This is a theory slot, paragraph-first.
   - It is the **prerequisite of every feasibility estimate at `(3, n >= 5)`** and of any future
     cell nomination there.
   - It is not a prerequisite of anything at `(3,4)`, `N = 5..8`.
   - It is ranked below items 1–3 only because those are cheap and fix standing statements.
5. **(c) G-A1, the boundary.** A theory slot, heavy, and EH-conditional (§3.3). It decides whether
   A.3 holds in full, so it is a prerequisite of any claim that the cap-minor lift target governs
   all of `D45 ∩ P5`. It is not a prerequisite of (a), (d) or (e).
6. **(d) Row 2 at `2 <= j <= N−4`.** B23-03 prices it. **Item 1**, a padding-side ceiling on
   `rank d_j` (theory), is the prerequisite of items 2–3 (pilots and a heavy lease). Without it
   the pilots give only MEASURED comparisons. Fund item 1 only.
7. **(e) The three-kinds theorem attempt.** B23-02's summary is ASSESSED. A theorem needs a
   definition of "mechanism" that does not make it vacuous. Its prerequisites are (c) and (d):
   both are open cases any such theorem must cover. Last.

**(f-2) Paper 2 repair.** No Batch 23 packet concerns Paper 2, and I read none. I do not rank it.

---

## 11. Honest negatives

1. **Session 1 is unattested beyond its files.** I have its pre-verdicts (timestamped in-file), its
   two scripts, its outputs and its two wrapper receipts. I have no record of its unwrapped actions
   or of what it read beyond what the pre-verdict file lists.
2. **BI and Landsberg were read in the ar5iv rendering, not the PDF bytes.** The PDF hashes pin the
   version only. A reader with a PDF text tool should confirm §7.1 against the v2 PDF. I do not
   expect a difference: the rendering hash is identical across two independent fetches.
3. **Delegated walks.**
   - §6.1 and §6.2 rest on delegated walks, spot-checked by hand at the rows and lines named there.
   - In §6.2, the README rows R1–R6 were spot-checked, not walked.
   - I did not re-walk all 46 CLAIMS rows myself.
4. **Not replayed.**
   - B23-03's Thm 2.1, `T3 ⊆ T2` and `T1 ⊄ T2`: read and affirmed only.
   - B23-01's runner evaluations: the pilot re-used the shipped rows.
   - B23-06's pilot.
5. **Not closed:** the lineage gaps C45 and C24, the washout residues (Thm 6, C33), G-A1, row 2,
   and the `N = 5` Kleiman discharge (priced, not run).
6. **The height-2000 ruling scopes a claim whose definition is lost.** If the original search code
   is ever found, it governs the reading.
7. **The three-pilot budget is exhausted.** Nothing further here was computed.

---

## 12. Closing ledger (decisions are transcribed from here only)

Method key: **R** = READ; **RP** = REPLAY; **IE** = INDEPENDENT EVALUATOR (code written here, or a
hand derivation); **pf** = formed before reading the defence.

### 12.1 Corrigenda (G15: these govern; no sealed file is edited)

| id | target (sealed) | reads | now reads | method |
|---|---|---|---|---|
| **K1** | B22-10 S11 (L427) and §3.2 (L175) | "rank 3 **iff** `P` divides every `3 × 3` minor"; "possible exactly when …" | "rank 3 **would require** `P` to divide every `3 × 3` minor of the exact rows at the 70 certified points; it holds **iff some such minor is nonzero over `Q`**" | pf, R + IE |
| **K2** | B23-01 §1.5(b) and §5 transcription | "Rank 3 over `Q` remains possible, exactly when both `P` and `P₂` divide every `3 × 3` minor … at the points used" | "Rank 3 over `Q` remains possible; it would require `P` to divide every `3 × 3` minor of the exact rows at the 70 certified points, and `P₂` every minor at the three points tested" | R + IE |
| **K3** | B22-10 §7 (L313–316) and S18's "strengthened" clause | "The cap minors **do vanish** on the plane family too (rank 64 there, pilot 2)" | "MEASURED: exact `rank M_4 = 64` at one random plane cubic (a floor). **Superseded by B23-03 Prop. 2.5: PROVED** for every member of `Sigma_Pi`." | pf, R + IE + RP |
| **K4** | B22-10 §1 (L65–66) and the §7 header (L308) | "(not 32 — the record is off by one)"; "The record's 'dimension 32' is off by one" | "B22-02's 32 was stated without a convention. It is the correct **projective** value (33 aff). The defect is G24's (a bare figure beside the affine 50), not an arithmetic error." | pf, R |
| **K5** | B23-03 §3.2 and L14 | "PROVED-kill in the whole window `N = 5..8`" | "PROVED-kill at `N = 6, 7, 8` (no adopted input); at `N = 5` PROVED as GKZ Theorem B, modulo Kleiman (ADOPTED, SECONDARY) at `k >= 7`" | R |
| **K6** | B23-02 L5 | "genuine members add no padding point outside `D45`" | add "**scheme-theoretically**". Under the set-theoretic reading, the triple-plane member puts **all** of `P5` in the condition: a direct PROVED-kill | pf, R + IE |
| **K7** | routeA §5.3, CURRENT_DIAGNOSTIC_STATE L50, arc_target CORRIGENDUM C3 | "no small-height rational lift exists (bound 2000)" | the §5.2 sentence (common-denominator reading; per-coefficient lifts exist; the MEASURED candidate has height 2842) | R + IE |
| **K8** | B23-04 GAPS G-17 | "rank measured mod `2^31 − 1`" | "rank computed exactly over `Q` at one point (a floor)" | R |
| **K9** | B23-05 GAPS G-P1 proposed wording | "equivalent to the case of … Cor. 7.2 and Prop. 7.3 in which no admissible set exists" | §4.4's wording | pf, R + IE |
| **K10** | Paper 1 `.tex` @ `bbd1d12e`, `rem:fails` (P7) | "rested on the fits refuted in (b)" | "(a)", or no letter | R |

### 12.2 Rulings

| id | ruling | label | method |
|---|---|---|---|
| B23-10.1 | G-17: B22-10 over-stated on its evidence; B23-04 right to call it OPEN (method misdescribed, K8); Prop. 2.5 closes it | K3 | pf; R + IE + RP |
| B23-10.2 | G-18: the allegation is right; the same defect is in B23-01 | K1, K2 | pf; R + IE |
| B23-10.3 | Dimensions: T2 = **35 aff / 34 proj**, T1 = **33 aff / 32 proj** (exact) | PROVED (B23-03), affirmed | R |
| B23-10.4 | B22-10 never wrote "projective ≥ 35"; its numbers stand; its "off by one" sentences are superseded (K4); "the reviewer was wrong and the record was right" | **REJECTED as stated** | pf; R |
| B23-10.5 | First producer correction of a reviewer: holds for B22-10 §7's one-point sentence and §1's "off by one", **not** for the dimensions. G24 vindicated | ruling | R |
| B23-10.6 | **Prop. 2.5**: `rank M_4 <= 64` on all of `Sigma_Pi`, generic 64 | **PROVED**; generic floor from 3 lineages (B22-10, B23-03, B23-10 p3: 64) | pf; R + IE (hand) + IE (p1, p3) |
| B23-10.7 | The witness has `rank M_4 = 58` (special member; not claimed by B23-03) | MEASURED (exact) | IE (p1) |
| B23-10.8 | **Thm 3.2** at `N = 6, 7, 8`, every `k` | **PROVED**; 8/8 floors, 8/8 ceilings, 3/3 Newton certificates replay | pf; R + IE (p1, p3) |
| B23-10.9 | Row 1 of B22-02 | **PROVED-kill at `N = 6, 7, 8`**; at `N = 5` PROVED modulo Kleiman at `k >= 7` (K5); B22-10's ASSESSED label discharged at 6–8 | R + IE |
| B23-10.10 | `N = 5` Kleiman discharge: `F_0 = x_1x_2x_3x_4 − x_5^4` gives `D(k) = (3k² − 33k + 50)/2 > 0` for `k >= 10`; `k = 7..9` need three floors | tail PROVED (hand); the rest priced, one pilot | IE (hand) |
| B23-10.11 | **G-A1**: boundary points `l·C*` with `C*` smooth are not excluded; routes (a)–(c) of §3.3 | **OPEN** | pf; R + IE (hand) |
| B23-10.12 | Theorem 2.1, `T3 ⊆ T2`, skew-bordered `⊆ T2`, `T1 ⊄ T2` | PROVED (B23-03), affirmed on reading | R |
| B23-10.13 | **Attribution**: Paper 1 Prop. 4.1 is the pigeonhole case of BI Cor. 7.2 and the counting step of BI Prop. 3.24(3); **not equivalent** (Cor. 7.2 is stronger; Prop. 7.3 unneeded and unproved in BI); Cor. 4.2 follows from BI | **RELATED — special case**; blocker for submission; wording §4.4 (K9) | pf; R (BI §7.1, Prop. 3.24; hashes in §4.1) + IE |
| B23-10.14 | The two proofs are the same antisymmetry; one remark sentence, no novelty claim | ruling | pf; R |
| B23-10.15 | B23-04 CLAIMS: **46/46 rows checked; 0 mismatches against cited sources; 5 stale** (C23, C30, C35, C36, C37) | as tabled §6.1 | R (delegated walk + hand spot-checks) |
| B23-10.16 | B23-05 CHANGES: **7/7 edits checked, 8/8 hunks covered, 0 unauthorised; 3 mismatches** (P4, P5 incomplete authority; P7 unsupported letter, K10) | as §6.2 | R (delegated walk + hand check of P7) |
| B23-10.17 | Lineage gaps ranked: 1 C45 (LMR at the base rung), 2 C24 (Astra), 3 washout, 4 deficit lemma | priced §7 | R |
| B23-10.18 | **Washout C32 closed**: Thm 2's premise replayed (ranks 4, 10, 20, 35; floor 50 at `r = 6`; two primes; code written here); restriction lemma, Lemma 1 and Thms 2–3 re-derived. Residues (Thm 6 exactness; C33) OPEN | **CLOSED (second lineage)** | IE (p2) + R |
| B23-10.19 | **Deficit lemma C04 closed**: Lemma 1 and (SUR) re-derived (a two-line substitution; disclosed as a reading within the minutes allowance). Prop. 3, Thms 2 and 5 not reviewed | **CLOSED (second lineage), Lemma 1 and (SUR) only** | R + IE (hand) |
| B23-10.20 | C45 and C24 | **OPEN**; C45's base rung CONDITIONAL on LMR at this use until read | R |
| B23-10.21 | B23-01: design = B22-10 §4; control substitution pre-registered before the run (snapshot `e265f969…` re-hashed; G25) and sound (G21); outcome (b) is evidence and moves no label; `α, β` candidates consistent at both primes | affirmed; K2 | pf; R + RP (arithmetic, p1) |
| B23-10.22 | Height 2000: definition unrecoverable; false per-coefficient (15 and 16 lifts), true common-denominator (none; candidate height 2842) | **SCOPED** (K7); original SUPERSEDED | R + IE (p1) |
| B23-10.23 | B23-06: `dc`/`dc̄` correction confirmed at source (Landsberg 1305.7387 §2, Problem 2.4); visible rows iff `n <= m²/2`; "exactly the LMR range" off at `n = m²/2`, `m` even | CONFIRMED / PROVED, with that precision | R (source) + IE (hand) |
| B23-10.24 | B23-02 Prop. 1.1 | PROVED (UNREAD-CLASSICAL inputs as labelled); row 10 closed under either reading (K6) | pf; R + IE |
| B23-10.25 | G19: B23-03's `print('x')` and empty program are **not** violations; one sentence added (§8) | ruling | R |
| B23-10.26 | Integrator ledger: transcriptions mostly faithful; 3 of 4 admissions accurate; the "criteria not written" count is 3, not 2; **8 unadmitted errors (E1–E8)**, the largest being E1 | ruling | R (delegated audit + hand check at the cited lines) |
| B23-10.27 | Gates: G1–G26, G9′, G14′, G15′, G20′ stand; G19 amended (§8); **G27** (direction of modular conditions) and **G28** (the integrator meets producer gates) added | ruling | — |
| B23-10.28 | Batch 24 order: (f-1) Paper 1 blockers → (b) C45, C24 plus the `N = 5` discharge → (f-3) Paper 3 corrections → (a) small-tail → (c) G-A1 → (d) row 2, item 1 only → (e) three-kinds. Paper 2 not assessed. No cell nominated | ruling | — |
| B23-10.29 | Housekeeping: **negation missing for `b23_10_`** (`.gitignore:51` ignores the three `results/logs/b23_10_*.pid`) | item | `git check-ignore -v` |

---

## 13. Resources, receipts, manifest

Interpreter `..\B15-02\.venv\python.exe` (Python 3.12.10, python-flint 0.9.0). Wrapper
`..\B15-02\analysis\b15_bound.py --seconds 60 --memory-mb 512 --slot 10` (`job_object_enforced:
true`). `PYTHONDONTWRITEBYTECODE=1`.

| run | session | started (UTC) | exit | wall | peak job memory | receipt |
|---|---|---|---|---|---|---|
| `b23_10_p1_witness_tail_height` | 1 | 01:53:24Z | 0 | 2.086 s | 17,149,952 B | `results/logs/b23_10_p1_witness_tail_height_resources.json`, `.pid` |
| `b23_10_p2_washout_replay` | 1 | 01:57:42Z | 0 | 0.031 s | 12,972,032 B | `results/logs/b23_10_p2_washout_replay_resources.json`, `.pid` |
| `b23_10_p3_det_floor_replay` | 2 | 15:42:02Z | 0 | 7.130 s | 207,310,848 B | `results/logs/b23_10_p3_det_floor_replay_resources.json`, `.pid` |

**Budget:** 3 of 3 launches; 9.25 s of 180 s. No cap hit, no crash, no retry.
- **Pilot 3** was pre-registered in `results/b23_10/p3_prereg.md`. Its sha256 was a required
  argument, checked and written as the output's first field (G25).
- Pilots 1–2 carry no pre-registration hash. Their predictions are in the pre-verdict file (Q2,
  Q3), which session 1 wrote 7–11 minutes before they ran.
- Before pilot 3, `Get-Process python*` returned 0, and no `b23_10_p3*` receipt existed.

**Unwrapped actions (session 2), all non-numerical under G19:**
- read-only git and `sha256sum`;
- `curl` fetches of arXiv/ar5iv pages into the scratchpad;
- `sed`/`tr` text extraction;
- reading the python-flint type stubs and the wrapper's argument parser;
- `Get-Process`;
- the bash seal step.

No interpreter was launched outside the wrapper.

**Receipts.** The three `.pid` are ignored at `.gitignore:51`. **Negation missing for `b23_10_`.**
The `_resources.json` and everything under `results/b23_10/` are not ignored.

**Write footprint.**
- Session 1: `analysis/b23_10_p1_witness_tail_height.py`, `analysis/b23_10_p2_washout_replay.py`,
  `results/b23_10/{preverdicts_formed_before_reading.md, p1_witness_tail_height.json,
  p2_washout_replay.json}`, and four receipts.
- Session 2: this report, `analysis/b23_10_p3_det_floor_replay.py`, `analysis/b23_10_seal.sh`,
  `results/b23_10/{p3_prereg.md, p3_det_floor_replay.json, MANIFEST.json, SEAL_LOG.txt}`, and two
  receipts.
- No existing file was edited.

**Manifest.** `results/b23_10/MANIFEST.json` is written by `analysis/b23_10_seal.sh`, which prints
every count into `SEAL_LOG.txt`. It binds:
- this report;
- the four scripts;
- the three pilot outputs;
- the pre-registration;
- the pre-verdicts;
- the six receipts;
- the external sources' hashes;
- the pinned inputs, hashed from the git object store.

Neither the manifest nor the seal log binds itself, and this report does not name its own hash. No
tool memory, chat value or scratchpad value is a premise of any PROVED or CERTIFIED row (G9, G9′).
The external files in the scratchpad are bound by hash only.
