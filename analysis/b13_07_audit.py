"""Exact S79 audit. All mutations are confined to results/b13_07."""
import collections
import datetime as dt
import gzip
import hashlib
import itertools as it
import json
import math
from pathlib import Path
import random
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/b13_07'
OUT.mkdir(exist_ok=True)
sys.path.insert(0, str(ROOT / 'analysis'))
sys.path.insert(0, str(ROOT / 'tools/verify'))
PRIMES = (2147483647, 2147483629)

def read(path):
    path = Path(path)
    with (gzip.open(path, 'rt', encoding='utf-8') if path.suffix == '.gz' else open(path, encoding='utf-8')) as f:
        return json.load(f)

def save(name, result):
    result.update(board_numbering='batch13', session_id='B13-07', time_utc=dt.datetime.now(dt.timezone.utc).isoformat())
    (OUT / (name + '.json')).write_text(json.dumps(result, indent=1) + '\n', encoding='utf-8')
    print(name, result.get('status', 'written'), flush=True)

def digest(path, algorithm='sha256'):
    h = hashlib.new(algorithm)
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(1024*1024), b''): h.update(b)
    return h.hexdigest()

def echelon(rows, p):
    a = [[int(x) % p for x in row] for row in rows]
    rank = 0; pivots = []; determinant = 1
    if not a: return 0, [], 1
    for c in range(len(a[0])):
        j = next((j for j in range(rank, len(a)) if a[j][c]), None)
        if j is None: continue
        if j != rank: a[rank], a[j] = a[j], a[rank]; determinant = -determinant
        pivot = a[rank][c]; determinant = determinant * pivot % p
        inv = pow(pivot, -1, p)
        a[rank] = [x * inv % p for x in a[rank]]
        for j in range(rank+1, len(a)):
            if a[j][c]:
                f = a[j][c]
                a[j] = [(x-f*y) % p for x,y in zip(a[j],a[rank])]
        pivots.append(c); rank += 1
        if rank == len(a): break
    return rank, pivots, determinant % p

def bareiss(rows):
    a = [list(row) for row in rows]; sign = 1; prev = 1; n = len(a)
    for k in range(n-1):
        j = next((j for j in range(k,n) if a[j][k]), None)
        if j is None: return 0
        if j != k: a[k],a[j] = a[j],a[k]; sign = -sign
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num = a[i][j]*pivot-a[i][k]*a[k][j]
                assert num % prev == 0
                a[i][j] = num//prev
            a[i][k] = 0
        prev = pivot
    return sign*a[-1][-1]

def dominance():
    from forms import permanent_pencil_form
    r=5; rng=random.Random(20260902*1000+r)
    A=[[[rng.randint(-10**6,10**6) for _ in range(3)] for _ in range(3)] for _ in range(r)]
    E=sorted(e for e in it.product(range(4),repeat=r) if sum(e)==3)
    index={e:i for i,e in enumerate(E)}
    base=permanent_pencil_form(A,r)
    J=[]; checked=0
    for k in range(r):
        for a in range(3):
            for b in range(3):
                row=[0]*len(E)
                rr=[i for i in range(3) if i!=a]; cc=[j for j in range(3) if j!=b]
                for pp in it.permutations(cc):
                    for i in range(r):
                        for j in range(r):
                            e=[0]*r; e[k]+=1; e[i]+=1; e[j]+=1
                            row[index[tuple(e)]] += A[i][rr[0]][pp[0]]*A[j][rr[1]][pp[1]]
                B=[[q[:] for q in m] for m in A]; B[k][a][b]+=1
                f=permanent_pencil_form(B,r)
                assert row==[f.get(e,0)-base.get(e,0) for e in E]
                checked+=1; J.append(row)
    transpose=list(map(list,zip(*J)))
    residues={}
    for p in PRIMES:
        rk, piv, _=echelon(transpose,p); assert rk==35
        minor=[[row[c] for c in piv] for row in transpose]
        det=bareiss(minor); assert det and det % p
        residues[str(p)]=dict(rank=rk,parameter_columns=piv,determinant_integer=str(det),determinant_mod_p=det%p)
    assert echelon([[0]*45 for _ in range(35)], PRIMES[0])[0]==0
    save('dominance',dict(status='CERTIFIED',seed=20260902005,box=10**6,pencil=A,exponents=E,
        jacobian=J,values_are='exact integer derivatives; rows=(k,matrix row,matrix column), columns=listed cubic exponents',
        exact_finite_difference_checks=checked,zero_jacobian_control_rank=0,per_prime=residues))

