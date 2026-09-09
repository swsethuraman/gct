"""Exact coefficient realization of the reducible restriction of bracket sources.

No sampled zeros are used as rational identities. No numeric Pieri conversion
or permanent-stage Q is implemented. All coefficient keys are lossless tuples.
"""
import collections, datetime, functools, gzip, hashlib, itertools, json, math, pathlib, random, time

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/b13_02'
PRIMES = (2147483647, 2147483629)

def read(p): return json.loads((ROOT / p).read_text(encoding='utf-8-sig'))
def write(name, obj):
    OUT.mkdir(exist_ok=True)
    obj = dict(board_numbering='batch13', session_id='B13-02', **obj)
    (OUT / name).write_text(json.dumps(obj, indent=1), encoding='utf8')
def packed(name, obj):
    OUT.mkdir(exist_ok=True)
    obj = dict(board_numbering='batch13', session_id='B13-02', **obj)
    with gzip.GzipFile(OUT / name, 'wb', mtime=0) as f:
        f.write(json.dumps(obj, separators=(',', ':')).encode())
def exps(n, r):
    if r == 1: return [(n,)]
    return [(k,)+t for k in range(n+1) for t in exps(n-k, r-1)]
def sign(p): return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def factorial_symbol(alpha): return math.prod(math.factorial(x) for x in alpha)
def clean(d): return {k:v for k,v in d.items() if v}

def raising(basis, exponent, vectors):
    idx = {e:i for i,e in enumerate(exponent)}; residual = [collections.defaultdict(int) for _ in vectors]
    nrows = set()
    for j, m in enumerate(basis):
        for i in range(len(exponent[0])-1):
            for k, count in collections.Counter(m).items():
                al = exponent[k]
                if not al[i+1]: continue
                be = list(al); be[i]+=1; be[i+1]-=1
                t = list(m); t.remove(k); t.append(idx[tuple(be)])
                key = (i, tuple(sorted(t))); nrows.add(key)
                for v, acc in zip(vectors, residual): acc[key] += v[j]*count*(al[i]+1)
    assert all(not any(x.values()) for x in residual)
    return len(nrows)

def split_polynomial(vector, basis, exponent):
    r = len(exponent[0]); e3 = exps(3,r); idx3={e:i for i,e in enumerate(e3)}
    full=collections.defaultdict(int); fixed=collections.defaultdict(int)
    for coefficient, mono in zip(vector,basis):
        if not coefficient: continue
        if all(exponent[k][0] for k in mono):
            t=[]
            for k in mono:
                be=list(exponent[k]);be[0]-=1;t.append(idx3[tuple(be)])
            fixed[tuple(sorted(t))]+=coefficient
        terms={((0,)*r,()): coefficient}
        for k in mono:
            nxt=collections.defaultdict(int)
            for i,v in enumerate(exponent[k]):
                if not v: continue
                be=list(exponent[k]);be[i]-=1;bid=idx3[tuple(be)]
                for (g,m),c in terms.items():
                    gg=list(g);gg[i]+=1;nxt[tuple(gg),tuple(sorted(m+(bid,)))]+=c
            terms=clean(nxt)
        for key,c in terms.items(): full[key]+=c
        if len(full)>200000: raise RuntimeError('Preregistered symbolic term cap')
    return clean(full),clean(fixed),e3

def literal_polynomial(F):
    h=F['h'];d=F['delta'];cols=[F['C1'],F['C2']]+F['two']+[[l] for l in F['one']]
    exp=exps(4,h);idx={e:i for i,e in enumerate(exp)};out=collections.defaultdict(int)
    assert math.prod(math.factorial(len(c)) for c in cols)<=1000000
    for perms in itertools.product(*(itertools.permutations(range(len(c))) for c in cols)):
        al=[[0]*h for _ in range(d)];sg=1
        for col,pm in zip(cols,perms):
            sg*=sign(pm)
            for l,k in zip(col,pm):al[l][k]+=1
        coeff=sg*math.prod(factorial_symbol(a) for a in al)
        out[tuple(sorted(idx[tuple(a)] for a in al))]+=coeff
    return clean(out),exp

