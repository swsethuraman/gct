# Stabiliser-reduction validation battery — session 36

Run before any new cell (PREREG_s36.md P1).  Both house primes at every rank.  Pad points everywhere are true padded-permanent restrictions `x_0 · per_3(x_1..x_9)` with random linear-form substitutions.

## Part 3 — the gate: the `l^3 m` witness (reduced and unreduced) and `wk8_s30_calib.py` as-is

- reduced witness, p = 2147483647: a = 1, kernel ∝ `(12, -3, 1)`, mult = 0 — ok (wrong rule would give `(1,-4,3)`, mult 1)
- reduced witness, p = 2147483629: a = 1, kernel ∝ `(12, -3, 1)`, mult = 0 — ok (wrong rule would give `(1,-4,3)`, mult 1)
- unreduced witness (`wk8_s30_core.measure`): mult = 0 — ok
- `analysis/wk8_s30_calib.py` as-is:

```
PASS witness {l^3 m} lam=(4,4) delta=2 : mult = 0
PASS witness kernel == (12,-3,1)
PASS discriminating battery: 48 World A cells, 41 with mult < a
PASS session 26's five cells
PASS mult_det = a at all 20 weights, n=3, delta<=4

CALIBRATION PASSED
```

**Part 3: PASS** — discriminating ratio quoted from the battery line above (World A cells with `mult < a` / cells).

_(part 3: 1s)_

---
**BATTERY PASSED** (parts run: ['3'])

## Part 1 — isotypic containment of the unreduced kernel, per candidate character

`dim(ker R ∩ V_psi)` for every linear character `psi` of `Stab(lam)` (`m^k:t` = trivial on the block of value `m`, size `k`; `:s` = sign).  Lemma predicts `a` at `psi = chi_lam` (sign iff `m` odd) and `0` elsewhere.

| lam | delta | a | Stab | character | dim(ker ∩ V_psi) | predicted | verdict |
|---|---|---|---|---|---|---|---|
| `(13, 5, 2, 2, 2)` | 6 | 2 | 6 | `2^3:t` | 2 | 2 | ok |
| `(13, 5, 2, 2, 2)` | 6 | 2 | 6 | `2^3:s` | 0 | 0 | ok |
| `(14, 4, 2, 2, 2)` | 6 | 2 | 6 | `2^3:t` | 2 | 2 | ok |
| `(14, 4, 2, 2, 2)` | 6 | 2 | 6 | `2^3:s` | 0 | 0 | ok |
| `(12, 6, 2, 2, 2)` | 6 | 4 | 6 | `2^3:t` | 4 | 4 | ok |
| `(12, 6, 2, 2, 2)` | 6 | 4 | 6 | `2^3:s` | 0 | 0 | ok |
| `(13, 5, 4, 1, 1)` | 6 | 2 | 2 | `1^2:t` | 0 | 0 | ok |
| `(13, 5, 4, 1, 1)` | 6 | 2 | 2 | `1^2:s` | 2 | 2 | ok |
| `(12, 5, 5, 1, 1)` | 6 | 2 | 4 | `5^2:t,1^2:t` | 0 | 0 | ok |
| `(12, 5, 5, 1, 1)` | 6 | 2 | 4 | `5^2:t,1^2:s` | 0 | 0 | ok |
| `(12, 5, 5, 1, 1)` | 6 | 2 | 4 | `5^2:s,1^2:t` | 0 | 0 | ok |
| `(12, 5, 5, 1, 1)` | 6 | 2 | 4 | `5^2:s,1^2:s` | 2 | 2 | ok |
| `(9, 8, 5, 1, 1)` | 6 | 2 | 2 | `1^2:t` | 0 | 0 | ok |
| `(9, 8, 5, 1, 1)` | 6 | 2 | 2 | `1^2:s` | 2 | 2 | ok |
| `(7, 7, 4, 1, 1)` | 5 | 1 | 4 | `7^2:t,1^2:t` | 0 | 0 | ok |
| `(7, 7, 4, 1, 1)` | 5 | 1 | 4 | `7^2:t,1^2:s` | 0 | 0 | ok |
| `(7, 7, 4, 1, 1)` | 5 | 1 | 4 | `7^2:s,1^2:t` | 0 | 0 | ok |
| `(7, 7, 4, 1, 1)` | 5 | 1 | 4 | `7^2:s,1^2:s` | 1 | 1 | ok |

**Part 1: 7 cells, 7 discriminating** (each has >= 2 candidate characters; the three even-block cells kill a 'sign always' rule, the three odd-block cells kill a 'trivial always' rule, the two-block cells `(12,5,5,1,1)` and `(7,7,4,1,1)` (four candidate characters each) kill every mixed rule).  Failures: none.

_(part 1: 598s)_

---
**BATTERY PASSED** (parts run: ['1'])

## Part 2 — reduced pipeline vs the s30 ledger, and compressed vs exact

