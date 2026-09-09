"""Prepare the tracked manifest and deliver a verified one-part research bundle."""
import datetime as dt
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
BASE='00495110c62acfbbbc951e82cc218ed091563b3f'
DEST=Path('C:/Users/swami/Projects/gct-gpt/Batch13_Results/B13-07')
OUT=ROOT/'results/b13_07'

def run(args):
    return subprocess.check_output(args,cwd=ROOT,stderr=subprocess.STDOUT).decode('utf-8').strip()
def sha(path,alg='sha256'):
    h=hashlib.new(alg)
    with open(path,'rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()
def info(p):
    return dict(path=p.relative_to(ROOT).as_posix(),bytes=p.stat().st_size,sha256=sha(p))
def save(p,obj):
    obj.update(board_numbering='batch13',session_id='B13-07')
    p.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def outputs():
    return sorted([ROOT/'docs/b13_07_report.md',ROOT/'results/PREREG_b13_07.md']+
        list((ROOT/'analysis').glob('b13_07_*.py'))+list(OUT.glob('*.json'))+
        [p for p in (ROOT/'results/logs').glob('b13_07_*') if p.suffix in ('.json','.log')])

def prepare():
    coverage=json.loads((OUT/'coverage.json').read_text())
    assert coverage['fully_replayed_weights']==23 and coverage['requires_regeneration']==187
    assert json.loads((OUT/'stable_batch.json').read_text())['passed']==16
    assert json.loads((OUT/'cubic_batch.json').read_text())['passed']==46
    claims=[
        ('dominance_r5','CERTIFIED','Exact integer Jacobian and nonzero 35-minor at both primes'),
        ('shorter_weight_inheritance','PROVED','All lengths at most five, all degrees'),
        ('degree9_census','CERTIFIED','331 six-row candidates; 210 positive; 365 shorter positive'),
        ('degree9_rank_replay','CERTIFIED PREFIX','23 weights both primes; 187 require source regeneration'),
        ('degree9_full_ideal_statement','ADOPTED','Remaining 187 full-rank inputs adopted from S79; inheritance independently verified'),
        ('stable16','CERTIFIED','All 16 positive stable blocks at both primes; complete census of 57 tails'),
        ('quartic682','ADOPTED CERTIFICATION','Both-prime record consistency verified; full matrices not independently regenerated'),
        ('deficient_rank_membership','MEASURED','59 drops, including 35 at degrees 10 to 12; no new rational membership'),
        ('epsilon_pad','CONDITIONAL','Modular containment replayed; exact rational implication not established'),
        ('LMR','ADOPTED / CERTIFIED FLOOR','Exact determinant rank 273 preserved; padded floor 269 replayed; D=1-i_pad(24) in [-4,1]')]
    save(OUT/'claim_ledger.json',dict(claims=[dict(claim=c,status=s,scope=t) for c,s,t in claims]))
    inputs=set()
    for name in ('batch13_worker_preamble','batch13_board','batch13_corrections','stocktake_batch12','brief_wording',
                 'washout_lemma','transfer_lemma','s79_review','s79_part2_review','s79_report','s57_report','s74_final_review'):
        inputs.add(ROOT/f'docs/{name}.md')
    for name in ('s79_cert_manifest.json','s79_cells.jsonl','s79_per6.jsonl','s79_queue.json','s37_jacobian.log',
                 'wk12_int_s74_final.json','PREREG_s79.md'):
        inputs.add(ROOT/'results'/name)
    for name in ('source.json','columns_pad_2147483647.json','columns_pad_2147483629.json'):
        inputs.add(ROOT/'results/s74'/name)
    for x in json.loads((OUT/'stable_batch.json').read_text())['runs']: inputs.add(ROOT/x['path'])
    for x in json.loads((OUT/'cubic_batch.json').read_text())['runs']: inputs.add(ROOT/x['path'])
    for name in ('wk12_int_s79_stable_verify.py','wk12_int_s74_final.py','wk8_s30_pleth.py','wk9_s37_jacobian.py',
                 'wk12_s79_per6.py','wk12_s79_cell6.py','wk12_s79_stable_check.py','wk12_s79_certs_manifest.py'):
        inputs.add(ROOT/'analysis'/name)
    for name in ('forms.py','hwv.py','points.py'): inputs.add(ROOT/'tools/verify'/name)
    paths=outputs()
    assert all(p.stat().st_size<=5_000_000 for p in paths)
    save(ROOT/'results/b13_07_manifest.json',dict(model='gpt-6-astra',reasoning_effort='xhigh',base_commit=BASE,
        branch='b13-07',status='verified_prefix_and_precise_bounded_fallback',delivery_parts=1,
        bundle='b13_07_s79_audit.bundle',parts=['b13_07_s79_audit.bundle.part00'],
        prepared_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
        artifact_hash_convention='SHA256 of delivered working-file bytes; Git checkout line-ending conversion may change text bytes',
        artifacts=[info(p) for p in paths],frozen_inputs=[info(p) for p in sorted(inputs)],
        replay='Use individual arguments from results/logs/b13_07_*_run.json through analysis/b13_07_run.py',
        resource_policy=dict(numerical_workers=1,blas_threads=1,job_memory_bytes=1610612736),
        limitations=['187 degree-nine weights need regenerated rank certificates','epsilon_pad equality remains conditional',
                     '682 quartic full-rank results adopted, with all per-prime records audited','29 supplemental hash mismatches identified']))
    print('Prepared manifest:',len(paths),'artifacts;',len(inputs),'frozen inputs')

def deliver():
    assert run(['git','branch','--show-current'])=='b13-07'
    assert not run(['git','status','--porcelain','--untracked-files=no'])
    head=run(['git','rev-parse','HEAD'])
    # No directory clearing or moves: this destination is explicitly authorized.
    assert DEST.resolve()==Path('C:/Users/swami/Projects/gct-gpt/Batch13_Results/B13-07').resolve()
    DEST.mkdir(parents=True,exist_ok=True)
    bundle=DEST/'b13_07_s79_audit.bundle'
    run(['git','bundle','create',str(bundle),BASE+'..HEAD'])
    verify=run(['git','bundle','verify',str(bundle)])
    refs=run(['git','bundle','list-heads',str(bundle)])
    assert head in refs
    part=DEST/(bundle.name+'.part00'); shutil.copyfile(bundle,part)
    assert sha(bundle)==sha(part)
    manifest=json.loads((ROOT/'results/b13_07_manifest.json').read_text())
    for x in manifest['artifacts']:
        p=ROOT/x['path']; assert sha(p)==x['sha256']
        dest=DEST/x['path']; dest.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(p,dest)
        assert sha(dest)==x['sha256']
    shutil.copyfile(ROOT/'results/b13_07_manifest.json',DEST/'b13_07_manifest.json')
    shutil.copyfile(ROOT/'docs/b13_07_report.md',DEST/'b13_07_report.md')
    for alg in ('md5','sha256'):
        lines=[sha(p,alg)+'  '+p.name for p in (bundle,part)]
        (DEST/(bundle.name+'.'+alg)).write_text('\n'.join(lines)+'\n',encoding='ascii')
        for line in lines:
            expected,name=line.split('  '); assert sha(DEST/name,alg)==expected
    save(DEST/'delivery_manifest.json',dict(model='gpt-6-astra',reasoning_effort='xhigh',base_commit=BASE,head_commit=head,
        branch='b13-07',parts=1,completed_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
        bundle_verification=verify,bundle_refs=refs,files=[dict(name=p.name,bytes=p.stat().st_size,md5=sha(p,'md5'),sha256=sha(p)) for p in (bundle,part)],
        report_sha256=sha(DEST/'b13_07_report.md'),tracked_manifest_sha256=sha(DEST/'b13_07_manifest.json'),
        artifact_count=len(manifest['artifacts']),status='verified_prefix_and_precise_bounded_fallback'))
    print(json.dumps(dict(destination=str(DEST),head=head,bundle_bytes=bundle.stat().st_size,parts=1,verified=True)))

if __name__=='__main__':
    {'prepare':prepare,'deliver':deliver}[sys.argv[1]]()