def controls():
    start=time.time();bank=read('results/astra/S4/artifacts/s64_control.json')
    exponent=[tuple(e) for e in bank['exponents']];basis=[tuple(m) for m in bank['basis']]
    vectors=bank['source_vectors'];assert len(basis)==561
    assert raising(basis,exponent,vectors)==1056
    full=[];fixed=[]
    for v in vectors:
        f,g,e3=split_polynomial(v,basis,exponent);full.append(f);fixed.append(g)
    assert not full[0] and not fixed[0] and full[1] and fixed[1]
    # Exact source independence and nonzero image witnesses, no numerical rank engine.
    source_minor=None
    for i,j in itertools.combinations(range(len(basis)),2):
        det=vectors[0][i]*vectors[1][j]-vectors[0][j]*vectors[1][i]
        if det: source_minor={'columns':[i,j],'determinant':det};break
    assert source_minor
    fkeys=sorted(set().union(*(set(x) for x in full)));gkeys=sorted(set().union(*(set(x) for x in fixed)))
    packed('control_r3_full_split.json.gz',dict(exponents_cubic=e3,source_input='results/astra/S4/artifacts/s64_control.json',
        values_are='exact integer coefficients of ordinary y^gamma times cubic coefficient monomials',
        columns=[[g,list(m)] for g,m in fkeys],matrix=[[f.get(k,0) for k in fkeys] for f in full],
        fixed_columns=gkeys,fixed_matrix=[[g.get(k,0) for k in gkeys] for g in fixed]))
    tiny={'h':2,'n':4,'delta':2,'C1':[0,1],'C2':[0,1],'two':[[0,1],[0,1]],'one':[]}
    tiny_poly,te=literal_polynomial(tiny);tb=sorted(tiny_poly);tv=[[tiny_poly[k] for k in tb]]
    raising(tb,te,tv);tf,tg,t3=split_polynomial(tv[0],tb,te)
    assert tg
    checks=[]
    for m,c in tg.items():
        target=tuple(sorted(tuple(i for i,v in enumerate(t3[k]) for _ in range(v)) for k in m))
        value,stat=extract(tiny,target,120,250000)
        assert value==c,(target,value,c)
        checks.append(dict(monomial=target,coefficient=value,states=stat))
    # Independently expand all tiny contraction coefficients including zeros.
    candidates=itertools.combinations_with_replacement(range(len(t3)),2)
    for m in candidates:
        if tuple(sum(t3[k][i] for k in m) for i in range(2))!=(2,4):continue
        target=tuple(sorted(tuple(i for i,v in enumerate(t3[k]) for _ in range(v)) for k in m))
        v,_=extract(tiny,target,120,250000);assert v==tg.get(m,0)
    write('controls.json',dict(status='CERTIFIED exact integer coefficient identities',r3_source_dimension=2,
        r3_raising_equations=1056,r3_source_independence_minor=source_minor,
        r3_full_split_nonzero_terms=list(map(len,full)),r3_fixed_nonzero_terms=list(map(len,fixed)),
        r3_exact_rank=1,r3_kernel_coordinates=[1,0],
        nonzero_restriction_witness={'monomial':list(gkeys[0]),'coefficient':fixed[1][gkeys[0]]},
        tiny_filling=tiny,tiny_polynomial=[[list(k),v] for k,v in tiny_poly.items()],
        tiny_exact_rank=1,tiny_coefficient_checks=checks,seconds=time.time()-start))
    print('Exact controls complete',len(fkeys),len(gkeys),time.time()-start,flush=True)

def order_filling(F):
    d=F['delta'];edges=F['two']; best=None
    for first in range(d):
        done=set();active=set();order=[];width=0;cur=first
        while len(done)<d:
            done.add(cur);order.append(cur)
            for e,(a,b) in enumerate(edges):
                if cur in (a,b):
                    if e in active:active.remove(e)
                    else:active.add(e)
            width=max(width,len(active))
            if len(done)<d:
                def cost(l):return len(active)+sum(-1 if e in active else 1 for e,ab in enumerate(edges) if l in ab)
                cur=min((l for l in range(d) if l not in done),key=lambda l:(cost(l),l))
        if best is None or (width,order)<best:best=(width,order)
    return best[1],best[0]

