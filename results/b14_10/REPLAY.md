# B14-10 replay and delivery

board_numbering: batch14. Actual model: gpt-6-astra. The delivery has one named
Git bundle (zero split bundle parts), and four numbered file-register parts.
The whole file-register digests and per-part digests are in
file_register.jsonl.parts.json. All new individual files are below 5 MB.

## Standalone exact witnesses (Python stdlib only)

Extract b14_10_evidence.zip and use its root as the current directory. The
archive contains four compact certificates and their verifier. For example:

```powershell
$py = 'C:/Users/swami/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe'
& $py analysis/b14_10/recover.py --verify results/b14_10/recovered/cubic8_7_5_5_2_2_1_1_1.json
```

Use any compatible Python 3.12+ on another host. Repeat `--verify` for each
of the four non-validation JSON files in results/b14_10/recovered. This checks
the integral polynomial, all raising derivatives, point reconstruction,
both determinant algorithms, and both prime residues. It needs no Git,
numpy, scipy or flint. The proof of ambient multiplicity one is the indexed
top-cell theorem, also supplied in the banked B13-05 report in the archive.
These are b14-10-catalecticant/1 certificates; the generic gct-cert/1 verifier
does not implement this compact format. Use the included independent checker.

## Import the branch into a separate receiver checkout

The bundle prerequisite is commit 9898e56941a7665f231873481dae956f08509995,
tree cb688cd3fe454d638f3202e759e2eaa0c629739f. It is intentionally incremental.
Do not use a moving main branch as the prerequisite or switch integration.

```powershell
git bundle verify C:/path/to/b14_10_astra.bundle
git bundle list-heads C:/path/to/b14_10_astra.bundle
git fetch C:/path/to/b14_10_astra.bundle b14-10-astra:review-b14-10-astra
```

Inspect the fetched branch in an isolated receiver checkout. The bundle
exports refs/heads/b14-10-astra explicitly. The delivery manifest gives the
actual head and tree. Its sidecars use bare filenames. The report, evidence
zip, bundle, manifest and verification logs are checksummed after copying.

## Full inventory and controls in the receiver checkout

The frozen base tree must be available, together with its binary certificates.
The evidence zip alone deliberately does not carry the full historical corpus.
The first input_manifest.json is immutable evidence of this run's input bytes;
Git blob IDs are the cross-platform contract. The inventory reads changed
baseline files from the frozen Git objects, so later index additions cannot
silently change the census. Session JSON artifacts are marked -text in
.gitattributes to preserve their byte checksums on Windows checkout.

```powershell
& $py analysis/b14_10/bounded.py --name b14_10_inventory_replay --seconds 120 --mib 1024 -- analysis/b14_10/inventory.py
& $py analysis/b14_10/bounded.py --name b14_10_replay_validation --seconds 120 --mib 1024 -- analysis/b14_10/validate.py
& $py analysis/b14_10/bounded.py --name b14_10_replay_reconciliation --seconds 120 --mib 1024 -- tools/integrate/reconcile_cells.py --json results/b14_10/reconciliation.json
& $py analysis/b14_10/bounded.py --name b14_10_replay_scan --seconds 120 --mib 1024 -- tools/integrate/scan_unstaged.py --json results/b14_10/unstaged_scan.json
& $py analysis/b14_10/finalize.py
```

Run inventory before validation: inventory restores the frozen availability
register; validation adds the eight links to new replacement witnesses.
To regenerate one exact certificate, use `recover.py --index 0` through
`--index 3`, each under bounded.py with --seconds 90 --mib 768, sequentially.
The wrapper is Windows-specific (Job Objects); on other hosts use an equivalent
wall/memory limiter and call the inner Python script. It does not require a
Linux shell on Windows. PID, peak process commit, elapsed seconds and exit code
are recorded under results/logs. No broad process-name termination is used.

The full validation checks nonempty coverage, exact path/digest accounting,
typed theorem contexts, all nine predicate boundaries, malformed inputs,
unsupported supersession and exact replacements. Its PASS refers only to
those checks. It does not replay the 1,313 historical present certificates.

## Query mathematical exclusions safely

```powershell
& $py tools/integrate/exclusion_predicates.py --context quartic_padded_gap --n 4 --delta 6 --lambda 14 2 2 2 2 2
```

This returns a typed D<=0 conclusion. For cubic per3 ideal questions use
`--context cubic_per3_ideal`; for the n=3 padded-per2 comparison use exactly
`padded_gap_at_l_per2`. An unknown predicate fails; an irrelevant context
returns no theorem. `stable_full_rank_closure` requires verified dimension
and witness flags and matching dimensions, and is not applied automatically.

## What remains

remaining_cell_keys.json lists 223 historical files needing schema/reference
review. certificate_register.jsonl retains all 1,005 missing original paths;
replacement_map.json links eight of those to four exact replacements.
digest_discrepancies.json lists 29 unresolved historical MD5 mismatches.
recovery_queue.json contains all missing paths, producer dimensions, measured
historical runtimes when available, and the recorded causes. Full legacy
regeneration needs scipy/python-flint and possibly the producer's platform
adaptation; that work was not silently replaced by a metadata PASS.
