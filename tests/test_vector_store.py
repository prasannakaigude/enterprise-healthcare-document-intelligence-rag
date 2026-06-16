from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings

from backend.app.core.settings import Settings, get_settings
from backend.app.rag.vector_store import (
    create_openai_embeddings,
    store_documents_in_chroma,
)


class FakeEmbeddings(Embeddings):
    """Deterministic local embeddings for tests."""

    def embed_documents(self, texts):
        return [self._embed(text) for text in texts]

    def embed_query(self, text):
        return self._embed(text)

    def _embed(self, text):
        length = float(len(text))
        vowels = float(sum(1 for char in text.lower() if char in "aeiou"))
        consonants = float(
            sum(1 for char in text.lower() if char.isalpha() and char not in "aeiou")
        )
        return [length, vowels, consonants]


class VectorStoreTests(unittest.TestCase):
    def test_settings_include_embedding_and_chroma_defaults(self):
        settings = get_settings()

        self.assertEqual(settings.embedding_model, "text-embedding-3-small")
        self.assertEqual(settings.chroma_collection_name, "healthcare_documents")

    def test_create_openai_embeddings_requires_api_key(self):
        with patch.dict("os.environ", {}, clear=True):
            with self.assertRaises(ValueError):
                create_openai_embeddings(Settings())

    def test_store_documents_in_chroma_persists_chunks(self):
        documents = [
            Document(
                page_content="Hypertension care plan includes blood pressure checks.",
                metadata={
                    "chunk_id": "care.pdf:page-1:chunk-1",
                    "file_name": "care.pdf",
                    "page_number": 1,
                },
            ),
            Document(
                page_content="Diabetes care plan includes glucose monitoring.",
                metadata={
                    "chunk_id": "care.pdf:page-2:chunk-1",
                    "file_name": "care.pdf",
                    "page_number": 2,
                },
            ),
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            vector_store = store_documents_in_chroma(
                documents=documents,
                embeddings=FakeEmbeddings(),
                persist_directory=Path(temp_dir),
                collection_name="test_healthcare_documents",
            )

            self.assertEqual(vector_store._collection.count(), 2)

            results = vector_store.similarity_search("blood pressure", k=1)

            self.assertEqual(len(results), 1)
            self.assertIn("care plan", results[0].page_content)
            self.assertIn("file_name", results[0].metadata)
            self.assertIn("page_number", results[0].metadata)


if __name__ == "__main__":
    unittest.main()
