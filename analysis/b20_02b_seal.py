"""B20-02b seal: hash every output, verify the copied inputs against their pins, re-hash the two B20-02 files read
(G11), print every count written (G16), and write results/b20_02b/MANIFEST.json. Read-only otherwise."""
import hashlib, json, os, subprocess, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)

def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()

outputs = ['docs/b20_02b_report.md', 'analysis/b20_02b_d8_blockwise.py', 'analysis/b20_02b_seal.py',
           'results/b20_02b/p1_d8_blockwise.json', 'results/b20_02b/p1_console.log',
           'results/logs/b20_02b_p1_d8_blockwise.pid', 'results/logs/b20_02b_p1_d8_blockwise_resources.json']
inputs_copied = {'results/b20_02b/inputs/p3_price16_blocks.json': '54838ca647397a331f6d79586a2d0b4b49d39ed6ea3958d15ab30c14b6ee254a',
                 'results/b20_02b/inputs/p3_koszul2_exact.json': 'a83162c2941e1305440cce11ebccdb181408d7471c7dd113ec4be3aeb0f0f151'}
b20_02_reads = {'results/b20_02/MANIFEST.json': 'a3798319a1ac18b494704b172e9f6a5709557523792657b1f783cecd6ffc499b',
                'results/b20_02/p3_price16_blocks.json': '54838ca647397a331f6d79586a2d0b4b49d39ed6ea3958d15ab30c14b6ee254a',
                'docs/b20_02_report.md': '15ef389b5eb84074e77f2bd88c2dd5e98b14399a394d150b05f2b1b3f2baeda2'}
man = {'slot': 'B20-02b', 'created_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
       'worktree': 'work/batch15_workers/B15-02', 'branch': 'b15-02-a1-probes',
       'head': subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip(),
       'prereg_hashes_before_launch': {'docs/b20_02b_report.md': 'c5c6511b78a081541c75f69c51b817eb13ec96c2bae2a8011b29a520b75e125a',
                                       'analysis/b20_02b_d8_blockwise.py': 'ae03c0d17115ef1f8555966489fc62c2bd0fe5cc2933b9765cbf126d1c44913c'},
       'outputs_sha256': {}, 'inputs_copied_sha256': {}, 'b20_02_reads_rehash': {}}
n_out = 0
for p in outputs:
    if Path(p).exists():
        man['outputs_sha256'][p] = sha(p); n_out += 1
    else:
        man['outputs_sha256'][p] = 'MISSING'
n_in = 0
for p, e in inputs_copied.items():
    h = sha(p); man['inputs_copied_sha256'][p] = {'sha256': h, 'expected': e, 'match': h == e}; n_in += (h == e)
n_rd = 0
for p, e in b20_02_reads.items():
    h = sha(p); man['b20_02_reads_rehash'][p] = {'sha256_now': h, 'sha256_at_read': e, 'unchanged': h == e}; n_rd += (h == e)
script_unchanged = sha('analysis/b20_02b_d8_blockwise.py') == man['prereg_hashes_before_launch']['analysis/b20_02b_d8_blockwise.py']
man['counts'] = {'outputs_hashed': [n_out, len(outputs)], 'inputs_copied_match': [n_in, len(inputs_copied)],
                 'b20_02_reads_unchanged': [n_rd, len(b20_02_reads)], 'pilot_script_unchanged_since_prereg': script_unchanged}
Path('results/b20_02b/MANIFEST.json').write_text(json.dumps(man, indent=1) + '\n')
print(json.dumps(man['counts']))
print('outputs hashed', n_out, '/', len(outputs))
print('inputs copied matching', n_in, '/', len(inputs_copied))
print('B20-02 reads unchanged', n_rd, '/', len(b20_02_reads))
print('pilot script unchanged since pre-registration:', script_unchanged)
for p, h in man['outputs_sha256'].items():
    print(h[:16], p)
print('MANIFEST sha256', sha('results/b20_02b/MANIFEST.json'))
