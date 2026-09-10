"""Windows launch guard: one child, memory capped before computation, wall limit.

Use: python analysis/b13_12_bounded.py NAME SECONDS SCRIPT [ARGS...]
The child waits on stdin until assigned to a Windows Job Object.
"""
import ctypes as c
from ctypes import wintypes as w
import datetime as dt
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


class Memory(c.Structure):
    _fields_ = [('length', w.DWORD), ('load', w.DWORD)] + [
        (n, c.c_ulonglong) for n in ('total', 'avail', 'page_total', 'page_avail',
                                    'virtual_total', 'virtual_avail', 'extended')]


def memory():
    m = Memory()
    m.length = c.sizeof(m)
    if not c.windll.kernel32.GlobalMemoryStatusEx(c.byref(m)):
        raise c.WinError()
    return {n: getattr(m, n) for n, _ in m._fields_}


class Basic(c.Structure):
    _fields_ = [('process_time', c.c_longlong), ('job_time', c.c_longlong),
                ('flags', w.DWORD), ('min_ws', c.c_size_t), ('max_ws', c.c_size_t),
                ('active', w.DWORD), ('affinity', c.c_size_t),
                ('priority', w.DWORD), ('scheduling', w.DWORD)]


class IO(c.Structure):
    _fields_ = [(n, c.c_ulonglong) for n in ('read_ops', 'write_ops', 'other_ops',
                                          'read_bytes', 'write_bytes', 'other_bytes')]


class Limits(c.Structure):
    _fields_ = [('basic', Basic), ('io', IO), ('process_memory', c.c_size_t),
                ('job_memory', c.c_size_t), ('peak_process', c.c_size_t),
                ('peak_job', c.c_size_t)]


def main():
    if os.name != 'nt':
        raise RuntimeError('This launcher requires Windows; use an equivalent resource guard elsewhere.')
    name, seconds, script, *args = sys.argv[1:]
    assert name.startswith('b13_12_') and all(x.isalnum() or x == '_' for x in name)
    seconds = int(seconds)
    assert 0 < seconds <= 300
    logdir = ROOT / 'results/logs'
    before = memory()
    cap = 1024**3
    if before['avail'] < 2 * cap:
        raise RuntimeError('Less than 2 GiB physical memory available; no computation launched.')
    k = c.WinDLL('kernel32', use_last_error=True)
    k.CreateJobObjectW.argtypes = [c.c_void_p, w.LPCWSTR]
    k.CreateJobObjectW.restype = w.HANDLE
    k.SetInformationJobObject.argtypes = [w.HANDLE, c.c_int, c.c_void_p, w.DWORD]
    k.AssignProcessToJobObject.argtypes = [w.HANDLE, w.HANDLE]
    k.QueryInformationJobObject.argtypes = [w.HANDLE, c.c_int, c.c_void_p, w.DWORD, c.c_void_p]
    k.TerminateJobObject.argtypes = [w.HANDLE, w.UINT]
    k.CloseHandle.argtypes = [w.HANDLE]
    job = k.CreateJobObjectW(None, None)
    if not job:
        raise c.WinError(c.get_last_error())
    limits = Limits()
    limits.basic.flags = 0x2000 | 0x100  # close job on exit, process-memory bound
    limits.process_memory = cap
    if not k.SetInformationJobObject(job, 9, c.byref(limits), c.sizeof(limits)):
        raise c.WinError(c.get_last_error())
    env = dict(os.environ)
    env.update({v: '1' for v in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS',
                               'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS')})
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    bootstrap = "import sys,runpy; assert sys.stdin.readline().strip()=='GO'; p=sys.argv[1]; sys.argv=sys.argv[1:]; runpy.run_path(p,run_name='__main__')"
    record = dict(board_numbering='batch13', session_id='B13-12', name=name,
                  started_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
                  command=[sys.executable, script] + args, memory_before=before,
                  process_memory_cap_bytes=cap, wall_cap_seconds=seconds,
                  workers=1, blas_threads=1)
    start = time.monotonic()
    proc = None
    try:
        with (logdir / (name + '.log')).open('w', encoding='utf-8') as log:
            proc = subprocess.Popen([sys.executable, '-u', '-c', bootstrap, script] + args,
                                    cwd=ROOT, env=env, stdin=subprocess.PIPE, stdout=log,
                                    stderr=subprocess.STDOUT, text=True,
                                    creationflags=subprocess.CREATE_NO_WINDOW)
            (logdir / (name + '.pid')).write_text(str(proc.pid) + '\n')
            record['pid'] = proc.pid
            if not k.AssignProcessToJobObject(job, w.HANDLE(proc._handle)):
                proc.stdin.close()  # bootstrap cannot proceed without GO
                proc.wait(timeout=10)
                raise c.WinError(c.get_last_error())
            proc.stdin.write('GO\n')
            proc.stdin.flush()
            proc.stdin.close()
            try:
                proc.wait(timeout=seconds)
                record['outcome'] = 'completed' if proc.returncode == 0 else 'nonzero_exit'
            except subprocess.TimeoutExpired:
                k.TerminateJobObject(job, 124)
                proc.wait(timeout=10)
                record['outcome'] = 'wall_limit'
            record['exit_code'] = proc.returncode
            used = Limits()
            if k.QueryInformationJobObject(job, 9, c.byref(used), c.sizeof(used), None):
                record['peak_process_commit_bytes'] = used.peak_process
                record['peak_job_commit_bytes'] = used.peak_job
    finally:
        k.CloseHandle(job)
        record['elapsed_seconds'] = round(time.monotonic() - start, 3)
        record['memory_after'] = memory()
        (logdir / (name + '_resources.json')).write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps(record, indent=2))
    if record.get('exit_code'):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
