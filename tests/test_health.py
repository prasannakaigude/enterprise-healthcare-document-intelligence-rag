from pathlib import Path
import unittest

from backend.app.core.health import get_health_status
from backend.app.core.settings import Settings, get_settings


class SettingsTests(unittest.TestCase):
    def test_default_settings_have_expected_local_paths(self):
        settings = get_settings()

        self.assertEqual(settings.environment, "local")
        self.assertEqual(settings.aws_region, "us-east-1")
        self.assertEqual(settings.aws_s3_raw_prefix, "healthcare-documents/raw")
        self.assertTrue(str(settings.raw_data_dir).endswith("data/raw"))
        self.assertTrue(str(settings.processed_data_dir).endswith("data/processed"))
        self.assertTrue(str(settings.chroma_db_dir).endswith("data/vector_db/chroma"))
        self.assertEqual(settings.embedding_model, "text-embedding-3-small")
        self.assertEqual(settings.chat_model, "gpt-4o-mini")
        self.assertEqual(settings.chat_temperature, 0.0)
        self.assertEqual(settings.chroma_collection_name, "healthcare_documents")
        self.assertEqual(settings.chunk_size, 1000)
        self.assertEqual(settings.chunk_overlap, 200)
        self.assertEqual(settings.retrieval_top_k, 4)


class HealthCheckTests(unittest.TestCase):
    def test_health_status_is_ok(self):
        settings = Settings(
            raw_data_dir=Path("data/raw"),
            processed_data_dir=Path("data/processed"),
            chroma_db_dir=Path("data/vector_db/chroma"),
        )

        status = get_health_status(settings)

        self.assertEqual(status["status"], "ok")
        self.assertEqual(status["app_version"], "0.15.0")
        self.assertIn("paths", status)
        self.assertIn("raw_data_dir", status["paths"])
        self.assertIn("processed_data_dir", status["paths"])
        self.assertIn("chroma_db_dir", status["paths"])


if __name__ == "__main__":
    unittest.main()
