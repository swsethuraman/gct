"""Dimension-explicit extension of banked B14-06 Claude Opus 5 code.

The B14-06 evaluator, Jet algebra, determinant and normalization helpers are
reused with original attribution. This adapter owns all point dimensions.
"""
import argparse
from pathlib import Path
from math import factorial
import json
import gzip
import itertools
import time
import numpy as np
import flint
from b14_06_bracket import (BracketEvaluator as BankedEvaluator, Jet,
    enumerate_brackets, jet_point_list, random_point, consistency_defect,
    det_mod, rank_mod, brute_value, PRIMES, _fl)
from b14_06_points import normalise_depress, _principal_minors, _det_jet, _per3

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/b15_06'


def save(name,data):
    raw=(json.dumps(data,sort_keys=True,separators=(',',':'))+'\n').encode()
    if name.endswith('.gz'):
        raw=gzip.compress(raw,mtime=0)
    OUT.mkdir(exist_ok=True)
    (OUT/name).write_bytes(raw)


class Evaluator(BankedEvaluator):
    def __init__(self,brackets,col,p,seed=20260913):
        brackets=[tuple(tuple(group) for group in bracket) for bracket in brackets]
        if not brackets or col<2:
            raise ValueError('nonempty brackets and col>=2 required')
        for a,b,c,z in brackets:
            if any(len(group)!=3 for group in (a,b,c,z)):
                raise ValueError('three letter degrees required')
            if any(x<0 for group in (a,b,c,z) for x in group):
                raise ValueError('negative bracket count')
            if sum(a)+sum(c)!=col or sum(b)+sum(c)!=col:
                raise ValueError('bracket column dimension mismatch')
        super().__init__(brackets,col,p,seed)
        self.fact=[factorial(k) for k in range(col+1)]

    def values(self,red):
        for d in (2,3,4):
            s,u,N=red[d]
            if len(u)!=self.col or len(N)!=self.col or any(len(row)!=self.col for row in N):
                raise ValueError('point dimension mismatch')
        return super().values(red)


def linear_jet(coeff,J,s0):
    if coeff.shape!=(J.n+1,J.npts):
        raise ValueError('linear form dimension mismatch')
    z=J.zero()
    z[0]=(coeff[0]*s0+coeff[1])%J.p
    z[1:1+J.n]=coeff[1:]%J.p
    return z


