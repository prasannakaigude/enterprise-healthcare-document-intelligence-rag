"""Run a local project health check from the command line."""

from pathlib import Path
from pprint import pprint
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.app.core.health import get_health_status


def main() -> None:
    """Print the current backend health status."""

    pprint(get_health_status())


if __name__ == "__main__":
    main()
