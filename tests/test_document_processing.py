import unittest
import warnings


warnings.filterwarnings("ignore", message="urllib3 v2 only supports OpenSSL.*")

from langchain_core.documents import Document

from backend.app.ingestion.pdf_loader import ParsedPDFPage
from backend.app.rag.document_processing import pages_to_documents, split_documents


class DocumentProcessingTests(unittest.TestCase):
    def test_pages_to_documents_preserves_citation_metadata(self):
        pages = [
            ParsedPDFPage(
                text="Patient discharge instructions include follow-up in 7 days.",
                file_name="patient-guide.pdf",
                file_path="data/raw/patient-guide.pdf",
                page_number=2,
                total_pages=5,
            )
        ]

        documents = pages_to_documents(pages)

        self.assertEqual(len(documents), 1)
        self.assertEqual(
            documents[0].page_content,
            "Patient discharge instructions include follow-up in 7 days.",
        )
        self.assertEqual(documents[0].metadata["source"], "patient-guide.pdf")
        self.assertEqual(documents[0].metadata["file_name"], "patient-guide.pdf")
        self.assertEqual(documents[0].metadata["page_number"], 2)
        self.assertEqual(documents[0].metadata["total_pages"], 5)

    def test_pages_to_documents_skips_empty_text(self):
        pages = [
            ParsedPDFPage(
                text="   ",
                file_name="scanned.pdf",
                file_path="data/raw/scanned.pdf",
                page_number=1,
                total_pages=1,
            )
        ]

        documents = pages_to_documents(pages)

        self.assertEqual(documents, [])

    def test_split_documents_creates_chunks_with_metadata(self):
        document = Document(
            page_content=(
                "Diabetes care plan includes diet monitoring, glucose checks, "
                "exercise, medication adherence, and follow-up appointments."
            ),
            metadata={
                "source": "care-plan.pdf",
                "file_name": "care-plan.pdf",
                "file_path": "data/raw/care-plan.pdf",
                "page_number": 1,
                "total_pages": 1,
            },
        )

        chunks = split_documents([document], chunk_size=60, chunk_overlap=10)

        self.assertGreater(len(chunks), 1)
        self.assertEqual(chunks[0].metadata["file_name"], "care-plan.pdf")
        self.assertEqual(chunks[0].metadata["page_number"], 1)
        self.assertEqual(chunks[0].metadata["chunk_number"], 1)
        self.assertEqual(chunks[0].metadata["chunk_id"], "care-plan.pdf:page-1:chunk-1")

    def test_split_documents_rejects_invalid_chunk_settings(self):
        with self.assertRaises(ValueError):
            split_documents([], chunk_size=0)

        with self.assertRaises(ValueError):
            split_documents([], chunk_size=100, chunk_overlap=-1)

        with self.assertRaises(ValueError):
            split_documents([], chunk_size=100, chunk_overlap=100)


if __name__ == "__main__":
    unittest.main()
