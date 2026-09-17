# ARCHIVE_NOTE — post-B19 packets, archived 2026-09-17

This directory holds byte-identical copies of the eleven post-Batch-19 packet
trees that were written under `C:\Users\swami\Projects\gct-gpt\work\` on
16–17 September 2026, outside version control. The originals are unchanged.
`RELOCATION_MAP.json` maps every original absolute path to its path here.

## What is here

| packet | governing document |
|---|---|
| `extension_descent_20260916` | `REPORT.md` |
| `fiber_compatibility_20260916` | `REPORT.md` |
| `descent_followup_claude_20260916` | `REPORT.md`, governed by `../descent_followup_claude_20260916_addendum/CORRIGENDUM.md` |
| `descent_followup_claude_20260916_addendum` | `CORRIGENDUM.md` |
| `claude_image_ceiling_20260916` | `REPORT.md` (proved range `d <= 6`; its section 0 item 4 predates its own check and still says `d <= 5`) |
| `claude_singular_locus_audit_20260916` | `REPORT.md` |
| `claude_transverse_structure_20260916` | `REPORT.md`, governed by the followup and its clarification |
| `claude_transverse_structure_20260916_followup` | `REPORT.md` + `CORRIGENDUM.md`, governed by `clarification_20260917/CORRIGENDUM.md` and `STABILIZER.md` |
| `claude_source_vectors_20260917` | `final_arc_diagnostic/CURRENT_DIAGNOSTIC_STATE.md` (consolidated handoff); `b_L = 74` is proved in `arc_target_dimension_followup` |
| `astra_gkz_degenerations_20260917` | `REPORT.md` |
| `claude_gkz_incidence_20260917` | `scope_corrigendum/REVISED_VERDICT.md` + `CORRIGENDUM.md` over the parent `REPORT.md` |

Later corrigenda govern. Original reports are preserved unedited and linked to
their corrections; nothing sealed was rewritten.

## What is not here

- Three Python bytecode caches: `extension_descent_20260916/__pycache__/{sixrow_witness,skew_witness}.cpython-312.pyc`
  and `descent_followup_claude_20260916/pilots/__pycache__/paired_runner.cpython-312.pyc`.
  The first two were dropped into the sealed `extension_descent_20260916` tree at
  2026-09-17T00:57:05Z by a later session's P9 run that imported its scripts; no source
  file changed and the packet's manifest still verifies, but the original tree is no
  longer byte-identical to its seal. Recorded here; not deleted from disk.
- Interpreter (`work/batch15_workers/B15-02/.venv/python.exe`) and the shared wrapper
  `analysis/b15_bound.py`, pinned by hash in the manifests, live on the worker branches
  or outside the repository.
- Literature (Eisenbud–Harris 1988 scan, Segal arXiv:2412.14748v1, Dimca arXiv:1210.1795v4),
  rendered page images, and chat attachments: pinned by hash only, never archived.

## Verification

Every `MANIFEST.json` in this archive verifies byte-exact against the files beside it
(pre-commit re-hash: 13 manifests, zero mismatches). A manifest does not hash itself.
Two nested packets (`scope_corrigendum`, `clarification_20260917`) postdate their parent
manifests and are covered by their own; a naive recursive hash of a parent will report
the child's files as extra. `routeA_signfilter_20260917/results/s1_screen_arc.json` pins a
`candidates_selected.json` that was extended after s1 ran; s1 is not replayable from this
archive (known defect D1).

Naming notes: `claude_image_ceiling_20260916` calls the batch-13 paper `det3-conductor.tex`
in its manifest and `det-conductor.tex` in section 3 (same file); its title's `delta_0` is
the det3 quinary-cubic onset, not a det4 quantity. The symbol `L` is overloaded across the
transverse chain (ambient jet line vs the grading-preserving Levi).
