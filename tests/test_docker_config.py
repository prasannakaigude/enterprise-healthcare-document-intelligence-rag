from pathlib import Path
import unittest

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class DockerConfigTests(unittest.TestCase):
    def test_backend_dockerfile_exists_and_runs_uvicorn(self):
        dockerfile = PROJECT_ROOT / "backend" / "Dockerfile"

        self.assertTrue(dockerfile.exists())
        contents = dockerfile.read_text()
        self.assertIn("python:3.11-slim", contents)
        self.assertIn("uvicorn", contents)
        self.assertIn("backend.app.main:app", contents)

    def test_frontend_dockerfile_exists_and_runs_streamlit(self):
        dockerfile = PROJECT_ROOT / "frontend" / "Dockerfile"

        self.assertTrue(dockerfile.exists())
        contents = dockerfile.read_text()
        self.assertIn("python:3.11-slim", contents)
        self.assertIn("streamlit", contents)
        self.assertIn("frontend/app.py", contents)

    def test_docker_compose_defines_backend_and_frontend(self):
        compose_file = PROJECT_ROOT / "docker-compose.yml"
        compose = yaml.safe_load(compose_file.read_text())

        self.assertIn("backend", compose["services"])
        self.assertIn("frontend", compose["services"])
        self.assertEqual(compose["services"]["backend"]["ports"], ["8000:8000"])
        self.assertEqual(compose["services"]["frontend"]["ports"], ["8501:8501"])
        self.assertIn("./data:/app/data", compose["services"]["backend"]["volumes"])
        self.assertIn("./data:/app/data", compose["services"]["frontend"]["volumes"])

    def test_dockerignore_excludes_secrets_and_local_data(self):
        dockerignore = (PROJECT_ROOT / ".dockerignore").read_text()

        self.assertIn(".env", dockerignore)
        self.assertIn("data/raw/*", dockerignore)
        self.assertIn("data/vector_db/chroma/*", dockerignore)


if __name__ == "__main__":
    unittest.main()
