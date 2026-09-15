"""Owned-files-only B16-10 filesystem delivery; never runs Git."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/b16_10'
DELIVERY=ROOT/'delivery/b16_10'


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def save(p,value):
    assert not p.exists(), str(p)
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(value,indent=2)+'\n')


def copy(src,dst):
    assert src.is_file() and not dst.exists(),str(dst)
    dst.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(src,dst)
    assert digest(src)==digest(dst)


def build():
    assert not DELIVERY.exists(),'preserve existing delivery'
    review=ROOT.parents[2]/'Batch16/reviews/02/integrator_review.json'
    snapshot=OUT/'input_snapshots/24_slot02_integrator_review.json'
    copy(review,snapshot)
    save(OUT/'supplemental_input_hashes.json',{'entries':[{'original_path':str(review),
         'snapshot':str(snapshot.relative_to(OUT)).replace('\\','/'),'bytes':review.stat().st_size,
         'sha256':digest(review),'claim':'Independent integrator acceptance of inherited finite census'}]})
    for name in ['b16_10_jet.py','b16_10_receive.py','b16_10_package.py','b15_bound.py']:
        copy(ROOT/'analysis'/name,DELIVERY/'analysis'/name)
    for p in (ROOT/'docs').glob('b16_10*'):
        copy(p,DELIVERY/'docs'/p.name)
    for name in ['jet_certificate.json','input_hashes.json','supplemental_input_hashes.json','producer.json','jet_receiver.json',
                 'receiver.json','receiver_final.json']:
        copy(OUT/name,DELIVERY/'results'/name)
    for p in (OUT/'input_snapshots').iterdir():
        copy(p,DELIVERY/'results/input_snapshots'/p.name)
    readme='''# B16-10 bounded filesystem delivery

Read docs/b16_10_report.md and docs/b16_10_proof.md. The exact coefficient
receiver uses only the copied Python modules and copied input snapshots.
The finite census is an explicitly inherited input, with slot02 proof and
receiver receipt preserved. No Git binding or publication is claimed.

From the reused B15-10 worktree, use a fresh log/receipt name:

```powershell
& .venv/python.exe -B delivery/b16_10/analysis/b15_bound.py --slot 10 --name b16_10_portable_fresh --seconds 60 --memory-mb 512 delivery/b16_10/analysis/b16_10_receive.py verify --inputs-dir delivery/b16_10/results --certificate delivery/b16_10/results/jet_certificate.json --receipt results/b16_10/portable_fresh.json
```

The Windows wrapper enforces the Job Object and time caps. One process,
one configured numerical thread; standard library only. Portable here means
that no live B15/other-worker mathematical module is imported. A Windows
Python runtime and the inspected wrapper are still required for the caps.
SHA256_MANIFEST.json lists exact delivery bytes; input_hashes.json records
actual original paths, their hashes and the copied snapshot names.
'''
    (DELIVERY/'README.md').write_text(readme)
    return {'status':'PASS_BUILD','files':len(list(DELIVERY.rglob('*')))}


def seal():
    copied=json.loads((OUT/'portable_receiver.json').read_text())
    assert copied['status']=='PASS'
    assert Path(copied['jet_module']).resolve()==(DELIVERY/'analysis/b16_10_jet.py').resolve()
    assert Path(copied['receiver_module']).resolve()==(DELIVERY/'analysis/b16_10_receive.py').resolve()
    copy(OUT/'portable_receiver.json',DELIVERY/'results/portable_receiver.json')
    rows=[]
    for p in sorted((ROOT/'results/logs').glob('b16_10*_resources.json')):
        data=json.loads(p.read_text())
        # The current sealing wrapper has not exited yet; its receipt remains
        # outside the sealed manifest and is not misrepresented as complete.
        if 'wall_seconds' not in data: continue
        copy(p,DELIVERY/'resources'/p.name)
        rows.append({'name':p.name,'pid':data['pid'],'exit_code':data['exit_code'],
                     'wall_seconds':data['wall_seconds'],
                     'peak_working_set':data['process_memory']['peak_working_set'],
                     'peak_job_memory':data['job_memory']['peak_job_memory'],
                     'wall_cap_seconds':data['wall_cap_seconds'],
                     'memory_cap_mb':data['memory_cap_mb'],
                     'job_object_enforced':data['job_object_enforced'],
                     'origin':'inherited launch smoke' if p.name=='b16_10_runtime_resources.json' else 'fresh B16-10'})
    summary={'status':'PASS','heavy_lease':'never requested or held',
             'heavy_jobs':0,'rows':rows,'git_operations':0,
             'current_seal_wrapper_receipt':'results/logs/b16_10_seal_01_resources.json; complete after manifest creation'}
    save(OUT/'resource_summary.json',summary)
    save(DELIVERY/'results/resource_summary.json',summary)
    files=[{'path':str(p.relative_to(DELIVERY)).replace('\\','/'),
            'bytes':p.stat().st_size,'sha256':digest(p)}
           for p in sorted(DELIVERY.rglob('*')) if p.is_file()]
    save(DELIVERY/'SHA256_MANIFEST.json',{'format':'b16-10-filesystem-delivery/1','files':files,
         'frozen_worktree_head_inherited':'9fd63fd543076d4cd42b5764c03039f0eff89934',
         'fresh_git_binding':False,'no_shared_merged_base_claimed':True})
    return {'status':'PASS_SEALED','manifest_sha256':digest(DELIVERY/'SHA256_MANIFEST.json'),
            'files':len(files),'bytes':sum(x['bytes'] for x in files),
            'portable_receiver':'PASS from copied modules','heavy_lease':'none; no heavy process'}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['build','seal']);a=p.parse_args()
    result=globals()[a.mode]()
    save(OUT/f'package_{a.mode}.json',result)
    print(json.dumps(result),flush=True)
