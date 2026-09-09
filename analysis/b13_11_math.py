"""Small exact computations for B13-11; no new numerical search."""
from functools import lru_cache
from itertools import permutations


@lru_cache(maxsize=4096)
def stable_weight_dimension(mu):
    # Independent integrator's object-integer DP: no machine integer overflow,
    # modular sizing assumption, or CRT reconstruction.
    from wk12_int_s79_stable_verify import weight_dim
    return weight_dim(tuple(mu)+(0,)*(5-len(mu)))


def a_inf_exact(tail,cache=None):
    tail=tuple(int(x) for x in tail)
    if len(tail)>5: raise ValueError('B13-11 exact census is bounded to five tail parts')
    tail=tail+(0,)*(5-len(tail)); rho=tuple(range(4,-1,-1)); total=0
    for w in permutations(range(5)):
        mu=tuple(tail[i]+rho[i]-rho[w[i]] for i in range(5))
        if min(mu)<0: continue
        sign=(-1)**sum(w[i]>w[j] for i in range(5) for j in range(i+1,5))
        total+=sign*stable_weight_dimension(tuple(sorted(mu,reverse=True)))
    if total<0: raise ValueError(f'negative stable multiplicity at {tail}')
    return total
