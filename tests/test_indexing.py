import unittest
from unittest.mock import Mock, patch

from backend.app.core.settings import Settings
from backend.app.rag.indexing import rebuild_vector_store


class IndexingTests(unittest.TestCase):
    @patch("backend.app.rag.indexing.store_documents_in_chroma")
    @patch("backend.app.rag.indexing.create_openai_embeddings")
    @patch("backend.app.rag.indexing.save_processed_artifacts")
    @patch("backend.app.rag.indexing.split_documents")
    @patch("backend.app.rag.indexing.pages_to_documents")
    @patch("backend.app.rag.indexing.load_pdfs_from_directory")
    def test_rebuild_vector_store_returns_indexing_summary(
        self,
        mock_load_pages,
        mock_pages_to_documents,
        mock_split_documents,
        mock_save_processed_artifacts,
        mock_create_embeddings,
        mock_store_documents,
    ):
        mock_load_pages.return_value = ["page"]
        mock_pages_to_documents.return_value = ["document"]
        mock_split_documents.return_value = ["chunk"]
        mock_create_embeddings.return_value = Mock()
        mock_vector_store = Mock()
        mock_vector_store._collection.count.return_value = 1
        mock_store_documents.return_value = mock_vector_store

        result = rebuild_vector_store(Settings())

        self.assertEqual(result.pdf_pages_parsed, 1)
        self.assertEqual(result.documents_created, 1)
        self.assertEqual(result.chunks_created, 1)
        self.assertEqual(result.chunks_stored, 1)
        mock_save_processed_artifacts.assert_called_once()
        mock_create_embeddings.assert_called_once()
        mock_store_documents.assert_called_once()

    @patch("backend.app.rag.indexing.create_openai_embeddings")
    @patch("backend.app.rag.indexing.save_processed_artifacts")
    @patch("backend.app.rag.indexing.split_documents")
    @patch("backend.app.rag.indexing.pages_to_documents")
    @patch("backend.app.rag.indexing.load_pdfs_from_directory")
    def test_rebuild_vector_store_skips_embeddings_when_no_chunks(
        self,
        mock_load_pages,
        mock_pages_to_documents,
        mock_split_documents,
        mock_save_processed_artifacts,
        mock_create_embeddings,
    ):
        mock_load_pages.return_value = []
        mock_pages_to_documents.return_value = []
        mock_split_documents.return_value = []

        result = rebuild_vector_store(Settings())

        self.assertEqual(result.chunks_created, 0)
        self.assertEqual(result.chunks_stored, 0)
        mock_save_processed_artifacts.assert_called_once()
        mock_create_embeddings.assert_not_called()


if __name__ == "__main__":
    unittest.main()
