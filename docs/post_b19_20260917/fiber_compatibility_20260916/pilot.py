import hashlib
import importlib.util
import json
import time
from pathlib import Path

HERE=Path(__file__).resolve().parent
SRC=HERE.parent/'batch15_workers/B15-02/analysis/b18_02_carrier.py'
spec=importlib.util.spec_from_file_location('carrier',SRC)
c=importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
np=c.np
P=c.P
LAM=(4,2,2,2,2)
HEIGHTS=c.conjugate(LAM)
SLOTS=[(j,k) for j,h in enumerate(HEIGHTS) for k in range(h)]

def tensors(Y):
    unique={h:c.column_tensor(Y,h) for h in set(HEIGHTS)}
    return [unique[h] for h in HEIGHTS]

def plan(pi,rho):
    labs=[]
    for j,h in enumerate(HEIGHTS):
        labs.append([(ab,(j,k)) for k in range(h) for ab in ('a','b')])
    for ab,part in [('a',pi),('b',rho)]:
        labs += [[(ab,slot) for slot in block] for block in part]
    return c.Net.plan(labs)[1:]

def value(pair,ct):
    pi,rho=pair
    a,mi,fl=c.evaluate_pair(pi,rho,ct,None,None)
    b,mj,gl=c.evaluate_pair(rho,pi,ct,None,None)
    return (a+b)%P

def main():
    start=time.perf_counter()
    rng=np.random.default_rng(1609202602)
    s,g=c.s_and_g(LAM,3)
    assert s==2
    points=[rng.integers(0,P,size=(5,4,4)).astype(np.int64) for _ in range(2)]
    cols=[tensors(Y) for Y in points]
    basis=[]
    plain=[]
    attempted=[]
    for n in range(48):
        pi=c.random_block_partition(SLOTS,rng)
        rho=c.random_block_partition(SLOTS,rng)
        pa,pb=plan(pi,rho),plan(rho,pi)
        if max(pa[0],pb[0])>2**24 or max(pa[1],pb[1])>10**8:
            attempted.append({'attempt':n,'status':'plan_cap','plans':[pa,pb]})
            continue
        vs=[value((pi,rho),ct) for ct in cols]
        added=c.rank_mod(plain+[vs])>len(basis)
        attempted.append({'attempt':n,'values':vs,'added':added,'plans':[pa,pb]})
        if added:
            basis.append((pi,rho))
            plain.append(vs)
            print('basis',len(basis),'attempt',n,'elapsed',time.perf_counter()-start,flush=True)
        if len(basis)==s or time.perf_counter()-start>35:
            break
    rec={'d':3,'lambda':LAM,'a':0,'s':s,'g':g,'prime':P,
         'source_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),
         'points':[Y.tolist() for Y in points],'attempts':attempted,
         'basis':basis,'basis_values':plain,'basis_rank':c.rank_mod(plain)}
    dest=HERE/'pilot.json'
    dest.write_text(json.dumps(rec,indent=2)+'\n')
    if len(basis)!=s:
        rec['status']='NOT_REACHED_basis'
    else:
        del cols
        # The pair uses exactly five matrix labels, with two 2x2 blocks.
        Y=np.zeros((5,4,4),dtype=np.int64)
        Y[:,:2,:2]=rng.integers(-3,4,size=(5,2,2))%P
        Y[:,2:,2:]=rng.integers(-3,4,size=(5,2,2))%P
        Yt=Y.copy()
        Yt[:,:2,:2]=np.swapaxes(Y[:,:2,:2],1,2)
        v0=[value(pair,tensors(Y)) for pair in basis]
        v1=[value(pair,tensors(Yt)) for pair in basis]
        D=[(a-b)%P for a,b in zip(v0,v1)]
        rec.update(fiber_point=Y.tolist(),fiber_partner=Yt.tolist(),fiber_values=[v0,v1],difference=D)
        dest.write_text(json.dumps(rec,indent=2)+'\n')
        rows=[]
        samples=[]
        for Y in points:
            nodes=list(range(9))
            vals=[]
            for u in nodes:
                ct=tensors(c.adapted_scale_u(Y,u))
                vals.append([value(pair,ct) for pair in basis])
            coeff=[c.solve_vandermonde(nodes,[vs[i] for vs in vals],nodes) for i in range(s)]
            rows.extend([[coeff[i][j] for i in range(s)] for j in (7,8)])
            samples.append(vals)
        rec.update(u_nodes=list(range(9)),skew_samples=samples,forbidden_rows=rows,
                   arc_rank=c.rank_mod(rows),fiber_rank=c.rank_mod([D]),combined_rank=c.rank_mod(rows+[D]))
        rec['status']='ARC_FULL_no_increment_possible' if rec['arc_rank']==s else 'UNRESOLVED_sampled_arc_kernel'
    rec['elapsed_seconds']=time.perf_counter()-start
    dest.write_text(json.dumps(rec,indent=2)+'\n')
    print(json.dumps({k:v for k,v in rec.items() if k not in ('points','attempts','basis','fiber_point','fiber_partner','skew_samples')},indent=2))

if __name__=='__main__':
    main()
