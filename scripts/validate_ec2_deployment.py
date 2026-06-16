"""Validate that the EC2 deployment path files are present."""

from pathlib import Path
import pprint
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def validate_ec2_deployment_files(project_root: Path = PROJECT_ROOT) -> dict:
    """Return a simple validation report for EC2 deployment files."""

    required_files = {
        "ec2_readme": project_root / "deployment" / "ec2" / "README.md",
        "ec2_user_data": project_root / "deployment" / "ec2" / "user_data.sh",
        "compose_base": project_root / "docker-compose.yml",
        "compose_ec2": project_root / "docker-compose.ec2.yml",
    }

    files = {
        name: {
            "path": str(path),
            "exists": path.exists(),
        }
        for name, path in required_files.items()
    }

    status = "ok" if all(file_info["exists"] for file_info in files.values()) else "error"

    return {
        "status": status,
        "files": files,
        "recommended_start_command": (
            "docker compose -f docker-compose.yml -f docker-compose.ec2.yml up -d --build"
        ),
    }


def main() -> None:
    """Print the EC2 deployment validation report."""

    report = validate_ec2_deployment_files()
    pprint.pprint(report)

    if report["status"] != "ok":
        sys.exit(1)


if __name__ == "__main__":
    main()
