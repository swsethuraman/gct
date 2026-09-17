"""B20-02 pilot 3 driver: ONE wrapped process running (1) the sixteen-variable pricing script and
(2) the five-variable Koszul profile with deadline guard and incremental JSON. Both scripts write their
own JSON under results/b20_02/; the wrapper receipt covers both."""
import os, runpy, sys, time
T0 = time.perf_counter()
here = os.path.dirname(os.path.abspath(__file__))
sys.argv = ['b20_02_price16.py', '--out', os.path.join('results', 'b20_02', 'p3_price16_blocks.json')]
runpy.run_path(os.path.join(here, 'b20_02_price16.py'), run_name='__main__')
print(f'[driver] pricing done at t={time.perf_counter()-T0:.1f}s', flush=True)
sys.argv = ['b20_02_koszul5.py', '--kmin', '3', '--kmax', '12', '--kmax-nondet', '10', '--exact-limit', '320000',
            '--n-primes', '1', '--out', os.path.join('results', 'b20_02', 'p3_koszul5_k3_12.json')]
runpy.run_path(os.path.join(here, 'b20_02_koszul5.py'), run_name='__main__')
print(f'[driver] all done at t={time.perf_counter()-T0:.1f}s', flush=True)
