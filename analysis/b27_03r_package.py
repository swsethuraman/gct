"""Administrative receipt and manifest generation; no mathematical computation."""
import datetime, hashlib, json, pathlib, subprocess

ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/'results/b27_03r'
LAUNCH=ROOT.parents[2]/'Claude_Handover_B15_B18/post_b19_housekeeping_20260917/batch27_launch'
GIT=['git','-c','safe.directory='+ROOT.as_posix(),'-C',str(ROOT)]
def digest(b): return hashlib.sha256(b).hexdigest()
def save(path,obj): path.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8',newline='\n')
def binding(commit,path,read_scope):
    full=subprocess.check_output(GIT+['rev-parse',commit],text=True).strip()
    b=subprocess.check_output(GIT+['show',full+':'+path])
    oid=subprocess.check_output(GIT+['rev-parse',full+':'+path],text=True).strip()
    return {'commit':full,'path':path,'blob':oid,'raw_sha256':digest(b),'bytes':len(b),'read_scope':read_scope}

briefs=[]
for name in ('B27_COMMON.md','R27-REVIEWS.md','BATCH27_BOARD.md','B27-03.md'):
    b=(LAUNCH/name).read_bytes()
    briefs.append({'path':str(LAUNCH/name),'bytes':len(b),'raw_sha256':digest(b)})
save(OUT/'PREFLIGHT.json',{
    'slot':'R27-03','reviewer_lineage':'Astra','prior_production_exposure':False,
    'branch':'b27-03r','expected_and_observed_head':'fcff7eeaa491aab4a3b1d1ba1161c24a89dae818',
    'tracked_and_untracked_status_at_preflight':'clean',
    'output_paths_absent_at_preflight':['docs/b27_03r_review.md','results/b27_03r/'],
    'producer_remote_tip_at_preflight':'7c36a52ddf338eb390a9bcd491cb9c50cf9e2a19',
    'reviewer_remote_tip_at_preflight':'fcff7eeaa491aab4a3b1d1ba1161c24a89dae818',
    'briefs':briefs,
    'setup_record':{'path':str(LAUNCH.parent/'B27_PART25_SETUP_RECEIPTS.json'),
                    'raw_sha256':digest((LAUNCH.parent/'B27_PART25_SETUP_RECEIPTS.json').read_bytes())},
    'hash_semantics':'SHA-256 of named raw file bytes, before decoding or newline conversion.',
    'notes':['Git used a command-local safe.directory setting; no global configuration was changed.',
             'Network/read-runtime access used approved sandbox escalations.',
             'No mismatch of brief hashes, branch, setup HEAD, cleanliness, output absence or pushed producer was found.']})
save(OUT/'ADDITIONAL_INPUTS.json',{
    'hash_semantics':'SHA-256 and byte count of raw git-show blob bytes before decoding.',
    'committed_inputs':[binding('01c49022','docs/b17_01_report.md','Header, ruled-components lemma, smooth-cubic consequence, explicit-witness and representation discussion; external literature not re-read.')],
    'producer_bound_read_scopes':{
        'docs/post_b19_20260917/claude_gkz_incidence_20260917/scope_corrigendum/CORRIGENDUM.md':'C10, inspected directly; other excerpts contextual only.',
        'docs/balanced_corner.md':'Cost, scope and one-sided-certificate passages; historical computations not replayed.',
        'results/a26_01/EXCLUSIONS.md':'Onset/adopted-premise and surrounding exclusion rows.',
        'other_bound_inputs':'Relevant mathematical statements read; binding verification alone is not acceptance of all historical claims.'}})

receipts=[json.loads((OUT/f'run{i}_receipt.json').read_bytes()) for i in range(1,9)]
assert all(r['exit_code']==0 and not r['timed_out'] for r in receipts)
assert all(r['wall_seconds']<60 and r['peak_job_memory_bytes']<512_000_000 for r in receipts)
assert all(r['matches_ignoring_wall_s'] is True for r in receipts[:7])
lines=['# R27-03 resource receipt','',
       'Eight mathematical runs, sequential: seven exact producer replays plus one independent verification. No installs or searches. All commands and input/output/log hashes are in the corresponding runN_receipt.json.',
       '', 'Runtime: installed Python 3.12.10, SymPy 1.14.0, NumPy 2.4.6. The bundled runtime lacked SymPy and was used only for administrative byte binding.',
       '', 'Each mathematical child waited for its supervisor to assign a Windows Job Object, then received the start token. The supervisor enforced 60 seconds wall time and a 512 MiB committed job-memory cap, queried PeakJobMemoryUsed, and recorded it. Every measured peak was also below the stricter decimal 512 MB threshold. OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1 were set. No mathematical runs overlapped.',
       '', '| Run | Script suffix | Wall seconds | Peak job bytes | Raw output equals producer | Mathematical JSON equals producer |',
       '|---|---|---:|---:|---|---|']
