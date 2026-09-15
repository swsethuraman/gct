"""Small final receipt audit; does not launch mathematical production or mutate inputs."""
from pathlib import Path
import argparse
import hashlib
import json
import sys

WORK = Path(__file__).resolve().parents[1]
OUT = WORK/'results/b16_12'
READS = {}


def read(path, expected=None):
    path = Path(path).resolve()
    data = path.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if expected is not None:
        assert digest == expected, str(path)
    READS[str(path)] = {'sha256':digest, 'bytes':len(data)}
    return data


def obj(path):
    return json.loads(read(path))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    target = Path(args.output).resolve()
    assert target.is_relative_to(OUT) and not target.exists()
    assert sys.dont_write_bytecode
    read(__file__)
    registry = obj(OUT/'received.json')
    assert [e['slot'] for e in registry['entries']] == ['03','04','05','06','07','08']
    all_intakes = []
    receipts = {}
    for entry in registry['entries']:
        assert entry['status'] == 'PASS_PROOF_REVIEW_AND_BOUNDED_REPLAY'
        ledger = obj(WORK/entry['hash_ledger'])
        read(ledger['manifest_source'], ledger['manifest_sha256'])
        for row in ledger['files']:
            read(row['source'], row['sha256'])
            read(row['snapshot'], row['sha256'])
        for row in ledger['original_inputs']:
            read(row['path'], row['sha256'])
        read(WORK/entry['proof_review'])
        receipts[entry['slot']] = obj(WORK/entry['receipt'])
        if 'proof_receipt' in entry:
            receipts['05_proof'] = obj(WORK/entry['proof_receipt'])
        all_intakes.append({'slot':entry['slot'], 'files':len(ledger['files']),
                            'input_records':len(ledger['original_inputs'])})
    integrity_files = ['replay_03_integrity.json', 'replay_07_integrity.json',
        'replay_04_verify_integrity.json', 'replay_05_replay_integrity.json',
        'replay_05_proof_integrity.json', 'replay_06_verify_integrity.json',
        'replay_08_receive_integrity.json']
    runtime_records = 0
    for name in integrity_files:
        rec = obj(OUT/name)
        assert rec['status'] == 'PASS'
        for row in rec['runtime_modules']:
            read(row['path'], row['sha256'])
            runtime_records += 1
        for row in rec.get('path_only_adaptations', []):
            read(row['path'], row['adapted_sha256'])
    own = obj(OUT/'receiver_complete.json')
    assert own['status'] == 'PASS_PROOF_CONTROLS_AND_INHERITED_ARITHMETIC'
    assert own['received_03_through_08'] == registry
    for path, rec in own['input_hashes'].items():
        read(path, rec['sha256'])
    cells = receipts['04']['declared_cells']
    assert [c['ambient_inherited'] for c in cells] == [189,294,294,429]
    assert [c['determinant_ideal_exact'] for c in cells] == [1,4,4,11]
    assert [c['gap_upper'] for c in cells] == [-30,-72,-72,-130]
    for cell in cells:
        assert cell['gap_upper'] == cell['padding_source_upper_inherited']-cell['determinant_coordinate_exact']
        assert cell['positive_witness_impossible_in_this_cell']
    assert receipts['04']['exact_coefficient_comparisons'] == 256
    assert receipts['05']['status'] == 'PASS'
    assert receipts['05_proof']['ambient_nonzero']['E3'] == 348671260102848768
    for family in ('SPLIT','PAD'):
        assert receipts['05_proof']['five_space_restriction'][family]['exact_restriction_rank'] == 4
    assert receipts['06']['status'] == 'EXACT_SELECTED_POLYNOMIAL_IMAGES_WITH_GLOBAL_PROOF'
    assert receipts['08']['status'] == 'PASS'
    assert receipts['08']['blocks_rebuilt'] == 165
    assert receipts['08']['columns_proved_independent'] == 630
    # Every actual read is bound, then rechecked at the end.
    for path, rec in READS.items():
        assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == rec['sha256'], path
    result = {'status':'PASS_ALL_ASSIGNED_SCOPED_REVIEWS_AND_FINAL_INTEGRITY',
        'intakes':all_intakes, 'runtime_module_records_rechecked':runtime_records,
        'finite_cells':cells, 'pending_assigned_deliveries':[], 'positive_gap_claimed':False,
        'fresh_vs_inherited':'Mathematical boundaries are in the four proof documents; numerical conclusions retain their inherited premises.',
        'notification':'UNSENT_AFTER_AUTO_REVIEW_REJECTION', 'input_hashes':READS}
    target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'status':result['status'],'distinct_input_files':len(READS),
                      'runtime_records':runtime_records,'gap_upper':[-30,-72,-72,-130]}))


if __name__ == '__main__':
    main()
