from pathlib import Path
import tempfile
import unittest

from backend.app.ingestion.unstructured_loader import (
    UnstructuredParserUnavailableError,
    _load_partition_pdf,
    load_pdf_pages_with_unstructured,
    load_pdfs_from_directory_with_unstructured,
)


class FakeMetadata:
    def __init__(self, page_number):
        self.page_number = page_number


class FakeElement:
    def __init__(self, text, page_number=None):
        self.text = text
        self.metadata = FakeMetadata(page_number) if page_number else object()

    def __str__(self):
        return self.text


def fake_partitioner(filename):
    return [
        FakeElement("Patient instructions", page_number=1),
        FakeElement("Follow up in 7 days", page_number=1),
        FakeElement("Medication list", page_number=2),
    ]


class UnstructuredLoaderTests(unittest.TestCase):
    def test_load_pdf_pages_with_unstructured_groups_elements_by_page(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            pdf_path = Path(temp_dir) / "patient.pdf"
            pdf_path.write_bytes(b"%PDF-1.4 fake test pdf")

            pages = load_pdf_pages_with_unstructured(
                pdf_path=pdf_path,
                partitioner=fake_partitioner,
            )

            self.assertEqual(len(pages), 2)
            self.assertEqual(pages[0].file_name, "patient.pdf")
            self.assertEqual(pages[0].page_number, 1)
            self.assertEqual(pages[0].total_pages, 2)
            self.assertIn("Patient instructions", pages[0].text)
            self.assertIn("Follow up", pages[0].text)
            self.assertEqual(pages[1].page_number, 2)

    def test_load_pdf_pages_with_unstructured_rejects_non_pdf_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            text_path = Path(temp_dir) / "patient.txt"
            text_path.write_text("not a pdf")

            with self.assertRaises(ValueError):
                load_pdf_pages_with_unstructured(
                    pdf_path=text_path,
                    partitioner=fake_partitioner,
                )

    def test_load_pdfs_from_directory_with_unstructured_loads_all_pdfs(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            directory = Path(temp_dir)
            (directory / "a.pdf").write_bytes(b"%PDF-1.4 fake a")
            (directory / "b.pdf").write_bytes(b"%PDF-1.4 fake b")

            pages = load_pdfs_from_directory_with_unstructured(
                directory=directory,
                partitioner=fake_partitioner,
            )

            self.assertEqual(len(pages), 4)

    def test_load_partition_pdf_reports_missing_optional_dependencies(self):
        try:
            _load_partition_pdf()
        except UnstructuredParserUnavailableError as error:
            self.assertIn("Unstructured PDF parsing is not fully available", str(error))


if __name__ == "__main__":
    unittest.main()

