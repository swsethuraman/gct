#!/usr/bin/env python3
"""
B13-10 -- the leaner raising-row construction.

The SAME matrix as wk9_s45_build (monomials_array -> orbit_setup_arr ->
raising_rows_arr -> build_cell): the same monomial order, the same codes, the
same chi-isotypic columns and signs, the same raising rule, the same canonical
H-orbit representative per target row, the same row order (operator blocks in
order, rows in the lexicographic order of the target basis, obstructed and empty
rows removed), the same integer entries.  Every convention is inherited by
calling the tree's own routines (wk8_s30_core.exps, wk9_s36_stabred.stab_group /
perm_tables, wk9_s45_build._dp_tables and _codes -- the latter looked up at call
time so that wk11_s71_codes.install() applies here exactly as it does there).

What changes is storage and pass structure, never mathematics:

  * M and every target basis in the narrowest integer dtype that holds L-1
    (int8 / int16 / int32); col_of int32; sgn int8; canon / acc / row ids int32;
    E.data int16 when the exact bound |Stab| * delta * (n+1) < 2^15 on a summed
    entry holds (asserted; every value re-checked after the build), else int32;
    E.indices int32; E.indptr int32 where nnz < 2^31.
  * monomials level by level into arrays whose size is known before allocation
    (the feasibility DP counts the children of every live prefix), no
    list-and-concatenate.
  * the stabiliser image index in row chunks, never a full np.sort(tab[M]) copy;
    the twisted coefficients acc by scattering from the representative rows
    (acc[g.rep] += chi(g)), which is the same sum as
    acc[j] = sum_g chi(g) [g.rep(j) = j] and needs one pass over the reps.
  * per operator: the target codes computed once (the old code computed them
    twice), canonicalisation in chunks, T and its index arrays freed before the
    raising pass -- the raising pass keeps one sorted code table and one row-id
    table (indexed by sorted position) per operator.
  * the raising triples stored compactly (rid int32, col int32, val int8) per
    chunk and turned into CSR by a counting sort (triples='store'), or generated
    twice and never stored (triples='recompute'); duplicates summed in place;
    obstructed and empty rows removed by re-indexing indptr only.
  * blocks kept in memory and concatenated once (blocks='memory') or written to
    a scratch directory as they complete and assembled at the end into
    preallocated arrays (blocks='disk').

Two `exps` orderings exist in this tree and are opposite; every letter here is
resolved through wk8_s30_core.exps(n, r) by index, as wk9_s45_build does.
"""
import os, sys, time, tempfile, shutil
import numpy as np
from scipy import sparse
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import wk9_s45_build as S45                      # _codes looked up on the module at call time
from wk9_s45_build import _dp_tables, log, _rss_gb
from wk8_s30_core import exps
from wk9_s36_stabred import stab_group, perm_tables


def _rss_now_gb():
    try:
        with open('/proc/self/status') as f:
            for line in f:
                if line.startswith('VmRSS'): return int(line.split()[1]) / 1048576.0
    except Exception: pass
    return float('nan')


def letter_dtype(L):
    """narrowest signed integer dtype holding every letter index in [0, L)."""
    if L - 1 < 128: return np.int8
    if L - 1 < 32768: return np.int16
    return np.int32


def codes(M, L):
    """the tree's monomial code, whichever is installed (wk9_s42_orbits._codes or
    wk11_s71_codes.codes_wide), on a narrow-dtype M: the lookup tables are indexed
    by the letter values, which are the same integers whatever the width."""
    return S45._codes(np.asarray(M), L)


