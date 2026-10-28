//! [B148] L4 THE CALL-STREAM TIMED REPLAY, ISOLATED (docs/design/
//! unusual_set_v1.md 7.1-7.2). A new mode is a new instrument: this crate
//! holds ONLY the replay loop; `rust-timed` (../timed/), the matching
//! instrument, is not edited (BD16). `#[inline(never)]`, its own section
//! aligned to 64, the same discipline as ../timed/src/lib.rs.
//!
//! One ITERATION is one full REPLAY of the declared call list, clocked
//! separately and SUMMED (P6). Each call is ONE `captures_read_at` (a pattern
//! with a group 1) or ONE `find_at` (none) over the WHOLE subject at the
//! call's offset -- the haystack before the offset is context, as on every
//! other engine. Only group 0 and group 1 are read (E-2b). The answer goes
//! into the preallocated `res` (integers only); the driver spells the tokens
//! after the clock. `regex` never gives up (no counter limits), so a call is
//! a match or a no-match.

use regex::bytes::{CaptureLocations, Regex};
use std::time::Instant;

/// One call's result; `kind` 0 = no match, 1 = match (calls_io.h's CALL_N /
/// CALL_M).
#[derive(Clone, Copy, Default)]
pub struct CallRes {
    pub kind: u8,
    pub s: i64,
    pub e: i64,
    pub g1s: i64,
    pub g1e: i64,
}

core::arch::global_asm!(".section .text.rust_timed_calls,\"ax\",@progbits", ".balign 64");

#[inline(never)]
#[link_section = ".text.rust_timed_calls"]
pub fn timed_calls(re: &Regex, locs: &mut CaptureLocations, buf: &[u8],
                   offsets: &[usize], iters: i64, has_g1: bool,
                   res: &mut [CallRes]) -> f64 {
    let mut total = 0.0f64;
    for _ in 0..iters {
        let t0 = Instant::now();
        for (i, &off) in offsets.iter().enumerate() {
            let r = &mut res[i];
            if has_g1 {
                match re.captures_read_at(locs, buf, off) {
                    Some(m) => {
                        r.kind = 1;
                        r.s = m.start() as i64;
                        r.e = m.end() as i64;
                        match locs.get(1) {
                            Some((a, b)) => { r.g1s = a as i64; r.g1e = b as i64; }
                            None => { r.g1s = -1; r.g1e = -1; }
                        }
                    }
                    None => r.kind = 0,
                }
            } else {
                match re.find_at(buf, off) {
                    Some(m) => {
                        r.kind = 1;
                        r.s = m.start() as i64;
                        r.e = m.end() as i64;
                    }
                    None => r.kind = 0,
                }
            }
        }
        total += t0.elapsed().as_secs_f64();
    }
    total
}