def inventory():
    m=read(ROOT/'results/s79_cert_manifest.json'); rows=[]
    for f in m['files']:
        path=ROOT/f['path']; exists=path.exists()
        x=dict(f,exists=exists)
        if exists:
            x.update(actual_bytes=path.stat().st_size,actual_md5=digest(path,'md5'),sha256=digest(path))
            x['match']=x['actual_bytes']==f['bytes'] and x['actual_md5']==f['md5']
        rows.append(x)
    assert all(f['exists'] and f['match'] for f in rows if f['shipped'])
    mismatches=[f['path'] for f in rows if f['exists'] and not f['match']]
    cubic=[json.loads(l) for l in open(ROOT/'results/s79_per6.jsonl')]
    quartic=[json.loads(l) for l in open(ROOT/'results/s79_cells.jsonl')]
    crecs=[]
    for x in cubic:
        assert set(x['per_prime'])==set(map(str,PRIMES))
        for p in PRIMES:
            pp=x['per_prime'][str(p)]; ats=pp['hybrid']['attempts']
            assert pp['mult']==x['a'] and pp['units']==0
            assert any(z['verified'] and z['rank']==x['a'] and z['projected_nullity']==x['a'] for z in ats)
        available=[f[0] for f in x.get('certs',[]) if (ROOT/f[0]).exists()]
        crecs.append(dict(mu=x['mu'],delta=x['delta'],a=x['a'],N_S=x['N_S'],NS_delta=x['NS_delta'],
            original_seconds=x['secs'],available_fullrank=available,record_status='RECORDED: both primes full; hybrid metadata consistent',
            replay_status='pending' if available else 'requires_regeneration'))
    drops=[]
    for x in quartic:
        assert set(x['per_prime'])==set(map(str,PRIMES))
        for p in PRIMES:
            sides=x['per_prime'][str(p)]['sides']
            assert sides['det']['mult']==sides['per4']['mult']==x['a']
            assert sides['pad']['mult']==sides['red_pts']['mult']==sides['red_star']['mult']
            assert x['D']==sides['pad']['mult']-sides['det']['mult']
            assert x['sides']['det']['per_prime'][str(p)]==x['a']
        if x['mult_red']<x['a']:
            drops.append(dict(lam=x['lam'],delta=x['delta'],a=x['a'],rank_floor=x['mult_red'],
                ideal_dimension_upper_bound=x['a']-x['mult_red'],D_measured=x['D'],membership_certified=False))
    assert len({(tuple(x['lam']),x['delta']) for x in quartic})==len(quartic)==682
    assert len(drops)==59
    stats=collections.Counter((f['shipped'],f['exists']) for f in rows)
    save('inventory',dict(status='SHIPPED HASHES PASS; supplemental mismatches recorded' if mismatches else 'PASS',
        mismatches=mismatches,total=len(rows),present=sum(f['exists'] for f in rows),
        shipped=sum(f['shipped'] for f in rows),missing=sum(not f['exists'] for f in rows),
        counts={str(k):v for k,v in stats.items()},files=rows))
    save('record_ledger',dict(status='PASS',cubic=crecs,quartic_count=682,quartic_full_det_records=682,
        quartic_full_padred_records=623,quartic_sampled_drops=drops,
        higher_degree_drop_count=sum(x['delta']>=10 for x in drops),
        warning='Record verification does not replay an omitted source or evaluation certificate.'))

