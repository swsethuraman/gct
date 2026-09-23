"""R27-03 byte binding and bounded replay logistics (no mathematical search)."""
import ctypes as ct
from ctypes import wintypes as wt
import hashlib, json, os, pathlib, subprocess, sys, tempfile, time

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/b27_03r'
TIP = '7c36a52ddf338eb390a9bcd491cb9c50cf9e2a19'
GIT = ['git', '-c', 'safe.directory=' + ROOT.as_posix(), '-C', str(ROOT)]
JOBS = [('witness', 'witness.json'), ('kernel', 'kernel_run2.json'),
        ('kernel2', 'kernel_run3.json'), ('dims', 'dims_run4.json'),
        ('rays', 'rays_run5.json'), ('deg4', 'deg4_run6.json'), ('ray2', 'ray2_run7.json')]

def sha(b): return hashlib.sha256(b).hexdigest()
def blob(commit, path): return subprocess.check_output(GIT + ['show', commit + ':' + path])
def write_json(path, obj):
    path.write_text(json.dumps(obj, indent=2) + '\n', encoding='utf-8', newline='\n')
def strip_times(obj):
    if isinstance(obj, dict): return {k: strip_times(v) for k,v in obj.items() if k != 'wall_s'}
    if isinstance(obj, list): return [strip_times(v) for v in obj]
    return obj

def prepare():
    assert not OUT.exists()
    manifest_path = 'results/b27_03/MANIFEST.json'
    raw = blob(TIP, manifest_path)
    manifest = json.loads(raw)
    rows = []
    payload_data = {}
    for entry in manifest['payloads']:
        b = blob(TIP, entry['path'])
        assert sha(b) == entry['sha256'] and len(b) == entry['bytes'], entry['path']
        payload_data[entry['path']] = b
        rows.append(dict(entry, matches=True))
    changed = subprocess.check_output(GIT + ['diff-tree','--no-commit-id','--name-only','-r',TIP], text=True).splitlines()
    assert set(changed) == {manifest_path} | set(payload_data)
    inputs = []
    for e in json.loads(payload_data['results/b27_03/INPUT_BINDINGS.json'])['committed_inputs']:
        b = blob(e['commit'], e['path'])
        full = subprocess.check_output(GIT + ['rev-parse', e['commit']], text=True).strip()
        oid = subprocess.check_output(GIT + ['rev-parse', full + ':' + e['path']], text=True).strip()
        assert sha(b) == e['raw_sha256'] and oid == e['blob'], e['path']
        inputs.append(dict(e, commit=full, bytes=len(b), matches=True))
    OUT.mkdir(parents=True)
    (OUT / 'replays').mkdir()
    for path,b in payload_data.items():
        if path.startswith('analysis/'):
            dest = ROOT / 'analysis' / ('b27_03r_source_' + pathlib.Path(path).name)
            assert not dest.exists()
            dest.write_bytes(b)
    write_json(OUT / 'INPUT_BINDINGS.json', {
        'slot':'R27-03', 'producer_tip':TIP,
        'producer_manifest':{'path':manifest_path, 'bytes':len(raw), 'raw_sha256':sha(raw)},
        'producer_payloads':rows, 'manifest_covers_exact_commit_changes':True,
        'producer_bound_inputs':inputs,
        'hash_semantics':'SHA-256 of raw git-show blob bytes, before decoding; bytes counts the same bytes.'})
    print(json.dumps({'manifest_sha256':sha(raw), 'payloads_verified':len(rows), 'inputs_verified':len(inputs)}))

class IO_COUNTERS(ct.Structure):
    _fields_ = [(x, ct.c_ulonglong) for x in ['ReadOperationCount','WriteOperationCount','OtherOperationCount','ReadTransferCount','WriteTransferCount','OtherTransferCount']]
class BASIC_LIMIT(ct.Structure):
    _fields_ = [('PerProcessUserTimeLimit',ct.c_longlong),('PerJobUserTimeLimit',ct.c_longlong),('LimitFlags',wt.DWORD),('MinimumWorkingSetSize',ct.c_size_t),('MaximumWorkingSetSize',ct.c_size_t),('ActiveProcessLimit',wt.DWORD),('Affinity',ct.c_size_t),('PriorityClass',wt.DWORD),('SchedulingClass',wt.DWORD)]
class EXT_LIMIT(ct.Structure):
    _fields_ = [('BasicLimitInformation',BASIC_LIMIT),('IoInfo',IO_COUNTERS),('ProcessMemoryLimit',ct.c_size_t),('JobMemoryLimit',ct.c_size_t),('PeakProcessMemoryUsed',ct.c_size_t),('PeakJobMemoryUsed',ct.c_size_t)]

