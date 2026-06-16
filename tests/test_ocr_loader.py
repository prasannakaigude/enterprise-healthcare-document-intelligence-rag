from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from backend.app.ingestion.ocr_loader import (
    OCRUnavailableError,
    load_pdf_pages_with_ocr,
    load_pdf_pages_with_ocr_fallback,
    load_pdfs_from_directory_with_ocr_fallback,
)
from backend.app.ingestion.pdf_loader import ParsedPDFPage


class FakeImage:
    def __init__(self, text):
        self.text = text


def fake_image_converter(path):
    return [FakeImage("Scanned discharge instructions"), FakeImage("Follow up in 7 days")]


def fake_image_to_text(image):
    return image.text


class OCRLoaderTests(unittest.TestCase):
    def test_load_pdf_pages_with_ocr_extracts_text_and_metadata(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            pdf_path = Path(temp_dir) / "scan.pdf"
            pdf_path.write_bytes(b"%PDF-1.4 fake scan")

            pages = load_pdf_pages_with_ocr(
                pdf_path=pdf_path,
                image_converter=fake_image_converter,
                image_to_text=fake_image_to_text,
            )

            self.assertEqual(len(pages), 2)
            self.assertEqual(pages[0].file_name, "scan.pdf")
            self.assertEqual(pages[0].page_number, 1)
            self.assertEqual(pages[0].total_pages, 2)
            self.assertIn("Scanned discharge", pages[0].text)

    def test_load_pdf_pages_with_ocr_rejects_non_pdf_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            text_path = Path(temp_dir) / "scan.txt"
            text_path.write_text("not a pdf")

            with self.assertRaises(ValueError):
                load_pdf_pages_with_ocr(
                    pdf_path=text_path,
                    image_converter=fake_image_converter,
                    image_to_text=fake_image_to_text,
                )

    def test_ocr_fallback_keeps_pypdf_text_when_available(self):
        pypdf_pages = [
            ParsedPDFPage(
                text="Existing embedded text",
                file_name="mixed.pdf",
                file_path="data/raw/mixed.pdf",
                page_number=1,
                total_pages=2,
            ),
            ParsedPDFPage(
                text="",
                file_name="mixed.pdf",
                file_path="data/raw/mixed.pdf",
                page_number=2,
                total_pages=2,
            ),
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            pdf_path = Path(temp_dir) / "mixed.pdf"
            pdf_path.write_bytes(b"%PDF-1.4 fake mixed")

            with patch(
                "backend.app.ingestion.ocr_loader.load_pdf_pages",
                return_value=pypdf_pages,
            ):
                pages = load_pdf_pages_with_ocr_fallback(
                    pdf_path=pdf_path,
                    image_converter=fake_image_converter,
                    image_to_text=fake_image_to_text,
                )

            self.assertEqual(pages[0].text, "Existing embedded text")
            self.assertEqual(pages[1].text, "Follow up in 7 days")

    def test_directory_ocr_fallback_loads_all_pdfs(self):
        pypdf_pages = [
            ParsedPDFPage(
                text="",
                file_name="scan.pdf",
                file_path="scan.pdf",
                page_number=1,
                total_pages=1,
            )
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            directory = Path(temp_dir)
            (directory / "a.pdf").write_bytes(b"%PDF-1.4 fake a")
            (directory / "b.pdf").write_bytes(b"%PDF-1.4 fake b")

            with patch(
                "backend.app.ingestion.ocr_loader.load_pdf_pages",
                return_value=pypdf_pages,
            ):
                pages = load_pdfs_from_directory_with_ocr_fallback(
                    directory=directory,
                    image_converter=lambda path: [FakeImage(f"OCR text for {path}")],
                    image_to_text=fake_image_to_text,
                )

            self.assertEqual(len(pages), 2)

    def test_ocr_reports_converter_dependency_errors(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            pdf_path = Path(temp_dir) / "scan.pdf"
            pdf_path.write_bytes(b"%PDF-1.4 fake scan")

            def failing_converter(path):
                raise RuntimeError("poppler missing")

            with self.assertRaises(OCRUnavailableError):
                load_pdf_pages_with_ocr(
                    pdf_path=pdf_path,
                    image_converter=failing_converter,
                    image_to_text=fake_image_to_text,
                )


if __name__ == "__main__":
    unittest.main()