def census():
    from wk8_s30_pleth import amb, parts, chi
    start=time.monotonic()
    A=amb(9,3,6)
    print('character census',len(A),'seconds',time.monotonic()-start,'cache',chi.cache_info(),flush=True)
    candidates=[x for x in parts(27) if len(x)==6]
    records=[json.loads(l) for l in open(ROOT/'results/s79_per6.jsonl') if json.loads(l)['delta']==9]
    seen={tuple(x['mu']):x['a'] for x in records}
    six={x:a for x,a in A.items() if len(x)==6}
    short={x:a for x,a in A.items() if len(x)<6}
    assert six==seen and len(candidates)==331 and len(six)==210 and sum(six.values())==592
    assert len(short)==365 and sum(short.values())==1213
    save('census',dict(status='CERTIFIED census (ranks separate)',method='exact power-sum plethysm and symmetric-group characters',
        candidates6=len(candidates),positive6=len(six),sum_a6=sum(six.values()),max_a6=max(six.values()),
        short_positive=len(short),short_sum_a=sum(short.values()),
        by_length={str(k):sum(len(x)==k for x in short) for k in range(1,6)},
        rows=[dict(mu=x,a=a,inheritance='dominance' if len(x)<6 else 'six-variable rank required') for x,a in sorted(A.items())],
        seconds=time.monotonic()-start))

def cert(path):
    from hwv import check_vector_shape, is_highest_weight, evaluate
    from points import form_of_point
    c=read(path); cell=c['cell']; p=c['prime']; a=cell['a']; r=cell['r']
    assert p in PRIMES and c['kind']=='full_rank' and cell['n']==3 and cell['delta']==9
    expected={tuple(x['mu']):x['a'] for x in read(OUT/'census.json')['rows']}
    assert expected[tuple(cell['lambda'])]==a
    assert c['conventions']=={'coefficient':'c_alpha(F) = coefficient of s^alpha in F',
        'raising':'E_ij c_alpha = (alpha_i + 1) c_{alpha + e_i - e_j}'}
    basis=[]
    for v in c['basis']:
        vv=[(tuple(tuple(e) for e in term),int(cf)) for term,cf in v['terms']]
        check_vector_shape(vv,3,r,9,cell['lambda'])
        assert is_highest_weight(vv,r,p)[0]
        basis.append(vv)
    assert len(basis)==a
    G=[]
    for q in c['points']:
        assert q['type']==c['variety']=='permanent_pencil'
        F=form_of_point(q,r,3)
        G.append([evaluate(v,F,p) for v in basis])
    rank,pivs,_=echelon(G,p); assert rank==a
    wrong=list(cell['lambda']); wrong[0]+=1; wrong[-1]-=1
    rejected=False
    try: check_vector_shape(basis[0],3,r,9,wrong)
    except ValueError: rejected=True
    assert rejected
    name=Path(path).name.replace('.json.gz','')
    save('replay_'+name,dict(status='CERTIFIED',certificate=str(Path(path).as_posix()),sha256=digest(path),cell=cell,prime=p,
         rank=rank,points=len(G),raising_checks=(r-1)*a,wrong_weight_rejected=rejected,G=G,
         values_are='mod-prime evaluation of the declared plain-coefficient highest-weight polynomials at the shipped integer pencils'))

