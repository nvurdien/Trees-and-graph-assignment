import sys, re, pathlib

README = pathlib.Path(__file__).resolve().parents[1] / "README.md"
text = README.read_text(encoding="utf-8")

placeholders = ["YOUR ANSWER HERE"]

missing = []
for ph in placeholders:
    if ph in text:
        missing.append(ph)

if missing:
    print("README check: ❌ Found unanswered placeholders:", ", ".join(missing))
    print("Please replace all 'YOUR ANSWER HERE' entries with your answers.")
    sys.exit(1)
else:
    print("README check: ✅ All questions answered.")
    sys.exit(0)
