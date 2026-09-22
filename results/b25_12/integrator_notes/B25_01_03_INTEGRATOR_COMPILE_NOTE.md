# Integrator compile note — B25-01 (Paper 3) and B25-03 (Paper 1)

**For intake by the B25-12 coordinator.** Integrator (Claude, Cowork), 2026-09-21. **Not a review;
accepts nothing.** B25-10 governs. Both packets stay UNCOMMITTED. This note closes one readiness
blocker each producer named and could not close itself — *"a compile on a machine with TeX"* —
and resolves one open item from B24-10.

Method: each `.tex` staged from the producer's worktree, hashed raw, CRLF-stripped **on a scratch
copy only**, three `pdflatex` passes. No file on the user's machine was touched.

## Paper 3 after B25-01 — compiles clean

| | value |
|---|---|
| source | `papers/det4-blindness/det4-blindness.tex`, working copy at `B23-04` (HEAD `f95742ae`, uncommitted after-state) |
| raw sha256 | `19e616cfb445ec36d16b7526a0972b8f4be52c05a1cb10df8d33da653082ff49` (108,327 B) |
| errors | **0** |
| undefined references / citations | **0** |
| LaTeX warnings | 0 (one cosmetic font-shape substitution only) |
| pages | **24** — was 22 at baseline `ab69ccbe…`; the growth is C51 (Corollary 4.5) and the sixteen renumbered results |
| overfull boxes | 3, same count as baseline |
| PDF sha256 | `9c39acbb0a30b6e7c776636df8cc7b12d3ea048f7455de8f7f2bb00891f88950` |

Also confirmed: `docs/b25_01_report.md` on disk hashes to `b791ceb3…`, matching the producer's own
`FILES.sha256`. The renumbering of sixteen results did not break a single `\ref`. **B25-01 readiness
blocker #2 closes.**

## Paper 1 after B25-03 — compiles clean, unsigned

| | value |
|---|---|
| source | `paper/det3-conductor.tex`, working copy at `B23-05` (HEAD `bc7e62b7`); **byte-unchanged by B25-03**, as its report states |
| raw (CRLF) sha256 | `b911a15184ebf819301deddfc178d76a5d9a6d01b881d5fc64b32a8982457445` (116,406 B) |
| LF-normalised sha256 | `f52f8d16a8d11d23a9f7ccd7ebc99dfb6d6fcf00b10ee3b128bb871034b4f866` — **equals the committed blob content at `bc7e62b7`** |
| errors | **0** |
| undefined references / citations | **0** |
| pages | **27** |
| overfull boxes | 8 |
| PDF sha256 | `9f8bab942ecd0c5290f5dcb06a70b60c81776aef9d932a723a3603e170ec39fe` |

`results/b25_03/MANIFEST.json` on disk hashes to `e476683e…`, matching the producer's report.
**B25-03's "compile" item closes** — for the *unsigned* paper. The attribution patch is not
applied, so this is not the circulation build; it is proof that the source the patch targets
builds.

## The `b911a151…` item resolves — and B24-10 §11.4.7 was right but incomplete

B24-10 hashed every committed version of the paper and found no match for `b911a151…`, and
labelled the patch UNBOUND. B25-03 found why, and the integrator has confirmed it from the bytes
above: **`b911a151…` is the sha256 of the CRLF working copy; `f52f8d16…` is the LF content git
stores.** Same file, two line-ending conventions. B24-10 compared only committed (LF) content, so
the digest could never match. The patch was bound to a real, current file all along — to its
on-disk bytes rather than its blob.

So the label moves from **UNBOUND** to **BOUND to working-copy bytes, now dual-bound by B25-03**.
Carry-forward item 18 in the B24 ledger and G29(b)'s wording both benefit from one added clause:
*a printed sha256 must say which bytes it names — committed content or on-disk file — because on
this repository they differ.* This is the third time line endings have produced a spurious
finding (PART 14's `b23-05` and `b23-04` exceptions were the first two).

## Not done here

No claim in either paper was checked for mathematical content. Neither PDF is the circulation
build: Paper 3 awaits delivery and review; Paper 1 awaits the author's signature on the patch, the
Kumar citation (G-P4), and the three unread sources B24-01 cited without a packet. The producer's
wording flag on the patch's *"no admissible family exists at all"* — which B23-10 §4.3 / K9 rejected
— is the author's to rule on when signing, and this note takes no position on it.
