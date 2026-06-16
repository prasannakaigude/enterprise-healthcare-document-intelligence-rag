import json
from pathlib import Path
import tempfile
import unittest

from langchain_core.documents import Document

from backend.app.ingestion.pdf_loader import ParsedPDFPage
from backend.app.rag.processed_artifacts import save_processed_artifacts


class ProcessedArtifactsTests(unittest.TestCase):
    def test_save_processed_artifacts_writes_pages_and_chunks_jsonl(self):
        pages = [
            ParsedPDFPage(
                text="Prior authorization is required.",
                file_name="policy.pdf",
                file_path="data/raw/policy.pdf",
                page_number=3,
                total_pages=10,
            )
        ]
        chunks = [
            Document(
                page_content="Prior authorization is required.",
                metadata={
                    "chunk_id": "policy.pdf:page-3:chunk-1",
                    "file_name": "policy.pdf",
                    "page_number": 3,
                },
            )
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            pages_path, chunks_path = save_processed_artifacts(
                pages=pages,
                chunks=chunks,
                processed_data_dir=Path(temp_dir),
            )

            page_records = [
                json.loads(line)
                for line in pages_path.read_text(encoding="utf-8").splitlines()
            ]
            chunk_records = [
                json.loads(line)
                for line in chunks_path.read_text(encoding="utf-8").splitlines()
            ]

        self.assertEqual(page_records[0]["file_name"], "policy.pdf")
        self.assertEqual(page_records[0]["page_number"], 3)
        self.assertEqual(chunk_records[0]["metadata"]["chunk_id"], "policy.pdf:page-3:chunk-1")
        self.assertIn("Prior authorization", chunk_records[0]["text"])


if __name__ == "__main__":
    unittest.main()
