//! [B133] THE TIMED LOOP, ISOLATED. Every instruction between the two clock
//! reads of a subject (search / find-all, the [B129] --prime pass,
//! `group_spans`, the find-all advance) is `run_subject` below and nowhere
//! else. See testees/pcrec/timed.c's header for the why ([B132]: stamp
//! getters added to a driver's main() moved the timed loop it contained by
//! +10-17% on short calls). Rust's version of the fix: this is a CRATE of its
//! own (own codegen units, own object), `#[inline(never)]`, so no edit to the
//! driver crate's main.rs can change the code generated for it. What Rust
//! cannot pin on stable: per-function alignment (`#![feature(fn_align)]` is
//! nightly) -- see the `global_asm!` section-alignment note below and
//! testees/rust/CLAUDE.md for what was and was not achievable. It is an
//! INSTRUMENT -- an edit here must be recorded as an instrument change
//! (docs/dev/decisions.md BD-B133). The body is the pre-[B133] loop moved
//! verbatim.

use regex::bytes::Regex;
use std::time::Instant;

fn now() -> Instant {
    Instant::now()
}

/// One subject's worth of work: `iters` repeats of the SAME operation
/// (find, or find-all in `--find-all` mode), only the FINAL iteration's
/// answer is reported -- the same convention every other driver in this
/// project holds to (the timed loop is deliberately homogeneous; what
/// varies is only how long it took).
pub struct SubjectResult {
    pub matched: bool,
    pub start: i64,
    pub end: i64,
    pub nmatches: i64, // -1 == "-" (not --find-all)
    pub caps: Vec<(i64, i64)>, // 1-based groups 1..n, empty when ncaps == 0
    pub elapsed: f64,
}

/// [B77] U1: the find-all EMPTY-MATCH advance under `--utf8` -- pcrec
/// match_api.md S3.1.1's NORMATIVE utf8 rule, the same one
/// pcrecbench/oracle_pcre2.py's `next_start()` and every other driver apply:
/// from pos + 1, skip every byte in 0x80-0xBF, stop at the first byte
/// outside that range or at n. Without `--utf8` the advance stays start + 1.
fn utf8_next_start(buf: &[u8], pos: usize) -> usize {
    let mut p = pos + 1;
    while p < buf.len() && (buf[p] & 0xC0) == 0x80 {
        p += 1;
    }
    p
}

// Alignment, as far as stable Rust allows: `#[repr(align)]` does not apply
// to functions and `#![feature(fn_align)]` is nightly. The function is given
// a section of its own (`.text.rust_timed_run`) and a module-level
// `global_asm!` declares the SAME section with `.balign 64`; the assembler
// merges the two, so the section -- and, being its only (first) contents,
// the function at offset 0 -- starts on a 64-byte boundary in the final
// link. Verified by objdump/nm in docs/dev/measurements/
// 2026-10-09-b133-isolation-proof.txt, not assumed.
core::arch::global_asm!(".section .text.rust_timed_run,\"ax\",@progbits", ".balign 64");

#[inline(never)]
#[link_section = ".text.rust_timed_run"]
pub fn run_subject(re: &Regex, buf: &[u8], iters: i64, find_all: bool, utf8_adv: bool, prime: bool) -> SubjectResult {
    let ncap = re.captures_len().saturating_sub(1); // group 0 excluded, RE2/onig convention
    let mut matched = false;
    let mut start: i64 = -1;
    let mut end: i64 = -1;
    let mut nmatches: i64 = -1;
    let mut caps: Vec<(i64, i64)> = Vec::new();

    let mut t0 = now();
    // [B129] --prime: pass 0 (only with the flag) is ONE untimed call of the
    // same body, then the clock restarts; the timed loop is the original one.
    for pass in (if prime { 0 } else { 1 })..2 {
        let n_it = if pass == 0 { 1 } else { iters.max(1) };
        if pass == 1 && prime {
            t0 = now();
        }
    for _ in 0..n_it {
        start = -1;
        end = -1;
        caps.clear();
        if find_all {
            let mut pos = 0usize;
            let mut count: i64 = 0;
            loop {
                if pos > buf.len() {
                    break;
                }
                let m = match re.find_at(buf, pos) {
                    Some(m) => m,
                    None => break,
                };
                let (ms, me) = (m.start(), m.end());
                if start < 0 {
                    start = ms as i64;
                    end = me as i64;
                    if let Some(c) = re.captures_at(buf, ms) {
                        caps = group_spans(&c, ncap);
                    }
                }
                count += 1;
                // pcrec match_api.md S3.1's find-all advance rule (adopted
                // by reference, KB-17, testees/pcre2/driver.c's own
                // comment): off the match's own reported START, never off
                // the scan position.
                // Under --utf8 ([B77] U1): the next CHARACTER boundary.
                pos = if me > ms {
                    me
                } else if utf8_adv {
                    utf8_next_start(buf, ms)
                } else {
                    ms + 1
                };
            }
            nmatches = count;
            matched = count > 0;
        } else {
            match re.find(buf) {
                Some(m) => {
                    matched = true;
                    start = m.start() as i64;
                    end = m.end() as i64;
                    if let Some(c) = re.captures(buf) {
                        caps = group_spans(&c, ncap);
                    }
                }
                None => {
                    matched = false;
                }
            }
        }
    }
    }
    let elapsed = t0.elapsed().as_secs_f64();

    SubjectResult { matched, start, end, nmatches, caps, elapsed }
}

fn group_spans(c: &regex::bytes::Captures, ncap: usize) -> Vec<(i64, i64)> {
    let mut out = Vec::with_capacity(ncap);
    for g in 1..=ncap {
        match c.get(g) {
            Some(m) => out.push((m.start() as i64, m.end() as i64)),
            None => out.push((-1, -1)),
        }
    }
    out
}