def extract(F, target, seconds=120, states=250000):
    """One EXACT integer coefficient at x1*c, by a lossless frontier DP.

    target is a cubic monomial as a tuple of sorted triples of variable indices.
    Each quartic tensor has ordinary-coefficient multiplier alpha!, not alpha0.
    Tall wedge signs are inversion counts; short signs use the original endpoints.
    """
    started=time.time();h=F['h'];d=F['delta'];assert len(target)==d
    types=sorted(set(target));counts=tuple(target.count(t) for t in types)
    alpha=[tuple(sorted((0,)+t)) for t in types];type_index={t:k for k,t in enumerate(alpha)}
    scalars=[math.prod(math.factorial(v) for v in collections.Counter(t).values()) for t in alpha]
    order,width=order_filling(F);active=[];trans=[]
    # Precompute legal local terms for each incoming short-edge assignment.
    for l in order:
        incident=[e for e,ab in enumerate(F['two']) if l in ab]
        opening=[e for e in incident if e not in active]
        after=sorted(set(active).symmetric_difference(incident))
        ia=l in F['C1'];ib=l in F['C2'];ones=F['one'].count(l);tab=[]
        for mask in range(1<<len(active)):
            options=[]
            for branch in range(1<<len(opening)):
                ev={e:(mask>>k)&1 for k,e in enumerate(active)}
                ev.update({e:(branch>>k)&1 for k,e in enumerate(opening)})
                bits=[ev[e] if e in opening else 1-ev[e] for e in incident]
                sg=1
                for e in opening:
                    original_first=ev[e] if F['two'][e][0]==l else 1-ev[e]
                    sg*=(-1)**original_first
                nextmask=sum(ev[e]<<k for k,e in enumerate(after))
                for i in range(h) if ia else [-1]:
                    for j in range(h) if ib else [-1]:
                        t=tuple(sorted(([i] if ia else [])+([j] if ib else [])+bits+[0]*ones))
                        k=type_index.get(t)
                        if k is not None:options.append((i,j,k,nextmask,sg*scalars[k]))
            tab.append(options)
        trans.append(tab);active=after
    assert not active
    phase=sign([F['C1'].index(l) for l in order if l in F['C1']])*sign([F['C2'].index(l) for l in order if l in F['C2']])
    visited=0
    @functools.lru_cache(maxsize=None)
    def rec(t,ma,mb,short,remaining):
        nonlocal visited
        visited+=1
        if visited>states:raise RuntimeError('state_cap')
        if visited%1024==0 and time.time()-started>seconds:raise RuntimeError('coefficient_time_cap')
        if t==d:
            assert ma==mb==(1<<h)-1 and short==0 and not any(remaining)
            return 1
        total=0
        for i,j,k,nmask,c in trans[t][short]:
            if not remaining[k] or (i>=0 and ma>>i&1) or (j>=0 and mb>>j&1):continue
            sg=c
            if i>=0:sg*=(-1)**((ma>>(i+1)).bit_count())
            if j>=0:sg*=(-1)**((mb>>(j+1)).bit_count())
            rr=list(remaining);rr[k]-=1
            total+=sg*rec(t+1,ma|(1<<i if i>=0 else 0),mb|(1<<j if j>=0 else 0),nmask,tuple(rr))
        return total
    try:
        value=phase*rec(0,0,0,0,counts)
        return value,dict(visited=visited,seconds=time.time()-started,width=width,types=len(types),complete=True)
    finally:rec.cache_clear()

