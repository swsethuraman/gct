"""Package the committed named branch; run from this session checkout root."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
from datetime import datetime, timezone

BASE = '9898e56941a7665f231873481dae956f08509995'
TREE = 'cb688cd3fe454d638f3202e759e2eaa0c629739f'
BRANCH = 'b14-03-astra'
OUT = Path('C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-03')


def command(args):
    r = subprocess.run(args,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=120)
    if r.returncode:
        raise RuntimeError(f'{args}: exit {r.returncode}\n{r.stdout}\n{r.stderr}')
    return r.stdout.strip(),r.stderr.strip()


def git(*args):
    return command(['git',*args])[0]


def digest(path,algorithm):
    return hashlib.new(algorithm,Path(path).read_bytes()).hexdigest()


def main():
    if git('branch','--show-current') != BRANCH or git('log','-1','--format=%H','batch14-base') != BASE:
        raise RuntimeError('branch or frozen base mismatch')
    if git('log','-1','--format=%T','batch14-base') != TREE:
        raise RuntimeError('frozen tree mismatch')
    if git('status','--porcelain'):
        raise RuntimeError('commit intentional session changes before packaging')
    head,tree = git('rev-parse','HEAD'),git('rev-parse','HEAD^{tree}')
    OUT.mkdir(parents=True,exist_ok=True)
    checker = [sys.executable,'tools/delivery/check_delivery.py','--branch',BRANCH,'--base',BASE]
    stdout,stderr = command(checker)
    (OUT/'delivery_before.log').write_text(stdout+'\n'+stderr+'\n',encoding='utf-8')
    bundle = OUT/'b14_03_astra.bundle'
    stdout,stderr = command(['git','bundle','create',str(bundle),BASE+'..'+BRANCH,BRANCH])
    (OUT/'bundle_create.log').write_text(stdout+'\n'+stderr+'\n',encoding='utf-8')
    stdout,stderr = command(checker+['--bundle',str(bundle)])
    (OUT/'delivery_after.log').write_text(stdout+'\n'+stderr+'\n',encoding='utf-8')
    stdout,stderr = command(['git','bundle','verify',str(bundle)])
    (OUT/'bundle_verify.log').write_text(stdout+'\n'+stderr+'\n',encoding='utf-8')
    heads = git('bundle','list-heads',str(bundle))
    if f'{head} refs/heads/{BRANCH}' not in heads.splitlines():
        raise RuntimeError('bundle missing named branch at exact committed head')
    (OUT/'bundle_heads.log').write_text(heads+'\n',encoding='utf-8')
    # One part for this small delivery; do not quietly emit an oversized part.
    if bundle.stat().st_size > 5_000_000:
        raise RuntimeError('bundle exceeds registered one-part delivery; split and revise part count')
    part = OUT/(bundle.name+'.part00')
    shutil.copyfile(bundle,part)
    sources = [Path('docs/b14_03_report.md'),Path('docs/b14_03_complete_interpolation.md'),
               Path('results/PREREG_b14_03.md'),Path('tools/verify/complete_interpolation.py')]
    sources += sorted(Path('results/b14_03').glob('*'))
    sources += sorted(Path('results/logs').glob('b14_03*'))
    sources += sorted(Path('analysis').glob('b14_03_*.py'))
    names = set()
    for src in sources:
        if not src.is_file():
            continue
        if src.name in names:
            raise RuntimeError('delivery basename collision: '+src.name)
        names.add(src.name)
        shutil.copyfile(src,OUT/src.name)
    for algorithm,suffix in [('md5','md5'),('sha256','sha256')]:
        (OUT/(bundle.name+'.'+suffix)).write_text(''.join(
            digest(p,algorithm)+'  '+p.name+'\n' for p in [bundle,part]),encoding='utf-8')
    # Validate source contracts from the immutable base, not changed working docs.
    inputs = json.loads(Path('results/b14_03/input_manifest.json').read_text(encoding='utf-8-sig'))
    for record in inputs:
        if git('rev-parse',BASE+':'+record['path']) != record['git_blob']:
            raise RuntimeError('frozen input blob mismatch: '+record['path'])
    with bundle.open('rb') as stream:
        header = []
        while True:
            line = stream.readline()
            if not line or line == b'\n':
                break
            header.append(line.decode('utf-8').rstrip())
    prerequisites = [s[1:].split()[0] for s in header if s.startswith('-')]
    if prerequisites != [BASE]:
        raise RuntimeError('unexpected bundle prerequisites: '+str(prerequisites))
    files = []
    for path in sorted(OUT.iterdir()):
        if path.is_file() and path.name not in {'manifest.json','CHECKSUMS.md5','CHECKSUMS.sha256','checksum_verification.log'}:
            if path.stat().st_size > 5_000_000:
                raise RuntimeError('oversized delivery file: '+path.name)
            files.append({'name':path.name,'bytes':path.stat().st_size,
                          'md5':digest(path,'md5'),'sha256':digest(path,'sha256')})
    manifest = {'board_numbering':'batch14','session_id':'B14-03','actual_model':'gpt-6-astra',
                'reasoning_effort':'xhigh','base':BASE,'base_tree':TREE,'head':head,'head_tree':tree,
                'branch':BRANCH,'bundle':bundle.name,'bundle_parts':[part.name],
                'prerequisites':prerequisites,'delivery_checks':{'before':'CLEAN','after':'CLEAN','bundle_verify':'OK'},
                'run_utc':datetime.now(timezone.utc).isoformat(),'files':files,
                'verification':'97 control cases; 95 negative mutations; 71 required-key deletions; 5 expected process exits',
                'limits':'one process per calculation, one numerical thread, 768 MiB, 120/600 seconds',
                'claim_scope':'exact h=1 control; no new LMR claim',
                'inventory_note':'manifest excludes itself and global checksum/audit files to avoid digest cycles'}
    (OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    check_paths = [p for p in sorted(OUT.iterdir()) if p.is_file() and p.name not in
                   {'CHECKSUMS.md5','CHECKSUMS.sha256','checksum_verification.log'}]
    for algorithm,suffix in [('md5','md5'),('sha256','sha256')]:
        sidecar = OUT/('CHECKSUMS.'+suffix)
        sidecar.write_text(''.join(digest(p,algorithm)+'  '+p.name+'\n' for p in check_paths),encoding='utf-8')
        for line in sidecar.read_text().splitlines():
            value,name = line.split('  ',1)
            if Path(name).name != name or digest(OUT/name,algorithm) != value:
                raise RuntimeError('checksum verification failed: '+name)
    (OUT/'checksum_verification.log').write_text(
        f'PASS: MD5 and SHA256 verified for {len(check_paths)} files; names are bare filenames.\n'
        'Whole bundle equals part00. Manifest and sidecars generated after copying.\n',encoding='utf-8')
    if bundle.read_bytes() != part.read_bytes():
        raise RuntimeError('part00 differs from bundle')
    print(json.dumps({k:manifest[k] for k in ['head','head_tree','branch','prerequisites','delivery_checks']}))
    print('Delivery directory: '+str(OUT))


if __name__ == '__main__':
    main()
