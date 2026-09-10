#!/usr/bin/env python3
"""
B13-10 -- one build in one process, so that VmHWM is that build's peak.

usage: python3 analysis/wk13_b10_run.py --builder old|lean --n N --delta D --lam a,b,c --out DIR --tag TAG
                                        [--triples store|recompute] [--blocks memory|disk] [--chunk C] [--no-save]

Writes DIR/TAG_<builder>[_<knobs>].npz (E as indptr/indices/data, arr as M/col_of/sgn)
and DIR/TAG_<builder>[_<knobs>].json (sizes, seconds per phase, VmHWM after imports and
at the end, dtypes).  The old builder is wk9_s45_build.build_cell exactly as the
s79 drivers call it (wk11_s71_codes installed, BLAS threads 1); the lean builder is
wk13_b10_lean.build_cell_lean.
"""
import sys, os, time, json
for _v in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ.setdefault(_v, '1')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)


def vm(key):
    with open('/proc/self/status') as f:
        for line in f:
            if line.startswith(key): return int(line.split()[1]) / 1048576.0
    return float('nan')


def main():
    args = sys.argv[1:]
    def arg(name, default=None):
        return args[args.index(name) + 1] if name in args else default
    builder = arg('--builder'); n = int(arg('--n')); delta = int(arg('--delta'))
    lam = tuple(int(x) for x in arg('--lam').split(','))
    out = arg('--out'); tag = arg('--tag')
    triples = arg('--triples', 'store'); blocks = arg('--blocks', 'memory'); chunk = int(arg('--chunk', '400000'))
    save = '--no-save' not in args
    t_imp = time.time()
    import numpy as np
    import wk11_s71_codes; wk11_s71_codes.install()
    from wk9_s42_census import a_weyl
    base_hwm = vm('VmHWM'); base_rss = vm('VmRSS')
    rec = dict(builder=builder, n=n, lam=list(lam), delta=delta, tag=tag, hwm_baseline_gb=round(base_hwm, 4), rss_baseline_gb=round(base_rss, 4),
               import_secs=round(time.time() - t_imp, 2), pid=os.getpid(), knobs=None)
    name = f"{tag}_{builder}"
    t0 = time.time()
    if builder == 'old':
        from wk9_s45_build import build_cell
        B = build_cell(lam, delta, n=n, verbose=True)
    elif builder == 'lean':
        from wk13_b10_lean import build_cell_lean
        B = build_cell_lean(lam, delta, n=n, verbose=True, chunk=chunk, triples=triples, blocks=blocks)
        rec['knobs'] = B['knobs']; rec['phases'] = B['phases']; rec['dtypes'] = B['dtypes']
        rec['hwm_mono_gb'] = round(B['hwm_mono_gb'], 4); rec['hwm_orbit_gb'] = round(B['hwm_orbit_gb'], 4)
        name += f"_{triples}_{blocks}_c{chunk}"
    else:
        raise SystemExit("builder?")
    secs = time.time() - t0
    E = B['E']; arr = B['arr']
    rec.update(a=int(a_weyl(lam, delta, n, {})), N_S=int(B['N_S']), stab=int(B['stab']), n_chi=int(B['n_chi']), nrows=int(E.shape[0]), nnz=int(E.nnz),
               nfixed=int(B['nfixed']), NS_delta=int(B['N_S']) * delta,
               secs=dict(total=round(secs, 2), mono=round(B['mono_secs'], 2), orbits=round(B['orbit_secs'], 2), rows=round(B['rows_secs'], 2)),
               hwm_gb=round(vm('VmHWM'), 4), hwm_above_baseline_gb=round(vm('VmHWM') - base_hwm, 4), rss_end_gb=round(vm('VmRSS'), 4),
               E_dtypes=dict(data=str(E.data.dtype), indices=str(E.indices.dtype), indptr=str(E.indptr.dtype)),
               M_dtype=str(arr['M'].dtype), abs_data_max=int(np.abs(E.data.astype(np.int64)).max(initial=0)))
    if save:
        os.makedirs(out, exist_ok=True)
        np.savez(os.path.join(out, name + '.npz'), indptr=E.indptr, indices=E.indices, data=E.data,
                 M=arr['M'], col_of=arr['col_of'], sgn=arr['sgn'], n_chi=np.int64(arr['n_chi']))
        rec['npz'] = name + '.npz'
    with open(os.path.join(out, name + '.json'), 'w') as f:
        json.dump(rec, f)
    print("RUN " + json.dumps({k: rec[k] for k in ('builder', 'lam', 'delta', 'N_S', 'n_chi', 'nrows', 'nnz', 'secs', 'hwm_gb', 'hwm_above_baseline_gb')}), flush=True)


if __name__ == '__main__':
    main()
