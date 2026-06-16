import unittest
from unittest.mock import Mock, patch

import requests

from frontend.api_client import (
    BackendAPIError,
    ask_backend,
    list_documents_backend,
    rebuild_vector_store_backend,
)


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

        result = ask_backend(
            "How should hypertension be monitored?",
            file_name="hypertension.pdf",
        )

        self.assertEqual(result["answer"], "Monitor blood pressure regularly.")
        self.assertEqual(result["citations"][0]["file_name"], "hypertension.pdf")
        mock_post.assert_called_once()
        self.assertEqual(
            mock_post.call_args.kwargs["json"]["file_name"],
            "hypertension.pdf",
        )

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

    @patch("frontend.api_client.requests.post")
    def test_rebuild_vector_store_backend_returns_json_response(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "pdf_pages_parsed": 10,
            "documents_created": 10,
            "chunks_created": 12,
            "chunks_stored": 12,
            "collection_name": "healthcare_documents",
        }
        mock_post.return_value = mock_response

        result = rebuild_vector_store_backend()

        self.assertEqual(result["chunks_created"], 12)
        mock_post.assert_called_once()

    @patch("frontend.api_client.requests.get")
    def test_list_documents_backend_returns_json_response(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"file_name": "policy.pdf"}]
        mock_get.return_value = mock_response

        result = list_documents_backend()

        self.assertEqual(result[0]["file_name"], "policy.pdf")
        mock_get.assert_called_once()
