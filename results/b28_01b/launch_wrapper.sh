#!/bin/bash
# B28-01b: the single Cell A run. stdout/stderr captured to ~/b28_01/b28_01b_launch_stdout.txt
L=$HOME/b28_01/b28_01b_launch_stdout.txt
echo "LAUNCH_UTC=$(date -u +%FT%TZ)" > "$L.meta"
bash ~/b28_01/frozen_d/b28_01d_cellA.sh 2>&1 | tee "$L"
RC=${PIPESTATUS[0]}
echo "END_UTC=$(date -u +%FT%TZ)" >> "$L.meta"
echo "LAUNCHER_EXIT=$RC" >> "$L.meta"
echo "LAUNCHER_EXIT=$RC"
