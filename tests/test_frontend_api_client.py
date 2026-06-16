import unittest
from unittest.mock import Mock, patch

import requests

from frontend.api_client import BackendAPIError, ask_backend


class FrontendAPIClientTests(unittest.TestCase):
    @patch("frontend.api_client.requests.post")
    def test_ask_backend_returns_json_response(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "answer": "Monitor blood pressure regularly.",
            "citations": [
                {
                    "file_name": "hypertension.pdf",
                    "page_number": 2,
                    "chunk_id": "hypertension.pdf:page-2:chunk-1",
                }
            ],
        }
        mock_post.return_value = mock_response

        result = ask_backend("How should hypertension be monitored?")

        self.assertEqual(result["answer"], "Monitor blood pressure regularly.")
        self.assertEqual(result["citations"][0]["file_name"], "hypertension.pdf")
        mock_post.assert_called_once()

    def test_ask_backend_rejects_empty_question(self):
        with self.assertRaises(ValueError):
            ask_backend(" ")

    @patch("frontend.api_client.requests.post")
    def test_ask_backend_handles_connection_error(self, mock_post):
        mock_post.side_effect = requests.ConnectionError("backend down")

        with self.assertRaises(BackendAPIError) as context:
            ask_backend("What does the document say?")

        self.assertIn("Could not connect", str(context.exception))

    @patch("frontend.api_client.requests.post")
    def test_ask_backend_handles_error_response(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.json.return_value = {"detail": "OPENAI_API_KEY is not set."}
        mock_response.text = "OPENAI_API_KEY is not set."
        mock_post.return_value = mock_response

        with self.assertRaises(BackendAPIError) as context:
            ask_backend("What does the document say?")

        self.assertIn("OPENAI_API_KEY is not set", str(context.exception))