def stable(path):
    import wk12_int_s79_stable_verify as v
    d=read(path); rho=tuple(d['rho']); mons=[tuple(x) for x in d['monomials']]
    assert len(mons)==len(set(mons))
    order=v.detect_order(mons,rho); assert order is not None
    mine=v.monomials_of(rho); assert mine==set(mons)
    ai=v.a_inf(rho); assert ai==d['a_inf'] and ai in (1,2,3,4)
    assert all(sum(A[k][i][i] for i in range(4))==0 for A in d['points'] for k in range(5))
    integer_values=[]
    for A in d['points']:
        values={}
        for degree in (2,3,4):
            coeff=v.char_poly_coeffs(A,degree)
            for gi,(deg,e) in enumerate(v.GENS):
                if deg==degree: values[gi]=coeff.get(e,0)
        integer_values.append(values)
    results={}
    for p in PRIMES:
        pp=d['per_prime'][str(p)]; K=pp['kernel']
        assert len(K)==ai and all(len(x)==len(mons) for x in K)
        assert echelon(K,p)[0]==ai
        for row in K:
            for i in range(4):
                image=v.apply_E(i,{j:x for j,x in enumerate(row) if x},mons)
                assert not any(x%p for x in image.values())
        G=[]
        for values in integer_values:
            ev=[math.prod(values[gi]%p for gi in m)%p for m in mons]
            G.append([sum(x*y for x,y in zip(ev,row))%p for row in K])
        assert [[-x%p for x in row] for row in G]==pp['G']
        rank=echelon(G,p)[0]; assert rank==ai
        # Alter one coefficient at a monomial with nontrivial raising image.
        j=next(j for j in range(len(mons)) if any(v.apply_E(i,{j:1},mons) for i in range(4)))
        wrong=K[0][:]; wrong[j]=(wrong[j]+1)%p
        assert any(any(x%p for x in v.apply_E(i,{j:x for j,x in enumerate(wrong) if x},mons).values()) for i in range(4))
        results[str(p)]=dict(rank=rank,kernel_rank=ai,raising_checks=4*ai,altered_vector_rejected=True,G=G,
            values_are='mod-prime e_d principal-minor evaluation; global sign -1 relative to stored characteristic-polynomial values at weight 13')
    save('stable_'+'_'.join(map(str,rho)).rstrip('_0'),dict(status='CERTIFIED',source=Path(path).as_posix(),sha256=digest(path),
        rho=rho,a_inf=ai,raw=len(mons),ordering=order,per_prime=results))

def epsilon():
    import wk12_int_s74_final as v
    src=read(ROOT/'results/s74/source.json'); ent=src['entries']; birth=[i for i,e in enumerate(ent) if e['rung']==24]
    assert len(ent)==274 and birth==[273] and all(e['rung']<=23 for e in ent[:273])
    per={}
    for p in PRIMES:
        col=v.load('pad',p); u=[v.msym_u('pad',q)%p for q in col['points']]
        assert u==[x%p for x in col['u_symbol']] and all(u)
        matrix=[[col['rows_native'][str(e['key'])][j]*pow(u[j],24-e['rung'],p)%p for j in range(col['K'])] for e in ent]
        rank,ker=v.kernel(matrix,p); assert rank==269 and len(ker)==5 and all(x[273]==0 for x in ker)
        assert v.kernel(matrix[:273],p)[0]==268
        per[str(p)]=dict(rank_floor=rank,old_modular_rank=268,nullity=5,birth_coefficients=[x[273] for x in ker],
                        u_values=u,values_are='u = 24 times s1^4 coefficient, reduced mod p; rows transported by u^(24-rung)')
    q=math.prod(PRIMES)
    # Ambient basis e0,e1; old subspace span(e0); evaluation row [q,1].
    # Both reductions have kernel span(e0), whereas rational kernel is (1,-q).
    assert all(echelon([[q,1]],p)[0]==1 and q%p==0 for p in PRIMES)
    assert q*1+1*(-q)==0 and math.gcd(1,q)==1
    save('epsilon',dict(status='CONDITIONAL equality retained',per_prime=per,
        counterexample=dict(matrix=[[q,1]],old_subspace='span(e0)',primitive_rational_kernel=[1,-q],
            birth_coordinate=-q,reduction_kernel='span(e0) at both primes'),
        missing='A rational proof that the degree-24 birth row is independent of the transported source after restriction to P; two-prime containment is insufficient.',
        unconditional='D = 1 - i_pad(24), -4 <= D <= 1; exact determinant rank 273 and padded floor 269 retained.'))

def stable_census():
    import wk12_int_s79_stable_verify as v
    from wk8_s30_pleth import parts
    rows=[]
    for rho in parts(13):
        if len(rho)>5: continue
        ai=v.a_inf(rho); assert ai>=0
        rows.append(dict(rho=rho,a_inf=ai))
    wanted={tuple(x['rho']):x['a_inf'] for x in rows if 0<x['a_inf']<=4}
    replay={tuple(x for x in read(p)['rho'] if x):read(p)['a_inf'] for p in OUT.glob('stable_*.json') if p.name not in ('stable_batch.json','stable_census.json')}
    assert wanted==replay and len(wanted)==16
    save('stable_census',dict(status='CERTIFIED',rows=rows,partitions=len(rows),positive_at_most_four=len(wanted),
         counts={str(a):sum(x['a_inf']==a for x in rows) for a in range(5)}))

