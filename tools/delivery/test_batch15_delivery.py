"""Small synthetic deliveries exercising the new committed-object contract."""
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[2]
os.environ['PYTHONUTF8'] = '1'

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module

gate = load('gate15', ROOT/'tools/delivery/check_batch15.py')
pred = load('pred15', ROOT/'tools/integrate/exclusion_predicates.py')

def main():
    fixtures = ROOT/'results/b15_prep/checks/fixtures'
    fixtures.mkdir(parents=True, exist_ok=True)
    repo = Path(tempfile.mkdtemp(prefix='delivery_', dir=fixtures)).resolve()
    # Keep the tiny fixture for inspection; no recursive removal is necessary.
    def g(*args):
        return gate.txt(repo, *args)
    def write(p, value):
        dest=repo/p; dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(value, encoding='utf-8')
    def commit(message):
        g('add','-A'); g('commit','-qm',message+'\n\nCo-Authored-By: GPT-6 Astra <noreply@openai.com>')
    g('init','-q'); g('config','user.name','Delivery fixture'); g('config','user.email','fixture@localhost')
    write('README.md','Fixture base\n'); write('old.md','Historical hunt wording.\n')
    commit('Base'); base=g('rev-parse','HEAD'); tree=g('rev-parse','HEAD^{tree}')
    g('tag','-a','test-b15-base','-m',f'commit {base}\ntree {tree}')
    branch='b15-01-fixture'; g('checkout','-qb',branch)
    write('results/PREREG_b15_01.md','Bounded fixture before work.\n'); commit('Preregister')
    write('docs/b15_01_report.md','Fixture report.\n'); write('docs/name with spaces.md','A valid result.\n')
    write('old.md','Historical hunt wording.\nNew valid line.\n'); commit('Result')
    head=g('rev-parse','HEAD'); bundle=repo.parent/(repo.name+'.bundle')
    g('bundle','create',str(bundle),base+'..'+branch,branch)
    raw=bundle.read_bytes()
    manifest=dict(head=head,head_tree=g('rev-parse','HEAD^{tree}'),base_commit=base,
                  bundle_prerequisites=[base],bundle_bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),
                  md5=hashlib.md5(raw).hexdigest(),models=[dict(model='gpt-6-astra',phase='fixture')],slot='01',branch=branch)
    mp=repo.parent/(repo.name+'.json'); cases=[]
    def run(name, expected, man=manifest, **kw):
        args=dict(repo=repo,branch=branch,base=base,slot='01',base_tag='test-b15-base',batch='b15',bundle=bundle,manifest=mp)
        if man is not None: mp.write_text(json.dumps(man),encoding='utf-8')
        args.update(kw)
        try: result=gate.check(**args); passed=result['status']=='PASS'
        except Exception as exc: result={'errors':[str(exc)]}; passed=False
        cases.append(dict(name=name,expected_pass=expected,actual_pass=passed,passed=passed==expected,errors=result.get('errors',[])))
    run('valid custom-tag b15, spaced path, inherited wording',True)
    run('valid pre-bundle check',True,bundle=None,manifest=None)
    run('missing base tag',False,base_tag='absent-base')
    run('empty object manifest',False,man={}); run('empty array manifest',False,man=[])
    missing=repo.parent/'no-manifest.json'; run('missing manifest',False,manifest=missing)
    run('post-bundle without manifest',False,manifest=None)
    for field,value in [('base_commit','a'*40),('head','a'*40),('head_tree','a'*40),
                        ('bundle_prerequisites',[base+' subject']),('bundle_prerequisites',[12]),
                        ('sha256','0'*64),('bundle_bytes',len(raw)+1),('models',[])]:
        m=copy.deepcopy(manifest);m[field]=value;run('wrong '+field+' '+str(value)[:18],False,man=m)
    # Working bytes are not authoritative in either direction.
    write('docs/name with spaces.md','hunt is uncommitted\n')
    run('bad uncommitted working file does not taint named commit',True)
    g('checkout','--','docs/name with spaces.md')
    write('docs/name with spaces.md','hunt is now committed\n');commit('Invalid document')
    write('docs/name with spaces.md','Working file hides the error.\n')
    run('bad committed spaced file rejected despite clean working copy',False,bundle=None,manifest=None)
    g('checkout','--','docs/name with spaces.md')
    run('stale bundle rejected after new commit',False)
    whole=repo.parent/(repo.name+'_whole.bundle');g('bundle','create',str(whole),branch)
    run('full-history bundle without required prerequisite',False,bundle=whole)
    # Source membership predicates must validate every branch, including unused ones.
    invalid=[{'any_of':[{'n':4},{'unknown':True}]},{'n':True},{'delta_min':8,'delta_max':7},
             {'lambda_in':[[1,3]]},{'any_of':[]}]
    for pr in invalid:
        try:pred.validate_predicate(pr); ok=False
        except Exception:ok=True
        cases.append(dict(name='invalid predicate '+str(pr),passed=ok))
    ledger=json.loads((ROOT/'results/integrate/inherited_exclusions.json').read_text(encoding='utf-8'))
    for entry in ledger['exclusions']:pred.validate_predicate(entry['predicate'])
    cases.append(dict(name='all current ledger predicates accepted',passed=True,count=len(ledger['exclusions'])))
    out=dict(status='PASS' if all(c['passed'] for c in cases) else 'FAIL',cases=cases,
             cases_passed=sum(c['passed'] for c in cases),cases_total=len(cases),fixture=str(repo))
    path=ROOT/'results/b15_prep/checks/delivery_selftest.json'
    path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='cases'},indent=2))
    for c in cases:
        if not c['passed']:print(json.dumps(c))
    return 0 if out['status']=='PASS' else 1

if __name__=='__main__':raise SystemExit(main())
