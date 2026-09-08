# Astra batch-12 theory deliverables, staged into the repository

The S1 and S2 sessions ran on a different host and wrote to an isolated
directory outside the repository.  **A worker cloning the repository therefore
had none of it** — and `docs/s78_prompt.md` tells its session to reproduce S2's
rank-3 arc and run S2's generated chart jobs, neither of which existed here.
Staged 2026-09-08 by the integrator, before the briefs went out.

Provenance: `C:\Users\swami\Projects\gct-gpt\Batch12_Results\{S1,S2}` on
`swamilaptop`, verbatim.  Multi-megabyte scratch (`S1/scratch/*`,
`S1/benchmark_design.json`, `S1/birth13_design.json`, `S1/control_design.json`,
`S2/tangent_calibration.json`, `S2/input_manifest.json`) was **not** copied — it
is regenerable from the scripts and would breach the 5 MB rule.  Ask if a session
needs one of those.

**These are session deliverables, not integrator-verified results.**  Treat every
number in them as MEASURED-by-that-session until this repository's own code has
re-derived it.  What the integrator has independently checked is recorded in
`docs/s1_batch12_review.md`, `docs/batch12_integrator_note2.md` and
`docs/batch12_s1_s2_consolidated.md`.

## S1 — the birth quotient

| file | what it is |
|---|---|
| `S1_report.md`, `run_results.md` | the session report and its timings |
| `partial_source_10.json` | ten evaluation-ready goal-cell vectors: eight replayed degree-13 birth classes plus the two seeds |
| `birth13_checks.json`, `n3_independent_minors.json` | the retained minors behind those |
| `control_matrices.json` | both control matrices |
| `relations.json` | the three complete fillings of the small Plücker example |
| `transported_det_lower_bound_2.json` | the transported seed determinant lower bound |
| `relay_to_integrator_s76.md` | S1's own relay (note: its numbering, not this batch's) |
| `s1_checks.py` | the session's checker |

## S2 — r = 5

| file | what it is |
|---|---|
| `S2_report.md`, `REPLAY.md` | the session report and its replay instructions |
| `HANDOFF_s77.md` | the finite completion specification. **This is s78's primary input** (its filename carries the other board's numbering) |
| `cas/chart_0_Q.sing`, `cas/chart_64_Q.sing` | the two generated elimination jobs, 149 variables each, never executed |
| `build_chart_jobs.py`, `chart_manifest.json` | the generator and the coefficient index |
| `intermediate_rank3_arc.json` | **the rank-3 counterexample and its arc — s78's mandatory first control** |
| `ker_coker_certificates.json` | the rational rank certificates behind the 0/9 theorem |
| `verify_s2.py`, `verification_summary.json` | the session's verifier and its summary |
| `chart_coefficient_checks.json`, `independent_jet_checks.json` | the fresh-point agreement checks |

Paths inside these files point at the original Windows directory.  Resolve them
against `results/astra/S1/` and `results/astra/S2/` instead.
