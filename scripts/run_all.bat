@echo off
python -m unittest discover -s tests -p "test_*.py" -v
IF ERRORLEVEL 1 EXIT /B 1
python scripts\check_readme.py
IF ERRORLEVEL 1 EXIT /B 1
echo.
echo ALL CHECKS PASSED ✅
