from io import BytesIO
from pathlib import Path
import tempfile
import unittest

from frontend.document_upload import sanitize_pdf_filename, save_uploaded_pdf


class FakeUploadedFile(BytesIO):
    def __init__(self, name: str, content: bytes):
        super().__init__(content)
        self.name = name


class DocumentUploadTests(unittest.TestCase):
    def test_sanitize_pdf_filename_keeps_safe_pdf_name(self):
        self.assertEqual(
            sanitize_pdf_filename("member policy.pdf"),
            "member_policy.pdf",
        )

    def test_sanitize_pdf_filename_rejects_non_pdf(self):
        with self.assertRaises(ValueError):
            sanitize_pdf_filename("notes.txt")

    def test_save_uploaded_pdf_writes_to_raw_data_dir(self):
        uploaded_file = FakeUploadedFile("care guide.pdf", b"fake pdf bytes")

        with tempfile.TemporaryDirectory() as temp_dir:
            saved_path = save_uploaded_pdf(
                uploaded_file,
                raw_data_dir=Path(temp_dir),
            )

            self.assertEqual(saved_path.name, "care_guide.pdf")
            self.assertEqual(saved_path.read_bytes(), b"fake pdf bytes")

    def test_save_uploaded_pdf_does_not_overwrite_existing_file(self):
        first_file = FakeUploadedFile("policy.pdf", b"first")
        second_file = FakeUploadedFile("policy.pdf", b"second")

        with tempfile.TemporaryDirectory() as temp_dir:
            raw_data_dir = Path(temp_dir)
            first_path = save_uploaded_pdf(first_file, raw_data_dir=raw_data_dir)
            second_path = save_uploaded_pdf(second_file, raw_data_dir=raw_data_dir)

            self.assertEqual(first_path.name, "policy.pdf")
            self.assertEqual(second_path.name, "policy_1.pdf")
            self.assertEqual(first_path.read_bytes(), b"first")
            self.assertEqual(second_path.read_bytes(), b"second")


if __name__ == "__main__":
    unittest.main()
