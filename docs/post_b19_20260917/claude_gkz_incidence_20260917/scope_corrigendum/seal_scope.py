"""Read-only hashing/sealing for the scope corrigendum: confirm the sealed parent packet is byte-identical
to its own MANIFEST.json, hash the inputs actually used, hash the outputs here. No computation."""
import hashlib, json, time
from pathlib import Path, PurePosixPath
root = Path('C:/users/swami/projects/gct-gpt')
parent = root / 'work/claude_gkz_incidence_20260917'
here = Path(__file__).resolve().parent
def h(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
pm = json.loads((parent / 'MANIFEST.json').read_text())
parent_check = {p: (h(parent / p) == v) for p, v in pm['outputs_sha256'].items()}
parent_files_now = sorted(PurePosixPath(p.relative_to(parent)).as_posix() for p in parent.rglob('*')
                          if p.is_file() and not PurePosixPath(p.relative_to(parent)).as_posix().startswith('scope_corrigendum/'))
unlisted = [p for p in parent_files_now if p not in pm['outputs_sha256'] and p != 'MANIFEST.json']
inputs = [
 'work/claude_gkz_incidence_20260917/REPORT.md',
 'work/claude_gkz_incidence_20260917/MANIFEST.json',
 'work/claude_gkz_incidence_20260917/pilots/p1_ambient_macaulay.json',
 'work/claude_gkz_incidence_20260917/pilots/p2_quinary_macaulay.json',
 'work/claude_gkz_incidence_20260917/pilots/p3_koszul2_exact.json',
 'work/astra_gkz_degenerations_20260917/REPORT.md',
 'work/astra_gkz_degenerations_20260917/MANIFEST.json',
 'work/claude_image_ceiling_20260916/REPORT.md',
 'work/batch15_workers/B15-01/docs/equation_census.md',
 'work/batch15_workers/B15-01/docs/excess_singularity.md',
]
inputs_orig = ['work/docs/onset_conjecture.md', 'work/docs/paper1_delta0_patch.md']
orig = Path('C:/users/swami/projects/gct')
outputs = sorted(PurePosixPath(p.relative_to(here)).as_posix() for p in here.rglob('*') if p.is_file() and p.name != 'MANIFEST.json')
man = {
 'session': 'claude_gkz_incidence_20260917/scope_corrigendum',
 'created_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
 'kind': 'proof-and-wording audit; no numerical pilot; no computation; read-only hashing only',
 'parent_packet_byte_identical_to_its_manifest': all(parent_check.values()),
 'parent_packet_file_checks': parent_check,
 'parent_files_unlisted_in_parent_manifest': unlisted,
 'parent_manifest_sha256': h(parent / 'MANIFEST.json'),
 'inputs_sha256_gct_gpt': {p: h(root / p) for p in inputs},
 'inputs_sha256_gct_original': {p: h(orig / p) for p in inputs_orig},
 'outputs_sha256': {p: h(here / p) for p in outputs},
 'numerical_certificates_changed': False,
 'theorems_changed': False,
 'note': 'Theorems A and B and the P1-P3 certificates are unchanged; consequences narrowed to the rank-threshold ideals J_k; whole-complex, exhaustiveness, monotonicity and delta_0 claims withdrawn (CORRIGENDUM.md). No theorem was independently replayed here; hashes confirm file identity only.',
}
(here / 'MANIFEST.json').write_text(json.dumps(man, indent=1) + '\n')
print('parent byte-identical:', man['parent_packet_byte_identical_to_its_manifest'], '; unlisted:', unlisted)
print(len(outputs), 'outputs hashed')
