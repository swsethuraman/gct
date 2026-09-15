"""Bounded receiver and input capture for B16-10; no B15/shared writes."""
import argparse
from copy import deepcopy
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
import hashlib
import json
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parent))
import b16_10_jet as J

ROOT=Path(__file__).resolve().parents[1]
PROJECT=ROOT.parents[2]
OUT=ROOT/'results/b16_10'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path,value):
    J.need(not path.exists(),'preserve existing output '+str(path))
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,indent=2)+'\n')


def capture():
    project_names=[
      'Batch16/BOARD.md','Batch16/launch/INPUT_MANIFEST.json','Batch16/launch/B16-10.md',
      'Batch16/launch/dispatch_02.json','Batch16/launch/dispatch_10.json','Batch16/LEASES.json',
      'Batch15_Launch/native_20260913/INTAKE.json']
    dream='Batch15_Launch/native_20260913/reviews_filesystem/Dream_Upper288/'
    project_names += [dream+s for s in ['DREAM_REPORT.md','integrator_review.json',
                                      'tiny_controls.py','verify_cubic_and_lift.py']]
    hessian='Batch15_Launch/native_20260913/reviews_filesystem/Hessian11_1631/'
    project_names += [hessian+s for s in ['REPORT.md','integrator_review.json']]
    own_names=['analysis/b15_bound.py','analysis/b15_10_witness.py','docs/b15_10_report.md',
               'docs/b15_10_proved.md','results/logs/b16_10_runtime_resources.json']
    two=PROJECT/'work/batch15_workers/B15-02'
    other_names=['analysis/b16_02_census.py','results/b16_02/census.json',
                 'results/b16_02/receiver.json']
    # Final delivered proof and receiver are included if already present.
    other_names += [str(p.relative_to(two)) for base in ['docs','analysis','results/b16_02']
                    for p in (two/base).glob('b16_02*')
                    if p.is_file() and str(p.relative_to(two)) not in other_names]
    paths=[PROJECT/s for s in project_names]+[ROOT/s for s in own_names]+[two/s for s in other_names]
    entries=[]
    for index,path in enumerate(paths):
        data=path.read_bytes(); digest=hashlib.sha256(data).hexdigest()
        name=f'input_snapshots/{index:02d}_{path.name}'
        dst=OUT/name
        J.need(not dst.exists(),'preserve input snapshot')
        dst.parent.mkdir(parents=True,exist_ok=True); dst.write_bytes(data)
        entries.append({'original_path':str(path),'snapshot':name,'bytes':len(data),
                        'sha256':digest,'sha256_normalized_lf':hashlib.sha256(data.replace(b'\r\n',b'\n')).hexdigest()})
    write(OUT/'input_hashes.json',{'format':'b16-10-actual-inputs/1','hash_convention':'exact file bytes; normalized LF also recorded',
          'frozen_worktree_head_inherited':'9fd63fd543076d4cd42b5764c03039f0eff89934',
          'git_operations_performed':False,'entries':entries})
    return {'status':'PASS','captured_inputs':len(entries)}


def check_certificate(cert):
    J.need(cert['spec']==J.spec(),'exact source formula/arc specification')
    actual=J.calculate(cert['spec'])
    J.need(actual==cert['result'],'coefficient/minor mismatch')
    return actual


