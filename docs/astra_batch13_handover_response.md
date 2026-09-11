# Delivery update — 2026-09-11

This update supersedes the earlier handover state below. Delivery branch astra-b13-delivery is based on e7769374c1eb6a41f7f8570513856e2b2f22085c, advanced using the two supplied rewritten-history bundles. No pre-rewrite history was merged.

The 17 Astra-only files are retained under results/integrate/astra_reconciliation/review_only/ for review, not installed as controlling tools. Historical status statements and old hashes in those copies are archival.

All newly requested S2/S3 files were recovered. S2 input_manifest.json and tangent_calibration.json are also restored; both are below 5 MB, and the stale README is corrected. The Gram gzip has an adjacent README with original and compressed hashes and decompression instructions. Original replay manifests remain historical snapshots; recovery hashes are separate.

The staged-tree scanner reports zero missing references; the s76 DAG files remain explicitly absent. A Windows SIGPIPE guard was added to make the scanner executable on this host. No mathematical calculation was rerun. The shared numerical-tool acceptance test remains separate.

## Earlier comparison record (historical)

# Astra reconciliation against the rewritten Batch 13 baseline

Astra ea3c6b0 tree: 90f7808727f592c6664b2cd58eb448044a7bc355.
Claude b31a0de tree: 7b0ba07c81d1063e4b363c825b0f01c61a09f35b.
They differ because they include different integration housekeeping, not just the twelve worker merges.

The complete file comparison is results/integrate/astra_reconciliation/tree_differences.json; the full Astra manifest is alongside it. There are 59 changed paths: 17 Astra-only, 21 Claude-only, 21 modified on both sides. The latter are the twelve report notices, three launch documents, four historical prose corrections, the s63 inequality note and the sweep-script trailer fix. All other shared file blobs match, including numerical arrays and certificates. No scientific result conflict was found in this tree comparison; it is not a new numerical replay.

Recommendation: retain Claude's rewritten branch and its housekeeping. Review Astra's correction register and entry-point conventions for incorporation; use the existing census-first reconciler rather than blindly overlaying a second controlling ledger. The 17 Astra-only paths are explicitly listed in the manifest diff; objects can be supplied if requested. No old-history merge or object bundle was made.

Four requested artifacts were recovered. The 7,917,718-byte Gram JSON is supplied losslessly gzipped; decompress it into an isolated replay directory, using the original name. artifact_recovery.json records original and compressed hashes. The S4 input manifest and preflight and S6 input manifest are restored without byte changes. Restoring these inputs does not itself validate portability of the old absolute-path replay scripts.

The S6 minors reference points to results/astra/S1/n3_independent_minors.json, already present and matching the hash in S6's audit. It is not a missing S6-generated file. The s76 level_DD_pP.npz entry is an explicit statement of absence in S3's compatibility note, not a delivery promise. It remains a real dependency gap for full recursive pairing; s76 documents regeneration, which was not run here.

The handover repeats an incorrect general length bound min(r,delta,9). Use min(r,delta) for ambient constituents; the degree-eight conclusion is unaffected. Also distinguish the reconciler's r (ambient variables or exact partition length) explicitly when joining our n,delta,lambda cell keys; its meaning should not be inferred from the name.

GitHub clone failed due to network connection failure. A separate clone was made from the locally available rewritten integration branch c93242483b370dd46cf0d2f5b5fc362fa55f820d. Remote push/rewrite claims were not independently checked. Original clones were preserved. No branch was pushed and main was not changed.
