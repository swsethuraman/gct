"""Replay standalone integer HWV polynomials and explicit determinant points."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools/verify'))
from hwv import check_vector_shape,is_highest_weight,evaluate
from points import form_of_point
from flint import fmpq_mat,fmpz_mat

OUT=ROOT/'results/b15_02'


def save(path,data,compact=False):
    path.write_text(json.dumps(data,indent=None if compact else 2,allow_nan=False)+'\n',encoding='utf-8')


def export(i):
    from wk9_s45_build import monomials_array,orbit_setup_arr
    from wk8_s30_core import exps
    tag=f'cell_{i:02d}'
    source=json.loads((OUT/f'{tag}_integral_source.json').read_text())
    verified=json.loads((OUT/f'{tag}_verified.json').read_text())
    c=source['cell'];lam=tuple(c['lam']);r=len(lam);d=c['delta']
    M=monomials_array(4,r,d,lam)
    arr=orbit_setup_arr(4,r,d,lam,M=M,verbose=False)
    Z=source['chi_coordinates'];terms=[]
    for k,row in enumerate(M):
        col=int(arr['col_of'][k])
        if col<0:continue
        v=Z[col]*int(arr['sgn'][k])
        if v:terms.append([row.tolist(),v])
    payload=dict(format='b15-02-integer-hwv/1',cell=c,
                 coefficient_convention='c_alpha is the ordinary coefficient of s^alpha',
                 exponent_letters=exps(4,r),
                 polynomial='sum_[indices,v] v*product_j c_(exponent_letters[indices[j]])',
                 indexed_terms=terms,
                 determinant_witnesses=verified['det_evaluations'])
    save(OUT/f'{tag}_polynomial.json',payload,compact=True)


def replay(i):
    t=time.perf_counter();path=OUT/f'cell_{i:02d}_polynomial.json'
    data=json.loads(path.read_text());c=data['cell'];r=c['working_variables']
    A=[tuple(a) for a in data['exponent_letters']]
    assert len(A)==len(set(A))
    assert all(len(a)==r and sum(a)==4 and all(type(x)is int and x>=0 for x in a) for a in A)
    vec=[]
    for indices,v in data['indexed_terms']:
        assert type(v)is int and v and all(type(k)is int and 0<=k<len(A) for k in indices)
        vec.append((tuple(A[k] for k in indices),v))
    check_vector_shape(vec,4,r,c['delta'],c['lam'])
    assert is_highest_weight(vec,r)[0]
    # Literal coefficient mutation of the complete polynomial is rejected.
    bad=list(vec);alphas,v=bad[0];bad[0]=(alphas,v+1)
    assert not is_highest_weight(bad,r)[0]
    values=[]
    for witness in data['determinant_witnesses']:
        co=form_of_point(witness['point'],r,4)
        value=evaluate(vec,co)
        assert value==int(witness['exact_integer_value']) and value!=0
        values.append(str(value))
    return dict(cell=c,status='EXACT',terms=len(vec),integer_values=values,
                full_HWV_check=True,changed_coefficient_rejected=True,
                fresh_polynomial_evaluation=True,seconds=time.perf_counter()-t,
                source_sha256=hashlib.sha256(path.read_bytes().replace(b'\r\n',b'\n')).hexdigest())


def orbit_frame():
    records=[json.loads((OUT/f'cell_{i:02d}_polynomial.json').read_text()) for i in range(1,10)]
    pencils=[x['determinant_witnesses'][0]['point']['pencil'] for x in records]
    assert all(p==pencils[0] for p in pencils)
    A=[[x for row in mat for x in row] for mat in pencils[0]]
    assert fmpq_mat(A).rank()==7
    added=[]
    for j in range(16):
        e=[int(i==j) for i in range(16)]
        if fmpq_mat(A+[e]).rank()>len(A):A.append(e);added.append(j)
        if len(A)==16:break
    det=int(fmpz_mat(A).det());assert det
    result=dict(status='EXACT',initial_frame_rank=7,completed_frame_rank=16,
                ambient_variables=16,flattening='row-major 4x4 entries; one row per variable',
                completed_integer_frame=A,added_standard_basis_indices=added,determinant=str(det),
                consequence='Invertible integer linear substitution of det4; each seven-variable coefficient used by the HWV is unchanged. Witness lies on the orbit, hence its closure.')
    save(OUT/'det_orbit_frame.json',result)
    return result


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--export',action='store_true');args=ap.parse_args()
    records=[]
    for i in range(1,10):
        if args.export:export(i)
        record=replay(i);records.append(record)
        print(json.dumps(dict(index=i,status=record['status'],seconds=record['seconds'])),flush=True)
    frame=orbit_frame()
    save(OUT/'standalone_replay.json',dict(status='EXACT',all_pass=True,cells=records,
                                          frame_determinant=frame['determinant'],model='gpt-6-astra'))
    if args.export:
        paths=set()
        for mod in list(sys.modules.values()):
            path=getattr(mod,'__file__',None)
            if path:
                p=Path(path).resolve()
                if p.suffix=='.py' and p.is_relative_to(ROOT) and not p.is_relative_to(ROOT/'.venv'):
                    paths.add(p)
        paths.update(ROOT/p for p in ['analysis/b15_02_probe.py','analysis/b15_02_verify.py','analysis/b15_bound.py',
                                     'results/b15_prep/candidate_preflight.json','results/b14_11/shortlist.json',
                                     'tools/integrate/exclusion_predicates.py','results/integrate/inherited_exclusions.json',
                                     'results/b15_prep/transport_overlay.json','analysis/b14_11_sizes.py'])
        save(OUT/'input_hashes.json',dict(convention='SHA-256; CRLF normalized to LF; all other bytes unchanged',
             files={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes().replace(b'\r\n',b'\n')).hexdigest() for p in sorted(paths)}))


if __name__=='__main__':main()
