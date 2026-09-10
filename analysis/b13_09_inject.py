#!/usr/bin/env python3
"""
B13-09 -- replace each `<!-- GENERATED: <section> -->` marker in the report with
the table that `analysis/b13_09_report.py` generates for it, so that no number in
the report is hand-transcribed from a log.

Idempotent: a marker is replaced by the marker plus the table, and a re-run
regenerates the table between the marker and the following `<!-- /GENERATED -->`
sentinel.

usage: python3 analysis/b13_09_inject.py [docs/b13_09_report.md]
"""
import sys, os, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))
MARK = re.compile(r'<!-- GENERATED: (\w+) -->(?:\n(?:.*?)\n<!-- /GENERATED -->)?', re.S)


def table(section):
    r = subprocess.run(['python3', os.path.join(HERE, 'b13_09_report.py'), '--section', section],
                       capture_output=True, text=True, cwd=ROOT)
    if r.returncode != 0:
        raise SystemExit(f"report generator failed for {section}: {r.stderr[-2000:]}")
    return r.stdout.strip()


def main(argv):
    path = argv[0] if argv else os.path.join(ROOT, 'docs', 'b13_09_report.md')
    s = open(path).read()
    found = []

    def rep(m):
        sec = m.group(1); found.append(sec)
        return f"<!-- GENERATED: {sec} -->\n{table(sec)}\n<!-- /GENERATED -->"

    out = MARK.sub(rep, s)
    open(path, 'w').write(out)
    print(f"injected {len(found)} generated sections into {os.path.relpath(path, ROOT)}: {', '.join(found)}")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