def determinant(r,p,A,shift=None,quartic=False):
    if A.shape[:3]!=(r-1,4,4) or A.ndim!=4:
        raise ValueError('pencil dimension mismatch')
    if np.any(np.trace(A,axis1=1,axis2=2)):
        raise ValueError('pencil must be traceless')
    J=Jet(r-1,p,A.shape[-1])
    matrices=[]
    for s0 in (range(5) if quartic else [0]):
        M=[[None]*4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                z=J.zero();z[0]=A[0,i,j]%p;z[1:1+J.n]=A[:,i,j]%p
                if i==j and quartic:
                    z[0]=(z[0]+s0)%p
                    if shift is not None:
                        z[0]=(z[0]+shift[0])%p
                        z[1:1+J.n]=(z[1:1+J.n]+shift)%p
                M[i][j]=z
        matrices.append(M)
    if quartic:
        jets,c,defect,valid=normalise_depress([_det_jet(M,J,p) for M in matrices],list(range(5)),p,J)
        assert defect==0 and np.all(valid) and np.all(c==1)
    else:
        jets={d:_principal_minors(matrices[0],J,p,d) for d in (2,3,4)}
    return J,jets


def product_point(r,p,L,padded=True):
    if L.ndim!=3 or L.shape[:2]!=((10 if padded else 4),r):
        raise ValueError('point linear forms have wrong dimension')
    J=Jet(r-1,p,L.shape[-1])
    values=[]
    for s0 in range(5):
        ls=[linear_jet(L[i],J,s0) for i in range(len(L))]
        if padded:
            per=_per3([[ls[1+3*i+j] for j in range(3)] for i in range(3)],J,p)
            value=J.mul(ls[0],per)
        else:
            value=J.mul(J.mul(ls[0],ls[1]),J.mul(ls[2],ls[3]))
        values.append(value)
    jets,c,defect,valid=normalise_depress(values,list(range(5)),p,J)
    assert defect==0
    return J,jets,c,valid


def generate(family,r,p,npts,seed):
    rng=np.random.default_rng(seed)
    if family=='GEN':
        reds=[random_point(r-1,p,rng) for _ in range(npts)]
        native={'kind':'symmetric_N_triples','points':reds,
                'rational_lift':'N integral; symmetric tensor entries T_ij0...0=N_ij, unused entries zero'}
    elif family=='DET':
        A=rng.integers(-12,13,(r-1,4,4,npts),dtype=np.int64)
        A[:,3,3]=-(A[:,0,0]+A[:,1,1]+A[:,2,2])
        J,jets=determinant(r,p,A)
        reds=jet_point_list(J,jets)
        native={'kind':'traceless_integer_pencils','A':A.tolist()}
    elif family in ('PAD','NEG'):
        L=rng.integers(-12,13,(10 if family=='PAD' else 4,r,npts),dtype=np.int64)
        J,jets,c,valid=product_point(r,p,L,family=='PAD')
        reds=[red for red,ok in zip(jet_point_list(J,jets),valid) if ok]
        native={'kind':'integer_linear_forms','L':L.tolist(),'c':c.tolist(),
                'valid':valid.tolist(),'entry_order':'padding then permanent row-major' if family=='PAD' else 'four factors'}
    else:
        raise ValueError('unknown family')
    assert reds and all(consistency_defect(red,r-1,p)==0 for red in reds)
    return reds,native


def require_rejected(fn):
    try:
        fn()
    except (ValueError,AssertionError):
        return True
    raise AssertionError('altered input accepted')


def covariance(ev,red,W):
    col,p=ev.col,ev.p
    # Unit upper triangular g fixes e_0; exact object arithmetic prevents overflow.
    g=np.eye(col,dtype=object);g[0,1]=3;g[1,2]=2
    g[:,1]*=3
    image={}
    for d,(s,u,N) in red.items():
        uu=g.T@np.array(u,dtype=object)
        NN=g.T@np.array(N,dtype=object)@g
        image[d]=(s,[int(v%p) for v in uu],[[int(v%p) for v in row] for row in NN])
    v=ev.values(red);w=ev.values(image)
    assert any(v) and w==[x*9%p for x in v] and w!=v
    ts=list(range(2,col+2));image={}
    for d,(s,u,N) in red.items():
        image[d]=(s*pow(ts[0],d,p)%p,
                  [u[i]*pow(ts[0],d-1,p)*ts[i]%p for i in range(col)],
                  [[N[i][j]*pow(ts[0],d-2,p)*ts[i]*ts[j]%p for j in range(col)] for i in range(col)])
    fac=pow(ts[0],W-2*col,p)
    for x in ts:fac=fac*x*x%p
    assert ev.values(image)==[x*fac%p for x in v]
    assert ev.values(image)!=[x*fac*ts[0]%p for x in v]


def controls():
    checks=[];native=[]
    for p in PRIMES:
        rng=np.random.default_rng(150606)
        bs=enumerate_brackets(13,3)
        ev=Evaluator(bs,3,p)
        red=random_point(3,p,rng)
        vals=[brute_value(b,red,3,p) for b in bs]
        assert ev.values(red)==vals
        ev.fact=[1]*4
        assert ev.values(red)!=vals
        ev=Evaluator(bs,3,p)
        signed=[(-v if sum(b[0])%2 else v)%p for b,v in zip(bs,vals)]
        assert signed!=vals
        require_rejected(lambda:Evaluator([],3,p))
        for r in range(7,11):
            reds,src=generate('DET',r,p,2,150600+r)
            A=np.array(src['A'],dtype=np.int64)
            shift=rng.integers(-3,4,(r-1,2),dtype=np.int64)
            J,js=determinant(r,p,A,shift=shift,quartic=True)
            assert jet_point_list(J,js)==reds
            altered=A.copy();altered[0,0,1]+=1
            assert jet_point_list(*determinant(r,p,altered))!=reds
            peak=Evaluator(enumerate_brackets(2*(r-1),r-1),r-1,p)
            assert len(peak.brackets)==1
            val=peak.values(reds[0])[0]
            assert val==factorial(r-1)*det_mod(reds[0][2][2],p)%p and val
            neg,negsrc=generate('NEG',r,p,2,100+r)
            assert all(peak.values(x)==[0] for x in neg)
            gen,gsrc=generate('GEN',r,p,1,300+r)
            W=2*(r-1)+3
            covariance(Evaluator(enumerate_brackets(W,r-1),r-1,p),gen[0],W)
            broken={d:(s,list(u),[list(row) for row in N]) for d,(s,u,N) in gen[0].items()}
            broken[2][1][0]+=1
            assert consistency_defect(broken,r-1,p)>0
            require_rejected(lambda:Evaluator(enumerate_brackets(W,r-1),r-1,p).values(red))
            pad,psrc=generate('PAD',r,p,2,900+r)
            if r==10:
                L=np.array(psrc['L'],dtype=np.int64)
                for k in range(2):
                    mat=L[:,:,k].tolist()
                    det=int(flint.fmpz_mat(mat).det())
                    assert det and det%p
                    # Independent scalar permanent evaluates coefficient c=F(e_0).
                    v=L[:,0,k].tolist()
                    c=v[0]*sum(v[1+s[0]]*v[4+s[1]]*v[7+s[2]] for s in itertools.permutations(range(3)))
                    assert c%p==psrc['c'][k]
                    # Exact full-support derivative rank of z*per3: 10 independent
                    # monomial-support vectors; invertible L preserves that rank.
                    derivatives=[{} for _ in range(10)]
                    for perm in itertools.permutations(range(3)):
                        mon=[0]*10;mon[0]=1
                        for i in range(3):mon[1+3*i+perm[i]]=1
                        for i in range(10):
                            if mon[i]:
                                dmon=mon.copy();dmon[i]-=1
                                key=tuple(dmon);derivatives[i][key]=derivatives[i].get(key,0)+1
                    mons=sorted(set().union(*(set(d) for d in derivatives)))
                    assert flint.fmpq_mat([[d.get(m,0) for m in mons] for d in derivatives]).rank()==10
            native.append({'r':r,'prime':p,'DET':src,'shift':shift.tolist(),'PAD':psrc,'NEG':negsrc,'GEN':gsrc})
            checks.append({'r':r,'prime':p,'peaked_value':val,'det_normalization':True,
                           'point_mutation_detected':True,'Euler_mutation_detected':True,
                           'covariance_and_weight':True,'negative_four_factors':True,
                           'full_padding_rank':10 if r==10 else None})
    save('extension_controls_native.json.gz',native)
    save('extension_controls.json',{'status':'EXACT','checks':checks,
        'brute_col':3,'brute_brackets':len(bs),'sign_and_factorial_defects_detected':True,
        'dimension_and_empty_inputs_rejected':True,'numpy':np.__version__,'flint':flint.__version__})
    print('EXTENSION CONTROLS PASS',len(checks),flush=True)


def minor_certificate(values,p):
    """Return a nonzero square minor, allowing a legitimate rank-zero matrix."""
    if not values or not values[0]:
        raise ValueError('empty evaluation matrix')
    M=_fl(values,p)
    R,rank=M.rref()
    cols=[]
    for i in range(rank):
        cols.append(next(j for j in range(M.ncols()) if R[i,j]))
    if not rank:
        return {'rank_lb':0,'rows':[],'columns':[],'determinant_mod_p':1}
    reduced=_fl([[row[j] for j in cols] for row in values],p)
    TR,rr=reduced.transpose().rref()
    rows=[next(j for j in range(TR.ncols()) if TR[i,j]) for i in range(rr)]
    assert rr==rank
    determinant=det_mod([[values[i][j] for j in cols] for i in rows],p)
    assert determinant
    return {'rank_lb':rank,'rows':rows,'columns':cols,'determinant_mod_p':determinant}


def pilot(r,t,npts,families):
    census=json.loads((OUT/'census.json').read_text())
    cell=next(x for x in census['rows'] if (x['r'],x['t'])==(r,t))
    assert not cell['reserved'] and not cell['overlay_exclusions'] and cell['a_inf']<=533
    assert json.loads((OUT/'extension_controls.json').read_text())['status']=='EXACT'
    started=time.perf_counter();summary=[]
    bs=enumerate_brackets(sum(cell['tail']),r-1)
    for p in PRIMES:
        build=time.perf_counter();ev=Evaluator(bs,r-1,p)
        build=time.perf_counter()-build
        for family in families:
            stamp=time.perf_counter()
            reds,src=generate(family,r,p,npts,15060000+100*r+t)
            point_seconds=time.perf_counter()-stamp
            stamp=time.perf_counter()
            # Rows are explicit bracket constructions, columns are geometric points.
            values=list(map(list,zip(*(ev.values(red) for red in reds))))
            eval_seconds=time.perf_counter()-stamp
            stamp=time.perf_counter();minor=minor_certificate(values,p)
            rank_seconds=time.perf_counter()-stamp
            assert minor['rank_lb']<=cell['a_inf']
            record={'status':'REPLAYED_RANK_FLOOR','r':r,'t':t,'prime':p,'family':family,
                'a_inf':cell['a_inf'],'m_pad_ub':cell['m_pad_ub'],**minor,
                'points_requested':npts,'valid_points':len(reds),
                'construction_seconds':build,'point_seconds':point_seconds,
                'evaluation_seconds':eval_seconds,'reduction_seconds':rank_seconds}
            name=f'pilot_r{r}_t{t}_{family}_{p}'
            save(name+'.json.gz',{'record':record,'brackets':bs,'native':src,
                'interpolation_seed':20260913,'matrix_orientation':'brackets by points',
                'values_are':'rational symmetric-tensor bracket values reduced modulo p',
                'values':values})
            summary.append(record)
            save(f'pilot_r{r}_t{t}_summary.json',{'status':'RECORDED','complete':False,'records':summary})
            print('RANK',r,t,family,p,minor['rank_lb'],'seconds',round(point_seconds+eval_seconds+rank_seconds,2),flush=True)
    save(f'pilot_r{r}_t{t}_summary.json',{'status':'REPLAYED_RANK_FLOOR','complete':True,
        'records':summary,'seconds':time.perf_counter()-started})


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['controls','pilot'])
    parser.add_argument('--r',type=int);parser.add_argument('--t',type=int)
    parser.add_argument('--points',type=int,default=520)
    parser.add_argument('--families',nargs='+',default=['GEN','DET','PAD'])
    args=parser.parse_args()
    if args.mode=='controls':controls()
    else:pilot(args.r,args.t,args.points,args.families)
