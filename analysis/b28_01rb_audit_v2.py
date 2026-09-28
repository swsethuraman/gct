#!/usr/bin/env python3
"""Audit the durable raw replay hashes and committed gate arithmetic; no cell builds.

The initial follow-up audit found temporary replay files unavailable. All replay
bytes had already been hashed in replay_receipt.json. Compare those raw hashes
directly to the bound manifests; recover small evidence blobs from the producer
commit only after proving their hashes equal the replay hashes.
"""
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
import resource
import subprocess
import time

ROOT=Path('/mnt/c/Users/swami/Projects/gct-gpt')
WT=ROOT/'work/batch28/b28-01r'
OUT=WT/'results/b28_01rb'
RUN=Path('/tmp/b28_01rb_replay_5a3174cd')
TIP='5a3174cd3a1ec96b05b92a8bcb73fbee58c0544b'
OLD='a1c3c3a69b789c91909ed5476354ad762f3e71c2'
GIT=['git','--git-dir='+str(ROOT/'work/batch15/.git')]
inputs={}
def digest(b): return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def fd(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''): h.update(b)
    return dict(bytes=p.stat().st_size,sha256=h.hexdigest())
def blob(ref,p):
    b=subprocess.check_output(GIT+['show',ref+':'+p])
    inputs[ref+':'+p]=digest(b)
    return b
def J(ref,p,exact=False): return json.loads(blob(ref,p),parse_float=Q if exact else float)
def save(p,o): p.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def flat(o,p=''):
    if isinstance(o,dict):
        r={}
        for k,v in o.items(): r.update(flat(v,p+'.'+k if p else k))
        return r
    return {p:o}
def diff(a,b):
    a,b=flat(a),flat(b)
    return dict(added={k:b[k] for k in sorted(b.keys()-a.keys())},removed={k:a[k] for k in sorted(a.keys()-b.keys())},changed={k:dict(old=a[k],new=b[k]) for k in sorted(a.keys()&b.keys()) if a[k]!=b[k]})
