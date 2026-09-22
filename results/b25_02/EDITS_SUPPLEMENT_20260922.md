# B25-02 edits supplement — Paper 2 bounded repair, 2026-09-22

Written by the housekeeping pass PART 17b (Claude Code, Claude Opus 5 (1M context)).

**Authority:**
- B25-10 §4 and its §10 row for Paper 2, "REPAIR (bounded)" (`docs/b25_10_review.md`, sha256
  `0488ce1e…`, delivered at `42e7f4ba45e8bd1fda529de9ce116f64e7ac6be1`);
- the author's decisions of 2026-09-22 (B14, B16, and citing the B23-03 report), as written in
  the PART 17 brief §0.

**No mathematics is added.** B25-02's sealed `results/b25_02/MANIFEST.json` (`71c008fe…`) is
**not edited**, and neither is the PART 16a `REPAIR_SUPPLEMENT_20260922.md`.

## The edits

| item | where | change |
|---|---|---|
| (i) B25-10 §4.3 | ¶ after Thm 6.2 | The closure statement `R_5 ⊄ D^det_5` is "carried in this paper as *adopted*: it is a separate, unpublished result of this programme, carried as ADOPTED on the programme's record, that exhibits … `s_5·C*` …", still cited to `Companion2`. The locator is the B14 `Companion2` bibitem, as the brief directs. |
| (ii) `n = 3` control | §9, "The method exhibited…" | "proved modulo one premise, (★) below" → "proved; its one premise beyond the measurements, (★) below, is itself proved". "…is proved modulo (★)" → "it is proved in this programme, so the conclusion … is proved". The symbol `(★)` is kept for the premise. |
| (ii)/(iii) `n = 4` | §9, "What the length-nine cell reduces to" | "and we do not separate the two here" → "the `n=3` case is proved; the `n=4` case is not yet checked, so this transfer is flagged, not established". **The transfer stays flagged**; B25-10 §2.4's check was not attempted. |
| B14 | bibliography | `Companion` → S. Sethuraman, *Conductors of orbit closures, and the fundamental invariant of the 3×3 determinant* (Paper 1's `\title` long form, `paper/det3-conductor.tex` L36–38 at `241da4db`), "arXiv preprint, 2026, arXiv:XXXX.XXXXX [identifier to be inserted at submission]". `Companion2` gains "2026; PDF at [repository URL to be inserted at submission]". |
| B16 | Acknowledgements | "…carried out jointly with Claude (Anthropic). … rests with the named author." → "…carried out using AI tools, including Claude (Anthropic). … rests with the author." The byline `\author` is unchanged. |
| Companion3 | bibliography + 3 cites | New `\bibitem{Companion3}`: S. Sethuraman, *`D_{45}∩P_5` classified up to its boundary, and the rank thresholds at `N=6,7,8`*, "technical report, this programme, 2026; PDF at [repository URL to be inserted at submission]". The title is the heading of `3bcad666:docs/b23_03_report.md` with the slot label "B23-03 — " removed. Its backticked math is set as TeX math; no word is changed. It is cited at: Rem. 6.3, the interior classification ("…cubics containing a plane (31)"); Rem. 6.3, the G-A1 boundary sentence ("…nothing here excludes one"); and the Σ_Π statement after Thm 7.1 ("…hence on all of it"). |

The TeX diff has 11 hunks, +22/−14 lines. `PAPER2_BLOCKERS.md` rows B14 and B16 are now REPAIRED,
with G-P2-SUB noted (+2/−2). `PAPER2_GAPS.md` gains Part IV, recording G-P2-SUB and the status of
G-P2-02/07/18/19 after this pass (+12/−0). No other file is edited. `PAPER2_CLAIMS.md` and
`PAPER2_READINESS.md` are not in this pass's authority, so their `(★)` wording for the `n = 3`
control is stale history (see the report).

## Hashes

`paper/det4-onset.tex` is `-text` (a5f16234), so its blob is the raw CRLF bytes. It stays uniformly
CRLF: 1,247 lines, 1,247 CRLF.

| file | before (at `a480a064`) | after |
|---|---|---|
| `paper/det4-onset.tex`, raw CRLF | `39d15aeaf2d5eaaf3696f3250c9a95441dd92c3cda38f3a87f9f24cb3e79ebc5` (71,240 B) | **`065f8799dbec4b24b0ddd93b2cd1fdf8528d435c4464bcc529700010f08f55d8`** (71,849 B; blob `60bc18a4…`) |
| `paper/det4-onset.tex`, LF-normalised | `ec5b1b4d0724761a5f2027b8711986489967e0e0b5e8c5997299c0d8112748ed` (the integrator's clean-build source) | `c265937d1494e50a6f1ca0f3b9c4a453c727791fc4ea2e10e2ca467cbaf39c3c` |
| `PAPER2_BLOCKERS.md` | `dfbcd16537325f107c5f830166596a3a3624e1077ac325c0288487de8ffdf050` | `ee34b3733c222a551adac985d1075b9bcbc7a7dfb7bfee964254f0fc0e72ea23` |
| `PAPER2_GAPS.md` | `4f86bcd45f2ca302243e28cd95d440516e3a5397b97290ab67f43bbf148dda55` | `9fa78279b900cdae0e85f5e3249ee4cbc117f10554a510e7b8e53770cce96acd` |

## Static checks (B25-02 §7), not a compile

`results/b25_02/texnum.py` was run on the before- and after-states:

- theorem numbering is **identical** for every numbered result (2.1 … 10.5); only line numbers
  shift;
- 33 labels, none duplicated; **0 undefined refs**;
- no cited key without a bibitem, and **every bibitem cited** (`Companion3` 3×, `Companion2` 2×,
  `Companion` 9×);
- brace balance 0; no bare-section locators.

A separate scan found:

- `$` parity even;
- **"B23-03" 0, "B17-01" 0, "B25-" 0**, and "Claude" 1, inside the acknowledgement sentence only;
- no slot label of the form `[AB]NN-NN`, no `[AUTHOR]`, no "jointly", no "named author".

**No compile was run: this machine has no TeX.** The integrator will compile the after-state
(`065f8799…`, LF `c265937d…`) and bind it. Until then the only build evidence is for the PART 16a
state `ec5b1b4d…`.

## What remains (Paper 2 is still not ready)

- **G-P2-SUB** (fill at submission): `Companion`'s arXiv identifier and the repository URL in
  `Companion2` and `Companion3`.
- The integrator compile of this after-state.
- The `n = 4` transfer (G-P2-19), flagged until B25-10 §2.4's check is made.
- The Paper 2 / Paper 3 overlap (BLOCKERS §2), out of scope here.
- Outcome-(2) mathematical readiness per B25-02.
