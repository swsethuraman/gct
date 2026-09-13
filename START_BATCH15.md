# Start the new GCT Batch 15 project here

Read [the twelve-session board](docs/batch15/BOARD.md), [accepted mathematical state](docs/batch15/ACCEPTED_STATE.md) and [new integrator prompt](docs/batch15/NEW_INTEGRATOR_PROMPT.md).

All twelve sessions use Astra. Every detailed brief is in `docs/batch15/briefs/`; all share `docs/batch15/WORKER_PREAMBLE.md`. The annotated `batch15-base` tag fixes the launch version. Exact base commit, tree, tag object and complete worker dispatch messages are in the external `Batch15_Launch` folder alongside the outer project.

This checkout includes the final Batch14 housekeeping and the separately accepted CI73 continuation. The canonical project and remote were left unchanged. No Batch15 workers have been launched by preparing this folder.

The input preflight is `tools/delivery/preflight_batch15.py`. Delivery uses `check_batch15.py` and `package_batch15.py` in the same directory. The portable slot/tool SHA256 convention is UTF-8 text with CRLF normalized to LF; binary files remain byte-exact. Hashes in preserved historical receipts retain their original conventions. Git commit/tree checks are always exact.
