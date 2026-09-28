#!/bin/bash
# B28-01b -- Cell A measurement, the frozen command.  NOT run by B28-01a.
# Runs only after R28-01 ACCEPT and the user's go.  Cell (12,8,6,4,2), degree 8,
# a = 109, n_chi = N_S = 813,314; determinant family only; primes 2147483647
# then 2147483629 (sequential); then one independent verifier replay at
# 2147483647.  Caps: 24 h wall in total, 24,000,000,000 bytes per process
# (one numerical process at a time), no swap.
set -u
F=$HOME/b28_01/frozen; ENG=$HOME/b28_01/engine; PY=$HOME/b28venv/bin/python
O=$HOME/b28_01/out/cellA; CAP_S=86400; CAP_B=24000000000
P1=2147483647; P2=2147483629

# ---- preflight: frozen hashes (driver, verifier, helpers, engine, host rates); output folder absent
cd "$F" || exit 2
sha256sum -c --quiet <<'EOF' || { echo "PREFLIGHT: frozen code hash mismatch"; exit 2; }
de202bb09855301e911123e1e39dd4e85b493d1fc8b6d1bcae7d9986bd71094c  b28_01_driver.py
7978a73aaf30ee0dee4fa37a6bdf088a52daf85b00390af62d532b2027e7def5  b28_01_verify.py
5166db3b1ff07d23d3a4c51d9430de1a9808dff9d1e5d4d92b802a98904995f7  b28_01_vfy.c
a5e8399d1e78e285a5864098dbe43d68f618c331a03705bbcb9df4e4dfd60fe6  b28_01_vfy.so
ce29445db75ab368f94b156d96d9f38fabc5890ff8ae45be630b4d8840ebfe64  b28_01_run.sh
6bbc5aedfe5ac42a58f86d1511d9689f786db2d06c7d4ae7dabb0a53a7c55019  gate_rates.json
EOF
cd "$ENG" || exit 2
sha256sum -c --quiet <<'EOF' || { echo "PREFLIGHT: engine hash mismatch"; exit 2; }
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
[ -e "$O" ] && { echo "PREFLIGHT: $O exists"; exit 2; }
mkdir -p "$O"
export B28_ENGINE=$ENG B28_VFY_SO=$F/b28_01_vfy.so S71_SCHUR_SO=$ENG/schur.so

# ---- producer: build, cover, gate (75% memory rule, remaining-time rule), then both primes
T0=$(date +%s)
"$F/b28_01_run.sh" cellA_driver "$CAP_B" "$CAP_S" "$PY" "$F/b28_01_driver.py" \
  --lam 12 8 6 4 2 --delta 8 --a 109 --nchi 813314 --primes $P1 $P2 --out "$O" \
  --wall-budget $CAP_S --mem-cap $CAP_B --rates "$F/gate_rates.json"
RC=$?
[ $RC -ne 0 ] && { echo "producer exit $RC (3 = gate stop, 4 = source gate failed, 124 = wall cap); no verifier run"; exit $RC; }

# ---- independent replay at the first prime, within the remaining wall budget
LEFT=$(( CAP_S - ( $(date +%s) - T0 ) ))
[ $LEFT -le 0 ] && { echo "wall budget exhausted before the verifier"; exit 124; }
"$F/b28_01_run.sh" cellA_verify "$CAP_B" "$LEFT" "$PY" "$F/b28_01_verify.py" \
  --lam 12 8 6 4 2 --delta 8 --a 109 --prime $P1 --dir "$O" --out "$O/12_8_6_4_2_d8_p${P1}_verify.json"
exit $?
