"""Bounded S1 checks. No writes to the source checkout; Python + NumPy only.
Run prepare, then run_packed.ps1, then summarize. Artifacts use integer coefficients.
"""
from pathlib import Path
import ast, collections, copy, gzip, hashlib, itertools, json, math, random, sys, time
import numpy as np
ROOT=Path(__file__).resolve().parent
LIVE_REPO=Path(r'C:\Users\swami\Projects\gct\work')
REPO=ROOT/'inputs/snapshot' if (ROOT/'inputs/snapshot').exists() else LIVE_REPO
P1,P2=2147483647,2147483629
PRIMES=(P1,P2)
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def write(p,x): Path(p).write_text(json.dumps(x,indent=1),encoding='utf-8')
def exps(n,r):
    if r==1:return ((n,),)
    return tuple((i,)+a for i in range(n+1) for a in exps(n-i,r-1))

# Reuse only the actual, audited filling and tensor packer definitions. No native library import.
names={'Filling','random_filling','sym_table','symbols_from_coeffs','_perms_with_sign',
       'brute_force_eval','unit_structure','letter_tensors','fast_eval_py','letter_order',
       'dp_pack'}
tree=ast.parse((REPO/'analysis/wk11_s69_circuit.py').read_text())
selected=ast.Module(body=[x for x in tree.body if isinstance(x,(ast.FunctionDef,ast.ClassDef)) and x.name in names],type_ignores=[])
exec(compile(selected,'audited_s69_definitions','exec'),globals())

def detmod(M,p):
    a=[[int(x)%p for x in row] for row in M]; out=1
    for k in range(len(a)):
        q=next((q for q in range(k,len(a)) if a[q][k]),None)
        if q is None:return 0
        if q!=k:a[k],a[q]=a[q],a[k];out=-out
        v=a[k][k];out=out*v%p;iv=pow(v,-1,p)
        for i in range(k+1,len(a)):
            f=a[i][k]*iv%p
            for j in range(k+1,len(a)):a[i][j]=(a[i][j]-f*a[k][j])%p
    return out%p
_det_mod=detmod
def rank_minor(rows,p):
    if not rows:return dict(rank=0,rows=[],cols=[],det=1)
    a=[[int(x)%p for x in row] for row in rows]; ids=list(range(len(a))); rr=[];cc=[];k=0
    for j in range(len(a[0])):
        q=next((q for q in range(k,len(a)) if a[q][j]),None)
        if q is None:continue
        a[k],a[q]=a[q],a[k];ids[k],ids[q]=ids[q],ids[k]
        rr.append(ids[k]);cc.append(j); iv=pow(a[k][j],-1,p)
        for i in range(k+1,len(a)):
            f=a[i][j]*iv%p
            for t in range(j,len(a[0])):a[i][t]=(a[i][t]-f*a[k][t])%p
        k+=1
        if k==len(a):break
    minor=[[rows[i][j] for j in cc] for i in rr]
    return dict(rank=k,rows=rr,cols=cc,det=detmod(minor,p))

