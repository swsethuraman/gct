# B25-03 signature supplement — Paper 1 attribution patch applied, 2026-09-22

Written by the housekeeping pass PART 17c (Claude Code, Claude Opus 5 (1M context)).

**Authority:**
- **Author decisions** (PART 17 brief §0, given 2026-09-22):
  - the author signs `ATTRIBUTION_PATCH.md` with **Form A** at Cor. 4.2 (§2.2's first form,
    keeping "with no computation");
  - the §4 optional addendum is **not** added;
  - the B16 acknowledgement sentence is replaced.
- **B25-10 ruling** (§5 and the §10 Paper 1 row, `docs/b25_10_review.md` at
  `42e7f4ba45e8bd1fda529de9ce116f64e7ac6be1`): the patch's §6 wording is **required** at the intro
  hunk.

B25-03's sealed `results/b25_03/MANIFEST.json` (`e476683e…`) is **not edited**. The byline
`\author{Swami Sethuraman}` is unchanged, and no AI system is named as an author.

## What was applied, in order (each stage hashed; LF = blob content)

| stage | change | LF sha256 |
|---|---|---|
| 0 | target: `paper/det3-conductor.tex` at `241da4db`, blob **`975b59e931ff5ac4a1a1b49d08dbe0ce246c5c6e`** (unchanged since `bc7e62b7`) | `f52f8d16a8d11d23a9f7ccd7ebc99dfb6d6fcf00b10ee3b128bb871034b4f866` (114,279 B, 2,127 lines) |
| 1 | `ATTRIBUTION_PATCH.md` §3, as `results/b25_03/attribution_patch_extracted.diff` (`ea80adeb…`), via `git apply`: 3 hunks, clean; Cor. 4.2 in **Form A** | **`a289c9de57455dcf4e3666801f7f1af12f5306e5212b8eeb3b48806ff85a598c` = the expected post-patch hash** (B25-03 §6) |
| 2 | intro hunk, §6 wording: "…\cite[Cor.~7.2]{BI} in which no **admissible family** exists at all…" → "…in which **no family of $\delta$ distinct $D$-subsets** exists at all…" | `9066ea5a4460c0c800dd1e57eed9fcd79be583022dcaf773f7f57bb553413acf` |
| 3 | B16: the acknowledgements carry the "carried out jointly with Claude" sentence, so it is replaced by "The work reported here was carried out using AI tools, including Claude (Anthropic). Responsibility for the correctness of every statement in this paper rests with the author." Nothing else changes. | **`4e1ccf7006879c748beeb57676567ae2443a3a587df7251efc0523fec4686338`** (114,836 B, 2,136 lines; blob **`7988a8a2d3f7a14c03a3ca5fe0eab793b10e07f3`**) |

**Working copy (CRLF, as checked out under `core.autocrlf`):** before
`b911a15184ebf819301deddfc178d76a5d9a6d01b881d5fc64b32a8982457445` (116,406 B); after
**`fada5f7c9663f4a207252af574c49c2c84f2291cb27fa6115bce06ed82317086`** (116,972 B, CRLF on all
2,136 lines). The committed blob is the LF form. The file has no `-text` attribute, which is
unchanged, as B25-03 and PART 16 direct.

A procedural note on stage 1: the patch was applied to a disposable LF copy with
`core.autocrlf=false`. A first attempt under the global `autocrlf=true` wrote CRLF and hashed
differently (`917e3c4f…`). It was discarded before anything touched the paper.

## Static checks (as B25-03 §6), before (stage 0) vs after (stage 3); not a compile

- **Theorem counter unchanged:** 52 environments with identical numbering; `prop:census` = 4.1,
  `cor:lower` = 4.2.
- 64 labels, none duplicated; **0 undefined refs**.
- **0 cited keys without a bibitem, and 0 uncited bibitems.**
- Braces balanced (1,393 / 1,393 by this pass's counter, which ignores `\{` and `\}`), and the `$`
  count is even.
- `\cite[Cor.~7.2]{BI}` occurs 3 times and `Prop.~7.3` 0 times. "no admissible family" occurs 0
  times, and "jointly" 0 times.

Scripts: B25-02's administrative `texnum.py` for numbering, labels and cites, plus an inline scan.
**No compile was run: this machine has no TeX.** The integrator's clean 27-page build covers the
unsigned bytes only (`f52f8d16…`). The signed bytes (`4e1ccf70…`) still need a compile.

## Left for Batch 26 (not done here, as the brief directs)

- **G-P4** (Kumar).
- The read-statuses for **IK, Kumar and Hüttenhain**.

Both stay in `GAPS.md` as they stand. Paper 1's readiness, per B25-10 §5, is four items. This pass
completes the signature. The compile of the signed bytes, G-P4 and the three read-statuses remain.
