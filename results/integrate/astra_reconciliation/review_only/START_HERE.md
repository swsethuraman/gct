# Shared research entry point

This checkout integrates all twelve Batch 13 branches without rewriting their history. Read this file, `docs/batch13_integration_corrections.md`, and `docs/interoperability.md` before selecting work. Original reports and certificates remain preserved; their frozen queue counts are not current planning counts.

Current accepted conclusions: global cubic-permanent ideal vanishing and padded/reducible equality through degree 8 (B13-05 + B13-09 + inherited shorter-length results); 99 higher-length degree-9 cells remain; 58 six-row degree-10 cells remain. The LMR determinant rank is 273, padded rank is at least 269, D is in [-4,1]. Exact degree-13 identities, padded birth equality, and five-variable determinant containment remain open.

Run `python analysis/research_catalog.py build` to regenerate the current index. Run `python analysis/research_catalog.py find TEXT` to search cell identities, source paths, and archived reports. Generated files are under `results/integration/`. The index combines the frozen B13-11 ledger with explicit Batch 13 additions; it is NOT a proof that every historical file has been semantically ingested. `coverage.json` exposes that distinction. Stable and containment exclusions remain in B13-11's inherited-rule files.

Before a new task: search the index; inspect source evidence and applicable inherited exclusions; record the exact base commit and duplicate-check result. Do not infer an open problem merely from absence in the rank table. After a task: supply machine-readable observations, source and certificate paths, hashes, conventions, replay commands, and unresolved obligations; rebuild the index.

Integration status: branches coexist; this is not a claim that all numerical production paths interoperate. The combined lean-builder / wide-multiplication runtime acceptance test is pending. No new numerical production sweep should assume that test passed.
