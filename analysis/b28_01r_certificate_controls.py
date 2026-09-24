#!/usr/bin/env python3
"""Two adversarial certificate controls on the already authorized small cell.
They expose missing verifier checks without changing any frozen code.
"""
import hashlib
import json
import os
import pathlib
import shutil
import subprocess
import tempfile
import time

WT=pathlib.Path('/mnt/c/Users/swami/Projects/gct-gpt/work/batch28/b28-01r')
OUT=WT/'results/b28_01r'
HOST=pathlib.Path.home()/'b28_01'
PY=pathlib.Path.home()/'b28venv/bin/python'
TAG='22_6_5_2_1_d9'; P=2147483647

def digest(path):
    b=path.read_bytes(); return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def save(path,obj):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')

def main():
    start=time.monotonic(); results=[]; receipts=[]
    bind=json.loads((OUT/'BINDINGS.json').read_text())
    for ent in bind['frozen']:
        assert digest(HOST/'frozen'/ent['name'])=={k:ent[k] for k in ('bytes','sha256')}
    scratch=pathlib.Path(tempfile.mkdtemp(prefix='b28_01r_cert_controls_'))
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',B28_VFY_SO=str(HOST/'frozen/b28_01_vfy.so'),
             OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',NUMEXPR_NUM_THREADS='1')
    for name in ('missing_minor','wrong_recipe_annotations'):
        case=scratch/name
        shutil.copytree(OUT/'replay/control',case)
        cf=case/f'{TAG}_p{P}_cert.json'; cert=json.loads(cf.read_text())
        if name=='missing_minor':
            del cert['evaluation']['minor_rows']; del cert['evaluation']['minor_det_mod_p']
        else:
            cert['hybrid']['projection']['base_seed']+=1
            cert['hybrid']['projection']['attempt']=3
        save(cf,cert)
        dest=OUT/'certificate_controls'/name
        save(dest/'modified_cert.json',cert)
        op=dest/'verify.json'
        cmd=[str(PY),str(HOST/'frozen/b28_01_verify.py'),'--lam','22','6','5','2','1','--delta','9','--a','24',
             '--prime',str(P),'--dir',str(case),'--out',str(op)]
        rr=OUT/'certificate_control_receipts'; rr.mkdir(exist_ok=True)
        so=rr/(name+'_stdout_receipt.txt'); se=rr/(name+'_stderr_receipt.txt'); tm=rr/(name+'_time_receipt.txt')
        t=time.monotonic()
        with so.open('wb') as sout,se.open('wb') as serr:
            p=subprocess.run(['/usr/bin/time','-v','-o',str(tm)]+cmd,stdout=sout,stderr=serr,env=env,timeout=30)
        vr=op.with_name('verify_receipt.json'); shutil.move(str(vr),str(rr/(name+'_verify_receipt.json')))
        answer=json.loads(op.read_text())
        assert p.returncode==0 and answer['verdict']=='ACCEPT'
        results.append(dict(case=name,verdict=answer['verdict'],exit_code=p.returncode,
                            modified_certificate=digest(cf),verifier_output=digest(op),
                            original_code_unchanged=True))
        receipts.append(dict(case=name,command=cmd,wall_seconds=time.monotonic()-t,code=digest(HOST/'frozen/b28_01_verify.py'),
                             stdout=digest(so),stderr=digest(se),timer=digest(tm)))
    save(OUT/'CERTIFICATE_CONTROLS.json',dict(evidence='COMPUTED adversarial controls; no new calibration or target',
        results=results,interpretation='The frozen verifier accepts a full-rank certificate without its required minor, and accepts nonfrozen projection annotations. These do not negate the independently recomputed full rank of this control.'))
    save(OUT/'certificate_control_receipts/RESOURCE_RECEIPT.json',dict(runs=receipts,wall_seconds=time.monotonic()-start,
        script=digest(pathlib.Path(__file__)),input_bindings=digest(OUT/'BINDINGS.json'),output=digest(OUT/'CERTIFICATE_CONTROLS.json'),
        scope_memory_bytes=512000000,scope_wall_seconds=60,scope_swap_bytes=0))
    print(json.dumps(results))

if __name__=='__main__': main()
