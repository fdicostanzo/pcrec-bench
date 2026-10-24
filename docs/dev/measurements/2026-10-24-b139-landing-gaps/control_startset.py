#!/usr/bin/env python3
# b139gaps / control_startset.py -- CONTROL sharing no code with landings.py's table parse: for every
# (set,pattern) whose artifact has a table site, ask the pinned pcrec for `--emit-facts` start_set (the
# pattern-facts record, hex bitmap) and compare it byte for byte with the emitted C table. (auto config;
# nocaps/vm tables compared in the same run when the site exists.)
import sys,os,re,subprocess,json,numpy as np
sys.path.insert(0,"/home/pcrec/projects/pcrec-bench")
from pcrecbench import subbench
sys.path.insert(0,"/var/tmp/pcrecbench/b139gaps")
ROOT="/home/pcrec/projects/pcrec-bench"; P=ROOT+"/build/pcrec-6b2dbd3e/build/pcrec"
CD="/var/tmp/pcrecbench/b139gaps/c"
def tab(t,n):
    m=re.search(r'static const unsigned char %s\[256\] = \{(.*?)\};'%n,t,re.S)
    return None if not m else np.array([1 if int(x) else 0 for x in re.findall(r'-?\d+',m.group(1))],dtype=np.uint8)
ok=bad=0; ex=[]
cfgfl={"auto":["--features","all"],"nocaps":["--features","all","--no-captures"],"vm":["--features","all","--engine=vm"]}
for s in ["altwide","bounded","capability","email","litrun","loglines","sentinel","syntax","utf8"]:
    sb=subbench.load(f"{ROOT}/bench/{s}")
    for p in sb.patterns:
        facts={}
        for cfg in ("auto","vm"):
            f=f"{CD}/{cfg}/{s}/{p.name}.c"
            if not os.path.exists(f): continue
            t=open(f,errors="replace").read()
            for n in ("rx_can_begin_match","rx_start_bytes","rx_start_set"):
                T=tab(t,n)
                if T is None: continue
                if "ss" not in facts:
                    r=subprocess.run([P,"-p","rx"]+cfgfl[cfg]+(["-e","utf8"] if s=="utf8" else [])+["--emit-facts","--pattern",bytes(sb.pattern_bytes(p.name))],capture_output=True,env={"LC_ALL":"C","PATH":os.environ["PATH"]})
                    m=re.search(rb'\tstart_set\tpattern\tE2\t\w+\t\w+\t(\d+):([0-9a-f]{64})',r.stdout)
                    facts["ss"]=m
                m=facts["ss"]
                if not m: ex.append(("nofact",cfg,s,p.name,n)); continue
                bits=np.zeros(256,dtype=np.uint8); raw=bytes.fromhex(m.group(2).decode())
                for b in range(256): bits[b]=(raw[b//8]>>(b%8))&1
                if (bits==T).all(): ok+=1
                else: bad+=1; ex.append(("DIFF",cfg,s,p.name,n,int(bits.sum()),int(T.sum())))
print("equal",ok,"differ",bad)
import collections
print(collections.Counter(e[0] for e in ex))
for e in ex[:25]: print(e)