def controls(cert):
    # Independent signed permutation determinant checks the subset recurrence.
    A=[[{(0,0):Q(2+i+2*j),(1,0):Q(i-j),(0,1):Q(i*j+1)}
        for j in range(3)] for i in range(3)]
    brute={}
    for p in permutations(range(3)):
        sign=(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        brute=J.add(brute,J.scale(J.multiply_all([A[i][p[i]] for i in range(3)]),sign))
    J.need(J.det(A)==brute,'Leibniz determinant check')
    v={(0,0):Q(3),(0,1):Q(2),(0,2):Q(-5)}
    J.need(J.mul(v,J.inv(v))==J.const(1),'series inverse control')
    # Exact formal partials have disjoint support, proving essential rank ten.
    partials=[{tuple(k for k in m if k!=i) for m in J.MONS if i in m} for i in range(10)]
    J.need(all(partials) and all(not (partials[i]&partials[j]) for i in range(10) for j in range(i)),
           'independent ten-variable source partials')
    rejected=[]
    for name in ['source','point','coefficient','minor']:
        bad=deepcopy(cert)
        if name=='source': bad['spec']['source_order'][0]='X11'
        if name=='point': bad['spec']['base_matrix'][0][0]+=1
        if name=='coefficient': bad['result']['arcs'][0]['coefficient_rows']['25'][1][0]='0'
        if name=='minor': bad['result']['minors']['25']['determinant']='0'
        try: check_certificate(bad)
        except ValueError: rejected.append(name)
        else: raise ValueError('mutation was accepted: '+name)
    return {'determinant_leibniz':'PASS','truncated_inverse':'PASS',
            'ten_essential_partials_disjoint_support':'PASS','mutations_rejected':rejected}


def exclusion(inputs_dir):
    manifest=json.loads((inputs_dir/'input_hashes.json').read_text())
    for item in manifest['entries']:
        J.need(sha(inputs_dir/item['snapshot'])==item['sha256'],'input snapshot hash mismatch')
    supplemental=inputs_dir/'supplemental_input_hashes.json'
    if supplemental.exists():
        extra=json.loads(supplemental.read_text())
        for item in extra['entries']:
            J.need(sha(inputs_dir/item['snapshot'])==item['sha256'],'supplemental input hash mismatch')
            review=json.loads((inputs_dir/item['snapshot']).read_text())
            J.need(review['status']=='PASS_INDEPENDENT_INTEGRATOR_REVIEW' and
                   review['counts']==[189,294,294,429] and review['D_upper']==[-20,-65,-65,-130],
                   'accepted finite census review')
    census_entry=next(x for x in manifest['entries'] if x['original_path'].replace('\\','/').endswith('/B15-02/results/b16_02/census.json'))
    census=json.loads((inputs_dir/census_entry['snapshot']).read_text())
    receiver_entry=next(x for x in manifest['entries'] if x['original_path'].replace('\\','/').endswith('/B15-02/results/b16_02/receiver.json'))
    received=json.loads((inputs_dir/receiver_entry['snapshot']).read_text())
    J.need(received['status']=='PASS' and received['fresh_exact_counts']=={'15':189,'17':294,'19':429},
           'slot02 receiver dependency')
    expected=[(23,61,15,189,158,-20),(25,67,17,294,218,-65),
              (26,71,17,294,218,-65),(27,73,19,429,288,-130)]
    rows=[]
    for d,first,t,a,ceiling,upper in expected:
        given=next(x for x in census['rows'] if x['degree']==d)
        J.need(given['lambda']==[first,t]+[2]*8 and given['a']==a and
               given['source_ceiling']==ceiling and given['inherited_full_det_ideal_upper']==11,
               'finite cell/premise binding')
        J.need(11+ceiling-a==upper<0,'full-ideal exclusion arithmetic')
        h_exp,c_exp={23:(2,8),25:(1,8),26:(1,7),27:(0,8)}[d]
        J.need(d+2*h_exp+c_exp==35 and first+6*h_exp+4*c_exp==105
               and t+2*h_exp==19,'explicit finite ideal transport')
        rows.append({'d':d,'lambda':[first,t]+[2]*8,'a_inherited_slot02':a,
                     'padding_upper_inherited':ceiling,'det_ideal_upper_inherited':11,
                     'padding_ideal_lower':a-ceiling,'D_upper':upper,
                     'target_with_q_at_most_11':a-10,
                     'injective_ideal_multiplier':{'h=8*c*a2-3*a1^2':h_exp,'c':c_exp},
                     'coefficient_r_fresh':{23:1,25:2,26:2,27:3}[d]})
    return {'status':'NO_ASSIGNED_CELL_SURVIVES_UNDER_RECORDED_PREMISES','rows':rows,
            'count_production_replayed_here':False,
            'proof':'m_pad<=U, i_det<=11, m_det=a-i_det, hence D<=U+11-a<0.',
            'hypotheses':['Characteristic zero and repository highest-weight coordinate convention',
              'Slot02 exact finite counts and finite-hook proof','Accepted Dream Sub9 cubic source ceilings',
              'Accepted stable a429 and determinant rank floor418',
              'Multiplication by nonzero highest-weight ambient polynomials gives injective ideal transport']}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('mode',choices=['capture','verify'])
    p.add_argument('--inputs-dir',type=Path,default=OUT)
    p.add_argument('--certificate',type=Path,default=OUT/'jet_certificate.json')
    p.add_argument('--receipt',type=Path)
    a=p.parse_args(); start=time.monotonic()
    if a.mode=='capture': result=capture()
    else:
        cert=json.loads(a.certificate.read_text())
        result={'status':'PASS','jet':check_certificate(cert),'controls':controls(cert),
                'exclusion':exclusion(a.inputs_dir)}
    result['receiver_module']=str(Path(__file__).resolve())
    result['jet_module']=str(Path(J.__file__).resolve())
    result['receiver_seconds']=time.monotonic()-start
    if a.receipt: write(a.receipt,result)
    print(json.dumps({'status':result['status'],'seconds':result['receiver_seconds'],
                      'exclusion':result.get('exclusion'),'controls':result.get('controls')}),flush=True)


if __name__=='__main__': main()
