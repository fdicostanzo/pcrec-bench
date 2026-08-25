# pcrec-bench — plain GNU make, on purpose (pcrec's D2 posture: a stranger's
# `make` must work with nothing installed but the toolchain). Testee adapters
# may use whatever their engine demands (cmake, cargo, meson); THIS file only
# ever drives what is ours.
#
# check-schema is the first target, so a bare `make` runs it.

PYTHON ?= python3
VALIDATE = $(PYTHON) schema/validate.py
EXAMPLES = schema/examples
BAD      = $(EXAMPLES)/bad

.PHONY: check check-schema check-harness deps help

## check-schema: validate the record schema, its examples and its sabotages
#
# Three checks, and the third is the one that makes the other two mean
# anything (pcrec's check-design lesson: a check with no failing case proves
# nothing).
#
#   1. the design note's field tables vs the JSON Schema, field for field;
#   2. every record in examples/ must be ACCEPTED (with --check-filename, so
#      the file-name rule X4 is exercised by the good examples too);
#   3. every record in examples/bad/ must be REJECTED, and rejected FOR THE
#      RULE ITS NAME CLAIMS -- the file name's leading token (`x11-...`,
#      `schema-...`) is the rule id the run requires to fire. A control that
#      rejects for an unrelated reason is not a control.
check-schema:
	@echo "== check-schema =="
	@$(PYTHON) schema/check_fields.py
	@echo
	@echo "-- good examples (must be ACCEPTED) --"
	@$(VALIDATE) --check-filename $(EXAMPLES)/*.jsonl
	@echo
	@echo "-- sabotaged examples (must be REJECTED, each for its own rule) --"
	@set -e; \
	 good=0; bad=0; \
	 for f in $(BAD)/*.jsonl; do \
	     b=$$(basename "$$f"); \
	     rule=$$(printf '%s' "$${b%%-*}" | tr 'a-z' 'A-Z'); \
	     extra=""; \
	     case "$$b" in x4-*) extra="--check-filename" ;; esac; \
	     if $(VALIDATE) --expect-reject --expect-rule "$$rule" $$extra "$$f" \
	            > /dev/null; then \
	         bad=$$((bad + 1)); \
	         printf '   %-44s rejected [%s]\n' "$$b" "$$rule"; \
	     else \
	         good=$$((good + 1)); \
	         printf '   %-44s NOT REJECTED AS INTENDED [%s]\n' "$$b" "$$rule"; \
	         $(VALIDATE) --expect-reject --expect-rule "$$rule" $$extra "$$f" \
	             || true; \
	     fi; \
	 done; \
	 echo; \
	 ngood=$$(ls -1 $(EXAMPLES)/*.jsonl | wc -l); \
	 echo "check-schema: $$ngood example(s) accepted, $$bad sabotage(s) rejected for the intended rule, $$good sabotage(s) WRONG"; \
	 test "$$good" -eq 0

## check: every self-check -- the schema's and the harness's (contract 6)
#
# check-schema is [B2]'s (the record schema, its examples, its 15 sabotages).
# check-harness is [B3]'s: the sub-bench generators reproduce their committed
# manifests, the expectations re-derive from the libpcre2 oracle, each driver
# smokes, the deliberately-wrong fixture yields the outcome it must, the two
# patterns are shown NOT to be one artifact, and a full `run` of one cell into
# a SCRATCH store is written and validator-accepted.
#
# It is a SMOKE SUITE, not a measurement: --trials 1 --iters 1, one regime,
# --force-unquiet, and every record it writes is marked `synthetic`. Nothing
# here may be read as a number.
check: check-schema check-harness

## check-harness: the harness self-checks (tools/selfcheck.py)
check-harness:
	@LC_ALL=C $(PYTHON) tools/selfcheck.py

## deps: report what the harness needs and whether this box has it
deps:
	@echo "== deps =="
	@LC_ALL=C $(PYTHON) -c "import sys; print('python      ', sys.version.split()[0], '(3.11+ needed for tomllib)')"
	@LC_ALL=C $(PYTHON) -c "import jsonschema; print('jsonschema  ', jsonschema.__version__)" \
	    || echo "jsonschema   MISSING -- pip install -r requirements.txt"
	@LC_ALL=C $(PYTHON) -c "import ctypes; ctypes.CDLL('libpcre2-8.so.0'); print('libpcre2-8   present (the expectation ORACLE and one testee)')" \
	    || echo "libpcre2-8   MISSING -- expectations cannot be re-derived and the pcre2 testee cannot run"
	@command -v mpstat  >/dev/null && echo "mpstat       present (the occupancy gate)" || echo "mpstat       MISSING -- occupancy is recorded 'unavailable', never skipped"
	@command -v taskset >/dev/null && echo "taskset      present (--pin)"              || echo "taskset      MISSING -- pinning is recorded 'unavailable'"
	@command -v gnutimeout >/dev/null && echo "gnutimeout   present"                   || echo "gnutimeout   MISSING -- driver processes run unguarded"
	@echo "$(CC)          $$($(CC) --version 2>/dev/null | head -1)"

## help: list the targets
help:
	@echo "pcrec-bench targets:"
	@grep -E '^## ' $(MAKEFILE_LIST) | sed -e 's/^## /  /'
