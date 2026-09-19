// testees/rust/src/main.rs -- the rust-regex batched in-process timing
// driver.
//
// Implements the DRIVER PROTOCOL in pcrecbench/adapters.py verbatim; read
// that first (and testees/re2/driver.cc / testees/onig/driver.c, the
// reference shapes this file's loop is deliberately identical to: same
// argv, same per-subject clock discipline, same find-all advance rule --
// so a difference between rust-regex's and the other engines' numbers is
// the ENGINE, not the harness).
//
// WHY A NATIVE RUST DRIVER, NOT A C DRIVER LINKED AGAINST A C ABI. The
// `regex` crate has no C ABI of its own (`regex-capi`/`rure` is a
// separate, effectively unmaintained wrapper this project does not need
// to add as a dependency); the driver protocol specifies argv/stdout
// SHAPE only, so a driver written entirely in Rust and built by
// `cargo build --release` satisfies it exactly as well as a C or C++ one
// does -- `testees/rust/adapter.py`'s `prepare_driver()` runs `cargo`,
// never `pcrecbench.driverrun.build_driver()` (a C-compiler assumption).
//
// BYTES, NOT `str`, FOR SUBJECTS: every `Regex` this driver builds is
// `regex::bytes::Regex`, which matches over `&[u8]` haystacks that need
// NOT be valid UTF-8 -- this is what makes `non-utf8-subject` satisfiable
// at all (docs/design/capability_set_v1.md 5.1's own row names "Rust
// `regex`'s DEFAULT `str` API" as the engine that refuses non-UTF-8
// input; the bytes API is the documented escape hatch, and using it is
// this adapter's own capability decision, exactly the same shape as RE2's
// `EncodingLatin1` choice or Oniguruma's `ONIG_ENCODING_ASCII` one).
//
// BUT THE PATTERN ITSELF MUST STILL BE VALID UTF-8 -- STRUCTURALLY,
// UNCONDITIONALLY, EVEN IN BYTES MODE. `regex::bytes::RegexBuilder::new`
// takes `&str`, never `&[u8]`; there is no bytes-mode escape hatch for
// the PATTERN SOURCE the way there is for the haystack. This driver
// therefore validates the raw pattern bytes as UTF-8 explicitly, BEFORE
// calling into the `regex` crate at all, and reports a clean structural
// `did-not-compile` (never a panic) naming the exact byte offset where
// validation failed when it is not. See testees/rust/CLAUDE.md's I-72
// section for why this is a genuine, different capability boundary from
// `non-utf8-subject`, discovered on this project's own shared high-byte
// witness pattern.
//
// TWO FORMS, BUT NO DUAL MATCH-INVOCATION LIKE testees/onig/driver.c's
// `onig_match`-vs-`onig_search`. Unlike Oniguruma (whose `\z`-only
// `pcrecbench.record.whole_subject_text` wrap relies on a SEPARATE
// runtime "anchored, no scanning" call to supply the START anchor) and
// unlike RE2/pcre2 (whose runtime API takes an explicit anchor
// parameter/flag), the `regex` crate's public `Regex`/`RegexBuilder`
// exposes NO runtime anchored-search option at all -- `find()` is always
// an unanchored scan from position 0 (it will happily report a match
// starting at byte 40 if there is none at byte 0). So `testees/rust/
// adapter.py` does NOT reuse `pcrecbench.record.whole_subject_text`
// (`(?:pattern)\z`) verbatim the way testees/onig/adapter.py does --
// using it here would UNDER-anchor a whole-subject artifact (a suffix
// match would wrongly pass). Instead the adapter bakes BOTH anchors into
// the compiled text itself: `\A(?:<pattern>)\z`. `\A` and `\z` are both
// real, always-true-position anchors in this crate's syntax (unaffected
// by multi-line mode, unlike `^`/`$`) -- once baked in, an ordinary
// unanchored `find()` call answers the `match` regime correctly with NO
// driver-side branching at all. This is the SAME kind of adapter-level
// decision TRE's own lane made (building its own `^(?:pattern)$` wrap
// rather than reusing the shared helper, for TRE's own different
// anchor-availability reason) -- `--form` is accepted and cross-checked
// against `--mode` purely as a protocol-shape courtesy matching the other
// drivers' convention; it does not change this driver's control flow.
//
// COMPILE COST: one phase, `compile` -- the `RegexBuilder::build()` call,
// timed in-driver. `execution_model = "eager-jit"` WITH THE SAME CAVEAT
// RE2 carries (capability_set_v1.md 7.1/7.2): this call parses the
// pattern and builds the HIR/literal-prefilter analysis, but the lazy DFA
// is built INCREMENTALLY AT MATCH TIME and cached (N2 5) -- not a full
// eager machine-code compile the way pcre2-jit's `pcre2_jit_compile` is.
//
// `giveup:<code>` NEVER FIRES FROM THIS DRIVER. The `regex` crate
// guarantees worst-case LINEAR time in the length of the haystack (no
// catastrophic backtracking is possible by construction) and its public
// match API (`find`/`captures`) returns a plain `Option`, never a
// resource-limit refusal code -- there is nothing to decline at match
// time, the same structural fact RE2's own driver states for its
// `Match()` API (capability_set_v1.md 5.4).
//
// THE PER-SUBJECT TIMEOUT IS A THREAD, NOT A SIGNAL/LONGJMP PAIR. Every
// other driver in this project uses `sigsetjmp`/`siglongjmp` across a
// SIGALRM handler; doing the same across Rust stack frames is undefined
// behavior (longjmp does not run Rust destructors, and Rust's own
// unwinding/aliasing invariants assume normal control flow only -- this
// is not a stylistic preference, `std::panic` documents that unwinding
// across an FFI boundary that does not expect it is UB, and a raw
// longjmp is the same hazard one layer lower). This driver instead runs
// each subject's timed operation on a plain (non-scoped) OS thread when
// `--subject-timeout` is set, and the MAIN thread waits on a channel with
// `recv_timeout`: if the timeout elapses first, the subject is reported
// `timedout` and the abandoned thread is left to finish (or not) on its
// own -- its result, if it ever arrives, is silently dropped. This is a
// SAFETY-NET-ONLY mechanism given the crate's own linear-time guarantee
// (unlike Oniguruma/pcre2, where a ReDoS witness can genuinely hang, a
// rust-regex timeout can only be provoked by raw input SIZE, not
// backtracking blowup -- capability_set_v1.md 5's own "redos-nested"
// family finding). The clock discipline itself (one `Instant::now()`
// reading before the `iters` loop, another after) happens INSIDE the
// timed thread, so a timeout detection's own thread-spawn latency is
// never part of a reported number, whether or not a timeout ever fires.

