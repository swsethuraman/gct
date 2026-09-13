"""Small delivery receipt preparation; never deletes caller artifacts."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/b15_10'


def write(path,data):
    if path.exists():
        raise ValueError('preserve existing receipt: '+str(path))
    path.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')


def main():
    p=argparse.ArgumentParser();p.add_argument('mode',choices=('corrupt','collect'))
    a=p.parse_args()
    if a.mode=='corrupt':
        cert=json.loads((OUT/'receiver_01/full_certificate.json').read_text(encoding='utf-8'))
        cert['determinant_points'][0]['pencil'][0][0][1]+=1
        write(OUT/'receiver_01/corrupted_point.json',cert)
        return
    names=['small_banked','direct_small','extension_small','full_small',
           'controls_small','receiver_small','corrupted_receiver_small']
    resources=[]
    for name in names:
        path=ROOT/f'results/logs/b15_10_{name}_resources.json'
        data=json.loads(path.read_text(encoding='utf-8'))
        expected=1 if name=='corrupted_receiver_small' else 0
        if data.get('exit_code')!=expected:
            raise ValueError('unexpected run exit code: '+name)
        resources.append(dict(name=name,path=str(path.relative_to(ROOT)).replace('\\','/'),
                              exit_code=data['exit_code'],wall_seconds=data['wall_seconds'],
                              peak_job_memory_bytes=data['job_memory']['peak_job_memory'],
                              peak_working_set_bytes=data['process_memory']['peak_working_set'],
                              cap_mb=data['memory_cap_mb'],cap_seconds=data['wall_cap_seconds']))
    write(OUT/'resource_summary.json',dict(status='EXACT',runs=resources,
          resource_decision='All research and receiver runs fit small controls: 60 seconds/512 MiB; no heavy numerical job or lease was needed.',
          setup_logs_preserved_separately=['results/logs/b15_10_runtime_native_20260913.pid',
                                          'results/logs/b15_10_runtime_native_20260913_resources.json']))
    inputs=['analysis/b14_12_cell.py','analysis/b14_12_families.py',
            'results/b14_12/b14_12.json','results/b15_prep/Q1_combined_bound.json',
            'results/b14_10/replacement_map.json','analysis/b14_10/recover.py',
            'results/b14_10/recovered/cubic8_7_5_5_2_2_1_1_1.json',
            'docs/batch15/ACCEPTED_STATE.md','results/integrate/inherited_exclusions.json',
            'results/b15_prep/transport_overlay.json',
            'analysis/b15_10_witness.py','analysis/b15_10_extend.py','analysis/b15_10_full.py']
    rows=[]
    for rel in inputs:
        data=(ROOT/rel).read_bytes()
        rows.append(dict(path=rel,bytes=len(data),sha256_exact_working_bytes=hashlib.sha256(data).hexdigest(),
                         sha256_utf8_lf=hashlib.sha256(data.replace(b'\r\n',b'\n')).hexdigest()))
    write(OUT/'input_hashes.json',dict(hash_convention='exact bytes plus UTF-8 text normalized CRLF to LF for checkout portability',inputs=rows))
    modules=['b15_10_witness.py','b15_10_extend.py','b15_10_full.py']
    for name in modules:
        if (ROOT/'analysis'/name).read_bytes()!=(OUT/'receiver_01'/name).read_bytes():
            raise ValueError('receiver module differs: '+name)
    if (OUT/'full_certificate.json').read_bytes()!=(OUT/'receiver_01/full_certificate.json').read_bytes():
        raise ValueError('receiver certificate differs')
    write(OUT/'receiver_manifest.json',dict(status='EXACT',
          portable_files=[dict(path='receiver_01/'+name,bytes=(OUT/'receiver_01'/name).stat().st_size,
                               sha256=hashlib.sha256((OUT/'receiver_01'/name).read_bytes()).hexdigest())
                          for name in modules+['full_certificate.json']],
          source_modules_equal=True,certificate_equal=True,receiver_process_fresh=True,
          corruption=dict(path='receiver_01/corrupted_point.json',mutation='A0[0,1] increased by 1',
                          expected_exit_code=1,observed_exit_code=1),
          cleanup='No directory removed; all caller outputs and receiver inputs retained.'))
    print(json.dumps(dict(status='EXACT',runs=len(resources),receiver_files=len(modules)+1)))


if __name__=='__main__':
    main()
