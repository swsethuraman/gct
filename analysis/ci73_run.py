"""Full fresh CI73 replay through the repository's normal verifier CLI."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path('tools/verify').resolve()))
from verify import main as standard_main

def main():
    raise SystemExit(standard_main(['results/ci73/certificate.json',
        '--report','results/ci73/receiver_report.md','--json-report','results/ci73/verification.json']))

if __name__=='__main__':main()
