"""Assemble the report from the final exact artifacts; do not change evidence."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'results/b14_11'
def read(name):return json.loads((OUT/name).read_text(encoding='utf-8'))
sizes=read('shortlist.json')['candidates'];summary=read('inventory_summary.json');audit=read('prose_audit.json')
logs=[json.loads(p.read_text()) for p in (ROOT/'results/logs').glob('b14_11_*.run.json')]
table='\n'.join('| '+str(i+1)+' | `('+','.join(map(str,s['lam']))+')` | '+str(s['h_pad'])+' | '+f"{s['N_S']:,}"+' | '+f"{s['n_chi']:,}"+' | '+f"{s['costs']['dense_square_int64_bytes']/1024**2:.2f}"+' | '+f"{s['costs']['build_seconds_model']:.2f}"+' |' for i,s in enumerate(sizes))
report=f'''---
board_numbering: batch14
session_id: B14-11
actual_model: gpt-6-astra
reasoning: xhigh requested; not independently introspected
base_commit: 9898e56941a7665f231873481dae956f08509995
base_tree: cb688cd3fe454d638f3202e759e2eaa0c629739f
branch: b14-11-astra
---

# B14-11 — exclusion audit and quartic shortlist

**Core completed. Delivery has one bundle part, `part00`, plus the whole named-branch
bundle.** The exact census preserves A1 labels and supplies ten distinct-tail
quartic candidates with exact reduced-space costs. The audit corrects 37 prose
passages across 15 existing documents, proves the quartic length bound directly,
and certifies 153 pullback-zero exclusions. The protected papers have explicit
integrator errata; they were not edited. No positive gap or new evaluation rank
is claimed. Focus next on the protected all-degree length-four statement and
on determinant evaluation of shortlist entries 1 and 3.

## Outcome and evidence

**CERTIFIED, exact finite combinatorics.** Exhaustively enumerated all **4,198**
partitions in `n=4`, `delta<=8`, `5<=length(lambda)<=delta`, `lambda_1>=delta`.
Exactly **2,734** have `a>0`; **667** have `a=1`. Degrees below five are empty
by the directly proved length bound. Every zero coefficient is also retained,
so coverage does not rely on an externally supplied positive-only census.

| Degree | Positive labels | A1 labels | Exact h_pad=0 | Recorded full det deferred | Additional recorded tail deferred | Candidate queue |
|---|---:|---:|---:|---:|---:|---:|
| 5 | 22 | 22 | 0 | 22 | 0 | 0 |
| 6 | 163 | 92 | 2 | 161 | 0 | 0 |
| 7 | 636 | 203 | 26 | 251 | 64 | 295 |
| 8 | 1,913 | 350 | 125 | 267 | 101 | 1,420 |
| Total | 2,734 | 667 | 153 | 701 | 165 | 1,715 |

**PROVED / CERTIFIED.** The 153 zero pullback bounds imply `mult_pad=0`,
hence `D<=0`, by the injection into `Sym^delta V tensor Sym^delta(Sym^3 V)`.
All channels and cubic multiplicities are saved, and a replay rechecks them.
These are the only new cell closures. No zero sampled evaluation, lack of a
known equation, positive pullback upper bound or A1 flag is treated as an exclusion.

**RECORDED.** The other 866 deferred labels have frozen full-rank or stable-tail
records. They remain `OPEN_IN_THIS_AUDIT` mathematically because this session did
not replay their geometric certificates. Their recorded provenance is sufficient
to avoid assigning the same measurement again. The full inventory retains every
label and all sources; missing certificates are not called PASS. No recorded
rank exceeds the independently counted ambient dimension, and recorded `N_S`
values have no conflicts in this join. The named s42/s54 census comparisons
agree on 1,877 and 777 overlapping coefficients, respectively.

**PROVED.** The length proof embeds the quartic symmetric power into
`(Sym^4 V)^tensor delta` and applies Pieri one horizontal four-strip at a time.
A strip adds at most one row. The first-row bound follows from a horizontal
`delta`-strip in the reducible pullback. Full proofs and arithmetic conventions:
`docs/b14_11_proofs.md`; indexed as `quartic_length_and_eligibility`,
`quartic_pullback_zero` and `quartic_signed_burnside_size` in `docs/PROVED.md`.

## Ten candidates and costs

**CERTIFIED sizes; OPEN gaps.** All ten selected labels have `delta=7`,
`length=7`, `a=1`; this is the result of the cost order, not a restriction of
the degree-eight census. Selection takes the first ten distinct tails in the
recorded `N_S` order after the filters above. Skipped rungs and the other 1,705
candidate labels remain in the inventory. Taking one representative per tail
is a funding choice; no equality of unmeasured rungs is inferred.

| # | lambda | h_pad | N_S | n_chi | One dense int64 square, MiB | Builder model, seconds |
|---|---|---:|---:|---:|---:|---:|
{table}

**MEASURED, exact calculation.** Sizing all ten took
{sum(s['wall_seconds'] for s in sizes):.3f} seconds of worker calculation,
excluding process startup, and less than 35 MiB peak working set per worker.
`n_chi` is a signed Burnside count, with every class trace saved; it is never
approximated by `N_S/|Stab|`. The first candidate has stabiliser order 720,
so its builder estimate extrapolates beyond the published model's well-tested
`|Stab|<=120` range. All builder seconds are estimates for that stage only;
kernel and evaluation runtimes are unmeasured. A square's byte count is storage,
not a process-peak prediction. Most larger entries need a sparse or hybrid
kernel route under this session's memory cap; no dense build was attempted.

**Next experiment, not a result.** Entries 1 and 3 have the smallest reduced
carriers (550 and 1,576). Start with a bounded determinant-side HWV evaluation
and the required forced-zero control. Each A1 nonzero determinant evaluation
would close its label. Vanishing on samples would leave it open. Suggested
launch envelope: one 300-second, 1.5-GiB process per label, with a checkpoint;
this is an allocation, not a runtime guarantee. The unresolved mathematical
bottleneck is the determinant/padded restriction rank or a genuine equation.

## Prose audit and assignment defects

**AUDITED.** Lexical scan covers {audit['scanned_files']} frozen tracked Markdown,
TeX and HTML files, with {audit['hits']} matching lines in {audit['matching_files']}
files. Every matched context is saved in `prose_audit.json`. The relabelling
had not reached all prose: `n4_gate`, `easy_counts`, `screen_results`,
`batch11_plan`, `s25_race` and other summaries still overstated BIP.
The 37 explicit corrections, with before/after text, are in `prose_changes.json`.
Historical numerical tables and preregistrations were preserved.

**PROVED corrections / ADOPTED source conventions.** The old BIP span lemma
was false for arbitrary torus weight vectors; its valid isotypic/HWV statement
is now supplied with a proof and a counterexample to the former wording.
The BIP rectangle `sharp` notation extends the first row; the former extra-row
reading even proposed `(2,2)` in degree-one quartics, where it cannot occur.
The independent padding variable here also prevents importing the cited
nine-variable support bound. The historical `chow6` point has essential span
at most four, so its zero is not an independent full-span-six argument.
The BIP v3 paper was checked at
[arXiv:1604.06431](https://arxiv.org/pdf/1604.06431), pages 2–5.

**RECORDED, integrator action.** Protected `paper/det4-onset.tex` still has an
all-degree ambient-fullness assertion for length at most four. Its own proof
acknowledges a hypersurface and only discusses measured degrees. The valid
all-degree conclusion is containment and `mult_pad<=mult_det`.
`docs/b14_11_protected_errata.md` gives precise frozen locations and replacement
wording, including the remaining unqualified BIP statements. No protected file
changed. This is a completed audit with pending owner edits, not a claim that
all historical prose is now correct.

**Implementation boundary.** The original seven inherited predicates are
unchanged. Two new exclusions are appended to `inherited_exclusions.json`:
relational partition bounds and the 153 explicit keys. The old range-only
`reconcile_cells.py` deliberately skips these unfamiliar predicate shapes.
`b14_11_finish.session_exclusions` enforces and tests them; integration must
explicitly support these types before the generic join applies them. It must
never treat an unrecognised predicate as “all n=4”.

## Validation and resource record

**PASS, exact arithmetic.** Controls compare five small plethysm coefficients,
including zero, against independent monomial-DP/Weyl counts. Four direct
monomial-orbit controls test signed Burnside, including odd repeated parts;
the wrong trivial character gives 4 instead of 2 and is rejected. The known
`(14,2,2,2,2,2)_6` size reproduces 7,508/171. The final checker replays the ten
sizes and coefficients, all **2,734** horizontal-strip lists, **1,348** distinct
cubic coefficients and all 153 exclusion keys. It tests corrupted coefficients,
signs and counts, empty and missing inputs, duplicates, bad partitions,
wrong length/first-row filters and an injected A1 exclusion. No required input
is missing. `controls.json`, `size_controls.json` and `validation.json` retain
the outcomes; not merely a prose PASS.

**Conventions.** Exact Z coefficient monomials and Q power-sum arithmetic,
descending partitions, no tensor coefficient normalisation changes.
All power-sum denominators are units at 2147483647 and 2147483629.
There are no stored value matrices: rows-as-vectors, columns-as-points,
`A^T K=0` and adjacent `values_are` apply to future evaluations. This session
does not use interpolation, modular kernels, CRT reconstruction or transported
point values to infer an equation.

**MEASURED resources.** Windows AMD64, Python 3.12.14, numpy 2.3.5; no flint
or psutil, no installations. Twenty logical CPUs and 33,752,997,888 bytes
physical RAM were reported; only 12,729,540,608 bytes were available at
preflight, on the shared host. One calculation at a time; numerical threads
one. Windows Job Objects impose a 1.5-GiB process-commit limit and the parent
imposes 60/120/300-second timeouts, recording the actual PID before waiting.
The {len(logs)} supervised attempts sum to **{sum(x['wall_seconds'] for x in logs):.2f}
seconds** of worker wall time, with longest {max(x['wall_seconds'] for x in logs):.3f}
seconds. This is not total session elapsed time or exclusive CPU accounting.
The census peak was 124,542,976 bytes of working set. No calculation hit its
resource limit. Initial assembly syntax and terminal-encoding issues were
corrected before final validation; no numerical result was promoted from a
failed run. The first narrow ledger join was expanded after it missed older
Markdown records; only the final joined inventory drives the shortlist.

## Evidence limits and handoff

**UNCHANGED / OPEN.** LMR remains `a24=274`, `mult_det=273`,
`mult_pad>=269`, `D in [-4,+1]`. Five sampled padded kernel vectors are not
five certified equations. No result from another concurrent session was used.
The degree-eight cubic equality may remove permanent-specific differences;
it does not imply a nonpositive determinant gap. No larger degree, rank or
absence-of-equation assertion is made.

**RECORDED provenance.** Preregistration commits precede the census and
the reduced-space measurements. Actual model was gpt-6-astra throughout,
without subagents; xhigh was requested and not independently introspected.
The peeled annotated tag, initial HEAD, base commit and base tree all matched
the dispatch. `input_manifest.json` records 88 frozen input blobs plus SHA256
and the external source version. `results/b14_11/REPLAY.md` gives exact commands.
The external delivery manifest records final head/tree, bundle prerequisites,
whole/part checksums and delivery-check outcomes. No push, merge, publication,
other worktree change or recurring work was performed.
'''
(ROOT/'docs/b14_11_report.md').write_text(report,encoding='utf-8')
print('report assembled from final evidence')
