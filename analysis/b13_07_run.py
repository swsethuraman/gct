"""Windows bounded launcher: one child, native memory cap, wall clock and PID log."""
import ctypes as C
from ctypes import wintypes as W
import datetime as dt
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
class Memory(C.Structure):
    _fields_ = [('length', W.DWORD), ('load', W.DWORD)] + [(n, C.c_ulonglong) for n in
        ('total_phys', 'available_phys', 'total_page', 'available_page', 'total_virtual', 'available_virtual', 'extended')]
class Basic(C.Structure):
    _fields_ = [('process_time', C.c_longlong), ('job_time', C.c_longlong), ('flags', W.DWORD),
                ('min_ws', C.c_size_t), ('max_ws', C.c_size_t), ('active', W.DWORD),
                ('affinity', C.c_size_t), ('priority', W.DWORD), ('scheduling', W.DWORD)]
class IO(C.Structure):
    _fields_ = [(n, C.c_ulonglong) for n in ('read_ops', 'write_ops', 'other_ops', 'read_bytes', 'write_bytes', 'other_bytes')]
class Limits(C.Structure):
    _fields_ = [('basic', Basic), ('io', IO), ('process_memory', C.c_size_t), ('job_memory', C.c_size_t),
                ('peak_process', C.c_size_t), ('peak_job', C.c_size_t)]

def main():
    tag, seconds, script, *args = sys.argv[1:]
    assert tag.startswith('b13_07_')
    os.chdir(ROOT)
    kernel = C.WinDLL('kernel32', use_last_error=True)
    kernel.CreateJobObjectW.restype = W.HANDLE
    kernel.CreateJobObjectW.argtypes = [C.c_void_p, W.LPCWSTR]
    kernel.SetInformationJobObject.argtypes = [W.HANDLE, C.c_int, C.c_void_p, W.DWORD]
    kernel.AssignProcessToJobObject.argtypes = [W.HANDLE, W.HANDLE]
    kernel.QueryInformationJobObject.argtypes = [W.HANDLE, C.c_int, C.c_void_p, W.DWORD, C.c_void_p]
    kernel.TerminateJobObject.argtypes = [W.HANDLE, W.UINT]
    kernel.CloseHandle.argtypes = [W.HANDLE]
    mem = Memory(); mem.length = C.sizeof(mem)
    assert kernel.GlobalMemoryStatusEx(C.byref(mem))
    preflight = {n: getattr(mem, n) for n, _ in mem._fields_}
    assert mem.available_phys >= 2 * 1024**3, 'Less than 2 GiB free: defer job'
    limits = Limits()
    limits.basic.flags = 0x100 | 0x200 | 0x2000  # process memory, job memory, close ends job
    limits.process_memory = limits.job_memory = 1536 * 1024**2
    job = kernel.CreateJobObjectW(None, None)
    assert job and kernel.SetInformationJobObject(job, 9, C.byref(limits), C.sizeof(limits)), C.get_last_error()
    logdir = ROOT / 'results/logs'; logdir.mkdir(exist_ok=True)
    report = dict(board_numbering='batch13', session_id='B13-07', tag=tag,
                  start_utc=dt.datetime.now(dt.timezone.utc).isoformat(), wall_limit_seconds=int(seconds),
                  memory_limit_bytes=limits.job_memory, preflight=preflight, command=[script] + args,
                  numerical_workers=1, blas_threads=1)
    env = os.environ.copy()
    for k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS', 'BLIS_NUM_THREADS'):
        env[k] = '1'
    env['PYTHONIOENCODING'] = 'utf-8'
    bootstrap = 'import sys,runpy; assert sys.stdin.readline().strip()=="GO"; sys.argv=sys.argv[1:]; runpy.run_path(sys.argv[0],run_name="__main__")'
    start = time.monotonic()
    with open(logdir / (tag + '.log'), 'w', encoding='utf-8') as log:
        child = subprocess.Popen([sys.executable, '-u', '-c', bootstrap, script] + args,
                                 stdin=subprocess.PIPE, stdout=log, stderr=subprocess.STDOUT, env=env, cwd=ROOT)
        (logdir / (tag + '.pid')).write_text(str(child.pid), encoding='ascii')
        report['pid'] = child.pid
        if not kernel.AssignProcessToJobObject(job, W.HANDLE(child._handle)):
            child.terminate(); raise OSError(C.get_last_error(), 'assign job failed before GO')
        child.stdin.write(b'GO\n'); child.stdin.close()
        try:
            report['exit_code'] = child.wait(timeout=int(seconds))
            report['status'] = 'completed' if child.returncode == 0 else 'failed'
        except subprocess.TimeoutExpired:
            kernel.TerminateJobObject(job, 124)
            child.wait(timeout=10)
            report.update(status='wall_limit', exit_code=124)
    actual = Limits()
    assert kernel.QueryInformationJobObject(job, 9, C.byref(actual), C.sizeof(actual), None)
    report.update(seconds=round(time.monotonic() - start, 3), peak_job_bytes=actual.peak_job,
                  peak_process_bytes=actual.peak_process, end_utc=dt.datetime.now(dt.timezone.utc).isoformat())
    kernel.CloseHandle(job)
    (logdir / (tag + '_run.json')).write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report), flush=True)
    return report['exit_code']

if __name__ == '__main__':
    sys.exit(main())
