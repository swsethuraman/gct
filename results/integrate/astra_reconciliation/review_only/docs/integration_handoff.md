# Batch 13 shared baseline handoff

Branch: `integration/batch13`. It contains all twelve session tips listed in
`results/integration/session_registry.json`, plus a separate housekeeping commit.
The original shared checkout and its main branch were not changed.

To consume the delivery bundle in either clone, first verify its SHA-256 against
the accompanying file. Run `git bundle verify PATH_TO_BUNDLE`, then
`git fetch PATH_TO_BUNDLE integration/batch13:integration/batch13` and create a
separate checkout with `git worktree add PATH_TO_NEW_CHECKOUT integration/batch13`.
If that branch already exists, inspect its commit before replacing anything.
Use the same resulting commit on both sides. These commands do not merge main.

Start with `START_HERE.md`. The session registry preserves provenance; the cell
catalog provides discovery; correction notices qualify historical prose. The
artifact index covers tracked files under analysis, docs and results, not external
Downloads, other checkouts, untracked files, or every historical conversation.
Unparsed result files include supporting metadata as well as potential results;
their count is not a count of missing theorems.

Artifact records retain a portable Git blob identifier as well as the indexed
working file's SHA-256. Text-file SHA-256 values can change with Windows/Linux
line endings; use Git blob identifiers for that comparison. Stage intended
changes before rebuilding the index so its blob identifiers reflect them.

Checks performed here: ancestry of all twelve session tips; the 25 inherited
ledger semantic checks; validation of dimensions and both-prime full ranks for
214 added observations. These are integration checks, not new numerical replay
of those observations. Frozen numerical certificate contents were not modified.

Remaining acceptance work, in order:

1. Provision a shared numerical environment with SciPy and python-flint and record
   exact versions. The available integration runtime lacks those packages.
2. Execute the combined production gate in `interoperability.md`, then select a
   supported common entry point. Coexisting modules do not yet form one API.
3. Retrieve omitted s79 and B13-09 certificates, retaining an explicit missing
   status until received or regenerated. Do not count a record as a replay.
4. Audit historical inventories against the artifact index, prioritizing exact
   identities, containment/stability rules and negative results. Extend parsers
   without silently changing the frozen B13-11 snapshot.
5. Before Batch 14 dispatch, use the corrected union of results and check inherited
   exclusions. Register new observations and evidence at delivery, not only in chat.

The frontiers in coverage.json are reviewed conclusions, not calculated by the
catalog. Report search matches are discovery aids; always read the cited source
and correction register before using a result.
