#!/bin/bash
# B28-01b -- Cell A measurement, the frozen command after R28-01's repairs (B28-01c).
# NOT run by B28-01c.  Runs only after R28-01b says YES and the user's go.
#   bash ~/b28_01/frozen_c/b28_01c_cellA.sh                  the measurement
#   bash ~/b28_01/frozen_c/b28_01c_cellA.sh --preflight-only  every launch check, then exit (builds nothing)
# Cell (12,8,6,4,2), degree 8, a = 109, n_chi = N_S = 813,314; determinant family only;
# primes 2147483647 then 2147483629 (sequential); then one independent verifier replay at
# 2147483647.  Caps (P5): ONE 86,400 s aggregate monotonic limit and ONE 24,000,000,000-byte
# (decimal) memory scope with no swap over producer plus replay, whole-job termination and a
# resource-stop receipt (b28_01c_supervise.py); 64 GB free-disk reservation; 50 GB artifact stop.
# This file's own bytes are bound externally (results/b28_01c/frozen_c_hashes.txt).
set -u
F=$HOME/b28_01/frozen_c; ENG=$HOME/b28_01/engine; PY=$HOME/b28venv/bin/python
OUTROOT=$HOME/b28_01/out; O=$OUTROOT/cellA; JOB=$HOME/b28_01/job_cellA
CAP_S=86400; CAP_B=24000000000; DISK_RESERVE=64000000000; ARTIFACT_STOP=50000000000
P1=2147483647; P2=2147483629
SCHUR_SO_SHA=d6024a63dca11dc5b820864bc87ac842dcfba3a39e1f35792d6febacc8ee936d
LIBS="3.12.3 2.5.3 1.18.1 0.9.0"
MODE=${1:-run}
fail(){ echo "PREFLIGHT FAILED: $*"; exit 2; }

# ---- preflight 1: input bindings (frozen code, rates, compiled helpers, engine, libraries)
cd "$F" || fail "no $F"
sha256sum -c --quiet <<'EOF' || fail "frozen code hash mismatch"
f6fe04e239d28fa4ff89e8a103b4dd2b9b9f93ae146cbd3f64e0ec86ce49e23e  b28_01c_driver.py
73dbb5ac318cda4328659f95f6e26f6081241ee4ee029033498961f35dca4400  b28_01c_model.py
fcac55b4eca11330048ed3f6a1401d6dfdbbe8a1a185ae36991e618f6a5e2532  b28_01c_verify.py
5166db3b1ff07d23d3a4c51d9430de1a9808dff9d1e5d4d92b802a98904995f7  b28_01c_vfy.c
a5e8399d1e78e285a5864098dbe43d68f618c331a03705bbcb9df4e4dfd60fe6  b28_01c_vfy.so
772979a1e2c72c9f854c12d4ca3e0a708047ddfbdff10ca93fbd4603312a9b4e  b28_01c_supervise.py
665e9da1dd997b4318976c0a617d52f09f924f53e0fe2c451a7b0afce4787d1b  gate_rates_c.json
EOF
cd "$ENG" || fail "no $ENG"
sha256sum -c --quiet <<'EOF' || fail "engine hash mismatch"
73490ef336e6e875daa7877b10b86f873622f0930b648150e6b29c32144e6323  wk10_s64_pad.py
2e46e351e4b9f512be36b20f0b05ee83e26b29a3fd953d4d580cc1ab6bed4bd0  wk11_s71_codes.py
26a69eaa177ccd276f87af364aa624baae083c2573969da796458e956ce26073  wk11_s71_hybrid.py
0e29bd408efe78ab7bf3f3c55cfff7aa83f1aefb4f9f53634ea1d5c1a2a158b1  wk12_s79_cell6.py
4cca6f67127d7435fe24c6413d1f39c139184905fbcc25bcfd9323cdb058f304  wk8_s30_core.py
55ae352881aa9447a9b29e89300105530764ca251c8e571602bc55186f547f41  wk8_s30_pleth.py
398385b6b6fb11f42b522577cac63bba2094e32310347a988f36f265a98be6db  wk9_s36_stabred.py
2aab179653a5e6f64bf00b7e4902a16d29ff5bafd14e2c804ede3543303e7210  wk9_s42_census.py
010972eea7c0c4d75d8657bbd7a2af92876f4540096519528076c5954e64bb28  wk9_s42_hpad.py
75045b5dc4be6b7188db13407f2ef4abc81ac66b4b31300740cb8f4a0dad6f01  wk9_s42_orbits.py
17491fd0e19802d09293190aaba2b5c79e4cb8e7c297f30f44cddfce75f5a5e6  wk9_s42_sparse.py
7a6b2e280d2e214430ad35f5f0edc596d04a856561b5a70a4413674a4f3ad1d3  wk9_s45_build.py
555680c323b67c1acefeb62195b74bb6c81dc79e3f1b5999ca60b3f9fc18f9f6  wk9_s45_cell.py
14a7108a5847eb13573c58dd4f34595e4b82e894a84d40a36d3e03509c0400bd  wk9_s60_cell.py
17cfdf423511b863cbd5f242c91776cc0b85bbfb4aeb9f2625450a0f5a2c695c  wk11_s71_schur.c
d6024a63dca11dc5b820864bc87ac842dcfba3a39e1f35792d6febacc8ee936d  schur.so
EOF
[ "$("$PY" -c 'import sys,numpy,scipy,flint;print(sys.version.split()[0],numpy.__version__,scipy.__version__,flint.__version__)')" = "$LIBS" ] \
  || fail "python/numpy/scipy/python-flint versions differ from $LIBS"

