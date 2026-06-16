"""Run the Streamlit frontend locally."""

from pathlib import Path
import subprocess
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    """Start the Streamlit frontend."""

    subprocess.run(
        [
            sys.executable,
            "-m",
            "streamlit",
            "run",
            str(PROJECT_ROOT / "frontend" / "app.py"),
        ],
        check=True,
    )


if __name__ == "__main__":
    main()

