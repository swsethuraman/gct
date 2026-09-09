#!/bin/bash
set -u
cd /home/claude/gct/results/astra/S2/cas
ulimit -v 6200000
exec Singular -q --no-warn reduced_dimS.sing
