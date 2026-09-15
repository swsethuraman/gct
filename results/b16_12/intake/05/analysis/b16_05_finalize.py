"""Write the scoped local delivery manifest; run through b15_bound.py."""
import json
import time
from pathlib import Path
from b16_05_receiver import HERE, ROOT, OUT, digest, inputs, read, save, modules


def main():
    modules()
    actual=inputs()
    control=read('control.json')
    proof=read('proof_arithmetic.json')
    assert actual==control['input_hashes']==proof['input_hashes']
    assert read('replay.json')['status']=='PASS'
    assert all(control['families'][f]['residual_minor']['rank_lb']==0 for f in ['SPLIT','PAD'])
    assert all(proof['five_space_restriction'][f]['exact_restriction_rank']==4 for f in ['SPLIT','PAD'])
    names=['preflight','control','replay','proof','five_space','receive_projection','receive_proof','essential']
    resources=[]
    for name in names:
        path=HERE/f'results/logs/b16_05_{name}_resources.json'
        r=json.loads(path.read_text())
        assert r['exit_code']==0 and r['job_object_enforced']
        assert r['workers']==r['blas_threads']==1
        assert r['memory_cap_mb']<=512 and r['wall_cap_seconds']<=60
        resources.append({'run':name,**r})
    release=read('lease_release.json')
    assert release['heavy_lease_held'] is False
    assert set(release['checked_pids'])==set(r['pid'] for r in resources)
    assert not release['active_pids']
    claims={
        'full_cell':{'degree':35,'weight':[105,19]+[2]*8,
                     'ambient429':'inherited','determinant418':'inherited',
                     'padding_interval':[243,288],'stable_gap_interval':[-175,-130]},
        'fresh_formal_shared_relations':4,
        'fresh_nonzero_shared_equation':{'name':'E3','value':348671260102848768,
                                        'finite_degree':27,'finite_weight':[73,19]+[2]*8},
        'five_space':{'basis':['S3','s2*S5','s3*S6','s4*S7','s2^2*S7'],
                      'ambient_dimension':5,'ambient_dimension_status':'inherited accepted',
                      'split_restriction_rank':4,'padding_restriction_rank':4,
                      'kernel':[1,-1,-1,-1,1],
                      'status':'exact; global relation plus fresh modular nonzero minors'},
        'full_space_control':{'points_each':4,'prime':2147483647,
                              'split_residual_rank':0,'padding_residual_rank':0,
                              'status':'sample observations only; no full exact243 claim'},
        'new_full_padding_rank_floor':None,'positive_gap':False,
        'next_sufficient_witness':'Exact split-image upper243 with global kernel proof, or a genuine padding minor244; positivity elsewhere needs one finite q+r>a.'}
    save('summary.json',{'status':'COMPLETE_SCOPED_SMALL_RESEARCH','claims':claims,
                         'resources':resources,'resource_release':release,
                         'hypotheses':['Characteristic zero','Accepted S57/ambient inheritance and degree35 basis',
                                       'Accepted Hessian11 five-space and finite pole-clearing',
                                       'Accepted Dream split-source upper288 and B15-06 floor243'],
                         'limitations':['No exact full split/padding image243','No full186-dimensional global residual kernel',
                                        'No complete eleven-space restriction computation','No finite positive gap',
                                        'No new Git binding or commit'],
                         'input_hashes':actual})
    output_paths=[HERE/'analysis/b16_05_receiver.py',HERE/'analysis/b16_05_proof.py',
                  HERE/'analysis/b16_05_finalize.py',HERE/'docs/b16_05_report.md',
                  HERE/'docs/b16_05_proof.md',HERE/'delivery/b16_05/RECEIVE.ps1']
    output_paths+=sorted(OUT.glob('*.json'))
    output_paths+=[HERE/f'results/logs/b16_05_{name}_resources.json' for name in names]
    outputs=[digest(p) for p in output_paths]
    manifest={'status':'LOCAL_DELIVERY_COMPLETE','slot':'05',
              'created_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
              'worktree':str(HERE),'claims':claims,'input_hashes':actual,
              'frozen_manifest_checks':read('preflight.json')['frozen_input_checks'],
              'outputs':outputs,'receiver':'delivery/b16_05/RECEIVE.ps1',
              'no_git_operations':True,'no_heavy_lease':True,
              'direct_integrator_notification':'Rejected by automatic approval review; local delivery only. No retry or workaround.',
              'frozen_head_inherited':'5a019b2fb24fecf208118e628772b373235a6d61'}
    target=HERE/'delivery/b16_05/MANIFEST.json'
    target.write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'status':manifest['status'],'outputs':len(outputs),'input_hashes':len(actual)}))


if __name__=='__main__':main()
