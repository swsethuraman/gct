"""Verify the portable packet, scoped candidate screen and unchanged CI73 inputs."""
import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
def read(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def canonical(data):
    try:
        data.decode('utf-8')
        if b'\0' not in data:return data.replace(b'\r\n',b'\n')
    except UnicodeDecodeError:pass
    return data
def sha(p):return hashlib.sha256(canonical((ROOT/p).read_bytes())).hexdigest()
def git(*a):return subprocess.check_output(['git','-C',str(ROOT),*a],stderr=subprocess.DEVNULL)

def main():
    p=argparse.ArgumentParser();p.add_argument('--require-tag',action='store_true');p.add_argument('--report',required=True)
    args=p.parse_args();checks=[]
    def check(name,ok,detail=None):checks.append(dict(name=name,passed=bool(ok),detail=detail))
    slots=read('results/b15_prep/slots.json')
    check('twelve unique all-Astra slots',len(slots)==12 and len({s['branch'] for s in slots})==12 and all(s['model']=='gpt-6-astra' for s in slots))
    for s in slots:
        check('brief '+s['slot'],(ROOT/s['brief']).is_file())
        for f in s['inputs']:check('input '+s['slot']+' '+f['path'],sha(f['path'])==f['sha256'])
    for t in read('results/b15_prep/TOOL_INDEX.json')['tools']:
        for f in t['sources']:check('tool '+f['path'],sha(f['path'])==f['sha256'])
    ci='62369e75e606fc6ac59e1d249a5871a57035b918'
    paths=git('ls-tree','-r','--name-only',ci).decode().splitlines()
    # Bind the accepted production backend and data to the exact reviewed Git object.
    paths=[p for p in paths if p.startswith(('analysis/ci73','results/ci73/','tools/verify/'))]
    identical=[];different=[]
    for path in paths:
        current=ROOT/path
        accepted=git('show',ci+':'+path)
        if not current.is_file() or canonical(current.read_bytes())!=canonical(accepted) or git('show','HEAD:'+path)!=accepted:different.append(path)
        else:identical.append(path)
    check('accepted CI73 Git blobs and normalized working inputs retained',not different,dict(files=len(paths),different=different,normalization='CRLF to LF only for NUL-free UTF8 text'))
    check('accepted authentic production replay receipt',read('results/b15_prep/ci73_acceptance.json')['status']=='PASS_FRESH_AUTHENTIC_PRODUCTION_REPLAY')
    spec=importlib.util.spec_from_file_location('pred',ROOT/'tools/integrate/exclusion_predicates.py')
    pred=importlib.util.module_from_spec(spec);spec.loader.exec_module(pred)
    ledger=read('results/integrate/inherited_exclusions.json');queue=read('results/b15_prep/candidate_preflight.json')
    screened=[]
    for row in queue['small_multiplicity_panel']+queue['a1_panel']:
        cell=dict(n=4,delta=row['delta'],ell=len(row['lam']),**{'lambda':row['lam']})
        hits=pred.conclusions_for(ledger,cell,'quartic_padded_gap')
        screened.append(dict(delta=row['delta'],lam=row['lam'],rules=hits))
    hits=[s for s in screened if s['rules']]
    check('71 small and nine a1 candidates re-screened',len(screened)==80)
    check('dispatched panels not excluded by current canonical predicates',not hits,hits)
    check('delivery selftests',read('results/b15_prep/checks/delivery_selftest.json')['status']=='PASS')
    tag=None
    if args.require_tag:
        commit=git('rev-parse','batch15-base^{commit}').decode().strip()
        tree=git('rev-parse','batch15-base^{tree}').decode().strip()
        obj=git('rev-parse','batch15-base').decode().strip()
        annotation=git('for-each-ref','--format=%(contents)','refs/tags/batch15-base').decode()
        check('annotated tag identifies commit and tree',commit in annotation and tree in annotation and obj!=commit)
        check('launch HEAD is frozen base',git('rev-parse','HEAD').decode().strip()==commit)
        tracked=set(git('ls-tree','-r','--name-only',commit).decode().splitlines())
        required={s['brief'] for s in slots}|{f['path'] for s in slots for f in s['inputs']}
        check('every dispatched brief and input is committed',required<=tracked,sorted(required-tracked))
        tag=dict(commit=commit,tree=tree,tag_object=obj)
    report=dict(status='PASS' if all(x['passed'] for x in checks) else 'FAIL',checks=checks,
                checks_passed=sum(x['passed'] for x in checks),checks_total=len(checks),tag=tag,
                fresh_mathematical_replay=False,note='Packaging/input preflight; accepted prior mathematics is inherited as explicitly stated.',
                candidate_screen=screened,python=sys.version)
    dest=Path(args.report);dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in ('checks','candidate_screen')},indent=2))
    for c in checks:
        if not c['passed']:print(json.dumps(c))
    return 0 if report['status']=='PASS' else 1

if __name__=='__main__':raise SystemExit(main())
