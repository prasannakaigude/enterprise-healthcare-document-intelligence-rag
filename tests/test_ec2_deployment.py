from pathlib import Path
import unittest

import yaml

from scripts.validate_ec2_deployment import validate_ec2_deployment_files


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class EC2DeploymentTests(unittest.TestCase):
    def test_ec2_deployment_files_exist(self):
        report = validate_ec2_deployment_files(PROJECT_ROOT)

        self.assertEqual(report["status"], "ok")
        self.assertIn("docker compose", report["recommended_start_command"])

    def test_ec2_compose_override_sets_restart_policy(self):
        compose_file = PROJECT_ROOT / "docker-compose.ec2.yml"
        compose = yaml.safe_load(compose_file.read_text())

        self.assertEqual(compose["services"]["backend"]["restart"], "unless-stopped")
        self.assertEqual(compose["services"]["frontend"]["restart"], "unless-stopped")
        self.assertIn("healthcare_data", compose["volumes"])

    def test_user_data_installs_docker_without_secrets(self):
        user_data = (PROJECT_ROOT / "deployment" / "ec2" / "user_data.sh").read_text()

        self.assertIn("docker-ce", user_data)
        self.assertIn("docker-compose-plugin", user_data)
        self.assertIn("Do not place real API keys", user_data)
        self.assertNotIn("OPENAI_API_KEY=", user_data)
        self.assertNotIn("AWS_SECRET_ACCESS_KEY=", user_data)

    def test_ec2_readme_documents_security_basics(self):
        readme = (PROJECT_ROOT / "deployment" / "ec2" / "README.md").read_text()

        self.assertIn("IAM role", readme)
        self.assertIn("HTTPS", readme)
        self.assertIn("Do not commit `.env`", readme)


if __name__ == "__main__":
    unittest.main()
