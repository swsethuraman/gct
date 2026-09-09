"""Exact small-control reconstruction, split identity and sample-variety audit."""
from s4 import *
from fractions import Fraction
def reconstruct(x,p):
    if x==0:return Fraction(0)
    r0,r1=p,x;t0,t1=0,1;limit=math.isqrt(p//2)
    while abs(r1)>limit:
        q=r0//r1;r0,r1=r1,r0-q*r1;t0,t1=t1,t0-q*t1
    if t1<0:r1,t1=-r1,-t1
    assert t1>0 and t1<=limit and (r1-x*t1)%p==0
    return Fraction(r1,t1)
def primitive(v,p):
    v=[reconstruct(x,p) for x in v];d=math.lcm(*(x.denominator for x in v));z=[int(d*x) for x in v];g=math.gcd(*z)
    return [x//g for x in z]
def nullspace(rows,n,p):
    piv={};original=[];pivotrows=[];pivotcols=[];diag=[]
    for rowid,row in enumerate(rows):
        r={j:v%p for j,v in row.items() if v%p}
        while r:
            j=min(r);v=r[j]
            if j not in piv:
                diag.append(v);iv=pow(v,-1,p);piv[j]={k:x*iv%p for k,x in r.items()};pivotrows.append(rowid);pivotcols.append(j);break
            for k,x in piv[j].items():
                y=(r.get(k,0)-v*x)%p
                if y:r[k]=y
                elif k in r:del r[k]
    free=[j for j in range(n) if j not in piv];kernel=[]
    for f in free:
        v=[0]*n;v[f]=1
        for j in sorted(piv,reverse=True):v[j]=-sum(x*v[k] for k,x in piv[j].items() if k!=j)%p
        kernel.append(v)
    return kernel,{'rank':len(piv),'rows':pivotrows,'cols':pivotcols,'triangular_pivots':diag,'free':free}
def raising(basis,exponents,r):
    rows={};labels=[]
    for j,m in enumerate(basis):
        for i in range(r-1):
            for index,count in collections.Counter(m).items():
                al=exponents[index]
                if al[i+1]==0:continue
                be=list(al);be[i]+=1;be[i+1]-=1
                t=list(m);t.remove(index);t.append(exponents.index(tuple(be)));key=(i,tuple(sorted(t)))
                if key not in rows:rows[key]={};labels.append(key)
                rows[key][j]=rows[key].get(j,0)+count*(al[i]+1)
    return list(rows.values()),labels
def ev(v,basis,cv,p):return sum(x*math.prod(cv[k] for k in m) for x,m in zip(v,basis))%p
def small_control():
    e=s.exps(4,3);lam=(8,8,8);basis=[m for m in itertools.combinations_with_replacement(range(len(e)),6) if tuple(sum(e[k][i] for k in m) for i in range(3))==lam]
    rows,labels=raising(basis,e,3);print('small raising dimensions',len(rows),len(basis),flush=True)
    ker,minor=nullspace(rows,len(basis),P[0]);assert len(ker)==2
    vectors=[primitive(v,P[0]) for v in ker]
    assert all(sum(row.get(j,0)*v[j] for j in row)==0 for row in rows for v in vectors)
    assert s.rank_minor(vectors,P[0])['rank']==2
    survive=[j for j,m in enumerate(basis) if all(e[k][0]>0 for k in m)]
    restricted=[[v[j] for j in survive] for v in vectors];rm=s.rank_minor(restricted,P[0]);assert rm['rank']==1
    pivot=rm['cols'][0];u=[restricted[1][pivot],-restricted[0][pivot]];g=math.gcd(*u);u=[x//g for x in u]
    assert all(sum(u[i]*restricted[i][j] for i in range(2))==0 for j in range(len(survive)))
    pts=[];results=[]
    for family in ['det','red','pad']:
        for j in range(3):
            seed=12041000+100*['det','red','pad'].index(family)+j;rng=random.Random(seed)
            if family=='det':cv,parameters=s.pencil(4,3,seed)
            elif family=='pad':parameters=[[rng.randint(-3,3) for _ in range(3)] for _ in range(10)];cv=coeffs(parameters)
            else:
                ell=[rng.randint(-4,4) for _ in range(3)];cube=[rng.randint(-4,4) for _ in s.exps(3,3)];co=collections.defaultdict(int)
                for b,c in zip(s.exps(3,3),cube):
                    for k,y in enumerate(ell):z=list(b);z[k]+=1;co[tuple(z)]+=c*y
                cv=[co[a] for a in e];parameters={'ell':ell,'cubic':cube}
            pts.append(dict(family=family,index=j,seed=seed,parameters=parameters,coefficients=cv))
        for p in P:
            mat=[[ev(v,basis,x['coefficients'],p) for x in pts if x['family']==family] for v in vectors]
            rank=s.rank_minor(mat,p);assert rank['rank']==(2 if family=='det' else 1)
            results.append(dict(family=family,prime=p,matrix=mat,minor=rank))
    write(A/'s64_control.json',dict(cell={'n':4,'r':3,'degree':6,'lambda':lam},exponents=e,basis=basis,raising_rows=[sorted(x.items()) for x in rows],raising_labels=labels,raising_minor=minor,source_vectors=vectors,source_rank_minor=s.rank_minor(vectors,P[0]),exact_raising_checks='all zero over Z',fixed_factor_columns=survive,split_rank_minor=rm,kernel_source_coordinates=u,points=pts,evaluations=results))
    print('small control exact source 2, det 2, red 1, pad 1; kernel',u,flush=True)
def dimensional():
    r=6;rng=random.Random(12042000);forms=[[rng.randint(-4,4) for _ in range(r)] for _ in range(10)];base=coeffs(forms);rows=[]
    # The polynomial is affine in each individual frame parameter, so difference is EXACT derivative.
    for k in range(10):
        for i in range(r):
            ff=copy.deepcopy(forms);ff[k][i]+=1;cc=coeffs(ff);rows.append([x-y for x,y in zip(cc,base)])
    ell=[rng.randint(-4,4) for _ in range(r)];cube=[rng.randint(-4,4) for _ in s.exps(3,r)];exp=s.exps(4,r);rr=[]
    for i in range(r):
        row=[0]*len(exp)
        for b,c in zip(s.exps(3,r),cube):z=list(b);z[i]+=1;row[exp.index(tuple(z))]=c
        rr.append(row)
    for b in s.exps(3,r):
        row=[0]*len(exp)
        for i,y in enumerate(ell):z=list(b);z[i]+=1;row[exp.index(tuple(z))]=y
        rr.append(row)
    checks=[]
    for p in P:
        m=s.rank_minor(rows,p);n=s.rank_minor(rr,p);assert (m['rank'],n['rank'])==(55,61)
        checks.append(dict(prime=p,pad=m,red=n))
    write(A/'r6_parametrization.json',dict(seed=12042000,pad_forms=forms,red_ell=ell,red_cubic=cube,exponents=exp,pad_jacobian=rows,red_jacobian=rr,checks=checks))
    print('r6 tangent lower bounds 55 and 61 at both primes',flush=True)
def blocks():
    lam=(65,17)+(2,)*7;out=[]
    for mu in itertools.product(*(range((lam+(0,))[i+1],lam[i]+1) for i in range(9))):
        if sum(mu)==72:out.append(tuple(x for x in mu if x))
    log=(ROOT/'inputs/snapshot/results/logs/hpad_lmr.log').read_text()
    old=[]
    for line in log.splitlines():
        m=re.search(r'mu=(\([^)]*\)).*a_3=(\d+)',line)
        if m:old.append((ast.literal_eval(m[1]),int(m[2])))
    assert len(out)==48 and [x[0] for x in old]==out and sum(x[1] for x in old)==521
    offset=0;ledger=[]
    for i,(mu,dim) in enumerate(old):
        ledger.append(dict(block=i+1,mu=mu,cubic_degree=24,inherited_dimension=dim,row_offset=offset,multiplicity_indices=list(range(dim)),new_split_rank_lower_bound=0,new_permanent_rank_lower_bound=0,permanent_kernel='NOT COMPUTED' if dim else 'zero if inherited dimension is accepted',status='index independently enumerated; multiplicity source-reported; no block rank computed'))
        offset+=dim
    write(A/'48_block_ledger.json',ledger)
    lines=['| block | mu | inherited a3 | row interval (zero-based, half-open) | S block / permanent rank |','|---:|---|---:|---|---|']
    for x in ledger:lines.append(f'| {x["block"]} | {tuple(x["mu"])} | {x["inherited_dimension"]} | [{x["row_offset"]},{x["row_offset"]+x["inherited_dimension"]}) | OPEN / OPEN |')
    (A/'48_block_ledger.md').write_text('\n'.join(lines)+'\n')
    rows=[json.loads(x) for x in (ROOT/'inputs/snapshot/results/s64_calibration_unified.jsonl').read_text().splitlines()]
    summary={'rows':len(rows),'padded_differs_reducible':[x for x in rows if x['mult_pad']!=x['mult_red']],'padded_differs_determinant':[x for x in rows if x['mult_pad']!=x['mult_det']]}
    assert len(summary['padded_differs_reducible'])==0 and len(summary['padded_differs_determinant'])==12
    write(A/'calibration_inventory.json',summary)
    print('48 block indices; inherited sum 521; s64 pad/red differences 0, pad/det differences 12')
def archived_kernel():
    bank=json.load(gzip.open(ROOT/'inputs/snapshot/results/s64_kern/kern_8_4_4_4_4_d6.json.gz','rt'))
    terms=bank['U_terms']['pad'][0]['terms'];rats=[reconstruct(c,P[0]) for _,c in terms]
    den=math.lcm(*(x.denominator for x in rats));ints=[int(x*den) for x in rats];g=math.gcd(*ints);ints=[x//g for x in ints]
    exponent=s.exps(4,5);index={e:i for i,e in enumerate(exponent)};monos=[tuple(index[tuple(e)] for e in m) for m,c in terms]
    rows,labels=raising(monos,exponent,5)
    assert all(sum(v*ints[j] for j,v in row.items())==0 for row in rows)
    assert not any(all(exponent[k][0]>0 for k in m) for m in monos)
    evals=[]
    for j in range(2):
        seed=12043000+j;rng=random.Random(seed);forms=[[rng.randint(-3,3) for _ in range(5)] for _ in range(10)];cv=coeffs(forms)
        detcv,detpencil=s.pencil(4,5,seed)
        vals=[{'prime':p,'pad':ev(ints,monos,cv,p),'det':ev(ints,monos,detcv,p)} for p in P]
        assert all(v['pad']==0 and v['det']!=0 for v in vals)
        evals.append(dict(seed=seed,pad_forms=forms,det_pencil=detpencil,pad_coefficients=cv,det_coefficients=detcv,values=vals))
    obj={'cell':bank['cell'],'exponents':exponent,'monomials':monos,'primitive_integer_coefficients':ints,'reconstruction_common_denominator':den,'integer_gcd_before_primitive':g,'exact_raising_row_count':len(rows),'exact_raising_result':'zero over Z','fixed_factor_surviving_terms':0,'archived_modular_source_coordinates':[1,0],'rational_to_archived_scalar_mod_p1':g*pow(den,-1,P[0])%P[0],'points':evals}
    with gzip.open(A/'s64_r5_exact_kernel.json.gz','wt',encoding='utf8') as f:json.dump(obj,f)
    print('r5 archived kernel lifted and proved over Q:',len(ints),'terms, denominator',den,'max coeff',max(map(abs,ints)),flush=True)
def n3_control():
    b=read(ROOT/'inputs/snapshot/results/s69_n3_d12.json');fs=[s.Filling.from_json(x) for x in b['basis']];pts=[];results=[]
    ideal=[66,-972,12,-37,4,320]
    for fam in ['det','unpadded_per3']:
        cvs=[]
        for j in range(7):
            seed=12044000+100*int(fam=='unpadded_per3')+j;cv,pp=s.pencil(3,7,seed,fam=='unpadded_per3');cvs.append(cv);pts.append(dict(family=fam,index=j,seed=seed,pencil=pp,coefficients=cv))
        for p in P:
            mat=[[s.fast_eval_py(F,s.symbols_from_coeffs(cv,3,7,p),p) for cv in cvs] for F in fs];minor=s.rank_minor(mat,p)
            assert minor['rank']==(5 if fam=='det' else 6)
            if fam=='det':assert all(sum(ideal[i]*mat[i][j] for i in range(6))%p==0 for j in range(7))
            results.append(dict(family=fam,prime=p,matrix=mat,minor=minor))
    write(A/'n3_control.json',dict(fillings=[F.to_json() for F in fs],ideal_source_coordinates=ideal,global_det_upper_bound='inherited n3 LMR/banked ideal identity; finite evaluations are only a consistency check',points=pts,results=results))
    print('fresh n3 control: unpadded per3 rank 6, determinant rank 5 at both primes',flush=True)
if __name__=='__main__':blocks();small_control();dimensional();archived_kernel();n3_control()
