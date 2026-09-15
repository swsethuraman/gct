# B16-11 frozen-launch receiver

Read REPORT.md and RECEIVER_SPEC.md. INPUT_HASHES.json pins the108 semantic/audit input copies. DELIVERY_MANIFEST.json seals this filesystem delivery; no commit or common merged base is asserted. The B15 proofs and expensive calculations are inherited. This receiver verifies metadata, conditional arithmetic, and its own rejection controls only.

From the assigned B15-11 worktree (choose fresh output names):

```powershell
& ./.venv/python.exe -B delivery/b16_11/b15_bound.py --slot 11 --name b16_11_receive_again --seconds 60 --memory-mb 512 delivery/b16_11/b16_11_receiver.py --package delivery/b16_11 --output results/b16_11/receive_again.json
```

Core b16_11_receiver.py and b15_bound.py are portable together with evidence/ and INPUT_HASHES.json. The test, build, Git and finalize scripts preserve provenance and use the original worktree layout; they are not the portable entry point. Another OS needs an equivalent enforced supervisor. No inherited producer code is executed.

Final archive-generation resources and final process exit are sibling worktree artifacts results/logs/b16_11_finalize_02_resources.json and results/b16_11/process_exit.json. The archive contains completed build, receiver and integration-control receipts; it cannot contain the receipt written after its own creation.
