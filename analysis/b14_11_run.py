"""Bound one B14-11 calculation on Windows; logs and PID are session-specific."""
import argparse, ctypes, json, os, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / 'results/logs'
LIMIT = 1536 * 1024**2
JOB = None


def memory_limit():
    global JOB
    if os.name != 'nt':
        import resource
        resource.setrlimit(resource.RLIMIT_AS, (LIMIT, LIMIT))
        return
    from ctypes import wintypes as w
    class Basic(ctypes.Structure):
        _fields_ = [('a', ctypes.c_longlong), ('b', ctypes.c_longlong),
                    ('flags', w.DWORD), ('minws', ctypes.c_size_t),
                    ('maxws', ctypes.c_size_t), ('active', w.DWORD),
                    ('affinity', ctypes.c_size_t), ('priority', w.DWORD), ('sched', w.DWORD)]
    class IO(ctypes.Structure):
        _fields_ = [(s, ctypes.c_ulonglong) for s in ['ro','wo','oo','rb','wb','ob']]
    class Extended(ctypes.Structure):
        _fields_ = [('basic', Basic), ('io', IO), ('process', ctypes.c_size_t),
                    ('job', ctypes.c_size_t), ('peakprocess', ctypes.c_size_t),
                    ('peakjob', ctypes.c_size_t)]
    k = ctypes.WinDLL('kernel32', use_last_error=True)
    k.CreateJobObjectW.restype = w.HANDLE
    k.CreateJobObjectW.argtypes = [ctypes.c_void_p, w.LPCWSTR]
    k.SetInformationJobObject.argtypes = [w.HANDLE, ctypes.c_int, ctypes.c_void_p, w.DWORD]
    k.AssignProcessToJobObject.argtypes = [w.HANDLE, w.HANDLE]
    k.GetCurrentProcess.restype = w.HANDLE
    JOB = k.CreateJobObjectW(None, None)
    info = Extended(); info.basic.flags = 0x100; info.process = LIMIT
    if not JOB or not k.SetInformationJobObject(JOB, 9, ctypes.byref(info), ctypes.sizeof(info)):
        raise ctypes.WinError(ctypes.get_last_error())
    if not k.AssignProcessToJobObject(JOB, k.GetCurrentProcess()):
        raise ctypes.WinError(ctypes.get_last_error())


def peak_memory():
    if os.name != 'nt':
        import resource
        return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
    class PMC(ctypes.Structure):
        _fields_ = [('cb', ctypes.c_ulong), ('faults', ctypes.c_ulong)] + [
            (s, ctypes.c_size_t) for s in ['peakws','ws','peakpaged','paged','peaknonpaged','nonpaged','pagefile','peakpagefile']]
    p = PMC(); p.cb = ctypes.sizeof(p)
    k = ctypes.WinDLL('kernel32'); k.GetCurrentProcess.restype = ctypes.c_void_p
    f = ctypes.WinDLL('psapi').GetProcessMemoryInfo
    f.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulong]
    if not f(k.GetCurrentProcess(), ctypes.byref(p), p.cb): raise ctypes.WinError()
    return p.peakws


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--seconds', type=int, default=300)
    ap.add_argument('--tag', required=True); ap.add_argument('worker_args', nargs=argparse.REMAINDER)
    args = ap.parse_args(); assert 1 <= args.seconds <= 300
    assert args.tag.startswith('b14_11_') and '/' not in args.tag and '\\' not in args.tag
    LOG.mkdir(exist_ok=True)
    env = os.environ.copy()
    for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:
        env[k] = '1'
    env['PYTHONHASHSEED'] = '0'; env['PYTHONUNBUFFERED'] = '1'
    start = time.time(); cmd = [sys.executable, '-u', str(ROOT/'analysis/b14_11_work.py'), *args.worker_args]
    with (LOG/(args.tag+'.log')).open('w', encoding='utf-8') as log:
        proc = subprocess.Popen(cmd, cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT)
        (LOG/(args.tag+'.pid')).write_text(str(proc.pid)+'\n')
        try:
            rc = proc.wait(timeout=args.seconds); status = 'COMPLETE' if rc == 0 else 'FAILED'
        except subprocess.TimeoutExpired:
            proc.kill(); proc.wait(); rc = proc.returncode; status = 'RESOURCE_KILLED_TIMEOUT'
    result = dict(command=cmd, pid=proc.pid, started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime(start)),
                  wall_seconds=round(time.time()-start,3), timeout_seconds=args.seconds,
                  process_commit_limit_bytes=LIMIT, threads=1, exit_code=rc,status=status)
    (LOG/(args.tag+'.run.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result)); print((LOG/(args.tag+'.log')).read_text(encoding='utf-8')[-3500:])
    return 0 if rc == 0 else 1

if __name__ == '__main__': sys.exit(main())
