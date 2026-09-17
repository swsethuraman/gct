"""B20-02 seal: hash every output of this slot and re-hash every sibling-worktree file read (G11),
print the totals (G16), and write results/b20_02/MANIFEST.json. Read-only apart from the manifest."""
import hashlib, json, os, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)

def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()

outputs = [
    'docs/b20_02_report.md',
    'analysis/b20_02_koszul5.py', 'analysis/b20_02_price16.py', 'analysis/b20_02_p3_driver.py', 'analysis/b20_02_seal.py',
    'results/b20_02/p3_koszul5_k3_12.json', 'results/b20_02/p3_price16_blocks.json',
    'results/b20_02/p1r_console.log', 'results/b20_02/p3_console.log',
    'results/b20_02/unwrapped/smoke_k3_7.json',
    'results/b20_02/unwrapped/bisect_A_k9_detP2_limit400k.json', 'results/b20_02/unwrapped/bisect_B_k9_detP2_limit800k.json',
    'results/logs/b20_02_p1_koszul5_k3_10.pid', 'results/logs/b20_02_p1_koszul5_k3_10_resources.json',
    'results/logs/b20_02_p1r_koszul5_k3_12.pid', 'results/logs/b20_02_p1r_koszul5_k3_12_resources.json',
    'results/logs/b20_02_p3_price16_and_koszul5_k3_12.pid', 'results/logs/b20_02_p3_price16_and_koszul5_k3_12_resources.json',
]
inputs_copied = {
    'results/b20_02/inputs/p2_quinary_macaulay.json': '05272bfc0b0be15c4c870637ab3f371d79be53bf044f9fbe4c15a704c40c193e',
    'results/b20_02/inputs/p3_koszul2_exact.json': 'a83162c2941e1305440cce11ebccdb181408d7471c7dd113ec4be3aeb0f0f151',
}
sibling_reads = {  # hashed at first read (values recorded in the report §1.1); re-hashed here
    '../B15-10/docs/b20_10_review.md': '021be68f748e8f05e0c8efcd7c50bd58bede1a34b420c2632f3006612fb3a5fa',
    '../B15-10/docs/b18_10_review.md': 'dc1cc655a95bcadb8e739f00ef89fa090722d3e0f9dc92b85f0c7b13118f8a91',
    '../B15-12/docs/b20_12_ledger.md': '585ee994a8667e2d5bdceb6116f6fa53a9d79d2c236ba0d767f3fa33da8a835c',
    'analysis/b15_bound.py': 'ca001081f49e0048812b871a31e3be85435b210b3a538170a9f006408a41f854',
}
git_pins = {  # immutable objects, listed for completeness; read with `git show 82633a60:<path>`
    'docs/post_b19_20260917/claude_gkz_incidence_20260917/scope_corrigendum/CORRIGENDUM.md': None,
    'docs/post_b19_20260917/claude_gkz_incidence_20260917/scope_corrigendum/REVISED_VERDICT.md': None,
    'docs/post_b19_20260917/claude_gkz_incidence_20260917/scope_corrigendum/CLAIM_SCOPE_TABLE.md': None,
    'docs/post_b19_20260917/claude_gkz_incidence_20260917/REPORT.md': None,
    'docs/post_b19_20260917/claude_gkz_incidence_20260917/MANIFEST.json': None,
    'docs/post_b19_20260917/claude_gkz_incidence_20260917/pilots/p2_quinary_macaulay.py': None,
    'docs/post_b19_20260917/claude_gkz_incidence_20260917/pilots/p2_quinary_macaulay.json': None,
    'docs/post_b19_20260917/claude_gkz_incidence_20260917/pilots/p3_koszul2_exact.py': None,
    'docs/post_b19_20260917/claude_gkz_incidence_20260917/pilots/p3_koszul2_exact.json': None,
    'docs/post_b19_20260917/astra_gkz_degenerations_20260917/REPORT.md': None,
}
COMMIT = '82633a60893236fab4fbc317df416e1b8a349005'
for path in git_pins:
    data = subprocess.run(['git', 'show', f'{COMMIT}:{path}'], capture_output=True, check=True).stdout
    git_pins[path] = hashlib.sha256(data).hexdigest()

man = {'slot': 'B20-02', 'created_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
       'worktree': 'work/batch15_workers/B15-02', 'branch': 'b15-02-a1-probes',
       'head_at_start': '75ddb900a0b47b911c53f941885bac73b358eacb', 'tree_at_start': 'c4d8aac88fbd19fd20a63d422d284fd57a99996a',
       'head_now': subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip(),
       'interpreter': '.venv/python.exe (Python 3.12.10, numpy 2.4.6, sympy 1.14.0, python-flint 0.9.0)',
       'wrapper': 'analysis/b15_bound.py --seconds 60 --memory-mb 512 (Job Object), PYTHONDONTWRITEBYTECODE=1',
       'outputs_sha256': {}, 'inputs_copied_sha256': {}, 'sibling_reads_rehash': {}, 'git_pins_sha256_at_82633a60': git_pins,
       'literature': {'dimca_1210.1795v4.pdf': {'sha256': '20b96f5830291574137000073237b9081e134e45d52c89d9981996e5a83c9c05',
                      'kept_in': 'session scratchpad (not in the delivery tree)', 'label': 'PRIMARY at statement level (Remark 3.5, 3.6)'}}}
n_out = 0
for p in outputs:
    if Path(p).exists():
        man['outputs_sha256'][p] = sha(p); n_out += 1
    else:
        man['outputs_sha256'][p] = 'MISSING'
n_in_ok = 0
for p, expect in inputs_copied.items():
    h = sha(p); man['inputs_copied_sha256'][p] = {'sha256': h, 'expected': expect, 'match': h == expect}; n_in_ok += (h == expect)
n_sib_ok = 0
for p, expect in sibling_reads.items():
    h = sha(p); man['sibling_reads_rehash'][p] = {'sha256_now': h, 'sha256_at_read': expect, 'unchanged': h == expect}; n_sib_ok += (h == expect)
man['counts'] = {'outputs_hashed': n_out, 'outputs_listed': len(outputs), 'inputs_copied_match': [n_in_ok, len(inputs_copied)],
                 'sibling_reads_unchanged': [n_sib_ok, len(sibling_reads)], 'git_pins_hashed': len(git_pins)}
Path('results/b20_02/MANIFEST.json').write_text(json.dumps(man, indent=1) + '\n')
print(json.dumps(man['counts']))
print('outputs hashed', n_out, '/', len(outputs))
print('inputs copied matching', n_in_ok, '/', len(inputs_copied))
print('sibling reads unchanged', n_sib_ok, '/', len(sibling_reads))
for p, h in man['outputs_sha256'].items():
    print(h[:16], p)
print('MANIFEST sha256', sha('results/b20_02/MANIFEST.json'))
