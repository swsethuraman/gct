# `A14_exact.json.gz` — the exact degree-14 source matrix

Gzipped per the board's 5 MB rule (§5: "gzip with a README giving original name,
size, both checksums and the decompression command").

| | |
|---|---|
| original name | `A14_exact.json` |
| original size | 787,449 bytes |
| original md5 | `0bf5883e254b0e9a0a0c5067c1680d9c` |
| original sha256 | `1197577cfe9a2e48e85d73cf421c884628c131c14db27ccc9d8504225f35514b` |
| compressed name | `A14_exact.json.gz` |
| compressed size | 342,817 bytes |
| compressed md5 | `8d18d20451a32fa0401ab9b84b977842` |
| compressed sha256 | `68a555cd11c566a8ed8dfe0fe87dff1bb1427a96165d8f493684b3bcea7a241d` |

Decompress with:

    gunzip -c results/b14_07/A14_exact.json.gz > A14_exact.json

## Contents

`matrix` is 93 rows x 212 columns of **decimal strings** (JSON has no exact
integer type at this magnitude; the largest entry is 134 bits). Rows are in
`results/s74/source.json` order restricted to rung <= 14; columns are in
`results/b14_prep/points/P14.json` order, 192 `primary` then 20 `holdout`, and
the `points` array gives each column's `role`.

`values_are`: literal transported fillings at degree 14,
`A[i][j] = F_native_i(f_j) * u(f_j)^(14 - d_i)`, `u = 4! [s_1^4] f`; **not**
u-normalised (the u-normalised vector is this divided by `24^(14 - d_i)`);
signed integers over Z.

**Orientation**: rows are source fillings and columns are points, so the ideal
relations live in the **LEFT** kernel — `K14` in `K14.json` satisfies
`A14^T . K14 = 0`. The right kernel is a different, larger space and is not the
object wanted.

The kernel dimension `k = 5` is determined on the 192 primary columns only; the
20 holdout columns are a control (C8) and all five kernel vectors annihilate them
too.
