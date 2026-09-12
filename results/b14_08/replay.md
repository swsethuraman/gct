# B14-08 replay and receiving instructions

This delivery is gpt-6-astra, xhigh, board_numbering batch14. It certifies the
239-row/717-test finite transport audit and 61 ambient factor HWVs. It does not
certify padded source equations, determinant rank upper bounds, or a new D gap.
Use the delivery manifest for the final head and tree; the fixed prerequisite is
commit 9898e56941a7665f231873481dae956f08509995, tree
cb688cd3fe454d638f3202e759e2eaa0c629739f. The bundle exposes
refs/heads/b14-08-astra. One part00 is an exact copy of the small whole bundle.

## Receive without changing integration

Use a separate checkout with the frozen base already available. Verify the
whole bundle's bare-filename MD5 and SHA256 sidecars (or reassemble contiguous
parts in binary order, then verify the whole digest). Example PowerShell from
the separate receiving repository:

```powershell
git bundle verify 'C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-08/b14_08_astra.bundle'
git bundle list-heads 'C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-08/b14_08_astra.bundle'
git fetch 'C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-08/b14_08_astra.bundle' 'b14-08-astra:b14-08-astra'
git switch b14-08-astra
git log -1 --format='%H %T' b14-08-astra
```

Compare the last command to delivery_manifest.json. Do not switch a shared
integration checkout. The original session used the already prepared worktree
at C:/Users/swami/Projects/gct-gpt/work/batch14/B14-08.

## Bounded Windows replay

Run from that worktree (or a separate received copy) using Python 3.12 or newer.
The fresh audit and exact witness checks use only stdlib. The explicitly
historical script replay additionally needs numpy; 2.3.5 was present here.

```powershell
$auditPython = 'C:/Users/swami/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe'
& $auditPython analysis/b14_08_bound.py --name replay --seconds 180 --mib 512 -- analysis/b14_08_audit.py --out results/b14_08/replay_output
if ($LASTEXITCODE -ne 0) { throw 'Audit failed' }
& $auditPython analysis/b14_08_bound.py --name replay_verify --seconds 180 --mib 512 -- analysis/b14_08_verify.py --data results/b14_08/replay_output --out results/b14_08/replay_verification.json
if ($LASTEXITCODE -ne 0) { throw 'Verification failed' }
```

Expected: 239 records, 717 tests, 600 dominance failures, 51 exact zero
multiplicities, 66 positive pairs with 61 HWVs; 5/31 reached at degree 25 and
26/208 at degree 26; 694 monomial-count checks, 239 birth-bound checks, 29 local
controls and eight historical runs. All 135 ten-row records are unreached.
There are four inherited numerical birth increments (0,1,0,1 in table order)
and 235 unresolved exact increments with conservative certified integer bounds.
No new exclusions are expected. Timing fields and resource/PID values naturally
change; mathematical content is deterministic.

The native wrapper enforces memory and wall bounds before loading the script,
sets numerical-library thread counts to one, writes the current PID, and stores
peak memory/time in results/logs/b14_08_<name>.resources.json. Non-Windows
receivers should impose equivalent native wall and address-space limits before
calling the two scripts directly. One process at a time suffices.

## Interfaces and evidence interpretation

- census.json: complete target keys, three sources and their differences;
  dominance inversions or exact character sums; positive witness IDs;
  Lemma T floor expressions and missing certificate fields; Lemma B predecessor,
  symbolic inequality, inherited dimensions and proved scalar-tail upper bound.
- witnesses.json: ordinary c_alpha integer polynomials with explicit exponent
  tuples, powers, coefficient values_are, normalization denominators, and
  raising-matrix orientation. Witnesses prove factor existence, not membership
  in the padded or determinant ideal.
- verification.json: exact independent derivative checks, input blob audit,
  character term recounts, negative controls, and historical exit transcripts.
- historical_00.json: the valid historical replay. historical_06.json and
  historical_07.json: deliberately invalid fixtures; their rejected status is
  in verification.json. Never consume these as a census.
- input_manifest.json: frozen prerequisite blob IDs and working-byte SHA256.
  External dispatch paths are provenance; the tracked complete packet is the
  portable prerequisite. The verifier permits only appends to PROVED.md and
  checks its inherited text against the exact frozen object.

The multiplication factors use a common Z model. Both primes avoid every
recorded rational construction denominator. The witness verifier proves zero
raising derivatives over Z before checking nonzero reductions; it never uses
modular deficient rank to assert a rational ideal equation. No points or
transported value matrices are claimed. A future transported evaluation
certificate must additionally include its actual points and nonzero u-values.

## Delivery gate commands

From the session worktree, with all intentional changes committed:

```powershell
& $auditPython tools/delivery/check_delivery.py --branch b14-08-astra --base 9898e56941a7665f231873481dae956f08509995
git bundle create 'C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-08/b14_08_astra.bundle' 9898e56941a7665f231873481dae956f08509995..b14-08-astra b14-08-astra
& $auditPython tools/delivery/check_delivery.py --branch b14-08-astra --base 9898e56941a7665f231873481dae956f08509995 --bundle 'C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-08/b14_08_astra.bundle'
```

The delivery script additionally verifies the bundle, tests an actual fetch by
the named branch in a temporary receiver, checks its head/tree, and produces
whole/part bare-filename checksum sidecars. See the delivery verification logs.
