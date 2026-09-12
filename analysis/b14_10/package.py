"""Package committed B14-10 artifacts and verify the actual named-branch bundle.

Run after the final intentional commit. Every subprocess has the remaining
180-second packaging deadline; files are streamed, not expanded into memory.
"""
import argparse, datetime, hashlib, json, os, pathlib, shutil, subprocess, sys, time, zipfile
ROOT=pathlib.Path(__file__).resolve().parents[2]
BASE='9898e56941a7665f231873481dae956f08509995'
TREE='cb688cd3fe454d638f3202e759e2eaa0c629739f'
BRANCH='b14-10-astra'
DEADLINE=time.monotonic()+180

def run(args):
    remaining=DEADLINE-time.monotonic()
    if remaining<=0:raise TimeoutError('180-second packaging budget exhausted')
    return subprocess.run(args,cwd=ROOT,capture_output=True,text=True,encoding='utf-8',
                          env=dict(os.environ,PYTHONUTF8='1',PYTHONDONTWRITEBYTECODE='1',OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1'),
                          timeout=min(60,remaining))

def git(*args):
    r=run(['git',*args])
    if r.returncode:raise RuntimeError(r.stderr)
    return r.stdout.strip()

def digests(path):
    md5=hashlib.md5();sha=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):md5.update(b);sha.update(b)
    return dict(bytes=path.stat().st_size,md5=md5.hexdigest(),sha256=sha.hexdigest())

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args()
    output=pathlib.Path(a.output).resolve()
    expected=ROOT.parents[2]/'Batch14_Results'/'B14-10'
    if output!=expected.resolve():raise ValueError('output must be the authorized B14-10 delivery directory')
    output.mkdir(parents=True,exist_ok=True)
    assert git('branch','--show-current')==BRANCH
    assert git('log','-1','--format=%H','batch14-base')==BASE
    assert git('log','-1','--format=%T','batch14-base')==TREE
    head=git('rev-parse',BRANCH);tree=git('show','-s','--format=%T',BRANCH)
    assert not git('diff','--name-only','HEAD','--'), 'uncommitted tracked changes'
    files=git('diff','--name-only',BASE,BRANCH).splitlines()
    assert files and all((ROOT/p).stat().st_size<=5_000_000 for p in files)
    checks={}
    def logged(name,args):
        result=run(args);(output/name).write_text(result.stdout+result.stderr,encoding='utf-8')
        checks[name]=dict(exit_code=result.returncode,command=args)
        if result.returncode:raise RuntimeError(name+' failed; see delivered log')
        return result.stdout+result.stderr
    checker=[sys.executable,'tools/delivery/check_delivery.py','--branch',BRANCH,'--base',BASE]
    logged('delivery_check_before.log',checker)
    bundle=output/'b14_10_astra.bundle'
    logged('bundle_create.log',['git','bundle','create',str(bundle),BASE+'..'+BRANCH,BRANCH])
    logged('delivery_check_after.log',checker+['--bundle',str(bundle)])
    logged('bundle_verify.log',['git','bundle','verify',str(bundle)])
    heads=logged('bundle_heads.log',['git','bundle','list-heads',str(bundle)])
    assert head+' refs/heads/'+BRANCH in heads
    with bundle.open('rb') as f:
        headers=[]
        for line in f:
            if line==b'\n':break
            headers.append(line.decode('utf-8').rstrip())
    prerequisite=[line[1:].split()[0] for line in headers if line.startswith('-')]
    assert prerequisite==[BASE],prerequisite
    if bundle.stat().st_size>5_000_000:raise ValueError('bundle exceeds ceiling; split before release')
    shutil.copyfile(ROOT/'docs/b14_10_report.md',output/'b14_10_report.md')
    shutil.copyfile(ROOT/'results/b14_10/REPLAY.md',output/'REPLAY.md')
    dependencies=['results/b13_05_topcells.json','docs/b13_05_report.md','docs/s57_report.md',
                  'docs/dispatch/B14-10_packet.md','docs/batch14_board.md','docs/brief_wording.md',
                  'docs/batch14_reconciliation.md','docs/b14_claude_scratch_code.md',
                  'results/s79_cert_manifest.json','results/b13_09/cert_manifest.json',
                  'tools/delivery/check_delivery.py']
    archive=output/'b14_10_evidence.zip'
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in sorted(set(files)|set(dependencies)):
            if time.monotonic()>DEADLINE:raise TimeoutError('package deadline')
            # Preserve the checked worktree bytes; delivery hashes describe this ZIP.
            z.write(ROOT/p,p)
    with zipfile.ZipFile(archive) as z:assert z.testzip() is None
    assert archive.stat().st_size<=5_000_000,'evidence zip exceeds ceiling'
    # Exercise the copy delivered inside the ZIP with no checkout input dependency.
    smoke="""import zipfile,json
with zipfile.ZipFile(__import__('sys').argv[1]) as z:
 ns={'__name__':'b14_10_packaged_verifier','__file__':'/standalone/analysis/b14_10/recover.py'}
 exec(compile(z.read('analysis/b14_10/recover.py'),'packaged_recover.py','exec'),ns)
 names=sorted(p for p in z.namelist() if p.startswith('results/b14_10/recovered/') and p.endswith('.json') and not p.endswith('.validation.json'))
 assert len(names)==4
 for p in names: assert ns['verify'](json.loads(z.read(p)))
 print('PASS: four exact witnesses replayed using verifier and certificates from delivered ZIP; stdlib only')
"""
    logged('standalone_zip_replay.log',[sys.executable,'-c',smoke,str(archive)])
    payloads={p.name:digests(p) for p in sorted(output.iterdir()) if p.is_file() and p.suffix not in ('.md5','.sha256') and p.name not in ('delivery_manifest.json','MD5SUMS','SHA256SUMS')}
    manifest=dict(board_numbering='batch14',actual_model='gpt-6-astra',created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  base_commit=BASE,base_tree=TREE,head=head,head_tree=tree,named_ref='refs/heads/'+BRANCH,
                  bundle_prerequisites=prerequisite,bundle_parts=0,file_register_parts=4,
                  verification=checks,delivery_check_failures=[],files=payloads,
                  outcome='substantive fallback; exact replacements for eight missing manifest entries, original bytes still missing',
                  archive_scope='all intentional committed session changes plus selected frozen proof dependencies; full inventory replay needs the base corpus',
                  elapsed_packaging_seconds=round(180-(DEADLINE-time.monotonic()),3))
    (output/'delivery_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    payloads['delivery_manifest.json']=digests(output/'delivery_manifest.json')
    for name,hashes in payloads.items():
        for kind in ('md5','sha256'):(output/(name+'.'+kind)).write_text(hashes[kind]+'  '+name+'\n',encoding='ascii')
    for kind,filename in [('md5','MD5SUMS'),('sha256','SHA256SUMS')]:
        (output/filename).write_text(''.join(payloads[p][kind]+'  '+p+'\n' for p in sorted(payloads)),encoding='ascii')
    for name,d in payloads.items():assert digests(output/name)==d
    print(json.dumps(dict(output=str(output),head=head,tree=tree,bundle_bytes=bundle.stat().st_size,
                         archive_bytes=archive.stat().st_size,named_ref='refs/heads/'+BRANCH,
                         all_delivery_checks='CLEAN',standalone_replay='four certificates PASS'),indent=2))

if __name__=='__main__':main()
