import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from backend.app.main import app
from backend.app.rag.answer_generator import GroundedAnswer, SourceCitation
from backend.app.rag.indexing import IndexingResult


class APITests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_health_endpoint_returns_status(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(body["status"], "ok")
        self.assertEqual(body["app_version"], "0.15.0")
        self.assertIn("Healthcare", body["app_name"])

    def test_ask_endpoint_returns_grounded_answer(self):
        fake_answer = GroundedAnswer(
            answer="Patients should monitor blood pressure regularly.",
            citations=[
                SourceCitation(
                    file_name="hypertension-guide.pdf",
                    page_number=4,
                    chunk_id="hypertension-guide.pdf:page-4:chunk-1",
                )
            ],
        )

        with patch("backend.app.api.routes.answer_question", return_value=fake_answer) as mock_answer, patch(
            "backend.app.api.routes.write_conversation_log"
        ) as mock_logger:
            response = self.client.post(
                "/ask",
                json={
                    "question": "How should hypertension be monitored?",
                    "file_name": "hypertension-guide.pdf",
                },
            )

        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(body["answer"], fake_answer.answer)
        self.assertEqual(body["citations"][0]["file_name"], "hypertension-guide.pdf")
        self.assertEqual(body["citations"][0]["page_number"], 4)
        mock_answer.assert_called_once_with(
            question="How should hypertension be monitored?",
            file_name="hypertension-guide.pdf",
        )
        mock_logger.assert_called_once()

    def test_ask_endpoint_rejects_empty_question(self):
        response = self.client.post("/ask", json={"question": ""})

        self.assertEqual(response.status_code, 422)

    def test_ask_endpoint_maps_value_error_to_bad_request(self):
        with patch(
            "backend.app.api.routes.answer_question",
            side_effect=ValueError("OPENAI_API_KEY is not set."),
        ):
            response = self.client.post("/ask", json={"question": "What is covered?"})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], "OPENAI_API_KEY is not set.")

    def test_rebuild_endpoint_returns_indexing_result(self):
        fake_result = IndexingResult(
            pdf_pages_parsed=10,
            documents_created=10,
            chunks_created=12,
            chunks_stored=12,
            collection_name="healthcare_documents",
        )

        with patch("backend.app.api.routes.rebuild_vector_store", return_value=fake_result):
            response = self.client.post("/ingest/rebuild")

        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(body["pdf_pages_parsed"], 10)
        self.assertEqual(body["chunks_created"], 12)
        self.assertEqual(body["collection_name"], "healthcare_documents")

    def test_documents_endpoint_lists_raw_pdfs(self):
        with patch("backend.app.api.routes.get_settings") as mock_settings:
            mock_settings.return_value.raw_data_dir.glob.return_value = [
                type("PathLike", (), {"name": "policy.pdf", "__lt__": lambda self, other: self.name < other.name})(),
                type("PathLike", (), {"name": "benefits.pdf", "__lt__": lambda self, other: self.name < other.name})(),
            ]

            response = self.client.get("/documents")

        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(
            [document["file_name"] for document in body],
            ["benefits.pdf", "policy.pdf"],
        )


if __name__ == "__main__":
    unittest.main()