def vmem(n,NS,k,a,z,rows,U,S,ro,zR,zF):
    m=U+64; w=max(1,250000000//(8*max(S,1))); nnz=min(m*n,8*zF)
    base=500000000+NS*(4*k+24)+12*z+8*rows
    terms=dict(build=64*NS*k+12*z,schur_A=76*zR+12*zF+512*ro+48*nnz,schur_B=76*zR+12*zF+96*ro+12*nnz+8*m*U+500000000+32*m*w,schur_C=72*m*U,lift=4*n*a+640*rows+384*n,eval=20*n*a+64*n+NS*(4*k+32))
    return base+max(terms.values())
def envelope(n,a,z,U): return 16*n*a+100*z+400*n+5*max(250000000,128*n)+80*U*U+500000000
def phases(n,k,a,z,U,r):
    weights=dict(cB=n*k,cS=z,cH=z*U,cV=(a+8)*n*k,cR=(a+8)*n*a,cD=U**3)
    return {c:r[c]*weights[c] for c in weights}
def main():
    start=time.monotonic()
    replay=json.loads((OUT/'replay_receipt.json').read_text())
    assert replay['rc']==0
    fresh={e['path']:{k:e[k] for k in ('bytes','sha256')} for e in replay['outputs']}
    manifests={ref:{e['path']:{k:e[k] for k in ('bytes','sha256')} for e in J(ref,'results/b28_01'+('c' if ref==TIP else '')+'/MANIFEST.json')['files' if ref==TIP else 'payloads']} for ref in (OLD,TIP)}
    retained={ref:{e['host_path']:{k:e[k] for k in ('bytes','sha256')} for e in J(ref,'results/b28_01'+('c' if ref==TIP else '')+'/HOST_RETAINED.json')['files']} for ref in (OLD,TIP)}
    def expected(ref,folder,name):
        prefix='results/b28_01c/out_c/' if ref==TIP else 'results/b28_01/'
        path=prefix+folder+'/'+name
        if path in manifests[ref]: return manifests[ref][path]
        return retained[ref][('out_c/' if ref==TIP else 'out/')+folder+'/'+name]
    reg=[]; jd=[]
    for folder,tag,primes in [('control','22_6_5_2_1_d9',[2147483647,2147483629]),('cal2','13_9_9_3_1_1_d9',[2147483647])]:
        names=[tag+'_pencils.json']+[tag+'_cover_'+s+'.npy' for s in ('S','U','rows')]+[tag+'_p'+str(p)+'_'+s+'.u32' for p in primes for s in ('K','VK')]
        for name in names:
            got=fresh[folder+'/'+name]
            a=expected(OLD,folder,name); c=expected(TIP,folder,name)
            assert got==a==c,(folder,name)
            reg.append(dict(path=folder+'/'+name,old=a,repair=c,replay=got,unchanged=True))
        for name in [tag+'_cell.json']+[tag+'_p'+str(p)+'_'+s+'.json' for p in primes for s in ('cert','verify')]:
            cpath='results/b28_01c/out_c/'+folder+'/'+name
            raw=blob(TIP,cpath)
            assert digest(raw)==fresh[folder+'/'+name]==expected(TIP,folder,name),name
            old=J(OLD,'results/b28_01/'+folder+'/'+name)
            new=json.loads(raw); d=diff(old,new)
            allowed={'schema','verdict'} if name.endswith('_verify.json') else {'schema'}
            assert not d['removed'] and set(d['changed'])<=allowed,(name,d)
            jd.append(dict(path=folder+'/'+name,repair_and_replay_identical=True,old_to_repair=d))
    # Every fresh deterministic certificate, fixture, matrix and kernel vs repair bytes.
    comparisons=[]; kept=[]; host=[]
    roots=['control','cal2','corrupt','malformed_missing_minor','malformed_wrong_recipe','deficiency','deficiency_corrupted','source_gate','disagreement']
    for folder in roots:
        for rel in sorted(k for k in fresh if k.startswith(folder+'/')):
            p=Path(rel)
            if 'receipt' in p.name: continue
            got=fresh[rel]; want=expected(TIP,folder,p.name)
            assert got==want,rel
            comparisons.append(dict(path=rel,**got,repair_identical=True))
            if p.suffix=='.json':
                raw=blob(TIP,'results/b28_01c/out_c/'+rel)
                assert digest(raw)==got
                dst=OUT/'replay'/rel; dst.parent.mkdir(parents=True,exist_ok=True); dst.write_bytes(raw)
                kept.append(str(dst.relative_to(OUT)))
            else: host.append(dict(original_temporary_path=str(RUN/rel),**got))
    save(OUT/'REGRESSION.json',dict(evidence='COMPUTED raw hashes taken by the replay runner before exit, compared with committed raw hashes; committed JSON analyzed after matching its replay hash',small_evidence_provenance='results/b28_01rb/replay JSON files are committed producer blobs recovered after proving raw hash equality to fresh replay output, not direct file copies',binary_and_pencil_comparisons=reg,json_comparisons=jd,all_fresh_deterministic_comparisons=comparisons,all_match=True))
    save(OUT/'TEMPORARY_OUTPUTS.json',dict(hash_convention='raw bytes',root=str(RUN),availability='Temporary replay files were unavailable at follow-up audit. Hashes and all command/control receipts were durably saved before replay exit. No large-file retention is claimed; producer-bound equivalents remain available.',files=host))
    # Exact-rational audit of frozen coefficients and scenario prices.
    rates=J(TIP,'results/b28_01c/gate_rates_c.json',True)
    oldrates=J(OLD,'results/b28_01/host_rates.json',True)
    assert rates['producer']==oldrates['producer'] and rates['verifier']==oldrates['verifier']
    rho=rates['verifier_ratio_up']; ratios={c:rates['verifier'][c]/rates['producer'][c] for c in rates['producer']}
    assert rho>=max(ratios.values())>rho-Q(1,10000)
    scenarios=J(TIP,'results/b28_01c/cellA_price_c.json',True)['scenarios']; audited=[]
    for r in scenarios:
        n=NS=813314;k=8;a=109;z=int(r['z']);U=int(r['U'])
        pm=phases(n,k,a,z,U,rates['producer']); vm=phases(n,k,a,z,U,rates['verifier'])
        prod=pm['cB']+pm['cS']+2*sum(pm[c] for c in ('cH','cV','cR','cD'))
        ver=max(sum(vm.values()),rho*sum(pm.values())); total=prod+ver
        rows=(3*z+9)//10
        est=vmem(n,NS,k,a,z,rows,U,n-U,rows,z,z);env=envelope(n,a,z,U)
        for key,value in [('producer_secs',prod),('verifier_direct_secs',sum(vm.values())),('verifier_ratio_secs',rho*sum(pm.values())),('verifier_gate_secs',ver),('total_secs',total)]:
            assert round(value,1)==r[key],(key,r,value)
        assert round(total/3600,3)==r['total_hours']
        assert est==r['verifier_mem_estimate_bytes'] and env==r['mem_envelope_bytes'] and max(est,env)==r['mem_needed_bytes']
        audited.append(dict(z_over_n=z//n,U=U,producer_seconds_exact=str(prod),verifier_seconds_exact=str(ver),total_hours_exact=str(total/3600),verifier_memory_bytes=est,producer_envelope_bytes=env,needed_bytes=max(est,env),fits_time=total<=86400,passes_memory_gate=max(est,env)<=18000000000))
    memory=[]
    for folder,tag in [('control','22_6_5_2_1_d9'),('cal1_gate','24_6_5_3_2_d10'),('cal2','13_9_9_3_1_1_d9')]:
        prefix='results/b28_01c/out_c/'+folder+'/'
        cell=J(TIP,prefix+tag+'_cell.json'); gate=J(TIP,prefix+tag+'_receipt.json')['gate']
        est=vmem(cell['n_chi'],gate['N_S'],cell['delta'],cell['a'],gate['z'],gate['rows_E'],gate['U'],gate['nS'],gate['rows_other'],gate['z_cover_rows'],gate['z_other_rows'])
        assert est==gate['verifier_mem_estimate_bytes']
        oldfolder='cal1' if folder=='cal1_gate' else folder
        vr=J(OLD,'results/b28_01/'+oldfolder+'/'+tag+'_p2147483647_verify_receipt.json')
        peak=max(x['peak_rss_bytes'] for x in vr['phases'])
        if folder!='cal1_gate':
            cv=J(TIP,prefix+tag+'_p2147483647_verify_receipt.json')
            peak=max(peak,max(x['peak_rss_bytes'] for x in cv['phases']))
        assert est>=peak
        memory.append(dict(cell=tag,estimate_bytes=est,committed_peak_bytes=peak,covers_committed_peak=True))
    save(OUT/'GATE_AUDIT.json',dict(evidence='COMPUTED rational time arithmetic and integer memory arithmetic from committed inputs',ratio_up=str(rho),ratios_exact={c:str(v) for c,v in ratios.items()},coefficients_unchanged=True,ratio_rounded_up=True,scenarios=audited,memory=memory))
    save(OUT/'AUDIT_INPUTS.json',inputs)
    outputs=[dict(path=str(p.relative_to(OUT)),**fd(p)) for p in sorted(OUT.rglob('*')) if p.is_file() and (p.name in ('REGRESSION.json','TEMPORARY_OUTPUTS.json','GATE_AUDIT.json','AUDIT_INPUTS.json') or '/replay/' in str(p))]
    save(OUT/'audit_receipt.json',dict(command='timeout 60 bash -c "ulimit -v 500000; exec python3 analysis/b28_01rb_audit_v2.py"',script=fd(Path(__file__)),inputs=fd(OUT/'AUDIT_INPUTS.json'),replay_input=fd(OUT/'replay_receipt.json'),outputs=outputs,wall_seconds=time.monotonic()-start,maxrss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,address_limit_kib=500000,timeout_seconds=60))
    print(json.dumps(dict(regression_files=len(reg),regression_json=len(jd),deterministic_repair_matches=len(comparisons),all_match=True,scenarios=len(audited))))

if __name__=='__main__': main()
