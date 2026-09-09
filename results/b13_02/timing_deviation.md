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

Second observation, 2026-09-09T21:10Z: pilot column 02 recorded 10891.34 seconds
inside its arithmetic driver. The absolute child guard marked the in-progress
coefficient `absolute_wall_deadline`, retained 31 completed entries and one null,
and stopped the column. The parent marked `completed_after_wall_deadline`.
The short follow-on columns 03 and 04 in the already-running sequential shell
then completed. This exposed a return-code defect: the parent reported exit
zero when the child returned zero after detecting its deadline. That defect is
now corrected, so any non-`completed` status returns nonzero to the shell.

No further coefficient pilot is launched. The exact 31 completed coefficients
in column 02 are retained; neither the missing coefficient nor the unattempted
rows are zeros. The two large wall gaps mean the preregistered elapsed pilot
budget was exceeded, irrespective of their unverified cause. The partial-result
fallback is used. Its mathematical coefficients and dimension counts do not
depend on timing; its performance extrapolations exclude no elapsed time from
the recorded totals and separately report later runs' recorded CPU times.
