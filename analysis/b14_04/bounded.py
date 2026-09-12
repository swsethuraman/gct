"""One-worker wall/commit-memory supervisor; stdlib, Windows Job Object."""
import argparse
import ctypes
from ctypes import wintypes as w
import json
import os
from pathlib import Path
import subprocess
import sys
import time


def windows_job(process, mib):
    class Basic(ctypes.Structure):
        _fields_ = [("process_time", ctypes.c_longlong), ("job_time", ctypes.c_longlong),
                    ("flags", w.DWORD), ("min_ws", ctypes.c_size_t),
                    ("max_ws", ctypes.c_size_t), ("active", w.DWORD),
                    ("affinity", ctypes.c_size_t), ("priority", w.DWORD),
                    ("scheduling", w.DWORD)]
    class IO(ctypes.Structure):
        _fields_ = [(n, ctypes.c_ulonglong) for n in
                    ("read_ops", "write_ops", "other_ops", "read_bytes", "write_bytes", "other_bytes")]
    class Extended(ctypes.Structure):
        _fields_ = [("basic", Basic), ("io", IO), ("process_limit", ctypes.c_size_t),
                    ("job_limit", ctypes.c_size_t), ("peak_process", ctypes.c_size_t),
                    ("peak_job", ctypes.c_size_t)]
    k = ctypes.WinDLL("kernel32", use_last_error=True)
    k.CreateJobObjectW.restype = w.HANDLE
    k.CreateJobObjectW.argtypes = [ctypes.c_void_p, w.LPCWSTR]
    k.SetInformationJobObject.argtypes = [w.HANDLE, ctypes.c_int, ctypes.c_void_p, w.DWORD]
    k.AssignProcessToJobObject.argtypes = [w.HANDLE, w.HANDLE]
    k.QueryInformationJobObject.argtypes = [w.HANDLE, ctypes.c_int, ctypes.c_void_p, w.DWORD, ctypes.c_void_p]
    k.CloseHandle.argtypes = [w.HANDLE]
    job = k.CreateJobObjectW(None, None)
    if not job:
        raise ctypes.WinError(ctypes.get_last_error())
    info = Extended()
    info.basic.flags = 0x100 | 0x2000  # process commit limit + close ends contained worker
    info.process_limit = mib * 1024 * 1024
    if not k.SetInformationJobObject(job, 9, ctypes.byref(info), ctypes.sizeof(info)):
        raise ctypes.WinError(ctypes.get_last_error())
    if not k.AssignProcessToJobObject(job, w.HANDLE(int(process._handle))):
        raise ctypes.WinError(ctypes.get_last_error())

    def finish():
        queried = bool(k.QueryInformationJobObject(job, 9, ctypes.byref(info), ctypes.sizeof(info), None))
        peak = info.peak_process if queried else None
        k.CloseHandle(job)
        return peak
    return finish


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--seconds", required=True, type=float)
    ap.add_argument("--memory-mib", type=int, default=1024)
    ap.add_argument("script")
    ap.add_argument("args", nargs=argparse.REMAINDER)
    a = ap.parse_args()
    root = Path(__file__).resolve().parents[2]
    logroot = root / "results/logs"
    logroot.mkdir(exist_ok=True)
    stem = logroot / ("b14_04_" + a.name)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONUNBUFFERED="1")
    for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
        env[name] = "1"
    bootstrap = "import runpy,sys; sys.stdin.readline(); sys.argv=sys.argv[1:]; runpy.run_path(sys.argv[0],run_name='__main__')"
    command = [sys.executable, "-u", "-c", bootstrap, a.script] + a.args
    started = time.monotonic()
    record = {"command": command, "utc_start": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
              "wall_limit_seconds": a.seconds, "memory_limit_mib": a.memory_mib,
              "threads": 1, "platform": sys.platform, "status": "STARTING"}
    with stem.with_suffix(".log").open("w", encoding="utf-8") as log:
        proc = subprocess.Popen(command, cwd=root, env=env, stdin=subprocess.PIPE,
                                stdout=log, stderr=subprocess.STDOUT)
        stem.with_suffix(".pid").write_text(str(proc.pid) + "\n")
        record["pid"] = proc.pid
        finish = None
        try:
            if sys.platform != "win32":
                raise RuntimeError("This supervisor implements Windows Job Objects; use OS limits on other hosts")
            finish = windows_job(proc, a.memory_mib)
            record["limit_enforced_before_work"] = True
            proc.stdin.write(b"\n")
            proc.stdin.close()
            while proc.poll() is None:
                if time.monotonic() - started > a.seconds:
                    assert int(stem.with_suffix(".pid").read_text()) == proc.pid
                    proc.terminate()
                    record["status"] = "RESOURCE_STOPPED_WALL"
                    break
                time.sleep(0.1)
            proc.wait(timeout=10)
            if record["status"] == "STARTING":
                record["status"] = "COMPLETE" if proc.returncode == 0 else "FAILED"
        except Exception as exc:
            record["status"] = "SUPERVISOR_FAILED"
            record["error"] = repr(exc)
            if proc.poll() is None:
                proc.terminate()
            proc.wait(timeout=10)
        finally:
            record["peak_commit_bytes"] = finish() if finish else None
            record["exit_code"] = proc.returncode
            record["wall_seconds"] = time.monotonic() - started
            stem.with_suffix(".resources.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(record, indent=2))
    return 0 if record["status"] == "COMPLETE" else 1


if __name__ == "__main__":
    sys.exit(main())
