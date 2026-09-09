"""Windows-native bounded, single-worker launcher (no external dependencies)."""
import argparse, ctypes, datetime, json, os, pathlib, subprocess, sys, time
from ctypes import wintypes as W

ROOT = pathlib.Path(__file__).resolve().parents[1]
LOG = ROOT / 'results/logs'
JOB = None

def memory():
    class MS(ctypes.Structure):
        _fields_ = [('length', W.DWORD), ('load', W.DWORD)] + [(n, ctypes.c_ulonglong) for n in
            ('total_phys', 'available_phys', 'total_page', 'available_page', 'total_virtual', 'available_virtual', 'extended')]
    s = MS(); s.length = ctypes.sizeof(s)
    assert ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(s))
    return {n: getattr(s, n) for n, _ in s._fields_}

def cap(mib):
    global JOB
    class BASIC(ctypes.Structure):
        _fields_ = [('process_time', ctypes.c_longlong), ('job_time', ctypes.c_longlong), ('flags', W.DWORD),
                    ('min_ws', ctypes.c_size_t), ('max_ws', ctypes.c_size_t), ('processes', W.DWORD),
                    ('affinity', ctypes.c_size_t), ('priority', W.DWORD), ('scheduling', W.DWORD)]
    class IO(ctypes.Structure):
        _fields_ = [(n, ctypes.c_ulonglong) for n in ('read_ops','write_ops','other_ops','read_bytes','write_bytes','other_bytes')]
    class EXT(ctypes.Structure):
        _fields_ = [('basic', BASIC), ('io', IO), ('process_memory', ctypes.c_size_t), ('job_memory', ctypes.c_size_t),
                    ('peak_process', ctypes.c_size_t), ('peak_job', ctypes.c_size_t)]
    k = ctypes.WinDLL('kernel32', use_last_error=True)
    k.CreateJobObjectW.restype = W.HANDLE
    k.CreateJobObjectW.argtypes = [ctypes.c_void_p, W.LPCWSTR]
    k.SetInformationJobObject.argtypes = [W.HANDLE, ctypes.c_int, ctypes.c_void_p, W.DWORD]
    k.AssignProcessToJobObject.argtypes = [W.HANDLE, W.HANDLE]
    k.GetCurrentProcess.restype = W.HANDLE
    JOB = k.CreateJobObjectW(None, None)
    assert JOB, ctypes.get_last_error()
    info = EXT(); info.basic.flags = 0x100; info.process_memory = mib * 1024**2
    assert k.SetInformationJobObject(JOB, 9, ctypes.byref(info), ctypes.sizeof(info)), ctypes.get_last_error()
    assert k.AssignProcessToJobObject(JOB, k.GetCurrentProcess()), ctypes.get_last_error()

def main():
    p = argparse.ArgumentParser(); p.add_argument('name'); p.add_argument('mode');
    p.add_argument('--seconds', type=int, default=600); p.add_argument('--mib', type=int, default=768)
    p.add_argument('--child', action='store_true'); p.add_argument('--arg', default='')
    a = p.parse_args(); os.chdir(ROOT)
    for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
        os.environ[key] = '1'
    os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
    if a.child:
        cap(a.mib)
        print(json.dumps({'process_memory_cap_mib': a.mib, 'pid': os.getpid(), 'memory': memory()}), flush=True)
        import b13_02_structural
        cpu_start=time.process_time()
        try: b13_02_structural.main(a.mode, a.arg)
        finally: print(json.dumps({'cpu_seconds':time.process_time()-cpu_start,'utc_finished':datetime.datetime.now(datetime.timezone.utc).isoformat()}),flush=True)
        return
    LOG.mkdir(exist_ok=True)
    before = memory()
    if before['available_phys'] < 2*a.mib*1024**2:
        raise RuntimeError('Insufficient available memory for conservative launch')
    cmd = [sys.executable, __file__, a.name, a.mode, '--child', '--mib', str(a.mib), '--arg', a.arg]
    start = time.time(); status = 'completed'
    os.environ['B13_02_DEADLINE_UNIX']=str(start+a.seconds)
    with open(LOG / f'{a.name}.log', 'w', encoding='utf8') as f:
        proc = subprocess.Popen(cmd, stdout=f, stderr=subprocess.STDOUT,
                                creationflags=subprocess.CREATE_NO_WINDOW, cwd=ROOT)
        (LOG / f'{a.name}.pid').write_text(str(proc.pid))
        while True:
            code=proc.poll()
            elapsed=time.time()-start
            if code is not None:
                if elapsed>a.seconds:status='completed_after_wall_deadline'
                break
            if elapsed>=a.seconds:
                status='wall_time_bound';proc.terminate();code=proc.wait(timeout=10);break
            try:proc.wait(timeout=min(1,a.seconds-elapsed))
            except subprocess.TimeoutExpired:pass
    meta = dict(board_numbering='batch13',session_id='B13-02',mode=a.mode,arg=a.arg,
                command=cmd,pid=proc.pid,seconds=time.time()-start,wall_cap_seconds=a.seconds,
                process_cap_mib=a.mib,memory_before=before,memory_after=memory(),exit_code=code,status=status,
                utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    (LOG / f'{a.name}_run.json').write_text(json.dumps(meta, indent=2))
    print(json.dumps(meta, indent=2)); print((LOG / f'{a.name}.log').read_text()[-6000:])
    sys.exit(0 if code == 0 and status == 'completed' else 1)

if __name__ == '__main__': main()
