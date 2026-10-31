"""[B149] lane b149prep: run a NAMED SUBSET of tools/selfcheck.py's check functions
(selfcheck.main() runs all of them; this is the targeted slice for the re-pin).
    python3 docs/dev/lanes/b149prep_checks.py [func ...]   (default: the list below)
Exit 1 on any FAIL. Prints selfcheck's own '-- section --' / PASS / FAIL lines."""
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools")); sys.path.insert(0, ROOT)
import selfcheck as sc
DEFAULT = """check_mechanism_stamps check_deny_flag_controls check_cap_axis check_noedge_axis check_cc_axis
check_cflags_axis check_olevel_axis check_encoding_axis check_opt42_preempts_collapse_policy
check_b104_reqrunenc_rightmost check_b104_k68_flags_mask check_b108_findings_stamp check_b108_litrun_stamp
check_b108_acceptance_mover check_b118_utf_check_stamp check_b118_ctxnode_engine_flip check_b118_clstree_stamps
check_b118_hybreseed_stamp check_b118_findtie_k69_noop_on_bench check_b122_round1_stamps check_b124_stamps
check_b126_stamps check_b135_stamps check_b135s3_stamps check_b136_stamps check_b142_stamps check_b147_stamps
check_b149_stamps check_b135_two_pin_window check_list_axes_registry check_list_definitions_registry
check_list_limits_registry check_emit_size_port check_abi_floor_refusal""".split()
for name in (sys.argv[1:] or DEFAULT):
    try:
        getattr(sc, name)()
    except Exception as e:                                   # noqa: BLE001
        sc.bad("%s raised" % name, "%s: %s" % (type(e).__name__, str(e)[:300]))
print()
print("b149prep_checks: %d passed, %d FAILED" % (len(sc.PASS), len(sc.FAIL)))
for f in sc.FAIL:
    print("FAILED:", f)
sys.exit(1 if sc.FAIL else 0)
