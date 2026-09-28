#!/usr/bin/env python3
"""Exact rational price audit, historical record comparison, and timer audit.
No source matrix is built. All mathematical input comes from committed blobs.
"""
import ast
from fractions import Fraction as Q
import hashlib
import json
import pathlib
import resource
import subprocess
import time

WT=pathlib.Path('/mnt/c/Users/swami/Projects/gct-gpt/work/batch28/b28-01r')
OUT=WT/'results/b28_01r'
HOST=pathlib.Path.home()/'b28_01'
TIP='a1c3c3a69b789c91909ed5476354ad762f3e71c2'
BASE='96a8074d'
GIT=['git','--git-dir=/mnt/c/Users/swami/Projects/gct-gpt/work/batch15/.git']
inputs={}

def digest(b): return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def blob(ref,p):
    b=subprocess.check_output(GIT+['show',ref+':'+p]); inputs[ref+':'+p]=digest(b); return b
def data(ref,p): return json.loads(blob(ref,p),parse_float=Q)
def plain(x):
    if isinstance(x,Q): return str(x)
    if isinstance(x,dict): return {k:plain(v) for k,v in x.items()}
    if isinstance(x,list): return [plain(v) for v in x]
    return x
def save(name,obj): (OUT/name).write_text(json.dumps(plain(obj),indent=2,sort_keys=True)+'\n')
def fixed(x,d=3):
    v=round(x*10**d); return ('-' if v<0 else '')+str(abs(v)//10**d)+'.'+str(abs(v)%10**d).zfill(d)
def model(r,n,k,a,z,u):
    return dict(B=r['cB']*n*k,S=r['cS']*z,H=r['cH']*z*u,V=r['cV']*(a+8)*n*k,
                R=r['cR']*(a+8)*n*a,D=r['cD']*u**3)
def envelope(n,a,z,u): return 16*n*a+100*z+400*n+5*max(250000000,128*n)+80*u*u+500000000

def main():
    t=time.monotonic()
    comparisons=[]
    for dirname,lam,d,record_path in [('control',[22,6,5,2,1],9,'results/s71_sweep.jsonl'),
                                     ('cal1',[24,6,5,3,2],10,'results/s71_sweep.jsonl'),
                                     ('cal2',[13,9,9,3,1,1],9,'results/s79_cells.jsonl')]:
        lines=blob(BASE,record_path).splitlines(keepends=True)
        matches=[(i+1,b,json.loads(b)) for i,b in enumerate(lines) if json.loads(b).get('lam')==lam and json.loads(b).get('delta')==d]
        assert len(matches)==1
        lineno,line,rec=matches[0]
        tag='_'.join(map(str,lam))+f'_d{d}'
        c=data(TIP,f'results/b28_01/{dirname}/{tag}_cell.json')
        fields={}
        for new,old in [('a','a'),('N_S','N_S'),('stab','stab'),('n_chi','n_chi'),('rows_E','nrows'),('nnz_E','nnz')]:
            assert c[new]==rec[old]; fields[new]=c[new]
        for key in ('size','order','stats'): assert c['cover'][key]==rec['cover_E'][key]
        certs=[]
        for p in ([2147483647,2147483629] if dirname=='control' else [2147483647]):
            cert=data(TIP,f'results/b28_01/{dirname}/{tag}_p{p}_cert.json')
            hy=cert['hybrid']; oldhy=rec['per_prime'][str(p)]['hybrid']
            assert cert['evaluation']['mult_det']==rec['per_prime'][str(p)]['sides']['det']['mult']==c['a']
            assert hy['source_gate'] and hy['projected_nullity']==c['a']
            assert hy['nU']==oldhy['nU'] and hy['projection']['m']==oldhy['attempts'][0]['m']
            certs.append(dict(prime=p,mult_det=cert['evaluation']['mult_det'],nU=hy['nU'],m=hy['projection']['m'],
                              actual_ublock=hy['ublock'],historical_ublock=oldhy.get('ublock'),nblocks=hy['nblocks']))
        comparisons.append(dict(cell=tag,source=BASE+':'+record_path,line=lineno,raw_line=digest(line),fields=fields,
                                cover=c['cover'],prime_checks=certs,match=True))
    save('RECORD_COMPARISON.json',dict(evidence='READ committed records; COMPUTED equality checks',cells=comparisons))

    rates=data(TIP,'results/b28_01/host_rates.json'); price=data(TIP,'results/b28_01/cellA_price.json')
    gate=data(TIP,'results/b28_01/gate_rates.json')
    derived={}; stored_rate_errors=[]
    for name,tag in [('cal1','24_6_5_3_2_d10'),('cal2','13_9_9_3_1_1_d9')]:
        c=data(TIP,f'results/b28_01/{name}/{tag}_cell.json')
        rc=data(TIP,f'results/b28_01/{name}/{tag}_receipt.json')
        vr=data(TIP,f'results/b28_01/{name}/{tag}_p2147483647_verify_receipt.json')
        p={x['phase']:x for x in rc['phases']}; v={x['phase']:x for x in vr['phases']}
        n,k,a,z,u=c['n_chi'],c['delta'],c['a'],c['nnz_E'],c['cover']['nU']
        rp=dict(cB=p['build']['secs']/(n*k),cS=p['cover']['secs']/z,
                cH=(p['schur']['secs']-p['schur']['nullspace_secs']+p['lift_check']['secs'])/(z*u),
                cD=max(Q(5,10**10),p['schur']['nullspace_secs']/u**3),
                cV=p['evaluation']['secs']/((a+8)*n*k),cR=p['evaluation']['secs']/((a+8)*n*a))
        rv=dict(cB=v['build']['secs']/(n*k),cS=v['cover']['secs']/z,
                cH=(v['schur']['secs']+v['lift_check']['secs'])/(z*u),cD=Q(5,10**10),
                cV=v['evaluation']['secs']/((a+8)*n*k),cR=v['evaluation']['secs']/((a+8)*n*a))
        derived[name]=dict(producer=rp,verifier=rv)
        for side,r in [('producer',rp),('verifier',rv)]:
            for key,value in r.items():
                stored_rate_errors.append(dict(cell=name,side=side,coefficient=key,exact_from_receipt=value,
                    stored_decimal=rates['per_cell'][name]['rates_'+side][key],
                    decimal_representation_error=rates['per_cell'][name]['rates_'+side][key]-value))
    exact_host={side:{key:max(derived[c][side][key] for c in derived) for key in derived['cal1'][side]}
                for side in ('producer','verifier')}
    rows=[]
    n,k,a=813314,8,109
    for row in price['scenarios']:
        z=row['z']; u=row['U']
        assert z==row['z_over_n']*n and u==a+-((-row['f']*n).numerator//(-row['f']*n).denominator)
        pm=model(rates['producer'],n,k,a,z,u); vm=model(rates['verifier'],n,k,a,z,u)
        pp=sum(pm[q] for q in ('H','V','R','D')); prod=pm['B']+pm['S']+2*pp; ver=sum(vm.values())
        exact_pm=model(exact_host['producer'],n,k,a,z,u); exact_vm=model(exact_host['verifier'],n,k,a,z,u)
        exact_prod=exact_pm['B']+exact_pm['S']+2*sum(exact_pm[q] for q in ('H','V','R','D'))
        exact_total=exact_prod+sum(exact_vm.values())
        assert round(prod,1)==row['producer_secs'] and round(ver,1)==row['verifier_secs']
        assert round(prod+ver,1)==row['total_secs'] and round((prod+ver)/3600,3)==row['total_hours']
        assert round(exact_total/3600,3)==row['total_hours']
        env=envelope(n,a,z,u); assert env==row['mem_envelope_bytes']
        gate_ver=gate['verifier_factor']*sum(pm.values())
        rows.append(dict(z_over_n=row['z_over_n'],f=row['f'],U=u,price_hours=fixed((prod+ver)/3600),
            mem_envelope_bytes=env,gate_verifier_seconds=fixed(gate_ver),phasewise_verifier_seconds=fixed(ver),
            verifier_underpricing_seconds=fixed(ver-gate_ver),gate_underprices_verifier=gate_ver<ver,
            exact_total_from_receipts_seconds=exact_total,all_published_roundings_match=True))
    c=rates['per_cell']['cal2']; e=envelope(c['n'],c['a'],c['z'],c['U'])
    save('PRICE_AUDIT.json',dict(evidence='COMPUTED exact Fraction arithmetic on committed decimal receipts/rates',
        note='Scenario estimates, not confidence intervals or measured Cell A costs. No Cell A build.',
        rows=rows,exact_host_rates=exact_host,rate_decimal_errors=stored_rate_errors,
        gate_factor=gate['verifier_factor'],max_phase_ratio=max(rates['verifier'][q]/rates['producer'][q] for q in rates['producer']),
        calibration2=dict(envelope_bytes=e,verifier_observed_peak_bytes=max(c['verifier_peak_bytes'].values()),
            verifier_peak_exceeds_envelope=max(c['verifier_peak_bytes'].values())>e)))

    receipt=data(TIP,'results/b28_01/RESOURCE_RECEIPT.json'); timer=[]
    for name in ('b28_01_driver.py','b28_01_verify.py'):
        old=(HOST/'superseded_v1/frozen'/name).read_bytes(); new=blob(TIP,'analysis/'+name)
        assert digest(old)['sha256']==receipt['frozen_code_v1_sha256_superseded'][name]
        assert old.replace(b'time.time()',b'time.perf_counter()')==new
        timer.append(dict(name=name,v1=digest(old),v2=digest(new),changed_calls=old.count(b'time.time()'),only_timer_replacement=True))
    manifest=data(TIP,'results/b28_01/MANIFEST.json'); pair=[]
    allentries={e['path']:e for e in manifest['payloads']}
    for p,e in allentries.items():
        if p.startswith('results/b28_01/superseded_v1/out/') and not p.endswith('_receipt.json'):
            now='results/b28_01/'+p.split('/out/',1)[1]
            assert (e['bytes'],e['sha256'])==(allentries[now]['bytes'],allentries[now]['sha256'])
            pair.append(dict(old=p,new=now,sha256=e['sha256'],bytes=e['bytes']))
    save('TIMER_AUDIT.json',dict(evidence='COMPUTED byte comparisons; v1 host bytes bound by committed receipt',
         code=timer,mathematical_output_pairs=pair,all_equal=True))
    verifier=blob(TIP,'analysis/b28_01_verify.py').decode(); tree=ast.parse(verifier)
    imports=[]
    for node in ast.walk(tree):
        if isinstance(node,ast.Import): imports.extend(a.name for a in node.names)
        if isinstance(node,ast.ImportFrom): imports.append(node.module)
    assert not any(x.startswith(('wk','b28_01_driver')) for x in imports)
    bounds=dict(float64_limb_sum=(2**21-1)*65535**2,float64_integer_limit=2**53,
        verifier_int64_limb_sum=2**15*65535*(2147483647-1),verifier_claimed_limit=2**62,
        sparse_kernel_limb_abs_sum=813314*65535**2,int64_limit=2**63,
        projection_product_abs_sum=8*(32*813314)*65535,
        max_residue_product_plus_residue=(2147483647-1)**2+(2147483647-1),
        target_baseL_key_bound=70**8,calibration2_baseL_key_bound=126**9)
    assert bounds['float64_limb_sum']<2**53
    assert bounds['verifier_int64_limb_sum']<2**62
    assert all(bounds[q]<2**63 for q in ('sparse_kernel_limb_abs_sum','projection_product_abs_sum',
        'max_residue_product_plus_residue','target_baseL_key_bound','calibration2_baseL_key_bound'))
    save('ARITHMETIC_AUDIT.json',dict(evidence='COMPUTED integer bounds; HAND inequalities explained in review',
        bounds=bounds,verifier_imports=sorted(set(imports)),producer_imports_absent=True))
    save('AUDIT_INPUTS.json',inputs)
    names=['RECORD_COMPARISON.json','PRICE_AUDIT.json','TIMER_AUDIT.json','ARITHMETIC_AUDIT.json','AUDIT_INPUTS.json']
    save('audit_receipt.json',dict(command='timeout 60 bash -c "ulimit -v 500000; exec python3 analysis/b28_01r_audit.py"',
        script=digest(pathlib.Path(__file__).read_bytes()),outputs={p:digest((OUT/p).read_bytes()) for p in names},
        input_bindings=digest((OUT/'AUDIT_INPUTS.json').read_bytes()),wall_seconds=time.monotonic()-t,
        maxrss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,timeout_seconds=60,address_limit_kib=500000))
    print(json.dumps(dict(records_match=True,price_roundings_match=True,timer_only_change=True,v1_pairs=len(pair),
                          gate_underprices_rows=sum(x['gate_underprices_verifier'] for x in rows))))

if __name__=='__main__': main()
