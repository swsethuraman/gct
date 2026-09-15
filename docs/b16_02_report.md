# B16-02 delivery: four finite cells excluded

All four requested quartic ambient multiplicities were computed exactly.
The fresh finite-character proof shows that these cells already equal
their stable ambient spaces; stable dimensions were not merely substituted
for unknown finite counts.

| degree | highest weight | exact ambient a | accepted padding ceiling | full determinant ideal upper | proved D upper |
|---:|---|---:|---:|---:|---:|
| 23 | (61,15,2^8) | 189 | 158 | 11 | -20 |
| 25 | (67,17,2^8) | 294 | 218 | 11 | -65 |
| 26 | (71,17,2^8) | 294 | 218 | 11 | -65 |
| 27 | (73,19,2^8) | 429 | 288 | 11 | -130 |

The exclusion uses `D=i_det-i_pad<=11-(a-h)`, where `h` is a padding
coordinate upper bound. It does not infer an exclusion from failure of
`q+r>a`. The padding source sizes are never called image ranks.

The new sufficient finite-stability criterion is `2d-|tau|+2>tau_1`.
A direct first-row Weyl extraction expresses each possible finite
correction as a hook Schur function multiplied by a Schur-positive
character. Its first row is at least `2d-|tau|+2`, so it cannot fit `tau`.
The complete proof and threshold arithmetic are in
[b16_02_proof.md](b16_02_proof.md).

Equality of the entire finite/stable ambient spaces also transfers the
accepted stable geometry to degree27: `i_det=11`, `m_det=418`,
`243<=m_pad<=288`, and `-175<=D<=-130`. It transfers the known four
independent stable tail-17 equations to degrees25 and26. These are new
dimension/filtration deductions, not freshly evaluated geometric minors
or explicit coefficient expansions of eleven polynomial lifts.

The supplied ideal floors1,2,2,5 would require padding ranks189,293,293,425
for positivity. Even the maximum possible ideal dimension11 would require
179,284,284,419, exceeding the corresponding source ceilings. None of
these cells admits a positive witness consistent with the accepted premises.
Earlier rungs outside the proved onsets23/25/27 remain outside this census;
a different surviving cell needs its own finite count, global determinant
ideal floor q and actual ten-variable padding rank floor r with `q+r>a`.

## Evidence and boundaries

Fresh: finite-stability proof; exact Fraction character recurrence and
all signed character-sum rows; 94 direct small finite-plethysm/branching
controls; 36 truncated-hook controls; an independently implemented receiver
using python-flint rationals and connected skew border strips; four-cell
arithmetic; rejection of five altered certificate types.

Inherited: S57's chart/ideal filtration; B15-06's accepted determinant
rank418, same-row multiplication injection and geometric proof boundaries;
Hessian11's global independent equation spaces; Dream_Upper288's accepted
split-cubic source bound and genuine independent-padding rank243. Their
proofs and original attribution were read via the frozen intake. No old
geometric computation was repeated. Characteristic zero, the positive
coordinate representation convention and sixteen ambient variables are
maintained. Padding retains ten independent source variables.

The producer reuses the attributed B14-04/B15-06 rational recurrence and
the preserved S30 beta-number Murnaghan-Nakayama routine. The receiver
imports neither producer nor inherited counting code; it regenerates
the recurrence with fmpq and computes characters by geometric rim-strip
enumeration. It is a different implementation, not a different symmetric
function formula. The receiver checked20 actual input hashes and complete
coefficient/character support. `results/b16_02/input_hashes.json` records
raw-byte SHA256 hashes, including the frozen brief, intake, original proof
sources, inspected code and Python executable.

## Bounded resources and replay

Every run used this worktree's `.venv/python.exe -B` and the inspected
`analysis/b15_bound.py`, one computation process and one numerical thread,
with enforced Windows Job Object memory caps and a deadline guard.
No dense quartic weight carrier or degree108 power-sum expansion was built.

| run | wall seconds | peak job bytes | exit |
|---|---:|---:|---:|
| sparse sizing | 0.04661 | 34263040 | 0 |
| finite/hook controls | 0.09117 | 14761984 | 0 |
| count pilot | 1.56449 | 45740032 | 0 |
| separate receiver | 0.63344 | 54247424 | 0 |

All four caps were60seconds/512MiB. The maximum measured working set was
66,375,680 bytes. The sparse preflight counted at most81,156 stored
partition coefficients and714,919 recurrence multiply-add operations.
No heavy process was needed. Initial lease02 was explicitly released to
the integrator after count PID38012 exited; every owned computation PID
was checked absent after completion. No extension was requested.
The unchanged legacy wrapper labels receipts `batch15/B15-02`; the names
`b16_02_*`, artifact manifest and this report identify the current batch.

From `C:\Users\swami\Projects\gct-gpt\work\batch15_workers\B15-02`:

```powershell
& .venv/python.exe -B analysis/b15_bound.py --slot 02 --name b16_02_receiver_fresh --seconds 60 --memory-mb 512 analysis/b16_02_receive.py
```

Full production replay, using fresh receipt names, runs
`analysis/b16_02_census.py sizing`, then `controls`, then `census`, each
through the same wrapper/caps, followed by the receiver above. All writes
remain in the owned B16 prefixes. `delivery/b16_02/MANIFEST.json` binds the
delivered sources, proofs, certificates and measured receipts. This is a
filesystem delivery; the frozen worktree HEAD remains
`77a16d78dcc9adf8067c562efc4c7fe9a858bfa0`. No B15 or shared theorem files
were edited or staged, and no Git commit, push or publication was made.
