"""Replay B14-03 on Windows, serially, checking positive and negative exits."""
import json
import os
from pathlib import Path
import subprocess
import sys
import time


def main():
    if os.name != 'nt':
        raise SystemExit('This bounded launcher uses Windows Job Objects; the standalone CI checker is portable.')
    env = dict(os.environ, PYTHONUTF8='1', OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
    jobs = [
        ('producer',120,0,['analysis/b14_03_produce.py']),
        ('controls',600,0,['analysis/b14_03_controls.py']),
        ('independent',600,0,['tools/verify/complete_interpolation.py','results/b14_03/control.json',
                             '--output','results/b14_03/verification.json']),
        ('dispatcher',600,0,['tools/verify/verify.py','results/b14_03/control.json',
                            'results/b14_03/rational_control.json','results/b14_03/control.json.gz',
                            '--report','results/b14_03/dispatcher_report.md']),
        ('rejections',600,1,['tools/verify/verify.py','results/b14_03/corrupted_entry_control.json',
                            'results/b14_03/missing_input_control.json','results/b14_03/duplicate_key_control.json',
                            'results/b14_03/nonexistent_control.json',
                            '--report','results/b14_03/dispatcher_rejections.md']),
    ]
    outcomes = []
    for name,seconds,expected,args in jobs:
        stem = 'b14_03_replay_'+name
        command = [sys.executable,'analysis/b14_03_bound.py','--seconds',str(seconds),
                   '--memory-mb','768','--name',stem,*args]
        start = time.perf_counter()
        r = subprocess.run(command,env=env,capture_output=True,text=True,encoding='utf-8',
                           errors='replace',timeout=seconds+30,creationflags=subprocess.CREATE_NO_WINDOW)
        Path('results/logs',stem+'.log').write_text(r.stdout+r.stderr,encoding='utf-8')
        item = {'name':name,'expected_exit':expected,'actual_exit':r.returncode,
                'test_passed':r.returncode==expected,'command':command,'wall_seconds':time.perf_counter()-start}
        outcomes.append(item)
        print(json.dumps(item),flush=True)
        if r.returncode != expected:
            raise SystemExit(f'replay stopped: {name}, see results/logs/{stem}.log')
    Path('results/b14_03/replay_results.json').write_text(json.dumps(outcomes,indent=2)+'\n',encoding='utf-8')


if __name__ == '__main__':
    main()
