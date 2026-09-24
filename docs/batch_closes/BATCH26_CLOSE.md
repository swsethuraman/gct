# Batch 26 — closed

**Written 2026-09-23 by the integrator from committed records.** The coordinator's seal goes in
`BATCH26_LIVE_LEDGER.md`. This file summarizes the batch; it does not replace the seal. The
integrator verified every hash below by staging the file and hashing it.

## Headline

Batch 26 settled all three research directions it opened. Every producer result is now
cross-lineage reviewed. It also closed C1 and C2 (the r=9 cell).

- **No construction was produced.** A25-10's programme decision stands: **no construction
  ready.**
- **Binding constraint, unchanged:** No five-row determinant equation is known to be nonzero on
  padding.

## What was established (all cross-lineage reviewed)

| # | result | producer | reviewer | level |
|---|---|---|---|---|
| 1 | **Symmetric padding is a determinant.** For linear forms `l,a,…,f`: `det diag(l, M_√2) = l·per[a d e; d b f; e f c]` over `Q(√2)`. Every determinant equation, in every degree and coordinate ring, vanishes on this family and on every shear of A25-04's old `T`. | A26-01 (Astra) `7464a2bd` | B26-10C (Claude) `a7b7c19f` | scoped containment / no-go |
| 2 | **Smooth-cubic exclusion.** `lC ∉ D₄,₅` for every smooth complex cubic threefold `C` and every `l ≠ 0`. Also: every component of a square-free `F ∈ D₄,₅` is ruled. | B17-01 (Claude) `01c49022` | B26-01 (Claude, same lineage) `901b0fe6`; A26-02R (Astra, cross-lineage, not blind, disclosed) `b0d2d2e8`, which **repaired** the rank-≤2 incidence step | geometric noncontainment |
| 3 | **The expander family is rejected member by member.** Each member survives actual padding. The height-two columns cannot see `Sym⁴(span(x₃,x₄,x₅))`. The pencil `D_n = z^{n−4}(A+B/2)²` differs from padding exactly by `B²/4` in that blind subspace. The witness cubic `wQ` is neither smooth nor a symmetric permanent. | notes (Astra) `0d6f5a8c` | B26-02 (Claude) `cdf6839c`; classification step 4 re-checked by B26-10A (Astra) | rejection of individual members |
| 4 | **Paired-column contractions cannot be determinant equations at n=4.** A26-03's one redesign sees `B²` but has `f(Q²) ≥ 3⁻⁵⁰·12⁻²⁵⁰`, where `Q² = det K_Q`. Corrected general statement: at n=4, every single fully paired tableau with no repeated label in a column is **nonzero** on `Q²`, and **strictly positive** when pairs are written in the same order. This independently covers the expander family. | A26-03 (Astra) `f7967d17` | B26-10C (Claude) | rejection plus structural obstruction |
| 5 | **Quartic 16→9 transfer, r=9 cell.** Paper 2's `D9` is the `det₄` pencil closure. Lemma R (R1–R6) holds at `(4,16,9)`, λ=(65,17,2⁷), δ=24. | B26-04 (Claude) `65736d9f` | B26-10A (Astra) `21816b3c`; LMR 1004.4802v1 read as primary source, bound by hash `cfc28275…`, PDF not committed | transfer lemma |

**Editorial (source/record findings; no review required):**
- **B26-03 (`af8468f3`), Paper 1 sources.** IK Lemma 5.2: narrow (`D ≥ 3`). Kumar Compositio and
  Hüttenhain: verified. G-P4: cite `KumarComp,KL`, not `KumarCMH`. Three patch proposals.
- **B26-05 (`96ea3293`, `721d54a2`), readiness and overlap.**
  - Stale metadata appends.
  - `(⋆)` rename at 3 sites; `thm:star` left alone.
  - Three submission placeholders.
  - A 14-row Paper 2/3 overlap map: no contradictions, 5 author points.
  - Most important: Paper 3's "PROVED at every rung" overstates the reviewed δ=12.

## Rulings on the record

- **C1 CLOSED; G-A1 CLOSED for smooth cubic factors only.** This was the user's ruling, given
  2026-09-23 to the coordinator. It is recorded as the user's, not the coordinator's, because the
  coordinator conversation also ran A26-02R. Singular and reducible cubic factors remain open.
  Paper 2 may cite the result; wording is set in the author's editorial pass.
- **Two-tier rule confirmed.** A same-lineage ACCEPT only releases gates. Record and paper changes
  need cross-lineage confirmation.

## Reopening condition for tableau-type separators (replaces earlier integrator wording)

