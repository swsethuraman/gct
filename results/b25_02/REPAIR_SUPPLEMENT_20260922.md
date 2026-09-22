# B25-02 repair supplement — Paper 2 line 653 (coordinator item D5), 2026-09-22

Written by the housekeeping pass PART 16a (Claude Code, Claude Opus 5 (1M context)), under the
user's authorization of 2026-09-22. This file is a **supplement**, not a re-seal:
`results/b25_02/MANIFEST.json` (raw sha256 `71c008fe10ed3496f1c10192e4ecce4ba8a1a746b2462cb998e99d564760b036`)
is B25-02's sealed record of the failed-build state and was **not edited**. Its binding of
`paper/det4-onset.tex` to `328b2335…` describes the bytes before this repair and does not bind the
repaired bytes. The bindings below do.

## What changed

One line of `paper/det4-onset.tex`. The citation in the optional argument of the theorem header is
braced, so the inner `[...]` no longer ends the outer optional argument. This fixes LaTeX syntax only;
no mathematical text, claim, qualifier or provenance label was changed.

```diff
653c653
< SECONDARY), Dimca \cite[Thm.~3.1]{Dimca13} (PRIMARY, statement level) and
---
> SECONDARY), Dimca {\cite[Thm.~3.1]{Dimca13}} (PRIMARY, statement level) and
```

That is the full content of
`Claude_Handover_B15_B18/post_b19_housekeeping_20260917/build_evidence_20260922/paper2_line653.diff`
(sha256 `2df284fe819b39a5f8c5e462c3e3f354f113cd2a8f7d9a4a03c7961ed11e7a33`), applied exactly. It was
applied as a byte edit of line 653 only: exactly 1 of 1239 lines differs, and the file's CRLF line
endings were kept (1239 CRLF, 0 bare LF, 0 bare CR, before and after).

## Hashes

| state | form | sha256 | bytes |
|---|---|---|---:|
| before (B25-02 "TeX after", as delivered) | raw CRLF on disk | `328b23350bf9dee438887403ed39d7fa8b51f52debb23304c9acae916285e6a3` | 71238 |
| before | LF-normalised | `7d3de2c4161c0a4fc098767b0fc91dc60afc24460237e5d019c9ee5f6017e991` | — |
| **after (repaired)** | **raw CRLF on disk** | **`39d15aeaf2d5eaaf3696f3250c9a95441dd92c3cda38f3a87f9f24cb3e79ebc5`** | **71240** |
| **after (repaired)** | **LF-normalised** (`sed 's/\r$//'`) | **`ec5b1b4d0724761a5f2027b8711986489967e0e0b5e8c5997299c0d8112748ed`** | **70001** |

## Verification: by hash against the integrator's build, not by a fresh compile

This machine has no TeX installation, so **no compile was run here.** The repair is verified by hash
against the integrator's clean build. The LF-normalised repaired file is byte-identical to the source
the integrator compiled:

| build-evidence file (in `build_evidence_20260922/`) | sha256 | what it shows |
|---|---|---|
| `paper2_B25-02_line653fixed_source_LF.tex` | `ec5b1b4d0724761a5f2027b8711986489967e0e0b5e8c5997299c0d8112748ed` | the compiled source; **equals the after LF hash above** |
| `paper2_B25-02_line653fixed.pdf` | `455c9ea87416aac511f1315662e2f5c899624707787e4dd81a07d3fddb5e7105` | the clean build, 15 pages |
| `paper2_B25-02_line653fixed_pass3.log` | `5b8bbcdb3c9896225934baa57c60241645a08fb6ddc2ee8906ab0369fb352fe3` | 0 `!` error lines; "Output written on det4-onset.pdf (15 pages, 386500 bytes)" |
| `paper2_B25-02_asdelivered_source_LF.tex` | `7d3de2c4161c0a4fc098767b0fc91dc60afc24460237e5d019c9ee5f6017e991` | the failed source; **equals the before LF hash above** |
| `paper2_B25-02_asdelivered_FAILED_pass3.log` | `dfb99eb9f2db5aeca6d20495a7684bd1198ef2bfd70a08dda757e04ad405169a` | the failed-state history: 2 `!` error lines at line 653 |
| `SHA256SUMS.txt` | `1c89f7ee9fae90036d88bd0f573996002e3ea16e4a82fad3f9997bbd85421ca5` | lists the hashes of every file in that folder; each listed hash was recomputed and matches |

The build certification is therefore the **integrator's** (a container build in three `pdflatex`
passes), tied to these repaired bytes by hash. There is no coordinator or local build
certification. The PDFs are not circulation builds, and Paper 2 remains unreviewed with its
outcome-(2) mathematical readiness blockers open.

## Delivery-list extension

This supplement did not exist when the coordinator's `DELIVERY_PROPOSAL_20260922.md` (sha256
`aa8b3c349169f0ebe4e209544bc5fa9080d658151c5d24b072a0f48e51d6925b`) was written. It is added to
B25-02's delivery list as a **list extension made under the user's 2026-09-22 authorization of this
pass**, following the proposal's D5 instruction to record the repair in "a separately identified
repair supplement" and to refresh the delivery list for newly created repair artifacts.
