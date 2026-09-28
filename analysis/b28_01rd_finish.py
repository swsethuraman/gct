#!/usr/bin/env python3
"""Compare replay bytes, assemble review and receipts, and seal payload hashes."""
import json, pathlib, time
from b28_01rd_audit import ROOT, OUT, HOST, TAG, TIP, PARENT, HEAD, fileinfo, save, git, digest

t0=time.perf_counter()
audit_text=(ROOT/'analysis/b28_01rd_audit.py').read_text()
old_start=audit_text.index('    # Windows-created worktree')
old_end=audit_text.index('\n\ndef digest',old_start)
initial_audit=(audit_text[:old_start]+"    return subprocess.check_output(['git', '-c', f'safe.directory={ROOT}', '-C', str(ROOT), *args])"+audit_text[old_end:]).encode()
result=OUT/(TAG+'_p2147483647_verify.json')
old=OUT/'inputs'/result.name
assert result.read_bytes() == old.read_bytes(), 'STOP: mathematical replay bytes differ'
v=json.loads(result.read_bytes())
assert v['verdict']=='FULL_RANK' and len(v['checks'])==16 and all(v['checks'].values())
x=v['values']
assert x['cover_size']+x['rank_G']==x['n_chi']-v['a']==813205
assert x['rank_K_U']==x['mult_det_mod_p']==109 and x['minor_det_mod_p']==763718730
job=json.loads((OUT/'receipts/job_receipt.json').read_text())
launch=json.loads((OUT/'receipts/launch_receipt.json').read_text())
assert job['exit']==launch['exit']==0 and job['resource_stop'] is None
assert job['job_processes_remaining_at_end']==0 and len(job['steps'])==1
assert job['scope']==dict(memory_max='24000000000',memory_swap_max='0')
assert launch['end_unix']-launch['start_unix']<3600 and launch['elapsed_monotonic_secs']<3600
assert not job['steps'][0]['survivors_sigkilled'] and not job['steps'][0]['group_alive_after_step']
bindings=json.loads((OUT/'BINDINGS.json').read_text())
for row in bindings['frozen_d']:
    assert fileinfo(HOST/'frozen_d'/row['path'])=={k:row[k] for k in ('bytes','sha256')}
for row in bindings['host_retained']:
    assert fileinfo(HOST/row['host_path'])=={k:row[k] for k in ('bytes','sha256')}
assert git('rev-parse','HEAD').decode().strip()==HEAD
power=(OUT/'power_after_receipt.txt').read_text()
assert 'Current AC Power Setting Index: 0x00000000' in power
events=json.loads((OUT/'receipts/power_events_receipt.json').read_text(encoding='utf-8-sig'))
assert events['query_succeeded'] and not events['events'], 'STOP: sleep event or failed power-event query'
summary=dict(label='COMPUTED',verdict='ACCEPT',replay_verdict=v['verdict'],all_checks=v['checks'],
    mathematical_bytes_identical=True,regenerated=fileinfo(result),previous_committed=fileinfo(old),
    source_rank=x['cover_size']+x['rank_G'],kernel_rank=x['rank_K_U'],minor_order=109,
    minor_rows_zero_based=list(range(109)),minor_det_mod_p=x['minor_det_mod_p'],prime=v['prime'],
    E_sha256=x['E_sha256'],G_sha256=x['G_sha256'],VK_sha256=x['VK_sha256'],
    frozen_files_unchanged=True,host_retained_unchanged=True)
