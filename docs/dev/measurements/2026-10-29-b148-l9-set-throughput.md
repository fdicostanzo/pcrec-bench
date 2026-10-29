# SOURCE HEADER (lane b148l9read, 2026-10-29): report --grain set --regime large-subject-throughput
# records: the SCRATCH store build/scratch-store (main tree) of the [B148] L9 window (19 unusual@0.1 records, tier scratch,
#   12 measured / 7 inconclusive-load; chain docs/dev/lanes/b148l9_chain.sh, log /var/tmp/pcrecbench/b148l9win/window_unusual.log)
# command: python3 -m pcrecbench report --store <main>/build/scratch-store --subbench unusual --grain set --regime large-subject-throughput --include-scratch --include-unmeasured --include-provenance (verbatim)
# reports/CLAUDE.md admits no scratch-tier report group, so this lives under docs/dev/measurements/ (never a ranking input).
# NOTE the stream/set tables' "state" is the CELL outcome state; the RECORD status (inconclusive-load) is in the Query list and Legend.

# pcrec-bench report

reporter: v28 (2026-10-25)

## Query

- filters: subbench=unusual, regime=large-subject-throughput
- record source: store/index.tsv (19 record(s) matching this query)
- records included: 19
- worst other-core busy: 50.0% (`libpcre2_10.46_jit-caps-simdna` / `wild-json-validate` / `large-subject-throughput`)
    - `unusual@0.1__libpcre2_10.46_interp-caps-simdna__ryzen7700x__20261029T001134Z` (scratch-store/records/unusual@0.1/libpcre2_10.46_interp-caps-simdna/unusual@0.1__libpcre2_10.46_interp-caps-simdna__ryzen7700x__20261029T001134Z.jsonl) — agreement: agree (0 of 38 groups; 0 of 3281 rows; 50 unjudged (2 all-timed-out); k=1.5, 2/3; 5 trials)
        - timeline: 42 group(s) (/proc/stat, provenance); 5 depart from the run's median by > 7 points
            - `co-luhn-pass` / `large-subject-throughput` / `plain`: 274 ms, target 96.3%, sibling 0.0%, busiest other cpu14 28.57%
            - `co-luhn-nofn` / `large-subject-throughput` / `plain`: 284 ms, target 96.55%, sibling 3.45%, busiest other cpu14 18.52%
            - `co-isbn-twin` / `large-subject-throughput` / `plain`: 231 ms, target 95.83%, sibling 0.0%, busiest other cpu12 29.17%
            - `co-member-twin` / `large-subject-throughput` / `plain`: 293 ms, target 96.55%, sibling 0.0%, busiest other cpu1 23.33%
            - `co-netstr-twin` / `large-subject-throughput` / `plain`: 355 ms, target 97.22%, sibling 0.0%, busiest other cpu6 27.03%
    - `unusual@0.1__libpcre2_10.46_interp-caps-simdna_lim-ceil1g__ryzen7700x__20261029T023344Z` (scratch-store/records/unusual@0.1/libpcre2_10.46_interp-caps-simdna_lim-ceil1g/unusual@0.1__libpcre2_10.46_interp-caps-simdna_lim-ceil1g__ryzen7700x__20261029T023344Z.jsonl) — agreement: agree (0 of 38 groups; 0 of 3281 rows; 50 unjudged (2 all-timed-out); k=1.5, 2/3; 5 trials)
        - timeline: 42 group(s) (/proc/stat, provenance); 9 depart from the run's median by > 7 points
            - `cscan-onig` / `call-stream` / `plain`: 3833 ms, target 99.74%, sibling 0.26%, busiest other cpu8 14.4%
            - `co-luhn` / `large-subject-throughput` / `plain`: 287 ms, target 96.55%, sibling 0.0%, busiest other cpu6 25.0%
            - `co-luhn-pass` / `large-subject-throughput` / `plain`: 284 ms, target 96.55%, sibling 0.0%, busiest other cpu11 20.69%
            - `co-luhn-twin` / `large-subject-throughput` / `plain`: 291 ms, target 96.55%, sibling 0.0%, busiest other cpu6 24.14%
            - `co-isbn` / `large-subject-throughput` / `plain`: 264 ms, target 96.3%, sibling 0.0%, busiest other cpu12 22.22%
            - `co-isbn-pass` / `large-subject-throughput` / `plain`: 271 ms, target 96.3%, sibling 0.0%, busiest other cpu2 21.43%
            - `co-member-pass` / `large-subject-throughput` / `plain`: 289 ms, target 96.55%, sibling 3.33%, busiest other cpu2 27.59%
            - `co-member-twin` / `large-subject-throughput` / `plain`: 285 ms, target 96.43%, sibling 0.0%, busiest other cpu0 17.24%
            - `co-netstr-assist` / `large-subject-throughput` / `plain`: 395 ms, target 97.44%, sibling 2.5%, busiest other cpu2 26.83%
    - `unusual@0.1__libpcre2_10.46_jit-caps-simdna__ryzen7700x__20261028T235037Z` (scratch-store/records/unusual@0.1/libpcre2_10.46_jit-caps-simdna/unusual@0.1__libpcre2_10.46_jit-caps-simdna__ryzen7700x__20261028T235037Z.jsonl) — agreement: agree (0 of 40 groups; 48 of 3303 rows; 28 unjudged; k=1.5, 2/3; 5 trials); after: occ 18.53%
        - provenance: after-sample (provenance, not a verdict): occupancy after the run 18.53% busy on the busiest non-target core (limit 10.00%)
        - timeline: 42 group(s) (/proc/stat, provenance); 11 depart from the run's median by > 7 points
            - `cscan-onig` / `call-stream` / `plain`: 921 ms, target 97.83%, sibling 8.79%, busiest other cpu12 13.98%
            - `wild-sexp-balanced` / `large-subject-throughput` / `plain`: 76 ms, target 75.0%, sibling 0.0%, busiest other cpu13 25.0%
            - `wild-json-validate` / `large-subject-throughput` / `plain`: 21 ms, target 50.0%, sibling 0.0%, busiest other cpu8 50.0%
            - `wild-json-validate-onig` / `large-subject-throughput` / `plain`: 19 ms, target 50.0%, sibling 0.0%, busiest other cpu0 0.0%
            - `co-luhn` / `large-subject-throughput` / `plain`: 284 ms, target 96.55%, sibling 0.0%, busiest other cpu0 18.52%
            - `co-luhn-nofn` / `large-subject-throughput` / `plain`: 291 ms, target 96.55%, sibling 0.0%, busiest other cpu4 23.33%
            - `co-isbn-nofn` / `large-subject-throughput` / `plain`: 267 ms, target 96.3%, sibling 3.7%, busiest other cpu6 28.57%
            - `co-member` / `large-subject-throughput` / `plain`: 235 ms, target 95.65%, sibling 0.0%, busiest other cpu0 16.67%
            - `co-member-twin` / `large-subject-throughput` / `plain`: 232 ms, target 91.67%, sibling 0.0%, busiest other cpu5 21.74%
            - `co-member-nofn` / `large-subject-throughput` / `plain`: 265 ms, target 92.86%, sibling 0.0%, busiest other cpu8 6.9%
            - `co-netstr-assist` / `large-subject-throughput` / `plain`: 327 ms, target 96.97%, sibling 0.0%, busiest other cpu5 26.47%
    - `unusual@0.1__libpcre2_10.46_jit-caps-simdna_assist-v01__ryzen7700x__20261028T231136Z` (scratch-store/records/unusual@0.1/libpcre2_10.46_jit-caps-simdna_assist-v01/unusual@0.1__libpcre2_10.46_jit-caps-simdna_assist-v01__ryzen7700x__20261028T231136Z.jsonl) — agreement: agree (0 of 6 groups; 0 of 515 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
        - timeline: 6 group(s) (/proc/stat, provenance); 1 depart from the run's median by > 7 points
            - `co-netstr` / `large-subject-throughput` / `plain`: 353 ms, target 97.14%, sibling 0.0%, busiest other cpu13 23.53%
    - `unusual@0.1__libpcre2_10.46_jit-caps-simdna_lim-ceil1g__ryzen7700x__20261029T021314Z` (scratch-store/records/unusual@0.1/libpcre2_10.46_jit-caps-simdna_lim-ceil1g/unusual@0.1__libpcre2_10.46_jit-caps-simdna_lim-ceil1g__ryzen7700x__20261029T021314Z.jsonl) — agreement: agree (0 of 42 groups; 0 of 3331 rows; 0 unjudged; k=1.5, 2/3; 5 trials); after: load1 2.08
        - provenance: after-sample (provenance, not a verdict): load1 after the run 2.08 exceeds the limit 2.00
        - provenance: `load.verdict = loaded` beside `status = measured` (v1.4 X20 is an either-sample fact; X13 reads the before sample)
        - timeline: 42 group(s) (/proc/stat, provenance); 6 depart from the run's median by > 7 points
            - `wild-json-validate` / `short-subject-search` / `plain`: 59348 ms, target 99.98%, sibling 1.05%, busiest other cpu9 15.05%
            - `wild-json-validate` / `large-subject-throughput` / `plain`: 428 ms, target 97.67%, sibling 0.0%, busiest other cpu3 29.27%
            - `co-luhn` / `large-subject-throughput` / `plain`: 284 ms, target 96.43%, sibling 3.45%, busiest other cpu1 28.57%
            - `co-isbn-twin` / `large-subject-throughput` / `plain`: 273 ms, target 100.0%, sibling 11.11%, busiest other cpu12 31.03%
            - `co-member-nofn` / `large-subject-throughput` / `plain`: 232 ms, target 95.45%, sibling 0.0%, busiest other cpu2 17.39%
            - `co-netstr-twin` / `large-subject-throughput` / `plain`: 286 ms, target 96.67%, sibling 0.0%, busiest other cpu6 17.24%
    - `unusual@0.1__oniguruma_6.9.10_default-caps-simdna__ryzen7700x__20261029T013849Z` (scratch-store/records/unusual@0.1/oniguruma_6.9.10_default-caps-simdna/unusual@0.1__oniguruma_6.9.10_default-caps-simdna__ryzen7700x__20261029T013849Z.jsonl) — agreement: agree (0 of 34 groups; 0 of 2801 rows; 44 unjudged; k=1.5, 2/3; 5 trials)
        - timeline: 36 group(s) (/proc/stat, provenance); 2 depart from the run's median by > 7 points
            - `co-luhn-pass` / `large-subject-throughput` / `plain`: 289 ms, target 96.55%, sibling 10.34%, busiest other cpu0 28.57%
            - `co-netstr-twin` / `large-subject-throughput` / `plain`: 310 ms, target 96.77%, sibling 0.0%, busiest other cpu3 22.58%
    - `unusual@0.1__oniguruma_6.9.10_default-caps-simdna_assist-v01__ryzen7700x__20261028T231549Z` (scratch-store/records/unusual@0.1/oniguruma_6.9.10_default-caps-simdna_assist-v01/unusual@0.1__oniguruma_6.9.10_default-caps-simdna_assist-v01__ryzen7700x__20261028T231549Z.jsonl) — agreement: agree (0 of 6 groups; 0 of 515 rows; 0 unjudged; k=1.5, 2/3; 5 trials); after: occ 10.71%
        - provenance: after-sample (provenance, not a verdict): occupancy after the run 10.71% busy on the busiest non-target core (limit 10.00%)
        - timeline: 6 group(s) (/proc/stat, provenance); 1 depart from the run's median by > 7 points
            - `co-netstr` / `large-subject-throughput` / `plain`: 381 ms, target 97.44%, sibling 0.0%, busiest other cpu14 23.68%
    - `unusual@0.1__oniguruma_6.9.10_default-caps-simdna_lim-ceil1g__ryzen7700x__20261029T043546Z` (scratch-store/records/unusual@0.1/oniguruma_6.9.10_default-caps-simdna_lim-ceil1g/unusual@0.1__oniguruma_6.9.10_default-caps-simdna_lim-ceil1g__ryzen7700x__20261029T043546Z.jsonl) — agreement: agree (0 of 31 groups; 0 of 2785 rows; 60 unjudged (2 all-timed-out); k=1.5, 2/3; 5 trials); after: occ 12.17%
        - provenance: after-sample (provenance, not a verdict): occupancy after the run 12.17% busy on the busiest non-target core (limit 10.00%)
        - timeline: 36 group(s) (/proc/stat, provenance); 3 depart from the run's median by > 7 points
            - `co-luhn-pass` / `large-subject-throughput` / `plain`: 290 ms, target 96.43%, sibling 0.0%, busiest other cpu4 23.33%
            - `co-member-pass` / `large-subject-throughput` / `plain`: 278 ms, target 92.86%, sibling 0.0%, busiest other cpu0 0.0%
            - `co-netstr-assist` / `large-subject-throughput` / `plain`: 412 ms, target 97.56%, sibling 7.32%, busiest other cpu0 27.5%
    - `unusual@0.1__pcrec_614d45eb3_auto-caps-simdna__ryzen7700x__20261029T010158Z` (scratch-store/records/unusual@0.1/pcrec_614d45eb3_auto-caps-simdna/unusual@0.1__pcrec_614d45eb3_auto-caps-simdna__ryzen7700x__20261029T010158Z.jsonl) — agreement: agree (0 of 35 groups; 0 of 2627 rows; 35 unjudged; k=1.5, 2/3; 5 trials); after: occ 12.98%
        - provenance: after-sample (provenance, not a verdict): occupancy after the run 12.98% busy on the busiest non-target core (limit 10.00%)
        - timeline: 37 group(s) (/proc/stat, provenance); 7 depart from the run's median by > 7 points
            - `wild-sexp-balanced` / `large-subject-throughput` / `plain`: 52 ms, target 66.67%, sibling 0.0%, busiest other cpu3 33.33%
            - `wild-json-validate-onig` / `large-subject-throughput` / `plain`: 19 ms, target 50.0%, sibling 0.0%, busiest other cpu2 33.33%
            - `co-luhn-pass` / `large-subject-throughput` / `plain`: 290 ms, target 96.55%, sibling 0.0%, busiest other cpu0 17.24%
            - `co-luhn-twin` / `large-subject-throughput` / `plain`: 283 ms, target 96.43%, sibling 0.0%, busiest other cpu9 28.57%
            - `co-isbn-twin` / `large-subject-throughput` / `plain`: 223 ms, target 95.45%, sibling 0.0%, busiest other cpu11 30.43%
            - `co-netstr` / `large-subject-throughput` / `plain`: 290 ms, target 96.55%, sibling 0.0%, busiest other cpu0 24.14%
            - `co-netstr-twin` / `large-subject-throughput` / `plain`: 267 ms, target 96.3%, sibling 0.0%, busiest other cpu9 14.81%
    - `unusual@0.1__pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g__ryzen7700x__20261029T032324Z` (scratch-store/records/unusual@0.1/pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g/unusual@0.1__pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g__ryzen7700x__20261029T032324Z.jsonl) — agreement: agree (0 of 36 groups; 0 of 2660 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
        - timeline: 37 group(s) (/proc/stat, provenance); 8 depart from the run's median by > 7 points
            - `wild-json-validate-onig` / `large-subject-throughput` / `plain`: 1462 ms, target 100.0%, sibling 0.68%, busiest other cpu8 19.86%
            - `co-luhn` / `large-subject-throughput` / `plain`: 280 ms, target 96.43%, sibling 0.0%, busiest other cpu1 28.57%
            - `co-luhn-pass` / `large-subject-throughput` / `plain`: 290 ms, target 96.55%, sibling 0.0%, busiest other cpu9 23.33%
            - `co-member` / `large-subject-throughput` / `plain`: 285 ms, target 100.0%, sibling 3.33%, busiest other cpu14 37.04%
            - `co-member-pass` / `large-subject-throughput` / `plain`: 281 ms, target 96.43%, sibling 3.57%, busiest other cpu5 21.43%
            - `co-member-twin` / `large-subject-throughput` / `plain`: 280 ms, target 96.55%, sibling 0.0%, busiest other cpu2 17.86%
            - `co-netstr` / `large-subject-throughput` / `plain`: 286 ms, target 96.55%, sibling 0.0%, busiest other cpu0 24.14%
            - `va-term-bang` / `call-stream` / `plain`: 236 ms, target 92.0%, sibling 0.0%, busiest other cpu3 4.17%
    - `unusual@0.1__pcrec_614d45eb3_vm-caps-simdna__ryzen7700x__20261029T012026Z` (scratch-store/records/unusual@0.1/pcrec_614d45eb3_vm-caps-simdna/unusual@0.1__pcrec_614d45eb3_vm-caps-simdna__ryzen7700x__20261029T012026Z.jsonl) — agreement: agree (0 of 35 groups; 0 of 2627 rows; 35 unjudged; k=1.5, 2/3; 5 trials)
        - timeline: 37 group(s) (/proc/stat, provenance); 15 depart from the run's median by > 7 points
            - `cscan-onig` / `large-subject-throughput` / `plain`: 382 ms, target 94.74%, sibling 2.63%, busiest other cpu12 26.32%
            - `cscan-onig` / `call-stream` / `plain`: 799 ms, target 98.75%, sibling 0.0%, busiest other cpu1 13.92%
            - `wild-sexp-balanced` / `large-subject-throughput` / `plain`: 55 ms, target 66.67%, sibling 0.0%, busiest other cpu11 16.67%
            - `wild-json-validate-onig` / `large-subject-throughput` / `plain`: 19 ms, target 50.0%, sibling 0.0%, busiest other cpu0 0.0%
            - `co-luhn-pass` / `large-subject-throughput` / `plain`: 288 ms, target 96.55%, sibling 3.33%, busiest other cpu14 23.33%
            - `co-isbn` / `large-subject-throughput` / `plain`: 280 ms, target 96.43%, sibling 0.0%, busiest other cpu10 25.0%
            - `co-member` / `large-subject-throughput` / `plain`: 279 ms, target 96.43%, sibling 0.0%, busiest other cpu5 25.0%
            - `co-member-pass` / `large-subject-throughput` / `plain`: 288 ms, target 92.86%, sibling 0.0%, busiest other cpu5 24.14%
            - `co-member-twin` / `large-subject-throughput` / `plain`: 268 ms, target 96.3%, sibling 3.7%, busiest other cpu10 25.93%
            - `co-netstr` / `large-subject-throughput` / `plain`: 283 ms, target 96.43%, sibling 0.0%, busiest other cpu1 27.59%
            - `co-netstr-assist` / `large-subject-throughput` / `plain`: 288 ms, target 96.55%, sibling 7.14%, busiest other cpu2 17.86%
            - `va-tenant` / `call-stream` / `plain`: 879 ms, target 97.75%, sibling 0.0%, busiest other cpu11 15.12%
            - `va-route` / `call-stream` / `plain`: 215 ms, target 100.0%, sibling 0.0%, busiest other cpu13 28.57%
            - `va-term` / `call-stream` / `plain`: 232 ms, target 92.0%, sibling 0.0%, busiest other cpu14 30.43%
            - `va-term-bang` / `call-stream` / `plain`: 232 ms, target 95.45%, sibling 0.0%, busiest other cpu2 27.27%
    - `unusual@0.1__pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g__ryzen7700x__20261029T035902Z` (scratch-store/records/unusual@0.1/pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g/unusual@0.1__pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g__ryzen7700x__20261029T035902Z.jsonl) — agreement: agree (0 of 36 groups; 0 of 2660 rows; 2 unjudged; k=1.5, 2/3; 5 trials); after: occ 10.44%
        - provenance: after-sample (provenance, not a verdict): occupancy after the run 10.44% busy on the busiest non-target core (limit 10.00%)
        - timeline: 37 group(s) (/proc/stat, provenance); 6 depart from the run's median by > 7 points
            - `co-isbn` / `large-subject-throughput` / `plain`: 233 ms, target 95.65%, sibling 8.0%, busiest other cpu13 8.7%
            - `co-member` / `large-subject-throughput` / `plain`: 281 ms, target 96.43%, sibling 0.0%, busiest other cpu13 24.14%
            - `co-netstr` / `large-subject-throughput` / `plain`: 290 ms, target 96.67%, sibling 0.0%, busiest other cpu8 26.67%
            - `va-route` / `call-stream` / `plain`: 226 ms, target 95.45%, sibling 0.0%, busiest other cpu4 17.39%
            - `va-term` / `call-stream` / `plain`: 241 ms, target 91.67%, sibling 0.0%, busiest other cpu6 25.0%
            - `va-term-bang` / `call-stream` / `plain`: 230 ms, target 91.3%, sibling 4.55%, busiest other cpu14 21.74%
    - `unusual@0.1__re2_11.0.0_default-caps-simdna__ryzen7700x__20261029T020244Z` (scratch-store/records/unusual@0.1/re2_11.0.0_default-caps-simdna/unusual@0.1__re2_11.0.0_default-caps-simdna__ryzen7700x__20261029T020244Z.jsonl) — agreement: agree (0 of 10 groups; 0 of 839 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
        - timeline: 10 group(s) (/proc/stat, provenance); 2 depart from the run's median by > 7 points
            - `co-isbn-twin` / `large-subject-throughput` / `plain`: 258 ms, target 96.15%, sibling 3.85%, busiest other cpu8 33.33%
            - `co-member-twin` / `large-subject-throughput` / `plain`: 273 ms, target 96.3%, sibling 0.0%, busiest other cpu6 29.63%
    - `unusual@0.1__re2_11.0.0_default-caps-simdna_assist-v01__ryzen7700x__20261028T232001Z` (scratch-store/records/unusual@0.1/re2_11.0.0_default-caps-simdna_assist-v01/unusual@0.1__re2_11.0.0_default-caps-simdna_assist-v01__ryzen7700x__20261028T232001Z.jsonl) — agreement: agree (0 of 27 groups; 0 of 1851 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
        - timeline: 27 group(s) (/proc/stat, provenance); 9 depart from the run's median by > 7 points
            - `co-luhn-twin` / `large-subject-throughput` / `plain`: 279 ms, target 96.43%, sibling 0.0%, busiest other cpu1 21.43%
            - `co-isbn` / `large-subject-throughput` / `plain`: 271 ms, target 96.43%, sibling 0.0%, busiest other cpu10 22.22%
            - `co-isbn-twin` / `large-subject-throughput` / `plain`: 267 ms, target 96.15%, sibling 0.0%, busiest other cpu6 24.14%
            - `co-member` / `large-subject-throughput` / `plain`: 281 ms, target 96.43%, sibling 0.0%, busiest other cpu5 24.14%
            - `co-member-twin` / `large-subject-throughput` / `plain`: 270 ms, target 96.3%, sibling 0.0%, busiest other cpu12 25.0%
            - `co-netstr` / `large-subject-throughput` / `plain`: 278 ms, target 96.43%, sibling 0.0%, busiest other cpu14 14.81%
            - `co-netstr-twin` / `large-subject-throughput` / `plain`: 283 ms, target 96.43%, sibling 0.0%, busiest other cpu5 13.79%
            - `va-route` / `call-stream` / `plain`: 212 ms, target 90.91%, sibling 0.0%, busiest other cpu0 0.0%
            - `va-term` / `call-stream` / `plain`: 234 ms, target 92.0%, sibling 0.0%, busiest other cpu10 4.0%
    - `unusual@0.1__rust_1.13.1_default-caps-simdna__ryzen7700x__20261029T020715Z` (scratch-store/records/unusual@0.1/rust_1.13.1_default-caps-simdna/unusual@0.1__rust_1.13.1_default-caps-simdna__ryzen7700x__20261029T020715Z.jsonl) — agreement: agree (0 of 10 groups; 0 of 839 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
        - timeline: 10 group(s) (/proc/stat, provenance); 1 depart from the run's median by > 7 points
            - `co-luhn-twin` / `large-subject-throughput` / `plain`: 279 ms, target 96.55%, sibling 3.45%, busiest other cpu12 27.59%
    - `unusual@0.1__rust_1.13.1_default-caps-simdna_assist-v01__ryzen7700x__20261028T233152Z` (scratch-store/records/unusual@0.1/rust_1.13.1_default-caps-simdna_assist-v01/unusual@0.1__rust_1.13.1_default-caps-simdna_assist-v01__ryzen7700x__20261028T233152Z.jsonl) — agreement: agree (0 of 27 groups; 0 of 1851 rows; 0 unjudged; k=1.5, 2/3; 5 trials); after: occ 10.12%
        - provenance: after-sample (provenance, not a verdict): occupancy after the run 10.12% busy on the busiest non-target core (limit 10.00%)
        - timeline: 27 group(s) (/proc/stat, provenance); 5 depart from the run's median by > 7 points
            - `co-isbn` / `large-subject-throughput` / `plain`: 285 ms, target 96.67%, sibling 0.0%, busiest other cpu8 24.14%
            - `co-netstr` / `large-subject-throughput` / `plain`: 292 ms, target 100.0%, sibling 0.0%, busiest other cpu0 20.0%
            - `va-route` / `call-stream` / `plain`: 253 ms, target 96.0%, sibling 3.85%, busiest other cpu12 25.0%
            - `va-term` / `call-stream` / `plain`: 259 ms, target 96.3%, sibling 0.0%, busiest other cpu11 26.92%
            - `va-term-bang` / `call-stream` / `plain`: 259 ms, target 96.0%, sibling 0.0%, busiest other cpu12 20.0%
    - `unusual@0.1__tre_0.9.0_default-caps-simdna__ryzen7700x__20261029T052235Z` (scratch-store/records/unusual@0.1/tre_0.9.0_default-caps-simdna/unusual@0.1__tre_0.9.0_default-caps-simdna__ryzen7700x__20261029T052235Z.jsonl) — agreement: agree (0 of 2 groups; 0 of 191 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
        - timeline: 2 group(s) (/proc/stat, provenance); 0 depart from the run's median by > 7 points
    - `unusual@0.1__vectorscan_5.4.11_block-som-nocaps-simd__ryzen7700x__20261029T021117Z` (scratch-store/records/unusual@0.1/vectorscan_5.4.11_block-som-nocaps-simd/unusual@0.1__vectorscan_5.4.11_block-som-nocaps-simd__ryzen7700x__20261029T021117Z.jsonl) — agreement: agree (0 of 2 groups; 0 of 191 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
        - timeline: 2 group(s) (/proc/stat, provenance); 0 depart from the run's median by > 7 points
    - `unusual@0.1__vectorscan_5.4.11_block-som-nocaps-simd_assist-v01__ryzen7700x__20261028T234405Z` (scratch-store/records/unusual@0.1/vectorscan_5.4.11_block-som-nocaps-simd_assist-v01/unusual@0.1__vectorscan_5.4.11_block-som-nocaps-simd_assist-v01__ryzen7700x__20261028T234405Z.jsonl) — agreement: agree (0 of 11 groups; 0 of 1008 rows; 1 unjudged; k=1.5, 2/3; 5 trials)
        - timeline: 12 group(s) (/proc/stat, provenance); 2 depart from the run's median by > 7 points
            - `co-luhn` / `large-subject-throughput` / `plain`: 281 ms, target 96.43%, sibling 10.71%, busiest other cpu8 18.52%
            - `co-member` / `large-subject-throughput` / `plain`: 277 ms, target 96.3%, sibling 6.9%, busiest other cpu14 22.22%
- sub-bench version(s): unusual@0.1
- machine(s): ryzen7700x
- schema version(s): 1.11
- call-stream rows skipped: 540 (a stream's time is per stream, never per subject; unusual_set_v1.md 7.5)
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown [ACTIVE]
- trial-agreement policy (schema v1.4, rule v1.11-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance [ACTIVE]
- status rule: v1.4 X13 (pre-flight + trial agreement) on 19 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column [ACTIVE]
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

_[B82] (inbox I-99, Frank's ruling -- a D119 addendum): this report's roster spans BOTH capture classes, so the two views below are the HEADLINE -- "If an engine is run non-capturing on a pattern, then we can't compare that to a capturing engine run -- they are almost completely different things with different objectives." No cell in either view compares across classes; the third, MIXED table further down restates today's single-roster ranking and is never the headline._

## Ranking -- CAPTURING engines only, caps vs caps (per pattern x regime, SET grain: sum over the subject set; best median first)

### `co-isbn` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 365,877.5 | 0.3659 | 365,073.9 | 366,124.8 | 368.2 | 0.401x | 1.000x | scratch |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 387,817.4 | 0.3878 | 386,809.1 | 391,554.3 | 1,912.0 | 0.425x | 1.060x | scratch |
| 3 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 556,063.2 | 0.5560 | 553,850.7 | 556,090.0 | 888.9 | 0.610x | 1.520x | scratch |
| 4 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 558,343.5 | 0.5583 | 555,350.9 | 575,870.7 | 9,291.3 | 0.612x | 1.526x | scratch |
| 5 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 567,748.6 | 0.5677 | 552,196.8 | 575,396.6 | 7,742.1 | 0.623x | 1.552x | scratch |
| 6 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 576,848.3 | 0.5768 | 556,004.9 | 582,992.6 | 9,174.9 | 0.633x | 1.577x | scratch |
| 7 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 911,868.6 | 0.9118 | 907,576.4 | 1,018,858.3 | 43,255.6 | 1.000x | 2.492x | scratch |
| 8 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 928,064.3 | 0.9280 | 914,989.7 | 933,084.6 | 6,240.3 | 1.018x | 2.537x | scratch |
| 9 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 1,870,114.6 | 1.8700 | 1,844,303.7 | 1,898,867.3 | 21,413.6 | 2.051x | 5.111x | scratch |
| 10 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,887,698.2 | 1.8876 | 1,865,628.2 | 1,905,112.9 | 15,395.9 | 2.070x | 5.159x | scratch |
| 11 | `re2_11.0.0_default-caps-simdna_assist-v01` | measured | `plain` | same program | 2,294,424.5 | 2.2943 | 2,290,045.8 | 2,311,223.2 | 7,353.6 | 2.516x | 6.271x | scratch |

#### `co-isbn` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 365,877.5 | 0.3659 |
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_jit-caps-simdna` | 387,817.4 | 0.3878 |
| `co-isbn-1m` | 1,000,051 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 556,063.2 | 0.5560 |
| `co-isbn-1m` | 1,000,051 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 558,343.5 | 0.5583 |
| `co-isbn-1m` | 1,000,051 | `pcrec_614d45eb3_auto-caps-simdna` | 567,748.6 | 0.5677 |
| `co-isbn-1m` | 1,000,051 | `pcrec_614d45eb3_vm-caps-simdna` | 576,848.3 | 0.5768 |
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_interp-caps-simdna` | 911,868.6 | 0.9118 |
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 928,064.3 | 0.9280 |
| `co-isbn-1m` | 1,000,051 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 1,870,114.6 | 1.8700 |
| `co-isbn-1m` | 1,000,051 | `oniguruma_6.9.10_default-caps-simdna` | 1,887,698.2 | 1.8876 |
| `co-isbn-1m` | 1,000,051 | `re2_11.0.0_default-caps-simdna_assist-v01` | 2,294,424.5 | 2.2943 |

### `co-isbn-nofn` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 305,756.7 | 0.3057 | 305,393.4 | 307,629.8 | 863.4 | 0.387x | 1.000x | scratch |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 353,367.4 | 0.3533 | 349,754.3 | 366,620.0 | 7,063.8 | 0.448x | 1.156x | scratch |
| 3 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 789,102.2 | 0.7891 | 781,517.8 | 796,404.4 | 5,060.4 | 1.000x | 2.581x | scratch |
| 4 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 792,645.7 | 0.7926 | 783,724.1 | 793,597.3 | 3,676.5 | 1.004x | 2.592x | scratch |

#### `co-isbn-nofn` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 305,756.7 | 0.3057 |
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_jit-caps-simdna` | 353,367.4 | 0.3533 |
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_interp-caps-simdna` | 789,102.2 | 0.7891 |
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 792,645.7 | 0.7926 |

### `co-isbn-pass` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 335,816.0 | 0.3358 | 335,384.4 | 336,750.4 | 488.5 | 0.407x | 1.000x | scratch |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 376,828.0 | 0.3768 | 376,376.5 | 381,360.0 | 1,833.8 | 0.456x | 1.122x | scratch |
| 3 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 472,498.3 | 0.4725 | 471,337.0 | 472,913.9 | 550.6 | 0.572x | 1.407x | scratch |
| 4 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 473,197.2 | 0.4732 | 471,486.4 | 473,950.8 | 818.8 | 0.573x | 1.409x | scratch |
| 5 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 485,272.3 | 0.4852 | 484,244.3 | 485,918.1 | 569.1 | 0.588x | 1.445x | scratch |
| 6 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 486,826.8 | 0.4868 | 485,906.2 | 488,109.0 | 713.9 | 0.590x | 1.450x | scratch |
| 7 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 825,569.5 | 0.8255 | 821,604.0 | 837,789.3 | 6,009.1 | 1.000x | 2.458x | scratch |
| 8 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 830,629.0 | 0.8306 | 825,870.4 | 834,914.7 | 3,143.2 | 1.006x | 2.473x | scratch |
| 9 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,008,198.5 | 2.0081 | 1,963,373.7 | 2,052,856.7 | 29,739.5 | 2.433x | 5.980x | scratch |
| 10 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 2,016,164.6 | 2.0161 | 1,978,139.8 | 2,152,865.0 | 62,432.3 | 2.442x | 6.004x | scratch |

#### `co-isbn-pass` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 335,816.0 | 0.3358 |
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_jit-caps-simdna` | 376,828.0 | 0.3768 |
| `co-isbn-1m` | 1,000,051 | `pcrec_614d45eb3_vm-caps-simdna` | 472,498.3 | 0.4725 |
| `co-isbn-1m` | 1,000,051 | `pcrec_614d45eb3_auto-caps-simdna` | 473,197.2 | 0.4732 |
| `co-isbn-1m` | 1,000,051 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 485,272.3 | 0.4852 |
| `co-isbn-1m` | 1,000,051 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 486,826.8 | 0.4868 |
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_interp-caps-simdna` | 825,569.5 | 0.8255 |
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 830,629.0 | 0.8306 |
| `co-isbn-1m` | 1,000,051 | `oniguruma_6.9.10_default-caps-simdna` | 2,008,198.5 | 2.0081 |
| `co-isbn-1m` | 1,000,051 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 2,016,164.6 | 2.0161 |

### `co-isbn-twin` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna_lim-ceil1g (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 315,169.1 | 0.3152 | 314,379.4 | 318,357.5 | 1,662.5 | 0.410x | 1.000x | scratch |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 335,553.8 | 0.3355 | 334,428.4 | 342,054.3 | 2,860.3 | 0.437x | 1.065x | scratch |
| 3 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 405,558.4 | 0.4055 | 404,697.1 | 406,686.2 | 680.3 | 0.528x | 1.287x | scratch |
| 4 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 407,378.3 | 0.4074 | 406,919.0 | 410,093.0 | 1,269.9 | 0.530x | 1.293x | scratch |
| 5 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 425,088.4 | 0.4251 | 424,217.1 | 427,526.0 | 1,150.4 | 0.553x | 1.349x | scratch |
| 6 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 459,519.0 | 0.4595 | 459,125.1 | 461,529.5 | 887.9 | 0.598x | 1.458x | scratch |
| 7 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 768,654.4 | 0.7686 | 755,524.9 | 780,157.8 | 7,847.3 | 1.000x | 2.439x | scratch |
| 8 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 772,185.9 | 0.7721 | 760,916.9 | 779,503.7 | 7,115.7 | 1.005x | 2.450x | scratch |
| 9 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 1,811,605.4 | 1.8115 | 1,786,732.1 | 1,856,433.8 | 28,875.1 | 2.357x | 5.748x | scratch |
| 10 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,837,607.8 | 1.8375 | 1,790,088.6 | 1,848,676.3 | 20,763.6 | 2.391x | 5.831x | scratch |
| 11 | `re2_11.0.0_default-caps-simdna_assist-v01` | measured | `plain` | same program | 2,135,425.4 | 2.1353 | 2,129,223.7 | 2,171,460.4 | 15,602.6 | 2.778x | 6.775x | scratch |
| 12 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,142,878.5 | 2.1428 | 2,137,515.8 | 2,163,624.5 | 9,574.7 | 2.788x | 6.799x | scratch |

#### `co-isbn-twin` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 315,169.1 | 0.3152 |
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_jit-caps-simdna` | 335,553.8 | 0.3355 |
| `co-isbn-1m` | 1,000,051 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 405,558.4 | 0.4055 |
| `co-isbn-1m` | 1,000,051 | `pcrec_614d45eb3_auto-caps-simdna` | 407,378.3 | 0.4074 |
| `co-isbn-1m` | 1,000,051 | `pcrec_614d45eb3_vm-caps-simdna` | 425,088.4 | 0.4251 |
| `co-isbn-1m` | 1,000,051 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 459,519.0 | 0.4595 |
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 768,654.4 | 0.7686 |
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_interp-caps-simdna` | 772,185.9 | 0.7721 |
| `co-isbn-1m` | 1,000,051 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 1,811,605.4 | 1.8115 |
| `co-isbn-1m` | 1,000,051 | `oniguruma_6.9.10_default-caps-simdna` | 1,837,607.8 | 1.8375 |
| `co-isbn-1m` | 1,000,051 | `re2_11.0.0_default-caps-simdna_assist-v01` | 2,135,425.4 | 2.1353 |
| `co-isbn-1m` | 1,000,051 | `re2_11.0.0_default-caps-simdna` | 2,142,878.5 | 2.1428 |

### `co-luhn` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 931,991.4 | 0.9320 | 926,407.8 | 943,440.3 | 6,467.8 | 0.219x | 1.000x | scratch |
| 2 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 934,494.0 | 0.9345 | 925,692.1 | 939,070.2 | 4,620.4 | 0.219x | 1.003x | scratch |
| 3 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 940,284.4 | 0.9403 | 922,785.5 | 1,006,813.9 | 30,937.8 | 0.221x | 1.009x | scratch |
| 4 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 953,116.3 | 0.9531 | 947,273.6 | 968,664.8 | 7,716.7 | 0.224x | 1.023x | scratch |
| 5 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 1,099,219.6 | 1.0992 | 1,097,967.5 | 1,108,628.6 | 3,890.8 | 0.258x | 1.179x | scratch |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,125,700.2 | 1.1257 | 1,123,312.4 | 1,154,341.3 | 11,637.7 | 0.264x | 1.208x | scratch |
| 7 | `re2_11.0.0_default-caps-simdna_assist-v01` | measured | `plain` | same program | 3,031,297.5 | 3.0312 | 3,026,721.4 | 3,077,287.4 | 18,918.8 | 0.711x | 3.252x | scratch |
| 8 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 4,262,732.6 | 4.2627 | 4,242,526.2 | 4,736,871.8 | 189,674.1 | 1.000x | 4.574x | scratch |
| 9 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 4,276,391.4 | 4.2763 | 4,213,082.0 | 4,334,004.1 | 38,564.3 | 1.003x | 4.588x | scratch |
| 10 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 5,400,307.9 | 5.4002 | 5,330,521.3 | 5,551,449.6 | 76,157.6 | 1.267x | 5.794x | scratch |
| 11 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,415,249.1 | 5.4152 | 5,309,289.5 | 5,515,884.8 | 67,950.9 | 1.270x | 5.810x | scratch |

#### `co-luhn` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-luhn-1m` | 1,000,017 | `pcrec_614d45eb3_auto-caps-simdna` | 931,991.4 | 0.9320 |
| `co-luhn-1m` | 1,000,017 | `pcrec_614d45eb3_vm-caps-simdna` | 934,494.0 | 0.9345 |
| `co-luhn-1m` | 1,000,017 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 940,284.4 | 0.9403 |
| `co-luhn-1m` | 1,000,017 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 953,116.3 | 0.9531 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 1,099,219.6 | 1.0992 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_jit-caps-simdna` | 1,125,700.2 | 1.1257 |
| `co-luhn-1m` | 1,000,017 | `re2_11.0.0_default-caps-simdna_assist-v01` | 3,031,297.5 | 3.0312 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_interp-caps-simdna` | 4,262,732.6 | 4.2627 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 4,276,391.4 | 4.2763 |
| `co-luhn-1m` | 1,000,017 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 5,400,307.9 | 5.4002 |
| `co-luhn-1m` | 1,000,017 | `oniguruma_6.9.10_default-caps-simdna` | 5,415,249.1 | 5.4152 |

### `co-luhn-nofn` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 759,264.2 | 0.7593 | 757,856.6 | 761,326.4 | 1,112.2 | 0.296x | 1.000x | scratch |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 848,897.9 | 0.8489 | 827,398.0 | 873,903.0 | 17,866.8 | 0.331x | 1.118x | scratch |
| 3 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 2,565,770.9 | 2.5657 | 2,553,411.6 | 2,617,814.9 | 23,024.9 | 1.000x | 3.379x | scratch |
| 4 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 2,567,053.3 | 2.5670 | 2,538,558.2 | 2,622,926.3 | 31,079.3 | 1.000x | 3.381x | scratch |

#### `co-luhn-nofn` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 759,264.2 | 0.7593 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_jit-caps-simdna` | 848,897.9 | 0.8489 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_interp-caps-simdna` | 2,565,770.9 | 2.5657 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 2,567,053.3 | 2.5670 |

### `co-luhn-pass` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna_lim-ceil1g (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 642,826.5 | 0.6428 | 634,189.6 | 646,348.3 | 4,044.0 | 0.249x | 1.000x | scratch |
| 2 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 643,297.3 | 0.6433 | 641,057.0 | 644,497.1 | 1,221.9 | 0.250x | 1.001x | scratch |
| 3 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 644,266.1 | 0.6443 | 641,651.2 | 653,196.2 | 4,242.0 | 0.250x | 1.002x | scratch |
| 4 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 650,518.0 | 0.6505 | 649,998.6 | 652,782.0 | 1,001.5 | 0.252x | 1.012x | scratch |
| 5 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 799,422.7 | 0.7994 | 798,847.2 | 804,661.3 | 2,197.0 | 0.310x | 1.244x | scratch |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 872,709.4 | 0.8727 | 863,495.8 | 889,228.8 | 8,872.0 | 0.339x | 1.358x | scratch |
| 7 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 2,577,656.6 | 2.5776 | 2,561,367.4 | 2,593,628.7 | 11,353.6 | 1.000x | 4.010x | scratch |
| 8 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 2,604,152.5 | 2.6041 | 2,596,746.9 | 2,609,414.0 | 4,335.6 | 1.010x | 4.051x | scratch |
| 9 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 3,949,298.5 | 3.9492 | 3,907,606.9 | 4,125,519.8 | 90,431.7 | 1.532x | 6.144x | scratch |
| 10 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,210,924.8 | 4.2109 | 4,124,626.3 | 4,608,930.6 | 181,316.1 | 1.634x | 6.551x | scratch |

#### `co-luhn-pass` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-luhn-1m` | 1,000,017 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 642,826.5 | 0.6428 |
| `co-luhn-1m` | 1,000,017 | `pcrec_614d45eb3_auto-caps-simdna` | 643,297.3 | 0.6433 |
| `co-luhn-1m` | 1,000,017 | `pcrec_614d45eb3_vm-caps-simdna` | 644,266.1 | 0.6443 |
| `co-luhn-1m` | 1,000,017 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 650,518.0 | 0.6505 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 799,422.7 | 0.7994 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_jit-caps-simdna` | 872,709.4 | 0.8727 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 2,577,656.6 | 2.5776 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_interp-caps-simdna` | 2,604,152.5 | 2.6041 |
| `co-luhn-1m` | 1,000,017 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 3,949,298.5 | 3.9492 |
| `co-luhn-1m` | 1,000,017 | `oniguruma_6.9.10_default-caps-simdna` | 4,210,924.8 | 4.2109 |

### `co-luhn-twin` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 540,695.5 | 0.5407 | 536,142.2 | 542,878.2 | 2,395.5 | 0.218x | 1.000x | scratch |
| 2 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 561,497.6 | 0.5615 | 559,880.0 | 563,138.1 | 1,047.1 | 0.226x | 1.038x | scratch |
| 3 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 732,666.6 | 0.7327 | 728,155.3 | 746,478.9 | 6,373.7 | 0.295x | 1.355x | scratch |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 789,318.8 | 0.7893 | 781,784.3 | 795,409.6 | 4,323.0 | 0.318x | 1.460x | scratch |
| 5 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 994,646.6 | 0.9946 | 992,435.3 | 1,004,202.2 | 4,150.4 | 0.401x | 1.840x | scratch |
| 6 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 1,013,493.7 | 1.0135 | 999,851.7 | 1,023,699.2 | 8,458.7 | 0.409x | 1.874x | scratch |
| 7 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 2,480,988.0 | 2.4809 | 2,465,701.5 | 2,505,052.3 | 13,283.0 | 1.000x | 4.589x | scratch |
| 8 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 2,509,192.4 | 2.5091 | 2,467,906.5 | 2,549,488.3 | 29,890.1 | 1.011x | 4.641x | scratch |
| 9 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,755,514.1 | 2.7555 | 2,727,443.6 | 2,779,020.1 | 18,122.7 | 1.111x | 5.096x | scratch |
| 10 | `re2_11.0.0_default-caps-simdna_assist-v01` | measured | `plain` | same program | 2,767,071.2 | 2.7670 | 2,756,052.3 | 2,778,209.9 | 8,093.6 | 1.115x | 5.118x | scratch |
| 11 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,696,168.4 | 3.6961 | 3,655,311.4 | 3,728,329.7 | 26,631.3 | 1.490x | 6.836x | scratch |
| 12 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 3,701,469.7 | 3.7014 | 3,640,949.2 | 3,772,283.9 | 42,521.8 | 1.492x | 6.846x | scratch |

#### `co-luhn-twin` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-luhn-1m` | 1,000,017 | `pcrec_614d45eb3_vm-caps-simdna` | 540,695.5 | 0.5407 |
| `co-luhn-1m` | 1,000,017 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 561,497.6 | 0.5615 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 732,666.6 | 0.7327 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_jit-caps-simdna` | 789,318.8 | 0.7893 |
| `co-luhn-1m` | 1,000,017 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 994,646.6 | 0.9946 |
| `co-luhn-1m` | 1,000,017 | `pcrec_614d45eb3_auto-caps-simdna` | 1,013,493.7 | 1.0135 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_interp-caps-simdna` | 2,480,988.0 | 2.4809 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 2,509,192.4 | 2.5091 |
| `co-luhn-1m` | 1,000,017 | `re2_11.0.0_default-caps-simdna` | 2,755,514.1 | 2.7555 |
| `co-luhn-1m` | 1,000,017 | `re2_11.0.0_default-caps-simdna_assist-v01` | 2,767,071.2 | 2.7670 |
| `co-luhn-1m` | 1,000,017 | `oniguruma_6.9.10_default-caps-simdna` | 3,696,168.4 | 3.6961 |
| `co-luhn-1m` | 1,000,017 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 3,701,469.7 | 3.7014 |

### `co-member` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna_lim-ceil1g (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 478,418.4 | 0.4784 | 476,328.0 | 479,338.1 | 1,334.1 | 0.322x | 1.000x | scratch |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 512,783.3 | 0.5127 | 502,540.2 | 516,597.6 | 5,102.2 | 0.345x | 1.072x | scratch |
| 3 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 752,556.3 | 0.7525 | 747,823.2 | 759,366.6 | 3,784.7 | 0.507x | 1.573x | scratch |
| 4 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 762,092.9 | 0.7620 | 758,493.6 | 773,134.0 | 5,577.3 | 0.513x | 1.593x | scratch |
| 5 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 768,798.6 | 0.7687 | 767,550.7 | 770,740.6 | 1,237.1 | 0.518x | 1.607x | scratch |
| 6 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 784,293.0 | 0.7842 | 768,030.3 | 823,946.2 | 19,544.9 | 0.528x | 1.639x | scratch |
| 7 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 1,484,705.9 | 1.4846 | 1,479,882.6 | 1,490,540.4 | 4,612.3 | 1.000x | 3.103x | scratch |
| 8 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 1,487,589.7 | 1.4875 | 1,485,726.8 | 1,499,804.6 | 5,069.5 | 1.002x | 3.109x | scratch |
| 9 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,752,373.7 | 1.7523 | 1,692,577.7 | 1,770,183.6 | 30,664.8 | 1.180x | 3.663x | scratch |
| 10 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 1,752,622.1 | 1.7525 | 1,705,774.9 | 1,976,029.3 | 98,172.8 | 1.180x | 3.663x | scratch |
| 11 | `re2_11.0.0_default-caps-simdna_assist-v01` | measured | `plain` | same program | 2,966,039.1 | 2.9658 | 2,954,936.9 | 3,068,304.9 | 42,995.6 | 1.998x | 6.200x | scratch |

#### `co-member` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 478,418.4 | 0.4784 |
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_jit-caps-simdna` | 512,783.3 | 0.5127 |
| `co-member-1m` | 1,000,066 | `pcrec_614d45eb3_auto-caps-simdna` | 752,556.3 | 0.7525 |
| `co-member-1m` | 1,000,066 | `pcrec_614d45eb3_vm-caps-simdna` | 762,092.9 | 0.7620 |
| `co-member-1m` | 1,000,066 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 768,798.6 | 0.7687 |
| `co-member-1m` | 1,000,066 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 784,293.0 | 0.7842 |
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 1,484,705.9 | 1.4846 |
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_interp-caps-simdna` | 1,487,589.7 | 1.4875 |
| `co-member-1m` | 1,000,066 | `oniguruma_6.9.10_default-caps-simdna` | 1,752,373.7 | 1.7523 |
| `co-member-1m` | 1,000,066 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 1,752,622.1 | 1.7525 |
| `co-member-1m` | 1,000,066 | `re2_11.0.0_default-caps-simdna_assist-v01` | 2,966,039.1 | 2.9658 |

### `co-member-nofn` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 395,978.8 | 0.3960 | 393,462.1 | 409,641.5 | 5,823.4 | 0.308x | 1.000x | scratch |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 456,346.8 | 0.4563 | 453,309.7 | 475,317.8 | 7,959.6 | 0.355x | 1.152x | scratch |
| 3 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 1,285,903.9 | 1.2858 | 1,279,240.3 | 1,294,583.5 | 6,394.8 | 1.000x | 3.247x | scratch |
| 4 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 1,293,456.5 | 1.2934 | 1,286,579.3 | 1,307,234.0 | 7,083.0 | 1.006x | 3.266x | scratch |

#### `co-member-nofn` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 395,978.8 | 0.3960 |
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_jit-caps-simdna` | 456,346.8 | 0.4563 |
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_interp-caps-simdna` | 1,285,903.9 | 1.2858 |
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 1,293,456.5 | 1.2934 |

### `co-member-pass` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 435,502.1 | 0.4355 | 433,016.3 | 448,448.9 | 6,878.8 | 0.325x | 1.000x | scratch |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 502,362.3 | 0.5023 | 496,777.5 | 536,109.0 | 14,534.1 | 0.375x | 1.154x | scratch |
| 3 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 638,428.2 | 0.6384 | 631,674.7 | 639,679.7 | 2,926.0 | 0.476x | 1.466x | scratch |
| 4 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 641,940.0 | 0.6419 | 638,540.0 | 655,377.6 | 6,657.6 | 0.479x | 1.474x | scratch |
| 5 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 643,251.5 | 0.6432 | 641,452.8 | 656,206.5 | 5,432.7 | 0.480x | 1.477x | scratch |
| 6 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 655,571.4 | 0.6555 | 646,503.7 | 659,351.9 | 4,388.9 | 0.489x | 1.505x | scratch |
| 7 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 1,340,840.0 | 1.3408 | 1,328,681.2 | 1,342,014.2 | 5,041.5 | 1.000x | 3.079x | scratch |
| 8 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 1,359,582.4 | 1.3595 | 1,352,327.4 | 1,364,611.9 | 4,062.4 | 1.014x | 3.122x | scratch |
| 9 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 2,139,134.1 | 2.1390 | 2,035,381.5 | 2,183,738.2 | 54,340.4 | 1.595x | 4.912x | scratch |
| 10 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,147,692.4 | 2.1476 | 2,030,104.2 | 2,216,353.5 | 75,680.9 | 1.602x | 4.932x | scratch |

#### `co-member-pass` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 435,502.1 | 0.4355 |
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_jit-caps-simdna` | 502,362.3 | 0.5023 |
| `co-member-1m` | 1,000,066 | `pcrec_614d45eb3_auto-caps-simdna` | 638,428.2 | 0.6384 |
| `co-member-1m` | 1,000,066 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 641,940.0 | 0.6419 |
| `co-member-1m` | 1,000,066 | `pcrec_614d45eb3_vm-caps-simdna` | 643,251.5 | 0.6432 |
| `co-member-1m` | 1,000,066 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 655,571.4 | 0.6555 |
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_interp-caps-simdna` | 1,340,840.0 | 1.3408 |
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 1,359,582.4 | 1.3595 |
| `co-member-1m` | 1,000,066 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 2,139,134.1 | 2.1390 |
| `co-member-1m` | 1,000,066 | `oniguruma_6.9.10_default-caps-simdna` | 2,147,692.4 | 2.1476 |

### `co-member-twin` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna_lim-ceil1g (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 373,398.4 | 0.3734 | 373,174.7 | 382,487.0 | 3,599.4 | 0.294x | 1.000x | scratch |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 433,125.2 | 0.4331 | 433,007.3 | 446,633.9 | 5,274.4 | 0.341x | 1.160x | scratch |
| 3 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 482,319.2 | 0.4823 | 481,295.7 | 483,545.9 | 734.6 | 0.379x | 1.292x | scratch |
| 4 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 508,887.6 | 0.5089 | 508,375.7 | 511,784.0 | 1,305.5 | 0.400x | 1.363x | scratch |
| 5 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 587,416.6 | 0.5874 | 586,707.2 | 616,278.5 | 11,331.3 | 0.462x | 1.573x | scratch |
| 6 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 588,418.3 | 0.5884 | 585,451.3 | 591,132.9 | 2,080.3 | 0.463x | 1.576x | scratch |
| 7 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 1,272,013.5 | 1.2719 | 1,255,983.0 | 1,294,093.9 | 13,724.4 | 1.000x | 3.407x | scratch |
| 8 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 1,282,663.7 | 1.2826 | 1,268,679.2 | 1,293,903.6 | 10,068.6 | 1.008x | 3.435x | scratch |
| 9 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 1,802,930.0 | 1.8028 | 1,785,366.2 | 2,294,328.8 | 198,880.1 | 1.417x | 4.828x | scratch |
| 10 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,803,318.1 | 1.8032 | 1,736,501.8 | 1,837,967.5 | 38,832.2 | 1.418x | 4.829x | scratch |
| 11 | `re2_11.0.0_default-caps-simdna_assist-v01` | measured | `plain` | same program | 2,670,130.4 | 2.6700 | 2,665,627.2 | 2,682,649.8 | 7,404.1 | 2.099x | 7.151x | scratch |
| 12 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,694,436.6 | 2.6943 | 2,678,994.6 | 2,707,397.6 | 9,112.9 | 2.118x | 7.216x | scratch |

#### `co-member-twin` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 373,398.4 | 0.3734 |
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_jit-caps-simdna` | 433,125.2 | 0.4331 |
| `co-member-1m` | 1,000,066 | `pcrec_614d45eb3_auto-caps-simdna` | 482,319.2 | 0.4823 |
| `co-member-1m` | 1,000,066 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 508,887.6 | 0.5089 |
| `co-member-1m` | 1,000,066 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 587,416.6 | 0.5874 |
| `co-member-1m` | 1,000,066 | `pcrec_614d45eb3_vm-caps-simdna` | 588,418.3 | 0.5884 |
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 1,272,013.5 | 1.2719 |
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_interp-caps-simdna` | 1,282,663.7 | 1.2826 |
| `co-member-1m` | 1,000,066 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 1,802,930.0 | 1.8028 |
| `co-member-1m` | 1,000,066 | `oniguruma_6.9.10_default-caps-simdna` | 1,803,318.1 | 1.8032 |
| `co-member-1m` | 1,000,066 | `re2_11.0.0_default-caps-simdna_assist-v01` | 2,670,130.4 | 2.6700 |
| `co-member-1m` | 1,000,066 | `re2_11.0.0_default-caps-simdna` | 2,694,436.6 | 2.6943 |

### `co-netstr` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_614d45eb3_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 1,513,115.4 | 1.5131 | 1,511,862.7 | 1,555,233.0 | 17,074.9 | 1.000x | 1.000x | scratch |
| 2 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 1,518,378.5 | 1.5183 | 1,516,875.4 | 1,521,809.4 | 1,890.2 | 1.003x | 1.003x | scratch |
| 3 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 1,534,868.6 | 1.5348 | 1,531,321.3 | 1,600,838.8 | 26,865.9 | 1.014x | 1.014x | scratch |
| 4 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 1,539,114.4 | 1.5391 | 1,534,249.0 | 1,544,708.4 | 3,880.0 | 1.017x | 1.017x | scratch |
| 5 | `re2_11.0.0_default-caps-simdna_assist-v01` | measured | `plain` | same program | 3,907,307.0 | 3.9072 | 3,867,652.2 | 3,953,516.6 | 32,588.9 | 2.582x | 2.582x | scratch |
| 6 | `oniguruma_6.9.10_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 16,235,296.0 | 16.2349 | 16,111,107.0 | 16,425,386.8 | 113,568.1 | 10.730x | 10.730x | scratch |
| 7 | `libpcre2_10.46_jit-caps-simdna_assist-v01` | measured | `plain` | same program | 19,550,667.7 | 19.5502 | 19,237,958.3 | 19,757,801.3 | 194,147.6 | 12.921x | 12.921x | scratch |

#### `co-netstr` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-netstr-1m` | 1,000,025 | `pcrec_614d45eb3_auto-caps-simdna` | 1,513,115.4 | 1.5131 |
| `co-netstr-1m` | 1,000,025 | `pcrec_614d45eb3_vm-caps-simdna` | 1,518,378.5 | 1.5183 |
| `co-netstr-1m` | 1,000,025 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 1,534,868.6 | 1.5348 |
| `co-netstr-1m` | 1,000,025 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 1,539,114.4 | 1.5391 |
| `co-netstr-1m` | 1,000,025 | `re2_11.0.0_default-caps-simdna_assist-v01` | 3,907,307.0 | 3.9072 |
| `co-netstr-1m` | 1,000,025 | `oniguruma_6.9.10_default-caps-simdna_assist-v01` | 16,235,296.0 | 16.2349 |
| `co-netstr-1m` | 1,000,025 | `libpcre2_10.46_jit-caps-simdna_assist-v01` | 19,550,667.7 | 19.5502 |

### `co-netstr-assist` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 7,702,979.7 | 7.7028 | 7,685,621.3 | 7,800,244.4 | 43,592.0 | 0.360x | 1.000x | scratch |
| 2 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 7,909,603.1 | 7.9094 | 7,884,377.0 | 8,300,591.3 | 157,432.5 | 0.370x | 1.027x | scratch |
| 3 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 7,958,042.4 | 7.9578 | 7,892,646.3 | 8,208,331.1 | 108,466.7 | 0.372x | 1.033x | scratch |
| 4 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 8,037,329.6 | 8.0371 | 7,879,937.3 | 8,171,827.3 | 93,525.4 | 0.376x | 1.043x | scratch |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 8,144,725.0 | 8.1445 | 8,068,365.3 | 8,454,869.4 | 141,729.2 | 0.381x | 1.057x | scratch |
| 6 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 8,269,661.2 | 8.2695 | 8,190,962.8 | 8,416,913.5 | 85,701.4 | 0.387x | 1.074x | scratch |
| 7 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 21,382,881.7 | 21.3823 | 21,331,114.3 | 21,537,813.3 | 69,816.8 | 1.000x | 2.776x | scratch |
| 8 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 21,821,189.0 | 21.8206 | 21,671,132.7 | 22,097,479.7 | 151,816.9 | 1.020x | 2.833x | scratch |
| 9 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 22,511,386.0 | 22.5108 | 22,312,300.7 | 22,666,705.3 | 135,614.7 | 1.053x | 2.922x | scratch |
| 10 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 22,756,958.3 | 22.7564 | 22,369,107.7 | 24,174,807.0 | 637,841.2 | 1.064x | 2.954x | scratch |

#### `co-netstr-assist` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-netstr-1m` | 1,000,025 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 7,702,979.7 | 7.7028 |
| `co-netstr-1m` | 1,000,025 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 7,909,603.1 | 7.9094 |
| `co-netstr-1m` | 1,000,025 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 7,958,042.4 | 7.9578 |
| `co-netstr-1m` | 1,000,025 | `pcrec_614d45eb3_auto-caps-simdna` | 8,037,329.6 | 8.0371 |
| `co-netstr-1m` | 1,000,025 | `libpcre2_10.46_jit-caps-simdna` | 8,144,725.0 | 8.1445 |
| `co-netstr-1m` | 1,000,025 | `pcrec_614d45eb3_vm-caps-simdna` | 8,269,661.2 | 8.2695 |
| `co-netstr-1m` | 1,000,025 | `libpcre2_10.46_interp-caps-simdna` | 21,382,881.7 | 21.3823 |
| `co-netstr-1m` | 1,000,025 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 21,821,189.0 | 21.8206 |
| `co-netstr-1m` | 1,000,025 | `oniguruma_6.9.10_default-caps-simdna` | 22,511,386.0 | 22.5108 |
| `co-netstr-1m` | 1,000,025 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 22,756,958.3 | 22.7564 |

### `co-netstr-twin` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna_lim-ceil1g (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 1,044,151.8 | 1.0441 | 1,041,577.0 | 1,049,020.1 | 2,630.7 | 0.070x | 1.000x | scratch |
| 2 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 1,074,069.7 | 1.0740 | 1,068,230.0 | 1,077,663.4 | 3,685.9 | 0.072x | 1.029x | scratch |
| 3 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 3,346,164.1 | 3.3461 | 3,341,627.3 | 3,350,006.2 | 3,118.9 | 0.224x | 3.205x | scratch |
| 4 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 3,612,883.4 | 3.6128 | 3,601,897.6 | 3,619,575.3 | 7,559.6 | 0.242x | 3.460x | scratch |
| 5 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 3,687,248.9 | 3.6872 | 3,669,114.1 | 3,696,766.8 | 9,043.2 | 0.247x | 3.531x | scratch |
| 6 | `libpcre2_10.46_jit-caps-simdna_assist-v01` | measured | `plain` | same program | 3,743,955.1 | 3.7439 | 3,739,877.4 | 3,753,903.0 | 5,052.4 | 0.251x | 3.586x | scratch |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,745,505.9 | 3.7454 | 3,736,952.6 | 3,766,312.9 | 10,371.9 | 0.251x | 3.587x | scratch |
| 8 | `re2_11.0.0_default-caps-simdna_assist-v01` | measured | `plain` | same program | 4,030,107.6 | 4.0300 | 3,998,457.9 | 4,070,136.3 | 23,310.7 | 0.270x | 3.860x | scratch |
| 9 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 4,050,126.8 | 4.0500 | 4,002,769.3 | 4,127,894.2 | 41,110.8 | 0.271x | 3.879x | scratch |
| 10 | `oniguruma_6.9.10_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 6,780,968.0 | 6.7808 | 6,630,989.6 | 6,899,525.6 | 103,046.5 | 0.454x | 6.494x | scratch |
| 11 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 6,852,676.2 | 6.8525 | 6,703,159.5 | 6,975,197.1 | 108,588.9 | 0.459x | 6.563x | scratch |
| 12 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 6,865,097.4 | 6.8649 | 6,719,142.4 | 6,975,318.9 | 90,570.3 | 0.460x | 6.575x | scratch |
| 13 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 14,922,929.8 | 14.9226 | 14,848,953.0 | 15,254,855.5 | 151,088.8 | 1.000x | 14.292x | scratch |
| 14 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 15,059,456.8 | 15.0591 | 14,994,121.2 | 15,137,070.5 | 48,717.3 | 1.009x | 14.423x | scratch |

#### `co-netstr-twin` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-netstr-1m` | 1,000,025 | `pcrec_614d45eb3_auto-caps-simdna` | 1,044,151.8 | 1.0441 |
| `co-netstr-1m` | 1,000,025 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 1,074,069.7 | 1.0740 |
| `co-netstr-1m` | 1,000,025 | `pcrec_614d45eb3_vm-caps-simdna` | 3,346,164.1 | 3.3461 |
| `co-netstr-1m` | 1,000,025 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 3,612,883.4 | 3.6128 |
| `co-netstr-1m` | 1,000,025 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 3,687,248.9 | 3.6872 |
| `co-netstr-1m` | 1,000,025 | `libpcre2_10.46_jit-caps-simdna_assist-v01` | 3,743,955.1 | 3.7439 |
| `co-netstr-1m` | 1,000,025 | `libpcre2_10.46_jit-caps-simdna` | 3,745,505.9 | 3.7454 |
| `co-netstr-1m` | 1,000,025 | `re2_11.0.0_default-caps-simdna_assist-v01` | 4,030,107.6 | 4.0300 |
| `co-netstr-1m` | 1,000,025 | `re2_11.0.0_default-caps-simdna` | 4,050,126.8 | 4.0500 |
| `co-netstr-1m` | 1,000,025 | `oniguruma_6.9.10_default-caps-simdna_assist-v01` | 6,780,968.0 | 6.7808 |
| `co-netstr-1m` | 1,000,025 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 6,852,676.2 | 6.8525 |
| `co-netstr-1m` | 1,000,025 | `oniguruma_6.9.10_default-caps-simdna` | 6,865,097.4 | 6.8649 |
| `co-netstr-1m` | 1,000,025 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 14,922,929.8 | 14.9226 |
| `co-netstr-1m` | 1,000,025 | `libpcre2_10.46_interp-caps-simdna` | 15,059,456.8 | 15.0591 |

### `cscan` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_jit-caps-simdna_lim-ceil1g (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 17,303,336.0 | 1.3562 | 17,138,804.2 | 17,544,569.9 | 158,475.3 | 1.000x | 1.000x | 23 | 100% | scratch |
| 2 | `re2_11.0.0_default-caps-simdna_assist-v01` | measured | `plain` | same program | 59,873,401.5 | 4.6927 | 59,594,816.1 | 60,063,596.6 | 187,397.7 | 3.460x | 3.460x | 23 | 100% | scratch |

#### `cscan` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `comment-5m` | 5,000,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 3,511,852.3 | 0.7024 |
| `comment-5m` | 5,000,011 | `re2_11.0.0_default-caps-simdna_assist-v01` | 10,332,625.7 | 2.0665 |
| `define-witness` | 12 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 60.9 | 5.0754 |
| `define-witness` | 12 | `re2_11.0.0_default-caps-simdna_assist-v01` | 191.3 | 15.9409 |
| `idents-1m` | 1,000,007 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 3,563,813.4 | 3.5638 |
| `idents-1m` | 1,000,007 | `re2_11.0.0_default-caps-simdna_assist-v01` | 10,478,005.6 | 10.4779 |
| `literal-100k` | 100,014 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 49,585.9 | 0.4958 |
| `literal-100k` | 100,014 | `re2_11.0.0_default-caps-simdna_assist-v01` | 199,505.0 | 1.9948 |
| `nest-brace-100k` | 200,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 2,462,709.2 | 12.3129 |
| `nest-brace-100k` | 200,011 | `re2_11.0.0_default-caps-simdna_assist-v01` | 15,603,286.6 | 78.0121 |
| `nest-brace-10k` | 20,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 224,169.9 | 11.2023 |
| `nest-brace-10k` | 20,011 | `re2_11.0.0_default-caps-simdna_assist-v01` | 1,556,786.1 | 77.7965 |
| `nest-brace-128` | 267 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 2,736.0 | 10.2472 |
| `nest-brace-128` | 267 | `re2_11.0.0_default-caps-simdna_assist-v01` | 19,969.9 | 74.7937 |
| `nest-brace-1k` | 2,059 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 21,931.2 | 10.6514 |
| `nest-brace-1k` | 2,059 | `re2_11.0.0_default-caps-simdna_assist-v01` | 160,112.9 | 77.7624 |
| `nest-brace-2k` | 4,107 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 44,617.5 | 10.8638 |
| `nest-brace-2k` | 4,107 | `re2_11.0.0_default-caps-simdna_assist-v01` | 318,759.6 | 77.6137 |
| `nest-brace-32k` | 65,547 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 762,226.2 | 11.6287 |
| `nest-brace-32k` | 65,547 | `re2_11.0.0_default-caps-simdna_assist-v01` | 5,100,860.2 | 77.8199 |
| `nest-brace-512` | 1,035 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 10,938.8 | 10.5689 |
| `nest-brace-512` | 1,035 | `re2_11.0.0_default-caps-simdna_assist-v01` | 79,610.7 | 76.9186 |
| `nest-brace-8k` | 16,395 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 183,211.6 | 11.1748 |
| `nest-brace-8k` | 16,395 | `re2_11.0.0_default-caps-simdna_assist-v01` | 1,274,591.0 | 77.7427 |
| `nest-digraph-10k` | 40,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 302,792.5 | 7.5677 |
| `nest-digraph-10k` | 40,011 | `re2_11.0.0_default-caps-simdna_assist-v01` | 1,609,077.3 | 40.2159 |
| `nest-paren-100k` | 200,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 1,077,442.4 | 5.3869 |
| `nest-paren-100k` | 200,011 | `re2_11.0.0_default-caps-simdna_assist-v01` | 406,510.9 | 2.0324 |
| `nest-paren-10k` | 20,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 107,714.3 | 5.3828 |
| `nest-paren-10k` | 20,011 | `re2_11.0.0_default-caps-simdna_assist-v01` | 40,743.1 | 2.0360 |
| `nest-paren-128` | 267 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 1,455.0 | 5.4494 |
| `nest-paren-128` | 267 | `re2_11.0.0_default-caps-simdna_assist-v01` | 724.0 | 2.7117 |
| `nest-paren-1k` | 2,059 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 11,017.8 | 5.3510 |
| `nest-paren-1k` | 2,059 | `re2_11.0.0_default-caps-simdna_assist-v01` | 4,442.5 | 2.1576 |
| `nest-paren-2k` | 4,107 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 22,083.7 | 5.3771 |
| `nest-paren-2k` | 4,107 | `re2_11.0.0_default-caps-simdna_assist-v01` | 8,558.1 | 2.0838 |
| `nest-paren-32k` | 65,547 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 352,939.4 | 5.3845 |
| `nest-paren-32k` | 65,547 | `re2_11.0.0_default-caps-simdna_assist-v01` | 132,728.0 | 2.0249 |
| `nest-paren-512` | 1,035 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 5,470.5 | 5.2855 |
| `nest-paren-512` | 1,035 | `re2_11.0.0_default-caps-simdna_assist-v01` | 2,320.5 | 2.2421 |
| `nest-paren-8k` | 16,395 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 88,249.0 | 5.3827 |
| `nest-paren-8k` | 16,395 | `re2_11.0.0_default-caps-simdna_assist-v01` | 33,632.2 | 2.0514 |
| `splice-1m` | 1,000,009 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 901,717.1 | 0.9017 |
| `splice-1m` | 1,000,009 | `re2_11.0.0_default-caps-simdna_assist-v01` | 2,068,453.5 | 2.0684 |
| `unterminated-5m` | 5,000,006 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 3,542,527.7 | 0.7085 |
| `unterminated-5m` | 5,000,006 | `re2_11.0.0_default-caps-simdna_assist-v01` | 10,348,372.6 | 2.0697 |

### `cscan-onig` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_jit-caps-simdna_lim-ceil1g (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 17,222,071.1 | 1.3498 | 17,164,751.5 | 17,498,695.6 | 122,450.4 | 1.000x | 1.000x | 23 | 100% | scratch |
| 2 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 47,856,813.6 | 3.7508 | 47,748,729.2 | 49,304,496.2 | 623,245.0 | 2.779x | 2.779x | 23 | 100% | scratch |
| 3 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 47,948,253.3 | 3.7580 | 47,865,359.9 | 49,571,982.7 | 751,182.7 | 2.784x | 2.784x | 23 | 100% | scratch |

#### `cscan-onig` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `comment-5m` | 5,000,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 3,513,364.4 | 0.7027 |
| `comment-5m` | 5,000,011 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 8,303,757.9 | 1.6607 |
| `comment-5m` | 5,000,011 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 8,304,739.2 | 1.6609 |
| `define-witness` | 12 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 60.6 | 5.0507 |
| `define-witness` | 12 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 116.4 | 9.7000 |
| `define-witness` | 12 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 115.7 | 9.6426 |
| `idents-1m` | 1,000,007 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 3,556,315.5 | 3.5563 |
| `idents-1m` | 1,000,007 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 10,569,101.5 | 10.5690 |
| `idents-1m` | 1,000,007 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 10,509,199.8 | 10.5091 |
| `literal-100k` | 100,014 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 49,656.1 | 0.4965 |
| `literal-100k` | 100,014 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 30,383.5 | 0.3038 |
| `literal-100k` | 100,014 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 30,417.9 | 0.3041 |
| `nest-brace-100k` | 200,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 2,433,784.4 | 12.1683 |
| `nest-brace-100k` | 200,011 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 11,638,861.1 | 58.1911 |
| `nest-brace-100k` | 200,011 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 11,729,506.2 | 58.6443 |
| `nest-brace-10k` | 20,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 226,821.3 | 11.3348 |
| `nest-brace-10k` | 20,011 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 906,270.2 | 45.2886 |
| `nest-brace-10k` | 20,011 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 906,356.1 | 45.2929 |
| `nest-brace-128` | 267 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 2,739.1 | 10.2587 |
| `nest-brace-128` | 267 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 11,468.5 | 42.9533 |
| `nest-brace-128` | 267 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 11,471.2 | 42.9632 |
| `nest-brace-1k` | 2,059 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 22,069.3 | 10.7185 |
| `nest-brace-1k` | 2,059 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 90,829.7 | 44.1135 |
| `nest-brace-1k` | 2,059 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 90,953.5 | 44.1736 |
| `nest-brace-2k` | 4,107 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 46,319.2 | 11.2781 |
| `nest-brace-2k` | 4,107 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 183,570.7 | 44.6970 |
| `nest-brace-2k` | 4,107 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 183,416.3 | 44.6594 |
| `nest-brace-32k` | 65,547 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 771,484.3 | 11.7699 |
| `nest-brace-32k` | 65,547 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 3,175,031.7 | 48.4390 |
| `nest-brace-32k` | 65,547 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 3,173,440.4 | 48.4147 |
| `nest-brace-512` | 1,035 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 10,965.8 | 10.5950 |
| `nest-brace-512` | 1,035 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 44,855.2 | 43.3383 |
| `nest-brace-512` | 1,035 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 45,289.0 | 43.7574 |
| `nest-brace-8k` | 16,395 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 185,692.9 | 11.3262 |
| `nest-brace-8k` | 16,395 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 741,517.3 | 45.2283 |
| `nest-brace-8k` | 16,395 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 740,543.1 | 45.1688 |
| `nest-digraph-10k` | 40,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 306,166.4 | 7.6521 |
| `nest-digraph-10k` | 40,011 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 1,207,715.3 | 30.1846 |
| `nest-digraph-10k` | 40,011 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 1,208,481.9 | 30.2037 |
| `nest-paren-100k` | 200,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 1,041,359.8 | 5.2065 |
| `nest-paren-100k` | 200,011 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 5,691,487.4 | 28.4559 |
| `nest-paren-100k` | 200,011 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 5,689,467.4 | 28.4458 |
| `nest-paren-10k` | 20,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 105,164.3 | 5.2553 |
| `nest-paren-10k` | 20,011 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 571,861.9 | 28.5774 |
| `nest-paren-10k` | 20,011 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 565,539.7 | 28.2614 |
| `nest-paren-128` | 267 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 1,432.7 | 5.3657 |
| `nest-paren-128` | 267 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 7,397.9 | 27.7076 |
| `nest-paren-128` | 267 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 7,353.3 | 27.5405 |
| `nest-paren-1k` | 2,059 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 10,756.3 | 5.2241 |
| `nest-paren-1k` | 2,059 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 57,828.6 | 28.0858 |
| `nest-paren-1k` | 2,059 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 58,000.4 | 28.1692 |
| `nest-paren-2k` | 4,107 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 21,408.5 | 5.2127 |
| `nest-paren-2k` | 4,107 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 115,449.1 | 28.1103 |
| `nest-paren-2k` | 4,107 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 115,427.4 | 28.1050 |
| `nest-paren-32k` | 65,547 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 341,330.0 | 5.2074 |
| `nest-paren-32k` | 65,547 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 1,860,850.3 | 28.3896 |
| `nest-paren-32k` | 65,547 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 1,860,166.7 | 28.3791 |
| `nest-paren-512` | 1,035 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 5,440.5 | 5.2566 |
| `nest-paren-512` | 1,035 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 29,111.0 | 28.1265 |
| `nest-paren-512` | 1,035 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 29,187.1 | 28.2001 |
| `nest-paren-8k` | 16,395 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 85,493.4 | 5.2146 |
| `nest-paren-8k` | 16,395 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 463,900.0 | 28.2952 |
| `nest-paren-8k` | 16,395 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 463,440.0 | 28.2672 |
| `splice-1m` | 1,000,009 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 903,423.4 | 0.9034 |
| `splice-1m` | 1,000,009 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 2,265,681.7 | 2.2657 |
| `splice-1m` | 1,000,009 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 2,277,038.3 | 2.2770 |
| `unterminated-5m` | 5,000,006 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 3,536,080.9 | 0.7072 |
| `unterminated-5m` | 5,000,006 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 37,788.5 | 0.0076 |
| `unterminated-5m` | 5,000,006 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 37,495.7 | 0.0075 |

### `floor` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 139,835.6 | 0.0071 | 138,205.8 | 141,705.1 | 1,465.1 | 0.982x | 1.000x | scratch |
| 2 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 140,088.5 | 0.0071 | 138,546.3 | 141,172.5 | 955.4 | 0.984x | 1.002x | scratch |
| 3 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 140,627.8 | 0.0071 | 138,489.4 | 143,280.1 | 1,703.0 | 0.988x | 1.006x | scratch |
| 4 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 141,038.5 | 0.0071 | 140,258.3 | 143,666.8 | 1,372.0 | 0.990x | 1.009x | scratch |
| 5 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 142,397.0 | 0.0072 | 139,963.8 | 144,315.5 | 1,545.5 | 1.000x | 1.018x | scratch |
| 6 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 142,861.1 | 0.0072 | 140,317.9 | 143,700.9 | 1,173.0 | 1.003x | 1.022x | scratch |
| 7 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 472,702.1 | 0.0239 | 471,879.1 | 473,330.7 | 554.2 | 3.320x | 3.380x | scratch |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 473,671.1 | 0.0240 | 472,082.5 | 477,307.5 | 1,824.3 | 3.326x | 3.387x | scratch |
| 9 | `libpcre2_10.46_jit-caps-simdna_assist-v01` | measured | `plain` | same program | 474,295.1 | 0.0240 | 471,548.3 | 475,707.3 | 1,536.6 | 3.331x | 3.392x | scratch |
| 10 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 888,029.3 | 0.0449 | 887,468.3 | 904,192.9 | 6,534.3 | 6.236x | 6.351x | scratch |
| 11 | `re2_11.0.0_default-caps-simdna_assist-v01` | measured | `plain` | same program | 892,979.3 | 0.0452 | 886,403.7 | 895,629.6 | 3,253.9 | 6.271x | 6.386x | scratch |
| 12 | `oniguruma_6.9.10_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 10,164,232.1 | 0.5143 | 10,159,654.3 | 10,182,077.0 | 8,876.9 | 71.380x | 72.687x | scratch |
| 13 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 10,172,906.0 | 0.5148 | 10,156,038.7 | 10,177,391.1 | 7,499.8 | 71.440x | 72.749x | scratch |
| 14 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 10,176,447.8 | 0.5149 | 10,140,883.9 | 10,216,218.6 | 26,336.8 | 71.465x | 72.774x | scratch |
| 15 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 10,456,670.1 | 0.5291 | 10,419,453.2 | 10,487,491.4 | 26,368.7 | 73.433x | 74.778x | scratch |

_per-subject rows: 30 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `wild-json-validate` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna_lim-ceil1g (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 16,703,102.0 | 8.3461 | 16,645,889.2 | 16,809,953.5 | 62,823.2 | 0.030x | 1.000x | 2 | 100% | scratch |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 159,609,809.0 | 79.7532 | 159,495,323.0 | 159,958,085.0 | 159,344.9 | 0.288x | 9.556x | 2 | 100% | scratch |
| 3 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 162,513,085.0 | 81.2039 | 158,826,086.0 | 163,456,883.0 | 1,763,295.2 | 0.293x | 9.730x | 2 | 100% | scratch |
| 4 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 554,045,352.0 | 276.8433 | 552,511,162.0 | 557,785,080.0 | 1,787,571.7 | 1.000x | 33.170x | 2 | 100% | scratch |
| 5 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 558,494,936.0 | 279.0666 | 557,958,696.0 | 563,458,790.0 | 2,033,405.9 | 1.008x | 33.437x | 2 | 100% | scratch |

#### `wild-json-validate` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `js-1m` | 1,000,648 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 6,176,020.2 | 6.1720 |
| `js-1m` | 1,000,648 | `oniguruma_6.9.10_default-caps-simdna` | 75,577,453.0 | 75.5285 |
| `js-1m` | 1,000,648 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 76,762,468.0 | 76.7128 |
| `js-1m` | 1,000,648 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 453,666,608.0 | 453.3728 |
| `js-1m` | 1,000,648 | `libpcre2_10.46_interp-caps-simdna` | 457,086,648.0 | 456.7906 |
| `js-near-1m` | 1,000,648 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 10,547,445.0 | 10.5406 |
| `js-near-1m` | 1,000,648 | `oniguruma_6.9.10_default-caps-simdna` | 83,917,870.0 | 83.8635 |
| `js-near-1m` | 1,000,648 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 85,471,781.0 | 85.4164 |
| `js-near-1m` | 1,000,648 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 101,320,338.0 | 101.2547 |
| `js-near-1m` | 1,000,648 | `libpcre2_10.46_interp-caps-simdna` | 101,581,294.0 | 101.5155 |

### `wild-json-validate-onig` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna_lim-ceil1g (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 15,933,617.2 | 7.9616 | 15,888,619.8 | 16,118,157.2 | 80,142.6 | 0.029x | 1.000x | 2 | 100% | scratch |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 157,961,032.0 | 78.9294 | 157,355,259.0 | 158,778,291.0 | 554,684.5 | 0.283x | 9.914x | 2 | 100% | scratch |
| 3 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 160,400,332.0 | 80.1482 | 159,203,198.0 | 161,307,232.0 | 788,798.9 | 0.288x | 10.067x | 2 | 100% | scratch |
| 4 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 182,004,146.0 | 90.9431 | 181,494,285.0 | 183,211,202.0 | 580,780.0 | 0.326x | 11.423x | 2 | 100% | scratch |
| 5 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 185,127,598.0 | 92.5039 | 184,943,280.0 | 185,309,201.0 | 125,168.8 | 0.332x | 11.619x | 2 | 100% | scratch |
| 6 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 557,693,717.0 | 278.6663 | 556,710,997.0 | 559,811,028.0 | 1,297,990.2 | 1.000x | 35.001x | 2 | 100% | scratch |
| 7 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 559,619,606.0 | 279.6286 | 556,855,607.0 | 565,724,369.0 | 2,959,670.2 | 1.003x | 35.122x | 2 | 100% | scratch |

#### `wild-json-validate-onig` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `js-1m` | 1,000,648 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 5,941,378.0 | 5.9375 |
| `js-1m` | 1,000,648 | `oniguruma_6.9.10_default-caps-simdna` | 74,457,623.0 | 74.4094 |
| `js-1m` | 1,000,648 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 76,280,299.0 | 76.2309 |
| `js-1m` | 1,000,648 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 127,449,959.0 | 127.3674 |
| `js-1m` | 1,000,648 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 129,481,311.0 | 129.3975 |
| `js-1m` | 1,000,648 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 455,278,435.0 | 454.9836 |
| `js-1m` | 1,000,648 | `libpcre2_10.46_interp-caps-simdna` | 457,678,363.0 | 457.3820 |
| `js-near-1m` | 1,000,648 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 9,994,082.5 | 9.9876 |
| `js-near-1m` | 1,000,648 | `oniguruma_6.9.10_default-caps-simdna` | 83,588,379.0 | 83.5342 |
| `js-near-1m` | 1,000,648 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 84,401,183.0 | 84.3465 |
| `js-near-1m` | 1,000,648 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 54,614,200.0 | 54.5788 |
| `js-near-1m` | 1,000,648 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 55,810,928.0 | 55.7748 |
| `js-near-1m` | 1,000,648 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 102,415,282.0 | 102.3490 |
| `js-near-1m` | 1,000,648 | `libpcre2_10.46_interp-caps-simdna` | 101,515,400.0 | 101.4497 |

### `wild-sexp-balanced` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 2,799,122.1 | 2.1343 | 2,763,369.3 | 2,881,645.1 | 39,670.4 | 0.127x | 1.000x | 9 | 100% | scratch |
| 2 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 7,704,877.8 | 5.8750 | 7,549,259.0 | 7,806,010.7 | 83,000.6 | 0.349x | 2.753x | 9 | 100% | scratch |
| 3 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 7,818,758.6 | 5.9618 | 7,599,898.4 | 8,773,224.7 | 421,817.2 | 0.354x | 2.793x | 9 | 100% | scratch |
| 4 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 22,080,218.3 | 16.8362 | 21,975,061.3 | 22,911,029.9 | 361,530.4 | 1.000x | 7.888x | 9 | 100% | scratch |
| 5 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 22,411,283.6 | 17.0886 | 21,964,669.9 | 22,488,366.9 | 201,738.3 | 1.015x | 8.007x | 9 | 100% | scratch |
| 6 | `re2_11.0.0_default-caps-simdna_assist-v01` | measured | `plain` | same program | 41,176,556.8 | 31.3972 | 41,038,186.0 | 41,501,310.0 | 163,900.6 | 1.865x | 14.711x | 9 | 100% | scratch |
| 7 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 40,858,636,323.0 | 31154.7437 | 40,462,531,457.0 | 40,976,932,967.0 | 189,700,612.1 | 1850.463x | 14596.947x | 9 | 100% | scratch |

#### `wild-sexp-balanced` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `nest-paren-100k` | 200,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 802,917.9 | 4.0144 |
| `nest-paren-100k` | 200,011 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 2,553,433.2 | 12.7665 |
| `nest-paren-100k` | 200,011 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 2,633,713.2 | 13.1678 |
| `nest-paren-100k` | 200,011 | `libpcre2_10.46_interp-caps-simdna` | 7,912,901.3 | 39.5623 |
| `nest-paren-100k` | 200,011 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 8,083,571.6 | 40.4156 |
| `nest-paren-100k` | 200,011 | `re2_11.0.0_default-caps-simdna_assist-v01` | 15,881,486.1 | 79.4031 |
| `nest-paren-100k` | 200,011 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 36,181,126,700.0 | 180895.6842 |
| `nest-paren-10k` | 20,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 69,260.8 | 3.4611 |
| `nest-paren-10k` | 20,011 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 248,751.7 | 12.4308 |
| `nest-paren-10k` | 20,011 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 249,206.8 | 12.4535 |
| `nest-paren-10k` | 20,011 | `libpcre2_10.46_interp-caps-simdna` | 665,637.7 | 33.2636 |
| `nest-paren-10k` | 20,011 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 676,175.1 | 33.7902 |
| `nest-paren-10k` | 20,011 | `re2_11.0.0_default-caps-simdna_assist-v01` | 1,567,881.6 | 78.3510 |
| `nest-paren-10k` | 20,011 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 358,972,538.0 | 17938.7606 |
| `nest-paren-128` | 267 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 891.9 | 3.3406 |
| `nest-paren-128` | 267 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 3,128.5 | 11.7171 |
| `nest-paren-128` | 267 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 3,123.4 | 11.6982 |
| `nest-paren-128` | 267 | `libpcre2_10.46_interp-caps-simdna` | 9,775.2 | 36.6112 |
| `nest-paren-128` | 267 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 9,859.3 | 36.9261 |
| `nest-paren-128` | 267 | `re2_11.0.0_default-caps-simdna_assist-v01` | 29,543.6 | 110.6501 |
| `nest-paren-128` | 267 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 81,253.0 | 304.3184 |
| `nest-paren-1k` | 2,059 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 7,264.6 | 3.5282 |
| `nest-paren-1k` | 2,059 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 26,769.6 | 13.0013 |
| `nest-paren-1k` | 2,059 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 26,809.5 | 13.0207 |
| `nest-paren-1k` | 2,059 | `libpcre2_10.46_interp-caps-simdna` | 73,465.0 | 35.6800 |
| `nest-paren-1k` | 2,059 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 73,019.0 | 35.4633 |
| `nest-paren-1k` | 2,059 | `re2_11.0.0_default-caps-simdna_assist-v01` | 162,461.1 | 78.9029 |
| `nest-paren-1k` | 2,059 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 3,832,953.0 | 1861.5605 |
| `nest-paren-2k` | 4,107 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 14,165.9 | 3.4492 |
| `nest-paren-2k` | 4,107 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 51,485.1 | 12.5360 |
| `nest-paren-2k` | 4,107 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 51,499.9 | 12.5395 |
| `nest-paren-2k` | 4,107 | `libpcre2_10.46_interp-caps-simdna` | 143,684.8 | 34.9853 |
| `nest-paren-2k` | 4,107 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 143,303.1 | 34.8924 |
| `nest-paren-2k` | 4,107 | `re2_11.0.0_default-caps-simdna_assist-v01` | 317,205.9 | 77.2354 |
| `nest-paren-2k` | 4,107 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 15,188,202.0 | 3698.1256 |
| `nest-paren-32k` | 65,547 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 238,692.4 | 3.6415 |
| `nest-paren-32k` | 65,547 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 829,725.4 | 12.6585 |
| `nest-paren-32k` | 65,547 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 831,777.2 | 12.6898 |
| `nest-paren-32k` | 65,547 | `libpcre2_10.46_interp-caps-simdna` | 2,332,372.8 | 35.5832 |
| `nest-paren-32k` | 65,547 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 2,357,385.9 | 35.9648 |
| `nest-paren-32k` | 65,547 | `re2_11.0.0_default-caps-simdna_assist-v01` | 5,240,796.2 | 79.9548 |
| `nest-paren-32k` | 65,547 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 3,919,793,668.0 | 59801.2673 |
| `nest-paren-512` | 1,035 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 3,454.3 | 3.3375 |
| `nest-paren-512` | 1,035 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 12,753.0 | 12.3218 |
| `nest-paren-512` | 1,035 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 12,639.6 | 12.2122 |
| `nest-paren-512` | 1,035 | `libpcre2_10.46_interp-caps-simdna` | 36,675.1 | 35.4348 |
| `nest-paren-512` | 1,035 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 36,826.1 | 35.5808 |
| `nest-paren-512` | 1,035 | `re2_11.0.0_default-caps-simdna_assist-v01` | 80,713.2 | 77.9837 |
| `nest-paren-512` | 1,035 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 1,014,282.0 | 979.9826 |
| `nest-paren-8k` | 16,395 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 56,840.6 | 3.4669 |
| `nest-paren-8k` | 16,395 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 207,512.1 | 12.6570 |
| `nest-paren-8k` | 16,395 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 207,409.0 | 12.6508 |
| `nest-paren-8k` | 16,395 | `libpcre2_10.46_interp-caps-simdna` | 583,013.7 | 35.5605 |
| `nest-paren-8k` | 16,395 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 586,169.9 | 35.7530 |
| `nest-paren-8k` | 16,395 | `re2_11.0.0_default-caps-simdna_assist-v01` | 1,286,010.4 | 78.4392 |
| `nest-paren-8k` | 16,395 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 243,734,905.0 | 14866.4169 |
| `sx-1m` | 1,002,042 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 1,603,365.4 | 1.6001 |
| `sx-1m` | 1,002,042 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 3,764,438.1 | 3.7568 |
| `sx-1m` | 1,002,042 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 3,787,036.4 | 3.7793 |
| `sx-1m` | 1,002,042 | `libpcre2_10.46_interp-caps-simdna` | 10,326,483.1 | 10.3054 |
| `sx-1m` | 1,002,042 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 10,435,776.2 | 10.4145 |
| `sx-1m` | 1,002,042 | `re2_11.0.0_default-caps-simdna_assist-v01` | 16,615,023.4 | 16.5812 |
| `sx-1m` | 1,002,042 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 18,636,681.0 | 18.5987 |

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `cscan` | `large-subject-throughput` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 23 | 96% | 0 | 0 | `nest-brace-100k` (timed-out) |
| `cscan` | `large-subject-throughput` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 23 | 96% | 0 | 0 | `nest-brace-100k` (timed-out) |
| `cscan` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 23 | 65% | -46:JIT×8 (smallest: nest-brace-512, 1,035 B) | 0 | `nest-brace-100k` (gave-up), `nest-brace-10k` (gave-up), `nest-brace-1k` (gave-up), `nest-brace-2k` (gave-up), `nest-brace-32k` (gave-up), `nest-brace-512` (gave-up), `nest-brace-8k` (gave-up), `nest-digraph-10k` (gave-up) |
| `cscan` | `large-subject-throughput` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 23 | 57% | 0 | 50 | `define-witness` (wrong), `nest-brace-100k` (wrong), `nest-brace-10k` (wrong), `nest-brace-128` (wrong), `nest-brace-1k` (wrong), `nest-brace-2k` (wrong), `nest-brace-32k` (wrong), `nest-brace-512` (wrong), `nest-brace-8k` (wrong), `nest-digraph-10k` (wrong) |
| `cscan` | `large-subject-throughput` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 23 | 91% | 0 | 5 | `define-witness` (wrong), `nest-brace-100k` (timed-out) |
| `cscan-onig` | `large-subject-throughput` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 23 | 96% | 0 | 0 | `nest-brace-100k` (timed-out) |
| `cscan-onig` | `large-subject-throughput` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 23 | 96% | 0 | 0 | `nest-brace-100k` (timed-out) |
| `cscan-onig` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 23 | 65% | -46:JIT×8 (smallest: nest-brace-512, 1,035 B) | 0 | `nest-brace-100k` (gave-up), `nest-brace-10k` (gave-up), `nest-brace-1k` (gave-up), `nest-brace-2k` (gave-up), `nest-brace-32k` (gave-up), `nest-brace-512` (gave-up), `nest-brace-8k` (gave-up), `nest-digraph-10k` (gave-up) |
| `cscan-onig` | `large-subject-throughput` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 23 | 61% | 0 | 45 | `nest-brace-100k` (wrong), `nest-brace-10k` (wrong), `nest-brace-128` (wrong), `nest-brace-1k` (wrong), `nest-brace-2k` (wrong), `nest-brace-32k` (wrong), `nest-brace-512` (wrong), `nest-brace-8k` (wrong), `nest-digraph-10k` (wrong) |
| `cscan-onig` | `large-subject-throughput` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 23 | 96% | 0 | 0 | `nest-brace-100k` (timed-out) |
| `cscan-onig` | `large-subject-throughput` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 23 | 17% | -3:PCREC_ERR_FRAMES×19 (smallest: nest-brace-128, 267 B) | 0 | `comment-5m` (gave-up), `idents-1m` (gave-up), `nest-brace-100k` (gave-up), `nest-brace-10k` (gave-up), `nest-brace-128` (gave-up), `nest-brace-1k` (gave-up), `nest-brace-2k` (gave-up), `nest-brace-32k` (gave-up), `nest-brace-512` (gave-up), `nest-brace-8k` (gave-up), `nest-digraph-10k` (gave-up), `nest-paren-100k` (gave-up), `nest-paren-10k` (gave-up), `nest-paren-1k` (gave-up), `nest-paren-2k` (gave-up), `nest-paren-32k` (gave-up), `nest-paren-512` (gave-up), `nest-paren-8k` (gave-up), `splice-1m` (gave-up) |
| `cscan-onig` | `large-subject-throughput` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 23 | 17% | -3:PCREC_ERR_FRAMES×19 (smallest: nest-brace-128, 267 B) | 0 | `comment-5m` (gave-up), `idents-1m` (gave-up), `nest-brace-100k` (gave-up), `nest-brace-10k` (gave-up), `nest-brace-128` (gave-up), `nest-brace-1k` (gave-up), `nest-brace-2k` (gave-up), `nest-brace-32k` (gave-up), `nest-brace-512` (gave-up), `nest-brace-8k` (gave-up), `nest-digraph-10k` (gave-up), `nest-paren-100k` (gave-up), `nest-paren-10k` (gave-up), `nest-paren-1k` (gave-up), `nest-paren-2k` (gave-up), `nest-paren-32k` (gave-up), `nest-paren-512` (gave-up), `nest-paren-8k` (gave-up), `splice-1m` (gave-up) |
| `wild-json-validate` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 2 | 0% | -46:JIT×2 (smallest: js-1m, 1,000,648 B) | 0 | `js-1m` (gave-up), `js-near-1m` (gave-up) |
| `wild-json-validate-onig` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 2 | 0% | -46:JIT×2 (smallest: js-1m, 1,000,648 B) | 0 | `js-1m` (gave-up), `js-near-1m` (gave-up) |
| `wild-json-validate-onig` | `large-subject-throughput` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 2 | 0% | -3:PCREC_ERR_FRAMES×2 (smallest: js-1m, 1,000,648 B) | 0 | `js-1m` (gave-up), `js-near-1m` (gave-up) |
| `wild-json-validate-onig` | `large-subject-throughput` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 2 | 0% | -3:PCREC_ERR_FRAMES×2 (smallest: js-1m, 1,000,648 B) | 0 | `js-1m` (gave-up), `js-near-1m` (gave-up) |
| `wild-sexp-balanced` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 9 | 11% | -46:JIT×8 (smallest: nest-paren-512, 1,035 B) | 0 | `nest-paren-100k` (gave-up), `nest-paren-10k` (gave-up), `nest-paren-1k` (gave-up), `nest-paren-2k` (gave-up), `nest-paren-32k` (gave-up), `nest-paren-512` (gave-up), `nest-paren-8k` (gave-up), `sx-1m` (gave-up) |
| `wild-sexp-balanced` | `large-subject-throughput` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 9 | 11% | 0 | 40 | `nest-paren-100k` (wrong), `nest-paren-10k` (wrong), `nest-paren-128` (wrong), `nest-paren-1k` (wrong), `nest-paren-2k` (wrong), `nest-paren-32k` (wrong), `nest-paren-512` (wrong), `nest-paren-8k` (wrong) |
| `wild-sexp-balanced` | `large-subject-throughput` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 9 | 11% | -3:PCREC_ERR_FRAMES×8 (smallest: nest-paren-512, 1,035 B) | 0 | `nest-paren-100k` (gave-up), `nest-paren-10k` (gave-up), `nest-paren-1k` (gave-up), `nest-paren-2k` (gave-up), `nest-paren-32k` (gave-up), `nest-paren-512` (gave-up), `nest-paren-8k` (gave-up), `sx-1m` (gave-up) |
| `wild-sexp-balanced` | `large-subject-throughput` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 9 | 11% | -3:PCREC_ERR_FRAMES×8 (smallest: nest-paren-512, 1,035 B) | 0 | `nest-paren-100k` (gave-up), `nest-paren-10k` (gave-up), `nest-paren-1k` (gave-up), `nest-paren-2k` (gave-up), `nest-paren-32k` (gave-up), `nest-paren-512` (gave-up), `nest-paren-8k` (gave-up), `sx-1m` (gave-up) |

## Ranking -- NON-CAPTURING engines only, nocaps vs nocaps (per pattern x regime, SET grain: sum over the subject set; best median first)

### `co-isbn` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna_assist-v01 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 1,103,849.0 | 1.1038 | 1,080,891.9 | 1,112,916.7 | 13,074.2 | 1.000x | 1.000x | scratch |

#### `co-isbn` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-isbn-1m` | 1,000,051 | `rust_1.13.1_default-caps-simdna_assist-v01` | 1,103,849.0 | 1.1038 |

- `rust_1.13.1_default-caps-simdna_assist-v01` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `co-isbn-twin` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna_assist-v01 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 619,005.2 | 0.6190 | 613,712.6 | 619,685.4 | 2,199.3 | 1.000x | 1.000x | scratch |
| 2 | `rust_1.13.1_default-caps-simdna` | inconclusive-load | `plain` | same program | 619,207.2 | 0.6192 | 618,641.1 | 622,458.3 | 1,397.7 | 1.000x | 1.000x | scratch |

#### `co-isbn-twin` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-isbn-1m` | 1,000,051 | `rust_1.13.1_default-caps-simdna_assist-v01` | 619,005.2 | 0.6190 |
| `co-isbn-1m` | 1,000,051 | `rust_1.13.1_default-caps-simdna` | 619,207.2 | 0.6192 |

- `rust_1.13.1_default-caps-simdna_assist-v01` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)
- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `co-luhn` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna_assist-v01 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 3,242,778.1 | 3.2427 | 3,217,860.5 | 3,367,719.2 | 53,295.3 | 1.000x | 1.000x | scratch |

#### `co-luhn` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-luhn-1m` | 1,000,017 | `rust_1.13.1_default-caps-simdna_assist-v01` | 3,242,778.1 | 3.2427 |

- `rust_1.13.1_default-caps-simdna_assist-v01` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `co-luhn-twin` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna_assist-v01 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 1,748,744.9 | 1.7487 | 1,746,748.3 | 1,751,419.6 | 1,704.5 | 1.000x | 1.000x | scratch |
| 2 | `rust_1.13.1_default-caps-simdna` | inconclusive-load | `plain` | same program | 1,803,282.8 | 1.8033 | 1,801,587.4 | 1,852,366.0 | 19,857.7 | 1.031x | 1.031x | scratch |

#### `co-luhn-twin` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-luhn-1m` | 1,000,017 | `rust_1.13.1_default-caps-simdna_assist-v01` | 1,748,744.9 | 1.7487 |
| `co-luhn-1m` | 1,000,017 | `rust_1.13.1_default-caps-simdna` | 1,803,282.8 | 1.8033 |

- `rust_1.13.1_default-caps-simdna_assist-v01` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)
- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `co-member` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna_assist-v01 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 1,765,295.8 | 1.7652 | 1,756,501.6 | 1,777,252.8 | 7,600.6 | 1.000x | 1.000x | scratch |

#### `co-member` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-member-1m` | 1,000,066 | `rust_1.13.1_default-caps-simdna_assist-v01` | 1,765,295.8 | 1.7652 |

- `rust_1.13.1_default-caps-simdna_assist-v01` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `co-member-twin` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | inconclusive-load | `plain` | same program | 897,171.8 | 0.8971 | 895,567.6 | 902,359.0 | 2,482.7 | 1.000x | 1.000x | scratch |
| 2 | `rust_1.13.1_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 897,677.2 | 0.8976 | 895,467.4 | 1,023,100.4 | 49,169.9 | 1.001x | 1.001x | scratch |

#### `co-member-twin` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-member-1m` | 1,000,066 | `rust_1.13.1_default-caps-simdna` | 897,171.8 | 0.8971 |
| `co-member-1m` | 1,000,066 | `rust_1.13.1_default-caps-simdna_assist-v01` | 897,677.2 | 0.8976 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)
- `rust_1.13.1_default-caps-simdna_assist-v01` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `co-netstr` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna_assist-v01 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 2,237,400.0 | 2.2373 | 2,214,476.3 | 2,502,639.8 | 109,283.5 | 1.000x | 1.000x | scratch |

#### `co-netstr` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-netstr-1m` | 1,000,025 | `rust_1.13.1_default-caps-simdna_assist-v01` | 2,237,400.0 | 2.2373 |

- `rust_1.13.1_default-caps-simdna_assist-v01` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `co-netstr-twin` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | inconclusive-load | `plain` | same program | 1,254,516.7 | 1.2545 | 1,251,160.1 | 1,306,838.6 | 21,475.6 | 1.000x | 1.000x | scratch |
| 2 | `rust_1.13.1_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 1,261,970.1 | 1.2619 | 1,257,552.8 | 1,454,193.3 | 77,433.6 | 1.006x | 1.006x | scratch |

#### `co-netstr-twin` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-netstr-1m` | 1,000,025 | `rust_1.13.1_default-caps-simdna` | 1,254,516.7 | 1.2545 |
| `co-netstr-1m` | 1,000,025 | `rust_1.13.1_default-caps-simdna_assist-v01` | 1,261,970.1 | 1.2619 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)
- `rust_1.13.1_default-caps-simdna_assist-v01` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `cscan` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna_assist-v01 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 46,239,064.4 | 3.6241 | 46,134,650.2 | 48,835,600.1 | 1,044,680.2 | 1.000x | 1.000x | scratch |

#### `cscan` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `comment-5m` | 5,000,011 | `rust_1.13.1_default-caps-simdna_assist-v01` | 13,341,720.7 | 2.6683 |
| `define-witness` | 12 | `rust_1.13.1_default-caps-simdna_assist-v01` | 97.4 | 8.1131 |
| `idents-1m` | 1,000,007 | `rust_1.13.1_default-caps-simdna_assist-v01` | 6,034,085.4 | 6.0340 |
| `literal-100k` | 100,014 | `rust_1.13.1_default-caps-simdna_assist-v01` | 224,569.1 | 2.2454 |
| `nest-brace-100k` | 200,011 | `rust_1.13.1_default-caps-simdna_assist-v01` | 5,861,173.1 | 29.3043 |
| `nest-brace-10k` | 20,011 | `rust_1.13.1_default-caps-simdna_assist-v01` | 587,897.3 | 29.3787 |
| `nest-brace-128` | 267 | `rust_1.13.1_default-caps-simdna_assist-v01` | 7,493.4 | 28.0651 |
| `nest-brace-1k` | 2,059 | `rust_1.13.1_default-caps-simdna_assist-v01` | 59,707.8 | 28.9984 |
| `nest-brace-2k` | 4,107 | `rust_1.13.1_default-caps-simdna_assist-v01` | 120,333.9 | 29.2997 |
| `nest-brace-32k` | 65,547 | `rust_1.13.1_default-caps-simdna_assist-v01` | 1,921,415.0 | 29.3135 |
| `nest-brace-512` | 1,035 | `rust_1.13.1_default-caps-simdna_assist-v01` | 30,110.4 | 29.0922 |
| `nest-brace-8k` | 16,395 | `rust_1.13.1_default-caps-simdna_assist-v01` | 480,096.1 | 29.2831 |
| `nest-digraph-10k` | 40,011 | `rust_1.13.1_default-caps-simdna_assist-v01` | 615,417.7 | 15.3812 |
| `nest-paren-100k` | 200,011 | `rust_1.13.1_default-caps-simdna_assist-v01` | 447,493.0 | 2.2373 |
| `nest-paren-10k` | 20,011 | `rust_1.13.1_default-caps-simdna_assist-v01` | 44,854.1 | 2.2415 |
| `nest-paren-128` | 267 | `rust_1.13.1_default-caps-simdna_assist-v01` | 661.4 | 2.4772 |
| `nest-paren-1k` | 2,059 | `rust_1.13.1_default-caps-simdna_assist-v01` | 4,813.9 | 2.3380 |
| `nest-paren-2k` | 4,107 | `rust_1.13.1_default-caps-simdna_assist-v01` | 9,430.9 | 2.2963 |
| `nest-paren-32k` | 65,547 | `rust_1.13.1_default-caps-simdna_assist-v01` | 147,022.0 | 2.2430 |
| `nest-paren-512` | 1,035 | `rust_1.13.1_default-caps-simdna_assist-v01` | 2,430.8 | 2.3486 |
| `nest-paren-8k` | 16,395 | `rust_1.13.1_default-caps-simdna_assist-v01` | 36,898.4 | 2.2506 |
| `splice-1m` | 1,000,009 | `rust_1.13.1_default-caps-simdna_assist-v01` | 2,953,543.9 | 2.9535 |
| `unterminated-5m` | 5,000,006 | `rust_1.13.1_default-caps-simdna_assist-v01` | 13,333,230.3 | 2.6666 |

- `rust_1.13.1_default-caps-simdna_assist-v01` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `floor` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | inconclusive-load | `plain` | same program | 234,119.2 | 0.0118 | 233,866.1 | 240,240.6 | 2,542.1 | 1.000x | 1.000x | scratch |
| 2 | `rust_1.13.1_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 234,720.1 | 0.0119 | 234,401.4 | 236,884.1 | 925.8 | 1.003x | 1.003x | scratch |

_per-subject rows: 30 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)
- `rust_1.13.1_default-caps-simdna_assist-v01` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-sexp-balanced` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna_assist-v01 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 6,632,279.6 | 5.0571 | 6,588,334.9 | 6,653,666.0 | 23,070.1 | 1.000x | 1.000x | scratch |

#### `wild-sexp-balanced` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `nest-paren-100k` | 200,011 | `rust_1.13.1_default-caps-simdna_assist-v01` | 2,681,755.3 | 13.4080 |
| `nest-paren-10k` | 20,011 | `rust_1.13.1_default-caps-simdna_assist-v01` | 266,189.4 | 13.3022 |
| `nest-paren-128` | 267 | `rust_1.13.1_default-caps-simdna_assist-v01` | 3,549.9 | 13.2955 |
| `nest-paren-1k` | 2,059 | `rust_1.13.1_default-caps-simdna_assist-v01` | 27,716.8 | 13.4613 |
| `nest-paren-2k` | 4,107 | `rust_1.13.1_default-caps-simdna_assist-v01` | 54,583.2 | 13.2903 |
| `nest-paren-32k` | 65,547 | `rust_1.13.1_default-caps-simdna_assist-v01` | 877,968.3 | 13.3945 |
| `nest-paren-512` | 1,035 | `rust_1.13.1_default-caps-simdna_assist-v01` | 13,895.9 | 13.4260 |
| `nest-paren-8k` | 16,395 | `rust_1.13.1_default-caps-simdna_assist-v01` | 218,699.7 | 13.3394 |
| `sx-1m` | 1,002,042 | `rust_1.13.1_default-caps-simdna_assist-v01` | 2,488,550.6 | 2.4835 |

- `rust_1.13.1_default-caps-simdna_assist-v01` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### Undeclared capture class (I-99: never guessed -- excluded from BOTH class-pure views above)

- `vectorscan_5.4.11_block-som-nocaps-simd`: `pcrecbench.capture_class` has no declared row for its (engine, mode, captures-token) identity
- `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01`: `pcrecbench.capture_class` has no declared row for its (engine, mode, captures-token) identity

## Ranking -- MIXED CLASSES, never compare across cells (per pattern x regime, SET grain: sum over the subject set; best median first)

### `co-isbn` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 365,877.5 | 0.3659 | 365,073.9 | 366,124.8 | 368.2 | 0.401x | 1.000x | scratch |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 387,817.4 | 0.3878 | 386,809.1 | 391,554.3 | 1,912.0 | 0.425x | 1.060x | scratch |
| 3 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 556,063.2 | 0.5560 | 553,850.7 | 556,090.0 | 888.9 | 0.610x | 1.520x | scratch |
| 4 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 558,343.5 | 0.5583 | 555,350.9 | 575,870.7 | 9,291.3 | 0.612x | 1.526x | scratch |
| 5 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 567,748.6 | 0.5677 | 552,196.8 | 575,396.6 | 7,742.1 | 0.623x | 1.552x | scratch |
| 6 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 576,848.3 | 0.5768 | 556,004.9 | 582,992.6 | 9,174.9 | 0.633x | 1.577x | scratch |
| 7 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 911,868.6 | 0.9118 | 907,576.4 | 1,018,858.3 | 43,255.6 | 1.000x | 2.492x | scratch |
| 8 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 928,064.3 | 0.9280 | 914,989.7 | 933,084.6 | 6,240.3 | 1.018x | 2.537x | scratch |
| 9 | `rust_1.13.1_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 1,103,849.0 | 1.1038 | 1,080,891.9 | 1,112,916.7 | 13,074.2 | 1.211x | 3.017x | scratch |
| 10 | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | measured | `plain` | same program | 1,856,957.7 | 1.8569 | 1,843,195.2 | 1,882,358.2 | 13,388.0 | 2.036x | 5.075x | scratch |
| 11 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 1,870,114.6 | 1.8700 | 1,844,303.7 | 1,898,867.3 | 21,413.6 | 2.051x | 5.111x | scratch |
| 12 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,887,698.2 | 1.8876 | 1,865,628.2 | 1,905,112.9 | 15,395.9 | 2.070x | 5.159x | scratch |
| 13 | `re2_11.0.0_default-caps-simdna_assist-v01` | measured | `plain` | same program | 2,294,424.5 | 2.2943 | 2,290,045.8 | 2,311,223.2 | 7,353.6 | 2.516x | 6.271x | scratch |

#### `co-isbn` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 365,877.5 | 0.3659 |
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_jit-caps-simdna` | 387,817.4 | 0.3878 |
| `co-isbn-1m` | 1,000,051 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 556,063.2 | 0.5560 |
| `co-isbn-1m` | 1,000,051 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 558,343.5 | 0.5583 |
| `co-isbn-1m` | 1,000,051 | `pcrec_614d45eb3_auto-caps-simdna` | 567,748.6 | 0.5677 |
| `co-isbn-1m` | 1,000,051 | `pcrec_614d45eb3_vm-caps-simdna` | 576,848.3 | 0.5768 |
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_interp-caps-simdna` | 911,868.6 | 0.9118 |
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 928,064.3 | 0.9280 |
| `co-isbn-1m` | 1,000,051 | `rust_1.13.1_default-caps-simdna_assist-v01` | 1,103,849.0 | 1.1038 |
| `co-isbn-1m` | 1,000,051 | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | 1,856,957.7 | 1.8569 |
| `co-isbn-1m` | 1,000,051 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 1,870,114.6 | 1.8700 |
| `co-isbn-1m` | 1,000,051 | `oniguruma_6.9.10_default-caps-simdna` | 1,887,698.2 | 1.8876 |
| `co-isbn-1m` | 1,000,051 | `re2_11.0.0_default-caps-simdna_assist-v01` | 2,294,424.5 | 2.2943 |

- `rust_1.13.1_default-caps-simdna_assist-v01` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `co-isbn-nofn` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 305,756.7 | 0.3057 | 305,393.4 | 307,629.8 | 863.4 | 0.387x | 1.000x | scratch |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 353,367.4 | 0.3533 | 349,754.3 | 366,620.0 | 7,063.8 | 0.448x | 1.156x | scratch |
| 3 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 789,102.2 | 0.7891 | 781,517.8 | 796,404.4 | 5,060.4 | 1.000x | 2.581x | scratch |
| 4 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 792,645.7 | 0.7926 | 783,724.1 | 793,597.3 | 3,676.5 | 1.004x | 2.592x | scratch |

#### `co-isbn-nofn` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 305,756.7 | 0.3057 |
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_jit-caps-simdna` | 353,367.4 | 0.3533 |
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_interp-caps-simdna` | 789,102.2 | 0.7891 |
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 792,645.7 | 0.7926 |

### `co-isbn-pass` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 335,816.0 | 0.3358 | 335,384.4 | 336,750.4 | 488.5 | 0.407x | 1.000x | scratch |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 376,828.0 | 0.3768 | 376,376.5 | 381,360.0 | 1,833.8 | 0.456x | 1.122x | scratch |
| 3 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 472,498.3 | 0.4725 | 471,337.0 | 472,913.9 | 550.6 | 0.572x | 1.407x | scratch |
| 4 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 473,197.2 | 0.4732 | 471,486.4 | 473,950.8 | 818.8 | 0.573x | 1.409x | scratch |
| 5 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 485,272.3 | 0.4852 | 484,244.3 | 485,918.1 | 569.1 | 0.588x | 1.445x | scratch |
| 6 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 486,826.8 | 0.4868 | 485,906.2 | 488,109.0 | 713.9 | 0.590x | 1.450x | scratch |
| 7 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 825,569.5 | 0.8255 | 821,604.0 | 837,789.3 | 6,009.1 | 1.000x | 2.458x | scratch |
| 8 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 830,629.0 | 0.8306 | 825,870.4 | 834,914.7 | 3,143.2 | 1.006x | 2.473x | scratch |
| 9 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,008,198.5 | 2.0081 | 1,963,373.7 | 2,052,856.7 | 29,739.5 | 2.433x | 5.980x | scratch |
| 10 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 2,016,164.6 | 2.0161 | 1,978,139.8 | 2,152,865.0 | 62,432.3 | 2.442x | 6.004x | scratch |

#### `co-isbn-pass` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 335,816.0 | 0.3358 |
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_jit-caps-simdna` | 376,828.0 | 0.3768 |
| `co-isbn-1m` | 1,000,051 | `pcrec_614d45eb3_vm-caps-simdna` | 472,498.3 | 0.4725 |
| `co-isbn-1m` | 1,000,051 | `pcrec_614d45eb3_auto-caps-simdna` | 473,197.2 | 0.4732 |
| `co-isbn-1m` | 1,000,051 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 485,272.3 | 0.4852 |
| `co-isbn-1m` | 1,000,051 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 486,826.8 | 0.4868 |
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_interp-caps-simdna` | 825,569.5 | 0.8255 |
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 830,629.0 | 0.8306 |
| `co-isbn-1m` | 1,000,051 | `oniguruma_6.9.10_default-caps-simdna` | 2,008,198.5 | 2.0081 |
| `co-isbn-1m` | 1,000,051 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 2,016,164.6 | 2.0161 |

### `co-isbn-twin` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna_lim-ceil1g (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 315,169.1 | 0.3152 | 314,379.4 | 318,357.5 | 1,662.5 | 0.410x | 1.000x | scratch |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 335,553.8 | 0.3355 | 334,428.4 | 342,054.3 | 2,860.3 | 0.437x | 1.065x | scratch |
| 3 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 405,558.4 | 0.4055 | 404,697.1 | 406,686.2 | 680.3 | 0.528x | 1.287x | scratch |
| 4 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 407,378.3 | 0.4074 | 406,919.0 | 410,093.0 | 1,269.9 | 0.530x | 1.293x | scratch |
| 5 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 425,088.4 | 0.4251 | 424,217.1 | 427,526.0 | 1,150.4 | 0.553x | 1.349x | scratch |
| 6 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 459,519.0 | 0.4595 | 459,125.1 | 461,529.5 | 887.9 | 0.598x | 1.458x | scratch |
| 7 | `rust_1.13.1_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 619,005.2 | 0.6190 | 613,712.6 | 619,685.4 | 2,199.3 | 0.805x | 1.964x | scratch |
| 8 | `rust_1.13.1_default-caps-simdna` | inconclusive-load | `plain` | same program | 619,207.2 | 0.6192 | 618,641.1 | 622,458.3 | 1,397.7 | 0.806x | 1.965x | scratch |
| 9 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 768,654.4 | 0.7686 | 755,524.9 | 780,157.8 | 7,847.3 | 1.000x | 2.439x | scratch |
| 10 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 772,185.9 | 0.7721 | 760,916.9 | 779,503.7 | 7,115.7 | 1.005x | 2.450x | scratch |
| 11 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 1,811,605.4 | 1.8115 | 1,786,732.1 | 1,856,433.8 | 28,875.1 | 2.357x | 5.748x | scratch |
| 12 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,837,607.8 | 1.8375 | 1,790,088.6 | 1,848,676.3 | 20,763.6 | 2.391x | 5.831x | scratch |
| 13 | `re2_11.0.0_default-caps-simdna_assist-v01` | measured | `plain` | same program | 2,135,425.4 | 2.1353 | 2,129,223.7 | 2,171,460.4 | 15,602.6 | 2.778x | 6.775x | scratch |
| 14 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,142,878.5 | 2.1428 | 2,137,515.8 | 2,163,624.5 | 9,574.7 | 2.788x | 6.799x | scratch |

#### `co-isbn-twin` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 315,169.1 | 0.3152 |
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_jit-caps-simdna` | 335,553.8 | 0.3355 |
| `co-isbn-1m` | 1,000,051 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 405,558.4 | 0.4055 |
| `co-isbn-1m` | 1,000,051 | `pcrec_614d45eb3_auto-caps-simdna` | 407,378.3 | 0.4074 |
| `co-isbn-1m` | 1,000,051 | `pcrec_614d45eb3_vm-caps-simdna` | 425,088.4 | 0.4251 |
| `co-isbn-1m` | 1,000,051 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 459,519.0 | 0.4595 |
| `co-isbn-1m` | 1,000,051 | `rust_1.13.1_default-caps-simdna_assist-v01` | 619,005.2 | 0.6190 |
| `co-isbn-1m` | 1,000,051 | `rust_1.13.1_default-caps-simdna` | 619,207.2 | 0.6192 |
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 768,654.4 | 0.7686 |
| `co-isbn-1m` | 1,000,051 | `libpcre2_10.46_interp-caps-simdna` | 772,185.9 | 0.7721 |
| `co-isbn-1m` | 1,000,051 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 1,811,605.4 | 1.8115 |
| `co-isbn-1m` | 1,000,051 | `oniguruma_6.9.10_default-caps-simdna` | 1,837,607.8 | 1.8375 |
| `co-isbn-1m` | 1,000,051 | `re2_11.0.0_default-caps-simdna_assist-v01` | 2,135,425.4 | 2.1353 |
| `co-isbn-1m` | 1,000,051 | `re2_11.0.0_default-caps-simdna` | 2,142,878.5 | 2.1428 |

- `rust_1.13.1_default-caps-simdna_assist-v01` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)
- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `co-luhn` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 931,991.4 | 0.9320 | 926,407.8 | 943,440.3 | 6,467.8 | 0.219x | 1.000x | scratch |
| 2 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 934,494.0 | 0.9345 | 925,692.1 | 939,070.2 | 4,620.4 | 0.219x | 1.003x | scratch |
| 3 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 940,284.4 | 0.9403 | 922,785.5 | 1,006,813.9 | 30,937.8 | 0.221x | 1.009x | scratch |
| 4 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 953,116.3 | 0.9531 | 947,273.6 | 968,664.8 | 7,716.7 | 0.224x | 1.023x | scratch |
| 5 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 1,099,219.6 | 1.0992 | 1,097,967.5 | 1,108,628.6 | 3,890.8 | 0.258x | 1.179x | scratch |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,125,700.2 | 1.1257 | 1,123,312.4 | 1,154,341.3 | 11,637.7 | 0.264x | 1.208x | scratch |
| 7 | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | measured | `plain` | same program | 2,029,291.8 | 2.0293 | 2,024,197.7 | 2,031,583.2 | 2,538.7 | 0.476x | 2.177x | scratch |
| 8 | `re2_11.0.0_default-caps-simdna_assist-v01` | measured | `plain` | same program | 3,031,297.5 | 3.0312 | 3,026,721.4 | 3,077,287.4 | 18,918.8 | 0.711x | 3.252x | scratch |
| 9 | `rust_1.13.1_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 3,242,778.1 | 3.2427 | 3,217,860.5 | 3,367,719.2 | 53,295.3 | 0.761x | 3.479x | scratch |
| 10 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 4,262,732.6 | 4.2627 | 4,242,526.2 | 4,736,871.8 | 189,674.1 | 1.000x | 4.574x | scratch |
| 11 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 4,276,391.4 | 4.2763 | 4,213,082.0 | 4,334,004.1 | 38,564.3 | 1.003x | 4.588x | scratch |
| 12 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 5,400,307.9 | 5.4002 | 5,330,521.3 | 5,551,449.6 | 76,157.6 | 1.267x | 5.794x | scratch |
| 13 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,415,249.1 | 5.4152 | 5,309,289.5 | 5,515,884.8 | 67,950.9 | 1.270x | 5.810x | scratch |

#### `co-luhn` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-luhn-1m` | 1,000,017 | `pcrec_614d45eb3_auto-caps-simdna` | 931,991.4 | 0.9320 |
| `co-luhn-1m` | 1,000,017 | `pcrec_614d45eb3_vm-caps-simdna` | 934,494.0 | 0.9345 |
| `co-luhn-1m` | 1,000,017 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 940,284.4 | 0.9403 |
| `co-luhn-1m` | 1,000,017 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 953,116.3 | 0.9531 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 1,099,219.6 | 1.0992 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_jit-caps-simdna` | 1,125,700.2 | 1.1257 |
| `co-luhn-1m` | 1,000,017 | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | 2,029,291.8 | 2.0293 |
| `co-luhn-1m` | 1,000,017 | `re2_11.0.0_default-caps-simdna_assist-v01` | 3,031,297.5 | 3.0312 |
| `co-luhn-1m` | 1,000,017 | `rust_1.13.1_default-caps-simdna_assist-v01` | 3,242,778.1 | 3.2427 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_interp-caps-simdna` | 4,262,732.6 | 4.2627 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 4,276,391.4 | 4.2763 |
| `co-luhn-1m` | 1,000,017 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 5,400,307.9 | 5.4002 |
| `co-luhn-1m` | 1,000,017 | `oniguruma_6.9.10_default-caps-simdna` | 5,415,249.1 | 5.4152 |

- `rust_1.13.1_default-caps-simdna_assist-v01` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `co-luhn-nofn` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 759,264.2 | 0.7593 | 757,856.6 | 761,326.4 | 1,112.2 | 0.296x | 1.000x | scratch |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 848,897.9 | 0.8489 | 827,398.0 | 873,903.0 | 17,866.8 | 0.331x | 1.118x | scratch |
| 3 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 2,565,770.9 | 2.5657 | 2,553,411.6 | 2,617,814.9 | 23,024.9 | 1.000x | 3.379x | scratch |
| 4 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 2,567,053.3 | 2.5670 | 2,538,558.2 | 2,622,926.3 | 31,079.3 | 1.000x | 3.381x | scratch |

#### `co-luhn-nofn` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 759,264.2 | 0.7593 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_jit-caps-simdna` | 848,897.9 | 0.8489 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_interp-caps-simdna` | 2,565,770.9 | 2.5657 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 2,567,053.3 | 2.5670 |

### `co-luhn-pass` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna_lim-ceil1g (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 642,826.5 | 0.6428 | 634,189.6 | 646,348.3 | 4,044.0 | 0.249x | 1.000x | scratch |
| 2 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 643,297.3 | 0.6433 | 641,057.0 | 644,497.1 | 1,221.9 | 0.250x | 1.001x | scratch |
| 3 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 644,266.1 | 0.6443 | 641,651.2 | 653,196.2 | 4,242.0 | 0.250x | 1.002x | scratch |
| 4 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 650,518.0 | 0.6505 | 649,998.6 | 652,782.0 | 1,001.5 | 0.252x | 1.012x | scratch |
| 5 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 799,422.7 | 0.7994 | 798,847.2 | 804,661.3 | 2,197.0 | 0.310x | 1.244x | scratch |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 872,709.4 | 0.8727 | 863,495.8 | 889,228.8 | 8,872.0 | 0.339x | 1.358x | scratch |
| 7 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 2,577,656.6 | 2.5776 | 2,561,367.4 | 2,593,628.7 | 11,353.6 | 1.000x | 4.010x | scratch |
| 8 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 2,604,152.5 | 2.6041 | 2,596,746.9 | 2,609,414.0 | 4,335.6 | 1.010x | 4.051x | scratch |
| 9 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 3,949,298.5 | 3.9492 | 3,907,606.9 | 4,125,519.8 | 90,431.7 | 1.532x | 6.144x | scratch |
| 10 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,210,924.8 | 4.2109 | 4,124,626.3 | 4,608,930.6 | 181,316.1 | 1.634x | 6.551x | scratch |

#### `co-luhn-pass` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-luhn-1m` | 1,000,017 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 642,826.5 | 0.6428 |
| `co-luhn-1m` | 1,000,017 | `pcrec_614d45eb3_auto-caps-simdna` | 643,297.3 | 0.6433 |
| `co-luhn-1m` | 1,000,017 | `pcrec_614d45eb3_vm-caps-simdna` | 644,266.1 | 0.6443 |
| `co-luhn-1m` | 1,000,017 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 650,518.0 | 0.6505 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 799,422.7 | 0.7994 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_jit-caps-simdna` | 872,709.4 | 0.8727 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 2,577,656.6 | 2.5776 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_interp-caps-simdna` | 2,604,152.5 | 2.6041 |
| `co-luhn-1m` | 1,000,017 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 3,949,298.5 | 3.9492 |
| `co-luhn-1m` | 1,000,017 | `oniguruma_6.9.10_default-caps-simdna` | 4,210,924.8 | 4.2109 |

### `co-luhn-twin` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 540,695.5 | 0.5407 | 536,142.2 | 542,878.2 | 2,395.5 | 0.218x | 1.000x | scratch |
| 2 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 561,497.6 | 0.5615 | 559,880.0 | 563,138.1 | 1,047.1 | 0.226x | 1.038x | scratch |
| 3 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 732,666.6 | 0.7327 | 728,155.3 | 746,478.9 | 6,373.7 | 0.295x | 1.355x | scratch |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 789,318.8 | 0.7893 | 781,784.3 | 795,409.6 | 4,323.0 | 0.318x | 1.460x | scratch |
| 5 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 994,646.6 | 0.9946 | 992,435.3 | 1,004,202.2 | 4,150.4 | 0.401x | 1.840x | scratch |
| 6 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 1,013,493.7 | 1.0135 | 999,851.7 | 1,023,699.2 | 8,458.7 | 0.409x | 1.874x | scratch |
| 7 | `rust_1.13.1_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 1,748,744.9 | 1.7487 | 1,746,748.3 | 1,751,419.6 | 1,704.5 | 0.705x | 3.234x | scratch |
| 8 | `rust_1.13.1_default-caps-simdna` | inconclusive-load | `plain` | same program | 1,803,282.8 | 1.8033 | 1,801,587.4 | 1,852,366.0 | 19,857.7 | 0.727x | 3.335x | scratch |
| 9 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 2,480,988.0 | 2.4809 | 2,465,701.5 | 2,505,052.3 | 13,283.0 | 1.000x | 4.589x | scratch |
| 10 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 2,509,192.4 | 2.5091 | 2,467,906.5 | 2,549,488.3 | 29,890.1 | 1.011x | 4.641x | scratch |
| 11 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,755,514.1 | 2.7555 | 2,727,443.6 | 2,779,020.1 | 18,122.7 | 1.111x | 5.096x | scratch |
| 12 | `re2_11.0.0_default-caps-simdna_assist-v01` | measured | `plain` | same program | 2,767,071.2 | 2.7670 | 2,756,052.3 | 2,778,209.9 | 8,093.6 | 1.115x | 5.118x | scratch |
| 13 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,696,168.4 | 3.6961 | 3,655,311.4 | 3,728,329.7 | 26,631.3 | 1.490x | 6.836x | scratch |
| 14 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 3,701,469.7 | 3.7014 | 3,640,949.2 | 3,772,283.9 | 42,521.8 | 1.492x | 6.846x | scratch |

#### `co-luhn-twin` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-luhn-1m` | 1,000,017 | `pcrec_614d45eb3_vm-caps-simdna` | 540,695.5 | 0.5407 |
| `co-luhn-1m` | 1,000,017 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 561,497.6 | 0.5615 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 732,666.6 | 0.7327 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_jit-caps-simdna` | 789,318.8 | 0.7893 |
| `co-luhn-1m` | 1,000,017 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 994,646.6 | 0.9946 |
| `co-luhn-1m` | 1,000,017 | `pcrec_614d45eb3_auto-caps-simdna` | 1,013,493.7 | 1.0135 |
| `co-luhn-1m` | 1,000,017 | `rust_1.13.1_default-caps-simdna_assist-v01` | 1,748,744.9 | 1.7487 |
| `co-luhn-1m` | 1,000,017 | `rust_1.13.1_default-caps-simdna` | 1,803,282.8 | 1.8033 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_interp-caps-simdna` | 2,480,988.0 | 2.4809 |
| `co-luhn-1m` | 1,000,017 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 2,509,192.4 | 2.5091 |
| `co-luhn-1m` | 1,000,017 | `re2_11.0.0_default-caps-simdna` | 2,755,514.1 | 2.7555 |
| `co-luhn-1m` | 1,000,017 | `re2_11.0.0_default-caps-simdna_assist-v01` | 2,767,071.2 | 2.7670 |
| `co-luhn-1m` | 1,000,017 | `oniguruma_6.9.10_default-caps-simdna` | 3,696,168.4 | 3.6961 |
| `co-luhn-1m` | 1,000,017 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 3,701,469.7 | 3.7014 |

- `rust_1.13.1_default-caps-simdna_assist-v01` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)
- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `co-member` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna_lim-ceil1g (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 478,418.4 | 0.4784 | 476,328.0 | 479,338.1 | 1,334.1 | 0.322x | 1.000x | scratch |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 512,783.3 | 0.5127 | 502,540.2 | 516,597.6 | 5,102.2 | 0.345x | 1.072x | scratch |
| 3 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 752,556.3 | 0.7525 | 747,823.2 | 759,366.6 | 3,784.7 | 0.507x | 1.573x | scratch |
| 4 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 762,092.9 | 0.7620 | 758,493.6 | 773,134.0 | 5,577.3 | 0.513x | 1.593x | scratch |
| 5 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 768,798.6 | 0.7687 | 767,550.7 | 770,740.6 | 1,237.1 | 0.518x | 1.607x | scratch |
| 6 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 784,293.0 | 0.7842 | 768,030.3 | 823,946.2 | 19,544.9 | 0.528x | 1.639x | scratch |
| 7 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 1,484,705.9 | 1.4846 | 1,479,882.6 | 1,490,540.4 | 4,612.3 | 1.000x | 3.103x | scratch |
| 8 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 1,487,589.7 | 1.4875 | 1,485,726.8 | 1,499,804.6 | 5,069.5 | 1.002x | 3.109x | scratch |
| 9 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,752,373.7 | 1.7523 | 1,692,577.7 | 1,770,183.6 | 30,664.8 | 1.180x | 3.663x | scratch |
| 10 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 1,752,622.1 | 1.7525 | 1,705,774.9 | 1,976,029.3 | 98,172.8 | 1.180x | 3.663x | scratch |
| 11 | `rust_1.13.1_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 1,765,295.8 | 1.7652 | 1,756,501.6 | 1,777,252.8 | 7,600.6 | 1.189x | 3.690x | scratch |
| 12 | `re2_11.0.0_default-caps-simdna_assist-v01` | measured | `plain` | same program | 2,966,039.1 | 2.9658 | 2,954,936.9 | 3,068,304.9 | 42,995.6 | 1.998x | 6.200x | scratch |
| 13 | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | measured | `plain` | same program | 3,426,965.5 | 3.4267 | 3,408,300.3 | 3,502,941.5 | 33,666.1 | 2.308x | 7.163x | scratch |

#### `co-member` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 478,418.4 | 0.4784 |
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_jit-caps-simdna` | 512,783.3 | 0.5127 |
| `co-member-1m` | 1,000,066 | `pcrec_614d45eb3_auto-caps-simdna` | 752,556.3 | 0.7525 |
| `co-member-1m` | 1,000,066 | `pcrec_614d45eb3_vm-caps-simdna` | 762,092.9 | 0.7620 |
| `co-member-1m` | 1,000,066 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 768,798.6 | 0.7687 |
| `co-member-1m` | 1,000,066 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 784,293.0 | 0.7842 |
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 1,484,705.9 | 1.4846 |
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_interp-caps-simdna` | 1,487,589.7 | 1.4875 |
| `co-member-1m` | 1,000,066 | `oniguruma_6.9.10_default-caps-simdna` | 1,752,373.7 | 1.7523 |
| `co-member-1m` | 1,000,066 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 1,752,622.1 | 1.7525 |
| `co-member-1m` | 1,000,066 | `rust_1.13.1_default-caps-simdna_assist-v01` | 1,765,295.8 | 1.7652 |
| `co-member-1m` | 1,000,066 | `re2_11.0.0_default-caps-simdna_assist-v01` | 2,966,039.1 | 2.9658 |
| `co-member-1m` | 1,000,066 | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | 3,426,965.5 | 3.4267 |

- `rust_1.13.1_default-caps-simdna_assist-v01` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `co-member-nofn` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 395,978.8 | 0.3960 | 393,462.1 | 409,641.5 | 5,823.4 | 0.308x | 1.000x | scratch |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 456,346.8 | 0.4563 | 453,309.7 | 475,317.8 | 7,959.6 | 0.355x | 1.152x | scratch |
| 3 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 1,285,903.9 | 1.2858 | 1,279,240.3 | 1,294,583.5 | 6,394.8 | 1.000x | 3.247x | scratch |
| 4 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 1,293,456.5 | 1.2934 | 1,286,579.3 | 1,307,234.0 | 7,083.0 | 1.006x | 3.266x | scratch |

#### `co-member-nofn` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 395,978.8 | 0.3960 |
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_jit-caps-simdna` | 456,346.8 | 0.4563 |
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_interp-caps-simdna` | 1,285,903.9 | 1.2858 |
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 1,293,456.5 | 1.2934 |

### `co-member-pass` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 435,502.1 | 0.4355 | 433,016.3 | 448,448.9 | 6,878.8 | 0.325x | 1.000x | scratch |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 502,362.3 | 0.5023 | 496,777.5 | 536,109.0 | 14,534.1 | 0.375x | 1.154x | scratch |
| 3 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 638,428.2 | 0.6384 | 631,674.7 | 639,679.7 | 2,926.0 | 0.476x | 1.466x | scratch |
| 4 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 641,940.0 | 0.6419 | 638,540.0 | 655,377.6 | 6,657.6 | 0.479x | 1.474x | scratch |
| 5 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 643,251.5 | 0.6432 | 641,452.8 | 656,206.5 | 5,432.7 | 0.480x | 1.477x | scratch |
| 6 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 655,571.4 | 0.6555 | 646,503.7 | 659,351.9 | 4,388.9 | 0.489x | 1.505x | scratch |
| 7 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 1,340,840.0 | 1.3408 | 1,328,681.2 | 1,342,014.2 | 5,041.5 | 1.000x | 3.079x | scratch |
| 8 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 1,359,582.4 | 1.3595 | 1,352,327.4 | 1,364,611.9 | 4,062.4 | 1.014x | 3.122x | scratch |
| 9 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 2,139,134.1 | 2.1390 | 2,035,381.5 | 2,183,738.2 | 54,340.4 | 1.595x | 4.912x | scratch |
| 10 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,147,692.4 | 2.1476 | 2,030,104.2 | 2,216,353.5 | 75,680.9 | 1.602x | 4.932x | scratch |

#### `co-member-pass` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 435,502.1 | 0.4355 |
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_jit-caps-simdna` | 502,362.3 | 0.5023 |
| `co-member-1m` | 1,000,066 | `pcrec_614d45eb3_auto-caps-simdna` | 638,428.2 | 0.6384 |
| `co-member-1m` | 1,000,066 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 641,940.0 | 0.6419 |
| `co-member-1m` | 1,000,066 | `pcrec_614d45eb3_vm-caps-simdna` | 643,251.5 | 0.6432 |
| `co-member-1m` | 1,000,066 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 655,571.4 | 0.6555 |
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_interp-caps-simdna` | 1,340,840.0 | 1.3408 |
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 1,359,582.4 | 1.3595 |
| `co-member-1m` | 1,000,066 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 2,139,134.1 | 2.1390 |
| `co-member-1m` | 1,000,066 | `oniguruma_6.9.10_default-caps-simdna` | 2,147,692.4 | 2.1476 |

### `co-member-twin` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna_lim-ceil1g (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 373,398.4 | 0.3734 | 373,174.7 | 382,487.0 | 3,599.4 | 0.294x | 1.000x | scratch |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 433,125.2 | 0.4331 | 433,007.3 | 446,633.9 | 5,274.4 | 0.341x | 1.160x | scratch |
| 3 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 482,319.2 | 0.4823 | 481,295.7 | 483,545.9 | 734.6 | 0.379x | 1.292x | scratch |
| 4 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 508,887.6 | 0.5089 | 508,375.7 | 511,784.0 | 1,305.5 | 0.400x | 1.363x | scratch |
| 5 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 587,416.6 | 0.5874 | 586,707.2 | 616,278.5 | 11,331.3 | 0.462x | 1.573x | scratch |
| 6 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 588,418.3 | 0.5884 | 585,451.3 | 591,132.9 | 2,080.3 | 0.463x | 1.576x | scratch |
| 7 | `rust_1.13.1_default-caps-simdna` | inconclusive-load | `plain` | same program | 897,171.8 | 0.8971 | 895,567.6 | 902,359.0 | 2,482.7 | 0.705x | 2.403x | scratch |
| 8 | `rust_1.13.1_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 897,677.2 | 0.8976 | 895,467.4 | 1,023,100.4 | 49,169.9 | 0.706x | 2.404x | scratch |
| 9 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 1,272,013.5 | 1.2719 | 1,255,983.0 | 1,294,093.9 | 13,724.4 | 1.000x | 3.407x | scratch |
| 10 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 1,282,663.7 | 1.2826 | 1,268,679.2 | 1,293,903.6 | 10,068.6 | 1.008x | 3.435x | scratch |
| 11 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 1,802,930.0 | 1.8028 | 1,785,366.2 | 2,294,328.8 | 198,880.1 | 1.417x | 4.828x | scratch |
| 12 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,803,318.1 | 1.8032 | 1,736,501.8 | 1,837,967.5 | 38,832.2 | 1.418x | 4.829x | scratch |
| 13 | `re2_11.0.0_default-caps-simdna_assist-v01` | measured | `plain` | same program | 2,670,130.4 | 2.6700 | 2,665,627.2 | 2,682,649.8 | 7,404.1 | 2.099x | 7.151x | scratch |
| 14 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,694,436.6 | 2.6943 | 2,678,994.6 | 2,707,397.6 | 9,112.9 | 2.118x | 7.216x | scratch |

#### `co-member-twin` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 373,398.4 | 0.3734 |
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_jit-caps-simdna` | 433,125.2 | 0.4331 |
| `co-member-1m` | 1,000,066 | `pcrec_614d45eb3_auto-caps-simdna` | 482,319.2 | 0.4823 |
| `co-member-1m` | 1,000,066 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 508,887.6 | 0.5089 |
| `co-member-1m` | 1,000,066 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 587,416.6 | 0.5874 |
| `co-member-1m` | 1,000,066 | `pcrec_614d45eb3_vm-caps-simdna` | 588,418.3 | 0.5884 |
| `co-member-1m` | 1,000,066 | `rust_1.13.1_default-caps-simdna` | 897,171.8 | 0.8971 |
| `co-member-1m` | 1,000,066 | `rust_1.13.1_default-caps-simdna_assist-v01` | 897,677.2 | 0.8976 |
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 1,272,013.5 | 1.2719 |
| `co-member-1m` | 1,000,066 | `libpcre2_10.46_interp-caps-simdna` | 1,282,663.7 | 1.2826 |
| `co-member-1m` | 1,000,066 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 1,802,930.0 | 1.8028 |
| `co-member-1m` | 1,000,066 | `oniguruma_6.9.10_default-caps-simdna` | 1,803,318.1 | 1.8032 |
| `co-member-1m` | 1,000,066 | `re2_11.0.0_default-caps-simdna_assist-v01` | 2,670,130.4 | 2.6700 |
| `co-member-1m` | 1,000,066 | `re2_11.0.0_default-caps-simdna` | 2,694,436.6 | 2.6943 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)
- `rust_1.13.1_default-caps-simdna_assist-v01` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `co-netstr` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_614d45eb3_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 1,513,115.4 | 1.5131 | 1,511,862.7 | 1,555,233.0 | 17,074.9 | 1.000x | 1.000x | scratch |
| 2 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 1,518,378.5 | 1.5183 | 1,516,875.4 | 1,521,809.4 | 1,890.2 | 1.003x | 1.003x | scratch |
| 3 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 1,534,868.6 | 1.5348 | 1,531,321.3 | 1,600,838.8 | 26,865.9 | 1.014x | 1.014x | scratch |
| 4 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 1,539,114.4 | 1.5391 | 1,534,249.0 | 1,544,708.4 | 3,880.0 | 1.017x | 1.017x | scratch |
| 5 | `rust_1.13.1_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 2,237,400.0 | 2.2373 | 2,214,476.3 | 2,502,639.8 | 109,283.5 | 1.479x | 1.479x | scratch |
| 6 | `re2_11.0.0_default-caps-simdna_assist-v01` | measured | `plain` | same program | 3,907,307.0 | 3.9072 | 3,867,652.2 | 3,953,516.6 | 32,588.9 | 2.582x | 2.582x | scratch |
| 7 | `oniguruma_6.9.10_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 16,235,296.0 | 16.2349 | 16,111,107.0 | 16,425,386.8 | 113,568.1 | 10.730x | 10.730x | scratch |
| 8 | `libpcre2_10.46_jit-caps-simdna_assist-v01` | measured | `plain` | same program | 19,550,667.7 | 19.5502 | 19,237,958.3 | 19,757,801.3 | 194,147.6 | 12.921x | 12.921x | scratch |
| 9 | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | measured | `plain` | same program | 7,010,489,442.0 | 7010.3142 | 6,979,745,859.0 | 7,096,425,106.0 | 40,954,383.9 | 4633.149x | 4633.149x | scratch |

#### `co-netstr` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-netstr-1m` | 1,000,025 | `pcrec_614d45eb3_auto-caps-simdna` | 1,513,115.4 | 1.5131 |
| `co-netstr-1m` | 1,000,025 | `pcrec_614d45eb3_vm-caps-simdna` | 1,518,378.5 | 1.5183 |
| `co-netstr-1m` | 1,000,025 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 1,534,868.6 | 1.5348 |
| `co-netstr-1m` | 1,000,025 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 1,539,114.4 | 1.5391 |
| `co-netstr-1m` | 1,000,025 | `rust_1.13.1_default-caps-simdna_assist-v01` | 2,237,400.0 | 2.2373 |
| `co-netstr-1m` | 1,000,025 | `re2_11.0.0_default-caps-simdna_assist-v01` | 3,907,307.0 | 3.9072 |
| `co-netstr-1m` | 1,000,025 | `oniguruma_6.9.10_default-caps-simdna_assist-v01` | 16,235,296.0 | 16.2349 |
| `co-netstr-1m` | 1,000,025 | `libpcre2_10.46_jit-caps-simdna_assist-v01` | 19,550,667.7 | 19.5502 |
| `co-netstr-1m` | 1,000,025 | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | 7,010,489,442.0 | 7010.3142 |

- `rust_1.13.1_default-caps-simdna_assist-v01` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `co-netstr-assist` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 7,702,979.7 | 7.7028 | 7,685,621.3 | 7,800,244.4 | 43,592.0 | 0.360x | 1.000x | scratch |
| 2 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 7,909,603.1 | 7.9094 | 7,884,377.0 | 8,300,591.3 | 157,432.5 | 0.370x | 1.027x | scratch |
| 3 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 7,958,042.4 | 7.9578 | 7,892,646.3 | 8,208,331.1 | 108,466.7 | 0.372x | 1.033x | scratch |
| 4 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 8,037,329.6 | 8.0371 | 7,879,937.3 | 8,171,827.3 | 93,525.4 | 0.376x | 1.043x | scratch |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 8,144,725.0 | 8.1445 | 8,068,365.3 | 8,454,869.4 | 141,729.2 | 0.381x | 1.057x | scratch |
| 6 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 8,269,661.2 | 8.2695 | 8,190,962.8 | 8,416,913.5 | 85,701.4 | 0.387x | 1.074x | scratch |
| 7 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 21,382,881.7 | 21.3823 | 21,331,114.3 | 21,537,813.3 | 69,816.8 | 1.000x | 2.776x | scratch |
| 8 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 21,821,189.0 | 21.8206 | 21,671,132.7 | 22,097,479.7 | 151,816.9 | 1.020x | 2.833x | scratch |
| 9 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 22,511,386.0 | 22.5108 | 22,312,300.7 | 22,666,705.3 | 135,614.7 | 1.053x | 2.922x | scratch |
| 10 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 22,756,958.3 | 22.7564 | 22,369,107.7 | 24,174,807.0 | 637,841.2 | 1.064x | 2.954x | scratch |

#### `co-netstr-assist` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-netstr-1m` | 1,000,025 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 7,702,979.7 | 7.7028 |
| `co-netstr-1m` | 1,000,025 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 7,909,603.1 | 7.9094 |
| `co-netstr-1m` | 1,000,025 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 7,958,042.4 | 7.9578 |
| `co-netstr-1m` | 1,000,025 | `pcrec_614d45eb3_auto-caps-simdna` | 8,037,329.6 | 8.0371 |
| `co-netstr-1m` | 1,000,025 | `libpcre2_10.46_jit-caps-simdna` | 8,144,725.0 | 8.1445 |
| `co-netstr-1m` | 1,000,025 | `pcrec_614d45eb3_vm-caps-simdna` | 8,269,661.2 | 8.2695 |
| `co-netstr-1m` | 1,000,025 | `libpcre2_10.46_interp-caps-simdna` | 21,382,881.7 | 21.3823 |
| `co-netstr-1m` | 1,000,025 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 21,821,189.0 | 21.8206 |
| `co-netstr-1m` | 1,000,025 | `oniguruma_6.9.10_default-caps-simdna` | 22,511,386.0 | 22.5108 |
| `co-netstr-1m` | 1,000,025 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 22,756,958.3 | 22.7564 |

### `co-netstr-twin` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna_lim-ceil1g (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 1,044,151.8 | 1.0441 | 1,041,577.0 | 1,049,020.1 | 2,630.7 | 0.070x | 1.000x | scratch |
| 2 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 1,074,069.7 | 1.0740 | 1,068,230.0 | 1,077,663.4 | 3,685.9 | 0.072x | 1.029x | scratch |
| 3 | `rust_1.13.1_default-caps-simdna` | inconclusive-load | `plain` | same program | 1,254,516.7 | 1.2545 | 1,251,160.1 | 1,306,838.6 | 21,475.6 | 0.084x | 1.201x | scratch |
| 4 | `rust_1.13.1_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 1,261,970.1 | 1.2619 | 1,257,552.8 | 1,454,193.3 | 77,433.6 | 0.085x | 1.209x | scratch |
| 5 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 3,346,164.1 | 3.3461 | 3,341,627.3 | 3,350,006.2 | 3,118.9 | 0.224x | 3.205x | scratch |
| 6 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 3,612,883.4 | 3.6128 | 3,601,897.6 | 3,619,575.3 | 7,559.6 | 0.242x | 3.460x | scratch |
| 7 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 3,687,248.9 | 3.6872 | 3,669,114.1 | 3,696,766.8 | 9,043.2 | 0.247x | 3.531x | scratch |
| 8 | `libpcre2_10.46_jit-caps-simdna_assist-v01` | measured | `plain` | same program | 3,743,955.1 | 3.7439 | 3,739,877.4 | 3,753,903.0 | 5,052.4 | 0.251x | 3.586x | scratch |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,745,505.9 | 3.7454 | 3,736,952.6 | 3,766,312.9 | 10,371.9 | 0.251x | 3.587x | scratch |
| 10 | `re2_11.0.0_default-caps-simdna_assist-v01` | measured | `plain` | same program | 4,030,107.6 | 4.0300 | 3,998,457.9 | 4,070,136.3 | 23,310.7 | 0.270x | 3.860x | scratch |
| 11 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 4,050,126.8 | 4.0500 | 4,002,769.3 | 4,127,894.2 | 41,110.8 | 0.271x | 3.879x | scratch |
| 12 | `oniguruma_6.9.10_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 6,780,968.0 | 6.7808 | 6,630,989.6 | 6,899,525.6 | 103,046.5 | 0.454x | 6.494x | scratch |
| 13 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 6,852,676.2 | 6.8525 | 6,703,159.5 | 6,975,197.1 | 108,588.9 | 0.459x | 6.563x | scratch |
| 14 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 6,865,097.4 | 6.8649 | 6,719,142.4 | 6,975,318.9 | 90,570.3 | 0.460x | 6.575x | scratch |
| 15 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 14,922,929.8 | 14.9226 | 14,848,953.0 | 15,254,855.5 | 151,088.8 | 1.000x | 14.292x | scratch |
| 16 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 15,059,456.8 | 15.0591 | 14,994,121.2 | 15,137,070.5 | 48,717.3 | 1.009x | 14.423x | scratch |

#### `co-netstr-twin` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `co-netstr-1m` | 1,000,025 | `pcrec_614d45eb3_auto-caps-simdna` | 1,044,151.8 | 1.0441 |
| `co-netstr-1m` | 1,000,025 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 1,074,069.7 | 1.0740 |
| `co-netstr-1m` | 1,000,025 | `rust_1.13.1_default-caps-simdna` | 1,254,516.7 | 1.2545 |
| `co-netstr-1m` | 1,000,025 | `rust_1.13.1_default-caps-simdna_assist-v01` | 1,261,970.1 | 1.2619 |
| `co-netstr-1m` | 1,000,025 | `pcrec_614d45eb3_vm-caps-simdna` | 3,346,164.1 | 3.3461 |
| `co-netstr-1m` | 1,000,025 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 3,612,883.4 | 3.6128 |
| `co-netstr-1m` | 1,000,025 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 3,687,248.9 | 3.6872 |
| `co-netstr-1m` | 1,000,025 | `libpcre2_10.46_jit-caps-simdna_assist-v01` | 3,743,955.1 | 3.7439 |
| `co-netstr-1m` | 1,000,025 | `libpcre2_10.46_jit-caps-simdna` | 3,745,505.9 | 3.7454 |
| `co-netstr-1m` | 1,000,025 | `re2_11.0.0_default-caps-simdna_assist-v01` | 4,030,107.6 | 4.0300 |
| `co-netstr-1m` | 1,000,025 | `re2_11.0.0_default-caps-simdna` | 4,050,126.8 | 4.0500 |
| `co-netstr-1m` | 1,000,025 | `oniguruma_6.9.10_default-caps-simdna_assist-v01` | 6,780,968.0 | 6.7808 |
| `co-netstr-1m` | 1,000,025 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 6,852,676.2 | 6.8525 |
| `co-netstr-1m` | 1,000,025 | `oniguruma_6.9.10_default-caps-simdna` | 6,865,097.4 | 6.8649 |
| `co-netstr-1m` | 1,000,025 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 14,922,929.8 | 14.9226 |
| `co-netstr-1m` | 1,000,025 | `libpcre2_10.46_interp-caps-simdna` | 15,059,456.8 | 15.0591 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)
- `rust_1.13.1_default-caps-simdna_assist-v01` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `cscan` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_jit-caps-simdna_lim-ceil1g (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 17,303,336.0 | 1.3562 | 17,138,804.2 | 17,544,569.9 | 158,475.3 | 1.000x | 1.000x | 23 | 100% | scratch |
| 2 | `rust_1.13.1_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 46,239,064.4 | 3.6241 | 46,134,650.2 | 48,835,600.1 | 1,044,680.2 | 2.672x | 2.672x | 23 | 100% | scratch |
| 3 | `re2_11.0.0_default-caps-simdna_assist-v01` | measured | `plain` | same program | 59,873,401.5 | 4.6927 | 59,594,816.1 | 60,063,596.6 | 187,397.7 | 3.460x | 3.460x | 23 | 100% | scratch |

#### `cscan` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `comment-5m` | 5,000,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 3,511,852.3 | 0.7024 |
| `comment-5m` | 5,000,011 | `rust_1.13.1_default-caps-simdna_assist-v01` | 13,341,720.7 | 2.6683 |
| `comment-5m` | 5,000,011 | `re2_11.0.0_default-caps-simdna_assist-v01` | 10,332,625.7 | 2.0665 |
| `define-witness` | 12 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 60.9 | 5.0754 |
| `define-witness` | 12 | `rust_1.13.1_default-caps-simdna_assist-v01` | 97.4 | 8.1131 |
| `define-witness` | 12 | `re2_11.0.0_default-caps-simdna_assist-v01` | 191.3 | 15.9409 |
| `idents-1m` | 1,000,007 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 3,563,813.4 | 3.5638 |
| `idents-1m` | 1,000,007 | `rust_1.13.1_default-caps-simdna_assist-v01` | 6,034,085.4 | 6.0340 |
| `idents-1m` | 1,000,007 | `re2_11.0.0_default-caps-simdna_assist-v01` | 10,478,005.6 | 10.4779 |
| `literal-100k` | 100,014 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 49,585.9 | 0.4958 |
| `literal-100k` | 100,014 | `rust_1.13.1_default-caps-simdna_assist-v01` | 224,569.1 | 2.2454 |
| `literal-100k` | 100,014 | `re2_11.0.0_default-caps-simdna_assist-v01` | 199,505.0 | 1.9948 |
| `nest-brace-100k` | 200,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 2,462,709.2 | 12.3129 |
| `nest-brace-100k` | 200,011 | `rust_1.13.1_default-caps-simdna_assist-v01` | 5,861,173.1 | 29.3043 |
| `nest-brace-100k` | 200,011 | `re2_11.0.0_default-caps-simdna_assist-v01` | 15,603,286.6 | 78.0121 |
| `nest-brace-10k` | 20,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 224,169.9 | 11.2023 |
| `nest-brace-10k` | 20,011 | `rust_1.13.1_default-caps-simdna_assist-v01` | 587,897.3 | 29.3787 |
| `nest-brace-10k` | 20,011 | `re2_11.0.0_default-caps-simdna_assist-v01` | 1,556,786.1 | 77.7965 |
| `nest-brace-128` | 267 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 2,736.0 | 10.2472 |
| `nest-brace-128` | 267 | `rust_1.13.1_default-caps-simdna_assist-v01` | 7,493.4 | 28.0651 |
| `nest-brace-128` | 267 | `re2_11.0.0_default-caps-simdna_assist-v01` | 19,969.9 | 74.7937 |
| `nest-brace-1k` | 2,059 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 21,931.2 | 10.6514 |
| `nest-brace-1k` | 2,059 | `rust_1.13.1_default-caps-simdna_assist-v01` | 59,707.8 | 28.9984 |
| `nest-brace-1k` | 2,059 | `re2_11.0.0_default-caps-simdna_assist-v01` | 160,112.9 | 77.7624 |
| `nest-brace-2k` | 4,107 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 44,617.5 | 10.8638 |
| `nest-brace-2k` | 4,107 | `rust_1.13.1_default-caps-simdna_assist-v01` | 120,333.9 | 29.2997 |
| `nest-brace-2k` | 4,107 | `re2_11.0.0_default-caps-simdna_assist-v01` | 318,759.6 | 77.6137 |
| `nest-brace-32k` | 65,547 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 762,226.2 | 11.6287 |
| `nest-brace-32k` | 65,547 | `rust_1.13.1_default-caps-simdna_assist-v01` | 1,921,415.0 | 29.3135 |
| `nest-brace-32k` | 65,547 | `re2_11.0.0_default-caps-simdna_assist-v01` | 5,100,860.2 | 77.8199 |
| `nest-brace-512` | 1,035 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 10,938.8 | 10.5689 |
| `nest-brace-512` | 1,035 | `rust_1.13.1_default-caps-simdna_assist-v01` | 30,110.4 | 29.0922 |
| `nest-brace-512` | 1,035 | `re2_11.0.0_default-caps-simdna_assist-v01` | 79,610.7 | 76.9186 |
| `nest-brace-8k` | 16,395 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 183,211.6 | 11.1748 |
| `nest-brace-8k` | 16,395 | `rust_1.13.1_default-caps-simdna_assist-v01` | 480,096.1 | 29.2831 |
| `nest-brace-8k` | 16,395 | `re2_11.0.0_default-caps-simdna_assist-v01` | 1,274,591.0 | 77.7427 |
| `nest-digraph-10k` | 40,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 302,792.5 | 7.5677 |
| `nest-digraph-10k` | 40,011 | `rust_1.13.1_default-caps-simdna_assist-v01` | 615,417.7 | 15.3812 |
| `nest-digraph-10k` | 40,011 | `re2_11.0.0_default-caps-simdna_assist-v01` | 1,609,077.3 | 40.2159 |
| `nest-paren-100k` | 200,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 1,077,442.4 | 5.3869 |
| `nest-paren-100k` | 200,011 | `rust_1.13.1_default-caps-simdna_assist-v01` | 447,493.0 | 2.2373 |
| `nest-paren-100k` | 200,011 | `re2_11.0.0_default-caps-simdna_assist-v01` | 406,510.9 | 2.0324 |
| `nest-paren-10k` | 20,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 107,714.3 | 5.3828 |
| `nest-paren-10k` | 20,011 | `rust_1.13.1_default-caps-simdna_assist-v01` | 44,854.1 | 2.2415 |
| `nest-paren-10k` | 20,011 | `re2_11.0.0_default-caps-simdna_assist-v01` | 40,743.1 | 2.0360 |
| `nest-paren-128` | 267 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 1,455.0 | 5.4494 |
| `nest-paren-128` | 267 | `rust_1.13.1_default-caps-simdna_assist-v01` | 661.4 | 2.4772 |
| `nest-paren-128` | 267 | `re2_11.0.0_default-caps-simdna_assist-v01` | 724.0 | 2.7117 |
| `nest-paren-1k` | 2,059 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 11,017.8 | 5.3510 |
| `nest-paren-1k` | 2,059 | `rust_1.13.1_default-caps-simdna_assist-v01` | 4,813.9 | 2.3380 |
| `nest-paren-1k` | 2,059 | `re2_11.0.0_default-caps-simdna_assist-v01` | 4,442.5 | 2.1576 |
| `nest-paren-2k` | 4,107 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 22,083.7 | 5.3771 |
| `nest-paren-2k` | 4,107 | `rust_1.13.1_default-caps-simdna_assist-v01` | 9,430.9 | 2.2963 |
| `nest-paren-2k` | 4,107 | `re2_11.0.0_default-caps-simdna_assist-v01` | 8,558.1 | 2.0838 |
| `nest-paren-32k` | 65,547 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 352,939.4 | 5.3845 |
| `nest-paren-32k` | 65,547 | `rust_1.13.1_default-caps-simdna_assist-v01` | 147,022.0 | 2.2430 |
| `nest-paren-32k` | 65,547 | `re2_11.0.0_default-caps-simdna_assist-v01` | 132,728.0 | 2.0249 |
| `nest-paren-512` | 1,035 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 5,470.5 | 5.2855 |
| `nest-paren-512` | 1,035 | `rust_1.13.1_default-caps-simdna_assist-v01` | 2,430.8 | 2.3486 |
| `nest-paren-512` | 1,035 | `re2_11.0.0_default-caps-simdna_assist-v01` | 2,320.5 | 2.2421 |
| `nest-paren-8k` | 16,395 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 88,249.0 | 5.3827 |
| `nest-paren-8k` | 16,395 | `rust_1.13.1_default-caps-simdna_assist-v01` | 36,898.4 | 2.2506 |
| `nest-paren-8k` | 16,395 | `re2_11.0.0_default-caps-simdna_assist-v01` | 33,632.2 | 2.0514 |
| `splice-1m` | 1,000,009 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 901,717.1 | 0.9017 |
| `splice-1m` | 1,000,009 | `rust_1.13.1_default-caps-simdna_assist-v01` | 2,953,543.9 | 2.9535 |
| `splice-1m` | 1,000,009 | `re2_11.0.0_default-caps-simdna_assist-v01` | 2,068,453.5 | 2.0684 |
| `unterminated-5m` | 5,000,006 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 3,542,527.7 | 0.7085 |
| `unterminated-5m` | 5,000,006 | `rust_1.13.1_default-caps-simdna_assist-v01` | 13,333,230.3 | 2.6666 |
| `unterminated-5m` | 5,000,006 | `re2_11.0.0_default-caps-simdna_assist-v01` | 10,348,372.6 | 2.0697 |

- `rust_1.13.1_default-caps-simdna_assist-v01` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `cscan-onig` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_jit-caps-simdna_lim-ceil1g (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 17,222,071.1 | 1.3498 | 17,164,751.5 | 17,498,695.6 | 122,450.4 | 1.000x | 1.000x | 23 | 100% | scratch |
| 2 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 47,856,813.6 | 3.7508 | 47,748,729.2 | 49,304,496.2 | 623,245.0 | 2.779x | 2.779x | 23 | 100% | scratch |
| 3 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 47,948,253.3 | 3.7580 | 47,865,359.9 | 49,571,982.7 | 751,182.7 | 2.784x | 2.784x | 23 | 100% | scratch |

#### `cscan-onig` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `comment-5m` | 5,000,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 3,513,364.4 | 0.7027 |
| `comment-5m` | 5,000,011 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 8,303,757.9 | 1.6607 |
| `comment-5m` | 5,000,011 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 8,304,739.2 | 1.6609 |
| `define-witness` | 12 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 60.6 | 5.0507 |
| `define-witness` | 12 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 116.4 | 9.7000 |
| `define-witness` | 12 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 115.7 | 9.6426 |
| `idents-1m` | 1,000,007 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 3,556,315.5 | 3.5563 |
| `idents-1m` | 1,000,007 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 10,569,101.5 | 10.5690 |
| `idents-1m` | 1,000,007 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 10,509,199.8 | 10.5091 |
| `literal-100k` | 100,014 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 49,656.1 | 0.4965 |
| `literal-100k` | 100,014 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 30,383.5 | 0.3038 |
| `literal-100k` | 100,014 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 30,417.9 | 0.3041 |
| `nest-brace-100k` | 200,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 2,433,784.4 | 12.1683 |
| `nest-brace-100k` | 200,011 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 11,638,861.1 | 58.1911 |
| `nest-brace-100k` | 200,011 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 11,729,506.2 | 58.6443 |
| `nest-brace-10k` | 20,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 226,821.3 | 11.3348 |
| `nest-brace-10k` | 20,011 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 906,270.2 | 45.2886 |
| `nest-brace-10k` | 20,011 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 906,356.1 | 45.2929 |
| `nest-brace-128` | 267 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 2,739.1 | 10.2587 |
| `nest-brace-128` | 267 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 11,468.5 | 42.9533 |
| `nest-brace-128` | 267 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 11,471.2 | 42.9632 |
| `nest-brace-1k` | 2,059 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 22,069.3 | 10.7185 |
| `nest-brace-1k` | 2,059 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 90,829.7 | 44.1135 |
| `nest-brace-1k` | 2,059 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 90,953.5 | 44.1736 |
| `nest-brace-2k` | 4,107 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 46,319.2 | 11.2781 |
| `nest-brace-2k` | 4,107 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 183,570.7 | 44.6970 |
| `nest-brace-2k` | 4,107 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 183,416.3 | 44.6594 |
| `nest-brace-32k` | 65,547 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 771,484.3 | 11.7699 |
| `nest-brace-32k` | 65,547 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 3,175,031.7 | 48.4390 |
| `nest-brace-32k` | 65,547 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 3,173,440.4 | 48.4147 |
| `nest-brace-512` | 1,035 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 10,965.8 | 10.5950 |
| `nest-brace-512` | 1,035 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 44,855.2 | 43.3383 |
| `nest-brace-512` | 1,035 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 45,289.0 | 43.7574 |
| `nest-brace-8k` | 16,395 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 185,692.9 | 11.3262 |
| `nest-brace-8k` | 16,395 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 741,517.3 | 45.2283 |
| `nest-brace-8k` | 16,395 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 740,543.1 | 45.1688 |
| `nest-digraph-10k` | 40,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 306,166.4 | 7.6521 |
| `nest-digraph-10k` | 40,011 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 1,207,715.3 | 30.1846 |
| `nest-digraph-10k` | 40,011 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 1,208,481.9 | 30.2037 |
| `nest-paren-100k` | 200,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 1,041,359.8 | 5.2065 |
| `nest-paren-100k` | 200,011 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 5,691,487.4 | 28.4559 |
| `nest-paren-100k` | 200,011 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 5,689,467.4 | 28.4458 |
| `nest-paren-10k` | 20,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 105,164.3 | 5.2553 |
| `nest-paren-10k` | 20,011 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 571,861.9 | 28.5774 |
| `nest-paren-10k` | 20,011 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 565,539.7 | 28.2614 |
| `nest-paren-128` | 267 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 1,432.7 | 5.3657 |
| `nest-paren-128` | 267 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 7,397.9 | 27.7076 |
| `nest-paren-128` | 267 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 7,353.3 | 27.5405 |
| `nest-paren-1k` | 2,059 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 10,756.3 | 5.2241 |
| `nest-paren-1k` | 2,059 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 57,828.6 | 28.0858 |
| `nest-paren-1k` | 2,059 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 58,000.4 | 28.1692 |
| `nest-paren-2k` | 4,107 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 21,408.5 | 5.2127 |
| `nest-paren-2k` | 4,107 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 115,449.1 | 28.1103 |
| `nest-paren-2k` | 4,107 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 115,427.4 | 28.1050 |
| `nest-paren-32k` | 65,547 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 341,330.0 | 5.2074 |
| `nest-paren-32k` | 65,547 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 1,860,850.3 | 28.3896 |
| `nest-paren-32k` | 65,547 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 1,860,166.7 | 28.3791 |
| `nest-paren-512` | 1,035 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 5,440.5 | 5.2566 |
| `nest-paren-512` | 1,035 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 29,111.0 | 28.1265 |
| `nest-paren-512` | 1,035 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 29,187.1 | 28.2001 |
| `nest-paren-8k` | 16,395 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 85,493.4 | 5.2146 |
| `nest-paren-8k` | 16,395 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 463,900.0 | 28.2952 |
| `nest-paren-8k` | 16,395 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 463,440.0 | 28.2672 |
| `splice-1m` | 1,000,009 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 903,423.4 | 0.9034 |
| `splice-1m` | 1,000,009 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 2,265,681.7 | 2.2657 |
| `splice-1m` | 1,000,009 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 2,277,038.3 | 2.2770 |
| `unterminated-5m` | 5,000,006 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 3,536,080.9 | 0.7072 |
| `unterminated-5m` | 5,000,006 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 37,788.5 | 0.0076 |
| `unterminated-5m` | 5,000,006 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 37,495.7 | 0.0075 |

### `floor` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 139,835.6 | 0.0071 | 138,205.8 | 141,705.1 | 1,465.1 | 0.982x | 1.000x | scratch |
| 2 | `pcrec_614d45eb3_vm-caps-simdna` | measured | `plain` | same program | 140,088.5 | 0.0071 | 138,546.3 | 141,172.5 | 955.4 | 0.984x | 1.002x | scratch |
| 3 | `pcrec_614d45eb3_auto-caps-simdna` | inconclusive-load | `plain` | same program | 140,627.8 | 0.0071 | 138,489.4 | 143,280.1 | 1,703.0 | 0.988x | 1.006x | scratch |
| 4 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 141,038.5 | 0.0071 | 140,258.3 | 143,666.8 | 1,372.0 | 0.990x | 1.009x | scratch |
| 5 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 142,397.0 | 0.0072 | 139,963.8 | 144,315.5 | 1,545.5 | 1.000x | 1.018x | scratch |
| 6 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 142,861.1 | 0.0072 | 140,317.9 | 143,700.9 | 1,173.0 | 1.003x | 1.022x | scratch |
| 7 | `rust_1.13.1_default-caps-simdna` | inconclusive-load | `plain` | same program | 234,119.2 | 0.0118 | 233,866.1 | 240,240.6 | 2,542.1 | 1.644x | 1.674x | scratch |
| 8 | `rust_1.13.1_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 234,720.1 | 0.0119 | 234,401.4 | 236,884.1 | 925.8 | 1.648x | 1.679x | scratch |
| 9 | `vectorscan_5.4.11_block-som-nocaps-simd` | measured | `plain` | same program | 327,480.2 | 0.0166 | 326,448.0 | 332,301.9 | 2,396.2 | 2.300x | 2.342x | scratch |
| 10 | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | measured | `plain` | same program | 328,550.7 | 0.0166 | 327,219.6 | 331,335.9 | 1,364.9 | 2.307x | 2.350x | scratch |
| 11 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 472,702.1 | 0.0239 | 471,879.1 | 473,330.7 | 554.2 | 3.320x | 3.380x | scratch |
| 12 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 473,671.1 | 0.0240 | 472,082.5 | 477,307.5 | 1,824.3 | 3.326x | 3.387x | scratch |
| 13 | `libpcre2_10.46_jit-caps-simdna_assist-v01` | measured | `plain` | same program | 474,295.1 | 0.0240 | 471,548.3 | 475,707.3 | 1,536.6 | 3.331x | 3.392x | scratch |
| 14 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 888,029.3 | 0.0449 | 887,468.3 | 904,192.9 | 6,534.3 | 6.236x | 6.351x | scratch |
| 15 | `re2_11.0.0_default-caps-simdna_assist-v01` | measured | `plain` | same program | 892,979.3 | 0.0452 | 886,403.7 | 895,629.6 | 3,253.9 | 6.271x | 6.386x | scratch |
| 16 | `oniguruma_6.9.10_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 10,164,232.1 | 0.5143 | 10,159,654.3 | 10,182,077.0 | 8,876.9 | 71.380x | 72.687x | scratch |
| 17 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 10,172,906.0 | 0.5148 | 10,156,038.7 | 10,177,391.1 | 7,499.8 | 71.440x | 72.749x | scratch |
| 18 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 10,176,447.8 | 0.5149 | 10,140,883.9 | 10,216,218.6 | 26,336.8 | 71.465x | 72.774x | scratch |
| 19 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 10,456,670.1 | 0.5291 | 10,419,453.2 | 10,487,491.4 | 26,368.7 | 73.433x | 74.778x | scratch |

_per-subject rows: 30 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)
- `rust_1.13.1_default-caps-simdna_assist-v01` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-json-validate` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna_lim-ceil1g (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 16,703,102.0 | 8.3461 | 16,645,889.2 | 16,809,953.5 | 62,823.2 | 0.030x | 1.000x | 2 | 100% | scratch |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 159,609,809.0 | 79.7532 | 159,495,323.0 | 159,958,085.0 | 159,344.9 | 0.288x | 9.556x | 2 | 100% | scratch |
| 3 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 162,513,085.0 | 81.2039 | 158,826,086.0 | 163,456,883.0 | 1,763,295.2 | 0.293x | 9.730x | 2 | 100% | scratch |
| 4 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 554,045,352.0 | 276.8433 | 552,511,162.0 | 557,785,080.0 | 1,787,571.7 | 1.000x | 33.170x | 2 | 100% | scratch |
| 5 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 558,494,936.0 | 279.0666 | 557,958,696.0 | 563,458,790.0 | 2,033,405.9 | 1.008x | 33.437x | 2 | 100% | scratch |

#### `wild-json-validate` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `js-1m` | 1,000,648 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 6,176,020.2 | 6.1720 |
| `js-1m` | 1,000,648 | `oniguruma_6.9.10_default-caps-simdna` | 75,577,453.0 | 75.5285 |
| `js-1m` | 1,000,648 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 76,762,468.0 | 76.7128 |
| `js-1m` | 1,000,648 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 453,666,608.0 | 453.3728 |
| `js-1m` | 1,000,648 | `libpcre2_10.46_interp-caps-simdna` | 457,086,648.0 | 456.7906 |
| `js-near-1m` | 1,000,648 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 10,547,445.0 | 10.5406 |
| `js-near-1m` | 1,000,648 | `oniguruma_6.9.10_default-caps-simdna` | 83,917,870.0 | 83.8635 |
| `js-near-1m` | 1,000,648 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 85,471,781.0 | 85.4164 |
| `js-near-1m` | 1,000,648 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 101,320,338.0 | 101.2547 |
| `js-near-1m` | 1,000,648 | `libpcre2_10.46_interp-caps-simdna` | 101,581,294.0 | 101.5155 |

### `wild-json-validate-onig` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna_lim-ceil1g (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 15,933,617.2 | 7.9616 | 15,888,619.8 | 16,118,157.2 | 80,142.6 | 0.029x | 1.000x | 2 | 100% | scratch |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 157,961,032.0 | 78.9294 | 157,355,259.0 | 158,778,291.0 | 554,684.5 | 0.283x | 9.914x | 2 | 100% | scratch |
| 3 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 160,400,332.0 | 80.1482 | 159,203,198.0 | 161,307,232.0 | 788,798.9 | 0.288x | 10.067x | 2 | 100% | scratch |
| 4 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 182,004,146.0 | 90.9431 | 181,494,285.0 | 183,211,202.0 | 580,780.0 | 0.326x | 11.423x | 2 | 100% | scratch |
| 5 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 185,127,598.0 | 92.5039 | 184,943,280.0 | 185,309,201.0 | 125,168.8 | 0.332x | 11.619x | 2 | 100% | scratch |
| 6 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 557,693,717.0 | 278.6663 | 556,710,997.0 | 559,811,028.0 | 1,297,990.2 | 1.000x | 35.001x | 2 | 100% | scratch |
| 7 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 559,619,606.0 | 279.6286 | 556,855,607.0 | 565,724,369.0 | 2,959,670.2 | 1.003x | 35.122x | 2 | 100% | scratch |

#### `wild-json-validate-onig` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `js-1m` | 1,000,648 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 5,941,378.0 | 5.9375 |
| `js-1m` | 1,000,648 | `oniguruma_6.9.10_default-caps-simdna` | 74,457,623.0 | 74.4094 |
| `js-1m` | 1,000,648 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 76,280,299.0 | 76.2309 |
| `js-1m` | 1,000,648 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 127,449,959.0 | 127.3674 |
| `js-1m` | 1,000,648 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 129,481,311.0 | 129.3975 |
| `js-1m` | 1,000,648 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 455,278,435.0 | 454.9836 |
| `js-1m` | 1,000,648 | `libpcre2_10.46_interp-caps-simdna` | 457,678,363.0 | 457.3820 |
| `js-near-1m` | 1,000,648 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 9,994,082.5 | 9.9876 |
| `js-near-1m` | 1,000,648 | `oniguruma_6.9.10_default-caps-simdna` | 83,588,379.0 | 83.5342 |
| `js-near-1m` | 1,000,648 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 84,401,183.0 | 84.3465 |
| `js-near-1m` | 1,000,648 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 54,614,200.0 | 54.5788 |
| `js-near-1m` | 1,000,648 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 55,810,928.0 | 55.7748 |
| `js-near-1m` | 1,000,648 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 102,415,282.0 | 102.3490 |
| `js-near-1m` | 1,000,648 | `libpcre2_10.46_interp-caps-simdna` | 101,515,400.0 | 101.4497 |

### `wild-sexp-balanced` / `large-subject-throughput` (unusual@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 2,799,122.1 | 2.1343 | 2,763,369.3 | 2,881,645.1 | 39,670.4 | 0.127x | 1.000x | 9 | 100% | scratch |
| 2 | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | measured | `plain` | same program | 4,893,213.4 | 3.7311 | 4,838,931.2 | 4,943,227.9 | 34,680.4 | 0.222x | 1.748x | 9 | 100% | scratch |
| 3 | `rust_1.13.1_default-caps-simdna_assist-v01` | inconclusive-load | `plain` | same program | 6,632,279.6 | 5.0571 | 6,588,334.9 | 6,653,666.0 | 23,070.1 | 0.300x | 2.369x | 9 | 100% | scratch |
| 4 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 7,704,877.8 | 5.8750 | 7,549,259.0 | 7,806,010.7 | 83,000.6 | 0.349x | 2.753x | 9 | 100% | scratch |
| 5 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | measured | `plain` | same program | 7,818,758.6 | 5.9618 | 7,599,898.4 | 8,773,224.7 | 421,817.2 | 0.354x | 2.793x | 9 | 100% | scratch |
| 6 | `libpcre2_10.46_interp-caps-simdna` | inconclusive-load | `plain` | same program | 22,080,218.3 | 16.8362 | 21,975,061.3 | 22,911,029.9 | 361,530.4 | 1.000x | 7.888x | 9 | 100% | scratch |
| 7 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 22,411,283.6 | 17.0886 | 21,964,669.9 | 22,488,366.9 | 201,738.3 | 1.015x | 8.007x | 9 | 100% | scratch |
| 8 | `re2_11.0.0_default-caps-simdna_assist-v01` | measured | `plain` | same program | 41,176,556.8 | 31.3972 | 41,038,186.0 | 41,501,310.0 | 163,900.6 | 1.865x | 14.711x | 9 | 100% | scratch |
| 9 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | inconclusive-load | `plain` | same program | 40,858,636,323.0 | 31154.7437 | 40,462,531,457.0 | 40,976,932,967.0 | 189,700,612.1 | 1850.463x | 14596.947x | 9 | 100% | scratch |

#### `wild-sexp-balanced` / `large-subject-throughput` per-subject (unusual@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `nest-paren-100k` | 200,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 802,917.9 | 4.0144 |
| `nest-paren-100k` | 200,011 | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | 1,326,999.9 | 6.6346 |
| `nest-paren-100k` | 200,011 | `rust_1.13.1_default-caps-simdna_assist-v01` | 2,681,755.3 | 13.4080 |
| `nest-paren-100k` | 200,011 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 2,553,433.2 | 12.7665 |
| `nest-paren-100k` | 200,011 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 2,633,713.2 | 13.1678 |
| `nest-paren-100k` | 200,011 | `libpcre2_10.46_interp-caps-simdna` | 7,912,901.3 | 39.5623 |
| `nest-paren-100k` | 200,011 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 8,083,571.6 | 40.4156 |
| `nest-paren-100k` | 200,011 | `re2_11.0.0_default-caps-simdna_assist-v01` | 15,881,486.1 | 79.4031 |
| `nest-paren-100k` | 200,011 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 36,181,126,700.0 | 180895.6842 |
| `nest-paren-10k` | 20,011 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 69,260.8 | 3.4611 |
| `nest-paren-10k` | 20,011 | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | 135,662.3 | 6.7794 |
| `nest-paren-10k` | 20,011 | `rust_1.13.1_default-caps-simdna_assist-v01` | 266,189.4 | 13.3022 |
| `nest-paren-10k` | 20,011 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 248,751.7 | 12.4308 |
| `nest-paren-10k` | 20,011 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 249,206.8 | 12.4535 |
| `nest-paren-10k` | 20,011 | `libpcre2_10.46_interp-caps-simdna` | 665,637.7 | 33.2636 |
| `nest-paren-10k` | 20,011 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 676,175.1 | 33.7902 |
| `nest-paren-10k` | 20,011 | `re2_11.0.0_default-caps-simdna_assist-v01` | 1,567,881.6 | 78.3510 |
| `nest-paren-10k` | 20,011 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 358,972,538.0 | 17938.7606 |
| `nest-paren-128` | 267 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 891.9 | 3.3406 |
| `nest-paren-128` | 267 | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | 2,801.3 | 10.4917 |
| `nest-paren-128` | 267 | `rust_1.13.1_default-caps-simdna_assist-v01` | 3,549.9 | 13.2955 |
| `nest-paren-128` | 267 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 3,128.5 | 11.7171 |
| `nest-paren-128` | 267 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 3,123.4 | 11.6982 |
| `nest-paren-128` | 267 | `libpcre2_10.46_interp-caps-simdna` | 9,775.2 | 36.6112 |
| `nest-paren-128` | 267 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 9,859.3 | 36.9261 |
| `nest-paren-128` | 267 | `re2_11.0.0_default-caps-simdna_assist-v01` | 29,543.6 | 110.6501 |
| `nest-paren-128` | 267 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 81,253.0 | 304.3184 |
| `nest-paren-1k` | 2,059 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 7,264.6 | 3.5282 |
| `nest-paren-1k` | 2,059 | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | 16,262.8 | 7.8984 |
| `nest-paren-1k` | 2,059 | `rust_1.13.1_default-caps-simdna_assist-v01` | 27,716.8 | 13.4613 |
| `nest-paren-1k` | 2,059 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 26,769.6 | 13.0013 |
| `nest-paren-1k` | 2,059 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 26,809.5 | 13.0207 |
| `nest-paren-1k` | 2,059 | `libpcre2_10.46_interp-caps-simdna` | 73,465.0 | 35.6800 |
| `nest-paren-1k` | 2,059 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 73,019.0 | 35.4633 |
| `nest-paren-1k` | 2,059 | `re2_11.0.0_default-caps-simdna_assist-v01` | 162,461.1 | 78.9029 |
| `nest-paren-1k` | 2,059 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 3,832,953.0 | 1861.5605 |
| `nest-paren-2k` | 4,107 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 14,165.9 | 3.4492 |
| `nest-paren-2k` | 4,107 | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | 29,779.1 | 7.2508 |
| `nest-paren-2k` | 4,107 | `rust_1.13.1_default-caps-simdna_assist-v01` | 54,583.2 | 13.2903 |
| `nest-paren-2k` | 4,107 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 51,485.1 | 12.5360 |
| `nest-paren-2k` | 4,107 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 51,499.9 | 12.5395 |
| `nest-paren-2k` | 4,107 | `libpcre2_10.46_interp-caps-simdna` | 143,684.8 | 34.9853 |
| `nest-paren-2k` | 4,107 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 143,303.1 | 34.8924 |
| `nest-paren-2k` | 4,107 | `re2_11.0.0_default-caps-simdna_assist-v01` | 317,205.9 | 77.2354 |
| `nest-paren-2k` | 4,107 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 15,188,202.0 | 3698.1256 |
| `nest-paren-32k` | 65,547 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 238,692.4 | 3.6415 |
| `nest-paren-32k` | 65,547 | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | 436,725.0 | 6.6628 |
| `nest-paren-32k` | 65,547 | `rust_1.13.1_default-caps-simdna_assist-v01` | 877,968.3 | 13.3945 |
| `nest-paren-32k` | 65,547 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 829,725.4 | 12.6585 |
| `nest-paren-32k` | 65,547 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 831,777.2 | 12.6898 |
| `nest-paren-32k` | 65,547 | `libpcre2_10.46_interp-caps-simdna` | 2,332,372.8 | 35.5832 |
| `nest-paren-32k` | 65,547 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 2,357,385.9 | 35.9648 |
| `nest-paren-32k` | 65,547 | `re2_11.0.0_default-caps-simdna_assist-v01` | 5,240,796.2 | 79.9548 |
| `nest-paren-32k` | 65,547 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 3,919,793,668.0 | 59801.2673 |
| `nest-paren-512` | 1,035 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 3,454.3 | 3.3375 |
| `nest-paren-512` | 1,035 | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | 9,584.7 | 9.2605 |
| `nest-paren-512` | 1,035 | `rust_1.13.1_default-caps-simdna_assist-v01` | 13,895.9 | 13.4260 |
| `nest-paren-512` | 1,035 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 12,753.0 | 12.3218 |
| `nest-paren-512` | 1,035 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 12,639.6 | 12.2122 |
| `nest-paren-512` | 1,035 | `libpcre2_10.46_interp-caps-simdna` | 36,675.1 | 35.4348 |
| `nest-paren-512` | 1,035 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 36,826.1 | 35.5808 |
| `nest-paren-512` | 1,035 | `re2_11.0.0_default-caps-simdna_assist-v01` | 80,713.2 | 77.9837 |
| `nest-paren-512` | 1,035 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 1,014,282.0 | 979.9826 |
| `nest-paren-8k` | 16,395 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 56,840.6 | 3.4669 |
| `nest-paren-8k` | 16,395 | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | 111,999.7 | 6.8313 |
| `nest-paren-8k` | 16,395 | `rust_1.13.1_default-caps-simdna_assist-v01` | 218,699.7 | 13.3394 |
| `nest-paren-8k` | 16,395 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 207,512.1 | 12.6570 |
| `nest-paren-8k` | 16,395 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 207,409.0 | 12.6508 |
| `nest-paren-8k` | 16,395 | `libpcre2_10.46_interp-caps-simdna` | 583,013.7 | 35.5605 |
| `nest-paren-8k` | 16,395 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 586,169.9 | 35.7530 |
| `nest-paren-8k` | 16,395 | `re2_11.0.0_default-caps-simdna_assist-v01` | 1,286,010.4 | 78.4392 |
| `nest-paren-8k` | 16,395 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 243,734,905.0 | 14866.4169 |
| `sx-1m` | 1,002,042 | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 1,603,365.4 | 1.6001 |
| `sx-1m` | 1,002,042 | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | 2,816,692.0 | 2.8110 |
| `sx-1m` | 1,002,042 | `rust_1.13.1_default-caps-simdna_assist-v01` | 2,488,550.6 | 2.4835 |
| `sx-1m` | 1,002,042 | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 3,764,438.1 | 3.7568 |
| `sx-1m` | 1,002,042 | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 3,787,036.4 | 3.7793 |
| `sx-1m` | 1,002,042 | `libpcre2_10.46_interp-caps-simdna` | 10,326,483.1 | 10.3054 |
| `sx-1m` | 1,002,042 | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 10,435,776.2 | 10.4145 |
| `sx-1m` | 1,002,042 | `re2_11.0.0_default-caps-simdna_assist-v01` | 16,615,023.4 | 16.5812 |
| `sx-1m` | 1,002,042 | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 18,636,681.0 | 18.5987 |

- `rust_1.13.1_default-caps-simdna_assist-v01` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `cscan` | `large-subject-throughput` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 23 | 96% | 0 | 0 | `nest-brace-100k` (timed-out) |
| `cscan` | `large-subject-throughput` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 23 | 96% | 0 | 0 | `nest-brace-100k` (timed-out) |
| `cscan` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 23 | 65% | -46:JIT×8 (smallest: nest-brace-512, 1,035 B) | 0 | `nest-brace-100k` (gave-up), `nest-brace-10k` (gave-up), `nest-brace-1k` (gave-up), `nest-brace-2k` (gave-up), `nest-brace-32k` (gave-up), `nest-brace-512` (gave-up), `nest-brace-8k` (gave-up), `nest-digraph-10k` (gave-up) |
| `cscan` | `large-subject-throughput` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 23 | 57% | 0 | 50 | `define-witness` (wrong), `nest-brace-100k` (wrong), `nest-brace-10k` (wrong), `nest-brace-128` (wrong), `nest-brace-1k` (wrong), `nest-brace-2k` (wrong), `nest-brace-32k` (wrong), `nest-brace-512` (wrong), `nest-brace-8k` (wrong), `nest-digraph-10k` (wrong) |
| `cscan` | `large-subject-throughput` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 23 | 91% | 0 | 5 | `define-witness` (wrong), `nest-brace-100k` (timed-out) |
| `cscan-onig` | `large-subject-throughput` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 23 | 96% | 0 | 0 | `nest-brace-100k` (timed-out) |
| `cscan-onig` | `large-subject-throughput` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 23 | 96% | 0 | 0 | `nest-brace-100k` (timed-out) |
| `cscan-onig` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 23 | 65% | -46:JIT×8 (smallest: nest-brace-512, 1,035 B) | 0 | `nest-brace-100k` (gave-up), `nest-brace-10k` (gave-up), `nest-brace-1k` (gave-up), `nest-brace-2k` (gave-up), `nest-brace-32k` (gave-up), `nest-brace-512` (gave-up), `nest-brace-8k` (gave-up), `nest-digraph-10k` (gave-up) |
| `cscan-onig` | `large-subject-throughput` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 23 | 61% | 0 | 45 | `nest-brace-100k` (wrong), `nest-brace-10k` (wrong), `nest-brace-128` (wrong), `nest-brace-1k` (wrong), `nest-brace-2k` (wrong), `nest-brace-32k` (wrong), `nest-brace-512` (wrong), `nest-brace-8k` (wrong), `nest-digraph-10k` (wrong) |
| `cscan-onig` | `large-subject-throughput` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 23 | 96% | 0 | 0 | `nest-brace-100k` (timed-out) |
| `cscan-onig` | `large-subject-throughput` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 23 | 17% | -3:PCREC_ERR_FRAMES×19 (smallest: nest-brace-128, 267 B) | 0 | `comment-5m` (gave-up), `idents-1m` (gave-up), `nest-brace-100k` (gave-up), `nest-brace-10k` (gave-up), `nest-brace-128` (gave-up), `nest-brace-1k` (gave-up), `nest-brace-2k` (gave-up), `nest-brace-32k` (gave-up), `nest-brace-512` (gave-up), `nest-brace-8k` (gave-up), `nest-digraph-10k` (gave-up), `nest-paren-100k` (gave-up), `nest-paren-10k` (gave-up), `nest-paren-1k` (gave-up), `nest-paren-2k` (gave-up), `nest-paren-32k` (gave-up), `nest-paren-512` (gave-up), `nest-paren-8k` (gave-up), `splice-1m` (gave-up) |
| `cscan-onig` | `large-subject-throughput` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 23 | 17% | -3:PCREC_ERR_FRAMES×19 (smallest: nest-brace-128, 267 B) | 0 | `comment-5m` (gave-up), `idents-1m` (gave-up), `nest-brace-100k` (gave-up), `nest-brace-10k` (gave-up), `nest-brace-128` (gave-up), `nest-brace-1k` (gave-up), `nest-brace-2k` (gave-up), `nest-brace-32k` (gave-up), `nest-brace-512` (gave-up), `nest-brace-8k` (gave-up), `nest-digraph-10k` (gave-up), `nest-paren-100k` (gave-up), `nest-paren-10k` (gave-up), `nest-paren-1k` (gave-up), `nest-paren-2k` (gave-up), `nest-paren-32k` (gave-up), `nest-paren-512` (gave-up), `nest-paren-8k` (gave-up), `splice-1m` (gave-up) |
| `wild-json-validate` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 2 | 0% | -46:JIT×2 (smallest: js-1m, 1,000,648 B) | 0 | `js-1m` (gave-up), `js-near-1m` (gave-up) |
| `wild-json-validate-onig` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 2 | 0% | -46:JIT×2 (smallest: js-1m, 1,000,648 B) | 0 | `js-1m` (gave-up), `js-near-1m` (gave-up) |
| `wild-json-validate-onig` | `large-subject-throughput` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 2 | 0% | -3:PCREC_ERR_FRAMES×2 (smallest: js-1m, 1,000,648 B) | 0 | `js-1m` (gave-up), `js-near-1m` (gave-up) |
| `wild-json-validate-onig` | `large-subject-throughput` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 2 | 0% | -3:PCREC_ERR_FRAMES×2 (smallest: js-1m, 1,000,648 B) | 0 | `js-1m` (gave-up), `js-near-1m` (gave-up) |
| `wild-sexp-balanced` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 9 | 11% | -46:JIT×8 (smallest: nest-paren-512, 1,035 B) | 0 | `nest-paren-100k` (gave-up), `nest-paren-10k` (gave-up), `nest-paren-1k` (gave-up), `nest-paren-2k` (gave-up), `nest-paren-32k` (gave-up), `nest-paren-512` (gave-up), `nest-paren-8k` (gave-up), `sx-1m` (gave-up) |
| `wild-sexp-balanced` | `large-subject-throughput` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 9 | 11% | 0 | 40 | `nest-paren-100k` (wrong), `nest-paren-10k` (wrong), `nest-paren-128` (wrong), `nest-paren-1k` (wrong), `nest-paren-2k` (wrong), `nest-paren-32k` (wrong), `nest-paren-512` (wrong), `nest-paren-8k` (wrong) |
| `wild-sexp-balanced` | `large-subject-throughput` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 9 | 11% | -3:PCREC_ERR_FRAMES×8 (smallest: nest-paren-512, 1,035 B) | 0 | `nest-paren-100k` (gave-up), `nest-paren-10k` (gave-up), `nest-paren-1k` (gave-up), `nest-paren-2k` (gave-up), `nest-paren-32k` (gave-up), `nest-paren-512` (gave-up), `nest-paren-8k` (gave-up), `sx-1m` (gave-up) |
| `wild-sexp-balanced` | `large-subject-throughput` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 9 | 11% | -3:PCREC_ERR_FRAMES×8 (smallest: nest-paren-512, 1,035 B) | 0 | `nest-paren-100k` (gave-up), `nest-paren-10k` (gave-up), `nest-paren-1k` (gave-up), `nest-paren-2k` (gave-up), `nest-paren-32k` (gave-up), `nest-paren-512` (gave-up), `nest-paren-8k` (gave-up), `sx-1m` (gave-up) |

## Standing cross-class query (inbox I-101; Frank's own anomaly check -- a QUERY, never a ranking; every hit below is a finding on pcrec's side by definition)

_0 hits: no included YES-class config's median beats any pcrec `auto-nocaps` row's median in this report's roster._

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_614d45eb3_auto-caps-simdna` / `co-isbn` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,207 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `co-isbn` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,312 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `co-isbn-pass` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,207 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `co-isbn-pass` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,312 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `co-isbn-twin` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, frameless=1, islands=0, shape=inline (prog: 2,058 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `co-isbn-twin` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,161 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `co-luhn` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,719 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `co-luhn` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,822 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `co-luhn-pass` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,719 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `co-luhn-pass` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,822 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `co-luhn-twin` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 1,570 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `co-luhn-twin` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 1,673 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `co-member` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,615 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `co-member` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,718 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `co-member-pass` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,615 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `co-member-pass` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,718 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `co-member-twin` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,1,2,3,4*, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 1,466 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `co-member-twin` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 1,569 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `co-netstr` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,537 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `co-netstr` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,640 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `co-netstr-assist` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,441 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/6 == stamped default (single tier), buffers=2/6 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `co-netstr-assist` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,546 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/6 == stamped default (single tier), buffers=2/6 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `co-netstr-twin` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 1,146 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `co-netstr-twin` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 1,249 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `cscan-onig` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 60,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=37/56 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_614d45eb3_auto-caps-simdna` / `cscan-onig` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 60,198 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=37/56 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_614d45eb3_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=handoff table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_614d45eb3_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_614d45eb3_auto-caps-simdna` / `va-route` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,123 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `va-route` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,229 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `va-tenant` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=1, shape=forward (prog: 2,906 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `va-tenant` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=1, shape=forward (prog: 3,011 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `va-term` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 1,127 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `va-term` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 1,230 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `va-term-bang` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 1,128 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `va-term-bang` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 1,231 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_614d45eb3_auto-caps-simdna` / `wild-json-validate-onig` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=1, shape=plain (prog: 69,569 B), clsfolds=1, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=39/59 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_614d45eb3_auto-caps-simdna` / `wild-json-validate-onig` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=1, shape=plain (prog: 69,676 B), clsfolds=1, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=39/59 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_614d45eb3_auto-caps-simdna` / `wild-sexp-balanced` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,132 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_614d45eb3_auto-caps-simdna` / `wild-sexp-balanced` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,237 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `co-isbn` / `plain`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,207 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `co-isbn` / `whole-subject`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,312 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `co-isbn-pass` / `plain`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,207 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `co-isbn-pass` / `whole-subject`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,312 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `co-isbn-twin` / `plain`: engine=vm, sel=selected, entry=_in, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, frameless=1, islands=0, shape=inline (prog: 2,058 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `co-isbn-twin` / `whole-subject`: engine=vm, sel=selected, entry=_in, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,161 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `co-luhn` / `plain`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,719 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `co-luhn` / `whole-subject`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,822 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `co-luhn-pass` / `plain`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,719 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `co-luhn-pass` / `whole-subject`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,822 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `co-luhn-twin` / `plain`: engine=vm, sel=selected, entry=_in, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=first-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 1,570 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `co-luhn-twin` / `whole-subject`: engine=vm, sel=selected, entry=_in, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 1,673 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `co-member` / `plain`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,615 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `co-member` / `whole-subject`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,718 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `co-member-pass` / `plain`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,615 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `co-member-pass` / `whole-subject`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,718 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `co-member-twin` / `plain`: engine=vm, sel=selected, entry=_in, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,1,2,3,4*, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 1,466 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `co-member-twin` / `whole-subject`: engine=vm, sel=selected, entry=_in, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 1,569 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `co-netstr` / `plain`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,537 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `co-netstr` / `whole-subject`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,640 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `co-netstr-assist` / `plain`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,441 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/6 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `co-netstr-assist` / `whole-subject`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,546 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/6 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `co-netstr-twin` / `plain`: engine=vm, sel=selected, entry=_in, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 1,146 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `co-netstr-twin` / `whole-subject`: engine=vm, sel=selected, entry=_in, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 1,249 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `cscan-onig` / `plain`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 60,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=37/56 fast, escalates to 2048/3072, buffers=10324440/41297760 (caller-provided), frame=40
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `cscan-onig` / `whole-subject`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 60,198 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=37/56 fast, escalates to 2048/3072, buffers=10324440/41297760 (caller-provided), frame=40
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=handoff table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `va-route` / `plain`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,123 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `va-route` / `whole-subject`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,229 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `va-tenant` / `plain`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=1, shape=forward (prog: 2,906 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `va-tenant` / `whole-subject`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=1, shape=forward (prog: 3,011 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `va-term` / `plain`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 1,127 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `va-term` / `whole-subject`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 1,230 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `va-term-bang` / `plain`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 1,128 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `va-term-bang` / `whole-subject`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 1,231 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `wild-json-validate-onig` / `plain`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=1, shape=plain (prog: 69,569 B), clsfolds=1, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=39/59 fast, escalates to 2048/3072, buffers=10324440/41297760 (caller-provided), frame=40
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `wild-json-validate-onig` / `whole-subject`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=1, shape=plain (prog: 69,676 B), clsfolds=1, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=39/59 fast, escalates to 2048/3072, buffers=10324440/41297760 (caller-provided), frame=40
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `wild-sexp-balanced` / `plain`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,132 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/70 fast, escalates to 2048/3072, buffers=10324440/41297760 (caller-provided), frame=40
- `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` / `wild-sexp-balanced` / `whole-subject`: engine=vm, sel=selected, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,237 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/70 fast, escalates to 2048/3072, buffers=10324440/41297760 (caller-provided), frame=40
- `pcrec_614d45eb3_vm-caps-simdna` / `co-isbn` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,207 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `co-isbn` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,312 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `co-isbn-pass` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,207 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `co-isbn-pass` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,312 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `co-isbn-twin` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,058 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `co-isbn-twin` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,161 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `co-luhn` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,719 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `co-luhn` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,822 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `co-luhn-pass` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,719 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `co-luhn-pass` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,822 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `co-luhn-twin` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 1,570 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `co-luhn-twin` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 1,673 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `co-member` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,615 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `co-member` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,718 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `co-member-pass` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,615 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `co-member-pass` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,718 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `co-member-twin` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 1,466 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `co-member-twin` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 1,569 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `co-netstr` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,537 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `co-netstr` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,640 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `co-netstr-assist` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,441 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/6 == stamped default (single tier), buffers=2/6 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `co-netstr-assist` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,546 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/6 == stamped default (single tier), buffers=2/6 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `co-netstr-twin` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 1,146 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `co-netstr-twin` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 1,249 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `cscan-onig` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 60,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=37/56 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_614d45eb3_vm-caps-simdna` / `cscan-onig` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 60,198 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=37/56 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_614d45eb3_vm-caps-simdna` / `floor` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 314 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `floor` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 417 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `va-route` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,123 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `va-route` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,229 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `va-tenant` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=1, shape=forward (prog: 2,906 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `va-tenant` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=1, shape=forward (prog: 3,011 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `va-term` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 1,127 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `va-term` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 1,230 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `va-term-bang` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 1,128 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `va-term-bang` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 1,231 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_614d45eb3_vm-caps-simdna` / `wild-json-validate-onig` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=1, shape=plain (prog: 69,569 B), clsfolds=1, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=39/59 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_614d45eb3_vm-caps-simdna` / `wild-json-validate-onig` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=1, shape=plain (prog: 69,676 B), clsfolds=1, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=39/59 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_614d45eb3_vm-caps-simdna` / `wild-sexp-balanced` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,132 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_614d45eb3_vm-caps-simdna` / `wild-sexp-balanced` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,237 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `co-isbn` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,207 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `co-isbn` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,312 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `co-isbn-pass` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,207 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `co-isbn-pass` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,312 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `co-isbn-twin` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,058 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `co-isbn-twin` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,161 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `co-luhn` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,719 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `co-luhn` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,822 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `co-luhn-pass` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,719 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `co-luhn-pass` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,822 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `co-luhn-twin` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 1,570 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `co-luhn-twin` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 1,673 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `co-member` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,615 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `co-member` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,718 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `co-member-pass` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,615 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `co-member-pass` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,718 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `co-member-twin` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 1,466 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `co-member-twin` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 1,569 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `co-netstr` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,537 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `co-netstr` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,640 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `co-netstr-assist` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,441 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/6 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `co-netstr-assist` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,546 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/6 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `co-netstr-twin` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 1,146 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `co-netstr-twin` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 1,249 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `cscan-onig` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 60,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=37/56 fast, escalates to 2048/3072, buffers=10324440/41297760 (caller-provided), frame=40
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `cscan-onig` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 60,198 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=37/56 fast, escalates to 2048/3072, buffers=10324440/41297760 (caller-provided), frame=40
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `floor` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 314 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `floor` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 417 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `va-route` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,123 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `va-route` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,229 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `va-tenant` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=1, shape=forward (prog: 2,906 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `va-tenant` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=1, shape=forward (prog: 3,011 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `va-term` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 1,127 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `va-term` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 1,230 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `va-term-bang` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 1,128 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `va-term-bang` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 1,231 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=12201611/48806444 (caller-provided), frame=24
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `wild-json-validate-onig` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=1, shape=plain (prog: 69,569 B), clsfolds=1, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=39/59 fast, escalates to 2048/3072, buffers=10324440/41297760 (caller-provided), frame=40
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `wild-json-validate-onig` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=1, shape=plain (prog: 69,676 B), clsfolds=1, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=39/59 fast, escalates to 2048/3072, buffers=10324440/41297760 (caller-provided), frame=40
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `wild-sexp-balanced` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,132 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/70 fast, escalates to 2048/3072, buffers=10324440/41297760 (caller-provided), frame=40
- `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` / `wild-sexp-balanced` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,237 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/70 fast, escalates to 2048/3072, buffers=10324440/41297760 (caller-provided), frame=40
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced), and NOTHING else -- since pcrec 263b013 ([LIM-1] / [OPT-4.1]) every fallback has its own token (`overflowed-dfa`, `overflowed-prefilter`, `collapsed-prefilter`, `declined-nullable`, `size-cap-retry`), the size-cap rescue included; at pcrec 96e44c2 that rescue stamped `sel=selected` and only its `lang=count-collapsed (size cap retry, ...)` clause says so.
    - K = pcrec's `RX_UNROLL_K`/`_WHY`: the VM counter rung's unroll factor and who chose it (default / option / denied / size-model / size-model-declined / cap-rescue / capacity-declined -- limits.md 8); caps = the EFFECTIVE `RX_MAX_EMIT_CODE_BYTES`/`RX_MAX_EMIT_BYTES` the artifact was built under (raise-only; 500,000/1,000,000 by default). VM artifacts only: a DFA artifact has no counter rung and stamps no code cap.
    - edge = pcrec's `RX_DFA_SCAN_EDGE` ([OPT-5] STEP 1, abi 13+), how a DFA scan tests a SCAN EDGE's byte class: `range` = a contiguous run (subtract-and-compare against two immediates); `bitmap` = a non-contiguous class (a 256-byte membership read); `mixed` = one artifact whose machines took both forms; `none` = no collapsible run (an attempt/empty scan, or -fno-scan-edge).
    - edges = pcrec's `scan_edges` ([B32]): how many [OPT-5] SCAN EDGES this artifact's SEARCH-side machines carry (`rx_search`/`rx_prefilter`), the per-scan-iteration compare-count covariate `edge`'s single shape token cannot separate (I-33: the cost is one compare per edge per iteration); the `(match: M)` parenthetical, when carried, is the SAME count on the anchored `rx_match` machine, kept apart because the measured [OPT-EDGE] regression is search-band only. `0` is a real, recorded value.
    - start = pcrec's `RX_DFA_START` ([OPT-5] STEP 2, abi 16+), how the SEARCH entry recovers the match START: `pinned` = the forward machine's start state accepts unconditionally, so the match provably begins at `search_from` and THE ARTIFACT CARRIES NO REVERSE MACHINE at all (no reverse tables, accessor block or scan loop); `reverse-pass` = it carries one and walks it backwards from the match end. The two forms are ANSWER-IDENTICAL by contract -- `caps[0][0]`'s absolute offsets and the zero-length-match convention hold under both -- so this explains a row's SIZE and pass count, never its answer.
      - start=end-minus-width: every match is one fixed byte width W, so the start is the verified end minus W; NO reverse machine (abi 74, [START-LANDING])
      - prefilter=handoff: the forward scan RE-ENTERS the pre-check handoff at each restart: it re-finds the one-byte or run landmark and moves to hit - K (K = `REQ_HANDOFF`) when that is ahead (abi 75, [REQ-HANDOFF-L1]); removed by `-fno-req-handoff`, which also removes the K82 entry handoff
    - frameless = pcrec's `RX_VM_FRAMELESS` ([OPT-VMFL], abi 16+): `1` iff this VM program emits NO push site and no linked call, so its fail label carries no pop-and-resume dispatch; `0` otherwise. VM artifacts only, hybrids included -- a DIFFERENT scope from `start=`, though the two stamps arrived at one abi. It is NOT `buffers=`'s resume-frame CAPACITY and the two can disagree: the capacity is what the artifact was SIZED for, this is what its program CONTAINS. `0` is a real, recorded value.
    - folds = pcrec's `RX_DFA_UNIFORM_FOLDS` ([CC-DIFF] STEP 1, abi 17+): how many of this artifact's DFA tables (two per machine it contains -- forward always, reverse unless `start=pinned`, anchored under `match=unwrapped`; so 0..6) had ALL-EQUAL cells and were NOT EMITTED, the accessor returning the constant. `table=` keeps naming the encoding that was SELECTED, so `premultiplied` beside `folds=4` is an artifact carrying NO transition table at all -- a SIZE fact, never an answer one. `0` is a real, recorded value.
    - islands = pcrec's `RX_VM_ALT_ISLANDS` ([ENG-ISL] STEP 1, abi 18+): how many of this VM program's flat alternations were lowered as an ALTERNATION ISLAND -- a trie dispatch over the alternatives' literal bytes -- instead of vm_alt's serial resume chain (one frame per untried branch). Selected per alternation on its LANGUAGE (a finite literal set), so a COUNT; a caseless, prefix-bearing-under-four-words or over-budget alternation is declined as a selection outcome. This is what removes the branch-ORDER effect (altwide srt-256 vs w-256) at the source; `-fno-alt-island` is the sibling that reads `0` at the same pin. `0` is a real, recorded value.
    - shape = pcrec's `RX_VM_ENTRY_SHAPE` with `RX_VM_PROGRAM_BYTES` in the parenthetical ([CC-DIFF] STEP 2, abi 22+): the entry-chain rung the emitter TOOK for the six entries -- `plain` (one body, six framed entries), `shared` (one out-of-line body behind three forwarding entries), `forward` (three bodies in the three `_in` entries, no canary anywhere), `inline` (six bodies) -- and the program size AUTO compared against VM_INLINE_CHAIN_MAX_BYTES (4,096 B) to choose it: `forward` at or below, `shared` above; `inline`/`plain` where a forward rung is illegal (the program writes its storage); a FRAMED program (`frameless=0`) is `plain` whatever the size. ANSWER-IDENTICAL across every value -- only the scaffolding above the first label moves -- so a COST and SIZE fact; the number is what makes the token checkable. `prog: N B` is the VM PROGRAM REGION with its COMMENTS INCLUDED (the raw length of the emitter's program buffer; the island trie writes a per-node comment), NOT the `code bytes` columns' quantity -- those and `--max-emit-code-bytes` count the whole .c+.h with every comment EXCLUDED -- so the program stamp can exceed the code bytes (w-256: 305,686 vs 292,043) and neither is wrong; for cap reasoning use the code bytes (pcrec I-50 1).
    - clsfolds = pcrec's `RX_VM_CLS_FOLDS` ([FORM-CHAR] STEP 1, abi 23+): how many of this VM program's class-pool entries take the ASCII-FOLD membership test -- a two-member set differing only in bit 0x20, both letters (what `(?i)` makes of a letter at parse time), tested as `(byte | 0x20) == lower` with NO 32-byte bitmap table emitted for it. Chosen per pool class, so a COUNT; a set that is not exactly two members, not a 0x20 pair, or a 0x20 pair of non-letters keeps its bitmap. A SIZE fact (one table per fold class gone, plus the test text), never an answer one: the fold compare and the bitmap read are the same predicate over the pair's two bytes. VM route only -- an `auto` row that selected the DFA prints no clause even on a `(?i)` pattern; `-fno-cls-fold` is the sibling that reads `0` at the same pin. `0` is a real, recorded value.

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | emit bytes | code bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `co-isbn` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 362,594,954.0 | 360,716,967.0 | 364,482,310.0 | 1,336,736.1 | 5 | 55,464 | 27,015 | 25,316 | 0.004 (max is trial 1) | compiled=5 | 1,651,842.0 | 360,946,098.0 | 74,400.0 |
| `co-isbn` | `whole-subject` | `pcrec_614d45eb3_auto-caps-simdna` | 370,717,416.0 | 369,082,926.0 | 372,674,524.0 | 1,160,969.3 | 5 | 55,464 | 27,244 | 25,545 | 0.003 (max is trial 1) | compiled=5 | 1,705,413.0 | 368,947,251.0 | 71,635.0 |
| `co-isbn` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 374,068,281.0 | 370,138,286.0 | 375,057,646.0 | 1,814,042.6 | 5 | 55,464 | 27,053 | 25,354 | 0.005 | compiled=5 | 1,570,861.0 | 372,455,672.0 | 65,463.0 |
| `co-isbn` | `whole-subject` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 391,677,014.0 | 379,023,179.0 | 395,106,238.0 | 6,044,751.6 | 5 | 55,464 | 27,282 | 25,583 | 0.015 | compiled=5 | 1,623,980.0 | 389,992,972.0 | 63,049.0 |
| `co-isbn` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 363,308,155.0 | 362,658,230.0 | 364,767,093.0 | 762,561.1 | 5 | 55,464 | 27,013 | 25,314 | 0.002 (max is trial 1) | compiled=5 | 1,629,862.0 | 361,567,023.0 | 77,036.0 |
| `co-isbn` | `whole-subject` | `pcrec_614d45eb3_vm-caps-simdna` | 381,611,014.0 | 371,167,204.0 | 385,467,801.0 | 5,178,050.3 | 5 | 55,464 | 27,242 | 25,543 | 0.014 | compiled=5 | 1,669,666.0 | 379,730,410.0 | 77,205.0 |
| `co-isbn` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 373,954,887.0 | 370,751,471.0 | 377,317,675.0 | 2,494,993.8 | 5 | 55,464 | 27,051 | 25,352 | 0.007 (max is trial 1) | compiled=5 | 1,693,441.0 | 372,081,427.0 | 61,395.0 |
| `co-isbn` | `whole-subject` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 370,534,232.0 | 369,741,888.0 | 374,574,286.0 | 1,706,788.4 | 5 | 55,464 | 27,280 | 25,581 | 0.005 (max is trial 1) | compiled=5 | 1,616,196.0 | 368,901,385.0 | 74,841.0 |
| `co-isbn-nofn` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `co-isbn-nofn` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `co-isbn-nofn` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `co-isbn-nofn` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `co-isbn-pass` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 374,904,484.0 | 363,553,320.0 | 381,796,679.0 | 6,545,242.1 | 5 | 55,464 | 27,015 | 25,316 | 0.017 | compiled=5 | 1,695,665.0 | 373,268,092.0 | 63,320.0 |
| `co-isbn-pass` | `whole-subject` | `pcrec_614d45eb3_auto-caps-simdna` | 382,361,414.0 | 379,895,277.0 | 389,368,194.0 | 3,306,061.5 | 5 | 55,464 | 27,244 | 25,545 | 0.009 | compiled=5 | 1,723,066.0 | 380,576,601.0 | 55,745.0 |
| `co-isbn-pass` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 378,157,187.0 | 375,297,768.0 | 379,532,039.0 | 1,555,963.7 | 5 | 55,464 | 27,053 | 25,354 | 0.004 | compiled=5 | 1,597,972.0 | 376,610,422.0 | 58,811.0 |
| `co-isbn-pass` | `whole-subject` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 372,806,694.0 | 372,131,651.0 | 384,822,548.0 | 4,918,233.2 | 5 | 55,464 | 27,282 | 25,583 | 0.013 (max is trial 1) | compiled=5 | 1,662,062.0 | 371,015,028.0 | 63,370.0 |
| `co-isbn-pass` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 372,863,461.0 | 372,623,519.0 | 379,773,891.0 | 2,744,550.3 | 5 | 55,464 | 27,013 | 25,314 | 0.007 (max is trial 1) | compiled=5 | 1,524,142.0 | 371,166,072.0 | 63,369.0 |
| `co-isbn-pass` | `whole-subject` | `pcrec_614d45eb3_vm-caps-simdna` | 371,548,953.0 | 368,810,202.0 | 378,533,184.0 | 3,512,631.9 | 5 | 55,464 | 27,242 | 25,543 | 0.009 (max is trial 1) | compiled=5 | 1,597,110.0 | 369,973,043.0 | 62,538.0 |
| `co-isbn-pass` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 361,475,951.0 | 359,500,577.0 | 363,074,514.0 | 1,337,947.7 | 5 | 55,464 | 27,051 | 25,352 | 0.004 | compiled=5 | 1,671,960.0 | 359,954,194.0 | 60,063.0 |
| `co-isbn-pass` | `whole-subject` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 370,352,609.0 | 369,941,073.0 | 374,732,043.0 | 1,824,028.9 | 5 | 55,464 | 27,280 | 25,581 | 0.005 | compiled=5 | 1,524,543.0 | 368,819,821.0 | 64,272.0 |
| `co-isbn-twin` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 248,976,449.0 | 248,507,525.0 | 250,681,120.0 | 794,148.7 | 5 | 37,264 | 30,166 | 27,144 | 0.003 (max is trial 1) | compiled=5 | 3,762,559.0 | 245,160,770.0 | 54,302.0 |
| `co-isbn-twin` | `whole-subject` | `pcrec_614d45eb3_auto-caps-simdna` | 228,307,628.0 | 227,615,425.0 | 230,512,192.0 | 1,015,321.0 | 5 | 37,208 | 30,067 | 26,599 | 0.004 | compiled=5 | 2,550,285.0 | 225,629,392.0 | 52,539.0 |
| `co-isbn-twin` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 249,173,313.0 | 246,505,075.0 | 250,009,961.0 | 1,183,769.4 | 5 | 37,264 | 30,204 | 27,182 | 0.005 (max is trial 1) | compiled=5 | 3,776,878.0 | 245,351,922.0 | 49,854.0 |
| `co-isbn-twin` | `whole-subject` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 227,008,093.0 | 226,542,385.0 | 227,968,252.0 | 543,286.3 | 5 | 37,208 | 30,105 | 26,637 | 0.002 | compiled=5 | 2,516,983.0 | 224,611,736.0 | 51,527.0 |
| `co-isbn-twin` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 251,639,991.0 | 251,285,272.0 | 252,955,411.0 | 622,567.9 | 5 | 37,008 | 25,417 | 23,718 | 0.002 | compiled=5 | 1,576,320.0 | 250,044,595.0 | 50,355.0 |
| `co-isbn-twin` | `whole-subject` | `pcrec_614d45eb3_vm-caps-simdna` | 252,478,641.0 | 251,428,071.0 | 258,722,125.0 | 2,693,092.5 | 5 | 37,008 | 25,644 | 23,945 | 0.011 | compiled=5 | 1,650,630.0 | 250,797,904.0 | 43,051.0 |
| `co-isbn-twin` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 250,607,551.0 | 249,027,933.0 | 252,373,759.0 | 1,110,337.8 | 5 | 37,008 | 25,455 | 23,756 | 0.004 | compiled=5 | 1,554,921.0 | 249,000,101.0 | 52,869.0 |
| `co-isbn-twin` | `whole-subject` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 251,216,759.0 | 250,625,665.0 | 251,351,162.0 | 295,304.9 | 5 | 37,008 | 25,682 | 23,983 | 0.001 | compiled=5 | 1,462,726.0 | 249,709,267.0 | 48,231.0 |
| `co-luhn` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 322,822,123.0 | 319,985,928.0 | 332,267,678.0 | 4,354,330.4 | 5 | 51,368 | 25,673 | 23,974 | 0.013 (max is trial 1) | compiled=5 | 1,409,917.0 | 321,332,667.0 | 76,153.0 |
| `co-luhn` | `whole-subject` | `pcrec_614d45eb3_auto-caps-simdna` | 337,904,639.0 | 330,514,835.0 | 339,364,257.0 | 3,196,545.1 | 5 | 51,368 | 25,900 | 24,201 | 0.009 | compiled=5 | 1,544,851.0 | 336,280,969.0 | 78,819.0 |
| `co-luhn` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 321,993,886.0 | 321,785,364.0 | 322,821,635.0 | 458,570.5 | 5 | 51,368 | 25,711 | 24,012 | 0.001 (max is trial 1) | compiled=5 | 1,517,960.0 | 320,427,304.0 | 78,408.0 |
| `co-luhn` | `whole-subject` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 329,619,096.0 | 329,039,112.0 | 330,339,303.0 | 439,654.2 | 5 | 51,368 | 25,938 | 24,239 | 0.001 | compiled=5 | 1,429,995.0 | 328,124,459.0 | 75,503.0 |
| `co-luhn` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 323,063,048.0 | 322,464,862.0 | 324,049,287.0 | 608,659.1 | 5 | 51,368 | 25,671 | 23,972 | 0.002 | compiled=5 | 1,397,774.0 | 321,646,018.0 | 76,634.0 |
| `co-luhn` | `whole-subject` | `pcrec_614d45eb3_vm-caps-simdna` | 339,172,494.0 | 338,328,624.0 | 341,345,669.0 | 1,032,596.1 | 5 | 51,368 | 25,898 | 24,199 | 0.003 | compiled=5 | 1,539,291.0 | 337,825,326.0 | 64,341.0 |
| `co-luhn` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 322,031,329.0 | 321,183,772.0 | 324,603,857.0 | 1,168,128.2 | 5 | 51,368 | 25,709 | 24,010 | 0.004 (max is trial 1) | compiled=5 | 1,413,995.0 | 320,499,271.0 | 77,336.0 |
| `co-luhn` | `whole-subject` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 327,666,988.0 | 327,594,882.0 | 329,900,487.0 | 1,045,550.1 | 5 | 51,368 | 25,936 | 24,237 | 0.003 | compiled=5 | 1,486,431.0 | 326,134,290.0 | 77,295.0 |
| `co-luhn-nofn` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `co-luhn-nofn` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `co-luhn-nofn` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `co-luhn-nofn` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `co-luhn-pass` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 332,848,682.0 | 332,583,923.0 | 335,809,170.0 | 1,422,287.7 | 5 | 51,368 | 25,673 | 23,974 | 0.004 | compiled=5 | 1,478,766.0 | 331,314,882.0 | 55,034.0 |
| `co-luhn-pass` | `whole-subject` | `pcrec_614d45eb3_auto-caps-simdna` | 329,292,833.0 | 327,483,255.0 | 341,439,017.0 | 5,227,851.6 | 5 | 51,368 | 25,900 | 24,201 | 0.016 (max is trial 1) | compiled=5 | 1,429,253.0 | 327,809,609.0 | 57,499.0 |
| `co-luhn-pass` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 322,025,025.0 | 321,831,820.0 | 327,166,444.0 | 2,051,549.0 | 5 | 51,368 | 25,711 | 24,012 | 0.006 | compiled=5 | 1,504,916.0 | 320,475,865.0 | 63,480.0 |
| `co-luhn-pass` | `whole-subject` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 328,396,182.0 | 327,802,732.0 | 330,204,449.0 | 813,795.7 | 5 | 51,368 | 25,938 | 24,239 | 0.002 | compiled=5 | 1,552,366.0 | 326,796,687.0 | 51,788.0 |
| `co-luhn-pass` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 333,926,538.0 | 331,427,349.0 | 339,215,085.0 | 2,772,596.3 | 5 | 51,368 | 25,671 | 23,972 | 0.008 | compiled=5 | 1,561,873.0 | 332,588,087.0 | 60,965.0 |
| `co-luhn-pass` | `whole-subject` | `pcrec_614d45eb3_vm-caps-simdna` | 331,333,122.0 | 328,191,903.0 | 334,562,337.0 | 2,336,866.4 | 5 | 51,368 | 25,898 | 24,199 | 0.007 (max is trial 1) | compiled=5 | 1,468,226.0 | 329,624,833.0 | 60,314.0 |
| `co-luhn-pass` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 321,943,994.0 | 321,476,463.0 | 323,580,668.0 | 716,433.9 | 5 | 51,368 | 25,709 | 24,010 | 0.002 (max is trial 1) | compiled=5 | 1,378,368.0 | 320,566,798.0 | 63,019.0 |
| `co-luhn-pass` | `whole-subject` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 337,884,543.0 | 335,719,795.0 | 339,900,132.0 | 1,409,142.7 | 5 | 51,368 | 25,936 | 24,237 | 0.004 | compiled=5 | 1,574,747.0 | 336,250,684.0 | 58,330.0 |
| `co-luhn-twin` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 210,285,354.0 | 209,295,870.0 | 210,588,176.0 | 489,596.0 | 5 | 37,504 | 33,559 | 26,734 | 0.002 | compiled=5 | 3,095,181.0 | 207,199,601.0 | 52,779.0 |
| `co-luhn-twin` | `whole-subject` | `pcrec_614d45eb3_auto-caps-simdna` | 205,407,073.0 | 204,134,356.0 | 206,183,537.0 | 754,342.3 | 5 | 37,208 | 29,258 | 26,094 | 0.004 | compiled=5 | 2,097,612.0 | 203,044,413.0 | 50,505.0 |
| `co-luhn-twin` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 207,625,816.0 | 206,349,711.0 | 208,837,749.0 | 850,939.8 | 5 | 37,504 | 33,597 | 26,772 | 0.004 (max is trial 1) | compiled=5 | 3,124,808.0 | 204,739,226.0 | 53,902.0 |
| `co-luhn-twin` | `whole-subject` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 204,844,394.0 | 202,374,550.0 | 205,638,332.0 | 1,164,991.5 | 5 | 37,208 | 29,296 | 26,132 | 0.006 | compiled=5 | 2,209,744.0 | 202,595,607.0 | 52,359.0 |
| `co-luhn-twin` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 210,088,773.0 | 209,367,324.0 | 211,136,387.0 | 624,110.8 | 5 | 36,960 | 24,075 | 22,376 | 0.003 | compiled=5 | 1,379,008.0 | 208,561,806.0 | 54,362.0 |
| `co-luhn-twin` | `whole-subject` | `pcrec_614d45eb3_vm-caps-simdna` | 211,019,076.0 | 209,199,378.0 | 211,879,167.0 | 1,065,442.1 | 5 | 36,960 | 24,302 | 22,603 | 0.005 | compiled=5 | 1,393,476.0 | 209,477,341.0 | 51,768.0 |
| `co-luhn-twin` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 220,344,389.0 | 218,144,835.0 | 221,960,515.0 | 1,221,467.8 | 5 | 36,960 | 24,113 | 22,414 | 0.006 | compiled=5 | 1,293,898.0 | 218,749,824.0 | 48,792.0 |
| `co-luhn-twin` | `whole-subject` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 220,256,323.0 | 219,285,352.0 | 222,371,218.0 | 1,088,547.8 | 5 | 36,960 | 24,340 | 22,641 | 0.005 (max is trial 1) | compiled=5 | 1,325,027.0 | 218,884,989.0 | 52,158.0 |
| `co-member` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 331,710,799.0 | 322,581,679.0 | 334,623,627.0 | 4,408,935.1 | 5 | 51,368 | 26,399 | 24,700 | 0.013 | compiled=5 | 1,706,585.0 | 329,852,428.0 | 77,135.0 |
| `co-member` | `whole-subject` | `pcrec_614d45eb3_auto-caps-simdna` | 333,187,730.0 | 332,987,615.0 | 335,744,898.0 | 1,037,754.4 | 5 | 51,368 | 26,512 | 24,813 | 0.003 | compiled=5 | 1,742,142.0 | 331,552,790.0 | 69,261.0 |
| `co-member` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 321,581,288.0 | 319,513,692.0 | 323,087,246.0 | 1,340,436.2 | 5 | 51,368 | 26,437 | 24,738 | 0.004 | compiled=5 | 1,672,522.0 | 319,821,402.0 | 75,612.0 |
| `co-member` | `whole-subject` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 324,308,387.0 | 322,103,512.0 | 325,874,078.0 | 1,371,478.3 | 5 | 51,368 | 26,550 | 24,851 | 0.004 | compiled=5 | 1,691,988.0 | 322,499,959.0 | 78,087.0 |
| `co-member` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 335,611,153.0 | 331,542,416.0 | 338,562,996.0 | 2,324,432.5 | 5 | 51,368 | 26,397 | 24,698 | 0.007 (max is trial 1) | compiled=5 | 1,836,852.0 | 332,471,547.0 | 74,470.0 |
| `co-member` | `whole-subject` | `pcrec_614d45eb3_vm-caps-simdna` | 334,108,441.0 | 330,066,646.0 | 338,785,835.0 | 3,016,675.0 | 5 | 51,368 | 26,510 | 24,811 | 0.009 | compiled=5 | 1,730,792.0 | 332,274,416.0 | 65,022.0 |
| `co-member` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 321,458,830.0 | 320,342,666.0 | 322,558,302.0 | 762,372.6 | 5 | 51,368 | 26,435 | 24,736 | 0.002 | compiled=5 | 1,822,274.0 | 319,115,784.0 | 75,503.0 |
| `co-member` | `whole-subject` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 324,037,719.0 | 323,367,787.0 | 324,901,456.0 | 526,990.8 | 5 | 51,368 | 26,548 | 24,849 | 0.002 | compiled=5 | 1,632,276.0 | 322,342,685.0 | 79,069.0 |
| `co-member-nofn` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `co-member-nofn` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `co-member-nofn` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `co-member-nofn` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `co-member-pass` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 322,745,469.0 | 321,651,286.0 | 332,665,096.0 | 4,066,797.5 | 5 | 51,368 | 26,399 | 24,700 | 0.013 (max is trial 1) | compiled=5 | 1,654,256.0 | 321,122,270.0 | 59,141.0 |
| `co-member-pass` | `whole-subject` | `pcrec_614d45eb3_auto-caps-simdna` | 323,982,708.0 | 323,236,744.0 | 326,052,919.0 | 1,082,692.6 | 5 | 51,368 | 26,512 | 24,813 | 0.003 | compiled=5 | 1,654,948.0 | 322,191,915.0 | 62,127.0 |
| `co-member-pass` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 321,893,206.0 | 320,226,606.0 | 322,390,875.0 | 751,944.8 | 5 | 51,368 | 26,437 | 24,738 | 0.002 (max is trial 1) | compiled=5 | 1,649,659.0 | 320,185,247.0 | 60,995.0 |
| `co-member-pass` | `whole-subject` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 324,537,790.0 | 322,871,198.0 | 324,741,463.0 | 724,424.2 | 5 | 51,368 | 26,550 | 24,851 | 0.002 | compiled=5 | 1,627,446.0 | 322,720,114.0 | 61,476.0 |
| `co-member-pass` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 322,437,349.0 | 320,879,102.0 | 324,741,751.0 | 1,561,289.9 | 5 | 51,368 | 26,397 | 24,698 | 0.005 (max is trial 1) | compiled=5 | 1,556,473.0 | 320,662,875.0 | 63,740.0 |
| `co-member-pass` | `whole-subject` | `pcrec_614d45eb3_vm-caps-simdna` | 324,579,185.0 | 323,855,561.0 | 325,497,234.0 | 550,910.4 | 5 | 51,368 | 26,510 | 24,811 | 0.002 | compiled=5 | 1,705,995.0 | 322,806,855.0 | 64,592.0 |
| `co-member-pass` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 332,985,341.0 | 321,400,099.0 | 334,156,318.0 | 4,768,316.9 | 5 | 51,368 | 26,435 | 24,736 | 0.014 | compiled=5 | 1,575,649.0 | 331,351,893.0 | 56,607.0 |
| `co-member-pass` | `whole-subject` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 347,048,974.0 | 343,667,371.0 | 348,877,059.0 | 2,026,243.4 | 5 | 51,368 | 26,548 | 24,849 | 0.006 | compiled=5 | 1,675,788.0 | 345,240,857.0 | 53,451.0 |
| `co-member-twin` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 199,099,271.0 | 198,494,670.0 | 200,197,689.0 | 691,178.2 | 5 | 37,448 | 33,931 | 27,719 | 0.003 | compiled=5 | 3,091,744.0 | 196,007,456.0 | 48,531.0 |
| `co-member-twin` | `whole-subject` | `pcrec_614d45eb3_auto-caps-simdna` | 191,744,433.0 | 190,839,929.0 | 193,541,259.0 | 1,057,283.9 | 5 | 37,208 | 28,704 | 25,873 | 0.006 | compiled=5 | 2,193,913.0 | 189,615,142.0 | 53,470.0 |
| `co-member-twin` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 204,389,908.0 | 199,610,050.0 | 205,035,664.0 | 2,039,617.1 | 5 | 37,448 | 33,969 | 27,757 | 0.010 | compiled=5 | 3,414,796.0 | 200,943,423.0 | 50,616.0 |
| `co-member-twin` | `whole-subject` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 194,391,427.0 | 194,344,677.0 | 194,989,211.0 | 296,065.8 | 5 | 37,208 | 28,742 | 25,911 | 0.002 | compiled=5 | 2,264,918.0 | 192,074,490.0 | 44,864.0 |
| `co-member-twin` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 208,142,627.0 | 207,049,538.0 | 208,740,955.0 | 582,481.8 | 5 | 37,008 | 24,800 | 23,101 | 0.003 (max is trial 1) | compiled=5 | 1,613,200.0 | 206,477,789.0 | 50,055.0 |
| `co-member-twin` | `whole-subject` | `pcrec_614d45eb3_vm-caps-simdna` | 213,773,017.0 | 212,624,833.0 | 215,249,948.0 | 1,124,594.4 | 5 | 37,008 | 24,913 | 23,214 | 0.005 | compiled=5 | 1,573,235.0 | 212,146,601.0 | 53,181.0 |
| `co-member-twin` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 218,353,326.0 | 214,964,338.0 | 221,996,092.0 | 2,298,368.3 | 5 | 37,008 | 24,838 | 23,139 | 0.011 (max is trial 1) | compiled=5 | 1,651,402.0 | 216,661,809.0 | 40,115.0 |
| `co-member-twin` | `whole-subject` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 216,748,984.0 | 213,127,438.0 | 219,294,190.0 | 2,071,330.1 | 5 | 37,008 | 24,951 | 23,252 | 0.010 (max is trial 1) | compiled=5 | 1,778,872.0 | 214,845,116.0 | 53,340.0 |
| `co-netstr` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 300,465,111.0 | 298,549,814.0 | 300,967,688.0 | 922,192.6 | 5 | 51,336 | 26,047 | 24,525 | 0.003 | compiled=5 | 1,448,148.0 | 298,740,072.0 | 75,612.0 |
| `co-netstr` | `whole-subject` | `pcrec_614d45eb3_auto-caps-simdna` | 309,139,524.0 | 300,766,460.0 | 312,436,987.0 | 4,781,537.1 | 5 | 51,336 | 26,158 | 24,636 | 0.015 | compiled=5 | 1,640,741.0 | 307,423,311.0 | 72,136.0 |
| `co-netstr` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 310,095,292.0 | 307,721,349.0 | 323,305,328.0 | 5,771,173.2 | 5 | 51,336 | 26,085 | 24,563 | 0.019 | compiled=5 | 1,601,799.0 | 308,359,561.0 | 76,765.0 |
| `co-netstr` | `whole-subject` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 315,742,263.0 | 313,497,745.0 | 322,949,177.0 | 3,291,294.5 | 5 | 51,336 | 26,196 | 24,674 | 0.010 (max is trial 1) | compiled=5 | 1,630,422.0 | 314,038,433.0 | 73,348.0 |
| `co-netstr` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 311,162,062.0 | 298,187,423.0 | 314,139,643.0 | 5,783,954.6 | 5 | 51,336 | 26,045 | 24,523 | 0.019 | compiled=5 | 1,620,253.0 | 309,687,684.0 | 77,216.0 |
| `co-netstr` | `whole-subject` | `pcrec_614d45eb3_vm-caps-simdna` | 313,025,393.0 | 311,160,620.0 | 313,694,263.0 | 1,062,633.8 | 5 | 51,336 | 26,156 | 24,634 | 0.003 (max is trial 1) | compiled=5 | 1,463,598.0 | 311,321,162.0 | 74,200.0 |
| `co-netstr` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 300,511,293.0 | 297,982,909.0 | 301,712,477.0 | 1,264,849.9 | 5 | 51,336 | 26,083 | 24,561 | 0.004 | compiled=5 | 1,481,582.0 | 298,942,417.0 | 81,804.0 |
| `co-netstr` | `whole-subject` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 300,583,570.0 | 299,296,445.0 | 303,623,960.0 | 1,488,163.2 | 5 | 51,336 | 26,194 | 24,672 | 0.005 | compiled=5 | 1,520,164.0 | 299,007,820.0 | 79,530.0 |
| `co-netstr-assist` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 164,827,222.0 | 162,714,340.0 | 165,982,340.0 | 1,242,854.1 | 5 | 42,936 | 26,920 | 25,398 | 0.008 | compiled=5 | 1,652,183.0 | 163,122,210.0 | 70,413.0 |
| `co-netstr-assist` | `whole-subject` | `pcrec_614d45eb3_auto-caps-simdna` | 164,769,615.0 | 163,607,254.0 | 167,870,635.0 | 1,421,309.0 | 5 | 42,936 | 27,033 | 25,511 | 0.009 | compiled=5 | 1,572,092.0 | 163,298,903.0 | 68,650.0 |
| `co-netstr-assist` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 165,752,535.0 | 163,562,487.0 | 168,033,924.0 | 1,607,381.2 | 5 | 42,936 | 26,958 | 25,436 | 0.010 | compiled=5 | 1,624,180.0 | 164,260,413.0 | 70,583.0 |
| `co-netstr-assist` | `whole-subject` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 161,894,805.0 | 160,127,425.0 | 164,142,060.0 | 1,487,606.4 | 5 | 42,936 | 27,071 | 25,549 | 0.009 (max is trial 1) | compiled=5 | 1,573,706.0 | 160,390,510.0 | 74,250.0 |
| `co-netstr-assist` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 162,284,143.0 | 160,216,636.0 | 164,090,075.0 | 1,663,998.0 | 5 | 42,936 | 26,918 | 25,396 | 0.010 (max is trial 1) | compiled=5 | 1,549,239.0 | 160,844,780.0 | 71,585.0 |
| `co-netstr-assist` | `whole-subject` | `pcrec_614d45eb3_vm-caps-simdna` | 159,894,941.0 | 157,969,982.0 | 160,564,732.0 | 940,748.4 | 5 | 42,936 | 27,031 | 25,509 | 0.006 (max is trial 1) | compiled=5 | 1,497,221.0 | 158,186,511.0 | 74,861.0 |
| `co-netstr-assist` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 156,104,389.0 | 155,953,494.0 | 159,016,766.0 | 1,308,579.0 | 5 | 42,936 | 26,956 | 25,434 | 0.008 (max is trial 1) | compiled=5 | 1,483,877.0 | 154,647,333.0 | 77,987.0 |
| `co-netstr-assist` | `whole-subject` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 158,744,794.0 | 157,477,676.0 | 160,210,768.0 | 879,805.0 | 5 | 42,936 | 27,069 | 25,547 | 0.006 | compiled=5 | 1,452,958.0 | 157,166,370.0 | 75,342.0 |
| `co-netstr-twin` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 189,252,609.0 | 187,606,708.0 | 196,139,093.0 | 2,999,263.6 | 5 | 37,304 | 32,127 | 27,213 | 0.016 | compiled=5 | 2,778,364.0 | 186,374,637.0 | 44,454.0 |
| `co-netstr-twin` | `whole-subject` | `pcrec_614d45eb3_auto-caps-simdna` | 177,253,613.0 | 175,175,557.0 | 178,481,426.0 | 1,182,215.3 | 5 | 37,112 | 28,514 | 26,634 | 0.007 (max is trial 1) | compiled=5 | 1,759,395.0 | 175,416,943.0 | 48,752.0 |
| `co-netstr-twin` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 182,177,999.0 | 180,466,594.0 | 183,129,071.0 | 959,823.4 | 5 | 37,304 | 32,165 | 27,251 | 0.005 | compiled=5 | 2,426,002.0 | 179,684,831.0 | 48,131.0 |
| `co-netstr-twin` | `whole-subject` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 173,855,415.0 | 173,176,826.0 | 174,729,633.0 | 494,227.0 | 5 | 37,112 | 28,552 | 26,672 | 0.003 | compiled=5 | 1,789,914.0 | 172,065,582.0 | 54,122.0 |
| `co-netstr-twin` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 174,617,463.0 | 174,527,994.0 | 174,932,286.0 | 182,688.9 | 5 | 32,872 | 23,941 | 22,473 | 0.001 (max is trial 1) | compiled=5 | 1,426,257.0 | 173,166,869.0 | 49,633.0 |
| `co-netstr-twin` | `whole-subject` | `pcrec_614d45eb3_vm-caps-simdna` | 181,041,980.0 | 180,766,449.0 | 182,456,235.0 | 626,185.3 | 5 | 32,872 | 24,168 | 22,700 | 0.003 | compiled=5 | 1,467,105.0 | 179,523,267.0 | 49,303.0 |
| `co-netstr-twin` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 173,180,610.0 | 172,855,267.0 | 173,712,541.0 | 357,164.8 | 5 | 32,872 | 23,979 | 22,511 | 0.002 | compiled=5 | 1,356,797.0 | 171,679,841.0 | 50,676.0 |
| `co-netstr-twin` | `whole-subject` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 180,305,296.0 | 179,620,624.0 | 184,506,542.0 | 1,795,104.2 | 5 | 32,872 | 24,206 | 22,738 | 0.010 (max is trial 1) | compiled=5 | 1,405,068.0 | 178,772,807.0 | 54,242.0 |
| `cscan` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `cscan` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `cscan` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `cscan` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `cscan-onig` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 395,123,077.0 | 393,703,191.0 | 395,760,018.0 | 715,983.1 | 5 | 53,688 | 82,455 | 81,316 | 0.002 | compiled=5 | 3,478,434.0 | 391,632,270.0 | 49,894.0 |
| `cscan-onig` | `whole-subject` | `pcrec_614d45eb3_auto-caps-simdna` | 395,941,177.0 | 394,626,591.0 | 397,390,830.0 | 889,516.3 | 5 | 53,688 | 82,570 | 81,431 | 0.002 (max is trial 1) | compiled=5 | 3,356,754.0 | 392,643,936.0 | 57,629.0 |
| `cscan-onig` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 395,158,755.0 | 394,488,564.0 | 398,333,671.0 | 1,408,264.6 | 5 | 53,688 | 82,493 | 81,354 | 0.004 | compiled=5 | 3,215,740.0 | 392,026,754.0 | 53,901.0 |
| `cscan-onig` | `whole-subject` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 411,868,186.0 | 397,934,227.0 | 418,632,293.0 | 7,445,438.6 | 5 | 53,688 | 82,608 | 81,469 | 0.018 | compiled=5 | 3,251,858.0 | 408,574,659.0 | 53,230.0 |
| `cscan-onig` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 395,258,490.0 | 392,549,686.0 | 396,565,332.0 | 1,390,282.9 | 5 | 53,688 | 82,453 | 81,314 | 0.004 | compiled=5 | 3,194,049.0 | 392,086,042.0 | 51,577.0 |
| `cscan-onig` | `whole-subject` | `pcrec_614d45eb3_vm-caps-simdna` | 395,426,796.0 | 394,218,821.0 | 399,348,137.0 | 1,778,369.4 | 5 | 53,688 | 82,568 | 81,429 | 0.004 | compiled=5 | 3,431,586.0 | 391,919,418.0 | 53,020.0 |
| `cscan-onig` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 425,410,177.0 | 417,664,028.0 | 433,189,967.0 | 5,779,948.5 | 5 | 53,688 | 82,491 | 81,352 | 0.014 | compiled=5 | 3,317,181.0 | 421,924,788.0 | 49,082.0 |
| `cscan-onig` | `whole-subject` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 411,620,790.0 | 411,011,833.0 | 422,250,602.0 | 4,263,528.8 | 5 | 53,688 | 82,606 | 81,467 | 0.010 (max is trial 1) | compiled=5 | 3,278,238.0 | 407,974,267.0 | 51,027.0 |
| `floor` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 86,588,031.0 | 85,732,398.0 | 87,331,622.0 | 580,076.5 | 5 | 33,128 | 19,184 | 15,655 | 0.007 (max is trial 1) | compiled=5 | 4,214,640.0 | 82,419,246.0 | 53,170.0 |
| `floor` | `whole-subject` | `pcrec_614d45eb3_auto-caps-simdna` | 79,113,770.0 | 78,609,419.0 | 80,224,252.0 | 563,747.5 | 5 | 33,176 | 19,926 | 16,036 | 0.007 | compiled=5 | 2,019,285.0 | 77,066,492.0 | 50,546.0 |
| `floor` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 86,015,357.0 | 84,903,283.0 | 86,622,462.0 | 565,682.2 | 5 | 33,128 | 19,184 | 15,655 | 0.007 | compiled=5 | 4,293,251.0 | 81,616,108.0 | 46,468.0 |
| `floor` | `whole-subject` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 79,602,313.0 | 79,323,036.0 | 80,426,225.0 | 383,499.7 | 5 | 33,176 | 19,926 | 16,036 | 0.005 (max is trial 1) | compiled=5 | 2,008,315.0 | 77,768,517.0 | 52,980.0 |
| `floor` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 95,171,466.0 | 94,644,170.0 | 95,916,268.0 | 489,571.8 | 5 | 32,920 | 23,074 | 21,606 | 0.005 (max is trial 1) | compiled=5 | 1,644,659.0 | 93,268,829.0 | 51,918.0 |
| `floor` | `whole-subject` | `pcrec_614d45eb3_vm-caps-simdna` | 99,532,792.0 | 99,217,289.0 | 100,110,993.0 | 322,119.8 | 5 | 32,920 | 23,298 | 21,830 | 0.003 | compiled=5 | 2,344,628.0 | 97,356,412.0 | 51,727.0 |
| `floor` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 97,093,181.0 | 96,708,928.0 | 98,525,110.0 | 723,779.8 | 5 | 32,920 | 23,112 | 21,644 | 0.007 | compiled=5 | 1,655,009.0 | 95,503,447.0 | 51,396.0 |
| `floor` | `whole-subject` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 100,935,864.0 | 99,994,020.0 | 101,566,643.0 | 530,520.3 | 5 | 32,920 | 23,336 | 21,868 | 0.005 (max is trial 1) | compiled=5 | 1,653,556.0 | 99,204,411.0 | 54,442.0 |
| `va-route` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 123,085,362.0 | 121,529,600.0 | 123,375,317.0 | 743,960.6 | 5 | 33,104 | 27,192 | 27,101 | 0.006 (max is trial 1) | compiled=5 | 1,603,912.0 | 121,434,712.0 | 46,738.0 |
| `va-route` | `whole-subject` | `pcrec_614d45eb3_auto-caps-simdna` | 126,781,514.0 | 124,969,050.0 | 127,527,229.0 | 859,710.2 | 5 | 33,104 | 27,306 | 27,215 | 0.007 (max is trial 1) | compiled=5 | 1,713,879.0 | 125,016,269.0 | 52,549.0 |
| `va-route` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 123,093,032.0 | 122,700,563.0 | 123,344,176.0 | 226,008.2 | 5 | 33,104 | 27,230 | 27,139 | 0.002 | compiled=5 | 1,618,360.0 | 121,333,235.0 | 51,457.0 |
| `va-route` | `whole-subject` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 123,002,661.0 | 122,031,330.0 | 123,139,770.0 | 402,740.8 | 5 | 33,104 | 27,344 | 27,253 | 0.003 (max is trial 1) | compiled=5 | 1,597,661.0 | 121,122,077.0 | 49,824.0 |
| `va-route` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 126,822,711.0 | 124,682,347.0 | 127,603,522.0 | 983,852.2 | 5 | 33,104 | 27,190 | 27,099 | 0.008 | compiled=5 | 1,741,311.0 | 125,024,542.0 | 45,726.0 |
| `va-route` | `whole-subject` | `pcrec_614d45eb3_vm-caps-simdna` | 126,763,068.0 | 126,643,492.0 | 134,019,131.0 | 2,924,861.5 | 5 | 33,104 | 27,304 | 27,213 | 0.023 | compiled=5 | 1,741,371.0 | 125,123,849.0 | 47,941.0 |
| `va-route` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 122,637,230.0 | 121,888,619.0 | 123,051,982.0 | 415,998.5 | 5 | 33,104 | 27,228 | 27,137 | 0.003 | compiled=5 | 1,626,194.0 | 121,113,749.0 | 49,724.0 |
| `va-route` | `whole-subject` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 123,144,274.0 | 122,789,587.0 | 123,709,559.0 | 371,591.8 | 5 | 33,104 | 27,342 | 27,251 | 0.003 | compiled=5 | 1,562,514.0 | 121,537,637.0 | 54,964.0 |
| `va-tenant` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 153,326,815.0 | 152,966,387.0 | 153,829,763.0 | 277,007.1 | 5 | 32,920 | 25,436 | 25,367 | 0.002 | compiled=5 | 1,429,343.0 | 151,827,180.0 | 49,834.0 |
| `va-tenant` | `whole-subject` | `pcrec_614d45eb3_auto-caps-simdna` | 153,764,369.0 | 153,071,254.0 | 154,381,403.0 | 436,470.9 | 5 | 32,920 | 25,549 | 25,480 | 0.003 | compiled=5 | 1,341,688.0 | 152,402,384.0 | 53,511.0 |
| `va-tenant` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 150,459,245.0 | 150,262,603.0 | 154,530,126.0 | 1,626,821.9 | 5 | 32,920 | 25,474 | 25,405 | 0.011 (max is trial 1) | compiled=5 | 1,525,906.0 | 148,885,719.0 | 51,177.0 |
| `va-tenant` | `whole-subject` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 151,266,596.0 | 150,734,413.0 | 152,175,527.0 | 470,071.6 | 5 | 32,920 | 25,587 | 25,518 | 0.003 | compiled=5 | 1,466,955.0 | 149,783,200.0 | 42,851.0 |
| `va-tenant` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 153,083,925.0 | 151,954,669.0 | 154,683,570.0 | 889,865.7 | 5 | 32,920 | 25,434 | 25,365 | 0.006 (max is trial 1) | compiled=5 | 1,353,631.0 | 151,716,509.0 | 53,390.0 |
| `va-tenant` | `whole-subject` | `pcrec_614d45eb3_vm-caps-simdna` | 153,731,365.0 | 153,125,434.0 | 157,843,616.0 | 1,736,556.7 | 5 | 32,920 | 25,547 | 25,478 | 0.011 | compiled=5 | 1,386,283.0 | 152,241,378.0 | 50,154.0 |
| `va-tenant` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 150,668,796.0 | 150,329,355.0 | 151,369,475.0 | 354,888.5 | 5 | 32,920 | 25,472 | 25,403 | 0.002 (max is trial 1) | compiled=5 | 1,358,740.0 | 149,297,401.0 | 49,353.0 |
| `va-tenant` | `whole-subject` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 152,171,357.0 | 151,129,445.0 | 152,505,718.0 | 479,483.1 | 5 | 32,920 | 25,585 | 25,516 | 0.003 | compiled=5 | 1,365,744.0 | 150,804,391.0 | 49,332.0 |
| `va-term` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 173,088,958.0 | 172,387,487.0 | 174,898,746.0 | 842,549.1 | 5 | 37,056 | 23,854 | 23,556 | 0.005 | compiled=5 | 1,470,060.0 | 171,571,899.0 | 46,227.0 |
| `va-term` | `whole-subject` | `pcrec_614d45eb3_auto-caps-simdna` | 172,629,451.0 | 170,294,553.0 | 172,999,900.0 | 1,197,968.5 | 5 | 32,960 | 23,965 | 23,667 | 0.007 | compiled=5 | 1,430,505.0 | 171,122,703.0 | 54,874.0 |
| `va-term` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 166,112,745.0 | 165,478,338.0 | 167,155,559.0 | 600,071.1 | 5 | 32,960 | 23,892 | 23,594 | 0.004 (max is trial 1) | compiled=5 | 1,467,897.0 | 164,593,371.0 | 51,477.0 |
| `va-term` | `whole-subject` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 163,411,814.0 | 163,067,044.0 | 165,823,869.0 | 1,004,353.0 | 5 | 32,960 | 24,003 | 23,705 | 0.006 | compiled=5 | 1,337,641.0 | 162,044,918.0 | 51,527.0 |
| `va-term` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 173,883,961.0 | 172,064,923.0 | 174,733,030.0 | 897,175.1 | 5 | 37,056 | 23,852 | 23,554 | 0.005 (max is trial 1) | compiled=5 | 1,392,715.0 | 172,415,389.0 | 49,854.0 |
| `va-term` | `whole-subject` | `pcrec_614d45eb3_vm-caps-simdna` | 171,147,229.0 | 169,172,137.0 | 173,115,426.0 | 1,483,321.7 | 5 | 32,960 | 23,963 | 23,665 | 0.009 | compiled=5 | 1,494,947.0 | 169,606,656.0 | 46,177.0 |
| `va-term` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 166,990,403.0 | 166,024,252.0 | 168,118,439.0 | 682,314.9 | 5 | 32,960 | 23,890 | 23,592 | 0.004 | compiled=5 | 1,365,373.0 | 165,463,766.0 | 53,511.0 |
| `va-term` | `whole-subject` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 163,539,901.0 | 162,748,450.0 | 164,051,326.0 | 426,307.8 | 5 | 32,960 | 24,001 | 23,703 | 0.003 (max is trial 1) | compiled=5 | 1,328,113.0 | 162,015,859.0 | 52,409.0 |
| `va-term-bang` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 174,768,932.0 | 173,112,410.0 | 175,544,665.0 | 817,677.8 | 5 | 37,056 | 23,855 | 23,557 | 0.005 | compiled=5 | 1,483,425.0 | 173,239,020.0 | 54,783.0 |
| `va-term-bang` | `whole-subject` | `pcrec_614d45eb3_auto-caps-simdna` | 171,077,328.0 | 168,826,386.0 | 174,250,806.0 | 2,219,841.3 | 5 | 32,960 | 23,966 | 23,668 | 0.013 (max is trial 1) | compiled=5 | 1,457,326.0 | 169,570,228.0 | 51,036.0 |
| `va-term-bang` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 166,019,197.0 | 164,371,793.0 | 166,458,865.0 | 729,136.2 | 5 | 32,960 | 23,893 | 23,595 | 0.004 | compiled=5 | 1,383,687.0 | 164,458,266.0 | 50,455.0 |
| `va-term-bang` | `whole-subject` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 162,974,440.0 | 162,779,352.0 | 165,587,655.0 | 1,060,045.6 | 5 | 32,960 | 24,004 | 23,706 | 0.007 | compiled=5 | 1,385,321.0 | 161,597,544.0 | 52,148.0 |
| `va-term-bang` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 175,250,029.0 | 170,952,370.0 | 176,393,013.0 | 2,002,172.8 | 5 | 37,056 | 23,853 | 23,555 | 0.011 | compiled=5 | 1,468,206.0 | 173,961,120.0 | 51,437.0 |
| `va-term-bang` | `whole-subject` | `pcrec_614d45eb3_vm-caps-simdna` | 167,467,605.0 | 166,864,900.0 | 168,597,093.0 | 727,405.8 | 5 | 32,960 | 23,964 | 23,666 | 0.004 (max is trial 1) | compiled=5 | 1,494,055.0 | 165,926,320.0 | 52,128.0 |
| `va-term-bang` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 166,387,529.0 | 165,735,267.0 | 167,807,183.0 | 733,512.0 | 5 | 32,960 | 23,891 | 23,593 | 0.004 | compiled=5 | 1,357,098.0 | 164,477,979.0 | 50,204.0 |
| `va-term-bang` | `whole-subject` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 163,767,721.0 | 163,363,268.0 | 171,072,207.0 | 2,908,401.0 | 5 | 32,960 | 24,002 | 23,704 | 0.018 | compiled=5 | 1,429,313.0 | 162,309,482.0 | 49,954.0 |
| `wild-json-validate` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-json-validate` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-json-validate` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-json-validate` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-json-validate-onig` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 573,017,859.0 | 556,212,798.0 | 578,137,804.0 | 9,368,940.9 | 5 | 66,096 | 92,448 | 91,007 | 0.016 | compiled=5 | 2,889,875.0 | 570,121,632.0 | 50,535.0 |
| `wild-json-validate-onig` | `whole-subject` | `pcrec_614d45eb3_auto-caps-simdna` | 585,505,184.0 | 570,534,409.0 | 589,678,536.0 | 6,889,261.1 | 5 | 66,096 | 92,567 | 91,126 | 0.012 (max is trial 1) | compiled=5 | 3,092,245.0 | 582,380,216.0 | 52,279.0 |
| `wild-json-validate-onig` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 588,866,564.0 | 586,109,669.0 | 625,821,117.0 | 17,469,253.2 | 5 | 66,096 | 92,486 | 91,045 | 0.030 | compiled=5 | 3,136,691.0 | 585,787,702.0 | 45,636.0 |
| `wild-json-validate-onig` | `whole-subject` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 568,505,894.0 | 557,570,037.0 | 593,826,490.0 | 12,816,349.6 | 5 | 66,096 | 92,605 | 91,164 | 0.023 (max is trial 1) | compiled=5 | 3,021,223.0 | 565,201,136.0 | 50,456.0 |
| `wild-json-validate-onig` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 587,414,501.0 | 583,928,261.0 | 590,154,795.0 | 2,511,293.7 | 5 | 66,096 | 92,446 | 91,005 | 0.004 | compiled=5 | 2,832,427.0 | 584,527,922.0 | 52,289.0 |
| `wild-json-validate-onig` | `whole-subject` | `pcrec_614d45eb3_vm-caps-simdna` | 560,876,856.0 | 555,241,116.0 | 578,067,548.0 | 8,240,857.3 | 5 | 66,096 | 92,565 | 91,124 | 0.015 (max is trial 1) | compiled=5 | 2,900,205.0 | 558,012,038.0 | 51,587.0 |
| `wild-json-validate-onig` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 555,723,241.0 | 554,906,552.0 | 560,620,350.0 | 2,086,401.4 | 5 | 66,096 | 92,484 | 91,043 | 0.004 | compiled=5 | 2,947,966.0 | 552,853,202.0 | 52,650.0 |
| `wild-json-validate-onig` | `whole-subject` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 557,177,070.0 | 555,968,864.0 | 566,103,672.0 | 3,668,556.5 | 5 | 66,096 | 92,603 | 91,162 | 0.007 | compiled=5 | 2,947,224.0 | 554,178,930.0 | 56,155.0 |
| `wild-sexp-balanced` | `plain` | `pcrec_614d45eb3_auto-caps-simdna` | 137,821,945.0 | 137,091,499.0 | 139,483,485.0 | 798,965.9 | 5 | 37,296 | 32,111 | 30,358 | 0.006 (max is trial 1) | compiled=5 | 1,660,749.0 | 136,189,840.0 | 50,555.0 |
| `wild-sexp-balanced` | `whole-subject` | `pcrec_614d45eb3_auto-caps-simdna` | 138,044,765.0 | 136,545,840.0 | 138,825,475.0 | 764,081.0 | 5 | 37,296 | 32,226 | 30,473 | 0.006 (max is trial 1) | compiled=5 | 1,656,731.0 | 136,193,997.0 | 50,725.0 |
| `wild-sexp-balanced` | `plain` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 142,859,213.0 | 141,365,335.0 | 144,340,805.0 | 990,632.8 | 5 | 37,296 | 32,149 | 30,396 | 0.007 | compiled=5 | 1,831,282.0 | 140,972,837.0 | 52,859.0 |
| `wild-sexp-balanced` | `whole-subject` | `pcrec_614d45eb3_auto-in-caps-simdna_lim-ceil1g` | 143,284,875.0 | 142,581,637.0 | 143,782,813.0 | 464,815.4 | 5 | 37,296 | 32,264 | 30,511 | 0.003 | compiled=5 | 1,844,336.0 | 141,305,184.0 | 48,681.0 |
| `wild-sexp-balanced` | `plain` | `pcrec_614d45eb3_vm-caps-simdna` | 137,847,725.0 | 136,917,472.0 | 138,239,724.0 | 506,816.4 | 5 | 37,296 | 32,109 | 30,356 | 0.004 | compiled=5 | 1,657,183.0 | 136,170,564.0 | 52,379.0 |
| `wild-sexp-balanced` | `whole-subject` | `pcrec_614d45eb3_vm-caps-simdna` | 141,901,103.0 | 140,461,421.0 | 145,128,846.0 | 1,589,995.5 | 5 | 37,296 | 32,224 | 30,471 | 0.011 | compiled=5 | 1,775,806.0 | 140,170,442.0 | 52,669.0 |
| `wild-sexp-balanced` | `plain` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 138,988,585.0 | 137,582,706.0 | 141,541,415.0 | 1,377,636.9 | 5 | 37,296 | 32,147 | 30,394 | 0.010 (max is trial 1) | compiled=5 | 1,664,808.0 | 137,193,091.0 | 52,679.0 |
| `wild-sexp-balanced` | `whole-subject` | `pcrec_614d45eb3_vm-in-caps-simdna_lim-ceil1g` | 137,954,745.0 | 137,465,744.0 | 139,676,792.0 | 890,937.8 | 5 | 37,296 | 32,262 | 30,509 | 0.006 | compiled=5 | 1,548,078.0 | 136,214,856.0 | 50,786.0 |
    - emit/code bytes across abi 77: pcrec's size definition moves at the boundary -- a flat ~+106 B of counted stamp and initializer lines on a typical artifact (`RX_COMPOUND`, `RX_MEASURES`, `.measures`/`.next`/`.next_n`), and from abi 83 the find-all iterator scaffold (`_next`, the forwarder twins) is EXCLUDED from both counts with no marker in the emitted text. Read a Delta that spans the boundary against that, not as a program change; the DFA retry machine (`RX_ITER_RETRY=retry`) is NOT scaffold and counts (b142prep: +3-4 KB on narrow DFAs).

### `eager-jit`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `co-isbn` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 6,000.0 | 4,248.0 | 40,586.0 | 13,958.8 | 5 | 216 | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 8,146.0 | 5,922.0 | 49,543.0 | 16,808.7 | 5 | 216 | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-isbn` | `plain` | `re2_11.0.0_default-caps-simdna_assist-v01` | 5,771.0 | 3,987.0 | 31,169.0 | 10,346.6 | 5 | 45,216 | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-isbn` | `plain` | `rust_1.13.1_default-caps-simdna_assist-v01` | 36,659.0 | 32,591.0 | 243,709.0 | 82,803.6 | 5 | 8,188,760 | 2.259 (max is trial 1) | compiled=5 |
| `co-isbn` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-isbn` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | 831,958.0 | 822,299.0 | 1,327,682.0 | 198,314.6 | 5 | 44,520 | 0.238 (max is trial 1) | compiled=5 |
| `co-isbn-nofn` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 7,334.0 | 5,361.0 | 43,952.0 | 14,829.3 | 5 | 216 | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn-nofn` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 5,881.0 | 4,469.0 | 36,098.0 | 12,182.0 | 5 | 216 | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn-nofn` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-isbn-nofn` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-isbn-nofn` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-isbn-pass` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 6,893.0 | 5,310.0 | 45,986.0 | 15,687.6 | 5 | 216 | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn-pass` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 6,112.0 | 4,408.0 | 38,974.0 | 13,283.7 | 5 | 216 | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn-pass` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-isbn-pass` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-isbn-pass` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-isbn-twin` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 4,659.0 | 3,487.0 | 36,950.0 | 12,937.5 | 5 | 210 | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn-twin` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 4,709.0 | 3,557.0 | 35,116.0 | 12,185.4 | 5 | 210 | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn-twin` | `plain` | `re2_11.0.0_default-caps-simdna` | 4,418.0 | 3,266.0 | 42,300.0 | 15,079.2 | 5 | 21 | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn-twin` | `plain` | `re2_11.0.0_default-caps-simdna_assist-v01` | 4,419.0 | 3,166.0 | 23,714.0 | 7,783.8 | 5 | 21 | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn-twin` | `plain` | `rust_1.13.1_default-caps-simdna` | 250,021.0 | 149,672.0 | 539,657.0 | 141,890.8 | 5 | - | 0.568 (max is trial 1) | compiled=5 |
| `co-isbn-twin` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 269,267.0 | 156,705.0 | 627,021.0 | 172,935.5 | 5 | - | 0.642 (max is trial 1) | compiled=5 |
| `co-isbn-twin` | `plain` | `rust_1.13.1_default-caps-simdna_assist-v01` | 235,183.0 | 146,967.0 | 508,539.0 | 132,384.5 | 5 | - | 0.563 (max is trial 1) | compiled=5 |
| `co-isbn-twin` | `whole-subject` | `rust_1.13.1_default-caps-simdna_assist-v01` | 256,092.0 | 151,255.0 | 530,710.0 | 138,509.3 | 5 | - | 0.541 (max is trial 1) | compiled=5 |
| `co-isbn-twin` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-isbn-twin` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-luhn` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5,761.0 | 4,248.0 | 63,881.0 | 23,235.0 | 5 | 183 | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 5,770.0 | 4,248.0 | 66,977.0 | 24,485.1 | 5 | 183 | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-luhn` | `plain` | `re2_11.0.0_default-caps-simdna_assist-v01` | 6,161.0 | 4,509.0 | 26,159.0 | 8,111.7 | 5 | 45,216 | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-luhn` | `plain` | `rust_1.13.1_default-caps-simdna_assist-v01` | 82,104.0 | 78,448.0 | 338,989.0 | 101,932.1 | 5 | 8,188,760 | 1.241 (max is trial 1) | compiled=5 |
| `co-luhn` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-luhn` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | 721,640.0 | 705,520.0 | 1,340,055.0 | 247,115.1 | 5 | 44,520 | 0.342 (max is trial 1) | compiled=5 |
| `co-luhn-nofn` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5,711.0 | 4,298.0 | 51,317.0 | 18,213.2 | 5 | 183 | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn-nofn` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 4,659.0 | 3,467.0 | 35,447.0 | 12,326.3 | 5 | 183 | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn-nofn` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-luhn-nofn` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-luhn-nofn` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-luhn-pass` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5,721.0 | 4,218.0 | 49,624.0 | 17,565.3 | 5 | 183 | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn-pass` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 5,621.0 | 4,198.0 | 47,619.0 | 16,795.3 | 5 | 183 | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn-pass` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-luhn-pass` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-luhn-pass` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-luhn-twin` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 4,599.0 | 3,567.0 | 45,516.0 | 16,318.0 | 5 | 177 | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn-twin` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 4,628.0 | 3,547.0 | 40,336.0 | 14,254.4 | 5 | 177 | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn-twin` | `plain` | `re2_11.0.0_default-caps-simdna` | 5,881.0 | 4,258.0 | 43,512.0 | 15,103.0 | 5 | 33 | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn-twin` | `plain` | `re2_11.0.0_default-caps-simdna_assist-v01` | 6,182.0 | 4,388.0 | 33,774.0 | 11,170.7 | 5 | 33 | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn-twin` | `plain` | `rust_1.13.1_default-caps-simdna` | 510,923.0 | 303,432.0 | 826,707.0 | 171,942.2 | 5 | - | 0.337 (max is trial 1) | compiled=5 |
| `co-luhn-twin` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 481,838.0 | 293,473.0 | 713,174.0 | 137,765.2 | 5 | - | 0.286 (max is trial 1) | compiled=5 |
| `co-luhn-twin` | `plain` | `rust_1.13.1_default-caps-simdna_assist-v01` | 498,759.0 | 298,051.0 | 829,123.0 | 174,588.8 | 5 | - | 0.350 (max is trial 1) | compiled=5 |
| `co-luhn-twin` | `whole-subject` | `rust_1.13.1_default-caps-simdna_assist-v01` | 630,688.0 | 430,972.0 | 886,220.0 | 156,748.7 | 5 | - | 0.249 (max is trial 1) | compiled=5 |
| `co-luhn-twin` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-luhn-twin` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-member` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 7,263.0 | 4,919.0 | 45,115.0 | 15,325.6 | 5 | 186 | timer-floor (max is trial 1) | compiled=5 |
| `co-member` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 7,124.0 | 4,969.0 | 48,732.0 | 16,813.2 | 5 | 186 | timer-floor (max is trial 1) | compiled=5 |
| `co-member` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-member` | `plain` | `re2_11.0.0_default-caps-simdna_assist-v01` | 3,787.0 | 2,544.0 | 23,865.0 | 8,112.5 | 5 | 45,216 | timer-floor (max is trial 1) | compiled=5 |
| `co-member` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-member` | `plain` | `rust_1.13.1_default-caps-simdna_assist-v01` | 9,588.0 | 7,935.0 | 207,751.0 | 78,917.1 | 5 | 8,188,760 | timer-floor (max is trial 1) | compiled=5 |
| `co-member` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-member` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | 222,199.0 | 166,053.0 | 637,681.0 | 176,826.7 | 5 | 44,520 | 0.796 (max is trial 1) | compiled=5 |
| `co-member-nofn` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 7,053.0 | 5,099.0 | 45,485.0 | 15,498.2 | 5 | 186 | timer-floor (max is trial 1) | compiled=5 |
| `co-member-nofn` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 5,680.0 | 4,108.0 | 38,463.0 | 13,203.1 | 5 | 186 | timer-floor (max is trial 1) | compiled=5 |
| `co-member-nofn` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-member-nofn` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-member-nofn` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-member-pass` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 6,983.0 | 5,130.0 | 44,936.0 | 15,251.5 | 5 | 186 | timer-floor (max is trial 1) | compiled=5 |
| `co-member-pass` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 5,932.0 | 4,158.0 | 44,664.0 | 15,619.1 | 5 | 186 | timer-floor (max is trial 1) | compiled=5 |
| `co-member-pass` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-member-pass` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-member-pass` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-member-twin` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 8,948.0 | 7,543.0 | 47,500.0 | 15,456.7 | 5 | 180 | timer-floor (max is trial 1) | compiled=5 |
| `co-member-twin` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 4,718.0 | 3,567.0 | 42,098.0 | 14,943.8 | 5 | 180 | timer-floor (max is trial 1) | compiled=5 |
| `co-member-twin` | `plain` | `re2_11.0.0_default-caps-simdna` | 3,877.0 | 2,635.0 | 36,398.0 | 12,980.7 | 5 | 16 | timer-floor (max is trial 1) | compiled=5 |
| `co-member-twin` | `plain` | `re2_11.0.0_default-caps-simdna_assist-v01` | 4,458.0 | 2,415.0 | 23,224.0 | 7,815.6 | 5 | 16 | timer-floor (max is trial 1) | compiled=5 |
| `co-member-twin` | `plain` | `rust_1.13.1_default-caps-simdna` | 347,254.0 | 281,020.0 | 725,357.0 | 164,364.9 | 5 | - | 0.473 (max is trial 1) | compiled=5 |
| `co-member-twin` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 380,678.0 | 248,949.0 | 713,013.0 | 161,000.3 | 5 | - | 0.423 (max is trial 1) | compiled=5 |
| `co-member-twin` | `plain` | `rust_1.13.1_default-caps-simdna_assist-v01` | 320,955.0 | 280,729.0 | 712,382.0 | 162,406.9 | 5 | - | 0.506 (max is trial 1) | compiled=5 |
| `co-member-twin` | `whole-subject` | `rust_1.13.1_default-caps-simdna_assist-v01` | 358,566.0 | 208,152.0 | 683,698.0 | 158,865.0 | 5 | - | 0.443 (max is trial 1) | compiled=5 |
| `co-member-twin` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-member-twin` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-netstr` | `plain` | `libpcre2_10.46_jit-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-netstr` | `plain` | `libpcre2_10.46_jit-caps-simdna_assist-v01` | 1,062.0 | 682.0 | 20,178.0 | 7,670.1 | 5 | 39,664 | timer-floor (max is trial 1) | compiled=5 |
| `co-netstr` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-netstr` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-netstr` | `plain` | `re2_11.0.0_default-caps-simdna_assist-v01` | 20.0 | 10.0 | 50.0 | 13.6 | 5 | 40,408 | timer-floor (max is trial 1) | compiled=5 |
| `co-netstr` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-netstr` | `plain` | `rust_1.13.1_default-caps-simdna_assist-v01` | 27,151.0 | 25,358.0 | 208,112.0 | 71,683.5 | 5 | 8,179,600 | 2.640 (max is trial 1) | compiled=5 |
| `co-netstr` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-netstr` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | 701,011.0 | 680,212.0 | 1,239,155.0 | 218,943.7 | 5 | 39,456 | 0.312 (max is trial 1) | compiled=5 |
| `co-netstr-assist` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5,962.0 | 4,389.0 | 43,320.0 | 15,010.3 | 5 | 196 | timer-floor (max is trial 1) | compiled=5 |
| `co-netstr-assist` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 7,815.0 | 5,260.0 | 50,585.0 | 17,322.0 | 5 | 196 | timer-floor (max is trial 1) | compiled=5 |
| `co-netstr-assist` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-netstr-assist` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-netstr-assist` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-netstr-twin` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 4,098.0 | 2,826.0 | 35,096.0 | 12,472.1 | 5 | 174 | timer-floor (max is trial 1) | compiled=5 |
| `co-netstr-twin` | `plain` | `libpcre2_10.46_jit-caps-simdna_assist-v01` | 3,907.0 | 2,796.0 | 61,025.0 | 22,877.2 | 5 | 174 | timer-floor (max is trial 1) | compiled=5 |
| `co-netstr-twin` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 4,079.0 | 2,876.0 | 44,645.0 | 16,233.3 | 5 | 174 | timer-floor (max is trial 1) | compiled=5 |
| `co-netstr-twin` | `plain` | `re2_11.0.0_default-caps-simdna` | 5,050.0 | 3,427.0 | 37,751.0 | 13,255.2 | 5 | 24 | timer-floor (max is trial 1) | compiled=5 |
| `co-netstr-twin` | `plain` | `re2_11.0.0_default-caps-simdna_assist-v01` | 6,232.0 | 4,177.0 | 29,977.0 | 9,785.4 | 5 | 24 | timer-floor (max is trial 1) | compiled=5 |
| `co-netstr-twin` | `plain` | `rust_1.13.1_default-caps-simdna` | 236,646.0 | 134,794.0 | 587,457.0 | 163,548.6 | 5 | - | 0.691 (max is trial 1) | compiled=5 |
| `co-netstr-twin` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 262,746.0 | 141,356.0 | 590,803.0 | 163,636.9 | 5 | - | 0.623 (max is trial 1) | compiled=5 |
| `co-netstr-twin` | `plain` | `rust_1.13.1_default-caps-simdna_assist-v01` | 243,970.0 | 146,256.0 | 574,913.0 | 154,904.7 | 5 | - | 0.635 (max is trial 1) | compiled=5 |
| `co-netstr-twin` | `whole-subject` | `rust_1.13.1_default-caps-simdna_assist-v01` | 225,795.0 | 132,931.0 | 466,409.0 | 121,376.0 | 5 | - | 0.538 (max is trial 1) | compiled=5 |
| `co-netstr-twin` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-netstr-twin` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `cscan` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 40,737.0 | 32,822.0 | 142,067.0 | 41,284.6 | 5 | 900 | 1.013 (max is trial 1) | compiled=5 |
| `cscan` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 33,393.0 | 27,081.0 | 123,522.0 | 36,551.9 | 5 | 900 | 1.095 (max is trial 1) | compiled=5 |
| `cscan` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `cscan` | `plain` | `re2_11.0.0_default-caps-simdna_assist-v01` | 48,201.0 | 38,332.0 | 473,593.0 | 170,701.3 | 5 | 40,664 | 3.541 (max is trial 1) | compiled=5 |
| `cscan` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `cscan` | `plain` | `rust_1.13.1_default-caps-simdna_assist-v01` | 91,102.0 | 71,545.0 | 304,654.0 | 89,566.0 | 5 | 8,194,696 | 0.983 (max is trial 1) | compiled=5 |
| `cscan` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `cscan` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `cscan-onig` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 32,942.0 | 27,452.0 | 101,511.0 | 27,963.5 | 5 | 895 | 0.849 (max is trial 1) | compiled=5 |
| `cscan-onig` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 32,731.0 | 27,342.0 | 98,044.0 | 26,669.6 | 5 | 895 | 0.815 (max is trial 1) | compiled=5 |
| `cscan-onig` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `cscan-onig` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `cscan-onig` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `floor` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 6,071.0 | 4,048.0 | 39,945.0 | 13,894.3 | 5 | 165 | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `libpcre2_10.46_jit-caps-simdna_assist-v01` | 3,598.0 | 2,835.0 | 40,687.0 | 14,793.5 | 5 | 165 | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 3,085.0 | 2,354.0 | 30,649.0 | 11,018.8 | 5 | 165 | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `re2_11.0.0_default-caps-simdna` | 1,443.0 | 852.0 | 35,657.0 | 13,709.9 | 5 | 7 | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `re2_11.0.0_default-caps-simdna_assist-v01` | 1,423.0 | 942.0 | 21,611.0 | 8,102.5 | 5 | 7 | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `rust_1.13.1_default-caps-simdna` | 1,773.0 | 1,312.0 | 107,142.0 | 41,978.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 10,750.0 | 4,679.0 | 127,881.0 | 48,050.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `rust_1.13.1_default-caps-simdna_assist-v01` | 1,553.0 | 1,132.0 | 99,828.0 | 39,174.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `whole-subject` | `rust_1.13.1_default-caps-simdna_assist-v01` | 10,781.0 | 4,909.0 | 122,290.0 | 45,489.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | 14,528.0 | 12,033.0 | 135,104.0 | 48,256.9 | 5 | 936 | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `whole-subject` | `vectorscan_5.4.11_block-som-nocaps-simd` | 50,726.0 | 46,047.0 | 283,996.0 | 92,761.2 | 5 | 1,320 | 1.829 (max is trial 1) | compiled=5 |
| `floor` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | 14,768.0 | 12,203.0 | 137,489.0 | 49,070.7 | 5 | 936 | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `whole-subject` | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | 50,194.0 | 45,256.0 | 239,631.0 | 75,145.1 | 5 | 1,320 | 1.497 (max is trial 1) | compiled=5 |
| `va-route` | `plain` | `libpcre2_10.46_jit-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-route` | `plain` | `libpcre2_10.46_jit-caps-simdna_assist-v01` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-route` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-route` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-route` | `plain` | `re2_11.0.0_default-caps-simdna_assist-v01` | 20.0 | 20.0 | 80.0 | 24.0 | 5 | 46,240 | timer-floor (max is trial 1) | compiled=5 |
| `va-route` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-route` | `plain` | `rust_1.13.1_default-caps-simdna_assist-v01` | 20.0 | 20.0 | 80.0 | 24.0 | 5 | 8,191,728 | timer-floor (max is trial 1) | compiled=5 |
| `va-route` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-route` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-tenant` | `plain` | `libpcre2_10.46_jit-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-tenant` | `plain` | `libpcre2_10.46_jit-caps-simdna_assist-v01` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-tenant` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-tenant` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-tenant` | `plain` | `re2_11.0.0_default-caps-simdna_assist-v01` | 20.0 | 10.0 | 70.0 | 21.3 | 5 | 45,984 | timer-floor (max is trial 1) | compiled=5 |
| `va-tenant` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-tenant` | `plain` | `rust_1.13.1_default-caps-simdna_assist-v01` | 20.0 | 10.0 | 60.0 | 17.4 | 5 | 8,191,624 | timer-floor (max is trial 1) | compiled=5 |
| `va-tenant` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-tenant` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term` | `plain` | `libpcre2_10.46_jit-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term` | `plain` | `libpcre2_10.46_jit-caps-simdna_assist-v01` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term` | `plain` | `re2_11.0.0_default-caps-simdna_assist-v01` | 20.0 | 10.0 | 60.0 | 18.5 | 5 | 46,216 | timer-floor (max is trial 1) | compiled=5 |
| `va-term` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term` | `plain` | `rust_1.13.1_default-caps-simdna_assist-v01` | 20.0 | 10.0 | 70.0 | 21.4 | 5 | 8,191,624 | timer-floor (max is trial 1) | compiled=5 |
| `va-term` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term-bang` | `plain` | `libpcre2_10.46_jit-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term-bang` | `plain` | `libpcre2_10.46_jit-caps-simdna_assist-v01` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term-bang` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term-bang` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term-bang` | `plain` | `re2_11.0.0_default-caps-simdna_assist-v01` | 20.0 | 10.0 | 61.0 | 18.9 | 5 | 46,216 | timer-floor (max is trial 1) | compiled=5 |
| `va-term-bang` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term-bang` | `plain` | `rust_1.13.1_default-caps-simdna_assist-v01` | 20.0 | 10.0 | 60.0 | 17.4 | 5 | 8,191,616 | timer-floor (max is trial 1) | compiled=5 |
| `va-term-bang` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term-bang` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-json-validate` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 29,406.0 | 23,454.0 | 99,408.0 | 28,568.1 | 5 | 723 | 0.972 (max is trial 1) | compiled=5 |
| `wild-json-validate` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 28,924.0 | 23,184.0 | 90,981.0 | 25,460.3 | 5 | 723 | 0.880 (max is trial 1) | compiled=5 |
| `wild-json-validate` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-json-validate` | `plain` | `re2_11.0.0_default-caps-simdna_assist-v01` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-json-validate` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-json-validate` | `plain` | `rust_1.13.1_default-caps-simdna_assist-v01` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-json-validate` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-json-validate` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-json-validate-onig` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 28,424.0 | 22,963.0 | 95,791.0 | 27,416.6 | 5 | 724 | 0.965 (max is trial 1) | compiled=5 |
| `wild-json-validate-onig` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 28,554.0 | 22,793.0 | 89,118.0 | 24,820.5 | 5 | 724 | 0.869 (max is trial 1) | compiled=5 |
| `wild-json-validate-onig` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-json-validate-onig` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-json-validate-onig` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-sexp-balanced` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 7,826.0 | 6,081.0 | 48,120.0 | 16,166.0 | 5 | 220 | timer-floor (max is trial 1) | compiled=5 |
| `wild-sexp-balanced` | `plain` | `libpcre2_10.46_jit-caps-simdna_lim-ceil1g` | 9,738.0 | 7,664.0 | 65,964.0 | 22,531.7 | 5 | 220 | timer-floor (max is trial 1) | compiled=5 |
| `wild-sexp-balanced` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-sexp-balanced` | `plain` | `re2_11.0.0_default-caps-simdna_assist-v01` | 1,302.0 | 841.0 | 15,619.0 | 5,717.0 | 5 | 40,256 | timer-floor (max is trial 1) | compiled=5 |
| `wild-sexp-balanced` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-sexp-balanced` | `plain` | `rust_1.13.1_default-caps-simdna_assist-v01` | 3,256.0 | 1,292.0 | 132,600.0 | 51,681.0 | 5 | 8,179,072 | timer-floor (max is trial 1) | compiled=5 |
| `wild-sexp-balanced` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-sexp-balanced` | `plain` | `vectorscan_5.4.11_block-som-nocaps-simd_assist-v01` | 67,868.0 | 64,010.0 | 316,045.0 | 97,842.7 | 5 | 39,600 | 1.442 (max is trial 1) | compiled=5 |

### `interpretive`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `co-isbn` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 721.0 | 431.0 | 11,151.0 | 4,184.3 | 5 | 216 | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 711.0 | 471.0 | 12,714.0 | 4,804.2 | 5 | 216 | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 2,014.0 | 1,392.0 | 7,274.0 | 2,192.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,645.0 | 1,974.0 | 8,927.0 | 2,589.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 1,953.0 | 1,423.0 | 7,544.0 | 2,292.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 2,164.0 | 1,603.0 | 6,993.0 | 2,004.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-isbn-nofn` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 902.0 | 541.0 | 11,872.0 | 4,412.1 | 5 | 216 | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn-nofn` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 811.0 | 541.0 | 18,295.0 | 7,000.0 | 5 | 216 | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn-nofn` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-isbn-nofn` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-isbn-nofn` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-isbn-pass` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 701.0 | 431.0 | 11,732.0 | 4,420.9 | 5 | 216 | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn-pass` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 691.0 | 421.0 | 11,271.0 | 4,239.0 | 5 | 216 | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn-pass` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 2,495.0 | 1,904.0 | 7,745.0 | 2,317.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn-pass` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,685.0 | 2,104.0 | 8,516.0 | 2,518.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn-pass` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 1,914.0 | 1,453.0 | 6,773.0 | 2,088.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn-pass` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 2,194.0 | 1,673.0 | 7,284.0 | 2,159.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn-pass` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-isbn-twin` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 621.0 | 400.0 | 11,201.0 | 4,232.3 | 5 | 210 | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn-twin` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 691.0 | 401.0 | 11,121.0 | 4,190.6 | 5 | 210 | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn-twin` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 2,184.0 | 1,683.0 | 7,714.0 | 2,250.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn-twin` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,425.0 | 1,894.0 | 6,402.0 | 1,673.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn-twin` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 1,763.0 | 1,393.0 | 4,879.0 | 1,298.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn-twin` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 2,003.0 | 1,533.0 | 6,843.0 | 1,997.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-isbn-twin` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-luhn` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 731.0 | 471.0 | 21,250.0 | 8,206.2 | 5 | 183 | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 721.0 | 481.0 | 21,019.0 | 8,110.2 | 5 | 183 | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 1,854.0 | 1,403.0 | 13,886.0 | 4,829.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 1,943.0 | 1,503.0 | 7,745.0 | 2,363.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 1,793.0 | 1,383.0 | 13,356.0 | 4,637.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 2,074.0 | 1,443.0 | 7,264.0 | 2,170.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-luhn-nofn` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 621.0 | 380.0 | 10,139.0 | 3,810.8 | 5 | 183 | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn-nofn` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 741.0 | 481.0 | 11,933.0 | 4,468.3 | 5 | 183 | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn-nofn` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-luhn-nofn` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-luhn-nofn` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-luhn-pass` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 631.0 | 391.0 | 10,971.0 | 4,144.2 | 5 | 183 | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn-pass` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 641.0 | 391.0 | 10,690.0 | 4,027.8 | 5 | 183 | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn-pass` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 2,395.0 | 1,233.0 | 4,028.0 | 1,048.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn-pass` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,144.0 | 1,553.0 | 7,434.0 | 2,311.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn-pass` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 2,425.0 | 1,172.0 | 5,401.0 | 1,549.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn-pass` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 2,164.0 | 1,532.0 | 7,153.0 | 2,217.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn-pass` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-luhn-twin` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 561.0 | 380.0 | 11,963.0 | 4,557.1 | 5 | 177 | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn-twin` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 591.0 | 361.0 | 10,370.0 | 3,921.3 | 5 | 177 | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn-twin` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 1,383.0 | 1,093.0 | 5,601.0 | 1,695.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn-twin` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 1,643.0 | 1,213.0 | 4,077.0 | 1,064.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn-twin` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 1,413.0 | 1,122.0 | 5,941.0 | 1,821.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn-twin` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 1,663.0 | 1,212.0 | 5,811.0 | 1,721.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-luhn-twin` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-member` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 691.0 | 360.0 | 9,268.0 | 3,464.9 | 5 | 186 | timer-floor (max is trial 1) | compiled=5 |
| `co-member` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 701.0 | 370.0 | 9,027.0 | 3,360.7 | 5 | 186 | timer-floor (max is trial 1) | compiled=5 |
| `co-member` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 1,904.0 | 1,383.0 | 6,833.0 | 2,015.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-member` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,064.0 | 1,543.0 | 7,404.0 | 2,181.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-member` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 1,493.0 | 1,172.0 | 4,348.0 | 1,187.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-member` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 2,414.0 | 1,442.0 | 6,042.0 | 1,610.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-member` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-member-nofn` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 722.0 | 370.0 | 9,498.0 | 3,550.0 | 5 | 186 | timer-floor (max is trial 1) | compiled=5 |
| `co-member-nofn` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 691.0 | 351.0 | 9,358.0 | 3,501.1 | 5 | 186 | timer-floor (max is trial 1) | compiled=5 |
| `co-member-nofn` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-member-nofn` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-member-nofn` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-member-pass` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 701.0 | 381.0 | 9,789.0 | 3,663.8 | 5 | 186 | timer-floor (max is trial 1) | compiled=5 |
| `co-member-pass` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 701.0 | 350.0 | 9,168.0 | 3,419.6 | 5 | 186 | timer-floor (max is trial 1) | compiled=5 |
| `co-member-pass` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 3,015.0 | 1,353.0 | 12,523.0 | 4,173.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-member-pass` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 1,784.0 | 1,163.0 | 5,731.0 | 1,803.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-member-pass` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 2,465.0 | 1,142.0 | 5,581.0 | 1,602.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-member-pass` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 1,783.0 | 1,203.0 | 4,589.0 | 1,432.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-member-pass` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-member-twin` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 571.0 | 351.0 | 9,358.0 | 3,527.7 | 5 | 180 | timer-floor (max is trial 1) | compiled=5 |
| `co-member-twin` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 601.0 | 351.0 | 9,467.0 | 3,562.7 | 5 | 180 | timer-floor (max is trial 1) | compiled=5 |
| `co-member-twin` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 1,713.0 | 1,222.0 | 6,162.0 | 1,845.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-member-twin` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 1,823.0 | 1,272.0 | 6,633.0 | 2,009.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-member-twin` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 1,462.0 | 1,002.0 | 4,819.0 | 1,418.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-member-twin` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 1,523.0 | 1,062.0 | 5,450.0 | 1,641.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-member-twin` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-netstr` | `plain` | `libpcre2_10.46_interp-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-netstr` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-netstr` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-netstr` | `plain` | `oniguruma_6.9.10_default-caps-simdna_assist-v01` | 3,497.0 | 1,904.0 | 25,328.0 | 8,880.4 | 5 | 39,840 | timer-floor (max is trial 1) | compiled=5 |
| `co-netstr` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-netstr` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-netstr-assist` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 932.0 | 571.0 | 14,207.0 | 5,321.6 | 5 | 196 | timer-floor (max is trial 1) | compiled=5 |
| `co-netstr-assist` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 952.0 | 571.0 | 13,656.0 | 5,104.2 | 5 | 196 | timer-floor (max is trial 1) | compiled=5 |
| `co-netstr-assist` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 1,963.0 | 1,452.0 | 7,634.0 | 2,315.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-netstr-assist` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,906.0 | 2,164.0 | 7,264.0 | 1,900.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-netstr-assist` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 2,124.0 | 1,533.0 | 5,831.0 | 1,585.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-netstr-assist` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 2,475.0 | 1,754.0 | 6,041.0 | 1,592.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-netstr-assist` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `co-netstr-twin` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 642.0 | 401.0 | 10,009.0 | 3,769.0 | 5 | 174 | timer-floor (max is trial 1) | compiled=5 |
| `co-netstr-twin` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 591.0 | 381.0 | 9,708.0 | 3,658.1 | 5 | 174 | timer-floor (max is trial 1) | compiled=5 |
| `co-netstr-twin` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 1,623.0 | 1,152.0 | 5,891.0 | 1,776.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-netstr-twin` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 1,664.0 | 1,243.0 | 6,382.0 | 1,936.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-netstr-twin` | `plain` | `oniguruma_6.9.10_default-caps-simdna_assist-v01` | 1,623.0 | 1,152.0 | 12,223.0 | 4,293.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-netstr-twin` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna_assist-v01` | 1,343.0 | 1,052.0 | 5,921.0 | 1,852.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-netstr-twin` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 1,393.0 | 912.0 | 4,970.0 | 1,509.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-netstr-twin` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 1,392.0 | 992.0 | 3,888.0 | 1,075.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `co-netstr-twin` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `cscan` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 7,875.0 | 6,653.0 | 38,101.0 | 12,076.2 | 5 | 900 | timer-floor (max is trial 1) | compiled=5 |
| `cscan` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 6,422.0 | 5,480.0 | 34,495.0 | 11,190.9 | 5 | 900 | timer-floor (max is trial 1) | compiled=5 |
| `cscan` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 56,927.0 | 43,743.0 | 90,320.0 | 16,842.7 | 5 | - | 0.296 (max is trial 1) | compiled=5 |
| `cscan` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 46,858.0 | 44,534.0 | 83,968.0 | 14,930.3 | 5 | - | 0.319 (max is trial 1) | compiled=5 |
| `cscan` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 38,182.0 | 34,495.0 | 74,130.0 | 14,583.3 | 5 | - | 0.382 (max is trial 1) | compiled=5 |
| `cscan` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 44,875.0 | 38,873.0 | 68,199.0 | 10,195.4 | 5 | - | 0.227 (max is trial 1) | compiled=5 |
| `cscan` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `cscan-onig` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 6,342.0 | 5,440.0 | 35,667.0 | 11,697.6 | 5 | 895 | timer-floor (max is trial 1) | compiled=5 |
| `cscan-onig` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 6,783.0 | 5,751.0 | 29,456.0 | 9,103.7 | 5 | 895 | timer-floor (max is trial 1) | compiled=5 |
| `cscan-onig` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 34,936.0 | 33,403.0 | 63,850.0 | 11,447.0 | 5 | - | 0.328 (max is trial 1) | compiled=5 |
| `cscan-onig` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 44,183.0 | 41,669.0 | 81,433.0 | 14,827.0 | 5 | - | 0.336 (max is trial 1) | compiled=5 |
| `cscan-onig` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 44,173.0 | 41,929.0 | 80,111.0 | 14,285.8 | 5 | - | 0.323 (max is trial 1) | compiled=5 |
| `cscan-onig` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 46,438.0 | 45,155.0 | 79,420.0 | 12,994.1 | 5 | - | 0.280 (max is trial 1) | compiled=5 |
| `cscan-onig` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `floor` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 281.0 | 170.0 | 9,197.0 | 3,573.7 | 5 | 165 | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 280.0 | 181.0 | 9,327.0 | 3,622.8 | 5 | 165 | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 370.0 | 331.0 | 3,216.0 | 1,127.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 591.0 | 411.0 | 4,028.0 | 1,380.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `oniguruma_6.9.10_default-caps-simdna_assist-v01` | 410.0 | 300.0 | 1,763.0 | 548.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna_assist-v01` | 581.0 | 410.0 | 3,837.0 | 1,306.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 321.0 | 281.0 | 3,286.0 | 1,181.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 621.0 | 421.0 | 2,214.0 | 666.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `tre_0.9.0_default-caps-simdna` | 1,382.0 | 892.0 | 7,664.0 | 2,557.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 1,563.0 | 1,133.0 | 7,243.0 | 2,312.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `va-route` | `plain` | `libpcre2_10.46_interp-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-route` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-route` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-route` | `plain` | `oniguruma_6.9.10_default-caps-simdna_assist-v01` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-route` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-route` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-tenant` | `plain` | `libpcre2_10.46_interp-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-tenant` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-tenant` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-tenant` | `plain` | `oniguruma_6.9.10_default-caps-simdna_assist-v01` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-tenant` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-tenant` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term` | `plain` | `libpcre2_10.46_interp-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term` | `plain` | `oniguruma_6.9.10_default-caps-simdna_assist-v01` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term-bang` | `plain` | `libpcre2_10.46_interp-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term-bang` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term-bang` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term-bang` | `plain` | `oniguruma_6.9.10_default-caps-simdna_assist-v01` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term-bang` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `va-term-bang` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-json-validate` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 7,915.0 | 5,901.0 | 29,576.0 | 8,850.9 | 5 | 723 | timer-floor (max is trial 1) | compiled=5 |
| `wild-json-validate` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 6,422.0 | 4,689.0 | 25,128.0 | 7,630.3 | 5 | 723 | timer-floor (max is trial 1) | compiled=5 |
| `wild-json-validate` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 36,328.0 | 30,668.0 | 68,509.0 | 13,932.1 | 5 | - | 0.384 (max is trial 1) | compiled=5 |
| `wild-json-validate` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 31,710.0 | 26,260.0 | 55,946.0 | 10,700.5 | 5 | - | 0.337 (max is trial 1) | compiled=5 |
| `wild-json-validate` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 29,485.0 | 25,608.0 | 60,594.0 | 13,023.7 | 5 | - | 0.442 (max is trial 1) | compiled=5 |
| `wild-json-validate` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 36,970.0 | 31,900.0 | 68,209.0 | 13,495.9 | 5 | - | 0.365 (max is trial 1) | compiled=5 |
| `wild-json-validate` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-json-validate-onig` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 6,542.0 | 4,969.0 | 29,476.0 | 9,291.5 | 5 | 724 | timer-floor (max is trial 1) | compiled=5 |
| `wild-json-validate-onig` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 8,065.0 | 6,072.0 | 34,986.0 | 10,933.8 | 5 | 724 | timer-floor (max is trial 1) | compiled=5 |
| `wild-json-validate-onig` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 27,061.0 | 22,593.0 | 49,964.0 | 10,067.7 | 5 | - | 0.372 (max is trial 1) | compiled=5 |
| `wild-json-validate-onig` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 34,615.0 | 28,754.0 | 64,832.0 | 13,589.9 | 5 | - | 0.393 (max is trial 1) | compiled=5 |
| `wild-json-validate-onig` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 27,873.0 | 23,414.0 | 55,505.0 | 11,969.8 | 5 | - | 0.429 (max is trial 1) | compiled=5 |
| `wild-json-validate-onig` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 28,684.0 | 23,244.0 | 53,341.0 | 11,015.8 | 5 | - | 0.384 (max is trial 1) | compiled=5 |
| `wild-json-validate-onig` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-sexp-balanced` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,002.0 | 561.0 | 13,165.0 | 4,903.2 | 5 | 220 | timer-floor (max is trial 1) | compiled=5 |
| `wild-sexp-balanced` | `plain` | `libpcre2_10.46_interp-caps-simdna_lim-ceil1g` | 982.0 | 521.0 | 12,284.0 | 4,558.4 | 5 | 220 | timer-floor (max is trial 1) | compiled=5 |
| `wild-sexp-balanced` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 4,218.0 | 1,654.0 | 9,448.0 | 2,793.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-sexp-balanced` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,455.0 | 1,613.0 | 10,881.0 | 3,491.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-sexp-balanced` | `plain` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 4,318.0 | 1,793.0 | 7,985.0 | 2,206.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-sexp-balanced` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna_lim-ceil1g` | 3,015.0 | 1,843.0 | 12,263.0 | 3,936.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-sexp-balanced` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |

