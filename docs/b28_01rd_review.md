# R28-01d — cross-lineage review of Cell A

**COMPUTED — ACCEPT: no determinant equation in Cell A.** The single independent
replay returns `FULL_RANK`, and its complete mathematical output is byte-identical
to B28-01b's committed replay. Achievement: a certified negative in one cell,
not PROVED and not a coefficient equation. None of the four achievements moves.

## D1 — Bindings: ACCEPT

**COMPUTED:** Reviewer branch `b28-01r` began at `ff62d929e53edf5abcf772c4b44cd0ff4c302b49`.
Producer tip is `467e8402478bca64923c0a1a852bd0efee331356`, parent `0f7af8b11e55da20cd135c73d04554a0360dd97f`.
Its 26 changed paths comprise only its 25 manifest payloads (including the
report) and its manifest. The manifest hash is
`9beba33cce900aed46940d25eacf535820c379385c2a3225d9f944541a45f314`.
All 25 payload sizes and raw hashes match the committed blobs; all four
host-retained files match their committed sizes/hashes. All nine `frozen_d` files
match `0f7af8b11e55da20cd135c73d04554a0360dd97f:results/b28_01d/frozen_d_hashes.txt`, before and after the run.
The host-retained files are unchanged afterward. `BINDINGS.json` records every
path, byte count and full SHA-256, including the raw common, brief and board hashes.
The output paths were absent at initial preflight; untracked files were left alone.

**READ:** Governing mathematical text is
`96a8074d:results/b27_06/PREREGISTRATION.md`, specifically the source gate,
independent replay and full-rank lifting rules. The exact verifier and supervisor
read are `0f7af8b11e55da20cd135c73d04554a0360dd97f:analysis/b28_01c_verify.py` and
`0f7af8b11e55da20cd135c73d04554a0360dd97f:analysis/b28_01d_supervise.py`; their blob hashes are in `BINDINGS.json`.
The verifier reconstructs E, cover, G and evaluations without importing producer
code. It shares only the declared low-level NumPy/SciPy/python-flint libraries.

## D2 — Host condition: ACCEPT after user correction

**COMPUTED:** The initial read-only Windows query reported AC sleep index `0x00000384`.
Work stopped, and the user subsequently reported changing the setting and authorized
resumption. **COMPUTED:** Both the immediate pre-run and post-run queries report
AC index `0x00000000` (Never). The reviewer did not change power settings.
The Windows System-log query covering the actual launch interval found no sleep
or resume events; raw observations and query bounds are receipt-only payloads.

## D3 — Frozen verifier replay: ACCEPT

**COMPUTED:** Exactly one verifier invocation, at prime 2,147,483,647, used the
unchanged `~/b28_01/frozen_d/b28_01c_verify.py` and its bound `.so`. Committed
certificate, cell and pencil bytes were exported to the review's inputs directory;
the bound original kernel was read through `--kernel`. No producer, other cell,
additional prime, control, calibration or retry was run.

**COMPUTED:** The single scope enforced `MemoryMax=24000000000`,
`MemorySwapMax=0`, `RuntimeMaxSec=3600`; the unchanged frozen supervisor had a
3540-second deadline, leaving shutdown margin within the outer cap. Live cgroup
limits were asserted before starting the verifier. Exit was 0, with no resource
stop or surviving job process. All phase timings, resource measurements and
nondeterministic logs are in receipt payloads, separate from mathematical output.

**COMPUTED:** The complete regenerated verifier JSON has raw SHA-256
`b4608a92a54708efca22e8cfffe9d1e7377550c1064b36ea9bef0075f0566276` (1793 bytes), identical byte
for byte to `467e8402478bca64923c0a1a852bd0efee331356:results/b28_01b/out_cellA/12_8_6_4_2_d8_p2147483647_verify.json`.
`COMPARISON.json` records the comparison and every check:

