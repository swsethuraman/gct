# `results/s36_cells/`

Per-cell measurement records from session 36 and later.

**Three files are stored gzipped.**  The padded-side vectors at
`(8,8,8,2,2)`, `δ = 7` — the exact-`ℤ` vector and the two mod-`p` vectors —
are 12–13 MB uncompressed, over the repository's 5 MB limit, and compress
about seventeen-fold:

    8_8_8_2_2_d7_pad_exactZ.txt.gz              11.9 MB -> 0.65 MB
    8_8_8_2_2_d7_pad_p2147483629_vec1.txt.gz    12.5 MB -> 0.74 MB
    8_8_8_2_2_d7_pad_p2147483647_vec1.txt.gz    12.4 MB -> 0.73 MB

Read them with `gzip -dc`, or in Python with `gzip.open(path, 'rt')`.  The
uncompressed content is unchanged — same bytes, same format as every other
`.txt` record in this directory.  This follows the precedent set at session 43
and the recommendation in `docs/s49_report.md` §4.

The uncompressed blobs remain in the git history before this commit; they are
removed by the history rewrite recorded in `docs/history_rewrite.md`.
