import subprocess, sys

def run(cmd):
    print(f"\n$ {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        sys.exit(result.returncode)

def main():
    # Run unit tests via discovery
    run('python3 -m unittest discover -s tests -p "test_*.py" -v')
    # README checks
    run("python3 scripts/check_readme.py")
    print("\nALL CHECKS PASSED ✅")

if __name__ == "__main__":
    main()
