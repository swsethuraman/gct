"""Sequential, per-object replay and banking; numerical subprocesses bounded by b13_07_run."""
import datetime as dt
import json
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
mode=sys.argv[1]
if mode=='stable':
    files=[p for p in (ROOT/'results/s79_stable').rglob('stable_*.json') if '_summary' not in p.name]
    groups=[[p] for p in sorted(files,key=lambda p:json.loads(p.read_text())['raw_weight_space'])]
elif mode=='cubic':
    files=list((ROOT/'results/certs/s79_per6').glob('*_d9_fullrank_*.json.gz'))
    keys=sorted({p.name.split('_p')[0] for p in files},key=lambda k:sum(p.stat().st_size for p in files if p.name.split('_p')[0]==k))
    groups=[[p for p in files if p.name.split('_p')[0]==key] for key in keys]
else: raise ValueError(mode)
out=[]
for index, group in enumerate(groups):
    if dt.datetime.now(dt.timezone.utc)>=dt.datetime(2026,9,10,0,15,tzinfo=dt.timezone.utc): break
    stage=[]; ok=True
    for sub,p in enumerate(group):
        tag=f'b13_07_{mode}_{index:02d}_{sub:02d}'
        args=[sys.executable,'analysis/b13_07_run.py',tag,'900' if mode=='stable' else '180','analysis/b13_07_audit.py',
              'stable' if mode=='stable' else 'cert',p.relative_to(ROOT).as_posix()]
        run=subprocess.run(args,cwd=ROOT,capture_output=True,text=True)
        print(run.stdout.strip(),flush=True)
        if run.stderr: print(run.stderr,flush=True)
        stage += [f'results/logs/{tag}.log', f'results/logs/{tag}_run.json']
        if mode=='stable':
            d=json.loads(p.read_text()); name='stable_'+'_'.join(map(str,d['rho'])).rstrip('_0')+'.json'
        else: name='replay_'+p.name.replace('.json.gz','.json')
        if (ROOT/'results/b13_07'/name).exists(): stage += ['results/b13_07/'+name]
        out.append(dict(path=p.relative_to(ROOT).as_posix(),exit_code=run.returncode,run=tag))
        ok &= run.returncode==0
    subprocess.run(['git','add','--']+stage,cwd=ROOT,check=True,capture_output=True)
    subprocess.run(['git','commit','-m',f'B13-07 audit {mode} object {index+1}/{len(groups)}: '+('verified' if ok else 'replay needs attention')],cwd=ROOT,check=True,capture_output=True)
    print('BANKED',mode,index+1,'/',len(groups),'PASS' if ok else 'NEEDS ATTENTION',flush=True)
    if not ok: break
report=dict(board_numbering='batch13',session_id='B13-07',mode=mode,expected_files=len(files),attempted=len(out),
            passed=sum(x['exit_code']==0 for x in out),runs=out,time_utc=dt.datetime.now(dt.timezone.utc).isoformat())
(ROOT/f'results/b13_07/{mode}_batch.json').write_text(json.dumps(report,indent=1)+'\n',encoding='utf-8')
