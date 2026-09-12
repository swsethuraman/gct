"""Export the committed named branch, verify it, and checksum the delivery."""
import hashlib,json,math,shutil,subprocess,sys,time,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT.parents[2]/'Batch14_Results/B14-11'
BASE='9898e56941a7665f231873481dae956f08509995';BRANCH='b14-11-astra';CEILING=5*1024**2

def run(args,log=None):
    r=subprocess.run(args,cwd=ROOT,capture_output=True,text=True,encoding='utf-8',errors='replace')
    text='$ '+' '.join(str(x) for x in args)+'\n'+r.stdout+r.stderr+'\nexit_code='+str(r.returncode)+'\n'
    if log:(DEST/log).write_text(text,encoding='utf-8')
    if r.returncode:raise RuntimeError(text)
    return r.stdout.strip()

def digest(p,algorithm):return hashlib.new(algorithm,p.read_bytes()).hexdigest()

def main():
    DEST.mkdir(parents=True,exist_ok=True)
    assert run(['git','branch','--show-current'])==BRANCH
    assert run(['git','log','-1','--format=%H','batch14-base'])==BASE
    assert not run(['git','status','--porcelain']), 'uncommitted work must be handled before delivery'
    head=run(['git','rev-parse',BRANCH]);tree=run(['git','log','-1','--format=%T',BRANCH])
    files=run(['git','diff','--name-only',BASE,BRANCH]).splitlines()
    assert all((ROOT/f).stat().st_size<=CEILING for f in files)
    checker=[sys.executable,'tools/delivery/check_delivery.py','--branch',BRANCH,'--base',BASE]
    run(checker,'delivery_check_before.log')
    bundle=DEST/'b14_11_astra.bundle'
    run(['git','bundle','create',str(bundle),BASE+'..'+BRANCH,BRANCH],'bundle_create.log')
    heads=run(['git','bundle','list-heads',str(bundle)],'bundle_heads.log')
    assert 'refs/heads/'+BRANCH in heads
    run(['git','bundle','verify',str(bundle)],'bundle_verify.log')
    run(checker+['--bundle',str(bundle)],'delivery_check_after.log')
    payload=bundle.read_bytes();part_count=math.ceil(len(payload)/CEILING)
    assert part_count==1,'report must be updated to actual part count before delivery'
    part=DEST/'b14_11_astra.bundle.part00';part.write_bytes(payload)
    for source,name in [('docs/b14_11_report.md','b14_11_report.md'),
                        ('docs/b14_11_proofs.md','b14_11_proofs.md'),
                        ('docs/b14_11_protected_errata.md','protected_errata.md'),
                        ('results/b14_11/REPLAY.md','REPLAY.md'),
                        ('results/b14_11/shortlist.json','shortlist.json'),
                        ('results/b14_11/validation.json','validation.json'),
                        ('results/b14_11/input_manifest.json','input_manifest.json'),
                        ('results/b14_11/inventory_summary.json','inventory_summary.json')]:
        shutil.copyfile(ROOT/source,DEST/name)
    archive=DEST/'research_artifacts.zip'
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for f in files:z.write(ROOT/f,f)
    assert archive.stat().st_size<=CEILING
    # Native bundle header is readable before the PACK block.
    header=payload.split(b'\n\n',1)[0].decode('utf-8')
    prerequisites=[line[1:] for line in header.splitlines() if line.startswith('-')]
    manifest=dict(session='B14-11',board_numbering='batch14',actual_model='gpt-6-astra',
       created_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
       branch=BRANCH,base_commit=BASE,base_tree='cb688cd3fe454d638f3202e759e2eaa0c629739f',
       head_commit=head,head_tree=tree,named_ref='refs/heads/'+BRANCH,
       bundle_prerequisites=prerequisites,bundle_part_count=part_count,
       delivery_checks={'before_bundle':'CLEAN','after_bundle':'CLEAN','bundle_verify':'PASS','named_ref':'PASS'},
       protected_files_unchanged=True,prose_status='AUDIT_COMPLETE_WITH_PROTECTED_ERRATA',
       mathematics='exact census and sizing; 153 pullback-zero closures; ten OPEN candidates; no new ranks',
       tracked_paths=files,files=[])
    for p in sorted(DEST.iterdir()):
        if p.is_file() and p.name not in ['manifest.json','checksums.md5','checksums.sha256'] and not p.name.endswith(('.md5','.sha256')):
            manifest['files'].append(dict(filename=p.name,bytes=p.stat().st_size,md5=digest(p,'md5'),sha256=digest(p,'sha256')))
    (DEST/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    names=[r['filename'] for r in manifest['files']]+['manifest.json']
    for algorithm in ['md5','sha256']:
        content=''.join(digest(DEST/name,algorithm)+'  '+name+'\n' for name in sorted(names))
        (DEST/('checksums.'+algorithm)).write_text(content)
        for p in [bundle,part,archive]:
            (DEST/(p.name+'.'+algorithm)).write_text(digest(p,algorithm)+'  '+p.name+'\n')
    # Check the actual exported bytes and the whole/part reconstruction.
    for r in manifest['files']:
        for algorithm in ['md5','sha256']:assert digest(DEST/r['filename'],algorithm)==r[algorithm]
    assert part.read_bytes()==bundle.read_bytes()
    print(json.dumps(dict(destination=str(DEST),head=head,tree=tree,bundle_bytes=len(payload),
         bundle_parts=part_count,archive_bytes=archive.stat().st_size,changed_files=len(files),checks='PASS'),indent=2))

if __name__=='__main__':main()