# ---- preflight 2: no recompile after the hash check (the engine's lib() rebuilds when schur.so is older than its source)
"$PY" -c 'import os,sys; sys.exit(0 if os.stat(sys.argv[1]).st_mtime_ns >= os.stat(sys.argv[2]).st_mtime_ns else 1)' \
  "$ENG/schur.so" "$ENG/wk11_s71_schur.c" || fail "schur.so is older than wk11_s71_schur.c; the engine would recompile"

# ---- preflight 3: no prior target output or job (target directories, and any Cell A file anywhere under ~/b28_01)
for x in "$O" "$JOB" "$OUTROOT"/cellA*/; do [ -e "$x" ] && fail "$x exists (prior target output or job)"; done
PRIOR=$(find "$HOME/b28_01" -name '12_8_6_4_2_d8_*' -print -quit)
[ -n "$PRIOR" ] && fail "$PRIOR exists (prior Cell A measurement file)"

# ---- preflight 4: free memory and disk
AVAIL=$(( $(awk '/^MemAvailable:/{print $2}' /proc/meminfo) * 1024 ))
[ "$AVAIL" -ge "$CAP_B" ] || fail "MemAvailable $AVAIL < job cap $CAP_B"
DISK=$(df -B1 --output=avail "$HOME" | tail -1 | tr -d ' ')
[ "$DISK" -ge "$DISK_RESERVE" ] || fail "free disk $DISK < reservation $DISK_RESERVE"
echo "PREFLIGHT OK: bindings, no-recompile, no prior output, MemAvailable=$AVAIL, free disk=$DISK"
[ "$MODE" = "--preflight-only" ] && exit 0
[ "$MODE" = "run" ] || fail "unknown argument $MODE"

# ---- the job: producer (build, cover, gate, both primes, prime comparison) then the replay, one scope, one monotonic cap
mkdir -p "$O" "$JOB"
export B28_ENGINE=$ENG B28_VFY_SO=$F/b28_01c_vfy.so S71_SCHUR_SO=$ENG/schur.so B28_SCHUR_SO_SHA256=$SCHUR_SO_SHA
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
STEPS=$(cat <<EOF
[{"label": "cellA_driver", "argv": ["$PY", "$F/b28_01c_driver.py", "--lam", "12", "8", "6", "4", "2", "--delta", "8", "--a", "109",
   "--nchi", "813314", "--primes", "$P1", "$P2", "--out", "$O", "--wall-budget", "{REMAINING}", "--mem-cap", "$CAP_B",
   "--rates", "$F/gate_rates_c.json"]},
 {"label": "cellA_verify", "argv": ["$PY", "$F/b28_01c_verify.py", "--lam", "12", "8", "6", "4", "2", "--delta", "8", "--a", "109",
   "--prime", "$P1", "--dir", "$O", "--out", "$O/12_8_6_4_2_d8_p${P1}_verify.json"]}]
EOF
)
systemd-run --user --scope --quiet -p MemoryMax=$CAP_B -p MemorySwapMax=0 -p RuntimeMaxSec=$((CAP_S + 600)) \
  "$PY" "$F/b28_01c_supervise.py" --cap-secs $CAP_S --out "$O" --artifact-stop $ARTIFACT_STOP \
  --receipt "$JOB/job_receipt.json" --steps "$STEPS"
RC=$?
sha256sum "$ENG/schur.so" "$F/b28_01c_vfy.so" > "$JOB/post_run_binaries.sha256"
case $RC in
  0) echo "FULL_RANK at $P1 (both primes agree; independent replay FULL_RANK)";;
  8) echo "MODULAR_DEFICIENCY (lower bound only; candidates unproved; both primes agree; replay accepted)";;
  3) echo "stopped at the build-and-cover gate (sizing receipt in $O)";;
  4) echo "source gate or check failed (inconclusive); stopped before the next prime";;
  6) echo "INCONCLUSIVE CONTROL FAILURE: the primes disagree; no replay";;
  5) echo "independent replay REJECTED the certificate";;
  124) echo "RESOURCE STOP: aggregate 86,400 s monotonic limit (receipt $JOB/job_receipt.json)";;
  125) echo "RESOURCE STOP: artifact size above 50 GB (receipt $JOB/job_receipt.json)";;
  137) echo "RESOURCE STOP: memory (scope OOM kill; receipt $JOB/job_receipt.json)";;
  *) echo "exit $RC (see $JOB/job_receipt.json)";;
esac
exit $RC