use regex::bytes::{Regex, RegexBuilder};
use std::env;
use std::fs;
use std::io::{self, BufRead, Write};
use std::path::PathBuf;
use std::sync::mpsc;
use std::thread;
use std::time::{Duration, Instant};

// RegexBuilder's own documented defaults, as of the `regex` crate version
// this project's research cited (docs/design/capability_set_v1.md 5's
// wild-datetime row: "RE2's max_mem and Rust's size_limit are the ones
// to watch"). NOT YET RECONFIRMED against the exact version Cargo.lock
// pins at this box's first build (testees/rust/CLAUDE.md's OWED item) --
// stated as CLI defaults here, not baked in unconditionally, so a future
// `rust-smallsize` config (capability_set_v1.md 8's own roster row) needs
// no driver change, only a new `--size-limit`/`--dfa-size-limit` value in
// configs.toml.
const DEFAULT_SIZE_LIMIT: usize = 10 * (1 << 20); // 10 MiB
const DEFAULT_DFA_SIZE_LIMIT: usize = 2 * (1 << 20); // 2 MiB

fn now() -> Instant {
    Instant::now()
}

fn die(what: &str) -> ! {
    println!("error\t{}", what);
    io::stdout().flush().ok();
    std::process::exit(2);
}

fn slurp(path: &PathBuf) -> io::Result<Vec<u8>> {
    fs::read(path)
}

struct Subject {
    id: String,
    buf: Vec<u8>,
}

