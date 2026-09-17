# B20-12 — Batch 20 integrator ledger

**Opened:** 2026-09-17, by the Batch 20 Cowork integrator (Claude), after the post-B19
housekeeping commits. **Lives at:** `work\batch15_workers\B15-12\docs\b20_12_ledger.md`,
untracked until a later housekeeping commit. **Governing documents:**
`Claude_Handover_B15_B18\post_b19_housekeeping_20260917\BATCH20_PROPOSED_BOARD.md` (filled
2026-09-17) and `PRE_AUDIT_FINDINGS.md` (`a2f7514a380c5c96…`). **Model:** `b19_12_ledger.md`
(`129a7c2c67a56e12…` at `f008ac39`).

**Rules this file keeps.** Six boxes, never mixed: §2 what an independent reviewer has actually
accepted; §3 what is plausible and who leans on it; §4 exact numbers per cell, `unknown` where
unknown; §5 gates per slot and whether each is met; §6 priced versus measured; §7 completion
states, where `NOT_TRIGGERED` is a completion state. Decision criteria (§8.1) are written before
the evidence arrives so that the decision (§8.4) is transcribed, not composed. Decisions are
transcribed only from a reviewer's **closing ledger**, never from its intermediate sections.
Where a sealed report and a corrigendum disagree, the corrigendum governs. A cap hit is a cap
hit. Receipts are never overwritten.

---

## 0. Plain terms

Batch 20 is one reviewer first and alone, then two producers with narrow questions, and one
slot deliberately empty. Nothing in it can produce a positive multiplicity gap, an asymptotic
improvement over LMR, or a determinant equation of length five to eight (§1). Its value is a
second review lineage for a record that has run on one, the closing of a paused diagnostic,
and one scoped assessment of a mechanism outside the two proved exclusions.

---

## 1. What this batch cannot produce — stated so no report drifts

- **No positive multiplicity gap.** B20-01's cell `(5,(4^5))` is closed at `D = -1` (`m_pad = 0`
  by padding vanishing, `m_det = 1` by B19-02 §8.1; the degree-five five-row family is fully
  determined: 22 cells at `D = 0`, one at `D = -1`). B20-02 produces a necessary condition or a
  closure, neither of which is a gap.
- **No asymptotic improvement over the LMR benchmark.**
- **No determinant equation of length five to eight written down.** The binding constraint
  B18-06 named, unchanged through four batches.

A **necessary source condition**, a **coefficient equation**, a **separation on padding**, and a
**positive multiplicity gap** are four different achievements. Phrasing that must not regress:
*"no five-row determinant equation known to be nonzero on padding"* — never *"none known"*
(degree-300 five-row `det_4` equations are on the record in three independent places, and the
assessed rank-threshold family also vanishes on padding). `delta_0` is the onset of `I(D_5)`,
quinary cubics, not of `I(D45)` (C10 withdrew the transfer). An evaluation on a general product
above five variables is not a padding certificate; only at `L = 5` does `P_5 = R135`. The Levi
bound `b_L = 74` belongs to `arc_target_dimension_followup`, not to the transverse chain, and
decides nothing (weaker than the trivial ceiling 4). The three transverse functionals are
jointly independent on `M_(4^5)` — `rank T = 3`, CERTIFIED with two lineages (B20-10 R9);
the earlier "not established, only pairwise" line is STRUCK. Do not call
the programme a failure because no gap was found; do not describe necessary-condition progress
as a gap.

---

## 1a. Pre-launch verification record (Step 1, 2026-09-17, integrator)

What the integrator could verify without a shell, and exactly what each check does and does not
establish.

