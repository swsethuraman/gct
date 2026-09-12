"""Capture exact consulted-input provenance; not needed by acceptance at runtime."""
import hashlib,json,shutil,subprocess,sys
from pathlib import Path
sys.path.insert(0,str(Path('tools/verify').resolve()))
import ci73_io as io

ROOT=Path('.').resolve();SHARED=ROOT.parents[2];BASE='9898e56941a7665f231873481dae956f08509995'
OUT=Path('results/ci73')

def git(repo,*args):
    p=subprocess.run(['git','-C',str(repo),*args],capture_output=True,text=True,timeout=30)
    if p.returncode:raise RuntimeError(p.stderr)
    return p.stdout.strip()

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def bind(repo,revision,rel):
    blob=git(repo,'rev-parse',revision+':'+rel)
    frozen=subprocess.check_output(['git','-C',str(repo),'cat-file','blob',blob],timeout=30)
    actual=(repo/rel).read_bytes()
    if not rel.endswith('.gz'):actual=actual.replace(b'\r\n',b'\n');frozen=frozen.replace(b'\r\n',b'\n')
    if actual!=frozen:raise RuntimeError('consumed bytes differ from frozen blob: '+str(repo/rel))
    return blob

def main():
    (OUT/'provenance.json').write_text('{"status":"RUNNING"}\n')
    pins=[('B14-01','work/reviews/b14-01','cf68004cf2bd31831117c77cea6ac6621f4b8c22'),
          ('B14-02','work/reviews/b14-02','f0e626263ef48e60e39e162daf418616162c3e2e'),
          ('B14-03','work/batch14/B14-03','d1ef799ddd96ef119584844c6a6d5188117eac0c'),
          ('B14-04','work/batch14/B14-04','27be12c0ea45944f392a30527ccc397d49487101'),
          ('B14-05','work/batch14/B14-05','545844527d004972483adad9a647ebaf1f246f6d')]
    repositories=[];agreements=[]
    for name,path,head in pins:
        repo=SHARED/path
        if git(repo,'rev-parse','HEAD')!=head:raise RuntimeError('pinned checkout changed '+name)
        repositories.append(dict(name=name,origin=str(repo),head=head,tree=git(repo,'rev-parse','HEAD^{tree}')))
        for rel in ['results/s74/source.json','results/b14_prep/points/P13.json']:
            p=repo/rel;local=ROOT/rel
            if io.digest(io.load(p))!=io.digest(io.load(local)):raise RuntimeError('shared definition disagreement '+name+' '+rel)
            agreements.append(dict(repository=name,path=rel,raw_sha256=sha(p),canonical_sha256=io.digest(io.load(p)),
                                   git_blob=bind(repo,head,rel)))
    inputs=io.load(OUT/'input_manifest.json')
    for row in inputs:
        current=sha(Path(row['origin']))
        if current!=row['sha256']:
            if not (row['snapshot'].endswith('/followup.md') and current=='59b338943dc40be91f36840b8658f25e6f152559646372db512ebd3f3b9f9746'):
                raise RuntimeError('original input changed: '+row['origin'])
            row['subsequent_revision_sha256']=current
            row['revision_note']='One supporting-review bullet added after initial snapshot; read and incorporated. Both versions retained.'
        snapshot=Path(row['snapshot'])
        row['snapshot_raw_sha256']=sha(snapshot)
        if snapshot.name.endswith(('.json','.gz')):row['canonical_sha256']=io.digest(io.load(snapshot))
    for rel,name in [('Batch14_Results/B14-03_review/FOLLOWUP_CI73.md','followup_updated.md'),
        ('Batch14_Results/B14-04_05_review/REVIEW.md','review04_05.md'),
        ('Batch14_Results/B14-04_05_review/b14_05_input_audit_fix.patch','b14_05_input_audit_fix.patch')]:
        origin=SHARED/rel;destination=OUT/'inputs'/name;shutil.copyfile(origin,destination)
        inputs.append(dict(origin=str(origin),snapshot=destination.as_posix(),sha256=sha(origin),snapshot_raw_sha256=sha(destination)))
    consulted=[('Batch14_Results/B14-02_review/joint_verify.py','review arithmetic helper; not acceptance'),
        ('Batch14_Results/B14-01_review/review_checks.py','review arithmetic helper; not acceptance'),
        ('Batch14_Results/B14-01_review/dimension_replay.json','review receipt; not acceptance'),
        ('work/reviews/b14-01/analysis/b14_01_mixed.py','producer comparison only; not imported'),
        ('work/reviews/b14-02/analysis/b14_02_source13.py','producer comparison only; not imported'),
        ('work/reviews/b14-02/analysis/b14_02_exact_check.py','separate exact-evaluator reference; not imported'),
        ('work/batch14/B14-04/analysis/b14_04/verify.py','independent Newton/MN component provenance')]
    consulted=[dict(origin=str(SHARED/path),sha256=sha(SHARED/path),use=use) for path,use in consulted]
    frozen=['results/s74/source.json','results/b14_prep/points/P13.json','results/s74/certified.json',
        'results/s74/columns_gen_2147483647.json.gz','docs/s57_report.md','docs/s74_report.md','docs/s74_final_review.md',
        'analysis/wk12_s74_certify.py','analysis/wk12_s74_certs.py','analysis/wk12_s74_decide.py','analysis/wk12_int_s74_final.py']
    frozen += [f'results/s74/columns_{family}_{p}.json' for family in ['pad','det'] for p in [2147483647,2147483629]]
    fixed=[dict(path=path,base=BASE,git_blob=bind(ROOT,BASE,path),
                working_raw_sha256=sha(ROOT/path)) for path in frozen]
    for row in inputs:
        for pin in repositories:
            origin=Path(row['origin']);repo=Path(pin['origin'])
            if origin.is_relative_to(repo):row['pinned_git_blob']=bind(repo,pin['head'],origin.relative_to(repo).as_posix())
    for row in consulted:
        for pin in repositories:
            origin=Path(row['origin']);repo=Path(pin['origin'])
            if origin.is_relative_to(repo):row['pinned_git_blob']=bind(repo,pin['head'],origin.relative_to(repo).as_posix())
    output=dict(status='PASS',base=BASE,base_tree=git(ROOT,'rev-parse',BASE+'^{tree}'),repositories=repositories,
        shared_definition_agreement=agreements,snapshotted_inputs=inputs,consulted_helpers=consulted,frozen_inputs=fixed,
        normalization='Raw file SHA256 identifies consumed bytes; canonical JSON SHA256 tolerates checkout line endings. Git blobs identify immutable base content.',
        derived_inputs={'inputs/generic39.json':'first 39 generic quartics; fresh verifier checks all 39x39 values',
                        'ambient13_power.json.gz':'complete Newton h13[h4] expansion generated by ci73_dimension_run.py',
                        'certificate.json':'ci73_prepare.py selects primary indices 0..72 and a 36-minor; no fresh-value authority'})
    (OUT/'provenance.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(status='PASS',pinned_repositories=len(repositories),shared_definitions=len(agreements),
                          snapshots=len(inputs),consulted_helpers=len(consulted),frozen_inputs=len(fixed))))

if __name__=='__main__':
    try:main()
    except Exception as exc:
        (OUT/'provenance.json').write_text(json.dumps(dict(status='FAIL',error=str(exc)))+'\n')
        raise