# --------------------------------------------------------------- monomials
def monomials_array_lean(n, r, delta, lam, block=250000, verbose=False, dtype=None):
    """wk9_s45_build.monomials_array with exact per-level sizing: the same rows
    in the same order (BFS in index order = the DFS lexicographic order), as an
    (N_S x delta) array of the narrowest letter dtype."""
    lam = tuple(lam) + (0,) * (r - len(lam))
    L = len(exps(n, r))
    dt = dtype or letter_dtype(L)
    if sum(lam) != delta * n:
        return np.zeros((0, delta), dtype=dt)
    REM, NID, G = _dp_tables(n, r, delta, lam)
    # suffix counts SC[k][t, s] = #{i >= s : G[k][t, i]}
    SC = []
    for k in range(delta):
        g = G[k]
        sc = np.zeros((g.shape[0], L + 1), dtype=np.int64)
        sc[:, :L] = np.cumsum(g[:, ::-1], axis=1)[:, ::-1]
        SC.append(sc)
    pref = np.zeros((1, 0), dtype=dt)
    tid = np.zeros(1, dtype=np.int32)
    last = np.zeros(1, dtype=dt)
    ar_L = np.arange(L, dtype=np.int32)
    blk = max(1000, min(block, 60_000_000 // max(L, 1)))     # the bool chunk x L mask stays ~60 MB
    for k in range(delta):
        g = G[k]; nid = NID[k]; sc = SC[k]
        cnt = sc[tid, last.astype(np.int64)]                  # children per live prefix
        total = int(cnt.sum())
        if total == 0:
            return np.zeros((0, delta), dtype=dt)
        off = np.zeros(len(cnt) + 1, dtype=np.int64); np.cumsum(cnt, out=off[1:])
        nxt = np.empty((total, k + 1), dtype=dt)
        ntid = np.empty(total, dtype=np.int32)
        nlast = np.empty(total, dtype=dt)
        for b0 in range(0, pref.shape[0], blk):
            b1 = min(b0 + blk, pref.shape[0])
            ok = g[tid[b0:b1]] & (ar_L[None, :] >= last[b0:b1, None].astype(np.int32))
            bi, ii = np.nonzero(ok); del ok
            o0, o1 = int(off[b0]), int(off[b1])
            assert o1 - o0 == len(bi), "child count disagrees with the suffix table"
            if len(bi) == 0: continue
            if k: nxt[o0:o1, :k] = pref[b0:b1][bi]
            nxt[o0:o1, k] = ii
            ntid[o0:o1] = nid[tid[b0:b1][bi], ii]
            nlast[o0:o1] = ii
            del bi, ii
        pref, tid, last = nxt, ntid, nlast
        del nxt, ntid, nlast, cnt, off
        if verbose: log(f"      level {k+1}: {pref.shape[0]} prefixes")
    assert not REM[delta][tid].any(), "residual weight nonzero at the last level"
    return pref


# ------------------------------------------------------- isotypic reduction
def _sorted_codes(M, L):
    c = codes(M, L)
    order = np.argsort(c, kind='stable')
    sc = c[order]
    assert np.all(np.diff(sc) > 0), "codes not injective"
    del c
    if len(order) < (1 << 31):
        order = order.astype(np.int32)
    return sc, order


def _image_index_chunk(Mc, tab_arr, sorted_codes, order, L):
    img = np.sort(tab_arr[Mc], axis=1)
    c = codes(img, L); del img
    p = np.searchsorted(sorted_codes, c)
    assert p.max(initial=0) < len(sorted_codes) and np.all(sorted_codes[p] == c), \
        "image monomial not in the basis (weight not preserved?)"
    del c
    return order[p]


def canon_obstructed(M, tabs, L, sorted_codes, order, chunk=400000, want_obstructed=True):
    """canon[j] = min_g index(g.m_j) (int32) and obstructed[j] = [some odd g fixes
    m_j], in row chunks of M -- the same values as wk9_s45_build._canon_acc's
    canon and obstructed."""
    N = M.shape[0]
    canon = np.empty(N, dtype=np.int32)
    obstructed = np.zeros(N, dtype=bool) if want_obstructed else None
    tab_arrs = [(np.asarray(tab, dtype=M.dtype), ch) for tab, ch in tabs]
    for b0 in range(0, N, chunk):
        b1 = min(b0 + chunk, N)
        Mc = M[b0:b1]
        cur = np.arange(b0, b1, dtype=np.int64)
        cmin = cur.copy()
        for tab_arr, ch in tab_arrs:
            idx = _image_index_chunk(Mc, tab_arr, sorted_codes, order, L)
            np.minimum(cmin, idx, out=cmin)
            if want_obstructed and ch == -1:
                obstructed[b0:b1] |= (idx == cur)
            del idx
        canon[b0:b1] = cmin
        del cur, cmin
    return canon, obstructed


def orbit_setup_lean(n, r, delta, lam, M=None, verbose=True, chunk=400000):
    """wk9_s45_build.orbit_setup_arr with the same partition, columns and signs,
    in chunked passes and narrow dtypes (col_of int32, sgn int8)."""
    lam = tuple(lam) + (0,) * (r - len(lam))
    t0 = time.time()
    L = len(exps(n, r))
    group = stab_group(lam)
    tabs = perm_tables(n, r, group)
    if M is None:
        M = monomials_array_lean(n, r, delta, lam, verbose=verbose)
    N = M.shape[0]
    if N == 0:
        return dict(M=M, col_of=np.zeros(0, np.int32), sgn=np.zeros(0, np.int8),
                    n_chi=0, N_S=0, stab=len(group), dropped=0, secs=0.0)
    G = len(group)
    if G == 1:
        # trivial stabiliser (the balanced cells): every orbit is a singleton with
        # twisted coefficient chi(id) = +1 -- canon = identity, acc = 1, exactly
        # what the two-pass computation returns
        assert group[0][1] == 1 and list(group[0][0]) == list(range(r))
        canon = np.arange(N, dtype=np.int32)
        acc = np.ones(N, dtype=np.int32)
        ar = canon
        is_rep = np.ones(N, dtype=bool)
    else:
        sorted_codes, order = _sorted_codes(M, L)
        canon, _ = canon_obstructed(M, tabs, L, sorted_codes, order, chunk=chunk, want_obstructed=False)
        ar = np.arange(N, dtype=np.int32)
        is_rep = canon == ar
        reps = np.nonzero(is_rep)[0]
        # acc by scattering from the representatives: acc[g.rep] += chi(g), one
        # bincount per group element over the images of every representative
        acc = np.zeros(N, dtype=np.int32)
        tab_arrs = [(np.asarray(tab, dtype=M.dtype), ch) for tab, ch in tabs]
        idx_all = np.empty(len(reps), dtype=np.int32)
        for tab_arr, ch in tab_arrs:
            for b0 in range(0, len(reps), chunk):
                rr = reps[b0:b0 + chunk]
                idx_all[b0:b0 + len(rr)] = _image_index_chunk(M[rr], tab_arr, sorted_codes, order, L)
            bc = np.bincount(idx_all, minlength=N)
            if ch == 1: acc += bc.astype(np.int32)
            else: acc -= bc.astype(np.int32)
            del bc
        del sorted_codes, order, idx_all, reps
    kept = is_rep & (acc != 0)
    n_chi = int(kept.sum())
    dropped = int(is_rep.sum()) - n_chi
    orbnum = np.full(N, -1, dtype=np.int32)
    orbnum[kept] = np.arange(n_chi, dtype=np.int32)
    col_of = orbnum[canon]
    del orbnum
    sgn = np.where(acc > 0, 1, -1).astype(np.int8)
    sgn[col_of < 0] = 0
    sizes = np.bincount(canon, minlength=N)
    sel = col_of >= 0
    assert np.all(np.abs(acc[sel]).astype(np.int64) * sizes[canon[sel]] == G), \
        ("twisted coefficients not +-|Stab(m)|", lam)
    assert not acc[~sel].any(), ("dropped orbit with a nonzero twisted coefficient", lam)
    del canon, acc, sizes, sel, kept, ar, is_rep
    if verbose:
        log(f"  lam={lam}: N_S={N} |Stab|={G} n_chi={n_chi} (orbits dropped: {dropped}) "
            f"[lean-b10, {time.time()-t0:.0f}s, HWM {_rss_gb():.2f} GB]")
    return dict(M=M, col_of=col_of, sgn=sgn, n_chi=n_chi, N_S=N, stab=G,
                dropped=dropped, secs=time.time() - t0)


# ---------------------------------------------------- raising operators
def entry_dtype(stab, delta, n):
    """int16 when every summed entry provably fits: an entry of E is a sum over
    the (m, k) pairs of one chi-orbit landing on one target, each term
    +-(alpha_i + 1) with alpha_i <= n, at most delta positions per monomial and
    at most |Stab| monomials per orbit."""
    bound = stab * delta * (n + 1)
    return (np.int16, bound) if bound < 32768 else (np.int32, bound)


def _triples_to_csr(chunks, nrow, ncol, dtype, counts=None):
    """counting sort of the stored (rid, col, val) chunks into a CSR with
    duplicates (summed by scipy afterwards).  `counts` (per-row triple counts)
    may be passed if already accumulated."""
    if counts is None:
        counts = np.zeros(nrow, dtype=np.int64)
        for rid, _, _ in chunks:
            counts += np.bincount(rid, minlength=nrow)
    nnz = int(counts.sum())
    ip_dt = np.int32 if nnz < (1 << 31) else np.int64
    indptr = np.zeros(nrow + 1, dtype=np.int64); np.cumsum(counts, out=indptr[1:])
    indices = np.empty(nnz, dtype=np.int32)
    data = np.empty(nnz, dtype=dtype)
    cursor = indptr[:-1].copy()
    for rid, col, val in chunks:
        o = np.argsort(rid, kind='stable')
        rs = rid[o]
        if len(rs) == 0: continue
        starts = np.r_[0, np.flatnonzero(rs[1:] != rs[:-1]) + 1]
        runlen = np.diff(np.r_[starts, len(rs)])
        rank = np.arange(len(rs), dtype=np.int64) - np.repeat(starts, runlen)
        pos = cursor[rs] + rank
        indices[pos] = col[o]
        data[pos] = val[o]
        cursor[rs[starts]] += runlen
        del o, rs, starts, runlen, rank, pos
    assert np.array_equal(cursor, indptr[1:]), "counting sort did not fill every row"
    return sparse.csr_matrix((data, indices, indptr.astype(ip_dt)), shape=(nrow, ncol), dtype=dtype)


def _finish_block(X, obst_row, lam, i):
    """sum duplicates in place, drop explicit zeros, assert the chi-obstructed
    fixed rows cancelled, and drop them and the empty rows by re-indexing indptr
    (every dropped row has zero length by then, so indices/data are untouched)."""
    X.sum_duplicates()
    X.eliminate_zeros()
    rowlen = np.diff(X.indptr)
    if obst_row.any():
        bad = int(rowlen[obst_row].sum())
        assert bad == 0, ("chi-obstructed fixed rows failed to cancel", lam, i, bad)
    keep = (rowlen > 0) & ~obst_row
    kept_rows = np.nonzero(keep)[0]
    new_indptr = np.empty(len(kept_rows) + 1, dtype=X.indptr.dtype)
    new_indptr[:-1] = X.indptr[kept_rows]
    new_indptr[-1] = X.indptr[-1]
    assert int(np.diff(new_indptr).sum()) == X.nnz
    Ek = sparse.csr_matrix((X.data, X.indices, new_indptr), shape=(len(kept_rows), X.shape[1]), dtype=X.dtype)
    Ek.has_sorted_indices = True
    Ek.has_canonical_format = True
    return Ek


def raising_rows_lean(n, r, delta, lam, arr, chunk=400000, triples='store', blocks='memory',
                      scratch=None, verbose=True, phase_hook=None):
    """The rows of every simple raising operator E_{i,i+1} restricted to V_chi --
    the same matrix as wk9_s45_build.raising_rows_arr (rows, order, values) --
    as a scipy CSR over the n_chi columns with narrow dtypes.  Returns (E, nfixed,
    phases) where phases lists per-operator sizes, seconds and HWM."""
    lam = tuple(lam) + (0,) * (r - len(lam))
    t0 = time.time()
    A = exps(n, r); idx = {a: k for k, a in enumerate(A)}; L = len(A)
    Aarr = np.array(A, dtype=np.int32)
    M = arr['M']; col_of = arr['col_of']; sgn = arr['sgn']; n_chi = arr['n_chi']
    N, d = M.shape
    edt, ebound = entry_dtype(arr['stab'], delta, n)
    ldt = M.dtype
    out_blocks = []          # (Ek) or (path, shape, nnz)
    nfixed = 0
    phases = []
    if blocks == 'disk':
        scratch = scratch or tempfile.mkdtemp(prefix='b13_10_rows_')
        os.makedirs(scratch, exist_ok=True)
    for i in range(r - 1):
        j = i + 1
        if lam[j] == 0: continue
        tgt = tuple(lam[k] + (1 if k == i else (-1 if k == j else 0)) for k in range(r))
        ti = time.time()
        T = monomials_array_lean(n, r, delta, tgt, dtype=ldt)
        nt = T.shape[0]
        if nt == 0: continue
        sortedT, orderT = _sorted_codes(T, L)
        H = stab_group(lam, fix=(i, j))
        Htabs = perm_tables(n, r, H)
        canonT, obstructedT = canon_obstructed(T, Htabs, L, sortedT, orderT, chunk=chunk)
        arT = np.arange(nt, dtype=np.int32)
        keepT = (canonT == arT) & ~obstructedT
        useT = keepT | obstructedT
        nrow = int(useT.sum())
        rowid = np.full(nt, -1, dtype=np.int32)
        rowid[useT] = np.arange(nrow, dtype=np.int32)
        obst_row = np.zeros(nrow, dtype=bool)
        obst_row[rowid[obstructedT]] = True
        # tables indexed by SORTED position, so that T and its index arrays can go
        rowid_s = rowid[orderT]
        obst_s = obstructedT[orderT]
        del T, orderT, canonT, obstructedT, arT, keepT, useT, rowid
        hit_s = np.zeros(nt, dtype=bool)
        shift = np.full(L, -1, dtype=np.int64)
        for a, al in enumerate(A):
            if al[j] > 0:
                nb = list(al); nb[j] -= 1; nb[i] += 1; shift[a] = idx[tuple(nb)]
        t_tab = time.time() - ti

        def raise_pass(emit_triples):
            """one pass over the source monomials; emit_triples(rid, col, val) per chunk."""
            for b0 in range(0, N, chunk):
                b1 = min(b0 + chunk, N)
                Mb = M[b0:b1]
                colc = col_of[b0:b1]
                sgb = sgn[b0:b1]
                live = colc >= 0
                for k in range(d):
                    src = Mb[:, k].astype(np.int64)
                    new = shift[src]
                    valid = (new >= 0) & live
                    if not valid.any(): continue
                    rows_new = Mb[valid].copy()
                    rows_new[:, k] = new[valid]
                    rows_new.sort(axis=1)
                    c = codes(rows_new, L); del rows_new
                    p = np.searchsorted(sortedT, c)
                    assert p.max(initial=0) < nt and np.all(sortedT[p] == c), \
                        "raising image not in the target basis"
                    del c
                    hit_s[p] = True
                    rid = rowid_s[p]; del p
                    sel = rid >= 0
                    if not sel.any(): continue
                    coef = (sgb[valid][sel].astype(np.int8) * (Aarr[src[valid][sel], i].astype(np.int8) + 1))
                    emit_triples(rid[sel], colc[valid][sel], coef)
                    del rid, sel, coef, valid, new, src

        tr = time.time()
        if triples == 'store':
            store = []
            def emit(rid, col, val): store.append((np.asarray(rid, dtype=np.int32), np.asarray(col, dtype=np.int32), np.asarray(val, dtype=np.int8)))
            raise_pass(emit)
            ntrip = sum(len(s[0]) for s in store)
            X = _triples_to_csr(store, nrow, n_chi, edt)
            del store
        elif triples == 'recompute':
            counts = np.zeros(nrow, dtype=np.int64)
            def count(rid, col, val): counts.__iadd__(np.bincount(rid, minlength=nrow))
            raise_pass(count)
            ntrip = int(counts.sum())
            indptr = np.zeros(nrow + 1, dtype=np.int64); np.cumsum(counts, out=indptr[1:])
            indices = np.empty(ntrip, dtype=np.int32); data = np.empty(ntrip, dtype=edt)
            cursor = indptr[:-1].copy()
            def fill(rid, col, val):
                o = np.argsort(rid, kind='stable'); rs = rid[o]
                starts = np.r_[0, np.flatnonzero(rs[1:] != rs[:-1]) + 1]
                runlen = np.diff(np.r_[starts, len(rs)])
                rank = np.arange(len(rs), dtype=np.int64) - np.repeat(starts, runlen)
                pos = cursor[rs] + rank
                indices[pos] = col[o]; data[pos] = val[o]
                cursor[rs[starts]] += runlen
            raise_pass(fill)
            assert np.array_equal(cursor, indptr[1:])
            ip_dt = np.int32 if ntrip < (1 << 31) else np.int64
            X = sparse.csr_matrix((data, indices, indptr.astype(ip_dt)), shape=(nrow, n_chi), dtype=edt)
            del counts, cursor
        else:
            raise ValueError(triples)
        t_rows = time.time() - tr
        ts = time.time()
        Ek = _finish_block(X, obst_row, lam, i); del X
        assert int(np.abs(Ek.data).max(initial=0)) <= ebound
        nfixed_i = int((obst_s & hit_s).sum())
        nfixed += nfixed_i
        ph = dict(op=f"E_{i}{j}", H=len(H), targets=int(nt), rows=int(Ek.shape[0]), nnz=int(Ek.nnz), triples=int(ntrip),
                  obstructed_hit=nfixed_i, secs_tables=round(t_tab, 1), secs_rows=round(t_rows, 1),
                  secs_finish=round(time.time() - ts, 1), hwm_gb=round(_rss_gb(), 3), rss_gb=round(_rss_now_gb(), 3))
        if blocks == 'disk':
            fn = os.path.join(scratch, f"block_{i}.npz")
            np.savez(fn, indptr=Ek.indptr, indices=Ek.indices, data=Ek.data)
            out_blocks.append((fn, Ek.shape, int(Ek.nnz), Ek.indptr.dtype)); del Ek
        else:
            out_blocks.append(Ek)
        phases.append(ph)
        if verbose:
            log(f"    {ph['op']}: |H|={ph['H']} targets {nt} canonical rows {ph['rows']} nnz {ph['nnz']} "
                f"(triples {ntrip}; obstructed fixed targets cancelled: {nfixed_i}) "
                f"[tables {t_tab:.0f}s rows {t_rows:.0f}s finish {ph['secs_finish']}s; {time.time()-t0:.0f}s, HWM {ph['hwm_gb']:.2f} GB, RSS {ph['rss_gb']:.2f} GB]")
        if phase_hook: phase_hook(ph)
        del sortedT, rowid_s, obst_s, hit_s, obst_row
    # assembly: one preallocated copy
    ta = time.time()
    if blocks == 'disk':
        nrows = sum(b[1][0] for b in out_blocks); nnz = sum(b[2] for b in out_blocks)
    else:
        nrows = sum(b.shape[0] for b in out_blocks); nnz = sum(int(b.nnz) for b in out_blocks)
    ip_dt = np.int32 if nnz < (1 << 31) else np.int64
    indptr = np.zeros(nrows + 1, dtype=ip_dt)
    indices = np.empty(nnz, dtype=np.int32)
    data = np.empty(nnz, dtype=edt)
    r0 = 0; e0 = 0
    for bi, b in enumerate(out_blocks):
        if blocks == 'disk':
            z = np.load(b[0]); ip, ix, dv = z['indptr'], z['indices'], z['data']; z.close()
        else:
            ip, ix, dv = b.indptr, b.indices, b.data
        m = len(ip) - 1; k = len(ix)
        indptr[r0 + 1:r0 + m + 1] = (ip[1:].astype(np.int64) + e0).astype(ip_dt)
        indices[e0:e0 + k] = ix
        data[e0:e0 + k] = dv
        r0 += m; e0 += k
        del ip, ix, dv
        if blocks != 'disk': out_blocks[bi] = None
    assert r0 == nrows and e0 == nnz
    del out_blocks
    if blocks == 'disk':
        shutil.rmtree(scratch, ignore_errors=True)
    E = sparse.csr_matrix((data, indices, indptr), shape=(nrows, n_chi), dtype=edt)
    E.has_sorted_indices = True
    E.has_canonical_format = True
    phases.append(dict(op='assemble', rows=int(nrows), nnz=int(nnz), secs=round(time.time() - ta, 1),
                       hwm_gb=round(_rss_gb(), 3), rss_gb=round(_rss_now_gb(), 3), data_dtype=str(edt.__name__), entry_bound=int(ebound)))
    return E, nfixed, phases


# --------------------------------------------------------------- the cell
def build_cell_lean(lam, delta, n=4, verbose=True, chunk=400000, triples='store', blocks='memory', scratch=None,
                    phase_hook=None):
    """Same dict shape as wk9_s45_build.build_cell (arr + E + sizes + seconds),
    plus `phases` and `lean=True`."""
    lam = tuple(lam); r = len(lam)
    assert sum(lam) == n * delta and all(lam[i] >= lam[i + 1] for i in range(r - 1)) and lam[-1] > 0
    t0 = time.time(); t_m = time.time()
    M = monomials_array_lean(n, r, delta, lam, verbose=verbose)
    mono_secs = time.time() - t_m
    hwm_mono = _rss_gb()
    arr = orbit_setup_lean(n, r, delta, lam, M=M, verbose=verbose, chunk=chunk)
    hwm_orb = _rss_gb()
    t_e = time.time()
    E, nfx, phases = raising_rows_lean(n, r, delta, lam, arr, chunk=chunk, triples=triples, blocks=blocks,
                                       scratch=scratch, verbose=verbose, phase_hook=phase_hook)
    rows_secs = time.time() - t_e
    out = dict(lam=lam, delta=delta, r=r, arr=arr, E=E, N_S=arr['N_S'], stab=arr['stab'],
               n_chi=arr['n_chi'], nrows=int(E.shape[0]), nnz=int(E.nnz), nfixed=nfx,
               mono_secs=mono_secs, orbit_secs=arr['secs'], rows_secs=rows_secs,
               build_secs=time.time() - t0, hwm_gb=_rss_gb(), hwm_mono_gb=hwm_mono, hwm_orbit_gb=hwm_orb,
               phases=phases, lean=True, knobs=dict(chunk=chunk, triples=triples, blocks=blocks),
               dtypes=dict(M=str(M.dtype), col_of=str(arr['col_of'].dtype), sgn=str(arr['sgn'].dtype),
                           E_data=str(E.data.dtype), E_indices=str(E.indices.dtype), E_indptr=str(E.indptr.dtype)))
    if verbose:
        log(f"  built-lean {lam} d{delta}: N_S={out['N_S']} |Stab|={out['stab']} n_chi={out['n_chi']} "
            f"rows={out['nrows']} nnz={out['nnz']} ({out['build_secs']:.0f}s: mono {mono_secs:.0f}s "
            f"orbits {arr['secs']:.0f}s rows {rows_secs:.0f}s; HWM {out['hwm_gb']:.2f} GB; E.data {E.data.dtype})")
    return out


# ------------------------------------------------ the consumer, dtype-safe
def _split_rows_safe(F, rows, colS, colU, p):
    """wk11_s71_hybrid._split_rows with the data upcast before `% p` (NumPy 2
    refuses `int16_array % 2147483647`).  Values identical."""
    R = F[rows].tocsr(); R.sort_indices()
    inS = colS[R.indices] >= 0
    nS = len(rows); nU = int((colU >= 0).sum())
    rowid = np.repeat(np.arange(nS), np.diff(R.indptr))
    Rd = R.data.astype(np.int64)
    Tr = rowid[inS]; Tc = colS[R.indices[inS]]; Tv = (Rd[inS] % p).astype(np.int64)
    T = sparse.csr_matrix((Tv, (Tr, Tc)), shape=(nS, nS), dtype=np.int64); T.sort_indices()
    diag = np.asarray(T.diagonal(), dtype=np.int64)
    assert np.all(diag != 0), "cover diagonal vanishes mod p"
    assert T.nnz == int(inS.sum())
    dinv = np.array([pow(int(dd), -1, p) for dd in diag], dtype=np.uint32)
    Ur = rowid[~inS]; Uc = colU[R.indices[~inS]]
    assert np.all(Uc >= 0)
    TU = sparse.csr_matrix((Rd[~inS].astype(np.int32), (Ur, Uc)), shape=(nS, nU), dtype=np.int32); TU.sort_indices()
    return T, dinv, TU


def _mod_p_u32(data, p, chunk=20_000_000):
    """data (any signed int dtype) reduced mod p into uint32, in chunks (no
    whole-array int64 transient)."""
    out = np.empty(len(data), dtype=np.uint32)
    for b0 in range(0, len(data), chunk):
        out[b0:b0 + chunk] = (data[b0:b0 + chunk].astype(np.int64) % p).astype(np.uint32)
    return out


def hybrid_kernel_lean(E, nc, p, a_expect, cov, seed=20260908, extra=64, nproj=8, retries=4, verbose=True, tag='',
                       ublock=None, vblock=64, mem_x=1.0e9, fo='copy', xblock='lean'):
    """wk11_s71_hybrid.hybrid_kernel on a compact E.  Identical algorithm --
    cover split, X = T^{-1} R_1[:, U] in column blocks, +-1 sparse projection of
    the Schur complement by the same C routine with the same seed, exact flint
    nullspace, block lifting, every vector verified on the full E, rank check --
    with three storage differences:
      * the cover rows and the other rows are reduced mod p through int64 in
        chunks (dtype-safe for int16 data);
      * fo='copy' forms F_o = E[other rows] as the original does; fo='inplace'
        passes ALL rows of E to the projection instead -- a cover row r satisfies
        R_1[r,U] - R_1[r,S] X = 0 exactly, so it contributes nothing, and the
        projection's per-row pseudo-random draws then index the rows of E rather
        than of F_o (a different but equally valid random projection);
      * xblock='lean' forms each X block as int32 % p -> uint32 (12 bytes per
        entry transient) instead of int64 % p (20 bytes).
    Soundness, as in the original, never depends on the randomness."""
    import wk11_s71_hybrid as HY
    from flint import nmod_mat
    t0 = time.time()
    E = E.tocsr(); E.sort_indices()
    rows = cov['rows']; S = cov['S']; U = cov['U']
    nS, nU = len(S), len(U)
    colS = np.full(nc, -1, dtype=np.int32); colS[S] = np.arange(nS, dtype=np.int32)
    colU = np.full(nc, -1, dtype=np.int32); colU[U] = np.arange(nU, dtype=np.int32)
    T, dinv, TU = _split_rows_safe(E, rows, colS, colU, p)
    TUc = TU.tocsc()
    t1 = time.time()
    mem_x = float(os.environ.get('S71_MEM_X', mem_x))
    if ublock is None:
        ublock = nU if 4.0 * nS * nU <= mem_x else max(32, int(mem_x / (4.0 * nS)))
    nblocks = (nU + ublock - 1) // ublock if nU else 0
    if fo == 'copy':
        mask = np.ones(E.shape[0], dtype=bool); mask[rows] = False
        Fo = E[np.nonzero(mask)[0]].tocsr(); Fo.sort_indices()
        del mask
    elif fo == 'inplace':
        Fo = E
    else:
        raise ValueError(fo)
    indptr = Fo.indptr.astype(np.int64); indices = np.asarray(Fo.indices, dtype=np.int32); data = _mod_p_u32(Fo.data, p)
    n_other = int(Fo.shape[0])
    if fo == 'copy': del Fo
    info = dict(nS=int(nS), nU=int(nU), excess=int(nU - a_expect), nnzT=int(T.nnz), rows_other=n_other,
                order=cov.get('order'), cover_stats=cov.get('stats'), ublock=int(ublock), nblocks=int(nblocks), attempts=[],
                lean=dict(fo=fo, xblock=xblock, data_dtype=str(E.data.dtype)))
    m = nU + extra
    K = None
    lib = HY.lib(); _ptr = HY._ptr
    for attempt in range(retries):
        ta = time.time(); t_solve = 0.0; t_schur = 0.0
        G = np.zeros((m, nU), dtype=np.uint32)
        pseed = np.uint64((seed + 7919 * attempt + p % 1000) % (1 << 63))
        for b0 in range(0, nU, ublock):
            b1 = min(nU, b0 + ublock); blk = b1 - b0
            ts = time.time()
            if xblock == 'lean':
                Bb = TUc[:, b0:b1].toarray()
                Bb %= p                                   # int32 (p < 2^31 fits int32; entries |v| < 2^31)
                Bb = np.ascontiguousarray(Bb.astype(np.uint32))
            else:
                Bb = np.ascontiguousarray((TUc[:, b0:b1].toarray().astype(np.int64) % p).astype(np.uint32))
            HY.trisolve(T, dinv, Bb, p)
            t_solve += time.time() - ts; ts = time.time()
            colUb = np.full(nc, -1, dtype=np.int32); colUb[U] = -2; colUb[U[b0:b1]] = np.arange(blk, dtype=np.int32)
            Gb = np.zeros((m, blk), dtype=np.uint32)
            rc = lib.schur_project(n_other, _ptr(indptr), _ptr(indices), _ptr(data), _ptr(colS), _ptr(colUb),
                                   _ptr(Bb), blk, m, _ptr(Gb), p, pseed, nproj)
            assert rc == 0, ("schur_project", rc)
            G[:, b0:b1] = Gb
            del Bb, Gb, colUb
            t_schur += time.time() - ts
        t3 = time.time()
        yU = HY.nullspace_mod_p(G.astype(np.int64), p)
        nul = yU.shape[0]
        del G
        t4 = time.time()
        Kc = np.zeros((nc, nul), dtype=np.uint32)
        ok = True
        for v0 in range(0, nul, vblock):
            v1 = min(nul, v0 + vblock)
            yUt = np.ascontiguousarray(yU[v0:v1].T.astype(np.uint32))
            w = HY.spmm_mod(TU, yUt, p)
            w = np.ascontiguousarray(((p - w.astype(np.int64)) % p).astype(np.uint32))
            yS = HY.trisolve(T, dinv, w, p)
            Kc[S, v0:v1] = yS; Kc[U, v0:v1] = yUt
            if not HY.check_kernel_mat(E, Kc[:, v0:v1].astype(np.int64), p): ok = False
        t5 = time.time()
        rk = HY.rank_tall(Kc, p) if nul else 0
        info['attempts'].append(dict(attempt=attempt, m=int(m), nproj=int(nproj), projected_nullity=int(nul), verified=bool(ok),
                                     rank=int(rk), secs=dict(split=round(t1 - t0, 1), trisolve=round(t_solve, 1), schur=round(t_schur, 1),
                                                             nullspace=round(t4 - t3, 1), lift_verify=round(t5 - t4, 1), rank=round(time.time() - t5, 1)),
                                     hwm_gb=round(_rss_gb(), 3)))
        if verbose:
            log(f"    hybrid-lean{tag} p={p} attempt {attempt}: |S|={nS} |U|={nU} (a={a_expect}, excess {nU - a_expect}) m={m} blocks {nblocks}x{ublock} "
                f"projected nullity {nul}, verified={ok}, rank {rk} [split {t1-t0:.1f}s trisolve {t_solve:.1f}s schur {t_schur:.1f}s "
                f"null {t4-t3:.1f}s lift {t5-t4:.1f}s rank {time.time()-t5:.1f}s; HWM {_rss_gb():.2f} GB]")
        if ok and nul == a_expect and rk == a_expect:
            K = Kc; break
        if nul < a_expect:
            raise RuntimeError(("hybrid: projected nullity below a -- impossible if a is right", nul, a_expect))
        del Kc
        m += nU + extra; nproj += 4
    if K is None:
        raise RuntimeError(("hybrid: projection retries exhausted", tag, p, info))
    info['secs'] = round(time.time() - t0, 1)
    return K, info
