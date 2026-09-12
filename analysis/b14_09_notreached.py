#!/usr/bin/env python3
"""
B14-09 -- the cells that were attempted and not decided, with the bound each hit
and the stage it reached.

`A negative characterised over a stated, priced region is a deliverable; an
unstated gap is not.`  A cell that ran out of address space after building is a
different fact from one that was never started, and both are different from a
drop.  This reads the lane logs and says which is which, per attempt.

usage: python3 analysis/b14_09_notreached.py [--out results/b14_09/notreached.json]
"""
import sys, os, re, json, glob
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))

START = re.compile(r"^=== lane (\S+) starting rank (\d+) at (\S+) ===")
EXIT = re.compile(r"^=== lane (\S+) rank (\d+) exit (\d+) ===")
BUILT = re.compile(r"^  built \((.*?)\) d10: N_S=(\d+) \|Stab\|=(\d+) n_chi=(\d+) rows=(\d+) nnz=(\d+) \((\d+)s")
PRIME = re.compile(r"^  per6-lean \((.*?)\) d10 p=(\d+): a=(\d+) n_chi=(\d+) mult=(\d+) units=(-?\d+)")
MEMERR = re.compile(r"numpy\._core\._exceptions\._ArrayMemoryError: Unable to allocate ([\d.]+ \w+)")

EXIT_MEANING = {
    0: "decided and banked",
    1: "address-space bound (`ulimit -v`) reached — NOT REACHED at that bound",
    124: "wall-clock bound (`timeout`) reached — NOT REACHED at that bound",
    137: "ended by the cgroup out-of-memory limit while two lanes ran concurrently — NOT REACHED",
    143: "ended by this session, by recorded pid, to restart the lane with a different bound",
}


def main():
    sz = {c['rank']: c for c in json.load(open(os.path.join(ROOT, 'results/b14_09/sizing.json')))['cells']}
    banked = set()
    for fn in glob.glob(os.path.join(ROOT, 'results/b14_09/per6_d10_lane*.jsonl')):
        for line in open(fn):
            if line.strip():
                banked.add(json.loads(line)['rank'])
    attempts = []
    for fn in sorted(glob.glob(os.path.join(ROOT, 'results/logs/b14_09_lane*.log'))):
        cur = None
        for line in open(fn):
            m = START.match(line)
            if m:
                cur = dict(lane=m.group(1), rank=int(m.group(2)), started=m.group(3),
                           log=os.path.relpath(fn, ROOT), built=None, primes_done=[], mem_error=None)
                continue
            if cur is None:
                continue
            m = BUILT.match(line)
            if m:
                cur['built'] = dict(N_S=int(m.group(2)), stab=int(m.group(3)), n_chi=int(m.group(4)),
                                    nrows=int(m.group(5)), nnz=int(m.group(6)), build_secs=int(m.group(7)))
                continue
            m = PRIME.match(line)
            if m:
                cur['primes_done'].append(dict(p=int(m.group(2)), a=int(m.group(3)),
                                               mult=int(m.group(5)), units=int(m.group(6))))
                continue
            m = MEMERR.search(line)
            if m:
                cur['mem_error'] = m.group(1)
                continue
            m = EXIT.match(line)
            if m and int(m.group(2)) == cur['rank']:
                cur['exit'] = int(m.group(3))
                cur['meaning'] = EXIT_MEANING.get(cur['exit'], f"exit {cur['exit']}")
                cur['reached'] = ('decided' if cur['exit'] == 0 else
                                  'built, stopped in the kernel/evaluation phase' if cur['built'] else
                                  'stopped during the build')
                attempts.append(cur); cur = None
    notreached = []
    for rk, c in sorted(sz.items()):
        if rk in banked:
            continue
        at = [a for a in attempts if a['rank'] == rk]
        notreached.append(dict(
            rank=rk, mu=c['mu'], a=c['a'], N_S=c['N_S'], stab=c['stab'], n_chi=c['n_chi'],
            needs_matmul_mod_wide=c['needs_matmul_mod_wide'],
            pred_build_secs=c['pred_build_secs'], pred_decide_secs=c['pred_decide_secs'],
            pred_peak_gb=c['pred_peak_gb'],
            attempts=[dict(lane=a['lane'], exit=a['exit'], meaning=a['meaning'], reached=a['reached'],
                           built=a['built'], primes_done=a['primes_done'], mem_error=a['mem_error'])
                      for a in at],
            status=('never started in this session' if not at else
                    'attempted and NOT REACHED — see attempts')))
    doc = dict(session='B14-09', banked=sorted(banked), banked_count=len(banked),
               not_reached_count=len(notreached),
               attempted_not_reached=sum(1 for n in notreached if n['attempts']),
               never_started=sum(1 for n in notreached if not n['attempts']),
               partial_prime_evidence=[dict(rank=n['rank'], mu=n['mu'],
                                            primes=[p for a in n['attempts'] for p in a['primes_done']])
                                       for n in notreached
                                       if any(a['primes_done'] for a in n['attempts'])],
               cells=notreached)
    dest = os.path.join(ROOT, sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv
                        else 'results/b14_09/notreached.json')
    json.dump(doc, open(dest, 'w'), indent=1)
    print(f"decided {doc['banked_count']}, not reached {doc['not_reached_count']} "
          f"({doc['attempted_not_reached']} attempted, {doc['never_started']} never started)")
    for n in doc['partial_prime_evidence']:
        print(f"  partial evidence at rank {n['rank']} {tuple(n['mu'])}: {n['primes']}")
    print(f"-> {os.path.relpath(dest, ROOT)}")


if __name__ == '__main__':
    main()
