from pathlib import Path
import tempfile
import unittest

from pypdf import PdfWriter

from backend.app.ingestion.pdf_loader import (
    load_pdf_pages,
    load_pdfs_from_directory,
)


class PDFLoaderTests(unittest.TestCase):
    def _create_blank_pdf(self, directory: Path, file_name: str = "sample.pdf") -> Path:
        pdf_path = directory / file_name
        writer = PdfWriter()
        writer.add_blank_page(width=200, height=200)

        with pdf_path.open("wb") as pdf_file:
            writer.write(pdf_file)

        return pdf_path

    def test_load_pdf_pages_returns_page_metadata(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            pdf_path = self._create_blank_pdf(Path(temp_dir), "clinical-note.pdf")

            pages = load_pdf_pages(pdf_path)

            self.assertEqual(len(pages), 1)
            self.assertEqual(pages[0].file_name, "clinical-note.pdf")
            self.assertEqual(pages[0].page_number, 1)
            self.assertEqual(pages[0].total_pages, 1)
            self.assertEqual(pages[0].text, "")

    def test_load_pdf_pages_rejects_non_pdf_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            text_path = Path(temp_dir) / "not-a-pdf.txt"
            text_path.write_text("not a pdf")

            with self.assertRaises(ValueError):
                load_pdf_pages(text_path)

    def test_load_pdfs_from_directory_loads_all_pdf_pages(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            directory = Path(temp_dir)
            self._create_blank_pdf(directory, "a.pdf")
            self._create_blank_pdf(directory, "b.pdf")

            pages = load_pdfs_from_directory(directory)

            self.assertEqual(len(pages), 2)
            self.assertEqual([page.file_name for page in pages], ["a.pdf", "b.pdf"])


if __name__ == "__main__":
    unittest.main()

