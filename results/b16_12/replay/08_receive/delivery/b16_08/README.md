# B16-08 receiver package

From this existing worktree, run `./delivery/b16_08/RECEIVE.ps1` in
PowerShell. It uses the worktree `.venv/python.exe`, the unchanged,
inspected `analysis/b15_bound.py`, and a fresh owned resource-receipt
name. The cap is 60 seconds/512 MiB with one process and one BLAS thread.
No heavy lease is needed for this small receiver.

The proof is `docs/b16_08_proof.md`, concise report
`docs/b16_08_report.md`, and executable source `analysis/b16_08_jets.py`.
`results/b16_08/certificate.json` contains the complete arithmetic.
`INPUT_HASHES.json` records raw SHA256 of every read research/control
input, preserving provenance and the per-worktree frozen head.
`ARTIFACT_HASHES.json` identifies immutable produced evidence; mutable
fresh receiver/resource outputs are kept outside that hash set.

The receiver recomputes determinant coefficients and all nonzero square
minors. It also verifies the input and artifact hashes if manifests are
present. It does not infer a polynomial equation from sampled zeros or
claim a full elimination ideal. The exact output is injectivity of the
34-coefficient chart map on the ordinary degree-at-most-two polynomial
space. This is not a sixteen-variable quartic equation.
