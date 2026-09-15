# B16-10 delivery: finite stop and reusable padding coefficients

All four assigned finite cells are excluded under the accepted bounds and
slot02's final finite census. In degrees23/25/26/27, respectively,
`D<=-20,-65,-65,-130`. The proof uses the full determinant ideal upper11
and padding source ceilings158/218/218/288. Failure of a sufficient gap
inequality is not used as an exclusion.

The integrator independently accepted slot02's census: its fresh receiver
passed in0.5511 seconds, with17 delivery hashes and20 input hashes checked.
The acceptance review is saved in a supplementary hashed input snapshot.

The bounded fresh control also supplies exact coefficient minors on
`L(u)=L0+u E_(X12,t)`, an invertible ten-variable substitution into genuine
independent `z*per3`. It certifies named-source restriction floors1,2,2,3
at those degrees. The degree25 minor is20304580134666240; the degree27
minor is1208423772021694132374994944. Degree27 already has the stronger
inherited padding floor243 after slot02's finite/stable identification.
The new rank3 certificate demonstrates the reusable method; it does not
improve that bound or prove a multiplicity obstruction.

`docs/b16_10_proof.md` retains the explicit curve, exact coefficient
matrices, source conventions, ring computation, finite transport
multipliers, and hypotheses. `results/b16_10/jet_certificate.json` retains
the intermediate polynomials, points, and minors. The two standalone
standard-library modules are `analysis/b16_10_jet.py` and
`analysis/b16_10_receive.py`. The receiver regenerates coefficients from
the six permanent monomials, checks the full ten-Hessian against the
factored computation, recomputes minors, rejects source/point/coefficient/
minor mutations, checks input snapshot hashes, and redoes exclusion
arithmetic. Slot02's count production is inherited and is not repeated.

All arithmetic is exact over Q, with order2 Hasse coefficients. The ten
source partials have disjoint supports, proving ten essential variables.
The largest polynomial support was57 and largest determinant layer220.
No dense carrier or heavy job was started. There was no heavy lease to
release; all slot10 research processes exited. The wrapper's legacy
`B15-10` label does not change that these are owned B16 runs.

| Run | Wrapper seconds | Peak working-set bytes | Peak Job Object bytes | Exit |
|---|---:|---:|---:|---:|
| Size preflight | 0.018347 | 21778432 | 13803520 | 0 |
| Coefficient producer | 0.182796 | 23314432 | 14524416 | 0 |
| Fresh jet receiver | 0.183529 | 23068672 | 14626816 | 0 |
| Input capture | 0.036633 | 22941696 | 13918208 | 0 |
| Full receiver and mutations | 0.549576 | 23318528 | 14917632 | 0 |

Every run used the worktree `.venv/python.exe -B` and inspected
`analysis/b15_bound.py`, one process, one configured numerical thread,
60-second deadline and512-MiB enforced Windows Job Object cap. The inherited
launch runtime smoke is recorded separately and is not fresh research.
Final packaging/portable-receiver receipts are in the resource summary.

The actual input manifest contains exact-byte and normalized-LF SHA256,
paths, byte counts, and local snapshots, including the frozen launch brief,
accepted Dream/Hessian evidence, inspected B15-10 sources, and slot02's
proof, census and receiver. Attribution stays with the original producers.
Fresh: padding arc coefficients/minors, receiver, direct finite polynomial
ideal-transport proof, and stop arithmetic. Inherited: source polynomiality
and highest weights, finite ambient counts, stable determinant floor418 in
ambient429, split-cubic padding ceilings, characteristic-zero representation
interpretation. No unified merged worktree base is asserted.

Replay from the reused B15-10 worktree, choosing a fresh receipt name:

```powershell
& .venv/python.exe -B analysis/b15_bound.py --slot 10 --name b16_10_replay_fresh --seconds 60 --memory-mb 512 analysis/b16_10_receive.py verify --receipt results/b16_10/replay_fresh.json
```

The same verified receiver is packaged under `delivery/b16_10/` with source,
snapshots, hashes and a portable replay command. Delivery is filesystem
evidence; no Git operation, commit, staging, bundle, push or publication was
performed. All B15 data, other workers' files and shared records are
preserved. No new task or subagent was created.

The next sufficient witness requires a different viable finite cell,
proved polynomial sources, and a coefficient minor r with q+r>a. The
current four cells admit no such witness under the recorded premises.
