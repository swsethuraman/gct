# B27-06 — record-search audit

**READ — finding.** No determinant-rank measurement was found at `(12,8,6,4,2), k=8` or `(14,10,6,4,2), k=9` in the available committed record. This is a scoped retrieval finding, not a mathematical proof that no measurement exists elsewhere.

**READ — frozen scope.** GIT_REFS.txt lists all local refs used. GIT_REACHABLE_OBJECTS.txt and GIT_OBJECT_SIZES.txt enumerate the reachable object set; RECORD_INVENTORY.json contains 14,130 unique blobs totaling 709,592,918 raw bytes. The continuation preflight verified that current refs are byte-for-byte unchanged, and rechecked every cited input against its committed blob. There was no fetch or Git write. Unreachable objects, absent remote-only commits and uncommitted files are outside this search.

**READ — search mechanics.** b27_06_record.py used broad partition patterns tolerant of whitespace and comma/semicolon/underscore/bar/bracket/quote separators. It read every text blob, decompressed gzip records, and searched text ZIP members. The scan processed 3,777,345,506 decoded bytes and returned 355 substring hits in 106 blobs or archive members. RECORD_SEARCH_MATCHES.json records offsets, line numbers and contextual excerpts. SEARCH_BLOB_BINDINGS.json distinguishes each raw Git-blob SHA-256 from the hash of its decoded/searched content. Compressed and uncompressed hashes do not name the same bytes.

**READ — binary review.** BINARY_REVIEW.json inventories 73 binary objects/archive containers. It includes text extraction searches of five committed PDFs, a non-executing unpickler review of seven historical pickle versions, and NPZ/NPY array metadata. No PDF or pickle target match was found. The numerical sidecars belong to other identified cells or small Gram experiments; their associated textual records were searched. Compiled libraries, bytecode, images and unlabelled scratch arrays were not reverse-engineered into supposed new mathematical claims. PDF content was used for target-string retrieval only, not as an external mathematical premise.

**READ — one archive exception.** Blob `e70135fcb3355c15e97132efc136f81f2b0519a4`, `results/certs/s60/15_7_4_1_1_d7_det_pencil_p2147483647.json.gz`, is historically truncated. Its raw SHA-256 is `e7e40643f64c7d2a61b56bbc92926071ec3f6b0ade402e7803b0d6a6e2c97a3d` (34,028 bytes). The available 483,496-byte decoded prefix was searched. Its certificate title and cell metadata identify `(15,7,4,1,1), degree 7, a=8`, a different cell. ARCHIVE_EXCEPTIONS.json preserves the exact exception and prefix. No absent suffix was treated as read.

**READ — classification of apparent hits.** Actual target entries are dimension/census rows, symmetric Kronecker calculations, skipped Session 54 jobs, open inventories, or queues. Other hits are proper substrings of longer partitions and numerical character tables. In particular:

| Evidence | Meaning |
|---|---|
| s54_cells_d8.jsonl:292; s54_cells_d9.jsonl:431 | Explicit `over_maxnb` skips |
| s58_calibration.jsonl:820,1504 | Target representation room, not restriction rank |
| s60_census.json and s60_tail_census.json | Carrier/source sizes and tail information |
| s60_cells.jsonl; s60_closing_cells.jsonl | No exact-target measurement rows |
| s71_sweep.jsonl; s79_cells.jsonl | No exact-target measurement rows |
| s71_queue.json positions 397,497 | Larger closing cells outside the measured 151-cell prefix; `rank` is queue order |
| b13_11 candidate inventory and ledger | Open status and empty rank evidence |
| b14_11 inventory/cost queue | Degree-8 historical rank `NOT_FOUND` |
| Reconciliation cells.part03:48 / part04:468 | Import only the skipped s54 records, empty ranks |
| s76_amb_refs.json | Ambient a=109, not determinant rank |
| s79_queue2.json substring matches | Different longer partitions |
| c4054603:b15_11/frontier.part03.jsonl:95 | Degree-8 unresolved candidate, empty recorded/replayed evidence |

**READ — citation resolution.** Except the explicitly later c4054603 frontier, these path names resolve at C=`7c36a52ddf338eb390a9bcd491cb9c50cf9e2a19`; exact full paths, commits, blob IDs, raw hashes and snapshots are in INPUT_BINDINGS.json. TARGET_RECORD_EXCERPTS.json stores the parsed exact-target records with JSON pointers/line numbers. A candidate inventory's absence of evidence was not used by itself to declare the whole-record negative.

**HAND — scope of the conclusion.** Rung 0 permits continuing to price a measurement. It supplies no determinant multiplicity, no equation, and no padding conclusion. A future executor must stop if contrary rank evidence is found.
