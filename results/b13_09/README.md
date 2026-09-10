# B13-09 artefacts — what is authoritative, and why two files can disagree

board_numbering: batch13

**`per_r{r}_d{delta}.jsonl` is authoritative** for what was measured.  Each line
is one weight's complete record, written by `analysis/b13_09_per_r.py` itself at
the end of that weight's own subprocess.  165 records in all: 5 + 42 + 105 + 5 + 8.

**`status_r{r}_d{delta}.json` is a per-invocation log of one sweep process**, not
a ledger of the group.  It can undercount, for two recorded reasons:

1. The sweeps were **restarted** when Addendum C changed the queue order from
   `N_S` to refitted cost, and again when stream B was ended to free CPU for the
   `(8,8)` group-completing weight.  A restarted sweep writes a fresh status file
   and re-reads the JSONL to skip what is already banked, so the *last* status
   file for a group covers only that invocation.
2. An **in-flight child keeps running and writes its own record** when its parent
   sweep is ended, because the evaluator appends to `--out` itself.  Those weights
   are in the JSONL and not in any status file.

So a reviewer counting from `status_*.json` will get a number at or below the
JSONL count, and the difference is exactly the weights described above.  Every
table in `docs/b13_09_report.md` is generated from the JSONL by
`analysis/b13_09_report.py`, so no number in the report is hand-transcribed and
none comes from a status file except the *reasons* in the not-reached table.

**`notreached_r8_d8_stab5040.json`** is the one weight that was attempted and not
completed: `(10,2,2,2,2,2,2,2)_8`, `|Stab| = 5040`, ended by its own
`timeout 5400` bound after 2 940 s of CPU inside the orbit setup.  It has no
record in the JSONL because it produced no result, and its absence is the reason
`I(D_8^{per_3})_8 = 0` is a five-of-six prefix rather than a theorem.

**`cert_manifest.json`** reads `git ls-files`, so its `shipped_in_bundle` flags
cannot disagree with the bundle.  252 certificates, 181.8 MB in all, none over the
5 MB repository limit, 84 shipped; every unshipped one carries its md5 and the
command that regenerates it.
