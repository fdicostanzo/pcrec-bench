#!/bin/bash
# [B132] layout facts: for a few patterns x {auto caps, nocaps} emit the artifact
# with pin 255bcdd8's pcrec (same argv as adapter.py phase 1), build it with
# SHIM-OLD and SHIM-NEW exactly as phase 2 does ($CC -O2 -std=gnu11 -fPIC
# -shared shim.c -DPB_ARTIFACT=... -I dir), print `size -A` of the .so (.text
# size + alignment from readelf -S), and every function symbol of the .so
# with address mod 64 / mod 4096 (nm -n --defined-only; addr = link-time VMA).
# usage: layout-facts.sh OUTDIR   (OLD/NEW shim dirs via $OLDD/$NEWD)
W=/home/duxevents/pcrec-bench/worktrees
OLDD=$W/b132shim-old/testees/pcrec; NEWD=$W/b132shim/testees/pcrec
PCREC=$(/home/duxevents/pcrec-bench/testees/pcrec/pin.sh --path 255bcdd8)
PAT=$W/b132shim/bench/capability/patterns
OUT=$(realpath -m "${1:?outdir}"); mkdir -p "$OUT"
for cfg in auto:"" nocaps:"--no-captures"; do
 name=${cfg%%:*}; fl=${cfg#*:}
 for p in winpath-near-miss base10num-near-miss ipv4-near-miss uuid-near-miss trim-nested-star keyword-prefix-order wild-waf-crs-942360-concat-sqli; do
  d=$OUT/$name-$p; mkdir -p $d
  $PCREC -p rx -fcomments --features all $fl -o $d/artifact.c --pattern "$(cat $PAT/$p.rx)" >/dev/null 2>$d/emit.err || { echo "emit failed $name $p"; continue; }
  for arm in OLD NEW; do
    sd=$OLDD; [ $arm = NEW ] && sd=$NEWD
    gcc -O2 -std=gnu11 -fPIC -shared -o $d/$arm.so $sd/shim.c -DPB_ARTIFACT="\"$d/artifact.c\"" -I $d 2>$d/$arm.err || { echo "gcc failed $arm $name $p"; continue; }
    echo "### $name $p $arm  sha256(.so)=$(sha256sum < $d/$arm.so | cut -c1-16) bytes=$(stat -c%s $d/$arm.so)"
    size -A $d/$arm.so | awk '$1==".text"||$1=="Total"{print "   size -A: "$0}'
    readelf -SW $d/$arm.so | awk '/ \.text /{print "   .text hdr: "$0}'
    readelf -lW $d/$arm.so | awk '$1=="LOAD"{print "   "$0}'
    nm -n --defined-only -S $d/$arm.so | awk '$3 ~ /[tT]/ {a=strtonum("0x"$1); printf "   fn %-34s addr=0x%x size=%d mod64=%d mod4096=%d\n",$4,a,strtonum("0x"$2),a%64,a%4096}'
  done
 done
done
