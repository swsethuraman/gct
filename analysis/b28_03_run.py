"""Sequential exact-check runner: hard Windows memory cap and 60-second timeout.

Timing/environment/peak memory go only to resource_receipt.json. Child stdout
is stored unchanged; no time or memory measurements enter certificate files.
"""
import ctypes
from ctypes import wintypes as w
import datetime
import hashlib
import json
from pathlib import Path
import runpy
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/b28_03'
SCRIPTS = {'replay': 'analysis/b28_03_replay_source.py', 'cases': 'analysis/b28_03_cases.py'}

def sha(b):
    return hashlib.sha256(b).hexdigest()

def bounded_worker(kind):
    class BASIC(ctypes.Structure):
        _fields_ = [('PerProcessUserTimeLimit', ctypes.c_int64), ('PerJobUserTimeLimit', ctypes.c_int64), ('LimitFlags', w.DWORD), ('MinimumWorkingSetSize', ctypes.c_size_t), ('MaximumWorkingSetSize', ctypes.c_size_t), ('ActiveProcessLimit', w.DWORD), ('Affinity', ctypes.c_size_t), ('PriorityClass', w.DWORD), ('SchedulingClass', w.DWORD)]
    class IO(ctypes.Structure):
        _fields_ = [(name, ctypes.c_uint64) for name in ['ReadOperationCount', 'WriteOperationCount', 'OtherOperationCount', 'ReadTransferCount', 'WriteTransferCount', 'OtherTransferCount']]
    class EXTENDED(ctypes.Structure):
        _fields_ = [('BasicLimitInformation', BASIC), ('IoInfo', IO), ('ProcessMemoryLimit', ctypes.c_size_t), ('JobMemoryLimit', ctypes.c_size_t), ('PeakProcessMemoryUsed', ctypes.c_size_t), ('PeakJobMemoryUsed', ctypes.c_size_t)]
    class MEMORY(ctypes.Structure):
        _fields_ = [('cb', w.DWORD), ('PageFaultCount', w.DWORD)] + [(name, ctypes.c_size_t) for name in ['PeakWorkingSetSize', 'WorkingSetSize', 'QuotaPeakPagedPoolUsage', 'QuotaPagedPoolUsage', 'QuotaPeakNonPagedPoolUsage', 'QuotaNonPagedPoolUsage', 'PagefileUsage', 'PeakPagefileUsage']]
    kernel = ctypes.WinDLL('kernel32', use_last_error=True)
    kernel.CreateJobObjectW.argtypes = [ctypes.c_void_p, w.LPCWSTR]
    kernel.CreateJobObjectW.restype = w.HANDLE
    kernel.SetInformationJobObject.argtypes = [w.HANDLE, ctypes.c_int, ctypes.c_void_p, w.DWORD]
    kernel.AssignProcessToJobObject.argtypes = [w.HANDLE, w.HANDLE]
    kernel.GetCurrentProcess.restype = w.HANDLE
    kernel.QueryInformationJobObject.argtypes = [w.HANDLE, ctypes.c_int, ctypes.c_void_p, w.DWORD, ctypes.c_void_p]
    job = kernel.CreateJobObjectW(None, None)
    if not job:
        raise ctypes.WinError(ctypes.get_last_error())
    limits = EXTENDED()
    limits.BasicLimitInformation.LimitFlags = 0x100 | 0x200 | 0x2000
    limits.ProcessMemoryLimit = limits.JobMemoryLimit = 512*1024*1024
    if not kernel.SetInformationJobObject(job, 9, ctypes.byref(limits), ctypes.sizeof(limits)):
        raise ctypes.WinError(ctypes.get_last_error())
    if not kernel.AssignProcessToJobObject(job, kernel.GetCurrentProcess()):
        raise ctypes.WinError(ctypes.get_last_error())
    runpy.run_path(str(ROOT / SCRIPTS[kind]), run_name='__main__')
    metrics = MEMORY()
    metrics.cb = ctypes.sizeof(metrics)
    psapi = ctypes.WinDLL('psapi', use_last_error=True)
    psapi.GetProcessMemoryInfo.argtypes = [w.HANDLE, ctypes.c_void_p, w.DWORD]
    if not psapi.GetProcessMemoryInfo(kernel.GetCurrentProcess(), ctypes.byref(metrics), ctypes.sizeof(metrics)):
        raise ctypes.WinError(ctypes.get_last_error())
    if not kernel.QueryInformationJobObject(job, 9, ctypes.byref(limits), ctypes.sizeof(limits), None):
        raise ctypes.WinError(ctypes.get_last_error())
    print('RESOURCE ' + json.dumps({'peak_working_set_bytes': metrics.PeakWorkingSetSize, 'peak_job_memory_bytes': limits.PeakJobMemoryUsed, 'hard_memory_limit_bytes': 512*1024*1024}), file=sys.stderr)

