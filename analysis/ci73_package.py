"""Package only the committed CI73 branch and verify its named-ref bundle."""
import hashlib,json,shutil,subprocess,sys
from datetime import datetime,timezone
from pathlib import Path

BASE='9898e56941a7665f231873481dae956f08509995'
TREE='cb688cd3fe454d638f3202e759e2eaa0c629739f'
BRANCH='b14-03-ci73'
ROOT=Path('.').resolve()
OUT=ROOT.parents[2]/'Batch14_Results/B14-03-ci73'

def command(args):
    p=subprocess.run(args,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=180)
    if p.returncode:raise RuntimeError(str(args)+'\n'+p.stdout+'\n'+p.stderr)
    return p.stdout.strip(),p.stderr.strip()

def git(*args):return command(['git',*args])[0]
def digest(path,algorithm='sha256'):return hashlib.new(algorithm,Path(path).read_bytes()).hexdigest()
def load(path):return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def save(path,data):Path(path).write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')

def main():
    if git('branch','--show-current')!=BRANCH or git('log','-1','--format=%H','batch14-base')!=BASE:
        raise RuntimeError('branch/base mismatch')
    if git('log','-1','--format=%T','batch14-base')!=TREE:raise RuntimeError('base tree mismatch')
    if git('status','--porcelain'):raise RuntimeError('commit intentional changes before packaging')
    verification=load('results/ci73/verification.json');controls=load('results/ci73/controls_summary.json')
    original=load('results/b14_03/control_results.json');inherited=load('results/ci73/inherited_replay.json')
    if verification['status']!='PASS' or controls['status']!='PASS' or original['test_count']!=97 or original['status']!='PASS':
        raise RuntimeError('required verification results absent')
    if inherited['status']!='PASS_ARITHMETIC_REPLAY':raise RuntimeError('inherited arithmetic replay absent')
    head,tree=git('rev-parse','HEAD'),git('rev-parse','HEAD^{tree}')
    OUT.mkdir(parents=True,exist_ok=True)
    checker=[sys.executable,'tools/delivery/check_delivery.py','--branch',BRANCH,'--base',BASE]
    for name,args in [('delivery_before',checker)]:
        out,err=command(args);(OUT/(name+'.log')).write_text(out+'\n'+err+'\n',encoding='utf-8')
    bundle=OUT/'b14_03_ci73.bundle'
    out,err=command(['git','bundle','create',str(bundle),BASE+'..'+BRANCH,BRANCH])
    (OUT/'bundle_create.log').write_text(out+'\n'+err+'\n',encoding='utf-8')
    for name,args in [('delivery_after',checker+['--bundle',str(bundle)]),('bundle_verify',['git','bundle','verify',str(bundle)])]:
        out,err=command(args);(OUT/(name+'.log')).write_text(out+'\n'+err+'\n',encoding='utf-8')
    heads=git('bundle','list-heads',str(bundle))
    if heads.splitlines()!=[head+' refs/heads/'+BRANCH]:raise RuntimeError('bundle ref mismatch')
    (OUT/'bundle_heads.log').write_text(heads+'\n')
    with bundle.open('rb') as stream:
        header=[]
        while True:
            line=stream.readline()
            if not line or line==b'\n':break
            header.append(line.decode().rstrip())
    prerequisites=[line[1:].split()[0] for line in header if line.startswith('-')]
    if prerequisites!=[BASE]:raise RuntimeError('bundle prerequisite mismatch')
    if bundle.stat().st_size>5_000_000:raise RuntimeError('registered one-part bundle exceeded 5 MB')
    part=OUT/(bundle.name+'.part00');shutil.copyfile(bundle,part)
    archive=OUT/'ci73_artifacts.zip'
    # Keep the Windows command line bounded; Git expands these pathspecs.
    command(['git','archive','--format=zip','--output='+str(archive),'HEAD',
             'docs/ci73*','analysis/ci73*','tools/verify','results/ci73','results/logs/ci73*','results/PREREG_ci73.md'])
    sources={'REPORT.md':'docs/ci73_report.md','REPLAY.md':'docs/ci73_replay.md','PROOF.md':'docs/ci73_proof.md',
        'EQUATIONS.md':'docs/ci73_equations.md','PREREG.md':'results/PREREG_ci73.md'}
    for name in ['certificate.json','equations.json','verification.json','controls_summary.json','inherited_replay.json',
                 'provenance.json','input_manifest.json','resource_summary.json','replay_results.json','artifact_manifest.json']:
        sources[name]='results/ci73/'+name
    for name,source in sources.items():shutil.copyfile(source,OUT/name)
    for algorithm in ['md5','sha256']:
        (OUT/(bundle.name+'.'+algorithm)).write_text(''.join(digest(p,algorithm)+'  '+p.name+'\n' for p in [bundle,part]),encoding='utf-8')
    files=[]
    exclusions={'manifest.json','CHECKSUMS.md5','CHECKSUMS.sha256','checksum_verification.log'}
    for path in sorted(OUT.iterdir()):
        if not path.is_file() or path.name in exclusions:continue
        if path.stat().st_size>5_000_000:raise RuntimeError('oversized delivery artifact '+path.name)
        files.append(dict(name=path.name,bytes=path.stat().st_size,md5=digest(path,'md5'),sha256=digest(path)))
    manifest=dict(session_id='B14-03-ci73',actual_model='gpt-6-astra',reasoning_effort='xhigh',
        base=BASE,base_tree=TREE,branch=BRANCH,head=head,head_tree=tree,prerequisites=prerequisites,
        bundle=bundle.name,bundle_parts=[part.name],part_count=1,
        delivery_checks=dict(before='CLEAN',after='CLEAN',bundle_verify='OK'),
        verification=dict(original_controls=97,degree13_controls=controls,
            degree13='full fresh standard-verifier polynomial PASS',inherited='separate S74 arithmetic replay'),
        claim_scope='i_red13=3; u^11 gives i_pad24>=3; inherited S74 facts give i_pad24 in [3,5], D in [-4,-2]; D=-4 open',
        limits='one numerical worker/thread, aggregate 768 MiB, 120 s per batch, 1800 s full replay',
        created_utc=datetime.now(timezone.utc).isoformat(),files=files,
        inventory_note='Excludes manifest itself and checksum audit files to avoid cycles. Artifact archive preserves repository-relative paths.')
    save(OUT/'manifest.json',manifest)
    paths=[p for p in sorted(OUT.iterdir()) if p.is_file() and p.name not in {'CHECKSUMS.md5','CHECKSUMS.sha256','checksum_verification.log'}]
    for algorithm in ['md5','sha256']:
        sidecar=OUT/('CHECKSUMS.'+algorithm)
        sidecar.write_text(''.join(digest(p,algorithm)+'  '+p.name+'\n' for p in paths),encoding='utf-8')
        for line in sidecar.read_text().splitlines():
            expected,name=line.split('  ',1)
            if Path(name).name!=name or digest(OUT/name,algorithm)!=expected:raise RuntimeError('checksum mismatch '+name)
    if part.read_bytes()!=bundle.read_bytes():raise RuntimeError('part00 differs from whole bundle')
    (OUT/'checksum_verification.log').write_text(f'PASS: MD5 and SHA256 for {len(paths)} files; all names are bare filenames.\nWhole bundle equals part00.\n')
    print(json.dumps(dict(status='PASS',head=head,tree=tree,bundle_bytes=bundle.stat().st_size,
                         archive_bytes=archive.stat().st_size,part_count=1,delivery=str(OUT))))

if __name__=='__main__':main()
