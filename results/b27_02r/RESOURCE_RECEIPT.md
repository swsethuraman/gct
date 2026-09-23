# R27-02 resource receipt

Claude Code (Opus 5.5), 2026-09-23. **COMPUTED** entries are exact runs; everything else is
**READ** administration. No installs, subagents, other sessions, messages, random searches or
sampled nullspaces. Python 3.12.10 on PATH; SymPy 1.14.0 was already installed.

## Runs: 4 of the 10 allowed, sequential, each capped at 60 s wall and 512 MiB

| run | command | start UTC | wall s | peak job bytes | exit | input SHA-256 | output SHA-256 |
|---|---|---|---:|---:|---:|---|---|
| 1 | `python analysis/b27_02_run.py run01 grouped` (producer code, replay tree) | 04:07:16Z | 0.076 | 33333248 | 0 | run `83343936…`, verify `fed48cb0…`, candidate `b75f8e9c…`, bindings `fd2a4437…` | `a4ae4176f63460cc84e938847e9e59b8c62e86f03812486047b64af225f31d5b` (**matches** producer run01) |
| 2 | `python analysis/b27_02_run.py run02 full` (producer code, replay tree) | 04:07:22Z | 0.855 | 33157120 | 0 | same four inputs | `92d8fbe91d0abe8847e13492ff4642f8bf733863c77d055c135b84517c2b6b1b` (**matches** producer run02) |
| 3 | `python analysis/b27_02r_run.py run03` → `b27_02r_check.py` | 04:08:17Z | 1.218 | 70746112 | 0 | check `c9803948ddb89a3eb59f458094336dc3dd1dcf04e224c084e375e5056f0d8e3b` | `b7982ebd9f7a10bdf07ae4ef25cb34f172b935a613c387b24b601dafa2da5b4f` |
| 4 | `python analysis/b27_02r_run.py run04 b27_02r_p4det.py` | 04:09:30Z | 0.873 | 68636672 | 0 | p4det `d65f6e4a0ff0fc927c34a31c0d3544c9f68b2721e75fd8b1ceef55aa20baf9b9` | `c10637c0d9d8030322f56916b78fc69b241c8eee44e47d1e9fe78601e3f5228e` |

- **Replay tree for runs 1–2.** The four producer inputs were written from committed blobs at
  `35eeff49` into a scratch directory, and their raw SHA-256 values were checked against the
  producer's receipt before running. The producer runner applies its own 512 MiB Job Object and
  55 s watchdog. Its resource receipts are kept as `replay_run01_resources.json` and
  `replay_run02_resources.json`. The output files are byte-identical to the producer's committed
  outputs, so they are not recopied.
- **Runner for runs 3–4.** `analysis/b27_02r_run.py` applies a 512 MiB Job Object cap and a 60 s
  timeout. Run 3 used its first version (SHA-256
  `d163da729303d05101e6e72917acf82de3b9426485140c59befadc7e018a1c4e`). Before run 4, the only
  change was the optional script argument. The committed runner is that second version, and
  MANIFEST.json binds it.
- **Wall time.** The session ran from about 04:03Z to about 04:13Z, inside the 60-minute ceiling.
