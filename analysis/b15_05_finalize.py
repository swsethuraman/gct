"""Record B15-05 completed numerical work and file provenance. gpt-6-astra."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'results/b15_05'


def write(name, value):
    (OUT/name).write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')


def main():
    runs = {}
    for name in ['resource_control','algorithm_controls','transport_control',
                 'expected_defect','pilot','geometric_replay']:
        file = ROOT/f'results/logs/b15_05_{name}_resources.json'
        record = json.loads(file.read_text())
        if record['exit_code'] != (1 if name=='expected_defect' else 0):
            raise ValueError('unexpected run exit: '+name)
        runs[name] = record
    pilot = json.loads((OUT/'pilot.json').read_text())
    replay = json.loads((OUT/'replay.json').read_text())
    if pilot['det_rank_lb'] != 529 or len(replay['records']) != 4:
        raise ValueError('final numerical summary disagreement')
    heavy = [runs['pilot'],runs['geometric_replay']]
    elapsed = sum(v['wall_seconds'] for v in heavy)
    if elapsed >= 900:
        raise ValueError('shared numerical budget exceeded')
    release = dict(slot='05',released_utc=datetime.now(timezone.utc).isoformat(),
        status='RELEASED',no_further_heavy_work=True,
        reason='Fixed-cap pilot and fresh geometric replay completed; determinant rank 529 at both primes; stop rule reached.',
        jobs=[dict(name='b15_05_'+name,pid=runs[name]['pid'],
            started_utc=runs[name]['started_utc'],exit_code=runs[name]['exit_code'],
            wall_seconds=runs[name]['wall_seconds'],aggregate_peak_bytes=runs[name]['job_memory']['peak_job_memory'])
            for name in ['pilot','geometric_replay']],
        combined_numerical_wall_seconds=elapsed,
        process_exit_check='Fresh Get-Process -Id 31376,32760 returned no processes after both exec sessions reported exit 0; no process was ended manually.')
    if not (OUT/'lease_release.json').exists():
        write('lease_release.json',release)
    decisions = json.loads((OUT/'resource_decisions.json').read_text())
    decisions['events'] = [e for e in decisions['events'] if e['event'] not in
        ['heavy_lease_granted','pilot_complete','replay_complete','lease_released']]
    decisions['events'].extend([
        dict(event='heavy_lease_granted',detail='Integrator explicitly granted 05 after verified release by 04; lease snapshot retained.'),
        dict(event='pilot_complete',wall_seconds=heavy[0]['wall_seconds'],
             aggregate_peak_bytes=heavy[0]['job_memory']['peak_job_memory'],det_rank_lb=529,
             detail='Fixed 600 DET and 560 GEN points per prime; no resampling beyond cap.'),
        dict(event='replay_complete',wall_seconds=heavy[1]['wall_seconds'],
             aggregate_peak_bytes=heavy[1]['job_memory']['peak_job_memory'],
             detail='All four actual minors freshly evaluated with a changed interpolation seed; exit 0. Replay cap reduced to 800 seconds to stay inside the same 900-second window.'),
        dict(event='lease_released',detail='Both heavy processes exited; no extension requested; no further heavy work.')])
    write('resource_decisions.json',decisions)
    write('proposed_exclusions.json',dict(status='RECORDED',proposed_exclusions=[],
        reason='Rank floor 529 is below sufficient threshold 530. The bound D<=1 excludes no positive gap.',
        scope=dict(n=4,ambient_variables=16,restriction_variables=9,stable_variables=8,
                   tail=[21]+[2]*7,from_degree=15,partition='(4d-35,21,2^7)'),
        determinant_coordinate_stable_lb=529,determinant_ideal_stable_ub=4,
        padded_ideal_lb=3,D_ub=1,
        next_sufficient_witness='One further independent stable determinant evaluation direction, giving a nonzero 530x530 minor; alternatively a fourth global padded ideal direction at degree15 that persists by u-multiplication.'))
    write('summary.json',dict(status='REPLAYED_RANK_FLOOR',model='gpt-6-astra',
        primes=[2147483647,2147483629],stable_ambient_dimension=533,
        determinant_coordinate_stable_lb=529,determinant_ideal_stable_ub=4,
        padded_ideal_lb=3,D_ub=1,threshold=530,threshold_met=False,
        finite26=dict(ambient_dimension=531,determinant_coordinate_lb=527,
                      padded_coordinate_ub=528,D_ub=1),
        sampled_kernel=dict(status='CANDIDATE',dimension_per_prime=4,
            basis='533 generic pivot bracket columns; see kernel files',
            global_ideal_membership=False),
        fresh_minor_entries=sum(r['entries_checked'] for r in replay['records']),
        numerical_wall_seconds=elapsed,
        aggregate_peak_bytes=max(r['job_memory']['peak_job_memory'] for r in heavy),
        resource_stop=False,stop='preregistered fixed sample cap with rank<=529',
        inherited_premises=pilot['inherited']+['degree26 ambient multiplicity531'],
        runs=runs))
    files = list(OUT.glob('*')) + [ROOT/'analysis/b15_05_tail21.py',Path(__file__),
        ROOT/'analysis/b15_bound.py',ROOT/'analysis/b14_06_run.py',
        ROOT/'tools/integrate/exclusion_predicates.py',ROOT/'results/b14_11/exact_exclusions.json',
        ROOT/'docs/b15_05_report.md',ROOT/'docs/b15_05_proved.md',ROOT/'results/PREREG_b15_05.md']
    files += list((ROOT/'results/logs').glob('b15_05_*_resources.json'))
    receipt = {}
    for file in sorted(set(files)):
        if not file.is_file() or file.name == 'file_receipt.json' or 'runtime_native' in file.name:
            continue
        data = file.read_bytes()
        if file.is_relative_to(OUT) and len(data)>=5_000_000:
            raise ValueError('output over per-file limit: '+str(file))
        receipt[file.relative_to(ROOT).as_posix()] = dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
    write('file_receipt.json',dict(status='RECORDED',hash_convention='exact native bytes; this receipt excludes itself to avoid self-reference',files=receipt))
    print(json.dumps(dict(det_rank_lb=529,D_ub=1,combined_wall_seconds=elapsed,
        aggregate_peak_mib=max(r['job_memory']['peak_job_memory'] for r in heavy)/1048576,
        release_path=str(OUT/'lease_release.json'))))


if __name__=='__main__':
    main()
