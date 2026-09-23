
---

## B26-05 current-state amendment (2026-09-22, PROPOSED, UNCOMMITTED, producer-only)

Everything above is kept as written: B24-01's pre-signature text and B25-03's four-item update.
The subject is `paper/det3-conductor.tex` at `848e22b4d7bf73c392bd6bac3ac6591315190b0e`
(committed LF blob `7988a8a2…`, LF sha256 `4e1ccf70…`; CRLF working copy `fada5f7c…`).
**Paper 1 is still not ready for arXiv. No readiness is declared here.**

B25-03's four items (and B25-10 §5), as they stand now:

| # | item | state at `848e22b4` | evidence |
|---|---|---|---|
| 1 | Attribution signature | **APPLIED** on 2026-09-22 (PART 17c). `ATTRIBUTION_PATCH.md` §3 was applied with Cor. 4.2 in **Form A**, and the intro hunk takes the §6 wording that B25-10 §5 requires. The B16 acknowledgement is replaced. The byline `\author{Swami Sethuraman}` is unchanged. | commit `848e22b4`; `results/b25_03/SIGNATURE_SUPPLEMENT_20260922.md` @ `848e22b4`. Re-checked from the LF blob by B26-05: `Cor.~7.2]{BI}` ×3, "no family of" ×2, "no admissible family" ×0, "jointly" ×0 |
| 2 | Compile of the signed bytes | **DONE by the integrator.** `4e1ccf70…` (LF) / `fada5f7c…` (CRLF; the bytes compiled, with identical content): 0 errors, 0 undefined refs/cites, 27 pp; two cosmetic hyperref warnings. The PDF and log are uncommitted. | `build_evidence_20260922_close/BUILD_NOTE.md`; `SHA256SUMS.txt` `c4c56d0d…` (12/12 verified by B26-05) |
| 3 | G-P4 (the Kumar citation in Remark 4.14) | **OPEN.** Owner: B26-03 (Batch 26). Its result is not anticipated here. | `GAPS.md` G-P4; B26-03 brief |
| 4 | Read-status of IK Lem. 5.2, Kumar (Compositio 2015), and Hüttenhain thesis §8.1 / Cor. 8.3.2 | **OPEN.** These are B24-01 readings with no packet. Owner: B26-03. | `GAPS.md` header (iii); B25-10 §5 |

**Stale lines above, not edited:**
- "what stands between it and arXiv is now one signature" (withdrawn by B25-03; the signature is now applied);
- "The one thing that remains … deliberately not applied" (now applied);
- "A real `pdflatex` run is still owed before posting" and "it was not compiled" (the signed bytes are now built, item 2).

**Unchanged author decisions (not defects):** G-P5 (Marcus–Minc label), the G-P2 and G-P3 framing,
MSC and arXiv categories, and the LMR journal metadata. **Unchanged open mathematics:** G-A1 to
G-A6, including the primitivity caveat on the headline factorisation.

**Submission placeholders:** none in Paper 1's own source. Paper 1's arXiv identifier is the
placeholder `arXiv:XXXX.XXXXX` in Paper 2's `Companion` bibitem, which is filled at Paper 2's
submission (G-P2-SUB). Paper 3's `Paper1` bibitem carries no locator yet.
