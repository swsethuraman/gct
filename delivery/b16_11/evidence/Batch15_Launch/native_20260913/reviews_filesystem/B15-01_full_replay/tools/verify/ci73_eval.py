"""Independent CI73 symbol construction, contraction planning and bounded backend.

Source coefficients are evaluated in Z/(2^256) only under a proved height bound;
modular target and generic minors use the same independently implemented sum.
"""
from collections import Counter
from functools import lru_cache
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
CACHE=ROOT/'results/ci73/cache'


def need(c,why):
    if not c: raise ValueError(why)


@lru_cache(None)
def exps(n,r):
    if r==1:return ((n,),)
    return tuple((i,)+a for i in range(n+1) for a in exps(n-i,r-1))


def filling(f):
    h=f['h'];v=f['val'];c1=f['C1'];c2=f['C2'];two=f['two'];one=f['one']
    need(type(h) is int and 1<=h<=9,'invalid height')
    need(len(c1)==len(c2)==h and len(set(c1))==len(set(c2))==h,'invalid tall columns')
    need(all(type(x) is int and 0<=x<len(v) for x in c1+c2+one+sum(two,[])),'invalid letter label')
    need(all(type(x) is int and x in (1,3,4) for x in v),'invalid letter valence')
    need(all(len(e)==2 and e[0]!=e[1] for e in two),'invalid two-column')
    counts=Counter(c1+c2+one+sum(two,[]))
    need([counts[i] for i in range(len(v))]==v,'letter valence mismatch')
    return {k:f[k] for k in ('h','val','C1','C2','two','one')}


def native_source(e,degree=13):
    f=e['native'];d=f['delta']
    need(f['n']==4 and e['rung']==d and 12<=d<=degree,'native degree mismatch')
    return filling(dict(h=f['h'],val=[4]*degree,C1=f['C1'],C2=f['C2'],two=f['two'],
                        one=f['one']+[i for i in range(d,degree) for _ in range(4)]))


@lru_cache(maxsize=200)
def plan(serialized):
    f=json.loads(serialized);d=len(f['val']);h=f['h'];edges=f['two']
    a=sum(1<<x for x in f['C1']);b=sum(1<<x for x in f['C2']);full=(1<<d)-1
    @lru_cache(None)
    def info(done):
        na=(done&a).bit_count();nb=(done&b).bit_count()
        width=sum(bool(done&(1<<i))!=bool(done&(1<<j)) for i,j in edges)
        return na,nb,width,math.comb(h,na)*math.comb(h,nb)*(1<<width)
    beam={0:(0,())}
    # All subsets for d<=13; otherwise deterministic beam, optimizing actual
    # transition count rather than reusing the producer's edge-slot heuristic.
    for stage in range(d):
        nxt={}
        for done,(cost,order) in beam.items():
            na,nb,w,states=info(done)
            for letter in range(d):
                if done&(1<<letter):continue
                opens=sum(letter in edge and not (done&(1<<(edge[1] if edge[0]==letter else edge[0]))) for edge in edges)
                transitions=states*(h-na if a&(1<<letter) else 1)*(h-nb if b&(1<<letter) else 1)*(1<<opens)
                mask=done|(1<<letter);candidate=(cost+transitions,order+(letter,))
                if mask not in nxt or candidate<nxt[mask]:nxt[mask]=candidate
        if d>13 and len(nxt)>128:
            nxt=dict(sorted(nxt.items(),key=lambda kv:(kv[1][0]+info(kv[0])[3],kv[1][1]))[:128])
        beam=nxt
    cost,order=beam[full];done=0;peak=0;previous=1;width=0
    for letter in order:
        done|=1<<letter;n1,n2,w,states=info(done);peak=max(peak,states+previous);previous=states;width=max(width,w)
    return {'order':order,'transitions':cost,'peak_states_pair':peak,'frontier':width}


def quartic_symbols(point,ce):
    l=point['linear'];c=point['cubic_coefficients'];r=len(l)
    need(len(ce)==len(c) and set(map(tuple,ce))==set(exps(3,r)),'cubic exponent list')
    q={a:0 for a in exps(4,r)}
    for a,value in zip(ce,c):
        for i,li in enumerate(l):
            b=list(a);b[i]+=1;q[tuple(b)]+=li*value
    return {a:value*math.prod(math.factorial(x) for x in a) for a,value in q.items()}


