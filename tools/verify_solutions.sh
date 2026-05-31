#!/usr/bin/env bash
# Verify every lab two ways:
#   1) the shipped stub should FAIL its tests (lab isn't accidentally pre-solved)
#   2) the reference solution should PASS its tests (lab is actually correct)
#
# For each lab it backs up the learner file, drops the solution in, runs pytest,
# then restores the stub. Run from anywhere:
#     bash tools/verify_solutions.sh
set -u
cd "$(dirname "$0")/.." || exit 1
PY="./.venv/bin/python"

stub_fail_ok=1
sol_pass_ok=1

echo "================ STUBS (each should FAIL) ================"
for sol in labs/*/*_solution.py; do
  dir=$(dirname "$sol")
  topic=$(basename "$sol"); topic=${topic%_solution.py}
  if "$PY" -m pytest "$dir" -q >/tmp/stub_$topic.log 2>&1; then
    echo "  UNEXPECTED PASS (stub solved?)  $dir"
    stub_fail_ok=0
  else
    echo "  ok, stub fails                  $dir"
  fi
done

echo ""
echo "================ SOLUTIONS (each should PASS) ============"
for sol in labs/*/*_solution.py; do
  dir=$(dirname "$sol")
  topic=$(basename "$sol"); topic=${topic%_solution.py}
  learner="$dir/$topic.py"
  cp "$learner" "/tmp/stub_keep_$topic.py"
  cp "$sol" "$learner"
  if "$PY" -m pytest "$dir" -q >/tmp/sol_$topic.log 2>&1; then
    echo "  PASS  $dir"
  else
    echo "  FAIL  $dir   -> /tmp/sol_$topic.log"
    sol_pass_ok=0
  fi
  cp "/tmp/stub_keep_$topic.py" "$learner"
done

echo ""
echo "================ RESULT =================================="
if [ "$stub_fail_ok" -eq 1 ] && [ "$sol_pass_ok" -eq 1 ]; then
  echo "ALL GOOD: every stub fails, every solution passes."
  exit 0
else
  echo "PROBLEMS FOUND. Check the logs in /tmp above."
  exit 1
fi
