"""Record completed small runs and portable per-slot source hashes."""
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/b15_07'


def main():
    records=[]
    for path in sorted((ROOT/'results/logs').glob('b15_07_*_resources.json')):
        if 'runtime_native' in path.name:
            continue  # setup provenance, not this research session
        record=json.loads(path.read_text(encoding='utf-8'))
        assert record['exit_code']==0 and record['job_object_enforced']
        assert record['workers']==record['blas_threads']==1
        log=path.with_name(path.name.removesuffix('_resources.json')+'.log')
        raw=log.read_bytes()
        # PowerShell transcript encodings vary. Normalize only these new
        # per-slot research logs; native setup receipts are left untouched.
        if raw.startswith((b'\xff\xfe',b'\xfe\xff')):
            log.write_text(raw.decode('utf-16'),encoding='utf-8')
        else:
            raw.decode('utf-8')
        records.append(dict(name=path.stem.removesuffix('_resources'),
            resource_file=str(path.relative_to(ROOT)).replace('\\','/'),
            log_file=str(log.relative_to(ROOT)).replace('\\','/'),
            pid=record['pid'],started_utc=record['started_utc'],exit_code=record['exit_code'],
            wall_seconds=record['wall_seconds'],
            aggregate_peak_committed_bytes=record['job_memory']['peak_job_memory'],
            process_peak_working_set_bytes=record['process_memory']['peak_working_set'],
            wall_cap_seconds=record['wall_cap_seconds'],memory_cap_mb=record['memory_cap_mb']))
    result=dict(status='RECORDED',actual_model='gpt-6-astra',reasoning_effort='xhigh',
        phases=['preregistration','proof','implementation','exact small controls','independent verification','delivery'],
        preregistration_commit='ebd6e6d8',heavy_lease_requested=False,heavy_lease_acquired=False,
        heavy_jobs_run=0,resource_stops=0,runs=records,
        preserved_uncommitted_setup=['results/logs/b15_07_runtime_native_20260913.pid',
            'results/logs/b15_07_runtime_native_20260913_resources.json'],
        completion='Bounded operator assignment complete; no geometric production attempt.')
    (OUT/'run_summary.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    paths=sorted((ROOT/'analysis').glob('b15_07_*.py'))
    paths+=sorted((ROOT/'docs').glob('b15_07_*.md'))
    paths+=[ROOT/'results/PREREG_b15_07.md']
    hashes=[]
    for path in paths:
        raw=path.read_bytes(); assert len(raw)<5_000_000
        hashes.append(dict(path=str(path.relative_to(ROOT)).replace('\\','/'),bytes=len(raw),
            sha256_exact=hashlib.sha256(raw).hexdigest(),
            sha256_normalized_lf=hashlib.sha256(raw.replace(b'\r\n',b'\n')).hexdigest()))
    (OUT/'source_hashes.json').write_text(json.dumps(dict(status='RECORDED',files=hashes),indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(status='PASS',small_runs=len(records),
        total_wall_seconds=sum(r['wall_seconds'] for r in records),
        largest_aggregate_peak_bytes=max(r['aggregate_peak_committed_bytes'] for r in records))))


if __name__=='__main__':
    main()