| lam | a (pleth) | N_S | Stab | n_chi | rows | route | a (kernel) | rank(R) | mult_det | mult_pad | ledger (det, pad) | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `(13, 5, 2, 2, 2)` | 2 | 3672 | 6 | 825 | 7214 | exact | 2 | 823 | 2 | 2 | (2, 2) | ok |
| `(14, 4, 2, 2, 2)` | 2 | 2337 | 6 | 546 | 4626 | exact | 2 | 544 | 2 | 2 | (2, 2) | ok |
| `(12, 6, 2, 2, 2)` | 4 | 5194 | 6 | 1162 | 10081 | exact | 4 | 1158 | 4 | 4 | (4, 4) | ok |
| `(13, 5, 4, 1, 1)` | 2 | 1824 | 2 | 658 | 1592 | exact | 2 | 656 | 2 | 2 | (2, 2) | ok |
| `(12, 5, 5, 1, 1)` | 2 | 2795 | 4 | 524 | 2514 | exact | 2 | 522 | 2 | 2 | (2, 2) | ok |
| `(9, 8, 5, 1, 1)` | 2 | 5159 | 2 | 1947 | 4857 | exact | 2 | 1945 | 2 | 2 | (2, 2) | ok |

Compressed route (`Agg = P·M`, certified) against the exact route, three cells:

| lam | prime | a | mult_det | mult_pad | kernel span identical | verdict |
|---|---|---|---|---|---|---|
| `(13, 5, 2, 2, 2)` | 2147483647 | 2 | 2 | 2 | yes | ok |
| `(13, 5, 2, 2, 2)` | 2147483629 | 2 | 2 | 2 | yes | ok |
| `(12, 5, 5, 1, 1)` | 2147483647 | 2 | 2 | 2 | yes | ok |
| `(12, 5, 5, 1, 1)` | 2147483629 | 2 | 2 | 2 | yes | ok |
| `(12, 6, 2, 2, 2)` | 2147483647 | 4 | 4 | 4 | yes | ok |
| `(12, 6, 2, 2, 2)` | 2147483629 | 4 | 4 | 4 | yes | ok |

**Part 2 failures: none.**

_(part 2: 44s)_


## Part 3 — the gate: the `l^3 m` witness (reduced and unreduced) and `wk8_s30_calib.py` as-is

- reduced witness, p = 2147483647: a = 1, kernel ∝ `(12, -3, 1)`, mult = 0 — ok (wrong rule would give `(1,-4,3)`, mult 1)
- reduced witness, p = 2147483629: a = 1, kernel ∝ `(12, -3, 1)`, mult = 0 — ok (wrong rule would give `(1,-4,3)`, mult 1)
- unreduced witness (`wk8_s30_core.measure`): mult = 0 — ok
- `analysis/wk8_s30_calib.py` as-is:

```
PASS witness {l^3 m} lam=(4,4) delta=2 : mult = 0
PASS witness kernel == (12,-3,1)
PASS discriminating battery: 48 World A cells, 41 with mult < a
PASS session 26's five cells
PASS mult_det = a at all 20 weights, n=3, delta<=4

CALIBRATION PASSED
```

**Part 3: PASS** — discriminating ratio quoted from the battery line above (World A cells with `mult < a` / cells).

_(part 3: 1s)_

---
**BATTERY PASSED** (parts run: ['3'])

## Part 1 — isotypic containment of the unreduced kernel, per candidate character

`dim(ker R ∩ V_psi)` for every linear character `psi` of `Stab(lam)` (`m^k:t` = trivial on the block of value `m`, size `k`; `:s` = sign).  Lemma predicts `a` at `psi = chi_lam` (sign iff `m` odd) and `0` elsewhere.

| lam | delta | a | Stab | character | dim(ker ∩ V_psi) | predicted | verdict |
|---|---|---|---|---|---|---|---|
| `(13, 5, 2, 2, 2)` | 6 | 2 | 6 | `2^3:t` | 2 | 2 | ok |
| `(13, 5, 2, 2, 2)` | 6 | 2 | 6 | `2^3:s` | 0 | 0 | ok |
| `(14, 4, 2, 2, 2)` | 6 | 2 | 6 | `2^3:t` | 2 | 2 | ok |
| `(14, 4, 2, 2, 2)` | 6 | 2 | 6 | `2^3:s` | 0 | 0 | ok |
| `(12, 6, 2, 2, 2)` | 6 | 4 | 6 | `2^3:t` | 4 | 4 | ok |
| `(12, 6, 2, 2, 2)` | 6 | 4 | 6 | `2^3:s` | 0 | 0 | ok |
| `(13, 5, 4, 1, 1)` | 6 | 2 | 2 | `1^2:t` | 0 | 0 | ok |
| `(13, 5, 4, 1, 1)` | 6 | 2 | 2 | `1^2:s` | 2 | 2 | ok |
| `(12, 5, 5, 1, 1)` | 6 | 2 | 4 | `5^2:t,1^2:t` | 0 | 0 | ok |
| `(12, 5, 5, 1, 1)` | 6 | 2 | 4 | `5^2:t,1^2:s` | 0 | 0 | ok |
| `(12, 5, 5, 1, 1)` | 6 | 2 | 4 | `5^2:s,1^2:t` | 0 | 0 | ok |
| `(12, 5, 5, 1, 1)` | 6 | 2 | 4 | `5^2:s,1^2:s` | 2 | 2 | ok |
| `(9, 8, 5, 1, 1)` | 6 | 2 | 2 | `1^2:t` | 0 | 0 | ok |
| `(9, 8, 5, 1, 1)` | 6 | 2 | 2 | `1^2:s` | 2 | 2 | ok |
| `(7, 7, 4, 1, 1)` | 5 | 1 | 4 | `7^2:t,1^2:t` | 0 | 0 | ok |
| `(7, 7, 4, 1, 1)` | 5 | 1 | 4 | `7^2:t,1^2:s` | 0 | 0 | ok |
| `(7, 7, 4, 1, 1)` | 5 | 1 | 4 | `7^2:s,1^2:t` | 0 | 0 | ok |
| `(7, 7, 4, 1, 1)` | 5 | 1 | 4 | `7^2:s,1^2:s` | 1 | 1 | ok |

