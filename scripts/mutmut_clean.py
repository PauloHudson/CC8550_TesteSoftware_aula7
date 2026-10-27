import subprocess
import sys


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Uso: python scripts/mutmut_clean.py ex1")

    result = subprocess.run(
        ["mutmut", "run"],
        cwd=sys.argv[1],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    sys.stdout.write(result.stdout.encode("ascii", "ignore").decode("ascii"))
    raise SystemExit(result.returncode)


if __name__ == "__main__":
    main()