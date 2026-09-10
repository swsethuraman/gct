"""Manifest and bundle delivery for this single isolated research run."""
import ast, datetime, hashlib, json, pathlib, shutil, subprocess, sys

ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/'results/b13_02'
DEST=pathlib.Path(r'C:\Users\swami\Projects\gct-gpt\Batch13_Results\B13-02')
BASE='00495110c62acfbbbc951e82cc218ed091563b3f'

def record(p):
    b=p.read_bytes();r=dict(path=p.relative_to(ROOT).as_posix(),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
    try:
        s=b.decode('utf-8-sig')
        if '\0' not in s:r['canonical_lf_sha256']=hashlib.sha256(s.replace('\r\n','\n').encode()).hexdigest()
    except UnicodeDecodeError:pass
    return r

def dump(p,x):p.write_text(json.dumps(dict(board_numbering='batch13',session_id='B13-02',**x),indent=2),encoding='utf8')

def stage():
    inputs=['docs/batch13_worker_preamble.md','docs/batch13_board.md','docs/batch13_corrections.md',
        'docs/stocktake_batch12.md','docs/brief_wording.md','docs/batch11_plan.md','docs/s74_final_review.md',
        'docs/s_split.md','results/s74/source.json','results/s74/decision_2147483647.json',
        'results/s74/decision_2147483629.json','results/s74/s4_crosscheck.json',
        'results/astra/S4/S4_report.md','results/astra/S4/HANDOFF_s74_s75_s76.md',
        'results/astra/S4/artifacts/s64_control.json','results/astra/S4/artifacts/48_block_ledger.json',
        'results/astra/S4/src/s4.py','results/astra/S4/src/calibrate.py',
        'analysis/wk11_s69_circuit.py','analysis/wk9_s42_census.py','analysis/wk8_s30_pleth.py']
    dump(OUT/'input_manifest.json',dict(base=BASE,files=[record(ROOT/p) for p in inputs],
        hash_convention='sha256 of actual Windows working-tree bytes; canonical_lf_sha256 additionally provided for UTF-8 text'))
    outputs=[ROOT/'results/PREREG_b13_02.md',ROOT/'docs/b13_02_report.md',ROOT/'docs/b13_02_replay.md']
    outputs+=sorted((ROOT/'analysis').glob('b13_02_*.py'))
    outputs+=sorted(p for p in OUT.iterdir() if p.is_file() and p.name!='manifest.json')
    outputs+=sorted(p for p in (ROOT/'results/logs').glob('b13_02*') if p.suffix!='.pid')
    assert all(p.stat().st_size<=5_000_000 for p in outputs)
    for p in outputs:
        if p.suffix=='.py':ast.parse(p.read_text(encoding='utf8'))
        if p.suffix=='.json':
            x=json.loads(p.read_text(encoding='utf8'));assert x['board_numbering']=='batch13' and x['session_id']=='B13-02',p
    dump(OUT/'manifest.json',dict(base=BASE,branch='b13-02',model='gpt-6-astra',reasoning_effort='xhigh',
        status='bounded-fallback; exact full restriction rank unresolved',bundle_parts=1,
        source_rows=274,verified_h_pad=521,exact_coefficient_entries=1127,uncomputed_entries=243,
        adopted_determinant_rank=273,adopted_padded_rank_floor=269,
        full_structural_rank_interval=[269,274],D_interval=[-4,1],
        memory_cap_mib=768,numerical_workers=1,blas_threads=1,
        deviations=['missing python-flint installation blocked by network permissions','two recorded wall-clock gaps exceeded launch bounds'],
        files=[record(p) for p in outputs],utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))
    print('Manifest staged',len(outputs),'files')

def deliver():
    head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    assert subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip()=='b13-02'
    assert not subprocess.check_output(['git','status','--porcelain','--untracked-files=no'],cwd=ROOT,text=True).strip()
    DEST.mkdir(parents=True,exist_ok=True)
    name='b13_02_structural_restriction.bundle';bundle=DEST/name
    subprocess.run(['git','bundle','create',str(bundle),BASE+'..HEAD'],cwd=ROOT,check=True)
    verification=subprocess.run(['git','bundle','verify',str(bundle)],cwd=ROOT,text=True,capture_output=True,check=True)
    (DEST/'bundle_verify.txt').write_text(verification.stdout+verification.stderr,encoding='utf8')
    part=DEST/(name+'.part00');shutil.copy2(bundle,part)
    digests=[]
    for p in (bundle,part):
        b=p.read_bytes();digests.append(dict(filename=p.name,bytes=len(b),md5=hashlib.md5(b).hexdigest(),sha256=hashlib.sha256(b).hexdigest()))
    for algorithm in ('md5','sha256'):
        (DEST/(name+'.'+algorithm)).write_text(''.join(x[algorithm]+'  '+x['filename']+'\n' for x in digests),encoding='ascii')
    manifest=json.loads((OUT/'manifest.json').read_text())
    paths=[x['path'] for x in manifest['files']]+['results/b13_02/manifest.json']
    for rel in paths:
        src=ROOT/rel;dst=DEST/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
        assert hashlib.sha256(src.read_bytes()).digest()==hashlib.sha256(dst.read_bytes()).digest()
    shutil.copy2(ROOT/'docs/b13_02_report.md',DEST/'b13_02_report.md')
    shutil.copy2(ROOT/'docs/b13_02_replay.md',DEST/'b13_02_replay.md')
    dump(DEST/'delivery_manifest.json',dict(base=BASE,head=head,branch='b13-02',model='gpt-6-astra',
        bundle_parts=1,whole_and_parts=digests,all_copies_byte_verified=True,
        artifact_manifest='results/b13_02/manifest.json',report='b13_02_report.md',
        utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))
    # Independent reread of named checksum files; filenames must be bare.
    for algorithm in ('md5','sha256'):
        for line in (DEST/(name+'.'+algorithm)).read_text().splitlines():
            digest,fn=line.split('  ');assert pathlib.Path(fn).name==fn
            assert hashlib.new(algorithm,(DEST/fn).read_bytes()).hexdigest()==digest
    print(json.dumps(dict(head=head,destination=str(DEST),digests=digests,verification=verification.stdout+verification.stderr),indent=2))

if __name__=='__main__':
    if sys.argv[1]=='stage':stage()
    elif sys.argv[1]=='deliver':deliver()
    else:raise ValueError(sys.argv[1])
