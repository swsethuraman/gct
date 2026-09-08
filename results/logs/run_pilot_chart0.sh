#!/bin/bash
set -u
cd /home/claude/gct/results/astra/S2/cas
ulimit -v 6200000    # ~6.2 GB virtual memory cap
exec Singular -q --no-warn chart_0_Q.sing
