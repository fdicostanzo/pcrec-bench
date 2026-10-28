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
#[repr(C)]
pub struct UbVar { name: *const std::os::raw::c_char, p: *const u8, len: usize }
/* one call's binding: get("name") is the value, or None when it is UNSET */
pub struct Binding<'a> { v: &'a [UbVar] }
impl<'a> Binding<'a> {
    fn get(&self, name: &str) -> Option<&'a [u8]> {
        let x = self.v.iter().find(|x| unsafe { std::ffi::CStr::from_ptr(x.name) }.to_bytes() == name.as_bytes())?;
        if x.p.is_null() { None } else { Some(unsafe { std::slice::from_raw_parts(x.p, x.len) }) }
    }
}
/* END BOILERPLATE */
/* BOILERPLATE shim */
type Cache = HashMap<Vec<u8>, Regex>;   /* the compiled-pattern cache */
/* END BOILERPLATE */

/* BOILERPLATE shim */
struct State {
/* END BOILERPLATE */
/* BOILERPLATE shim */
}
fn setup(pattern: &[u8]) -> Result<State, String> {
/* END BOILERPLATE */
    Ok(State {})
/* BOILERPLATE shim */
}
/* END BOILERPLATE */

fn lit(v: &[u8]) -> String { v.iter().map(|c| format!("\\x{:02x}", c)).collect() }
fn run(cache: &mut Cache, pat: String, line: &[u8], m: &mut Span) -> i32 {
    let re = cache.entry(pat.clone().into_bytes()).or_insert_with(|| Regex::new(&pat).unwrap());
    re.find(line).map_or(UB_N, |x| { m.s = x.start() as i64; m.e = x.end() as i64; UB_M })
}

/* ASSIST: one call. `line` is matched alone (offsets line-relative);
 * b.get("name") is the variable's value or None when UNSET. Keep compiled
 * patterns in `cache`. */
/* BOILERPLATE shim */
fn vars(st: &mut State, cache: &mut Cache, line: &[u8], b: &Binding, m: &mut Span) -> i32 {
/* END BOILERPLATE */
    let p = b.get("prefix").filter(|p| !p.is_empty()).unwrap_or(b"api");
    let Some(r) = b.get("res") else { return UB_R };
    let f = if b.get("fmt").is_some() { "\\.json" } else { "" };
    run(cache, format!("(?-u)^/{}/v[0-9]+/{}{}(?:\\?|$)", lit(p), lit(r), f), line, m)
/* BOILERPLATE shim */
}
static mut STATE: Option<State> = None;
static mut CACHE: Option<Cache> = None;
#[no_mangle]
pub extern "C" fn ub_setup(p: *const u8, n: usize, _member: *const u8) -> i32 {
    let r = setup(unsafe { std::slice::from_raw_parts(p, n) });
    r.map(|st| unsafe { STATE = Some(st) }).map_or_else(fail, |_| 0)
}
/* END BOILERPLATE */
/* BOILERPLATE shim */
#[no_mangle]
pub extern "C" fn ub_vars(l: *const u8, n: usize, v: *const UbVar, nv: usize, m: *mut Span) -> i32 {
    unsafe {
        let b = Binding { v: std::slice::from_raw_parts(v, nv) };
        vars(STATE.as_mut().unwrap(), CACHE.get_or_insert_with(HashMap::new), std::slice::from_raw_parts(l, n), &b, &mut *m)
    }
}
#[no_mangle]
pub extern "C" fn ub_reset() { unsafe { CACHE = None } }
/* END BOILERPLATE */

/* BOILERPLATE main */
#[no_mangle]
pub extern "C" fn main(argc: i32, argv: *const *const u8) -> i32 { unsafe { ub_main(argc, argv) } }
/* END BOILERPLATE */
