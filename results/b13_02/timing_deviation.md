board_numbering: batch13
session_id: B13-02

Recorded 2026-09-09T18:07Z. The fresh dimension run completed its exact arithmetic
and independently matched all 48 inherited multiplicities (sum 521), but recorded
11001.92 seconds from launch to return against a requested 600-second bound.
Block 16 alone reports 10896.79 seconds. The Windows subprocess wait did not
enforce the intended elapsed wall-clock bound. No CPU timing was retained for
that run, and the cause of the gap is unverified; no elapsed time is subtracted
from the log and no claim of budget compliance is made.

Before further launches, the parent was changed to poll the recorded child PID
against an absolute wall-clock deadline once per second, and the child now checks
the same deadline within coefficient extraction and before every numerical DP
addition. Child CPU time is recorded on all subsequent launches. The existing
Windows Job Object 768 MiB process memory bound remains in place. There has
been at most one numerical worker, with all BLAS thread environment settings 1.
