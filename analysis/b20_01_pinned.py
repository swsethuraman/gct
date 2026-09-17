"""B20-01 pinned-input loader (read-only git; G9/G10/G11).

Every input is fetched as committed bytes with `git show <commit>:<path>`, hashed, and checked against
the pin recorded here.  Copies of the two code inputs are materialised under results/b20_01/pinned/
(the runner with its carrier path patched to the pinned carrier copy) so that no sealed working tree
is imported from.  PINS: full sha256 of the committed bytes."""
import hashlib, subprocess, sys, types
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]           # worktree B15-01
PIN = ROOT / 'results/b20_01/pinned'
ARCH = '82633a60893236fab4fbc317df416e1b8a349005'
B1502 = '75ddb900a0b47b911c53f941885bac73b358eacb'
D = 'docs/post_b19_20260917/'
SV = D + 'claude_source_vectors_20260917/'
PINS = {
 'paired_runner.py': (ARCH, D + 'descent_followup_claude_20260916/pilots/paired_runner.py', '33c81c967e71270ab31f05c360bfd7ba1a18a3f79aca8172769be3b5a6ff3260'),
 'b18_02_carrier.py': (B1502, 'analysis/b18_02_carrier.py', '8670040e2a980026563d1a265f8d32e5749a47f61a0c100e82be9ffa0c75a154'),
 'p6_basis.json': (ARCH, D + 'descent_followup_claude_20260916/pilots/p6_basis.json', 'aaee6ec05ecf9ea2cc22e722b114576f3661f30f7bb36c49e79984c1c87067e7'),
 'p7_arc_S0.json': (ARCH, D + 'descent_followup_claude_20260916/pilots/p7_arc_S0.json', None),
 'n02_definition.json': (ARCH, SV + 'routeA_signfilter_20260917/certificates/n02_definition.json', None),
 'candidates_selected.json': (ARCH, SV + 'routeA_signfilter_20260917/certificates/candidates_selected.json', None),
 's1_screen_arc.py': (ARCH, SV + 'routeA_signfilter_20260917/pilots/s1_screen_arc.py', None),
 's2_certify_n02_and_new.py': (ARCH, SV + 'routeA_signfilter_20260917/pilots/s2_certify_n02_and_new.py', None),
 's3_full_forbidden_rows.py': (ARCH, SV + 'routeA_signfilter_20260917/pilots/s3_full_forbidden_rows.py', None),
 'f1_new_point_minor.py': (ARCH, SV + 'final_arc_diagnostic/code/f1_new_point_minor.py', None),
 'f1_new_point_minor.json': (ARCH, SV + 'final_arc_diagnostic/results/f1_new_point_minor.json', None),
 's3_full_forbidden_rows.json': (ARCH, SV + 'routeA_signfilter_20260917/results/s3_full_forbidden_rows.json', None),
}
PREFIX = {'p7_arc_S0.json': 'b84168a2', 'n02_definition.json': 'ffeead803eba', 'candidates_selected.json': 'a69c6313f2d736b2',
          's1_screen_arc.py': '81d3ee7a8a66aea2', 's2_certify_n02_and_new.py': 'ac6c3a233924abf8', 's3_full_forbidden_rows.py': 'b03dab8226e9a6e0',
          'f1_new_point_minor.py': 'b531cfb1fdb95b14'}
def sha(b): return hashlib.sha256(b).hexdigest()
def fetch(name):
    commit, path, full = PINS[name]
    b = subprocess.run(['git', 'show', '%s:%s' % (commit, path)], cwd=ROOT, capture_output=True, check=True).stdout
    h = sha(b)
    if full is not None: assert h == full, (name, h)
    if name in PREFIX: assert h.startswith(PREFIX[name]), (name, h)
    return b, dict(commit=commit, path=path, sha256=h, bytes=len(b))
def load_runner():
    """Returns (pr module, pin record dict)."""
    PIN.mkdir(parents=True, exist_ok=True)
    cb, crec = fetch('b18_02_carrier.py'); rb, rrec = fetch('paired_runner.py')
    cpath = PIN / 'b18_02_carrier.py'; cpath.write_bytes(cb)
    src = rb.decode()
    old = "SRC = HERE.parents[2] / 'work/batch15_workers/B15-02/analysis/b18_02_carrier.py'"
    assert old in src
    src = src.replace(old, "SRC = HERE / 'b18_02_carrier.py'")
    rpath = PIN / 'paired_runner.py'; rpath.write_text(src, newline='\n')
    sys.dont_write_bytecode = True
    if str(PIN) not in sys.path: sys.path.insert(0, str(PIN))
    import paired_runner as pr
    assert sha(pr.SRC.read_bytes()) == crec['sha256']
    rec = dict(carrier=crec, runner_original=rrec, runner_patched_sha256=sha(rpath.read_bytes()),
               patch='carrier path line replaced by SRC = HERE / b18_02_carrier.py (one line; no other byte changed)')
    return pr, rec
