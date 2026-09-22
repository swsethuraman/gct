# B25-02 — Paper 2 repair: false theorem first

**Producer:** Claude (Opus 5), slot B25-02. **Worktree:** `work/batch15_workers/B24-06`, branch
`b24-06-paper2`. **Session:** 2026-09-22T01:59Z – 2026-09-22T03:40Z (UTC, from `date -u`).
**State of everything below: UNCOMMITTED, producer-only, not reviewed.** No Git mutation, no
pilot, no mathematical computation, no `.pid`, no lease, no subagent, no circulation.

## Outcome (preregistered space, ledger §B25-02)

**Outcome (2): B2 repaired from the existing three-clause slab theorem; exact remaining blockers
prevent readiness.** Theorem 9.1 is restated as `docs/blindness_slab.md` Theorem A with every
clause, hypothesis and label mapped; no new mathematics was needed. B3, B4, B1 (checked at
Kadish–Landsberg), B5–B9, B11–B13 and B15's substance are repaired or qualified in the TeX.
Remaining blockers are listed in §6; they include one mathematical qualification this slot had
to introduce (Theorem 6.2's closure statement is now carried as ADOPTED, not proved — §4.3) and
the author-reserved items. **The paper is not ready for arXiv.** It has **not been compiled**:
no LaTeX toolchain exists on this host (§7).

## 1. Preflight and before-state bindings

```
branch  b24-06-paper2            HEAD 0019b2e2359eeabe065dad4271b89f06e2553896 (= baseline)
git status --porcelain --ignored   empty at start (2026-09-22T01:59:18Z)
core.autocrlf=true; .gitattributes: PAPER2_*.md -text; paper/*.tex has no attribute
```

| path | raw working-copy bytes / sha256 (before) | Git blob @ HEAD | blob-content sha256 |
|---|---|---|---|
| paper/det4-onset.tex | 51,891 B, 957 CRLF lines, `7c2bc7365c3aacc75e5d79906a4aaa3364ff015e5bbc91e2f585b1ca45678b7b` | `3e09a841027c6ad2fbd6cc3fc06c5276ce3b0a5d` | `c873c2175ef4e78c99360ccba23de4d61b3f520072a842d942e3b4fffae061ce` (LF; differs from raw by CRLF only) |
| PAPER2_BLOCKERS.md | 28,605 B, `00e3ebbeccfda6d2724b842deca6afe7c0a7c422e07874cfe5763b0db0f81543` | `3736bfe30f8be1767fe6063371e892300b8e64ab` | identical to raw |
| PAPER2_CLAIMS.md | 30,354 B, `6dafcb311d9af7fead7e20d2d157dfb37b4c8d868b739db144556c5af027785b` | `fa0b44dd038c35e8d533c748807c67c23a02fa87` | identical |
| PAPER2_GAPS.md | 14,308 B, `88bb3dfb260218bbfaf86eed8602f320135dced9a1af93e44139bfddb1cc59af` | `b3260b3275c3824f467e15fad10bc06ea718b751` | identical |
| PAPER2_READINESS.md | 4,153 B, `b2e77f8e0e650ea22be43a8ab6a63cd9a936cd829d18e3ec1f7ad0f60e0142f5` | `ec379e8bfb8578530d102e3cdda74bce5f506ebb` | identical |

The TeX raw digest `7c2bc736…` is the one B24-06 recorded; it is the CRLF working copy, not the
blob content. **The historical B24-06 assessment has no packet manifest** (SOURCE_INDEX provenance
caution); none was invented. Its four files are bound above at commit `0019b2e2`.

**Inputs read, with committed locators** (all read by me this session unless marked):

| input | commit : path | blob |
|---|---|---|
| Theorem A | `82633a60:docs/blindness_slab.md` §0–§1 | `b0ee82b2…` |
| notation (`f_units`, `D`, restriction lemma, Prop. 5–6, Cor. 7) | `82633a60:docs/washout_lemma.md` §1, §4–§5 | — |
| containment theorem, ℓ ≥ 5 gate | `82633a60:docs/n4_gate.md` §1–§2 | `1f718f2e…` |
| rows `lmr_ranks`, `lmr_D_upper`, `degree8_global`, `length_bound`, `n4_gate_containment`, `quartic_length_and_eligibility`, `b14_11_quartic_census`, `nchi_*`, `quartic_signed_burnside_size`, `i_det_zero_12_4x5_d8`, `n3_padded_seven_row` | `82633a60:docs/PROVED.md` | `b93a27c7…` |
| cap theorem, §2.2, §4, §5, §6 | `82633a60:docs/onset_conjecture.md` | `89f8abf4…` |
| LMR cell | `82633a60:docs/lmr_cell.md` §1–§3 | `482cd4cf…` |
| (★) criterion, Cor. B, §5 literature | `82633a60:docs/reducible_ideal.md` §0 | `6a5f43d2…` |
| B24-10 review §5, §11.5, §11.9 | `ab2f8a40:docs/b24_10_review.md` (B15-10) | `46edbcb0…`; manifest sha256 `ba6aea51…` matches the ledger |
| B24-02b LMR packet | `5a97317e:docs/b24_02b_report.md`, `results/b24_02b/lmr_quotes.md` (B15-01) | `56f3c4ce…`, `f2e45a2a…` |
| B23-03 Thm 2.1, Prop. 2.5, §2.6 G-A1, §4 | `3bcad666:docs/b23_03_report.md` (B23-03) | — |
| Paper 1 locators | `bc7e62b7:paper/det3-conductor.tex` (B23-05) | `975b59e9…` |
| B17-01 statement only | `01c49022:docs/b17_01_report.md` (B15-01; ancestor of `5a97317e`) | raw sha256 `8812eeef…` |
| e-value context | `82633a60:docs/e4_hunt.md` §2, `docs/s33_review.md` | — |

## 2. Source-reading gate

Beauville was read in the primary (arXiv:math/9910030v2, PDF sha256 `1ba560a5…eb586`) **before**
any Beauville citation was edited. Kadish–Landsberg v1, LMR v1 (hash equal to the record's
`cfc28275…`) and LLV v3 (hash prefix equal to the record's `67b1701f…`) were also read in the
primary. Passages, hashes and limits: `results/b25_02/SOURCE_READING.md`. Findings that change
the paper:

- Beauville contains **none** of Prop. 2.1's dimensions, Thm 7.1 Step 2's nodes, or Thm 7.3; it is
  the source for the two facts Prop. 6.1 uses (Cor. 6.4; (1.9)). B6(a)'s worry is resolved in
  the paper's favour as far as Beauville goes.
- Kadish–Landsberg Thm 1.3 confirms B1 at source.
- LMR: Thm 1.0.1 supports use 1; Thm 2.3.1 + 3.1.1 (+ §3.2's n = 3 example) support uses 2–4;
  Thm 1.0.2 and §3.2's general formula are halved and are not used.
- LLV Thm 2 / Table 2 / Cor. 4.1 identify `F1 = P(D^det_4)` with degree 320112; Cor. 3.1 gives
  `dim D^det_4 = 34`.

## 3. B2 — the repair, with notation mapped

**Before** (`thm:slab`, source lines 692–705 at `0019b2e2`): "For every weight with ℓ(λ) ≤ 4 and
every degree, `mult_λ C[D^det_4] = a(λ,δ)`; hence Δ ≤ 0 on the entire length-≤4 slab" — false at
δ = e (B24-10 §5.1).

**Notation map (record → paper).** Record `mult_f(λ,δ)` = paper `mult_λ C[D^f_k]_δ`, k = ℓ(λ)
(restriction lemma = paper eq. (2.1)); record `det_units = a − mult_det` = paper's new
`i_det(λ,δ)`, the **ideal-copy count** (number of copies of S_λ in `I(D^det_k)_δ`), explicitly
distinguished in the text from the **coordinate-ring multiplicity**; record `D = mult_pad −
mult_det` = paper Δ (Thm 4.1); record `pad_units = a − mult_{R_k}`.

**After** (`thm:slab`, now four items, same number 9.1): (1) Δ ≤ 0 for ℓ ≤ 4 in every degree —
proof by degree-free containment (Thm 3.1 `P_k = R_k`; Prop. 6.1 `R_k ⊆ D^det_k`; surjection of
coordinate rings); (2) `i_det = 0` for ℓ ≤ 3 in every degree (`D^det_k = W_k`, k ≤ 3); (3) for
ℓ = 4, `i_det = 0` only for δ ≤ e − 1, e the generator degree of the principal `I(D^det_4)`;
**e ≥ 10 certified** (rectangular rungs 4, 6, 7, 8 attain `a`; `a = 0` at the other rungs ≤ 9) and
**e = 320112 adopted** from LLV Thm 2, kept separate; at δ = e the generator is an ideal copy of
`S_{(e^4)}`, so the old equality fails there; (4) on the range of (2)–(3), Δ = −pad_units, with the
two strict cells `((8,8,8),6)` and `((12,8,8),7)` named (Δ = −1). Every hypothesis of Theorem A was
checked against its proof in `blindness_slab.md` §1; the containment half relies on the
Jacobian-rank-20 density certificate of `n4_gate.md` §1 (not on Beauville, which is cited as a
second source). **No new mathematics.** The only sentence beyond Theorem A's text is the δ = e
witness, which is B24-10 §5.1's own refutation argument.

Cross-references traced: the §1 "Negative results" paragraph (restated to match (1)–(3)); Prop. 6.1
(its printed inequality was **reversed** — `mult C[R_r] ≥ mult C[D^det_4]` — and mistyped; now
`≤`, `D^det_r`: new finding N1, a dependency of item (1)); the "honest frame" (now cites item (1)).

## 4. Remaining repairs, in the prescribed order

### 4.1 B3, B4, B1
- **B3:** §9 opening and "honest frame" now say length ≥ 5, each coordinate labelled (length:
  proved; first row: proved; degree ≥ 8: measured only), the five-row open region preserved with
  the certified count 4,198 / 2,734 / 2,571; the washout is stated as an interpretation, not an
  impossibility theorem (also in §1 and Rem. 9.3, which now carries the ℓ ≥ 5 and λ1 ≥ δ gates).
- **B4:** `[−4, +1]` → `Δ ∈ [−4, −2]`, CERTIFIED conditional on ADOPTED `dim N13 = 73` (named as
  "the dimension 73 of a rung-13 source space, adopted on two lineages"); the chain is spelled
  out (injective evaluation, three exact ideal copies at `(21,17,2⁷)_13`, `u¹¹` transport,
  `P9 ⊆ R9`). The uncommitted `[−4, −3]` is **not** used. The "two structural facts" are relabelled
  as measured on the sampled kernel.
- **B1:** Cor. 5.3 now gives `mult_λ C[R_r]_δ = 0`, the whole isotypic component in the ideal,
  and "omits every variable" (was "some"); attribution to KL Thm 1.3's first assertion, PRIMARY.

### 4.2 B5–B9
- **B5:** four LMR uses relocated (Thm 1.0.1; Thm 2.3.1 + 3.1.1 + §3.2); Thm 1.0.2 explicitly not
  used; the n = 3 control rewritten: LMR gives `i_det ≥ 1` (a ceiling on mult, not "bounded
  below"), the measured rank gives `mult ≥ 5`, and `Δ = +1` is **PROVED modulo (★)** with (★)
  named as record-internal.
- **B6:** (a) Beauville PRIMARY at both uses; (b) LLV added to the bibliography and cited for e and
  for `dim D^det_4`; (c) the cap label "PROVED modulo Kleiman (SECONDARY), Dimca (PRIMARY,
  statement level), Gulliksen–Negård (SECONDARY), all adopted" is in Thm 7.1's heading, the §1
  paragraph and the abstract (moved out of "We prove:"); (d) novelty: "not found … in one
  literature pass, not as new"; also "values at n = 5,6,7 are new" → "not found elsewhere; no
  priority". A read-status paragraph was added to §1 (G14′).
- **B7:** `\cite{MM}` (Marcus–Minc) removed with its bibitem. Actual use verified: Lemma 3.3 needs
  only a 4-dimensional torus for `per_3` (and the 30-dimensional `G_eff` for `det_4`), both
  proved in the lemma; the full stabilisers (Marcus–May / Botta) are not used, so no unread
  citation was added (proposed optional patch in §6).
- **B8:** Thm 6.2 restated: four-dimensional singular subspaces, `D^det_5`, the compression
  obstacle stated as obstacle, the separation as the count 31 < 35, no HWVs. Prop. 6.1 typed
  `D^det_r`.
- **B9:** Prop. 2.1's garbled formula replaced by Lemma 3.3's actual bound
  `dim D^det_r ≤ min(dim W_r, 16r − 30)`, equality for 3 ≤ r ≤ 6 (Cor. 7 table). Lemma 3.3 rewritten
  from its actual proof (`washout_lemma.md` Prop. 5–6): scope narrowed to `det_4` and `per_3`
  (the record adopts the count beyond n = 4 — new finding N4), upper bound only with equality via
  Jacobian sandwich, and the r = 2 exception stated correctly (commutant of one generic matrix,
  3-dimensional mod scalars; the old "2n − dim" fragment deleted).

### 4.3 B10/B11 — and a qualification this slot had to add
- **B10:** Rem. 6.3 now opens by separating the two enumerated objects (singular subspaces vs
  components of `Proj gr_J R`), notes (ii) does not contradict Thm 6.2, and closes with the
  boundary gap (G-A1, components ≥ 19) instead of "the one thing between … and an unconditional
  theorem".
- **Thm 6.2's closure claim (new finding N3).** The paper's own argument proves only the
  determinant part (actual determinants in `W`: dimension ≤ 31 < 35; = B23-03 Thm 2.1 at fixed l).
  It does **not** prove `R5 ⊄ D^det_5`, because `D^det_5` is a closure and its boundary meeting
  `R5` is unclassified (B23-03 §2.6; the paper's Remark itself said so). The theorem is now titled
  "determinant part"; the closure statement is carried as **ADOPTED** from B17-01 (committed
  `01c49022`, B15-01), which states `lC ∉ D45` for smooth C; B23-03 §4 reads that result as
  ADOPTED and as excluding "one specific C*" only. The paper uses only the existence of one
  smooth witness, the weaker reading. This is a withdrawal of an unsupported "unconditional",
  not a new result.
- **B11:** after Thm 7.1, the Σ_Π statement (B23-03 Prop. 2.5, PROVED; its one-syzygy proof
  sketched in the text) and the consequence: the minors' zero locus strictly contains `D^det_5`,
  they do not identify `I(D^det_5)`; Conj. 7.2 unaffected.

### 4.4 B12–B16
- **B12:** `n_χ ≈ N_S/|Stab|` removed from Thm 8.1; signed Burnside count stated; quotient declared
  neither bound; "senary sextic" → `I_6`, the degree-six invariant of senary quartics, weight
  (4⁶); reach restated as implementation-dependent with one later cell (N_S = 27,009,659).
- **B13:** §1 and Q 10.5 now state `degree8_global` (every r, δ ≤ 8; r = 6 through δ = 9) with its
  single reconciliation lineage and the length window 6 ≤ ℓ(μ) ≤ min(r,δ); no second lineage
  claimed; no clamp at nine appears (none was in the paper; none introduced). The 682 cells are
  labelled measured (G-P2-12). §7.1's saturation condition restored (G-P2-09); Thm 7.3's component
  half now proved in the sketch (G-P2-10).
- **B14:** `\cite[\S]{Companion2}` → `\cite{Companion2}`. Self-locators verified against Paper 1
  at `bc7e62b7` (numbering derived from source order; Paper 1 uncompiled): "Prop. C" does not exist
  → `Prop. 4.19` (length reduction, stated there for det_3; the paper now says the proof applies
  verbatim); cap = `Prop. 4.23`; `Question 8.5` confirmed, and Paper 1 already sketches Thm 7.3's
  frame argument there, so "settles a question left open" was stale (new finding N6).
  Companion/Companion2 locatability remains [AUTHOR].
- **B15:** "second author" removed. Paper 1 already contains the 65 cap, so the sentence now cites
  it and gives the bracket `6 ≤ δ0 ≤ 65` unconditional, `8 ≤ δ0 ≤ 65` given the measured totals,
  with δ0's quinary-cubic scope.
- **B16:** untouched (user's credit decision).
- **Double superscripts** (historical board lines 144 and 874: `\Ddet_r^{\per_3}` =
  `D^{\det}_r^{\per_3}`). Both replaced by `D^{\per_3}_r`, now defined. **Order deviation,
  disclosed:** the first (old L149 / board L144) disappeared when B13 rewrote that sentence; the
  second (Q 10.5) was fixed last. One further double superscript that I introduced in Rem. 6.3
  (`\Ddet_5^{\circ}`) was caught by the mechanical scan and replaced by `D^{\det,\circ}_5`.
- **Also corrected (new finding N2):** the abstract's "maximal minors … of size cap(n)" — they are
  not maximal minors; now "minors of size cap(n) … the rank at a smooth form".

## 5. Disposition table B1–B16

| # | disposition | evidence | edited location (after-state) | remaining blocker |
|---|---|---|---|---|
| B1 | **REPAIRED** | KL Thm 1.3 PRIMARY; `reducible_ideal.md` Cor. B | Cor. 5.3 + attribution ¶ (§5) | none |
| B2 | **REPAIRED** (Outcome 2 core) | `blindness_slab.md` Thm A; LLV Thm 2 PRIMARY; B24-10 §5.1 | Thm 9.1 + preamble + proof; §1 "Negative results"; Prop. 6.1 | e = 320112 stays ADOPTED (G-P2-01) |
| B3 | **REPAIRED** | `n4_gate.md` §2; `PROVED.md` rows; B24-10 §5.2 | §9 opening, "honest frame", Rem. 9.3; §1 washout ¶ | degree ≥ 8 is measured only (stated) |
| B4 | **REPAIRED** | `lmr_D_upper`; B24-10 §5.2 | "What the length-nine cell reduces to" | `dim N13 = 73` ADOPTED (stated) |
| B5 | **REPAIRED, qualified** | LMR PRIMARY (this slot); B24-02b | §1 intro, §9 frame, n = 3 control, length-nine ¶¶ | (★) open pending B25-05; n = 4 16 → 9 transfer flagged (F3) |
| B6 | **REPAIRED (a–d)** | Beauville, LLV PRIMARY; B24-10 §5.3 | Prop. 6.1; Prop. 2.1; Thm 7.1 heading; abstract; §1 status ¶; §5, §7 novelty wording; §7.3 intro | Dimca/Kleiman/GN not re-read (record statuses carried); wider prior-art search for Thm 7.3 not made |
| B7 | **REPAIRED** | `washout_lemma.md` Prop. 5–6 | Lemma 3.3 + proof; bibliography | optional Marcus–May/Botta citation needs a verified reading (§6 P2) |
| B8 | **REPAIRED** | `singular_spaces.md` via B24-06; B23-03 | Thm 6.2 + following ¶¶; Prop. 6.1 | — |
| B9 | **REPAIRED** | Lemma 3.3's proof; Cor. 7 | Prop. 2.1; Lemma 3.3 | — |
| B10 | **QUALIFIED** | B23-03 Thm 2.1, §2.6 | Rem. 6.3 opening, (ii), (iv) close; Thm 6.2 closure ¶ | G-A1 OPEN; closure statement ADOPTED (N3); B23-03 is a sibling branch [AUTHOR] |
| B11 | **REPAIRED** | B23-03 Prop. 2.5 | ¶ after the corank measurement, §7 | B23-03 citation route [AUTHOR] |
| B12 | **REPAIRED** | `nchi_*`, `quartic_signed_burnside_size`, `stabiliser_reduction.md` §4.3 | §1 engine ¶; Thm 8.1; ¶ after it | — |
| B13 | **REPAIRED** | `degree8_global`, `length6_record`, `length_bound` | §1 washout-persists ¶; Q 10.5; Q 10.2 labels | — |
| B14 | **PARTLY REPAIRED** | Paper 1 source @ `bc7e62b7` | eq. (2.1) locator; §7.3 intro; `\cite{Companion2}` | Companion/Companion2 unlocatable to a reader [AUTHOR]; Paper 1 numbering uncompiled |
| B15 | **REPAIRED** | Paper 1 Prop. 4.23 and δ0 bracket | §1 cap ¶ | — |
| B16 | **UNTOUCHED** by instruction | — | — | user credit decision |

## 6. Remaining blockers to readiness, and proposed patches

1. **No compile** (G-P2-17). The after-state is checked mechanically only (§7).
2. **Theorem 6.2's closure statement** rests on B17-01, ADOPTED and read differently by B23-03;
   needs review or an accepted citation route (and G-A1 remains OPEN).
3. **(★)** for the n = 3 control (B25-05 pending) and the flagged n = 4 transfer (F3).
4. **Sibling/uncommitted sources** named in prose without a public locator: B23-03 results (Rem. 6.3,
   §7 Σ_Π), B17-01, the 4,198-label census, `lmr_D_upper` chain — all land under `Companion2` /
   "the programme" / Data availability; G-P2-13 (repository URL, committed artefacts) unresolved.
5. **[AUTHOR]:** B14 companion references; B16 acknowledgement; whether Paper 2 may cite B23-03.
6. Paper 2 vs Paper 3 overlap (BLOCKERS §2) not resolved (out of scope).

**Proposed patches (not applied):** P1 — none to any bibliography outside the TeX (the TeX carries
its own). P2 — if the author wants the full permanent stabiliser cited, add Marcus–May and Botta
**after** a primary reading; bibliographic data not verified here, so no entry is proposed.

## 7. Verification and build

- **Compilation: unavailable.** No `pdflatex`, `latexmk`, `tectonic`, MiKTeX or TeX Live on this
  host (checked `which` and standard install paths). No build log or PDF exists; none is faked.
- **Mechanical checks** (administrative script `results/b25_02/texnum.py`, not mathematics):
  33 labels, no duplicates, **0 undefined references**, every cite key has a bibitem and every
  bibitem is cited (LLV added, MM removed), brace balance 0, `$` parity even, no bare `\cite[\S]`,
  theorem numbering unchanged for every numbered result (2.1, 3.1–3.4, 4.1, 5.1–5.3, 6.1–6.3,
  7.1–7.3, 8.1, 9.1–9.3, 10.1–10.5), no remaining `}^{…}^`-type double superscript found by regex.
  Outputs: `mechanical_check_before.txt`, `mechanical_check_after.txt`.
- **Verification kind:** READ of all record inputs; PRIMARY reading of four sources; INDEPENDENT hand
  arithmetic for Ω(6,4), Ω(4,3) and the Thm 1.0.2 halving. No REPLAY and no INDEPENDENT EVALUATOR.
- Line endings: the TeX remains uniformly CRLF in the working copy (1,239 lines, 1,239 CR), as at
  baseline.

## 8. After-state bindings (all UNCOMMITTED)

Digests of the packet and edited files are in `results/b25_02/MANIFEST.json` (the manifest does
not hash itself). TeX after-state: see manifest; full diff `results/b25_02/det4-onset.diff`.

**Files modified:** `paper/det4-onset.tex`, `PAPER2_BLOCKERS.md`, `PAPER2_CLAIMS.md`,
`PAPER2_GAPS.md`, `PAPER2_READINESS.md` (each: an appended B25-02 section; historical text
preserved). **Files created:** `docs/b25_02_report.md`, `results/b25_02/{MANIFEST.json,
SOURCE_READING.md, det4-onset.diff, mechanical_check_before.txt, mechanical_check_after.txt,
texnum.py}`. Nothing else in the tree changed. Scratchpad (outside tree): downloaded PDFs and
text extractions.

**Tool memory:** consumed none as a premise. Created/updated one memory entry recording that
`pdftotext` is available (correcting an earlier note) and this slot's outcome; it is not evidence.

**Pilots / compute:** 0 pilots, 0 s, no lease.

**Single next required certificate:** a successful compile of the after-state with its log
inspected (undefined references, the new double-superscript-free notation, overfull theorem
headings), followed by review of the Thm 6.2 closure statement's source (B17-01) — the one
mathematical dependency this repair downgraded rather than discharged.
