from pathlib import Path
import tempfile
import unittest

from langchain_core.documents import Document

from backend.app.rag.retriever import retrieve_relevant_chunks
from backend.app.rag.vector_store import store_documents_in_chroma
from tests.test_vector_store import FakeEmbeddings


class RetrieverTests(unittest.TestCase):
    def test_retrieve_relevant_chunks_returns_source_metadata(self):
        documents = [
            Document(
                page_content="Blood pressure monitoring is important for hypertension.",
                metadata={
                    "chunk_id": "hypertension.pdf:page-3:chunk-1",
                    "file_name": "hypertension.pdf",
                    "source": "hypertension.pdf",
                    "page_number": 3,
                },
            ),
            Document(
                page_content="Glucose monitoring is important for diabetes care.",
                metadata={
                    "chunk_id": "diabetes.pdf:page-2:chunk-1",
                    "file_name": "diabetes.pdf",
                    "source": "diabetes.pdf",
                    "page_number": 2,
                },
            ),
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            store_documents_in_chroma(
                documents=documents,
                embeddings=FakeEmbeddings(),
                persist_directory=Path(temp_dir),
                collection_name="test_retrieval_collection",
            )

            results = retrieve_relevant_chunks(
                query="blood pressure",
                embeddings=FakeEmbeddings(),
                persist_directory=Path(temp_dir),
                collection_name="test_retrieval_collection",
                top_k=2,
            )

            self.assertEqual(len(results), 2)
            self.assertIn(results[0].file_name, {"hypertension.pdf", "diabetes.pdf"})
            self.assertIsInstance(results[0].score, float)
            self.assertIn("chunk_id", results[0].metadata)
            self.assertGreater(results[0].page_number, 0)

    def test_retrieve_relevant_chunks_can_filter_by_file_name(self):
        documents = [
            Document(
                page_content="Prior authorization requires supporting notes.",
                metadata={
                    "chunk_id": "policy.pdf:page-3:chunk-1",
                    "file_name": "policy.pdf",
                    "page_number": 3,
                },
            ),
            Document(
                page_content="Electric fields describe forces on charges.",
                metadata={
                    "chunk_id": "physics.pdf:page-1:chunk-1",
                    "file_name": "physics.pdf",
                    "page_number": 1,
                },
            ),
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            store_documents_in_chroma(
                documents=documents,
                embeddings=FakeEmbeddings(),
                persist_directory=Path(temp_dir),
                collection_name="test_filtered_retrieval_collection",
            )

            results = retrieve_relevant_chunks(
                query="authorization notes",
                embeddings=FakeEmbeddings(),
                persist_directory=Path(temp_dir),
                collection_name="test_filtered_retrieval_collection",
                top_k=2,
                file_name="policy.pdf",
            )

            self.assertTrue(results)
            self.assertTrue(all(result.file_name == "policy.pdf" for result in results))

    def test_retrieve_relevant_chunks_rejects_empty_query(self):
        with self.assertRaises(ValueError):
            retrieve_relevant_chunks(
                query=" ",
                embeddings=FakeEmbeddings(),
                persist_directory=Path("data/vector_db/chroma"),
                collection_name="test_retrieval_collection",
            )

    def test_retrieve_relevant_chunks_rejects_invalid_top_k(self):
        with self.assertRaises(ValueError):
            retrieve_relevant_chunks(
                query="diabetes",
                embeddings=FakeEmbeddings(),
                persist_directory=Path("data/vector_db/chroma"),
                collection_name="test_retrieval_collection",
                top_k=0,
            )


if __name__ == "__main__":
    unittest.main()
