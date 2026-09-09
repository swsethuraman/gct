"""Independent scalar arithmetic and semantic checks on the delivered certificates."""
from s4 import *
import numpy as np
def determinant_numpy(M,p):
    a=np.array(M,dtype=np.int64)%p;v=1
    for k in range(len(a)):
        nz=np.flatnonzero(a[k:,k]);
        if not len(nz):return 0
        q=k+int(nz[0]);
        if q!=k:a[[q,k]]=a[[k,q]];v=-v
        v=v*int(a[k,k])%p;f=a[k+1:,k]*pow(int(a[k,k]),-1,p)%p
        # Each product < 2^62; each subtraction in (-2^62,2^31), safe int64.
        a[k+1:,k+1:]=(a[k+1:,k+1:]-f[:,None]*a[k,k+1:][None,:])%p
    return v%p
def bareiss(M):
    a=[list(map(int,x)) for x in M];last=1;sign=1
    for k in range(len(a)-1):
        q=next((j for j in range(k,len(a)) if a[j][k]),None)
        if q is None:return 0
        if q!=k:a[k],a[q]=a[q],a[k];sign=-sign
        z=a[k][k]
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):
                num=a[i][j]*z-a[i][k]*a[k][j];assert num%last==0;a[i][j]=num//last
        for i in range(k+1,len(a)):a[i][k]=0
        last=z
    return sign*a[-1][-1] if a else 1
def minor(M,m):return [[M[i][j] for j in m['cols']] for i in m['rows']]
def tiny_prepare():
    jobs=[];exp=[];rng=random.Random(12045000)
    for z in range(4):
        F=s.random_filling(3,4,4,3,4,rng,k=2);forms=[[rng.randint(-3,3) for _ in range(3)] for _ in range(10)];cv=coeffs(forms);sy={t:direct_symbol(forms,t) for t in itertools.combinations_with_replacement(range(3),4)}
        for p in P:
            jid=f'tiny_{z}_{p}';j=s.pack_job(F,cv,p,jid);v=s.brute_force_eval(F,s.symbols_from_coeffs(cv,4,3,p),p)
            jobs.append(dict(id=jid,primary=j,independent=ind_pack(F,sy,p,j['order'])))
            exp.append(dict(id=jid,filling=F.to_json(),forms=forms,literal_value=v))
    write(ROOT/'scratch/tiny_00.json',jobs);write(A/'tiny_literal.json',exp)
def all_checks():
    checks=[]
    target=read(A/'padded_certificate.json')
    for q in target['results']:
        p=q['prime'];M=minor(q['target_matrix'],q['minor']);d=bareiss(M)%p;assert d==q['minor']['det']!=0
        checks.append(dict(check='target 12-minor integer Bareiss on residues',prime=p,value=d))
    ctrl=read(A/'s64_control.json');m=ctrl['raising_minor'];rows=[dict(x) for x in ctrl['raising_rows']]
    sub=[[rows[i].get(j,0) for j in m['cols']] for i in m['rows']];d=determinant_numpy(sub,P[0]);assert d!=0
    assert d==math.prod(m['triangular_pivots'])%P[0]
    checks.append(dict(check='559-minor independent elimination',prime=P[0],value=d))
    for q in ctrl['evaluations']:
        d=bareiss(minor(q['matrix'],q['minor']))%q['prime'];assert d==q['minor']['det']!=0
        checks.append(dict(check='s64 control '+q['family'],prime=q['prime'],value=d))
    dim=read(A/'r6_parametrization.json')
    for q in dim['checks']:
        for fam in ['pad','red']:
            d=bareiss(minor(dim[fam+'_jacobian'],q[fam]))%q['prime'];assert d==q[fam]['det']!=0
            checks.append(dict(check='r6 '+fam+' Jacobian minor',prime=q['prime'],value=d))
    n3=read(A/'n3_control.json')
    for q in n3['results']:
        d=bareiss(minor(q['matrix'],q['minor']))%q['prime'];assert d==q['minor']['det']!=0
        checks.append(dict(check='n3 '+q['family'],prime=q['prime'],value=d))
    tiny=read(A/'tiny_literal.json');tv={q['id']:q for q in read(ROOT/'scratch/tiny_values_00.json')}
    for q in tiny:assert q['literal_value']==tv[q['id']]['value']==tv[q['id']]['independent']
    checks.append(dict(check='literal full contractions vs both C# evaluators',count=len(tiny)))
    write(A/'independent_checks.json',checks);print('Independent arithmetic and tiny literal checks PASS:',len(checks))
def transforms():
    src=read(A/'source.json');perms=[]
    for v in src['vectors']:
        f=copy.deepcopy(v['native_filling'])
        for l in range(f['delta'],24):f['one'] += [l]*4
        f['delta']=24;F=s.Filling.from_json(f);assert F.lam==(65,17)+(2,)*7
        columns=[F.C1,F.C2]+[list(t) for t in F.two]+[[x] for x in F.one]
        counts=[0]*24;pi=[]
        for c in columns:
            for l in c:pi.append(4*l+counts[l]);counts[l]+=1
        assert sorted(pi)==list(range(96))
        perms.append(dict(index=v['index'],literal_target_filling=F.to_json(),column_slots_to_quartic_slots=pi,scalar_numerator=1,scalar_denominator=24**v['u_power']))
    sigma=[72+l if a==0 else 3*l+a-1 for l in range(24) for a in range(4)]
    write(A/'source_coordinate_transforms.json',{'scalar_meaning':'normalized target vector = scalar times literal target filling polynomial','quartic_to_cubic_first_linear_last':sigma,'tensor_split_scalar':4**24,'row_order':'34 archived ladder rows; independently certified minor uses only rows 0 through 11','vectors':perms})
if __name__=='__main__':
    if sys.argv[1:] == ['tiny']:tiny_prepare()
    else:all_checks();transforms()