**Part 1: 7 cells, 7 discriminating** (each has >= 2 candidate characters; the three even-block cells kill a 'sign always' rule, the three odd-block cells kill a 'trivial always' rule, the two-block cells `(12,5,5,1,1)` and `(7,7,4,1,1)` (four candidate characters each) kill every mixed rule).  Failures: none.

_(part 1: 598s)_

---
**BATTERY PASSED** (parts run: ['1'])

## Part 2 — reduced pipeline vs the s30 ledger, and compressed vs exact

| lam | a (pleth) | N_S | Stab | n_chi | rows | route | a (kernel) | rank(R) | mult_det | mult_pad | ledger (det, pad) | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `(13, 5, 2, 2, 2)` | 2 | 3672 | 6 | 825 | 7214 | exact | 2 | 823 | 2 | 2 | (2, 2) | ok |
| `(14, 4, 2, 2, 2)` | 2 | 2337 | 6 | 546 | 4626 | exact | 2 | 544 | 2 | 2 | (2, 2) | ok |
| `(12, 6, 2, 2, 2)` | 4 | 5194 | 6 | 1162 | 10081 | exact | 4 | 1158 | 4 | 4 | (4, 4) | ok |
| `(13, 5, 4, 1, 1)` | 2 | 1824 | 2 | 658 | 1592 | exact | 2 | 656 | 2 | 2 | (2, 2) | ok |
| `(12, 5, 5, 1, 1)` | 2 | 2795 | 4 | 524 | 2514 | exact | 2 | 522 | 2 | 2 | (2, 2) | ok |
| `(9, 8, 5, 1, 1)` | 2 | 5159 | 2 | 1947 | 4857 | exact | 2 | 1945 | 2 | 2 | (2, 2) | ok |

Compressed route (`Agg = P·M`, certified) against the exact route, three cells:

| lam | prime | a | mult_det | mult_pad | kernel span identical | verdict |
|---|---|---|---|---|---|---|
| `(13, 5, 2, 2, 2)` | 2147483647 | 2 | 2 | 2 | yes | ok |
| `(13, 5, 2, 2, 2)` | 2147483629 | 2 | 2 | 2 | yes | ok |
| `(12, 5, 5, 1, 1)` | 2147483647 | 2 | 2 | 2 | yes | ok |
| `(12, 5, 5, 1, 1)` | 2147483629 | 2 | 2 | 2 | yes | ok |
| `(12, 6, 2, 2, 2)` | 2147483647 | 4 | 4 | 4 | yes | ok |
| `(12, 6, 2, 2, 2)` | 2147483629 | 4 | 4 | 4 | yes | ok |

**Part 2 failures: none.**

_(part 2: 47s)_

---
**BATTERY PASSED** (parts run: ['2'])

## Part 4 — the s35 cell `mult_det((10,10,10,6), 9)` at `r = 4`

- `a = 10` by plethysm; `N_S = 659741`, `|Stab| = 6` (block `10^3`, even → trivial character; singleton 6), `n_chi = 111508` (70s of orbit enumeration).
- Resident model for the compressed route: `8 · n_chi^2 = 99 GB`; measured constant `2.5e-8 · n_chi^2 = 311 GB` — against 6.5 GB usable.  **The direct measurement is out of reach on this container by a factor of ~48.**
- What stands: s35's T1w exhibits one weight-`(10,10,10,6)` HWV (the extremal catalecticant 9-minor) nonzero at a det pencil, so `mult_det >= 1`; `mult_det = a = 10` follows from `docs/s35_review.md` §2 (principality of `I(D_4^det)` + no rectangular equation below degree 10, s33).  Not banked as a measurement.  See the PREREG P1.4 feasibility line, written before this part ran.

_(part 4: 70s)_

---
**BATTERY PASSED** (parts run: ['4'])