def audit():
    source=read('results/s74/source.json');entries=source['entries'];assert len(entries)==274
    e4=exps(4,9);e3=exps(3,9);ui=e4.index((4,)+(0,)*8);assert ui==source['u_index']
    circuits=[]
    for j,e in enumerate(entries):
        for name in ('native','literal'):
            F=e[name];cols=[F['C1'],F['C2']]+F['two']+[[l] for l in F['one']]
            cnt=collections.Counter(l for col in cols for l in col)
            assert cnt=={l:4 for l in range(F['delta'])}
            assert all(len(c)==len(set(c)) for c in cols)
            lam=tuple(sum(len(c)>r for c in cols) for r in range(9))
            assert tuple(F['lam'])==lam
        F=e['native'];t=24-F['delta'];L=e['literal'];assert t==e['exponent']
        assert all(F[k]==L[k] for k in ('C1','C2','two'))
        assert L['one']==F['one']+[l for l in range(F['delta'],24) for _ in range(4)]
        assert e['factorial_scalar']==24**t
        circuits.append(dict(source_index=j,native_filling=F,transport_power=t,
                             transport_scalar=24**t,transport_cubic=(0,0,0)))
    substitutions=[]
    for a in e4:
        terms=[]
        for i,v in enumerate(a):
            if v:
                b=list(a);b[i]-=1
                terms.append(dict(linear_index=i,cubic_exponent=b,house_symbol_multiplier=v))
        fixed=None
        if a[0]:
            b=list(a);b[0]-=1
            fixed=dict(cubic_exponent=b,cubic_ordinary_coefficient_multiplier=factorial_symbol(a))
        substitutions.append(dict(quartic_exponent=a,full_house_terms=terms,fixed_house_in_ordinary_cubic=fixed))
    packed('source_restriction_circuit.json.gz',dict(source_sha256=hashlib.sha256((ROOT/'results/s74/source.json').read_bytes()).hexdigest(),
        formula='Each column alternates its index assignments; each letter uses the displayed substitution; multiply by (24*d_(3,0^8))^transport_power',
        values_are='exact integer substitution scalars; source is s74 literal degree-24 normalization',
        quartic_exponents=e4,cubic_exponents=e3,substitutions=substitutions,source_circuits=circuits))
    # Preregistered deterministic monomials from literal valid summands.
    selectors=[0,1,2,39,273];monos=[];rng=random.Random(130200)
    for row in selectors:
        F=entries[row]['native'];cols=[F['C1'],F['C2']]+F['two']+[[l] for l in F['one']]
        for trial in range(100000):
            assignments=[rng.sample(range(len(c)),len(c)) for c in cols]
            ids=[[] for _ in range(F['delta'])]
            for c,pm in zip(cols,assignments):
                for l,k in zip(c,pm):ids[l].append(k)
            if all(0 in t for t in ids):
                for t in ids:t.remove(0)
                target=tuple(sorted([tuple(sorted(t)) for t in ids]+[(0,0,0)]*(24-F['delta'])))
                if target not in [tuple(tuple(t) for t in m['cubic_triples']) for m in monos]:
                    monos.append(dict(generated_from_row=row,trial=trial,cubic_triples=target));break
        else:raise RuntimeError('No coefficient selector found')
    write('source_audit.json',dict(source_rows=274,all_literal_incidence_checks=True,u_index_resolved=ui,
         source_basis_status='ADOPTED s74 generic full-rank certificate',coefficient_seed=130200,coefficient_columns=monos))
    # Preserve the modular candidate coordinates in the exact source normalization.
    candidates=[]
    for p in PRIMES:
        x=read(f'results/s74/decision_{p}.json')['columns']['red']
        candidates.append(dict(prime=p,source='results/s74/decision_'+str(p)+'.json',data=x,
                               status='MEASURED sampled candidates only; not rational ideal elements'))
    write('inherited_candidates.json',dict(candidates=candidates))
    print('Audited all 274 source circuits; selected 5 exact coefficient columns',flush=True)

def pilot(arg):
    column=int(arg);source=read('results/s74/source.json')['entries'];audit=read('results/b13_02/source_audit.json')
    target=tuple(tuple(t) for t in audit['coefficient_columns'][column]['cubic_triples'])
    result=[];start=time.time()
    # Native controls first, then all remaining source rows if within the launch bound.
    row_order=list(dict.fromkeys([0,1,2,39,273]+list(range(274))))
    for j in row_order:
        e=source[j];m=list(target);power=e['exponent'];stat={}
        if m.count((0,0,0))<power:value=0;stat={'reason':'transport monomial support exclusion','complete':True}
        else:
            for _ in range(power):m.remove((0,0,0))
            try:
                value,stat=extract(e['native'],tuple(m));value*=24**power
            except (RuntimeError,MemoryError) as exc:
                value=None;stat={'complete':False,'reason':str(exc)}
        result.append(dict(source_row=j,coefficient=value,computation=stat))
        write(f'pilot_column_{column:02d}.json',dict(column_index=column,cubic_monomial=target,
            values_are='exact integer coefficients of s74 literal degree-24 source evaluated at x1*c; null means NOT computed, not zero',
            entries=result,elapsed_seconds=time.time()-start))
        print('column',column,'row',j,'coefficient',value,'stats',stat,flush=True)
        if time.time()-start>550:break

def main(mode,arg=''):
    if mode=='audit':audit()
    elif mode=='controls':controls()
    elif mode=='pilot':pilot(arg)
    else:raise ValueError(mode)