def pencil(n,r,seed,permanent=False,As=None):
    rng=random.Random(seed)
    As=As if As is not None else [[rng.randint(-7,7) for _ in range(n*n)] for _ in range(r)]
    zero=(0,)*r; co=collections.defaultdict(int)
    for perm in itertools.permutations(range(n)):
        sign=1 if permanent else (-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        cur={zero:sign}
        for a,b in enumerate(perm):
            nxt=collections.defaultdict(int)
            for al,v in cur.items():
                for i in range(r):
                    be=list(al);be[i]+=1;nxt[tuple(be)]+=v*As[i][a*n+b]
            cur=nxt
        for al,v in cur.items():co[al]+=v
    # Independent numeric substitution verifies coefficient building.
    s=[i-2 for i in range(r)]; M=[[sum(s[i]*As[i][a*n+b] for i in range(r)) for b in range(n)] for a in range(n)]
    v=sum(cf*math.prod(x**e for x,e in zip(s,al)) for al,cf in co.items())
    direct=sum((1 if permanent else (-1)**sum(pm[i]>pm[j] for i in range(n) for j in range(i+1,n)))*math.prod(M[i][pm[i]] for i in range(n)) for pm in itertools.permutations(range(n)))
    assert v==direct
    return [co[a] for a in exps(n,r)],As

def pack_job(F,cv,p,id):
    # Deterministic ordering, with explicit no-cache behavior.
    order,W=letter_order(F,rng=random.Random(0),restarts=8)
    P=dp_pack(F,symbols_from_coeffs(cv,F.n,F.h,p),p,order=order)
    assert P['W']<=6
    P['stride']=int(P['l_edge'].shape[1]);P['id']=id
    for k,v in list(P.items()):
        if isinstance(v,np.ndarray):P[k]=v.reshape(-1).tolist()
    return P

def canonical(F):
    """Signed normalization for fixed labels.
    It removes safe duplicates, without claiming a complete graph canonical form.
    """
    x=F.to_json();sg=1
    for key in ('C1','C2'):
        seq=x[key];sg*=(-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
        x[key]=sorted(seq)
    if x['C2']<x['C1']:x['C1'],x['C2']=x['C2'],x['C1']
    tw=[]
    for a,b in x['two']:
        if a>b:sg=-sg;a,b=b,a
        tw.append([a,b])
    x['two']=sorted(tw);x['one']=sorted(x['one'])
    return Filling.from_json(x),sg

def plucker_once(F):
    x=F.to_json()
    for i,(a,b) in enumerate(x['two']):
        for j,(c,d) in enumerate(x['two']):
            if i<j and a<c<d<b:
                y=copy.deepcopy(x);z=copy.deepcopy(x)
                y['two'][i]=[a,d];y['two'][j]=[c,b]
                z['two'][i]=[a,c];z['two'][j]=[d,b]
                return Filling.from_json(y),Filling.from_json(z)
    return None

def prepare():
    (ROOT/'scratch').mkdir(exist_ok=True);(ROOT/'inputs').mkdir(exist_ok=True)
    inputs=[]
    paths=list(Path(r'C:\Users\swami\Projects\gct-gpt').glob('*.md'))+[Path(r'C:\Users\swami\Projects\gct-gpt\Batch12_Reconciled_Final_Proposal.docx')]
    paths += [Path(r'C:\Users\swami\Documents\Codex\2026-09-08\referenced-chatgpt-conversation-this-is-an-2\outputs')/f for f in ['S1_Astra_Straightening.md','Batch12_Launch_Packet.md']]
    paths += [p for p in (REPO/'analysis').glob('wk11_s69_*') if p.suffix in ['.py','.c']]
    paths += [REPO/f for f in ['docs/compact_circuit.md','docs/s69_report.md','results/s69_n4_seed.json','results/s69_ladder_n4.json','results/s69_lmr_state.json','results/s63_aladder.json','results/s69_n3_d12.json','results/artefacts/s69_n3_d12_basis.json.gz','results/artefacts/s69_banked_n3_d12.json','tools/verify/selftest.py','tools/verify/points.py']]
    if (ROOT/'inputs/snapshot').exists():paths=[]  # Preserve the frozen original-location manifest on portable replay.
    for p in paths:inputs.append(dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
    if inputs:write(ROOT/'input_manifest.json',inputs)
    n3=read(REPO/'results/s69_n3_d12.json');n4=read(REPO/'results/s69_n4_seed.json')
    basis={3:[Filling.from_json(f) for f in n3['basis']],4:[Filling.from_json(f) for f in n4['basis']]}
    points={};jobs=[];design={'basis':{str(n):[f.to_json() for f in fs] for n,fs in basis.items()},'points':{},'jobs':[]}
    def add(F,cv,p,id):
        jobs.append(pack_job(F,cv,p,id));design['jobs'].append({'id':id,'filling':F.to_json(),'coefficients':cv,'prime':p})
    for n,fs in basis.items():
        r=fs[0].h
        for family in (['generic','det','permanent','birth'] if n==3 else ['generic','det']):
            cvs=[];raw=[]
            for j in range(7 if n==3 else 3):
                seed=120100+n*1000+100*(['generic','det','permanent','birth'].index(family))+j
                if family in ['det','permanent']:cv,As=pencil(n,r,seed,family=='permanent');raw.append({'seed':seed,'pencil':As})
                else:
                    rng=random.Random(seed);cv=[rng.randrange(1,100000) for _ in exps(n,r)]
                    if family=='birth':cv[exps(n,r).index((n,)+(0,)*(r-1))]=0
                    raw.append({'seed':seed})
                cvs.append(cv)
            design['points'][f'{n}_{family}']={'coefficients':cvs,'parameters':raw,'exponent_order':exps(n,r)}
            for p in PRIMES:
                for i,F in enumerate(fs):
                    for j,cv in enumerate(cvs):add(F,cv,p,f'{n}_{family}_{p}_{i}_{j}')
    # Fresh independent tiny controls for literal and Plucker/sign checks.
    rng=random.Random(1201);tiny=[]
    for z in range(8):
        F=random_filling(3,4,4,3,4,rng,k=2)
        cv=[rng.randrange(1,1000) for _ in exps(4,3)]
        G,sg=canonical(F);pair=plucker_once(G)
        for p in PRIMES:
            value=brute_force_eval(F,symbols_from_coeffs(cv,4,3,p),p)
            assert value==fast_eval_py(F,symbols_from_coeffs(cv,4,3,p),p)
            assert value==sg*brute_force_eval(G,symbols_from_coeffs(cv,4,3,p),p)%p
            if pair:
                assert brute_force_eval(G,symbols_from_coeffs(cv,4,3,p),p)==(brute_force_eval(pair[0],symbols_from_coeffs(cv,4,3,p),p)-brute_force_eval(pair[1],symbols_from_coeffs(cv,4,3,p),p))%p
            add(F,cv,p,f'tiny_{p}_{z}')
            tiny.append({'id':f'tiny_{p}_{z}','literal':value,'mixed_determinant':value,'plucker_test':pair is not None})
    write(ROOT/'tiny_checks.json',tiny)
    # Verify exact integer combination of the archived chi arrays, independently of original LA.
    with gzip.open(REPO/'results/artefacts/s69_n3_d12_basis.json.gz','rt') as f:art=json.load(f)
    bk=read(REPO/'results/artefacts/s69_banked_n3_d12.json')['vector_chi_coords']
    co=[66,-972,12,-37,4,320]
    u=[sum(c*v[j] for c,v in zip(co,art['chi_vectors'])) for j in range(len(bk))]
    gcd=math.gcd(*u);primitive=[v//gcd for v in u];sg=1 if primitive==bk else -1
    assert [sg*v for v in primitive]==bk
    archive={'integer_ideal_coefficients':co,'combination_gcd':gcd,'sign_to_bank':sg,'coordinate_count':len(bk),'mismatches':0,'support':sum(v!=0 for v in bk),'max_abs':max(map(abs,bk)),
        'scope':'Exact arithmetic on archived chi expansions, not a fresh expansion or E-matrix replay.'}
    archive['chi_minors']={str(p):rank_minor(art['chi_vectors'],p) for p in PRIMES}
    archive['seed_minors']={fam:{str(p):rank_minor(n4['rows_'+fam][str(p)],p) for p in PRIMES} for fam in ['generic','det']}
    st=read(REPO/'results/s69_lmr_state.json');archive['target_archived_row_minor']=rank_minor(st['rows'],P1)
    archive['target_archived_scope']='Archived 113x300 matrix arithmetic only, not a new target evaluation certificate.'
    ladder=read(REPO/'results/s69_ladder_n4.json');archive['checkpoint_birth_counts']=dict(collections.Counter(b['birth'] for b in ladder['basis']))
    write(ROOT/'archive_checks.json',archive)
    write(ROOT/'control_design.json',design)
    write(ROOT/'scratch/packed.json',jobs)
    print('Prepared',len(jobs),'evaluations; archived ideal/minor arithmetic passed',flush=True)

def summarize():
    out=read(ROOT/'scratch/evaluations.json');by={x['id']:x for x in out};design=read(ROOT/'control_design.json')
    rows={};checks={}
    for n in [3,4]:
        fs=design['basis'][str(n)]
        for family in (['generic','det','permanent','birth'] if n==3 else ['generic','det']):
            for p in PRIMES:
                key=f'{n}_{family}_{p}';K=7 if n==3 else 3
                rows[key]=[[by[f'{key}_{i}_{j}']['value'] for j in range(K)] for i in range(len(fs))]
                checks[key]=rank_minor(rows[key],p)
                if n==3 and family=='det':
                    co=[66,-972,12,-37,4,320]
                    checks[key]['ideal_values']=[sum(co[i]*rows[key][i][j] for i in range(6))%p for j in range(K)]
    for x in read(ROOT/'tiny_checks.json'):assert by[x['id']]['value']==x['literal']
    # Genuinely different evaluator: determinant polarization with plain Python elimination.
    independent=[]
    for p in PRIMES:
        for i in range(6):
            id=f'3_det_{p}_{i}_0';job=next(x for x in design['jobs'] if x['id']==id);F=Filling.from_json(job['filling']);t=time.perf_counter()
            v=fast_eval_py(F,symbols_from_coeffs(job['coefficients'],3,7,p),p)
            assert v==by[id]['value'];independent.append(dict(id=id,value=v,seconds=time.perf_counter()-t))
    write(ROOT/'control_matrices.json',{'matrices':rows,'minors':checks,'independent_mixed_determinant':independent,'evaluation_timings':out})
    print(json.dumps(checks,indent=1));print('Independent evaluator comparisons passed',len(independent),flush=True)

if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    {'prepare':prepare,'summarize':summarize}[sys.argv[1]]()
