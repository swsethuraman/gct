"""One cheap falsification gate; never interpret a sampled zero as an equation."""
import hashlib
import importlib.util
import json
import time
from pathlib import Path

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'batch15_workers/B15-06/analysis/b18_06_sweep.py'
spec=importlib.util.spec_from_file_location('saved_sweep',SOURCE)
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

def main():
    t=time.perf_counter()
    lam=(12,8,2,1,1)
    rec={'degree':6,'lambda':lam,'ambient_inherited':1,'source_inherited':24,
         'source_path':str(SOURCE),'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest()}
    K=len(m.weight_basis(lam,6))
    rec['weight_space_dimension']=K
    print('weight-space dimension',K,flush=True)
    if K>10000:
        rec['status']='STOP_support_cap'
    else:
        W,base,ops,dims,K=m.exact_hwv(lam,6,record=rec)
        if W is None:
            rec['status']='STOP_no_exact_hwv'
        else:
            rec['raising_operators']=[dict(target_dimension=dims[('mid',i+1,i)],
                nonzeros=len(ops[('down',i+1,i)][0])) for i in range(4)]
            assert all(x['target_dimension'] and x['nonzeros'] for x in rec['raising_operators'])
            assert not any(any(r) for r in m.raising_residues(lam,W,ops,dims))
            corrupt=list(W)
            corrupt[next(i for i,x in enumerate(W) if x)]+=1
            rec['corruption_rejected']=any(any(r) for r in m.raising_residues(lam,corrupt,ops,dims))
            assert rec['corruption_rejected']
            point,f=m.det_point(m.np.random.default_rng(16092026))
            rec['determinant_point']=point
            rec['determinant_value']=m.evaluate_exact(W,base,f)
            rec['status']='STOP_no_equation_in_cell' if rec['determinant_value'] else 'SAMPLED_ZERO_only'
            # Store the actual finite polynomial, rather than only a regeneration recipe.
            rec['coefficient_polynomial']=[{'coefficient':w,'factors':[m.MONS[i] for i in mono]}
                for w,mono in zip(W,base) if w]
    rec['elapsed_seconds']=time.perf_counter()-t
    HERE.joinpath('five_row_pilot.json').write_text(json.dumps(rec,indent=2)+'\n')
    print(json.dumps({k:v for k,v in rec.items() if k not in ('coefficient_polynomial','determinant_point')},indent=2))

if __name__=='__main__':
    main()
