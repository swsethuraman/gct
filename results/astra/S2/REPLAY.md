# S2 replay and artifact guide

All paths below are inside the permitted isolated output directory. The original shared checkout and canonical files are inputs only.

## Completed verification

Use the bundled Python, or a normal Python 3 installation. No third-party package is required for these commands.

```powershell
Set-Location -LiteralPath 'C:\Users\swami\Projects\gct-gpt\Batch12_Results\S2'
& 'C:\Users\swami\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'verify_s2.py'
& 'C:\Users\swami\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'build_chart_jobs.py'
```

These commands regenerate the finite verification records and the two CAS input files. Copy the frozen directory before replay if its delivered hashes must remain unchanged. The scripts write only under their own directory.

Expected verification: rank cases 9,0,3,9 over Q and both primes; tangent control dPhi=16, kernel=64, tangent ranks 57/57, intersection=50, sum=64, transverse quotient=0; eight independent block-jet interpolation cases; a rank-three actual arc with leading form v*w*(y+v)*(z+v), coefficient-span five, and 24 numerical determinant checks. The chart generator checks 12 exact determinant evaluations and emits 15,000 signed determinant terms per chart.

Matrices use zero-based indices. Sparse polynomials are lists of [exponent-array, coefficient] pairs. Nonintegral rationals use the exact string p/q. Pivot rows and columns refer to the stored matrix, not a hidden reordered matrix. Every finite rational rank has a nonzero minor and an exact full kernel. The modular checks use primes 2147483647 and 2147483629. The scripts use no floating-point rank calculation.

## Generated but unrun CAS work

The [s77 handoff](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/HANDOFF_s77.md) is authoritative. The generated Singular recipes are mathematical inputs, not claimed certificates or tested Singular runs. Singular and msolve were unavailable here.

On a host with Singular, in a separate working copy, run a resource-bounded pilot of one recipe, retaining logs and the process identifier. Stop at the stated time/memory budget and preserve the residual ideal if it does not finish. For example, a Unix host could use `timeout 600s Singular -q cas/chart_0_Q.sing`; choose an explicit memory limit appropriate to that host. The process may need substantial resources; no runtime estimate has been established.

A completed Gröbner calculation needs independent rational certificate checking. The jobs intentionally saturate the **full graph before** imposing the W coordinates. Swapping these steps changes the problem and can lose exactly the boundary directions under study.

## Input snapshots and limitations

The [input manifest](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/input_manifest.json) freezes the relevant tracked files at b8d82416735f75b4c91f359b7e7708ce6a2a5455, together with all four canonical documents and both controlling briefs. Do not rerun the input-freezing script when reproducing this particular frozen report: a later HEAD may differ. The current snapshot, not an assumed branch tip, is the input to audit.

The repository self-test was attempted from the isolated snapshot using its original command:

```powershell
& 'C:\Users\swami\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'tools\verify\selftest.py'
```

It failed importing `flint` through layer1, before any test case ran. This does not affect the independent standard-library S2 verification; it does prevent claiming a full repository calibration PASS. No original msolve, Singular, s72 top-component, generic arc sweep or LMR target computation was run.

## Main deliverables

* [Research report](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/S2_report.md)
* [Finite implementation handoff](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/HANDOFF_s77.md)
* [Verification summary](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/verification_summary.json)
* [Exact ker/coker matrices](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/ker_coker_certificates.json)
* [Intermediate-rank actual arc](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/intermediate_rank3_arc.json)
* [Tangent calibration](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/tangent_calibration.json)
* [Independent jet evaluation path](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/independent_jet_checks.json)
* [Chart equations and coordinates](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/chart_manifest.json)
* [Final SHA256 manifest](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/artifact_manifest.json)

The S2 report is a partial theorem plus verified obstruction and bounded fallback. It is not a completed global r=5 noncontainment theorem. Outputs are frozen for independent review before promotion; this run schedules no further work.
