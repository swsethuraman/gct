"""Bounded sequential Windows runner; every invocation records its raw input/output hashes."""
import contextlib
import ctypes as C
from ctypes import wintypes as W
import hashlib
import io
import json
from pathlib import Path
import runpy
import sys
import threading
import time
import traceback
import os

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/b27_02'

def binding(path):
    raw = path.read_bytes()
    return {'path': path.relative_to(ROOT).as_posix(), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}

def cap():
    class Basic(C.Structure):
        _fields_ = [('process_time', C.c_longlong), ('job_time', C.c_longlong), ('flags', W.DWORD),
                    ('minimum', C.c_size_t), ('maximum', C.c_size_t), ('active', W.DWORD),
                    ('affinity', C.c_size_t), ('priority', W.DWORD), ('scheduling', W.DWORD)]
    class IO(C.Structure):
        _fields_ = [(n, C.c_ulonglong) for n in ('read_ops','write_ops','other_ops','read_bytes','write_bytes','other_bytes')]
    class Extended(C.Structure):
        _fields_ = [('basic', Basic), ('io', IO), ('process_memory', C.c_size_t), ('job_memory', C.c_size_t),
                    ('peak_process', C.c_size_t), ('peak_job', C.c_size_t)]
    kernel = C.WinDLL('kernel32', use_last_error=True)
    kernel.CreateJobObjectW.restype = W.HANDLE
    kernel.CreateJobObjectW.argtypes = [C.c_void_p, W.LPCWSTR]
    kernel.SetInformationJobObject.argtypes = [W.HANDLE, C.c_int, C.c_void_p, W.DWORD]
    kernel.GetCurrentProcess.restype = W.HANDLE
    kernel.AssignProcessToJobObject.argtypes = [W.HANDLE, W.HANDLE]
    kernel.QueryInformationJobObject.argtypes = [W.HANDLE, C.c_int, C.c_void_p, W.DWORD, C.c_void_p]
    job = kernel.CreateJobObjectW(None, None)
    if not job:
        raise C.WinError(C.get_last_error())
    info = Extended()
    info.basic.flags = 0x100 | 0x200 | 0x2000
    info.process_memory = info.job_memory = 512 * 1024 ** 2
    if not kernel.SetInformationJobObject(job, 9, C.byref(info), C.sizeof(info)):
        raise C.WinError(C.get_last_error())
    if not kernel.AssignProcessToJobObject(job, kernel.GetCurrentProcess()):
        raise C.WinError(C.get_last_error())
    def statistics():
        info = Extended()
        if not kernel.QueryInformationJobObject(job, 9, C.byref(info), C.sizeof(info), None):
            raise C.WinError(C.get_last_error())
        return {'peak_job_bytes': info.peak_job, 'peak_process_bytes': info.peak_process}
    return job, statistics

tag, mode = sys.argv[1:]
assert tag in ('run01', 'run02') and mode in ('grouped', 'full')
receipt_path = OUT / (tag + '_resources.json')
output_path = OUT / (tag + '_output.json')
assert not receipt_path.exists() and not output_path.exists(), 'Refuse to overwrite a run'
assert len(list(OUT.glob('run*_resources.json'))) < 10
command_argv = [sys.executable, str(Path(__file__).resolve()), tag, mode]
inputs = [ROOT / 'analysis/b27_02_run.py', ROOT / 'analysis/b27_02_verify.py', OUT / 'candidate.json', OUT / 'INPUT_BINDINGS.json']
meta = {'label': 'COMPUTED resource receipt', 'command_argv': command_argv, 'cwd': str(ROOT),
        'started_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'inputs': [binding(p) for p in inputs],
        'input_sha256_domain': 'raw file bytes, no newline conversion', 'wall_cap_seconds': 55,
        'memory_cap_bytes': 512 * 1024 ** 2, 'sequential_workers': 1, 'python': sys.version}
receipt_path.write_text(json.dumps(meta, indent=2) + '\n')
job, statistics = cap()
meta['job_object_enforced'] = bool(job)
timer = threading.Timer(55, lambda: os._exit(124))
timer.daemon = True
timer.start()
started = time.perf_counter()
buffer = io.StringIO()
exit_code = 0
try:
    sys.argv = [str(ROOT / 'analysis/b27_02_verify.py'), mode]
    with contextlib.redirect_stdout(buffer), contextlib.redirect_stderr(buffer):
        runpy.run_path(sys.argv[0], run_name='__main__')
except BaseException:
    exit_code = 1
    buffer.write(traceback.format_exc())
finally:
    meta['wall_seconds'] = time.perf_counter() - started
    timer.cancel()
    meta.update(statistics())
    meta['exit_code'] = exit_code
    output_path.write_bytes(buffer.getvalue().encode('utf-8'))
    meta['output'] = binding(output_path)
    receipt_path.write_bytes((json.dumps(meta, indent=2) + '\n').encode())
    print(json.dumps(meta, indent=2))
if exit_code:
    print(buffer.getvalue())
raise SystemExit(exit_code)
