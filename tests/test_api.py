import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from backend.app.main import app
from backend.app.rag.answer_generator import GroundedAnswer, SourceCitation


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

        with patch("backend.app.api.routes.answer_question", return_value=fake_answer):
            response = self.client.post(
                "/ask",
                json={"question": "How should hypertension be monitored?"},
            )

        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(body["answer"], fake_answer.answer)
        self.assertEqual(body["citations"][0]["file_name"], "hypertension-guide.pdf")
        self.assertEqual(body["citations"][0]["page_number"], 4)

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


if __name__ == "__main__":
    unittest.main()
