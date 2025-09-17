#!/usr/bin/env bash
set -e
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/check_readme.py
echo
echo 'ALL CHECKS PASSED ✅'
