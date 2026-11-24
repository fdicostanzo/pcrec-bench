#!/bin/bash
# [B152] launch wrapper (boxq_window needs an EXECUTABLE chain path; the 2026-10-29 lesson).
cd /home/pcrec/projects/pcrec-bench || exit 9
export MACHINE_ID=ryzen7700x
exec bash /home/pcrec/projects/pcrec-bench/docs/dev/lanes/b152win_chain.sh
