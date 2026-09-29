#!/bin/bash
# [B116] I-119 executor run, verbatim except: archive copy (no git log line; pin in ../pin.txt).
cd /var/tmp/clstree_s0/pcrec || exit 9
for i in $(seq 1 90); do awk '{exit !($1<0.15 && $2<0.3)}' /proc/loadavg && break; sleep 30; done
echo "pre-wait load: $(cat /proc/loadavg)"
echo "pin: $(cat ../pin.txt)"
gcc --version | head -1
mkdir -p build/clstree_s0
gnutimeout 7200 make -C studies/cls_tree_study bench2 CC=gcc \
    > build/clstree_s0/b1_bench2.log 2>&1
tail -5 build/clstree_s0/b1_bench2.log
wc -l studies/cls_tree_study/results/bench2.tsv
head -1 studies/cls_tree_study/results/bench2.tsv
gnutimeout 1800 make -C studies/cls_tree_study bench2-bytes CC=gcc \
    > build/clstree_s0/clspack_bench2_bytes.log 2>&1
tail -5 build/clstree_s0/clspack_bench2_bytes.log
wc -l studies/cls_tree_study/results/bench2_bytes.tsv
head -1 studies/cls_tree_study/results/bench2_bytes.tsv
gnutimeout 600 python3 studies/cls_tree_study/bench.py \
    --population k53 --sets '^C' --regimes member --lams 0,16,256 \
    --rounds 41 --out capC_isolated.tsv \
    > build/clstree_s0/measc_isolated.log 2>&1
tail -5 build/clstree_s0/measc_isolated.log
wc -l studies/cls_tree_study/results/capC_isolated.tsv
echo "CLS-TREE-S0-TIMING DONE"
