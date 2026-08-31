# The live locus, verified and ranked

Independent check of the critique session's ambient-cap argument, plus a
ranking of the weights it leaves alive.  Written from scratch (the container
had reset; no repo, no session-24b code) — Murnaghan–Nakayama, plethysm and
symmetric-Kronecker all re-derived, so this shares no code with either track.

## 1. The critique's claims, verified

`a(lam,delta)` = multiplicity of `S_lam(C^9)` in `Sym^delta(Sym^3 C^9)`, the
ambient both closures are quotients of, so `mult_det, mult_per <= a` and
`D <= a`.

| delta | weights (<=9 rows) | a=0 | a=1 | a>=2 |
|---|---|---|---|---|
| 2 | 11 | 9 | 2 | 0 |
| 3 | 30 | 25 | 5 | 0 |
| 4 | 73 | **61** | **12** | 0 |
| 5 | 157 | 129 | 27 | **1 — (9,4,2), a=2** |

- `Sym^2(Sym^3) = s_(6) + s_(4,2)`, so **a((2,2,2),2) = 0**: both closure
  counts are forced to zero, `def = m` on both sides, and `Def = P` is an
  identity, not a measurement.  CONFIRMED.
- delta=4 split 61/12 and delta=5 split 156/1 both reproduce.  CONFIRMED.
- `g((9,4,2),5^3,5^3) = 3`.  CONFIRMED.

## 2. Where the live locus opens up

| delta | weights | a>=2 | % live |
|---|---|---|---|
| 5 | 157 | 1 | 0.6% |
| 6 | 318 | 12 | 3.8% |
| 7 | 598 | 50 | 8.4% |

The wall is a **low-degree** wall, not a structural one.

## 3. World A is NOT ambient-starved — the Week-1 kill criterion probably misfires

Ambient `Sym^delta(Sym^4 C^2)`; `a((4d-b,b),d) = N(b) - N(b-1)` with `N` the
Gaussian binomial (partitions in a delta x 4 box).

| delta <= 14 | count |
|---|---|
| a = 0 | 27 of 221 (**12.2%**, falling: 2 of 29 at delta=14) |
| a = 1 | 60 |
| **a >= 2** | **134 (61%)** |

So 61% of World A weights had genuine room for a multiplicity obstruction and
D was zero there anyway.  The ambient cap fully dissolves the n=3 flagship
datum; it does not obviously dissolve the 742.

Complication in the other direction: `a=0` *guarantees* `D=0`, so a=0 cells are
over-represented among the zeros, and 27 forced weights across ~21 closure
pairs is the same order as 742.  The audit's outcome is genuinely uncertain.
PREDICTION (registered before the audit): well under 90% forced.

## 4. The ranked live locus — and the profile that does not occur

`mult_det <= min(m_det, a)` and `mult_per <= a`.  The prize profile is
`m_det < a`: the determinant lacking the orbit functions to fill the ambient
room, giving an obstruction with no help from any deficit.

`m_det` recomputed from scratch as the symmetric Kronecker
`m_det = (1/2) sum_rho (chi^lam(rho)/z_rho) [ chi^rect(rho)^2 + chi^rect(tau(rho)) ]`,
`tau` halving each even part into two.  Calibrated against the measured easy
counts: sums 3, 11, 43 and supports 3, 10, 34 at delta=2,3,4 — all exact.

| delta | a>=2 weights | with m_det < a | with m_det = 0 |
|---|---|---|---|
| 5 | 1 | **0** | 0 |
| 6 | 12 | **0** | 0 |
| 7 | 50 | **0** | 0 |

**In all 63 live weights through delta=7, `m_det >= a`.**  The prize profile
does not occur in range.  The binding cap is `a` on both sides, so an
obstruction still requires the determinant's deficit to do work.

Cheapest cells (a is the cap, both sides):

    delta=5   (9,4,2)    a=2  m_det=3
    delta=6   (12,6)     a=2  m_det=2     <- two bits decide it
    delta=7   (15,6)     a=2  m_det=2     <- two bits decide it

At a=2 the lambda-isotypic multiplicity space is 2-dimensional, so `mult` is a
rank computation there — the paper's one-bit argument at a=1, one step up.  No
level algorithm.

## 5. Addition to the Week-1 audit

The paper's own deficit numbers need the same screen.  At delta=2 `m_det` is
supported on `(6), (4,2), (2,2,2)` with `a = 1, 1, 0`.  So
`def((2,2,2),2) = 1` — the base point of the flagship conductor result — is
ambient-forced, not boundary geometry.  The conductor statement `c = 1` is
unaffected as a statement (it says the deficit clears at the first ray step),
but whether §4 frames that base deficit as non-normality should be checked
before submission, not after.