- **COMPUTED:** `E_matches_producer = true`.
- **COMPUTED:** `G1_cover_pivots = true`.
- **COMPUTED:** `G2_residual_rank = true`.
- **COMPUTED:** `G_matches_producer = true`.
- **COMPUTED:** `K1_EK_zero_all_rows = true`.
- **COMPUTED:** `K1b_rank_K = true`.
- **COMPUTED:** `K_file_matches_cert = true`.
- **COMPUTED:** `M1_claimed_minor_nonzero = true`.
- **COMPUTED:** `VK_matches_producer = true`.
- **COMPUTED:** `cover_matches_producer = true`.
- **COMPUTED:** `mult_det_matches_claim = true`.
- **COMPUTED:** `n_chi_matches_frozen = true`.
- **COMPUTED:** `outcome_label_matches = true`.
- **COMPUTED:** `pencils_match_generator = true`.
- **COMPUTED:** `point_count_registered = true`.
- **COMPUTED:** `projection_recipe_registered = true`.

**COMPUTED — regenerated matrix hashes:**

| matrix | SHA-256 | precise bytes named |
|---|---|---|
| E | `7f37eee63d6c73dca94f0f2268c601032fb7cb929043edf3c1c85033c78c1938` | CSR indptr, indices, data as contiguous little-endian int64, concatenated in that order, followed by UTF-8 JSON of shape |
| G | `e5eeb58185e7706552f303e0b36b41dac1b92f27eb8b89588500c7b8c5f8ad7e` | row-major little-endian uint32 residual entries |
| VK | `076c3c7d3cf249fc02e247583b26de0d7a25a70831987490c8b23a8a74151105` | row-major little-endian uint32 evaluation entries |

## D4 — Certificate reading: ACCEPT

**COMPUTED:** The regenerated source has n = 813,314 columns, 2,310,607 rows and
10,062,442 nonzeros. The verified upper-triangular cover has 809,656 nonzero
pivots; U has 3,658 columns and the regenerated projected residual has rank 3,549.
Thus the lower bound on source rank is 809,656 + 3,549 = 813,205 = n - 109.
The original full kernel K, shape 813,314 by 109, is checked on every row of the
regenerated E; E K = 0 and rank K[U,:] = 109. These give the matching upper bound,
so rank over the specified finite field is exactly n - a, with a = 109.

**COMPUTED:** Independently regenerated evaluation VK has shape 117 by 109 and
rank 109. The claimed minor uses zero-based rows 0 through 108 and all columns;
the verifier recomputes its determinant as 763,718,730 modulo 2,147,483,647,
which is nonzero. This conclusion uses the fresh values, not stored rank claims.

**READ:** The preregistration fixes rational source multiplicity a = 109 and
requires these exact source and evaluation certificates for its lifting argument.
**HAND:** The nonzero source minor and the fixed rational source dimension make
the source kernel specialize without a dimension jump at this prime. Alternatively,
the verified source kernel and injective VK imply that the stacked integer matrix
[E; V] has trivial modular kernel and therefore full column rank over Q. Hence
evaluation is injective on the 109-dimensional rational source; determinant
multiplicity is 109 over Q. **COMPUTED:** Under the preregistered certificate rule,
this records no determinant equation in this cell; it is a certified negative.

## D5 — Sleep assessment: ACCEPT

**READ:** B28-01b's committed `host_power_events.txt`, supervisor receipt and GNU
time receipt place the suspension inside its verifier step. Its producer and
verifier both exited normally; the receipt records no resource stop, OOM, forced
termination, leftover process, or extra verifier step. The supervisor contains
no restart/retry path. Exact original timing observations remain in those committed
receipts, whose bytes are bound by the validated producer manifest.

**HAND:** Suspension affected elapsed-time accounting and violated the declared
host condition; the monotonic timer excluded suspended time. The evidence shows
no truncation, restart, or resource-stop path. All payload and retained-file hashes
are intact, and the clean replay reproduces the complete mathematical output.
There is no remaining evidence that suspension affected the certificate or verdict.
This does not erase the historical host-condition deviation.

## Outcome boundary

**COMPUTED:** D1–D5 ACCEPT; registered outcome **ACCEPT** for
"COMPUTED: no determinant equation in Cell A", lambda = (12,8,6,4,2), k = 8.
**HAND:** This is a certified negative in one cell. It supplies no coefficient
equation, padding separation, or positive multiplicity gap and moves none of
the four achievements (source condition, coefficient equation, separation on
padding, positive multiplicity gap). No geometric noncontainment or asymptotic
bound is claimed.

**READ — binding constraint:** "No five-row determinant equation is known to be nonzero on padding."

**READ — programme decision:** "no construction ready."
