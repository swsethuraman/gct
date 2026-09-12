"""Finish serial legacy, semantic, inherited, resource and export checks."""
import json,os,subprocess,sys,time
from pathlib import Path

def main():
    env=dict(os.environ,PYTHONUTF8='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    jobs=[('original',1900,768,0,['analysis/b14_03_replay.py'],False),
          ('chow',300,768,0,['analysis/ci73_chow_control.py'],True),
          ('inherited',120,768,0,['analysis/ci73_inherited_run.py'],True),
          ('memory_probe',60,32,77,['analysis/ci73_resource_probe.py','memory'],True),
          ('backend_timeout_probe',60,768,78,['analysis/ci73_resource_probe.py','backend_timeout'],True),
          ('wall_probe',1,768,124,['analysis/ci73_resource_probe.py','wall'],True),
          ('equations',120,768,0,['analysis/ci73_export.py'],True)]
    outcomes=[]
    Path('results/ci73/postcheck.json').write_text('[]\n')
    for name,seconds,memory,expected,args,bounded in jobs:
        stem='ci73_post_'+name
        command=[sys.executable]+(['analysis/ci73_bound.py','--seconds',str(seconds),'--memory-mb',str(memory),'--name',stem] if bounded else [])+args
        start=time.monotonic()
        p=subprocess.run(command,env=env,capture_output=True,text=True,encoding='utf-8',errors='replace',
            timeout=seconds+30,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
        Path('results/logs',stem+'.log').write_text(p.stdout+p.stderr,encoding='utf-8')
        item=dict(name=name,expected_exit=expected,actual_exit=p.returncode,passed=p.returncode==expected,
                  seconds=time.monotonic()-start,command=command)
        outcomes.append(item)
        Path('results/ci73/postcheck.json').write_text(json.dumps(outcomes,indent=2)+'\n')
        print(json.dumps(item),flush=True)
        if not item['passed']:raise SystemExit('Postcheck stopped: '+stem)

if __name__=='__main__':main()
