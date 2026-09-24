# B27-06 delivery

**HAND — current result:** outcome 2, a completed priced preregistration. No target measurement is authorized or claimed.

| File | Purpose |
|---|---|
| REPORT.md | Rung findings, certificate arguments, every method's pricing and limitations |
| PREREGISTRATION.md | Standalone proposal for a future user decision |
| SEARCH_AUDIT.md | Search scope, relevant records and archive exception |
| INPUT_BINDINGS.json | Full commits, paths, Git blob IDs, raw SHA-256 and byte lengths of mathematical inputs |
| PRICE_CALCULATIONS.json | Original exact pricing arithmetic, preserved |
| FINAL_PRICE_AUDIT.json | Verified corrections to hybrid memory and independent-rebuild time; these fields supersede the original prices |
| TIMING_DATA.json | Extracted historical per-cell timing rows and descriptive fits |
| RESOURCE_RECEIPT.json | All attempts, continuation history and final checks |
| MANIFEST.json | Raw payload hashes/bytes, excluding itself |
| interrupted_delivery/ | Unchanged snapshot of the first stopped delivery's report, receipt, stop notice and manifest |

**READ — historical files.** STOP_REPORT.md at the top level and b27_06_seal.py describe the earlier stopped segment. They are retained for provenance and are superseded by REPORT.md and the final manifest. The original unsuccessful parser script's raw hash survives, but that overwritten version was not recovered. It yielded no mathematical result.

**READ — successful arithmetic scripts.** b27_06_price_run02.py preserves the exact successful original script; b27_06_audit.py performs the final 32 formula checks and corrections. The latter uses only Python's standard library and a Windows Job Object; its actual interpreter and command are recorded in RUN_03_RECEIPT.json. A reviewer should replay in a separate copy of the delivery folder to preserve the sealed raw evidence; timestamps/resource receipts will naturally change. No target matrix or rank is computed by either script.

**READ — final sealing.** b27_06_finalize.py verifies input/receipt/archive hashes and current document links, then writes the final receipt and manifest. It does not run a mathematical experiment. A SHA-256 manifest establishes byte integrity, not the truth of a mathematical claim.

**HAND — achievement boundary.** READ record review, HAND certificate/pricing reasoning and COMPUTED arithmetic. No new source condition, coefficient equation, padding separation or positive multiplicity gap. **READ:** “No five-row determinant equation is known to be nonzero on padding.”
