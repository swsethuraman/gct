#!/usr/bin/env python3
"""Batch-14 intake gate: run this on every worker bundle before merging.

    python3 tools/integrate/intake_b14.py <bundle> [--slot NN]

Checks, in order, stopping at the first that cannot be evaluated:
  1  the bundle verifies and requires exactly the dispatch base
  2  it carries exactly one branch ref, named for a batch-14 slot
  3  every commit trailer is Co-Authored-By only -- no session-link line
  4  no file in the delivered tree exceeds 5 MB
  5  no single-writer file is touched
  6  a pre-registration exists and lands BEFORE the first non-prereg commit
  7  a report exists for the slot
  8  the house wording list is clean in every added .md
  9  no claude.ai URL anywhere in the delivered tree

Exit 0 only if every check passes.  Every failure prints the slot, the check and
what to do about it.  This tool is itself subject to check_must_be_able_to_fail:
run --selftest to see each check rejected by a constructed bad input.
"""
import argparse, os, re, subprocess, sys, tempfile

BASE_TAG = 'batch14-base'
SINGLE_WRITER = ('paper/det3-conductor.tex', 'paper/det4-onset.tex',
                 'PROJECT_NOTES.md', 'docs/boundary_deficit.html')
BANNED = ['kill', 'pkill', 'hunt', 'brutal', 'attack', 'exploit',
          'proxy', 'bypass', 'circumvent', 'STOP-EVERYTHING']
MAXBYTES = 5 * 1024 * 1024


def git(*a, repo=None, check=True):
    cmd = ['git'] + (['-C', repo] if repo else []) + list(a)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if check and r.returncode:
        raise RuntimeError(f"{' '.join(cmd)}\n  exit {r.returncode}: {r.stderr.strip()}")
    return r.stdout


