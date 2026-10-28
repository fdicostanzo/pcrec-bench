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


/* BOILERPLATE wrappers */
extern "C" {
    fn ub_pred(s: *const u8, n: usize, b: usize, c: usize) -> i32;
}
fn pred(s: &[u8], b: usize, c: usize) -> bool { unsafe { ub_pred(s.as_ptr(), s.len(), b, c) != 0 } }
/* END BOILERPLATE */

/* BOILERPLATE shim */
struct State {
/* END BOILERPLATE */
    re: Regex,
/* BOILERPLATE shim */
}
fn setup(pattern: &[u8]) -> Result<State, String> {
/* END BOILERPLATE */
    Ok(State { re: Regex::new(r"(?-u)\buser=(\w+)").map_err(|e| e.to_string())? })
/* BOILERPLATE shim */
}
/* END BOILERPLATE */

/* ASSIST: the first PASSING candidate at or after `start` in the whole
 * subject `s` (bytes before `start` stay visible). pred(s, b, c) is the
 * member's shared predicate on group 1 = [b, c). Fill m.s, m.e and group 1
 * in m.g1s, m.g1e. */
/* BOILERPLATE shim */
fn find(st: &mut State, s: &[u8], start: usize, m: &mut Span) -> i32 {
/* END BOILERPLATE */
    let mut at = start;
    while let Some(c) = st.re.captures_at(s, at) {
        let (w, g) = (c.get(0).unwrap(), c.get(1).unwrap());
        if pred(s, g.start(), g.end()) {
            *m = Span { s: w.start() as i64, e: w.end() as i64, g1s: g.start() as i64, g1e: g.end() as i64 };
            return UB_M;
        }
        at = w.start() + 1;
    }
    UB_N
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
