"""Independent border-strip character formulation and full-support S7 control.

No retained character/evaluator module is imported. This is a same-task
independent arithmetic formulation, not an external integrator review.
"""
from functools import lru_cache
from fractions import Fraction as Q
from pathlib import Path
import gzip
import hashlib
import json
import importlib.util
import os
import time

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('local_tiny_controls',HERE/'tiny_controls.py')
T=importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)

def deadline():
    if time.monotonic()+2 > float(os.environ['CI73_DEADLINE']):
        raise RuntimeError('Verification incomplete; approaching cap')

@lru_cache(maxsize=None)
def removals(lam,k):
    """Enumerate Young subdiagrams; test connected skew shape with no 2x2.

    This deliberately does not use beta numbers or retained rim-hook code.
    """
    output=[]
    def visit(prefix,remaining):
        i=len(prefix)
        if i==len(lam):
            if remaining: return
            cells={(r,c) for r in range(len(lam)) for c in range(prefix[r],lam[r])}
            if len(cells)!=k: return
            if any((r+1,c) in cells and (r,c+1) in cells and (r+1,c+1) in cells for r,c in cells): return
            todo=[next(iter(cells))]; seen=set(todo)
            while todo:
                r,c=todo.pop()
                for v in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                    if v in cells and v not in seen: seen.add(v);todo.append(v)
            if seen!=cells:return
            height=len({r for r,c in cells})-1
            output.append((tuple(x for x in prefix if x),(-1)**height))
            return
        cap=min(lam[i],prefix[-1] if prefix else lam[i],remaining)
        for a in range(cap,-1,-1):
            rem=remaining-a
            if rem>sum(min(a,v) for v in lam[i+1:]): continue
            visit(prefix+(a,),rem)
    visit((),sum(lam)-k)
    return tuple(output)

@lru_cache(maxsize=None)
def character(lam,rho):
    if not rho:return int(not lam)
    return sum(sign*character(mu,rho[1:]) for mu,sign in removals(lam,rho[0]))

def main():
    start=time.monotonic()
    saved=json.loads((HERE/'cubic_bound.json').read_text())
    rows=[]; hashes={}
    for b in range(2,20):
        deadline()
        path=HERE/f'cubic_tail_{b}.json.gz'
        hashes[path.name]=hashlib.sha256(path.read_bytes()).hexdigest()
        cert=json.loads(gzip.decompress(path.read_bytes()))
        lam=tuple(cert['row']['tail'])
        total=Q(0)
        for rho,num,den,oldchar in cert['power_sum_numerator_denominator_character_rows']:
            c=character(lam,tuple(rho))
            assert c==oldchar,(lam,rho,c,oldchar)
            total+=Q(num,den)*c
            if character.cache_info().currsize>100000:character.cache_clear()
        assert total==cert['row']['stable_cubic_upper']
        rows.append({'b':b,'value':int(total),'characters_checked':cert['row']['terms']})
        character.cache_clear()
    # Explicit interlacing enumeration, without assuming the 18-channel formula.
    strips={}
    for d,t in ((23,15),(25,17),(27,19),(35,19)):
        lam=(4*d-t-16,t)+(2,)*8
        channels=[]
        def walk(mu):
            i=len(mu)
            if i==10:
                if sum(mu)==3*d and not mu[-1]:channels.append(tuple(x for x in mu if x))
                return
            lo=lam[i+1] if i<9 else 0
            for v in range(lo,lam[i]+1):
                if sum(mu)+v>3*d:break
                walk(mu+(v,))
        walk(())
        expected=[(3*d-14-b,b)+(2,)*7 for b in range(2,t+1)]
        assert sorted(channels)==sorted(expected)
        strips[f'{d},{t}']={'channels':channels,'source_upper':sum(r['value'] for r in rows if r['b']<=t)}
    # Complete invertible 10-variable extension of the previous polynomial line.
    a=[1,1,0,0,0,1,0,0,0,1]
    b=[2,1,2,1,3,1,2,2,1,4]
    cols=[a,b]+[[int(i==j) for i in range(10)] for j in range(2,10)]
    L=list(map(list,zip(*cols)))
    assert T.det(L)==-1
    old=json.loads((HERE/'tiny_evidence.json').read_text())
    rawD=list(map(Q,old['line_control']['det_Hess_P_coefficients']))
    rawP=T.mul([2,1],list(map(Q,old['line_control']['C_coefficients'])))
    assert rawP[-1]==1 and rawP[-2]==8
    def shift(poly,s):
        out=[Q(0)]; power=[Q(1)]
        for c in poly:
            out=T.add(out,[c*v for v in power]); power=T.mul(power,[s,1])
        return out
    depressedP=shift(rawP,-2)
    depressedD=shift(rawD,-2)
    assert depressedP[-2]==0
    S=T.remainder(depressedD,T.mul(depressedP,depressedP))
    S+= [Q(0)]*(8-len(S))
    assert S[7]==8918784
    # The quartic shear in all x directions has determinant one, not just on e.
    source_grad_at_a=[1,1,0,0,0,1,0,0,0,1]
    cubic_coeff=[sum(source_grad_at_a[i]*col[i] for i in range(10)) for col in cols[1:]]
    assert cubic_coeff[0]==8
    s2,s3,s4=depressedP[2],depressedP[1],depressedP[0]
    common_relation=S[3]-s2*S[5]-s3*S[6]-(s4-s2*s2)*S[7]
    assert common_relation==0
    output={'status':'PASS_BORDER_STRIP_CHARACTERS_AND_S7_LIFT',
            'character_formulation':'literal connected Young-skew cells, no 2x2; independent of beta-number code',
            'power_sum_coefficients':'inherited from cubic_bound.py; direct low-weight controls there, not independently regenerated here',
            'rows':rows,'channels':strips,'certificate_hashes':hashes,
            'degree23_padding_witness':{'source_order':'z then X row-major','target_order':'t,x1,...,x9',
                'L':L,'det_L':-1,'leading_coefficient':1,'cubic_t_coefficient_linear_form':cubic_coeff,
                'depression':'t -> t - a1(x)/4','depressed_P_at_e':list(map(T.integer,depressedP)),
                'S_at_e':list(map(T.integer,S)),
                'c23_S7':8918784,'coefficient_degree':23,'weight':[61,15]+[2]*8,
                'claim':'One nonzero padding restriction of the inherited degree23 determinant equation; no positive multiplicity gap.'},
            'common_padding_relation_value':T.integer(common_relation),
            'wall_seconds':time.monotonic()-start}
    (HERE/'independent_checks.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'status':output['status'],'source_bounds':{k:v['source_upper'] for k,v in strips.items()},
                      'degree23_c23_S7':8918784,'seconds':output['wall_seconds']}),flush=True)

if __name__=='__main__':main()