| check | result | establishes | does NOT establish |
|---|---|---|---|
| Housekeeping deliverables present | all 14 files + `launch_prompts\` (4) present in `post_b19_housekeeping_20260917\` | the tree the board expects exists | — |
| Competing board | exactly one `BATCH20_PROPOSED_BOARD.md`; `MANIFEST.json` `part6_status = SKIPPED by user instruction`; the board is listed there as external, hash `fbfc782b7fd8de9d…` (pre-fill) | PART 6 was skipped; no merge question | — |
| Housekeeping directory vs its `MANIFEST.json` | 16/16 sha256 match (10 deliverables + 6 external, pre-fill) | the record is intact as delivered | — |
| Working tree vs recorded committed hashes | 76-file sample staged and hashed: 75 exact; 1 explained — `B15-11/docs/delivery_contract.md` on disk `dfc7b93a017d…` (CRLF), LF-normalised `ee256f38438f…` = committed hash, as `COMMIT_REPORT.md` §2 states | **the working tree matches what the report says was committed** | **that the commits exist** — that is B20-10's, Layer 0 of its dependency chain |
| Sample composition | two whole packets (`fiber_compatibility_20260916` 14/14, `claude_singular_locus_audit_20260916` 13/13); all 16 packet `MANIFEST.json`; the 11 worker files the packets pin; B20-01's and B20-02's named inputs incl. the 4 scripts carrying the `q_3`/`q_7` orderings; every B19 report/review/intake/ledger | — | replay of any computation |
| `.pyc` exclusion | the three `.pyc` in `PRE_AUDIT_FINDINGS.md` §2a appear in no packet add list, no worker add list, no `staged_paths` of any of the 9 commits | exclusion held at staging | that they are absent from the commits — B20-10 sweep |
| "Batch 20" label collision | no `b20`/`batch20` in the 36 refs of `STATE_CAPTURE.json`, in `gct-gpt\`, `gct-gpt\work\` or `Claude_Handover_B15_B18\` directory names | PARTIAL, provisionally clear | `git log --all` message search — delegated to B20-10 |
| Remaining dirty state (`COMMIT_REPORT.md` §§4–5, carried forward) | intentionally uncommitted: `Claude_Handover_B15_B18\` (all); `B15-01/results/b18_01/literature/` (2 PDFs, 2 extractions, 1,072,012 B); the three `.pyc`; `eh1988.pdf` `6b10d8fea80396a7…` + 21 page images in a `%TEMP%` scratchpad; Segal/Dimca PDFs in scratchpads; 34 files under `.codex\attachments\`; the B15-02 interpreter; B15-era run-log residue in every worktree; root `results/b15_integrator/LEDGER.json` (stale); B15-12 untracked page images | carried as-of 16:56 UTC | current state |

**Post-commit state used for slot assignment** (`COMMIT_RECEIPTS.json` `final_verification`,
16:56:30 UTC): all thirteen checkouts 0 tracked changes, 0 staged; stash empty; no index locks;
worker branches 2 ahead (committed) or 1 ahead (untouched) of origin, 0 behind; `origin/*` and
`housekeeping/batch14-close`, `integration/batch13`, `batch15-base`, `batch14-base` unchanged.
This is as of that capture, not live; every session confirms `git status --porcelain` before its
first write.

**Slot assignment (board §9, filled):** B20-10 → `B15-10` / `b15-10-portable-witness` /
`5764e7ffc03439b7f34b912ff9ff984554c0884e`; B20-01 → `B15-01` / `b15-01-ci159` /
`6b16151328d38dc0ce39bcfab51e83459a035d79`; B20-02 → `B15-02` / `b15-02-a1-probes` /
`75ddb900a0b47b911c53f941885bac73b358eacb`. Reason: B15-10 is the board's own choice (clean,
holds no `b19_*` artefact); B15-01/02 by slot-number continuity now that PART 4 has committed
their B19 deliverables. Fallbacks: B15-03, B15-07, B15-08, B15-09 (free before the commits);
B15-04 excluded (permission-denied sandbox cells). No session's model or settings changed.

**Commit pins** are in each launch prompt; the archive is `batch15-launch` @
`82633a60893236fab4fbc317df416e1b8a349005` (tree `e82fd3291d1a2adc8a577647314c251366ff5142`),
prefix `docs/post_b19_20260917/`. B20-10's committed-artifact dependency chain (Layers 0–5) is in
`launch_prompts\B20-10.md`.

**Housekeeping-record note.** The board and the four launch prompts were filled after
`MANIFEST.json` was written; its `external_files` hashes describe the pre-fill versions. The
filled versions supersede them. No sealed packet, report or manifest was edited.

**Concurrent-fill incident (2026-09-17 17:07 UTC) — recorded, resolved by the user.** While
this session was filling the three fields, another session wrote its own fill of the same four
files to disk (all four within one second at 17:07:01–02 UTC; a scripted write, not a hand
edit). Its choices: slots B20-10 → `B15-09` (`44a51860…`), B20-01 → `B15-03` (`dfe4ef64…`),
B20-02 → `B15-07` (`3d2a7c16…`), `B15-08` reserve, explicitly declining every branch PART 4
committed into; a nine-row commit table with short ids and no per-file hashes; no
dependency-chain section for B20-10; label check asserted CLEAR without cited evidence.
Preserved verbatim (sha256 prefixes): board `bf8a53b661816734…` (29,098 B), `B20-10.md`
`5df59b10933020d3…` (8,664 B), `B20-01.md` `f36b021795929134…` (10,876 B), `B20-02.md`
`3b3bd5d077c278da…` (10,643 B), in this integrator's session outputs under
`competing_fill_17-07Z\`. The user chose this session's fill on 2026-09-17; the competing
versions were overwritten on disk with that approval and are **superseded**. Nothing in either
fill touched a sealed file. The lesson goes in the successor handover: check
`device_list_dir` mtimes immediately before every `device_commit_files`, and ask the user to
close any earlier integrator session before starting.

---

## 2. Independently reviewed — what a second lineage has actually accepted

| item | reviewer | state |
|---|---|---|
| Batch 18 slot-01 v1 | slot 10 (Batch 18) | reviewed by a second lineage |
| Batch 18 slots 02, 05, 06 | integrator only (F8–F11) | one lineage |
| Batch 18 slot-10 review, slot 12 | integrator | one lineage |
| Batch 19 slots 01, 02, 11 | integrator reviews on disk (ACCEPT) — `b19_01_review.md` `33b154e6…`, `b19_02_review.md` `e28bcc93…`, `b19_11_review.md` `c9604f9e…` | **one lineage; slot 10 never reported** |
| Batch 19 slot 05 intake, slot 12 ledger | integrator | one lineage |
| The eleven post-B19 packets | none | **no independent adversarial review of anything** (`PRE_AUDIT_FINDINGS.md` §0) |
| Reconciliation A–H | integrator (`PRE_AUDIT_FINDINGS.md` §4) — recomputed recorded integers; re-evaluated no source vector | one lineage |
| Batch 20 — B20-10 closing ledger (`021be68f…`), 2026-09-17 | independent reviewer, verdicts pre-formed where marked | **second lineage now exists for exactly:** R1 commit chain VERIFIED; R2 Levi commutation PROVED; R5 raw-triple counts PROVED; R6 `m_det((4^5),5) = 1` CERTIFIED by independent evaluator; R7 `m_pad = 0` PROVED; R8 `D = −1`; R9 `rank T = 3` CERTIFIED (pilot 2 replay); R10 four source directions CERTIFIED at the level of replayed arithmetic (honest negative 5: no independent evaluator for any source vector); R13 LLV PRIMARY. **Nothing else** — G18 |

The three items deferred to slot 10 since Batch 19 are now ruled: Levi commutation PROVED
(R2, proof-gap note R3); 10,505 count PROVED as a raw-triple count (R5); G5 generalisation
ACCEPTED as G5′ (R22).

---

## 3. Plausible, unproved — and who leans on it

| hypothesis / dependency | status | who leans on it |
|---|---|---|
| Eisenbud–Harris 1988 §1 unaltered by later correction (C3; Ballico 1995 UNREAD after three failed fetches, R12; secondary record suggests corroboration of Atkinson, not correction) | NOT VERIFIED — CONDITIONAL, exposure is a wrongly-closed route only (R11) | `claude_singular_locus_audit` Thm 4.1 (`rho_Z = 0` in every five-row cell), conditional only on C1; downstream the corrected restriction bound in the descent chain |
| EH proofs (C1: PRIMARY at statement level, §3 proofs re-verified by no one, R11, honest negative 2) | CONDITIONAL | same |
| Refined Bézout (Fulton Ex. 8.4.6 / Thm 12.3) | secondary quotation | descent chain |
| Gulliksen–Negard, Kleiman: SECONDARY; Dimca, Segal: PRIMARY (hashed), not load-bearing; HMSV 6.6: POINTER; **Bruns–Herzog 1.5.12: UNREAD, unlabelled load-bearing pointer inside GKZ Thm B(iii)** (R15) | as stated; Thm B(iii) CONDITIONAL until read (G14) | GKZ incidence packet — **carried into B20-02** |
| Dimca Thm 3.1 | VERIFIED-SOURCE, `k = 6` alternative only | GKZ incidence |
| LLV arXiv:2303.09028v3, five-component precision (`D44` = `F1`, degree 320112; others 320, 2508, 38475, 136512) | PRIMARY, CONDITIONAL lifted, confirmed by B20-10 from the hashed text extraction (R13) | B19 |
| D5, reduced (R16): `-12`, `108`, `-14`, `3/896`, `175/36` are recomputed in committed pilot outputs; only `Omega det Q = 315/4` is chat-only, and nothing consumes it | one unconsumed constant; rule = G9 | — |
| D1: `s1_screen_arc` consumed a 12-record `candidates_selected.json` (`11df1d52…`) that exists nowhere; the sealed file is 14 records (`a69c6313…`) | not replayable | routeA s1; everything downstream of s1's selection |
| D3: `q_3`, `q_7` orderings `((0,1,2,3),(0,2,1,3))` exist only as literals in four scripts | CERTIFIED (validity), portability defective (R18) — replayable-from-code, not portable-as-data | every certificate naming `q_3` or `q_7`; **G8, B20-01 hard prerequisite** |
| Pattern-span injectivity (`direct_arc` §4) | conditional premise | the established-identity block B20-01 starts from (unconditional at the general point) |
| `S57` identification behind nine of ten ten-row exclusions; batch-13 `d <= 5` (two primes, not replayed); total-deficit identity `1, 6, 31, 141, 618, 2488` | producer-certified, not replayed | the inherited exclusions |
| Forbidden matrix evidence at `P = 524287` only | single prime | the five-row diagnostic |

---

## 4. Exact numbers per cell — `unknown` where unknown

Canonical source: `CURRENT_CLAIM_LEDGER.md` (`b9390f35277ccfc6…`) and `B15-05/docs/b19_05_intake.md`
(`dc074191e4362231…` at `e3aa25b4`); this box transcribes only what Batch 20 touches.

| cell | `a = m_det` | `m_pad` | `D` | `s` | `U` | `b` | `q` | state |
|---|---|---|---|---|---|---|---|---|
| `(5,(4^5))`, `d = 5` | 1 (PROVED, B19-01 §5) | 0 (padding vanishing) | **-1** | 5 (`dim M`) | unknown | unknown (no certified `b >= 1` anywhere) | unknown | EXCLUDED; diagnostic PAUSED |
| the other 22 degree-five five-row cells | 1 | — | 0 | — | — | unknown | unknown | EXCLUDED (batch 18, integrator-accepted) |
| any cell, type length 5–8 | — | — | — | — | — | no certified `b >= 1` | no certified `q >= 1` | no certified `B < U` anywhere (B19-05 §2.7) |

Five-row diagnostic numbers at `P = 524287` (`POST_B19_STOCKTAKE.md` §7): `dim M = 5`, `g = 6`,
`e(K5) = 322560` (PROVED); source directions `q_3, q_7, e, n02` rank 4 over `Q` (CERTIFIED,
`independence_q3_q7_e_n02.json` `1f0da0af2c8b…`); fifth direction not found (OPEN);
`rank(C|U) ∈ {2,3}`, floor 2 certified (`104967`, `171205`) (OPEN — **B20-01's question**);
forbidden `14 x 3` matrix rank 2 mod one prime, all 364 `3x3` minors vanish, degree-12 rows
rank 1 with ratio pair `(101007, 295818)` (MEASURED, one prime); `rank C ∈ {2,3,4}`, ceiling 4
from `E ⊆ ker C` not from the Levi (OPEN); `rank T = 3`, det `225843` (PROVED); `b_L = 74`
(PROVED, `arc_target_dimension_followup`, decides nothing); `dim F''` not computed (OPEN);
residues `265391`, `275398` are modular coefficients of a sampled relation, not rational
witnesses (no lift to height 2000).

**Five-row diagnostic after B20-01 (producer-only):** `rank(C|_U)` still OPEN; Route 2 at the
reduced price found **no nonzero `3x3` minor** at five generic points mod `P` (570 minors
tested with two degree-11 rows; `rank_mod_P_all_rows = 2`; relation residuals `d11 = 0`,
`d12 = 0` at every point; degree-12 ratios `101007`, `295818` at all five) — **MEASURED, one
prime, not a ceiling**; consistent with the identity, proves nothing. Theorem A (reduction to
the flag locus, 15 evaluations instead of 39): PROVED on paper, **numerical control FAILED**
(`theorem_A_passed: false`; all six reconstructions disagree, e.g. deg-11 `q_3` `300999` vs
sealed `86170`; sign-convention reconstruction, `top_equal_across_k` and `S_3` signs all pass)
— **DISPUTED, open item O1**: either the proof's bookkeeping or the pilot's is wrong; B20-01c's
conjecture (one wrong normalising factor) is a conjecture. C3 and C8 rest on Theorem A and are
CONDITIONAL on O1. Proposition B, Proposition C (`dim V_70 = 70`), C6, C7, C9 (≥ 17,640) stand
as producer-only proofs. The Missing Theorem (§5.1) is the reopening condition; deciding the
identity with it costs 840–1050 evaluations, above budget.

**`N = 16`, `j = 2`, `k = 8` (B20-02b, CERTIFIED exact over `Q`, producer-only):** `rho_2(8) = 16320`
(`K_3(8) = 0`, so `d_2^{(8)}` is injective at a smooth quartic); `rank d_2^{(8)}(det_4) = 15660`,
`dim H_2 = 660`; `rank d_2^{(8)}(z per_3) = 13490`, `dim H_2 = 2830`. **No reversal.** `M_5`
kernels `464` / `932` reproduced exactly (second lineage for the corrigendum's values, which
had entered the record single-lineage). Nothing at `k >= 9` or `j >= 3`.

GKZ-incidence numbers B20-02 inherits (scope corrigendum governs): `D_6` rank 120/105 (`det_4` /
`z per_3`), kernels 0/15; `D_7` 1904 of 1920 / 1650, kernels 16/270; `d_2` at `N = 5` **never
computed**; `D_8` needs the quadratic syzygy space (dim 464 / 932) from the `2176 x 15504`
matrix `M_5`, ≈270 MB dense. Margins: `k=7, N=5` det 299 vs pad 244 (generic 300); `k=4, N=16`
det 226 vs pad 155 (generic 256).

Record corrections carried: `b_L = 74` cited to `arc_target_dimension_followup` (stands);
~~the transverse triple's rank on `M` is 2 or 3, undecided~~ — **STRUCK by B20-10 R9:
`rank T = 3` CERTIFIED, two lineages; L21 governs, L24 and PRE_AUDIT §4D/§7.5 superseded**;
`(4^5)` at `d = 5` is `D = -1`, not `D <= 0` (intake row corrected in B20-10 §10; now
two-lineage, R6–R8); new bounds R21: `(6,(8,4,4,4,4))` `D <= 0`, `(6,(12,8,2,1,1))` `i_det = 0`,
`(6,(4^6))` OPEN;
D2 — `final_arc_diagnostic` §6's "36/36" is actually 30 PASS (harmless, not reproducible as 36).

---

## 5. Prerequisites and gates

| slot | gated on (board) | gate met? | state of the premise |
|---|---|---|---|
| B20-10 | (1) PART 4 commits exist and `COMMIT_RECEIPTS.json` final; (2) reads committed bytes; (3) verdict before defence, and says which | all three **met** (§0 of its review: committed bytes via `git show`, hashes checked; five pre-formed verdicts preserved) | COMPLETE |
| B20-01 | B20-10 reported (met); **G8** D3 certificates; strategy and plan in writing before any pilot; corrigenda before parents; G9, G10, G14, G16, G18 | strategy/plan **met**; **G8 MET** by B20-01c pilot 1 (all checks true: four literals agree, both regenerations, hand-plan orders, `n02` vs `candidates_selected`, four sealed-value replays; three certificates with 64-hex ordering hashes) | COMPLETE |
| B20-02 | B20-10 reported; G17; non-applicability before computation; priced before run; G13/G14 | **all met** — L1 non-applicability for both candidates written before computation (§3–§5); prices in §7.1 before runs; `D_8` PRICED, NOT LAUNCHED (§8); conventions §1.2; literature labelled §9 (T1 Bruns–Herzog 1.6.17 UNREAD, T2 Cor. 2.1.4 UNREAD, Dimca Remark 3.5 PRIMARY) | COMPLETE |
| B20-03 | a concrete mechanism from B20-01 or B20-02 | **not met** by design | NOT LAUNCHED; delta folded into B20-10 |
| B20-12 | this file | — | OPEN |

Batch-wide: one numerical job at a time initially; one process, one BLAS thread; three pilots
per session; 60 s / 512 MiB per pilot; 180 s total numerical wall time per session; symbolic
work and retries count; no lease, no long carrier run; every wrapped run through
`b15_bound.py --seconds 60 --memory-mb 512` with the Job Object enforced. Phase 2 concurrency
only after independent directories, inputs and numerical scheduling are confirmed.

**Approvals that are the user's, not the integrator's:** B20-01's Route 1 alternative (~2,700
runner evaluations, ~20 min); B20-02's `D_8` (~270 MB dense); stopping the batch if B20-10's
dependency check fails; any change to the board's shape; the committed third-party PDFs on
`b15-12-padding-orbit-bounds` (`results/b15_12/sources/`, 1,237,113 B, since `f57316b6`, on the
public remote) — leave and record, or a deletion commit that keeps history; not a retraction,
no rewrite.

---

## 6. Costs: measured versus estimated

| item | priced | measured |
|---|---|---|
| B20-10 pilots | 3 budgeted | **measured (R24):** two wrapped pilots, 1.07 s and 0.08 s, peaks 12.96 MB and 12.69 MB, exit 0/0, no cap hit, no retry, 1.15 s of 180 s; `verify_layers.py` 16 s unwrapped read-only |
| B20-01 Route 1 (density argument on product locus) | 2–4 wrapped pilots, or 70-vector basis ≈2,700 evaluations ≈20 min (**exceeds default**) | unknown |
| B20-01 Route 2 (one nonzero `3x3` full-row minor) | ≈39 evaluations, ≈18 s per new general point | unknown |
| B20-01 D3 certificates | minutes | unknown |
| B20-02 `d_2` at `N = 5` | within default budget (board) — **to be priced by the session before running** | unknown |
| B20-02 wrapped pilots | 3 budgeted | **measured (§11):** 3 of 3 launched; two **cap hits** (memory, FLINT abort under the Job Object — recorded as cap hits, not mathematics; receipts start-only); p3 exit 0, 20.97 s, 285.9 MB, checks 13/13 emitted; wrapped ≈75 s, unwrapped 54.4 s, total ≈130 s (≤175 s worst case) of 180 s |
| B20-01 pilots | 3 budgeted; Missing-Theorem route 840–1050 evaluations (exceedance) | **measured (§9):** p1 6.524 s / 165.1 MiB exit 0; p2 28.887 s / 393.9 MiB exit 0 (control failed); p3 35.546 s / 263.1 MiB exit 0; 70.96 s of 180 s; 3 of 3; retry not used; no unwrapped run; no cap hit |
| B20-02b `D_8` at `N = 16`, blockwise | priced 21.2 MB / ≤ `1.2 x 10^8` ops | **measured:** one wrapped run `b20_02b_p1_d8_blockwise`, 3.35 s, 92.2 MB peak, exit 0, all 2449 + 6757 blocks exact over `Q`, no modular fallback, 15/15 checks emitted; no unwrapped runs |
| B20-02 `D_8` at `N = 16` (pricing row, superseded by the run above) | **PRICED** (`p3_price16_blocks.json`): torus grading splits `D_8` (`16320 x 248064`) into 2449 blocks, largest `192 x 528`, 21.2 MB all blocks, elimination cost ≤ `1.2 x 10^8`; at `z per_3` 6757 blocks, 2.3 MB. Fits the default cap by the price. **NOT LAUNCHED — user pre-approval is the gate (G17)** | no rank computed |
| Post-B19 receipt gaps carried (D8) | — | two aborted check-2 starts and the ImageMagick render have no receipt; failed P7 survives only as console text (`exit 1, 0.6 s, 94,101,504 B`) |

---

## 7. Completion states

`NOT_TRIGGERED` is a completion state, not a failure. A report on disk is not an accepted
result: `REPORTED (unreviewed)` moves to `ACCEPTED (scoped)`, `CONDITIONAL` or `REJECTED` only
on an independent reviewer's closing-ledger line.

| slot | state at opening (2026-09-17, after fill) | on disk |
|---|---|---|
| B20-10 | **COMPLETE** (closing ledger R1–R26; status COMPLETE) | `B15-10\docs\b20_10_review.md` `021be68f…`; `results\b20_10\MANIFEST.json` `b8c8ad31…`; two pilot scripts, receipts; untracked |
| B20-01 | **COMPLETE — sealed by B20-01c (Opus, default mode, 2026-09-17 ~22:00 UTC).** Diagnostic PAUSED with the missing theorem stated; G8 discharged; Theorem A's numerical control FAILED (open item O1); Route 2 found `rank(C|_U) = 2` at five generic points (MEASURED, not a ceiling). Report `e5f426410f6e5dff…` (54,708 B, §§0–8 untouched, §9 from receipts, §11 completion log); manifest `results\b20_01\MANIFEST.json` `0e5fd02631470e6a…` (20 files + 8 pinned inputs, 0 disagreements); certificates `q3_definition.json` ordering hash `ae832e3d…`, `q7_definition.json` `17b7d324…`, `n02_ordering_hash.json` `61505bd5…`. Producer-only throughout. *Superseded row follows for the record:* PAUSED — INCOMPLETE ON DISK. Theory delivered (report §§0–8, 38,730 B, `2d6e1e2b661e62e3…` as staged, unsealed); **no pilot ran** (auto-mode safety classifier refused every program execution after the inputs were read; read-only git and file writes worked; the session did not route around it); G8 **not discharged**; §9 empty; no hashes; no manifest. Completion is mechanical: three wrapped pilots, fill §9 from receipts, seal — prompt `launch_prompts\B20-01c.md`, **default permission mode, not auto mode** | `B15-01\docs\b20_01_report.md`; `analysis\b20_01_{pinned,flag,p1_definitions,p2_reduction,p3_flag_rows}.py`; `results\b20_01\certificates\` (empty); untracked; HEAD `6b161513` |
| B20-02 | **COMPLETE** — stopped at the board's first stop condition, "a rigorous closure of the chosen candidate"; REPORTED, producer-only (unreviewed) | `B15-02\docs\b20_02_report.md` `15ef389b5eb84074…`; `results\b20_02\MANIFEST.json` `a3798319a1ac18b4…` (18/18 outputs hashed, 2/2 inputs match, 4/4 sibling reads unchanged); four scripts; six receipts; untracked; HEAD `75ddb900` unchanged |
| B20-02b | **COMPLETE** — the one pre-registered question answered; REPORTED, producer-only | `B15-02\docs\b20_02b_report.md` `60ff4be461ad1f3b…` (197 lines); `results\b20_02b\MANIFEST.json` `af2dcbc68a181cad…`; one wrapped pilot; untracked; HEAD `75ddb900`; B20-02 packet re-hashed unchanged |
| B20-03 | NOT LAUNCHED by design | `launch_prompts\B20-03_NOT_LAUNCHED.md` |
| B20-12 | OPEN (this file) | `B15-12\docs\b20_12_ledger.md` |

Inherited: Batch 19 slots 01, 02, 05, 11, 12 COMPLETE (integrator-reviewed only); slot 10
**did not report**; 03, 04, 06, 07, 08, 09 NOT_TRIGGERED. The eleven post-B19 packets: sealed,
corrigenda in force, unreviewed.

---

## 8. The decision this ledger exists to make first: does Phase 2 open?

### 8.1 Criteria, written before B20-10 reports

Transcribe from B20-10's **closing ledger** only. Phase 2 opens if and only if all of:

1. **Layer 0 holds.** The nine commits exist with the recorded parents and trees, and the
   committed blobs hash to `COMMIT_RECEIPTS.json` for every worker path (137) and the sampled
   archive paths. A mismatch on any worker path stops the batch pending re-establishment of the
   record. A mismatch confined to archive paths that no Phase 2 input depends on is recorded,
   not stopping.
2. **No load-bearing dependency has failed.** "Failed" means B20-10 rules a dependency FALSE or
   rules a claim that Phase 2 inherits REJECTED — not merely CONDITIONAL, not merely "unread".
   The named exposure: if B20-10 finds that a later correction alters EH §1 in a way that
   breaks Thm 4.1, the batch **stops** and re-establishing the record outranks new work. If
   B20-10 leaves C3 at NOT VERIFIED (cannot obtain Ballico 1995), that is CONDITIONAL, recorded,
   and Phase 2 may open with the condition carried in both producer prompts.
3. **Phase 2's own inputs survive at the scope the prompts assume.** For B20-01: the
   established-identity block (`PRE_AUDIT_FINDINGS.md` §5), the four-vector independence
   certificate, `transverse_triple_rank3.json`, and `arc_target` Prop 7.1 are not REJECTED. For
   B20-02: the scope corrigendum C1–C12 and Astra Thm 8.1/8.2/Cor 8.3 stand as stated, and P1/P2/P3
   are not REJECTED. A scope *narrowing* is carried into the prompt, not a stop.
4. **Release gates are written.** B20-10 delivers gates for Phase 2 numerical work and an
   explicit ruling on the G5 generalisation (accept, reject, or defer with reason). If it
   defers, Phase 2 opens under G1–G7 as written in Batch 18 and the roadmap's generalisation
   stays an integrator proposal.
5. **D1 and D3 dispositions exist.** Whatever they say, B20-01 launches only with D3 as its
   first task; if B20-10 rules that D1 makes the routeA selection unusable as an input, B20-01's
   prompt is amended to say which certificates are downstream of s1 before launch.

Otherwise: the batch's result is B20-10's report, and this ledger's §8.4 records STOP with the
failed criterion named.

Secondary transcriptions from the same closing ledger: verdicts on the Levi commutation
argument and the 10,505-count (populate §2); the disposition of D1–D9 (update §3); the
per-link primary/secondary/unread labels (update §3); the intake delta and the `D = -1`
correction (update §4); any demotion PROVED → CONDITIONAL (update §§2–3).

### 8.2 Reading of Phase 1

B20-10 reported 2026-09-17 ~18:55 UTC. `B15-10/docs/b20_10_review.md` sha256 `021be68f748e8f05…`
(65,714 B); `results/b20_10/MANIFEST.json` `b8c8ad31d78cfe37…`. HEAD unchanged at `5764e7ff`,
0 tracked changes; write footprint eight untracked paths. Five verdicts pre-formed before
reading the defence (P1–P5, preserved byte-for-byte). Two wrapped pilots, 1.15 s of 180 s, no
cap hit. Transcription below is from §12 (closing ledger) only.

### 8.3 Decision status

DECIDED 2026-09-17 — Phase 2 OPENS, both producers gated.

### 8.5 B20-02, transcribed against the board's stop rules (2026-09-17, ~21:10 UTC)

Read from `b20_02_report.md` §0, §7.2, §8, §10 (labelled ledger), §11 only.

**Stop rule met: "a rigorous closure of the chosen candidate."** Candidate A (higher Koszul
differentials) chosen after written non-applicability for both candidates (L1 PROVED,
producer-only); Candidate B left ABSENT with the reason recorded (L2: every cheap invariant
named is rank-threshold, reversed on padding, or unpriced).

**The closure (L6, Theorem 6.4):** in five variables, for every `j >= 2` and every internal
grading `k`, the maximal rank of `d_j^{(k)}` on `D45` equals its maximal rank on all quartics,
so the rank-threshold ideal of every higher differential on `D45` is the zero ideal and the C5
reversal cannot occur in five variables. Mechanism: generic quinary determinantal quartic has
finite singular locus → Jacobian ideal grade 4 among five partials → depth sensitivity kills
Koszul homology in positions ≥ 2. **Label: PROVED CONDITIONAL** on (T1) Bruns–Herzog 1.6.17
(UNREAD; Dimca 1210.1795v4 Remark 3.5 PRIMARY at statement level) and (T2) grade = height
(Bruns–Herzog Cor. 2.1.4, UNREAD). **Unconditional certificate (L7):** `j = 2, 3, 4`,
`k = 3..12`, exact over `Q` for `k <= 8`, single-prime modular floors equal to the maximum for
`k = 9..12`, at the pinned P2 pencil plus a second independent pencil through `k = 10`.
Corollary 6.5 (L8): `rank d_2(P5) <= rho_2 = r_{D45}^{(2)}` at every `k`. Padding data (L9):
`rank d_2^{(8)} = 146 < 150` exact, `dim H_2(8) = 4`; floors `324 < 340`, `611 < 650` at
`k = 9, 10` — the direction reversal again, as predicted. L10 supplies a second lineage for the
P2 `rank d_1` profile `5, 25, 75, 165, 299, 475, 695` (`k <= 9`).

**What it is not (L12, transcribed):** no gap, no cell, no equation nonzero on padding, no
statement about `N = 16` ranks, no funding recommendation for B. A closure with exact scope —
one of the two complete deliverables the board named.

**Resource record.** Three wrapped launches; two cap hits recorded as cap hits (memory; FLINT
`abort` so the wrapper's receipt is start-only — disclosed). **Deviation, disclosed, recorded
here:** two *unwrapped* bisection runs at `k = 9` reached a 735 MB working set — above the
512 MiB per-pilot memory cap — outside the Job Object; and one unwrapped smoke test. Wall
time was counted (54.4 s) but the memory cap was not enforced on those runs. Nothing
load-bearing rests on them: the certificate (L7) comes from the wrapped p3 run (285.9 MB,
exit 0) and the bisections only chose the exact-arithmetic threshold. G10 was honoured ("no
receipt" lines present). **Rule for the successor:** unwrapped numerical runs of any size are
not permitted; a diagnostic that needs more than the cap comes back for approval like any
other exceedance (proposed G19 for the next board).

**Unreviewed.** Every row of L1–L9, L11 is producer-only (G18). The theorem's proof is short
and its conditional literature is named; a reviewer pass is the next thing it needs.

**User decision opened by this report:** the blockwise `D_8` plan at `N = 16` is priced and
fits the default caps by a wide margin; C5's reversal remains live at `N = 16` (`grade 4` among
sixteen partials gives homology only above position 12). Launching it is a change to the
board's shape (B20-02 has stopped) and is the user's call — as a bounded B20-02b after B20-01
reports (one numerical job at a time), or deferred to the next board.

### 8.8 B20-01c, transcribed from report §9 and §11 (2026-09-17, ~22:05 UTC)

**Mechanical completion done; the slot is COMPLETE and sealed.** Three wrapped pilots, no
retry, no unwrapped run, no cap hit, 70.96 s of 180 s. §§0–8 untouched; §9 from receipts; §11
completion log with contradiction C1 and eight deviations. Manifest `0e5fd026…` binds 20 files
and each pilot's pinned inputs (8 distinct, 0 disagreements).

**Pilot 1 — G8 discharged.** `q3_definition.json` (`ae832e3d…`), `q7_definition.json`
(`17b7d324…`), `n02_ordering_hash.json` (`61505bd5…`); every check true, including the four
sealed-value replays. D3 is repaired going forward; Phase 3 may consume `q_3`/`q_7` as data.

**Pilot 2 — Theorem A's control FAILED.** Recorded, not repaired, per the brief. The sign
convention, the top-degree agreement across `k`, and the three `S_3` signs all pass; every
reconstruction disagrees with the sealed values by what looks like a scalar. **Theorem A is
DISPUTED (O1)**; its corollaries C3, C8 are CONDITIONAL on O1. This is exactly the case the
control was built for, and it is the first item for the next reviewer.

**Pilot 3 — Route 2 did not close the diagnostic.** `first_nonzero: null`; five concordant
rows; `rank(C|_U) = 2` at five points mod one prime — MEASURED, not a ceiling (rank floors are
the only thing evaluation proves). The identity remains OPEN, now with fourteen + five
concordant points and a stated Missing Theorem.

**Two provenance notes from B20-01c (D8-class):** the seal script lives in the session
scratchpad, outside the `analysis/b20_01_*.py` set it binds (its hash is in the log and the
manifest); the seal was re-run twice to correct its own log (line count, generator hash) —
receipts untouched, report hash unchanged.

**Batch state after this row:** every slot has a final state. B20-10 COMPLETE (reviewer);
B20-02, B20-02b, B20-01 COMPLETE (producers, unreviewed); B20-03 NOT LAUNCHED. The batch closes
on the next integrator pass (§11 stocktake, completion table, next-board proposal,
housekeeping prompt).

### 8.7 B20-01, transcribed from report §§7–10 (2026-09-17, ~21:50 UTC)

**Board stop gate reached in substance, not in form.** The board says: if the density argument
is not closed by pilot 2, stop, state the missing theorem precisely, deliver that — a complete
deliverable. The report does deliver it: **Theorem A** (C2, PROVED, producer-only) reduces the
degree-11 identity to the vanishing of one function `F_1` on triples with zero skew block, so a
full degree-11 functional costs 15 runner evaluations instead of 39 (C3); **Proposition B**
(C4) degree-11 parts anti-invariant, degree-12 invariant under `r ↔ c`; **Proposition C** (C5)
the degree-11 target on the flag locus is exactly the 70-dimensional Levi-invariant space; the
symmetry search closes the relabelling-sign mechanism (C6, conditional on the height-2000
search) and names the isotropic-type structure of `B` as the one remaining testable mechanism
(C7); **the Missing Theorem** (§5.1, C8): an explicit spanning set of `F^L_{-1}` with a certified
injective 70-point evaluation set on the flag locus, after which the identity is decidable in
840–1050 evaluations (above the 180 s budget — an exceedance for the user); and **why the
density route cannot substitute** (C9): any transversal slice of the flag cone carries a
function space of dimension ≥ 17,640 against 70, and `U_-` mixes degrees 11 and 12. C11–C12
unchanged (SAMPLED / OPEN). Nothing supersedes anything; R9 honoured.

**But no pilot ran.** The auto-mode safety classifier refused every command that executes a
program after the inputs were read (§2.2); the session did not route around it. Consequences,
all disclosed in the report: G8 not discharged (C10 OPEN — scripts ready, certificates not
emitted); Theorem A has no numerical control (pilot 2 unrun); Route 2 at the reduced price
(pilot 3, 75 evaluations) unrun; §9 receipts table empty; no file hashed; no manifest. Wrapped
budget used 0 of 180 s, 0 of 3 pilots. **The slot is PAUSED with the theory on disk and the
mechanical completion outstanding.** Its mathematical claims stay producer-only, and its
numerical claims do not yet exist.

**Completion (user decision, recommended):** one fresh Claude Code session in *default*
permission mode from `B15-01`, running exactly the four commands of report §10 under the
wrapper, filling §9 from the receipts, hashing, sealing. Zero slack in the pilot count (three
scripts, three pilots); the prompt asks the user to grant one retry of pilot 1 only. Reopening
conditions for the mathematics are the report's (a)–(d); (a) needs a budget exceedance.

**Tooling defect for the successor handover:** an auto-mode session reading this programme's
documents can lose execution for the rest of the session. Producer sessions that must run
pilots should be started in default permission mode.

### 8.6 B20-02b, transcribed (2026-09-17, ~21:45 UTC)

Read from `b20_02b_report.md` §1 (pre-registration), §5 (ledger), §6 (resources). The
transcription sentence pre-registered for this outcome, copied: *"At `N = 16`, `j = 2`,
`k = 8`, no reversal: the padded permanent's second-differential rank is at most the
determinant's, so the ideal of `(rank(det_4)+1)`-minors of `d_2^{(8)}` lies in
`I(Y_det) ∩ I(Y_pad)` by the `d_2`-version of Lemma 3.1–3.2, and the direction reversal holds
one level down at `N = 16` exactly as at `N = 5`. Scope: `j = 2`, `k = 8` only; nothing is said
about `k >= 9` or `j >= 3`."* Also: `d_2^{(8)}(det_4)` is deficient by `660` below `rho_2(8)`,
reported as data, consistent with the five-variable closure argument not reaching `N = 16`.
L1–L5 producer-only (G18). The corrigendum's unassessed list shrinks by exactly this item
(`d_2` at `k = 8`, `N = 16`). Resource record clean: 1 of 3 pilots, 3.35 s of 180 s, no
unwrapped run, no cap hit, no receipt overwritten. **Stop rule met** (the two ranks on disk
with receipts). Nothing further is funded from this line without a new board decision: the
next items (`k = 9`, `d_3`) are sized, not priced in blocks, and the Fitting-ideal
decomposition has no method on the record.

### 8.4 The decision, transcribed against §8.1

| criterion | closing-ledger row | met? |
|---|---|---|
| 1. Layer 0 holds | R1 VERIFIED: nine commits with recorded parent/tree/subject/tip; 244/244 + 137/137 path hashes; 565 manifest values resolve; eleven pins resolve; twelve B19 hashes match; `origin/*` as post-push; "Batch 20" label free | **yes** |
| 2. No load-bearing dependency FAILED | R11: singular-locus Thm 4.1 PROVED CONDITIONAL on C1 (EH primary at statement level, proofs unread) and C3 (Ballico UNREAD, R12); route-closing only, no positive claim rests on it. R13: LLV PRIMARY, CONDITIONAL lifted, five components confirmed. R14: refined Bézout SECONDARY, CONDITIONAL stands. Nothing REJECTED, nothing FALSE | **yes** — conditions carried into both prompts |
| 3. Phase 2 inputs survive at scope | R9 `rank T = 3` CERTIFIED (two lineages); R10 four source directions CERTIFIED (arithmetic replayed), residues SAMPLED; R18 D3 valid but not portable → G8; R15 Bruns–Herzog 1.5.12 UNREAD load-bearing inside GKZ Thm B(iii) → narrowing carried into B20-02; Astra 8.1–8.3 not moved. One scope narrowing, no rejection | **yes** |
| 4. Release gates written; G5 ruled | R22 G5 generalisation ACCEPTED as G5′ (four conditions + `a = 1` exception); R23 G1–G4, G6, G7 stand, G8–G18 added | **yes** |
| 5. D1 and D3 dispositions exist | R17 D1 confirmed, nothing certified rests on s1 alone (no prompt amendment needed); R18 D3 → G8 hard prerequisite for B20-01 | **yes** |

**Decision: Phase 2 OPEN.** B20-01 launches with G8 as hard prerequisite; B20-02 with G17.
Closing-ledger status line: *"Phase 2 may open on this report with G8 … for B20-01 and G17 …
for B20-02."*

**Secondary transcriptions.** R2 Levi commutation PROVED (with R3 proof-gap note: the `|mu| = d`
restriction holds by the scalar subtorus of `L`, `arc_target` §3.2, not Prop 3.1). R5 the
10,505 (`d = 7`) and 424,193,140 (`d = 26`) counts PROVED as raw-triple counts bounding an
enumeration, not `b`. R6–R8 `(4^5)`, `d = 5`: `m_det = 1` CERTIFIED two lineages (independent
evaluator, no project code, constant ratio 192 to recorded values, zero at three padding
points), `m_pad = 0` PROVED, `D = −1` PROVED/CERTIFIED; intake row corrected (§10). R16 D5
reduced: five of six values recomputed in committed artifacts; only `Ω det Q = 315/4` is
chat-only and it is unconsumed. R21 new bounds: `(6,(8,4,4,4,4))` `D ≤ 0`; `(6,(12,8,2,1,1))`
`i_det = 0`; `(6,(4^6))` named OPEN. R25 Layer 4 recoverable today, uncommitted; EH page
images unpinned. R26 wording slips W1–W5 not to be quoted forward.

**Correction to this ledger and to the stocktake (R9).** §1's line "three transverse rows are
globally independent is not established — only pairwise" and §4's "the transverse triple's
rank on `M` is 2 or 3, undecided" were transcribed from `PRE_AUDIT_FINDINGS.md` §4D/§7.5 and
`CURRENT_CLAIM_LEDGER.md` L24. B20-10 rules those wrong: the routeA certificate is a nonzero
`3x3` modular minor (det `225843`) on three certified source vectors, replayed in pilot 2; L21
governs; `rank T = 3` CERTIFIED. Both lines are struck below and the "record correction" does
not enter the board.

---

## 9. Labelled claims of this slot

- **[CERTIFIED, integrator]** The working tree matches the recorded committed hashes on a
  76-file sample (75 exact + 1 explained LF-normalisation) and the housekeeping directory matches
  its `MANIFEST.json` (16/16). Scope: working tree only; commit existence not checked here.
- **[MEASURED, integrator]** No ref, tag or directory under `gct-gpt` carries `b20`/`batch20`
  as of 2026-09-17 17:05 UTC. `git log --all` not searched.
- **[ADOPTED]** All mathematical content in §§1, 3, 4 is transcribed from
  `CURRENT_CLAIM_LEDGER.md`, `POST_B19_STOCKTAKE.md`, `PRE_AUDIT_FINDINGS.md` and
  `BATCH20_PROPOSED_BOARD.md`; the integrator composed none of it.
- **[OPEN]** Everything in §8.

---

## 10. Observation log (2026-09-17, UTC)

- 17:03 link to `swamilaptop` up; `C:\Users\swami\Projects` connected.
- 17:04 housekeeping tree listed: 14 files + `launch_prompts\` (4); single board; PART 6 skipped.
- 17:05 refs (36) and directory trees searched for `b20`/`batch20`: none.
- 17:06 76-file sample staged (two calls, 40 + 36); hashed; 75 exact, 1 explained.
- 17:07 housekeeping directory 16/16 vs `MANIFEST.json`.
- 17:10 board §9, the label-collision line, §2–4 pins, and the three launch prompts filled;
  `<PENDING>` count 0 in all four; no sealed file touched.
- 17:12 this ledger opened; committed to `B15-12\docs\`.
- 17:14 `device_commit_files` of the four filled files refused: device versions changed at
  17:07 by another session (§1a incident). Competing versions re-staged, diffed, preserved.
- 17:2x user chose this session's fill; four files written with the mtime guard overridden by
  that instruction; ledger amended and rewritten.
- 17:4x user decisions: (1) push the nine housekeeping commits to `origin`; (2) the four
  third-party PDFs on `b15-12-padding-orbit-bounds` — option (b), a deletion commit, history
  retained, conditional on a manifest pre-check. Prompt handed to the Claude Code housekeeping
  session as `post_b19_housekeeping_20260917\PUSH_AND_PDF_PROMPT.md` (PART 7). Its receipts
  will be `PUSH_RECEIPTS.json`, `PUSH_REPORT.md`, `PART7_MANIFEST.json`. §5 "approvals" row
  on the PDFs is thereby decided; this ledger stays untracked until a later commit.
- 17:44 PART 7 reported (user relay; receipts on disk: `PUSH_RECEIPTS.json` 24,058 B,
  `PUSH_REPORT.md` 5,209 B, `PDF_DECISION_REPORT.md` 4,878 B, `PART7_MANIFEST.json`).
  **Push: complete.** All thirteen branches fast-forwarded to `origin`, 0 ahead / 0 behind by
  `git ls-remote`; the nine PART 4 commits plus the 15 Sep B19 rules commit on the five
  untouched branches (never pushed before). Sweep clean. Fetch changed no local branch;
  refreshed `origin/main` and added remote-tracking refs for 18 older `s21`–`s48` branches.
  **PDF deletion: NOT made** — the pre-check fired: committed `analysis/b16_12_receive.py`
  opens the Kadish–Landsberg PDF by path from its input registry and sealed
  `source_manifest.json` with no existence guard, so a deletion breaks that verifier on a
  fresh checkout. B15-12 pushed as it stood at `f008ac39`. Reopened for the user with three
  options in `PDF_DECISION_REPORT.md`: delete all four and document the restore step; delete
  the three no script opens (1,086,823 of 1,237,113 B) and keep KL; leave all four. Not a
  Batch 20 gate. §5 approvals row on the PDFs reverts to OPEN. Nothing started for Batch 20.
- Batch 20 slot files unaffected: B15-01, B15-02, B15-10 touched by read-only git only.
- ~22:05 B20-01c reported: sealed (`e5f42641…`, `0e5fd026…`). G8 discharged; Theorem A control
  failed (O1, DISPUTED); Route 2 `rank(C|_U) = 2` measured at five points. Transcribed in §8.8.
  **All Batch 20 slots now final.**
- ~21:50 B20-01 reported PAUSED, no pilot ran (classifier block); report staged
  (`2d6e1e2b…`); transcribed in §8.7; completion prompt `B20-01c.md` written.
- ~21:45 B20-02b reported COMPLETE (`60ff4be4…`, `af2dcbc6…`); transcribed in §8.6. No
  reversal at `N = 16`, `j = 2`, `k = 8`. Outstanding: B20-01 (running); PDF decision (user).
- ~21:30 user approved the blockwise `D_8` plan (G17 pre-approval) as a bounded follow-on
  **B20-02b**, same worktree, one pre-registered question (`rank d_2^{(8)}` at `det_4` vs
  `z per_3` vs `rho_2(8)`, `N = 16`); prompt `launch_prompts\B20-02b.md`. Board shape change:
  one bounded slot added, wrapped-only rule (G19-provisional) written into it. §7 row added.
- ~21:10 B20-02 reported COMPLETE (user relay; report and manifest staged and hashed:
  `15ef389b…`, `a3798319…`). Transcribed in §8.5. Unwrapped-run memory deviation recorded.
  `D_8` at `N = 16` priced, not launched; user decision opened. B20-01 still running.
- ~19:00 B20-10 reported COMPLETE. Closing ledger staged, hashed (`021be68f…`), transcribed
  against §8.1: all five criteria met; **Phase 2 OPEN**. R9 corrects this ledger and the
  stocktake (struck lines above). Producer prompts amended with a Phase 2 release block
  (gates, R3/R9/R15 carry-forwards, one-numerical-job rule); board §9 note appended.

---

## 11. Close (2026-09-17, ~22:20 UTC)

**Batch 20 is CLOSED.** The plain-language stocktake, the completion table, the open items
O1–O8 and the proposed Batch 21 board are in
`Claude_Handover_B15_B18\post_b19_housekeeping_20260917\BATCH20_CLOSE.md`, which this section
points at rather than duplicates. The housekeeping prompt to commit the five packets and this
ledger, push, and settle the PDFs is `launch_prompts\HOUSEKEEPING_B20_PROMPT.md`.

**One sentence per slot.** B20-10: the record held, two lineages now exist for the claims
that carry weight, and the integrator's own "record correction" was the one thing found wrong.
B20-02 + B20-02b: the Koszul-differential family is closed in five variables (PROVED
CONDITIONAL on two textbook citations; certified exactly at ten gradings) and shows no reversal
at `(16, 2, 8)`; the direction reversal holds one level down. B20-01: the five-row identity is
reduced to one named missing theorem with a price; the D3 defect is repaired; the reduction
theorem is DISPUTED because its own control failed; five more concordant points; PAUSED.
B20-03: NOT LAUNCHED, correctly.

**What must not be written about this batch.** Not a gap, not a cell, not an equation nonzero
on padding, not a failure. Not "reviewed" for any producer item. Not "Theorem A is false" —
its control failed, which is a different sentence.

**For the successor integrator.** Three things cost time this session and are worth avoiding:
another integrator session left open raced this one on the same files (check mtimes before
every commit; ask the user to close old sessions first); an auto-mode producer lost execution
for a whole session after reading the record (producer sessions in default permission mode);
and the `PRE_AUDIT_FINDINGS.md` "record correction" on transverse rows was wrong and nearly
travelled into a launch prompt (transcribe corrections from a reviewer's closing ledger, not
from an audit's prose). The bridge tools that worked: `device_list_dir`, `device_stage_files`,
`device_commit_files` with `stagedPath` under outputs (no 404 this session). No shell on the
user's machine; every hash check was done on staged copies.

**Labelled claims of this slot, at close.** [CERTIFIED, integrator] the working-tree hash
checks of §1a. [MEASURED] the label-collision search (closed by B20-10 R1). [ADOPTED] every
mathematical statement in this file, from the packets and B20-10's closing ledger. [OPEN]
O1–O8 as listed in `BATCH20_CLOSE.md` §3. Nothing here is a mathematical claim of the
integrator's own.
