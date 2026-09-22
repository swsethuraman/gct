# B25-01 bindings: before/after bytes of the five Paper 3 files

**Every "after" digest below names an UNCOMMITTED working-copy state** in worktree
`work/batch15_workers/B23-04` (branch `b23-04-paper3`), measured 2026-09-21T03:48:27Z (DIFF_NOTES.md re-measured at 2026-09-21T03:50:52Z after a one-line tool-memory note). None of it is
committed. A separately authorised delivery pass must commit the explicit paths and verify that the
committed blobs equal the "after blob (predicted)" column. **Every "before" digest names committed
content**: path at commit `f95742aed4dd22d3f04ac1313ce3d78e6e0bc87c`, with its blob id.

Line endings: all ten states (five before, five after) are **LF-only, 0 CR bytes**. So the raw
working-copy SHA-256 equals the SHA-256 of the blob content, and `git hash-object` with and without
filters gives the same id (`core.autocrlf=true` does not rewrite an LF-only file on add). No file
was normalised. `det4-blindness.tex` is pure ASCII before and after.

## Before (committed at `f95742ae`)

| path | blob | content sha256 (= raw working copy at start) | bytes |
|---|---|---|---|
| `papers/det4-blindness/det4-blindness.tex` | `50b1918cdf1d100c6a6c3423b45d6d6327cce894` | `ab69ccbe6cc79decccb3a2a3798e08e3d3a97412d79a6d095b12f3a68678455b` | 96,414 |
| `papers/det4-blindness/CLAIMS.md` | `def1b53fba09ea33df925d8389c4497b8c17c329` | `74c7536c621e2ac099d2011fbd4cfef63425186a03f92e6b4d60060619cfe5db` | 37,770 |
| `papers/det4-blindness/GAPS.md` | `32118ee8a6763eff75073934b71317d32efc92fb` | `fd1f523336119060e13cb5bda171c2eefe103b6cdcef55d6c241189b52837bc5` | 35,326 |
| `papers/det4-blindness/BIB.md` | `3b214bf8c671510c63978aea0c786320826ffc27` | `60c2a078cf6371cec2f484bec7ffcb04c84ee302c74eb5d2d48d851709b5a112` | 12,774 |
| `papers/det4-blindness/DIFF_NOTES.md` | `846f5b9bf3f42ea0aee9bda654b0907c556a933a` | `3d52d3ead5d88adfbb4754e62eac91fbe553eabca632c34f1e160a70d60d8d57` | 20,197 |

The tex before-state `ab69ccbe…` is the byte string the integrator compiled to 22 pages
(`docs/b24_12_ledger.md` @ `f55ed57f`, lines 652–664; PDF `1958bade…e521e1f5`, not committed).

## After (UNCOMMITTED)

| path | raw sha256 (UNCOMMITTED) | bytes | lines | after blob (predicted, `git hash-object`) |
|---|---|---|---|---|
| `papers/det4-blindness/det4-blindness.tex` | `19e616cfb445ec36d16b7526a0972b8f4be52c05a1cb10df8d33da653082ff49` | 108,327 | 1,209 | `33116c4ad15d4bc39a7000fb6b10d570437c9379` |
| `papers/det4-blindness/CLAIMS.md` | `ac1736518ec3cfa47194ac04164b1277ecfac31a0f3a30f773b6a2425fda89a9` | 46,003 | 213 | `ac5d551eba8701566fa73e61ef7309f6015b17c9` |
| `papers/det4-blindness/GAPS.md` | `a85518f23c87df80240bca3703357b49eb697fc4699b6b3d079360a6652f9a27` | 44,076 | 158 | `3bdc5e0d8d5a74b796c7b3019ee430dfe04a849a` |
| `papers/det4-blindness/BIB.md` | `55e3b24d10221957257fa68c451969b4a931cc64c5f5a970698c0d63b98f75ed` | 14,356 | 87 | `157ce244e1fbd87265c8b1d99b0678e4590b2ff9` |
| `papers/det4-blindness/DIFF_NOTES.md` | `a35b79c47ee4bd5909dabcc6fdeccbccd03bca589256580120527452387adc60` | 30,641 | 310 | `74554538b93834e74bcc6e8b4129a1fe65b0a331` |

The digests of this slot's own new files (`docs/b25_01_report.md`, `results/b25_01/*`) are in
`results/b25_01/FILES.sha256`, which does not hash itself.

## Committed inputs read (all through `git show <commit>:<path>` on the shared object database)

| input | commit | path(s) | what was used |
|---|---|---|---|
| B24-10 review | `ab2f8a407f5eac320c13d1eefca33c9b930ded86` | `docs/b24_10_review.md` | §§2, 3, 5.3, 6, 9.3; closing ledger §11.2, 11.3, 11.5, 11.6, 11.9 (governs) |
| B24-02 | `f8273c3b5542fe085c596e3814c45621d3608ca7` | `docs/b24_02_report.md` | §§0, 2.2–2.4, 3, 4, 5, 6 |
| B24-02b | `5a97317e7e28753261cf6e8dcece180a0e71b718` | `docs/b24_02b_report.md`; `results/b24_02b/lmr_quotes.md` | §§0–5; Q1–Q7 |
| B24-05 | `5c5ba86edd318d349b858c5c99df27b6be9355c2` | `docs/b24_05_report.md` | §§1.2, 4, 5 |
| archive | `82633a60893236fab4fbc317df416e1b8a349005` | `docs/onset_conjecture.md` §0; `docs/s73_report.md` §1 | cap statement wording; (★) wording and range |
| B24 ledger | `f55ed57f636e5ae6ea791f3238a66f9414008c90` | `docs/b24_12_ledger.md` lines 645–665 | the 22-page compile record |

The live B25-12 ledger (UNCOMMITTED, administrative) was read for the registered B25-01 outcome
space only.
