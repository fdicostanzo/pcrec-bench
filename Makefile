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

.PHONY: check-schema help

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

## help: list the targets
help:
	@echo "pcrec-bench targets:"
	@grep -E '^## ' $(MAKEFILE_LIST) | sed -e 's/^## /  /'
