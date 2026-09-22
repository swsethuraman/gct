# B25-01 edits supplement — Paper 3 edits-only pass, 2026-09-22

Written by the housekeeping pass PART 17a (Claude Code, Claude Opus 5 (1M context)). **Authority:**
B25-10 §3, "Paper 3 verdict", and §2.4 (`docs/b25_10_review.md`, sha256 `0488ce1e…`, delivered at
`42e7f4ba45e8bd1fda529de9ce116f64e7ac6be1` on `b15-10-portable-witness`). B25-10 authorises exactly
one edits-only pass, bounded to four items, and this pass does only those. **B25-01's sealed record,
`results/b25_01/FILES.sha256` (`9bfa9d00…`), is not edited.** It binds the before-state below, and
this supplement binds the after-state.

## The edits (no mathematics added)

1. **C45 / Theorem 8.1:** "PROVED modulo `(★)`" becomes **PROVED**.
   - The provenance now names the length-restriction lemma: `isotypic_rank.md` Prop. 5 @ `82633a60`,
     with B25-05 Lemma R @ `2688efd1` and B25-10 §2 @ `42e7f4ba`.
   - LMR Thm. 2.3.1 + §3.1 stays the one PRIMARY external input.
   - The upgrade covers the base rung `δ = 12`. The rungs above keep the s73 lineage (Prop. S,
     Lemma L), as B25-10 §2.4 scopes it.
   - B25-10's lineage (READ + INDEPENDENT hand re-derivation of R1–R6) is added.
2. **Rename `(★)` to "the length-restriction lemma" at every point of use** in
   `det4-blindness.tex`:
   - the abstract (L128);
   - §1.3's closing (L215);
   - Thm 8.1's provenance (L1025);
   - §8's closing and scope paragraph (L1036, L1057, L1061–1063, and the L1066 provenance);
   - §9 item 4 (L1095–1099), reworded from "waits on" to "settled";
   - the LMR bibitem (L1197).

   After the pass, `\star` and "★" occur **0** times in the TeX.
3. **GAPS G-37 CLOSED**, with a dated prefix; the 2026-09-21 text is kept as history.
4. **BIB.md LMR entry (iii):** the `C⁹ → C⁷` sentence now reads "length-restriction lemma … PROVED
   … so C45 is PROVED". `CLAIMS.md` C45 is updated in label, sources, commits and lineage, along
   with its two self-check lines (the C45 line and the Batch-25 citation line).

Each of CLAIMS and GAPS gains a dated change note. `DIFF_NOTES.md` is not edited. Nothing else
changes. The five-row baseline sentence, the author line, scoping, `Σ_Π` and G-A1 are untouched.

## Hashes (all four files are LF-only, `-text`; raw bytes = committed blob content)

| file | before (at `ddc7649e`) | after |
|---|---|---|
| `papers/det4-blindness/det4-blindness.tex` | `19e616cfb445ec36d16b7526a0972b8f4be52c05a1cb10df8d33da653082ff49` (108,327 B) | **`d7d92249994e50cc33cf54b6de0f51365f951f33b45abe2037c5d31248ad7614`** (108,977 B; blob `8ff59649…`) |
| `papers/det4-blindness/CLAIMS.md` | `ac1736518ec3cfa47194ac04164b1277ecfac31a0f3a30f773b6a2425fda89a9` | `23744c6a3549fb283eb510641d3ba5186e120b9dd08d26865bdf4f9e7fef4c1f` |
| `papers/det4-blindness/GAPS.md` | `a85518f23c87df80240bca3703357b49eb697fc4699b6b3d079360a6652f9a27` | `23104bfd56c8c8a333128492be260effeb55233f362aaa397497b8cc40ff0364` |
| `papers/det4-blindness/BIB.md` | `55e3b24d10221957257fa68c451969b4a931cc64c5f5a970698c0d63b98f75ed` | `bd64b9f7ebd2d20abae744425bba7e466a2c8f395aafef0b166cdcfc6d4da417` |

The TeX diff has 9 hunks, +16/−15 lines (CLAIMS +10/−4, GAPS +6/−2, BIB +1/−1). The before-state is the source the integrator built clean
(`build_evidence_20260922/paper3_B25-01_source_LF.tex`, `19e616cf…`, 24 pages).

## Verification: a static check, not a compile

**This machine has no TeX, so no compile was run.** Verification follows B25-01: the same script,
`results/b25_01/static_check.py`, run on the after-state and on the before-state (the blob at
`ddc7649e`). **Its output is identical for both:**

- 51 claim IDs, C01–C51, with 50 on result headings and none duplicated;
- 59 labels, none duplicated; 43 distinct refs, none undefined;
- no cited key without a bibitem, and no bibitem left uncited (the `#1` is the `\lit` macro's own
  parameter);
- environments balanced, brace balance 0, `$` parity even, 61 `\prov` lines.

Every added `\cm{…}` uses the existing one-argument macro.

**The integrator will compile the after-state and bind it.** The build certification for these
bytes (`d7d92249…`) does not exist yet. Until it does, Paper 3's after-state is statically checked
only. B25-10 §3 orders the recompile before the author's circulation decision.
