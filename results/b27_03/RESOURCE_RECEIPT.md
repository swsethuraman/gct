# B27-03 resource receipt

The compute allowance is 10 runs, each ≤ 60 s and ≤ 512 MB, run sequentially. **Seven runs were used.** Interpreter: Python 3.12.10, sympy 1.14.0 and numpy 2.4.6, all pre-installed.
Memory was not instrumented. The largest array was 1921×1905 int64, about 29 MB, so each run stayed far below 512 MB. Wall times are shell `time` real seconds.
The working directory is the worktree root. `lib` = `analysis/b27_03_kernel_lib.py` (sha256 `b868eaf593d3b6a9cf2c8978a94df2159b69a2d759e1b0d2828007f95e6a4002`), derived mechanically from run 2's script with the job list removed.

| # | start (UTC, 2026-09-23) | command | input sha256 (script; lib) | output | output sha256 | wall |
|---|---|---|---|---|---|---|
| 1 | 03:53:49 | `python analysis/b27_03_witness.py results/b27_03/witness.json` | e8469bfa207dc57eda317f134c02a2294c1254d3df1466cff59f8148066f6c8b | witness.json | 132616f48f90150f24de0cda27fab118db22408c9e62d828fdd1fbcc884142a9 | 1.14 s |
| 2 | 03:54:53 | `python analysis/b27_03_kernel.py results/b27_03/kernel_run2.json` | cb14818b59fbb975080f27301be32d5958dff1ab1653db5fb25087ef9e2730a8 | kernel_run2.json | 53faa7c20f94dcd03bd6a79dee1a34358916c5f5dca23fc1ba3462c5ee3918f9 | 6.22 s |
| 3 | 03:56:01 | `python analysis/b27_03_kernel2.py results/b27_03/kernel_run3.json` | 614c416bb326d9c0a63599d81e0eb8fdfeb89f241324e2f37416de0b61348b46; lib | kernel_run3.json | b8142414ce319ec3843ed49d95b31b9c818415b91dcfbbbe171461a4a99a10ef | 42.75 s |
| 4 | 03:57:28 | `python analysis/b27_03_dims.py results/b27_03/dims_run4.json` | 29f9e319ab02840ec948b73cb52e8378a48dbdaa6b420aa5a806849b30c20f56 | dims_run4.json | f73e4616269b7fb810ec15eb8d7ab26af61780adc6e2b9c5d626850ee2572c09 | 0.97 s |
| 5 | 03:58:03 | `python analysis/b27_03_rays.py results/b27_03/rays_run5.json` | 88fda4ab517fc03d2621b983533a23f7d0108a4d21d3b23632981340fb7d153c; lib | rays_run5.json | 784606b0fb8b06d93b4c478fa8d594ce8f668b1f1201a92480aaabafca7fc9e9 | 33.89 s |
| 6 | 03:59:23 | `python analysis/b27_03_deg4.py results/b27_03/deg4_run6.json` | 109f8948c321c7d342f917277addb527ed9db2923d423955dac711a9c65761cb; lib | deg4_run6.json | 4668d2bf59dd3356a25787b3205cc01045d1299b2b3902d0a8d82c2c0eb9e03a | 30.59 s |
| 7 | 04:01:02 | `python analysis/b27_03_ray2.py results/b27_03/ray2_run7.json` | 7e96a3e19e21f0664fcd823d8f932688cc18bb2a12d6d9b949c064a7b8fd1103; lib | ray2_run7.json | e2d567f2c0384a8b6a73c78c8600371cd0395a0456a410b73ac43e24a1087232 | 38.55 s |

Notes:
- Run 2's 70-ring result at `(8,(24,2,2,2,2))`, rank 613/619, is a point-set artifact, superseded by run 3 (rank 619/619). No claim was made from it.
- Run 5's docstring says N+32 points; the run used N+16, the library constant, and its JSON records that.
- Reviewer re-run: the same commands, from the worktree root. The outputs are deterministic: fixed seeds, exact integer arithmetic and fixed primes.
- Other processes: Git, hashing and file reads only. No random search and no sampled nullspace. Kernel claims appear only as rank = dim certificates.