save(OUT/'COMPARISON.json',summary)
checks='\n'.join('- **COMPUTED:** `'+k+' = true`.' for k in v['checks'])
report=f'''# R28-01d — cross-lineage review of Cell A

**COMPUTED — ACCEPT: no determinant equation in Cell A.** The single independent
replay returns `FULL_RANK`, and its complete mathematical output is byte-identical
to B28-01b's committed replay. Achievement: a certified negative in one cell,
not PROVED and not a coefficient equation. None of the four achievements moves.

## D1 — Bindings: ACCEPT

**COMPUTED:** Reviewer branch `b28-01r` began at `{HEAD}`.
Producer tip is `{TIP}`, parent `{PARENT}`.
Its 26 changed paths comprise only its 25 manifest payloads (including the
report) and its manifest. The manifest hash is
`9beba33cce900aed46940d25eacf535820c379385c2a3225d9f944541a45f314`.
All 25 payload sizes and raw hashes match the committed blobs; all four
host-retained files match their committed sizes/hashes. All nine `frozen_d` files
match `{PARENT}:results/b28_01d/frozen_d_hashes.txt`, before and after the run.
The host-retained files are unchanged afterward. `BINDINGS.json` records every
path, byte count and full SHA-256, including the raw common, brief and board hashes.
The output paths were absent at initial preflight; untracked files were left alone.

**READ:** Governing mathematical text is
`96a8074d:results/b27_06/PREREGISTRATION.md`, specifically the source gate,
independent replay and full-rank lifting rules. The exact verifier and supervisor
read are `{PARENT}:analysis/b28_01c_verify.py` and
`{PARENT}:analysis/b28_01d_supervise.py`; their blob hashes are in `BINDINGS.json`.
The verifier reconstructs E, cover, G and evaluations without importing producer
code. It shares only the declared low-level NumPy/SciPy/python-flint libraries.

## D2 — Host condition: ACCEPT after user correction

**COMPUTED:** The initial read-only Windows query reported AC sleep index `0x00000384`.
Work stopped, and the user subsequently reported changing the setting and authorized
resumption. **COMPUTED:** Both the immediate pre-run and post-run queries report
AC index `0x00000000` (Never). The reviewer did not change power settings.
The Windows System-log query covering the actual launch interval found no sleep
or resume events; raw observations and query bounds are receipt-only payloads.

## D3 — Frozen verifier replay: ACCEPT

**COMPUTED:** Exactly one verifier invocation, at prime 2,147,483,647, used the
unchanged `~/b28_01/frozen_d/b28_01c_verify.py` and its bound `.so`. Committed
certificate, cell and pencil bytes were exported to the review's inputs directory;
the bound original kernel was read through `--kernel`. No producer, other cell,
additional prime, control, calibration or retry was run.

**COMPUTED:** The single scope enforced `MemoryMax=24000000000`,
`MemorySwapMax=0`, `RuntimeMaxSec=3600`; the unchanged frozen supervisor had a
3540-second deadline, leaving shutdown margin within the outer cap. Live cgroup
limits were asserted before starting the verifier. Exit was 0, with no resource
stop or surviving job process. All phase timings, resource measurements and
nondeterministic logs are in receipt payloads, separate from mathematical output.

**COMPUTED:** The complete regenerated verifier JSON has raw SHA-256
`{fileinfo(result)['sha256']}` ({fileinfo(result)['bytes']} bytes), identical byte
for byte to `{TIP}:results/b28_01b/out_cellA/{result.name}`.
`COMPARISON.json` records the comparison and every check:

{checks}

**COMPUTED — regenerated matrix hashes:**

| matrix | SHA-256 | precise bytes named |
|---|---|---|
| E | `{x['E_sha256']}` | CSR indptr, indices, data as contiguous little-endian int64, concatenated in that order, followed by UTF-8 JSON of shape |
| G | `{x['G_sha256']}` | row-major little-endian uint32 residual entries |
| VK | `{x['VK_sha256']}` | row-major little-endian uint32 evaluation entries |

## D4 — Certificate reading: ACCEPT

**COMPUTED:** The regenerated source has n = 813,314 columns, 2,310,607 rows and
10,062,442 nonzeros. The verified upper-triangular cover has 809,656 nonzero
pivots; U has 3,658 columns and the regenerated projected residual has rank 3,549.
Thus the lower bound on source rank is 809,656 + 3,549 = 813,205 = n - 109.
The original full kernel K, shape 813,314 by 109, is checked on every row of the
regenerated E; E K = 0 and rank K[U,:] = 109. These give the matching upper bound,
so rank over the specified finite field is exactly n - a, with a = 109.

**COMPUTED:** Independently regenerated evaluation VK has shape 117 by 109 and
rank 109. The claimed minor uses zero-based rows 0 through 108 and all columns;
the verifier recomputes its determinant as 763,718,730 modulo 2,147,483,647,
which is nonzero. This conclusion uses the fresh values, not stored rank claims.

**READ:** The preregistration fixes rational source multiplicity a = 109 and
requires these exact source and evaluation certificates for its lifting argument.
**HAND:** The nonzero source minor and the fixed rational source dimension make
the source kernel specialize without a dimension jump at this prime. Alternatively,
the verified source kernel and injective VK imply that the stacked integer matrix
[E; V] has trivial modular kernel and therefore full column rank over Q. Hence
evaluation is injective on the 109-dimensional rational source; determinant
multiplicity is 109 over Q. **COMPUTED:** Under the preregistered certificate rule,
this records no determinant equation in this cell; it is a certified negative.

## D5 — Sleep assessment: ACCEPT

**READ:** B28-01b's committed `host_power_events.txt`, supervisor receipt and GNU
time receipt place the suspension inside its verifier step. Its producer and
verifier both exited normally; the receipt records no resource stop, OOM, forced
termination, leftover process, or extra verifier step. The supervisor contains
no restart/retry path. Exact original timing observations remain in those committed
receipts, whose bytes are bound by the validated producer manifest.

**HAND:** Suspension affected elapsed-time accounting and violated the declared
host condition; the monotonic timer excluded suspended time. The evidence shows
no truncation, restart, or resource-stop path. All payload and retained-file hashes
are intact, and the clean replay reproduces the complete mathematical output.
There is no remaining evidence that suspension affected the certificate or verdict.
This does not erase the historical host-condition deviation.

## Outcome boundary

**COMPUTED:** D1–D5 ACCEPT; registered outcome **ACCEPT** for
"COMPUTED: no determinant equation in Cell A", lambda = (12,8,6,4,2), k = 8.
**HAND:** This is a certified negative in one cell. It supplies no coefficient
equation, padding separation, or positive multiplicity gap and moves none of
the four achievements (source condition, coefficient equation, separation on
padding, positive multiplicity gap). No geometric noncontainment or asymptotic
bound is claimed.

**READ — binding constraint:** "No five-row determinant equation is known to be nonzero on padding."

**READ — programme decision:** "no construction ready."
'''
(ROOT/'docs/b28_01rd_review.md').write_text(report)
save(OUT/'RESOURCE_RECEIPT.json',dict(schema='b28-01rd-resource/1',numerical_runs=1,
    command='PYTHONDONTWRITEBYTECODE=1 /home/swami/b28venv/bin/python analysis/b28_01rd_run.py',
    input_binding=fileinfo(OUT/'BINDINGS.json'),output=fileinfo(result),
    run=launch,scope=json.loads((OUT/'receipts/scope_receipt.json').read_text()),job=job,
    binding_run=json.loads((OUT/'binding_receipt.json').read_text()),
    preliminary_failed_metadata_audit=dict(wall_secs=2.2567975000000002,exit=1,
        input_worktree_pointer=fileinfo(ROOT/'.git'),script_sha256=digest(initial_audit),output_sha256=None,
        command='timeout 60s bash -c "ulimit -v 524288; python3 analysis/b28_01rd_audit.py bind"',
        reason='Linux Git could not interpret Windows absolute .git path; no numerical run and no output; audit helper corrected to supply translated --git-dir and --work-tree; repository configuration unchanged'),
    receipt_note='All *.log and *.time under receipts are resource receipt components, not mathematical outputs.',
    assembly_command='PYTHONDONTWRITEBYTECODE=1 python3 analysis/b28_01rd_finish.py',
    assembly_wall_secs=time.perf_counter()-t0,
    scripts={p.name:fileinfo(p) for p in sorted((ROOT/'analysis').glob('b28_01rd_*')) if p.is_file()}))
payloads=[ROOT/'docs/b28_01rd_review.md']+sorted(p for p in OUT.rglob('*') if p.is_file() and p.name!='MANIFEST.json')+sorted((ROOT/'analysis').glob('b28_01rd_*'))
save(OUT/'MANIFEST.json',dict(schema='b28-01rd-manifest/1',branch='b28-01r',parent=HEAD,
    rule='Raw file-byte SHA-256 and byte counts; every payload, excluding this manifest',count=len(payloads),
    files=[dict(path=str(p.relative_to(ROOT)),**fileinfo(p)) for p in payloads]))
print(json.dumps(dict(verdict='ACCEPT',manifest=fileinfo(OUT/'MANIFEST.json'),payloads=len(payloads)),indent=2))
