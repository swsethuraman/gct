# S3's degree-13 conversion — what is in the tree and what is not

Staged from `Projects\gct-gpt\Batch12_Results\S3\degree13_conversion_20260908`
on the delivering host.  The review found this material missing from the tree at
the batch-13 freeze; this closes that gap for everything the five-megabyte rule
allows.

**These are session deliverables, not integrator-verified results.**  Treat every
number as MEASURED-by-S3 until this repository's own code has re-derived it.  The
integrator has independently confirmed only `a₁₃ = 39` (three ways) and the
report's internal arithmetic (`6 084 = 4 × 39²`); the conversion and evaluation
certificates have not been replayed here.

## In the tree

    artifacts/common_source_transport.json    the rational-source convention and
                                              the transports L; det L at the root
    artifacts/conversion_certificate.json     C = G_M^-1 A, the full 39x39 minors
    artifacts/evaluation_certificate.json     generic and determinant evaluation
                                              matrices and their determinants
    artifacts/node_certificates_p*.json       per-node residual, pivots, minor,
                                              kernel, free-row identity
    artifacts/gram_nodes_p*.json              the invariant Gram forms
    artifacts/independent_source_audit.json   S3's own audit
    artifacts/source_path_witnesses.json      the path witnesses that supplied
                                              the last two pairing ranks
    artifacts/points_det.json                 integer determinant pencils
    artifacts/points_generic.json             integer generic coefficient vectors
    artifacts/rank_{det,generic}_p*.json      point-by-point rank growth
    artifacts/resource_summary.json           costs, bounds and the overrun
    delivery_manifest.json                    the full file list with digests
    REPORT.md, REPLAY.md, CLAIM_LEDGER.md, S76_COMPATIBILITY.md

## Not in the tree — over five megabytes

    artifacts/gram_spherical.json          7,917,718 bytes
    artifacts/nodes_p2147483647.json       5,768,534
    artifacts/nodes_p2147483629.json       5,768,436

Three files, 19.5 MB.  They are the per-node source records and the spherical
Gram.  A session that needs them takes them from the delivering host's
`degree13_conversion_20260908/artifacts/`; `delivery_manifest.json` carries their
digests so what arrives can be checked.

## Not in the tree — replay scratch

`artifacts/pair_*_checkpoint.pkl` (nine files, 900 MB), the four
`jobs_{det,generic}_p*.jsonl` streams (115 MB), `control_p*.json` (14.7 MB), and
`scratch/`.  These are resumable state and raw per-evaluation records, not
inputs; `REPLAY.md` says how to regenerate them.

Author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
