"""Serial bounded receiver replay; no original absolute input layout required."""
import json,os,subprocess,sys,time
from pathlib import Path

def main():
    env=dict(os.environ,PYTHONUTF8='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    jobs=[('original',1900,0,['analysis/b14_03_replay.py'],False),
        ('literal',120,0,['analysis/ci73_literal_controls.py'],True),
        ('benchmark',120,0,['analysis/ci73_benchmark.py'],True),
        ('chow',300,0,['analysis/ci73_chow_control.py'],True),
        ('standard',1800,0,['tools/verify/verify.py','results/ci73/certificate.json','--report','results/ci73/receiver_report.md'],True),
        ('controls',1800,0,['analysis/ci73_controls.py'],True),
        ('inherited',120,0,['analysis/ci73_inherited_run.py'],True),
        ('equations',120,0,['analysis/ci73_export.py'],True)]
    outcomes=[]
    for name,seconds,expected,args,bounded in jobs:
        stem='ci73_replay_'+name
        command=[sys.executable]+(['analysis/ci73_bound.py','--seconds',str(seconds),'--memory-mb','768','--name',stem] if bounded else [])+args
        start=time.monotonic()
        p=subprocess.run(command,env=env,capture_output=True,text=True,encoding='utf-8',errors='replace',
            timeout=seconds+30,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
        Path('results/logs',stem+'.log').write_text(p.stdout+p.stderr,encoding='utf-8')
        item=dict(name=name,expected_exit=expected,actual_exit=p.returncode,passed=p.returncode==expected,
                  seconds=time.monotonic()-start,command=command)
        outcomes.append(item)
        Path('results/ci73/replay_results.json').write_text(json.dumps(outcomes,indent=2)+'\n')
        print(json.dumps(item),flush=True)
        if not item['passed']:raise SystemExit('Replay stopped: '+stem)

if __name__=='__main__':main()
