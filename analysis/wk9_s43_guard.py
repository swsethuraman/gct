#!/usr/bin/env python3
"""
Session 43 -- the shared memory guard used by both concurrent phases.

The container is ~7 GB with 2 cores.  Phase A (n = 4 cells) and Phase B
(n = 3 permanent weights) run at the same time, so they must not both hold a
large flint matrix.  Two devices, both pre-registered in results/PREREG_s43.md
section 0:

  * a WAIT on MemAvailable: a run starts only when its predicted peak fits
    inside `headroom` of what is free.  The guard waits; it never skips.
  * a HEAVY LOCK: any run predicted above HEAVY_GB takes an exclusive lock
    file first, so above that size the container is a one-cell machine
    (docs/sixrow_frontier.md, engineering notes).

Stale locks are released by reading the recorded process id out of the lock
file and testing whether that process still exists -- never by name matching.
"""
import os, time, errno

WORK = os.environ.get('S43_WORK', '/root/s43')
HEAVY = os.path.join(WORK, 'heavy.lock')
HEAVY_GB = 1.5
MEM_PEAK_INPL = 1.4e-8
MEM_INPL_BASE = 0.4


def predicted_gb(n_chi):
    if n_chi <= 800:
        return 0.5
    return MEM_PEAK_INPL * n_chi ** 2 + MEM_INPL_BASE


def free_gb():
    for ln in open('/proc/meminfo'):
        if ln.startswith('MemAvailable:'):
            return int(ln.split()[1]) / 1048576.0
    return 0.0


def _alive(pid):
    try:
        os.kill(pid, 0)
    except OSError as e:
        return e.errno != errno.ESRCH
    return True


def _reconcile():
    """release the heavy lock if the process that recorded it is gone"""
    try:
        txt = open(HEAVY).read().split()
    except FileNotFoundError:
        return
    try:
        pid = int(txt[0])
    except (IndexError, ValueError):
        os.unlink(HEAVY)
        return
    if not _alive(pid):
        os.unlink(HEAVY)


class heavy_lock:
    """context manager; a no-op when the run is small"""

    def __init__(self, gb, tag, log=print, poll=20):
        self.need = gb > HEAVY_GB
        self.tag, self.log, self.poll = tag, log, poll
        self.held = False

    def __enter__(self):
        if not self.need:
            return self
        os.makedirs(WORK, exist_ok=True)
        said = False
        while True:
            _reconcile()
            try:
                fd = os.open(HEAVY, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                os.write(fd, ("%d %s\n" % (os.getpid(), self.tag)).encode())
                os.close(fd)
                self.held = True
                return self
            except FileExistsError:
                if not said:
                    self.log(f"   [guard] {self.tag} waiting for the heavy lock")
                    said = True
                time.sleep(self.poll)

    def __exit__(self, *exc):
        if self.held and os.path.exists(HEAVY):
            try:
                if int(open(HEAVY).read().split()[0]) == os.getpid():
                    os.unlink(HEAVY)
            except Exception:
                pass
        return False


RESERVE_GB = 1.2            # left free for the other worker and the container


def wait_for_memory(gb, tag, headroom=0.85, log=print, poll=30):
    """wait until the run's predicted peak fits with RESERVE_GB still free"""
    said = False
    while gb > headroom * free_gb() or gb + RESERVE_GB > free_gb():
        if not said:
            log(f"   [guard] {tag} needs ~{gb:.1f} GB, {free_gb():.1f} GB free -- waiting")
            said = True
        time.sleep(poll)
