#!/usr/bin/env python3
"""Session 74 driver -- the determinant column accumulates rung by rung (integrator
relay, batch-12 note 3): whenever a birth rung lands, pause the birth streams
(SIGSTOP on their recorded process group), evaluate the new rows on the det
column at P1, read the running lower bound rank T_det(24) >= m, bank, resume.
When the streams end: pad at P1, decision, then the remaining columns and P2.

Every subprocess is bounded by `timeout`; the streams are paused/resumed only by
the process-group id recorded in results/logs/s74_births_1319b.pid, never by name.
State: results/s74/driver_state.json.  Log: results/logs/s74_driver.log.
"""
import json
import os
import signal
import subprocess
import sys
import time

ROOT = "/home/claude/gct"
OUT = os.path.join(ROOT, "results", "s74")
LOGS = os.path.join(ROOT, "results", "logs")
P1, P2 = 2147483647, 2147483629
BIRTH = {13: 37, 14: 54, 15: 52, 16: 43, 17: 31, 18: 22, 19: 14}
STATE = os.path.join(OUT, "driver_state.json")
TRAILER = "\n\nCo-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"


def log(msg):
    line = f"[{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}] {msg}"
    print(line, flush=True)
    with open(os.path.join(LOGS, "s74_driver.log"), "a", encoding="utf-8") as f:
        f.write(line + "\n")


def run(label, tmo, args):
    log(f"start {label}: {' '.join(args)}")
    with open(os.path.join(LOGS, f"s74_{label}.log"), "a", encoding="utf-8") as f:
        rc = subprocess.call(["timeout", str(tmo)] + args, cwd=ROOT, stdout=f, stderr=subprocess.STDOUT)
    log(f"end {label} (exit {rc})")
    return rc


def bank(msg):
    subprocess.call(["git", "add", "-A", "results/s74", "results/logs", "results/certs"], cwd=ROOT)
    rc = subprocess.call(["git", "commit", "-q", "-m", msg + TRAILER], cwd=ROOT)
    log(f"commit ({'ok' if rc == 0 else 'nothing to commit'}): {msg}")


def births_pgid():
    try:
        pid = int(open(os.path.join(LOGS, "s74_births_1319b.pid")).read().strip())
        os.kill(pid, 0)
        return os.getpgid(pid)
    except Exception:                                    # noqa: BLE001
        return None


def rung_complete(d):
    p = os.path.join(OUT, f"births_d{d}.json")
    if not os.path.exists(p):
        return False
    st = json.load(open(p, encoding="utf-8"))
    return bool(st.get("complete")) and st.get("p2_rank") == BIRTH[d]


def det_status(p=P1):
    path = os.path.join(OUT, f"decision_{p}.json")
    if not os.path.exists(path):
        return None
    return json.load(open(path, encoding="utf-8"))["columns"].get("det")


def det_pass(evaluated, pg):
    """pause the streams, evaluate the det column on the rows now in the source, resume."""
    if pg is not None:
        os.killpg(pg, signal.SIGSTOP)
        log(f"streams paused (pgid {pg})")
    try:
        run("build", 600, ["python3", "analysis/wk12_s74_columns.py", "--build"])
        run("det_P1", 14400, ["python3", "analysis/wk12_s74_columns.py", "--family", "det",
                              "--prime", str(P1), "--workers", "2"])
        run("decide_det", 1200, ["python3", "analysis/wk12_s74_decide.py", "--prime", str(P1),
                                 "--families", "det"])
        c = det_status()
        if c:
            log(f"det column at P1: rows {c['rows']}, rank_24 {c['rank_24']}; rows<=23 {c['rows_23']}, "
                f"rank_23 {c['rank_23']}  ->  rank T_det(24) >= {c['rank_23']} (running lower bound)")
        bank(f"s74: determinant column at P1 on {c['rows'] if c else '?'} source rows "
             f"(rungs {sorted(evaluated)}), running lower bound rank T_det >= {c['rank_23'] if c else '?'}.")
    finally:
        if pg is not None:
            os.killpg(pg, signal.SIGCONT)
            log("streams resumed")


def main():
    st = json.load(open(STATE)) if os.path.exists(STATE) else dict(evaluated_rungs=[], det_done=False)
    evaluated = set(st["evaluated_rungs"])
    # the rows that need no stream: seeds, 20..24 -- evaluate them first
    first = not evaluated
    while True:
        pg = births_pgid()
        done = {d for d in BIRTH if rung_complete(d)}
        new = done - evaluated
        if first or new or pg is None:
            evaluated |= new
            first = False
            det_pass(evaluated, pg)
            st["evaluated_rungs"] = sorted(evaluated)
            c = det_status()
            if c and c.get("rank_23") == 273:
                st["det_done"] = True
                log("DETERMINANT SIDE FINISHED: rank T_det = 273 on the transported delta=23 source "
                    "(i_det(23) = 0, hence i_det(24) = 1 with LMR)")
            json.dump(st, open(STATE, "w"), indent=1)
        if pg is None:
            break
        time.sleep(60)
    log("streams ended; final source build and the padded column")
    run("build", 600, ["python3", "analysis/wk12_s74_columns.py", "--build"])
    run("rowcheck", 3600, ["python3", "analysis/wk12_s74_columns.py", "--check-rows", "--workers", "2"])
    run("det_P1", 14400, ["python3", "analysis/wk12_s74_columns.py", "--family", "det", "--prime", str(P1), "--workers", "2"])
    run("pad_P1", 14400, ["python3", "analysis/wk12_s74_columns.py", "--family", "pad", "--prime", str(P1), "--workers", "2"])
    run("decide2", 1200, ["python3", "analysis/wk12_s74_decide.py", "--prime", str(P1), "--families", "det,pad"])
    bank("s74: padded-permanent column at P1 banked; decision at P1 read.")
    run("pad_P2", 14400, ["python3", "analysis/wk12_s74_columns.py", "--family", "pad", "--prime", str(P2), "--workers", "2"])
    run("det_P2", 14400, ["python3", "analysis/wk12_s74_columns.py", "--family", "det", "--prime", str(P2), "--workers", "2"])
    run("decide4", 1200, ["python3", "analysis/wk12_s74_decide.py", "--prime", str(P2), "--families", "det,pad"])
    bank("s74: determinant and padded columns at P2 banked.")
    run("rest_P1", 28800, ["python3", "analysis/wk12_s74_columns.py", "--family", "gen,red,per4", "--prime", str(P1), "--workers", "2"])
    run("decide3", 1200, ["python3", "analysis/wk12_s74_decide.py", "--prime", str(P1), "--families", "gen,det,pad,red,per4"])
    bank("s74: generic, reducible and per_4 columns at P1 banked.")
    run("rest_P2", 28800, ["python3", "analysis/wk12_s74_columns.py", "--family", "gen,red,per4", "--prime", str(P2), "--workers", "2"])
    run("decide5", 1200, ["python3", "analysis/wk12_s74_decide.py", "--prime", str(P2), "--families", "gen,det,pad,red,per4"])
    bank("s74: all five columns at both primes banked.")
    log("driver done")


if __name__ == "__main__":
    sys.exit(main())
