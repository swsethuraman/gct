# Session 50 — robustness and dual-dimension audit (banked)

All numbers reproduce from `analysis/wk9_s50_*.py`; primes
`p1=2147483647, p2=2147483629, p3=2147483587`.

## Engine validation (wk9_s50_validate.py)

    V1  det_3 divisibility (n=3, F=7, edeg=7): DIVIDES  (p1,p2), deg g = 7
    V2  generic cubic in 9 vars:               NOT_DIVIDES
    V3  rank H_det3 on {det=0} = 6 = 2n ;  generic = 9
    V4  rank H_det4 on {det=0} = 8 = 2n ;  generic = 16

## Four controls (wk9_s50_experiment.py, plane seed=0)

    1 det_4          DIVIDES      (p1,p2)   -> in I(D_det)
    2 generic quartic NOT_DIVIDES (p1)
    3 l*c            NOT_DIVIDES  (p1)
    4 x0*per_3       NOT_DIVIDES  (p1,p2)   -> not in I(P_pad)   [SEPARATION]

## Independent exact-Q verification (wk9_s50_verify.py)

    C1 det_4    remainder over Q == 0            (exact division certificate)
    C4 x0*per_3 remainder over Q != 0            (explicit nonzero rational poly)
               on two independent planes B, B'
    rank on {per_3=0}: 9 at all 6 sampled points

## Robustness (wk9_s50 robustness run)

    5 independent full 9-planes (seeds 1,2,3,9,17):
        det_4  = DIVIDES     at every plane
        x0per3 = NOT_DIVIDES at every plane
    x0*per_3 over three primes (p1,p2,p3): NOT_DIVIDES, G not identically zero
    active-only 9-plane (rows 10..15 = 0): x0*per_3 NOT_DIVIDES

## Dual-dimension audit (rank H on {P=0}; dim dual = rank - 2), both primes

    det_4            rank 8  -> dim dual 6  = 2n-2      (in Dual_{6,4,16})
    x0*per_3         rank 9  -> dim dual 7  > 6         (NOT in Dual_{6,4,16})
    generic quartic  rank 10 -> dim dual 8  (10 active vars; a generic quartic in
                                             P^9 has a hypersurface dual, dim 8)

The determinant sits exactly at dim dual = 2n-2 = 6; the padded permanent is one
higher, dim dual = 7 — the geometric reason the k=6 equation separates.
