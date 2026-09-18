# B21-12 — Batch 21 integrator ledger

**Opened:** 2026-09-18, by the Batch 21 Cowork integrator (Claude), the same session that ran
Batch 20. **Lives at:** `work\batch15_workers\B15-12\docs\b21_12_ledger.md`, untracked until the
next housekeeping commit. **Governing documents:** `BATCH20_CLOSE.md` §4 (the proposed board),
`B15-10/docs/b21_10_review.md` (`ce2814c74be173b8…`, manifest `9c61c05a067e4d92…`), and the
Batch 20 ledger (`b20_12_ledger.md`, tracked at `da803892`, later edits working-tree). Same six
boxes, same rules: decisions are transcribed from a reviewer's closing ledger only; criteria are
written before the evidence; a cap hit is a cap hit; receipts are never overwritten.

---

## 0. Plain terms

Batch 21 is the reviewer first and alone, then one small producer. The reviewer has reported.
It cleared the one disputed theorem, lifted a condition, corrected two counts without changing
any conclusion, and named the slot the record supports. Nothing in this batch can produce a
gap, a cell, or an equation nonzero on padding.

---

## 1. What this batch cannot produce

Unchanged from Batch 20 §1, verbatim in force: no positive multiplicity gap (the five-row cell
is `D = −1`, two lineages); no asymptotic improvement over LMR; no determinant equation of
length five to eight nonzero on padding. Four achievements, never conflated. "No five-row
determinant equation known to be nonzero on padding", never "none known". `rank T = 3`
CERTIFIED. A floor on `rank(C|_U)` is never a ceiling.

---

## 2. Independently reviewed — second lineage now exists for

From B21-10's closing ledger (R1–R27), and for **nothing else** (G18):

