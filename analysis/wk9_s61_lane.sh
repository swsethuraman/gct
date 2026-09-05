#!/bin/bash
# Session 61: run a lane of polar-profile jobs sequentially (two lanes = two cores).
#   usage: wk9_s61_lane.sh <lane-name> <job>... where each job is "form:prime:seed:radical[:ks][:engine][:sat]"
# The lane's own pid goes to results/logs/s61_lane_<name>.pid; each job records its own
# engine pid through the driver.  Ended only by recorded pid.
set -u
LANE="$1"; shift
cd "$(dirname "$0")/.." || exit 1
echo $$ > "results/logs/s61_lane_$LANE.pid"
for job in "$@"; do
  IFS=: read -r form prime seed radical ks engine sat <<< "$job"
  args=(--form "$form" --prime "$prime" --seed "$seed" --radical "$radical" --timeout 14000 --mem-kb 6000000)
  [ -n "${ks:-}" ] && args+=(--ks "$ks")
  [ -n "${engine:-}" ] && args+=(--engine "$engine")
  [ -n "${sat:-}" ] && args+=(--sat "$sat")
  echo "$(date -u +%FT%TZ) lane $LANE start $job" >> "results/logs/s61_lane_$LANE.log"
  python3 analysis/wk9_s61_polar.py "${args[@]}" >> "results/logs/s61_lane_$LANE.log" 2>&1
  echo "$(date -u +%FT%TZ) lane $LANE done  $job" >> "results/logs/s61_lane_$LANE.log"
done
echo "$(date -u +%FT%TZ) lane $LANE finished" >> "results/logs/s61_lane_$LANE.log"