names=['witness','kernel','kernel2','dims','rays','deg4','ray2','independent']
for r,name in zip(receipts,names):
    lines.append(f"| {r['run']} | {name} | {r['wall_seconds']:.6f} | {r['peak_job_memory_bytes']} | {'no' if r['run']<=7 else 'not applicable'} | {'yes, ignoring only wall_s' if r['run']<=7 else 'independent certificate'} |")
lines += ['', 'Raw output SHA-256 values (hashes name the exact files on disk, with no normalization):','',
          '| Run | Reviewer output SHA-256 | Producer output SHA-256 |','|---|---|---|']
for r in receipts:
    lines.append(f"| {r['run']} | `{r['output_sha256']}` | `{r['producer_output_sha256'] or 'not applicable'}` |")
lines += ['', 'The mathematical comparison parses both JSON files and recursively removes only dictionary keys exactly named wall_s. Every other value, key and list order agrees on all seven replays. Raw output hashes do not agree; timing fields prevent byte-identical reexecution. No changed source code or frozen clock was used to force a match.',
          '', 'Runs 1–7 executed the manager version preserved byte-for-byte as analysis/b27_03r_manage_replays.py, SHA-256 '+digest((ROOT/'analysis/b27_03r_manage_replays.py').read_bytes())+'. The final analysis/b27_03r_manage.py adds support for independent run 8 without changing the seven replay algorithms. Producer code was extracted with git show and executed from isolated temporary analysis directories with its original filenames and imports. Delivered source copies are under analysis/b27_03r_source_*. The library is recorded as an input even for the witness and dimension jobs that do not import it.',
          '', 'Independent run 8 imports no producer mathematics. Its premise is the committed witness JSON. It expands the permanent via sparse integer polynomial multiplication, independently forms gradient Macaulay matrices and nonzero minors, checks prime moduli by exhaustive trial division, verifies the two previously approximate stable-degree dimensions, and checks the stated degree-five combinatorial price. Matrix hashes in independent_run8.json name UTF-8 bytes of json.dumps(matrix,separators=(",",":")), without a trailing newline.',
          '', 'Administrative Python, PowerShell and Git operations only located installed runtimes, copied/read files, hashed and compared bytes, generated receipts/manifests or managed this branch. These are not mathematical runs. The two initial interpreter/import probes found no usable sandbox-PATH Python/SymPy; they did not run mathematical scripts.',
          '', 'First recorded clock after intake: 2026-09-23 04:11:29 UTC. All mathematical runs finished before 2026-09-23 04:18:41 UTC. Initial intake was not separately timestamped. Packet generation UTC: '+datetime.datetime.now(datetime.timezone.utc).isoformat()+'.',
          '', 'No follow-up computation, installation, subagent/session, task message, publication or automatic continuation was launched.']
(OUT/'RESOURCE_RECEIPT.md').write_text('\n'.join(lines)+'\n',encoding='utf-8',newline='\n')

manifest_path=OUT/'MANIFEST.json'
payloads=sorted([ROOT/'docs/b27_03r_review.md']+list((ROOT/'analysis').glob('b27_03r_*.py'))+
                [p for p in OUT.rglob('*') if p.is_file() and p!=manifest_path])
entries=[]
for path in payloads:
    raw=path.read_bytes()
    entries.append({'path':path.relative_to(ROOT).as_posix(),'bytes':len(raw),'sha256':digest(raw)})
save(manifest_path,{'slot':'R27-03','branch':'b27-03r',
     'parent':'fcff7eeaa491aab4a3b1d1ba1161c24a89dae818',
     'producer_tip':'7c36a52ddf338eb390a9bcd491cb9c50cf9e2a19',
     'excludes':'results/b27_03r/MANIFEST.json (itself)',
     'hash_semantics':'Every SHA-256 and byte count names the raw bytes of the listed payload; no normalization.',
     'payloads':entries})
print(json.dumps({'payload_count':len(entries),'manifest_sha256':digest(manifest_path.read_bytes()),
                  'total_mathematical_seconds':sum(r['wall_seconds'] for r in receipts),
                  'maximum_peak_job_bytes':max(r['peak_job_memory_bytes'] for r in receipts)}))
