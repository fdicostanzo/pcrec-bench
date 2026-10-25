//! [B140] THE SUBSTITUTION TIMED CALL, ISOLATED. Every instruction between the
//! two clock reads of a `--mode subst` subject is `timed_subst` below and
//! nowhere else. Same discipline as ../timed/src/lib.rs (BD16,
//! docs/dev/decisions.md): a crate of its own, `#[inline(never)]`, its own
//! section aligned to 64.
//!
//! WHY A THIRD CRATE AND NOT A SECOND FUNCTION IN `rust-timed`. `rust-timed`
//! is the INSTRUMENT every rust-regex matching cell in the store was measured
//! with; BD16 (2) makes any edit to it an instrument change needing a
//! re-pin-control timing run, and this lane may not run timing. A new mode
//! needs a new timed function, not a changed old one (the pcre2 driver's
//! `timed_subst.c` is the same decision). `rust_timed::run_subject` is
//! byte-identical in the old and new driver: the proof is
//! docs/dev/measurements/2026-10-25-b140drv2-instrument-additivity.txt.
//!
//! WHAT IS TIMED (docs/design/subst_bench_v1.md 3.1): ONE
//! `regex::bytes::Regex::replace_all(&[u8], &[u8])` call. The returned
//! `Cow<[u8]>` allocates INSIDE the clock -- intrinsic to the API, a reading
//! note and not engineered away (a hand loop over `captures_iter` into a
//! reserved Vec would be a different, non-idiomatic competitor). The result
//! is handed back UNTOUCHED (still a `Cow`): turning it into an owned Vec, the
//! substitution count and the output file are all the driver's, after the
//! clock stopped. iters is 1 in this bench; the driver refuses anything else,
//! so there is no loop here to put a drop of the previous result inside the
//! clock.

use regex::bytes::Regex;
use std::borrow::Cow;
use std::time::Instant;

// Alignment as far as stable Rust allows: see ../timed/src/lib.rs for the
// derivation (a section of its own + a module-level `.balign 64`). Its own
// section name, so the two crates' sections cannot merge.
core::arch::global_asm!(".section .text.rust_timed_subst,\"ax\",@progbits", ".balign 64");

#[inline(never)]
#[link_section = ".text.rust_timed_subst"]
pub fn timed_subst<'h>(re: &Regex, buf: &'h [u8], repl: &[u8]) -> (f64, Cow<'h, [u8]>) {
    let t0 = Instant::now();
    let out = re.replace_all(buf, repl);
    let elapsed = t0.elapsed().as_secs_f64();
    (elapsed, out)
}