def run(index, python):
    name, output_name = JOBS[index-1]
    assert not (OUT / f'run{index}_receipt.json').exists()
    scratch = pathlib.Path(tempfile.mkdtemp(prefix='r27_03_replay_'))
    (scratch/'analysis').mkdir()
    inputs = []
    for part in (name, 'kernel_lib'):
        original = f'analysis/b27_03_{part}.py'
        b = blob(TIP, original)
        copied = ROOT / 'analysis' / ('b27_03r_source_' + pathlib.Path(original).name)
        assert copied.read_bytes() == b
        (scratch/original).write_bytes(b)
        inputs.append({'path':original, 'sha256':sha(b), 'bytes':len(b)})
    dest = OUT / 'replays' / output_name
    command = [python, '-B', str(ROOT/'analysis/b27_03r_manage.py'), 'child', str(scratch), name, str(dest)]
    kernel = ct.WinDLL('kernel32', use_last_error=True)
    kernel.CreateJobObjectW.restype = wt.HANDLE
    kernel.SetInformationJobObject.argtypes = [wt.HANDLE,ct.c_int,ct.c_void_p,wt.DWORD]
    kernel.AssignProcessToJobObject.argtypes = [wt.HANDLE,wt.HANDLE]
    kernel.QueryInformationJobObject.argtypes = [wt.HANDLE,ct.c_int,ct.c_void_p,wt.DWORD,ct.c_void_p]
    kernel.TerminateJobObject.argtypes = [wt.HANDLE,wt.UINT]
    kernel.CloseHandle.argtypes = [wt.HANDLE]
    job = kernel.CreateJobObjectW(None,None)
    if not job: raise ct.WinError(ct.get_last_error())
    limits = EXT_LIMIT()
    limits.BasicLimitInformation.LimitFlags = 0x2000 | 0x200
    limits.JobMemoryLimit = 512 * 1024 * 1024
    if not kernel.SetInformationJobObject(job,9,ct.byref(limits),ct.sizeof(limits)): raise ct.WinError(ct.get_last_error())
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
    start = time.perf_counter()
    p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=env)
    if not kernel.AssignProcessToJobObject(job,wt.HANDLE(p._handle)):
        p.kill(); raise ct.WinError(ct.get_last_error())
    timed_out = False
    try:
        log,_ = p.communicate(b'g',timeout=max(0.1,60-(time.perf_counter()-start)))
    except subprocess.TimeoutExpired:
        timed_out=True
        kernel.TerminateJobObject(job,124)
        log,_ = p.communicate()
    elapsed = time.perf_counter()-start
    actual = EXT_LIMIT()
    if not kernel.QueryInformationJobObject(job,9,ct.byref(actual),ct.sizeof(actual),None): raise ct.WinError(ct.get_last_error())
    kernel.CloseHandle(job)
    logpath = OUT / 'replays' / f'run{index}.log'
    logpath.write_bytes(log)
    original_out = blob(TIP, 'results/b27_03/'+output_name)
    new = dest.read_bytes() if dest.exists() else None
    rec = {'run':index, 'command':command, 'equivalent_producer_command':f'python analysis/b27_03_{name}.py {dest}',
           'inputs':inputs, 'wall_seconds':round(elapsed,6), 'limit_seconds':60,
           'memory_limit_bytes':limits.JobMemoryLimit,'peak_job_memory_bytes':actual.PeakJobMemoryUsed,
           'exit_code':p.returncode, 'timed_out':timed_out, 'output':str(dest.relative_to(ROOT)),
           'output_sha256':sha(new) if new else None, 'producer_output_sha256':sha(original_out),
           'raw_output_matches':new==original_out,
           'matches_ignoring_wall_s':strip_times(json.loads(new))==strip_times(json.loads(original_out)) if new else False,
           'log_sha256':sha(log)}
    write_json(OUT/f'run{index}_receipt.json',rec)
    print(json.dumps(rec,indent=2))
    print(log.decode(errors='replace'))

def child(scratch, name, dest):
    sys.stdin.buffer.read(1)
    os.chdir(scratch)
    import runpy
    script = f'analysis/b27_03_{name}.py'
    sys.argv = [script,dest]
    runpy.run_path(script,run_name='__main__')

if __name__ == '__main__':
    if sys.argv[1]=='prepare': prepare()
    elif sys.argv[1]=='run': run(int(sys.argv[2]),sys.argv[3])
    elif sys.argv[1]=='child': child(*sys.argv[2:])
