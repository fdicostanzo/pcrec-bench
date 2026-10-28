/* ASSIST TEMPLATE -- rust-regex (Rust). Families: recursion, callouts, netstr, vars.
 *
 * Start with `python3 -m pcrecbench assist-init --member M --engine rust`:
 * it writes assists/M/rust/assist.rs holding only M's family. Fill the
 * function(s) marked ASSIST, your State and your setup; leave every
 * BOILERPLATE fence exactly as it is (the self-test compares them with this
 * template). Read bench/unusual/assists/AUTHORS.md and your problem
 * statement first.
 *
 * Built as a `staticlib` crate (edition 2021, the regex crate pinned by
 * testees/assist/rust/Cargo.lock, byte matching via regex::bytes) and linked
 * with the assist runner (testees/assist/), which owns main's work, the
 * protocol, the clock and the answer tokens. Return UB_M (fill m), UB_N,
 * UB_R (vars: the call is refused) or, on an engine give-up, a NEGATIVE
 * code. */

/* BOILERPLATE shim */
#![allow(dead_code, unused_imports, unused_variables, static_mut_refs)]
/* END BOILERPLATE */

/* BOILERPLATE includes */
use regex::bytes::Regex;
use std::collections::HashMap;
/* END BOILERPLATE */

/* BOILERPLATE shim */
#[repr(C)]
pub struct Span { pub s: i64, pub e: i64, pub g1s: i64, pub g1e: i64 }
const UB_N: i32 = 0;
const UB_M: i32 = 1;
const UB_R: i32 = 2;
extern "C" {
    fn ub_main(argc: i32, argv: *const *const u8) -> i32;
    fn ub_fail(msg: *const u8);
}
fn fail(e: String) -> i32 {
    let c = std::ffi::CString::new(e).unwrap_or_default();
    unsafe { ub_fail(c.as_ptr() as *const u8) };
    1
}
/* END BOILERPLATE */

/* BOILERPLATE shim */
struct State {
/* END BOILERPLATE */
    re: Regex,

/* BOILERPLATE shim */
}
fn setup(pattern: &[u8]) -> Result<State, String> {
/* END BOILERPLATE */
    Regex::new(r"[()]").map(|re| State { re }).map_err(|e| e.to_string())
/* BOILERPLATE shim */
}
/* END BOILERPLATE */

/* ASSIST: the first match at or after `start` (cscan: exactly at `start`) in
 * the whole subject `s` (bytes before `start` stay visible). Fill m.s, m.e
 * and, for cscan, the body in m.g1s, m.g1e. */
/* BOILERPLATE shim */
fn find(st: &mut State, s: &[u8], start: usize, m: &mut Span) -> i32 {
/* END BOILERPLATE */
    let (mut open, mut best) = (Vec::new(), None);
    for p in st.re.find_iter(&s[start..]) {
        let i = start + p.start();
        if s[i] == b'(' {
            open.push(i);
            continue;
        }
        let Some(o) = open.pop() else { continue };
        if open.is_empty() {
            best = Some((o, i + 1));
            break;
        }
        if best.map_or(true, |b: (usize, usize)| o < b.0) {
            best = Some((o, i + 1));
        }
    }
    best.map_or(UB_N, |(s, e)| {
        (m.s, m.e) = (s as i64, e as i64);
        UB_M
    })
/* BOILERPLATE shim */
}
static mut STATE: Option<State> = None;
#[no_mangle]
pub extern "C" fn ub_setup(p: *const u8, n: usize, _member: *const u8) -> i32 {
    let r = setup(unsafe { std::slice::from_raw_parts(p, n) });
    r.map(|st| unsafe { STATE = Some(st) }).map_or_else(fail, |_| 0)
}
#[no_mangle]
pub extern "C" fn ub_find(s: *const u8, n: usize, start: usize, m: *mut Span) -> i32 {
    unsafe { find(STATE.as_mut().unwrap(), std::slice::from_raw_parts(s, n), start, &mut *m) }
}
/* END BOILERPLATE */




/* BOILERPLATE main */
#[no_mangle]
pub extern "C" fn main(argc: i32, argv: *const *const u8) -> i32 { unsafe { ub_main(argc, argv) } }
/* END BOILERPLATE */
