from pathlib import Path
import tempfile
import unittest

from backend.app.storage.s3_storage import (
    build_s3_key,
    create_s3_client,
    list_s3_documents,
    upload_pdf_to_s3,
    upload_pdfs_to_s3,
)


class FakePaginator:
    def paginate(self, Bucket, Prefix):
        return [
            {
                "Contents": [
                    {
                        "Key": f"{Prefix}/policy.pdf",
                        "Size": 2048,
                        "LastModified": "2026-01-01 00:00:00+00:00",
                    },
                    {
                        "Key": f"{Prefix}/",
                        "Size": 0,
                        "LastModified": "2026-01-01 00:00:00+00:00",
                    },
                ]
            }
        ]


class FakeS3Client:
    def __init__(self):
        self.uploads = []

    def upload_file(self, local_path, bucket_name, key):
        self.uploads.append((local_path, bucket_name, key))

    def get_paginator(self, name):
        if name != "list_objects_v2":
            raise ValueError(name)
        return FakePaginator()


class FakeBoto3:
    def __init__(self):
        self.client_calls = []

    def client(self, service_name, region_name):
        self.client_calls.append((service_name, region_name))
        return FakeS3Client()


class S3StorageTests(unittest.TestCase):
    def test_build_s3_key_uses_prefix_and_file_name(self):
        key = build_s3_key("/tmp/private/patient-handbook.pdf", "documents/raw/")

        self.assertEqual(key, "documents/raw/patient-handbook.pdf")

    def test_create_s3_client_uses_boto3_s3_client(self):
        fake_boto3 = FakeBoto3()

        client = create_s3_client("us-east-1", boto3_module=fake_boto3)

        self.assertIsInstance(client, FakeS3Client)
        self.assertEqual(fake_boto3.client_calls, [("s3", "us-east-1")])

    def test_upload_pdf_to_s3_uploads_and_returns_key(self):
        fake_client = FakeS3Client()

        with tempfile.TemporaryDirectory() as temp_dir:
            pdf_path = Path(temp_dir) / "clinical-policy.pdf"
            pdf_path.write_text("fake pdf content")

            key = upload_pdf_to_s3(
                local_pdf_path=pdf_path,
                bucket_name="healthcare-rag-documents",
                prefix="healthcare-documents/raw",
                s3_client=fake_client,
            )

        self.assertEqual(key, "healthcare-documents/raw/clinical-policy.pdf")
        self.assertEqual(len(fake_client.uploads), 1)
        self.assertEqual(
            fake_client.uploads[0][1:],
            ("healthcare-rag-documents", "healthcare-documents/raw/clinical-policy.pdf"),
        )

    def test_upload_pdf_to_s3_rejects_non_pdf(self):
        fake_client = FakeS3Client()

        with tempfile.TemporaryDirectory() as temp_dir:
            text_path = Path(temp_dir) / "notes.txt"
            text_path.write_text("not a pdf")

            with self.assertRaises(ValueError):
                upload_pdf_to_s3(
                    local_pdf_path=text_path,
                    bucket_name="healthcare-rag-documents",
                    prefix="healthcare-documents/raw",
                    s3_client=fake_client,
                )

    def test_upload_pdfs_to_s3_uploads_multiple_files(self):
        fake_client = FakeS3Client()

        with tempfile.TemporaryDirectory() as temp_dir:
            first = Path(temp_dir) / "first.pdf"
            second = Path(temp_dir) / "second.pdf"
            first.write_text("first")
            second.write_text("second")

            keys = upload_pdfs_to_s3(
                pdf_paths=[first, second],
                bucket_name="healthcare-rag-documents",
                prefix="raw",
                s3_client=fake_client,
            )

        self.assertEqual(keys, ["raw/first.pdf", "raw/second.pdf"])
        self.assertEqual(len(fake_client.uploads), 2)

    def test_list_s3_documents_returns_document_metadata(self):
        fake_client = FakeS3Client()

        documents = list_s3_documents(
            bucket_name="healthcare-rag-documents",
            prefix="healthcare-documents/raw",
            s3_client=fake_client,
        )

        self.assertEqual(len(documents), 1)
        self.assertEqual(documents[0].bucket, "healthcare-rag-documents")
        self.assertEqual(documents[0].key, "healthcare-documents/raw/policy.pdf")
        self.assertEqual(documents[0].size_bytes, 2048)


if __name__ == "__main__":
    unittest.main()
