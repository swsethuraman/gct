# Review of the Batch 14 housekeeping handoff

The supplied bundle verifies against its MD5 and SHA256 and advances the integrated branch to1e61cfb171ed521368d79840680895ae1b945916. The old canonical local checkout was2816cdc78554115543e2768fc45e905f6b2580e6. An independent launch clone now combines the handoff and accepted CI73 continuation. Canonical shared files and remote branches were not changed by this preparation.

The contract's core lessons are sound: dispatch the real commit and tree, package the named branch, build a manifest only after the last commit, preserve actual model attribution, keep rank floors separate from global equations, and require checks that accept valid inputs and reject invalid ones.

I read the nineteen-case selftest. Its cases do not establish that all thirteen requirements work in all supported modes. In particular, the selftest children and fixture names remain tied to Batch14 even when the parent accepts another batch. The new focused Batch15 suite tests current batch/tag parameters, paths with spaces, committed versus working bytes, missing/empty/wrong manifests, stale bundle heads, absent prerequisites, and nested predicate validation. It includes legitimate positive controls. Its machine receipt is in `results/b15_prep/checks/delivery_selftest.json`.

| Gap in the supplied tool | Session-facing repair |
|---|---|
| Several checks inspect mutable working files while claiming to check a branch | Read committed blobs, including paths with spaces; missing working files cannot hide committed errors |
| Missing base tag can become only a note | Require an annotated tag whose peeled commit and declared tree match the dispatch |
| Manifest may be absent or empty; syntax-only hashes need not bind the actual base | Require a populated canonical manifest and compare every base/head/tree/hash/size to the actual objects |
| Bundle named ref need not match the current branch; prerequisite parsing can miss hashes followed by subjects | Parse the bundle header, require the current named head and exactly the frozen prerequisite |
| Concurrent workers all edit the theorem index | Per-slot proof files and proposed exclusions; one integrator writes shared records |
| Predicate-key lists can drift, and unused any_of alternatives can escape checks | Consumer-owned validate_predicate validates every branch before evaluation |
| POSIX-only resource commands and ignored PID records | An adapted accepted Windows aggregate runner, per-slot PID log exception and explicit runtime preflight |
| Format limits are confused with mathematical certifiability | Keep portable-certificate gaps separate from whether a theorem has been proved |

The new `check_batch15.py` is an additional explicit Batch15 contract, not a retroactive reclassification of historical deliveries. The historical checker stays unchanged. New slots receive a canonical manifest template through the packaging helper; old manifests retain their field names and provenance. The new guard's PASS certifies packaging, never mathematics.

The quoted incidence counts (eleven missing dispatches, seven HEAD-only bundles, four malformed Astra prerequisite fields) remain attributed to Claude's close audit. I have not rederived all incident counts from complete per-session event histories, so I do not promote them to an independent recount. The reproducible local problems included missing flint, Windows-incompatible launch commands, paths tied to another checkout, PID tracking gaps and the absence of a shared immutable dispatch message. These explain practical repairs without inventing session timings.

The supplied mathematical carry-forward needs the explicit corrections in `ACCEPTED_STATE.md`: four equations do not force D=-4; degree13 is complete; stable ideal bounds may transfer before ambient stabilization; operational queue counts are not theorem counts; independent padding must not inherit an unproved nine-variable restriction. Protected-paper errata remain separately visible.
