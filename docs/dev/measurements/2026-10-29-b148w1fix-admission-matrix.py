import sys
root=sys.argv[1]; sys.path.insert(0,root)
from pcrecbench import subbench, capability as C
sb=subbench.load(root+"/bench/unusual")
import re
tids=sorted(C.capabilities_for.__globals__['_load_matrix'](sb))
for t in tids:
    for p in sb.patterns:
        m=C.missing_capabilities(sb,t,p)
        print(p.name,t,",".join(sorted(m)) or "ADMIT",sep="\t")