def mixed_symbols(point,ce):
    r=len(point['linear'])
    return {1:{tuple(int(i==j) for i in range(r)):v for j,v in enumerate(point['linear'])},
            3:{tuple(a):v*math.prod(math.factorial(x) for x in a) for a,v in zip(ce,point['cubic_coefficients'])}}


def tensors(f,symbols,order,prime=0):
    h=f['h'];r=len(next(iter(next(iter(symbols[0].values())).keys())))
    result=[]
    for letter in order:
        in1=letter in f['C1'];in2=letter in f['C2'];edges=[e for e in f['two'] if letter in e]
        one=f['one'].count(letter);data=[]
        for i in range(h) if in1 else [None]:
            for j in range(h) if in2 else [None]:
                for bits in range(1<<len(edges)):
                    ids=[0]*one+([i] if in1 else [])+([j] if in2 else [])+[(bits>>q)&1 for q in range(len(edges))]
                    alpha=tuple(ids.count(k) for k in range(r))
                    for table in symbols:
                        value=table[f['val'][letter]][alpha]
                        data.append(value%prime if prime else value)
        result.append(data)
    return result


def build():
    CACHE.mkdir(parents=True,exist_ok=True)
    src=HERE/'ci73_backend.cs';identity=hashlib.sha256(src.read_bytes()).hexdigest()
    exe=CACHE/('ci73_'+identity[:16]+'.exe')
    if exe.exists():return exe
    compiler=Path(os.environ.get('CI73_CSC','C:/Windows/Microsoft.NET/Framework64/v4.0.30319/csc.exe'))
    need(compiler.exists(),'C# compiler absent; set CI73_CSC to a C#5-compatible compiler')
    command=[str(compiler),'/nologo','/optimize+','/platform:x64','/r:System.Numerics.dll','/r:System.Web.Extensions.dll',
             '/out:'+str(exe),str(src)]
    p=subprocess.run(command,capture_output=True,text=True,timeout=60,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    (CACHE/'build.log').write_text(p.stdout+p.stderr,encoding='utf-8')
    need(p.returncode==0,'backend build failed: '+p.stdout+p.stderr)
    return exe


def evaluate(f,symbols,prime=0,name='entry',seconds=120):
    f=filling(f);spec=plan(json.dumps(f,sort_keys=True));batch=len(symbols)
    need(spec['peak_states_pair']*batch*(8 if prime else 32)<=500_000_000,'batch exceeds backend array budget')
    payload=dict(f,order=spec['order'],batch=batch,prime=prime,mode='modular' if prime else 'integer256',
                 tensors=tensors(f,symbols,spec['order'],prime))
    if not prime:need(all(abs(x)<2**30 for row in payload['tensors'] for x in row),'exact tensor outside Int64 bound')
    exe=build();ip=CACHE/(name+'.input.json');op=CACHE/(name+'.output.json')
    ip.write_text(json.dumps(payload,separators=(',',':')),encoding='utf-8')
    p=subprocess.Popen([str(exe),str(ip),str(op)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,
                       creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    logs=ROOT/'results/logs';logs.mkdir(exist_ok=True)
    (logs/(name+'.pid')).write_text(str(p.pid)+'\n')
    started=time.monotonic()
    try:out,err=p.communicate(timeout=seconds)
    except subprocess.TimeoutExpired:
        p.kill();p.communicate();raise RuntimeError('backend deadline, recorded pid '+str(p.pid))
    need(p.returncode==0,'backend failure: '+err.decode(errors='replace'))
    result=json.loads(op.read_text());need(result['status']=='OK','backend result incomplete')
    result.update(pid=p.pid,exit=p.returncode,wall_seconds=time.monotonic()-started,plan=spec)
    (logs/(name+'.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    return [int(x) for x in result['values']],result


def literal(f,symbols):
    """Independent small reference: Cartesian product of all column permutations."""
    columns=[f['C1'],f['C2']]+f['two']+[[x] for x in f['one']]
    assignments=[]
    for col in columns:
        options=[]
        for perm in itertools.permutations(range(len(col))):
            sign=(-1)**sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))
            options.append((perm,sign))
        assignments.append(options)
    r=len(next(iter(next(iter(symbols.values())).keys())))
    value=0
    for choice in itertools.product(*assignments):
        slots=[[] for _ in f['val']];coefficient=1
        for col,(perm,sgn) in zip(columns,choice):
            coefficient*=sgn
            for letter,i in zip(col,perm):slots[letter].append(i)
        for val,indices in zip(f['val'],slots):
            coefficient*=symbols[val][tuple(indices.count(i) for i in range(r))]
        value+=coefficient
    return value
