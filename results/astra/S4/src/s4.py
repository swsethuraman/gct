"""S4 bounded padded certificates. Writes only within its own artifact directory."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import ast,collections,copy,datetime,gzip,hashlib,importlib.util,itertools,json,math,random,re,time
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('frozen_s1',ROOT/'inputs/s1_checks.py')
s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)
P=s.PRIMES
A=ROOT/'artifacts'
def write(path,x):path.write_text(json.dumps(x,indent=1),encoding='utf8')
def read(path):return json.loads(path.read_text(encoding='utf-8-sig'))
def coeffs(forms):
    r=len(forms[0]); out=collections.defaultdict(int)
    for pm in itertools.permutations(range(3)):
        f={ (0,)*r:1 }
        for lf in [forms[0]]+[forms[1+3*a+pm[a]] for a in range(3)]:
            nxt=collections.defaultdict(int)
            for e,c in f.items():
                for j,x in enumerate(lf):
                    z=list(e);z[j]+=1;nxt[tuple(z)]+=c*x
            f=nxt
        for e,c in f.items():out[e]+=c
    return [out[e] for e in s.exps(4,r)]
def direct_symbol(forms,indices):
    # Coefficient of t1*t2*t3*t4 in f(sum ti*e_indices[i]). No alpha! packer.
    return sum(forms[0][indices[q[0]]]*math.prod(forms[1+3*a+pm[a]][indices[q[a+1]]] for a in range(3))
               for q in itertools.permutations(range(4)) for pm in itertools.permutations(range(3)))
def perm_sign(x):return (-1)**sum(x[i]>x[j] for i in range(len(x)) for j in range(i+1,len(x)))
def ind_pack(F,symbol,p,order):
    # Reverse sweep, dynamic bags indexed by actual edge IDs, signs paid when opening.
    order=list(reversed(order));seen=set();active=[];stages=[];h=F.h
    for l in order:
        incident=[e for e,(a,b) in enumerate(F.two) if l in (a,b)]
        opening=[e for e in incident if e not in active]
        after=sorted(set(active).symmetric_difference(incident))
        bits=[];states=[];signs=[]
        for old in range(1<<len(active)):
            for new in range(1<<len(opening)):
                edgeValues={e:(old>>k)&1 for k,e in enumerate(active)}
                edgeValues.update({e:(new>>k)&1 for k,e in enumerate(opening)})
                val=0
                for k,e in enumerate(incident):
                    # edgeValues is the assignment at the FIRST endpoint processed.
                    v=edgeValues[e] if e in opening else 1-edgeValues[e]
                    val|=v<<k
                sg=0
                for e in opening:
                    x=edgeValues[e];sg^=x if F.two[e][0]==l else 1-x
                bits.append(val);states.append(sum(edgeValues[e]<<k for k,e in enumerate(after)));signs.append(sg)
        ina=l in F.C1;inb=l in F.C2;na=h if ina else 1;nb=h if inb else 1
        ns=F.one.count(l);tensors=[]
        for i in range(na):
            for j in range(nb):
                for b in range(1<<len(incident)):
                    ids=([i] if ina else [])+([j] if inb else [])+[(b>>k)&1 for k in range(len(incident))]+[0]*ns
                    assert len(ids)==4
                    tensors.append(symbol[tuple(sorted(ids))]%p)
        stages.append(dict(ina=int(ina),inb=int(inb),oldN=1<<len(active),newN=1<<len(after),branches=1<<len(opening),degree=len(incident),bits=bits,states=states,signs=signs,tensor=tensors))
        active=after;seen.add(l)
    assert not active
    sign=perm_sign([F.C1.index(l) for l in order if l in F.C1])*perm_sign([F.C2.index(l) for l in order if l in F.C2])
    return dict(h=h,p=p,sign=sign,stages=stages)
def prepare(count=36):
    start=time.perf_counter();scratch=ROOT/'scratch';scratch.mkdir(exist_ok=True)
    bank=read(ROOT/'inputs/snapshot/results/s69_ladder_n4.json')['basis']
    Fs=[s.Filling.from_json(x['filling']) for x in bank];assert len(Fs)==34
    points=[]
    for j in range(count):
        seed=12040000+j;rng=random.Random(seed)
        forms=[[rng.randint(-3,3) for _ in range(9)] for _ in range(10)]
        cv=coeffs(forms)
        # Retain same integer points at both primes; reject u=0 before evaluation.
        while cv[-1]==0:
            forms=[[rng.randint(-3,3) for _ in range(9)] for _ in range(10)];cv=coeffs(forms)
        symbols={t:direct_symbol(forms,t) for t in itertools.combinations_with_replacement(range(9),4)}
        exp=s.exps(4,9);byexp=dict(zip(exp,cv))
        for t,v in symbols.items():
            e=tuple(t.count(i) for i in range(9));assert v==math.prod(math.factorial(z) for z in e)*byexp[e]
        c3=s.exps(3,9)
        grad=[[ (b[k]+1)*byexp[tuple(b[i]+int(i==k) for i in range(9))] for b in c3] for k in range(9)]
        checks={str(p):{'frame':s.rank_minor(list(map(list,zip(*forms))),p),'concision':s.rank_minor(grad,p)} for p in P}
        assert all(checks[str(p)]['frame']['rank']==9 and checks[str(p)]['concision']['rank']==9 for p in P)
        points.append(dict(index=j,seed=seed,linear_forms=forms,coefficients=cv,u=cv[-1],checks=checks))
        jobs=[]
        for p in P:
            for i,F in enumerate(Fs):
                jid=f'p{p}_r{i}_c{j}'
                primary=s.pack_job(F,cv,p,jid)
                independent=ind_pack(F,symbols,p,primary['order'])
                jobs.append(dict(id=jid,primary=primary,independent=independent))
        (scratch/f'point_{j:02d}.json').write_text(json.dumps(jobs,separators=(',',':')))
        print('prepared point',j,round(time.perf_counter()-start,2),flush=True)
    write(A/'points.json',dict(exponents=s.exps(4,9),points=points))
    write(A/'source.json',{'lambda':[65,17]+[2]*7,'degree':24,'vectors':[{'index':i,'native_filling':F.to_json(),'native_degree':F.delta,'u_power':24-F.delta,'literal_extension_factor':{'numerator':1,'denominator':24**(24-F.delta)}} for i,F in enumerate(Fs)]})
def summarize():
    source=read(A/'source.json');pts=read(A/'points.json')['points'];data=[]
    for path in sorted((ROOT/'scratch').glob('values_*.json')):data+=read(path)
    vals={x['id']:x for x in data};cols=[j for j in range(len(pts)) if all(f'p{p}_r{i}_c{j}' in vals for p in P for i in range(34))]
    assert cols
    out={'completed_columns':cols,'results':[],'independent_entries_checked':0,'timings':{'primary':0,'independent':0}}
    for x in data:
        assert x['value']==x['independent'],x['id']
        out['independent_entries_checked']+=1
        for k in out['timings']:out['timings'][k]+=x[k+'_seconds']
    for p in P:
        native=[[vals[f'p{p}_r{i}_c{j}']['value'] for j in cols] for i in range(34)]
        target=[[native[i][k]*pow(pts[j]['u'],source['vectors'][i]['u_power'],p)%p for k,j in enumerate(cols)] for i in range(34)]
        m=s.rank_minor(target,p);out['results'].append(dict(prime=p,native_matrix=native,target_matrix=target,minor=m))
    write(A/'padded_certificate.json',out)
    print({k:v for k,v in out.items() if k!='results'})
    print([{'prime':x['prime'],'minor':x['minor']} for x in out['results']])
if __name__=='__main__':
    if sys.argv[1]=='prepare':prepare(int(sys.argv[2]) if len(sys.argv)>2 else 36)
    elif sys.argv[1]=='summarize':summarize()
