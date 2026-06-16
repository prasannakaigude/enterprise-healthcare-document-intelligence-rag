import json
from pathlib import Path
import tempfile
import unittest

from backend.app.core.conversation_logger import (
    build_conversation_log_record,
    write_conversation_log,
)
from backend.app.core.settings import Settings
from backend.app.rag.answer_generator import SourceCitation


class ConversationLoggerTests(unittest.TestCase):
    def _settings(self, log_path: Path, raw_text: bool = False) -> Settings:
        return Settings(
            conversation_log_path=log_path,
            log_conversations=True,
            log_raw_conversation_text=raw_text,
        )

    def test_build_conversation_log_record_uses_hashes_by_default(self):
        record = build_conversation_log_record(
            question="What is covered?",
            answer="The document says coverage depends on eligibility.",
            citations=[
                SourceCitation(
                    file_name="policy.pdf",
                    page_number=2,
                    chunk_id="policy.pdf:page-2:chunk-1",
                )
            ],
            settings=self._settings(Path("conversation_logs.jsonl")),
        )

        self.assertIn("question_hash", record)
        self.assertIn("answer_hash", record)
        self.assertNotIn("question", record)
        self.assertNotIn("answer", record)
        self.assertEqual(record["citation_count"], 1)
        self.assertFalse(record["raw_text_saved"])

    def test_build_conversation_log_record_can_include_raw_text(self):
        record = build_conversation_log_record(
            question="What is covered?",
            answer="Eligibility is checked first.",
            citations=[],
            settings=self._settings(Path("conversation_logs.jsonl"), raw_text=True),
        )

        self.assertEqual(record["question"], "What is covered?")
        self.assertEqual(record["answer"], "Eligibility is checked first.")
        self.assertTrue(record["raw_text_saved"])

    def test_write_conversation_log_appends_jsonl_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            log_path = Path(temp_dir) / "conversation_logs.jsonl"

            written_path = write_conversation_log(
                question="What is covered?",
                answer="Eligibility is checked first.",
                citations=[],
                settings=self._settings(log_path),
            )

            self.assertEqual(written_path, log_path)
            lines = log_path.read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(lines), 1)
            record = json.loads(lines[0])
            self.assertEqual(record["citation_count"], 0)

    def test_write_conversation_log_can_be_disabled(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            log_path = Path(temp_dir) / "conversation_logs.jsonl"
            settings = Settings(
                conversation_log_path=log_path,
                log_conversations=False,
            )

            written_path = write_conversation_log(
                question="What is covered?",
                answer="Eligibility is checked first.",
                citations=[],
                settings=settings,
            )

            self.assertIsNone(written_path)
            self.assertFalse(log_path.exists())


if __name__ == "__main__":
    unittest.main()
