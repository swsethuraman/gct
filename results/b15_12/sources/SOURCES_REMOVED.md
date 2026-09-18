# Third-party PDFs removed from the checkout

Removed 2026-09-17 by the post-B19 housekeeping session (PART 8c), on the user's decision.
Reason: the checkout should not carry 1,086,823 B of third-party papers that no script opens.
Nothing was rewritten. Every blob stays in history and every hash pin still resolves.

| file | sha256 | bytes |
|---|---|---|
| `bip_1604.06431v3.pdf` | `b6d54e77f91579b01490e4ac9b8b1c46b29226c9dd33291ef1f093eb1950016d` | 406,395 |
| `blmw_0907.2850v2.pdf` | `70bb2af9d4cc56d41ab003f1ba56346a513f378e1edd49ed6e1190751252d226` | 346,907 |
| `ip_1512.03798v2.pdf` | `683d3aa4d89dfeb6f6f42ac05ef6545ccd91c3c84e95f813cc99799e45a39e2a` | 333,521 |

Introduced by `f57316b64975dc2ef0d93bdd4b821eba22a02204` (2026-09-13). The bytes are identical
at that commit, at the commit before this one and on disk at removal, so any of them recovers
the file:

    git show f57316b6:results/b15_12/sources/bip_1604.06431v3.pdf > results/b15_12/sources/bip_1604.06431v3.pdf

**`kl_1204.4693v1.pdf` is deliberately kept.** `analysis/b16_12_receive.py` (line 278) reads it
by path through `source_manifest.json` and asserts its hash, with no existence guard. Deleting
it would make that committed verifier raise `FileNotFoundError` on a fresh checkout before any
check runs.

**Every pin still resolves.** `results/b15_12/source_manifest.json` keeps all four rows with
their URLs, sizes and sha256 values; it pins by hash, not by a path it opens. The hash records
in `results/b16_12/{final_audit,receiver_*}.json`, `results/b16_12/input_paths.json` and the
archived B17-12 copies under `results/b17_12/inputs/` name only `kl_1204.4693v1.pdf`, which is
still present. A pre-check of every tracked file on this branch found exactly one reference to
each of the three removed names — the `"file"` field of its `source_manifest.json` row — and no
script, manifest or glob that opens them.