def coverage():
    ledger=read(OUT/'record_ledger.json')
    records=[json.loads(l) for l in open(ROOT/'results/s79_per6.jsonl')]
    record_index={(tuple(x['mu']),x['delta']):x for x in records}
    d9=[]
    for x in ledger['cubic']:
        if x['delta']!=9: continue
        r=record_index[tuple(x['mu']),9]
        complete=[p for p in x['available_fullrank'] if (OUT/('replay_'+Path(p).name.replace('.json.gz','.json'))).exists()]
        x=dict(x,replayed_certificates=complete,
            status='CERTIFIED: both primes independently replayed' if len(complete)==2 else 'ADOPTED full-rank result; source regeneration required',
            original_fullrank_certificate_count=len(r.get('certs',[])),
            regeneration_arguments=['analysis/wk12_s79_per6.py','9',*map(str,x['mu']),'--a',str(x['a']),
              '--out','results/b13_07/regenerated_per6.jsonl','--certs','results/b13_07/regenerated_certs'])
        d9.append(x)
    missing=[x for x in d9 if len(x['replayed_certificates'])!=2]
    quartic=[json.loads(l) for l in open(ROOT/'results/s79_cells.jsonl')]
    q={(tuple(x['lam']),x['delta']):x for x in read(ROOT/'results/s79_queue.json')}
    stable=[x for x in quartic if (tuple(x['lam']),x['delta']) in q and q[tuple(x['lam']),x['delta']]['a_inf']==x['a']]
    assert len(stable)==69 and len({tuple(x['lam'][1:]) for x in stable})==63
    assert all(x['mult_pad']==x['mult_red']==x['mult_det']==x['mult_per4']==x['a'] for x in stable)
    q1drops=[x for x in ledger['quartic_sampled_drops'] if x['delta']>=10 and (tuple(x['lam']),x['delta']) in q]
    assert len(q1drops)==4 and ledger['higher_degree_drop_count']==35
    manifest=read(OUT/'inventory.json')
    # The original blobs cannot be reconstructed by checking only gzip timestamps.
    # Add canonical-content hashes to identify the actual supplemental objects.
    supplements=[]
    for f in manifest['files']:
        if f['path'] not in manifest['mismatches']: continue
        payload=read(ROOT/f['path'])
        canonical=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
        supplements.append(dict(path=f['path'],actual_sha256=f['sha256'],canonical_json_sha256=hashlib.sha256(canonical).hexdigest(),
            expected_md5=f['md5'],actual_md5=f['actual_md5'],original_bytes=f['bytes'],actual_bytes=f['actual_bytes'],
            kind=payload.get('kind'),source_state='supplemental merged/checkpoint object; original final bytes unavailable'))
    save('coverage',dict(status='VERIFIED PREFIX with explicit regeneration boundary',degree9=d9,
        fully_replayed_weights=210-len(missing),requires_regeneration=len(missing),
        missing_original_certificates=sum(x['original_fullrank_certificate_count'] for x in missing),
        missing_weights_never_had_expanded_certificate=sum(x['original_fullrank_certificate_count']==0 for x in missing),
        original_seconds_for_missing=round(sum(x['original_seconds'] for x in missing),1),
        missing_max_N_S=max(x['N_S'] for x in missing),missing_max_NS_delta=max(x['NS_delta'] for x in missing),
        q1_first_stable_records=69,q1_closed_tail_records=63,
        q1_high_degree_sampled_drops=q1drops,total_high_degree_sampled_drops=35,
        supplemental_hash_mismatches=supplements))

if __name__=='__main__':
    mode,*args=sys.argv[1:]
    {'dominance':dominance,'inventory':inventory,'census':census,'cert':cert,'stable':stable,'epsilon':epsilon,
     'stable_census':stable_census,'coverage':coverage}[mode](*args)
