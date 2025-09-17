#!/usr/bin/env bash
set -e
python3 -m unittest discover -s tests -p "test_*.py" -v
python3 scripts/check_readme.py
echo
echo 'ALL CHECKS PASSED ✅'
