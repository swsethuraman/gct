# B15-04 preregistration

Model for reasoning, implementation, and verification: gpt-6-astra (requested xhigh). Banked code retains its original attribution. This session uses the existing B15-04 worktree and b15-04-small-panel branch only.

## Readiness and fixed inputs

HEAD and batch15-base both resolve to commit f365568d80d5f66fea2dd9342ff1998e1d866915, tree aff6ca0921ec964cc8b7fcbd64bd5e5e9de9fbbd. The annotated tag object is 80209c13e9ae33bad8933cb47413bf7710c96cb1. These were freshly compared before edits. Native READINESS.md reports a passed Windows Job Object runtime control and local NumPy, SciPy, SymPy, flint, and Numba. Algorithm-specific controls remain to be run. Existing runtime logs are setup provenance and will not be staged.

SHA-256 below uses UTF-8 text with CRLF normalized to LF; the new receipt will also record exact-byte hashes of consumed inputs.

| Input | SHA-256 |
|---|---|
| docs/batch15/WORKER_PREAMBLE.md | b41ab684785ad4be1fa91ec491c25c10fa463c0bdf2d5bb69b3e59e2abf6797d |
| docs/batch15/ACCEPTED_STATE.md | 97b07d5f50c21fc6a3a6bba267339ba385dcda0b6bad7a067c5905b1351352df |
| docs/batch15/briefs/B15-04.md | bf21868685b84085b6ff5467c10752acd3afccde44053b5431edda733aff713c |
| results/b15_prep/small_panel_sizing.json | 372d54e76a6f45c84c0833955422e15cc4c8cfd7a877127e0df17e2e5cbe7e04 |
| analysis/b14_11_work.py | e450476147cb826ccbbfb6d3faff34deb4d8e6c6407dad33ab7bfe5ab37dcc43 |
| analysis/b14_12_cell.py | ce55b0e7c6233a2b27f53bee85c69f651e5725566376c354fefabc2d53854af4 |
| analysis/b14_12_families.py | 45b0f859aa5dc64f05dffdfc47eaff7e4e22a64bcdfd1a77b3dc3ac7f55c8298 |
| analysis/b14_11_sizes.py | adc9e3bc5a5fac3e618eaf7f9f50c5f142176b207307d8b068225bbbbf4ba887 |
| analysis/wk13_b10_lean.py | f612ead043c9b0f2db59345e1265d2eff4905a725e2e3c3e27ce456f2e179231 |
| results/integrate/inherited_exclusions.json | bfdf6bf971e192723bb48c9c9be4cf00f32ecb0f05647f4df790858145edb338 |
| results/b15_prep/transport_overlay.json | e8f2d129c60eaf36e0ec6644b5e9f706a6c540cc85a8329f17bcdc0c8ba6c007 |
| results/b15_prep/shortlist_overlay.json | 93f0bd43549038dfb29d1cad4fecbe9e97b2ff95365632bd2e455c1cf6dc00c4 |

## Mathematical question and conventions

Work with quartics (n=4), polynomial degree delta=8, ambient variable count 16, and highest-weight labels lambda=(11,11,5,2,1,1,1) then (12,11,4,2,1,1,1). Seven-variable restrictions evaluate HWVs of length seven in the 16-variable representation; they are not an assertion that the independently padded permanent has only seven or nine essential variables. The full padded form is z per_3 with ten independent essential variables, restricted using ten independent linear forms.

The supplied ambient multiplicities are a=4 and 3; both pullback bounds are h_pad=3. Apply the scoped exclusion ledger and accepted overlay before evaluation. With only the trivial padded ideal lower bound L_pad=0, U_pad=min(a,h_pad,a-L_pad)=3 for both cells. Define D=m_pad-m_det=i_det-i_pad. Determinant rank at least three suffices to exclude D>0. At the first cell, global i_det>=2 plus padded rank at least three proves D>=1; at the second, global i_det>=1 plus padded rank at least three suffices. A sampled kernel never supplies these global lower bounds.

Retain wk8_s30_core.exps letter order, integral factorial symbols alpha! c_alpha, degree-eight source orientation, stabilizer character, and modular primes 2147483647 and 2147483629. No u transport or change of basis is planned. Monomial evaluation includes the factorial normalization and signed orbit coefficients. Record exact points, source construction, and all source-to-polynomial conventions.

## Algorithm and gates

1. Recompute signed Burnside dimensions over Python integers, with explicit small orbit enumeration as an independent control. Recompute ambient multiplicities and Pieri/cubic pullback dimensions when affordable; otherwise label them inherited. Do not use N_S divided by stabilizer order as n_chi.
2. Use the banked lean monomial/orbit/raising-row construction in a per-slot driver, with construction, cover, reduction, and evaluation timed separately. Avoid importing drivers that create output folders outside the assigned worktree. Use compact CSR, chunked construction, and uniquely created scratch children. Retain compact source construction rather than oversized native arrays when needed.
3. Run small controls before any research carrier. Compare the lean integer raising matrix with the older constructor. A known nonzero HWV must evaluate nontrivially on a determinant pencil independently of either research rank. Compare coefficient evaluation with an independent exact contraction or direct determinant polynomial evaluation. Alter signs, normalization, source, and point data to demonstrate defect detection. A research rank of zero is permitted.
4. Measure each research carrier and its best triangular cover. Price dense Schur storage and transient copies before allocating. If a native compiled helper is unavailable, a checked Numba implementation or a bounded small exact reduction is allowed; no blanket dependency failure claim. Stop on a demonstrated memory/time limitation and export the smallest valid source/evaluation witness, with a costed alternative.
5. A modular HWV is eligible for a rational rank claim only with an integral construction or a proved lifting argument. For an integral raising matrix E of rational kernel dimension a, exhibit rank_p(E)=n_chi-a through a triangular cover plus projected residual rank, then verify the full kernel. A p-unit maximal minor makes the rational kernel commute with reduction over Z_(p), which justifies lifting the modular kernel and its nonzero evaluation minor. Checking only E K=0 is insufficient.
6. Stop accumulating determinant directions when rank three is reached. If rank remains below three, report only a rank floor and candidate status. A positive claim additionally needs exact global determinant membership and a padded rank witness; use full target completeness for any interpolation argument. Do not promote stable sample deficiency.

## Resources and delivery

Exact executable: C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-04/.venv/python.exe. Every shell command has the assigned worktree as its explicit working directory. Small controls use the existing analysis/b15_bound.py Windows Job Object wrapper, initially at most 60 seconds and 512 MiB (a justified change may be recorded before rerun). One process and one BLAS thread.

The initial LEASES.json names only slots 01 and 02. B15-04 has no heavy lease. Request one in this task after controls and sizing; read the record again before any heavy launch. A leased pilot is at most 900 seconds and 1536 MiB aggregate; a production attempt may extend to 5400 seconds only after measured evidence and integrator allocation. No unbounded dense build. Record available RAM, return code, wall time, aggregate peak memory, and resource decisions, including an ended attempt.

Only per-slot files are written. No shared theorem/exclusion records are edited. Proposed exclusions go to results/b15_04/proposed_exclusions.json. Required report and proof fragment distinguish EXACT, REPLAYED_RANK_FLOOR, RECORDED, CANDIDATE, and RESOURCE_STOP with inherited premises separately named. All new tracked files stay below 5,000,000 bytes. Commit this preregistration first with model attribution; preserve setup logs. Finish with the mandated delivery check and a fresh one-ref delta bundle in delivery/b15_04_final, without pushing or publishing.
