"""Bound one B13-11 Python worker on Windows before permitting it to execute."""
import argparse
import ctypes
from ctypes import wintypes as w
import datetime
import json
import os
from pathlib import Path
import subprocess
import sys
import time


def memory():
    class M(ctypes.Structure):
        _fields_ = [('length', w.DWORD), ('load', w.DWORD)] + [
            (n, ctypes.c_ulonglong) for n in
            ('total', 'available', 'page', 'available_page', 'virtual', 'available_virtual', 'extended')]
    m = M(); m.length = ctypes.sizeof(m)
    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m)):
        raise ctypes.WinError()
    return {'total_bytes': m.total, 'available_bytes': m.available}


def make_job(limit):
    class BASIC(ctypes.Structure):
        _fields_ = [('process_time', ctypes.c_longlong), ('job_time', ctypes.c_longlong),
                    ('flags', w.DWORD), ('min_working', ctypes.c_size_t),
                    ('max_working', ctypes.c_size_t), ('active', w.DWORD),
                    ('affinity', ctypes.c_size_t), ('priority', w.DWORD), ('scheduling', w.DWORD)]
    class IO(ctypes.Structure):
        _fields_ = [(n, ctypes.c_ulonglong) for n in ('read_ops','write_ops','other_ops','read','write','other')]
    class EXT(ctypes.Structure):
        _fields_ = [('basic', BASIC), ('io', IO), ('process_memory', ctypes.c_size_t),
                    ('job_memory', ctypes.c_size_t), ('peak_process', ctypes.c_size_t),
                    ('peak_job', ctypes.c_size_t)]
    k = ctypes.WinDLL('kernel32', use_last_error=True)
    k.CreateJobObjectW.argtypes = [ctypes.c_void_p, w.LPCWSTR]; k.CreateJobObjectW.restype = w.HANDLE
    k.SetInformationJobObject.argtypes = [w.HANDLE, ctypes.c_int, ctypes.c_void_p, w.DWORD]
    k.AssignProcessToJobObject.argtypes = [w.HANDLE, w.HANDLE]
    k.CloseHandle.argtypes = [w.HANDLE]
    h = k.CreateJobObjectW(None, None)
    if not h: raise ctypes.WinError(ctypes.get_last_error())
    info = EXT(); info.basic.flags = 0x100 | 0x2000  # process memory; end worker when job closes
    info.process_memory = limit
    if not k.SetInformationJobObject(h, 9, ctypes.byref(info), ctypes.sizeof(info)):
        raise ctypes.WinError(ctypes.get_last_error())
    return k, h


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--name', required=True)
    ap.add_argument('--seconds', type=int, default=600)
    ap.add_argument('--memory-mib', type=int, default=1024)
    ap.add_argument('script'); ap.add_argument('args', nargs=argparse.REMAINDER)
    a = ap.parse_args()
    root = Path(__file__).resolve().parents[1]
    logbase = root / 'results' / 'logs' / ('b13_11_' + a.name)
    logbase.parent.mkdir(exist_ok=True)
    info = {'board_numbering':'batch13', 'session_id':'B13-11',
            'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'memory_before': memory(), 'memory_cap_bytes':a.memory_mib * 1024**2,
            'wall_cap_seconds':a.seconds, 'script':a.script, 'args':a.args}
    env = dict(os.environ)
    env.update({n:'1' for n in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS')})
    env['PYTHONIOENCODING'] = 'utf-8'; env['PYTHONDONTWRITEBYTECODE'] = '1'
    bootstrap = ('import sys,runpy; sys.stdin.readline(); '
                 'sys.path.insert(0,"analysis"); sys.argv=sys.argv[1:]; '
                 'runpy.run_path(sys.argv[0],run_name="__main__")')
    k,h = make_job(info['memory_cap_bytes'])
    start = time.monotonic()
    try:
        with logbase.with_suffix('.log').open('w',encoding='utf-8') as log:
            child = subprocess.Popen([sys.executable,'-u','-c',bootstrap,a.script,*a.args],
                                     cwd=root,env=env,stdin=subprocess.PIPE,stdout=log,stderr=subprocess.STDOUT)
            info['pid'] = child.pid
            logbase.with_suffix('.pid').write_text(str(child.pid)+'\n')
            if not k.AssignProcessToJobObject(h,w.HANDLE(int(child._handle))):
                child.terminate(); child.wait()
                raise ctypes.WinError(ctypes.get_last_error())
            info['job_memory_limit_enforced'] = True
            try:
                child.communicate(input=b'\n',timeout=a.seconds)
                info['exit_code'] = child.returncode
            except subprocess.TimeoutExpired:
                child.terminate(); child.wait(); info['exit_code'] = child.returncode
                info['timed_out'] = True
    finally:
        k.CloseHandle(h)
        info['elapsed_seconds'] = round(time.monotonic()-start,3)
        logbase.with_suffix('.run.json').write_text(json.dumps(info,indent=2)+'\n')
    print(json.dumps(info),flush=True)
    return 0 if info.get('exit_code') == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
