# Integrator compile note — B25-02 (Paper 2)

**For intake by the B25-12 coordinator.** Integrator (Claude, Cowork), 2026-09-21. **Not a review;
accepts nothing.** B25-10 governs. The packet stays UNCOMMITTED. This closes the producer's named
next step — *"compile the after-state and inspect the log"* — and it found something.

Method: `paper/det4-onset.tex` staged from `B24-06`, hashed raw, CRLF-stripped on a scratch copy
only, three `pdflatex` passes. Nothing on the user's machine was touched.

## Bindings match

| | sha256 |
|---|---|
| `paper/det4-onset.tex` after-state, raw | `328b23350bf9dee438887403ed39d7fa8b51f52debb23304c9acae916285e6a3` (71,238 B) — **matches the producer's "TeX after"** |
| `results/b25_02/MANIFEST.json` | `71c008fe10ed3496f1c10192e4ecce4ba8a1a746b2462cb998e99d564760b036` — **matches** |

## The two old errors are gone; two new ones were introduced

**Baseline (B24-06 state, compiled by the integrator 2026-09-20):** aborted on `Double superscript`
at source lines 144 and 874. **After-state: both are gone** — zero occurrences of the `\Ddet^{\per`
pattern remain. That part of B25-02's work is confirmed from the build.

**After-state: 2 errors, both from one line, one fix.**

```
! Argument of \@citex@checkblank has an extra }.
! Paragraph ended before \@citex@checkblank was complete.
l.653 SECONDARY), Dimca \cite[Thm.~3.1]{Dimca13} (PRIMARY, statement level) and
```

Source, lines 652–654:

```latex
\begin{theorem}[The cap; proved modulo Kleiman \cite{Kleiman} (read-status
SECONDARY), Dimca \cite[Thm.~3.1]{Dimca13} (PRIMARY, statement level) and
Gulliksen--Neg\aa rd \cite{GN} (SECONDARY), all adopted]\label{thm:cap}
```

**Cause.** This is the B6 repair — the cap-theorem label that B24-10 §11.5.10 ruled must appear in
Thm 7.1 — placed in the theorem environment's optional argument. Inside `[...]`, the `]` of
`\cite[Thm.~3.1]` closes the theorem's own bracket early. LaTeX's optional arguments do not nest.

**Fix (one edit, for B25-02 or the delivery pass, not applied here):** brace the citation:
`{\cite[Thm.~3.1]{Dimca13}}` — or move the read-status text out of the theorem header into the
sentence after it, which is arguably where a provenance label belongs anyway.

**Why the static check missed it.** B25-02's mechanical check tests brace balance and reference
resolution. This is bracket *nesting* inside an optional argument, which is balanced and resolves,
and only a real build catches it. The same held for the two `Double superscript` errors last week:
**the readiness statement "source checked statically" is not a substitute for a compile, and both
producers said so themselves.**

## Everything else in the build

`pdflatex` in nonstopmode recovered past line 653 and produced a **15-page** PDF
(`189d5fef052386f84874c637fd14ff033222aecc47b5e3551ecf9707251ec968`), up from 12 pages at baseline.
**The PDF is not a clean build and should not be circulated or treated as the after-state's
rendering** — Theorem 7.1's header is mangled where the parser recovered. Zero undefined references,
zero undefined citations, 2 overfull boxes, and two hyperref warnings for math in a section title
at line 748 (cosmetic). After the one-brace fix the integrator expects a clean 15-page build, and
will re-run it on request.

## Not done here

No mathematical claim was checked. The B2 repair, the Prop. 6.1 inequality reversal, the Theorem
6.2 retitling, and the B17-01 dependency it introduces are all B25-10's. The integrator notes only
that B25-02's own report names two items the paper now *adopts* from unreviewed sources — B17-01's
non-containment and the `n = 4` analogue of `(★)` — and that both are correctly labelled as such.