A candidate must contain **a column with no identical partner, or a linear combination with
mixed-sign coefficients.** That is necessary, not sufficient. It must also see the
`x₃,x₄,x₅`-quartic directions and must not be positive on Pfaffian-square determinants. **Any
actual-padding witness `T′` must break symmetry** (result 1).

## What did not happen

- No separation.
- No coefficient equation nonzero on padding.
- No positive multiplicity gap.
- No asymptotic statement.
- No paper edited. All patches are proposals awaiting the author.

## Integrator errors this batch

The count now stands at 19.

- **17:** ill-typed checkpoint ("the projection keeps its kernel"); corrected by the coordinator.
- **18:** at A26-03 intake, did not check the manifest's own line endings; PART 23 stopped and
  PART 23B superseded it.
- **19:** overbroad general reading of A26-03 ("positive"); B26-10C repaired it.
- **Also noted:** a verification slip, where a stale directory listing led me to report the
  ledger missing.

Integrator research suggestions remain **0 for 3**. No mechanism was proposed this batch.

## Process record

- **Sessions:** 11 research/review (A26-01, A26-02R, A26-03, B26-01–05, B26-10A, B26-10C, plus the
  expander notes delivered as input) and 8 delivery passes (PARTs 18–24, including 23/23B).
- **Stops:**
  - two on CRLF bytes: 21c for an attribute edit blocked in auto mode, and 23 for the manifest;
  - one on permission mode (21c);
  - all were correct stops, and none changed Git.
- **Launch protocol simplified mid-batch** (`LAUNCH_PROTOCOL_B26.md`): a one-line launch, with
  checks moved to intake.
- **Timing:** every session finished at 4–13 minutes against ceilings of 30–90.
- **Sources:** third-party PDFs are bound by hash and never committed (B26-03 `literature/`,
  B26-10A LMR).

## Delivery receipts (integrator-verified)

| pass | receipts | commits |
|---|---|---|
| 18 | `d44784e8…` | `0d6f5a8c`, `61cf7ad3`, `7464a2bd` |
| 19 | `a66f8e45…` | `901b0fe6` |
| 20 | `20157c3d…` | `cdf6839c` |
| 21 | `ede53acc…` | `af8468f3`, `65736d9f`, `96ea3293`, `721d54a2` |
| 22 | `4700df34…` | `b0d2d2e8` |
| 23 (stopped) / 23B | `a0fc8fd3…` / `34bb5fca…` | — / `cef0459a`, `f7967d17` |
| 24 | `0d67ba22…` | `21816b3c`, `a7b7c19f` |

## Carried into Batch 27

| # | item | note |
|---|---|---|
| K1 | Where can a nonsymmetric `T′` live? | Map the actual padding family against the known determinant families: symmetric padding, Pfaffian-square pencils, smooth-cubic exclusion. |
| K2 | Unpaired or mixed-sign contractions | Only with an escape paragraph against result 4 and the reopening condition above. |
| K3 | A25-10 reopening condition at a nonsymmetric `T′` | Whole-ring `ker Q_D ⊆ ker Q_P`, or `h` with `h(P_T′) ≠ 0`. |
| K4 | B26-10A §2.3 general degree-4 extension | New Astra work, unreviewed. Needs a Claude check before Paper 2's other `eq:lengthred` uses (L105–122, §2, L888) lose their protection. |
| K5 | G-A1 for singular and reducible cubic factors | Open. |
| K6 | A26-01 literature priority | DEFER; no primary source read. |
| K7 | Editorial pass: Paper 1 | G-P4 required; `D ≥ 3` recommended; arXiv locator optional. |
| K8 | Editorial pass: Paper 2 | `(⋆)` rename; cite the closed C1 result; remove the r=9 flag at L1060–1063; metadata appends. |
| K9 | Editorial pass: Paper 3 | Narrow "every rung" to δ=12; the other four overlap points. |
| K10 | Compile after edits; readiness call | The author's decision. |
| K11 | Application 3's floor is CERTIFIED-modular (one prime) | Unchanged (C11). |
| K12 | Padding status of A26-03's redesign; n>4; signed combinations | Open; low priority. |

**Batch 27 operating changes, approved by the user 2026-09-23:**
- Producers commit to their own slot branches.
- A bounded exact/symbolic compute allowance: ≤10 runs, ≤60 s and 512 MB each; results labelled
  COMPUTED; reviewers re-run.
- One batch-start `.gitattributes` rule.
- Ladders of sub-questions per slot.
- Cross-lineage review folded into each wave.