fn load_list(path: &PathBuf) -> io::Result<Vec<Subject>> {
    let f = fs::File::open(path)?;
    let mut out = Vec::new();
    for line in io::BufReader::new(f).lines() {
        let line = line?;
        let line = line.trim_end_matches(['\n', '\r']);
        if line.is_empty() {
            continue;
        }
        let mut parts = line.splitn(2, '\t');
        let id = match parts.next() {
            Some(s) if !s.is_empty() => s.to_string(),
            _ => continue,
        };
        let subj_path = match parts.next() {
            Some(s) => s,
            None => continue,
        };
        let buf = slurp(&PathBuf::from(subj_path))?;
        out.push(Subject { id, buf });
    }
    Ok(out)
}

/// The bracketed name this driver embeds in its `error` line
/// (`regex build failed [<name>]: <message>`), read from `regex::Error`'s
/// own stable `Debug` variant name rather than an exhaustive `match` --
/// `regex::Error` is `#[non_exhaustive]` (the crate's own MSRV-stability
/// promise: a new variant can appear in a minor release), so a `match`
/// would need a wildcard arm regardless; reading the Debug name is the
/// SAME "adapter classifies structurally, driver only reports" split
/// `testees/re2/driver.cc`'s header states for its own `error_code_name`.
/// `testees/rust/adapter.py`'s `classify_refusal` is the single place
/// that maps this name to `refusal_class`.
fn error_variant_name(e: &regex::Error) -> String {
    let dbg = format!("{:?}", e);
    dbg.split(['(', ' '])
        .next()
        .unwrap_or("Unknown")
        .to_string()
}

fn caps_string(n_groups: usize, spans: &[(i64, i64)]) -> String {
    if n_groups == 0 || spans.is_empty() {
        return "-".to_string();
    }
    let mut parts = Vec::with_capacity(spans.len());
    for (s, e) in spans {
        parts.push(format!("{}:{}", s, e));
    }
    parts.join(",")
}

/// One subject's worth of work: `iters` repeats of the SAME operation
/// (find, or find-all in `--find-all` mode), only the FINAL iteration's
/// answer is reported -- the same convention every other driver in this
/// project holds to (the timed loop is deliberately homogeneous; what
/// varies is only how long it took).
struct SubjectResult {
    matched: bool,
    start: i64,
    end: i64,
    nmatches: i64, // -1 == "-" (not --find-all)
    caps: Vec<(i64, i64)>, // 1-based groups 1..n, empty when ncaps == 0
    elapsed: f64,
}