def check(repo, bundle, slot=None):
    fails, notes = [], []
    base = git('log', '-1', '--format=%H', BASE_TAG, repo=repo).strip()

    # 1  bundle verifies, requires the dispatch base.
    # NOTE: `git bundle verify` writes its human-readable report to STDERR, not
    # stdout.  An earlier version of this tool read stdout only, so every bundle
    # looked unverifiable and every later check rejected everything -- five of six
    # selftest cases "passed" for the wrong reason.  Only the positive control
    # found it.  Read both streams.
    r = subprocess.run(['git', '-C', repo, 'bundle', 'verify', bundle],
                       capture_output=True, text=True)
    out = r.stdout + r.stderr
    if r.returncode or 'is okay' not in out:
        return ['1  bundle does not verify -- ask for a fresh one'], notes
    req = re.findall(r'^([0-9a-f]{40})\s*$', out, re.M)
    if base not in req:
        fails.append(f'1  bundle requires {req or "nothing"}, not the dispatch base {base[:8]}'
                     f' -- the session used the wrong base; do NOT relabel, ask it to re-cut')

    # 2  exactly one delivered ref.
    # A bundle cut as `batch14-base..HEAD` -- which is what the packets and the
    # board's delivery rule told sessions to run, and what batch 13's packets said
    # before them -- stores the ref as `HEAD`, not `refs/heads/<branch>`.  That is
    # a defect in the brief, not in the delivery: the objects are all there and
    # `HEAD:refs/...` fetches them.  Accept it, name it, and take the slot from
    # --slot or the bundle filename.
    heads = [l.split() for l in git('bundle', 'list-heads', bundle, repo=repo).splitlines()]
    branches = [(h, r) for h, r in heads if r.startswith('refs/heads/')]
    headonly = [(h, r) for h, r in heads if r == 'HEAD']
    if len(branches) > 1:
        fails.append(f'2  bundle carries {len(branches)} branch refs, want exactly 1: '
                     f'{[r for _, r in branches]}')
        return fails, notes
    if branches:
        tip, ref = branches[0]
        name = ref.rsplit('/', 1)[-1]
    elif headonly:
        tip, ref = headonly[0]
        name = slot or os.path.basename(bundle)
        notes.append('2  bundle carries HEAD rather than a named branch -- the brief '
                     'said `batch14-base..HEAD`, which does that. Not the session\'s '
                     'fault and not a rejection; slot taken from the filename.')
    else:
        fails.append('2  bundle carries no usable ref')
        return fails, notes
    m = re.search(r'b14[-_]?(\d{2})', name, re.I)
    if m:
        nn = m.group(1)
    elif slot:
        nn = slot.zfill(2)
        notes.append(f'2  slot {nn} taken from --slot; the ref name did not carry it')
    else:
        fails.append(f'2  {name!r} does not name a batch-14 slot -- pass --slot NN')
        return fails, notes
    if slot and m and m.group(1) != slot:
        fails.append(f'2  branch says slot {m.group(1)}, --slot says {slot}')

    git('fetch', bundle, f'{ref}:refs/b14intake/{nn}', repo=repo)
    rng = f'{base}..refs/b14intake/{nn}'
    commits = git('log', '--format=%H', rng, repo=repo).split()
    if not commits:
        fails.append('2  bundle adds no commits over the base')
        return fails, notes
    notes.append(f'slot {nn}: {len(commits)} commits, tip {tip[:8]}')

    # 3  trailers
    for c in commits:
        body = git('log', '-1', '--format=%B', c, repo=repo)
        if re.search(r'claude\.ai|Claude-Session', body, re.I):
            fails.append(f'3  {c[:8]} carries a session-link trailer or URL')
        if 'Co-Authored-By:' not in body:
            notes.append(f'3  {c[:8]} has no Co-Authored-By (permitted, noted)')

    # 4/5/9  the delivered tree
    files = git('diff', '--name-only', rng, repo=repo).split('\n')
    files = [f for f in files if f]
    for f in files:
        if f in SINGLE_WRITER:
            fails.append(f'5  touches single-writer file {f}')
        blob = git('rev-parse', f'refs/b14intake/{nn}:{f}', repo=repo, check=False).strip()
        if not blob:
            continue                      # deleted
        size = int(git('cat-file', '-s', blob, repo=repo).strip())
        if size > MAXBYTES:
            fails.append(f'4  {f} is {size/1048576:.1f} MB, over the 5 MB limit')
        content = git('cat-file', '-p', blob, repo=repo, check=False)
        if re.search(r'claude\.ai', content, re.I):
            fails.append(f'9  {f} contains a session-link URL')
        if f.endswith('.md'):
            hits = [w for w in BANNED if re.search(rf'\b{w}\b', content, re.I)]
            if hits:
                fails.append(f'8  {f} uses {hits} -- see docs/brief_wording.md section 2')

    # 6  pre-registration lands first
    prereg = [f for f in files if re.search(rf'PREREG_b14_{nn}', f)]
    if not prereg:
        fails.append(f'6  no results/PREREG_b14_{nn}.md in the delivery')
    else:
        first_pre = git('log', '--format=%H', rng, '--reverse', '--', *prereg,
                        repo=repo).split()
        order = list(reversed(commits))
        if first_pre and order.index(first_pre[0]) != 0:
            fails.append(f'6  pre-registration lands at commit '
                         f'{order.index(first_pre[0])+1} of {len(order)}, not first -- '
                         f'everything before it is exploratory')

    # 7  report
    if not any(re.search(rf'b14_{nn}_report', f) for f in files):
        fails.append(f'7  no docs/b14_{nn}_report.md in the delivery')

    git('update-ref', '-d', f'refs/b14intake/{nn}', repo=repo, check=False)
    return fails, notes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('bundle', nargs='?')
    ap.add_argument('--slot')
    ap.add_argument('--repo', default=os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    ap.add_argument('--selftest', action='store_true')
    a = ap.parse_args()
    if a.selftest:
        return selftest(a.repo)
    if not a.bundle:
        ap.error('give a bundle, or --selftest')
    fails, notes = check(a.repo, os.path.abspath(a.bundle), a.slot)
    for n in notes:
        print('  note  ' + n)
    for f in fails:
        print('  FAIL  ' + f)
    print('INTAKE', 'CLEAN' if not fails else f'{len(fails)} FAILURES')
    return 0 if not fails else 1


def selftest(repo):
    """every check must reject a constructed bad input."""
    import shutil
    base = git('log', '-1', '--format=%H', BASE_TAG, repo=repo).strip()
    tmp = tempfile.mkdtemp(prefix='b14intake')
    wc = os.path.join(tmp, 'wc')
    git('clone', '-q', '--no-local', '-b', 'integration/batch13', repo, wc)
    git('fetch', '-q', repo, f'refs/tags/{BASE_TAG}:refs/tags/{BASE_TAG}', repo=wc)
    results = []

    def build(name, mutate):
        git('checkout', '-q', BASE_TAG, repo=wc, check=False)
        git('checkout', '-q', '-B', name, BASE_TAG, repo=wc)
        mutate(wc)
        b = os.path.join(tmp, name + '.bundle')
        git('bundle', 'create', b, f'{BASE_TAG}..{name}', f'--branches={name}', repo=wc)
        return b

    def commit(repo_, msg, trailer=True):
        git('add', '-A', repo=repo_)
        body = msg + ('\n\nCo-Authored-By: Claude Opus 5 <noreply@anthropic.com>' if trailer else '')
        git('-c', 'user.name=w', '-c', 'user.email=w@x', 'commit', '-q', '-m', body, repo=repo_)

    def good(w):
        open(os.path.join(w, 'results', 'PREREG_b14_01.md'), 'w').write('# prereg\n')
        commit(w, 'prereg')
        os.makedirs(os.path.join(w, 'docs'), exist_ok=True)
        open(os.path.join(w, 'docs', 'b14_01_report.md'), 'w').write('# report\nPROVED nothing.\n')
        commit(w, 'report')

    def no_prereg(w):
        open(os.path.join(w, 'docs', 'b14_01_report.md'), 'w').write('# report\n')
        commit(w, 'report only')

    def prereg_late(w):
        open(os.path.join(w, 'docs', 'b14_01_report.md'), 'w').write('# report\n')
        commit(w, 'measured first')
        open(os.path.join(w, 'results', 'PREREG_b14_01.md'), 'w').write('# prereg\n')
        commit(w, 'prereg after the fact')

    def single_writer(w):
        good(w)
        open(os.path.join(w, 'PROJECT_NOTES.md'), 'a').write('\nworker edit\n')
        commit(w, 'touch a single-writer file')

    def banned_word(w):
        good(w)
        open(os.path.join(w, 'docs', 'b14_01_report.md'), 'a').write('\nkill criteria: none.\n')
        commit(w, 'wording')

    def session_link(w):
        good(w)
        open(os.path.join(w, 'docs', 'b14_01_report.md'), 'a').write('\nsee https://claude.ai/x\n')
        commit(w, 'link')

    def wrong_base(w):
        # the failure Astra warned about: a session that branched from an older
        # commit and cut its bundle there.  Everything inside may be fine.
        git('checkout', '-q', '-B', 'b14-01-wrongbase', f'{BASE_TAG}~1', repo=w)
        open(os.path.join(w, 'results', 'PREREG_b14_01.md'), 'w').write('# prereg\n')
        commit(w, 'prereg')
        open(os.path.join(w, 'docs', 'b14_01_report.md'), 'w').write('# report\n')
        commit(w, 'report')

    def build_wrong(name):
        git('checkout', '-q', BASE_TAG, repo=wc, check=False)
        wrong_base(wc)
        b = os.path.join(tmp, name + '.bundle')
        git('bundle', 'create', b, f'{BASE_TAG}~1..b14-01-wrongbase', repo=wc)
        return b

    b = build_wrong('b14-01-wrongbase')
    fails, _ = check(repo, b, None)
    hit = any(f.startswith('1 ') for f in fails)
    results_pre = [hit]
    print(f"  {'PASS' if hit else 'FAIL'}  {'b14-01-wrongbase':20s} "
          f"expected rejection on check 1, got {len(fails)} failures"
          + (f"  [{fails[0][:70]}]" if fails else ''))

    cases = [('b14-01-good', good, 0), ('b14-01-noprereg', no_prereg, 1),
             ('b14-01-preregL', prereg_late, 1), ('b14-01-singlew', single_writer, 1),
             ('b14-01-wording', banned_word, 1), ('b14-01-link', session_link, 1)]
    results.extend(results_pre)
    for name, fn, want_fail in cases:
        b = build(name, fn)
        fails, _ = check(repo, b, None)
        got = 1 if fails else 0
        ok = got == want_fail
        results.append(ok)
        print(f"  {'PASS' if ok else 'FAIL'}  {name:20s} "
              f"expected {'rejection' if want_fail else 'clean'}, "
              f"got {len(fails)} failures"
              + (f"  [{fails[0][:70]}]" if fails else ''))
    shutil.rmtree(tmp, ignore_errors=True)
    print('SELFTEST', 'PASS' if all(results) else 'FAIL')
    return 0 if all(results) else 1


if __name__ == '__main__':
    sys.exit(main())
