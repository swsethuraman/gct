# Replay

Dependencies: Windows PowerShell, its C# compiler through Add-Type, and Python with NumPy. No flint, SymPy, network access or ambient Specht expansion is needed. Keep this directory and `continuation_20260908` under the frozen S3 directory because the scripts import its verified local helpers.

Quick read-only verification (hashes, original preservation, source residual, pairings, conversion identities, all 6,084 values and full scalar minors):

```powershell
$taskPython = 'C:/Users/swami/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe'
$taskDir = 'C:/Users/swami/Projects/gct-gpt/Batch12_Results/S3/degree13_conversion_20260908'
& $taskPython "$taskDir/src/verify_delivery.py"
```

Full numerical replay in a **new sibling directory**, preserving this delivery:

```powershell
& powershell -NoProfile -File "$taskDir/src/replay.ps1" -Python $taskPython
```

The script prints its destination. It reconstructs both sources, Grams, rational-source transport, source audit, all 78 accepted pairings, both conversions, evaluator diagnostics, 6,084 fresh evaluations and independent scalar audits. It copies only executable code and the selected original filling specifications, not computed pairing or evaluation answers. Selections are verified anew. It does not repeat unsuccessful candidate discovery or inspect/construct degree 24. Allow about 30 minutes for serial replay; this is an estimate based on the measured stage times. Each source has 180 seconds / 256 MiB, each pairing 20 seconds / 256 MiB, and each evaluation family/prime 900 seconds / 256 MiB. Stage limits are checked as described in the retained preregistrations; they are experiment bounds, not mathematical claims.

On an evaluator bound, the replay stops and preserves its completed JSONL values. Resume that exact evaluation stage in a fresh process using its printed input/output paths:

```powershell
$replayDir = 'C:/Users/swami/Projects/gct-gpt/Batch12_Results/S3/degree13_replay_YYYYMMDD_HHMMSS'
& powershell -NoProfile -File "$replayDir/src/evaluate_jobs.ps1" -InputFile "$replayDir/artifacts/jobs_generic_p2147483647.jsonl" -OutputFile "$replayDir/artifacts/values_generic_p2147483647.jsonl" -Seconds 900
& $taskPython "$replayDir/src/point_rank.py" --family generic --prime 2147483647
```

Substitute the actual replay directory, family and prime. The evaluator skips already saved IDs. A pairing bound retains the exact MPS/word/gate-prefix pickle and a JSON explanation; inspect it before choosing an alternate representative or new budget. Do not feed untrusted pickle files to Python.

After all four evaluation streams finish, run `evaluation_audit.py` and `verify_delivery.py` in the replay's `src` directory. The standalone verifier also works on the replay without a delivery manifest; it reports zero delivery hashes in that case and still checks arithmetic and frozen-input preservation.

Discovery replay is optional. Its executable stages are `select_stage.py`, `fallback_select.py`, `alternate_select.py`, `structured_select.py`, and `guided_select.py`; their exact stopping states and candidate specifications are retained here. The structured search had an unexplained coordinator wall interval, so reproducing its elapsed duration is not promised. The final selected-input replay is sufficient to reconstruct all success certificates.

The full delivery manifest covers reports, code, imported s76 inspection inputs, candidate specifications, completed results and stopped checkpoints. `scratch/` is excluded: it is only a local Git object reader used to inspect the s76 bundle, and is unnecessary for the degree-13 replay.