fn run_subject(re: &Regex, buf: &[u8], iters: i64, find_all: bool) -> SubjectResult {
    let ncap = re.captures_len().saturating_sub(1); // group 0 excluded, RE2/onig convention
    let mut matched = false;
    let mut start: i64 = -1;
    let mut end: i64 = -1;
    let mut nmatches: i64 = -1;
    let mut caps: Vec<(i64, i64)> = Vec::new();

    let t0 = now();
    for _ in 0..iters.max(1) {
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
                pos = if me > ms { me } else { ms + 1 };
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

struct Args {
    pattern_path: Option<PathBuf>,
    list_path: Option<PathBuf>,
    mode: String,
    form: String,
    iters: i64,
    compile_trials: i64,
    subject_timeout: u64,
    skip: usize,
    find_all: bool,
    size_limit: usize,
    dfa_size_limit: usize,
}

fn parse_args() -> Args {
    let argv: Vec<String> = env::args().collect();
    let mut a = Args {
        pattern_path: None,
        list_path: None,
        mode: "search".to_string(),
        form: "plain".to_string(),
        iters: 1,
        compile_trials: 1,
        subject_timeout: 0,
        skip: 0,
        find_all: false,
        size_limit: DEFAULT_SIZE_LIMIT,
        dfa_size_limit: DEFAULT_DFA_SIZE_LIMIT,
    };
    let mut i = 1;
    while i < argv.len() {
        let arg = argv[i].as_str();
        macro_rules! next {
            () => {{
                i += 1;
                if i >= argv.len() {
                    die(&format!("{} requires a value", arg));
                }
                argv[i].clone()
            }};
        }
        match arg {
            "--pattern" => a.pattern_path = Some(PathBuf::from(next!())),
            "--list" => a.list_path = Some(PathBuf::from(next!())),
            "--mode" => a.mode = next!(),
            "--form" => a.form = next!(),
            "--iters" => a.iters = next!().parse().unwrap_or(1),
            "--compile-trials" => a.compile_trials = next!().parse().unwrap_or(1),
            "--subject-timeout" => a.subject_timeout = next!().parse().unwrap_or(0),
            "--skip" => a.skip = next!().parse().unwrap_or(0),
            "--find-all" => a.find_all = true,
            "--size-limit" => a.size_limit = next!().parse().unwrap_or(DEFAULT_SIZE_LIMIT),
            "--dfa-size-limit" => {
                a.dfa_size_limit = next!().parse().unwrap_or(DEFAULT_DFA_SIZE_LIMIT)
            }
            other => die(&format!("unknown argument {}", other)),
        }
        i += 1;
    }
    a
}

fn main() {
    let args = parse_args();
    let pattern_path = match &args.pattern_path {
        Some(p) => p.clone(),
        None => die("--pattern is required"),
    };
    let iters = if args.iters < 1 { 1 } else { args.iters };

    // Cross-check mirroring testees/onig/driver.c's `--mode`/`--form`
    // pair: this driver's own control flow does not actually branch on
    // `--form` (see this file's header), but the flags are still checked
    // together so a future adapter bug that decouples them fails LOUDLY
    // rather than quietly measuring the wrong regime.
    if args.list_path.is_some() {
        let mode_wants_whole = args.mode == "match";
        let form_is_whole = args.form == "whole-subject";
        if mode_wants_whole != form_is_whole {
            die("--mode and --form disagree (this driver expects the \
                 whole-subject anchor baked into --pattern's text by the \
                 adapter, not a second runtime dial)");
        }
    }

    let stdout = io::stdout();
    let mut lock = stdout.lock();
    // Unlike the C/C++ drivers' setvbuf(_IOLBF), Rust's stdout is
    // line-buffered by default only when it detects a terminal; explicit
    // flushes after every printed line (below) give python the SAME
    // liveness/crash-attribution guarantee `pcrecbench/adapters.py`'s
    // protocol docstring requires regardless of what stdout is attached
    // to.
    macro_rules! emit {
        ($($arg:tt)*) => {{
            writeln!(lock, $($arg)*).ok();
            lock.flush().ok();
        }};
    }

    emit!("info\tsize_limit\t{}", args.size_limit);
    emit!("info\tdfa_size_limit\t{}", args.dfa_size_limit);
    emit!("info\tform\t{}", args.form);

    let pat_bytes = match slurp(&pattern_path) {
        Ok(b) => b,
        Err(e) => {
            emit!("error\tcannot read pattern {}: {}", pattern_path.display(), e);
            std::process::exit(2);
        }
    };

    // THE STRUCTURAL UTF-8 CHECK (this file's header, and testees/rust/
    // CLAUDE.md's I-72 section): `regex::bytes::RegexBuilder::new` takes
    // `&str`. A pattern file containing raw, non-UTF-8-valid bytes (this
    // project's own I-72 witness among them) fails HERE, cleanly, naming
    // the exact byte offset -- never a panic, never a silent
    // reinterpretation.
    let pat_str: &str = match std::str::from_utf8(&pat_bytes) {
        Ok(s) => s,
        Err(e) => {
            emit!(
                "error\tpattern is not valid UTF-8 at byte {}: {}",
                e.valid_up_to(),
                e
            );
            std::process::exit(3);
        }
    };

    let mut re: Option<Regex> = None;
    for t in 1..=args.compile_trials.max(1) {
        let t0 = now();
        let built = RegexBuilder::new(pat_str)
            .size_limit(args.size_limit)
            .dfa_size_limit(args.dfa_size_limit)
            .build();
        let elapsed = t0.elapsed().as_secs_f64();
        match built {
            Ok(r) => {
                emit!("compile\t{}\tcompile\t{:.9}", t, elapsed);
                re = Some(r);
            }
            Err(e) => {
                let name = error_variant_name(&e);
                emit!("error\tregex build failed [{}]: {}", name, e);
                std::process::exit(3);
            }
        }
    }
    let re = re.expect("compile_trials >= 1 guarantees a compiled regex or an early exit");

    // engine_metadata, `pattern`-scoped (record_schema.md 7 rule 2):
    // declared in testees/rust/adapter.py's METADATA_DECL.
    let ncap = re.captures_len().saturating_sub(1);
    let named_count = re.capture_names().filter(|n| n.is_some()).count();
    emit!("info\tncapturegroups\t{}", ncap);
    emit!("info\tnamed_count\t{}", named_count);

    let list_path = match &args.list_path {
        Some(p) => p.clone(),
        None => {
            io::stdout().flush().ok();
            std::process::exit(0); // compile-only run
        }
    };

    let subs = match load_list(&list_path) {
        Ok(v) => v,
        Err(e) => {
            emit!("error\tcannot read subject list {}: {}", list_path.display(), e);
            std::process::exit(2);
        }
    };

    for s in subs.into_iter().skip(args.skip) {
        let id = s.id.clone();
        let buf_len = s.buf.len();

        let result: Option<SubjectResult> = if args.subject_timeout > 0 {
            // See this file's header: a thread + channel, never a
            // signal/longjmp pair (unsound across Rust frames). The
            // regex clone is Arc-based (cheap, `regex::bytes::Regex`'s
            // own documented sharing story); `buf` moves into the
            // thread, owned, so the main thread's loop borrows nothing
            // across the timeout boundary.
            let re2 = re.clone();
            let buf = s.buf;
            let iters = iters;
            let find_all = args.find_all;
            let (tx, rx) = mpsc::channel();
            thread::spawn(move || {
                let r = run_subject(&re2, &buf, iters, find_all);
                let _ = tx.send(r); // Err is fine: the receiver may be gone (timed out)
            });
            match rx.recv_timeout(Duration::from_secs(args.subject_timeout)) {
                Ok(r) => Some(r),
                Err(mpsc::RecvTimeoutError::Timeout) => None,
                // Disconnected means the worker thread PANICKED rather
                // than hung -- a real, different finding this driver
                // cannot yet distinguish on the wire (the protocol has
                // no per-subject `crashed` answer, only `timedout`).
                // Mapped to the same `timedout` row rather than
                // crashing the whole process (Rust does not propagate a
                // child thread's panic to the main thread by default),
                // so one bad subject does not lose every subject after
                // it. A distinguishing crash-message channel is a
                // future refinement, not built this lane.
                Err(mpsc::RecvTimeoutError::Disconnected) => None,
            }
        } else {
            Some(run_subject(&re, &s.buf, iters, args.find_all))
        };

        let r = match result {
            Some(r) => r,
            None => {
                // The reported elapsed is the CONFIGURED timeout, not a
                // measured value: `recv_timeout` blocks for exactly that
                // long before returning, deterministically, unlike the
                // C/C++ drivers' `volatile double elapsed = 0.0` (never
                // assigned before their siglongjmp skips past it). Named
                // here since a reader comparing this column across
                // engines should know the two are not the same
                // quantity on a timed-out row.
                emit!(
                    "subject\t{}\ttimedout\t-\t-\t0\t-\t{}\t{:.9}\t-\t-",
                    id,
                    iters,
                    args.subject_timeout as f64
                );
                continue;
            }
        };

        let ncap_out = r.caps.len();
        let (answer, sbuf, ebuf, capsbuf) = if r.matched {
            (
                "match".to_string(),
                r.start.to_string(),
                r.end.to_string(),
                caps_string(ncap_out, &r.caps),
            )
        } else {
            ("nomatch".to_string(), "-".to_string(), "-".to_string(), "-".to_string())
        };
        let nbuf = if args.find_all && r.nmatches >= 0 {
            r.nmatches.to_string()
        } else {
            "-".to_string()
        };

        // consumed_length: the whole subject -- regex::bytes::Regex's
        // find/captures take an explicit &[u8] slice and expose no scan
        // high-water mark, the SAME convention testees/pcre2/CLAUDE.md
        // and testees/re2/CLAUDE.md state for their own engines: "no
        // byte was withheld or refused", never "the engine looked at
        // every byte".
        emit!(
            "subject\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{:.9}\t{}\t{}",
            id, answer, sbuf, ebuf, ncap_out, buf_len, iters, r.elapsed, nbuf, capsbuf
        );
    }

    io::stdout().flush().ok();
}