def parent(kind):
    receipt_path = OUT / 'resource_receipt.json'
    receipt = json.loads(receipt_path.read_bytes()) if receipt_path.exists() else {'slot': 'B28-03', 'first_clock_observed_utc': '2026-09-24T11:51:54Z', 'session_ceiling_minutes': 60, 'compute_runs_limit': 10, 'per_run_limit_seconds': 60, 'per_run_limit_bytes': 512*1024*1024, 'installs': 0, 'subagents': 0, 'paper_edits': 0, 'runs': [], 'administrative_notes': ['Raw Git blob hashes and sealing are administrative, not mathematical runs.', 'Bundled Python lacked SymPy. Existing Windows Python312 has Python 3.12.10 / SymPy 1.14.0. WSL inspection and package metadata checks performed no mathematics and no installs.']}
    assert len(receipt['runs']) < 10
    inputs = [{'path': p, 'sha256': sha((ROOT / p).read_bytes())} for p in [SCRIPTS[kind], 'analysis/b28_03_run.py']]
    cmd = [sys.executable, '-B', str(Path(__file__).resolve()), '--worker', kind]
    start = time.perf_counter()
    result = subprocess.run(cmd, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60, check=False)
    wall = time.perf_counter() - start
    output = OUT / (kind + '_output.' + ('txt' if kind == 'replay' else 'json'))
    output.write_bytes(result.stdout)
    metadata = result.stderr.decode().strip()
    resource = json.loads(metadata[len('RESOURCE '):]) if metadata.startswith('RESOURCE ') else {'stderr': metadata}
    entry = {'run': len(receipt['runs'])+1, 'kind': kind, 'command': subprocess.list2cmdline(cmd), 'inputs': inputs, 'input_hash_semantics': 'SHA-256 of canonical JSON list of the script and runner path/hash bindings', 'input_sha256': sha(json.dumps(inputs, sort_keys=True, separators=(',', ':')).encode()), 'output_path': output.relative_to(ROOT).as_posix(), 'output_sha256': sha(result.stdout), 'output_bytes': len(result.stdout), 'wall_time_seconds': wall, 'finished_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'exit_code': result.returncode, **resource}
    if kind == 'replay':
        entry['matches_both_archived_outputs_byte_for_byte'] = sha(result.stdout) == 'cae16ecf22d1f63cf0f7b526559ebd726609df8629afe18a1a9f89a8948e03ab'
    receipt['runs'].append(entry)
    receipt['compute_runs_used'] = len(receipt['runs'])
    receipt_path.write_bytes((json.dumps(receipt, indent=2) + '\n').encode())
    print(json.dumps(entry, indent=2))
    assert result.returncode == 0, metadata
    assert wall < 60
    if kind == 'replay':
        assert entry['matches_both_archived_outputs_byte_for_byte']

if __name__ == '__main__':
    if sys.argv[1] == '--worker':
        bounded_worker(sys.argv[2])
    else:
        parent(sys.argv[1])