| item | ruling | method |
|---|---|---|
| Theorem A (i)–(v), B20-01 §4.2 | **PROVED** | READ, re-derived, pre-formed (P1) |
| Theorem A's control | **defect named, control PASSES corrected** (`det(g)^{-4}`, not `det(g)^4`; all six ratios `= det(g)^8 = 432557 mod 524287`; all six sealed values reproduced) — **O1 CLOSED** | INDEPENDENT EVALUATOR from the 60 raw runner outputs, ratio predicted before looking |
| C3 (15 evaluations) | PROVED; Corollary A.1's "degree-12 comes free" REJECTED for the four-node variant (kernel `(4,0,−5,0,1)`) | INDEPENDENT, exact over `Q` |
| C8 | PROVED: `1050` gives the degree-12 rows free; `840` decides degree 11 alone and does not | READ + R6 |
| Proposition C | PROVED on inherited `b_L(11) = 70` and the classical FFT | READ |
| C9's number 17,640 | PROVED, two lineages (`dim S_{(4,4,1)}(C^7)`) | INDEPENDENT hand + REPLAY, pre-formed (P2) |
| C9's inequality | **PROVED-with-correction**: `m ≥ 8` (full `G'`), `m ≥ 11` (Levi), not 6/7 and 9; true floor `55,440 = dim S_{(4,4,1)}(C^8)`, `792×` the target — conclusion a fortiori | INDEPENDENT hand + REPLAY |
| `U_-` mixes `z_{-1}`, `z_{-2}` | PROVED (reviewer's own pre-verdict mis-identified `z_{-2}`; corrected in text, pre-verdict file unedited) | READ |
| B20-02 Lemma 6.3 | PROVED, every dimension reproduced | INDEPENDENT hand + REPLAY |
| (T1) Bruns–Herzog 1.6.17 | UNREAD; **condition LIFTED** for the vanishing half Theorem 6.4 needs, by a self-contained proof (§3.2); nonvanishing half (Cor. 6.5 last sentence) stays CONDITIONAL | READ + INDEPENDENT proof |
| (T2) Bruns–Herzog Cor. 2.1.4 | UNREAD-CLASSICAL; condition KEPT; **Theorem 6.4 all-`k` now CONDITIONAL on (T2) alone** | READ |
| Bruns–Herzog 1.5.12 (GKZ Thm B(iii)) | UNREAD-CLASSICAL; the fact PROVED here (§3.2 Step 1); the GKZ packet's labelling defect stands, repairable only by a sibling corrigendum | READ + INDEPENDENT proof |
| Dimca 1210.1795v4 | PRIMARY at statement level; pin `20b96f58…` resolves byte-for-byte; B20-02's transcription accurate; note: Remark 3.6 cites BH 1.6.16 while (T1) cites 1.6.17 — unreconciled in B20-02 §9 | READ |
| G8 | **CERTIFIED** — three certificates replay, ordering hashes recompute; `q_3`, `q_7` CERTIFIED-portable | REPLAY |
| `rho_j(k)` profiles, `N = 5` and `16` | REPLAYED, consistent (`N = 5` deficiencies `0,0,0,0,1,5,15`; `N = 16` `H_2 = 660 / 2830`) | REPLAY |
| Scope in all four packets | holds | READ |
| G8 text ruling | §11 governs — integrator's ruling AFFIRMED; shortfall: §11 does not name the superseded G8 sentences (G15′) | READ |

Still producer-only after this review: everything in the four packets not listed above.

---

## 3. Plausible, unproved — who leans on it

| item | status | who leans |
|---|---|---|
| (T2) grade = height in a CM ring | UNREAD-CLASSICAL, condition kept, exposure nil | B20-02 Thm 6.4 all-`k` |
| (T1) nonvanishing half | CONDITIONAL | B20-02 Cor. 6.5 last sentence only |
| Eisenbud–Harris C1/C3, Ballico 1995 | unchanged from Batch 20 (CONDITIONAL / UNREAD) | singular-locus closure theorem (route-closing only) |
| `b_L(11) = 70` | inherited from `arc_target`, not recomputed by B21-10 | Proposition C |
| The Missing Theorem (B20-01 §5.1) | OPEN; premises (Theorem A, Prop. C) now STAND | O4, the user's exceedance |
| Isotropic-type mechanism for the identity (B20-01 §4.5(c)) | OPEN, testable in one pilot | B21-01 |
| GKZ packet literature table lacks BH 1.5.12 | packet defect, unrepaired | a future sibling corrigendum |

---

## 4. Exact numbers — additions this batch

`det(g)^8 ≡ 432557 (mod 524287)` — the single factor behind all six control failures. The six
sealed values `86170, 71919, 226580; 376209, 469277, 41046` reproduced by an independent
evaluator. C9 floor corrected `17,640 → 55,440` (`792×` the 70-dimensional target). Everything
else as Batch 20 §4.

---

## 5. Gates and slots

**Gates in force for Phase 2 (R23):** G1–G4, G6, G7, G5′, G8–G18; **G19** (no unwrapped
*numerical* run — hashing, manifests, listings and read-only git are not numerical runs; the
budget counts launches, not scripts); **G20′** (the checkable requirement B20-01 already met;
permission mode itself is handover, not gate); **G21** a control is the identity it tests;
**G22** an interpolation claim names what it leaves free; **G23** a dimension inequality names
its ambient; **G14′** UNREAD-SPECIALIST vs UNREAD-CLASSICAL; **G15′** a governing later section
names the sentences it supersedes.

| slot | gated on | met? | state |
|---|---|---|---|
| B21-10 | Batch 20 packets committed; committed bytes; verdicts before defence | all met | COMPLETE |
| B21-01 | B21-10 reported (**met**); slot (a) supported (**met**, R24); expectations and transcription sentences written before the run; one wrapped pilot; G19–G23 | released by R24 | OPEN — `launch_prompts\B21-01.md` |
| O4 (Missing-Theorem run, 840 / 1050 evaluations) | the user's exceedance approval; the Missing Theorem itself (not yet proved) | premises STAND (R24); theorem OPEN | NOT LAUNCHED — user decision |

Not supported by the record (R24): Candidate B; `N = 16` at `k ≥ 9` or `j ≥ 3`; any
cell-selection carrier.

**Housekeeping note (R27, corrected):** `.gitignore:51` ignores `results/logs/*.pid`; the
`b20_*` receipts are tracked because PART 8's rules commits added `!results/logs/b20_NN_*.pid`
negations (B16–B19 precedent) — **not** by force-add. B21's rules commit adds
`!results/logs/b21_*.pid` the same way; `-f` remains forbidden.

---

## 6. Costs

| item | priced | measured |
|---|---|---|
| B21-10 | 3 pilots | 3 wrapped launches, 0.040 s total; peaks 13.37 / 13.05 / 13.81 MB; exits 1 (reviewer's own hook-length indexing bug, relaunched under a new name, receipt kept), 0, 0; pilot 2 emitted 38/39 with the one false a typo in the reviewer's expectation array, caught by the emitted count; no cap hit; no unwrapped run |
| B21-01 (type test) | one wrapped pilot | **measured:** two wrapped launches, 25.98 s of 180 s; first exit 1 at 1.45 s (producer's own dropped reshape), relaunched as `b21_01_p1r_type_test`, failed receipt kept and bound; peak 294.1 MiB; no cap hit; no unwrapped run |
| O4 | ≈ 840 (degree 11 only) or 1050 (degree-12 rows free) runner evaluations; ~10 min laptop; above the 180 s rule | not launched |

---

## 7. Completion states

| slot | state | on disk |
|---|---|---|
| B21-10 | **COMPLETE** | `B15-10\docs\b21_10_review.md` `ce2814c7…`; `results\b21_10\MANIFEST.json` `9c61c05a…`; untracked at `6915ae6f` |
| B21-01 | **COMPLETE** — outcome (2), mechanism CLOSED; REPORTED, producer-only | `B15-01\docs\b21_01_report.md` `fdc709e0f7fb7f1d…` (288 lines; overrun disclosed — §§0–2 saved before the run, not edited after); `results\b21_01\MANIFEST.json` `1944b24d504c087f…` (10 files + 6 pinned inputs); untracked at `878258f2` |
| B21-12 | OPEN (this file) | `B15-12\docs\b21_12_ledger.md` |

---

## 8. Decisions

### 8.1 Criteria for B21-01, written before it runs

B21-01 tests one mechanism: whether the isotropic-type decomposition of the pairing `B`
(B20-01 §4.5(c), C7's four-term type formula) forces the degree-11 identity. Its report is
transcribed only from its pre-registered sentences:

1. **Mechanism found** — a type component of the relevant pairings vanishes identically (as a
   polynomial statement, not a sample) in a way that implies the degree-11 relation: label
   PROVED only with a proof; a sampled vanishing is MEASURED. Then O4 becomes cheaper or
   unnecessary — say which.
2. **Mechanism closed** — the type components do not vanish, or vanish but do not imply the
   relation: a scoped negative; the identity stays OPEN; O4's premises unchanged.
3. **Inconclusive within one pilot** — record PAUSED with the missing computation named.

In no case does the result touch `D`, any cell, or padding. If the pilot cap is hit, the
outcome is "cap hit", not (2).

### 8.2 The decision this ledger exists to make — transcribed from B21-10 §10

Phase 2 OPENS with slot (a) (R24). O1 CLOSED (R2–R4). O2 reduced to (T2) alone plus one
packet-labelling repair (R14–R16). O7 discharged for exactly R1–R27. G8 text ruling AFFIRMED
(R21). Gates as R22–R23. O4's premises stand; its exceedance is the user's.

### 8.4 B21-01, transcribed against §8.1 (2026-09-18, ~01:45 UTC)

**Outcome (2) — mechanism closed.** Sentence 2 of the pre-registration is in §4 verbatim. At
five flag-locus points (the pinned P6 point 0 plus four seeded general points mod `P`), none
of the 32 type blocks of the `t_i`, `s_i` of the four covariants vanishes (160 block tests,
all nonzero — B21-01.6); the degree-11 relation is nonzero in each of its four type
contributions and cancels only in the sum, likewise in degree 12 (B21-01.7). The isotropic
structure of `B` neither forces the identity nor is available to prove it. **The
mixed-pairing identity stays OPEN; O4's premises and price unchanged.** Controls: G21 sealed
replay with `det(g)^{-4}` 6/6 (confirms B21-10 R4 a third time); factorisation control 3/3;
C7 four-term formula vs definition 24/24; covariant route vs pinned runner at flag point 0
6/6. Evidence, not certification: the relation held at four flag-locus points no packet had
evaluated (B21-01.9); `X_11` of every top has rank 2 while every other block has rank 3 at all
five points (B21-01.11, logged as an open lead, not a claim). Everything producer-only (G18).
Nothing touches `D`, any cell, or padding. Scope: five points, one prime, one lineage.

### 8.3 Open for the user

- **O4:** approve the Missing-Theorem run (≈ 1050 evaluations, ~10 min) — *after* someone
  proves the Missing Theorem; the run is decidable only with the basis and the 70 certified
  points. Not fireable yet. Recommendation: fund a theory session for the Missing Theorem only
  if B21-01 leaves the identity open and the user wants it closed.
- The GKZ packet's labelling defect (BH 1.5.12) — a sibling corrigendum is cheap and can ride
  in the next housekeeping pass or be left recorded.

---

## 9. Observation log (2026-09-18, UTC)

- ~01:00 B21-10 reported COMPLETE; review staged, hashed, closing ledger transcribed above.
  R27's premise corrected (negation, not force-add). Batch 21 ledger opened. B21-01 prompt
  written.

---

## 10. Close (2026-09-18, ~01:50 UTC)

**Batch 21 is CLOSED.** Two slots, both complete. The reviewer (B21-10) cleared Theorem A,
named the control's defect, lifted one textbook condition, corrected two counts a fortiori,
certified G8, and set the gates. The producer (B21-01) closed the last cheap mechanism for the
five-row identity with a pre-registered one-pilot test. Plain-language stocktake, completion
table, open items and the proposed next board: `BATCH21_CLOSE.md` beside `BATCH20_CLOSE.md`.
Housekeeping prompt: `launch_prompts\HOUSEKEEPING_B21_PROMPT.md` (PART 9).

**What must not be written.** Not a gap, not a cell, not an equation nonzero on padding, not a
failure. Not "the identity is true" — it held at 19 points and is OPEN. Not "reviewed" for
B21-01 or for any Batch 21 producer claim.

**Where the five-row identity now stands, in one paragraph.** Reduced (Theorem A, PROVED, two
lineages) to one linear relation among three vectors in a 70-dimensional target (Prop. C,
PROVED). Every cheap mechanism that could force it for free is closed: relabelling sign
(B20-01 C6), transversal-slice density (C9, corrected floor 55,440), isotropic type (B21-01).
Every cheap negation test has failed to refute it (19 concordant points, one prime). What
would settle it is the Missing Theorem (an explicit spanning set of `F^L_{-1}` with 70
certified injective points) followed by ≈ 840–1050 evaluations — theory first, compute second,
the user's exceedance. Whatever the answer, it is an existence statement or a closure in a
`D = −1` cell, not a gap.

- 01:45 B21-01 reported; transcribed §8.4. Batch closed.
