#!/usr/bin/env python3
"""Assemble the review resource index and raw-byte payload manifest."""
import datetime
import hashlib
import json
import pathlib
import time

WT=pathlib.Path('/mnt/c/Users/swami/Projects/gct-gpt/work/batch28/b28-01r')
OUT=WT/'results/b28_01r'

def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''): h.update(b)
    return dict(bytes=path.stat().st_size,sha256=h.hexdigest())
def save(path,obj): path.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')

def main():
    start=time.monotonic()
    read=lambda p:json.loads((OUT/p).read_text())
    bind=read('BINDINGS.json'); replay=read('REPLAY_COMPARISON.json')
    assert bind['all_match'] and replay['all_mathematical_outputs_byte_identical']
    assert len(replay['comparisons'])==26
    math_runs=read('replay_receipts/runs_receipt.json')
    cert_runs=read('certificate_control_receipts/RESOURCE_RECEIPT.json')
    completion=read('replay_receipts/completion_receipt.json')
    aux=[read('binding_receipt.json'),read('audit_receipt.json')]
    assert completion['wall_seconds']+cert_runs['wall_seconds']+sum(x['wall_seconds'] for x in aux)<3600
    assert completion['frozen_host_bytes_unchanged']
    assert not (pathlib.Path.home()/'b28_01/out/cellA').exists()
    payload_roots=[WT/'docs/b28_01r_review.md',*sorted((WT/'analysis').glob('b28_01r_*'))]
    assert all(p.is_file() for p in payload_roots)
    for receipt in [*aux,completion,cert_runs]:
        script=receipt['script']
        assert any(digest(p)==script for p in payload_roots if p.suffix=='.py'),script
    # Each job command/stdout/stderr/code hash is already recorded in these receipts.
    index=['binding_receipt.json','audit_receipt.json','scope_time_receipt.txt','scope_limits_receipt.txt',
           'replay_receipts/runs_receipt.json','replay_receipts/completion_receipt.json',
           'replay_receipts/host_retained_receipt.json','certificate_control_scope_receipt.txt',
           'certificate_control_receipts/RESOURCE_RECEIPT.json']
    output_files=[p for p in sorted(OUT.rglob('*')) if p.is_file() and p.name not in ('MANIFEST.json','RESOURCE_RECEIPT.json')]
    save(OUT/'RESOURCE_RECEIPT.json',dict(schema='r28-01-resource-receipt/1',
        generated_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        authorization='R28-01 user launch; no installs, no Cell A build, no change under ~/b28_01',
        hash_convention='SHA-256 of raw bytes; every payload is additionally bound by MANIFEST.json',
        windows_mathematical_runs=0,auxiliary_hash_exact_audits=2,
        auxiliary_limit='each timeout 60 seconds, ulimit -v 500000 KiB = 512000000 bytes',
        wsl_replay_python_invocations=len(math_runs['runs']),
        wsl_additional_control_python_invocations=len(cert_runs['runs']),
        wsl_calibration_cells_run=1,wsl_calibration_cell='(13,9,9,3,1,1), k=9, one prime',
        wsl_main_scope=dict(memory_bytes=8000000000,swap_bytes=0,hard_timeout_seconds=3600),
        wsl_additional_controls_scope=dict(memory_bytes=512000000,swap_bytes=0,hard_timeout_seconds=60),
        scope_command='systemd-run --user --scope --unit=b28-01r-review -p MemoryMax=8000000000 -p MemorySwapMax=0 /usr/bin/time -v -o results/b28_01r/scope_time_receipt.txt timeout --signal=KILL 3600 /home/swami/b28venv/bin/python analysis/b28_01r_replay.py',
        extra_controls_command='systemd-run --user --scope --unit=b28-01r-certificate-controls -p MemoryMax=512000000 -p MemorySwapMax=0 /usr/bin/time -v -o results/b28_01r/certificate_control_scope_receipt.txt timeout --signal=KILL 60 /home/swami/b28venv/bin/python analysis/b28_01r_certificate_controls.py',
        finalizer_command='timeout 60 bash -c "ulimit -v 500000; exec python3 analysis/b28_01r_finalize.py"',
        all_runs_sequential=True,main_replay_internal_wall_seconds=completion['wall_seconds'],
        additional_controls_internal_wall_seconds=cert_runs['wall_seconds'],
        main_outer_elapsed_seconds=556.11,
        elapsed_note='Outer GNU time is 9:16.11; internal monotonic runner elapsed is recorded separately. Both and auxiliary/control work together are below one hour.',
        main_max_observed_phase_VmHWM_bytes=5645541376,
        original_files_untouched=True,raw_source_hashes_rechecked_after_replay=True,
        scripts={p.relative_to(WT).as_posix():digest(p) for p in payload_roots if p.suffix=='.py'},
        inputs=dict(producer_tip=bind['producer_tip'],producer_manifest=bind['manifest'],
                    binding_file=digest(OUT/'BINDINGS.json'),audit_input_file=digest(OUT/'AUDIT_INPUTS.json')),
        receipts={p:digest(OUT/p) for p in index},
        run_outputs={p.relative_to(OUT).as_posix():digest(p) for p in output_files},
        finalization_hashing_wall_seconds=time.monotonic()-start,
        excluded_nonnumerical_operations='Shell/Git text reads, metadata inspection, file writing and authorized Git delivery; no numerical search or target construction.'))
    files=payload_roots+[p for p in sorted(OUT.rglob('*')) if p.is_file() and p.name!='MANIFEST.json']
    assert len(files)==len(set(files))
    manifest=dict(schema='r28-01-manifest/1',slot='R28-01',branch='b28-01r',
        base='ee354b57a9f60baacef7f451db28e5cce86d29bd',producer_tip=bind['producer_tip'],
        verdicts=dict(R1='ACCEPT',R2='REPAIR',R3='REPAIR',R4='ACCEPT',R5='REPAIR',R6='ACCEPT'),
        launch='YES after listed repairs',achievement='Review only; no achievement level moves; Cell A unbuilt',
        hash_convention='SHA-256 of raw file bytes',excludes=['results/b28_01r/MANIFEST.json'],
        payloads=[dict(path=p.relative_to(WT).as_posix(),**digest(p)) for p in sorted(files)])
    save(OUT/'MANIFEST.json',manifest)
    print(json.dumps(dict(payloads=len(files),manifest=digest(OUT/'MANIFEST.json'))))

if __name__=='__main__': main()
