"""subst_py.py -- the python TOOLS-tier testee's committed script
(docs/design/subst_bench_v1.md 3.2, ruling 8a item 6): a whole-file `re.sub`
on BYTES, one call, the idiomatic "edit a file" script. The result goes to
stdout (the tools tier pipes it into `wc -c`, or a file for the untimed
correctness pass).

    python3 -I subst_py.py PATTERN_FILE TEMPLATE_FILE INPUT_FILE

PATTERN_FILE and TEMPLATE_FILE hold the case's pattern and the template
already rendered in python's bytes-template dialect (`\\g<N>`), raw bytes, no
trailing newline. Interpreter start-up is part of the number, as it is for
every tool.
"""
import re
import sys

pat = open(sys.argv[1], "rb").read()
repl = open(sys.argv[2], "rb").read()
data = open(sys.argv[3], "rb").read()
sys.stdout.buffer.write(re.sub(pat, repl, data, flags=re.ASCII))
