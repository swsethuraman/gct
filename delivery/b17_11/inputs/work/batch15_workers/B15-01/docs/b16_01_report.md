# B16-01 delivery: exact finite cubic source bounds

**PASS. The finite source dimensions are 158, 218, 218 and 288.** These equal
the previous chart ceilings numerically and remain upper bounds for padding
image ranks. No assigned cell obtains a smaller ceiling from finite cubic
counting. Work used the supplied B15-01 worktree; no worktree, task, subagent,
Git operation, shared-file edit or B15 replay was performed.

| Degree and weight | Exact source | Padding upper |
|---|---|---|
| 23, (61,15,2^8) | 158 | 158 |
| 25, (67,17,2^8) | 218 | 218 |
| 26, (71,17,2^8) | 218 | 218 |
| 27, (73,19,2^8) | 288 | 288 |

The new finite proof is a branching/Weyl identity. For beta of size w and
first part b, a3_d(3d-w,beta) equals its depressed-cubic chart dimension when
d>=floor((w+b)/2), assuming the full weight is dominant. Potential finite
corrections are signed hook products; hook containment requires
2d<=w+b-2. For beta=(b,2^7), d>=b+7 therefore suffices, and every assigned
channel meets this threshold. This is a sufficient threshold, not an optimal
one. [Full proof](b16_01_proof.md) includes the finite formula and all map
directions.

Fresh arithmetic regenerated all 18 character sums, checked both outer-rim
and beta-number characters, enumerated all Pieri channels and correction
hooks, and compared against 235 small full cubic plethysms. It also checked
the alternative series formula through weight12 and character orthogonality
through S6. The receiver recomputes the complete certificate and rejects four
mutations, including presenting a source dimension as a padding rank.

The explicit multipliers u=c and v=8cB-3A^2, for the first binary quartic
coefficients c,A,B, have degree/weight (1,(4,0)) and (2,(6,2)). Exact shear
arithmetic verifies v's highest-weight covariance. Multiplication by
u^8v^2, u^8v, u^7v and u^8 respectively injects the four finite determinant
ideals into the accepted d35,(105,19,2^8) ideal. Its inherited dimension11
therefore gives i_det<=11 at each cell. With the source ceilings, finite
ambient counts at least **169,229,229,299** respectively would exclude a
positive gap. These are conditional thresholds, not ambient count claims.

The known ideal floors q=1,2,2,5 require actual padding floors
r=a,a-1,a-1,a-4. Given the source ceilings, those particular floors can prove
positivity only if a<=158,219,219,292. Failure of this last condition alone
does not exclude a gap using stronger ideal information.

Fresh versus inherited: the finite threshold, its application, arithmetic
and explicit transport proof are fresh. The product-map framing, accepted
stable a429/m_det418/padding floor243, and finite determinant equation floors
are inherited from the frozen inputs. The accepted B15-01 full replay was
read and preserved; its nine-row results were not rerun or relabeled as
ten-row evidence. Original S74/B14-07/Claude attribution is retained in the
proof. This task's two character implementations are not an external
independent review.

All calculations used the assigned .venv/python.exe with -B and the inspected
analysis/b15_bound.py. They ran sequentially in one process, with one configured
BLAS thread, no numerical child processes, a 60-second deadline and a 512 MiB
enforced Job Object cap. The wrapper's legacy B15 label is only metadata.

| Run | Wall seconds | Peak Job Object bytes | Exit |
|---|---:|---:|---:|
| preflight | 0.034734 | 26,935,296 | 0 |
| producer | 2.191542 | 59,330,560 | 0 |
| receiver | 2.554019 | 66,121,728 | 0 |
| transport | 0.031008 | 23,486,464 | 0 |

Total measured wall time was 4.811303 seconds; largest peak was about63.1 MiB.
The preflight estimated 110,516,224 bytes of series storage and at most363,757
recurrence pairs. That estimate was not treated as a memory bound; the Job
Object supplied the cap. No heavy computation was required. The initial heavy
lease was explicitly released unused and the release was delivered to the
integrator. All original task Python processes exited; PID22724 was later
reused by svchost, recorded separately rather than reported as a live worker.

Reproduce from the supplied worktree:

```powershell
& './analysis/b16_01_receive.ps1'
```

This runs the count and transport receivers sequentially under separate
60-second/512-MiB caps. It writes only owned B16 receipt paths. The saved
producer receipt predates a receiver-only mutation-check improvement; the
current receiver source freshly regenerated the same certificate successfully.

Primary artifacts:

- docs/b16_01_proof.md: full finite argument, map/transport proof and limitations.
- analysis/b16_01_finite.py, b16_01_transport.py, b16_01_receive.ps1: bounded receivers.
- results/b16_01/certificate.json.gz: all rational sums, characters, channels,
  finite correction hooks and small controls (229435 bytes).
- results/b16_01/input_hashes.json: exact working-byte SHA256 for all local
  source/context files read; code hashes also appear in the execution receipts.
- results/b16_01/transport.json, resource_summary.json and lease_release.json.
- delivery/b16_01/MANIFEST.json: output inventory and delivery hashes.

Certificate SHA256:
`61f4198e72028642211f350398dd81a5d49683941dabc6df14085fb3c038038c`.

Limitations: no finite quartic ambient census, new padding image rank/minor,
complete determinant filtration, or positive gap. Independent ten-variable
z*per3 was preserved throughout. Frozen per-worktree HEAD is inherited from
the launch manifest; no fresh Git binding or unified merged base is claimed.
The delivery is a filesystem artifact, not a new commit or publication.

Next sufficient witness: combine an exact finite ambient count with either
the exclusion inequality a>=U+11, or a globally certified determinant ideal
floor q and an actual ten-variable padding coordinate minor of rank r with
q+r>a. Lowering the padding ceiling further now requires information about
the product-map image or its genuine-permanent restriction, not more finite
cubic source counts at these cells.

The initial integrator progress message was rejected by automatic approval
review due to an account usage-limit error. After the authorized resume,
progress and lease-release messages succeeded; no delivery blockage remains.
The read-only CIM process query returned access denied, so an ordinary
Get-Process query was used to inspect process state.
