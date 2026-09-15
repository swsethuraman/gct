"""Finalize local B16-04 evidence inventory; no Git or external writes."""
from pathlib import Path
import json,hashlib,time
from b16_04_filtration import HERE,OUT,dump

def main():
    closed=[]
    for path in sorted((HERE/'results/logs').glob('b16_04*_resources.json')):
        if path.name in ('b16_04_runtime_resources.json','b16_04_finalize_resources.json'): continue
        rec=json.loads(path.read_text())
        assert 'wall_seconds' in rec and 'exit_code' in rec
        assert rec['job_object_enforced'] and rec['memory_cap_mb']<=512 and rec['wall_cap_seconds']<=60
        closed.append({'path':str(path),'resource_receipt':rec})
    exit_receipt=json.loads((OUT/'process_exit.json').read_text(encoding='utf-8-sig'))
    assert not any(p['research_process_alive'] for p in exit_receipt['processes'])
    final=json.loads((HERE/'results/logs/b16_04_delivered_receiver_resources.json').read_text())
    receiver=json.loads((OUT/'receiver.json').read_text())
    assert receiver['status']=='PASS' and len(receiver['input_hash_checks'])==62
    summary={'status':'ALL_RESEARCH_PROCESSES_EXITED','heavy_lease_requested':False,'heavy_lease_held':False,
      'final_receiver_seconds':final['wall_seconds'],
      'final_receiver_peak_job_bytes':final['job_memory']['peak_job_memory'],
      'final_receiver_peak_working_set_bytes':final['process_memory']['peak_working_set'],
      'all_closed_control_wall_seconds':sum(x['resource_receipt']['wall_seconds'] for x in closed),
      'largest_closed_job_peak_bytes':max(x['resource_receipt']['job_memory']['peak_job_memory'] for x in closed),
      'closed_control_count':len(closed),'nonzero_debug_exit_count':sum(x['resource_receipt']['exit_code']!=0 for x in closed),
      'debug_failures':'FLINT coefficient string coercion; fmpz JSON serialization; fresh-versus-JSON key types; absent optional pyvenv.cfg. Each corrected; no mathematical failure suppressed.',
      'scope':'Includes all completed B16-04 research/preparatory controls, including debug failures. Excludes inherited launch smoke and this final filesystem-packaging run, whose separate wrapper receipt is results/logs/b16_04_finalize_resources.json.',
      'receipts':closed}
    dump('resource_summary.json',summary)
    delivery=HERE/'delivery/b16_04'; delivery.mkdir(parents=True,exist_ok=True)
    files=sorted(set(HERE.glob('analysis/b16_04*.py')) | set(HERE.glob('docs/b16_04*.md'))
                 | set(OUT.glob('*')) | {Path(x['path']) for x in closed})
    entries=[]
    for path in files:
        if not path.is_file(): continue
        entries.append({'path':str(path.relative_to(HERE)).replace('\\','/'),
                        'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    manifest={'slot':'04','status':'COMPLETE_LOCAL_FILESYSTEM_DELIVERY','worktree':str(HERE),
      'frozen_head_inherited':'3d3f9f8b427f257a0d5db678b1645212033652ff','new_git_operations':False,
      'generated_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
      'proof':'docs/b16_04_proof.md','report':'docs/b16_04_report.md',
      'receiver':'analysis/b16_04_verify.py','input_hashes':'results/b16_04/input_hashes.json',
      'exact_filtration_tail19':[4,7,9,10,11],'filtration_degrees':[23,24,25,26,27],
      'declared_ideal_dimensions':[1,4,4,11],'declared_gap_upper':[-30,-72,-72,-130],
      'files':entries}
    (delivery/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'status':manifest['status'],'files':len(entries),'final_receiver_seconds':summary['final_receiver_seconds'],
      'peak_job_MiB':summary['largest_closed_job_peak_bytes']/1024**2,
      'closed_control_seconds':summary['all_closed_control_wall_seconds']}))

if __name__=='__main__': main()
