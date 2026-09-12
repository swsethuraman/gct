"""One Windows calculation, gated before runpy, with a Job memory limit."""
import argparse, ctypes as C, datetime, json, os, pathlib, subprocess, sys, time
from ctypes import wintypes as W

class BASIC(C.Structure):
    _fields_ = [('PerProcessUserTimeLimit', C.c_longlong), ('PerJobUserTimeLimit', C.c_longlong),
                ('LimitFlags', W.DWORD), ('MinimumWorkingSetSize', C.c_size_t),
                ('MaximumWorkingSetSize', C.c_size_t), ('ActiveProcessLimit', W.DWORD),
                ('Affinity', C.c_size_t), ('PriorityClass', W.DWORD), ('SchedulingClass', W.DWORD)]
class IO(C.Structure):
    _fields_ = [(x, C.c_ulonglong) for x in ('ReadOperationCount','WriteOperationCount',
                'OtherOperationCount','ReadTransferCount','WriteTransferCount','OtherTransferCount')]
class EXT(C.Structure):
    _fields_ = [('BasicLimitInformation', BASIC), ('IoInfo', IO),
                ('ProcessMemoryLimit', C.c_size_t), ('JobMemoryLimit', C.c_size_t),
                ('PeakProcessMemoryUsed', C.c_size_t), ('PeakJobMemoryUsed', C.c_size_t)]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--name', required=True); ap.add_argument('--seconds', type=int, default=120)
    ap.add_argument('--mib', type=int, default=1024); ap.add_argument('command', nargs=argparse.REMAINDER)
    a = ap.parse_args(); command = a.command
    if command and command[0] == '--': command = command[1:]
    if not command: raise ValueError('required Python script missing')
    logs = pathlib.Path('results/logs'); logs.mkdir(exist_ok=True)
    k = C.WinDLL('kernel32', use_last_error=True)
    k.CreateJobObjectW.restype = W.HANDLE; k.CreateJobObjectW.argtypes = [C.c_void_p, W.LPCWSTR]
    k.SetInformationJobObject.argtypes = [W.HANDLE, C.c_int, C.c_void_p, W.DWORD]
    k.AssignProcessToJobObject.argtypes = [W.HANDLE, W.HANDLE]
    k.QueryInformationJobObject.argtypes = [W.HANDLE, C.c_int, C.c_void_p, W.DWORD, C.c_void_p]
    k.CloseHandle.argtypes = [W.HANDLE]
    job = k.CreateJobObjectW(None, None)
    if not job: raise C.WinError(C.get_last_error())
    limit = EXT(); limit.BasicLimitInformation.LimitFlags = 0x100 | 0x2000
    limit.ProcessMemoryLimit = a.mib * 1024**2
    if not k.SetInformationJobObject(job, 9, C.byref(limit), C.sizeof(limit)):
        raise C.WinError(C.get_last_error())
    env = dict(os.environ, PYTHONUTF8='1', PYTHONDONTWRITEBYTECODE='1', OMP_NUM_THREADS='1',
               OPENBLAS_NUM_THREADS='1', MKL_NUM_THREADS='1', NUMEXPR_NUM_THREADS='1')
    bootstrap = "import sys,runpy,pathlib; assert sys.stdin.readline().strip()=='GO'; p=sys.argv[1]; sys.argv=sys.argv[1:]; sys.path.insert(0,str(pathlib.Path(p).resolve().parent)); runpy.run_path(p,run_name='__main__')"
    start = time.monotonic(); utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    status = 'completed'
    with (logs / (a.name + '.log')).open('w', encoding='utf-8') as log:
        p = subprocess.Popen([sys.executable, '-u', '-c', bootstrap, *command], env=env,
                             stdin=subprocess.PIPE, stdout=log, stderr=subprocess.STDOUT, text=True)
        (logs / (a.name + '.pid')).write_text(str(p.pid) + '\n')
        if not k.AssignProcessToJobObject(job, W.HANDLE(p._handle)):
            p.terminate(); p.wait(); raise C.WinError(C.get_last_error())
        p.stdin.write('GO\n'); p.stdin.close()
        try: p.wait(timeout=a.seconds)
        except subprocess.TimeoutExpired:
            status = 'resource_stopped_wall_time'; p.terminate(); p.wait()
        if p.returncode and status == 'completed': status = 'failed'
    usage = EXT()
    if not k.QueryInformationJobObject(job, 9, C.byref(usage), C.sizeof(usage), None):
        raise C.WinError(C.get_last_error())
    k.CloseHandle(job)
    record = dict(start_utc=utc, elapsed_seconds=round(time.monotonic()-start, 3), pid=p.pid,
                  command=command, wall_limit_seconds=a.seconds, process_memory_limit_bytes=limit.ProcessMemoryLimit,
                  peak_process_commit_bytes=usage.PeakProcessMemoryUsed, status=status, exit_code=p.returncode,
                  enforcement='Windows Job process-memory limit before calculation; subprocess timeout; thread env=1')
    (logs / (a.name + '.resource.json')).write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps(record)); print((logs / (a.name + '.log')).read_text(encoding='utf-8')[-12000:])
    return p.returncode

if __name__ == '__main__': sys.exit(main())
