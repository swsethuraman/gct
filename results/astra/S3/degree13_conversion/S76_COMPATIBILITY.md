# Degree-24 interface: inspected, not converted

After the degree-13 bridge passed, this continuation inspected the local s76 bundle at commit `99852a406be2ec46f8d063354129db38226e053c`. Its source code, report, dimension tables, top source and top Gram arrays were extracted read-only into this continuation's `inputs/s76/`; exact hashes are in [s76_compatibility_inspection.json](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S3/degree13_conversion_20260908/artifacts/s76_compatibility_inspection.json). No degree-24 source construction, pairing or evaluation was launched.

The bundle contains E24 of shape 274-by-2168 and G24 of shape 274-by-274 at each house prime, plus twelve ordered predecessor labels and widths. It contains **no** `s76_dag/level_DD_pP.npz` files. s76's report says these full inclusion levels were saved in its computation environment but not committed. The local search did not locate them. The top matrices and dimension tables alone cannot replay a recursive pairing.

## Concrete convention mismatch and transport

Let r = 1/(content(i+1)-content(i)). In S3, the column action is

`s_i e_T = r e_T + (1+r) e_swapped`.

s76's saved implementation instead uses

`s_i f_T = r f_T + (1-r) f_swapped`.

These are diagonal gauges, not interchangeable coordinate arrays. Let g_T be the S3 seminormal squared norm, with row-superstandard norm one. Its adjacent-tableau ratio is g_swapped/g_T = (1-r)/(1+r). The exact intertwiner is

`f_T -> e_T / g_T`.

Indeed the two off-diagonal coefficients agree after this scaling. It also carries the s76 norm 1/g_T to the S3 invariant form. This specifies the map, including its overall normalization.

For a horizontal four-strip lambda/mu, write g_relative(S) = g_(T_child appended S)/g_T_child; it depends only on mu and the strip filling S. If S0 is the lexicographically first standard strip filling, s76's normalized invariant has coefficient

`c_s76(S) = g_relative(S) / g_relative(S0)`.

After the gauge map, the s76 strip embedding is the S3 all-one embedding multiplied by

`q(mu,lambda) = 1 / g_relative(S0)`.

The diagnostic executes s76's exact Fraction strip-invariant implementation and verifies this formula on all 12 nonzero-predecessor strips at the degree-13 root. The exact rational q values and filling counts are retained. This is a small compatibility check, not an audit over the degree-24 DAG.

A future adapter has two concrete choices. It can contract s76's source directly in S3 seminormal coordinates by using q-weighted strip embeddings and **transposing** each row-stored E to obtain the column inclusion U. Alternatively it can build explicit per-node coordinate transforms into another independently certified S3 basis. If T_mu maps s76 child coordinates into S3 child coordinates, the parent precursor inclusion is blockdiag(q(mu,lambda) T_mu) E_lambda^t; solve for its coordinates in the S3 parent U and verify equality, residuals, full rank and transported Grams. This transport must be computed at every included node; a top-level transpose or matching pivot pattern does not suffice.

Keep the query vector e_tc in S3 coordinates when reusing the present circuit map. If queries instead use s76's f_tc, its polynomial image is the column wedge divided by g_tc; adjust both pairing and circuit normalization consistently. Recompute g_tc for lambda24, and use house factor (4!)^24. Audit the actual bubble-word direction with a small nonsymmetric permutation: s76's comments and generator order must not substitute for a pi-versus-inverse test. Retain C = G_M^(-1) A and E = C^(-t) E_circuit with basis vectors as columns.

## Required predecessor and common-source data

Obtain all saved inclusion levels, their hashes, per-node multiplicities, ordered `horiz_strips` predecessor blocks, RREF row-basis labels and residual/kernel certificates. Include the empty shape explicitly: s76 counts 7,658 nodes including degree zero; older counts of 7,657 omit that base. Reconcile overlapping degree-13 nodes using the gauge/strip map and explicit source-coordinate transport; the current degree-13 arrays cannot simply replace s76's nodes.

For a common rational source across primes, lift one specified first-prime set of E matrices recursively and apply rational H averages in the chosen gauge. Compute the second-prime transport with the matching Gram forms, including q factors if using S3 coordinates. Verify nonsingularity at every required node. s76 reports equal pivot and zero patterns at two primes; those patterns alone do not establish one rational basis.

## Storage and bounded next measurements

s76 reports 70,070,803 inclusion entries over the full DAG: 280,283,212 bytes as uint32, already larger than 256 MiB before Python objects or contractions. Its reported peak adjacent levels have 15,997,326 entries: 63,989,304 raw uint32 bytes. These are arithmetic consequences of its recorded counts, not independently measured memory for a new adapter. The inspected top E24 has 594,032 entries: 2,376,128 bytes as stored uint32, or 4,752,256 as int64. A dense 2168-by-2168 int64 precursor Gram alone requires 37,601,792 bytes. s76 reports 0.67 GB for its largest source solve; do not transfer S3's 256 MiB source-construction cap to that implementation.

Before any target conversion, measure the retrieved predecessor files' actual bytes and the cache needed by one recursive query. Stream levels or individual nodes and retain only needed source Grams; the current degree-13 Gram wrapper retains precursor Grams at all nodes and must be redesigned for the target. Record I/O and cache peaks as well as matrix bytes.

The core shape-resolved pairing method is general, but current wrappers contain degree-13 constants: 52 slots, 13 letters, 39 outputs and lambda=(21,17,2^7). Parameterize these to 96 slots, 24 letters, 274 outputs and lambda=(65,17,2^7) only in a separately bounded adapter trial. Its column heights are 9,9, fifteen 2s and forty-eight 1s. Measure a few prescribed query contraction widths and circuit evaluation widths before setting a full selection budget. Source-path witnesses can propose circuits, but only actual pairing columns certify their independence.

No full degree-24 conversion is proposed on the strength of small local swap blocks. Candidate coverage, predecessor access cost, full-query widths and evaluation cost remain unresolved. The usable target basis and the determinant273/true-padded274/D=1 programme claims remain open.
