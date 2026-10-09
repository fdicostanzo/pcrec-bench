#!/bin/bash
# [B132] the DRIVER's own layout: build driver.c as the harness does (gcc -O2
# -std=gnu11 ... -ldl as driverrun.build_driver; extras read there) from each
# arm's file and print main's address/size mod 64 / 4096 and the .text size.
# Arms: 26eebfa (OLD), e46e326 (WIN, window-era), master (NEW).
D=$(mktemp -d); trap 'rm -rf $D' EXIT
for r in 26eebfa e46e326 master; do
  git show $r:testees/pcrec/driver.c > $D/driver-$r.c
  gcc -O2 -std=gnu11 -o $D/drv-$r $D/driver-$r.c -ldl -lm 2>$D/err-$r || { echo "gcc failed $r"; cat $D/err-$r|head -3; continue; }
  echo "### driver @$r  .text: $(size -A $D/drv-$r | awk '$1==".text"{print $2}')"
  nm -n -S --defined-only $D/drv-$r | awk '$4=="main"||$4=="now"{a=strtonum("0x"$1); printf "   %-6s addr=0x%x size=%d mod64=%d mod4096=%d\n",$4,a,strtonum("0x"$2),a%64,a%4096}'
done
